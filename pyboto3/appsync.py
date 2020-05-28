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

def create_api_cache(apiId=None, ttl=None, transitEncryptionEnabled=None, atRestEncryptionEnabled=None, apiCachingBehavior=None, type=None):
    """
    Creates a cache for the GraphQL API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_api_cache(
        apiId='string',
        ttl=123,
        transitEncryptionEnabled=True|False,
        atRestEncryptionEnabled=True|False,
        apiCachingBehavior='FULL_REQUEST_CACHING'|'PER_RESOLVER_CACHING',
        type='T2_SMALL'|'T2_MEDIUM'|'R4_LARGE'|'R4_XLARGE'|'R4_2XLARGE'|'R4_4XLARGE'|'R4_8XLARGE'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe GraphQL API Id.\n

    :type ttl: integer
    :param ttl: [REQUIRED]\nTTL in seconds for cache entries.\nValid values are between 1 and 3600 seconds.\n

    :type transitEncryptionEnabled: boolean
    :param transitEncryptionEnabled: Transit encryption flag when connecting to cache. This setting cannot be updated after creation.

    :type atRestEncryptionEnabled: boolean
    :param atRestEncryptionEnabled: At rest encryption flag for cache. This setting cannot be updated after creation.

    :type apiCachingBehavior: string
    :param apiCachingBehavior: [REQUIRED]\nCaching behavior.\n\nFULL_REQUEST_CACHING : All requests are fully cached.\nPER_RESOLVER_CACHING : Individual resovlers that you specify are cached.\n\n

    :type type: string
    :param type: [REQUIRED]\nThe cache instance type.\n\nT2_SMALL : A t2.small instance type.\nT2_MEDIUM : A t2.medium instance type.\nR4_LARGE : A r4.large instance type.\nR4_XLARGE : A r4.xlarge instance type.\nR4_2XLARGE : A r4.2xlarge instance type.\nR4_4XLARGE : A r4.4xlarge instance type.\nR4_8XLARGE : A r4.8xlarge instance type.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'apiCache': {
        'ttl': 123,
        'apiCachingBehavior': 'FULL_REQUEST_CACHING'|'PER_RESOLVER_CACHING',
        'transitEncryptionEnabled': True|False,
        'atRestEncryptionEnabled': True|False,
        'type': 'T2_SMALL'|'T2_MEDIUM'|'R4_LARGE'|'R4_XLARGE'|'R4_2XLARGE'|'R4_4XLARGE'|'R4_8XLARGE',
        'status': 'AVAILABLE'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'
    }
}


Response Structure

(dict) --
Represents the output of a CreateApiCache operation.

apiCache (dict) --
The ApiCache object.

ttl (integer) --
TTL in seconds for cache entries.
Valid values are between 1 and 3600 seconds.

apiCachingBehavior (string) --
Caching behavior.

FULL_REQUEST_CACHING : All requests are fully cached.
PER_RESOLVER_CACHING : Individual resovlers that you specify are cached.


transitEncryptionEnabled (boolean) --
Transit encryption flag when connecting to cache. This setting cannot be updated after creation.

atRestEncryptionEnabled (boolean) --
At rest encryption flag for cache. This setting cannot be updated after creation.

type (string) --
The cache instance type.

T2_SMALL : A t2.small instance type.
T2_MEDIUM : A t2.medium instance type.
R4_LARGE : A r4.large instance type.
R4_XLARGE : A r4.xlarge instance type.
R4_2XLARGE : A r4.2xlarge instance type.
R4_4XLARGE : A r4.4xlarge instance type.
R4_8XLARGE : A r4.8xlarge instance type.


status (string) --
The cache instance status.

AVAILABLE : The instance is available for use.
CREATING : The instance is currently creating.
DELETING : The instance is currently deleting.
MODIFYING : The instance is currently modifying.
FAILED : The instance has failed creation.










Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'apiCache': {
            'ttl': 123,
            'apiCachingBehavior': 'FULL_REQUEST_CACHING'|'PER_RESOLVER_CACHING',
            'transitEncryptionEnabled': True|False,
            'atRestEncryptionEnabled': True|False,
            'type': 'T2_SMALL'|'T2_MEDIUM'|'R4_LARGE'|'R4_XLARGE'|'R4_2XLARGE'|'R4_4XLARGE'|'R4_8XLARGE',
            'status': 'AVAILABLE'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'
        }
    }
    
    
    :returns: 
    FULL_REQUEST_CACHING : All requests are fully cached.
    PER_RESOLVER_CACHING : Individual resovlers that you specify are cached.
    
    """
    pass

def create_api_key(apiId=None, description=None, expires=None):
    """
    Creates a unique key that you can distribute to clients who are executing your API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_api_key(
        apiId='string',
        description='string',
        expires=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe ID for your GraphQL API.\n

    :type description: string
    :param description: A description of the purpose of the API key.

    :type expires: integer
    :param expires: The time from creation time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour. The default value for this parameter is 7 days from creation time. For more information, see .

    :rtype: dict

ReturnsResponse Syntax
{
    'apiKey': {
        'id': 'string',
        'description': 'string',
        'expires': 123
    }
}


Response Structure

(dict) --

apiKey (dict) --
The API key.

id (string) --
The API key ID.

description (string) --
A description of the purpose of the API key.

expires (integer) --
The time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour.









Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.LimitExceededException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.LimitExceededException
AppSync.Client.exceptions.InternalFailureException
AppSync.Client.exceptions.ApiKeyLimitExceededException
AppSync.Client.exceptions.ApiKeyValidityOutOfBoundsException


    :return: {
        'apiKey': {
            'id': 'string',
            'description': 'string',
            'expires': 123
        }
    }
    
    
    :returns: 
    AppSync.Client.exceptions.BadRequestException
    AppSync.Client.exceptions.NotFoundException
    AppSync.Client.exceptions.LimitExceededException
    AppSync.Client.exceptions.UnauthorizedException
    AppSync.Client.exceptions.LimitExceededException
    AppSync.Client.exceptions.InternalFailureException
    AppSync.Client.exceptions.ApiKeyLimitExceededException
    AppSync.Client.exceptions.ApiKeyValidityOutOfBoundsException
    
    """
    pass

def create_data_source(apiId=None, name=None, description=None, type=None, serviceRoleArn=None, dynamodbConfig=None, lambdaConfig=None, elasticsearchConfig=None, httpConfig=None, relationalDatabaseConfig=None):
    """
    Creates a DataSource object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_data_source(
        apiId='string',
        name='string',
        description='string',
        type='AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
        serviceRoleArn='string',
        dynamodbConfig={
            'tableName': 'string',
            'awsRegion': 'string',
            'useCallerCredentials': True|False,
            'deltaSyncConfig': {
                'baseTableTTL': 123,
                'deltaSyncTableName': 'string',
                'deltaSyncTableTTL': 123
            },
            'versioned': True|False
        },
        lambdaConfig={
            'lambdaFunctionArn': 'string'
        },
        elasticsearchConfig={
            'endpoint': 'string',
            'awsRegion': 'string'
        },
        httpConfig={
            'endpoint': 'string',
            'authorizationConfig': {
                'authorizationType': 'AWS_IAM',
                'awsIamConfig': {
                    'signingRegion': 'string',
                    'signingServiceName': 'string'
                }
            }
        },
        relationalDatabaseConfig={
            'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
            'rdsHttpEndpointConfig': {
                'awsRegion': 'string',
                'dbClusterIdentifier': 'string',
                'databaseName': 'string',
                'schema': 'string',
                'awsSecretStoreArn': 'string'
            }
        }
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID for the GraphQL API for the DataSource .\n

    :type name: string
    :param name: [REQUIRED]\nA user-supplied name for the DataSource .\n

    :type description: string
    :param description: A description of the DataSource .

    :type type: string
    :param type: [REQUIRED]\nThe type of the DataSource .\n

    :type serviceRoleArn: string
    :param serviceRoleArn: The AWS IAM service role ARN for the data source. The system assumes this role when accessing the data source.

    :type dynamodbConfig: dict
    :param dynamodbConfig: Amazon DynamoDB settings.\n\ntableName (string) -- [REQUIRED]The table name.\n\nawsRegion (string) -- [REQUIRED]The AWS Region.\n\nuseCallerCredentials (boolean) --Set to TRUE to use Amazon Cognito credentials with this data source.\n\ndeltaSyncConfig (dict) --The DeltaSyncConfig for a versioned datasource.\n\nbaseTableTTL (integer) --The number of minutes an Item is stored in the datasource.\n\ndeltaSyncTableName (string) --The Delta Sync table name.\n\ndeltaSyncTableTTL (integer) --The number of minutes a Delta Sync log entry is stored in the Delta Sync table.\n\n\n\nversioned (boolean) --Set to TRUE to use Conflict Detection and Resolution with this data source.\n\n\n

    :type lambdaConfig: dict
    :param lambdaConfig: AWS Lambda settings.\n\nlambdaFunctionArn (string) -- [REQUIRED]The ARN for the Lambda function.\n\n\n

    :type elasticsearchConfig: dict
    :param elasticsearchConfig: Amazon Elasticsearch Service settings.\n\nendpoint (string) -- [REQUIRED]The endpoint.\n\nawsRegion (string) -- [REQUIRED]The AWS Region.\n\n\n

    :type httpConfig: dict
    :param httpConfig: HTTP endpoint settings.\n\nendpoint (string) --The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.\n\nauthorizationConfig (dict) --The authorization config in case the HTTP endpoint requires authorization.\n\nauthorizationType (string) -- [REQUIRED]The authorization type required by the HTTP endpoint.\n\nAWS_IAM : The authorization type is Sigv4.\n\n\nawsIamConfig (dict) --The AWS IAM settings.\n\nsigningRegion (string) --The signing region for AWS IAM authorization.\n\nsigningServiceName (string) --The signing service name for AWS IAM authorization.\n\n\n\n\n\n\n

    :type relationalDatabaseConfig: dict
    :param relationalDatabaseConfig: Relational database settings.\n\nrelationalDatabaseSourceType (string) --Source type for the relational database.\n\nRDS_HTTP_ENDPOINT : The relational database source type is an Amazon RDS HTTP endpoint.\n\n\nrdsHttpEndpointConfig (dict) --Amazon RDS HTTP endpoint settings.\n\nawsRegion (string) --AWS Region for RDS HTTP endpoint.\n\ndbClusterIdentifier (string) --Amazon RDS cluster identifier.\n\ndatabaseName (string) --Logical database name.\n\nschema (string) --Logical schema name.\n\nawsSecretStoreArn (string) --AWS secret store ARN for database credentials.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'dataSource': {
        'dataSourceArn': 'string',
        'name': 'string',
        'description': 'string',
        'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
        'serviceRoleArn': 'string',
        'dynamodbConfig': {
            'tableName': 'string',
            'awsRegion': 'string',
            'useCallerCredentials': True|False,
            'deltaSyncConfig': {
                'baseTableTTL': 123,
                'deltaSyncTableName': 'string',
                'deltaSyncTableTTL': 123
            },
            'versioned': True|False
        },
        'lambdaConfig': {
            'lambdaFunctionArn': 'string'
        },
        'elasticsearchConfig': {
            'endpoint': 'string',
            'awsRegion': 'string'
        },
        'httpConfig': {
            'endpoint': 'string',
            'authorizationConfig': {
                'authorizationType': 'AWS_IAM',
                'awsIamConfig': {
                    'signingRegion': 'string',
                    'signingServiceName': 'string'
                }
            }
        },
        'relationalDatabaseConfig': {
            'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
            'rdsHttpEndpointConfig': {
                'awsRegion': 'string',
                'dbClusterIdentifier': 'string',
                'databaseName': 'string',
                'schema': 'string',
                'awsSecretStoreArn': 'string'
            }
        }
    }
}


Response Structure

(dict) --

dataSource (dict) --
The DataSource object.

dataSourceArn (string) --
The data source ARN.

name (string) --
The name of the data source.

description (string) --
The description of the data source.

type (string) --
The type of the data source.

AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
AWS_LAMBDA : The data source is an AWS Lambda function.
NONE : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
HTTP : The data source is an HTTP endpoint.
RELATIONAL_DATABASE : The data source is a relational database.


serviceRoleArn (string) --
The AWS IAM service role ARN for the data source. The system assumes this role when accessing the data source.

dynamodbConfig (dict) --
Amazon DynamoDB settings.

tableName (string) --
The table name.

awsRegion (string) --
The AWS Region.

useCallerCredentials (boolean) --
Set to TRUE to use Amazon Cognito credentials with this data source.

deltaSyncConfig (dict) --
The DeltaSyncConfig for a versioned datasource.

baseTableTTL (integer) --
The number of minutes an Item is stored in the datasource.

deltaSyncTableName (string) --
The Delta Sync table name.

deltaSyncTableTTL (integer) --
The number of minutes a Delta Sync log entry is stored in the Delta Sync table.



versioned (boolean) --
Set to TRUE to use Conflict Detection and Resolution with this data source.



lambdaConfig (dict) --
AWS Lambda settings.

lambdaFunctionArn (string) --
The ARN for the Lambda function.



elasticsearchConfig (dict) --
Amazon Elasticsearch Service settings.

endpoint (string) --
The endpoint.

awsRegion (string) --
The AWS Region.



httpConfig (dict) --
HTTP endpoint settings.

endpoint (string) --
The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.

authorizationConfig (dict) --
The authorization config in case the HTTP endpoint requires authorization.

authorizationType (string) --
The authorization type required by the HTTP endpoint.

AWS_IAM : The authorization type is Sigv4.


awsIamConfig (dict) --
The AWS IAM settings.

signingRegion (string) --
The signing region for AWS IAM authorization.

signingServiceName (string) --
The signing service name for AWS IAM authorization.







relationalDatabaseConfig (dict) --
Relational database settings.

relationalDatabaseSourceType (string) --
Source type for the relational database.

RDS_HTTP_ENDPOINT : The relational database source type is an Amazon RDS HTTP endpoint.


rdsHttpEndpointConfig (dict) --
Amazon RDS HTTP endpoint settings.

awsRegion (string) --
AWS Region for RDS HTTP endpoint.

dbClusterIdentifier (string) --
Amazon RDS cluster identifier.

databaseName (string) --
Logical database name.

schema (string) --
Logical schema name.

awsSecretStoreArn (string) --
AWS secret store ARN for database credentials.













Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'dataSource': {
            'dataSourceArn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
            'serviceRoleArn': 'string',
            'dynamodbConfig': {
                'tableName': 'string',
                'awsRegion': 'string',
                'useCallerCredentials': True|False,
                'deltaSyncConfig': {
                    'baseTableTTL': 123,
                    'deltaSyncTableName': 'string',
                    'deltaSyncTableTTL': 123
                },
                'versioned': True|False
            },
            'lambdaConfig': {
                'lambdaFunctionArn': 'string'
            },
            'elasticsearchConfig': {
                'endpoint': 'string',
                'awsRegion': 'string'
            },
            'httpConfig': {
                'endpoint': 'string',
                'authorizationConfig': {
                    'authorizationType': 'AWS_IAM',
                    'awsIamConfig': {
                        'signingRegion': 'string',
                        'signingServiceName': 'string'
                    }
                }
            },
            'relationalDatabaseConfig': {
                'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                'rdsHttpEndpointConfig': {
                    'awsRegion': 'string',
                    'dbClusterIdentifier': 'string',
                    'databaseName': 'string',
                    'schema': 'string',
                    'awsSecretStoreArn': 'string'
                }
            }
        }
    }
    
    
    :returns: 
    AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
    AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
    AWS_LAMBDA : The data source is an AWS Lambda function.
    NONE : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
    HTTP : The data source is an HTTP endpoint.
    RELATIONAL_DATABASE : The data source is a relational database.
    
    """
    pass

