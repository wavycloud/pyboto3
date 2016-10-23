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


def create_identity_pool(IdentityPoolName=None, AllowUnauthenticatedIdentities=None, SupportedLoginProviders=None,
                         DeveloperProviderName=None, OpenIdConnectProviderARNs=None, CognitoIdentityProviders=None,
                         SamlProviderARNs=None):
    """
    :param IdentityPoolName: [REQUIRED]
            A string that you provide.
            
    :type IdentityPoolName: string
    :param AllowUnauthenticatedIdentities: [REQUIRED]
            TRUE if the identity pool supports unauthenticated logins.
            
    :type AllowUnauthenticatedIdentities: boolean
    :param SupportedLoginProviders: Optional key:value pairs mapping provider names to provider app IDs.
            (string) --
            (string) --
            
    :type SupportedLoginProviders: dict
    :param DeveloperProviderName: The 'domain' by which Cognito will refer to your users. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the DeveloperProviderName , you can use letters as well as period (. ), underscore (_ ), and dash (- ).
            Once you have set a developer provider name, you cannot change it. Please take care in setting this parameter.
            
    :type DeveloperProviderName: string
    :param OpenIdConnectProviderARNs: A list of OpendID Connect provider ARNs.
            (string) --
            
    :type OpenIdConnectProviderARNs: list
    :param CognitoIdentityProviders: An array of Amazon Cognito Identity user pools.
            (dict) --A provider representing an Amazon Cognito Identity User Pool and its client ID.
            ProviderName (string) --The provider name for an Amazon Cognito Identity User Pool. For example, cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789 .
            ClientId (string) --The client ID for the Amazon Cognito Identity User Pool.
            
            
    :type CognitoIdentityProviders: list
    :param SamlProviderARNs: An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.
            (string) --
            
    :type SamlProviderARNs: list
    """
    pass


def delete_identities(IdentityIdsToDelete=None):
    """
    :param IdentityIdsToDelete: [REQUIRED]
            A list of 1-60 identities that you want to delete.
            (string) --
            Return typedict
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
            
            
            
    :type IdentityIdsToDelete: list
    """
    pass


def delete_identity_pool(IdentityPoolId=None):
    """
    :param IdentityPoolId: [REQUIRED] An identity pool ID in the format REGION:GUID.
            ReturnsNone
            
    :type IdentityPoolId: string
    """
    pass


def describe_identity(IdentityId=None):
    """
    :param IdentityId: [REQUIRED]
            A unique identifier in the format REGION:GUID.
            Return typedict
            ReturnsResponse Syntax{
              'IdentityId': 'string',
              'Logins': [
                'string',
              ],
              'CreationDate': datetime(2015, 1, 1),
              'LastModifiedDate': datetime(2015, 1, 1)
            }
            Response Structure
            (dict) -- A description of the identity.
            IdentityId (string) -- A unique identifier in the format REGION:GUID.
            Logins (list) -- A set of optional name-value pairs that map provider names to provider tokens.
            (string) --
            CreationDate (datetime) --Date on which the identity was created.
            LastModifiedDate (datetime) --Date on which the identity was last modified.
            
            
    :type IdentityId: string
    """
    pass


