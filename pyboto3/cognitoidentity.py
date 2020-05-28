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

def create_identity_pool(IdentityPoolName=None, AllowUnauthenticatedIdentities=None, AllowClassicFlow=None, SupportedLoginProviders=None, DeveloperProviderName=None, OpenIdConnectProviderARNs=None, CognitoIdentityProviders=None, SamlProviderARNs=None, IdentityPoolTags=None):
    """
    Creates a new identity pool. The identity pool is a store of user identity information that is specific to your AWS account. The keys for SupportedLoginProviders are as follows:
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_identity_pool(
        IdentityPoolName='string',
        AllowUnauthenticatedIdentities=True|False,
        AllowClassicFlow=True|False,
        SupportedLoginProviders={
            'string': 'string'
        },
        DeveloperProviderName='string',
        OpenIdConnectProviderARNs=[
            'string',
        ],
        CognitoIdentityProviders=[
            {
                'ProviderName': 'string',
                'ClientId': 'string',
                'ServerSideTokenCheck': True|False
            },
        ],
        SamlProviderARNs=[
            'string',
        ],
        IdentityPoolTags={
            'string': 'string'
        }
    )
    
    
    :type IdentityPoolName: string
    :param IdentityPoolName: [REQUIRED]\nA string that you provide.\n

    :type AllowUnauthenticatedIdentities: boolean
    :param AllowUnauthenticatedIdentities: [REQUIRED]\nTRUE if the identity pool supports unauthenticated logins.\n

    :type AllowClassicFlow: boolean
    :param AllowClassicFlow: Enables or disables the Basic (Classic) authentication flow. For more information, see Identity Pools (Federated Identities) Authentication Flow in the Amazon Cognito Developer Guide .

    :type SupportedLoginProviders: dict
    :param SupportedLoginProviders: Optional key:value pairs mapping provider names to provider app IDs.\n\n(string) --\n(string) --\n\n\n\n

    :type DeveloperProviderName: string
    :param DeveloperProviderName: The 'domain' by which Cognito will refer to your users. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the DeveloperProviderName , you can use letters as well as period (. ), underscore (_ ), and dash (- ).\nOnce you have set a developer provider name, you cannot change it. Please take care in setting this parameter.\n

    :type OpenIdConnectProviderARNs: list
    :param OpenIdConnectProviderARNs: A list of OpendID Connect provider ARNs.\n\n(string) --\n\n

    :type CognitoIdentityProviders: list
    :param CognitoIdentityProviders: An array of Amazon Cognito user pools and their client IDs.\n\n(dict) --A provider representing an Amazon Cognito user pool and its client ID.\n\nProviderName (string) --The provider name for an Amazon Cognito user pool. For example, cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789 .\n\nClientId (string) --The client ID for the Amazon Cognito user pool.\n\nServerSideTokenCheck (boolean) --TRUE if server-side token validation is enabled for the identity provider\xe2\x80\x99s token.\nOnce you set ServerSideTokenCheck to TRUE for an identity pool, that identity pool will check with the integrated user pools to make sure that the user has not been globally signed out or deleted before the identity pool provides an OIDC token or AWS credentials for the user.\nIf the user is signed out or deleted, the identity pool will return a 400 Not Authorized error.\n\n\n\n\n

    :type SamlProviderARNs: list
    :param SamlProviderARNs: An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.\n\n(string) --\n\n

    :type IdentityPoolTags: dict
    :param IdentityPoolTags: Tags to assign to the identity pool. A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityPoolId': 'string',
    'IdentityPoolName': 'string',
    'AllowUnauthenticatedIdentities': True|False,
    'AllowClassicFlow': True|False,
    'SupportedLoginProviders': {
        'string': 'string'
    },
    'DeveloperProviderName': 'string',
    'OpenIdConnectProviderARNs': [
        'string',
    ],
    'CognitoIdentityProviders': [
        {
            'ProviderName': 'string',
            'ClientId': 'string',
            'ServerSideTokenCheck': True|False
        },
    ],
    'SamlProviderARNs': [
        'string',
    ],
    'IdentityPoolTags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
An object representing an Amazon Cognito identity pool.

IdentityPoolId (string) --
An identity pool ID in the format REGION:GUID.

IdentityPoolName (string) --
A string that you provide.

AllowUnauthenticatedIdentities (boolean) --
TRUE if the identity pool supports unauthenticated logins.

AllowClassicFlow (boolean) --
Enables or disables the Basic (Classic) authentication flow. For more information, see Identity Pools (Federated Identities) Authentication Flow in the Amazon Cognito Developer Guide .

SupportedLoginProviders (dict) --
Optional key:value pairs mapping provider names to provider app IDs.

(string) --
(string) --




DeveloperProviderName (string) --
The "domain" by which Cognito will refer to your users.

OpenIdConnectProviderARNs (list) --
A list of OpendID Connect provider ARNs.

(string) --


CognitoIdentityProviders (list) --
A list representing an Amazon Cognito user pool and its client ID.

(dict) --
A provider representing an Amazon Cognito user pool and its client ID.

ProviderName (string) --
The provider name for an Amazon Cognito user pool. For example, cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789 .

ClientId (string) --
The client ID for the Amazon Cognito user pool.

ServerSideTokenCheck (boolean) --
TRUE if server-side token validation is enabled for the identity provider\xe2\x80\x99s token.
Once you set ServerSideTokenCheck to TRUE for an identity pool, that identity pool will check with the integrated user pools to make sure that the user has not been globally signed out or deleted before the identity pool provides an OIDC token or AWS credentials for the user.
If the user is signed out or deleted, the identity pool will return a 400 Not Authorized error.





SamlProviderARNs (list) --
An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.

(string) --


IdentityPoolTags (dict) --
The tags that are assigned to the identity pool. A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.

(string) --
(string) --










Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.ResourceConflictException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException
CognitoIdentity.Client.exceptions.LimitExceededException


    :return: {
        'IdentityPoolId': 'string',
        'IdentityPoolName': 'string',
        'AllowUnauthenticatedIdentities': True|False,
        'AllowClassicFlow': True|False,
        'SupportedLoginProviders': {
            'string': 'string'
        },
        'DeveloperProviderName': 'string',
        'OpenIdConnectProviderARNs': [
            'string',
        ],
        'CognitoIdentityProviders': [
            {
                'ProviderName': 'string',
                'ClientId': 'string',
                'ServerSideTokenCheck': True|False
            },
        ],
        'SamlProviderARNs': [
            'string',
        ],
        'IdentityPoolTags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    IdentityPoolName (string) -- [REQUIRED]
    A string that you provide.
    
    AllowUnauthenticatedIdentities (boolean) -- [REQUIRED]
    TRUE if the identity pool supports unauthenticated logins.
    
    AllowClassicFlow (boolean) -- Enables or disables the Basic (Classic) authentication flow. For more information, see Identity Pools (Federated Identities) Authentication Flow in the Amazon Cognito Developer Guide .
    SupportedLoginProviders (dict) -- Optional key:value pairs mapping provider names to provider app IDs.
    
    (string) --
    (string) --
    
    
    
    
    DeveloperProviderName (string) -- The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the DeveloperProviderName , you can use letters as well as period (. ), underscore (_ ), and dash (- ).
    Once you have set a developer provider name, you cannot change it. Please take care in setting this parameter.
    
    OpenIdConnectProviderARNs (list) -- A list of OpendID Connect provider ARNs.
    
    (string) --
    
    
    CognitoIdentityProviders (list) -- An array of Amazon Cognito user pools and their client IDs.
    
    (dict) --A provider representing an Amazon Cognito user pool and its client ID.
    
    ProviderName (string) --The provider name for an Amazon Cognito user pool. For example, cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789 .
    
    ClientId (string) --The client ID for the Amazon Cognito user pool.
    
    ServerSideTokenCheck (boolean) --TRUE if server-side token validation is enabled for the identity provider\xe2\x80\x99s token.
    Once you set ServerSideTokenCheck to TRUE for an identity pool, that identity pool will check with the integrated user pools to make sure that the user has not been globally signed out or deleted before the identity pool provides an OIDC token or AWS credentials for the user.
    If the user is signed out or deleted, the identity pool will return a 400 Not Authorized error.
    
    
    
    
    
    SamlProviderARNs (list) -- An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.
    
    (string) --
    
    
    IdentityPoolTags (dict) -- Tags to assign to the identity pool. A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.
    
    (string) --
    (string) --
    
    
    
    
    
    """
    pass

