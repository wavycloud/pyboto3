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


def acknowledge_job(jobId=None, nonce=None):
    """
    :param jobId: [REQUIRED]
            The unique system-generated ID of the job for which you want to confirm receipt.
            
    :type jobId: string
    :param nonce: [REQUIRED]
            A system-generated random number that AWS CodePipeline uses to ensure that the job is being worked on by only one job worker. This number must be returned in the response.
            
    :type nonce: string
    """
    pass


def acknowledge_third_party_job(jobId=None, nonce=None, clientToken=None):
    """
    :param jobId: [REQUIRED]
            The unique system-generated ID of the job.
            
    :type jobId: string
    :param nonce: [REQUIRED]
            A system-generated random number that AWS CodePipeline uses to ensure that the job is being worked on by only one job worker. This number must be returned in the response.
            
    :type nonce: string
    :param clientToken: [REQUIRED]
            The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
            
    :type clientToken: string
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


def create_custom_action_type(category=None, provider=None, version=None, settings=None, configurationProperties=None,
                              inputArtifactDetails=None, outputArtifactDetails=None):
    """
    :param category: [REQUIRED]
            The category of the custom action, such as a build action or a test action.
            Note
            Although Source and Approval are listed as valid values, they are not currently functional. These values are reserved for future use.
            
    :type category: string
    :param provider: [REQUIRED]
            The provider of the service used in the custom action, such as AWS CodeDeploy.
            
    :type provider: string
    :param version: [REQUIRED]
            The version identifier of the custom action.
            
    :type version: string
    :param settings: Returns information about the settings for an action type.
            thirdPartyConfigurationUrl (string) --The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.
            entityUrlTemplate (string) --The URL returned to the AWS CodePipeline console that provides a deep link to the resources of the external system, such as the configuration page for an AWS CodeDeploy deployment group. This link is provided as part of the action display within the pipeline.
            executionUrlTemplate (string) --The URL returned to the AWS CodePipeline console that contains a link to the top-level landing page for the external system, such as console page for AWS CodeDeploy. This link is shown on the pipeline view page in the AWS CodePipeline console and provides a link to the execution entity of the external action.
            revisionUrlTemplate (string) --The URL returned to the AWS CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.
            
    :type settings: dict
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
            
            
    :type configurationProperties: list
    :param inputArtifactDetails: [REQUIRED]
            Returns information about the details of an artifact.
            minimumCount (integer) -- [REQUIRED]The minimum number of artifacts allowed for the action type.
            maximumCount (integer) -- [REQUIRED]The maximum number of artifacts allowed for the action type.
            
    :type inputArtifactDetails: dict
    :param outputArtifactDetails: [REQUIRED]
            Returns information about the details of an artifact.
            minimumCount (integer) -- [REQUIRED]The minimum number of artifacts allowed for the action type.
            maximumCount (integer) -- [REQUIRED]The maximum number of artifacts allowed for the action type.
            
    :type outputArtifactDetails: dict
    """
    pass


def create_pipeline(pipeline=None):
    """
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
            Return typedict
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
            Response Structure
            (dict) --Represents the output of a create pipeline action.
            pipeline (dict) --Represents the structure of actions and stages to be performed in the pipeline.
            name (string) --The name of the action to be performed.
            roleArn (string) --The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no actionRoleArn, or to use to assume roles for actions with an actionRoleArn.
            artifactStore (dict) --The Amazon S3 location where artifacts are stored for the pipeline. If this Amazon S3 bucket is created manually, it must meet the requirements for AWS CodePipeline. For more information, see the Concepts .
            type (string) --The type of the artifact store, such as S3.
            location (string) --The location for storing the artifacts for a pipeline, such as an S3 bucket or folder.
            encryptionKey (dict) --The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.
            id (string) --The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
            type (string) --The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to 'KMS'.
            
            stages (list) --The stage in which to perform the action.
            (dict) --Represents information about a stage and its definition.
            name (string) --The name of the stage.
            blockers (list) --Reserved for future use.
            (dict) --Reserved for future use.
            name (string) --Reserved for future use.
            type (string) --Reserved for future use.
            
            actions (list) --The actions included in a stage.
            (dict) --Represents information about an action declaration.
            name (string) --The action declaration's name.
            actionTypeId (dict) --The configuration information for the action type.
            category (string) --A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
            owner (string) --The creator of the action being called.
            provider (string) --The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
            version (string) --A string that identifies the action type.
            runOrder (integer) --The order in which actions are run.
            configuration (dict) --The action declaration's configuration.
            (string) --
            (string) --
            
            outputArtifacts (list) --The name or ID of the result of the action declaration, such as a test or build artifact.
            (dict) --Represents information about the output of an action.
            name (string) --The name of the output of an artifact, such as 'My App'.
            The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
            Output artifact names must be unique within a pipeline.
            
            inputArtifacts (list) --The name or ID of the artifact consumed by the action, such as a test or build artifact.
            (dict) --Represents information about an artifact to be worked on, such as a test or build artifact.
            name (string) --The name of the artifact to be worked on, for example, 'My App'.
            The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
            
            roleArn (string) --The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.
            
            
            version (integer) --The version number of the pipeline. A new pipeline always has a version number of 1. This number is automatically incremented when a pipeline is updated.
            
            
            
    :type pipeline: dict
    """
    pass


def delete_custom_action_type(category=None, provider=None, version=None):
    """
    :param category: [REQUIRED]
            The category of the custom action that you want to delete, such as source or deploy.
            
    :type category: string
    :param provider: [REQUIRED]
            The provider of the service used in the custom action, such as AWS CodeDeploy.
            
    :type provider: string
    :param version: [REQUIRED]
            The version of the custom action to delete.
            
    :type version: string
    """
    pass


def delete_pipeline(name=None):
    """
    :param name: [REQUIRED]
            The name of the pipeline to be deleted.
            ReturnsNone
            
    :type name: string
    """
    pass


def disable_stage_transition(pipelineName=None, stageName=None, transitionType=None, reason=None):
    """
    :param pipelineName: [REQUIRED]
            The name of the pipeline in which you want to disable the flow of artifacts from one stage to another.
            
    :type pipelineName: string
    :param stageName: [REQUIRED]
            The name of the stage where you want to disable the inbound or outbound transition of artifacts.
            
    :type stageName: string
    :param transitionType: [REQUIRED]
            Specifies whether artifacts will be prevented from transitioning into the stage and being processed by the actions in that stage (inbound), or prevented from transitioning from the stage after they have been processed by the actions in that stage (outbound).
            
    :type transitionType: string
    :param reason: [REQUIRED]
            The reason given to the user why a stage is disabled, such as waiting for manual approval or manual tests. This message is displayed in the pipeline console UI.
            
    :type reason: string
    """
    pass


def enable_stage_transition(pipelineName=None, stageName=None, transitionType=None):
    """
    :param pipelineName: [REQUIRED]
            The name of the pipeline in which you want to enable the flow of artifacts from one stage to another.
            
    :type pipelineName: string
    :param stageName: [REQUIRED]
            The name of the stage where you want to enable the transition of artifacts, either into the stage (inbound) or from that stage to the next stage (outbound).
            
    :type stageName: string
    :param transitionType: [REQUIRED]
            Specifies whether artifacts will be allowed to enter the stage and be processed by the actions in that stage (inbound) or whether already-processed artifacts will be allowed to transition to the next stage (outbound).
            
    :type transitionType: string
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


