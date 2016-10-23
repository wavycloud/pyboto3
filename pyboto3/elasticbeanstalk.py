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


def abort_environment_update(EnvironmentId=None, EnvironmentName=None):
    """
    :param EnvironmentId: This specifies the ID of the environment with the in-progress update that you want to cancel.
    :type EnvironmentId: string
    :param EnvironmentName: This specifies the name of the environment with the in-progress update that you want to cancel.
    :type EnvironmentName: string
    """
    pass


def apply_environment_managed_action(EnvironmentName=None, EnvironmentId=None, ActionId=None):
    """
    :param EnvironmentName: The name of the target environment.
    :type EnvironmentName: string
    :param EnvironmentId: The environment ID of the target environment.
    :type EnvironmentId: string
    :param ActionId: [REQUIRED]
            The action ID of the scheduled managed action to execute.
            
    :type ActionId: string
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


def check_dns_availability(CNAMEPrefix=None):
    """
    :param CNAMEPrefix: [REQUIRED]
            The prefix used when this CNAME is reserved.
            Return typedict
            ReturnsResponse Syntax{
              'Available': True|False,
              'FullyQualifiedCNAME': 'string'
            }
            Response Structure
            (dict) --Indicates if the specified CNAME is available.
            Available (boolean) --Indicates if the specified CNAME is available:
            true : The CNAME is available.
            false : The CNAME is not available.
            FullyQualifiedCNAME (string) --The fully qualified CNAME to reserve when CreateEnvironment is called with the provided prefix.
            
            Examples
            The following operation checks the availability of the subdomain my-cname:
            response = client.check_dns_availability(
              CNAMEPrefix='my-cname',
            )
            print(response)
            Expected Output:
            {
              'Available': True,
              'FullyQualifiedCNAME': 'my-cname.us-west-2.elasticbeanstalk.com',
              'ResponseMetadata': {
                '...': '...',
              },
            }
            
    :type CNAMEPrefix: string
    """
    pass


def compose_environments(ApplicationName=None, GroupName=None, VersionLabels=None):
    """
    :param ApplicationName: The name of the application to which the specified source bundles belong.
    :type ApplicationName: string
    :param GroupName: The name of the group to which the target environments belong. Specify a group name only if the environment name defined in each target environment's manifest ends with a + (plus) character. See Environment Manifest (env.yaml) for details.
    :type GroupName: string
    :param VersionLabels: A list of version labels, specifying one or more application source bundles that belong to the target application. Each source bundle must include an environment manifest that specifies the name of the environment and the name of the solution stack to use, and optionally can specify environment links to create.
            (string) --
            
    :type VersionLabels: list
    """
    pass


def create_application(ApplicationName=None, Description=None):
    """
    :param ApplicationName: [REQUIRED]
            The name of the application.
            Constraint: This name must be unique within your account. If the specified name already exists, the action returns an InvalidParameterValue error.
            
    :type ApplicationName: string
    :param Description: Describes the application.
    :type Description: string
    """
    pass


def create_application_version(ApplicationName=None, VersionLabel=None, Description=None, SourceBuildInformation=None,
                               SourceBundle=None, AutoCreateApplication=None, Process=None):
    """
    :param ApplicationName: [REQUIRED]
            The name of the application. If no application is found with this name, and AutoCreateApplication is false , returns an InvalidParameterValue error.
            
    :type ApplicationName: string
    :param VersionLabel: [REQUIRED]
            A label identifying this version.
            Constraint: Must be unique per application. If an application version already exists with this label for the specified application, AWS Elastic Beanstalk returns an InvalidParameterValue error.
            
    :type VersionLabel: string
    :param Description: Describes this version.
    :type Description: string
    :param SourceBuildInformation: 
            SourceType (string) -- [REQUIRED]
            SourceRepository (string) -- [REQUIRED]
            SourceLocation (string) -- [REQUIRED]
            
    :type SourceBuildInformation: dict
    :param SourceBundle: The Amazon S3 bucket and key that identify the location of the source bundle for this version.
            If data found at the Amazon S3 location exceeds the maximum allowed source bundle size, AWS Elastic Beanstalk returns an InvalidParameterValue error. The maximum size allowed is 512 MB.
            Default: If not specified, AWS Elastic Beanstalk uses a sample application. If only partially specified (for example, a bucket is provided but not the key) or if no data is found at the Amazon S3 location, AWS Elastic Beanstalk returns an InvalidParameterCombination error.
            S3Bucket (string) --The Amazon S3 bucket where the data is located.
            S3Key (string) --The Amazon S3 key where the data is located.
            
    :type SourceBundle: dict
    :param AutoCreateApplication: Determines how the system behaves if the specified application for this version does not already exist:
            true : Automatically creates the specified application for this release if it does not already exist.
            false : Throws an InvalidParameterValue if the specified application for this release does not already exist.
            Default: false
            Valid Values: true | false
            
    :type AutoCreateApplication: boolean
    :param Process: Preprocesses and validates the environment manifest and configuration files in the source bundle. Validating configuration files can identify issues prior to deploying the application version to an environment.
    :type Process: boolean
    """
    pass


def create_configuration_template(ApplicationName=None, TemplateName=None, SolutionStackName=None,
                                  SourceConfiguration=None, EnvironmentId=None, Description=None, OptionSettings=None):
    """
    :param ApplicationName: [REQUIRED]
            The name of the application to associate with this configuration template. If no application is found with this name, AWS Elastic Beanstalk returns an InvalidParameterValue error.
            
    :type ApplicationName: string
    :param TemplateName: [REQUIRED]
            The name of the configuration template.
            Constraint: This name must be unique per application.
            Default: If a configuration template already exists with this name, AWS Elastic Beanstalk returns an InvalidParameterValue error.
            
    :type TemplateName: string
    :param SolutionStackName: The name of the solution stack used by this configuration. The solution stack specifies the operating system, architecture, and application server for a configuration template. It determines the set of configuration options as well as the possible and default values.
            Use ListAvailableSolutionStacks to obtain a list of available solution stacks.
            A solution stack name or a source configuration parameter must be specified, otherwise AWS Elastic Beanstalk returns an InvalidParameterValue error.
            If a solution stack name is not specified and the source configuration parameter is specified, AWS Elastic Beanstalk uses the same solution stack as the source configuration template.
            
    :type SolutionStackName: string
    :param SourceConfiguration: If specified, AWS Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.
            Values specified in the OptionSettings parameter of this call overrides any values obtained from the SourceConfiguration .
            If no configuration template is found, returns an InvalidParameterValue error.
            Constraint: If both the solution stack name parameter and the source configuration parameters are specified, the solution stack of the source configuration template must match the specified solution stack name or else AWS Elastic Beanstalk returns an InvalidParameterCombination error.
            ApplicationName (string) --The name of the application associated with the configuration.
            TemplateName (string) --The name of the configuration template.
            
    :type SourceConfiguration: dict
    :param EnvironmentId: The ID of the environment used with this configuration template.
    :type EnvironmentId: string
    :param Description: Describes this configuration.
    :type Description: string
    :param OptionSettings: If specified, AWS Elastic Beanstalk sets the specified configuration option to the requested value. The new value overrides the value obtained from the solution stack or the source configuration template.
            (dict) --A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to Option Values in the AWS Elastic Beanstalk Developer Guide .
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            Value (string) --The current value for the configuration option.
            
            
    :type OptionSettings: list
    """
    pass


def create_environment(ApplicationName=None, EnvironmentName=None, GroupName=None, Description=None, CNAMEPrefix=None,
                       Tier=None, Tags=None, VersionLabel=None, TemplateName=None, SolutionStackName=None,
                       OptionSettings=None, OptionsToRemove=None):
    """
    :param ApplicationName: [REQUIRED]
            The name of the application that contains the version to be deployed.
            If no application is found with this name, CreateEnvironment returns an InvalidParameterValue error.
            
    :type ApplicationName: string
    :param EnvironmentName: A unique name for the deployment environment. Used in the application URL.
            Constraint: Must be from 4 to 40 characters in length. The name can contain only letters, numbers, and hyphens. It cannot start or end with a hyphen. This name must be unique in your account. If the specified name already exists, AWS Elastic Beanstalk returns an InvalidParameterValue error.
            Default: If the CNAME parameter is not specified, the environment name becomes part of the CNAME, and therefore part of the visible URL for your application.
            
    :type EnvironmentName: string
    :param GroupName: The name of the group to which the target environment belongs. Specify a group name only if the environment's name is specified in an environment manifest and not with the environment name parameter. See Environment Manifest (env.yaml) for details.
    :type GroupName: string
    :param Description: Describes this environment.
    :type Description: string
    :param CNAMEPrefix: If specified, the environment attempts to use this value as the prefix for the CNAME. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.
    :type CNAMEPrefix: string
    :param Tier: This specifies the tier to use for creating this environment.
            Name (string) --The name of this environment tier.
            Type (string) --The type of this environment tier.
            Version (string) --The version of this environment tier.
            
    :type Tier: dict
    :param Tags: This specifies the tags applied to resources in the environment.
            (dict) --Describes a tag applied to a resource in an environment.
            Key (string) --The key of the tag.
            Value (string) --The value of the tag.
            
            
    :type Tags: list
    :param VersionLabel: The name of the application version to deploy.
            If the specified application has no associated application versions, AWS Elastic Beanstalk UpdateEnvironment returns an InvalidParameterValue error.
            Default: If not specified, AWS Elastic Beanstalk attempts to launch the sample application in the container.
            
    :type VersionLabel: string
    :param TemplateName: The name of the configuration template to use in deployment. If no configuration template is found with this name, AWS Elastic Beanstalk returns an InvalidParameterValue error.
            Condition: You must specify either this parameter or a SolutionStackName , but not both. If you specify both, AWS Elastic Beanstalk returns an InvalidParameterCombination error. If you do not specify either, AWS Elastic Beanstalk returns a MissingRequiredParameter error.
            
    :type TemplateName: string
    :param SolutionStackName: This is an alternative to specifying a template name. If specified, AWS Elastic Beanstalk sets the configuration values to the default values associated with the specified solution stack.
            Condition: You must specify either this or a TemplateName , but not both. If you specify both, AWS Elastic Beanstalk returns an InvalidParameterCombination error. If you do not specify either, AWS Elastic Beanstalk returns a MissingRequiredParameter error.
            
    :type SolutionStackName: string
    :param OptionSettings: If specified, AWS Elastic Beanstalk sets the specified configuration options to the requested value in the configuration set for the new environment. These override the values obtained from the solution stack or the configuration template.
            (dict) --A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to Option Values in the AWS Elastic Beanstalk Developer Guide .
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            Value (string) --The current value for the configuration option.
            
            
    :type OptionSettings: list
    :param OptionsToRemove: A list of custom user-defined configuration options to remove from the configuration set for this new environment.
            (dict) --A specification identifying an individual configuration option.
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            
            
    :type OptionsToRemove: list
    """
    pass


def create_storage_location():
    """
    """
    pass


def delete_application(ApplicationName=None, TerminateEnvByForce=None):
    """
    :param ApplicationName: [REQUIRED]
            The name of the application to delete.
            
    :type ApplicationName: string
    :param TerminateEnvByForce: When set to true, running environments will be terminated before deleting the application.
    :type TerminateEnvByForce: boolean
    """
    pass


def delete_application_version(ApplicationName=None, VersionLabel=None, DeleteSourceBundle=None):
    """
    :param ApplicationName: [REQUIRED]
            The name of the application to delete releases from.
            
    :type ApplicationName: string
    :param VersionLabel: [REQUIRED]
            The label of the version to delete.
            
    :type VersionLabel: string
    :param DeleteSourceBundle: Indicates whether to delete the associated source bundle from Amazon S3:
            true : An attempt is made to delete the associated Amazon S3 source bundle specified at time of creation.
            false : No action is taken on the Amazon S3 source bundle specified at time of creation.
            Valid Values: true | false
            
    :type DeleteSourceBundle: boolean
    """
    pass


def delete_configuration_template(ApplicationName=None, TemplateName=None):
    """
    :param ApplicationName: [REQUIRED]
            The name of the application to delete the configuration template from.
            
    :type ApplicationName: string
    :param TemplateName: [REQUIRED]
            The name of the configuration template to delete.
            
    :type TemplateName: string
    """
    pass


def delete_environment_configuration(ApplicationName=None, EnvironmentName=None):
    """
    :param ApplicationName: [REQUIRED]
            The name of the application the environment is associated with.
            
    :type ApplicationName: string
    :param EnvironmentName: [REQUIRED]
            The name of the environment to delete the draft configuration from.
            
    :type EnvironmentName: string
    """
    pass


def describe_application_versions(ApplicationName=None, VersionLabels=None, MaxRecords=None, NextToken=None):
    """
    :param ApplicationName: If specified, AWS Elastic Beanstalk restricts the returned descriptions to only include ones that are associated with the specified application.
    :type ApplicationName: string
    :param VersionLabels: If specified, restricts the returned descriptions to only include ones that have the specified version labels.
            (string) --
            
    :type VersionLabels: list
    :param MaxRecords: Specify a maximum number of application versions to paginate in the request.
    :type MaxRecords: integer
    :param NextToken: Specify a next token to retrieve the next page in a paginated request.
    :type NextToken: string
    """
    pass


def describe_applications(ApplicationNames=None):
    """
    :param ApplicationNames: If specified, AWS Elastic Beanstalk restricts the returned descriptions to only include those with the specified names.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
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
                  ]
                },
              ]
            }
            Response Structure
            (dict) --Result message containing a list of application descriptions.
            Applications (list) --This parameter contains a list of ApplicationDescription .
            (dict) --Describes the properties of an application.
            ApplicationName (string) --The name of the application.
            Description (string) --User-defined description of the application.
            DateCreated (datetime) --The date when the application was created.
            DateUpdated (datetime) --The date when the application was last modified.
            Versions (list) --The names of the versions for this application.
            (string) --
            ConfigurationTemplates (list) --The names of the configuration templates associated with this application.
            (string) --
            
            
            Examples
            The following operation retrieves information about applications in the current region:
            response = client.describe_applications(
            )
            print(response)
            Expected Output:
            {
              'Applications': [
                {
                  'ApplicationName': 'ruby',
                  'ConfigurationTemplates': [
                  ],
                  'DateCreated': datetime(2015, 8, 13, 21, 5, 44, 3, 225, 0),
                  'DateUpdated': datetime(2015, 8, 13, 21, 5, 44, 3, 225, 0),
                  'Versions': [
                    'Sample Application',
                  ],
                },
                {
                  'ApplicationName': 'pythonsample',
                  'ConfigurationTemplates': [
                  ],
                  'DateCreated': datetime(2015, 8, 13, 19, 5, 43, 3, 225, 0),
                  'DateUpdated': datetime(2015, 8, 13, 19, 5, 43, 3, 225, 0),
                  'Description': 'Application created from the EB CLI using 'eb init'',
                  'Versions': [
                    'Sample Application',
                  ],
                },
                {
                  'ApplicationName': 'nodejs-example',
                  'ConfigurationTemplates': [
                  ],
                  'DateCreated': datetime(2015, 8, 6, 17, 50, 2, 3, 218, 0),
                  'DateUpdated': datetime(2015, 8, 6, 17, 50, 2, 3, 218, 0),
                  'Versions': [
                    'add elasticache',
                    'First Release',
                  ],
                },
              ],
              'ResponseMetadata': {
                '...': '...',
              },
            }
            
    :type ApplicationNames: list
    """
    pass


def describe_configuration_options(ApplicationName=None, TemplateName=None, EnvironmentName=None,
                                   SolutionStackName=None, Options=None):
    """
    :param ApplicationName: The name of the application associated with the configuration template or environment. Only needed if you want to describe the configuration options associated with either the configuration template or environment.
    :type ApplicationName: string
    :param TemplateName: The name of the configuration template whose configuration options you want to describe.
    :type TemplateName: string
    :param EnvironmentName: The name of the environment whose configuration options you want to describe.
    :type EnvironmentName: string
    :param SolutionStackName: The name of the solution stack whose configuration options you want to describe.
    :type SolutionStackName: string
    :param Options: If specified, restricts the descriptions to only the specified options.
            (dict) --A specification identifying an individual configuration option.
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            
            
    :type Options: list
    """
    pass


def describe_configuration_settings(ApplicationName=None, TemplateName=None, EnvironmentName=None):
    """
    :param ApplicationName: [REQUIRED]
            The application for the environment or configuration template.
            
    :type ApplicationName: string
    :param TemplateName: The name of the configuration template to describe.
            Conditional: You must specify either this parameter or an EnvironmentName, but not both. If you specify both, AWS Elastic Beanstalk returns an InvalidParameterCombination error. If you do not specify either, AWS Elastic Beanstalk returns a MissingRequiredParameter error.
            
    :type TemplateName: string
    :param EnvironmentName: The name of the environment to describe.
            Condition: You must specify either this or a TemplateName, but not both. If you specify both, AWS Elastic Beanstalk returns an InvalidParameterCombination error. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentName: string
    """
    pass


def describe_environment_health(EnvironmentName=None, EnvironmentId=None, AttributeNames=None):
    """
    :param EnvironmentName: Specifies the AWS Elastic Beanstalk environment name.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentName: string
    :param EnvironmentId: Specifies the AWS Elastic Beanstalk environment ID.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentId: string
    :param AttributeNames: Specifies the response elements you wish to receive. If no attribute names are specified, AWS Elastic Beanstalk only returns the name of the environment.
            (string) --
            
    :type AttributeNames: list
    """
    pass


def describe_environment_managed_action_history(EnvironmentId=None, EnvironmentName=None, NextToken=None,
                                                MaxItems=None):
    """
    :param EnvironmentId: The environment ID of the target environment.
    :type EnvironmentId: string
    :param EnvironmentName: The name of the target environment.
    :type EnvironmentName: string
    :param NextToken: The pagination token returned by a previous request.
    :type NextToken: string
    :param MaxItems: The maximum number of items to return for a single request.
    :type MaxItems: integer
    """
    pass


def describe_environment_managed_actions(EnvironmentName=None, EnvironmentId=None, Status=None):
    """
    :param EnvironmentName: The name of the target environment.
    :type EnvironmentName: string
    :param EnvironmentId: The environment ID of the target environment.
    :type EnvironmentId: string
    :param Status: To show only actions with a particular status, specify a status.
    :type Status: string
    """
    pass


def describe_environment_resources(EnvironmentId=None, EnvironmentName=None):
    """
    :param EnvironmentId: The ID of the environment to retrieve AWS resource usage data.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentId: string
    :param EnvironmentName: The name of the environment to retrieve AWS resource usage data.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentName: string
    """
    pass


def describe_environments(ApplicationName=None, VersionLabel=None, EnvironmentIds=None, EnvironmentNames=None,
                          IncludeDeleted=None, IncludedDeletedBackTo=None):
    """
    :param ApplicationName: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application.
    :type ApplicationName: string
    :param VersionLabel: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application version.
    :type VersionLabel: string
    :param EnvironmentIds: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified IDs.
            (string) --
            
    :type EnvironmentIds: list
    :param EnvironmentNames: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified names.
            (string) --
            
    :type EnvironmentNames: list
    :param IncludeDeleted: Indicates whether to include deleted environments:
            true : Environments that have been deleted after IncludedDeletedBackTo are displayed.false : Do not include deleted environments.
            
    :type IncludeDeleted: boolean
    :param IncludedDeletedBackTo: If specified when IncludeDeleted is set to true , then environments deleted after this date are displayed.
    :type IncludedDeletedBackTo: datetime
    """
    pass


def describe_events(ApplicationName=None, VersionLabel=None, TemplateName=None, EnvironmentId=None,
                    EnvironmentName=None, RequestId=None, Severity=None, StartTime=None, EndTime=None, MaxRecords=None,
                    NextToken=None):
    """
    :param ApplicationName: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those associated with this application.
    :type ApplicationName: string
    :param VersionLabel: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this application version.
    :type VersionLabel: string
    :param TemplateName: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that are associated with this environment configuration.
    :type TemplateName: string
    :param EnvironmentId: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.
    :type EnvironmentId: string
    :param EnvironmentName: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.
    :type EnvironmentName: string
    :param RequestId: If specified, AWS Elastic Beanstalk restricts the described events to include only those associated with this request ID.
    :type RequestId: string
    :param Severity: If specified, limits the events returned from this call to include only those with the specified severity or higher.
    :type Severity: string
    :param StartTime: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur on or after this time.
    :type StartTime: datetime
    :param EndTime: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur up to, but not including, the EndTime .
    :type EndTime: datetime
    :param MaxRecords: Specifies the maximum number of events that can be returned, beginning with the most recent event.
    :type MaxRecords: integer
    :param NextToken: Pagination token. If specified, the events return the next batch of results.
    :type NextToken: string
    """
    pass


def describe_instances_health(EnvironmentName=None, EnvironmentId=None, AttributeNames=None, NextToken=None):
    """
    :param EnvironmentName: Specifies the AWS Elastic Beanstalk environment name.
    :type EnvironmentName: string
    :param EnvironmentId: Specifies the AWS Elastic Beanstalk environment ID.
    :type EnvironmentId: string
    :param AttributeNames: Specifies the response elements you wish to receive. If no attribute names are specified, AWS Elastic Beanstalk only returns a list of instances.
            (string) --
            
    :type AttributeNames: list
    :param NextToken: Specifies the next token of the request.
    :type NextToken: string
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


