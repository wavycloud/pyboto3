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

def create_application(Name=None, Description=None, Tags=None):
    """
    An application in AppConfig is a logical unit of code that provides capabilities for your customers. For example, an application can be a microservice that runs on Amazon EC2 instances, a mobile application installed by your users, a serverless application using Amazon API Gateway and AWS Lambda, or any system you run on behalf of others.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_application(
        Name='string',
        Description='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA name for the application.\n

    :type Description: string
    :param Description: A description of the application.

    :type Tags: dict
    :param Tags: Metadata to assign to the application. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Id': 'string',
    'Name': 'string',
    'Description': 'string'
}


Response Structure

(dict) --

Id (string) --
The application ID.

Name (string) --
The application name.

Description (string) --
The description of the application.







Exceptions

AppConfig.Client.exceptions.BadRequestException
AppConfig.Client.exceptions.InternalServerException


    :return: {
        'Id': 'string',
        'Name': 'string',
        'Description': 'string'
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.BadRequestException
    AppConfig.Client.exceptions.InternalServerException
    
    """
    pass

def create_configuration_profile(ApplicationId=None, Name=None, Description=None, LocationUri=None, RetrievalRoleArn=None, Validators=None, Tags=None):
    """
    Information that enables AppConfig to access the configuration source. Valid configuration sources include Systems Manager (SSM) documents, SSM Parameter Store parameters, and Amazon S3 objects. A configuration profile includes the following information.
    For more information, see Create a Configuration and a Configuration Profile in the AWS AppConfig User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_configuration_profile(
        ApplicationId='string',
        Name='string',
        Description='string',
        LocationUri='string',
        RetrievalRoleArn='string',
        Validators=[
            {
                'Type': 'JSON_SCHEMA'|'LAMBDA',
                'Content': 'string'
            },
        ],
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe application ID.\n

    :type Name: string
    :param Name: [REQUIRED]\nA name for the configuration profile.\n

    :type Description: string
    :param Description: A description of the configuration profile.

    :type LocationUri: string
    :param LocationUri: [REQUIRED]\nA URI to locate the configuration. You can specify a Systems Manager (SSM) document, an SSM Parameter Store parameter, or an Amazon S3 object. For an SSM document, specify either the document name in the format ssm-document://<Document_name> or the Amazon Resource Name (ARN). For a parameter, specify either the parameter name in the format ssm-parameter://<Parameter_name> or the ARN. For an Amazon S3 object, specify the URI in the following format: s3://<bucket>/<objectKey> . Here is an example: s3://my-bucket/my-app/us-east-1/my-config.json\n

    :type RetrievalRoleArn: string
    :param RetrievalRoleArn: [REQUIRED]\nThe ARN of an IAM role with permission to access the configuration at the specified LocationUri.\n

    :type Validators: list
    :param Validators: A list of methods for validating the configuration.\n\n(dict) --A validator provides a syntactic or semantic check to ensure the configuration you want to deploy functions as intended. To validate your application configuration data, you provide a schema or a Lambda function that runs against the configuration. The configuration deployment or update can only proceed when the configuration data is valid.\n\nType (string) -- [REQUIRED]AppConfig supports validators of type JSON_SCHEMA and LAMBDA\n\nContent (string) -- [REQUIRED]Either the JSON Schema content or the Amazon Resource Name (ARN) of an AWS Lambda function.\n\n\n\n\n

    :type Tags: dict
    :param Tags: Metadata to assign to the configuration profile. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'Id': 'string',
    'Name': 'string',
    'Description': 'string',
    'LocationUri': 'string',
    'RetrievalRoleArn': 'string',
    'Validators': [
        {
            'Type': 'JSON_SCHEMA'|'LAMBDA',
            'Content': 'string'
        },
    ]
}


Response Structure

(dict) --

ApplicationId (string) --
The application ID.

Id (string) --
The configuration profile ID.

Name (string) --
The name of the configuration profile.

Description (string) --
The configuration profile description.

LocationUri (string) --
The URI location of the configuration.

RetrievalRoleArn (string) --
The ARN of an IAM role with permission to access the configuration at the specified LocationUri.

Validators (list) --
A list of methods for validating the configuration.

(dict) --
A validator provides a syntactic or semantic check to ensure the configuration you want to deploy functions as intended. To validate your application configuration data, you provide a schema or a Lambda function that runs against the configuration. The configuration deployment or update can only proceed when the configuration data is valid.

Type (string) --
AppConfig supports validators of type JSON_SCHEMA and LAMBDA

Content (string) --
Either the JSON Schema content or the Amazon Resource Name (ARN) of an AWS Lambda function.











Exceptions

AppConfig.Client.exceptions.BadRequestException
AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException


    :return: {
        'ApplicationId': 'string',
        'Id': 'string',
        'Name': 'string',
        'Description': 'string',
        'LocationUri': 'string',
        'RetrievalRoleArn': 'string',
        'Validators': [
            {
                'Type': 'JSON_SCHEMA'|'LAMBDA',
                'Content': 'string'
            },
        ]
    }
    
    
    :returns: 
    ApplicationId (string) -- [REQUIRED]
    The application ID.
    
    Name (string) -- [REQUIRED]
    A name for the configuration profile.
    
    Description (string) -- A description of the configuration profile.
    LocationUri (string) -- [REQUIRED]
    A URI to locate the configuration. You can specify a Systems Manager (SSM) document, an SSM Parameter Store parameter, or an Amazon S3 object. For an SSM document, specify either the document name in the format ssm-document://<Document_name> or the Amazon Resource Name (ARN). For a parameter, specify either the parameter name in the format ssm-parameter://<Parameter_name> or the ARN. For an Amazon S3 object, specify the URI in the following format: s3://<bucket>/<objectKey> . Here is an example: s3://my-bucket/my-app/us-east-1/my-config.json
    
    RetrievalRoleArn (string) -- [REQUIRED]
    The ARN of an IAM role with permission to access the configuration at the specified LocationUri.
    
    Validators (list) -- A list of methods for validating the configuration.
    
    (dict) --A validator provides a syntactic or semantic check to ensure the configuration you want to deploy functions as intended. To validate your application configuration data, you provide a schema or a Lambda function that runs against the configuration. The configuration deployment or update can only proceed when the configuration data is valid.
    
    Type (string) -- [REQUIRED]AppConfig supports validators of type JSON_SCHEMA and LAMBDA
    
    Content (string) -- [REQUIRED]Either the JSON Schema content or the Amazon Resource Name (ARN) of an AWS Lambda function.
    
    
    
    
    
    Tags (dict) -- Metadata to assign to the configuration profile. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
    
    (string) --
    (string) --
    
    
    
    
    
    """
    pass

