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
    
    
    :example: response = client.associate_team_member(
        projectId='string',
        clientRequestToken='string',
        userArn='string',
        projectRole='string',
        remoteAccessAllowed=True|False
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]
            The ID of the project to which you will add the IAM user.
            

    :type clientRequestToken: string
    :param clientRequestToken: A user- or system-generated token that identifies the entity that requested the team member association to the project. This token can be used to repeat the request.

    :type userArn: string
    :param userArn: [REQUIRED]
            The Amazon Resource Name (ARN) for the IAM user you want to add to the DevHub project.
            

    :type projectRole: string
    :param projectRole: [REQUIRED]
            The AWS CodeStar project role that will apply to this user. This role determines what actions a user can take in an AWS CodeStar project.
            

    :type remoteAccessAllowed: boolean
    :param remoteAccessAllowed: Whether the team member is allowed to use an SSH public/private key pair to remotely access project resources, for example Amazon EC2 instances.

    :rtype: dict
    :return: {
        'clientRequestToken': 'string'
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

def create_project(name=None, id=None, description=None, clientRequestToken=None):
    """
    Reserved for future use. To create a project, use the AWS CodeStar console.
    See also: AWS API Documentation
    
    
    :example: response = client.create_project(
        name='string',
        id='string',
        description='string',
        clientRequestToken='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            Reserved for future use.
            

    :type id: string
    :param id: [REQUIRED]
            Reserved for future use.
            

    :type description: string
    :param description: Reserved for future use.

    :type clientRequestToken: string
    :param clientRequestToken: Reserved for future use.

    :rtype: dict
    :return: {
        'id': 'string',
        'arn': 'string',
        'clientRequestToken': 'string',
        'projectTemplateId': 'string'
    }
    
    
    """
    pass

def create_user_profile(userArn=None, displayName=None, emailAddress=None, sshPublicKey=None):
    """
    Creates a profile for a user that includes user preferences, such as the display name and email address assocciated with the user, in AWS CodeStar. The user profile is not project-specific. Information in the user profile is displayed wherever the user's information appears to other users in AWS CodeStar.
    See also: AWS API Documentation
    
    
    :example: response = client.create_user_profile(
        userArn='string',
        displayName='string',
        emailAddress='string',
        sshPublicKey='string'
    )
    
    
    :type userArn: string
    :param userArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the user in IAM.
            

    :type displayName: string
    :param displayName: [REQUIRED]
            The name that will be displayed as the friendly name for the user in AWS CodeStar.
            

    :type emailAddress: string
    :param emailAddress: [REQUIRED]
            The email address that will be displayed as part of the user's profile in AWS CodeStar.
            

    :type sshPublicKey: string
    :param sshPublicKey: The SSH public key associated with the user in AWS CodeStar. If a project owner allows the user remote access to project resources, this public key will be used along with the user's private key for SSH access.

    :rtype: dict
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

def delete_project(id=None, clientRequestToken=None, deleteStack=None):
    """
    Deletes a project, including project resources. Does not delete users associated with the project, but does delete the IAM roles that allowed access to the project.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_project(
        id='string',
        clientRequestToken='string',
        deleteStack=True|False
    )
    
    
    :type id: string
    :param id: [REQUIRED]
            The ID of the project to be deleted in AWS CodeStar.
            

    :type clientRequestToken: string
    :param clientRequestToken: A user- or system-generated token that identifies the entity that requested project deletion. This token can be used to repeat the request.

    :type deleteStack: boolean
    :param deleteStack: Whether to send a delete request for the primary stack in AWS CloudFormation originally used to generate the project and its resources. This option will delete all AWS resources for the project (except for any buckets in Amazon S3) as well as deleting the project itself. Recommended for most use cases.

    :rtype: dict
    :return: {
        'stackId': 'string',
        'projectArn': 'string'
    }
    
    
    """
    pass

def delete_user_profile(userArn=None):
    """
    Deletes a user profile in AWS CodeStar, including all personal preference data associated with that profile, such as display name and email address. It does not delete the history of that user, for example the history of commits made by that user.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_user_profile(
        userArn='string'
    )
    
    
    :type userArn: string
    :param userArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the user to delete from AWS CodeStar.
            

    :rtype: dict
    :return: {
        'userArn': 'string'
    }
    
    
    """
    pass

def describe_project(id=None):
    """
    Describes a project and its resources.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_project(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]
            The ID of the project.
            

    :rtype: dict
    :return: {
        'name': 'string',
        'id': 'string',
        'arn': 'string',
        'description': 'string',
        'clientRequestToken': 'string',
        'createdTimeStamp': datetime(2015, 1, 1),
        'stackId': 'string',
        'projectTemplateId': 'string'
    }
    
    
    """
    pass

def describe_user_profile(userArn=None):
    """
    Describes a user in AWS CodeStar and the user attributes across all projects.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_user_profile(
        userArn='string'
    )
    
    
    :type userArn: string
    :param userArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the user.
            

    :rtype: dict
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
    Removes a user from a project. Removing a user from a project also removes the IAM policies from that user that allowed access to the project and its resources. Disassociating a team member does not remove that user's profile from AWS CodeStar. It does not remove the user from IAM.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_team_member(
        projectId='string',
        userArn='string'
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]
            The ID of the AWS CodeStar project from which you want to remove a team member.
            

    :type userArn: string
    :param userArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM user or group whom you want to remove from the project.
            

    :rtype: dict
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

