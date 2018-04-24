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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    """
    pass

def create_environment_ec2(name=None, description=None, clientRequestToken=None, instanceType=None, subnetId=None, automaticStopTimeMinutes=None, ownerArn=None):
    """
    Creates an AWS Cloud9 development environment, launches an Amazon Elastic Compute Cloud (Amazon EC2) instance, and then connects from the instance to the environment.
    See also: AWS API Documentation
    
    
    :example: response = client.create_environment_ec2(
        name='string',
        description='string',
        clientRequestToken='string',
        instanceType='string',
        subnetId='string',
        automaticStopTimeMinutes=123,
        ownerArn='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the environment to create.
            This name is visible to other AWS IAM users in the same AWS account.
            

    :type description: string
    :param description: The description of the environment to create.

    :type clientRequestToken: string
    :param clientRequestToken: A unique, case-sensitive string that helps AWS Cloud9 to ensure this operation completes no more than one time.
            For more information, see Client Tokens in the Amazon EC2 API Reference .
            

    :type instanceType: string
    :param instanceType: [REQUIRED]
            The type of instance to connect to the environment (for example, t2.micro ).
            

    :type subnetId: string
    :param subnetId: The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.

    :type automaticStopTimeMinutes: integer
    :param automaticStopTimeMinutes: The number of minutes until the running instance is shut down after the environment has last been used.

    :type ownerArn: string
    :param ownerArn: The Amazon Resource Name (ARN) of the environment owner. This ARN can be the ARN of any AWS IAM principal. If this value is not specified, the ARN defaults to this environment's creator.

    :rtype: dict
    :return: {
        'environmentId': 'string'
    }
    
    
    """
    pass

def create_environment_membership(environmentId=None, userArn=None, permissions=None):
    """
    Adds an environment member to an AWS Cloud9 development environment.
    See also: AWS API Documentation
    
    
    :example: response = client.create_environment_membership(
        environmentId='string',
        userArn='string',
        permissions='read-write'|'read-only'
    )
    
    
    :type environmentId: string
    :param environmentId: [REQUIRED]
            The ID of the environment that contains the environment member you want to add.
            

    :type userArn: string
    :param userArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the environment member you want to add.
            

    :type permissions: string
    :param permissions: [REQUIRED]
            The type of environment member permissions you want to associate with this environment member. Available values include:
            read-only : Has read-only access to the environment.
            read-write : Has read-write access to the environment.
            

    :rtype: dict
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
    
    
    :example: response = client.delete_environment(
        environmentId='string'
    )
    
    
    :type environmentId: string
    :param environmentId: [REQUIRED]
            The ID of the environment to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_environment_membership(environmentId=None, userArn=None):
    """
    Deletes an environment member from an AWS Cloud9 development environment.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_environment_membership(
        environmentId='string',
        userArn='string'
    )
    
    
    :type environmentId: string
    :param environmentId: [REQUIRED]
            The ID of the environment to delete the environment member from.
            

    :type userArn: string
    :param userArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the environment member to delete from the environment.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_environment_memberships(userArn=None, environmentId=None, permissions=None, nextToken=None, maxResults=None):
    """
    Gets information about environment members for an AWS Cloud9 development environment.
    See also: AWS API Documentation
    
    
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
    :param permissions: The type of environment member permissions to get information about. Available values include:
            owner : Owns the environment.
            read-only : Has read-only access to the environment.
            read-write : Has read-write access to the environment.
            If no value is specified, information about all environment members are returned.
            (string) --
            

    :type nextToken: string
    :param nextToken: During a previous call, if there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a next token . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :type maxResults: integer
    :param maxResults: The maximum number of environment members to get information about.

    :rtype: dict
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
    
    
    :example: response = client.describe_environment_status(
        environmentId='string'
    )
    
    
    :type environmentId: string
    :param environmentId: [REQUIRED]
            The ID of the environment to get status information about.
            

    :rtype: dict
    :return: {
        'status': 'error'|'creating'|'connecting'|'ready'|'stopping'|'stopped'|'deleting',
        'message': 'string'
    }
    
    
    """
    pass

def describe_environments(environmentIds=None):
    """
    Gets information about AWS Cloud9 development environments.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_environments(
        environmentIds=[
            'string',
        ]
    )
    
    
    :type environmentIds: list
    :param environmentIds: [REQUIRED]
            The IDs of individual environments to get information about.
            (string) --
            

    :rtype: dict
    :return: {
        'environments': [
            {
                'id': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'ssh'|'ec2',
                'arn': 'string',
                'ownerArn': 'string'
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

def list_environments(nextToken=None, maxResults=None):
    """
    Gets a list of AWS Cloud9 development environment identifiers.
    See also: AWS API Documentation
    
    
    :example: response = client.list_environments(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: During a previous call, if there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a next token . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :type maxResults: integer
    :param maxResults: The maximum number of environments to get identifiers for.

    :rtype: dict
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

def update_environment(environmentId=None, name=None, description=None):
    """
    Changes the settings of an existing AWS Cloud9 development environment.
    See also: AWS API Documentation
    
    
    :example: response = client.update_environment(
        environmentId='string',
        name='string',
        description='string'
    )
    
    
    :type environmentId: string
    :param environmentId: [REQUIRED]
            The ID of the environment to change settings.
            

    :type name: string
    :param name: A replacement name for the environment.

    :type description: string
    :param description: Any new or replacement description for the environment.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_environment_membership(environmentId=None, userArn=None, permissions=None):
    """
    Changes the settings of an existing environment member for an AWS Cloud9 development environment.
    See also: AWS API Documentation
    
    
    :example: response = client.update_environment_membership(
        environmentId='string',
        userArn='string',
        permissions='read-write'|'read-only'
    )
    
    
    :type environmentId: string
    :param environmentId: [REQUIRED]
            The ID of the environment for the environment member whose settings you want to change.
            

    :type userArn: string
    :param userArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the environment member whose settings you want to change.
            

    :type permissions: string
    :param permissions: [REQUIRED]
            The replacement type of environment member permissions you want to associate with this environment member. Available values include:
            read-only : Has read-only access to the environment.
            read-write : Has read-write access to the environment.
            

    :rtype: dict
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