def list_available_solution_stacks():
    """
    """
    pass


def rebuild_environment(EnvironmentId=None, EnvironmentName=None):
    """
    :param EnvironmentId: The ID of the environment to rebuild.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentId: string
    :param EnvironmentName: The name of the environment to rebuild.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentName: string
    """
    pass


def request_environment_info(EnvironmentId=None, EnvironmentName=None, InfoType=None):
    """
    :param EnvironmentId: The ID of the environment of the requested data.
            If no such environment is found, RequestEnvironmentInfo returns an InvalidParameterValue error.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentId: string
    :param EnvironmentName: The name of the environment of the requested data.
            If no such environment is found, RequestEnvironmentInfo returns an InvalidParameterValue error.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentName: string
    :param InfoType: [REQUIRED]
            The type of information to request.
            
    :type InfoType: string
    """
    pass


def restart_app_server(EnvironmentId=None, EnvironmentName=None):
    """
    :param EnvironmentId: The ID of the environment to restart the server for.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentId: string
    :param EnvironmentName: The name of the environment to restart the server for.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentName: string
    """
    pass


def retrieve_environment_info(EnvironmentId=None, EnvironmentName=None, InfoType=None):
    """
    :param EnvironmentId: The ID of the data's environment.
            If no such environment is found, returns an InvalidParameterValue error.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentId: string
    :param EnvironmentName: The name of the data's environment.
            If no such environment is found, returns an InvalidParameterValue error.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentName: string
    :param InfoType: [REQUIRED]
            The type of information to retrieve.
            
    :type InfoType: string
    """
    pass


