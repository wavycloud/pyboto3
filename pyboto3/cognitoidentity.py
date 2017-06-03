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

def create_identity_pool(IdentityPoolName=None, AllowUnauthenticatedIdentities=None, SupportedLoginProviders=None, DeveloperProviderName=None, OpenIdConnectProviderARNs=None, CognitoIdentityProviders=None, SamlProviderARNs=None):
    """
    Creates a new identity pool. The identity pool is a store of user identity information that is specific to your AWS account. The limit on identity pools is 60 per account. The keys for SupportedLoginProviders are as follows:
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    
    :example: response = client.create_identity_pool(
        IdentityPoolName='string',
        AllowUnauthenticatedIdentities=True|False,
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
        ]
    )
    
    
    :type IdentityPoolName: string
    :param IdentityPoolName: [REQUIRED]
            A string that you provide.
            

    :type AllowUnauthenticatedIdentities: boolean
    :param AllowUnauthenticatedIdentities: [REQUIRED]
            TRUE if the identity pool supports unauthenticated logins.
            

    :type SupportedLoginProviders: dict
    :param SupportedLoginProviders: Optional key:value pairs mapping provider names to provider app IDs.
            (string) --
            (string) --
            

    :type DeveloperProviderName: string
    :param DeveloperProviderName: The 'domain' by which Cognito will refer to your users. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the DeveloperProviderName , you can use letters as well as period (. ), underscore (_ ), and dash (- ).
            Once you have set a developer provider name, you cannot change it. Please take care in setting this parameter.
            

    :type OpenIdConnectProviderARNs: list
    :param OpenIdConnectProviderARNs: A list of OpendID Connect provider ARNs.
            (string) --
            

    :type CognitoIdentityProviders: list
    :param CognitoIdentityProviders: An array of Amazon Cognito Identity user pools and their client IDs.
            (dict) --A provider representing an Amazon Cognito Identity User Pool and its client ID.
            ProviderName (string) --The provider name for an Amazon Cognito Identity User Pool. For example, cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789 .
            ClientId (string) --The client ID for the Amazon Cognito Identity User Pool.
            ServerSideTokenCheck (boolean) --TRUE if server-side token validation is enabled for the identity provider s token.
            
            

    :type SamlProviderARNs: list
    :param SamlProviderARNs: An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.
            (string) --
            

    :rtype: dict
    :return: {
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
                'ClientId': 'string',
                'ServerSideTokenCheck': True|False
            },
        ],
        'SamlProviderARNs': [
            'string',
        ]
    }
    
    
    :returns: 
    IdentityPoolName (string) -- [REQUIRED]
    A string that you provide.
    
    AllowUnauthenticatedIdentities (boolean) -- [REQUIRED]
    TRUE if the identity pool supports unauthenticated logins.
    
    SupportedLoginProviders (dict) -- Optional key:value pairs mapping provider names to provider app IDs.
    
    (string) --
    (string) --
    
    
    
    
    DeveloperProviderName (string) -- The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the DeveloperProviderName , you can use letters as well as period (. ), underscore (_ ), and dash (- ).
    Once you have set a developer provider name, you cannot change it. Please take care in setting this parameter.
    
    OpenIdConnectProviderARNs (list) -- A list of OpendID Connect provider ARNs.
    
    (string) --
    
    
    CognitoIdentityProviders (list) -- An array of Amazon Cognito Identity user pools and their client IDs.
    
    (dict) --A provider representing an Amazon Cognito Identity User Pool and its client ID.
    
    ProviderName (string) --The provider name for an Amazon Cognito Identity User Pool. For example, cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789 .
    
    ClientId (string) --The client ID for the Amazon Cognito Identity User Pool.
    
    ServerSideTokenCheck (boolean) --TRUE if server-side token validation is enabled for the identity providers token.
    
    
    
    
    
    SamlProviderARNs (list) -- An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.
    
    (string) --
    
    
    
    """
    pass