def get_waiter():
    """
    
    """
    pass

def list_projects(nextToken=None, maxResults=None):
    """
    Lists all projects in AWS CodeStar associated with your AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_projects(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The continuation token to be used to return the next set of results, if the results cannot be returned in one response.

    :type maxResults: integer
    :param maxResults: The maximum amount of data that can be contained in a single set of results.

    :rtype: dict
    :return: {
        'projects': [
            {
                'projectId': 'string',
                'projectArn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_resources(projectId=None, nextToken=None, maxResults=None):
    """
    Lists resources associated with a project in AWS CodeStar.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resources(
        projectId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]
            The ID of the project.
            

    :type nextToken: string
    :param nextToken: The continuation token for the next set of results, if the results cannot be returned in one response.

    :type maxResults: integer
    :param maxResults: he maximum amount of data that can be contained in a single set of results.

    :rtype: dict
    :return: {
        'resources': [
            {
                'id': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_team_members(projectId=None, nextToken=None, maxResults=None):
    """
    Lists all team members associated with a project.
    See also: AWS API Documentation
    
    
    :example: response = client.list_team_members(
        projectId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]
            The ID of the project for which you want to list team members.
            

    :type nextToken: string
    :param nextToken: The continuation token for the next set of results, if the results cannot be returned in one response.

    :type maxResults: integer
    :param maxResults: The maximum number of team members you want returned in a response.

    :rtype: dict
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
    
    
    """
    pass

def list_user_profiles(nextToken=None, maxResults=None):
    """
    Lists all the user profiles configured for your AWS account in AWS CodeStar.
    See also: AWS API Documentation
    
    
    :example: response = client.list_user_profiles(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The continuation token for the next set of results, if the results cannot be returned in one response.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in a response.

    :rtype: dict
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
    
    
    """
    pass

def update_project(id=None, name=None, description=None):
    """
    Updates a project in AWS CodeStar.
    See also: AWS API Documentation
    
    
    :example: response = client.update_project(
        id='string',
        name='string',
        description='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]
            The ID of the project you want to update.
            

    :type name: string
    :param name: The name of the project you want to update.

    :type description: string
    :param description: The description of the project, if any.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_team_member(projectId=None, userArn=None, projectRole=None, remoteAccessAllowed=None):
    """
    Updates a team member's attributes in an AWS CodeStar project. For example, you can change a team member's role in the project, or change whether they have remote access to project resources.
    See also: AWS API Documentation
    
    
    :example: response = client.update_team_member(
        projectId='string',
        userArn='string',
        projectRole='string',
        remoteAccessAllowed=True|False
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]
            The ID of the project.
            

    :type userArn: string
    :param userArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the user for whom you want to change team membership attributes.
            

    :type projectRole: string
    :param projectRole: The role assigned to the user in the project. Project roles have different levels of access. For more information, see Working with Teams in the AWS CodeStar User Guide.

    :type remoteAccessAllowed: boolean
    :param remoteAccessAllowed: Whether a team member is allowed to remotely access project resources using the SSH public key associated with the user's profile. Even if this is set to True, the user must associate a public key with their profile before the user can access resources.

    :rtype: dict
    :return: {
        'userArn': 'string',
        'projectRole': 'string',
        'remoteAccessAllowed': True|False
    }
    
    
    """
    pass

def update_user_profile(userArn=None, displayName=None, emailAddress=None, sshPublicKey=None):
    """
    Updates a user's profile in AWS CodeStar. The user profile is not project-specific. Information in the user profile is displayed wherever the user's information appears to other users in AWS CodeStar.
    See also: AWS API Documentation
    
    
    :example: response = client.update_user_profile(
        userArn='string',
        displayName='string',
        emailAddress='string',
        sshPublicKey='string'
    )
    
    
    :type userArn: string
    :param userArn: [REQUIRED]
            The name that will be displayed as the friendly name for the user in AWS CodeStar.
            

    :type displayName: string
    :param displayName: The name that is displayed as the friendly name for the user in AWS CodeStar.

    :type emailAddress: string
    :param emailAddress: The email address that is displayed as part of the user's profile in AWS CodeStar.

    :type sshPublicKey: string
    :param sshPublicKey: The SSH public key associated with the user in AWS CodeStar. If a project owner allows the user remote access to project resources, this public key will be used along with the user's private key for SSH access.

    :rtype: dict
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

