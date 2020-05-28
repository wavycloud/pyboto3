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

def create_application(Author=None, Description=None, HomePageUrl=None, Labels=None, LicenseBody=None, LicenseUrl=None, Name=None, ReadmeBody=None, ReadmeUrl=None, SemanticVersion=None, SourceCodeArchiveUrl=None, SourceCodeUrl=None, SpdxLicenseId=None, TemplateBody=None, TemplateUrl=None):
    """
    Creates an application, optionally including an AWS SAM file to create the first application version in the same call.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_application(
        Author='string',
        Description='string',
        HomePageUrl='string',
        Labels=[
            'string',
        ],
        LicenseBody='string',
        LicenseUrl='string',
        Name='string',
        ReadmeBody='string',
        ReadmeUrl='string',
        SemanticVersion='string',
        SourceCodeArchiveUrl='string',
        SourceCodeUrl='string',
        SpdxLicenseId='string',
        TemplateBody='string',
        TemplateUrl='string'
    )
    
    
    :type Author: string
    :param Author: [REQUIRED]\nThe name of the author publishing the app.\nMinimum length=1. Maximum length=127.\nPattern '^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$';\n

    :type Description: string
    :param Description: [REQUIRED]\nThe description of the application.\nMinimum length=1. Maximum length=256\n

    :type HomePageUrl: string
    :param HomePageUrl: A URL with more information about the application, for example the location of your GitHub repository for the application.

    :type Labels: list
    :param Labels: Labels to improve discovery of apps in search results.\nMinimum length=1. Maximum length=127. Maximum number of labels: 10\nPattern: '^[a-zA-Z0-9+\\-_:\\/@]+$';\n\n(string) --\n\n

    :type LicenseBody: string
    :param LicenseBody: A local text file that contains the license of the app that matches the spdxLicenseID value of your application. The file has the format file://<path>/<filename>.\nMaximum size 5 MB\nYou can specify only one of licenseBody and licenseUrl; otherwise, an error results.\n

    :type LicenseUrl: string
    :param LicenseUrl: A link to the S3 object that contains the license of the app that matches the spdxLicenseID value of your application.\nMaximum size 5 MB\nYou can specify only one of licenseBody and licenseUrl; otherwise, an error results.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the application that you want to publish.\nMinimum length=1. Maximum length=140\nPattern: '[a-zA-Z0-9\\-]+';\n

    :type ReadmeBody: string
    :param ReadmeBody: A local text readme file in Markdown language that contains a more detailed description of the application and how it works. The file has the format file://<path>/<filename>.\nMaximum size 5 MB\nYou can specify only one of readmeBody and readmeUrl; otherwise, an error results.\n

    :type ReadmeUrl: string
    :param ReadmeUrl: A link to the S3 object in Markdown language that contains a more detailed description of the application and how it works.\nMaximum size 5 MB\nYou can specify only one of readmeBody and readmeUrl; otherwise, an error results.\n

    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application:\n\nhttps://semver.org/\n

    :type SourceCodeArchiveUrl: string
    :param SourceCodeArchiveUrl: A link to the S3 object that contains the ZIP archive of the source code for this version of your application.\nMaximum size 50 MB\n

    :type SourceCodeUrl: string
    :param SourceCodeUrl: A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.

    :type SpdxLicenseId: string
    :param SpdxLicenseId: A valid identifier from https://spdx.org/licenses/ .

    :type TemplateBody: string
    :param TemplateBody: The local raw packaged AWS SAM template file of your application. The file has the format file://<path>/<filename>.\nYou can specify only one of templateBody and templateUrl; otherwise an error results.\n

    :type TemplateUrl: string
    :param TemplateUrl: A link to the S3 object containing the packaged AWS SAM template of your application.\nYou can specify only one of templateBody and templateUrl; otherwise an error results.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'Author': 'string',
    'CreationTime': 'string',
    'Description': 'string',
    'HomePageUrl': 'string',
    'IsVerifiedAuthor': True|False,
    'Labels': [
        'string',
    ],
    'LicenseUrl': 'string',
    'Name': 'string',
    'ReadmeUrl': 'string',
    'SpdxLicenseId': 'string',
    'VerifiedAuthorUrl': 'string',
    'Version': {
        'ApplicationId': 'string',
        'CreationTime': 'string',
        'ParameterDefinitions': [
            {
                'AllowedPattern': 'string',
                'AllowedValues': [
                    'string',
                ],
                'ConstraintDescription': 'string',
                'DefaultValue': 'string',
                'Description': 'string',
                'MaxLength': 123,
                'MaxValue': 123,
                'MinLength': 123,
                'MinValue': 123,
                'Name': 'string',
                'NoEcho': True|False,
                'ReferencedByResources': [
                    'string',
                ],
                'Type': 'string'
            },
        ],
        'RequiredCapabilities': [
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND'|'CAPABILITY_RESOURCE_POLICY',
        ],
        'ResourcesSupported': True|False,
        'SemanticVersion': 'string',
        'SourceCodeArchiveUrl': 'string',
        'SourceCodeUrl': 'string',
        'TemplateUrl': 'string'
    }
}


Response Structure

(dict) --
Success

ApplicationId (string) --
The application Amazon Resource Name (ARN).

Author (string) --
The name of the author publishing the app.
Minimum length=1. Maximum length=127.
Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";

CreationTime (string) --
The date and time this resource was created.

Description (string) --
The description of the application.
Minimum length=1. Maximum length=256

HomePageUrl (string) --
A URL with more information about the application, for example the location of your GitHub repository for the application.

IsVerifiedAuthor (boolean) --
Whether the author of this application has been verified. This means means that AWS has made a good faith review, as a reasonable and prudent service provider, of the information provided by the requester and has confirmed that the requester\'s identity is as claimed.

Labels (list) --
Labels to improve discovery of apps in search results.
Minimum length=1. Maximum length=127. Maximum number of labels: 10
Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";

(string) --


LicenseUrl (string) --
A link to a license file of the app that matches the spdxLicenseID value of your application.
Maximum size 5 MB

Name (string) --
The name of the application.
Minimum length=1. Maximum length=140
Pattern: "[a-zA-Z0-9\\-]+";

ReadmeUrl (string) --
A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.
Maximum size 5 MB

SpdxLicenseId (string) --
A valid identifier from https://spdx.org/licenses/.

VerifiedAuthorUrl (string) --
The URL to the public profile of a verified author. This URL is submitted by the author.

Version (dict) --
Version information about the application.

ApplicationId (string) --
The application Amazon Resource Name (ARN).

CreationTime (string) --
The date and time this resource was created.

ParameterDefinitions (list) --
An array of parameter types supported by the application.

(dict) --
Parameters supported by the application.

AllowedPattern (string) --
A regular expression that represents the patterns to allow for String types.

AllowedValues (list) --
An array containing the list of values allowed for the parameter.

(string) --


ConstraintDescription (string) --
A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user specifies an invalid value:
Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+
By adding a constraint description, such as "must contain only uppercase and lowercase letters and numbers," you can display the following customized error message:
Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers.

DefaultValue (string) --
A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints.

Description (string) --
A string of up to 4,000 characters that describes the parameter.

MaxLength (integer) --
An integer value that determines the largest number of characters that you want to allow for String types.

MaxValue (integer) --
A numeric value that determines the largest numeric value that you want to allow for Number types.

MinLength (integer) --
An integer value that determines the smallest number of characters that you want to allow for String types.

MinValue (integer) --
A numeric value that determines the smallest numeric value that you want to allow for Number types.

Name (string) --
The name of the parameter.

NoEcho (boolean) --
Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the value to true, the parameter value is masked with asterisks (*).

ReferencedByResources (list) --
A list of AWS SAM resources that use this parameter.

(string) --


Type (string) --
The type of the parameter.
Valid values: String | Number | List<Number> | CommaDelimitedList
String: A literal string.
For example, users can specify "MyUserName".
Number: An integer or float. AWS CloudFormation validates the parameter value as a number. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a string.
For example, users might specify "8888".
List<Number>: An array of integers or floats that are separated by commas. AWS CloudFormation validates the parameter value as numbers. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a list of strings.
For example, users might specify "80,20", and then Ref results in ["80","20"].
CommaDelimitedList: An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas. Also, each member string is space-trimmed.
For example, users might specify "test,dev,prod", and then Ref results in ["test","dev","prod"].





RequiredCapabilities (list) --
A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.
The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY, and CAPABILITY_AUTO_EXPAND.
The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: AWS::IAM::Group , AWS::IAM::InstanceProfile , AWS::IAM::Policy , and AWS::IAM::Role . If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.
The following resources require you to specify CAPABILITY_RESOURCE_POLICY: AWS::Lambda::Permission , AWS::IAM:Policy , AWS::ApplicationAutoScaling::ScalingPolicy , AWS::S3::BucketPolicy , AWS::SQS::QueuePolicy , and AWS::SNS::TopicPolicy .
Applications that contain one or more nested applications require you to specify CAPABILITY_AUTO_EXPAND.
If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don\'t specify this parameter for an application that requires capabilities, the call will fail.

(string) --
Values that must be specified in order to deploy some applications.



ResourcesSupported (boolean) --
Whether all of the AWS resources contained in this application are supported in the region in which it is being retrieved.

SemanticVersion (string) --
The semantic version of the application:

https://semver.org/


SourceCodeArchiveUrl (string) --
A link to the S3 object that contains the ZIP archive of the source code for this version of your application.
Maximum size 50 MB

SourceCodeUrl (string) --
A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.

TemplateUrl (string) --
A link to the packaged AWS SAM template of your application.









Exceptions

ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
ServerlessApplicationRepository.Client.exceptions.BadRequestException
ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
ServerlessApplicationRepository.Client.exceptions.ConflictException
ServerlessApplicationRepository.Client.exceptions.ForbiddenException


    :return: {
        'ApplicationId': 'string',
        'Author': 'string',
        'CreationTime': 'string',
        'Description': 'string',
        'HomePageUrl': 'string',
        'IsVerifiedAuthor': True|False,
        'Labels': [
            'string',
        ],
        'LicenseUrl': 'string',
        'Name': 'string',
        'ReadmeUrl': 'string',
        'SpdxLicenseId': 'string',
        'VerifiedAuthorUrl': 'string',
        'Version': {
            'ApplicationId': 'string',
            'CreationTime': 'string',
            'ParameterDefinitions': [
                {
                    'AllowedPattern': 'string',
                    'AllowedValues': [
                        'string',
                    ],
                    'ConstraintDescription': 'string',
                    'DefaultValue': 'string',
                    'Description': 'string',
                    'MaxLength': 123,
                    'MaxValue': 123,
                    'MinLength': 123,
                    'MinValue': 123,
                    'Name': 'string',
                    'NoEcho': True|False,
                    'ReferencedByResources': [
                        'string',
                    ],
                    'Type': 'string'
                },
            ],
            'RequiredCapabilities': [
                'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND'|'CAPABILITY_RESOURCE_POLICY',
            ],
            'ResourcesSupported': True|False,
            'SemanticVersion': 'string',
            'SourceCodeArchiveUrl': 'string',
            'SourceCodeUrl': 'string',
            'TemplateUrl': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_application_version(ApplicationId=None, SemanticVersion=None, SourceCodeArchiveUrl=None, SourceCodeUrl=None, TemplateBody=None, TemplateUrl=None):
    """
    Creates an application version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_application_version(
        ApplicationId='string',
        SemanticVersion='string',
        SourceCodeArchiveUrl='string',
        SourceCodeUrl='string',
        TemplateBody='string',
        TemplateUrl='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application.\n

    :type SemanticVersion: string
    :param SemanticVersion: [REQUIRED]\nThe semantic version of the new version.\n

    :type SourceCodeArchiveUrl: string
    :param SourceCodeArchiveUrl: A link to the S3 object that contains the ZIP archive of the source code for this version of your application.\nMaximum size 50 MB\n

    :type SourceCodeUrl: string
    :param SourceCodeUrl: A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.

    :type TemplateBody: string
    :param TemplateBody: The raw packaged AWS SAM template of your application.

    :type TemplateUrl: string
    :param TemplateUrl: A link to the packaged AWS SAM template of your application.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'CreationTime': 'string',
    'ParameterDefinitions': [
        {
            'AllowedPattern': 'string',
            'AllowedValues': [
                'string',
            ],
            'ConstraintDescription': 'string',
            'DefaultValue': 'string',
            'Description': 'string',
            'MaxLength': 123,
            'MaxValue': 123,
            'MinLength': 123,
            'MinValue': 123,
            'Name': 'string',
            'NoEcho': True|False,
            'ReferencedByResources': [
                'string',
            ],
            'Type': 'string'
        },
    ],
    'RequiredCapabilities': [
        'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND'|'CAPABILITY_RESOURCE_POLICY',
    ],
    'ResourcesSupported': True|False,
    'SemanticVersion': 'string',
    'SourceCodeArchiveUrl': 'string',
    'SourceCodeUrl': 'string',
    'TemplateUrl': 'string'
}