def get_job_details(jobId=None):
    """
    :param jobId: [REQUIRED]
            The unique system-generated ID for the job.
            Return typedict
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
            Response Structure
            (dict) --Represents the output of a get job details action.
            jobDetails (dict) --The details of the job.
            Note
            If AWSSessionCredentials is used, a long-running job can call GetJobDetails again to obtain new credentials.
            id (string) --The unique system-generated ID of the job.
            data (dict) --Represents additional information about a job required for a job worker to complete the job.
            actionTypeId (dict) --Represents information about an action type.
            category (string) --A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
            owner (string) --The creator of the action being called.
            provider (string) --The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
            version (string) --A string that identifies the action type.
            actionConfiguration (dict) --Represents information about an action configuration.
            configuration (dict) --The configuration data for the action.
            (string) --
            (string) --
            
            pipelineContext (dict) --Represents information about a pipeline to a job worker.
            pipelineName (string) --The name of the pipeline. This is a user-specified value. Pipeline names must be unique across all pipeline names under an Amazon Web Services account.
            stage (dict) --The stage of the pipeline.
            name (string) --The name of the stage.
            action (dict) --Represents the context of an action within the stage of a pipeline to a job worker.
            name (string) --The name of the action within the context of a job.
            
            inputArtifacts (list) --The artifact supplied to the job.
            (dict) --Represents information about an artifact that will be worked upon by actions in the pipeline.
            name (string) --The artifact's name.
            revision (string) --The artifact's revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).
            location (dict) --The location of an artifact.
            type (string) --The type of artifact in the location.
            s3Location (dict) --The Amazon S3 bucket that contains the artifact.
            bucketName (string) --The name of the Amazon S3 bucket.
            objectKey (string) --The key of the object in the Amazon S3 bucket, which uniquely identifies the object in the bucket.
            
            
            outputArtifacts (list) --The output of the job.
            (dict) --Represents information about an artifact that will be worked upon by actions in the pipeline.
            name (string) --The artifact's name.
            revision (string) --The artifact's revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).
            location (dict) --The location of an artifact.
            type (string) --The type of artifact in the location.
            s3Location (dict) --The Amazon S3 bucket that contains the artifact.
            bucketName (string) --The name of the Amazon S3 bucket.
            objectKey (string) --The key of the object in the Amazon S3 bucket, which uniquely identifies the object in the bucket.
            
            
            artifactCredentials (dict) --Represents an AWS session credentials object. These credentials are temporary credentials that are issued by AWS Secure Token Service (STS). They can be used to access input and output artifacts in the Amazon S3 bucket used to store artifact for the pipeline in AWS CodePipeline.
            accessKeyId (string) --The access key for the session.
            secretAccessKey (string) --The secret access key for the session.
            sessionToken (string) --The token for the session.
            continuationToken (string) --A system-generated token, such as a AWS CodeDeploy deployment ID, that a job requires in order to continue the job asynchronously.
            encryptionKey (dict) --Represents information about the key used to encrypt data in the artifact store, such as an AWS Key Management Service (AWS KMS) key.
            id (string) --The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
            type (string) --The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to 'KMS'.
            
            accountId (string) --The AWS account ID associated with the job.
            
            
            
    :type jobId: string
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


def get_pipeline(name=None, version=None):
    """
    :param name: [REQUIRED]
            The name of the pipeline for which you want to get information. Pipeline names must be unique under an Amazon Web Services (AWS) user account.
            
    :type name: string
    :param version: The version number of the pipeline. If you do not specify a version, defaults to the most current version.
    :type version: integer
    """
    pass


def get_pipeline_execution(pipelineName=None, pipelineExecutionId=None):
    """
    :param pipelineName: [REQUIRED]
            The name of the pipeline about which you want to get execution details.
            
    :type pipelineName: string
    :param pipelineExecutionId: [REQUIRED]
            The ID of the pipeline execution about which you want to get execution details.
            
    :type pipelineExecutionId: string
    """
    pass


def get_pipeline_state(name=None):
    """
    :param name: [REQUIRED]
            The name of the pipeline about which you want to get information.
            Return typedict
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
            Response Structure
            (dict) --Represents the output of a get pipeline state action.
            pipelineName (string) --The name of the pipeline for which you want to get the state.
            pipelineVersion (integer) --The version number of the pipeline.
            Note
            A newly-created pipeline is always assigned a version number of 1 .
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
            revisionChangeId (string) --The unique identifier of the change that set the state to this revision, for example a deployment ID or timestamp.
            created (datetime) --The date and time when the most recent version of the action was created, in timestamp format.
            latestExecution (dict) --Represents information about the run of an action.
            status (string) --The status of the action, or for a completed action, the last status of the action.
            summary (string) --A summary of the run of the action.
            lastStatusChange (datetime) --The last status change of the action.
            token (string) --The system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the GetPipelineState command and is used to validate that the approval request corresponding to this token is still valid.
            lastUpdatedBy (string) --The ARN of the user who last changed the pipeline.
            externalExecutionId (string) --The external ID of the run of the action.
            externalExecutionUrl (string) --The URL of a resource external to AWS that will be used when running the action, for example an external repository URL.
            percentComplete (integer) --A percentage of completeness of the action as it runs.
            errorDetails (dict) --The details of an error returned by a URL external to AWS.
            code (string) --The system ID or error number code of the error.
            message (string) --The text of the error message.
            
            entityUrl (string) --A URL link for more information about the state of the action, such as a deployment group details page.
            revisionUrl (string) --A URL link for more information about the revision, such as a commit details page.
            
            latestExecution (dict) --Information about the latest execution in the stage, including its ID and status.
            pipelineExecutionId (string) --The ID of the pipeline execution associated with the stage.
            status (string) --The status of the stage, or for a completed stage, the last status of the stage.
            
            created (datetime) --The date and time the pipeline was created, in timestamp format.
            updated (datetime) --The date and time the pipeline was last updated, in timestamp format.
            
            
    :type name: string
    """
    pass


def get_third_party_job_details(jobId=None, clientToken=None):
    """
    :param jobId: [REQUIRED]
            The unique system-generated ID used for identifying the job.
            
    :type jobId: string
    :param clientToken: [REQUIRED]
            The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
            
    :type clientToken: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_action_types(actionOwnerFilter=None, nextToken=None):
    """
    :param actionOwnerFilter: Filters the list of action types to those created by a specified entity.
    :type actionOwnerFilter: string
    :param nextToken: An identifier that was returned from the previous list action types call, which can be used to return the next set of action types in the list.
    :type nextToken: string
    """
    pass


