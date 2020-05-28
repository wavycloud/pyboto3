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

def associate_team_member(projectId=None, clientRequestToken=None, userArn=None, projectRole=None, remoteAccessAllowed=None):
    """
    Adds an IAM user to the team for an AWS CodeStar project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_team_member(
        projectId='string',
        clientRequestToken='string',
        userArn='string',
        projectRole='string',
        remoteAccessAllowed=True|False
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]\nThe ID of the project to which you will add the IAM user.\n

    :type clientRequestToken: string
    :param clientRequestToken: A user- or system-generated token that identifies the entity that requested the team member association to the project. This token can be used to repeat the request.

    :type userArn: string
    :param userArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the IAM user you want to add to the AWS CodeStar project.\n

    :type projectRole: string
    :param projectRole: [REQUIRED]\nThe AWS CodeStar project role that will apply to this user. This role determines what actions a user can take in an AWS CodeStar project.\n

    :type remoteAccessAllowed: boolean
    :param remoteAccessAllowed: Whether the team member is allowed to use an SSH public/private key pair to remotely access project resources, for example Amazon EC2 instances.

    :rtype: dict

ReturnsResponse Syntax
{
    'clientRequestToken': 'string'
}


Response Structure

(dict) --

clientRequestToken (string) --
The user- or system-generated token from the initial request that can be used to repeat the request.







Exceptions

CodeStar.Client.exceptions.LimitExceededException
CodeStar.Client.exceptions.ProjectNotFoundException
CodeStar.Client.exceptions.TeamMemberAlreadyAssociatedException
CodeStar.Client.exceptions.ValidationException
CodeStar.Client.exceptions.InvalidServiceRoleException
CodeStar.Client.exceptions.ProjectConfigurationException
CodeStar.Client.exceptions.ConcurrentModificationException


    :return: {
        'clientRequestToken': 'string'
    }
    
    
    :returns: 
    CodeStar.Client.exceptions.LimitExceededException
    CodeStar.Client.exceptions.ProjectNotFoundException
    CodeStar.Client.exceptions.TeamMemberAlreadyAssociatedException
    CodeStar.Client.exceptions.ValidationException
    CodeStar.Client.exceptions.InvalidServiceRoleException
    CodeStar.Client.exceptions.ProjectConfigurationException
    CodeStar.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_project(name=None, id=None, description=None, clientRequestToken=None, sourceCode=None, toolchain=None, tags=None):
    """
    Creates a project, including project resources. This action creates a project based on a submitted project request. A set of source code files and a toolchain template file can be included with the project request. If these are not provided, an empty project is created.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_project(
        name='string',
        id='string',
        description='string',
        clientRequestToken='string',
        sourceCode=[
            {
                'source': {
                    's3': {
                        'bucketName': 'string',
                        'bucketKey': 'string'
                    }
                },
                'destination': {
                    'codeCommit': {
                        'name': 'string'
                    },
                    'gitHub': {
                        'name': 'string',
                        'description': 'string',
                        'type': 'string',
                        'owner': 'string',
                        'privateRepository': True|False,
                        'issuesEnabled': True|False,
                        'token': 'string'
                    }
                }
            },
        ],
        toolchain={
            'source': {
                's3': {
                    'bucketName': 'string',
                    'bucketKey': 'string'
                }
            },
            'roleArn': 'string',
            'stackParameters': {
                'string': 'string'
            }
        },
        tags={
            'string': 'string'
        }
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe display name for the project to be created in AWS CodeStar.\n

    :type id: string
    :param id: [REQUIRED]\nThe ID of the project to be created in AWS CodeStar.\n

    :type description: string
    :param description: The description of the project, if any.

    :type clientRequestToken: string
    :param clientRequestToken: A user- or system-generated token that identifies the entity that requested project creation. This token can be used to repeat the request.

    :type sourceCode: list
    :param sourceCode: A list of the Code objects submitted with the project request. If this parameter is specified, the request must also include the toolchain parameter.\n\n(dict) --Location and destination information about the source code files provided with the project request. The source code is uploaded to the new project source repository after project creation.\n\nsource (dict) -- [REQUIRED]The location where the source code files provided with the project request are stored. AWS CodeStar retrieves the files during project creation.\n\ns3 (dict) -- [REQUIRED]Information about the Amazon S3 location where the source code files provided with the project request are stored.\n\nbucketName (string) --The Amazon S3 bucket name where the source code files provided with the project request are stored.\n\nbucketKey (string) --The Amazon S3 object key where the source code files provided with the project request are stored.\n\n\n\n\n\ndestination (dict) -- [REQUIRED]The repository to be created in AWS CodeStar. Valid values are AWS CodeCommit or GitHub. After AWS CodeStar provisions the new repository, the source code files provided with the project request are placed in the repository.\n\ncodeCommit (dict) --Information about the AWS CodeCommit repository to be created in AWS CodeStar. This is where the source code files provided with the project request will be uploaded after project creation.\n\nname (string) -- [REQUIRED]The name of the AWS CodeCommit repository to be created in AWS CodeStar.\n\n\n\ngitHub (dict) --Information about the GitHub repository to be created in AWS CodeStar. This is where the source code files provided with the project request will be uploaded after project creation.\n\nname (string) -- [REQUIRED]Name of the GitHub repository to be created in AWS CodeStar.\n\ndescription (string) --Description for the GitHub repository to be created in AWS CodeStar. This description displays in GitHub after the repository is created.\n\ntype (string) -- [REQUIRED]The type of GitHub repository to be created in AWS CodeStar. Valid values are User or Organization.\n\nowner (string) -- [REQUIRED]The GitHub username for the owner of the GitHub repository to be created in AWS CodeStar. If this repository should be owned by a GitHub organization, provide its name.\n\nprivateRepository (boolean) -- [REQUIRED]Whether the GitHub repository is to be a private repository.\n\nissuesEnabled (boolean) -- [REQUIRED]Whether to enable issues for the GitHub repository.\n\ntoken (string) -- [REQUIRED]The GitHub user\'s personal access token for the GitHub repository.\n\n\n\n\n\n\n\n\n

    :type toolchain: dict
    :param toolchain: The name of the toolchain template file submitted with the project request. If this parameter is specified, the request must also include the sourceCode parameter.\n\nsource (dict) -- [REQUIRED]The Amazon S3 location where the toolchain template file provided with the project request is stored. AWS CodeStar retrieves the file during project creation.\n\ns3 (dict) -- [REQUIRED]The Amazon S3 bucket where the toolchain template file provided with the project request is stored.\n\nbucketName (string) --The Amazon S3 bucket name where the source code files provided with the project request are stored.\n\nbucketKey (string) --The Amazon S3 object key where the source code files provided with the project request are stored.\n\n\n\n\n\nroleArn (string) --The service role ARN for AWS CodeStar to use for the toolchain template during stack provisioning.\n\nstackParameters (dict) --The list of parameter overrides to be passed into the toolchain template during stack provisioning, if any.\n\n(string) --\n(string) --\n\n\n\n\n\n

    :type tags: dict
    :param tags: The tags created for the project.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'id': 'string',
    'arn': 'string',
    'clientRequestToken': 'string',
    'projectTemplateId': 'string'
}


