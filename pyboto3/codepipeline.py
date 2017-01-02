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
    Returns information about a specified job and whether that job has been received by the job worker. Only used for custom actions.
    See also: AWS API Documentation
    
    
    :example: response = client.acknowledge_job(
        jobId='string',
        nonce='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The unique system-generated ID of the job for which you want to confirm receipt.
            

    :type nonce: string
    :param nonce: [REQUIRED]
            A system-generated random number that AWS CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response of the PollForJobs request that returned this job.
            

    :rtype: dict
    :return: {
        'status': 'Created'|'Queued'|'Dispatched'|'InProgress'|'TimedOut'|'Succeeded'|'Failed'
    }
    
    
    """
    pass

def acknowledge_third_party_job(jobId=None, nonce=None, clientToken=None):
    """
    Confirms a job worker has received the specified job. Only used for partner actions.
    See also: AWS API Documentation
    
    
    :example: response = client.acknowledge_third_party_job(
        jobId='string',
        nonce='string',
        clientToken='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The unique system-generated ID of the job.
            

    :type nonce: string
    :param nonce: [REQUIRED]
            A system-generated random number that AWS CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response to a GetThirdPartyJobDetails request.
            

    :type clientToken: string
    :param clientToken: [REQUIRED]
            The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
            

    :rtype: dict
    :return: {
        'status': 'Created'|'Queued'|'Dispatched'|'InProgress'|'TimedOut'|'Succeeded'|'Failed'
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

def create_custom_action_type(category=None, provider=None, version=None, settings=None, configurationProperties=None, inputArtifactDetails=None, outputArtifactDetails=None):
    """
    Creates a new custom action that can be used in all pipelines associated with the AWS account. Only used for custom actions.
    See also: AWS API Documentation
    
    
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
        }
    )
    
    
    :type category: string
    :param category: [REQUIRED]
            The category of the custom action, such as a build action or a test action.
            Note
            Although Source and Approval are listed as valid values, they are not currently functional. These values are reserved for future use.
            

    :type provider: string
    :param provider: [REQUIRED]
            The provider of the service used in the custom action, such as AWS CodeDeploy.
            

    :type version: string
    :param version: [REQUIRED]
            The version identifier of the custom action.
            

    :type settings: dict
    :param settings: Returns information about the settings for an action type.
            thirdPartyConfigurationUrl (string) --The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.
            entityUrlTemplate (string) --The URL returned to the AWS CodePipeline console that provides a deep link to the resources of the external system, such as the configuration page for an AWS CodeDeploy deployment group. This link is provided as part of the action display within the pipeline.
            executionUrlTemplate (string) --The URL returned to the AWS CodePipeline console that contains a link to the top-level landing page for the external system, such as console page for AWS CodeDeploy. This link is shown on the pipeline view page in the AWS CodePipeline console and provides a link to the execution entity of the external action.
            revisionUrlTemplate (string) --The URL returned to the AWS CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.
            

    :type configurationProperties: list
    :param configurationProperties: The configuration properties for the custom action.
            Note
            You can refer to a name in the configuration properties of the custom action within the URL templates by following the format of {Config:name}, as long as the configuration property is both required and not secret. For more information, see Create a Custom Action for a Pipeline .
            (dict) --Represents information about an action configuration property.
            name (string) -- [REQUIRED]The name of the action configuration property.
            required (boolean) -- [REQUIRED]Whether the configuration property is a required value.
            key (boolean) -- [REQUIRED]Whether the configuration property is a key.
            secret (boolean) -- [REQUIRED]Whether the configuration property is secret. Secrets are hidden from all calls except for GetJobDetails, GetThirdPartyJobDetails, PollForJobs, and PollForThirdPartyJobs.
            When updating a pipeline, passing * * * * * without changing any other values of the action will preserve the prior value of the secret.
            queryable (boolean) --Indicates that the proprety will be used in conjunction with PollForJobs. When creating a custom action, an action can have up to one queryable property. If it has one, that property must be both required and not secret.
            If you create a pipeline with a custom action type, and that custom action contains a queryable property, the value for that configuration property is subject to additional restrictions. The value must be less than or equal to twenty (20) characters. The value can contain only alphanumeric characters, underscores, and hyphens.
            description (string) --The description of the action configuration property that will be displayed to users.
            type (string) --The type of the configuration property.
            
            

    :type inputArtifactDetails: dict
    :param inputArtifactDetails: [REQUIRED]
            Returns information about the details of an artifact.
            minimumCount (integer) -- [REQUIRED]The minimum number of artifacts allowed for the action type.
            maximumCount (integer) -- [REQUIRED]The maximum number of artifacts allowed for the action type.
            

    :type outputArtifactDetails: dict
    :param outputArtifactDetails: [REQUIRED]
            Returns information about the details of an artifact.
            minimumCount (integer) -- [REQUIRED]The minimum number of artifacts allowed for the action type.
            maximumCount (integer) -- [REQUIRED]The maximum number of artifacts allowed for the action type.
            

    :rtype: dict
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
        }
    }
    
    
    """
    pass

def create_pipeline(pipeline=None):
    """
    Creates a pipeline.
    See also: AWS API Documentation
    
    
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
                            'roleArn': 'string'
                        },
                    ]
                },
            ],
            'version': 123
        }
    )
    
    
    :type pipeline: dict
    :param pipeline: [REQUIRED]
            Represents the structure of actions and stages to be performed in the pipeline.
            name (string) -- [REQUIRED]The name of the action to be performed.
            roleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no actionRoleArn, or to use to assume roles for actions with an actionRoleArn.
            artifactStore (dict) -- [REQUIRED]The Amazon S3 location where artifacts are stored for the pipeline. If this Amazon S3 bucket is created manually, it must meet the requirements for AWS CodePipeline. For more information, see the Concepts .
            type (string) -- [REQUIRED]The type of the artifact store, such as S3.
            location (string) -- [REQUIRED]The location for storing the artifacts for a pipeline, such as an S3 bucket or folder.
            encryptionKey (dict) --The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.
            id (string) -- [REQUIRED]The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
            type (string) -- [REQUIRED]The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to 'KMS'.
            
            stages (list) -- [REQUIRED]The stage in which to perform the action.
            (dict) --Represents information about a stage and its definition.
            name (string) -- [REQUIRED]The name of the stage.
            blockers (list) --Reserved for future use.
            (dict) --Reserved for future use.
            name (string) -- [REQUIRED]Reserved for future use.
            type (string) -- [REQUIRED]Reserved for future use.
            
            actions (list) -- [REQUIRED]The actions included in a stage.
            (dict) --Represents information about an action declaration.
            name (string) -- [REQUIRED]The action declaration's name.
            actionTypeId (dict) -- [REQUIRED]The configuration information for the action type.
            category (string) -- [REQUIRED]A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
            owner (string) -- [REQUIRED]The creator of the action being called.
            provider (string) -- [REQUIRED]The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
            version (string) -- [REQUIRED]A string that identifies the action type.
            runOrder (integer) --The order in which actions are run.
            configuration (dict) --The action declaration's configuration.
            (string) --
            (string) --
            
            outputArtifacts (list) --The name or ID of the result of the action declaration, such as a test or build artifact.
            (dict) --Represents information about the output of an action.
            name (string) -- [REQUIRED]The name of the output of an artifact, such as 'My App'.
            The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
            Output artifact names must be unique within a pipeline.
            
            inputArtifacts (list) --The name or ID of the artifact consumed by the action, such as a test or build artifact.
            (dict) --Represents information about an artifact to be worked on, such as a test or build artifact.
            name (string) -- [REQUIRED]The name of the artifact to be worked on, for example, 'My App'.
            The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
            
            roleArn (string) --The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.
            
            
            version (integer) --The version number of the pipeline. A new pipeline always has a version number of 1. This number is automatically incremented when a pipeline is updated.
            

    :rtype: dict
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
                            'roleArn': 'string'
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

def delete_custom_action_type(category=None, provider=None, version=None):
    """
    Marks a custom action as deleted. PollForJobs for the custom action will fail after the action is marked for deletion. Only used for custom actions.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_custom_action_type(
        category='Source'|'Build'|'Deploy'|'Test'|'Invoke'|'Approval',
        provider='string',
        version='string'
    )
    
    
    :type category: string
    :param category: [REQUIRED]
            The category of the custom action that you want to delete, such as source or deploy.
            

    :type provider: string
    :param provider: [REQUIRED]
            The provider of the service used in the custom action, such as AWS CodeDeploy.
            

    :type version: string
    :param version: [REQUIRED]
            The version of the custom action to delete.
            

    """
    pass

def delete_pipeline(name=None):
    """
    Deletes the specified pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_pipeline(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the pipeline to be deleted.
            

    """
    pass

def disable_stage_transition(pipelineName=None, stageName=None, transitionType=None, reason=None):
    """
    Prevents artifacts in a pipeline from transitioning to the next stage in the pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_stage_transition(
        pipelineName='string',
        stageName='string',
        transitionType='Inbound'|'Outbound',
        reason='string'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]
            The name of the pipeline in which you want to disable the flow of artifacts from one stage to another.
            

    :type stageName: string
    :param stageName: [REQUIRED]
            The name of the stage where you want to disable the inbound or outbound transition of artifacts.
            

    :type transitionType: string
    :param transitionType: [REQUIRED]
            Specifies whether artifacts will be prevented from transitioning into the stage and being processed by the actions in that stage (inbound), or prevented from transitioning from the stage after they have been processed by the actions in that stage (outbound).
            

    :type reason: string
    :param reason: [REQUIRED]
            The reason given to the user why a stage is disabled, such as waiting for manual approval or manual tests. This message is displayed in the pipeline console UI.
            

    """
    pass

def enable_stage_transition(pipelineName=None, stageName=None, transitionType=None):
    """
    Enables artifacts in a pipeline to transition to a stage in a pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_stage_transition(
        pipelineName='string',
        stageName='string',
        transitionType='Inbound'|'Outbound'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]
            The name of the pipeline in which you want to enable the flow of artifacts from one stage to another.
            

    :type stageName: string
    :param stageName: [REQUIRED]
            The name of the stage where you want to enable the transition of artifacts, either into the stage (inbound) or from that stage to the next stage (outbound).
            

    :type transitionType: string
    :param transitionType: [REQUIRED]
            Specifies whether artifacts will be allowed to enter the stage and be processed by the actions in that stage (inbound) or whether already-processed artifacts will be allowed to transition to the next stage (outbound).
            

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

def get_job_details(jobId=None):
    """
    Returns information about a job. Only used for custom actions.
    See also: AWS API Documentation
    
    
    :example: response = client.get_job_details(
        jobId='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The unique system-generated ID for the job.
            

    :rtype: dict
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
                        'name': 'string'
                    }
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

def get_pipeline(name=None, version=None):
    """
    Returns the metadata, structure, stages, and actions of a pipeline. Can be used to return the entire structure of a pipeline in JSON format, which can then be modified and used to update the pipeline structure with  UpdatePipeline .
    See also: AWS API Documentation
    
    
    :example: response = client.get_pipeline(
        name='string',
        version=123
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the pipeline for which you want to get information. Pipeline names must be unique under an Amazon Web Services (AWS) user account.
            

    :type version: integer
    :param version: The version number of the pipeline. If you do not specify a version, defaults to the most current version.

    :rtype: dict
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
                            'roleArn': 'string'
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

def get_pipeline_execution(pipelineName=None, pipelineExecutionId=None):
    """
    Returns information about an execution of a pipeline, including details about artifacts, the pipeline execution ID, and the name, version, and status of the pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.get_pipeline_execution(
        pipelineName='string',
        pipelineExecutionId='string'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]
            The name of the pipeline about which you want to get execution details.
            

    :type pipelineExecutionId: string
    :param pipelineExecutionId: [REQUIRED]
            The ID of the pipeline execution about which you want to get execution details.
            

    :rtype: dict
    :return: {
        'pipelineExecution': {
            'pipelineName': 'string',
            'pipelineVersion': 123,
            'pipelineExecutionId': 'string',
            'status': 'InProgress'|'Succeeded'|'Superseded'|'Failed',
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
    Succeeded: The pipeline execution completed successfully.
    Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution caught up and continued through the pipeline instead.
    Failed: The pipeline did not complete successfully.
    
    """
    pass

def get_pipeline_state(name=None):
    """
    Returns information about the state of a pipeline, including the stages and actions.
    See also: AWS API Documentation
    
    
    :example: response = client.get_pipeline_state(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the pipeline about which you want to get information.
            

    :rtype: dict
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
                            'status': 'InProgress'|'Succeeded'|'Failed',
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
                    'status': 'InProgress'|'Failed'|'Succeeded'
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
    Requests the details of a job for a third party action. Only used for partner actions.
    See also: AWS API Documentation
    
    
    :example: response = client.get_third_party_job_details(
        jobId='string',
        clientToken='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The unique system-generated ID used for identifying the job.
            

    :type clientToken: string
    :param clientToken: [REQUIRED]
            The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
            

    :rtype: dict
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
                        'name': 'string'
                    }
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

def get_waiter():
    """
    
    """
    pass

def list_action_types(actionOwnerFilter=None, nextToken=None):
    """
    Gets a summary of all AWS CodePipeline action types associated with your account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_action_types(
        actionOwnerFilter='AWS'|'ThirdParty'|'Custom',
        nextToken='string'
    )
    
    
    :type actionOwnerFilter: string
    :param actionOwnerFilter: Filters the list of action types to those created by a specified entity.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous list action types call, which can be used to return the next set of action types in the list.

    :rtype: dict
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
    
    
    """
    pass

def list_pipelines(nextToken=None):
    """
    Gets a summary of all of the pipelines associated with your account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_pipelines(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous list pipelines call, which can be used to return the next set of pipelines in the list.

    :rtype: dict
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

def poll_for_jobs(actionTypeId=None, maxBatchSize=None, queryParam=None):
    """
    Returns information about any jobs for AWS CodePipeline to act upon.
    See also: AWS API Documentation
    
    
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
    :param actionTypeId: [REQUIRED]
            Represents information about an action type.
            category (string) -- [REQUIRED]A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
            owner (string) -- [REQUIRED]The creator of the action being called.
            provider (string) -- [REQUIRED]The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
            version (string) -- [REQUIRED]A string that identifies the action type.
            

    :type maxBatchSize: integer
    :param maxBatchSize: The maximum number of jobs to return in a poll for jobs call.

    :type queryParam: dict
    :param queryParam: A map of property names and values. For an action type with no queryable properties, this value must be null or an empty map. For an action type with a queryable property, you must supply that property as a key in the map. Only jobs whose action configuration matches the mapped value will be returned.
            (string) --
            (string) --
            

    :rtype: dict
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
                            'name': 'string'
                        }
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
    Determines whether there are any third party jobs for a job worker to act on. Only used for partner actions.
    See also: AWS API Documentation
    
    
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
    :param actionTypeId: [REQUIRED]
            Represents information about an action type.
            category (string) -- [REQUIRED]A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
            owner (string) -- [REQUIRED]The creator of the action being called.
            provider (string) -- [REQUIRED]The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
            version (string) -- [REQUIRED]A string that identifies the action type.
            

    :type maxBatchSize: integer
    :param maxBatchSize: The maximum number of jobs to return in a poll for jobs call.

    :rtype: dict
    :return: {
        'jobs': [
            {
                'clientId': 'string',
                'jobId': 'string'
            },
        ]
    }
    
    
    """
    pass

def put_action_revision(pipelineName=None, stageName=None, actionName=None, actionRevision=None):
    """
    Provides information to AWS CodePipeline about new revisions to a source.
    See also: AWS API Documentation
    
    
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
    :param pipelineName: [REQUIRED]
            The name of the pipeline that will start processing the revision to the source.
            

    :type stageName: string
    :param stageName: [REQUIRED]
            The name of the stage that contains the action that will act upon the revision.
            

    :type actionName: string
    :param actionName: [REQUIRED]
            The name of the action that will process the revision.
            

    :type actionRevision: dict
    :param actionRevision: [REQUIRED]
            Represents information about the version (or revision) of an action.
            revisionId (string) -- [REQUIRED]The system-generated unique ID that identifies the revision number of the action.
            revisionChangeId (string) -- [REQUIRED]The unique identifier of the change that set the state to this revision, for example a deployment ID or timestamp.
            created (datetime) -- [REQUIRED]The date and time when the most recent version of the action was created, in timestamp format.
            

    :rtype: dict
    :return: {
        'newRevision': True|False,
        'pipelineExecutionId': 'string'
    }
    
    
    """
    pass

def put_approval_result(pipelineName=None, stageName=None, actionName=None, result=None, token=None):
    """
    Provides the response to a manual approval request to AWS CodePipeline. Valid responses include Approved and Rejected.
    See also: AWS API Documentation
    
    
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
    :param pipelineName: [REQUIRED]
            The name of the pipeline that contains the action.
            

    :type stageName: string
    :param stageName: [REQUIRED]
            The name of the stage that contains the action.
            

    :type actionName: string
    :param actionName: [REQUIRED]
            The name of the action for which approval is requested.
            

    :type result: dict
    :param result: [REQUIRED]
            Represents information about the result of the approval request.
            summary (string) -- [REQUIRED]The summary of the current status of the approval request.
            status (string) -- [REQUIRED]The response submitted by a reviewer assigned to an approval action request.
            

    :type token: string
    :param token: [REQUIRED]
            The system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the GetPipelineState action and is used to validate that the approval request corresponding to this token is still valid.
            

    :rtype: dict
    :return: {
        'approvedAt': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def put_job_failure_result(jobId=None, failureDetails=None):
    """
    Represents the failure of a job as returned to the pipeline by a job worker. Only used for custom actions.
    See also: AWS API Documentation
    
    
    :example: response = client.put_job_failure_result(
        jobId='string',
        failureDetails={
            'type': 'JobFailed'|'ConfigurationError'|'PermissionError'|'RevisionOutOfSync'|'RevisionUnavailable'|'SystemUnavailable',
            'message': 'string',
            'externalExecutionId': 'string'
        }
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The unique system-generated ID of the job that failed. This is the same ID returned from PollForJobs.
            

    :type failureDetails: dict
    :param failureDetails: [REQUIRED]
            The details about the failure of a job.
            type (string) -- [REQUIRED]The type of the failure.
            message (string) -- [REQUIRED]The message about the failure.
            externalExecutionId (string) --The external ID of the run of the action that failed.
            

    """
    pass

def put_job_success_result(jobId=None, currentRevision=None, continuationToken=None, executionDetails=None):
    """
    Represents the success of a job as returned to the pipeline by a job worker. Only used for custom actions.
    See also: AWS API Documentation
    
    
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
        }
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The unique system-generated ID of the job that succeeded. This is the same ID returned from PollForJobs.
            

    :type currentRevision: dict
    :param currentRevision: The ID of the current revision of the artifact successfully worked upon by the job.
            revision (string) -- [REQUIRED]The revision ID of the current version of an artifact.
            changeIdentifier (string) -- [REQUIRED]The change identifier for the current revision.
            created (datetime) --The date and time when the most recent revision of the artifact was created, in timestamp format.
            revisionSummary (string) --The summary of the most recent revision of the artifact.
            

    :type continuationToken: string
    :param continuationToken: A token generated by a job worker, such as an AWS CodeDeploy deployment ID, that a successful job provides to identify a custom action in progress. Future jobs will use this token in order to identify the running instance of the action. It can be reused to return additional information about the progress of the custom action. When the action is complete, no continuation token should be supplied.

    :type executionDetails: dict
    :param executionDetails: The execution details of the successful job, such as the actions taken by the job worker.
            summary (string) --The summary of the current status of the actions.
            externalExecutionId (string) --The system-generated unique ID of this action used to identify this job worker in any external systems, such as AWS CodeDeploy.
            percentComplete (integer) --The percentage of work completed on the action, represented on a scale of zero to one hundred percent.
            

    """
    pass

def put_third_party_job_failure_result(jobId=None, clientToken=None, failureDetails=None):
    """
    Represents the failure of a third party job as returned to the pipeline by a job worker. Only used for partner actions.
    See also: AWS API Documentation
    
    
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
    :param jobId: [REQUIRED]
            The ID of the job that failed. This is the same ID returned from PollForThirdPartyJobs.
            

    :type clientToken: string
    :param clientToken: [REQUIRED]
            The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
            

    :type failureDetails: dict
    :param failureDetails: [REQUIRED]
            Represents information about failure details.
            type (string) -- [REQUIRED]The type of the failure.
            message (string) -- [REQUIRED]The message about the failure.
            externalExecutionId (string) --The external ID of the run of the action that failed.
            

    """
    pass

def put_third_party_job_success_result(jobId=None, clientToken=None, currentRevision=None, continuationToken=None, executionDetails=None):
    """
    Represents the success of a third party job as returned to the pipeline by a job worker. Only used for partner actions.
    See also: AWS API Documentation
    
    
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
    :param jobId: [REQUIRED]
            The ID of the job that successfully completed. This is the same ID returned from PollForThirdPartyJobs.
            

    :type clientToken: string
    :param clientToken: [REQUIRED]
            The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
            

    :type currentRevision: dict
    :param currentRevision: Represents information about a current revision.
            revision (string) -- [REQUIRED]The revision ID of the current version of an artifact.
            changeIdentifier (string) -- [REQUIRED]The change identifier for the current revision.
            created (datetime) --The date and time when the most recent revision of the artifact was created, in timestamp format.
            revisionSummary (string) --The summary of the most recent revision of the artifact.
            

    :type continuationToken: string
    :param continuationToken: A token generated by a job worker, such as an AWS CodeDeploy deployment ID, that a successful job provides to identify a partner action in progress. Future jobs will use this token in order to identify the running instance of the action. It can be reused to return additional information about the progress of the partner action. When the action is complete, no continuation token should be supplied.

    :type executionDetails: dict
    :param executionDetails: The details of the actions taken and results produced on an artifact as it passes through stages in the pipeline.
            summary (string) --The summary of the current status of the actions.
            externalExecutionId (string) --The system-generated unique ID of this action used to identify this job worker in any external systems, such as AWS CodeDeploy.
            percentComplete (integer) --The percentage of work completed on the action, represented on a scale of zero to one hundred percent.
            

    """
    pass

def retry_stage_execution(pipelineName=None, stageName=None, pipelineExecutionId=None, retryMode=None):
    """
    Resumes the pipeline execution by retrying the last failed actions in a stage.
    See also: AWS API Documentation
    
    
    :example: response = client.retry_stage_execution(
        pipelineName='string',
        stageName='string',
        pipelineExecutionId='string',
        retryMode='FAILED_ACTIONS'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]
            The name of the pipeline that contains the failed stage.
            

    :type stageName: string
    :param stageName: [REQUIRED]
            The name of the failed stage to be retried.
            

    :type pipelineExecutionId: string
    :param pipelineExecutionId: [REQUIRED]
            The ID of the pipeline execution in the failed stage to be retried. Use the GetPipelineState action to retrieve the current pipelineExecutionId of the failed stage
            

    :type retryMode: string
    :param retryMode: [REQUIRED]
            The scope of the retry attempt. Currently, the only supported value is FAILED_ACTIONS.
            

    :rtype: dict
    :return: {
        'pipelineExecutionId': 'string'
    }
    
    
    """
    pass

def start_pipeline_execution(name=None):
    """
    Starts the specified pipeline. Specifically, it begins processing the latest commit to the source location specified as part of the pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.start_pipeline_execution(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the pipeline to start.
            

    :rtype: dict
    :return: {
        'pipelineExecutionId': 'string'
    }
    
    
    """
    pass

def update_pipeline(pipeline=None):
    """
    Updates a specified pipeline with edits or changes to its structure. Use a JSON file with the pipeline structure in conjunction with UpdatePipeline to provide the full structure of the pipeline. Updating the pipeline increases the version number of the pipeline by 1.
    See also: AWS API Documentation
    
    
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
                            'roleArn': 'string'
                        },
                    ]
                },
            ],
            'version': 123
        }
    )
    
    
    :type pipeline: dict
    :param pipeline: [REQUIRED]
            The name of the pipeline to be updated.
            name (string) -- [REQUIRED]The name of the action to be performed.
            roleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no actionRoleArn, or to use to assume roles for actions with an actionRoleArn.
            artifactStore (dict) -- [REQUIRED]The Amazon S3 location where artifacts are stored for the pipeline. If this Amazon S3 bucket is created manually, it must meet the requirements for AWS CodePipeline. For more information, see the Concepts .
            type (string) -- [REQUIRED]The type of the artifact store, such as S3.
            location (string) -- [REQUIRED]The location for storing the artifacts for a pipeline, such as an S3 bucket or folder.
            encryptionKey (dict) --The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.
            id (string) -- [REQUIRED]The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
            type (string) -- [REQUIRED]The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to 'KMS'.
            
            stages (list) -- [REQUIRED]The stage in which to perform the action.
            (dict) --Represents information about a stage and its definition.
            name (string) -- [REQUIRED]The name of the stage.
            blockers (list) --Reserved for future use.
            (dict) --Reserved for future use.
            name (string) -- [REQUIRED]Reserved for future use.
            type (string) -- [REQUIRED]Reserved for future use.
            
            actions (list) -- [REQUIRED]The actions included in a stage.
            (dict) --Represents information about an action declaration.
            name (string) -- [REQUIRED]The action declaration's name.
            actionTypeId (dict) -- [REQUIRED]The configuration information for the action type.
            category (string) -- [REQUIRED]A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
            owner (string) -- [REQUIRED]The creator of the action being called.
            provider (string) -- [REQUIRED]The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
            version (string) -- [REQUIRED]A string that identifies the action type.
            runOrder (integer) --The order in which actions are run.
            configuration (dict) --The action declaration's configuration.
            (string) --
            (string) --
            
            outputArtifacts (list) --The name or ID of the result of the action declaration, such as a test or build artifact.
            (dict) --Represents information about the output of an action.
            name (string) -- [REQUIRED]The name of the output of an artifact, such as 'My App'.
            The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
            Output artifact names must be unique within a pipeline.
            
            inputArtifacts (list) --The name or ID of the artifact consumed by the action, such as a test or build artifact.
            (dict) --Represents information about an artifact to be worked on, such as a test or build artifact.
            name (string) -- [REQUIRED]The name of the artifact to be worked on, for example, 'My App'.
            The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
            
            roleArn (string) --The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.
            
            
            version (integer) --The version number of the pipeline. A new pipeline always has a version number of 1. This number is automatically incremented when a pipeline is updated.
            

    :rtype: dict
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
                            'roleArn': 'string'
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