def delete_identities(IdentityIdsToDelete=None):
    """
    Deletes identities from an identity pool. You can specify a list of 1-60 identities that you want to delete.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_identities(
        IdentityIdsToDelete=[
            'string',
        ]
    )
    
    
    :type IdentityIdsToDelete: list
    :param IdentityIdsToDelete: [REQUIRED]
            A list of 1-60 identities that you want to delete.
            (string) --
            

    :rtype: dict
    :return: {
        'UnprocessedIdentityIds': [
            {
                'IdentityId': 'string',
                'ErrorCode': 'AccessDenied'|'InternalServerError'
            },
        ]
    }
    
    
    """
    pass

def delete_identity_pool(IdentityPoolId=None):
    """
    Deletes a user pool. Once a pool is deleted, users will not be able to authenticate with the pool.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_identity_pool(
        IdentityPoolId='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            

    """
    pass

def describe_identity(IdentityId=None):
    """
    Returns metadata related to the given identity, including when the identity was created and any associated linked logins.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_identity(
        IdentityId='string'
    )
    
    
    :type IdentityId: string
    :param IdentityId: [REQUIRED]
            A unique identifier in the format REGION:GUID.
            

    :rtype: dict
    :return: {
        'IdentityId': 'string',
        'Logins': [
            'string',
        ],
        'CreationDate': datetime(2015, 1, 1),
        'LastModifiedDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_identity_pool(IdentityPoolId=None):
    """
    Gets details about a particular identity pool, including the pool name, ID description, creation date, and current number of users.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_identity_pool(
        IdentityPoolId='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            

    :rtype: dict
    :return: {
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
                'ClientId': 'string',
                'ServerSideTokenCheck': True|False
            },
        ],
        'SamlProviderARNs': [
            'string',
        ]
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

