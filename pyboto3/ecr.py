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


def batch_check_layer_availability(registryId=None, repositoryName=None, layerDigests=None):
    """
    :param registryId: The AWS account ID associated with the registry that contains the image layers to check. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryName: [REQUIRED]
            The name of the repository that is associated with the image layers to check.
            
    :type repositoryName: string
    :param layerDigests: [REQUIRED]
            The digests of the image layers to check.
            (string) --
            
    :type layerDigests: list
    """
    pass


def batch_delete_image(registryId=None, repositoryName=None, imageIds=None):
    """
    :param registryId: The AWS account ID associated with the registry that contains the image to delete. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryName: [REQUIRED]
            The repository that contains the image to delete.
            
    :type repositoryName: string
    :param imageIds: [REQUIRED]
            A list of image ID references that correspond to images to delete. The format of the imageIds reference is imageTag=tag or imageDigest=digest .
            (dict) --An object with identifying information for an Amazon ECR image.
            imageDigest (string) --The sha256 digest of the image manifest.
            imageTag (string) --The tag used for the image.
            
            
    :type imageIds: list
    """
    pass


def batch_get_image(registryId=None, repositoryName=None, imageIds=None):
    """
    :param registryId: The AWS account ID associated with the registry that contains the images to describe. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryName: [REQUIRED]
            The repository that contains the images to describe.
            
    :type repositoryName: string
    :param imageIds: [REQUIRED]
            A list of image ID references that correspond to images to describe. The format of the imageIds reference is imageTag=tag or imageDigest=digest .
            (dict) --An object with identifying information for an Amazon ECR image.
            imageDigest (string) --The sha256 digest of the image manifest.
            imageTag (string) --The tag used for the image.
            
            
    :type imageIds: list
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


def complete_layer_upload(registryId=None, repositoryName=None, uploadId=None, layerDigests=None):
    """
    :param registryId: The AWS account ID associated with the registry to which to upload layers. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryName: [REQUIRED]
            The name of the repository to associate with the image layer.
            
    :type repositoryName: string
    :param uploadId: [REQUIRED]
            The upload ID from a previous InitiateLayerUpload operation to associate with the image layer.
            
    :type uploadId: string
    :param layerDigests: [REQUIRED]
            The sha256 digest of the image layer.
            (string) --
            
    :type layerDigests: list
    """
    pass


def create_repository(repositoryName=None):
    """
    :param repositoryName: [REQUIRED]
            The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app ) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app ).
            Return typedict
            ReturnsResponse Syntax{
              'repository': {
                'repositoryArn': 'string',
                'registryId': 'string',
                'repositoryName': 'string',
                'repositoryUri': 'string',
                'createdAt': datetime(2015, 1, 1)
              }
            }
            Response Structure
            (dict) --
            repository (dict) --The repository that was created.
            repositoryArn (string) --The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the arn:aws:ecr namespace, followed by the region of the repository, the AWS account ID of the repository owner, the repository namespace, and then the repository name. For example, arn:aws:ecr:region:012345678910:repository/test .
            registryId (string) --The AWS account ID associated with the registry that contains the repository.
            repositoryName (string) --The name of the repository.
            repositoryUri (string) --The URI for the repository. You can use this URI for Docker push and pull operations.
            createdAt (datetime) --The date and time, in JavaScript date/time format, when the repository was created.
            
            
            
    :type repositoryName: string
    """
    pass


def delete_repository(registryId=None, repositoryName=None, force=None):
    """
    :param registryId: The AWS account ID associated with the registry that contains the repository to delete. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryName: [REQUIRED]
            The name of the repository to delete.
            
    :type repositoryName: string
    :param force: Force the deletion of the repository if it contains images.
    :type force: boolean
    """
    pass


def delete_repository_policy(registryId=None, repositoryName=None):
    """
    :param registryId: The AWS account ID associated with the registry that contains the repository policy to delete. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryName: [REQUIRED]
            The name of the repository that is associated with the repository policy to delete.
            
    :type repositoryName: string
    """
    pass


def describe_images(registryId=None, repositoryName=None, imageIds=None, nextToken=None, maxResults=None, filter=None):
    """
    :param registryId: The AWS account ID associated with the registry that contains the repository in which to list images. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryName: [REQUIRED]
            A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described.
            
    :type repositoryName: string
    :param imageIds: The list of image IDs for the requested repository.
            (dict) --An object with identifying information for an Amazon ECR image.
            imageDigest (string) --The sha256 digest of the image manifest.
            imageTag (string) --The tag used for the image.
            
            
    :type imageIds: list
    :param nextToken: The nextToken value returned from a previous paginated DescribeImages request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.
    :type nextToken: string
    :param maxResults: The maximum number of repository results returned by DescribeImages in paginated output. When this parameter is used, DescribeImages only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeImages request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then DescribeImages returns up to 100 results and a nextToken value, if applicable.
    :type maxResults: integer
    :param filter: The filter key and value with which to filter your DescribeImages results.
            tagStatus (string) --The tag status with which to filter your DescribeImages results. You can filter results based on whether they are TAGGED or UNTAGGED .
            
    :type filter: dict
    """
    pass


def describe_repositories(registryId=None, repositoryNames=None, nextToken=None, maxResults=None):
    """
    :param registryId: The AWS account ID associated with the registry that contains the repositories to be described. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryNames: A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described.
            (string) --
            
    :type repositoryNames: list
    :param nextToken: The nextToken value returned from a previous paginated DescribeRepositories request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            
    :type nextToken: string
    :param maxResults: The maximum number of repository results returned by DescribeRepositories in paginated output. When this parameter is used, DescribeRepositories only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeRepositories request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then DescribeRepositories returns up to 100 results and a nextToken value, if applicable.
    :type maxResults: integer
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


