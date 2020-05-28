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

def create_environment_ec2(name=None, description=None, clientRequestToken=None, instanceType=None, subnetId=None, automaticStopTimeMinutes=None, ownerArn=None, tags=None):
    """
    Creates an AWS Cloud9 development environment, launches an Amazon Elastic Compute Cloud (Amazon EC2) instance, and then connects from the instance to the environment.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.create_environment_ec2(
        name='string',
        description='string',
        clientRequestToken='string',
        instanceType='string',
        subnetId='string',
        automaticStopTimeMinutes=123,
        ownerArn='string',
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the environment to create.\nThis name is visible to other AWS IAM users in the same AWS account.\n

    :type description: string
    :param description: The description of the environment to create.

    :type clientRequestToken: string
    :param clientRequestToken: A unique, case-sensitive string that helps AWS Cloud9 to ensure this operation completes no more than one time.\nFor more information, see Client Tokens in the Amazon EC2 API Reference .\n

    :type instanceType: string
    :param instanceType: [REQUIRED]\nThe type of instance to connect to the environment (for example, t2.micro ).\n

    :type subnetId: string
    :param subnetId: The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.

    :type automaticStopTimeMinutes: integer
    :param automaticStopTimeMinutes: The number of minutes until the running instance is shut down after the environment has last been used.

    :type ownerArn: string
    :param ownerArn: The Amazon Resource Name (ARN) of the environment owner. This ARN can be the ARN of any AWS IAM principal. If this value is not specified, the ARN defaults to this environment\'s creator.

    :type tags: list
    :param tags: An array of key-value pairs that will be associated with the new AWS Cloud9 development environment.\n\n(dict) --Metadata that is associated with AWS resources. In particular, a name-value pair that can be associated with an AWS Cloud9 development environment. There are two types of tags: user tags and system tags . A user tag is created by the user. A system tag is automatically created by AWS services. A system tag is prefixed with 'aws:' and cannot be modified by the user.\n\nKey (string) -- [REQUIRED]The name part of a tag.\n\nValue (string) -- [REQUIRED]The value part of a tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'environmentId': 'string'
}


Response Structure

(dict) --

environmentId (string) --
The ID of the environment that was created.







Exceptions

Cloud9.Client.exceptions.BadRequestException
Cloud9.Client.exceptions.ConflictException
Cloud9.Client.exceptions.NotFoundException
Cloud9.Client.exceptions.ForbiddenException
Cloud9.Client.exceptions.TooManyRequestsException
Cloud9.Client.exceptions.LimitExceededException
Cloud9.Client.exceptions.InternalServerErrorException

Examples
response = client.create_environment_ec2(
    name='my-demo-environment',
    automaticStopTimeMinutes=60,
    description='This is my demonstration environment.',
    instanceType='t2.micro',
    ownerArn='arn:aws:iam::123456789012:user/MyDemoUser',
    subnetId='subnet-1fab8aEX',
)

print(response)


Expected Output:
{
    'environmentId': '8d9967e2f0624182b74e7690ad69ebEX',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'environmentId': 'string'
    }
    
    
    :returns: 
    Cloud9.Client.exceptions.BadRequestException
    Cloud9.Client.exceptions.ConflictException
    Cloud9.Client.exceptions.NotFoundException
    Cloud9.Client.exceptions.ForbiddenException
    Cloud9.Client.exceptions.TooManyRequestsException
    Cloud9.Client.exceptions.LimitExceededException
    Cloud9.Client.exceptions.InternalServerErrorException
    
    """
    pass