def get_credentials_for_identity(IdentityId=None, Logins=None, CustomRoleArn=None):
    """
    Returns credentials for the provided identity ID. Any provided logins will be validated against supported login providers. If the token is for cognito-identity.amazonaws.com, it will be passed through to AWS Security Token Service with the appropriate role for the token.
    This is a public API. You do not need any credentials to call this API.
    See also: AWS API Documentation
    
    
    :example: response = client.get_credentials_for_identity(
        IdentityId='string',
        Logins={
            'string': 'string'
        },
        CustomRoleArn='string'
    )
    
    
    :type IdentityId: string
    :param IdentityId: [REQUIRED]
            A unique identifier in the format REGION:GUID.
            

    :type Logins: dict
    :param Logins: A set of optional name-value pairs that map provider names to provider tokens.
            (string) --
            (string) --
            

    :type CustomRoleArn: string
    :param CustomRoleArn: The Amazon Resource Name (ARN) of the role to be assumed when multiple roles were received in the token from the identity provider. For example, a SAML-based identity provider. This parameter is optional for identity providers that do not support role customization.

    :rtype: dict
    :return: {
        'IdentityId': 'string',
        'Credentials': {
            'AccessKeyId': 'string',
            'SecretKey': 'string',
            'SessionToken': 'string',
            'Expiration': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_id(AccountId=None, IdentityPoolId=None, Logins=None):
    """
    Generates (or retrieves) a Cognito ID. Supplying multiple logins will create an implicit linked account.
    This is a public API. You do not need any credentials to call this API.
    See also: AWS API Documentation
    
    
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
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            

    :type Logins: dict
    :param Logins: A set of optional name-value pairs that map provider names to provider tokens. The available provider names for Logins are as follows:
            Facebook: graph.facebook.com
            Amazon Cognito Identity Provider: cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789
            Google: accounts.google.com
            Amazon: www.amazon.com
            Twitter: api.twitter.com
            Digits: www.digits.com
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'IdentityId': 'string'
    }
    
    
    """
    pass

def get_identity_pool_roles(IdentityPoolId=None):
    """
    Gets the roles for an identity pool.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    
    :example: response = client.get_identity_pool_roles(
        IdentityPoolId='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            

    :rtype: dict
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
    
    
    """
    pass

def get_open_id_token(IdentityId=None, Logins=None):
    """
    Gets an OpenID token, using a known Cognito ID. This known Cognito ID is returned by  GetId . You can optionally add additional logins for the identity. Supplying multiple logins creates an implicit link.
    The OpenId token is valid for 15 minutes.
    This is a public API. You do not need any credentials to call this API.
    See also: AWS API Documentation
    
    
    :example: response = client.get_open_id_token(
        IdentityId='string',
        Logins={
            'string': 'string'
        }
    )
    
    
    :type IdentityId: string
    :param IdentityId: [REQUIRED]
            A unique identifier in the format REGION:GUID.
            

    :type Logins: dict
    :param Logins: A set of optional name-value pairs that map provider names to provider tokens. When using graph.facebook.com and www.amazon.com, supply the access_token returned from the provider's authflow. For accounts.google.com, an Amazon Cognito Identity Provider, or any other OpenId Connect provider, always include the id_token .
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'IdentityId': 'string',
        'Token': 'string'
    }
    
    
    """
    pass

def get_open_id_token_for_developer_identity(IdentityPoolId=None, IdentityId=None, Logins=None, TokenDuration=None):
    """
    Registers (or retrieves) a Cognito IdentityId and an OpenID Connect token for a user authenticated by your backend authentication process. Supplying multiple logins will create an implicit linked account. You can only specify one developer provider as part of the Logins map, which is linked to the identity pool. The developer provider is the "domain" by which Cognito will refer to your users.
    You can use GetOpenIdTokenForDeveloperIdentity to create a new identity and to link new logins (that is, user credentials issued by a public provider or developer provider) to an existing identity. When you want to create a new identity, the IdentityId should be null. When you want to associate a new login with an existing authenticated/unauthenticated identity, you can do so by providing the existing IdentityId . This API will create the identity in the specified IdentityPoolId .
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    
    :example: response = client.get_open_id_token_for_developer_identity(
        IdentityPoolId='string',
        IdentityId='string',
        Logins={
            'string': 'string'
        },
        TokenDuration=123
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            

    :type IdentityId: string
    :param IdentityId: A unique identifier in the format REGION:GUID.

    :type Logins: dict
    :param Logins: [REQUIRED]
            A set of optional name-value pairs that map provider names to provider tokens. Each name-value pair represents a user from a public provider or developer provider. If the user is from a developer provider, the name-value pair will follow the syntax 'developer_provider_name': 'developer_user_identifier' . The developer provider is the 'domain' by which Cognito will refer to your users; you provided this domain while creating/updating the identity pool. The developer user identifier is an identifier from your backend that uniquely identifies a user. When you create an identity pool, you can specify the supported logins.
            (string) --
            (string) --
            

    :type TokenDuration: integer
    :param TokenDuration: The expiration time of the token, in seconds. You can specify a custom expiration time for the token so that you can cache it. If you don't provide an expiration time, the token is valid for 15 minutes. You can exchange the token with Amazon STS for temporary AWS credentials, which are valid for a maximum of one hour. The maximum token duration you can set is 24 hours. You should take care in setting the expiration time for a token, as there are significant security implications: an attacker could use a leaked token to access your AWS resources for the token's duration.

    :rtype: dict
    :return: {
        'IdentityId': 'string',
        'Token': 'string'
    }
    
    
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

def list_identities(IdentityPoolId=None, MaxResults=None, NextToken=None, HideDisabled=None):
    """
    Lists the identities in a pool.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    
    :example: response = client.list_identities(
        IdentityPoolId='string',
        MaxResults=123,
        NextToken='string',
        HideDisabled=True|False
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            

    :type MaxResults: integer
    :param MaxResults: [REQUIRED]
            The maximum number of identities to return.
            

    :type NextToken: string
    :param NextToken: A pagination token.

    :type HideDisabled: boolean
    :param HideDisabled: An optional boolean parameter that allows you to hide disabled identities. If omitted, the ListIdentities API will include disabled identities in the response.

    :rtype: dict
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
    
    
    :example: response = client.list_identity_pools(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: [REQUIRED]
            The maximum number of identities to return.
            

    :type NextToken: string
    :param NextToken: A pagination token.

    :rtype: dict
    :return: {
        'IdentityPools': [
            {
                'IdentityPoolId': 'string',
                'IdentityPoolName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def lookup_developer_identity(IdentityPoolId=None, IdentityId=None, DeveloperUserIdentifier=None, MaxResults=None, NextToken=None):
    """
    Retrieves the IdentityID associated with a DeveloperUserIdentifier or the list of DeveloperUserIdentifier s associated with an IdentityId for an existing identity. Either IdentityID or DeveloperUserIdentifier must not be null. If you supply only one of these values, the other value will be searched in the database and returned as a part of the response. If you supply both, DeveloperUserIdentifier will be matched against IdentityID . If the values are verified against the database, the response returns both values and is the same as the request. Otherwise a ResourceConflictException is thrown.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    
    :example: response = client.lookup_developer_identity(
        IdentityPoolId='string',
        IdentityId='string',
        DeveloperUserIdentifier='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            

    :type IdentityId: string
    :param IdentityId: A unique identifier in the format REGION:GUID.

    :type DeveloperUserIdentifier: string
    :param DeveloperUserIdentifier: A unique ID used by your backend authentication process to identify a user. Typically, a developer identity provider would issue many developer user identifiers, in keeping with the number of users.

    :type MaxResults: integer
    :param MaxResults: The maximum number of identities to return.

    :type NextToken: string
    :param NextToken: A pagination token. The first call you make will have NextToken set to null. After that the service will return NextToken values as needed. For example, let's say you make a request with MaxResults set to 10, and there are 20 matches in the database. The service will return a pagination token as a part of the response. This token can be used to call the API again and get results starting from the 11th match.

    :rtype: dict
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
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    
    :example: response = client.merge_developer_identities(
        SourceUserIdentifier='string',
        DestinationUserIdentifier='string',
        DeveloperProviderName='string',
        IdentityPoolId='string'
    )
    
    
    :type SourceUserIdentifier: string
    :param SourceUserIdentifier: [REQUIRED]
            User identifier for the source user. The value should be a DeveloperUserIdentifier .
            

    :type DestinationUserIdentifier: string
    :param DestinationUserIdentifier: [REQUIRED]
            User identifier for the destination user. The value should be a DeveloperUserIdentifier .
            

    :type DeveloperProviderName: string
    :param DeveloperProviderName: [REQUIRED]
            The 'domain' by which Cognito will refer to your users. This is a (pseudo) domain name that you provide while creating an identity pool. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the DeveloperProviderName , you can use letters as well as period (.), underscore (_), and dash (-).
            

    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            

    :rtype: dict
    :return: {
        'IdentityId': 'string'
    }
    
    
    """
    pass

def set_identity_pool_roles(IdentityPoolId=None, Roles=None, RoleMappings=None):
    """
    Sets the roles for an identity pool. These roles are used when making calls to  GetCredentialsForIdentity action.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    
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
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            

    :type Roles: dict
    :param Roles: [REQUIRED]
            The map of roles associated with this pool. For a given role, the key will be either 'authenticated' or 'unauthenticated' and the value will be the Role ARN.
            (string) --
            (string) --
            

    :type RoleMappings: dict
    :param RoleMappings: How users for a specific identity provider are to mapped to roles. This is a string to RoleMapping object map. The string identifies the identity provider, for example, 'graph.facebook.com' or 'cognito-idp-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id'.
            Up to 25 rules can be specified per identity provider.
            (string) --
            (dict) --A role mapping.
            Type (string) -- [REQUIRED]The role mapping type. Token will use cognito:roles and cognito:preferred_role claims from the Cognito identity provider token to map groups to roles. Rules will attempt to match claims from the token to map to a role.
            AmbiguousRoleResolution (string) --If you specify Token or Rules as the Type , AmbiguousRoleResolution is required.
            Specifies the action to be taken if either no rules match the claim value for the Rules type, or there is no cognito:preferred_role claim and there are multiple cognito:roles matches for the Token type.
            RulesConfiguration (dict) --The rules to be used for mapping users to roles.
            If you specify Rules as the role mapping type, RulesConfiguration is required.
            Rules (list) -- [REQUIRED]An array of rules. You can specify up to 25 rules per identity provider.
            Rules are evaluated in order. The first one to match specifies the role.
            (dict) --A rule that maps a claim name, a claim value, and a match type to a role ARN.
            Claim (string) -- [REQUIRED]The claim name that must be present in the token, for example, 'isAdmin' or 'paid'.
            MatchType (string) -- [REQUIRED]The match condition that specifies how closely the claim value in the IdP token must match Value .
            Value (string) -- [REQUIRED]A brief string that the claim must match, for example, 'paid' or 'yes'.
            RoleARN (string) -- [REQUIRED]The role ARN.
            
            
            
            

    """
    pass

def unlink_developer_identity(IdentityId=None, IdentityPoolId=None, DeveloperProviderName=None, DeveloperUserIdentifier=None):
    """
    Unlinks a DeveloperUserIdentifier from an existing identity. Unlinked developer users will be considered new identities next time they are seen. If, for a given Cognito identity, you remove all federated identities as well as the developer user identifier, the Cognito identity becomes inaccessible.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    
    :example: response = client.unlink_developer_identity(
        IdentityId='string',
        IdentityPoolId='string',
        DeveloperProviderName='string',
        DeveloperUserIdentifier='string'
    )
    
    
    :type IdentityId: string
    :param IdentityId: [REQUIRED]
            A unique identifier in the format REGION:GUID.
            

    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            

    :type DeveloperProviderName: string
    :param DeveloperProviderName: [REQUIRED]
            The 'domain' by which Cognito will refer to your users.
            

    :type DeveloperUserIdentifier: string
    :param DeveloperUserIdentifier: [REQUIRED]
            A unique ID used by your backend authentication process to identify a user.
            

    """
    pass

def unlink_identity(IdentityId=None, Logins=None, LoginsToRemove=None):
    """
    Unlinks a federated identity from an existing account. Unlinked logins will be considered new identities next time they are seen. Removing the last linked login will make this identity inaccessible.
    This is a public API. You do not need any credentials to call this API.
    See also: AWS API Documentation
    
    
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
    :param IdentityId: [REQUIRED]
            A unique identifier in the format REGION:GUID.
            

    :type Logins: dict
    :param Logins: [REQUIRED]
            A set of optional name-value pairs that map provider names to provider tokens.
            (string) --
            (string) --
            

    :type LoginsToRemove: list
    :param LoginsToRemove: [REQUIRED]
            Provider names to unlink from this identity.
            (string) --
            

    """
    pass

def update_identity_pool(IdentityPoolId=None, IdentityPoolName=None, AllowUnauthenticatedIdentities=None, SupportedLoginProviders=None, DeveloperProviderName=None, OpenIdConnectProviderARNs=None, CognitoIdentityProviders=None, SamlProviderARNs=None):
    """
    Updates a user pool.
    You must use AWS Developer credentials to call this API.
    See also: AWS API Documentation
    
    
    :example: response = client.update_identity_pool(
        IdentityPoolId='string',
        IdentityPoolName='string',
        AllowUnauthenticatedIdentities=True|False,
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
        ]
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]
            An identity pool ID in the format REGION:GUID.
            

    :type IdentityPoolName: string
    :param IdentityPoolName: [REQUIRED]
            A string that you provide.
            

    :type AllowUnauthenticatedIdentities: boolean
    :param AllowUnauthenticatedIdentities: [REQUIRED]
            TRUE if the identity pool supports unauthenticated logins.
            

    :type SupportedLoginProviders: dict
    :param SupportedLoginProviders: Optional key:value pairs mapping provider names to provider app IDs.
            (string) --
            (string) --
            

    :type DeveloperProviderName: string
    :param DeveloperProviderName: The 'domain' by which Cognito will refer to your users.

    :type OpenIdConnectProviderARNs: list
    :param OpenIdConnectProviderARNs: A list of OpendID Connect provider ARNs.
            (string) --
            

    :type CognitoIdentityProviders: list
    :param CognitoIdentityProviders: A list representing an Amazon Cognito Identity User Pool and its client ID.
            (dict) --A provider representing an Amazon Cognito Identity User Pool and its client ID.
            ProviderName (string) --The provider name for an Amazon Cognito Identity User Pool. For example, cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789 .
            ClientId (string) --The client ID for the Amazon Cognito Identity User Pool.
            ServerSideTokenCheck (boolean) --TRUE if server-side token validation is enabled for the identity provider s token.
            
            

    :type SamlProviderARNs: list
    :param SamlProviderARNs: An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.
            (string) --
            

    :rtype: dict
    :return: {
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
                'ClientId': 'string',
                'ServerSideTokenCheck': True|False
            },
        ],
        'SamlProviderARNs': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

