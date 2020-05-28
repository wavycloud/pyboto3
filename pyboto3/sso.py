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

def get_role_credentials(roleName=None, accountId=None, accessToken=None):
    """
    Returns the STS short-term credentials for a given role name that is assigned to the user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_role_credentials(
        roleName='string',
        accountId='string',
        accessToken='string'
    )
    
    
    :type roleName: string
    :param roleName: [REQUIRED]\nThe friendly name of the role that is assigned to the user.\n

    :type accountId: string
    :param accountId: [REQUIRED]\nThe identifier for the AWS account that is assigned to the user.\n

    :type accessToken: string
    :param accessToken: [REQUIRED]\nThe token issued by the CreateToken API call. For more information, see CreateToken in the AWS SSO OIDC API Reference Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'roleCredentials': {
        'accessKeyId': 'string',
        'secretAccessKey': 'string',
        'sessionToken': 'string',
        'expiration': 123
    }
}


Response Structure

(dict) --

roleCredentials (dict) --
The credentials for the role that is assigned to the user.

accessKeyId (string) --
The identifier used for the temporary security credentials. For more information, see Using Temporary Security Credentials to Request Access to AWS Resources in the AWS IAM User Guide .

secretAccessKey (string) --
The key that is used to sign the request. For more information, see Using Temporary Security Credentials to Request Access to AWS Resources in the AWS IAM User Guide .

sessionToken (string) --
The token used for temporary credentials. For more information, see Using Temporary Security Credentials to Request Access to AWS Resources in the AWS IAM User Guide .

expiration (integer) --
The date on which temporary security credentials expire.









Exceptions

SSO.Client.exceptions.InvalidRequestException
SSO.Client.exceptions.UnauthorizedException
SSO.Client.exceptions.TooManyRequestsException
SSO.Client.exceptions.ResourceNotFoundException


    :return: {
        'roleCredentials': {
            'accessKeyId': 'string',
            'secretAccessKey': 'string',
            'sessionToken': 'string',
            'expiration': 123
        }
    }
    
    
    :returns: 
    SSO.Client.exceptions.InvalidRequestException
    SSO.Client.exceptions.UnauthorizedException
    SSO.Client.exceptions.TooManyRequestsException
    SSO.Client.exceptions.ResourceNotFoundException
    
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

def list_account_roles(nextToken=None, maxResults=None, accessToken=None, accountId=None):
    """
    Lists all roles that are assigned to the user for a given AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_account_roles(
        nextToken='string',
        maxResults=123,
        accessToken='string',
        accountId='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The page token from the previous response output when you request subsequent pages.

    :type maxResults: integer
    :param maxResults: The number of items that clients can request per page.

    :type accessToken: string
    :param accessToken: [REQUIRED]\nThe token issued by the CreateToken API call. For more information, see CreateToken in the AWS SSO OIDC API Reference Guide .\n

    :type accountId: string
    :param accountId: [REQUIRED]\nThe identifier for the AWS account that is assigned to the user.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'roleList': [
        {
            'roleName': 'string',
            'accountId': 'string'
        },
    ]
}


Response Structure

(dict) --

nextToken (string) --
The page token client that is used to retrieve the list of accounts.

roleList (list) --
A paginated response with the list of roles and the next token if more results are available.

(dict) --
Provides information about the role that is assigned to the user.

roleName (string) --
The friendly name of the role that is assigned to the user.

accountId (string) --
The identifier of the AWS account assigned to the user.











Exceptions

SSO.Client.exceptions.InvalidRequestException
SSO.Client.exceptions.UnauthorizedException
SSO.Client.exceptions.TooManyRequestsException
SSO.Client.exceptions.ResourceNotFoundException


    :return: {
        'nextToken': 'string',
        'roleList': [
            {
                'roleName': 'string',
                'accountId': 'string'
            },
        ]
    }
    
    
    :returns: 
    SSO.Client.exceptions.InvalidRequestException
    SSO.Client.exceptions.UnauthorizedException
    SSO.Client.exceptions.TooManyRequestsException
    SSO.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_accounts(nextToken=None, maxResults=None, accessToken=None):
    """
    Lists all AWS accounts assigned to the user. These AWS accounts are assigned by the administrator of the account. For more information, see Assign User Access in the AWS SSO User Guide . This operation returns a paginated response.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_accounts(
        nextToken='string',
        maxResults=123,
        accessToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: (Optional) When requesting subsequent pages, this is the page token from the previous response output.

    :type maxResults: integer
    :param maxResults: This is the number of items clients can request per page.

    :type accessToken: string
    :param accessToken: [REQUIRED]\nThe token issued by the CreateToken API call. For more information, see CreateToken in the AWS SSO OIDC API Reference Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'accountList': [
        {
            'accountId': 'string',
            'accountName': 'string',
            'emailAddress': 'string'
        },
    ]
}


Response Structure

(dict) --

nextToken (string) --
The page token client that is used to retrieve the list of accounts.

accountList (list) --
A paginated response with the list of account information and the next token if more results are available.

(dict) --
Provides information about your AWS account.

accountId (string) --
The identifier of the AWS account that is assigned to the user.

accountName (string) --
The display name of the AWS account that is assigned to the user.

emailAddress (string) --
The email address of the AWS account that is assigned to the user.











Exceptions

SSO.Client.exceptions.InvalidRequestException
SSO.Client.exceptions.UnauthorizedException
SSO.Client.exceptions.TooManyRequestsException
SSO.Client.exceptions.ResourceNotFoundException


    :return: {
        'nextToken': 'string',
        'accountList': [
            {
                'accountId': 'string',
                'accountName': 'string',
                'emailAddress': 'string'
            },
        ]
    }
    
    
    :returns: 
    SSO.Client.exceptions.InvalidRequestException
    SSO.Client.exceptions.UnauthorizedException
    SSO.Client.exceptions.TooManyRequestsException
    SSO.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def logout(accessToken=None):
    """
    Removes the client- and server-side session that is associated with the user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.logout(
        accessToken='string'
    )
    
    
    :type accessToken: string
    :param accessToken: [REQUIRED]\nThe token issued by the CreateToken API call. For more information, see CreateToken in the AWS SSO OIDC API Reference Guide .\n

    """
    pass

