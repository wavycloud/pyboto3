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

def batch_check_layer_availability(registryId=None, repositoryName=None, layerDigests=None):
    """
    Checks the availability of one or more image layers in a repository.
    When an image is pushed to a repository, each image layer is checked to verify if it has been uploaded before. If it has been uploaded, then the image layer is skipped.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_check_layer_availability(
        registryId='string',
        repositoryName='string',
        layerDigests=[
            'string',
        ]
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the image layers to check. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository that is associated with the image layers to check.\n

    :type layerDigests: list
    :param layerDigests: [REQUIRED]\nThe digests of the image layers to check.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'layers': [
        {
            'layerDigest': 'string',
            'layerAvailability': 'AVAILABLE'|'UNAVAILABLE',
            'layerSize': 123,
            'mediaType': 'string'
        },
    ],
    'failures': [
        {
            'layerDigest': 'string',
            'failureCode': 'InvalidLayerDigest'|'MissingLayerDigest',
            'failureReason': 'string'
        },
    ]
}


Response Structure

(dict) --

layers (list) --
A list of image layer objects corresponding to the image layer references in the request.

(dict) --
An object representing an Amazon ECR image layer.

layerDigest (string) --
The sha256 digest of the image layer.

layerAvailability (string) --
The availability status of the image layer.

layerSize (integer) --
The size, in bytes, of the image layer.

mediaType (string) --
The media type of the layer, such as application/vnd.docker.image.rootfs.diff.tar.gzip or application/vnd.oci.image.layer.v1.tar+gzip .





failures (list) --
Any failures associated with the call.

(dict) --
An object representing an Amazon ECR image layer failure.

layerDigest (string) --
The layer digest associated with the failure.

failureCode (string) --
The failure code associated with the failure.

failureReason (string) --
The reason for the failure.











Exceptions

ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.ServerException


    :return: {
        'layers': [
            {
                'layerDigest': 'string',
                'layerAvailability': 'AVAILABLE'|'UNAVAILABLE',
                'layerSize': 123,
                'mediaType': 'string'
            },
        ],
        'failures': [
            {
                'layerDigest': 'string',
                'failureCode': 'InvalidLayerDigest'|'MissingLayerDigest',
                'failureReason': 'string'
            },
        ]
    }
    
    
    :returns: 
    ECR.Client.exceptions.RepositoryNotFoundException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.ServerException
    
    """
    pass

def batch_delete_image(registryId=None, repositoryName=None, imageIds=None):
    """
    Deletes a list of specified images within a repository. Images are specified with either an imageTag or imageDigest .
    You can remove a tag from an image by specifying the image\'s tag in your request. When you remove the last tag from an image, the image is deleted from your repository.
    You can completely delete an image (and all of its tags) by specifying the image\'s digest in your request.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes images with the tags precise and trusty in a repository called ubuntu in the default registry for an account.
    Expected Output:
    
    :example: response = client.batch_delete_image(
        registryId='string',
        repositoryName='string',
        imageIds=[
            {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
        ]
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the image to delete. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe repository that contains the image to delete.\n

    :type imageIds: list
    :param imageIds: [REQUIRED]\nA list of image ID references that correspond to images to delete. The format of the imageIds reference is imageTag=tag or imageDigest=digest .\n\n(dict) --An object with identifying information for an Amazon ECR image.\n\nimageDigest (string) --The sha256 digest of the image manifest.\n\nimageTag (string) --The tag used for the image.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'imageIds': [
        {
            'imageDigest': 'string',
            'imageTag': 'string'
        },
    ],
    'failures': [
        {
            'imageId': {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
            'failureCode': 'InvalidImageDigest'|'InvalidImageTag'|'ImageTagDoesNotMatchDigest'|'ImageNotFound'|'MissingDigestAndTag'|'ImageReferencedByManifestList',
            'failureReason': 'string'
        },
    ]
}


Response Structure

(dict) --

imageIds (list) --
The image IDs of the deleted images.

(dict) --
An object with identifying information for an Amazon ECR image.

imageDigest (string) --
The sha256 digest of the image manifest.

imageTag (string) --
The tag used for the image.





failures (list) --
Any failures associated with the call.

(dict) --
An object representing an Amazon ECR image failure.

imageId (dict) --
The image ID associated with the failure.

imageDigest (string) --
The sha256 digest of the image manifest.

imageTag (string) --
The tag used for the image.



failureCode (string) --
The code associated with the failure.

failureReason (string) --
The reason for the failure.











Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException

Examples
This example deletes images with the tags precise and trusty in a repository called ubuntu in the default registry for an account.
response = client.batch_delete_image(
    imageIds=[
        {
            'imageTag': 'precise',
        },
    ],
    repositoryName='ubuntu',
)

print(response)


Expected Output:
{
    'failures': [
    ],
    'imageIds': [
        {
            'imageDigest': 'sha256:examplee6d1e504117a17000003d3753086354a38375961f2e665416ef4b1b2f',
            'imageTag': 'precise',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'imageIds': [
            {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
        ],
        'failures': [
            {
                'imageId': {
                    'imageDigest': 'string',
                    'imageTag': 'string'
                },
                'failureCode': 'InvalidImageDigest'|'InvalidImageTag'|'ImageTagDoesNotMatchDigest'|'ImageNotFound'|'MissingDigestAndTag'|'ImageReferencedByManifestList',
                'failureReason': 'string'
            },
        ]
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    
    """
    pass

