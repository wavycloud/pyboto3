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

def batch_execute_statement(database=None, parameterSets=None, resourceArn=None, schema=None, secretArn=None, sql=None, transactionId=None):
    """
    Runs a batch SQL statement over an array of data.
    You can run bulk update and insert operations for multiple records using a DML statement with different parameter sets. Bulk operations can provide a significant performance improvement over individual insert and update operations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_execute_statement(
        database='string',
        parameterSets=[
            [
                {
                    'name': 'string',
                    'typeHint': 'DATE'|'DECIMAL'|'TIME'|'TIMESTAMP',
                    'value': {
                        'arrayValue': {
                            'arrayValues': [
                                {'... recursive ...'},
                            ],
                            'booleanValues': [
                                True|False,
                            ],
                            'doubleValues': [
                                123.0,
                            ],
                            'longValues': [
                                123,
                            ],
                            'stringValues': [
                                'string',
                            ]
                        },
                        'blobValue': b'bytes',
                        'booleanValue': True|False,
                        'doubleValue': 123.0,
                        'isNull': True|False,
                        'longValue': 123,
                        'stringValue': 'string'
                    }
                },
            ],
        ],
        resourceArn='string',
        schema='string',
        secretArn='string',
        sql='string',
        transactionId='string'
    )
    
    
    :type database: string
    :param database: The name of the database.

    :type parameterSets: list
    :param parameterSets: The parameter set for the batch operation.\nThe SQL statement is executed as many times as the number of parameter sets provided. To execute a SQL statement with no parameters, use one of the following options:\n\nSpecify one or more empty parameter sets.\nUse the ExecuteStatement operation instead of the BatchExecuteStatement operation.\n\n\nNote\nArray parameters are not supported.\n\n\n(list) --\n(dict) --A parameter used in a SQL statement.\n\nname (string) --The name of the parameter.\n\ntypeHint (string) --A hint that specifies the correct object type for data type mapping.\n\nValues:\n\nDECIMAL - The corresponding String parameter value is sent as an object of DECIMAL type to the database.\nTIMESTAMP - The corresponding String parameter value is sent as an object of TIMESTAMP type to the database. The accepted format is YYYY-MM-DD HH:MM:SS[.FFF] .\nTIME - The corresponding String parameter value is sent as an object of TIME type to the database. The accepted format is HH:MM:SS[.FFF] .\nDATE - The corresponding String parameter value is sent as an object of DATE type to the database. The accepted format is YYYY-MM-DD .\n\n\nvalue (dict) --The value of the parameter.\n\narrayValue (dict) --An array of values.\n\narrayValues (list) --An array of arrays.\n\n(dict) --Contains an array.\n\n\n\nbooleanValues (list) --An array of Boolean values.\n\n(boolean) --\n\n\ndoubleValues (list) --An array of integers.\n\n(float) --\n\n\nlongValues (list) --An array of floating point numbers.\n\n(integer) --\n\n\nstringValues (list) --An array of strings.\n\n(string) --\n\n\n\n\nblobValue (bytes) --A value of BLOB data type.\n\nbooleanValue (boolean) --A value of Boolean data type.\n\ndoubleValue (float) --A value of double data type.\n\nisNull (boolean) --A NULL value.\n\nlongValue (integer) --A value of long data type.\n\nstringValue (string) --A value of string data type.\n\n\n\n\n\n\n\n\n

    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.\n

    :type schema: string
    :param schema: The name of the database schema.

    :type secretArn: string
    :param secretArn: [REQUIRED]\nThe name or ARN of the secret that enables access to the DB cluster.\n

    :type sql: string
    :param sql: [REQUIRED]\nThe SQL statement to run.\n

    :type transactionId: string
    :param transactionId: The identifier of a transaction that was started by using the BeginTransaction operation. Specify the transaction ID of the transaction that you want to include the SQL statement in.\nIf the SQL statement is not part of a transaction, don\'t set this parameter.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'updateResults': [
        {
            'generatedFields': [
                {
                    'arrayValue': {
                        'arrayValues': [
                            {'... recursive ...'},
                        ],
                        'booleanValues': [
                            True|False,
                        ],
                        'doubleValues': [
                            123.0,
                        ],
                        'longValues': [
                            123,
                        ],
                        'stringValues': [
                            'string',
                        ]
                    },
                    'blobValue': b'bytes',
                    'booleanValue': True|False,
                    'doubleValue': 123.0,
                    'isNull': True|False,
                    'longValue': 123,
                    'stringValue': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --
The response elements represent the output of a SQL statement over an array of data.

updateResults (list) --
The execution results of each batch entry.

(dict) --
The response elements represent the results of an update.

generatedFields (list) --
Values for fields generated during the request.

(dict) --
Contains a value.

arrayValue (dict) --
An array of values.

arrayValues (list) --
An array of arrays.

(dict) --
Contains an array.



booleanValues (list) --
An array of Boolean values.

(boolean) --


doubleValues (list) --
An array of integers.

(float) --


longValues (list) --
An array of floating point numbers.

(integer) --


stringValues (list) --
An array of strings.

(string) --




blobValue (bytes) --
A value of BLOB data type.

booleanValue (boolean) --
A value of Boolean data type.

doubleValue (float) --
A value of double data type.

isNull (boolean) --
A NULL value.

longValue (integer) --
A value of long data type.

stringValue (string) --
A value of string data type.















Exceptions

RDSDataService.Client.exceptions.BadRequestException
RDSDataService.Client.exceptions.StatementTimeoutException
RDSDataService.Client.exceptions.InternalServerErrorException
RDSDataService.Client.exceptions.ForbiddenException
RDSDataService.Client.exceptions.ServiceUnavailableError


    :return: {
        'updateResults': [
            {
                'generatedFields': [
                    {
                        'arrayValue': {
                            'arrayValues': [
                                {'... recursive ...'},
                            ],
                            'booleanValues': [
                                True|False,
                            ],
                            'doubleValues': [
                                123.0,
                            ],
                            'longValues': [
                                123,
                            ],
                            'stringValues': [
                                'string',
                            ]
                        },
                        'blobValue': b'bytes',
                        'booleanValue': True|False,
                        'doubleValue': 123.0,
                        'isNull': True|False,
                        'longValue': 123,
                        'stringValue': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    (boolean) --
    
    """
    pass

