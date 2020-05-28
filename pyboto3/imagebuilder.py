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

def cancel_image_creation(imageBuildVersionArn=None, clientToken=None):
    """
    CancelImageCreation cancels the creation of Image. This operation can only be used on images in a non-terminal state.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_image_creation(
        imageBuildVersionArn='string',
        clientToken='string'
    )
    
    
    :type imageBuildVersionArn: string
    :param imageBuildVersionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image whose creation you want to cancel.\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe idempotency token used to make this request idempotent.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'clientToken': 'string',
    'imageBuildVersionArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

clientToken (string) --
The idempotency token used to make this request idempotent.

imageBuildVersionArn (string) --
The Amazon Resource Name (ARN) of the image whose creation has been cancelled.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.IdempotentParameterMismatchException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceInUseException


    :return: {
        'requestId': 'string',
        'clientToken': 'string',
        'imageBuildVersionArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.IdempotentParameterMismatchException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    imagebuilder.Client.exceptions.ResourceInUseException
    
    """
    pass

def create_component(name=None, semanticVersion=None, description=None, changeDescription=None, platform=None, supportedOsVersions=None, data=None, uri=None, kmsKeyId=None, tags=None, clientToken=None):
    """
    Creates a new component that can be used to build, validate, test, and assess your image.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_component(
        name='string',
        semanticVersion='string',
        description='string',
        changeDescription='string',
        platform='Windows'|'Linux',
        supportedOsVersions=[
            'string',
        ],
        data='string',
        uri='string',
        kmsKeyId='string',
        tags={
            'string': 'string'
        },
        clientToken='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the component.\n

    :type semanticVersion: string
    :param semanticVersion: [REQUIRED]\nThe semantic version of the component. This version follows the semantic version syntax. For example, major.minor.patch. This could be versioned like software (2.0.1) or like a date (2019.12.01).\n

    :type description: string
    :param description: The description of the component. Describes the contents of the component.

    :type changeDescription: string
    :param changeDescription: The change description of the component. Describes what change has been made in this version, or what makes this version different from other versions of this component.

    :type platform: string
    :param platform: [REQUIRED]\nThe platform of the component.\n

    :type supportedOsVersions: list
    :param supportedOsVersions: The operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the parent image OS version during image recipe creation.\n\n(string) --\n\n

    :type data: string
    :param data: The data of the component. Used to specify the data inline. Either data or uri can be used to specify the data within the component.

    :type uri: string
    :param uri: The uri of the component. Must be an S3 URL and the requester must have permission to access the S3 bucket. If you use S3, you can specify component content up to your service quota. Either data or uri can be used to specify the data within the component.

    :type kmsKeyId: string
    :param kmsKeyId: The ID of the KMS key that should be used to encrypt this component.

    :type tags: dict
    :param tags: The tags of the component.\n\n(string) --\n(string) --\n\n\n\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe idempotency token of the component.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'clientToken': 'string',
    'componentBuildVersionArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

clientToken (string) --
The idempotency token used to make this request idempotent.

componentBuildVersionArn (string) --
The Amazon Resource Name (ARN) of the component that was created by this request.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.IdempotentParameterMismatchException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.InvalidVersionNumberException
imagebuilder.Client.exceptions.ResourceInUseException
imagebuilder.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'requestId': 'string',
        'clientToken': 'string',
        'componentBuildVersionArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.IdempotentParameterMismatchException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    imagebuilder.Client.exceptions.InvalidVersionNumberException
    imagebuilder.Client.exceptions.ResourceInUseException
    imagebuilder.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def create_distribution_configuration(name=None, description=None, distributions=None, tags=None, clientToken=None):
    """
    Creates a new distribution configuration. Distribution configurations define and configure the outputs of your pipeline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_distribution_configuration(
        name='string',
        description='string',
        distributions=[
            {
                'region': 'string',
                'amiDistributionConfiguration': {
                    'name': 'string',
                    'description': 'string',
                    'amiTags': {
                        'string': 'string'
                    },
                    'launchPermission': {
                        'userIds': [
                            'string',
                        ],
                        'userGroups': [
                            'string',
                        ]
                    }
                },
                'licenseConfigurationArns': [
                    'string',
                ]
            },
        ],
        tags={
            'string': 'string'
        },
        clientToken='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the distribution configuration.\n

    :type description: string
    :param description: The description of the distribution configuration.

    :type distributions: list
    :param distributions: [REQUIRED]\nThe distributions of the distribution configuration.\n\n(dict) --Defines the settings for a specific Region.\n\nregion (string) -- [REQUIRED]The target Region.\n\namiDistributionConfiguration (dict) --The specific AMI settings (for example, launch permissions, AMI tags).\n\nname (string) --The name of the distribution configuration.\n\ndescription (string) --The description of the distribution configuration.\n\namiTags (dict) --The tags to apply to AMIs distributed to this Region.\n\n(string) --\n(string) --\n\n\n\n\nlaunchPermission (dict) --Launch permissions can be used to configure which AWS accounts can use the AMI to launch instances.\n\nuserIds (list) --The AWS account ID.\n\n(string) --\n\n\nuserGroups (list) --The name of the group.\n\n(string) --\n\n\n\n\n\n\nlicenseConfigurationArns (list) --The License Manager Configuration to associate with the AMI in the specified Region.\n\n(string) --\n\n\n\n\n\n

    :type tags: dict
    :param tags: The tags of the distribution configuration.\n\n(string) --\n(string) --\n\n\n\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe idempotency token of the distribution configuration.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'clientToken': 'string',
    'distributionConfigurationArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

clientToken (string) --
The idempotency token used to make this request idempotent.

distributionConfigurationArn (string) --
The Amazon Resource Name (ARN) of the distribution configuration that was created by this request.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.IdempotentParameterMismatchException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceInUseException
imagebuilder.Client.exceptions.ResourceAlreadyExistsException
imagebuilder.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'requestId': 'string',
        'clientToken': 'string',
        'distributionConfigurationArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.IdempotentParameterMismatchException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    imagebuilder.Client.exceptions.ResourceInUseException
    imagebuilder.Client.exceptions.ResourceAlreadyExistsException
    imagebuilder.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def create_image(imageRecipeArn=None, distributionConfigurationArn=None, infrastructureConfigurationArn=None, imageTestsConfiguration=None, enhancedImageMetadataEnabled=None, tags=None, clientToken=None):
    """
    Creates a new image. This request will create a new image along with all of the configured output resources defined in the distribution configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_image(
        imageRecipeArn='string',
        distributionConfigurationArn='string',
        infrastructureConfigurationArn='string',
        imageTestsConfiguration={
            'imageTestsEnabled': True|False,
            'timeoutMinutes': 123
        },
        enhancedImageMetadataEnabled=True|False,
        tags={
            'string': 'string'
        },
        clientToken='string'
    )
    
    
    :type imageRecipeArn: string
    :param imageRecipeArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.\n

    :type distributionConfigurationArn: string
    :param distributionConfigurationArn: The Amazon Resource Name (ARN) of the distribution configuration that defines and configures the outputs of your pipeline.

    :type infrastructureConfigurationArn: string
    :param infrastructureConfigurationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the infrastructure configuration that defines the environment in which your image will be built and tested.\n

    :type imageTestsConfiguration: dict
    :param imageTestsConfiguration: The image tests configuration of the image.\n\nimageTestsEnabled (boolean) --Defines if tests should be executed when building this image.\n\ntimeoutMinutes (integer) --The maximum time in minutes that tests are permitted to run.\n\n\n

    :type enhancedImageMetadataEnabled: boolean
    :param enhancedImageMetadataEnabled: Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.

    :type tags: dict
    :param tags: The tags of the image.\n\n(string) --\n(string) --\n\n\n\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe idempotency token used to make this request idempotent.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'clientToken': 'string',
    'imageBuildVersionArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

clientToken (string) --
The idempotency token used to make this request idempotent.

imageBuildVersionArn (string) --
The Amazon Resource Name (ARN) of the image that was created by this request.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.IdempotentParameterMismatchException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceInUseException


    :return: {
        'requestId': 'string',
        'clientToken': 'string',
        'imageBuildVersionArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.IdempotentParameterMismatchException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    imagebuilder.Client.exceptions.ResourceInUseException
    
    """
    pass

def create_image_pipeline(name=None, description=None, imageRecipeArn=None, infrastructureConfigurationArn=None, distributionConfigurationArn=None, imageTestsConfiguration=None, enhancedImageMetadataEnabled=None, schedule=None, status=None, tags=None, clientToken=None):
    """
    Creates a new image pipeline. Image pipelines enable you to automate the creation and distribution of images.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_image_pipeline(
        name='string',
        description='string',
        imageRecipeArn='string',
        infrastructureConfigurationArn='string',
        distributionConfigurationArn='string',
        imageTestsConfiguration={
            'imageTestsEnabled': True|False,
            'timeoutMinutes': 123
        },
        enhancedImageMetadataEnabled=True|False,
        schedule={
            'scheduleExpression': 'string',
            'pipelineExecutionStartCondition': 'EXPRESSION_MATCH_ONLY'|'EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE'
        },
        status='DISABLED'|'ENABLED',
        tags={
            'string': 'string'
        },
        clientToken='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the image pipeline.\n

    :type description: string
    :param description: The description of the image pipeline.

    :type imageRecipeArn: string
    :param imageRecipeArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image recipe that will be used to configure images created by this image pipeline.\n

    :type infrastructureConfigurationArn: string
    :param infrastructureConfigurationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the infrastructure configuration that will be used to build images created by this image pipeline.\n

    :type distributionConfigurationArn: string
    :param distributionConfigurationArn: The Amazon Resource Name (ARN) of the distribution configuration that will be used to configure and distribute images created by this image pipeline.

    :type imageTestsConfiguration: dict
    :param imageTestsConfiguration: The image test configuration of the image pipeline.\n\nimageTestsEnabled (boolean) --Defines if tests should be executed when building this image.\n\ntimeoutMinutes (integer) --The maximum time in minutes that tests are permitted to run.\n\n\n

    :type enhancedImageMetadataEnabled: boolean
    :param enhancedImageMetadataEnabled: Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.

    :type schedule: dict
    :param schedule: The schedule of the image pipeline.\n\nscheduleExpression (string) --The expression determines how often EC2 Image Builder evaluates your pipelineExecutionStartCondition .\n\npipelineExecutionStartCondition (string) --The condition configures when the pipeline should trigger a new image build. When the pipelineExecutionStartCondition is set to EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE , EC2 Image Builder will build a new image only when there are known changes pending. When it is set to EXPRESSION_MATCH_ONLY , it will build a new image every time the CRON expression matches the current time.\n\n\n

    :type status: string
    :param status: The status of the image pipeline.

    :type tags: dict
    :param tags: The tags of the image pipeline.\n\n(string) --\n(string) --\n\n\n\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe idempotency token used to make this request idempotent.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'clientToken': 'string',
    'imagePipelineArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

clientToken (string) --
The idempotency token used to make this request idempotent.

imagePipelineArn (string) --
The Amazon Resource Name (ARN) of the image pipeline that was created by this request.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.IdempotentParameterMismatchException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceInUseException
imagebuilder.Client.exceptions.ResourceAlreadyExistsException


    :return: {
        'requestId': 'string',
        'clientToken': 'string',
        'imagePipelineArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.IdempotentParameterMismatchException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    imagebuilder.Client.exceptions.ResourceInUseException
    imagebuilder.Client.exceptions.ResourceAlreadyExistsException
    
    """
    pass

def create_image_recipe(name=None, description=None, semanticVersion=None, components=None, parentImage=None, blockDeviceMappings=None, tags=None, clientToken=None):
    """
    Creates a new image recipe. Image recipes define how images are configured, tested, and assessed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_image_recipe(
        name='string',
        description='string',
        semanticVersion='string',
        components=[
            {
                'componentArn': 'string'
            },
        ],
        parentImage='string',
        blockDeviceMappings=[
            {
                'deviceName': 'string',
                'ebs': {
                    'encrypted': True|False,
                    'deleteOnTermination': True|False,
                    'iops': 123,
                    'kmsKeyId': 'string',
                    'snapshotId': 'string',
                    'volumeSize': 123,
                    'volumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1'
                },
                'virtualName': 'string',
                'noDevice': 'string'
            },
        ],
        tags={
            'string': 'string'
        },
        clientToken='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the image recipe.\n

    :type description: string
    :param description: The description of the image recipe.

    :type semanticVersion: string
    :param semanticVersion: [REQUIRED]\nThe semantic version of the image recipe.\n

    :type components: list
    :param components: [REQUIRED]\nThe components of the image recipe.\n\n(dict) --Configuration details of the component.\n\ncomponentArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the component.\n\n\n\n\n

    :type parentImage: string
    :param parentImage: [REQUIRED]\nThe parent image of the image recipe. The value of the string can be the ARN of the parent image or an AMI ID. The format for the ARN follows this example: arn:aws:imagebuilder:us-west-2:aws:image/windows-server-2016-english-full-base-x86/2019.x.x . The ARN ends with /20xx.x.x , which communicates to EC2 Image Builder that you want to use the latest AMI created in 20xx (year). You can provide the specific version that you want to use, or you can use a wildcard in all of the fields. If you enter an AMI ID for the string value, you must have access to the AMI, and the AMI must be in the same Region in which you are using Image Builder.\n

    :type blockDeviceMappings: list
    :param blockDeviceMappings: The block device mappings of the image recipe.\n\n(dict) --Defines block device mappings for the instance used to configure your image.\n\ndeviceName (string) --The device to which these mappings apply.\n\nebs (dict) --Use to manage Amazon EBS-specific configuration for this mapping.\n\nencrypted (boolean) --Use to configure device encryption.\n\ndeleteOnTermination (boolean) --Use to configure delete on termination of the associated device.\n\niops (integer) --Use to configure device IOPS.\n\nkmsKeyId (string) --Use to configure the KMS key to use when encrypting the device.\n\nsnapshotId (string) --The snapshot that defines the device contents.\n\nvolumeSize (integer) --Use to override the device\'s volume size.\n\nvolumeType (string) --Use to override the device\'s volume type.\n\n\n\nvirtualName (string) --Use to manage instance ephemeral devices.\n\nnoDevice (string) --Use to remove a mapping from the parent image.\n\n\n\n\n

    :type tags: dict
    :param tags: The tags of the image recipe.\n\n(string) --\n(string) --\n\n\n\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe idempotency token used to make this request idempotent.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'clientToken': 'string',
    'imageRecipeArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

clientToken (string) --
The idempotency token used to make this request idempotent.

imageRecipeArn (string) --
The Amazon Resource Name (ARN) of the image recipe that was created by this request.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.IdempotentParameterMismatchException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.InvalidVersionNumberException
imagebuilder.Client.exceptions.ResourceInUseException
imagebuilder.Client.exceptions.ResourceAlreadyExistsException


    :return: {
        'requestId': 'string',
        'clientToken': 'string',
        'imageRecipeArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.IdempotentParameterMismatchException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    imagebuilder.Client.exceptions.InvalidVersionNumberException
    imagebuilder.Client.exceptions.ResourceInUseException
    imagebuilder.Client.exceptions.ResourceAlreadyExistsException
    
    """
    pass

def create_infrastructure_configuration(name=None, description=None, instanceTypes=None, instanceProfileName=None, securityGroupIds=None, subnetId=None, logging=None, keyPair=None, terminateInstanceOnFailure=None, snsTopicArn=None, tags=None, clientToken=None):
    """
    Creates a new infrastructure configuration. An infrastructure configuration defines the environment in which your image will be built and tested.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_infrastructure_configuration(
        name='string',
        description='string',
        instanceTypes=[
            'string',
        ],
        instanceProfileName='string',
        securityGroupIds=[
            'string',
        ],
        subnetId='string',
        logging={
            's3Logs': {
                's3BucketName': 'string',
                's3KeyPrefix': 'string'
            }
        },
        keyPair='string',
        terminateInstanceOnFailure=True|False,
        snsTopicArn='string',
        tags={
            'string': 'string'
        },
        clientToken='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the infrastructure configuration.\n

    :type description: string
    :param description: The description of the infrastructure configuration.

    :type instanceTypes: list
    :param instanceTypes: The instance types of the infrastructure configuration. You can specify one or more instance types to use for this build. The service will pick one of these instance types based on availability.\n\n(string) --\n\n

    :type instanceProfileName: string
    :param instanceProfileName: [REQUIRED]\nThe instance profile to associate with the instance used to customize your EC2 AMI.\n

    :type securityGroupIds: list
    :param securityGroupIds: The security group IDs to associate with the instance used to customize your EC2 AMI.\n\n(string) --\n\n

    :type subnetId: string
    :param subnetId: The subnet ID in which to place the instance used to customize your EC2 AMI.

    :type logging: dict
    :param logging: The logging configuration of the infrastructure configuration.\n\ns3Logs (dict) --The Amazon S3 logging configuration.\n\ns3BucketName (string) --The Amazon S3 bucket in which to store the logs.\n\ns3KeyPrefix (string) --The Amazon S3 path in which to store the logs.\n\n\n\n\n

    :type keyPair: string
    :param keyPair: The key pair of the infrastructure configuration. This can be used to log on to and debug the instance used to create your image.

    :type terminateInstanceOnFailure: boolean
    :param terminateInstanceOnFailure: The terminate instance on failure setting of the infrastructure configuration. Set to false if you want Image Builder to retain the instance used to configure your AMI if the build or test phase of your workflow fails.

    :type snsTopicArn: string
    :param snsTopicArn: The SNS topic on which to send image build events.

    :type tags: dict
    :param tags: The tags of the infrastructure configuration.\n\n(string) --\n(string) --\n\n\n\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe idempotency token used to make this request idempotent.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'clientToken': 'string',
    'infrastructureConfigurationArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

clientToken (string) --
The idempotency token used to make this request idempotent.

infrastructureConfigurationArn (string) --
The Amazon Resource Name (ARN) of the infrastructure configuration that was created by this request.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.IdempotentParameterMismatchException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceInUseException
imagebuilder.Client.exceptions.ResourceAlreadyExistsException


    :return: {
        'requestId': 'string',
        'clientToken': 'string',
        'infrastructureConfigurationArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.IdempotentParameterMismatchException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    imagebuilder.Client.exceptions.ResourceInUseException
    imagebuilder.Client.exceptions.ResourceAlreadyExistsException
    
    """
    pass

def delete_component(componentBuildVersionArn=None):
    """
    Deletes a component build version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_component(
        componentBuildVersionArn='string'
    )
    
    
    :type componentBuildVersionArn: string
    :param componentBuildVersionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the component build version to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'componentBuildVersionArn': 'string'
}


Response Structure

(dict) --
requestId (string) --The request ID that uniquely identifies this request.

componentBuildVersionArn (string) --The Amazon Resource Name (ARN) of the component build version that was deleted.






Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceDependencyException


    :return: {
        'requestId': 'string',
        'componentBuildVersionArn': 'string'
    }
    
    
    """
    pass

def delete_distribution_configuration(distributionConfigurationArn=None):
    """
    Deletes a distribution configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_distribution_configuration(
        distributionConfigurationArn='string'
    )
    
    
    :type distributionConfigurationArn: string
    :param distributionConfigurationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the distribution configuration to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'distributionConfigurationArn': 'string'
}


Response Structure

(dict) --
requestId (string) --The request ID that uniquely identifies this request.

distributionConfigurationArn (string) --The Amazon Resource Name (ARN) of the distribution configuration that was deleted.






Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceDependencyException


    :return: {
        'requestId': 'string',
        'distributionConfigurationArn': 'string'
    }
    
    
    """
    pass

def delete_image(imageBuildVersionArn=None):
    """
    Deletes an image.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_image(
        imageBuildVersionArn='string'
    )
    
    
    :type imageBuildVersionArn: string
    :param imageBuildVersionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'imageBuildVersionArn': 'string'
}


Response Structure

(dict) --
requestId (string) --The request ID that uniquely identifies this request.

imageBuildVersionArn (string) --The Amazon Resource Name (ARN) of the image that was deleted.






Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceDependencyException


    :return: {
        'requestId': 'string',
        'imageBuildVersionArn': 'string'
    }
    
    
    """
    pass

def delete_image_pipeline(imagePipelineArn=None):
    """
    Deletes an image pipeline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_image_pipeline(
        imagePipelineArn='string'
    )
    
    
    :type imagePipelineArn: string
    :param imagePipelineArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image pipeline to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'imagePipelineArn': 'string'
}


Response Structure

(dict) --
requestId (string) --The request ID that uniquely identifies this request.

imagePipelineArn (string) --The Amazon Resource Name (ARN) of the image pipeline that was deleted.






Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceDependencyException


    :return: {
        'requestId': 'string',
        'imagePipelineArn': 'string'
    }
    
    
    """
    pass

def delete_image_recipe(imageRecipeArn=None):
    """
    Deletes an image recipe.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_image_recipe(
        imageRecipeArn='string'
    )
    
    
    :type imageRecipeArn: string
    :param imageRecipeArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image recipe to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'imageRecipeArn': 'string'
}


Response Structure

(dict) --
requestId (string) --The request ID that uniquely identifies this request.

imageRecipeArn (string) --The Amazon Resource Name (ARN) of the image recipe that was deleted.






Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceDependencyException


    :return: {
        'requestId': 'string',
        'imageRecipeArn': 'string'
    }
    
    
    """
    pass

def delete_infrastructure_configuration(infrastructureConfigurationArn=None):
    """
    Deletes an infrastructure configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_infrastructure_configuration(
        infrastructureConfigurationArn='string'
    )
    
    
    :type infrastructureConfigurationArn: string
    :param infrastructureConfigurationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the infrastructure configuration to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'infrastructureConfigurationArn': 'string'
}


Response Structure

(dict) --
requestId (string) --The request ID that uniquely identifies this request.

infrastructureConfigurationArn (string) --The Amazon Resource Name (ARN) of the infrastructure configuration that was deleted.






Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceDependencyException


    :return: {
        'requestId': 'string',
        'infrastructureConfigurationArn': 'string'
    }
    
    
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

def get_component(componentBuildVersionArn=None):
    """
    Gets a component object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_component(
        componentBuildVersionArn='string'
    )
    
    
    :type componentBuildVersionArn: string
    :param componentBuildVersionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the component that you want to retrieve. Regex requires '/d+$' suffix.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'component': {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'description': 'string',
        'changeDescription': 'string',
        'type': 'BUILD'|'TEST',
        'platform': 'Windows'|'Linux',
        'supportedOsVersions': [
            'string',
        ],
        'owner': 'string',
        'data': 'string',
        'kmsKeyId': 'string',
        'encrypted': True|False,
        'dateCreated': 'string',
        'tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --
requestId (string) --The request ID that uniquely identifies this request.

component (dict) --The component object associated with the specified ARN.

arn (string) --The Amazon Resource Name (ARN) of the component.

name (string) --The name of the component.

version (string) --The version of the component.

description (string) --The description of the component.

changeDescription (string) --The change description of the component.

type (string) --The type of the component denotes whether the component is used to build the image or only to test it.

platform (string) --The platform of the component.

supportedOsVersions (list) --The operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the parent image OS version during image recipe creation.

(string) --


owner (string) --The owner of the component.

data (string) --The data of the component.

kmsKeyId (string) --The KMS key identifier used to encrypt the component.

encrypted (boolean) --The encryption status of the component.

dateCreated (string) --The date that the component was created.

tags (dict) --The tags associated with the component.

(string) --
(string) --











Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'component': {
            'arn': 'string',
            'name': 'string',
            'version': 'string',
            'description': 'string',
            'changeDescription': 'string',
            'type': 'BUILD'|'TEST',
            'platform': 'Windows'|'Linux',
            'supportedOsVersions': [
                'string',
            ],
            'owner': 'string',
            'data': 'string',
            'kmsKeyId': 'string',
            'encrypted': True|False,
            'dateCreated': 'string',
            'tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_component_policy(componentArn=None):
    """
    Gets a component policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_component_policy(
        componentArn='string'
    )
    
    
    :type componentArn: string
    :param componentArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the component whose policy you want to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'policy': 'string'
}


Response Structure

(dict) --
requestId (string) --The request ID that uniquely identifies this request.

policy (string) --The component policy.






Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.ResourceNotFoundException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'policy': 'string'
    }
    
    
    """
    pass

def get_distribution_configuration(distributionConfigurationArn=None):
    """
    Gets a distribution configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_distribution_configuration(
        distributionConfigurationArn='string'
    )
    
    
    :type distributionConfigurationArn: string
    :param distributionConfigurationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the distribution configuration that you want to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'distributionConfiguration': {
        'arn': 'string',
        'name': 'string',
        'description': 'string',
        'distributions': [
            {
                'region': 'string',
                'amiDistributionConfiguration': {
                    'name': 'string',
                    'description': 'string',
                    'amiTags': {
                        'string': 'string'
                    },
                    'launchPermission': {
                        'userIds': [
                            'string',
                        ],
                        'userGroups': [
                            'string',
                        ]
                    }
                },
                'licenseConfigurationArns': [
                    'string',
                ]
            },
        ],
        'timeoutMinutes': 123,
        'dateCreated': 'string',
        'dateUpdated': 'string',
        'tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --
requestId (string) --The request ID that uniquely identifies this request.

distributionConfiguration (dict) --The distribution configuration object.

arn (string) --The Amazon Resource Name (ARN) of the distribution configuration.

name (string) --The name of the distribution configuration.

description (string) --The description of the distribution configuration.

distributions (list) --The distributions of the distribution configuration.

(dict) --Defines the settings for a specific Region.

region (string) --The target Region.

amiDistributionConfiguration (dict) --The specific AMI settings (for example, launch permissions, AMI tags).

name (string) --The name of the distribution configuration.

description (string) --The description of the distribution configuration.

amiTags (dict) --The tags to apply to AMIs distributed to this Region.

(string) --
(string) --




launchPermission (dict) --Launch permissions can be used to configure which AWS accounts can use the AMI to launch instances.

userIds (list) --The AWS account ID.

(string) --


userGroups (list) --The name of the group.

(string) --






licenseConfigurationArns (list) --The License Manager Configuration to associate with the AMI in the specified Region.

(string) --






timeoutMinutes (integer) --The maximum duration in minutes for this distribution configuration.

dateCreated (string) --The date on which this distribution configuration was created.

dateUpdated (string) --The date on which this distribution configuration was last updated.

tags (dict) --The tags of the distribution configuration.

(string) --
(string) --











Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'distributionConfiguration': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'distributions': [
                {
                    'region': 'string',
                    'amiDistributionConfiguration': {
                        'name': 'string',
                        'description': 'string',
                        'amiTags': {
                            'string': 'string'
                        },
                        'launchPermission': {
                            'userIds': [
                                'string',
                            ],
                            'userGroups': [
                                'string',
                            ]
                        }
                    },
                    'licenseConfigurationArns': [
                        'string',
                    ]
                },
            ],
            'timeoutMinutes': 123,
            'dateCreated': 'string',
            'dateUpdated': 'string',
            'tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_image(imageBuildVersionArn=None):
    """
    Gets an image.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_image(
        imageBuildVersionArn='string'
    )
    
    
    :type imageBuildVersionArn: string
    :param imageBuildVersionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image that you want to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'image': {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'platform': 'Windows'|'Linux',
        'enhancedImageMetadataEnabled': True|False,
        'osVersion': 'string',
        'state': {
            'status': 'PENDING'|'CREATING'|'BUILDING'|'TESTING'|'DISTRIBUTING'|'INTEGRATING'|'AVAILABLE'|'CANCELLED'|'FAILED'|'DEPRECATED'|'DELETED',
            'reason': 'string'
        },
        'imageRecipe': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'platform': 'Windows'|'Linux',
            'owner': 'string',
            'version': 'string',
            'components': [
                {
                    'componentArn': 'string'
                },
            ],
            'parentImage': 'string',
            'blockDeviceMappings': [
                {
                    'deviceName': 'string',
                    'ebs': {
                        'encrypted': True|False,
                        'deleteOnTermination': True|False,
                        'iops': 123,
                        'kmsKeyId': 'string',
                        'snapshotId': 'string',
                        'volumeSize': 123,
                        'volumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1'
                    },
                    'virtualName': 'string',
                    'noDevice': 'string'
                },
            ],
            'dateCreated': 'string',
            'tags': {
                'string': 'string'
            }
        },
        'sourcePipelineName': 'string',
        'sourcePipelineArn': 'string',
        'infrastructureConfiguration': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'instanceTypes': [
                'string',
            ],
            'instanceProfileName': 'string',
            'securityGroupIds': [
                'string',
            ],
            'subnetId': 'string',
            'logging': {
                's3Logs': {
                    's3BucketName': 'string',
                    's3KeyPrefix': 'string'
                }
            },
            'keyPair': 'string',
            'terminateInstanceOnFailure': True|False,
            'snsTopicArn': 'string',
            'dateCreated': 'string',
            'dateUpdated': 'string',
            'tags': {
                'string': 'string'
            }
        },
        'distributionConfiguration': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'distributions': [
                {
                    'region': 'string',
                    'amiDistributionConfiguration': {
                        'name': 'string',
                        'description': 'string',
                        'amiTags': {
                            'string': 'string'
                        },
                        'launchPermission': {
                            'userIds': [
                                'string',
                            ],
                            'userGroups': [
                                'string',
                            ]
                        }
                    },
                    'licenseConfigurationArns': [
                        'string',
                    ]
                },
            ],
            'timeoutMinutes': 123,
            'dateCreated': 'string',
            'dateUpdated': 'string',
            'tags': {
                'string': 'string'
            }
        },
        'imageTestsConfiguration': {
            'imageTestsEnabled': True|False,
            'timeoutMinutes': 123
        },
        'dateCreated': 'string',
        'outputResources': {
            'amis': [
                {
                    'region': 'string',
                    'image': 'string',
                    'name': 'string',
                    'description': 'string',
                    'state': {
                        'status': 'PENDING'|'CREATING'|'BUILDING'|'TESTING'|'DISTRIBUTING'|'INTEGRATING'|'AVAILABLE'|'CANCELLED'|'FAILED'|'DEPRECATED'|'DELETED',
                        'reason': 'string'
                    }
                },
            ]
        },
        'tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --
requestId (string) --The request ID that uniquely identifies this request.

image (dict) --The image object.

arn (string) --The Amazon Resource Name (ARN) of the image.

name (string) --The name of the image.

version (string) --The semantic version of the image.

platform (string) --The platform of the image.

enhancedImageMetadataEnabled (boolean) --Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.

osVersion (string) --The operating system version of the instance. For example, Amazon Linux 2, Ubuntu 18, or Microsoft Windows Server 2019.

state (dict) --The state of the image.

status (string) --The status of the image.

reason (string) --The reason for the image\'s status.



imageRecipe (dict) --The image recipe used when creating the image.

arn (string) --The Amazon Resource Name (ARN) of the image recipe.

name (string) --The name of the image recipe.

description (string) --The description of the image recipe.

platform (string) --The platform of the image recipe.

owner (string) --The owner of the image recipe.

version (string) --The version of the image recipe.

components (list) --The components of the image recipe.

(dict) --Configuration details of the component.

componentArn (string) --The Amazon Resource Name (ARN) of the component.





parentImage (string) --The parent image of the image recipe.

blockDeviceMappings (list) --The block device mappings to apply when creating images from this recipe.

(dict) --Defines block device mappings for the instance used to configure your image.

deviceName (string) --The device to which these mappings apply.

ebs (dict) --Use to manage Amazon EBS-specific configuration for this mapping.

encrypted (boolean) --Use to configure device encryption.

deleteOnTermination (boolean) --Use to configure delete on termination of the associated device.

iops (integer) --Use to configure device IOPS.

kmsKeyId (string) --Use to configure the KMS key to use when encrypting the device.

snapshotId (string) --The snapshot that defines the device contents.

volumeSize (integer) --Use to override the device\'s volume size.

volumeType (string) --Use to override the device\'s volume type.



virtualName (string) --Use to manage instance ephemeral devices.

noDevice (string) --Use to remove a mapping from the parent image.





dateCreated (string) --The date on which this image recipe was created.

tags (dict) --The tags of the image recipe.

(string) --
(string) --






sourcePipelineName (string) --The name of the image pipeline that created this image.

sourcePipelineArn (string) --The Amazon Resource Name (ARN) of the image pipeline that created this image.

infrastructureConfiguration (dict) --The infrastructure used when creating this image.

arn (string) --The Amazon Resource Name (ARN) of the infrastructure configuration.

name (string) --The name of the infrastructure configuration.

description (string) --The description of the infrastructure configuration.

instanceTypes (list) --The instance types of the infrastructure configuration.

(string) --


instanceProfileName (string) --The instance profile of the infrastructure configuration.

securityGroupIds (list) --The security group IDs of the infrastructure configuration.

(string) --


subnetId (string) --The subnet ID of the infrastructure configuration.

logging (dict) --The logging configuration of the infrastructure configuration.

s3Logs (dict) --The Amazon S3 logging configuration.

s3BucketName (string) --The Amazon S3 bucket in which to store the logs.

s3KeyPrefix (string) --The Amazon S3 path in which to store the logs.





keyPair (string) --The EC2 key pair of the infrastructure configuration.

terminateInstanceOnFailure (boolean) --The terminate instance on failure configuration of the infrastructure configuration.

snsTopicArn (string) --The SNS topic Amazon Resource Name (ARN) of the infrastructure configuration.

dateCreated (string) --The date on which the infrastructure configuration was created.

dateUpdated (string) --The date on which the infrastructure configuration was last updated.

tags (dict) --The tags of the infrastructure configuration.

(string) --
(string) --






distributionConfiguration (dict) --The distribution configuration used when creating this image.

arn (string) --The Amazon Resource Name (ARN) of the distribution configuration.

name (string) --The name of the distribution configuration.

description (string) --The description of the distribution configuration.

distributions (list) --The distributions of the distribution configuration.

(dict) --Defines the settings for a specific Region.

region (string) --The target Region.

amiDistributionConfiguration (dict) --The specific AMI settings (for example, launch permissions, AMI tags).

name (string) --The name of the distribution configuration.

description (string) --The description of the distribution configuration.

amiTags (dict) --The tags to apply to AMIs distributed to this Region.

(string) --
(string) --




launchPermission (dict) --Launch permissions can be used to configure which AWS accounts can use the AMI to launch instances.

userIds (list) --The AWS account ID.

(string) --


userGroups (list) --The name of the group.

(string) --






licenseConfigurationArns (list) --The License Manager Configuration to associate with the AMI in the specified Region.

(string) --






timeoutMinutes (integer) --The maximum duration in minutes for this distribution configuration.

dateCreated (string) --The date on which this distribution configuration was created.

dateUpdated (string) --The date on which this distribution configuration was last updated.

tags (dict) --The tags of the distribution configuration.

(string) --
(string) --






imageTestsConfiguration (dict) --The image tests configuration used when creating this image.

imageTestsEnabled (boolean) --Defines if tests should be executed when building this image.

timeoutMinutes (integer) --The maximum time in minutes that tests are permitted to run.



dateCreated (string) --The date on which this image was created.

outputResources (dict) --The output resources produced when creating this image.

amis (list) --The EC2 AMIs created by this image.

(dict) --Details of an EC2 AMI.

region (string) --The AWS Region of the EC2 AMI.

image (string) --The AMI ID of the EC2 AMI.

name (string) --The name of the EC2 AMI.

description (string) --The description of the EC2 AMI.

state (dict) --Image state shows the image status and the reason for that status.

status (string) --The status of the image.

reason (string) --The reason for the image\'s status.









tags (dict) --The tags of the image.

(string) --
(string) --











Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'image': {
            'arn': 'string',
            'name': 'string',
            'version': 'string',
            'platform': 'Windows'|'Linux',
            'enhancedImageMetadataEnabled': True|False,
            'osVersion': 'string',
            'state': {
                'status': 'PENDING'|'CREATING'|'BUILDING'|'TESTING'|'DISTRIBUTING'|'INTEGRATING'|'AVAILABLE'|'CANCELLED'|'FAILED'|'DEPRECATED'|'DELETED',
                'reason': 'string'
            },
            'imageRecipe': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'platform': 'Windows'|'Linux',
                'owner': 'string',
                'version': 'string',
                'components': [
                    {
                        'componentArn': 'string'
                    },
                ],
                'parentImage': 'string',
                'blockDeviceMappings': [
                    {
                        'deviceName': 'string',
                        'ebs': {
                            'encrypted': True|False,
                            'deleteOnTermination': True|False,
                            'iops': 123,
                            'kmsKeyId': 'string',
                            'snapshotId': 'string',
                            'volumeSize': 123,
                            'volumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1'
                        },
                        'virtualName': 'string',
                        'noDevice': 'string'
                    },
                ],
                'dateCreated': 'string',
                'tags': {
                    'string': 'string'
                }
            },
            'sourcePipelineName': 'string',
            'sourcePipelineArn': 'string',
            'infrastructureConfiguration': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'instanceTypes': [
                    'string',
                ],
                'instanceProfileName': 'string',
                'securityGroupIds': [
                    'string',
                ],
                'subnetId': 'string',
                'logging': {
                    's3Logs': {
                        's3BucketName': 'string',
                        's3KeyPrefix': 'string'
                    }
                },
                'keyPair': 'string',
                'terminateInstanceOnFailure': True|False,
                'snsTopicArn': 'string',
                'dateCreated': 'string',
                'dateUpdated': 'string',
                'tags': {
                    'string': 'string'
                }
            },
            'distributionConfiguration': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'distributions': [
                    {
                        'region': 'string',
                        'amiDistributionConfiguration': {
                            'name': 'string',
                            'description': 'string',
                            'amiTags': {
                                'string': 'string'
                            },
                            'launchPermission': {
                                'userIds': [
                                    'string',
                                ],
                                'userGroups': [
                                    'string',
                                ]
                            }
                        },
                        'licenseConfigurationArns': [
                            'string',
                        ]
                    },
                ],
                'timeoutMinutes': 123,
                'dateCreated': 'string',
                'dateUpdated': 'string',
                'tags': {
                    'string': 'string'
                }
            },
            'imageTestsConfiguration': {
                'imageTestsEnabled': True|False,
                'timeoutMinutes': 123
            },
            'dateCreated': 'string',
            'outputResources': {
                'amis': [
                    {
                        'region': 'string',
                        'image': 'string',
                        'name': 'string',
                        'description': 'string',
                        'state': {
                            'status': 'PENDING'|'CREATING'|'BUILDING'|'TESTING'|'DISTRIBUTING'|'INTEGRATING'|'AVAILABLE'|'CANCELLED'|'FAILED'|'DEPRECATED'|'DELETED',
                            'reason': 'string'
                        }
                    },
                ]
            },
            'tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_image_pipeline(imagePipelineArn=None):
    """
    Gets an image pipeline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_image_pipeline(
        imagePipelineArn='string'
    )
    
    
    :type imagePipelineArn: string
    :param imagePipelineArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image pipeline that you want to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'imagePipeline': {
        'arn': 'string',
        'name': 'string',
        'description': 'string',
        'platform': 'Windows'|'Linux',
        'enhancedImageMetadataEnabled': True|False,
        'imageRecipeArn': 'string',
        'infrastructureConfigurationArn': 'string',
        'distributionConfigurationArn': 'string',
        'imageTestsConfiguration': {
            'imageTestsEnabled': True|False,
            'timeoutMinutes': 123
        },
        'schedule': {
            'scheduleExpression': 'string',
            'pipelineExecutionStartCondition': 'EXPRESSION_MATCH_ONLY'|'EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE'
        },
        'status': 'DISABLED'|'ENABLED',
        'dateCreated': 'string',
        'dateUpdated': 'string',
        'dateLastRun': 'string',
        'dateNextRun': 'string',
        'tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --
requestId (string) --The request ID that uniquely identifies this request.

imagePipeline (dict) --The image pipeline object.

arn (string) --The Amazon Resource Name (ARN) of the image pipeline.

name (string) --The name of the image pipeline.

description (string) --The description of the image pipeline.

platform (string) --The platform of the image pipeline.

enhancedImageMetadataEnabled (boolean) --Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.

imageRecipeArn (string) --The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.

infrastructureConfigurationArn (string) --The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.

distributionConfigurationArn (string) --The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.

imageTestsConfiguration (dict) --The image tests configuration of the image pipeline.

imageTestsEnabled (boolean) --Defines if tests should be executed when building this image.

timeoutMinutes (integer) --The maximum time in minutes that tests are permitted to run.



schedule (dict) --The schedule of the image pipeline.

scheduleExpression (string) --The expression determines how often EC2 Image Builder evaluates your pipelineExecutionStartCondition .

pipelineExecutionStartCondition (string) --The condition configures when the pipeline should trigger a new image build. When the pipelineExecutionStartCondition is set to EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE , EC2 Image Builder will build a new image only when there are known changes pending. When it is set to EXPRESSION_MATCH_ONLY , it will build a new image every time the CRON expression matches the current time.



status (string) --The status of the image pipeline.

dateCreated (string) --The date on which this image pipeline was created.

dateUpdated (string) --The date on which this image pipeline was last updated.

dateLastRun (string) --The date on which this image pipeline was last run.

dateNextRun (string) --The date on which this image pipeline will next be run.

tags (dict) --The tags of this image pipeline.

(string) --
(string) --











Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'imagePipeline': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'platform': 'Windows'|'Linux',
            'enhancedImageMetadataEnabled': True|False,
            'imageRecipeArn': 'string',
            'infrastructureConfigurationArn': 'string',
            'distributionConfigurationArn': 'string',
            'imageTestsConfiguration': {
                'imageTestsEnabled': True|False,
                'timeoutMinutes': 123
            },
            'schedule': {
                'scheduleExpression': 'string',
                'pipelineExecutionStartCondition': 'EXPRESSION_MATCH_ONLY'|'EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE'
            },
            'status': 'DISABLED'|'ENABLED',
            'dateCreated': 'string',
            'dateUpdated': 'string',
            'dateLastRun': 'string',
            'dateNextRun': 'string',
            'tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    
    """
    pass