def create_environment_membership(environmentId=None, userArn=None, permissions=None):
    """
    Adds an environment member to an AWS Cloud9 development environment.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.create_environment_membership(
        environmentId='string',
        userArn='string',
        permissions='read-write'|'read-only'
    )
    
    
    :type environmentId: string
    :param environmentId: [REQUIRED]\nThe ID of the environment that contains the environment member you want to add.\n

    :type userArn: string
    :param userArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the environment member you want to add.\n

    :type permissions: string
    :param permissions: [REQUIRED]\nThe type of environment member permissions you want to associate with this environment member. Available values include:\n\nread-only : Has read-only access to the environment.\nread-write : Has read-write access to the environment.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'membership': {
        'permissions': 'owner'|'read-write'|'read-only',
        'userId': 'string',
        'userArn': 'string',
        'environmentId': 'string',
        'lastAccess': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

membership (dict) --
Information about the environment member that was added.

permissions (string) --
The type of environment member permissions associated with this environment member. Available values include:

owner : Owns the environment.
read-only : Has read-only access to the environment.
read-write : Has read-write access to the environment.


userId (string) --
The user ID in AWS Identity and Access Management (AWS IAM) of the environment member.

userArn (string) --
The Amazon Resource Name (ARN) of the environment member.

environmentId (string) --
The ID of the environment for the environment member.

lastAccess (datetime) --
The time, expressed in epoch time format, when the environment member last opened the environment.









Exceptions

Cloud9.Client.exceptions.BadRequestException
Cloud9.Client.exceptions.ConflictException
Cloud9.Client.exceptions.NotFoundException
Cloud9.Client.exceptions.ForbiddenException
Cloud9.Client.exceptions.TooManyRequestsException
Cloud9.Client.exceptions.LimitExceededException
Cloud9.Client.exceptions.InternalServerErrorException

Examples
response = client.create_environment_membership(
    environmentId='8d9967e2f0624182b74e7690ad69ebEX',
    permissions='read-write',
    userArn='arn:aws:iam::123456789012:user/AnotherDemoUser',
)

print(response)


Expected Output:
{
    'membership': {
        'environmentId': '8d9967e2f0624182b74e7690ad69ebEX',
        'permissions': 'read-write',
        'userArn': 'arn:aws:iam::123456789012:user/AnotherDemoUser',
        'userId': 'AIDAJ3BA6O2FMJWCWXHEX',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'membership': {
            'permissions': 'owner'|'read-write'|'read-only',
            'userId': 'string',
            'userArn': 'string',
            'environmentId': 'string',
            'lastAccess': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    owner : Owns the environment.
    read-only : Has read-only access to the environment.
    read-write : Has read-write access to the environment.
    
    """
    pass

def delete_environment(environmentId=None):
    """
    Deletes an AWS Cloud9 development environment. If an Amazon EC2 instance is connected to the environment, also terminates the instance.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.delete_environment(
        environmentId='string'
    )
    
    
    :type environmentId: string
    :param environmentId: [REQUIRED]\nThe ID of the environment to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Cloud9.Client.exceptions.BadRequestException
Cloud9.Client.exceptions.ConflictException
Cloud9.Client.exceptions.NotFoundException
Cloud9.Client.exceptions.ForbiddenException
Cloud9.Client.exceptions.TooManyRequestsException
Cloud9.Client.exceptions.LimitExceededException
Cloud9.Client.exceptions.InternalServerErrorException

Examples
response = client.delete_environment(
    environmentId='8d9967e2f0624182b74e7690ad69ebEX',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    Cloud9.Client.exceptions.BadRequestException
    Cloud9.Client.exceptions.ConflictException
    Cloud9.Client.exceptions.NotFoundException
    Cloud9.Client.exceptions.ForbiddenException
    Cloud9.Client.exceptions.TooManyRequestsException
    Cloud9.Client.exceptions.LimitExceededException
    Cloud9.Client.exceptions.InternalServerErrorException
    
    """
    pass