def begin_transaction(database=None, resourceArn=None, schema=None, secretArn=None):
    """
    Starts a SQL transaction.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.begin_transaction(
        database='string',
        resourceArn='string',
        schema='string',
        secretArn='string'
    )
    
    
    :type database: string
    :param database: The name of the database.

    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.\n

    :type schema: string
    :param schema: The name of the database schema.

    :type secretArn: string
    :param secretArn: [REQUIRED]\nThe name or ARN of the secret that enables access to the DB cluster.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'transactionId': 'string'
}


Response Structure

(dict) --
The response elements represent the output of a request to start a SQL transaction.

transactionId (string) --
The transaction ID of the transaction started by the call.







Exceptions

RDSDataService.Client.exceptions.BadRequestException
RDSDataService.Client.exceptions.StatementTimeoutException
RDSDataService.Client.exceptions.InternalServerErrorException
RDSDataService.Client.exceptions.ForbiddenException
RDSDataService.Client.exceptions.ServiceUnavailableError


    :return: {
        'transactionId': 'string'
    }
    
    
    :returns: 
    RDSDataService.Client.exceptions.BadRequestException
    RDSDataService.Client.exceptions.StatementTimeoutException
    RDSDataService.Client.exceptions.InternalServerErrorException
    RDSDataService.Client.exceptions.ForbiddenException
    RDSDataService.Client.exceptions.ServiceUnavailableError
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def commit_transaction(resourceArn=None, secretArn=None, transactionId=None):
    """
    Ends a SQL transaction started with the BeginTransaction operation and commits the changes.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.commit_transaction(
        resourceArn='string',
        secretArn='string',
        transactionId='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.\n

    :type secretArn: string
    :param secretArn: [REQUIRED]\nThe name or ARN of the secret that enables access to the DB cluster.\n

    :type transactionId: string
    :param transactionId: [REQUIRED]\nThe identifier of the transaction to end and commit.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'transactionStatus': 'string'
}


