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

def create_api_key(name=None, description=None, enabled=None, generateDistinctId=None, value=None, stageKeys=None, customerId=None):
    """
    Create an  ApiKey resource.
    See also: AWS API Documentation
    
    
    :example: response = client.create_api_key(
        name='string',
        description='string',
        enabled=True|False,
        generateDistinctId=True|False,
        value='string',
        stageKeys=[
            {
                'restApiId': 'string',
                'stageName': 'string'
            },
        ],
        customerId='string'
    )
    
    
    :type name: string
    :param name: The name of the ApiKey .

    :type description: string
    :param description: The description of the ApiKey .

    :type enabled: boolean
    :param enabled: Specifies whether the ApiKey can be used by callers.

    :type generateDistinctId: boolean
    :param generateDistinctId: Specifies whether (true ) or not (false ) the key identifier is distinct from the created API key value.

    :type value: string
    :param value: Specifies a value of the API key.

    :type stageKeys: list
    :param stageKeys: DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.
            (dict) --A reference to a unique stage identified in the format {restApiId}/{stage} .
            restApiId (string) --The string identifier of the associated RestApi .
            stageName (string) --The stage name associated with the stage key.
            
            

    :type customerId: string
    :param customerId: An AWS Marketplace customer identifier , when integrating with the AWS SaaS Marketplace.

    :rtype: dict
    :return: {
        'id': 'string',
        'value': 'string',
        'name': 'string',
        'customerId': 'string',
        'description': 'string',
        'enabled': True|False,
        'createdDate': datetime(2015, 1, 1),
        'lastUpdatedDate': datetime(2015, 1, 1),
        'stageKeys': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_authorizer(restApiId=None, name=None, type=None, providerARNs=None, authType=None, authorizerUri=None, authorizerCredentials=None, identitySource=None, identityValidationExpression=None, authorizerResultTtlInSeconds=None):
    """
    Adds a new  Authorizer resource to an existing  RestApi resource.
    See also: AWS API Documentation
    
    
    :example: response = client.create_authorizer(
        restApiId='string',
        name='string',
        type='TOKEN'|'REQUEST'|'COGNITO_USER_POOLS',
        providerARNs=[
            'string',
        ],
        authType='string',
        authorizerUri='string',
        authorizerCredentials='string',
        identitySource='string',
        identityValidationExpression='string',
        authorizerResultTtlInSeconds=123
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type name: string
    :param name: [REQUIRED]
            [Required] The name of the authorizer.
            

    :type type: string
    :param type: [REQUIRED]
            [Required] The authorizer type. Valid values are TOKEN for a Lambda function using a single authorization token submitted in a custom header, REQUEST for a Lambda function using incoming request parameters, and COGNITO_USER_POOLS for using an Amazon Cognito user pool.
            

    :type providerARNs: list
    :param providerARNs: A list of the Amazon Cognito user pool ARNs for the COGNITO_USER_POOLS authorizer. Each element is of this format: arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id} . For a TOKEN or REQUEST authorizer, this is not defined.
            (string) --
            

    :type authType: string
    :param authType: Optional customer-defined field, used in Swagger imports and exports without functional impact.

    :type authorizerUri: string
    :param authorizerUri: Specifies the authorizer's Uniform Resource Identifier (URI). For TOKEN or REQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations . In general, the URI has this form arn:aws:apigateway:{region}:lambda:path/{service_api} , where {region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial / . For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations .

    :type authorizerCredentials: string
    :param authorizerCredentials: Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.

    :type identitySource: string
    :param identitySource: The identity source for which authorization is requested.
            For a TOKEN or COGNITO_USER_POOLS authorizer, this is required and specifies the request header mapping expression for the custom header holding the authorization token submitted by the client. For example, if the token header name is Auth , the header mapping expression is method.request.header.Auth .
            For the REQUEST authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an Auth header, a Name query string parameter are defined as identity sources, this value is method.request.header.Auth, method.request.querystring.Name . These parameters will be used to derive the authorization caching key and to perform runtime validation of the REQUEST authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.
            

    :type identityValidationExpression: string
    :param identityValidationExpression: A validation expression for the incoming identity token. For TOKEN authorizers, this value is a regular expression. API Gateway will match the aud field of the incoming token from the client against the specified regular expression. It will invoke the authorizer's Lambda function when there is a match. Otherwise, it will return a 401 Unauthorized response without calling the Lambda function. The validation expression does not apply to the REQUEST authorizer.

    :type authorizerResultTtlInSeconds: integer
    :param authorizerResultTtlInSeconds: The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'type': 'TOKEN'|'REQUEST'|'COGNITO_USER_POOLS',
        'providerARNs': [
            'string',
        ],
        'authType': 'string',
        'authorizerUri': 'string',
        'authorizerCredentials': 'string',
        'identitySource': 'string',
        'identityValidationExpression': 'string',
        'authorizerResultTtlInSeconds': 123
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_base_path_mapping(domainName=None, basePath=None, restApiId=None, stage=None):
    """
    Creates a new  BasePathMapping resource.
    See also: AWS API Documentation
    
    
    :example: response = client.create_base_path_mapping(
        domainName='string',
        basePath='string',
        restApiId='string',
        stage='string'
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            [Required] The domain name of the BasePathMapping resource to create.
            

    :type basePath: string
    :param basePath: The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Leave this blank if you do not want callers to specify a base path name after the domain name.

    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type stage: string
    :param stage: The name of the API's stage that you want to use for this mapping. Leave this blank if you do not want callers to explicitly specify the stage name after any base path name.

    :rtype: dict
    :return: {
        'basePath': 'string',
        'restApiId': 'string',
        'stage': 'string'
    }
    
    
    """
    pass

def create_deployment(restApiId=None, stageName=None, stageDescription=None, description=None, cacheClusterEnabled=None, cacheClusterSize=None, variables=None, canarySettings=None):
    """
    Creates a  Deployment resource, which makes a specified  RestApi callable over the internet.
    See also: AWS API Documentation
    
    
    :example: response = client.create_deployment(
        restApiId='string',
        stageName='string',
        stageDescription='string',
        description='string',
        cacheClusterEnabled=True|False,
        cacheClusterSize='0.5'|'1.6'|'6.1'|'13.5'|'28.4'|'58.2'|'118'|'237',
        variables={
            'string': 'string'
        },
        canarySettings={
            'percentTraffic': 123.0,
            'stageVariableOverrides': {
                'string': 'string'
            },
            'useStageCache': True|False
        }
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type stageName: string
    :param stageName: The name of the Stage resource for the Deployment resource to create.

    :type stageDescription: string
    :param stageDescription: The description of the Stage resource for the Deployment resource to create.

    :type description: string
    :param description: The description for the Deployment resource to create.

    :type cacheClusterEnabled: boolean
    :param cacheClusterEnabled: Enables a cache cluster for the Stage resource specified in the input.

    :type cacheClusterSize: string
    :param cacheClusterSize: Specifies the cache cluster size for the Stage resource specified in the input, if a cache cluster is enabled.

    :type variables: dict
    :param variables: A map that defines the stage variables for the Stage resource that is associated with the new deployment. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#=,]+ .
            (string) --
            (string) --
            

    :type canarySettings: dict
    :param canarySettings: The input configuration for the canary deployment when the deployment is a canary release deployment.
            percentTraffic (float) --The percentage (0.0-100.0) of traffic routed to the canary deployment.
            stageVariableOverrides (dict) --A stage variable overrides used for the canary release deployment. They can override existing stage variables or add new stage variables for the canary release deployment. These stage variables are represented as a string-to-string map between stage variable names and their values.
            (string) --
            (string) --
            
            useStageCache (boolean) --A Boolean flag to indicate whether the canary release deployment uses the stage cache or not.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'description': 'string',
        'createdDate': datetime(2015, 1, 1),
        'apiSummary': {
            'string': {
                'string': {
                    'authorizationType': 'string',
                    'apiKeyRequired': True|False
                }
            }
        }
    }
    
    
    """
    pass