def swap_environment_cnames(SourceEnvironmentId=None, SourceEnvironmentName=None, DestinationEnvironmentId=None,
                            DestinationEnvironmentName=None):
    """
    :param SourceEnvironmentId: The ID of the source environment.
            Condition: You must specify at least the SourceEnvironmentID or the SourceEnvironmentName . You may also specify both. If you specify the SourceEnvironmentId , you must specify the DestinationEnvironmentId .
            
    :type SourceEnvironmentId: string
    :param SourceEnvironmentName: The name of the source environment.
            Condition: You must specify at least the SourceEnvironmentID or the SourceEnvironmentName . You may also specify both. If you specify the SourceEnvironmentName , you must specify the DestinationEnvironmentName .
            
    :type SourceEnvironmentName: string
    :param DestinationEnvironmentId: The ID of the destination environment.
            Condition: You must specify at least the DestinationEnvironmentID or the DestinationEnvironmentName . You may also specify both. You must specify the SourceEnvironmentId with the DestinationEnvironmentId .
            
    :type DestinationEnvironmentId: string
    :param DestinationEnvironmentName: The name of the destination environment.
            Condition: You must specify at least the DestinationEnvironmentID or the DestinationEnvironmentName . You may also specify both. You must specify the SourceEnvironmentName with the DestinationEnvironmentName .
            
    :type DestinationEnvironmentName: string
    """
    pass


