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

def batch_get_named_query(NamedQueryIds=None):
    """
    Returns the details of a single named query or a list of up to 50 queries, which you provide as an array of query ID strings. Use  ListNamedQueries to get the list of named query IDs. If information could not be retrieved for a submitted query ID, information about the query ID submitted is listed under  UnprocessedNamedQueryId . Named queries are different from executed queries. Use  BatchGetQueryExecution to get details about each unique query execution, and  ListQueryExecutions to get a list of query execution IDs.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_get_named_query(
        NamedQueryIds=[
            'string',
        ]
    )
    
    
    :type NamedQueryIds: list
    :param NamedQueryIds: [REQUIRED]
            An array of query IDs.
            (string) --
            

    :rtype: dict
    :return: {
        'NamedQueries': [
            {
                'Name': 'string',
                'Description': 'string',
                'Database': 'string',
                'QueryString': 'string',
                'NamedQueryId': 'string'
            },
        ],
        'UnprocessedNamedQueryIds': [
            {
                'NamedQueryId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_get_query_execution(QueryExecutionIds=None):
    """
    Returns the details of a single query execution or a list of up to 50 query executions, which you provide as an array of query execution ID strings. To get a list of query execution IDs, use  ListQueryExecutions . Query executions are different from named (saved) queries. Use  BatchGetNamedQuery to get details about named queries.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_get_query_execution(
        QueryExecutionIds=[
            'string',
        ]
    )
    
    
    :type QueryExecutionIds: list
    :param QueryExecutionIds: [REQUIRED]
            An array of query execution IDs.
            (string) --
            

    :rtype: dict
    :return: {
        'QueryExecutions': [
            {
                'QueryExecutionId': 'string',
                'Query': 'string',
                'ResultConfiguration': {
                    'OutputLocation': 'string',
                    'EncryptionConfiguration': {
                        'EncryptionOption': 'SSE_S3'|'SSE_KMS'|'CSE_KMS',
                        'KmsKey': 'string'
                    }
                },
                'QueryExecutionContext': {
                    'Database': 'string'
                },
                'Status': {
                    'State': 'QUEUED'|'RUNNING'|'SUCCEEDED'|'FAILED'|'CANCELLED',
                    'StateChangeReason': 'string',
                    'SubmissionDateTime': datetime(2015, 1, 1),
                    'CompletionDateTime': datetime(2015, 1, 1)
                },
                'Statistics': {
                    'EngineExecutionTimeInMillis': 123,
                    'DataScannedInBytes': 123
                }
            },
        ],
        'UnprocessedQueryExecutionIds': [
            {
                'QueryExecutionId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

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

def create_named_query(Name=None, Description=None, Database=None, QueryString=None, ClientRequestToken=None):
    """
    Creates a named query.
    For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_named_query(
        Name='string',
        Description='string',
        Database='string',
        QueryString='string',
        ClientRequestToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The plain language name for the query.
            

    :type Description: string
    :param Description: A brief explanation of the query.

    :type Database: string
    :param Database: [REQUIRED]
            The database to which the query belongs.
            

    :type QueryString: string
    :param QueryString: [REQUIRED]
            The text of the query itself. In other words, all query statements.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another CreateNamedQuery request is received, the same response is returned and another query is not created. If a parameter has changed, for example, the QueryString , an error is returned.
            Warning
            This token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for users. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'NamedQueryId': 'string'
    }
    
    
    """
    pass

def delete_named_query(NamedQueryId=None):
    """
    Deletes a named query.
    For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_named_query(
        NamedQueryId='string'
    )
    
    
    :type NamedQueryId: string
    :param NamedQueryId: [REQUIRED]
            The unique ID of the query to delete.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {}
    
    
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

def get_named_query(NamedQueryId=None):
    """
    Returns information about a single query.
    See also: AWS API Documentation
    
    
    :example: response = client.get_named_query(
        NamedQueryId='string'
    )
    
    
    :type NamedQueryId: string
    :param NamedQueryId: [REQUIRED]
            The unique ID of the query. Use ListNamedQueries to get query IDs.
            

    :rtype: dict
    :return: {
        'NamedQuery': {
            'Name': 'string',
            'Description': 'string',
            'Database': 'string',
            'QueryString': 'string',
            'NamedQueryId': 'string'
        }
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

def get_query_execution(QueryExecutionId=None):
    """
    Returns information about a single execution of a query. Each time a query executes, information about the query execution is saved with a unique ID.
    See also: AWS API Documentation
    
    
    :example: response = client.get_query_execution(
        QueryExecutionId='string'
    )
    
    
    :type QueryExecutionId: string
    :param QueryExecutionId: [REQUIRED]
            The unique ID of the query execution.
            

    :rtype: dict
    :return: {
        'QueryExecution': {
            'QueryExecutionId': 'string',
            'Query': 'string',
            'ResultConfiguration': {
                'OutputLocation': 'string',
                'EncryptionConfiguration': {
                    'EncryptionOption': 'SSE_S3'|'SSE_KMS'|'CSE_KMS',
                    'KmsKey': 'string'
                }
            },
            'QueryExecutionContext': {
                'Database': 'string'
            },
            'Status': {
                'State': 'QUEUED'|'RUNNING'|'SUCCEEDED'|'FAILED'|'CANCELLED',
                'StateChangeReason': 'string',
                'SubmissionDateTime': datetime(2015, 1, 1),
                'CompletionDateTime': datetime(2015, 1, 1)
            },
            'Statistics': {
                'EngineExecutionTimeInMillis': 123,
                'DataScannedInBytes': 123
            }
        }
    }
    
    
    """
    pass

def get_query_results(QueryExecutionId=None, NextToken=None, MaxResults=None):
    """
    Returns the results of a single query execution specified by QueryExecutionId . This request does not execute the query but returns results. Use  StartQueryExecution to run a query.
    See also: AWS API Documentation
    
    
    :example: response = client.get_query_results(
        QueryExecutionId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type QueryExecutionId: string
    :param QueryExecutionId: [REQUIRED]
            The unique ID of the query execution.
            

    :type NextToken: string
    :param NextToken: The token that specifies where to start pagination if a previous request was truncated.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results (rows) to return in this request.

    :rtype: dict
    :return: {
        'ResultSet': {
            'Rows': [
                {
                    'Data': [
                        {
                            'VarCharValue': 'string'
                        },
                    ]
                },
            ],
            'ResultSetMetadata': {
                'ColumnInfo': [
                    {
                        'CatalogName': 'string',
                        'SchemaName': 'string',
                        'TableName': 'string',
                        'Name': 'string',
                        'Label': 'string',
                        'Type': 'string',
                        'Precision': 123,
                        'Scale': 123,
                        'Nullable': 'NOT_NULL'|'NULLABLE'|'UNKNOWN',
                        'CaseSensitive': True|False
                    },
                ]
            }
        },
        'NextToken': 'string'
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_named_queries(NextToken=None, MaxResults=None):
    """
    Provides a list of all available query IDs.
    For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.list_named_queries(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The token that specifies where to start pagination if a previous request was truncated.

    :type MaxResults: integer
    :param MaxResults: The maximum number of queries to return in this request.

    :rtype: dict
    :return: {
        'NamedQueryIds': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_query_executions(NextToken=None, MaxResults=None):
    """
    Provides a list of all available query execution IDs.
    For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.list_query_executions(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The token that specifies where to start pagination if a previous request was truncated.

    :type MaxResults: integer
    :param MaxResults: The maximum number of query executions to return in this request.

    :rtype: dict
    :return: {
        'QueryExecutionIds': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def start_query_execution(QueryString=None, ClientRequestToken=None, QueryExecutionContext=None, ResultConfiguration=None):
    """
    Runs (executes) the SQL query statements contained in the Query string.
    For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.start_query_execution(
        QueryString='string',
        ClientRequestToken='string',
        QueryExecutionContext={
            'Database': 'string'
        },
        ResultConfiguration={
            'OutputLocation': 'string',
            'EncryptionConfiguration': {
                'EncryptionOption': 'SSE_S3'|'SSE_KMS'|'CSE_KMS',
                'KmsKey': 'string'
            }
        }
    )
    
    
    :type QueryString: string
    :param QueryString: [REQUIRED]
            The SQL query statements to be executed.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another StartQueryExecution request is received, the same response is returned and another query is not created. If a parameter has changed, for example, the QueryString , an error is returned.
            Warning
            This token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for users. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.
            This field is autopopulated if not provided.
            

    :type QueryExecutionContext: dict
    :param QueryExecutionContext: The database within which the query executes.
            Database (string) --The name of the database.
            

    :type ResultConfiguration: dict
    :param ResultConfiguration: [REQUIRED]
            Specifies information about where and how to save the results of the query execution.
            OutputLocation (string) -- [REQUIRED]The location in S3 where query results are stored.
            EncryptionConfiguration (dict) --If query results are encrypted in S3, indicates the S3 encryption option used (for example, SSE-KMS or CSE-KMS and key information.
            EncryptionOption (string) -- [REQUIRED]Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (SSE-S3 ), server-side encryption with KMS-managed keys (SSE-KMS ), or client-side encryption with KMS-managed keys (CSE-KMS) is used.
            KmsKey (string) --For SSE-KMS and CSE-KMS , this is the KMS key ARN or ID.
            
            

    :rtype: dict
    :return: {
        'QueryExecutionId': 'string'
    }
    
    
    """
    pass

def stop_query_execution(QueryExecutionId=None):
    """
    Stops a query execution.
    For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.stop_query_execution(
        QueryExecutionId='string'
    )
    
    
    :type QueryExecutionId: string
    :param QueryExecutionId: [REQUIRED]
            The unique ID of the query execution to stop.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