def describe_identity_pool(IdentityPoolId=None):
    """
    :param IdentityPoolId: [REQUIRED] An identity pool ID in the format REGION:GUID.
            Return typedict
            ReturnsResponse Syntax{
              'IdentityPoolId': 'string',
              'IdentityPoolName': 'string',
              'AllowUnauthenticatedIdentities': True|False,
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
                  'ClientId': 'string'
                },
              ],
              'SamlProviderARNs': [
                'string',
              ]
            }
            Response Structure
            (dict) -- An object representing a Cognito identity pool.
            IdentityPoolId (string) -- An identity pool ID in the format REGION:GUID.
            IdentityPoolName (string) --A string that you provide.
            AllowUnauthenticatedIdentities (boolean) -- TRUE if the identity pool supports unauthenticated logins.
            SupportedLoginProviders (dict) --Optional key:value pairs mapping provider names to provider app IDs.
            (string) --
            (string) --
            
            DeveloperProviderName (string) --The 'domain' by which Cognito will refer to your users.
            OpenIdConnectProviderARNs (list) --A list of OpendID Connect provider ARNs.
            (string) --
            CognitoIdentityProviders (list) --A list representing an Amazon Cognito Identity User Pool and its client ID.
            (dict) --A provider representing an Amazon Cognito Identity User Pool and its client ID.
            ProviderName (string) --The provider name for an Amazon Cognito Identity User Pool. For example, cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789 .
            ClientId (string) --The client ID for the Amazon Cognito Identity User Pool.
            
            SamlProviderARNs (list) --An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.
            (string) --
            
            
    :type IdentityPoolId: string
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


def get_credentials_for_identity(IdentityId=None, Logins=None, CustomRoleArn=None):
    """
    :param IdentityId: [REQUIRED]
            A unique identifier in the format REGION:GUID.
            
    :type IdentityId: string
    :param Logins: A set of optional name-value pairs that map provider names to provider tokens.
            (string) --
            (string) --
            
    :type Logins: dict
    :param CustomRoleArn: The Amazon Resource Name (ARN) of the role to be assumed when multiple roles were received in the token from the identity provider. For example, a SAML-based identity provider. This parameter is optional for identity providers that do not support role customization.
    :type CustomRoleArn: string
    """
    pass


def get_id(AccountId=None, IdentityPoolId=None, Logins=None):
    """
    :param AccountId: A standard AWS account ID (9+ digits).
    :type AccountId: string
    :param IdentityPoolId: [REQUIRED] An identity pool ID in the format REGION:GUID.
    :type IdentityPoolId: string
    :param Logins: A set of optional name-value pairs that map provider names to provider tokens.
            The available provider names for Logins are as follows:
            Facebook: graph.facebook.com
            Google: accounts.google.com
            Amazon: www.amazon.com
            Twitter: api.twitter.com
            Digits: www.digits.com
            (string) --
            (string) --
            
    :type Logins: dict
    """
    pass


def get_identity_pool_roles(IdentityPoolId=None):
    """
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            Return typedict
            ReturnsResponse Syntax{
              'IdentityPoolId': 'string',
              'Roles': {
                'string': 'string'
              }
            }
            Response Structure
            (dict) --Returned in response to a successful GetIdentityPoolRoles operation.
            IdentityPoolId (string) --An identity pool ID in the format REGION:GUID.
            Roles (dict) --The map of roles associated with this pool. Currently only authenticated and unauthenticated roles are supported.
            (string) --
            (string) --
            
            
            
    :type IdentityPoolId: string
    """
    pass


def get_open_id_token(IdentityId=None, Logins=None):
    """
    :param IdentityId: [REQUIRED] A unique identifier in the format REGION:GUID.
    :type IdentityId: string
    :param Logins: A set of optional name-value pairs that map provider names to provider tokens. When using graph.facebook.com and www.amazon.com, supply the access_token returned from the provider's authflow. For accounts.google.com or any other OpenId Connect provider, always include the id_token.
            (string) --
            (string) --
            
    :type Logins: dict
    """
    pass


def get_open_id_token_for_developer_identity(IdentityPoolId=None, IdentityId=None, Logins=None, TokenDuration=None):
    """
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            
    :type IdentityPoolId: string
    :param IdentityId: A unique identifier in the format REGION:GUID.
    :type IdentityId: string
    :param Logins: [REQUIRED]
            A set of optional name-value pairs that map provider names to provider tokens. Each name-value pair represents a user from a public provider or developer provider. If the user is from a developer provider, the name-value pair will follow the syntax 'developer_provider_name': 'developer_user_identifier' . The developer provider is the 'domain' by which Cognito will refer to your users; you provided this domain while creating/updating the identity pool. The developer user identifier is an identifier from your backend that uniquely identifies a user. When you create an identity pool, you can specify the supported logins.
            (string) --
            (string) --
            
    :type Logins: dict
    :param TokenDuration: The expiration time of the token, in seconds. You can specify a custom expiration time for the token so that you can cache it. If you don't provide an expiration time, the token is valid for 15 minutes. You can exchange the token with Amazon STS for temporary AWS credentials, which are valid for a maximum of one hour. The maximum token duration you can set is 24 hours. You should take care in setting the expiration time for a token, as there are significant security implications: an attacker could use a leaked token to access your AWS resources for the token's duration.
    :type TokenDuration: integer
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


def get_waiter():
    """
    """
    pass


def list_identities(IdentityPoolId=None, MaxResults=None, NextToken=None, HideDisabled=None):
    """
    :param IdentityPoolId: [REQUIRED] An identity pool ID in the format REGION:GUID.
    :type IdentityPoolId: string
    :param MaxResults: [REQUIRED] The maximum number of identities to return.
    :type MaxResults: integer
    :param NextToken: A pagination token.
    :type NextToken: string
    :param HideDisabled: An optional boolean parameter that allows you to hide disabled identities. If omitted, the ListIdentities API will include disabled identities in the response.
    :type HideDisabled: boolean
    """
    pass


def list_identity_pools(MaxResults=None, NextToken=None):
    """
    :param MaxResults: [REQUIRED] The maximum number of identities to return.
    :type MaxResults: integer
    :param NextToken: A pagination token.
    :type NextToken: string
    """
    pass


