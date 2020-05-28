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

def acknowledge_job(jobId=None, nonce=None):
    """
    Returns information about a specified job and whether that job has been received by the job worker. Used for custom actions only.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.acknowledge_job(
        jobId='string',
        nonce='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique system-generated ID of the job for which you want to confirm receipt.\n

    :type nonce: string
    :param nonce: [REQUIRED]\nA system-generated random number that AWS CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response of the PollForJobs request that returned this job.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'status': 'Created'|'Queued'|'Dispatched'|'InProgress'|'TimedOut'|'Succeeded'|'Failed'
}


Response Structure

(dict) --
Represents the output of an AcknowledgeJob action.

status (string) --
Whether the job worker has received the specified job.







Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.InvalidNonceException
CodePipeline.Client.exceptions.JobNotFoundException


    :return: {
        'status': 'Created'|'Queued'|'Dispatched'|'InProgress'|'TimedOut'|'Succeeded'|'Failed'
    }
    
    
    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.InvalidNonceException
    CodePipeline.Client.exceptions.JobNotFoundException
    
    """
    pass

def acknowledge_third_party_job(jobId=None, nonce=None, clientToken=None):
    """
    Confirms a job worker has received the specified job. Used for partner actions only.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.acknowledge_third_party_job(
        jobId='string',
        nonce='string',
        clientToken='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique system-generated ID of the job.\n

    :type nonce: string
    :param nonce: [REQUIRED]\nA system-generated random number that AWS CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response to a GetThirdPartyJobDetails request.\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'status': 'Created'|'Queued'|'Dispatched'|'InProgress'|'TimedOut'|'Succeeded'|'Failed'
}


Response Structure

(dict) --
Represents the output of an AcknowledgeThirdPartyJob action.

status (string) --
The status information for the third party job, if any.







Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.InvalidNonceException
CodePipeline.Client.exceptions.JobNotFoundException
CodePipeline.Client.exceptions.InvalidClientTokenException


    :return: {
        'status': 'Created'|'Queued'|'Dispatched'|'InProgress'|'TimedOut'|'Succeeded'|'Failed'
    }
    
    
    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.InvalidNonceException
    CodePipeline.Client.exceptions.JobNotFoundException
    CodePipeline.Client.exceptions.InvalidClientTokenException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_custom_action_type(category=None, provider=None, version=None, settings=None, configurationProperties=None, inputArtifactDetails=None, outputArtifactDetails=None, tags=None):
    """
    Creates a new custom action that can be used in all pipelines associated with the AWS account. Only used for custom actions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_custom_action_type(
        category='Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
        provider='string',
        version='string',
        settings={
            'thirdPartyConfigurationUrl': 'string',
            'entityUrlTemplate': 'string',
            'executionUrlTemplate': 'string',
            'revisionUrlTemplate': 'string'
        },
        configurationProperties=[
            {
                'name': 'string',
                'required': True|False,
                'key': True|False,
                'secret': True|False,
                'queryable': True|False,
                'description': 'string',
                'type': 'String'|'Number'|'Boolean'
            },
        ],
        inputArtifactDetails={
            'minimumCount': 123,
            'maximumCount': 123
        },
        outputArtifactDetails={
            'minimumCount': 123,
            'maximumCount': 123
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type category: string
    :param category: [REQUIRED]\nThe category of the custom action, such as a build action or a test action.\n\nNote\nAlthough Source and Approval are listed as valid values, they are not currently functional. These values are reserved for future use.\n\n

    :type provider: string
    :param provider: [REQUIRED]\nThe provider of the service used in the custom action, such as AWS CodeDeploy.\n

    :type version: string
    :param version: [REQUIRED]\nThe version identifier of the custom action.\n

    :type settings: dict
    :param settings: URLs that provide users information about this custom action.\n\nthirdPartyConfigurationUrl (string) --The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.\n\nentityUrlTemplate (string) --The URL returned to the AWS CodePipeline console that provides a deep link to the resources of the external system, such as the configuration page for an AWS CodeDeploy deployment group. This link is provided as part of the action display in the pipeline.\n\nexecutionUrlTemplate (string) --The URL returned to the AWS CodePipeline console that contains a link to the top-level landing page for the external system, such as the console page for AWS CodeDeploy. This link is shown on the pipeline view page in the AWS CodePipeline console and provides a link to the execution entity of the external action.\n\nrevisionUrlTemplate (string) --The URL returned to the AWS CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.\n\n\n

    :type configurationProperties: list
    :param configurationProperties: The configuration properties for the custom action.\n\nNote\nYou can refer to a name in the configuration properties of the custom action within the URL templates by following the format of {Config:name}, as long as the configuration property is both required and not secret. For more information, see Create a Custom Action for a Pipeline .\n\n\n(dict) --Represents information about an action configuration property.\n\nname (string) -- [REQUIRED]The name of the action configuration property.\n\nrequired (boolean) -- [REQUIRED]Whether the configuration property is a required value.\n\nkey (boolean) -- [REQUIRED]Whether the configuration property is a key.\n\nsecret (boolean) -- [REQUIRED]Whether the configuration property is secret. Secrets are hidden from all calls except for GetJobDetails , GetThirdPartyJobDetails , PollForJobs , and PollForThirdPartyJobs .\nWhen updating a pipeline, passing * * * * * without changing any other values of the action preserves the previous value of the secret.\n\nqueryable (boolean) --Indicates that the property is used with PollForJobs . When creating a custom action, an action can have up to one queryable property. If it has one, that property must be both required and not secret.\nIf you create a pipeline with a custom action type, and that custom action contains a queryable property, the value for that configuration property is subject to other restrictions. The value must be less than or equal to twenty (20) characters. The value can contain only alphanumeric characters, underscores, and hyphens.\n\ndescription (string) --The description of the action configuration property that is displayed to users.\n\ntype (string) --The type of the configuration property.\n\n\n\n\n

    :type inputArtifactDetails: dict
    :param inputArtifactDetails: [REQUIRED]\nThe details of the input artifact for the action, such as its commit ID.\n\nminimumCount (integer) -- [REQUIRED]The minimum number of artifacts allowed for the action type.\n\nmaximumCount (integer) -- [REQUIRED]The maximum number of artifacts allowed for the action type.\n\n\n

    :type outputArtifactDetails: dict
    :param outputArtifactDetails: [REQUIRED]\nThe details of the output artifact of the action, such as its commit ID.\n\nminimumCount (integer) -- [REQUIRED]The minimum number of artifacts allowed for the action type.\n\nmaximumCount (integer) -- [REQUIRED]The maximum number of artifacts allowed for the action type.\n\n\n

    :type tags: list
    :param tags: The tags for the custom action.\n\n(dict) --A tag is a key-value pair that is used to manage the resource.\n\nkey (string) -- [REQUIRED]The tag\'s key.\n\nvalue (string) -- [REQUIRED]The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'actionType': {
        'id': {
            'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
            'owner': 'AWS'|'ThirdParty'|'Custom',
            'provider': 'string',
            'version': 'string'
        },
        'settings': {
            'thirdPartyConfigurationUrl': 'string',
            'entityUrlTemplate': 'string',
            'executionUrlTemplate': 'string',
            'revisionUrlTemplate': 'string'
        },
        'actionConfigurationProperties': [
            {
                'name': 'string',
                'required': True|False,
                'key': True|False,
                'secret': True|False,
                'queryable': True|False,
                'description': 'string',
                'type': 'String'|'Number'|'Boolean'
            },
        ],
        'inputArtifactDetails': {
            'minimumCount': 123,
            'maximumCount': 123
        },
        'outputArtifactDetails': {
            'minimumCount': 123,
            'maximumCount': 123
        }
    },
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a CreateCustomActionType operation.

actionType (dict) --
Returns information about the details of an action type.

id (dict) --
Represents information about an action type.

category (string) --
A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.

owner (string) --
The creator of the action being called.

provider (string) --
The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see Valid Action Types and Providers in CodePipeline .

version (string) --
A string that describes the action version.



settings (dict) --
The settings for the action type.

thirdPartyConfigurationUrl (string) --
The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.

entityUrlTemplate (string) --
The URL returned to the AWS CodePipeline console that provides a deep link to the resources of the external system, such as the configuration page for an AWS CodeDeploy deployment group. This link is provided as part of the action display in the pipeline.

executionUrlTemplate (string) --
The URL returned to the AWS CodePipeline console that contains a link to the top-level landing page for the external system, such as the console page for AWS CodeDeploy. This link is shown on the pipeline view page in the AWS CodePipeline console and provides a link to the execution entity of the external action.

revisionUrlTemplate (string) --
The URL returned to the AWS CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.



actionConfigurationProperties (list) --
The configuration properties for the action type.

(dict) --
Represents information about an action configuration property.

name (string) --
The name of the action configuration property.

required (boolean) --
Whether the configuration property is a required value.

key (boolean) --
Whether the configuration property is a key.

secret (boolean) --
Whether the configuration property is secret. Secrets are hidden from all calls except for GetJobDetails , GetThirdPartyJobDetails , PollForJobs , and PollForThirdPartyJobs .
When updating a pipeline, passing * * * * * without changing any other values of the action preserves the previous value of the secret.

queryable (boolean) --
Indicates that the property is used with PollForJobs . When creating a custom action, an action can have up to one queryable property. If it has one, that property must be both required and not secret.
If you create a pipeline with a custom action type, and that custom action contains a queryable property, the value for that configuration property is subject to other restrictions. The value must be less than or equal to twenty (20) characters. The value can contain only alphanumeric characters, underscores, and hyphens.

description (string) --
The description of the action configuration property that is displayed to users.

type (string) --
The type of the configuration property.





inputArtifactDetails (dict) --
The details of the input artifact for the action, such as its commit ID.

minimumCount (integer) --
The minimum number of artifacts allowed for the action type.

maximumCount (integer) --
The maximum number of artifacts allowed for the action type.



outputArtifactDetails (dict) --
The details of the output artifact of the action, such as its commit ID.

minimumCount (integer) --
The minimum number of artifacts allowed for the action type.

maximumCount (integer) --
The maximum number of artifacts allowed for the action type.





tags (list) --
Specifies the tags applied to the custom action.

(dict) --
A tag is a key-value pair that is used to manage the resource.

key (string) --
The tag\'s key.

value (string) --
The tag\'s value.











Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.LimitExceededException
CodePipeline.Client.exceptions.TooManyTagsException
CodePipeline.Client.exceptions.InvalidTagsException
CodePipeline.Client.exceptions.ConcurrentModificationException


    :return: {
        'actionType': {
            'id': {
                'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                'owner': 'AWS'|'ThirdParty'|'Custom',
                'provider': 'string',
                'version': 'string'
            },
            'settings': {
                'thirdPartyConfigurationUrl': 'string',
                'entityUrlTemplate': 'string',
                'executionUrlTemplate': 'string',
                'revisionUrlTemplate': 'string'
            },
            'actionConfigurationProperties': [
                {
                    'name': 'string',
                    'required': True|False,
                    'key': True|False,
                    'secret': True|False,
                    'queryable': True|False,
                    'description': 'string',
                    'type': 'String'|'Number'|'Boolean'
                },
            ],
            'inputArtifactDetails': {
                'minimumCount': 123,
                'maximumCount': 123
            },
            'outputArtifactDetails': {
                'minimumCount': 123,
                'maximumCount': 123
            }
        },
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.LimitExceededException
    CodePipeline.Client.exceptions.TooManyTagsException
    CodePipeline.Client.exceptions.InvalidTagsException
    CodePipeline.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def create_pipeline(pipeline=None, tags=None):
    """
    Creates a pipeline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_pipeline(
        pipeline={
            'name': 'string',
            'roleArn': 'string',
            'artifactStore': {
                'type': 'S3',
                'location': 'string',
                'encryptionKey': {
                    'id': 'string',
                    'type': 'KMS'
                }
            },
            'artifactStores': {
                'string': {
                    'type': 'S3',
                    'location': 'string',
                    'encryptionKey': {
                        'id': 'string',
                        'type': 'KMS'
                    }
                }
            },
            'stages': [
                {
                    'name': 'string',
                    'blockers': [
                        {
                            'name': 'string',
                            'type': 'Schedule'
                        },
                    ],
                    'actions': [
                        {
                            'name': 'string',
                            'actionTypeId': {
                                'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                                'owner': 'AWS'|'ThirdParty'|'Custom',
                                'provider': 'string',
                                'version': 'string'
                            },
                            'runOrder': 123,
                            'configuration': {
                                'string': 'string'
                            },
                            'outputArtifacts': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'inputArtifacts': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'roleArn': 'string',
                            'region': 'string',
                            'namespace': 'string'
                        },
                    ]
                },
            ],
            'version': 123
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type pipeline: dict
    :param pipeline: [REQUIRED]\nRepresents the structure of actions and stages to be performed in the pipeline.\n\nname (string) -- [REQUIRED]The name of the action to be performed.\n\nroleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no actionRoleArn , or to use to assume roles for actions with an actionRoleArn .\n\nartifactStore (dict) --Represents information about the S3 bucket where artifacts are stored for the pipeline.\n\nNote\nYou must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .\n\n\ntype (string) -- [REQUIRED]The type of the artifact store, such as S3.\n\nlocation (string) -- [REQUIRED]The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.\n\nencryptionKey (dict) --The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.\n\nid (string) -- [REQUIRED]The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN, or the alias ARN.\n\nNote\nAliases are recognized only in the account that created the customer master key (CMK). For cross-account actions, you can only use the key ID or key ARN to identify the key.\n\n\ntype (string) -- [REQUIRED]The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.\n\n\n\n\n\nartifactStores (dict) --A mapping of artifactStore objects and their corresponding AWS Regions. There must be an artifact store for the pipeline Region and for each cross-region action in the pipeline.\n\nNote\nYou must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .\n\n\n(string) --\n(dict) --The S3 bucket where artifacts for the pipeline are stored.\n\nNote\nYou must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .\n\n\ntype (string) -- [REQUIRED]The type of the artifact store, such as S3.\n\nlocation (string) -- [REQUIRED]The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.\n\nencryptionKey (dict) --The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.\n\nid (string) -- [REQUIRED]The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN, or the alias ARN.\n\nNote\nAliases are recognized only in the account that created the customer master key (CMK). For cross-account actions, you can only use the key ID or key ARN to identify the key.\n\n\ntype (string) -- [REQUIRED]The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.\n\n\n\n\n\n\n\n\n\nstages (list) -- [REQUIRED]The stage in which to perform the action.\n\n(dict) --Represents information about a stage and its definition.\n\nname (string) -- [REQUIRED]The name of the stage.\n\nblockers (list) --Reserved for future use.\n\n(dict) --Reserved for future use.\n\nname (string) -- [REQUIRED]Reserved for future use.\n\ntype (string) -- [REQUIRED]Reserved for future use.\n\n\n\n\n\nactions (list) -- [REQUIRED]The actions included in a stage.\n\n(dict) --Represents information about an action declaration.\n\nname (string) -- [REQUIRED]The action declaration\'s name.\n\nactionTypeId (dict) -- [REQUIRED]Specifies the action type and the provider of the action.\n\ncategory (string) -- [REQUIRED]A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.\n\nowner (string) -- [REQUIRED]The creator of the action being called.\n\nprovider (string) -- [REQUIRED]The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see Valid Action Types and Providers in CodePipeline .\n\nversion (string) -- [REQUIRED]A string that describes the action version.\n\n\n\nrunOrder (integer) --The order in which actions are run.\n\nconfiguration (dict) --The action\'s configuration. These are key-value pairs that specify input values for an action. For more information, see Action Structure Requirements in CodePipeline . For the list of configuration properties for the AWS CloudFormation action type in CodePipeline, see Configuration Properties Reference in the AWS CloudFormation User Guide . For template snippets with examples, see Using Parameter Override Functions with CodePipeline Pipelines in the AWS CloudFormation User Guide .\nThe values can be represented in either JSON or YAML format. For example, the JSON configuration item format is as follows:\n\nJSON:'Configuration' : { Key : Value },\n\n\n(string) --\n(string) --\n\n\n\n\noutputArtifacts (list) --The name or ID of the result of the action declaration, such as a test or build artifact.\n\n(dict) --Represents information about the output of an action.\n\nname (string) -- [REQUIRED]The name of the output of an artifact, such as 'My App'.\nThe input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.\nOutput artifact names must be unique within a pipeline.\n\n\n\n\n\ninputArtifacts (list) --The name or ID of the artifact consumed by the action, such as a test or build artifact.\n\n(dict) --Represents information about an artifact to be worked on, such as a test or build artifact.\n\nname (string) -- [REQUIRED]The name of the artifact to be worked on (for example, 'My App').\nThe input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.\n\n\n\n\n\nroleArn (string) --The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline.\n\nregion (string) --The action declaration\'s AWS Region, such as us-east-1.\n\nnamespace (string) --The variable namespace associated with the action. All variables produced as output by this action fall under this namespace.\n\n\n\n\n\n\n\n\n\nversion (integer) --The version number of the pipeline. A new pipeline always has a version number of 1. This number is incremented when a pipeline is updated.\n\n\n

    :type tags: list
    :param tags: The tags for the pipeline.\n\n(dict) --A tag is a key-value pair that is used to manage the resource.\n\nkey (string) -- [REQUIRED]The tag\'s key.\n\nvalue (string) -- [REQUIRED]The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'pipeline': {
        'name': 'string',
        'roleArn': 'string',
        'artifactStore': {
            'type': 'S3',
            'location': 'string',
            'encryptionKey': {
                'id': 'string',
                'type': 'KMS'
            }
        },
        'artifactStores': {
            'string': {
                'type': 'S3',
                'location': 'string',
                'encryptionKey': {
                    'id': 'string',
                    'type': 'KMS'
                }
            }
        },
        'stages': [
            {
                'name': 'string',
                'blockers': [
                    {
                        'name': 'string',
                        'type': 'Schedule'
                    },
                ],
                'actions': [
                    {
                        'name': 'string',
                        'actionTypeId': {
                            'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                            'owner': 'AWS'|'ThirdParty'|'Custom',
                            'provider': 'string',
                            'version': 'string'
                        },
                        'runOrder': 123,
                        'configuration': {
                            'string': 'string'
                        },
                        'outputArtifacts': [
                            {
                                'name': 'string'
                            },
                        ],
                        'inputArtifacts': [
                            {
                                'name': 'string'
                            },
                        ],
                        'roleArn': 'string',
                        'region': 'string',
                        'namespace': 'string'
                    },
                ]
            },
        ],
        'version': 123
    },
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a CreatePipeline action.

pipeline (dict) --
Represents the structure of actions and stages to be performed in the pipeline.

name (string) --
The name of the action to be performed.

roleArn (string) --
The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no actionRoleArn , or to use to assume roles for actions with an actionRoleArn .

artifactStore (dict) --
Represents information about the S3 bucket where artifacts are stored for the pipeline.

Note
You must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .


type (string) --
The type of the artifact store, such as S3.

location (string) --
The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

encryptionKey (dict) --
The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.

id (string) --
The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN, or the alias ARN.

Note
Aliases are recognized only in the account that created the customer master key (CMK). For cross-account actions, you can only use the key ID or key ARN to identify the key.


type (string) --
The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.





artifactStores (dict) --
A mapping of artifactStore objects and their corresponding AWS Regions. There must be an artifact store for the pipeline Region and for each cross-region action in the pipeline.

Note
You must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .


(string) --

(dict) --
The S3 bucket where artifacts for the pipeline are stored.

Note
You must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .


type (string) --
The type of the artifact store, such as S3.

location (string) --
The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

encryptionKey (dict) --
The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.

id (string) --
The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN, or the alias ARN.

Note
Aliases are recognized only in the account that created the customer master key (CMK). For cross-account actions, you can only use the key ID or key ARN to identify the key.


type (string) --
The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.









stages (list) --
The stage in which to perform the action.

(dict) --
Represents information about a stage and its definition.

name (string) --
The name of the stage.

blockers (list) --
Reserved for future use.

(dict) --
Reserved for future use.

name (string) --
Reserved for future use.

type (string) --
Reserved for future use.





actions (list) --
The actions included in a stage.

(dict) --
Represents information about an action declaration.

name (string) --
The action declaration\'s name.

actionTypeId (dict) --
Specifies the action type and the provider of the action.

category (string) --
A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.

owner (string) --
The creator of the action being called.

provider (string) --
The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see Valid Action Types and Providers in CodePipeline .

version (string) --
A string that describes the action version.



runOrder (integer) --
The order in which actions are run.

configuration (dict) --
The action\'s configuration. These are key-value pairs that specify input values for an action. For more information, see Action Structure Requirements in CodePipeline . For the list of configuration properties for the AWS CloudFormation action type in CodePipeline, see Configuration Properties Reference in the AWS CloudFormation User Guide . For template snippets with examples, see Using Parameter Override Functions with CodePipeline Pipelines in the AWS CloudFormation User Guide .
The values can be represented in either JSON or YAML format. For example, the JSON configuration item format is as follows:

JSON:
"Configuration" : { Key : Value },


(string) --
(string) --




outputArtifacts (list) --
The name or ID of the result of the action declaration, such as a test or build artifact.

(dict) --
Represents information about the output of an action.

name (string) --
The name of the output of an artifact, such as "My App".
The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
Output artifact names must be unique within a pipeline.





inputArtifacts (list) --
The name or ID of the artifact consumed by the action, such as a test or build artifact.

(dict) --
Represents information about an artifact to be worked on, such as a test or build artifact.

name (string) --
The name of the artifact to be worked on (for example, "My App").
The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.





roleArn (string) --
The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline.

region (string) --
The action declaration\'s AWS Region, such as us-east-1.

namespace (string) --
The variable namespace associated with the action. All variables produced as output by this action fall under this namespace.









version (integer) --
The version number of the pipeline. A new pipeline always has a version number of 1. This number is incremented when a pipeline is updated.



tags (list) --
Specifies the tags applied to the pipeline.

(dict) --
A tag is a key-value pair that is used to manage the resource.

key (string) --
The tag\'s key.

value (string) --
The tag\'s value.











Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.PipelineNameInUseException
CodePipeline.Client.exceptions.InvalidStageDeclarationException
CodePipeline.Client.exceptions.InvalidActionDeclarationException
CodePipeline.Client.exceptions.InvalidBlockerDeclarationException
CodePipeline.Client.exceptions.InvalidStructureException
CodePipeline.Client.exceptions.LimitExceededException
CodePipeline.Client.exceptions.TooManyTagsException
CodePipeline.Client.exceptions.InvalidTagsException
CodePipeline.Client.exceptions.ConcurrentModificationException


    :return: {
        'pipeline': {
            'name': 'string',
            'roleArn': 'string',
            'artifactStore': {
                'type': 'S3',
                'location': 'string',
                'encryptionKey': {
                    'id': 'string',
                    'type': 'KMS'
                }
            },
            'artifactStores': {
                'string': {
                    'type': 'S3',
                    'location': 'string',
                    'encryptionKey': {
                        'id': 'string',
                        'type': 'KMS'
                    }
                }
            },
            'stages': [
                {
                    'name': 'string',
                    'blockers': [
                        {
                            'name': 'string',
                            'type': 'Schedule'
                        },
                    ],
                    'actions': [
                        {
                            'name': 'string',
                            'actionTypeId': {
                                'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                                'owner': 'AWS'|'ThirdParty'|'Custom',
                                'provider': 'string',
                                'version': 'string'
                            },
                            'runOrder': 123,
                            'configuration': {
                                'string': 'string'
                            },
                            'outputArtifacts': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'inputArtifacts': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'roleArn': 'string',
                            'region': 'string',
                            'namespace': 'string'
                        },
                    ]
                },
            ],
            'version': 123
        },
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def delete_custom_action_type(category=None, provider=None, version=None):
    """
    Marks a custom action as deleted. PollForJobs for the custom action fails after the action is marked for deletion. Used for custom actions only.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_custom_action_type(
        category='Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
        provider='string',
        version='string'
    )
    
    
    :type category: string
    :param category: [REQUIRED]\nThe category of the custom action that you want to delete, such as source or deploy.\n

    :type provider: string
    :param provider: [REQUIRED]\nThe provider of the service used in the custom action, such as AWS CodeDeploy.\n

    :type version: string
    :param version: [REQUIRED]\nThe version of the custom action to delete.\n

    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def delete_pipeline(name=None):
    """
    Deletes the specified pipeline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_pipeline(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the pipeline to be deleted.\n

    """
    pass

def delete_webhook(name=None):
    """
    Deletes a previously created webhook by name. Deleting the webhook stops AWS CodePipeline from starting a pipeline every time an external event occurs. The API returns successfully when trying to delete a webhook that is already deleted. If a deleted webhook is re-created by calling PutWebhook with the same name, it will have a different URL.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_webhook(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the webhook you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def deregister_webhook_with_third_party(webhookName=None):
    """
    Removes the connection between the webhook that was created by CodePipeline and the external tool with events to be detected. Currently supported only for webhooks that target an action type of GitHub.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_webhook_with_third_party(
        webhookName='string'
    )
    
    
    :type webhookName: string
    :param webhookName: The name of the webhook you want to deregister.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.WebhookNotFoundException


    :return: {}
    
    
    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.WebhookNotFoundException
    
    """
    pass

def disable_stage_transition(pipelineName=None, stageName=None, transitionType=None, reason=None):
    """
    Prevents artifacts in a pipeline from transitioning to the next stage in the pipeline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_stage_transition(
        pipelineName='string',
        stageName='string',
        transitionType='Inbound'|'Outbound',
        reason='string'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]\nThe name of the pipeline in which you want to disable the flow of artifacts from one stage to another.\n

    :type stageName: string
    :param stageName: [REQUIRED]\nThe name of the stage where you want to disable the inbound or outbound transition of artifacts.\n

    :type transitionType: string
    :param transitionType: [REQUIRED]\nSpecifies whether artifacts are prevented from transitioning into the stage and being processed by the actions in that stage (inbound), or prevented from transitioning from the stage after they have been processed by the actions in that stage (outbound).\n

    :type reason: string
    :param reason: [REQUIRED]\nThe reason given to the user that a stage is disabled, such as waiting for manual approval or manual tests. This message is displayed in the pipeline console UI.\n

    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.PipelineNotFoundException
    CodePipeline.Client.exceptions.StageNotFoundException
    
    """
    pass

def enable_stage_transition(pipelineName=None, stageName=None, transitionType=None):
    """
    Enables artifacts in a pipeline to transition to a stage in a pipeline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_stage_transition(
        pipelineName='string',
        stageName='string',
        transitionType='Inbound'|'Outbound'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]\nThe name of the pipeline in which you want to enable the flow of artifacts from one stage to another.\n

    :type stageName: string
    :param stageName: [REQUIRED]\nThe name of the stage where you want to enable the transition of artifacts, either into the stage (inbound) or from that stage to the next stage (outbound).\n

    :type transitionType: string
    :param transitionType: [REQUIRED]\nSpecifies whether artifacts are allowed to enter the stage and be processed by the actions in that stage (inbound) or whether already processed artifacts are allowed to transition to the next stage (outbound).\n

    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.PipelineNotFoundException
    CodePipeline.Client.exceptions.StageNotFoundException
    
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

def get_job_details(jobId=None):
    """
    Returns information about a job. Used for custom actions only.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_job_details(
        jobId='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique system-generated ID for the job.\n

    :rtype: dict
ReturnsResponse Syntax{
    'jobDetails': {
        'id': 'string',
        'data': {
            'actionTypeId': {
                'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                'owner': 'AWS'|'ThirdParty'|'Custom',
                'provider': 'string',
                'version': 'string'
            },
            'actionConfiguration': {
                'configuration': {
                    'string': 'string'
                }
            },
            'pipelineContext': {
                'pipelineName': 'string',
                'stage': {
                    'name': 'string'
                },
                'action': {
                    'name': 'string',
                    'actionExecutionId': 'string'
                },
                'pipelineArn': 'string',
                'pipelineExecutionId': 'string'
            },
            'inputArtifacts': [
                {
                    'name': 'string',
                    'revision': 'string',
                    'location': {
                        'type': 'S3',
                        's3Location': {
                            'bucketName': 'string',
                            'objectKey': 'string'
                        }
                    }
                },
            ],
            'outputArtifacts': [
                {
                    'name': 'string',
                    'revision': 'string',
                    'location': {
                        'type': 'S3',
                        's3Location': {
                            'bucketName': 'string',
                            'objectKey': 'string'
                        }
                    }
                },
            ],
            'artifactCredentials': {
                'accessKeyId': 'string',
                'secretAccessKey': 'string',
                'sessionToken': 'string'
            },
            'continuationToken': 'string',
            'encryptionKey': {
                'id': 'string',
                'type': 'KMS'
            }
        },
        'accountId': 'string'
    }
}


Response Structure

(dict) --Represents the output of a GetJobDetails action.

jobDetails (dict) --The details of the job.

Note
If AWSSessionCredentials is used, a long-running job can call GetJobDetails again to obtain new credentials.


id (string) --The unique system-generated ID of the job.

data (dict) --Represents other information about a job required for a job worker to complete the job.

actionTypeId (dict) --Represents information about an action type.

category (string) --A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.

owner (string) --The creator of the action being called.

provider (string) --The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see Valid Action Types and Providers in CodePipeline .

version (string) --A string that describes the action version.



actionConfiguration (dict) --Represents information about an action configuration.

configuration (dict) --The configuration data for the action.

(string) --
(string) --






pipelineContext (dict) --Represents information about a pipeline to a job worker.

Note
Includes pipelineArn and pipelineExecutionId for custom jobs.


pipelineName (string) --The name of the pipeline. This is a user-specified value. Pipeline names must be unique across all pipeline names under an Amazon Web Services account.

stage (dict) --The stage of the pipeline.

name (string) --The name of the stage.



action (dict) --The context of an action to a job worker in the stage of a pipeline.

name (string) --The name of the action in the context of a job.

actionExecutionId (string) --The system-generated unique ID that corresponds to an action\'s execution.



pipelineArn (string) --The Amazon Resource Name (ARN) of the pipeline.

pipelineExecutionId (string) --The execution ID of the pipeline.



inputArtifacts (list) --The artifact supplied to the job.

(dict) --Represents information about an artifact that is worked on by actions in the pipeline.

name (string) --The artifact\'s name.

revision (string) --The artifact\'s revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).

location (dict) --The location of an artifact.

type (string) --The type of artifact in the location.

s3Location (dict) --The S3 bucket that contains the artifact.

bucketName (string) --The name of the S3 bucket.

objectKey (string) --The key of the object in the S3 bucket, which uniquely identifies the object in the bucket.









outputArtifacts (list) --The output of the job.

(dict) --Represents information about an artifact that is worked on by actions in the pipeline.

name (string) --The artifact\'s name.

revision (string) --The artifact\'s revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).

location (dict) --The location of an artifact.

type (string) --The type of artifact in the location.

s3Location (dict) --The S3 bucket that contains the artifact.

bucketName (string) --The name of the S3 bucket.

objectKey (string) --The key of the object in the S3 bucket, which uniquely identifies the object in the bucket.









artifactCredentials (dict) --Represents an AWS session credentials object. These credentials are temporary credentials that are issued by AWS Secure Token Service (STS). They can be used to access input and output artifacts in the S3 bucket used to store artifacts for the pipeline in AWS CodePipeline.

accessKeyId (string) --The access key for the session.

secretAccessKey (string) --The secret access key for the session.

sessionToken (string) --The token for the session.



continuationToken (string) --A system-generated token, such as a AWS CodeDeploy deployment ID, required by a job to continue the job asynchronously.

encryptionKey (dict) --Represents information about the key used to encrypt data in the artifact store, such as an AWS Key Management Service (AWS KMS) key.

id (string) --The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN, or the alias ARN.

Note
Aliases are recognized only in the account that created the customer master key (CMK). For cross-account actions, you can only use the key ID or key ARN to identify the key.


type (string) --The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.





accountId (string) --The AWS account ID associated with the job.








Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.JobNotFoundException


    :return: {
        'jobDetails': {
            'id': 'string',
            'data': {
                'actionTypeId': {
                    'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                    'owner': 'AWS'|'ThirdParty'|'Custom',
                    'provider': 'string',
                    'version': 'string'
                },
                'actionConfiguration': {
                    'configuration': {
                        'string': 'string'
                    }
                },
                'pipelineContext': {
                    'pipelineName': 'string',
                    'stage': {
                        'name': 'string'
                    },
                    'action': {
                        'name': 'string',
                        'actionExecutionId': 'string'
                    },
                    'pipelineArn': 'string',
                    'pipelineExecutionId': 'string'
                },
                'inputArtifacts': [
                    {
                        'name': 'string',
                        'revision': 'string',
                        'location': {
                            'type': 'S3',
                            's3Location': {
                                'bucketName': 'string',
                                'objectKey': 'string'
                            }
                        }
                    },
                ],
                'outputArtifacts': [
                    {
                        'name': 'string',
                        'revision': 'string',
                        'location': {
                            'type': 'S3',
                            's3Location': {
                                'bucketName': 'string',
                                'objectKey': 'string'
                            }
                        }
                    },
                ],
                'artifactCredentials': {
                    'accessKeyId': 'string',
                    'secretAccessKey': 'string',
                    'sessionToken': 'string'
                },
                'continuationToken': 'string',
                'encryptionKey': {
                    'id': 'string',
                    'type': 'KMS'
                }
            },
            'accountId': 'string'
        }
    }
    
    
    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.JobNotFoundException
    
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

def get_pipeline(name=None, version=None):
    """
    Returns the metadata, structure, stages, and actions of a pipeline. Can be used to return the entire structure of a pipeline in JSON format, which can then be modified and used to update the pipeline structure with  UpdatePipeline .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_pipeline(
        name='string',
        version=123
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the pipeline for which you want to get information. Pipeline names must be unique under an AWS user account.\n

    :type version: integer
    :param version: The version number of the pipeline. If you do not specify a version, defaults to the current version.

    :rtype: dict

ReturnsResponse Syntax
{
    'pipeline': {
        'name': 'string',
        'roleArn': 'string',
        'artifactStore': {
            'type': 'S3',
            'location': 'string',
            'encryptionKey': {
                'id': 'string',
                'type': 'KMS'
            }
        },
        'artifactStores': {
            'string': {
                'type': 'S3',
                'location': 'string',
                'encryptionKey': {
                    'id': 'string',
                    'type': 'KMS'
                }
            }
        },
        'stages': [
            {
                'name': 'string',
                'blockers': [
                    {
                        'name': 'string',
                        'type': 'Schedule'
                    },
                ],
                'actions': [
                    {
                        'name': 'string',
                        'actionTypeId': {
                            'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                            'owner': 'AWS'|'ThirdParty'|'Custom',
                            'provider': 'string',
                            'version': 'string'
                        },
                        'runOrder': 123,
                        'configuration': {
                            'string': 'string'
                        },
                        'outputArtifacts': [
                            {
                                'name': 'string'
                            },
                        ],
                        'inputArtifacts': [
                            {
                                'name': 'string'
                            },
                        ],
                        'roleArn': 'string',
                        'region': 'string',
                        'namespace': 'string'
                    },
                ]
            },
        ],
        'version': 123
    },
    'metadata': {
        'pipelineArn': 'string',
        'created': datetime(2015, 1, 1),
        'updated': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Represents the output of a GetPipeline action.

pipeline (dict) --
Represents the structure of actions and stages to be performed in the pipeline.

name (string) --
The name of the action to be performed.

roleArn (string) --
The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no actionRoleArn , or to use to assume roles for actions with an actionRoleArn .

artifactStore (dict) --
Represents information about the S3 bucket where artifacts are stored for the pipeline.

Note
You must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .


type (string) --
The type of the artifact store, such as S3.

location (string) --
The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

encryptionKey (dict) --
The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.

id (string) --
The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN, or the alias ARN.

Note
Aliases are recognized only in the account that created the customer master key (CMK). For cross-account actions, you can only use the key ID or key ARN to identify the key.


type (string) --
The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.





artifactStores (dict) --
A mapping of artifactStore objects and their corresponding AWS Regions. There must be an artifact store for the pipeline Region and for each cross-region action in the pipeline.

Note
You must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .


(string) --

(dict) --
The S3 bucket where artifacts for the pipeline are stored.

Note
You must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .


type (string) --
The type of the artifact store, such as S3.

location (string) --
The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

encryptionKey (dict) --
The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.

id (string) --
The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN, or the alias ARN.

Note
Aliases are recognized only in the account that created the customer master key (CMK). For cross-account actions, you can only use the key ID or key ARN to identify the key.


type (string) --
The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.









stages (list) --
The stage in which to perform the action.

(dict) --
Represents information about a stage and its definition.

name (string) --
The name of the stage.

blockers (list) --
Reserved for future use.

(dict) --
Reserved for future use.

name (string) --
Reserved for future use.

type (string) --
Reserved for future use.





actions (list) --
The actions included in a stage.

(dict) --
Represents information about an action declaration.

name (string) --
The action declaration\'s name.

actionTypeId (dict) --
Specifies the action type and the provider of the action.

category (string) --
A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.

owner (string) --
The creator of the action being called.

provider (string) --
The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see Valid Action Types and Providers in CodePipeline .

version (string) --
A string that describes the action version.



runOrder (integer) --
The order in which actions are run.

configuration (dict) --
The action\'s configuration. These are key-value pairs that specify input values for an action. For more information, see Action Structure Requirements in CodePipeline . For the list of configuration properties for the AWS CloudFormation action type in CodePipeline, see Configuration Properties Reference in the AWS CloudFormation User Guide . For template snippets with examples, see Using Parameter Override Functions with CodePipeline Pipelines in the AWS CloudFormation User Guide .
The values can be represented in either JSON or YAML format. For example, the JSON configuration item format is as follows:

JSON:
"Configuration" : { Key : Value },


(string) --
(string) --




outputArtifacts (list) --
The name or ID of the result of the action declaration, such as a test or build artifact.

(dict) --
Represents information about the output of an action.

name (string) --
The name of the output of an artifact, such as "My App".
The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
Output artifact names must be unique within a pipeline.





inputArtifacts (list) --
The name or ID of the artifact consumed by the action, such as a test or build artifact.

(dict) --
Represents information about an artifact to be worked on, such as a test or build artifact.

name (string) --
The name of the artifact to be worked on (for example, "My App").
The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.





roleArn (string) --
The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline.

region (string) --
The action declaration\'s AWS Region, such as us-east-1.

namespace (string) --
The variable namespace associated with the action. All variables produced as output by this action fall under this namespace.









version (integer) --
The version number of the pipeline. A new pipeline always has a version number of 1. This number is incremented when a pipeline is updated.



metadata (dict) --
Represents the pipeline metadata information returned as part of the output of a GetPipeline action.

pipelineArn (string) --
The Amazon Resource Name (ARN) of the pipeline.

created (datetime) --
The date and time the pipeline was created, in timestamp format.

updated (datetime) --
The date and time the pipeline was last updated, in timestamp format.









Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.PipelineNotFoundException
CodePipeline.Client.exceptions.PipelineVersionNotFoundException


    :return: {
        'pipeline': {
            'name': 'string',
            'roleArn': 'string',
            'artifactStore': {
                'type': 'S3',
                'location': 'string',
                'encryptionKey': {
                    'id': 'string',
                    'type': 'KMS'
                }
            },
            'artifactStores': {
                'string': {
                    'type': 'S3',
                    'location': 'string',
                    'encryptionKey': {
                        'id': 'string',
                        'type': 'KMS'
                    }
                }
            },
            'stages': [
                {
                    'name': 'string',
                    'blockers': [
                        {
                            'name': 'string',
                            'type': 'Schedule'
                        },
                    ],
                    'actions': [
                        {
                            'name': 'string',
                            'actionTypeId': {
                                'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                                'owner': 'AWS'|'ThirdParty'|'Custom',
                                'provider': 'string',
                                'version': 'string'
                            },
                            'runOrder': 123,
                            'configuration': {
                                'string': 'string'
                            },
                            'outputArtifacts': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'inputArtifacts': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'roleArn': 'string',
                            'region': 'string',
                            'namespace': 'string'
                        },
                    ]
                },
            ],
            'version': 123
        },
        'metadata': {
            'pipelineArn': 'string',
            'created': datetime(2015, 1, 1),
            'updated': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_pipeline_execution(pipelineName=None, pipelineExecutionId=None):
    """
    Returns information about an execution of a pipeline, including details about artifacts, the pipeline execution ID, and the name, version, and status of the pipeline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_pipeline_execution(
        pipelineName='string',
        pipelineExecutionId='string'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]\nThe name of the pipeline about which you want to get execution details.\n

    :type pipelineExecutionId: string
    :param pipelineExecutionId: [REQUIRED]\nThe ID of the pipeline execution about which you want to get execution details.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'pipelineExecution': {
        'pipelineName': 'string',
        'pipelineVersion': 123,
        'pipelineExecutionId': 'string',
        'status': 'InProgress'|'Stopped'|'Stopping'|'Succeeded'|'Superseded'|'Failed',
        'artifactRevisions': [
            {
                'name': 'string',
                'revisionId': 'string',
                'revisionChangeIdentifier': 'string',
                'revisionSummary': 'string',
                'created': datetime(2015, 1, 1),
                'revisionUrl': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Represents the output of a GetPipelineExecution action.

pipelineExecution (dict) --
Represents information about the execution of a pipeline.

pipelineName (string) --
The name of the pipeline with the specified pipeline execution.

pipelineVersion (integer) --
The version number of the pipeline with the specified pipeline execution.

pipelineExecutionId (string) --
The ID of the pipeline execution.

status (string) --
The status of the pipeline execution.

InProgress: The pipeline execution is currently running.
Stopped: The pipeline execution was manually stopped. For more information, see Stopped Executions .
Stopping: The pipeline execution received a request to be manually stopped. Depending on the selected stop mode, the execution is either completing or abandoning in-progress actions. For more information, see Stopped Executions .
Succeeded: The pipeline execution was completed successfully.
Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution advanced and continued through the pipeline instead. For more information, see Superseded Executions .
Failed: The pipeline execution was not completed successfully.


artifactRevisions (list) --
A list of ArtifactRevision objects included in a pipeline execution.

(dict) --
Represents revision details of an artifact.

name (string) --
The name of an artifact. This name might be system-generated, such as "MyApp", or defined by the user when an action is created.

revisionId (string) --
The revision ID of the artifact.

revisionChangeIdentifier (string) --
An additional identifier for a revision, such as a commit date or, for artifacts stored in Amazon S3 buckets, the ETag value.

revisionSummary (string) --
Summary information about the most recent revision of the artifact. For GitHub and AWS CodeCommit repositories, the commit message. For Amazon S3 buckets or actions, the user-provided content of a codepipeline-artifact-revision-summary key specified in the object metadata.

created (datetime) --
The date and time when the most recent revision of the artifact was created, in timestamp format.

revisionUrl (string) --
The commit ID for the artifact revision. For artifacts stored in GitHub or AWS CodeCommit repositories, the commit ID is linked to a commit details page.













Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.PipelineNotFoundException
CodePipeline.Client.exceptions.PipelineExecutionNotFoundException


    :return: {
        'pipelineExecution': {
            'pipelineName': 'string',
            'pipelineVersion': 123,
            'pipelineExecutionId': 'string',
            'status': 'InProgress'|'Stopped'|'Stopping'|'Succeeded'|'Superseded'|'Failed',
            'artifactRevisions': [
                {
                    'name': 'string',
                    'revisionId': 'string',
                    'revisionChangeIdentifier': 'string',
                    'revisionSummary': 'string',
                    'created': datetime(2015, 1, 1),
                    'revisionUrl': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    InProgress: The pipeline execution is currently running.
    Stopped: The pipeline execution was manually stopped. For more information, see Stopped Executions .
    Stopping: The pipeline execution received a request to be manually stopped. Depending on the selected stop mode, the execution is either completing or abandoning in-progress actions. For more information, see Stopped Executions .
    Succeeded: The pipeline execution was completed successfully.
    Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution advanced and continued through the pipeline instead. For more information, see Superseded Executions .
    Failed: The pipeline execution was not completed successfully.
    
    """
    pass

def get_pipeline_state(name=None):
    """
    Returns information about the state of a pipeline, including the stages and actions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_pipeline_state(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the pipeline about which you want to get information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'pipelineName': 'string',
    'pipelineVersion': 123,
    'stageStates': [
        {
            'stageName': 'string',
            'inboundTransitionState': {
                'enabled': True|False,
                'lastChangedBy': 'string',
                'lastChangedAt': datetime(2015, 1, 1),
                'disabledReason': 'string'
            },
            'actionStates': [
                {
                    'actionName': 'string',
                    'currentRevision': {
                        'revisionId': 'string',
                        'revisionChangeId': 'string',
                        'created': datetime(2015, 1, 1)
                    },
                    'latestExecution': {
                        'status': 'InProgress'|'Abandoned'|'Succeeded'|'Failed',
                        'summary': 'string',
                        'lastStatusChange': datetime(2015, 1, 1),
                        'token': 'string',
                        'lastUpdatedBy': 'string',
                        'externalExecutionId': 'string',
                        'externalExecutionUrl': 'string',
                        'percentComplete': 123,
                        'errorDetails': {
                            'code': 'string',
                            'message': 'string'
                        }
                    },
                    'entityUrl': 'string',
                    'revisionUrl': 'string'
                },
            ],
            'latestExecution': {
                'pipelineExecutionId': 'string',
                'status': 'InProgress'|'Failed'|'Stopped'|'Stopping'|'Succeeded'
            }
        },
    ],
    'created': datetime(2015, 1, 1),
    'updated': datetime(2015, 1, 1)
}


Response Structure

(dict) --Represents the output of a GetPipelineState action.

pipelineName (string) --The name of the pipeline for which you want to get the state.

pipelineVersion (integer) --The version number of the pipeline.

Note
A newly created pipeline is always assigned a version number of 1 .


stageStates (list) --A list of the pipeline stage output information, including stage name, state, most recent run details, whether the stage is disabled, and other data.

(dict) --Represents information about the state of the stage.

stageName (string) --The name of the stage.

inboundTransitionState (dict) --The state of the inbound transition, which is either enabled or disabled.

enabled (boolean) --Whether the transition between stages is enabled (true) or disabled (false).

lastChangedBy (string) --The ID of the user who last changed the transition state.

lastChangedAt (datetime) --The timestamp when the transition state was last changed.

disabledReason (string) --The user-specified reason why the transition between two stages of a pipeline was disabled.



actionStates (list) --The state of the stage.

(dict) --Represents information about the state of an action.

actionName (string) --The name of the action.

currentRevision (dict) --Represents information about the version (or revision) of an action.

revisionId (string) --The system-generated unique ID that identifies the revision number of the action.

revisionChangeId (string) --The unique identifier of the change that set the state to this revision (for example, a deployment ID or timestamp).

created (datetime) --The date and time when the most recent version of the action was created, in timestamp format.



latestExecution (dict) --Represents information about the run of an action.

status (string) --The status of the action, or for a completed action, the last status of the action.

summary (string) --A summary of the run of the action.

lastStatusChange (datetime) --The last status change of the action.

token (string) --The system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the GetPipelineState command. It is used to validate that the approval request corresponding to this token is still valid.

lastUpdatedBy (string) --The ARN of the user who last changed the pipeline.

externalExecutionId (string) --The external ID of the run of the action.

externalExecutionUrl (string) --The URL of a resource external to AWS that is used when running the action (for example, an external repository URL).

percentComplete (integer) --A percentage of completeness of the action as it runs.

errorDetails (dict) --The details of an error returned by a URL external to AWS.

code (string) --The system ID or number code of the error.

message (string) --The text of the error message.





entityUrl (string) --A URL link for more information about the state of the action, such as a deployment group details page.

revisionUrl (string) --A URL link for more information about the revision, such as a commit details page.





latestExecution (dict) --Information about the latest execution in the stage, including its ID and status.

pipelineExecutionId (string) --The ID of the pipeline execution associated with the stage.

status (string) --The status of the stage, or for a completed stage, the last status of the stage.







created (datetime) --The date and time the pipeline was created, in timestamp format.

updated (datetime) --The date and time the pipeline was last updated, in timestamp format.






Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.PipelineNotFoundException


    :return: {
        'pipelineName': 'string',
        'pipelineVersion': 123,
        'stageStates': [
            {
                'stageName': 'string',
                'inboundTransitionState': {
                    'enabled': True|False,
                    'lastChangedBy': 'string',
                    'lastChangedAt': datetime(2015, 1, 1),
                    'disabledReason': 'string'
                },
                'actionStates': [
                    {
                        'actionName': 'string',
                        'currentRevision': {
                            'revisionId': 'string',
                            'revisionChangeId': 'string',
                            'created': datetime(2015, 1, 1)
                        },
                        'latestExecution': {
                            'status': 'InProgress'|'Abandoned'|'Succeeded'|'Failed',
                            'summary': 'string',
                            'lastStatusChange': datetime(2015, 1, 1),
                            'token': 'string',
                            'lastUpdatedBy': 'string',
                            'externalExecutionId': 'string',
                            'externalExecutionUrl': 'string',
                            'percentComplete': 123,
                            'errorDetails': {
                                'code': 'string',
                                'message': 'string'
                            }
                        },
                        'entityUrl': 'string',
                        'revisionUrl': 'string'
                    },
                ],
                'latestExecution': {
                    'pipelineExecutionId': 'string',
                    'status': 'InProgress'|'Failed'|'Stopped'|'Stopping'|'Succeeded'
                }
            },
        ],
        'created': datetime(2015, 1, 1),
        'updated': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def get_third_party_job_details(jobId=None, clientToken=None):
    """
    Requests the details of a job for a third party action. Used for partner actions only.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_third_party_job_details(
        jobId='string',
        clientToken='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique system-generated ID used for identifying the job.\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'jobDetails': {
        'id': 'string',
        'data': {
            'actionTypeId': {
                'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                'owner': 'AWS'|'ThirdParty'|'Custom',
                'provider': 'string',
                'version': 'string'
            },
            'actionConfiguration': {
                'configuration': {
                    'string': 'string'
                }
            },
            'pipelineContext': {
                'pipelineName': 'string',
                'stage': {
                    'name': 'string'
                },
                'action': {
                    'name': 'string',
                    'actionExecutionId': 'string'
                },
                'pipelineArn': 'string',
                'pipelineExecutionId': 'string'
            },
            'inputArtifacts': [
                {
                    'name': 'string',
                    'revision': 'string',
                    'location': {
                        'type': 'S3',
                        's3Location': {
                            'bucketName': 'string',
                            'objectKey': 'string'
                        }
                    }
                },
            ],
            'outputArtifacts': [
                {
                    'name': 'string',
                    'revision': 'string',
                    'location': {
                        'type': 'S3',
                        's3Location': {
                            'bucketName': 'string',
                            'objectKey': 'string'
                        }
                    }
                },
            ],
            'artifactCredentials': {
                'accessKeyId': 'string',
                'secretAccessKey': 'string',
                'sessionToken': 'string'
            },
            'continuationToken': 'string',
            'encryptionKey': {
                'id': 'string',
                'type': 'KMS'
            }
        },
        'nonce': 'string'
    }
}


Response Structure

(dict) --
Represents the output of a GetThirdPartyJobDetails action.

jobDetails (dict) --
The details of the job, including any protected values defined for the job.

id (string) --
The identifier used to identify the job details in AWS CodePipeline.

data (dict) --
The data to be returned by the third party job worker.

actionTypeId (dict) --
Represents information about an action type.

category (string) --
A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.

owner (string) --
The creator of the action being called.

provider (string) --
The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see Valid Action Types and Providers in CodePipeline .

version (string) --
A string that describes the action version.



actionConfiguration (dict) --
Represents information about an action configuration.

configuration (dict) --
The configuration data for the action.

(string) --
(string) --






pipelineContext (dict) --
Represents information about a pipeline to a job worker.

Note
Does not include pipelineArn and pipelineExecutionId for ThirdParty jobs.


pipelineName (string) --
The name of the pipeline. This is a user-specified value. Pipeline names must be unique across all pipeline names under an Amazon Web Services account.

stage (dict) --
The stage of the pipeline.

name (string) --
The name of the stage.



action (dict) --
The context of an action to a job worker in the stage of a pipeline.

name (string) --
The name of the action in the context of a job.

actionExecutionId (string) --
The system-generated unique ID that corresponds to an action\'s execution.



pipelineArn (string) --
The Amazon Resource Name (ARN) of the pipeline.

pipelineExecutionId (string) --
The execution ID of the pipeline.



inputArtifacts (list) --
The name of the artifact that is worked on by the action, if any. This name might be system-generated, such as "MyApp", or it might be defined by the user when the action is created. The input artifact name must match the name of an output artifact generated by an action in an earlier action or stage of the pipeline.

(dict) --
Represents information about an artifact that is worked on by actions in the pipeline.

name (string) --
The artifact\'s name.

revision (string) --
The artifact\'s revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).

location (dict) --
The location of an artifact.

type (string) --
The type of artifact in the location.

s3Location (dict) --
The S3 bucket that contains the artifact.

bucketName (string) --
The name of the S3 bucket.

objectKey (string) --
The key of the object in the S3 bucket, which uniquely identifies the object in the bucket.









outputArtifacts (list) --
The name of the artifact that is the result of the action, if any. This name might be system-generated, such as "MyBuiltApp", or it might be defined by the user when the action is created.

(dict) --
Represents information about an artifact that is worked on by actions in the pipeline.

name (string) --
The artifact\'s name.

revision (string) --
The artifact\'s revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).

location (dict) --
The location of an artifact.

type (string) --
The type of artifact in the location.

s3Location (dict) --
The S3 bucket that contains the artifact.

bucketName (string) --
The name of the S3 bucket.

objectKey (string) --
The key of the object in the S3 bucket, which uniquely identifies the object in the bucket.









artifactCredentials (dict) --
Represents an AWS session credentials object. These credentials are temporary credentials that are issued by AWS Secure Token Service (STS). They can be used to access input and output artifacts in the S3 bucket used to store artifact for the pipeline in AWS CodePipeline.

accessKeyId (string) --
The access key for the session.

secretAccessKey (string) --
The secret access key for the session.

sessionToken (string) --
The token for the session.



continuationToken (string) --
A system-generated token, such as a AWS CodeDeploy deployment ID, that a job requires to continue the job asynchronously.

encryptionKey (dict) --
The encryption key used to encrypt and decrypt data in the artifact store for the pipeline, such as an AWS Key Management Service (AWS KMS) key. This is optional and might not be present.

id (string) --
The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN, or the alias ARN.

Note
Aliases are recognized only in the account that created the customer master key (CMK). For cross-account actions, you can only use the key ID or key ARN to identify the key.


type (string) --
The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.





nonce (string) --
A system-generated random number that AWS CodePipeline uses to ensure that the job is being worked on by only one job worker. Use this number in an  AcknowledgeThirdPartyJob request.









Exceptions

CodePipeline.Client.exceptions.JobNotFoundException
CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.InvalidClientTokenException
CodePipeline.Client.exceptions.InvalidJobException


    :return: {
        'jobDetails': {
            'id': 'string',
            'data': {
                'actionTypeId': {
                    'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                    'owner': 'AWS'|'ThirdParty'|'Custom',
                    'provider': 'string',
                    'version': 'string'
                },
                'actionConfiguration': {
                    'configuration': {
                        'string': 'string'
                    }
                },
                'pipelineContext': {
                    'pipelineName': 'string',
                    'stage': {
                        'name': 'string'
                    },
                    'action': {
                        'name': 'string',
                        'actionExecutionId': 'string'
                    },
                    'pipelineArn': 'string',
                    'pipelineExecutionId': 'string'
                },
                'inputArtifacts': [
                    {
                        'name': 'string',
                        'revision': 'string',
                        'location': {
                            'type': 'S3',
                            's3Location': {
                                'bucketName': 'string',
                                'objectKey': 'string'
                            }
                        }
                    },
                ],
                'outputArtifacts': [
                    {
                        'name': 'string',
                        'revision': 'string',
                        'location': {
                            'type': 'S3',
                            's3Location': {
                                'bucketName': 'string',
                                'objectKey': 'string'
                            }
                        }
                    },
                ],
                'artifactCredentials': {
                    'accessKeyId': 'string',
                    'secretAccessKey': 'string',
                    'sessionToken': 'string'
                },
                'continuationToken': 'string',
                'encryptionKey': {
                    'id': 'string',
                    'type': 'KMS'
                }
            },
            'nonce': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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

def list_action_executions(pipelineName=None, filter=None, maxResults=None, nextToken=None):
    """
    Lists the action executions that have occurred in a pipeline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_action_executions(
        pipelineName='string',
        filter={
            'pipelineExecutionId': 'string'
        },
        maxResults=123,
        nextToken='string'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]\nThe name of the pipeline for which you want to list action execution history.\n

    :type filter: dict
    :param filter: Input information used to filter action execution history.\n\npipelineExecutionId (string) --The pipeline execution ID used to filter action execution history.\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Action execution history is retained for up to 12 months, based on action execution start times. Default value is 100.\n\nNote\nDetailed execution history is available for executions run on or after February 21, 2019.\n\n

    :type nextToken: string
    :param nextToken: The token that was returned from the previous ListActionExecutions call, which can be used to return the next set of action executions in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'actionExecutionDetails': [
        {
            'pipelineExecutionId': 'string',
            'actionExecutionId': 'string',
            'pipelineVersion': 123,
            'stageName': 'string',
            'actionName': 'string',
            'startTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1),
            'status': 'InProgress'|'Abandoned'|'Succeeded'|'Failed',
            'input': {
                'actionTypeId': {
                    'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                    'owner': 'AWS'|'ThirdParty'|'Custom',
                    'provider': 'string',
                    'version': 'string'
                },
                'configuration': {
                    'string': 'string'
                },
                'resolvedConfiguration': {
                    'string': 'string'
                },
                'roleArn': 'string',
                'region': 'string',
                'inputArtifacts': [
                    {
                        'name': 'string',
                        's3location': {
                            'bucket': 'string',
                            'key': 'string'
                        }
                    },
                ],
                'namespace': 'string'
            },
            'output': {
                'outputArtifacts': [
                    {
                        'name': 'string',
                        's3location': {
                            'bucket': 'string',
                            'key': 'string'
                        }
                    },
                ],
                'executionResult': {
                    'externalExecutionId': 'string',
                    'externalExecutionSummary': 'string',
                    'externalExecutionUrl': 'string'
                },
                'outputVariables': {
                    'string': 'string'
                }
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

actionExecutionDetails (list) --
The details for a list of recent executions, such as action execution ID.

(dict) --
Returns information about an execution of an action, including the action execution ID, and the name, version, and timing of the action.

pipelineExecutionId (string) --
The pipeline execution ID for the action execution.

actionExecutionId (string) --
The action execution ID.

pipelineVersion (integer) --
The version of the pipeline where the action was run.

stageName (string) --
The name of the stage that contains the action.

actionName (string) --
The name of the action.

startTime (datetime) --
The start time of the action execution.

lastUpdateTime (datetime) --
The last update time of the action execution.

status (string) --
The status of the action execution. Status categories are InProgress , Succeeded , and Failed .

input (dict) --
Input details for the action execution, such as role ARN, Region, and input artifacts.

actionTypeId (dict) --
Represents information about an action type.

category (string) --
A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.

owner (string) --
The creator of the action being called.

provider (string) --
The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see Valid Action Types and Providers in CodePipeline .

version (string) --
A string that describes the action version.



configuration (dict) --
Configuration data for an action execution.

(string) --
(string) --




resolvedConfiguration (dict) --
Configuration data for an action execution with all variable references replaced with their real values for the execution.

(string) --
(string) --




roleArn (string) --
The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline.

region (string) --
The AWS Region for the action, such as us-east-1.

inputArtifacts (list) --
Details of input artifacts of the action that correspond to the action execution.

(dict) --
Artifact details for the action execution, such as the artifact location.

name (string) --
The artifact object name for the action execution.

s3location (dict) --
The Amazon S3 artifact location for the action execution.

bucket (string) --
The Amazon S3 artifact bucket for an action\'s artifacts.

key (string) --
The artifact name.







namespace (string) --
The variable namespace associated with the action. All variables produced as output by this action fall under this namespace.



output (dict) --
Output details for the action execution, such as the action execution result.

outputArtifacts (list) --
Details of output artifacts of the action that correspond to the action execution.

(dict) --
Artifact details for the action execution, such as the artifact location.

name (string) --
The artifact object name for the action execution.

s3location (dict) --
The Amazon S3 artifact location for the action execution.

bucket (string) --
The Amazon S3 artifact bucket for an action\'s artifacts.

key (string) --
The artifact name.







executionResult (dict) --
Execution result information listed in the output details for an action execution.

externalExecutionId (string) --
The action provider\'s external ID for the action execution.

externalExecutionSummary (string) --
The action provider\'s summary for the action execution.

externalExecutionUrl (string) --
The deepest external link to the external resource (for example, a repository URL or deployment endpoint) that is used when running the action.



outputVariables (dict) --
The outputVariables field shows the key-value pairs that were output as part of that execution.

(string) --
(string) --










nextToken (string) --
If the amount of returned information is significantly large, an identifier is also returned and can be used in a subsequent ListActionExecutions call to return the next set of action executions in the list.







Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.PipelineNotFoundException
CodePipeline.Client.exceptions.InvalidNextTokenException
CodePipeline.Client.exceptions.PipelineExecutionNotFoundException


    :return: {
        'actionExecutionDetails': [
            {
                'pipelineExecutionId': 'string',
                'actionExecutionId': 'string',
                'pipelineVersion': 123,
                'stageName': 'string',
                'actionName': 'string',
                'startTime': datetime(2015, 1, 1),
                'lastUpdateTime': datetime(2015, 1, 1),
                'status': 'InProgress'|'Abandoned'|'Succeeded'|'Failed',
                'input': {
                    'actionTypeId': {
                        'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                        'owner': 'AWS'|'ThirdParty'|'Custom',
                        'provider': 'string',
                        'version': 'string'
                    },
                    'configuration': {
                        'string': 'string'
                    },
                    'resolvedConfiguration': {
                        'string': 'string'
                    },
                    'roleArn': 'string',
                    'region': 'string',
                    'inputArtifacts': [
                        {
                            'name': 'string',
                            's3location': {
                                'bucket': 'string',
                                'key': 'string'
                            }
                        },
                    ],
                    'namespace': 'string'
                },
                'output': {
                    'outputArtifacts': [
                        {
                            'name': 'string',
                            's3location': {
                                'bucket': 'string',
                                'key': 'string'
                            }
                        },
                    ],
                    'executionResult': {
                        'externalExecutionId': 'string',
                        'externalExecutionSummary': 'string',
                        'externalExecutionUrl': 'string'
                    },
                    'outputVariables': {
                        'string': 'string'
                    }
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_action_types(actionOwnerFilter=None, nextToken=None):
    """
    Gets a summary of all AWS CodePipeline action types associated with your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_action_types(
        actionOwnerFilter='AWS'|'ThirdParty'|'Custom',
        nextToken='string'
    )
    
    
    :type actionOwnerFilter: string
    :param actionOwnerFilter: Filters the list of action types to those created by a specified entity.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous list action types call, which can be used to return the next set of action types in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'actionTypes': [
        {
            'id': {
                'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                'owner': 'AWS'|'ThirdParty'|'Custom',
                'provider': 'string',
                'version': 'string'
            },
            'settings': {
                'thirdPartyConfigurationUrl': 'string',
                'entityUrlTemplate': 'string',
                'executionUrlTemplate': 'string',
                'revisionUrlTemplate': 'string'
            },
            'actionConfigurationProperties': [
                {
                    'name': 'string',
                    'required': True|False,
                    'key': True|False,
                    'secret': True|False,
                    'queryable': True|False,
                    'description': 'string',
                    'type': 'String'|'Number'|'Boolean'
                },
            ],
            'inputArtifactDetails': {
                'minimumCount': 123,
                'maximumCount': 123
            },
            'outputArtifactDetails': {
                'minimumCount': 123,
                'maximumCount': 123
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the output of a ListActionTypes action.

actionTypes (list) --
Provides details of the action types.

(dict) --
Returns information about the details of an action type.

id (dict) --
Represents information about an action type.

category (string) --
A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.

owner (string) --
The creator of the action being called.

provider (string) --
The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see Valid Action Types and Providers in CodePipeline .

version (string) --
A string that describes the action version.



settings (dict) --
The settings for the action type.

thirdPartyConfigurationUrl (string) --
The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.

entityUrlTemplate (string) --
The URL returned to the AWS CodePipeline console that provides a deep link to the resources of the external system, such as the configuration page for an AWS CodeDeploy deployment group. This link is provided as part of the action display in the pipeline.

executionUrlTemplate (string) --
The URL returned to the AWS CodePipeline console that contains a link to the top-level landing page for the external system, such as the console page for AWS CodeDeploy. This link is shown on the pipeline view page in the AWS CodePipeline console and provides a link to the execution entity of the external action.

revisionUrlTemplate (string) --
The URL returned to the AWS CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.



actionConfigurationProperties (list) --
The configuration properties for the action type.

(dict) --
Represents information about an action configuration property.

name (string) --
The name of the action configuration property.

required (boolean) --
Whether the configuration property is a required value.

key (boolean) --
Whether the configuration property is a key.

secret (boolean) --
Whether the configuration property is secret. Secrets are hidden from all calls except for GetJobDetails , GetThirdPartyJobDetails , PollForJobs , and PollForThirdPartyJobs .
When updating a pipeline, passing * * * * * without changing any other values of the action preserves the previous value of the secret.

queryable (boolean) --
Indicates that the property is used with PollForJobs . When creating a custom action, an action can have up to one queryable property. If it has one, that property must be both required and not secret.
If you create a pipeline with a custom action type, and that custom action contains a queryable property, the value for that configuration property is subject to other restrictions. The value must be less than or equal to twenty (20) characters. The value can contain only alphanumeric characters, underscores, and hyphens.

description (string) --
The description of the action configuration property that is displayed to users.

type (string) --
The type of the configuration property.





inputArtifactDetails (dict) --
The details of the input artifact for the action, such as its commit ID.

minimumCount (integer) --
The minimum number of artifacts allowed for the action type.

maximumCount (integer) --
The maximum number of artifacts allowed for the action type.



outputArtifactDetails (dict) --
The details of the output artifact of the action, such as its commit ID.

minimumCount (integer) --
The minimum number of artifacts allowed for the action type.

maximumCount (integer) --
The maximum number of artifacts allowed for the action type.







nextToken (string) --
If the amount of returned information is significantly large, an identifier is also returned. It can be used in a subsequent list action types call to return the next set of action types in the list.







Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.InvalidNextTokenException


    :return: {
        'actionTypes': [
            {
                'id': {
                    'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                    'owner': 'AWS'|'ThirdParty'|'Custom',
                    'provider': 'string',
                    'version': 'string'
                },
                'settings': {
                    'thirdPartyConfigurationUrl': 'string',
                    'entityUrlTemplate': 'string',
                    'executionUrlTemplate': 'string',
                    'revisionUrlTemplate': 'string'
                },
                'actionConfigurationProperties': [
                    {
                        'name': 'string',
                        'required': True|False,
                        'key': True|False,
                        'secret': True|False,
                        'queryable': True|False,
                        'description': 'string',
                        'type': 'String'|'Number'|'Boolean'
                    },
                ],
                'inputArtifactDetails': {
                    'minimumCount': 123,
                    'maximumCount': 123
                },
                'outputArtifactDetails': {
                    'minimumCount': 123,
                    'maximumCount': 123
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def list_pipeline_executions(pipelineName=None, maxResults=None, nextToken=None):
    """
    Gets a summary of the most recent executions for a pipeline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_pipeline_executions(
        pipelineName='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]\nThe name of the pipeline for which you want to get execution summary information.\n

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Pipeline history is limited to the most recent 12 months, based on pipeline execution start times. Default value is 100.

    :type nextToken: string
    :param nextToken: The token that was returned from the previous ListPipelineExecutions call, which can be used to return the next set of pipeline executions in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'pipelineExecutionSummaries': [
        {
            'pipelineExecutionId': 'string',
            'status': 'InProgress'|'Stopped'|'Stopping'|'Succeeded'|'Superseded'|'Failed',
            'startTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1),
            'sourceRevisions': [
                {
                    'actionName': 'string',
                    'revisionId': 'string',
                    'revisionSummary': 'string',
                    'revisionUrl': 'string'
                },
            ],
            'trigger': {
                'triggerType': 'CreatePipeline'|'StartPipelineExecution'|'PollForSourceChanges'|'Webhook'|'CloudWatchEvent'|'PutActionRevision',
                'triggerDetail': 'string'
            },
            'stopTrigger': {
                'reason': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the output of a ListPipelineExecutions action.

pipelineExecutionSummaries (list) --
A list of executions in the history of a pipeline.

(dict) --
Summary information about a pipeline execution.

pipelineExecutionId (string) --
The ID of the pipeline execution.

status (string) --
The status of the pipeline execution.

InProgress: The pipeline execution is currently running.
Stopped: The pipeline execution was manually stopped. For more information, see Stopped Executions .
Stopping: The pipeline execution received a request to be manually stopped. Depending on the selected stop mode, the execution is either completing or abandoning in-progress actions. For more information, see Stopped Executions .
Succeeded: The pipeline execution was completed successfully.
Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution advanced and continued through the pipeline instead. For more information, see Superseded Executions .
Failed: The pipeline execution was not completed successfully.


startTime (datetime) --
The date and time when the pipeline execution began, in timestamp format.

lastUpdateTime (datetime) --
The date and time of the last change to the pipeline execution, in timestamp format.

sourceRevisions (list) --
A list of the source artifact revisions that initiated a pipeline execution.

(dict) --
Information about the version (or revision) of a source artifact that initiated a pipeline execution.

actionName (string) --
The name of the action that processed the revision to the source artifact.

revisionId (string) --
The system-generated unique ID that identifies the revision number of the artifact.

revisionSummary (string) --
Summary information about the most recent revision of the artifact. For GitHub and AWS CodeCommit repositories, the commit message. For Amazon S3 buckets or actions, the user-provided content of a codepipeline-artifact-revision-summary key specified in the object metadata.

revisionUrl (string) --
The commit ID for the artifact revision. For artifacts stored in GitHub or AWS CodeCommit repositories, the commit ID is linked to a commit details page.





trigger (dict) --
The interaction or event that started a pipeline execution, such as automated change detection or a StartPipelineExecution API call.

triggerType (string) --
The type of change-detection method, command, or user interaction that started a pipeline execution.

triggerDetail (string) --
Detail related to the event that started a pipeline execution, such as the webhook ARN of the webhook that triggered the pipeline execution or the user ARN for a user-initiated start-pipeline-execution CLI command.



stopTrigger (dict) --
The interaction that stopped a pipeline execution.

reason (string) --
The user-specified reason the pipeline was stopped.







nextToken (string) --
A token that can be used in the next ListPipelineExecutions call. To view all items in the list, continue to call this operation with each subsequent token until no more nextToken values are returned.







Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.PipelineNotFoundException
CodePipeline.Client.exceptions.InvalidNextTokenException


    :return: {
        'pipelineExecutionSummaries': [
            {
                'pipelineExecutionId': 'string',
                'status': 'InProgress'|'Stopped'|'Stopping'|'Succeeded'|'Superseded'|'Failed',
                'startTime': datetime(2015, 1, 1),
                'lastUpdateTime': datetime(2015, 1, 1),
                'sourceRevisions': [
                    {
                        'actionName': 'string',
                        'revisionId': 'string',
                        'revisionSummary': 'string',
                        'revisionUrl': 'string'
                    },
                ],
                'trigger': {
                    'triggerType': 'CreatePipeline'|'StartPipelineExecution'|'PollForSourceChanges'|'Webhook'|'CloudWatchEvent'|'PutActionRevision',
                    'triggerDetail': 'string'
                },
                'stopTrigger': {
                    'reason': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    InProgress: The pipeline execution is currently running.
    Stopped: The pipeline execution was manually stopped. For more information, see Stopped Executions .
    Stopping: The pipeline execution received a request to be manually stopped. Depending on the selected stop mode, the execution is either completing or abandoning in-progress actions. For more information, see Stopped Executions .
    Succeeded: The pipeline execution was completed successfully.
    Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution advanced and continued through the pipeline instead. For more information, see Superseded Executions .
    Failed: The pipeline execution was not completed successfully.
    
    """
    pass

def list_pipelines(nextToken=None):
    """
    Gets a summary of all of the pipelines associated with your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_pipelines(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous list pipelines call. It can be used to return the next set of pipelines in the list.

    :rtype: dict
ReturnsResponse Syntax{
    'pipelines': [
        {
            'name': 'string',
            'version': 123,
            'created': datetime(2015, 1, 1),
            'updated': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --Represents the output of a ListPipelines action.

pipelines (list) --The list of pipelines.

(dict) --Returns a summary of a pipeline.

name (string) --The name of the pipeline.

version (integer) --The version number of the pipeline.

created (datetime) --The date and time the pipeline was created, in timestamp format.

updated (datetime) --The date and time of the last update to the pipeline, in timestamp format.





nextToken (string) --If the amount of returned information is significantly large, an identifier is also returned. It can be used in a subsequent list pipelines call to return the next set of pipelines in the list.






Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.InvalidNextTokenException


    :return: {
        'pipelines': [
            {
                'name': 'string',
                'version': 123,
                'created': datetime(2015, 1, 1),
                'updated': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_tags_for_resource(resourceArn=None, nextToken=None, maxResults=None):
    """
    Gets the set of key-value pairs (metadata) that are used to manage the resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to get tags for.\n

    :type nextToken: string
    :param nextToken: The token that was returned from the previous API call, which would be used to return the next page of the list. The ListTagsforResource call lists all available tags in one call and does not use pagination.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in a single call.

    :rtype: dict

ReturnsResponse Syntax
{
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

tags (list) --
The tags for the resource.

(dict) --
A tag is a key-value pair that is used to manage the resource.

key (string) --
The tag\'s key.

value (string) --
The tag\'s value.





nextToken (string) --
If the amount of returned information is significantly large, an identifier is also returned and can be used in a subsequent API call to return the next page of the list. The ListTagsforResource call lists all available tags in one call and does not use pagination.







Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.ResourceNotFoundException
CodePipeline.Client.exceptions.InvalidNextTokenException
CodePipeline.Client.exceptions.InvalidArnException


    :return: {
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.ResourceNotFoundException
    CodePipeline.Client.exceptions.InvalidNextTokenException
    CodePipeline.Client.exceptions.InvalidArnException
    
    """
    pass

def list_webhooks(NextToken=None, MaxResults=None):
    """
    Gets a listing of all the webhooks in this AWS Region for this account. The output lists all webhooks and includes the webhook URL and ARN and the configuration for each webhook.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_webhooks(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The token that was returned from the previous ListWebhooks call, which can be used to return the next set of webhooks in the list.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'webhooks': [
        {
            'definition': {
                'name': 'string',
                'targetPipeline': 'string',
                'targetAction': 'string',
                'filters': [
                    {
                        'jsonPath': 'string',
                        'matchEquals': 'string'
                    },
                ],
                'authentication': 'GITHUB_HMAC'|'IP'|'UNAUTHENTICATED',
                'authenticationConfiguration': {
                    'AllowedIPRange': 'string',
                    'SecretToken': 'string'
                }
            },
            'url': 'string',
            'errorMessage': 'string',
            'errorCode': 'string',
            'lastTriggered': datetime(2015, 1, 1),
            'arn': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

webhooks (list) --
The JSON detail returned for each webhook in the list output for the ListWebhooks call.

(dict) --
The detail returned for each webhook after listing webhooks, such as the webhook URL, the webhook name, and the webhook ARN.

definition (dict) --
The detail returned for each webhook, such as the webhook authentication type and filter rules.

name (string) --
The name of the webhook.

targetPipeline (string) --
The name of the pipeline you want to connect to the webhook.

targetAction (string) --
The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.

filters (list) --
A list of rules applied to the body/payload sent in the POST request to a webhook URL. All defined rules must pass for the request to be accepted and the pipeline started.

(dict) --
The event criteria that specify when a webhook notification is sent to your URL.

jsonPath (string) --
A JsonPath expression that is applied to the body/payload of the webhook. The value selected by the JsonPath expression must match the value specified in the MatchEquals field. Otherwise, the request is ignored. For more information, see Java JsonPath implementation in GitHub.

matchEquals (string) --
The value selected by the JsonPath expression must match what is supplied in the MatchEquals field. Otherwise, the request is ignored. Properties from the target action configuration can be included as placeholders in this value by surrounding the action configuration key with curly brackets. For example, if the value supplied here is "refs/heads/{Branch}" and the target action has an action configuration property called "Branch" with a value of "master", the MatchEquals value is evaluated as "refs/heads/master". For a list of action configuration properties for built-in action types, see Pipeline Structure Reference Action Requirements .





authentication (string) --
Supported options are GITHUB_HMAC, IP, and UNAUTHENTICATED.

For information about the authentication scheme implemented by GITHUB_HMAC, see Securing your webhooks on the GitHub Developer website.
IP rejects webhooks trigger requests unless they originate from an IP address in the IP range whitelisted in the authentication configuration.
UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.


authenticationConfiguration (dict) --
Properties that configure the authentication applied to incoming webhook trigger requests. The required properties depend on the authentication type. For GITHUB_HMAC, only the SecretToken property must be set. For IP, only the AllowedIPRange property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be set.

AllowedIPRange (string) --
The property used to configure acceptance of webhooks in an IP address range. For IP, only the AllowedIPRange property must be set. This property must be set to a valid CIDR range.

SecretToken (string) --
The property used to configure GitHub authentication. For GITHUB_HMAC, only the SecretToken property must be set.





url (string) --
A unique URL generated by CodePipeline. When a POST request is made to this URL, the defined pipeline is started as long as the body of the post request satisfies the defined authentication and filtering conditions. Deleting and re-creating a webhook makes the old URL invalid and generates a new one.

errorMessage (string) --
The text of the error message about the webhook.

errorCode (string) --
The number code of the error.

lastTriggered (datetime) --
The date and time a webhook was last successfully triggered, in timestamp format.

arn (string) --
The Amazon Resource Name (ARN) of the webhook.

tags (list) --
Specifies the tags applied to the webhook.

(dict) --
A tag is a key-value pair that is used to manage the resource.

key (string) --
The tag\'s key.

value (string) --
The tag\'s value.









NextToken (string) --
If the amount of returned information is significantly large, an identifier is also returned and can be used in a subsequent ListWebhooks call to return the next set of webhooks in the list.







Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.InvalidNextTokenException


    :return: {
        'webhooks': [
            {
                'definition': {
                    'name': 'string',
                    'targetPipeline': 'string',
                    'targetAction': 'string',
                    'filters': [
                        {
                            'jsonPath': 'string',
                            'matchEquals': 'string'
                        },
                    ],
                    'authentication': 'GITHUB_HMAC'|'IP'|'UNAUTHENTICATED',
                    'authenticationConfiguration': {
                        'AllowedIPRange': 'string',
                        'SecretToken': 'string'
                    }
                },
                'url': 'string',
                'errorMessage': 'string',
                'errorCode': 'string',
                'lastTriggered': datetime(2015, 1, 1),
                'arn': 'string',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    For information about the authentication scheme implemented by GITHUB_HMAC, see Securing your webhooks on the GitHub Developer website.
    IP rejects webhooks trigger requests unless they originate from an IP address in the IP range whitelisted in the authentication configuration.
    UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.
    
    """
    pass

def poll_for_jobs(actionTypeId=None, maxBatchSize=None, queryParam=None):
    """
    Returns information about any jobs for AWS CodePipeline to act on. PollForJobs is valid only for action types with "Custom" in the owner field. If the action type contains "AWS" or "ThirdParty" in the owner field, the PollForJobs action returns an error.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.poll_for_jobs(
        actionTypeId={
            'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
            'owner': 'AWS'|'ThirdParty'|'Custom',
            'provider': 'string',
            'version': 'string'
        },
        maxBatchSize=123,
        queryParam={
            'string': 'string'
        }
    )
    
    
    :type actionTypeId: dict
    :param actionTypeId: [REQUIRED]\nRepresents information about an action type.\n\ncategory (string) -- [REQUIRED]A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.\n\nowner (string) -- [REQUIRED]The creator of the action being called.\n\nprovider (string) -- [REQUIRED]The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see Valid Action Types and Providers in CodePipeline .\n\nversion (string) -- [REQUIRED]A string that describes the action version.\n\n\n

    :type maxBatchSize: integer
    :param maxBatchSize: The maximum number of jobs to return in a poll for jobs call.

    :type queryParam: dict
    :param queryParam: A map of property names and values. For an action type with no queryable properties, this value must be null or an empty map. For an action type with a queryable property, you must supply that property as a key in the map. Only jobs whose action configuration matches the mapped value are returned.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'jobs': [
        {
            'id': 'string',
            'data': {
                'actionTypeId': {
                    'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                    'owner': 'AWS'|'ThirdParty'|'Custom',
                    'provider': 'string',
                    'version': 'string'
                },
                'actionConfiguration': {
                    'configuration': {
                        'string': 'string'
                    }
                },
                'pipelineContext': {
                    'pipelineName': 'string',
                    'stage': {
                        'name': 'string'
                    },
                    'action': {
                        'name': 'string',
                        'actionExecutionId': 'string'
                    },
                    'pipelineArn': 'string',
                    'pipelineExecutionId': 'string'
                },
                'inputArtifacts': [
                    {
                        'name': 'string',
                        'revision': 'string',
                        'location': {
                            'type': 'S3',
                            's3Location': {
                                'bucketName': 'string',
                                'objectKey': 'string'
                            }
                        }
                    },
                ],
                'outputArtifacts': [
                    {
                        'name': 'string',
                        'revision': 'string',
                        'location': {
                            'type': 'S3',
                            's3Location': {
                                'bucketName': 'string',
                                'objectKey': 'string'
                            }
                        }
                    },
                ],
                'artifactCredentials': {
                    'accessKeyId': 'string',
                    'secretAccessKey': 'string',
                    'sessionToken': 'string'
                },
                'continuationToken': 'string',
                'encryptionKey': {
                    'id': 'string',
                    'type': 'KMS'
                }
            },
            'nonce': 'string',
            'accountId': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a PollForJobs action.

jobs (list) --
Information about the jobs to take action on.

(dict) --
Represents information about a job.

id (string) --
The unique system-generated ID of the job.

data (dict) --
Other data about a job.

actionTypeId (dict) --
Represents information about an action type.

category (string) --
A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.

owner (string) --
The creator of the action being called.

provider (string) --
The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see Valid Action Types and Providers in CodePipeline .

version (string) --
A string that describes the action version.



actionConfiguration (dict) --
Represents information about an action configuration.

configuration (dict) --
The configuration data for the action.

(string) --
(string) --






pipelineContext (dict) --
Represents information about a pipeline to a job worker.

Note
Includes pipelineArn and pipelineExecutionId for custom jobs.


pipelineName (string) --
The name of the pipeline. This is a user-specified value. Pipeline names must be unique across all pipeline names under an Amazon Web Services account.

stage (dict) --
The stage of the pipeline.

name (string) --
The name of the stage.



action (dict) --
The context of an action to a job worker in the stage of a pipeline.

name (string) --
The name of the action in the context of a job.

actionExecutionId (string) --
The system-generated unique ID that corresponds to an action\'s execution.



pipelineArn (string) --
The Amazon Resource Name (ARN) of the pipeline.

pipelineExecutionId (string) --
The execution ID of the pipeline.



inputArtifacts (list) --
The artifact supplied to the job.

(dict) --
Represents information about an artifact that is worked on by actions in the pipeline.

name (string) --
The artifact\'s name.

revision (string) --
The artifact\'s revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).

location (dict) --
The location of an artifact.

type (string) --
The type of artifact in the location.

s3Location (dict) --
The S3 bucket that contains the artifact.

bucketName (string) --
The name of the S3 bucket.

objectKey (string) --
The key of the object in the S3 bucket, which uniquely identifies the object in the bucket.









outputArtifacts (list) --
The output of the job.

(dict) --
Represents information about an artifact that is worked on by actions in the pipeline.

name (string) --
The artifact\'s name.

revision (string) --
The artifact\'s revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).

location (dict) --
The location of an artifact.

type (string) --
The type of artifact in the location.

s3Location (dict) --
The S3 bucket that contains the artifact.

bucketName (string) --
The name of the S3 bucket.

objectKey (string) --
The key of the object in the S3 bucket, which uniquely identifies the object in the bucket.









artifactCredentials (dict) --
Represents an AWS session credentials object. These credentials are temporary credentials that are issued by AWS Secure Token Service (STS). They can be used to access input and output artifacts in the S3 bucket used to store artifacts for the pipeline in AWS CodePipeline.

accessKeyId (string) --
The access key for the session.

secretAccessKey (string) --
The secret access key for the session.

sessionToken (string) --
The token for the session.



continuationToken (string) --
A system-generated token, such as a AWS CodeDeploy deployment ID, required by a job to continue the job asynchronously.

encryptionKey (dict) --
Represents information about the key used to encrypt data in the artifact store, such as an AWS Key Management Service (AWS KMS) key.

id (string) --
The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN, or the alias ARN.

Note
Aliases are recognized only in the account that created the customer master key (CMK). For cross-account actions, you can only use the key ID or key ARN to identify the key.


type (string) --
The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.





nonce (string) --
A system-generated random number that AWS CodePipeline uses to ensure that the job is being worked on by only one job worker. Use this number in an  AcknowledgeJob request.

accountId (string) --
The ID of the AWS account to use when performing the job.











Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.ActionTypeNotFoundException


    :return: {
        'jobs': [
            {
                'id': 'string',
                'data': {
                    'actionTypeId': {
                        'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                        'owner': 'AWS'|'ThirdParty'|'Custom',
                        'provider': 'string',
                        'version': 'string'
                    },
                    'actionConfiguration': {
                        'configuration': {
                            'string': 'string'
                        }
                    },
                    'pipelineContext': {
                        'pipelineName': 'string',
                        'stage': {
                            'name': 'string'
                        },
                        'action': {
                            'name': 'string',
                            'actionExecutionId': 'string'
                        },
                        'pipelineArn': 'string',
                        'pipelineExecutionId': 'string'
                    },
                    'inputArtifacts': [
                        {
                            'name': 'string',
                            'revision': 'string',
                            'location': {
                                'type': 'S3',
                                's3Location': {
                                    'bucketName': 'string',
                                    'objectKey': 'string'
                                }
                            }
                        },
                    ],
                    'outputArtifacts': [
                        {
                            'name': 'string',
                            'revision': 'string',
                            'location': {
                                'type': 'S3',
                                's3Location': {
                                    'bucketName': 'string',
                                    'objectKey': 'string'
                                }
                            }
                        },
                    ],
                    'artifactCredentials': {
                        'accessKeyId': 'string',
                        'secretAccessKey': 'string',
                        'sessionToken': 'string'
                    },
                    'continuationToken': 'string',
                    'encryptionKey': {
                        'id': 'string',
                        'type': 'KMS'
                    }
                },
                'nonce': 'string',
                'accountId': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def poll_for_third_party_jobs(actionTypeId=None, maxBatchSize=None):
    """
    Determines whether there are any third party jobs for a job worker to act on. Used for partner actions only.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.poll_for_third_party_jobs(
        actionTypeId={
            'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
            'owner': 'AWS'|'ThirdParty'|'Custom',
            'provider': 'string',
            'version': 'string'
        },
        maxBatchSize=123
    )
    
    
    :type actionTypeId: dict
    :param actionTypeId: [REQUIRED]\nRepresents information about an action type.\n\ncategory (string) -- [REQUIRED]A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.\n\nowner (string) -- [REQUIRED]The creator of the action being called.\n\nprovider (string) -- [REQUIRED]The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see Valid Action Types and Providers in CodePipeline .\n\nversion (string) -- [REQUIRED]A string that describes the action version.\n\n\n

    :type maxBatchSize: integer
    :param maxBatchSize: The maximum number of jobs to return in a poll for jobs call.

    :rtype: dict

ReturnsResponse Syntax
{
    'jobs': [
        {
            'clientId': 'string',
            'jobId': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a PollForThirdPartyJobs action.

jobs (list) --
Information about the jobs to take action on.

(dict) --
A response to a PollForThirdPartyJobs request returned by AWS CodePipeline when there is a job to be worked on by a partner action.

clientId (string) --
The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.

jobId (string) --
The identifier used to identify the job in AWS CodePipeline.











Exceptions

CodePipeline.Client.exceptions.ActionTypeNotFoundException
CodePipeline.Client.exceptions.ValidationException


    :return: {
        'jobs': [
            {
                'clientId': 'string',
                'jobId': 'string'
            },
        ]
    }
    
    
    :returns: 
    CodePipeline.Client.exceptions.ActionTypeNotFoundException
    CodePipeline.Client.exceptions.ValidationException
    
    """
    pass

def put_action_revision(pipelineName=None, stageName=None, actionName=None, actionRevision=None):
    """
    Provides information to AWS CodePipeline about new revisions to a source.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_action_revision(
        pipelineName='string',
        stageName='string',
        actionName='string',
        actionRevision={
            'revisionId': 'string',
            'revisionChangeId': 'string',
            'created': datetime(2015, 1, 1)
        }
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]\nThe name of the pipeline that starts processing the revision to the source.\n

    :type stageName: string
    :param stageName: [REQUIRED]\nThe name of the stage that contains the action that acts on the revision.\n

    :type actionName: string
    :param actionName: [REQUIRED]\nThe name of the action that processes the revision.\n

    :type actionRevision: dict
    :param actionRevision: [REQUIRED]\nRepresents information about the version (or revision) of an action.\n\nrevisionId (string) -- [REQUIRED]The system-generated unique ID that identifies the revision number of the action.\n\nrevisionChangeId (string) -- [REQUIRED]The unique identifier of the change that set the state to this revision (for example, a deployment ID or timestamp).\n\ncreated (datetime) -- [REQUIRED]The date and time when the most recent version of the action was created, in timestamp format.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'newRevision': True|False,
    'pipelineExecutionId': 'string'
}


Response Structure

(dict) --
Represents the output of a PutActionRevision action.

newRevision (boolean) --
Indicates whether the artifact revision was previously used in an execution of the specified pipeline.

pipelineExecutionId (string) --
The ID of the current workflow state of the pipeline.







Exceptions

CodePipeline.Client.exceptions.PipelineNotFoundException
CodePipeline.Client.exceptions.StageNotFoundException
CodePipeline.Client.exceptions.ActionNotFoundException
CodePipeline.Client.exceptions.ValidationException


    :return: {
        'newRevision': True|False,
        'pipelineExecutionId': 'string'
    }
    
    
    :returns: 
    CodePipeline.Client.exceptions.PipelineNotFoundException
    CodePipeline.Client.exceptions.StageNotFoundException
    CodePipeline.Client.exceptions.ActionNotFoundException
    CodePipeline.Client.exceptions.ValidationException
    
    """
    pass

def put_approval_result(pipelineName=None, stageName=None, actionName=None, result=None, token=None):
    """
    Provides the response to a manual approval request to AWS CodePipeline. Valid responses include Approved and Rejected.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_approval_result(
        pipelineName='string',
        stageName='string',
        actionName='string',
        result={
            'summary': 'string',
            'status': 'Approved'|'Rejected'
        },
        token='string'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]\nThe name of the pipeline that contains the action.\n

    :type stageName: string
    :param stageName: [REQUIRED]\nThe name of the stage that contains the action.\n

    :type actionName: string
    :param actionName: [REQUIRED]\nThe name of the action for which approval is requested.\n

    :type result: dict
    :param result: [REQUIRED]\nRepresents information about the result of the approval request.\n\nsummary (string) -- [REQUIRED]The summary of the current status of the approval request.\n\nstatus (string) -- [REQUIRED]The response submitted by a reviewer assigned to an approval action request.\n\n\n

    :type token: string
    :param token: [REQUIRED]\nThe system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the GetPipelineState action. It is used to validate that the approval request corresponding to this token is still valid.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'approvedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --
Represents the output of a PutApprovalResult action.

approvedAt (datetime) --
The timestamp showing when the approval or rejection was submitted.







Exceptions

CodePipeline.Client.exceptions.InvalidApprovalTokenException
CodePipeline.Client.exceptions.ApprovalAlreadyCompletedException
CodePipeline.Client.exceptions.PipelineNotFoundException
CodePipeline.Client.exceptions.StageNotFoundException
CodePipeline.Client.exceptions.ActionNotFoundException
CodePipeline.Client.exceptions.ValidationException


    :return: {
        'approvedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    CodePipeline.Client.exceptions.InvalidApprovalTokenException
    CodePipeline.Client.exceptions.ApprovalAlreadyCompletedException
    CodePipeline.Client.exceptions.PipelineNotFoundException
    CodePipeline.Client.exceptions.StageNotFoundException
    CodePipeline.Client.exceptions.ActionNotFoundException
    CodePipeline.Client.exceptions.ValidationException
    
    """
    pass

def put_job_failure_result(jobId=None, failureDetails=None):
    """
    Represents the failure of a job as returned to the pipeline by a job worker. Used for custom actions only.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_job_failure_result(
        jobId='string',
        failureDetails={
            'type': 'JobFailed'|'ConfigurationError'|'PermissionError'|'RevisionOutOfSync'|'RevisionUnavailable'|'SystemUnavailable',
            'message': 'string',
            'externalExecutionId': 'string'
        }
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique system-generated ID of the job that failed. This is the same ID returned from PollForJobs .\n

    :type failureDetails: dict
    :param failureDetails: [REQUIRED]\nThe details about the failure of a job.\n\ntype (string) -- [REQUIRED]The type of the failure.\n\nmessage (string) -- [REQUIRED]The message about the failure.\n\nexternalExecutionId (string) --The external ID of the run of the action that failed.\n\n\n

    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.JobNotFoundException
    CodePipeline.Client.exceptions.InvalidJobStateException
    
    """
    pass

def put_job_success_result(jobId=None, currentRevision=None, continuationToken=None, executionDetails=None, outputVariables=None):
    """
    Represents the success of a job as returned to the pipeline by a job worker. Used for custom actions only.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_job_success_result(
        jobId='string',
        currentRevision={
            'revision': 'string',
            'changeIdentifier': 'string',
            'created': datetime(2015, 1, 1),
            'revisionSummary': 'string'
        },
        continuationToken='string',
        executionDetails={
            'summary': 'string',
            'externalExecutionId': 'string',
            'percentComplete': 123
        },
        outputVariables={
            'string': 'string'
        }
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique system-generated ID of the job that succeeded. This is the same ID returned from PollForJobs .\n

    :type currentRevision: dict
    :param currentRevision: The ID of the current revision of the artifact successfully worked on by the job.\n\nrevision (string) -- [REQUIRED]The revision ID of the current version of an artifact.\n\nchangeIdentifier (string) -- [REQUIRED]The change identifier for the current revision.\n\ncreated (datetime) --The date and time when the most recent revision of the artifact was created, in timestamp format.\n\nrevisionSummary (string) --The summary of the most recent revision of the artifact.\n\n\n

    :type continuationToken: string
    :param continuationToken: A token generated by a job worker, such as an AWS CodeDeploy deployment ID, that a successful job provides to identify a custom action in progress. Future jobs use this token to identify the running instance of the action. It can be reused to return more information about the progress of the custom action. When the action is complete, no continuation token should be supplied.

    :type executionDetails: dict
    :param executionDetails: The execution details of the successful job, such as the actions taken by the job worker.\n\nsummary (string) --The summary of the current status of the actions.\n\nexternalExecutionId (string) --The system-generated unique ID of this action used to identify this job worker in any external systems, such as AWS CodeDeploy.\n\npercentComplete (integer) --The percentage of work completed on the action, represented on a scale of 0 to 100 percent.\n\n\n

    :type outputVariables: dict
    :param outputVariables: Key-value pairs produced as output by a job worker that can be made available to a downstream action configuration. outputVariables can be included only when there is no continuation token on the request.\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.JobNotFoundException
    CodePipeline.Client.exceptions.InvalidJobStateException
    CodePipeline.Client.exceptions.OutputVariablesSizeExceededException
    
    """
    pass

def put_third_party_job_failure_result(jobId=None, clientToken=None, failureDetails=None):
    """
    Represents the failure of a third party job as returned to the pipeline by a job worker. Used for partner actions only.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_third_party_job_failure_result(
        jobId='string',
        clientToken='string',
        failureDetails={
            'type': 'JobFailed'|'ConfigurationError'|'PermissionError'|'RevisionOutOfSync'|'RevisionUnavailable'|'SystemUnavailable',
            'message': 'string',
            'externalExecutionId': 'string'
        }
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe ID of the job that failed. This is the same ID returned from PollForThirdPartyJobs .\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.\n

    :type failureDetails: dict
    :param failureDetails: [REQUIRED]\nRepresents information about failure details.\n\ntype (string) -- [REQUIRED]The type of the failure.\n\nmessage (string) -- [REQUIRED]The message about the failure.\n\nexternalExecutionId (string) --The external ID of the run of the action that failed.\n\n\n

    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.JobNotFoundException
    CodePipeline.Client.exceptions.InvalidJobStateException
    CodePipeline.Client.exceptions.InvalidClientTokenException
    
    """
    pass

def put_third_party_job_success_result(jobId=None, clientToken=None, currentRevision=None, continuationToken=None, executionDetails=None):
    """
    Represents the success of a third party job as returned to the pipeline by a job worker. Used for partner actions only.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_third_party_job_success_result(
        jobId='string',
        clientToken='string',
        currentRevision={
            'revision': 'string',
            'changeIdentifier': 'string',
            'created': datetime(2015, 1, 1),
            'revisionSummary': 'string'
        },
        continuationToken='string',
        executionDetails={
            'summary': 'string',
            'externalExecutionId': 'string',
            'percentComplete': 123
        }
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe ID of the job that successfully completed. This is the same ID returned from PollForThirdPartyJobs .\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.\n

    :type currentRevision: dict
    :param currentRevision: Represents information about a current revision.\n\nrevision (string) -- [REQUIRED]The revision ID of the current version of an artifact.\n\nchangeIdentifier (string) -- [REQUIRED]The change identifier for the current revision.\n\ncreated (datetime) --The date and time when the most recent revision of the artifact was created, in timestamp format.\n\nrevisionSummary (string) --The summary of the most recent revision of the artifact.\n\n\n

    :type continuationToken: string
    :param continuationToken: A token generated by a job worker, such as an AWS CodeDeploy deployment ID, that a successful job provides to identify a partner action in progress. Future jobs use this token to identify the running instance of the action. It can be reused to return more information about the progress of the partner action. When the action is complete, no continuation token should be supplied.

    :type executionDetails: dict
    :param executionDetails: The details of the actions taken and results produced on an artifact as it passes through stages in the pipeline.\n\nsummary (string) --The summary of the current status of the actions.\n\nexternalExecutionId (string) --The system-generated unique ID of this action used to identify this job worker in any external systems, such as AWS CodeDeploy.\n\npercentComplete (integer) --The percentage of work completed on the action, represented on a scale of 0 to 100 percent.\n\n\n

    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.JobNotFoundException
    CodePipeline.Client.exceptions.InvalidJobStateException
    CodePipeline.Client.exceptions.InvalidClientTokenException
    
    """
    pass

def put_webhook(webhook=None, tags=None):
    """
    Defines a webhook and returns a unique webhook URL generated by CodePipeline. This URL can be supplied to third party source hosting providers to call every time there\'s a code change. When CodePipeline receives a POST request on this URL, the pipeline defined in the webhook is started as long as the POST request satisfied the authentication and filtering requirements supplied when defining the webhook. RegisterWebhookWithThirdParty and DeregisterWebhookWithThirdParty APIs can be used to automatically configure supported third parties to call the generated webhook URL.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_webhook(
        webhook={
            'name': 'string',
            'targetPipeline': 'string',
            'targetAction': 'string',
            'filters': [
                {
                    'jsonPath': 'string',
                    'matchEquals': 'string'
                },
            ],
            'authentication': 'GITHUB_HMAC'|'IP'|'UNAUTHENTICATED',
            'authenticationConfiguration': {
                'AllowedIPRange': 'string',
                'SecretToken': 'string'
            }
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type webhook: dict
    :param webhook: [REQUIRED]\nThe detail provided in an input file to create the webhook, such as the webhook name, the pipeline name, and the action name. Give the webhook a unique name that helps you identify it. You might name the webhook after the pipeline and action it targets so that you can easily recognize what it\'s used for later.\n\nname (string) -- [REQUIRED]The name of the webhook.\n\ntargetPipeline (string) -- [REQUIRED]The name of the pipeline you want to connect to the webhook.\n\ntargetAction (string) -- [REQUIRED]The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.\n\nfilters (list) -- [REQUIRED]A list of rules applied to the body/payload sent in the POST request to a webhook URL. All defined rules must pass for the request to be accepted and the pipeline started.\n\n(dict) --The event criteria that specify when a webhook notification is sent to your URL.\n\njsonPath (string) -- [REQUIRED]A JsonPath expression that is applied to the body/payload of the webhook. The value selected by the JsonPath expression must match the value specified in the MatchEquals field. Otherwise, the request is ignored. For more information, see Java JsonPath implementation in GitHub.\n\nmatchEquals (string) --The value selected by the JsonPath expression must match what is supplied in the MatchEquals field. Otherwise, the request is ignored. Properties from the target action configuration can be included as placeholders in this value by surrounding the action configuration key with curly brackets. For example, if the value supplied here is 'refs/heads/{Branch}' and the target action has an action configuration property called 'Branch' with a value of 'master', the MatchEquals value is evaluated as 'refs/heads/master'. For a list of action configuration properties for built-in action types, see Pipeline Structure Reference Action Requirements .\n\n\n\n\n\nauthentication (string) -- [REQUIRED]Supported options are GITHUB_HMAC, IP, and UNAUTHENTICATED.\n\nFor information about the authentication scheme implemented by GITHUB_HMAC, see Securing your webhooks on the GitHub Developer website.\nIP rejects webhooks trigger requests unless they originate from an IP address in the IP range whitelisted in the authentication configuration.\nUNAUTHENTICATED accepts all webhook trigger requests regardless of origin.\n\n\nauthenticationConfiguration (dict) -- [REQUIRED]Properties that configure the authentication applied to incoming webhook trigger requests. The required properties depend on the authentication type. For GITHUB_HMAC, only the SecretToken property must be set. For IP, only the AllowedIPRange property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be set.\n\nAllowedIPRange (string) --The property used to configure acceptance of webhooks in an IP address range. For IP, only the AllowedIPRange property must be set. This property must be set to a valid CIDR range.\n\nSecretToken (string) --The property used to configure GitHub authentication. For GITHUB_HMAC, only the SecretToken property must be set.\n\n\n\n\n

    :type tags: list
    :param tags: The tags for the webhook.\n\n(dict) --A tag is a key-value pair that is used to manage the resource.\n\nkey (string) -- [REQUIRED]The tag\'s key.\n\nvalue (string) -- [REQUIRED]The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'webhook': {
        'definition': {
            'name': 'string',
            'targetPipeline': 'string',
            'targetAction': 'string',
            'filters': [
                {
                    'jsonPath': 'string',
                    'matchEquals': 'string'
                },
            ],
            'authentication': 'GITHUB_HMAC'|'IP'|'UNAUTHENTICATED',
            'authenticationConfiguration': {
                'AllowedIPRange': 'string',
                'SecretToken': 'string'
            }
        },
        'url': 'string',
        'errorMessage': 'string',
        'errorCode': 'string',
        'lastTriggered': datetime(2015, 1, 1),
        'arn': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

webhook (dict) --
The detail returned from creating the webhook, such as the webhook name, webhook URL, and webhook ARN.

definition (dict) --
The detail returned for each webhook, such as the webhook authentication type and filter rules.

name (string) --
The name of the webhook.

targetPipeline (string) --
The name of the pipeline you want to connect to the webhook.

targetAction (string) --
The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.

filters (list) --
A list of rules applied to the body/payload sent in the POST request to a webhook URL. All defined rules must pass for the request to be accepted and the pipeline started.

(dict) --
The event criteria that specify when a webhook notification is sent to your URL.

jsonPath (string) --
A JsonPath expression that is applied to the body/payload of the webhook. The value selected by the JsonPath expression must match the value specified in the MatchEquals field. Otherwise, the request is ignored. For more information, see Java JsonPath implementation in GitHub.

matchEquals (string) --
The value selected by the JsonPath expression must match what is supplied in the MatchEquals field. Otherwise, the request is ignored. Properties from the target action configuration can be included as placeholders in this value by surrounding the action configuration key with curly brackets. For example, if the value supplied here is "refs/heads/{Branch}" and the target action has an action configuration property called "Branch" with a value of "master", the MatchEquals value is evaluated as "refs/heads/master". For a list of action configuration properties for built-in action types, see Pipeline Structure Reference Action Requirements .





authentication (string) --
Supported options are GITHUB_HMAC, IP, and UNAUTHENTICATED.

For information about the authentication scheme implemented by GITHUB_HMAC, see Securing your webhooks on the GitHub Developer website.
IP rejects webhooks trigger requests unless they originate from an IP address in the IP range whitelisted in the authentication configuration.
UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.


authenticationConfiguration (dict) --
Properties that configure the authentication applied to incoming webhook trigger requests. The required properties depend on the authentication type. For GITHUB_HMAC, only the SecretToken property must be set. For IP, only the AllowedIPRange property must be set to a valid CIDR range. For UNAUTHENTICATED, no properties can be set.

AllowedIPRange (string) --
The property used to configure acceptance of webhooks in an IP address range. For IP, only the AllowedIPRange property must be set. This property must be set to a valid CIDR range.

SecretToken (string) --
The property used to configure GitHub authentication. For GITHUB_HMAC, only the SecretToken property must be set.





url (string) --
A unique URL generated by CodePipeline. When a POST request is made to this URL, the defined pipeline is started as long as the body of the post request satisfies the defined authentication and filtering conditions. Deleting and re-creating a webhook makes the old URL invalid and generates a new one.

errorMessage (string) --
The text of the error message about the webhook.

errorCode (string) --
The number code of the error.

lastTriggered (datetime) --
The date and time a webhook was last successfully triggered, in timestamp format.

arn (string) --
The Amazon Resource Name (ARN) of the webhook.

tags (list) --
Specifies the tags applied to the webhook.

(dict) --
A tag is a key-value pair that is used to manage the resource.

key (string) --
The tag\'s key.

value (string) --
The tag\'s value.













Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.LimitExceededException
CodePipeline.Client.exceptions.InvalidWebhookFilterPatternException
CodePipeline.Client.exceptions.InvalidWebhookAuthenticationParametersException
CodePipeline.Client.exceptions.PipelineNotFoundException
CodePipeline.Client.exceptions.TooManyTagsException
CodePipeline.Client.exceptions.InvalidTagsException
CodePipeline.Client.exceptions.ConcurrentModificationException


    :return: {
        'webhook': {
            'definition': {
                'name': 'string',
                'targetPipeline': 'string',
                'targetAction': 'string',
                'filters': [
                    {
                        'jsonPath': 'string',
                        'matchEquals': 'string'
                    },
                ],
                'authentication': 'GITHUB_HMAC'|'IP'|'UNAUTHENTICATED',
                'authenticationConfiguration': {
                    'AllowedIPRange': 'string',
                    'SecretToken': 'string'
                }
            },
            'url': 'string',
            'errorMessage': 'string',
            'errorCode': 'string',
            'lastTriggered': datetime(2015, 1, 1),
            'arn': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    For information about the authentication scheme implemented by GITHUB_HMAC, see Securing your webhooks on the GitHub Developer website.
    IP rejects webhooks trigger requests unless they originate from an IP address in the IP range whitelisted in the authentication configuration.
    UNAUTHENTICATED accepts all webhook trigger requests regardless of origin.
    
    """
    pass

def register_webhook_with_third_party(webhookName=None):
    """
    Configures a connection between the webhook that was created and the external tool with events to be detected.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_webhook_with_third_party(
        webhookName='string'
    )
    
    
    :type webhookName: string
    :param webhookName: The name of an existing webhook created with PutWebhook to register with a supported third party.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.WebhookNotFoundException


    :return: {}
    
    
    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.WebhookNotFoundException
    
    """
    pass

def retry_stage_execution(pipelineName=None, stageName=None, pipelineExecutionId=None, retryMode=None):
    """
    Resumes the pipeline execution by retrying the last failed actions in a stage. You can retry a stage immediately if any of the actions in the stage fail. When you retry, all actions that are still in progress continue working, and failed actions are triggered again.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.retry_stage_execution(
        pipelineName='string',
        stageName='string',
        pipelineExecutionId='string',
        retryMode='FAILED_ACTIONS'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]\nThe name of the pipeline that contains the failed stage.\n

    :type stageName: string
    :param stageName: [REQUIRED]\nThe name of the failed stage to be retried.\n

    :type pipelineExecutionId: string
    :param pipelineExecutionId: [REQUIRED]\nThe ID of the pipeline execution in the failed stage to be retried. Use the GetPipelineState action to retrieve the current pipelineExecutionId of the failed stage\n

    :type retryMode: string
    :param retryMode: [REQUIRED]\nThe scope of the retry attempt. Currently, the only supported value is FAILED_ACTIONS.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'pipelineExecutionId': 'string'
}


Response Structure

(dict) --
Represents the output of a RetryStageExecution action.

pipelineExecutionId (string) --
The ID of the current workflow execution in the failed stage.







Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.PipelineNotFoundException
CodePipeline.Client.exceptions.StageNotFoundException
CodePipeline.Client.exceptions.StageNotRetryableException
CodePipeline.Client.exceptions.NotLatestPipelineExecutionException


    :return: {
        'pipelineExecutionId': 'string'
    }
    
    
    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.PipelineNotFoundException
    CodePipeline.Client.exceptions.StageNotFoundException
    CodePipeline.Client.exceptions.StageNotRetryableException
    CodePipeline.Client.exceptions.NotLatestPipelineExecutionException
    
    """
    pass

def start_pipeline_execution(name=None, clientRequestToken=None):
    """
    Starts the specified pipeline. Specifically, it begins processing the latest commit to the source location specified as part of the pipeline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_pipeline_execution(
        name='string',
        clientRequestToken='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the pipeline to start.\n

    :type clientRequestToken: string
    :param clientRequestToken: The system-generated unique ID used to identify a unique execution request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'pipelineExecutionId': 'string'
}


Response Structure

(dict) --
Represents the output of a StartPipelineExecution action.

pipelineExecutionId (string) --
The unique system-generated ID of the pipeline execution that was started.







Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.PipelineNotFoundException


    :return: {
        'pipelineExecutionId': 'string'
    }
    
    
    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.PipelineNotFoundException
    
    """
    pass

def stop_pipeline_execution(pipelineName=None, pipelineExecutionId=None, abandon=None, reason=None):
    """
    Stops the specified pipeline execution. You choose to either stop the pipeline execution by completing in-progress actions without starting subsequent actions, or by abandoning in-progress actions. While completing or abandoning in-progress actions, the pipeline execution is in a Stopping state. After all in-progress actions are completed or abandoned, the pipeline execution is in a Stopped state.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_pipeline_execution(
        pipelineName='string',
        pipelineExecutionId='string',
        abandon=True|False,
        reason='string'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]\nThe name of the pipeline to stop.\n

    :type pipelineExecutionId: string
    :param pipelineExecutionId: [REQUIRED]\nThe ID of the pipeline execution to be stopped in the current stage. Use the GetPipelineState action to retrieve the current pipelineExecutionId.\n

    :type abandon: boolean
    :param abandon: Use this option to stop the pipeline execution by abandoning, rather than finishing, in-progress actions.\n\nNote\nThis option can lead to failed or out-of-sequence tasks.\n\n

    :type reason: string
    :param reason: Use this option to enter comments, such as the reason the pipeline was stopped.

    :rtype: dict

ReturnsResponse Syntax
{
    'pipelineExecutionId': 'string'
}


Response Structure

(dict) --

pipelineExecutionId (string) --
The unique system-generated ID of the pipeline execution that was stopped.







Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.PipelineNotFoundException
CodePipeline.Client.exceptions.PipelineExecutionNotStoppableException
CodePipeline.Client.exceptions.DuplicatedStopRequestException


    :return: {
        'pipelineExecutionId': 'string'
    }
    
    
    :returns: 
    CodePipeline.Client.exceptions.ValidationException
    CodePipeline.Client.exceptions.PipelineNotFoundException
    CodePipeline.Client.exceptions.PipelineExecutionNotStoppableException
    CodePipeline.Client.exceptions.DuplicatedStopRequestException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource you want to add tags to.\n

    :type tags: list
    :param tags: [REQUIRED]\nThe tags you want to modify or add to the resource.\n\n(dict) --A tag is a key-value pair that is used to manage the resource.\n\nkey (string) -- [REQUIRED]The tag\'s key.\n\nvalue (string) -- [REQUIRED]The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.ResourceNotFoundException
CodePipeline.Client.exceptions.InvalidArnException
CodePipeline.Client.exceptions.TooManyTagsException
CodePipeline.Client.exceptions.InvalidTagsException
CodePipeline.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes tags from an AWS resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to remove tags from.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe list of keys for the tags to be removed from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.ResourceNotFoundException
CodePipeline.Client.exceptions.InvalidArnException
CodePipeline.Client.exceptions.InvalidTagsException
CodePipeline.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_pipeline(pipeline=None):
    """
    Updates a specified pipeline with edits or changes to its structure. Use a JSON file with the pipeline structure and UpdatePipeline to provide the full structure of the pipeline. Updating the pipeline increases the version number of the pipeline by 1.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_pipeline(
        pipeline={
            'name': 'string',
            'roleArn': 'string',
            'artifactStore': {
                'type': 'S3',
                'location': 'string',
                'encryptionKey': {
                    'id': 'string',
                    'type': 'KMS'
                }
            },
            'artifactStores': {
                'string': {
                    'type': 'S3',
                    'location': 'string',
                    'encryptionKey': {
                        'id': 'string',
                        'type': 'KMS'
                    }
                }
            },
            'stages': [
                {
                    'name': 'string',
                    'blockers': [
                        {
                            'name': 'string',
                            'type': 'Schedule'
                        },
                    ],
                    'actions': [
                        {
                            'name': 'string',
                            'actionTypeId': {
                                'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                                'owner': 'AWS'|'ThirdParty'|'Custom',
                                'provider': 'string',
                                'version': 'string'
                            },
                            'runOrder': 123,
                            'configuration': {
                                'string': 'string'
                            },
                            'outputArtifacts': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'inputArtifacts': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'roleArn': 'string',
                            'region': 'string',
                            'namespace': 'string'
                        },
                    ]
                },
            ],
            'version': 123
        }
    )
    
    
    :type pipeline: dict
    :param pipeline: [REQUIRED]\nThe name of the pipeline to be updated.\n\nname (string) -- [REQUIRED]The name of the action to be performed.\n\nroleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no actionRoleArn , or to use to assume roles for actions with an actionRoleArn .\n\nartifactStore (dict) --Represents information about the S3 bucket where artifacts are stored for the pipeline.\n\nNote\nYou must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .\n\n\ntype (string) -- [REQUIRED]The type of the artifact store, such as S3.\n\nlocation (string) -- [REQUIRED]The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.\n\nencryptionKey (dict) --The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.\n\nid (string) -- [REQUIRED]The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN, or the alias ARN.\n\nNote\nAliases are recognized only in the account that created the customer master key (CMK). For cross-account actions, you can only use the key ID or key ARN to identify the key.\n\n\ntype (string) -- [REQUIRED]The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.\n\n\n\n\n\nartifactStores (dict) --A mapping of artifactStore objects and their corresponding AWS Regions. There must be an artifact store for the pipeline Region and for each cross-region action in the pipeline.\n\nNote\nYou must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .\n\n\n(string) --\n(dict) --The S3 bucket where artifacts for the pipeline are stored.\n\nNote\nYou must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .\n\n\ntype (string) -- [REQUIRED]The type of the artifact store, such as S3.\n\nlocation (string) -- [REQUIRED]The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.\n\nencryptionKey (dict) --The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.\n\nid (string) -- [REQUIRED]The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN, or the alias ARN.\n\nNote\nAliases are recognized only in the account that created the customer master key (CMK). For cross-account actions, you can only use the key ID or key ARN to identify the key.\n\n\ntype (string) -- [REQUIRED]The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.\n\n\n\n\n\n\n\n\n\nstages (list) -- [REQUIRED]The stage in which to perform the action.\n\n(dict) --Represents information about a stage and its definition.\n\nname (string) -- [REQUIRED]The name of the stage.\n\nblockers (list) --Reserved for future use.\n\n(dict) --Reserved for future use.\n\nname (string) -- [REQUIRED]Reserved for future use.\n\ntype (string) -- [REQUIRED]Reserved for future use.\n\n\n\n\n\nactions (list) -- [REQUIRED]The actions included in a stage.\n\n(dict) --Represents information about an action declaration.\n\nname (string) -- [REQUIRED]The action declaration\'s name.\n\nactionTypeId (dict) -- [REQUIRED]Specifies the action type and the provider of the action.\n\ncategory (string) -- [REQUIRED]A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.\n\nowner (string) -- [REQUIRED]The creator of the action being called.\n\nprovider (string) -- [REQUIRED]The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see Valid Action Types and Providers in CodePipeline .\n\nversion (string) -- [REQUIRED]A string that describes the action version.\n\n\n\nrunOrder (integer) --The order in which actions are run.\n\nconfiguration (dict) --The action\'s configuration. These are key-value pairs that specify input values for an action. For more information, see Action Structure Requirements in CodePipeline . For the list of configuration properties for the AWS CloudFormation action type in CodePipeline, see Configuration Properties Reference in the AWS CloudFormation User Guide . For template snippets with examples, see Using Parameter Override Functions with CodePipeline Pipelines in the AWS CloudFormation User Guide .\nThe values can be represented in either JSON or YAML format. For example, the JSON configuration item format is as follows:\n\nJSON:'Configuration' : { Key : Value },\n\n\n(string) --\n(string) --\n\n\n\n\noutputArtifacts (list) --The name or ID of the result of the action declaration, such as a test or build artifact.\n\n(dict) --Represents information about the output of an action.\n\nname (string) -- [REQUIRED]The name of the output of an artifact, such as 'My App'.\nThe input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.\nOutput artifact names must be unique within a pipeline.\n\n\n\n\n\ninputArtifacts (list) --The name or ID of the artifact consumed by the action, such as a test or build artifact.\n\n(dict) --Represents information about an artifact to be worked on, such as a test or build artifact.\n\nname (string) -- [REQUIRED]The name of the artifact to be worked on (for example, 'My App').\nThe input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.\n\n\n\n\n\nroleArn (string) --The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline.\n\nregion (string) --The action declaration\'s AWS Region, such as us-east-1.\n\nnamespace (string) --The variable namespace associated with the action. All variables produced as output by this action fall under this namespace.\n\n\n\n\n\n\n\n\n\nversion (integer) --The version number of the pipeline. A new pipeline always has a version number of 1. This number is incremented when a pipeline is updated.\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'pipeline': {
        'name': 'string',
        'roleArn': 'string',
        'artifactStore': {
            'type': 'S3',
            'location': 'string',
            'encryptionKey': {
                'id': 'string',
                'type': 'KMS'
            }
        },
        'artifactStores': {
            'string': {
                'type': 'S3',
                'location': 'string',
                'encryptionKey': {
                    'id': 'string',
                    'type': 'KMS'
                }
            }
        },
        'stages': [
            {
                'name': 'string',
                'blockers': [
                    {
                        'name': 'string',
                        'type': 'Schedule'
                    },
                ],
                'actions': [
                    {
                        'name': 'string',
                        'actionTypeId': {
                            'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                            'owner': 'AWS'|'ThirdParty'|'Custom',
                            'provider': 'string',
                            'version': 'string'
                        },
                        'runOrder': 123,
                        'configuration': {
                            'string': 'string'
                        },
                        'outputArtifacts': [
                            {
                                'name': 'string'
                            },
                        ],
                        'inputArtifacts': [
                            {
                                'name': 'string'
                            },
                        ],
                        'roleArn': 'string',
                        'region': 'string',
                        'namespace': 'string'
                    },
                ]
            },
        ],
        'version': 123
    }
}


Response Structure

(dict) --Represents the output of an UpdatePipeline action.

pipeline (dict) --The structure of the updated pipeline.

name (string) --The name of the action to be performed.

roleArn (string) --The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no actionRoleArn , or to use to assume roles for actions with an actionRoleArn .

artifactStore (dict) --Represents information about the S3 bucket where artifacts are stored for the pipeline.

Note
You must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .


type (string) --The type of the artifact store, such as S3.

location (string) --The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

encryptionKey (dict) --The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.

id (string) --The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN, or the alias ARN.

Note
Aliases are recognized only in the account that created the customer master key (CMK). For cross-account actions, you can only use the key ID or key ARN to identify the key.


type (string) --The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.





artifactStores (dict) --A mapping of artifactStore objects and their corresponding AWS Regions. There must be an artifact store for the pipeline Region and for each cross-region action in the pipeline.

Note
You must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .


(string) --
(dict) --The S3 bucket where artifacts for the pipeline are stored.

Note
You must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores .


type (string) --The type of the artifact store, such as S3.

location (string) --The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.

encryptionKey (dict) --The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.

id (string) --The ID used to identify the key. For an AWS KMS key, you can use the key ID, the key ARN, or the alias ARN.

Note
Aliases are recognized only in the account that created the customer master key (CMK). For cross-account actions, you can only use the key ID or key ARN to identify the key.


type (string) --The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to \'KMS\'.









stages (list) --The stage in which to perform the action.

(dict) --Represents information about a stage and its definition.

name (string) --The name of the stage.

blockers (list) --Reserved for future use.

(dict) --Reserved for future use.

name (string) --Reserved for future use.

type (string) --Reserved for future use.





actions (list) --The actions included in a stage.

(dict) --Represents information about an action declaration.

name (string) --The action declaration\'s name.

actionTypeId (dict) --Specifies the action type and the provider of the action.

category (string) --A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.

owner (string) --The creator of the action being called.

provider (string) --The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy. For more information, see Valid Action Types and Providers in CodePipeline .

version (string) --A string that describes the action version.



runOrder (integer) --The order in which actions are run.

configuration (dict) --The action\'s configuration. These are key-value pairs that specify input values for an action. For more information, see Action Structure Requirements in CodePipeline . For the list of configuration properties for the AWS CloudFormation action type in CodePipeline, see Configuration Properties Reference in the AWS CloudFormation User Guide . For template snippets with examples, see Using Parameter Override Functions with CodePipeline Pipelines in the AWS CloudFormation User Guide .
The values can be represented in either JSON or YAML format. For example, the JSON configuration item format is as follows:

JSON:"Configuration" : { Key : Value },


(string) --
(string) --




outputArtifacts (list) --The name or ID of the result of the action declaration, such as a test or build artifact.

(dict) --Represents information about the output of an action.

name (string) --The name of the output of an artifact, such as "My App".
The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
Output artifact names must be unique within a pipeline.





inputArtifacts (list) --The name or ID of the artifact consumed by the action, such as a test or build artifact.

(dict) --Represents information about an artifact to be worked on, such as a test or build artifact.

name (string) --The name of the artifact to be worked on (for example, "My App").
The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.





roleArn (string) --The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline.

region (string) --The action declaration\'s AWS Region, such as us-east-1.

namespace (string) --The variable namespace associated with the action. All variables produced as output by this action fall under this namespace.









version (integer) --The version number of the pipeline. A new pipeline always has a version number of 1. This number is incremented when a pipeline is updated.








Exceptions

CodePipeline.Client.exceptions.ValidationException
CodePipeline.Client.exceptions.InvalidStageDeclarationException
CodePipeline.Client.exceptions.InvalidActionDeclarationException
CodePipeline.Client.exceptions.InvalidBlockerDeclarationException
CodePipeline.Client.exceptions.InvalidStructureException
CodePipeline.Client.exceptions.LimitExceededException


    :return: {
        'pipeline': {
            'name': 'string',
            'roleArn': 'string',
            'artifactStore': {
                'type': 'S3',
                'location': 'string',
                'encryptionKey': {
                    'id': 'string',
                    'type': 'KMS'
                }
            },
            'artifactStores': {
                'string': {
                    'type': 'S3',
                    'location': 'string',
                    'encryptionKey': {
                        'id': 'string',
                        'type': 'KMS'
                    }
                }
            },
            'stages': [
                {
                    'name': 'string',
                    'blockers': [
                        {
                            'name': 'string',
                            'type': 'Schedule'
                        },
                    ],
                    'actions': [
                        {
                            'name': 'string',
                            'actionTypeId': {
                                'category': 'Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
                                'owner': 'AWS'|'ThirdParty'|'Custom',
                                'provider': 'string',
                                'version': 'string'
                            },
                            'runOrder': 123,
                            'configuration': {
                                'string': 'string'
                            },
                            'outputArtifacts': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'inputArtifacts': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'roleArn': 'string',
                            'region': 'string',
                            'namespace': 'string'
                        },
                    ]
                },
            ],
            'version': 123
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