Response Structure

(dict) --

id (string) --
The ID of the project.

arn (string) --
The Amazon Resource Name (ARN) of the created project.

clientRequestToken (string) --
A user- or system-generated token that identifies the entity that requested project creation.

projectTemplateId (string) --
Reserved for future use.







Exceptions

CodeStar.Client.exceptions.ProjectAlreadyExistsException
CodeStar.Client.exceptions.LimitExceededException
CodeStar.Client.exceptions.ValidationException
CodeStar.Client.exceptions.ProjectCreationFailedException
CodeStar.Client.exceptions.InvalidServiceRoleException
CodeStar.Client.exceptions.ProjectConfigurationException
CodeStar.Client.exceptions.ConcurrentModificationException


    :return: {
        'id': 'string',
        'arn': 'string',
        'clientRequestToken': 'string',
        'projectTemplateId': 'string'
    }
    
    
    :returns: 
    CodeStar.Client.exceptions.ProjectAlreadyExistsException
    CodeStar.Client.exceptions.LimitExceededException
    CodeStar.Client.exceptions.ValidationException
    CodeStar.Client.exceptions.ProjectCreationFailedException
    CodeStar.Client.exceptions.InvalidServiceRoleException
    CodeStar.Client.exceptions.ProjectConfigurationException
    CodeStar.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def create_user_profile(userArn=None, displayName=None, emailAddress=None, sshPublicKey=None):
    """
    Creates a profile for a user that includes user preferences, such as the display name and email address assocciated with the user, in AWS CodeStar. The user profile is not project-specific. Information in the user profile is displayed wherever the user\'s information appears to other users in AWS CodeStar.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_user_profile(
        userArn='string',
        displayName='string',
        emailAddress='string',
        sshPublicKey='string'
    )
    
    
    :type userArn: string
    :param userArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the user in IAM.\n

    :type displayName: string
    :param displayName: [REQUIRED]\nThe name that will be displayed as the friendly name for the user in AWS CodeStar.\n

    :type emailAddress: string
    :param emailAddress: [REQUIRED]\nThe email address that will be displayed as part of the user\'s profile in AWS CodeStar.\n

    :type sshPublicKey: string
    :param sshPublicKey: The SSH public key associated with the user in AWS CodeStar. If a project owner allows the user remote access to project resources, this public key will be used along with the user\'s private key for SSH access.

    :rtype: dict

ReturnsResponse Syntax
{
    'userArn': 'string',
    'displayName': 'string',
    'emailAddress': 'string',
    'sshPublicKey': 'string',
    'createdTimestamp': datetime(2015, 1, 1),
    'lastModifiedTimestamp': datetime(2015, 1, 1)
}


Response Structure

(dict) --

userArn (string) --
The Amazon Resource Name (ARN) of the user in IAM.

displayName (string) --
The name that is displayed as the friendly name for the user in AWS CodeStar.

emailAddress (string) --
The email address that is displayed as part of the user\'s profile in AWS CodeStar.

sshPublicKey (string) --
The SSH public key associated with the user in AWS CodeStar. This is the public portion of the public/private keypair the user can use to access project resources if a project owner allows the user remote access to those resources.

createdTimestamp (datetime) --
The date the user profile was created, in timestamp format.

lastModifiedTimestamp (datetime) --
The date the user profile was last modified, in timestamp format.







Exceptions

CodeStar.Client.exceptions.UserProfileAlreadyExistsException
CodeStar.Client.exceptions.ValidationException


    :return: {
        'userArn': 'string',
        'displayName': 'string',
        'emailAddress': 'string',
        'sshPublicKey': 'string',
        'createdTimestamp': datetime(2015, 1, 1),
        'lastModifiedTimestamp': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    CodeStar.Client.exceptions.UserProfileAlreadyExistsException
    CodeStar.Client.exceptions.ValidationException
    
    """
    pass