def batch_get_image(registryId=None, repositoryName=None, imageIds=None, acceptedMediaTypes=None):
    """
    Gets detailed information for an image. Images are specified with either an imageTag or imageDigest .
    When an image is pulled, the BatchGetImage API is called once to retrieve the image manifest.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example obtains information for an image with a specified image digest ID from the repository named ubuntu in the current account.
    Expected Output:
    
    :example: response = client.batch_get_image(
        registryId='string',
        repositoryName='string',
        imageIds=[
            {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
        ],
        acceptedMediaTypes=[
            'string',
        ]
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the images to describe. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe repository that contains the images to describe.\n

    :type imageIds: list
    :param imageIds: [REQUIRED]\nA list of image ID references that correspond to images to describe. The format of the imageIds reference is imageTag=tag or imageDigest=digest .\n\n(dict) --An object with identifying information for an Amazon ECR image.\n\nimageDigest (string) --The sha256 digest of the image manifest.\n\nimageTag (string) --The tag used for the image.\n\n\n\n\n

    :type acceptedMediaTypes: list
    :param acceptedMediaTypes: The accepted media types for the request.\nValid values: application/vnd.docker.distribution.manifest.v1+json | application/vnd.docker.distribution.manifest.v2+json | application/vnd.oci.image.manifest.v1+json\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'images': [
        {
            'registryId': 'string',
            'repositoryName': 'string',
            'imageId': {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
            'imageManifest': 'string',
            'imageManifestMediaType': 'string'
        },
    ],
    'failures': [
        {
            'imageId': {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
            'failureCode': 'InvalidImageDigest'|'InvalidImageTag'|'ImageTagDoesNotMatchDigest'|'ImageNotFound'|'MissingDigestAndTag'|'ImageReferencedByManifestList',
            'failureReason': 'string'
        },
    ]
}


Response Structure

(dict) --

images (list) --
A list of image objects corresponding to the image references in the request.

(dict) --
An object representing an Amazon ECR image.

registryId (string) --
The AWS account ID associated with the registry containing the image.

repositoryName (string) --
The name of the repository associated with the image.

imageId (dict) --
An object containing the image tag and image digest associated with an image.

imageDigest (string) --
The sha256 digest of the image manifest.

imageTag (string) --
The tag used for the image.



imageManifest (string) --
The image manifest associated with the image.

imageManifestMediaType (string) --
The media type associated with the image manifest.





failures (list) --
Any failures associated with the call.

(dict) --
An object representing an Amazon ECR image failure.

imageId (dict) --
The image ID associated with the failure.

imageDigest (string) --
The sha256 digest of the image manifest.

imageTag (string) --
The tag used for the image.



failureCode (string) --
The code associated with the failure.

failureReason (string) --
The reason for the failure.











Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException

Examples
This example obtains information for an image with a specified image digest ID from the repository named ubuntu in the current account.
response = client.batch_get_image(
    imageIds=[
        {
            'imageTag': 'precise',
        },
    ],
    repositoryName='ubuntu',
)

print(response)


Expected Output:
{
    'failures': [
    ],
    'images': [
        {
            'imageId': {
                'imageDigest': 'sha256:example76bdff6d83a09ba2a818f0d00000063724a9ac3ba5019c56f74ebf42a',
                'imageTag': 'precise',
            },
            'imageManifest': '{\
 "schemaVersion": 1,\
 "name": "ubuntu",\
 "tag": "precise",\
...',
            'registryId': '244698725403',
            'repositoryName': 'ubuntu',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'images': [
            {
                'registryId': 'string',
                'repositoryName': 'string',
                'imageId': {
                    'imageDigest': 'string',
                    'imageTag': 'string'
                },
                'imageManifest': 'string',
                'imageManifestMediaType': 'string'
            },
        ],
        'failures': [
            {
                'imageId': {
                    'imageDigest': 'string',
                    'imageTag': 'string'
                },
                'failureCode': 'InvalidImageDigest'|'InvalidImageTag'|'ImageTagDoesNotMatchDigest'|'ImageNotFound'|'MissingDigestAndTag'|'ImageReferencedByManifestList',
                'failureReason': 'string'
            },
        ]
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def complete_layer_upload(registryId=None, repositoryName=None, uploadId=None, layerDigests=None):
    """
    Informs Amazon ECR that the image layer upload has completed for a specified registry, repository name, and upload ID. You can optionally provide a sha256 digest of the image layer for data validation purposes.
    When an image is pushed, the CompleteLayerUpload API is called once per each new image layer to verify that the upload has completed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.complete_layer_upload(
        registryId='string',
        repositoryName='string',
        uploadId='string',
        layerDigests=[
            'string',
        ]
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry to which to upload layers. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository to associate with the image layer.\n

    :type uploadId: string
    :param uploadId: [REQUIRED]\nThe upload ID from a previous InitiateLayerUpload operation to associate with the image layer.\n

    :type layerDigests: list
    :param layerDigests: [REQUIRED]\nThe sha256 digest of the image layer.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'registryId': 'string',
    'repositoryName': 'string',
    'uploadId': 'string',
    'layerDigest': 'string'
}


Response Structure

(dict) --

registryId (string) --
The registry ID associated with the request.

repositoryName (string) --
The repository name associated with the request.

uploadId (string) --
The upload ID associated with the layer.

layerDigest (string) --
The sha256 digest of the image layer.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.UploadNotFoundException
ECR.Client.exceptions.InvalidLayerException
ECR.Client.exceptions.LayerPartTooSmallException
ECR.Client.exceptions.LayerAlreadyExistsException
ECR.Client.exceptions.EmptyUploadException


    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'uploadId': 'string',
        'layerDigest': 'string'
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    ECR.Client.exceptions.UploadNotFoundException
    ECR.Client.exceptions.InvalidLayerException
    ECR.Client.exceptions.LayerPartTooSmallException
    ECR.Client.exceptions.LayerAlreadyExistsException
    ECR.Client.exceptions.EmptyUploadException
    
    """
    pass

def create_repository(repositoryName=None, tags=None, imageTagMutability=None, imageScanningConfiguration=None):
    """
    Creates a repository. For more information, see Amazon ECR Repositories in the Amazon Elastic Container Registry User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example creates a repository called nginx-web-app inside the project-a namespace in the default registry for an account.
    Expected Output:
    
    :example: response = client.create_repository(
        repositoryName='string',
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        imageTagMutability='MUTABLE'|'IMMUTABLE',
        imageScanningConfiguration={
            'scanOnPush': True|False
        }
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name to use for the repository. The repository name may be specified on its own (such as nginx-web-app ) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app ).\n

    :type tags: list
    :param tags: The metadata that you apply to the repository to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\n(dict) --The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\nKey (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.\n\nValue (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).\n\n\n\n\n

    :type imageTagMutability: string
    :param imageTagMutability: The tag mutability setting for the repository. If this parameter is omitted, the default setting of MUTABLE will be used which will allow image tags to be overwritten. If IMMUTABLE is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.

    :type imageScanningConfiguration: dict
    :param imageScanningConfiguration: The image scanning configuration for the repository. This setting determines whether images are scanned for known vulnerabilities after being pushed to the repository.\n\nscanOnPush (boolean) --The setting that determines whether images are scanned after being pushed to a repository. If set to true , images will be scanned after being pushed. If this parameter is not specified, it will default to false and images will not be scanned unless a scan is manually started with the StartImageScan API.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'repository': {
        'repositoryArn': 'string',
        'registryId': 'string',
        'repositoryName': 'string',
        'repositoryUri': 'string',
        'createdAt': datetime(2015, 1, 1),
        'imageTagMutability': 'MUTABLE'|'IMMUTABLE',
        'imageScanningConfiguration': {
            'scanOnPush': True|False
        }
    }
}


Response Structure

(dict) --

repository (dict) --
The repository that was created.

repositoryArn (string) --
The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the arn:aws:ecr namespace, followed by the region of the repository, AWS account ID of the repository owner, repository namespace, and repository name. For example, arn:aws:ecr:region:012345678910:repository/test .

registryId (string) --
The AWS account ID associated with the registry that contains the repository.

repositoryName (string) --
The name of the repository.

repositoryUri (string) --
The URI for the repository. You can use this URI for Docker push or pull operations.

createdAt (datetime) --
The date and time, in JavaScript date format, when the repository was created.

imageTagMutability (string) --
The tag mutability setting for the repository.

imageScanningConfiguration (dict) --
The image scanning configuration for a repository.

scanOnPush (boolean) --
The setting that determines whether images are scanned after being pushed to a repository. If set to true , images will be scanned after being pushed. If this parameter is not specified, it will default to false and images will not be scanned unless a scan is manually started with the  StartImageScan API.











Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.InvalidTagParameterException
ECR.Client.exceptions.TooManyTagsException
ECR.Client.exceptions.RepositoryAlreadyExistsException
ECR.Client.exceptions.LimitExceededException

Examples
This example creates a repository called nginx-web-app inside the project-a namespace in the default registry for an account.
response = client.create_repository(
    repositoryName='project-a/nginx-web-app',
)

print(response)