def delete_identities(IdentityIdsToDelete=None):
    """
    Deletes identities from an identity pool. You can specify a list of 1-60 identities that you want to delete.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_identities(
        IdentityIdsToDelete=[
            'string',
        ]
    )
    
    
    :type IdentityIdsToDelete: list
    :param IdentityIdsToDelete: [REQUIRED]\nA list of 1-60 identities that you want to delete.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'UnprocessedIdentityIds': [
        {
            'IdentityId': 'string',
            'ErrorCode': 'AccessDenied'|'InternalServerError'
        },
    ]
}


Response Structure

(dict) --Returned in response to a successful DeleteIdentities operation.

UnprocessedIdentityIds (list) --An array of UnprocessedIdentityId objects, each of which contains an ErrorCode and IdentityId.

(dict) --An array of UnprocessedIdentityId objects, each of which contains an ErrorCode and IdentityId.

IdentityId (string) --A unique identifier in the format REGION:GUID.

ErrorCode (string) --The error code indicating the type of error that occurred.










Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException


    :return: {
        'UnprocessedIdentityIds': [
            {
                'IdentityId': 'string',
                'ErrorCode': 'AccessDenied'|'InternalServerError'
            },
        ]
    }
    
    
    :returns: 
    CognitoIdentity.Client.exceptions.InvalidParameterException
    CognitoIdentity.Client.exceptions.TooManyRequestsException
    CognitoIdentity.Client.exceptions.InternalErrorException
    
    """
    pass

def delete_identity_pool(IdentityPoolId=None):
    """
    Deletes an identity pool. Once a pool is deleted, users will not be able to authenticate with the pool.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_identity_pool(
        IdentityPoolId='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nAn identity pool ID in the format REGION:GUID.\n

    """
    pass

def describe_identity(IdentityId=None):
    """
    Returns metadata related to the given identity, including when the identity was created and any associated linked logins.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_identity(
        IdentityId='string'
    )
    
    
    :type IdentityId: string
    :param IdentityId: [REQUIRED]\nA unique identifier in the format REGION:GUID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'IdentityId': 'string',
    'Logins': [
        'string',
    ],
    'CreationDate': datetime(2015, 1, 1),
    'LastModifiedDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --A description of the identity.

IdentityId (string) --A unique identifier in the format REGION:GUID.

Logins (list) --The provider names.

(string) --


CreationDate (datetime) --Date on which the identity was created.

LastModifiedDate (datetime) --Date on which the identity was last modified.






Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException


    :return: {
        'IdentityId': 'string',
        'Logins': [
            'string',
        ],
        'CreationDate': datetime(2015, 1, 1),
        'LastModifiedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    CognitoIdentity.Client.exceptions.InvalidParameterException
    CognitoIdentity.Client.exceptions.ResourceNotFoundException
    CognitoIdentity.Client.exceptions.NotAuthorizedException
    CognitoIdentity.Client.exceptions.TooManyRequestsException
    CognitoIdentity.Client.exceptions.InternalErrorException
    
    """
    pass