def delete_project(id=None, clientRequestToken=None, deleteStack=None):
    """
    Deletes a project, including project resources. Does not delete users associated with the project, but does delete the IAM roles that allowed access to the project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_project(
        id='string',
        clientRequestToken='string',
        deleteStack=True|False
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the project to be deleted in AWS CodeStar.\n

    :type clientRequestToken: string
    :param clientRequestToken: A user- or system-generated token that identifies the entity that requested project deletion. This token can be used to repeat the request.

    :type deleteStack: boolean
    :param deleteStack: Whether to send a delete request for the primary stack in AWS CloudFormation originally used to generate the project and its resources. This option will delete all AWS resources for the project (except for any buckets in Amazon S3) as well as deleting the project itself. Recommended for most use cases.

    :rtype: dict

ReturnsResponse Syntax
{
    'stackId': 'string',
    'projectArn': 'string'
}


Response Structure

(dict) --

stackId (string) --
The ID of the primary stack in AWS CloudFormation that will be deleted as part of deleting the project and its resources.

projectArn (string) --
The Amazon Resource Name (ARN) of the deleted project.







Exceptions

CodeStar.Client.exceptions.ConcurrentModificationException
CodeStar.Client.exceptions.ValidationException
CodeStar.Client.exceptions.InvalidServiceRoleException


    :return: {
        'stackId': 'string',
        'projectArn': 'string'
    }
    
    
    :returns: 
    CodeStar.Client.exceptions.ConcurrentModificationException
    CodeStar.Client.exceptions.ValidationException
    CodeStar.Client.exceptions.InvalidServiceRoleException
    
    """
    pass

def delete_user_profile(userArn=None):
    """
    Deletes a user profile in AWS CodeStar, including all personal preference data associated with that profile, such as display name and email address. It does not delete the history of that user, for example the history of commits made by that user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user_profile(
        userArn='string'
    )
    
    
    :type userArn: string
    :param userArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the user to delete from AWS CodeStar.\n

    :rtype: dict
ReturnsResponse Syntax{
    'userArn': 'string'
}


Response Structure

(dict) --
userArn (string) --The Amazon Resource Name (ARN) of the user deleted from AWS CodeStar.






Exceptions

CodeStar.Client.exceptions.ValidationException


    :return: {
        'userArn': 'string'
    }
    
    
    """
    pass