def create_function(apiId=None, name=None, description=None, dataSourceName=None, requestMappingTemplate=None, responseMappingTemplate=None, functionVersion=None):
    """
    Creates a Function object.
    A function is a reusable entity. Multiple functions can be used to compose the resolver logic.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_function(
        apiId='string',
        name='string',
        description='string',
        dataSourceName='string',
        requestMappingTemplate='string',
        responseMappingTemplate='string',
        functionVersion='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe GraphQL API ID.\n

    :type name: string
    :param name: [REQUIRED]\nThe Function name. The function name does not have to be unique.\n

    :type description: string
    :param description: The Function description.

    :type dataSourceName: string
    :param dataSourceName: [REQUIRED]\nThe Function DataSource name.\n

    :type requestMappingTemplate: string
    :param requestMappingTemplate: [REQUIRED]\nThe Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.\n

    :type responseMappingTemplate: string
    :param responseMappingTemplate: The Function response mapping template.

    :type functionVersion: string
    :param functionVersion: [REQUIRED]\nThe version of the request mapping template. Currently the supported value is 2018-05-29.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'functionConfiguration': {
        'functionId': 'string',
        'functionArn': 'string',
        'name': 'string',
        'description': 'string',
        'dataSourceName': 'string',
        'requestMappingTemplate': 'string',
        'responseMappingTemplate': 'string',
        'functionVersion': 'string'
    }
}


Response Structure

(dict) --

functionConfiguration (dict) --
The Function object.

functionId (string) --
A unique ID representing the Function object.

functionArn (string) --
The ARN of the Function object.

name (string) --
The name of the Function object.

description (string) --
The Function description.

dataSourceName (string) --
The name of the DataSource .

requestMappingTemplate (string) --
The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.

responseMappingTemplate (string) --
The Function response mapping template.

functionVersion (string) --
The version of the request mapping template. Currently only the 2018-05-29 version of the template is supported.









Exceptions

AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'functionConfiguration': {
            'functionId': 'string',
            'functionArn': 'string',
            'name': 'string',
            'description': 'string',
            'dataSourceName': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'functionVersion': 'string'
        }
    }
    
    
    :returns: 
    AppSync.Client.exceptions.ConcurrentModificationException
    AppSync.Client.exceptions.NotFoundException
    AppSync.Client.exceptions.UnauthorizedException
    AppSync.Client.exceptions.InternalFailureException
    
    """
    pass

def create_graphql_api(name=None, logConfig=None, authenticationType=None, userPoolConfig=None, openIDConnectConfig=None, tags=None, additionalAuthenticationProviders=None, xrayEnabled=None):
    """
    Creates a GraphqlApi object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_graphql_api(
        name='string',
        logConfig={
            'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
            'cloudWatchLogsRoleArn': 'string',
            'excludeVerboseContent': True|False
        },
        authenticationType='API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
        userPoolConfig={
            'userPoolId': 'string',
            'awsRegion': 'string',
            'defaultAction': 'ALLOW'|'DENY',
            'appIdClientRegex': 'string'
        },
        openIDConnectConfig={
            'issuer': 'string',
            'clientId': 'string',
            'iatTTL': 123,
            'authTTL': 123
        },
        tags={
            'string': 'string'
        },
        additionalAuthenticationProviders=[
            {
                'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                'openIDConnectConfig': {
                    'issuer': 'string',
                    'clientId': 'string',
                    'iatTTL': 123,
                    'authTTL': 123
                },
                'userPoolConfig': {
                    'userPoolId': 'string',
                    'awsRegion': 'string',
                    'appIdClientRegex': 'string'
                }
            },
        ],
        xrayEnabled=True|False
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nA user-supplied name for the GraphqlApi .\n

    :type logConfig: dict
    :param logConfig: The Amazon CloudWatch Logs configuration.\n\nfieldLogLevel (string) -- [REQUIRED]The field logging level. Values can be NONE, ERROR, or ALL.\n\nNONE : No field-level logs are captured.\nERROR : Logs the following information only for the fields that are in error:\nThe error section in the server response.\nField-level errors.\nThe generated request/response functions that got resolved for error fields.\n\n\nALL : The following information is logged for all fields in the query:\nField-level tracing information.\nThe generated request/response functions that got resolved for each field.\n\n\n\n\ncloudWatchLogsRoleArn (string) -- [REQUIRED]The service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.\n\nexcludeVerboseContent (boolean) --Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.\n\n\n

    :type authenticationType: string
    :param authenticationType: [REQUIRED]\nThe authentication type: API key, AWS IAM, OIDC, or Amazon Cognito user pools.\n

    :type userPoolConfig: dict
    :param userPoolConfig: The Amazon Cognito user pool configuration.\n\nuserPoolId (string) -- [REQUIRED]The user pool ID.\n\nawsRegion (string) -- [REQUIRED]The AWS Region in which the user pool was created.\n\ndefaultAction (string) -- [REQUIRED]The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn\'t match the Amazon Cognito user pool configuration.\n\nappIdClientRegex (string) --A regular expression for validating the incoming Amazon Cognito user pool app client ID.\n\n\n

    :type openIDConnectConfig: dict
    :param openIDConnectConfig: The OpenID Connect configuration.\n\nissuer (string) -- [REQUIRED]The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of iss in the ID token.\n\nclientId (string) --The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.\n\niatTTL (integer) --The number of milliseconds a token is valid after being issued to a user.\n\nauthTTL (integer) --The number of milliseconds a token is valid after being authenticated.\n\n\n

    :type tags: dict
    :param tags: A TagMap object.\n\n(string) --The key for the tag.\n\n(string) --The value for the tag.\n\n\n\n\n

    :type additionalAuthenticationProviders: list
    :param additionalAuthenticationProviders: A list of additional authentication providers for the GraphqlApi API.\n\n(dict) --Describes an additional authentication provider.\n\nauthenticationType (string) --The authentication type: API key, AWS IAM, OIDC, or Amazon Cognito user pools.\n\nopenIDConnectConfig (dict) --The OpenID Connect configuration.\n\nissuer (string) -- [REQUIRED]The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of iss in the ID token.\n\nclientId (string) --The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.\n\niatTTL (integer) --The number of milliseconds a token is valid after being issued to a user.\n\nauthTTL (integer) --The number of milliseconds a token is valid after being authenticated.\n\n\n\nuserPoolConfig (dict) --The Amazon Cognito user pool configuration.\n\nuserPoolId (string) -- [REQUIRED]The user pool ID.\n\nawsRegion (string) -- [REQUIRED]The AWS Region in which the user pool was created.\n\nappIdClientRegex (string) --A regular expression for validating the incoming Amazon Cognito user pool app client ID.\n\n\n\n\n\n\n

    :type xrayEnabled: boolean
    :param xrayEnabled: A flag indicating whether to enable X-Ray tracing for the GraphqlApi .

    :rtype: dict

ReturnsResponse Syntax
{
    'graphqlApi': {
        'name': 'string',
        'apiId': 'string',
        'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
        'logConfig': {
            'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
            'cloudWatchLogsRoleArn': 'string',
            'excludeVerboseContent': True|False
        },
        'userPoolConfig': {
            'userPoolId': 'string',
            'awsRegion': 'string',
            'defaultAction': 'ALLOW'|'DENY',
            'appIdClientRegex': 'string'
        },
        'openIDConnectConfig': {
            'issuer': 'string',
            'clientId': 'string',
            'iatTTL': 123,
            'authTTL': 123
        },
        'arn': 'string',
        'uris': {
            'string': 'string'
        },
        'tags': {
            'string': 'string'
        },
        'additionalAuthenticationProviders': [
            {
                'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                'openIDConnectConfig': {
                    'issuer': 'string',
                    'clientId': 'string',
                    'iatTTL': 123,
                    'authTTL': 123
                },
                'userPoolConfig': {
                    'userPoolId': 'string',
                    'awsRegion': 'string',
                    'appIdClientRegex': 'string'
                }
            },
        ],
        'xrayEnabled': True|False
    }
}


Response Structure

(dict) --

graphqlApi (dict) --
The GraphqlApi .

name (string) --
The API name.

apiId (string) --
The API ID.

authenticationType (string) --
The authentication type.

logConfig (dict) --
The Amazon CloudWatch Logs configuration.

fieldLogLevel (string) --
The field logging level. Values can be NONE, ERROR, or ALL.

NONE : No field-level logs are captured.
ERROR : Logs the following information only for the fields that are in error:
The error section in the server response.
Field-level errors.
The generated request/response functions that got resolved for error fields.


ALL : The following information is logged for all fields in the query:
Field-level tracing information.
The generated request/response functions that got resolved for each field.




cloudWatchLogsRoleArn (string) --
The service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.

excludeVerboseContent (boolean) --
Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.



userPoolConfig (dict) --
The Amazon Cognito user pool configuration.

userPoolId (string) --
The user pool ID.

awsRegion (string) --
The AWS Region in which the user pool was created.

defaultAction (string) --
The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn\'t match the Amazon Cognito user pool configuration.

appIdClientRegex (string) --
A regular expression for validating the incoming Amazon Cognito user pool app client ID.



openIDConnectConfig (dict) --
The OpenID Connect configuration.

issuer (string) --
The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of iss in the ID token.

clientId (string) --
The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.

iatTTL (integer) --
The number of milliseconds a token is valid after being issued to a user.

authTTL (integer) --
The number of milliseconds a token is valid after being authenticated.



arn (string) --
The ARN.

uris (dict) --
The URIs.

(string) --
(string) --




tags (dict) --
The tags.

(string) --
The key for the tag.

(string) --
The value for the tag.





additionalAuthenticationProviders (list) --
A list of additional authentication providers for the GraphqlApi API.

(dict) --
Describes an additional authentication provider.

authenticationType (string) --
The authentication type: API key, AWS IAM, OIDC, or Amazon Cognito user pools.

openIDConnectConfig (dict) --
The OpenID Connect configuration.

issuer (string) --
The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of iss in the ID token.

clientId (string) --
The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.

iatTTL (integer) --
The number of milliseconds a token is valid after being issued to a user.

authTTL (integer) --
The number of milliseconds a token is valid after being authenticated.



userPoolConfig (dict) --
The Amazon Cognito user pool configuration.

userPoolId (string) --
The user pool ID.

awsRegion (string) --
The AWS Region in which the user pool was created.

appIdClientRegex (string) --
A regular expression for validating the incoming Amazon Cognito user pool app client ID.







xrayEnabled (boolean) --
A flag representing whether X-Ray tracing is enabled for this GraphqlApi .









Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.LimitExceededException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException
AppSync.Client.exceptions.ApiLimitExceededException


    :return: {
        'graphqlApi': {
            'name': 'string',
            'apiId': 'string',
            'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
            'logConfig': {
                'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                'cloudWatchLogsRoleArn': 'string',
                'excludeVerboseContent': True|False
            },
            'userPoolConfig': {
                'userPoolId': 'string',
                'awsRegion': 'string',
                'defaultAction': 'ALLOW'|'DENY',
                'appIdClientRegex': 'string'
            },
            'openIDConnectConfig': {
                'issuer': 'string',
                'clientId': 'string',
                'iatTTL': 123,
                'authTTL': 123
            },
            'arn': 'string',
            'uris': {
                'string': 'string'
            },
            'tags': {
                'string': 'string'
            },
            'additionalAuthenticationProviders': [
                {
                    'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                    'openIDConnectConfig': {
                        'issuer': 'string',
                        'clientId': 'string',
                        'iatTTL': 123,
                        'authTTL': 123
                    },
                    'userPoolConfig': {
                        'userPoolId': 'string',
                        'awsRegion': 'string',
                        'appIdClientRegex': 'string'
                    }
                },
            ],
            'xrayEnabled': True|False
        }
    }
    
    
    :returns: 
    NONE : No field-level logs are captured.
    ERROR : Logs the following information only for the fields that are in error:
    The error section in the server response.
    Field-level errors.
    The generated request/response functions that got resolved for error fields.
    
    
    ALL : The following information is logged for all fields in the query:
    Field-level tracing information.
    The generated request/response functions that got resolved for each field.
    
    
    
    """
    pass

