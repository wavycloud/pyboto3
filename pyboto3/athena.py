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
    Returns the details of a single named query or a list of up to 50 queries, which you provide as an array of query ID strings. Requires you to have access to the workgroup in which the queries were saved. Use  ListNamedQueriesInput to get the list of named query IDs in the specified workgroup. If information could not be retrieved for a submitted query ID, information about the query ID submitted is listed under  UnprocessedNamedQueryId . Named queries differ from executed queries. Use  BatchGetQueryExecutionInput to get details about each unique query execution, and  ListQueryExecutionsInput to get a list of query execution IDs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_named_query(
        NamedQueryIds=[
            'string',
        ]
    )
    
    
    :type NamedQueryIds: list
    :param NamedQueryIds: [REQUIRED]\nAn array of query IDs.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'NamedQueries': [
        {
            'Name': 'string',
            'Description': 'string',
            'Database': 'string',
            'QueryString': 'string',
            'NamedQueryId': 'string',
            'WorkGroup': 'string'
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


Response Structure

(dict) --
NamedQueries (list) --Information about the named query IDs submitted.

(dict) --A query, where QueryString is the list of SQL query statements that comprise the query.

Name (string) --The query name.

Description (string) --The query description.

Database (string) --The database to which the query belongs.

QueryString (string) --The SQL query statements that comprise the query.

NamedQueryId (string) --The unique identifier of the query.

WorkGroup (string) --The name of the workgroup that contains the named query.





UnprocessedNamedQueryIds (list) --Information about provided query IDs.

(dict) --Information about a named query ID that could not be processed.

NamedQueryId (string) --The unique identifier of the named query.

ErrorCode (string) --The error code returned when the processing request for the named query failed, if applicable.

ErrorMessage (string) --The error message returned when the processing request for the named query failed, if applicable.










Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


    :return: {
        'NamedQueries': [
            {
                'Name': 'string',
                'Description': 'string',
                'Database': 'string',
                'QueryString': 'string',
                'NamedQueryId': 'string',
                'WorkGroup': 'string'
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
    
    
    :returns: 
    Athena.Client.exceptions.InternalServerException
    Athena.Client.exceptions.InvalidRequestException
    
    """
    pass

def batch_get_query_execution(QueryExecutionIds=None):
    """
    Returns the details of a single query execution or a list of up to 50 query executions, which you provide as an array of query execution ID strings. Requires you to have access to the workgroup in which the queries ran. To get a list of query execution IDs, use  ListQueryExecutionsInput$WorkGroup . Query executions differ from named (saved) queries. Use  BatchGetNamedQueryInput to get details about named queries.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_query_execution(
        QueryExecutionIds=[
            'string',
        ]
    )
    
    
    :type QueryExecutionIds: list
    :param QueryExecutionIds: [REQUIRED]\nAn array of query execution IDs.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'QueryExecutions': [
        {
            'QueryExecutionId': 'string',
            'Query': 'string',
            'StatementType': 'DDL'|'DML'|'UTILITY',
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
                'DataScannedInBytes': 123,
                'DataManifestLocation': 'string',
                'TotalExecutionTimeInMillis': 123,
                'QueryQueueTimeInMillis': 123,
                'QueryPlanningTimeInMillis': 123,
                'ServiceProcessingTimeInMillis': 123
            },
            'WorkGroup': 'string'
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


Response Structure

(dict) --
QueryExecutions (list) --Information about a query execution.

(dict) --Information about a single instance of a query execution.

QueryExecutionId (string) --The unique identifier for each query execution.

Query (string) --The SQL query statements which the query execution ran.

StatementType (string) --The type of query statement that was run. DDL indicates DDL query statements. DML indicates DML (Data Manipulation Language) query statements, such as CREATE TABLE AS SELECT . UTILITY indicates query statements other than DDL and DML, such as SHOW CREATE TABLE , or DESCRIBE <table> .

ResultConfiguration (dict) --The location in Amazon S3 where query results were stored and the encryption option, if any, used for query results. These are known as "client-side settings". If workgroup settings override client-side settings, then the query uses the location for the query results and the encryption configuration that are specified for the workgroup.

OutputLocation (string) --The location in Amazon S3 where your query results are stored, such as s3://path/to/query/bucket/ . To run the query, you must specify the query results location using one of the ways: either for individual queries using either this setting (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is set, Athena issues an error that no output location is provided. For more information, see Query Results . If workgroup settings override client-side settings, then the query uses the settings specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

EncryptionConfiguration (dict) --If query results are encrypted in Amazon S3, indicates the encryption option used (for example, SSE-KMS or CSE-KMS ) and key information. This is a client-side setting. If workgroup settings override client-side settings, then the query uses the encryption configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration and Workgroup Settings Override Client-Side Settings .

EncryptionOption (string) --Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (SSE-S3 ), server-side encryption with KMS-managed keys (SSE-KMS ), or client-side encryption with KMS-managed keys (CSE-KMS) is used.
If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup\'s setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.

KmsKey (string) --For SSE-KMS and CSE-KMS , this is the KMS key ARN or ID.





QueryExecutionContext (dict) --The database in which the query execution occurred.

Database (string) --The name of the database.



Status (dict) --The completion date, current state, submission time, and state change reason (if applicable) for the query execution.

State (string) --The state of query execution. QUEUED indicates that the query has been submitted to the service, and Athena will execute the query as soon as resources are available. RUNNING indicates that the query is in execution phase. SUCCEEDED indicates that the query completed without errors. FAILED indicates that the query experienced an error and did not complete processing. CANCELLED indicates that a user input interrupted query execution.

StateChangeReason (string) --Further detail about the status of the query.

SubmissionDateTime (datetime) --The date and time that the query was submitted.

CompletionDateTime (datetime) --The date and time that the query completed.



Statistics (dict) --Query execution statistics, such as the amount of data scanned, the amount of time that the query took to process, and the type of statement that was run.

EngineExecutionTimeInMillis (integer) --The number of milliseconds that the query took to execute.

DataScannedInBytes (integer) --The number of bytes in the data that was queried.

DataManifestLocation (string) --The location and file name of a data manifest file. The manifest file is saved to the Athena query results location in Amazon S3. The manifest file tracks files that the query wrote to Amazon S3. If the query fails, the manifest file also tracks files that the query intended to write. The manifest is useful for identifying orphaned files resulting from a failed query. For more information, see Working with Query Results, Output Files, and Query History in the Amazon Athena User Guide .

TotalExecutionTimeInMillis (integer) --The number of milliseconds that Athena took to run the query.

QueryQueueTimeInMillis (integer) --The number of milliseconds that the query was in your query queue waiting for resources. Note that if transient errors occur, Athena might automatically add the query back to the queue.

QueryPlanningTimeInMillis (integer) --The number of milliseconds that Athena took to plan the query processing flow. This includes the time spent retrieving table partitions from the data source. Note that because the query engine performs the query planning, query planning time is a subset of engine processing time.

ServiceProcessingTimeInMillis (integer) --The number of milliseconds that Athena took to finalize and publish the query results after the query engine finished running the query.



WorkGroup (string) --The name of the workgroup in which the query ran.





UnprocessedQueryExecutionIds (list) --Information about the query executions that failed to run.

(dict) --Describes a query execution that failed to process.

QueryExecutionId (string) --The unique identifier of the query execution.

ErrorCode (string) --The error code returned when the query execution failed to process, if applicable.

ErrorMessage (string) --The error message returned when the query execution failed to process, if applicable.










Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


    :return: {
        'QueryExecutions': [
            {
                'QueryExecutionId': 'string',
                'Query': 'string',
                'StatementType': 'DDL'|'DML'|'UTILITY',
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
                    'DataScannedInBytes': 123,
                    'DataManifestLocation': 'string',
                    'TotalExecutionTimeInMillis': 123,
                    'QueryQueueTimeInMillis': 123,
                    'QueryPlanningTimeInMillis': 123,
                    'ServiceProcessingTimeInMillis': 123
                },
                'WorkGroup': 'string'
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
    
    
    :returns: 
    Athena.Client.exceptions.InternalServerException
    Athena.Client.exceptions.InvalidRequestException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_named_query(Name=None, Description=None, Database=None, QueryString=None, ClientRequestToken=None, WorkGroup=None):
    """
    Creates a named query in the specified workgroup. Requires that you have access to the workgroup.
    For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_named_query(
        Name='string',
        Description='string',
        Database='string',
        QueryString='string',
        ClientRequestToken='string',
        WorkGroup='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe query name.\n

    :type Description: string
    :param Description: The query description.

    :type Database: string
    :param Database: [REQUIRED]\nThe database to which the query belongs.\n

    :type QueryString: string
    :param QueryString: [REQUIRED]\nThe contents of the query with all query statements.\n

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another CreateNamedQuery request is received, the same response is returned and another query is not created. If a parameter has changed, for example, the QueryString , an error is returned.\n\nWarning\nThis token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for users. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.\n\nThis field is autopopulated if not provided.\n

    :type WorkGroup: string
    :param WorkGroup: The name of the workgroup in which the named query is being created.

    :rtype: dict

ReturnsResponse Syntax
{
    'NamedQueryId': 'string'
}


Response Structure

(dict) --

NamedQueryId (string) --
The unique ID of the query.







Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


    :return: {
        'NamedQueryId': 'string'
    }
    
    
    :returns: 
    Athena.Client.exceptions.InternalServerException
    Athena.Client.exceptions.InvalidRequestException
    
    """
    pass

def create_work_group(Name=None, Configuration=None, Description=None, Tags=None):
    """
    Creates a workgroup with the specified name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_work_group(
        Name='string',
        Configuration={
            'ResultConfiguration': {
                'OutputLocation': 'string',
                'EncryptionConfiguration': {
                    'EncryptionOption': 'SSE_S3'|'SSE_KMS'|'CSE_KMS',
                    'KmsKey': 'string'
                }
            },
            'EnforceWorkGroupConfiguration': True|False,
            'PublishCloudWatchMetricsEnabled': True|False,
            'BytesScannedCutoffPerQuery': 123,
            'RequesterPaysEnabled': True|False
        },
        Description='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe workgroup name.\n

    :type Configuration: dict
    :param Configuration: The configuration for the workgroup, which includes the location in Amazon S3 where query results are stored, the encryption configuration, if any, used for encrypting query results, whether the Amazon CloudWatch Metrics are enabled for the workgroup, the limit for the amount of bytes scanned (cutoff) per query, if it is specified, and whether workgroup\'s settings (specified with EnforceWorkGroupConfiguration) in the WorkGroupConfiguration override client-side settings. See WorkGroupConfiguration$EnforceWorkGroupConfiguration .\n\nResultConfiguration (dict) --The configuration for the workgroup, which includes the location in Amazon S3 where query results are stored and the encryption option, if any, used for query results. To run the query, you must specify the query results location using one of the ways: either in the workgroup using this setting, or for individual queries (client-side), using ResultConfiguration$OutputLocation . If none of them is set, Athena issues an error that no output location is provided. For more information, see Query Results .\n\nOutputLocation (string) --The location in Amazon S3 where your query results are stored, such as s3://path/to/query/bucket/ . To run the query, you must specify the query results location using one of the ways: either for individual queries using either this setting (client-side), or in the workgroup, using WorkGroupConfiguration . If none of them is set, Athena issues an error that no output location is provided. For more information, see Query Results . If workgroup settings override client-side settings, then the query uses the settings specified for the workgroup. See WorkGroupConfiguration$EnforceWorkGroupConfiguration .\n\nEncryptionConfiguration (dict) --If query results are encrypted in Amazon S3, indicates the encryption option used (for example, SSE-KMS or CSE-KMS ) and key information. This is a client-side setting. If workgroup settings override client-side settings, then the query uses the encryption configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See WorkGroupConfiguration$EnforceWorkGroupConfiguration and Workgroup Settings Override Client-Side Settings .\n\nEncryptionOption (string) -- [REQUIRED]Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (SSE-S3 ), server-side encryption with KMS-managed keys (SSE-KMS ), or client-side encryption with KMS-managed keys (CSE-KMS) is used.\nIf a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup\'s setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.\n\nKmsKey (string) --For SSE-KMS and CSE-KMS , this is the KMS key ARN or ID.\n\n\n\n\n\nEnforceWorkGroupConfiguration (boolean) --If set to 'true', the settings for the workgroup override client-side settings. If set to 'false', client-side settings are used. For more information, see Workgroup Settings Override Client-Side Settings .\n\nPublishCloudWatchMetricsEnabled (boolean) --Indicates that the Amazon CloudWatch metrics are enabled for the workgroup.\n\nBytesScannedCutoffPerQuery (integer) --The upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan.\n\nRequesterPaysEnabled (boolean) --If set to true , allows members assigned to a workgroup to reference Amazon S3 Requester Pays buckets in queries. If set to false , workgroup members cannot query data from Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error. The default is false . For more information about Requester Pays buckets, see Requester Pays Buckets in the Amazon Simple Storage Service Developer Guide .\n\n\n

    :type Description: string
    :param Description: The workgroup description.

    :type Tags: list
    :param Tags: One or more tags, separated by commas, that you want to attach to the workgroup as you create it.\n\n(dict) --A tag that you can add to a resource. A tag is a label that you assign to an AWS Athena resource (a workgroup). Each tag consists of a key and an optional value, both of which you define. Tags enable you to categorize workgroups in Athena, for example, by purpose, owner, or environment. Use a consistent set of tag keys to make it easier to search and filter workgroups in your account. The maximum tag key length is 128 Unicode characters in UTF-8. The maximum tag value length is 256 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag keys and values are case-sensitive. Tag keys must be unique per resource.\n\nKey (string) --A tag key. The tag key length is from 1 to 128 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag keys are case-sensitive and must be unique per resource.\n\nValue (string) --A tag value. The tag value length is from 0 to 256 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag values are case-sensitive.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_named_query(NamedQueryId=None):
    """
    Deletes the named query if you have access to the workgroup in which the query was saved.
    For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_named_query(
        NamedQueryId='string'
    )
    
    
    :type NamedQueryId: string
    :param NamedQueryId: [REQUIRED]\nThe unique ID of the query to delete.\nThis field is autopopulated if not provided.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


    :return: {}
    
    
    :returns: 
    Athena.Client.exceptions.InternalServerException
    Athena.Client.exceptions.InvalidRequestException
    
    """
    pass

def delete_work_group(WorkGroup=None, RecursiveDeleteOption=None):
    """
    Deletes the workgroup with the specified name. The primary workgroup cannot be deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_work_group(
        WorkGroup='string',
        RecursiveDeleteOption=True|False
    )
    
    
    :type WorkGroup: string
    :param WorkGroup: [REQUIRED]\nThe unique name of the workgroup to delete.\n

    :type RecursiveDeleteOption: boolean
    :param RecursiveDeleteOption: The option to delete the workgroup and its contents even if the workgroup contains any named queries.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


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
    :param Params: The parameters normally passed to\nClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid\nfor. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By\ndefault, the http method is whatever is used in the method\'s model.

    """
    pass

def get_named_query(NamedQueryId=None):
    """
    Returns information about a single query. Requires that you have access to the workgroup in which the query was saved.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_named_query(
        NamedQueryId='string'
    )
    
    
    :type NamedQueryId: string
    :param NamedQueryId: [REQUIRED]\nThe unique ID of the query. Use ListNamedQueries to get query IDs.\n

    :rtype: dict
ReturnsResponse Syntax{
    'NamedQuery': {
        'Name': 'string',
        'Description': 'string',
        'Database': 'string',
        'QueryString': 'string',
        'NamedQueryId': 'string',
        'WorkGroup': 'string'
    }
}


Response Structure

(dict) --
NamedQuery (dict) --Information about the query.

Name (string) --The query name.

Description (string) --The query description.

Database (string) --The database to which the query belongs.

QueryString (string) --The SQL query statements that comprise the query.

NamedQueryId (string) --The unique identifier of the query.

WorkGroup (string) --The name of the workgroup that contains the named query.








Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


    :return: {
        'NamedQuery': {
            'Name': 'string',
            'Description': 'string',
            'Database': 'string',
            'QueryString': 'string',
            'NamedQueryId': 'string',
            'WorkGroup': 'string'
        }
    }
    
    
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

def get_query_execution(QueryExecutionId=None):
    """
    Returns information about a single execution of a query if you have access to the workgroup in which the query ran. Each time a query executes, information about the query execution is saved with a unique ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_query_execution(
        QueryExecutionId='string'
    )
    
    
    :type QueryExecutionId: string
    :param QueryExecutionId: [REQUIRED]\nThe unique ID of the query execution.\n

    :rtype: dict
ReturnsResponse Syntax{
    'QueryExecution': {
        'QueryExecutionId': 'string',
        'Query': 'string',
        'StatementType': 'DDL'|'DML'|'UTILITY',
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
            'DataScannedInBytes': 123,
            'DataManifestLocation': 'string',
            'TotalExecutionTimeInMillis': 123,
            'QueryQueueTimeInMillis': 123,
            'QueryPlanningTimeInMillis': 123,
            'ServiceProcessingTimeInMillis': 123
        },
        'WorkGroup': 'string'
    }
}


Response Structure

(dict) --
QueryExecution (dict) --Information about the query execution.

QueryExecutionId (string) --The unique identifier for each query execution.

Query (string) --The SQL query statements which the query execution ran.

StatementType (string) --The type of query statement that was run. DDL indicates DDL query statements. DML indicates DML (Data Manipulation Language) query statements, such as CREATE TABLE AS SELECT . UTILITY indicates query statements other than DDL and DML, such as SHOW CREATE TABLE , or DESCRIBE <table> .

ResultConfiguration (dict) --The location in Amazon S3 where query results were stored and the encryption option, if any, used for query results. These are known as "client-side settings". If workgroup settings override client-side settings, then the query uses the location for the query results and the encryption configuration that are specified for the workgroup.

OutputLocation (string) --The location in Amazon S3 where your query results are stored, such as s3://path/to/query/bucket/ . To run the query, you must specify the query results location using one of the ways: either for individual queries using either this setting (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is set, Athena issues an error that no output location is provided. For more information, see Query Results . If workgroup settings override client-side settings, then the query uses the settings specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

EncryptionConfiguration (dict) --If query results are encrypted in Amazon S3, indicates the encryption option used (for example, SSE-KMS or CSE-KMS ) and key information. This is a client-side setting. If workgroup settings override client-side settings, then the query uses the encryption configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration and Workgroup Settings Override Client-Side Settings .

EncryptionOption (string) --Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (SSE-S3 ), server-side encryption with KMS-managed keys (SSE-KMS ), or client-side encryption with KMS-managed keys (CSE-KMS) is used.
If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup\'s setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.

KmsKey (string) --For SSE-KMS and CSE-KMS , this is the KMS key ARN or ID.





QueryExecutionContext (dict) --The database in which the query execution occurred.

Database (string) --The name of the database.



Status (dict) --The completion date, current state, submission time, and state change reason (if applicable) for the query execution.

State (string) --The state of query execution. QUEUED indicates that the query has been submitted to the service, and Athena will execute the query as soon as resources are available. RUNNING indicates that the query is in execution phase. SUCCEEDED indicates that the query completed without errors. FAILED indicates that the query experienced an error and did not complete processing. CANCELLED indicates that a user input interrupted query execution.

StateChangeReason (string) --Further detail about the status of the query.

SubmissionDateTime (datetime) --The date and time that the query was submitted.

CompletionDateTime (datetime) --The date and time that the query completed.



Statistics (dict) --Query execution statistics, such as the amount of data scanned, the amount of time that the query took to process, and the type of statement that was run.

EngineExecutionTimeInMillis (integer) --The number of milliseconds that the query took to execute.

DataScannedInBytes (integer) --The number of bytes in the data that was queried.

DataManifestLocation (string) --The location and file name of a data manifest file. The manifest file is saved to the Athena query results location in Amazon S3. The manifest file tracks files that the query wrote to Amazon S3. If the query fails, the manifest file also tracks files that the query intended to write. The manifest is useful for identifying orphaned files resulting from a failed query. For more information, see Working with Query Results, Output Files, and Query History in the Amazon Athena User Guide .

TotalExecutionTimeInMillis (integer) --The number of milliseconds that Athena took to run the query.

QueryQueueTimeInMillis (integer) --The number of milliseconds that the query was in your query queue waiting for resources. Note that if transient errors occur, Athena might automatically add the query back to the queue.

QueryPlanningTimeInMillis (integer) --The number of milliseconds that Athena took to plan the query processing flow. This includes the time spent retrieving table partitions from the data source. Note that because the query engine performs the query planning, query planning time is a subset of engine processing time.

ServiceProcessingTimeInMillis (integer) --The number of milliseconds that Athena took to finalize and publish the query results after the query engine finished running the query.



WorkGroup (string) --The name of the workgroup in which the query ran.








Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


    :return: {
        'QueryExecution': {
            'QueryExecutionId': 'string',
            'Query': 'string',
            'StatementType': 'DDL'|'DML'|'UTILITY',
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
                'DataScannedInBytes': 123,
                'DataManifestLocation': 'string',
                'TotalExecutionTimeInMillis': 123,
                'QueryQueueTimeInMillis': 123,
                'QueryPlanningTimeInMillis': 123,
                'ServiceProcessingTimeInMillis': 123
            },
            'WorkGroup': 'string'
        }
    }
    
    
    """
    pass

def get_query_results(QueryExecutionId=None, NextToken=None, MaxResults=None):
    """
    Streams the results of a single query execution specified by QueryExecutionId from the Athena query results location in Amazon S3. For more information, see Query Results in the Amazon Athena User Guide . This request does not execute the query but returns results. Use  StartQueryExecution to run a query.
    To stream query results successfully, the IAM principal with permission to call GetQueryResults also must have permissions to the Amazon S3 GetObject action for the Athena query results location.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_query_results(
        QueryExecutionId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type QueryExecutionId: string
    :param QueryExecutionId: [REQUIRED]\nThe unique ID of the query execution.\n

    :type NextToken: string
    :param NextToken: The token that specifies where to start pagination if a previous request was truncated.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results (rows) to return in this request.

    :rtype: dict

ReturnsResponse Syntax
{
    'UpdateCount': 123,
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


Response Structure

(dict) --

UpdateCount (integer) --
The number of rows inserted with a CREATE TABLE AS SELECT statement.

ResultSet (dict) --
The results of the query execution.

Rows (list) --
The rows in the table.

(dict) --
The rows that comprise a query result table.

Data (list) --
The data that populates a row in a query result table.

(dict) --
A piece of data (a field in the table).

VarCharValue (string) --
The value of the datum.









ResultSetMetadata (dict) --
The metadata that describes the column structure and data types of a table of query results.

ColumnInfo (list) --
Information about the columns returned in a query result metadata.

(dict) --
Information about the columns in a query execution result.

CatalogName (string) --
The catalog to which the query results belong.

SchemaName (string) --
The schema name (database name) to which the query results belong.

TableName (string) --
The table name for the query results.

Name (string) --
The name of the column.

Label (string) --
A column label.

Type (string) --
The data type of the column.

Precision (integer) --
For DECIMAL data types, specifies the total number of digits, up to 38. For performance reasons, we recommend up to 18 digits.

Scale (integer) --
For DECIMAL data types, specifies the total number of digits in the fractional part of the value. Defaults to 0.

Nullable (string) --
Indicates the column\'s nullable status.

CaseSensitive (boolean) --
Indicates whether values in the column are case-sensitive.









NextToken (string) --
A token to be used by the next request if this request is truncated.







Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


    :return: {
        'UpdateCount': 123,
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
    
    
    :returns: 
    Athena.Client.exceptions.InternalServerException
    Athena.Client.exceptions.InvalidRequestException
    
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

def get_work_group(WorkGroup=None):
    """
    Returns information about the workgroup with the specified name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_work_group(
        WorkGroup='string'
    )
    
    
    :type WorkGroup: string
    :param WorkGroup: [REQUIRED]\nThe name of the workgroup.\n

    :rtype: dict
ReturnsResponse Syntax{
    'WorkGroup': {
        'Name': 'string',
        'State': 'ENABLED'|'DISABLED',
        'Configuration': {
            'ResultConfiguration': {
                'OutputLocation': 'string',
                'EncryptionConfiguration': {
                    'EncryptionOption': 'SSE_S3'|'SSE_KMS'|'CSE_KMS',
                    'KmsKey': 'string'
                }
            },
            'EnforceWorkGroupConfiguration': True|False,
            'PublishCloudWatchMetricsEnabled': True|False,
            'BytesScannedCutoffPerQuery': 123,
            'RequesterPaysEnabled': True|False
        },
        'Description': 'string',
        'CreationTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
WorkGroup (dict) --Information about the workgroup.

Name (string) --The workgroup name.

State (string) --The state of the workgroup: ENABLED or DISABLED.

Configuration (dict) --The configuration of the workgroup, which includes the location in Amazon S3 where query results are stored, the encryption configuration, if any, used for query results; whether the Amazon CloudWatch Metrics are enabled for the workgroup; whether workgroup settings override client-side settings; and the data usage limits for the amount of data scanned per query or per workgroup. The workgroup settings override is specified in EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

ResultConfiguration (dict) --The configuration for the workgroup, which includes the location in Amazon S3 where query results are stored and the encryption option, if any, used for query results. To run the query, you must specify the query results location using one of the ways: either in the workgroup using this setting, or for individual queries (client-side), using  ResultConfiguration$OutputLocation . If none of them is set, Athena issues an error that no output location is provided. For more information, see Query Results .

OutputLocation (string) --The location in Amazon S3 where your query results are stored, such as s3://path/to/query/bucket/ . To run the query, you must specify the query results location using one of the ways: either for individual queries using either this setting (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is set, Athena issues an error that no output location is provided. For more information, see Query Results . If workgroup settings override client-side settings, then the query uses the settings specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

EncryptionConfiguration (dict) --If query results are encrypted in Amazon S3, indicates the encryption option used (for example, SSE-KMS or CSE-KMS ) and key information. This is a client-side setting. If workgroup settings override client-side settings, then the query uses the encryption configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration and Workgroup Settings Override Client-Side Settings .

EncryptionOption (string) --Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (SSE-S3 ), server-side encryption with KMS-managed keys (SSE-KMS ), or client-side encryption with KMS-managed keys (CSE-KMS) is used.
If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup\'s setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.

KmsKey (string) --For SSE-KMS and CSE-KMS , this is the KMS key ARN or ID.





EnforceWorkGroupConfiguration (boolean) --If set to "true", the settings for the workgroup override client-side settings. If set to "false", client-side settings are used. For more information, see Workgroup Settings Override Client-Side Settings .

PublishCloudWatchMetricsEnabled (boolean) --Indicates that the Amazon CloudWatch metrics are enabled for the workgroup.

BytesScannedCutoffPerQuery (integer) --The upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan.

RequesterPaysEnabled (boolean) --If set to true , allows members assigned to a workgroup to reference Amazon S3 Requester Pays buckets in queries. If set to false , workgroup members cannot query data from Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error. The default is false . For more information about Requester Pays buckets, see Requester Pays Buckets in the Amazon Simple Storage Service Developer Guide .



Description (string) --The workgroup description.

CreationTime (datetime) --The date and time the workgroup was created.








Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


    :return: {
        'WorkGroup': {
            'Name': 'string',
            'State': 'ENABLED'|'DISABLED',
            'Configuration': {
                'ResultConfiguration': {
                    'OutputLocation': 'string',
                    'EncryptionConfiguration': {
                        'EncryptionOption': 'SSE_S3'|'SSE_KMS'|'CSE_KMS',
                        'KmsKey': 'string'
                    }
                },
                'EnforceWorkGroupConfiguration': True|False,
                'PublishCloudWatchMetricsEnabled': True|False,
                'BytesScannedCutoffPerQuery': 123,
                'RequesterPaysEnabled': True|False
            },
            'Description': 'string',
            'CreationTime': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def list_named_queries(NextToken=None, MaxResults=None, WorkGroup=None):
    """
    Provides a list of available query IDs only for queries saved in the specified workgroup. Requires that you have access to the workgroup. If a workgroup is not specified, lists the saved queries for the primary workgroup.
    For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_named_queries(
        NextToken='string',
        MaxResults=123,
        WorkGroup='string'
    )
    
    
    :type NextToken: string
    :param NextToken: The token that specifies where to start pagination if a previous request was truncated.

    :type MaxResults: integer
    :param MaxResults: The maximum number of queries to return in this request.

    :type WorkGroup: string
    :param WorkGroup: The name of the workgroup from which the named queries are returned. If a workgroup is not specified, the saved queries for the primary workgroup are returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'NamedQueryIds': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

NamedQueryIds (list) --
The list of unique query IDs.

(string) --


NextToken (string) --
A token to be used by the next request if this request is truncated.







Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


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

def list_query_executions(NextToken=None, MaxResults=None, WorkGroup=None):
    """
    Provides a list of available query execution IDs for the queries in the specified workgroup. If a workgroup is not specified, returns a list of query execution IDs for the primary workgroup. Requires you to have access to the workgroup in which the queries ran.
    For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_query_executions(
        NextToken='string',
        MaxResults=123,
        WorkGroup='string'
    )
    
    
    :type NextToken: string
    :param NextToken: The token that specifies where to start pagination if a previous request was truncated.

    :type MaxResults: integer
    :param MaxResults: The maximum number of query executions to return in this request.

    :type WorkGroup: string
    :param WorkGroup: The name of the workgroup from which queries are returned. If a workgroup is not specified, a list of available query execution IDs for the queries in the primary workgroup is returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'QueryExecutionIds': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

QueryExecutionIds (list) --
The unique IDs of each query execution as an array of strings.

(string) --


NextToken (string) --
A token to be used by the next request if this request is truncated.







Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


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

def list_tags_for_resource(ResourceARN=None, NextToken=None, MaxResults=None):
    """
    Lists the tags associated with this workgroup.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceARN='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nLists the tags for the workgroup resource with the specified ARN.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results, or null if there are no additional results for this request, where the request lists the tags for the workgroup resource with the specified ARN.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned per request that lists the tags for the workgroup resource.

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Tags (list) --
The list of tags associated with this workgroup.

(dict) --
A tag that you can add to a resource. A tag is a label that you assign to an AWS Athena resource (a workgroup). Each tag consists of a key and an optional value, both of which you define. Tags enable you to categorize workgroups in Athena, for example, by purpose, owner, or environment. Use a consistent set of tag keys to make it easier to search and filter workgroups in your account. The maximum tag key length is 128 Unicode characters in UTF-8. The maximum tag value length is 256 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag keys and values are case-sensitive. Tag keys must be unique per resource.

Key (string) --
A tag key. The tag key length is from 1 to 128 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag keys are case-sensitive and must be unique per resource.

Value (string) --
A tag value. The tag value length is from 0 to 256 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag values are case-sensitive.





NextToken (string) --
A token to be used by the next request if this request is truncated.







Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException
Athena.Client.exceptions.ResourceNotFoundException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Athena.Client.exceptions.InternalServerException
    Athena.Client.exceptions.InvalidRequestException
    Athena.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_work_groups(NextToken=None, MaxResults=None):
    """
    Lists available workgroups for the account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_work_groups(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: A token to be used by the next request if this request is truncated.

    :type MaxResults: integer
    :param MaxResults: The maximum number of workgroups to return in this request.

    :rtype: dict

ReturnsResponse Syntax
{
    'WorkGroups': [
        {
            'Name': 'string',
            'State': 'ENABLED'|'DISABLED',
            'Description': 'string',
            'CreationTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

WorkGroups (list) --
The list of workgroups, including their names, descriptions, creation times, and states.

(dict) --
The summary information for the workgroup, which includes its name, state, description, and the date and time it was created.

Name (string) --
The name of the workgroup.

State (string) --
The state of the workgroup.

Description (string) --
The workgroup description.

CreationTime (datetime) --
The workgroup creation date and time.





NextToken (string) --
A token to be used by the next request if this request is truncated.







Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


    :return: {
        'WorkGroups': [
            {
                'Name': 'string',
                'State': 'ENABLED'|'DISABLED',
                'Description': 'string',
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Athena.Client.exceptions.InternalServerException
    Athena.Client.exceptions.InvalidRequestException
    
    """
    pass

def start_query_execution(QueryString=None, ClientRequestToken=None, QueryExecutionContext=None, ResultConfiguration=None, WorkGroup=None):
    """
    Runs the SQL query statements contained in the Query . Requires you to have access to the workgroup in which the query ran.
    For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
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
        },
        WorkGroup='string'
    )
    
    
    :type QueryString: string
    :param QueryString: [REQUIRED]\nThe SQL query statements to be executed.\n

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another StartQueryExecution request is received, the same response is returned and another query is not created. If a parameter has changed, for example, the QueryString , an error is returned.\n\nWarning\nThis token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for users. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.\n\nThis field is autopopulated if not provided.\n

    :type QueryExecutionContext: dict
    :param QueryExecutionContext: The database within which the query executes.\n\nDatabase (string) --The name of the database.\n\n\n

    :type ResultConfiguration: dict
    :param ResultConfiguration: Specifies information about where and how to save the results of the query execution. If the query runs in a workgroup, then workgroup\'s settings may override query settings. This affects the query results location. The workgroup settings override is specified in EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See WorkGroupConfiguration$EnforceWorkGroupConfiguration .\n\nOutputLocation (string) --The location in Amazon S3 where your query results are stored, such as s3://path/to/query/bucket/ . To run the query, you must specify the query results location using one of the ways: either for individual queries using either this setting (client-side), or in the workgroup, using WorkGroupConfiguration . If none of them is set, Athena issues an error that no output location is provided. For more information, see Query Results . If workgroup settings override client-side settings, then the query uses the settings specified for the workgroup. See WorkGroupConfiguration$EnforceWorkGroupConfiguration .\n\nEncryptionConfiguration (dict) --If query results are encrypted in Amazon S3, indicates the encryption option used (for example, SSE-KMS or CSE-KMS ) and key information. This is a client-side setting. If workgroup settings override client-side settings, then the query uses the encryption configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See WorkGroupConfiguration$EnforceWorkGroupConfiguration and Workgroup Settings Override Client-Side Settings .\n\nEncryptionOption (string) -- [REQUIRED]Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (SSE-S3 ), server-side encryption with KMS-managed keys (SSE-KMS ), or client-side encryption with KMS-managed keys (CSE-KMS) is used.\nIf a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup\'s setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.\n\nKmsKey (string) --For SSE-KMS and CSE-KMS , this is the KMS key ARN or ID.\n\n\n\n\n

    :type WorkGroup: string
    :param WorkGroup: The name of the workgroup in which the query is being started.

    :rtype: dict

ReturnsResponse Syntax
{
    'QueryExecutionId': 'string'
}


Response Structure

(dict) --

QueryExecutionId (string) --
The unique ID of the query that ran as a result of this request.







Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException
Athena.Client.exceptions.TooManyRequestsException


    :return: {
        'QueryExecutionId': 'string'
    }
    
    
    :returns: 
    Athena.Client.exceptions.InternalServerException
    Athena.Client.exceptions.InvalidRequestException
    Athena.Client.exceptions.TooManyRequestsException
    
    """
    pass

def stop_query_execution(QueryExecutionId=None):
    """
    Stops a query execution. Requires you to have access to the workgroup in which the query ran.
    For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_query_execution(
        QueryExecutionId='string'
    )
    
    
    :type QueryExecutionId: string
    :param QueryExecutionId: [REQUIRED]\nThe unique ID of the query execution to stop.\nThis field is autopopulated if not provided.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


    :return: {}
    
    
    :returns: 
    Athena.Client.exceptions.InternalServerException
    Athena.Client.exceptions.InvalidRequestException
    
    """
    pass

def tag_resource(ResourceARN=None, Tags=None):
    """
    Adds one or more tags to the resource, such as a workgroup. A tag is a label that you assign to an AWS Athena resource (a workgroup). Each tag consists of a key and an optional value, both of which you define. Tags enable you to categorize resources (workgroups) in Athena, for example, by purpose, owner, or environment. Use a consistent set of tag keys to make it easier to search and filter workgroups in your account. For best practices, see AWS Tagging Strategies . The key length is from 1 (minimum) to 128 (maximum) Unicode characters in UTF-8. The tag value length is from 0 (minimum) to 256 (maximum) Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag keys and values are case-sensitive. Tag keys must be unique per resource. If you specify more than one, separate them by commas.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceARN='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nRequests that one or more tags are added to the resource (such as a workgroup) for the specified ARN.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nOne or more tags, separated by commas, to be added to the resource, such as a workgroup.\n\n(dict) --A tag that you can add to a resource. A tag is a label that you assign to an AWS Athena resource (a workgroup). Each tag consists of a key and an optional value, both of which you define. Tags enable you to categorize workgroups in Athena, for example, by purpose, owner, or environment. Use a consistent set of tag keys to make it easier to search and filter workgroups in your account. The maximum tag key length is 128 Unicode characters in UTF-8. The maximum tag value length is 256 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag keys and values are case-sensitive. Tag keys must be unique per resource.\n\nKey (string) --A tag key. The tag key length is from 1 to 128 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag keys are case-sensitive and must be unique per resource.\n\nValue (string) --A tag value. The tag value length is from 0 to 256 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag values are case-sensitive.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException
Athena.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceARN=None, TagKeys=None):
    """
    Removes one or more tags from the workgroup resource. Takes as an input a list of TagKey Strings separated by commas, and removes their tags at the same time.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nRemoves one or more tags from the workgroup resource for the specified ARN.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nRemoves the tags associated with one or more tag keys from the workgroup resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException
Athena.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_work_group(WorkGroup=None, Description=None, ConfigurationUpdates=None, State=None):
    """
    Updates the workgroup with the specified name. The workgroup\'s name cannot be changed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_work_group(
        WorkGroup='string',
        Description='string',
        ConfigurationUpdates={
            'EnforceWorkGroupConfiguration': True|False,
            'ResultConfigurationUpdates': {
                'OutputLocation': 'string',
                'RemoveOutputLocation': True|False,
                'EncryptionConfiguration': {
                    'EncryptionOption': 'SSE_S3'|'SSE_KMS'|'CSE_KMS',
                    'KmsKey': 'string'
                },
                'RemoveEncryptionConfiguration': True|False
            },
            'PublishCloudWatchMetricsEnabled': True|False,
            'BytesScannedCutoffPerQuery': 123,
            'RemoveBytesScannedCutoffPerQuery': True|False,
            'RequesterPaysEnabled': True|False
        },
        State='ENABLED'|'DISABLED'
    )
    
    
    :type WorkGroup: string
    :param WorkGroup: [REQUIRED]\nThe specified workgroup that will be updated.\n

    :type Description: string
    :param Description: The workgroup description.

    :type ConfigurationUpdates: dict
    :param ConfigurationUpdates: The workgroup configuration that will be updated for the given workgroup.\n\nEnforceWorkGroupConfiguration (boolean) --If set to 'true', the settings for the workgroup override client-side settings. If set to 'false' client-side settings are used. For more information, see Workgroup Settings Override Client-Side Settings .\n\nResultConfigurationUpdates (dict) --The result configuration information about the queries in this workgroup that will be updated. Includes the updated results location and an updated option for encrypting query results.\n\nOutputLocation (string) --The location in Amazon S3 where your query results are stored, such as s3://path/to/query/bucket/ . For more information, see Query Results If workgroup settings override client-side settings, then the query uses the location for the query results and the encryption configuration that are specified for the workgroup. The 'workgroup settings override' is specified in EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See WorkGroupConfiguration$EnforceWorkGroupConfiguration .\n\nRemoveOutputLocation (boolean) --If set to 'true', indicates that the previously-specified query results location (also known as a client-side setting) for queries in this workgroup should be ignored and set to null. If set to 'false' or not set, and a value is present in the OutputLocation in ResultConfigurationUpdates (the client-side setting), the OutputLocation in the workgroup\'s ResultConfiguration will be updated with the new value. For more information, see Workgroup Settings Override Client-Side Settings .\n\nEncryptionConfiguration (dict) --The encryption configuration for the query results.\n\nEncryptionOption (string) -- [REQUIRED]Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (SSE-S3 ), server-side encryption with KMS-managed keys (SSE-KMS ), or client-side encryption with KMS-managed keys (CSE-KMS) is used.\nIf a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup\'s setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.\n\nKmsKey (string) --For SSE-KMS and CSE-KMS , this is the KMS key ARN or ID.\n\n\n\nRemoveEncryptionConfiguration (boolean) --If set to 'true', indicates that the previously-specified encryption configuration (also known as the client-side setting) for queries in this workgroup should be ignored and set to null. If set to 'false' or not set, and a value is present in the EncryptionConfiguration in ResultConfigurationUpdates (the client-side setting), the EncryptionConfiguration in the workgroup\'s ResultConfiguration will be updated with the new value. For more information, see Workgroup Settings Override Client-Side Settings .\n\n\n\nPublishCloudWatchMetricsEnabled (boolean) --Indicates whether this workgroup enables publishing metrics to Amazon CloudWatch.\n\nBytesScannedCutoffPerQuery (integer) --The upper limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan.\n\nRemoveBytesScannedCutoffPerQuery (boolean) --Indicates that the data usage control limit per query is removed. WorkGroupConfiguration$BytesScannedCutoffPerQuery\n\nRequesterPaysEnabled (boolean) --If set to true , allows members assigned to a workgroup to specify Amazon S3 Requester Pays buckets in queries. If set to false , workgroup members cannot query data from Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error. The default is false . For more information about Requester Pays buckets, see Requester Pays Buckets in the Amazon Simple Storage Service Developer Guide .\n\n\n

    :type State: string
    :param State: The workgroup state that will be updated for the given workgroup.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Athena.Client.exceptions.InternalServerException
Athena.Client.exceptions.InvalidRequestException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