def create_deployment_strategy(Name=None, Description=None, DeploymentDurationInMinutes=None, FinalBakeTimeInMinutes=None, GrowthFactor=None, GrowthType=None, ReplicateTo=None, Tags=None):
    """
    A deployment strategy defines important criteria for rolling out your configuration to the designated targets. A deployment strategy includes: the overall duration required, a percentage of targets to receive the deployment during each interval, an algorithm that defines how percentage grows, and bake time.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_deployment_strategy(
        Name='string',
        Description='string',
        DeploymentDurationInMinutes=123,
        FinalBakeTimeInMinutes=123,
        GrowthFactor=...,
        GrowthType='LINEAR'|'EXPONENTIAL',
        ReplicateTo='NONE'|'SSM_DOCUMENT',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA name for the deployment strategy.\n

    :type Description: string
    :param Description: A description of the deployment strategy.

    :type DeploymentDurationInMinutes: integer
    :param DeploymentDurationInMinutes: [REQUIRED]\nTotal amount of time for a deployment to last.\n

    :type FinalBakeTimeInMinutes: integer
    :param FinalBakeTimeInMinutes: The amount of time AppConfig monitors for alarms before considering the deployment to be complete and no longer eligible for automatic roll back.

    :type GrowthFactor: float
    :param GrowthFactor: [REQUIRED]\nThe percentage of targets to receive a deployed configuration during each interval.\n

    :type GrowthType: string
    :param GrowthType: The algorithm used to define how percentage grows over time. AWS AppConfig supports the following growth types:\n\nLinear : For this type, AppConfig processes the deployment by dividing the total number of targets by the value specified for Step percentage . For example, a linear deployment that uses a Step percentage of 10 deploys the configuration to 10 percent of the hosts. After those deployments are complete, the system deploys the configuration to the next 10 percent. This continues until 100% of the targets have successfully received the configuration.Exponential : For this type, AppConfig processes the deployment exponentially using the following formula: G*(2^N) . In this formula, G is the growth factor specified by the user and N is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows:\n2*(2^0)\n2*(2^1)\n2*(2^2)\n\nExpressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.\n

    :type ReplicateTo: string
    :param ReplicateTo: [REQUIRED]\nSave the deployment strategy to a Systems Manager (SSM) document.\n

    :type Tags: dict
    :param Tags: Metadata to assign to the deployment strategy. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Id': 'string',
    'Name': 'string',
    'Description': 'string',
    'DeploymentDurationInMinutes': 123,
    'GrowthType': 'LINEAR'|'EXPONENTIAL',
    'GrowthFactor': ...,
    'FinalBakeTimeInMinutes': 123,
    'ReplicateTo': 'NONE'|'SSM_DOCUMENT'
}


Response Structure

(dict) --

Id (string) --
The deployment strategy ID.

Name (string) --
The name of the deployment strategy.

Description (string) --
The description of the deployment strategy.

DeploymentDurationInMinutes (integer) --
Total amount of time the deployment lasted.

GrowthType (string) --
The algorithm used to define how percentage grew over time.

GrowthFactor (float) --
The percentage of targets that received a deployed configuration during each interval.

FinalBakeTimeInMinutes (integer) --
The amount of time AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic roll back.

ReplicateTo (string) --
Save the deployment strategy to a Systems Manager (SSM) document.







Exceptions

AppConfig.Client.exceptions.InternalServerException
AppConfig.Client.exceptions.BadRequestException


    :return: {
        'Id': 'string',
        'Name': 'string',
        'Description': 'string',
        'DeploymentDurationInMinutes': 123,
        'GrowthType': 'LINEAR'|'EXPONENTIAL',
        'GrowthFactor': ...,
        'FinalBakeTimeInMinutes': 123,
        'ReplicateTo': 'NONE'|'SSM_DOCUMENT'
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.InternalServerException
    AppConfig.Client.exceptions.BadRequestException
    
    """
    pass

def create_environment(ApplicationId=None, Name=None, Description=None, Monitors=None, Tags=None):
    """
    For each application, you define one or more environments. An environment is a logical deployment group of AppConfig targets, such as applications in a Beta or Production environment. You can also define environments for application subcomponents such as the Web , Mobile and Back-end components for your application. You can configure Amazon CloudWatch alarms for each environment. The system monitors alarms during a configuration deployment. If an alarm is triggered, the system rolls back the configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_environment(
        ApplicationId='string',
        Name='string',
        Description='string',
        Monitors=[
            {
                'AlarmArn': 'string',
                'AlarmRoleArn': 'string'
            },
        ],
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe application ID.\n

    :type Name: string
    :param Name: [REQUIRED]\nA name for the environment.\n

    :type Description: string
    :param Description: A description of the environment.

    :type Monitors: list
    :param Monitors: Amazon CloudWatch alarms to monitor during the deployment process.\n\n(dict) --Amazon CloudWatch alarms to monitor during the deployment process.\n\nAlarmArn (string) --ARN of the Amazon CloudWatch alarm.\n\nAlarmRoleArn (string) --ARN of an IAM role for AppConfig to monitor AlarmArn .\n\n\n\n\n

    :type Tags: dict
    :param Tags: Metadata to assign to the environment. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'Id': 'string',
    'Name': 'string',
    'Description': 'string',
    'State': 'READY_FOR_DEPLOYMENT'|'DEPLOYING'|'ROLLING_BACK'|'ROLLED_BACK',
    'Monitors': [
        {
            'AlarmArn': 'string',
            'AlarmRoleArn': 'string'
        },
    ]
}


Response Structure

(dict) --

ApplicationId (string) --
The application ID.

Id (string) --
The environment ID.

Name (string) --
The name of the environment.

Description (string) --
The description of the environment.

State (string) --
The state of the environment. An environment can be in one of the following states: READY_FOR_DEPLOYMENT , DEPLOYING , ROLLING_BACK , or ROLLED_BACK

Monitors (list) --
Amazon CloudWatch alarms monitored during the deployment.

(dict) --
Amazon CloudWatch alarms to monitor during the deployment process.

AlarmArn (string) --
ARN of the Amazon CloudWatch alarm.

AlarmRoleArn (string) --
ARN of an IAM role for AppConfig to monitor AlarmArn .











Exceptions

AppConfig.Client.exceptions.InternalServerException
AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.BadRequestException


    :return: {
        'ApplicationId': 'string',
        'Id': 'string',
        'Name': 'string',
        'Description': 'string',
        'State': 'READY_FOR_DEPLOYMENT'|'DEPLOYING'|'ROLLING_BACK'|'ROLLED_BACK',
        'Monitors': [
            {
                'AlarmArn': 'string',
                'AlarmRoleArn': 'string'
            },
        ]
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.InternalServerException
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.BadRequestException
    
    """
    pass

def delete_application(ApplicationId=None):
    """
    Delete an application. Deleting an application does not delete a configuration from a host.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe ID of the application to delete.\n

    """
    pass

def delete_configuration_profile(ApplicationId=None, ConfigurationProfileId=None):
    """
    Delete a configuration profile. Deleting a configuration profile does not delete a configuration from a host.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_configuration_profile(
        ApplicationId='string',
        ConfigurationProfileId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe application ID that includes the configuration profile you want to delete.\n

    :type ConfigurationProfileId: string
    :param ConfigurationProfileId: [REQUIRED]\nThe ID of the configuration profile you want to delete.\n

    :returns: 
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.ConflictException
    AppConfig.Client.exceptions.InternalServerException
    AppConfig.Client.exceptions.BadRequestException
    
    """
    pass

def delete_deployment_strategy(DeploymentStrategyId=None):
    """
    Delete a deployment strategy. Deleting a deployment strategy does not delete a configuration from a host.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_deployment_strategy(
        DeploymentStrategyId='string'
    )
    
    
    :type DeploymentStrategyId: string
    :param DeploymentStrategyId: [REQUIRED]\nThe ID of the deployment strategy you want to delete.\n

    """
    pass