def create_resolver(apiId=None, typeName=None, fieldName=None, dataSourceName=None, requestMappingTemplate=None, responseMappingTemplate=None, kind=None, pipelineConfig=None, syncConfig=None, cachingConfig=None):
    """
    Creates a Resolver object.
    A resolver converts incoming requests into a format that a data source can understand and converts the data source\'s responses into GraphQL.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_resolver(
        apiId='string',
        typeName='string',
        fieldName='string',
        dataSourceName='string',
        requestMappingTemplate='string',
        responseMappingTemplate='string',
        kind='UNIT'|'PIPELINE',
        pipelineConfig={
            'functions': [
                'string',
            ]
        },
        syncConfig={
            'conflictHandler': 'OPTIMISTIC_CONCURRENCY'|'LAMBDA'|'AUTOMERGE'|'NONE',
            'conflictDetection': 'VERSION'|'NONE',
            'lambdaConflictHandlerConfig': {
                'lambdaConflictHandlerArn': 'string'
            }
        },
        cachingConfig={
            'ttl': 123,
            'cachingKeys': [
                'string',
            ]
        }
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe ID for the GraphQL API for which the resolver is being created.\n

    :type typeName: string
    :param typeName: [REQUIRED]\nThe name of the Type .\n

    :type fieldName: string
    :param fieldName: [REQUIRED]\nThe name of the field to attach the resolver to.\n

    :type dataSourceName: string
    :param dataSourceName: The name of the data source for which the resolver is being created.

    :type requestMappingTemplate: string
    :param requestMappingTemplate: [REQUIRED]\nThe mapping template to be used for requests.\nA resolver uses a request mapping template to convert a GraphQL expression into a format that a data source can understand. Mapping templates are written in Apache Velocity Template Language (VTL).\n

    :type responseMappingTemplate: string
    :param responseMappingTemplate: The mapping template to be used for responses from the data source.

    :type kind: string
    :param kind: The resolver type.\n\nUNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.\nPIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.\n\n

    :type pipelineConfig: dict
    :param pipelineConfig: The PipelineConfig .\n\nfunctions (list) --A list of Function objects.\n\n(string) --\n\n\n\n

    :type syncConfig: dict
    :param syncConfig: The SyncConfig for a resolver attached to a versioned datasource.\n\nconflictHandler (string) --The Conflict Resolution strategy to perform in the event of a conflict.\n\nOPTIMISTIC_CONCURRENCY : Resolve conflicts by rejecting mutations when versions do not match the latest version at the server.\nAUTOMERGE : Resolve conflicts with the Automerge conflict resolution strategy.\nLAMBDA : Resolve conflicts with a Lambda function supplied in the LambdaConflictHandlerConfig.\n\n\nconflictDetection (string) --The Conflict Detection strategy to use.\n\nVERSION : Detect conflicts based on object versions for this resolver.\nNONE : Do not detect conflicts when executing this resolver.\n\n\nlambdaConflictHandlerConfig (dict) --The LambdaConflictHandlerConfig when configuring LAMBDA as the Conflict Handler.\n\nlambdaConflictHandlerArn (string) --The Arn for the Lambda function to use as the Conflict Handler.\n\n\n\n\n

    :type cachingConfig: dict
    :param cachingConfig: The caching configuration for the resolver.\n\nttl (integer) --The TTL in seconds for a resolver that has caching enabled.\nValid values are between 1 and 3600 seconds.\n\ncachingKeys (list) --The caching keys for a resolver that has caching enabled.\nValid values are entries from the $context.identity and $context.arguments maps.\n\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'resolver': {
        'typeName': 'string',
        'fieldName': 'string',
        'dataSourceName': 'string',
        'resolverArn': 'string',
        'requestMappingTemplate': 'string',
        'responseMappingTemplate': 'string',
        'kind': 'UNIT'|'PIPELINE',
        'pipelineConfig': {
            'functions': [
                'string',
            ]
        },
        'syncConfig': {
            'conflictHandler': 'OPTIMISTIC_CONCURRENCY'|'LAMBDA'|'AUTOMERGE'|'NONE',
            'conflictDetection': 'VERSION'|'NONE',
            'lambdaConflictHandlerConfig': {
                'lambdaConflictHandlerArn': 'string'
            }
        },
        'cachingConfig': {
            'ttl': 123,
            'cachingKeys': [
                'string',
            ]
        }
    }
}


Response Structure

(dict) --

resolver (dict) --
The Resolver object.

typeName (string) --
The resolver type name.

fieldName (string) --
The resolver field name.

dataSourceName (string) --
The resolver data source name.

resolverArn (string) --
The resolver ARN.

requestMappingTemplate (string) --
The request mapping template.

responseMappingTemplate (string) --
The response mapping template.

kind (string) --
The resolver type.

UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.


pipelineConfig (dict) --
The PipelineConfig .

functions (list) --
A list of Function objects.

(string) --




syncConfig (dict) --
The SyncConfig for a resolver attached to a versioned datasource.

conflictHandler (string) --
The Conflict Resolution strategy to perform in the event of a conflict.

OPTIMISTIC_CONCURRENCY : Resolve conflicts by rejecting mutations when versions do not match the latest version at the server.
AUTOMERGE : Resolve conflicts with the Automerge conflict resolution strategy.
LAMBDA : Resolve conflicts with a Lambda function supplied in the LambdaConflictHandlerConfig.


conflictDetection (string) --
The Conflict Detection strategy to use.

VERSION : Detect conflicts based on object versions for this resolver.
NONE : Do not detect conflicts when executing this resolver.


lambdaConflictHandlerConfig (dict) --
The LambdaConflictHandlerConfig when configuring LAMBDA as the Conflict Handler.

lambdaConflictHandlerArn (string) --
The Arn for the Lambda function to use as the Conflict Handler.





cachingConfig (dict) --
The caching configuration for the resolver.

ttl (integer) --
The TTL in seconds for a resolver that has caching enabled.
Valid values are between 1 and 3600 seconds.

cachingKeys (list) --
The caching keys for a resolver that has caching enabled.
Valid values are entries from the $context.identity and $context.arguments maps.

(string) --












Exceptions

AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'resolver': {
            'typeName': 'string',
            'fieldName': 'string',
            'dataSourceName': 'string',
            'resolverArn': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'kind': 'UNIT'|'PIPELINE',
            'pipelineConfig': {
                'functions': [
                    'string',
                ]
            },
            'syncConfig': {
                'conflictHandler': 'OPTIMISTIC_CONCURRENCY'|'LAMBDA'|'AUTOMERGE'|'NONE',
                'conflictDetection': 'VERSION'|'NONE',
                'lambdaConflictHandlerConfig': {
                    'lambdaConflictHandlerArn': 'string'
                }
            },
            'cachingConfig': {
                'ttl': 123,
                'cachingKeys': [
                    'string',
                ]
            }
        }
    }
    
    
    :returns: 
    UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
    PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.
    
    """
    pass

