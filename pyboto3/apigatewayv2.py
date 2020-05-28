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

def create_api(ApiKeySelectionExpression=None, CorsConfiguration=None, CredentialsArn=None, Description=None, DisableSchemaValidation=None, Name=None, ProtocolType=None, RouteKey=None, RouteSelectionExpression=None, Tags=None, Target=None, Version=None):
    """
    Creates an Api resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_api(
        ApiKeySelectionExpression='string',
        CorsConfiguration={
            'AllowCredentials': True|False,
            'AllowHeaders': [
                'string',
            ],
            'AllowMethods': [
                'string',
            ],
            'AllowOrigins': [
                'string',
            ],
            'ExposeHeaders': [
                'string',
            ],
            'MaxAge': 123
        },
        CredentialsArn='string',
        Description='string',
        DisableSchemaValidation=True|False,
        Name='string',
        ProtocolType='WEBSOCKET'|'HTTP',
        RouteKey='string',
        RouteSelectionExpression='string',
        Tags={
            'string': 'string'
        },
        Target='string',
        Version='string'
    )
    
    
    :type ApiKeySelectionExpression: string
    :param ApiKeySelectionExpression: An API key selection expression. Supported only for WebSocket APIs. See API Key Selection Expressions .

    :type CorsConfiguration: dict
    :param CorsConfiguration: A CORS configuration. Supported only for HTTP APIs. See Configuring CORS for more information.\n\nAllowCredentials (boolean) --Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.\n\nAllowHeaders (list) --Represents a collection of allowed headers. Supported only for HTTP APIs.\n\n(string) --\n\n\nAllowMethods (list) --Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.\n\n(string) --A string with a length between [1-64].\n\n\n\nAllowOrigins (list) --Represents a collection of allowed origins. Supported only for HTTP APIs.\n\n(string) --\n\n\nExposeHeaders (list) --Represents a collection of exposed headers. Supported only for HTTP APIs.\n\n(string) --\n\n\nMaxAge (integer) --The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.\n\n\n

    :type CredentialsArn: string
    :param CredentialsArn: This property is part of quick create. It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To require that the caller\'s identity be passed through from the request, specify arn:aws:iam:::user/. To use resource-based permissions on supported AWS services, specify null. Currently, this property is not used for HTTP integrations. Supported only for HTTP APIs.

    :type Description: string
    :param Description: The description of the API.

    :type DisableSchemaValidation: boolean
    :param DisableSchemaValidation: Avoid validating models when creating a deployment. Supported only for WebSocket APIs.

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the API.\n

    :type ProtocolType: string
    :param ProtocolType: [REQUIRED]\nThe API protocol.\n

    :type RouteKey: string
    :param RouteKey: This property is part of quick create. If you don\'t specify a routeKey, a default route of $default is created. The $default route acts as a catch-all for any request made to your API, for a particular stage. The $default route key can\'t be modified. You can add routes after creating the API, and you can update the route keys of additional routes. Supported only for HTTP APIs.

    :type RouteSelectionExpression: string
    :param RouteSelectionExpression: The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.

    :type Tags: dict
    :param Tags: The collection of tags. Each tag element is associated with a given resource.\n\n(string) --\n(string) --A string with a length between [0-1600].\n\n\n\n\n

    :type Target: string
    :param Target: This property is part of quick create. Quick create produces an API with an integration, a default catch-all route, and a default stage which is configured to automatically deploy changes. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. Supported only for HTTP APIs.

    :type Version: string
    :param Version: A version identifier for the API.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiEndpoint': 'string',
    'ApiId': 'string',
    'ApiKeySelectionExpression': 'string',
    'CorsConfiguration': {
        'AllowCredentials': True|False,
        'AllowHeaders': [
            'string',
        ],
        'AllowMethods': [
            'string',
        ],
        'AllowOrigins': [
            'string',
        ],
        'ExposeHeaders': [
            'string',
        ],
        'MaxAge': 123
    },
    'CreatedDate': datetime(2015, 1, 1),
    'Description': 'string',
    'DisableSchemaValidation': True|False,
    'ImportInfo': [
        'string',
    ],
    'Name': 'string',
    'ProtocolType': 'WEBSOCKET'|'HTTP',
    'RouteSelectionExpression': 'string',
    'Tags': {
        'string': 'string'
    },
    'Version': 'string',
    'Warnings': [
        'string',
    ]
}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.

ApiEndpoint (string) --
The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage.

ApiId (string) --
The API ID.

ApiKeySelectionExpression (string) --
An API key selection expression. Supported only for WebSocket APIs. See API Key Selection Expressions .

CorsConfiguration (dict) --
A CORS configuration. Supported only for HTTP APIs.

AllowCredentials (boolean) --
Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.

AllowHeaders (list) --
Represents a collection of allowed headers. Supported only for HTTP APIs.

(string) --


AllowMethods (list) --
Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.

(string) --
A string with a length between [1-64].



AllowOrigins (list) --
Represents a collection of allowed origins. Supported only for HTTP APIs.

(string) --


ExposeHeaders (list) --
Represents a collection of exposed headers. Supported only for HTTP APIs.

(string) --


MaxAge (integer) --
The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.



CreatedDate (datetime) --
The timestamp when the API was created.

Description (string) --
The description of the API.

DisableSchemaValidation (boolean) --
Avoid validating models when creating a deployment. Supported only for WebSocket APIs.

ImportInfo (list) --
The validation information during API import. This may include particular properties of your OpenAPI definition which are ignored during import. Supported only for HTTP APIs.

(string) --


Name (string) --
The name of the API.

ProtocolType (string) --
The API protocol.

RouteSelectionExpression (string) --
The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.

Tags (dict) --
A collection of tags associated with the API.

(string) --

(string) --
A string with a length between [0-1600].





Version (string) --
A version identifier for the API.

Warnings (list) --
The warning messages reported when failonwarnings is turned on during API import.

(string) --








Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ApiEndpoint': 'string',
        'ApiId': 'string',
        'ApiKeySelectionExpression': 'string',
        'CorsConfiguration': {
            'AllowCredentials': True|False,
            'AllowHeaders': [
                'string',
            ],
            'AllowMethods': [
                'string',
            ],
            'AllowOrigins': [
                'string',
            ],
            'ExposeHeaders': [
                'string',
            ],
            'MaxAge': 123
        },
        'CreatedDate': datetime(2015, 1, 1),
        'Description': 'string',
        'DisableSchemaValidation': True|False,
        'ImportInfo': [
            'string',
        ],
        'Name': 'string',
        'ProtocolType': 'WEBSOCKET'|'HTTP',
        'RouteSelectionExpression': 'string',
        'Tags': {
            'string': 'string'
        },
        'Version': 'string',
        'Warnings': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_api_mapping(ApiId=None, ApiMappingKey=None, DomainName=None, Stage=None):
    """
    Creates an API mapping.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_api_mapping(
        ApiId='string',
        ApiMappingKey='string',
        DomainName='string',
        Stage='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ApiMappingKey: string
    :param ApiMappingKey: The API mapping key.

    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe domain name.\n

    :type Stage: string
    :param Stage: [REQUIRED]\nThe API stage.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiId': 'string',
    'ApiMappingId': 'string',
    'ApiMappingKey': 'string',
    'Stage': 'string'
}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.

ApiId (string) --
The API identifier.

ApiMappingId (string) --
The API mapping identifier.

ApiMappingKey (string) --
The API mapping key.

