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

def create_api_key(apiId=None, description=None, expires=None):
    """
    Creates a unique key that you can distribute to clients who are executing your API.
    See also: AWS API Documentation
    
    
    :example: response = client.create_api_key(
        apiId='string',
        description='string',
        expires=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The ID for your GraphQL API.
            

    :type description: string
    :param description: A description of the purpose of the API key.

    :type expires: integer
    :param expires: The time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour. The default value for this parameter is 7 days from creation time.

    :rtype: dict
    :return: {
        'apiKey': {
            'id': 'string',
            'description': 'string',
            'expires': 123
        }
    }
    
    
    """
    pass

def create_data_source(apiId=None, name=None, description=None, type=None, serviceRoleArn=None, dynamodbConfig=None, lambdaConfig=None, elasticsearchConfig=None):
    """
    Creates a DataSource object.
    See also: AWS API Documentation
    
    
    :example: response = client.create_data_source(
        apiId='string',
        name='string',
        description='string',
        type='AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE',
        serviceRoleArn='string',
        dynamodbConfig={
            'tableName': 'string',
            'awsRegion': 'string',
            'useCallerCredentials': True|False
        },
        lambdaConfig={
            'lambdaFunctionArn': 'string'
        },
        elasticsearchConfig={
            'endpoint': 'string',
            'awsRegion': 'string'
        }
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID for the GraphQL API for the DataSource .
            

    :type name: string
    :param name: [REQUIRED]
            A user-supplied name for the DataSource .
            

    :type description: string
    :param description: A description of the DataSource .

    :type type: string
    :param type: [REQUIRED]
            The type of the DataSource .
            

    :type serviceRoleArn: string
    :param serviceRoleArn: The IAM service role ARN for the data source. The system assumes this role when accessing the data source.

    :type dynamodbConfig: dict
    :param dynamodbConfig: DynamoDB settings.
            tableName (string) -- [REQUIRED]The table name.
            awsRegion (string) -- [REQUIRED]The AWS region.
            useCallerCredentials (boolean) --Set to TRUE to use Amazon Cognito credentials with this data source.
            

    :type lambdaConfig: dict
    :param lambdaConfig: AWS Lambda settings.
            lambdaFunctionArn (string) -- [REQUIRED]The ARN for the Lambda function.
            

    :type elasticsearchConfig: dict
    :param elasticsearchConfig: Amazon Elasticsearch settings.
            endpoint (string) -- [REQUIRED]The endpoint.
            awsRegion (string) -- [REQUIRED]The AWS region.
            

    :rtype: dict
    :return: {
        'dataSource': {
            'dataSourceArn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE',
            'serviceRoleArn': 'string',
            'dynamodbConfig': {
                'tableName': 'string',
                'awsRegion': 'string',
                'useCallerCredentials': True|False
            },
            'lambdaConfig': {
                'lambdaFunctionArn': 'string'
            },
            'elasticsearchConfig': {
                'endpoint': 'string',
                'awsRegion': 'string'
            }
        }
    }
    
    
    :returns: 
    AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
    AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
    AWS_LAMBDA : The data source is an AWS Lambda function.
    NONE : There is no data source. This type is used when the required information can be computed on the fly without connecting to a back-end data source.
    
    """
    pass