def describe_project(id=None):
    """
    Describes a project and its resources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_project(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the project.\n

    :rtype: dict
ReturnsResponse Syntax{
    'name': 'string',
    'id': 'string',
    'arn': 'string',
    'description': 'string',
    'clientRequestToken': 'string',
    'createdTimeStamp': datetime(2015, 1, 1),
    'stackId': 'string',
    'projectTemplateId': 'string',
    'status': {
        'state': 'string',
        'reason': 'string'
    }
}


Response Structure

(dict) --
name (string) --The display name for the project.

id (string) --The ID of the project.

arn (string) --The Amazon Resource Name (ARN) for the project.

description (string) --The description of the project, if any.

clientRequestToken (string) --A user- or system-generated token that identifies the entity that requested project creation.

createdTimeStamp (datetime) --The date and time the project was created, in timestamp format.

stackId (string) --The ID of the primary stack in AWS CloudFormation used to generate resources for the project.

projectTemplateId (string) --The ID for the AWS CodeStar project template used to create the project.

status (dict) --The project creation or deletion status.

state (string) --The phase of completion for a project creation or deletion.

reason (string) --In the case of a project creation or deletion failure, a reason for the failure.








Exceptions

CodeStar.Client.exceptions.ProjectNotFoundException
CodeStar.Client.exceptions.ValidationException
CodeStar.Client.exceptions.InvalidServiceRoleException
CodeStar.Client.exceptions.ProjectConfigurationException
CodeStar.Client.exceptions.ConcurrentModificationException


    :return: {
        'name': 'string',
        'id': 'string',
        'arn': 'string',
        'description': 'string',
        'clientRequestToken': 'string',
        'createdTimeStamp': datetime(2015, 1, 1),
        'stackId': 'string',
        'projectTemplateId': 'string',
        'status': {
            'state': 'string',
            'reason': 'string'
        }
    }
    
    
    """
    pass

def describe_user_profile(userArn=None):
    """
    Describes a user in AWS CodeStar and the user attributes across all projects.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_user_profile(
        userArn='string'
    )
    
    
    :type userArn: string
    :param userArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the user.\n

    :rtype: dict
ReturnsResponse Syntax{
    'userArn': 'string',
    'displayName': 'string',
    'emailAddress': 'string',
    'sshPublicKey': 'string',
    'createdTimestamp': datetime(2015, 1, 1),
    'lastModifiedTimestamp': datetime(2015, 1, 1)
}


Response Structure

(dict) --
userArn (string) --The Amazon Resource Name (ARN) of the user.

displayName (string) --The display name shown for the user in AWS CodeStar projects. For example, this could be set to both first and last name ("Mary Major") or a single name ("Mary"). The display name is also used to generate the initial icon associated with the user in AWS CodeStar projects. If spaces are included in the display name, the first character that appears after the space will be used as the second character in the user initial icon. The initial icon displays a maximum of two characters, so a display name with more than one space (for example "Mary Jane Major") would generate an initial icon using the first character and the first character after the space ("MJ", not "MM").

emailAddress (string) --The email address for the user. Optional.

sshPublicKey (string) --The SSH public key associated with the user. This SSH public key is associated with the user profile, and can be used in conjunction with the associated private key for access to project resources, such as Amazon EC2 instances, if a project owner grants remote access to those resources.

createdTimestamp (datetime) --The date and time when the user profile was created in AWS CodeStar, in timestamp format.

lastModifiedTimestamp (datetime) --The date and time when the user profile was last modified, in timestamp format.






Exceptions

CodeStar.Client.exceptions.UserProfileNotFoundException
CodeStar.Client.exceptions.ValidationException


    :return: {
        'userArn': 'string',
        'displayName': 'string',
        'emailAddress': 'string',
        'sshPublicKey': 'string',
        'createdTimestamp': datetime(2015, 1, 1),
        'lastModifiedTimestamp': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def disassociate_team_member(projectId=None, userArn=None):
    """
    Removes a user from a project. Removing a user from a project also removes the IAM policies from that user that allowed access to the project and its resources. Disassociating a team member does not remove that user\'s profile from AWS CodeStar. It does not remove the user from IAM.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_team_member(
        projectId='string',
        userArn='string'
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]\nThe ID of the AWS CodeStar project from which you want to remove a team member.\n

    :type userArn: string
    :param userArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM user or group whom you want to remove from the project.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CodeStar.Client.exceptions.ProjectNotFoundException
