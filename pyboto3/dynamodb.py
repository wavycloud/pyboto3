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

def batch_get_item(RequestItems=None, ReturnConsumedCapacity=None):
    """
    The BatchGetItem operation returns the attributes of one or more items from one or more tables. You identify requested items by primary key.
    A single operation can retrieve up to 16 MB of data, which can contain as many as 100 items. BatchGetItem returns a partial result if the response size limit is exceeded, the table\'s provisioned throughput is exceeded, or an internal processing failure occurs. If a partial result is returned, the operation returns a value for UnprocessedKeys . You can use this value to retry the operation starting with the next item to get.
    For example, if you ask to retrieve 100 items, but each individual item is 300 KB in size, the system returns 52 items (so as not to exceed the 16 MB limit). It also returns an appropriate UnprocessedKeys value so you can get the next page of results. If desired, your application can include its own logic to assemble the pages of results into one dataset.
    If none of the items can be processed due to insufficient provisioned throughput on all of the tables in the request, then BatchGetItem returns a ProvisionedThroughputExceededException . If at least one of the items is successfully processed, then BatchGetItem completes successfully, while returning the keys of the unread items in UnprocessedKeys .
    By default, BatchGetItem performs eventually consistent reads on every table in the request. If you want strongly consistent reads instead, you can set ConsistentRead to true for any or all tables.
    In order to minimize response latency, BatchGetItem retrieves items in parallel.
    When designing your application, keep in mind that DynamoDB does not return items in any particular order. To help parse the response by item, include the primary key values for the items in your request in the ProjectionExpression parameter.
    If a requested item does not exist, it is not returned in the result. Requests for nonexistent items consume the minimum read capacity units according to the type of read. For more information, see Working with Tables in the Amazon DynamoDB Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example reads multiple items from the Music table using a batch of three GetItem requests.  Only the AlbumTitle attribute is returned.
    Expected Output:
    
    :example: response = client.batch_get_item(
        RequestItems={
            'string': {
                'Keys': [
                    {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                ],
                'AttributesToGet': [
                    'string',
                ],
                'ConsistentRead': True|False,
                'ProjectionExpression': 'string',
                'ExpressionAttributeNames': {
                    'string': 'string'
                }
            }
        },
        ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE'
    )
    
    
    :type RequestItems: dict
    :param RequestItems: [REQUIRED]\nA map of one or more table names and, for each table, a map that describes one or more items to retrieve from that table. Each table name can be used only once per BatchGetItem request.\nEach element in the map of items to retrieve consists of the following:\n\nConsistentRead - If true , a strongly consistent read is used; if false (the default), an eventually consistent read is used.\nExpressionAttributeNames - One or more substitution tokens for attribute names in the ProjectionExpression parameter. The following are some use cases for using ExpressionAttributeNames :\nTo access an attribute whose name conflicts with a DynamoDB reserved word.\nTo create a placeholder for repeating occurrences of an attribute name in an expression.\nTo prevent special characters in an attribute name from being misinterpreted in an expression.\n\n\n\nUse the # character in an expression to dereference an attribute name. For example, consider the following attribute name:\n\n\nPercentile\n\n\nThe name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide ). To work around this, you could specify the following for ExpressionAttributeNames :\n\n\n{'#P':'Percentile'}\n\n\nYou could then use this substitution in an expression, as in this example:\n\n\n#P = :val\n\n\n\nNote\nTokens that begin with the : character are expression attribute values , which are placeholders for the actual value at runtime.\n\nFor more information about expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide .\n\nKeys - An array of primary key attribute values that define specific items in the table. For each primary key, you must provide all of the key attributes. For example, with a simple primary key, you only need to provide the partition key value. For a composite key, you must provide both the partition key value and the sort key value.\nProjectionExpression - A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas. If no attribute names are specified, then all attributes are returned. If any of the requested attributes are not found, they do not appear in the result. For more information, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide .\nAttributesToGet - This is a legacy parameter. Use ProjectionExpression instead. For more information, see AttributesToGet in the Amazon DynamoDB Developer Guide .\n\n\n(string) --\n(dict) --Represents a set of primary keys and, for each key, the attributes to retrieve from the table.\nFor each primary key, you must provide all of the key attributes. For example, with a simple primary key, you only need to provide the partition key. For a composite primary key, you must provide both the partition key and the sort key.\n\nKeys (list) -- [REQUIRED]The primary key attribute values that define the items and the attributes associated with the items.\n\n(dict) --\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\n\n\nAttributesToGet (list) --This is a legacy parameter. Use ProjectionExpression instead. For more information, see Legacy Conditional Parameters in the Amazon DynamoDB Developer Guide .\n\n(string) --\n\n\nConsistentRead (boolean) --The consistency of a read operation. If set to true , then a strongly consistent read is used; otherwise, an eventually consistent read is used.\n\nProjectionExpression (string) --A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the ProjectionExpression must be separated by commas.\nIf no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result.\nFor more information, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide .\n\nExpressionAttributeNames (dict) --One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames :\n\nTo access an attribute whose name conflicts with a DynamoDB reserved word.\nTo create a placeholder for repeating occurrences of an attribute name in an expression.\nTo prevent special characters in an attribute name from being misinterpreted in an expression.\n\nUse the # character in an expression to dereference an attribute name. For example, consider the following attribute name:\n\nPercentile\n\nThe name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide ). To work around this, you could specify the following for ExpressionAttributeNames :\n\n{'#P':'Percentile'}\n\nYou could then use this substitution in an expression, as in this example:\n\n#P = :val\n\n\nNote\nTokens that begin with the : character are expression attribute values , which are placeholders for the actual value at runtime.\n\nFor more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\n\n

    :type ReturnConsumedCapacity: string
    :param ReturnConsumedCapacity: Determines the level of detail about provisioned throughput consumption that is returned in the response:\n\nINDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem , do not access any indexes at all. In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s).\nTOTAL - The response includes only the aggregate ConsumedCapacity for the operation.\nNONE - No ConsumedCapacity details are included in the response.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Responses': {
        'string': [
            {
                'string': {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                }
            },
        ]
    },
    'UnprocessedKeys': {
        'string': {
            'Keys': [
                {
                    'string': {
                        'S': 'string',
                        'N': 'string',
                        'B': b'bytes',
                        'SS': [
                            'string',
                        ],
                        'NS': [
                            'string',
                        ],
                        'BS': [
                            b'bytes',
                        ],
                        'M': {
                            'string': {'... recursive ...'}
                        },
                        'L': [
                            {'... recursive ...'},
                        ],
                        'NULL': True|False,
                        'BOOL': True|False
                    }
                },
            ],
            'AttributesToGet': [
                'string',
            ],
            'ConsistentRead': True|False,
            'ProjectionExpression': 'string',
            'ExpressionAttributeNames': {
                'string': 'string'
            }
        }
    },
    'ConsumedCapacity': [
        {
            'TableName': 'string',
            'CapacityUnits': 123.0,
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'Table': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            },
            'LocalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            },
            'GlobalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            }
        },
    ]
}


Response Structure

(dict) --
Represents the output of a BatchGetItem operation.

Responses (dict) --
A map of table name to a list of items. Each object in Responses consists of a table name, along with a map of attribute data consisting of the data type and attribute value.

(string) --

(list) --

(dict) --

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true














UnprocessedKeys (dict) --
A map of tables and their respective keys that were not processed with the current response. The UnprocessedKeys value is in the same form as RequestItems , so the value can be provided directly to a subsequent BatchGetItem operation. For more information, see RequestItems in the Request Parameters section.
Each element consists of:

Keys - An array of primary key attribute values that define specific items in the table.
ProjectionExpression - One or more attributes to be retrieved from the table or index. By default, all attributes are returned. If a requested attribute is not found, it does not appear in the result.
ConsistentRead - The consistency of a read operation. If set to true , then a strongly consistent read is used; otherwise, an eventually consistent read is used.

If there are no unprocessed keys remaining, the response contains an empty UnprocessedKeys map.

(string) --

(dict) --
Represents a set of primary keys and, for each key, the attributes to retrieve from the table.
For each primary key, you must provide all of the key attributes. For example, with a simple primary key, you only need to provide the partition key. For a composite primary key, you must provide both the partition key and the sort key.

Keys (list) --
The primary key attribute values that define the items and the attributes associated with the items.

(dict) --

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true










AttributesToGet (list) --
This is a legacy parameter. Use ProjectionExpression instead. For more information, see Legacy Conditional Parameters in the Amazon DynamoDB Developer Guide .

(string) --


ConsistentRead (boolean) --
The consistency of a read operation. If set to true , then a strongly consistent read is used; otherwise, an eventually consistent read is used.

ProjectionExpression (string) --
A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the ProjectionExpression must be separated by commas.
If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result.
For more information, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide .

ExpressionAttributeNames (dict) --
One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames :

To access an attribute whose name conflicts with a DynamoDB reserved word.
To create a placeholder for repeating occurrences of an attribute name in an expression.
To prevent special characters in an attribute name from being misinterpreted in an expression.

Use the # character in an expression to dereference an attribute name. For example, consider the following attribute name:

Percentile

The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide ). To work around this, you could specify the following for ExpressionAttributeNames :

{"#P":"Percentile"}

You could then use this substitution in an expression, as in this example:

#P = :val


Note
Tokens that begin with the : character are expression attribute values , which are placeholders for the actual value at runtime.

For more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide .

(string) --
(string) --










ConsumedCapacity (list) --
The read capacity units consumed by the entire BatchGetItem operation.
Each element consists of:

TableName - The table that consumed the provisioned throughput.
CapacityUnits - The total number of capacity units consumed.


(dict) --
The capacity units consumed by an operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. ConsumedCapacity is only returned if the request asked for it. For more information, see Provisioned Throughput in the Amazon DynamoDB Developer Guide .

TableName (string) --
The name of the table that was affected by the operation.

CapacityUnits (float) --
The total number of capacity units consumed by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed by the operation.

WriteCapacityUnits (float) --
The total number of write capacity units consumed by the operation.

Table (dict) --
The amount of throughput consumed on the table affected by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.



LocalSecondaryIndexes (dict) --
The amount of throughput consumed on each local index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.







GlobalSecondaryIndexes (dict) --
The amount of throughput consumed on each global index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.

















Exceptions

DynamoDB.Client.exceptions.ProvisionedThroughputExceededException
DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.RequestLimitExceeded
DynamoDB.Client.exceptions.InternalServerError

Examples
This example reads multiple items from the Music table using a batch of three GetItem requests.  Only the AlbumTitle attribute is returned.
response = client.batch_get_item(
    RequestItems={
        'Music': {
            'Keys': [
                {
                    'Artist': {
                        'S': 'No One You Know',
                    },
                    'SongTitle': {
                        'S': 'Call Me Today',
                    },
                },
                {
                    'Artist': {
                        'S': 'Acme Band',
                    },
                    'SongTitle': {
                        'S': 'Happy Day',
                    },
                },
                {
                    'Artist': {
                        'S': 'No One You Know',
                    },
                    'SongTitle': {
                        'S': 'Scared of My Shadow',
                    },
                },
            ],
            'ProjectionExpression': 'AlbumTitle',
        },
    },
)

print(response)


Expected Output:
{
    'Responses': {
        'Music': [
            {
                'AlbumTitle': {
                    'S': 'Somewhat Famous',
                },
            },
            {
                'AlbumTitle': {
                    'S': 'Blue Sky Blues',
                },
            },
            {
                'AlbumTitle': {
                    'S': 'Louder Than Ever',
                },
            },
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Responses': {
            'string': [
                {
                    'string': {
                        'S': 'string',
                        'N': 'string',
                        'B': b'bytes',
                        'SS': [
                            'string',
                        ],
                        'NS': [
                            'string',
                        ],
                        'BS': [
                            b'bytes',
                        ],
                        'M': {
                            'string': {'... recursive ...'}
                        },
                        'L': [
                            {'... recursive ...'},
                        ],
                        'NULL': True|False,
                        'BOOL': True|False
                    }
                },
            ]
        },
        'UnprocessedKeys': {
            'string': {
                'Keys': [
                    {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                ],
                'AttributesToGet': [
                    'string',
                ],
                'ConsistentRead': True|False,
                'ProjectionExpression': 'string',
                'ExpressionAttributeNames': {
                    'string': 'string'
                }
            }
        },
        'ConsumedCapacity': [
            {
                'TableName': 'string',
                'CapacityUnits': 123.0,
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'Table': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                },
                'LocalSecondaryIndexes': {
                    'string': {
                        'ReadCapacityUnits': 123.0,
                        'WriteCapacityUnits': 123.0,
                        'CapacityUnits': 123.0
                    }
                },
                'GlobalSecondaryIndexes': {
                    'string': {
                        'ReadCapacityUnits': 123.0,
                        'WriteCapacityUnits': 123.0,
                        'CapacityUnits': 123.0
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def batch_write_item(RequestItems=None, ReturnConsumedCapacity=None, ReturnItemCollectionMetrics=None):
    """
    The BatchWriteItem operation puts or deletes multiple items in one or more tables. A single call to BatchWriteItem can write up to 16 MB of data, which can comprise as many as 25 put or delete requests. Individual items to be written can be as large as 400 KB.
    The individual PutItem and DeleteItem operations specified in BatchWriteItem are atomic; however BatchWriteItem as a whole is not. If any requested operations fail because the table\'s provisioned throughput is exceeded or an internal processing failure occurs, the failed operations are returned in the UnprocessedItems response parameter. You can investigate and optionally resend the requests. Typically, you would call BatchWriteItem in a loop. Each iteration would check for unprocessed items and submit a new BatchWriteItem request with those unprocessed items until all items have been processed.
    If none of the items can be processed due to insufficient provisioned throughput on all of the tables in the request, then BatchWriteItem returns a ProvisionedThroughputExceededException .
    With BatchWriteItem , you can efficiently write or delete large amounts of data, such as from Amazon EMR, or copy data from another database into DynamoDB. In order to improve performance with these large-scale operations, BatchWriteItem does not behave in the same way as individual PutItem and DeleteItem calls would. For example, you cannot specify conditions on individual put and delete requests, and BatchWriteItem does not return deleted items in the response.
    If you use a programming language that supports concurrency, you can use threads to write items in parallel. Your application must include the necessary logic to manage the threads. With languages that don\'t support threading, you must update or delete the specified items one at a time. In both situations, BatchWriteItem performs the specified put and delete operations in parallel, giving you the power of the thread pool approach without having to introduce complexity into your application.
    Parallel processing reduces latency, but each specified put and delete request consumes the same number of write capacity units whether it is processed in parallel or not. Delete operations on nonexistent items consume one write capacity unit.
    If one or more of the following is true, DynamoDB rejects the entire batch write operation:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example adds three new items to the Music table using a batch of three PutItem requests.
    Expected Output:
    
    :example: response = client.batch_write_item(
        RequestItems={
            'string': [
                {
                    'PutRequest': {
                        'Item': {
                            'string': {
                                'S': 'string',
                                'N': 'string',
                                'B': b'bytes',
                                'SS': [
                                    'string',
                                ],
                                'NS': [
                                    'string',
                                ],
                                'BS': [
                                    b'bytes',
                                ],
                                'M': {
                                    'string': {'... recursive ...'}
                                },
                                'L': [
                                    {'... recursive ...'},
                                ],
                                'NULL': True|False,
                                'BOOL': True|False
                            }
                        }
                    },
                    'DeleteRequest': {
                        'Key': {
                            'string': {
                                'S': 'string',
                                'N': 'string',
                                'B': b'bytes',
                                'SS': [
                                    'string',
                                ],
                                'NS': [
                                    'string',
                                ],
                                'BS': [
                                    b'bytes',
                                ],
                                'M': {
                                    'string': {'... recursive ...'}
                                },
                                'L': [
                                    {'... recursive ...'},
                                ],
                                'NULL': True|False,
                                'BOOL': True|False
                            }
                        }
                    }
                },
            ]
        },
        ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
        ReturnItemCollectionMetrics='SIZE'|'NONE'
    )
    
    
    :type RequestItems: dict
    :param RequestItems: [REQUIRED]\nA map of one or more table names and, for each table, a list of operations to be performed (DeleteRequest or PutRequest ). Each element in the map consists of the following:\n\nDeleteRequest - Perform a DeleteItem operation on the specified item. The item to be deleted is identified by a Key subelement:\nKey - A map of primary key attribute values that uniquely identify the item. Each entry in this map consists of an attribute name and an attribute value. For each primary key, you must provide all of the key attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.\n\n\nPutRequest - Perform a PutItem operation on the specified item. The item to be put is identified by an Item subelement:\nItem - A map of attributes and their values. Each entry in this map consists of an attribute name and an attribute value. Attribute values must not be null; string and binary type attributes must have lengths greater than zero; and set type attributes must not be empty. Requests that contain empty values are rejected with a ValidationException exception. If you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table\'s attribute definition.\n\n\n\n\n(string) --\n(list) --\n(dict) --Represents an operation to perform - either DeleteItem or PutItem . You can only request one of these operations, not both, in a single WriteRequest . If you do need to perform both of these operations, you need to provide two separate WriteRequest objects.\n\nPutRequest (dict) --A request to perform a PutItem operation.\n\nItem (dict) -- [REQUIRED]A map of attribute name to attribute values, representing the primary key of an item to be processed by PutItem . All of the table\'s primary key attributes must be specified, and their data types must match those of the table\'s key schema. If any attributes are present in the item that are part of an index key schema for the table, their types must match the index key schema.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\n\n\nDeleteRequest (dict) --A request to perform a DeleteItem operation.\n\nKey (dict) -- [REQUIRED]A map of attribute name to attribute values, representing the primary key of the item to delete. All of the table\'s primary key attributes must be specified, and their data types must match those of the table\'s key schema.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

    :type ReturnConsumedCapacity: string
    :param ReturnConsumedCapacity: Determines the level of detail about provisioned throughput consumption that is returned in the response:\n\nINDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem , do not access any indexes at all. In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s).\nTOTAL - The response includes only the aggregate ConsumedCapacity for the operation.\nNONE - No ConsumedCapacity details are included in the response.\n\n

    :type ReturnItemCollectionMetrics: string
    :param ReturnItemCollectionMetrics: Determines whether item collection metrics are returned. If set to SIZE , the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'UnprocessedItems': {
        'string': [
            {
                'PutRequest': {
                    'Item': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    }
                },
                'DeleteRequest': {
                    'Key': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    }
                }
            },
        ]
    },
    'ItemCollectionMetrics': {
        'string': [
            {
                'ItemCollectionKey': {
                    'string': {
                        'S': 'string',
                        'N': 'string',
                        'B': b'bytes',
                        'SS': [
                            'string',
                        ],
                        'NS': [
                            'string',
                        ],
                        'BS': [
                            b'bytes',
                        ],
                        'M': {
                            'string': {'... recursive ...'}
                        },
                        'L': [
                            {'... recursive ...'},
                        ],
                        'NULL': True|False,
                        'BOOL': True|False
                    }
                },
                'SizeEstimateRangeGB': [
                    123.0,
                ]
            },
        ]
    },
    'ConsumedCapacity': [
        {
            'TableName': 'string',
            'CapacityUnits': 123.0,
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'Table': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            },
            'LocalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            },
            'GlobalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            }
        },
    ]
}


Response Structure

(dict) --
Represents the output of a BatchWriteItem operation.

UnprocessedItems (dict) --
A map of tables and requests against those tables that were not processed. The UnprocessedItems value is in the same form as RequestItems , so you can provide this value directly to a subsequent BatchGetItem operation. For more information, see RequestItems in the Request Parameters section.
Each UnprocessedItems entry consists of a table name and, for that table, a list of operations to perform (DeleteRequest or PutRequest ).

DeleteRequest - Perform a DeleteItem operation on the specified item. The item to be deleted is identified by a Key subelement:
Key - A map of primary key attribute values that uniquely identify the item. Each entry in this map consists of an attribute name and an attribute value.


PutRequest - Perform a PutItem operation on the specified item. The item to be put is identified by an Item subelement:
Item - A map of attributes and their values. Each entry in this map consists of an attribute name and an attribute value. Attribute values must not be null; string and binary type attributes must have lengths greater than zero; and set type attributes must not be empty. Requests that contain empty values will be rejected with a ValidationException exception. If you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table\'s attribute definition.



If there are no unprocessed items remaining, the response contains an empty UnprocessedItems map.

(string) --

(list) --

(dict) --
Represents an operation to perform - either DeleteItem or PutItem . You can only request one of these operations, not both, in a single WriteRequest . If you do need to perform both of these operations, you need to provide two separate WriteRequest objects.

PutRequest (dict) --
A request to perform a PutItem operation.

Item (dict) --
A map of attribute name to attribute values, representing the primary key of an item to be processed by PutItem . All of the table\'s primary key attributes must be specified, and their data types must match those of the table\'s key schema. If any attributes are present in the item that are part of an index key schema for the table, their types must match the index key schema.

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true










DeleteRequest (dict) --
A request to perform a DeleteItem operation.

Key (dict) --
A map of attribute name to attribute values, representing the primary key of the item to delete. All of the table\'s primary key attributes must be specified, and their data types must match those of the table\'s key schema.

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true


















ItemCollectionMetrics (dict) --
A list of tables that were processed by BatchWriteItem and, for each table, information about any item collections that were affected by individual DeleteItem or PutItem operations.
Each entry consists of the following subelements:

ItemCollectionKey - The partition key value of the item collection. This is the same as the partition key value of the item.
SizeEstimateRangeGB - An estimate of item collection size, expressed in GB. This is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on the table. Use this estimate to measure whether a local secondary index is approaching its size limit. The estimate is subject to change over time; therefore, do not rely on the precision or accuracy of the estimate.


(string) --

(list) --

(dict) --
Information about item collections, if any, that were affected by the operation. ItemCollectionMetrics is only returned if the request asked for it. If the table does not have any local secondary indexes, this information is not returned in the response.

ItemCollectionKey (dict) --
The partition key value of the item collection. This value is the same as the partition key value of the item.

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true








SizeEstimateRangeGB (list) --
An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit.
The estimate is subject to change over time; therefore, do not rely on the precision or accuracy of the estimate.

(float) --










ConsumedCapacity (list) --
The capacity units consumed by the entire BatchWriteItem operation.
Each element consists of:

TableName - The table that consumed the provisioned throughput.
CapacityUnits - The total number of capacity units consumed.


(dict) --
The capacity units consumed by an operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. ConsumedCapacity is only returned if the request asked for it. For more information, see Provisioned Throughput in the Amazon DynamoDB Developer Guide .

TableName (string) --
The name of the table that was affected by the operation.

CapacityUnits (float) --
The total number of capacity units consumed by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed by the operation.

WriteCapacityUnits (float) --
The total number of write capacity units consumed by the operation.

Table (dict) --
The amount of throughput consumed on the table affected by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.



LocalSecondaryIndexes (dict) --
The amount of throughput consumed on each local index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.







GlobalSecondaryIndexes (dict) --
The amount of throughput consumed on each global index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.

















Exceptions

DynamoDB.Client.exceptions.ProvisionedThroughputExceededException
DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.ItemCollectionSizeLimitExceededException
DynamoDB.Client.exceptions.RequestLimitExceeded
DynamoDB.Client.exceptions.InternalServerError

Examples
This example adds three new items to the Music table using a batch of three PutItem requests.
response = client.batch_write_item(
    RequestItems={
        'Music': [
            {
                'PutRequest': {
                    'Item': {
                        'AlbumTitle': {
                            'S': 'Somewhat Famous',
                        },
                        'Artist': {
                            'S': 'No One You Know',
                        },
                        'SongTitle': {
                            'S': 'Call Me Today',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'AlbumTitle': {
                            'S': 'Songs About Life',
                        },
                        'Artist': {
                            'S': 'Acme Band',
                        },
                        'SongTitle': {
                            'S': 'Happy Day',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'AlbumTitle': {
                            'S': 'Blue Sky Blues',
                        },
                        'Artist': {
                            'S': 'No One You Know',
                        },
                        'SongTitle': {
                            'S': 'Scared of My Shadow',
                        },
                    },
                },
            },
        ],
    },
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'UnprocessedItems': {
            'string': [
                {
                    'PutRequest': {
                        'Item': {
                            'string': {
                                'S': 'string',
                                'N': 'string',
                                'B': b'bytes',
                                'SS': [
                                    'string',
                                ],
                                'NS': [
                                    'string',
                                ],
                                'BS': [
                                    b'bytes',
                                ],
                                'M': {
                                    'string': {'... recursive ...'}
                                },
                                'L': [
                                    {'... recursive ...'},
                                ],
                                'NULL': True|False,
                                'BOOL': True|False
                            }
                        }
                    },
                    'DeleteRequest': {
                        'Key': {
                            'string': {
                                'S': 'string',
                                'N': 'string',
                                'B': b'bytes',
                                'SS': [
                                    'string',
                                ],
                                'NS': [
                                    'string',
                                ],
                                'BS': [
                                    b'bytes',
                                ],
                                'M': {
                                    'string': {'... recursive ...'}
                                },
                                'L': [
                                    {'... recursive ...'},
                                ],
                                'NULL': True|False,
                                'BOOL': True|False
                            }
                        }
                    }
                },
            ]
        },
        'ItemCollectionMetrics': {
            'string': [
                {
                    'ItemCollectionKey': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                    'SizeEstimateRangeGB': [
                        123.0,
                    ]
                },
            ]
        },
        'ConsumedCapacity': [
            {
                'TableName': 'string',
                'CapacityUnits': 123.0,
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'Table': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                },
                'LocalSecondaryIndexes': {
                    'string': {
                        'ReadCapacityUnits': 123.0,
                        'WriteCapacityUnits': 123.0,
                        'CapacityUnits': 123.0
                    }
                },
                'GlobalSecondaryIndexes': {
                    'string': {
                        'ReadCapacityUnits': 123.0,
                        'WriteCapacityUnits': 123.0,
                        'CapacityUnits': 123.0
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    RequestItems (dict) -- [REQUIRED]
    A map of one or more table names and, for each table, a list of operations to be performed (DeleteRequest or PutRequest ). Each element in the map consists of the following:
    
    DeleteRequest - Perform a DeleteItem operation on the specified item. The item to be deleted is identified by a Key subelement:
    Key - A map of primary key attribute values that uniquely identify the item. Each entry in this map consists of an attribute name and an attribute value. For each primary key, you must provide all of the key attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.
    
    
    PutRequest - Perform a PutItem operation on the specified item. The item to be put is identified by an Item subelement:
    Item - A map of attributes and their values. Each entry in this map consists of an attribute name and an attribute value. Attribute values must not be null; string and binary type attributes must have lengths greater than zero; and set type attributes must not be empty. Requests that contain empty values are rejected with a ValidationException exception. If you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table\'s attribute definition.
    
    
    
    
    (string) --
    (list) --
    (dict) --Represents an operation to perform - either DeleteItem or PutItem . You can only request one of these operations, not both, in a single WriteRequest . If you do need to perform both of these operations, you need to provide two separate WriteRequest objects.
    
    PutRequest (dict) --A request to perform a PutItem operation.
    
    Item (dict) -- [REQUIRED]A map of attribute name to attribute values, representing the primary key of an item to be processed by PutItem . All of the table\'s primary key attributes must be specified, and their data types must match those of the table\'s key schema. If any attributes are present in the item that are part of an index key schema for the table, their types must match the index key schema.
    
    (string) --
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    S (string) --An attribute of type String. For example:
    
    "S": "Hello"
    
    N (string) --An attribute of type Number. For example:
    
    "N": "123.45"
    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
    
    B (bytes) --An attribute of type Binary. For example:
    
    "B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"
    
    SS (list) --An attribute of type String Set. For example:
    
    "SS": ["Giraffe", "Hippo" ,"Zebra"]
    
    (string) --
    
    
    NS (list) --An attribute of type Number Set. For example:
    
    "NS": ["42.2", "-19", "7.5", "3.14"]
    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
    
    (string) --
    
    
    BS (list) --An attribute of type Binary Set. For example:
    
    "BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]
    
    (bytes) --
    
    
    M (dict) --An attribute of type Map. For example:
    
    "M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}
    
    (string) --
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    
    
    
    
    L (list) --An attribute of type List. For example:
    
    "L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]
    
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    
    
    NULL (boolean) --An attribute of type Null. For example:
    
    "NULL": true
    
    BOOL (boolean) --An attribute of type Boolean. For example:
    
    "BOOL": true
    
    
    
    
    
    
    
    
    
    DeleteRequest (dict) --A request to perform a DeleteItem operation.
    
    Key (dict) -- [REQUIRED]A map of attribute name to attribute values, representing the primary key of the item to delete. All of the table\'s primary key attributes must be specified, and their data types must match those of the table\'s key schema.
    
    (string) --
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    S (string) --An attribute of type String. For example:
    
    "S": "Hello"
    
    N (string) --An attribute of type Number. For example:
    
    "N": "123.45"
    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
    
    B (bytes) --An attribute of type Binary. For example:
    
    "B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"
    
    SS (list) --An attribute of type String Set. For example:
    
    "SS": ["Giraffe", "Hippo" ,"Zebra"]
    
    (string) --
    
    
    NS (list) --An attribute of type Number Set. For example:
    
    "NS": ["42.2", "-19", "7.5", "3.14"]
    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
    
    (string) --
    
    
    BS (list) --An attribute of type Binary Set. For example:
    
    "BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]
    
    (bytes) --
    
    
    M (dict) --An attribute of type Map. For example:
    
    "M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}
    
    (string) --
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    
    
    
    
    L (list) --An attribute of type List. For example:
    
    "L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]
    
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    
    
    NULL (boolean) --An attribute of type Null. For example:
    
    "NULL": true
    
    BOOL (boolean) --An attribute of type Boolean. For example:
    
    "BOOL": true
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ReturnConsumedCapacity (string) -- Determines the level of detail about provisioned throughput consumption that is returned in the response:
    
    INDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem , do not access any indexes at all. In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s).
    TOTAL - The response includes only the aggregate ConsumedCapacity for the operation.
    NONE - No ConsumedCapacity details are included in the response.
    
    
    ReturnItemCollectionMetrics (string) -- Determines whether item collection metrics are returned. If set to SIZE , the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_backup(TableName=None, BackupName=None):
    """
    Creates a backup for an existing table.
    Each time you create an on-demand backup, the entire table data is backed up. There is no limit to the number of on-demand backups that can be taken.
    When you create an on-demand backup, a time marker of the request is cataloged, and the backup is created asynchronously, by applying all changes until the time of the request to the last full table snapshot. Backup requests are processed instantaneously and become available for restore within minutes.
    You can call CreateBackup at a maximum rate of 50 times per second.
    All backups in DynamoDB work without consuming any provisioned throughput on the table.
    If you submit a backup request on 2018-12-14 at 14:25:00, the backup is guaranteed to contain all data committed to the table up to 14:24:00, and data committed after 14:26:00 will not be. The backup might contain data modifications made between 14:24:00 and 14:26:00. On-demand backup does not support causal consistency.
    Along with data, the following are also included on the backups:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_backup(
        TableName='string',
        BackupName='string'
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table.\n

    :type BackupName: string
    :param BackupName: [REQUIRED]\nSpecified name for the backup.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'BackupDetails': {
        'BackupArn': 'string',
        'BackupName': 'string',
        'BackupSizeBytes': 123,
        'BackupStatus': 'CREATING'|'DELETED'|'AVAILABLE',
        'BackupType': 'USER'|'SYSTEM'|'AWS_BACKUP',
        'BackupCreationDateTime': datetime(2015, 1, 1),
        'BackupExpiryDateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

BackupDetails (dict) --
Contains the details of the backup created for the table.

BackupArn (string) --
ARN associated with the backup.

BackupName (string) --
Name of the requested backup.

BackupSizeBytes (integer) --
Size of the backup in bytes.

BackupStatus (string) --
Backup can be in one of the following states: CREATING, ACTIVE, DELETED.

BackupType (string) --
BackupType:

USER - You create and manage these using the on-demand backup feature.
SYSTEM - If you delete a table with point-in-time recovery enabled, a SYSTEM backup is automatically created and is retained for 35 days (at no additional cost). System backups allow you to restore the deleted table to the state it was in just before the point of deletion.
AWS_BACKUP - On-demand backup created by you from AWS Backup service.


BackupCreationDateTime (datetime) --
Time at which the backup was created. This is the request time of the backup.

BackupExpiryDateTime (datetime) --
Time at which the automatic on-demand backup created by DynamoDB will expire. This SYSTEM on-demand backup expires automatically 35 days after its creation.









Exceptions

DynamoDB.Client.exceptions.TableNotFoundException
DynamoDB.Client.exceptions.TableInUseException
DynamoDB.Client.exceptions.ContinuousBackupsUnavailableException
DynamoDB.Client.exceptions.BackupInUseException
DynamoDB.Client.exceptions.LimitExceededException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'BackupDetails': {
            'BackupArn': 'string',
            'BackupName': 'string',
            'BackupSizeBytes': 123,
            'BackupStatus': 'CREATING'|'DELETED'|'AVAILABLE',
            'BackupType': 'USER'|'SYSTEM'|'AWS_BACKUP',
            'BackupCreationDateTime': datetime(2015, 1, 1),
            'BackupExpiryDateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    TableName (string) -- [REQUIRED]
    The name of the table.
    
    BackupName (string) -- [REQUIRED]
    Specified name for the backup.
    
    
    """
    pass

def create_global_table(GlobalTableName=None, ReplicationGroup=None):
    """
    Creates a global table from an existing table. A global table creates a replication relationship between two or more DynamoDB tables with the same table name in the provided Regions.
    If you want to add a new replica table to a global table, each of the following conditions must be true:
    If global secondary indexes are specified, then the following conditions must also be met:
    If local secondary indexes are specified, then the following conditions must also be met:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_global_table(
        GlobalTableName='string',
        ReplicationGroup=[
            {
                'RegionName': 'string'
            },
        ]
    )
    
    
    :type GlobalTableName: string
    :param GlobalTableName: [REQUIRED]\nThe global table name.\n

    :type ReplicationGroup: list
    :param ReplicationGroup: [REQUIRED]\nThe Regions where the global table needs to be created.\n\n(dict) --Represents the properties of a replica.\n\nRegionName (string) --The Region where the replica needs to be created.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalTableDescription': {
        'ReplicationGroup': [
            {
                'RegionName': 'string',
                'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                'ReplicaStatusDescription': 'string',
                'ReplicaStatusPercentProgress': 'string',
                'KMSMasterKeyId': 'string',
                'ProvisionedThroughputOverride': {
                    'ReadCapacityUnits': 123
                },
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'ProvisionedThroughputOverride': {
                            'ReadCapacityUnits': 123
                        }
                    },
                ]
            },
        ],
        'GlobalTableArn': 'string',
        'CreationDateTime': datetime(2015, 1, 1),
        'GlobalTableStatus': 'CREATING'|'ACTIVE'|'DELETING'|'UPDATING',
        'GlobalTableName': 'string'
    }
}


Response Structure

(dict) --

GlobalTableDescription (dict) --
Contains the details of the global table.

ReplicationGroup (list) --
The Regions where the global table has replicas.

(dict) --
Contains the details of the replica.

RegionName (string) --
The name of the Region.

ReplicaStatus (string) --
The current state of the replica:

CREATING - The replica is being created.
UPDATING - The replica is being updated.
DELETING - The replica is being deleted.
ACTIVE - The replica is ready for use.


ReplicaStatusDescription (string) --
Detailed information about the replica status.

ReplicaStatusPercentProgress (string) --
Specifies the progress of a Create, Update, or Delete action on the replica as a percentage.

KMSMasterKeyId (string) --
The AWS KMS customer master key (CMK) of the replica that will be used for AWS KMS encryption.

ProvisionedThroughputOverride (dict) --
Replica-specific provisioned throughput. If not described, uses the source table\'s provisioned throughput settings.

ReadCapacityUnits (integer) --
Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.



GlobalSecondaryIndexes (list) --
Replica-specific global secondary index settings.

(dict) --
Represents the properties of a replica global secondary index.

IndexName (string) --
The name of the global secondary index.

ProvisionedThroughputOverride (dict) --
If not described, uses the source table GSI\'s read capacity settings.

ReadCapacityUnits (integer) --
Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.











GlobalTableArn (string) --
The unique identifier of the global table.

CreationDateTime (datetime) --
The creation time of the global table.

GlobalTableStatus (string) --
The current state of the global table:

CREATING - The global table is being created.
UPDATING - The global table is being updated.
DELETING - The global table is being deleted.
ACTIVE - The global table is ready for use.


GlobalTableName (string) --
The global table name.









Exceptions

DynamoDB.Client.exceptions.LimitExceededException
DynamoDB.Client.exceptions.InternalServerError
DynamoDB.Client.exceptions.GlobalTableAlreadyExistsException
DynamoDB.Client.exceptions.TableNotFoundException


    :return: {
        'GlobalTableDescription': {
            'ReplicationGroup': [
                {
                    'RegionName': 'string',
                    'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                    'ReplicaStatusDescription': 'string',
                    'ReplicaStatusPercentProgress': 'string',
                    'KMSMasterKeyId': 'string',
                    'ProvisionedThroughputOverride': {
                        'ReadCapacityUnits': 123
                    },
                    'GlobalSecondaryIndexes': [
                        {
                            'IndexName': 'string',
                            'ProvisionedThroughputOverride': {
                                'ReadCapacityUnits': 123
                            }
                        },
                    ]
                },
            ],
            'GlobalTableArn': 'string',
            'CreationDateTime': datetime(2015, 1, 1),
            'GlobalTableStatus': 'CREATING'|'ACTIVE'|'DELETING'|'UPDATING',
            'GlobalTableName': 'string'
        }
    }
    
    
    :returns: 
    The global secondary indexes must have the same name.
    The global secondary indexes must have the same hash key and sort key (if present).
    
    """
    pass

def create_table(AttributeDefinitions=None, TableName=None, KeySchema=None, LocalSecondaryIndexes=None, GlobalSecondaryIndexes=None, BillingMode=None, ProvisionedThroughput=None, StreamSpecification=None, SSESpecification=None, Tags=None):
    """
    The CreateTable operation adds a new table to your account. In an AWS account, table names must be unique within each Region. That is, you can have two tables with same name if you create the tables in different Regions.
    You can optionally define secondary indexes on the new table, as part of the CreateTable operation. If you want to create multiple tables with secondary indexes on them, you must create the tables sequentially. Only one table with secondary indexes can be in the CREATING state at any given time.
    You can use the DescribeTable action to check the table status.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example creates a table named Music.
    Expected Output:
    
    :example: response = client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'string',
                'AttributeType': 'S'|'N'|'B'
            },
        ],
        TableName='string',
        KeySchema=[
            {
                'AttributeName': 'string',
                'KeyType': 'HASH'|'RANGE'
            },
        ],
        LocalSecondaryIndexes=[
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                }
            },
        ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                }
            },
        ],
        BillingMode='PROVISIONED'|'PAY_PER_REQUEST',
        ProvisionedThroughput={
            'ReadCapacityUnits': 123,
            'WriteCapacityUnits': 123
        },
        StreamSpecification={
            'StreamEnabled': True|False,
            'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
        },
        SSESpecification={
            'Enabled': True|False,
            'SSEType': 'AES256'|'KMS',
            'KMSMasterKeyId': 'string'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type AttributeDefinitions: list
    :param AttributeDefinitions: [REQUIRED]\nAn array of attributes that describe the key schema for the table and indexes.\n\n(dict) --Represents an attribute for describing the key schema for the table and indexes.\n\nAttributeName (string) -- [REQUIRED]A name for the attribute.\n\nAttributeType (string) -- [REQUIRED]The data type for the attribute, where:\n\nS - the attribute is of type String\nN - the attribute is of type Number\nB - the attribute is of type Binary\n\n\n\n\n\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table to create.\n

    :type KeySchema: list
    :param KeySchema: [REQUIRED]\nSpecifies the attributes that make up the primary key for a table or an index. The attributes in KeySchema must also be defined in the AttributeDefinitions array. For more information, see Data Model in the Amazon DynamoDB Developer Guide .\nEach KeySchemaElement in the array is composed of:\n\nAttributeName - The name of this key attribute.\nKeyType - The role that the key attribute will assume:\nHASH - partition key\nRANGE - sort key\n\n\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from the DynamoDB usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\nFor a simple primary key (partition key), you must provide exactly one element with a KeyType of HASH .\nFor a composite primary key (partition key and sort key), you must provide exactly two elements, in this order: The first element must have a KeyType of HASH , and the second element must have a KeyType of RANGE .\nFor more information, see Working with Tables in the Amazon DynamoDB Developer Guide .\n\n(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.\nA KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.\nA KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.\n\nAttributeName (string) -- [REQUIRED]The name of a key attribute.\n\nKeyType (string) -- [REQUIRED]The role that this key attribute will assume:\n\nHASH - partition key\nRANGE - sort key\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\n\n\n\n\n

    :type LocalSecondaryIndexes: list
    :param LocalSecondaryIndexes: One or more local secondary indexes (the maximum is 5) to be created on the table. Each index is scoped to a given partition key value. There is a 10 GB size limit per partition key value; otherwise, the size of a local secondary index is unconstrained.\nEach local secondary index in the array includes the following:\n\nIndexName - The name of the local secondary index. Must be unique only for this table.\nKeySchema - Specifies the key schema for the local secondary index. The key schema must begin with the same partition key as the table.\nProjection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:\nProjectionType - One of the following:\nKEYS_ONLY - Only the index and primary keys are projected into the index.\nINCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .\nALL - All of the table attributes are projected into the index.\n\n\nNonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes , summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.\n\n\n\n\n(dict) --Represents the properties of a local secondary index.\n\nIndexName (string) -- [REQUIRED]The name of the local secondary index. The name must be unique among all other indexes on this table.\n\nKeySchema (list) -- [REQUIRED]The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:\n\nHASH - partition key\nRANGE - sort key\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\n\n(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.\nA KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.\nA KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.\n\nAttributeName (string) -- [REQUIRED]The name of a key attribute.\n\nKeyType (string) -- [REQUIRED]The role that this key attribute will assume:\n\nHASH - partition key\nRANGE - sort key\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\n\n\n\n\n\nProjection (dict) -- [REQUIRED]Represents attributes that are copied (projected) from the table into the local secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.\n\nProjectionType (string) --The set of attributes that are projected into the index:\n\nKEYS_ONLY - Only the index and primary keys are projected into the index.\nINCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .\nALL - All of the table attributes are projected into the index.\n\n\nNonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.\nFor local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.\n\n(string) --\n\n\n\n\n\n\n\n

    :type GlobalSecondaryIndexes: list
    :param GlobalSecondaryIndexes: One or more global secondary indexes (the maximum is 20) to be created on the table. Each global secondary index in the array includes the following:\n\nIndexName - The name of the global secondary index. Must be unique only for this table.\nKeySchema - Specifies the key schema for the global secondary index.\nProjection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:\nProjectionType - One of the following:\nKEYS_ONLY - Only the index and primary keys are projected into the index.\nINCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .\nALL - All of the table attributes are projected into the index.\n\n\nNonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes , summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.\n\n\nProvisionedThroughput - The provisioned throughput settings for the global secondary index, consisting of read and write capacity units.\n\n\n(dict) --Represents the properties of a global secondary index.\n\nIndexName (string) -- [REQUIRED]The name of the global secondary index. The name must be unique among all other indexes on this table.\n\nKeySchema (list) -- [REQUIRED]The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:\n\nHASH - partition key\nRANGE - sort key\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\n\n(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.\nA KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.\nA KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.\n\nAttributeName (string) -- [REQUIRED]The name of a key attribute.\n\nKeyType (string) -- [REQUIRED]The role that this key attribute will assume:\n\nHASH - partition key\nRANGE - sort key\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\n\n\n\n\n\nProjection (dict) -- [REQUIRED]Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.\n\nProjectionType (string) --The set of attributes that are projected into the index:\n\nKEYS_ONLY - Only the index and primary keys are projected into the index.\nINCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .\nALL - All of the table attributes are projected into the index.\n\n\nNonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.\nFor local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.\n\n(string) --\n\n\n\n\nProvisionedThroughput (dict) --Represents the provisioned throughput settings for the specified global secondary index.\nFor current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .\n\nReadCapacityUnits (integer) -- [REQUIRED]The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\nWriteCapacityUnits (integer) -- [REQUIRED]The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\n\n\n\n\n\n

    :type BillingMode: string
    :param BillingMode: Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.\n\nPROVISIONED - We recommend using PROVISIONED for predictable workloads. PROVISIONED sets the billing mode to Provisioned Mode .\nPAY_PER_REQUEST - We recommend using PAY_PER_REQUEST for unpredictable workloads. PAY_PER_REQUEST sets the billing mode to On-Demand Mode .\n\n

    :type ProvisionedThroughput: dict
    :param ProvisionedThroughput: Represents the provisioned throughput settings for a specified table or index. The settings can be modified using the UpdateTable operation.\nIf you set BillingMode as PROVISIONED , you must specify this property. If you set BillingMode as PAY_PER_REQUEST , you cannot specify this property.\nFor current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .\n\nReadCapacityUnits (integer) -- [REQUIRED]The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\nWriteCapacityUnits (integer) -- [REQUIRED]The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\n\n

    :type StreamSpecification: dict
    :param StreamSpecification: The settings for DynamoDB Streams on the table. These settings consist of:\n\nStreamEnabled - Indicates whether DynamoDB Streams is to be enabled (true) or disabled (false).\nStreamViewType - When an item in the table is modified, StreamViewType determines what information is written to the table\'s stream. Valid values for StreamViewType are:\nKEYS_ONLY - Only the key attributes of the modified item are written to the stream.\nNEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.\nOLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.\nNEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream.\n\n\n\n\nStreamEnabled (boolean) -- [REQUIRED]Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.\n\nStreamViewType (string) --When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are:\n\nKEYS_ONLY - Only the key attributes of the modified item are written to the stream.\nNEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.\nOLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.\nNEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream.\n\n\n\n

    :type SSESpecification: dict
    :param SSESpecification: Represents the settings used to enable server-side encryption.\n\nEnabled (boolean) --Indicates whether server-side encryption is done using an AWS managed CMK or an AWS owned CMK. If enabled (true), server-side encryption type is set to KMS and an AWS managed CMK is used (AWS KMS charges apply). If disabled (false) or not specified, server-side encryption is set to AWS owned CMK.\n\nSSEType (string) --Server-side encryption type. The only supported value is:\n\nKMS - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).\n\n\nKMSMasterKeyId (string) --The AWS KMS customer master key (CMK) that should be used for the AWS KMS encryption. To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB customer master key alias/aws/dynamodb.\n\n\n

    :type Tags: list
    :param Tags: A list of key-value pairs to label the table. For more information, see Tagging for DynamoDB .\n\n(dict) --Describes a tag. A tag is a key-value pair. You can add up to 50 tags to a single DynamoDB table.\nAWS-assigned tag names and values are automatically assigned the aws: prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix user: in the Cost Allocation Report. You cannot backdate the application of a tag.\nFor an overview on tagging DynamoDB resources, see Tagging for DynamoDB in the Amazon DynamoDB Developer Guide .\n\nKey (string) -- [REQUIRED]The key of the tag. Tag keys are case sensitive. Each DynamoDB table can only have up to one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.\n\nValue (string) -- [REQUIRED]The value of the tag. Tag values are case-sensitive and can be null.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TableDescription': {
        'AttributeDefinitions': [
            {
                'AttributeName': 'string',
                'AttributeType': 'S'|'N'|'B'
            },
        ],
        'TableName': 'string',
        'KeySchema': [
            {
                'AttributeName': 'string',
                'KeyType': 'HASH'|'RANGE'
            },
        ],
        'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
        'CreationDateTime': datetime(2015, 1, 1),
        'ProvisionedThroughput': {
            'LastIncreaseDateTime': datetime(2015, 1, 1),
            'LastDecreaseDateTime': datetime(2015, 1, 1),
            'NumberOfDecreasesToday': 123,
            'ReadCapacityUnits': 123,
            'WriteCapacityUnits': 123
        },
        'TableSizeBytes': 123,
        'ItemCount': 123,
        'TableArn': 'string',
        'TableId': 'string',
        'BillingModeSummary': {
            'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
            'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
        },
        'LocalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexArn': 'string'
            },
        ],
        'GlobalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                'Backfilling': True|False,
                'ProvisionedThroughput': {
                    'LastIncreaseDateTime': datetime(2015, 1, 1),
                    'LastDecreaseDateTime': datetime(2015, 1, 1),
                    'NumberOfDecreasesToday': 123,
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexArn': 'string'
            },
        ],
        'StreamSpecification': {
            'StreamEnabled': True|False,
            'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
        },
        'LatestStreamLabel': 'string',
        'LatestStreamArn': 'string',
        'GlobalTableVersion': 'string',
        'Replicas': [
            {
                'RegionName': 'string',
                'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                'ReplicaStatusDescription': 'string',
                'ReplicaStatusPercentProgress': 'string',
                'KMSMasterKeyId': 'string',
                'ProvisionedThroughputOverride': {
                    'ReadCapacityUnits': 123
                },
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'ProvisionedThroughputOverride': {
                            'ReadCapacityUnits': 123
                        }
                    },
                ]
            },
        ],
        'RestoreSummary': {
            'SourceBackupArn': 'string',
            'SourceTableArn': 'string',
            'RestoreDateTime': datetime(2015, 1, 1),
            'RestoreInProgress': True|False
        },
        'SSEDescription': {
            'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
            'SSEType': 'AES256'|'KMS',
            'KMSMasterKeyArn': 'string',
            'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
        },
        'ArchivalSummary': {
            'ArchivalDateTime': datetime(2015, 1, 1),
            'ArchivalReason': 'string',
            'ArchivalBackupArn': 'string'
        }
    }
}


Response Structure

(dict) --
Represents the output of a CreateTable operation.

TableDescription (dict) --
Represents the properties of the table.

AttributeDefinitions (list) --
An array of AttributeDefinition objects. Each of these objects describes one attribute in the table and index key schema.
Each AttributeDefinition object in this array is composed of:

AttributeName - The name of the attribute.
AttributeType - The data type for the attribute.


(dict) --
Represents an attribute for describing the key schema for the table and indexes.

AttributeName (string) --
A name for the attribute.

AttributeType (string) --
The data type for the attribute, where:

S - the attribute is of type String
N - the attribute is of type Number
B - the attribute is of type Binary






TableName (string) --
The name of the table.

KeySchema (list) --
The primary key structure for the table. Each KeySchemaElement consists of:

AttributeName - The name of the attribute.
KeyType - The role of the attribute:
HASH - partition key
RANGE - sort key




Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

For more information about primary keys, see Primary Key in the Amazon DynamoDB Developer Guide .

(dict) --
Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --
The name of a key attribute.

KeyType (string) --
The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






TableStatus (string) --
The current state of the table:

CREATING - The table is being created.
UPDATING - The table is being updated.
DELETING - The table is being deleted.
ACTIVE - The table is ready for use.
INACCESSIBLE_ENCRYPTION_CREDENTIALS - The AWS KMS key used to encrypt the table in inaccessible. Table operations may fail due to failure to use the AWS KMS key. DynamoDB will initiate the table archival process when a table\'s AWS KMS key remains inaccessible for more than seven days.
ARCHIVING - The table is being archived. Operations are not allowed until archival is complete.
ARCHIVED - The table has been archived. See the ArchivalReason for more information.


CreationDateTime (datetime) --
The date and time when the table was created, in UNIX epoch time format.

ProvisionedThroughput (dict) --
The provisioned throughput settings for the table, consisting of read and write capacity units, along with data about increases and decreases.

LastIncreaseDateTime (datetime) --
The date and time of the last provisioned throughput increase for this table.

LastDecreaseDateTime (datetime) --
The date and time of the last provisioned throughput decrease for this table.

NumberOfDecreasesToday (integer) --
The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see Limits in the Amazon DynamoDB Developer Guide .

ReadCapacityUnits (integer) --
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 ReadCapacityUnits per second provides 100 eventually consistent ReadCapacityUnits per second.

WriteCapacityUnits (integer) --
The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException .



TableSizeBytes (integer) --
The total size of the specified table, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --
The number of items in the specified table. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

TableArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the table.

TableId (string) --
Unique identifier for the table for which the backup was created.

BillingModeSummary (dict) --
Contains the details for the read/write capacity mode.

BillingMode (string) --
Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.

PROVISIONED - Sets the read/write capacity mode to PROVISIONED . We recommend using PROVISIONED for predictable workloads.
PAY_PER_REQUEST - Sets the read/write capacity mode to PAY_PER_REQUEST . We recommend using PAY_PER_REQUEST for unpredictable workloads.


LastUpdateToPayPerRequestDateTime (datetime) --
Represents the time when PAY_PER_REQUEST was last set as the read/write capacity mode.



LocalSecondaryIndexes (list) --
Represents one or more local secondary indexes on the table. Each index is scoped to a given partition key value. Tables with one or more local secondary indexes are subject to an item collection size limit, where the amount of data within a given item collection cannot exceed 10 GB. Each element is composed of:

IndexName - The name of the local secondary index.
KeySchema - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
Projection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
ProjectionType - One of the following:
KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes , summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.


IndexSizeBytes - Represents the total size of the index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
ItemCount - Represents the number of items in the index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

If the table is in the DELETING state, no information about indexes will be returned.

(dict) --
Represents the properties of a local secondary index.

IndexName (string) --
Represents the name of the local secondary index.

KeySchema (list) --
The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --
Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --
The name of a key attribute.

KeyType (string) --
The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --
Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --
The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --
Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --




IndexSizeBytes (integer) --
The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --
The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

IndexArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the index.





GlobalSecondaryIndexes (list) --
The global secondary indexes, if any, on the table. Each index is scoped to a given partition key value. Each element is composed of:

Backfilling - If true, then the index is currently in the backfilling phase. Backfilling occurs only when a new global secondary index is added to the table. It is the process by which DynamoDB populates the new index with data from the table. (This attribute does not appear for indexes that were created during a CreateTable operation.)  You can delete an index that is being created during the Backfilling phase when IndexStatus is set to CREATING and Backfilling is true. You can\'t delete the index that is being created when IndexStatus is set to CREATING and Backfilling is false. (This attribute does not appear for indexes that were created during a CreateTable operation.)
IndexName - The name of the global secondary index.
IndexSizeBytes - The total size of the global secondary index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
IndexStatus - The current status of the global secondary index:
CREATING - The index is being created.
UPDATING - The index is being updated.
DELETING - The index is being deleted.
ACTIVE - The index is ready for use.


ItemCount - The number of items in the global secondary index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
KeySchema - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
Projection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
ProjectionType - One of the following:
KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes , summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.


ProvisionedThroughput - The provisioned throughput settings for the global secondary index, consisting of read and write capacity units, along with data about increases and decreases.

If the table is in the DELETING state, no information about indexes will be returned.

(dict) --
Represents the properties of a global secondary index.

IndexName (string) --
The name of the global secondary index.

KeySchema (list) --
The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --
Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --
The name of a key attribute.

KeyType (string) --
The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --
Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --
The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --
Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --




IndexStatus (string) --
The current state of the global secondary index:

CREATING - The index is being created.
UPDATING - The index is being updated.
DELETING - The index is being deleted.
ACTIVE - The index is ready for use.


Backfilling (boolean) --
Indicates whether the index is currently backfilling. Backfilling is the process of reading items from the table and determining whether they can be added to the index. (Not all items will qualify: For example, a partition key cannot have any duplicate values.) If an item can be added to the index, DynamoDB will do so. After all items have been processed, the backfilling operation is complete and Backfilling is false.
You can delete an index that is being created during the Backfilling phase when IndexStatus is set to CREATING and Backfilling is true. You can\'t delete the index that is being created when IndexStatus is set to CREATING and Backfilling is false.

Note
For indexes that were created during a CreateTable operation, the Backfilling attribute does not appear in the DescribeTable output.


ProvisionedThroughput (dict) --
Represents the provisioned throughput settings for the specified global secondary index.
For current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .

LastIncreaseDateTime (datetime) --
The date and time of the last provisioned throughput increase for this table.

LastDecreaseDateTime (datetime) --
The date and time of the last provisioned throughput decrease for this table.

NumberOfDecreasesToday (integer) --
The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see Limits in the Amazon DynamoDB Developer Guide .

ReadCapacityUnits (integer) --
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 ReadCapacityUnits per second provides 100 eventually consistent ReadCapacityUnits per second.

WriteCapacityUnits (integer) --
The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException .



IndexSizeBytes (integer) --
The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --
The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

IndexArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the index.





StreamSpecification (dict) --
The current DynamoDB Streams configuration for the table.

StreamEnabled (boolean) --
Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.

StreamViewType (string) --
When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are:

KEYS_ONLY - Only the key attributes of the modified item are written to the stream.
NEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.
OLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.
NEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream.




LatestStreamLabel (string) --
A timestamp, in ISO 8601 format, for this stream.
Note that LatestStreamLabel is not a unique identifier for the stream, because it is possible that a stream from another table might have the same timestamp. However, the combination of the following three elements is guaranteed to be unique:

AWS customer ID
Table name
StreamLabel


LatestStreamArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the latest stream for this table.

GlobalTableVersion (string) --
Represents the version of global tables in use, if the table is replicated across AWS Regions.

Replicas (list) --
Represents replicas of the table.

(dict) --
Contains the details of the replica.

RegionName (string) --
The name of the Region.

ReplicaStatus (string) --
The current state of the replica:

CREATING - The replica is being created.
UPDATING - The replica is being updated.
DELETING - The replica is being deleted.
ACTIVE - The replica is ready for use.


ReplicaStatusDescription (string) --
Detailed information about the replica status.

ReplicaStatusPercentProgress (string) --
Specifies the progress of a Create, Update, or Delete action on the replica as a percentage.

KMSMasterKeyId (string) --
The AWS KMS customer master key (CMK) of the replica that will be used for AWS KMS encryption.

ProvisionedThroughputOverride (dict) --
Replica-specific provisioned throughput. If not described, uses the source table\'s provisioned throughput settings.

ReadCapacityUnits (integer) --
Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.



GlobalSecondaryIndexes (list) --
Replica-specific global secondary index settings.

(dict) --
Represents the properties of a replica global secondary index.

IndexName (string) --
The name of the global secondary index.

ProvisionedThroughputOverride (dict) --
If not described, uses the source table GSI\'s read capacity settings.

ReadCapacityUnits (integer) --
Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.











RestoreSummary (dict) --
Contains details for the restore.

SourceBackupArn (string) --
The Amazon Resource Name (ARN) of the backup from which the table was restored.

SourceTableArn (string) --
The ARN of the source table of the backup that is being restored.

RestoreDateTime (datetime) --
Point in time or source backup time.

RestoreInProgress (boolean) --
Indicates if a restore is in progress or not.



SSEDescription (dict) --
The description of the server-side encryption status on the specified table.

Status (string) --
Represents the current state of server-side encryption. The only supported values are:

ENABLED - Server-side encryption is enabled.
UPDATING - Server-side encryption is being updated.


SSEType (string) --
Server-side encryption type. The only supported value is:

KMS - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).


KMSMasterKeyArn (string) --
The AWS KMS customer master key (CMK) ARN used for the AWS KMS encryption.

InaccessibleEncryptionDateTime (datetime) --
Indicates the time, in UNIX epoch date format, when DynamoDB detected that the table\'s AWS KMS key was inaccessible. This attribute will automatically be cleared when DynamoDB detects that the table\'s AWS KMS key is accessible again. DynamoDB will initiate the table archival process when table\'s AWS KMS key remains inaccessible for more than seven days from this date.



ArchivalSummary (dict) --
Contains information about the table archive.

ArchivalDateTime (datetime) --
The date and time when table archival was initiated by DynamoDB, in UNIX epoch time format.

ArchivalReason (string) --
The reason DynamoDB archived the table. Currently, the only possible value is:

INACCESSIBLE_ENCRYPTION_CREDENTIALS - The table was archived due to the table\'s AWS KMS key being inaccessible for more than seven days. An On-Demand backup was created at the archival time.


ArchivalBackupArn (string) --
The Amazon Resource Name (ARN) of the backup the table was archived to, when applicable in the archival reason. If you wish to restore this backup to the same table name, you will need to delete the original table.











Exceptions

DynamoDB.Client.exceptions.ResourceInUseException
DynamoDB.Client.exceptions.LimitExceededException
DynamoDB.Client.exceptions.InternalServerError

Examples
This example creates a table named Music.
response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Artist',
            'AttributeType': 'S',
        },
        {
            'AttributeName': 'SongTitle',
            'AttributeType': 'S',
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'Artist',
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'SongTitle',
            'KeyType': 'RANGE',
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5,
    },
    TableName='Music',
)

print(response)


Expected Output:
{
    'TableDescription': {
        'AttributeDefinitions': [
            {
                'AttributeName': 'Artist',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'SongTitle',
                'AttributeType': 'S',
            },
        ],
        'CreationDateTime': datetime(2015, 1, 21, 19, 2, 32, 2, 21, 0),
        'ItemCount': 0,
        'KeySchema': [
            {
                'AttributeName': 'Artist',
                'KeyType': 'HASH',
            },
            {
                'AttributeName': 'SongTitle',
                'KeyType': 'RANGE',
            },
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        },
        'TableName': 'Music',
        'TableSizeBytes': 0,
        'TableStatus': 'CREATING',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TableDescription': {
            'AttributeDefinitions': [
                {
                    'AttributeName': 'string',
                    'AttributeType': 'S'|'N'|'B'
                },
            ],
            'TableName': 'string',
            'KeySchema': [
                {
                    'AttributeName': 'string',
                    'KeyType': 'HASH'|'RANGE'
                },
            ],
            'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
            'CreationDateTime': datetime(2015, 1, 1),
            'ProvisionedThroughput': {
                'LastIncreaseDateTime': datetime(2015, 1, 1),
                'LastDecreaseDateTime': datetime(2015, 1, 1),
                'NumberOfDecreasesToday': 123,
                'ReadCapacityUnits': 123,
                'WriteCapacityUnits': 123
            },
            'TableSizeBytes': 123,
            'ItemCount': 123,
            'TableArn': 'string',
            'TableId': 'string',
            'BillingModeSummary': {
                'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
                'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
            },
            'LocalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'IndexSizeBytes': 123,
                    'ItemCount': 123,
                    'IndexArn': 'string'
                },
            ],
            'GlobalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                    'Backfilling': True|False,
                    'ProvisionedThroughput': {
                        'LastIncreaseDateTime': datetime(2015, 1, 1),
                        'LastDecreaseDateTime': datetime(2015, 1, 1),
                        'NumberOfDecreasesToday': 123,
                        'ReadCapacityUnits': 123,
                        'WriteCapacityUnits': 123
                    },
                    'IndexSizeBytes': 123,
                    'ItemCount': 123,
                    'IndexArn': 'string'
                },
            ],
            'StreamSpecification': {
                'StreamEnabled': True|False,
                'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
            },
            'LatestStreamLabel': 'string',
            'LatestStreamArn': 'string',
            'GlobalTableVersion': 'string',
            'Replicas': [
                {
                    'RegionName': 'string',
                    'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                    'ReplicaStatusDescription': 'string',
                    'ReplicaStatusPercentProgress': 'string',
                    'KMSMasterKeyId': 'string',
                    'ProvisionedThroughputOverride': {
                        'ReadCapacityUnits': 123
                    },
                    'GlobalSecondaryIndexes': [
                        {
                            'IndexName': 'string',
                            'ProvisionedThroughputOverride': {
                                'ReadCapacityUnits': 123
                            }
                        },
                    ]
                },
            ],
            'RestoreSummary': {
                'SourceBackupArn': 'string',
                'SourceTableArn': 'string',
                'RestoreDateTime': datetime(2015, 1, 1),
                'RestoreInProgress': True|False
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
                'SSEType': 'AES256'|'KMS',
                'KMSMasterKeyArn': 'string',
                'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
            },
            'ArchivalSummary': {
                'ArchivalDateTime': datetime(2015, 1, 1),
                'ArchivalReason': 'string',
                'ArchivalBackupArn': 'string'
            }
        }
    }
    
    
    :returns: 
    AttributeName - The name of the attribute.
    AttributeType - The data type for the attribute.
    
    """
    pass

def delete_backup(BackupArn=None):
    """
    Deletes an existing backup of a table.
    You can call DeleteBackup at a maximum rate of 10 times per second.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_backup(
        BackupArn='string'
    )
    
    
    :type BackupArn: string
    :param BackupArn: [REQUIRED]\nThe ARN associated with the backup.\n

    :rtype: dict
ReturnsResponse Syntax{
    'BackupDescription': {
        'BackupDetails': {
            'BackupArn': 'string',
            'BackupName': 'string',
            'BackupSizeBytes': 123,
            'BackupStatus': 'CREATING'|'DELETED'|'AVAILABLE',
            'BackupType': 'USER'|'SYSTEM'|'AWS_BACKUP',
            'BackupCreationDateTime': datetime(2015, 1, 1),
            'BackupExpiryDateTime': datetime(2015, 1, 1)
        },
        'SourceTableDetails': {
            'TableName': 'string',
            'TableId': 'string',
            'TableArn': 'string',
            'TableSizeBytes': 123,
            'KeySchema': [
                {
                    'AttributeName': 'string',
                    'KeyType': 'HASH'|'RANGE'
                },
            ],
            'TableCreationDateTime': datetime(2015, 1, 1),
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 123,
                'WriteCapacityUnits': 123
            },
            'ItemCount': 123,
            'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST'
        },
        'SourceTableFeatureDetails': {
            'LocalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    }
                },
            ],
            'GlobalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 123,
                        'WriteCapacityUnits': 123
                    }
                },
            ],
            'StreamDescription': {
                'StreamEnabled': True|False,
                'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
            },
            'TimeToLiveDescription': {
                'TimeToLiveStatus': 'ENABLING'|'DISABLING'|'ENABLED'|'DISABLED',
                'AttributeName': 'string'
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
                'SSEType': 'AES256'|'KMS',
                'KMSMasterKeyArn': 'string',
                'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
            }
        }
    }
}


Response Structure

(dict) --
BackupDescription (dict) --Contains the description of the backup created for the table.

BackupDetails (dict) --Contains the details of the backup created for the table.

BackupArn (string) --ARN associated with the backup.

BackupName (string) --Name of the requested backup.

BackupSizeBytes (integer) --Size of the backup in bytes.

BackupStatus (string) --Backup can be in one of the following states: CREATING, ACTIVE, DELETED.

BackupType (string) --BackupType:

USER - You create and manage these using the on-demand backup feature.
SYSTEM - If you delete a table with point-in-time recovery enabled, a SYSTEM backup is automatically created and is retained for 35 days (at no additional cost). System backups allow you to restore the deleted table to the state it was in just before the point of deletion.
AWS_BACKUP - On-demand backup created by you from AWS Backup service.


BackupCreationDateTime (datetime) --Time at which the backup was created. This is the request time of the backup.

BackupExpiryDateTime (datetime) --Time at which the automatic on-demand backup created by DynamoDB will expire. This SYSTEM on-demand backup expires automatically 35 days after its creation.



SourceTableDetails (dict) --Contains the details of the table when the backup was created.

TableName (string) --The name of the table for which the backup was created.

TableId (string) --Unique identifier for the table for which the backup was created.

TableArn (string) --ARN of the table for which backup was created.

TableSizeBytes (integer) --Size of the table in bytes. Note that this is an approximate value.

KeySchema (list) --Schema of the table.

(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --The name of a key attribute.

KeyType (string) --The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






TableCreationDateTime (datetime) --Time when the source table was created.

ProvisionedThroughput (dict) --Read IOPs and Write IOPS on the table when the backup was created.

ReadCapacityUnits (integer) --The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.

WriteCapacityUnits (integer) --The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.



ItemCount (integer) --Number of items in the table. Note that this is an approximate value.

BillingMode (string) --Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.

PROVISIONED - Sets the read/write capacity mode to PROVISIONED . We recommend using PROVISIONED for predictable workloads.
PAY_PER_REQUEST - Sets the read/write capacity mode to PAY_PER_REQUEST . We recommend using PAY_PER_REQUEST for unpredictable workloads.




SourceTableFeatureDetails (dict) --Contains the details of the features enabled on the table when the backup was created. For example, LSIs, GSIs, streams, TTL.

LocalSecondaryIndexes (list) --Represents the LSI properties for the table when the backup was created. It includes the IndexName, KeySchema and Projection for the LSIs on the table at the time of backup.

(dict) --Represents the properties of a local secondary index for the table when the backup was created.

IndexName (string) --Represents the name of the local secondary index.

KeySchema (list) --The complete key schema for a local secondary index, which consists of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --The name of a key attribute.

KeyType (string) --The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --








GlobalSecondaryIndexes (list) --Represents the GSI properties for the table when the backup was created. It includes the IndexName, KeySchema, Projection, and ProvisionedThroughput for the GSIs on the table at the time of backup.

(dict) --Represents the properties of a global secondary index for the table when the backup was created.

IndexName (string) --The name of the global secondary index.

KeySchema (list) --The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --The name of a key attribute.

KeyType (string) --The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --




ProvisionedThroughput (dict) --Represents the provisioned throughput settings for the specified global secondary index.

ReadCapacityUnits (integer) --The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.

WriteCapacityUnits (integer) --The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.







StreamDescription (dict) --Stream settings on the table when the backup was created.

StreamEnabled (boolean) --Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.

StreamViewType (string) --When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are:

KEYS_ONLY - Only the key attributes of the modified item are written to the stream.
NEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.
OLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.
NEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream.




TimeToLiveDescription (dict) --Time to Live settings on the table when the backup was created.

TimeToLiveStatus (string) --The TTL status for the table.

AttributeName (string) --The name of the TTL attribute for items in the table.



SSEDescription (dict) --The description of the server-side encryption status on the table when the backup was created.

Status (string) --Represents the current state of server-side encryption. The only supported values are:

ENABLED - Server-side encryption is enabled.
UPDATING - Server-side encryption is being updated.


SSEType (string) --Server-side encryption type. The only supported value is:

KMS - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).


KMSMasterKeyArn (string) --The AWS KMS customer master key (CMK) ARN used for the AWS KMS encryption.

InaccessibleEncryptionDateTime (datetime) --Indicates the time, in UNIX epoch date format, when DynamoDB detected that the table\'s AWS KMS key was inaccessible. This attribute will automatically be cleared when DynamoDB detects that the table\'s AWS KMS key is accessible again. DynamoDB will initiate the table archival process when table\'s AWS KMS key remains inaccessible for more than seven days from this date.












Exceptions

DynamoDB.Client.exceptions.BackupNotFoundException
DynamoDB.Client.exceptions.BackupInUseException
DynamoDB.Client.exceptions.LimitExceededException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'BackupDescription': {
            'BackupDetails': {
                'BackupArn': 'string',
                'BackupName': 'string',
                'BackupSizeBytes': 123,
                'BackupStatus': 'CREATING'|'DELETED'|'AVAILABLE',
                'BackupType': 'USER'|'SYSTEM'|'AWS_BACKUP',
                'BackupCreationDateTime': datetime(2015, 1, 1),
                'BackupExpiryDateTime': datetime(2015, 1, 1)
            },
            'SourceTableDetails': {
                'TableName': 'string',
                'TableId': 'string',
                'TableArn': 'string',
                'TableSizeBytes': 123,
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'TableCreationDateTime': datetime(2015, 1, 1),
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                },
                'ItemCount': 123,
                'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST'
            },
            'SourceTableFeatureDetails': {
                'LocalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'KeySchema': [
                            {
                                'AttributeName': 'string',
                                'KeyType': 'HASH'|'RANGE'
                            },
                        ],
                        'Projection': {
                            'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                            'NonKeyAttributes': [
                                'string',
                            ]
                        }
                    },
                ],
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'KeySchema': [
                            {
                                'AttributeName': 'string',
                                'KeyType': 'HASH'|'RANGE'
                            },
                        ],
                        'Projection': {
                            'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                            'NonKeyAttributes': [
                                'string',
                            ]
                        },
                        'ProvisionedThroughput': {
                            'ReadCapacityUnits': 123,
                            'WriteCapacityUnits': 123
                        }
                    },
                ],
                'StreamDescription': {
                    'StreamEnabled': True|False,
                    'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
                },
                'TimeToLiveDescription': {
                    'TimeToLiveStatus': 'ENABLING'|'DISABLING'|'ENABLED'|'DISABLED',
                    'AttributeName': 'string'
                },
                'SSEDescription': {
                    'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
                    'SSEType': 'AES256'|'KMS',
                    'KMSMasterKeyArn': 'string',
                    'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
                }
            }
        }
    }
    
    
    :returns: 
    HASH - partition key
    RANGE - sort key
    
    """
    pass

def delete_item(TableName=None, Key=None, Expected=None, ConditionalOperator=None, ReturnValues=None, ReturnConsumedCapacity=None, ReturnItemCollectionMetrics=None, ConditionExpression=None, ExpressionAttributeNames=None, ExpressionAttributeValues=None):
    """
    Deletes a single item in a table by primary key. You can perform a conditional delete operation that deletes the item if it exists, or if it has an expected attribute value.
    In addition to deleting an item, you can also return the item\'s attribute values in the same operation, using the ReturnValues parameter.
    Unless you specify conditions, the DeleteItem is an idempotent operation; running it multiple times on the same item or attribute does not result in an error response.
    Conditional deletes are useful for deleting items only if specific conditions are met. If those conditions are met, DynamoDB performs the delete. Otherwise, the item is not deleted.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes an item from the Music table.
    Expected Output:
    
    :example: response = client.delete_item(
        TableName='string',
        Key={
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        Expected={
            'string': {
                'Value': {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                },
                'Exists': True|False,
                'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH',
                'AttributeValueList': [
                    {
                        'S': 'string',
                        'N': 'string',
                        'B': b'bytes',
                        'SS': [
                            'string',
                        ],
                        'NS': [
                            'string',
                        ],
                        'BS': [
                            b'bytes',
                        ],
                        'M': {
                            'string': {'... recursive ...'}
                        },
                        'L': [
                            {'... recursive ...'},
                        ],
                        'NULL': True|False,
                        'BOOL': True|False
                    },
                ]
            }
        },
        ConditionalOperator='AND'|'OR',
        ReturnValues='NONE'|'ALL_OLD'|'UPDATED_OLD'|'ALL_NEW'|'UPDATED_NEW',
        ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
        ReturnItemCollectionMetrics='SIZE'|'NONE',
        ConditionExpression='string',
        ExpressionAttributeNames={
            'string': 'string'
        },
        ExpressionAttributeValues={
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        }
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table from which to delete the item.\n

    :type Key: dict
    :param Key: [REQUIRED]\nA map of attribute names to AttributeValue objects, representing the primary key of the item to delete.\nFor the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n

    :type Expected: dict
    :param Expected: This is a legacy parameter. Use ConditionExpression instead. For more information, see Expected in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(dict) --Represents a condition to be compared with an attribute value. This condition can be used with DeleteItem , PutItem , or UpdateItem operations; if the comparison evaluates to true, the operation succeeds; if not, the operation fails. You can use ExpectedAttributeValue in one of two different ways:\n\nUse AttributeValueList to specify one or more values to compare against an attribute. Use ComparisonOperator to specify how you want to perform the comparison. If the comparison evaluates to true, then the conditional operation succeeds.\nUse Value to specify a value that DynamoDB will compare against an attribute. If the values match, then ExpectedAttributeValue evaluates to true and the conditional operation succeeds. Optionally, you can also set Exists to false, indicating that you do not expect to find the attribute value in the table. In this case, the conditional operation succeeds only if the comparison evaluates to false.\n\n\nValue and Exists are incompatible with AttributeValueList and ComparisonOperator . Note that if you use both sets of parameters at once, DynamoDB will return a ValidationException exception.\n\nValue (dict) --Represents the data for the expected attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\nExists (boolean) --Causes DynamoDB to evaluate the value before attempting a conditional operation:\n\nIf Exists is true , DynamoDB will check to see if that attribute value already exists in the table. If it is found, then the operation succeeds. If it is not found, the operation fails with a ConditionCheckFailedException .\nIf Exists is false , DynamoDB assumes that the attribute value does not exist in the table. If in fact the value does not exist, then the assumption is valid and the operation succeeds. If the value is found, despite the assumption that it does not exist, the operation fails with a ConditionCheckFailedException .\n\nThe default setting for Exists is true . If you supply a Value all by itself, DynamoDB assumes the attribute exists: You don\'t have to set Exists to true , because it is implied.\nDynamoDB returns a ValidationException if:\n\nExists is true but there is no Value to check. (You expect a value to exist, but don\'t specify what that value is.)\nExists is false but you also provide a Value . (You cannot expect an attribute to have a value, while also expecting it not to exist.)\n\n\nComparisonOperator (string) --A comparator for evaluating attributes in the AttributeValueList . For example, equals, greater than, less than, etc.\nThe following comparison operators are available:\n\nEQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS | NOT_CONTAINS | BEGINS_WITH | IN | BETWEEN\nThe following are descriptions of each comparison operator.\n\nEQ : Equal. EQ is supported for all data types, including lists and maps. AttributeValueList can contain only one AttributeValue element of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not equal {'NS':['6', '2', '1']} .\nNE : Not equal. NE is supported for all data types, including lists and maps. AttributeValueList can contain only one AttributeValue of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an AttributeValue of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not equal {'NS':['6', '2', '1']} .\nLE : Less than or equal.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nLT : Less than.  AttributeValueList can contain only one AttributeValue of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nGE : Greater than or equal.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nGT : Greater than.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nNOT_NULL : The attribute exists. NOT_NULL is supported for all data types, including lists and maps.\n\n\nNote\nThis operator tests for the existence of an attribute, not its data type. If the data type of attribute 'a ' is null, and you evaluate it using NOT_NULL , the result is a Boolean true . This result is because the attribute 'a ' exists; its data type is not relevant to the NOT_NULL comparison operator.\n\n\nNULL : The attribute does not exist. NULL is supported for all data types, including lists and maps.\n\n\nNote\nThis operator tests for the nonexistence of an attribute, not its data type. If the data type of attribute 'a ' is null, and you evaluate it using NULL , the result is a Boolean false . This is because the attribute 'a ' exists; its data type is not relevant to the NULL comparison operator.\n\n\nCONTAINS : Checks for a subsequence, or value in a set. AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is of type String, then the operator checks for a substring match. If the target attribute of the comparison is of type Binary, then the operator looks for a subsequence of the target that matches the input. If the target attribute of the comparison is a set ('SS ', 'NS ', or 'BS '), then the operator evaluates to true if it finds an exact match with any member of the set. CONTAINS is supported for lists: When evaluating 'a CONTAINS b ', 'a ' can be a list; however, 'b ' cannot be a set, a map, or a list.\nNOT_CONTAINS : Checks for absence of a subsequence, or absence of a value in a set. AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is a String, then the operator checks for the absence of a substring match. If the target attribute of the comparison is Binary, then the operator checks for the absence of a subsequence of the target that matches the input. If the target attribute of the comparison is a set ('SS ', 'NS ', or 'BS '), then the operator evaluates to true if it does not find an exact match with any member of the set. NOT_CONTAINS is supported for lists: When evaluating 'a NOT CONTAINS b ', 'a ' can be a list; however, 'b ' cannot be a set, a map, or a list.\nBEGINS_WITH : Checks for a prefix.  AttributeValueList can contain only one AttributeValue of type String or Binary (not a Number or a set type). The target attribute of the comparison must be of type String or Binary (not a Number or a set type).\nIN : Checks for matching elements in a list. AttributeValueList can contain one or more AttributeValue elements of type String, Number, or Binary. These attributes are compared against an existing attribute of an item. If any elements of the input are equal to the item attribute, the expression evaluates to true.\nBETWEEN : Greater than or equal to the first value, and less than or equal to the second value.  AttributeValueList must contain two AttributeValue elements of the same type, either String, Number, or Binary (not a set type). A target attribute matches if the target value is greater than, or equal to, the first element and less than, or equal to, the second element. If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not compare to {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']}\n\n\nAttributeValueList (list) --One or more values to evaluate against the supplied attribute. The number of values in the list depends on the ComparisonOperator being used.\nFor type Number, value comparisons are numeric.\nString value comparisons for greater than, equals, or less than are based on ASCII character code values. For example, a is greater than A , and a is greater than B . For a list of code values, see http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters .\nFor Binary, DynamoDB treats each byte of the binary data as unsigned when it compares binary values.\nFor information on specifying data types in JSON, see JSON Data Format in the Amazon DynamoDB Developer Guide .\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\n\n\n\n

    :type ConditionalOperator: string
    :param ConditionalOperator: This is a legacy parameter. Use ConditionExpression instead. For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide .

    :type ReturnValues: string
    :param ReturnValues: Use ReturnValues if you want to get the item attributes as they appeared before they were deleted. For DeleteItem , the valid values are:\n\nNONE - If ReturnValues is not specified, or if its value is NONE , then nothing is returned. (This setting is the default for ReturnValues .)\nALL_OLD - The content of the old item is returned.\n\n\nNote\nThe ReturnValues parameter is used by several DynamoDB operations; however, DeleteItem does not recognize any values other than NONE or ALL_OLD .\n\n

    :type ReturnConsumedCapacity: string
    :param ReturnConsumedCapacity: Determines the level of detail about provisioned throughput consumption that is returned in the response:\n\nINDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem , do not access any indexes at all. In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s).\nTOTAL - The response includes only the aggregate ConsumedCapacity for the operation.\nNONE - No ConsumedCapacity details are included in the response.\n\n

    :type ReturnItemCollectionMetrics: string
    :param ReturnItemCollectionMetrics: Determines whether item collection metrics are returned. If set to SIZE , the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.

    :type ConditionExpression: string
    :param ConditionExpression: A condition that must be satisfied in order for a conditional DeleteItem to succeed.\nAn expression can contain any of the following:\n\nFunctions: attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size  These function names are case-sensitive.\nComparison operators: = | <> | < | > | <= | >= | BETWEEN | IN\nLogical operators: AND | OR | NOT\n\nFor more information about condition expressions, see Condition Expressions in the Amazon DynamoDB Developer Guide .\n

    :type ExpressionAttributeNames: dict
    :param ExpressionAttributeNames: One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames :\n\nTo access an attribute whose name conflicts with a DynamoDB reserved word.\nTo create a placeholder for repeating occurrences of an attribute name in an expression.\nTo prevent special characters in an attribute name from being misinterpreted in an expression.\n\nUse the # character in an expression to dereference an attribute name. For example, consider the following attribute name:\n\nPercentile\n\nThe name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide ). To work around this, you could specify the following for ExpressionAttributeNames :\n\n{'#P':'Percentile'}\n\nYou could then use this substitution in an expression, as in this example:\n\n#P = :val\n\n\nNote\nTokens that begin with the : character are expression attribute values , which are placeholders for the actual value at runtime.\n\nFor more information on expression attribute names, see Specifying Item Attributes in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type ExpressionAttributeValues: dict
    :param ExpressionAttributeValues: One or more values that can be substituted in an expression.\nUse the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:\n\nAvailable | Backordered | Discontinued\nYou would first need to specify ExpressionAttributeValues as follows:\n\n{ ':avail':{'S':'Available'}, ':back':{'S':'Backordered'}, ':disc':{'S':'Discontinued'} }\nYou could then use these values in an expression, such as this:\n\nProductStatus IN (:avail, :back, :disc)\nFor more information on expression attribute values, see Condition Expressions in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Attributes': {
        'string': {
            'S': 'string',
            'N': 'string',
            'B': b'bytes',
            'SS': [
                'string',
            ],
            'NS': [
                'string',
            ],
            'BS': [
                b'bytes',
            ],
            'M': {
                'string': {'... recursive ...'}
            },
            'L': [
                {'... recursive ...'},
            ],
            'NULL': True|False,
            'BOOL': True|False
        }
    },
    'ConsumedCapacity': {
        'TableName': 'string',
        'CapacityUnits': 123.0,
        'ReadCapacityUnits': 123.0,
        'WriteCapacityUnits': 123.0,
        'Table': {
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'CapacityUnits': 123.0
        },
        'LocalSecondaryIndexes': {
            'string': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            }
        },
        'GlobalSecondaryIndexes': {
            'string': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            }
        }
    },
    'ItemCollectionMetrics': {
        'ItemCollectionKey': {
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        'SizeEstimateRangeGB': [
            123.0,
        ]
    }
}


Response Structure

(dict) --
Represents the output of a DeleteItem operation.

Attributes (dict) --
A map of attribute names to AttributeValue objects, representing the item as it appeared before the DeleteItem operation. This map appears in the response only if ReturnValues was specified as ALL_OLD in the request.

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true








ConsumedCapacity (dict) --
The capacity units consumed by the DeleteItem operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. ConsumedCapacity is only returned if the ReturnConsumedCapacity parameter was specified. For more information, see Provisioned Mode in the Amazon DynamoDB Developer Guide .

TableName (string) --
The name of the table that was affected by the operation.

CapacityUnits (float) --
The total number of capacity units consumed by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed by the operation.

WriteCapacityUnits (float) --
The total number of write capacity units consumed by the operation.

Table (dict) --
The amount of throughput consumed on the table affected by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.



LocalSecondaryIndexes (dict) --
The amount of throughput consumed on each local index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.







GlobalSecondaryIndexes (dict) --
The amount of throughput consumed on each global index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.









ItemCollectionMetrics (dict) --
Information about item collections, if any, that were affected by the DeleteItem operation. ItemCollectionMetrics is only returned if the ReturnItemCollectionMetrics parameter was specified. If the table does not have any local secondary indexes, this information is not returned in the response.
Each ItemCollectionMetrics element consists of:

ItemCollectionKey - The partition key value of the item collection. This is the same as the partition key value of the item itself.
SizeEstimateRangeGB - An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit. The estimate is subject to change over time; therefore, do not rely on the precision or accuracy of the estimate.


ItemCollectionKey (dict) --
The partition key value of the item collection. This value is the same as the partition key value of the item.

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true








SizeEstimateRangeGB (list) --
An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit.
The estimate is subject to change over time; therefore, do not rely on the precision or accuracy of the estimate.

(float) --










Exceptions

DynamoDB.Client.exceptions.ConditionalCheckFailedException
DynamoDB.Client.exceptions.ProvisionedThroughputExceededException
DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.ItemCollectionSizeLimitExceededException
DynamoDB.Client.exceptions.TransactionConflictException
DynamoDB.Client.exceptions.RequestLimitExceeded
DynamoDB.Client.exceptions.InternalServerError

Examples
This example deletes an item from the Music table.
response = client.delete_item(
    Key={
        'Artist': {
            'S': 'No One You Know',
        },
        'SongTitle': {
            'S': 'Scared of My Shadow',
        },
    },
    TableName='Music',
)

print(response)


Expected Output:
{
    'ConsumedCapacity': {
        'CapacityUnits': 1,
        'TableName': 'Music',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Attributes': {
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        'ConsumedCapacity': {
            'TableName': 'string',
            'CapacityUnits': 123.0,
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'Table': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            },
            'LocalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            },
            'GlobalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            }
        },
        'ItemCollectionMetrics': {
            'ItemCollectionKey': {
                'string': {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                }
            },
            'SizeEstimateRangeGB': [
                123.0,
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_table(TableName=None):
    """
    The DeleteTable operation deletes a table and all of its items. After a DeleteTable request, the specified table is in the DELETING state until DynamoDB completes the deletion. If the table is in the ACTIVE state, you can delete it. If a table is in CREATING or UPDATING states, then DynamoDB returns a ResourceInUseException . If the specified table does not exist, DynamoDB returns a ResourceNotFoundException . If table is already in the DELETING state, no error is returned.
    When you delete a table, any indexes on that table are also deleted.
    If you have DynamoDB Streams enabled on the table, then the corresponding stream on that table goes into the DISABLED state, and the stream is automatically deleted after 24 hours.
    Use the DescribeTable action to check the status of the table.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the Music table.
    Expected Output:
    
    :example: response = client.delete_table(
        TableName='string'
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TableDescription': {
        'AttributeDefinitions': [
            {
                'AttributeName': 'string',
                'AttributeType': 'S'|'N'|'B'
            },
        ],
        'TableName': 'string',
        'KeySchema': [
            {
                'AttributeName': 'string',
                'KeyType': 'HASH'|'RANGE'
            },
        ],
        'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
        'CreationDateTime': datetime(2015, 1, 1),
        'ProvisionedThroughput': {
            'LastIncreaseDateTime': datetime(2015, 1, 1),
            'LastDecreaseDateTime': datetime(2015, 1, 1),
            'NumberOfDecreasesToday': 123,
            'ReadCapacityUnits': 123,
            'WriteCapacityUnits': 123
        },
        'TableSizeBytes': 123,
        'ItemCount': 123,
        'TableArn': 'string',
        'TableId': 'string',
        'BillingModeSummary': {
            'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
            'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
        },
        'LocalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexArn': 'string'
            },
        ],
        'GlobalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                'Backfilling': True|False,
                'ProvisionedThroughput': {
                    'LastIncreaseDateTime': datetime(2015, 1, 1),
                    'LastDecreaseDateTime': datetime(2015, 1, 1),
                    'NumberOfDecreasesToday': 123,
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexArn': 'string'
            },
        ],
        'StreamSpecification': {
            'StreamEnabled': True|False,
            'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
        },
        'LatestStreamLabel': 'string',
        'LatestStreamArn': 'string',
        'GlobalTableVersion': 'string',
        'Replicas': [
            {
                'RegionName': 'string',
                'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                'ReplicaStatusDescription': 'string',
                'ReplicaStatusPercentProgress': 'string',
                'KMSMasterKeyId': 'string',
                'ProvisionedThroughputOverride': {
                    'ReadCapacityUnits': 123
                },
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'ProvisionedThroughputOverride': {
                            'ReadCapacityUnits': 123
                        }
                    },
                ]
            },
        ],
        'RestoreSummary': {
            'SourceBackupArn': 'string',
            'SourceTableArn': 'string',
            'RestoreDateTime': datetime(2015, 1, 1),
            'RestoreInProgress': True|False
        },
        'SSEDescription': {
            'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
            'SSEType': 'AES256'|'KMS',
            'KMSMasterKeyArn': 'string',
            'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
        },
        'ArchivalSummary': {
            'ArchivalDateTime': datetime(2015, 1, 1),
            'ArchivalReason': 'string',
            'ArchivalBackupArn': 'string'
        }
    }
}


Response Structure

(dict) --Represents the output of a DeleteTable operation.

TableDescription (dict) --Represents the properties of a table.

AttributeDefinitions (list) --An array of AttributeDefinition objects. Each of these objects describes one attribute in the table and index key schema.
Each AttributeDefinition object in this array is composed of:

AttributeName - The name of the attribute.
AttributeType - The data type for the attribute.


(dict) --Represents an attribute for describing the key schema for the table and indexes.

AttributeName (string) --A name for the attribute.

AttributeType (string) --The data type for the attribute, where:

S - the attribute is of type String
N - the attribute is of type Number
B - the attribute is of type Binary






TableName (string) --The name of the table.

KeySchema (list) --The primary key structure for the table. Each KeySchemaElement consists of:

AttributeName - The name of the attribute.
KeyType - The role of the attribute:
HASH - partition key
RANGE - sort key




Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

For more information about primary keys, see Primary Key in the Amazon DynamoDB Developer Guide .

(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --The name of a key attribute.

KeyType (string) --The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






TableStatus (string) --The current state of the table:

CREATING - The table is being created.
UPDATING - The table is being updated.
DELETING - The table is being deleted.
ACTIVE - The table is ready for use.
INACCESSIBLE_ENCRYPTION_CREDENTIALS - The AWS KMS key used to encrypt the table in inaccessible. Table operations may fail due to failure to use the AWS KMS key. DynamoDB will initiate the table archival process when a table\'s AWS KMS key remains inaccessible for more than seven days.
ARCHIVING - The table is being archived. Operations are not allowed until archival is complete.
ARCHIVED - The table has been archived. See the ArchivalReason for more information.


CreationDateTime (datetime) --The date and time when the table was created, in UNIX epoch time format.

ProvisionedThroughput (dict) --The provisioned throughput settings for the table, consisting of read and write capacity units, along with data about increases and decreases.

LastIncreaseDateTime (datetime) --The date and time of the last provisioned throughput increase for this table.

LastDecreaseDateTime (datetime) --The date and time of the last provisioned throughput decrease for this table.

NumberOfDecreasesToday (integer) --The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see Limits in the Amazon DynamoDB Developer Guide .

ReadCapacityUnits (integer) --The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 ReadCapacityUnits per second provides 100 eventually consistent ReadCapacityUnits per second.

WriteCapacityUnits (integer) --The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException .



TableSizeBytes (integer) --The total size of the specified table, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --The number of items in the specified table. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

TableArn (string) --The Amazon Resource Name (ARN) that uniquely identifies the table.

TableId (string) --Unique identifier for the table for which the backup was created.

BillingModeSummary (dict) --Contains the details for the read/write capacity mode.

BillingMode (string) --Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.

PROVISIONED - Sets the read/write capacity mode to PROVISIONED . We recommend using PROVISIONED for predictable workloads.
PAY_PER_REQUEST - Sets the read/write capacity mode to PAY_PER_REQUEST . We recommend using PAY_PER_REQUEST for unpredictable workloads.


LastUpdateToPayPerRequestDateTime (datetime) --Represents the time when PAY_PER_REQUEST was last set as the read/write capacity mode.



LocalSecondaryIndexes (list) --Represents one or more local secondary indexes on the table. Each index is scoped to a given partition key value. Tables with one or more local secondary indexes are subject to an item collection size limit, where the amount of data within a given item collection cannot exceed 10 GB. Each element is composed of:

IndexName - The name of the local secondary index.
KeySchema - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
Projection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
ProjectionType - One of the following:
KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes , summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.


IndexSizeBytes - Represents the total size of the index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
ItemCount - Represents the number of items in the index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

If the table is in the DELETING state, no information about indexes will be returned.

(dict) --Represents the properties of a local secondary index.

IndexName (string) --Represents the name of the local secondary index.

KeySchema (list) --The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --The name of a key attribute.

KeyType (string) --The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --




IndexSizeBytes (integer) --The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

IndexArn (string) --The Amazon Resource Name (ARN) that uniquely identifies the index.





GlobalSecondaryIndexes (list) --The global secondary indexes, if any, on the table. Each index is scoped to a given partition key value. Each element is composed of:

Backfilling - If true, then the index is currently in the backfilling phase. Backfilling occurs only when a new global secondary index is added to the table. It is the process by which DynamoDB populates the new index with data from the table. (This attribute does not appear for indexes that were created during a CreateTable operation.)  You can delete an index that is being created during the Backfilling phase when IndexStatus is set to CREATING and Backfilling is true. You can\'t delete the index that is being created when IndexStatus is set to CREATING and Backfilling is false. (This attribute does not appear for indexes that were created during a CreateTable operation.)
IndexName - The name of the global secondary index.
IndexSizeBytes - The total size of the global secondary index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
IndexStatus - The current status of the global secondary index:
CREATING - The index is being created.
UPDATING - The index is being updated.
DELETING - The index is being deleted.
ACTIVE - The index is ready for use.


ItemCount - The number of items in the global secondary index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
KeySchema - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
Projection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
ProjectionType - One of the following:
KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes , summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.


ProvisionedThroughput - The provisioned throughput settings for the global secondary index, consisting of read and write capacity units, along with data about increases and decreases.

If the table is in the DELETING state, no information about indexes will be returned.

(dict) --Represents the properties of a global secondary index.

IndexName (string) --The name of the global secondary index.

KeySchema (list) --The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --The name of a key attribute.

KeyType (string) --The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --




IndexStatus (string) --The current state of the global secondary index:

CREATING - The index is being created.
UPDATING - The index is being updated.
DELETING - The index is being deleted.
ACTIVE - The index is ready for use.


Backfilling (boolean) --Indicates whether the index is currently backfilling. Backfilling is the process of reading items from the table and determining whether they can be added to the index. (Not all items will qualify: For example, a partition key cannot have any duplicate values.) If an item can be added to the index, DynamoDB will do so. After all items have been processed, the backfilling operation is complete and Backfilling is false.
You can delete an index that is being created during the Backfilling phase when IndexStatus is set to CREATING and Backfilling is true. You can\'t delete the index that is being created when IndexStatus is set to CREATING and Backfilling is false.

Note
For indexes that were created during a CreateTable operation, the Backfilling attribute does not appear in the DescribeTable output.


ProvisionedThroughput (dict) --Represents the provisioned throughput settings for the specified global secondary index.
For current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .

LastIncreaseDateTime (datetime) --The date and time of the last provisioned throughput increase for this table.

LastDecreaseDateTime (datetime) --The date and time of the last provisioned throughput decrease for this table.

NumberOfDecreasesToday (integer) --The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see Limits in the Amazon DynamoDB Developer Guide .

ReadCapacityUnits (integer) --The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 ReadCapacityUnits per second provides 100 eventually consistent ReadCapacityUnits per second.

WriteCapacityUnits (integer) --The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException .



IndexSizeBytes (integer) --The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

IndexArn (string) --The Amazon Resource Name (ARN) that uniquely identifies the index.





StreamSpecification (dict) --The current DynamoDB Streams configuration for the table.

StreamEnabled (boolean) --Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.

StreamViewType (string) --When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are:

KEYS_ONLY - Only the key attributes of the modified item are written to the stream.
NEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.
OLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.
NEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream.




LatestStreamLabel (string) --A timestamp, in ISO 8601 format, for this stream.
Note that LatestStreamLabel is not a unique identifier for the stream, because it is possible that a stream from another table might have the same timestamp. However, the combination of the following three elements is guaranteed to be unique:

AWS customer ID
Table name
StreamLabel


LatestStreamArn (string) --The Amazon Resource Name (ARN) that uniquely identifies the latest stream for this table.

GlobalTableVersion (string) --Represents the version of global tables in use, if the table is replicated across AWS Regions.

Replicas (list) --Represents replicas of the table.

(dict) --Contains the details of the replica.

RegionName (string) --The name of the Region.

ReplicaStatus (string) --The current state of the replica:

CREATING - The replica is being created.
UPDATING - The replica is being updated.
DELETING - The replica is being deleted.
ACTIVE - The replica is ready for use.


ReplicaStatusDescription (string) --Detailed information about the replica status.

ReplicaStatusPercentProgress (string) --Specifies the progress of a Create, Update, or Delete action on the replica as a percentage.

KMSMasterKeyId (string) --The AWS KMS customer master key (CMK) of the replica that will be used for AWS KMS encryption.

ProvisionedThroughputOverride (dict) --Replica-specific provisioned throughput. If not described, uses the source table\'s provisioned throughput settings.

ReadCapacityUnits (integer) --Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.



GlobalSecondaryIndexes (list) --Replica-specific global secondary index settings.

(dict) --Represents the properties of a replica global secondary index.

IndexName (string) --The name of the global secondary index.

ProvisionedThroughputOverride (dict) --If not described, uses the source table GSI\'s read capacity settings.

ReadCapacityUnits (integer) --Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.











RestoreSummary (dict) --Contains details for the restore.

SourceBackupArn (string) --The Amazon Resource Name (ARN) of the backup from which the table was restored.

SourceTableArn (string) --The ARN of the source table of the backup that is being restored.

RestoreDateTime (datetime) --Point in time or source backup time.

RestoreInProgress (boolean) --Indicates if a restore is in progress or not.



SSEDescription (dict) --The description of the server-side encryption status on the specified table.

Status (string) --Represents the current state of server-side encryption. The only supported values are:

ENABLED - Server-side encryption is enabled.
UPDATING - Server-side encryption is being updated.


SSEType (string) --Server-side encryption type. The only supported value is:

KMS - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).


KMSMasterKeyArn (string) --The AWS KMS customer master key (CMK) ARN used for the AWS KMS encryption.

InaccessibleEncryptionDateTime (datetime) --Indicates the time, in UNIX epoch date format, when DynamoDB detected that the table\'s AWS KMS key was inaccessible. This attribute will automatically be cleared when DynamoDB detects that the table\'s AWS KMS key is accessible again. DynamoDB will initiate the table archival process when table\'s AWS KMS key remains inaccessible for more than seven days from this date.



ArchivalSummary (dict) --Contains information about the table archive.

ArchivalDateTime (datetime) --The date and time when table archival was initiated by DynamoDB, in UNIX epoch time format.

ArchivalReason (string) --The reason DynamoDB archived the table. Currently, the only possible value is:

INACCESSIBLE_ENCRYPTION_CREDENTIALS - The table was archived due to the table\'s AWS KMS key being inaccessible for more than seven days. An On-Demand backup was created at the archival time.


ArchivalBackupArn (string) --The Amazon Resource Name (ARN) of the backup the table was archived to, when applicable in the archival reason. If you wish to restore this backup to the same table name, you will need to delete the original table.










Exceptions

DynamoDB.Client.exceptions.ResourceInUseException
DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.LimitExceededException
DynamoDB.Client.exceptions.InternalServerError

Examples
This example deletes the Music table.
response = client.delete_table(
    TableName='Music',
)

print(response)


Expected Output:
{
    'TableDescription': {
        'ItemCount': 0,
        'ProvisionedThroughput': {
            'NumberOfDecreasesToday': 1,
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        },
        'TableName': 'Music',
        'TableSizeBytes': 0,
        'TableStatus': 'DELETING',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TableDescription': {
            'AttributeDefinitions': [
                {
                    'AttributeName': 'string',
                    'AttributeType': 'S'|'N'|'B'
                },
            ],
            'TableName': 'string',
            'KeySchema': [
                {
                    'AttributeName': 'string',
                    'KeyType': 'HASH'|'RANGE'
                },
            ],
            'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
            'CreationDateTime': datetime(2015, 1, 1),
            'ProvisionedThroughput': {
                'LastIncreaseDateTime': datetime(2015, 1, 1),
                'LastDecreaseDateTime': datetime(2015, 1, 1),
                'NumberOfDecreasesToday': 123,
                'ReadCapacityUnits': 123,
                'WriteCapacityUnits': 123
            },
            'TableSizeBytes': 123,
            'ItemCount': 123,
            'TableArn': 'string',
            'TableId': 'string',
            'BillingModeSummary': {
                'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
                'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
            },
            'LocalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'IndexSizeBytes': 123,
                    'ItemCount': 123,
                    'IndexArn': 'string'
                },
            ],
            'GlobalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                    'Backfilling': True|False,
                    'ProvisionedThroughput': {
                        'LastIncreaseDateTime': datetime(2015, 1, 1),
                        'LastDecreaseDateTime': datetime(2015, 1, 1),
                        'NumberOfDecreasesToday': 123,
                        'ReadCapacityUnits': 123,
                        'WriteCapacityUnits': 123
                    },
                    'IndexSizeBytes': 123,
                    'ItemCount': 123,
                    'IndexArn': 'string'
                },
            ],
            'StreamSpecification': {
                'StreamEnabled': True|False,
                'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
            },
            'LatestStreamLabel': 'string',
            'LatestStreamArn': 'string',
            'GlobalTableVersion': 'string',
            'Replicas': [
                {
                    'RegionName': 'string',
                    'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                    'ReplicaStatusDescription': 'string',
                    'ReplicaStatusPercentProgress': 'string',
                    'KMSMasterKeyId': 'string',
                    'ProvisionedThroughputOverride': {
                        'ReadCapacityUnits': 123
                    },
                    'GlobalSecondaryIndexes': [
                        {
                            'IndexName': 'string',
                            'ProvisionedThroughputOverride': {
                                'ReadCapacityUnits': 123
                            }
                        },
                    ]
                },
            ],
            'RestoreSummary': {
                'SourceBackupArn': 'string',
                'SourceTableArn': 'string',
                'RestoreDateTime': datetime(2015, 1, 1),
                'RestoreInProgress': True|False
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
                'SSEType': 'AES256'|'KMS',
                'KMSMasterKeyArn': 'string',
                'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
            },
            'ArchivalSummary': {
                'ArchivalDateTime': datetime(2015, 1, 1),
                'ArchivalReason': 'string',
                'ArchivalBackupArn': 'string'
            }
        }
    }
    
    
    :returns: 
    S - the attribute is of type String
    N - the attribute is of type Number
    B - the attribute is of type Binary
    
    """
    pass

def describe_backup(BackupArn=None):
    """
    Describes an existing backup of a table.
    You can call DescribeBackup at a maximum rate of 10 times per second.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_backup(
        BackupArn='string'
    )
    
    
    :type BackupArn: string
    :param BackupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) associated with the backup.\n

    :rtype: dict
ReturnsResponse Syntax{
    'BackupDescription': {
        'BackupDetails': {
            'BackupArn': 'string',
            'BackupName': 'string',
            'BackupSizeBytes': 123,
            'BackupStatus': 'CREATING'|'DELETED'|'AVAILABLE',
            'BackupType': 'USER'|'SYSTEM'|'AWS_BACKUP',
            'BackupCreationDateTime': datetime(2015, 1, 1),
            'BackupExpiryDateTime': datetime(2015, 1, 1)
        },
        'SourceTableDetails': {
            'TableName': 'string',
            'TableId': 'string',
            'TableArn': 'string',
            'TableSizeBytes': 123,
            'KeySchema': [
                {
                    'AttributeName': 'string',
                    'KeyType': 'HASH'|'RANGE'
                },
            ],
            'TableCreationDateTime': datetime(2015, 1, 1),
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 123,
                'WriteCapacityUnits': 123
            },
            'ItemCount': 123,
            'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST'
        },
        'SourceTableFeatureDetails': {
            'LocalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    }
                },
            ],
            'GlobalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 123,
                        'WriteCapacityUnits': 123
                    }
                },
            ],
            'StreamDescription': {
                'StreamEnabled': True|False,
                'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
            },
            'TimeToLiveDescription': {
                'TimeToLiveStatus': 'ENABLING'|'DISABLING'|'ENABLED'|'DISABLED',
                'AttributeName': 'string'
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
                'SSEType': 'AES256'|'KMS',
                'KMSMasterKeyArn': 'string',
                'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
            }
        }
    }
}


Response Structure

(dict) --
BackupDescription (dict) --Contains the description of the backup created for the table.

BackupDetails (dict) --Contains the details of the backup created for the table.

BackupArn (string) --ARN associated with the backup.

BackupName (string) --Name of the requested backup.

BackupSizeBytes (integer) --Size of the backup in bytes.

BackupStatus (string) --Backup can be in one of the following states: CREATING, ACTIVE, DELETED.

BackupType (string) --BackupType:

USER - You create and manage these using the on-demand backup feature.
SYSTEM - If you delete a table with point-in-time recovery enabled, a SYSTEM backup is automatically created and is retained for 35 days (at no additional cost). System backups allow you to restore the deleted table to the state it was in just before the point of deletion.
AWS_BACKUP - On-demand backup created by you from AWS Backup service.


BackupCreationDateTime (datetime) --Time at which the backup was created. This is the request time of the backup.

BackupExpiryDateTime (datetime) --Time at which the automatic on-demand backup created by DynamoDB will expire. This SYSTEM on-demand backup expires automatically 35 days after its creation.



SourceTableDetails (dict) --Contains the details of the table when the backup was created.

TableName (string) --The name of the table for which the backup was created.

TableId (string) --Unique identifier for the table for which the backup was created.

TableArn (string) --ARN of the table for which backup was created.

TableSizeBytes (integer) --Size of the table in bytes. Note that this is an approximate value.

KeySchema (list) --Schema of the table.

(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --The name of a key attribute.

KeyType (string) --The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






TableCreationDateTime (datetime) --Time when the source table was created.

ProvisionedThroughput (dict) --Read IOPs and Write IOPS on the table when the backup was created.

ReadCapacityUnits (integer) --The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.

WriteCapacityUnits (integer) --The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.



ItemCount (integer) --Number of items in the table. Note that this is an approximate value.

BillingMode (string) --Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.

PROVISIONED - Sets the read/write capacity mode to PROVISIONED . We recommend using PROVISIONED for predictable workloads.
PAY_PER_REQUEST - Sets the read/write capacity mode to PAY_PER_REQUEST . We recommend using PAY_PER_REQUEST for unpredictable workloads.




SourceTableFeatureDetails (dict) --Contains the details of the features enabled on the table when the backup was created. For example, LSIs, GSIs, streams, TTL.

LocalSecondaryIndexes (list) --Represents the LSI properties for the table when the backup was created. It includes the IndexName, KeySchema and Projection for the LSIs on the table at the time of backup.

(dict) --Represents the properties of a local secondary index for the table when the backup was created.

IndexName (string) --Represents the name of the local secondary index.

KeySchema (list) --The complete key schema for a local secondary index, which consists of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --The name of a key attribute.

KeyType (string) --The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --








GlobalSecondaryIndexes (list) --Represents the GSI properties for the table when the backup was created. It includes the IndexName, KeySchema, Projection, and ProvisionedThroughput for the GSIs on the table at the time of backup.

(dict) --Represents the properties of a global secondary index for the table when the backup was created.

IndexName (string) --The name of the global secondary index.

KeySchema (list) --The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --The name of a key attribute.

KeyType (string) --The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --




ProvisionedThroughput (dict) --Represents the provisioned throughput settings for the specified global secondary index.

ReadCapacityUnits (integer) --The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.

WriteCapacityUnits (integer) --The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.







StreamDescription (dict) --Stream settings on the table when the backup was created.

StreamEnabled (boolean) --Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.

StreamViewType (string) --When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are:

KEYS_ONLY - Only the key attributes of the modified item are written to the stream.
NEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.
OLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.
NEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream.




TimeToLiveDescription (dict) --Time to Live settings on the table when the backup was created.

TimeToLiveStatus (string) --The TTL status for the table.

AttributeName (string) --The name of the TTL attribute for items in the table.



SSEDescription (dict) --The description of the server-side encryption status on the table when the backup was created.

Status (string) --Represents the current state of server-side encryption. The only supported values are:

ENABLED - Server-side encryption is enabled.
UPDATING - Server-side encryption is being updated.


SSEType (string) --Server-side encryption type. The only supported value is:

KMS - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).


KMSMasterKeyArn (string) --The AWS KMS customer master key (CMK) ARN used for the AWS KMS encryption.

InaccessibleEncryptionDateTime (datetime) --Indicates the time, in UNIX epoch date format, when DynamoDB detected that the table\'s AWS KMS key was inaccessible. This attribute will automatically be cleared when DynamoDB detects that the table\'s AWS KMS key is accessible again. DynamoDB will initiate the table archival process when table\'s AWS KMS key remains inaccessible for more than seven days from this date.












Exceptions

DynamoDB.Client.exceptions.BackupNotFoundException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'BackupDescription': {
            'BackupDetails': {
                'BackupArn': 'string',
                'BackupName': 'string',
                'BackupSizeBytes': 123,
                'BackupStatus': 'CREATING'|'DELETED'|'AVAILABLE',
                'BackupType': 'USER'|'SYSTEM'|'AWS_BACKUP',
                'BackupCreationDateTime': datetime(2015, 1, 1),
                'BackupExpiryDateTime': datetime(2015, 1, 1)
            },
            'SourceTableDetails': {
                'TableName': 'string',
                'TableId': 'string',
                'TableArn': 'string',
                'TableSizeBytes': 123,
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'TableCreationDateTime': datetime(2015, 1, 1),
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                },
                'ItemCount': 123,
                'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST'
            },
            'SourceTableFeatureDetails': {
                'LocalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'KeySchema': [
                            {
                                'AttributeName': 'string',
                                'KeyType': 'HASH'|'RANGE'
                            },
                        ],
                        'Projection': {
                            'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                            'NonKeyAttributes': [
                                'string',
                            ]
                        }
                    },
                ],
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'KeySchema': [
                            {
                                'AttributeName': 'string',
                                'KeyType': 'HASH'|'RANGE'
                            },
                        ],
                        'Projection': {
                            'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                            'NonKeyAttributes': [
                                'string',
                            ]
                        },
                        'ProvisionedThroughput': {
                            'ReadCapacityUnits': 123,
                            'WriteCapacityUnits': 123
                        }
                    },
                ],
                'StreamDescription': {
                    'StreamEnabled': True|False,
                    'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
                },
                'TimeToLiveDescription': {
                    'TimeToLiveStatus': 'ENABLING'|'DISABLING'|'ENABLED'|'DISABLED',
                    'AttributeName': 'string'
                },
                'SSEDescription': {
                    'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
                    'SSEType': 'AES256'|'KMS',
                    'KMSMasterKeyArn': 'string',
                    'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
                }
            }
        }
    }
    
    
    :returns: 
    HASH - partition key
    RANGE - sort key
    
    """
    pass

def describe_continuous_backups(TableName=None):
    """
    Checks the status of continuous backups and point in time recovery on the specified table. Continuous backups are ENABLED on all tables at table creation. If point in time recovery is enabled, PointInTimeRecoveryStatus will be set to ENABLED.
    After continuous backups and point in time recovery are enabled, you can restore to any point in time within EarliestRestorableDateTime and LatestRestorableDateTime .
    You can call DescribeContinuousBackups at a maximum rate of 10 times per second.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_continuous_backups(
        TableName='string'
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nName of the table for which the customer wants to check the continuous backups and point in time recovery settings.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ContinuousBackupsDescription': {
        'ContinuousBackupsStatus': 'ENABLED'|'DISABLED',
        'PointInTimeRecoveryDescription': {
            'PointInTimeRecoveryStatus': 'ENABLED'|'DISABLED',
            'EarliestRestorableDateTime': datetime(2015, 1, 1),
            'LatestRestorableDateTime': datetime(2015, 1, 1)
        }
    }
}


Response Structure

(dict) --
ContinuousBackupsDescription (dict) --Represents the continuous backups and point in time recovery settings on the table.

ContinuousBackupsStatus (string) --
ContinuousBackupsStatus can be one of the following states: ENABLED, DISABLED

PointInTimeRecoveryDescription (dict) --The description of the point in time recovery settings applied to the table.

PointInTimeRecoveryStatus (string) --The current state of point in time recovery:

ENABLING - Point in time recovery is being enabled.
ENABLED - Point in time recovery is enabled.
DISABLED - Point in time recovery is disabled.


EarliestRestorableDateTime (datetime) --Specifies the earliest point in time you can restore your table to. You can restore your table to any point in time during the last 35 days.

LatestRestorableDateTime (datetime) --
LatestRestorableDateTime is typically 5 minutes before the current time.










Exceptions

DynamoDB.Client.exceptions.TableNotFoundException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'ContinuousBackupsDescription': {
            'ContinuousBackupsStatus': 'ENABLED'|'DISABLED',
            'PointInTimeRecoveryDescription': {
                'PointInTimeRecoveryStatus': 'ENABLED'|'DISABLED',
                'EarliestRestorableDateTime': datetime(2015, 1, 1),
                'LatestRestorableDateTime': datetime(2015, 1, 1)
            }
        }
    }
    
    
    :returns: 
    DynamoDB.Client.exceptions.TableNotFoundException
    DynamoDB.Client.exceptions.InternalServerError
    
    """
    pass

def describe_contributor_insights(TableName=None, IndexName=None):
    """
    Returns information about contributor insights, for a given table or global secondary index.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_contributor_insights(
        TableName='string',
        IndexName='string'
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table to describe.\n

    :type IndexName: string
    :param IndexName: The name of the global secondary index to describe, if applicable.

    :rtype: dict

ReturnsResponse Syntax
{
    'TableName': 'string',
    'IndexName': 'string',
    'ContributorInsightsRuleList': [
        'string',
    ],
    'ContributorInsightsStatus': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'FAILED',
    'LastUpdateDateTime': datetime(2015, 1, 1),
    'FailureException': {
        'ExceptionName': 'string',
        'ExceptionDescription': 'string'
    }
}


Response Structure

(dict) --

TableName (string) --
The name of the table being described.

IndexName (string) --
The name of the global secondary index being described.

ContributorInsightsRuleList (list) --
List of names of the associated Alpine rules.

(string) --


ContributorInsightsStatus (string) --
Current Status contributor insights.

LastUpdateDateTime (datetime) --
Timestamp of the last time the status was changed.

FailureException (dict) --
Returns information about the last failure that encountered.
The most common exceptions for a FAILED status are:

LimitExceededException - Per-account Amazon CloudWatch Contributor Insights rule limit reached. Please disable Contributor Insights for other tables/indexes OR disable Contributor Insights rules before retrying.
AccessDeniedException - Amazon CloudWatch Contributor Insights rules cannot be modified due to insufficient permissions.
AccessDeniedException - Failed to create service-linked role for Contributor Insights due to insufficient permissions.
InternalServerError - Failed to create Amazon CloudWatch Contributor Insights rules. Please retry request.


ExceptionName (string) --
Exception name.

ExceptionDescription (string) --
Description of the failure.









Exceptions

DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'TableName': 'string',
        'IndexName': 'string',
        'ContributorInsightsRuleList': [
            'string',
        ],
        'ContributorInsightsStatus': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'FAILED',
        'LastUpdateDateTime': datetime(2015, 1, 1),
        'FailureException': {
            'ExceptionName': 'string',
            'ExceptionDescription': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_endpoints():
    """
    Returns the regional endpoint information.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_endpoints()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'Endpoints': [
        {
            'Address': 'string',
            'CachePeriodInMinutes': 123
        },
    ]
}


Response Structure

(dict) --
Endpoints (list) --List of endpoints.

(dict) --An endpoint information details.

Address (string) --IP address of the endpoint.

CachePeriodInMinutes (integer) --Endpoint cache time to live (TTL) value.











    :return: {
        'Endpoints': [
            {
                'Address': 'string',
                'CachePeriodInMinutes': 123
            },
        ]
    }
    
    
    """
    pass

def describe_global_table(GlobalTableName=None):
    """
    Returns information about the specified global table.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_global_table(
        GlobalTableName='string'
    )
    
    
    :type GlobalTableName: string
    :param GlobalTableName: [REQUIRED]\nThe name of the global table.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GlobalTableDescription': {
        'ReplicationGroup': [
            {
                'RegionName': 'string',
                'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                'ReplicaStatusDescription': 'string',
                'ReplicaStatusPercentProgress': 'string',
                'KMSMasterKeyId': 'string',
                'ProvisionedThroughputOverride': {
                    'ReadCapacityUnits': 123
                },
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'ProvisionedThroughputOverride': {
                            'ReadCapacityUnits': 123
                        }
                    },
                ]
            },
        ],
        'GlobalTableArn': 'string',
        'CreationDateTime': datetime(2015, 1, 1),
        'GlobalTableStatus': 'CREATING'|'ACTIVE'|'DELETING'|'UPDATING',
        'GlobalTableName': 'string'
    }
}


Response Structure

(dict) --
GlobalTableDescription (dict) --Contains the details of the global table.

ReplicationGroup (list) --The Regions where the global table has replicas.

(dict) --Contains the details of the replica.

RegionName (string) --The name of the Region.

ReplicaStatus (string) --The current state of the replica:

CREATING - The replica is being created.
UPDATING - The replica is being updated.
DELETING - The replica is being deleted.
ACTIVE - The replica is ready for use.


ReplicaStatusDescription (string) --Detailed information about the replica status.

ReplicaStatusPercentProgress (string) --Specifies the progress of a Create, Update, or Delete action on the replica as a percentage.

KMSMasterKeyId (string) --The AWS KMS customer master key (CMK) of the replica that will be used for AWS KMS encryption.

ProvisionedThroughputOverride (dict) --Replica-specific provisioned throughput. If not described, uses the source table\'s provisioned throughput settings.

ReadCapacityUnits (integer) --Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.



GlobalSecondaryIndexes (list) --Replica-specific global secondary index settings.

(dict) --Represents the properties of a replica global secondary index.

IndexName (string) --The name of the global secondary index.

ProvisionedThroughputOverride (dict) --If not described, uses the source table GSI\'s read capacity settings.

ReadCapacityUnits (integer) --Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.











GlobalTableArn (string) --The unique identifier of the global table.

CreationDateTime (datetime) --The creation time of the global table.

GlobalTableStatus (string) --The current state of the global table:

CREATING - The global table is being created.
UPDATING - The global table is being updated.
DELETING - The global table is being deleted.
ACTIVE - The global table is ready for use.


GlobalTableName (string) --The global table name.








Exceptions

DynamoDB.Client.exceptions.InternalServerError
DynamoDB.Client.exceptions.GlobalTableNotFoundException


    :return: {
        'GlobalTableDescription': {
            'ReplicationGroup': [
                {
                    'RegionName': 'string',
                    'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                    'ReplicaStatusDescription': 'string',
                    'ReplicaStatusPercentProgress': 'string',
                    'KMSMasterKeyId': 'string',
                    'ProvisionedThroughputOverride': {
                        'ReadCapacityUnits': 123
                    },
                    'GlobalSecondaryIndexes': [
                        {
                            'IndexName': 'string',
                            'ProvisionedThroughputOverride': {
                                'ReadCapacityUnits': 123
                            }
                        },
                    ]
                },
            ],
            'GlobalTableArn': 'string',
            'CreationDateTime': datetime(2015, 1, 1),
            'GlobalTableStatus': 'CREATING'|'ACTIVE'|'DELETING'|'UPDATING',
            'GlobalTableName': 'string'
        }
    }
    
    
    :returns: 
    CREATING - The global table is being created.
    UPDATING - The global table is being updated.
    DELETING - The global table is being deleted.
    ACTIVE - The global table is ready for use.
    
    """
    pass

def describe_global_table_settings(GlobalTableName=None):
    """
    Describes Region-specific settings for a global table.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_global_table_settings(
        GlobalTableName='string'
    )
    
    
    :type GlobalTableName: string
    :param GlobalTableName: [REQUIRED]\nThe name of the global table to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GlobalTableName': 'string',
    'ReplicaSettings': [
        {
            'RegionName': 'string',
            'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
            'ReplicaBillingModeSummary': {
                'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
                'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
            },
            'ReplicaProvisionedReadCapacityUnits': 123,
            'ReplicaProvisionedReadCapacityAutoScalingSettings': {
                'MinimumUnits': 123,
                'MaximumUnits': 123,
                'AutoScalingDisabled': True|False,
                'AutoScalingRoleArn': 'string',
                'ScalingPolicies': [
                    {
                        'PolicyName': 'string',
                        'TargetTrackingScalingPolicyConfiguration': {
                            'DisableScaleIn': True|False,
                            'ScaleInCooldown': 123,
                            'ScaleOutCooldown': 123,
                            'TargetValue': 123.0
                        }
                    },
                ]
            },
            'ReplicaProvisionedWriteCapacityUnits': 123,
            'ReplicaProvisionedWriteCapacityAutoScalingSettings': {
                'MinimumUnits': 123,
                'MaximumUnits': 123,
                'AutoScalingDisabled': True|False,
                'AutoScalingRoleArn': 'string',
                'ScalingPolicies': [
                    {
                        'PolicyName': 'string',
                        'TargetTrackingScalingPolicyConfiguration': {
                            'DisableScaleIn': True|False,
                            'ScaleInCooldown': 123,
                            'ScaleOutCooldown': 123,
                            'TargetValue': 123.0
                        }
                    },
                ]
            },
            'ReplicaGlobalSecondaryIndexSettings': [
                {
                    'IndexName': 'string',
                    'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                    'ProvisionedReadCapacityUnits': 123,
                    'ProvisionedReadCapacityAutoScalingSettings': {
                        'MinimumUnits': 123,
                        'MaximumUnits': 123,
                        'AutoScalingDisabled': True|False,
                        'AutoScalingRoleArn': 'string',
                        'ScalingPolicies': [
                            {
                                'PolicyName': 'string',
                                'TargetTrackingScalingPolicyConfiguration': {
                                    'DisableScaleIn': True|False,
                                    'ScaleInCooldown': 123,
                                    'ScaleOutCooldown': 123,
                                    'TargetValue': 123.0
                                }
                            },
                        ]
                    },
                    'ProvisionedWriteCapacityUnits': 123,
                    'ProvisionedWriteCapacityAutoScalingSettings': {
                        'MinimumUnits': 123,
                        'MaximumUnits': 123,
                        'AutoScalingDisabled': True|False,
                        'AutoScalingRoleArn': 'string',
                        'ScalingPolicies': [
                            {
                                'PolicyName': 'string',
                                'TargetTrackingScalingPolicyConfiguration': {
                                    'DisableScaleIn': True|False,
                                    'ScaleInCooldown': 123,
                                    'ScaleOutCooldown': 123,
                                    'TargetValue': 123.0
                                }
                            },
                        ]
                    }
                },
            ]
        },
    ]
}


Response Structure

(dict) --
GlobalTableName (string) --The name of the global table.

ReplicaSettings (list) --The Region-specific settings for the global table.

(dict) --Represents the properties of a replica.

RegionName (string) --The Region name of the replica.

ReplicaStatus (string) --The current state of the Region:

CREATING - The Region is being created.
UPDATING - The Region is being updated.
DELETING - The Region is being deleted.
ACTIVE - The Region is ready for use.


ReplicaBillingModeSummary (dict) --The read/write capacity mode of the replica.

BillingMode (string) --Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.

PROVISIONED - Sets the read/write capacity mode to PROVISIONED . We recommend using PROVISIONED for predictable workloads.
PAY_PER_REQUEST - Sets the read/write capacity mode to PAY_PER_REQUEST . We recommend using PAY_PER_REQUEST for unpredictable workloads.


LastUpdateToPayPerRequestDateTime (datetime) --Represents the time when PAY_PER_REQUEST was last set as the read/write capacity mode.



ReplicaProvisionedReadCapacityUnits (integer) --The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .

ReplicaProvisionedReadCapacityAutoScalingSettings (dict) --Auto scaling settings for a global table replica\'s read capacity units.

MinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --Information about the scaling policies.

(dict) --Represents the properties of the scaling policy.

PolicyName (string) --The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).









ReplicaProvisionedWriteCapacityUnits (integer) --The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .

ReplicaProvisionedWriteCapacityAutoScalingSettings (dict) --Auto scaling settings for a global table replica\'s write capacity units.

MinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --Information about the scaling policies.

(dict) --Represents the properties of the scaling policy.

PolicyName (string) --The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).









ReplicaGlobalSecondaryIndexSettings (list) --Replica global secondary index settings for the global table.

(dict) --Represents the properties of a global secondary index.

IndexName (string) --The name of the global secondary index. The name must be unique among all other indexes on this table.

IndexStatus (string) --The current status of the global secondary index:

CREATING - The global secondary index is being created.
UPDATING - The global secondary index is being updated.
DELETING - The global secondary index is being deleted.
ACTIVE - The global secondary index is ready for use.


ProvisionedReadCapacityUnits (integer) --The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException .

ProvisionedReadCapacityAutoScalingSettings (dict) --Auto scaling settings for a global secondary index replica\'s read capacity units.

MinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --Information about the scaling policies.

(dict) --Represents the properties of the scaling policy.

PolicyName (string) --The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).









ProvisionedWriteCapacityUnits (integer) --The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException .

ProvisionedWriteCapacityAutoScalingSettings (dict) --Auto scaling settings for a global secondary index replica\'s write capacity units.

MinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --Information about the scaling policies.

(dict) --Represents the properties of the scaling policy.

PolicyName (string) --The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).






















Exceptions

DynamoDB.Client.exceptions.GlobalTableNotFoundException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'GlobalTableName': 'string',
        'ReplicaSettings': [
            {
                'RegionName': 'string',
                'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                'ReplicaBillingModeSummary': {
                    'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
                    'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
                },
                'ReplicaProvisionedReadCapacityUnits': 123,
                'ReplicaProvisionedReadCapacityAutoScalingSettings': {
                    'MinimumUnits': 123,
                    'MaximumUnits': 123,
                    'AutoScalingDisabled': True|False,
                    'AutoScalingRoleArn': 'string',
                    'ScalingPolicies': [
                        {
                            'PolicyName': 'string',
                            'TargetTrackingScalingPolicyConfiguration': {
                                'DisableScaleIn': True|False,
                                'ScaleInCooldown': 123,
                                'ScaleOutCooldown': 123,
                                'TargetValue': 123.0
                            }
                        },
                    ]
                },
                'ReplicaProvisionedWriteCapacityUnits': 123,
                'ReplicaProvisionedWriteCapacityAutoScalingSettings': {
                    'MinimumUnits': 123,
                    'MaximumUnits': 123,
                    'AutoScalingDisabled': True|False,
                    'AutoScalingRoleArn': 'string',
                    'ScalingPolicies': [
                        {
                            'PolicyName': 'string',
                            'TargetTrackingScalingPolicyConfiguration': {
                                'DisableScaleIn': True|False,
                                'ScaleInCooldown': 123,
                                'ScaleOutCooldown': 123,
                                'TargetValue': 123.0
                            }
                        },
                    ]
                },
                'ReplicaGlobalSecondaryIndexSettings': [
                    {
                        'IndexName': 'string',
                        'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                        'ProvisionedReadCapacityUnits': 123,
                        'ProvisionedReadCapacityAutoScalingSettings': {
                            'MinimumUnits': 123,
                            'MaximumUnits': 123,
                            'AutoScalingDisabled': True|False,
                            'AutoScalingRoleArn': 'string',
                            'ScalingPolicies': [
                                {
                                    'PolicyName': 'string',
                                    'TargetTrackingScalingPolicyConfiguration': {
                                        'DisableScaleIn': True|False,
                                        'ScaleInCooldown': 123,
                                        'ScaleOutCooldown': 123,
                                        'TargetValue': 123.0
                                    }
                                },
                            ]
                        },
                        'ProvisionedWriteCapacityUnits': 123,
                        'ProvisionedWriteCapacityAutoScalingSettings': {
                            'MinimumUnits': 123,
                            'MaximumUnits': 123,
                            'AutoScalingDisabled': True|False,
                            'AutoScalingRoleArn': 'string',
                            'ScalingPolicies': [
                                {
                                    'PolicyName': 'string',
                                    'TargetTrackingScalingPolicyConfiguration': {
                                        'DisableScaleIn': True|False,
                                        'ScaleInCooldown': 123,
                                        'ScaleOutCooldown': 123,
                                        'TargetValue': 123.0
                                    }
                                },
                            ]
                        }
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    PROVISIONED - Sets the read/write capacity mode to PROVISIONED . We recommend using PROVISIONED for predictable workloads.
    PAY_PER_REQUEST - Sets the read/write capacity mode to PAY_PER_REQUEST . We recommend using PAY_PER_REQUEST for unpredictable workloads.
    
    """
    pass

def describe_limits():
    """
    Returns the current provisioned-capacity limits for your AWS account in a Region, both for the Region as a whole and for any one DynamoDB table that you create there.
    When you establish an AWS account, the account has initial limits on the maximum read capacity units and write capacity units that you can provision across all of your DynamoDB tables in a given Region. Also, there are per-table limits that apply when you create a table there. For more information, see Limits page in the Amazon DynamoDB Developer Guide .
    Although you can increase these limits by filing a case at AWS Support Center , obtaining the increase is not instantaneous. The DescribeLimits action lets you write code to compare the capacity you are currently using to those limits imposed by your account so that you have enough time to apply for an increase before you hit a limit.
    For example, you could use one of the AWS SDKs to do the following:
    This will let you see whether you are getting close to your account-level limits.
    The per-table limits apply only when you are creating a new table. They restrict the sum of the provisioned capacity of the new table itself and all its global secondary indexes.
    For existing tables and their GSIs, DynamoDB doesn\'t let you increase provisioned capacity extremely rapidly. But the only upper limit that applies is that the aggregate provisioned capacity over all your tables and GSIs cannot exceed either of the per-account limits.
    The DescribeLimits Request element has no content.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns the maximum read and write capacity units per table, and for the AWS account, in the current AWS region.
    Expected Output:
    
    :example: response = client.describe_limits()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'AccountMaxReadCapacityUnits': 123,
    'AccountMaxWriteCapacityUnits': 123,
    'TableMaxReadCapacityUnits': 123,
    'TableMaxWriteCapacityUnits': 123
}


Response Structure

(dict) --Represents the output of a DescribeLimits operation.

AccountMaxReadCapacityUnits (integer) --The maximum total read capacity units that your account allows you to provision across all of your tables in this Region.

AccountMaxWriteCapacityUnits (integer) --The maximum total write capacity units that your account allows you to provision across all of your tables in this Region.

TableMaxReadCapacityUnits (integer) --The maximum read capacity units that your account allows you to provision for a new table that you are creating in this Region, including the read capacity units provisioned for its global secondary indexes (GSIs).

TableMaxWriteCapacityUnits (integer) --The maximum write capacity units that your account allows you to provision for a new table that you are creating in this Region, including the write capacity units provisioned for its global secondary indexes (GSIs).






Exceptions

DynamoDB.Client.exceptions.InternalServerError

Examples
The following example returns the maximum read and write capacity units per table, and for the AWS account, in the current AWS region.
response = client.describe_limits(
)

print(response)


Expected Output:
{
    'AccountMaxReadCapacityUnits': 20000,
    'AccountMaxWriteCapacityUnits': 20000,
    'TableMaxReadCapacityUnits': 10000,
    'TableMaxWriteCapacityUnits': 10000,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AccountMaxReadCapacityUnits': 123,
        'AccountMaxWriteCapacityUnits': 123,
        'TableMaxReadCapacityUnits': 123,
        'TableMaxWriteCapacityUnits': 123
    }
    
    
    :returns: 
    DynamoDB.Client.exceptions.InternalServerError
    
    """
    pass

def describe_table(TableName=None):
    """
    Returns information about the table, including the current status of the table, when it was created, the primary key schema, and any indexes on the table.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the Music table.
    Expected Output:
    
    :example: response = client.describe_table(
        TableName='string'
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Table': {
        'AttributeDefinitions': [
            {
                'AttributeName': 'string',
                'AttributeType': 'S'|'N'|'B'
            },
        ],
        'TableName': 'string',
        'KeySchema': [
            {
                'AttributeName': 'string',
                'KeyType': 'HASH'|'RANGE'
            },
        ],
        'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
        'CreationDateTime': datetime(2015, 1, 1),
        'ProvisionedThroughput': {
            'LastIncreaseDateTime': datetime(2015, 1, 1),
            'LastDecreaseDateTime': datetime(2015, 1, 1),
            'NumberOfDecreasesToday': 123,
            'ReadCapacityUnits': 123,
            'WriteCapacityUnits': 123
        },
        'TableSizeBytes': 123,
        'ItemCount': 123,
        'TableArn': 'string',
        'TableId': 'string',
        'BillingModeSummary': {
            'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
            'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
        },
        'LocalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexArn': 'string'
            },
        ],
        'GlobalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                'Backfilling': True|False,
                'ProvisionedThroughput': {
                    'LastIncreaseDateTime': datetime(2015, 1, 1),
                    'LastDecreaseDateTime': datetime(2015, 1, 1),
                    'NumberOfDecreasesToday': 123,
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexArn': 'string'
            },
        ],
        'StreamSpecification': {
            'StreamEnabled': True|False,
            'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
        },
        'LatestStreamLabel': 'string',
        'LatestStreamArn': 'string',
        'GlobalTableVersion': 'string',
        'Replicas': [
            {
                'RegionName': 'string',
                'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                'ReplicaStatusDescription': 'string',
                'ReplicaStatusPercentProgress': 'string',
                'KMSMasterKeyId': 'string',
                'ProvisionedThroughputOverride': {
                    'ReadCapacityUnits': 123
                },
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'ProvisionedThroughputOverride': {
                            'ReadCapacityUnits': 123
                        }
                    },
                ]
            },
        ],
        'RestoreSummary': {
            'SourceBackupArn': 'string',
            'SourceTableArn': 'string',
            'RestoreDateTime': datetime(2015, 1, 1),
            'RestoreInProgress': True|False
        },
        'SSEDescription': {
            'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
            'SSEType': 'AES256'|'KMS',
            'KMSMasterKeyArn': 'string',
            'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
        },
        'ArchivalSummary': {
            'ArchivalDateTime': datetime(2015, 1, 1),
            'ArchivalReason': 'string',
            'ArchivalBackupArn': 'string'
        }
    }
}


Response Structure

(dict) --Represents the output of a DescribeTable operation.

Table (dict) --The properties of the table.

AttributeDefinitions (list) --An array of AttributeDefinition objects. Each of these objects describes one attribute in the table and index key schema.
Each AttributeDefinition object in this array is composed of:

AttributeName - The name of the attribute.
AttributeType - The data type for the attribute.


(dict) --Represents an attribute for describing the key schema for the table and indexes.

AttributeName (string) --A name for the attribute.

AttributeType (string) --The data type for the attribute, where:

S - the attribute is of type String
N - the attribute is of type Number
B - the attribute is of type Binary






TableName (string) --The name of the table.

KeySchema (list) --The primary key structure for the table. Each KeySchemaElement consists of:

AttributeName - The name of the attribute.
KeyType - The role of the attribute:
HASH - partition key
RANGE - sort key




Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

For more information about primary keys, see Primary Key in the Amazon DynamoDB Developer Guide .

(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --The name of a key attribute.

KeyType (string) --The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






TableStatus (string) --The current state of the table:

CREATING - The table is being created.
UPDATING - The table is being updated.
DELETING - The table is being deleted.
ACTIVE - The table is ready for use.
INACCESSIBLE_ENCRYPTION_CREDENTIALS - The AWS KMS key used to encrypt the table in inaccessible. Table operations may fail due to failure to use the AWS KMS key. DynamoDB will initiate the table archival process when a table\'s AWS KMS key remains inaccessible for more than seven days.
ARCHIVING - The table is being archived. Operations are not allowed until archival is complete.
ARCHIVED - The table has been archived. See the ArchivalReason for more information.


CreationDateTime (datetime) --The date and time when the table was created, in UNIX epoch time format.

ProvisionedThroughput (dict) --The provisioned throughput settings for the table, consisting of read and write capacity units, along with data about increases and decreases.

LastIncreaseDateTime (datetime) --The date and time of the last provisioned throughput increase for this table.

LastDecreaseDateTime (datetime) --The date and time of the last provisioned throughput decrease for this table.

NumberOfDecreasesToday (integer) --The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see Limits in the Amazon DynamoDB Developer Guide .

ReadCapacityUnits (integer) --The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 ReadCapacityUnits per second provides 100 eventually consistent ReadCapacityUnits per second.

WriteCapacityUnits (integer) --The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException .



TableSizeBytes (integer) --The total size of the specified table, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --The number of items in the specified table. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

TableArn (string) --The Amazon Resource Name (ARN) that uniquely identifies the table.

TableId (string) --Unique identifier for the table for which the backup was created.

BillingModeSummary (dict) --Contains the details for the read/write capacity mode.

BillingMode (string) --Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.

PROVISIONED - Sets the read/write capacity mode to PROVISIONED . We recommend using PROVISIONED for predictable workloads.
PAY_PER_REQUEST - Sets the read/write capacity mode to PAY_PER_REQUEST . We recommend using PAY_PER_REQUEST for unpredictable workloads.


LastUpdateToPayPerRequestDateTime (datetime) --Represents the time when PAY_PER_REQUEST was last set as the read/write capacity mode.



LocalSecondaryIndexes (list) --Represents one or more local secondary indexes on the table. Each index is scoped to a given partition key value. Tables with one or more local secondary indexes are subject to an item collection size limit, where the amount of data within a given item collection cannot exceed 10 GB. Each element is composed of:

IndexName - The name of the local secondary index.
KeySchema - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
Projection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
ProjectionType - One of the following:
KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes , summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.


IndexSizeBytes - Represents the total size of the index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
ItemCount - Represents the number of items in the index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

If the table is in the DELETING state, no information about indexes will be returned.

(dict) --Represents the properties of a local secondary index.

IndexName (string) --Represents the name of the local secondary index.

KeySchema (list) --The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --The name of a key attribute.

KeyType (string) --The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --




IndexSizeBytes (integer) --The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

IndexArn (string) --The Amazon Resource Name (ARN) that uniquely identifies the index.





GlobalSecondaryIndexes (list) --The global secondary indexes, if any, on the table. Each index is scoped to a given partition key value. Each element is composed of:

Backfilling - If true, then the index is currently in the backfilling phase. Backfilling occurs only when a new global secondary index is added to the table. It is the process by which DynamoDB populates the new index with data from the table. (This attribute does not appear for indexes that were created during a CreateTable operation.)  You can delete an index that is being created during the Backfilling phase when IndexStatus is set to CREATING and Backfilling is true. You can\'t delete the index that is being created when IndexStatus is set to CREATING and Backfilling is false. (This attribute does not appear for indexes that were created during a CreateTable operation.)
IndexName - The name of the global secondary index.
IndexSizeBytes - The total size of the global secondary index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
IndexStatus - The current status of the global secondary index:
CREATING - The index is being created.
UPDATING - The index is being updated.
DELETING - The index is being deleted.
ACTIVE - The index is ready for use.


ItemCount - The number of items in the global secondary index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
KeySchema - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
Projection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
ProjectionType - One of the following:
KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes , summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.


ProvisionedThroughput - The provisioned throughput settings for the global secondary index, consisting of read and write capacity units, along with data about increases and decreases.

If the table is in the DELETING state, no information about indexes will be returned.

(dict) --Represents the properties of a global secondary index.

IndexName (string) --The name of the global secondary index.

KeySchema (list) --The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --The name of a key attribute.

KeyType (string) --The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --




IndexStatus (string) --The current state of the global secondary index:

CREATING - The index is being created.
UPDATING - The index is being updated.
DELETING - The index is being deleted.
ACTIVE - The index is ready for use.


Backfilling (boolean) --Indicates whether the index is currently backfilling. Backfilling is the process of reading items from the table and determining whether they can be added to the index. (Not all items will qualify: For example, a partition key cannot have any duplicate values.) If an item can be added to the index, DynamoDB will do so. After all items have been processed, the backfilling operation is complete and Backfilling is false.
You can delete an index that is being created during the Backfilling phase when IndexStatus is set to CREATING and Backfilling is true. You can\'t delete the index that is being created when IndexStatus is set to CREATING and Backfilling is false.

Note
For indexes that were created during a CreateTable operation, the Backfilling attribute does not appear in the DescribeTable output.


ProvisionedThroughput (dict) --Represents the provisioned throughput settings for the specified global secondary index.
For current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .

LastIncreaseDateTime (datetime) --The date and time of the last provisioned throughput increase for this table.

LastDecreaseDateTime (datetime) --The date and time of the last provisioned throughput decrease for this table.

NumberOfDecreasesToday (integer) --The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see Limits in the Amazon DynamoDB Developer Guide .

ReadCapacityUnits (integer) --The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 ReadCapacityUnits per second provides 100 eventually consistent ReadCapacityUnits per second.

WriteCapacityUnits (integer) --The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException .



IndexSizeBytes (integer) --The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

IndexArn (string) --The Amazon Resource Name (ARN) that uniquely identifies the index.





StreamSpecification (dict) --The current DynamoDB Streams configuration for the table.

StreamEnabled (boolean) --Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.

StreamViewType (string) --When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are:

KEYS_ONLY - Only the key attributes of the modified item are written to the stream.
NEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.
OLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.
NEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream.




LatestStreamLabel (string) --A timestamp, in ISO 8601 format, for this stream.
Note that LatestStreamLabel is not a unique identifier for the stream, because it is possible that a stream from another table might have the same timestamp. However, the combination of the following three elements is guaranteed to be unique:

AWS customer ID
Table name
StreamLabel


LatestStreamArn (string) --The Amazon Resource Name (ARN) that uniquely identifies the latest stream for this table.

GlobalTableVersion (string) --Represents the version of global tables in use, if the table is replicated across AWS Regions.

Replicas (list) --Represents replicas of the table.

(dict) --Contains the details of the replica.

RegionName (string) --The name of the Region.

ReplicaStatus (string) --The current state of the replica:

CREATING - The replica is being created.
UPDATING - The replica is being updated.
DELETING - The replica is being deleted.
ACTIVE - The replica is ready for use.


ReplicaStatusDescription (string) --Detailed information about the replica status.

ReplicaStatusPercentProgress (string) --Specifies the progress of a Create, Update, or Delete action on the replica as a percentage.

KMSMasterKeyId (string) --The AWS KMS customer master key (CMK) of the replica that will be used for AWS KMS encryption.

ProvisionedThroughputOverride (dict) --Replica-specific provisioned throughput. If not described, uses the source table\'s provisioned throughput settings.

ReadCapacityUnits (integer) --Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.



GlobalSecondaryIndexes (list) --Replica-specific global secondary index settings.

(dict) --Represents the properties of a replica global secondary index.

IndexName (string) --The name of the global secondary index.

ProvisionedThroughputOverride (dict) --If not described, uses the source table GSI\'s read capacity settings.

ReadCapacityUnits (integer) --Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.











RestoreSummary (dict) --Contains details for the restore.

SourceBackupArn (string) --The Amazon Resource Name (ARN) of the backup from which the table was restored.

SourceTableArn (string) --The ARN of the source table of the backup that is being restored.

RestoreDateTime (datetime) --Point in time or source backup time.

RestoreInProgress (boolean) --Indicates if a restore is in progress or not.



SSEDescription (dict) --The description of the server-side encryption status on the specified table.

Status (string) --Represents the current state of server-side encryption. The only supported values are:

ENABLED - Server-side encryption is enabled.
UPDATING - Server-side encryption is being updated.


SSEType (string) --Server-side encryption type. The only supported value is:

KMS - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).


KMSMasterKeyArn (string) --The AWS KMS customer master key (CMK) ARN used for the AWS KMS encryption.

InaccessibleEncryptionDateTime (datetime) --Indicates the time, in UNIX epoch date format, when DynamoDB detected that the table\'s AWS KMS key was inaccessible. This attribute will automatically be cleared when DynamoDB detects that the table\'s AWS KMS key is accessible again. DynamoDB will initiate the table archival process when table\'s AWS KMS key remains inaccessible for more than seven days from this date.



ArchivalSummary (dict) --Contains information about the table archive.

ArchivalDateTime (datetime) --The date and time when table archival was initiated by DynamoDB, in UNIX epoch time format.

ArchivalReason (string) --The reason DynamoDB archived the table. Currently, the only possible value is:

INACCESSIBLE_ENCRYPTION_CREDENTIALS - The table was archived due to the table\'s AWS KMS key being inaccessible for more than seven days. An On-Demand backup was created at the archival time.


ArchivalBackupArn (string) --The Amazon Resource Name (ARN) of the backup the table was archived to, when applicable in the archival reason. If you wish to restore this backup to the same table name, you will need to delete the original table.










Exceptions

DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.InternalServerError

Examples
This example describes the Music table.
response = client.describe_table(
    TableName='Music',
)

print(response)


Expected Output:
{
    'Table': {
        'AttributeDefinitions': [
            {
                'AttributeName': 'Artist',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'SongTitle',
                'AttributeType': 'S',
            },
        ],
        'CreationDateTime': datetime(2015, 1, 21, 19, 2, 32, 2, 21, 0),
        'ItemCount': 0,
        'KeySchema': [
            {
                'AttributeName': 'Artist',
                'KeyType': 'HASH',
            },
            {
                'AttributeName': 'SongTitle',
                'KeyType': 'RANGE',
            },
        ],
        'ProvisionedThroughput': {
            'NumberOfDecreasesToday': 1,
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        },
        'TableName': 'Music',
        'TableSizeBytes': 0,
        'TableStatus': 'ACTIVE',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Table': {
            'AttributeDefinitions': [
                {
                    'AttributeName': 'string',
                    'AttributeType': 'S'|'N'|'B'
                },
            ],
            'TableName': 'string',
            'KeySchema': [
                {
                    'AttributeName': 'string',
                    'KeyType': 'HASH'|'RANGE'
                },
            ],
            'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
            'CreationDateTime': datetime(2015, 1, 1),
            'ProvisionedThroughput': {
                'LastIncreaseDateTime': datetime(2015, 1, 1),
                'LastDecreaseDateTime': datetime(2015, 1, 1),
                'NumberOfDecreasesToday': 123,
                'ReadCapacityUnits': 123,
                'WriteCapacityUnits': 123
            },
            'TableSizeBytes': 123,
            'ItemCount': 123,
            'TableArn': 'string',
            'TableId': 'string',
            'BillingModeSummary': {
                'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
                'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
            },
            'LocalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'IndexSizeBytes': 123,
                    'ItemCount': 123,
                    'IndexArn': 'string'
                },
            ],
            'GlobalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                    'Backfilling': True|False,
                    'ProvisionedThroughput': {
                        'LastIncreaseDateTime': datetime(2015, 1, 1),
                        'LastDecreaseDateTime': datetime(2015, 1, 1),
                        'NumberOfDecreasesToday': 123,
                        'ReadCapacityUnits': 123,
                        'WriteCapacityUnits': 123
                    },
                    'IndexSizeBytes': 123,
                    'ItemCount': 123,
                    'IndexArn': 'string'
                },
            ],
            'StreamSpecification': {
                'StreamEnabled': True|False,
                'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
            },
            'LatestStreamLabel': 'string',
            'LatestStreamArn': 'string',
            'GlobalTableVersion': 'string',
            'Replicas': [
                {
                    'RegionName': 'string',
                    'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                    'ReplicaStatusDescription': 'string',
                    'ReplicaStatusPercentProgress': 'string',
                    'KMSMasterKeyId': 'string',
                    'ProvisionedThroughputOverride': {
                        'ReadCapacityUnits': 123
                    },
                    'GlobalSecondaryIndexes': [
                        {
                            'IndexName': 'string',
                            'ProvisionedThroughputOverride': {
                                'ReadCapacityUnits': 123
                            }
                        },
                    ]
                },
            ],
            'RestoreSummary': {
                'SourceBackupArn': 'string',
                'SourceTableArn': 'string',
                'RestoreDateTime': datetime(2015, 1, 1),
                'RestoreInProgress': True|False
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
                'SSEType': 'AES256'|'KMS',
                'KMSMasterKeyArn': 'string',
                'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
            },
            'ArchivalSummary': {
                'ArchivalDateTime': datetime(2015, 1, 1),
                'ArchivalReason': 'string',
                'ArchivalBackupArn': 'string'
            }
        }
    }
    
    
    :returns: 
    S - the attribute is of type String
    N - the attribute is of type Number
    B - the attribute is of type Binary
    
    """
    pass

def describe_table_replica_auto_scaling(TableName=None):
    """
    Describes auto scaling settings across replicas of the global table at once.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_table_replica_auto_scaling(
        TableName='string'
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TableAutoScalingDescription': {
        'TableName': 'string',
        'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
        'Replicas': [
            {
                'RegionName': 'string',
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                        'ProvisionedReadCapacityAutoScalingSettings': {
                            'MinimumUnits': 123,
                            'MaximumUnits': 123,
                            'AutoScalingDisabled': True|False,
                            'AutoScalingRoleArn': 'string',
                            'ScalingPolicies': [
                                {
                                    'PolicyName': 'string',
                                    'TargetTrackingScalingPolicyConfiguration': {
                                        'DisableScaleIn': True|False,
                                        'ScaleInCooldown': 123,
                                        'ScaleOutCooldown': 123,
                                        'TargetValue': 123.0
                                    }
                                },
                            ]
                        },
                        'ProvisionedWriteCapacityAutoScalingSettings': {
                            'MinimumUnits': 123,
                            'MaximumUnits': 123,
                            'AutoScalingDisabled': True|False,
                            'AutoScalingRoleArn': 'string',
                            'ScalingPolicies': [
                                {
                                    'PolicyName': 'string',
                                    'TargetTrackingScalingPolicyConfiguration': {
                                        'DisableScaleIn': True|False,
                                        'ScaleInCooldown': 123,
                                        'ScaleOutCooldown': 123,
                                        'TargetValue': 123.0
                                    }
                                },
                            ]
                        }
                    },
                ],
                'ReplicaProvisionedReadCapacityAutoScalingSettings': {
                    'MinimumUnits': 123,
                    'MaximumUnits': 123,
                    'AutoScalingDisabled': True|False,
                    'AutoScalingRoleArn': 'string',
                    'ScalingPolicies': [
                        {
                            'PolicyName': 'string',
                            'TargetTrackingScalingPolicyConfiguration': {
                                'DisableScaleIn': True|False,
                                'ScaleInCooldown': 123,
                                'ScaleOutCooldown': 123,
                                'TargetValue': 123.0
                            }
                        },
                    ]
                },
                'ReplicaProvisionedWriteCapacityAutoScalingSettings': {
                    'MinimumUnits': 123,
                    'MaximumUnits': 123,
                    'AutoScalingDisabled': True|False,
                    'AutoScalingRoleArn': 'string',
                    'ScalingPolicies': [
                        {
                            'PolicyName': 'string',
                            'TargetTrackingScalingPolicyConfiguration': {
                                'DisableScaleIn': True|False,
                                'ScaleInCooldown': 123,
                                'ScaleOutCooldown': 123,
                                'TargetValue': 123.0
                            }
                        },
                    ]
                },
                'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE'
            },
        ]
    }
}


Response Structure

(dict) --
TableAutoScalingDescription (dict) --Represents the auto scaling properties of the table.

TableName (string) --The name of the table.

TableStatus (string) --The current state of the table:

CREATING - The table is being created.
UPDATING - The table is being updated.
DELETING - The table is being deleted.
ACTIVE - The table is ready for use.


Replicas (list) --Represents replicas of the global table.

(dict) --Represents the auto scaling settings of the replica.

RegionName (string) --The Region where the replica exists.

GlobalSecondaryIndexes (list) --Replica-specific global secondary index auto scaling settings.

(dict) --Represents the auto scaling configuration for a replica global secondary index.

IndexName (string) --The name of the global secondary index.

IndexStatus (string) --The current state of the replica global secondary index:

CREATING - The index is being created.
UPDATING - The index is being updated.
DELETING - The index is being deleted.
ACTIVE - The index is ready for use.


ProvisionedReadCapacityAutoScalingSettings (dict) --Represents the auto scaling settings for a global table or global secondary index.

MinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --Information about the scaling policies.

(dict) --Represents the properties of the scaling policy.

PolicyName (string) --The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).









ProvisionedWriteCapacityAutoScalingSettings (dict) --Represents the auto scaling settings for a global table or global secondary index.

MinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --Information about the scaling policies.

(dict) --Represents the properties of the scaling policy.

PolicyName (string) --The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).













ReplicaProvisionedReadCapacityAutoScalingSettings (dict) --Represents the auto scaling settings for a global table or global secondary index.

MinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --Information about the scaling policies.

(dict) --Represents the properties of the scaling policy.

PolicyName (string) --The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).









ReplicaProvisionedWriteCapacityAutoScalingSettings (dict) --Represents the auto scaling settings for a global table or global secondary index.

MinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --Information about the scaling policies.

(dict) --Represents the properties of the scaling policy.

PolicyName (string) --The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).









ReplicaStatus (string) --The current state of the replica:

CREATING - The replica is being created.
UPDATING - The replica is being updated.
DELETING - The replica is being deleted.
ACTIVE - The replica is ready for use.













Exceptions

DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'TableAutoScalingDescription': {
            'TableName': 'string',
            'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
            'Replicas': [
                {
                    'RegionName': 'string',
                    'GlobalSecondaryIndexes': [
                        {
                            'IndexName': 'string',
                            'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                            'ProvisionedReadCapacityAutoScalingSettings': {
                                'MinimumUnits': 123,
                                'MaximumUnits': 123,
                                'AutoScalingDisabled': True|False,
                                'AutoScalingRoleArn': 'string',
                                'ScalingPolicies': [
                                    {
                                        'PolicyName': 'string',
                                        'TargetTrackingScalingPolicyConfiguration': {
                                            'DisableScaleIn': True|False,
                                            'ScaleInCooldown': 123,
                                            'ScaleOutCooldown': 123,
                                            'TargetValue': 123.0
                                        }
                                    },
                                ]
                            },
                            'ProvisionedWriteCapacityAutoScalingSettings': {
                                'MinimumUnits': 123,
                                'MaximumUnits': 123,
                                'AutoScalingDisabled': True|False,
                                'AutoScalingRoleArn': 'string',
                                'ScalingPolicies': [
                                    {
                                        'PolicyName': 'string',
                                        'TargetTrackingScalingPolicyConfiguration': {
                                            'DisableScaleIn': True|False,
                                            'ScaleInCooldown': 123,
                                            'ScaleOutCooldown': 123,
                                            'TargetValue': 123.0
                                        }
                                    },
                                ]
                            }
                        },
                    ],
                    'ReplicaProvisionedReadCapacityAutoScalingSettings': {
                        'MinimumUnits': 123,
                        'MaximumUnits': 123,
                        'AutoScalingDisabled': True|False,
                        'AutoScalingRoleArn': 'string',
                        'ScalingPolicies': [
                            {
                                'PolicyName': 'string',
                                'TargetTrackingScalingPolicyConfiguration': {
                                    'DisableScaleIn': True|False,
                                    'ScaleInCooldown': 123,
                                    'ScaleOutCooldown': 123,
                                    'TargetValue': 123.0
                                }
                            },
                        ]
                    },
                    'ReplicaProvisionedWriteCapacityAutoScalingSettings': {
                        'MinimumUnits': 123,
                        'MaximumUnits': 123,
                        'AutoScalingDisabled': True|False,
                        'AutoScalingRoleArn': 'string',
                        'ScalingPolicies': [
                            {
                                'PolicyName': 'string',
                                'TargetTrackingScalingPolicyConfiguration': {
                                    'DisableScaleIn': True|False,
                                    'ScaleInCooldown': 123,
                                    'ScaleOutCooldown': 123,
                                    'TargetValue': 123.0
                                }
                            },
                        ]
                    },
                    'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE'
                },
            ]
        }
    }
    
    
    :returns: 
    CREATING - The index is being created.
    UPDATING - The index is being updated.
    DELETING - The index is being deleted.
    ACTIVE - The index is ready for use.
    
    """
    pass

def describe_time_to_live(TableName=None):
    """
    Gives a description of the Time to Live (TTL) status on the specified table.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_time_to_live(
        TableName='string'
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table to be described.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TimeToLiveDescription': {
        'TimeToLiveStatus': 'ENABLING'|'DISABLING'|'ENABLED'|'DISABLED',
        'AttributeName': 'string'
    }
}


Response Structure

(dict) --
TimeToLiveDescription (dict) --
TimeToLiveStatus (string) --The TTL status for the table.

AttributeName (string) --The name of the TTL attribute for items in the table.








Exceptions

DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'TimeToLiveDescription': {
            'TimeToLiveStatus': 'ENABLING'|'DISABLING'|'ENABLED'|'DISABLED',
            'AttributeName': 'string'
        }
    }
    
    
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

def get_item(TableName=None, Key=None, AttributesToGet=None, ConsistentRead=None, ReturnConsumedCapacity=None, ProjectionExpression=None, ExpressionAttributeNames=None):
    """
    The GetItem operation returns a set of attributes for the item with the given primary key. If there is no matching item, GetItem does not return any data and there will be no Item element in the response.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example retrieves an item from the Music table. The table has a partition key and a sort key (Artist and SongTitle), so you must specify both of these attributes.
    Expected Output:
    
    :example: response = client.get_item(
        TableName='string',
        Key={
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        AttributesToGet=[
            'string',
        ],
        ConsistentRead=True|False,
        ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
        ProjectionExpression='string',
        ExpressionAttributeNames={
            'string': 'string'
        }
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table containing the requested item.\n

    :type Key: dict
    :param Key: [REQUIRED]\nA map of attribute names to AttributeValue objects, representing the primary key of the item to retrieve.\nFor the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n

    :type AttributesToGet: list
    :param AttributesToGet: This is a legacy parameter. Use ProjectionExpression instead. For more information, see AttributesToGet in the Amazon DynamoDB Developer Guide .\n\n(string) --\n\n

    :type ConsistentRead: boolean
    :param ConsistentRead: Determines the read consistency model: If set to true , then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads.

    :type ReturnConsumedCapacity: string
    :param ReturnConsumedCapacity: Determines the level of detail about provisioned throughput consumption that is returned in the response:\n\nINDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem , do not access any indexes at all. In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s).\nTOTAL - The response includes only the aggregate ConsumedCapacity for the operation.\nNONE - No ConsumedCapacity details are included in the response.\n\n

    :type ProjectionExpression: string
    :param ProjectionExpression: A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.\nIf no attribute names are specified, then all attributes are returned. If any of the requested attributes are not found, they do not appear in the result.\nFor more information, see Specifying Item Attributes in the Amazon DynamoDB Developer Guide .\n

    :type ExpressionAttributeNames: dict
    :param ExpressionAttributeNames: One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames :\n\nTo access an attribute whose name conflicts with a DynamoDB reserved word.\nTo create a placeholder for repeating occurrences of an attribute name in an expression.\nTo prevent special characters in an attribute name from being misinterpreted in an expression.\n\nUse the # character in an expression to dereference an attribute name. For example, consider the following attribute name:\n\nPercentile\n\nThe name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide ). To work around this, you could specify the following for ExpressionAttributeNames :\n\n{'#P':'Percentile'}\n\nYou could then use this substitution in an expression, as in this example:\n\n#P = :val\n\n\nNote\nTokens that begin with the : character are expression attribute values , which are placeholders for the actual value at runtime.\n\nFor more information on expression attribute names, see Specifying Item Attributes in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Item': {
        'string': {
            'S': 'string',
            'N': 'string',
            'B': b'bytes',
            'SS': [
                'string',
            ],
            'NS': [
                'string',
            ],
            'BS': [
                b'bytes',
            ],
            'M': {
                'string': {'... recursive ...'}
            },
            'L': [
                {'... recursive ...'},
            ],
            'NULL': True|False,
            'BOOL': True|False
        }
    },
    'ConsumedCapacity': {
        'TableName': 'string',
        'CapacityUnits': 123.0,
        'ReadCapacityUnits': 123.0,
        'WriteCapacityUnits': 123.0,
        'Table': {
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'CapacityUnits': 123.0
        },
        'LocalSecondaryIndexes': {
            'string': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            }
        },
        'GlobalSecondaryIndexes': {
            'string': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            }
        }
    }
}


Response Structure

(dict) --
Represents the output of a GetItem operation.

Item (dict) --
A map of attribute names to AttributeValue objects, as specified by ProjectionExpression .

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true








ConsumedCapacity (dict) --
The capacity units consumed by the GetItem operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. ConsumedCapacity is only returned if the ReturnConsumedCapacity parameter was specified. For more information, see Read/Write Capacity Mode in the Amazon DynamoDB Developer Guide .

TableName (string) --
The name of the table that was affected by the operation.

CapacityUnits (float) --
The total number of capacity units consumed by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed by the operation.

WriteCapacityUnits (float) --
The total number of write capacity units consumed by the operation.

Table (dict) --
The amount of throughput consumed on the table affected by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.



LocalSecondaryIndexes (dict) --
The amount of throughput consumed on each local index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.







GlobalSecondaryIndexes (dict) --
The amount of throughput consumed on each global index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.















Exceptions

DynamoDB.Client.exceptions.ProvisionedThroughputExceededException
DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.RequestLimitExceeded
DynamoDB.Client.exceptions.InternalServerError

Examples
This example retrieves an item from the Music table. The table has a partition key and a sort key (Artist and SongTitle), so you must specify both of these attributes.
response = client.get_item(
    Key={
        'Artist': {
            'S': 'Acme Band',
        },
        'SongTitle': {
            'S': 'Happy Day',
        },
    },
    TableName='Music',
)

print(response)


Expected Output:
{
    'Item': {
        'AlbumTitle': {
            'S': 'Songs About Life',
        },
        'Artist': {
            'S': 'Acme Band',
        },
        'SongTitle': {
            'S': 'Happy Day',
        },
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Item': {
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        'ConsumedCapacity': {
            'TableName': 'string',
            'CapacityUnits': 123.0,
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'Table': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            },
            'LocalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            },
            'GlobalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            }
        }
    }
    
    
    :returns: 
    (string) --
    
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

def list_backups(TableName=None, Limit=None, TimeRangeLowerBound=None, TimeRangeUpperBound=None, ExclusiveStartBackupArn=None, BackupType=None):
    """
    List backups associated with an AWS account. To list backups for a given table, specify TableName . ListBackups returns a paginated list of results with at most 1 MB worth of items in a page. You can also specify a limit for the maximum number of entries to be returned in a page.
    In the request, start time is inclusive, but end time is exclusive. Note that these limits are for the time at which the original backup was requested.
    You can call ListBackups a maximum of five times per second.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_backups(
        TableName='string',
        Limit=123,
        TimeRangeLowerBound=datetime(2015, 1, 1),
        TimeRangeUpperBound=datetime(2015, 1, 1),
        ExclusiveStartBackupArn='string',
        BackupType='USER'|'SYSTEM'|'AWS_BACKUP'|'ALL'
    )
    
    
    :type TableName: string
    :param TableName: The backups from the table specified by TableName are listed.

    :type Limit: integer
    :param Limit: Maximum number of backups to return at once.

    :type TimeRangeLowerBound: datetime
    :param TimeRangeLowerBound: Only backups created after this time are listed. TimeRangeLowerBound is inclusive.

    :type TimeRangeUpperBound: datetime
    :param TimeRangeUpperBound: Only backups created before this time are listed. TimeRangeUpperBound is exclusive.

    :type ExclusiveStartBackupArn: string
    :param ExclusiveStartBackupArn: LastEvaluatedBackupArn is the Amazon Resource Name (ARN) of the backup last evaluated when the current page of results was returned, inclusive of the current page of results. This value may be specified as the ExclusiveStartBackupArn of a new ListBackups operation in order to fetch the next page of results.

    :type BackupType: string
    :param BackupType: The backups from the table specified by BackupType are listed.\nWhere BackupType can be:\n\nUSER - On-demand backup created by you.\nSYSTEM - On-demand backup automatically created by DynamoDB.\nALL - All types of on-demand backups (USER and SYSTEM).\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'BackupSummaries': [
        {
            'TableName': 'string',
            'TableId': 'string',
            'TableArn': 'string',
            'BackupArn': 'string',
            'BackupName': 'string',
            'BackupCreationDateTime': datetime(2015, 1, 1),
            'BackupExpiryDateTime': datetime(2015, 1, 1),
            'BackupStatus': 'CREATING'|'DELETED'|'AVAILABLE',
            'BackupType': 'USER'|'SYSTEM'|'AWS_BACKUP',
            'BackupSizeBytes': 123
        },
    ],
    'LastEvaluatedBackupArn': 'string'
}


Response Structure

(dict) --

BackupSummaries (list) --
List of BackupSummary objects.

(dict) --
Contains details for the backup.

TableName (string) --
Name of the table.

TableId (string) --
Unique identifier for the table.

TableArn (string) --
ARN associated with the table.

BackupArn (string) --
ARN associated with the backup.

BackupName (string) --
Name of the specified backup.

BackupCreationDateTime (datetime) --
Time at which the backup was created.

BackupExpiryDateTime (datetime) --
Time at which the automatic on-demand backup created by DynamoDB will expire. This SYSTEM on-demand backup expires automatically 35 days after its creation.

BackupStatus (string) --
Backup can be in one of the following states: CREATING, ACTIVE, DELETED.

BackupType (string) --
BackupType:

USER - You create and manage these using the on-demand backup feature.
SYSTEM - If you delete a table with point-in-time recovery enabled, a SYSTEM backup is automatically created and is retained for 35 days (at no additional cost). System backups allow you to restore the deleted table to the state it was in just before the point of deletion.
AWS_BACKUP - On-demand backup created by you from AWS Backup service.


BackupSizeBytes (integer) --
Size of the backup in bytes.





LastEvaluatedBackupArn (string) --
The ARN of the backup last evaluated when the current page of results was returned, inclusive of the current page of results. This value may be specified as the ExclusiveStartBackupArn of a new ListBackups operation in order to fetch the next page of results.
If LastEvaluatedBackupArn is empty, then the last page of results has been processed and there are no more results to be retrieved.
If LastEvaluatedBackupArn is not empty, this may or may not indicate that there is more data to be returned. All results are guaranteed to have been returned if and only if no value for LastEvaluatedBackupArn is returned.







Exceptions

DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'BackupSummaries': [
            {
                'TableName': 'string',
                'TableId': 'string',
                'TableArn': 'string',
                'BackupArn': 'string',
                'BackupName': 'string',
                'BackupCreationDateTime': datetime(2015, 1, 1),
                'BackupExpiryDateTime': datetime(2015, 1, 1),
                'BackupStatus': 'CREATING'|'DELETED'|'AVAILABLE',
                'BackupType': 'USER'|'SYSTEM'|'AWS_BACKUP',
                'BackupSizeBytes': 123
            },
        ],
        'LastEvaluatedBackupArn': 'string'
    }
    
    
    :returns: 
    USER - You create and manage these using the on-demand backup feature.
    SYSTEM - If you delete a table with point-in-time recovery enabled, a SYSTEM backup is automatically created and is retained for 35 days (at no additional cost). System backups allow you to restore the deleted table to the state it was in just before the point of deletion.
    AWS_BACKUP - On-demand backup created by you from AWS Backup service.
    
    """
    pass

def list_contributor_insights(TableName=None, NextToken=None, MaxResults=None):
    """
    Returns a list of ContributorInsightsSummary for a table and all its global secondary indexes.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_contributor_insights(
        TableName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type TableName: string
    :param TableName: The name of the table.

    :type NextToken: string
    :param NextToken: A token to for the desired page, if there is one.

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'ContributorInsightsSummaries': [
        {
            'TableName': 'string',
            'IndexName': 'string',
            'ContributorInsightsStatus': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'FAILED'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ContributorInsightsSummaries (list) --
A list of ContributorInsightsSummary.

(dict) --
Represents a Contributor Insights summary entry..

TableName (string) --
Name of the table associated with the summary.

IndexName (string) --
Name of the index associated with the summary, if any.

ContributorInsightsStatus (string) --
Describes the current status for contributor insights for the given table and index, if applicable.





NextToken (string) --
A token to go to the next page if there is one.







Exceptions

DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'ContributorInsightsSummaries': [
            {
                'TableName': 'string',
                'IndexName': 'string',
                'ContributorInsightsStatus': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'FAILED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DynamoDB.Client.exceptions.ResourceNotFoundException
    DynamoDB.Client.exceptions.InternalServerError
    
    """
    pass

def list_global_tables(ExclusiveStartGlobalTableName=None, Limit=None, RegionName=None):
    """
    Lists all global tables that have a replica in the specified Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_global_tables(
        ExclusiveStartGlobalTableName='string',
        Limit=123,
        RegionName='string'
    )
    
    
    :type ExclusiveStartGlobalTableName: string
    :param ExclusiveStartGlobalTableName: The first global table name that this operation will evaluate.

    :type Limit: integer
    :param Limit: The maximum number of table names to return, if the parameter is not specified DynamoDB defaults to 100.\nIf the number of global tables DynamoDB finds reaches this limit, it stops the operation and returns the table names collected up to that point, with a table name in the LastEvaluatedGlobalTableName to apply in a subsequent operation to the ExclusiveStartGlobalTableName parameter.\n

    :type RegionName: string
    :param RegionName: Lists the global tables in a specific Region.

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalTables': [
        {
            'GlobalTableName': 'string',
            'ReplicationGroup': [
                {
                    'RegionName': 'string'
                },
            ]
        },
    ],
    'LastEvaluatedGlobalTableName': 'string'
}


Response Structure

(dict) --

GlobalTables (list) --
List of global table names.

(dict) --
Represents the properties of a global table.

GlobalTableName (string) --
The global table name.

ReplicationGroup (list) --
The Regions where the global table has replicas.

(dict) --
Represents the properties of a replica.

RegionName (string) --
The Region where the replica needs to be created.









LastEvaluatedGlobalTableName (string) --
Last evaluated global table name.







Exceptions

DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'GlobalTables': [
            {
                'GlobalTableName': 'string',
                'ReplicationGroup': [
                    {
                        'RegionName': 'string'
                    },
                ]
            },
        ],
        'LastEvaluatedGlobalTableName': 'string'
    }
    
    
    :returns: 
    DynamoDB.Client.exceptions.InternalServerError
    
    """
    pass

def list_tables(ExclusiveStartTableName=None, Limit=None):
    """
    Returns an array of table names associated with the current account and endpoint. The output from ListTables is paginated, with each page returning a maximum of 100 table names.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example lists all of the tables associated with the current AWS account and endpoint.
    Expected Output:
    
    :example: response = client.list_tables(
        ExclusiveStartTableName='string',
        Limit=123
    )
    
    
    :type ExclusiveStartTableName: string
    :param ExclusiveStartTableName: The first table name that this operation will evaluate. Use the value that was returned for LastEvaluatedTableName in a previous operation, so that you can obtain the next page of results.

    :type Limit: integer
    :param Limit: A maximum number of table names to return. If this parameter is not specified, the limit is 100.

    :rtype: dict

ReturnsResponse Syntax
{
    'TableNames': [
        'string',
    ],
    'LastEvaluatedTableName': 'string'
}


Response Structure

(dict) --
Represents the output of a ListTables operation.

TableNames (list) --
The names of the tables associated with the current account at the current endpoint. The maximum size of this array is 100.
If LastEvaluatedTableName also appears in the output, you can use this value as the ExclusiveStartTableName parameter in a subsequent ListTables request and obtain the next page of results.

(string) --


LastEvaluatedTableName (string) --
The name of the last table in the current page of results. Use this value as the ExclusiveStartTableName in a new request to obtain the next page of results, until all the table names are returned.
If you do not receive a LastEvaluatedTableName value in the response, this means that there are no more table names to be retrieved.







Exceptions

DynamoDB.Client.exceptions.InternalServerError

Examples
This example lists all of the tables associated with the current AWS account and endpoint.
response = client.list_tables(
)

print(response)


Expected Output:
{
    'TableNames': [
        'Forum',
        'ProductCatalog',
        'Reply',
        'Thread',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TableNames': [
            'string',
        ],
        'LastEvaluatedTableName': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_of_resource(ResourceArn=None, NextToken=None):
    """
    List all tags on an Amazon DynamoDB resource. You can call ListTagsOfResource up to 10 times per second, per account.
    For an overview on tagging DynamoDB resources, see Tagging for DynamoDB in the Amazon DynamoDB Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_of_resource(
        ResourceArn='string',
        NextToken='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon DynamoDB resource with tags to be listed. This value is an Amazon Resource Name (ARN).\n

    :type NextToken: string
    :param NextToken: An optional string that, if supplied, must be copied from the output of a previous call to ListTagOfResource. When provided in this manner, this API fetches the next page of results.

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
The tags currently associated with the Amazon DynamoDB resource.

(dict) --
Describes a tag. A tag is a key-value pair. You can add up to 50 tags to a single DynamoDB table.
AWS-assigned tag names and values are automatically assigned the aws: prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix user: in the Cost Allocation Report. You cannot backdate the application of a tag.
For an overview on tagging DynamoDB resources, see Tagging for DynamoDB in the Amazon DynamoDB Developer Guide .

Key (string) --
The key of the tag. Tag keys are case sensitive. Each DynamoDB table can only have up to one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.

Value (string) --
The value of the tag. Tag values are case-sensitive and can be null.





NextToken (string) --
If this value is returned, there are additional results to be displayed. To retrieve them, call ListTagsOfResource again, with NextToken set to this value.







Exceptions

DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.InternalServerError


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
    DynamoDB.Client.exceptions.ResourceNotFoundException
    DynamoDB.Client.exceptions.InternalServerError
    
    """
    pass

def put_item(TableName=None, Item=None, Expected=None, ReturnValues=None, ReturnConsumedCapacity=None, ReturnItemCollectionMetrics=None, ConditionalOperator=None, ConditionExpression=None, ExpressionAttributeNames=None, ExpressionAttributeValues=None):
    """
    Creates a new item, or replaces an old item with a new item. If an item that has the same primary key as the new item already exists in the specified table, the new item completely replaces the existing item. You can perform a conditional put operation (add a new item if one with the specified primary key doesn\'t exist), or replace an existing item if it has certain attribute values. You can return the item\'s attribute values in the same operation, using the ReturnValues parameter.
    When you add an item, the primary key attributes are the only required attributes. Attribute values cannot be null.
    Empty String and Binary attribute values are allowed. Attribute values of type String and Binary must have a length greater than zero if the attribute is used as a key attribute for a table or index. Set type attributes cannot be empty.
    Invalid Requests with empty values will be rejected with a ValidationException exception.
    For more information about PutItem , see Working with Items in the Amazon DynamoDB Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example adds a new item to the Music table.
    Expected Output:
    
    :example: response = client.put_item(
        TableName='string',
        Item={
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        Expected={
            'string': {
                'Value': {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                },
                'Exists': True|False,
                'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH',
                'AttributeValueList': [
                    {
                        'S': 'string',
                        'N': 'string',
                        'B': b'bytes',
                        'SS': [
                            'string',
                        ],
                        'NS': [
                            'string',
                        ],
                        'BS': [
                            b'bytes',
                        ],
                        'M': {
                            'string': {'... recursive ...'}
                        },
                        'L': [
                            {'... recursive ...'},
                        ],
                        'NULL': True|False,
                        'BOOL': True|False
                    },
                ]
            }
        },
        ReturnValues='NONE'|'ALL_OLD'|'UPDATED_OLD'|'ALL_NEW'|'UPDATED_NEW',
        ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
        ReturnItemCollectionMetrics='SIZE'|'NONE',
        ConditionalOperator='AND'|'OR',
        ConditionExpression='string',
        ExpressionAttributeNames={
            'string': 'string'
        },
        ExpressionAttributeValues={
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        }
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table to contain the item.\n

    :type Item: dict
    :param Item: [REQUIRED]\nA map of attribute name/value pairs, one for each attribute. Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.\nYou must provide all of the attributes for the primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide both values for both the partition key and the sort key.\nIf you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table\'s attribute definition.\nEmpty String and Binary attribute values are allowed. Attribute values of type String and Binary must have a length greater than zero if the attribute is used as a key attribute for a table or index.\nFor more information about primary keys, see Primary Key in the Amazon DynamoDB Developer Guide .\nEach element in the Item map is an AttributeValue object.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n

    :type Expected: dict
    :param Expected: This is a legacy parameter. Use ConditionExpression instead. For more information, see Expected in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(dict) --Represents a condition to be compared with an attribute value. This condition can be used with DeleteItem , PutItem , or UpdateItem operations; if the comparison evaluates to true, the operation succeeds; if not, the operation fails. You can use ExpectedAttributeValue in one of two different ways:\n\nUse AttributeValueList to specify one or more values to compare against an attribute. Use ComparisonOperator to specify how you want to perform the comparison. If the comparison evaluates to true, then the conditional operation succeeds.\nUse Value to specify a value that DynamoDB will compare against an attribute. If the values match, then ExpectedAttributeValue evaluates to true and the conditional operation succeeds. Optionally, you can also set Exists to false, indicating that you do not expect to find the attribute value in the table. In this case, the conditional operation succeeds only if the comparison evaluates to false.\n\n\nValue and Exists are incompatible with AttributeValueList and ComparisonOperator . Note that if you use both sets of parameters at once, DynamoDB will return a ValidationException exception.\n\nValue (dict) --Represents the data for the expected attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\nExists (boolean) --Causes DynamoDB to evaluate the value before attempting a conditional operation:\n\nIf Exists is true , DynamoDB will check to see if that attribute value already exists in the table. If it is found, then the operation succeeds. If it is not found, the operation fails with a ConditionCheckFailedException .\nIf Exists is false , DynamoDB assumes that the attribute value does not exist in the table. If in fact the value does not exist, then the assumption is valid and the operation succeeds. If the value is found, despite the assumption that it does not exist, the operation fails with a ConditionCheckFailedException .\n\nThe default setting for Exists is true . If you supply a Value all by itself, DynamoDB assumes the attribute exists: You don\'t have to set Exists to true , because it is implied.\nDynamoDB returns a ValidationException if:\n\nExists is true but there is no Value to check. (You expect a value to exist, but don\'t specify what that value is.)\nExists is false but you also provide a Value . (You cannot expect an attribute to have a value, while also expecting it not to exist.)\n\n\nComparisonOperator (string) --A comparator for evaluating attributes in the AttributeValueList . For example, equals, greater than, less than, etc.\nThe following comparison operators are available:\n\nEQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS | NOT_CONTAINS | BEGINS_WITH | IN | BETWEEN\nThe following are descriptions of each comparison operator.\n\nEQ : Equal. EQ is supported for all data types, including lists and maps. AttributeValueList can contain only one AttributeValue element of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not equal {'NS':['6', '2', '1']} .\nNE : Not equal. NE is supported for all data types, including lists and maps. AttributeValueList can contain only one AttributeValue of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an AttributeValue of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not equal {'NS':['6', '2', '1']} .\nLE : Less than or equal.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nLT : Less than.  AttributeValueList can contain only one AttributeValue of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nGE : Greater than or equal.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nGT : Greater than.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nNOT_NULL : The attribute exists. NOT_NULL is supported for all data types, including lists and maps.\n\n\nNote\nThis operator tests for the existence of an attribute, not its data type. If the data type of attribute 'a ' is null, and you evaluate it using NOT_NULL , the result is a Boolean true . This result is because the attribute 'a ' exists; its data type is not relevant to the NOT_NULL comparison operator.\n\n\nNULL : The attribute does not exist. NULL is supported for all data types, including lists and maps.\n\n\nNote\nThis operator tests for the nonexistence of an attribute, not its data type. If the data type of attribute 'a ' is null, and you evaluate it using NULL , the result is a Boolean false . This is because the attribute 'a ' exists; its data type is not relevant to the NULL comparison operator.\n\n\nCONTAINS : Checks for a subsequence, or value in a set. AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is of type String, then the operator checks for a substring match. If the target attribute of the comparison is of type Binary, then the operator looks for a subsequence of the target that matches the input. If the target attribute of the comparison is a set ('SS ', 'NS ', or 'BS '), then the operator evaluates to true if it finds an exact match with any member of the set. CONTAINS is supported for lists: When evaluating 'a CONTAINS b ', 'a ' can be a list; however, 'b ' cannot be a set, a map, or a list.\nNOT_CONTAINS : Checks for absence of a subsequence, or absence of a value in a set. AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is a String, then the operator checks for the absence of a substring match. If the target attribute of the comparison is Binary, then the operator checks for the absence of a subsequence of the target that matches the input. If the target attribute of the comparison is a set ('SS ', 'NS ', or 'BS '), then the operator evaluates to true if it does not find an exact match with any member of the set. NOT_CONTAINS is supported for lists: When evaluating 'a NOT CONTAINS b ', 'a ' can be a list; however, 'b ' cannot be a set, a map, or a list.\nBEGINS_WITH : Checks for a prefix.  AttributeValueList can contain only one AttributeValue of type String or Binary (not a Number or a set type). The target attribute of the comparison must be of type String or Binary (not a Number or a set type).\nIN : Checks for matching elements in a list. AttributeValueList can contain one or more AttributeValue elements of type String, Number, or Binary. These attributes are compared against an existing attribute of an item. If any elements of the input are equal to the item attribute, the expression evaluates to true.\nBETWEEN : Greater than or equal to the first value, and less than or equal to the second value.  AttributeValueList must contain two AttributeValue elements of the same type, either String, Number, or Binary (not a set type). A target attribute matches if the target value is greater than, or equal to, the first element and less than, or equal to, the second element. If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not compare to {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']}\n\n\nAttributeValueList (list) --One or more values to evaluate against the supplied attribute. The number of values in the list depends on the ComparisonOperator being used.\nFor type Number, value comparisons are numeric.\nString value comparisons for greater than, equals, or less than are based on ASCII character code values. For example, a is greater than A , and a is greater than B . For a list of code values, see http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters .\nFor Binary, DynamoDB treats each byte of the binary data as unsigned when it compares binary values.\nFor information on specifying data types in JSON, see JSON Data Format in the Amazon DynamoDB Developer Guide .\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\n\n\n\n

    :type ReturnValues: string
    :param ReturnValues: Use ReturnValues if you want to get the item attributes as they appeared before they were updated with the PutItem request. For PutItem , the valid values are:\n\nNONE - If ReturnValues is not specified, or if its value is NONE , then nothing is returned. (This setting is the default for ReturnValues .)\nALL_OLD - If PutItem overwrote an attribute name-value pair, then the content of the old item is returned.\n\n\nNote\nThe ReturnValues parameter is used by several DynamoDB operations; however, PutItem does not recognize any values other than NONE or ALL_OLD .\n\n

    :type ReturnConsumedCapacity: string
    :param ReturnConsumedCapacity: Determines the level of detail about provisioned throughput consumption that is returned in the response:\n\nINDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem , do not access any indexes at all. In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s).\nTOTAL - The response includes only the aggregate ConsumedCapacity for the operation.\nNONE - No ConsumedCapacity details are included in the response.\n\n

    :type ReturnItemCollectionMetrics: string
    :param ReturnItemCollectionMetrics: Determines whether item collection metrics are returned. If set to SIZE , the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.

    :type ConditionalOperator: string
    :param ConditionalOperator: This is a legacy parameter. Use ConditionExpression instead. For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide .

    :type ConditionExpression: string
    :param ConditionExpression: A condition that must be satisfied in order for a conditional PutItem operation to succeed.\nAn expression can contain any of the following:\n\nFunctions: attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size  These function names are case-sensitive.\nComparison operators: = | <> | < | > | <= | >= | BETWEEN | IN\nLogical operators: AND | OR | NOT\n\nFor more information on condition expressions, see Condition Expressions in the Amazon DynamoDB Developer Guide .\n

    :type ExpressionAttributeNames: dict
    :param ExpressionAttributeNames: One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames :\n\nTo access an attribute whose name conflicts with a DynamoDB reserved word.\nTo create a placeholder for repeating occurrences of an attribute name in an expression.\nTo prevent special characters in an attribute name from being misinterpreted in an expression.\n\nUse the # character in an expression to dereference an attribute name. For example, consider the following attribute name:\n\nPercentile\n\nThe name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide ). To work around this, you could specify the following for ExpressionAttributeNames :\n\n{'#P':'Percentile'}\n\nYou could then use this substitution in an expression, as in this example:\n\n#P = :val\n\n\nNote\nTokens that begin with the : character are expression attribute values , which are placeholders for the actual value at runtime.\n\nFor more information on expression attribute names, see Specifying Item Attributes in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type ExpressionAttributeValues: dict
    :param ExpressionAttributeValues: One or more values that can be substituted in an expression.\nUse the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:\n\nAvailable | Backordered | Discontinued\nYou would first need to specify ExpressionAttributeValues as follows:\n\n{ ':avail':{'S':'Available'}, ':back':{'S':'Backordered'}, ':disc':{'S':'Discontinued'} }\nYou could then use these values in an expression, such as this:\n\nProductStatus IN (:avail, :back, :disc)\nFor more information on expression attribute values, see Condition Expressions in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Attributes': {
        'string': {
            'S': 'string',
            'N': 'string',
            'B': b'bytes',
            'SS': [
                'string',
            ],
            'NS': [
                'string',
            ],
            'BS': [
                b'bytes',
            ],
            'M': {
                'string': {'... recursive ...'}
            },
            'L': [
                {'... recursive ...'},
            ],
            'NULL': True|False,
            'BOOL': True|False
        }
    },
    'ConsumedCapacity': {
        'TableName': 'string',
        'CapacityUnits': 123.0,
        'ReadCapacityUnits': 123.0,
        'WriteCapacityUnits': 123.0,
        'Table': {
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'CapacityUnits': 123.0
        },
        'LocalSecondaryIndexes': {
            'string': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            }
        },
        'GlobalSecondaryIndexes': {
            'string': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            }
        }
    },
    'ItemCollectionMetrics': {
        'ItemCollectionKey': {
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        'SizeEstimateRangeGB': [
            123.0,
        ]
    }
}


Response Structure

(dict) --
Represents the output of a PutItem operation.

Attributes (dict) --
The attribute values as they appeared before the PutItem operation, but only if ReturnValues is specified as ALL_OLD in the request. Each element consists of an attribute name and an attribute value.

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true








ConsumedCapacity (dict) --
The capacity units consumed by the PutItem operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. ConsumedCapacity is only returned if the ReturnConsumedCapacity parameter was specified. For more information, see Read/Write Capacity Mode in the Amazon DynamoDB Developer Guide .

TableName (string) --
The name of the table that was affected by the operation.

CapacityUnits (float) --
The total number of capacity units consumed by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed by the operation.

WriteCapacityUnits (float) --
The total number of write capacity units consumed by the operation.

Table (dict) --
The amount of throughput consumed on the table affected by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.



LocalSecondaryIndexes (dict) --
The amount of throughput consumed on each local index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.







GlobalSecondaryIndexes (dict) --
The amount of throughput consumed on each global index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.









ItemCollectionMetrics (dict) --
Information about item collections, if any, that were affected by the PutItem operation. ItemCollectionMetrics is only returned if the ReturnItemCollectionMetrics parameter was specified. If the table does not have any local secondary indexes, this information is not returned in the response.
Each ItemCollectionMetrics element consists of:

ItemCollectionKey - The partition key value of the item collection. This is the same as the partition key value of the item itself.
SizeEstimateRangeGB - An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit. The estimate is subject to change over time; therefore, do not rely on the precision or accuracy of the estimate.


ItemCollectionKey (dict) --
The partition key value of the item collection. This value is the same as the partition key value of the item.

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true








SizeEstimateRangeGB (list) --
An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit.
The estimate is subject to change over time; therefore, do not rely on the precision or accuracy of the estimate.

(float) --










Exceptions

DynamoDB.Client.exceptions.ConditionalCheckFailedException
DynamoDB.Client.exceptions.ProvisionedThroughputExceededException
DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.ItemCollectionSizeLimitExceededException
DynamoDB.Client.exceptions.TransactionConflictException
DynamoDB.Client.exceptions.RequestLimitExceeded
DynamoDB.Client.exceptions.InternalServerError

Examples
This example adds a new item to the Music table.
response = client.put_item(
    Item={
        'AlbumTitle': {
            'S': 'Somewhat Famous',
        },
        'Artist': {
            'S': 'No One You Know',
        },
        'SongTitle': {
            'S': 'Call Me Today',
        },
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='Music',
)

print(response)


Expected Output:
{
    'ConsumedCapacity': {
        'CapacityUnits': 1,
        'TableName': 'Music',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Attributes': {
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        'ConsumedCapacity': {
            'TableName': 'string',
            'CapacityUnits': 123.0,
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'Table': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            },
            'LocalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            },
            'GlobalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            }
        },
        'ItemCollectionMetrics': {
            'ItemCollectionKey': {
                'string': {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                }
            },
            'SizeEstimateRangeGB': [
                123.0,
            ]
        }
    }
    
    
    :returns: 
    TableName (string) -- [REQUIRED]
    The name of the table to contain the item.
    
    Item (dict) -- [REQUIRED]
    A map of attribute name/value pairs, one for each attribute. Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.
    You must provide all of the attributes for the primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide both values for both the partition key and the sort key.
    If you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table\'s attribute definition.
    Empty String and Binary attribute values are allowed. Attribute values of type String and Binary must have a length greater than zero if the attribute is used as a key attribute for a table or index.
    For more information about primary keys, see Primary Key in the Amazon DynamoDB Developer Guide .
    Each element in the Item map is an AttributeValue object.
    
    (string) --
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    S (string) --An attribute of type String. For example:
    
    "S": "Hello"
    
    N (string) --An attribute of type Number. For example:
    
    "N": "123.45"
    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
    
    B (bytes) --An attribute of type Binary. For example:
    
    "B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"
    
    SS (list) --An attribute of type String Set. For example:
    
    "SS": ["Giraffe", "Hippo" ,"Zebra"]
    
    (string) --
    
    
    NS (list) --An attribute of type Number Set. For example:
    
    "NS": ["42.2", "-19", "7.5", "3.14"]
    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
    
    (string) --
    
    
    BS (list) --An attribute of type Binary Set. For example:
    
    "BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]
    
    (bytes) --
    
    
    M (dict) --An attribute of type Map. For example:
    
    "M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}
    
    (string) --
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    
    
    
    
    L (list) --An attribute of type List. For example:
    
    "L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]
    
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    
    
    NULL (boolean) --An attribute of type Null. For example:
    
    "NULL": true
    
    BOOL (boolean) --An attribute of type Boolean. For example:
    
    "BOOL": true
    
    
    
    
    
    
    
    Expected (dict) -- This is a legacy parameter. Use ConditionExpression instead. For more information, see Expected in the Amazon DynamoDB Developer Guide .
    
    (string) --
    (dict) --Represents a condition to be compared with an attribute value. This condition can be used with DeleteItem , PutItem , or UpdateItem operations; if the comparison evaluates to true, the operation succeeds; if not, the operation fails. You can use ExpectedAttributeValue in one of two different ways:
    
    Use AttributeValueList to specify one or more values to compare against an attribute. Use ComparisonOperator to specify how you want to perform the comparison. If the comparison evaluates to true, then the conditional operation succeeds.
    Use Value to specify a value that DynamoDB will compare against an attribute. If the values match, then ExpectedAttributeValue evaluates to true and the conditional operation succeeds. Optionally, you can also set Exists to false, indicating that you do not expect to find the attribute value in the table. In this case, the conditional operation succeeds only if the comparison evaluates to false.
    
    
    Value and Exists are incompatible with AttributeValueList and ComparisonOperator . Note that if you use both sets of parameters at once, DynamoDB will return a ValidationException exception.
    
    Value (dict) --Represents the data for the expected attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    S (string) --An attribute of type String. For example:
    
    "S": "Hello"
    
    N (string) --An attribute of type Number. For example:
    
    "N": "123.45"
    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
    
    B (bytes) --An attribute of type Binary. For example:
    
    "B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"
    
    SS (list) --An attribute of type String Set. For example:
    
    "SS": ["Giraffe", "Hippo" ,"Zebra"]
    
    (string) --
    
    
    NS (list) --An attribute of type Number Set. For example:
    
    "NS": ["42.2", "-19", "7.5", "3.14"]
    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
    
    (string) --
    
    
    BS (list) --An attribute of type Binary Set. For example:
    
    "BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]
    
    (bytes) --
    
    
    M (dict) --An attribute of type Map. For example:
    
    "M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}
    
    (string) --
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    
    
    
    
    L (list) --An attribute of type List. For example:
    
    "L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]
    
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    
    
    NULL (boolean) --An attribute of type Null. For example:
    
    "NULL": true
    
    BOOL (boolean) --An attribute of type Boolean. For example:
    
    "BOOL": true
    
    
    
    Exists (boolean) --Causes DynamoDB to evaluate the value before attempting a conditional operation:
    
    If Exists is true , DynamoDB will check to see if that attribute value already exists in the table. If it is found, then the operation succeeds. If it is not found, the operation fails with a ConditionCheckFailedException .
    If Exists is false , DynamoDB assumes that the attribute value does not exist in the table. If in fact the value does not exist, then the assumption is valid and the operation succeeds. If the value is found, despite the assumption that it does not exist, the operation fails with a ConditionCheckFailedException .
    
    The default setting for Exists is true . If you supply a Value all by itself, DynamoDB assumes the attribute exists: You don\'t have to set Exists to true , because it is implied.
    DynamoDB returns a ValidationException if:
    
    Exists is true but there is no Value to check. (You expect a value to exist, but don\'t specify what that value is.)
    Exists is false but you also provide a Value . (You cannot expect an attribute to have a value, while also expecting it not to exist.)
    
    
    ComparisonOperator (string) --A comparator for evaluating attributes in the AttributeValueList . For example, equals, greater than, less than, etc.
    The following comparison operators are available:
    
    EQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS | NOT_CONTAINS | BEGINS_WITH | IN | BETWEEN
    The following are descriptions of each comparison operator.
    
    EQ : Equal. EQ is supported for all data types, including lists and maps.  AttributeValueList can contain only one AttributeValue element of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {"S":"6"} does not equal {"N":"6"} . Also, {"N":"6"} does not equal {"NS":["6", "2", "1"]} .
    NE : Not equal. NE is supported for all data types, including lists and maps.  AttributeValueList can contain only one AttributeValue of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an AttributeValue of a different type than the one provided in the request, the value does not match. For example, {"S":"6"} does not equal {"N":"6"} . Also, {"N":"6"} does not equal {"NS":["6", "2", "1"]} .
    LE : Less than or equal.   AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {"S":"6"} does not equal {"N":"6"} . Also, {"N":"6"} does not compare to {"NS":["6", "2", "1"]} .
    LT : Less than.   AttributeValueList can contain only one AttributeValue of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {"S":"6"} does not equal {"N":"6"} . Also, {"N":"6"} does not compare to {"NS":["6", "2", "1"]} .
    GE : Greater than or equal.   AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {"S":"6"} does not equal {"N":"6"} . Also, {"N":"6"} does not compare to {"NS":["6", "2", "1"]} .
    GT : Greater than.   AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {"S":"6"} does not equal {"N":"6"} . Also, {"N":"6"} does not compare to {"NS":["6", "2", "1"]} .
    NOT_NULL : The attribute exists. NOT_NULL is supported for all data types, including lists and maps.
    
    
    Note
    This operator tests for the existence of an attribute, not its data type. If the data type of attribute "a " is null, and you evaluate it using NOT_NULL , the result is a Boolean true . This result is because the attribute "a " exists; its data type is not relevant to the NOT_NULL comparison operator.
    
    
    NULL : The attribute does not exist. NULL is supported for all data types, including lists and maps.
    
    
    Note
    This operator tests for the nonexistence of an attribute, not its data type. If the data type of attribute "a " is null, and you evaluate it using NULL , the result is a Boolean false . This is because the attribute "a " exists; its data type is not relevant to the NULL comparison operator.
    
    
    CONTAINS : Checks for a subsequence, or value in a set.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is of type String, then the operator checks for a substring match. If the target attribute of the comparison is of type Binary, then the operator looks for a subsequence of the target that matches the input. If the target attribute of the comparison is a set ("SS ", "NS ", or "BS "), then the operator evaluates to true if it finds an exact match with any member of the set. CONTAINS is supported for lists: When evaluating "a CONTAINS b ", "a " can be a list; however, "b " cannot be a set, a map, or a list.
    NOT_CONTAINS : Checks for absence of a subsequence, or absence of a value in a set.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is a String, then the operator checks for the absence of a substring match. If the target attribute of the comparison is Binary, then the operator checks for the absence of a subsequence of the target that matches the input. If the target attribute of the comparison is a set ("SS ", "NS ", or "BS "), then the operator evaluates to true if it does not find an exact match with any member of the set. NOT_CONTAINS is supported for lists: When evaluating "a NOT CONTAINS b ", "a " can be a list; however, "b " cannot be a set, a map, or a list.
    BEGINS_WITH : Checks for a prefix.   AttributeValueList can contain only one AttributeValue of type String or Binary (not a Number or a set type). The target attribute of the comparison must be of type String or Binary (not a Number or a set type).
    IN : Checks for matching elements in a list.  AttributeValueList can contain one or more AttributeValue elements of type String, Number, or Binary. These attributes are compared against an existing attribute of an item. If any elements of the input are equal to the item attribute, the expression evaluates to true.
    BETWEEN : Greater than or equal to the first value, and less than or equal to the second value.   AttributeValueList must contain two AttributeValue elements of the same type, either String, Number, or Binary (not a set type). A target attribute matches if the target value is greater than, or equal to, the first element and less than, or equal to, the second element. If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {"S":"6"} does not compare to {"N":"6"} . Also, {"N":"6"} does not compare to {"NS":["6", "2", "1"]}
    
    
    AttributeValueList (list) --One or more values to evaluate against the supplied attribute. The number of values in the list depends on the ComparisonOperator being used.
    For type Number, value comparisons are numeric.
    String value comparisons for greater than, equals, or less than are based on ASCII character code values. For example, a is greater than A , and a is greater than B . For a list of code values, see http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters .
    For Binary, DynamoDB treats each byte of the binary data as unsigned when it compares binary values.
    For information on specifying data types in JSON, see JSON Data Format in the Amazon DynamoDB Developer Guide .
    
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    S (string) --An attribute of type String. For example:
    
    "S": "Hello"
    
    N (string) --An attribute of type Number. For example:
    
    "N": "123.45"
    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
    
    B (bytes) --An attribute of type Binary. For example:
    
    "B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"
    
    SS (list) --An attribute of type String Set. For example:
    
    "SS": ["Giraffe", "Hippo" ,"Zebra"]
    
    (string) --
    
    
    NS (list) --An attribute of type Number Set. For example:
    
    "NS": ["42.2", "-19", "7.5", "3.14"]
    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
    
    (string) --
    
    
    BS (list) --An attribute of type Binary Set. For example:
    
    "BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]
    
    (bytes) --
    
    
    M (dict) --An attribute of type Map. For example:
    
    "M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}
    
    (string) --
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    
    
    
    
    L (list) --An attribute of type List. For example:
    
    "L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]
    
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    
    
    NULL (boolean) --An attribute of type Null. For example:
    
    "NULL": true
    
    BOOL (boolean) --An attribute of type Boolean. For example:
    
    "BOOL": true
    
    
    
    
    
    
    
    
    
    
    
    ReturnValues (string) -- Use ReturnValues if you want to get the item attributes as they appeared before they were updated with the PutItem request. For PutItem , the valid values are:
    
    NONE - If ReturnValues is not specified, or if its value is NONE , then nothing is returned. (This setting is the default for ReturnValues .)
    ALL_OLD - If PutItem overwrote an attribute name-value pair, then the content of the old item is returned.
    
    
    Note
    The ReturnValues parameter is used by several DynamoDB operations; however, PutItem does not recognize any values other than NONE or ALL_OLD .
    
    
    ReturnConsumedCapacity (string) -- Determines the level of detail about provisioned throughput consumption that is returned in the response:
    
    INDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem , do not access any indexes at all. In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s).
    TOTAL - The response includes only the aggregate ConsumedCapacity for the operation.
    NONE - No ConsumedCapacity details are included in the response.
    
    
    ReturnItemCollectionMetrics (string) -- Determines whether item collection metrics are returned. If set to SIZE , the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.
    ConditionalOperator (string) -- This is a legacy parameter. Use ConditionExpression instead. For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide .
    ConditionExpression (string) -- A condition that must be satisfied in order for a conditional PutItem operation to succeed.
    An expression can contain any of the following:
    
    Functions: attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size   These function names are case-sensitive.
    Comparison operators: = | <> | < | > | <= | >= | BETWEEN | IN
    Logical operators: AND | OR | NOT
    
    For more information on condition expressions, see Condition Expressions in the Amazon DynamoDB Developer Guide .
    
    ExpressionAttributeNames (dict) -- One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames :
    
    To access an attribute whose name conflicts with a DynamoDB reserved word.
    To create a placeholder for repeating occurrences of an attribute name in an expression.
    To prevent special characters in an attribute name from being misinterpreted in an expression.
    
    Use the # character in an expression to dereference an attribute name. For example, consider the following attribute name:
    
    Percentile
    
    The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide ). To work around this, you could specify the following for ExpressionAttributeNames :
    
    {"#P":"Percentile"}
    
    You could then use this substitution in an expression, as in this example:
    
    #P = :val
    
    
    Note
    Tokens that begin with the : character are expression attribute values , which are placeholders for the actual value at runtime.
    
    For more information on expression attribute names, see Specifying Item Attributes in the Amazon DynamoDB Developer Guide .
    
    (string) --
    (string) --
    
    
    
    
    ExpressionAttributeValues (dict) -- One or more values that can be substituted in an expression.
    Use the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:
    
    Available | Backordered | Discontinued
    You would first need to specify ExpressionAttributeValues as follows:
    
    { ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }
    You could then use these values in an expression, such as this:
    
    ProductStatus IN (:avail, :back, :disc)
    For more information on expression attribute values, see Condition Expressions in the Amazon DynamoDB Developer Guide .
    
    (string) --
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    S (string) --An attribute of type String. For example:
    
    "S": "Hello"
    
    N (string) --An attribute of type Number. For example:
    
    "N": "123.45"
    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
    
    B (bytes) --An attribute of type Binary. For example:
    
    "B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"
    
    SS (list) --An attribute of type String Set. For example:
    
    "SS": ["Giraffe", "Hippo" ,"Zebra"]
    
    (string) --
    
    
    NS (list) --An attribute of type Number Set. For example:
    
    "NS": ["42.2", "-19", "7.5", "3.14"]
    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
    
    (string) --
    
    
    BS (list) --An attribute of type Binary Set. For example:
    
    "BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]
    
    (bytes) --
    
    
    M (dict) --An attribute of type Map. For example:
    
    "M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}
    
    (string) --
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    
    
    
    
    L (list) --An attribute of type List. For example:
    
    "L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]
    
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    
    
    NULL (boolean) --An attribute of type Null. For example:
    
    "NULL": true
    
    BOOL (boolean) --An attribute of type Boolean. For example:
    
    "BOOL": true
    
    
    
    
    
    
    
    
    """
    pass

def query(TableName=None, IndexName=None, Select=None, AttributesToGet=None, Limit=None, ConsistentRead=None, KeyConditions=None, QueryFilter=None, ConditionalOperator=None, ScanIndexForward=None, ExclusiveStartKey=None, ReturnConsumedCapacity=None, ProjectionExpression=None, FilterExpression=None, KeyConditionExpression=None, ExpressionAttributeNames=None, ExpressionAttributeValues=None):
    """
    The Query operation finds items based on primary key values. You can query any table or secondary index that has a composite primary key (a partition key and a sort key).
    Use the KeyConditionExpression parameter to provide a specific value for the partition key. The Query operation will return all of the items from the table or index with that partition key value. You can optionally narrow the scope of the Query operation by specifying a sort key value and a comparison operator in KeyConditionExpression . To further refine the Query results, you can optionally provide a FilterExpression . A FilterExpression determines which items within the results should be returned to you. All of the other results are discarded.
    A Query operation always returns a result set. If no matching items are found, the result set will be empty. Queries that do not return results consume the minimum number of read capacity units for that type of read operation.
    A single Query operation will read up to the maximum number of items set (if using the Limit parameter) or a maximum of 1 MB of data and then apply any filtering to the results using FilterExpression . If LastEvaluatedKey is present in the response, you will need to paginate the result set. For more information, see Paginating the Results in the Amazon DynamoDB Developer Guide .
    You can query a table, a local secondary index, or a global secondary index. For a query on a table or on a local secondary index, you can set the ConsistentRead parameter to true and obtain a strongly consistent result. Global secondary indexes support eventually consistent reads only, so do not specify ConsistentRead when querying a global secondary index.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example queries items in the Music table. The table has a partition key and sort key (Artist and SongTitle), but this query only specifies the partition key value. It returns song titles by the artist named "No One You Know".
    Expected Output:
    
    :example: response = client.query(
        TableName='string',
        IndexName='string',
        Select='ALL_ATTRIBUTES'|'ALL_PROJECTED_ATTRIBUTES'|'SPECIFIC_ATTRIBUTES'|'COUNT',
        AttributesToGet=[
            'string',
        ],
        Limit=123,
        ConsistentRead=True|False,
        KeyConditions={
            'string': {
                'AttributeValueList': [
                    {
                        'S': 'string',
                        'N': 'string',
                        'B': b'bytes',
                        'SS': [
                            'string',
                        ],
                        'NS': [
                            'string',
                        ],
                        'BS': [
                            b'bytes',
                        ],
                        'M': {
                            'string': {'... recursive ...'}
                        },
                        'L': [
                            {'... recursive ...'},
                        ],
                        'NULL': True|False,
                        'BOOL': True|False
                    },
                ],
                'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH'
            }
        },
        QueryFilter={
            'string': {
                'AttributeValueList': [
                    {
                        'S': 'string',
                        'N': 'string',
                        'B': b'bytes',
                        'SS': [
                            'string',
                        ],
                        'NS': [
                            'string',
                        ],
                        'BS': [
                            b'bytes',
                        ],
                        'M': {
                            'string': {'... recursive ...'}
                        },
                        'L': [
                            {'... recursive ...'},
                        ],
                        'NULL': True|False,
                        'BOOL': True|False
                    },
                ],
                'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH'
            }
        },
        ConditionalOperator='AND'|'OR',
        ScanIndexForward=True|False,
        ExclusiveStartKey={
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
        ProjectionExpression='string',
        FilterExpression='string',
        KeyConditionExpression='string',
        ExpressionAttributeNames={
            'string': 'string'
        },
        ExpressionAttributeValues={
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        }
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table containing the requested items.\n

    :type IndexName: string
    :param IndexName: The name of an index to query. This index can be any local secondary index or global secondary index on the table. Note that if you use the IndexName parameter, you must also provide TableName.

    :type Select: string
    :param Select: The attributes to be returned in the result. You can retrieve all item attributes, specific item attributes, the count of matching items, or in the case of an index, some or all of the attributes projected into the index.\n\nALL_ATTRIBUTES - Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index, DynamoDB fetches the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required.\nALL_PROJECTED_ATTRIBUTES - Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying ALL_ATTRIBUTES .\nCOUNT - Returns the number of matching items, rather than the matching items themselves.\nSPECIFIC_ATTRIBUTES - Returns only the attributes listed in AttributesToGet . This return value is equivalent to specifying AttributesToGet without specifying any value for Select . If you query or scan a local secondary index and request only attributes that are projected into that index, the operation will read only the index and not the table. If any of the requested attributes are not projected into the local secondary index, DynamoDB fetches each of these attributes from the parent table. This extra fetching incurs additional throughput cost and latency. If you query or scan a global secondary index, you can only request attributes that are projected into the index. Global secondary index queries cannot fetch attributes from the parent table.\n\nIf neither Select nor AttributesToGet are specified, DynamoDB defaults to ALL_ATTRIBUTES when accessing a table, and ALL_PROJECTED_ATTRIBUTES when accessing an index. You cannot use both Select and AttributesToGet together in a single request, unless the value for Select is SPECIFIC_ATTRIBUTES . (This usage is equivalent to specifying AttributesToGet without any value for Select .)\n\nNote\nIf you use the ProjectionExpression parameter, then the value for Select can only be SPECIFIC_ATTRIBUTES . Any other value for Select will return an error.\n\n

    :type AttributesToGet: list
    :param AttributesToGet: This is a legacy parameter. Use ProjectionExpression instead. For more information, see AttributesToGet in the Amazon DynamoDB Developer Guide .\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of items to evaluate (not necessarily the number of matching items). If DynamoDB processes the number of items up to the limit while processing the results, it stops the operation and returns the matching values up to that point, and a key in LastEvaluatedKey to apply in a subsequent operation, so that you can pick up where you left off. Also, if the processed dataset size exceeds 1 MB before DynamoDB reaches this limit, it stops the operation and returns the matching values up to the limit, and a key in LastEvaluatedKey to apply in a subsequent operation to continue the operation. For more information, see Query and Scan in the Amazon DynamoDB Developer Guide .

    :type ConsistentRead: boolean
    :param ConsistentRead: Determines the read consistency model: If set to true , then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads.\nStrongly consistent reads are not supported on global secondary indexes. If you query a global secondary index with ConsistentRead set to true , you will receive a ValidationException .\n

    :type KeyConditions: dict
    :param KeyConditions: This is a legacy parameter. Use KeyConditionExpression instead. For more information, see KeyConditions in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(dict) --Represents the selection criteria for a Query or Scan operation:\n\nFor a Query operation, Condition is used for specifying the KeyConditions to use when querying a table or an index. For KeyConditions , only the following comparison operators are supported: EQ | LE | LT | GE | GT | BEGINS_WITH | BETWEEN Condition is also used in a QueryFilter , which evaluates the query results and returns only the desired values.\nFor a Scan operation, Condition is used in a ScanFilter , which evaluates the scan results and returns only the desired values.\n\n\nAttributeValueList (list) --One or more values to evaluate against the supplied attribute. The number of values in the list depends on the ComparisonOperator being used.\nFor type Number, value comparisons are numeric.\nString value comparisons for greater than, equals, or less than are based on ASCII character code values. For example, a is greater than A , and a is greater than B . For a list of code values, see http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters .\nFor Binary, DynamoDB treats each byte of the binary data as unsigned when it compares binary values.\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\nComparisonOperator (string) -- [REQUIRED]A comparator for evaluating attributes. For example, equals, greater than, less than, etc.\nThe following comparison operators are available:\n\nEQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS | NOT_CONTAINS | BEGINS_WITH | IN | BETWEEN\nThe following are descriptions of each comparison operator.\n\nEQ : Equal. EQ is supported for all data types, including lists and maps. AttributeValueList can contain only one AttributeValue element of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not equal {'NS':['6', '2', '1']} .\nNE : Not equal. NE is supported for all data types, including lists and maps. AttributeValueList can contain only one AttributeValue of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an AttributeValue of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not equal {'NS':['6', '2', '1']} .\nLE : Less than or equal.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nLT : Less than.  AttributeValueList can contain only one AttributeValue of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nGE : Greater than or equal.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nGT : Greater than.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nNOT_NULL : The attribute exists. NOT_NULL is supported for all data types, including lists and maps.\n\n\nNote\nThis operator tests for the existence of an attribute, not its data type. If the data type of attribute 'a ' is null, and you evaluate it using NOT_NULL , the result is a Boolean true . This result is because the attribute 'a ' exists; its data type is not relevant to the NOT_NULL comparison operator.\n\n\nNULL : The attribute does not exist. NULL is supported for all data types, including lists and maps.\n\n\nNote\nThis operator tests for the nonexistence of an attribute, not its data type. If the data type of attribute 'a ' is null, and you evaluate it using NULL , the result is a Boolean false . This is because the attribute 'a ' exists; its data type is not relevant to the NULL comparison operator.\n\n\nCONTAINS : Checks for a subsequence, or value in a set. AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is of type String, then the operator checks for a substring match. If the target attribute of the comparison is of type Binary, then the operator looks for a subsequence of the target that matches the input. If the target attribute of the comparison is a set ('SS ', 'NS ', or 'BS '), then the operator evaluates to true if it finds an exact match with any member of the set. CONTAINS is supported for lists: When evaluating 'a CONTAINS b ', 'a ' can be a list; however, 'b ' cannot be a set, a map, or a list.\nNOT_CONTAINS : Checks for absence of a subsequence, or absence of a value in a set. AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is a String, then the operator checks for the absence of a substring match. If the target attribute of the comparison is Binary, then the operator checks for the absence of a subsequence of the target that matches the input. If the target attribute of the comparison is a set ('SS ', 'NS ', or 'BS '), then the operator evaluates to true if it does not find an exact match with any member of the set. NOT_CONTAINS is supported for lists: When evaluating 'a NOT CONTAINS b ', 'a ' can be a list; however, 'b ' cannot be a set, a map, or a list.\nBEGINS_WITH : Checks for a prefix.  AttributeValueList can contain only one AttributeValue of type String or Binary (not a Number or a set type). The target attribute of the comparison must be of type String or Binary (not a Number or a set type).\nIN : Checks for matching elements in a list. AttributeValueList can contain one or more AttributeValue elements of type String, Number, or Binary. These attributes are compared against an existing attribute of an item. If any elements of the input are equal to the item attribute, the expression evaluates to true.\nBETWEEN : Greater than or equal to the first value, and less than or equal to the second value.  AttributeValueList must contain two AttributeValue elements of the same type, either String, Number, or Binary (not a set type). A target attribute matches if the target value is greater than, or equal to, the first element and less than, or equal to, the second element. If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not compare to {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']}\n\nFor usage examples of AttributeValueList and ComparisonOperator , see Legacy Conditional Parameters in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\n\n

    :type QueryFilter: dict
    :param QueryFilter: This is a legacy parameter. Use FilterExpression instead. For more information, see QueryFilter in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(dict) --Represents the selection criteria for a Query or Scan operation:\n\nFor a Query operation, Condition is used for specifying the KeyConditions to use when querying a table or an index. For KeyConditions , only the following comparison operators are supported: EQ | LE | LT | GE | GT | BEGINS_WITH | BETWEEN Condition is also used in a QueryFilter , which evaluates the query results and returns only the desired values.\nFor a Scan operation, Condition is used in a ScanFilter , which evaluates the scan results and returns only the desired values.\n\n\nAttributeValueList (list) --One or more values to evaluate against the supplied attribute. The number of values in the list depends on the ComparisonOperator being used.\nFor type Number, value comparisons are numeric.\nString value comparisons for greater than, equals, or less than are based on ASCII character code values. For example, a is greater than A , and a is greater than B . For a list of code values, see http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters .\nFor Binary, DynamoDB treats each byte of the binary data as unsigned when it compares binary values.\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\nComparisonOperator (string) -- [REQUIRED]A comparator for evaluating attributes. For example, equals, greater than, less than, etc.\nThe following comparison operators are available:\n\nEQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS | NOT_CONTAINS | BEGINS_WITH | IN | BETWEEN\nThe following are descriptions of each comparison operator.\n\nEQ : Equal. EQ is supported for all data types, including lists and maps. AttributeValueList can contain only one AttributeValue element of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not equal {'NS':['6', '2', '1']} .\nNE : Not equal. NE is supported for all data types, including lists and maps. AttributeValueList can contain only one AttributeValue of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an AttributeValue of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not equal {'NS':['6', '2', '1']} .\nLE : Less than or equal.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nLT : Less than.  AttributeValueList can contain only one AttributeValue of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nGE : Greater than or equal.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nGT : Greater than.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nNOT_NULL : The attribute exists. NOT_NULL is supported for all data types, including lists and maps.\n\n\nNote\nThis operator tests for the existence of an attribute, not its data type. If the data type of attribute 'a ' is null, and you evaluate it using NOT_NULL , the result is a Boolean true . This result is because the attribute 'a ' exists; its data type is not relevant to the NOT_NULL comparison operator.\n\n\nNULL : The attribute does not exist. NULL is supported for all data types, including lists and maps.\n\n\nNote\nThis operator tests for the nonexistence of an attribute, not its data type. If the data type of attribute 'a ' is null, and you evaluate it using NULL , the result is a Boolean false . This is because the attribute 'a ' exists; its data type is not relevant to the NULL comparison operator.\n\n\nCONTAINS : Checks for a subsequence, or value in a set. AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is of type String, then the operator checks for a substring match. If the target attribute of the comparison is of type Binary, then the operator looks for a subsequence of the target that matches the input. If the target attribute of the comparison is a set ('SS ', 'NS ', or 'BS '), then the operator evaluates to true if it finds an exact match with any member of the set. CONTAINS is supported for lists: When evaluating 'a CONTAINS b ', 'a ' can be a list; however, 'b ' cannot be a set, a map, or a list.\nNOT_CONTAINS : Checks for absence of a subsequence, or absence of a value in a set. AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is a String, then the operator checks for the absence of a substring match. If the target attribute of the comparison is Binary, then the operator checks for the absence of a subsequence of the target that matches the input. If the target attribute of the comparison is a set ('SS ', 'NS ', or 'BS '), then the operator evaluates to true if it does not find an exact match with any member of the set. NOT_CONTAINS is supported for lists: When evaluating 'a NOT CONTAINS b ', 'a ' can be a list; however, 'b ' cannot be a set, a map, or a list.\nBEGINS_WITH : Checks for a prefix.  AttributeValueList can contain only one AttributeValue of type String or Binary (not a Number or a set type). The target attribute of the comparison must be of type String or Binary (not a Number or a set type).\nIN : Checks for matching elements in a list. AttributeValueList can contain one or more AttributeValue elements of type String, Number, or Binary. These attributes are compared against an existing attribute of an item. If any elements of the input are equal to the item attribute, the expression evaluates to true.\nBETWEEN : Greater than or equal to the first value, and less than or equal to the second value.  AttributeValueList must contain two AttributeValue elements of the same type, either String, Number, or Binary (not a set type). A target attribute matches if the target value is greater than, or equal to, the first element and less than, or equal to, the second element. If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not compare to {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']}\n\nFor usage examples of AttributeValueList and ComparisonOperator , see Legacy Conditional Parameters in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\n\n

    :type ConditionalOperator: string
    :param ConditionalOperator: This is a legacy parameter. Use FilterExpression instead. For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide .

    :type ScanIndexForward: boolean
    :param ScanIndexForward: Specifies the order for index traversal: If true (default), the traversal is performed in ascending order; if false , the traversal is performed in descending order.\nItems with the same partition key value are stored in sorted order by sort key. If the sort key data type is Number, the results are stored in numeric order. For type String, the results are stored in order of UTF-8 bytes. For type Binary, DynamoDB treats each byte of the binary data as unsigned.\nIf ScanIndexForward is true , DynamoDB returns the results in the order in which they are stored (by sort key value). This is the default behavior. If ScanIndexForward is false , DynamoDB reads the results in reverse order by sort key value, and then returns the results to the client.\n

    :type ExclusiveStartKey: dict
    :param ExclusiveStartKey: The primary key of the first item that this operation will evaluate. Use the value that was returned for LastEvaluatedKey in the previous operation.\nThe data type for ExclusiveStartKey must be String, Number, or Binary. No set data types are allowed.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n

    :type ReturnConsumedCapacity: string
    :param ReturnConsumedCapacity: Determines the level of detail about provisioned throughput consumption that is returned in the response:\n\nINDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem , do not access any indexes at all. In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s).\nTOTAL - The response includes only the aggregate ConsumedCapacity for the operation.\nNONE - No ConsumedCapacity details are included in the response.\n\n

    :type ProjectionExpression: string
    :param ProjectionExpression: A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.\nIf no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result.\nFor more information, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide .\n

    :type FilterExpression: string
    :param FilterExpression: A string that contains conditions that DynamoDB applies after the Query operation, but before the data is returned to you. Items that do not satisfy the FilterExpression criteria are not returned.\nA FilterExpression does not allow key attributes. You cannot define a filter expression based on a partition key or a sort key.\n\nNote\nA FilterExpression is applied after the items have already been read; the process of filtering does not consume any additional read capacity units.\n\nFor more information, see Filter Expressions in the Amazon DynamoDB Developer Guide .\n

    :type KeyConditionExpression: string
    :param KeyConditionExpression: The condition that specifies the key values for items to be retrieved by the Query action.\nThe condition must perform an equality test on a single partition key value.\nThe condition can optionally perform one of several comparison tests on a single sort key value. This allows Query to retrieve one item with a given partition key value and sort key value, or several items that have the same partition key value but different sort key values.\nThe partition key equality test is required, and must be specified in the following format:\n\npartitionKeyName = :partitionkeyval\nIf you also want to provide a condition for the sort key, it must be combined using AND with the condition for the sort key. Following is an example, using the = comparison operator for the sort key:\n\npartitionKeyName = :partitionkeyval AND sortKeyName = :sortkeyval\nValid comparisons for the sort key condition are as follows:\n\nsortKeyName = :sortkeyval - true if the sort key value is equal to :sortkeyval .\nsortKeyName < :sortkeyval - true if the sort key value is less than :sortkeyval .\nsortKeyName <= :sortkeyval - true if the sort key value is less than or equal to :sortkeyval .\nsortKeyName > :sortkeyval - true if the sort key value is greater than :sortkeyval .\nsortKeyName >= :sortkeyval - true if the sort key value is greater than or equal to :sortkeyval .\nsortKeyName BETWEEN :sortkeyval1 AND :sortkeyval2 - true if the sort key value is greater than or equal to :sortkeyval1 , and less than or equal to :sortkeyval2 .\nbegins_with ( sortKeyName , :sortkeyval ) - true if the sort key value begins with a particular operand. (You cannot use this function with a sort key that is of type Number.) Note that the function name begins_with is case-sensitive.\n\nUse the ExpressionAttributeValues parameter to replace tokens such as :partitionval and :sortval with actual values at runtime.\nYou can optionally use the ExpressionAttributeNames parameter to replace the names of the partition key and sort key with placeholder tokens. This option might be necessary if an attribute name conflicts with a DynamoDB reserved word. For example, the following KeyConditionExpression parameter causes an error because Size is a reserved word:\n\nSize = :myval\n\nTo work around this, define a placeholder (such a #S ) to represent the attribute name Size . KeyConditionExpression then is as follows:\n\n#S = :myval\n\nFor a list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide .\nFor more information on ExpressionAttributeNames and ExpressionAttributeValues , see Using Placeholders for Attribute Names and Values in the Amazon DynamoDB Developer Guide .\n

    :type ExpressionAttributeNames: dict
    :param ExpressionAttributeNames: One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames :\n\nTo access an attribute whose name conflicts with a DynamoDB reserved word.\nTo create a placeholder for repeating occurrences of an attribute name in an expression.\nTo prevent special characters in an attribute name from being misinterpreted in an expression.\n\nUse the # character in an expression to dereference an attribute name. For example, consider the following attribute name:\n\nPercentile\n\nThe name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide ). To work around this, you could specify the following for ExpressionAttributeNames :\n\n{'#P':'Percentile'}\n\nYou could then use this substitution in an expression, as in this example:\n\n#P = :val\n\n\nNote\nTokens that begin with the : character are expression attribute values , which are placeholders for the actual value at runtime.\n\nFor more information on expression attribute names, see Specifying Item Attributes in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type ExpressionAttributeValues: dict
    :param ExpressionAttributeValues: One or more values that can be substituted in an expression.\nUse the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:\n\nAvailable | Backordered | Discontinued\nYou would first need to specify ExpressionAttributeValues as follows:\n\n{ ':avail':{'S':'Available'}, ':back':{'S':'Backordered'}, ':disc':{'S':'Discontinued'} }\nYou could then use these values in an expression, such as this:\n\nProductStatus IN (:avail, :back, :disc)\nFor more information on expression attribute values, see Specifying Conditions in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
    ],
    'Count': 123,
    'ScannedCount': 123,
    'LastEvaluatedKey': {
        'string': {
            'S': 'string',
            'N': 'string',
            'B': b'bytes',
            'SS': [
                'string',
            ],
            'NS': [
                'string',
            ],
            'BS': [
                b'bytes',
            ],
            'M': {
                'string': {'... recursive ...'}
            },
            'L': [
                {'... recursive ...'},
            ],
            'NULL': True|False,
            'BOOL': True|False
        }
    },
    'ConsumedCapacity': {
        'TableName': 'string',
        'CapacityUnits': 123.0,
        'ReadCapacityUnits': 123.0,
        'WriteCapacityUnits': 123.0,
        'Table': {
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'CapacityUnits': 123.0
        },
        'LocalSecondaryIndexes': {
            'string': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            }
        },
        'GlobalSecondaryIndexes': {
            'string': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            }
        }
    }
}


Response Structure

(dict) --
Represents the output of a Query operation.

Items (list) --
An array of item attributes that match the query criteria. Each element in this array consists of an attribute name and the value for that attribute.

(dict) --

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true










Count (integer) --
The number of items in the response.
If you used a QueryFilter in the request, then Count is the number of items returned after the filter was applied, and ScannedCount is the number of matching items before the filter was applied.
If you did not use a filter in the request, then Count and ScannedCount are the same.

ScannedCount (integer) --
The number of items evaluated, before any QueryFilter is applied. A high ScannedCount value with few, or no, Count results indicates an inefficient Query operation. For more information, see Count and ScannedCount in the Amazon DynamoDB Developer Guide .
If you did not use a filter in the request, then ScannedCount is the same as Count .

LastEvaluatedKey (dict) --
The primary key of the item where the operation stopped, inclusive of the previous result set. Use this value to start a new operation, excluding this value in the new request.
If LastEvaluatedKey is empty, then the "last page" of results has been processed and there is no more data to be retrieved.
If LastEvaluatedKey is not empty, it does not necessarily mean that there is more data in the result set. The only way to know when you have reached the end of the result set is when LastEvaluatedKey is empty.

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true








ConsumedCapacity (dict) --
The capacity units consumed by the Query operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. ConsumedCapacity is only returned if the ReturnConsumedCapacity parameter was specified. For more information, see Provisioned Throughput in the Amazon DynamoDB Developer Guide .

TableName (string) --
The name of the table that was affected by the operation.

CapacityUnits (float) --
The total number of capacity units consumed by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed by the operation.

WriteCapacityUnits (float) --
The total number of write capacity units consumed by the operation.

Table (dict) --
The amount of throughput consumed on the table affected by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.



LocalSecondaryIndexes (dict) --
The amount of throughput consumed on each local index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.







GlobalSecondaryIndexes (dict) --
The amount of throughput consumed on each global index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.















Exceptions

DynamoDB.Client.exceptions.ProvisionedThroughputExceededException
DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.RequestLimitExceeded
DynamoDB.Client.exceptions.InternalServerError

Examples
This example queries items in the Music table. The table has a partition key and sort key (Artist and SongTitle), but this query only specifies the partition key value. It returns song titles by the artist named "No One You Know".
response = client.query(
    ExpressionAttributeValues={
        ':v1': {
            'S': 'No One You Know',
        },
    },
    KeyConditionExpression='Artist = :v1',
    ProjectionExpression='SongTitle',
    TableName='Music',
)

print(response)


Expected Output:
{
    'ConsumedCapacity': {
    },
    'Count': 2,
    'Items': [
        {
            'SongTitle': {
                'S': 'Call Me Today',
            },
        },
    ],
    'ScannedCount': 2,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Items': [
            {
                'string': {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                }
            },
        ],
        'Count': 123,
        'ScannedCount': 123,
        'LastEvaluatedKey': {
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        'ConsumedCapacity': {
            'TableName': 'string',
            'CapacityUnits': 123.0,
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'Table': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            },
            'LocalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            },
            'GlobalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def restore_table_from_backup(TargetTableName=None, BackupArn=None, BillingModeOverride=None, GlobalSecondaryIndexOverride=None, LocalSecondaryIndexOverride=None, ProvisionedThroughputOverride=None, SSESpecificationOverride=None):
    """
    Creates a new table from an existing backup. Any number of users can execute up to 4 concurrent restores (any type of restore) in a given account.
    You can call RestoreTableFromBackup at a maximum rate of 10 times per second.
    You must manually set up the following on the restored table:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.restore_table_from_backup(
        TargetTableName='string',
        BackupArn='string',
        BillingModeOverride='PROVISIONED'|'PAY_PER_REQUEST',
        GlobalSecondaryIndexOverride=[
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                }
            },
        ],
        LocalSecondaryIndexOverride=[
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                }
            },
        ],
        ProvisionedThroughputOverride={
            'ReadCapacityUnits': 123,
            'WriteCapacityUnits': 123
        },
        SSESpecificationOverride={
            'Enabled': True|False,
            'SSEType': 'AES256'|'KMS',
            'KMSMasterKeyId': 'string'
        }
    )
    
    
    :type TargetTableName: string
    :param TargetTableName: [REQUIRED]\nThe name of the new table to which the backup must be restored.\n

    :type BackupArn: string
    :param BackupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) associated with the backup.\n

    :type BillingModeOverride: string
    :param BillingModeOverride: The billing mode of the restored table.

    :type GlobalSecondaryIndexOverride: list
    :param GlobalSecondaryIndexOverride: List of global secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.\n\n(dict) --Represents the properties of a global secondary index.\n\nIndexName (string) -- [REQUIRED]The name of the global secondary index. The name must be unique among all other indexes on this table.\n\nKeySchema (list) -- [REQUIRED]The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:\n\nHASH - partition key\nRANGE - sort key\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\n\n(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.\nA KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.\nA KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.\n\nAttributeName (string) -- [REQUIRED]The name of a key attribute.\n\nKeyType (string) -- [REQUIRED]The role that this key attribute will assume:\n\nHASH - partition key\nRANGE - sort key\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\n\n\n\n\n\nProjection (dict) -- [REQUIRED]Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.\n\nProjectionType (string) --The set of attributes that are projected into the index:\n\nKEYS_ONLY - Only the index and primary keys are projected into the index.\nINCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .\nALL - All of the table attributes are projected into the index.\n\n\nNonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.\nFor local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.\n\n(string) --\n\n\n\n\nProvisionedThroughput (dict) --Represents the provisioned throughput settings for the specified global secondary index.\nFor current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .\n\nReadCapacityUnits (integer) -- [REQUIRED]The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\nWriteCapacityUnits (integer) -- [REQUIRED]The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\n\n\n\n\n\n

    :type LocalSecondaryIndexOverride: list
    :param LocalSecondaryIndexOverride: List of local secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.\n\n(dict) --Represents the properties of a local secondary index.\n\nIndexName (string) -- [REQUIRED]The name of the local secondary index. The name must be unique among all other indexes on this table.\n\nKeySchema (list) -- [REQUIRED]The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:\n\nHASH - partition key\nRANGE - sort key\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\n\n(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.\nA KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.\nA KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.\n\nAttributeName (string) -- [REQUIRED]The name of a key attribute.\n\nKeyType (string) -- [REQUIRED]The role that this key attribute will assume:\n\nHASH - partition key\nRANGE - sort key\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\n\n\n\n\n\nProjection (dict) -- [REQUIRED]Represents attributes that are copied (projected) from the table into the local secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.\n\nProjectionType (string) --The set of attributes that are projected into the index:\n\nKEYS_ONLY - Only the index and primary keys are projected into the index.\nINCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .\nALL - All of the table attributes are projected into the index.\n\n\nNonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.\nFor local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.\n\n(string) --\n\n\n\n\n\n\n\n

    :type ProvisionedThroughputOverride: dict
    :param ProvisionedThroughputOverride: Provisioned throughput settings for the restored table.\n\nReadCapacityUnits (integer) -- [REQUIRED]The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\nWriteCapacityUnits (integer) -- [REQUIRED]The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\n\n

    :type SSESpecificationOverride: dict
    :param SSESpecificationOverride: The new server-side encryption settings for the restored table.\n\nEnabled (boolean) --Indicates whether server-side encryption is done using an AWS managed CMK or an AWS owned CMK. If enabled (true), server-side encryption type is set to KMS and an AWS managed CMK is used (AWS KMS charges apply). If disabled (false) or not specified, server-side encryption is set to AWS owned CMK.\n\nSSEType (string) --Server-side encryption type. The only supported value is:\n\nKMS - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).\n\n\nKMSMasterKeyId (string) --The AWS KMS customer master key (CMK) that should be used for the AWS KMS encryption. To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB customer master key alias/aws/dynamodb.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TableDescription': {
        'AttributeDefinitions': [
            {
                'AttributeName': 'string',
                'AttributeType': 'S'|'N'|'B'
            },
        ],
        'TableName': 'string',
        'KeySchema': [
            {
                'AttributeName': 'string',
                'KeyType': 'HASH'|'RANGE'
            },
        ],
        'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
        'CreationDateTime': datetime(2015, 1, 1),
        'ProvisionedThroughput': {
            'LastIncreaseDateTime': datetime(2015, 1, 1),
            'LastDecreaseDateTime': datetime(2015, 1, 1),
            'NumberOfDecreasesToday': 123,
            'ReadCapacityUnits': 123,
            'WriteCapacityUnits': 123
        },
        'TableSizeBytes': 123,
        'ItemCount': 123,
        'TableArn': 'string',
        'TableId': 'string',
        'BillingModeSummary': {
            'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
            'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
        },
        'LocalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexArn': 'string'
            },
        ],
        'GlobalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                'Backfilling': True|False,
                'ProvisionedThroughput': {
                    'LastIncreaseDateTime': datetime(2015, 1, 1),
                    'LastDecreaseDateTime': datetime(2015, 1, 1),
                    'NumberOfDecreasesToday': 123,
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexArn': 'string'
            },
        ],
        'StreamSpecification': {
            'StreamEnabled': True|False,
            'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
        },
        'LatestStreamLabel': 'string',
        'LatestStreamArn': 'string',
        'GlobalTableVersion': 'string',
        'Replicas': [
            {
                'RegionName': 'string',
                'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                'ReplicaStatusDescription': 'string',
                'ReplicaStatusPercentProgress': 'string',
                'KMSMasterKeyId': 'string',
                'ProvisionedThroughputOverride': {
                    'ReadCapacityUnits': 123
                },
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'ProvisionedThroughputOverride': {
                            'ReadCapacityUnits': 123
                        }
                    },
                ]
            },
        ],
        'RestoreSummary': {
            'SourceBackupArn': 'string',
            'SourceTableArn': 'string',
            'RestoreDateTime': datetime(2015, 1, 1),
            'RestoreInProgress': True|False
        },
        'SSEDescription': {
            'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
            'SSEType': 'AES256'|'KMS',
            'KMSMasterKeyArn': 'string',
            'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
        },
        'ArchivalSummary': {
            'ArchivalDateTime': datetime(2015, 1, 1),
            'ArchivalReason': 'string',
            'ArchivalBackupArn': 'string'
        }
    }
}


Response Structure

(dict) --

TableDescription (dict) --
The description of the table created from an existing backup.

AttributeDefinitions (list) --
An array of AttributeDefinition objects. Each of these objects describes one attribute in the table and index key schema.
Each AttributeDefinition object in this array is composed of:

AttributeName - The name of the attribute.
AttributeType - The data type for the attribute.


(dict) --
Represents an attribute for describing the key schema for the table and indexes.

AttributeName (string) --
A name for the attribute.

AttributeType (string) --
The data type for the attribute, where:

S - the attribute is of type String
N - the attribute is of type Number
B - the attribute is of type Binary






TableName (string) --
The name of the table.

KeySchema (list) --
The primary key structure for the table. Each KeySchemaElement consists of:

AttributeName - The name of the attribute.
KeyType - The role of the attribute:
HASH - partition key
RANGE - sort key




Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

For more information about primary keys, see Primary Key in the Amazon DynamoDB Developer Guide .

(dict) --
Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --
The name of a key attribute.

KeyType (string) --
The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






TableStatus (string) --
The current state of the table:

CREATING - The table is being created.
UPDATING - The table is being updated.
DELETING - The table is being deleted.
ACTIVE - The table is ready for use.
INACCESSIBLE_ENCRYPTION_CREDENTIALS - The AWS KMS key used to encrypt the table in inaccessible. Table operations may fail due to failure to use the AWS KMS key. DynamoDB will initiate the table archival process when a table\'s AWS KMS key remains inaccessible for more than seven days.
ARCHIVING - The table is being archived. Operations are not allowed until archival is complete.
ARCHIVED - The table has been archived. See the ArchivalReason for more information.


CreationDateTime (datetime) --
The date and time when the table was created, in UNIX epoch time format.

ProvisionedThroughput (dict) --
The provisioned throughput settings for the table, consisting of read and write capacity units, along with data about increases and decreases.

LastIncreaseDateTime (datetime) --
The date and time of the last provisioned throughput increase for this table.

LastDecreaseDateTime (datetime) --
The date and time of the last provisioned throughput decrease for this table.

NumberOfDecreasesToday (integer) --
The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see Limits in the Amazon DynamoDB Developer Guide .

ReadCapacityUnits (integer) --
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 ReadCapacityUnits per second provides 100 eventually consistent ReadCapacityUnits per second.

WriteCapacityUnits (integer) --
The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException .



TableSizeBytes (integer) --
The total size of the specified table, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --
The number of items in the specified table. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

TableArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the table.

TableId (string) --
Unique identifier for the table for which the backup was created.

BillingModeSummary (dict) --
Contains the details for the read/write capacity mode.

BillingMode (string) --
Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.

PROVISIONED - Sets the read/write capacity mode to PROVISIONED . We recommend using PROVISIONED for predictable workloads.
PAY_PER_REQUEST - Sets the read/write capacity mode to PAY_PER_REQUEST . We recommend using PAY_PER_REQUEST for unpredictable workloads.


LastUpdateToPayPerRequestDateTime (datetime) --
Represents the time when PAY_PER_REQUEST was last set as the read/write capacity mode.



LocalSecondaryIndexes (list) --
Represents one or more local secondary indexes on the table. Each index is scoped to a given partition key value. Tables with one or more local secondary indexes are subject to an item collection size limit, where the amount of data within a given item collection cannot exceed 10 GB. Each element is composed of:

IndexName - The name of the local secondary index.
KeySchema - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
Projection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
ProjectionType - One of the following:
KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes , summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.


IndexSizeBytes - Represents the total size of the index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
ItemCount - Represents the number of items in the index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

If the table is in the DELETING state, no information about indexes will be returned.

(dict) --
Represents the properties of a local secondary index.

IndexName (string) --
Represents the name of the local secondary index.

KeySchema (list) --
The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --
Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --
The name of a key attribute.

KeyType (string) --
The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --
Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --
The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --
Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --




IndexSizeBytes (integer) --
The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --
The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

IndexArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the index.





GlobalSecondaryIndexes (list) --
The global secondary indexes, if any, on the table. Each index is scoped to a given partition key value. Each element is composed of:

Backfilling - If true, then the index is currently in the backfilling phase. Backfilling occurs only when a new global secondary index is added to the table. It is the process by which DynamoDB populates the new index with data from the table. (This attribute does not appear for indexes that were created during a CreateTable operation.)  You can delete an index that is being created during the Backfilling phase when IndexStatus is set to CREATING and Backfilling is true. You can\'t delete the index that is being created when IndexStatus is set to CREATING and Backfilling is false. (This attribute does not appear for indexes that were created during a CreateTable operation.)
IndexName - The name of the global secondary index.
IndexSizeBytes - The total size of the global secondary index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
IndexStatus - The current status of the global secondary index:
CREATING - The index is being created.
UPDATING - The index is being updated.
DELETING - The index is being deleted.
ACTIVE - The index is ready for use.


ItemCount - The number of items in the global secondary index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
KeySchema - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
Projection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
ProjectionType - One of the following:
KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes , summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.


ProvisionedThroughput - The provisioned throughput settings for the global secondary index, consisting of read and write capacity units, along with data about increases and decreases.

If the table is in the DELETING state, no information about indexes will be returned.

(dict) --
Represents the properties of a global secondary index.

IndexName (string) --
The name of the global secondary index.

KeySchema (list) --
The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --
Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --
The name of a key attribute.

KeyType (string) --
The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --
Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --
The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --
Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --




IndexStatus (string) --
The current state of the global secondary index:

CREATING - The index is being created.
UPDATING - The index is being updated.
DELETING - The index is being deleted.
ACTIVE - The index is ready for use.


Backfilling (boolean) --
Indicates whether the index is currently backfilling. Backfilling is the process of reading items from the table and determining whether they can be added to the index. (Not all items will qualify: For example, a partition key cannot have any duplicate values.) If an item can be added to the index, DynamoDB will do so. After all items have been processed, the backfilling operation is complete and Backfilling is false.
You can delete an index that is being created during the Backfilling phase when IndexStatus is set to CREATING and Backfilling is true. You can\'t delete the index that is being created when IndexStatus is set to CREATING and Backfilling is false.

Note
For indexes that were created during a CreateTable operation, the Backfilling attribute does not appear in the DescribeTable output.


ProvisionedThroughput (dict) --
Represents the provisioned throughput settings for the specified global secondary index.
For current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .

LastIncreaseDateTime (datetime) --
The date and time of the last provisioned throughput increase for this table.

LastDecreaseDateTime (datetime) --
The date and time of the last provisioned throughput decrease for this table.

NumberOfDecreasesToday (integer) --
The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see Limits in the Amazon DynamoDB Developer Guide .

ReadCapacityUnits (integer) --
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 ReadCapacityUnits per second provides 100 eventually consistent ReadCapacityUnits per second.

WriteCapacityUnits (integer) --
The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException .



IndexSizeBytes (integer) --
The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --
The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

IndexArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the index.





StreamSpecification (dict) --
The current DynamoDB Streams configuration for the table.

StreamEnabled (boolean) --
Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.

StreamViewType (string) --
When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are:

KEYS_ONLY - Only the key attributes of the modified item are written to the stream.
NEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.
OLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.
NEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream.




LatestStreamLabel (string) --
A timestamp, in ISO 8601 format, for this stream.
Note that LatestStreamLabel is not a unique identifier for the stream, because it is possible that a stream from another table might have the same timestamp. However, the combination of the following three elements is guaranteed to be unique:

AWS customer ID
Table name
StreamLabel


LatestStreamArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the latest stream for this table.

GlobalTableVersion (string) --
Represents the version of global tables in use, if the table is replicated across AWS Regions.

Replicas (list) --
Represents replicas of the table.

(dict) --
Contains the details of the replica.

RegionName (string) --
The name of the Region.

ReplicaStatus (string) --
The current state of the replica:

CREATING - The replica is being created.
UPDATING - The replica is being updated.
DELETING - The replica is being deleted.
ACTIVE - The replica is ready for use.


ReplicaStatusDescription (string) --
Detailed information about the replica status.

ReplicaStatusPercentProgress (string) --
Specifies the progress of a Create, Update, or Delete action on the replica as a percentage.

KMSMasterKeyId (string) --
The AWS KMS customer master key (CMK) of the replica that will be used for AWS KMS encryption.

ProvisionedThroughputOverride (dict) --
Replica-specific provisioned throughput. If not described, uses the source table\'s provisioned throughput settings.

ReadCapacityUnits (integer) --
Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.



GlobalSecondaryIndexes (list) --
Replica-specific global secondary index settings.

(dict) --
Represents the properties of a replica global secondary index.

IndexName (string) --
The name of the global secondary index.

ProvisionedThroughputOverride (dict) --
If not described, uses the source table GSI\'s read capacity settings.

ReadCapacityUnits (integer) --
Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.











RestoreSummary (dict) --
Contains details for the restore.

SourceBackupArn (string) --
The Amazon Resource Name (ARN) of the backup from which the table was restored.

SourceTableArn (string) --
The ARN of the source table of the backup that is being restored.

RestoreDateTime (datetime) --
Point in time or source backup time.

RestoreInProgress (boolean) --
Indicates if a restore is in progress or not.



SSEDescription (dict) --
The description of the server-side encryption status on the specified table.

Status (string) --
Represents the current state of server-side encryption. The only supported values are:

ENABLED - Server-side encryption is enabled.
UPDATING - Server-side encryption is being updated.


SSEType (string) --
Server-side encryption type. The only supported value is:

KMS - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).


KMSMasterKeyArn (string) --
The AWS KMS customer master key (CMK) ARN used for the AWS KMS encryption.

InaccessibleEncryptionDateTime (datetime) --
Indicates the time, in UNIX epoch date format, when DynamoDB detected that the table\'s AWS KMS key was inaccessible. This attribute will automatically be cleared when DynamoDB detects that the table\'s AWS KMS key is accessible again. DynamoDB will initiate the table archival process when table\'s AWS KMS key remains inaccessible for more than seven days from this date.



ArchivalSummary (dict) --
Contains information about the table archive.

ArchivalDateTime (datetime) --
The date and time when table archival was initiated by DynamoDB, in UNIX epoch time format.

ArchivalReason (string) --
The reason DynamoDB archived the table. Currently, the only possible value is:

INACCESSIBLE_ENCRYPTION_CREDENTIALS - The table was archived due to the table\'s AWS KMS key being inaccessible for more than seven days. An On-Demand backup was created at the archival time.


ArchivalBackupArn (string) --
The Amazon Resource Name (ARN) of the backup the table was archived to, when applicable in the archival reason. If you wish to restore this backup to the same table name, you will need to delete the original table.











Exceptions

DynamoDB.Client.exceptions.TableAlreadyExistsException
DynamoDB.Client.exceptions.TableInUseException
DynamoDB.Client.exceptions.BackupNotFoundException
DynamoDB.Client.exceptions.BackupInUseException
DynamoDB.Client.exceptions.LimitExceededException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'TableDescription': {
            'AttributeDefinitions': [
                {
                    'AttributeName': 'string',
                    'AttributeType': 'S'|'N'|'B'
                },
            ],
            'TableName': 'string',
            'KeySchema': [
                {
                    'AttributeName': 'string',
                    'KeyType': 'HASH'|'RANGE'
                },
            ],
            'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
            'CreationDateTime': datetime(2015, 1, 1),
            'ProvisionedThroughput': {
                'LastIncreaseDateTime': datetime(2015, 1, 1),
                'LastDecreaseDateTime': datetime(2015, 1, 1),
                'NumberOfDecreasesToday': 123,
                'ReadCapacityUnits': 123,
                'WriteCapacityUnits': 123
            },
            'TableSizeBytes': 123,
            'ItemCount': 123,
            'TableArn': 'string',
            'TableId': 'string',
            'BillingModeSummary': {
                'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
                'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
            },
            'LocalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'IndexSizeBytes': 123,
                    'ItemCount': 123,
                    'IndexArn': 'string'
                },
            ],
            'GlobalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                    'Backfilling': True|False,
                    'ProvisionedThroughput': {
                        'LastIncreaseDateTime': datetime(2015, 1, 1),
                        'LastDecreaseDateTime': datetime(2015, 1, 1),
                        'NumberOfDecreasesToday': 123,
                        'ReadCapacityUnits': 123,
                        'WriteCapacityUnits': 123
                    },
                    'IndexSizeBytes': 123,
                    'ItemCount': 123,
                    'IndexArn': 'string'
                },
            ],
            'StreamSpecification': {
                'StreamEnabled': True|False,
                'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
            },
            'LatestStreamLabel': 'string',
            'LatestStreamArn': 'string',
            'GlobalTableVersion': 'string',
            'Replicas': [
                {
                    'RegionName': 'string',
                    'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                    'ReplicaStatusDescription': 'string',
                    'ReplicaStatusPercentProgress': 'string',
                    'KMSMasterKeyId': 'string',
                    'ProvisionedThroughputOverride': {
                        'ReadCapacityUnits': 123
                    },
                    'GlobalSecondaryIndexes': [
                        {
                            'IndexName': 'string',
                            'ProvisionedThroughputOverride': {
                                'ReadCapacityUnits': 123
                            }
                        },
                    ]
                },
            ],
            'RestoreSummary': {
                'SourceBackupArn': 'string',
                'SourceTableArn': 'string',
                'RestoreDateTime': datetime(2015, 1, 1),
                'RestoreInProgress': True|False
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
                'SSEType': 'AES256'|'KMS',
                'KMSMasterKeyArn': 'string',
                'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
            },
            'ArchivalSummary': {
                'ArchivalDateTime': datetime(2015, 1, 1),
                'ArchivalReason': 'string',
                'ArchivalBackupArn': 'string'
            }
        }
    }
    
    
    :returns: 
    TargetTableName (string) -- [REQUIRED]
    The name of the new table to which the backup must be restored.
    
    BackupArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) associated with the backup.
    
    BillingModeOverride (string) -- The billing mode of the restored table.
    GlobalSecondaryIndexOverride (list) -- List of global secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.
    
    (dict) --Represents the properties of a global secondary index.
    
    IndexName (string) -- [REQUIRED]The name of the global secondary index. The name must be unique among all other indexes on this table.
    
    KeySchema (list) -- [REQUIRED]The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:
    
    HASH - partition key
    RANGE - sort key
    
    
    Note
    The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
    The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.
    
    
    (dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
    A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
    A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.
    
    AttributeName (string) -- [REQUIRED]The name of a key attribute.
    
    KeyType (string) -- [REQUIRED]The role that this key attribute will assume:
    
    HASH - partition key
    RANGE - sort key
    
    
    Note
    The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
    The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.
    
    
    
    
    
    
    Projection (dict) -- [REQUIRED]Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.
    
    ProjectionType (string) --The set of attributes that are projected into the index:
    
    KEYS_ONLY - Only the index and primary keys are projected into the index.
    INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
    ALL - All of the table attributes are projected into the index.
    
    
    NonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.
    For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.
    
    (string) --
    
    
    
    
    ProvisionedThroughput (dict) --Represents the provisioned throughput settings for the specified global secondary index.
    For current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .
    
    ReadCapacityUnits (integer) -- [REQUIRED]The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
    If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.
    
    WriteCapacityUnits (integer) -- [REQUIRED]The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
    If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.
    
    
    
    
    
    
    
    LocalSecondaryIndexOverride (list) -- List of local secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.
    
    (dict) --Represents the properties of a local secondary index.
    
    IndexName (string) -- [REQUIRED]The name of the local secondary index. The name must be unique among all other indexes on this table.
    
    KeySchema (list) -- [REQUIRED]The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:
    
    HASH - partition key
    RANGE - sort key
    
    
    Note
    The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
    The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.
    
    
    (dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
    A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
    A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.
    
    AttributeName (string) -- [REQUIRED]The name of a key attribute.
    
    KeyType (string) -- [REQUIRED]The role that this key attribute will assume:
    
    HASH - partition key
    RANGE - sort key
    
    
    Note
    The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
    The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.
    
    
    
    
    
    
    Projection (dict) -- [REQUIRED]Represents attributes that are copied (projected) from the table into the local secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.
    
    ProjectionType (string) --The set of attributes that are projected into the index:
    
    KEYS_ONLY - Only the index and primary keys are projected into the index.
    INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
    ALL - All of the table attributes are projected into the index.
    
    
    NonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.
    For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.
    
    (string) --
    
    
    
    
    
    
    
    
    ProvisionedThroughputOverride (dict) -- Provisioned throughput settings for the restored table.
    
    ReadCapacityUnits (integer) -- [REQUIRED]The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
    If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.
    
    WriteCapacityUnits (integer) -- [REQUIRED]The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
    If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.
    
    
    
    SSESpecificationOverride (dict) -- The new server-side encryption settings for the restored table.
    
    Enabled (boolean) --Indicates whether server-side encryption is done using an AWS managed CMK or an AWS owned CMK. If enabled (true), server-side encryption type is set to KMS and an AWS managed CMK is used (AWS KMS charges apply). If disabled (false) or not specified, server-side encryption is set to AWS owned CMK.
    
    SSEType (string) --Server-side encryption type. The only supported value is:
    
    KMS - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).
    
    
    KMSMasterKeyId (string) --The AWS KMS customer master key (CMK) that should be used for the AWS KMS encryption. To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB customer master key alias/aws/dynamodb.
    
    
    
    
    """
    pass

def restore_table_to_point_in_time(SourceTableArn=None, SourceTableName=None, TargetTableName=None, UseLatestRestorableTime=None, RestoreDateTime=None, BillingModeOverride=None, GlobalSecondaryIndexOverride=None, LocalSecondaryIndexOverride=None, ProvisionedThroughputOverride=None, SSESpecificationOverride=None):
    """
    Restores the specified table to the specified point in time within EarliestRestorableDateTime and LatestRestorableDateTime . You can restore your table to any point in time during the last 35 days. Any number of users can execute up to 4 concurrent restores (any type of restore) in a given account.
    When you restore using point in time recovery, DynamoDB restores your table data to the state based on the selected date and time (day:hour:minute:second) to a new table.
    Along with data, the following are also included on the new restored table using point in time recovery:
    You must manually set up the following on the restored table:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.restore_table_to_point_in_time(
        SourceTableArn='string',
        SourceTableName='string',
        TargetTableName='string',
        UseLatestRestorableTime=True|False,
        RestoreDateTime=datetime(2015, 1, 1),
        BillingModeOverride='PROVISIONED'|'PAY_PER_REQUEST',
        GlobalSecondaryIndexOverride=[
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                }
            },
        ],
        LocalSecondaryIndexOverride=[
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                }
            },
        ],
        ProvisionedThroughputOverride={
            'ReadCapacityUnits': 123,
            'WriteCapacityUnits': 123
        },
        SSESpecificationOverride={
            'Enabled': True|False,
            'SSEType': 'AES256'|'KMS',
            'KMSMasterKeyId': 'string'
        }
    )
    
    
    :type SourceTableArn: string
    :param SourceTableArn: The DynamoDB table that will be restored. This value is an Amazon Resource Name (ARN).

    :type SourceTableName: string
    :param SourceTableName: Name of the source table that is being restored.

    :type TargetTableName: string
    :param TargetTableName: [REQUIRED]\nThe name of the new table to which it must be restored to.\n

    :type UseLatestRestorableTime: boolean
    :param UseLatestRestorableTime: Restore the table to the latest possible time. LatestRestorableDateTime is typically 5 minutes before the current time.

    :type RestoreDateTime: datetime
    :param RestoreDateTime: Time in the past to restore the table to.

    :type BillingModeOverride: string
    :param BillingModeOverride: The billing mode of the restored table.

    :type GlobalSecondaryIndexOverride: list
    :param GlobalSecondaryIndexOverride: List of global secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.\n\n(dict) --Represents the properties of a global secondary index.\n\nIndexName (string) -- [REQUIRED]The name of the global secondary index. The name must be unique among all other indexes on this table.\n\nKeySchema (list) -- [REQUIRED]The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:\n\nHASH - partition key\nRANGE - sort key\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\n\n(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.\nA KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.\nA KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.\n\nAttributeName (string) -- [REQUIRED]The name of a key attribute.\n\nKeyType (string) -- [REQUIRED]The role that this key attribute will assume:\n\nHASH - partition key\nRANGE - sort key\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\n\n\n\n\n\nProjection (dict) -- [REQUIRED]Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.\n\nProjectionType (string) --The set of attributes that are projected into the index:\n\nKEYS_ONLY - Only the index and primary keys are projected into the index.\nINCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .\nALL - All of the table attributes are projected into the index.\n\n\nNonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.\nFor local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.\n\n(string) --\n\n\n\n\nProvisionedThroughput (dict) --Represents the provisioned throughput settings for the specified global secondary index.\nFor current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .\n\nReadCapacityUnits (integer) -- [REQUIRED]The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\nWriteCapacityUnits (integer) -- [REQUIRED]The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\n\n\n\n\n\n

    :type LocalSecondaryIndexOverride: list
    :param LocalSecondaryIndexOverride: List of local secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.\n\n(dict) --Represents the properties of a local secondary index.\n\nIndexName (string) -- [REQUIRED]The name of the local secondary index. The name must be unique among all other indexes on this table.\n\nKeySchema (list) -- [REQUIRED]The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:\n\nHASH - partition key\nRANGE - sort key\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\n\n(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.\nA KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.\nA KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.\n\nAttributeName (string) -- [REQUIRED]The name of a key attribute.\n\nKeyType (string) -- [REQUIRED]The role that this key attribute will assume:\n\nHASH - partition key\nRANGE - sort key\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\n\n\n\n\n\nProjection (dict) -- [REQUIRED]Represents attributes that are copied (projected) from the table into the local secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.\n\nProjectionType (string) --The set of attributes that are projected into the index:\n\nKEYS_ONLY - Only the index and primary keys are projected into the index.\nINCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .\nALL - All of the table attributes are projected into the index.\n\n\nNonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.\nFor local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.\n\n(string) --\n\n\n\n\n\n\n\n

    :type ProvisionedThroughputOverride: dict
    :param ProvisionedThroughputOverride: Provisioned throughput settings for the restored table.\n\nReadCapacityUnits (integer) -- [REQUIRED]The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\nWriteCapacityUnits (integer) -- [REQUIRED]The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\n\n

    :type SSESpecificationOverride: dict
    :param SSESpecificationOverride: The new server-side encryption settings for the restored table.\n\nEnabled (boolean) --Indicates whether server-side encryption is done using an AWS managed CMK or an AWS owned CMK. If enabled (true), server-side encryption type is set to KMS and an AWS managed CMK is used (AWS KMS charges apply). If disabled (false) or not specified, server-side encryption is set to AWS owned CMK.\n\nSSEType (string) --Server-side encryption type. The only supported value is:\n\nKMS - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).\n\n\nKMSMasterKeyId (string) --The AWS KMS customer master key (CMK) that should be used for the AWS KMS encryption. To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB customer master key alias/aws/dynamodb.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TableDescription': {
        'AttributeDefinitions': [
            {
                'AttributeName': 'string',
                'AttributeType': 'S'|'N'|'B'
            },
        ],
        'TableName': 'string',
        'KeySchema': [
            {
                'AttributeName': 'string',
                'KeyType': 'HASH'|'RANGE'
            },
        ],
        'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
        'CreationDateTime': datetime(2015, 1, 1),
        'ProvisionedThroughput': {
            'LastIncreaseDateTime': datetime(2015, 1, 1),
            'LastDecreaseDateTime': datetime(2015, 1, 1),
            'NumberOfDecreasesToday': 123,
            'ReadCapacityUnits': 123,
            'WriteCapacityUnits': 123
        },
        'TableSizeBytes': 123,
        'ItemCount': 123,
        'TableArn': 'string',
        'TableId': 'string',
        'BillingModeSummary': {
            'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
            'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
        },
        'LocalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexArn': 'string'
            },
        ],
        'GlobalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                'Backfilling': True|False,
                'ProvisionedThroughput': {
                    'LastIncreaseDateTime': datetime(2015, 1, 1),
                    'LastDecreaseDateTime': datetime(2015, 1, 1),
                    'NumberOfDecreasesToday': 123,
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexArn': 'string'
            },
        ],
        'StreamSpecification': {
            'StreamEnabled': True|False,
            'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
        },
        'LatestStreamLabel': 'string',
        'LatestStreamArn': 'string',
        'GlobalTableVersion': 'string',
        'Replicas': [
            {
                'RegionName': 'string',
                'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                'ReplicaStatusDescription': 'string',
                'ReplicaStatusPercentProgress': 'string',
                'KMSMasterKeyId': 'string',
                'ProvisionedThroughputOverride': {
                    'ReadCapacityUnits': 123
                },
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'ProvisionedThroughputOverride': {
                            'ReadCapacityUnits': 123
                        }
                    },
                ]
            },
        ],
        'RestoreSummary': {
            'SourceBackupArn': 'string',
            'SourceTableArn': 'string',
            'RestoreDateTime': datetime(2015, 1, 1),
            'RestoreInProgress': True|False
        },
        'SSEDescription': {
            'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
            'SSEType': 'AES256'|'KMS',
            'KMSMasterKeyArn': 'string',
            'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
        },
        'ArchivalSummary': {
            'ArchivalDateTime': datetime(2015, 1, 1),
            'ArchivalReason': 'string',
            'ArchivalBackupArn': 'string'
        }
    }
}


Response Structure

(dict) --

TableDescription (dict) --
Represents the properties of a table.

AttributeDefinitions (list) --
An array of AttributeDefinition objects. Each of these objects describes one attribute in the table and index key schema.
Each AttributeDefinition object in this array is composed of:

AttributeName - The name of the attribute.
AttributeType - The data type for the attribute.


(dict) --
Represents an attribute for describing the key schema for the table and indexes.

AttributeName (string) --
A name for the attribute.

AttributeType (string) --
The data type for the attribute, where:

S - the attribute is of type String
N - the attribute is of type Number
B - the attribute is of type Binary






TableName (string) --
The name of the table.

KeySchema (list) --
The primary key structure for the table. Each KeySchemaElement consists of:

AttributeName - The name of the attribute.
KeyType - The role of the attribute:
HASH - partition key
RANGE - sort key




Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

For more information about primary keys, see Primary Key in the Amazon DynamoDB Developer Guide .

(dict) --
Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --
The name of a key attribute.

KeyType (string) --
The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






TableStatus (string) --
The current state of the table:

CREATING - The table is being created.
UPDATING - The table is being updated.
DELETING - The table is being deleted.
ACTIVE - The table is ready for use.
INACCESSIBLE_ENCRYPTION_CREDENTIALS - The AWS KMS key used to encrypt the table in inaccessible. Table operations may fail due to failure to use the AWS KMS key. DynamoDB will initiate the table archival process when a table\'s AWS KMS key remains inaccessible for more than seven days.
ARCHIVING - The table is being archived. Operations are not allowed until archival is complete.
ARCHIVED - The table has been archived. See the ArchivalReason for more information.


CreationDateTime (datetime) --
The date and time when the table was created, in UNIX epoch time format.

ProvisionedThroughput (dict) --
The provisioned throughput settings for the table, consisting of read and write capacity units, along with data about increases and decreases.

LastIncreaseDateTime (datetime) --
The date and time of the last provisioned throughput increase for this table.

LastDecreaseDateTime (datetime) --
The date and time of the last provisioned throughput decrease for this table.

NumberOfDecreasesToday (integer) --
The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see Limits in the Amazon DynamoDB Developer Guide .

ReadCapacityUnits (integer) --
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 ReadCapacityUnits per second provides 100 eventually consistent ReadCapacityUnits per second.

WriteCapacityUnits (integer) --
The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException .



TableSizeBytes (integer) --
The total size of the specified table, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --
The number of items in the specified table. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

TableArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the table.

TableId (string) --
Unique identifier for the table for which the backup was created.

BillingModeSummary (dict) --
Contains the details for the read/write capacity mode.

BillingMode (string) --
Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.

PROVISIONED - Sets the read/write capacity mode to PROVISIONED . We recommend using PROVISIONED for predictable workloads.
PAY_PER_REQUEST - Sets the read/write capacity mode to PAY_PER_REQUEST . We recommend using PAY_PER_REQUEST for unpredictable workloads.


LastUpdateToPayPerRequestDateTime (datetime) --
Represents the time when PAY_PER_REQUEST was last set as the read/write capacity mode.



LocalSecondaryIndexes (list) --
Represents one or more local secondary indexes on the table. Each index is scoped to a given partition key value. Tables with one or more local secondary indexes are subject to an item collection size limit, where the amount of data within a given item collection cannot exceed 10 GB. Each element is composed of:

IndexName - The name of the local secondary index.
KeySchema - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
Projection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
ProjectionType - One of the following:
KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes , summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.


IndexSizeBytes - Represents the total size of the index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
ItemCount - Represents the number of items in the index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

If the table is in the DELETING state, no information about indexes will be returned.

(dict) --
Represents the properties of a local secondary index.

IndexName (string) --
Represents the name of the local secondary index.

KeySchema (list) --
The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --
Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --
The name of a key attribute.

KeyType (string) --
The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --
Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --
The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --
Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --




IndexSizeBytes (integer) --
The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --
The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

IndexArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the index.





GlobalSecondaryIndexes (list) --
The global secondary indexes, if any, on the table. Each index is scoped to a given partition key value. Each element is composed of:

Backfilling - If true, then the index is currently in the backfilling phase. Backfilling occurs only when a new global secondary index is added to the table. It is the process by which DynamoDB populates the new index with data from the table. (This attribute does not appear for indexes that were created during a CreateTable operation.)  You can delete an index that is being created during the Backfilling phase when IndexStatus is set to CREATING and Backfilling is true. You can\'t delete the index that is being created when IndexStatus is set to CREATING and Backfilling is false. (This attribute does not appear for indexes that were created during a CreateTable operation.)
IndexName - The name of the global secondary index.
IndexSizeBytes - The total size of the global secondary index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
IndexStatus - The current status of the global secondary index:
CREATING - The index is being created.
UPDATING - The index is being updated.
DELETING - The index is being deleted.
ACTIVE - The index is ready for use.


ItemCount - The number of items in the global secondary index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
KeySchema - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
Projection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
ProjectionType - One of the following:
KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes , summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.


ProvisionedThroughput - The provisioned throughput settings for the global secondary index, consisting of read and write capacity units, along with data about increases and decreases.

If the table is in the DELETING state, no information about indexes will be returned.

(dict) --
Represents the properties of a global secondary index.

IndexName (string) --
The name of the global secondary index.

KeySchema (list) --
The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --
Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --
The name of a key attribute.

KeyType (string) --
The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --
Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --
The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --
Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --




IndexStatus (string) --
The current state of the global secondary index:

CREATING - The index is being created.
UPDATING - The index is being updated.
DELETING - The index is being deleted.
ACTIVE - The index is ready for use.


Backfilling (boolean) --
Indicates whether the index is currently backfilling. Backfilling is the process of reading items from the table and determining whether they can be added to the index. (Not all items will qualify: For example, a partition key cannot have any duplicate values.) If an item can be added to the index, DynamoDB will do so. After all items have been processed, the backfilling operation is complete and Backfilling is false.
You can delete an index that is being created during the Backfilling phase when IndexStatus is set to CREATING and Backfilling is true. You can\'t delete the index that is being created when IndexStatus is set to CREATING and Backfilling is false.

Note
For indexes that were created during a CreateTable operation, the Backfilling attribute does not appear in the DescribeTable output.


ProvisionedThroughput (dict) --
Represents the provisioned throughput settings for the specified global secondary index.
For current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .

LastIncreaseDateTime (datetime) --
The date and time of the last provisioned throughput increase for this table.

LastDecreaseDateTime (datetime) --
The date and time of the last provisioned throughput decrease for this table.

NumberOfDecreasesToday (integer) --
The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see Limits in the Amazon DynamoDB Developer Guide .

ReadCapacityUnits (integer) --
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 ReadCapacityUnits per second provides 100 eventually consistent ReadCapacityUnits per second.

WriteCapacityUnits (integer) --
The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException .



IndexSizeBytes (integer) --
The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --
The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

IndexArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the index.





StreamSpecification (dict) --
The current DynamoDB Streams configuration for the table.

StreamEnabled (boolean) --
Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.

StreamViewType (string) --
When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are:

KEYS_ONLY - Only the key attributes of the modified item are written to the stream.
NEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.
OLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.
NEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream.




LatestStreamLabel (string) --
A timestamp, in ISO 8601 format, for this stream.
Note that LatestStreamLabel is not a unique identifier for the stream, because it is possible that a stream from another table might have the same timestamp. However, the combination of the following three elements is guaranteed to be unique:

AWS customer ID
Table name
StreamLabel


LatestStreamArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the latest stream for this table.

GlobalTableVersion (string) --
Represents the version of global tables in use, if the table is replicated across AWS Regions.

Replicas (list) --
Represents replicas of the table.

(dict) --
Contains the details of the replica.

RegionName (string) --
The name of the Region.

ReplicaStatus (string) --
The current state of the replica:

CREATING - The replica is being created.
UPDATING - The replica is being updated.
DELETING - The replica is being deleted.
ACTIVE - The replica is ready for use.


ReplicaStatusDescription (string) --
Detailed information about the replica status.

ReplicaStatusPercentProgress (string) --
Specifies the progress of a Create, Update, or Delete action on the replica as a percentage.

KMSMasterKeyId (string) --
The AWS KMS customer master key (CMK) of the replica that will be used for AWS KMS encryption.

ProvisionedThroughputOverride (dict) --
Replica-specific provisioned throughput. If not described, uses the source table\'s provisioned throughput settings.

ReadCapacityUnits (integer) --
Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.



GlobalSecondaryIndexes (list) --
Replica-specific global secondary index settings.

(dict) --
Represents the properties of a replica global secondary index.

IndexName (string) --
The name of the global secondary index.

ProvisionedThroughputOverride (dict) --
If not described, uses the source table GSI\'s read capacity settings.

ReadCapacityUnits (integer) --
Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.











RestoreSummary (dict) --
Contains details for the restore.

SourceBackupArn (string) --
The Amazon Resource Name (ARN) of the backup from which the table was restored.

SourceTableArn (string) --
The ARN of the source table of the backup that is being restored.

RestoreDateTime (datetime) --
Point in time or source backup time.

RestoreInProgress (boolean) --
Indicates if a restore is in progress or not.



SSEDescription (dict) --
The description of the server-side encryption status on the specified table.

Status (string) --
Represents the current state of server-side encryption. The only supported values are:

ENABLED - Server-side encryption is enabled.
UPDATING - Server-side encryption is being updated.


SSEType (string) --
Server-side encryption type. The only supported value is:

KMS - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).


KMSMasterKeyArn (string) --
The AWS KMS customer master key (CMK) ARN used for the AWS KMS encryption.

InaccessibleEncryptionDateTime (datetime) --
Indicates the time, in UNIX epoch date format, when DynamoDB detected that the table\'s AWS KMS key was inaccessible. This attribute will automatically be cleared when DynamoDB detects that the table\'s AWS KMS key is accessible again. DynamoDB will initiate the table archival process when table\'s AWS KMS key remains inaccessible for more than seven days from this date.



ArchivalSummary (dict) --
Contains information about the table archive.

ArchivalDateTime (datetime) --
The date and time when table archival was initiated by DynamoDB, in UNIX epoch time format.

ArchivalReason (string) --
The reason DynamoDB archived the table. Currently, the only possible value is:

INACCESSIBLE_ENCRYPTION_CREDENTIALS - The table was archived due to the table\'s AWS KMS key being inaccessible for more than seven days. An On-Demand backup was created at the archival time.


ArchivalBackupArn (string) --
The Amazon Resource Name (ARN) of the backup the table was archived to, when applicable in the archival reason. If you wish to restore this backup to the same table name, you will need to delete the original table.











Exceptions

DynamoDB.Client.exceptions.TableAlreadyExistsException
DynamoDB.Client.exceptions.TableNotFoundException
DynamoDB.Client.exceptions.TableInUseException
DynamoDB.Client.exceptions.LimitExceededException
DynamoDB.Client.exceptions.InvalidRestoreTimeException
DynamoDB.Client.exceptions.PointInTimeRecoveryUnavailableException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'TableDescription': {
            'AttributeDefinitions': [
                {
                    'AttributeName': 'string',
                    'AttributeType': 'S'|'N'|'B'
                },
            ],
            'TableName': 'string',
            'KeySchema': [
                {
                    'AttributeName': 'string',
                    'KeyType': 'HASH'|'RANGE'
                },
            ],
            'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
            'CreationDateTime': datetime(2015, 1, 1),
            'ProvisionedThroughput': {
                'LastIncreaseDateTime': datetime(2015, 1, 1),
                'LastDecreaseDateTime': datetime(2015, 1, 1),
                'NumberOfDecreasesToday': 123,
                'ReadCapacityUnits': 123,
                'WriteCapacityUnits': 123
            },
            'TableSizeBytes': 123,
            'ItemCount': 123,
            'TableArn': 'string',
            'TableId': 'string',
            'BillingModeSummary': {
                'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
                'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
            },
            'LocalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'IndexSizeBytes': 123,
                    'ItemCount': 123,
                    'IndexArn': 'string'
                },
            ],
            'GlobalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                    'Backfilling': True|False,
                    'ProvisionedThroughput': {
                        'LastIncreaseDateTime': datetime(2015, 1, 1),
                        'LastDecreaseDateTime': datetime(2015, 1, 1),
                        'NumberOfDecreasesToday': 123,
                        'ReadCapacityUnits': 123,
                        'WriteCapacityUnits': 123
                    },
                    'IndexSizeBytes': 123,
                    'ItemCount': 123,
                    'IndexArn': 'string'
                },
            ],
            'StreamSpecification': {
                'StreamEnabled': True|False,
                'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
            },
            'LatestStreamLabel': 'string',
            'LatestStreamArn': 'string',
            'GlobalTableVersion': 'string',
            'Replicas': [
                {
                    'RegionName': 'string',
                    'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                    'ReplicaStatusDescription': 'string',
                    'ReplicaStatusPercentProgress': 'string',
                    'KMSMasterKeyId': 'string',
                    'ProvisionedThroughputOverride': {
                        'ReadCapacityUnits': 123
                    },
                    'GlobalSecondaryIndexes': [
                        {
                            'IndexName': 'string',
                            'ProvisionedThroughputOverride': {
                                'ReadCapacityUnits': 123
                            }
                        },
                    ]
                },
            ],
            'RestoreSummary': {
                'SourceBackupArn': 'string',
                'SourceTableArn': 'string',
                'RestoreDateTime': datetime(2015, 1, 1),
                'RestoreInProgress': True|False
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
                'SSEType': 'AES256'|'KMS',
                'KMSMasterKeyArn': 'string',
                'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
            },
            'ArchivalSummary': {
                'ArchivalDateTime': datetime(2015, 1, 1),
                'ArchivalReason': 'string',
                'ArchivalBackupArn': 'string'
            }
        }
    }
    
    
    :returns: 
    Auto scaling policies
    IAM policies
    Amazon CloudWatch metrics and alarms
    Tags
    Stream settings
    Time to Live (TTL) settings
    Point in time recovery settings
    
    """
    pass

def scan(TableName=None, IndexName=None, AttributesToGet=None, Limit=None, Select=None, ScanFilter=None, ConditionalOperator=None, ExclusiveStartKey=None, ReturnConsumedCapacity=None, TotalSegments=None, Segment=None, ProjectionExpression=None, FilterExpression=None, ExpressionAttributeNames=None, ExpressionAttributeValues=None, ConsistentRead=None):
    """
    The Scan operation returns one or more items and item attributes by accessing every item in a table or a secondary index. To have DynamoDB return fewer items, you can provide a FilterExpression operation.
    If the total number of scanned items exceeds the maximum dataset size limit of 1 MB, the scan stops and results are returned to the user as a LastEvaluatedKey value to continue the scan in a subsequent operation. The results also include the number of items exceeding the limit. A scan can result in no table data meeting the filter criteria.
    A single Scan operation reads up to the maximum number of items set (if using the Limit parameter) or a maximum of 1 MB of data and then apply any filtering to the results using FilterExpression . If LastEvaluatedKey is present in the response, you need to paginate the result set. For more information, see Paginating the Results in the Amazon DynamoDB Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example scans the entire Music table, and then narrows the results to songs by the artist "No One You Know". For each item, only the album title and song title are returned.
    Expected Output:
    
    :example: response = client.scan(
        TableName='string',
        IndexName='string',
        AttributesToGet=[
            'string',
        ],
        Limit=123,
        Select='ALL_ATTRIBUTES'|'ALL_PROJECTED_ATTRIBUTES'|'SPECIFIC_ATTRIBUTES'|'COUNT',
        ScanFilter={
            'string': {
                'AttributeValueList': [
                    {
                        'S': 'string',
                        'N': 'string',
                        'B': b'bytes',
                        'SS': [
                            'string',
                        ],
                        'NS': [
                            'string',
                        ],
                        'BS': [
                            b'bytes',
                        ],
                        'M': {
                            'string': {'... recursive ...'}
                        },
                        'L': [
                            {'... recursive ...'},
                        ],
                        'NULL': True|False,
                        'BOOL': True|False
                    },
                ],
                'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH'
            }
        },
        ConditionalOperator='AND'|'OR',
        ExclusiveStartKey={
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
        TotalSegments=123,
        Segment=123,
        ProjectionExpression='string',
        FilterExpression='string',
        ExpressionAttributeNames={
            'string': 'string'
        },
        ExpressionAttributeValues={
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        ConsistentRead=True|False
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table containing the requested items; or, if you provide IndexName , the name of the table to which that index belongs.\n

    :type IndexName: string
    :param IndexName: The name of a secondary index to scan. This index can be any local secondary index or global secondary index. Note that if you use the IndexName parameter, you must also provide TableName .

    :type AttributesToGet: list
    :param AttributesToGet: This is a legacy parameter. Use ProjectionExpression instead. For more information, see AttributesToGet in the Amazon DynamoDB Developer Guide .\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of items to evaluate (not necessarily the number of matching items). If DynamoDB processes the number of items up to the limit while processing the results, it stops the operation and returns the matching values up to that point, and a key in LastEvaluatedKey to apply in a subsequent operation, so that you can pick up where you left off. Also, if the processed dataset size exceeds 1 MB before DynamoDB reaches this limit, it stops the operation and returns the matching values up to the limit, and a key in LastEvaluatedKey to apply in a subsequent operation to continue the operation. For more information, see Working with Queries in the Amazon DynamoDB Developer Guide .

    :type Select: string
    :param Select: The attributes to be returned in the result. You can retrieve all item attributes, specific item attributes, the count of matching items, or in the case of an index, some or all of the attributes projected into the index.\n\nALL_ATTRIBUTES - Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index, DynamoDB fetches the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required.\nALL_PROJECTED_ATTRIBUTES - Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying ALL_ATTRIBUTES .\nCOUNT - Returns the number of matching items, rather than the matching items themselves.\nSPECIFIC_ATTRIBUTES - Returns only the attributes listed in AttributesToGet . This return value is equivalent to specifying AttributesToGet without specifying any value for Select . If you query or scan a local secondary index and request only attributes that are projected into that index, the operation reads only the index and not the table. If any of the requested attributes are not projected into the local secondary index, DynamoDB fetches each of these attributes from the parent table. This extra fetching incurs additional throughput cost and latency. If you query or scan a global secondary index, you can only request attributes that are projected into the index. Global secondary index queries cannot fetch attributes from the parent table.\n\nIf neither Select nor AttributesToGet are specified, DynamoDB defaults to ALL_ATTRIBUTES when accessing a table, and ALL_PROJECTED_ATTRIBUTES when accessing an index. You cannot use both Select and AttributesToGet together in a single request, unless the value for Select is SPECIFIC_ATTRIBUTES . (This usage is equivalent to specifying AttributesToGet without any value for Select .)\n\nNote\nIf you use the ProjectionExpression parameter, then the value for Select can only be SPECIFIC_ATTRIBUTES . Any other value for Select will return an error.\n\n

    :type ScanFilter: dict
    :param ScanFilter: This is a legacy parameter. Use FilterExpression instead. For more information, see ScanFilter in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(dict) --Represents the selection criteria for a Query or Scan operation:\n\nFor a Query operation, Condition is used for specifying the KeyConditions to use when querying a table or an index. For KeyConditions , only the following comparison operators are supported: EQ | LE | LT | GE | GT | BEGINS_WITH | BETWEEN Condition is also used in a QueryFilter , which evaluates the query results and returns only the desired values.\nFor a Scan operation, Condition is used in a ScanFilter , which evaluates the scan results and returns only the desired values.\n\n\nAttributeValueList (list) --One or more values to evaluate against the supplied attribute. The number of values in the list depends on the ComparisonOperator being used.\nFor type Number, value comparisons are numeric.\nString value comparisons for greater than, equals, or less than are based on ASCII character code values. For example, a is greater than A , and a is greater than B . For a list of code values, see http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters .\nFor Binary, DynamoDB treats each byte of the binary data as unsigned when it compares binary values.\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\nComparisonOperator (string) -- [REQUIRED]A comparator for evaluating attributes. For example, equals, greater than, less than, etc.\nThe following comparison operators are available:\n\nEQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS | NOT_CONTAINS | BEGINS_WITH | IN | BETWEEN\nThe following are descriptions of each comparison operator.\n\nEQ : Equal. EQ is supported for all data types, including lists and maps. AttributeValueList can contain only one AttributeValue element of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not equal {'NS':['6', '2', '1']} .\nNE : Not equal. NE is supported for all data types, including lists and maps. AttributeValueList can contain only one AttributeValue of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an AttributeValue of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not equal {'NS':['6', '2', '1']} .\nLE : Less than or equal.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nLT : Less than.  AttributeValueList can contain only one AttributeValue of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nGE : Greater than or equal.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nGT : Greater than.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nNOT_NULL : The attribute exists. NOT_NULL is supported for all data types, including lists and maps.\n\n\nNote\nThis operator tests for the existence of an attribute, not its data type. If the data type of attribute 'a ' is null, and you evaluate it using NOT_NULL , the result is a Boolean true . This result is because the attribute 'a ' exists; its data type is not relevant to the NOT_NULL comparison operator.\n\n\nNULL : The attribute does not exist. NULL is supported for all data types, including lists and maps.\n\n\nNote\nThis operator tests for the nonexistence of an attribute, not its data type. If the data type of attribute 'a ' is null, and you evaluate it using NULL , the result is a Boolean false . This is because the attribute 'a ' exists; its data type is not relevant to the NULL comparison operator.\n\n\nCONTAINS : Checks for a subsequence, or value in a set. AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is of type String, then the operator checks for a substring match. If the target attribute of the comparison is of type Binary, then the operator looks for a subsequence of the target that matches the input. If the target attribute of the comparison is a set ('SS ', 'NS ', or 'BS '), then the operator evaluates to true if it finds an exact match with any member of the set. CONTAINS is supported for lists: When evaluating 'a CONTAINS b ', 'a ' can be a list; however, 'b ' cannot be a set, a map, or a list.\nNOT_CONTAINS : Checks for absence of a subsequence, or absence of a value in a set. AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is a String, then the operator checks for the absence of a substring match. If the target attribute of the comparison is Binary, then the operator checks for the absence of a subsequence of the target that matches the input. If the target attribute of the comparison is a set ('SS ', 'NS ', or 'BS '), then the operator evaluates to true if it does not find an exact match with any member of the set. NOT_CONTAINS is supported for lists: When evaluating 'a NOT CONTAINS b ', 'a ' can be a list; however, 'b ' cannot be a set, a map, or a list.\nBEGINS_WITH : Checks for a prefix.  AttributeValueList can contain only one AttributeValue of type String or Binary (not a Number or a set type). The target attribute of the comparison must be of type String or Binary (not a Number or a set type).\nIN : Checks for matching elements in a list. AttributeValueList can contain one or more AttributeValue elements of type String, Number, or Binary. These attributes are compared against an existing attribute of an item. If any elements of the input are equal to the item attribute, the expression evaluates to true.\nBETWEEN : Greater than or equal to the first value, and less than or equal to the second value.  AttributeValueList must contain two AttributeValue elements of the same type, either String, Number, or Binary (not a set type). A target attribute matches if the target value is greater than, or equal to, the first element and less than, or equal to, the second element. If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not compare to {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']}\n\nFor usage examples of AttributeValueList and ComparisonOperator , see Legacy Conditional Parameters in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\n\n

    :type ConditionalOperator: string
    :param ConditionalOperator: This is a legacy parameter. Use FilterExpression instead. For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide .

    :type ExclusiveStartKey: dict
    :param ExclusiveStartKey: The primary key of the first item that this operation will evaluate. Use the value that was returned for LastEvaluatedKey in the previous operation.\nThe data type for ExclusiveStartKey must be String, Number or Binary. No set data types are allowed.\nIn a parallel scan, a Scan request that includes ExclusiveStartKey must specify the same segment whose previous Scan returned the corresponding value of LastEvaluatedKey .\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n

    :type ReturnConsumedCapacity: string
    :param ReturnConsumedCapacity: Determines the level of detail about provisioned throughput consumption that is returned in the response:\n\nINDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem , do not access any indexes at all. In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s).\nTOTAL - The response includes only the aggregate ConsumedCapacity for the operation.\nNONE - No ConsumedCapacity details are included in the response.\n\n

    :type TotalSegments: integer
    :param TotalSegments: For a parallel Scan request, TotalSegments represents the total number of segments into which the Scan operation will be divided. The value of TotalSegments corresponds to the number of application workers that will perform the parallel scan. For example, if you want to use four application threads to scan a table or an index, specify a TotalSegments value of 4.\nThe value for TotalSegments must be greater than or equal to 1, and less than or equal to 1000000. If you specify a TotalSegments value of 1, the Scan operation will be sequential rather than parallel.\nIf you specify TotalSegments , you must also specify Segment .\n

    :type Segment: integer
    :param Segment: For a parallel Scan request, Segment identifies an individual segment to be scanned by an application worker.\nSegment IDs are zero-based, so the first segment is always 0. For example, if you want to use four application threads to scan a table or an index, then the first thread specifies a Segment value of 0, the second thread specifies 1, and so on.\nThe value of LastEvaluatedKey returned from a parallel Scan request must be used as ExclusiveStartKey with the same segment ID in a subsequent Scan operation.\nThe value for Segment must be greater than or equal to 0, and less than the value provided for TotalSegments .\nIf you provide Segment , you must also provide TotalSegments .\n

    :type ProjectionExpression: string
    :param ProjectionExpression: A string that identifies one or more attributes to retrieve from the specified table or index. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.\nIf no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result.\nFor more information, see Specifying Item Attributes in the Amazon DynamoDB Developer Guide .\n

    :type FilterExpression: string
    :param FilterExpression: A string that contains conditions that DynamoDB applies after the Scan operation, but before the data is returned to you. Items that do not satisfy the FilterExpression criteria are not returned.\n\nNote\nA FilterExpression is applied after the items have already been read; the process of filtering does not consume any additional read capacity units.\n\nFor more information, see Filter Expressions in the Amazon DynamoDB Developer Guide .\n

    :type ExpressionAttributeNames: dict
    :param ExpressionAttributeNames: One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames :\n\nTo access an attribute whose name conflicts with a DynamoDB reserved word.\nTo create a placeholder for repeating occurrences of an attribute name in an expression.\nTo prevent special characters in an attribute name from being misinterpreted in an expression.\n\nUse the # character in an expression to dereference an attribute name. For example, consider the following attribute name:\n\nPercentile\n\nThe name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide ). To work around this, you could specify the following for ExpressionAttributeNames :\n\n{'#P':'Percentile'}\n\nYou could then use this substitution in an expression, as in this example:\n\n#P = :val\n\n\nNote\nTokens that begin with the : character are expression attribute values , which are placeholders for the actual value at runtime.\n\nFor more information on expression attribute names, see Specifying Item Attributes in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type ExpressionAttributeValues: dict
    :param ExpressionAttributeValues: One or more values that can be substituted in an expression.\nUse the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:\n\nAvailable | Backordered | Discontinued\nYou would first need to specify ExpressionAttributeValues as follows:\n\n{ ':avail':{'S':'Available'}, ':back':{'S':'Backordered'}, ':disc':{'S':'Discontinued'} }\nYou could then use these values in an expression, such as this:\n\nProductStatus IN (:avail, :back, :disc)\nFor more information on expression attribute values, see Condition Expressions in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n

    :type ConsistentRead: boolean
    :param ConsistentRead: A Boolean value that determines the read consistency model during the scan:\n\nIf ConsistentRead is false , then the data returned from Scan might not contain the results from other recently completed write operations (PutItem , UpdateItem , or DeleteItem ).\nIf ConsistentRead is true , then all of the write operations that completed before the Scan began are guaranteed to be contained in the Scan response.\n\nThe default setting for ConsistentRead is false .\nThe ConsistentRead parameter is not supported on global secondary indexes. If you scan a global secondary index with ConsistentRead set to true, you will receive a ValidationException .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
    ],
    'Count': 123,
    'ScannedCount': 123,
    'LastEvaluatedKey': {
        'string': {
            'S': 'string',
            'N': 'string',
            'B': b'bytes',
            'SS': [
                'string',
            ],
            'NS': [
                'string',
            ],
            'BS': [
                b'bytes',
            ],
            'M': {
                'string': {'... recursive ...'}
            },
            'L': [
                {'... recursive ...'},
            ],
            'NULL': True|False,
            'BOOL': True|False
        }
    },
    'ConsumedCapacity': {
        'TableName': 'string',
        'CapacityUnits': 123.0,
        'ReadCapacityUnits': 123.0,
        'WriteCapacityUnits': 123.0,
        'Table': {
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'CapacityUnits': 123.0
        },
        'LocalSecondaryIndexes': {
            'string': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            }
        },
        'GlobalSecondaryIndexes': {
            'string': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            }
        }
    }
}


Response Structure

(dict) --
Represents the output of a Scan operation.

Items (list) --
An array of item attributes that match the scan criteria. Each element in this array consists of an attribute name and the value for that attribute.

(dict) --

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true










Count (integer) --
The number of items in the response.
If you set ScanFilter in the request, then Count is the number of items returned after the filter was applied, and ScannedCount is the number of matching items before the filter was applied.
If you did not use a filter in the request, then Count is the same as ScannedCount .

ScannedCount (integer) --
The number of items evaluated, before any ScanFilter is applied. A high ScannedCount value with few, or no, Count results indicates an inefficient Scan operation. For more information, see Count and ScannedCount in the Amazon DynamoDB Developer Guide .
If you did not use a filter in the request, then ScannedCount is the same as Count .

LastEvaluatedKey (dict) --
The primary key of the item where the operation stopped, inclusive of the previous result set. Use this value to start a new operation, excluding this value in the new request.
If LastEvaluatedKey is empty, then the "last page" of results has been processed and there is no more data to be retrieved.
If LastEvaluatedKey is not empty, it does not necessarily mean that there is more data in the result set. The only way to know when you have reached the end of the result set is when LastEvaluatedKey is empty.

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true








ConsumedCapacity (dict) --
The capacity units consumed by the Scan operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. ConsumedCapacity is only returned if the ReturnConsumedCapacity parameter was specified. For more information, see Provisioned Throughput in the Amazon DynamoDB Developer Guide .

TableName (string) --
The name of the table that was affected by the operation.

CapacityUnits (float) --
The total number of capacity units consumed by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed by the operation.

WriteCapacityUnits (float) --
The total number of write capacity units consumed by the operation.

Table (dict) --
The amount of throughput consumed on the table affected by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.



LocalSecondaryIndexes (dict) --
The amount of throughput consumed on each local index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.







GlobalSecondaryIndexes (dict) --
The amount of throughput consumed on each global index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.















Exceptions

DynamoDB.Client.exceptions.ProvisionedThroughputExceededException
DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.RequestLimitExceeded
DynamoDB.Client.exceptions.InternalServerError

Examples
This example scans the entire Music table, and then narrows the results to songs by the artist "No One You Know". For each item, only the album title and song title are returned.
response = client.scan(
    ExpressionAttributeNames={
        'AT': 'AlbumTitle',
        'ST': 'SongTitle',
    },
    ExpressionAttributeValues={
        ':a': {
            'S': 'No One You Know',
        },
    },
    FilterExpression='Artist = :a',
    ProjectionExpression='#ST, #AT',
    TableName='Music',
)

print(response)


Expected Output:
{
    'ConsumedCapacity': {
    },
    'Count': 2,
    'Items': [
        {
            'AlbumTitle': {
                'S': 'Somewhat Famous',
            },
            'SongTitle': {
                'S': 'Call Me Today',
            },
        },
        {
            'AlbumTitle': {
                'S': 'Blue Sky Blues',
            },
            'SongTitle': {
                'S': 'Scared of My Shadow',
            },
        },
    ],
    'ScannedCount': 3,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Items': [
            {
                'string': {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                }
            },
        ],
        'Count': 123,
        'ScannedCount': 123,
        'LastEvaluatedKey': {
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        'ConsumedCapacity': {
            'TableName': 'string',
            'CapacityUnits': 123.0,
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'Table': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            },
            'LocalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            },
            'GlobalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Associate a set of tags with an Amazon DynamoDB resource. You can then activate these user-defined tags so that they appear on the Billing and Cost Management console for cost allocation tracking. You can call TagResource up to five times per second, per account.
    For an overview on tagging DynamoDB resources, see Tagging for DynamoDB in the Amazon DynamoDB Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nIdentifies the Amazon DynamoDB resource to which tags should be added. This value is an Amazon Resource Name (ARN).\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags to be assigned to the Amazon DynamoDB resource.\n\n(dict) --Describes a tag. A tag is a key-value pair. You can add up to 50 tags to a single DynamoDB table.\nAWS-assigned tag names and values are automatically assigned the aws: prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix user: in the Cost Allocation Report. You cannot backdate the application of a tag.\nFor an overview on tagging DynamoDB resources, see Tagging for DynamoDB in the Amazon DynamoDB Developer Guide .\n\nKey (string) -- [REQUIRED]The key of the tag. Tag keys are case sensitive. Each DynamoDB table can only have up to one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.\n\nValue (string) -- [REQUIRED]The value of the tag. Tag values are case-sensitive and can be null.\n\n\n\n\n

    :returns: 
    DynamoDB.Client.exceptions.LimitExceededException
    DynamoDB.Client.exceptions.ResourceNotFoundException
    DynamoDB.Client.exceptions.InternalServerError
    DynamoDB.Client.exceptions.ResourceInUseException
    
    """
    pass

def transact_get_items(TransactItems=None, ReturnConsumedCapacity=None):
    """
    DynamoDB rejects the entire TransactGetItems request if any of the following is true:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.transact_get_items(
        TransactItems=[
            {
                'Get': {
                    'Key': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                    'TableName': 'string',
                    'ProjectionExpression': 'string',
                    'ExpressionAttributeNames': {
                        'string': 'string'
                    }
                }
            },
        ],
        ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE'
    )
    
    
    :type TransactItems: list
    :param TransactItems: [REQUIRED]\nAn ordered array of up to 25 TransactGetItem objects, each of which contains a Get structure.\n\n(dict) --Specifies an item to be retrieved as part of the transaction.\n\nGet (dict) -- [REQUIRED]Contains the primary key that identifies the item to get, together with the name of the table that contains the item, and optionally the specific attributes of the item to retrieve.\n\nKey (dict) -- [REQUIRED]A map of attribute names to AttributeValue objects that specifies the primary key of the item to retrieve.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\nTableName (string) -- [REQUIRED]The name of the table from which to retrieve the specified item.\n\nProjectionExpression (string) --A string that identifies one or more attributes of the specified item to retrieve from the table. The attributes in the expression must be separated by commas. If no attribute names are specified, then all attributes of the specified item are returned. If any of the requested attributes are not found, they do not appear in the result.\n\nExpressionAttributeNames (dict) --One or more substitution tokens for attribute names in the ProjectionExpression parameter.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\n\n

    :type ReturnConsumedCapacity: string
    :param ReturnConsumedCapacity: A value of TOTAL causes consumed capacity information to be returned, and a value of NONE prevents that information from being returned. No other value is valid.

    :rtype: dict

ReturnsResponse Syntax
{
    'ConsumedCapacity': [
        {
            'TableName': 'string',
            'CapacityUnits': 123.0,
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'Table': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            },
            'LocalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            },
            'GlobalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            }
        },
    ],
    'Responses': [
        {
            'Item': {
                'string': {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                }
            }
        },
    ]
}


Response Structure

(dict) --

ConsumedCapacity (list) --
If the ReturnConsumedCapacity value was TOTAL , this is an array of ConsumedCapacity objects, one for each table addressed by TransactGetItem objects in the TransactItems parameter. These ConsumedCapacity objects report the read-capacity units consumed by the TransactGetItems call in that table.

(dict) --
The capacity units consumed by an operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. ConsumedCapacity is only returned if the request asked for it. For more information, see Provisioned Throughput in the Amazon DynamoDB Developer Guide .

TableName (string) --
The name of the table that was affected by the operation.

CapacityUnits (float) --
The total number of capacity units consumed by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed by the operation.

WriteCapacityUnits (float) --
The total number of write capacity units consumed by the operation.

Table (dict) --
The amount of throughput consumed on the table affected by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.



LocalSecondaryIndexes (dict) --
The amount of throughput consumed on each local index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.







GlobalSecondaryIndexes (dict) --
The amount of throughput consumed on each global index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.











Responses (list) --
An ordered array of up to 25 ItemResponse objects, each of which corresponds to the TransactGetItem object in the same position in the TransactItems array. Each ItemResponse object contains a Map of the name-value pairs that are the projected attributes of the requested item.
If a requested item could not be retrieved, the corresponding ItemResponse object is Null, or if the requested item has no projected attributes, the corresponding ItemResponse object is an empty Map.

(dict) --
Details for the requested item.

Item (dict) --
Map of attribute data consisting of the data type and attribute value.

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true


















Exceptions

DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.TransactionCanceledException
DynamoDB.Client.exceptions.ProvisionedThroughputExceededException
DynamoDB.Client.exceptions.RequestLimitExceeded
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'ConsumedCapacity': [
            {
                'TableName': 'string',
                'CapacityUnits': 123.0,
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'Table': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                },
                'LocalSecondaryIndexes': {
                    'string': {
                        'ReadCapacityUnits': 123.0,
                        'WriteCapacityUnits': 123.0,
                        'CapacityUnits': 123.0
                    }
                },
                'GlobalSecondaryIndexes': {
                    'string': {
                        'ReadCapacityUnits': 123.0,
                        'WriteCapacityUnits': 123.0,
                        'CapacityUnits': 123.0
                    }
                }
            },
        ],
        'Responses': [
            {
                'Item': {
                    'string': {
                        'S': 'string',
                        'N': 'string',
                        'B': b'bytes',
                        'SS': [
                            'string',
                        ],
                        'NS': [
                            'string',
                        ],
                        'BS': [
                            b'bytes',
                        ],
                        'M': {
                            'string': {'... recursive ...'}
                        },
                        'L': [
                            {'... recursive ...'},
                        ],
                        'NULL': True|False,
                        'BOOL': True|False
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    TransactItems (list) -- [REQUIRED]
    An ordered array of up to 25 TransactGetItem objects, each of which contains a Get structure.
    
    (dict) --Specifies an item to be retrieved as part of the transaction.
    
    Get (dict) -- [REQUIRED]Contains the primary key that identifies the item to get, together with the name of the table that contains the item, and optionally the specific attributes of the item to retrieve.
    
    Key (dict) -- [REQUIRED]A map of attribute names to AttributeValue objects that specifies the primary key of the item to retrieve.
    
    (string) --
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    S (string) --An attribute of type String. For example:
    
    "S": "Hello"
    
    N (string) --An attribute of type Number. For example:
    
    "N": "123.45"
    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
    
    B (bytes) --An attribute of type Binary. For example:
    
    "B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"
    
    SS (list) --An attribute of type String Set. For example:
    
    "SS": ["Giraffe", "Hippo" ,"Zebra"]
    
    (string) --
    
    
    NS (list) --An attribute of type Number Set. For example:
    
    "NS": ["42.2", "-19", "7.5", "3.14"]
    Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
    
    (string) --
    
    
    BS (list) --An attribute of type Binary Set. For example:
    
    "BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]
    
    (bytes) --
    
    
    M (dict) --An attribute of type Map. For example:
    
    "M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}
    
    (string) --
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    
    
    
    
    L (list) --An attribute of type List. For example:
    
    "L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]
    
    (dict) --Represents the data for an attribute.
    Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
    For more information, see Data Types in the Amazon DynamoDB Developer Guide .
    
    
    
    NULL (boolean) --An attribute of type Null. For example:
    
    "NULL": true
    
    BOOL (boolean) --An attribute of type Boolean. For example:
    
    "BOOL": true
    
    
    
    
    
    
    
    TableName (string) -- [REQUIRED]The name of the table from which to retrieve the specified item.
    
    ProjectionExpression (string) --A string that identifies one or more attributes of the specified item to retrieve from the table. The attributes in the expression must be separated by commas. If no attribute names are specified, then all attributes of the specified item are returned. If any of the requested attributes are not found, they do not appear in the result.
    
    ExpressionAttributeNames (dict) --One or more substitution tokens for attribute names in the ProjectionExpression parameter.
    
    (string) --
    (string) --
    
    
    
    
    
    
    
    
    
    
    ReturnConsumedCapacity (string) -- A value of TOTAL causes consumed capacity information to be returned, and a value of NONE prevents that information from being returned. No other value is valid.
    
    """
    pass

def transact_write_items(TransactItems=None, ReturnConsumedCapacity=None, ReturnItemCollectionMetrics=None, ClientRequestToken=None):
    """
    The actions are completed atomically so that either all of them succeed, or all of them fail. They are defined by the following objects:
    DynamoDB rejects the entire TransactWriteItems request if any of the following is true:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.transact_write_items(
        TransactItems=[
            {
                'ConditionCheck': {
                    'Key': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                    'TableName': 'string',
                    'ConditionExpression': 'string',
                    'ExpressionAttributeNames': {
                        'string': 'string'
                    },
                    'ExpressionAttributeValues': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                    'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'|'NONE'
                },
                'Put': {
                    'Item': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                    'TableName': 'string',
                    'ConditionExpression': 'string',
                    'ExpressionAttributeNames': {
                        'string': 'string'
                    },
                    'ExpressionAttributeValues': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                    'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'|'NONE'
                },
                'Delete': {
                    'Key': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                    'TableName': 'string',
                    'ConditionExpression': 'string',
                    'ExpressionAttributeNames': {
                        'string': 'string'
                    },
                    'ExpressionAttributeValues': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                    'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'|'NONE'
                },
                'Update': {
                    'Key': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                    'UpdateExpression': 'string',
                    'TableName': 'string',
                    'ConditionExpression': 'string',
                    'ExpressionAttributeNames': {
                        'string': 'string'
                    },
                    'ExpressionAttributeValues': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                    'ReturnValuesOnConditionCheckFailure': 'ALL_OLD'|'NONE'
                }
            },
        ],
        ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
        ReturnItemCollectionMetrics='SIZE'|'NONE',
        ClientRequestToken='string'
    )
    
    
    :type TransactItems: list
    :param TransactItems: [REQUIRED]\nAn ordered array of up to 25 TransactWriteItem objects, each of which contains a ConditionCheck , Put , Update , or Delete object. These can operate on items in different tables, but the tables must reside in the same AWS account and Region, and no two of them can operate on the same item.\n\n(dict) --A list of requests that can perform update, put, delete, or check operations on multiple items in one or more tables atomically.\n\nConditionCheck (dict) --A request to perform a check item operation.\n\nKey (dict) -- [REQUIRED]The primary key of the item to be checked. Each element consists of an attribute name and a value for that attribute.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\nTableName (string) -- [REQUIRED]Name of the table for the check item request.\n\nConditionExpression (string) -- [REQUIRED]A condition that must be satisfied in order for a conditional update to succeed.\n\nExpressionAttributeNames (dict) --One or more substitution tokens for attribute names in an expression.\n\n(string) --\n(string) --\n\n\n\n\nExpressionAttributeValues (dict) --One or more values that can be substituted in an expression.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\nReturnValuesOnConditionCheckFailure (string) --Use ReturnValuesOnConditionCheckFailure to get the item attributes if the ConditionCheck condition fails. For ReturnValuesOnConditionCheckFailure , the valid values are: NONE and ALL_OLD.\n\n\n\nPut (dict) --A request to perform a PutItem operation.\n\nItem (dict) -- [REQUIRED]A map of attribute name to attribute values, representing the primary key of the item to be written by PutItem . All of the table\'s primary key attributes must be specified, and their data types must match those of the table\'s key schema. If any attributes are present in the item that are part of an index key schema for the table, their types must match the index key schema.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\nTableName (string) -- [REQUIRED]Name of the table in which to write the item.\n\nConditionExpression (string) --A condition that must be satisfied in order for a conditional update to succeed.\n\nExpressionAttributeNames (dict) --One or more substitution tokens for attribute names in an expression.\n\n(string) --\n(string) --\n\n\n\n\nExpressionAttributeValues (dict) --One or more values that can be substituted in an expression.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\nReturnValuesOnConditionCheckFailure (string) --Use ReturnValuesOnConditionCheckFailure to get the item attributes if the Put condition fails. For ReturnValuesOnConditionCheckFailure , the valid values are: NONE and ALL_OLD.\n\n\n\nDelete (dict) --A request to perform a DeleteItem operation.\n\nKey (dict) -- [REQUIRED]The primary key of the item to be deleted. Each element consists of an attribute name and a value for that attribute.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\nTableName (string) -- [REQUIRED]Name of the table in which the item to be deleted resides.\n\nConditionExpression (string) --A condition that must be satisfied in order for a conditional delete to succeed.\n\nExpressionAttributeNames (dict) --One or more substitution tokens for attribute names in an expression.\n\n(string) --\n(string) --\n\n\n\n\nExpressionAttributeValues (dict) --One or more values that can be substituted in an expression.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\nReturnValuesOnConditionCheckFailure (string) --Use ReturnValuesOnConditionCheckFailure to get the item attributes if the Delete condition fails. For ReturnValuesOnConditionCheckFailure , the valid values are: NONE and ALL_OLD.\n\n\n\nUpdate (dict) --A request to perform an UpdateItem operation.\n\nKey (dict) -- [REQUIRED]The primary key of the item to be updated. Each element consists of an attribute name and a value for that attribute.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\nUpdateExpression (string) -- [REQUIRED]An expression that defines one or more attributes to be updated, the action to be performed on them, and new value(s) for them.\n\nTableName (string) -- [REQUIRED]Name of the table for the UpdateItem request.\n\nConditionExpression (string) --A condition that must be satisfied in order for a conditional update to succeed.\n\nExpressionAttributeNames (dict) --One or more substitution tokens for attribute names in an expression.\n\n(string) --\n(string) --\n\n\n\n\nExpressionAttributeValues (dict) --One or more values that can be substituted in an expression.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\nReturnValuesOnConditionCheckFailure (string) --Use ReturnValuesOnConditionCheckFailure to get the item attributes if the Update condition fails. For ReturnValuesOnConditionCheckFailure , the valid values are: NONE, ALL_OLD, UPDATED_OLD, ALL_NEW, UPDATED_NEW.\n\n\n\n\n\n\n

    :type ReturnConsumedCapacity: string
    :param ReturnConsumedCapacity: Determines the level of detail about provisioned throughput consumption that is returned in the response:\n\nINDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem , do not access any indexes at all. In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s).\nTOTAL - The response includes only the aggregate ConsumedCapacity for the operation.\nNONE - No ConsumedCapacity details are included in the response.\n\n

    :type ReturnItemCollectionMetrics: string
    :param ReturnItemCollectionMetrics: Determines whether item collection metrics are returned. If set to SIZE , the response includes statistics about item collections (if any), that were modified during the operation and are returned in the response. If set to NONE (the default), no statistics are returned.

    :type ClientRequestToken: string
    :param ClientRequestToken: Providing a ClientRequestToken makes the call to TransactWriteItems idempotent, meaning that multiple identical calls have the same effect as one single call.\nAlthough multiple identical calls using the same client request token produce the same result on the server (no side effects), the responses to the calls might not be the same. If the ReturnConsumedCapacity> parameter is set, then the initial TransactWriteItems call returns the amount of write capacity units consumed in making the changes. Subsequent TransactWriteItems calls with the same client token return the number of read capacity units consumed in reading the item.\nA client request token is valid for 10 minutes after the first request that uses it is completed. After 10 minutes, any request with the same client token is treated as a new request. Do not resubmit the same request with the same client token for more than 10 minutes, or the result might not be idempotent.\nIf you submit a request with the same client token but a change in other parameters within the 10-minute idempotency window, DynamoDB returns an IdempotentParameterMismatch exception.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ConsumedCapacity': [
        {
            'TableName': 'string',
            'CapacityUnits': 123.0,
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'Table': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            },
            'LocalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            },
            'GlobalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            }
        },
    ],
    'ItemCollectionMetrics': {
        'string': [
            {
                'ItemCollectionKey': {
                    'string': {
                        'S': 'string',
                        'N': 'string',
                        'B': b'bytes',
                        'SS': [
                            'string',
                        ],
                        'NS': [
                            'string',
                        ],
                        'BS': [
                            b'bytes',
                        ],
                        'M': {
                            'string': {'... recursive ...'}
                        },
                        'L': [
                            {'... recursive ...'},
                        ],
                        'NULL': True|False,
                        'BOOL': True|False
                    }
                },
                'SizeEstimateRangeGB': [
                    123.0,
                ]
            },
        ]
    }
}


Response Structure

(dict) --

ConsumedCapacity (list) --
The capacity units consumed by the entire TransactWriteItems operation. The values of the list are ordered according to the ordering of the TransactItems request parameter.

(dict) --
The capacity units consumed by an operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. ConsumedCapacity is only returned if the request asked for it. For more information, see Provisioned Throughput in the Amazon DynamoDB Developer Guide .

TableName (string) --
The name of the table that was affected by the operation.

CapacityUnits (float) --
The total number of capacity units consumed by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed by the operation.

WriteCapacityUnits (float) --
The total number of write capacity units consumed by the operation.

Table (dict) --
The amount of throughput consumed on the table affected by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.



LocalSecondaryIndexes (dict) --
The amount of throughput consumed on each local index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.







GlobalSecondaryIndexes (dict) --
The amount of throughput consumed on each global index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.











ItemCollectionMetrics (dict) --
A list of tables that were processed by TransactWriteItems and, for each table, information about any item collections that were affected by individual UpdateItem , PutItem , or DeleteItem operations.

(string) --

(list) --

(dict) --
Information about item collections, if any, that were affected by the operation. ItemCollectionMetrics is only returned if the request asked for it. If the table does not have any local secondary indexes, this information is not returned in the response.

ItemCollectionKey (dict) --
The partition key value of the item collection. This value is the same as the partition key value of the item.

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true








SizeEstimateRangeGB (list) --
An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit.
The estimate is subject to change over time; therefore, do not rely on the precision or accuracy of the estimate.

(float) --
















Exceptions

DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.TransactionCanceledException
DynamoDB.Client.exceptions.TransactionInProgressException
DynamoDB.Client.exceptions.IdempotentParameterMismatchException
DynamoDB.Client.exceptions.ProvisionedThroughputExceededException
DynamoDB.Client.exceptions.RequestLimitExceeded
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'ConsumedCapacity': [
            {
                'TableName': 'string',
                'CapacityUnits': 123.0,
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'Table': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                },
                'LocalSecondaryIndexes': {
                    'string': {
                        'ReadCapacityUnits': 123.0,
                        'WriteCapacityUnits': 123.0,
                        'CapacityUnits': 123.0
                    }
                },
                'GlobalSecondaryIndexes': {
                    'string': {
                        'ReadCapacityUnits': 123.0,
                        'WriteCapacityUnits': 123.0,
                        'CapacityUnits': 123.0
                    }
                }
            },
        ],
        'ItemCollectionMetrics': {
            'string': [
                {
                    'ItemCollectionKey': {
                        'string': {
                            'S': 'string',
                            'N': 'string',
                            'B': b'bytes',
                            'SS': [
                                'string',
                            ],
                            'NS': [
                                'string',
                            ],
                            'BS': [
                                b'bytes',
                            ],
                            'M': {
                                'string': {'... recursive ...'}
                            },
                            'L': [
                                {'... recursive ...'},
                            ],
                            'NULL': True|False,
                            'BOOL': True|False
                        }
                    },
                    'SizeEstimateRangeGB': [
                        123.0,
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    A condition in one of the condition expressions is not met.
    An ongoing operation is in the process of updating the same item.
    There is insufficient provisioned capacity for the transaction to be completed.
    An item size becomes too large (bigger than 400 KB), a local secondary index (LSI) becomes too large, or a similar validation error occurs because of changes made by the transaction.
    The aggregate size of the items in the transaction exceeds 4 MB.
    There is a user error, such as an invalid data format.
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes the association of tags from an Amazon DynamoDB resource. You can call UntagResource up to five times per second, per account.
    For an overview on tagging DynamoDB resources, see Tagging for DynamoDB in the Amazon DynamoDB Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe DynamoDB resource that the tags will be removed from. This value is an Amazon Resource Name (ARN).\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of tag keys. Existing tags of the resource whose keys are members of this list will be removed from the DynamoDB resource.\n\n(string) --\n\n

    :returns: 
    DynamoDB.Client.exceptions.LimitExceededException
    DynamoDB.Client.exceptions.ResourceNotFoundException
    DynamoDB.Client.exceptions.InternalServerError
    DynamoDB.Client.exceptions.ResourceInUseException
    
    """
    pass

def update_continuous_backups(TableName=None, PointInTimeRecoverySpecification=None):
    """
    Once continuous backups and point in time recovery are enabled, you can restore to any point in time within EarliestRestorableDateTime and LatestRestorableDateTime .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_continuous_backups(
        TableName='string',
        PointInTimeRecoverySpecification={
            'PointInTimeRecoveryEnabled': True|False
        }
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table.\n

    :type PointInTimeRecoverySpecification: dict
    :param PointInTimeRecoverySpecification: [REQUIRED]\nRepresents the settings used to enable point in time recovery.\n\nPointInTimeRecoveryEnabled (boolean) -- [REQUIRED]Indicates whether point in time recovery is enabled (true) or disabled (false) on the table.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ContinuousBackupsDescription': {
        'ContinuousBackupsStatus': 'ENABLED'|'DISABLED',
        'PointInTimeRecoveryDescription': {
            'PointInTimeRecoveryStatus': 'ENABLED'|'DISABLED',
            'EarliestRestorableDateTime': datetime(2015, 1, 1),
            'LatestRestorableDateTime': datetime(2015, 1, 1)
        }
    }
}


Response Structure

(dict) --

ContinuousBackupsDescription (dict) --
Represents the continuous backups and point in time recovery settings on the table.

ContinuousBackupsStatus (string) --

ContinuousBackupsStatus can be one of the following states: ENABLED, DISABLED


PointInTimeRecoveryDescription (dict) --
The description of the point in time recovery settings applied to the table.

PointInTimeRecoveryStatus (string) --
The current state of point in time recovery:

ENABLING - Point in time recovery is being enabled.
ENABLED - Point in time recovery is enabled.
DISABLED - Point in time recovery is disabled.


EarliestRestorableDateTime (datetime) --
Specifies the earliest point in time you can restore your table to. You can restore your table to any point in time during the last 35 days.

LatestRestorableDateTime (datetime) --

LatestRestorableDateTime is typically 5 minutes before the current time.












Exceptions

DynamoDB.Client.exceptions.TableNotFoundException
DynamoDB.Client.exceptions.ContinuousBackupsUnavailableException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'ContinuousBackupsDescription': {
            'ContinuousBackupsStatus': 'ENABLED'|'DISABLED',
            'PointInTimeRecoveryDescription': {
                'PointInTimeRecoveryStatus': 'ENABLED'|'DISABLED',
                'EarliestRestorableDateTime': datetime(2015, 1, 1),
                'LatestRestorableDateTime': datetime(2015, 1, 1)
            }
        }
    }
    
    
    :returns: 
    ENABLING - Point in time recovery is being enabled.
    ENABLED - Point in time recovery is enabled.
    DISABLED - Point in time recovery is disabled.
    
    """
    pass

def update_contributor_insights(TableName=None, IndexName=None, ContributorInsightsAction=None):
    """
    Updates the status for contributor insights for a specific table or index.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_contributor_insights(
        TableName='string',
        IndexName='string',
        ContributorInsightsAction='ENABLE'|'DISABLE'
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table.\n

    :type IndexName: string
    :param IndexName: The global secondary index name, if applicable.

    :type ContributorInsightsAction: string
    :param ContributorInsightsAction: [REQUIRED]\nRepresents the contributor insights action.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TableName': 'string',
    'IndexName': 'string',
    'ContributorInsightsStatus': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'FAILED'
}


Response Structure

(dict) --

TableName (string) --
The name of the table.

IndexName (string) --
The name of the global secondary index, if applicable.

ContributorInsightsStatus (string) --
The status of contributor insights







Exceptions

DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'TableName': 'string',
        'IndexName': 'string',
        'ContributorInsightsStatus': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'FAILED'
    }
    
    
    :returns: 
    DynamoDB.Client.exceptions.ResourceNotFoundException
    DynamoDB.Client.exceptions.InternalServerError
    
    """
    pass

def update_global_table(GlobalTableName=None, ReplicaUpdates=None):
    """
    Adds or removes replicas in the specified global table. The global table must already exist to be able to use this operation. Any replica to be added must be empty, have the same name as the global table, have the same key schema, have DynamoDB Streams enabled, and have the same provisioned and maximum write capacity units.
    If global secondary indexes are specified, then the following conditions must also be met:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_global_table(
        GlobalTableName='string',
        ReplicaUpdates=[
            {
                'Create': {
                    'RegionName': 'string'
                },
                'Delete': {
                    'RegionName': 'string'
                }
            },
        ]
    )
    
    
    :type GlobalTableName: string
    :param GlobalTableName: [REQUIRED]\nThe global table name.\n

    :type ReplicaUpdates: list
    :param ReplicaUpdates: [REQUIRED]\nA list of Regions that should be added or removed from the global table.\n\n(dict) --Represents one of the following:\n\nA new replica to be added to an existing global table.\nNew parameters for an existing replica.\nAn existing replica to be removed from an existing global table.\n\n\nCreate (dict) --The parameters required for creating a replica on an existing global table.\n\nRegionName (string) -- [REQUIRED]The Region of the replica to be added.\n\n\n\nDelete (dict) --The name of the existing replica to be removed.\n\nRegionName (string) -- [REQUIRED]The Region of the replica to be removed.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalTableDescription': {
        'ReplicationGroup': [
            {
                'RegionName': 'string',
                'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                'ReplicaStatusDescription': 'string',
                'ReplicaStatusPercentProgress': 'string',
                'KMSMasterKeyId': 'string',
                'ProvisionedThroughputOverride': {
                    'ReadCapacityUnits': 123
                },
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'ProvisionedThroughputOverride': {
                            'ReadCapacityUnits': 123
                        }
                    },
                ]
            },
        ],
        'GlobalTableArn': 'string',
        'CreationDateTime': datetime(2015, 1, 1),
        'GlobalTableStatus': 'CREATING'|'ACTIVE'|'DELETING'|'UPDATING',
        'GlobalTableName': 'string'
    }
}


Response Structure

(dict) --

GlobalTableDescription (dict) --
Contains the details of the global table.

ReplicationGroup (list) --
The Regions where the global table has replicas.

(dict) --
Contains the details of the replica.

RegionName (string) --
The name of the Region.

ReplicaStatus (string) --
The current state of the replica:

CREATING - The replica is being created.
UPDATING - The replica is being updated.
DELETING - The replica is being deleted.
ACTIVE - The replica is ready for use.


ReplicaStatusDescription (string) --
Detailed information about the replica status.

ReplicaStatusPercentProgress (string) --
Specifies the progress of a Create, Update, or Delete action on the replica as a percentage.

KMSMasterKeyId (string) --
The AWS KMS customer master key (CMK) of the replica that will be used for AWS KMS encryption.

ProvisionedThroughputOverride (dict) --
Replica-specific provisioned throughput. If not described, uses the source table\'s provisioned throughput settings.

ReadCapacityUnits (integer) --
Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.



GlobalSecondaryIndexes (list) --
Replica-specific global secondary index settings.

(dict) --
Represents the properties of a replica global secondary index.

IndexName (string) --
The name of the global secondary index.

ProvisionedThroughputOverride (dict) --
If not described, uses the source table GSI\'s read capacity settings.

ReadCapacityUnits (integer) --
Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.











GlobalTableArn (string) --
The unique identifier of the global table.

CreationDateTime (datetime) --
The creation time of the global table.

GlobalTableStatus (string) --
The current state of the global table:

CREATING - The global table is being created.
UPDATING - The global table is being updated.
DELETING - The global table is being deleted.
ACTIVE - The global table is ready for use.


GlobalTableName (string) --
The global table name.









Exceptions

DynamoDB.Client.exceptions.InternalServerError
DynamoDB.Client.exceptions.GlobalTableNotFoundException
DynamoDB.Client.exceptions.ReplicaAlreadyExistsException
DynamoDB.Client.exceptions.ReplicaNotFoundException
DynamoDB.Client.exceptions.TableNotFoundException


    :return: {
        'GlobalTableDescription': {
            'ReplicationGroup': [
                {
                    'RegionName': 'string',
                    'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                    'ReplicaStatusDescription': 'string',
                    'ReplicaStatusPercentProgress': 'string',
                    'KMSMasterKeyId': 'string',
                    'ProvisionedThroughputOverride': {
                        'ReadCapacityUnits': 123
                    },
                    'GlobalSecondaryIndexes': [
                        {
                            'IndexName': 'string',
                            'ProvisionedThroughputOverride': {
                                'ReadCapacityUnits': 123
                            }
                        },
                    ]
                },
            ],
            'GlobalTableArn': 'string',
            'CreationDateTime': datetime(2015, 1, 1),
            'GlobalTableStatus': 'CREATING'|'ACTIVE'|'DELETING'|'UPDATING',
            'GlobalTableName': 'string'
        }
    }
    
    
    :returns: 
    GlobalTableName (string) -- [REQUIRED]
    The global table name.
    
    ReplicaUpdates (list) -- [REQUIRED]
    A list of Regions that should be added or removed from the global table.
    
    (dict) --Represents one of the following:
    
    A new replica to be added to an existing global table.
    New parameters for an existing replica.
    An existing replica to be removed from an existing global table.
    
    
    Create (dict) --The parameters required for creating a replica on an existing global table.
    
    RegionName (string) -- [REQUIRED]The Region of the replica to be added.
    
    
    
    Delete (dict) --The name of the existing replica to be removed.
    
    RegionName (string) -- [REQUIRED]The Region of the replica to be removed.
    
    
    
    
    
    
    
    
    """
    pass

def update_global_table_settings(GlobalTableName=None, GlobalTableBillingMode=None, GlobalTableProvisionedWriteCapacityUnits=None, GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate=None, GlobalTableGlobalSecondaryIndexSettingsUpdate=None, ReplicaSettingsUpdate=None):
    """
    Updates settings for a global table.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_global_table_settings(
        GlobalTableName='string',
        GlobalTableBillingMode='PROVISIONED'|'PAY_PER_REQUEST',
        GlobalTableProvisionedWriteCapacityUnits=123,
        GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate={
            'MinimumUnits': 123,
            'MaximumUnits': 123,
            'AutoScalingDisabled': True|False,
            'AutoScalingRoleArn': 'string',
            'ScalingPolicyUpdate': {
                'PolicyName': 'string',
                'TargetTrackingScalingPolicyConfiguration': {
                    'DisableScaleIn': True|False,
                    'ScaleInCooldown': 123,
                    'ScaleOutCooldown': 123,
                    'TargetValue': 123.0
                }
            }
        },
        GlobalTableGlobalSecondaryIndexSettingsUpdate=[
            {
                'IndexName': 'string',
                'ProvisionedWriteCapacityUnits': 123,
                'ProvisionedWriteCapacityAutoScalingSettingsUpdate': {
                    'MinimumUnits': 123,
                    'MaximumUnits': 123,
                    'AutoScalingDisabled': True|False,
                    'AutoScalingRoleArn': 'string',
                    'ScalingPolicyUpdate': {
                        'PolicyName': 'string',
                        'TargetTrackingScalingPolicyConfiguration': {
                            'DisableScaleIn': True|False,
                            'ScaleInCooldown': 123,
                            'ScaleOutCooldown': 123,
                            'TargetValue': 123.0
                        }
                    }
                }
            },
        ],
        ReplicaSettingsUpdate=[
            {
                'RegionName': 'string',
                'ReplicaProvisionedReadCapacityUnits': 123,
                'ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate': {
                    'MinimumUnits': 123,
                    'MaximumUnits': 123,
                    'AutoScalingDisabled': True|False,
                    'AutoScalingRoleArn': 'string',
                    'ScalingPolicyUpdate': {
                        'PolicyName': 'string',
                        'TargetTrackingScalingPolicyConfiguration': {
                            'DisableScaleIn': True|False,
                            'ScaleInCooldown': 123,
                            'ScaleOutCooldown': 123,
                            'TargetValue': 123.0
                        }
                    }
                },
                'ReplicaGlobalSecondaryIndexSettingsUpdate': [
                    {
                        'IndexName': 'string',
                        'ProvisionedReadCapacityUnits': 123,
                        'ProvisionedReadCapacityAutoScalingSettingsUpdate': {
                            'MinimumUnits': 123,
                            'MaximumUnits': 123,
                            'AutoScalingDisabled': True|False,
                            'AutoScalingRoleArn': 'string',
                            'ScalingPolicyUpdate': {
                                'PolicyName': 'string',
                                'TargetTrackingScalingPolicyConfiguration': {
                                    'DisableScaleIn': True|False,
                                    'ScaleInCooldown': 123,
                                    'ScaleOutCooldown': 123,
                                    'TargetValue': 123.0
                                }
                            }
                        }
                    },
                ]
            },
        ]
    )
    
    
    :type GlobalTableName: string
    :param GlobalTableName: [REQUIRED]\nThe name of the global table\n

    :type GlobalTableBillingMode: string
    :param GlobalTableBillingMode: The billing mode of the global table. If GlobalTableBillingMode is not specified, the global table defaults to PROVISIONED capacity billing mode.\n\nPROVISIONED - We recommend using PROVISIONED for predictable workloads. PROVISIONED sets the billing mode to Provisioned Mode .\nPAY_PER_REQUEST - We recommend using PAY_PER_REQUEST for unpredictable workloads. PAY_PER_REQUEST sets the billing mode to On-Demand Mode .\n\n

    :type GlobalTableProvisionedWriteCapacityUnits: integer
    :param GlobalTableProvisionedWriteCapacityUnits: The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException.

    :type GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: dict
    :param GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: Auto scaling settings for managing provisioned write capacity for the global table.\n\nMinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.\n\nMaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.\n\nAutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.\n\nAutoScalingRoleArn (string) --Role ARN used for configuring auto scaling policy.\n\nScalingPolicyUpdate (dict) --The scaling policy to apply for scaling target global table or global secondary index capacity units.\n\nPolicyName (string) --The name of the scaling policy.\n\nTargetTrackingScalingPolicyConfiguration (dict) -- [REQUIRED]Represents a target tracking scaling policy configuration.\n\nDisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.\n\nScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.\n\nScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.\n\nTargetValue (float) -- [REQUIRED]The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).\n\n\n\n\n\n\n

    :type GlobalTableGlobalSecondaryIndexSettingsUpdate: list
    :param GlobalTableGlobalSecondaryIndexSettingsUpdate: Represents the settings of a global secondary index for a global table that will be modified.\n\n(dict) --Represents the settings of a global secondary index for a global table that will be modified.\n\nIndexName (string) -- [REQUIRED]The name of the global secondary index. The name must be unique among all other indexes on this table.\n\nProvisionedWriteCapacityUnits (integer) --The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException.\n\nProvisionedWriteCapacityAutoScalingSettingsUpdate (dict) --Auto scaling settings for managing a global secondary index\'s write capacity units.\n\nMinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.\n\nMaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.\n\nAutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.\n\nAutoScalingRoleArn (string) --Role ARN used for configuring auto scaling policy.\n\nScalingPolicyUpdate (dict) --The scaling policy to apply for scaling target global table or global secondary index capacity units.\n\nPolicyName (string) --The name of the scaling policy.\n\nTargetTrackingScalingPolicyConfiguration (dict) -- [REQUIRED]Represents a target tracking scaling policy configuration.\n\nDisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.\n\nScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.\n\nScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.\n\nTargetValue (float) -- [REQUIRED]The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).\n\n\n\n\n\n\n\n\n\n\n

    :type ReplicaSettingsUpdate: list
    :param ReplicaSettingsUpdate: Represents the settings for a global table in a Region that will be modified.\n\n(dict) --Represents the settings for a global table in a Region that will be modified.\n\nRegionName (string) -- [REQUIRED]The Region of the replica to be added.\n\nReplicaProvisionedReadCapacityUnits (integer) --The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\n\nReplicaProvisionedReadCapacityAutoScalingSettingsUpdate (dict) --Auto scaling settings for managing a global table replica\'s read capacity units.\n\nMinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.\n\nMaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.\n\nAutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.\n\nAutoScalingRoleArn (string) --Role ARN used for configuring auto scaling policy.\n\nScalingPolicyUpdate (dict) --The scaling policy to apply for scaling target global table or global secondary index capacity units.\n\nPolicyName (string) --The name of the scaling policy.\n\nTargetTrackingScalingPolicyConfiguration (dict) -- [REQUIRED]Represents a target tracking scaling policy configuration.\n\nDisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.\n\nScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.\n\nScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.\n\nTargetValue (float) -- [REQUIRED]The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).\n\n\n\n\n\n\n\nReplicaGlobalSecondaryIndexSettingsUpdate (list) --Represents the settings of a global secondary index for a global table that will be modified.\n\n(dict) --Represents the settings of a global secondary index for a global table that will be modified.\n\nIndexName (string) -- [REQUIRED]The name of the global secondary index. The name must be unique among all other indexes on this table.\n\nProvisionedReadCapacityUnits (integer) --The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException .\n\nProvisionedReadCapacityAutoScalingSettingsUpdate (dict) --Auto scaling settings for managing a global secondary index replica\'s read capacity units.\n\nMinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.\n\nMaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.\n\nAutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.\n\nAutoScalingRoleArn (string) --Role ARN used for configuring auto scaling policy.\n\nScalingPolicyUpdate (dict) --The scaling policy to apply for scaling target global table or global secondary index capacity units.\n\nPolicyName (string) --The name of the scaling policy.\n\nTargetTrackingScalingPolicyConfiguration (dict) -- [REQUIRED]Represents a target tracking scaling policy configuration.\n\nDisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.\n\nScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.\n\nScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.\n\nTargetValue (float) -- [REQUIRED]The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalTableName': 'string',
    'ReplicaSettings': [
        {
            'RegionName': 'string',
            'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
            'ReplicaBillingModeSummary': {
                'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
                'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
            },
            'ReplicaProvisionedReadCapacityUnits': 123,
            'ReplicaProvisionedReadCapacityAutoScalingSettings': {
                'MinimumUnits': 123,
                'MaximumUnits': 123,
                'AutoScalingDisabled': True|False,
                'AutoScalingRoleArn': 'string',
                'ScalingPolicies': [
                    {
                        'PolicyName': 'string',
                        'TargetTrackingScalingPolicyConfiguration': {
                            'DisableScaleIn': True|False,
                            'ScaleInCooldown': 123,
                            'ScaleOutCooldown': 123,
                            'TargetValue': 123.0
                        }
                    },
                ]
            },
            'ReplicaProvisionedWriteCapacityUnits': 123,
            'ReplicaProvisionedWriteCapacityAutoScalingSettings': {
                'MinimumUnits': 123,
                'MaximumUnits': 123,
                'AutoScalingDisabled': True|False,
                'AutoScalingRoleArn': 'string',
                'ScalingPolicies': [
                    {
                        'PolicyName': 'string',
                        'TargetTrackingScalingPolicyConfiguration': {
                            'DisableScaleIn': True|False,
                            'ScaleInCooldown': 123,
                            'ScaleOutCooldown': 123,
                            'TargetValue': 123.0
                        }
                    },
                ]
            },
            'ReplicaGlobalSecondaryIndexSettings': [
                {
                    'IndexName': 'string',
                    'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                    'ProvisionedReadCapacityUnits': 123,
                    'ProvisionedReadCapacityAutoScalingSettings': {
                        'MinimumUnits': 123,
                        'MaximumUnits': 123,
                        'AutoScalingDisabled': True|False,
                        'AutoScalingRoleArn': 'string',
                        'ScalingPolicies': [
                            {
                                'PolicyName': 'string',
                                'TargetTrackingScalingPolicyConfiguration': {
                                    'DisableScaleIn': True|False,
                                    'ScaleInCooldown': 123,
                                    'ScaleOutCooldown': 123,
                                    'TargetValue': 123.0
                                }
                            },
                        ]
                    },
                    'ProvisionedWriteCapacityUnits': 123,
                    'ProvisionedWriteCapacityAutoScalingSettings': {
                        'MinimumUnits': 123,
                        'MaximumUnits': 123,
                        'AutoScalingDisabled': True|False,
                        'AutoScalingRoleArn': 'string',
                        'ScalingPolicies': [
                            {
                                'PolicyName': 'string',
                                'TargetTrackingScalingPolicyConfiguration': {
                                    'DisableScaleIn': True|False,
                                    'ScaleInCooldown': 123,
                                    'ScaleOutCooldown': 123,
                                    'TargetValue': 123.0
                                }
                            },
                        ]
                    }
                },
            ]
        },
    ]
}


Response Structure

(dict) --

GlobalTableName (string) --
The name of the global table.

ReplicaSettings (list) --
The Region-specific settings for the global table.

(dict) --
Represents the properties of a replica.

RegionName (string) --
The Region name of the replica.

ReplicaStatus (string) --
The current state of the Region:

CREATING - The Region is being created.
UPDATING - The Region is being updated.
DELETING - The Region is being deleted.
ACTIVE - The Region is ready for use.


ReplicaBillingModeSummary (dict) --
The read/write capacity mode of the replica.

BillingMode (string) --
Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.

PROVISIONED - Sets the read/write capacity mode to PROVISIONED . We recommend using PROVISIONED for predictable workloads.
PAY_PER_REQUEST - Sets the read/write capacity mode to PAY_PER_REQUEST . We recommend using PAY_PER_REQUEST for unpredictable workloads.


LastUpdateToPayPerRequestDateTime (datetime) --
Represents the time when PAY_PER_REQUEST was last set as the read/write capacity mode.



ReplicaProvisionedReadCapacityUnits (integer) --
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .

ReplicaProvisionedReadCapacityAutoScalingSettings (dict) --
Auto scaling settings for a global table replica\'s read capacity units.

MinimumUnits (integer) --
The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --
The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --
Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --
Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --
Information about the scaling policies.

(dict) --
Represents the properties of the scaling policy.

PolicyName (string) --
The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --
Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --
Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --
The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --
The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --
The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).









ReplicaProvisionedWriteCapacityUnits (integer) --
The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .

ReplicaProvisionedWriteCapacityAutoScalingSettings (dict) --
Auto scaling settings for a global table replica\'s write capacity units.

MinimumUnits (integer) --
The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --
The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --
Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --
Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --
Information about the scaling policies.

(dict) --
Represents the properties of the scaling policy.

PolicyName (string) --
The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --
Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --
Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --
The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --
The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --
The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).









ReplicaGlobalSecondaryIndexSettings (list) --
Replica global secondary index settings for the global table.

(dict) --
Represents the properties of a global secondary index.

IndexName (string) --
The name of the global secondary index. The name must be unique among all other indexes on this table.

IndexStatus (string) --
The current status of the global secondary index:

CREATING - The global secondary index is being created.
UPDATING - The global secondary index is being updated.
DELETING - The global secondary index is being deleted.
ACTIVE - The global secondary index is ready for use.


ProvisionedReadCapacityUnits (integer) --
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException .

ProvisionedReadCapacityAutoScalingSettings (dict) --
Auto scaling settings for a global secondary index replica\'s read capacity units.

MinimumUnits (integer) --
The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --
The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --
Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --
Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --
Information about the scaling policies.

(dict) --
Represents the properties of the scaling policy.

PolicyName (string) --
The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --
Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --
Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --
The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --
The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --
The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).









ProvisionedWriteCapacityUnits (integer) --
The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException .

ProvisionedWriteCapacityAutoScalingSettings (dict) --
Auto scaling settings for a global secondary index replica\'s write capacity units.

MinimumUnits (integer) --
The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --
The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --
Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --
Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --
Information about the scaling policies.

(dict) --
Represents the properties of the scaling policy.

PolicyName (string) --
The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --
Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --
Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --
The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --
The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --
The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).























Exceptions

DynamoDB.Client.exceptions.GlobalTableNotFoundException
DynamoDB.Client.exceptions.ReplicaNotFoundException
DynamoDB.Client.exceptions.IndexNotFoundException
DynamoDB.Client.exceptions.LimitExceededException
DynamoDB.Client.exceptions.ResourceInUseException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'GlobalTableName': 'string',
        'ReplicaSettings': [
            {
                'RegionName': 'string',
                'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                'ReplicaBillingModeSummary': {
                    'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
                    'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
                },
                'ReplicaProvisionedReadCapacityUnits': 123,
                'ReplicaProvisionedReadCapacityAutoScalingSettings': {
                    'MinimumUnits': 123,
                    'MaximumUnits': 123,
                    'AutoScalingDisabled': True|False,
                    'AutoScalingRoleArn': 'string',
                    'ScalingPolicies': [
                        {
                            'PolicyName': 'string',
                            'TargetTrackingScalingPolicyConfiguration': {
                                'DisableScaleIn': True|False,
                                'ScaleInCooldown': 123,
                                'ScaleOutCooldown': 123,
                                'TargetValue': 123.0
                            }
                        },
                    ]
                },
                'ReplicaProvisionedWriteCapacityUnits': 123,
                'ReplicaProvisionedWriteCapacityAutoScalingSettings': {
                    'MinimumUnits': 123,
                    'MaximumUnits': 123,
                    'AutoScalingDisabled': True|False,
                    'AutoScalingRoleArn': 'string',
                    'ScalingPolicies': [
                        {
                            'PolicyName': 'string',
                            'TargetTrackingScalingPolicyConfiguration': {
                                'DisableScaleIn': True|False,
                                'ScaleInCooldown': 123,
                                'ScaleOutCooldown': 123,
                                'TargetValue': 123.0
                            }
                        },
                    ]
                },
                'ReplicaGlobalSecondaryIndexSettings': [
                    {
                        'IndexName': 'string',
                        'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                        'ProvisionedReadCapacityUnits': 123,
                        'ProvisionedReadCapacityAutoScalingSettings': {
                            'MinimumUnits': 123,
                            'MaximumUnits': 123,
                            'AutoScalingDisabled': True|False,
                            'AutoScalingRoleArn': 'string',
                            'ScalingPolicies': [
                                {
                                    'PolicyName': 'string',
                                    'TargetTrackingScalingPolicyConfiguration': {
                                        'DisableScaleIn': True|False,
                                        'ScaleInCooldown': 123,
                                        'ScaleOutCooldown': 123,
                                        'TargetValue': 123.0
                                    }
                                },
                            ]
                        },
                        'ProvisionedWriteCapacityUnits': 123,
                        'ProvisionedWriteCapacityAutoScalingSettings': {
                            'MinimumUnits': 123,
                            'MaximumUnits': 123,
                            'AutoScalingDisabled': True|False,
                            'AutoScalingRoleArn': 'string',
                            'ScalingPolicies': [
                                {
                                    'PolicyName': 'string',
                                    'TargetTrackingScalingPolicyConfiguration': {
                                        'DisableScaleIn': True|False,
                                        'ScaleInCooldown': 123,
                                        'ScaleOutCooldown': 123,
                                        'TargetValue': 123.0
                                    }
                                },
                            ]
                        }
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    CREATING - The Region is being created.
    UPDATING - The Region is being updated.
    DELETING - The Region is being deleted.
    ACTIVE - The Region is ready for use.
    
    """
    pass

def update_item(TableName=None, Key=None, AttributeUpdates=None, Expected=None, ConditionalOperator=None, ReturnValues=None, ReturnConsumedCapacity=None, ReturnItemCollectionMetrics=None, UpdateExpression=None, ConditionExpression=None, ExpressionAttributeNames=None, ExpressionAttributeValues=None):
    """
    Edits an existing item\'s attributes, or adds a new item to the table if it does not already exist. You can put, delete, or add attribute values. You can also perform a conditional update on an existing item (insert a new attribute name-value pair if it doesn\'t exist, or replace an existing name-value pair if it has certain expected attribute values).
    You can also return the item\'s attribute values in the same UpdateItem operation using the ReturnValues parameter.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example updates an item in the Music table. It adds a new attribute (Year) and modifies the AlbumTitle attribute.  All of the attributes in the item, as they appear after the update, are returned in the response.
    Expected Output:
    
    :example: response = client.update_item(
        TableName='string',
        Key={
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        AttributeUpdates={
            'string': {
                'Value': {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                },
                'Action': 'ADD'|'PUT'|'DELETE'
            }
        },
        Expected={
            'string': {
                'Value': {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                },
                'Exists': True|False,
                'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH',
                'AttributeValueList': [
                    {
                        'S': 'string',
                        'N': 'string',
                        'B': b'bytes',
                        'SS': [
                            'string',
                        ],
                        'NS': [
                            'string',
                        ],
                        'BS': [
                            b'bytes',
                        ],
                        'M': {
                            'string': {'... recursive ...'}
                        },
                        'L': [
                            {'... recursive ...'},
                        ],
                        'NULL': True|False,
                        'BOOL': True|False
                    },
                ]
            }
        },
        ConditionalOperator='AND'|'OR',
        ReturnValues='NONE'|'ALL_OLD'|'UPDATED_OLD'|'ALL_NEW'|'UPDATED_NEW',
        ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
        ReturnItemCollectionMetrics='SIZE'|'NONE',
        UpdateExpression='string',
        ConditionExpression='string',
        ExpressionAttributeNames={
            'string': 'string'
        },
        ExpressionAttributeValues={
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        }
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table containing the item to update.\n

    :type Key: dict
    :param Key: [REQUIRED]\nThe primary key of the item to be updated. Each element consists of an attribute name and a value for that attribute.\nFor the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n

    :type AttributeUpdates: dict
    :param AttributeUpdates: This is a legacy parameter. Use UpdateExpression instead. For more information, see AttributeUpdates in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(dict) --For the UpdateItem operation, represents the attributes to be modified, the action to perform on each, and the new value for each.\n\nNote\nYou cannot use UpdateItem to update any primary key attributes. Instead, you will need to delete the item, and then use PutItem to create a new item with new attributes.\n\nAttribute values cannot be null; string and binary type attributes must have lengths greater than zero; and set type attributes must not be empty. Requests with empty values will be rejected with a ValidationException exception.\n\nValue (dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\nAction (string) --Specifies how to perform the update. Valid values are PUT (default), DELETE , and ADD . The behavior depends on whether the specified primary key already exists in the table.\n\nIf an item with the specified *Key* is found in the table:\n\nPUT - Adds the specified attribute to the item. If the attribute already exists, it is replaced by the new value.\nDELETE - If no value is specified, the attribute and its value are removed from the item. The data type of the specified value must match the existing value\'s data type. If a set of values is specified, then those values are subtracted from the old set. For example, if the attribute value was the set [a,b,c] and the DELETE action specified [a,c] , then the final attribute value would be [b] . Specifying an empty set is an error.\nADD - If the attribute does not already exist, then the attribute and its values are added to the item. If the attribute does exist, then the behavior of ADD depends on the data type of the attribute:\nIf the existing attribute is a number, and if Value is also a number, then the Value is mathematically added to the existing attribute. If Value is a negative number, then it is subtracted from the existing attribute.\n\n\nNote\nIf you use ADD to increment or decrement a number value for an item that doesn\'t exist before the update, DynamoDB uses 0 as the initial value. In addition, if you use ADD to update an existing item, and intend to increment or decrement an attribute value which does not yet exist, DynamoDB uses 0 as the initial value. For example, suppose that the item you want to update does not yet have an attribute named itemcount , but you decide to ADD the number 3 to this attribute anyway, even though it currently does not exist. DynamoDB will create the itemcount attribute, set its initial value to 0 , and finally add 3 to it. The result will be a new itemcount attribute in the item, with a value of 3 .\n\n\nIf the existing data type is a set, and if the Value is also a set, then the Value is added to the existing set. (This is a set operation, not mathematical addition.) For example, if the attribute value was the set [1,2] , and the ADD action specified [3] , then the final attribute value would be [1,2,3] . An error occurs if an Add action is specified for a set attribute and the attribute type specified does not match the existing set type. Both sets must have the same primitive data type. For example, if the existing data type is a set of strings, the Value must also be a set of strings. The same holds true for number sets and binary sets.\n\n\n\nThis action is only valid for an existing attribute whose data type is number or is a set. Do not use ADD for any other data types.\n\nIf no item with the specified *Key* is found:\n\nPUT - DynamoDB creates a new item with the specified primary key, and then adds the attribute.\nDELETE - Nothing happens; there is no attribute to delete.\nADD - DynamoDB creates an item with the supplied primary key and number (or set of numbers) for the attribute value. The only data types allowed are number and number set; no other data types can be specified.\n\n\n\n\n\n\n\n

    :type Expected: dict
    :param Expected: This is a legacy parameter. Use ConditionExpression instead. For more information, see Expected in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(dict) --Represents a condition to be compared with an attribute value. This condition can be used with DeleteItem , PutItem , or UpdateItem operations; if the comparison evaluates to true, the operation succeeds; if not, the operation fails. You can use ExpectedAttributeValue in one of two different ways:\n\nUse AttributeValueList to specify one or more values to compare against an attribute. Use ComparisonOperator to specify how you want to perform the comparison. If the comparison evaluates to true, then the conditional operation succeeds.\nUse Value to specify a value that DynamoDB will compare against an attribute. If the values match, then ExpectedAttributeValue evaluates to true and the conditional operation succeeds. Optionally, you can also set Exists to false, indicating that you do not expect to find the attribute value in the table. In this case, the conditional operation succeeds only if the comparison evaluates to false.\n\n\nValue and Exists are incompatible with AttributeValueList and ComparisonOperator . Note that if you use both sets of parameters at once, DynamoDB will return a ValidationException exception.\n\nValue (dict) --Represents the data for the expected attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\nExists (boolean) --Causes DynamoDB to evaluate the value before attempting a conditional operation:\n\nIf Exists is true , DynamoDB will check to see if that attribute value already exists in the table. If it is found, then the operation succeeds. If it is not found, the operation fails with a ConditionCheckFailedException .\nIf Exists is false , DynamoDB assumes that the attribute value does not exist in the table. If in fact the value does not exist, then the assumption is valid and the operation succeeds. If the value is found, despite the assumption that it does not exist, the operation fails with a ConditionCheckFailedException .\n\nThe default setting for Exists is true . If you supply a Value all by itself, DynamoDB assumes the attribute exists: You don\'t have to set Exists to true , because it is implied.\nDynamoDB returns a ValidationException if:\n\nExists is true but there is no Value to check. (You expect a value to exist, but don\'t specify what that value is.)\nExists is false but you also provide a Value . (You cannot expect an attribute to have a value, while also expecting it not to exist.)\n\n\nComparisonOperator (string) --A comparator for evaluating attributes in the AttributeValueList . For example, equals, greater than, less than, etc.\nThe following comparison operators are available:\n\nEQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS | NOT_CONTAINS | BEGINS_WITH | IN | BETWEEN\nThe following are descriptions of each comparison operator.\n\nEQ : Equal. EQ is supported for all data types, including lists and maps. AttributeValueList can contain only one AttributeValue element of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not equal {'NS':['6', '2', '1']} .\nNE : Not equal. NE is supported for all data types, including lists and maps. AttributeValueList can contain only one AttributeValue of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an AttributeValue of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not equal {'NS':['6', '2', '1']} .\nLE : Less than or equal.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nLT : Less than.  AttributeValueList can contain only one AttributeValue of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nGE : Greater than or equal.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nGT : Greater than.  AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not equal {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']} .\nNOT_NULL : The attribute exists. NOT_NULL is supported for all data types, including lists and maps.\n\n\nNote\nThis operator tests for the existence of an attribute, not its data type. If the data type of attribute 'a ' is null, and you evaluate it using NOT_NULL , the result is a Boolean true . This result is because the attribute 'a ' exists; its data type is not relevant to the NOT_NULL comparison operator.\n\n\nNULL : The attribute does not exist. NULL is supported for all data types, including lists and maps.\n\n\nNote\nThis operator tests for the nonexistence of an attribute, not its data type. If the data type of attribute 'a ' is null, and you evaluate it using NULL , the result is a Boolean false . This is because the attribute 'a ' exists; its data type is not relevant to the NULL comparison operator.\n\n\nCONTAINS : Checks for a subsequence, or value in a set. AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is of type String, then the operator checks for a substring match. If the target attribute of the comparison is of type Binary, then the operator looks for a subsequence of the target that matches the input. If the target attribute of the comparison is a set ('SS ', 'NS ', or 'BS '), then the operator evaluates to true if it finds an exact match with any member of the set. CONTAINS is supported for lists: When evaluating 'a CONTAINS b ', 'a ' can be a list; however, 'b ' cannot be a set, a map, or a list.\nNOT_CONTAINS : Checks for absence of a subsequence, or absence of a value in a set. AttributeValueList can contain only one AttributeValue element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is a String, then the operator checks for the absence of a substring match. If the target attribute of the comparison is Binary, then the operator checks for the absence of a subsequence of the target that matches the input. If the target attribute of the comparison is a set ('SS ', 'NS ', or 'BS '), then the operator evaluates to true if it does not find an exact match with any member of the set. NOT_CONTAINS is supported for lists: When evaluating 'a NOT CONTAINS b ', 'a ' can be a list; however, 'b ' cannot be a set, a map, or a list.\nBEGINS_WITH : Checks for a prefix.  AttributeValueList can contain only one AttributeValue of type String or Binary (not a Number or a set type). The target attribute of the comparison must be of type String or Binary (not a Number or a set type).\nIN : Checks for matching elements in a list. AttributeValueList can contain one or more AttributeValue elements of type String, Number, or Binary. These attributes are compared against an existing attribute of an item. If any elements of the input are equal to the item attribute, the expression evaluates to true.\nBETWEEN : Greater than or equal to the first value, and less than or equal to the second value.  AttributeValueList must contain two AttributeValue elements of the same type, either String, Number, or Binary (not a set type). A target attribute matches if the target value is greater than, or equal to, the first element and less than, or equal to, the second element. If an item contains an AttributeValue element of a different type than the one provided in the request, the value does not match. For example, {'S':'6'} does not compare to {'N':'6'} . Also, {'N':'6'} does not compare to {'NS':['6', '2', '1']}\n\n\nAttributeValueList (list) --One or more values to evaluate against the supplied attribute. The number of values in the list depends on the ComparisonOperator being used.\nFor type Number, value comparisons are numeric.\nString value comparisons for greater than, equals, or less than are based on ASCII character code values. For example, a is greater than A , and a is greater than B . For a list of code values, see http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters .\nFor Binary, DynamoDB treats each byte of the binary data as unsigned when it compares binary values.\nFor information on specifying data types in JSON, see JSON Data Format in the Amazon DynamoDB Developer Guide .\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n\n\n\n\n

    :type ConditionalOperator: string
    :param ConditionalOperator: This is a legacy parameter. Use ConditionExpression instead. For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide .

    :type ReturnValues: string
    :param ReturnValues: Use ReturnValues if you want to get the item attributes as they appear before or after they are updated. For UpdateItem , the valid values are:\n\nNONE - If ReturnValues is not specified, or if its value is NONE , then nothing is returned. (This setting is the default for ReturnValues .)\nALL_OLD - Returns all of the attributes of the item, as they appeared before the UpdateItem operation.\nUPDATED_OLD - Returns only the updated attributes, as they appeared before the UpdateItem operation.\nALL_NEW - Returns all of the attributes of the item, as they appear after the UpdateItem operation.\nUPDATED_NEW - Returns only the updated attributes, as they appear after the UpdateItem operation.\n\nThere is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.\nThe values returned are strongly consistent.\n

    :type ReturnConsumedCapacity: string
    :param ReturnConsumedCapacity: Determines the level of detail about provisioned throughput consumption that is returned in the response:\n\nINDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem , do not access any indexes at all. In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s).\nTOTAL - The response includes only the aggregate ConsumedCapacity for the operation.\nNONE - No ConsumedCapacity details are included in the response.\n\n

    :type ReturnItemCollectionMetrics: string
    :param ReturnItemCollectionMetrics: Determines whether item collection metrics are returned. If set to SIZE , the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.

    :type UpdateExpression: string
    :param UpdateExpression: An expression that defines one or more attributes to be updated, the action to be performed on them, and new values for them.\nThe following action values are available for UpdateExpression .\n\nSET - Adds one or more attributes and values to an item. If any of these attributes already exist, they are replaced by the new values. You can also use SET to add or subtract from an attribute that is of type Number. For example: SET myNum = myNum + :val SET supports the following functions:\nif_not_exists (path, operand) - if the item does not contain an attribute at the specified path, then if_not_exists evaluates to operand; otherwise, it evaluates to path. You can use this function to avoid overwriting an attribute that may already be present in the item.\nlist_append (operand, operand) - evaluates to a list with a new element added to it. You can append the new element to the start or the end of the list by reversing the order of the operands.\n\n\n\nThese function names are case-sensitive.\n\nREMOVE - Removes one or more attributes from an item.\nADD - Adds the specified value to the item, if the attribute does not already exist. If the attribute does exist, then the behavior of ADD depends on the data type of the attribute:\nIf the existing attribute is a number, and if Value is also a number, then Value is mathematically added to the existing attribute. If Value is a negative number, then it is subtracted from the existing attribute.\n\n\nNote\nIf you use ADD to increment or decrement a number value for an item that doesn\'t exist before the update, DynamoDB uses 0 as the initial value. Similarly, if you use ADD for an existing item to increment or decrement an attribute value that doesn\'t exist before the update, DynamoDB uses 0 as the initial value. For example, suppose that the item you want to update doesn\'t have an attribute named itemcount , but you decide to ADD the number 3 to this attribute anyway. DynamoDB will create the itemcount attribute, set its initial value to 0 , and finally add 3 to it. The result will be a new itemcount attribute in the item, with a value of 3 .\n\n\nIf the existing data type is a set and if Value is also a set, then Value is added to the existing set. For example, if the attribute value is the set [1,2] , and the ADD action specified [3] , then the final attribute value is [1,2,3] . An error occurs if an ADD action is specified for a set attribute and the attribute type specified does not match the existing set type. Both sets must have the same primitive data type. For example, if the existing data type is a set of strings, the Value must also be a set of strings.\n\n\n\n\nWarning\nThe ADD action only supports Number and set data types. In addition, ADD can only be used on top-level attributes, not nested attributes.\n\n\nDELETE - Deletes an element from a set. If a set of values is specified, then those values are subtracted from the old set. For example, if the attribute value was the set [a,b,c] and the DELETE action specifies [a,c] , then the final attribute value is [b] . Specifying an empty set is an error.\n\n\nWarning\nThe DELETE action only supports set data types. In addition, DELETE can only be used on top-level attributes, not nested attributes.\n\nYou can have many actions in a single expression, such as the following: SET a=:value1, b=:value2 DELETE :value3, :value4, :value5\nFor more information on update expressions, see Modifying Items and Attributes in the Amazon DynamoDB Developer Guide .\n

    :type ConditionExpression: string
    :param ConditionExpression: A condition that must be satisfied in order for a conditional update to succeed.\nAn expression can contain any of the following:\n\nFunctions: attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size  These function names are case-sensitive.\nComparison operators: = | <> | < | > | <= | >= | BETWEEN | IN\nLogical operators: AND | OR | NOT\n\nFor more information about condition expressions, see Specifying Conditions in the Amazon DynamoDB Developer Guide .\n

    :type ExpressionAttributeNames: dict
    :param ExpressionAttributeNames: One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames :\n\nTo access an attribute whose name conflicts with a DynamoDB reserved word.\nTo create a placeholder for repeating occurrences of an attribute name in an expression.\nTo prevent special characters in an attribute name from being misinterpreted in an expression.\n\nUse the # character in an expression to dereference an attribute name. For example, consider the following attribute name:\n\nPercentile\n\nThe name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide .) To work around this, you could specify the following for ExpressionAttributeNames :\n\n{'#P':'Percentile'}\n\nYou could then use this substitution in an expression, as in this example:\n\n#P = :val\n\n\nNote\nTokens that begin with the : character are expression attribute values , which are placeholders for the actual value at runtime.\n\nFor more information about expression attribute names, see Specifying Item Attributes in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type ExpressionAttributeValues: dict
    :param ExpressionAttributeValues: One or more values that can be substituted in an expression.\nUse the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:\n\nAvailable | Backordered | Discontinued\nYou would first need to specify ExpressionAttributeValues as follows:\n\n{ ':avail':{'S':'Available'}, ':back':{'S':'Backordered'}, ':disc':{'S':'Discontinued'} }\nYou could then use these values in an expression, such as this:\n\nProductStatus IN (:avail, :back, :disc)\nFor more information on expression attribute values, see Condition Expressions in the Amazon DynamoDB Developer Guide .\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\nS (string) --An attribute of type String. For example:\n\n'S': 'Hello'\n\nN (string) --An attribute of type Number. For example:\n\n'N': '123.45'\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\nB (bytes) --An attribute of type Binary. For example:\n\n'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'\n\nSS (list) --An attribute of type String Set. For example:\n\n'SS': ['Giraffe', 'Hippo' ,'Zebra']\n\n(string) --\n\n\nNS (list) --An attribute of type Number Set. For example:\n\n'NS': ['42.2', '-19', '7.5', '3.14']\nNumbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.\n\n(string) --\n\n\nBS (list) --An attribute of type Binary Set. For example:\n\n'BS': ['U3Vubnk=', 'UmFpbnk=', 'U25vd3k=']\n\n(bytes) --\n\n\nM (dict) --An attribute of type Map. For example:\n\n'M': {'Name': {'S': 'Joe'}, 'Age': {'N': '35'}}\n\n(string) --\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\n\n\nL (list) --An attribute of type List. For example:\n\n'L': [ {'S': 'Cookies'} , {'S': 'Coffee'}, {'N', '3.14159'}]\n\n(dict) --Represents the data for an attribute.\nEach attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.\nFor more information, see Data Types in the Amazon DynamoDB Developer Guide .\n\n\n\nNULL (boolean) --An attribute of type Null. For example:\n\n'NULL': true\n\nBOOL (boolean) --An attribute of type Boolean. For example:\n\n'BOOL': true\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Attributes': {
        'string': {
            'S': 'string',
            'N': 'string',
            'B': b'bytes',
            'SS': [
                'string',
            ],
            'NS': [
                'string',
            ],
            'BS': [
                b'bytes',
            ],
            'M': {
                'string': {'... recursive ...'}
            },
            'L': [
                {'... recursive ...'},
            ],
            'NULL': True|False,
            'BOOL': True|False
        }
    },
    'ConsumedCapacity': {
        'TableName': 'string',
        'CapacityUnits': 123.0,
        'ReadCapacityUnits': 123.0,
        'WriteCapacityUnits': 123.0,
        'Table': {
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'CapacityUnits': 123.0
        },
        'LocalSecondaryIndexes': {
            'string': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            }
        },
        'GlobalSecondaryIndexes': {
            'string': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            }
        }
    },
    'ItemCollectionMetrics': {
        'ItemCollectionKey': {
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        'SizeEstimateRangeGB': [
            123.0,
        ]
    }
}


Response Structure

(dict) --
Represents the output of an UpdateItem operation.

Attributes (dict) --
A map of attribute values as they appear before or after the UpdateItem operation, as determined by the ReturnValues parameter.
The Attributes map is only present if ReturnValues was specified as something other than NONE in the request. Each element represents one attribute.

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true








ConsumedCapacity (dict) --
The capacity units consumed by the UpdateItem operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. ConsumedCapacity is only returned if the ReturnConsumedCapacity parameter was specified. For more information, see Provisioned Throughput in the Amazon DynamoDB Developer Guide .

TableName (string) --
The name of the table that was affected by the operation.

CapacityUnits (float) --
The total number of capacity units consumed by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed by the operation.

WriteCapacityUnits (float) --
The total number of write capacity units consumed by the operation.

Table (dict) --
The amount of throughput consumed on the table affected by the operation.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.



LocalSecondaryIndexes (dict) --
The amount of throughput consumed on each local index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.







GlobalSecondaryIndexes (dict) --
The amount of throughput consumed on each global index affected by the operation.

(string) --

(dict) --
Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits (float) --
The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits (float) --
The total number of write capacity units consumed on a table or an index.

CapacityUnits (float) --
The total number of capacity units consumed on a table or an index.









ItemCollectionMetrics (dict) --
Information about item collections, if any, that were affected by the UpdateItem operation. ItemCollectionMetrics is only returned if the ReturnItemCollectionMetrics parameter was specified. If the table does not have any local secondary indexes, this information is not returned in the response.
Each ItemCollectionMetrics element consists of:

ItemCollectionKey - The partition key value of the item collection. This is the same as the partition key value of the item itself.
SizeEstimateRangeGB - An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit. The estimate is subject to change over time; therefore, do not rely on the precision or accuracy of the estimate.


ItemCollectionKey (dict) --
The partition key value of the item collection. This value is the same as the partition key value of the item.

(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .

S (string) --
An attribute of type String. For example:

"S": "Hello"


N (string) --
An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B (bytes) --
An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS (list) --
An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]


(string) --


NS (list) --
An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string) --


BS (list) --
An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]


(bytes) --


M (dict) --
An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}


(string) --

(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .





L (list) --
An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]


(dict) --
Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .



NULL (boolean) --
An attribute of type Null. For example:

"NULL": true


BOOL (boolean) --
An attribute of type Boolean. For example:

"BOOL": true








SizeEstimateRangeGB (list) --
An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit.
The estimate is subject to change over time; therefore, do not rely on the precision or accuracy of the estimate.

(float) --










Exceptions

DynamoDB.Client.exceptions.ConditionalCheckFailedException
DynamoDB.Client.exceptions.ProvisionedThroughputExceededException
DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.ItemCollectionSizeLimitExceededException
DynamoDB.Client.exceptions.TransactionConflictException
DynamoDB.Client.exceptions.RequestLimitExceeded
DynamoDB.Client.exceptions.InternalServerError

Examples
This example updates an item in the Music table. It adds a new attribute (Year) and modifies the AlbumTitle attribute.  All of the attributes in the item, as they appear after the update, are returned in the response.
response = client.update_item(
    ExpressionAttributeNames={
        '#AT': 'AlbumTitle',
        '#Y': 'Year',
    },
    ExpressionAttributeValues={
        ':t': {
            'S': 'Louder Than Ever',
        },
        ':y': {
            'N': '2015',
        },
    },
    Key={
        'Artist': {
            'S': 'Acme Band',
        },
        'SongTitle': {
            'S': 'Happy Day',
        },
    },
    ReturnValues='ALL_NEW',
    TableName='Music',
    UpdateExpression='SET #Y = :y, #AT = :t',
)

print(response)


Expected Output:
{
    'Attributes': {
        'AlbumTitle': {
            'S': 'Louder Than Ever',
        },
        'Artist': {
            'S': 'Acme Band',
        },
        'SongTitle': {
            'S': 'Happy Day',
        },
        'Year': {
            'N': '2015',
        },
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Attributes': {
            'string': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            }
        },
        'ConsumedCapacity': {
            'TableName': 'string',
            'CapacityUnits': 123.0,
            'ReadCapacityUnits': 123.0,
            'WriteCapacityUnits': 123.0,
            'Table': {
                'ReadCapacityUnits': 123.0,
                'WriteCapacityUnits': 123.0,
                'CapacityUnits': 123.0
            },
            'LocalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            },
            'GlobalSecondaryIndexes': {
                'string': {
                    'ReadCapacityUnits': 123.0,
                    'WriteCapacityUnits': 123.0,
                    'CapacityUnits': 123.0
                }
            }
        },
        'ItemCollectionMetrics': {
            'ItemCollectionKey': {
                'string': {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                }
            },
            'SizeEstimateRangeGB': [
                123.0,
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_table(AttributeDefinitions=None, TableName=None, BillingMode=None, ProvisionedThroughput=None, GlobalSecondaryIndexUpdates=None, StreamSpecification=None, SSESpecification=None, ReplicaUpdates=None):
    """
    Modifies the provisioned throughput settings, global secondary indexes, or DynamoDB Streams settings for a given table.
    You can only perform one of the following operations at once:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example increases the provisioned read and write capacity on the Music table.
    Expected Output:
    
    :example: response = client.update_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'string',
                'AttributeType': 'S'|'N'|'B'
            },
        ],
        TableName='string',
        BillingMode='PROVISIONED'|'PAY_PER_REQUEST',
        ProvisionedThroughput={
            'ReadCapacityUnits': 123,
            'WriteCapacityUnits': 123
        },
        GlobalSecondaryIndexUpdates=[
            {
                'Update': {
                    'IndexName': 'string',
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 123,
                        'WriteCapacityUnits': 123
                    }
                },
                'Create': {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 123,
                        'WriteCapacityUnits': 123
                    }
                },
                'Delete': {
                    'IndexName': 'string'
                }
            },
        ],
        StreamSpecification={
            'StreamEnabled': True|False,
            'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
        },
        SSESpecification={
            'Enabled': True|False,
            'SSEType': 'AES256'|'KMS',
            'KMSMasterKeyId': 'string'
        },
        ReplicaUpdates=[
            {
                'Create': {
                    'RegionName': 'string',
                    'KMSMasterKeyId': 'string',
                    'ProvisionedThroughputOverride': {
                        'ReadCapacityUnits': 123
                    },
                    'GlobalSecondaryIndexes': [
                        {
                            'IndexName': 'string',
                            'ProvisionedThroughputOverride': {
                                'ReadCapacityUnits': 123
                            }
                        },
                    ]
                },
                'Update': {
                    'RegionName': 'string',
                    'KMSMasterKeyId': 'string',
                    'ProvisionedThroughputOverride': {
                        'ReadCapacityUnits': 123
                    },
                    'GlobalSecondaryIndexes': [
                        {
                            'IndexName': 'string',
                            'ProvisionedThroughputOverride': {
                                'ReadCapacityUnits': 123
                            }
                        },
                    ]
                },
                'Delete': {
                    'RegionName': 'string'
                }
            },
        ]
    )
    
    
    :type AttributeDefinitions: list
    :param AttributeDefinitions: An array of attributes that describe the key schema for the table and indexes. If you are adding a new global secondary index to the table, AttributeDefinitions must include the key element(s) of the new index.\n\n(dict) --Represents an attribute for describing the key schema for the table and indexes.\n\nAttributeName (string) -- [REQUIRED]A name for the attribute.\n\nAttributeType (string) -- [REQUIRED]The data type for the attribute, where:\n\nS - the attribute is of type String\nN - the attribute is of type Number\nB - the attribute is of type Binary\n\n\n\n\n\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table to be updated.\n

    :type BillingMode: string
    :param BillingMode: Controls how you are charged for read and write throughput and how you manage capacity. When switching from pay-per-request to provisioned capacity, initial provisioned capacity values must be set. The initial provisioned capacity values are estimated based on the consumed read and write capacity of your table and global secondary indexes over the past 30 minutes.\n\nPROVISIONED - We recommend using PROVISIONED for predictable workloads. PROVISIONED sets the billing mode to Provisioned Mode .\nPAY_PER_REQUEST - We recommend using PAY_PER_REQUEST for unpredictable workloads. PAY_PER_REQUEST sets the billing mode to On-Demand Mode .\n\n

    :type ProvisionedThroughput: dict
    :param ProvisionedThroughput: The new provisioned throughput settings for the specified table or index.\n\nReadCapacityUnits (integer) -- [REQUIRED]The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\nWriteCapacityUnits (integer) -- [REQUIRED]The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\n\n

    :type GlobalSecondaryIndexUpdates: list
    :param GlobalSecondaryIndexUpdates: An array of one or more global secondary indexes for the table. For each index in the array, you can request one action:\n\nCreate - add a new global secondary index to the table.\nUpdate - modify the provisioned throughput settings of an existing global secondary index.\nDelete - remove a global secondary index from the table.\n\nYou can create or delete only one global secondary index per UpdateTable operation.\nFor more information, see Managing Global Secondary Indexes in the Amazon DynamoDB Developer Guide .\n\n(dict) --Represents one of the following:\n\nA new global secondary index to be added to an existing table.\nNew provisioned throughput parameters for an existing global secondary index.\nAn existing global secondary index to be removed from an existing table.\n\n\nUpdate (dict) --The name of an existing global secondary index, along with new provisioned throughput settings to be applied to that index.\n\nIndexName (string) -- [REQUIRED]The name of the global secondary index to be updated.\n\nProvisionedThroughput (dict) -- [REQUIRED]Represents the provisioned throughput settings for the specified global secondary index.\nFor current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .\n\nReadCapacityUnits (integer) -- [REQUIRED]The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\nWriteCapacityUnits (integer) -- [REQUIRED]The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\n\n\n\n\nCreate (dict) --The parameters required for creating a global secondary index on an existing table:\n\nIndexName\nKeySchema\nAttributeDefinitions\nProjection\nProvisionedThroughput\n\n\nIndexName (string) -- [REQUIRED]The name of the global secondary index to be created.\n\nKeySchema (list) -- [REQUIRED]The key schema for the global secondary index.\n\n(dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.\nA KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.\nA KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.\n\nAttributeName (string) -- [REQUIRED]The name of a key attribute.\n\nKeyType (string) -- [REQUIRED]The role that this key attribute will assume:\n\nHASH - partition key\nRANGE - sort key\n\n\nNote\nThe partition key of an item is also known as its hash attribute . The term 'hash attribute' derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.\nThe sort key of an item is also known as its range attribute . The term 'range attribute' derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.\n\n\n\n\n\n\nProjection (dict) -- [REQUIRED]Represents attributes that are copied (projected) from the table into an index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.\n\nProjectionType (string) --The set of attributes that are projected into the index:\n\nKEYS_ONLY - Only the index and primary keys are projected into the index.\nINCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .\nALL - All of the table attributes are projected into the index.\n\n\nNonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.\nFor local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.\n\n(string) --\n\n\n\n\nProvisionedThroughput (dict) --Represents the provisioned throughput settings for the specified global secondary index.\nFor current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .\n\nReadCapacityUnits (integer) -- [REQUIRED]The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\nWriteCapacityUnits (integer) -- [REQUIRED]The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .\nIf read/write capacity mode is PAY_PER_REQUEST the value is set to 0.\n\n\n\n\n\nDelete (dict) --The name of an existing global secondary index to be removed.\n\nIndexName (string) -- [REQUIRED]The name of the global secondary index to be deleted.\n\n\n\n\n\n\n

    :type StreamSpecification: dict
    :param StreamSpecification: Represents the DynamoDB Streams configuration for the table.\n\nNote\nYou receive a ResourceInUseException if you try to enable a stream on a table that already has a stream, or if you try to disable a stream on a table that doesn\'t have a stream.\n\n\nStreamEnabled (boolean) -- [REQUIRED]Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.\n\nStreamViewType (string) --When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are:\n\nKEYS_ONLY - Only the key attributes of the modified item are written to the stream.\nNEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.\nOLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.\nNEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream.\n\n\n\n

    :type SSESpecification: dict
    :param SSESpecification: The new server-side encryption settings for the specified table.\n\nEnabled (boolean) --Indicates whether server-side encryption is done using an AWS managed CMK or an AWS owned CMK. If enabled (true), server-side encryption type is set to KMS and an AWS managed CMK is used (AWS KMS charges apply). If disabled (false) or not specified, server-side encryption is set to AWS owned CMK.\n\nSSEType (string) --Server-side encryption type. The only supported value is:\n\nKMS - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).\n\n\nKMSMasterKeyId (string) --The AWS KMS customer master key (CMK) that should be used for the AWS KMS encryption. To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB customer master key alias/aws/dynamodb.\n\n\n

    :type ReplicaUpdates: list
    :param ReplicaUpdates: A list of replica update actions (create, delete, or update) for the table.\n\nNote\nThis property only applies to Version 2019.11.21 of global tables.\n\n\n(dict) --Represents one of the following:\n\nA new replica to be added to an existing regional table or global table. This request invokes the CreateTableReplica action in the destination Region.\nNew parameters for an existing replica. This request invokes the UpdateTable action in the destination Region.\nAn existing replica to be deleted. The request invokes the DeleteTableReplica action in the destination Region, deleting the replica and all if its items in the destination Region.\n\n\nCreate (dict) --The parameters required for creating a replica for the table.\n\nRegionName (string) -- [REQUIRED]The Region where the new replica will be created.\n\nKMSMasterKeyId (string) --The AWS KMS customer master key (CMK) that should be used for AWS KMS encryption in the new replica. To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB KMS master key alias/aws/dynamodb.\n\nProvisionedThroughputOverride (dict) --Replica-specific provisioned throughput. If not specified, uses the source table\'s provisioned throughput settings.\n\nReadCapacityUnits (integer) --Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.\n\n\n\nGlobalSecondaryIndexes (list) --Replica-specific global secondary index settings.\n\n(dict) --Represents the properties of a replica global secondary index.\n\nIndexName (string) -- [REQUIRED]The name of the global secondary index.\n\nProvisionedThroughputOverride (dict) --Replica table GSI-specific provisioned throughput. If not specified, uses the source table GSI\'s read capacity settings.\n\nReadCapacityUnits (integer) --Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.\n\n\n\n\n\n\n\n\n\nUpdate (dict) --The parameters required for updating a replica for the table.\n\nRegionName (string) -- [REQUIRED]The Region where the replica exists.\n\nKMSMasterKeyId (string) --The AWS KMS customer master key (CMK) of the replica that should be used for AWS KMS encryption. To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB KMS master key alias/aws/dynamodb.\n\nProvisionedThroughputOverride (dict) --Replica-specific provisioned throughput. If not specified, uses the source table\'s provisioned throughput settings.\n\nReadCapacityUnits (integer) --Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.\n\n\n\nGlobalSecondaryIndexes (list) --Replica-specific global secondary index settings.\n\n(dict) --Represents the properties of a replica global secondary index.\n\nIndexName (string) -- [REQUIRED]The name of the global secondary index.\n\nProvisionedThroughputOverride (dict) --Replica table GSI-specific provisioned throughput. If not specified, uses the source table GSI\'s read capacity settings.\n\nReadCapacityUnits (integer) --Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.\n\n\n\n\n\n\n\n\n\nDelete (dict) --The parameters required for deleting a replica for the table.\n\nRegionName (string) -- [REQUIRED]The Region where the replica exists.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TableDescription': {
        'AttributeDefinitions': [
            {
                'AttributeName': 'string',
                'AttributeType': 'S'|'N'|'B'
            },
        ],
        'TableName': 'string',
        'KeySchema': [
            {
                'AttributeName': 'string',
                'KeyType': 'HASH'|'RANGE'
            },
        ],
        'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
        'CreationDateTime': datetime(2015, 1, 1),
        'ProvisionedThroughput': {
            'LastIncreaseDateTime': datetime(2015, 1, 1),
            'LastDecreaseDateTime': datetime(2015, 1, 1),
            'NumberOfDecreasesToday': 123,
            'ReadCapacityUnits': 123,
            'WriteCapacityUnits': 123
        },
        'TableSizeBytes': 123,
        'ItemCount': 123,
        'TableArn': 'string',
        'TableId': 'string',
        'BillingModeSummary': {
            'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
            'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
        },
        'LocalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexArn': 'string'
            },
        ],
        'GlobalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'|'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                'Backfilling': True|False,
                'ProvisionedThroughput': {
                    'LastIncreaseDateTime': datetime(2015, 1, 1),
                    'LastDecreaseDateTime': datetime(2015, 1, 1),
                    'NumberOfDecreasesToday': 123,
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexArn': 'string'
            },
        ],
        'StreamSpecification': {
            'StreamEnabled': True|False,
            'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
        },
        'LatestStreamLabel': 'string',
        'LatestStreamArn': 'string',
        'GlobalTableVersion': 'string',
        'Replicas': [
            {
                'RegionName': 'string',
                'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                'ReplicaStatusDescription': 'string',
                'ReplicaStatusPercentProgress': 'string',
                'KMSMasterKeyId': 'string',
                'ProvisionedThroughputOverride': {
                    'ReadCapacityUnits': 123
                },
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'ProvisionedThroughputOverride': {
                            'ReadCapacityUnits': 123
                        }
                    },
                ]
            },
        ],
        'RestoreSummary': {
            'SourceBackupArn': 'string',
            'SourceTableArn': 'string',
            'RestoreDateTime': datetime(2015, 1, 1),
            'RestoreInProgress': True|False
        },
        'SSEDescription': {
            'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
            'SSEType': 'AES256'|'KMS',
            'KMSMasterKeyArn': 'string',
            'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
        },
        'ArchivalSummary': {
            'ArchivalDateTime': datetime(2015, 1, 1),
            'ArchivalReason': 'string',
            'ArchivalBackupArn': 'string'
        }
    }
}


Response Structure

(dict) --
Represents the output of an UpdateTable operation.

TableDescription (dict) --
Represents the properties of the table.

AttributeDefinitions (list) --
An array of AttributeDefinition objects. Each of these objects describes one attribute in the table and index key schema.
Each AttributeDefinition object in this array is composed of:

AttributeName - The name of the attribute.
AttributeType - The data type for the attribute.


(dict) --
Represents an attribute for describing the key schema for the table and indexes.

AttributeName (string) --
A name for the attribute.

AttributeType (string) --
The data type for the attribute, where:

S - the attribute is of type String
N - the attribute is of type Number
B - the attribute is of type Binary






TableName (string) --
The name of the table.

KeySchema (list) --
The primary key structure for the table. Each KeySchemaElement consists of:

AttributeName - The name of the attribute.
KeyType - The role of the attribute:
HASH - partition key
RANGE - sort key




Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

For more information about primary keys, see Primary Key in the Amazon DynamoDB Developer Guide .

(dict) --
Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --
The name of a key attribute.

KeyType (string) --
The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






TableStatus (string) --
The current state of the table:

CREATING - The table is being created.
UPDATING - The table is being updated.
DELETING - The table is being deleted.
ACTIVE - The table is ready for use.
INACCESSIBLE_ENCRYPTION_CREDENTIALS - The AWS KMS key used to encrypt the table in inaccessible. Table operations may fail due to failure to use the AWS KMS key. DynamoDB will initiate the table archival process when a table\'s AWS KMS key remains inaccessible for more than seven days.
ARCHIVING - The table is being archived. Operations are not allowed until archival is complete.
ARCHIVED - The table has been archived. See the ArchivalReason for more information.


CreationDateTime (datetime) --
The date and time when the table was created, in UNIX epoch time format.

ProvisionedThroughput (dict) --
The provisioned throughput settings for the table, consisting of read and write capacity units, along with data about increases and decreases.

LastIncreaseDateTime (datetime) --
The date and time of the last provisioned throughput increase for this table.

LastDecreaseDateTime (datetime) --
The date and time of the last provisioned throughput decrease for this table.

NumberOfDecreasesToday (integer) --
The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see Limits in the Amazon DynamoDB Developer Guide .

ReadCapacityUnits (integer) --
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 ReadCapacityUnits per second provides 100 eventually consistent ReadCapacityUnits per second.

WriteCapacityUnits (integer) --
The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException .



TableSizeBytes (integer) --
The total size of the specified table, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --
The number of items in the specified table. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

TableArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the table.

TableId (string) --
Unique identifier for the table for which the backup was created.

BillingModeSummary (dict) --
Contains the details for the read/write capacity mode.

BillingMode (string) --
Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.

PROVISIONED - Sets the read/write capacity mode to PROVISIONED . We recommend using PROVISIONED for predictable workloads.
PAY_PER_REQUEST - Sets the read/write capacity mode to PAY_PER_REQUEST . We recommend using PAY_PER_REQUEST for unpredictable workloads.


LastUpdateToPayPerRequestDateTime (datetime) --
Represents the time when PAY_PER_REQUEST was last set as the read/write capacity mode.



LocalSecondaryIndexes (list) --
Represents one or more local secondary indexes on the table. Each index is scoped to a given partition key value. Tables with one or more local secondary indexes are subject to an item collection size limit, where the amount of data within a given item collection cannot exceed 10 GB. Each element is composed of:

IndexName - The name of the local secondary index.
KeySchema - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
Projection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
ProjectionType - One of the following:
KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes , summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.


IndexSizeBytes - Represents the total size of the index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
ItemCount - Represents the number of items in the index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

If the table is in the DELETING state, no information about indexes will be returned.

(dict) --
Represents the properties of a local secondary index.

IndexName (string) --
Represents the name of the local secondary index.

KeySchema (list) --
The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --
Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --
The name of a key attribute.

KeyType (string) --
The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --
Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --
The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --
Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --




IndexSizeBytes (integer) --
The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --
The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

IndexArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the index.





GlobalSecondaryIndexes (list) --
The global secondary indexes, if any, on the table. Each index is scoped to a given partition key value. Each element is composed of:

Backfilling - If true, then the index is currently in the backfilling phase. Backfilling occurs only when a new global secondary index is added to the table. It is the process by which DynamoDB populates the new index with data from the table. (This attribute does not appear for indexes that were created during a CreateTable operation.)  You can delete an index that is being created during the Backfilling phase when IndexStatus is set to CREATING and Backfilling is true. You can\'t delete the index that is being created when IndexStatus is set to CREATING and Backfilling is false. (This attribute does not appear for indexes that were created during a CreateTable operation.)
IndexName - The name of the global secondary index.
IndexSizeBytes - The total size of the global secondary index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
IndexStatus - The current status of the global secondary index:
CREATING - The index is being created.
UPDATING - The index is being updated.
DELETING - The index is being deleted.
ACTIVE - The index is ready for use.


ItemCount - The number of items in the global secondary index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
KeySchema - Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.
Projection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:
ProjectionType - One of the following:
KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes , summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.


ProvisionedThroughput - The provisioned throughput settings for the global secondary index, consisting of read and write capacity units, along with data about increases and decreases.

If the table is in the DELETING state, no information about indexes will be returned.

(dict) --
Represents the properties of a global secondary index.

IndexName (string) --
The name of the global secondary index.

KeySchema (list) --
The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.


(dict) --
Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.

AttributeName (string) --
The name of a key attribute.

KeyType (string) --
The role that this key attribute will assume:

HASH - partition key
RANGE - sort key


Note
The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.






Projection (dict) --
Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

ProjectionType (string) --
The set of attributes that are projected into the index:

KEYS_ONLY - Only the index and primary keys are projected into the index.
INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
ALL - All of the table attributes are projected into the index.


NonKeyAttributes (list) --
Represents the non-key attribute names which will be projected into the index.
For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

(string) --




IndexStatus (string) --
The current state of the global secondary index:

CREATING - The index is being created.
UPDATING - The index is being updated.
DELETING - The index is being deleted.
ACTIVE - The index is ready for use.


Backfilling (boolean) --
Indicates whether the index is currently backfilling. Backfilling is the process of reading items from the table and determining whether they can be added to the index. (Not all items will qualify: For example, a partition key cannot have any duplicate values.) If an item can be added to the index, DynamoDB will do so. After all items have been processed, the backfilling operation is complete and Backfilling is false.
You can delete an index that is being created during the Backfilling phase when IndexStatus is set to CREATING and Backfilling is true. You can\'t delete the index that is being created when IndexStatus is set to CREATING and Backfilling is false.

Note
For indexes that were created during a CreateTable operation, the Backfilling attribute does not appear in the DescribeTable output.


ProvisionedThroughput (dict) --
Represents the provisioned throughput settings for the specified global secondary index.
For current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .

LastIncreaseDateTime (datetime) --
The date and time of the last provisioned throughput increase for this table.

LastDecreaseDateTime (datetime) --
The date and time of the last provisioned throughput decrease for this table.

NumberOfDecreasesToday (integer) --
The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see Limits in the Amazon DynamoDB Developer Guide .

ReadCapacityUnits (integer) --
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 ReadCapacityUnits per second provides 100 eventually consistent ReadCapacityUnits per second.

WriteCapacityUnits (integer) --
The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException .



IndexSizeBytes (integer) --
The total size of the specified index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

ItemCount (integer) --
The number of items in the specified index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

IndexArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the index.





StreamSpecification (dict) --
The current DynamoDB Streams configuration for the table.

StreamEnabled (boolean) --
Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.

StreamViewType (string) --
When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are:

KEYS_ONLY - Only the key attributes of the modified item are written to the stream.
NEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.
OLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.
NEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream.




LatestStreamLabel (string) --
A timestamp, in ISO 8601 format, for this stream.
Note that LatestStreamLabel is not a unique identifier for the stream, because it is possible that a stream from another table might have the same timestamp. However, the combination of the following three elements is guaranteed to be unique:

AWS customer ID
Table name
StreamLabel


LatestStreamArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the latest stream for this table.

GlobalTableVersion (string) --
Represents the version of global tables in use, if the table is replicated across AWS Regions.

Replicas (list) --
Represents replicas of the table.

(dict) --
Contains the details of the replica.

RegionName (string) --
The name of the Region.

ReplicaStatus (string) --
The current state of the replica:

CREATING - The replica is being created.
UPDATING - The replica is being updated.
DELETING - The replica is being deleted.
ACTIVE - The replica is ready for use.


ReplicaStatusDescription (string) --
Detailed information about the replica status.

ReplicaStatusPercentProgress (string) --
Specifies the progress of a Create, Update, or Delete action on the replica as a percentage.

KMSMasterKeyId (string) --
The AWS KMS customer master key (CMK) of the replica that will be used for AWS KMS encryption.

ProvisionedThroughputOverride (dict) --
Replica-specific provisioned throughput. If not described, uses the source table\'s provisioned throughput settings.

ReadCapacityUnits (integer) --
Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.



GlobalSecondaryIndexes (list) --
Replica-specific global secondary index settings.

(dict) --
Represents the properties of a replica global secondary index.

IndexName (string) --
The name of the global secondary index.

ProvisionedThroughputOverride (dict) --
If not described, uses the source table GSI\'s read capacity settings.

ReadCapacityUnits (integer) --
Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.











RestoreSummary (dict) --
Contains details for the restore.

SourceBackupArn (string) --
The Amazon Resource Name (ARN) of the backup from which the table was restored.

SourceTableArn (string) --
The ARN of the source table of the backup that is being restored.

RestoreDateTime (datetime) --
Point in time or source backup time.

RestoreInProgress (boolean) --
Indicates if a restore is in progress or not.



SSEDescription (dict) --
The description of the server-side encryption status on the specified table.

Status (string) --
Represents the current state of server-side encryption. The only supported values are:

ENABLED - Server-side encryption is enabled.
UPDATING - Server-side encryption is being updated.


SSEType (string) --
Server-side encryption type. The only supported value is:

KMS - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).


KMSMasterKeyArn (string) --
The AWS KMS customer master key (CMK) ARN used for the AWS KMS encryption.

InaccessibleEncryptionDateTime (datetime) --
Indicates the time, in UNIX epoch date format, when DynamoDB detected that the table\'s AWS KMS key was inaccessible. This attribute will automatically be cleared when DynamoDB detects that the table\'s AWS KMS key is accessible again. DynamoDB will initiate the table archival process when table\'s AWS KMS key remains inaccessible for more than seven days from this date.



ArchivalSummary (dict) --
Contains information about the table archive.

ArchivalDateTime (datetime) --
The date and time when table archival was initiated by DynamoDB, in UNIX epoch time format.

ArchivalReason (string) --
The reason DynamoDB archived the table. Currently, the only possible value is:

INACCESSIBLE_ENCRYPTION_CREDENTIALS - The table was archived due to the table\'s AWS KMS key being inaccessible for more than seven days. An On-Demand backup was created at the archival time.


ArchivalBackupArn (string) --
The Amazon Resource Name (ARN) of the backup the table was archived to, when applicable in the archival reason. If you wish to restore this backup to the same table name, you will need to delete the original table.











Exceptions

DynamoDB.Client.exceptions.ResourceInUseException
DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.LimitExceededException
DynamoDB.Client.exceptions.InternalServerError

Examples
This example increases the provisioned read and write capacity on the Music table.
response = client.update_table(
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10,
    },
    TableName='MusicCollection',
)

print(response)


Expected Output:
{
    'TableDescription': {
        'AttributeDefinitions': [
            {
                'AttributeName': 'Artist',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'SongTitle',
                'AttributeType': 'S',
            },
        ],
        'CreationDateTime': datetime(2015, 1, 21, 19, 2, 32, 2, 21, 0),
        'ItemCount': 0,
        'KeySchema': [
            {
                'AttributeName': 'Artist',
                'KeyType': 'HASH',
            },
            {
                'AttributeName': 'SongTitle',
                'KeyType': 'RANGE',
            },
        ],
        'ProvisionedThroughput': {
            'LastIncreaseDateTime': datetime(2015, 1, 21, 21, 12, 39, 2, 21, 0),
            'NumberOfDecreasesToday': 1,
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        },
        'TableName': 'MusicCollection',
        'TableSizeBytes': 0,
        'TableStatus': 'UPDATING',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TableDescription': {
            'AttributeDefinitions': [
                {
                    'AttributeName': 'string',
                    'AttributeType': 'S'|'N'|'B'
                },
            ],
            'TableName': 'string',
            'KeySchema': [
                {
                    'AttributeName': 'string',
                    'KeyType': 'HASH'|'RANGE'
                },
            ],
            'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
            'CreationDateTime': datetime(2015, 1, 1),
            'ProvisionedThroughput': {
                'LastIncreaseDateTime': datetime(2015, 1, 1),
                'LastDecreaseDateTime': datetime(2015, 1, 1),
                'NumberOfDecreasesToday': 123,
                'ReadCapacityUnits': 123,
                'WriteCapacityUnits': 123
            },
            'TableSizeBytes': 123,
            'ItemCount': 123,
            'TableArn': 'string',
            'TableId': 'string',
            'BillingModeSummary': {
                'BillingMode': 'PROVISIONED'|'PAY_PER_REQUEST',
                'LastUpdateToPayPerRequestDateTime': datetime(2015, 1, 1)
            },
            'LocalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'IndexSizeBytes': 123,
                    'ItemCount': 123,
                    'IndexArn': 'string'
                },
            ],
            'GlobalSecondaryIndexes': [
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                    'Backfilling': True|False,
                    'ProvisionedThroughput': {
                        'LastIncreaseDateTime': datetime(2015, 1, 1),
                        'LastDecreaseDateTime': datetime(2015, 1, 1),
                        'NumberOfDecreasesToday': 123,
                        'ReadCapacityUnits': 123,
                        'WriteCapacityUnits': 123
                    },
                    'IndexSizeBytes': 123,
                    'ItemCount': 123,
                    'IndexArn': 'string'
                },
            ],
            'StreamSpecification': {
                'StreamEnabled': True|False,
                'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
            },
            'LatestStreamLabel': 'string',
            'LatestStreamArn': 'string',
            'GlobalTableVersion': 'string',
            'Replicas': [
                {
                    'RegionName': 'string',
                    'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE',
                    'ReplicaStatusDescription': 'string',
                    'ReplicaStatusPercentProgress': 'string',
                    'KMSMasterKeyId': 'string',
                    'ProvisionedThroughputOverride': {
                        'ReadCapacityUnits': 123
                    },
                    'GlobalSecondaryIndexes': [
                        {
                            'IndexName': 'string',
                            'ProvisionedThroughputOverride': {
                                'ReadCapacityUnits': 123
                            }
                        },
                    ]
                },
            ],
            'RestoreSummary': {
                'SourceBackupArn': 'string',
                'SourceTableArn': 'string',
                'RestoreDateTime': datetime(2015, 1, 1),
                'RestoreInProgress': True|False
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'|'UPDATING',
                'SSEType': 'AES256'|'KMS',
                'KMSMasterKeyArn': 'string',
                'InaccessibleEncryptionDateTime': datetime(2015, 1, 1)
            },
            'ArchivalSummary': {
                'ArchivalDateTime': datetime(2015, 1, 1),
                'ArchivalReason': 'string',
                'ArchivalBackupArn': 'string'
            }
        }
    }
    
    
    :returns: 
    AttributeDefinitions (list) -- An array of attributes that describe the key schema for the table and indexes. If you are adding a new global secondary index to the table, AttributeDefinitions must include the key element(s) of the new index.
    
    (dict) --Represents an attribute for describing the key schema for the table and indexes.
    
    AttributeName (string) -- [REQUIRED]A name for the attribute.
    
    AttributeType (string) -- [REQUIRED]The data type for the attribute, where:
    
    S - the attribute is of type String
    N - the attribute is of type Number
    B - the attribute is of type Binary
    
    
    
    
    
    
    TableName (string) -- [REQUIRED]
    The name of the table to be updated.
    
    BillingMode (string) -- Controls how you are charged for read and write throughput and how you manage capacity. When switching from pay-per-request to provisioned capacity, initial provisioned capacity values must be set. The initial provisioned capacity values are estimated based on the consumed read and write capacity of your table and global secondary indexes over the past 30 minutes.
    
    PROVISIONED - We recommend using PROVISIONED for predictable workloads. PROVISIONED sets the billing mode to Provisioned Mode .
    PAY_PER_REQUEST - We recommend using PAY_PER_REQUEST for unpredictable workloads. PAY_PER_REQUEST sets the billing mode to On-Demand Mode .
    
    
    ProvisionedThroughput (dict) -- The new provisioned throughput settings for the specified table or index.
    
    ReadCapacityUnits (integer) -- [REQUIRED]The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
    If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.
    
    WriteCapacityUnits (integer) -- [REQUIRED]The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
    If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.
    
    
    
    GlobalSecondaryIndexUpdates (list) -- An array of one or more global secondary indexes for the table. For each index in the array, you can request one action:
    
    Create - add a new global secondary index to the table.
    Update - modify the provisioned throughput settings of an existing global secondary index.
    Delete - remove a global secondary index from the table.
    
    You can create or delete only one global secondary index per UpdateTable operation.
    For more information, see Managing Global Secondary Indexes in the Amazon DynamoDB Developer Guide .
    
    (dict) --Represents one of the following:
    
    A new global secondary index to be added to an existing table.
    New provisioned throughput parameters for an existing global secondary index.
    An existing global secondary index to be removed from an existing table.
    
    
    Update (dict) --The name of an existing global secondary index, along with new provisioned throughput settings to be applied to that index.
    
    IndexName (string) -- [REQUIRED]The name of the global secondary index to be updated.
    
    ProvisionedThroughput (dict) -- [REQUIRED]Represents the provisioned throughput settings for the specified global secondary index.
    For current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .
    
    ReadCapacityUnits (integer) -- [REQUIRED]The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
    If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.
    
    WriteCapacityUnits (integer) -- [REQUIRED]The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
    If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.
    
    
    
    
    
    Create (dict) --The parameters required for creating a global secondary index on an existing table:
    
    IndexName
    KeySchema
    AttributeDefinitions
    Projection
    ProvisionedThroughput
    
    
    IndexName (string) -- [REQUIRED]The name of the global secondary index to be created.
    
    KeySchema (list) -- [REQUIRED]The key schema for the global secondary index.
    
    (dict) --Represents a single element of a key schema. A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
    A KeySchemaElement represents exactly one attribute of the primary key. For example, a simple primary key would be represented by one KeySchemaElement (for the partition key). A composite primary key would require one KeySchemaElement for the partition key, and another KeySchemaElement for the sort key.
    A KeySchemaElement must be a scalar, top-level attribute (not a nested attribute). The data type must be one of String, Number, or Binary. The attribute cannot be nested within a List or a Map.
    
    AttributeName (string) -- [REQUIRED]The name of a key attribute.
    
    KeyType (string) -- [REQUIRED]The role that this key attribute will assume:
    
    HASH - partition key
    RANGE - sort key
    
    
    Note
    The partition key of an item is also known as its hash attribute . The term "hash attribute" derives from DynamoDB\'s usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
    The sort key of an item is also known as its range attribute . The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.
    
    
    
    
    
    
    Projection (dict) -- [REQUIRED]Represents attributes that are copied (projected) from the table into an index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.
    
    ProjectionType (string) --The set of attributes that are projected into the index:
    
    KEYS_ONLY - Only the index and primary keys are projected into the index.
    INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes is in NonKeyAttributes .
    ALL - All of the table attributes are projected into the index.
    
    
    NonKeyAttributes (list) --Represents the non-key attribute names which will be projected into the index.
    For local secondary indexes, the total count of NonKeyAttributes summed across all of the local secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.
    
    (string) --
    
    
    
    
    ProvisionedThroughput (dict) --Represents the provisioned throughput settings for the specified global secondary index.
    For current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide .
    
    ReadCapacityUnits (integer) -- [REQUIRED]The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
    If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.
    
    WriteCapacityUnits (integer) -- [REQUIRED]The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException . For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide .
    If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.
    
    
    
    
    
    Delete (dict) --The name of an existing global secondary index to be removed.
    
    IndexName (string) -- [REQUIRED]The name of the global secondary index to be deleted.
    
    
    
    
    
    
    
    StreamSpecification (dict) -- Represents the DynamoDB Streams configuration for the table.
    
    Note
    You receive a ResourceInUseException if you try to enable a stream on a table that already has a stream, or if you try to disable a stream on a table that doesn\'t have a stream.
    
    
    StreamEnabled (boolean) -- [REQUIRED]Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.
    
    StreamViewType (string) --When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are:
    
    KEYS_ONLY - Only the key attributes of the modified item are written to the stream.
    NEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.
    OLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.
    NEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream.
    
    
    
    
    SSESpecification (dict) -- The new server-side encryption settings for the specified table.
    
    Enabled (boolean) --Indicates whether server-side encryption is done using an AWS managed CMK or an AWS owned CMK. If enabled (true), server-side encryption type is set to KMS and an AWS managed CMK is used (AWS KMS charges apply). If disabled (false) or not specified, server-side encryption is set to AWS owned CMK.
    
    SSEType (string) --Server-side encryption type. The only supported value is:
    
    KMS - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).
    
    
    KMSMasterKeyId (string) --The AWS KMS customer master key (CMK) that should be used for the AWS KMS encryption. To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB customer master key alias/aws/dynamodb.
    
    
    
    ReplicaUpdates (list) -- A list of replica update actions (create, delete, or update) for the table.
    
    Note
    This property only applies to Version 2019.11.21 of global tables.
    
    
    (dict) --Represents one of the following:
    
    A new replica to be added to an existing regional table or global table. This request invokes the CreateTableReplica action in the destination Region.
    New parameters for an existing replica. This request invokes the UpdateTable action in the destination Region.
    An existing replica to be deleted. The request invokes the DeleteTableReplica action in the destination Region, deleting the replica and all if its items in the destination Region.
    
    
    Create (dict) --The parameters required for creating a replica for the table.
    
    RegionName (string) -- [REQUIRED]The Region where the new replica will be created.
    
    KMSMasterKeyId (string) --The AWS KMS customer master key (CMK) that should be used for AWS KMS encryption in the new replica. To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB KMS master key alias/aws/dynamodb.
    
    ProvisionedThroughputOverride (dict) --Replica-specific provisioned throughput. If not specified, uses the source table\'s provisioned throughput settings.
    
    ReadCapacityUnits (integer) --Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.
    
    
    
    GlobalSecondaryIndexes (list) --Replica-specific global secondary index settings.
    
    (dict) --Represents the properties of a replica global secondary index.
    
    IndexName (string) -- [REQUIRED]The name of the global secondary index.
    
    ProvisionedThroughputOverride (dict) --Replica table GSI-specific provisioned throughput. If not specified, uses the source table GSI\'s read capacity settings.
    
    ReadCapacityUnits (integer) --Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.
    
    
    
    
    
    
    
    
    
    Update (dict) --The parameters required for updating a replica for the table.
    
    RegionName (string) -- [REQUIRED]The Region where the replica exists.
    
    KMSMasterKeyId (string) --The AWS KMS customer master key (CMK) of the replica that should be used for AWS KMS encryption. To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB KMS master key alias/aws/dynamodb.
    
    ProvisionedThroughputOverride (dict) --Replica-specific provisioned throughput. If not specified, uses the source table\'s provisioned throughput settings.
    
    ReadCapacityUnits (integer) --Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.
    
    
    
    GlobalSecondaryIndexes (list) --Replica-specific global secondary index settings.
    
    (dict) --Represents the properties of a replica global secondary index.
    
    IndexName (string) -- [REQUIRED]The name of the global secondary index.
    
    ProvisionedThroughputOverride (dict) --Replica table GSI-specific provisioned throughput. If not specified, uses the source table GSI\'s read capacity settings.
    
    ReadCapacityUnits (integer) --Replica-specific read capacity units. If not specified, uses the source table\'s read capacity settings.
    
    
    
    
    
    
    
    
    
    Delete (dict) --The parameters required for deleting a replica for the table.
    
    RegionName (string) -- [REQUIRED]The Region where the replica exists.
    
    
    
    
    
    
    
    
    """
    pass

def update_table_replica_auto_scaling(GlobalSecondaryIndexUpdates=None, TableName=None, ProvisionedWriteCapacityAutoScalingUpdate=None, ReplicaUpdates=None):
    """
    Updates auto scaling settings on your global tables at once.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_table_replica_auto_scaling(
        GlobalSecondaryIndexUpdates=[
            {
                'IndexName': 'string',
                'ProvisionedWriteCapacityAutoScalingUpdate': {
                    'MinimumUnits': 123,
                    'MaximumUnits': 123,
                    'AutoScalingDisabled': True|False,
                    'AutoScalingRoleArn': 'string',
                    'ScalingPolicyUpdate': {
                        'PolicyName': 'string',
                        'TargetTrackingScalingPolicyConfiguration': {
                            'DisableScaleIn': True|False,
                            'ScaleInCooldown': 123,
                            'ScaleOutCooldown': 123,
                            'TargetValue': 123.0
                        }
                    }
                }
            },
        ],
        TableName='string',
        ProvisionedWriteCapacityAutoScalingUpdate={
            'MinimumUnits': 123,
            'MaximumUnits': 123,
            'AutoScalingDisabled': True|False,
            'AutoScalingRoleArn': 'string',
            'ScalingPolicyUpdate': {
                'PolicyName': 'string',
                'TargetTrackingScalingPolicyConfiguration': {
                    'DisableScaleIn': True|False,
                    'ScaleInCooldown': 123,
                    'ScaleOutCooldown': 123,
                    'TargetValue': 123.0
                }
            }
        },
        ReplicaUpdates=[
            {
                'RegionName': 'string',
                'ReplicaGlobalSecondaryIndexUpdates': [
                    {
                        'IndexName': 'string',
                        'ProvisionedReadCapacityAutoScalingUpdate': {
                            'MinimumUnits': 123,
                            'MaximumUnits': 123,
                            'AutoScalingDisabled': True|False,
                            'AutoScalingRoleArn': 'string',
                            'ScalingPolicyUpdate': {
                                'PolicyName': 'string',
                                'TargetTrackingScalingPolicyConfiguration': {
                                    'DisableScaleIn': True|False,
                                    'ScaleInCooldown': 123,
                                    'ScaleOutCooldown': 123,
                                    'TargetValue': 123.0
                                }
                            }
                        }
                    },
                ],
                'ReplicaProvisionedReadCapacityAutoScalingUpdate': {
                    'MinimumUnits': 123,
                    'MaximumUnits': 123,
                    'AutoScalingDisabled': True|False,
                    'AutoScalingRoleArn': 'string',
                    'ScalingPolicyUpdate': {
                        'PolicyName': 'string',
                        'TargetTrackingScalingPolicyConfiguration': {
                            'DisableScaleIn': True|False,
                            'ScaleInCooldown': 123,
                            'ScaleOutCooldown': 123,
                            'TargetValue': 123.0
                        }
                    }
                }
            },
        ]
    )
    
    
    :type GlobalSecondaryIndexUpdates: list
    :param GlobalSecondaryIndexUpdates: Represents the auto scaling settings of the global secondary indexes of the replica to be updated.\n\n(dict) --Represents the auto scaling settings of a global secondary index for a global table that will be modified.\n\nIndexName (string) --The name of the global secondary index.\n\nProvisionedWriteCapacityAutoScalingUpdate (dict) --Represents the auto scaling settings to be modified for a global table or global secondary index.\n\nMinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.\n\nMaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.\n\nAutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.\n\nAutoScalingRoleArn (string) --Role ARN used for configuring auto scaling policy.\n\nScalingPolicyUpdate (dict) --The scaling policy to apply for scaling target global table or global secondary index capacity units.\n\nPolicyName (string) --The name of the scaling policy.\n\nTargetTrackingScalingPolicyConfiguration (dict) -- [REQUIRED]Represents a target tracking scaling policy configuration.\n\nDisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.\n\nScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.\n\nScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.\n\nTargetValue (float) -- [REQUIRED]The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).\n\n\n\n\n\n\n\n\n\n\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the global table to be updated.\n

    :type ProvisionedWriteCapacityAutoScalingUpdate: dict
    :param ProvisionedWriteCapacityAutoScalingUpdate: Represents the auto scaling settings to be modified for a global table or global secondary index.\n\nMinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.\n\nMaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.\n\nAutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.\n\nAutoScalingRoleArn (string) --Role ARN used for configuring auto scaling policy.\n\nScalingPolicyUpdate (dict) --The scaling policy to apply for scaling target global table or global secondary index capacity units.\n\nPolicyName (string) --The name of the scaling policy.\n\nTargetTrackingScalingPolicyConfiguration (dict) -- [REQUIRED]Represents a target tracking scaling policy configuration.\n\nDisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.\n\nScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.\n\nScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.\n\nTargetValue (float) -- [REQUIRED]The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).\n\n\n\n\n\n\n

    :type ReplicaUpdates: list
    :param ReplicaUpdates: Represents the auto scaling settings of replicas of the table that will be modified.\n\n(dict) --Represents the auto scaling settings of a replica that will be modified.\n\nRegionName (string) -- [REQUIRED]The Region where the replica exists.\n\nReplicaGlobalSecondaryIndexUpdates (list) --Represents the auto scaling settings of global secondary indexes that will be modified.\n\n(dict) --Represents the auto scaling settings of a global secondary index for a replica that will be modified.\n\nIndexName (string) --The name of the global secondary index.\n\nProvisionedReadCapacityAutoScalingUpdate (dict) --Represents the auto scaling settings to be modified for a global table or global secondary index.\n\nMinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.\n\nMaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.\n\nAutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.\n\nAutoScalingRoleArn (string) --Role ARN used for configuring auto scaling policy.\n\nScalingPolicyUpdate (dict) --The scaling policy to apply for scaling target global table or global secondary index capacity units.\n\nPolicyName (string) --The name of the scaling policy.\n\nTargetTrackingScalingPolicyConfiguration (dict) -- [REQUIRED]Represents a target tracking scaling policy configuration.\n\nDisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.\n\nScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.\n\nScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.\n\nTargetValue (float) -- [REQUIRED]The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).\n\n\n\n\n\n\n\n\n\n\n\nReplicaProvisionedReadCapacityAutoScalingUpdate (dict) --Represents the auto scaling settings to be modified for a global table or global secondary index.\n\nMinimumUnits (integer) --The minimum capacity units that a global table or global secondary index should be scaled down to.\n\nMaximumUnits (integer) --The maximum capacity units that a global table or global secondary index should be scaled up to.\n\nAutoScalingDisabled (boolean) --Disabled auto scaling for this global table or global secondary index.\n\nAutoScalingRoleArn (string) --Role ARN used for configuring auto scaling policy.\n\nScalingPolicyUpdate (dict) --The scaling policy to apply for scaling target global table or global secondary index capacity units.\n\nPolicyName (string) --The name of the scaling policy.\n\nTargetTrackingScalingPolicyConfiguration (dict) -- [REQUIRED]Represents a target tracking scaling policy configuration.\n\nDisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.\n\nScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.\n\nScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.\n\nTargetValue (float) -- [REQUIRED]The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).\n\n\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TableAutoScalingDescription': {
        'TableName': 'string',
        'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
        'Replicas': [
            {
                'RegionName': 'string',
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                        'ProvisionedReadCapacityAutoScalingSettings': {
                            'MinimumUnits': 123,
                            'MaximumUnits': 123,
                            'AutoScalingDisabled': True|False,
                            'AutoScalingRoleArn': 'string',
                            'ScalingPolicies': [
                                {
                                    'PolicyName': 'string',
                                    'TargetTrackingScalingPolicyConfiguration': {
                                        'DisableScaleIn': True|False,
                                        'ScaleInCooldown': 123,
                                        'ScaleOutCooldown': 123,
                                        'TargetValue': 123.0
                                    }
                                },
                            ]
                        },
                        'ProvisionedWriteCapacityAutoScalingSettings': {
                            'MinimumUnits': 123,
                            'MaximumUnits': 123,
                            'AutoScalingDisabled': True|False,
                            'AutoScalingRoleArn': 'string',
                            'ScalingPolicies': [
                                {
                                    'PolicyName': 'string',
                                    'TargetTrackingScalingPolicyConfiguration': {
                                        'DisableScaleIn': True|False,
                                        'ScaleInCooldown': 123,
                                        'ScaleOutCooldown': 123,
                                        'TargetValue': 123.0
                                    }
                                },
                            ]
                        }
                    },
                ],
                'ReplicaProvisionedReadCapacityAutoScalingSettings': {
                    'MinimumUnits': 123,
                    'MaximumUnits': 123,
                    'AutoScalingDisabled': True|False,
                    'AutoScalingRoleArn': 'string',
                    'ScalingPolicies': [
                        {
                            'PolicyName': 'string',
                            'TargetTrackingScalingPolicyConfiguration': {
                                'DisableScaleIn': True|False,
                                'ScaleInCooldown': 123,
                                'ScaleOutCooldown': 123,
                                'TargetValue': 123.0
                            }
                        },
                    ]
                },
                'ReplicaProvisionedWriteCapacityAutoScalingSettings': {
                    'MinimumUnits': 123,
                    'MaximumUnits': 123,
                    'AutoScalingDisabled': True|False,
                    'AutoScalingRoleArn': 'string',
                    'ScalingPolicies': [
                        {
                            'PolicyName': 'string',
                            'TargetTrackingScalingPolicyConfiguration': {
                                'DisableScaleIn': True|False,
                                'ScaleInCooldown': 123,
                                'ScaleOutCooldown': 123,
                                'TargetValue': 123.0
                            }
                        },
                    ]
                },
                'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE'
            },
        ]
    }
}


Response Structure

(dict) --

TableAutoScalingDescription (dict) --
Returns information about the auto scaling settings of a table with replicas.

TableName (string) --
The name of the table.

TableStatus (string) --
The current state of the table:

CREATING - The table is being created.
UPDATING - The table is being updated.
DELETING - The table is being deleted.
ACTIVE - The table is ready for use.


Replicas (list) --
Represents replicas of the global table.

(dict) --
Represents the auto scaling settings of the replica.

RegionName (string) --
The Region where the replica exists.

GlobalSecondaryIndexes (list) --
Replica-specific global secondary index auto scaling settings.

(dict) --
Represents the auto scaling configuration for a replica global secondary index.

IndexName (string) --
The name of the global secondary index.

IndexStatus (string) --
The current state of the replica global secondary index:

CREATING - The index is being created.
UPDATING - The index is being updated.
DELETING - The index is being deleted.
ACTIVE - The index is ready for use.


ProvisionedReadCapacityAutoScalingSettings (dict) --
Represents the auto scaling settings for a global table or global secondary index.

MinimumUnits (integer) --
The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --
The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --
Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --
Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --
Information about the scaling policies.

(dict) --
Represents the properties of the scaling policy.

PolicyName (string) --
The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --
Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --
Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --
The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --
The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --
The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).









ProvisionedWriteCapacityAutoScalingSettings (dict) --
Represents the auto scaling settings for a global table or global secondary index.

MinimumUnits (integer) --
The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --
The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --
Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --
Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --
Information about the scaling policies.

(dict) --
Represents the properties of the scaling policy.

PolicyName (string) --
The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --
Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --
Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --
The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --
The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --
The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).













ReplicaProvisionedReadCapacityAutoScalingSettings (dict) --
Represents the auto scaling settings for a global table or global secondary index.

MinimumUnits (integer) --
The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --
The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --
Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --
Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --
Information about the scaling policies.

(dict) --
Represents the properties of the scaling policy.

PolicyName (string) --
The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --
Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --
Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --
The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --
The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --
The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).









ReplicaProvisionedWriteCapacityAutoScalingSettings (dict) --
Represents the auto scaling settings for a global table or global secondary index.

MinimumUnits (integer) --
The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits (integer) --
The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled (boolean) --
Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn (string) --
Role ARN used for configuring the auto scaling policy.

ScalingPolicies (list) --
Information about the scaling policies.

(dict) --
Represents the properties of the scaling policy.

PolicyName (string) --
The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration (dict) --
Represents a target tracking scaling policy configuration.

DisableScaleIn (boolean) --
Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won\'t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown (integer) --
The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application\'s availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown (integer) --
The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue (float) --
The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).









ReplicaStatus (string) --
The current state of the replica:

CREATING - The replica is being created.
UPDATING - The replica is being updated.
DELETING - The replica is being deleted.
ACTIVE - The replica is ready for use.














Exceptions

DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.ResourceInUseException
DynamoDB.Client.exceptions.LimitExceededException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'TableAutoScalingDescription': {
            'TableName': 'string',
            'TableStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
            'Replicas': [
                {
                    'RegionName': 'string',
                    'GlobalSecondaryIndexes': [
                        {
                            'IndexName': 'string',
                            'IndexStatus': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE',
                            'ProvisionedReadCapacityAutoScalingSettings': {
                                'MinimumUnits': 123,
                                'MaximumUnits': 123,
                                'AutoScalingDisabled': True|False,
                                'AutoScalingRoleArn': 'string',
                                'ScalingPolicies': [
                                    {
                                        'PolicyName': 'string',
                                        'TargetTrackingScalingPolicyConfiguration': {
                                            'DisableScaleIn': True|False,
                                            'ScaleInCooldown': 123,
                                            'ScaleOutCooldown': 123,
                                            'TargetValue': 123.0
                                        }
                                    },
                                ]
                            },
                            'ProvisionedWriteCapacityAutoScalingSettings': {
                                'MinimumUnits': 123,
                                'MaximumUnits': 123,
                                'AutoScalingDisabled': True|False,
                                'AutoScalingRoleArn': 'string',
                                'ScalingPolicies': [
                                    {
                                        'PolicyName': 'string',
                                        'TargetTrackingScalingPolicyConfiguration': {
                                            'DisableScaleIn': True|False,
                                            'ScaleInCooldown': 123,
                                            'ScaleOutCooldown': 123,
                                            'TargetValue': 123.0
                                        }
                                    },
                                ]
                            }
                        },
                    ],
                    'ReplicaProvisionedReadCapacityAutoScalingSettings': {
                        'MinimumUnits': 123,
                        'MaximumUnits': 123,
                        'AutoScalingDisabled': True|False,
                        'AutoScalingRoleArn': 'string',
                        'ScalingPolicies': [
                            {
                                'PolicyName': 'string',
                                'TargetTrackingScalingPolicyConfiguration': {
                                    'DisableScaleIn': True|False,
                                    'ScaleInCooldown': 123,
                                    'ScaleOutCooldown': 123,
                                    'TargetValue': 123.0
                                }
                            },
                        ]
                    },
                    'ReplicaProvisionedWriteCapacityAutoScalingSettings': {
                        'MinimumUnits': 123,
                        'MaximumUnits': 123,
                        'AutoScalingDisabled': True|False,
                        'AutoScalingRoleArn': 'string',
                        'ScalingPolicies': [
                            {
                                'PolicyName': 'string',
                                'TargetTrackingScalingPolicyConfiguration': {
                                    'DisableScaleIn': True|False,
                                    'ScaleInCooldown': 123,
                                    'ScaleOutCooldown': 123,
                                    'TargetValue': 123.0
                                }
                            },
                        ]
                    },
                    'ReplicaStatus': 'CREATING'|'CREATION_FAILED'|'UPDATING'|'DELETING'|'ACTIVE'
                },
            ]
        }
    }
    
    
    :returns: 
    CREATING - The table is being created.
    UPDATING - The table is being updated.
    DELETING - The table is being deleted.
    ACTIVE - The table is ready for use.
    
    """
    pass

def update_time_to_live(TableName=None, TimeToLiveSpecification=None):
    """
    The UpdateTimeToLive method enables or disables Time to Live (TTL) for the specified table. A successful UpdateTimeToLive call returns the current TimeToLiveSpecification . It can take up to one hour for the change to fully process. Any additional UpdateTimeToLive calls for the same table during this one hour duration result in a ValidationException .
    TTL compares the current time in epoch time format to the time stored in the TTL attribute of an item. If the epoch time value stored in the attribute is less than the current time, the item is marked as expired and subsequently deleted.
    DynamoDB deletes expired items on a best-effort basis to ensure availability of throughput for other data operations.
    As items are deleted, they are removed from any local secondary index and global secondary index immediately in the same eventually consistent way as a standard delete operation.
    For more information, see Time To Live in the Amazon DynamoDB Developer Guide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_time_to_live(
        TableName='string',
        TimeToLiveSpecification={
            'Enabled': True|False,
            'AttributeName': 'string'
        }
    )
    
    
    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table to be configured.\n

    :type TimeToLiveSpecification: dict
    :param TimeToLiveSpecification: [REQUIRED]\nRepresents the settings used to enable or disable Time to Live for the specified table.\n\nEnabled (boolean) -- [REQUIRED]Indicates whether TTL is to be enabled (true) or disabled (false) on the table.\n\nAttributeName (string) -- [REQUIRED]The name of the TTL attribute used to store the expiration time for items in the table.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TimeToLiveSpecification': {
        'Enabled': True|False,
        'AttributeName': 'string'
    }
}


Response Structure

(dict) --

TimeToLiveSpecification (dict) --
Represents the output of an UpdateTimeToLive operation.

Enabled (boolean) --
Indicates whether TTL is to be enabled (true) or disabled (false) on the table.

AttributeName (string) --
The name of the TTL attribute used to store the expiration time for items in the table.









Exceptions

DynamoDB.Client.exceptions.ResourceInUseException
DynamoDB.Client.exceptions.ResourceNotFoundException
DynamoDB.Client.exceptions.LimitExceededException
DynamoDB.Client.exceptions.InternalServerError


    :return: {
        'TimeToLiveSpecification': {
            'Enabled': True|False,
            'AttributeName': 'string'
        }
    }
    
    
    :returns: 
    DynamoDB.Client.exceptions.ResourceInUseException
    DynamoDB.Client.exceptions.ResourceNotFoundException
    DynamoDB.Client.exceptions.LimitExceededException
    DynamoDB.Client.exceptions.InternalServerError
    
    """
    pass