def create_type(apiId=None, definition=None, format=None):
    """
    Creates a Type object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_type(
        apiId='string',
        definition='string',
        format='SDL'|'JSON'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type definition: string
    :param definition: [REQUIRED]\nThe type definition, in GraphQL Schema Definition Language (SDL) format.\nFor more information, see the GraphQL SDL documentation .\n

    :type format: string
    :param format: [REQUIRED]\nThe type format: SDL or JSON.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'type': {
        'name': 'string',
        'description': 'string',
        'arn': 'string',
        'definition': 'string',
        'format': 'SDL'|'JSON'
    }
}


Response Structure

(dict) --

type (dict) --
The Type object.

name (string) --
The type name.

description (string) --
The type description.

arn (string) --
The type ARN.

definition (string) --
The type definition.

format (string) --
The type format: SDL or JSON.









Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'type': {
            'name': 'string',
            'description': 'string',
            'arn': 'string',
            'definition': 'string',
            'format': 'SDL'|'JSON'
        }
    }
    
    
    :returns: 
    AppSync.Client.exceptions.BadRequestException
    AppSync.Client.exceptions.ConcurrentModificationException
    AppSync.Client.exceptions.NotFoundException
    AppSync.Client.exceptions.UnauthorizedException
    AppSync.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_api_cache(apiId=None):
    """
    Deletes an ApiCache object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_api_cache(
        apiId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --Represents the output of a DeleteApiCache operation.




Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {}
    
    
    """
    pass

def delete_api_key(apiId=None, id=None):
    """
    Deletes an API key.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_api_key(
        apiId='string',
        id='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type id: string
    :param id: [REQUIRED]\nThe ID for the API key.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_data_source(apiId=None, name=None):
    """
    Deletes a DataSource object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_data_source(
        apiId='string',
        name='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type name: string
    :param name: [REQUIRED]\nThe name of the data source.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_function(apiId=None, functionId=None):
    """
    Deletes a Function .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_function(
        apiId='string',
        functionId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe GraphQL API ID.\n

    :type functionId: string
    :param functionId: [REQUIRED]\nThe Function ID.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_graphql_api(apiId=None):
    """
    Deletes a GraphqlApi object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_graphql_api(
        apiId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException
AppSync.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    AppSync.Client.exceptions.BadRequestException
    AppSync.Client.exceptions.ConcurrentModificationException
    AppSync.Client.exceptions.NotFoundException
    AppSync.Client.exceptions.UnauthorizedException
    AppSync.Client.exceptions.InternalFailureException
    AppSync.Client.exceptions.AccessDeniedException
    
    """
    pass

def delete_resolver(apiId=None, typeName=None, fieldName=None):
    """
    Deletes a Resolver object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_resolver(
        apiId='string',
        typeName='string',
        fieldName='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type typeName: string
    :param typeName: [REQUIRED]\nThe name of the resolver type.\n

    :type fieldName: string
    :param fieldName: [REQUIRED]\nThe resolver field name.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_type(apiId=None, typeName=None):
    """
    Deletes a Type object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_type(
        apiId='string',
        typeName='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type typeName: string
    :param typeName: [REQUIRED]\nThe type name.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def flush_api_cache(apiId=None):
    """
    Flushes an ApiCache object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.flush_api_cache(
        apiId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --Represents the output of a FlushApiCache operation.




Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {}
    
    
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

def get_api_cache(apiId=None):
    """
    Retrieves an ApiCache object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_api_cache(
        apiId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'apiCache': {
        'ttl': 123,
        'apiCachingBehavior': 'FULL_REQUEST_CACHING'|'PER_RESOLVER_CACHING',
        'transitEncryptionEnabled': True|False,
        'atRestEncryptionEnabled': True|False,
        'type': 'T2_SMALL'|'T2_MEDIUM'|'R4_LARGE'|'R4_XLARGE'|'R4_2XLARGE'|'R4_4XLARGE'|'R4_8XLARGE',
        'status': 'AVAILABLE'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'
    }
}


Response Structure

(dict) --Represents the output of a GetApiCache operation.

apiCache (dict) --The ApiCache object.

ttl (integer) --TTL in seconds for cache entries.
Valid values are between 1 and 3600 seconds.

apiCachingBehavior (string) --Caching behavior.

FULL_REQUEST_CACHING : All requests are fully cached.
PER_RESOLVER_CACHING : Individual resovlers that you specify are cached.


transitEncryptionEnabled (boolean) --Transit encryption flag when connecting to cache. This setting cannot be updated after creation.

atRestEncryptionEnabled (boolean) --At rest encryption flag for cache. This setting cannot be updated after creation.

type (string) --The cache instance type.

T2_SMALL : A t2.small instance type.
T2_MEDIUM : A t2.medium instance type.
R4_LARGE : A r4.large instance type.
R4_XLARGE : A r4.xlarge instance type.
R4_2XLARGE : A r4.2xlarge instance type.
R4_4XLARGE : A r4.4xlarge instance type.
R4_8XLARGE : A r4.8xlarge instance type.


status (string) --The cache instance status.

AVAILABLE : The instance is available for use.
CREATING : The instance is currently creating.
DELETING : The instance is currently deleting.
MODIFYING : The instance is currently modifying.
FAILED : The instance has failed creation.









Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'apiCache': {
            'ttl': 123,
            'apiCachingBehavior': 'FULL_REQUEST_CACHING'|'PER_RESOLVER_CACHING',
            'transitEncryptionEnabled': True|False,
            'atRestEncryptionEnabled': True|False,
            'type': 'T2_SMALL'|'T2_MEDIUM'|'R4_LARGE'|'R4_XLARGE'|'R4_2XLARGE'|'R4_4XLARGE'|'R4_8XLARGE',
            'status': 'AVAILABLE'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'
        }
    }
    
    
    :returns: 
    T2_SMALL : A t2.small instance type.
    T2_MEDIUM : A t2.medium instance type.
    R4_LARGE : A r4.large instance type.
    R4_XLARGE : A r4.xlarge instance type.
    R4_2XLARGE : A r4.2xlarge instance type.
    R4_4XLARGE : A r4.4xlarge instance type.
    R4_8XLARGE : A r4.8xlarge instance type.
    
    """
    pass

def get_data_source(apiId=None, name=None):
    """
    Retrieves a DataSource object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_data_source(
        apiId='string',
        name='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type name: string
    :param name: [REQUIRED]\nThe name of the data source.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'dataSource': {
        'dataSourceArn': 'string',
        'name': 'string',
        'description': 'string',
        'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
        'serviceRoleArn': 'string',
        'dynamodbConfig': {
            'tableName': 'string',
            'awsRegion': 'string',
            'useCallerCredentials': True|False,
            'deltaSyncConfig': {
                'baseTableTTL': 123,
                'deltaSyncTableName': 'string',
                'deltaSyncTableTTL': 123
            },
            'versioned': True|False
        },
        'lambdaConfig': {
            'lambdaFunctionArn': 'string'
        },
        'elasticsearchConfig': {
            'endpoint': 'string',
            'awsRegion': 'string'
        },
        'httpConfig': {
            'endpoint': 'string',
            'authorizationConfig': {
                'authorizationType': 'AWS_IAM',
                'awsIamConfig': {
                    'signingRegion': 'string',
                    'signingServiceName': 'string'
                }
            }
        },
        'relationalDatabaseConfig': {
            'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
            'rdsHttpEndpointConfig': {
                'awsRegion': 'string',
                'dbClusterIdentifier': 'string',
                'databaseName': 'string',
                'schema': 'string',
                'awsSecretStoreArn': 'string'
            }
        }
    }
}


Response Structure

(dict) --

dataSource (dict) --
The DataSource object.

dataSourceArn (string) --
The data source ARN.

name (string) --
The name of the data source.

description (string) --
The description of the data source.

type (string) --
The type of the data source.

AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
AWS_LAMBDA : The data source is an AWS Lambda function.
NONE : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
HTTP : The data source is an HTTP endpoint.
RELATIONAL_DATABASE : The data source is a relational database.


serviceRoleArn (string) --
The AWS IAM service role ARN for the data source. The system assumes this role when accessing the data source.

dynamodbConfig (dict) --
Amazon DynamoDB settings.

tableName (string) --
The table name.

awsRegion (string) --
The AWS Region.

useCallerCredentials (boolean) --
Set to TRUE to use Amazon Cognito credentials with this data source.

deltaSyncConfig (dict) --
The DeltaSyncConfig for a versioned datasource.

baseTableTTL (integer) --
The number of minutes an Item is stored in the datasource.

deltaSyncTableName (string) --
The Delta Sync table name.

deltaSyncTableTTL (integer) --
The number of minutes a Delta Sync log entry is stored in the Delta Sync table.



versioned (boolean) --
Set to TRUE to use Conflict Detection and Resolution with this data source.



lambdaConfig (dict) --
AWS Lambda settings.

lambdaFunctionArn (string) --
The ARN for the Lambda function.



elasticsearchConfig (dict) --
Amazon Elasticsearch Service settings.

endpoint (string) --
The endpoint.

awsRegion (string) --
The AWS Region.



httpConfig (dict) --
HTTP endpoint settings.

endpoint (string) --
The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.

authorizationConfig (dict) --
The authorization config in case the HTTP endpoint requires authorization.

authorizationType (string) --
The authorization type required by the HTTP endpoint.

AWS_IAM : The authorization type is Sigv4.


awsIamConfig (dict) --
The AWS IAM settings.

signingRegion (string) --
The signing region for AWS IAM authorization.

signingServiceName (string) --
The signing service name for AWS IAM authorization.







relationalDatabaseConfig (dict) --
Relational database settings.

relationalDatabaseSourceType (string) --
Source type for the relational database.

RDS_HTTP_ENDPOINT : The relational database source type is an Amazon RDS HTTP endpoint.


rdsHttpEndpointConfig (dict) --
Amazon RDS HTTP endpoint settings.

awsRegion (string) --
AWS Region for RDS HTTP endpoint.

dbClusterIdentifier (string) --
Amazon RDS cluster identifier.

databaseName (string) --
Logical database name.

schema (string) --
Logical schema name.

awsSecretStoreArn (string) --
AWS secret store ARN for database credentials.













Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'dataSource': {
            'dataSourceArn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
            'serviceRoleArn': 'string',
            'dynamodbConfig': {
                'tableName': 'string',
                'awsRegion': 'string',
                'useCallerCredentials': True|False,
                'deltaSyncConfig': {
                    'baseTableTTL': 123,
                    'deltaSyncTableName': 'string',
                    'deltaSyncTableTTL': 123
                },
                'versioned': True|False
            },
            'lambdaConfig': {
                'lambdaFunctionArn': 'string'
            },
            'elasticsearchConfig': {
                'endpoint': 'string',
                'awsRegion': 'string'
            },
            'httpConfig': {
                'endpoint': 'string',
                'authorizationConfig': {
                    'authorizationType': 'AWS_IAM',
                    'awsIamConfig': {
                        'signingRegion': 'string',
                        'signingServiceName': 'string'
                    }
                }
            },
            'relationalDatabaseConfig': {
                'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                'rdsHttpEndpointConfig': {
                    'awsRegion': 'string',
                    'dbClusterIdentifier': 'string',
                    'databaseName': 'string',
                    'schema': 'string',
                    'awsSecretStoreArn': 'string'
                }
            }
        }
    }
    
    
    :returns: 
    AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
    AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
    AWS_LAMBDA : The data source is an AWS Lambda function.
    NONE : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
    HTTP : The data source is an HTTP endpoint.
    RELATIONAL_DATABASE : The data source is a relational database.
    
    """
    pass

def get_function(apiId=None, functionId=None):
    """
    Get a Function .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_function(
        apiId='string',
        functionId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe GraphQL API ID.\n

    :type functionId: string
    :param functionId: [REQUIRED]\nThe Function ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'functionConfiguration': {
        'functionId': 'string',
        'functionArn': 'string',
        'name': 'string',
        'description': 'string',
        'dataSourceName': 'string',
        'requestMappingTemplate': 'string',
        'responseMappingTemplate': 'string',
        'functionVersion': 'string'
    }
}


Response Structure

(dict) --

functionConfiguration (dict) --
The Function object.

functionId (string) --
A unique ID representing the Function object.

functionArn (string) --
The ARN of the Function object.

name (string) --
The name of the Function object.

description (string) --
The Function description.

dataSourceName (string) --
The name of the DataSource .

requestMappingTemplate (string) --
The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.

responseMappingTemplate (string) --
The Function response mapping template.

functionVersion (string) --
The version of the request mapping template. Currently only the 2018-05-29 version of the template is supported.









Exceptions

AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException


    :return: {
        'functionConfiguration': {
            'functionId': 'string',
            'functionArn': 'string',
            'name': 'string',
            'description': 'string',
            'dataSourceName': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'functionVersion': 'string'
        }
    }
    
    
    :returns: 
    AppSync.Client.exceptions.ConcurrentModificationException
    AppSync.Client.exceptions.NotFoundException
    AppSync.Client.exceptions.UnauthorizedException
    
    """
    pass

def get_graphql_api(apiId=None):
    """
    Retrieves a GraphqlApi object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_graphql_api(
        apiId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID for the GraphQL API.\n

    :rtype: dict
ReturnsResponse Syntax{
    'graphqlApi': {
        'name': 'string',
        'apiId': 'string',
        'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
        'logConfig': {
            'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
            'cloudWatchLogsRoleArn': 'string',
            'excludeVerboseContent': True|False
        },
        'userPoolConfig': {
            'userPoolId': 'string',
            'awsRegion': 'string',
            'defaultAction': 'ALLOW'|'DENY',
            'appIdClientRegex': 'string'
        },
        'openIDConnectConfig': {
            'issuer': 'string',
            'clientId': 'string',
            'iatTTL': 123,
            'authTTL': 123
        },
        'arn': 'string',
        'uris': {
            'string': 'string'
        },
        'tags': {
            'string': 'string'
        },
        'additionalAuthenticationProviders': [
            {
                'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                'openIDConnectConfig': {
                    'issuer': 'string',
                    'clientId': 'string',
                    'iatTTL': 123,
                    'authTTL': 123
                },
                'userPoolConfig': {
                    'userPoolId': 'string',
                    'awsRegion': 'string',
                    'appIdClientRegex': 'string'
                }
            },
        ],
        'xrayEnabled': True|False
    }
}


Response Structure

(dict) --
graphqlApi (dict) --The GraphqlApi object.

name (string) --The API name.

apiId (string) --The API ID.

authenticationType (string) --The authentication type.

logConfig (dict) --The Amazon CloudWatch Logs configuration.

fieldLogLevel (string) --The field logging level. Values can be NONE, ERROR, or ALL.

NONE : No field-level logs are captured.
ERROR : Logs the following information only for the fields that are in error:
The error section in the server response.
Field-level errors.
The generated request/response functions that got resolved for error fields.


ALL : The following information is logged for all fields in the query:
Field-level tracing information.
The generated request/response functions that got resolved for each field.




cloudWatchLogsRoleArn (string) --The service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.

excludeVerboseContent (boolean) --Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.



userPoolConfig (dict) --The Amazon Cognito user pool configuration.

userPoolId (string) --The user pool ID.

awsRegion (string) --The AWS Region in which the user pool was created.

defaultAction (string) --The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn\'t match the Amazon Cognito user pool configuration.

appIdClientRegex (string) --A regular expression for validating the incoming Amazon Cognito user pool app client ID.



openIDConnectConfig (dict) --The OpenID Connect configuration.

issuer (string) --The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of iss in the ID token.

clientId (string) --The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.

iatTTL (integer) --The number of milliseconds a token is valid after being issued to a user.

authTTL (integer) --The number of milliseconds a token is valid after being authenticated.



arn (string) --The ARN.

uris (dict) --The URIs.

(string) --
(string) --




tags (dict) --The tags.

(string) --The key for the tag.

(string) --The value for the tag.





additionalAuthenticationProviders (list) --A list of additional authentication providers for the GraphqlApi API.

(dict) --Describes an additional authentication provider.

authenticationType (string) --The authentication type: API key, AWS IAM, OIDC, or Amazon Cognito user pools.

openIDConnectConfig (dict) --The OpenID Connect configuration.

issuer (string) --The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of iss in the ID token.

clientId (string) --The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.

iatTTL (integer) --The number of milliseconds a token is valid after being issued to a user.

authTTL (integer) --The number of milliseconds a token is valid after being authenticated.



userPoolConfig (dict) --The Amazon Cognito user pool configuration.

userPoolId (string) --The user pool ID.

awsRegion (string) --The AWS Region in which the user pool was created.

appIdClientRegex (string) --A regular expression for validating the incoming Amazon Cognito user pool app client ID.







xrayEnabled (boolean) --A flag representing whether X-Ray tracing is enabled for this GraphqlApi .








Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException
AppSync.Client.exceptions.AccessDeniedException


    :return: {
        'graphqlApi': {
            'name': 'string',
            'apiId': 'string',
            'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
            'logConfig': {
                'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                'cloudWatchLogsRoleArn': 'string',
                'excludeVerboseContent': True|False
            },
            'userPoolConfig': {
                'userPoolId': 'string',
                'awsRegion': 'string',
                'defaultAction': 'ALLOW'|'DENY',
                'appIdClientRegex': 'string'
            },
            'openIDConnectConfig': {
                'issuer': 'string',
                'clientId': 'string',
                'iatTTL': 123,
                'authTTL': 123
            },
            'arn': 'string',
            'uris': {
                'string': 'string'
            },
            'tags': {
                'string': 'string'
            },
            'additionalAuthenticationProviders': [
                {
                    'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                    'openIDConnectConfig': {
                        'issuer': 'string',
                        'clientId': 'string',
                        'iatTTL': 123,
                        'authTTL': 123
                    },
                    'userPoolConfig': {
                        'userPoolId': 'string',
                        'awsRegion': 'string',
                        'appIdClientRegex': 'string'
                    }
                },
            ],
            'xrayEnabled': True|False
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_introspection_schema(apiId=None, format=None, includeDirectives=None):
    """
    Retrieves the introspection schema for a GraphQL API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_introspection_schema(
        apiId='string',
        format='SDL'|'JSON',
        includeDirectives=True|False
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type format: string
    :param format: [REQUIRED]\nThe schema format: SDL or JSON.\n

    :type includeDirectives: boolean
    :param includeDirectives: A flag that specifies whether the schema introspection should contain directives.

    :rtype: dict

ReturnsResponse Syntax
{
    'schema': StreamingBody()
}


Response Structure

(dict) --

schema (StreamingBody) --
The schema, in GraphQL Schema Definition Language (SDL) format.
For more information, see the GraphQL SDL documentation .







Exceptions

AppSync.Client.exceptions.GraphQLSchemaException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'schema': StreamingBody()
    }
    
    
    :returns: 
    AppSync.Client.exceptions.GraphQLSchemaException
    AppSync.Client.exceptions.NotFoundException
    AppSync.Client.exceptions.UnauthorizedException
    AppSync.Client.exceptions.InternalFailureException
    
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

def get_resolver(apiId=None, typeName=None, fieldName=None):
    """
    Retrieves a Resolver object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resolver(
        apiId='string',
        typeName='string',
        fieldName='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type typeName: string
    :param typeName: [REQUIRED]\nThe resolver type name.\n

    :type fieldName: string
    :param fieldName: [REQUIRED]\nThe resolver field name.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'resolver': {
        'typeName': 'string',
        'fieldName': 'string',
        'dataSourceName': 'string',
        'resolverArn': 'string',
        'requestMappingTemplate': 'string',
        'responseMappingTemplate': 'string',
        'kind': 'UNIT'|'PIPELINE',
        'pipelineConfig': {
            'functions': [
                'string',
            ]
        },
        'syncConfig': {
            'conflictHandler': 'OPTIMISTIC_CONCURRENCY'|'LAMBDA'|'AUTOMERGE'|'NONE',
            'conflictDetection': 'VERSION'|'NONE',
            'lambdaConflictHandlerConfig': {
                'lambdaConflictHandlerArn': 'string'
            }
        },
        'cachingConfig': {
            'ttl': 123,
            'cachingKeys': [
                'string',
            ]
        }
    }
}


Response Structure

(dict) --

resolver (dict) --
The Resolver object.

typeName (string) --
The resolver type name.

fieldName (string) --
The resolver field name.

dataSourceName (string) --
The resolver data source name.

resolverArn (string) --
The resolver ARN.

requestMappingTemplate (string) --
The request mapping template.

responseMappingTemplate (string) --
The response mapping template.

kind (string) --
The resolver type.

UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.


pipelineConfig (dict) --
The PipelineConfig .

functions (list) --
A list of Function objects.

(string) --




syncConfig (dict) --
The SyncConfig for a resolver attached to a versioned datasource.

conflictHandler (string) --
The Conflict Resolution strategy to perform in the event of a conflict.

OPTIMISTIC_CONCURRENCY : Resolve conflicts by rejecting mutations when versions do not match the latest version at the server.
AUTOMERGE : Resolve conflicts with the Automerge conflict resolution strategy.
LAMBDA : Resolve conflicts with a Lambda function supplied in the LambdaConflictHandlerConfig.


conflictDetection (string) --
The Conflict Detection strategy to use.

VERSION : Detect conflicts based on object versions for this resolver.
NONE : Do not detect conflicts when executing this resolver.


lambdaConflictHandlerConfig (dict) --
The LambdaConflictHandlerConfig when configuring LAMBDA as the Conflict Handler.

lambdaConflictHandlerArn (string) --
The Arn for the Lambda function to use as the Conflict Handler.





cachingConfig (dict) --
The caching configuration for the resolver.

ttl (integer) --
The TTL in seconds for a resolver that has caching enabled.
Valid values are between 1 and 3600 seconds.

cachingKeys (list) --
The caching keys for a resolver that has caching enabled.
Valid values are entries from the $context.identity and $context.arguments maps.

(string) --












Exceptions

AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException


    :return: {
        'resolver': {
            'typeName': 'string',
            'fieldName': 'string',
            'dataSourceName': 'string',
            'resolverArn': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'kind': 'UNIT'|'PIPELINE',
            'pipelineConfig': {
                'functions': [
                    'string',
                ]
            },
            'syncConfig': {
                'conflictHandler': 'OPTIMISTIC_CONCURRENCY'|'LAMBDA'|'AUTOMERGE'|'NONE',
                'conflictDetection': 'VERSION'|'NONE',
                'lambdaConflictHandlerConfig': {
                    'lambdaConflictHandlerArn': 'string'
                }
            },
            'cachingConfig': {
                'ttl': 123,
                'cachingKeys': [
                    'string',
                ]
            }
        }
    }
    
    
    :returns: 
    UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
    PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.
    
    """
    pass

def get_schema_creation_status(apiId=None):
    """
    Retrieves the current status of a schema creation operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_schema_creation_status(
        apiId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'status': 'PROCESSING'|'ACTIVE'|'DELETING'|'FAILED'|'SUCCESS'|'NOT_APPLICABLE',
    'details': 'string'
}


Response Structure

(dict) --
status (string) --The current state of the schema (PROCESSING, FAILED, SUCCESS, or NOT_APPLICABLE). When the schema is in the ACTIVE state, you can add data.

details (string) --Detailed information about the status of the schema creation operation.






Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'status': 'PROCESSING'|'ACTIVE'|'DELETING'|'FAILED'|'SUCCESS'|'NOT_APPLICABLE',
        'details': 'string'
    }
    
    
    """
    pass

def get_type(apiId=None, typeName=None, format=None):
    """
    Retrieves a Type object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_type(
        apiId='string',
        typeName='string',
        format='SDL'|'JSON'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type typeName: string
    :param typeName: [REQUIRED]\nThe type name.\n

    :type format: string
    :param format: [REQUIRED]\nThe type format: SDL or JSON.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'type': {
        'name': 'string',
        'description': 'string',
        'arn': 'string',
        'definition': 'string',
        'format': 'SDL'|'JSON'
    }
}


Response Structure

(dict) --

type (dict) --
The Type object.

name (string) --
The type name.

description (string) --
The type description.

arn (string) --
The type ARN.

definition (string) --
The type definition.

format (string) --
The type format: SDL or JSON.









Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'type': {
            'name': 'string',
            'description': 'string',
            'arn': 'string',
            'definition': 'string',
            'format': 'SDL'|'JSON'
        }
    }
    
    
    :returns: 
    AppSync.Client.exceptions.BadRequestException
    AppSync.Client.exceptions.ConcurrentModificationException
    AppSync.Client.exceptions.NotFoundException
    AppSync.Client.exceptions.UnauthorizedException
    AppSync.Client.exceptions.InternalFailureException
    
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