CodeStar.Client.exceptions.ValidationException
CodeStar.Client.exceptions.InvalidServiceRoleException
CodeStar.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def list_projects(nextToken=None, maxResults=None):
    """
    Lists all projects in AWS CodeStar associated with your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_projects(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The continuation token to be used to return the next set of results, if the results cannot be returned in one response.

    :type maxResults: integer
    :param maxResults: The maximum amount of data that can be contained in a single set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'projects': [
        {
            'projectId': 'string',
            'projectArn': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

projects (list) --
A list of projects.

(dict) --
Information about the metadata for a project.

projectId (string) --
The ID of the project.

projectArn (string) --
The Amazon Resource Name (ARN) of the project.





nextToken (string) --
The continuation token to use when requesting the next set of results, if there are more results to be returned.







Exceptions

CodeStar.Client.exceptions.InvalidNextTokenException
CodeStar.Client.exceptions.ValidationException


    :return: {
        'projects': [
            {
                'projectId': 'string',
                'projectArn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CodeStar.Client.exceptions.InvalidNextTokenException
    CodeStar.Client.exceptions.ValidationException
    
    """
    pass

def list_resources(projectId=None, nextToken=None, maxResults=None):
    """
    Lists resources associated with a project in AWS CodeStar.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resources(
        projectId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]\nThe ID of the project.\n

    :type nextToken: string
    :param nextToken: The continuation token for the next set of results, if the results cannot be returned in one response.

    :type maxResults: integer
    :param maxResults: The maximum amount of data that can be contained in a single set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'resources': [
        {
            'id': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

resources (list) --
An array of resources associated with the project.

(dict) --
Information about a resource for a project.

id (string) --
The Amazon Resource Name (ARN) of the resource.





nextToken (string) --
The continuation token to use when requesting the next set of results, if there are more results to be returned.







Exceptions

CodeStar.Client.exceptions.ProjectNotFoundException
CodeStar.Client.exceptions.InvalidNextTokenException
CodeStar.Client.exceptions.ValidationException


    :return: {
        'resources': [
            {
                'id': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CodeStar.Client.exceptions.ProjectNotFoundException
    CodeStar.Client.exceptions.InvalidNextTokenException
    CodeStar.Client.exceptions.ValidationException
    
    """
    pass

def list_tags_for_project(id=None, nextToken=None, maxResults=None):
    """
    Gets the tags for a project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_project(
        id='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the project to get tags for.\n

    :type nextToken: string
    :param nextToken: Reserved for future use.

    :type maxResults: integer
    :param maxResults: Reserved for future use.

    :rtype: dict

ReturnsResponse Syntax
{
    'tags': {
        'string': 'string'
    },
    'nextToken': 'string'
}


Response Structure

(dict) --

tags (dict) --
The tags for the project.

(string) --
(string) --




nextToken (string) --
Reserved for future use.







Exceptions

CodeStar.Client.exceptions.ProjectNotFoundException
CodeStar.Client.exceptions.ValidationException
CodeStar.Client.exceptions.InvalidNextTokenException


    :return: {
        'tags': {
            'string': 'string'
        },
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_team_members(projectId=None, nextToken=None, maxResults=None):
    """
    Lists all team members associated with a project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_team_members(
        projectId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]\nThe ID of the project for which you want to list team members.\n

    :type nextToken: string
    :param nextToken: The continuation token for the next set of results, if the results cannot be returned in one response.

    :type maxResults: integer
    :param maxResults: The maximum number of team members you want returned in a response.

    :rtype: dict