Response Structure

(dict) --
Success

ApplicationId (string) --
The application Amazon Resource Name (ARN).

CreationTime (string) --
The date and time this resource was created.

ParameterDefinitions (list) --
An array of parameter types supported by the application.

(dict) --
Parameters supported by the application.

AllowedPattern (string) --
A regular expression that represents the patterns to allow for String types.

AllowedValues (list) --
An array containing the list of values allowed for the parameter.

(string) --


ConstraintDescription (string) --
A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user specifies an invalid value:
Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+
By adding a constraint description, such as "must contain only uppercase and lowercase letters and numbers," you can display the following customized error message:
Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers.

DefaultValue (string) --
A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints.

Description (string) --
A string of up to 4,000 characters that describes the parameter.

MaxLength (integer) --
An integer value that determines the largest number of characters that you want to allow for String types.

MaxValue (integer) --
A numeric value that determines the largest numeric value that you want to allow for Number types.

MinLength (integer) --
An integer value that determines the smallest number of characters that you want to allow for String types.

MinValue (integer) --
A numeric value that determines the smallest numeric value that you want to allow for Number types.

Name (string) --
The name of the parameter.

NoEcho (boolean) --
Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the value to true, the parameter value is masked with asterisks (*).

ReferencedByResources (list) --
A list of AWS SAM resources that use this parameter.