Response Structure

(dict) --
The response elements represent the output of a commit transaction request.

transactionStatus (string) --
The status of the commit operation.







Exceptions

RDSDataService.Client.exceptions.BadRequestException
RDSDataService.Client.exceptions.StatementTimeoutException
RDSDataService.Client.exceptions.InternalServerErrorException
RDSDataService.Client.exceptions.ForbiddenException
RDSDataService.Client.exceptions.ServiceUnavailableError
RDSDataService.Client.exceptions.NotFoundException


    :return: {
        'transactionStatus': 'string'
    }
    
    
    :returns: 
    RDSDataService.Client.exceptions.BadRequestException
    RDSDataService.Client.exceptions.StatementTimeoutException
    RDSDataService.Client.exceptions.InternalServerErrorException
    RDSDataService.Client.exceptions.ForbiddenException
    RDSDataService.Client.exceptions.ServiceUnavailableError
    RDSDataService.Client.exceptions.NotFoundException
    
    """
    pass

def execute_sql(awsSecretStoreArn=None, database=None, dbClusterOrInstanceArn=None, schema=None, sqlStatements=None):
    """
    Runs one or more SQL statements.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.execute_sql(
        awsSecretStoreArn='string',
        database='string',
        dbClusterOrInstanceArn='string',
        schema='string',
        sqlStatements='string'
    )
    
    
    :type awsSecretStoreArn: string
    :param awsSecretStoreArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the secret that enables access to the DB cluster.\n

    :type database: string
    :param database: The name of the database.

    :type dbClusterOrInstanceArn: string
    :param dbClusterOrInstanceArn: [REQUIRED]\nThe ARN of the Aurora Serverless DB cluster.\n

    :type schema: string
    :param schema: The name of the database schema.

    :type sqlStatements: string
    :param sqlStatements: [REQUIRED]\nOne or more SQL statements to run on the DB cluster.\nYou can separate SQL statements from each other with a semicolon (;). Any valid SQL statement is permitted, including data definition, data manipulation, and commit statements.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'sqlStatementResults': [
        {
            'numberOfRecordsUpdated': 123,
            'resultFrame': {
                'records': [
                    {
                        'values': [
                            {
                                'arrayValues': [
                                    {'... recursive ...'},
                                ],
                                'bigIntValue': 123,
                                'bitValue': True|False,
                                'blobValue': b'bytes',
                                'doubleValue': 123.0,
                                'intValue': 123,
                                'isNull': True|False,
                                'realValue': ...,
                                'stringValue': 'string',
                                'structValue': {
                                    'attributes': [
                                        {'... recursive ...'},
                                    ]
                                }
                            },
                        ]
                    },
                ],
                'resultSetMetadata': {
                    'columnCount': 123,
                    'columnMetadata': [
                        {
                            'arrayBaseColumnType': 123,
                            'isAutoIncrement': True|False,
                            'isCaseSensitive': True|False,
                            'isCurrency': True|False,
                            'isSigned': True|False,
                            'label': 'string',
                            'name': 'string',
                            'nullable': 123,
                            'precision': 123,
                            'scale': 123,
                            'schemaName': 'string',
                            'tableName': 'string',
                            'type': 123,
                            'typeName': 'string'
                        },
                    ]
                }
            }
        },
    ]
}


Response Structure

(dict) --
The response elements represent the output of a request to run one or more SQL statements.

sqlStatementResults (list) --
The results of the SQL statement or statements.

(dict) --
The result of a SQL statement.

<important> <p>This data type is deprecated.</p> </important>


numberOfRecordsUpdated (integer) --
The number of records updated by a SQL statement.

resultFrame (dict) --
The result set of the SQL statement.

records (list) --
The records in the result set.

(dict) --
A record returned by a call.

values (list) --
The values returned in the record.

(dict) --
Contains the value of a column.

<important> <p>This data type is deprecated.</p> </important>


arrayValues (list) --
An array of column values.

(dict) --
Contains the value of a column.