ReturnsResponse Syntax
{
    'teamMembers': [
        {
            'userArn': 'string',
            'projectRole': 'string',
            'remoteAccessAllowed': True|False
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

teamMembers (list) --
A list of team member objects for the project.

(dict) --
Information about a team member in a project.

userArn (string) --
The Amazon Resource Name (ARN) of the user in IAM.

projectRole (string) --
The role assigned to the user in the project. Project roles have different levels of access. For more information, see Working with Teams in the AWS CodeStar User Guide .

remoteAccessAllowed (boolean) --
Whether the user is allowed to remotely access project resources using an SSH public/private key pair.





nextToken (string) --
The continuation token to use when requesting the next set of results, if there are more results to be returned.







Exceptions

CodeStar.Client.exceptions.ProjectNotFoundException
CodeStar.Client.exceptions.InvalidNextTokenException
CodeStar.Client.exceptions.ValidationException


    :return: {
        'teamMembers': [
            {
                'userArn': 'string',
                'projectRole': 'string',
                'remoteAccessAllowed': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CodeStar.Client.exceptions.ProjectNotFoundException
    CodeStar.Client.exceptions.InvalidNextTokenException
    CodeStar.Client.exceptions.ValidationException
    
    """
    pass

def list_user_profiles(nextToken=None, maxResults=None):
    """
    Lists all the user profiles configured for your AWS account in AWS CodeStar.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_user_profiles(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The continuation token for the next set of results, if the results cannot be returned in one response.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in a response.

    :rtype: dict

ReturnsResponse Syntax
{
    'userProfiles': [
        {
            'userArn': 'string',
            'displayName': 'string',
            'emailAddress': 'string',
            'sshPublicKey': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

userProfiles (list) --
All the user profiles configured in AWS CodeStar for an AWS account.

(dict) --
Information about a user\'s profile in AWS CodeStar.

userArn (string) --
The Amazon Resource Name (ARN) of the user in IAM.

displayName (string) --
The display name of a user in AWS CodeStar. For example, this could be set to both first and last name ("Mary Major") or a single name ("Mary"). The display name is also used to generate the initial icon associated with the user in AWS CodeStar projects. If spaces are included in the display name, the first character that appears after the space will be used as the second character in the user initial icon. The initial icon displays a maximum of two characters, so a display name with more than one space (for example "Mary Jane Major") would generate an initial icon using the first character and the first character after the space ("MJ", not "MM").

emailAddress (string) --
The email address associated with the user.

sshPublicKey (string) --
The SSH public key associated with the user in AWS CodeStar. If a project owner allows the user remote access to project resources, this public key will be used along with the user\'s private key for SSH access.





nextToken (string) --
The continuation token to use when requesting the next set of results, if there are more results to be returned.







Exceptions

CodeStar.Client.exceptions.InvalidNextTokenException
CodeStar.Client.exceptions.ValidationException


    :return: {
        'userProfiles': [
            {
                'userArn': 'string',
                'displayName': 'string',
                'emailAddress': 'string',
                'sshPublicKey': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CodeStar.Client.exceptions.InvalidNextTokenException
    CodeStar.Client.exceptions.ValidationException
    
    """
    pass

def tag_project(id=None, tags=None):
    """
    Adds tags to a project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_project(
        id='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the project you want to add a tag to.\n

    :type tags: dict
    :param tags: [REQUIRED]\nThe tags you want to add to the project.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

tags (dict) --
The tags for the project.

(string) --
(string) --










Exceptions

CodeStar.Client.exceptions.ProjectNotFoundException
CodeStar.Client.exceptions.ValidationException
CodeStar.Client.exceptions.LimitExceededException
CodeStar.Client.exceptions.ConcurrentModificationException


    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def untag_project(id=None, tags=None):
    """
    Removes tags from a project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_project(
        id='string',
        tags=[
            'string',
        ]
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the project to remove tags from.\n

    :type tags: list
    :param tags: [REQUIRED]\nThe tags to remove from the project.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CodeStar.Client.exceptions.ProjectNotFoundException
CodeStar.Client.exceptions.ValidationException
CodeStar.Client.exceptions.LimitExceededException
CodeStar.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_project(id=None, name=None, description=None):
    """
    Updates a project in AWS CodeStar.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_project(
        id='string',
        name='string',
        description='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the project you want to update.\n

    :type name: string
    :param name: The name of the project you want to update.

    :type description: string
    :param description: The description of the project, if any.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CodeStar.Client.exceptions.ProjectNotFoundException
CodeStar.Client.exceptions.ValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_team_member(projectId=None, userArn=None, projectRole=None, remoteAccessAllowed=None):
    """
    Updates a team member\'s attributes in an AWS CodeStar project. For example, you can change a team member\'s role in the project, or change whether they have remote access to project resources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_team_member(
        projectId='string',
        userArn='string',
        projectRole='string',
        remoteAccessAllowed=True|False
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]\nThe ID of the project.\n

    :type userArn: string
    :param userArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the user for whom you want to change team membership attributes.\n

    :type projectRole: string
    :param projectRole: The role assigned to the user in the project. Project roles have different levels of access. For more information, see Working with Teams in the AWS CodeStar User Guide .

    :type remoteAccessAllowed: boolean
    :param remoteAccessAllowed: Whether a team member is allowed to remotely access project resources using the SSH public key associated with the user\'s profile. Even if this is set to True, the user must associate a public key with their profile before the user can access resources.

    :rtype: dict

ReturnsResponse Syntax
{
    'userArn': 'string',
    'projectRole': 'string',
    'remoteAccessAllowed': True|False
}


Response Structure

(dict) --

userArn (string) --
The Amazon Resource Name (ARN) of the user whose team membership attributes were updated.

projectRole (string) --
The project role granted to the user.

remoteAccessAllowed (boolean) --
Whether a team member is allowed to remotely access project resources using the SSH public key associated with the user\'s profile.







Exceptions

CodeStar.Client.exceptions.LimitExceededException
CodeStar.Client.exceptions.ProjectNotFoundException
CodeStar.Client.exceptions.ValidationException
CodeStar.Client.exceptions.InvalidServiceRoleException
CodeStar.Client.exceptions.ProjectConfigurationException
CodeStar.Client.exceptions.ConcurrentModificationException
CodeStar.Client.exceptions.TeamMemberNotFoundException


    :return: {
        'userArn': 'string',
        'projectRole': 'string',
        'remoteAccessAllowed': True|False
    }
    
    
    :returns: 
    CodeStar.Client.exceptions.LimitExceededException
    CodeStar.Client.exceptions.ProjectNotFoundException
    CodeStar.Client.exceptions.ValidationException
    CodeStar.Client.exceptions.InvalidServiceRoleException
    CodeStar.Client.exceptions.ProjectConfigurationException
    CodeStar.Client.exceptions.ConcurrentModificationException
    CodeStar.Client.exceptions.TeamMemberNotFoundException
    
    """
    pass

def update_user_profile(userArn=None, displayName=None, emailAddress=None, sshPublicKey=None):
    """
    Updates a user\'s profile in AWS CodeStar. The user profile is not project-specific. Information in the user profile is displayed wherever the user\'s information appears to other users in AWS CodeStar.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user_profile(
        userArn='string',
        displayName='string',
        emailAddress='string',
        sshPublicKey='string'
    )
    
    
    :type userArn: string
    :param userArn: [REQUIRED]\nThe name that will be displayed as the friendly name for the user in AWS CodeStar.\n

    :type displayName: string
    :param displayName: The name that is displayed as the friendly name for the user in AWS CodeStar.

    :type emailAddress: string
    :param emailAddress: The email address that is displayed as part of the user\'s profile in AWS CodeStar.

    :type sshPublicKey: string
    :param sshPublicKey: The SSH public key associated with the user in AWS CodeStar. If a project owner allows the user remote access to project resources, this public key will be used along with the user\'s private key for SSH access.

    :rtype: dict

ReturnsResponse Syntax
{
    'userArn': 'string',
    'displayName': 'string',
    'emailAddress': 'string',
    'sshPublicKey': 'string',
    'createdTimestamp': datetime(2015, 1, 1),
    'lastModifiedTimestamp': datetime(2015, 1, 1)
}


Response Structure

(dict) --

userArn (string) --
The Amazon Resource Name (ARN) of the user in IAM.

displayName (string) --
The name that is displayed as the friendly name for the user in AWS CodeStar.

emailAddress (string) --
The email address that is displayed as part of the user\'s profile in AWS CodeStar.

sshPublicKey (string) --
The SSH public key associated with the user in AWS CodeStar. This is the public portion of the public/private keypair the user can use to access project resources if a project owner allows the user remote access to those resources.

createdTimestamp (datetime) --
The date the user profile was created, in timestamp format.

lastModifiedTimestamp (datetime) --
The date the user profile was last modified, in timestamp format.







Exceptions

CodeStar.Client.exceptions.UserProfileNotFoundException
CodeStar.Client.exceptions.ValidationException


    :return: {
        'userArn': 'string',
        'displayName': 'string',
        'emailAddress': 'string',
        'sshPublicKey': 'string',
        'createdTimestamp': datetime(2015, 1, 1),
        'lastModifiedTimestamp': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    CodeStar.Client.exceptions.UserProfileNotFoundException
    CodeStar.Client.exceptions.ValidationException
    
    """
    pass