def list_api_keys(apiId=None, nextToken=None, maxResults=None):
    """
    Lists the API keys for a given API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_api_keys(
        apiId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'apiKeys': [
        {
            'id': 'string',
            'description': 'string',
            'expires': 123
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

apiKeys (list) --
The ApiKey objects.

(dict) --
Describes an API key.
Customers invoke AWS AppSync GraphQL API operations with API keys as an identity mechanism. There are two key versions:

da1 : This version was introduced at launch in November 2017. These keys always expire after 7 days. Key expiration is managed by Amazon DynamoDB TTL. The keys ceased to be valid after February 21, 2018 and should not be used after that date.


ListApiKeys returns the expiration time in milliseconds.
CreateApiKey returns the expiration time in milliseconds.
UpdateApiKey is not available for this key version.
DeleteApiKey deletes the item from the table.
Expiration is stored in Amazon DynamoDB as milliseconds. This results in a bug where keys are not automatically deleted because DynamoDB expects the TTL to be stored in seconds. As a one-time action, we will delete these keys from the table after February 21, 2018.


da2 : This version was introduced in February 2018 when AppSync added support to extend key expiration.


ListApiKeys returns the expiration time in seconds.
CreateApiKey returns the expiration time in seconds and accepts a user-provided expiration time in seconds.
UpdateApiKey returns the expiration time in seconds and accepts a user-provided expiration time in seconds. Key expiration can only be updated while the key has not expired.
DeleteApiKey deletes the item from the table.
Expiration is stored in Amazon DynamoDB as seconds.


id (string) --
The API key ID.

description (string) --
A description of the purpose of the API key.

expires (integer) --
The time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour.





nextToken (string) --
An identifier to be passed in the next request to this operation to return the next set of items in the list.







Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'apiKeys': [
            {
                'id': 'string',
                'description': 'string',
                'expires': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    ListApiKeys returns the expiration time in milliseconds.
    CreateApiKey returns the expiration time in milliseconds.
    UpdateApiKey is not available for this key version.
    DeleteApiKey deletes the item from the table.
    Expiration is stored in Amazon DynamoDB as milliseconds. This results in a bug where keys are not automatically deleted because DynamoDB expects the TTL to be stored in seconds. As a one-time action, we will delete these keys from the table after February 21, 2018.
    
    """
    pass

def list_data_sources(apiId=None, nextToken=None, maxResults=None):
    """
    Lists the data sources for a given API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_data_sources(
        apiId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'dataSources': [
        {
            'dataSourceArn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
            'serviceRoleArn': 'string',
            'dynamodbConfig': {
                'tableName': 'string',
                'awsRegion': 'string',
                'useCallerCredentials': True|False,
                'deltaSyncConfig': {
                    'baseTableTTL': 123,
                    'deltaSyncTableName': 'string',
                    'deltaSyncTableTTL': 123
                },
                'versioned': True|False
            },
            'lambdaConfig': {
                'lambdaFunctionArn': 'string'
            },
            'elasticsearchConfig': {
                'endpoint': 'string',
                'awsRegion': 'string'
            },
            'httpConfig': {
                'endpoint': 'string',
                'authorizationConfig': {
                    'authorizationType': 'AWS_IAM',
                    'awsIamConfig': {
                        'signingRegion': 'string',
                        'signingServiceName': 'string'
                    }
                }
            },
            'relationalDatabaseConfig': {
                'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                'rdsHttpEndpointConfig': {
                    'awsRegion': 'string',
                    'dbClusterIdentifier': 'string',
                    'databaseName': 'string',
                    'schema': 'string',
                    'awsSecretStoreArn': 'string'
                }
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

dataSources (list) --
The DataSource objects.

(dict) --
Describes a data source.

dataSourceArn (string) --
The data source ARN.

name (string) --
The name of the data source.

description (string) --
The description of the data source.

type (string) --
The type of the data source.

AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
AWS_LAMBDA : The data source is an AWS Lambda function.
NONE : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
HTTP : The data source is an HTTP endpoint.
RELATIONAL_DATABASE : The data source is a relational database.


serviceRoleArn (string) --
The AWS IAM service role ARN for the data source. The system assumes this role when accessing the data source.

dynamodbConfig (dict) --
Amazon DynamoDB settings.

tableName (string) --
The table name.

awsRegion (string) --
The AWS Region.

useCallerCredentials (boolean) --
Set to TRUE to use Amazon Cognito credentials with this data source.

deltaSyncConfig (dict) --
The DeltaSyncConfig for a versioned datasource.

baseTableTTL (integer) --
The number of minutes an Item is stored in the datasource.

deltaSyncTableName (string) --
The Delta Sync table name.

deltaSyncTableTTL (integer) --
The number of minutes a Delta Sync log entry is stored in the Delta Sync table.



versioned (boolean) --
Set to TRUE to use Conflict Detection and Resolution with this data source.



lambdaConfig (dict) --
AWS Lambda settings.

lambdaFunctionArn (string) --
The ARN for the Lambda function.



elasticsearchConfig (dict) --
Amazon Elasticsearch Service settings.

endpoint (string) --
The endpoint.

awsRegion (string) --
The AWS Region.



httpConfig (dict) --
HTTP endpoint settings.

endpoint (string) --
The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.

authorizationConfig (dict) --
The authorization config in case the HTTP endpoint requires authorization.

authorizationType (string) --
The authorization type required by the HTTP endpoint.

AWS_IAM : The authorization type is Sigv4.


awsIamConfig (dict) --
The AWS IAM settings.

signingRegion (string) --
The signing region for AWS IAM authorization.

signingServiceName (string) --
The signing service name for AWS IAM authorization.







relationalDatabaseConfig (dict) --
Relational database settings.

relationalDatabaseSourceType (string) --
Source type for the relational database.

RDS_HTTP_ENDPOINT : The relational database source type is an Amazon RDS HTTP endpoint.


rdsHttpEndpointConfig (dict) --
Amazon RDS HTTP endpoint settings.

awsRegion (string) --
AWS Region for RDS HTTP endpoint.

dbClusterIdentifier (string) --
Amazon RDS cluster identifier.

databaseName (string) --
Logical database name.

schema (string) --
Logical schema name.

awsSecretStoreArn (string) --
AWS secret store ARN for database credentials.









nextToken (string) --
An identifier to be passed in the next request to this operation to return the next set of items in the list.







Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'dataSources': [
            {
                'dataSourceArn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
                'serviceRoleArn': 'string',
                'dynamodbConfig': {
                    'tableName': 'string',
                    'awsRegion': 'string',
                    'useCallerCredentials': True|False,
                    'deltaSyncConfig': {
                        'baseTableTTL': 123,
                        'deltaSyncTableName': 'string',
                        'deltaSyncTableTTL': 123
                    },
                    'versioned': True|False
                },
                'lambdaConfig': {
                    'lambdaFunctionArn': 'string'
                },
                'elasticsearchConfig': {
                    'endpoint': 'string',
                    'awsRegion': 'string'
                },
                'httpConfig': {
                    'endpoint': 'string',
                    'authorizationConfig': {
                        'authorizationType': 'AWS_IAM',
                        'awsIamConfig': {
                            'signingRegion': 'string',
                            'signingServiceName': 'string'
                        }
                    }
                },
                'relationalDatabaseConfig': {
                    'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                    'rdsHttpEndpointConfig': {
                        'awsRegion': 'string',
                        'dbClusterIdentifier': 'string',
                        'databaseName': 'string',
                        'schema': 'string',
                        'awsSecretStoreArn': 'string'
                    }
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
    AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
    AWS_LAMBDA : The data source is an AWS Lambda function.
    NONE : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
    HTTP : The data source is an HTTP endpoint.
    RELATIONAL_DATABASE : The data source is a relational database.
    
    """
    pass

def list_functions(apiId=None, nextToken=None, maxResults=None):
    """
    List multiple functions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_functions(
        apiId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe GraphQL API ID.\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'functions': [
        {
            'functionId': 'string',
            'functionArn': 'string',
            'name': 'string',
            'description': 'string',
            'dataSourceName': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'functionVersion': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

functions (list) --
A list of Function objects.

(dict) --
A function is a reusable entity. Multiple functions can be used to compose the resolver logic.

functionId (string) --
A unique ID representing the Function object.

functionArn (string) --
The ARN of the Function object.

name (string) --
The name of the Function object.

description (string) --
The Function description.

dataSourceName (string) --
The name of the DataSource .

requestMappingTemplate (string) --
The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.

responseMappingTemplate (string) --
The Function response mapping template.

functionVersion (string) --
The version of the request mapping template. Currently only the 2018-05-29 version of the template is supported.





nextToken (string) --
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.







Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'functions': [
            {
                'functionId': 'string',
                'functionArn': 'string',
                'name': 'string',
                'description': 'string',
                'dataSourceName': 'string',
                'requestMappingTemplate': 'string',
                'responseMappingTemplate': 'string',
                'functionVersion': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    AppSync.Client.exceptions.BadRequestException
    AppSync.Client.exceptions.NotFoundException
    AppSync.Client.exceptions.UnauthorizedException
    AppSync.Client.exceptions.InternalFailureException
    
    """
    pass

def list_graphql_apis(nextToken=None, maxResults=None):
    """
    Lists your GraphQL APIs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_graphql_apis(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'graphqlApis': [
        {
            'name': 'string',
            'apiId': 'string',
            'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
            'logConfig': {
                'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                'cloudWatchLogsRoleArn': 'string',
                'excludeVerboseContent': True|False
            },
            'userPoolConfig': {
                'userPoolId': 'string',
                'awsRegion': 'string',
                'defaultAction': 'ALLOW'|'DENY',
                'appIdClientRegex': 'string'
            },
            'openIDConnectConfig': {
                'issuer': 'string',
                'clientId': 'string',
                'iatTTL': 123,
                'authTTL': 123
            },
            'arn': 'string',
            'uris': {
                'string': 'string'
            },
            'tags': {
                'string': 'string'
            },
            'additionalAuthenticationProviders': [
                {
                    'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                    'openIDConnectConfig': {
                        'issuer': 'string',
                        'clientId': 'string',
                        'iatTTL': 123,
                        'authTTL': 123
                    },
                    'userPoolConfig': {
                        'userPoolId': 'string',
                        'awsRegion': 'string',
                        'appIdClientRegex': 'string'
                    }
                },
            ],
            'xrayEnabled': True|False
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

graphqlApis (list) --
The GraphqlApi objects.

(dict) --
Describes a GraphQL API.

name (string) --
The API name.

apiId (string) --
The API ID.

authenticationType (string) --
The authentication type.

logConfig (dict) --
The Amazon CloudWatch Logs configuration.

fieldLogLevel (string) --
The field logging level. Values can be NONE, ERROR, or ALL.

NONE : No field-level logs are captured.
ERROR : Logs the following information only for the fields that are in error:
The error section in the server response.
Field-level errors.
The generated request/response functions that got resolved for error fields.


ALL : The following information is logged for all fields in the query:
Field-level tracing information.
The generated request/response functions that got resolved for each field.




cloudWatchLogsRoleArn (string) --
The service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.

excludeVerboseContent (boolean) --
Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.



userPoolConfig (dict) --
The Amazon Cognito user pool configuration.

userPoolId (string) --
The user pool ID.

awsRegion (string) --
The AWS Region in which the user pool was created.

defaultAction (string) --
The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn\'t match the Amazon Cognito user pool configuration.

appIdClientRegex (string) --
A regular expression for validating the incoming Amazon Cognito user pool app client ID.



openIDConnectConfig (dict) --
The OpenID Connect configuration.

issuer (string) --
The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of iss in the ID token.

clientId (string) --
The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.

iatTTL (integer) --
The number of milliseconds a token is valid after being issued to a user.

authTTL (integer) --
The number of milliseconds a token is valid after being authenticated.



arn (string) --
The ARN.

uris (dict) --
The URIs.

(string) --
(string) --




tags (dict) --
The tags.

(string) --
The key for the tag.

(string) --
The value for the tag.





additionalAuthenticationProviders (list) --
A list of additional authentication providers for the GraphqlApi API.

(dict) --
Describes an additional authentication provider.

authenticationType (string) --
The authentication type: API key, AWS IAM, OIDC, or Amazon Cognito user pools.

openIDConnectConfig (dict) --
The OpenID Connect configuration.

issuer (string) --
The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of iss in the ID token.

clientId (string) --
The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.

iatTTL (integer) --
The number of milliseconds a token is valid after being issued to a user.

authTTL (integer) --
The number of milliseconds a token is valid after being authenticated.



userPoolConfig (dict) --
The Amazon Cognito user pool configuration.

userPoolId (string) --
The user pool ID.

awsRegion (string) --
The AWS Region in which the user pool was created.

appIdClientRegex (string) --
A regular expression for validating the incoming Amazon Cognito user pool app client ID.







xrayEnabled (boolean) --
A flag representing whether X-Ray tracing is enabled for this GraphqlApi .





nextToken (string) --
An identifier to be passed in the next request to this operation to return the next set of items in the list.







Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'graphqlApis': [
            {
                'name': 'string',
                'apiId': 'string',
                'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                'logConfig': {
                    'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                    'cloudWatchLogsRoleArn': 'string',
                    'excludeVerboseContent': True|False
                },
                'userPoolConfig': {
                    'userPoolId': 'string',
                    'awsRegion': 'string',
                    'defaultAction': 'ALLOW'|'DENY',
                    'appIdClientRegex': 'string'
                },
                'openIDConnectConfig': {
                    'issuer': 'string',
                    'clientId': 'string',
                    'iatTTL': 123,
                    'authTTL': 123
                },
                'arn': 'string',
                'uris': {
                    'string': 'string'
                },
                'tags': {
                    'string': 'string'
                },
                'additionalAuthenticationProviders': [
                    {
                        'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                        'openIDConnectConfig': {
                            'issuer': 'string',
                            'clientId': 'string',
                            'iatTTL': 123,
                            'authTTL': 123
                        },
                        'userPoolConfig': {
                            'userPoolId': 'string',
                            'awsRegion': 'string',
                            'appIdClientRegex': 'string'
                        }
                    },
                ],
                'xrayEnabled': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    NONE : No field-level logs are captured.
    ERROR : Logs the following information only for the fields that are in error:
    The error section in the server response.
    Field-level errors.
    The generated request/response functions that got resolved for error fields.
    
    
    ALL : The following information is logged for all fields in the query:
    Field-level tracing information.
    The generated request/response functions that got resolved for each field.
    
    
    
    """
    pass