def list_pipelines(nextToken=None):
    """
    :param nextToken: An identifier that was returned from the previous list pipelines call, which can be used to return the next set of pipelines in the list.
            Return typedict
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
            (dict) --Represents the output of a list pipelines action.
            pipelines (list) --The list of pipelines.
            (dict) --Returns a summary of a pipeline.
            name (string) --The name of the pipeline.
            version (integer) --The version number of the pipeline.
            created (datetime) --The date and time the pipeline was created, in timestamp format.
            updated (datetime) --The date and time of the last update to the pipeline, in timestamp format.
            
            nextToken (string) --If the amount of returned information is significantly large, an identifier is also returned which can be used in a subsequent list pipelines call to return the next set of pipelines in the list.
            
            
    :type nextToken: string
    """
    pass


def poll_for_jobs(actionTypeId=None, maxBatchSize=None, queryParam=None):
    """
    :param actionTypeId: [REQUIRED]
            Represents information about an action type.
            category (string) -- [REQUIRED]A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
            owner (string) -- [REQUIRED]The creator of the action being called.
            provider (string) -- [REQUIRED]The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
            version (string) -- [REQUIRED]A string that identifies the action type.
            
    :type actionTypeId: dict
    :param maxBatchSize: The maximum number of jobs to return in a poll for jobs call.
    :type maxBatchSize: integer
    :param queryParam: A map of property names and values. For an action type with no queryable properties, this value must be null or an empty map. For an action type with a queryable property, you must supply that property as a key in the map. Only jobs whose action configuration matches the mapped value will be returned.
            (string) --
            (string) --
            
    :type queryParam: dict
    """
    pass


