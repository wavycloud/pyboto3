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


def batch_get_repositories(repositoryNames=None):
    """
    :param repositoryNames: [REQUIRED]
            The names of the repositories to get information about.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the output of a batch get repositories operation.
            repositories (list) --A list of repositories returned by the batch get repositories operation.
            (dict) --Information about a repository.
            accountId (string) --The ID of the AWS account associated with the repository.
            repositoryId (string) --The ID of the repository.
            repositoryName (string) --The repository's name.
            repositoryDescription (string) --A comment or description about the repository.
            defaultBranch (string) --The repository's default branch name.
            lastModifiedDate (datetime) --The date and time the repository was last modified, in timestamp format.
            creationDate (datetime) --The date and time the repository was created, in timestamp format.
            cloneUrlHttp (string) --The URL to use for cloning the repository over HTTPS.
            cloneUrlSsh (string) --The URL to use for cloning the repository over SSH.
            Arn (string) --The Amazon Resource Name (ARN) of the repository.
            
            repositoriesNotFound (list) --Returns a list of repository names for which information could not be found.
            (string) --
            
            
    :type repositoryNames: list
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


def create_branch(repositoryName=None, branchName=None, commitId=None):
    """
    :param repositoryName: [REQUIRED]
            The name of the repository in which you want to create the new branch.
            
    :type repositoryName: string
    :param branchName: [REQUIRED]
            The name of the new branch to create.
            
    :type branchName: string
    :param commitId: [REQUIRED]
            The ID of the commit to point the new branch to.
            
    :type commitId: string
    """
    pass


def create_repository(repositoryName=None, repositoryDescription=None):
    """
    :param repositoryName: [REQUIRED]
            The name of the new repository to be created.
            Note
            The repository name must be unique across the calling AWS account. In addition, repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. For a full description of the limits on repository names, see Limits in the AWS CodeCommit User Guide. The suffix '.git' is prohibited.
            
    :type repositoryName: string
    :param repositoryDescription: A comment or description about the new repository.
            Note
            The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a web page could expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a web page.
            
    :type repositoryDescription: string
    """
    pass


def delete_repository(repositoryName=None):
    """
    :param repositoryName: [REQUIRED]
            The name of the repository to delete.
            Return typedict
            ReturnsResponse Syntax{
              'repositoryId': 'string'
            }
            Response Structure
            (dict) --Represents the output of a delete repository operation.
            repositoryId (string) --The ID of the repository that was deleted.
            
            
    :type repositoryName: string
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


def get_branch(repositoryName=None, branchName=None):
    """
    :param repositoryName: The name of the repository that contains the branch for which you want to retrieve information.
    :type repositoryName: string
    :param branchName: The name of the branch for which you want to retrieve information.
    :type branchName: string
    """
    pass


def get_commit(repositoryName=None, commitId=None):
    """
    :param repositoryName: [REQUIRED]
            The name of the repository to which the commit was made.
            
    :type repositoryName: string
    :param commitId: [REQUIRED]
            The commit ID.
            
    :type commitId: string
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


def get_repository(repositoryName=None):
    """
    :param repositoryName: [REQUIRED]
            The name of the repository to get information about.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the output of a get repository operation.
            repositoryMetadata (dict) --Information about the repository.
            accountId (string) --The ID of the AWS account associated with the repository.
            repositoryId (string) --The ID of the repository.
            repositoryName (string) --The repository's name.
            repositoryDescription (string) --A comment or description about the repository.
            defaultBranch (string) --The repository's default branch name.
            lastModifiedDate (datetime) --The date and time the repository was last modified, in timestamp format.
            creationDate (datetime) --The date and time the repository was created, in timestamp format.
            cloneUrlHttp (string) --The URL to use for cloning the repository over HTTPS.
            cloneUrlSsh (string) --The URL to use for cloning the repository over SSH.
            Arn (string) --The Amazon Resource Name (ARN) of the repository.
            
            
            
    :type repositoryName: string
    """
    pass


def get_repository_triggers(repositoryName=None):
    """
    :param repositoryName: The name of the repository for which the trigger is configured.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the output of a get repository triggers operation.
            configurationId (string) --The system-generated unique ID for the trigger.
            triggers (list) --The JSON block of configuration information for each trigger.
            (dict) --Information about a trigger for a repository.
            name (string) --The name of the trigger.
            destinationArn (string) --The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).
            customData (string) --Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.
            branches (list) --The branches that will be included in the trigger configuration. If no branches are specified, the trigger will apply to all branches.
            (string) --
            events (list) --The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS). If no events are specified, the trigger will run for all repository events.
            (string) --
            
            
            
    :type repositoryName: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_branches(repositoryName=None, nextToken=None):
    """
    :param repositoryName: [REQUIRED]
            The name of the repository that contains the branches.
            
    :type repositoryName: string
    :param nextToken: An enumeration token that allows the operation to batch the results.
    :type nextToken: string
    """
    pass


def list_repositories(nextToken=None, sortBy=None, order=None):
    """
    :param nextToken: An enumeration token that allows the operation to batch the results of the operation. Batch sizes are 1,000 for list repository operations. When the client sends the token back to AWS CodeCommit, another page of 1,000 records is retrieved.
    :type nextToken: string
    :param sortBy: The criteria used to sort the results of a list repositories operation.
    :type sortBy: string
    :param order: The order in which to sort the results of a list repositories operation.
    :type order: string
    """
    pass


def put_repository_triggers(repositoryName=None, triggers=None):
    """
    :param repositoryName: The name of the repository where you want to create or update the trigger.
    :type repositoryName: string
    :param triggers: The JSON block of configuration information for each trigger.
            (dict) --Information about a trigger for a repository.
            name (string) --The name of the trigger.
            destinationArn (string) --The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).
            customData (string) --Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.
            branches (list) --The branches that will be included in the trigger configuration. If no branches are specified, the trigger will apply to all branches.
            (string) --
            events (list) --The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS). If no events are specified, the trigger will run for all repository events.
            (string) --
            
            
    :type triggers: list
    """
    pass


def test_repository_triggers(repositoryName=None, triggers=None):
    """
    :param repositoryName: The name of the repository in which to test the triggers.
    :type repositoryName: string
    :param triggers: The list of triggers to test.
            (dict) --Information about a trigger for a repository.
            name (string) --The name of the trigger.
            destinationArn (string) --The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).
            customData (string) --Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.
            branches (list) --The branches that will be included in the trigger configuration. If no branches are specified, the trigger will apply to all branches.
            (string) --
            events (list) --The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS). If no events are specified, the trigger will run for all repository events.
            (string) --
            
            
    :type triggers: list
    """
    pass


def update_default_branch(repositoryName=None, defaultBranchName=None):
    """
    :param repositoryName: [REQUIRED]
            The name of the repository to set or change the default branch for.
            
    :type repositoryName: string
    :param defaultBranchName: [REQUIRED]
            The name of the branch to set as the default.
            
    :type defaultBranchName: string
    """
    pass


def update_repository_description(repositoryName=None, repositoryDescription=None):
    """
    :param repositoryName: [REQUIRED]
            The name of the repository to set or change the comment or description for.
            
    :type repositoryName: string
    :param repositoryDescription: The new comment or description for the specified repository. Repository descriptions are limited to 1,000 characters.
    :type repositoryDescription: string
    """
    pass


def update_repository_name(oldName=None, newName=None):
    """
    :param oldName: [REQUIRED]
            The existing name of the repository.
            
    :type oldName: string
    :param newName: [REQUIRED]
            The new name for the repository.
            
    :type newName: string
    """
    pass