def get_image_policy(imageArn=None):
    """
    Gets an image policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_image_policy(
        imageArn='string'
    )
    
    
    :type imageArn: string
    :param imageArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image whose policy you want to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'policy': 'string'
}


Response Structure

(dict) --
requestId (string) --The request ID that uniquely identifies this request.

policy (string) --The image policy object.






Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.ResourceNotFoundException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'policy': 'string'
    }
    
    
    """
    pass

def get_image_recipe(imageRecipeArn=None):
    """
    Gets an image recipe.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_image_recipe(
        imageRecipeArn='string'
    )
    
    
    :type imageRecipeArn: string
    :param imageRecipeArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image recipe that you want to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'imageRecipe': {
        'arn': 'string',
        'name': 'string',
        'description': 'string',
        'platform': 'Windows'|'Linux',
        'owner': 'string',
        'version': 'string',
        'components': [
            {
                'componentArn': 'string'
            },
        ],
        'parentImage': 'string',
        'blockDeviceMappings': [
            {
                'deviceName': 'string',
                'ebs': {
                    'encrypted': True|False,
                    'deleteOnTermination': True|False,
                    'iops': 123,
                    'kmsKeyId': 'string',
                    'snapshotId': 'string',
                    'volumeSize': 123,
                    'volumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1'
                },
                'virtualName': 'string',
                'noDevice': 'string'
            },
        ],
        'dateCreated': 'string',
        'tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --
requestId (string) --The request ID that uniquely identifies this request.

imageRecipe (dict) --The image recipe object.

arn (string) --The Amazon Resource Name (ARN) of the image recipe.

name (string) --The name of the image recipe.

description (string) --The description of the image recipe.

platform (string) --The platform of the image recipe.

owner (string) --The owner of the image recipe.

version (string) --The version of the image recipe.

components (list) --The components of the image recipe.

(dict) --Configuration details of the component.

componentArn (string) --The Amazon Resource Name (ARN) of the component.





parentImage (string) --The parent image of the image recipe.

blockDeviceMappings (list) --The block device mappings to apply when creating images from this recipe.

(dict) --Defines block device mappings for the instance used to configure your image.

deviceName (string) --The device to which these mappings apply.

ebs (dict) --Use to manage Amazon EBS-specific configuration for this mapping.

encrypted (boolean) --Use to configure device encryption.

deleteOnTermination (boolean) --Use to configure delete on termination of the associated device.

iops (integer) --Use to configure device IOPS.

kmsKeyId (string) --Use to configure the KMS key to use when encrypting the device.

snapshotId (string) --The snapshot that defines the device contents.

volumeSize (integer) --Use to override the device\'s volume size.

volumeType (string) --Use to override the device\'s volume type.



virtualName (string) --Use to manage instance ephemeral devices.

noDevice (string) --Use to remove a mapping from the parent image.





dateCreated (string) --The date on which this image recipe was created.

tags (dict) --The tags of the image recipe.

(string) --
(string) --











Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'imageRecipe': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'platform': 'Windows'|'Linux',
            'owner': 'string',
            'version': 'string',
            'components': [
                {
                    'componentArn': 'string'
                },
            ],
            'parentImage': 'string',
            'blockDeviceMappings': [
                {
                    'deviceName': 'string',
                    'ebs': {
                        'encrypted': True|False,
                        'deleteOnTermination': True|False,
                        'iops': 123,
                        'kmsKeyId': 'string',
                        'snapshotId': 'string',
                        'volumeSize': 123,
                        'volumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1'
                    },
                    'virtualName': 'string',
                    'noDevice': 'string'
                },
            ],
            'dateCreated': 'string',
            'tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    
    """
    pass

