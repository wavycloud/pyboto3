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

def create_token(clientId=None, clientSecret=None, grantType=None, deviceCode=None, code=None, refreshToken=None, scope=None, redirectUri=None):
    """
    Creates and returns an access token for the authorized client. The access token issued will be used to fetch short-term credentials for the assigned roles in the AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_token(
        clientId='string',
        clientSecret='string',
        grantType='string',
        deviceCode='string',
        code='string',
        refreshToken='string',
        scope=[
            'string',
        ],
        redirectUri='string'
    )
    
    
    :type clientId: string
    :param clientId: [REQUIRED]\nThe unique identifier string for each client. This value should come from the persisted result of the RegisterClient API.\n

    :type clientSecret: string
    :param clientSecret: [REQUIRED]\nA secret string generated for the client. This value should come from the persisted result of the RegisterClient API.\n

    :type grantType: string
    :param grantType: [REQUIRED]\nSupports grant types for authorization code, refresh token, and device code request.\n

    :type deviceCode: string
    :param deviceCode: [REQUIRED]\nUsed only when calling this API for the device code grant type. This short-term code is used to identify this authentication attempt. This should come from an in-memory reference to the result of the StartDeviceAuthorization API.\n

    :type code: string
    :param code: The authorization code received from the authorization service. This parameter is required to perform an authorization grant request to get access to a token.

    :type refreshToken: string
    :param refreshToken: The token used to obtain an access token in the event that the access token is invalid or expired. This token is not issued by the service.

    :type scope: list
    :param scope: The list of scopes that is defined by the client. Upon authorization, this list is used to restrict permissions when granting an access token.\n\n(string) --\n\n

    :type redirectUri: string
    :param redirectUri: The location of the application that will receive the authorization code. Users authorize the service to send the request to this location.

    :rtype: dict

ReturnsResponse Syntax
{
    'accessToken': 'string',
    'tokenType': 'string',
    'expiresIn': 123,
    'refreshToken': 'string',
    'idToken': 'string'
}


Response Structure

(dict) --

accessToken (string) --
An opaque token to access AWS SSO resources assigned to a user.

tokenType (string) --
Used to notify the client that the returned token is an access token. The supported type is BearerToken .

expiresIn (integer) --
Indicates the time in seconds when an access token will expire.

refreshToken (string) --
A token that, if present, can be used to refresh a previously issued access token that might have expired.

idToken (string) --
The identifier of the user that associated with the access token, if present.







Exceptions

SSOOIDC.Client.exceptions.InvalidRequestException
SSOOIDC.Client.exceptions.InvalidClientException
SSOOIDC.Client.exceptions.InvalidGrantException
SSOOIDC.Client.exceptions.UnauthorizedClientException
SSOOIDC.Client.exceptions.UnsupportedGrantTypeException
SSOOIDC.Client.exceptions.InvalidScopeException
SSOOIDC.Client.exceptions.AuthorizationPendingException
SSOOIDC.Client.exceptions.SlowDownException
SSOOIDC.Client.exceptions.AccessDeniedException
SSOOIDC.Client.exceptions.ExpiredTokenException
SSOOIDC.Client.exceptions.InternalServerException


    :return: {
        'accessToken': 'string',
        'tokenType': 'string',
        'expiresIn': 123,
        'refreshToken': 'string',
        'idToken': 'string'
    }
    
    
    :returns: 
    SSOOIDC.Client.exceptions.InvalidRequestException
    SSOOIDC.Client.exceptions.InvalidClientException
    SSOOIDC.Client.exceptions.InvalidGrantException
    SSOOIDC.Client.exceptions.UnauthorizedClientException
    SSOOIDC.Client.exceptions.UnsupportedGrantTypeException
    SSOOIDC.Client.exceptions.InvalidScopeException
    SSOOIDC.Client.exceptions.AuthorizationPendingException
    SSOOIDC.Client.exceptions.SlowDownException
    SSOOIDC.Client.exceptions.AccessDeniedException
    SSOOIDC.Client.exceptions.ExpiredTokenException
    SSOOIDC.Client.exceptions.InternalServerException
    
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

def register_client(clientName=None, clientType=None, scopes=None):
    """
    Registers a client with AWS SSO. This allows clients to initiate device authorization. The output should be persisted for reuse through many authentication requests.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_client(
        clientName='string',
        clientType='string',
        scopes=[
            'string',
        ]
    )
    
    
    :type clientName: string
    :param clientName: [REQUIRED]\nThe friendly name of the client.\n

    :type clientType: string
    :param clientType: [REQUIRED]\nThe type of client. The service supports only public as a client type. Anything other than public will be rejected by the service.\n

    :type scopes: list
    :param scopes: The list of scopes that are defined by the client. Upon authorization, this list is used to restrict permissions when granting an access token.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'clientId': 'string',
    'clientSecret': 'string',
    'clientIdIssuedAt': 123,
    'clientSecretExpiresAt': 123,
    'authorizationEndpoint': 'string',
    'tokenEndpoint': 'string'
}