def delete_environment(ApplicationId=None, EnvironmentId=None):
    """
    Delete an environment. Deleting an environment does not delete a configuration from a host.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_environment(
        ApplicationId='string',
        EnvironmentId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe application ID that includes the environment you want to delete.\n

    :type EnvironmentId: string
    :param EnvironmentId: [REQUIRED]\nThe ID of the environment you want to delete.\n

    :returns: 
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.ConflictException
    AppConfig.Client.exceptions.InternalServerException
    AppConfig.Client.exceptions.BadRequestException
    
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

def get_application(ApplicationId=None):
    """
    Retrieve information about an application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_application(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe ID of the application you want to get.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Id': 'string',
    'Name': 'string',
    'Description': 'string'
}


Response Structure

(dict) --
Id (string) --The application ID.

Name (string) --The application name.

Description (string) --The description of the application.






Exceptions

AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException
AppConfig.Client.exceptions.BadRequestException


    :return: {
        'Id': 'string',
        'Name': 'string',
        'Description': 'string'
    }
    
    
    """
    pass

def get_configuration(Application=None, Environment=None, Configuration=None, ClientId=None, ClientConfigurationVersion=None):
    """
    Receive information about a configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_configuration(
        Application='string',
        Environment='string',
        Configuration='string',
        ClientId='string',
        ClientConfigurationVersion='string'
    )
    
    
    :type Application: string
    :param Application: [REQUIRED]\nThe application to get. Specify either the application name or the application ID.\n

    :type Environment: string
    :param Environment: [REQUIRED]\nThe environment to get. Specify either the environment name or the environment ID.\n

    :type Configuration: string
    :param Configuration: [REQUIRED]\nThe configuration to get. Specify either the configuration name or the configuration ID.\n

    :type ClientId: string
    :param ClientId: [REQUIRED]\nA unique ID to identify the client for the configuration. This ID enables AppConfig to deploy the configuration in intervals, as defined in the deployment strategy.\n

    :type ClientConfigurationVersion: string
    :param ClientConfigurationVersion: The configuration version returned in the most recent GetConfiguration response.\n\nWarning\nAWS AppConfig uses the value of the ClientConfigurationVersion parameter to identify the configuration version on your clients. If you don\xe2\x80\x99t send ClientConfigurationVersion with each call to GetConfiguration , your clients receive the current configuration. You are charged each time your clients receive a configuration.\nTo avoid excess charges, we recommend that you include the ClientConfigurationVersion value with every call to GetConfiguration . This value must be saved on your client. Subsequent calls to GetConfiguration must pass this value by using the ClientConfigurationVersion parameter.\n\nFor more information about working with configurations, see Retrieving the Configuration in the AWS AppConfig User Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Content': StreamingBody(),
    'ConfigurationVersion': 'string',
    'ContentType': 'string'
}


Response Structure

(dict) --

Content (StreamingBody) --
The content of the configuration or the configuration data.

ConfigurationVersion (string) --
The configuration version.

ContentType (string) --
A standard MIME type describing the format of the configuration content. For more information, see Content-Type .







Exceptions

AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException
AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.BadRequestException


    :return: {
        'Content': StreamingBody(),
        'ConfigurationVersion': 'string',
        'ContentType': 'string'
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.InternalServerException
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.BadRequestException
    
    """
    pass

def get_configuration_profile(ApplicationId=None, ConfigurationProfileId=None):
    """
    Retrieve information about a configuration profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_configuration_profile(
        ApplicationId='string',
        ConfigurationProfileId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe ID of the application that includes the configuration profile you want to get.\n

    :type ConfigurationProfileId: string
    :param ConfigurationProfileId: [REQUIRED]\nThe ID of the configuration profile you want to get.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'Id': 'string',
    'Name': 'string',
    'Description': 'string',
    'LocationUri': 'string',
    'RetrievalRoleArn': 'string',
    'Validators': [
        {
            'Type': 'JSON_SCHEMA'|'LAMBDA',
            'Content': 'string'
        },
    ]
}


Response Structure

(dict) --

ApplicationId (string) --
The application ID.

Id (string) --
The configuration profile ID.

Name (string) --
The name of the configuration profile.

Description (string) --
The configuration profile description.

LocationUri (string) --
The URI location of the configuration.

RetrievalRoleArn (string) --
The ARN of an IAM role with permission to access the configuration at the specified LocationUri.

Validators (list) --
A list of methods for validating the configuration.

(dict) --
A validator provides a syntactic or semantic check to ensure the configuration you want to deploy functions as intended. To validate your application configuration data, you provide a schema or a Lambda function that runs against the configuration. The configuration deployment or update can only proceed when the configuration data is valid.

Type (string) --
AppConfig supports validators of type JSON_SCHEMA and LAMBDA

Content (string) --
Either the JSON Schema content or the Amazon Resource Name (ARN) of an AWS Lambda function.











Exceptions

AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException
AppConfig.Client.exceptions.BadRequestException


    :return: {
        'ApplicationId': 'string',
        'Id': 'string',
        'Name': 'string',
        'Description': 'string',
        'LocationUri': 'string',
        'RetrievalRoleArn': 'string',
        'Validators': [
            {
                'Type': 'JSON_SCHEMA'|'LAMBDA',
                'Content': 'string'
            },
        ]
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.InternalServerException
    AppConfig.Client.exceptions.BadRequestException
    
    """
    pass

def get_deployment(ApplicationId=None, EnvironmentId=None, DeploymentNumber=None):
    """
    Retrieve information about a configuration deployment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_deployment(
        ApplicationId='string',
        EnvironmentId='string',
        DeploymentNumber=123
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe ID of the application that includes the deployment you want to get.\n

    :type EnvironmentId: string
    :param EnvironmentId: [REQUIRED]\nThe ID of the environment that includes the deployment you want to get.\n

    :type DeploymentNumber: integer
    :param DeploymentNumber: [REQUIRED]\nThe sequence number of the deployment.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'EnvironmentId': 'string',
    'DeploymentStrategyId': 'string',
    'ConfigurationProfileId': 'string',
    'DeploymentNumber': 123,
    'ConfigurationName': 'string',
    'ConfigurationLocationUri': 'string',
    'ConfigurationVersion': 'string',
    'Description': 'string',
    'DeploymentDurationInMinutes': 123,
    'GrowthType': 'LINEAR'|'EXPONENTIAL',
    'GrowthFactor': ...,
    'FinalBakeTimeInMinutes': 123,
    'State': 'BAKING'|'VALIDATING'|'DEPLOYING'|'COMPLETE'|'ROLLING_BACK'|'ROLLED_BACK',
    'EventLog': [
        {
            'EventType': 'PERCENTAGE_UPDATED'|'ROLLBACK_STARTED'|'ROLLBACK_COMPLETED'|'BAKE_TIME_STARTED'|'DEPLOYMENT_STARTED'|'DEPLOYMENT_COMPLETED',
            'TriggeredBy': 'USER'|'APPCONFIG'|'CLOUDWATCH_ALARM'|'INTERNAL_ERROR',
            'Description': 'string',
            'OccurredAt': datetime(2015, 1, 1)
        },
    ],
    'PercentageComplete': ...,
    'StartedAt': datetime(2015, 1, 1),
    'CompletedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --

ApplicationId (string) --
The ID of the application that was deployed.

EnvironmentId (string) --
The ID of the environment that was deployed.

DeploymentStrategyId (string) --
The ID of the deployment strategy that was deployed.

ConfigurationProfileId (string) --
The ID of the configuration profile that was deployed.

DeploymentNumber (integer) --
The sequence number of the deployment.

ConfigurationName (string) --
The name of the configuration.

ConfigurationLocationUri (string) --
Information about the source location of the configuration.

ConfigurationVersion (string) --
The configuration version that was deployed.

Description (string) --
The description of the deployment.

DeploymentDurationInMinutes (integer) --
Total amount of time the deployment lasted.

GrowthType (string) --
The algorithm used to define how percentage grew over time.

GrowthFactor (float) --
The percentage of targets to receive a deployed configuration during each interval.

FinalBakeTimeInMinutes (integer) --
The amount of time AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic roll back.

State (string) --
The state of the deployment.

EventLog (list) --
A list containing all events related to a deployment. The most recent events are displayed first.

(dict) --
An object that describes a deployment event.

EventType (string) --
The type of deployment event. Deployment event types include the start, stop, or completion of a deployment; a percentage update; the start or stop of a bake period; the start or completion of a rollback.

TriggeredBy (string) --
The entity that triggered the deployment event. Events can be triggered by a user, AWS AppConfig, an Amazon CloudWatch alarm, or an internal error.

Description (string) --
A description of the deployment event. Descriptions include, but are not limited to, the user account or the CloudWatch alarm ARN that initiated a rollback, the percentage of hosts that received the deployment, or in the case of an internal error, a recommendation to attempt a new deployment.

OccurredAt (datetime) --
The date and time the event occurred.





PercentageComplete (float) --
The percentage of targets for which the deployment is available.

StartedAt (datetime) --
The time the deployment started.

CompletedAt (datetime) --
The time the deployment completed.







Exceptions

AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException
AppConfig.Client.exceptions.BadRequestException


    :return: {
        'ApplicationId': 'string',
        'EnvironmentId': 'string',
        'DeploymentStrategyId': 'string',
        'ConfigurationProfileId': 'string',
        'DeploymentNumber': 123,
        'ConfigurationName': 'string',
        'ConfigurationLocationUri': 'string',
        'ConfigurationVersion': 'string',
        'Description': 'string',
        'DeploymentDurationInMinutes': 123,
        'GrowthType': 'LINEAR'|'EXPONENTIAL',
        'GrowthFactor': ...,
        'FinalBakeTimeInMinutes': 123,
        'State': 'BAKING'|'VALIDATING'|'DEPLOYING'|'COMPLETE'|'ROLLING_BACK'|'ROLLED_BACK',
        'EventLog': [
            {
                'EventType': 'PERCENTAGE_UPDATED'|'ROLLBACK_STARTED'|'ROLLBACK_COMPLETED'|'BAKE_TIME_STARTED'|'DEPLOYMENT_STARTED'|'DEPLOYMENT_COMPLETED',
                'TriggeredBy': 'USER'|'APPCONFIG'|'CLOUDWATCH_ALARM'|'INTERNAL_ERROR',
                'Description': 'string',
                'OccurredAt': datetime(2015, 1, 1)
            },
        ],
        'PercentageComplete': ...,
        'StartedAt': datetime(2015, 1, 1),
        'CompletedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.InternalServerException
    AppConfig.Client.exceptions.BadRequestException
    
    """
    pass

def get_deployment_strategy(DeploymentStrategyId=None):
    """
    Retrieve information about a deployment strategy. A deployment strategy defines important criteria for rolling out your configuration to the designated targets. A deployment strategy includes: the overall duration required, a percentage of targets to receive the deployment during each interval, an algorithm that defines how percentage grows, and bake time.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_deployment_strategy(
        DeploymentStrategyId='string'
    )
    
    
    :type DeploymentStrategyId: string
    :param DeploymentStrategyId: [REQUIRED]\nThe ID of the deployment strategy to get.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Id': 'string',
    'Name': 'string',
    'Description': 'string',
    'DeploymentDurationInMinutes': 123,
    'GrowthType': 'LINEAR'|'EXPONENTIAL',
    'GrowthFactor': ...,
    'FinalBakeTimeInMinutes': 123,
    'ReplicateTo': 'NONE'|'SSM_DOCUMENT'
}


Response Structure

(dict) --
Id (string) --The deployment strategy ID.

Name (string) --The name of the deployment strategy.

Description (string) --The description of the deployment strategy.

DeploymentDurationInMinutes (integer) --Total amount of time the deployment lasted.

GrowthType (string) --The algorithm used to define how percentage grew over time.

GrowthFactor (float) --The percentage of targets that received a deployed configuration during each interval.

FinalBakeTimeInMinutes (integer) --The amount of time AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic roll back.

ReplicateTo (string) --Save the deployment strategy to a Systems Manager (SSM) document.






Exceptions

AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException
AppConfig.Client.exceptions.BadRequestException


    :return: {
        'Id': 'string',
        'Name': 'string',
        'Description': 'string',
        'DeploymentDurationInMinutes': 123,
        'GrowthType': 'LINEAR'|'EXPONENTIAL',
        'GrowthFactor': ...,
        'FinalBakeTimeInMinutes': 123,
        'ReplicateTo': 'NONE'|'SSM_DOCUMENT'
    }
    
    
    """
    pass

def get_environment(ApplicationId=None, EnvironmentId=None):
    """
    Retrieve information about an environment. An environment is a logical deployment group of AppConfig applications, such as applications in a Production environment or in an EU_Region environment. Each configuration deployment targets an environment. You can enable one or more Amazon CloudWatch alarms for an environment. If an alarm is triggered during a deployment, AppConfig roles back the configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_environment(
        ApplicationId='string',
        EnvironmentId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe ID of the application that includes the environment you want to get.\n

    :type EnvironmentId: string
    :param EnvironmentId: [REQUIRED]\nThe ID of the environment you wnat to get.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'Id': 'string',
    'Name': 'string',
    'Description': 'string',
    'State': 'READY_FOR_DEPLOYMENT'|'DEPLOYING'|'ROLLING_BACK'|'ROLLED_BACK',
    'Monitors': [
        {
            'AlarmArn': 'string',
            'AlarmRoleArn': 'string'
        },
    ]
}


Response Structure

(dict) --

ApplicationId (string) --
The application ID.

Id (string) --
The environment ID.

Name (string) --
The name of the environment.

Description (string) --
The description of the environment.

State (string) --
The state of the environment. An environment can be in one of the following states: READY_FOR_DEPLOYMENT , DEPLOYING , ROLLING_BACK , or ROLLED_BACK

Monitors (list) --
Amazon CloudWatch alarms monitored during the deployment.

(dict) --
Amazon CloudWatch alarms to monitor during the deployment process.

AlarmArn (string) --
ARN of the Amazon CloudWatch alarm.

AlarmRoleArn (string) --
ARN of an IAM role for AppConfig to monitor AlarmArn .











Exceptions

AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException
AppConfig.Client.exceptions.BadRequestException


    :return: {
        'ApplicationId': 'string',
        'Id': 'string',
        'Name': 'string',
        'Description': 'string',
        'State': 'READY_FOR_DEPLOYMENT'|'DEPLOYING'|'ROLLING_BACK'|'ROLLED_BACK',
        'Monitors': [
            {
                'AlarmArn': 'string',
                'AlarmRoleArn': 'string'
            },
        ]
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.InternalServerException
    AppConfig.Client.exceptions.BadRequestException
    
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

def list_applications(MaxResults=None, NextToken=None):
    """
    List all applications in your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_applications(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Items (list) --
The elements from this collection.

(dict) --

Id (string) --
The application ID.

Name (string) --
The application name.

Description (string) --
The description of the application.





NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

AppConfig.Client.exceptions.InternalServerException
AppConfig.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.InternalServerException
    AppConfig.Client.exceptions.BadRequestException
    
    """
    pass

def list_configuration_profiles(ApplicationId=None, MaxResults=None, NextToken=None):
    """
    Lists the configuration profiles for an application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_configuration_profiles(
        ApplicationId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe application ID.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'ApplicationId': 'string',
            'Id': 'string',
            'Name': 'string',
            'LocationUri': 'string',
            'ValidatorTypes': [
                'JSON_SCHEMA'|'LAMBDA',
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Items (list) --
The elements from this collection.

(dict) --
A summary of a configuration profile.

ApplicationId (string) --
The application ID.

Id (string) --
The ID of the configuration profile.

Name (string) --
The name of the configuration profile.

LocationUri (string) --
The URI location of the configuration.

ValidatorTypes (list) --
The types of validators in the configuration profile.

(string) --






NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException
AppConfig.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'ApplicationId': 'string',
                'Id': 'string',
                'Name': 'string',
                'LocationUri': 'string',
                'ValidatorTypes': [
                    'JSON_SCHEMA'|'LAMBDA',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_deployment_strategies(MaxResults=None, NextToken=None):
    """
    List deployment strategies.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_deployment_strategies(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'DeploymentDurationInMinutes': 123,
            'GrowthType': 'LINEAR'|'EXPONENTIAL',
            'GrowthFactor': ...,
            'FinalBakeTimeInMinutes': 123,
            'ReplicateTo': 'NONE'|'SSM_DOCUMENT'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Items (list) --
The elements from this collection.

(dict) --

Id (string) --
The deployment strategy ID.

Name (string) --
The name of the deployment strategy.

Description (string) --
The description of the deployment strategy.

DeploymentDurationInMinutes (integer) --
Total amount of time the deployment lasted.

GrowthType (string) --
The algorithm used to define how percentage grew over time.

GrowthFactor (float) --
The percentage of targets that received a deployed configuration during each interval.

FinalBakeTimeInMinutes (integer) --
The amount of time AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic roll back.

ReplicateTo (string) --
Save the deployment strategy to a Systems Manager (SSM) document.





NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

AppConfig.Client.exceptions.InternalServerException
AppConfig.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'DeploymentDurationInMinutes': 123,
                'GrowthType': 'LINEAR'|'EXPONENTIAL',
                'GrowthFactor': ...,
                'FinalBakeTimeInMinutes': 123,
                'ReplicateTo': 'NONE'|'SSM_DOCUMENT'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.InternalServerException
    AppConfig.Client.exceptions.BadRequestException
    
    """
    pass

def list_deployments(ApplicationId=None, EnvironmentId=None, MaxResults=None, NextToken=None):
    """
    Lists the deployments for an environment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_deployments(
        ApplicationId='string',
        EnvironmentId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe application ID.\n

    :type EnvironmentId: string
    :param EnvironmentId: [REQUIRED]\nThe environment ID.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'DeploymentNumber': 123,
            'ConfigurationName': 'string',
            'ConfigurationVersion': 'string',
            'DeploymentDurationInMinutes': 123,
            'GrowthType': 'LINEAR'|'EXPONENTIAL',
            'GrowthFactor': ...,
            'FinalBakeTimeInMinutes': 123,
            'State': 'BAKING'|'VALIDATING'|'DEPLOYING'|'COMPLETE'|'ROLLING_BACK'|'ROLLED_BACK',
            'PercentageComplete': ...,
            'StartedAt': datetime(2015, 1, 1),
            'CompletedAt': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Items (list) --
The elements from this collection.

(dict) --
Information about the deployment.

DeploymentNumber (integer) --
The sequence number of the deployment.

ConfigurationName (string) --
The name of the configuration.

ConfigurationVersion (string) --
The version of the configuration.

DeploymentDurationInMinutes (integer) --
Total amount of time the deployment lasted.

GrowthType (string) --
The algorithm used to define how percentage grows over time.

GrowthFactor (float) --
The percentage of targets to receive a deployed configuration during each interval.

FinalBakeTimeInMinutes (integer) --
The amount of time AppConfig monitors for alarms before considering the deployment to be complete and no longer eligible for automatic roll back.

State (string) --
The state of the deployment.

PercentageComplete (float) --
The percentage of targets for which the deployment is available.

StartedAt (datetime) --
Time the deployment started.

CompletedAt (datetime) --
Time the deployment completed.





NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException
AppConfig.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'DeploymentNumber': 123,
                'ConfigurationName': 'string',
                'ConfigurationVersion': 'string',
                'DeploymentDurationInMinutes': 123,
                'GrowthType': 'LINEAR'|'EXPONENTIAL',
                'GrowthFactor': ...,
                'FinalBakeTimeInMinutes': 123,
                'State': 'BAKING'|'VALIDATING'|'DEPLOYING'|'COMPLETE'|'ROLLING_BACK'|'ROLLED_BACK',
                'PercentageComplete': ...,
                'StartedAt': datetime(2015, 1, 1),
                'CompletedAt': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.InternalServerException
    AppConfig.Client.exceptions.BadRequestException
    
    """
    pass

def list_environments(ApplicationId=None, MaxResults=None, NextToken=None):
    """
    List the environments for an application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_environments(
        ApplicationId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe application ID.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'ApplicationId': 'string',
            'Id': 'string',
            'Name': 'string',
            'Description': 'string',
            'State': 'READY_FOR_DEPLOYMENT'|'DEPLOYING'|'ROLLING_BACK'|'ROLLED_BACK',
            'Monitors': [
                {
                    'AlarmArn': 'string',
                    'AlarmRoleArn': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Items (list) --
The elements from this collection.

(dict) --

ApplicationId (string) --
The application ID.

Id (string) --
The environment ID.

Name (string) --
The name of the environment.

Description (string) --
The description of the environment.

State (string) --
The state of the environment. An environment can be in one of the following states: READY_FOR_DEPLOYMENT , DEPLOYING , ROLLING_BACK , or ROLLED_BACK

Monitors (list) --
Amazon CloudWatch alarms monitored during the deployment.

(dict) --
Amazon CloudWatch alarms to monitor during the deployment process.

AlarmArn (string) --
ARN of the Amazon CloudWatch alarm.

AlarmRoleArn (string) --
ARN of an IAM role for AppConfig to monitor AlarmArn .









NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException
AppConfig.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'ApplicationId': 'string',
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'State': 'READY_FOR_DEPLOYMENT'|'DEPLOYING'|'ROLLING_BACK'|'ROLLED_BACK',
                'Monitors': [
                    {
                        'AlarmArn': 'string',
                        'AlarmRoleArn': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.InternalServerException
    AppConfig.Client.exceptions.BadRequestException
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Retrieves the list of key-value tags assigned to the resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe resource ARN.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Tags (dict) --Metadata to assign to AppConfig resources. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

(string) --
(string) --









Exceptions

AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.BadRequestException
AppConfig.Client.exceptions.InternalServerException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.BadRequestException
    AppConfig.Client.exceptions.InternalServerException
    
    """
    pass

def start_deployment(ApplicationId=None, EnvironmentId=None, DeploymentStrategyId=None, ConfigurationProfileId=None, ConfigurationVersion=None, Description=None, Tags=None):
    """
    Starts a deployment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_deployment(
        ApplicationId='string',
        EnvironmentId='string',
        DeploymentStrategyId='string',
        ConfigurationProfileId='string',
        ConfigurationVersion='string',
        Description='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe application ID.\n

    :type EnvironmentId: string
    :param EnvironmentId: [REQUIRED]\nThe environment ID.\n

    :type DeploymentStrategyId: string
    :param DeploymentStrategyId: [REQUIRED]\nThe deployment strategy ID.\n

    :type ConfigurationProfileId: string
    :param ConfigurationProfileId: [REQUIRED]\nThe configuration profile ID.\n

    :type ConfigurationVersion: string
    :param ConfigurationVersion: [REQUIRED]\nThe configuration version to deploy.\n

    :type Description: string
    :param Description: A description of the deployment.

    :type Tags: dict
    :param Tags: Metadata to assign to the deployment. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'EnvironmentId': 'string',
    'DeploymentStrategyId': 'string',
    'ConfigurationProfileId': 'string',
    'DeploymentNumber': 123,
    'ConfigurationName': 'string',
    'ConfigurationLocationUri': 'string',
    'ConfigurationVersion': 'string',
    'Description': 'string',
    'DeploymentDurationInMinutes': 123,
    'GrowthType': 'LINEAR'|'EXPONENTIAL',
    'GrowthFactor': ...,
    'FinalBakeTimeInMinutes': 123,
    'State': 'BAKING'|'VALIDATING'|'DEPLOYING'|'COMPLETE'|'ROLLING_BACK'|'ROLLED_BACK',
    'EventLog': [
        {
            'EventType': 'PERCENTAGE_UPDATED'|'ROLLBACK_STARTED'|'ROLLBACK_COMPLETED'|'BAKE_TIME_STARTED'|'DEPLOYMENT_STARTED'|'DEPLOYMENT_COMPLETED',
            'TriggeredBy': 'USER'|'APPCONFIG'|'CLOUDWATCH_ALARM'|'INTERNAL_ERROR',
            'Description': 'string',
            'OccurredAt': datetime(2015, 1, 1)
        },
    ],
    'PercentageComplete': ...,
    'StartedAt': datetime(2015, 1, 1),
    'CompletedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --

ApplicationId (string) --
The ID of the application that was deployed.

EnvironmentId (string) --
The ID of the environment that was deployed.

DeploymentStrategyId (string) --
The ID of the deployment strategy that was deployed.

ConfigurationProfileId (string) --
The ID of the configuration profile that was deployed.

DeploymentNumber (integer) --
The sequence number of the deployment.

ConfigurationName (string) --
The name of the configuration.

ConfigurationLocationUri (string) --
Information about the source location of the configuration.

ConfigurationVersion (string) --
The configuration version that was deployed.

Description (string) --
The description of the deployment.

DeploymentDurationInMinutes (integer) --
Total amount of time the deployment lasted.

GrowthType (string) --
The algorithm used to define how percentage grew over time.

GrowthFactor (float) --
The percentage of targets to receive a deployed configuration during each interval.

FinalBakeTimeInMinutes (integer) --
The amount of time AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic roll back.

State (string) --
The state of the deployment.

EventLog (list) --
A list containing all events related to a deployment. The most recent events are displayed first.

(dict) --
An object that describes a deployment event.

EventType (string) --
The type of deployment event. Deployment event types include the start, stop, or completion of a deployment; a percentage update; the start or stop of a bake period; the start or completion of a rollback.

TriggeredBy (string) --
The entity that triggered the deployment event. Events can be triggered by a user, AWS AppConfig, an Amazon CloudWatch alarm, or an internal error.

Description (string) --
A description of the deployment event. Descriptions include, but are not limited to, the user account or the CloudWatch alarm ARN that initiated a rollback, the percentage of hosts that received the deployment, or in the case of an internal error, a recommendation to attempt a new deployment.

OccurredAt (datetime) --
The date and time the event occurred.





PercentageComplete (float) --
The percentage of targets for which the deployment is available.

StartedAt (datetime) --
The time the deployment started.

CompletedAt (datetime) --
The time the deployment completed.







Exceptions

AppConfig.Client.exceptions.BadRequestException
AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.ConflictException
AppConfig.Client.exceptions.InternalServerException


    :return: {
        'ApplicationId': 'string',
        'EnvironmentId': 'string',
        'DeploymentStrategyId': 'string',
        'ConfigurationProfileId': 'string',
        'DeploymentNumber': 123,
        'ConfigurationName': 'string',
        'ConfigurationLocationUri': 'string',
        'ConfigurationVersion': 'string',
        'Description': 'string',
        'DeploymentDurationInMinutes': 123,
        'GrowthType': 'LINEAR'|'EXPONENTIAL',
        'GrowthFactor': ...,
        'FinalBakeTimeInMinutes': 123,
        'State': 'BAKING'|'VALIDATING'|'DEPLOYING'|'COMPLETE'|'ROLLING_BACK'|'ROLLED_BACK',
        'EventLog': [
            {
                'EventType': 'PERCENTAGE_UPDATED'|'ROLLBACK_STARTED'|'ROLLBACK_COMPLETED'|'BAKE_TIME_STARTED'|'DEPLOYMENT_STARTED'|'DEPLOYMENT_COMPLETED',
                'TriggeredBy': 'USER'|'APPCONFIG'|'CLOUDWATCH_ALARM'|'INTERNAL_ERROR',
                'Description': 'string',
                'OccurredAt': datetime(2015, 1, 1)
            },
        ],
        'PercentageComplete': ...,
        'StartedAt': datetime(2015, 1, 1),
        'CompletedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.BadRequestException
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.ConflictException
    AppConfig.Client.exceptions.InternalServerException
    
    """
    pass

def stop_deployment(ApplicationId=None, EnvironmentId=None, DeploymentNumber=None):
    """
    Stops a deployment. This API action works only on deployments that have a status of DEPLOYING . This action moves the deployment to a status of ROLLED_BACK .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_deployment(
        ApplicationId='string',
        EnvironmentId='string',
        DeploymentNumber=123
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe application ID.\n

    :type EnvironmentId: string
    :param EnvironmentId: [REQUIRED]\nThe environment ID.\n

    :type DeploymentNumber: integer
    :param DeploymentNumber: [REQUIRED]\nThe sequence number of the deployment.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'EnvironmentId': 'string',
    'DeploymentStrategyId': 'string',
    'ConfigurationProfileId': 'string',
    'DeploymentNumber': 123,
    'ConfigurationName': 'string',
    'ConfigurationLocationUri': 'string',
    'ConfigurationVersion': 'string',
    'Description': 'string',
    'DeploymentDurationInMinutes': 123,
    'GrowthType': 'LINEAR'|'EXPONENTIAL',
    'GrowthFactor': ...,
    'FinalBakeTimeInMinutes': 123,
    'State': 'BAKING'|'VALIDATING'|'DEPLOYING'|'COMPLETE'|'ROLLING_BACK'|'ROLLED_BACK',
    'EventLog': [
        {
            'EventType': 'PERCENTAGE_UPDATED'|'ROLLBACK_STARTED'|'ROLLBACK_COMPLETED'|'BAKE_TIME_STARTED'|'DEPLOYMENT_STARTED'|'DEPLOYMENT_COMPLETED',
            'TriggeredBy': 'USER'|'APPCONFIG'|'CLOUDWATCH_ALARM'|'INTERNAL_ERROR',
            'Description': 'string',
            'OccurredAt': datetime(2015, 1, 1)
        },
    ],
    'PercentageComplete': ...,
    'StartedAt': datetime(2015, 1, 1),
    'CompletedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --

ApplicationId (string) --
The ID of the application that was deployed.

EnvironmentId (string) --
The ID of the environment that was deployed.

DeploymentStrategyId (string) --
The ID of the deployment strategy that was deployed.

ConfigurationProfileId (string) --
The ID of the configuration profile that was deployed.

DeploymentNumber (integer) --
The sequence number of the deployment.

ConfigurationName (string) --
The name of the configuration.

ConfigurationLocationUri (string) --
Information about the source location of the configuration.

ConfigurationVersion (string) --
The configuration version that was deployed.

Description (string) --
The description of the deployment.

DeploymentDurationInMinutes (integer) --
Total amount of time the deployment lasted.

GrowthType (string) --
The algorithm used to define how percentage grew over time.

GrowthFactor (float) --
The percentage of targets to receive a deployed configuration during each interval.

FinalBakeTimeInMinutes (integer) --
The amount of time AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic roll back.

State (string) --
The state of the deployment.

EventLog (list) --
A list containing all events related to a deployment. The most recent events are displayed first.

(dict) --
An object that describes a deployment event.

EventType (string) --
The type of deployment event. Deployment event types include the start, stop, or completion of a deployment; a percentage update; the start or stop of a bake period; the start or completion of a rollback.

TriggeredBy (string) --
The entity that triggered the deployment event. Events can be triggered by a user, AWS AppConfig, an Amazon CloudWatch alarm, or an internal error.

Description (string) --
A description of the deployment event. Descriptions include, but are not limited to, the user account or the CloudWatch alarm ARN that initiated a rollback, the percentage of hosts that received the deployment, or in the case of an internal error, a recommendation to attempt a new deployment.

OccurredAt (datetime) --
The date and time the event occurred.





PercentageComplete (float) --
The percentage of targets for which the deployment is available.

StartedAt (datetime) --
The time the deployment started.

CompletedAt (datetime) --
The time the deployment completed.







Exceptions

AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException
AppConfig.Client.exceptions.BadRequestException


    :return: {
        'ApplicationId': 'string',
        'EnvironmentId': 'string',
        'DeploymentStrategyId': 'string',
        'ConfigurationProfileId': 'string',
        'DeploymentNumber': 123,
        'ConfigurationName': 'string',
        'ConfigurationLocationUri': 'string',
        'ConfigurationVersion': 'string',
        'Description': 'string',
        'DeploymentDurationInMinutes': 123,
        'GrowthType': 'LINEAR'|'EXPONENTIAL',
        'GrowthFactor': ...,
        'FinalBakeTimeInMinutes': 123,
        'State': 'BAKING'|'VALIDATING'|'DEPLOYING'|'COMPLETE'|'ROLLING_BACK'|'ROLLED_BACK',
        'EventLog': [
            {
                'EventType': 'PERCENTAGE_UPDATED'|'ROLLBACK_STARTED'|'ROLLBACK_COMPLETED'|'BAKE_TIME_STARTED'|'DEPLOYMENT_STARTED'|'DEPLOYMENT_COMPLETED',
                'TriggeredBy': 'USER'|'APPCONFIG'|'CLOUDWATCH_ALARM'|'INTERNAL_ERROR',
                'Description': 'string',
                'OccurredAt': datetime(2015, 1, 1)
            },
        ],
        'PercentageComplete': ...,
        'StartedAt': datetime(2015, 1, 1),
        'CompletedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.InternalServerException
    AppConfig.Client.exceptions.BadRequestException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Metadata to assign to an AppConfig resource. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define. You can specify a maximum of 50 tags for a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the resource for which to retrieve tags.\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nThe key-value string map. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with aws: . The tag value can be up to 256 characters.\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.BadRequestException
    AppConfig.Client.exceptions.InternalServerException
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Deletes a tag key and value from an AppConfig resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the resource for which to remove tags.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag keys to delete.\n\n(string) --\n\n

    :returns: 
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.BadRequestException
    AppConfig.Client.exceptions.InternalServerException
    
    """
    pass

def update_application(ApplicationId=None, Name=None, Description=None):
    """
    Updates an application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_application(
        ApplicationId='string',
        Name='string',
        Description='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe application ID.\n

    :type Name: string
    :param Name: The name of the application.

    :type Description: string
    :param Description: A description of the application.

    :rtype: dict

ReturnsResponse Syntax
{
    'Id': 'string',
    'Name': 'string',
    'Description': 'string'
}


Response Structure

(dict) --

Id (string) --
The application ID.

Name (string) --
The application name.

Description (string) --
The description of the application.







Exceptions

AppConfig.Client.exceptions.BadRequestException
AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException


    :return: {
        'Id': 'string',
        'Name': 'string',
        'Description': 'string'
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.BadRequestException
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.InternalServerException
    
    """
    pass

def update_configuration_profile(ApplicationId=None, ConfigurationProfileId=None, Name=None, Description=None, RetrievalRoleArn=None, Validators=None):
    """
    Updates a configuration profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_configuration_profile(
        ApplicationId='string',
        ConfigurationProfileId='string',
        Name='string',
        Description='string',
        RetrievalRoleArn='string',
        Validators=[
            {
                'Type': 'JSON_SCHEMA'|'LAMBDA',
                'Content': 'string'
            },
        ]
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe application ID.\n

    :type ConfigurationProfileId: string
    :param ConfigurationProfileId: [REQUIRED]\nThe ID of the configuration profile.\n

    :type Name: string
    :param Name: The name of the configuration profile.

    :type Description: string
    :param Description: A description of the configuration profile.

    :type RetrievalRoleArn: string
    :param RetrievalRoleArn: The ARN of an IAM role with permission to access the configuration at the specified LocationUri.

    :type Validators: list
    :param Validators: A list of methods for validating the configuration.\n\n(dict) --A validator provides a syntactic or semantic check to ensure the configuration you want to deploy functions as intended. To validate your application configuration data, you provide a schema or a Lambda function that runs against the configuration. The configuration deployment or update can only proceed when the configuration data is valid.\n\nType (string) -- [REQUIRED]AppConfig supports validators of type JSON_SCHEMA and LAMBDA\n\nContent (string) -- [REQUIRED]Either the JSON Schema content or the Amazon Resource Name (ARN) of an AWS Lambda function.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'Id': 'string',
    'Name': 'string',
    'Description': 'string',
    'LocationUri': 'string',
    'RetrievalRoleArn': 'string',
    'Validators': [
        {
            'Type': 'JSON_SCHEMA'|'LAMBDA',
            'Content': 'string'
        },
    ]
}


Response Structure

(dict) --

ApplicationId (string) --
The application ID.

Id (string) --
The configuration profile ID.

Name (string) --
The name of the configuration profile.

Description (string) --
The configuration profile description.

LocationUri (string) --
The URI location of the configuration.

RetrievalRoleArn (string) --
The ARN of an IAM role with permission to access the configuration at the specified LocationUri.

Validators (list) --
A list of methods for validating the configuration.

(dict) --
A validator provides a syntactic or semantic check to ensure the configuration you want to deploy functions as intended. To validate your application configuration data, you provide a schema or a Lambda function that runs against the configuration. The configuration deployment or update can only proceed when the configuration data is valid.

Type (string) --
AppConfig supports validators of type JSON_SCHEMA and LAMBDA

Content (string) --
Either the JSON Schema content or the Amazon Resource Name (ARN) of an AWS Lambda function.











Exceptions

AppConfig.Client.exceptions.BadRequestException
AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException


    :return: {
        'ApplicationId': 'string',
        'Id': 'string',
        'Name': 'string',
        'Description': 'string',
        'LocationUri': 'string',
        'RetrievalRoleArn': 'string',
        'Validators': [
            {
                'Type': 'JSON_SCHEMA'|'LAMBDA',
                'Content': 'string'
            },
        ]
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.BadRequestException
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.InternalServerException
    
    """
    pass

def update_deployment_strategy(DeploymentStrategyId=None, Description=None, DeploymentDurationInMinutes=None, FinalBakeTimeInMinutes=None, GrowthFactor=None, GrowthType=None):
    """
    Updates a deployment strategy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_deployment_strategy(
        DeploymentStrategyId='string',
        Description='string',
        DeploymentDurationInMinutes=123,
        FinalBakeTimeInMinutes=123,
        GrowthFactor=...,
        GrowthType='LINEAR'|'EXPONENTIAL'
    )
    
    
    :type DeploymentStrategyId: string
    :param DeploymentStrategyId: [REQUIRED]\nThe deployment strategy ID.\n

    :type Description: string
    :param Description: A description of the deployment strategy.

    :type DeploymentDurationInMinutes: integer
    :param DeploymentDurationInMinutes: Total amount of time for a deployment to last.

    :type FinalBakeTimeInMinutes: integer
    :param FinalBakeTimeInMinutes: The amount of time AppConfig monitors for alarms before considering the deployment to be complete and no longer eligible for automatic roll back.

    :type GrowthFactor: float
    :param GrowthFactor: The percentage of targets to receive a deployed configuration during each interval.

    :type GrowthType: string
    :param GrowthType: The algorithm used to define how percentage grows over time. AWS AppConfig supports the following growth types:\n\nLinear : For this type, AppConfig processes the deployment by increments of the growth factor evenly distributed over the deployment time. For example, a linear deployment that uses a growth factor of 20 initially makes the configuration available to 20 percent of the targets. After 1/5th of the deployment time has passed, the system updates the percentage to 40 percent. This continues until 100% of the targets are set to receive the deployed configuration.Exponential : For this type, AppConfig processes the deployment exponentially using the following formula: G*(2^N) . In this formula, G is the growth factor specified by the user and N is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows:\n2*(2^0)\n2*(2^1)\n2*(2^2)\n\nExpressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Id': 'string',
    'Name': 'string',
    'Description': 'string',
    'DeploymentDurationInMinutes': 123,
    'GrowthType': 'LINEAR'|'EXPONENTIAL',
    'GrowthFactor': ...,
    'FinalBakeTimeInMinutes': 123,
    'ReplicateTo': 'NONE'|'SSM_DOCUMENT'
}


Response Structure

(dict) --

Id (string) --
The deployment strategy ID.

Name (string) --
The name of the deployment strategy.

Description (string) --
The description of the deployment strategy.

DeploymentDurationInMinutes (integer) --
Total amount of time the deployment lasted.

GrowthType (string) --
The algorithm used to define how percentage grew over time.

GrowthFactor (float) --
The percentage of targets that received a deployed configuration during each interval.

FinalBakeTimeInMinutes (integer) --
The amount of time AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic roll back.

ReplicateTo (string) --
Save the deployment strategy to a Systems Manager (SSM) document.







Exceptions

AppConfig.Client.exceptions.BadRequestException
AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException


    :return: {
        'Id': 'string',
        'Name': 'string',
        'Description': 'string',
        'DeploymentDurationInMinutes': 123,
        'GrowthType': 'LINEAR'|'EXPONENTIAL',
        'GrowthFactor': ...,
        'FinalBakeTimeInMinutes': 123,
        'ReplicateTo': 'NONE'|'SSM_DOCUMENT'
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.BadRequestException
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.InternalServerException
    
    """
    pass

def update_environment(ApplicationId=None, EnvironmentId=None, Name=None, Description=None, Monitors=None):
    """
    Updates an environment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_environment(
        ApplicationId='string',
        EnvironmentId='string',
        Name='string',
        Description='string',
        Monitors=[
            {
                'AlarmArn': 'string',
                'AlarmRoleArn': 'string'
            },
        ]
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe application ID.\n

    :type EnvironmentId: string
    :param EnvironmentId: [REQUIRED]\nThe environment ID.\n

    :type Name: string
    :param Name: The name of the environment.

    :type Description: string
    :param Description: A description of the environment.

    :type Monitors: list
    :param Monitors: Amazon CloudWatch alarms to monitor during the deployment process.\n\n(dict) --Amazon CloudWatch alarms to monitor during the deployment process.\n\nAlarmArn (string) --ARN of the Amazon CloudWatch alarm.\n\nAlarmRoleArn (string) --ARN of an IAM role for AppConfig to monitor AlarmArn .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'Id': 'string',
    'Name': 'string',
    'Description': 'string',
    'State': 'READY_FOR_DEPLOYMENT'|'DEPLOYING'|'ROLLING_BACK'|'ROLLED_BACK',
    'Monitors': [
        {
            'AlarmArn': 'string',
            'AlarmRoleArn': 'string'
        },
    ]
}


Response Structure

(dict) --

ApplicationId (string) --
The application ID.

Id (string) --
The environment ID.

Name (string) --
The name of the environment.

Description (string) --
The description of the environment.

State (string) --
The state of the environment. An environment can be in one of the following states: READY_FOR_DEPLOYMENT , DEPLOYING , ROLLING_BACK , or ROLLED_BACK

Monitors (list) --
Amazon CloudWatch alarms monitored during the deployment.

(dict) --
Amazon CloudWatch alarms to monitor during the deployment process.

AlarmArn (string) --
ARN of the Amazon CloudWatch alarm.

AlarmRoleArn (string) --
ARN of an IAM role for AppConfig to monitor AlarmArn .











Exceptions

AppConfig.Client.exceptions.BadRequestException
AppConfig.Client.exceptions.ResourceNotFoundException
AppConfig.Client.exceptions.InternalServerException


    :return: {
        'ApplicationId': 'string',
        'Id': 'string',
        'Name': 'string',
        'Description': 'string',
        'State': 'READY_FOR_DEPLOYMENT'|'DEPLOYING'|'ROLLING_BACK'|'ROLLED_BACK',
        'Monitors': [
            {
                'AlarmArn': 'string',
                'AlarmRoleArn': 'string'
            },
        ]
    }
    
    
    :returns: 
    AppConfig.Client.exceptions.BadRequestException
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.InternalServerException
    
    """
    pass

def validate_configuration(ApplicationId=None, ConfigurationProfileId=None, ConfigurationVersion=None):
    """
    Uses the validators in a configuration profile to validate a configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.validate_configuration(
        ApplicationId='string',
        ConfigurationProfileId='string',
        ConfigurationVersion='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe application ID.\n

    :type ConfigurationProfileId: string
    :param ConfigurationProfileId: [REQUIRED]\nThe configuration profile ID.\n

    :type ConfigurationVersion: string
    :param ConfigurationVersion: [REQUIRED]\nThe version of the configuration to validate.\n

    :returns: 
    AppConfig.Client.exceptions.BadRequestException
    AppConfig.Client.exceptions.ResourceNotFoundException
    AppConfig.Client.exceptions.InternalServerException
    
    """
    pass