(string) --


Type (string) --
The type of the parameter.
Valid values: String | Number | List<Number> | CommaDelimitedList
String: A literal string.
For example, users can specify "MyUserName".
Number: An integer or float. AWS CloudFormation validates the parameter value as a number. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a string.
For example, users might specify "8888".
List<Number>: An array of integers or floats that are separated by commas. AWS CloudFormation validates the parameter value as numbers. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a list of strings.
For example, users might specify "80,20", and then Ref results in ["80","20"].
CommaDelimitedList: An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas. Also, each member string is space-trimmed.
For example, users might specify "test,dev,prod", and then Ref results in ["test","dev","prod"].





RequiredCapabilities (list) --
A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.
The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY, and CAPABILITY_AUTO_EXPAND.
The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: AWS::IAM::Group , AWS::IAM::InstanceProfile , AWS::IAM::Policy , and AWS::IAM::Role . If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.
The following resources require you to specify CAPABILITY_RESOURCE_POLICY: AWS::Lambda::Permission , AWS::IAM:Policy , AWS::ApplicationAutoScaling::ScalingPolicy , AWS::S3::BucketPolicy , AWS::SQS::QueuePolicy , and AWS::SNS::TopicPolicy .
Applications that contain one or more nested applications require you to specify CAPABILITY_AUTO_EXPAND.
If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don\'t specify this parameter for an application that requires capabilities, the call will fail.

(string) --
Values that must be specified in order to deploy some applications.



ResourcesSupported (boolean) --
Whether all of the AWS resources contained in this application are supported in the region in which it is being retrieved.

SemanticVersion (string) --
The semantic version of the application:

https://semver.org/


SourceCodeArchiveUrl (string) --
A link to the S3 object that contains the ZIP archive of the source code for this version of your application.
Maximum size 50 MB

SourceCodeUrl (string) --
A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.

TemplateUrl (string) --
A link to the packaged AWS SAM template of your application.







