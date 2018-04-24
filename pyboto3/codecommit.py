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

def batch_get_repositories(repositoryNames=None):
    """
    Returns information about one or more repositories.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_get_repositories(
        repositoryNames=[
            'string',
        ]
    )
    
    
    :type repositoryNames: list
    :param repositoryNames: [REQUIRED]
            The names of the repositories to get information about.
            (string) --
            

    :rtype: dict
    :return: {
        'repositories': [
            {
                'accountId': 'string',
                'repositoryId': 'string',
                'repositoryName': 'string',
                'repositoryDescription': 'string',
                'defaultBranch': 'string',
                'lastModifiedDate': datetime(2015, 1, 1),
                'creationDate': datetime(2015, 1, 1),
                'cloneUrlHttp': 'string',
                'cloneUrlSsh': 'string',
                'Arn': 'string'
            },
        ],
        'repositoriesNotFound': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
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

def create_branch(repositoryName=None, branchName=None, commitId=None):
    """
    Creates a new branch in a repository and points the branch to a commit.
    See also: AWS API Documentation
    
    
    :example: response = client.create_branch(
        repositoryName='string',
        branchName='string',
        commitId='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository in which you want to create the new branch.
            

    :type branchName: string
    :param branchName: [REQUIRED]
            The name of the new branch to create.
            

    :type commitId: string
    :param commitId: [REQUIRED]
            The ID of the commit to point the new branch to.
            

    """
    pass

def create_pull_request(title=None, description=None, targets=None, clientRequestToken=None):
    """
    Creates a pull request in the specified repository.
    See also: AWS API Documentation
    
    
    :example: response = client.create_pull_request(
        title='string',
        description='string',
        targets=[
            {
                'repositoryName': 'string',
                'sourceReference': 'string',
                'destinationReference': 'string'
            },
        ],
        clientRequestToken='string'
    )
    
    
    :type title: string
    :param title: [REQUIRED]
            The title of the pull request. This title will be used to identify the pull request to other users in the repository.
            

    :type description: string
    :param description: A description of the pull request.

    :type targets: list
    :param targets: [REQUIRED]
            The targets for the pull request, including the source of the code to be reviewed (the source branch), and the destination where the creator of the pull request intends the code to be merged after the pull request is closed (the destination branch).
            (dict) --Returns information about a target for a pull request.
            repositoryName (string) -- [REQUIRED]The name of the repository that contains the pull request.
            sourceReference (string) -- [REQUIRED]The branch of the repository that contains the changes for the pull request. Also known as the source branch.
            destinationReference (string) --The branch of the repository where the pull request changes will be merged into. Also known as the destination branch.
            
            

    :type clientRequestToken: string
    :param clientRequestToken: A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
            Note
            The AWS SDKs prepopulate client request tokens. If using an AWS SDK, you do not have to generate an idempotency token, as this will be done for you.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'pullRequest': {
            'pullRequestId': 'string',
            'title': 'string',
            'description': 'string',
            'lastActivityDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'pullRequestStatus': 'OPEN'|'CLOSED',
            'authorArn': 'string',
            'pullRequestTargets': [
                {
                    'repositoryName': 'string',
                    'sourceReference': 'string',
                    'destinationReference': 'string',
                    'destinationCommit': 'string',
                    'sourceCommit': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string'
                    }
                },
            ],
            'clientRequestToken': 'string'
        }
    }
    
    
    """
    pass

def create_repository(repositoryName=None, repositoryDescription=None):
    """
    Creates a new, empty repository.
    See also: AWS API Documentation
    
    
    :example: response = client.create_repository(
        repositoryName='string',
        repositoryDescription='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the new repository to be created.
            Note
            The repository name must be unique across the calling AWS account. In addition, repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. For a full description of the limits on repository names, see Limits in the AWS CodeCommit User Guide. The suffix '.git' is prohibited.
            

    :type repositoryDescription: string
    :param repositoryDescription: A comment or description about the new repository.
            Note
            The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a web page could expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a web page.
            

    :rtype: dict
    :return: {
        'repositoryMetadata': {
            'accountId': 'string',
            'repositoryId': 'string',
            'repositoryName': 'string',
            'repositoryDescription': 'string',
            'defaultBranch': 'string',
            'lastModifiedDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'cloneUrlHttp': 'string',
            'cloneUrlSsh': 'string',
            'Arn': 'string'
        }
    }
    
    
    """
    pass

def delete_branch(repositoryName=None, branchName=None):
    """
    Deletes a branch from a repository, unless that branch is the default branch for the repository.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_branch(
        repositoryName='string',
        branchName='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository that contains the branch to be deleted.
            

    :type branchName: string
    :param branchName: [REQUIRED]
            The name of the branch to delete.
            

    :rtype: dict
    :return: {
        'deletedBranch': {
            'branchName': 'string',
            'commitId': 'string'
        }
    }
    
    
    """
    pass

def delete_comment_content(commentId=None):
    """
    Deletes the content of a comment made on a change, file, or commit in a repository.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_comment_content(
        commentId='string'
    )
    
    
    :type commentId: string
    :param commentId: [REQUIRED]
            The unique, system-generated ID of the comment. To get this ID, use GetCommentsForComparedCommit or GetCommentsForPullRequest .
            

    :rtype: dict
    :return: {
        'comment': {
            'commentId': 'string',
            'content': 'string',
            'inReplyTo': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'authorArn': 'string',
            'deleted': True|False,
            'clientRequestToken': 'string'
        }
    }
    
    
    """
    pass

def delete_repository(repositoryName=None):
    """
    Deletes a repository. If a specified repository was already deleted, a null repository ID will be returned.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_repository(
        repositoryName='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository to delete.
            

    :rtype: dict
    :return: {
        'repositoryId': 'string'
    }
    
    
    """
    pass

def describe_pull_request_events(pullRequestId=None, pullRequestEventType=None, actorArn=None, nextToken=None, maxResults=None):
    """
    Returns information about one or more pull request events.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_pull_request_events(
        pullRequestId='string',
        pullRequestEventType='PULL_REQUEST_CREATED'|'PULL_REQUEST_STATUS_CHANGED'|'PULL_REQUEST_SOURCE_REFERENCE_UPDATED'|'PULL_REQUEST_MERGE_STATE_CHANGED',
        actorArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]
            The system-generated ID of the pull request. To get this ID, use ListPullRequests .
            

    :type pullRequestEventType: string
    :param pullRequestEventType: Optional. The pull request event type about which you want to return information.

    :type actorArn: string
    :param actorArn: The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples include updating the pull request with additional commits or changing the status of a pull request.

    :type nextToken: string
    :param nextToken: An enumeration token that when provided in a request, returns the next batch of the results.

    :type maxResults: integer
    :param maxResults: A non-negative integer used to limit the number of returned results. The default is 100 events, which is also the maximum number of events that can be returned in a result.

    :rtype: dict
    :return: {
        'pullRequestEvents': [
            {
                'pullRequestId': 'string',
                'eventDate': datetime(2015, 1, 1),
                'pullRequestEventType': 'PULL_REQUEST_CREATED'|'PULL_REQUEST_STATUS_CHANGED'|'PULL_REQUEST_SOURCE_REFERENCE_UPDATED'|'PULL_REQUEST_MERGE_STATE_CHANGED',
                'actorArn': 'string',
                'pullRequestStatusChangedEventMetadata': {
                    'pullRequestStatus': 'OPEN'|'CLOSED'
                },
                'pullRequestSourceReferenceUpdatedEventMetadata': {
                    'repositoryName': 'string',
                    'beforeCommitId': 'string',
                    'afterCommitId': 'string'
                },
                'pullRequestMergedStateChangedEventMetadata': {
                    'repositoryName': 'string',
                    'destinationReference': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string'
                    }
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
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

def get_blob(repositoryName=None, blobId=None):
    """
    Returns the base-64 encoded content of an individual blob within a repository.
    See also: AWS API Documentation
    
    
    :example: response = client.get_blob(
        repositoryName='string',
        blobId='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository that contains the blob.
            

    :type blobId: string
    :param blobId: [REQUIRED]
            The ID of the blob, which is its SHA-1 pointer.
            

    :rtype: dict
    :return: {
        'content': b'bytes'
    }
    
    
    """
    pass

def get_branch(repositoryName=None, branchName=None):
    """
    Returns information about a repository branch, including its name and the last commit ID.
    See also: AWS API Documentation
    
    
    :example: response = client.get_branch(
        repositoryName='string',
        branchName='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: The name of the repository that contains the branch for which you want to retrieve information.

    :type branchName: string
    :param branchName: The name of the branch for which you want to retrieve information.

    :rtype: dict
    :return: {
        'branch': {
            'branchName': 'string',
            'commitId': 'string'
        }
    }
    
    
    """
    pass

def get_comment(commentId=None):
    """
    Returns the content of a comment made on a change, file, or commit in a repository.
    See also: AWS API Documentation
    
    
    :example: response = client.get_comment(
        commentId='string'
    )
    
    
    :type commentId: string
    :param commentId: [REQUIRED]
            The unique, system-generated ID of the comment. To get this ID, use GetCommentsForComparedCommit or GetCommentsForPullRequest .
            

    :rtype: dict
    :return: {
        'comment': {
            'commentId': 'string',
            'content': 'string',
            'inReplyTo': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'authorArn': 'string',
            'deleted': True|False,
            'clientRequestToken': 'string'
        }
    }
    
    
    """
    pass

def get_comments_for_compared_commit(repositoryName=None, beforeCommitId=None, afterCommitId=None, nextToken=None, maxResults=None):
    """
    Returns information about comments made on the comparison between two commits.
    See also: AWS API Documentation
    
    
    :example: response = client.get_comments_for_compared_commit(
        repositoryName='string',
        beforeCommitId='string',
        afterCommitId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository where you want to compare commits.
            

    :type beforeCommitId: string
    :param beforeCommitId: To establish the directionality of the comparison, the full commit ID of the 'before' commit.

    :type afterCommitId: string
    :param afterCommitId: [REQUIRED]
            To establish the directionality of the comparison, the full commit ID of the 'after' commit.
            

    :type nextToken: string
    :param nextToken: An enumeration token that when provided in a request, returns the next batch of the results.

    :type maxResults: integer
    :param maxResults: A non-negative integer used to limit the number of returned results. The default is 100 comments, and is configurable up to 500.

    :rtype: dict
    :return: {
        'commentsForComparedCommitData': [
            {
                'repositoryName': 'string',
                'beforeCommitId': 'string',
                'afterCommitId': 'string',
                'beforeBlobId': 'string',
                'afterBlobId': 'string',
                'location': {
                    'filePath': 'string',
                    'filePosition': 123,
                    'relativeFileVersion': 'BEFORE'|'AFTER'
                },
                'comments': [
                    {
                        'commentId': 'string',
                        'content': 'string',
                        'inReplyTo': 'string',
                        'creationDate': datetime(2015, 1, 1),
                        'lastModifiedDate': datetime(2015, 1, 1),
                        'authorArn': 'string',
                        'deleted': True|False,
                        'clientRequestToken': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def get_comments_for_pull_request(pullRequestId=None, repositoryName=None, beforeCommitId=None, afterCommitId=None, nextToken=None, maxResults=None):
    """
    Returns comments made on a pull request.
    See also: AWS API Documentation
    
    
    :example: response = client.get_comments_for_pull_request(
        pullRequestId='string',
        repositoryName='string',
        beforeCommitId='string',
        afterCommitId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]
            The system-generated ID of the pull request. To get this ID, use ListPullRequests .
            

    :type repositoryName: string
    :param repositoryName: The name of the repository that contains the pull request.

    :type beforeCommitId: string
    :param beforeCommitId: The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was created.

    :type afterCommitId: string
    :param afterCommitId: The full commit ID of the commit in the source branch that was the tip of the branch at the time the comment was made.

    :type nextToken: string
    :param nextToken: An enumeration token that when provided in a request, returns the next batch of the results.

    :type maxResults: integer
    :param maxResults: A non-negative integer used to limit the number of returned results. The default is 100 comments. You can return up to 500 comments with a single request.

    :rtype: dict
    :return: {
        'commentsForPullRequestData': [
            {
                'pullRequestId': 'string',
                'repositoryName': 'string',
                'beforeCommitId': 'string',
                'afterCommitId': 'string',
                'beforeBlobId': 'string',
                'afterBlobId': 'string',
                'location': {
                    'filePath': 'string',
                    'filePosition': 123,
                    'relativeFileVersion': 'BEFORE'|'AFTER'
                },
                'comments': [
                    {
                        'commentId': 'string',
                        'content': 'string',
                        'inReplyTo': 'string',
                        'creationDate': datetime(2015, 1, 1),
                        'lastModifiedDate': datetime(2015, 1, 1),
                        'authorArn': 'string',
                        'deleted': True|False,
                        'clientRequestToken': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def get_commit(repositoryName=None, commitId=None):
    """
    Returns information about a commit, including commit message and committer information.
    See also: AWS API Documentation
    
    
    :example: response = client.get_commit(
        repositoryName='string',
        commitId='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository to which the commit was made.
            

    :type commitId: string
    :param commitId: [REQUIRED]
            The commit ID. Commit IDs are the full SHA of the commit.
            

    :rtype: dict
    :return: {
        'commit': {
            'commitId': 'string',
            'treeId': 'string',
            'parents': [
                'string',
            ],
            'message': 'string',
            'author': {
                'name': 'string',
                'email': 'string',
                'date': 'string'
            },
            'committer': {
                'name': 'string',
                'email': 'string',
                'date': 'string'
            },
            'additionalData': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_differences(repositoryName=None, beforeCommitSpecifier=None, afterCommitSpecifier=None, beforePath=None, afterPath=None, MaxResults=None, NextToken=None):
    """
    Returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID or other fully qualified reference). Results can be limited to a specified path.
    See also: AWS API Documentation
    
    
    :example: response = client.get_differences(
        repositoryName='string',
        beforeCommitSpecifier='string',
        afterCommitSpecifier='string',
        beforePath='string',
        afterPath='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository where you want to get differences.
            

    :type beforeCommitSpecifier: string
    :param beforeCommitSpecifier: The branch, tag, HEAD, or other fully qualified reference used to identify a commit. For example, the full commit ID. Optional. If not specified, all changes prior to the afterCommitSpecifier value will be shown. If you do not use beforeCommitSpecifier in your request, consider limiting the results with maxResults .

    :type afterCommitSpecifier: string
    :param afterCommitSpecifier: [REQUIRED]
            The branch, tag, HEAD, or other fully qualified reference used to identify a commit.
            

    :type beforePath: string
    :param beforePath: The file path in which to check for differences. Limits the results to this path. Can also be used to specify the previous name of a directory or folder. If beforePath and afterPath are not specified, differences will be shown for all paths.

    :type afterPath: string
    :param afterPath: The file path in which to check differences. Limits the results to this path. Can also be used to specify the changed name of a directory or folder, if it has changed. If not specified, differences will be shown for all paths.

    :type MaxResults: integer
    :param MaxResults: A non-negative integer used to limit the number of returned results.

    :type NextToken: string
    :param NextToken: An enumeration token that when provided in a request, returns the next batch of the results.

    :rtype: dict
    :return: {
        'differences': [
            {
                'beforeBlob': {
                    'blobId': 'string',
                    'path': 'string',
                    'mode': 'string'
                },
                'afterBlob': {
                    'blobId': 'string',
                    'path': 'string',
                    'mode': 'string'
                },
                'changeType': 'A'|'M'|'D'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    100644 indicates read/write
    100755 indicates read/write/execute
    160000 indicates a submodule
    120000 indicates a symlink
    
    """
    pass

def get_merge_conflicts(repositoryName=None, destinationCommitSpecifier=None, sourceCommitSpecifier=None, mergeOption=None):
    """
    Returns information about merge conflicts between the before and after commit IDs for a pull request in a repository.
    See also: AWS API Documentation
    
    
    :example: response = client.get_merge_conflicts(
        repositoryName='string',
        destinationCommitSpecifier='string',
        sourceCommitSpecifier='string',
        mergeOption='FAST_FORWARD_MERGE'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository where the pull request was created.
            

    :type destinationCommitSpecifier: string
    :param destinationCommitSpecifier: [REQUIRED]
            The branch, tag, HEAD, or other fully qualified reference used to identify a commit. For example, a branch name or a full commit ID.
            

    :type sourceCommitSpecifier: string
    :param sourceCommitSpecifier: [REQUIRED]
            The branch, tag, HEAD, or other fully qualified reference used to identify a commit. For example, a branch name or a full commit ID.
            

    :type mergeOption: string
    :param mergeOption: [REQUIRED]
            The merge option or strategy you want to use to merge the code. The only valid value is FAST_FORWARD_MERGE.
            

    :rtype: dict
    :return: {
        'mergeable': True|False,
        'destinationCommitId': 'string',
        'sourceCommitId': 'string'
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

def get_pull_request(pullRequestId=None):
    """
    Gets information about a pull request in a specified repository.
    See also: AWS API Documentation
    
    
    :example: response = client.get_pull_request(
        pullRequestId='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]
            The system-generated ID of the pull request. To get this ID, use ListPullRequests .
            

    :rtype: dict
    :return: {
        'pullRequest': {
            'pullRequestId': 'string',
            'title': 'string',
            'description': 'string',
            'lastActivityDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'pullRequestStatus': 'OPEN'|'CLOSED',
            'authorArn': 'string',
            'pullRequestTargets': [
                {
                    'repositoryName': 'string',
                    'sourceReference': 'string',
                    'destinationReference': 'string',
                    'destinationCommit': 'string',
                    'sourceCommit': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string'
                    }
                },
            ],
            'clientRequestToken': 'string'
        }
    }
    
    
    """
    pass

def get_repository(repositoryName=None):
    """
    Returns information about a repository.
    See also: AWS API Documentation
    
    
    :example: response = client.get_repository(
        repositoryName='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository to get information about.
            

    :rtype: dict
    :return: {
        'repositoryMetadata': {
            'accountId': 'string',
            'repositoryId': 'string',
            'repositoryName': 'string',
            'repositoryDescription': 'string',
            'defaultBranch': 'string',
            'lastModifiedDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'cloneUrlHttp': 'string',
            'cloneUrlSsh': 'string',
            'Arn': 'string'
        }
    }
    
    
    """
    pass

def get_repository_triggers(repositoryName=None):
    """
    Gets information about triggers configured for a repository.
    See also: AWS API Documentation
    
    
    :example: response = client.get_repository_triggers(
        repositoryName='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository for which the trigger is configured.
            

    :rtype: dict
    :return: {
        'configurationId': 'string',
        'triggers': [
            {
                'name': 'string',
                'destinationArn': 'string',
                'customData': 'string',
                'branches': [
                    'string',
                ],
                'events': [
                    'all'|'updateReference'|'createReference'|'deleteReference',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_branches(repositoryName=None, nextToken=None):
    """
    Gets information about one or more branches in a repository.
    See also: AWS API Documentation
    
    
    :example: response = client.list_branches(
        repositoryName='string',
        nextToken='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository that contains the branches.
            

    :type nextToken: string
    :param nextToken: An enumeration token that allows the operation to batch the results.

    :rtype: dict
    :return: {
        'branches': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_pull_requests(repositoryName=None, authorArn=None, pullRequestStatus=None, nextToken=None, maxResults=None):
    """
    Returns a list of pull requests for a specified repository. The return list can be refined by pull request status or pull request author ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.list_pull_requests(
        repositoryName='string',
        authorArn='string',
        pullRequestStatus='OPEN'|'CLOSED',
        nextToken='string',
        maxResults=123
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository for which you want to list pull requests.
            

    :type authorArn: string
    :param authorArn: Optional. The Amazon Resource Name (ARN) of the user who created the pull request. If used, this filters the results to pull requests created by that user.

    :type pullRequestStatus: string
    :param pullRequestStatus: Optional. The status of the pull request. If used, this refines the results to the pull requests that match the specified status.

    :type nextToken: string
    :param nextToken: An enumeration token that when provided in a request, returns the next batch of the results.

    :type maxResults: integer
    :param maxResults: A non-negative integer used to limit the number of returned results.

    :rtype: dict
    :return: {
        'pullRequestIds': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_repositories(nextToken=None, sortBy=None, order=None):
    """
    Gets information about one or more repositories.
    See also: AWS API Documentation
    
    
    :example: response = client.list_repositories(
        nextToken='string',
        sortBy='repositoryName'|'lastModifiedDate',
        order='ascending'|'descending'
    )
    
    
    :type nextToken: string
    :param nextToken: An enumeration token that allows the operation to batch the results of the operation. Batch sizes are 1,000 for list repository operations. When the client sends the token back to AWS CodeCommit, another page of 1,000 records is retrieved.

    :type sortBy: string
    :param sortBy: The criteria used to sort the results of a list repositories operation.

    :type order: string
    :param order: The order in which to sort the results of a list repositories operation.

    :rtype: dict
    :return: {
        'repositories': [
            {
                'repositoryName': 'string',
                'repositoryId': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def merge_pull_request_by_fast_forward(pullRequestId=None, repositoryName=None, sourceCommitId=None):
    """
    Closes a pull request and attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the fast-forward merge option.
    See also: AWS API Documentation
    
    
    :example: response = client.merge_pull_request_by_fast_forward(
        pullRequestId='string',
        repositoryName='string',
        sourceCommitId='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]
            The system-generated ID of the pull request. To get this ID, use ListPullRequests .
            

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository where the pull request was created.
            

    :type sourceCommitId: string
    :param sourceCommitId: The full commit ID of the original or updated commit in the pull request source branch. Pass this value if you want an exception thrown if the current commit ID of the tip of the source branch does not match this commit ID.

    :rtype: dict
    :return: {
        'pullRequest': {
            'pullRequestId': 'string',
            'title': 'string',
            'description': 'string',
            'lastActivityDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'pullRequestStatus': 'OPEN'|'CLOSED',
            'authorArn': 'string',
            'pullRequestTargets': [
                {
                    'repositoryName': 'string',
                    'sourceReference': 'string',
                    'destinationReference': 'string',
                    'destinationCommit': 'string',
                    'sourceCommit': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string'
                    }
                },
            ],
            'clientRequestToken': 'string'
        }
    }
    
    
    """
    pass

def post_comment_for_compared_commit(repositoryName=None, beforeCommitId=None, afterCommitId=None, location=None, content=None, clientRequestToken=None):
    """
    Posts a comment on the comparison between two commits.
    See also: AWS API Documentation
    
    
    :example: response = client.post_comment_for_compared_commit(
        repositoryName='string',
        beforeCommitId='string',
        afterCommitId='string',
        location={
            'filePath': 'string',
            'filePosition': 123,
            'relativeFileVersion': 'BEFORE'|'AFTER'
        },
        content='string',
        clientRequestToken='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository where you want to post a comment on the comparison between commits.
            

    :type beforeCommitId: string
    :param beforeCommitId: To establish the directionality of the comparison, the full commit ID of the 'before' commit.

    :type afterCommitId: string
    :param afterCommitId: [REQUIRED]
            To establish the directionality of the comparison, the full commit ID of the 'after' commit.
            

    :type location: dict
    :param location: The location of the comparison where you want to comment.
            filePath (string) --The name of the file being compared, including its extension and subdirectory, if any.
            filePosition (integer) --The position of a change within a compared file, in line number format.
            relativeFileVersion (string) --In a comparison of commits or a pull request, whether the change is in the 'before' or 'after' of that comparison.
            

    :type content: string
    :param content: [REQUIRED]
            The content of the comment you want to make.
            

    :type clientRequestToken: string
    :param clientRequestToken: A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'repositoryName': 'string',
        'beforeCommitId': 'string',
        'afterCommitId': 'string',
        'beforeBlobId': 'string',
        'afterBlobId': 'string',
        'location': {
            'filePath': 'string',
            'filePosition': 123,
            'relativeFileVersion': 'BEFORE'|'AFTER'
        },
        'comment': {
            'commentId': 'string',
            'content': 'string',
            'inReplyTo': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'authorArn': 'string',
            'deleted': True|False,
            'clientRequestToken': 'string'
        }
    }
    
    
    """
    pass

def post_comment_for_pull_request(pullRequestId=None, repositoryName=None, beforeCommitId=None, afterCommitId=None, location=None, content=None, clientRequestToken=None):
    """
    Posts a comment on a pull request.
    See also: AWS API Documentation
    
    
    :example: response = client.post_comment_for_pull_request(
        pullRequestId='string',
        repositoryName='string',
        beforeCommitId='string',
        afterCommitId='string',
        location={
            'filePath': 'string',
            'filePosition': 123,
            'relativeFileVersion': 'BEFORE'|'AFTER'
        },
        content='string',
        clientRequestToken='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]
            The system-generated ID of the pull request. To get this ID, use ListPullRequests .
            

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository where you want to post a comment on a pull request.
            

    :type beforeCommitId: string
    :param beforeCommitId: [REQUIRED]
            The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was created.
            

    :type afterCommitId: string
    :param afterCommitId: [REQUIRED]
            The full commit ID of the commit in the source branch that is the current tip of the branch for the pull request when you post the comment.
            

    :type location: dict
    :param location: The location of the change where you want to post your comment. If no location is provided, the comment will be posted as a general comment on the pull request difference between the before commit ID and the after commit ID.
            filePath (string) --The name of the file being compared, including its extension and subdirectory, if any.
            filePosition (integer) --The position of a change within a compared file, in line number format.
            relativeFileVersion (string) --In a comparison of commits or a pull request, whether the change is in the 'before' or 'after' of that comparison.
            

    :type content: string
    :param content: [REQUIRED]
            The content of your comment on the change.
            

    :type clientRequestToken: string
    :param clientRequestToken: A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'repositoryName': 'string',
        'pullRequestId': 'string',
        'beforeCommitId': 'string',
        'afterCommitId': 'string',
        'beforeBlobId': 'string',
        'afterBlobId': 'string',
        'location': {
            'filePath': 'string',
            'filePosition': 123,
            'relativeFileVersion': 'BEFORE'|'AFTER'
        },
        'comment': {
            'commentId': 'string',
            'content': 'string',
            'inReplyTo': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'authorArn': 'string',
            'deleted': True|False,
            'clientRequestToken': 'string'
        }
    }
    
    
    """
    pass

def post_comment_reply(inReplyTo=None, clientRequestToken=None, content=None):
    """
    Posts a comment in reply to an existing comment on a comparison between commits or a pull request.
    See also: AWS API Documentation
    
    
    :example: response = client.post_comment_reply(
        inReplyTo='string',
        clientRequestToken='string',
        content='string'
    )
    
    
    :type inReplyTo: string
    :param inReplyTo: [REQUIRED]
            The system-generated ID of the comment to which you want to reply. To get this ID, use GetCommentsForComparedCommit or GetCommentsForPullRequest .
            

    :type clientRequestToken: string
    :param clientRequestToken: A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
            This field is autopopulated if not provided.
            

    :type content: string
    :param content: [REQUIRED]
            The contents of your reply to a comment.
            

    :rtype: dict
    :return: {
        'comment': {
            'commentId': 'string',
            'content': 'string',
            'inReplyTo': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'authorArn': 'string',
            'deleted': True|False,
            'clientRequestToken': 'string'
        }
    }
    
    
    """
    pass

def put_file(repositoryName=None, branchName=None, fileContent=None, filePath=None, fileMode=None, parentCommitId=None, commitMessage=None, name=None, email=None):
    """
    Adds or updates a file in an AWS CodeCommit repository.
    See also: AWS API Documentation
    
    
    :example: response = client.put_file(
        repositoryName='string',
        branchName='string',
        fileContent=b'bytes',
        filePath='string',
        fileMode='EXECUTABLE'|'NORMAL'|'SYMLINK',
        parentCommitId='string',
        commitMessage='string',
        name='string',
        email='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository where you want to add or update the file.
            

    :type branchName: string
    :param branchName: [REQUIRED]
            The name of the branch where you want to add or update the file.
            

    :type fileContent: bytes
    :param fileContent: [REQUIRED]
            The content of the file, in binary object format.
            

    :type filePath: string
    :param filePath: [REQUIRED]
            The name of the file you want to add or update, including the relative path to the file in the repository.
            Note
            If the path does not currently exist in the repository, the path will be created as part of adding the file.
            

    :type fileMode: string
    :param fileMode: The file mode permissions of the blob. Valid file mode permissions are listed below.

    :type parentCommitId: string
    :param parentCommitId: The full commit ID of the head commit in the branch where you want to add or update the file. If the commit ID does not match the ID of the head commit at the time of the operation, an error will occur, and the file will not be added or updated.

    :type commitMessage: string
    :param commitMessage: A message about why this file was added or updated. While optional, adding a message is strongly encouraged in order to provide a more useful commit history for your repository.

    :type name: string
    :param name: The name of the person adding or updating the file. While optional, adding a name is strongly encouraged in order to provide a more useful commit history for your repository.

    :type email: string
    :param email: An email address for the person adding or updating the file.

    :rtype: dict
    :return: {
        'commitId': 'string',
        'blobId': 'string',
        'treeId': 'string'
    }
    
    
    """
    pass

def put_repository_triggers(repositoryName=None, triggers=None):
    """
    Replaces all triggers for a repository. This can be used to create or delete triggers.
    See also: AWS API Documentation
    
    
    :example: response = client.put_repository_triggers(
        repositoryName='string',
        triggers=[
            {
                'name': 'string',
                'destinationArn': 'string',
                'customData': 'string',
                'branches': [
                    'string',
                ],
                'events': [
                    'all'|'updateReference'|'createReference'|'deleteReference',
                ]
            },
        ]
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository where you want to create or update the trigger.
            

    :type triggers: list
    :param triggers: [REQUIRED]
            The JSON block of configuration information for each trigger.
            (dict) --Information about a trigger for a repository.
            name (string) -- [REQUIRED]The name of the trigger.
            destinationArn (string) -- [REQUIRED]The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).
            customData (string) --Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.
            branches (list) --The branches that will be included in the trigger configuration. If you specify an empty array, the trigger will apply to all branches.
            Note
            While no content is required in the array, you must include the array itself.
            (string) --
            events (list) -- [REQUIRED]The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS).
            Note
            The valid value 'all' cannot be used with any other values.
            (string) --
            
            

    :rtype: dict
    :return: {
        'configurationId': 'string'
    }
    
    
    """
    pass

def test_repository_triggers(repositoryName=None, triggers=None):
    """
    Tests the functionality of repository triggers by sending information to the trigger target. If real data is available in the repository, the test will send data from the last commit. If no data is available, sample data will be generated.
    See also: AWS API Documentation
    
    
    :example: response = client.test_repository_triggers(
        repositoryName='string',
        triggers=[
            {
                'name': 'string',
                'destinationArn': 'string',
                'customData': 'string',
                'branches': [
                    'string',
                ],
                'events': [
                    'all'|'updateReference'|'createReference'|'deleteReference',
                ]
            },
        ]
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository in which to test the triggers.
            

    :type triggers: list
    :param triggers: [REQUIRED]
            The list of triggers to test.
            (dict) --Information about a trigger for a repository.
            name (string) -- [REQUIRED]The name of the trigger.
            destinationArn (string) -- [REQUIRED]The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).
            customData (string) --Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.
            branches (list) --The branches that will be included in the trigger configuration. If you specify an empty array, the trigger will apply to all branches.
            Note
            While no content is required in the array, you must include the array itself.
            (string) --
            events (list) -- [REQUIRED]The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS).
            Note
            The valid value 'all' cannot be used with any other values.
            (string) --
            
            

    :rtype: dict
    :return: {
        'successfulExecutions': [
            'string',
        ],
        'failedExecutions': [
            {
                'trigger': 'string',
                'failureMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_comment(commentId=None, content=None):
    """
    Replaces the contents of a comment.
    See also: AWS API Documentation
    
    
    :example: response = client.update_comment(
        commentId='string',
        content='string'
    )
    
    
    :type commentId: string
    :param commentId: [REQUIRED]
            The system-generated ID of the comment you want to update. To get this ID, use GetCommentsForComparedCommit or GetCommentsForPullRequest .
            

    :type content: string
    :param content: [REQUIRED]
            The updated content with which you want to replace the existing content of the comment.
            

    :rtype: dict
    :return: {
        'comment': {
            'commentId': 'string',
            'content': 'string',
            'inReplyTo': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'authorArn': 'string',
            'deleted': True|False,
            'clientRequestToken': 'string'
        }
    }
    
    
    """
    pass

def update_default_branch(repositoryName=None, defaultBranchName=None):
    """
    Sets or changes the default branch name for the specified repository.
    See also: AWS API Documentation
    
    
    :example: response = client.update_default_branch(
        repositoryName='string',
        defaultBranchName='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository to set or change the default branch for.
            

    :type defaultBranchName: string
    :param defaultBranchName: [REQUIRED]
            The name of the branch to set as the default.
            

    """
    pass

def update_pull_request_description(pullRequestId=None, description=None):
    """
    Replaces the contents of the description of a pull request.
    See also: AWS API Documentation
    
    
    :example: response = client.update_pull_request_description(
        pullRequestId='string',
        description='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]
            The system-generated ID of the pull request. To get this ID, use ListPullRequests .
            

    :type description: string
    :param description: [REQUIRED]
            The updated content of the description for the pull request. This content will replace the existing description.
            

    :rtype: dict
    :return: {
        'pullRequest': {
            'pullRequestId': 'string',
            'title': 'string',
            'description': 'string',
            'lastActivityDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'pullRequestStatus': 'OPEN'|'CLOSED',
            'authorArn': 'string',
            'pullRequestTargets': [
                {
                    'repositoryName': 'string',
                    'sourceReference': 'string',
                    'destinationReference': 'string',
                    'destinationCommit': 'string',
                    'sourceCommit': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string'
                    }
                },
            ],
            'clientRequestToken': 'string'
        }
    }
    
    
    """
    pass

def update_pull_request_status(pullRequestId=None, pullRequestStatus=None):
    """
    Updates the status of a pull request.
    See also: AWS API Documentation
    
    
    :example: response = client.update_pull_request_status(
        pullRequestId='string',
        pullRequestStatus='OPEN'|'CLOSED'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]
            The system-generated ID of the pull request. To get this ID, use ListPullRequests .
            

    :type pullRequestStatus: string
    :param pullRequestStatus: [REQUIRED]
            The status of the pull request. The only valid operations are to update the status from OPEN to OPEN , OPEN to CLOSED or from from CLOSED to CLOSED .
            

    :rtype: dict
    :return: {
        'pullRequest': {
            'pullRequestId': 'string',
            'title': 'string',
            'description': 'string',
            'lastActivityDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'pullRequestStatus': 'OPEN'|'CLOSED',
            'authorArn': 'string',
            'pullRequestTargets': [
                {
                    'repositoryName': 'string',
                    'sourceReference': 'string',
                    'destinationReference': 'string',
                    'destinationCommit': 'string',
                    'sourceCommit': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string'
                    }
                },
            ],
            'clientRequestToken': 'string'
        }
    }
    
    
    """
    pass

def update_pull_request_title(pullRequestId=None, title=None):
    """
    Replaces the title of a pull request.
    See also: AWS API Documentation
    
    
    :example: response = client.update_pull_request_title(
        pullRequestId='string',
        title='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]
            The system-generated ID of the pull request. To get this ID, use ListPullRequests .
            

    :type title: string
    :param title: [REQUIRED]
            The updated title of the pull request. This will replace the existing title.
            

    :rtype: dict
    :return: {
        'pullRequest': {
            'pullRequestId': 'string',
            'title': 'string',
            'description': 'string',
            'lastActivityDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'pullRequestStatus': 'OPEN'|'CLOSED',
            'authorArn': 'string',
            'pullRequestTargets': [
                {
                    'repositoryName': 'string',
                    'sourceReference': 'string',
                    'destinationReference': 'string',
                    'destinationCommit': 'string',
                    'sourceCommit': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string'
                    }
                },
            ],
            'clientRequestToken': 'string'
        }
    }
    
    
    """
    pass

def update_repository_description(repositoryName=None, repositoryDescription=None):
    """
    Sets or changes the comment or description for a repository.
    See also: AWS API Documentation
    
    
    :example: response = client.update_repository_description(
        repositoryName='string',
        repositoryDescription='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository to set or change the comment or description for.
            

    :type repositoryDescription: string
    :param repositoryDescription: The new comment or description for the specified repository. Repository descriptions are limited to 1,000 characters.

    """
    pass

def update_repository_name(oldName=None, newName=None):
    """
    Renames a repository. The repository name must be unique across the calling AWS account. In addition, repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. The suffix ".git" is prohibited. For a full description of the limits on repository names, see Limits in the AWS CodeCommit User Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.update_repository_name(
        oldName='string',
        newName='string'
    )
    
    
    :type oldName: string
    :param oldName: [REQUIRED]
            The existing name of the repository.
            

    :type newName: string
    :param newName: [REQUIRED]
            The new name for the repository.
            

    """
    pass

