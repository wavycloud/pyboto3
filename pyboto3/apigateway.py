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
            restApiId (string) --A list of Stage resources that are associated with the ApiKey resource.
            stageName (string) --The stage name in the RestApi that the stage key references.
            
            

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
        type='TOKEN'|'COGNITO_USER_POOLS',
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
            The RestApi identifier under which the Authorizer will be created.
            

    :type name: string
    :param name: [REQUIRED]
            [Required] The name of the authorizer.
            

    :type type: string
    :param type: [REQUIRED]
            [Required] The type of the authorizer.
            

    :type providerARNs: list
    :param providerARNs: A list of the Cognito Your User Pool authorizer's provider ARNs.
            (string) --
            

    :type authType: string
    :param authType: Optional customer-defined field, used in Swagger imports/exports. Has no functional impact.

    :type authorizerUri: string
    :param authorizerUri: [Required] Specifies the authorizer's Uniform Resource Identifier (URI).

    :type authorizerCredentials: string
    :param authorizerCredentials: Specifies the credentials required for the authorizer, if any.

    :type identitySource: string
    :param identitySource: [REQUIRED]
            [Required] The source of the identity in an incoming request.
            

    :type identityValidationExpression: string
    :param identityValidationExpression: A validation expression for the incoming identity.

    :type authorizerResultTtlInSeconds: integer
    :param authorizerResultTtlInSeconds: The TTL of cached authorizer results.

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'type': 'TOKEN'|'COGNITO_USER_POOLS',
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
            The domain name of the BasePathMapping resource to create.
            

    :type basePath: string
    :param basePath: The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Leave this blank if you do not want callers to specify a base path name after the domain name.

    :type restApiId: string
    :param restApiId: [REQUIRED]
            The name of the API that you want to apply this mapping to.
            

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

def create_deployment(restApiId=None, stageName=None, stageDescription=None, description=None, cacheClusterEnabled=None, cacheClusterSize=None, variables=None):
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
        }
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            The RestApi resource identifier for the Deployment resource to create.
            

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
            [Required] The identifier of an API of the to-be-created documentation part.
            

    :type location: dict
    :param location: [REQUIRED]
            [Required] The location of the targeted API entity of the to-be-created documentation part.
            type (string) -- [REQUIRED]The type of API entity to which the documentation content applies. It is a valid and required field for API entity types of API , AUTHORIZER , MODEL , RESOURCE , METHOD , PATH_PARAMETER , QUERY_PARAMETER , REQUEST_HEADER , REQUEST_BODY , RESPONSE , RESPONSE_HEADER , and RESPONSE_BODY . Content inheritance does not apply to any entity of the API , AUTHROZER , METHOD , MODEL , REQUEST_BODY , or RESOURCE type.
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
            [Required] Specifies the API identifier of the to-be-created documentation version.
            

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