def list_resolvers(apiId=None, typeName=None, nextToken=None, maxResults=None):
    """
    Lists the resolvers for a given API and type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resolvers(
        apiId='string',
        typeName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type typeName: string
    :param typeName: [REQUIRED]\nThe type name.\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'resolvers': [
        {
            'typeName': 'string',
            'fieldName': 'string',
            'dataSourceName': 'string',
            'resolverArn': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'kind': 'UNIT'|'PIPELINE',
            'pipelineConfig': {
                'functions': [
                    'string',
                ]
            },
            'syncConfig': {
                'conflictHandler': 'OPTIMISTIC_CONCURRENCY'|'LAMBDA'|'AUTOMERGE'|'NONE',
                'conflictDetection': 'VERSION'|'NONE',
                'lambdaConflictHandlerConfig': {
                    'lambdaConflictHandlerArn': 'string'
                }
            },
            'cachingConfig': {
                'ttl': 123,
                'cachingKeys': [
                    'string',
                ]
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

resolvers (list) --
The Resolver objects.

(dict) --
Describes a resolver.

typeName (string) --
The resolver type name.

fieldName (string) --
The resolver field name.

dataSourceName (string) --
The resolver data source name.

resolverArn (string) --
The resolver ARN.

requestMappingTemplate (string) --
The request mapping template.

responseMappingTemplate (string) --
The response mapping template.

kind (string) --
The resolver type.

UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.


pipelineConfig (dict) --
The PipelineConfig .

functions (list) --
A list of Function objects.

(string) --




syncConfig (dict) --
The SyncConfig for a resolver attached to a versioned datasource.

conflictHandler (string) --
The Conflict Resolution strategy to perform in the event of a conflict.

OPTIMISTIC_CONCURRENCY : Resolve conflicts by rejecting mutations when versions do not match the latest version at the server.
AUTOMERGE : Resolve conflicts with the Automerge conflict resolution strategy.
LAMBDA : Resolve conflicts with a Lambda function supplied in the LambdaConflictHandlerConfig.


conflictDetection (string) --
The Conflict Detection strategy to use.

VERSION : Detect conflicts based on object versions for this resolver.
NONE : Do not detect conflicts when executing this resolver.


lambdaConflictHandlerConfig (dict) --
The LambdaConflictHandlerConfig when configuring LAMBDA as the Conflict Handler.

lambdaConflictHandlerArn (string) --
The Arn for the Lambda function to use as the Conflict Handler.





cachingConfig (dict) --
The caching configuration for the resolver.

ttl (integer) --
The TTL in seconds for a resolver that has caching enabled.
Valid values are between 1 and 3600 seconds.

cachingKeys (list) --
The caching keys for a resolver that has caching enabled.
Valid values are entries from the $context.identity and $context.arguments maps.

(string) --








nextToken (string) --
An identifier to be passed in the next request to this operation to return the next set of items in the list.







Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'resolvers': [
            {
                'typeName': 'string',
                'fieldName': 'string',
                'dataSourceName': 'string',
                'resolverArn': 'string',
                'requestMappingTemplate': 'string',
                'responseMappingTemplate': 'string',
                'kind': 'UNIT'|'PIPELINE',
                'pipelineConfig': {
                    'functions': [
                        'string',
                    ]
                },
                'syncConfig': {
                    'conflictHandler': 'OPTIMISTIC_CONCURRENCY'|'LAMBDA'|'AUTOMERGE'|'NONE',
                    'conflictDetection': 'VERSION'|'NONE',
                    'lambdaConflictHandlerConfig': {
                        'lambdaConflictHandlerArn': 'string'
                    }
                },
                'cachingConfig': {
                    'ttl': 123,
                    'cachingKeys': [
                        'string',
                    ]
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
    PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.
    
    """
    pass

def list_resolvers_by_function(apiId=None, functionId=None, nextToken=None, maxResults=None):
    """
    List the resolvers that are associated with a specific function.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resolvers_by_function(
        apiId='string',
        functionId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type functionId: string
    :param functionId: [REQUIRED]\nThe Function ID.\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'resolvers': [
        {
            'typeName': 'string',
            'fieldName': 'string',
            'dataSourceName': 'string',
            'resolverArn': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'kind': 'UNIT'|'PIPELINE',
            'pipelineConfig': {
                'functions': [
                    'string',
                ]
            },
            'syncConfig': {
                'conflictHandler': 'OPTIMISTIC_CONCURRENCY'|'LAMBDA'|'AUTOMERGE'|'NONE',
                'conflictDetection': 'VERSION'|'NONE',
                'lambdaConflictHandlerConfig': {
                    'lambdaConflictHandlerArn': 'string'
                }
            },
            'cachingConfig': {
                'ttl': 123,
                'cachingKeys': [
                    'string',
                ]
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

resolvers (list) --
The list of resolvers.

(dict) --
Describes a resolver.

typeName (string) --
The resolver type name.

fieldName (string) --
The resolver field name.

dataSourceName (string) --
The resolver data source name.

resolverArn (string) --
The resolver ARN.

requestMappingTemplate (string) --
The request mapping template.

responseMappingTemplate (string) --
The response mapping template.

kind (string) --
The resolver type.

UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.


pipelineConfig (dict) --
The PipelineConfig .

functions (list) --
A list of Function objects.

(string) --




syncConfig (dict) --
The SyncConfig for a resolver attached to a versioned datasource.

conflictHandler (string) --
The Conflict Resolution strategy to perform in the event of a conflict.

OPTIMISTIC_CONCURRENCY : Resolve conflicts by rejecting mutations when versions do not match the latest version at the server.
AUTOMERGE : Resolve conflicts with the Automerge conflict resolution strategy.
LAMBDA : Resolve conflicts with a Lambda function supplied in the LambdaConflictHandlerConfig.


conflictDetection (string) --
The Conflict Detection strategy to use.

VERSION : Detect conflicts based on object versions for this resolver.
NONE : Do not detect conflicts when executing this resolver.


lambdaConflictHandlerConfig (dict) --
The LambdaConflictHandlerConfig when configuring LAMBDA as the Conflict Handler.

lambdaConflictHandlerArn (string) --
The Arn for the Lambda function to use as the Conflict Handler.





cachingConfig (dict) --
The caching configuration for the resolver.

ttl (integer) --
The TTL in seconds for a resolver that has caching enabled.
Valid values are between 1 and 3600 seconds.

cachingKeys (list) --
The caching keys for a resolver that has caching enabled.
Valid values are entries from the $context.identity and $context.arguments maps.

(string) --








nextToken (string) --
An identifier that can be used to return the next set of items in the list.







Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'resolvers': [
            {
                'typeName': 'string',
                'fieldName': 'string',
                'dataSourceName': 'string',
                'resolverArn': 'string',
                'requestMappingTemplate': 'string',
                'responseMappingTemplate': 'string',
                'kind': 'UNIT'|'PIPELINE',
                'pipelineConfig': {
                    'functions': [
                        'string',
                    ]
                },
                'syncConfig': {
                    'conflictHandler': 'OPTIMISTIC_CONCURRENCY'|'LAMBDA'|'AUTOMERGE'|'NONE',
                    'conflictDetection': 'VERSION'|'NONE',
                    'lambdaConflictHandlerConfig': {
                        'lambdaConflictHandlerArn': 'string'
                    }
                },
                'cachingConfig': {
                    'ttl': 123,
                    'cachingKeys': [
                        'string',
                    ]
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
    PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    Lists the tags for a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe GraphqlApi ARN.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
tags (dict) --A TagMap object.

(string) --The key for the tag.

(string) --The value for the tag.










Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.LimitExceededException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException
AppSync.Client.exceptions.AccessDeniedException


    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    """
    pass

def list_types(apiId=None, format=None, nextToken=None, maxResults=None):
    """
    Lists the types for a given API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_types(
        apiId='string',
        format='SDL'|'JSON',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type format: string
    :param format: [REQUIRED]\nThe type format: SDL or JSON.\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'types': [
        {
            'name': 'string',
            'description': 'string',
            'arn': 'string',
            'definition': 'string',
            'format': 'SDL'|'JSON'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

types (list) --
The Type objects.

(dict) --
Describes a type.

name (string) --
The type name.

description (string) --
The type description.

arn (string) --
The type ARN.

definition (string) --
The type definition.

format (string) --
The type format: SDL or JSON.





nextToken (string) --
An identifier to be passed in the next request to this operation to return the next set of items in the list.







Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'types': [
            {
                'name': 'string',
                'description': 'string',
                'arn': 'string',
                'definition': 'string',
                'format': 'SDL'|'JSON'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    AppSync.Client.exceptions.BadRequestException
    AppSync.Client.exceptions.ConcurrentModificationException
    AppSync.Client.exceptions.NotFoundException
    AppSync.Client.exceptions.UnauthorizedException
    AppSync.Client.exceptions.InternalFailureException
    
    """
    pass

def start_schema_creation(apiId=None, definition=None):
    """
    Adds a new schema to your GraphQL API.
    This operation is asynchronous. Use to determine when it has completed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_schema_creation(
        apiId='string',
        definition=b'bytes'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type definition: bytes
    :param definition: [REQUIRED]\nThe schema definition, in GraphQL schema language format.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'status': 'PROCESSING'|'ACTIVE'|'DELETING'|'FAILED'|'SUCCESS'|'NOT_APPLICABLE'
}


Response Structure

(dict) --

status (string) --
The current state of the schema (PROCESSING, FAILED, SUCCESS, or NOT_APPLICABLE). When the schema is in the ACTIVE state, you can add data.







Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'status': 'PROCESSING'|'ACTIVE'|'DELETING'|'FAILED'|'SUCCESS'|'NOT_APPLICABLE'
    }
    
    
    :returns: 
    AppSync.Client.exceptions.BadRequestException
    AppSync.Client.exceptions.ConcurrentModificationException
    AppSync.Client.exceptions.NotFoundException
    AppSync.Client.exceptions.UnauthorizedException
    AppSync.Client.exceptions.InternalFailureException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Tags a resource with user-supplied tags.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe GraphqlApi ARN.\n

    :type tags: dict
    :param tags: [REQUIRED]\nA TagMap object.\n\n(string) --The key for the tag.\n\n(string) --The value for the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.LimitExceededException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException
AppSync.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Untags a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe GraphqlApi ARN.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nA list of TagKey objects.\n\n(string) --The key for the tag.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.LimitExceededException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException
AppSync.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_api_cache(apiId=None, ttl=None, apiCachingBehavior=None, type=None):
    """
    Updates the cache for the GraphQL API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_api_cache(
        apiId='string',
        ttl=123,
        apiCachingBehavior='FULL_REQUEST_CACHING'|'PER_RESOLVER_CACHING',
        type='T2_SMALL'|'T2_MEDIUM'|'R4_LARGE'|'R4_XLARGE'|'R4_2XLARGE'|'R4_4XLARGE'|'R4_8XLARGE'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe GraphQL API Id.\n

    :type ttl: integer
    :param ttl: [REQUIRED]\nTTL in seconds for cache entries.\nValid values are between 1 and 3600 seconds.\n

    :type apiCachingBehavior: string
    :param apiCachingBehavior: [REQUIRED]\nCaching behavior.\n\nFULL_REQUEST_CACHING : All requests are fully cached.\nPER_RESOLVER_CACHING : Individual resovlers that you specify are cached.\n\n

    :type type: string
    :param type: [REQUIRED]\nThe cache instance type.\n\nT2_SMALL : A t2.small instance type.\nT2_MEDIUM : A t2.medium instance type.\nR4_LARGE : A r4.large instance type.\nR4_XLARGE : A r4.xlarge instance type.\nR4_2XLARGE : A r4.2xlarge instance type.\nR4_4XLARGE : A r4.4xlarge instance type.\nR4_8XLARGE : A r4.8xlarge instance type.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'apiCache': {
        'ttl': 123,
        'apiCachingBehavior': 'FULL_REQUEST_CACHING'|'PER_RESOLVER_CACHING',
        'transitEncryptionEnabled': True|False,
        'atRestEncryptionEnabled': True|False,
        'type': 'T2_SMALL'|'T2_MEDIUM'|'R4_LARGE'|'R4_XLARGE'|'R4_2XLARGE'|'R4_4XLARGE'|'R4_8XLARGE',
        'status': 'AVAILABLE'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'
    }
}


Response Structure

(dict) --
Represents the output of a UpdateApiCache operation.

apiCache (dict) --
The ApiCache object.

ttl (integer) --
TTL in seconds for cache entries.
Valid values are between 1 and 3600 seconds.

apiCachingBehavior (string) --
Caching behavior.

FULL_REQUEST_CACHING : All requests are fully cached.
PER_RESOLVER_CACHING : Individual resovlers that you specify are cached.


transitEncryptionEnabled (boolean) --
Transit encryption flag when connecting to cache. This setting cannot be updated after creation.

atRestEncryptionEnabled (boolean) --
At rest encryption flag for cache. This setting cannot be updated after creation.

type (string) --
The cache instance type.

T2_SMALL : A t2.small instance type.
T2_MEDIUM : A t2.medium instance type.
R4_LARGE : A r4.large instance type.
R4_XLARGE : A r4.xlarge instance type.
R4_2XLARGE : A r4.2xlarge instance type.
R4_4XLARGE : A r4.4xlarge instance type.
R4_8XLARGE : A r4.8xlarge instance type.


status (string) --
The cache instance status.