def terminate_environment(EnvironmentId=None, EnvironmentName=None, TerminateResources=None, ForceTerminate=None):
    """
    :param EnvironmentId: The ID of the environment to terminate.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentId: string
    :param EnvironmentName: The name of the environment to terminate.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentName: string
    :param TerminateResources: Indicates whether the associated AWS resources should shut down when the environment is terminated:
            true : The specified environment as well as the associated AWS resources, such as Auto Scaling group and LoadBalancer, are terminated.
            false : AWS Elastic Beanstalk resource management is removed from the environment, but the AWS resources continue to operate.
            For more information, see the AWS Elastic Beanstalk User Guide.
            Default: true
            Valid Values: true | false
            
    :type TerminateResources: boolean
    :param ForceTerminate: Terminates the target environment even if another environment in the same group is dependent on it.
    :type ForceTerminate: boolean
    """
    pass


def update_application(ApplicationName=None, Description=None):
    """
    :param ApplicationName: [REQUIRED]
            The name of the application to update. If no such application is found, UpdateApplication returns an InvalidParameterValue error.
            
    :type ApplicationName: string
    :param Description: A new description for the application.
            Default: If not specified, AWS Elastic Beanstalk does not update the description.
            
    :type Description: string
    """
    pass


def update_application_version(ApplicationName=None, VersionLabel=None, Description=None):
    """
    :param ApplicationName: [REQUIRED]
            The name of the application associated with this version.
            If no application is found with this name, UpdateApplication returns an InvalidParameterValue error.
            
    :type ApplicationName: string
    :param VersionLabel: [REQUIRED]
            The name of the version to update.
            If no application version is found with this label, UpdateApplication returns an InvalidParameterValue error.
            
    :type VersionLabel: string
    :param Description: A new description for this release.
    :type Description: string
    """
    pass