Exceptions

ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
ServerlessApplicationRepository.Client.exceptions.BadRequestException
ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
ServerlessApplicationRepository.Client.exceptions.ConflictException
ServerlessApplicationRepository.Client.exceptions.ForbiddenException


    :return: {
        'ApplicationId': 'string',
        'CreationTime': 'string',
        'ParameterDefinitions': [
            {
                'AllowedPattern': 'string',
                'AllowedValues': [
                    'string',
                ],
                'ConstraintDescription': 'string',
                'DefaultValue': 'string',
                'Description': 'string',
                'MaxLength': 123,
                'MaxValue': 123,
                'MinLength': 123,
                'MinValue': 123,
                'Name': 'string',
                'NoEcho': True|False,
                'ReferencedByResources': [
                    'string',
                ],
                'Type': 'string'
            },
        ],
        'RequiredCapabilities': [
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND'|'CAPABILITY_RESOURCE_POLICY',
        ],
        'ResourcesSupported': True|False,
        'SemanticVersion': 'string',
        'SourceCodeArchiveUrl': 'string',
        'SourceCodeUrl': 'string',
        'TemplateUrl': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_cloud_formation_change_set(ApplicationId=None, Capabilities=None, ChangeSetName=None, ClientToken=None, Description=None, NotificationArns=None, ParameterOverrides=None, ResourceTypes=None, RollbackConfiguration=None, SemanticVersion=None, StackName=None, Tags=None, TemplateId=None):
    """
    Creates an AWS CloudFormation change set for the given application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_cloud_formation_change_set(
        ApplicationId='string',
        Capabilities=[
            'string',
        ],
        ChangeSetName='string',
        ClientToken='string',
        Description='string',
        NotificationArns=[
            'string',
        ],
        ParameterOverrides=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        ResourceTypes=[
            'string',
        ],
        RollbackConfiguration={
            'MonitoringTimeInMinutes': 123,
            'RollbackTriggers': [
                {
                    'Arn': 'string',
                    'Type': 'string'
                },
            ]
        },
        SemanticVersion='string',
        StackName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        TemplateId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application.\n

    :type Capabilities: list
    :param Capabilities: A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.\nThe only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY, and CAPABILITY_AUTO_EXPAND.\nThe following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: AWS::IAM::Group , AWS::IAM::InstanceProfile , AWS::IAM::Policy , and AWS::IAM::Role . If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.\nThe following resources require you to specify CAPABILITY_RESOURCE_POLICY: AWS::Lambda::Permission , AWS::IAM:Policy , AWS::ApplicationAutoScaling::ScalingPolicy , AWS::S3::BucketPolicy , AWS::SQS::QueuePolicy , and AWS::SNS:TopicPolicy .\nApplications that contain one or more nested applications require you to specify CAPABILITY_AUTO_EXPAND.\nIf your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don\'t specify this parameter for an application that requires capabilities, the call will fail.\n\n(string) --\n\n

    :type ChangeSetName: string
    :param ChangeSetName: This property corresponds to the parameter of the same name for the *AWS CloudFormation CreateChangeSet * API.

    :type ClientToken: string
    :param ClientToken: This property corresponds to the parameter of the same name for the *AWS CloudFormation CreateChangeSet * API.

    :type Description: string
    :param Description: This property corresponds to the parameter of the same name for the *AWS CloudFormation CreateChangeSet * API.

    :type NotificationArns: list
    :param NotificationArns: This property corresponds to the parameter of the same name for the *AWS CloudFormation CreateChangeSet * API.\n\n(string) --\n\n

    :type ParameterOverrides: list
    :param ParameterOverrides: A list of parameter values for the parameters of the application.\n\n(dict) --Parameter value of the application.\n\nName (string) -- [REQUIRED]The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.\n\nValue (string) -- [REQUIRED]The input value associated with the parameter.\n\n\n\n\n

    :type ResourceTypes: list
    :param ResourceTypes: This property corresponds to the parameter of the same name for the *AWS CloudFormation CreateChangeSet * API.\n\n(string) --\n\n

    :type RollbackConfiguration: dict
    :param RollbackConfiguration: This property corresponds to the parameter of the same name for the *AWS CloudFormation CreateChangeSet * API.\n\nMonitoringTimeInMinutes (integer) --This property corresponds to the content of the same name for the *AWS CloudFormation RollbackConfiguration * Data Type.\n\nRollbackTriggers (list) --This property corresponds to the content of the same name for the *AWS CloudFormation RollbackConfiguration * Data Type.\n\n(dict) --This property corresponds to the *AWS CloudFormation RollbackTrigger * Data Type.\n\nArn (string) -- [REQUIRED]This property corresponds to the content of the same name for the *AWS CloudFormation RollbackTrigger * Data Type.\n\nType (string) -- [REQUIRED]This property corresponds to the content of the same name for the *AWS CloudFormation RollbackTrigger * Data Type.\n\n\n\n\n\n\n

    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application:\n\nhttps://semver.org/\n

    :type StackName: string
    :param StackName: [REQUIRED]\nThis property corresponds to the parameter of the same name for the *AWS CloudFormation CreateChangeSet * API.\n

    :type Tags: list
    :param Tags: This property corresponds to the parameter of the same name for the *AWS CloudFormation CreateChangeSet * API.\n\n(dict) --This property corresponds to the *AWS CloudFormation Tag * Data Type.\n\nKey (string) -- [REQUIRED]This property corresponds to the content of the same name for the *AWS CloudFormation Tag * Data Type.\n\nValue (string) -- [REQUIRED]This property corresponds to the content of the same name for the *AWS CloudFormation Tag * Data Type.\n\n\n\n\n

    :type TemplateId: string
    :param TemplateId: The UUID returned by CreateCloudFormationTemplate.\nPattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'ChangeSetId': 'string',
    'SemanticVersion': 'string',
    'StackId': 'string'
}


Response Structure

(dict) --
Success

ApplicationId (string) --
The application Amazon Resource Name (ARN).

ChangeSetId (string) --
The Amazon Resource Name (ARN) of the change set.
Length constraints: Minimum length of 1.
Pattern: ARN:[-a-zA-Z0-9:/]*

SemanticVersion (string) --
The semantic version of the application:

https://semver.org/


StackId (string) --
The unique ID of the stack.







Exceptions

ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
ServerlessApplicationRepository.Client.exceptions.BadRequestException
ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
ServerlessApplicationRepository.Client.exceptions.ForbiddenException


    :return: {
        'ApplicationId': 'string',
        'ChangeSetId': 'string',
        'SemanticVersion': 'string',
        'StackId': 'string'
    }
    
    
    :returns: 
    ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
    ServerlessApplicationRepository.Client.exceptions.BadRequestException
    ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
    ServerlessApplicationRepository.Client.exceptions.ForbiddenException
    
    """
    pass

def create_cloud_formation_template(ApplicationId=None, SemanticVersion=None):
    """
    Creates an AWS CloudFormation template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_cloud_formation_template(
        ApplicationId='string',
        SemanticVersion='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application.\n

    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application:\n\nhttps://semver.org/\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'CreationTime': 'string',
    'ExpirationTime': 'string',
    'SemanticVersion': 'string',
    'Status': 'PREPARING'|'ACTIVE'|'EXPIRED',
    'TemplateId': 'string',
    'TemplateUrl': 'string'
}


Response Structure

(dict) --
Success

ApplicationId (string) --
The application Amazon Resource Name (ARN).

CreationTime (string) --
The date and time this resource was created.

ExpirationTime (string) --
The date and time this template expires. Templates expire 1 hour after creation.

SemanticVersion (string) --
The semantic version of the application:

https://semver.org/


Status (string) --
Status of the template creation workflow.
Possible values: PREPARING | ACTIVE | EXPIRED

TemplateId (string) --
The UUID returned by CreateCloudFormationTemplate.
Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}

TemplateUrl (string) --
A link to the template that can be used to deploy the application using AWS CloudFormation.







Exceptions

ServerlessApplicationRepository.Client.exceptions.NotFoundException
ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
ServerlessApplicationRepository.Client.exceptions.BadRequestException
ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
ServerlessApplicationRepository.Client.exceptions.ForbiddenException


    :return: {
        'ApplicationId': 'string',
        'CreationTime': 'string',
        'ExpirationTime': 'string',
        'SemanticVersion': 'string',
        'Status': 'PREPARING'|'ACTIVE'|'EXPIRED',
        'TemplateId': 'string',
        'TemplateUrl': 'string'
    }
    
    
    :returns: 
    ServerlessApplicationRepository.Client.exceptions.NotFoundException
    ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
    ServerlessApplicationRepository.Client.exceptions.BadRequestException
    ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
    ServerlessApplicationRepository.Client.exceptions.ForbiddenException
    
    """
    pass

def delete_application(ApplicationId=None):
    """
    Deletes the specified application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application.\n

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

def get_application(ApplicationId=None, SemanticVersion=None):
    """
    Gets the specified application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_application(
        ApplicationId='string',
        SemanticVersion='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application.\n

    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application to get.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'Author': 'string',
    'CreationTime': 'string',
    'Description': 'string',
    'HomePageUrl': 'string',
    'IsVerifiedAuthor': True|False,
    'Labels': [
        'string',
    ],
    'LicenseUrl': 'string',
    'Name': 'string',
    'ReadmeUrl': 'string',
    'SpdxLicenseId': 'string',
    'VerifiedAuthorUrl': 'string',
    'Version': {
        'ApplicationId': 'string',
        'CreationTime': 'string',
        'ParameterDefinitions': [
            {
                'AllowedPattern': 'string',
                'AllowedValues': [
                    'string',
                ],
                'ConstraintDescription': 'string',
                'DefaultValue': 'string',
                'Description': 'string',
                'MaxLength': 123,
                'MaxValue': 123,
                'MinLength': 123,
                'MinValue': 123,
                'Name': 'string',
                'NoEcho': True|False,
                'ReferencedByResources': [
                    'string',
                ],
                'Type': 'string'
            },
        ],
        'RequiredCapabilities': [
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND'|'CAPABILITY_RESOURCE_POLICY',
        ],
        'ResourcesSupported': True|False,
        'SemanticVersion': 'string',
        'SourceCodeArchiveUrl': 'string',
        'SourceCodeUrl': 'string',
        'TemplateUrl': 'string'
    }
}


Response Structure

(dict) --
Success

ApplicationId (string) --
The application Amazon Resource Name (ARN).

Author (string) --
The name of the author publishing the app.
Minimum length=1. Maximum length=127.
Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";

CreationTime (string) --
The date and time this resource was created.

Description (string) --
The description of the application.
Minimum length=1. Maximum length=256

HomePageUrl (string) --
A URL with more information about the application, for example the location of your GitHub repository for the application.

IsVerifiedAuthor (boolean) --
Whether the author of this application has been verified. This means means that AWS has made a good faith review, as a reasonable and prudent service provider, of the information provided by the requester and has confirmed that the requester\'s identity is as claimed.

Labels (list) --
Labels to improve discovery of apps in search results.
Minimum length=1. Maximum length=127. Maximum number of labels: 10
Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";

(string) --


LicenseUrl (string) --
A link to a license file of the app that matches the spdxLicenseID value of your application.
Maximum size 5 MB

Name (string) --
The name of the application.
Minimum length=1. Maximum length=140
Pattern: "[a-zA-Z0-9\\-]+";

ReadmeUrl (string) --
A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.
Maximum size 5 MB

SpdxLicenseId (string) --
A valid identifier from https://spdx.org/licenses/.

VerifiedAuthorUrl (string) --
The URL to the public profile of a verified author. This URL is submitted by the author.

Version (dict) --
Version information about the application.

ApplicationId (string) --
The application Amazon Resource Name (ARN).

CreationTime (string) --
The date and time this resource was created.

ParameterDefinitions (list) --
An array of parameter types supported by the application.

(dict) --
Parameters supported by the application.

AllowedPattern (string) --
A regular expression that represents the patterns to allow for String types.

AllowedValues (list) --
An array containing the list of values allowed for the parameter.

(string) --


ConstraintDescription (string) --
A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user specifies an invalid value:
Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+
By adding a constraint description, such as "must contain only uppercase and lowercase letters and numbers," you can display the following customized error message:
Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers.

DefaultValue (string) --
A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints.

Description (string) --
A string of up to 4,000 characters that describes the parameter.

MaxLength (integer) --
An integer value that determines the largest number of characters that you want to allow for String types.

MaxValue (integer) --
A numeric value that determines the largest numeric value that you want to allow for Number types.

MinLength (integer) --
An integer value that determines the smallest number of characters that you want to allow for String types.

MinValue (integer) --
A numeric value that determines the smallest numeric value that you want to allow for Number types.

Name (string) --
The name of the parameter.

NoEcho (boolean) --
Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the value to true, the parameter value is masked with asterisks (*).

ReferencedByResources (list) --
A list of AWS SAM resources that use this parameter.

(string) --


Type (string) --
The type of the parameter.
Valid values: String | Number | List<Number> | CommaDelimitedList
String: A literal string.
For example, users can specify "MyUserName".
Number: An integer or float. AWS CloudFormation validates the parameter value as a number. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a string.
For example, users might specify "8888".
List<Number>: An array of integers or floats that are separated by commas. AWS CloudFormation validates the parameter value as numbers. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a list of strings.
For example, users might specify "80,20", and then Ref results in ["80","20"].
CommaDelimitedList: An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas. Also, each member string is space-trimmed.
For example, users might specify "test,dev,prod", and then Ref results in ["test","dev","prod"].





RequiredCapabilities (list) --
A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.
The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY, and CAPABILITY_AUTO_EXPAND.
The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: AWS::IAM::Group , AWS::IAM::InstanceProfile , AWS::IAM::Policy , and AWS::IAM::Role . If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.
The following resources require you to specify CAPABILITY_RESOURCE_POLICY: AWS::Lambda::Permission , AWS::IAM:Policy , AWS::ApplicationAutoScaling::ScalingPolicy , AWS::S3::BucketPolicy , AWS::SQS::QueuePolicy , and AWS::SNS::TopicPolicy .
Applications that contain one or more nested applications require you to specify CAPABILITY_AUTO_EXPAND.
If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don\'t specify this parameter for an application that requires capabilities, the call will fail.

(string) --
Values that must be specified in order to deploy some applications.



ResourcesSupported (boolean) --
Whether all of the AWS resources contained in this application are supported in the region in which it is being retrieved.

SemanticVersion (string) --
The semantic version of the application:

https://semver.org/


SourceCodeArchiveUrl (string) --
A link to the S3 object that contains the ZIP archive of the source code for this version of your application.
Maximum size 50 MB

SourceCodeUrl (string) --
A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.

TemplateUrl (string) --
A link to the packaged AWS SAM template of your application.









Exceptions

ServerlessApplicationRepository.Client.exceptions.NotFoundException
ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
ServerlessApplicationRepository.Client.exceptions.BadRequestException
ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
ServerlessApplicationRepository.Client.exceptions.ForbiddenException


    :return: {
        'ApplicationId': 'string',
        'Author': 'string',
        'CreationTime': 'string',
        'Description': 'string',
        'HomePageUrl': 'string',
        'IsVerifiedAuthor': True|False,
        'Labels': [
            'string',
        ],
        'LicenseUrl': 'string',
        'Name': 'string',
        'ReadmeUrl': 'string',
        'SpdxLicenseId': 'string',
        'VerifiedAuthorUrl': 'string',
        'Version': {
            'ApplicationId': 'string',
            'CreationTime': 'string',
            'ParameterDefinitions': [
                {
                    'AllowedPattern': 'string',
                    'AllowedValues': [
                        'string',
                    ],
                    'ConstraintDescription': 'string',
                    'DefaultValue': 'string',
                    'Description': 'string',
                    'MaxLength': 123,
                    'MaxValue': 123,
                    'MinLength': 123,
                    'MinValue': 123,
                    'Name': 'string',
                    'NoEcho': True|False,
                    'ReferencedByResources': [
                        'string',
                    ],
                    'Type': 'string'
                },
            ],
            'RequiredCapabilities': [
                'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND'|'CAPABILITY_RESOURCE_POLICY',
            ],
            'ResourcesSupported': True|False,
            'SemanticVersion': 'string',
            'SourceCodeArchiveUrl': 'string',
            'SourceCodeUrl': 'string',
            'TemplateUrl': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_application_policy(ApplicationId=None):
    """
    Retrieves the policy for the application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_application_policy(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Statements': [
        {
            'Actions': [
                'string',
            ],
            'PrincipalOrgIDs': [
                'string',
            ],
            'Principals': [
                'string',
            ],
            'StatementId': 'string'
        },
    ]
}


Response Structure

(dict) --Success

Statements (list) --An array of policy statements applied to the application.

(dict) --Policy statement applied to the application.

Actions (list) --For the list of actions supported for this operation, see Application Permissions .

(string) --


PrincipalOrgIDs (list) --An array of PrinciplalOrgIDs, which corresponds to AWS IAM aws:PrincipalOrgID global condition key.

(string) --


Principals (list) --An array of AWS account IDs, or * to make the application public.

(string) --


StatementId (string) --A unique ID for the statement.










Exceptions

ServerlessApplicationRepository.Client.exceptions.NotFoundException
ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
ServerlessApplicationRepository.Client.exceptions.BadRequestException
ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
ServerlessApplicationRepository.Client.exceptions.ForbiddenException


    :return: {
        'Statements': [
            {
                'Actions': [
                    'string',
                ],
                'PrincipalOrgIDs': [
                    'string',
                ],
                'Principals': [
                    'string',
                ],
                'StatementId': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_cloud_formation_template(ApplicationId=None, TemplateId=None):
    """
    Gets the specified AWS CloudFormation template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_cloud_formation_template(
        ApplicationId='string',
        TemplateId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application.\n

    :type TemplateId: string
    :param TemplateId: [REQUIRED]\nThe UUID returned by CreateCloudFormationTemplate.\nPattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'CreationTime': 'string',
    'ExpirationTime': 'string',
    'SemanticVersion': 'string',
    'Status': 'PREPARING'|'ACTIVE'|'EXPIRED',
    'TemplateId': 'string',
    'TemplateUrl': 'string'
}


Response Structure

(dict) --
Success

ApplicationId (string) --
The application Amazon Resource Name (ARN).

CreationTime (string) --
The date and time this resource was created.

ExpirationTime (string) --
The date and time this template expires. Templates expire 1 hour after creation.

SemanticVersion (string) --
The semantic version of the application:

https://semver.org/


Status (string) --
Status of the template creation workflow.
Possible values: PREPARING | ACTIVE | EXPIRED

TemplateId (string) --
The UUID returned by CreateCloudFormationTemplate.
Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}

TemplateUrl (string) --
A link to the template that can be used to deploy the application using AWS CloudFormation.







Exceptions

ServerlessApplicationRepository.Client.exceptions.NotFoundException
ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
ServerlessApplicationRepository.Client.exceptions.BadRequestException
ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
ServerlessApplicationRepository.Client.exceptions.ForbiddenException


    :return: {
        'ApplicationId': 'string',
        'CreationTime': 'string',
        'ExpirationTime': 'string',
        'SemanticVersion': 'string',
        'Status': 'PREPARING'|'ACTIVE'|'EXPIRED',
        'TemplateId': 'string',
        'TemplateUrl': 'string'
    }
    
    
    :returns: 
    ServerlessApplicationRepository.Client.exceptions.NotFoundException
    ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
    ServerlessApplicationRepository.Client.exceptions.BadRequestException
    ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
    ServerlessApplicationRepository.Client.exceptions.ForbiddenException
    
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

def list_application_dependencies(ApplicationId=None, MaxItems=None, NextToken=None, SemanticVersion=None):
    """
    Retrieves the list of applications nested in the containing application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_application_dependencies(
        ApplicationId='string',
        MaxItems=123,
        NextToken='string',
        SemanticVersion='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application.\n

    :type MaxItems: integer
    :param MaxItems: The total number of items to return.

    :type NextToken: string
    :param NextToken: A token to specify where to start paginating.

    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application to get.

    :rtype: dict

ReturnsResponse Syntax
{
    'Dependencies': [
        {
            'ApplicationId': 'string',
            'SemanticVersion': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success

Dependencies (list) --
An array of application summaries nested in the application.

(dict) --
A nested application summary.

ApplicationId (string) --
The Amazon Resource Name (ARN) of the nested application.

SemanticVersion (string) --
The semantic version of the nested application.





NextToken (string) --
The token to request the next page of results.







Exceptions

ServerlessApplicationRepository.Client.exceptions.NotFoundException
ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
ServerlessApplicationRepository.Client.exceptions.BadRequestException
ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
ServerlessApplicationRepository.Client.exceptions.ForbiddenException


    :return: {
        'Dependencies': [
            {
                'ApplicationId': 'string',
                'SemanticVersion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ServerlessApplicationRepository.Client.exceptions.NotFoundException
    ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
    ServerlessApplicationRepository.Client.exceptions.BadRequestException
    ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
    ServerlessApplicationRepository.Client.exceptions.ForbiddenException
    
    """
    pass

def list_application_versions(ApplicationId=None, MaxItems=None, NextToken=None):
    """
    Lists versions for the specified application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_application_versions(
        ApplicationId='string',
        MaxItems=123,
        NextToken='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application.\n

    :type MaxItems: integer
    :param MaxItems: The total number of items to return.

    :type NextToken: string
    :param NextToken: A token to specify where to start paginating.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Versions': [
        {
            'ApplicationId': 'string',
            'CreationTime': 'string',
            'SemanticVersion': 'string',
            'SourceCodeUrl': 'string'
        },
    ]
}


Response Structure

(dict) --
Success

NextToken (string) --
The token to request the next page of results.

Versions (list) --
An array of version summaries for the application.

(dict) --
An application version summary.

ApplicationId (string) --
The application Amazon Resource Name (ARN).

CreationTime (string) --
The date and time this resource was created.

SemanticVersion (string) --
The semantic version of the application:

https://semver.org/


SourceCodeUrl (string) --
A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.











Exceptions

ServerlessApplicationRepository.Client.exceptions.NotFoundException
ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
ServerlessApplicationRepository.Client.exceptions.BadRequestException
ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
ServerlessApplicationRepository.Client.exceptions.ForbiddenException


    :return: {
        'NextToken': 'string',
        'Versions': [
            {
                'ApplicationId': 'string',
                'CreationTime': 'string',
                'SemanticVersion': 'string',
                'SourceCodeUrl': 'string'
            },
        ]
    }
    
    
    :returns: 
    ServerlessApplicationRepository.Client.exceptions.NotFoundException
    ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
    ServerlessApplicationRepository.Client.exceptions.BadRequestException
    ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
    ServerlessApplicationRepository.Client.exceptions.ForbiddenException
    
    """
    pass

def list_applications(MaxItems=None, NextToken=None):
    """
    Lists applications owned by the requester.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_applications(
        MaxItems=123,
        NextToken='string'
    )
    
    
    :type MaxItems: integer
    :param MaxItems: The total number of items to return.

    :type NextToken: string
    :param NextToken: A token to specify where to start paginating.

    :rtype: dict

ReturnsResponse Syntax
{
    'Applications': [
        {
            'ApplicationId': 'string',
            'Author': 'string',
            'CreationTime': 'string',
            'Description': 'string',
            'HomePageUrl': 'string',
            'Labels': [
                'string',
            ],
            'Name': 'string',
            'SpdxLicenseId': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success

Applications (list) --
An array of application summaries.

(dict) --
Summary of details about the application.

ApplicationId (string) --
The application Amazon Resource Name (ARN).

Author (string) --
The name of the author publishing the app.
Minimum length=1. Maximum length=127.
Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";

CreationTime (string) --
The date and time this resource was created.

Description (string) --
The description of the application.
Minimum length=1. Maximum length=256

HomePageUrl (string) --
A URL with more information about the application, for example the location of your GitHub repository for the application.

Labels (list) --
Labels to improve discovery of apps in search results.
Minimum length=1. Maximum length=127. Maximum number of labels: 10
Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";

(string) --


Name (string) --
The name of the application.
Minimum length=1. Maximum length=140
Pattern: "[a-zA-Z0-9\\-]+";

SpdxLicenseId (string) --
A valid identifier from https://spdx.org/licenses/ .





NextToken (string) --
The token to request the next page of results.







Exceptions

ServerlessApplicationRepository.Client.exceptions.NotFoundException
ServerlessApplicationRepository.Client.exceptions.BadRequestException
ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
ServerlessApplicationRepository.Client.exceptions.ForbiddenException


    :return: {
        'Applications': [
            {
                'ApplicationId': 'string',
                'Author': 'string',
                'CreationTime': 'string',
                'Description': 'string',
                'HomePageUrl': 'string',
                'Labels': [
                    'string',
                ],
                'Name': 'string',
                'SpdxLicenseId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_application_policy(ApplicationId=None, Statements=None):
    """
    Sets the permission policy for an application. For the list of actions supported for this operation, see Application Permissions .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_application_policy(
        ApplicationId='string',
        Statements=[
            {
                'Actions': [
                    'string',
                ],
                'PrincipalOrgIDs': [
                    'string',
                ],
                'Principals': [
                    'string',
                ],
                'StatementId': 'string'
            },
        ]
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application.\n

    :type Statements: list
    :param Statements: [REQUIRED]\nAn array of policy statements applied to the application.\n\n(dict) --Policy statement applied to the application.\n\nActions (list) -- [REQUIRED]For the list of actions supported for this operation, see Application Permissions .\n\n(string) --\n\n\nPrincipalOrgIDs (list) --An array of PrinciplalOrgIDs, which corresponds to AWS IAM aws:PrincipalOrgID global condition key.\n\n(string) --\n\n\nPrincipals (list) -- [REQUIRED]An array of AWS account IDs, or * to make the application public.\n\n(string) --\n\n\nStatementId (string) --A unique ID for the statement.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Statements': [
        {
            'Actions': [
                'string',
            ],
            'PrincipalOrgIDs': [
                'string',
            ],
            'Principals': [
                'string',
            ],
            'StatementId': 'string'
        },
    ]
}


Response Structure

(dict) --
Success

Statements (list) --
An array of policy statements applied to the application.

(dict) --
Policy statement applied to the application.

Actions (list) --
For the list of actions supported for this operation, see Application Permissions .

(string) --


PrincipalOrgIDs (list) --
An array of PrinciplalOrgIDs, which corresponds to AWS IAM aws:PrincipalOrgID global condition key.

(string) --


Principals (list) --
An array of AWS account IDs, or * to make the application public.

(string) --


StatementId (string) --
A unique ID for the statement.











Exceptions

ServerlessApplicationRepository.Client.exceptions.NotFoundException
ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
ServerlessApplicationRepository.Client.exceptions.BadRequestException
ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
ServerlessApplicationRepository.Client.exceptions.ForbiddenException


    :return: {
        'Statements': [
            {
                'Actions': [
                    'string',
                ],
                'PrincipalOrgIDs': [
                    'string',
                ],
                'Principals': [
                    'string',
                ],
                'StatementId': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def unshare_application(ApplicationId=None, OrganizationId=None):
    """
    Unshares an application from an AWS Organization.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.unshare_application(
        ApplicationId='string',
        OrganizationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application.\n

    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]\nThe AWS Organization ID to unshare the application from.\n

    :returns: 
    ServerlessApplicationRepository.Client.exceptions.NotFoundException
    ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
    ServerlessApplicationRepository.Client.exceptions.BadRequestException
    ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
    ServerlessApplicationRepository.Client.exceptions.ForbiddenException
    
    """
    pass

def update_application(ApplicationId=None, Author=None, Description=None, HomePageUrl=None, Labels=None, ReadmeBody=None, ReadmeUrl=None):
    """
    Updates the specified application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_application(
        ApplicationId='string',
        Author='string',
        Description='string',
        HomePageUrl='string',
        Labels=[
            'string',
        ],
        ReadmeBody='string',
        ReadmeUrl='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application.\n

    :type Author: string
    :param Author: The name of the author publishing the app.\nMinimum length=1. Maximum length=127.\nPattern '^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$';\n

    :type Description: string
    :param Description: The description of the application.\nMinimum length=1. Maximum length=256\n

    :type HomePageUrl: string
    :param HomePageUrl: A URL with more information about the application, for example the location of your GitHub repository for the application.

    :type Labels: list
    :param Labels: Labels to improve discovery of apps in search results.\nMinimum length=1. Maximum length=127. Maximum number of labels: 10\nPattern: '^[a-zA-Z0-9+\\-_:\\/@]+$';\n\n(string) --\n\n

    :type ReadmeBody: string
    :param ReadmeBody: A text readme file in Markdown language that contains a more detailed description of the application and how it works.\nMaximum size 5 MB\n

    :type ReadmeUrl: string
    :param ReadmeUrl: A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.\nMaximum size 5 MB\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationId': 'string',
    'Author': 'string',
    'CreationTime': 'string',
    'Description': 'string',
    'HomePageUrl': 'string',
    'IsVerifiedAuthor': True|False,
    'Labels': [
        'string',
    ],
    'LicenseUrl': 'string',
    'Name': 'string',
    'ReadmeUrl': 'string',
    'SpdxLicenseId': 'string',
    'VerifiedAuthorUrl': 'string',
    'Version': {
        'ApplicationId': 'string',
        'CreationTime': 'string',
        'ParameterDefinitions': [
            {
                'AllowedPattern': 'string',
                'AllowedValues': [
                    'string',
                ],
                'ConstraintDescription': 'string',
                'DefaultValue': 'string',
                'Description': 'string',
                'MaxLength': 123,
                'MaxValue': 123,
                'MinLength': 123,
                'MinValue': 123,
                'Name': 'string',
                'NoEcho': True|False,
                'ReferencedByResources': [
                    'string',
                ],
                'Type': 'string'
            },
        ],
        'RequiredCapabilities': [
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND'|'CAPABILITY_RESOURCE_POLICY',
        ],
        'ResourcesSupported': True|False,
        'SemanticVersion': 'string',
        'SourceCodeArchiveUrl': 'string',
        'SourceCodeUrl': 'string',
        'TemplateUrl': 'string'
    }
}


Response Structure

(dict) --
Success

ApplicationId (string) --
The application Amazon Resource Name (ARN).

Author (string) --
The name of the author publishing the app.
Minimum length=1. Maximum length=127.
Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";

CreationTime (string) --
The date and time this resource was created.

Description (string) --
The description of the application.
Minimum length=1. Maximum length=256

HomePageUrl (string) --
A URL with more information about the application, for example the location of your GitHub repository for the application.

IsVerifiedAuthor (boolean) --
Whether the author of this application has been verified. This means means that AWS has made a good faith review, as a reasonable and prudent service provider, of the information provided by the requester and has confirmed that the requester\'s identity is as claimed.

Labels (list) --
Labels to improve discovery of apps in search results.
Minimum length=1. Maximum length=127. Maximum number of labels: 10
Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";

(string) --


LicenseUrl (string) --
A link to a license file of the app that matches the spdxLicenseID value of your application.
Maximum size 5 MB

Name (string) --
The name of the application.
Minimum length=1. Maximum length=140
Pattern: "[a-zA-Z0-9\\-]+";

ReadmeUrl (string) --
A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.
Maximum size 5 MB

SpdxLicenseId (string) --
A valid identifier from https://spdx.org/licenses/.

VerifiedAuthorUrl (string) --
The URL to the public profile of a verified author. This URL is submitted by the author.

Version (dict) --
Version information about the application.

ApplicationId (string) --
The application Amazon Resource Name (ARN).

CreationTime (string) --
The date and time this resource was created.

ParameterDefinitions (list) --
An array of parameter types supported by the application.

(dict) --
Parameters supported by the application.

AllowedPattern (string) --
A regular expression that represents the patterns to allow for String types.

AllowedValues (list) --
An array containing the list of values allowed for the parameter.

(string) --


ConstraintDescription (string) --
A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user specifies an invalid value:
Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+
By adding a constraint description, such as "must contain only uppercase and lowercase letters and numbers," you can display the following customized error message:
Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers.

DefaultValue (string) --
A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints.

Description (string) --
A string of up to 4,000 characters that describes the parameter.

MaxLength (integer) --
An integer value that determines the largest number of characters that you want to allow for String types.

MaxValue (integer) --
A numeric value that determines the largest numeric value that you want to allow for Number types.

MinLength (integer) --
An integer value that determines the smallest number of characters that you want to allow for String types.

MinValue (integer) --
A numeric value that determines the smallest numeric value that you want to allow for Number types.

Name (string) --
The name of the parameter.

NoEcho (boolean) --
Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the value to true, the parameter value is masked with asterisks (*).

ReferencedByResources (list) --
A list of AWS SAM resources that use this parameter.

(string) --


Type (string) --
The type of the parameter.
Valid values: String | Number | List<Number> | CommaDelimitedList
String: A literal string.
For example, users can specify "MyUserName".
Number: An integer or float. AWS CloudFormation validates the parameter value as a number. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a string.
For example, users might specify "8888".
List<Number>: An array of integers or floats that are separated by commas. AWS CloudFormation validates the parameter value as numbers. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a list of strings.
For example, users might specify "80,20", and then Ref results in ["80","20"].
CommaDelimitedList: An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas. Also, each member string is space-trimmed.
For example, users might specify "test,dev,prod", and then Ref results in ["test","dev","prod"].





RequiredCapabilities (list) --
A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.
The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY, and CAPABILITY_AUTO_EXPAND.
The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: AWS::IAM::Group , AWS::IAM::InstanceProfile , AWS::IAM::Policy , and AWS::IAM::Role . If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.
The following resources require you to specify CAPABILITY_RESOURCE_POLICY: AWS::Lambda::Permission , AWS::IAM:Policy , AWS::ApplicationAutoScaling::ScalingPolicy , AWS::S3::BucketPolicy , AWS::SQS::QueuePolicy , and AWS::SNS::TopicPolicy .
Applications that contain one or more nested applications require you to specify CAPABILITY_AUTO_EXPAND.
If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don\'t specify this parameter for an application that requires capabilities, the call will fail.

(string) --
Values that must be specified in order to deploy some applications.



ResourcesSupported (boolean) --
Whether all of the AWS resources contained in this application are supported in the region in which it is being retrieved.

SemanticVersion (string) --
The semantic version of the application:

https://semver.org/


SourceCodeArchiveUrl (string) --
A link to the S3 object that contains the ZIP archive of the source code for this version of your application.
Maximum size 50 MB

SourceCodeUrl (string) --
A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.

TemplateUrl (string) --
A link to the packaged AWS SAM template of your application.









Exceptions

ServerlessApplicationRepository.Client.exceptions.BadRequestException
ServerlessApplicationRepository.Client.exceptions.InternalServerErrorException
ServerlessApplicationRepository.Client.exceptions.ForbiddenException
ServerlessApplicationRepository.Client.exceptions.NotFoundException
ServerlessApplicationRepository.Client.exceptions.TooManyRequestsException
ServerlessApplicationRepository.Client.exceptions.ConflictException


    :return: {
        'ApplicationId': 'string',
        'Author': 'string',
        'CreationTime': 'string',
        'Description': 'string',
        'HomePageUrl': 'string',
        'IsVerifiedAuthor': True|False,
        'Labels': [
            'string',
        ],
        'LicenseUrl': 'string',
        'Name': 'string',
        'ReadmeUrl': 'string',
        'SpdxLicenseId': 'string',
        'VerifiedAuthorUrl': 'string',
        'Version': {
            'ApplicationId': 'string',
            'CreationTime': 'string',
            'ParameterDefinitions': [
                {
                    'AllowedPattern': 'string',
                    'AllowedValues': [
                        'string',
                    ],
                    'ConstraintDescription': 'string',
                    'DefaultValue': 'string',
                    'Description': 'string',
                    'MaxLength': 123,
                    'MaxValue': 123,
                    'MinLength': 123,
                    'MinValue': 123,
                    'Name': 'string',
                    'NoEcho': True|False,
                    'ReferencedByResources': [
                        'string',
                    ],
                    'Type': 'string'
                },
            ],
            'RequiredCapabilities': [
                'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND'|'CAPABILITY_RESOURCE_POLICY',
            ],
            'ResourcesSupported': True|False,
            'SemanticVersion': 'string',
            'SourceCodeArchiveUrl': 'string',
            'SourceCodeUrl': 'string',
            'TemplateUrl': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