Stage (string) --
The API stage.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ApiId': 'string',
        'ApiMappingId': 'string',
        'ApiMappingKey': 'string',
        'Stage': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def create_authorizer(ApiId=None, AuthorizerCredentialsArn=None, AuthorizerResultTtlInSeconds=None, AuthorizerType=None, AuthorizerUri=None, IdentitySource=None, IdentityValidationExpression=None, JwtConfiguration=None, Name=None):
    """
    Creates an Authorizer for an API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_authorizer(
        ApiId='string',
        AuthorizerCredentialsArn='string',
        AuthorizerResultTtlInSeconds=123,
        AuthorizerType='REQUEST'|'JWT',
        AuthorizerUri='string',
        IdentitySource=[
            'string',
        ],
        IdentityValidationExpression='string',
        JwtConfiguration={
            'Audience': [
                'string',
            ],
            'Issuer': 'string'
        },
        Name='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type AuthorizerCredentialsArn: string
    :param AuthorizerCredentialsArn: Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null. Supported only for REQUEST authorizers.

    :type AuthorizerResultTtlInSeconds: integer
    :param AuthorizerResultTtlInSeconds: Authorizer caching is not currently supported. Don\'t specify this value for authorizers.

    :type AuthorizerType: string
    :param AuthorizerType: [REQUIRED]\nThe authorizer type. For WebSocket APIs, specify REQUEST for a Lambda function using incoming request parameters. For HTTP APIs, specify JWT to use JSON Web Tokens.\n

    :type AuthorizerUri: string
    :param AuthorizerUri: The authorizer\'s Uniform Resource Identifier (URI). For REQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations. In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api}, where {region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations. Supported only for REQUEST authorizers.

    :type IdentitySource: list
    :param IdentitySource: [REQUIRED]\nThe identity source for which authorization is requested.\nFor a REQUEST authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. Currently, the identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name. These parameters will be used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function.\nFor JWT, a single entry that specifies where to extract the JSON Web Token (JWT )from inbound requests. Currently only header-based and query parameter-based selections are supported, for example '$request.header.Authorization'.\n\n(string) --\n\n

    :type IdentityValidationExpression: string
    :param IdentityValidationExpression: This parameter is not used.

    :type JwtConfiguration: dict
    :param JwtConfiguration: Represents the configuration of a JWT authorizer. Required for the JWT authorizer type. Supported only for HTTP APIs.\n\nAudience (list) --A list of the intended recipients of the JWT. A valid JWT must provide an aud that matches at least one entry in this list. See RFC 7519 . Supported only for HTTP APIs.\n\n(string) --\n\n\nIssuer (string) --The base domain of the identity provider that issues JSON Web Tokens. For example, an Amazon Cognito user pool has the following format: https://cognito-idp.{region}.amazonaws.com/{userPoolId}. Required for the JWT authorizer type. Supported only for HTTP APIs.\n\n\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the authorizer.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AuthorizerCredentialsArn': 'string',
    'AuthorizerId': 'string',
    'AuthorizerResultTtlInSeconds': 123,
    'AuthorizerType': 'REQUEST'|'JWT',
    'AuthorizerUri': 'string',
    'IdentitySource': [
        'string',
    ],
    'IdentityValidationExpression': 'string',
    'JwtConfiguration': {
        'Audience': [
            'string',
        ],
        'Issuer': 'string'
    },
    'Name': 'string'
}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.

AuthorizerCredentialsArn (string) --
Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null. Supported only for REQUEST authorizers.

AuthorizerId (string) --
The authorizer identifier.

AuthorizerResultTtlInSeconds (integer) --
Authorizer caching is not currently supported. Don\'t specify this value for authorizers.

AuthorizerType (string) --
The authorizer type. For WebSocket APIs, specify REQUEST for a Lambda function using incoming request parameters. For HTTP APIs, specify JWT to use JSON Web Tokens.

AuthorizerUri (string) --
The authorizer\'s Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations. In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api}, where {region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations. Supported only for REQUEST authorizers.

IdentitySource (list) --
The identity source for which authorization is requested.
For a REQUEST authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. Currently, the identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name. These parameters will be used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function.
For JWT, a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example "$request.header.Authorization".

(string) --


IdentityValidationExpression (string) --
The validation expression does not apply to the REQUEST authorizer.

JwtConfiguration (dict) --
Represents the configuration of a JWT authorizer. Required for the JWT authorizer type. Supported only for HTTP APIs.

Audience (list) --
A list of the intended recipients of the JWT. A valid JWT must provide an aud that matches at least one entry in this list. See RFC 7519 . Supported only for HTTP APIs.

(string) --


Issuer (string) --
The base domain of the identity provider that issues JSON Web Tokens. For example, an Amazon Cognito user pool has the following format: https://cognito-idp.{region}.amazonaws.com/{userPoolId}. Required for the JWT authorizer type. Supported only for HTTP APIs.



Name (string) --
The name of the authorizer.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'AuthorizerCredentialsArn': 'string',
        'AuthorizerId': 'string',
        'AuthorizerResultTtlInSeconds': 123,
        'AuthorizerType': 'REQUEST'|'JWT',
        'AuthorizerUri': 'string',
        'IdentitySource': [
            'string',
        ],
        'IdentityValidationExpression': 'string',
        'JwtConfiguration': {
            'Audience': [
                'string',
            ],
            'Issuer': 'string'
        },
        'Name': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_deployment(ApiId=None, Description=None, StageName=None):
    """
    Creates a Deployment for an API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_deployment(
        ApiId='string',
        Description='string',
        StageName='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type Description: string
    :param Description: The description for the deployment resource.

    :type StageName: string
    :param StageName: The name of the Stage resource for the Deployment resource to create.

    :rtype: dict

ReturnsResponse Syntax
{
    'AutoDeployed': True|False,
    'CreatedDate': datetime(2015, 1, 1),
    'DeploymentId': 'string',
    'DeploymentStatus': 'PENDING'|'FAILED'|'DEPLOYED',
    'DeploymentStatusMessage': 'string',
    'Description': 'string'
}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.

AutoDeployed (boolean) --
Specifies whether a deployment was automatically released.

CreatedDate (datetime) --
The date and time when the Deployment resource was created.

DeploymentId (string) --
The identifier for the deployment.

DeploymentStatus (string) --
The status of the deployment: PENDING, FAILED, or SUCCEEDED.

DeploymentStatusMessage (string) --
May contain additional feedback on the status of an API deployment.

Description (string) --
The description for the deployment.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'AutoDeployed': True|False,
        'CreatedDate': datetime(2015, 1, 1),
        'DeploymentId': 'string',
        'DeploymentStatus': 'PENDING'|'FAILED'|'DEPLOYED',
        'DeploymentStatusMessage': 'string',
        'Description': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def create_domain_name(DomainName=None, DomainNameConfigurations=None, Tags=None):
    """
    Creates a domain name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_domain_name(
        DomainName='string',
        DomainNameConfigurations=[
            {
                'ApiGatewayDomainName': 'string',
                'CertificateArn': 'string',
                'CertificateName': 'string',
                'CertificateUploadDate': datetime(2015, 1, 1),
                'DomainNameStatus': 'AVAILABLE'|'UPDATING',
                'DomainNameStatusMessage': 'string',
                'EndpointType': 'REGIONAL'|'EDGE',
                'HostedZoneId': 'string',
                'SecurityPolicy': 'TLS_1_0'|'TLS_1_2'
            },
        ],
        Tags={
            'string': 'string'
        }
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe domain name.\n

    :type DomainNameConfigurations: list
    :param DomainNameConfigurations: The domain name configurations.\n\n(dict) --The domain name configuration.\n\nApiGatewayDomainName (string) --A domain name for the API.\n\nCertificateArn (string) --An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.\n\nCertificateName (string) --The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.\n\nCertificateUploadDate (datetime) --The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.\n\nDomainNameStatus (string) --The status of the domain name migration. The valid values are AVAILABLE and UPDATING. If the status is UPDATING, the domain cannot be modified further until the existing operation is complete. If it is AVAILABLE, the domain can be updated.\n\nDomainNameStatusMessage (string) --An optional text message containing detailed information about status of the domain name migration.\n\nEndpointType (string) --The endpoint type.\n\nHostedZoneId (string) --The Amazon Route 53 Hosted Zone ID of the endpoint.\n\nSecurityPolicy (string) --The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are TLS_1_0 and TLS_1_2.\n\n\n\n\n

    :type Tags: dict
    :param Tags: The collection of tags associated with a domain name.\n\n(string) --\n(string) --A string with a length between [0-1600].\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiMappingSelectionExpression': 'string',
    'DomainName': 'string',
    'DomainNameConfigurations': [
        {
            'ApiGatewayDomainName': 'string',
            'CertificateArn': 'string',
            'CertificateName': 'string',
            'CertificateUploadDate': datetime(2015, 1, 1),
            'DomainNameStatus': 'AVAILABLE'|'UPDATING',
            'DomainNameStatusMessage': 'string',
            'EndpointType': 'REGIONAL'|'EDGE',
            'HostedZoneId': 'string',
            'SecurityPolicy': 'TLS_1_0'|'TLS_1_2'
        },
    ],
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.

ApiMappingSelectionExpression (string) --
The API mapping selection expression.

DomainName (string) --
The name of the DomainName resource.

DomainNameConfigurations (list) --
The domain name configurations.

(dict) --
The domain name configuration.

ApiGatewayDomainName (string) --
A domain name for the API.

CertificateArn (string) --
An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.

CertificateName (string) --
The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.

CertificateUploadDate (datetime) --
The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.

DomainNameStatus (string) --
The status of the domain name migration. The valid values are AVAILABLE and UPDATING. If the status is UPDATING, the domain cannot be modified further until the existing operation is complete. If it is AVAILABLE, the domain can be updated.

DomainNameStatusMessage (string) --
An optional text message containing detailed information about status of the domain name migration.

EndpointType (string) --
The endpoint type.

HostedZoneId (string) --
The Amazon Route 53 Hosted Zone ID of the endpoint.

SecurityPolicy (string) --
The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are TLS_1_0 and TLS_1_2.





Tags (dict) --
The collection of tags associated with a domain name.

(string) --

(string) --
A string with a length between [0-1600].











Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException
ApiGatewayV2.Client.exceptions.AccessDeniedException


    :return: {
        'ApiMappingSelectionExpression': 'string',
        'DomainName': 'string',
        'DomainNameConfigurations': [
            {
                'ApiGatewayDomainName': 'string',
                'CertificateArn': 'string',
                'CertificateName': 'string',
                'CertificateUploadDate': datetime(2015, 1, 1),
                'DomainNameStatus': 'AVAILABLE'|'UPDATING',
                'DomainNameStatusMessage': 'string',
                'EndpointType': 'REGIONAL'|'EDGE',
                'HostedZoneId': 'string',
                'SecurityPolicy': 'TLS_1_0'|'TLS_1_2'
            },
        ],
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    ApiGatewayV2.Client.exceptions.AccessDeniedException
    
    """
    pass

def create_integration(ApiId=None, ConnectionId=None, ConnectionType=None, ContentHandlingStrategy=None, CredentialsArn=None, Description=None, IntegrationMethod=None, IntegrationType=None, IntegrationUri=None, PassthroughBehavior=None, PayloadFormatVersion=None, RequestParameters=None, RequestTemplates=None, TemplateSelectionExpression=None, TimeoutInMillis=None, TlsConfig=None):
    """
    Creates an Integration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_integration(
        ApiId='string',
        ConnectionId='string',
        ConnectionType='INTERNET'|'VPC_LINK',
        ContentHandlingStrategy='CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
        CredentialsArn='string',
        Description='string',
        IntegrationMethod='string',
        IntegrationType='AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
        IntegrationUri='string',
        PassthroughBehavior='WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
        PayloadFormatVersion='string',
        RequestParameters={
            'string': 'string'
        },
        RequestTemplates={
            'string': 'string'
        },
        TemplateSelectionExpression='string',
        TimeoutInMillis=123,
        TlsConfig={
            'ServerNameToVerify': 'string'
        }
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ConnectionId: string
    :param ConnectionId: The ID of the VPC link for a private integration. Supported only for HTTP APIs.

    :type ConnectionType: string
    :param ConnectionType: The type of the network connection to the integration endpoint. Specify INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and resources in a VPC. The default value is INTERNET.

    :type ContentHandlingStrategy: string
    :param ContentHandlingStrategy: Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:\nCONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.\nCONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.\nIf this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.\n

    :type CredentialsArn: string
    :param CredentialsArn: Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To require that the caller\'s identity be passed through from the request, specify the string arn:aws:iam:::user/. To use resource-based permissions on supported AWS services, specify null.

    :type Description: string
    :param Description: The description of the integration.

    :type IntegrationMethod: string
    :param IntegrationMethod: Specifies the integration\'s HTTP method type.

    :type IntegrationType: string
    :param IntegrationType: [REQUIRED]\nThe integration type of an integration. One of the following:\nAWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs.\nAWS_PROXY: for integrating the route or method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as Lambda proxy integration.\nHTTP: for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs.\nHTTP_PROXY: for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration. For HTTP API private integrations, use an HTTP_PROXY integration.\nMOCK: for integrating the route or method request with API Gateway as a 'loopback' endpoint without invoking any backend. Supported only for WebSocket APIs.\n

    :type IntegrationUri: string
    :param IntegrationUri: For a Lambda integration, specify the URI of a Lambda function.\nFor an HTTP integration, specify a fully-qualified URL.\nFor an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service. If you specify the ARN of an AWS Cloud Map service, API Gateway uses DiscoverInstances to identify resources. You can use query parameters to target specific resources. To learn more, see DiscoverInstances . For private integrations, all resources must be owned by the same AWS account.\n

    :type PassthroughBehavior: string
    :param PassthroughBehavior: Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Supported only for WebSocket APIs.\nWHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.\nNEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.\nWHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.\n

    :type PayloadFormatVersion: string
    :param PayloadFormatVersion: Specifies the format of the payload sent to an integration. Required for HTTP APIs.

    :type RequestParameters: dict
    :param RequestParameters: A key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.{location}.{name}, where {location}is querystring, path, or header; and {name}must be a valid and unique method request parameter name. Supported only for WebSocket APIs.\n\n(string) --\n(string) --A string with a length between [1-512].\n\n\n\n\n

    :type RequestTemplates: dict
    :param RequestTemplates: Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value. Supported only for WebSocket APIs.\n\n(string) --\n(string) --A string with a length between [0-32768].\n\n\n\n\n

    :type TemplateSelectionExpression: string
    :param TemplateSelectionExpression: The template selection expression for the integration.

    :type TimeoutInMillis: integer
    :param TimeoutInMillis: Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.

    :type TlsConfig: dict
    :param TlsConfig: The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.\n\nServerNameToVerify (string) --If you specify a server name, API Gateway uses it to verify the hostname on the integration\'s certificate. The server name is also included in the TLS handshake to support Server Name Indication (SNI) or virtual hosting.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiGatewayManaged': True|False,
    'ConnectionId': 'string',
    'ConnectionType': 'INTERNET'|'VPC_LINK',
    'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
    'CredentialsArn': 'string',
    'Description': 'string',
    'IntegrationId': 'string',
    'IntegrationMethod': 'string',
    'IntegrationResponseSelectionExpression': 'string',
    'IntegrationType': 'AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
    'IntegrationUri': 'string',
    'PassthroughBehavior': 'WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
    'PayloadFormatVersion': 'string',
    'RequestParameters': {
        'string': 'string'
    },
    'RequestTemplates': {
        'string': 'string'
    },
    'TemplateSelectionExpression': 'string',
    'TimeoutInMillis': 123,
    'TlsConfig': {
        'ServerNameToVerify': 'string'
    }
}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.

ApiGatewayManaged (boolean) --
Specifies whether an integration is managed by API Gateway. If you created an API using using quick create, the resulting integration is managed by API Gateway. You can update a managed integration, but you can\'t delete it.

ConnectionId (string) --
The ID of the VPC link for a private integration. Supported only for HTTP APIs.

ConnectionType (string) --
The type of the network connection to the integration endpoint. Specify INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and resources in a VPC. The default value is INTERNET.

ContentHandlingStrategy (string) --
Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.

CredentialsArn (string) --
Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To require that the caller\'s identity be passed through from the request, specify the string arn:aws:iam:::user/. To use resource-based permissions on supported AWS services, specify null.

Description (string) --
Represents the description of an integration.

IntegrationId (string) --
Represents the identifier of an integration.

IntegrationMethod (string) --
Specifies the integration\'s HTTP method type.

IntegrationResponseSelectionExpression (string) --
The integration response selection expression for the integration. Supported only for WebSocket APIs. See Integration Response Selection Expressions .

IntegrationType (string) --
The integration type of an integration. One of the following:
AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs.
AWS_PROXY: for integrating the route or method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as Lambda proxy integration.
HTTP: for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs.
HTTP_PROXY: for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration.
MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend. Supported only for WebSocket APIs.

IntegrationUri (string) --
For a Lambda integration, specify the URI of a Lambda function.
For an HTTP integration, specify a fully-qualified URL.
For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service. If you specify the ARN of an AWS Cloud Map service, API Gateway uses DiscoverInstances to identify resources. You can use query parameters to target specific resources. To learn more, see DiscoverInstances . For private integrations, all resources must be owned by the same AWS account.

PassthroughBehavior (string) --
Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Supported only for WebSocket APIs.
WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.
NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.
WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.

PayloadFormatVersion (string) --
Specifies the format of the payload sent to an integration. Required for HTTP APIs.

RequestParameters (dict) --
A key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.{location}.{name}, where {location}is querystring, path, or header; and {name}must be a valid and unique method request parameter name. Supported only for WebSocket APIs.

(string) --

(string) --
A string with a length between [1-512].





RequestTemplates (dict) --
Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value. Supported only for WebSocket APIs.

(string) --

(string) --
A string with a length between [0-32768].





TemplateSelectionExpression (string) --
The template selection expression for the integration. Supported only for WebSocket APIs.

TimeoutInMillis (integer) --
Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.

TlsConfig (dict) --
The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.

ServerNameToVerify (string) --
If you specify a server name, API Gateway uses it to verify the hostname on the integration\'s certificate. The server name is also included in the TLS handshake to support Server Name Indication (SNI) or virtual hosting.









Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ApiGatewayManaged': True|False,
        'ConnectionId': 'string',
        'ConnectionType': 'INTERNET'|'VPC_LINK',
        'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
        'CredentialsArn': 'string',
        'Description': 'string',
        'IntegrationId': 'string',
        'IntegrationMethod': 'string',
        'IntegrationResponseSelectionExpression': 'string',
        'IntegrationType': 'AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
        'IntegrationUri': 'string',
        'PassthroughBehavior': 'WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
        'PayloadFormatVersion': 'string',
        'RequestParameters': {
            'string': 'string'
        },
        'RequestTemplates': {
            'string': 'string'
        },
        'TemplateSelectionExpression': 'string',
        'TimeoutInMillis': 123,
        'TlsConfig': {
            'ServerNameToVerify': 'string'
        }
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def create_integration_response(ApiId=None, ContentHandlingStrategy=None, IntegrationId=None, IntegrationResponseKey=None, ResponseParameters=None, ResponseTemplates=None, TemplateSelectionExpression=None):
    """
    Creates an IntegrationResponses.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_integration_response(
        ApiId='string',
        ContentHandlingStrategy='CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
        IntegrationId='string',
        IntegrationResponseKey='string',
        ResponseParameters={
            'string': 'string'
        },
        ResponseTemplates={
            'string': 'string'
        },
        TemplateSelectionExpression='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ContentHandlingStrategy: string
    :param ContentHandlingStrategy: Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:\nCONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.\nCONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.\nIf this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.\n

    :type IntegrationId: string
    :param IntegrationId: [REQUIRED]\nThe integration ID.\n

    :type IntegrationResponseKey: string
    :param IntegrationResponseKey: [REQUIRED]\nThe integration response key.\n

    :type ResponseParameters: dict
    :param ResponseParameters: A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where {name} is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where {name} is a valid and unique response header name and {JSON-expression} is a valid JSON expression without the $ prefix.\n\n(string) --\n(string) --A string with a length between [1-512].\n\n\n\n\n

    :type ResponseTemplates: dict
    :param ResponseTemplates: The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.\n\n(string) --\n(string) --A string with a length between [0-32768].\n\n\n\n\n

    :type TemplateSelectionExpression: string
    :param TemplateSelectionExpression: The template selection expression for the integration response. Supported only for WebSocket APIs.

    :rtype: dict

ReturnsResponse Syntax
{
    'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
    'IntegrationResponseId': 'string',
    'IntegrationResponseKey': 'string',
    'ResponseParameters': {
        'string': 'string'
    },
    'ResponseTemplates': {
        'string': 'string'
    },
    'TemplateSelectionExpression': 'string'
}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.

ContentHandlingStrategy (string) --
Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.

IntegrationResponseId (string) --
The integration response ID.

IntegrationResponseKey (string) --
The integration response key.

ResponseParameters (dict) --
A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where name is a valid and unique response header name and JSON-expression is a valid JSON expression without the $ prefix.

(string) --

(string) --
A string with a length between [1-512].





ResponseTemplates (dict) --
The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

(string) --

(string) --
A string with a length between [0-32768].





TemplateSelectionExpression (string) --
The template selection expressions for the integration response.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
        'IntegrationResponseId': 'string',
        'IntegrationResponseKey': 'string',
        'ResponseParameters': {
            'string': 'string'
        },
        'ResponseTemplates': {
            'string': 'string'
        },
        'TemplateSelectionExpression': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def create_model(ApiId=None, ContentType=None, Description=None, Name=None, Schema=None):
    """
    Creates a Model for an API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_model(
        ApiId='string',
        ContentType='string',
        Description='string',
        Name='string',
        Schema='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ContentType: string
    :param ContentType: The content-type for the model, for example, 'application/json'.

    :type Description: string
    :param Description: The description of the model.

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the model. Must be alphanumeric.\n

    :type Schema: string
    :param Schema: [REQUIRED]\nThe schema for the model. For application/json models, this should be JSON schema draft 4 model.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ContentType': 'string',
    'Description': 'string',
    'ModelId': 'string',
    'Name': 'string',
    'Schema': 'string'
}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.

ContentType (string) --
The content-type for the model, for example, "application/json".

Description (string) --
The description of the model.

ModelId (string) --
The model identifier.

Name (string) --
The name of the model. Must be alphanumeric.

Schema (string) --
The schema for the model. For application/json models, this should be JSON schema draft 4 model.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ContentType': 'string',
        'Description': 'string',
        'ModelId': 'string',
        'Name': 'string',
        'Schema': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def create_route(ApiId=None, ApiKeyRequired=None, AuthorizationScopes=None, AuthorizationType=None, AuthorizerId=None, ModelSelectionExpression=None, OperationName=None, RequestModels=None, RequestParameters=None, RouteKey=None, RouteResponseSelectionExpression=None, Target=None):
    """
    Creates a Route for an API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_route(
        ApiId='string',
        ApiKeyRequired=True|False,
        AuthorizationScopes=[
            'string',
        ],
        AuthorizationType='NONE'|'AWS_IAM'|'CUSTOM'|'JWT',
        AuthorizerId='string',
        ModelSelectionExpression='string',
        OperationName='string',
        RequestModels={
            'string': 'string'
        },
        RequestParameters={
            'string': {
                'Required': True|False
            }
        },
        RouteKey='string',
        RouteResponseSelectionExpression='string',
        Target='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ApiKeyRequired: boolean
    :param ApiKeyRequired: Specifies whether an API key is required for the route. Supported only for WebSocket APIs.

    :type AuthorizationScopes: list
    :param AuthorizationScopes: The authorization scopes supported by this route.\n\n(string) --A string with a length between [1-64].\n\n\n

    :type AuthorizationType: string
    :param AuthorizationType: The authorization type for the route. For WebSocket APIs, valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer For HTTP APIs, valid values are NONE for open access, or JWT for using JSON Web Tokens.

    :type AuthorizerId: string
    :param AuthorizerId: The identifier of the Authorizer resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.

    :type ModelSelectionExpression: string
    :param ModelSelectionExpression: The model selection expression for the route. Supported only for WebSocket APIs.

    :type OperationName: string
    :param OperationName: The operation name for the route.

    :type RequestModels: dict
    :param RequestModels: The request models for the route. Supported only for WebSocket APIs.\n\n(string) --\n(string) --A string with a length between [1-128].\n\n\n\n\n

    :type RequestParameters: dict
    :param RequestParameters: The request parameters for the route. Supported only for WebSocket APIs.\n\n(string) --\n(dict) --Validation constraints imposed on parameters of a request (path, query string, headers).\n\nRequired (boolean) --Whether or not the parameter is required.\n\n\n\n\n\n\n

    :type RouteKey: string
    :param RouteKey: [REQUIRED]\nThe route key for the route.\n

    :type RouteResponseSelectionExpression: string
    :param RouteResponseSelectionExpression: The route response selection expression for the route. Supported only for WebSocket APIs.

    :type Target: string
    :param Target: The target for the route.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiGatewayManaged': True|False,
    'ApiKeyRequired': True|False,
    'AuthorizationScopes': [
        'string',
    ],
    'AuthorizationType': 'NONE'|'AWS_IAM'|'CUSTOM'|'JWT',
    'AuthorizerId': 'string',
    'ModelSelectionExpression': 'string',
    'OperationName': 'string',
    'RequestModels': {
        'string': 'string'
    },
    'RequestParameters': {
        'string': {
            'Required': True|False
        }
    },
    'RouteId': 'string',
    'RouteKey': 'string',
    'RouteResponseSelectionExpression': 'string',
    'Target': 'string'
}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.

ApiGatewayManaged (boolean) --
Specifies whether a route is managed by API Gateway. If you created an API using quick create, the $default route is managed by API Gateway. You can\'t modify the $default route key.

ApiKeyRequired (boolean) --
Specifies whether an API key is required for this route. Supported only for WebSocket APIs.

AuthorizationScopes (list) --
A list of authorization scopes configured on a route. The scopes are used with a JWT authorizer to authorize the method invocation. The authorization works by matching the route scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any route scope matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the route scope is configured, the client must provide an access token instead of an identity token for authorization purposes.

(string) --
A string with a length between [1-64].



AuthorizationType (string) --
The authorization type for the route. For WebSocket APIs, valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer For HTTP APIs, valid values are NONE for open access, or JWT for using JSON Web Tokens.

AuthorizerId (string) --
The identifier of the Authorizer resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.

ModelSelectionExpression (string) --
The model selection expression for the route. Supported only for WebSocket APIs.

OperationName (string) --
The operation name for the route.

RequestModels (dict) --
The request models for the route. Supported only for WebSocket APIs.

(string) --

(string) --
A string with a length between [1-128].





RequestParameters (dict) --
The request parameters for the route. Supported only for WebSocket APIs.

(string) --

(dict) --
Validation constraints imposed on parameters of a request (path, query string, headers).

Required (boolean) --
Whether or not the parameter is required.







RouteId (string) --
The route ID.

RouteKey (string) --
The route key for the route.

RouteResponseSelectionExpression (string) --
The route response selection expression for the route. Supported only for WebSocket APIs.

Target (string) --
The target for the route.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ApiGatewayManaged': True|False,
        'ApiKeyRequired': True|False,
        'AuthorizationScopes': [
            'string',
        ],
        'AuthorizationType': 'NONE'|'AWS_IAM'|'CUSTOM'|'JWT',
        'AuthorizerId': 'string',
        'ModelSelectionExpression': 'string',
        'OperationName': 'string',
        'RequestModels': {
            'string': 'string'
        },
        'RequestParameters': {
            'string': {
                'Required': True|False
            }
        },
        'RouteId': 'string',
        'RouteKey': 'string',
        'RouteResponseSelectionExpression': 'string',
        'Target': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def create_route_response(ApiId=None, ModelSelectionExpression=None, ResponseModels=None, ResponseParameters=None, RouteId=None, RouteResponseKey=None):
    """
    Creates a RouteResponse for a Route.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_route_response(
        ApiId='string',
        ModelSelectionExpression='string',
        ResponseModels={
            'string': 'string'
        },
        ResponseParameters={
            'string': {
                'Required': True|False
            }
        },
        RouteId='string',
        RouteResponseKey='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ModelSelectionExpression: string
    :param ModelSelectionExpression: The model selection expression for the route response. Supported only for WebSocket APIs.

    :type ResponseModels: dict
    :param ResponseModels: The response models for the route response.\n\n(string) --\n(string) --A string with a length between [1-128].\n\n\n\n\n

    :type ResponseParameters: dict
    :param ResponseParameters: The route response parameters.\n\n(string) --\n(dict) --Validation constraints imposed on parameters of a request (path, query string, headers).\n\nRequired (boolean) --Whether or not the parameter is required.\n\n\n\n\n\n\n

    :type RouteId: string
    :param RouteId: [REQUIRED]\nThe route ID.\n

    :type RouteResponseKey: string
    :param RouteResponseKey: [REQUIRED]\nThe route response key.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ModelSelectionExpression': 'string',
    'ResponseModels': {
        'string': 'string'
    },
    'ResponseParameters': {
        'string': {
            'Required': True|False
        }
    },
    'RouteResponseId': 'string',
    'RouteResponseKey': 'string'
}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.

ModelSelectionExpression (string) --
Represents the model selection expression of a route response. Supported only for WebSocket APIs.

ResponseModels (dict) --
Represents the response models of a route response.

(string) --

(string) --
A string with a length between [1-128].





ResponseParameters (dict) --
Represents the response parameters of a route response.

(string) --

(dict) --
Validation constraints imposed on parameters of a request (path, query string, headers).

Required (boolean) --
Whether or not the parameter is required.







RouteResponseId (string) --
Represents the identifier of a route response.

RouteResponseKey (string) --
Represents the route response key of a route response.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ModelSelectionExpression': 'string',
        'ResponseModels': {
            'string': 'string'
        },
        'ResponseParameters': {
            'string': {
                'Required': True|False
            }
        },
        'RouteResponseId': 'string',
        'RouteResponseKey': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def create_stage(AccessLogSettings=None, ApiId=None, AutoDeploy=None, ClientCertificateId=None, DefaultRouteSettings=None, DeploymentId=None, Description=None, RouteSettings=None, StageName=None, StageVariables=None, Tags=None):
    """
    Creates a Stage for an API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_stage(
        AccessLogSettings={
            'DestinationArn': 'string',
            'Format': 'string'
        },
        ApiId='string',
        AutoDeploy=True|False,
        ClientCertificateId='string',
        DefaultRouteSettings={
            'DataTraceEnabled': True|False,
            'DetailedMetricsEnabled': True|False,
            'LoggingLevel': 'ERROR'|'INFO'|'OFF',
            'ThrottlingBurstLimit': 123,
            'ThrottlingRateLimit': 123.0
        },
        DeploymentId='string',
        Description='string',
        RouteSettings={
            'string': {
                'DataTraceEnabled': True|False,
                'DetailedMetricsEnabled': True|False,
                'LoggingLevel': 'ERROR'|'INFO'|'OFF',
                'ThrottlingBurstLimit': 123,
                'ThrottlingRateLimit': 123.0
            }
        },
        StageName='string',
        StageVariables={
            'string': 'string'
        },
        Tags={
            'string': 'string'
        }
    )
    
    
    :type AccessLogSettings: dict
    :param AccessLogSettings: Settings for logging access in this stage.\n\nDestinationArn (string) --The ARN of the CloudWatch Logs log group to receive access logs.\n\nFormat (string) --A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.\n\n\n

    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type AutoDeploy: boolean
    :param AutoDeploy: Specifies whether updates to an API automatically trigger a new deployment. The default value is false.

    :type ClientCertificateId: string
    :param ClientCertificateId: The identifier of a client certificate for a Stage. Supported only for WebSocket APIs.

    :type DefaultRouteSettings: dict
    :param DefaultRouteSettings: The default route settings for the stage.\n\nDataTraceEnabled (boolean) --Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.\n\nDetailedMetricsEnabled (boolean) --Specifies whether detailed metrics are enabled.\n\nLoggingLevel (string) --Specifies the logging level for this route: INFO, ERROR, or OFF. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.\n\nThrottlingBurstLimit (integer) --Specifies the throttling burst limit.\n\nThrottlingRateLimit (float) --Specifies the throttling rate limit.\n\n\n

    :type DeploymentId: string
    :param DeploymentId: The deployment identifier of the API stage.

    :type Description: string
    :param Description: The description for the API stage.

    :type RouteSettings: dict
    :param RouteSettings: Route settings for the stage, by routeKey.\n\n(string) --\n(dict) --Represents a collection of route settings.\n\nDataTraceEnabled (boolean) --Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.\n\nDetailedMetricsEnabled (boolean) --Specifies whether detailed metrics are enabled.\n\nLoggingLevel (string) --Specifies the logging level for this route: INFO, ERROR, or OFF. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.\n\nThrottlingBurstLimit (integer) --Specifies the throttling burst limit.\n\nThrottlingRateLimit (float) --Specifies the throttling rate limit.\n\n\n\n\n\n\n

    :type StageName: string
    :param StageName: [REQUIRED]\nThe name of the stage.\n

    :type StageVariables: dict
    :param StageVariables: A map that defines the stage variables for a Stage. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.\n\n(string) --\n(string) --A string with a length between [0-2048].\n\n\n\n\n

    :type Tags: dict
    :param Tags: The collection of tags. Each tag element is associated with a given resource.\n\n(string) --\n(string) --A string with a length between [0-1600].\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AccessLogSettings': {
        'DestinationArn': 'string',
        'Format': 'string'
    },
    'ApiGatewayManaged': True|False,
    'AutoDeploy': True|False,
    'ClientCertificateId': 'string',
    'CreatedDate': datetime(2015, 1, 1),
    'DefaultRouteSettings': {
        'DataTraceEnabled': True|False,
        'DetailedMetricsEnabled': True|False,
        'LoggingLevel': 'ERROR'|'INFO'|'OFF',
        'ThrottlingBurstLimit': 123,
        'ThrottlingRateLimit': 123.0
    },
    'DeploymentId': 'string',
    'Description': 'string',
    'LastDeploymentStatusMessage': 'string',
    'LastUpdatedDate': datetime(2015, 1, 1),
    'RouteSettings': {
        'string': {
            'DataTraceEnabled': True|False,
            'DetailedMetricsEnabled': True|False,
            'LoggingLevel': 'ERROR'|'INFO'|'OFF',
            'ThrottlingBurstLimit': 123,
            'ThrottlingRateLimit': 123.0
        }
    },
    'StageName': 'string',
    'StageVariables': {
        'string': 'string'
    },
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.

AccessLogSettings (dict) --
Settings for logging access in this stage.

DestinationArn (string) --
The ARN of the CloudWatch Logs log group to receive access logs.

Format (string) --
A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.



ApiGatewayManaged (boolean) --
Specifies whether a stage is managed by API Gateway. If you created an API using quick create, the $default stage is managed by API Gateway. You can\'t modify the $default stage.

AutoDeploy (boolean) --
Specifies whether updates to an API automatically trigger a new deployment. The default value is false.

ClientCertificateId (string) --
The identifier of a client certificate for a Stage. Supported only for WebSocket APIs.

CreatedDate (datetime) --
The timestamp when the stage was created.

DefaultRouteSettings (dict) --
Default route settings for the stage.

DataTraceEnabled (boolean) --
Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

DetailedMetricsEnabled (boolean) --
Specifies whether detailed metrics are enabled.

LoggingLevel (string) --
Specifies the logging level for this route: INFO, ERROR, or OFF. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

ThrottlingBurstLimit (integer) --
Specifies the throttling burst limit.

ThrottlingRateLimit (float) --
Specifies the throttling rate limit.



DeploymentId (string) --
The identifier of the Deployment that the Stage is associated with. Can\'t be updated if autoDeploy is enabled.

Description (string) --
The description of the stage.

LastDeploymentStatusMessage (string) --
Describes the status of the last deployment of a stage. Supported only for stages with autoDeploy enabled.

LastUpdatedDate (datetime) --
The timestamp when the stage was last updated.

RouteSettings (dict) --
Route settings for the stage, by routeKey.

(string) --

(dict) --
Represents a collection of route settings.

DataTraceEnabled (boolean) --
Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

DetailedMetricsEnabled (boolean) --
Specifies whether detailed metrics are enabled.

LoggingLevel (string) --
Specifies the logging level for this route: INFO, ERROR, or OFF. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

ThrottlingBurstLimit (integer) --
Specifies the throttling burst limit.

ThrottlingRateLimit (float) --
Specifies the throttling rate limit.







StageName (string) --
The name of the stage.

StageVariables (dict) --
A map that defines the stage variables for a stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.

(string) --

(string) --
A string with a length between [0-2048].





Tags (dict) --
The collection of tags. Each tag element is associated with a given resource.

(string) --

(string) --
A string with a length between [0-1600].











Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'AccessLogSettings': {
            'DestinationArn': 'string',
            'Format': 'string'
        },
        'ApiGatewayManaged': True|False,
        'AutoDeploy': True|False,
        'ClientCertificateId': 'string',
        'CreatedDate': datetime(2015, 1, 1),
        'DefaultRouteSettings': {
            'DataTraceEnabled': True|False,
            'DetailedMetricsEnabled': True|False,
            'LoggingLevel': 'ERROR'|'INFO'|'OFF',
            'ThrottlingBurstLimit': 123,
            'ThrottlingRateLimit': 123.0
        },
        'DeploymentId': 'string',
        'Description': 'string',
        'LastDeploymentStatusMessage': 'string',
        'LastUpdatedDate': datetime(2015, 1, 1),
        'RouteSettings': {
            'string': {
                'DataTraceEnabled': True|False,
                'DetailedMetricsEnabled': True|False,
                'LoggingLevel': 'ERROR'|'INFO'|'OFF',
                'ThrottlingBurstLimit': 123,
                'ThrottlingRateLimit': 123.0
            }
        },
        'StageName': 'string',
        'StageVariables': {
            'string': 'string'
        },
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def create_vpc_link(Name=None, SecurityGroupIds=None, SubnetIds=None, Tags=None):
    """
    Creates a VPC link.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_vpc_link(
        Name='string',
        SecurityGroupIds=[
            'string',
        ],
        SubnetIds=[
            'string',
        ],
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the VPC link.\n

    :type SecurityGroupIds: list
    :param SecurityGroupIds: A list of security group IDs for the VPC link.\n\n(string) --\n\n

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nA list of subnet IDs to include in the VPC link.\n\n(string) --\n\n

    :type Tags: dict
    :param Tags: A list of tags.\n\n(string) --\n(string) --A string with a length between [0-1600].\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CreatedDate': datetime(2015, 1, 1),
    'Name': 'string',
    'SecurityGroupIds': [
        'string',
    ],
    'SubnetIds': [
        'string',
    ],
    'Tags': {
        'string': 'string'
    },
    'VpcLinkId': 'string',
    'VpcLinkStatus': 'PENDING'|'AVAILABLE'|'DELETING'|'FAILED'|'INACTIVE',
    'VpcLinkStatusMessage': 'string',
    'VpcLinkVersion': 'V2'
}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.

CreatedDate (datetime) --
The timestamp when the VPC link was created.

Name (string) --
The name of the VPC link.

SecurityGroupIds (list) --
A list of security group IDs for the VPC link.

(string) --


SubnetIds (list) --
A list of subnet IDs to include in the VPC link.

(string) --


Tags (dict) --
Tags for the VPC link.

(string) --

(string) --
A string with a length between [0-1600].





VpcLinkId (string) --
The ID of the VPC link.

VpcLinkStatus (string) --
The status of the VPC link.

VpcLinkStatusMessage (string) --
A message summarizing the cause of the status of the VPC link.

VpcLinkVersion (string) --
The version of the VPC link.







Exceptions

ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {
        'CreatedDate': datetime(2015, 1, 1),
        'Name': 'string',
        'SecurityGroupIds': [
            'string',
        ],
        'SubnetIds': [
            'string',
        ],
        'Tags': {
            'string': 'string'
        },
        'VpcLinkId': 'string',
        'VpcLinkStatus': 'PENDING'|'AVAILABLE'|'DELETING'|'FAILED'|'INACTIVE',
        'VpcLinkStatusMessage': 'string',
        'VpcLinkVersion': 'V2'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_access_log_settings(ApiId=None, StageName=None):
    """
    Deletes the AccessLogSettings for a Stage. To disable access logging for a Stage, delete its AccessLogSettings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_access_log_settings(
        ApiId='string',
        StageName='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type StageName: string
    :param StageName: [REQUIRED]\nThe stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.\n

    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_api(ApiId=None):
    """
    Deletes an Api resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_api(
        ApiId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    """
    pass

def delete_api_mapping(ApiMappingId=None, DomainName=None):
    """
    Deletes an API mapping.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_api_mapping(
        ApiMappingId='string',
        DomainName='string'
    )
    
    
    :type ApiMappingId: string
    :param ApiMappingId: [REQUIRED]\nThe API mapping identifier.\n

    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe domain name.\n

    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    
    """
    pass

def delete_authorizer(ApiId=None, AuthorizerId=None):
    """
    Deletes an Authorizer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_authorizer(
        ApiId='string',
        AuthorizerId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type AuthorizerId: string
    :param AuthorizerId: [REQUIRED]\nThe authorizer identifier.\n

    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_cors_configuration(ApiId=None):
    """
    Deletes a CORS configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_cors_configuration(
        ApiId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    """
    pass

def delete_deployment(ApiId=None, DeploymentId=None):
    """
    Deletes a Deployment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_deployment(
        ApiId='string',
        DeploymentId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type DeploymentId: string
    :param DeploymentId: [REQUIRED]\nThe deployment ID.\n

    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_domain_name(DomainName=None):
    """
    Deletes a domain name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_domain_name(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe domain name.\n

    """
    pass

def delete_integration(ApiId=None, IntegrationId=None):
    """
    Deletes an Integration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_integration(
        ApiId='string',
        IntegrationId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type IntegrationId: string
    :param IntegrationId: [REQUIRED]\nThe integration ID.\n

    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_integration_response(ApiId=None, IntegrationId=None, IntegrationResponseId=None):
    """
    Deletes an IntegrationResponses.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_integration_response(
        ApiId='string',
        IntegrationId='string',
        IntegrationResponseId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type IntegrationId: string
    :param IntegrationId: [REQUIRED]\nThe integration ID.\n

    :type IntegrationResponseId: string
    :param IntegrationResponseId: [REQUIRED]\nThe integration response ID.\n

    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_model(ApiId=None, ModelId=None):
    """
    Deletes a Model.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_model(
        ApiId='string',
        ModelId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ModelId: string
    :param ModelId: [REQUIRED]\nThe model ID.\n

    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_route(ApiId=None, RouteId=None):
    """
    Deletes a Route.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_route(
        ApiId='string',
        RouteId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type RouteId: string
    :param RouteId: [REQUIRED]\nThe route ID.\n

    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_route_request_parameter(ApiId=None, RequestParameterKey=None, RouteId=None):
    """
    Deletes a route request parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_route_request_parameter(
        ApiId='string',
        RequestParameterKey='string',
        RouteId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type RequestParameterKey: string
    :param RequestParameterKey: [REQUIRED]\nThe route request parameter key.\n

    :type RouteId: string
    :param RouteId: [REQUIRED]\nThe route ID.\n

    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_route_response(ApiId=None, RouteId=None, RouteResponseId=None):
    """
    Deletes a RouteResponse.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_route_response(
        ApiId='string',
        RouteId='string',
        RouteResponseId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type RouteId: string
    :param RouteId: [REQUIRED]\nThe route ID.\n

    :type RouteResponseId: string
    :param RouteResponseId: [REQUIRED]\nThe route response ID.\n

    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_route_settings(ApiId=None, RouteKey=None, StageName=None):
    """
    Deletes the RouteSettings for a stage.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_route_settings(
        ApiId='string',
        RouteKey='string',
        StageName='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type RouteKey: string
    :param RouteKey: [REQUIRED]\nThe route key.\n

    :type StageName: string
    :param StageName: [REQUIRED]\nThe stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.\n

    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_stage(ApiId=None, StageName=None):
    """
    Deletes a Stage.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_stage(
        ApiId='string',
        StageName='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type StageName: string
    :param StageName: [REQUIRED]\nThe stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.\n

    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_vpc_link(VpcLinkId=None):
    """
    Deletes a VPC link.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_vpc_link(
        VpcLinkId='string'
    )
    
    
    :type VpcLinkId: string
    :param VpcLinkId: [REQUIRED]\nThe ID of the VPC link.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --202 response




Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    """
    pass

def export_api(ApiId=None, ExportVersion=None, IncludeExtensions=None, OutputType=None, Specification=None, StageName=None):
    """
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.export_api(
        ApiId='string',
        ExportVersion='string',
        IncludeExtensions=True|False,
        OutputType='YAML'|'JSON',
        Specification='OAS30',
        StageName='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ExportVersion: string
    :param ExportVersion: The version of the API Gateway export algorithm. API Gateway uses the latest version by default. Currently, the only supported version is 1.0.

    :type IncludeExtensions: boolean
    :param IncludeExtensions: Specifies whether to include API Gateway extensions in the exported API definition. API Gateway extensions are included by default.

    :type OutputType: string
    :param OutputType: [REQUIRED]\nThe output type of the exported definition file. Valid values are JSON and YAML.\n

    :type Specification: string
    :param Specification: [REQUIRED]\nThe version of the API specification to use. OAS30, for OpenAPI 3.0, is the only supported value.\n

    :type StageName: string
    :param StageName: The name of the API stage to export. If you don\'t specify this property, a representation of the latest API configuration is exported.

    :rtype: dict

ReturnsResponse Syntax
{
    'body': StreamingBody()
}


Response Structure

(dict) --
Success

body (StreamingBody) --
Represents an exported definition of an API in a particular output format, for example, YAML. The API is serialized to the requested specification, for example, OpenAPI 3.0.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException


    :return: {
        'body': StreamingBody()
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    
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

def get_api(ApiId=None):
    """
    Gets an Api resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_api(
        ApiId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ApiEndpoint': 'string',
    'ApiId': 'string',
    'ApiKeySelectionExpression': 'string',
    'CorsConfiguration': {
        'AllowCredentials': True|False,
        'AllowHeaders': [
            'string',
        ],
        'AllowMethods': [
            'string',
        ],
        'AllowOrigins': [
            'string',
        ],
        'ExposeHeaders': [
            'string',
        ],
        'MaxAge': 123
    },
    'CreatedDate': datetime(2015, 1, 1),
    'Description': 'string',
    'DisableSchemaValidation': True|False,
    'ImportInfo': [
        'string',
    ],
    'Name': 'string',
    'ProtocolType': 'WEBSOCKET'|'HTTP',
    'RouteSelectionExpression': 'string',
    'Tags': {
        'string': 'string'
    },
    'Version': 'string',
    'Warnings': [
        'string',
    ]
}


Response Structure

(dict) --Success

ApiEndpoint (string) --The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage.

ApiId (string) --The API ID.

ApiKeySelectionExpression (string) --An API key selection expression. Supported only for WebSocket APIs. See API Key Selection Expressions .

CorsConfiguration (dict) --A CORS configuration. Supported only for HTTP APIs.

AllowCredentials (boolean) --Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.

AllowHeaders (list) --Represents a collection of allowed headers. Supported only for HTTP APIs.

(string) --


AllowMethods (list) --Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.

(string) --A string with a length between [1-64].



AllowOrigins (list) --Represents a collection of allowed origins. Supported only for HTTP APIs.

(string) --


ExposeHeaders (list) --Represents a collection of exposed headers. Supported only for HTTP APIs.

(string) --


MaxAge (integer) --The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.



CreatedDate (datetime) --The timestamp when the API was created.

Description (string) --The description of the API.

DisableSchemaValidation (boolean) --Avoid validating models when creating a deployment. Supported only for WebSocket APIs.

ImportInfo (list) --The validation information during API import. This may include particular properties of your OpenAPI definition which are ignored during import. Supported only for HTTP APIs.

(string) --


Name (string) --The name of the API.

ProtocolType (string) --The API protocol.

RouteSelectionExpression (string) --The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.

Tags (dict) --A collection of tags associated with the API.

(string) --
(string) --A string with a length between [0-1600].





Version (string) --A version identifier for the API.

Warnings (list) --The warning messages reported when failonwarnings is turned on during API import.

(string) --







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {
        'ApiEndpoint': 'string',
        'ApiId': 'string',
        'ApiKeySelectionExpression': 'string',
        'CorsConfiguration': {
            'AllowCredentials': True|False,
            'AllowHeaders': [
                'string',
            ],
            'AllowMethods': [
                'string',
            ],
            'AllowOrigins': [
                'string',
            ],
            'ExposeHeaders': [
                'string',
            ],
            'MaxAge': 123
        },
        'CreatedDate': datetime(2015, 1, 1),
        'Description': 'string',
        'DisableSchemaValidation': True|False,
        'ImportInfo': [
            'string',
        ],
        'Name': 'string',
        'ProtocolType': 'WEBSOCKET'|'HTTP',
        'RouteSelectionExpression': 'string',
        'Tags': {
            'string': 'string'
        },
        'Version': 'string',
        'Warnings': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_api_mapping(ApiMappingId=None, DomainName=None):
    """
    Gets an API mapping.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_api_mapping(
        ApiMappingId='string',
        DomainName='string'
    )
    
    
    :type ApiMappingId: string
    :param ApiMappingId: [REQUIRED]\nThe API mapping identifier.\n

    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe domain name.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiId': 'string',
    'ApiMappingId': 'string',
    'ApiMappingKey': 'string',
    'Stage': 'string'
}


Response Structure

(dict) --
Success

ApiId (string) --
The API identifier.

ApiMappingId (string) --
The API mapping identifier.

ApiMappingKey (string) --
The API mapping key.

Stage (string) --
The API stage.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException


    :return: {
        'ApiId': 'string',
        'ApiMappingId': 'string',
        'ApiMappingKey': 'string',
        'Stage': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    
    """
    pass

def get_api_mappings(DomainName=None, MaxResults=None, NextToken=None):
    """
    Gets API mappings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_api_mappings(
        DomainName='string',
        MaxResults='string',
        NextToken='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe domain name.\n

    :type MaxResults: string
    :param MaxResults: The maximum number of elements to be returned for this resource.

    :type NextToken: string
    :param NextToken: The next page of elements from this collection. Not valid for the last element of the collection.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'ApiId': 'string',
            'ApiMappingId': 'string',
            'ApiMappingKey': 'string',
            'Stage': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success

Items (list) --
The elements from this collection.

(dict) --
Represents an API mapping.

ApiId (string) --
The API identifier.

ApiMappingId (string) --
The API mapping identifier.

ApiMappingKey (string) --
The API mapping key.

Stage (string) --
The API stage.





NextToken (string) --
The next page of elements from this collection. Not valid for the last element of the collection.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'ApiId': 'string',
                'ApiMappingId': 'string',
                'ApiMappingKey': 'string',
                'Stage': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    
    """
    pass

def get_apis(MaxResults=None, NextToken=None):
    """
    Gets a collection of Api resources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_apis(
        MaxResults='string',
        NextToken='string'
    )
    
    
    :type MaxResults: string
    :param MaxResults: The maximum number of elements to be returned for this resource.

    :type NextToken: string
    :param NextToken: The next page of elements from this collection. Not valid for the last element of the collection.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'ApiEndpoint': 'string',
            'ApiId': 'string',
            'ApiKeySelectionExpression': 'string',
            'CorsConfiguration': {
                'AllowCredentials': True|False,
                'AllowHeaders': [
                    'string',
                ],
                'AllowMethods': [
                    'string',
                ],
                'AllowOrigins': [
                    'string',
                ],
                'ExposeHeaders': [
                    'string',
                ],
                'MaxAge': 123
            },
            'CreatedDate': datetime(2015, 1, 1),
            'Description': 'string',
            'DisableSchemaValidation': True|False,
            'ImportInfo': [
                'string',
            ],
            'Name': 'string',
            'ProtocolType': 'WEBSOCKET'|'HTTP',
            'RouteSelectionExpression': 'string',
            'Tags': {
                'string': 'string'
            },
            'Version': 'string',
            'Warnings': [
                'string',
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success

Items (list) --
The elements from this collection.

(dict) --
Represents an API.

ApiEndpoint (string) --
The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage.

ApiId (string) --
The API ID.

ApiKeySelectionExpression (string) --
An API key selection expression. Supported only for WebSocket APIs. See API Key Selection Expressions .

CorsConfiguration (dict) --
A CORS configuration. Supported only for HTTP APIs.

AllowCredentials (boolean) --
Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.

AllowHeaders (list) --
Represents a collection of allowed headers. Supported only for HTTP APIs.

(string) --


AllowMethods (list) --
Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.

(string) --
A string with a length between [1-64].



AllowOrigins (list) --
Represents a collection of allowed origins. Supported only for HTTP APIs.

(string) --


ExposeHeaders (list) --
Represents a collection of exposed headers. Supported only for HTTP APIs.

(string) --


MaxAge (integer) --
The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.



CreatedDate (datetime) --
The timestamp when the API was created.

Description (string) --
The description of the API.

DisableSchemaValidation (boolean) --
Avoid validating models when creating a deployment. Supported only for WebSocket APIs.

ImportInfo (list) --
The validation information during API import. This may include particular properties of your OpenAPI definition which are ignored during import. Supported only for HTTP APIs.

(string) --


Name (string) --
The name of the API.

ProtocolType (string) --
The API protocol.

RouteSelectionExpression (string) --
The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.

Tags (dict) --
A collection of tags associated with the API.

(string) --

(string) --
A string with a length between [0-1600].





Version (string) --
A version identifier for the API.

Warnings (list) --
The warning messages reported when failonwarnings is turned on during API import.

(string) --






NextToken (string) --
The next page of elements from this collection. Not valid for the last element of the collection.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'ApiEndpoint': 'string',
                'ApiId': 'string',
                'ApiKeySelectionExpression': 'string',
                'CorsConfiguration': {
                    'AllowCredentials': True|False,
                    'AllowHeaders': [
                        'string',
                    ],
                    'AllowMethods': [
                        'string',
                    ],
                    'AllowOrigins': [
                        'string',
                    ],
                    'ExposeHeaders': [
                        'string',
                    ],
                    'MaxAge': 123
                },
                'CreatedDate': datetime(2015, 1, 1),
                'Description': 'string',
                'DisableSchemaValidation': True|False,
                'ImportInfo': [
                    'string',
                ],
                'Name': 'string',
                'ProtocolType': 'WEBSOCKET'|'HTTP',
                'RouteSelectionExpression': 'string',
                'Tags': {
                    'string': 'string'
                },
                'Version': 'string',
                'Warnings': [
                    'string',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_authorizer(ApiId=None, AuthorizerId=None):
    """
    Gets an Authorizer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_authorizer(
        ApiId='string',
        AuthorizerId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type AuthorizerId: string
    :param AuthorizerId: [REQUIRED]\nThe authorizer identifier.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AuthorizerCredentialsArn': 'string',
    'AuthorizerId': 'string',
    'AuthorizerResultTtlInSeconds': 123,
    'AuthorizerType': 'REQUEST'|'JWT',
    'AuthorizerUri': 'string',
    'IdentitySource': [
        'string',
    ],
    'IdentityValidationExpression': 'string',
    'JwtConfiguration': {
        'Audience': [
            'string',
        ],
        'Issuer': 'string'
    },
    'Name': 'string'
}


Response Structure

(dict) --
Success

AuthorizerCredentialsArn (string) --
Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null. Supported only for REQUEST authorizers.

AuthorizerId (string) --
The authorizer identifier.

AuthorizerResultTtlInSeconds (integer) --
Authorizer caching is not currently supported. Don\'t specify this value for authorizers.

AuthorizerType (string) --
The authorizer type. For WebSocket APIs, specify REQUEST for a Lambda function using incoming request parameters. For HTTP APIs, specify JWT to use JSON Web Tokens.

AuthorizerUri (string) --
The authorizer\'s Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations. In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api}, where {region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations. Supported only for REQUEST authorizers.

IdentitySource (list) --
The identity source for which authorization is requested.
For a REQUEST authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. Currently, the identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name. These parameters will be used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function.
For JWT, a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example "$request.header.Authorization".

(string) --


IdentityValidationExpression (string) --
The validation expression does not apply to the REQUEST authorizer.

JwtConfiguration (dict) --
Represents the configuration of a JWT authorizer. Required for the JWT authorizer type. Supported only for HTTP APIs.

Audience (list) --
A list of the intended recipients of the JWT. A valid JWT must provide an aud that matches at least one entry in this list. See RFC 7519 . Supported only for HTTP APIs.

(string) --


Issuer (string) --
The base domain of the identity provider that issues JSON Web Tokens. For example, an Amazon Cognito user pool has the following format: https://cognito-idp.{region}.amazonaws.com/{userPoolId}. Required for the JWT authorizer type. Supported only for HTTP APIs.



Name (string) --
The name of the authorizer.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {
        'AuthorizerCredentialsArn': 'string',
        'AuthorizerId': 'string',
        'AuthorizerResultTtlInSeconds': 123,
        'AuthorizerType': 'REQUEST'|'JWT',
        'AuthorizerUri': 'string',
        'IdentitySource': [
            'string',
        ],
        'IdentityValidationExpression': 'string',
        'JwtConfiguration': {
            'Audience': [
                'string',
            ],
            'Issuer': 'string'
        },
        'Name': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_authorizers(ApiId=None, MaxResults=None, NextToken=None):
    """
    Gets the Authorizers for an API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_authorizers(
        ApiId='string',
        MaxResults='string',
        NextToken='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type MaxResults: string
    :param MaxResults: The maximum number of elements to be returned for this resource.

    :type NextToken: string
    :param NextToken: The next page of elements from this collection. Not valid for the last element of the collection.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'AuthorizerCredentialsArn': 'string',
            'AuthorizerId': 'string',
            'AuthorizerResultTtlInSeconds': 123,
            'AuthorizerType': 'REQUEST'|'JWT',
            'AuthorizerUri': 'string',
            'IdentitySource': [
                'string',
            ],
            'IdentityValidationExpression': 'string',
            'JwtConfiguration': {
                'Audience': [
                    'string',
                ],
                'Issuer': 'string'
            },
            'Name': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success

Items (list) --
The elements from this collection.

(dict) --
Represents an authorizer.

AuthorizerCredentialsArn (string) --
Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null. Supported only for REQUEST authorizers.

AuthorizerId (string) --
The authorizer identifier.

AuthorizerResultTtlInSeconds (integer) --
Authorizer caching is not currently supported. Don\'t specify this value for authorizers.

AuthorizerType (string) --
The authorizer type. For WebSocket APIs, specify REQUEST for a Lambda function using incoming request parameters. For HTTP APIs, specify JWT to use JSON Web Tokens.

AuthorizerUri (string) --
The authorizer\'s Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations. In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api}, where {region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations. Supported only for REQUEST authorizers.

IdentitySource (list) --
The identity source for which authorization is requested.
For a REQUEST authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. Currently, the identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name. These parameters will be used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function.
For JWT, a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example "$request.header.Authorization".

(string) --


IdentityValidationExpression (string) --
The validation expression does not apply to the REQUEST authorizer.

JwtConfiguration (dict) --
Represents the configuration of a JWT authorizer. Required for the JWT authorizer type. Supported only for HTTP APIs.

Audience (list) --
A list of the intended recipients of the JWT. A valid JWT must provide an aud that matches at least one entry in this list. See RFC 7519 . Supported only for HTTP APIs.

(string) --


Issuer (string) --
The base domain of the identity provider that issues JSON Web Tokens. For example, an Amazon Cognito user pool has the following format: https://cognito-idp.{region}.amazonaws.com/{userPoolId}. Required for the JWT authorizer type. Supported only for HTTP APIs.



Name (string) --
The name of the authorizer.





NextToken (string) --
The next page of elements from this collection. Not valid for the last element of the collection.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'AuthorizerCredentialsArn': 'string',
                'AuthorizerId': 'string',
                'AuthorizerResultTtlInSeconds': 123,
                'AuthorizerType': 'REQUEST'|'JWT',
                'AuthorizerUri': 'string',
                'IdentitySource': [
                    'string',
                ],
                'IdentityValidationExpression': 'string',
                'JwtConfiguration': {
                    'Audience': [
                        'string',
                    ],
                    'Issuer': 'string'
                },
                'Name': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_deployment(ApiId=None, DeploymentId=None):
    """
    Gets a Deployment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_deployment(
        ApiId='string',
        DeploymentId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type DeploymentId: string
    :param DeploymentId: [REQUIRED]\nThe deployment ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AutoDeployed': True|False,
    'CreatedDate': datetime(2015, 1, 1),
    'DeploymentId': 'string',
    'DeploymentStatus': 'PENDING'|'FAILED'|'DEPLOYED',
    'DeploymentStatusMessage': 'string',
    'Description': 'string'
}


Response Structure

(dict) --
Success

AutoDeployed (boolean) --
Specifies whether a deployment was automatically released.

CreatedDate (datetime) --
The date and time when the Deployment resource was created.

DeploymentId (string) --
The identifier for the deployment.

DeploymentStatus (string) --
The status of the deployment: PENDING, FAILED, or SUCCEEDED.

DeploymentStatusMessage (string) --
May contain additional feedback on the status of an API deployment.

Description (string) --
The description for the deployment.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {
        'AutoDeployed': True|False,
        'CreatedDate': datetime(2015, 1, 1),
        'DeploymentId': 'string',
        'DeploymentStatus': 'PENDING'|'FAILED'|'DEPLOYED',
        'DeploymentStatusMessage': 'string',
        'Description': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def get_deployments(ApiId=None, MaxResults=None, NextToken=None):
    """
    Gets the Deployments for an API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_deployments(
        ApiId='string',
        MaxResults='string',
        NextToken='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type MaxResults: string
    :param MaxResults: The maximum number of elements to be returned for this resource.

    :type NextToken: string
    :param NextToken: The next page of elements from this collection. Not valid for the last element of the collection.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'AutoDeployed': True|False,
            'CreatedDate': datetime(2015, 1, 1),
            'DeploymentId': 'string',
            'DeploymentStatus': 'PENDING'|'FAILED'|'DEPLOYED',
            'DeploymentStatusMessage': 'string',
            'Description': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success

Items (list) --
The elements from this collection.

(dict) --
An immutable representation of an API that can be called by users. A Deployment must be associated with a Stage for it to be callable over the internet.

AutoDeployed (boolean) --
Specifies whether a deployment was automatically released.

CreatedDate (datetime) --
The date and time when the Deployment resource was created.

DeploymentId (string) --
The identifier for the deployment.

DeploymentStatus (string) --
The status of the deployment: PENDING, FAILED, or SUCCEEDED.

DeploymentStatusMessage (string) --
May contain additional feedback on the status of an API deployment.

Description (string) --
The description for the deployment.





NextToken (string) --
The next page of elements from this collection. Not valid for the last element of the collection.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'AutoDeployed': True|False,
                'CreatedDate': datetime(2015, 1, 1),
                'DeploymentId': 'string',
                'DeploymentStatus': 'PENDING'|'FAILED'|'DEPLOYED',
                'DeploymentStatusMessage': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    
    """
    pass

def get_domain_name(DomainName=None):
    """
    Gets a domain name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_domain_name(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe domain name.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ApiMappingSelectionExpression': 'string',
    'DomainName': 'string',
    'DomainNameConfigurations': [
        {
            'ApiGatewayDomainName': 'string',
            'CertificateArn': 'string',
            'CertificateName': 'string',
            'CertificateUploadDate': datetime(2015, 1, 1),
            'DomainNameStatus': 'AVAILABLE'|'UPDATING',
            'DomainNameStatusMessage': 'string',
            'EndpointType': 'REGIONAL'|'EDGE',
            'HostedZoneId': 'string',
            'SecurityPolicy': 'TLS_1_0'|'TLS_1_2'
        },
    ],
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --Success

ApiMappingSelectionExpression (string) --The API mapping selection expression.

DomainName (string) --The name of the DomainName resource.

DomainNameConfigurations (list) --The domain name configurations.

(dict) --The domain name configuration.

ApiGatewayDomainName (string) --A domain name for the API.

CertificateArn (string) --An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.

CertificateName (string) --The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.

CertificateUploadDate (datetime) --The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.

DomainNameStatus (string) --The status of the domain name migration. The valid values are AVAILABLE and UPDATING. If the status is UPDATING, the domain cannot be modified further until the existing operation is complete. If it is AVAILABLE, the domain can be updated.

DomainNameStatusMessage (string) --An optional text message containing detailed information about status of the domain name migration.

EndpointType (string) --The endpoint type.

HostedZoneId (string) --The Amazon Route 53 Hosted Zone ID of the endpoint.

SecurityPolicy (string) --The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are TLS_1_0 and TLS_1_2.





Tags (dict) --The collection of tags associated with a domain name.

(string) --
(string) --A string with a length between [0-1600].










Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {
        'ApiMappingSelectionExpression': 'string',
        'DomainName': 'string',
        'DomainNameConfigurations': [
            {
                'ApiGatewayDomainName': 'string',
                'CertificateArn': 'string',
                'CertificateName': 'string',
                'CertificateUploadDate': datetime(2015, 1, 1),
                'DomainNameStatus': 'AVAILABLE'|'UPDATING',
                'DomainNameStatusMessage': 'string',
                'EndpointType': 'REGIONAL'|'EDGE',
                'HostedZoneId': 'string',
                'SecurityPolicy': 'TLS_1_0'|'TLS_1_2'
            },
        ],
        'Tags': {
            'string': 'string'
        }
    }
    
    
    """
    pass

def get_domain_names(MaxResults=None, NextToken=None):
    """
    Gets the domain names for an AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_domain_names(
        MaxResults='string',
        NextToken='string'
    )
    
    
    :type MaxResults: string
    :param MaxResults: The maximum number of elements to be returned for this resource.

    :type NextToken: string
    :param NextToken: The next page of elements from this collection. Not valid for the last element of the collection.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'ApiMappingSelectionExpression': 'string',
            'DomainName': 'string',
            'DomainNameConfigurations': [
                {
                    'ApiGatewayDomainName': 'string',
                    'CertificateArn': 'string',
                    'CertificateName': 'string',
                    'CertificateUploadDate': datetime(2015, 1, 1),
                    'DomainNameStatus': 'AVAILABLE'|'UPDATING',
                    'DomainNameStatusMessage': 'string',
                    'EndpointType': 'REGIONAL'|'EDGE',
                    'HostedZoneId': 'string',
                    'SecurityPolicy': 'TLS_1_0'|'TLS_1_2'
                },
            ],
            'Tags': {
                'string': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success

Items (list) --
The elements from this collection.

(dict) --
Represents a domain name.

ApiMappingSelectionExpression (string) --
The API mapping selection expression.

DomainName (string) --
The name of the DomainName resource.

DomainNameConfigurations (list) --
The domain name configurations.

(dict) --
The domain name configuration.

ApiGatewayDomainName (string) --
A domain name for the API.

CertificateArn (string) --
An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.

CertificateName (string) --
The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.

CertificateUploadDate (datetime) --
The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.

DomainNameStatus (string) --
The status of the domain name migration. The valid values are AVAILABLE and UPDATING. If the status is UPDATING, the domain cannot be modified further until the existing operation is complete. If it is AVAILABLE, the domain can be updated.

DomainNameStatusMessage (string) --
An optional text message containing detailed information about status of the domain name migration.

EndpointType (string) --
The endpoint type.

HostedZoneId (string) --
The Amazon Route 53 Hosted Zone ID of the endpoint.

SecurityPolicy (string) --
The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are TLS_1_0 and TLS_1_2.





Tags (dict) --
The collection of tags associated with a domain name.

(string) --

(string) --
A string with a length between [0-1600].









NextToken (string) --
The next page of elements from this collection. Not valid for the last element of the collection.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'ApiMappingSelectionExpression': 'string',
                'DomainName': 'string',
                'DomainNameConfigurations': [
                    {
                        'ApiGatewayDomainName': 'string',
                        'CertificateArn': 'string',
                        'CertificateName': 'string',
                        'CertificateUploadDate': datetime(2015, 1, 1),
                        'DomainNameStatus': 'AVAILABLE'|'UPDATING',
                        'DomainNameStatusMessage': 'string',
                        'EndpointType': 'REGIONAL'|'EDGE',
                        'HostedZoneId': 'string',
                        'SecurityPolicy': 'TLS_1_0'|'TLS_1_2'
                    },
                ],
                'Tags': {
                    'string': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    
    """
    pass

def get_integration(ApiId=None, IntegrationId=None):
    """
    Gets an Integration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_integration(
        ApiId='string',
        IntegrationId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type IntegrationId: string
    :param IntegrationId: [REQUIRED]\nThe integration ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiGatewayManaged': True|False,
    'ConnectionId': 'string',
    'ConnectionType': 'INTERNET'|'VPC_LINK',
    'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
    'CredentialsArn': 'string',
    'Description': 'string',
    'IntegrationId': 'string',
    'IntegrationMethod': 'string',
    'IntegrationResponseSelectionExpression': 'string',
    'IntegrationType': 'AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
    'IntegrationUri': 'string',
    'PassthroughBehavior': 'WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
    'PayloadFormatVersion': 'string',
    'RequestParameters': {
        'string': 'string'
    },
    'RequestTemplates': {
        'string': 'string'
    },
    'TemplateSelectionExpression': 'string',
    'TimeoutInMillis': 123,
    'TlsConfig': {
        'ServerNameToVerify': 'string'
    }
}


Response Structure

(dict) --
Success

ApiGatewayManaged (boolean) --
Specifies whether an integration is managed by API Gateway. If you created an API using using quick create, the resulting integration is managed by API Gateway. You can update a managed integration, but you can\'t delete it.

ConnectionId (string) --
The ID of the VPC link for a private integration. Supported only for HTTP APIs.

ConnectionType (string) --
The type of the network connection to the integration endpoint. Specify INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and resources in a VPC. The default value is INTERNET.

ContentHandlingStrategy (string) --
Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.

CredentialsArn (string) --
Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To require that the caller\'s identity be passed through from the request, specify the string arn:aws:iam:::user/. To use resource-based permissions on supported AWS services, specify null.

Description (string) --
Represents the description of an integration.

IntegrationId (string) --
Represents the identifier of an integration.

IntegrationMethod (string) --
Specifies the integration\'s HTTP method type.

IntegrationResponseSelectionExpression (string) --
The integration response selection expression for the integration. Supported only for WebSocket APIs. See Integration Response Selection Expressions .

IntegrationType (string) --
The integration type of an integration. One of the following:
AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs.
AWS_PROXY: for integrating the route or method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as Lambda proxy integration.
HTTP: for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs.
HTTP_PROXY: for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration.
MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend. Supported only for WebSocket APIs.

IntegrationUri (string) --
For a Lambda integration, specify the URI of a Lambda function.
For an HTTP integration, specify a fully-qualified URL.
For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service. If you specify the ARN of an AWS Cloud Map service, API Gateway uses DiscoverInstances to identify resources. You can use query parameters to target specific resources. To learn more, see DiscoverInstances . For private integrations, all resources must be owned by the same AWS account.

PassthroughBehavior (string) --
Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Supported only for WebSocket APIs.
WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.
NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.
WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.

PayloadFormatVersion (string) --
Specifies the format of the payload sent to an integration. Required for HTTP APIs.

RequestParameters (dict) --
A key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.{location}.{name}, where {location}is querystring, path, or header; and {name}must be a valid and unique method request parameter name. Supported only for WebSocket APIs.

(string) --

(string) --
A string with a length between [1-512].





RequestTemplates (dict) --
Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value. Supported only for WebSocket APIs.

(string) --

(string) --
A string with a length between [0-32768].





TemplateSelectionExpression (string) --
The template selection expression for the integration. Supported only for WebSocket APIs.

TimeoutInMillis (integer) --
Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.

TlsConfig (dict) --
The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.

ServerNameToVerify (string) --
If you specify a server name, API Gateway uses it to verify the hostname on the integration\'s certificate. The server name is also included in the TLS handshake to support Server Name Indication (SNI) or virtual hosting.









Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {
        'ApiGatewayManaged': True|False,
        'ConnectionId': 'string',
        'ConnectionType': 'INTERNET'|'VPC_LINK',
        'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
        'CredentialsArn': 'string',
        'Description': 'string',
        'IntegrationId': 'string',
        'IntegrationMethod': 'string',
        'IntegrationResponseSelectionExpression': 'string',
        'IntegrationType': 'AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
        'IntegrationUri': 'string',
        'PassthroughBehavior': 'WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
        'PayloadFormatVersion': 'string',
        'RequestParameters': {
            'string': 'string'
        },
        'RequestTemplates': {
            'string': 'string'
        },
        'TemplateSelectionExpression': 'string',
        'TimeoutInMillis': 123,
        'TlsConfig': {
            'ServerNameToVerify': 'string'
        }
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def get_integration_response(ApiId=None, IntegrationId=None, IntegrationResponseId=None):
    """
    Gets an IntegrationResponses.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_integration_response(
        ApiId='string',
        IntegrationId='string',
        IntegrationResponseId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type IntegrationId: string
    :param IntegrationId: [REQUIRED]\nThe integration ID.\n

    :type IntegrationResponseId: string
    :param IntegrationResponseId: [REQUIRED]\nThe integration response ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
    'IntegrationResponseId': 'string',
    'IntegrationResponseKey': 'string',
    'ResponseParameters': {
        'string': 'string'
    },
    'ResponseTemplates': {
        'string': 'string'
    },
    'TemplateSelectionExpression': 'string'
}


Response Structure

(dict) --
Success

ContentHandlingStrategy (string) --
Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.

IntegrationResponseId (string) --
The integration response ID.

IntegrationResponseKey (string) --
The integration response key.

ResponseParameters (dict) --
A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where name is a valid and unique response header name and JSON-expression is a valid JSON expression without the $ prefix.

(string) --

(string) --
A string with a length between [1-512].





ResponseTemplates (dict) --
The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

(string) --

(string) --
A string with a length between [0-32768].





TemplateSelectionExpression (string) --
The template selection expressions for the integration response.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {
        'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
        'IntegrationResponseId': 'string',
        'IntegrationResponseKey': 'string',
        'ResponseParameters': {
            'string': 'string'
        },
        'ResponseTemplates': {
            'string': 'string'
        },
        'TemplateSelectionExpression': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def get_integration_responses(ApiId=None, IntegrationId=None, MaxResults=None, NextToken=None):
    """
    Gets the IntegrationResponses for an Integration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_integration_responses(
        ApiId='string',
        IntegrationId='string',
        MaxResults='string',
        NextToken='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type IntegrationId: string
    :param IntegrationId: [REQUIRED]\nThe integration ID.\n

    :type MaxResults: string
    :param MaxResults: The maximum number of elements to be returned for this resource.

    :type NextToken: string
    :param NextToken: The next page of elements from this collection. Not valid for the last element of the collection.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
            'IntegrationResponseId': 'string',
            'IntegrationResponseKey': 'string',
            'ResponseParameters': {
                'string': 'string'
            },
            'ResponseTemplates': {
                'string': 'string'
            },
            'TemplateSelectionExpression': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success

Items (list) --
The elements from this collection.

(dict) --
Represents an integration response.

ContentHandlingStrategy (string) --
Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.

IntegrationResponseId (string) --
The integration response ID.

IntegrationResponseKey (string) --
The integration response key.

ResponseParameters (dict) --
A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where name is a valid and unique response header name and JSON-expression is a valid JSON expression without the $ prefix.

(string) --

(string) --
A string with a length between [1-512].





ResponseTemplates (dict) --
The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

(string) --

(string) --
A string with a length between [0-32768].





TemplateSelectionExpression (string) --
The template selection expressions for the integration response.





NextToken (string) --
The next page of elements from this collection. Not valid for the last element of the collection.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                'IntegrationResponseId': 'string',
                'IntegrationResponseKey': 'string',
                'ResponseParameters': {
                    'string': 'string'
                },
                'ResponseTemplates': {
                    'string': 'string'
                },
                'TemplateSelectionExpression': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    
    """
    pass

def get_integrations(ApiId=None, MaxResults=None, NextToken=None):
    """
    Gets the Integrations for an API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_integrations(
        ApiId='string',
        MaxResults='string',
        NextToken='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type MaxResults: string
    :param MaxResults: The maximum number of elements to be returned for this resource.

    :type NextToken: string
    :param NextToken: The next page of elements from this collection. Not valid for the last element of the collection.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'ApiGatewayManaged': True|False,
            'ConnectionId': 'string',
            'ConnectionType': 'INTERNET'|'VPC_LINK',
            'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
            'CredentialsArn': 'string',
            'Description': 'string',
            'IntegrationId': 'string',
            'IntegrationMethod': 'string',
            'IntegrationResponseSelectionExpression': 'string',
            'IntegrationType': 'AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
            'IntegrationUri': 'string',
            'PassthroughBehavior': 'WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
            'PayloadFormatVersion': 'string',
            'RequestParameters': {
                'string': 'string'
            },
            'RequestTemplates': {
                'string': 'string'
            },
            'TemplateSelectionExpression': 'string',
            'TimeoutInMillis': 123,
            'TlsConfig': {
                'ServerNameToVerify': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success

Items (list) --
The elements from this collection.

(dict) --
Represents an integration.

ApiGatewayManaged (boolean) --
Specifies whether an integration is managed by API Gateway. If you created an API using using quick create, the resulting integration is managed by API Gateway. You can update a managed integration, but you can\'t delete it.

ConnectionId (string) --
The ID of the VPC link for a private integration. Supported only for HTTP APIs.

ConnectionType (string) --
The type of the network connection to the integration endpoint. Specify INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and resources in a VPC. The default value is INTERNET.

ContentHandlingStrategy (string) --
Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.

CredentialsArn (string) --
Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To require that the caller\'s identity be passed through from the request, specify the string arn:aws:iam:::user/. To use resource-based permissions on supported AWS services, specify null.

Description (string) --
Represents the description of an integration.

IntegrationId (string) --
Represents the identifier of an integration.

IntegrationMethod (string) --
Specifies the integration\'s HTTP method type.

IntegrationResponseSelectionExpression (string) --
The integration response selection expression for the integration. Supported only for WebSocket APIs. See Integration Response Selection Expressions .

IntegrationType (string) --
The integration type of an integration. One of the following:
AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs.
AWS_PROXY: for integrating the route or method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as Lambda proxy integration.
HTTP: for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs.
HTTP_PROXY: for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration.
MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend. Supported only for WebSocket APIs.

IntegrationUri (string) --
For a Lambda integration, specify the URI of a Lambda function.
For an HTTP integration, specify a fully-qualified URL.
For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service. If you specify the ARN of an AWS Cloud Map service, API Gateway uses DiscoverInstances to identify resources. You can use query parameters to target specific resources. To learn more, see DiscoverInstances . For private integrations, all resources must be owned by the same AWS account.

PassthroughBehavior (string) --
Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Supported only for WebSocket APIs.
WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.
NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.
WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.

PayloadFormatVersion (string) --
Specifies the format of the payload sent to an integration. Required for HTTP APIs.

RequestParameters (dict) --
A key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.{location}.{name}, where {location}is querystring, path, or header; and {name}must be a valid and unique method request parameter name. Supported only for WebSocket APIs.

(string) --

(string) --
A string with a length between [1-512].





RequestTemplates (dict) --
Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value. Supported only for WebSocket APIs.

(string) --

(string) --
A string with a length between [0-32768].





TemplateSelectionExpression (string) --
The template selection expression for the integration. Supported only for WebSocket APIs.

TimeoutInMillis (integer) --
Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.

TlsConfig (dict) --
The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.

ServerNameToVerify (string) --
If you specify a server name, API Gateway uses it to verify the hostname on the integration\'s certificate. The server name is also included in the TLS handshake to support Server Name Indication (SNI) or virtual hosting.







NextToken (string) --
The next page of elements from this collection. Not valid for the last element of the collection.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'ApiGatewayManaged': True|False,
                'ConnectionId': 'string',
                'ConnectionType': 'INTERNET'|'VPC_LINK',
                'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                'CredentialsArn': 'string',
                'Description': 'string',
                'IntegrationId': 'string',
                'IntegrationMethod': 'string',
                'IntegrationResponseSelectionExpression': 'string',
                'IntegrationType': 'AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                'IntegrationUri': 'string',
                'PassthroughBehavior': 'WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
                'PayloadFormatVersion': 'string',
                'RequestParameters': {
                    'string': 'string'
                },
                'RequestTemplates': {
                    'string': 'string'
                },
                'TemplateSelectionExpression': 'string',
                'TimeoutInMillis': 123,
                'TlsConfig': {
                    'ServerNameToVerify': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    
    """
    pass

def get_model(ApiId=None, ModelId=None):
    """
    Gets a Model.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_model(
        ApiId='string',
        ModelId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ModelId: string
    :param ModelId: [REQUIRED]\nThe model ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ContentType': 'string',
    'Description': 'string',
    'ModelId': 'string',
    'Name': 'string',
    'Schema': 'string'
}


Response Structure

(dict) --
Success

ContentType (string) --
The content-type for the model, for example, "application/json".

Description (string) --
The description of the model.

ModelId (string) --
The model identifier.

Name (string) --
The name of the model. Must be alphanumeric.

Schema (string) --
The schema for the model. For application/json models, this should be JSON schema draft 4 model.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {
        'ContentType': 'string',
        'Description': 'string',
        'ModelId': 'string',
        'Name': 'string',
        'Schema': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def get_model_template(ApiId=None, ModelId=None):
    """
    Gets a model template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_model_template(
        ApiId='string',
        ModelId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ModelId: string
    :param ModelId: [REQUIRED]\nThe model ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Value': 'string'
}


Response Structure

(dict) --
Success

Value (string) --
The template value.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {
        'Value': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def get_models(ApiId=None, MaxResults=None, NextToken=None):
    """
    Gets the Models for an API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_models(
        ApiId='string',
        MaxResults='string',
        NextToken='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type MaxResults: string
    :param MaxResults: The maximum number of elements to be returned for this resource.

    :type NextToken: string
    :param NextToken: The next page of elements from this collection. Not valid for the last element of the collection.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'ContentType': 'string',
            'Description': 'string',
            'ModelId': 'string',
            'Name': 'string',
            'Schema': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success

Items (list) --
The elements from this collection.

(dict) --
Represents a data model for an API. Supported only for WebSocket APIs. See Create Models and Mapping Templates for Request and Response Mappings .

ContentType (string) --
The content-type for the model, for example, "application/json".

Description (string) --
The description of the model.

ModelId (string) --
The model identifier.

Name (string) --
The name of the model. Must be alphanumeric.

Schema (string) --
The schema for the model. For application/json models, this should be JSON schema draft 4 model.





NextToken (string) --
The next page of elements from this collection. Not valid for the last element of the collection.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'ContentType': 'string',
                'Description': 'string',
                'ModelId': 'string',
                'Name': 'string',
                'Schema': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    
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

def get_route(ApiId=None, RouteId=None):
    """
    Gets a Route.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_route(
        ApiId='string',
        RouteId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type RouteId: string
    :param RouteId: [REQUIRED]\nThe route ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiGatewayManaged': True|False,
    'ApiKeyRequired': True|False,
    'AuthorizationScopes': [
        'string',
    ],
    'AuthorizationType': 'NONE'|'AWS_IAM'|'CUSTOM'|'JWT',
    'AuthorizerId': 'string',
    'ModelSelectionExpression': 'string',
    'OperationName': 'string',
    'RequestModels': {
        'string': 'string'
    },
    'RequestParameters': {
        'string': {
            'Required': True|False
        }
    },
    'RouteId': 'string',
    'RouteKey': 'string',
    'RouteResponseSelectionExpression': 'string',
    'Target': 'string'
}


Response Structure

(dict) --
Success

ApiGatewayManaged (boolean) --
Specifies whether a route is managed by API Gateway. If you created an API using quick create, the $default route is managed by API Gateway. You can\'t modify the $default route key.

ApiKeyRequired (boolean) --
Specifies whether an API key is required for this route. Supported only for WebSocket APIs.

AuthorizationScopes (list) --
A list of authorization scopes configured on a route. The scopes are used with a JWT authorizer to authorize the method invocation. The authorization works by matching the route scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any route scope matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the route scope is configured, the client must provide an access token instead of an identity token for authorization purposes.

(string) --
A string with a length between [1-64].



AuthorizationType (string) --
The authorization type for the route. For WebSocket APIs, valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer For HTTP APIs, valid values are NONE for open access, or JWT for using JSON Web Tokens.

AuthorizerId (string) --
The identifier of the Authorizer resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.

ModelSelectionExpression (string) --
The model selection expression for the route. Supported only for WebSocket APIs.

OperationName (string) --
The operation name for the route.

RequestModels (dict) --
The request models for the route. Supported only for WebSocket APIs.

(string) --

(string) --
A string with a length between [1-128].





RequestParameters (dict) --
The request parameters for the route. Supported only for WebSocket APIs.

(string) --

(dict) --
Validation constraints imposed on parameters of a request (path, query string, headers).

Required (boolean) --
Whether or not the parameter is required.







RouteId (string) --
The route ID.

RouteKey (string) --
The route key for the route.

RouteResponseSelectionExpression (string) --
The route response selection expression for the route. Supported only for WebSocket APIs.

Target (string) --
The target for the route.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {
        'ApiGatewayManaged': True|False,
        'ApiKeyRequired': True|False,
        'AuthorizationScopes': [
            'string',
        ],
        'AuthorizationType': 'NONE'|'AWS_IAM'|'CUSTOM'|'JWT',
        'AuthorizerId': 'string',
        'ModelSelectionExpression': 'string',
        'OperationName': 'string',
        'RequestModels': {
            'string': 'string'
        },
        'RequestParameters': {
            'string': {
                'Required': True|False
            }
        },
        'RouteId': 'string',
        'RouteKey': 'string',
        'RouteResponseSelectionExpression': 'string',
        'Target': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def get_route_response(ApiId=None, RouteId=None, RouteResponseId=None):
    """
    Gets a RouteResponse.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_route_response(
        ApiId='string',
        RouteId='string',
        RouteResponseId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type RouteId: string
    :param RouteId: [REQUIRED]\nThe route ID.\n

    :type RouteResponseId: string
    :param RouteResponseId: [REQUIRED]\nThe route response ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ModelSelectionExpression': 'string',
    'ResponseModels': {
        'string': 'string'
    },
    'ResponseParameters': {
        'string': {
            'Required': True|False
        }
    },
    'RouteResponseId': 'string',
    'RouteResponseKey': 'string'
}


Response Structure

(dict) --
Success

ModelSelectionExpression (string) --
Represents the model selection expression of a route response. Supported only for WebSocket APIs.

ResponseModels (dict) --
Represents the response models of a route response.

(string) --

(string) --
A string with a length between [1-128].





ResponseParameters (dict) --
Represents the response parameters of a route response.

(string) --

(dict) --
Validation constraints imposed on parameters of a request (path, query string, headers).

Required (boolean) --
Whether or not the parameter is required.







RouteResponseId (string) --
Represents the identifier of a route response.

RouteResponseKey (string) --
Represents the route response key of a route response.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {
        'ModelSelectionExpression': 'string',
        'ResponseModels': {
            'string': 'string'
        },
        'ResponseParameters': {
            'string': {
                'Required': True|False
            }
        },
        'RouteResponseId': 'string',
        'RouteResponseKey': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def get_route_responses(ApiId=None, MaxResults=None, NextToken=None, RouteId=None):
    """
    Gets the RouteResponses for a Route.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_route_responses(
        ApiId='string',
        MaxResults='string',
        NextToken='string',
        RouteId='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type MaxResults: string
    :param MaxResults: The maximum number of elements to be returned for this resource.

    :type NextToken: string
    :param NextToken: The next page of elements from this collection. Not valid for the last element of the collection.

    :type RouteId: string
    :param RouteId: [REQUIRED]\nThe route ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'ModelSelectionExpression': 'string',
            'ResponseModels': {
                'string': 'string'
            },
            'ResponseParameters': {
                'string': {
                    'Required': True|False
                }
            },
            'RouteResponseId': 'string',
            'RouteResponseKey': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success

Items (list) --
The elements from this collection.

(dict) --
Represents a route response.

ModelSelectionExpression (string) --
Represents the model selection expression of a route response. Supported only for WebSocket APIs.

ResponseModels (dict) --
Represents the response models of a route response.

(string) --

(string) --
A string with a length between [1-128].





ResponseParameters (dict) --
Represents the response parameters of a route response.

(string) --

(dict) --
Validation constraints imposed on parameters of a request (path, query string, headers).

Required (boolean) --
Whether or not the parameter is required.







RouteResponseId (string) --
Represents the identifier of a route response.

RouteResponseKey (string) --
Represents the route response key of a route response.





NextToken (string) --
The next page of elements from this collection. Not valid for the last element of the collection.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'ModelSelectionExpression': 'string',
                'ResponseModels': {
                    'string': 'string'
                },
                'ResponseParameters': {
                    'string': {
                        'Required': True|False
                    }
                },
                'RouteResponseId': 'string',
                'RouteResponseKey': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    
    """
    pass

def get_routes(ApiId=None, MaxResults=None, NextToken=None):
    """
    Gets the Routes for an API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_routes(
        ApiId='string',
        MaxResults='string',
        NextToken='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type MaxResults: string
    :param MaxResults: The maximum number of elements to be returned for this resource.

    :type NextToken: string
    :param NextToken: The next page of elements from this collection. Not valid for the last element of the collection.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'ApiGatewayManaged': True|False,
            'ApiKeyRequired': True|False,
            'AuthorizationScopes': [
                'string',
            ],
            'AuthorizationType': 'NONE'|'AWS_IAM'|'CUSTOM'|'JWT',
            'AuthorizerId': 'string',
            'ModelSelectionExpression': 'string',
            'OperationName': 'string',
            'RequestModels': {
                'string': 'string'
            },
            'RequestParameters': {
                'string': {
                    'Required': True|False
                }
            },
            'RouteId': 'string',
            'RouteKey': 'string',
            'RouteResponseSelectionExpression': 'string',
            'Target': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success

Items (list) --
The elements from this collection.

(dict) --
Represents a route.

ApiGatewayManaged (boolean) --
Specifies whether a route is managed by API Gateway. If you created an API using quick create, the $default route is managed by API Gateway. You can\'t modify the $default route key.

ApiKeyRequired (boolean) --
Specifies whether an API key is required for this route. Supported only for WebSocket APIs.

AuthorizationScopes (list) --
A list of authorization scopes configured on a route. The scopes are used with a JWT authorizer to authorize the method invocation. The authorization works by matching the route scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any route scope matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the route scope is configured, the client must provide an access token instead of an identity token for authorization purposes.

(string) --
A string with a length between [1-64].



AuthorizationType (string) --
The authorization type for the route. For WebSocket APIs, valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer For HTTP APIs, valid values are NONE for open access, or JWT for using JSON Web Tokens.

AuthorizerId (string) --
The identifier of the Authorizer resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.

ModelSelectionExpression (string) --
The model selection expression for the route. Supported only for WebSocket APIs.

OperationName (string) --
The operation name for the route.

RequestModels (dict) --
The request models for the route. Supported only for WebSocket APIs.

(string) --

(string) --
A string with a length between [1-128].





RequestParameters (dict) --
The request parameters for the route. Supported only for WebSocket APIs.

(string) --

(dict) --
Validation constraints imposed on parameters of a request (path, query string, headers).

Required (boolean) --
Whether or not the parameter is required.







RouteId (string) --
The route ID.

RouteKey (string) --
The route key for the route.

RouteResponseSelectionExpression (string) --
The route response selection expression for the route. Supported only for WebSocket APIs.

Target (string) --
The target for the route.





NextToken (string) --
The next page of elements from this collection. Not valid for the last element of the collection.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'ApiGatewayManaged': True|False,
                'ApiKeyRequired': True|False,
                'AuthorizationScopes': [
                    'string',
                ],
                'AuthorizationType': 'NONE'|'AWS_IAM'|'CUSTOM'|'JWT',
                'AuthorizerId': 'string',
                'ModelSelectionExpression': 'string',
                'OperationName': 'string',
                'RequestModels': {
                    'string': 'string'
                },
                'RequestParameters': {
                    'string': {
                        'Required': True|False
                    }
                },
                'RouteId': 'string',
                'RouteKey': 'string',
                'RouteResponseSelectionExpression': 'string',
                'Target': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    
    """
    pass

def get_stage(ApiId=None, StageName=None):
    """
    Gets a Stage.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_stage(
        ApiId='string',
        StageName='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type StageName: string
    :param StageName: [REQUIRED]\nThe stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AccessLogSettings': {
        'DestinationArn': 'string',
        'Format': 'string'
    },
    'ApiGatewayManaged': True|False,
    'AutoDeploy': True|False,
    'ClientCertificateId': 'string',
    'CreatedDate': datetime(2015, 1, 1),
    'DefaultRouteSettings': {
        'DataTraceEnabled': True|False,
        'DetailedMetricsEnabled': True|False,
        'LoggingLevel': 'ERROR'|'INFO'|'OFF',
        'ThrottlingBurstLimit': 123,
        'ThrottlingRateLimit': 123.0
    },
    'DeploymentId': 'string',
    'Description': 'string',
    'LastDeploymentStatusMessage': 'string',
    'LastUpdatedDate': datetime(2015, 1, 1),
    'RouteSettings': {
        'string': {
            'DataTraceEnabled': True|False,
            'DetailedMetricsEnabled': True|False,
            'LoggingLevel': 'ERROR'|'INFO'|'OFF',
            'ThrottlingBurstLimit': 123,
            'ThrottlingRateLimit': 123.0
        }
    },
    'StageName': 'string',
    'StageVariables': {
        'string': 'string'
    },
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Success

AccessLogSettings (dict) --
Settings for logging access in this stage.

DestinationArn (string) --
The ARN of the CloudWatch Logs log group to receive access logs.

Format (string) --
A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.



ApiGatewayManaged (boolean) --
Specifies whether a stage is managed by API Gateway. If you created an API using quick create, the $default stage is managed by API Gateway. You can\'t modify the $default stage.

AutoDeploy (boolean) --
Specifies whether updates to an API automatically trigger a new deployment. The default value is false.

ClientCertificateId (string) --
The identifier of a client certificate for a Stage. Supported only for WebSocket APIs.

CreatedDate (datetime) --
The timestamp when the stage was created.

DefaultRouteSettings (dict) --
Default route settings for the stage.

DataTraceEnabled (boolean) --
Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

DetailedMetricsEnabled (boolean) --
Specifies whether detailed metrics are enabled.

LoggingLevel (string) --
Specifies the logging level for this route: INFO, ERROR, or OFF. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

ThrottlingBurstLimit (integer) --
Specifies the throttling burst limit.

ThrottlingRateLimit (float) --
Specifies the throttling rate limit.



DeploymentId (string) --
The identifier of the Deployment that the Stage is associated with. Can\'t be updated if autoDeploy is enabled.

Description (string) --
The description of the stage.

LastDeploymentStatusMessage (string) --
Describes the status of the last deployment of a stage. Supported only for stages with autoDeploy enabled.

LastUpdatedDate (datetime) --
The timestamp when the stage was last updated.

RouteSettings (dict) --
Route settings for the stage, by routeKey.

(string) --

(dict) --
Represents a collection of route settings.

DataTraceEnabled (boolean) --
Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

DetailedMetricsEnabled (boolean) --
Specifies whether detailed metrics are enabled.

LoggingLevel (string) --
Specifies the logging level for this route: INFO, ERROR, or OFF. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

ThrottlingBurstLimit (integer) --
Specifies the throttling burst limit.

ThrottlingRateLimit (float) --
Specifies the throttling rate limit.







StageName (string) --
The name of the stage.

StageVariables (dict) --
A map that defines the stage variables for a stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.

(string) --

(string) --
A string with a length between [0-2048].





Tags (dict) --
The collection of tags. Each tag element is associated with a given resource.

(string) --

(string) --
A string with a length between [0-1600].











Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {
        'AccessLogSettings': {
            'DestinationArn': 'string',
            'Format': 'string'
        },
        'ApiGatewayManaged': True|False,
        'AutoDeploy': True|False,
        'ClientCertificateId': 'string',
        'CreatedDate': datetime(2015, 1, 1),
        'DefaultRouteSettings': {
            'DataTraceEnabled': True|False,
            'DetailedMetricsEnabled': True|False,
            'LoggingLevel': 'ERROR'|'INFO'|'OFF',
            'ThrottlingBurstLimit': 123,
            'ThrottlingRateLimit': 123.0
        },
        'DeploymentId': 'string',
        'Description': 'string',
        'LastDeploymentStatusMessage': 'string',
        'LastUpdatedDate': datetime(2015, 1, 1),
        'RouteSettings': {
            'string': {
                'DataTraceEnabled': True|False,
                'DetailedMetricsEnabled': True|False,
                'LoggingLevel': 'ERROR'|'INFO'|'OFF',
                'ThrottlingBurstLimit': 123,
                'ThrottlingRateLimit': 123.0
            }
        },
        'StageName': 'string',
        'StageVariables': {
            'string': 'string'
        },
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    
    """
    pass

def get_stages(ApiId=None, MaxResults=None, NextToken=None):
    """
    Gets the Stages for an API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_stages(
        ApiId='string',
        MaxResults='string',
        NextToken='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type MaxResults: string
    :param MaxResults: The maximum number of elements to be returned for this resource.

    :type NextToken: string
    :param NextToken: The next page of elements from this collection. Not valid for the last element of the collection.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'AccessLogSettings': {
                'DestinationArn': 'string',
                'Format': 'string'
            },
            'ApiGatewayManaged': True|False,
            'AutoDeploy': True|False,
            'ClientCertificateId': 'string',
            'CreatedDate': datetime(2015, 1, 1),
            'DefaultRouteSettings': {
                'DataTraceEnabled': True|False,
                'DetailedMetricsEnabled': True|False,
                'LoggingLevel': 'ERROR'|'INFO'|'OFF',
                'ThrottlingBurstLimit': 123,
                'ThrottlingRateLimit': 123.0
            },
            'DeploymentId': 'string',
            'Description': 'string',
            'LastDeploymentStatusMessage': 'string',
            'LastUpdatedDate': datetime(2015, 1, 1),
            'RouteSettings': {
                'string': {
                    'DataTraceEnabled': True|False,
                    'DetailedMetricsEnabled': True|False,
                    'LoggingLevel': 'ERROR'|'INFO'|'OFF',
                    'ThrottlingBurstLimit': 123,
                    'ThrottlingRateLimit': 123.0
                }
            },
            'StageName': 'string',
            'StageVariables': {
                'string': 'string'
            },
            'Tags': {
                'string': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success

Items (list) --
The elements from this collection.

(dict) --
Represents an API stage.

AccessLogSettings (dict) --
Settings for logging access in this stage.

DestinationArn (string) --
The ARN of the CloudWatch Logs log group to receive access logs.

Format (string) --
A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.



ApiGatewayManaged (boolean) --
Specifies whether a stage is managed by API Gateway. If you created an API using quick create, the $default stage is managed by API Gateway. You can\'t modify the $default stage.

AutoDeploy (boolean) --
Specifies whether updates to an API automatically trigger a new deployment. The default value is false.

ClientCertificateId (string) --
The identifier of a client certificate for a Stage. Supported only for WebSocket APIs.

CreatedDate (datetime) --
The timestamp when the stage was created.

DefaultRouteSettings (dict) --
Default route settings for the stage.

DataTraceEnabled (boolean) --
Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

DetailedMetricsEnabled (boolean) --
Specifies whether detailed metrics are enabled.

LoggingLevel (string) --
Specifies the logging level for this route: INFO, ERROR, or OFF. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

ThrottlingBurstLimit (integer) --
Specifies the throttling burst limit.

ThrottlingRateLimit (float) --
Specifies the throttling rate limit.



DeploymentId (string) --
The identifier of the Deployment that the Stage is associated with. Can\'t be updated if autoDeploy is enabled.

Description (string) --
The description of the stage.

LastDeploymentStatusMessage (string) --
Describes the status of the last deployment of a stage. Supported only for stages with autoDeploy enabled.

LastUpdatedDate (datetime) --
The timestamp when the stage was last updated.

RouteSettings (dict) --
Route settings for the stage, by routeKey.

(string) --

(dict) --
Represents a collection of route settings.

DataTraceEnabled (boolean) --
Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

DetailedMetricsEnabled (boolean) --
Specifies whether detailed metrics are enabled.

LoggingLevel (string) --
Specifies the logging level for this route: INFO, ERROR, or OFF. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

ThrottlingBurstLimit (integer) --
Specifies the throttling burst limit.

ThrottlingRateLimit (float) --
Specifies the throttling rate limit.







StageName (string) --
The name of the stage.

StageVariables (dict) --
A map that defines the stage variables for a stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.

(string) --

(string) --
A string with a length between [0-2048].





Tags (dict) --
The collection of tags. Each tag element is associated with a given resource.

(string) --

(string) --
A string with a length between [0-1600].









NextToken (string) --
The next page of elements from this collection. Not valid for the last element of the collection.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException


    :return: {
        'Items': [
            {
                'AccessLogSettings': {
                    'DestinationArn': 'string',
                    'Format': 'string'
                },
                'ApiGatewayManaged': True|False,
                'AutoDeploy': True|False,
                'ClientCertificateId': 'string',
                'CreatedDate': datetime(2015, 1, 1),
                'DefaultRouteSettings': {
                    'DataTraceEnabled': True|False,
                    'DetailedMetricsEnabled': True|False,
                    'LoggingLevel': 'ERROR'|'INFO'|'OFF',
                    'ThrottlingBurstLimit': 123,
                    'ThrottlingRateLimit': 123.0
                },
                'DeploymentId': 'string',
                'Description': 'string',
                'LastDeploymentStatusMessage': 'string',
                'LastUpdatedDate': datetime(2015, 1, 1),
                'RouteSettings': {
                    'string': {
                        'DataTraceEnabled': True|False,
                        'DetailedMetricsEnabled': True|False,
                        'LoggingLevel': 'ERROR'|'INFO'|'OFF',
                        'ThrottlingBurstLimit': 123,
                        'ThrottlingRateLimit': 123.0
                    }
                },
                'StageName': 'string',
                'StageVariables': {
                    'string': 'string'
                },
                'Tags': {
                    'string': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    
    """
    pass

def get_tags(ResourceArn=None):
    """
    Gets a collection of Tag resources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_tags(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe resource ARN for the tag.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --Success

Tags (dict) --Represents a collection of tags associated with the resource.

(string) --
(string) --A string with a length between [0-1600].










Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    """
    pass

def get_vpc_link(VpcLinkId=None):
    """
    Gets a VPC link.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_vpc_link(
        VpcLinkId='string'
    )
    
    
    :type VpcLinkId: string
    :param VpcLinkId: [REQUIRED]\nThe ID of the VPC link.\n

    :rtype: dict
ReturnsResponse Syntax{
    'CreatedDate': datetime(2015, 1, 1),
    'Name': 'string',
    'SecurityGroupIds': [
        'string',
    ],
    'SubnetIds': [
        'string',
    ],
    'Tags': {
        'string': 'string'
    },
    'VpcLinkId': 'string',
    'VpcLinkStatus': 'PENDING'|'AVAILABLE'|'DELETING'|'FAILED'|'INACTIVE',
    'VpcLinkStatusMessage': 'string',
    'VpcLinkVersion': 'V2'
}


Response Structure

(dict) --Success

CreatedDate (datetime) --The timestamp when the VPC link was created.

Name (string) --The name of the VPC link.

SecurityGroupIds (list) --A list of security group IDs for the VPC link.

(string) --


SubnetIds (list) --A list of subnet IDs to include in the VPC link.

(string) --


Tags (dict) --Tags for the VPC link.

(string) --
(string) --A string with a length between [0-1600].





VpcLinkId (string) --The ID of the VPC link.

VpcLinkStatus (string) --The status of the VPC link.

VpcLinkStatusMessage (string) --A message summarizing the cause of the status of the VPC link.

VpcLinkVersion (string) --The version of the VPC link.






Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {
        'CreatedDate': datetime(2015, 1, 1),
        'Name': 'string',
        'SecurityGroupIds': [
            'string',
        ],
        'SubnetIds': [
            'string',
        ],
        'Tags': {
            'string': 'string'
        },
        'VpcLinkId': 'string',
        'VpcLinkStatus': 'PENDING'|'AVAILABLE'|'DELETING'|'FAILED'|'INACTIVE',
        'VpcLinkStatusMessage': 'string',
        'VpcLinkVersion': 'V2'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_vpc_links(MaxResults=None, NextToken=None):
    """
    Gets a collection of VPC links.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_vpc_links(
        MaxResults='string',
        NextToken='string'
    )
    
    
    :type MaxResults: string
    :param MaxResults: The maximum number of elements to be returned for this resource.

    :type NextToken: string
    :param NextToken: The next page of elements from this collection. Not valid for the last element of the collection.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'CreatedDate': datetime(2015, 1, 1),
            'Name': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'SubnetIds': [
                'string',
            ],
            'Tags': {
                'string': 'string'
            },
            'VpcLinkId': 'string',
            'VpcLinkStatus': 'PENDING'|'AVAILABLE'|'DELETING'|'FAILED'|'INACTIVE',
            'VpcLinkStatusMessage': 'string',
            'VpcLinkVersion': 'V2'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success

Items (list) --
A collection of VPC links.

(dict) --
Represents a VPC link.

CreatedDate (datetime) --
The timestamp when the VPC link was created.

Name (string) --
The name of the VPC link.

SecurityGroupIds (list) --
A list of security group IDs for the VPC link.

(string) --


SubnetIds (list) --
A list of subnet IDs to include in the VPC link.

(string) --


Tags (dict) --
Tags for the VPC link.

(string) --

(string) --
A string with a length between [0-1600].





VpcLinkId (string) --
The ID of the VPC link.

VpcLinkStatus (string) --
The status of the VPC link.

VpcLinkStatusMessage (string) --
A message summarizing the cause of the status of the VPC link.

VpcLinkVersion (string) --
The version of the VPC link.





NextToken (string) --
The next page of elements from this collection. Not valid for the last element of the collection.







Exceptions

ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.TooManyRequestsException


    :return: {
        'Items': [
            {
                'CreatedDate': datetime(2015, 1, 1),
                'Name': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'SubnetIds': [
                    'string',
                ],
                'Tags': {
                    'string': 'string'
                },
                'VpcLinkId': 'string',
                'VpcLinkStatus': 'PENDING'|'AVAILABLE'|'DELETING'|'FAILED'|'INACTIVE',
                'VpcLinkStatusMessage': 'string',
                'VpcLinkVersion': 'V2'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
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

def import_api(Basepath=None, Body=None, FailOnWarnings=None):
    """
    Imports an API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.import_api(
        Basepath='string',
        Body='string',
        FailOnWarnings=True|False
    )
    
    
    :type Basepath: string
    :param Basepath: Specifies how to interpret the base path of the API during import. Valid values are ignore, prepend, and split. The default value is ignore. To learn more, see Set the OpenAPI basePath Property . Supported only for HTTP APIs.

    :type Body: string
    :param Body: [REQUIRED]\nThe OpenAPI definition. Supported only for HTTP APIs.\n

    :type FailOnWarnings: boolean
    :param FailOnWarnings: Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiEndpoint': 'string',
    'ApiId': 'string',
    'ApiKeySelectionExpression': 'string',
    'CorsConfiguration': {
        'AllowCredentials': True|False,
        'AllowHeaders': [
            'string',
        ],
        'AllowMethods': [
            'string',
        ],
        'AllowOrigins': [
            'string',
        ],
        'ExposeHeaders': [
            'string',
        ],
        'MaxAge': 123
    },
    'CreatedDate': datetime(2015, 1, 1),
    'Description': 'string',
    'DisableSchemaValidation': True|False,
    'ImportInfo': [
        'string',
    ],
    'Name': 'string',
    'ProtocolType': 'WEBSOCKET'|'HTTP',
    'RouteSelectionExpression': 'string',
    'Tags': {
        'string': 'string'
    },
    'Version': 'string',
    'Warnings': [
        'string',
    ]
}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.

ApiEndpoint (string) --
The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage.

ApiId (string) --
The API ID.

ApiKeySelectionExpression (string) --
An API key selection expression. Supported only for WebSocket APIs. See API Key Selection Expressions .

CorsConfiguration (dict) --
A CORS configuration. Supported only for HTTP APIs.

AllowCredentials (boolean) --
Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.

AllowHeaders (list) --
Represents a collection of allowed headers. Supported only for HTTP APIs.

(string) --


AllowMethods (list) --
Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.

(string) --
A string with a length between [1-64].



AllowOrigins (list) --
Represents a collection of allowed origins. Supported only for HTTP APIs.

(string) --


ExposeHeaders (list) --
Represents a collection of exposed headers. Supported only for HTTP APIs.

(string) --


MaxAge (integer) --
The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.



CreatedDate (datetime) --
The timestamp when the API was created.

Description (string) --
The description of the API.

DisableSchemaValidation (boolean) --
Avoid validating models when creating a deployment. Supported only for WebSocket APIs.

ImportInfo (list) --
The validation information during API import. This may include particular properties of your OpenAPI definition which are ignored during import. Supported only for HTTP APIs.

(string) --


Name (string) --
The name of the API.

ProtocolType (string) --
The API protocol.

RouteSelectionExpression (string) --
The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.

Tags (dict) --
A collection of tags associated with the API.

(string) --

(string) --
A string with a length between [0-1600].





Version (string) --
A version identifier for the API.

Warnings (list) --
The warning messages reported when failonwarnings is turned on during API import.

(string) --








Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ApiEndpoint': 'string',
        'ApiId': 'string',
        'ApiKeySelectionExpression': 'string',
        'CorsConfiguration': {
            'AllowCredentials': True|False,
            'AllowHeaders': [
                'string',
            ],
            'AllowMethods': [
                'string',
            ],
            'AllowOrigins': [
                'string',
            ],
            'ExposeHeaders': [
                'string',
            ],
            'MaxAge': 123
        },
        'CreatedDate': datetime(2015, 1, 1),
        'Description': 'string',
        'DisableSchemaValidation': True|False,
        'ImportInfo': [
            'string',
        ],
        'Name': 'string',
        'ProtocolType': 'WEBSOCKET'|'HTTP',
        'RouteSelectionExpression': 'string',
        'Tags': {
            'string': 'string'
        },
        'Version': 'string',
        'Warnings': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def reimport_api(ApiId=None, Basepath=None, Body=None, FailOnWarnings=None):
    """
    Puts an Api resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reimport_api(
        ApiId='string',
        Basepath='string',
        Body='string',
        FailOnWarnings=True|False
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type Basepath: string
    :param Basepath: Specifies how to interpret the base path of the API during import. Valid values are ignore, prepend, and split. The default value is ignore. To learn more, see Set the OpenAPI basePath Property . Supported only for HTTP APIs.

    :type Body: string
    :param Body: [REQUIRED]\nThe OpenAPI definition. Supported only for HTTP APIs.\n

    :type FailOnWarnings: boolean
    :param FailOnWarnings: Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiEndpoint': 'string',
    'ApiId': 'string',
    'ApiKeySelectionExpression': 'string',
    'CorsConfiguration': {
        'AllowCredentials': True|False,
        'AllowHeaders': [
            'string',
        ],
        'AllowMethods': [
            'string',
        ],
        'AllowOrigins': [
            'string',
        ],
        'ExposeHeaders': [
            'string',
        ],
        'MaxAge': 123
    },
    'CreatedDate': datetime(2015, 1, 1),
    'Description': 'string',
    'DisableSchemaValidation': True|False,
    'ImportInfo': [
        'string',
    ],
    'Name': 'string',
    'ProtocolType': 'WEBSOCKET'|'HTTP',
    'RouteSelectionExpression': 'string',
    'Tags': {
        'string': 'string'
    },
    'Version': 'string',
    'Warnings': [
        'string',
    ]
}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.

ApiEndpoint (string) --
The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage.

ApiId (string) --
The API ID.

ApiKeySelectionExpression (string) --
An API key selection expression. Supported only for WebSocket APIs. See API Key Selection Expressions .

CorsConfiguration (dict) --
A CORS configuration. Supported only for HTTP APIs.

AllowCredentials (boolean) --
Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.

AllowHeaders (list) --
Represents a collection of allowed headers. Supported only for HTTP APIs.

(string) --


AllowMethods (list) --
Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.

(string) --
A string with a length between [1-64].



AllowOrigins (list) --
Represents a collection of allowed origins. Supported only for HTTP APIs.

(string) --


ExposeHeaders (list) --
Represents a collection of exposed headers. Supported only for HTTP APIs.

(string) --


MaxAge (integer) --
The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.



CreatedDate (datetime) --
The timestamp when the API was created.

Description (string) --
The description of the API.

DisableSchemaValidation (boolean) --
Avoid validating models when creating a deployment. Supported only for WebSocket APIs.

ImportInfo (list) --
The validation information during API import. This may include particular properties of your OpenAPI definition which are ignored during import. Supported only for HTTP APIs.

(string) --


Name (string) --
The name of the API.

ProtocolType (string) --
The API protocol.

RouteSelectionExpression (string) --
The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.

Tags (dict) --
A collection of tags associated with the API.

(string) --

(string) --
A string with a length between [0-1600].





Version (string) --
A version identifier for the API.

Warnings (list) --
The warning messages reported when failonwarnings is turned on during API import.

(string) --








Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ApiEndpoint': 'string',
        'ApiId': 'string',
        'ApiKeySelectionExpression': 'string',
        'CorsConfiguration': {
            'AllowCredentials': True|False,
            'AllowHeaders': [
                'string',
            ],
            'AllowMethods': [
                'string',
            ],
            'AllowOrigins': [
                'string',
            ],
            'ExposeHeaders': [
                'string',
            ],
            'MaxAge': 123
        },
        'CreatedDate': datetime(2015, 1, 1),
        'Description': 'string',
        'DisableSchemaValidation': True|False,
        'ImportInfo': [
            'string',
        ],
        'Name': 'string',
        'ProtocolType': 'WEBSOCKET'|'HTTP',
        'RouteSelectionExpression': 'string',
        'Tags': {
            'string': 'string'
        },
        'Version': 'string',
        'Warnings': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Creates a new Tag resource to represent a tag.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe resource ARN for the tag.\n

    :type Tags: dict
    :param Tags: The collection of tags. Each tag element is associated with a given resource.\n\n(string) --\n(string) --A string with a length between [0-1600].\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The request has succeeded and has resulted in the creation of a resource.





Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {}
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Deletes a Tag.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe resource ARN for the tag.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe Tag keys to delete\n\n(string) --\n\n

    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def update_api(ApiId=None, ApiKeySelectionExpression=None, CorsConfiguration=None, CredentialsArn=None, Description=None, DisableSchemaValidation=None, Name=None, RouteKey=None, RouteSelectionExpression=None, Target=None, Version=None):
    """
    Updates an Api resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_api(
        ApiId='string',
        ApiKeySelectionExpression='string',
        CorsConfiguration={
            'AllowCredentials': True|False,
            'AllowHeaders': [
                'string',
            ],
            'AllowMethods': [
                'string',
            ],
            'AllowOrigins': [
                'string',
            ],
            'ExposeHeaders': [
                'string',
            ],
            'MaxAge': 123
        },
        CredentialsArn='string',
        Description='string',
        DisableSchemaValidation=True|False,
        Name='string',
        RouteKey='string',
        RouteSelectionExpression='string',
        Target='string',
        Version='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ApiKeySelectionExpression: string
    :param ApiKeySelectionExpression: An API key selection expression. Supported only for WebSocket APIs. See API Key Selection Expressions .

    :type CorsConfiguration: dict
    :param CorsConfiguration: A CORS configuration. Supported only for HTTP APIs.\n\nAllowCredentials (boolean) --Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.\n\nAllowHeaders (list) --Represents a collection of allowed headers. Supported only for HTTP APIs.\n\n(string) --\n\n\nAllowMethods (list) --Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.\n\n(string) --A string with a length between [1-64].\n\n\n\nAllowOrigins (list) --Represents a collection of allowed origins. Supported only for HTTP APIs.\n\n(string) --\n\n\nExposeHeaders (list) --Represents a collection of exposed headers. Supported only for HTTP APIs.\n\n(string) --\n\n\nMaxAge (integer) --The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.\n\n\n

    :type CredentialsArn: string
    :param CredentialsArn: This property is part of quick create. It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To require that the caller\'s identity be passed through from the request, specify arn:aws:iam:::user/. To use resource-based permissions on supported AWS services, specify null. Currently, this property is not used for HTTP integrations. If provided, this value replaces the credentials associated with the quick create integration. Supported only for HTTP APIs.

    :type Description: string
    :param Description: The description of the API.

    :type DisableSchemaValidation: boolean
    :param DisableSchemaValidation: Avoid validating models when creating a deployment. Supported only for WebSocket APIs.

    :type Name: string
    :param Name: The name of the API.

    :type RouteKey: string
    :param RouteKey: This property is part of quick create. If not specified, the route created using quick create is kept. Otherwise, this value replaces the route key of the quick create route. Additional routes may still be added after the API is updated. Supported only for HTTP APIs.

    :type RouteSelectionExpression: string
    :param RouteSelectionExpression: The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.

    :type Target: string
    :param Target: This property is part of quick create. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. The value provided updates the integration URI and integration type. You can update a quick-created target, but you can\'t remove it from an API. Supported only for HTTP APIs.

    :type Version: string
    :param Version: A version identifier for the API.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiEndpoint': 'string',
    'ApiId': 'string',
    'ApiKeySelectionExpression': 'string',
    'CorsConfiguration': {
        'AllowCredentials': True|False,
        'AllowHeaders': [
            'string',
        ],
        'AllowMethods': [
            'string',
        ],
        'AllowOrigins': [
            'string',
        ],
        'ExposeHeaders': [
            'string',
        ],
        'MaxAge': 123
    },
    'CreatedDate': datetime(2015, 1, 1),
    'Description': 'string',
    'DisableSchemaValidation': True|False,
    'ImportInfo': [
        'string',
    ],
    'Name': 'string',
    'ProtocolType': 'WEBSOCKET'|'HTTP',
    'RouteSelectionExpression': 'string',
    'Tags': {
        'string': 'string'
    },
    'Version': 'string',
    'Warnings': [
        'string',
    ]
}


Response Structure

(dict) --
Success

ApiEndpoint (string) --
The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage.

ApiId (string) --
The API ID.

ApiKeySelectionExpression (string) --
An API key selection expression. Supported only for WebSocket APIs. See API Key Selection Expressions .

CorsConfiguration (dict) --
A CORS configuration. Supported only for HTTP APIs.

AllowCredentials (boolean) --
Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.

AllowHeaders (list) --
Represents a collection of allowed headers. Supported only for HTTP APIs.

(string) --


AllowMethods (list) --
Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.

(string) --
A string with a length between [1-64].



AllowOrigins (list) --
Represents a collection of allowed origins. Supported only for HTTP APIs.

(string) --


ExposeHeaders (list) --
Represents a collection of exposed headers. Supported only for HTTP APIs.

(string) --


MaxAge (integer) --
The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.



CreatedDate (datetime) --
The timestamp when the API was created.

Description (string) --
The description of the API.

DisableSchemaValidation (boolean) --
Avoid validating models when creating a deployment. Supported only for WebSocket APIs.

ImportInfo (list) --
The validation information during API import. This may include particular properties of your OpenAPI definition which are ignored during import. Supported only for HTTP APIs.

(string) --


Name (string) --
The name of the API.

ProtocolType (string) --
The API protocol.

RouteSelectionExpression (string) --
The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.

Tags (dict) --
A collection of tags associated with the API.

(string) --

(string) --
A string with a length between [0-1600].





Version (string) --
A version identifier for the API.

Warnings (list) --
The warning messages reported when failonwarnings is turned on during API import.

(string) --








Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ApiEndpoint': 'string',
        'ApiId': 'string',
        'ApiKeySelectionExpression': 'string',
        'CorsConfiguration': {
            'AllowCredentials': True|False,
            'AllowHeaders': [
                'string',
            ],
            'AllowMethods': [
                'string',
            ],
            'AllowOrigins': [
                'string',
            ],
            'ExposeHeaders': [
                'string',
            ],
            'MaxAge': 123
        },
        'CreatedDate': datetime(2015, 1, 1),
        'Description': 'string',
        'DisableSchemaValidation': True|False,
        'ImportInfo': [
            'string',
        ],
        'Name': 'string',
        'ProtocolType': 'WEBSOCKET'|'HTTP',
        'RouteSelectionExpression': 'string',
        'Tags': {
            'string': 'string'
        },
        'Version': 'string',
        'Warnings': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_api_mapping(ApiId=None, ApiMappingId=None, ApiMappingKey=None, DomainName=None, Stage=None):
    """
    The API mapping.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_api_mapping(
        ApiId='string',
        ApiMappingId='string',
        ApiMappingKey='string',
        DomainName='string',
        Stage='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ApiMappingId: string
    :param ApiMappingId: [REQUIRED]\nThe API mapping identifier.\n

    :type ApiMappingKey: string
    :param ApiMappingKey: The API mapping key.

    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe domain name.\n

    :type Stage: string
    :param Stage: The API stage.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiId': 'string',
    'ApiMappingId': 'string',
    'ApiMappingKey': 'string',
    'Stage': 'string'
}


Response Structure

(dict) --
Success

ApiId (string) --
The API identifier.

ApiMappingId (string) --
The API mapping identifier.

ApiMappingKey (string) --
The API mapping key.

Stage (string) --
The API stage.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ApiId': 'string',
        'ApiMappingId': 'string',
        'ApiMappingKey': 'string',
        'Stage': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def update_authorizer(ApiId=None, AuthorizerCredentialsArn=None, AuthorizerId=None, AuthorizerResultTtlInSeconds=None, AuthorizerType=None, AuthorizerUri=None, IdentitySource=None, IdentityValidationExpression=None, JwtConfiguration=None, Name=None):
    """
    Updates an Authorizer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_authorizer(
        ApiId='string',
        AuthorizerCredentialsArn='string',
        AuthorizerId='string',
        AuthorizerResultTtlInSeconds=123,
        AuthorizerType='REQUEST'|'JWT',
        AuthorizerUri='string',
        IdentitySource=[
            'string',
        ],
        IdentityValidationExpression='string',
        JwtConfiguration={
            'Audience': [
                'string',
            ],
            'Issuer': 'string'
        },
        Name='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type AuthorizerCredentialsArn: string
    :param AuthorizerCredentialsArn: Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.

    :type AuthorizerId: string
    :param AuthorizerId: [REQUIRED]\nThe authorizer identifier.\n

    :type AuthorizerResultTtlInSeconds: integer
    :param AuthorizerResultTtlInSeconds: Authorizer caching is not currently supported. Don\'t specify this value for authorizers.

    :type AuthorizerType: string
    :param AuthorizerType: The authorizer type. For WebSocket APIs, specify REQUEST for a Lambda function using incoming request parameters. For HTTP APIs, specify JWT to use JSON Web Tokens.

    :type AuthorizerUri: string
    :param AuthorizerUri: The authorizer\'s Uniform Resource Identifier (URI). For REQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations. In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api}, where {region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations. Supported only for REQUEST authorizers.

    :type IdentitySource: list
    :param IdentitySource: The identity source for which authorization is requested.\nFor a REQUEST authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. Currently, the identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name. These parameters will be used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function.\nFor JWT, a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example '$request.header.Authorization'.\n\n(string) --\n\n

    :type IdentityValidationExpression: string
    :param IdentityValidationExpression: This parameter is not used.

    :type JwtConfiguration: dict
    :param JwtConfiguration: Represents the configuration of a JWT authorizer. Required for the JWT authorizer type. Supported only for HTTP APIs.\n\nAudience (list) --A list of the intended recipients of the JWT. A valid JWT must provide an aud that matches at least one entry in this list. See RFC 7519 . Supported only for HTTP APIs.\n\n(string) --\n\n\nIssuer (string) --The base domain of the identity provider that issues JSON Web Tokens. For example, an Amazon Cognito user pool has the following format: https://cognito-idp.{region}.amazonaws.com/{userPoolId}. Required for the JWT authorizer type. Supported only for HTTP APIs.\n\n\n

    :type Name: string
    :param Name: The name of the authorizer.

    :rtype: dict

ReturnsResponse Syntax
{
    'AuthorizerCredentialsArn': 'string',
    'AuthorizerId': 'string',
    'AuthorizerResultTtlInSeconds': 123,
    'AuthorizerType': 'REQUEST'|'JWT',
    'AuthorizerUri': 'string',
    'IdentitySource': [
        'string',
    ],
    'IdentityValidationExpression': 'string',
    'JwtConfiguration': {
        'Audience': [
            'string',
        ],
        'Issuer': 'string'
    },
    'Name': 'string'
}


Response Structure

(dict) --
Success

AuthorizerCredentialsArn (string) --
Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null. Supported only for REQUEST authorizers.

AuthorizerId (string) --
The authorizer identifier.

AuthorizerResultTtlInSeconds (integer) --
Authorizer caching is not currently supported. Don\'t specify this value for authorizers.

AuthorizerType (string) --
The authorizer type. For WebSocket APIs, specify REQUEST for a Lambda function using incoming request parameters. For HTTP APIs, specify JWT to use JSON Web Tokens.

AuthorizerUri (string) --
The authorizer\'s Uniform Resource Identifier (URI). ForREQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations. In general, the URI has this form: arn:aws:apigateway:{region}:lambda:path/{service_api}, where {region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations. Supported only for REQUEST authorizers.

IdentitySource (list) --
The identity source for which authorization is requested.
For a REQUEST authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. Currently, the identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name. These parameters will be used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function.
For JWT, a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example "$request.header.Authorization".

(string) --


IdentityValidationExpression (string) --
The validation expression does not apply to the REQUEST authorizer.

JwtConfiguration (dict) --
Represents the configuration of a JWT authorizer. Required for the JWT authorizer type. Supported only for HTTP APIs.

Audience (list) --
A list of the intended recipients of the JWT. A valid JWT must provide an aud that matches at least one entry in this list. See RFC 7519 . Supported only for HTTP APIs.

(string) --


Issuer (string) --
The base domain of the identity provider that issues JSON Web Tokens. For example, an Amazon Cognito user pool has the following format: https://cognito-idp.{region}.amazonaws.com/{userPoolId}. Required for the JWT authorizer type. Supported only for HTTP APIs.



Name (string) --
The name of the authorizer.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'AuthorizerCredentialsArn': 'string',
        'AuthorizerId': 'string',
        'AuthorizerResultTtlInSeconds': 123,
        'AuthorizerType': 'REQUEST'|'JWT',
        'AuthorizerUri': 'string',
        'IdentitySource': [
            'string',
        ],
        'IdentityValidationExpression': 'string',
        'JwtConfiguration': {
            'Audience': [
                'string',
            ],
            'Issuer': 'string'
        },
        'Name': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_deployment(ApiId=None, DeploymentId=None, Description=None):
    """
    Updates a Deployment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_deployment(
        ApiId='string',
        DeploymentId='string',
        Description='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type DeploymentId: string
    :param DeploymentId: [REQUIRED]\nThe deployment ID.\n

    :type Description: string
    :param Description: The description for the deployment resource.

    :rtype: dict

ReturnsResponse Syntax
{
    'AutoDeployed': True|False,
    'CreatedDate': datetime(2015, 1, 1),
    'DeploymentId': 'string',
    'DeploymentStatus': 'PENDING'|'FAILED'|'DEPLOYED',
    'DeploymentStatusMessage': 'string',
    'Description': 'string'
}


Response Structure

(dict) --
Success

AutoDeployed (boolean) --
Specifies whether a deployment was automatically released.

CreatedDate (datetime) --
The date and time when the Deployment resource was created.

DeploymentId (string) --
The identifier for the deployment.

DeploymentStatus (string) --
The status of the deployment: PENDING, FAILED, or SUCCEEDED.

DeploymentStatusMessage (string) --
May contain additional feedback on the status of an API deployment.

Description (string) --
The description for the deployment.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'AutoDeployed': True|False,
        'CreatedDate': datetime(2015, 1, 1),
        'DeploymentId': 'string',
        'DeploymentStatus': 'PENDING'|'FAILED'|'DEPLOYED',
        'DeploymentStatusMessage': 'string',
        'Description': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def update_domain_name(DomainName=None, DomainNameConfigurations=None):
    """
    Updates a domain name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_domain_name(
        DomainName='string',
        DomainNameConfigurations=[
            {
                'ApiGatewayDomainName': 'string',
                'CertificateArn': 'string',
                'CertificateName': 'string',
                'CertificateUploadDate': datetime(2015, 1, 1),
                'DomainNameStatus': 'AVAILABLE'|'UPDATING',
                'DomainNameStatusMessage': 'string',
                'EndpointType': 'REGIONAL'|'EDGE',
                'HostedZoneId': 'string',
                'SecurityPolicy': 'TLS_1_0'|'TLS_1_2'
            },
        ]
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe domain name.\n

    :type DomainNameConfigurations: list
    :param DomainNameConfigurations: The domain name configurations.\n\n(dict) --The domain name configuration.\n\nApiGatewayDomainName (string) --A domain name for the API.\n\nCertificateArn (string) --An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.\n\nCertificateName (string) --The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.\n\nCertificateUploadDate (datetime) --The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.\n\nDomainNameStatus (string) --The status of the domain name migration. The valid values are AVAILABLE and UPDATING. If the status is UPDATING, the domain cannot be modified further until the existing operation is complete. If it is AVAILABLE, the domain can be updated.\n\nDomainNameStatusMessage (string) --An optional text message containing detailed information about status of the domain name migration.\n\nEndpointType (string) --The endpoint type.\n\nHostedZoneId (string) --The Amazon Route 53 Hosted Zone ID of the endpoint.\n\nSecurityPolicy (string) --The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are TLS_1_0 and TLS_1_2.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiMappingSelectionExpression': 'string',
    'DomainName': 'string',
    'DomainNameConfigurations': [
        {
            'ApiGatewayDomainName': 'string',
            'CertificateArn': 'string',
            'CertificateName': 'string',
            'CertificateUploadDate': datetime(2015, 1, 1),
            'DomainNameStatus': 'AVAILABLE'|'UPDATING',
            'DomainNameStatusMessage': 'string',
            'EndpointType': 'REGIONAL'|'EDGE',
            'HostedZoneId': 'string',
            'SecurityPolicy': 'TLS_1_0'|'TLS_1_2'
        },
    ],
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Success

ApiMappingSelectionExpression (string) --
The API mapping selection expression.

DomainName (string) --
The name of the DomainName resource.

DomainNameConfigurations (list) --
The domain name configurations.

(dict) --
The domain name configuration.

ApiGatewayDomainName (string) --
A domain name for the API.

CertificateArn (string) --
An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.

CertificateName (string) --
The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.

CertificateUploadDate (datetime) --
The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.

DomainNameStatus (string) --
The status of the domain name migration. The valid values are AVAILABLE and UPDATING. If the status is UPDATING, the domain cannot be modified further until the existing operation is complete. If it is AVAILABLE, the domain can be updated.

DomainNameStatusMessage (string) --
An optional text message containing detailed information about status of the domain name migration.

EndpointType (string) --
The endpoint type.

HostedZoneId (string) --
The Amazon Route 53 Hosted Zone ID of the endpoint.

SecurityPolicy (string) --
The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are TLS_1_0 and TLS_1_2.





Tags (dict) --
The collection of tags associated with a domain name.

(string) --

(string) --
A string with a length between [0-1600].











Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ApiMappingSelectionExpression': 'string',
        'DomainName': 'string',
        'DomainNameConfigurations': [
            {
                'ApiGatewayDomainName': 'string',
                'CertificateArn': 'string',
                'CertificateName': 'string',
                'CertificateUploadDate': datetime(2015, 1, 1),
                'DomainNameStatus': 'AVAILABLE'|'UPDATING',
                'DomainNameStatusMessage': 'string',
                'EndpointType': 'REGIONAL'|'EDGE',
                'HostedZoneId': 'string',
                'SecurityPolicy': 'TLS_1_0'|'TLS_1_2'
            },
        ],
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def update_integration(ApiId=None, ConnectionId=None, ConnectionType=None, ContentHandlingStrategy=None, CredentialsArn=None, Description=None, IntegrationId=None, IntegrationMethod=None, IntegrationType=None, IntegrationUri=None, PassthroughBehavior=None, PayloadFormatVersion=None, RequestParameters=None, RequestTemplates=None, TemplateSelectionExpression=None, TimeoutInMillis=None, TlsConfig=None):
    """
    Updates an Integration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_integration(
        ApiId='string',
        ConnectionId='string',
        ConnectionType='INTERNET'|'VPC_LINK',
        ContentHandlingStrategy='CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
        CredentialsArn='string',
        Description='string',
        IntegrationId='string',
        IntegrationMethod='string',
        IntegrationType='AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
        IntegrationUri='string',
        PassthroughBehavior='WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
        PayloadFormatVersion='string',
        RequestParameters={
            'string': 'string'
        },
        RequestTemplates={
            'string': 'string'
        },
        TemplateSelectionExpression='string',
        TimeoutInMillis=123,
        TlsConfig={
            'ServerNameToVerify': 'string'
        }
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ConnectionId: string
    :param ConnectionId: The ID of the VPC link for a private integration. Supported only for HTTP APIs.

    :type ConnectionType: string
    :param ConnectionType: The type of the network connection to the integration endpoint. Specify INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and resources in a VPC. The default value is INTERNET.

    :type ContentHandlingStrategy: string
    :param ContentHandlingStrategy: Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:\nCONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.\nCONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.\nIf this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.\n

    :type CredentialsArn: string
    :param CredentialsArn: Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To require that the caller\'s identity be passed through from the request, specify the string arn:aws:iam:::user/. To use resource-based permissions on supported AWS services, specify null.

    :type Description: string
    :param Description: The description of the integration

    :type IntegrationId: string
    :param IntegrationId: [REQUIRED]\nThe integration ID.\n

    :type IntegrationMethod: string
    :param IntegrationMethod: Specifies the integration\'s HTTP method type.

    :type IntegrationType: string
    :param IntegrationType: The integration type of an integration. One of the following:\nAWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs.\nAWS_PROXY: for integrating the route or method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as Lambda proxy integration.\nHTTP: for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs.\nHTTP_PROXY: for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration. For HTTP API private integrations, use an HTTP_PROXY integration.\nMOCK: for integrating the route or method request with API Gateway as a 'loopback' endpoint without invoking any backend. Supported only for WebSocket APIs.\n

    :type IntegrationUri: string
    :param IntegrationUri: For a Lambda integration, specify the URI of a Lambda function.\nFor an HTTP integration, specify a fully-qualified URL.\nFor an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service. If you specify the ARN of an AWS Cloud Map service, API Gateway uses DiscoverInstances to identify resources. You can use query parameters to target specific resources. To learn more, see DiscoverInstances . For private integrations, all resources must be owned by the same AWS account.\n

    :type PassthroughBehavior: string
    :param PassthroughBehavior: Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Supported only for WebSocket APIs.\nWHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.\nNEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.\nWHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.\n

    :type PayloadFormatVersion: string
    :param PayloadFormatVersion: Specifies the format of the payload sent to an integration. Required for HTTP APIs.

    :type RequestParameters: dict
    :param RequestParameters: A key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.{location}.{name}, where {location}is querystring, path, or header; and {name}must be a valid and unique method request parameter name. Supported only for WebSocket APIs.\n\n(string) --\n(string) --A string with a length between [1-512].\n\n\n\n\n

    :type RequestTemplates: dict
    :param RequestTemplates: Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value. Supported only for WebSocket APIs.\n\n(string) --\n(string) --A string with a length between [0-32768].\n\n\n\n\n

    :type TemplateSelectionExpression: string
    :param TemplateSelectionExpression: The template selection expression for the integration.

    :type TimeoutInMillis: integer
    :param TimeoutInMillis: Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.

    :type TlsConfig: dict
    :param TlsConfig: The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.\n\nServerNameToVerify (string) --If you specify a server name, API Gateway uses it to verify the hostname on the integration\'s certificate. The server name is also included in the TLS handshake to support Server Name Indication (SNI) or virtual hosting.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiGatewayManaged': True|False,
    'ConnectionId': 'string',
    'ConnectionType': 'INTERNET'|'VPC_LINK',
    'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
    'CredentialsArn': 'string',
    'Description': 'string',
    'IntegrationId': 'string',
    'IntegrationMethod': 'string',
    'IntegrationResponseSelectionExpression': 'string',
    'IntegrationType': 'AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
    'IntegrationUri': 'string',
    'PassthroughBehavior': 'WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
    'PayloadFormatVersion': 'string',
    'RequestParameters': {
        'string': 'string'
    },
    'RequestTemplates': {
        'string': 'string'
    },
    'TemplateSelectionExpression': 'string',
    'TimeoutInMillis': 123,
    'TlsConfig': {
        'ServerNameToVerify': 'string'
    }
}


Response Structure

(dict) --
Success

ApiGatewayManaged (boolean) --
Specifies whether an integration is managed by API Gateway. If you created an API using using quick create, the resulting integration is managed by API Gateway. You can update a managed integration, but you can\'t delete it.

ConnectionId (string) --
The ID of the VPC link for a private integration. Supported only for HTTP APIs.

ConnectionType (string) --
The type of the network connection to the integration endpoint. Specify INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and resources in a VPC. The default value is INTERNET.

ContentHandlingStrategy (string) --
Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.

CredentialsArn (string) --
Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role\'s Amazon Resource Name (ARN). To require that the caller\'s identity be passed through from the request, specify the string arn:aws:iam:::user/. To use resource-based permissions on supported AWS services, specify null.

Description (string) --
Represents the description of an integration.

IntegrationId (string) --
Represents the identifier of an integration.

IntegrationMethod (string) --
Specifies the integration\'s HTTP method type.

IntegrationResponseSelectionExpression (string) --
The integration response selection expression for the integration. Supported only for WebSocket APIs. See Integration Response Selection Expressions .

IntegrationType (string) --
The integration type of an integration. One of the following:
AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs.
AWS_PROXY: for integrating the route or method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as Lambda proxy integration.
HTTP: for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs.
HTTP_PROXY: for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration.
MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend. Supported only for WebSocket APIs.

IntegrationUri (string) --
For a Lambda integration, specify the URI of a Lambda function.
For an HTTP integration, specify a fully-qualified URL.
For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service. If you specify the ARN of an AWS Cloud Map service, API Gateway uses DiscoverInstances to identify resources. You can use query parameters to target specific resources. To learn more, see DiscoverInstances . For private integrations, all resources must be owned by the same AWS account.

PassthroughBehavior (string) --
Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Supported only for WebSocket APIs.
WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.
NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.
WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.

PayloadFormatVersion (string) --
Specifies the format of the payload sent to an integration. Required for HTTP APIs.

RequestParameters (dict) --
A key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.{location}.{name}, where {location}is querystring, path, or header; and {name}must be a valid and unique method request parameter name. Supported only for WebSocket APIs.

(string) --

(string) --
A string with a length between [1-512].





RequestTemplates (dict) --
Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value. Supported only for WebSocket APIs.

(string) --

(string) --
A string with a length between [0-32768].





TemplateSelectionExpression (string) --
The template selection expression for the integration. Supported only for WebSocket APIs.

TimeoutInMillis (integer) --
Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.

TlsConfig (dict) --
The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.

ServerNameToVerify (string) --
If you specify a server name, API Gateway uses it to verify the hostname on the integration\'s certificate. The server name is also included in the TLS handshake to support Server Name Indication (SNI) or virtual hosting.









Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ApiGatewayManaged': True|False,
        'ConnectionId': 'string',
        'ConnectionType': 'INTERNET'|'VPC_LINK',
        'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
        'CredentialsArn': 'string',
        'Description': 'string',
        'IntegrationId': 'string',
        'IntegrationMethod': 'string',
        'IntegrationResponseSelectionExpression': 'string',
        'IntegrationType': 'AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
        'IntegrationUri': 'string',
        'PassthroughBehavior': 'WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
        'PayloadFormatVersion': 'string',
        'RequestParameters': {
            'string': 'string'
        },
        'RequestTemplates': {
            'string': 'string'
        },
        'TemplateSelectionExpression': 'string',
        'TimeoutInMillis': 123,
        'TlsConfig': {
            'ServerNameToVerify': 'string'
        }
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def update_integration_response(ApiId=None, ContentHandlingStrategy=None, IntegrationId=None, IntegrationResponseId=None, IntegrationResponseKey=None, ResponseParameters=None, ResponseTemplates=None, TemplateSelectionExpression=None):
    """
    Updates an IntegrationResponses.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_integration_response(
        ApiId='string',
        ContentHandlingStrategy='CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
        IntegrationId='string',
        IntegrationResponseId='string',
        IntegrationResponseKey='string',
        ResponseParameters={
            'string': 'string'
        },
        ResponseTemplates={
            'string': 'string'
        },
        TemplateSelectionExpression='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ContentHandlingStrategy: string
    :param ContentHandlingStrategy: Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:\nCONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.\nCONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.\nIf this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.\n

    :type IntegrationId: string
    :param IntegrationId: [REQUIRED]\nThe integration ID.\n

    :type IntegrationResponseId: string
    :param IntegrationResponseId: [REQUIRED]\nThe integration response ID.\n

    :type IntegrationResponseKey: string
    :param IntegrationResponseKey: The integration response key.

    :type ResponseParameters: dict
    :param ResponseParameters: A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name}or integration.response.body.{JSON-expression}, where {name}is a valid and unique response header name and {JSON-expression}is a valid JSON expression without the $ prefix.\n\n(string) --\n(string) --A string with a length between [1-512].\n\n\n\n\n

    :type ResponseTemplates: dict
    :param ResponseTemplates: The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.\n\n(string) --\n(string) --A string with a length between [0-32768].\n\n\n\n\n

    :type TemplateSelectionExpression: string
    :param TemplateSelectionExpression: The template selection expression for the integration response. Supported only for WebSocket APIs.

    :rtype: dict

ReturnsResponse Syntax
{
    'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
    'IntegrationResponseId': 'string',
    'IntegrationResponseKey': 'string',
    'ResponseParameters': {
        'string': 'string'
    },
    'ResponseTemplates': {
        'string': 'string'
    },
    'TemplateSelectionExpression': 'string'
}


Response Structure

(dict) --
Success

ContentHandlingStrategy (string) --
Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.

IntegrationResponseId (string) --
The integration response ID.

IntegrationResponseKey (string) --
The integration response key.

ResponseParameters (dict) --
A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where name is a valid and unique response header name and JSON-expression is a valid JSON expression without the $ prefix.

(string) --

(string) --
A string with a length between [1-512].





ResponseTemplates (dict) --
The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

(string) --

(string) --
A string with a length between [0-32768].





TemplateSelectionExpression (string) --
The template selection expressions for the integration response.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
        'IntegrationResponseId': 'string',
        'IntegrationResponseKey': 'string',
        'ResponseParameters': {
            'string': 'string'
        },
        'ResponseTemplates': {
            'string': 'string'
        },
        'TemplateSelectionExpression': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def update_model(ApiId=None, ContentType=None, Description=None, ModelId=None, Name=None, Schema=None):
    """
    Updates a Model.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_model(
        ApiId='string',
        ContentType='string',
        Description='string',
        ModelId='string',
        Name='string',
        Schema='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ContentType: string
    :param ContentType: The content-type for the model, for example, 'application/json'.

    :type Description: string
    :param Description: The description of the model.

    :type ModelId: string
    :param ModelId: [REQUIRED]\nThe model ID.\n

    :type Name: string
    :param Name: The name of the model.

    :type Schema: string
    :param Schema: The schema for the model. For application/json models, this should be JSON schema draft 4 model.

    :rtype: dict

ReturnsResponse Syntax
{
    'ContentType': 'string',
    'Description': 'string',
    'ModelId': 'string',
    'Name': 'string',
    'Schema': 'string'
}


Response Structure

(dict) --
Success

ContentType (string) --
The content-type for the model, for example, "application/json".

Description (string) --
The description of the model.

ModelId (string) --
The model identifier.

Name (string) --
The name of the model. Must be alphanumeric.

Schema (string) --
The schema for the model. For application/json models, this should be JSON schema draft 4 model.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ContentType': 'string',
        'Description': 'string',
        'ModelId': 'string',
        'Name': 'string',
        'Schema': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def update_route(ApiId=None, ApiKeyRequired=None, AuthorizationScopes=None, AuthorizationType=None, AuthorizerId=None, ModelSelectionExpression=None, OperationName=None, RequestModels=None, RequestParameters=None, RouteId=None, RouteKey=None, RouteResponseSelectionExpression=None, Target=None):
    """
    Updates a Route.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_route(
        ApiId='string',
        ApiKeyRequired=True|False,
        AuthorizationScopes=[
            'string',
        ],
        AuthorizationType='NONE'|'AWS_IAM'|'CUSTOM'|'JWT',
        AuthorizerId='string',
        ModelSelectionExpression='string',
        OperationName='string',
        RequestModels={
            'string': 'string'
        },
        RequestParameters={
            'string': {
                'Required': True|False
            }
        },
        RouteId='string',
        RouteKey='string',
        RouteResponseSelectionExpression='string',
        Target='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ApiKeyRequired: boolean
    :param ApiKeyRequired: Specifies whether an API key is required for the route. Supported only for WebSocket APIs.

    :type AuthorizationScopes: list
    :param AuthorizationScopes: The authorization scopes supported by this route.\n\n(string) --A string with a length between [1-64].\n\n\n

    :type AuthorizationType: string
    :param AuthorizationType: The authorization type for the route. For WebSocket APIs, valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer For HTTP APIs, valid values are NONE for open access, or JWT for using JSON Web Tokens.

    :type AuthorizerId: string
    :param AuthorizerId: The identifier of the Authorizer resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.

    :type ModelSelectionExpression: string
    :param ModelSelectionExpression: The model selection expression for the route. Supported only for WebSocket APIs.

    :type OperationName: string
    :param OperationName: The operation name for the route.

    :type RequestModels: dict
    :param RequestModels: The request models for the route. Supported only for WebSocket APIs.\n\n(string) --\n(string) --A string with a length between [1-128].\n\n\n\n\n

    :type RequestParameters: dict
    :param RequestParameters: The request parameters for the route. Supported only for WebSocket APIs.\n\n(string) --\n(dict) --Validation constraints imposed on parameters of a request (path, query string, headers).\n\nRequired (boolean) --Whether or not the parameter is required.\n\n\n\n\n\n\n

    :type RouteId: string
    :param RouteId: [REQUIRED]\nThe route ID.\n

    :type RouteKey: string
    :param RouteKey: The route key for the route.

    :type RouteResponseSelectionExpression: string
    :param RouteResponseSelectionExpression: The route response selection expression for the route. Supported only for WebSocket APIs.

    :type Target: string
    :param Target: The target for the route.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApiGatewayManaged': True|False,
    'ApiKeyRequired': True|False,
    'AuthorizationScopes': [
        'string',
    ],
    'AuthorizationType': 'NONE'|'AWS_IAM'|'CUSTOM'|'JWT',
    'AuthorizerId': 'string',
    'ModelSelectionExpression': 'string',
    'OperationName': 'string',
    'RequestModels': {
        'string': 'string'
    },
    'RequestParameters': {
        'string': {
            'Required': True|False
        }
    },
    'RouteId': 'string',
    'RouteKey': 'string',
    'RouteResponseSelectionExpression': 'string',
    'Target': 'string'
}


Response Structure

(dict) --
Success

ApiGatewayManaged (boolean) --
Specifies whether a route is managed by API Gateway. If you created an API using quick create, the $default route is managed by API Gateway. You can\'t modify the $default route key.

ApiKeyRequired (boolean) --
Specifies whether an API key is required for this route. Supported only for WebSocket APIs.

AuthorizationScopes (list) --
A list of authorization scopes configured on a route. The scopes are used with a JWT authorizer to authorize the method invocation. The authorization works by matching the route scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any route scope matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the route scope is configured, the client must provide an access token instead of an identity token for authorization purposes.

(string) --
A string with a length between [1-64].



AuthorizationType (string) --
The authorization type for the route. For WebSocket APIs, valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer For HTTP APIs, valid values are NONE for open access, or JWT for using JSON Web Tokens.

AuthorizerId (string) --
The identifier of the Authorizer resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.

ModelSelectionExpression (string) --
The model selection expression for the route. Supported only for WebSocket APIs.

OperationName (string) --
The operation name for the route.

RequestModels (dict) --
The request models for the route. Supported only for WebSocket APIs.

(string) --

(string) --
A string with a length between [1-128].





RequestParameters (dict) --
The request parameters for the route. Supported only for WebSocket APIs.

(string) --

(dict) --
Validation constraints imposed on parameters of a request (path, query string, headers).

Required (boolean) --
Whether or not the parameter is required.







RouteId (string) --
The route ID.

RouteKey (string) --
The route key for the route.

RouteResponseSelectionExpression (string) --
The route response selection expression for the route. Supported only for WebSocket APIs.

Target (string) --
The target for the route.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ApiGatewayManaged': True|False,
        'ApiKeyRequired': True|False,
        'AuthorizationScopes': [
            'string',
        ],
        'AuthorizationType': 'NONE'|'AWS_IAM'|'CUSTOM'|'JWT',
        'AuthorizerId': 'string',
        'ModelSelectionExpression': 'string',
        'OperationName': 'string',
        'RequestModels': {
            'string': 'string'
        },
        'RequestParameters': {
            'string': {
                'Required': True|False
            }
        },
        'RouteId': 'string',
        'RouteKey': 'string',
        'RouteResponseSelectionExpression': 'string',
        'Target': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def update_route_response(ApiId=None, ModelSelectionExpression=None, ResponseModels=None, ResponseParameters=None, RouteId=None, RouteResponseId=None, RouteResponseKey=None):
    """
    Updates a RouteResponse.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_route_response(
        ApiId='string',
        ModelSelectionExpression='string',
        ResponseModels={
            'string': 'string'
        },
        ResponseParameters={
            'string': {
                'Required': True|False
            }
        },
        RouteId='string',
        RouteResponseId='string',
        RouteResponseKey='string'
    )
    
    
    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type ModelSelectionExpression: string
    :param ModelSelectionExpression: The model selection expression for the route response. Supported only for WebSocket APIs.

    :type ResponseModels: dict
    :param ResponseModels: The response models for the route response.\n\n(string) --\n(string) --A string with a length between [1-128].\n\n\n\n\n

    :type ResponseParameters: dict
    :param ResponseParameters: The route response parameters.\n\n(string) --\n(dict) --Validation constraints imposed on parameters of a request (path, query string, headers).\n\nRequired (boolean) --Whether or not the parameter is required.\n\n\n\n\n\n\n

    :type RouteId: string
    :param RouteId: [REQUIRED]\nThe route ID.\n

    :type RouteResponseId: string
    :param RouteResponseId: [REQUIRED]\nThe route response ID.\n

    :type RouteResponseKey: string
    :param RouteResponseKey: The route response key.

    :rtype: dict

ReturnsResponse Syntax
{
    'ModelSelectionExpression': 'string',
    'ResponseModels': {
        'string': 'string'
    },
    'ResponseParameters': {
        'string': {
            'Required': True|False
        }
    },
    'RouteResponseId': 'string',
    'RouteResponseKey': 'string'
}


Response Structure

(dict) --
Success

ModelSelectionExpression (string) --
Represents the model selection expression of a route response. Supported only for WebSocket APIs.

ResponseModels (dict) --
Represents the response models of a route response.

(string) --

(string) --
A string with a length between [1-128].





ResponseParameters (dict) --
Represents the response parameters of a route response.

(string) --

(dict) --
Validation constraints imposed on parameters of a request (path, query string, headers).

Required (boolean) --
Whether or not the parameter is required.







RouteResponseId (string) --
Represents the identifier of a route response.

RouteResponseKey (string) --
Represents the route response key of a route response.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'ModelSelectionExpression': 'string',
        'ResponseModels': {
            'string': 'string'
        },
        'ResponseParameters': {
            'string': {
                'Required': True|False
            }
        },
        'RouteResponseId': 'string',
        'RouteResponseKey': 'string'
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def update_stage(AccessLogSettings=None, ApiId=None, AutoDeploy=None, ClientCertificateId=None, DefaultRouteSettings=None, DeploymentId=None, Description=None, RouteSettings=None, StageName=None, StageVariables=None):
    """
    Updates a Stage.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_stage(
        AccessLogSettings={
            'DestinationArn': 'string',
            'Format': 'string'
        },
        ApiId='string',
        AutoDeploy=True|False,
        ClientCertificateId='string',
        DefaultRouteSettings={
            'DataTraceEnabled': True|False,
            'DetailedMetricsEnabled': True|False,
            'LoggingLevel': 'ERROR'|'INFO'|'OFF',
            'ThrottlingBurstLimit': 123,
            'ThrottlingRateLimit': 123.0
        },
        DeploymentId='string',
        Description='string',
        RouteSettings={
            'string': {
                'DataTraceEnabled': True|False,
                'DetailedMetricsEnabled': True|False,
                'LoggingLevel': 'ERROR'|'INFO'|'OFF',
                'ThrottlingBurstLimit': 123,
                'ThrottlingRateLimit': 123.0
            }
        },
        StageName='string',
        StageVariables={
            'string': 'string'
        }
    )
    
    
    :type AccessLogSettings: dict
    :param AccessLogSettings: Settings for logging access in this stage.\n\nDestinationArn (string) --The ARN of the CloudWatch Logs log group to receive access logs.\n\nFormat (string) --A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.\n\n\n

    :type ApiId: string
    :param ApiId: [REQUIRED]\nThe API identifier.\n

    :type AutoDeploy: boolean
    :param AutoDeploy: Specifies whether updates to an API automatically trigger a new deployment. The default value is false.

    :type ClientCertificateId: string
    :param ClientCertificateId: The identifier of a client certificate for a Stage.

    :type DefaultRouteSettings: dict
    :param DefaultRouteSettings: The default route settings for the stage.\n\nDataTraceEnabled (boolean) --Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.\n\nDetailedMetricsEnabled (boolean) --Specifies whether detailed metrics are enabled.\n\nLoggingLevel (string) --Specifies the logging level for this route: INFO, ERROR, or OFF. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.\n\nThrottlingBurstLimit (integer) --Specifies the throttling burst limit.\n\nThrottlingRateLimit (float) --Specifies the throttling rate limit.\n\n\n

    :type DeploymentId: string
    :param DeploymentId: The deployment identifier for the API stage. Can\'t be updated if autoDeploy is enabled.

    :type Description: string
    :param Description: The description for the API stage.

    :type RouteSettings: dict
    :param RouteSettings: Route settings for the stage.\n\n(string) --\n(dict) --Represents a collection of route settings.\n\nDataTraceEnabled (boolean) --Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.\n\nDetailedMetricsEnabled (boolean) --Specifies whether detailed metrics are enabled.\n\nLoggingLevel (string) --Specifies the logging level for this route: INFO, ERROR, or OFF. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.\n\nThrottlingBurstLimit (integer) --Specifies the throttling burst limit.\n\nThrottlingRateLimit (float) --Specifies the throttling rate limit.\n\n\n\n\n\n\n

    :type StageName: string
    :param StageName: [REQUIRED]\nThe stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.\n

    :type StageVariables: dict
    :param StageVariables: A map that defines the stage variables for a Stage. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.\n\n(string) --\n(string) --A string with a length between [0-2048].\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AccessLogSettings': {
        'DestinationArn': 'string',
        'Format': 'string'
    },
    'ApiGatewayManaged': True|False,
    'AutoDeploy': True|False,
    'ClientCertificateId': 'string',
    'CreatedDate': datetime(2015, 1, 1),
    'DefaultRouteSettings': {
        'DataTraceEnabled': True|False,
        'DetailedMetricsEnabled': True|False,
        'LoggingLevel': 'ERROR'|'INFO'|'OFF',
        'ThrottlingBurstLimit': 123,
        'ThrottlingRateLimit': 123.0
    },
    'DeploymentId': 'string',
    'Description': 'string',
    'LastDeploymentStatusMessage': 'string',
    'LastUpdatedDate': datetime(2015, 1, 1),
    'RouteSettings': {
        'string': {
            'DataTraceEnabled': True|False,
            'DetailedMetricsEnabled': True|False,
            'LoggingLevel': 'ERROR'|'INFO'|'OFF',
            'ThrottlingBurstLimit': 123,
            'ThrottlingRateLimit': 123.0
        }
    },
    'StageName': 'string',
    'StageVariables': {
        'string': 'string'
    },
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Success

AccessLogSettings (dict) --
Settings for logging access in this stage.

DestinationArn (string) --
The ARN of the CloudWatch Logs log group to receive access logs.

Format (string) --
A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.



ApiGatewayManaged (boolean) --
Specifies whether a stage is managed by API Gateway. If you created an API using quick create, the $default stage is managed by API Gateway. You can\'t modify the $default stage.

AutoDeploy (boolean) --
Specifies whether updates to an API automatically trigger a new deployment. The default value is false.

ClientCertificateId (string) --
The identifier of a client certificate for a Stage. Supported only for WebSocket APIs.

CreatedDate (datetime) --
The timestamp when the stage was created.

DefaultRouteSettings (dict) --
Default route settings for the stage.

DataTraceEnabled (boolean) --
Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

DetailedMetricsEnabled (boolean) --
Specifies whether detailed metrics are enabled.

LoggingLevel (string) --
Specifies the logging level for this route: INFO, ERROR, or OFF. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

ThrottlingBurstLimit (integer) --
Specifies the throttling burst limit.

ThrottlingRateLimit (float) --
Specifies the throttling rate limit.



DeploymentId (string) --
The identifier of the Deployment that the Stage is associated with. Can\'t be updated if autoDeploy is enabled.

Description (string) --
The description of the stage.

LastDeploymentStatusMessage (string) --
Describes the status of the last deployment of a stage. Supported only for stages with autoDeploy enabled.

LastUpdatedDate (datetime) --
The timestamp when the stage was last updated.

RouteSettings (dict) --
Route settings for the stage, by routeKey.

(string) --

(dict) --
Represents a collection of route settings.

DataTraceEnabled (boolean) --
Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

DetailedMetricsEnabled (boolean) --
Specifies whether detailed metrics are enabled.

LoggingLevel (string) --
Specifies the logging level for this route: INFO, ERROR, or OFF. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

ThrottlingBurstLimit (integer) --
Specifies the throttling burst limit.

ThrottlingRateLimit (float) --
Specifies the throttling rate limit.







StageName (string) --
The name of the stage.

StageVariables (dict) --
A map that defines the stage variables for a stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.

(string) --

(string) --
A string with a length between [0-2048].





Tags (dict) --
The collection of tags. Each tag element is associated with a given resource.

(string) --

(string) --
A string with a length between [0-1600].











Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException
ApiGatewayV2.Client.exceptions.ConflictException


    :return: {
        'AccessLogSettings': {
            'DestinationArn': 'string',
            'Format': 'string'
        },
        'ApiGatewayManaged': True|False,
        'AutoDeploy': True|False,
        'ClientCertificateId': 'string',
        'CreatedDate': datetime(2015, 1, 1),
        'DefaultRouteSettings': {
            'DataTraceEnabled': True|False,
            'DetailedMetricsEnabled': True|False,
            'LoggingLevel': 'ERROR'|'INFO'|'OFF',
            'ThrottlingBurstLimit': 123,
            'ThrottlingRateLimit': 123.0
        },
        'DeploymentId': 'string',
        'Description': 'string',
        'LastDeploymentStatusMessage': 'string',
        'LastUpdatedDate': datetime(2015, 1, 1),
        'RouteSettings': {
            'string': {
                'DataTraceEnabled': True|False,
                'DetailedMetricsEnabled': True|False,
                'LoggingLevel': 'ERROR'|'INFO'|'OFF',
                'ThrottlingBurstLimit': 123,
                'ThrottlingRateLimit': 123.0
            }
        },
        'StageName': 'string',
        'StageVariables': {
            'string': 'string'
        },
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    ApiGatewayV2.Client.exceptions.NotFoundException
    ApiGatewayV2.Client.exceptions.TooManyRequestsException
    ApiGatewayV2.Client.exceptions.BadRequestException
    ApiGatewayV2.Client.exceptions.ConflictException
    
    """
    pass

def update_vpc_link(Name=None, VpcLinkId=None):
    """
    Updates a VPC link.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_vpc_link(
        Name='string',
        VpcLinkId='string'
    )
    
    
    :type Name: string
    :param Name: The name of the VPC link.

    :type VpcLinkId: string
    :param VpcLinkId: [REQUIRED]\nThe ID of the VPC link.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CreatedDate': datetime(2015, 1, 1),
    'Name': 'string',
    'SecurityGroupIds': [
        'string',
    ],
    'SubnetIds': [
        'string',
    ],
    'Tags': {
        'string': 'string'
    },
    'VpcLinkId': 'string',
    'VpcLinkStatus': 'PENDING'|'AVAILABLE'|'DELETING'|'FAILED'|'INACTIVE',
    'VpcLinkStatusMessage': 'string',
    'VpcLinkVersion': 'V2'
}


Response Structure

(dict) --
200 response

CreatedDate (datetime) --
The timestamp when the VPC link was created.

Name (string) --
The name of the VPC link.

SecurityGroupIds (list) --
A list of security group IDs for the VPC link.

(string) --


SubnetIds (list) --
A list of subnet IDs to include in the VPC link.

(string) --


Tags (dict) --
Tags for the VPC link.

(string) --

(string) --
A string with a length between [0-1600].





VpcLinkId (string) --
The ID of the VPC link.

VpcLinkStatus (string) --
The status of the VPC link.

VpcLinkStatusMessage (string) --
A message summarizing the cause of the status of the VPC link.

VpcLinkVersion (string) --
The version of the VPC link.







Exceptions

ApiGatewayV2.Client.exceptions.NotFoundException
ApiGatewayV2.Client.exceptions.TooManyRequestsException
ApiGatewayV2.Client.exceptions.BadRequestException


    :return: {
        'CreatedDate': datetime(2015, 1, 1),
        'Name': 'string',
        'SecurityGroupIds': [
            'string',
        ],
        'SubnetIds': [
            'string',
        ],
        'Tags': {
            'string': 'string'
        },
        'VpcLinkId': 'string',
        'VpcLinkStatus': 'PENDING'|'AVAILABLE'|'DELETING'|'FAILED'|'INACTIVE',
        'VpcLinkStatusMessage': 'string',
        'VpcLinkVersion': 'V2'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