def update_configuration_template(ApplicationName=None, TemplateName=None, Description=None, OptionSettings=None,
                                  OptionsToRemove=None):
    """
    :param ApplicationName: [REQUIRED]
            The name of the application associated with the configuration template to update.
            If no application is found with this name, UpdateConfigurationTemplate returns an InvalidParameterValue error.
            
    :type ApplicationName: string
    :param TemplateName: [REQUIRED]
            The name of the configuration template to update.
            If no configuration template is found with this name, UpdateConfigurationTemplate returns an InvalidParameterValue error.
            
    :type TemplateName: string
    :param Description: A new description for the configuration.
    :type Description: string
    :param OptionSettings: A list of configuration option settings to update with the new specified option value.
            (dict) --A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to Option Values in the AWS Elastic Beanstalk Developer Guide .
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            Value (string) --The current value for the configuration option.
            
            
    :type OptionSettings: list
    :param OptionsToRemove: A list of configuration options to remove from the configuration set.
            Constraint: You can remove only UserDefined configuration options.
            (dict) --A specification identifying an individual configuration option.
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            
            
    :type OptionsToRemove: list
    """
    pass


def update_environment(ApplicationName=None, EnvironmentId=None, EnvironmentName=None, GroupName=None, Description=None,
                       Tier=None, VersionLabel=None, TemplateName=None, SolutionStackName=None, OptionSettings=None,
                       OptionsToRemove=None):
    """
    :param ApplicationName: The name of the application with which the environment is associated.
    :type ApplicationName: string
    :param EnvironmentId: The ID of the environment to update.
            If no environment with this ID exists, AWS Elastic Beanstalk returns an InvalidParameterValue error.
            Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentId: string
    :param EnvironmentName: The name of the environment to update. If no environment with this name exists, AWS Elastic Beanstalk returns an InvalidParameterValue error.
            Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns MissingRequiredParameter error.
            
    :type EnvironmentName: string
    :param GroupName: The name of the group to which the target environment belongs. Specify a group name only if the environment's name is specified in an environment manifest and not with the environment name or environment ID parameters. See Environment Manifest (env.yaml) for details.
    :type GroupName: string
    :param Description: If this parameter is specified, AWS Elastic Beanstalk updates the description of this environment.
    :type Description: string
    :param Tier: This specifies the tier to use to update the environment.
            Condition: At this time, if you change the tier version, name, or type, AWS Elastic Beanstalk returns InvalidParameterValue error.
            Name (string) --The name of this environment tier.
            Type (string) --The type of this environment tier.
            Version (string) --The version of this environment tier.
            
    :type Tier: dict
    :param VersionLabel: If this parameter is specified, AWS Elastic Beanstalk deploys the named application version to the environment. If no such application version is found, returns an InvalidParameterValue error.
    :type VersionLabel: string
    :param TemplateName: If this parameter is specified, AWS Elastic Beanstalk deploys this configuration template to the environment. If no such configuration template is found, AWS Elastic Beanstalk returns an InvalidParameterValue error.
    :type TemplateName: string
    :param SolutionStackName: This specifies the platform version that the environment will run after the environment is updated.
    :type SolutionStackName: string
    :param OptionSettings: If specified, AWS Elastic Beanstalk updates the configuration set associated with the running environment and sets the specified configuration options to the requested value.
            (dict) --A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to Option Values in the AWS Elastic Beanstalk Developer Guide .
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            Value (string) --The current value for the configuration option.
            
            
    :type OptionSettings: list
    :param OptionsToRemove: A list of custom user-defined configuration options to remove from the configuration set for this environment.
            (dict) --A specification identifying an individual configuration option.
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            
            
    :type OptionsToRemove: list
    """
    pass


def validate_configuration_settings(ApplicationName=None, TemplateName=None, EnvironmentName=None, OptionSettings=None):
    """
    :param ApplicationName: [REQUIRED]
            The name of the application that the configuration template or environment belongs to.
            
    :type ApplicationName: string
    :param TemplateName: The name of the configuration template to validate the settings against.
            Condition: You cannot specify both this and an environment name.
            
    :type TemplateName: string
    :param EnvironmentName: The name of the environment to validate the settings against.
            Condition: You cannot specify both this and a configuration template name.
            
    :type EnvironmentName: string
    :param OptionSettings: [REQUIRED]
            A list of the options and desired values to evaluate.
            (dict) --A specification identifying an individual configuration option along with its current value. For a list of possible option values, go to Option Values in the AWS Elastic Beanstalk Developer Guide .
            ResourceName (string) --A unique resource name for a time-based scaling configuration option.
            Namespace (string) --A unique namespace identifying the option's associated AWS resource.
            OptionName (string) --The name of the configuration option.
            Value (string) --The current value for the configuration option.
            
            
    :type OptionSettings: list
    """
    pass