def delete_environment_membership(environmentId=None, userArn=None):
    """
    Deletes an environment member from an AWS Cloud9 development environment.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.delete_environment_membership(
        environmentId='string',
        userArn='string'
    )
    
    
    :type environmentId: string
    :param environmentId: [REQUIRED]\nThe ID of the environment to delete the environment member from.\n

    :type userArn: string
    :param userArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the environment member to delete from the environment.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Cloud9.Client.exceptions.BadRequestException
Cloud9.Client.exceptions.ConflictException
Cloud9.Client.exceptions.NotFoundException
Cloud9.Client.exceptions.ForbiddenException
Cloud9.Client.exceptions.TooManyRequestsException
Cloud9.Client.exceptions.LimitExceededException
Cloud9.Client.exceptions.InternalServerErrorException

Examples
response = client.delete_environment_membership(
    environmentId='8d9967e2f0624182b74e7690ad69ebEX',
    userArn='arn:aws:iam::123456789012:user/AnotherDemoUser',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_environment_memberships(userArn=None, environmentId=None, permissions=None, nextToken=None, maxResults=None):
    """
    Gets information about environment members for an AWS Cloud9 development environment.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example gets information about all of the environment members for the specified AWS Cloud9 development environment.
    Expected Output:
    The following example gets information about the owner of the specified AWS Cloud9 development environment.
    Expected Output:
    The following example gets AWS Cloud9 development environment membership information for the specified user.
    Expected Output:
    
    :example: response = client.describe_environment_memberships(
        userArn='string',
        environmentId='string',
        permissions=[
            'owner'|'read-write'|'read-only',
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type userArn: string
    :param userArn: The Amazon Resource Name (ARN) of an individual environment member to get information about. If no value is specified, information about all environment members are returned.

    :type environmentId: string
    :param environmentId: The ID of the environment to get environment member information about.

    :type permissions: list
    :param permissions: The type of environment member permissions to get information about. Available values include:\n\nowner : Owns the environment.\nread-only : Has read-only access to the environment.\nread-write : Has read-write access to the environment.\n\nIf no value is specified, information about all environment members are returned.\n\n(string) --\n\n

    :type nextToken: string
    :param nextToken: During a previous call, if there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a next token . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :type maxResults: integer
    :param maxResults: The maximum number of environment members to get information about.

    :rtype: dict

ReturnsResponse Syntax
{
    'memberships': [
        {
            'permissions': 'owner'|'read-write'|'read-only',
            'userId': 'string',
            'userArn': 'string',
            'environmentId': 'string',
            'lastAccess': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

memberships (list) --
Information about the environment members for the environment.

(dict) --
Information about an environment member for an AWS Cloud9 development environment.

permissions (string) --
The type of environment member permissions associated with this environment member. Available values include:

owner : Owns the environment.
read-only : Has read-only access to the environment.
read-write : Has read-write access to the environment.


userId (string) --
The user ID in AWS Identity and Access Management (AWS IAM) of the environment member.

userArn (string) --
The Amazon Resource Name (ARN) of the environment member.

environmentId (string) --
The ID of the environment for the environment member.

lastAccess (datetime) --
The time, expressed in epoch time format, when the environment member last opened the environment.





nextToken (string) --
If there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a next token . To get the next batch of items in the list, call this operation again, adding the next token to the call.







Exceptions

Cloud9.Client.exceptions.BadRequestException
Cloud9.Client.exceptions.ConflictException
Cloud9.Client.exceptions.NotFoundException
Cloud9.Client.exceptions.ForbiddenException
Cloud9.Client.exceptions.TooManyRequestsException
Cloud9.Client.exceptions.LimitExceededException
Cloud9.Client.exceptions.InternalServerErrorException

Examples
The following example gets information about all of the environment members for the specified AWS Cloud9 development environment.
response = client.describe_environment_memberships(
    environmentId='8d9967e2f0624182b74e7690ad69ebEX',
)

print(response)


Expected Output:
{
    'memberships': [
        {
            'environmentId': '8d9967e2f0624182b74e7690ad69ebEX',
            'permissions': 'read-write',
            'userArn': 'arn:aws:iam::123456789012:user/AnotherDemoUser',
            'userId': 'AIDAJ3BA6O2FMJWCWXHEX',
        },
        {
            'environmentId': '8d9967e2f0624182b74e7690ad69ebEX',
            'permissions': 'owner',
            'userArn': 'arn:aws:iam::123456789012:user/MyDemoUser',
            'userId': 'AIDAJNUEDQAQWFELJDLEX',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example gets information about the owner of the specified AWS Cloud9 development environment.
response = client.describe_environment_memberships(
    environmentId='8d9967e2f0624182b74e7690ad69ebEX',
    permissions=[
        'owner',
    ],
)

print(response)


Expected Output:
{
    'memberships': [
        {
            'environmentId': '8d9967e2f0624182b74e7690ad69ebEX',
            'permissions': 'owner',
            'userArn': 'arn:aws:iam::123456789012:user/MyDemoUser',
            'userId': 'AIDAJNUEDQAQWFELJDLEX',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example gets AWS Cloud9 development environment membership information for the specified user.
response = client.describe_environment_memberships(
    userArn='arn:aws:iam::123456789012:user/MyDemoUser',
)

print(response)


Expected Output:
{
    'memberships': [
        {
            'environmentId': '10a75714bd494714929e7f5ec4125aEX',
            'lastAccess': datetime(2018, 1, 19, 11, 6, 13, 4, 19, 0),
            'permissions': 'owner',
            'userArn': 'arn:aws:iam::123456789012:user/MyDemoUser',
            'userId': 'AIDAJNUEDQAQWFELJDLEX',
        },
        {
            'environmentId': '12bfc3cd537f41cb9776f8af5525c9EX',
            'lastAccess': datetime(2018, 1, 19, 11, 39, 19, 4, 19, 0),
            'permissions': 'owner',
            'userArn': 'arn:aws:iam::123456789012:user/MyDemoUser',
            'userId': 'AIDAJNUEDQAQWFELJDLEX',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'memberships': [
            {
                'permissions': 'owner'|'read-write'|'read-only',
                'userId': 'string',
                'userArn': 'string',
                'environmentId': 'string',
                'lastAccess': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    owner : Owns the environment.
    read-only : Has read-only access to the environment.
    read-write : Has read-write access to the environment.
    
    """
    pass

def describe_environment_status(environmentId=None):
    """
    Gets status information for an AWS Cloud9 development environment.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.describe_environment_status(
        environmentId='string'
    )
    
    
    :type environmentId: string
    :param environmentId: [REQUIRED]\nThe ID of the environment to get status information about.\n

    :rtype: dict
ReturnsResponse Syntax{
    'status': 'error'|'creating'|'connecting'|'ready'|'stopping'|'stopped'|'deleting',
    'message': 'string'
}


Response Structure

(dict) --
status (string) --The status of the environment. Available values include:

connecting : The environment is connecting.
creating : The environment is being created.
deleting : The environment is being deleted.
error : The environment is in an error state.
ready : The environment is ready.
stopped : The environment is stopped.
stopping : The environment is stopping.


message (string) --Any informational message about the status of the environment.






Exceptions

Cloud9.Client.exceptions.BadRequestException
Cloud9.Client.exceptions.ConflictException
Cloud9.Client.exceptions.NotFoundException
Cloud9.Client.exceptions.ForbiddenException
Cloud9.Client.exceptions.TooManyRequestsException
Cloud9.Client.exceptions.LimitExceededException
Cloud9.Client.exceptions.InternalServerErrorException

Examples
response = client.describe_environment_status(
    environmentId='8d9967e2f0624182b74e7690ad69ebEX',
)

print(response)


Expected Output:
{
    'message': 'Environment is ready to use',
    'status': 'ready',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'status': 'error'|'creating'|'connecting'|'ready'|'stopping'|'stopped'|'deleting',
        'message': 'string'
    }
    
    
    :returns: 
    Cloud9.Client.exceptions.BadRequestException
    Cloud9.Client.exceptions.ConflictException
    Cloud9.Client.exceptions.NotFoundException
    Cloud9.Client.exceptions.ForbiddenException
    Cloud9.Client.exceptions.TooManyRequestsException
    Cloud9.Client.exceptions.LimitExceededException
    Cloud9.Client.exceptions.InternalServerErrorException
    
    """
    pass

def describe_environments(environmentIds=None):
    """
    Gets information about AWS Cloud9 development environments.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.describe_environments(
        environmentIds=[
            'string',
        ]
    )
    
    
    :type environmentIds: list
    :param environmentIds: [REQUIRED]\nThe IDs of individual environments to get information about.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'environments': [
        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'ssh'|'ec2',
            'arn': 'string',
            'ownerArn': 'string',
            'lifecycle': {
                'status': 'CREATING'|'CREATED'|'CREATE_FAILED'|'DELETING'|'DELETE_FAILED',
                'reason': 'string',
                'failureResource': 'string'
            }
        },
    ]
}


Response Structure

(dict) --
environments (list) --Information about the environments that are returned.

(dict) --Information about an AWS Cloud9 development environment.

id (string) --The ID of the environment.

name (string) --The name of the environment.

description (string) --The description for the environment.

type (string) --The type of environment. Valid values include the following:

ec2 : An Amazon Elastic Compute Cloud (Amazon EC2) instance connects to the environment.
ssh : Your own server connects to the environment.


arn (string) --The Amazon Resource Name (ARN) of the environment.

ownerArn (string) --The Amazon Resource Name (ARN) of the environment owner.

lifecycle (dict) --The state of the environment in its creation or deletion lifecycle.

status (string) --The current creation or deletion lifecycle state of the environment.

CREATING : The environment is in the process of being created.
CREATED : The environment was successfully created.
CREATE_FAILED : The environment failed to be created.
DELETING : The environment is in the process of being deleted.
DELETE_FAILED : The environment failed to delete.


reason (string) --Any informational message about the lifecycle state of the environment.

failureResource (string) --If the environment failed to delete, the Amazon Resource Name (ARN) of the related AWS resource.












Exceptions

Cloud9.Client.exceptions.BadRequestException
Cloud9.Client.exceptions.ConflictException
Cloud9.Client.exceptions.NotFoundException
Cloud9.Client.exceptions.ForbiddenException
Cloud9.Client.exceptions.TooManyRequestsException
Cloud9.Client.exceptions.LimitExceededException
Cloud9.Client.exceptions.InternalServerErrorException

Examples
response = client.describe_environments(
    environmentIds=[
        '8d9967e2f0624182b74e7690ad69ebEX',
        '349c86d4579e4e7298d500ff57a6b2EX',
    ],
)

print(response)


Expected Output:
{
    'environments': [
        {
            'name': 'my-demo-environment',
            'type': 'ec2',
            'arn': 'arn:aws:cloud9:us-east-2:123456789012:environment:8d9967e2f0624182b74e7690ad69ebEX',
            'description': 'This is my demonstration environment.',
            'id': '8d9967e2f0624182b74e7690ad69ebEX',
            'ownerArn': 'arn:aws:iam::123456789012:user/MyDemoUser',
        },
        {
            'name': 'another-demo-environment',
            'type': 'ssh',
            'arn': 'arn:aws:cloud9:us-east-2:123456789012:environment:349c86d4579e4e7298d500ff57a6b2EX',
            'id': '349c86d4579e4e7298d500ff57a6b2EX',
            'ownerArn': 'arn:aws:sts::123456789012:assumed-role/AnotherDemoUser/AnotherDemoUser',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'environments': [
            {
                'id': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'ssh'|'ec2',
                'arn': 'string',
                'ownerArn': 'string',
                'lifecycle': {
                    'status': 'CREATING'|'CREATED'|'CREATE_FAILED'|'DELETING'|'DELETE_FAILED',
                    'reason': 'string',
                    'failureResource': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    ec2 : An Amazon Elastic Compute Cloud (Amazon EC2) instance connects to the environment.
    ssh : Your own server connects to the environment.
    
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

def list_environments(nextToken=None, maxResults=None):
    """
    Gets a list of AWS Cloud9 development environment identifiers.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.list_environments(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: During a previous call, if there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a next token . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :type maxResults: integer
    :param maxResults: The maximum number of environments to get identifiers for.

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'environmentIds': [
        'string',
    ]
}


Response Structure

(dict) --

nextToken (string) --
If there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a next token . To get the next batch of items in the list, call this operation again, adding the next token to the call.

environmentIds (list) --
The list of environment identifiers.

(string) --








Exceptions

Cloud9.Client.exceptions.BadRequestException
Cloud9.Client.exceptions.ConflictException
Cloud9.Client.exceptions.NotFoundException
Cloud9.Client.exceptions.ForbiddenException
Cloud9.Client.exceptions.TooManyRequestsException
Cloud9.Client.exceptions.LimitExceededException
Cloud9.Client.exceptions.InternalServerErrorException

Examples
response = client.list_environments(
)

print(response)


Expected Output:
{
    'environmentIds': [
        '349c86d4579e4e7298d500ff57a6b2EX',
        '45a3da47af0840f2b0c0824f5ee232EX',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'nextToken': 'string',
        'environmentIds': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(ResourceARN=None):
    """
    Gets a list of the tags associated with an AWS Cloud9 development environment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceARN='string'
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the AWS Cloud9 development environment to get the tags for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Tags (list) --The list of tags associated with the AWS Cloud9 development environment.

(dict) --Metadata that is associated with AWS resources. In particular, a name-value pair that can be associated with an AWS Cloud9 development environment. There are two types of tags: user tags and system tags . A user tag is created by the user. A system tag is automatically created by AWS services. A system tag is prefixed with "aws:" and cannot be modified by the user.

Key (string) --The name part of a tag.

Value (string) --The value part of a tag.










Exceptions

Cloud9.Client.exceptions.NotFoundException
Cloud9.Client.exceptions.InternalServerErrorException
Cloud9.Client.exceptions.BadRequestException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def tag_resource(ResourceARN=None, Tags=None):
    """
    Adds tags to an AWS Cloud9 development environment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceARN='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the AWS Cloud9 development environment to add tags to.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe list of tags to add to the given AWS Cloud9 development environment.\n\n(dict) --Metadata that is associated with AWS resources. In particular, a name-value pair that can be associated with an AWS Cloud9 development environment. There are two types of tags: user tags and system tags . A user tag is created by the user. A system tag is automatically created by AWS services. A system tag is prefixed with 'aws:' and cannot be modified by the user.\n\nKey (string) -- [REQUIRED]The name part of a tag.\n\nValue (string) -- [REQUIRED]The value part of a tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Cloud9.Client.exceptions.NotFoundException
Cloud9.Client.exceptions.InternalServerErrorException
Cloud9.Client.exceptions.BadRequestException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceARN=None, TagKeys=None):
    """
    Removes tags from an AWS Cloud9 development environment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the AWS Cloud9 development environment to remove tags from.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag names of the tags to remove from the given AWS Cloud9 development environment.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Cloud9.Client.exceptions.NotFoundException
Cloud9.Client.exceptions.InternalServerErrorException
Cloud9.Client.exceptions.BadRequestException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_environment(environmentId=None, name=None, description=None):
    """
    Changes the settings of an existing AWS Cloud9 development environment.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.update_environment(
        environmentId='string',
        name='string',
        description='string'
    )
    
    
    :type environmentId: string
    :param environmentId: [REQUIRED]\nThe ID of the environment to change settings.\n

    :type name: string
    :param name: A replacement name for the environment.

    :type description: string
    :param description: Any new or replacement description for the environment.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Cloud9.Client.exceptions.BadRequestException
Cloud9.Client.exceptions.ConflictException
Cloud9.Client.exceptions.NotFoundException
Cloud9.Client.exceptions.ForbiddenException
Cloud9.Client.exceptions.TooManyRequestsException
Cloud9.Client.exceptions.LimitExceededException
Cloud9.Client.exceptions.InternalServerErrorException

Examples
response = client.update_environment(
    name='my-changed-demo-environment',
    description='This is my changed demonstration environment.',
    environmentId='8d9967e2f0624182b74e7690ad69ebEX',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_environment_membership(environmentId=None, userArn=None, permissions=None):
    """
    Changes the settings of an existing environment member for an AWS Cloud9 development environment.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.update_environment_membership(
        environmentId='string',
        userArn='string',
        permissions='read-write'|'read-only'
    )
    
    
    :type environmentId: string
    :param environmentId: [REQUIRED]\nThe ID of the environment for the environment member whose settings you want to change.\n

    :type userArn: string
    :param userArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the environment member whose settings you want to change.\n

    :type permissions: string
    :param permissions: [REQUIRED]\nThe replacement type of environment member permissions you want to associate with this environment member. Available values include:\n\nread-only : Has read-only access to the environment.\nread-write : Has read-write access to the environment.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'membership': {
        'permissions': 'owner'|'read-write'|'read-only',
        'userId': 'string',
        'userArn': 'string',
        'environmentId': 'string',
        'lastAccess': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

membership (dict) --
Information about the environment member whose settings were changed.

permissions (string) --
The type of environment member permissions associated with this environment member. Available values include:

owner : Owns the environment.
read-only : Has read-only access to the environment.
read-write : Has read-write access to the environment.


userId (string) --
The user ID in AWS Identity and Access Management (AWS IAM) of the environment member.

userArn (string) --
The Amazon Resource Name (ARN) of the environment member.

environmentId (string) --
The ID of the environment for the environment member.

lastAccess (datetime) --
The time, expressed in epoch time format, when the environment member last opened the environment.









Exceptions

Cloud9.Client.exceptions.BadRequestException
Cloud9.Client.exceptions.ConflictException
Cloud9.Client.exceptions.NotFoundException
Cloud9.Client.exceptions.ForbiddenException
Cloud9.Client.exceptions.TooManyRequestsException
Cloud9.Client.exceptions.LimitExceededException
Cloud9.Client.exceptions.InternalServerErrorException

Examples
response = client.update_environment_membership(
    environmentId='8d9967e2f0624182b74e7690ad69ebEX',
    permissions='read-only',
    userArn='arn:aws:iam::123456789012:user/AnotherDemoUser',
)

print(response)


Expected Output:
{
    'membership': {
        'environmentId': '8d9967e2f0624182b74e7690ad69eb31',
        'permissions': 'read-only',
        'userArn': 'arn:aws:iam::123456789012:user/AnotherDemoUser',
        'userId': 'AIDAJ3BA6O2FMJWCWXHEX',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'membership': {
            'permissions': 'owner'|'read-write'|'read-only',
            'userId': 'string',
            'userArn': 'string',
            'environmentId': 'string',
            'lastAccess': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    owner : Owns the environment.
    read-only : Has read-only access to the environment.
    read-write : Has read-write access to the environment.
    
    """
    pass