def describe_identity_pool(IdentityPoolId=None):
    """
    Gets details about a particular identity pool, including the pool name, ID description, creation date, and current number of users.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_identity_pool(
        IdentityPoolId='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nAn identity pool ID in the format REGION:GUID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'IdentityPoolId': 'string',
    'IdentityPoolName': 'string',
    'AllowUnauthenticatedIdentities': True|False,
    'AllowClassicFlow': True|False,
    'SupportedLoginProviders': {
        'string': 'string'
    },
    'DeveloperProviderName': 'string',
    'OpenIdConnectProviderARNs': [
        'string',
    ],
    'CognitoIdentityProviders': [
        {
            'ProviderName': 'string',
            'ClientId': 'string',
            'ServerSideTokenCheck': True|False
        },
    ],
    'SamlProviderARNs': [
        'string',
    ],
    'IdentityPoolTags': {
        'string': 'string'
    }
}


Response Structure

(dict) --An object representing an Amazon Cognito identity pool.

IdentityPoolId (string) --An identity pool ID in the format REGION:GUID.

IdentityPoolName (string) --A string that you provide.

AllowUnauthenticatedIdentities (boolean) --TRUE if the identity pool supports unauthenticated logins.

AllowClassicFlow (boolean) --Enables or disables the Basic (Classic) authentication flow. For more information, see Identity Pools (Federated Identities) Authentication Flow in the Amazon Cognito Developer Guide .

SupportedLoginProviders (dict) --Optional key:value pairs mapping provider names to provider app IDs.

(string) --
(string) --




DeveloperProviderName (string) --The "domain" by which Cognito will refer to your users.

OpenIdConnectProviderARNs (list) --A list of OpendID Connect provider ARNs.

(string) --


CognitoIdentityProviders (list) --A list representing an Amazon Cognito user pool and its client ID.

(dict) --A provider representing an Amazon Cognito user pool and its client ID.

ProviderName (string) --The provider name for an Amazon Cognito user pool. For example, cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789 .

ClientId (string) --The client ID for the Amazon Cognito user pool.

ServerSideTokenCheck (boolean) --TRUE if server-side token validation is enabled for the identity provider\xe2\x80\x99s token.
Once you set ServerSideTokenCheck to TRUE for an identity pool, that identity pool will check with the integrated user pools to make sure that the user has not been globally signed out or deleted before the identity pool provides an OIDC token or AWS credentials for the user.
If the user is signed out or deleted, the identity pool will return a 400 Not Authorized error.





SamlProviderARNs (list) --An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.

(string) --


IdentityPoolTags (dict) --The tags that are assigned to the identity pool. A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.

(string) --
(string) --









Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException


    :return: {
        'IdentityPoolId': 'string',
        'IdentityPoolName': 'string',
        'AllowUnauthenticatedIdentities': True|False,
        'AllowClassicFlow': True|False,
        'SupportedLoginProviders': {
            'string': 'string'
        },
        'DeveloperProviderName': 'string',
        'OpenIdConnectProviderARNs': [
            'string',
        ],
        'CognitoIdentityProviders': [
            {
                'ProviderName': 'string',
                'ClientId': 'string',
                'ServerSideTokenCheck': True|False
            },
        ],
        'SamlProviderARNs': [
            'string',
        ],
        'IdentityPoolTags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
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

def get_credentials_for_identity(IdentityId=None, Logins=None, CustomRoleArn=None):
    """
    Returns credentials for the provided identity ID. Any provided logins will be validated against supported login providers. If the token is for cognito-identity.amazonaws.com, it will be passed through to AWS Security Token Service with the appropriate role for the token.
    This is a public API. You do not need any credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_credentials_for_identity(
        IdentityId='string',
        Logins={
            'string': 'string'
        },
        CustomRoleArn='string'
    )
    
    
    :type IdentityId: string
    :param IdentityId: [REQUIRED]\nA unique identifier in the format REGION:GUID.\n

    :type Logins: dict
    :param Logins: A set of optional name-value pairs that map provider names to provider tokens. The name-value pair will follow the syntax 'provider_name': 'provider_user_identifier'.\nLogins should not be specified when trying to get credentials for an unauthenticated identity.\nThe Logins parameter is required when using identities associated with external identity providers such as FaceBook. For examples of Logins maps, see the code examples in the External Identity Providers section of the Amazon Cognito Developer Guide.\n\n(string) --\n(string) --\n\n\n\n

    :type CustomRoleArn: string
    :param CustomRoleArn: The Amazon Resource Name (ARN) of the role to be assumed when multiple roles were received in the token from the identity provider. For example, a SAML-based identity provider. This parameter is optional for identity providers that do not support role customization.

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityId': 'string',
    'Credentials': {
        'AccessKeyId': 'string',
        'SecretKey': 'string',
        'SessionToken': 'string',
        'Expiration': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Returned in response to a successful GetCredentialsForIdentity operation.

IdentityId (string) --
A unique identifier in the format REGION:GUID.

Credentials (dict) --
Credentials for the provided identity ID.

AccessKeyId (string) --
The Access Key portion of the credentials.

SecretKey (string) --
The Secret Access Key portion of the credentials

SessionToken (string) --
The Session Token portion of the credentials

Expiration (datetime) --
The date at which these credentials will expire.









Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.ResourceConflictException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InvalidIdentityPoolConfigurationException
CognitoIdentity.Client.exceptions.InternalErrorException
CognitoIdentity.Client.exceptions.ExternalServiceException


    :return: {
        'IdentityId': 'string',
        'Credentials': {
            'AccessKeyId': 'string',
            'SecretKey': 'string',
            'SessionToken': 'string',
            'Expiration': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CognitoIdentity.Client.exceptions.InvalidParameterException
    CognitoIdentity.Client.exceptions.ResourceNotFoundException
    CognitoIdentity.Client.exceptions.NotAuthorizedException
    CognitoIdentity.Client.exceptions.ResourceConflictException
    CognitoIdentity.Client.exceptions.TooManyRequestsException
    CognitoIdentity.Client.exceptions.InvalidIdentityPoolConfigurationException
    CognitoIdentity.Client.exceptions.InternalErrorException
    CognitoIdentity.Client.exceptions.ExternalServiceException
    
    """
    pass

def get_id(AccountId=None, IdentityPoolId=None, Logins=None):
    """
    Generates (or retrieves) a Cognito ID. Supplying multiple logins will create an implicit linked account.
    This is a public API. You do not need any credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_id(
        AccountId='string',
        IdentityPoolId='string',
        Logins={
            'string': 'string'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: A standard AWS account ID (9+ digits).

    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nAn identity pool ID in the format REGION:GUID.\n

    :type Logins: dict
    :param Logins: A set of optional name-value pairs that map provider names to provider tokens. The available provider names for Logins are as follows:\n\nFacebook: graph.facebook.com\nAmazon Cognito user pool: cognito-idp.<region>.amazonaws.com/<YOUR_USER_POOL_ID> , for example, cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789 .\nGoogle: accounts.google.com\nAmazon: www.amazon.com\nTwitter: api.twitter.com\nDigits: www.digits.com\n\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityId': 'string'
}


Response Structure

(dict) --
Returned in response to a GetId request.

IdentityId (string) --
A unique identifier in the format REGION:GUID.







Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.ResourceConflictException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException
CognitoIdentity.Client.exceptions.LimitExceededException
CognitoIdentity.Client.exceptions.ExternalServiceException


    :return: {
        'IdentityId': 'string'
    }
    
    
    :returns: 
    CognitoIdentity.Client.exceptions.InvalidParameterException
    CognitoIdentity.Client.exceptions.ResourceNotFoundException
    CognitoIdentity.Client.exceptions.NotAuthorizedException
    CognitoIdentity.Client.exceptions.ResourceConflictException
    CognitoIdentity.Client.exceptions.TooManyRequestsException
    CognitoIdentity.Client.exceptions.InternalErrorException
    CognitoIdentity.Client.exceptions.LimitExceededException
    CognitoIdentity.Client.exceptions.ExternalServiceException
    
    """
    pass

def get_identity_pool_roles(IdentityPoolId=None):
    """
    Gets the roles for an identity pool.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_identity_pool_roles(
        IdentityPoolId='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nAn identity pool ID in the format REGION:GUID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'IdentityPoolId': 'string',
    'Roles': {
        'string': 'string'
    },
    'RoleMappings': {
        'string': {
            'Type': 'Token'|'Rules',
            'AmbiguousRoleResolution': 'AuthenticatedRole'|'Deny',
            'RulesConfiguration': {
                'Rules': [
                    {
                        'Claim': 'string',
                        'MatchType': 'Equals'|'Contains'|'StartsWith'|'NotEqual',
                        'Value': 'string',
                        'RoleARN': 'string'
                    },
                ]
            }
        }
    }
}


Response Structure

(dict) --Returned in response to a successful GetIdentityPoolRoles operation.

IdentityPoolId (string) --An identity pool ID in the format REGION:GUID.

Roles (dict) --The map of roles associated with this pool. Currently only authenticated and unauthenticated roles are supported.

(string) --
(string) --




RoleMappings (dict) --How users for a specific identity provider are to mapped to roles. This is a String-to- RoleMapping object map. The string identifies the identity provider, for example, "graph.facebook.com" or "cognito-idp.us-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id".

(string) --
(dict) --A role mapping.

Type (string) --The role mapping type. Token will use cognito:roles and cognito:preferred_role claims from the Cognito identity provider token to map groups to roles. Rules will attempt to match claims from the token to map to a role.

AmbiguousRoleResolution (string) --If you specify Token or Rules as the Type , AmbiguousRoleResolution is required.
Specifies the action to be taken if either no rules match the claim value for the Rules type, or there is no cognito:preferred_role claim and there are multiple cognito:roles matches for the Token type.

RulesConfiguration (dict) --The rules to be used for mapping users to roles.
If you specify Rules as the role mapping type, RulesConfiguration is required.

Rules (list) --An array of rules. You can specify up to 25 rules per identity provider.
Rules are evaluated in order. The first one to match specifies the role.

(dict) --A rule that maps a claim name, a claim value, and a match type to a role ARN.

Claim (string) --The claim name that must be present in the token, for example, "isAdmin" or "paid".

MatchType (string) --The match condition that specifies how closely the claim value in the IdP token must match Value .

Value (string) --A brief string that the claim must match, for example, "paid" or "yes".

RoleARN (string) --The role ARN.


















Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.ResourceConflictException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException


    :return: {
        'IdentityPoolId': 'string',
        'Roles': {
            'string': 'string'
        },
        'RoleMappings': {
            'string': {
                'Type': 'Token'|'Rules',
                'AmbiguousRoleResolution': 'AuthenticatedRole'|'Deny',
                'RulesConfiguration': {
                    'Rules': [
                        {
                            'Claim': 'string',
                            'MatchType': 'Equals'|'Contains'|'StartsWith'|'NotEqual',
                            'Value': 'string',
                            'RoleARN': 'string'
                        },
                    ]
                }
            }
        }
    }
    
    
    :returns: 
    CognitoIdentity.Client.exceptions.InvalidParameterException
    CognitoIdentity.Client.exceptions.ResourceNotFoundException
    CognitoIdentity.Client.exceptions.NotAuthorizedException
    CognitoIdentity.Client.exceptions.ResourceConflictException
    CognitoIdentity.Client.exceptions.TooManyRequestsException
    CognitoIdentity.Client.exceptions.InternalErrorException
    
    """
    pass

def get_open_id_token(IdentityId=None, Logins=None):
    """
    Gets an OpenID token, using a known Cognito ID. This known Cognito ID is returned by  GetId . You can optionally add additional logins for the identity. Supplying multiple logins creates an implicit link.
    The OpenId token is valid for 10 minutes.
    This is a public API. You do not need any credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_open_id_token(
        IdentityId='string',
        Logins={
            'string': 'string'
        }
    )
    
    
    :type IdentityId: string
    :param IdentityId: [REQUIRED]\nA unique identifier in the format REGION:GUID.\n

    :type Logins: dict
    :param Logins: A set of optional name-value pairs that map provider names to provider tokens. When using graph.facebook.com and www.amazon.com, supply the access_token returned from the provider\'s authflow. For accounts.google.com, an Amazon Cognito user pool provider, or any other OpenId Connect provider, always include the id_token .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityId': 'string',
    'Token': 'string'
}


Response Structure

(dict) --
Returned in response to a successful GetOpenIdToken request.

IdentityId (string) --
A unique identifier in the format REGION:GUID. Note that the IdentityId returned may not match the one passed on input.

Token (string) --
An OpenID token, valid for 10 minutes.







Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.ResourceConflictException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException
CognitoIdentity.Client.exceptions.ExternalServiceException


    :return: {
        'IdentityId': 'string',
        'Token': 'string'
    }
    
    
    :returns: 
    CognitoIdentity.Client.exceptions.InvalidParameterException
    CognitoIdentity.Client.exceptions.ResourceNotFoundException
    CognitoIdentity.Client.exceptions.NotAuthorizedException
    CognitoIdentity.Client.exceptions.ResourceConflictException
    CognitoIdentity.Client.exceptions.TooManyRequestsException
    CognitoIdentity.Client.exceptions.InternalErrorException
    CognitoIdentity.Client.exceptions.ExternalServiceException
    
    """
    pass

def get_open_id_token_for_developer_identity(IdentityPoolId=None, IdentityId=None, Logins=None, TokenDuration=None):
    """
    Registers (or retrieves) a Cognito IdentityId and an OpenID Connect token for a user authenticated by your backend authentication process. Supplying multiple logins will create an implicit linked account. You can only specify one developer provider as part of the Logins map, which is linked to the identity pool. The developer provider is the "domain" by which Cognito will refer to your users.
    You can use GetOpenIdTokenForDeveloperIdentity to create a new identity and to link new logins (that is, user credentials issued by a public provider or developer provider) to an existing identity. When you want to create a new identity, the IdentityId should be null. When you want to associate a new login with an existing authenticated/unauthenticated identity, you can do so by providing the existing IdentityId . This API will create the identity in the specified IdentityPoolId .
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_open_id_token_for_developer_identity(
        IdentityPoolId='string',
        IdentityId='string',
        Logins={
            'string': 'string'
        },
        TokenDuration=123
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nAn identity pool ID in the format REGION:GUID.\n

    :type IdentityId: string
    :param IdentityId: A unique identifier in the format REGION:GUID.

    :type Logins: dict
    :param Logins: [REQUIRED]\nA set of optional name-value pairs that map provider names to provider tokens. Each name-value pair represents a user from a public provider or developer provider. If the user is from a developer provider, the name-value pair will follow the syntax 'developer_provider_name': 'developer_user_identifier' . The developer provider is the 'domain' by which Cognito will refer to your users; you provided this domain while creating/updating the identity pool. The developer user identifier is an identifier from your backend that uniquely identifies a user. When you create an identity pool, you can specify the supported logins.\n\n(string) --\n(string) --\n\n\n\n

    :type TokenDuration: integer
    :param TokenDuration: The expiration time of the token, in seconds. You can specify a custom expiration time for the token so that you can cache it. If you don\'t provide an expiration time, the token is valid for 15 minutes. You can exchange the token with Amazon STS for temporary AWS credentials, which are valid for a maximum of one hour. The maximum token duration you can set is 24 hours. You should take care in setting the expiration time for a token, as there are significant security implications: an attacker could use a leaked token to access your AWS resources for the token\'s duration.\n\nNote\nPlease provide for a small grace period, usually no more than 5 minutes, to account for clock skew.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityId': 'string',
    'Token': 'string'
}


Response Structure

(dict) --
Returned in response to a successful GetOpenIdTokenForDeveloperIdentity request.

IdentityId (string) --
A unique identifier in the format REGION:GUID.

Token (string) --
An OpenID token.







Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.ResourceConflictException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException
CognitoIdentity.Client.exceptions.DeveloperUserAlreadyRegisteredException


    :return: {
        'IdentityId': 'string',
        'Token': 'string'
    }
    
    
    :returns: 
    CognitoIdentity.Client.exceptions.InvalidParameterException
    CognitoIdentity.Client.exceptions.ResourceNotFoundException
    CognitoIdentity.Client.exceptions.NotAuthorizedException
    CognitoIdentity.Client.exceptions.ResourceConflictException
    CognitoIdentity.Client.exceptions.TooManyRequestsException
    CognitoIdentity.Client.exceptions.InternalErrorException
    CognitoIdentity.Client.exceptions.DeveloperUserAlreadyRegisteredException
    
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

def list_identities(IdentityPoolId=None, MaxResults=None, NextToken=None, HideDisabled=None):
    """
    Lists the identities in an identity pool.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_identities(
        IdentityPoolId='string',
        MaxResults=123,
        NextToken='string',
        HideDisabled=True|False
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nAn identity pool ID in the format REGION:GUID.\n

    :type MaxResults: integer
    :param MaxResults: [REQUIRED]\nThe maximum number of identities to return.\n

    :type NextToken: string
    :param NextToken: A pagination token.

    :type HideDisabled: boolean
    :param HideDisabled: An optional boolean parameter that allows you to hide disabled identities. If omitted, the ListIdentities API will include disabled identities in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityPoolId': 'string',
    'Identities': [
        {
            'IdentityId': 'string',
            'Logins': [
                'string',
            ],
            'CreationDate': datetime(2015, 1, 1),
            'LastModifiedDate': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
The response to a ListIdentities request.

IdentityPoolId (string) --
An identity pool ID in the format REGION:GUID.

Identities (list) --
An object containing a set of identities and associated mappings.

(dict) --
A description of the identity.

IdentityId (string) --
A unique identifier in the format REGION:GUID.

Logins (list) --
The provider names.

(string) --


CreationDate (datetime) --
Date on which the identity was created.

LastModifiedDate (datetime) --
Date on which the identity was last modified.





NextToken (string) --
A pagination token.







Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException


    :return: {
        'IdentityPoolId': 'string',
        'Identities': [
            {
                'IdentityId': 'string',
                'Logins': [
                    'string',
                ],
                'CreationDate': datetime(2015, 1, 1),
                'LastModifiedDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_identity_pools(MaxResults=None, NextToken=None):
    """
    Lists all of the Cognito identity pools registered for your account.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_identity_pools(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: [REQUIRED]\nThe maximum number of identities to return.\n

    :type NextToken: string
    :param NextToken: A pagination token.

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityPools': [
        {
            'IdentityPoolId': 'string',
            'IdentityPoolName': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
The result of a successful ListIdentityPools action.

IdentityPools (list) --
The identity pools returned by the ListIdentityPools action.

(dict) --
A description of the identity pool.

IdentityPoolId (string) --
An identity pool ID in the format REGION:GUID.

IdentityPoolName (string) --
A string that you provide.





NextToken (string) --
A pagination token.







Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.InternalErrorException


    :return: {
        'IdentityPools': [
            {
                'IdentityPoolId': 'string',
                'IdentityPoolName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CognitoIdentity.Client.exceptions.InvalidParameterException
    CognitoIdentity.Client.exceptions.NotAuthorizedException
    CognitoIdentity.Client.exceptions.TooManyRequestsException
    CognitoIdentity.Client.exceptions.ResourceNotFoundException
    CognitoIdentity.Client.exceptions.InternalErrorException
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Lists the tags that are assigned to an Amazon Cognito identity pool.
    A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.
    You can use this action up to 10 times per second, per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the identity pool that the tags are assigned to.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Tags (dict) --The tags that are assigned to the identity pool.

(string) --
(string) --









Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    CognitoIdentity.Client.exceptions.InvalidParameterException
    CognitoIdentity.Client.exceptions.ResourceNotFoundException
    CognitoIdentity.Client.exceptions.NotAuthorizedException
    CognitoIdentity.Client.exceptions.TooManyRequestsException
    CognitoIdentity.Client.exceptions.InternalErrorException
    
    """
    pass

def lookup_developer_identity(IdentityPoolId=None, IdentityId=None, DeveloperUserIdentifier=None, MaxResults=None, NextToken=None):
    """
    Retrieves the IdentityID associated with a DeveloperUserIdentifier or the list of DeveloperUserIdentifier values associated with an IdentityId for an existing identity. Either IdentityID or DeveloperUserIdentifier must not be null. If you supply only one of these values, the other value will be searched in the database and returned as a part of the response. If you supply both, DeveloperUserIdentifier will be matched against IdentityID . If the values are verified against the database, the response returns both values and is the same as the request. Otherwise a ResourceConflictException is thrown.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.lookup_developer_identity(
        IdentityPoolId='string',
        IdentityId='string',
        DeveloperUserIdentifier='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nAn identity pool ID in the format REGION:GUID.\n

    :type IdentityId: string
    :param IdentityId: A unique identifier in the format REGION:GUID.

    :type DeveloperUserIdentifier: string
    :param DeveloperUserIdentifier: A unique ID used by your backend authentication process to identify a user. Typically, a developer identity provider would issue many developer user identifiers, in keeping with the number of users.

    :type MaxResults: integer
    :param MaxResults: The maximum number of identities to return.

    :type NextToken: string
    :param NextToken: A pagination token. The first call you make will have NextToken set to null. After that the service will return NextToken values as needed. For example, let\'s say you make a request with MaxResults set to 10, and there are 20 matches in the database. The service will return a pagination token as a part of the response. This token can be used to call the API again and get results starting from the 11th match.

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityId': 'string',
    'DeveloperUserIdentifierList': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Returned in response to a successful LookupDeveloperIdentity action.

IdentityId (string) --
A unique identifier in the format REGION:GUID.

DeveloperUserIdentifierList (list) --
This is the list of developer user identifiers associated with an identity ID. Cognito supports the association of multiple developer user identifiers with an identity ID.

(string) --


NextToken (string) --
A pagination token. The first call you make will have NextToken set to null. After that the service will return NextToken values as needed. For example, let\'s say you make a request with MaxResults set to 10, and there are 20 matches in the database. The service will return a pagination token as a part of the response. This token can be used to call the API again and get results starting from the 11th match.







Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.ResourceConflictException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException


    :return: {
        'IdentityId': 'string',
        'DeveloperUserIdentifierList': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def merge_developer_identities(SourceUserIdentifier=None, DestinationUserIdentifier=None, DeveloperProviderName=None, IdentityPoolId=None):
    """
    Merges two users having different IdentityId s, existing in the same identity pool, and identified by the same developer provider. You can use this action to request that discrete users be merged and identified as a single user in the Cognito environment. Cognito associates the given source user (SourceUserIdentifier ) with the IdentityId of the DestinationUserIdentifier . Only developer-authenticated users can be merged. If the users to be merged are associated with the same public provider, but as two different users, an exception will be thrown.
    The number of linked logins is limited to 20. So, the number of linked logins for the source user, SourceUserIdentifier , and the destination user, DestinationUserIdentifier , together should not be larger than 20. Otherwise, an exception will be thrown.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.merge_developer_identities(
        SourceUserIdentifier='string',
        DestinationUserIdentifier='string',
        DeveloperProviderName='string',
        IdentityPoolId='string'
    )
    
    
    :type SourceUserIdentifier: string
    :param SourceUserIdentifier: [REQUIRED]\nUser identifier for the source user. The value should be a DeveloperUserIdentifier .\n

    :type DestinationUserIdentifier: string
    :param DestinationUserIdentifier: [REQUIRED]\nUser identifier for the destination user. The value should be a DeveloperUserIdentifier .\n

    :type DeveloperProviderName: string
    :param DeveloperProviderName: [REQUIRED]\nThe 'domain' by which Cognito will refer to your users. This is a (pseudo) domain name that you provide while creating an identity pool. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the DeveloperProviderName , you can use letters as well as period (.), underscore (_), and dash (-).\n

    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nAn identity pool ID in the format REGION:GUID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityId': 'string'
}


Response Structure

(dict) --
Returned in response to a successful MergeDeveloperIdentities action.

IdentityId (string) --
A unique identifier in the format REGION:GUID.







Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.ResourceConflictException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException


    :return: {
        'IdentityId': 'string'
    }
    
    
    :returns: 
    CognitoIdentity.Client.exceptions.InvalidParameterException
    CognitoIdentity.Client.exceptions.ResourceNotFoundException
    CognitoIdentity.Client.exceptions.NotAuthorizedException
    CognitoIdentity.Client.exceptions.ResourceConflictException
    CognitoIdentity.Client.exceptions.TooManyRequestsException
    CognitoIdentity.Client.exceptions.InternalErrorException
    
    """
    pass

def set_identity_pool_roles(IdentityPoolId=None, Roles=None, RoleMappings=None):
    """
    Sets the roles for an identity pool. These roles are used when making calls to  GetCredentialsForIdentity action.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_identity_pool_roles(
        IdentityPoolId='string',
        Roles={
            'string': 'string'
        },
        RoleMappings={
            'string': {
                'Type': 'Token'|'Rules',
                'AmbiguousRoleResolution': 'AuthenticatedRole'|'Deny',
                'RulesConfiguration': {
                    'Rules': [
                        {
                            'Claim': 'string',
                            'MatchType': 'Equals'|'Contains'|'StartsWith'|'NotEqual',
                            'Value': 'string',
                            'RoleARN': 'string'
                        },
                    ]
                }
            }
        }
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nAn identity pool ID in the format REGION:GUID.\n

    :type Roles: dict
    :param Roles: [REQUIRED]\nThe map of roles associated with this pool. For a given role, the key will be either 'authenticated' or 'unauthenticated' and the value will be the Role ARN.\n\n(string) --\n(string) --\n\n\n\n

    :type RoleMappings: dict
    :param RoleMappings: How users for a specific identity provider are to mapped to roles. This is a string to RoleMapping object map. The string identifies the identity provider, for example, 'graph.facebook.com' or 'cognito-idp-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id'.\nUp to 25 rules can be specified per identity provider.\n\n(string) --\n(dict) --A role mapping.\n\nType (string) -- [REQUIRED]The role mapping type. Token will use cognito:roles and cognito:preferred_role claims from the Cognito identity provider token to map groups to roles. Rules will attempt to match claims from the token to map to a role.\n\nAmbiguousRoleResolution (string) --If you specify Token or Rules as the Type , AmbiguousRoleResolution is required.\nSpecifies the action to be taken if either no rules match the claim value for the Rules type, or there is no cognito:preferred_role claim and there are multiple cognito:roles matches for the Token type.\n\nRulesConfiguration (dict) --The rules to be used for mapping users to roles.\nIf you specify Rules as the role mapping type, RulesConfiguration is required.\n\nRules (list) -- [REQUIRED]An array of rules. You can specify up to 25 rules per identity provider.\nRules are evaluated in order. The first one to match specifies the role.\n\n(dict) --A rule that maps a claim name, a claim value, and a match type to a role ARN.\n\nClaim (string) -- [REQUIRED]The claim name that must be present in the token, for example, 'isAdmin' or 'paid'.\n\nMatchType (string) -- [REQUIRED]The match condition that specifies how closely the claim value in the IdP token must match Value .\n\nValue (string) -- [REQUIRED]A brief string that the claim must match, for example, 'paid' or 'yes'.\n\nRoleARN (string) -- [REQUIRED]The role ARN.\n\n\n\n\n\n\n\n\n\n\n\n\n

    :returns: 
    CognitoIdentity.Client.exceptions.InvalidParameterException
    CognitoIdentity.Client.exceptions.ResourceNotFoundException
    CognitoIdentity.Client.exceptions.NotAuthorizedException
    CognitoIdentity.Client.exceptions.ResourceConflictException
    CognitoIdentity.Client.exceptions.TooManyRequestsException
    CognitoIdentity.Client.exceptions.InternalErrorException
    CognitoIdentity.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Assigns a set of tags to an Amazon Cognito identity pool. A tag is a label that you can use to categorize and manage identity pools in different ways, such as by purpose, owner, environment, or other criteria.
    Each tag consists of a key and value, both of which you define. A key is a general category for more specific values. For example, if you have two versions of an identity pool, one for testing and another for production, you might assign an Environment tag key to both identity pools. The value of this key might be Test for one identity pool and Production for the other.
    Tags are useful for cost tracking and access control. You can activate your tags so that they appear on the Billing and Cost Management console, where you can track the costs associated with your identity pools. In an IAM policy, you can constrain permissions for identity pools based on specific tags or tag values.
    You can use this action up to 5 times per second, per account. An identity pool can have as many as 50 tags.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the identity pool to assign the tags to.\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nThe tags to assign to the identity pool.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def unlink_developer_identity(IdentityId=None, IdentityPoolId=None, DeveloperProviderName=None, DeveloperUserIdentifier=None):
    """
    Unlinks a DeveloperUserIdentifier from an existing identity. Unlinked developer users will be considered new identities next time they are seen. If, for a given Cognito identity, you remove all federated identities as well as the developer user identifier, the Cognito identity becomes inaccessible.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.unlink_developer_identity(
        IdentityId='string',
        IdentityPoolId='string',
        DeveloperProviderName='string',
        DeveloperUserIdentifier='string'
    )
    
    
    :type IdentityId: string
    :param IdentityId: [REQUIRED]\nA unique identifier in the format REGION:GUID.\n

    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nAn identity pool ID in the format REGION:GUID.\n

    :type DeveloperProviderName: string
    :param DeveloperProviderName: [REQUIRED]\nThe 'domain' by which Cognito will refer to your users.\n

    :type DeveloperUserIdentifier: string
    :param DeveloperUserIdentifier: [REQUIRED]\nA unique ID used by your backend authentication process to identify a user.\n

    :returns: 
    CognitoIdentity.Client.exceptions.InvalidParameterException
    CognitoIdentity.Client.exceptions.ResourceNotFoundException
    CognitoIdentity.Client.exceptions.NotAuthorizedException
    CognitoIdentity.Client.exceptions.ResourceConflictException
    CognitoIdentity.Client.exceptions.TooManyRequestsException
    CognitoIdentity.Client.exceptions.InternalErrorException
    
    """
    pass

def unlink_identity(IdentityId=None, Logins=None, LoginsToRemove=None):
    """
    Unlinks a federated identity from an existing account. Unlinked logins will be considered new identities next time they are seen. Removing the last linked login will make this identity inaccessible.
    This is a public API. You do not need any credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.unlink_identity(
        IdentityId='string',
        Logins={
            'string': 'string'
        },
        LoginsToRemove=[
            'string',
        ]
    )
    
    
    :type IdentityId: string
    :param IdentityId: [REQUIRED]\nA unique identifier in the format REGION:GUID.\n

    :type Logins: dict
    :param Logins: [REQUIRED]\nA set of optional name-value pairs that map provider names to provider tokens.\n\n(string) --\n(string) --\n\n\n\n

    :type LoginsToRemove: list
    :param LoginsToRemove: [REQUIRED]\nProvider names to unlink from this identity.\n\n(string) --\n\n

    :returns: 
    CognitoIdentity.Client.exceptions.InvalidParameterException
    CognitoIdentity.Client.exceptions.ResourceNotFoundException
    CognitoIdentity.Client.exceptions.NotAuthorizedException
    CognitoIdentity.Client.exceptions.ResourceConflictException
    CognitoIdentity.Client.exceptions.TooManyRequestsException
    CognitoIdentity.Client.exceptions.InternalErrorException
    CognitoIdentity.Client.exceptions.ExternalServiceException
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes the specified tags from an Amazon Cognito identity pool. You can use this action up to 5 times per second, per account
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the identity pool that the tags are assigned to.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe keys of the tags to remove from the user pool.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_identity_pool(IdentityPoolId=None, IdentityPoolName=None, AllowUnauthenticatedIdentities=None, AllowClassicFlow=None, SupportedLoginProviders=None, DeveloperProviderName=None, OpenIdConnectProviderARNs=None, CognitoIdentityProviders=None, SamlProviderARNs=None, IdentityPoolTags=None):
    """
    Updates an identity pool.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_identity_pool(
        IdentityPoolId='string',
        IdentityPoolName='string',
        AllowUnauthenticatedIdentities=True|False,
        AllowClassicFlow=True|False,
        SupportedLoginProviders={
            'string': 'string'
        },
        DeveloperProviderName='string',
        OpenIdConnectProviderARNs=[
            'string',
        ],
        CognitoIdentityProviders=[
            {
                'ProviderName': 'string',
                'ClientId': 'string',
                'ServerSideTokenCheck': True|False
            },
        ],
        SamlProviderARNs=[
            'string',
        ],
        IdentityPoolTags={
            'string': 'string'
        }
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nAn identity pool ID in the format REGION:GUID.\n

    :type IdentityPoolName: string
    :param IdentityPoolName: [REQUIRED]\nA string that you provide.\n

    :type AllowUnauthenticatedIdentities: boolean
    :param AllowUnauthenticatedIdentities: [REQUIRED]\nTRUE if the identity pool supports unauthenticated logins.\n

    :type AllowClassicFlow: boolean
    :param AllowClassicFlow: Enables or disables the Basic (Classic) authentication flow. For more information, see Identity Pools (Federated Identities) Authentication Flow in the Amazon Cognito Developer Guide .

    :type SupportedLoginProviders: dict
    :param SupportedLoginProviders: Optional key:value pairs mapping provider names to provider app IDs.\n\n(string) --\n(string) --\n\n\n\n

    :type DeveloperProviderName: string
    :param DeveloperProviderName: The 'domain' by which Cognito will refer to your users.

    :type OpenIdConnectProviderARNs: list
    :param OpenIdConnectProviderARNs: A list of OpendID Connect provider ARNs.\n\n(string) --\n\n

    :type CognitoIdentityProviders: list
    :param CognitoIdentityProviders: A list representing an Amazon Cognito user pool and its client ID.\n\n(dict) --A provider representing an Amazon Cognito user pool and its client ID.\n\nProviderName (string) --The provider name for an Amazon Cognito user pool. For example, cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789 .\n\nClientId (string) --The client ID for the Amazon Cognito user pool.\n\nServerSideTokenCheck (boolean) --TRUE if server-side token validation is enabled for the identity provider\xe2\x80\x99s token.\nOnce you set ServerSideTokenCheck to TRUE for an identity pool, that identity pool will check with the integrated user pools to make sure that the user has not been globally signed out or deleted before the identity pool provides an OIDC token or AWS credentials for the user.\nIf the user is signed out or deleted, the identity pool will return a 400 Not Authorized error.\n\n\n\n\n

    :type SamlProviderARNs: list
    :param SamlProviderARNs: An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.\n\n(string) --\n\n

    :type IdentityPoolTags: dict
    :param IdentityPoolTags: The tags that are assigned to the identity pool. A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityPoolId': 'string',
    'IdentityPoolName': 'string',
    'AllowUnauthenticatedIdentities': True|False,
    'AllowClassicFlow': True|False,
    'SupportedLoginProviders': {
        'string': 'string'
    },
    'DeveloperProviderName': 'string',
    'OpenIdConnectProviderARNs': [
        'string',
    ],
    'CognitoIdentityProviders': [
        {
            'ProviderName': 'string',
            'ClientId': 'string',
            'ServerSideTokenCheck': True|False
        },
    ],
    'SamlProviderARNs': [
        'string',
    ],
    'IdentityPoolTags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
An object representing an Amazon Cognito identity pool.

IdentityPoolId (string) --
An identity pool ID in the format REGION:GUID.

IdentityPoolName (string) --
A string that you provide.

AllowUnauthenticatedIdentities (boolean) --
TRUE if the identity pool supports unauthenticated logins.

AllowClassicFlow (boolean) --
Enables or disables the Basic (Classic) authentication flow. For more information, see Identity Pools (Federated Identities) Authentication Flow in the Amazon Cognito Developer Guide .

SupportedLoginProviders (dict) --
Optional key:value pairs mapping provider names to provider app IDs.

(string) --
(string) --




DeveloperProviderName (string) --
The "domain" by which Cognito will refer to your users.

OpenIdConnectProviderARNs (list) --
A list of OpendID Connect provider ARNs.

(string) --


CognitoIdentityProviders (list) --
A list representing an Amazon Cognito user pool and its client ID.

(dict) --
A provider representing an Amazon Cognito user pool and its client ID.

ProviderName (string) --
The provider name for an Amazon Cognito user pool. For example, cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789 .

ClientId (string) --
The client ID for the Amazon Cognito user pool.

ServerSideTokenCheck (boolean) --
TRUE if server-side token validation is enabled for the identity provider\xe2\x80\x99s token.
Once you set ServerSideTokenCheck to TRUE for an identity pool, that identity pool will check with the integrated user pools to make sure that the user has not been globally signed out or deleted before the identity pool provides an OIDC token or AWS credentials for the user.
If the user is signed out or deleted, the identity pool will return a 400 Not Authorized error.





SamlProviderARNs (list) --
An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.

(string) --


IdentityPoolTags (dict) --
The tags that are assigned to the identity pool. A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.

(string) --
(string) --










Exceptions

CognitoIdentity.Client.exceptions.InvalidParameterException
CognitoIdentity.Client.exceptions.ResourceNotFoundException
CognitoIdentity.Client.exceptions.NotAuthorizedException
CognitoIdentity.Client.exceptions.ResourceConflictException
CognitoIdentity.Client.exceptions.TooManyRequestsException
CognitoIdentity.Client.exceptions.InternalErrorException
CognitoIdentity.Client.exceptions.ConcurrentModificationException
CognitoIdentity.Client.exceptions.LimitExceededException


    :return: {
        'IdentityPoolId': 'string',
        'IdentityPoolName': 'string',
        'AllowUnauthenticatedIdentities': True|False,
        'AllowClassicFlow': True|False,
        'SupportedLoginProviders': {
            'string': 'string'
        },
        'DeveloperProviderName': 'string',
        'OpenIdConnectProviderARNs': [
            'string',
        ],
        'CognitoIdentityProviders': [
            {
                'ProviderName': 'string',
                'ClientId': 'string',
                'ServerSideTokenCheck': True|False
            },
        ],
        'SamlProviderARNs': [
            'string',
        ],
        'IdentityPoolTags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