AVAILABLE : The instance is available for use.
CREATING : The instance is currently creating.
DELETING : The instance is currently deleting.
MODIFYING : The instance is currently modifying.
FAILED : The instance has failed creation.










Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'apiCache': {
            'ttl': 123,
            'apiCachingBehavior': 'FULL_REQUEST_CACHING'|'PER_RESOLVER_CACHING',
            'transitEncryptionEnabled': True|False,
            'atRestEncryptionEnabled': True|False,
            'type': 'T2_SMALL'|'T2_MEDIUM'|'R4_LARGE'|'R4_XLARGE'|'R4_2XLARGE'|'R4_4XLARGE'|'R4_8XLARGE',
            'status': 'AVAILABLE'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'
        }
    }
    
    
    :returns: 
    FULL_REQUEST_CACHING : All requests are fully cached.
    PER_RESOLVER_CACHING : Individual resovlers that you specify are cached.
    
    """
    pass

def update_api_key(apiId=None, id=None, description=None, expires=None):
    """
    Updates an API key.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_api_key(
        apiId='string',
        id='string',
        description='string',
        expires=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe ID for the GraphQL API.\n

    :type id: string
    :param id: [REQUIRED]\nThe API key ID.\n

    :type description: string
    :param description: A description of the purpose of the API key.

    :type expires: integer
    :param expires: The time from update time after which the API key expires. The date is represented as seconds since the epoch. For more information, see .

    :rtype: dict

ReturnsResponse Syntax
{
    'apiKey': {
        'id': 'string',
        'description': 'string',
        'expires': 123
    }
}


Response Structure

(dict) --

apiKey (dict) --
The API key.

id (string) --
The API key ID.

description (string) --
A description of the purpose of the API key.

expires (integer) --
The time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour.









Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.LimitExceededException
AppSync.Client.exceptions.InternalFailureException
AppSync.Client.exceptions.ApiKeyValidityOutOfBoundsException


    :return: {
        'apiKey': {
            'id': 'string',
            'description': 'string',
            'expires': 123
        }
    }
    
    
    :returns: 
    AppSync.Client.exceptions.BadRequestException
    AppSync.Client.exceptions.NotFoundException
    AppSync.Client.exceptions.UnauthorizedException
    AppSync.Client.exceptions.LimitExceededException
    AppSync.Client.exceptions.InternalFailureException
    AppSync.Client.exceptions.ApiKeyValidityOutOfBoundsException
    
    """
    pass

def update_data_source(apiId=None, name=None, description=None, type=None, serviceRoleArn=None, dynamodbConfig=None, lambdaConfig=None, elasticsearchConfig=None, httpConfig=None, relationalDatabaseConfig=None):
    """
    Updates a DataSource object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_data_source(
        apiId='string',
        name='string',
        description='string',
        type='AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
        serviceRoleArn='string',
        dynamodbConfig={
            'tableName': 'string',
            'awsRegion': 'string',
            'useCallerCredentials': True|False,
            'deltaSyncConfig': {
                'baseTableTTL': 123,
                'deltaSyncTableName': 'string',
                'deltaSyncTableTTL': 123
            },
            'versioned': True|False
        },
        lambdaConfig={
            'lambdaFunctionArn': 'string'
        },
        elasticsearchConfig={
            'endpoint': 'string',
            'awsRegion': 'string'
        },
        httpConfig={
            'endpoint': 'string',
            'authorizationConfig': {
                'authorizationType': 'AWS_IAM',
                'awsIamConfig': {
                    'signingRegion': 'string',
                    'signingServiceName': 'string'
                }
            }
        },
        relationalDatabaseConfig={
            'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
            'rdsHttpEndpointConfig': {
                'awsRegion': 'string',
                'dbClusterIdentifier': 'string',
                'databaseName': 'string',
                'schema': 'string',
                'awsSecretStoreArn': 'string'
            }
        }
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type name: string
    :param name: [REQUIRED]\nThe new name for the data source.\n

    :type description: string
    :param description: The new description for the data source.

    :type type: string
    :param type: [REQUIRED]\nThe new data source type.\n

    :type serviceRoleArn: string
    :param serviceRoleArn: The new service role ARN for the data source.

    :type dynamodbConfig: dict
    :param dynamodbConfig: The new Amazon DynamoDB configuration.\n\ntableName (string) -- [REQUIRED]The table name.\n\nawsRegion (string) -- [REQUIRED]The AWS Region.\n\nuseCallerCredentials (boolean) --Set to TRUE to use Amazon Cognito credentials with this data source.\n\ndeltaSyncConfig (dict) --The DeltaSyncConfig for a versioned datasource.\n\nbaseTableTTL (integer) --The number of minutes an Item is stored in the datasource.\n\ndeltaSyncTableName (string) --The Delta Sync table name.\n\ndeltaSyncTableTTL (integer) --The number of minutes a Delta Sync log entry is stored in the Delta Sync table.\n\n\n\nversioned (boolean) --Set to TRUE to use Conflict Detection and Resolution with this data source.\n\n\n

    :type lambdaConfig: dict
    :param lambdaConfig: The new AWS Lambda configuration.\n\nlambdaFunctionArn (string) -- [REQUIRED]The ARN for the Lambda function.\n\n\n

    :type elasticsearchConfig: dict
    :param elasticsearchConfig: The new Elasticsearch Service configuration.\n\nendpoint (string) -- [REQUIRED]The endpoint.\n\nawsRegion (string) -- [REQUIRED]The AWS Region.\n\n\n

    :type httpConfig: dict
    :param httpConfig: The new HTTP endpoint configuration.\n\nendpoint (string) --The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.\n\nauthorizationConfig (dict) --The authorization config in case the HTTP endpoint requires authorization.\n\nauthorizationType (string) -- [REQUIRED]The authorization type required by the HTTP endpoint.\n\nAWS_IAM : The authorization type is Sigv4.\n\n\nawsIamConfig (dict) --The AWS IAM settings.\n\nsigningRegion (string) --The signing region for AWS IAM authorization.\n\nsigningServiceName (string) --The signing service name for AWS IAM authorization.\n\n\n\n\n\n\n

    :type relationalDatabaseConfig: dict
    :param relationalDatabaseConfig: The new relational database configuration.\n\nrelationalDatabaseSourceType (string) --Source type for the relational database.\n\nRDS_HTTP_ENDPOINT : The relational database source type is an Amazon RDS HTTP endpoint.\n\n\nrdsHttpEndpointConfig (dict) --Amazon RDS HTTP endpoint settings.\n\nawsRegion (string) --AWS Region for RDS HTTP endpoint.\n\ndbClusterIdentifier (string) --Amazon RDS cluster identifier.\n\ndatabaseName (string) --Logical database name.\n\nschema (string) --Logical schema name.\n\nawsSecretStoreArn (string) --AWS secret store ARN for database credentials.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'dataSource': {
        'dataSourceArn': 'string',
        'name': 'string',
        'description': 'string',
        'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
        'serviceRoleArn': 'string',
        'dynamodbConfig': {
            'tableName': 'string',
            'awsRegion': 'string',
            'useCallerCredentials': True|False,
            'deltaSyncConfig': {
                'baseTableTTL': 123,
                'deltaSyncTableName': 'string',
                'deltaSyncTableTTL': 123
            },
            'versioned': True|False
        },
        'lambdaConfig': {
            'lambdaFunctionArn': 'string'
        },
        'elasticsearchConfig': {
            'endpoint': 'string',
            'awsRegion': 'string'
        },
        'httpConfig': {
            'endpoint': 'string',
            'authorizationConfig': {
                'authorizationType': 'AWS_IAM',
                'awsIamConfig': {
                    'signingRegion': 'string',
                    'signingServiceName': 'string'
                }
            }
        },
        'relationalDatabaseConfig': {
            'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
            'rdsHttpEndpointConfig': {
                'awsRegion': 'string',
                'dbClusterIdentifier': 'string',
                'databaseName': 'string',
                'schema': 'string',
                'awsSecretStoreArn': 'string'
            }
        }
    }
}


Response Structure

(dict) --

dataSource (dict) --
The updated DataSource object.

dataSourceArn (string) --
The data source ARN.

name (string) --
The name of the data source.

description (string) --
The description of the data source.

type (string) --
The type of the data source.

AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
AWS_LAMBDA : The data source is an AWS Lambda function.
NONE : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
HTTP : The data source is an HTTP endpoint.
RELATIONAL_DATABASE : The data source is a relational database.


serviceRoleArn (string) --
The AWS IAM service role ARN for the data source. The system assumes this role when accessing the data source.

dynamodbConfig (dict) --
Amazon DynamoDB settings.

tableName (string) --
The table name.

awsRegion (string) --
The AWS Region.

useCallerCredentials (boolean) --
Set to TRUE to use Amazon Cognito credentials with this data source.

deltaSyncConfig (dict) --
The DeltaSyncConfig for a versioned datasource.

baseTableTTL (integer) --
The number of minutes an Item is stored in the datasource.

deltaSyncTableName (string) --
The Delta Sync table name.

deltaSyncTableTTL (integer) --
The number of minutes a Delta Sync log entry is stored in the Delta Sync table.



versioned (boolean) --
Set to TRUE to use Conflict Detection and Resolution with this data source.



lambdaConfig (dict) --
AWS Lambda settings.

lambdaFunctionArn (string) --
The ARN for the Lambda function.



elasticsearchConfig (dict) --
Amazon Elasticsearch Service settings.

endpoint (string) --
The endpoint.

awsRegion (string) --
The AWS Region.



httpConfig (dict) --
HTTP endpoint settings.

endpoint (string) --
The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.

authorizationConfig (dict) --
The authorization config in case the HTTP endpoint requires authorization.

authorizationType (string) --
The authorization type required by the HTTP endpoint.

AWS_IAM : The authorization type is Sigv4.


awsIamConfig (dict) --
The AWS IAM settings.

signingRegion (string) --
The signing region for AWS IAM authorization.

signingServiceName (string) --
The signing service name for AWS IAM authorization.







relationalDatabaseConfig (dict) --
Relational database settings.

relationalDatabaseSourceType (string) --
Source type for the relational database.

RDS_HTTP_ENDPOINT : The relational database source type is an Amazon RDS HTTP endpoint.


rdsHttpEndpointConfig (dict) --
Amazon RDS HTTP endpoint settings.

awsRegion (string) --
AWS Region for RDS HTTP endpoint.

dbClusterIdentifier (string) --
Amazon RDS cluster identifier.

databaseName (string) --
Logical database name.

schema (string) --
Logical schema name.

awsSecretStoreArn (string) --
AWS secret store ARN for database credentials.













Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'dataSource': {
            'dataSourceArn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
            'serviceRoleArn': 'string',
            'dynamodbConfig': {
                'tableName': 'string',
                'awsRegion': 'string',
                'useCallerCredentials': True|False,
                'deltaSyncConfig': {
                    'baseTableTTL': 123,
                    'deltaSyncTableName': 'string',
                    'deltaSyncTableTTL': 123
                },
                'versioned': True|False
            },
            'lambdaConfig': {
                'lambdaFunctionArn': 'string'
            },
            'elasticsearchConfig': {
                'endpoint': 'string',
                'awsRegion': 'string'
            },
            'httpConfig': {
                'endpoint': 'string',
                'authorizationConfig': {
                    'authorizationType': 'AWS_IAM',
                    'awsIamConfig': {
                        'signingRegion': 'string',
                        'signingServiceName': 'string'
                    }
                }
            },
            'relationalDatabaseConfig': {
                'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                'rdsHttpEndpointConfig': {
                    'awsRegion': 'string',
                    'dbClusterIdentifier': 'string',
                    'databaseName': 'string',
                    'schema': 'string',
                    'awsSecretStoreArn': 'string'
                }
            }
        }
    }
    
    
    :returns: 
    AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
    AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
    AWS_LAMBDA : The data source is an AWS Lambda function.
    NONE : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
    HTTP : The data source is an HTTP endpoint.
    RELATIONAL_DATABASE : The data source is a relational database.
    
    """
    pass

def update_function(apiId=None, name=None, description=None, functionId=None, dataSourceName=None, requestMappingTemplate=None, responseMappingTemplate=None, functionVersion=None):
    """
    Updates a Function object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_function(
        apiId='string',
        name='string',
        description='string',
        functionId='string',
        dataSourceName='string',
        requestMappingTemplate='string',
        responseMappingTemplate='string',
        functionVersion='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe GraphQL API ID.\n

    :type name: string
    :param name: [REQUIRED]\nThe Function name.\n

    :type description: string
    :param description: The Function description.

    :type functionId: string
    :param functionId: [REQUIRED]\nThe function ID.\n

    :type dataSourceName: string
    :param dataSourceName: [REQUIRED]\nThe Function DataSource name.\n

    :type requestMappingTemplate: string
    :param requestMappingTemplate: [REQUIRED]\nThe Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.\n

    :type responseMappingTemplate: string
    :param responseMappingTemplate: The Function request mapping template.

    :type functionVersion: string
    :param functionVersion: [REQUIRED]\nThe version of the request mapping template. Currently the supported value is 2018-05-29.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'functionConfiguration': {
        'functionId': 'string',
        'functionArn': 'string',
        'name': 'string',
        'description': 'string',
        'dataSourceName': 'string',
        'requestMappingTemplate': 'string',
        'responseMappingTemplate': 'string',
        'functionVersion': 'string'
    }
}


Response Structure

(dict) --

functionConfiguration (dict) --
The Function object.

functionId (string) --
A unique ID representing the Function object.

functionArn (string) --
The ARN of the Function object.

name (string) --
The name of the Function object.

description (string) --
The Function description.

dataSourceName (string) --
The name of the DataSource .

requestMappingTemplate (string) --
The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.

responseMappingTemplate (string) --
The Function response mapping template.

functionVersion (string) --
The version of the request mapping template. Currently only the 2018-05-29 version of the template is supported.









Exceptions

AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'functionConfiguration': {
            'functionId': 'string',
            'functionArn': 'string',
            'name': 'string',
            'description': 'string',
            'dataSourceName': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'functionVersion': 'string'
        }
    }
    
    
    :returns: 
    AppSync.Client.exceptions.ConcurrentModificationException
    AppSync.Client.exceptions.NotFoundException
    AppSync.Client.exceptions.UnauthorizedException
    AppSync.Client.exceptions.InternalFailureException
    
    """
    pass

def update_graphql_api(apiId=None, name=None, logConfig=None, authenticationType=None, userPoolConfig=None, openIDConnectConfig=None, additionalAuthenticationProviders=None, xrayEnabled=None):
    """
    Updates a GraphqlApi object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_graphql_api(
        apiId='string',
        name='string',
        logConfig={
            'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
            'cloudWatchLogsRoleArn': 'string',
            'excludeVerboseContent': True|False
        },
        authenticationType='API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
        userPoolConfig={
            'userPoolId': 'string',
            'awsRegion': 'string',
            'defaultAction': 'ALLOW'|'DENY',
            'appIdClientRegex': 'string'
        },
        openIDConnectConfig={
            'issuer': 'string',
            'clientId': 'string',
            'iatTTL': 123,
            'authTTL': 123
        },
        additionalAuthenticationProviders=[
            {
                'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                'openIDConnectConfig': {
                    'issuer': 'string',
                    'clientId': 'string',
                    'iatTTL': 123,
                    'authTTL': 123
                },
                'userPoolConfig': {
                    'userPoolId': 'string',
                    'awsRegion': 'string',
                    'appIdClientRegex': 'string'
                }
            },
        ],
        xrayEnabled=True|False
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type name: string
    :param name: [REQUIRED]\nThe new name for the GraphqlApi object.\n

    :type logConfig: dict
    :param logConfig: The Amazon CloudWatch Logs configuration for the GraphqlApi object.\n\nfieldLogLevel (string) -- [REQUIRED]The field logging level. Values can be NONE, ERROR, or ALL.\n\nNONE : No field-level logs are captured.\nERROR : Logs the following information only for the fields that are in error:\nThe error section in the server response.\nField-level errors.\nThe generated request/response functions that got resolved for error fields.\n\n\nALL : The following information is logged for all fields in the query:\nField-level tracing information.\nThe generated request/response functions that got resolved for each field.\n\n\n\n\ncloudWatchLogsRoleArn (string) -- [REQUIRED]The service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.\n\nexcludeVerboseContent (boolean) --Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.\n\n\n

    :type authenticationType: string
    :param authenticationType: The new authentication type for the GraphqlApi object.

    :type userPoolConfig: dict
    :param userPoolConfig: The new Amazon Cognito user pool configuration for the GraphqlApi object.\n\nuserPoolId (string) -- [REQUIRED]The user pool ID.\n\nawsRegion (string) -- [REQUIRED]The AWS Region in which the user pool was created.\n\ndefaultAction (string) -- [REQUIRED]The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn\'t match the Amazon Cognito user pool configuration.\n\nappIdClientRegex (string) --A regular expression for validating the incoming Amazon Cognito user pool app client ID.\n\n\n

    :type openIDConnectConfig: dict
    :param openIDConnectConfig: The OpenID Connect configuration for the GraphqlApi object.\n\nissuer (string) -- [REQUIRED]The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of iss in the ID token.\n\nclientId (string) --The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.\n\niatTTL (integer) --The number of milliseconds a token is valid after being issued to a user.\n\nauthTTL (integer) --The number of milliseconds a token is valid after being authenticated.\n\n\n

    :type additionalAuthenticationProviders: list
    :param additionalAuthenticationProviders: A list of additional authentication providers for the GraphqlApi API.\n\n(dict) --Describes an additional authentication provider.\n\nauthenticationType (string) --The authentication type: API key, AWS IAM, OIDC, or Amazon Cognito user pools.\n\nopenIDConnectConfig (dict) --The OpenID Connect configuration.\n\nissuer (string) -- [REQUIRED]The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of iss in the ID token.\n\nclientId (string) --The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.\n\niatTTL (integer) --The number of milliseconds a token is valid after being issued to a user.\n\nauthTTL (integer) --The number of milliseconds a token is valid after being authenticated.\n\n\n\nuserPoolConfig (dict) --The Amazon Cognito user pool configuration.\n\nuserPoolId (string) -- [REQUIRED]The user pool ID.\n\nawsRegion (string) -- [REQUIRED]The AWS Region in which the user pool was created.\n\nappIdClientRegex (string) --A regular expression for validating the incoming Amazon Cognito user pool app client ID.\n\n\n\n\n\n\n

    :type xrayEnabled: boolean
    :param xrayEnabled: A flag indicating whether to enable X-Ray tracing for the GraphqlApi .

    :rtype: dict