def create_documentation_part(restApiId=None, location=None, properties=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.create_documentation_part(
        restApiId='string',
        location={
            'type': 'API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'|'PATH_PARAMETER'|'QUERY_PARAMETER'|'REQUEST_HEADER'|'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'|'RESPONSE_BODY',
            'path': 'string',
            'method': 'string',
            'statusCode': 'string',
            'name': 'string'
        },
        properties='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type location: dict
    :param location: [REQUIRED]
            [Required] The location of the targeted API entity of the to-be-created documentation part.
            type (string) -- [REQUIRED][Required] The type of API entity to which the documentation content applies. Valid values are API , AUTHORIZER , MODEL , RESOURCE , METHOD , PATH_PARAMETER , QUERY_PARAMETER , REQUEST_HEADER , REQUEST_BODY , RESPONSE , RESPONSE_HEADER , and RESPONSE_BODY . Content inheritance does not apply to any entity of the API , AUTHORIZER , METHOD , MODEL , REQUEST_BODY , or RESOURCE type.
            path (string) --The URL path of the target. It is a valid field for the API entity types of RESOURCE , METHOD , PATH_PARAMETER , QUERY_PARAMETER , REQUEST_HEADER , REQUEST_BODY , RESPONSE , RESPONSE_HEADER , and RESPONSE_BODY . The default value is / for the root resource. When an applicable child entity inherits the content of another entity of the same type with more general specifications of the other location attributes, the child entity's path attribute must match that of the parent entity as a prefix.
            method (string) --The HTTP verb of a method. It is a valid field for the API entity types of METHOD , PATH_PARAMETER , QUERY_PARAMETER , REQUEST_HEADER , REQUEST_BODY , RESPONSE , RESPONSE_HEADER , and RESPONSE_BODY . The default value is * for any method. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other location attributes, the child entity's method attribute must match that of the parent entity exactly.
            statusCode (string) --The HTTP status code of a response. It is a valid field for the API entity types of RESPONSE , RESPONSE_HEADER , and RESPONSE_BODY . The default value is * for any status code. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other location attributes, the child entity's statusCode attribute must match that of the parent entity exactly.
            name (string) --The name of the targeted API entity. It is a valid and required field for the API entity types of AUTHORIZER , MODEL , PATH_PARAMETER , QUERY_PARAMETER , REQUEST_HEADER , REQUEST_BODY and RESPONSE_HEADER . It is an invalid field for any other entity type.
            

    :type properties: string
    :param properties: [REQUIRED]
            [Required] The new documentation content map of the targeted API entity. Enclosed key-value pairs are API-specific, but only Swagger-compliant key-value pairs can be exported and, hence, published.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'location': {
            'type': 'API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'|'PATH_PARAMETER'|'QUERY_PARAMETER'|'REQUEST_HEADER'|'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'|'RESPONSE_BODY',
            'path': 'string',
            'method': 'string',
            'statusCode': 'string',
            'name': 'string'
        },
        'properties': 'string'
    }
    
    
    """
    pass

def create_documentation_version(restApiId=None, documentationVersion=None, stageName=None, description=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.create_documentation_version(
        restApiId='string',
        documentationVersion='string',
        stageName='string',
        description='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type documentationVersion: string
    :param documentationVersion: [REQUIRED]
            [Required] The version identifier of the new snapshot.
            

    :type stageName: string
    :param stageName: The stage name to be associated with the new documentation snapshot.

    :type description: string
    :param description: A description about the new documentation snapshot.

    :rtype: dict
    :return: {
        'version': 'string',
        'createdDate': datetime(2015, 1, 1),
        'description': 'string'
    }
    
    
    """
    pass

def create_domain_name(domainName=None, certificateName=None, certificateBody=None, certificatePrivateKey=None, certificateChain=None, certificateArn=None, regionalCertificateName=None, regionalCertificateArn=None, endpointConfiguration=None):
    """
    Creates a new domain name.
    See also: AWS API Documentation
    
    
    :example: response = client.create_domain_name(
        domainName='string',
        certificateName='string',
        certificateBody='string',
        certificatePrivateKey='string',
        certificateChain='string',
        certificateArn='string',
        regionalCertificateName='string',
        regionalCertificateArn='string',
        endpointConfiguration={
            'types': [
                'REGIONAL'|'EDGE',
            ]
        }
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            [Required] The name of the DomainName resource.
            

    :type certificateName: string
    :param certificateName: The user-friendly name of the certificate that will be used by edge-optimized endpoint for this domain name.

    :type certificateBody: string
    :param certificateBody: [Deprecated] The body of the server certificate that will be used by edge-optimized endpoint for this domain name provided by your certificate authority.

    :type certificatePrivateKey: string
    :param certificatePrivateKey: [Deprecated] Your edge-optimized endpoint's domain name certificate's private key.

    :type certificateChain: string
    :param certificateChain: [Deprecated] The intermediate certificates and optionally the root certificate, one after the other without any blank lines, used by an edge-optimized endpoint for this domain name. If you include the root certificate, your certificate chain must start with intermediate certificates and end with the root certificate. Use the intermediate certificates that were provided by your certificate authority. Do not include any intermediaries that are not in the chain of trust path.

    :type certificateArn: string
    :param certificateArn: The reference to an AWS-managed certificate that will be used by edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.

    :type regionalCertificateName: string
    :param regionalCertificateName: The user-friendly name of the certificate that will be used by regional endpoint for this domain name.

    :type regionalCertificateArn: string
    :param regionalCertificateArn: The reference to an AWS-managed certificate that will be used by regional endpoint for this domain name. AWS Certificate Manager is the only supported source.

    :type endpointConfiguration: dict
    :param endpointConfiguration: The endpoint configuration of this DomainName showing the endpoint types of the domain name.
            types (list) --A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is 'EDGE' . For a regional API and its custom domain name, the endpoint type is REGIONAL .
            (string) --The endpoint type. The valid value is EDGE for edge-optimized API setup, most suitable for mobile applications, REGIONAL for regional API endpoint setup, most suitable for calling from AWS Region
            
            

    :rtype: dict
    :return: {
        'domainName': 'string',
        'certificateName': 'string',
        'certificateArn': 'string',
        'certificateUploadDate': datetime(2015, 1, 1),
        'regionalDomainName': 'string',
        'regionalHostedZoneId': 'string',
        'regionalCertificateName': 'string',
        'regionalCertificateArn': 'string',
        'distributionDomainName': 'string',
        'distributionHostedZoneId': 'string',
        'endpointConfiguration': {
            'types': [
                'REGIONAL'|'EDGE',
            ]
        }
    }
    
    
    """
    pass

def create_model(restApiId=None, name=None, description=None, schema=None, contentType=None):
    """
    Adds a new  Model resource to an existing  RestApi resource.
    See also: AWS API Documentation
    
    
    :example: response = client.create_model(
        restApiId='string',
        name='string',
        description='string',
        schema='string',
        contentType='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The RestApi identifier under which the Model will be created.
            

    :type name: string
    :param name: [REQUIRED]
            [Required] The name of the model. Must be alphanumeric.
            

    :type description: string
    :param description: The description of the model.

    :type schema: string
    :param schema: The schema for the model. For application/json models, this should be JSON schema draft 4 model.

    :type contentType: string
    :param contentType: [REQUIRED]
            [Required] The content-type for the model.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'description': 'string',
        'schema': 'string',
        'contentType': 'string'
    }
    
    
    """
    pass

def create_request_validator(restApiId=None, name=None, validateRequestBody=None, validateRequestParameters=None):
    """
    Creates a  ReqeustValidator of a given  RestApi .
    See also: AWS API Documentation
    
    
    :example: response = client.create_request_validator(
        restApiId='string',
        name='string',
        validateRequestBody=True|False,
        validateRequestParameters=True|False
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type name: string
    :param name: The name of the to-be-created RequestValidator .

    :type validateRequestBody: boolean
    :param validateRequestBody: A Boolean flag to indicate whether to validate request body according to the configured model schema for the method (true ) or not (false ).

    :type validateRequestParameters: boolean
    :param validateRequestParameters: A Boolean flag to indicate whether to validate request parameters, true , or not false .

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'validateRequestBody': True|False,
        'validateRequestParameters': True|False
    }
    
    
    """
    pass

def create_resource(restApiId=None, parentId=None, pathPart=None):
    """
    Creates a  Resource resource.
    See also: AWS API Documentation
    
    
    :example: response = client.create_resource(
        restApiId='string',
        parentId='string',
        pathPart='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type parentId: string
    :param parentId: [REQUIRED]
            [Required] The parent resource's identifier.
            

    :type pathPart: string
    :param pathPart: [REQUIRED]
            The last path segment for this resource.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'parentId': 'string',
        'pathPart': 'string',
        'path': 'string',
        'resourceMethods': {
            'string': {
                'httpMethod': 'string',
                'authorizationType': 'string',
                'authorizerId': 'string',
                'apiKeyRequired': True|False,
                'requestValidatorId': 'string',
                'operationName': 'string',
                'requestParameters': {
                    'string': True|False
                },
                'requestModels': {
                    'string': 'string'
                },
                'methodResponses': {
                    'string': {
                        'statusCode': 'string',
                        'responseParameters': {
                            'string': True|False
                        },
                        'responseModels': {
                            'string': 'string'
                        }
                    }
                },
                'methodIntegration': {
                    'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                    'httpMethod': 'string',
                    'uri': 'string',
                    'connectionType': 'INTERNET'|'VPC_LINK',
                    'connectionId': 'string',
                    'credentials': 'string',
                    'requestParameters': {
                        'string': 'string'
                    },
                    'requestTemplates': {
                        'string': 'string'
                    },
                    'passthroughBehavior': 'string',
                    'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                    'timeoutInMillis': 123,
                    'cacheNamespace': 'string',
                    'cacheKeyParameters': [
                        'string',
                    ],
                    'integrationResponses': {
                        'string': {
                            'statusCode': 'string',
                            'selectionPattern': 'string',
                            'responseParameters': {
                                'string': 'string'
                            },
                            'responseTemplates': {
                                'string': 'string'
                            },
                            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                        }
                    }
                },
                'authorizationScopes': [
                    'string',
                ]
            }
        }
    }
    
    
    :returns: 
    (string) --
    (boolean) --
    
    
    
    """
    pass

def create_rest_api(name=None, description=None, version=None, cloneFrom=None, binaryMediaTypes=None, minimumCompressionSize=None, apiKeySource=None, endpointConfiguration=None, policy=None):
    """
    Creates a new  RestApi resource.
    See also: AWS API Documentation
    
    
    :example: response = client.create_rest_api(
        name='string',
        description='string',
        version='string',
        cloneFrom='string',
        binaryMediaTypes=[
            'string',
        ],
        minimumCompressionSize=123,
        apiKeySource='HEADER'|'AUTHORIZER',
        endpointConfiguration={
            'types': [
                'REGIONAL'|'EDGE',
            ]
        },
        policy='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            [Required] The name of the RestApi .
            

    :type description: string
    :param description: The description of the RestApi .

    :type version: string
    :param version: A version identifier for the API.

    :type cloneFrom: string
    :param cloneFrom: The ID of the RestApi that you want to clone from.

    :type binaryMediaTypes: list
    :param binaryMediaTypes: The list of binary media types supported by the RestApi . By default, the RestApi supports only UTF-8-encoded text payloads.
            (string) --
            

    :type minimumCompressionSize: integer
    :param minimumCompressionSize: A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size.

    :type apiKeySource: string
    :param apiKeySource: The source of the API key for metering requests according to a usage plan. Valid values are:
            HEADER to read the API key from the X-API-Key header of a request.
            AUTHORIZER to read the API key from the UsageIdentifierKey from a custom authorizer.
            

    :type endpointConfiguration: dict
    :param endpointConfiguration: The endpoint configuration of this RestApi showing the endpoint types of the API.
            types (list) --A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For an edge-optimized API and its custom domain name, the endpoint type is 'EDGE' . For a regional API and its custom domain name, the endpoint type is REGIONAL .
            (string) --The endpoint type. The valid value is EDGE for edge-optimized API setup, most suitable for mobile applications, REGIONAL for regional API endpoint setup, most suitable for calling from AWS Region
            
            

    :type policy: string
    :param policy: A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration.

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'description': 'string',
        'createdDate': datetime(2015, 1, 1),
        'version': 'string',
        'warnings': [
            'string',
        ],
        'binaryMediaTypes': [
            'string',
        ],
        'minimumCompressionSize': 123,
        'apiKeySource': 'HEADER'|'AUTHORIZER',
        'endpointConfiguration': {
            'types': [
                'REGIONAL'|'EDGE',
            ]
        },
        'policy': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_stage(restApiId=None, stageName=None, deploymentId=None, description=None, cacheClusterEnabled=None, cacheClusterSize=None, variables=None, documentationVersion=None, canarySettings=None, tags=None):
    """
    Creates a new  Stage resource that references a pre-existing  Deployment for the API.
    See also: AWS API Documentation
    
    
    :example: response = client.create_stage(
        restApiId='string',
        stageName='string',
        deploymentId='string',
        description='string',
        cacheClusterEnabled=True|False,
        cacheClusterSize='0.5'|'1.6'|'6.1'|'13.5'|'28.4'|'58.2'|'118'|'237',
        variables={
            'string': 'string'
        },
        documentationVersion='string',
        canarySettings={
            'percentTraffic': 123.0,
            'deploymentId': 'string',
            'stageVariableOverrides': {
                'string': 'string'
            },
            'useStageCache': True|False
        },
        tags={
            'string': 'string'
        }
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type stageName: string
    :param stageName: [REQUIRED]
            [Required] The name for the Stage resource.
            

    :type deploymentId: string
    :param deploymentId: [REQUIRED]
            [Required] The identifier of the Deployment resource for the Stage resource.
            

    :type description: string
    :param description: The description of the Stage resource.

    :type cacheClusterEnabled: boolean
    :param cacheClusterEnabled: Whether cache clustering is enabled for the stage.

    :type cacheClusterSize: string
    :param cacheClusterSize: The stage's cache cluster size.

    :type variables: dict
    :param variables: A map that defines the stage variables for the new Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#=,]+ .
            (string) --
            (string) --
            

    :type documentationVersion: string
    :param documentationVersion: The version of the associated API documentation.

    :type canarySettings: dict
    :param canarySettings: The canary deployment settings of this stage.
            percentTraffic (float) --The percent (0-100) of traffic diverted to a canary deployment.
            deploymentId (string) --The ID of the canary deployment.
            stageVariableOverrides (dict) --Stage variables overridden for a canary release deployment, including new stage variables introduced in the canary. These stage variables are represented as a string-to-string map between stage variable names and their values.
            (string) --
            (string) --
            
            useStageCache (boolean) --A Boolean flag to indicate whether the canary deployment uses the stage cache or not.
            

    :type tags: dict
    :param tags: The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with aws: . The tag value can be up to 256 characters.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'deploymentId': 'string',
        'clientCertificateId': 'string',
        'stageName': 'string',
        'description': 'string',
        'cacheClusterEnabled': True|False,
        'cacheClusterSize': '0.5'|'1.6'|'6.1'|'13.5'|'28.4'|'58.2'|'118'|'237',
        'cacheClusterStatus': 'CREATE_IN_PROGRESS'|'AVAILABLE'|'DELETE_IN_PROGRESS'|'NOT_AVAILABLE'|'FLUSH_IN_PROGRESS',
        'methodSettings': {
            'string': {
                'metricsEnabled': True|False,
                'loggingLevel': 'string',
                'dataTraceEnabled': True|False,
                'throttlingBurstLimit': 123,
                'throttlingRateLimit': 123.0,
                'cachingEnabled': True|False,
                'cacheTtlInSeconds': 123,
                'cacheDataEncrypted': True|False,
                'requireAuthorizationForCacheControl': True|False,
                'unauthorizedCacheControlHeaderStrategy': 'FAIL_WITH_403'|'SUCCEED_WITH_RESPONSE_HEADER'|'SUCCEED_WITHOUT_RESPONSE_HEADER'
            }
        },
        'variables': {
            'string': 'string'
        },
        'documentationVersion': 'string',
        'accessLogSettings': {
            'format': 'string',
            'destinationArn': 'string'
        },
        'canarySettings': {
            'percentTraffic': 123.0,
            'deploymentId': 'string',
            'stageVariableOverrides': {
                'string': 'string'
            },
            'useStageCache': True|False
        },
        'tags': {
            'string': 'string'
        },
        'createdDate': datetime(2015, 1, 1),
        'lastUpdatedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_usage_plan(name=None, description=None, apiStages=None, throttle=None, quota=None):
    """
    Creates a usage plan with the throttle and quota limits, as well as the associated API stages, specified in the payload.
    See also: AWS API Documentation
    
    
    :example: response = client.create_usage_plan(
        name='string',
        description='string',
        apiStages=[
            {
                'apiId': 'string',
                'stage': 'string'
            },
        ],
        throttle={
            'burstLimit': 123,
            'rateLimit': 123.0
        },
        quota={
            'limit': 123,
            'offset': 123,
            'period': 'DAY'|'WEEK'|'MONTH'
        }
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            [Required] The name of the usage plan.
            

    :type description: string
    :param description: The description of the usage plan.

    :type apiStages: list
    :param apiStages: The associated API stages of the usage plan.
            (dict) --API stage name of the associated API stage in a usage plan.
            apiId (string) --API Id of the associated API stage in a usage plan.
            stage (string) --API stage name of the associated API stage in a usage plan.
            
            

    :type throttle: dict
    :param throttle: The throttling limits of the usage plan.
            burstLimit (integer) --The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
            rateLimit (float) --The API request steady-state rate limit.
            

    :type quota: dict
    :param quota: The quota of the usage plan.
            limit (integer) --The maximum number of requests that can be made in a given time period.
            offset (integer) --The number of requests subtracted from the given limit in the initial time period.
            period (string) --The time period in which the limit applies. Valid values are 'DAY', 'WEEK' or 'MONTH'.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'description': 'string',
        'apiStages': [
            {
                'apiId': 'string',
                'stage': 'string'
            },
        ],
        'throttle': {
            'burstLimit': 123,
            'rateLimit': 123.0
        },
        'quota': {
            'limit': 123,
            'offset': 123,
            'period': 'DAY'|'WEEK'|'MONTH'
        },
        'productCode': 'string'
    }
    
    
    """
    pass

def create_usage_plan_key(usagePlanId=None, keyId=None, keyType=None):
    """
    Creates a usage plan key for adding an existing API key to a usage plan.
    See also: AWS API Documentation
    
    
    :example: response = client.create_usage_plan_key(
        usagePlanId='string',
        keyId='string',
        keyType='string'
    )
    
    
    :type usagePlanId: string
    :param usagePlanId: [REQUIRED]
            [Required] The Id of the UsagePlan resource representing the usage plan containing the to-be-created UsagePlanKey resource representing a plan customer.
            

    :type keyId: string
    :param keyId: [REQUIRED]
            [Required] The identifier of a UsagePlanKey resource for a plan customer.
            

    :type keyType: string
    :param keyType: [REQUIRED]
            [Required] The type of a UsagePlanKey resource for a plan customer.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'type': 'string',
        'value': 'string',
        'name': 'string'
    }
    
    
    """
    pass

def create_vpc_link(name=None, description=None, targetArns=None):
    """
    Creates a VPC link, under the caller's account in a selected region, in an asynchronous operation that typically takes 2-4 minutes to complete and become operational. The caller must have permissions to create and update VPC Endpoint services.
    See also: AWS API Documentation
    
    
    :example: response = client.create_vpc_link(
        name='string',
        description='string',
        targetArns=[
            'string',
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            [Required] The name used to label and identify the VPC link.
            

    :type description: string
    :param description: The description of the VPC link.

    :type targetArns: list
    :param targetArns: [REQUIRED]
            [Required] The ARNs of network load balancers of the VPC targeted by the VPC link. The network load balancers must be owned by the same AWS account of the API owner.
            (string) --
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'description': 'string',
        'targetArns': [
            'string',
        ],
        'status': 'AVAILABLE'|'PENDING'|'DELETING'|'FAILED',
        'statusMessage': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_api_key(apiKey=None):
    """
    Deletes the  ApiKey resource.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_api_key(
        apiKey='string'
    )
    
    
    :type apiKey: string
    :param apiKey: [REQUIRED]
            [Required] The identifier of the ApiKey resource to be deleted.
            

    """
    pass

def delete_authorizer(restApiId=None, authorizerId=None):
    """
    Deletes an existing  Authorizer resource.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_authorizer(
        restApiId='string',
        authorizerId='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type authorizerId: string
    :param authorizerId: [REQUIRED]
            [Required] The identifier of the Authorizer resource.
            

    """
    pass

def delete_base_path_mapping(domainName=None, basePath=None):
    """
    Deletes the  BasePathMapping resource.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_base_path_mapping(
        domainName='string',
        basePath='string'
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            [Required] The domain name of the BasePathMapping resource to delete.
            

    :type basePath: string
    :param basePath: [REQUIRED]
            [Required] The base path name of the BasePathMapping resource to delete.
            

    """
    pass

def delete_client_certificate(clientCertificateId=None):
    """
    Deletes the  ClientCertificate resource.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_client_certificate(
        clientCertificateId='string'
    )
    
    
    :type clientCertificateId: string
    :param clientCertificateId: [REQUIRED]
            [Required] The identifier of the ClientCertificate resource to be deleted.
            

    """
    pass

def delete_deployment(restApiId=None, deploymentId=None):
    """
    Deletes a  Deployment resource. Deleting a deployment will only succeed if there are no  Stage resources associated with it.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_deployment(
        restApiId='string',
        deploymentId='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type deploymentId: string
    :param deploymentId: [REQUIRED]
            [Required] The identifier of the Deployment resource to delete.
            

    """
    pass

def delete_documentation_part(restApiId=None, documentationPartId=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.delete_documentation_part(
        restApiId='string',
        documentationPartId='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type documentationPartId: string
    :param documentationPartId: [REQUIRED]
            [Required] The identifier of the to-be-deleted documentation part.
            

    """
    pass

def delete_documentation_version(restApiId=None, documentationVersion=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.delete_documentation_version(
        restApiId='string',
        documentationVersion='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type documentationVersion: string
    :param documentationVersion: [REQUIRED]
            [Required] The version identifier of a to-be-deleted documentation snapshot.
            

    """
    pass

def delete_domain_name(domainName=None):
    """
    Deletes the  DomainName resource.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_domain_name(
        domainName='string'
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            [Required] The name of the DomainName resource to be deleted.
            

    """
    pass

def delete_gateway_response(restApiId=None, responseType=None):
    """
    Clears any customization of a  GatewayResponse of a specified response type on the given  RestApi and resets it with the default settings.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_gateway_response(
        restApiId='string',
        responseType='DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type responseType: string
    :param responseType: [REQUIRED]
            [Required]
            The response type of the associated GatewayResponse . Valid values are
            ACCESS_DENIED
            API_CONFIGURATION_ERROR
            AUTHORIZER_FAILURE
            AUTHORIZER_CONFIGURATION_ERROR
            BAD_REQUEST_PARAMETERS
            BAD_REQUEST_BODY
            DEFAULT_4XX
            DEFAULT_5XX
            EXPIRED_TOKEN
            INVALID_SIGNATURE
            INTEGRATION_FAILURE
            INTEGRATION_TIMEOUT
            INVALID_API_KEY
            MISSING_AUTHENTICATION_TOKEN
            QUOTA_EXCEEDED
            REQUEST_TOO_LARGE
            RESOURCE_NOT_FOUND
            THROTTLED
            UNAUTHORIZED
            UNSUPPORTED_MEDIA_TYPE
            

    """
    pass

def delete_integration(restApiId=None, resourceId=None, httpMethod=None):
    """
    Represents a delete integration.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_integration(
        restApiId='string',
        resourceId='string',
        httpMethod='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] Specifies a delete integration request's resource identifier.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] Specifies a delete integration request's HTTP method.
            

    """
    pass

def delete_integration_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None):
    """
    Represents a delete integration response.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_integration_response(
        restApiId='string',
        resourceId='string',
        httpMethod='string',
        statusCode='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] Specifies a delete integration response request's resource identifier.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] Specifies a delete integration response request's HTTP method.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            [Required] Specifies a delete integration response request's status code.
            

    """
    pass

def delete_method(restApiId=None, resourceId=None, httpMethod=None):
    """
    Deletes an existing  Method resource.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_method(
        restApiId='string',
        resourceId='string',
        httpMethod='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] The Resource identifier for the Method resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] The HTTP verb of the Method resource.
            

    """
    pass

def delete_method_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None):
    """
    Deletes an existing  MethodResponse resource.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_method_response(
        restApiId='string',
        resourceId='string',
        httpMethod='string',
        statusCode='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] The Resource identifier for the MethodResponse resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] The HTTP verb of the Method resource.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            [Required] The status code identifier for the MethodResponse resource.
            

    """
    pass

def delete_model(restApiId=None, modelName=None):
    """
    Deletes a model.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_model(
        restApiId='string',
        modelName='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type modelName: string
    :param modelName: [REQUIRED]
            [Required] The name of the model to delete.
            

    """
    pass

def delete_request_validator(restApiId=None, requestValidatorId=None):
    """
    Deletes a  RequestValidator of a given  RestApi .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_request_validator(
        restApiId='string',
        requestValidatorId='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type requestValidatorId: string
    :param requestValidatorId: [REQUIRED]
            [Required] The identifier of the RequestValidator to be deleted.
            

    """
    pass

def delete_resource(restApiId=None, resourceId=None):
    """
    Deletes a  Resource resource.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_resource(
        restApiId='string',
        resourceId='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] The identifier of the Resource resource.
            

    """
    pass

def delete_rest_api(restApiId=None):
    """
    Deletes the specified API.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_rest_api(
        restApiId='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    """
    pass

def delete_stage(restApiId=None, stageName=None):
    """
    Deletes a  Stage resource.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_stage(
        restApiId='string',
        stageName='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type stageName: string
    :param stageName: [REQUIRED]
            [Required] The name of the Stage resource to delete.
            

    """
    pass

def delete_usage_plan(usagePlanId=None):
    """
    Deletes a usage plan of a given plan Id.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_usage_plan(
        usagePlanId='string'
    )
    
    
    :type usagePlanId: string
    :param usagePlanId: [REQUIRED]
            [Required] The Id of the to-be-deleted usage plan.
            

    """
    pass

def delete_usage_plan_key(usagePlanId=None, keyId=None):
    """
    Deletes a usage plan key and remove the underlying API key from the associated usage plan.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_usage_plan_key(
        usagePlanId='string',
        keyId='string'
    )
    
    
    :type usagePlanId: string
    :param usagePlanId: [REQUIRED]
            [Required] The Id of the UsagePlan resource representing the usage plan containing the to-be-deleted UsagePlanKey resource representing a plan customer.
            

    :type keyId: string
    :param keyId: [REQUIRED]
            [Required] The Id of the UsagePlanKey resource to be deleted.
            

    """
    pass

def delete_vpc_link(vpcLinkId=None):
    """
    Deletes an existing  VpcLink of a specified identifier.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_vpc_link(
        vpcLinkId='string'
    )
    
    
    :type vpcLinkId: string
    :param vpcLinkId: [REQUIRED]
            [Required] The identifier of the VpcLink . It is used in an Integration to reference this VpcLink .
            

    """
    pass

def flush_stage_authorizers_cache(restApiId=None, stageName=None):
    """
    Flushes all authorizer cache entries on a stage.
    See also: AWS API Documentation
    
    
    :example: response = client.flush_stage_authorizers_cache(
        restApiId='string',
        stageName='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            The string identifier of the associated RestApi .
            

    :type stageName: string
    :param stageName: [REQUIRED]
            The name of the stage to flush.
            

    """
    pass

def flush_stage_cache(restApiId=None, stageName=None):
    """
    Flushes a stage's cache.
    See also: AWS API Documentation
    
    
    :example: response = client.flush_stage_cache(
        restApiId='string',
        stageName='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type stageName: string
    :param stageName: [REQUIRED]
            [Required] The name of the stage to flush its cache.
            

    """
    pass

def generate_client_certificate(description=None):
    """
    Generates a  ClientCertificate resource.
    See also: AWS API Documentation
    
    
    :example: response = client.generate_client_certificate(
        description='string'
    )
    
    
    :type description: string
    :param description: The description of the ClientCertificate .

    :rtype: dict
    :return: {
        'clientCertificateId': 'string',
        'description': 'string',
        'pemEncodedCertificate': 'string',
        'createdDate': datetime(2015, 1, 1),
        'expirationDate': datetime(2015, 1, 1)
    }
    
    
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

def get_account():
    """
    Gets information about the current  Account resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_account()
    
    
    :rtype: dict
    :return: {
        'cloudwatchRoleArn': 'string',
        'throttleSettings': {
            'burstLimit': 123,
            'rateLimit': 123.0
        },
        'features': [
            'string',
        ],
        'apiKeyVersion': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_api_key(apiKey=None, includeValue=None):
    """
    Gets information about the current  ApiKey resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_api_key(
        apiKey='string',
        includeValue=True|False
    )
    
    
    :type apiKey: string
    :param apiKey: [REQUIRED]
            [Required] The identifier of the ApiKey resource.
            

    :type includeValue: boolean
    :param includeValue: A boolean flag to specify whether (true ) or not (false ) the result contains the key value.

    :rtype: dict
    :return: {
        'id': 'string',
        'value': 'string',
        'name': 'string',
        'customerId': 'string',
        'description': 'string',
        'enabled': True|False,
        'createdDate': datetime(2015, 1, 1),
        'lastUpdatedDate': datetime(2015, 1, 1),
        'stageKeys': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_api_keys(position=None, limit=None, nameQuery=None, customerId=None, includeValues=None):
    """
    Gets information about the current  ApiKeys resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_api_keys(
        position='string',
        limit=123,
        nameQuery='string',
        customerId='string',
        includeValues=True|False
    )
    
    
    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :type nameQuery: string
    :param nameQuery: The name of queried API keys.

    :type customerId: string
    :param customerId: The identifier of a customer in AWS Marketplace or an external system, such as a developer portal.

    :type includeValues: boolean
    :param includeValues: A boolean flag to specify whether (true ) or not (false ) the result contains key values.

    :rtype: dict
    :return: {
        'warnings': [
            'string',
        ],
        'position': 'string',
        'items': [
            {
                'id': 'string',
                'value': 'string',
                'name': 'string',
                'customerId': 'string',
                'description': 'string',
                'enabled': True|False,
                'createdDate': datetime(2015, 1, 1),
                'lastUpdatedDate': datetime(2015, 1, 1),
                'stageKeys': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_authorizer(restApiId=None, authorizerId=None):
    """
    Describe an existing  Authorizer resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_authorizer(
        restApiId='string',
        authorizerId='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type authorizerId: string
    :param authorizerId: [REQUIRED]
            [Required] The identifier of the Authorizer resource.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'type': 'TOKEN'|'REQUEST'|'COGNITO_USER_POOLS',
        'providerARNs': [
            'string',
        ],
        'authType': 'string',
        'authorizerUri': 'string',
        'authorizerCredentials': 'string',
        'identitySource': 'string',
        'identityValidationExpression': 'string',
        'authorizerResultTtlInSeconds': 123
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_authorizers(restApiId=None, position=None, limit=None):
    """
    Describe an existing  Authorizers resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_authorizers(
        restApiId='string',
        position='string',
        limit=123
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'id': 'string',
                'name': 'string',
                'type': 'TOKEN'|'REQUEST'|'COGNITO_USER_POOLS',
                'providerARNs': [
                    'string',
                ],
                'authType': 'string',
                'authorizerUri': 'string',
                'authorizerCredentials': 'string',
                'identitySource': 'string',
                'identityValidationExpression': 'string',
                'authorizerResultTtlInSeconds': 123
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_base_path_mapping(domainName=None, basePath=None):
    """
    Describe a  BasePathMapping resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_base_path_mapping(
        domainName='string',
        basePath='string'
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            [Required] The domain name of the BasePathMapping resource to be described.
            

    :type basePath: string
    :param basePath: [REQUIRED]
            [Required] The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Leave this blank if you do not want callers to specify any base path name after the domain name.
            

    :rtype: dict
    :return: {
        'basePath': 'string',
        'restApiId': 'string',
        'stage': 'string'
    }
    
    
    """
    pass

def get_base_path_mappings(domainName=None, position=None, limit=None):
    """
    Represents a collection of  BasePathMapping resources.
    See also: AWS API Documentation
    
    
    :example: response = client.get_base_path_mappings(
        domainName='string',
        position='string',
        limit=123
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            [Required] The domain name of a BasePathMapping resource.
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'basePath': 'string',
                'restApiId': 'string',
                'stage': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_client_certificate(clientCertificateId=None):
    """
    Gets information about the current  ClientCertificate resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_client_certificate(
        clientCertificateId='string'
    )
    
    
    :type clientCertificateId: string
    :param clientCertificateId: [REQUIRED]
            [Required] The identifier of the ClientCertificate resource to be described.
            

    :rtype: dict
    :return: {
        'clientCertificateId': 'string',
        'description': 'string',
        'pemEncodedCertificate': 'string',
        'createdDate': datetime(2015, 1, 1),
        'expirationDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def get_client_certificates(position=None, limit=None):
    """
    Gets a collection of  ClientCertificate resources.
    See also: AWS API Documentation
    
    
    :example: response = client.get_client_certificates(
        position='string',
        limit=123
    )
    
    
    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'clientCertificateId': 'string',
                'description': 'string',
                'pemEncodedCertificate': 'string',
                'createdDate': datetime(2015, 1, 1),
                'expirationDate': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def get_deployment(restApiId=None, deploymentId=None, embed=None):
    """
    Gets information about a  Deployment resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_deployment(
        restApiId='string',
        deploymentId='string',
        embed=[
            'string',
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type deploymentId: string
    :param deploymentId: [REQUIRED]
            [Required] The identifier of the Deployment resource to get information about.
            

    :type embed: list
    :param embed: A query parameter to retrieve the specified embedded resources of the returned Deployment resource in the response. In a REST API call, this embed parameter value is a list of comma-separated strings, as in GET /restapis/{restapi_id}/deployments/{deployment_id}?embed=var1,var2 . The SDK and other platform-dependent libraries might use a different format for the list. Currently, this request supports only retrieval of the embedded API summary this way. Hence, the parameter value must be a single-valued list containing only the 'apisummary' string. For example, GET /restapis/{restapi_id}/deployments/{deployment_id}?embed=apisummary .
            (string) --
            

    :rtype: dict
    :return: {
        'id': 'string',
        'description': 'string',
        'createdDate': datetime(2015, 1, 1),
        'apiSummary': {
            'string': {
                'string': {
                    'authorizationType': 'string',
                    'apiKeyRequired': True|False
                }
            }
        }
    }
    
    
    """
    pass

def get_deployments(restApiId=None, position=None, limit=None):
    """
    Gets information about a  Deployments collection.
    See also: AWS API Documentation
    
    
    :example: response = client.get_deployments(
        restApiId='string',
        position='string',
        limit=123
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'id': 'string',
                'description': 'string',
                'createdDate': datetime(2015, 1, 1),
                'apiSummary': {
                    'string': {
                        'string': {
                            'authorizationType': 'string',
                            'apiKeyRequired': True|False
                        }
                    }
                }
            },
        ]
    }
    
    
    """
    pass

def get_documentation_part(restApiId=None, documentationPartId=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.get_documentation_part(
        restApiId='string',
        documentationPartId='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type documentationPartId: string
    :param documentationPartId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :rtype: dict
    :return: {
        'id': 'string',
        'location': {
            'type': 'API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'|'PATH_PARAMETER'|'QUERY_PARAMETER'|'REQUEST_HEADER'|'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'|'RESPONSE_BODY',
            'path': 'string',
            'method': 'string',
            'statusCode': 'string',
            'name': 'string'
        },
        'properties': 'string'
    }
    
    
    """
    pass

def get_documentation_parts(restApiId=None, type=None, nameQuery=None, path=None, position=None, limit=None, locationStatus=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.get_documentation_parts(
        restApiId='string',
        type='API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'|'PATH_PARAMETER'|'QUERY_PARAMETER'|'REQUEST_HEADER'|'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'|'RESPONSE_BODY',
        nameQuery='string',
        path='string',
        position='string',
        limit=123,
        locationStatus='DOCUMENTED'|'UNDOCUMENTED'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type type: string
    :param type: The type of API entities of the to-be-retrieved documentation parts.

    :type nameQuery: string
    :param nameQuery: The name of API entities of the to-be-retrieved documentation parts.

    :type path: string
    :param path: The path of API entities of the to-be-retrieved documentation parts.

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :type locationStatus: string
    :param locationStatus: The status of the API documentation parts to retrieve. Valid values are DOCUMENTED for retrieving DocumentationPart resources with content and UNDOCUMENTED for DocumentationPart resources without content.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'id': 'string',
                'location': {
                    'type': 'API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'|'PATH_PARAMETER'|'QUERY_PARAMETER'|'REQUEST_HEADER'|'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'|'RESPONSE_BODY',
                    'path': 'string',
                    'method': 'string',
                    'statusCode': 'string',
                    'name': 'string'
                },
                'properties': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_documentation_version(restApiId=None, documentationVersion=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.get_documentation_version(
        restApiId='string',
        documentationVersion='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type documentationVersion: string
    :param documentationVersion: [REQUIRED]
            [Required] The version identifier of the to-be-retrieved documentation snapshot.
            

    :rtype: dict
    :return: {
        'version': 'string',
        'createdDate': datetime(2015, 1, 1),
        'description': 'string'
    }
    
    
    """
    pass

def get_documentation_versions(restApiId=None, position=None, limit=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.get_documentation_versions(
        restApiId='string',
        position='string',
        limit=123
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'version': 'string',
                'createdDate': datetime(2015, 1, 1),
                'description': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_domain_name(domainName=None):
    """
    Represents a domain name that is contained in a simpler, more intuitive URL that can be called.
    See also: AWS API Documentation
    
    
    :example: response = client.get_domain_name(
        domainName='string'
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            [Required] The name of the DomainName resource.
            

    :rtype: dict
    :return: {
        'domainName': 'string',
        'certificateName': 'string',
        'certificateArn': 'string',
        'certificateUploadDate': datetime(2015, 1, 1),
        'regionalDomainName': 'string',
        'regionalHostedZoneId': 'string',
        'regionalCertificateName': 'string',
        'regionalCertificateArn': 'string',
        'distributionDomainName': 'string',
        'distributionHostedZoneId': 'string',
        'endpointConfiguration': {
            'types': [
                'REGIONAL'|'EDGE',
            ]
        }
    }
    
    
    """
    pass

def get_domain_names(position=None, limit=None):
    """
    Represents a collection of  DomainName resources.
    See also: AWS API Documentation
    
    
    :example: response = client.get_domain_names(
        position='string',
        limit=123
    )
    
    
    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'domainName': 'string',
                'certificateName': 'string',
                'certificateArn': 'string',
                'certificateUploadDate': datetime(2015, 1, 1),
                'regionalDomainName': 'string',
                'regionalHostedZoneId': 'string',
                'regionalCertificateName': 'string',
                'regionalCertificateArn': 'string',
                'distributionDomainName': 'string',
                'distributionHostedZoneId': 'string',
                'endpointConfiguration': {
                    'types': [
                        'REGIONAL'|'EDGE',
                    ]
                }
            },
        ]
    }
    
    
    """
    pass

def get_export(restApiId=None, stageName=None, exportType=None, parameters=None, accepts=None):
    """
    Exports a deployed version of a  RestApi in a specified format.
    See also: AWS API Documentation
    
    
    :example: response = client.get_export(
        restApiId='string',
        stageName='string',
        exportType='string',
        parameters={
            'string': 'string'
        },
        accepts='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type stageName: string
    :param stageName: [REQUIRED]
            [Required] The name of the Stage that will be exported.
            

    :type exportType: string
    :param exportType: [REQUIRED]
            [Required] The type of export. Currently only 'swagger' is supported.
            

    :type parameters: dict
    :param parameters: A key-value map of query string parameters that specify properties of the export, depending on the requested exportType . For exportType swagger , any combination of the following parameters are supported: integrations will export the API with x-amazon-apigateway-integration extensions. authorizers will export the API with x-amazon-apigateway-authorizer extensions. postman will export the API with Postman extensions, allowing for import to the Postman tool
            (string) --
            (string) --
            

    :type accepts: string
    :param accepts: The content-type of the export, for example application/json . Currently application/json and application/yaml are supported for exportType of swagger . This should be specified in the Accept header for direct API requests.

    :rtype: dict
    :return: {
        'contentType': 'string',
        'contentDisposition': 'string',
        'body': StreamingBody()
    }
    
    
    """
    pass

def get_gateway_response(restApiId=None, responseType=None):
    """
    Gets a  GatewayResponse of a specified response type on the given  RestApi .
    See also: AWS API Documentation
    
    
    :example: response = client.get_gateway_response(
        restApiId='string',
        responseType='DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type responseType: string
    :param responseType: [REQUIRED]
            [Required]
            The response type of the associated GatewayResponse . Valid values are
            ACCESS_DENIED
            API_CONFIGURATION_ERROR
            AUTHORIZER_FAILURE
            AUTHORIZER_CONFIGURATION_ERROR
            BAD_REQUEST_PARAMETERS
            BAD_REQUEST_BODY
            DEFAULT_4XX
            DEFAULT_5XX
            EXPIRED_TOKEN
            INVALID_SIGNATURE
            INTEGRATION_FAILURE
            INTEGRATION_TIMEOUT
            INVALID_API_KEY
            MISSING_AUTHENTICATION_TOKEN
            QUOTA_EXCEEDED
            REQUEST_TOO_LARGE
            RESOURCE_NOT_FOUND
            THROTTLED
            UNAUTHORIZED
            UNSUPPORTED_MEDIA_TYPE
            

    :rtype: dict
    :return: {
        'responseType': 'DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED',
        'statusCode': 'string',
        'responseParameters': {
            'string': 'string'
        },
        'responseTemplates': {
            'string': 'string'
        },
        'defaultResponse': True|False
    }
    
    
    :returns: 
    ACCESS_DENIED
    API_CONFIGURATION_ERROR
    AUTHORIZER_FAILURE
    AUTHORIZER_CONFIGURATION_ERROR
    BAD_REQUEST_PARAMETERS
    BAD_REQUEST_BODY
    DEFAULT_4XX
    DEFAULT_5XX
    EXPIRED_TOKEN
    INVALID_SIGNATURE
    INTEGRATION_FAILURE
    INTEGRATION_TIMEOUT
    INVALID_API_KEY
    MISSING_AUTHENTICATION_TOKEN
    QUOTA_EXCEEDED
    REQUEST_TOO_LARGE
    RESOURCE_NOT_FOUND
    THROTTLED
    UNAUTHORIZED
    UNSUPPORTED_MEDIA_TYPE
    
    """
    pass

def get_gateway_responses(restApiId=None, position=None, limit=None):
    """
    Gets the  GatewayResponses collection on the given  RestApi . If an API developer has not added any definitions for gateway responses, the result will be the API Gateway-generated default  GatewayResponses collection for the supported response types.
    See also: AWS API Documentation
    
    
    :example: response = client.get_gateway_responses(
        restApiId='string',
        position='string',
        limit=123
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type position: string
    :param position: The current pagination position in the paged result set. The GatewayResponse collection does not support pagination and the position does not apply here.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500. The GatewayResponses collection does not support pagination and the limit does not apply here.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'responseType': 'DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED',
                'statusCode': 'string',
                'responseParameters': {
                    'string': 'string'
                },
                'responseTemplates': {
                    'string': 'string'
                },
                'defaultResponse': True|False
            },
        ]
    }
    
    
    :returns: 
    ACCESS_DENIED
    API_CONFIGURATION_ERROR
    AUTHORIZER_FAILURE
    AUTHORIZER_CONFIGURATION_ERROR
    BAD_REQUEST_PARAMETERS
    BAD_REQUEST_BODY
    DEFAULT_4XX
    DEFAULT_5XX
    EXPIRED_TOKEN
    INVALID_SIGNATURE
    INTEGRATION_FAILURE
    INTEGRATION_TIMEOUT
    INVALID_API_KEY
    MISSING_AUTHENTICATION_TOKEN
    QUOTA_EXCEEDED
    REQUEST_TOO_LARGE
    RESOURCE_NOT_FOUND
    THROTTLED
    UNAUTHORIZED
    UNSUPPORTED_MEDIA_TYPE
    
    """
    pass

def get_integration(restApiId=None, resourceId=None, httpMethod=None):
    """
    Get the integration settings.
    See also: AWS API Documentation
    
    
    :example: response = client.get_integration(
        restApiId='string',
        resourceId='string',
        httpMethod='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] Specifies a get integration request's resource identifier
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] Specifies a get integration request's HTTP method.
            

    :rtype: dict
    :return: {
        'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
        'httpMethod': 'string',
        'uri': 'string',
        'connectionType': 'INTERNET'|'VPC_LINK',
        'connectionId': 'string',
        'credentials': 'string',
        'requestParameters': {
            'string': 'string'
        },
        'requestTemplates': {
            'string': 'string'
        },
        'passthroughBehavior': 'string',
        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
        'timeoutInMillis': 123,
        'cacheNamespace': 'string',
        'cacheKeyParameters': [
            'string',
        ],
        'integrationResponses': {
            'string': {
                'statusCode': 'string',
                'selectionPattern': 'string',
                'responseParameters': {
                    'string': 'string'
                },
                'responseTemplates': {
                    'string': 'string'
                },
                'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
            }
        }
    }
    
    
    :returns: 
    AWS : for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
    AWS_PROXY : for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
    HTTP : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
    HTTP_PROXY : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
    MOCK : for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.
    
    """
    pass

def get_integration_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None):
    """
    Represents a get integration response.
    See also: AWS API Documentation
    
    
    :example: response = client.get_integration_response(
        restApiId='string',
        resourceId='string',
        httpMethod='string',
        statusCode='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] Specifies a get integration response request's resource identifier.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] Specifies a get integration response request's HTTP method.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            [Required] Specifies a get integration response request's status code.
            

    :rtype: dict
    :return: {
        'statusCode': 'string',
        'selectionPattern': 'string',
        'responseParameters': {
            'string': 'string'
        },
        'responseTemplates': {
            'string': 'string'
        },
        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_method(restApiId=None, resourceId=None, httpMethod=None):
    """
    Describe an existing  Method resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_method(
        restApiId='string',
        resourceId='string',
        httpMethod='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] The Resource identifier for the Method resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] Specifies the method request's HTTP method type.
            

    :rtype: dict
    :return: {
        'httpMethod': 'string',
        'authorizationType': 'string',
        'authorizerId': 'string',
        'apiKeyRequired': True|False,
        'requestValidatorId': 'string',
        'operationName': 'string',
        'requestParameters': {
            'string': True|False
        },
        'requestModels': {
            'string': 'string'
        },
        'methodResponses': {
            'string': {
                'statusCode': 'string',
                'responseParameters': {
                    'string': True|False
                },
                'responseModels': {
                    'string': 'string'
                }
            }
        },
        'methodIntegration': {
            'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
            'httpMethod': 'string',
            'uri': 'string',
            'connectionType': 'INTERNET'|'VPC_LINK',
            'connectionId': 'string',
            'credentials': 'string',
            'requestParameters': {
                'string': 'string'
            },
            'requestTemplates': {
                'string': 'string'
            },
            'passthroughBehavior': 'string',
            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
            'timeoutInMillis': 123,
            'cacheNamespace': 'string',
            'cacheKeyParameters': [
                'string',
            ],
            'integrationResponses': {
                'string': {
                    'statusCode': 'string',
                    'selectionPattern': 'string',
                    'responseParameters': {
                        'string': 'string'
                    },
                    'responseTemplates': {
                        'string': 'string'
                    },
                    'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                }
            }
        },
        'authorizationScopes': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    (boolean) --
    
    
    
    """
    pass

def get_method_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None):
    """
    Describes a  MethodResponse resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_method_response(
        restApiId='string',
        resourceId='string',
        httpMethod='string',
        statusCode='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] The Resource identifier for the MethodResponse resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] The HTTP verb of the Method resource.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            [Required] The status code for the MethodResponse resource.
            

    :rtype: dict
    :return: {
        'statusCode': 'string',
        'responseParameters': {
            'string': True|False
        },
        'responseModels': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (boolean) --
    
    
    
    """
    pass

def get_model(restApiId=None, modelName=None, flatten=None):
    """
    Describes an existing model defined for a  RestApi resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_model(
        restApiId='string',
        modelName='string',
        flatten=True|False
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The RestApi identifier under which the Model exists.
            

    :type modelName: string
    :param modelName: [REQUIRED]
            [Required] The name of the model as an identifier.
            

    :type flatten: boolean
    :param flatten: A query parameter of a Boolean value to resolve (true ) all external model references and returns a flattened model schema or not (false ) The default is false .

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'description': 'string',
        'schema': 'string',
        'contentType': 'string'
    }
    
    
    """
    pass

def get_model_template(restApiId=None, modelName=None):
    """
    Generates a sample mapping template that can be used to transform a payload into the structure of a model.
    See also: AWS API Documentation
    
    
    :example: response = client.get_model_template(
        restApiId='string',
        modelName='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type modelName: string
    :param modelName: [REQUIRED]
            [Required] The name of the model for which to generate a template.
            

    :rtype: dict
    :return: {
        'value': 'string'
    }
    
    
    """
    pass

def get_models(restApiId=None, position=None, limit=None):
    """
    Describes existing  Models defined for a  RestApi resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_models(
        restApiId='string',
        position='string',
        limit=123
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'id': 'string',
                'name': 'string',
                'description': 'string',
                'schema': 'string',
                'contentType': 'string'
            },
        ]
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

def get_request_validator(restApiId=None, requestValidatorId=None):
    """
    Gets a  RequestValidator of a given  RestApi .
    See also: AWS API Documentation
    
    
    :example: response = client.get_request_validator(
        restApiId='string',
        requestValidatorId='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type requestValidatorId: string
    :param requestValidatorId: [REQUIRED]
            [Required] The identifier of the RequestValidator to be retrieved.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'validateRequestBody': True|False,
        'validateRequestParameters': True|False
    }
    
    
    """
    pass

def get_request_validators(restApiId=None, position=None, limit=None):
    """
    Gets the  RequestValidators collection of a given  RestApi .
    See also: AWS API Documentation
    
    
    :example: response = client.get_request_validators(
        restApiId='string',
        position='string',
        limit=123
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'id': 'string',
                'name': 'string',
                'validateRequestBody': True|False,
                'validateRequestParameters': True|False
            },
        ]
    }
    
    
    """
    pass

def get_resource(restApiId=None, resourceId=None, embed=None):
    """
    Lists information about a resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_resource(
        restApiId='string',
        resourceId='string',
        embed=[
            'string',
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] The identifier for the Resource resource.
            

    :type embed: list
    :param embed: A query parameter to retrieve the specified resources embedded in the returned Resource representation in the response. This embed parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded Method resources this way. The query parameter value must be a single-valued list and contain the 'methods' string. For example, GET /restapis/{restapi_id}/resources/{resource_id}?embed=methods .
            (string) --
            

    :rtype: dict
    :return: {
        'id': 'string',
        'parentId': 'string',
        'pathPart': 'string',
        'path': 'string',
        'resourceMethods': {
            'string': {
                'httpMethod': 'string',
                'authorizationType': 'string',
                'authorizerId': 'string',
                'apiKeyRequired': True|False,
                'requestValidatorId': 'string',
                'operationName': 'string',
                'requestParameters': {
                    'string': True|False
                },
                'requestModels': {
                    'string': 'string'
                },
                'methodResponses': {
                    'string': {
                        'statusCode': 'string',
                        'responseParameters': {
                            'string': True|False
                        },
                        'responseModels': {
                            'string': 'string'
                        }
                    }
                },
                'methodIntegration': {
                    'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                    'httpMethod': 'string',
                    'uri': 'string',
                    'connectionType': 'INTERNET'|'VPC_LINK',
                    'connectionId': 'string',
                    'credentials': 'string',
                    'requestParameters': {
                        'string': 'string'
                    },
                    'requestTemplates': {
                        'string': 'string'
                    },
                    'passthroughBehavior': 'string',
                    'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                    'timeoutInMillis': 123,
                    'cacheNamespace': 'string',
                    'cacheKeyParameters': [
                        'string',
                    ],
                    'integrationResponses': {
                        'string': {
                            'statusCode': 'string',
                            'selectionPattern': 'string',
                            'responseParameters': {
                                'string': 'string'
                            },
                            'responseTemplates': {
                                'string': 'string'
                            },
                            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                        }
                    }
                },
                'authorizationScopes': [
                    'string',
                ]
            }
        }
    }
    
    
    :returns: 
    (string) --
    (boolean) --
    
    
    
    """
    pass

def get_resources(restApiId=None, position=None, limit=None, embed=None):
    """
    Lists information about a collection of  Resource resources.
    See also: AWS API Documentation
    
    
    :example: response = client.get_resources(
        restApiId='string',
        position='string',
        limit=123,
        embed=[
            'string',
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :type embed: list
    :param embed: A query parameter used to retrieve the specified resources embedded in the returned Resources resource in the response. This embed parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded Method resources this way. The query parameter value must be a single-valued list and contain the 'methods' string. For example, GET /restapis/{restapi_id}/resources?embed=methods .
            (string) --
            

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'id': 'string',
                'parentId': 'string',
                'pathPart': 'string',
                'path': 'string',
                'resourceMethods': {
                    'string': {
                        'httpMethod': 'string',
                        'authorizationType': 'string',
                        'authorizerId': 'string',
                        'apiKeyRequired': True|False,
                        'requestValidatorId': 'string',
                        'operationName': 'string',
                        'requestParameters': {
                            'string': True|False
                        },
                        'requestModels': {
                            'string': 'string'
                        },
                        'methodResponses': {
                            'string': {
                                'statusCode': 'string',
                                'responseParameters': {
                                    'string': True|False
                                },
                                'responseModels': {
                                    'string': 'string'
                                }
                            }
                        },
                        'methodIntegration': {
                            'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                            'httpMethod': 'string',
                            'uri': 'string',
                            'connectionType': 'INTERNET'|'VPC_LINK',
                            'connectionId': 'string',
                            'credentials': 'string',
                            'requestParameters': {
                                'string': 'string'
                            },
                            'requestTemplates': {
                                'string': 'string'
                            },
                            'passthroughBehavior': 'string',
                            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                            'timeoutInMillis': 123,
                            'cacheNamespace': 'string',
                            'cacheKeyParameters': [
                                'string',
                            ],
                            'integrationResponses': {
                                'string': {
                                    'statusCode': 'string',
                                    'selectionPattern': 'string',
                                    'responseParameters': {
                                        'string': 'string'
                                    },
                                    'responseTemplates': {
                                        'string': 'string'
                                    },
                                    'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                                }
                            }
                        },
                        'authorizationScopes': [
                            'string',
                        ]
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (boolean) --
    
    
    
    """
    pass

def get_rest_api(restApiId=None):
    """
    Lists the  RestApi resource in the collection.
    See also: AWS API Documentation
    
    
    :example: response = client.get_rest_api(
        restApiId='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'description': 'string',
        'createdDate': datetime(2015, 1, 1),
        'version': 'string',
        'warnings': [
            'string',
        ],
        'binaryMediaTypes': [
            'string',
        ],
        'minimumCompressionSize': 123,
        'apiKeySource': 'HEADER'|'AUTHORIZER',
        'endpointConfiguration': {
            'types': [
                'REGIONAL'|'EDGE',
            ]
        },
        'policy': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_rest_apis(position=None, limit=None):
    """
    Lists the  RestApis resources for your collection.
    See also: AWS API Documentation
    
    
    :example: response = client.get_rest_apis(
        position='string',
        limit=123
    )
    
    
    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'id': 'string',
                'name': 'string',
                'description': 'string',
                'createdDate': datetime(2015, 1, 1),
                'version': 'string',
                'warnings': [
                    'string',
                ],
                'binaryMediaTypes': [
                    'string',
                ],
                'minimumCompressionSize': 123,
                'apiKeySource': 'HEADER'|'AUTHORIZER',
                'endpointConfiguration': {
                    'types': [
                        'REGIONAL'|'EDGE',
                    ]
                },
                'policy': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_sdk(restApiId=None, stageName=None, sdkType=None, parameters=None):
    """
    Generates a client SDK for a  RestApi and  Stage .
    See also: AWS API Documentation
    
    
    :example: response = client.get_sdk(
        restApiId='string',
        stageName='string',
        sdkType='string',
        parameters={
            'string': 'string'
        }
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type stageName: string
    :param stageName: [REQUIRED]
            [Required] The name of the Stage that the SDK will use.
            

    :type sdkType: string
    :param sdkType: [REQUIRED]
            [Required] The language for the generated SDK. Currently java , javascript , android , objectivec (for iOS), swift (for iOS), and ruby are supported.
            

    :type parameters: dict
    :param parameters: A string-to-string key-value map of query parameters sdkType -dependent properties of the SDK. For sdkType of objectivec or swift , a parameter named classPrefix is required. For sdkType of android , parameters named groupId , artifactId , artifactVersion , and invokerPackage are required. For sdkType of java , parameters named serviceName and javaPackageName are required.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'contentType': 'string',
        'contentDisposition': 'string',
        'body': StreamingBody()
    }
    
    
    """
    pass

def get_sdk_type(id=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.get_sdk_type(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]
            [Required] The identifier of the queried SdkType instance.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'friendlyName': 'string',
        'description': 'string',
        'configurationProperties': [
            {
                'name': 'string',
                'friendlyName': 'string',
                'description': 'string',
                'required': True|False,
                'defaultValue': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_sdk_types(position=None, limit=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.get_sdk_types(
        position='string',
        limit=123
    )
    
    
    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'id': 'string',
                'friendlyName': 'string',
                'description': 'string',
                'configurationProperties': [
                    {
                        'name': 'string',
                        'friendlyName': 'string',
                        'description': 'string',
                        'required': True|False,
                        'defaultValue': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def get_stage(restApiId=None, stageName=None):
    """
    Gets information about a  Stage resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_stage(
        restApiId='string',
        stageName='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type stageName: string
    :param stageName: [REQUIRED]
            [Required] The name of the Stage resource to get information about.
            

    :rtype: dict
    :return: {
        'deploymentId': 'string',
        'clientCertificateId': 'string',
        'stageName': 'string',
        'description': 'string',
        'cacheClusterEnabled': True|False,
        'cacheClusterSize': '0.5'|'1.6'|'6.1'|'13.5'|'28.4'|'58.2'|'118'|'237',
        'cacheClusterStatus': 'CREATE_IN_PROGRESS'|'AVAILABLE'|'DELETE_IN_PROGRESS'|'NOT_AVAILABLE'|'FLUSH_IN_PROGRESS',
        'methodSettings': {
            'string': {
                'metricsEnabled': True|False,
                'loggingLevel': 'string',
                'dataTraceEnabled': True|False,
                'throttlingBurstLimit': 123,
                'throttlingRateLimit': 123.0,
                'cachingEnabled': True|False,
                'cacheTtlInSeconds': 123,
                'cacheDataEncrypted': True|False,
                'requireAuthorizationForCacheControl': True|False,
                'unauthorizedCacheControlHeaderStrategy': 'FAIL_WITH_403'|'SUCCEED_WITH_RESPONSE_HEADER'|'SUCCEED_WITHOUT_RESPONSE_HEADER'
            }
        },
        'variables': {
            'string': 'string'
        },
        'documentationVersion': 'string',
        'accessLogSettings': {
            'format': 'string',
            'destinationArn': 'string'
        },
        'canarySettings': {
            'percentTraffic': 123.0,
            'deploymentId': 'string',
            'stageVariableOverrides': {
                'string': 'string'
            },
            'useStageCache': True|False
        },
        'tags': {
            'string': 'string'
        },
        'createdDate': datetime(2015, 1, 1),
        'lastUpdatedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_stages(restApiId=None, deploymentId=None):
    """
    Gets information about one or more  Stage resources.
    See also: AWS API Documentation
    
    
    :example: response = client.get_stages(
        restApiId='string',
        deploymentId='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type deploymentId: string
    :param deploymentId: The stages' deployment identifiers.

    :rtype: dict
    :return: {
        'item': [
            {
                'deploymentId': 'string',
                'clientCertificateId': 'string',
                'stageName': 'string',
                'description': 'string',
                'cacheClusterEnabled': True|False,
                'cacheClusterSize': '0.5'|'1.6'|'6.1'|'13.5'|'28.4'|'58.2'|'118'|'237',
                'cacheClusterStatus': 'CREATE_IN_PROGRESS'|'AVAILABLE'|'DELETE_IN_PROGRESS'|'NOT_AVAILABLE'|'FLUSH_IN_PROGRESS',
                'methodSettings': {
                    'string': {
                        'metricsEnabled': True|False,
                        'loggingLevel': 'string',
                        'dataTraceEnabled': True|False,
                        'throttlingBurstLimit': 123,
                        'throttlingRateLimit': 123.0,
                        'cachingEnabled': True|False,
                        'cacheTtlInSeconds': 123,
                        'cacheDataEncrypted': True|False,
                        'requireAuthorizationForCacheControl': True|False,
                        'unauthorizedCacheControlHeaderStrategy': 'FAIL_WITH_403'|'SUCCEED_WITH_RESPONSE_HEADER'|'SUCCEED_WITHOUT_RESPONSE_HEADER'
                    }
                },
                'variables': {
                    'string': 'string'
                },
                'documentationVersion': 'string',
                'accessLogSettings': {
                    'format': 'string',
                    'destinationArn': 'string'
                },
                'canarySettings': {
                    'percentTraffic': 123.0,
                    'deploymentId': 'string',
                    'stageVariableOverrides': {
                        'string': 'string'
                    },
                    'useStageCache': True|False
                },
                'tags': {
                    'string': 'string'
                },
                'createdDate': datetime(2015, 1, 1),
                'lastUpdatedDate': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_tags(resourceArn=None, position=None, limit=None):
    """
    Gets the  Tags collection for a given resource.
    See also: AWS API Documentation
    
    
    :example: response = client.get_tags(
        resourceArn='string',
        position='string',
        limit=123
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            [Required] The ARN of a resource that can be tagged. The resource ARN must be URL-encoded. At present, Stage is the only taggable resource.
            

    :type position: string
    :param position: (Not currently supported) The current pagination position in the paged result set.

    :type limit: integer
    :param limit: (Not currently supported) The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :rtype: dict
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

def get_usage(usagePlanId=None, keyId=None, startDate=None, endDate=None, position=None, limit=None):
    """
    Gets the usage data of a usage plan in a specified time interval.
    See also: AWS API Documentation
    
    
    :example: response = client.get_usage(
        usagePlanId='string',
        keyId='string',
        startDate='string',
        endDate='string',
        position='string',
        limit=123
    )
    
    
    :type usagePlanId: string
    :param usagePlanId: [REQUIRED]
            [Required] The Id of the usage plan associated with the usage data.
            

    :type keyId: string
    :param keyId: The Id of the API key associated with the resultant usage data.

    :type startDate: string
    :param startDate: [REQUIRED]
            [Required] The starting date (e.g., 2016-01-01) of the usage data.
            

    :type endDate: string
    :param endDate: [REQUIRED]
            [Required] The ending date (e.g., 2016-12-31) of the usage data.
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :rtype: dict
    :return: {
        'usagePlanId': 'string',
        'startDate': 'string',
        'endDate': 'string',
        'position': 'string',
        'items': {
            'string': [
                [
                    123,
                ],
            ]
        }
    }
    
    
    :returns: 
    (string) --
    (list) --
    (list) --
    (integer) --
    
    
    
    
    
    
    
    """
    pass

def get_usage_plan(usagePlanId=None):
    """
    Gets a usage plan of a given plan identifier.
    See also: AWS API Documentation
    
    
    :example: response = client.get_usage_plan(
        usagePlanId='string'
    )
    
    
    :type usagePlanId: string
    :param usagePlanId: [REQUIRED]
            [Required] The identifier of the UsagePlan resource to be retrieved.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'description': 'string',
        'apiStages': [
            {
                'apiId': 'string',
                'stage': 'string'
            },
        ],
        'throttle': {
            'burstLimit': 123,
            'rateLimit': 123.0
        },
        'quota': {
            'limit': 123,
            'offset': 123,
            'period': 'DAY'|'WEEK'|'MONTH'
        },
        'productCode': 'string'
    }
    
    
    """
    pass

def get_usage_plan_key(usagePlanId=None, keyId=None):
    """
    Gets a usage plan key of a given key identifier.
    See also: AWS API Documentation
    
    
    :example: response = client.get_usage_plan_key(
        usagePlanId='string',
        keyId='string'
    )
    
    
    :type usagePlanId: string
    :param usagePlanId: [REQUIRED]
            [Required] The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.
            

    :type keyId: string
    :param keyId: [REQUIRED]
            [Required] The key Id of the to-be-retrieved UsagePlanKey resource representing a plan customer.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'type': 'string',
        'value': 'string',
        'name': 'string'
    }
    
    
    """
    pass

def get_usage_plan_keys(usagePlanId=None, position=None, limit=None, nameQuery=None):
    """
    Gets all the usage plan keys representing the API keys added to a specified usage plan.
    See also: AWS API Documentation
    
    
    :example: response = client.get_usage_plan_keys(
        usagePlanId='string',
        position='string',
        limit=123,
        nameQuery='string'
    )
    
    
    :type usagePlanId: string
    :param usagePlanId: [REQUIRED]
            [Required] The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :type nameQuery: string
    :param nameQuery: A query parameter specifying the name of the to-be-returned usage plan keys.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'id': 'string',
                'type': 'string',
                'value': 'string',
                'name': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_usage_plans(position=None, keyId=None, limit=None):
    """
    Gets all the usage plans of the caller's account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_usage_plans(
        position='string',
        keyId='string',
        limit=123
    )
    
    
    :type position: string
    :param position: The current pagination position in the paged result set.

    :type keyId: string
    :param keyId: The identifier of the API key associated with the usage plans.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'id': 'string',
                'name': 'string',
                'description': 'string',
                'apiStages': [
                    {
                        'apiId': 'string',
                        'stage': 'string'
                    },
                ],
                'throttle': {
                    'burstLimit': 123,
                    'rateLimit': 123.0
                },
                'quota': {
                    'limit': 123,
                    'offset': 123,
                    'period': 'DAY'|'WEEK'|'MONTH'
                },
                'productCode': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_vpc_link(vpcLinkId=None):
    """
    Gets a specified VPC link under the caller's account in a region.
    See also: AWS API Documentation
    
    
    :example: response = client.get_vpc_link(
        vpcLinkId='string'
    )
    
    
    :type vpcLinkId: string
    :param vpcLinkId: [REQUIRED]
            [Required] The identifier of the VpcLink . It is used in an Integration to reference this VpcLink .
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'description': 'string',
        'targetArns': [
            'string',
        ],
        'status': 'AVAILABLE'|'PENDING'|'DELETING'|'FAILED',
        'statusMessage': 'string'
    }
    
    
    """
    pass

def get_vpc_links(position=None, limit=None):
    """
    Gets the  VpcLinks collection under the caller's account in a selected region.
    See also: AWS API Documentation
    
    
    :example: response = client.get_vpc_links(
        position='string',
        limit=123
    )
    
    
    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'id': 'string',
                'name': 'string',
                'description': 'string',
                'targetArns': [
                    'string',
                ],
                'status': 'AVAILABLE'|'PENDING'|'DELETING'|'FAILED',
                'statusMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def import_api_keys(body=None, format=None, failOnWarnings=None):
    """
    Import API keys from an external source, such as a CSV-formatted file.
    See also: AWS API Documentation
    
    
    :example: response = client.import_api_keys(
        body=b'bytes'|file,
        format='csv',
        failOnWarnings=True|False
    )
    
    
    :type body: bytes or seekable file-like object
    :param body: [REQUIRED]
            The payload of the POST request to import API keys. For the payload format, see API Key File Format .
            

    :type format: string
    :param format: [REQUIRED]
            A query parameter to specify the input format to imported API keys. Currently, only the csv format is supported.
            

    :type failOnWarnings: boolean
    :param failOnWarnings: A query parameter to indicate whether to rollback ApiKey importation (true ) or not (false ) when error is encountered.

    :rtype: dict
    :return: {
        'ids': [
            'string',
        ],
        'warnings': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def import_documentation_parts(restApiId=None, mode=None, failOnWarnings=None, body=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.import_documentation_parts(
        restApiId='string',
        mode='merge'|'overwrite',
        failOnWarnings=True|False,
        body=b'bytes'|file
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type mode: string
    :param mode: A query parameter to indicate whether to overwrite (OVERWRITE ) any existing DocumentationParts definition or to merge (MERGE ) the new definition into the existing one. The default value is MERGE .

    :type failOnWarnings: boolean
    :param failOnWarnings: A query parameter to specify whether to rollback the documentation importation (true ) or not (false ) when a warning is encountered. The default value is false .

    :type body: bytes or seekable file-like object
    :param body: [REQUIRED]
            [Required] Raw byte array representing the to-be-imported documentation parts. To import from a Swagger file, this is a JSON object.
            

    :rtype: dict
    :return: {
        'ids': [
            'string',
        ],
        'warnings': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def import_rest_api(failOnWarnings=None, parameters=None, body=None):
    """
    A feature of the API Gateway control service for creating a new API from an external API definition file.
    See also: AWS API Documentation
    
    
    :example: response = client.import_rest_api(
        failOnWarnings=True|False,
        parameters={
            'string': 'string'
        },
        body=b'bytes'|file
    )
    
    
    :type failOnWarnings: boolean
    :param failOnWarnings: A query parameter to indicate whether to rollback the API creation (true ) or not (false ) when a warning is encountered. The default value is false .

    :type parameters: dict
    :param parameters: A key-value map of context-specific query string parameters specifying the behavior of different API importing operations. The following shows operation-specific parameters and their supported values.
            To exclude DocumentationParts from the import, set parameters as ignore=documentation .
            To configure the endpoint type, set parameters as endpointConfigurationTypes=EDGE or``endpointConfigurationTypes=REGIONAL`` . The default endpoint type is EDGE .
            To handle imported basePath , set parameters as basePath=ignore , basePath=prepend or basePath=split .
            For example, the AWS CLI command to exclude documentation from the imported API is:
            aws apigateway import-rest-api --parameters ignore=documentation --body 'file:///path/to/imported-api-body.json
            The AWS CLI command to set the regional endpoint on the imported API is:
            aws apigateway import-rest-api --parameters endpointConfigurationTypes=REGIONAL --body 'file:///path/to/imported-api-body.json
            (string) --
            (string) --
            

    :type body: bytes or seekable file-like object
    :param body: [REQUIRED]
            [Required] The POST request body containing external API definitions. Currently, only Swagger definition JSON files are supported. The maximum size of the API definition file is 2MB.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'description': 'string',
        'createdDate': datetime(2015, 1, 1),
        'version': 'string',
        'warnings': [
            'string',
        ],
        'binaryMediaTypes': [
            'string',
        ],
        'minimumCompressionSize': 123,
        'apiKeySource': 'HEADER'|'AUTHORIZER',
        'endpointConfiguration': {
            'types': [
                'REGIONAL'|'EDGE',
            ]
        },
        'policy': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_gateway_response(restApiId=None, responseType=None, statusCode=None, responseParameters=None, responseTemplates=None):
    """
    Creates a customization of a  GatewayResponse of a specified response type and status code on the given  RestApi .
    See also: AWS API Documentation
    
    
    :example: response = client.put_gateway_response(
        restApiId='string',
        responseType='DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED',
        statusCode='string',
        responseParameters={
            'string': 'string'
        },
        responseTemplates={
            'string': 'string'
        }
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type responseType: string
    :param responseType: [REQUIRED]
            [Required]
            The response type of the associated GatewayResponse . Valid values are
            ACCESS_DENIED
            API_CONFIGURATION_ERROR
            AUTHORIZER_FAILURE
            AUTHORIZER_CONFIGURATION_ERROR
            BAD_REQUEST_PARAMETERS
            BAD_REQUEST_BODY
            DEFAULT_4XX
            DEFAULT_5XX
            EXPIRED_TOKEN
            INVALID_SIGNATURE
            INTEGRATION_FAILURE
            INTEGRATION_TIMEOUT
            INVALID_API_KEY
            MISSING_AUTHENTICATION_TOKEN
            QUOTA_EXCEEDED
            REQUEST_TOO_LARGE
            RESOURCE_NOT_FOUND
            THROTTLED
            UNAUTHORIZED
            UNSUPPORTED_MEDIA_TYPE
            

    :type statusCode: string
    :param statusCode: The HTTP status code of the GatewayResponse .

    :type responseParameters: dict
    :param responseParameters: Response parameters (paths, query strings and headers) of the GatewayResponse as a string-to-string map of key-value pairs.
            (string) --
            (string) --
            

    :type responseTemplates: dict
    :param responseTemplates: Response templates of the GatewayResponse as a string-to-string map of key-value pairs.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'responseType': 'DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED',
        'statusCode': 'string',
        'responseParameters': {
            'string': 'string'
        },
        'responseTemplates': {
            'string': 'string'
        },
        'defaultResponse': True|False
    }
    
    
    :returns: 
    ACCESS_DENIED
    API_CONFIGURATION_ERROR
    AUTHORIZER_FAILURE
    AUTHORIZER_CONFIGURATION_ERROR
    BAD_REQUEST_PARAMETERS
    BAD_REQUEST_BODY
    DEFAULT_4XX
    DEFAULT_5XX
    EXPIRED_TOKEN
    INVALID_SIGNATURE
    INTEGRATION_FAILURE
    INTEGRATION_TIMEOUT
    INVALID_API_KEY
    MISSING_AUTHENTICATION_TOKEN
    QUOTA_EXCEEDED
    REQUEST_TOO_LARGE
    RESOURCE_NOT_FOUND
    THROTTLED
    UNAUTHORIZED
    UNSUPPORTED_MEDIA_TYPE
    
    """
    pass

def put_integration(restApiId=None, resourceId=None, httpMethod=None, type=None, integrationHttpMethod=None, uri=None, connectionType=None, connectionId=None, credentials=None, requestParameters=None, requestTemplates=None, passthroughBehavior=None, cacheNamespace=None, cacheKeyParameters=None, contentHandling=None, timeoutInMillis=None):
    """
    Sets up a method's integration.
    See also: AWS API Documentation
    
    
    :example: response = client.put_integration(
        restApiId='string',
        resourceId='string',
        httpMethod='string',
        type='HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
        integrationHttpMethod='string',
        uri='string',
        connectionType='INTERNET'|'VPC_LINK',
        connectionId='string',
        credentials='string',
        requestParameters={
            'string': 'string'
        },
        requestTemplates={
            'string': 'string'
        },
        passthroughBehavior='string',
        cacheNamespace='string',
        cacheKeyParameters=[
            'string',
        ],
        contentHandling='CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
        timeoutInMillis=123
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] Specifies a put integration request's resource ID.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] Specifies a put integration request's HTTP method.
            

    :type type: string
    :param type: [REQUIRED]
            [Required] Specifies a put integration input's type.
            

    :type integrationHttpMethod: string
    :param integrationHttpMethod: Specifies a put integration HTTP method. When the integration type is HTTP or AWS, this field is required.

    :type uri: string
    :param uri: Specifies Uniform Resource Identifier (URI) of the integration endpoint.
            For HTTP or HTTP_PROXY integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification , for either standard integration, where connectionType is not VPC_LINK , or private integration, where connectionType is VPC_LINK . For a private HTTP integration, the URI is not used for routing.
            For AWS or AWS_PROXY integrations, the URI is of the form arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api} . Here, {Region} is the API Gateway region (e.g., us-east-1 ); {service} is the name of the integrated AWS service (e.g., s3 ); and {subdomain} is a designated subdomain supported by certain AWS service for fast host-name lookup. action can be used for an AWS service action-based API, using an Action={name}{p1}={v1}p2={v2}... query string. The ensuing {service_api} refers to a supported action {name} plus any required input parameters. Alternatively, path can be used for an AWS service path-based API. The ensuing service_api refers to the path to an AWS service resource, including the region of the integrated AWS service, if applicable. For example, for integration with the S3 API of `GetObject <http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__ , the uri can be either arn:aws:apigateway:us-west-2:s3:action/GetObjectBucket={bucket}Key={key} or arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}
            

    :type connectionType: string
    :param connectionType: The type of the network connection to the integration endpoint. The valid value is INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and a network load balancer in a VPC. The default value is INTERNET .

    :type connectionId: string
    :param connectionId: The (`id <http://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__ ) of the VpcLink used for the integration when connectionType=VPC_LINK and undefined, otherwise.

    :type credentials: string
    :param credentials: Specifies whether credentials are required for a put integration.

    :type requestParameters: dict
    :param requestParameters: A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of method.request.{location}.{name} , where location is querystring , path , or header and name must be a valid and unique method request parameter name.
            (string) --
            (string) --
            

    :type requestTemplates: dict
    :param requestTemplates: Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.
            (string) --
            (string) --
            

    :type passthroughBehavior: string
    :param passthroughBehavior: Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH , WHEN_NO_TEMPLATES , and NEVER .
            WHEN_NO_MATCH passes the request body for unmapped content types through to the integration back end without transformation.
            NEVER rejects unmapped content types with an HTTP 415 'Unsupported Media Type' response.
            WHEN_NO_TEMPLATES allows pass-through when the integration has NO content types mapped to templates. However if there is at least one content type defined, unmapped content types will be rejected with the same 415 response.
            

    :type cacheNamespace: string
    :param cacheNamespace: Specifies a put integration input's cache namespace.

    :type cacheKeyParameters: list
    :param cacheKeyParameters: Specifies a put integration input's cache key parameters.
            (string) --
            

    :type contentHandling: string
    :param contentHandling: Specifies how to handle request payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT , with the following behaviors:
            CONVERT_TO_BINARY : Converts a request payload from a Base64-encoded string to the corresponding binary blob.
            CONVERT_TO_TEXT : Converts a request payload from a binary blob to a Base64-encoded string.
            If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the passthroughBehaviors is configured to support payload pass-through.
            

    :type timeoutInMillis: integer
    :param timeoutInMillis: Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.

    :rtype: dict
    :return: {
        'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
        'httpMethod': 'string',
        'uri': 'string',
        'connectionType': 'INTERNET'|'VPC_LINK',
        'connectionId': 'string',
        'credentials': 'string',
        'requestParameters': {
            'string': 'string'
        },
        'requestTemplates': {
            'string': 'string'
        },
        'passthroughBehavior': 'string',
        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
        'timeoutInMillis': 123,
        'cacheNamespace': 'string',
        'cacheKeyParameters': [
            'string',
        ],
        'integrationResponses': {
            'string': {
                'statusCode': 'string',
                'selectionPattern': 'string',
                'responseParameters': {
                    'string': 'string'
                },
                'responseTemplates': {
                    'string': 'string'
                },
                'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
            }
        }
    }
    
    
    :returns: 
    AWS : for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
    AWS_PROXY : for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
    HTTP : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
    HTTP_PROXY : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
    MOCK : for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.
    
    """
    pass

def put_integration_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None, selectionPattern=None, responseParameters=None, responseTemplates=None, contentHandling=None):
    """
    Represents a put integration.
    See also: AWS API Documentation
    
    
    :example: response = client.put_integration_response(
        restApiId='string',
        resourceId='string',
        httpMethod='string',
        statusCode='string',
        selectionPattern='string',
        responseParameters={
            'string': 'string'
        },
        responseTemplates={
            'string': 'string'
        },
        contentHandling='CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] Specifies a put integration response request's resource identifier.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] Specifies a put integration response request's HTTP method.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            [Required] Specifies the status code that is used to map the integration response to an existing MethodResponse .
            

    :type selectionPattern: string
    :param selectionPattern: Specifies the selection pattern of a put integration response.

    :type responseParameters: dict
    :param responseParameters: A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name} , where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression} , where name must be a valid and unique response header name and JSON-expression a valid JSON expression without the $ prefix.
            (string) --
            (string) --
            

    :type responseTemplates: dict
    :param responseTemplates: Specifies a put integration response's templates.
            (string) --
            (string) --
            

    :type contentHandling: string
    :param contentHandling: Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT , with the following behaviors:
            CONVERT_TO_BINARY : Converts a response payload from a Base64-encoded string to the corresponding binary blob.
            CONVERT_TO_TEXT : Converts a response payload from a binary blob to a Base64-encoded string.
            If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.
            

    :rtype: dict
    :return: {
        'statusCode': 'string',
        'selectionPattern': 'string',
        'responseParameters': {
            'string': 'string'
        },
        'responseTemplates': {
            'string': 'string'
        },
        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def put_method(restApiId=None, resourceId=None, httpMethod=None, authorizationType=None, authorizerId=None, apiKeyRequired=None, operationName=None, requestParameters=None, requestModels=None, requestValidatorId=None, authorizationScopes=None):
    """
    Add a method to an existing  Resource resource.
    See also: AWS API Documentation
    
    
    :example: response = client.put_method(
        restApiId='string',
        resourceId='string',
        httpMethod='string',
        authorizationType='string',
        authorizerId='string',
        apiKeyRequired=True|False,
        operationName='string',
        requestParameters={
            'string': True|False
        },
        requestModels={
            'string': 'string'
        },
        requestValidatorId='string',
        authorizationScopes=[
            'string',
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] The Resource identifier for the new Method resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] Specifies the method request's HTTP method type.
            

    :type authorizationType: string
    :param authorizationType: [REQUIRED]
            [Required] The method's authorization type. Valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, CUSTOM for using a custom authorizer, or COGNITO_USER_POOLS for using a Cognito user pool.
            

    :type authorizerId: string
    :param authorizerId: Specifies the identifier of an Authorizer to use on this Method, if the type is CUSTOM or COGNITO_USER_POOLS. The authorizer identifier is generated by API Gateway when you created the authorizer.

    :type apiKeyRequired: boolean
    :param apiKeyRequired: Specifies whether the method required a valid ApiKey .

    :type operationName: string
    :param operationName: A human-friendly operation identifier for the method. For example, you can assign the operationName of ListPets for the GET /pets method in PetStore example.

    :type requestParameters: dict
    :param requestParameters: A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key defines a method request parameter name matching the pattern of method.request.{location}.{name} , where location is querystring , path , or header and name is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (true ) or optional (false ). The method request parameter names defined here are available in Integration to be mapped to integration request parameters or body-mapping templates.
            (string) --
            (boolean) --
            

    :type requestModels: dict
    :param requestModels: Specifies the Model resources used for the request's content type. Request models are represented as a key/value map, with a content type as the key and a Model name as the value.
            (string) --
            (string) --
            

    :type requestValidatorId: string
    :param requestValidatorId: The identifier of a RequestValidator for validating the method request.

    :type authorizationScopes: list
    :param authorizationScopes: A list of authorization scopes configured on the method. The scopes are used with a COGNITO_USER_POOLS authorizer to authorize the method invocation. The authorization works by matching the method scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any method scopes matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the method scope is configured, the client must provide an access token instead of an identity token for authorization purposes.
            (string) --
            

    :rtype: dict
    :return: {
        'httpMethod': 'string',
        'authorizationType': 'string',
        'authorizerId': 'string',
        'apiKeyRequired': True|False,
        'requestValidatorId': 'string',
        'operationName': 'string',
        'requestParameters': {
            'string': True|False
        },
        'requestModels': {
            'string': 'string'
        },
        'methodResponses': {
            'string': {
                'statusCode': 'string',
                'responseParameters': {
                    'string': True|False
                },
                'responseModels': {
                    'string': 'string'
                }
            }
        },
        'methodIntegration': {
            'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
            'httpMethod': 'string',
            'uri': 'string',
            'connectionType': 'INTERNET'|'VPC_LINK',
            'connectionId': 'string',
            'credentials': 'string',
            'requestParameters': {
                'string': 'string'
            },
            'requestTemplates': {
                'string': 'string'
            },
            'passthroughBehavior': 'string',
            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
            'timeoutInMillis': 123,
            'cacheNamespace': 'string',
            'cacheKeyParameters': [
                'string',
            ],
            'integrationResponses': {
                'string': {
                    'statusCode': 'string',
                    'selectionPattern': 'string',
                    'responseParameters': {
                        'string': 'string'
                    },
                    'responseTemplates': {
                        'string': 'string'
                    },
                    'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                }
            }
        },
        'authorizationScopes': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    (boolean) --
    
    
    
    """
    pass

def put_method_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None, responseParameters=None, responseModels=None):
    """
    Adds a  MethodResponse to an existing  Method resource.
    See also: AWS API Documentation
    
    
    :example: response = client.put_method_response(
        restApiId='string',
        resourceId='string',
        httpMethod='string',
        statusCode='string',
        responseParameters={
            'string': True|False
        },
        responseModels={
            'string': 'string'
        }
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] The Resource identifier for the Method resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] The HTTP verb of the Method resource.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            [Required] The method response's status code.
            

    :type responseParameters: dict
    :param responseParameters: A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header name and the associated value is a Boolean flag indicating whether the method response parameter is required or not. The method response header names must match the pattern of method.response.header.{name} , where name is a valid and unique header name. The response parameter names defined here are available in the integration response to be mapped from an integration response header expressed in integration.response.header.{name} , a static value enclosed within a pair of single quotes (e.g., 'application/json' ), or a JSON expression from the back-end response payload in the form of integration.response.body.{JSON-expression} , where JSON-expression is a valid JSON expression without the $ prefix.)
            (string) --
            (boolean) --
            

    :type responseModels: dict
    :param responseModels: Specifies the Model resources used for the response's content type. Response models are represented as a key/value map, with a content type as the key and a Model name as the value.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'statusCode': 'string',
        'responseParameters': {
            'string': True|False
        },
        'responseModels': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (boolean) --
    
    
    
    """
    pass

def put_rest_api(restApiId=None, mode=None, failOnWarnings=None, parameters=None, body=None):
    """
    A feature of the API Gateway control service for updating an existing API with an input of external API definitions. The update can take the form of merging the supplied definition into the existing API or overwriting the existing API.
    See also: AWS API Documentation
    
    
    :example: response = client.put_rest_api(
        restApiId='string',
        mode='merge'|'overwrite',
        failOnWarnings=True|False,
        parameters={
            'string': 'string'
        },
        body=b'bytes'|file
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type mode: string
    :param mode: The mode query parameter to specify the update mode. Valid values are 'merge' and 'overwrite'. By default, the update mode is 'merge'.

    :type failOnWarnings: boolean
    :param failOnWarnings: A query parameter to indicate whether to rollback the API update (true ) or not (false ) when a warning is encountered. The default value is false .

    :type parameters: dict
    :param parameters: Custom header parameters as part of the request. For example, to exclude DocumentationParts from an imported API, set ignore=documentation as a parameters value, as in the AWS CLI command of aws apigateway import-rest-api --parameters ignore=documentation --body 'file:///path/to/imported-api-body.json .
            (string) --
            (string) --
            

    :type body: bytes or seekable file-like object
    :param body: [REQUIRED]
            [Required] The PUT request body containing external API definitions. Currently, only Swagger definition JSON files are supported. The maximum size of the API definition file is 2MB.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'description': 'string',
        'createdDate': datetime(2015, 1, 1),
        'version': 'string',
        'warnings': [
            'string',
        ],
        'binaryMediaTypes': [
            'string',
        ],
        'minimumCompressionSize': 123,
        'apiKeySource': 'HEADER'|'AUTHORIZER',
        'endpointConfiguration': {
            'types': [
                'REGIONAL'|'EDGE',
            ]
        },
        'policy': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds or updates a tag on a given resource.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            [Required] The ARN of a resource that can be tagged. The resource ARN must be URL-encoded. At present, Stage is the only taggable resource.
            

    :type tags: dict
    :param tags: [REQUIRED]
            [Required] The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with aws: . The tag value can be up to 256 characters.
            (string) --
            (string) --
            

    """
    pass

def test_invoke_authorizer(restApiId=None, authorizerId=None, headers=None, pathWithQueryString=None, body=None, stageVariables=None, additionalContext=None):
    """
    Simulate the execution of an  Authorizer in your  RestApi with headers, parameters, and an incoming request body.
    See also: AWS API Documentation
    
    
    :example: response = client.test_invoke_authorizer(
        restApiId='string',
        authorizerId='string',
        headers={
            'string': 'string'
        },
        pathWithQueryString='string',
        body='string',
        stageVariables={
            'string': 'string'
        },
        additionalContext={
            'string': 'string'
        }
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type authorizerId: string
    :param authorizerId: [REQUIRED]
            [Required] Specifies a test invoke authorizer request's Authorizer ID.
            

    :type headers: dict
    :param headers: [Required] A key-value map of headers to simulate an incoming invocation request. This is where the incoming authorization token, or identity source, should be specified.
            (string) --
            (string) --
            

    :type pathWithQueryString: string
    :param pathWithQueryString: [Optional] The URI path, including query string, of the simulated invocation request. Use this to specify path parameters and query string parameters.

    :type body: string
    :param body: [Optional] The simulated request body of an incoming invocation request.

    :type stageVariables: dict
    :param stageVariables: A key-value map of stage variables to simulate an invocation on a deployed Stage .
            (string) --
            (string) --
            

    :type additionalContext: dict
    :param additionalContext: [Optional] A key-value map of additional context variables.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'clientStatus': 123,
        'log': 'string',
        'latency': 123,
        'principalId': 'string',
        'policy': 'string',
        'authorization': {
            'string': [
                'string',
            ]
        },
        'claims': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def test_invoke_method(restApiId=None, resourceId=None, httpMethod=None, pathWithQueryString=None, body=None, headers=None, clientCertificateId=None, stageVariables=None):
    """
    Simulate the execution of a  Method in your  RestApi with headers, parameters, and an incoming request body.
    See also: AWS API Documentation
    
    
    :example: response = client.test_invoke_method(
        restApiId='string',
        resourceId='string',
        httpMethod='string',
        pathWithQueryString='string',
        body='string',
        headers={
            'string': 'string'
        },
        clientCertificateId='string',
        stageVariables={
            'string': 'string'
        }
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] Specifies a test invoke method request's resource ID.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] Specifies a test invoke method request's HTTP method.
            

    :type pathWithQueryString: string
    :param pathWithQueryString: The URI path, including query string, of the simulated invocation request. Use this to specify path parameters and query string parameters.

    :type body: string
    :param body: The simulated request body of an incoming invocation request.

    :type headers: dict
    :param headers: A key-value map of headers to simulate an incoming invocation request.
            (string) --
            (string) --
            

    :type clientCertificateId: string
    :param clientCertificateId: A ClientCertificate identifier to use in the test invocation. API Gateway will use the certificate when making the HTTPS request to the defined back-end endpoint.

    :type stageVariables: dict
    :param stageVariables: A key-value map of stage variables to simulate an invocation on a deployed Stage .
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'status': 123,
        'body': 'string',
        'headers': {
            'string': 'string'
        },
        'log': 'string',
        'latency': 123
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes a tag from a given resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            [Required] The ARN of a resource that can be tagged. The resource ARN must be URL-encoded. At present, Stage is the only taggable resource.
            

    :type tagKeys: list
    :param tagKeys: [REQUIRED]
            [Required] The Tag keys to delete.
            (string) --
            

    """
    pass

def update_account(patchOperations=None):
    """
    Changes information about the current  Account resource.
    See also: AWS API Documentation
    
    
    :example: response = client.update_account(
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'cloudwatchRoleArn': 'string',
        'throttleSettings': {
            'burstLimit': 123,
            'rateLimit': 123.0
        },
        'features': [
            'string',
        ],
        'apiKeyVersion': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_api_key(apiKey=None, patchOperations=None):
    """
    Changes information about an  ApiKey resource.
    See also: AWS API Documentation
    
    
    :example: response = client.update_api_key(
        apiKey='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type apiKey: string
    :param apiKey: [REQUIRED]
            [Required] The identifier of the ApiKey resource to be updated.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'id': 'string',
        'value': 'string',
        'name': 'string',
        'customerId': 'string',
        'description': 'string',
        'enabled': True|False,
        'createdDate': datetime(2015, 1, 1),
        'lastUpdatedDate': datetime(2015, 1, 1),
        'stageKeys': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_authorizer(restApiId=None, authorizerId=None, patchOperations=None):
    """
    Updates an existing  Authorizer resource.
    See also: AWS API Documentation
    
    
    :example: response = client.update_authorizer(
        restApiId='string',
        authorizerId='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type authorizerId: string
    :param authorizerId: [REQUIRED]
            [Required] The identifier of the Authorizer resource.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'type': 'TOKEN'|'REQUEST'|'COGNITO_USER_POOLS',
        'providerARNs': [
            'string',
        ],
        'authType': 'string',
        'authorizerUri': 'string',
        'authorizerCredentials': 'string',
        'identitySource': 'string',
        'identityValidationExpression': 'string',
        'authorizerResultTtlInSeconds': 123
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_base_path_mapping(domainName=None, basePath=None, patchOperations=None):
    """
    Changes information about the  BasePathMapping resource.
    See also: AWS API Documentation
    
    
    :example: response = client.update_base_path_mapping(
        domainName='string',
        basePath='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            [Required] The domain name of the BasePathMapping resource to change.
            

    :type basePath: string
    :param basePath: [REQUIRED]
            [Required] The base path of the BasePathMapping resource to change.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'basePath': 'string',
        'restApiId': 'string',
        'stage': 'string'
    }
    
    
    """
    pass

def update_client_certificate(clientCertificateId=None, patchOperations=None):
    """
    Changes information about an  ClientCertificate resource.
    See also: AWS API Documentation
    
    
    :example: response = client.update_client_certificate(
        clientCertificateId='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type clientCertificateId: string
    :param clientCertificateId: [REQUIRED]
            [Required] The identifier of the ClientCertificate resource to be updated.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'clientCertificateId': 'string',
        'description': 'string',
        'pemEncodedCertificate': 'string',
        'createdDate': datetime(2015, 1, 1),
        'expirationDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def update_deployment(restApiId=None, deploymentId=None, patchOperations=None):
    """
    Changes information about a  Deployment resource.
    See also: AWS API Documentation
    
    
    :example: response = client.update_deployment(
        restApiId='string',
        deploymentId='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type deploymentId: string
    :param deploymentId: [REQUIRED]
            The replacement identifier for the Deployment resource to change information about.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'id': 'string',
        'description': 'string',
        'createdDate': datetime(2015, 1, 1),
        'apiSummary': {
            'string': {
                'string': {
                    'authorizationType': 'string',
                    'apiKeyRequired': True|False
                }
            }
        }
    }
    
    
    """
    pass

def update_documentation_part(restApiId=None, documentationPartId=None, patchOperations=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.update_documentation_part(
        restApiId='string',
        documentationPartId='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type documentationPartId: string
    :param documentationPartId: [REQUIRED]
            [Required] The identifier of the to-be-updated documentation part.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'id': 'string',
        'location': {
            'type': 'API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'|'PATH_PARAMETER'|'QUERY_PARAMETER'|'REQUEST_HEADER'|'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'|'RESPONSE_BODY',
            'path': 'string',
            'method': 'string',
            'statusCode': 'string',
            'name': 'string'
        },
        'properties': 'string'
    }
    
    
    """
    pass

def update_documentation_version(restApiId=None, documentationVersion=None, patchOperations=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.update_documentation_version(
        restApiId='string',
        documentationVersion='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi ..
            

    :type documentationVersion: string
    :param documentationVersion: [REQUIRED]
            [Required] The version identifier of the to-be-updated documentation version.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'version': 'string',
        'createdDate': datetime(2015, 1, 1),
        'description': 'string'
    }
    
    
    """
    pass

def update_domain_name(domainName=None, patchOperations=None):
    """
    Changes information about the  DomainName resource.
    See also: AWS API Documentation
    
    
    :example: response = client.update_domain_name(
        domainName='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            [Required] The name of the DomainName resource to be changed.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'domainName': 'string',
        'certificateName': 'string',
        'certificateArn': 'string',
        'certificateUploadDate': datetime(2015, 1, 1),
        'regionalDomainName': 'string',
        'regionalHostedZoneId': 'string',
        'regionalCertificateName': 'string',
        'regionalCertificateArn': 'string',
        'distributionDomainName': 'string',
        'distributionHostedZoneId': 'string',
        'endpointConfiguration': {
            'types': [
                'REGIONAL'|'EDGE',
            ]
        }
    }
    
    
    """
    pass

def update_gateway_response(restApiId=None, responseType=None, patchOperations=None):
    """
    Updates a  GatewayResponse of a specified response type on the given  RestApi .
    See also: AWS API Documentation
    
    
    :example: response = client.update_gateway_response(
        restApiId='string',
        responseType='DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type responseType: string
    :param responseType: [REQUIRED]
            [Required]
            The response type of the associated GatewayResponse . Valid values are
            ACCESS_DENIED
            API_CONFIGURATION_ERROR
            AUTHORIZER_FAILURE
            AUTHORIZER_CONFIGURATION_ERROR
            BAD_REQUEST_PARAMETERS
            BAD_REQUEST_BODY
            DEFAULT_4XX
            DEFAULT_5XX
            EXPIRED_TOKEN
            INVALID_SIGNATURE
            INTEGRATION_FAILURE
            INTEGRATION_TIMEOUT
            INVALID_API_KEY
            MISSING_AUTHENTICATION_TOKEN
            QUOTA_EXCEEDED
            REQUEST_TOO_LARGE
            RESOURCE_NOT_FOUND
            THROTTLED
            UNAUTHORIZED
            UNSUPPORTED_MEDIA_TYPE
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'responseType': 'DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'|'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'|'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'|'INVALID_SIGNATURE'|'EXPIRED_TOKEN'|'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'|'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'|'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'|'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'|'QUOTA_EXCEEDED',
        'statusCode': 'string',
        'responseParameters': {
            'string': 'string'
        },
        'responseTemplates': {
            'string': 'string'
        },
        'defaultResponse': True|False
    }
    
    
    :returns: 
    ACCESS_DENIED
    API_CONFIGURATION_ERROR
    AUTHORIZER_FAILURE
    AUTHORIZER_CONFIGURATION_ERROR
    BAD_REQUEST_PARAMETERS
    BAD_REQUEST_BODY
    DEFAULT_4XX
    DEFAULT_5XX
    EXPIRED_TOKEN
    INVALID_SIGNATURE
    INTEGRATION_FAILURE
    INTEGRATION_TIMEOUT
    INVALID_API_KEY
    MISSING_AUTHENTICATION_TOKEN
    QUOTA_EXCEEDED
    REQUEST_TOO_LARGE
    RESOURCE_NOT_FOUND
    THROTTLED
    UNAUTHORIZED
    UNSUPPORTED_MEDIA_TYPE
    
    """
    pass

def update_integration(restApiId=None, resourceId=None, httpMethod=None, patchOperations=None):
    """
    Represents an update integration.
    See also: AWS API Documentation
    
    
    :example: response = client.update_integration(
        restApiId='string',
        resourceId='string',
        httpMethod='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] Represents an update integration request's resource identifier.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] Represents an update integration request's HTTP method.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
        'httpMethod': 'string',
        'uri': 'string',
        'connectionType': 'INTERNET'|'VPC_LINK',
        'connectionId': 'string',
        'credentials': 'string',
        'requestParameters': {
            'string': 'string'
        },
        'requestTemplates': {
            'string': 'string'
        },
        'passthroughBehavior': 'string',
        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
        'timeoutInMillis': 123,
        'cacheNamespace': 'string',
        'cacheKeyParameters': [
            'string',
        ],
        'integrationResponses': {
            'string': {
                'statusCode': 'string',
                'selectionPattern': 'string',
                'responseParameters': {
                    'string': 'string'
                },
                'responseTemplates': {
                    'string': 'string'
                },
                'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
            }
        }
    }
    
    
    :returns: 
    AWS : for integrating the API method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration.
    AWS_PROXY : for integrating the API method request with the Lambda function-invoking action with the client request passed through as-is. This integration is also referred to as the Lambda proxy integration.
    HTTP : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC. This integration is also referred to as the HTTP custom integration.
    HTTP_PROXY : for integrating the API method request with an HTTP endpoint, including a private HTTP endpoint within a VPC, with the client request passed through as-is. This is also referred to as the HTTP proxy integration.
    MOCK : for integrating the API method request with API Gateway as a "loop-back" endpoint without invoking any backend.
    
    """
    pass

def update_integration_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None, patchOperations=None):
    """
    Represents an update integration response.
    See also: AWS API Documentation
    
    
    :example: response = client.update_integration_response(
        restApiId='string',
        resourceId='string',
        httpMethod='string',
        statusCode='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] Specifies an update integration response request's resource identifier.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] Specifies an update integration response request's HTTP method.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            [Required] Specifies an update integration response request's status code.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'statusCode': 'string',
        'selectionPattern': 'string',
        'responseParameters': {
            'string': 'string'
        },
        'responseTemplates': {
            'string': 'string'
        },
        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_method(restApiId=None, resourceId=None, httpMethod=None, patchOperations=None):
    """
    Updates an existing  Method resource.
    See also: AWS API Documentation
    
    
    :example: response = client.update_method(
        restApiId='string',
        resourceId='string',
        httpMethod='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] The Resource identifier for the Method resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] The HTTP verb of the Method resource.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'httpMethod': 'string',
        'authorizationType': 'string',
        'authorizerId': 'string',
        'apiKeyRequired': True|False,
        'requestValidatorId': 'string',
        'operationName': 'string',
        'requestParameters': {
            'string': True|False
        },
        'requestModels': {
            'string': 'string'
        },
        'methodResponses': {
            'string': {
                'statusCode': 'string',
                'responseParameters': {
                    'string': True|False
                },
                'responseModels': {
                    'string': 'string'
                }
            }
        },
        'methodIntegration': {
            'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
            'httpMethod': 'string',
            'uri': 'string',
            'connectionType': 'INTERNET'|'VPC_LINK',
            'connectionId': 'string',
            'credentials': 'string',
            'requestParameters': {
                'string': 'string'
            },
            'requestTemplates': {
                'string': 'string'
            },
            'passthroughBehavior': 'string',
            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
            'timeoutInMillis': 123,
            'cacheNamespace': 'string',
            'cacheKeyParameters': [
                'string',
            ],
            'integrationResponses': {
                'string': {
                    'statusCode': 'string',
                    'selectionPattern': 'string',
                    'responseParameters': {
                        'string': 'string'
                    },
                    'responseTemplates': {
                        'string': 'string'
                    },
                    'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                }
            }
        },
        'authorizationScopes': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    (boolean) --
    
    
    
    """
    pass

def update_method_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None, patchOperations=None):
    """
    Updates an existing  MethodResponse resource.
    See also: AWS API Documentation
    
    
    :example: response = client.update_method_response(
        restApiId='string',
        resourceId='string',
        httpMethod='string',
        statusCode='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] The Resource identifier for the MethodResponse resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            [Required] The HTTP verb of the Method resource.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            [Required] The status code for the MethodResponse resource.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'statusCode': 'string',
        'responseParameters': {
            'string': True|False
        },
        'responseModels': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (boolean) --
    
    
    
    """
    pass

def update_model(restApiId=None, modelName=None, patchOperations=None):
    """
    Changes information about a model.
    See also: AWS API Documentation
    
    
    :example: response = client.update_model(
        restApiId='string',
        modelName='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type modelName: string
    :param modelName: [REQUIRED]
            [Required] The name of the model to update.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'description': 'string',
        'schema': 'string',
        'contentType': 'string'
    }
    
    
    """
    pass

def update_request_validator(restApiId=None, requestValidatorId=None, patchOperations=None):
    """
    Updates a  RequestValidator of a given  RestApi .
    See also: AWS API Documentation
    
    
    :example: response = client.update_request_validator(
        restApiId='string',
        requestValidatorId='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type requestValidatorId: string
    :param requestValidatorId: [REQUIRED]
            [Required] The identifier of RequestValidator to be updated.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'validateRequestBody': True|False,
        'validateRequestParameters': True|False
    }
    
    
    """
    pass

def update_resource(restApiId=None, resourceId=None, patchOperations=None):
    """
    Changes information about a  Resource resource.
    See also: AWS API Documentation
    
    
    :example: response = client.update_resource(
        restApiId='string',
        resourceId='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            [Required] The identifier of the Resource resource.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'id': 'string',
        'parentId': 'string',
        'pathPart': 'string',
        'path': 'string',
        'resourceMethods': {
            'string': {
                'httpMethod': 'string',
                'authorizationType': 'string',
                'authorizerId': 'string',
                'apiKeyRequired': True|False,
                'requestValidatorId': 'string',
                'operationName': 'string',
                'requestParameters': {
                    'string': True|False
                },
                'requestModels': {
                    'string': 'string'
                },
                'methodResponses': {
                    'string': {
                        'statusCode': 'string',
                        'responseParameters': {
                            'string': True|False
                        },
                        'responseModels': {
                            'string': 'string'
                        }
                    }
                },
                'methodIntegration': {
                    'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                    'httpMethod': 'string',
                    'uri': 'string',
                    'connectionType': 'INTERNET'|'VPC_LINK',
                    'connectionId': 'string',
                    'credentials': 'string',
                    'requestParameters': {
                        'string': 'string'
                    },
                    'requestTemplates': {
                        'string': 'string'
                    },
                    'passthroughBehavior': 'string',
                    'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                    'timeoutInMillis': 123,
                    'cacheNamespace': 'string',
                    'cacheKeyParameters': [
                        'string',
                    ],
                    'integrationResponses': {
                        'string': {
                            'statusCode': 'string',
                            'selectionPattern': 'string',
                            'responseParameters': {
                                'string': 'string'
                            },
                            'responseTemplates': {
                                'string': 'string'
                            },
                            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                        }
                    }
                },
                'authorizationScopes': [
                    'string',
                ]
            }
        }
    }
    
    
    :returns: 
    (string) --
    (boolean) --
    
    
    
    """
    pass

def update_rest_api(restApiId=None, patchOperations=None):
    """
    Changes information about the specified API.
    See also: AWS API Documentation
    
    
    :example: response = client.update_rest_api(
        restApiId='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'description': 'string',
        'createdDate': datetime(2015, 1, 1),
        'version': 'string',
        'warnings': [
            'string',
        ],
        'binaryMediaTypes': [
            'string',
        ],
        'minimumCompressionSize': 123,
        'apiKeySource': 'HEADER'|'AUTHORIZER',
        'endpointConfiguration': {
            'types': [
                'REGIONAL'|'EDGE',
            ]
        },
        'policy': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_stage(restApiId=None, stageName=None, patchOperations=None):
    """
    Changes information about a  Stage resource.
    See also: AWS API Documentation
    
    
    :example: response = client.update_stage(
        restApiId='string',
        stageName='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The string identifier of the associated RestApi .
            

    :type stageName: string
    :param stageName: [REQUIRED]
            [Required] The name of the Stage resource to change information about.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'deploymentId': 'string',
        'clientCertificateId': 'string',
        'stageName': 'string',
        'description': 'string',
        'cacheClusterEnabled': True|False,
        'cacheClusterSize': '0.5'|'1.6'|'6.1'|'13.5'|'28.4'|'58.2'|'118'|'237',
        'cacheClusterStatus': 'CREATE_IN_PROGRESS'|'AVAILABLE'|'DELETE_IN_PROGRESS'|'NOT_AVAILABLE'|'FLUSH_IN_PROGRESS',
        'methodSettings': {
            'string': {
                'metricsEnabled': True|False,
                'loggingLevel': 'string',
                'dataTraceEnabled': True|False,
                'throttlingBurstLimit': 123,
                'throttlingRateLimit': 123.0,
                'cachingEnabled': True|False,
                'cacheTtlInSeconds': 123,
                'cacheDataEncrypted': True|False,
                'requireAuthorizationForCacheControl': True|False,
                'unauthorizedCacheControlHeaderStrategy': 'FAIL_WITH_403'|'SUCCEED_WITH_RESPONSE_HEADER'|'SUCCEED_WITHOUT_RESPONSE_HEADER'
            }
        },
        'variables': {
            'string': 'string'
        },
        'documentationVersion': 'string',
        'accessLogSettings': {
            'format': 'string',
            'destinationArn': 'string'
        },
        'canarySettings': {
            'percentTraffic': 123.0,
            'deploymentId': 'string',
            'stageVariableOverrides': {
                'string': 'string'
            },
            'useStageCache': True|False
        },
        'tags': {
            'string': 'string'
        },
        'createdDate': datetime(2015, 1, 1),
        'lastUpdatedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_usage(usagePlanId=None, keyId=None, patchOperations=None):
    """
    Grants a temporary extension to the remaining quota of a usage plan associated with a specified API key.
    See also: AWS API Documentation
    
    
    :example: response = client.update_usage(
        usagePlanId='string',
        keyId='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type usagePlanId: string
    :param usagePlanId: [REQUIRED]
            [Required] The Id of the usage plan associated with the usage data.
            

    :type keyId: string
    :param keyId: [REQUIRED]
            [Required] The identifier of the API key associated with the usage plan in which a temporary extension is granted to the remaining quota.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'usagePlanId': 'string',
        'startDate': 'string',
        'endDate': 'string',
        'position': 'string',
        'items': {
            'string': [
                [
                    123,
                ],
            ]
        }
    }
    
    
    :returns: 
    (string) --
    (list) --
    (list) --
    (integer) --
    
    
    
    
    
    
    
    """
    pass

def update_usage_plan(usagePlanId=None, patchOperations=None):
    """
    Updates a usage plan of a given plan Id.
    See also: AWS API Documentation
    
    
    :example: response = client.update_usage_plan(
        usagePlanId='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type usagePlanId: string
    :param usagePlanId: [REQUIRED]
            [Required] The Id of the to-be-updated usage plan.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'description': 'string',
        'apiStages': [
            {
                'apiId': 'string',
                'stage': 'string'
            },
        ],
        'throttle': {
            'burstLimit': 123,
            'rateLimit': 123.0
        },
        'quota': {
            'limit': 123,
            'offset': 123,
            'period': 'DAY'|'WEEK'|'MONTH'
        },
        'productCode': 'string'
    }
    
    
    """
    pass

def update_vpc_link(vpcLinkId=None, patchOperations=None):
    """
    Updates an existing  VpcLink of a specified identifier.
    See also: AWS API Documentation
    
    
    :example: response = client.update_vpc_link(
        vpcLinkId='string',
        patchOperations=[
            {
                'op': 'add'|'remove'|'replace'|'move'|'copy'|'test',
                'path': 'string',
                'value': 'string',
                'from': 'string'
            },
        ]
    )
    
    
    :type vpcLinkId: string
    :param vpcLinkId: [REQUIRED]
            [Required] The identifier of the VpcLink . It is used in an Integration to reference this VpcLink .
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be add , remove , replace or copy . Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --The copy update operation's source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with 'op':'copy' , 'from':'/canarySettings/deploymentId' and 'path':'/deploymentId' .
            
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'description': 'string',
        'targetArns': [
            'string',
        ],
        'status': 'AVAILABLE'|'PENDING'|'DELETING'|'FAILED',
        'statusMessage': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