def poll_for_third_party_jobs(actionTypeId=None, maxBatchSize=None):
    """
    :param actionTypeId: [REQUIRED]
            Represents information about an action type.
            category (string) -- [REQUIRED]A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
            owner (string) -- [REQUIRED]The creator of the action being called.
            provider (string) -- [REQUIRED]The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
            version (string) -- [REQUIRED]A string that identifies the action type.
            
    :type actionTypeId: dict
    :param maxBatchSize: The maximum number of jobs to return in a poll for jobs call.
    :type maxBatchSize: integer
    """
    pass


def put_action_revision(pipelineName=None, stageName=None, actionName=None, actionRevision=None):
    """
    :param pipelineName: [REQUIRED]
            The name of the pipeline that will start processing the revision to the source.
            
    :type pipelineName: string
    :param stageName: [REQUIRED]
            The name of the stage that contains the action that will act upon the revision.
            
    :type stageName: string
    :param actionName: [REQUIRED]
            The name of the action that will process the revision.
            
    :type actionName: string
    :param actionRevision: [REQUIRED]
            Represents information about the version (or revision) of an action.
            revisionId (string) -- [REQUIRED]The system-generated unique ID that identifies the revision number of the action.
            revisionChangeId (string) -- [REQUIRED]The unique identifier of the change that set the state to this revision, for example a deployment ID or timestamp.
            created (datetime) -- [REQUIRED]The date and time when the most recent version of the action was created, in timestamp format.
            
    :type actionRevision: dict
    """
    pass