<important> <p>This data type is deprecated.</p> </important>




bigIntValue (integer) --
A value for a column of big integer data type.

bitValue (boolean) --
A value for a column of BIT data type.

blobValue (bytes) --
A value for a column of BLOB data type.

doubleValue (float) --
A value for a column of double data type.

intValue (integer) --
A value for a column of integer data type.

isNull (boolean) --
A NULL value.

realValue (float) --
A value for a column of real data type.

stringValue (string) --
A value for a column of string data type.

structValue (dict) --
A value for a column of STRUCT data type.

attributes (list) --
The attributes returned in the record.

(dict) --
Contains the value of a column.

<important> <p>This data type is deprecated.</p> </important>














resultSetMetadata (dict) --
The result-set metadata in the result set.

columnCount (integer) --
The number of columns in the result set.

columnMetadata (list) --
The metadata of the columns in the result set.

(dict) --
Contains the metadata for a column.

arrayBaseColumnType (integer) --
The type of the column.

isAutoIncrement (boolean) --
A value that indicates whether the column increments automatically.

isCaseSensitive (boolean) --
A value that indicates whether the column is case-sensitive.

isCurrency (boolean) --
A value that indicates whether the column contains currency values.

isSigned (boolean) --
A value that indicates whether an integer column is signed.

label (string) --
The label for the column.

name (string) --
The name of the column.

nullable (integer) --
A value that indicates whether the column is nullable.

precision (integer) --
The precision value of a decimal number column.

scale (integer) --
The scale value of a decimal number column.

schemaName (string) --
The name of the schema that owns the table that includes the column.

tableName (string) --
The name of the table that includes the column.

type (integer) --
The type of the column.

typeName (string) --
The database-specific data type of the column.



















Exceptions