def lookup_developer_identity(IdentityPoolId=None, IdentityId=None, DeveloperUserIdentifier=None, MaxResults=None,
                              NextToken=None):
    """
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            
    :type IdentityPoolId: string
    :param IdentityId: A unique identifier in the format REGION:GUID.
    :type IdentityId: string
    :param DeveloperUserIdentifier: A unique ID used by your backend authentication process to identify a user. Typically, a developer identity provider would issue many developer user identifiers, in keeping with the number of users.
    :type DeveloperUserIdentifier: string
    :param MaxResults: The maximum number of identities to return.
    :type MaxResults: integer
    :param NextToken: A pagination token. The first call you make will have NextToken set to null. After that the service will return NextToken values as needed. For example, let's say you make a request with MaxResults set to 10, and there are 20 matches in the database. The service will return a pagination token as a part of the response. This token can be used to call the API again and get results starting from the 11th match.
    :type NextToken: string
    """
    pass


def merge_developer_identities(SourceUserIdentifier=None, DestinationUserIdentifier=None, DeveloperProviderName=None,
                               IdentityPoolId=None):
    """
    :param SourceUserIdentifier: [REQUIRED]
            User identifier for the source user. The value should be a DeveloperUserIdentifier .
            
    :type SourceUserIdentifier: string
    :param DestinationUserIdentifier: [REQUIRED]
            User identifier for the destination user. The value should be a DeveloperUserIdentifier .
            
    :type DestinationUserIdentifier: string
    :param DeveloperProviderName: [REQUIRED]
            The 'domain' by which Cognito will refer to your users. This is a (pseudo) domain name that you provide while creating an identity pool. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the DeveloperProviderName , you can use letters as well as period (.), underscore (_), and dash (-).
            
    :type DeveloperProviderName: string
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            
    :type IdentityPoolId: string
    """
    pass


def set_identity_pool_roles(IdentityPoolId=None, Roles=None):
    """
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            
    :type IdentityPoolId: string
    :param Roles: [REQUIRED]
            The map of roles associated with this pool. For a given role, the key will be either 'authenticated' or 'unauthenticated' and the value will be the Role ARN.
            (string) --
            (string) --
            
    :type Roles: dict
    """
    pass


def unlink_developer_identity(IdentityId=None, IdentityPoolId=None, DeveloperProviderName=None,
                              DeveloperUserIdentifier=None):
    """
    :param IdentityId: [REQUIRED]
            A unique identifier in the format REGION:GUID.
            
    :type IdentityId: string
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            
    :type IdentityPoolId: string
    :param DeveloperProviderName: [REQUIRED]
            The 'domain' by which Cognito will refer to your users.
            
    :type DeveloperProviderName: string
    :param DeveloperUserIdentifier: [REQUIRED] A unique ID used by your backend authentication process to identify a user.
    :type DeveloperUserIdentifier: string
    """
    pass


def unlink_identity(IdentityId=None, Logins=None, LoginsToRemove=None):
    """
    :param IdentityId: [REQUIRED] A unique identifier in the format REGION:GUID.
    :type IdentityId: string
    :param Logins: [REQUIRED] A set of optional name-value pairs that map provider names to provider tokens.
            (string) --
            (string) --
            
    :type Logins: dict
    :param LoginsToRemove: [REQUIRED] Provider names to unlink from this identity.
            (string) --
            
    :type LoginsToRemove: list
    """
    pass


def update_identity_pool(IdentityPoolId=None, IdentityPoolName=None, AllowUnauthenticatedIdentities=None,
                         SupportedLoginProviders=None, DeveloperProviderName=None, OpenIdConnectProviderARNs=None,
                         CognitoIdentityProviders=None, SamlProviderARNs=None):
    """
    :param IdentityPoolId: [REQUIRED] An identity pool ID in the format REGION:GUID.
    :type IdentityPoolId: string
    :param IdentityPoolName: [REQUIRED]
            A string that you provide.
            
    :type IdentityPoolName: string
    :param AllowUnauthenticatedIdentities: [REQUIRED] TRUE if the identity pool supports unauthenticated logins.
    :type AllowUnauthenticatedIdentities: boolean
    :param SupportedLoginProviders: Optional key:value pairs mapping provider names to provider app IDs.
            (string) --
            (string) --
            
    :type SupportedLoginProviders: dict
    :param DeveloperProviderName: The 'domain' by which Cognito will refer to your users.
    :type DeveloperProviderName: string
    :param OpenIdConnectProviderARNs: A list of OpendID Connect provider ARNs.
            (string) --
            
    :type OpenIdConnectProviderARNs: list
    :param CognitoIdentityProviders: A list representing an Amazon Cognito Identity User Pool and its client ID.
            (dict) --A provider representing an Amazon Cognito Identity User Pool and its client ID.
            ProviderName (string) --The provider name for an Amazon Cognito Identity User Pool. For example, cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789 .
            ClientId (string) --The client ID for the Amazon Cognito Identity User Pool.
            
            
    :type CognitoIdentityProviders: list
    :param SamlProviderARNs: An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.
            (string) --
            
    :type SamlProviderARNs: list
    """
    pass