def create_graphql_api(name=None, authenticationType=None, userPoolConfig=None):
    """
    Creates a GraphqlApi object.
    See also: AWS API Documentation
    
    
    :example: response = client.create_graphql_api(
        name='string',
        authenticationType='API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS',
        userPoolConfig={
            'userPoolId': 'string',
            'awsRegion': 'string',
            'defaultAction': 'ALLOW'|'DENY',
            'appIdClientRegex': 'string'
        }
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            A user-supplied name for the GraphqlApi .
            

    :type authenticationType: string
    :param authenticationType: [REQUIRED]
            The authentication type: API key, IAM, or Amazon Cognito User Pools.
            

    :type userPoolConfig: dict
    :param userPoolConfig: The Amazon Cognito User Pool configuration.
            userPoolId (string) -- [REQUIRED]The user pool ID.
            awsRegion (string) -- [REQUIRED]The AWS region in which the user pool was created.
            defaultAction (string) -- [REQUIRED]The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn't match the Amazon Cognito User Pool configuration.
            appIdClientRegex (string) --A regular expression for validating the incoming Amazon Cognito User Pool app client ID.
            

    :rtype: dict
    :return: {
        'graphqlApi': {
            'name': 'string',
            'apiId': 'string',
            'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS',
            'userPoolConfig': {
                'userPoolId': 'string',
                'awsRegion': 'string',
                'defaultAction': 'ALLOW'|'DENY',
                'appIdClientRegex': 'string'
            },
            'arn': 'string',
            'uris': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_resolver(apiId=None, typeName=None, fieldName=None, dataSourceName=None, requestMappingTemplate=None, responseMappingTemplate=None):
    """
    Creates a Resolver object.
    A resolver converts incoming requests into a format that a data source can understand and converts the data source's responses into GraphQL.
    See also: AWS API Documentation
    
    
    :example: response = client.create_resolver(
        apiId='string',
        typeName='string',
        fieldName='string',
        dataSourceName='string',
        requestMappingTemplate='string',
        responseMappingTemplate='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The ID for the GraphQL API for which the resolver is being created.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The name of the Type .
            

    :type fieldName: string
    :param fieldName: [REQUIRED]
            The name of the field to attach the resolver to.
            

    :type dataSourceName: string
    :param dataSourceName: [REQUIRED]
            The name of the data source for which the resolver is being created.
            

    :type requestMappingTemplate: string
    :param requestMappingTemplate: [REQUIRED]
            The mapping template to be used for requests.
            A resolver uses a request mapping template to convert a GraphQL expression into a format that a data source can understand. Mapping templates are written in Apache Velocity Template Language (VTL).
            

    :type responseMappingTemplate: string
    :param responseMappingTemplate: The mapping template to be used for responses from the data source.

    :rtype: dict
    :return: {
        'resolver': {
            'typeName': 'string',
            'fieldName': 'string',
            'dataSourceName': 'string',
            'resolverArn': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string'
        }
    }
    
    
    """
    pass

def create_type(apiId=None, definition=None, format=None):
    """
    Creates a Type object.
    See also: AWS API Documentation
    
    
    :example: response = client.create_type(
        apiId='string',
        definition='string',
        format='SDL'|'JSON'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type definition: string
    :param definition: [REQUIRED]
            The type definition, in GraphQL Schema Definition Language (SDL) format.
            For more information, see the GraphQL SDL documentation .
            

    :type format: string
    :param format: [REQUIRED]
            The type format: SDL or JSON.
            

    :rtype: dict
    :return: {
        'type': {
            'name': 'string',
            'description': 'string',
            'arn': 'string',
            'definition': 'string',
            'format': 'SDL'|'JSON'
        }
    }
    
    
    """
    pass

def delete_api_key(apiId=None, id=None):
    """
    Deletes an API key.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_api_key(
        apiId='string',
        id='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type id: string
    :param id: [REQUIRED]
            The ID for the API key.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_data_source(apiId=None, name=None):
    """
    Deletes a DataSource object.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_data_source(
        apiId='string',
        name='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type name: string
    :param name: [REQUIRED]
            The name of the data source.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_graphql_api(apiId=None):
    """
    Deletes a GraphqlApi object.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_graphql_api(
        apiId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_resolver(apiId=None, typeName=None, fieldName=None):
    """
    Deletes a Resolver object.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_resolver(
        apiId='string',
        typeName='string',
        fieldName='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The name of the resolver type.
            

    :type fieldName: string
    :param fieldName: [REQUIRED]
            The resolver field name.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_type(apiId=None, typeName=None):
    """
    Deletes a Type object.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_type(
        apiId='string',
        typeName='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The type name.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def get_data_source(apiId=None, name=None):
    """
    Retrieves a DataSource object.
    See also: AWS API Documentation
    
    
    :example: response = client.get_data_source(
        apiId='string',
        name='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type name: string
    :param name: [REQUIRED]
            The name of the data source.
            

    :rtype: dict
    :return: {
        'dataSource': {
            'dataSourceArn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE',
            'serviceRoleArn': 'string',
            'dynamodbConfig': {
                'tableName': 'string',
                'awsRegion': 'string',
                'useCallerCredentials': True|False
            },
            'lambdaConfig': {
                'lambdaFunctionArn': 'string'
            },
            'elasticsearchConfig': {
                'endpoint': 'string',
                'awsRegion': 'string'
            }
        }
    }
    
    
    :returns: 
    AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
    AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
    AWS_LAMBDA : The data source is an AWS Lambda function.
    NONE : There is no data source. This type is used when the required information can be computed on the fly without connecting to a back-end data source.
    
    """
    pass

def get_graphql_api(apiId=None):
    """
    Retrieves a GraphqlApi object.
    See also: AWS API Documentation
    
    
    :example: response = client.get_graphql_api(
        apiId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID for the GraphQL API.
            

    :rtype: dict
    :return: {
        'graphqlApi': {
            'name': 'string',
            'apiId': 'string',
            'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS',
            'userPoolConfig': {
                'userPoolId': 'string',
                'awsRegion': 'string',
                'defaultAction': 'ALLOW'|'DENY',
                'appIdClientRegex': 'string'
            },
            'arn': 'string',
            'uris': {
                'string': 'string'
            }
        }
    }
    
    
    """
    pass

def get_introspection_schema(apiId=None, format=None):
    """
    Retrieves the introspection schema for a GraphQL API.
    See also: AWS API Documentation
    
    
    :example: response = client.get_introspection_schema(
        apiId='string',
        format='SDL'|'JSON'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type format: string
    :param format: [REQUIRED]
            The schema format: SDL or JSON.
            

    :rtype: dict
    :return: {
        'schema': StreamingBody()
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

def get_resolver(apiId=None, typeName=None, fieldName=None):
    """
    Retrieves a Resolver object.
    See also: AWS API Documentation
    
    
    :example: response = client.get_resolver(
        apiId='string',
        typeName='string',
        fieldName='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The resolver type name.
            

    :type fieldName: string
    :param fieldName: [REQUIRED]
            The resolver field name.
            

    :rtype: dict
    :return: {
        'resolver': {
            'typeName': 'string',
            'fieldName': 'string',
            'dataSourceName': 'string',
            'resolverArn': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string'
        }
    }
    
    
    """
    pass

def get_schema_creation_status(apiId=None):
    """
    Retrieves the current status of a schema creation operation.
    See also: AWS API Documentation
    
    
    :example: response = client.get_schema_creation_status(
        apiId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :rtype: dict
    :return: {
        'status': 'PROCESSING'|'ACTIVE'|'DELETING',
        'details': 'string'
    }
    
    
    """
    pass

def get_type(apiId=None, typeName=None, format=None):
    """
    Retrieves a Type object.
    See also: AWS API Documentation
    
    
    :example: response = client.get_type(
        apiId='string',
        typeName='string',
        format='SDL'|'JSON'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The type name.
            

    :type format: string
    :param format: [REQUIRED]
            The type format: SDL or JSON.
            

    :rtype: dict
    :return: {
        'type': {
            'name': 'string',
            'description': 'string',
            'arn': 'string',
            'definition': 'string',
            'format': 'SDL'|'JSON'
        }
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_api_keys(apiId=None, nextToken=None, maxResults=None):
    """
    Lists the API keys for a given API.
    See also: AWS API Documentation
    
    
    :example: response = client.list_api_keys(
        apiId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict
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
    
    
    """
    pass

def list_data_sources(apiId=None, nextToken=None, maxResults=None):
    """
    Lists the data sources for a given API.
    See also: AWS API Documentation
    
    
    :example: response = client.list_data_sources(
        apiId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict
    :return: {
        'dataSources': [
            {
                'dataSourceArn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE',
                'serviceRoleArn': 'string',
                'dynamodbConfig': {
                    'tableName': 'string',
                    'awsRegion': 'string',
                    'useCallerCredentials': True|False
                },
                'lambdaConfig': {
                    'lambdaFunctionArn': 'string'
                },
                'elasticsearchConfig': {
                    'endpoint': 'string',
                    'awsRegion': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
    AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
    AWS_LAMBDA : The data source is an AWS Lambda function.
    NONE : There is no data source. This type is used when the required information can be computed on the fly without connecting to a back-end data source.
    
    """
    pass

def list_graphql_apis(nextToken=None, maxResults=None):
    """
    Lists your GraphQL APIs.
    See also: AWS API Documentation
    
    
    :example: response = client.list_graphql_apis(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict
    :return: {
        'graphqlApis': [
            {
                'name': 'string',
                'apiId': 'string',
                'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS',
                'userPoolConfig': {
                    'userPoolId': 'string',
                    'awsRegion': 'string',
                    'defaultAction': 'ALLOW'|'DENY',
                    'appIdClientRegex': 'string'
                },
                'arn': 'string',
                'uris': {
                    'string': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_resolvers(apiId=None, typeName=None, nextToken=None, maxResults=None):
    """
    Lists the resolvers for a given API and type.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resolvers(
        apiId='string',
        typeName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The type name.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict
    :return: {
        'resolvers': [
            {
                'typeName': 'string',
                'fieldName': 'string',
                'dataSourceName': 'string',
                'resolverArn': 'string',
                'requestMappingTemplate': 'string',
                'responseMappingTemplate': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_types(apiId=None, format=None, nextToken=None, maxResults=None):
    """
    Lists the types for a given API.
    See also: AWS API Documentation
    
    
    :example: response = client.list_types(
        apiId='string',
        format='SDL'|'JSON',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type format: string
    :param format: [REQUIRED]
            The type format: SDL or JSON.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict
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
    
    
    """
    pass

def start_schema_creation(apiId=None, definition=None):
    """
    Adds a new schema to your GraphQL API.
    This operation is asynchronous. Use to determine when it has completed.
    See also: AWS API Documentation
    
    
    :example: response = client.start_schema_creation(
        apiId='string',
        definition=b'bytes'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type definition: bytes
    :param definition: [REQUIRED]
            The schema definition, in GraphQL schema language format.
            

    :rtype: dict
    :return: {
        'status': 'PROCESSING'|'ACTIVE'|'DELETING'
    }
    
    
    """
    pass

def update_api_key(apiId=None, id=None, description=None, expires=None):
    """
    Updates an API key.
    See also: AWS API Documentation
    
    
    :example: response = client.update_api_key(
        apiId='string',
        id='string',
        description='string',
        expires=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The ID for the GraphQL API
            

    :type id: string
    :param id: [REQUIRED]
            The API key ID.
            

    :type description: string
    :param description: A description of the purpose of the API key.

    :type expires: integer
    :param expires: The time after which the API key expires. The date is represented as seconds since the epoch.

    :rtype: dict
    :return: {
        'apiKey': {
            'id': 'string',
            'description': 'string',
            'expires': 123
        }
    }
    
    
    """
    pass

def update_data_source(apiId=None, name=None, description=None, type=None, serviceRoleArn=None, dynamodbConfig=None, lambdaConfig=None, elasticsearchConfig=None):
    """
    Updates a DataSource object.
    See also: AWS API Documentation
    
    
    :example: response = client.update_data_source(
        apiId='string',
        name='string',
        description='string',
        type='AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE',
        serviceRoleArn='string',
        dynamodbConfig={
            'tableName': 'string',
            'awsRegion': 'string',
            'useCallerCredentials': True|False
        },
        lambdaConfig={
            'lambdaFunctionArn': 'string'
        },
        elasticsearchConfig={
            'endpoint': 'string',
            'awsRegion': 'string'
        }
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type name: string
    :param name: [REQUIRED]
            The new name for the data source.
            

    :type description: string
    :param description: The new description for the data source.

    :type type: string
    :param type: [REQUIRED]
            The new data source type.
            

    :type serviceRoleArn: string
    :param serviceRoleArn: The new service role ARN for the data source.

    :type dynamodbConfig: dict
    :param dynamodbConfig: The new DynamoDB configuration.
            tableName (string) -- [REQUIRED]The table name.
            awsRegion (string) -- [REQUIRED]The AWS region.
            useCallerCredentials (boolean) --Set to TRUE to use Amazon Cognito credentials with this data source.
            

    :type lambdaConfig: dict
    :param lambdaConfig: The new Lambda configuration.
            lambdaFunctionArn (string) -- [REQUIRED]The ARN for the Lambda function.
            

    :type elasticsearchConfig: dict
    :param elasticsearchConfig: The new Elasticsearch configuration.
            endpoint (string) -- [REQUIRED]The endpoint.
            awsRegion (string) -- [REQUIRED]The AWS region.
            

    :rtype: dict
    :return: {
        'dataSource': {
            'dataSourceArn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE',
            'serviceRoleArn': 'string',
            'dynamodbConfig': {
                'tableName': 'string',
                'awsRegion': 'string',
                'useCallerCredentials': True|False
            },
            'lambdaConfig': {
                'lambdaFunctionArn': 'string'
            },
            'elasticsearchConfig': {
                'endpoint': 'string',
                'awsRegion': 'string'
            }
        }
    }
    
    
    :returns: 
    AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
    AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
    AWS_LAMBDA : The data source is an AWS Lambda function.
    NONE : There is no data source. This type is used when the required information can be computed on the fly without connecting to a back-end data source.
    
    """
    pass

def update_graphql_api(apiId=None, name=None, authenticationType=None, userPoolConfig=None):
    """
    Updates a GraphqlApi object.
    See also: AWS API Documentation
    
    
    :example: response = client.update_graphql_api(
        apiId='string',
        name='string',
        authenticationType='API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS',
        userPoolConfig={
            'userPoolId': 'string',
            'awsRegion': 'string',
            'defaultAction': 'ALLOW'|'DENY',
            'appIdClientRegex': 'string'
        }
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type name: string
    :param name: [REQUIRED]
            The new name for the GraphqlApi object.
            

    :type authenticationType: string
    :param authenticationType: The new authentication type for the GraphqlApi object.

    :type userPoolConfig: dict
    :param userPoolConfig: The new Amazon Cognito User Pool configuration for the GraphqlApi object.
            userPoolId (string) -- [REQUIRED]The user pool ID.
            awsRegion (string) -- [REQUIRED]The AWS region in which the user pool was created.
            defaultAction (string) -- [REQUIRED]The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn't match the Amazon Cognito User Pool configuration.
            appIdClientRegex (string) --A regular expression for validating the incoming Amazon Cognito User Pool app client ID.
            

    :rtype: dict
    :return: {
        'graphqlApi': {
            'name': 'string',
            'apiId': 'string',
            'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS',
            'userPoolConfig': {
                'userPoolId': 'string',
                'awsRegion': 'string',
                'defaultAction': 'ALLOW'|'DENY',
                'appIdClientRegex': 'string'
            },
            'arn': 'string',
            'uris': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_resolver(apiId=None, typeName=None, fieldName=None, dataSourceName=None, requestMappingTemplate=None, responseMappingTemplate=None):
    """
    Updates a Resolver object.
    See also: AWS API Documentation
    
    
    :example: response = client.update_resolver(
        apiId='string',
        typeName='string',
        fieldName='string',
        dataSourceName='string',
        requestMappingTemplate='string',
        responseMappingTemplate='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The new type name.
            

    :type fieldName: string
    :param fieldName: [REQUIRED]
            The new field name.
            

    :type dataSourceName: string
    :param dataSourceName: [REQUIRED]
            The new data source name.
            

    :type requestMappingTemplate: string
    :param requestMappingTemplate: [REQUIRED]
            The new request mapping template.
            

    :type responseMappingTemplate: string
    :param responseMappingTemplate: The new response mapping template.

    :rtype: dict
    :return: {
        'resolver': {
            'typeName': 'string',
            'fieldName': 'string',
            'dataSourceName': 'string',
            'resolverArn': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string'
        }
    }
    
    
    """
    pass

def update_type(apiId=None, typeName=None, definition=None, format=None):
    """
    Updates a Type object.
    See also: AWS API Documentation
    
    
    :example: response = client.update_type(
        apiId='string',
        typeName='string',
        definition='string',
        format='SDL'|'JSON'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The new type name.
            

    :type definition: string
    :param definition: The new definition.

    :type format: string
    :param format: [REQUIRED]
            The new type format: SDL or JSON.
            

    :rtype: dict
    :return: {
        'type': {
            'name': 'string',
            'description': 'string',
            'arn': 'string',
            'definition': 'string',
            'format': 'SDL'|'JSON'
        }
    }
    
    
    """
    pass