ReturnsResponse Syntax
{
    'graphqlApi': {
        'name': 'string',
        'apiId': 'string',
        'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
        'logConfig': {
            'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
            'cloudWatchLogsRoleArn': 'string',
            'excludeVerboseContent': True|False
        },
        'userPoolConfig': {
            'userPoolId': 'string',
            'awsRegion': 'string',
            'defaultAction': 'ALLOW'|'DENY',
            'appIdClientRegex': 'string'
        },
        'openIDConnectConfig': {
            'issuer': 'string',
            'clientId': 'string',
            'iatTTL': 123,
            'authTTL': 123
        },
        'arn': 'string',
        'uris': {
            'string': 'string'
        },
        'tags': {
            'string': 'string'
        },
        'additionalAuthenticationProviders': [
            {
                'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                'openIDConnectConfig': {
                    'issuer': 'string',
                    'clientId': 'string',
                    'iatTTL': 123,
                    'authTTL': 123
                },
                'userPoolConfig': {
                    'userPoolId': 'string',
                    'awsRegion': 'string',
                    'appIdClientRegex': 'string'
                }
            },
        ],
        'xrayEnabled': True|False
    }
}


Response Structure

(dict) --

graphqlApi (dict) --
The updated GraphqlApi object.

name (string) --
The API name.

apiId (string) --
The API ID.

authenticationType (string) --
The authentication type.

logConfig (dict) --
The Amazon CloudWatch Logs configuration.

fieldLogLevel (string) --
The field logging level. Values can be NONE, ERROR, or ALL.

NONE : No field-level logs are captured.
ERROR : Logs the following information only for the fields that are in error:
The error section in the server response.
Field-level errors.
The generated request/response functions that got resolved for error fields.


ALL : The following information is logged for all fields in the query:
Field-level tracing information.
The generated request/response functions that got resolved for each field.




cloudWatchLogsRoleArn (string) --
The service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.

excludeVerboseContent (boolean) --
Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.



userPoolConfig (dict) --
The Amazon Cognito user pool configuration.

userPoolId (string) --
The user pool ID.

awsRegion (string) --
The AWS Region in which the user pool was created.

defaultAction (string) --
The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn\'t match the Amazon Cognito user pool configuration.

appIdClientRegex (string) --
A regular expression for validating the incoming Amazon Cognito user pool app client ID.



openIDConnectConfig (dict) --
The OpenID Connect configuration.

issuer (string) --
The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of iss in the ID token.

clientId (string) --
The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.

iatTTL (integer) --
The number of milliseconds a token is valid after being issued to a user.

authTTL (integer) --
The number of milliseconds a token is valid after being authenticated.



arn (string) --
The ARN.

uris (dict) --
The URIs.

(string) --
(string) --




tags (dict) --
The tags.

(string) --
The key for the tag.

(string) --
The value for the tag.





additionalAuthenticationProviders (list) --
A list of additional authentication providers for the GraphqlApi API.

(dict) --
Describes an additional authentication provider.

authenticationType (string) --
The authentication type: API key, AWS IAM, OIDC, or Amazon Cognito user pools.

openIDConnectConfig (dict) --
The OpenID Connect configuration.

issuer (string) --
The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of iss in the ID token.

clientId (string) --
The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.

iatTTL (integer) --
The number of milliseconds a token is valid after being issued to a user.

authTTL (integer) --
The number of milliseconds a token is valid after being authenticated.



userPoolConfig (dict) --
The Amazon Cognito user pool configuration.

userPoolId (string) --
The user pool ID.

awsRegion (string) --
The AWS Region in which the user pool was created.

appIdClientRegex (string) --
A regular expression for validating the incoming Amazon Cognito user pool app client ID.







xrayEnabled (boolean) --
A flag representing whether X-Ray tracing is enabled for this GraphqlApi .









Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException
AppSync.Client.exceptions.AccessDeniedException


    :return: {
        'graphqlApi': {
            'name': 'string',
            'apiId': 'string',
            'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
            'logConfig': {
                'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                'cloudWatchLogsRoleArn': 'string',
                'excludeVerboseContent': True|False
            },
            'userPoolConfig': {
                'userPoolId': 'string',
                'awsRegion': 'string',
                'defaultAction': 'ALLOW'|'DENY',
                'appIdClientRegex': 'string'
            },
            'openIDConnectConfig': {
                'issuer': 'string',
                'clientId': 'string',
                'iatTTL': 123,
                'authTTL': 123
            },
            'arn': 'string',
            'uris': {
                'string': 'string'
            },
            'tags': {
                'string': 'string'
            },
            'additionalAuthenticationProviders': [
                {
                    'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                    'openIDConnectConfig': {
                        'issuer': 'string',
                        'clientId': 'string',
                        'iatTTL': 123,
                        'authTTL': 123
                    },
                    'userPoolConfig': {
                        'userPoolId': 'string',
                        'awsRegion': 'string',
                        'appIdClientRegex': 'string'
                    }
                },
            ],
            'xrayEnabled': True|False
        }
    }
    
    
    :returns: 
    NONE : No field-level logs are captured.
    ERROR : Logs the following information only for the fields that are in error:
    The error section in the server response.
    Field-level errors.
    The generated request/response functions that got resolved for error fields.
    
    
    ALL : The following information is logged for all fields in the query:
    Field-level tracing information.
    The generated request/response functions that got resolved for each field.
    
    
    
    """
    pass

def update_resolver(apiId=None, typeName=None, fieldName=None, dataSourceName=None, requestMappingTemplate=None, responseMappingTemplate=None, kind=None, pipelineConfig=None, syncConfig=None, cachingConfig=None):
    """
    Updates a Resolver object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_resolver(
        apiId='string',
        typeName='string',
        fieldName='string',
        dataSourceName='string',
        requestMappingTemplate='string',
        responseMappingTemplate='string',
        kind='UNIT'|'PIPELINE',
        pipelineConfig={
            'functions': [
                'string',
            ]
        },
        syncConfig={
            'conflictHandler': 'OPTIMISTIC_CONCURRENCY'|'LAMBDA'|'AUTOMERGE'|'NONE',
            'conflictDetection': 'VERSION'|'NONE',
            'lambdaConflictHandlerConfig': {
                'lambdaConflictHandlerArn': 'string'
            }
        },
        cachingConfig={
            'ttl': 123,
            'cachingKeys': [
                'string',
            ]
        }
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type typeName: string
    :param typeName: [REQUIRED]\nThe new type name.\n

    :type fieldName: string
    :param fieldName: [REQUIRED]\nThe new field name.\n

    :type dataSourceName: string
    :param dataSourceName: The new data source name.

    :type requestMappingTemplate: string
    :param requestMappingTemplate: [REQUIRED]\nThe new request mapping template.\n

    :type responseMappingTemplate: string
    :param responseMappingTemplate: The new response mapping template.

    :type kind: string
    :param kind: The resolver type.\n\nUNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.\nPIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.\n\n

    :type pipelineConfig: dict
    :param pipelineConfig: The PipelineConfig .\n\nfunctions (list) --A list of Function objects.\n\n(string) --\n\n\n\n

    :type syncConfig: dict
    :param syncConfig: The SyncConfig for a resolver attached to a versioned datasource.\n\nconflictHandler (string) --The Conflict Resolution strategy to perform in the event of a conflict.\n\nOPTIMISTIC_CONCURRENCY : Resolve conflicts by rejecting mutations when versions do not match the latest version at the server.\nAUTOMERGE : Resolve conflicts with the Automerge conflict resolution strategy.\nLAMBDA : Resolve conflicts with a Lambda function supplied in the LambdaConflictHandlerConfig.\n\n\nconflictDetection (string) --The Conflict Detection strategy to use.\n\nVERSION : Detect conflicts based on object versions for this resolver.\nNONE : Do not detect conflicts when executing this resolver.\n\n\nlambdaConflictHandlerConfig (dict) --The LambdaConflictHandlerConfig when configuring LAMBDA as the Conflict Handler.\n\nlambdaConflictHandlerArn (string) --The Arn for the Lambda function to use as the Conflict Handler.\n\n\n\n\n

    :type cachingConfig: dict
    :param cachingConfig: The caching configuration for the resolver.\n\nttl (integer) --The TTL in seconds for a resolver that has caching enabled.\nValid values are between 1 and 3600 seconds.\n\ncachingKeys (list) --The caching keys for a resolver that has caching enabled.\nValid values are entries from the $context.identity and $context.arguments maps.\n\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'resolver': {
        'typeName': 'string',
        'fieldName': 'string',
        'dataSourceName': 'string',
        'resolverArn': 'string',
        'requestMappingTemplate': 'string',
        'responseMappingTemplate': 'string',
        'kind': 'UNIT'|'PIPELINE',
        'pipelineConfig': {
            'functions': [
                'string',
            ]
        },
        'syncConfig': {
            'conflictHandler': 'OPTIMISTIC_CONCURRENCY'|'LAMBDA'|'AUTOMERGE'|'NONE',
            'conflictDetection': 'VERSION'|'NONE',
            'lambdaConflictHandlerConfig': {
                'lambdaConflictHandlerArn': 'string'
            }
        },
        'cachingConfig': {
            'ttl': 123,
            'cachingKeys': [
                'string',
            ]
        }
    }
}


Response Structure

(dict) --

resolver (dict) --
The updated Resolver object.

typeName (string) --
The resolver type name.

fieldName (string) --
The resolver field name.

dataSourceName (string) --
The resolver data source name.

resolverArn (string) --
The resolver ARN.

requestMappingTemplate (string) --
The request mapping template.

responseMappingTemplate (string) --
The response mapping template.

kind (string) --
The resolver type.

UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.


pipelineConfig (dict) --
The PipelineConfig .

functions (list) --
A list of Function objects.

(string) --




syncConfig (dict) --
The SyncConfig for a resolver attached to a versioned datasource.

conflictHandler (string) --
The Conflict Resolution strategy to perform in the event of a conflict.

OPTIMISTIC_CONCURRENCY : Resolve conflicts by rejecting mutations when versions do not match the latest version at the server.
AUTOMERGE : Resolve conflicts with the Automerge conflict resolution strategy.
LAMBDA : Resolve conflicts with a Lambda function supplied in the LambdaConflictHandlerConfig.


conflictDetection (string) --
The Conflict Detection strategy to use.

VERSION : Detect conflicts based on object versions for this resolver.
NONE : Do not detect conflicts when executing this resolver.


lambdaConflictHandlerConfig (dict) --
The LambdaConflictHandlerConfig when configuring LAMBDA as the Conflict Handler.

lambdaConflictHandlerArn (string) --
The Arn for the Lambda function to use as the Conflict Handler.





cachingConfig (dict) --
The caching configuration for the resolver.

ttl (integer) --
The TTL in seconds for a resolver that has caching enabled.
Valid values are between 1 and 3600 seconds.

cachingKeys (list) --
The caching keys for a resolver that has caching enabled.
Valid values are entries from the $context.identity and $context.arguments maps.

(string) --












Exceptions

AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'resolver': {
            'typeName': 'string',
            'fieldName': 'string',
            'dataSourceName': 'string',
            'resolverArn': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'kind': 'UNIT'|'PIPELINE',
            'pipelineConfig': {
                'functions': [
                    'string',
                ]
            },
            'syncConfig': {
                'conflictHandler': 'OPTIMISTIC_CONCURRENCY'|'LAMBDA'|'AUTOMERGE'|'NONE',
                'conflictDetection': 'VERSION'|'NONE',
                'lambdaConflictHandlerConfig': {
                    'lambdaConflictHandlerArn': 'string'
                }
            },
            'cachingConfig': {
                'ttl': 123,
                'cachingKeys': [
                    'string',
                ]
            }
        }
    }
    
    
    :returns: 
    UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
    PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.
    
    """
    pass

def update_type(apiId=None, typeName=None, definition=None, format=None):
    """
    Updates a Type object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_type(
        apiId='string',
        typeName='string',
        definition='string',
        format='SDL'|'JSON'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]\nThe API ID.\n

    :type typeName: string
    :param typeName: [REQUIRED]\nThe new type name.\n

    :type definition: string
    :param definition: The new definition.

    :type format: string
    :param format: [REQUIRED]\nThe new type format: SDL or JSON.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'type': {
        'name': 'string',
        'description': 'string',
        'arn': 'string',
        'definition': 'string',
        'format': 'SDL'|'JSON'
    }
}


Response Structure

(dict) --

type (dict) --
The updated Type object.

name (string) --
The type name.

description (string) --
The type description.

arn (string) --
The type ARN.

definition (string) --
The type definition.

format (string) --
The type format: SDL or JSON.









Exceptions

AppSync.Client.exceptions.BadRequestException
AppSync.Client.exceptions.ConcurrentModificationException
AppSync.Client.exceptions.NotFoundException
AppSync.Client.exceptions.UnauthorizedException
AppSync.Client.exceptions.InternalFailureException


    :return: {
        'type': {
            'name': 'string',
            'description': 'string',
            'arn': 'string',
            'definition': 'string',
            'format': 'SDL'|'JSON'
        }
    }
    
    
    :returns: 
    AppSync.Client.exceptions.BadRequestException
    AppSync.Client.exceptions.ConcurrentModificationException
    AppSync.Client.exceptions.NotFoundException
    AppSync.Client.exceptions.UnauthorizedException
    AppSync.Client.exceptions.InternalFailureException
    
    """
    pass

