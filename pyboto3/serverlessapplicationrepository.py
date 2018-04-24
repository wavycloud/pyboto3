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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    """
    pass

def create_application(Author=None, Description=None, HomePageUrl=None, Labels=None, LicenseBody=None, LicenseUrl=None, Name=None, ReadmeBody=None, ReadmeUrl=None, SemanticVersion=None, SourceCodeUrl=None, SpdxLicenseId=None, TemplateBody=None, TemplateUrl=None):
    """
    Creates an application, optionally including an AWS SAM file to create the first application version in the same call.
    See also: AWS API Documentation
    
    
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
        SourceCodeUrl='string',
        SpdxLicenseId='string',
        TemplateBody='string',
        TemplateUrl='string'
    )
    
    
    :type Author: string
    :param Author: The name of the author publishing the app.
            Min Length=1. Max Length=127.
            Pattern '^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$';
            

    :type Description: string
    :param Description: The description of the application.
            Min Length=1. Max Length=256
            

    :type HomePageUrl: string
    :param HomePageUrl: A URL with more information about the application, for example the location of your GitHub repository for the application.

    :type Labels: list
    :param Labels: Labels to improve discovery of apps in search results.
            Min Length=1. Max Length=127. Maximum number of labels: 10
            Pattern: '^[a-zA-Z0-9+\-_:\/@]+$';
            (string) --
            

    :type LicenseBody: string
    :param LicenseBody: A raw text file that contains the license of the app that matches the spdxLicenseID of your application.
            Max size 5 MB
            

    :type LicenseUrl: string
    :param LicenseUrl: A link to a license file of the app that matches the spdxLicenseID of your application.
            Max size 5 MB
            

    :type Name: string
    :param Name: The name of the application you want to publish.
            Min Length=1. Max Length=140
            Pattern: '[a-zA-Z0-9\-]+';
            

    :type ReadmeBody: string
    :param ReadmeBody: A raw text Readme file that contains a more detailed description of the application and how it works in markdown language.
            Max size 5 MB
            

    :type ReadmeUrl: string
    :param ReadmeUrl: A link to the Readme file that contains a more detailed description of the application and how it works in markdown language.
            Max size 5 MB
            

    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application:
            https://semver.org/
            

    :type SourceCodeUrl: string
    :param SourceCodeUrl: A link to a public repository for the source code of your application.

    :type SpdxLicenseId: string
    :param SpdxLicenseId: A valid identifier from https://spdx.org/licenses/ .

    :type TemplateBody: string
    :param TemplateBody: The raw packaged AWS SAM template of your application.

    :type TemplateUrl: string
    :param TemplateUrl: A link to the packaged AWS SAM template of your application.

    :rtype: dict
    :return: {
        'ApplicationId': 'string',
        'Author': 'string',
        'CreationTime': 'string',
        'Description': 'string',
        'HomePageUrl': 'string',
        'Labels': [
            'string',
        ],
        'LicenseUrl': 'string',
        'Name': 'string',
        'ReadmeUrl': 'string',
        'SpdxLicenseId': 'string',
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
            'SemanticVersion': 'string',
            'SourceCodeUrl': 'string',
            'TemplateUrl': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_application_version(ApplicationId=None, SemanticVersion=None, SourceCodeUrl=None, TemplateBody=None, TemplateUrl=None):
    """
    Creates an application version.
    See also: AWS API Documentation
    
    
    :example: response = client.create_application_version(
        ApplicationId='string',
        SemanticVersion='string',
        SourceCodeUrl='string',
        TemplateBody='string',
        TemplateUrl='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The ID of the application to get.
            

    :type SemanticVersion: string
    :param SemanticVersion: [REQUIRED]
            The semantic version of the new version.
            

    :type SourceCodeUrl: string
    :param SourceCodeUrl: A link to a public repository for the source code of your application.

    :type TemplateBody: string
    :param TemplateBody: The raw packaged AWS SAM template of your application.

    :type TemplateUrl: string
    :param TemplateUrl: A link to the packaged AWS SAM template of your application.

    :rtype: dict
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
        'SemanticVersion': 'string',
        'SourceCodeUrl': 'string',
        'TemplateUrl': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_cloud_formation_change_set(ApplicationId=None, ParameterOverrides=None, SemanticVersion=None, StackName=None):
    """
    Creates an AWS CloudFormation ChangeSet for the given application.
    See also: AWS API Documentation
    
    
    :example: response = client.create_cloud_formation_change_set(
        ApplicationId='string',
        ParameterOverrides=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        SemanticVersion='string',
        StackName='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The ID of the application to get.
            

    :type ParameterOverrides: list
    :param ParameterOverrides: A list of parameter values for the parameters of the application.
            (dict) --Parameter value of the application.
            Name (string) -- [REQUIRED]The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
            Value (string) -- [REQUIRED]The input value associated with the parameter.
            
            

    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application:
            https://semver.org/
            

    :type StackName: string
    :param StackName: The name or the unique ID of the stack for which you are creating a change set. AWS CloudFormation generates the change set by comparing this stack's information with the information that you submit, such as a modified template or different parameter input values.
            Constraints: Minimum length of 1.
            Pattern: ([a-zA-Z][-a-zA-Z0-9]*)|(arn:b(aws|aws-us-gov|aws-cn)b:[-a-zA-Z0-9:/._+]*)
            

    :rtype: dict
    :return: {
        'ApplicationId': 'string',
        'ChangeSetId': 'string',
        'SemanticVersion': 'string',
        'StackId': 'string'
    }
    
    
    """
    pass

def delete_application(ApplicationId=None):
    """
    Deletes the specified application.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_application(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The ID of the application to get.
            

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

def get_application(ApplicationId=None, SemanticVersion=None):
    """
    Gets the specified application.
    See also: AWS API Documentation
    
    
    :example: response = client.get_application(
        ApplicationId='string',
        SemanticVersion='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The ID of the application to get.
            

    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application to get.

    :rtype: dict
    :return: {
        'ApplicationId': 'string',
        'Author': 'string',
        'CreationTime': 'string',
        'Description': 'string',
        'HomePageUrl': 'string',
        'Labels': [
            'string',
        ],
        'LicenseUrl': 'string',
        'Name': 'string',
        'ReadmeUrl': 'string',
        'SpdxLicenseId': 'string',
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
            'SemanticVersion': 'string',
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
    Gets the policy for the specified application.
    See also: AWS API Documentation
    
    
    :example: response = client.get_application_policy(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The ID of the application to get.
            

    :rtype: dict
    :return: {
        'Statements': [
            {
                'Actions': [
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

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def list_application_versions(ApplicationId=None, MaxItems=None, NextToken=None):
    """
    Lists versions for the specified application.
    See also: AWS API Documentation
    
    
    :example: response = client.list_application_versions(
        ApplicationId='string',
        MaxItems=123,
        NextToken='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The ID of the application to get.
            

    :type MaxItems: integer
    :param MaxItems: The total number of items to return.

    :type NextToken: string
    :param NextToken: A token to specify where to start paginating.

    :rtype: dict
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
    
    
    """
    pass

def list_applications(MaxItems=None, NextToken=None):
    """
    Lists applications owned by the requester.
    See also: AWS API Documentation
    
    
    :example: response = client.list_applications(
        MaxItems=123,
        NextToken='string'
    )
    
    
    :type MaxItems: integer
    :param MaxItems: The total number of items to return.

    :type NextToken: string
    :param NextToken: A token to specify where to start paginating.

    :rtype: dict
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
    Puts the policy for the specified application.
    See also: AWS API Documentation
    
    
    :example: response = client.put_application_policy(
        ApplicationId='string',
        Statements=[
            {
                'Actions': [
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
    :param ApplicationId: [REQUIRED]
            The ID of the application to get.
            

    :type Statements: list
    :param Statements: Array of policy statements applied to the application.
            (dict) --Policy statement applied to the application.
            Actions (list) -- [REQUIRED]A list of supported actions:
            GetApplication
            CreateCloudFormationChangeSet
            ListApplicationVersions
            SearchApplications
            Deploy (Note: This action enables all other actions above.)
            (string) --
            Principals (list) -- [REQUIRED]An AWS account ID, or * to make the application public.
            (string) --
            StatementId (string) --A unique ID for the statement.
            
            

    :rtype: dict
    :return: {
        'Statements': [
            {
                'Actions': [
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

def update_application(ApplicationId=None, Author=None, Description=None, HomePageUrl=None, Labels=None, ReadmeBody=None, ReadmeUrl=None):
    """
    Updates the specified application.
    See also: AWS API Documentation
    
    
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
    :param ApplicationId: [REQUIRED]
            The ID of the application to get.
            

    :type Author: string
    :param Author: The name of the author publishing the app.
            Min Length=1. Max Length=127.
            Pattern '^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$';
            

    :type Description: string
    :param Description: The description of the application.
            Min Length=1. Max Length=256
            

    :type HomePageUrl: string
    :param HomePageUrl: A URL with more information about the application, for example the location of your GitHub repository for the application.

    :type Labels: list
    :param Labels: Labels to improve discovery of apps in search results.
            Min Length=1. Max Length=127. Maximum number of labels: 10
            Pattern: '^[a-zA-Z0-9+\-_:\/@]+$';
            (string) --
            

    :type ReadmeBody: string
    :param ReadmeBody: A raw text Readme file that contains a more detailed description of the application and how it works in markdown language.
            Max size 5 MB
            

    :type ReadmeUrl: string
    :param ReadmeUrl: A link to the Readme file that contains a more detailed description of the application and how it works in markdown language.
            Max size 5 MB
            

    :rtype: dict
    :return: {
        'ApplicationId': 'string',
        'Author': 'string',
        'CreationTime': 'string',
        'Description': 'string',
        'HomePageUrl': 'string',
        'Labels': [
            'string',
        ],
        'LicenseUrl': 'string',
        'Name': 'string',
        'ReadmeUrl': 'string',
        'SpdxLicenseId': 'string',
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
            'SemanticVersion': 'string',
            'SourceCodeUrl': 'string',
            'TemplateUrl': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