def create_domain_name(domainName=None, certificateName=None, certificateBody=None, certificatePrivateKey=None, certificateChain=None, certificateArn=None):
    """
    Creates a new domain name.
    See also: AWS API Documentation
    
    
    :example: response = client.create_domain_name(
        domainName='string',
        certificateName='string',
        certificateBody='string',
        certificatePrivateKey='string',
        certificateChain='string',
        certificateArn='string'
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            (Required) The name of the DomainName resource.
            

    :type certificateName: string
    :param certificateName: The user-friendly name of the certificate.

    :type certificateBody: string
    :param certificateBody: [Deprecated] The body of the server certificate provided by your certificate authority.

    :type certificatePrivateKey: string
    :param certificatePrivateKey: [Deprecated] Your certificate's private key.

    :type certificateChain: string
    :param certificateChain: [Deprecated] The intermediate certificates and optionally the root certificate, one after the other without any blank lines. If you include the root certificate, your certificate chain must start with intermediate certificates and end with the root certificate. Use the intermediate certificates that were provided by your certificate authority. Do not include any intermediaries that are not in the chain of trust path.

    :type certificateArn: string
    :param certificateArn: The reference to an AWS-managed certificate. AWS Certificate Manager is the only supported source.

    :rtype: dict
    :return: {
        'domainName': 'string',
        'certificateName': 'string',
        'certificateArn': 'string',
        'certificateUploadDate': datetime(2015, 1, 1),
        'distributionDomainName': 'string'
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
            The RestApi identifier under which the Model will be created.
            

    :type name: string
    :param name: [REQUIRED]
            The name of the model.
            

    :type description: string
    :param description: The description of the model.

    :type schema: string
    :param schema: The schema for the model. For application/json models, this should be JSON-schema draft v4 model.

    :type contentType: string
    :param contentType: [REQUIRED]
            The content-type for the model.
            

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
            [Required] The identifier of the RestApi for which the RequestValidator is created.
            

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
            The identifier of the RestApi for the resource.
            

    :type parentId: string
    :param parentId: [REQUIRED]
            The parent resource's identifier.
            

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
                    'credentials': 'string',
                    'requestParameters': {
                        'string': 'string'
                    },
                    'requestTemplates': {
                        'string': 'string'
                    },
                    'passthroughBehavior': 'string',
                    'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
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
            }
        }
    }
    
    
    :returns: 
    (string) --
    (boolean) --
    
    
    
    """
    pass