def put_approval_result(pipelineName=None, stageName=None, actionName=None, result=None, token=None):
    """
    :param pipelineName: [REQUIRED]
            The name of the pipeline that contains the action.
            
    :type pipelineName: string
    :param stageName: [REQUIRED]
            The name of the stage that contains the action.
            
    :type stageName: string
    :param actionName: [REQUIRED]
            The name of the action for which approval is requested.
            
    :type actionName: string
    :param result: [REQUIRED]
            Represents information about the result of the approval request.
            summary (string) -- [REQUIRED]The summary of the current status of the approval request.
            status (string) -- [REQUIRED]The response submitted by a reviewer assigned to an approval action request.
            
    :type result: dict
    :param token: [REQUIRED]
            The system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the GetPipelineState action and is used to validate that the approval request corresponding to this token is still valid.
            
    :type token: string
    """
    pass


def put_job_failure_result(jobId=None, failureDetails=None):
    """
    :param jobId: [REQUIRED]
            The unique system-generated ID of the job that failed. This is the same ID returned from PollForJobs.
            
    :type jobId: string
    :param failureDetails: [REQUIRED]
            The details about the failure of a job.
            type (string) -- [REQUIRED]The type of the failure.
            message (string) -- [REQUIRED]The message about the failure.
            externalExecutionId (string) --The external ID of the run of the action that failed.
            
    :type failureDetails: dict
    """
    pass


def put_job_success_result(jobId=None, currentRevision=None, continuationToken=None, executionDetails=None):
    """
    :param jobId: [REQUIRED]
            The unique system-generated ID of the job that succeeded. This is the same ID returned from PollForJobs.
            
    :type jobId: string
    :param currentRevision: The ID of the current revision of the artifact successfully worked upon by the job.
            revision (string) -- [REQUIRED]The revision ID of the current version of an artifact.
            changeIdentifier (string) -- [REQUIRED]The change identifier for the current revision.
            created (datetime) --The date and time when the most recent revision of the artifact was created, in timestamp format.
            revisionSummary (string) --The summary of the most recent revision of the artifact.
            
    :type currentRevision: dict
    :param continuationToken: A token generated by a job worker, such as an AWS CodeDeploy deployment ID, that a successful job provides to identify a custom action in progress. Future jobs will use this token in order to identify the running instance of the action. It can be reused to return additional information about the progress of the custom action. When the action is complete, no continuation token should be supplied.
    :type continuationToken: string
    :param executionDetails: The execution details of the successful job, such as the actions taken by the job worker.
            summary (string) --The summary of the current status of the actions.
            externalExecutionId (string) --The system-generated unique ID of this action used to identify this job worker in any external systems, such as AWS CodeDeploy.
            percentComplete (integer) --The percentage of work completed on the action, represented on a scale of zero to one hundred percent.
            
    :type executionDetails: dict
    """
    pass


def put_third_party_job_failure_result(jobId=None, clientToken=None, failureDetails=None):
    """
    :param jobId: [REQUIRED]
            The ID of the job that failed. This is the same ID returned from PollForThirdPartyJobs.
            
    :type jobId: string
    :param clientToken: [REQUIRED]
            The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
            
    :type clientToken: string
    :param failureDetails: [REQUIRED]
            Represents information about failure details.
            type (string) -- [REQUIRED]The type of the failure.
            message (string) -- [REQUIRED]The message about the failure.
            externalExecutionId (string) --The external ID of the run of the action that failed.
            
    :type failureDetails: dict
    """
    pass


def put_third_party_job_success_result(jobId=None, clientToken=None, currentRevision=None, continuationToken=None,
                                       executionDetails=None):
    """
    :param jobId: [REQUIRED]
            The ID of the job that successfully completed. This is the same ID returned from PollForThirdPartyJobs.
            
    :type jobId: string
    :param clientToken: [REQUIRED]
            The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
            
    :type clientToken: string
    :param currentRevision: Represents information about a current revision.
            revision (string) -- [REQUIRED]The revision ID of the current version of an artifact.
            changeIdentifier (string) -- [REQUIRED]The change identifier for the current revision.
            created (datetime) --The date and time when the most recent revision of the artifact was created, in timestamp format.
            revisionSummary (string) --The summary of the most recent revision of the artifact.
            
    :type currentRevision: dict
    :param continuationToken: A token generated by a job worker, such as an AWS CodeDeploy deployment ID, that a successful job provides to identify a partner action in progress. Future jobs will use this token in order to identify the running instance of the action. It can be reused to return additional information about the progress of the partner action. When the action is complete, no continuation token should be supplied.
    :type continuationToken: string
    :param executionDetails: The details of the actions taken and results produced on an artifact as it passes through stages in the pipeline.
            summary (string) --The summary of the current status of the actions.
            externalExecutionId (string) --The system-generated unique ID of this action used to identify this job worker in any external systems, such as AWS CodeDeploy.
            percentComplete (integer) --The percentage of work completed on the action, represented on a scale of zero to one hundred percent.
            
    :type executionDetails: dict
    """
    pass