def get_authorization_token(registryIds=None):
    """
    :param registryIds: A list of AWS account IDs that are associated with the registries for which to get authorization tokens. If you do not specify a registry, the default registry is assumed.
            (string) --
            Return typedict
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
            
            
            
    :type registryIds: list
    """
    pass


def get_download_url_for_layer(registryId=None, repositoryName=None, layerDigest=None):
    """
    :param registryId: The AWS account ID associated with the registry that contains the image layer to download. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryName: [REQUIRED]
            The name of the repository that is associated with the image layer to download.
            
    :type repositoryName: string
    :param layerDigest: [REQUIRED]
            The digest of the image layer to download.
            
    :type layerDigest: string
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


def get_repository_policy(registryId=None, repositoryName=None):
    """
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryName: [REQUIRED]
            The name of the repository whose policy you want to retrieve.
            
    :type repositoryName: string
    """
    pass


def get_waiter():
    """
    """
    pass


def initiate_layer_upload(registryId=None, repositoryName=None):
    """
    :param registryId: The AWS account ID associated with the registry that you intend to upload layers to. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryName: [REQUIRED]
            The name of the repository that you intend to upload layers to.
            
    :type repositoryName: string
    """
    pass


def list_images(registryId=None, repositoryName=None, nextToken=None, maxResults=None, filter=None):
    """
    :param registryId: The AWS account ID associated with the registry that contains the repository to list images in. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryName: [REQUIRED]
            The repository whose image IDs are to be listed.
            
    :type repositoryName: string
    :param nextToken: The nextToken value returned from a previous paginated ListImages request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            
    :type nextToken: string
    :param maxResults: The maximum number of image results returned by ListImages in paginated output. When this parameter is used, ListImages only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListImages request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListImages returns up to 100 results and a nextToken value, if applicable.
    :type maxResults: integer
    :param filter: The filter key and value with which to filter your ListImages results.
            tagStatus (string) --The tag status with which to filter your ListImages results. You can filter results based on whether they are TAGGED or UNTAGGED .
            
    :type filter: dict
    """
    pass


def put_image(registryId=None, repositoryName=None, imageManifest=None):
    """
    :param registryId: The AWS account ID associated with the registry that contains the repository in which to put the image. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryName: [REQUIRED]
            The name of the repository in which to put the image.
            
    :type repositoryName: string
    :param imageManifest: [REQUIRED]
            The image manifest corresponding to the image to be uploaded.
            
    :type imageManifest: string
    """
    pass


def set_repository_policy(registryId=None, repositoryName=None, policyText=None, force=None):
    """
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryName: [REQUIRED]
            The name of the repository to receive the policy.
            
    :type repositoryName: string
    :param policyText: [REQUIRED]
            The JSON repository policy text to apply to the repository.
            
    :type policyText: string
    :param force: If the policy you are attempting to set on a repository policy would prevent you from setting another policy in the future, you must force the SetRepositoryPolicy operation. This is intended to prevent accidental repository lock outs.
    :type force: boolean
    """
    pass


def upload_layer_part(registryId=None, repositoryName=None, uploadId=None, partFirstByte=None, partLastByte=None,
                      layerPartBlob=None):
    """
    :param registryId: The AWS account ID associated with the registry that you are uploading layer parts to. If you do not specify a registry, the default registry is assumed.
    :type registryId: string
    :param repositoryName: [REQUIRED]
            The name of the repository that you are uploading layer parts to.
            
    :type repositoryName: string
    :param uploadId: [REQUIRED]
            The upload ID from a previous InitiateLayerUpload operation to associate with the layer part upload.
            
    :type uploadId: string
    :param partFirstByte: [REQUIRED]
            The integer value of the first byte of the layer part.
            
    :type partFirstByte: integer
    :param partLastByte: [REQUIRED]
            The integer value of the last byte of the layer part.
            
    :type partLastByte: integer
    :param layerPartBlob: [REQUIRED]
            The base64-encoded layer part payload.
            
    :type layerPartBlob: bytes
    """
    pass