def create_rest_api(name=None, description=None, version=None, cloneFrom=None, binaryMediaTypes=None):
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
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the RestApi .
            

    :type description: string
    :param description: The description of the RestApi .

    :type version: string
    :param version: A version identifier for the API.

    :type cloneFrom: string
    :param cloneFrom: The ID of the RestApi that you want to clone from.

    :type binaryMediaTypes: list
    :param binaryMediaTypes: The list of binary media types supported by the RestApi . By default, the RestApi supports only UTF-8-encoded text payloads.
            (string) --
            

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
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_stage(restApiId=None, stageName=None, deploymentId=None, description=None, cacheClusterEnabled=None, cacheClusterSize=None, variables=None, documentationVersion=None):
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
        documentationVersion='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            The identifier of the RestApi resource for the Stage resource to create.
            

    :type stageName: string
    :param stageName: [REQUIRED]
            The name for the Stage resource.
            

    :type deploymentId: string
    :param deploymentId: [REQUIRED]
            The identifier of the Deployment resource for the Stage resource.
            

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
            The name of the usage plan.
            

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
            The Id of the UsagePlan resource representing the usage plan containing the to-be-created UsagePlanKey resource representing a plan customer.
            

    :type keyId: string
    :param keyId: [REQUIRED]
            The identifier of a UsagePlanKey resource for a plan customer.
            

    :type keyType: string
    :param keyType: [REQUIRED]
            The type of a UsagePlanKey resource for a plan customer.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'type': 'string',
        'value': 'string',
        'name': 'string'
    }
    
    
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
            The identifier of the ApiKey resource to be deleted.
            

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
            The RestApi identifier for the Authorizer resource.
            

    :type authorizerId: string
    :param authorizerId: [REQUIRED]
            The identifier of the Authorizer resource.
            

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
            The domain name of the BasePathMapping resource to delete.
            

    :type basePath: string
    :param basePath: [REQUIRED]
            The base path name of the BasePathMapping resource to delete.
            

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
            The identifier of the ClientCertificate resource to be deleted.
            

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
            The identifier of the RestApi resource for the Deployment resource to delete.
            

    :type deploymentId: string
    :param deploymentId: [REQUIRED]
            The identifier of the Deployment resource to delete.
            

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
            [Required] Specifies the identifier of an API of the to-be-deleted documentation part.
            

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
            [Required] The identifier of an API of a to-be-deleted documentation snapshot.
            

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
            The name of the DomainName resource to be deleted.
            

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
            Specifies a delete integration request's API identifier.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            Specifies a delete integration request's resource identifier.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            Specifies a delete integration request's HTTP method.
            

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
            Specifies a delete integration response request's API identifier.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            Specifies a delete integration response request's resource identifier.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            Specifies a delete integration response request's HTTP method.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            Specifies a delete integration response request's status code.
            

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
            The RestApi identifier for the Method resource.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the Method resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            The HTTP verb of the Method resource.
            

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
            The RestApi identifier for the MethodResponse resource.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the MethodResponse resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            The HTTP verb of the Method resource.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            The status code identifier for the MethodResponse resource.
            

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
            The RestApi under which the model will be deleted.
            

    :type modelName: string
    :param modelName: [REQUIRED]
            The name of the model to delete.
            

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
            [Required] The identifier of the RestApi from which the given RequestValidator is deleted.
            

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
            The RestApi identifier for the Resource resource.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            The identifier of the Resource resource.
            

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
            The ID of the RestApi you want to delete.
            

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
            The identifier of the RestApi resource for the Stage resource to delete.
            

    :type stageName: string
    :param stageName: [REQUIRED]
            The name of the Stage resource to delete.
            

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
            The Id of the to-be-deleted usage plan.
            

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
            The Id of the UsagePlan resource representing the usage plan containing the to-be-deleted UsagePlanKey resource representing a plan customer.
            

    :type keyId: string
    :param keyId: [REQUIRED]
            The Id of the UsagePlanKey resource to be deleted.
            

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
            The API identifier of the stage to flush.
            

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
            The API identifier of the stage to flush its cache.
            

    :type stageName: string
    :param stageName: [REQUIRED]
            The name of the stage to flush its cache.
            

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
            The identifier of the ApiKey resource.
            

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
    :param limit: The maximum number of ApiKeys to get information about.

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
            The RestApi identifier for the Authorizer resource.
            

    :type authorizerId: string
    :param authorizerId: [REQUIRED]
            The identifier of the Authorizer resource.
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'type': 'TOKEN'|'COGNITO_USER_POOLS',
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
            The RestApi identifier for the Authorizers resource.
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'id': 'string',
                'name': 'string',
                'type': 'TOKEN'|'COGNITO_USER_POOLS',
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
            The domain name of the BasePathMapping resource to be described.
            

    :type basePath: string
    :param basePath: [REQUIRED]
            The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Leave this blank if you do not want callers to specify any base path name after the domain name.
            

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
            The domain name of a BasePathMapping resource.
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The value is 25 by default and could be between 1 - 500.

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
            The identifier of the ClientCertificate resource to be described.
            

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
    :param limit: The maximum number of returned results per page. The value is 25 by default and could be between 1 - 500.

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
            The identifier of the RestApi resource for the Deployment resource to get information about.
            

    :type deploymentId: string
    :param deploymentId: [REQUIRED]
            The identifier of the Deployment resource to get information about.
            

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
            The identifier of the RestApi resource for the collection of Deployment resources to get information about.
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The value is 25 by default and could be between 1 - 500.

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
            [Required] The identifier of an API of the to-be-retrieved documentation part.
            

    :type documentationPartId: string
    :param documentationPartId: [REQUIRED]
            [Required] The identifier of the to-be-retrieved documentation part.
            

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