def retry_stage_execution(pipelineName=None, stageName=None, pipelineExecutionId=None, retryMode=None):
    """
    :param pipelineName: [REQUIRED]
            The name of the pipeline that contains the failed stage.
            
    :type pipelineName: string
    :param stageName: [REQUIRED]
            The name of the failed stage to be retried.
            
    :type stageName: string
    :param pipelineExecutionId: [REQUIRED]
            The ID of the pipeline execution in the failed stage to be retried. Use the GetPipelineState action to retrieve the current pipelineExecutionId of the failed stage
            
    :type pipelineExecutionId: string
    :param retryMode: [REQUIRED]
            The scope of the retry attempt. Currently, the only supported value is FAILED_ACTIONS.
            
    :type retryMode: string
    """
    pass


def start_pipeline_execution(name=None):
    """
    :param name: [REQUIRED]
            The name of the pipeline to start.
            Return typedict
            ReturnsResponse Syntax{
              'pipelineExecutionId': 'string'
            }
            Response Structure
            (dict) --Represents the output of a start pipeline execution action.
            pipelineExecutionId (string) --The unique system-generated ID of the pipeline execution that was started.
            
            
    :type name: string
    """
    pass


def update_pipeline(pipeline=None):
    """
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
            Return typedict
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
            Response Structure
            (dict) --Represents the output of an update pipeline action.
            pipeline (dict) --The structure of the updated pipeline.
            name (string) --The name of the action to be performed.
            roleArn (string) --The Amazon Resource Name (ARN) for AWS CodePipeline to use to either perform actions with no actionRoleArn, or to use to assume roles for actions with an actionRoleArn.
            artifactStore (dict) --The Amazon S3 location where artifacts are stored for the pipeline. If this Amazon S3 bucket is created manually, it must meet the requirements for AWS CodePipeline. For more information, see the Concepts .
            type (string) --The type of the artifact store, such as S3.
            location (string) --The location for storing the artifacts for a pipeline, such as an S3 bucket or folder.
            encryptionKey (dict) --The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If this is undefined, the default key for Amazon S3 is used.
            id (string) --The ID used to identify the key. For an AWS KMS key, this is the key ID or key ARN.
            type (string) --The type of encryption key, such as an AWS Key Management Service (AWS KMS) key. When creating or updating a pipeline, the value must be set to 'KMS'.
            
            stages (list) --The stage in which to perform the action.
            (dict) --Represents information about a stage and its definition.
            name (string) --The name of the stage.
            blockers (list) --Reserved for future use.
            (dict) --Reserved for future use.
            name (string) --Reserved for future use.
            type (string) --Reserved for future use.
            
            actions (list) --The actions included in a stage.
            (dict) --Represents information about an action declaration.
            name (string) --The action declaration's name.
            actionTypeId (dict) --The configuration information for the action type.
            category (string) --A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
            owner (string) --The creator of the action being called.
            provider (string) --The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.
            version (string) --A string that identifies the action type.
            runOrder (integer) --The order in which actions are run.
            configuration (dict) --The action declaration's configuration.
            (string) --
            (string) --
            
            outputArtifacts (list) --The name or ID of the result of the action declaration, such as a test or build artifact.
            (dict) --Represents information about the output of an action.
            name (string) --The name of the output of an artifact, such as 'My App'.
            The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
            Output artifact names must be unique within a pipeline.
            
            inputArtifacts (list) --The name or ID of the artifact consumed by the action, such as a test or build artifact.
            (dict) --Represents information about an artifact to be worked on, such as a test or build artifact.
            name (string) --The name of the artifact to be worked on, for example, 'My App'.
            The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
            
            roleArn (string) --The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.
            
            
            version (integer) --The version number of the pipeline. A new pipeline always has a version number of 1. This number is automatically incremented when a pipeline is updated.
            
            
            
    :type pipeline: dict
    """
    pass
