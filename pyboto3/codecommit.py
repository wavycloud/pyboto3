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
            The commit ID.
            

    :rtype: dict
    :return: {
        'commit': {
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
            branches (list) --The branches that will be included in the trigger configuration. If no branches are specified, the trigger will apply to all branches.
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
            branches (list) --The branches that will be included in the trigger configuration. If no branches are specified, the trigger will apply to all branches.
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

