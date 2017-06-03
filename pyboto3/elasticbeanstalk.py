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

def abort_environment_update(EnvironmentId=None, EnvironmentName=None):
    """
    Cancels in-progress environment configuration update or application version deployment.
    See also: AWS API Documentation
    
    Examples
    The following code aborts a running application version deployment for an environment named my-env:
    Expected Output:
    
    :example: response = client.abort_environment_update(
        EnvironmentId='string',
        EnvironmentName='string'
    )
    
    
    :type EnvironmentId: string
    :param EnvironmentId: This specifies the ID of the environment with the in-progress update that you want to cancel.

    :type EnvironmentName: string
    :param EnvironmentName: This specifies the name of the environment with the in-progress update that you want to cancel.

    :return: response = client.abort_environment_update(
        EnvironmentName='my-env',
    )
    
    print(response)
    
    
    """
    pass

def apply_environment_managed_action(EnvironmentName=None, EnvironmentId=None, ActionId=None):
    """
    Applies a scheduled managed action immediately. A managed action can be applied only if its status is Scheduled . Get the status and action ID of a managed action with  DescribeEnvironmentManagedActions .
    See also: AWS API Documentation
    
    
    :example: response = client.apply_environment_managed_action(
        EnvironmentName='string',
        EnvironmentId='string',
        ActionId='string'
    )
    
    
    :type EnvironmentName: string
    :param EnvironmentName: The name of the target environment.

    :type EnvironmentId: string
    :param EnvironmentId: The environment ID of the target environment.

    :type ActionId: string
    :param ActionId: [REQUIRED]
            The action ID of the scheduled managed action to execute.
            

    :rtype: dict
    :return: {
        'ActionId': 'string',
        'ActionDescription': 'string',
        'ActionType': 'InstanceRefresh'|'PlatformUpdate'|'Unknown',
        'Status': 'string'
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

def check_dns_availability(CNAMEPrefix=None):
    """
    Checks if the specified CNAME is available.
    See also: AWS API Documentation
    
    Examples
    The following operation checks the availability of the subdomain my-cname:
    Expected Output:
    
    :example: response = client.check_dns_availability(
        CNAMEPrefix='string'
    )
    
    
    :type CNAMEPrefix: string
    :param CNAMEPrefix: [REQUIRED]
            The prefix used when this CNAME is reserved.
            

    :rtype: dict
    :return: {
        'Available': True|False,
        'FullyQualifiedCNAME': 'string'
    }
    
    
    """
    pass

def compose_environments(ApplicationName=None, GroupName=None, VersionLabels=None):
    """
    Create or update a group of environments that each run a separate component of a single application. Takes a list of version labels that specify application source bundles for each of the environments to create or update. The name of each environment and other required information must be included in the source bundles in an environment manifest named env.yaml . See Compose Environments for details.
    See also: AWS API Documentation
    
    
    :example: response = client.compose_environments(
        ApplicationName='string',
        GroupName='string',
        VersionLabels=[
            'string',
        ]
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: The name of the application to which the specified source bundles belong.

    :type GroupName: string
    :param GroupName: The name of the group to which the target environments belong. Specify a group name only if the environment name defined in each target environment's manifest ends with a + (plus) character. See Environment Manifest (env.yaml) for details.

    :type VersionLabels: list
    :param VersionLabels: A list of version labels, specifying one or more application source bundles that belong to the target application. Each source bundle must include an environment manifest that specifies the name of the environment and the name of the solution stack to use, and optionally can specify environment links to create.
            (string) --
            

    :rtype: dict
    :return: {
        'Environments': [
            {
                'EnvironmentName': 'string',
                'EnvironmentId': 'string',
                'ApplicationName': 'string',
                'VersionLabel': 'string',
                'SolutionStackName': 'string',
                'PlatformArn': 'string',
                'TemplateName': 'string',
                'Description': 'string',
                'EndpointURL': 'string',
                'CNAME': 'string',
                'DateCreated': datetime(2015, 1, 1),
                'DateUpdated': datetime(2015, 1, 1),
                'Status': 'Launching'|'Updating'|'Ready'|'Terminating'|'Terminated',
                'AbortableOperationInProgress': True|False,
                'Health': 'Green'|'Yellow'|'Red'|'Grey',
                'HealthStatus': 'NoData'|'Unknown'|'Pending'|'Ok'|'Info'|'Warning'|'Degraded'|'Severe',
                'Resources': {
                    'LoadBalancer': {
                        'LoadBalancerName': 'string',
                        'Domain': 'string',
                        'Listeners': [
                            {
                                'Protocol': 'string',
                                'Port': 123
                            },
                        ]
                    }
                },
                'Tier': {
                    'Name': 'string',
                    'Type': 'string',
                    'Version': 'string'
                },
                'EnvironmentLinks': [
                    {
                        'LinkName': 'string',
                        'EnvironmentName': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    Launching : Environment is in the process of initial deployment.
    Updating : Environment is in the process of updating its configuration settings or application version.
    Ready : Environment is available to have an action performed on it, such as update or terminate.
    Terminating : Environment is in the shut-down process.
    Terminated : Environment is not running.
    
    """
    pass

def create_application(ApplicationName=None, Description=None, ResourceLifecycleConfig=None):
    """
    Creates an application that has one configuration template named default and no application versions.
    See also: AWS API Documentation
    
    Examples
    The following operation creates a new application named my-app:
    Expected Output:
    
    :example: response = client.create_application(
        ApplicationName='string',
        Description='string',
        ResourceLifecycleConfig={
            'ServiceRole': 'string',
            'VersionLifecycleConfig': {
                'MaxCountRule': {
                    'Enabled': True|False,
                    'MaxCount': 123,
                    'DeleteSourceFromS3': True|False
                },
                'MaxAgeRule': {
                    'Enabled': True|False,
                    'MaxAgeInDays': 123,
                    'DeleteSourceFromS3': True|False
                }
            }
        }
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]
            The name of the application.
            Constraint: This name must be unique within your account. If the specified name already exists, the action returns an InvalidParameterValue error.
            

    :type Description: string
    :param Description: Describes the application.

    :type ResourceLifecycleConfig: dict
    :param ResourceLifecycleConfig: Specify an application resource lifecycle configuration to prevent your application from accumulating too many versions.
            ServiceRole (string) --The ARN of an IAM service role that Elastic Beanstalk has permission to assume.
            VersionLifecycleConfig (dict) --The application version lifecycle configuration.
            MaxCountRule (dict) --Specify a max count rule to restrict the number of application versions that are retained for an application.
            Enabled (boolean) -- [REQUIRED]Specify true to apply the rule, or false to disable it.
            MaxCount (integer) --Specify the maximum number of application versions to retain.
            DeleteSourceFromS3 (boolean) --Set to true to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.
            MaxAgeRule (dict) --Specify a max age rule to restrict the length of time that application versions are retained for an application.
            Enabled (boolean) -- [REQUIRED]Specify true to apply the rule, or false to disable it.
            MaxAgeInDays (integer) --Specify the number of days to retain an application versions.
            DeleteSourceFromS3 (boolean) --Set to true to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.
            
            

    :rtype: dict
    :return: {
        'Application': {
            'ApplicationName': 'string',
            'Description': 'string',
            'DateCreated': datetime(2015, 1, 1),
            'DateUpdated': datetime(2015, 1, 1),
            'Versions': [
                'string',
            ],
            'ConfigurationTemplates': [
                'string',
            ],
            'ResourceLifecycleConfig': {
                'ServiceRole': 'string',
                'VersionLifecycleConfig': {
                    'MaxCountRule': {
                        'Enabled': True|False,
                        'MaxCount': 123,
                        'DeleteSourceFromS3': True|False
                    },
                    'MaxAgeRule': {
                        'Enabled': True|False,
                        'MaxAgeInDays': 123,
                        'DeleteSourceFromS3': True|False
                    }
                }
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_application_version(ApplicationName=None, VersionLabel=None, Description=None, SourceBuildInformation=None, SourceBundle=None, BuildConfiguration=None, AutoCreateApplication=None, Process=None):
    """
    Creates an application version for the specified application. You can create an application version from a source bundle in Amazon S3, a commit in AWS CodeCommit, or the output of an AWS CodeBuild build as follows:
    Specify a commit in an AWS CodeCommit repository with SourceBuildInformation .
    Specify a build in an AWS CodeBuild with SourceBuildInformation and BuildConfiguration .
    Specify a source bundle in S3 with SourceBundle
    Omit both SourceBuildInformation and SourceBundle to use the default sample application.
    See also: AWS API Documentation
    
    Examples
    The following operation creates a new version (v1) of an application named my-app:
    Expected Output:
    
    :example: response = client.create_application_version(
        ApplicationName='string',
        VersionLabel='string',
        Description='string',
        SourceBuildInformation={
            'SourceType': 'Git'|'Zip',
            'SourceRepository': 'CodeCommit'|'S3',
            'SourceLocation': 'string'
        },
        SourceBundle={
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        BuildConfiguration={
            'ArtifactName': 'string',
            'CodeBuildServiceRole': 'string',
            'ComputeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
            'Image': 'string',
            'TimeoutInMinutes': 123
        },
        AutoCreateApplication=True|False,
        Process=True|False
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]
            The name of the application. If no application is found with this name, and AutoCreateApplication is false , returns an InvalidParameterValue error.
            

    :type VersionLabel: string
    :param VersionLabel: [REQUIRED]
            A label identifying this version.
            Constraint: Must be unique per application. If an application version already exists with this label for the specified application, AWS Elastic Beanstalk returns an InvalidParameterValue error.
            

    :type Description: string
    :param Description: Describes this version.

    :type SourceBuildInformation: dict
    :param SourceBuildInformation: Specify a commit in an AWS CodeCommit Git repository to use as the source code for the application version.
            SourceType (string) -- [REQUIRED]The type of repository.
            Git
            Zip
            SourceRepository (string) -- [REQUIRED]Location where the repository is stored.
            CodeCommit
            S3
            SourceLocation (string) -- [REQUIRED]The location of the source code, as a formatted string, depending on the value of SourceRepository
            For CodeCommit , the format is the repository name and commit ID, separated by a forward slash. For example, my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a .
            For S3 , the format is the S3 bucket name and object key, separated by a forward slash. For example, my-s3-bucket/Folders/my-source-file .
            

    :type SourceBundle: dict
    :param SourceBundle: The Amazon S3 bucket and key that identify the location of the source bundle for this version.
            Note
            The Amazon S3 bucket must be in the same region as the environment.
            Specify a source bundle in S3 or a commit in an AWS CodeCommit repository (with SourceBuildInformation ), but not both. If neither SourceBundle nor SourceBuildInformation are provided, Elastic Beanstalk uses a sample application.
            S3Bucket (string) --The Amazon S3 bucket where the data is located.
            S3Key (string) --The Amazon S3 key where the data is located.
            

    :type BuildConfiguration: dict
    :param BuildConfiguration: Settings for an AWS CodeBuild build.
            ArtifactName (string) --The name of the artifact of the CodeBuild build. If provided, Elastic Beanstalk stores the build artifact in the S3 location S3-bucket /resources/application-name /codebuild/codebuild-version-label -artifact-name .zip. If not provided, Elastic Beanstalk stores the build artifact in the S3 location S3-bucket /resources/application-name /codebuild/codebuild-version-label .zip.
            CodeBuildServiceRole (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
            ComputeType (string) --Information about the compute resources the build project will use.
            BUILD_GENERAL1_SMALL: Use up to 3 GB memory and 2 vCPUs for builds
            BUILD_GENERAL1_MEDIUM: Use up to 7 GB memory and 4 vCPUs for builds
            BUILD_GENERAL1_LARGE: Use up to 15 GB memory and 8 vCPUs for builds
            Image (string) -- [REQUIRED]The ID of the Docker image to use for this build project.
            TimeoutInMinutes (integer) --How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
            

    :type AutoCreateApplication: boolean
    :param AutoCreateApplication: Set to true to create an application with the specified name if it doesn't already exist.

    :type Process: boolean
    :param Process: Preprocesses and validates the environment manifest and configuration files in the source bundle. Validating configuration files can identify issues prior to deploying the application version to an environment.

    :rtype: dict
    :return: {
        'ApplicationVersion': {
            'ApplicationName': 'string',
            'Description': 'string',
            'VersionLabel': 'string',
            'SourceBuildInformation': {
                'SourceType': 'Git'|'Zip',
                'SourceRepository': 'CodeCommit'|'S3',
                'SourceLocation': 'string'
            },
            'BuildArn': 'string',
            'SourceBundle': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'DateCreated': datetime(2015, 1, 1),
            'DateUpdated': datetime(2015, 1, 1),
            'Status': 'Processed'|'Unprocessed'|'Failed'|'Processing'|'Building'
        }
    }
    
    
    :returns: 
    Git
    Zip
    
    """
    pass

def create_configuration_template(ApplicationName=None, TemplateName=None, SolutionStackName=None, PlatformArn=None, SourceConfiguration=None, EnvironmentId=None, Description=None, OptionSettings=None):
    """
    Creates a configuration template. Templates are associated with a specific application and are used to deploy different versions of the application with the same configuration settings.
    Related Topics
    See also: AWS API Documentation
    
    Examples
    The following operation creates a configuration template named my-app-v1 from the settings applied to an environment with the id e-rpqsewtp2j:
    Expected Output:
    
    :example: response = client.create_configuration_template(
        ApplicationName='string',
        TemplateName='string',
        SolutionStackName='string',
        PlatformArn='string',
        SourceConfiguration={
            'ApplicationName': 'string',
            'TemplateName': 'string'
        },
        EnvironmentId='string',
        Description='string',
        OptionSettings=[
            {
                'ResourceName': 'string',
                'Namespace': 'string',
                'OptionName': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]
            The name of the application to associate with this configuration template. If no application is found with this name, AWS Elastic Beanstalk returns an InvalidParameterValue error.
            

    :type TemplateName: string
    :param TemplateName: [REQUIRED]
            The name of the configuration template.
            Constraint: This name must be unique per application.
            Default: If a configuration template already exists with this name, AWS Elastic Beanstalk returns an InvalidParameterValue error.
            

    :type SolutionStackName: string
    :param SolutionStackName: The name of the solution stack used by this configuration. The solution stack specifies the operating system, architecture, and application server for a configuration template. It determines the set of configuration options as well as the possible and default values.
            Use ListAvailableSolutionStacks to obtain a list of available solution stacks.
            A solution stack name or a source configuration parameter must be specified, otherwise AWS Elastic Beanstalk returns an InvalidParameterValue error.
            If a solution stack name is not specified and the source configuration parameter is specified, AWS Elastic Beanstalk uses the same solution stack as the source configuration template.
            

    :type PlatformArn: string
    :param PlatformArn: The ARN of the custome platform.

    :type SourceConfiguration: dict
    :param SourceConfiguration: If specified, AWS Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.
            Values specified in the OptionSettings parameter of this call overrides any values obtained from the SourceConfiguration .
            If no configuration template is found, returns an InvalidParameterValue error.
            Constraint: If both the solution stack name parameter and the source configuration parameters are specified, the solution stack of the source configuration template must match the specified solution stack name or else AWS Elastic Beanstalk returns an InvalidParameterCombination error.
            ApplicationName (string) --The name of the application associated with the configuration.
            TemplateName (string) --The name of the configuration template.
            

    :type EnvironmentId: string
    :param EnvironmentId: The ID of the environment used with this configuration template.

    :type Description: string
    :param Description: Describes this configuration.

    :type OptionSettings: list
    :param OptionSettings: If specified, AWS Elastic Beanstalk sets the specified configuration option to the requested value. The new value overrides the value obtained from the solution stack or the source configuration template.
            (dict) --A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to Option Values in the AWS Elastic Beanstalk Developer Guide .
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            Value (string) --The current value for the configuration option.
            
            

    :rtype: dict
    :return: {
        'SolutionStackName': 'string',
        'PlatformArn': 'string',
        'ApplicationName': 'string',
        'TemplateName': 'string',
        'Description': 'string',
        'EnvironmentName': 'string',
        'DeploymentStatus': 'deployed'|'pending'|'failed',
        'DateCreated': datetime(2015, 1, 1),
        'DateUpdated': datetime(2015, 1, 1),
        'OptionSettings': [
            {
                'ResourceName': 'string',
                'Namespace': 'string',
                'OptionName': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    ApplicationName (string) -- [REQUIRED]
    The name of the application to associate with this configuration template. If no application is found with this name, AWS Elastic Beanstalk returns an InvalidParameterValue error.
    
    TemplateName (string) -- [REQUIRED]
    The name of the configuration template.
    Constraint: This name must be unique per application.
    Default: If a configuration template already exists with this name, AWS Elastic Beanstalk returns an InvalidParameterValue error.
    
    SolutionStackName (string) -- The name of the solution stack used by this configuration. The solution stack specifies the operating system, architecture, and application server for a configuration template. It determines the set of configuration options as well as the possible and default values.
    Use  ListAvailableSolutionStacks to obtain a list of available solution stacks.
    A solution stack name or a source configuration parameter must be specified, otherwise AWS Elastic Beanstalk returns an InvalidParameterValue error.
    If a solution stack name is not specified and the source configuration parameter is specified, AWS Elastic Beanstalk uses the same solution stack as the source configuration template.
    
    PlatformArn (string) -- The ARN of the custome platform.
    SourceConfiguration (dict) -- If specified, AWS Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.
    Values specified in the OptionSettings parameter of this call overrides any values obtained from the SourceConfiguration .
    If no configuration template is found, returns an InvalidParameterValue error.
    Constraint: If both the solution stack name parameter and the source configuration parameters are specified, the solution stack of the source configuration template must match the specified solution stack name or else AWS Elastic Beanstalk returns an InvalidParameterCombination error.
    
    ApplicationName (string) --The name of the application associated with the configuration.
    
    TemplateName (string) --The name of the configuration template.
    
    
    
    EnvironmentId (string) -- The ID of the environment used with this configuration template.
    Description (string) -- Describes this configuration.
    OptionSettings (list) -- If specified, AWS Elastic Beanstalk sets the specified configuration option to the requested value. The new value overrides the value obtained from the solution stack or the source configuration template.
    
    (dict) --A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to Option Values in the AWS Elastic Beanstalk Developer Guide .
    
    ResourceName (string) --A unique resource name for a time-based scaling configuration option.
    
    Namespace (string) --A unique namespace identifying the option's associated AWS resource.
    
    OptionName (string) --The name of the configuration option.
    
    Value (string) --The current value for the configuration option.
    
    
    
    
    
    
    """
    pass

def create_environment(ApplicationName=None, EnvironmentName=None, GroupName=None, Description=None, CNAMEPrefix=None, Tier=None, Tags=None, VersionLabel=None, TemplateName=None, SolutionStackName=None, PlatformArn=None, OptionSettings=None, OptionsToRemove=None):
    """
    Launches an environment for the specified application using the specified configuration.
    See also: AWS API Documentation
    
    Examples
    The following operation creates a new environment for version v1 of a java application named my-app:
    Expected Output:
    
    :example: response = client.create_environment(
        ApplicationName='string',
        EnvironmentName='string',
        GroupName='string',
        Description='string',
        CNAMEPrefix='string',
        Tier={
            'Name': 'string',
            'Type': 'string',
            'Version': 'string'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        VersionLabel='string',
        TemplateName='string',
        SolutionStackName='string',
        PlatformArn='string',
        OptionSettings=[
            {
                'ResourceName': 'string',
                'Namespace': 'string',
                'OptionName': 'string',
                'Value': 'string'
            },
        ],
        OptionsToRemove=[
            {
                'ResourceName': 'string',
                'Namespace': 'string',
                'OptionName': 'string'
            },
        ]
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]
            The name of the application that contains the version to be deployed.
            If no application is found with this name, CreateEnvironment returns an InvalidParameterValue error.
            

    :type EnvironmentName: string
    :param EnvironmentName: A unique name for the deployment environment. Used in the application URL.
            Constraint: Must be from 4 to 40 characters in length. The name can contain only letters, numbers, and hyphens. It cannot start or end with a hyphen. This name must be unique in your account. If the specified name already exists, AWS Elastic Beanstalk returns an InvalidParameterValue error.
            Default: If the CNAME parameter is not specified, the environment name becomes part of the CNAME, and therefore part of the visible URL for your application.
            

    :type GroupName: string
    :param GroupName: The name of the group to which the target environment belongs. Specify a group name only if the environment's name is specified in an environment manifest and not with the environment name parameter. See Environment Manifest (env.yaml) for details.

    :type Description: string
    :param Description: Describes this environment.

    :type CNAMEPrefix: string
    :param CNAMEPrefix: If specified, the environment attempts to use this value as the prefix for the CNAME. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.

    :type Tier: dict
    :param Tier: This specifies the tier to use for creating this environment.
            Name (string) --The name of this environment tier.
            Type (string) --The type of this environment tier.
            Version (string) --The version of this environment tier.
            

    :type Tags: list
    :param Tags: This specifies the tags applied to resources in the environment.
            (dict) --Describes a tag applied to a resource in an environment.
            Key (string) --The key of the tag.
            Value (string) --The value of the tag.
            
            

    :type VersionLabel: string
    :param VersionLabel: The name of the application version to deploy.
            If the specified application has no associated application versions, AWS Elastic Beanstalk UpdateEnvironment returns an InvalidParameterValue error.
            Default: If not specified, AWS Elastic Beanstalk attempts to launch the sample application in the container.
            

    :type TemplateName: string
    :param TemplateName: The name of the configuration template to use in deployment. If no configuration template is found with this name, AWS Elastic Beanstalk returns an InvalidParameterValue error.

    :type SolutionStackName: string
    :param SolutionStackName: This is an alternative to specifying a template name. If specified, AWS Elastic Beanstalk sets the configuration values to the default values associated with the specified solution stack.

    :type PlatformArn: string
    :param PlatformArn: The ARN of the custom platform.

    :type OptionSettings: list
    :param OptionSettings: If specified, AWS Elastic Beanstalk sets the specified configuration options to the requested value in the configuration set for the new environment. These override the values obtained from the solution stack or the configuration template.
            (dict) --A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to Option Values in the AWS Elastic Beanstalk Developer Guide .
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            Value (string) --The current value for the configuration option.
            
            

    :type OptionsToRemove: list
    :param OptionsToRemove: A list of custom user-defined configuration options to remove from the configuration set for this new environment.
            (dict) --A specification identifying an individual configuration option.
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            
            

    :rtype: dict
    :return: {
        'EnvironmentName': 'string',
        'EnvironmentId': 'string',
        'ApplicationName': 'string',
        'VersionLabel': 'string',
        'SolutionStackName': 'string',
        'PlatformArn': 'string',
        'TemplateName': 'string',
        'Description': 'string',
        'EndpointURL': 'string',
        'CNAME': 'string',
        'DateCreated': datetime(2015, 1, 1),
        'DateUpdated': datetime(2015, 1, 1),
        'Status': 'Launching'|'Updating'|'Ready'|'Terminating'|'Terminated',
        'AbortableOperationInProgress': True|False,
        'Health': 'Green'|'Yellow'|'Red'|'Grey',
        'HealthStatus': 'NoData'|'Unknown'|'Pending'|'Ok'|'Info'|'Warning'|'Degraded'|'Severe',
        'Resources': {
            'LoadBalancer': {
                'LoadBalancerName': 'string',
                'Domain': 'string',
                'Listeners': [
                    {
                        'Protocol': 'string',
                        'Port': 123
                    },
                ]
            }
        },
        'Tier': {
            'Name': 'string',
            'Type': 'string',
            'Version': 'string'
        },
        'EnvironmentLinks': [
            {
                'LinkName': 'string',
                'EnvironmentName': 'string'
            },
        ]
    }
    
    
    :returns: 
    Launching : Environment is in the process of initial deployment.
    Updating : Environment is in the process of updating its configuration settings or application version.
    Ready : Environment is available to have an action performed on it, such as update or terminate.
    Terminating : Environment is in the shut-down process.
    Terminated : Environment is not running.
    
    """
    pass

def create_platform_version(PlatformName=None, PlatformVersion=None, PlatformDefinitionBundle=None, EnvironmentName=None, OptionSettings=None):
    """
    Create a new version of your custom platform.
    See also: AWS API Documentation
    
    
    :example: response = client.create_platform_version(
        PlatformName='string',
        PlatformVersion='string',
        PlatformDefinitionBundle={
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        EnvironmentName='string',
        OptionSettings=[
            {
                'ResourceName': 'string',
                'Namespace': 'string',
                'OptionName': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type PlatformName: string
    :param PlatformName: [REQUIRED]
            The name of your custom platform.
            

    :type PlatformVersion: string
    :param PlatformVersion: [REQUIRED]
            The number, such as 1.0.2, for the new platform version.
            

    :type PlatformDefinitionBundle: dict
    :param PlatformDefinitionBundle: [REQUIRED]
            The location of the platform definition archive in Amazon S3.
            S3Bucket (string) --The Amazon S3 bucket where the data is located.
            S3Key (string) --The Amazon S3 key where the data is located.
            

    :type EnvironmentName: string
    :param EnvironmentName: The name of the builder environment.

    :type OptionSettings: list
    :param OptionSettings: The configuration option settings to apply to the builder environment.
            (dict) --A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to Option Values in the AWS Elastic Beanstalk Developer Guide .
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            Value (string) --The current value for the configuration option.
            
            

    :rtype: dict
    :return: {
        'PlatformSummary': {
            'PlatformArn': 'string',
            'PlatformOwner': 'string',
            'PlatformStatus': 'Creating'|'Failed'|'Ready'|'Deleting'|'Deleted',
            'PlatformCategory': 'string',
            'OperatingSystemName': 'string',
            'OperatingSystemVersion': 'string',
            'SupportedTierList': [
                'string',
            ],
            'SupportedAddonList': [
                'string',
            ]
        },
        'Builder': {
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_storage_location():
    """
    Creates the Amazon S3 storage location for the account.
    This location is used to store user log files.
    See also: AWS API Documentation
    
    Examples
    The following operation creates a new environment for version v1 of a java application named my-app:
    Expected Output:
    
    :example: response = client.create_storage_location()
    
    
    :rtype: dict
    :return: {
        'S3Bucket': 'string'
    }
    
    
    """
    pass

def delete_application(ApplicationName=None, TerminateEnvByForce=None):
    """
    Deletes the specified application along with all associated versions and configurations. The application versions will not be deleted from your Amazon S3 bucket.
    See also: AWS API Documentation
    
    Examples
    The following operation deletes an application named my-app:
    Expected Output:
    
    :example: response = client.delete_application(
        ApplicationName='string',
        TerminateEnvByForce=True|False
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]
            The name of the application to delete.
            

    :type TerminateEnvByForce: boolean
    :param TerminateEnvByForce: When set to true, running environments will be terminated before deleting the application.

    :return: response = client.delete_application(
        ApplicationName='my-app',
    )
    
    print(response)
    
    
    """
    pass

def delete_application_version(ApplicationName=None, VersionLabel=None, DeleteSourceBundle=None):
    """
    Deletes the specified version from the specified application.
    See also: AWS API Documentation
    
    Examples
    The following operation deletes an application version named 22a0-stage-150819_182129 for an application named my-app:
    Expected Output:
    
    :example: response = client.delete_application_version(
        ApplicationName='string',
        VersionLabel='string',
        DeleteSourceBundle=True|False
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]
            The name of the application to which the version belongs.
            

    :type VersionLabel: string
    :param VersionLabel: [REQUIRED]
            The label of the version to delete.
            

    :type DeleteSourceBundle: boolean
    :param DeleteSourceBundle: Set to true to delete the source bundle from your storage bucket. Otherwise, the application version is deleted only from Elastic Beanstalk and the source bundle remains in Amazon S3.

    :return: response = client.delete_application_version(
        ApplicationName='my-app',
        DeleteSourceBundle=True,
        VersionLabel='22a0-stage-150819_182129',
    )
    
    print(response)
    
    
    """
    pass

def delete_configuration_template(ApplicationName=None, TemplateName=None):
    """
    Deletes the specified configuration template.
    See also: AWS API Documentation
    
    Examples
    The following operation deletes a configuration template named my-template for an application named my-app:
    Expected Output:
    
    :example: response = client.delete_configuration_template(
        ApplicationName='string',
        TemplateName='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]
            The name of the application to delete the configuration template from.
            

    :type TemplateName: string
    :param TemplateName: [REQUIRED]
            The name of the configuration template to delete.
            

    :return: response = client.delete_configuration_template(
        ApplicationName='my-app',
        TemplateName='my-template',
    )
    
    print(response)
    
    
    """
    pass

def delete_environment_configuration(ApplicationName=None, EnvironmentName=None):
    """
    Deletes the draft configuration associated with the running environment.
    Updating a running environment with any configuration changes creates a draft configuration set. You can get the draft configuration using  DescribeConfigurationSettings while the update is in progress or if the update fails. The DeploymentStatus for the draft configuration indicates whether the deployment is in process or has failed. The draft configuration remains in existence until it is deleted with this action.
    See also: AWS API Documentation
    
    Examples
    The following operation deletes a draft configuration for an environment named my-env:
    Expected Output:
    
    :example: response = client.delete_environment_configuration(
        ApplicationName='string',
        EnvironmentName='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]
            The name of the application the environment is associated with.
            

    :type EnvironmentName: string
    :param EnvironmentName: [REQUIRED]
            The name of the environment to delete the draft configuration from.
            

    :return: response = client.delete_environment_configuration(
        ApplicationName='my-app',
        EnvironmentName='my-env',
    )
    
    print(response)
    
    
    """
    pass

def delete_platform_version(PlatformArn=None):
    """
    Deletes the specified version of a custom platform.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_platform_version(
        PlatformArn='string'
    )
    
    
    :type PlatformArn: string
    :param PlatformArn: The ARN of the version of the custom platform.

    :rtype: dict
    :return: {
        'PlatformSummary': {
            'PlatformArn': 'string',
            'PlatformOwner': 'string',
            'PlatformStatus': 'Creating'|'Failed'|'Ready'|'Deleting'|'Deleted',
            'PlatformCategory': 'string',
            'OperatingSystemName': 'string',
            'OperatingSystemVersion': 'string',
            'SupportedTierList': [
                'string',
            ],
            'SupportedAddonList': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_application_versions(ApplicationName=None, VersionLabels=None, MaxRecords=None, NextToken=None):
    """
    Retrieve a list of application versions.
    See also: AWS API Documentation
    
    Examples
    The following operation retrieves information about an application version labeled v2:
    Expected Output:
    
    :example: response = client.describe_application_versions(
        ApplicationName='string',
        VersionLabels=[
            'string',
        ],
        MaxRecords=123,
        NextToken='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: Specify an application name to show only application versions for that application.

    :type VersionLabels: list
    :param VersionLabels: Specify a version label to show a specific application version.
            (string) --
            

    :type MaxRecords: integer
    :param MaxRecords: Specify a maximum number of application versions to paginate in the request.

    :type NextToken: string
    :param NextToken: Specify a next token to retrieve the next page in a paginated request.

    :rtype: dict
    :return: {
        'ApplicationVersions': [
            {
                'ApplicationName': 'string',
                'Description': 'string',
                'VersionLabel': 'string',
                'SourceBuildInformation': {
                    'SourceType': 'Git'|'Zip',
                    'SourceRepository': 'CodeCommit'|'S3',
                    'SourceLocation': 'string'
                },
                'BuildArn': 'string',
                'SourceBundle': {
                    'S3Bucket': 'string',
                    'S3Key': 'string'
                },
                'DateCreated': datetime(2015, 1, 1),
                'DateUpdated': datetime(2015, 1, 1),
                'Status': 'Processed'|'Unprocessed'|'Failed'|'Processing'|'Building'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Git
    Zip
    
    """
    pass

def describe_applications(ApplicationNames=None):
    """
    Returns the descriptions of existing applications.
    See also: AWS API Documentation
    
    Examples
    The following operation retrieves information about applications in the current region:
    Expected Output:
    
    :example: response = client.describe_applications(
        ApplicationNames=[
            'string',
        ]
    )
    
    
    :type ApplicationNames: list
    :param ApplicationNames: If specified, AWS Elastic Beanstalk restricts the returned descriptions to only include those with the specified names.
            (string) --
            

    :rtype: dict
    :return: {
        'Applications': [
            {
                'ApplicationName': 'string',
                'Description': 'string',
                'DateCreated': datetime(2015, 1, 1),
                'DateUpdated': datetime(2015, 1, 1),
                'Versions': [
                    'string',
                ],
                'ConfigurationTemplates': [
                    'string',
                ],
                'ResourceLifecycleConfig': {
                    'ServiceRole': 'string',
                    'VersionLifecycleConfig': {
                        'MaxCountRule': {
                            'Enabled': True|False,
                            'MaxCount': 123,
                            'DeleteSourceFromS3': True|False
                        },
                        'MaxAgeRule': {
                            'Enabled': True|False,
                            'MaxAgeInDays': 123,
                            'DeleteSourceFromS3': True|False
                        }
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_configuration_options(ApplicationName=None, TemplateName=None, EnvironmentName=None, SolutionStackName=None, PlatformArn=None, Options=None):
    """
    Describes the configuration options that are used in a particular configuration template or environment, or that a specified solution stack defines. The description includes the values the options, their default values, and an indication of the required action on a running environment if an option value is changed.
    See also: AWS API Documentation
    
    Examples
    The following operation retrieves descriptions of all available configuration options for an environment named my-env:
    Expected Output:
    
    :example: response = client.describe_configuration_options(
        ApplicationName='string',
        TemplateName='string',
        EnvironmentName='string',
        SolutionStackName='string',
        PlatformArn='string',
        Options=[
            {
                'ResourceName': 'string',
                'Namespace': 'string',
                'OptionName': 'string'
            },
        ]
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: The name of the application associated with the configuration template or environment. Only needed if you want to describe the configuration options associated with either the configuration template or environment.

    :type TemplateName: string
    :param TemplateName: The name of the configuration template whose configuration options you want to describe.

    :type EnvironmentName: string
    :param EnvironmentName: The name of the environment whose configuration options you want to describe.

    :type SolutionStackName: string
    :param SolutionStackName: The name of the solution stack whose configuration options you want to describe.

    :type PlatformArn: string
    :param PlatformArn: The ARN of the custom platform.

    :type Options: list
    :param Options: If specified, restricts the descriptions to only the specified options.
            (dict) --A specification identifying an individual configuration option.
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            
            

    :rtype: dict
    :return: {
        'SolutionStackName': 'string',
        'PlatformArn': 'string',
        'Options': [
            {
                'Namespace': 'string',
                'Name': 'string',
                'DefaultValue': 'string',
                'ChangeSeverity': 'string',
                'UserDefined': True|False,
                'ValueType': 'Scalar'|'List',
                'ValueOptions': [
                    'string',
                ],
                'MinValue': 123,
                'MaxValue': 123,
                'MaxLength': 123,
                'Regex': {
                    'Pattern': 'string',
                    'Label': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    NoInterruption : There is no interruption to the environment or application availability.
    RestartEnvironment : The environment is entirely restarted, all AWS resources are deleted and recreated, and the environment is unavailable during the process.
    RestartApplicationServer : The environment is available the entire time. However, a short application outage occurs when the application servers on the running Amazon EC2 instances are restarted.
    
    """
    pass

def describe_configuration_settings(ApplicationName=None, TemplateName=None, EnvironmentName=None):
    """
    Returns a description of the settings for the specified configuration set, that is, either a configuration template or the configuration set associated with a running environment.
    When describing the settings for the configuration set associated with a running environment, it is possible to receive two sets of setting descriptions. One is the deployed configuration set, and the other is a draft configuration of an environment that is either in the process of deployment or that failed to deploy.
    Related Topics
    See also: AWS API Documentation
    
    Examples
    The following operation retrieves configuration settings for an environment named my-env:
    Expected Output:
    
    :example: response = client.describe_configuration_settings(
        ApplicationName='string',
        TemplateName='string',
        EnvironmentName='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]
            The application for the environment or configuration template.
            

    :type TemplateName: string
    :param TemplateName: The name of the configuration template to describe.
            Conditional: You must specify either this parameter or an EnvironmentName, but not both. If you specify both, AWS Elastic Beanstalk returns an InvalidParameterCombination error. If you do not specify either, AWS Elastic Beanstalk returns a MissingRequiredParameter error.
            

    :type EnvironmentName: string
    :param EnvironmentName: The name of the environment to describe.
            Condition: You must specify either this or a TemplateName, but not both. If you specify both, AWS Elastic Beanstalk returns an InvalidParameterCombination error. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :rtype: dict
    :return: {
        'ConfigurationSettings': [
            {
                'SolutionStackName': 'string',
                'PlatformArn': 'string',
                'ApplicationName': 'string',
                'TemplateName': 'string',
                'Description': 'string',
                'EnvironmentName': 'string',
                'DeploymentStatus': 'deployed'|'pending'|'failed',
                'DateCreated': datetime(2015, 1, 1),
                'DateUpdated': datetime(2015, 1, 1),
                'OptionSettings': [
                    {
                        'ResourceName': 'string',
                        'Namespace': 'string',
                        'OptionName': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    ApplicationName (string) -- [REQUIRED]
    The application for the environment or configuration template.
    
    TemplateName (string) -- The name of the configuration template to describe.
    Conditional: You must specify either this parameter or an EnvironmentName, but not both. If you specify both, AWS Elastic Beanstalk returns an InvalidParameterCombination error. If you do not specify either, AWS Elastic Beanstalk returns a MissingRequiredParameter error.
    
    EnvironmentName (string) -- The name of the environment to describe.
    Condition: You must specify either this or a TemplateName, but not both. If you specify both, AWS Elastic Beanstalk returns an InvalidParameterCombination error. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
    
    
    """
    pass

def describe_environment_health(EnvironmentName=None, EnvironmentId=None, AttributeNames=None):
    """
    Returns information about the overall health of the specified environment. The DescribeEnvironmentHealth operation is only available with AWS Elastic Beanstalk Enhanced Health.
    See also: AWS API Documentation
    
    Examples
    The following operation retrieves overall health information for an environment named my-env:
    Expected Output:
    
    :example: response = client.describe_environment_health(
        EnvironmentName='string',
        EnvironmentId='string',
        AttributeNames=[
            'Status'|'Color'|'Causes'|'ApplicationMetrics'|'InstancesHealth'|'All'|'HealthStatus'|'RefreshedAt',
        ]
    )
    
    
    :type EnvironmentName: string
    :param EnvironmentName: Specify the environment by name.
            You must specify either this or an EnvironmentName, or both.
            

    :type EnvironmentId: string
    :param EnvironmentId: Specify the environment by ID.
            You must specify either this or an EnvironmentName, or both.
            

    :type AttributeNames: list
    :param AttributeNames: Specify the response elements to return. To retrieve all attributes, set to All . If no attribute names are specified, returns the name of the environment.
            (string) --
            

    :rtype: dict
    :return: {
        'EnvironmentName': 'string',
        'HealthStatus': 'string',
        'Status': 'Green'|'Yellow'|'Red'|'Grey',
        'Color': 'string',
        'Causes': [
            'string',
        ],
        'ApplicationMetrics': {
            'Duration': 123,
            'RequestCount': 123,
            'StatusCodes': {
                'Status2xx': 123,
                'Status3xx': 123,
                'Status4xx': 123,
                'Status5xx': 123
            },
            'Latency': {
                'P999': 123.0,
                'P99': 123.0,
                'P95': 123.0,
                'P90': 123.0,
                'P85': 123.0,
                'P75': 123.0,
                'P50': 123.0,
                'P10': 123.0
            }
        },
        'InstancesHealth': {
            'NoData': 123,
            'Unknown': 123,
            'Pending': 123,
            'Ok': 123,
            'Info': 123,
            'Warning': 123,
            'Degraded': 123,
            'Severe': 123
        },
        'RefreshedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_environment_managed_action_history(EnvironmentId=None, EnvironmentName=None, NextToken=None, MaxItems=None):
    """
    Lists an environment's completed and failed managed actions.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_environment_managed_action_history(
        EnvironmentId='string',
        EnvironmentName='string',
        NextToken='string',
        MaxItems=123
    )
    
    
    :type EnvironmentId: string
    :param EnvironmentId: The environment ID of the target environment.

    :type EnvironmentName: string
    :param EnvironmentName: The name of the target environment.

    :type NextToken: string
    :param NextToken: The pagination token returned by a previous request.

    :type MaxItems: integer
    :param MaxItems: The maximum number of items to return for a single request.

    :rtype: dict
    :return: {
        'ManagedActionHistoryItems': [
            {
                'ActionId': 'string',
                'ActionType': 'InstanceRefresh'|'PlatformUpdate'|'Unknown',
                'ActionDescription': 'string',
                'FailureType': 'UpdateCancelled'|'CancellationFailed'|'RollbackFailed'|'RollbackSuccessful'|'InternalFailure'|'InvalidEnvironmentState'|'PermissionsError',
                'Status': 'Completed'|'Failed'|'Unknown',
                'FailureDescription': 'string',
                'ExecutedTime': datetime(2015, 1, 1),
                'FinishedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_environment_managed_actions(EnvironmentName=None, EnvironmentId=None, Status=None):
    """
    Lists an environment's upcoming and in-progress managed actions.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_environment_managed_actions(
        EnvironmentName='string',
        EnvironmentId='string',
        Status='Scheduled'|'Pending'|'Running'|'Unknown'
    )
    
    
    :type EnvironmentName: string
    :param EnvironmentName: The name of the target environment.

    :type EnvironmentId: string
    :param EnvironmentId: The environment ID of the target environment.

    :type Status: string
    :param Status: To show only actions with a particular status, specify a status.

    :rtype: dict
    :return: {
        'ManagedActions': [
            {
                'ActionId': 'string',
                'ActionDescription': 'string',
                'ActionType': 'InstanceRefresh'|'PlatformUpdate'|'Unknown',
                'Status': 'Scheduled'|'Pending'|'Running'|'Unknown',
                'WindowStartTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def describe_environment_resources(EnvironmentId=None, EnvironmentName=None):
    """
    Returns AWS resources for this environment.
    See also: AWS API Documentation
    
    Examples
    The following operation retrieves information about resources in an environment named my-env:
    Expected Output:
    
    :example: response = client.describe_environment_resources(
        EnvironmentId='string',
        EnvironmentName='string'
    )
    
    
    :type EnvironmentId: string
    :param EnvironmentId: The ID of the environment to retrieve AWS resource usage data.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :type EnvironmentName: string
    :param EnvironmentName: The name of the environment to retrieve AWS resource usage data.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :rtype: dict
    :return: {
        'EnvironmentResources': {
            'EnvironmentName': 'string',
            'AutoScalingGroups': [
                {
                    'Name': 'string'
                },
            ],
            'Instances': [
                {
                    'Id': 'string'
                },
            ],
            'LaunchConfigurations': [
                {
                    'Name': 'string'
                },
            ],
            'LoadBalancers': [
                {
                    'Name': 'string'
                },
            ],
            'Triggers': [
                {
                    'Name': 'string'
                },
            ],
            'Queues': [
                {
                    'Name': 'string',
                    'URL': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def describe_environments(ApplicationName=None, VersionLabel=None, EnvironmentIds=None, EnvironmentNames=None, IncludeDeleted=None, IncludedDeletedBackTo=None):
    """
    Returns descriptions for existing environments.
    See also: AWS API Documentation
    
    Examples
    The following operation retrieves information about an environment named my-env:
    Expected Output:
    
    :example: response = client.describe_environments(
        ApplicationName='string',
        VersionLabel='string',
        EnvironmentIds=[
            'string',
        ],
        EnvironmentNames=[
            'string',
        ],
        IncludeDeleted=True|False,
        IncludedDeletedBackTo=datetime(2015, 1, 1)
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application.

    :type VersionLabel: string
    :param VersionLabel: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application version.

    :type EnvironmentIds: list
    :param EnvironmentIds: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified IDs.
            (string) --
            

    :type EnvironmentNames: list
    :param EnvironmentNames: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified names.
            (string) --
            

    :type IncludeDeleted: boolean
    :param IncludeDeleted: Indicates whether to include deleted environments:
            true : Environments that have been deleted after IncludedDeletedBackTo are displayed.false : Do not include deleted environments.
            

    :type IncludedDeletedBackTo: datetime
    :param IncludedDeletedBackTo: If specified when IncludeDeleted is set to true , then environments deleted after this date are displayed.

    :rtype: dict
    :return: {
        'Environments': [
            {
                'EnvironmentName': 'string',
                'EnvironmentId': 'string',
                'ApplicationName': 'string',
                'VersionLabel': 'string',
                'SolutionStackName': 'string',
                'PlatformArn': 'string',
                'TemplateName': 'string',
                'Description': 'string',
                'EndpointURL': 'string',
                'CNAME': 'string',
                'DateCreated': datetime(2015, 1, 1),
                'DateUpdated': datetime(2015, 1, 1),
                'Status': 'Launching'|'Updating'|'Ready'|'Terminating'|'Terminated',
                'AbortableOperationInProgress': True|False,
                'Health': 'Green'|'Yellow'|'Red'|'Grey',
                'HealthStatus': 'NoData'|'Unknown'|'Pending'|'Ok'|'Info'|'Warning'|'Degraded'|'Severe',
                'Resources': {
                    'LoadBalancer': {
                        'LoadBalancerName': 'string',
                        'Domain': 'string',
                        'Listeners': [
                            {
                                'Protocol': 'string',
                                'Port': 123
                            },
                        ]
                    }
                },
                'Tier': {
                    'Name': 'string',
                    'Type': 'string',
                    'Version': 'string'
                },
                'EnvironmentLinks': [
                    {
                        'LinkName': 'string',
                        'EnvironmentName': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    Launching : Environment is in the process of initial deployment.
    Updating : Environment is in the process of updating its configuration settings or application version.
    Ready : Environment is available to have an action performed on it, such as update or terminate.
    Terminating : Environment is in the shut-down process.
    Terminated : Environment is not running.
    
    """
    pass

def describe_events(ApplicationName=None, VersionLabel=None, TemplateName=None, EnvironmentId=None, EnvironmentName=None, PlatformArn=None, RequestId=None, Severity=None, StartTime=None, EndTime=None, MaxRecords=None, NextToken=None):
    """
    Returns list of event descriptions matching criteria up to the last 6 weeks.
    See also: AWS API Documentation
    
    Examples
    The following operation retrieves events for an environment named my-env:
    Expected Output:
    
    :example: response = client.describe_events(
        ApplicationName='string',
        VersionLabel='string',
        TemplateName='string',
        EnvironmentId='string',
        EnvironmentName='string',
        PlatformArn='string',
        RequestId='string',
        Severity='TRACE'|'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        MaxRecords=123,
        NextToken='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those associated with this application.

    :type VersionLabel: string
    :param VersionLabel: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this application version.

    :type TemplateName: string
    :param TemplateName: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that are associated with this environment configuration.

    :type EnvironmentId: string
    :param EnvironmentId: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.

    :type EnvironmentName: string
    :param EnvironmentName: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.

    :type PlatformArn: string
    :param PlatformArn: The ARN of the version of the custom platform.

    :type RequestId: string
    :param RequestId: If specified, AWS Elastic Beanstalk restricts the described events to include only those associated with this request ID.

    :type Severity: string
    :param Severity: If specified, limits the events returned from this call to include only those with the specified severity or higher.

    :type StartTime: datetime
    :param StartTime: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur on or after this time.

    :type EndTime: datetime
    :param EndTime: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur up to, but not including, the EndTime .

    :type MaxRecords: integer
    :param MaxRecords: Specifies the maximum number of events that can be returned, beginning with the most recent event.

    :type NextToken: string
    :param NextToken: Pagination token. If specified, the events return the next batch of results.

    :rtype: dict
    :return: {
        'Events': [
            {
                'EventDate': datetime(2015, 1, 1),
                'Message': 'string',
                'ApplicationName': 'string',
                'VersionLabel': 'string',
                'TemplateName': 'string',
                'EnvironmentName': 'string',
                'PlatformArn': 'string',
                'RequestId': 'string',
                'Severity': 'TRACE'|'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_instances_health(EnvironmentName=None, EnvironmentId=None, AttributeNames=None, NextToken=None):
    """
    Retrives detailed information about the health of instances in your AWS Elastic Beanstalk. This operation requires enhanced health reporting .
    See also: AWS API Documentation
    
    Examples
    The following operation retrieves health information for instances in an environment named my-env:
    Expected Output:
    
    :example: response = client.describe_instances_health(
        EnvironmentName='string',
        EnvironmentId='string',
        AttributeNames=[
            'HealthStatus'|'Color'|'Causes'|'ApplicationMetrics'|'RefreshedAt'|'LaunchedAt'|'System'|'Deployment'|'AvailabilityZone'|'InstanceType'|'All',
        ],
        NextToken='string'
    )
    
    
    :type EnvironmentName: string
    :param EnvironmentName: Specify the AWS Elastic Beanstalk environment by name.

    :type EnvironmentId: string
    :param EnvironmentId: Specify the AWS Elastic Beanstalk environment by ID.

    :type AttributeNames: list
    :param AttributeNames: Specifies the response elements you wish to receive. To retrieve all attributes, set to All . If no attribute names are specified, returns a list of instances.
            (string) --
            

    :type NextToken: string
    :param NextToken: Specify the pagination token returned by a previous call.

    :rtype: dict
    :return: {
        'InstanceHealthList': [
            {
                'InstanceId': 'string',
                'HealthStatus': 'string',
                'Color': 'string',
                'Causes': [
                    'string',
                ],
                'LaunchedAt': datetime(2015, 1, 1),
                'ApplicationMetrics': {
                    'Duration': 123,
                    'RequestCount': 123,
                    'StatusCodes': {
                        'Status2xx': 123,
                        'Status3xx': 123,
                        'Status4xx': 123,
                        'Status5xx': 123
                    },
                    'Latency': {
                        'P999': 123.0,
                        'P99': 123.0,
                        'P95': 123.0,
                        'P90': 123.0,
                        'P85': 123.0,
                        'P75': 123.0,
                        'P50': 123.0,
                        'P10': 123.0
                    }
                },
                'System': {
                    'CPUUtilization': {
                        'User': 123.0,
                        'Nice': 123.0,
                        'System': 123.0,
                        'Idle': 123.0,
                        'IOWait': 123.0,
                        'IRQ': 123.0,
                        'SoftIRQ': 123.0
                    },
                    'LoadAverage': [
                        123.0,
                    ]
                },
                'Deployment': {
                    'VersionLabel': 'string',
                    'DeploymentId': 123,
                    'Status': 'string',
                    'DeploymentTime': datetime(2015, 1, 1)
                },
                'AvailabilityZone': 'string',
                'InstanceType': 'string'
            },
        ],
        'RefreshedAt': datetime(2015, 1, 1),
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_platform_version(PlatformArn=None):
    """
    Describes the version of the platform.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_platform_version(
        PlatformArn='string'
    )
    
    
    :type PlatformArn: string
    :param PlatformArn: The ARN of the version of the platform.

    :rtype: dict
    :return: {
        'PlatformDescription': {
            'PlatformArn': 'string',
            'PlatformOwner': 'string',
            'PlatformName': 'string',
            'PlatformVersion': 'string',
            'SolutionStackName': 'string',
            'PlatformStatus': 'Creating'|'Failed'|'Ready'|'Deleting'|'Deleted',
            'DateCreated': datetime(2015, 1, 1),
            'DateUpdated': datetime(2015, 1, 1),
            'PlatformCategory': 'string',
            'Description': 'string',
            'Maintainer': 'string',
            'OperatingSystemName': 'string',
            'OperatingSystemVersion': 'string',
            'ProgrammingLanguages': [
                {
                    'Name': 'string',
                    'Version': 'string'
                },
            ],
            'Frameworks': [
                {
                    'Name': 'string',
                    'Version': 'string'
                },
            ],
            'CustomAmiList': [
                {
                    'VirtualizationType': 'string',
                    'ImageId': 'string'
                },
            ],
            'SupportedTierList': [
                'string',
            ],
            'SupportedAddonList': [
                'string',
            ]
        }
    }
    
    
    :returns: 
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

def list_available_solution_stacks():
    """
    Returns a list of the available solution stack names, with the public version first and then in reverse chronological order.
    See also: AWS API Documentation
    
    Examples
    The following operation lists solution stacks for all currently available platform configurations and any that you have used in the past:
    Expected Output:
    
    :example: response = client.list_available_solution_stacks()
    
    
    :rtype: dict
    :return: {
        'SolutionStacks': [
            'string',
        ],
        'SolutionStackDetails': [
            {
                'SolutionStackName': 'string',
                'PermittedFileTypes': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_platform_versions(Filters=None, MaxRecords=None, NextToken=None):
    """
    Lists the available platforms.
    See also: AWS API Documentation
    
    
    :example: response = client.list_platform_versions(
        Filters=[
            {
                'Type': 'string',
                'Operator': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        NextToken='string'
    )
    
    
    :type Filters: list
    :param Filters: List only the platforms where the platform member value relates to one of the supplied values.
            (dict) --Specify criteria to restrict the results when listing custom platforms.
            The filter is evaluated as the expression:
            Type Operator Values[i]
            Type (string) --The custom platform attribute to which the filter values are applied.
            Valid Values: PlatformName | PlatformVersion | PlatformStatus | PlatformOwner
            Operator (string) --The operator to apply to the Type with each of the Values .
            Valid Values: = (equal to) | != (not equal to) | ```` (less than) | = (less than or equal to) | ```` (greater than) | = (greater than or equal to) | contains | begins_with | ends_with
            Values (list) --The list of values applied to the custom platform attribute.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of platform values returned in one call.

    :type NextToken: string
    :param NextToken: The starting index into the remaining list of platforms. Use the NextToken value from a previous ListPlatformVersion call.

    :rtype: dict
    :return: {
        'PlatformSummaryList': [
            {
                'PlatformArn': 'string',
                'PlatformOwner': 'string',
                'PlatformStatus': 'Creating'|'Failed'|'Ready'|'Deleting'|'Deleted',
                'PlatformCategory': 'string',
                'OperatingSystemName': 'string',
                'OperatingSystemVersion': 'string',
                'SupportedTierList': [
                    'string',
                ],
                'SupportedAddonList': [
                    'string',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def rebuild_environment(EnvironmentId=None, EnvironmentName=None):
    """
    Deletes and recreates all of the AWS resources (for example: the Auto Scaling group, load balancer, etc.) for a specified environment and forces a restart.
    See also: AWS API Documentation
    
    Examples
    The following operation terminates and recreates the resources in an environment named my-env:
    Expected Output:
    
    :example: response = client.rebuild_environment(
        EnvironmentId='string',
        EnvironmentName='string'
    )
    
    
    :type EnvironmentId: string
    :param EnvironmentId: The ID of the environment to rebuild.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :type EnvironmentName: string
    :param EnvironmentName: The name of the environment to rebuild.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :return: response = client.rebuild_environment(
        EnvironmentName='my-env',
    )
    
    print(response)
    
    
    """
    pass

def request_environment_info(EnvironmentId=None, EnvironmentName=None, InfoType=None):
    """
    Initiates a request to compile the specified type of information of the deployed environment.
    Setting the InfoType to tail compiles the last lines from the application server log files of every Amazon EC2 instance in your environment.
    Setting the InfoType to bundle compresses the application server log files for every Amazon EC2 instance into a .zip file. Legacy and .NET containers do not support bundle logs.
    Use  RetrieveEnvironmentInfo to obtain the set of logs.
    Related Topics
    See also: AWS API Documentation
    
    Examples
    The following operation requests logs from an environment named my-env:
    Expected Output:
    
    :example: response = client.request_environment_info(
        EnvironmentId='string',
        EnvironmentName='string',
        InfoType='tail'|'bundle'
    )
    
    
    :type EnvironmentId: string
    :param EnvironmentId: The ID of the environment of the requested data.
            If no such environment is found, RequestEnvironmentInfo returns an InvalidParameterValue error.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :type EnvironmentName: string
    :param EnvironmentName: The name of the environment of the requested data.
            If no such environment is found, RequestEnvironmentInfo returns an InvalidParameterValue error.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :type InfoType: string
    :param InfoType: [REQUIRED]
            The type of information to request.
            

    :return: response = client.request_environment_info(
        EnvironmentName='my-env',
        InfoType='tail',
    )
    
    print(response)
    
    
    :returns: 
    EnvironmentId (string) -- The ID of the environment of the requested data.
    If no such environment is found, RequestEnvironmentInfo returns an InvalidParameterValue error.
    Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
    
    EnvironmentName (string) -- The name of the environment of the requested data.
    If no such environment is found, RequestEnvironmentInfo returns an InvalidParameterValue error.
    Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
    
    InfoType (string) -- [REQUIRED]
    The type of information to request.
    
    
    """
    pass

def restart_app_server(EnvironmentId=None, EnvironmentName=None):
    """
    Causes the environment to restart the application container server running on each Amazon EC2 instance.
    See also: AWS API Documentation
    
    Examples
    The following operation restarts application servers on all instances in an environment named my-env:
    Expected Output:
    
    :example: response = client.restart_app_server(
        EnvironmentId='string',
        EnvironmentName='string'
    )
    
    
    :type EnvironmentId: string
    :param EnvironmentId: The ID of the environment to restart the server for.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :type EnvironmentName: string
    :param EnvironmentName: The name of the environment to restart the server for.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :return: response = client.restart_app_server(
        EnvironmentName='my-env',
    )
    
    print(response)
    
    
    """
    pass

def retrieve_environment_info(EnvironmentId=None, EnvironmentName=None, InfoType=None):
    """
    Retrieves the compiled information from a  RequestEnvironmentInfo request.
    Related Topics
    See also: AWS API Documentation
    
    Examples
    The following operation retrieves a link to logs from an environment named my-env:
    Expected Output:
    
    :example: response = client.retrieve_environment_info(
        EnvironmentId='string',
        EnvironmentName='string',
        InfoType='tail'|'bundle'
    )
    
    
    :type EnvironmentId: string
    :param EnvironmentId: The ID of the data's environment.
            If no such environment is found, returns an InvalidParameterValue error.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :type EnvironmentName: string
    :param EnvironmentName: The name of the data's environment.
            If no such environment is found, returns an InvalidParameterValue error.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :type InfoType: string
    :param InfoType: [REQUIRED]
            The type of information to retrieve.
            

    :rtype: dict
    :return: {
        'EnvironmentInfo': [
            {
                'InfoType': 'tail'|'bundle',
                'Ec2InstanceId': 'string',
                'SampleTimestamp': datetime(2015, 1, 1),
                'Message': 'string'
            },
        ]
    }
    
    
    :returns: 
    EnvironmentId (string) -- The ID of the data's environment.
    If no such environment is found, returns an InvalidParameterValue error.
    Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
    
    EnvironmentName (string) -- The name of the data's environment.
    If no such environment is found, returns an InvalidParameterValue error.
    Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
    
    InfoType (string) -- [REQUIRED]
    The type of information to retrieve.
    
    
    """
    pass

def swap_environment_cnames(SourceEnvironmentId=None, SourceEnvironmentName=None, DestinationEnvironmentId=None, DestinationEnvironmentName=None):
    """
    Swaps the CNAMEs of two environments.
    See also: AWS API Documentation
    
    Examples
    The following operation swaps the assigned subdomains of two environments:
    Expected Output:
    
    :example: response = client.swap_environment_cnames(
        SourceEnvironmentId='string',
        SourceEnvironmentName='string',
        DestinationEnvironmentId='string',
        DestinationEnvironmentName='string'
    )
    
    
    :type SourceEnvironmentId: string
    :param SourceEnvironmentId: The ID of the source environment.
            Condition: You must specify at least the SourceEnvironmentID or the SourceEnvironmentName . You may also specify both. If you specify the SourceEnvironmentId , you must specify the DestinationEnvironmentId .
            

    :type SourceEnvironmentName: string
    :param SourceEnvironmentName: The name of the source environment.
            Condition: You must specify at least the SourceEnvironmentID or the SourceEnvironmentName . You may also specify both. If you specify the SourceEnvironmentName , you must specify the DestinationEnvironmentName .
            

    :type DestinationEnvironmentId: string
    :param DestinationEnvironmentId: The ID of the destination environment.
            Condition: You must specify at least the DestinationEnvironmentID or the DestinationEnvironmentName . You may also specify both. You must specify the SourceEnvironmentId with the DestinationEnvironmentId .
            

    :type DestinationEnvironmentName: string
    :param DestinationEnvironmentName: The name of the destination environment.
            Condition: You must specify at least the DestinationEnvironmentID or the DestinationEnvironmentName . You may also specify both. You must specify the SourceEnvironmentName with the DestinationEnvironmentName .
            

    :return: response = client.swap_environment_cnames(
        DestinationEnvironmentName='my-env-green',
        SourceEnvironmentName='my-env-blue',
    )
    
    print(response)
    
    
    """
    pass

def terminate_environment(EnvironmentId=None, EnvironmentName=None, TerminateResources=None, ForceTerminate=None):
    """
    Terminates the specified environment.
    See also: AWS API Documentation
    
    Examples
    The following operation terminates an Elastic Beanstalk environment named my-env:
    Expected Output:
    
    :example: response = client.terminate_environment(
        EnvironmentId='string',
        EnvironmentName='string',
        TerminateResources=True|False,
        ForceTerminate=True|False
    )
    
    
    :type EnvironmentId: string
    :param EnvironmentId: The ID of the environment to terminate.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :type EnvironmentName: string
    :param EnvironmentName: The name of the environment to terminate.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :type TerminateResources: boolean
    :param TerminateResources: Indicates whether the associated AWS resources should shut down when the environment is terminated:
            true : The specified environment as well as the associated AWS resources, such as Auto Scaling group and LoadBalancer, are terminated.
            false : AWS Elastic Beanstalk resource management is removed from the environment, but the AWS resources continue to operate.
            For more information, see the AWS Elastic Beanstalk User Guide.
            Default: true
            Valid Values: true | false
            

    :type ForceTerminate: boolean
    :param ForceTerminate: Terminates the target environment even if another environment in the same group is dependent on it.

    :rtype: dict
    :return: {
        'EnvironmentName': 'string',
        'EnvironmentId': 'string',
        'ApplicationName': 'string',
        'VersionLabel': 'string',
        'SolutionStackName': 'string',
        'PlatformArn': 'string',
        'TemplateName': 'string',
        'Description': 'string',
        'EndpointURL': 'string',
        'CNAME': 'string',
        'DateCreated': datetime(2015, 1, 1),
        'DateUpdated': datetime(2015, 1, 1),
        'Status': 'Launching'|'Updating'|'Ready'|'Terminating'|'Terminated',
        'AbortableOperationInProgress': True|False,
        'Health': 'Green'|'Yellow'|'Red'|'Grey',
        'HealthStatus': 'NoData'|'Unknown'|'Pending'|'Ok'|'Info'|'Warning'|'Degraded'|'Severe',
        'Resources': {
            'LoadBalancer': {
                'LoadBalancerName': 'string',
                'Domain': 'string',
                'Listeners': [
                    {
                        'Protocol': 'string',
                        'Port': 123
                    },
                ]
            }
        },
        'Tier': {
            'Name': 'string',
            'Type': 'string',
            'Version': 'string'
        },
        'EnvironmentLinks': [
            {
                'LinkName': 'string',
                'EnvironmentName': 'string'
            },
        ]
    }
    
    
    :returns: 
    Launching : Environment is in the process of initial deployment.
    Updating : Environment is in the process of updating its configuration settings or application version.
    Ready : Environment is available to have an action performed on it, such as update or terminate.
    Terminating : Environment is in the shut-down process.
    Terminated : Environment is not running.
    
    """
    pass

def update_application(ApplicationName=None, Description=None):
    """
    Updates the specified application to have the specified properties.
    See also: AWS API Documentation
    
    Examples
    The following operation updates the description of an application named my-app:
    Expected Output:
    
    :example: response = client.update_application(
        ApplicationName='string',
        Description='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]
            The name of the application to update. If no such application is found, UpdateApplication returns an InvalidParameterValue error.
            

    :type Description: string
    :param Description: A new description for the application.
            Default: If not specified, AWS Elastic Beanstalk does not update the description.
            

    :rtype: dict
    :return: {
        'Application': {
            'ApplicationName': 'string',
            'Description': 'string',
            'DateCreated': datetime(2015, 1, 1),
            'DateUpdated': datetime(2015, 1, 1),
            'Versions': [
                'string',
            ],
            'ConfigurationTemplates': [
                'string',
            ],
            'ResourceLifecycleConfig': {
                'ServiceRole': 'string',
                'VersionLifecycleConfig': {
                    'MaxCountRule': {
                        'Enabled': True|False,
                        'MaxCount': 123,
                        'DeleteSourceFromS3': True|False
                    },
                    'MaxAgeRule': {
                        'Enabled': True|False,
                        'MaxAgeInDays': 123,
                        'DeleteSourceFromS3': True|False
                    }
                }
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_application_resource_lifecycle(ApplicationName=None, ResourceLifecycleConfig=None):
    """
    Modifies lifecycle settings for an application.
    See also: AWS API Documentation
    
    
    :example: response = client.update_application_resource_lifecycle(
        ApplicationName='string',
        ResourceLifecycleConfig={
            'ServiceRole': 'string',
            'VersionLifecycleConfig': {
                'MaxCountRule': {
                    'Enabled': True|False,
                    'MaxCount': 123,
                    'DeleteSourceFromS3': True|False
                },
                'MaxAgeRule': {
                    'Enabled': True|False,
                    'MaxAgeInDays': 123,
                    'DeleteSourceFromS3': True|False
                }
            }
        }
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]
            The name of the application.
            

    :type ResourceLifecycleConfig: dict
    :param ResourceLifecycleConfig: [REQUIRED]
            The lifecycle configuration.
            ServiceRole (string) --The ARN of an IAM service role that Elastic Beanstalk has permission to assume.
            VersionLifecycleConfig (dict) --The application version lifecycle configuration.
            MaxCountRule (dict) --Specify a max count rule to restrict the number of application versions that are retained for an application.
            Enabled (boolean) -- [REQUIRED]Specify true to apply the rule, or false to disable it.
            MaxCount (integer) --Specify the maximum number of application versions to retain.
            DeleteSourceFromS3 (boolean) --Set to true to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.
            MaxAgeRule (dict) --Specify a max age rule to restrict the length of time that application versions are retained for an application.
            Enabled (boolean) -- [REQUIRED]Specify true to apply the rule, or false to disable it.
            MaxAgeInDays (integer) --Specify the number of days to retain an application versions.
            DeleteSourceFromS3 (boolean) --Set to true to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.
            
            

    :rtype: dict
    :return: {
        'ApplicationName': 'string',
        'ResourceLifecycleConfig': {
            'ServiceRole': 'string',
            'VersionLifecycleConfig': {
                'MaxCountRule': {
                    'Enabled': True|False,
                    'MaxCount': 123,
                    'DeleteSourceFromS3': True|False
                },
                'MaxAgeRule': {
                    'Enabled': True|False,
                    'MaxAgeInDays': 123,
                    'DeleteSourceFromS3': True|False
                }
            }
        }
    }
    
    
    """
    pass

def update_application_version(ApplicationName=None, VersionLabel=None, Description=None):
    """
    Updates the specified application version to have the specified properties.
    See also: AWS API Documentation
    
    Examples
    The following operation updates the description of an application version named 22a0-stage-150819_185942:
    Expected Output:
    
    :example: response = client.update_application_version(
        ApplicationName='string',
        VersionLabel='string',
        Description='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]
            The name of the application associated with this version.
            If no application is found with this name, UpdateApplication returns an InvalidParameterValue error.
            

    :type VersionLabel: string
    :param VersionLabel: [REQUIRED]
            The name of the version to update.
            If no application version is found with this label, UpdateApplication returns an InvalidParameterValue error.
            

    :type Description: string
    :param Description: A new description for this version.

    :rtype: dict
    :return: {
        'ApplicationVersion': {
            'ApplicationName': 'string',
            'Description': 'string',
            'VersionLabel': 'string',
            'SourceBuildInformation': {
                'SourceType': 'Git'|'Zip',
                'SourceRepository': 'CodeCommit'|'S3',
                'SourceLocation': 'string'
            },
            'BuildArn': 'string',
            'SourceBundle': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'DateCreated': datetime(2015, 1, 1),
            'DateUpdated': datetime(2015, 1, 1),
            'Status': 'Processed'|'Unprocessed'|'Failed'|'Processing'|'Building'
        }
    }
    
    
    :returns: 
    Git
    Zip
    
    """
    pass

def update_configuration_template(ApplicationName=None, TemplateName=None, Description=None, OptionSettings=None, OptionsToRemove=None):
    """
    Updates the specified configuration template to have the specified properties or configuration option values.
    Related Topics
    See also: AWS API Documentation
    
    Examples
    The following operation removes the configured CloudWatch custom health metrics configuration ConfigDocument from a saved configuration template named my-template:
    Expected Output:
    
    :example: response = client.update_configuration_template(
        ApplicationName='string',
        TemplateName='string',
        Description='string',
        OptionSettings=[
            {
                'ResourceName': 'string',
                'Namespace': 'string',
                'OptionName': 'string',
                'Value': 'string'
            },
        ],
        OptionsToRemove=[
            {
                'ResourceName': 'string',
                'Namespace': 'string',
                'OptionName': 'string'
            },
        ]
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]
            The name of the application associated with the configuration template to update.
            If no application is found with this name, UpdateConfigurationTemplate returns an InvalidParameterValue error.
            

    :type TemplateName: string
    :param TemplateName: [REQUIRED]
            The name of the configuration template to update.
            If no configuration template is found with this name, UpdateConfigurationTemplate returns an InvalidParameterValue error.
            

    :type Description: string
    :param Description: A new description for the configuration.

    :type OptionSettings: list
    :param OptionSettings: A list of configuration option settings to update with the new specified option value.
            (dict) --A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to Option Values in the AWS Elastic Beanstalk Developer Guide .
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            Value (string) --The current value for the configuration option.
            
            

    :type OptionsToRemove: list
    :param OptionsToRemove: A list of configuration options to remove from the configuration set.
            Constraint: You can remove only UserDefined configuration options.
            (dict) --A specification identifying an individual configuration option.
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            
            

    :rtype: dict
    :return: {
        'SolutionStackName': 'string',
        'PlatformArn': 'string',
        'ApplicationName': 'string',
        'TemplateName': 'string',
        'Description': 'string',
        'EnvironmentName': 'string',
        'DeploymentStatus': 'deployed'|'pending'|'failed',
        'DateCreated': datetime(2015, 1, 1),
        'DateUpdated': datetime(2015, 1, 1),
        'OptionSettings': [
            {
                'ResourceName': 'string',
                'Namespace': 'string',
                'OptionName': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    ApplicationName (string) -- [REQUIRED]
    The name of the application associated with the configuration template to update.
    If no application is found with this name, UpdateConfigurationTemplate returns an InvalidParameterValue error.
    
    TemplateName (string) -- [REQUIRED]
    The name of the configuration template to update.
    If no configuration template is found with this name, UpdateConfigurationTemplate returns an InvalidParameterValue error.
    
    Description (string) -- A new description for the configuration.
    OptionSettings (list) -- A list of configuration option settings to update with the new specified option value.
    
    (dict) --A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to Option Values in the AWS Elastic Beanstalk Developer Guide .
    
    ResourceName (string) --A unique resource name for a time-based scaling configuration option.
    
    Namespace (string) --A unique namespace identifying the option's associated AWS resource.
    
    OptionName (string) --The name of the configuration option.
    
    Value (string) --The current value for the configuration option.
    
    
    
    
    
    OptionsToRemove (list) -- A list of configuration options to remove from the configuration set.
    Constraint: You can remove only UserDefined configuration options.
    
    (dict) --A specification identifying an individual configuration option.
    
    ResourceName (string) --A unique resource name for a time-based scaling configuration option.
    
    Namespace (string) --A unique namespace identifying the option's associated AWS resource.
    
    OptionName (string) --The name of the configuration option.
    
    
    
    
    
    
    """
    pass

def update_environment(ApplicationName=None, EnvironmentId=None, EnvironmentName=None, GroupName=None, Description=None, Tier=None, VersionLabel=None, TemplateName=None, SolutionStackName=None, PlatformArn=None, OptionSettings=None, OptionsToRemove=None):
    """
    Updates the environment description, deploys a new application version, updates the configuration settings to an entirely new configuration template, or updates select configuration option values in the running environment.
    Attempting to update both the release and configuration is not allowed and AWS Elastic Beanstalk returns an InvalidParameterCombination error.
    When updating the configuration settings to a new template or individual settings, a draft configuration is created and  DescribeConfigurationSettings for this environment returns two setting descriptions with different DeploymentStatus values.
    See also: AWS API Documentation
    
    Examples
    The following operation updates an environment named "my-env" to version "v2" of the application to which it belongs:
    Expected Output:
    The following operation configures several options in the aws:elb:loadbalancer namespace:
    Expected Output:
    
    :example: response = client.update_environment(
        ApplicationName='string',
        EnvironmentId='string',
        EnvironmentName='string',
        GroupName='string',
        Description='string',
        Tier={
            'Name': 'string',
            'Type': 'string',
            'Version': 'string'
        },
        VersionLabel='string',
        TemplateName='string',
        SolutionStackName='string',
        PlatformArn='string',
        OptionSettings=[
            {
                'ResourceName': 'string',
                'Namespace': 'string',
                'OptionName': 'string',
                'Value': 'string'
            },
        ],
        OptionsToRemove=[
            {
                'ResourceName': 'string',
                'Namespace': 'string',
                'OptionName': 'string'
            },
        ]
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: The name of the application with which the environment is associated.

    :type EnvironmentId: string
    :param EnvironmentId: The ID of the environment to update.
            If no environment with this ID exists, AWS Elastic Beanstalk returns an InvalidParameterValue error.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :type EnvironmentName: string
    :param EnvironmentName: The name of the environment to update. If no environment with this name exists, AWS Elastic Beanstalk returns an InvalidParameterValue error.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            

    :type GroupName: string
    :param GroupName: The name of the group to which the target environment belongs. Specify a group name only if the environment's name is specified in an environment manifest and not with the environment name or environment ID parameters. See Environment Manifest (env.yaml) for details.

    :type Description: string
    :param Description: If this parameter is specified, AWS Elastic Beanstalk updates the description of this environment.

    :type Tier: dict
    :param Tier: This specifies the tier to use to update the environment.
            Condition: At this time, if you change the tier version, name, or type, AWS Elastic Beanstalk returns InvalidParameterValue error.
            Name (string) --The name of this environment tier.
            Type (string) --The type of this environment tier.
            Version (string) --The version of this environment tier.
            

    :type VersionLabel: string
    :param VersionLabel: If this parameter is specified, AWS Elastic Beanstalk deploys the named application version to the environment. If no such application version is found, returns an InvalidParameterValue error.

    :type TemplateName: string
    :param TemplateName: If this parameter is specified, AWS Elastic Beanstalk deploys this configuration template to the environment. If no such configuration template is found, AWS Elastic Beanstalk returns an InvalidParameterValue error.

    :type SolutionStackName: string
    :param SolutionStackName: This specifies the platform version that the environment will run after the environment is updated.

    :type PlatformArn: string
    :param PlatformArn: The ARN of the platform, if used.

    :type OptionSettings: list
    :param OptionSettings: If specified, AWS Elastic Beanstalk updates the configuration set associated with the running environment and sets the specified configuration options to the requested value.
            (dict) --A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to Option Values in the AWS Elastic Beanstalk Developer Guide .
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            Value (string) --The current value for the configuration option.
            
            

    :type OptionsToRemove: list
    :param OptionsToRemove: A list of custom user-defined configuration options to remove from the configuration set for this environment.
            (dict) --A specification identifying an individual configuration option.
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            
            

    :rtype: dict
    :return: {
        'EnvironmentName': 'string',
        'EnvironmentId': 'string',
        'ApplicationName': 'string',
        'VersionLabel': 'string',
        'SolutionStackName': 'string',
        'PlatformArn': 'string',
        'TemplateName': 'string',
        'Description': 'string',
        'EndpointURL': 'string',
        'CNAME': 'string',
        'DateCreated': datetime(2015, 1, 1),
        'DateUpdated': datetime(2015, 1, 1),
        'Status': 'Launching'|'Updating'|'Ready'|'Terminating'|'Terminated',
        'AbortableOperationInProgress': True|False,
        'Health': 'Green'|'Yellow'|'Red'|'Grey',
        'HealthStatus': 'NoData'|'Unknown'|'Pending'|'Ok'|'Info'|'Warning'|'Degraded'|'Severe',
        'Resources': {
            'LoadBalancer': {
                'LoadBalancerName': 'string',
                'Domain': 'string',
                'Listeners': [
                    {
                        'Protocol': 'string',
                        'Port': 123
                    },
                ]
            }
        },
        'Tier': {
            'Name': 'string',
            'Type': 'string',
            'Version': 'string'
        },
        'EnvironmentLinks': [
            {
                'LinkName': 'string',
                'EnvironmentName': 'string'
            },
        ]
    }
    
    
    :returns: 
    Launching : Environment is in the process of initial deployment.
    Updating : Environment is in the process of updating its configuration settings or application version.
    Ready : Environment is available to have an action performed on it, such as update or terminate.
    Terminating : Environment is in the shut-down process.
    Terminated : Environment is not running.
    
    """
    pass

def validate_configuration_settings(ApplicationName=None, TemplateName=None, EnvironmentName=None, OptionSettings=None):
    """
    Takes a set of configuration settings and either a configuration template or environment, and determines whether those values are valid.
    This action returns a list of messages indicating any errors or warnings associated with the selection of option values.
    See also: AWS API Documentation
    
    Examples
    The following operation validates a CloudWatch custom metrics config document:
    Expected Output:
    
    :example: response = client.validate_configuration_settings(
        ApplicationName='string',
        TemplateName='string',
        EnvironmentName='string',
        OptionSettings=[
            {
                'ResourceName': 'string',
                'Namespace': 'string',
                'OptionName': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]
            The name of the application that the configuration template or environment belongs to.
            

    :type TemplateName: string
    :param TemplateName: The name of the configuration template to validate the settings against.
            Condition: You cannot specify both this and an environment name.
            

    :type EnvironmentName: string
    :param EnvironmentName: The name of the environment to validate the settings against.
            Condition: You cannot specify both this and a configuration template name.
            

    :type OptionSettings: list
    :param OptionSettings: [REQUIRED]
            A list of the options and desired values to evaluate.
            (dict) --A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to Option Values in the AWS Elastic Beanstalk Developer Guide .
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            Value (string) --The current value for the configuration option.
            
            

    :rtype: dict
    :return: {
        'Messages': [
            {
                'Message': 'string',
                'Severity': 'error'|'warning',
                'Namespace': 'string',
                'OptionName': 'string'
            },
        ]
    }
    
    
    :returns: 
    error : This message indicates that this is not a valid setting for an option.
    warning : This message is providing information you should take into account.
    
    """
    pass