def get_documentation_parts(restApiId=None, type=None, nameQuery=None, path=None, position=None, limit=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.get_documentation_parts(
        restApiId='string',
        type='API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'|'PATH_PARAMETER'|'QUERY_PARAMETER'|'REQUEST_HEADER'|'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'|'RESPONSE_BODY',
        nameQuery='string',
        path='string',
        position='string',
        limit=123
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            [Required] The identifier of the API of the to-be-retrieved documentation parts.
            

    :type type: string
    :param type: The type of API entities of the to-be-retrieved documentation parts.

    :type nameQuery: string
    :param nameQuery: The name of API entities of the to-be-retrieved documentation parts.

    :type path: string
    :param path: The path of API entities of the to-be-retrieved documentation parts.

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page.

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
            [Required] The identifier of the API of the to-be-retrieved documentation snapshot.
            

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
            [Required] The identifier of an API of the to-be-retrieved documentation versions.
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page.

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
            The name of the DomainName resource.
            

    :rtype: dict
    :return: {
        'domainName': 'string',
        'certificateName': 'string',
        'certificateArn': 'string',
        'certificateUploadDate': datetime(2015, 1, 1),
        'distributionDomainName': 'string'
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
    :param limit: The maximum number of returned results per page. The value is 25 by default and could be between 1 - 500.

    :rtype: dict
    :return: {
        'position': 'string',
        'items': [
            {
                'domainName': 'string',
                'certificateName': 'string',
                'certificateArn': 'string',
                'certificateUploadDate': datetime(2015, 1, 1),
                'distributionDomainName': 'string'
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
            The identifier of the RestApi to be exported.
            

    :type stageName: string
    :param stageName: [REQUIRED]
            The name of the Stage that will be exported.
            

    :type exportType: string
    :param exportType: [REQUIRED]
            The type of export. Currently only 'swagger' is supported.
            

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

def get_integration(restApiId=None, resourceId=None, httpMethod=None):
    """
    Represents a get integration.
    See also: AWS API Documentation
    
    
    :example: response = client.get_integration(
        restApiId='string',
        resourceId='string',
        httpMethod='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            Specifies a get integration request's API identifier.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            Specifies a get integration request's resource identifier
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            Specifies a get integration request's HTTP method.
            

    :rtype: dict
    :return: {
        'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
        'httpMethod': 'string',
        'uri': 'string',
        'credentials': 'string',
        'requestParameters': {
            'string': 'string'
        },
        'requestTemplates': {
            'string': 'string'
        },
        'passthroughBehavior': 'string',
        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
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
    (string) --
    (string) --
    
    
    
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
            Specifies a get integration response request's API identifier.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            Specifies a get integration response request's resource identifier.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            Specifies a get integration response request's HTTP method.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            Specifies a get integration response request's status code.
            

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
            The RestApi identifier for the Method resource.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the Method resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            Specifies the method request's HTTP method type.
            

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
            'credentials': 'string',
            'requestParameters': {
                'string': 'string'
            },
            'requestTemplates': {
                'string': 'string'
            },
            'passthroughBehavior': 'string',
            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
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
            The RestApi identifier for the MethodResponse resource.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the MethodResponse resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            The HTTP verb of the Method resource.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            The status code for the MethodResponse resource.
            

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
            The RestApi identifier under which the Model exists.
            

    :type modelName: string
    :param modelName: [REQUIRED]
            The name of the model as an identifier.
            

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
            The ID of the RestApi under which the model exists.
            

    :type modelName: string
    :param modelName: [REQUIRED]
            The name of the model for which to generate a template.
            

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
            The RestApi identifier.
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The value is 25 by default and could be between 1 - 500.

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
            [Required] The identifier of the RestApi to which the specified RequestValidator belongs.
            

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
            [Required] The identifier of a RestApi to which the RequestValidators collection belongs.
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page.

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
            The RestApi identifier for the resource.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            The identifier for the Resource resource.
            

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
                    'credentials': 'string',
                    'requestParameters': {
                        'string': 'string'
                    },
                    'requestTemplates': {
                        'string': 'string'
                    },
                    'passthroughBehavior': 'string',
                    'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
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
            The RestApi identifier for the Resource.
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page. The value is 25 by default and could be between 1 - 500.

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
                            'credentials': 'string',
                            'requestParameters': {
                                'string': 'string'
                            },
                            'requestTemplates': {
                                'string': 'string'
                            },
                            'passthroughBehavior': 'string',
                            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
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
            The identifier of the RestApi resource.
            

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
        ]
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
    :param limit: The maximum number of returned results per page. The value is 25 by default and could be between 1 - 500.

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
                ]
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
            The identifier of the RestApi that the SDK will use.
            

    :type stageName: string
    :param stageName: [REQUIRED]
            The name of the Stage that the SDK will use.
            

    :type sdkType: string
    :param sdkType: [REQUIRED]
            The language for the generated SDK. Currently javascript , android , and objectivec (for iOS) are supported.
            

    :type parameters: dict
    :param parameters: A key-value map of query string parameters that specify properties of the SDK, depending on the requested sdkType . For sdkType of objectivec , a parameter named classPrefix is required. For sdkType of android , parameters named groupId , artifactId , artifactVersion , and invokerPackage are required.
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
            The identifier of the queried SdkType instance.
            

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
    :param limit: The maximum number of returned results per page.

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
            The identifier of the RestApi resource for the Stage resource to get information about.
            

    :type stageName: string
    :param stageName: [REQUIRED]
            The name of the Stage resource to get information about.
            

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
            The stages' API identifiers.
            

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
            The Id of the usage plan associated with the usage data.
            

    :type keyId: string
    :param keyId: The Id of the API key associated with the resultant usage data.

    :type startDate: string
    :param startDate: [REQUIRED]
            The starting date (e.g., 2016-01-01) of the usage data.
            

    :type endDate: string
    :param endDate: [REQUIRED]
            The ending date (e.g., 2016-12-31) of the usage data.
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page.

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
            The identifier of the UsagePlan resource to be retrieved.
            

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
            The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.
            

    :type keyId: string
    :param keyId: [REQUIRED]
            The key Id of the to-be-retrieved UsagePlanKey resource representing a plan customer.
            

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
            The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.
            

    :type position: string
    :param position: The current pagination position in the paged result set.

    :type limit: integer
    :param limit: The maximum number of returned results per page.

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
    :param limit: The maximum number of returned results per page.

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
            [Required] The identifier of an API of the to-be-imported documentation parts.
            

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
    A feature of the Amazon API Gateway control service for creating a new API from an external API definition file.
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
    :param parameters: Custom header parameters as part of the request.
            (string) --
            (string) --
            

    :type body: bytes or seekable file-like object
    :param body: [REQUIRED]
            The POST request body containing external API definitions. Currently, only Swagger definition JSON files are supported.
            

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
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_integration(restApiId=None, resourceId=None, httpMethod=None, type=None, integrationHttpMethod=None, uri=None, credentials=None, requestParameters=None, requestTemplates=None, passthroughBehavior=None, cacheNamespace=None, cacheKeyParameters=None, contentHandling=None):
    """
    Represents a put integration.
    See also: AWS API Documentation
    
    
    :example: response = client.put_integration(
        restApiId='string',
        resourceId='string',
        httpMethod='string',
        type='HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
        integrationHttpMethod='string',
        uri='string',
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
        contentHandling='CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            Specifies a put integration request's API identifier.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            Specifies a put integration request's resource ID.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            Specifies a put integration request's HTTP method.
            

    :type type: string
    :param type: [REQUIRED]
            Specifies a put integration input's type.
            

    :type integrationHttpMethod: string
    :param integrationHttpMethod: Specifies a put integration HTTP method. When the integration type is HTTP or AWS, this field is required.

    :type uri: string
    :param uri: Specifies a put integration input's Uniform Resource Identifier (URI). When the integration type is HTTP or AWS, this field is required. For integration with Lambda as an AWS service proxy, this value is of the 'arn:aws:apigateway:region:lambda:path/2015-03-31/functions/functionArn/invocations' format.

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
            

    :rtype: dict
    :return: {
        'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
        'httpMethod': 'string',
        'uri': 'string',
        'credentials': 'string',
        'requestParameters': {
            'string': 'string'
        },
        'requestTemplates': {
            'string': 'string'
        },
        'passthroughBehavior': 'string',
        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
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
    (string) --
    (string) --
    
    
    
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
            Specifies a put integration response request's API identifier.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            Specifies a put integration response request's resource identifier.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            Specifies a put integration response request's HTTP method.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            Specifies the status code that is used to map the integration response to an existing MethodResponse .
            

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

def put_method(restApiId=None, resourceId=None, httpMethod=None, authorizationType=None, authorizerId=None, apiKeyRequired=None, operationName=None, requestParameters=None, requestModels=None, requestValidatorId=None):
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
        requestValidatorId='string'
    )
    
    
    :type restApiId: string
    :param restApiId: [REQUIRED]
            The RestApi identifier for the new Method resource.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the new Method resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            Specifies the method request's HTTP method type.
            

    :type authorizationType: string
    :param authorizationType: [REQUIRED]
            The method's authorization type. Valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, CUSTOM for using a custom authorizer, or COGNITO_USER_POOLS for using a Cognito user pool.
            

    :type authorizerId: string
    :param authorizerId: Specifies the identifier of an Authorizer to use on this Method, if the type is CUSTOM.

    :type apiKeyRequired: boolean
    :param apiKeyRequired: Specifies whether the method required a valid ApiKey .

    :type operationName: string
    :param operationName: A human-friendly operation identifier for the method. For example, you can assign the operationName of ListPets for the GET /pets method in PetStore example.

    :type requestParameters: dict
    :param requestParameters: A key-value map defining required or optional method request parameters that can be accepted by Amazon API Gateway. A key defines a method request parameter name matching the pattern of method.request.{location}.{name} , where location is querystring , path , or header and name is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (true ) or optional (false ). The method request parameter names defined here are available in Integration to be mapped to integration request parameters or body-mapping templates.
            (string) --
            (boolean) --
            

    :type requestModels: dict
    :param requestModels: Specifies the Model resources used for the request's content type. Request models are represented as a key/value map, with a content type as the key and a Model name as the value.
            (string) --
            (string) --
            

    :type requestValidatorId: string
    :param requestValidatorId: The identifier of a RequestValidator for validating the method request.

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
            'credentials': 'string',
            'requestParameters': {
                'string': 'string'
            },
            'requestTemplates': {
                'string': 'string'
            },
            'passthroughBehavior': 'string',
            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
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
            The RestApi identifier for the Method resource.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the Method resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            The HTTP verb of the Method resource.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            The method response's status code.
            

    :type responseParameters: dict
    :param responseParameters: A key-value map specifying required or optional response parameters that Amazon API Gateway can send back to the caller. A key defines a method response header name and the associated value is a Boolean flag indicating whether the method response parameter is required or not. The method response header names must match the pattern of method.response.header.{name} , where name is a valid and unique header name. The response parameter names defined here are available in the integration response to be mapped from an integration response header expressed in integration.response.header.{name} , a static value enclosed within a pair of single quotes (e.g., 'application/json' ), or a JSON expression from the back-end response payload in the form of integration.response.body.{JSON-expression} , where JSON-expression is a valid JSON expression without the $ prefix.)
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
    A feature of the Amazon API Gateway control service for updating an existing API with an input of external API definitions. The update can take the form of merging the supplied definition into the existing API or overwriting the existing API.
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
            The identifier of the RestApi to be updated.
            

    :type mode: string
    :param mode: The mode query parameter to specify the update mode. Valid values are 'merge' and 'overwrite'. By default, the update mode is 'merge'.

    :type failOnWarnings: boolean
    :param failOnWarnings: A query parameter to indicate whether to rollback the API update (true ) or not (false ) when a warning is encountered. The default value is false .

    :type parameters: dict
    :param parameters: Custom headers supplied as part of the request.
            (string) --
            (string) --
            

    :type body: bytes or seekable file-like object
    :param body: [REQUIRED]
            The PUT request body containing external API definitions. Currently, only Swagger definition JSON files are supported.
            

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
        ]
    }
    
    
    :returns: 
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
            Specifies a test invoke authorizer request's RestApi identifier.
            

    :type authorizerId: string
    :param authorizerId: [REQUIRED]
            Specifies a test invoke authorizer request's Authorizer ID.
            

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
            Specifies a test invoke method request's API identifier.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            Specifies a test invoke method request's resource ID.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            Specifies a test invoke method request's HTTP method.
            

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
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
            The identifier of the ApiKey resource to be updated.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
            The RestApi identifier for the Authorizer resource.
            

    :type authorizerId: string
    :param authorizerId: [REQUIRED]
            The identifier of the Authorizer resource.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

    :rtype: dict
    :return: {
        'id': 'string',
        'name': 'string',
        'type': 'TOKEN'|'COGNITO_USER_POOLS',
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
            The domain name of the BasePathMapping resource to change.
            

    :type basePath: string
    :param basePath: [REQUIRED]
            The base path of the BasePathMapping resource to change.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
            The identifier of the ClientCertificate resource to be updated.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
            The replacement identifier of the RestApi resource for the Deployment resource to change information about.
            

    :type deploymentId: string
    :param deploymentId: [REQUIRED]
            The replacement identifier for the Deployment resource to change information about.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
            [Required] The identifier of an API of the to-be-updated documentation part.
            

    :type documentationPartId: string
    :param documentationPartId: [REQUIRED]
            [Required] The identifier of the to-be-updated documentation part.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
            [Required] The identifier of an API of the to-be-updated documentation version.
            

    :type documentationVersion: string
    :param documentationVersion: [REQUIRED]
            [Required] The version identifier of the to-be-updated documentation version.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
            The name of the DomainName resource to be changed.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

    :rtype: dict
    :return: {
        'domainName': 'string',
        'certificateName': 'string',
        'certificateArn': 'string',
        'certificateUploadDate': datetime(2015, 1, 1),
        'distributionDomainName': 'string'
    }
    
    
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
            Represents an update integration request's API identifier.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            Represents an update integration request's resource identifier.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            Represents an update integration request's HTTP method.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

    :rtype: dict
    :return: {
        'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
        'httpMethod': 'string',
        'uri': 'string',
        'credentials': 'string',
        'requestParameters': {
            'string': 'string'
        },
        'requestTemplates': {
            'string': 'string'
        },
        'passthroughBehavior': 'string',
        'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
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
    (string) --
    (string) --
    
    
    
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
            Specifies an update integration response request's API identifier.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            Specifies an update integration response request's resource identifier.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            Specifies an update integration response request's HTTP method.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            Specifies an update integration response request's status code.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
            The RestApi identifier for the Method resource.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the Method resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            The HTTP verb of the Method resource.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
            'credentials': 'string',
            'requestParameters': {
                'string': 'string'
            },
            'requestTemplates': {
                'string': 'string'
            },
            'passthroughBehavior': 'string',
            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
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
            The RestApi identifier for the MethodResponse resource.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the MethodResponse resource.
            

    :type httpMethod: string
    :param httpMethod: [REQUIRED]
            The HTTP verb of the Method resource.
            

    :type statusCode: string
    :param statusCode: [REQUIRED]
            The status code for the MethodResponse resource.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
            The RestApi identifier under which the model exists.
            

    :type modelName: string
    :param modelName: [REQUIRED]
            The name of the model to update.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
            [Required] The identifier of the RestApi for which the given RequestValidator is updated.
            

    :type requestValidatorId: string
    :param requestValidatorId: [REQUIRED]
            [Required] The identifier of RequestValidator to be updated.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
            The RestApi identifier for the Resource resource.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            The identifier of the Resource resource.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
                    'credentials': 'string',
                    'requestParameters': {
                        'string': 'string'
                    },
                    'requestTemplates': {
                        'string': 'string'
                    },
                    'passthroughBehavior': 'string',
                    'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
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
            The ID of the RestApi you want to update.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
        ]
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
            The identifier of the RestApi resource for the Stage resource to change information about.
            

    :type stageName: string
    :param stageName: [REQUIRED]
            The name of the Stage resource to change information about.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
    Grants a temporary extension to the reamining quota of a usage plan associated with a specified API key.
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
            The Id of the usage plan associated with the usage data.
            

    :type keyId: string
    :param keyId: [REQUIRED]
            The identifier of the API key associated with the usage plan in which a temporary extension is granted to the remaining quota.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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
            The Id of the to-be-updated usage plan.
            

    :type patchOperations: list
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., '{'a': ...}'. In a Windows shell, see Using JSON for Parameters .
            from (string) --Not supported.
            
            

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