RDSDataService.Client.exceptions.BadRequestException
RDSDataService.Client.exceptions.InternalServerErrorException
RDSDataService.Client.exceptions.ForbiddenException
RDSDataService.Client.exceptions.ServiceUnavailableError


    :return: {
        'sqlStatementResults': [
            {
                'numberOfRecordsUpdated': 123,
                'resultFrame': {
                    'records': [
                        {
                            'values': [
                                {
                                    'arrayValues': [
                                        {'... recursive ...'},
                                    ],
                                    'bigIntValue': 123,
                                    'bitValue': True|False,
                                    'blobValue': b'bytes',
                                    'doubleValue': 123.0,
                                    'intValue': 123,
                                    'isNull': True|False,
                                    'realValue': ...,
                                    'stringValue': 'string',
                                    'structValue': {
                                        'attributes': [
                                            {'... recursive ...'},
                                        ]
                                    }
                                },
                            ]
                        },
                    ],
                    'resultSetMetadata': {
                        'columnCount': 123,
                        'columnMetadata': [
                            {
                                'arrayBaseColumnType': 123,
                                'isAutoIncrement': True|False,
                                'isCaseSensitive': True|False,
                                'isCurrency': True|False,
                                'isSigned': True|False,
                                'label': 'string',
                                'name': 'string',
                                'nullable': 123,
                                'precision': 123,
                                'scale': 123,
                                'schemaName': 'string',
                                'tableName': 'string',
                                'type': 123,
                                'typeName': 'string'
                            },
                        ]
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    RDSDataService.Client.exceptions.BadRequestException
    RDSDataService.Client.exceptions.InternalServerErrorException
    RDSDataService.Client.exceptions.ForbiddenException
    RDSDataService.Client.exceptions.ServiceUnavailableError
    
    """
    pass

def execute_statement(continueAfterTimeout=None, database=None, includeResultMetadata=None, parameters=None, resourceArn=None, resultSetOptions=None, schema=None, secretArn=None, sql=None, transactionId=None):
    """
    Runs a SQL statement against a database.
    The response size limit is 1 MB. If the call returns more than 1 MB of response data, the call is terminated.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.execute_statement(
        continueAfterTimeout=True|False,
        database='string',
        includeResultMetadata=True|False,
        parameters=[
            {
                'name': 'string',
                'typeHint': 'DATE'|'DECIMAL'|'TIME'|'TIMESTAMP',
                'value': {
                    'arrayValue': {
                        'arrayValues': [
                            {'... recursive ...'},
                        ],
                        'booleanValues': [
                            True|False,
                        ],
                        'doubleValues': [
                            123.0,
                        ],
                        'longValues': [
                            123,
                        ],
                        'stringValues': [
                            'string',
                        ]
                    },
                    'blobValue': b'bytes',
                    'booleanValue': True|False,
                    'doubleValue': 123.0,
                    'isNull': True|False,
                    'longValue': 123,
                    'stringValue': 'string'
                }
            },
        ],
        resourceArn='string',
        resultSetOptions={
            'decimalReturnType': 'DOUBLE_OR_LONG'|'STRING'
        },
        schema='string',
        secretArn='string',
        sql='string',
        transactionId='string'
    )
    
    
    :type continueAfterTimeout: boolean
    :param continueAfterTimeout: A value that indicates whether to continue running the statement after the call times out. By default, the statement stops running when the call times out.\n\nWarning\nFor DDL statements, we recommend continuing to run the statement after the call times out. When a DDL statement terminates before it is finished running, it can result in errors and possibly corrupted data structures.\n\n

    :type database: string
    :param database: The name of the database.

    :type includeResultMetadata: boolean
    :param includeResultMetadata: A value that indicates whether to include metadata in the results.

    :type parameters: list
    :param parameters: The parameters for the SQL statement.\n\nNote\nArray parameters are not supported.\n\n\n(dict) --A parameter used in a SQL statement.\n\nname (string) --The name of the parameter.\n\ntypeHint (string) --A hint that specifies the correct object type for data type mapping.\n\nValues:\n\nDECIMAL - The corresponding String parameter value is sent as an object of DECIMAL type to the database.\nTIMESTAMP - The corresponding String parameter value is sent as an object of TIMESTAMP type to the database. The accepted format is YYYY-MM-DD HH:MM:SS[.FFF] .\nTIME - The corresponding String parameter value is sent as an object of TIME type to the database. The accepted format is HH:MM:SS[.FFF] .\nDATE - The corresponding String parameter value is sent as an object of DATE type to the database. The accepted format is YYYY-MM-DD .\n\n\nvalue (dict) --The value of the parameter.\n\narrayValue (dict) --An array of values.\n\narrayValues (list) --An array of arrays.\n\n(dict) --Contains an array.\n\n\n\nbooleanValues (list) --An array of Boolean values.\n\n(boolean) --\n\n\ndoubleValues (list) --An array of integers.\n\n(float) --\n\n\nlongValues (list) --An array of floating point numbers.\n\n(integer) --\n\n\nstringValues (list) --An array of strings.\n\n(string) --\n\n\n\n\nblobValue (bytes) --A value of BLOB data type.\n\nbooleanValue (boolean) --A value of Boolean data type.\n\ndoubleValue (float) --A value of double data type.\n\nisNull (boolean) --A NULL value.\n\nlongValue (integer) --A value of long data type.\n\nstringValue (string) --A value of string data type.\n\n\n\n\n\n\n

    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.\n

    :type resultSetOptions: dict
    :param resultSetOptions: Options that control how the result set is returned.\n\ndecimalReturnType (string) --A value that indicates how a field of DECIMAL type is represented in the response. The value of STRING , the default, specifies that it is converted to a String value. The value of DOUBLE_OR_LONG specifies that it is converted to a Long value if its scale is 0, or to a Double value otherwise.\n\nWarning\nConversion to Double or Long can result in roundoff errors due to precision loss. We recommend converting to String, especially when working with currency values.\n\n\n\n

    :type schema: string
    :param schema: The name of the database schema.

    :type secretArn: string
    :param secretArn: [REQUIRED]\nThe name or ARN of the secret that enables access to the DB cluster.\n

    :type sql: string
    :param sql: [REQUIRED]\nThe SQL statement to run.\n

    :type transactionId: string
    :param transactionId: The identifier of a transaction that was started by using the BeginTransaction operation. Specify the transaction ID of the transaction that you want to include the SQL statement in.\nIf the SQL statement is not part of a transaction, don\'t set this parameter.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'columnMetadata': [
        {
            'arrayBaseColumnType': 123,
            'isAutoIncrement': True|False,
            'isCaseSensitive': True|False,
            'isCurrency': True|False,
            'isSigned': True|False,
            'label': 'string',
            'name': 'string',
            'nullable': 123,
            'precision': 123,
            'scale': 123,
            'schemaName': 'string',
            'tableName': 'string',
            'type': 123,
            'typeName': 'string'
        },
    ],
    'generatedFields': [
        {
            'arrayValue': {
                'arrayValues': [
                    {'... recursive ...'},
                ],
                'booleanValues': [
                    True|False,
                ],
                'doubleValues': [
                    123.0,
                ],
                'longValues': [
                    123,
                ],
                'stringValues': [
                    'string',
                ]
            },
            'blobValue': b'bytes',
            'booleanValue': True|False,
            'doubleValue': 123.0,
            'isNull': True|False,
            'longValue': 123,
            'stringValue': 'string'
        },
    ],
    'numberOfRecordsUpdated': 123,
    'records': [
        [
            {
                'arrayValue': {
                    'arrayValues': [
                        {'... recursive ...'},
                    ],
                    'booleanValues': [
                        True|False,
                    ],
                    'doubleValues': [
                        123.0,
                    ],
                    'longValues': [
                        123,
                    ],
                    'stringValues': [
                        'string',
                    ]
                },
                'blobValue': b'bytes',
                'booleanValue': True|False,
                'doubleValue': 123.0,
                'isNull': True|False,
                'longValue': 123,
                'stringValue': 'string'
            },
        ],
    ]
}


Response Structure

(dict) --
The response elements represent the output of a request to run a SQL statement against a database.

columnMetadata (list) --
Metadata for the columns included in the results.

(dict) --
Contains the metadata for a column.

arrayBaseColumnType (integer) --
The type of the column.

isAutoIncrement (boolean) --
A value that indicates whether the column increments automatically.

isCaseSensitive (boolean) --
A value that indicates whether the column is case-sensitive.

isCurrency (boolean) --
A value that indicates whether the column contains currency values.

isSigned (boolean) --
A value that indicates whether an integer column is signed.

label (string) --
The label for the column.

name (string) --
The name of the column.

nullable (integer) --
A value that indicates whether the column is nullable.

precision (integer) --
The precision value of a decimal number column.

scale (integer) --
The scale value of a decimal number column.

schemaName (string) --
The name of the schema that owns the table that includes the column.

tableName (string) --
The name of the table that includes the column.

type (integer) --
The type of the column.

typeName (string) --
The database-specific data type of the column.





generatedFields (list) --
Values for fields generated during the request.

<note> <p>The <code>generatedFields</code> data isn\'t supported by Aurora PostgreSQL. To get the values of generated fields, use the <code>RETURNING</code> clause. For more information, see <a href="https://www.postgresql.org/docs/10/dml-returning.html">Returning Data From Modified Rows</a> in the PostgreSQL documentation.</p> </note>


(dict) --
Contains a value.

arrayValue (dict) --
An array of values.

arrayValues (list) --
An array of arrays.

(dict) --
Contains an array.



booleanValues (list) --
An array of Boolean values.

(boolean) --


doubleValues (list) --
An array of integers.

(float) --


longValues (list) --
An array of floating point numbers.

(integer) --


stringValues (list) --
An array of strings.

(string) --




blobValue (bytes) --
A value of BLOB data type.

booleanValue (boolean) --
A value of Boolean data type.

doubleValue (float) --
A value of double data type.

isNull (boolean) --
A NULL value.

longValue (integer) --
A value of long data type.

stringValue (string) --
A value of string data type.





numberOfRecordsUpdated (integer) --
The number of records updated by the request.

records (list) --
The records returned by the SQL statement.

(list) --

(dict) --
Contains a value.

arrayValue (dict) --
An array of values.

arrayValues (list) --
An array of arrays.

(dict) --
Contains an array.



booleanValues (list) --
An array of Boolean values.

(boolean) --


doubleValues (list) --
An array of integers.

(float) --


longValues (list) --
An array of floating point numbers.

(integer) --


stringValues (list) --
An array of strings.

(string) --




blobValue (bytes) --
A value of BLOB data type.

booleanValue (boolean) --
A value of Boolean data type.

doubleValue (float) --
A value of double data type.

isNull (boolean) --
A NULL value.

longValue (integer) --
A value of long data type.

stringValue (string) --
A value of string data type.













Exceptions

RDSDataService.Client.exceptions.BadRequestException
RDSDataService.Client.exceptions.StatementTimeoutException
RDSDataService.Client.exceptions.InternalServerErrorException
RDSDataService.Client.exceptions.ForbiddenException
RDSDataService.Client.exceptions.ServiceUnavailableError


    :return: {
        'columnMetadata': [
            {
                'arrayBaseColumnType': 123,
                'isAutoIncrement': True|False,
                'isCaseSensitive': True|False,
                'isCurrency': True|False,
                'isSigned': True|False,
                'label': 'string',
                'name': 'string',
                'nullable': 123,
                'precision': 123,
                'scale': 123,
                'schemaName': 'string',
                'tableName': 'string',
                'type': 123,
                'typeName': 'string'
            },
        ],
        'generatedFields': [
            {
                'arrayValue': {
                    'arrayValues': [
                        {'... recursive ...'},
                    ],
                    'booleanValues': [
                        True|False,
                    ],
                    'doubleValues': [
                        123.0,
                    ],
                    'longValues': [
                        123,
                    ],
                    'stringValues': [
                        'string',
                    ]
                },
                'blobValue': b'bytes',
                'booleanValue': True|False,
                'doubleValue': 123.0,
                'isNull': True|False,
                'longValue': 123,
                'stringValue': 'string'
            },
        ],
        'numberOfRecordsUpdated': 123,
        'records': [
            [
                {
                    'arrayValue': {
                        'arrayValues': [
                            {'... recursive ...'},
                        ],
                        'booleanValues': [
                            True|False,
                        ],
                        'doubleValues': [
                            123.0,
                        ],
                        'longValues': [
                            123,
                        ],
                        'stringValues': [
                            'string',
                        ]
                    },
                    'blobValue': b'bytes',
                    'booleanValue': True|False,
                    'doubleValue': 123.0,
                    'isNull': True|False,
                    'longValue': 123,
                    'stringValue': 'string'
                },
            ],
        ]
    }
    
    
    :returns: 
    (boolean) --
    
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

def rollback_transaction(resourceArn=None, secretArn=None, transactionId=None):
    """
    Performs a rollback of a transaction. Rolling back a transaction cancels its changes.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.rollback_transaction(
        resourceArn='string',
        secretArn='string',
        transactionId='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.\n

    :type secretArn: string
    :param secretArn: [REQUIRED]\nThe name or ARN of the secret that enables access to the DB cluster.\n

    :type transactionId: string
    :param transactionId: [REQUIRED]\nThe identifier of the transaction to roll back.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'transactionStatus': 'string'
}


Response Structure

(dict) --
The response elements represent the output of a request to perform a rollback of a transaction.

transactionStatus (string) --
The status of the rollback operation.







Exceptions

RDSDataService.Client.exceptions.BadRequestException
RDSDataService.Client.exceptions.StatementTimeoutException
RDSDataService.Client.exceptions.InternalServerErrorException
RDSDataService.Client.exceptions.ForbiddenException
RDSDataService.Client.exceptions.ServiceUnavailableError
RDSDataService.Client.exceptions.NotFoundException


    :return: {
        'transactionStatus': 'string'
    }
    
    
    :returns: 
    RDSDataService.Client.exceptions.BadRequestException
    RDSDataService.Client.exceptions.StatementTimeoutException
    RDSDataService.Client.exceptions.InternalServerErrorException
    RDSDataService.Client.exceptions.ForbiddenException
    RDSDataService.Client.exceptions.ServiceUnavailableError
    RDSDataService.Client.exceptions.NotFoundException
    
    """
    pass