def get_image_recipe_policy(imageRecipeArn=None):
    """
    Gets an image recipe policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_image_recipe_policy(
        imageRecipeArn='string'
    )
    
    
    :type imageRecipeArn: string
    :param imageRecipeArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image recipe whose policy you want to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'policy': 'string'
}


Response Structure

(dict) --
requestId (string) --The request ID that uniquely identifies this request.

policy (string) --The image recipe policy object.






Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ResourceNotFoundException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'policy': 'string'
    }
    
    
    """
    pass

def get_infrastructure_configuration(infrastructureConfigurationArn=None):
    """
    Gets an infrastructure configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_infrastructure_configuration(
        infrastructureConfigurationArn='string'
    )
    
    
    :type infrastructureConfigurationArn: string
    :param infrastructureConfigurationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the infrastructure configuration that you want to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'requestId': 'string',
    'infrastructureConfiguration': {
        'arn': 'string',
        'name': 'string',
        'description': 'string',
        'instanceTypes': [
            'string',
        ],
        'instanceProfileName': 'string',
        'securityGroupIds': [
            'string',
        ],
        'subnetId': 'string',
        'logging': {
            's3Logs': {
                's3BucketName': 'string',
                's3KeyPrefix': 'string'
            }
        },
        'keyPair': 'string',
        'terminateInstanceOnFailure': True|False,
        'snsTopicArn': 'string',
        'dateCreated': 'string',
        'dateUpdated': 'string',
        'tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --GetInfrastructureConfiguration response object.

requestId (string) --The request ID that uniquely identifies this request.

infrastructureConfiguration (dict) --The infrastructure configuration object.

arn (string) --The Amazon Resource Name (ARN) of the infrastructure configuration.

name (string) --The name of the infrastructure configuration.

description (string) --The description of the infrastructure configuration.

instanceTypes (list) --The instance types of the infrastructure configuration.

(string) --


instanceProfileName (string) --The instance profile of the infrastructure configuration.

securityGroupIds (list) --The security group IDs of the infrastructure configuration.

(string) --


subnetId (string) --The subnet ID of the infrastructure configuration.

logging (dict) --The logging configuration of the infrastructure configuration.

s3Logs (dict) --The Amazon S3 logging configuration.

s3BucketName (string) --The Amazon S3 bucket in which to store the logs.

s3KeyPrefix (string) --The Amazon S3 path in which to store the logs.





keyPair (string) --The EC2 key pair of the infrastructure configuration.

terminateInstanceOnFailure (boolean) --The terminate instance on failure configuration of the infrastructure configuration.

snsTopicArn (string) --The SNS topic Amazon Resource Name (ARN) of the infrastructure configuration.

dateCreated (string) --The date on which the infrastructure configuration was created.

dateUpdated (string) --The date on which the infrastructure configuration was last updated.

tags (dict) --The tags of the infrastructure configuration.

(string) --
(string) --











Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'infrastructureConfiguration': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'instanceTypes': [
                'string',
            ],
            'instanceProfileName': 'string',
            'securityGroupIds': [
                'string',
            ],
            'subnetId': 'string',
            'logging': {
                's3Logs': {
                    's3BucketName': 'string',
                    's3KeyPrefix': 'string'
                }
            },
            'keyPair': 'string',
            'terminateInstanceOnFailure': True|False,
            'snsTopicArn': 'string',
            'dateCreated': 'string',
            'dateUpdated': 'string',
            'tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
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

def import_component(name=None, semanticVersion=None, description=None, changeDescription=None, type=None, format=None, platform=None, data=None, uri=None, kmsKeyId=None, tags=None, clientToken=None):
    """
    Imports a component and transforms its data into a component document.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.import_component(
        name='string',
        semanticVersion='string',
        description='string',
        changeDescription='string',
        type='BUILD'|'TEST',
        format='SHELL',
        platform='Windows'|'Linux',
        data='string',
        uri='string',
        kmsKeyId='string',
        tags={
            'string': 'string'
        },
        clientToken='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the component.\n

    :type semanticVersion: string
    :param semanticVersion: [REQUIRED]\nThe semantic version of the component. This version follows the semantic version syntax. For example, major.minor.patch. This could be versioned like software (2.0.1) or like a date (2019.12.01).\n

    :type description: string
    :param description: The description of the component. Describes the contents of the component.

    :type changeDescription: string
    :param changeDescription: The change description of the component. Describes what change has been made in this version, or what makes this version different from other versions of this component.

    :type type: string
    :param type: [REQUIRED]\nThe type of the component denotes whether the component is used to build the image or only to test it.\n

    :type format: string
    :param format: [REQUIRED]\nThe format of the resource that you want to import as a component.\n

    :type platform: string
    :param platform: [REQUIRED]\nThe platform of the component.\n

    :type data: string
    :param data: The data of the component. Used to specify the data inline. Either data or uri can be used to specify the data within the component.

    :type uri: string
    :param uri: The uri of the component. Must be an S3 URL and the requester must have permission to access the S3 bucket. If you use S3, you can specify component content up to your service quota. Either data or uri can be used to specify the data within the component.

    :type kmsKeyId: string
    :param kmsKeyId: The ID of the KMS key that should be used to encrypt this component.

    :type tags: dict
    :param tags: The tags of the component.\n\n(string) --\n(string) --\n\n\n\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe idempotency token of the component.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'clientToken': 'string',
    'componentBuildVersionArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

clientToken (string) --
The idempotency token used to make this request idempotent.

componentBuildVersionArn (string) --
The Amazon Resource Name (ARN) of the imported component.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.IdempotentParameterMismatchException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.InvalidVersionNumberException
imagebuilder.Client.exceptions.ResourceInUseException
imagebuilder.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'requestId': 'string',
        'clientToken': 'string',
        'componentBuildVersionArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.IdempotentParameterMismatchException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    imagebuilder.Client.exceptions.InvalidVersionNumberException
    imagebuilder.Client.exceptions.ResourceInUseException
    imagebuilder.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def list_component_build_versions(componentVersionArn=None, maxResults=None, nextToken=None):
    """
    Returns the list of component build versions for the specified semantic version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_component_build_versions(
        componentVersionArn='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type componentVersionArn: string
    :param componentVersionArn: [REQUIRED]\nThe component version Amazon Resource Name (ARN) whose versions you want to list.\n

    :type maxResults: integer
    :param maxResults: The maximum items to return in a request.

    :type nextToken: string
    :param nextToken: A token to specify where to start paginating. This is the NextToken from a previously truncated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'componentSummaryList': [
        {
            'arn': 'string',
            'name': 'string',
            'version': 'string',
            'platform': 'Windows'|'Linux',
            'supportedOsVersions': [
                'string',
            ],
            'type': 'BUILD'|'TEST',
            'owner': 'string',
            'description': 'string',
            'changeDescription': 'string',
            'dateCreated': 'string',
            'tags': {
                'string': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

componentSummaryList (list) --
The list of component summaries for the specified semantic version.

(dict) --
A high-level summary of a component.

arn (string) --
The Amazon Resource Name (ARN) of the component.

name (string) --
The name of the component.

version (string) --
The version of the component.

platform (string) --
The platform of the component.

supportedOsVersions (list) --
The operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the parent image OS version during image recipe creation.

(string) --


type (string) --
The type of the component denotes whether the component is used to build the image or only to test it.

owner (string) --
The owner of the component.

description (string) --
The description of the component.

changeDescription (string) --
The change description of the component.

dateCreated (string) --
The date that the component was created.

tags (dict) --
The tags associated with the component.

(string) --
(string) --








nextToken (string) --
The next token used for paginated responses. When this is not empty, there are additional elements that the service has not included in this request. Use this token with the next request to retrieve additional objects.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.InvalidPaginationTokenException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'componentSummaryList': [
            {
                'arn': 'string',
                'name': 'string',
                'version': 'string',
                'platform': 'Windows'|'Linux',
                'supportedOsVersions': [
                    'string',
                ],
                'type': 'BUILD'|'TEST',
                'owner': 'string',
                'description': 'string',
                'changeDescription': 'string',
                'dateCreated': 'string',
                'tags': {
                    'string': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_components(owner=None, filters=None, maxResults=None, nextToken=None):
    """
    Returns the list of component build versions for the specified semantic version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_components(
        owner='Self'|'Shared'|'Amazon',
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type owner: string
    :param owner: The owner defines which components you want to list. By default, this request will only show components owned by your account. You can use this field to specify if you want to view components owned by yourself, by Amazon, or those components that have been shared with you by other customers.

    :type filters: list
    :param filters: The filters.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results from a list operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.\n\nname (string) --The name of the filter. Filter names are case-sensitive.\n\nvalues (list) --The filter values. Filter values are case-sensitive.\n\n(string) --\n\n\n\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum items to return in a request.

    :type nextToken: string
    :param nextToken: A token to specify where to start paginating. This is the NextToken from a previously truncated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'componentVersionList': [
        {
            'arn': 'string',
            'name': 'string',
            'version': 'string',
            'description': 'string',
            'platform': 'Windows'|'Linux',
            'supportedOsVersions': [
                'string',
            ],
            'type': 'BUILD'|'TEST',
            'owner': 'string',
            'dateCreated': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

componentVersionList (list) --
The list of component semantic versions.

(dict) --
A high-level overview of a component semantic version.

arn (string) --
The Amazon Resource Name (ARN) of the component.

name (string) --
The name of the component.

version (string) --
The semantic version of the component.

description (string) --
The description of the component.

platform (string) --
The platform of the component.

supportedOsVersions (list) --
The operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the parent image OS version during image recipe creation.

(string) --


type (string) --
The type of the component denotes whether the component is used to build the image or only to test it.

owner (string) --
The owner of the component.

dateCreated (string) --
The date that the component was created.





nextToken (string) --
The next token used for paginated responses. When this is not empty, there are additional elements that the service has not included in this request. Use this token with the next request to retrieve additional objects.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.InvalidPaginationTokenException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'componentVersionList': [
            {
                'arn': 'string',
                'name': 'string',
                'version': 'string',
                'description': 'string',
                'platform': 'Windows'|'Linux',
                'supportedOsVersions': [
                    'string',
                ],
                'type': 'BUILD'|'TEST',
                'owner': 'string',
                'dateCreated': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_distribution_configurations(filters=None, maxResults=None, nextToken=None):
    """
    Returns a list of distribution configurations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_distribution_configurations(
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type filters: list
    :param filters: The filters.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results from a list operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.\n\nname (string) --The name of the filter. Filter names are case-sensitive.\n\nvalues (list) --The filter values. Filter values are case-sensitive.\n\n(string) --\n\n\n\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum items to return in a request.

    :type nextToken: string
    :param nextToken: A token to specify where to start paginating. This is the NextToken from a previously truncated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'distributionConfigurationSummaryList': [
        {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'dateCreated': 'string',
            'dateUpdated': 'string',
            'tags': {
                'string': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

distributionConfigurationSummaryList (list) --
The list of distributions.

(dict) --
A high-level overview of a distribution configuration.

arn (string) --
The Amazon Resource Name (ARN) of the distribution configuration.

name (string) --
The name of the distribution configuration.

description (string) --
The description of the distribution configuration.

dateCreated (string) --
The date on which the distribution configuration was created.

dateUpdated (string) --
The date on which the distribution configuration was updated.

tags (dict) --
The tags associated with the distribution configuration.

(string) --
(string) --








nextToken (string) --
The next token used for paginated responses. When this is not empty, there are additional elements that the service has not included in this request. Use this token with the next request to retrieve additional objects.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.InvalidPaginationTokenException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'distributionConfigurationSummaryList': [
            {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'dateCreated': 'string',
                'dateUpdated': 'string',
                'tags': {
                    'string': 'string'
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

def list_image_build_versions(imageVersionArn=None, filters=None, maxResults=None, nextToken=None):
    """
    Returns a list of distribution configurations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_image_build_versions(
        imageVersionArn='string',
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type imageVersionArn: string
    :param imageVersionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image whose build versions you want to retrieve.\n

    :type filters: list
    :param filters: The filters.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results from a list operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.\n\nname (string) --The name of the filter. Filter names are case-sensitive.\n\nvalues (list) --The filter values. Filter values are case-sensitive.\n\n(string) --\n\n\n\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum items to return in a request.

    :type nextToken: string
    :param nextToken: A token to specify where to start paginating. This is the NextToken from a previously truncated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'imageSummaryList': [
        {
            'arn': 'string',
            'name': 'string',
            'version': 'string',
            'platform': 'Windows'|'Linux',
            'osVersion': 'string',
            'state': {
                'status': 'PENDING'|'CREATING'|'BUILDING'|'TESTING'|'DISTRIBUTING'|'INTEGRATING'|'AVAILABLE'|'CANCELLED'|'FAILED'|'DEPRECATED'|'DELETED',
                'reason': 'string'
            },
            'owner': 'string',
            'dateCreated': 'string',
            'outputResources': {
                'amis': [
                    {
                        'region': 'string',
                        'image': 'string',
                        'name': 'string',
                        'description': 'string',
                        'state': {
                            'status': 'PENDING'|'CREATING'|'BUILDING'|'TESTING'|'DISTRIBUTING'|'INTEGRATING'|'AVAILABLE'|'CANCELLED'|'FAILED'|'DEPRECATED'|'DELETED',
                            'reason': 'string'
                        }
                    },
                ]
            },
            'tags': {
                'string': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

imageSummaryList (list) --
The list of image build versions.

(dict) --
An image summary.

arn (string) --
The Amazon Resource Name (ARN) of the image.

name (string) --
The name of the image.

version (string) --
The version of the image.

platform (string) --
The platform of the image.

osVersion (string) --
The operating system version of the instance. For example, Amazon Linux 2, Ubuntu 18, or Microsoft Windows Server 2019.

state (dict) --
The state of the image.

status (string) --
The status of the image.

reason (string) --
The reason for the image\'s status.



owner (string) --
The owner of the image.

dateCreated (string) --
The date on which this image was created.

outputResources (dict) --
The output resources produced when creating this image.

amis (list) --
The EC2 AMIs created by this image.

(dict) --
Details of an EC2 AMI.

region (string) --
The AWS Region of the EC2 AMI.

image (string) --
The AMI ID of the EC2 AMI.

name (string) --
The name of the EC2 AMI.

description (string) --
The description of the EC2 AMI.

state (dict) --
Image state shows the image status and the reason for that status.

status (string) --
The status of the image.

reason (string) --
The reason for the image\'s status.









tags (dict) --
The tags of the image.

(string) --
(string) --








nextToken (string) --
The next token used for paginated responses. When this is not empty, there are additional elements that the service has not included in this request. Use this token with the next request to retrieve additional objects.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.InvalidPaginationTokenException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'imageSummaryList': [
            {
                'arn': 'string',
                'name': 'string',
                'version': 'string',
                'platform': 'Windows'|'Linux',
                'osVersion': 'string',
                'state': {
                    'status': 'PENDING'|'CREATING'|'BUILDING'|'TESTING'|'DISTRIBUTING'|'INTEGRATING'|'AVAILABLE'|'CANCELLED'|'FAILED'|'DEPRECATED'|'DELETED',
                    'reason': 'string'
                },
                'owner': 'string',
                'dateCreated': 'string',
                'outputResources': {
                    'amis': [
                        {
                            'region': 'string',
                            'image': 'string',
                            'name': 'string',
                            'description': 'string',
                            'state': {
                                'status': 'PENDING'|'CREATING'|'BUILDING'|'TESTING'|'DISTRIBUTING'|'INTEGRATING'|'AVAILABLE'|'CANCELLED'|'FAILED'|'DEPRECATED'|'DELETED',
                                'reason': 'string'
                            }
                        },
                    ]
                },
                'tags': {
                    'string': 'string'
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

def list_image_pipeline_images(imagePipelineArn=None, filters=None, maxResults=None, nextToken=None):
    """
    Returns a list of images created by the specified pipeline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_image_pipeline_images(
        imagePipelineArn='string',
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type imagePipelineArn: string
    :param imagePipelineArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image pipeline whose images you want to view.\n

    :type filters: list
    :param filters: The filters.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results from a list operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.\n\nname (string) --The name of the filter. Filter names are case-sensitive.\n\nvalues (list) --The filter values. Filter values are case-sensitive.\n\n(string) --\n\n\n\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum items to return in a request.

    :type nextToken: string
    :param nextToken: A token to specify where to start paginating. This is the NextToken from a previously truncated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'imageSummaryList': [
        {
            'arn': 'string',
            'name': 'string',
            'version': 'string',
            'platform': 'Windows'|'Linux',
            'osVersion': 'string',
            'state': {
                'status': 'PENDING'|'CREATING'|'BUILDING'|'TESTING'|'DISTRIBUTING'|'INTEGRATING'|'AVAILABLE'|'CANCELLED'|'FAILED'|'DEPRECATED'|'DELETED',
                'reason': 'string'
            },
            'owner': 'string',
            'dateCreated': 'string',
            'outputResources': {
                'amis': [
                    {
                        'region': 'string',
                        'image': 'string',
                        'name': 'string',
                        'description': 'string',
                        'state': {
                            'status': 'PENDING'|'CREATING'|'BUILDING'|'TESTING'|'DISTRIBUTING'|'INTEGRATING'|'AVAILABLE'|'CANCELLED'|'FAILED'|'DEPRECATED'|'DELETED',
                            'reason': 'string'
                        }
                    },
                ]
            },
            'tags': {
                'string': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

imageSummaryList (list) --
The list of images built by this pipeline.

(dict) --
An image summary.

arn (string) --
The Amazon Resource Name (ARN) of the image.

name (string) --
The name of the image.

version (string) --
The version of the image.

platform (string) --
The platform of the image.

osVersion (string) --
The operating system version of the instance. For example, Amazon Linux 2, Ubuntu 18, or Microsoft Windows Server 2019.

state (dict) --
The state of the image.

status (string) --
The status of the image.

reason (string) --
The reason for the image\'s status.



owner (string) --
The owner of the image.

dateCreated (string) --
The date on which this image was created.

outputResources (dict) --
The output resources produced when creating this image.

amis (list) --
The EC2 AMIs created by this image.

(dict) --
Details of an EC2 AMI.

region (string) --
The AWS Region of the EC2 AMI.

image (string) --
The AMI ID of the EC2 AMI.

name (string) --
The name of the EC2 AMI.

description (string) --
The description of the EC2 AMI.

state (dict) --
Image state shows the image status and the reason for that status.

status (string) --
The status of the image.

reason (string) --
The reason for the image\'s status.









tags (dict) --
The tags of the image.

(string) --
(string) --








nextToken (string) --
The next token used for paginated responses. When this is not empty, there are additional elements that the service has not included in this request. Use this token with the next request to retrieve additional objects.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.InvalidPaginationTokenException
imagebuilder.Client.exceptions.ResourceNotFoundException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'imageSummaryList': [
            {
                'arn': 'string',
                'name': 'string',
                'version': 'string',
                'platform': 'Windows'|'Linux',
                'osVersion': 'string',
                'state': {
                    'status': 'PENDING'|'CREATING'|'BUILDING'|'TESTING'|'DISTRIBUTING'|'INTEGRATING'|'AVAILABLE'|'CANCELLED'|'FAILED'|'DEPRECATED'|'DELETED',
                    'reason': 'string'
                },
                'owner': 'string',
                'dateCreated': 'string',
                'outputResources': {
                    'amis': [
                        {
                            'region': 'string',
                            'image': 'string',
                            'name': 'string',
                            'description': 'string',
                            'state': {
                                'status': 'PENDING'|'CREATING'|'BUILDING'|'TESTING'|'DISTRIBUTING'|'INTEGRATING'|'AVAILABLE'|'CANCELLED'|'FAILED'|'DEPRECATED'|'DELETED',
                                'reason': 'string'
                            }
                        },
                    ]
                },
                'tags': {
                    'string': 'string'
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

def list_image_pipelines(filters=None, maxResults=None, nextToken=None):
    """
    Returns a list of image pipelines.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_image_pipelines(
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type filters: list
    :param filters: The filters.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results from a list operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.\n\nname (string) --The name of the filter. Filter names are case-sensitive.\n\nvalues (list) --The filter values. Filter values are case-sensitive.\n\n(string) --\n\n\n\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum items to return in a request.

    :type nextToken: string
    :param nextToken: A token to specify where to start paginating. This is the NextToken from a previously truncated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'imagePipelineList': [
        {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'platform': 'Windows'|'Linux',
            'enhancedImageMetadataEnabled': True|False,
            'imageRecipeArn': 'string',
            'infrastructureConfigurationArn': 'string',
            'distributionConfigurationArn': 'string',
            'imageTestsConfiguration': {
                'imageTestsEnabled': True|False,
                'timeoutMinutes': 123
            },
            'schedule': {
                'scheduleExpression': 'string',
                'pipelineExecutionStartCondition': 'EXPRESSION_MATCH_ONLY'|'EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE'
            },
            'status': 'DISABLED'|'ENABLED',
            'dateCreated': 'string',
            'dateUpdated': 'string',
            'dateLastRun': 'string',
            'dateNextRun': 'string',
            'tags': {
                'string': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

imagePipelineList (list) --
The list of image pipelines.

(dict) --
Details of an image pipeline.

arn (string) --
The Amazon Resource Name (ARN) of the image pipeline.

name (string) --
The name of the image pipeline.

description (string) --
The description of the image pipeline.

platform (string) --
The platform of the image pipeline.

enhancedImageMetadataEnabled (boolean) --
Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.

imageRecipeArn (string) --
The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.

infrastructureConfigurationArn (string) --
The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.

distributionConfigurationArn (string) --
The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.

imageTestsConfiguration (dict) --
The image tests configuration of the image pipeline.

imageTestsEnabled (boolean) --
Defines if tests should be executed when building this image.

timeoutMinutes (integer) --
The maximum time in minutes that tests are permitted to run.



schedule (dict) --
The schedule of the image pipeline.

scheduleExpression (string) --
The expression determines how often EC2 Image Builder evaluates your pipelineExecutionStartCondition .

pipelineExecutionStartCondition (string) --
The condition configures when the pipeline should trigger a new image build. When the pipelineExecutionStartCondition is set to EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE , EC2 Image Builder will build a new image only when there are known changes pending. When it is set to EXPRESSION_MATCH_ONLY , it will build a new image every time the CRON expression matches the current time.



status (string) --
The status of the image pipeline.

dateCreated (string) --
The date on which this image pipeline was created.

dateUpdated (string) --
The date on which this image pipeline was last updated.

dateLastRun (string) --
The date on which this image pipeline was last run.

dateNextRun (string) --
The date on which this image pipeline will next be run.

tags (dict) --
The tags of this image pipeline.

(string) --
(string) --








nextToken (string) --
The next token used for paginated responses. When this is not empty, there are additional elements that the service has not included in this request. Use this token with the next request to retrieve additional objects.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.InvalidPaginationTokenException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'imagePipelineList': [
            {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'platform': 'Windows'|'Linux',
                'enhancedImageMetadataEnabled': True|False,
                'imageRecipeArn': 'string',
                'infrastructureConfigurationArn': 'string',
                'distributionConfigurationArn': 'string',
                'imageTestsConfiguration': {
                    'imageTestsEnabled': True|False,
                    'timeoutMinutes': 123
                },
                'schedule': {
                    'scheduleExpression': 'string',
                    'pipelineExecutionStartCondition': 'EXPRESSION_MATCH_ONLY'|'EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE'
                },
                'status': 'DISABLED'|'ENABLED',
                'dateCreated': 'string',
                'dateUpdated': 'string',
                'dateLastRun': 'string',
                'dateNextRun': 'string',
                'tags': {
                    'string': 'string'
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

def list_image_recipes(owner=None, filters=None, maxResults=None, nextToken=None):
    """
    Returns a list of image recipes.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_image_recipes(
        owner='Self'|'Shared'|'Amazon',
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type owner: string
    :param owner: The owner defines which image recipes you want to list. By default, this request will only show image recipes owned by your account. You can use this field to specify if you want to view image recipes owned by yourself, by Amazon, or those image recipes that have been shared with you by other customers.

    :type filters: list
    :param filters: The filters.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results from a list operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.\n\nname (string) --The name of the filter. Filter names are case-sensitive.\n\nvalues (list) --The filter values. Filter values are case-sensitive.\n\n(string) --\n\n\n\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum items to return in a request.

    :type nextToken: string
    :param nextToken: A token to specify where to start paginating. This is the NextToken from a previously truncated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'imageRecipeSummaryList': [
        {
            'arn': 'string',
            'name': 'string',
            'platform': 'Windows'|'Linux',
            'owner': 'string',
            'parentImage': 'string',
            'dateCreated': 'string',
            'tags': {
                'string': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

imageRecipeSummaryList (list) --
The list of image pipelines.

(dict) --
A summary of an image recipe.

arn (string) --
The Amazon Resource Name (ARN) of the image recipe.

name (string) --
The name of the image recipe.

platform (string) --
The platform of the image recipe.

owner (string) --
The owner of the image recipe.

parentImage (string) --
The parent image of the image recipe.

dateCreated (string) --
The date on which this image recipe was created.

tags (dict) --
The tags of the image recipe.

(string) --
(string) --








nextToken (string) --
The next token used for paginated responses. When this is not empty, there are additional elements that the service has not included in this request. Use this token with the next request to retrieve additional objects.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.InvalidPaginationTokenException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'imageRecipeSummaryList': [
            {
                'arn': 'string',
                'name': 'string',
                'platform': 'Windows'|'Linux',
                'owner': 'string',
                'parentImage': 'string',
                'dateCreated': 'string',
                'tags': {
                    'string': 'string'
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

def list_images(owner=None, filters=None, maxResults=None, nextToken=None):
    """
    Returns the list of image build versions for the specified semantic version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_images(
        owner='Self'|'Shared'|'Amazon',
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type owner: string
    :param owner: The owner defines which images you want to list. By default, this request will only show images owned by your account. You can use this field to specify if you want to view images owned by yourself, by Amazon, or those images that have been shared with you by other customers.

    :type filters: list
    :param filters: The filters.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results from a list operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.\n\nname (string) --The name of the filter. Filter names are case-sensitive.\n\nvalues (list) --The filter values. Filter values are case-sensitive.\n\n(string) --\n\n\n\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum items to return in a request.

    :type nextToken: string
    :param nextToken: A token to specify where to start paginating. This is the NextToken from a previously truncated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'imageVersionList': [
        {
            'arn': 'string',
            'name': 'string',
            'version': 'string',
            'platform': 'Windows'|'Linux',
            'osVersion': 'string',
            'owner': 'string',
            'dateCreated': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

imageVersionList (list) --
The list of image semantic versions.

(dict) --
An image semantic version.

arn (string) --
The Amazon Resource Name (ARN) of the image semantic version.

name (string) --
The name of the image semantic version.

version (string) --
The semantic version of the image semantic version.

platform (string) --
The platform of the image semantic version.

osVersion (string) --
The operating system version of the instance. For example, Amazon Linux 2, Ubuntu 18, or Microsoft Windows Server 2019.

owner (string) --
The owner of the image semantic version.

dateCreated (string) --
The date at which this image semantic version was created.





nextToken (string) --
The next token used for paginated responses. When this is not empty, there are additional elements that the service has not included in this request. Use this token with the next request to retrieve additional objects.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.InvalidPaginationTokenException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'imageVersionList': [
            {
                'arn': 'string',
                'name': 'string',
                'version': 'string',
                'platform': 'Windows'|'Linux',
                'osVersion': 'string',
                'owner': 'string',
                'dateCreated': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.InvalidPaginationTokenException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    
    """
    pass

def list_infrastructure_configurations(filters=None, maxResults=None, nextToken=None):
    """
    Returns a list of infrastructure configurations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_infrastructure_configurations(
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type filters: list
    :param filters: The filters.\n\n(dict) --A filter name and value pair that is used to return a more specific list of results from a list operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.\n\nname (string) --The name of the filter. Filter names are case-sensitive.\n\nvalues (list) --The filter values. Filter values are case-sensitive.\n\n(string) --\n\n\n\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum items to return in a request.

    :type nextToken: string
    :param nextToken: A token to specify where to start paginating. This is the NextToken from a previously truncated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'infrastructureConfigurationSummaryList': [
        {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'dateCreated': 'string',
            'dateUpdated': 'string',
            'tags': {
                'string': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

infrastructureConfigurationSummaryList (list) --
The list of infrastructure configurations.

(dict) --
The infrastructure used when building EC2 AMIs.

arn (string) --
The Amazon Resource Name (ARN) of the infrastructure configuration.

name (string) --
The name of the infrastructure configuration.

description (string) --
The description of the infrastructure configuration.

dateCreated (string) --
The date on which the infrastructure configuration was created.

dateUpdated (string) --
The date on which the infrastructure configuration was last updated.

tags (dict) --
The tags of the infrastructure configuration.

(string) --
(string) --








nextToken (string) --
The next token used for paginated responses. When this is not empty, there are additional elements that the service has not included in this request. Use this token with the next request to retrieve additional objects.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.InvalidPaginationTokenException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'infrastructureConfigurationSummaryList': [
            {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'dateCreated': 'string',
                'dateUpdated': 'string',
                'tags': {
                    'string': 'string'
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

def list_tags_for_resource(resourceArn=None):
    """
    Returns the list of tags for the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
tags (dict) --The tags for the specified resource.

(string) --
(string) --









Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.InvalidParameterException
imagebuilder.Client.exceptions.ResourceNotFoundException


    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.InvalidParameterException
    imagebuilder.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def put_component_policy(componentArn=None, policy=None):
    """
    Applies a policy to a component. We recommend that you call the RAM API CreateResourceShare to share resources. If you call the Image Builder API PutComponentPolicy , you must also call the RAM API PromoteResourceShareCreatedFromPolicy in order for the resource to be visible to all principals with whom the resource is shared.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_component_policy(
        componentArn='string',
        policy='string'
    )
    
    
    :type componentArn: string
    :param componentArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the component that this policy should be applied to.\n

    :type policy: string
    :param policy: [REQUIRED]\nThe policy to apply.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'componentArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

componentArn (string) --
The Amazon Resource Name (ARN) of the component that this policy was applied to.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.InvalidParameterValueException
imagebuilder.Client.exceptions.ResourceNotFoundException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'componentArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.InvalidParameterValueException
    imagebuilder.Client.exceptions.ResourceNotFoundException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    
    """
    pass

def put_image_policy(imageArn=None, policy=None):
    """
    Applies a policy to an image. We recommend that you call the RAM API CreateResourceShare to share resources. If you call the Image Builder API PutImagePolicy , you must also call the RAM API PromoteResourceShareCreatedFromPolicy in order for the resource to be visible to all principals with whom the resource is shared.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_image_policy(
        imageArn='string',
        policy='string'
    )
    
    
    :type imageArn: string
    :param imageArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image that this policy should be applied to.\n

    :type policy: string
    :param policy: [REQUIRED]\nThe policy to apply.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'imageArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

imageArn (string) --
The Amazon Resource Name (ARN) of the image that this policy was applied to.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.InvalidParameterValueException
imagebuilder.Client.exceptions.ResourceNotFoundException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'imageArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.InvalidParameterValueException
    imagebuilder.Client.exceptions.ResourceNotFoundException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    
    """
    pass

def put_image_recipe_policy(imageRecipeArn=None, policy=None):
    """
    Applies a policy to an image recipe. We recommend that you call the RAM API CreateResourceShare to share resources. If you call the Image Builder API PutImageRecipePolicy , you must also call the RAM API PromoteResourceShareCreatedFromPolicy in order for the resource to be visible to all principals with whom the resource is shared.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_image_recipe_policy(
        imageRecipeArn='string',
        policy='string'
    )
    
    
    :type imageRecipeArn: string
    :param imageRecipeArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image recipe that this policy should be applied to.\n

    :type policy: string
    :param policy: [REQUIRED]\nThe policy to apply.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'imageRecipeArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

imageRecipeArn (string) --
The Amazon Resource Name (ARN) of the image recipe that this policy was applied to.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.InvalidParameterValueException
imagebuilder.Client.exceptions.ResourceNotFoundException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException


    :return: {
        'requestId': 'string',
        'imageRecipeArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.InvalidParameterValueException
    imagebuilder.Client.exceptions.ResourceNotFoundException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    
    """
    pass

def start_image_pipeline_execution(imagePipelineArn=None, clientToken=None):
    """
    Manually triggers a pipeline to create an image.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_image_pipeline_execution(
        imagePipelineArn='string',
        clientToken='string'
    )
    
    
    :type imagePipelineArn: string
    :param imagePipelineArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image pipeline that you want to manually invoke.\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe idempotency token used to make this request idempotent.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'clientToken': 'string',
    'imageBuildVersionArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

clientToken (string) --
The idempotency token used to make this request idempotent.

imageBuildVersionArn (string) --
The Amazon Resource Name (ARN) of the image that was created by this request.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.ResourceNotFoundException
imagebuilder.Client.exceptions.IdempotentParameterMismatchException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceInUseException


    :return: {
        'requestId': 'string',
        'clientToken': 'string',
        'imageBuildVersionArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.ResourceNotFoundException
    imagebuilder.Client.exceptions.IdempotentParameterMismatchException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    imagebuilder.Client.exceptions.ResourceInUseException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds a tag to a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource that you want to tag.\n

    :type tags: dict
    :param tags: [REQUIRED]\nThe tags to apply to the resource.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.InvalidParameterException
imagebuilder.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes a tag from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource that you want to untag.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe tag keys to remove from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.InvalidParameterException
imagebuilder.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_distribution_configuration(distributionConfigurationArn=None, description=None, distributions=None, clientToken=None):
    """
    Updates a new distribution configuration. Distribution configurations define and configure the outputs of your pipeline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_distribution_configuration(
        distributionConfigurationArn='string',
        description='string',
        distributions=[
            {
                'region': 'string',
                'amiDistributionConfiguration': {
                    'name': 'string',
                    'description': 'string',
                    'amiTags': {
                        'string': 'string'
                    },
                    'launchPermission': {
                        'userIds': [
                            'string',
                        ],
                        'userGroups': [
                            'string',
                        ]
                    }
                },
                'licenseConfigurationArns': [
                    'string',
                ]
            },
        ],
        clientToken='string'
    )
    
    
    :type distributionConfigurationArn: string
    :param distributionConfigurationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the distribution configuration that you want to update.\n

    :type description: string
    :param description: The description of the distribution configuration.

    :type distributions: list
    :param distributions: [REQUIRED]\nThe distributions of the distribution configuration.\n\n(dict) --Defines the settings for a specific Region.\n\nregion (string) -- [REQUIRED]The target Region.\n\namiDistributionConfiguration (dict) --The specific AMI settings (for example, launch permissions, AMI tags).\n\nname (string) --The name of the distribution configuration.\n\ndescription (string) --The description of the distribution configuration.\n\namiTags (dict) --The tags to apply to AMIs distributed to this Region.\n\n(string) --\n(string) --\n\n\n\n\nlaunchPermission (dict) --Launch permissions can be used to configure which AWS accounts can use the AMI to launch instances.\n\nuserIds (list) --The AWS account ID.\n\n(string) --\n\n\nuserGroups (list) --The name of the group.\n\n(string) --\n\n\n\n\n\n\nlicenseConfigurationArns (list) --The License Manager Configuration to associate with the AMI in the specified Region.\n\n(string) --\n\n\n\n\n\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe idempotency token of the distribution configuration.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'clientToken': 'string',
    'distributionConfigurationArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

clientToken (string) --
The idempotency token used to make this request idempotent.

distributionConfigurationArn (string) --
The Amazon Resource Name (ARN) of the distribution configuration that was updated by this request.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.IdempotentParameterMismatchException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceInUseException
imagebuilder.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'requestId': 'string',
        'clientToken': 'string',
        'distributionConfigurationArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.IdempotentParameterMismatchException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    imagebuilder.Client.exceptions.ResourceInUseException
    imagebuilder.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def update_image_pipeline(imagePipelineArn=None, description=None, imageRecipeArn=None, infrastructureConfigurationArn=None, distributionConfigurationArn=None, imageTestsConfiguration=None, enhancedImageMetadataEnabled=None, schedule=None, status=None, clientToken=None):
    """
    Updates a new image pipeline. Image pipelines enable you to automate the creation and distribution of images.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_image_pipeline(
        imagePipelineArn='string',
        description='string',
        imageRecipeArn='string',
        infrastructureConfigurationArn='string',
        distributionConfigurationArn='string',
        imageTestsConfiguration={
            'imageTestsEnabled': True|False,
            'timeoutMinutes': 123
        },
        enhancedImageMetadataEnabled=True|False,
        schedule={
            'scheduleExpression': 'string',
            'pipelineExecutionStartCondition': 'EXPRESSION_MATCH_ONLY'|'EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE'
        },
        status='DISABLED'|'ENABLED',
        clientToken='string'
    )
    
    
    :type imagePipelineArn: string
    :param imagePipelineArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image pipeline that you want to update.\n

    :type description: string
    :param description: The description of the image pipeline.

    :type imageRecipeArn: string
    :param imageRecipeArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the image recipe that will be used to configure images updated by this image pipeline.\n

    :type infrastructureConfigurationArn: string
    :param infrastructureConfigurationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the infrastructure configuration that will be used to build images updated by this image pipeline.\n

    :type distributionConfigurationArn: string
    :param distributionConfigurationArn: The Amazon Resource Name (ARN) of the distribution configuration that will be used to configure and distribute images updated by this image pipeline.

    :type imageTestsConfiguration: dict
    :param imageTestsConfiguration: The image test configuration of the image pipeline.\n\nimageTestsEnabled (boolean) --Defines if tests should be executed when building this image.\n\ntimeoutMinutes (integer) --The maximum time in minutes that tests are permitted to run.\n\n\n

    :type enhancedImageMetadataEnabled: boolean
    :param enhancedImageMetadataEnabled: Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.

    :type schedule: dict
    :param schedule: The schedule of the image pipeline.\n\nscheduleExpression (string) --The expression determines how often EC2 Image Builder evaluates your pipelineExecutionStartCondition .\n\npipelineExecutionStartCondition (string) --The condition configures when the pipeline should trigger a new image build. When the pipelineExecutionStartCondition is set to EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE , EC2 Image Builder will build a new image only when there are known changes pending. When it is set to EXPRESSION_MATCH_ONLY , it will build a new image every time the CRON expression matches the current time.\n\n\n

    :type status: string
    :param status: The status of the image pipeline.

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe idempotency token used to make this request idempotent.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'clientToken': 'string',
    'imagePipelineArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

clientToken (string) --
The idempotency token used to make this request idempotent.

imagePipelineArn (string) --
The Amazon Resource Name (ARN) of the image pipeline that was updated by this request.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.IdempotentParameterMismatchException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceInUseException


    :return: {
        'requestId': 'string',
        'clientToken': 'string',
        'imagePipelineArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.IdempotentParameterMismatchException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    imagebuilder.Client.exceptions.ResourceInUseException
    
    """
    pass

def update_infrastructure_configuration(infrastructureConfigurationArn=None, description=None, instanceTypes=None, instanceProfileName=None, securityGroupIds=None, subnetId=None, logging=None, keyPair=None, terminateInstanceOnFailure=None, snsTopicArn=None, clientToken=None):
    """
    Updates a new infrastructure configuration. An infrastructure configuration defines the environment in which your image will be built and tested.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_infrastructure_configuration(
        infrastructureConfigurationArn='string',
        description='string',
        instanceTypes=[
            'string',
        ],
        instanceProfileName='string',
        securityGroupIds=[
            'string',
        ],
        subnetId='string',
        logging={
            's3Logs': {
                's3BucketName': 'string',
                's3KeyPrefix': 'string'
            }
        },
        keyPair='string',
        terminateInstanceOnFailure=True|False,
        snsTopicArn='string',
        clientToken='string'
    )
    
    
    :type infrastructureConfigurationArn: string
    :param infrastructureConfigurationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the infrastructure configuration that you want to update.\n

    :type description: string
    :param description: The description of the infrastructure configuration.

    :type instanceTypes: list
    :param instanceTypes: The instance types of the infrastructure configuration. You can specify one or more instance types to use for this build. The service will pick one of these instance types based on availability.\n\n(string) --\n\n

    :type instanceProfileName: string
    :param instanceProfileName: [REQUIRED]\nThe instance profile to associate with the instance used to customize your EC2 AMI.\n

    :type securityGroupIds: list
    :param securityGroupIds: The security group IDs to associate with the instance used to customize your EC2 AMI.\n\n(string) --\n\n

    :type subnetId: string
    :param subnetId: The subnet ID to place the instance used to customize your EC2 AMI in.

    :type logging: dict
    :param logging: The logging configuration of the infrastructure configuration.\n\ns3Logs (dict) --The Amazon S3 logging configuration.\n\ns3BucketName (string) --The Amazon S3 bucket in which to store the logs.\n\ns3KeyPrefix (string) --The Amazon S3 path in which to store the logs.\n\n\n\n\n

    :type keyPair: string
    :param keyPair: The key pair of the infrastructure configuration. This can be used to log on to and debug the instance used to create your image.

    :type terminateInstanceOnFailure: boolean
    :param terminateInstanceOnFailure: The terminate instance on failure setting of the infrastructure configuration. Set to false if you want Image Builder to retain the instance used to configure your AMI if the build or test phase of your workflow fails.

    :type snsTopicArn: string
    :param snsTopicArn: The SNS topic on which to send image build events.

    :type clientToken: string
    :param clientToken: [REQUIRED]\nThe idempotency token used to make this request idempotent.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'requestId': 'string',
    'clientToken': 'string',
    'infrastructureConfigurationArn': 'string'
}


Response Structure

(dict) --

requestId (string) --
The request ID that uniquely identifies this request.

clientToken (string) --
The idempotency token used to make this request idempotent.

infrastructureConfigurationArn (string) --
The Amazon Resource Name (ARN) of the infrastructure configuration that was updated by this request.







Exceptions

imagebuilder.Client.exceptions.ServiceException
imagebuilder.Client.exceptions.ClientException
imagebuilder.Client.exceptions.ServiceUnavailableException
imagebuilder.Client.exceptions.InvalidRequestException
imagebuilder.Client.exceptions.IdempotentParameterMismatchException
imagebuilder.Client.exceptions.ForbiddenException
imagebuilder.Client.exceptions.CallRateLimitExceededException
imagebuilder.Client.exceptions.ResourceInUseException


    :return: {
        'requestId': 'string',
        'clientToken': 'string',
        'infrastructureConfigurationArn': 'string'
    }
    
    
    :returns: 
    imagebuilder.Client.exceptions.ServiceException
    imagebuilder.Client.exceptions.ClientException
    imagebuilder.Client.exceptions.ServiceUnavailableException
    imagebuilder.Client.exceptions.InvalidRequestException
    imagebuilder.Client.exceptions.IdempotentParameterMismatchException
    imagebuilder.Client.exceptions.ForbiddenException
    imagebuilder.Client.exceptions.CallRateLimitExceededException
    imagebuilder.Client.exceptions.ResourceInUseException
    
    """
    pass