Expected Output:
{
    'repository': {
        'registryId': '012345678901',
        'repositoryArn': 'arn:aws:ecr:us-west-2:012345678901:repository/project-a/nginx-web-app',
        'repositoryName': 'project-a/nginx-web-app',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'repository': {
            'repositoryArn': 'string',
            'registryId': 'string',
            'repositoryName': 'string',
            'repositoryUri': 'string',
            'createdAt': datetime(2015, 1, 1),
            'imageTagMutability': 'MUTABLE'|'IMMUTABLE',
            'imageScanningConfiguration': {
                'scanOnPush': True|False
            }
        }
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.InvalidTagParameterException
    ECR.Client.exceptions.TooManyTagsException
    ECR.Client.exceptions.RepositoryAlreadyExistsException
    ECR.Client.exceptions.LimitExceededException
    
    """
    pass

def delete_lifecycle_policy(registryId=None, repositoryName=None):
    """
    Deletes the lifecycle policy associated with the specified repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_lifecycle_policy(
        registryId='string',
        repositoryName='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'registryId': 'string',
    'repositoryName': 'string',
    'lifecyclePolicyText': 'string',
    'lastEvaluatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --

registryId (string) --
The registry ID associated with the request.

repositoryName (string) --
The repository name associated with the request.

lifecyclePolicyText (string) --
The JSON lifecycle policy text.

lastEvaluatedAt (datetime) --
The time stamp of the last time that the lifecycle policy was run.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.LifecyclePolicyNotFoundException


    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'lifecyclePolicyText': 'string',
        'lastEvaluatedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    ECR.Client.exceptions.LifecyclePolicyNotFoundException
    
    """
    pass

def delete_repository(registryId=None, repositoryName=None, force=None):
    """
    Deletes a repository. If the repository contains images, you must either delete all images in the repository or use the force option to delete the repository.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example force deletes a repository named ubuntu in the default registry for an account. The force parameter is required if the repository contains images.
    Expected Output:
    
    :example: response = client.delete_repository(
        registryId='string',
        repositoryName='string',
        force=True|False
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository to delete. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository to delete.\n

    :type force: boolean
    :param force: If a repository contains images, forces the deletion.

    :rtype: dict

ReturnsResponse Syntax
{
    'repository': {
        'repositoryArn': 'string',
        'registryId': 'string',
        'repositoryName': 'string',
        'repositoryUri': 'string',
        'createdAt': datetime(2015, 1, 1),
        'imageTagMutability': 'MUTABLE'|'IMMUTABLE',
        'imageScanningConfiguration': {
            'scanOnPush': True|False
        }
    }
}


Response Structure

(dict) --

repository (dict) --
The repository that was deleted.

repositoryArn (string) --
The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the arn:aws:ecr namespace, followed by the region of the repository, AWS account ID of the repository owner, repository namespace, and repository name. For example, arn:aws:ecr:region:012345678910:repository/test .

registryId (string) --
The AWS account ID associated with the registry that contains the repository.

repositoryName (string) --
The name of the repository.

repositoryUri (string) --
The URI for the repository. You can use this URI for Docker push or pull operations.

createdAt (datetime) --
The date and time, in JavaScript date format, when the repository was created.

imageTagMutability (string) --
The tag mutability setting for the repository.

imageScanningConfiguration (dict) --
The image scanning configuration for a repository.

scanOnPush (boolean) --
The setting that determines whether images are scanned after being pushed to a repository. If set to true , images will be scanned after being pushed. If this parameter is not specified, it will default to false and images will not be scanned unless a scan is manually started with the  StartImageScan API.











Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.RepositoryNotEmptyException

Examples
This example force deletes a repository named ubuntu in the default registry for an account. The force parameter is required if the repository contains images.
response = client.delete_repository(
    force=True,
    repositoryName='ubuntu',
)

print(response)


Expected Output:
{
    'repository': {
        'registryId': '012345678901',
        'repositoryArn': 'arn:aws:ecr:us-west-2:012345678901:repository/ubuntu',
        'repositoryName': 'ubuntu',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'repository': {
            'repositoryArn': 'string',
            'registryId': 'string',
            'repositoryName': 'string',
            'repositoryUri': 'string',
            'createdAt': datetime(2015, 1, 1),
            'imageTagMutability': 'MUTABLE'|'IMMUTABLE',
            'imageScanningConfiguration': {
                'scanOnPush': True|False
            }
        }
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    ECR.Client.exceptions.RepositoryNotEmptyException
    
    """
    pass

def delete_repository_policy(registryId=None, repositoryName=None):
    """
    Deletes the repository policy associated with the specified repository.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the policy associated with the repository named ubuntu in the current account.
    Expected Output:
    
    :example: response = client.delete_repository_policy(
        registryId='string',
        repositoryName='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository policy to delete. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository that is associated with the repository policy to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'registryId': 'string',
    'repositoryName': 'string',
    'policyText': 'string'
}


Response Structure

(dict) --

registryId (string) --
The registry ID associated with the request.

repositoryName (string) --
The repository name associated with the request.

policyText (string) --
The JSON repository policy that was deleted from the repository.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.RepositoryPolicyNotFoundException

Examples
This example deletes the policy associated with the repository named ubuntu in the current account.
response = client.delete_repository_policy(
    repositoryName='ubuntu',
)

print(response)


Expected Output:
{
    'policyText': '{ ... }',
    'registryId': '012345678901',
    'repositoryName': 'ubuntu',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'policyText': 'string'
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    ECR.Client.exceptions.RepositoryPolicyNotFoundException
    
    """
    pass

def describe_image_scan_findings(registryId=None, repositoryName=None, imageId=None, nextToken=None, maxResults=None):
    """
    Returns the scan findings for the specified image.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_image_scan_findings(
        registryId='string',
        repositoryName='string',
        imageId={
            'imageDigest': 'string',
            'imageTag': 'string'
        },
        nextToken='string',
        maxResults=123
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository in which to describe the image scan findings for. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe repository for the image for which to describe the scan findings.\n

    :type imageId: dict
    :param imageId: [REQUIRED]\nAn object with identifying information for an Amazon ECR image.\n\nimageDigest (string) --The sha256 digest of the image manifest.\n\nimageTag (string) --The tag used for the image.\n\n\n

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeImageScanFindings request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.

    :type maxResults: integer
    :param maxResults: The maximum number of image scan results returned by DescribeImageScanFindings in paginated output. When this parameter is used, DescribeImageScanFindings only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeImageScanFindings request with the returned nextToken value. This value can be between 1 and 1000. If this parameter is not used, then DescribeImageScanFindings returns up to 100 results and a nextToken value, if applicable.

    :rtype: dict

ReturnsResponse Syntax
{
    'registryId': 'string',
    'repositoryName': 'string',
    'imageId': {
        'imageDigest': 'string',
        'imageTag': 'string'
    },
    'imageScanStatus': {
        'status': 'IN_PROGRESS'|'COMPLETE'|'FAILED',
        'description': 'string'
    },
    'imageScanFindings': {
        'imageScanCompletedAt': datetime(2015, 1, 1),
        'vulnerabilitySourceUpdatedAt': datetime(2015, 1, 1),
        'findings': [
            {
                'name': 'string',
                'description': 'string',
                'uri': 'string',
                'severity': 'INFORMATIONAL'|'LOW'|'MEDIUM'|'HIGH'|'CRITICAL'|'UNDEFINED',
                'attributes': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            },
        ],
        'findingSeverityCounts': {
            'string': 123
        }
    },
    'nextToken': 'string'
}


Response Structure

(dict) --

registryId (string) --
The registry ID associated with the request.

repositoryName (string) --
The repository name associated with the request.

imageId (dict) --
An object with identifying information for an Amazon ECR image.

imageDigest (string) --
The sha256 digest of the image manifest.

imageTag (string) --
The tag used for the image.



imageScanStatus (dict) --
The current state of the scan.

status (string) --
The current state of an image scan.

description (string) --
The description of the image scan status.



imageScanFindings (dict) --
The information contained in the image scan findings.

imageScanCompletedAt (datetime) --
The time of the last completed image scan.

vulnerabilitySourceUpdatedAt (datetime) --
The time when the vulnerability data was last scanned.

findings (list) --
The findings from the image scan.

(dict) --
Contains information about an image scan finding.

name (string) --
The name associated with the finding, usually a CVE number.

description (string) --
The description of the finding.

uri (string) --
A link containing additional details about the security vulnerability.

severity (string) --
The finding severity.

attributes (list) --
A collection of attributes of the host from which the finding is generated.

(dict) --
This data type is used in the  ImageScanFinding data type.

key (string) --
The attribute key.

value (string) --
The value assigned to the attribute key.









findingSeverityCounts (dict) --
The image vulnerability counts, sorted by severity.

(string) --
(integer) --






nextToken (string) --
The nextToken value to include in a future DescribeImageScanFindings request. When the results of a DescribeImageScanFindings request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.ImageNotFoundException
ECR.Client.exceptions.ScanNotFoundException


    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'imageId': {
            'imageDigest': 'string',
            'imageTag': 'string'
        },
        'imageScanStatus': {
            'status': 'IN_PROGRESS'|'COMPLETE'|'FAILED',
            'description': 'string'
        },
        'imageScanFindings': {
            'imageScanCompletedAt': datetime(2015, 1, 1),
            'vulnerabilitySourceUpdatedAt': datetime(2015, 1, 1),
            'findings': [
                {
                    'name': 'string',
                    'description': 'string',
                    'uri': 'string',
                    'severity': 'INFORMATIONAL'|'LOW'|'MEDIUM'|'HIGH'|'CRITICAL'|'UNDEFINED',
                    'attributes': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ]
                },
            ],
            'findingSeverityCounts': {
                'string': 123
            }
        },
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (integer) --
    
    
    
    """
    pass

def describe_images(registryId=None, repositoryName=None, imageIds=None, nextToken=None, maxResults=None, filter=None):
    """
    Returns metadata about the images in a repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_images(
        registryId='string',
        repositoryName='string',
        imageIds=[
            {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
        ],
        nextToken='string',
        maxResults=123,
        filter={
            'tagStatus': 'TAGGED'|'UNTAGGED'|'ANY'
        }
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository in which to describe images. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe repository that contains the images to describe.\n

    :type imageIds: list
    :param imageIds: The list of image IDs for the requested repository.\n\n(dict) --An object with identifying information for an Amazon ECR image.\n\nimageDigest (string) --The sha256 digest of the image manifest.\n\nimageTag (string) --The tag used for the image.\n\n\n\n\n

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeImages request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return. This option cannot be used when you specify images with imageIds .

    :type maxResults: integer
    :param maxResults: The maximum number of repository results returned by DescribeImages in paginated output. When this parameter is used, DescribeImages only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeImages request with the returned nextToken value. This value can be between 1 and 1000. If this parameter is not used, then DescribeImages returns up to 100 results and a nextToken value, if applicable. This option cannot be used when you specify images with imageIds .

    :type filter: dict
    :param filter: The filter key and value with which to filter your DescribeImages results.\n\ntagStatus (string) --The tag status with which to filter your DescribeImages results. You can filter results based on whether they are TAGGED or UNTAGGED .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'imageDetails': [
        {
            'registryId': 'string',
            'repositoryName': 'string',
            'imageDigest': 'string',
            'imageTags': [
                'string',
            ],
            'imageSizeInBytes': 123,
            'imagePushedAt': datetime(2015, 1, 1),
            'imageScanStatus': {
                'status': 'IN_PROGRESS'|'COMPLETE'|'FAILED',
                'description': 'string'
            },
            'imageScanFindingsSummary': {
                'imageScanCompletedAt': datetime(2015, 1, 1),
                'vulnerabilitySourceUpdatedAt': datetime(2015, 1, 1),
                'findingSeverityCounts': {
                    'string': 123
                }
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

imageDetails (list) --
A list of  ImageDetail objects that contain data about the image.

(dict) --
An object that describes an image returned by a  DescribeImages operation.

registryId (string) --
The AWS account ID associated with the registry to which this image belongs.

repositoryName (string) --
The name of the repository to which this image belongs.

imageDigest (string) --
The sha256 digest of the image manifest.

imageTags (list) --
The list of tags associated with this image.

(string) --


imageSizeInBytes (integer) --
The size, in bytes, of the image in the repository.
If the image is a manifest list, this will be the max size of all manifests in the list.

Note
Beginning with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the docker images command shows the uncompressed image size, so it may return a larger image size than the image sizes returned by  DescribeImages .


imagePushedAt (datetime) --
The date and time, expressed in standard JavaScript date format, at which the current image was pushed to the repository.

imageScanStatus (dict) --
The current state of the scan.

status (string) --
The current state of an image scan.

description (string) --
The description of the image scan status.



imageScanFindingsSummary (dict) --
A summary of the last completed image scan.

imageScanCompletedAt (datetime) --
The time of the last completed image scan.

vulnerabilitySourceUpdatedAt (datetime) --
The time when the vulnerability data was last scanned.

findingSeverityCounts (dict) --
The image vulnerability counts, sorted by severity.

(string) --
(integer) --










nextToken (string) --
The nextToken value to include in a future DescribeImages request. When the results of a DescribeImages request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.ImageNotFoundException


    :return: {
        'imageDetails': [
            {
                'registryId': 'string',
                'repositoryName': 'string',
                'imageDigest': 'string',
                'imageTags': [
                    'string',
                ],
                'imageSizeInBytes': 123,
                'imagePushedAt': datetime(2015, 1, 1),
                'imageScanStatus': {
                    'status': 'IN_PROGRESS'|'COMPLETE'|'FAILED',
                    'description': 'string'
                },
                'imageScanFindingsSummary': {
                    'imageScanCompletedAt': datetime(2015, 1, 1),
                    'vulnerabilitySourceUpdatedAt': datetime(2015, 1, 1),
                    'findingSeverityCounts': {
                        'string': 123
                    }
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_repositories(registryId=None, repositoryNames=None, nextToken=None, maxResults=None):
    """
    Describes image repositories in a registry.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example obtains a list and description of all repositories in the default registry to which the current user has access.
    Expected Output:
    
    :example: response = client.describe_repositories(
        registryId='string',
        repositoryNames=[
            'string',
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repositories to be described. If you do not specify a registry, the default registry is assumed.

    :type repositoryNames: list
    :param repositoryNames: A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described.\n\n(string) --\n\n

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeRepositories request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return. This option cannot be used when you specify repositories with repositoryNames .\n\nNote\nThis token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.\n\n

    :type maxResults: integer
    :param maxResults: The maximum number of repository results returned by DescribeRepositories in paginated output. When this parameter is used, DescribeRepositories only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeRepositories request with the returned nextToken value. This value can be between 1 and 1000. If this parameter is not used, then DescribeRepositories returns up to 100 results and a nextToken value, if applicable. This option cannot be used when you specify repositories with repositoryNames .

    :rtype: dict

ReturnsResponse Syntax
{
    'repositories': [
        {
            'repositoryArn': 'string',
            'registryId': 'string',
            'repositoryName': 'string',
            'repositoryUri': 'string',
            'createdAt': datetime(2015, 1, 1),
            'imageTagMutability': 'MUTABLE'|'IMMUTABLE',
            'imageScanningConfiguration': {
                'scanOnPush': True|False
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

repositories (list) --
A list of repository objects corresponding to valid repositories.

(dict) --
An object representing a repository.

repositoryArn (string) --
The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the arn:aws:ecr namespace, followed by the region of the repository, AWS account ID of the repository owner, repository namespace, and repository name. For example, arn:aws:ecr:region:012345678910:repository/test .

registryId (string) --
The AWS account ID associated with the registry that contains the repository.

repositoryName (string) --
The name of the repository.

repositoryUri (string) --
The URI for the repository. You can use this URI for Docker push or pull operations.

createdAt (datetime) --
The date and time, in JavaScript date format, when the repository was created.

imageTagMutability (string) --
The tag mutability setting for the repository.

imageScanningConfiguration (dict) --
The image scanning configuration for a repository.

scanOnPush (boolean) --
The setting that determines whether images are scanned after being pushed to a repository. If set to true , images will be scanned after being pushed. If this parameter is not specified, it will default to false and images will not be scanned unless a scan is manually started with the  StartImageScan API.







nextToken (string) --
The nextToken value to include in a future DescribeRepositories request. When the results of a DescribeRepositories request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException

Examples
The following example obtains a list and description of all repositories in the default registry to which the current user has access.
response = client.describe_repositories(
)

print(response)


Expected Output:
{
    'repositories': [
        {
            'registryId': '012345678910',
            'repositoryArn': 'arn:aws:ecr:us-west-2:012345678910:repository/ubuntu',
            'repositoryName': 'ubuntu',
        },
        {
            'registryId': '012345678910',
            'repositoryArn': 'arn:aws:ecr:us-west-2:012345678910:repository/test',
            'repositoryName': 'test',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'repositories': [
            {
                'repositoryArn': 'string',
                'registryId': 'string',
                'repositoryName': 'string',
                'repositoryUri': 'string',
                'createdAt': datetime(2015, 1, 1),
                'imageTagMutability': 'MUTABLE'|'IMMUTABLE',
                'imageScanningConfiguration': {
                    'scanOnPush': True|False
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    
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

def get_authorization_token(registryIds=None):
    """
    Retrieves an authorization token. An authorization token represents your IAM authentication credentials and can be used to access any Amazon ECR registry that your IAM principal has access to. The authorization token is valid for 12 hours.
    The authorizationToken returned is a base64 encoded string that can be decoded and used in a docker login command to authenticate to a registry. The AWS CLI offers an get-login-password command that simplifies the login process. For more information, see Registry Authentication in the Amazon Elastic Container Registry User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_authorization_token(
        registryIds=[
            'string',
        ]
    )
    
    
    :type registryIds: list
    :param registryIds: A list of AWS account IDs that are associated with the registries for which to get AuthorizationData objects. If you do not specify a registry, the default registry is assumed.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'authorizationData': [
        {
            'authorizationToken': 'string',
            'expiresAt': datetime(2015, 1, 1),
            'proxyEndpoint': 'string'
        },
    ]
}


Response Structure

(dict) --
authorizationData (list) --A list of authorization token data objects that correspond to the registryIds values in the request.

(dict) --An object representing authorization data for an Amazon ECR registry.

authorizationToken (string) --A base64-encoded string that contains authorization data for the specified Amazon ECR registry. When the string is decoded, it is presented in the format user:password for private registry authentication using docker login .

expiresAt (datetime) --The Unix time in seconds and milliseconds when the authorization token expires. Authorization tokens are valid for 12 hours.

proxyEndpoint (string) --The registry URL to use for this authorization token in a docker login command. The Amazon ECR registry URL format is https://aws_account_id.dkr.ecr.region.amazonaws.com . For example, https://012345678910.dkr.ecr.us-east-1.amazonaws.com ..










Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException


    :return: {
        'authorizationData': [
            {
                'authorizationToken': 'string',
                'expiresAt': datetime(2015, 1, 1),
                'proxyEndpoint': 'string'
            },
        ]
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    
    """
    pass

def get_download_url_for_layer(registryId=None, repositoryName=None, layerDigest=None):
    """
    Retrieves the pre-signed Amazon S3 download URL corresponding to an image layer. You can only get URLs for image layers that are referenced in an image.
    When an image is pulled, the GetDownloadUrlForLayer API is called once per image layer that is not already cached.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_download_url_for_layer(
        registryId='string',
        repositoryName='string',
        layerDigest='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the image layer to download. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository that is associated with the image layer to download.\n

    :type layerDigest: string
    :param layerDigest: [REQUIRED]\nThe digest of the image layer to download.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'downloadUrl': 'string',
    'layerDigest': 'string'
}


Response Structure

(dict) --

downloadUrl (string) --
The pre-signed Amazon S3 download URL for the requested layer.

layerDigest (string) --
The digest of the image layer to download.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.LayersNotFoundException
ECR.Client.exceptions.LayerInaccessibleException
ECR.Client.exceptions.RepositoryNotFoundException


    :return: {
        'downloadUrl': 'string',
        'layerDigest': 'string'
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.LayersNotFoundException
    ECR.Client.exceptions.LayerInaccessibleException
    ECR.Client.exceptions.RepositoryNotFoundException
    
    """
    pass

def get_lifecycle_policy(registryId=None, repositoryName=None):
    """
    Retrieves the lifecycle policy for the specified repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_lifecycle_policy(
        registryId='string',
        repositoryName='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'registryId': 'string',
    'repositoryName': 'string',
    'lifecyclePolicyText': 'string',
    'lastEvaluatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --

registryId (string) --
The registry ID associated with the request.

repositoryName (string) --
The repository name associated with the request.

lifecyclePolicyText (string) --
The JSON lifecycle policy text.

lastEvaluatedAt (datetime) --
The time stamp of the last time that the lifecycle policy was run.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.LifecyclePolicyNotFoundException


    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'lifecyclePolicyText': 'string',
        'lastEvaluatedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    ECR.Client.exceptions.LifecyclePolicyNotFoundException
    
    """
    pass

def get_lifecycle_policy_preview(registryId=None, repositoryName=None, imageIds=None, nextToken=None, maxResults=None, filter=None):
    """
    Retrieves the results of the lifecycle policy preview request for the specified repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_lifecycle_policy_preview(
        registryId='string',
        repositoryName='string',
        imageIds=[
            {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
        ],
        nextToken='string',
        maxResults=123,
        filter={
            'tagStatus': 'TAGGED'|'UNTAGGED'|'ANY'
        }
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository.\n

    :type imageIds: list
    :param imageIds: The list of imageIDs to be included.\n\n(dict) --An object with identifying information for an Amazon ECR image.\n\nimageDigest (string) --The sha256 digest of the image manifest.\n\nimageTag (string) --The tag used for the image.\n\n\n\n\n

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated GetLifecyclePolicyPreviewRequest request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return. This option cannot be used when you specify images with imageIds .

    :type maxResults: integer
    :param maxResults: The maximum number of repository results returned by GetLifecyclePolicyPreviewRequest in paginated output. When this parameter is used, GetLifecyclePolicyPreviewRequest only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another GetLifecyclePolicyPreviewRequest request with the returned nextToken value. This value can be between 1 and 1000. If this parameter is not used, then GetLifecyclePolicyPreviewRequest returns up to 100 results and a nextToken value, if applicable. This option cannot be used when you specify images with imageIds .

    :type filter: dict
    :param filter: An optional parameter that filters results based on image tag status and all tags, if tagged.\n\ntagStatus (string) --The tag status of the image.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'registryId': 'string',
    'repositoryName': 'string',
    'lifecyclePolicyText': 'string',
    'status': 'IN_PROGRESS'|'COMPLETE'|'EXPIRED'|'FAILED',
    'nextToken': 'string',
    'previewResults': [
        {
            'imageTags': [
                'string',
            ],
            'imageDigest': 'string',
            'imagePushedAt': datetime(2015, 1, 1),
            'action': {
                'type': 'EXPIRE'
            },
            'appliedRulePriority': 123
        },
    ],
    'summary': {
        'expiringImageTotalCount': 123
    }
}


Response Structure

(dict) --

registryId (string) --
The registry ID associated with the request.

repositoryName (string) --
The repository name associated with the request.

lifecyclePolicyText (string) --
The JSON lifecycle policy text.

status (string) --
The status of the lifecycle policy preview request.

nextToken (string) --
The nextToken value to include in a future GetLifecyclePolicyPreview request. When the results of a GetLifecyclePolicyPreview request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.

previewResults (list) --
The results of the lifecycle policy preview request.

(dict) --
The result of the lifecycle policy preview.

imageTags (list) --
The list of tags associated with this image.

(string) --


imageDigest (string) --
The sha256 digest of the image manifest.

imagePushedAt (datetime) --
The date and time, expressed in standard JavaScript date format, at which the current image was pushed to the repository.

action (dict) --
The type of action to be taken.

type (string) --
The type of action to be taken.



appliedRulePriority (integer) --
The priority of the applied rule.





summary (dict) --
The list of images that is returned as a result of the action.

expiringImageTotalCount (integer) --
The number of expiring images.









Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.LifecyclePolicyPreviewNotFoundException


    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'lifecyclePolicyText': 'string',
        'status': 'IN_PROGRESS'|'COMPLETE'|'EXPIRED'|'FAILED',
        'nextToken': 'string',
        'previewResults': [
            {
                'imageTags': [
                    'string',
                ],
                'imageDigest': 'string',
                'imagePushedAt': datetime(2015, 1, 1),
                'action': {
                    'type': 'EXPIRE'
                },
                'appliedRulePriority': 123
            },
        ],
        'summary': {
            'expiringImageTotalCount': 123
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

def get_repository_policy(registryId=None, repositoryName=None):
    """
    Retrieves the repository policy for the specified repository.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example obtains the repository policy for the repository named ubuntu.
    Expected Output:
    
    :example: response = client.get_repository_policy(
        registryId='string',
        repositoryName='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository with the policy to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'registryId': 'string',
    'repositoryName': 'string',
    'policyText': 'string'
}


Response Structure

(dict) --

registryId (string) --
The registry ID associated with the request.

repositoryName (string) --
The repository name associated with the request.

policyText (string) --
The JSON repository policy text associated with the repository.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.RepositoryPolicyNotFoundException

Examples
This example obtains the repository policy for the repository named ubuntu.
response = client.get_repository_policy(
    repositoryName='ubuntu',
)

print(response)


Expected Output:
{
    'policyText': '{\
  "Version" : "2008-10-17",\
  "Statement" : [ {\
    "Sid" : "new statement",\
    "Effect" : "Allow",\
    "Principal" : {\
     "AWS" : "arn:aws:iam::012345678901:role/CodeDeployDemo"\
    },\
"Action" : [ "ecr:GetDownloadUrlForLayer", "ecr:BatchGetImage", "ecr:BatchCheckLayerAvailability" ]\
 } ]\
}',
    'registryId': '012345678901',
    'repositoryName': 'ubuntu',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'policyText': 'string'
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    ECR.Client.exceptions.RepositoryPolicyNotFoundException
    
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

def initiate_layer_upload(registryId=None, repositoryName=None):
    """
    Notifies Amazon ECR that you intend to upload an image layer.
    When an image is pushed, the InitiateLayerUpload API is called once per image layer that has not already been uploaded. Whether or not an image layer has been uploaded is determined by the BatchCheckLayerAvailability API action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.initiate_layer_upload(
        registryId='string',
        repositoryName='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry to which you intend to upload layers. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository to which you intend to upload layers.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'uploadId': 'string',
    'partSize': 123
}


Response Structure

(dict) --

uploadId (string) --
The upload ID for the layer upload. This parameter is passed to further  UploadLayerPart and  CompleteLayerUpload operations.

partSize (integer) --
The size, in bytes, that Amazon ECR expects future layer part uploads to be.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException


    :return: {
        'uploadId': 'string',
        'partSize': 123
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    
    """
    pass

def list_images(registryId=None, repositoryName=None, nextToken=None, maxResults=None, filter=None):
    """
    Lists all the image IDs for the specified repository.
    You can filter images based on whether or not they are tagged by using the tagStatus filter and specifying either TAGGED , UNTAGGED or ANY . For example, you can filter your results to return only UNTAGGED images and then pipe that result to a  BatchDeleteImage operation to delete them. Or, you can filter your results to return only TAGGED images to list all of the tags in your repository.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example lists all of the images in the repository named ubuntu in the default registry in the current account.
    Expected Output:
    
    :example: response = client.list_images(
        registryId='string',
        repositoryName='string',
        nextToken='string',
        maxResults=123,
        filter={
            'tagStatus': 'TAGGED'|'UNTAGGED'|'ANY'
        }
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository in which to list images. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe repository with image IDs to be listed.\n

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListImages request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.\n\nNote\nThis token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.\n\n

    :type maxResults: integer
    :param maxResults: The maximum number of image results returned by ListImages in paginated output. When this parameter is used, ListImages only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListImages request with the returned nextToken value. This value can be between 1 and 1000. If this parameter is not used, then ListImages returns up to 100 results and a nextToken value, if applicable.

    :type filter: dict
    :param filter: The filter key and value with which to filter your ListImages results.\n\ntagStatus (string) --The tag status with which to filter your ListImages results. You can filter results based on whether they are TAGGED or UNTAGGED .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'imageIds': [
        {
            'imageDigest': 'string',
            'imageTag': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

imageIds (list) --
The list of image IDs for the requested repository.

(dict) --
An object with identifying information for an Amazon ECR image.

imageDigest (string) --
The sha256 digest of the image manifest.

imageTag (string) --
The tag used for the image.





nextToken (string) --
The nextToken value to include in a future ListImages request. When the results of a ListImages request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException

Examples
This example lists all of the images in the repository named ubuntu in the default registry in the current account.
response = client.list_images(
    repositoryName='ubuntu',
)

print(response)


Expected Output:
{
    'imageIds': [
        {
            'imageDigest': 'sha256:764f63476bdff6d83a09ba2a818f0d35757063724a9ac3ba5019c56f74ebf42a',
            'imageTag': 'precise',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'imageIds': [
            {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    List the tags for an Amazon ECR resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the only supported resource is an Amazon ECR repository.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
tags (list) --The tags for the resource.

(dict) --The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.

Key (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.

Value (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).










Exceptions

ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.ServerException


    :return: {
        'tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def put_image(registryId=None, repositoryName=None, imageManifest=None, imageManifestMediaType=None, imageTag=None):
    """
    Creates or updates the image manifest and tags associated with an image.
    When an image is pushed and all new image layers have been uploaded, the PutImage API is called once to create or update the image manifest and the tags associated with the image.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_image(
        registryId='string',
        repositoryName='string',
        imageManifest='string',
        imageManifestMediaType='string',
        imageTag='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository in which to put the image. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository in which to put the image.\n

    :type imageManifest: string
    :param imageManifest: [REQUIRED]\nThe image manifest corresponding to the image to be uploaded.\n

    :type imageManifestMediaType: string
    :param imageManifestMediaType: The media type of the image manifest. If you push an image manifest that does not contain the mediaType field, you must specify the imageManifestMediaType in the request.

    :type imageTag: string
    :param imageTag: The tag to associate with the image. This parameter is required for images that use the Docker Image Manifest V2 Schema 2 or OCI formats.

    :rtype: dict

ReturnsResponse Syntax
{
    'image': {
        'registryId': 'string',
        'repositoryName': 'string',
        'imageId': {
            'imageDigest': 'string',
            'imageTag': 'string'
        },
        'imageManifest': 'string',
        'imageManifestMediaType': 'string'
    }
}


Response Structure

(dict) --

image (dict) --
Details of the image uploaded.

registryId (string) --
The AWS account ID associated with the registry containing the image.

repositoryName (string) --
The name of the repository associated with the image.

imageId (dict) --
An object containing the image tag and image digest associated with an image.

imageDigest (string) --
The sha256 digest of the image manifest.

imageTag (string) --
The tag used for the image.



imageManifest (string) --
The image manifest associated with the image.

imageManifestMediaType (string) --
The media type associated with the image manifest.









Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.ImageAlreadyExistsException
ECR.Client.exceptions.LayersNotFoundException
ECR.Client.exceptions.ReferencedImagesNotFoundException
ECR.Client.exceptions.LimitExceededException
ECR.Client.exceptions.ImageTagAlreadyExistsException


    :return: {
        'image': {
            'registryId': 'string',
            'repositoryName': 'string',
            'imageId': {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
            'imageManifest': 'string',
            'imageManifestMediaType': 'string'
        }
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    ECR.Client.exceptions.ImageAlreadyExistsException
    ECR.Client.exceptions.LayersNotFoundException
    ECR.Client.exceptions.ReferencedImagesNotFoundException
    ECR.Client.exceptions.LimitExceededException
    ECR.Client.exceptions.ImageTagAlreadyExistsException
    
    """
    pass

def put_image_scanning_configuration(registryId=None, repositoryName=None, imageScanningConfiguration=None):
    """
    Updates the image scanning configuration for the specified repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_image_scanning_configuration(
        registryId='string',
        repositoryName='string',
        imageScanningConfiguration={
            'scanOnPush': True|False
        }
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository in which to update the image scanning configuration setting. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository in which to update the image scanning configuration setting.\n

    :type imageScanningConfiguration: dict
    :param imageScanningConfiguration: [REQUIRED]\nThe image scanning configuration for the repository. This setting determines whether images are scanned for known vulnerabilities after being pushed to the repository.\n\nscanOnPush (boolean) --The setting that determines whether images are scanned after being pushed to a repository. If set to true , images will be scanned after being pushed. If this parameter is not specified, it will default to false and images will not be scanned unless a scan is manually started with the StartImageScan API.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'registryId': 'string',
    'repositoryName': 'string',
    'imageScanningConfiguration': {
        'scanOnPush': True|False
    }
}


Response Structure

(dict) --

registryId (string) --
The registry ID associated with the request.

repositoryName (string) --
The repository name associated with the request.

imageScanningConfiguration (dict) --
The image scanning configuration setting for the repository.

scanOnPush (boolean) --
The setting that determines whether images are scanned after being pushed to a repository. If set to true , images will be scanned after being pushed. If this parameter is not specified, it will default to false and images will not be scanned unless a scan is manually started with the  StartImageScan API.









Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException


    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'imageScanningConfiguration': {
            'scanOnPush': True|False
        }
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    
    """
    pass

def put_image_tag_mutability(registryId=None, repositoryName=None, imageTagMutability=None):
    """
    Updates the image tag mutability settings for the specified repository. For more information, see Image Tag Mutability in the Amazon Elastic Container Registry User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_image_tag_mutability(
        registryId='string',
        repositoryName='string',
        imageTagMutability='MUTABLE'|'IMMUTABLE'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository in which to update the image tag mutability settings. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository in which to update the image tag mutability settings.\n

    :type imageTagMutability: string
    :param imageTagMutability: [REQUIRED]\nThe tag mutability setting for the repository. If MUTABLE is specified, image tags can be overwritten. If IMMUTABLE is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'registryId': 'string',
    'repositoryName': 'string',
    'imageTagMutability': 'MUTABLE'|'IMMUTABLE'
}


Response Structure

(dict) --

registryId (string) --
The registry ID associated with the request.

repositoryName (string) --
The repository name associated with the request.

imageTagMutability (string) --
The image tag mutability setting for the repository.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException


    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'imageTagMutability': 'MUTABLE'|'IMMUTABLE'
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    
    """
    pass

def put_lifecycle_policy(registryId=None, repositoryName=None, lifecyclePolicyText=None):
    """
    Creates or updates the lifecycle policy for the specified repository. For more information, see Lifecycle Policy Template .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_lifecycle_policy(
        registryId='string',
        repositoryName='string',
        lifecyclePolicyText='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository to receive the policy.\n

    :type lifecyclePolicyText: string
    :param lifecyclePolicyText: [REQUIRED]\nThe JSON repository policy text to apply to the repository.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'registryId': 'string',
    'repositoryName': 'string',
    'lifecyclePolicyText': 'string'
}


Response Structure

(dict) --

registryId (string) --
The registry ID associated with the request.

repositoryName (string) --
The repository name associated with the request.

lifecyclePolicyText (string) --
The JSON repository policy text.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException


    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'lifecyclePolicyText': 'string'
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    
    """
    pass

def set_repository_policy(registryId=None, repositoryName=None, policyText=None, force=None):
    """
    Applies a repository policy to the specified repository to control access permissions. For more information, see Amazon ECR Repository Policies in the Amazon Elastic Container Registry User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_repository_policy(
        registryId='string',
        repositoryName='string',
        policyText='string',
        force=True|False
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository to receive the policy.\n

    :type policyText: string
    :param policyText: [REQUIRED]\nThe JSON repository policy text to apply to the repository. For more information, see Amazon ECR Repository Policies in the Amazon Elastic Container Registry User Guide .\n

    :type force: boolean
    :param force: If the policy you are attempting to set on a repository policy would prevent you from setting another policy in the future, you must force the SetRepositoryPolicy operation. This is intended to prevent accidental repository lock outs.

    :rtype: dict

ReturnsResponse Syntax
{
    'registryId': 'string',
    'repositoryName': 'string',
    'policyText': 'string'
}


Response Structure

(dict) --

registryId (string) --
The registry ID associated with the request.

repositoryName (string) --
The repository name associated with the request.

policyText (string) --
The JSON repository policy text applied to the repository.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException


    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'policyText': 'string'
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    
    """
    pass

def start_image_scan(registryId=None, repositoryName=None, imageId=None):
    """
    Starts an image vulnerability scan. An image scan can only be started once per day on an individual image. This limit includes if an image was scanned on initial push. For more information, see Image Scanning in the Amazon Elastic Container Registry User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_image_scan(
        registryId='string',
        repositoryName='string',
        imageId={
            'imageDigest': 'string',
            'imageTag': 'string'
        }
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository in which to start an image scan request. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository that contains the images to scan.\n

    :type imageId: dict
    :param imageId: [REQUIRED]\nAn object with identifying information for an Amazon ECR image.\n\nimageDigest (string) --The sha256 digest of the image manifest.\n\nimageTag (string) --The tag used for the image.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'registryId': 'string',
    'repositoryName': 'string',
    'imageId': {
        'imageDigest': 'string',
        'imageTag': 'string'
    },
    'imageScanStatus': {
        'status': 'IN_PROGRESS'|'COMPLETE'|'FAILED',
        'description': 'string'
    }
}


Response Structure

(dict) --

registryId (string) --
The registry ID associated with the request.

repositoryName (string) --
The repository name associated with the request.

imageId (dict) --
An object with identifying information for an Amazon ECR image.

imageDigest (string) --
The sha256 digest of the image manifest.

imageTag (string) --
The tag used for the image.



imageScanStatus (dict) --
The current state of the scan.

status (string) --
The current state of an image scan.

description (string) --
The description of the image scan status.









Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.UnsupportedImageTypeException
ECR.Client.exceptions.LimitExceededException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.ImageNotFoundException


    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'imageId': {
            'imageDigest': 'string',
            'imageTag': 'string'
        },
        'imageScanStatus': {
            'status': 'IN_PROGRESS'|'COMPLETE'|'FAILED',
            'description': 'string'
        }
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.UnsupportedImageTypeException
    ECR.Client.exceptions.LimitExceededException
    ECR.Client.exceptions.RepositoryNotFoundException
    ECR.Client.exceptions.ImageNotFoundException
    
    """
    pass

def start_lifecycle_policy_preview(registryId=None, repositoryName=None, lifecyclePolicyText=None):
    """
    Starts a preview of a lifecycle policy for the specified repository. This allows you to see the results before associating the lifecycle policy with the repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_lifecycle_policy_preview(
        registryId='string',
        repositoryName='string',
        lifecyclePolicyText='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository to be evaluated.\n

    :type lifecyclePolicyText: string
    :param lifecyclePolicyText: The policy to be evaluated against. If you do not specify a policy, the current policy for the repository is used.

    :rtype: dict

ReturnsResponse Syntax
{
    'registryId': 'string',
    'repositoryName': 'string',
    'lifecyclePolicyText': 'string',
    'status': 'IN_PROGRESS'|'COMPLETE'|'EXPIRED'|'FAILED'
}


Response Structure

(dict) --

registryId (string) --
The registry ID associated with the request.

repositoryName (string) --
The repository name associated with the request.

lifecyclePolicyText (string) --
The JSON repository policy text.

status (string) --
The status of the lifecycle policy preview request.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.LifecyclePolicyNotFoundException
ECR.Client.exceptions.LifecyclePolicyPreviewInProgressException


    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'lifecyclePolicyText': 'string',
        'status': 'IN_PROGRESS'|'COMPLETE'|'EXPIRED'|'FAILED'
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.RepositoryNotFoundException
    ECR.Client.exceptions.LifecyclePolicyNotFoundException
    ECR.Client.exceptions.LifecyclePolicyPreviewInProgressException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds specified tags to a resource with the specified ARN. Existing tags on a resource are not changed if they are not specified in the request parameters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the the resource to which to add tags. Currently, the only supported resource is an Amazon ECR repository.\n

    :type tags: list
    :param tags: [REQUIRED]\nThe tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\n(dict) --The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\nKey (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.\n\nValue (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.InvalidTagParameterException
ECR.Client.exceptions.TooManyTagsException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.ServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Deletes specified tags from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource from which to remove tags. Currently, the only supported resource is an Amazon ECR repository.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe keys of the tags to be removed.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.InvalidTagParameterException
ECR.Client.exceptions.TooManyTagsException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.ServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def upload_layer_part(registryId=None, repositoryName=None, uploadId=None, partFirstByte=None, partLastByte=None, layerPartBlob=None):
    """
    Uploads an image layer part to Amazon ECR.
    When an image is pushed, each new image layer is uploaded in parts. The maximum size of each image layer part can be 20971520 bytes (or about 20MB). The UploadLayerPart API is called once per each new image layer part.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.upload_layer_part(
        registryId='string',
        repositoryName='string',
        uploadId='string',
        partFirstByte=123,
        partLastByte=123,
        layerPartBlob=b'bytes'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry to which you are uploading layer parts. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository to which you are uploading layer parts.\n

    :type uploadId: string
    :param uploadId: [REQUIRED]\nThe upload ID from a previous InitiateLayerUpload operation to associate with the layer part upload.\n

    :type partFirstByte: integer
    :param partFirstByte: [REQUIRED]\nThe position of the first byte of the layer part witin the overall image layer.\n

    :type partLastByte: integer
    :param partLastByte: [REQUIRED]\nThe position of the last byte of the layer part within the overall image layer.\n

    :type layerPartBlob: bytes
    :param layerPartBlob: [REQUIRED]\nThe base64-encoded layer part payload.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'registryId': 'string',
    'repositoryName': 'string',
    'uploadId': 'string',
    'lastByteReceived': 123
}


Response Structure

(dict) --

registryId (string) --
The registry ID associated with the request.

repositoryName (string) --
The repository name associated with the request.

uploadId (string) --
The upload ID associated with the request.

lastByteReceived (integer) --
The integer value of the last byte received in the request.







Exceptions

ECR.Client.exceptions.ServerException
ECR.Client.exceptions.InvalidParameterException
ECR.Client.exceptions.InvalidLayerPartException
ECR.Client.exceptions.RepositoryNotFoundException
ECR.Client.exceptions.UploadNotFoundException
ECR.Client.exceptions.LimitExceededException


    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'uploadId': 'string',
        'lastByteReceived': 123
    }
    
    
    :returns: 
    ECR.Client.exceptions.ServerException
    ECR.Client.exceptions.InvalidParameterException
    ECR.Client.exceptions.InvalidLayerPartException
    ECR.Client.exceptions.RepositoryNotFoundException
    ECR.Client.exceptions.UploadNotFoundException
    ECR.Client.exceptions.LimitExceededException
    
    """
    pass