Response Structure

(dict) --

clientId (string) --
The unique identifier string for each client. This client uses this identifier to get authenticated by the service in subsequent calls.

clientSecret (string) --
A secret string generated for the client. The client will use this string to get authenticated by the service in subsequent calls.

clientIdIssuedAt (integer) --
Indicates the time at which the clientId and clientSecret were issued.

clientSecretExpiresAt (integer) --
Indicates the time at which the clientId and clientSecret will become invalid.

authorizationEndpoint (string) --
The endpoint where the client can request authorization.

tokenEndpoint (string) --
The endpoint where the client can get an access token.







Exceptions

SSOOIDC.Client.exceptions.InvalidRequestException
SSOOIDC.Client.exceptions.InvalidScopeException
SSOOIDC.Client.exceptions.InvalidClientMetadataException
SSOOIDC.Client.exceptions.InternalServerException


    :return: {
        'clientId': 'string',
        'clientSecret': 'string',
        'clientIdIssuedAt': 123,
        'clientSecretExpiresAt': 123,
        'authorizationEndpoint': 'string',
        'tokenEndpoint': 'string'
    }
    
    
    :returns: 
    SSOOIDC.Client.exceptions.InvalidRequestException
    SSOOIDC.Client.exceptions.InvalidScopeException
    SSOOIDC.Client.exceptions.InvalidClientMetadataException
    SSOOIDC.Client.exceptions.InternalServerException
    
    """
    pass

def start_device_authorization(clientId=None, clientSecret=None, startUrl=None):
    """
    Initiates device authorization by requesting a pair of verification codes from the authorization service.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_device_authorization(
        clientId='string',
        clientSecret='string',
        startUrl='string'
    )
    
    
    :type clientId: string
    :param clientId: [REQUIRED]\nThe unique identifier string for the client that is registered with AWS SSO. This value should come from the persisted result of the RegisterClient API operation.\n

    :type clientSecret: string
    :param clientSecret: [REQUIRED]\nA secret string that is generated for the client. This value should come from the persisted result of the RegisterClient API operation.\n

    :type startUrl: string
    :param startUrl: [REQUIRED]\nThe URL for the AWS SSO user portal. For more information, see Using the User Portal in the AWS Single Sign-On User Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'deviceCode': 'string',
    'userCode': 'string',
    'verificationUri': 'string',
    'verificationUriComplete': 'string',
    'expiresIn': 123,
    'interval': 123
}


Response Structure

(dict) --

deviceCode (string) --
The short-lived code that is used by the device when polling for a session token.

userCode (string) --
A one-time user verification code. This is needed to authorize an in-use device.

verificationUri (string) --
The URI of the verification page that takes the userCode to authorize the device.

verificationUriComplete (string) --
An alternate URL that the client can use to automatically launch a browser. This process skips the manual step in which the user visits the verification page and enters their code.

expiresIn (integer) --
Indicates the number of seconds in which the verification code will become invalid.

interval (integer) --
Indicates the number of seconds the client must wait between attempts when polling for a session.







Exceptions

SSOOIDC.Client.exceptions.InvalidRequestException
SSOOIDC.Client.exceptions.InvalidClientException
SSOOIDC.Client.exceptions.UnauthorizedClientException
SSOOIDC.Client.exceptions.SlowDownException
SSOOIDC.Client.exceptions.InternalServerException


    :return: {
        'deviceCode': 'string',
        'userCode': 'string',
        'verificationUri': 'string',
        'verificationUriComplete': 'string',
        'expiresIn': 123,
        'interval': 123
    }
    
    
    :returns: 
    SSOOIDC.Client.exceptions.InvalidRequestException
    SSOOIDC.Client.exceptions.InvalidClientException
    SSOOIDC.Client.exceptions.UnauthorizedClientException
    SSOOIDC.Client.exceptions.SlowDownException
    SSOOIDC.Client.exceptions.InternalServerException
    
    """
    pass

