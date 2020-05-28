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

def batch_create_partition(CatalogId=None, DatabaseName=None, TableName=None, PartitionInputList=None):
    """
    Creates one or more partitions in a batch operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_create_partition(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        PartitionInputList=[
            {
                'Values': [
                    'string',
                ],
                'LastAccessTime': datetime(2015, 1, 1),
                'StorageDescriptor': {
                    'Columns': [
                        {
                            'Name': 'string',
                            'Type': 'string',
                            'Comment': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                    ],
                    'Location': 'string',
                    'InputFormat': 'string',
                    'OutputFormat': 'string',
                    'Compressed': True|False,
                    'NumberOfBuckets': 123,
                    'SerdeInfo': {
                        'Name': 'string',
                        'SerializationLibrary': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                    'BucketColumns': [
                        'string',
                    ],
                    'SortColumns': [
                        {
                            'Column': 'string',
                            'SortOrder': 123
                        },
                    ],
                    'Parameters': {
                        'string': 'string'
                    },
                    'SkewedInfo': {
                        'SkewedColumnNames': [
                            'string',
                        ],
                        'SkewedColumnValues': [
                            'string',
                        ],
                        'SkewedColumnValueLocationMaps': {
                            'string': 'string'
                        }
                    },
                    'StoredAsSubDirectories': True|False
                },
                'Parameters': {
                    'string': 'string'
                },
                'LastAnalyzedTime': datetime(2015, 1, 1)
            },
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the catalog in which the partition is to be created. Currently, this should be the AWS account ID.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the metadata database in which the partition is to be created.\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the metadata table in which the partition is to be created.\n

    :type PartitionInputList: list
    :param PartitionInputList: [REQUIRED]\nA list of PartitionInput structures that define the partitions to be created.\n\n(dict) --The structure used to create and update a partition.\n\nValues (list) --The values of the partition. Although this parameter is not required by the SDK, you must specify this parameter for a valid input.\nThe values for the keys for the new partition must be passed as an array of String objects that must be ordered in the same order as the partition keys appearing in the Amazon S3 prefix. Otherwise AWS Glue will add the values to the wrong keys.\n\n(string) --\n\n\nLastAccessTime (datetime) --The last time at which the partition was accessed.\n\nStorageDescriptor (dict) --Provides information about the physical location where the partition is stored.\n\nColumns (list) --A list of the Columns in the table.\n\n(dict) --A column in a Table .\n\nName (string) -- [REQUIRED]The name of the Column .\n\nType (string) --The data type of the Column .\n\nComment (string) --A free-form text comment.\n\nParameters (dict) --These key-value pairs define properties associated with the column.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\nLocation (string) --The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.\n\nInputFormat (string) --The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.\n\nOutputFormat (string) --The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.\n\nCompressed (boolean) --\nTrue if the data in the table is compressed, or False if not.\n\nNumberOfBuckets (integer) --Must be specified if the table contains any dimension columns.\n\nSerdeInfo (dict) --The serialization/deserialization (SerDe) information.\n\nName (string) --Name of the SerDe.\n\nSerializationLibrary (string) --Usually the class that implements the SerDe. An example is org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .\n\nParameters (dict) --These key-value pairs define initialization parameters for the SerDe.\n\n(string) --\n(string) --\n\n\n\n\n\n\nBucketColumns (list) --A list of reducer grouping columns, clustering columns, and bucketing columns in the table.\n\n(string) --\n\n\nSortColumns (list) --A list specifying the sort order of each bucket in the table.\n\n(dict) --Specifies the sort order of a sorted column.\n\nColumn (string) -- [REQUIRED]The name of the column.\n\nSortOrder (integer) -- [REQUIRED]Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).\n\n\n\n\n\nParameters (dict) --The user-supplied properties in key-value form.\n\n(string) --\n(string) --\n\n\n\n\nSkewedInfo (dict) --The information about values that appear frequently in a column (skewed values).\n\nSkewedColumnNames (list) --A list of names of columns that contain skewed values.\n\n(string) --\n\n\nSkewedColumnValues (list) --A list of values that appear so frequently as to be considered skewed.\n\n(string) --\n\n\nSkewedColumnValueLocationMaps (dict) --A mapping of skewed values to the columns that contain them.\n\n(string) --\n(string) --\n\n\n\n\n\n\nStoredAsSubDirectories (boolean) --\nTrue if the table data is stored in subdirectories, or False if not.\n\n\n\nParameters (dict) --These key-value pairs define partition parameters.\n\n(string) --\n(string) --\n\n\n\n\nLastAnalyzedTime (datetime) --The last time at which column statistics were computed for this partition.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Errors': [
        {
            'PartitionValues': [
                'string',
            ],
            'ErrorDetail': {
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

Errors (list) --
The errors encountered when trying to create the requested partitions.

(dict) --
Contains information about a partition error.

PartitionValues (list) --
The values that define the partition.

(string) --


ErrorDetail (dict) --
The details about the partition error.

ErrorCode (string) --
The code associated with this error.

ErrorMessage (string) --
A message describing the error.













Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.GlueEncryptionException


    :return: {
        'Errors': [
            {
                'PartitionValues': [
                    'string',
                ],
                'ErrorDetail': {
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def batch_delete_connection(CatalogId=None, ConnectionNameList=None):
    """
    Deletes a list of connection definitions from the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_delete_connection(
        CatalogId='string',
        ConnectionNameList=[
            'string',
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the connections reside. If none is provided, the AWS account ID is used by default.

    :type ConnectionNameList: list
    :param ConnectionNameList: [REQUIRED]\nA list of names of the connections to delete.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Succeeded': [
        'string',
    ],
    'Errors': {
        'string': {
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        }
    }
}


Response Structure

(dict) --

Succeeded (list) --
A list of names of the connection definitions that were successfully deleted.

(string) --


Errors (dict) --
A map of the names of connections that were not successfully deleted to error details.

(string) --

(dict) --
Contains details about an error.

ErrorCode (string) --
The code associated with this error.

ErrorMessage (string) --
A message describing the error.













Exceptions

Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Succeeded': [
            'string',
        ],
        'Errors': {
            'string': {
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def batch_delete_partition(CatalogId=None, DatabaseName=None, TableName=None, PartitionsToDelete=None):
    """
    Deletes one or more partitions in a batch operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_delete_partition(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        PartitionsToDelete=[
            {
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the partition to be deleted resides. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the catalog database in which the table in question resides.\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table that contains the partitions to be deleted.\n

    :type PartitionsToDelete: list
    :param PartitionsToDelete: [REQUIRED]\nA list of PartitionInput structures that define the partitions to be deleted.\n\n(dict) --Contains a list of values defining partitions.\n\nValues (list) -- [REQUIRED]The list of values.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Errors': [
        {
            'PartitionValues': [
                'string',
            ],
            'ErrorDetail': {
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

Errors (list) --
The errors encountered when trying to delete the requested partitions.

(dict) --
Contains information about a partition error.

PartitionValues (list) --
The values that define the partition.

(string) --


ErrorDetail (dict) --
The details about the partition error.

ErrorCode (string) --
The code associated with this error.

ErrorMessage (string) --
A message describing the error.













Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Errors': [
            {
                'PartitionValues': [
                    'string',
                ],
                'ErrorDetail': {
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def batch_delete_table(CatalogId=None, DatabaseName=None, TablesToDelete=None):
    """
    Deletes multiple tables at once.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_delete_table(
        CatalogId='string',
        DatabaseName='string',
        TablesToDelete=[
            'string',
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the table resides. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the catalog database in which the tables to delete reside. For Hive compatibility, this name is entirely lowercase.\n

    :type TablesToDelete: list
    :param TablesToDelete: [REQUIRED]\nA list of the table to delete.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Errors': [
        {
            'TableName': 'string',
            'ErrorDetail': {
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

Errors (list) --
A list of errors encountered in attempting to delete the specified tables.

(dict) --
An error record for table operations.

TableName (string) --
The name of the table. For Hive compatibility, this must be entirely lowercase.

ErrorDetail (dict) --
The details about the error.

ErrorCode (string) --
The code associated with this error.

ErrorMessage (string) --
A message describing the error.













Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Errors': [
            {
                'TableName': 'string',
                'ErrorDetail': {
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def batch_delete_table_version(CatalogId=None, DatabaseName=None, TableName=None, VersionIds=None):
    """
    Deletes a specified batch of versions of a table.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_delete_table_version(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        VersionIds=[
            'string',
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the tables reside. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table. For Hive compatibility, this name is entirely lowercase.\n

    :type VersionIds: list
    :param VersionIds: [REQUIRED]\nA list of the IDs of versions to be deleted. A VersionId is a string representation of an integer. Each version is incremented by 1.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Errors': [
        {
            'TableName': 'string',
            'VersionId': 'string',
            'ErrorDetail': {
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

Errors (list) --
A list of errors encountered while trying to delete the specified table versions.

(dict) --
An error record for table-version operations.

TableName (string) --
The name of the table in question.

VersionId (string) --
The ID value of the version in question. A VersionID is a string representation of an integer. Each version is incremented by 1.

ErrorDetail (dict) --
The details about the error.

ErrorCode (string) --
The code associated with this error.

ErrorMessage (string) --
A message describing the error.













Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Errors': [
            {
                'TableName': 'string',
                'VersionId': 'string',
                'ErrorDetail': {
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def batch_get_crawlers(CrawlerNames=None):
    """
    Returns a list of resource metadata for a given list of crawler names. After calling the ListCrawlers operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that uses tags.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_crawlers(
        CrawlerNames=[
            'string',
        ]
    )
    
    
    :type CrawlerNames: list
    :param CrawlerNames: [REQUIRED]\nA list of crawler names, which might be the names returned from the ListCrawlers operation.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'Crawlers': [
        {
            'Name': 'string',
            'Role': 'string',
            'Targets': {
                'S3Targets': [
                    {
                        'Path': 'string',
                        'Exclusions': [
                            'string',
                        ]
                    },
                ],
                'JdbcTargets': [
                    {
                        'ConnectionName': 'string',
                        'Path': 'string',
                        'Exclusions': [
                            'string',
                        ]
                    },
                ],
                'DynamoDBTargets': [
                    {
                        'Path': 'string'
                    },
                ],
                'CatalogTargets': [
                    {
                        'DatabaseName': 'string',
                        'Tables': [
                            'string',
                        ]
                    },
                ]
            },
            'DatabaseName': 'string',
            'Description': 'string',
            'Classifiers': [
                'string',
            ],
            'SchemaChangePolicy': {
                'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
                'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
            },
            'State': 'READY'|'RUNNING'|'STOPPING',
            'TablePrefix': 'string',
            'Schedule': {
                'ScheduleExpression': 'string',
                'State': 'SCHEDULED'|'NOT_SCHEDULED'|'TRANSITIONING'
            },
            'CrawlElapsedTime': 123,
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdated': datetime(2015, 1, 1),
            'LastCrawl': {
                'Status': 'SUCCEEDED'|'CANCELLED'|'FAILED',
                'ErrorMessage': 'string',
                'LogGroup': 'string',
                'LogStream': 'string',
                'MessagePrefix': 'string',
                'StartTime': datetime(2015, 1, 1)
            },
            'Version': 123,
            'Configuration': 'string',
            'CrawlerSecurityConfiguration': 'string'
        },
    ],
    'CrawlersNotFound': [
        'string',
    ]
}


Response Structure

(dict) --
Crawlers (list) --A list of crawler definitions.

(dict) --Specifies a crawler program that examines a data source and uses classifiers to try to determine its schema. If successful, the crawler records metadata concerning the data source in the AWS Glue Data Catalog.

Name (string) --The name of the crawler.

Role (string) --The Amazon Resource Name (ARN) of an IAM role that\'s used to access customer resources, such as Amazon Simple Storage Service (Amazon S3) data.

Targets (dict) --A collection of targets to crawl.

S3Targets (list) --Specifies Amazon Simple Storage Service (Amazon S3) targets.

(dict) --Specifies a data store in Amazon Simple Storage Service (Amazon S3).

Path (string) --The path to the Amazon S3 target.

Exclusions (list) --A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler .

(string) --






JdbcTargets (list) --Specifies JDBC targets.

(dict) --Specifies a JDBC data store to crawl.

ConnectionName (string) --The name of the connection to use to connect to the JDBC target.

Path (string) --The path of the JDBC target.

Exclusions (list) --A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler .

(string) --






DynamoDBTargets (list) --Specifies Amazon DynamoDB targets.

(dict) --Specifies an Amazon DynamoDB table to crawl.

Path (string) --The name of the DynamoDB table to crawl.





CatalogTargets (list) --Specifies AWS Glue Data Catalog targets.

(dict) --Specifies an AWS Glue Data Catalog target.

DatabaseName (string) --The name of the database to be synchronized.

Tables (list) --A list of the tables to be synchronized.

(string) --








DatabaseName (string) --The name of the database in which the crawler\'s output is stored.

Description (string) --A description of the crawler.

Classifiers (list) --A list of UTF-8 strings that specify the custom classifiers that are associated with the crawler.

(string) --


SchemaChangePolicy (dict) --The policy that specifies update and delete behaviors for the crawler.

UpdateBehavior (string) --The update behavior when the crawler finds a changed schema.

DeleteBehavior (string) --The deletion behavior when the crawler finds a deleted object.



State (string) --Indicates whether the crawler is running, or whether a run is pending.

TablePrefix (string) --The prefix added to the names of tables that are created.

Schedule (dict) --For scheduled crawlers, the schedule when the crawler runs.

ScheduleExpression (string) --A cron expression used to specify the schedule. For more information, see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, specify cron(15 12 * * ? *) .

State (string) --The state of the schedule.



CrawlElapsedTime (integer) --If the crawler is running, contains the total time elapsed since the last crawl began.

CreationTime (datetime) --The time that the crawler was created.

LastUpdated (datetime) --The time that the crawler was last updated.

LastCrawl (dict) --The status of the last crawl, and potentially error information if an error occurred.

Status (string) --Status of the last crawl.

ErrorMessage (string) --If an error occurred, the error information about the last crawl.

LogGroup (string) --The log group for the last crawl.

LogStream (string) --The log stream for the last crawl.

MessagePrefix (string) --The prefix for a message about this crawl.

StartTime (datetime) --The time at which the crawl started.



Version (integer) --The version of the crawler.

Configuration (string) --Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler\'s behavior. For more information, see Configuring a Crawler .

CrawlerSecurityConfiguration (string) --The name of the SecurityConfiguration structure to be used by this crawler.





CrawlersNotFound (list) --A list of names of crawlers that were not found.

(string) --







Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Crawlers': [
            {
                'Name': 'string',
                'Role': 'string',
                'Targets': {
                    'S3Targets': [
                        {
                            'Path': 'string',
                            'Exclusions': [
                                'string',
                            ]
                        },
                    ],
                    'JdbcTargets': [
                        {
                            'ConnectionName': 'string',
                            'Path': 'string',
                            'Exclusions': [
                                'string',
                            ]
                        },
                    ],
                    'DynamoDBTargets': [
                        {
                            'Path': 'string'
                        },
                    ],
                    'CatalogTargets': [
                        {
                            'DatabaseName': 'string',
                            'Tables': [
                                'string',
                            ]
                        },
                    ]
                },
                'DatabaseName': 'string',
                'Description': 'string',
                'Classifiers': [
                    'string',
                ],
                'SchemaChangePolicy': {
                    'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
                    'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
                },
                'State': 'READY'|'RUNNING'|'STOPPING',
                'TablePrefix': 'string',
                'Schedule': {
                    'ScheduleExpression': 'string',
                    'State': 'SCHEDULED'|'NOT_SCHEDULED'|'TRANSITIONING'
                },
                'CrawlElapsedTime': 123,
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdated': datetime(2015, 1, 1),
                'LastCrawl': {
                    'Status': 'SUCCEEDED'|'CANCELLED'|'FAILED',
                    'ErrorMessage': 'string',
                    'LogGroup': 'string',
                    'LogStream': 'string',
                    'MessagePrefix': 'string',
                    'StartTime': datetime(2015, 1, 1)
                },
                'Version': 123,
                'Configuration': 'string',
                'CrawlerSecurityConfiguration': 'string'
            },
        ],
        'CrawlersNotFound': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def batch_get_dev_endpoints(DevEndpointNames=None):
    """
    Returns a list of resource metadata for a given list of development endpoint names. After calling the ListDevEndpoints operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that uses tags.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_dev_endpoints(
        DevEndpointNames=[
            'string',
        ]
    )
    
    
    :type DevEndpointNames: list
    :param DevEndpointNames: [REQUIRED]\nThe list of DevEndpoint names, which might be the names returned from the ListDevEndpoint operation.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'DevEndpoints': [
        {
            'EndpointName': 'string',
            'RoleArn': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'SubnetId': 'string',
            'YarnEndpointAddress': 'string',
            'PrivateAddress': 'string',
            'ZeppelinRemoteSparkInterpreterPort': 123,
            'PublicAddress': 'string',
            'Status': 'string',
            'WorkerType': 'Standard'|'G.1X'|'G.2X',
            'GlueVersion': 'string',
            'NumberOfWorkers': 123,
            'NumberOfNodes': 123,
            'AvailabilityZone': 'string',
            'VpcId': 'string',
            'ExtraPythonLibsS3Path': 'string',
            'ExtraJarsS3Path': 'string',
            'FailureReason': 'string',
            'LastUpdateStatus': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'LastModifiedTimestamp': datetime(2015, 1, 1),
            'PublicKey': 'string',
            'PublicKeys': [
                'string',
            ],
            'SecurityConfiguration': 'string',
            'Arguments': {
                'string': 'string'
            }
        },
    ],
    'DevEndpointsNotFound': [
        'string',
    ]
}


Response Structure

(dict) --
DevEndpoints (list) --A list of DevEndpoint definitions.

(dict) --A development endpoint where a developer can remotely debug extract, transform, and load (ETL) scripts.

EndpointName (string) --The name of the DevEndpoint .

RoleArn (string) --The Amazon Resource Name (ARN) of the IAM role used in this DevEndpoint .

SecurityGroupIds (list) --A list of security group identifiers used in this DevEndpoint .

(string) --


SubnetId (string) --The subnet ID for this DevEndpoint .

YarnEndpointAddress (string) --The YARN endpoint address used by this DevEndpoint .

PrivateAddress (string) --A private IP address to access the DevEndpoint within a VPC if the DevEndpoint is created within one. The PrivateAddress field is present only when you create the DevEndpoint within your VPC.

ZeppelinRemoteSparkInterpreterPort (integer) --The Apache Zeppelin port for the remote Apache Spark interpreter.

PublicAddress (string) --The public IP address used by this DevEndpoint . The PublicAddress field is present only when you create a non-virtual private cloud (VPC) DevEndpoint .

Status (string) --The current status of this DevEndpoint .

WorkerType (string) --The type of predefined worker that is allocated to the development endpoint. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.
For the G.2X worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.

Known issue: when a development endpoint is created with the G.2X WorkerType configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB of memory, and a 64 GB disk.

GlueVersion (string) --Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.
Development endpoints that are created without specifying a Glue version default to Glue 0.9.
You can specify a version of Python support for development endpoints by using the Arguments parameter in the CreateDevEndpoint or UpdateDevEndpoint APIs. If no arguments are provided, the version defaults to Python 2.

NumberOfWorkers (integer) --The number of workers of a defined workerType that are allocated to the development endpoint.
The maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .

NumberOfNodes (integer) --The number of AWS Glue Data Processing Units (DPUs) allocated to this DevEndpoint .

AvailabilityZone (string) --The AWS Availability Zone where this DevEndpoint is located.

VpcId (string) --The ID of the virtual private cloud (VPC) used by this DevEndpoint .

ExtraPythonLibsS3Path (string) --The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your DevEndpoint . Multiple values must be complete paths separated by a comma.

Note
You can only use pure Python libraries with a DevEndpoint . Libraries that rely on C extensions, such as the pandas Python data analysis library, are not currently supported.


ExtraJarsS3Path (string) --The path to one or more Java .jar files in an S3 bucket that should be loaded in your DevEndpoint .

Note
You can only use pure Java/Scala libraries with a DevEndpoint .


FailureReason (string) --The reason for a current failure in this DevEndpoint .

LastUpdateStatus (string) --The status of the last update.

CreatedTimestamp (datetime) --The point in time at which this DevEndpoint was created.

LastModifiedTimestamp (datetime) --The point in time at which this DevEndpoint was last modified.

PublicKey (string) --The public key to be used by this DevEndpoint for authentication. This attribute is provided for backward compatibility because the recommended attribute to use is public keys.

PublicKeys (list) --A list of public keys to be used by the DevEndpoints for authentication. Using this attribute is preferred over a single public key because the public keys allow you to have a different private key per client.

Note
If you previously created an endpoint with a public key, you must remove that key to be able to set a list of public keys. Call the UpdateDevEndpoint API operation with the public key content in the deletePublicKeys attribute, and the list of new keys in the addPublicKeys attribute.


(string) --


SecurityConfiguration (string) --The name of the SecurityConfiguration structure to be used with this DevEndpoint .

Arguments (dict) --A map of arguments used to configure the DevEndpoint .
Valid arguments are:

"--enable-glue-datacatalog": ""
"GLUE_PYTHON_VERSION": "3"
"GLUE_PYTHON_VERSION": "2"

You can specify a version of Python support for development endpoints by using the Arguments parameter in the CreateDevEndpoint or UpdateDevEndpoint APIs. If no arguments are provided, the version defaults to Python 2.

(string) --
(string) --








DevEndpointsNotFound (list) --A list of DevEndpoints not found.

(string) --







Exceptions

Glue.Client.exceptions.AccessDeniedException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException


    :return: {
        'DevEndpoints': [
            {
                'EndpointName': 'string',
                'RoleArn': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'SubnetId': 'string',
                'YarnEndpointAddress': 'string',
                'PrivateAddress': 'string',
                'ZeppelinRemoteSparkInterpreterPort': 123,
                'PublicAddress': 'string',
                'Status': 'string',
                'WorkerType': 'Standard'|'G.1X'|'G.2X',
                'GlueVersion': 'string',
                'NumberOfWorkers': 123,
                'NumberOfNodes': 123,
                'AvailabilityZone': 'string',
                'VpcId': 'string',
                'ExtraPythonLibsS3Path': 'string',
                'ExtraJarsS3Path': 'string',
                'FailureReason': 'string',
                'LastUpdateStatus': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'LastModifiedTimestamp': datetime(2015, 1, 1),
                'PublicKey': 'string',
                'PublicKeys': [
                    'string',
                ],
                'SecurityConfiguration': 'string',
                'Arguments': {
                    'string': 'string'
                }
            },
        ],
        'DevEndpointsNotFound': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def batch_get_jobs(JobNames=None):
    """
    Returns a list of resource metadata for a given list of job names. After calling the ListJobs operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that uses tags.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_jobs(
        JobNames=[
            'string',
        ]
    )
    
    
    :type JobNames: list
    :param JobNames: [REQUIRED]\nA list of job names, which might be the names returned from the ListJobs operation.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'Jobs': [
        {
            'Name': 'string',
            'Description': 'string',
            'LogUri': 'string',
            'Role': 'string',
            'CreatedOn': datetime(2015, 1, 1),
            'LastModifiedOn': datetime(2015, 1, 1),
            'ExecutionProperty': {
                'MaxConcurrentRuns': 123
            },
            'Command': {
                'Name': 'string',
                'ScriptLocation': 'string',
                'PythonVersion': 'string'
            },
            'DefaultArguments': {
                'string': 'string'
            },
            'NonOverridableArguments': {
                'string': 'string'
            },
            'Connections': {
                'Connections': [
                    'string',
                ]
            },
            'MaxRetries': 123,
            'AllocatedCapacity': 123,
            'Timeout': 123,
            'MaxCapacity': 123.0,
            'WorkerType': 'Standard'|'G.1X'|'G.2X',
            'NumberOfWorkers': 123,
            'SecurityConfiguration': 'string',
            'NotificationProperty': {
                'NotifyDelayAfter': 123
            },
            'GlueVersion': 'string'
        },
    ],
    'JobsNotFound': [
        'string',
    ]
}


Response Structure

(dict) --
Jobs (list) --A list of job definitions.

(dict) --Specifies a job definition.

Name (string) --The name you assign to this job definition.

Description (string) --A description of the job.

LogUri (string) --This field is reserved for future use.

Role (string) --The name or Amazon Resource Name (ARN) of the IAM role associated with this job.

CreatedOn (datetime) --The time and date that this job definition was created.

LastModifiedOn (datetime) --The last point in time when this job definition was modified.

ExecutionProperty (dict) --An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job.

MaxConcurrentRuns (integer) --The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.



Command (dict) --The JobCommand that executes this job.

Name (string) --The name of the job command. For an Apache Spark ETL job, this must be glueetl . For a Python shell job, it must be pythonshell .

ScriptLocation (string) --Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that executes a job.

PythonVersion (string) --The Python version being used to execute a Python shell job. Allowed values are 2 or 3.



DefaultArguments (dict) --The default arguments for this job, specified as name-value pairs.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




NonOverridableArguments (dict) --Non-overridable arguments for this job, specified as name-value pairs.

(string) --
(string) --




Connections (dict) --The connections used for this job.

Connections (list) --A list of connections used by the job.

(string) --




MaxRetries (integer) --The maximum number of times to retry this job after a JobRun fails.

AllocatedCapacity (integer) --This field is deprecated. Use MaxCapacity instead.
The number of AWS Glue data processing units (DPUs) allocated to runs of this job. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .

Timeout (integer) --The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours).

MaxCapacity (float) --The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .
Do not set Max Capacity if using WorkerType and NumberOfWorkers .
The value that can be allocated for MaxCapacity depends on whether you are running a Python shell job or an Apache Spark ETL job:

When you specify a Python shell job (JobCommand.Name ="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
When you specify an Apache Spark ETL job (JobCommand.Name ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.


WorkerType (string) --The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.
For the G.2X worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.


NumberOfWorkers (integer) --The number of workers of a defined workerType that are allocated when a job runs.
The maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .

SecurityConfiguration (string) --The name of the SecurityConfiguration structure to be used with this job.

NotificationProperty (dict) --Specifies configuration properties of a job notification.

NotifyDelayAfter (integer) --After a job run starts, the number of minutes to wait before sending a job run delay notification.



GlueVersion (string) --Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.
Jobs that are created without specifying a Glue version default to Glue 0.9.





JobsNotFound (list) --A list of names of jobs not found.

(string) --







Exceptions

Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException


    :return: {
        'Jobs': [
            {
                'Name': 'string',
                'Description': 'string',
                'LogUri': 'string',
                'Role': 'string',
                'CreatedOn': datetime(2015, 1, 1),
                'LastModifiedOn': datetime(2015, 1, 1),
                'ExecutionProperty': {
                    'MaxConcurrentRuns': 123
                },
                'Command': {
                    'Name': 'string',
                    'ScriptLocation': 'string',
                    'PythonVersion': 'string'
                },
                'DefaultArguments': {
                    'string': 'string'
                },
                'NonOverridableArguments': {
                    'string': 'string'
                },
                'Connections': {
                    'Connections': [
                        'string',
                    ]
                },
                'MaxRetries': 123,
                'AllocatedCapacity': 123,
                'Timeout': 123,
                'MaxCapacity': 123.0,
                'WorkerType': 'Standard'|'G.1X'|'G.2X',
                'NumberOfWorkers': 123,
                'SecurityConfiguration': 'string',
                'NotificationProperty': {
                    'NotifyDelayAfter': 123
                },
                'GlueVersion': 'string'
            },
        ],
        'JobsNotFound': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def batch_get_partition(CatalogId=None, DatabaseName=None, TableName=None, PartitionsToGet=None):
    """
    Retrieves partitions in a batch request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_partition(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        PartitionsToGet=[
            {
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the partitions in question reside. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the catalog database where the partitions reside.\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the partitions\' table.\n

    :type PartitionsToGet: list
    :param PartitionsToGet: [REQUIRED]\nA list of partition values identifying the partitions to retrieve.\n\n(dict) --Contains a list of values defining partitions.\n\nValues (list) -- [REQUIRED]The list of values.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Partitions': [
        {
            'Values': [
                'string',
            ],
            'DatabaseName': 'string',
            'TableName': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'LastAccessTime': datetime(2015, 1, 1),
            'StorageDescriptor': {
                'Columns': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'Location': 'string',
                'InputFormat': 'string',
                'OutputFormat': 'string',
                'Compressed': True|False,
                'NumberOfBuckets': 123,
                'SerdeInfo': {
                    'Name': 'string',
                    'SerializationLibrary': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
                'BucketColumns': [
                    'string',
                ],
                'SortColumns': [
                    {
                        'Column': 'string',
                        'SortOrder': 123
                    },
                ],
                'Parameters': {
                    'string': 'string'
                },
                'SkewedInfo': {
                    'SkewedColumnNames': [
                        'string',
                    ],
                    'SkewedColumnValues': [
                        'string',
                    ],
                    'SkewedColumnValueLocationMaps': {
                        'string': 'string'
                    }
                },
                'StoredAsSubDirectories': True|False
            },
            'Parameters': {
                'string': 'string'
            },
            'LastAnalyzedTime': datetime(2015, 1, 1)
        },
    ],
    'UnprocessedKeys': [
        {
            'Values': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --

Partitions (list) --
A list of the requested partitions.

(dict) --
Represents a slice of table data.

Values (list) --
The values of the partition.

(string) --


DatabaseName (string) --
The name of the catalog database in which to create the partition.

TableName (string) --
The name of the database table in which to create the partition.

CreationTime (datetime) --
The time at which the partition was created.

LastAccessTime (datetime) --
The last time at which the partition was accessed.

StorageDescriptor (dict) --
Provides information about the physical location where the partition is stored.

Columns (list) --
A list of the Columns in the table.

(dict) --
A column in a Table .

Name (string) --
The name of the Column .

Type (string) --
The data type of the Column .

Comment (string) --
A free-form text comment.

Parameters (dict) --
These key-value pairs define properties associated with the column.

(string) --
(string) --








Location (string) --
The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

InputFormat (string) --
The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.

OutputFormat (string) --
The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.

Compressed (boolean) --

True if the data in the table is compressed, or False if not.


NumberOfBuckets (integer) --
Must be specified if the table contains any dimension columns.

SerdeInfo (dict) --
The serialization/deserialization (SerDe) information.

Name (string) --
Name of the SerDe.

SerializationLibrary (string) --
Usually the class that implements the SerDe. An example is org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .

Parameters (dict) --
These key-value pairs define initialization parameters for the SerDe.

(string) --
(string) --






BucketColumns (list) --
A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

(string) --


SortColumns (list) --
A list specifying the sort order of each bucket in the table.

(dict) --
Specifies the sort order of a sorted column.

Column (string) --
The name of the column.

SortOrder (integer) --
Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).





Parameters (dict) --
The user-supplied properties in key-value form.

(string) --
(string) --




SkewedInfo (dict) --
The information about values that appear frequently in a column (skewed values).

SkewedColumnNames (list) --
A list of names of columns that contain skewed values.

(string) --


SkewedColumnValues (list) --
A list of values that appear so frequently as to be considered skewed.

(string) --


SkewedColumnValueLocationMaps (dict) --
A mapping of skewed values to the columns that contain them.

(string) --
(string) --






StoredAsSubDirectories (boolean) --

True if the table data is stored in subdirectories, or False if not.




Parameters (dict) --
These key-value pairs define partition parameters.

(string) --
(string) --




LastAnalyzedTime (datetime) --
The last time at which column statistics were computed for this partition.





UnprocessedKeys (list) --
A list of the partition values in the request for which partitions were not returned.

(dict) --
Contains a list of values defining partitions.

Values (list) --
The list of values.

(string) --












Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.GlueEncryptionException


    :return: {
        'Partitions': [
            {
                'Values': [
                    'string',
                ],
                'DatabaseName': 'string',
                'TableName': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastAccessTime': datetime(2015, 1, 1),
                'StorageDescriptor': {
                    'Columns': [
                        {
                            'Name': 'string',
                            'Type': 'string',
                            'Comment': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                    ],
                    'Location': 'string',
                    'InputFormat': 'string',
                    'OutputFormat': 'string',
                    'Compressed': True|False,
                    'NumberOfBuckets': 123,
                    'SerdeInfo': {
                        'Name': 'string',
                        'SerializationLibrary': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                    'BucketColumns': [
                        'string',
                    ],
                    'SortColumns': [
                        {
                            'Column': 'string',
                            'SortOrder': 123
                        },
                    ],
                    'Parameters': {
                        'string': 'string'
                    },
                    'SkewedInfo': {
                        'SkewedColumnNames': [
                            'string',
                        ],
                        'SkewedColumnValues': [
                            'string',
                        ],
                        'SkewedColumnValueLocationMaps': {
                            'string': 'string'
                        }
                    },
                    'StoredAsSubDirectories': True|False
                },
                'Parameters': {
                    'string': 'string'
                },
                'LastAnalyzedTime': datetime(2015, 1, 1)
            },
        ],
        'UnprocessedKeys': [
            {
                'Values': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def batch_get_triggers(TriggerNames=None):
    """
    Returns a list of resource metadata for a given list of trigger names. After calling the ListTriggers operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that uses tags.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_triggers(
        TriggerNames=[
            'string',
        ]
    )
    
    
    :type TriggerNames: list
    :param TriggerNames: [REQUIRED]\nA list of trigger names, which may be the names returned from the ListTriggers operation.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'Triggers': [
        {
            'Name': 'string',
            'WorkflowName': 'string',
            'Id': 'string',
            'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
            'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
            'Description': 'string',
            'Schedule': 'string',
            'Actions': [
                {
                    'JobName': 'string',
                    'Arguments': {
                        'string': 'string'
                    },
                    'Timeout': 123,
                    'SecurityConfiguration': 'string',
                    'NotificationProperty': {
                        'NotifyDelayAfter': 123
                    },
                    'CrawlerName': 'string'
                },
            ],
            'Predicate': {
                'Logical': 'AND'|'ANY',
                'Conditions': [
                    {
                        'LogicalOperator': 'EQUALS',
                        'JobName': 'string',
                        'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                        'CrawlerName': 'string',
                        'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                    },
                ]
            }
        },
    ],
    'TriggersNotFound': [
        'string',
    ]
}


Response Structure

(dict) --
Triggers (list) --A list of trigger definitions.

(dict) --Information about a specific trigger.

Name (string) --The name of the trigger.

WorkflowName (string) --The name of the workflow associated with the trigger.

Id (string) --Reserved for future use.

Type (string) --The type of trigger that this is.

State (string) --The current state of the trigger.

Description (string) --A description of this trigger.

Schedule (string) --A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .

Actions (list) --The actions initiated by this trigger.

(dict) --Defines an action to be initiated by a trigger.

JobName (string) --The name of a job to be executed.

Arguments (dict) --The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




Timeout (integer) --The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

SecurityConfiguration (string) --The name of the SecurityConfiguration structure to be used with this action.

NotificationProperty (dict) --Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --After a job run starts, the number of minutes to wait before sending a job run delay notification.



CrawlerName (string) --The name of the crawler to be used with this action.





Predicate (dict) --The predicate of this trigger, which defines when it will fire.

Logical (string) --An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.

Conditions (list) --A list of the conditions that determine when the trigger will fire.

(dict) --Defines a condition under which a trigger fires.

LogicalOperator (string) --A logical operator.

JobName (string) --The name of the job whose JobRuns this condition applies to, and on which this trigger waits.

State (string) --The condition state. Currently, the only job states that a trigger can listen for are SUCCEEDED , STOPPED , FAILED , and TIMEOUT . The only crawler states that a trigger can listen for are SUCCEEDED , FAILED , and CANCELLED .

CrawlerName (string) --The name of the crawler to which this condition applies.

CrawlState (string) --The state of the crawler to which this condition applies.











TriggersNotFound (list) --A list of names of triggers not found.

(string) --







Exceptions

Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException


    :return: {
        'Triggers': [
            {
                'Name': 'string',
                'WorkflowName': 'string',
                'Id': 'string',
                'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                'Description': 'string',
                'Schedule': 'string',
                'Actions': [
                    {
                        'JobName': 'string',
                        'Arguments': {
                            'string': 'string'
                        },
                        'Timeout': 123,
                        'SecurityConfiguration': 'string',
                        'NotificationProperty': {
                            'NotifyDelayAfter': 123
                        },
                        'CrawlerName': 'string'
                    },
                ],
                'Predicate': {
                    'Logical': 'AND'|'ANY',
                    'Conditions': [
                        {
                            'LogicalOperator': 'EQUALS',
                            'JobName': 'string',
                            'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                            'CrawlerName': 'string',
                            'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                        },
                    ]
                }
            },
        ],
        'TriggersNotFound': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def batch_get_workflows(Names=None, IncludeGraph=None):
    """
    Returns a list of resource metadata for a given list of workflow names. After calling the ListWorkflows operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that uses tags.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_workflows(
        Names=[
            'string',
        ],
        IncludeGraph=True|False
    )
    
    
    :type Names: list
    :param Names: [REQUIRED]\nA list of workflow names, which may be the names returned from the ListWorkflows operation.\n\n(string) --\n\n

    :type IncludeGraph: boolean
    :param IncludeGraph: Specifies whether to include a graph when returning the workflow resource metadata.

    :rtype: dict

ReturnsResponse Syntax
{
    'Workflows': [
        {
            'Name': 'string',
            'Description': 'string',
            'DefaultRunProperties': {
                'string': 'string'
            },
            'CreatedOn': datetime(2015, 1, 1),
            'LastModifiedOn': datetime(2015, 1, 1),
            'LastRun': {
                'Name': 'string',
                'WorkflowRunId': 'string',
                'WorkflowRunProperties': {
                    'string': 'string'
                },
                'StartedOn': datetime(2015, 1, 1),
                'CompletedOn': datetime(2015, 1, 1),
                'Status': 'RUNNING'|'COMPLETED'|'STOPPING'|'STOPPED',
                'Statistics': {
                    'TotalActions': 123,
                    'TimeoutActions': 123,
                    'FailedActions': 123,
                    'StoppedActions': 123,
                    'SucceededActions': 123,
                    'RunningActions': 123
                },
                'Graph': {
                    'Nodes': [
                        {
                            'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                            'Name': 'string',
                            'UniqueId': 'string',
                            'TriggerDetails': {
                                'Trigger': {
                                    'Name': 'string',
                                    'WorkflowName': 'string',
                                    'Id': 'string',
                                    'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                    'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                                    'Description': 'string',
                                    'Schedule': 'string',
                                    'Actions': [
                                        {
                                            'JobName': 'string',
                                            'Arguments': {
                                                'string': 'string'
                                            },
                                            'Timeout': 123,
                                            'SecurityConfiguration': 'string',
                                            'NotificationProperty': {
                                                'NotifyDelayAfter': 123
                                            },
                                            'CrawlerName': 'string'
                                        },
                                    ],
                                    'Predicate': {
                                        'Logical': 'AND'|'ANY',
                                        'Conditions': [
                                            {
                                                'LogicalOperator': 'EQUALS',
                                                'JobName': 'string',
                                                'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                                'CrawlerName': 'string',
                                                'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                                            },
                                        ]
                                    }
                                }
                            },
                            'JobDetails': {
                                'JobRuns': [
                                    {
                                        'Id': 'string',
                                        'Attempt': 123,
                                        'PreviousRunId': 'string',
                                        'TriggerName': 'string',
                                        'JobName': 'string',
                                        'StartedOn': datetime(2015, 1, 1),
                                        'LastModifiedOn': datetime(2015, 1, 1),
                                        'CompletedOn': datetime(2015, 1, 1),
                                        'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                        'Arguments': {
                                            'string': 'string'
                                        },
                                        'ErrorMessage': 'string',
                                        'PredecessorRuns': [
                                            {
                                                'JobName': 'string',
                                                'RunId': 'string'
                                            },
                                        ],
                                        'AllocatedCapacity': 123,
                                        'ExecutionTime': 123,
                                        'Timeout': 123,
                                        'MaxCapacity': 123.0,
                                        'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                        'NumberOfWorkers': 123,
                                        'SecurityConfiguration': 'string',
                                        'LogGroupName': 'string',
                                        'NotificationProperty': {
                                            'NotifyDelayAfter': 123
                                        },
                                        'GlueVersion': 'string'
                                    },
                                ]
                            },
                            'CrawlerDetails': {
                                'Crawls': [
                                    {
                                        'State': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED',
                                        'StartedOn': datetime(2015, 1, 1),
                                        'CompletedOn': datetime(2015, 1, 1),
                                        'ErrorMessage': 'string',
                                        'LogGroup': 'string',
                                        'LogStream': 'string'
                                    },
                                ]
                            }
                        },
                    ],
                    'Edges': [
                        {
                            'SourceId': 'string',
                            'DestinationId': 'string'
                        },
                    ]
                }
            },
            'Graph': {
                'Nodes': [
                    {
                        'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                        'Name': 'string',
                        'UniqueId': 'string',
                        'TriggerDetails': {
                            'Trigger': {
                                'Name': 'string',
                                'WorkflowName': 'string',
                                'Id': 'string',
                                'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                                'Description': 'string',
                                'Schedule': 'string',
                                'Actions': [
                                    {
                                        'JobName': 'string',
                                        'Arguments': {
                                            'string': 'string'
                                        },
                                        'Timeout': 123,
                                        'SecurityConfiguration': 'string',
                                        'NotificationProperty': {
                                            'NotifyDelayAfter': 123
                                        },
                                        'CrawlerName': 'string'
                                    },
                                ],
                                'Predicate': {
                                    'Logical': 'AND'|'ANY',
                                    'Conditions': [
                                        {
                                            'LogicalOperator': 'EQUALS',
                                            'JobName': 'string',
                                            'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                            'CrawlerName': 'string',
                                            'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                                        },
                                    ]
                                }
                            }
                        },
                        'JobDetails': {
                            'JobRuns': [
                                {
                                    'Id': 'string',
                                    'Attempt': 123,
                                    'PreviousRunId': 'string',
                                    'TriggerName': 'string',
                                    'JobName': 'string',
                                    'StartedOn': datetime(2015, 1, 1),
                                    'LastModifiedOn': datetime(2015, 1, 1),
                                    'CompletedOn': datetime(2015, 1, 1),
                                    'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                    'Arguments': {
                                        'string': 'string'
                                    },
                                    'ErrorMessage': 'string',
                                    'PredecessorRuns': [
                                        {
                                            'JobName': 'string',
                                            'RunId': 'string'
                                        },
                                    ],
                                    'AllocatedCapacity': 123,
                                    'ExecutionTime': 123,
                                    'Timeout': 123,
                                    'MaxCapacity': 123.0,
                                    'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                    'NumberOfWorkers': 123,
                                    'SecurityConfiguration': 'string',
                                    'LogGroupName': 'string',
                                    'NotificationProperty': {
                                        'NotifyDelayAfter': 123
                                    },
                                    'GlueVersion': 'string'
                                },
                            ]
                        },
                        'CrawlerDetails': {
                            'Crawls': [
                                {
                                    'State': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED',
                                    'StartedOn': datetime(2015, 1, 1),
                                    'CompletedOn': datetime(2015, 1, 1),
                                    'ErrorMessage': 'string',
                                    'LogGroup': 'string',
                                    'LogStream': 'string'
                                },
                            ]
                        }
                    },
                ],
                'Edges': [
                    {
                        'SourceId': 'string',
                        'DestinationId': 'string'
                    },
                ]
            }
        },
    ],
    'MissingWorkflows': [
        'string',
    ]
}


Response Structure

(dict) --

Workflows (list) --
A list of workflow resource metadata.

(dict) --
A workflow represents a flow in which AWS Glue components should be executed to complete a logical task.

Name (string) --
The name of the workflow representing the flow.

Description (string) --
A description of the workflow.

DefaultRunProperties (dict) --
A collection of properties to be used as part of each execution of the workflow.

(string) --
(string) --




CreatedOn (datetime) --
The date and time when the workflow was created.

LastModifiedOn (datetime) --
The date and time when the workflow was last modified.

LastRun (dict) --
The information about the last execution of the workflow.

Name (string) --
Name of the workflow which was executed.

WorkflowRunId (string) --
The ID of this workflow run.

WorkflowRunProperties (dict) --
The workflow run properties which were set during the run.

(string) --
(string) --




StartedOn (datetime) --
The date and time when the workflow run was started.

CompletedOn (datetime) --
The date and time when the workflow run completed.

Status (string) --
The status of the workflow run.

Statistics (dict) --
The statistics of the run.

TotalActions (integer) --
Total number of Actions in the workflow run.

TimeoutActions (integer) --
Total number of Actions which timed out.

FailedActions (integer) --
Total number of Actions which have failed.

StoppedActions (integer) --
Total number of Actions which have stopped.

SucceededActions (integer) --
Total number of Actions which have succeeded.

RunningActions (integer) --
Total number Actions in running state.



Graph (dict) --
The graph representing all the AWS Glue components that belong to the workflow as nodes and directed connections between them as edges.

Nodes (list) --
A list of the the AWS Glue components belong to the workflow represented as nodes.

(dict) --
A node represents an AWS Glue component like Trigger, Job etc. which is part of a workflow.

Type (string) --
The type of AWS Glue component represented by the node.

Name (string) --
The name of the AWS Glue component represented by the node.

UniqueId (string) --
The unique Id assigned to the node within the workflow.

TriggerDetails (dict) --
Details of the Trigger when the node represents a Trigger.

Trigger (dict) --
The information of the trigger represented by the trigger node.

Name (string) --
The name of the trigger.

WorkflowName (string) --
The name of the workflow associated with the trigger.

Id (string) --
Reserved for future use.

Type (string) --
The type of trigger that this is.

State (string) --
The current state of the trigger.

Description (string) --
A description of this trigger.

Schedule (string) --
A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .

Actions (list) --
The actions initiated by this trigger.

(dict) --
Defines an action to be initiated by a trigger.

JobName (string) --
The name of a job to be executed.

Arguments (dict) --
The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this action.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



CrawlerName (string) --
The name of the crawler to be used with this action.





Predicate (dict) --
The predicate of this trigger, which defines when it will fire.

Logical (string) --
An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.

Conditions (list) --
A list of the conditions that determine when the trigger will fire.

(dict) --
Defines a condition under which a trigger fires.

LogicalOperator (string) --
A logical operator.

JobName (string) --
The name of the job whose JobRuns this condition applies to, and on which this trigger waits.

State (string) --
The condition state. Currently, the only job states that a trigger can listen for are SUCCEEDED , STOPPED , FAILED , and TIMEOUT . The only crawler states that a trigger can listen for are SUCCEEDED , FAILED , and CANCELLED .

CrawlerName (string) --
The name of the crawler to which this condition applies.

CrawlState (string) --
The state of the crawler to which this condition applies.











JobDetails (dict) --
Details of the Job when the node represents a Job.

JobRuns (list) --
The information for the job runs represented by the job node.

(dict) --
Contains information about a job run.

Id (string) --
The ID of this job run.

Attempt (integer) --
The number of the attempt to run this job.

PreviousRunId (string) --
The ID of the previous run of this job. For example, the JobRunId specified in the StartJobRun action.

TriggerName (string) --
The name of the trigger that started this job run.

JobName (string) --
The name of the job definition being used in this run.

StartedOn (datetime) --
The date and time at which this job run was started.

LastModifiedOn (datetime) --
The last time that this job run was modified.

CompletedOn (datetime) --
The date and time that this job run completed.

JobRunState (string) --
The current state of the job run. For more information about the statuses of jobs that have terminated abnormally, see AWS Glue Job Run Statuses .

Arguments (dict) --
The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




ErrorMessage (string) --
An error message associated with this job run.

PredecessorRuns (list) --
A list of predecessors to this job run.

(dict) --
A job run that was used in the predicate of a conditional trigger that triggered this job run.

JobName (string) --
The name of the job definition used by the predecessor job run.

RunId (string) --
The job-run ID of the predecessor job run.





AllocatedCapacity (integer) --
This field is deprecated. Use MaxCapacity instead.
The number of AWS Glue data processing units (DPUs) allocated to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .

ExecutionTime (integer) --
The amount of time (in seconds) that the job run consumed resources.

Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

MaxCapacity (float) --
The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .
Do not set Max Capacity if using WorkerType and NumberOfWorkers .
The value that can be allocated for MaxCapacity depends on whether you are running a Python shell job or an Apache Spark ETL job:

When you specify a Python shell job (JobCommand.Name ="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
When you specify an Apache Spark ETL job (JobCommand.Name ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.


WorkerType (string) --
The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
For the G.2X worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.


NumberOfWorkers (integer) --
The number of workers of a defined workerType that are allocated when a job runs.
The maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this job run.

LogGroupName (string) --
The name of the log group for secure logging that can be server-side encrypted in Amazon CloudWatch using AWS KMS. This name can be /aws-glue/jobs/ , in which case the default encryption is NONE . If you add a role name and SecurityConfiguration name (in other words, /aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/ ), then that security configuration is used to encrypt the log group.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



GlueVersion (string) --
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.
Jobs that are created without specifying a Glue version default to Glue 0.9.







CrawlerDetails (dict) --
Details of the crawler when the node represents a crawler.

Crawls (list) --
A list of crawls represented by the crawl node.

(dict) --
The details of a crawl in the workflow.

State (string) --
The state of the crawler.

StartedOn (datetime) --
The date and time on which the crawl started.

CompletedOn (datetime) --
The date and time on which the crawl completed.

ErrorMessage (string) --
The error message associated with the crawl.

LogGroup (string) --
The log group associated with the crawl.

LogStream (string) --
The log stream associated with the crawl.











Edges (list) --
A list of all the directed connections between the nodes belonging to the workflow.

(dict) --
An edge represents a directed connection between two AWS Glue components which are part of the workflow the edge belongs to.

SourceId (string) --
The unique of the node within the workflow where the edge starts.

DestinationId (string) --
The unique of the node within the workflow where the edge ends.









Graph (dict) --
The graph representing all the AWS Glue components that belong to the workflow as nodes and directed connections between them as edges.

Nodes (list) --
A list of the the AWS Glue components belong to the workflow represented as nodes.

(dict) --
A node represents an AWS Glue component like Trigger, Job etc. which is part of a workflow.

Type (string) --
The type of AWS Glue component represented by the node.

Name (string) --
The name of the AWS Glue component represented by the node.

UniqueId (string) --
The unique Id assigned to the node within the workflow.

TriggerDetails (dict) --
Details of the Trigger when the node represents a Trigger.

Trigger (dict) --
The information of the trigger represented by the trigger node.

Name (string) --
The name of the trigger.

WorkflowName (string) --
The name of the workflow associated with the trigger.

Id (string) --
Reserved for future use.

Type (string) --
The type of trigger that this is.

State (string) --
The current state of the trigger.

Description (string) --
A description of this trigger.

Schedule (string) --
A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .

Actions (list) --
The actions initiated by this trigger.

(dict) --
Defines an action to be initiated by a trigger.

JobName (string) --
The name of a job to be executed.

Arguments (dict) --
The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this action.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



CrawlerName (string) --
The name of the crawler to be used with this action.





Predicate (dict) --
The predicate of this trigger, which defines when it will fire.

Logical (string) --
An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.

Conditions (list) --
A list of the conditions that determine when the trigger will fire.

(dict) --
Defines a condition under which a trigger fires.

LogicalOperator (string) --
A logical operator.

JobName (string) --
The name of the job whose JobRuns this condition applies to, and on which this trigger waits.

State (string) --
The condition state. Currently, the only job states that a trigger can listen for are SUCCEEDED , STOPPED , FAILED , and TIMEOUT . The only crawler states that a trigger can listen for are SUCCEEDED , FAILED , and CANCELLED .

CrawlerName (string) --
The name of the crawler to which this condition applies.

CrawlState (string) --
The state of the crawler to which this condition applies.











JobDetails (dict) --
Details of the Job when the node represents a Job.

JobRuns (list) --
The information for the job runs represented by the job node.

(dict) --
Contains information about a job run.

Id (string) --
The ID of this job run.

Attempt (integer) --
The number of the attempt to run this job.

PreviousRunId (string) --
The ID of the previous run of this job. For example, the JobRunId specified in the StartJobRun action.

TriggerName (string) --
The name of the trigger that started this job run.

JobName (string) --
The name of the job definition being used in this run.

StartedOn (datetime) --
The date and time at which this job run was started.

LastModifiedOn (datetime) --
The last time that this job run was modified.

CompletedOn (datetime) --
The date and time that this job run completed.

JobRunState (string) --
The current state of the job run. For more information about the statuses of jobs that have terminated abnormally, see AWS Glue Job Run Statuses .

Arguments (dict) --
The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




ErrorMessage (string) --
An error message associated with this job run.

PredecessorRuns (list) --
A list of predecessors to this job run.

(dict) --
A job run that was used in the predicate of a conditional trigger that triggered this job run.

JobName (string) --
The name of the job definition used by the predecessor job run.

RunId (string) --
The job-run ID of the predecessor job run.





AllocatedCapacity (integer) --
This field is deprecated. Use MaxCapacity instead.
The number of AWS Glue data processing units (DPUs) allocated to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .

ExecutionTime (integer) --
The amount of time (in seconds) that the job run consumed resources.

Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

MaxCapacity (float) --
The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .
Do not set Max Capacity if using WorkerType and NumberOfWorkers .
The value that can be allocated for MaxCapacity depends on whether you are running a Python shell job or an Apache Spark ETL job:

When you specify a Python shell job (JobCommand.Name ="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
When you specify an Apache Spark ETL job (JobCommand.Name ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.


WorkerType (string) --
The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
For the G.2X worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.


NumberOfWorkers (integer) --
The number of workers of a defined workerType that are allocated when a job runs.
The maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this job run.

LogGroupName (string) --
The name of the log group for secure logging that can be server-side encrypted in Amazon CloudWatch using AWS KMS. This name can be /aws-glue/jobs/ , in which case the default encryption is NONE . If you add a role name and SecurityConfiguration name (in other words, /aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/ ), then that security configuration is used to encrypt the log group.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



GlueVersion (string) --
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.
Jobs that are created without specifying a Glue version default to Glue 0.9.







CrawlerDetails (dict) --
Details of the crawler when the node represents a crawler.

Crawls (list) --
A list of crawls represented by the crawl node.

(dict) --
The details of a crawl in the workflow.

State (string) --
The state of the crawler.

StartedOn (datetime) --
The date and time on which the crawl started.

CompletedOn (datetime) --
The date and time on which the crawl completed.

ErrorMessage (string) --
The error message associated with the crawl.

LogGroup (string) --
The log group associated with the crawl.

LogStream (string) --
The log stream associated with the crawl.











Edges (list) --
A list of all the directed connections between the nodes belonging to the workflow.

(dict) --
An edge represents a directed connection between two AWS Glue components which are part of the workflow the edge belongs to.

SourceId (string) --
The unique of the node within the workflow where the edge starts.

DestinationId (string) --
The unique of the node within the workflow where the edge ends.











MissingWorkflows (list) --
A list of names of workflows not found.

(string) --








Exceptions

Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException


    :return: {
        'Workflows': [
            {
                'Name': 'string',
                'Description': 'string',
                'DefaultRunProperties': {
                    'string': 'string'
                },
                'CreatedOn': datetime(2015, 1, 1),
                'LastModifiedOn': datetime(2015, 1, 1),
                'LastRun': {
                    'Name': 'string',
                    'WorkflowRunId': 'string',
                    'WorkflowRunProperties': {
                        'string': 'string'
                    },
                    'StartedOn': datetime(2015, 1, 1),
                    'CompletedOn': datetime(2015, 1, 1),
                    'Status': 'RUNNING'|'COMPLETED'|'STOPPING'|'STOPPED',
                    'Statistics': {
                        'TotalActions': 123,
                        'TimeoutActions': 123,
                        'FailedActions': 123,
                        'StoppedActions': 123,
                        'SucceededActions': 123,
                        'RunningActions': 123
                    },
                    'Graph': {
                        'Nodes': [
                            {
                                'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                                'Name': 'string',
                                'UniqueId': 'string',
                                'TriggerDetails': {
                                    'Trigger': {
                                        'Name': 'string',
                                        'WorkflowName': 'string',
                                        'Id': 'string',
                                        'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                        'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                                        'Description': 'string',
                                        'Schedule': 'string',
                                        'Actions': [
                                            {
                                                'JobName': 'string',
                                                'Arguments': {
                                                    'string': 'string'
                                                },
                                                'Timeout': 123,
                                                'SecurityConfiguration': 'string',
                                                'NotificationProperty': {
                                                    'NotifyDelayAfter': 123
                                                },
                                                'CrawlerName': 'string'
                                            },
                                        ],
                                        'Predicate': {
                                            'Logical': 'AND'|'ANY',
                                            'Conditions': [
                                                {
                                                    'LogicalOperator': 'EQUALS',
                                                    'JobName': 'string',
                                                    'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                                    'CrawlerName': 'string',
                                                    'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                                                },
                                            ]
                                        }
                                    }
                                },
                                'JobDetails': {
                                    'JobRuns': [
                                        {
                                            'Id': 'string',
                                            'Attempt': 123,
                                            'PreviousRunId': 'string',
                                            'TriggerName': 'string',
                                            'JobName': 'string',
                                            'StartedOn': datetime(2015, 1, 1),
                                            'LastModifiedOn': datetime(2015, 1, 1),
                                            'CompletedOn': datetime(2015, 1, 1),
                                            'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                            'Arguments': {
                                                'string': 'string'
                                            },
                                            'ErrorMessage': 'string',
                                            'PredecessorRuns': [
                                                {
                                                    'JobName': 'string',
                                                    'RunId': 'string'
                                                },
                                            ],
                                            'AllocatedCapacity': 123,
                                            'ExecutionTime': 123,
                                            'Timeout': 123,
                                            'MaxCapacity': 123.0,
                                            'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                            'NumberOfWorkers': 123,
                                            'SecurityConfiguration': 'string',
                                            'LogGroupName': 'string',
                                            'NotificationProperty': {
                                                'NotifyDelayAfter': 123
                                            },
                                            'GlueVersion': 'string'
                                        },
                                    ]
                                },
                                'CrawlerDetails': {
                                    'Crawls': [
                                        {
                                            'State': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED',
                                            'StartedOn': datetime(2015, 1, 1),
                                            'CompletedOn': datetime(2015, 1, 1),
                                            'ErrorMessage': 'string',
                                            'LogGroup': 'string',
                                            'LogStream': 'string'
                                        },
                                    ]
                                }
                            },
                        ],
                        'Edges': [
                            {
                                'SourceId': 'string',
                                'DestinationId': 'string'
                            },
                        ]
                    }
                },
                'Graph': {
                    'Nodes': [
                        {
                            'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                            'Name': 'string',
                            'UniqueId': 'string',
                            'TriggerDetails': {
                                'Trigger': {
                                    'Name': 'string',
                                    'WorkflowName': 'string',
                                    'Id': 'string',
                                    'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                    'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                                    'Description': 'string',
                                    'Schedule': 'string',
                                    'Actions': [
                                        {
                                            'JobName': 'string',
                                            'Arguments': {
                                                'string': 'string'
                                            },
                                            'Timeout': 123,
                                            'SecurityConfiguration': 'string',
                                            'NotificationProperty': {
                                                'NotifyDelayAfter': 123
                                            },
                                            'CrawlerName': 'string'
                                        },
                                    ],
                                    'Predicate': {
                                        'Logical': 'AND'|'ANY',
                                        'Conditions': [
                                            {
                                                'LogicalOperator': 'EQUALS',
                                                'JobName': 'string',
                                                'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                                'CrawlerName': 'string',
                                                'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                                            },
                                        ]
                                    }
                                }
                            },
                            'JobDetails': {
                                'JobRuns': [
                                    {
                                        'Id': 'string',
                                        'Attempt': 123,
                                        'PreviousRunId': 'string',
                                        'TriggerName': 'string',
                                        'JobName': 'string',
                                        'StartedOn': datetime(2015, 1, 1),
                                        'LastModifiedOn': datetime(2015, 1, 1),
                                        'CompletedOn': datetime(2015, 1, 1),
                                        'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                        'Arguments': {
                                            'string': 'string'
                                        },
                                        'ErrorMessage': 'string',
                                        'PredecessorRuns': [
                                            {
                                                'JobName': 'string',
                                                'RunId': 'string'
                                            },
                                        ],
                                        'AllocatedCapacity': 123,
                                        'ExecutionTime': 123,
                                        'Timeout': 123,
                                        'MaxCapacity': 123.0,
                                        'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                        'NumberOfWorkers': 123,
                                        'SecurityConfiguration': 'string',
                                        'LogGroupName': 'string',
                                        'NotificationProperty': {
                                            'NotifyDelayAfter': 123
                                        },
                                        'GlueVersion': 'string'
                                    },
                                ]
                            },
                            'CrawlerDetails': {
                                'Crawls': [
                                    {
                                        'State': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED',
                                        'StartedOn': datetime(2015, 1, 1),
                                        'CompletedOn': datetime(2015, 1, 1),
                                        'ErrorMessage': 'string',
                                        'LogGroup': 'string',
                                        'LogStream': 'string'
                                    },
                                ]
                            }
                        },
                    ],
                    'Edges': [
                        {
                            'SourceId': 'string',
                            'DestinationId': 'string'
                        },
                    ]
                }
            },
        ],
        'MissingWorkflows': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def batch_stop_job_run(JobName=None, JobRunIds=None):
    """
    Stops one or more job runs for a specified job definition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_stop_job_run(
        JobName='string',
        JobRunIds=[
            'string',
        ]
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]\nThe name of the job definition for which to stop job runs.\n

    :type JobRunIds: list
    :param JobRunIds: [REQUIRED]\nA list of the JobRunIds that should be stopped for that job definition.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SuccessfulSubmissions': [
        {
            'JobName': 'string',
            'JobRunId': 'string'
        },
    ],
    'Errors': [
        {
            'JobName': 'string',
            'JobRunId': 'string',
            'ErrorDetail': {
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

SuccessfulSubmissions (list) --
A list of the JobRuns that were successfully submitted for stopping.

(dict) --
Records a successful request to stop a specified JobRun .

JobName (string) --
The name of the job definition used in the job run that was stopped.

JobRunId (string) --
The JobRunId of the job run that was stopped.





Errors (list) --
A list of the errors that were encountered in trying to stop JobRuns , including the JobRunId for which each error was encountered and details about the error.

(dict) --
Records an error that occurred when attempting to stop a specified job run.

JobName (string) --
The name of the job definition that is used in the job run in question.

JobRunId (string) --
The JobRunId of the job run in question.

ErrorDetail (dict) --
Specifies details about the error that was encountered.

ErrorCode (string) --
The code associated with this error.

ErrorMessage (string) --
A message describing the error.













Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'SuccessfulSubmissions': [
            {
                'JobName': 'string',
                'JobRunId': 'string'
            },
        ],
        'Errors': [
            {
                'JobName': 'string',
                'JobRunId': 'string',
                'ErrorDetail': {
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def cancel_ml_task_run(TransformId=None, TaskRunId=None):
    """
    Cancels (stops) a task run. Machine learning task runs are asynchronous tasks that AWS Glue runs on your behalf as part of various machine learning workflows. You can cancel a machine learning task run at any time by calling CancelMLTaskRun with a task run\'s parent transform\'s TransformID and the task run\'s TaskRunId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_ml_task_run(
        TransformId='string',
        TaskRunId='string'
    )
    
    
    :type TransformId: string
    :param TransformId: [REQUIRED]\nThe unique identifier of the machine learning transform.\n

    :type TaskRunId: string
    :param TaskRunId: [REQUIRED]\nA unique identifier for the task run.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TransformId': 'string',
    'TaskRunId': 'string',
    'Status': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT'
}


Response Structure

(dict) --

TransformId (string) --
The unique identifier of the machine learning transform.

TaskRunId (string) --
The unique identifier for the task run.

Status (string) --
The status for this run.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException


    :return: {
        'TransformId': 'string',
        'TaskRunId': 'string',
        'Status': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT'
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.InternalServiceException
    
    """
    pass

def create_classifier(GrokClassifier=None, XMLClassifier=None, JsonClassifier=None, CsvClassifier=None):
    """
    Creates a classifier in the user\'s account. This can be a GrokClassifier , an XMLClassifier , a JsonClassifier , or a CsvClassifier , depending on which field of the request is present.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_classifier(
        GrokClassifier={
            'Classification': 'string',
            'Name': 'string',
            'GrokPattern': 'string',
            'CustomPatterns': 'string'
        },
        XMLClassifier={
            'Classification': 'string',
            'Name': 'string',
            'RowTag': 'string'
        },
        JsonClassifier={
            'Name': 'string',
            'JsonPath': 'string'
        },
        CsvClassifier={
            'Name': 'string',
            'Delimiter': 'string',
            'QuoteSymbol': 'string',
            'ContainsHeader': 'UNKNOWN'|'PRESENT'|'ABSENT',
            'Header': [
                'string',
            ],
            'DisableValueTrimming': True|False,
            'AllowSingleColumn': True|False
        }
    )
    
    
    :type GrokClassifier: dict
    :param GrokClassifier: A GrokClassifier object specifying the classifier to create.\n\nClassification (string) -- [REQUIRED]An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.\n\nName (string) -- [REQUIRED]The name of the new classifier.\n\nGrokPattern (string) -- [REQUIRED]The grok pattern used by this classifier.\n\nCustomPatterns (string) --Optional custom grok patterns used by this classifier.\n\n\n

    :type XMLClassifier: dict
    :param XMLClassifier: An XMLClassifier object specifying the classifier to create.\n\nClassification (string) -- [REQUIRED]An identifier of the data format that the classifier matches.\n\nName (string) -- [REQUIRED]The name of the classifier.\n\nRowTag (string) --The XML tag designating the element that contains each record in an XML document being parsed. This can\'t identify a self-closing element (closed by /> ). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, <row item_a='A' item_b='B'></row> is okay, but <row item_a='A' item_b='B' /> is not).\n\n\n

    :type JsonClassifier: dict
    :param JsonClassifier: A JsonClassifier object specifying the classifier to create.\n\nName (string) -- [REQUIRED]The name of the classifier.\n\nJsonPath (string) -- [REQUIRED]A JsonPath string defining the JSON data for the classifier to classify. AWS Glue supports a subset of JsonPath , as described in Writing JsonPath Custom Classifiers .\n\n\n

    :type CsvClassifier: dict
    :param CsvClassifier: A CsvClassifier object specifying the classifier to create.\n\nName (string) -- [REQUIRED]The name of the classifier.\n\nDelimiter (string) --A custom symbol to denote what separates each column entry in the row.\n\nQuoteSymbol (string) --A custom symbol to denote what combines content into a single column value. Must be different from the column delimiter.\n\nContainsHeader (string) --Indicates whether the CSV file contains a header.\n\nHeader (list) --A list of strings representing column names.\n\n(string) --\n\n\nDisableValueTrimming (boolean) --Specifies not to trim values before identifying the type of column values. The default value is true.\n\nAllowSingleColumn (boolean) --Enables the processing of files that contain only one column.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_connection(CatalogId=None, ConnectionInput=None):
    """
    Creates a connection definition in the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_connection(
        CatalogId='string',
        ConnectionInput={
            'Name': 'string',
            'Description': 'string',
            'ConnectionType': 'JDBC'|'SFTP'|'MONGODB'|'KAFKA',
            'MatchCriteria': [
                'string',
            ],
            'ConnectionProperties': {
                'string': 'string'
            },
            'PhysicalConnectionRequirements': {
                'SubnetId': 'string',
                'SecurityGroupIdList': [
                    'string',
                ],
                'AvailabilityZone': 'string'
            }
        }
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which to create the connection. If none is provided, the AWS account ID is used by default.

    :type ConnectionInput: dict
    :param ConnectionInput: [REQUIRED]\nA ConnectionInput object defining the connection to create.\n\nName (string) -- [REQUIRED]The name of the connection.\n\nDescription (string) --The description of the connection.\n\nConnectionType (string) -- [REQUIRED]The type of the connection. Currently, these types are supported:\n\nJDBC - Designates a connection to a database through Java Database Connectivity (JDBC).\nKAFKA - Designates a connection to an Apache Kafka streaming platform.\nMONGODB - Designates a connection to a MongoDB document database.\n\nSFTP is not supported.\n\nMatchCriteria (list) --A list of criteria that can be used in selecting this connection.\n\n(string) --\n\n\nConnectionProperties (dict) -- [REQUIRED]These key-value pairs define parameters for the connection.\n\n(string) --\n(string) --\n\n\n\n\nPhysicalConnectionRequirements (dict) --A map of physical connection requirements, such as virtual private cloud (VPC) and SecurityGroup , that are needed to successfully make this connection.\n\nSubnetId (string) --The subnet ID used by the connection.\n\nSecurityGroupIdList (list) --The security group ID list used by the connection.\n\n(string) --\n\n\nAvailabilityZone (string) --The connection\'s Availability Zone. This field is redundant because the specified subnet implies the Availability Zone to be used. Currently the field must be populated, but it will be deprecated in the future.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.GlueEncryptionException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_crawler(Name=None, Role=None, DatabaseName=None, Description=None, Targets=None, Schedule=None, Classifiers=None, TablePrefix=None, SchemaChangePolicy=None, Configuration=None, CrawlerSecurityConfiguration=None, Tags=None):
    """
    Creates a new crawler with specified targets, role, configuration, and optional schedule. At least one crawl target must be specified, in the s3Targets field, the jdbcTargets field, or the DynamoDBTargets field.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_crawler(
        Name='string',
        Role='string',
        DatabaseName='string',
        Description='string',
        Targets={
            'S3Targets': [
                {
                    'Path': 'string',
                    'Exclusions': [
                        'string',
                    ]
                },
            ],
            'JdbcTargets': [
                {
                    'ConnectionName': 'string',
                    'Path': 'string',
                    'Exclusions': [
                        'string',
                    ]
                },
            ],
            'DynamoDBTargets': [
                {
                    'Path': 'string'
                },
            ],
            'CatalogTargets': [
                {
                    'DatabaseName': 'string',
                    'Tables': [
                        'string',
                    ]
                },
            ]
        },
        Schedule='string',
        Classifiers=[
            'string',
        ],
        TablePrefix='string',
        SchemaChangePolicy={
            'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
            'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
        },
        Configuration='string',
        CrawlerSecurityConfiguration='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the new crawler.\n

    :type Role: string
    :param Role: [REQUIRED]\nThe IAM role or Amazon Resource Name (ARN) of an IAM role used by the new crawler to access customer resources.\n

    :type DatabaseName: string
    :param DatabaseName: The AWS Glue database where results are written, such as: arn:aws:daylight:us-east-1::database/sometable/* .

    :type Description: string
    :param Description: A description of the new crawler.

    :type Targets: dict
    :param Targets: [REQUIRED]\nA list of collection of targets to crawl.\n\nS3Targets (list) --Specifies Amazon Simple Storage Service (Amazon S3) targets.\n\n(dict) --Specifies a data store in Amazon Simple Storage Service (Amazon S3).\n\nPath (string) --The path to the Amazon S3 target.\n\nExclusions (list) --A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler .\n\n(string) --\n\n\n\n\n\n\nJdbcTargets (list) --Specifies JDBC targets.\n\n(dict) --Specifies a JDBC data store to crawl.\n\nConnectionName (string) --The name of the connection to use to connect to the JDBC target.\n\nPath (string) --The path of the JDBC target.\n\nExclusions (list) --A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler .\n\n(string) --\n\n\n\n\n\n\nDynamoDBTargets (list) --Specifies Amazon DynamoDB targets.\n\n(dict) --Specifies an Amazon DynamoDB table to crawl.\n\nPath (string) --The name of the DynamoDB table to crawl.\n\n\n\n\n\nCatalogTargets (list) --Specifies AWS Glue Data Catalog targets.\n\n(dict) --Specifies an AWS Glue Data Catalog target.\n\nDatabaseName (string) -- [REQUIRED]The name of the database to be synchronized.\n\nTables (list) -- [REQUIRED]A list of the tables to be synchronized.\n\n(string) --\n\n\n\n\n\n\n\n

    :type Schedule: string
    :param Schedule: A cron expression used to specify the schedule. For more information, see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, specify cron(15 12 * * ? *) .

    :type Classifiers: list
    :param Classifiers: A list of custom classifiers that the user has registered. By default, all built-in classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.\n\n(string) --\n\n

    :type TablePrefix: string
    :param TablePrefix: The table prefix used for catalog tables that are created.

    :type SchemaChangePolicy: dict
    :param SchemaChangePolicy: The policy for the crawler\'s update and deletion behavior.\n\nUpdateBehavior (string) --The update behavior when the crawler finds a changed schema.\n\nDeleteBehavior (string) --The deletion behavior when the crawler finds a deleted object.\n\n\n

    :type Configuration: string
    :param Configuration: The crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler\'s behavior. For more information, see Configuring a Crawler .

    :type CrawlerSecurityConfiguration: string
    :param CrawlerSecurityConfiguration: The name of the SecurityConfiguration structure to be used by this crawler.

    :type Tags: dict
    :param Tags: The tags to use with this crawler request. You can use tags to limit access to the crawler. For more information, see AWS Tags in AWS Glue .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ResourceNumberLimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_database(CatalogId=None, DatabaseInput=None):
    """
    Creates a new database in a Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_database(
        CatalogId='string',
        DatabaseInput={
            'Name': 'string',
            'Description': 'string',
            'LocationUri': 'string',
            'Parameters': {
                'string': 'string'
            },
            'CreateTableDefaultPermissions': [
                {
                    'Principal': {
                        'DataLakePrincipalIdentifier': 'string'
                    },
                    'Permissions': [
                        'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                    ]
                },
            ]
        }
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which to create the database. If none is provided, the AWS account ID is used by default.

    :type DatabaseInput: dict
    :param DatabaseInput: [REQUIRED]\nThe metadata for the database.\n\nName (string) -- [REQUIRED]The name of the database. For Hive compatibility, this is folded to lowercase when it is stored.\n\nDescription (string) --A description of the database.\n\nLocationUri (string) --The location of the database (for example, an HDFS path).\n\nParameters (dict) --These key-value pairs define parameters and properties of the database.\nThese key-value pairs define parameters and properties of the database.\n\n(string) --\n(string) --\n\n\n\n\nCreateTableDefaultPermissions (list) --Creates a set of default permissions on the table for principals.\n\n(dict) --Permissions granted to a principal.\n\nPrincipal (dict) --The principal who is granted permissions.\n\nDataLakePrincipalIdentifier (string) --An identifier for the AWS Lake Formation principal.\n\n\n\nPermissions (list) --The permissions that are granted to the principal.\n\n(string) --\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.GlueEncryptionException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_dev_endpoint(EndpointName=None, RoleArn=None, SecurityGroupIds=None, SubnetId=None, PublicKey=None, PublicKeys=None, NumberOfNodes=None, WorkerType=None, GlueVersion=None, NumberOfWorkers=None, ExtraPythonLibsS3Path=None, ExtraJarsS3Path=None, SecurityConfiguration=None, Tags=None, Arguments=None):
    """
    Creates a new development endpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_dev_endpoint(
        EndpointName='string',
        RoleArn='string',
        SecurityGroupIds=[
            'string',
        ],
        SubnetId='string',
        PublicKey='string',
        PublicKeys=[
            'string',
        ],
        NumberOfNodes=123,
        WorkerType='Standard'|'G.1X'|'G.2X',
        GlueVersion='string',
        NumberOfWorkers=123,
        ExtraPythonLibsS3Path='string',
        ExtraJarsS3Path='string',
        SecurityConfiguration='string',
        Tags={
            'string': 'string'
        },
        Arguments={
            'string': 'string'
        }
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]\nThe name to be assigned to the new DevEndpoint .\n

    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nThe IAM role for the DevEndpoint .\n

    :type SecurityGroupIds: list
    :param SecurityGroupIds: Security group IDs for the security groups to be used by the new DevEndpoint .\n\n(string) --\n\n

    :type SubnetId: string
    :param SubnetId: The subnet ID for the new DevEndpoint to use.

    :type PublicKey: string
    :param PublicKey: The public key to be used by this DevEndpoint for authentication. This attribute is provided for backward compatibility because the recommended attribute to use is public keys.

    :type PublicKeys: list
    :param PublicKeys: A list of public keys to be used by the development endpoints for authentication. The use of this attribute is preferred over a single public key because the public keys allow you to have a different private key per client.\n\nNote\nIf you previously created an endpoint with a public key, you must remove that key to be able to set a list of public keys. Call the UpdateDevEndpoint API with the public key content in the deletePublicKeys attribute, and the list of new keys in the addPublicKeys attribute.\n\n\n(string) --\n\n

    :type NumberOfNodes: integer
    :param NumberOfNodes: The number of AWS Glue Data Processing Units (DPUs) to allocate to this DevEndpoint .

    :type WorkerType: string
    :param WorkerType: The type of predefined worker that is allocated to the development endpoint. Accepts a value of Standard, G.1X, or G.2X.\n\nFor the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.\nFor the G.1X worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.\nFor the G.2X worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.\n\nKnown issue: when a development endpoint is created with the G.2X WorkerType configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB of memory, and a 64 GB disk.\n

    :type GlueVersion: string
    :param GlueVersion: Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints.\nFor more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.\nDevelopment endpoints that are created without specifying a Glue version default to Glue 0.9.\nYou can specify a version of Python support for development endpoints by using the Arguments parameter in the CreateDevEndpoint or UpdateDevEndpoint APIs. If no arguments are provided, the version defaults to Python 2.\n

    :type NumberOfWorkers: integer
    :param NumberOfWorkers: The number of workers of a defined workerType that are allocated to the development endpoint.\nThe maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .\n

    :type ExtraPythonLibsS3Path: string
    :param ExtraPythonLibsS3Path: The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your DevEndpoint . Multiple values must be complete paths separated by a comma.\n\nNote\nYou can only use pure Python libraries with a DevEndpoint . Libraries that rely on C extensions, such as the pandas Python data analysis library, are not yet supported.\n\n

    :type ExtraJarsS3Path: string
    :param ExtraJarsS3Path: The path to one or more Java .jar files in an S3 bucket that should be loaded in your DevEndpoint .

    :type SecurityConfiguration: string
    :param SecurityConfiguration: The name of the SecurityConfiguration structure to be used with this DevEndpoint .

    :type Tags: dict
    :param Tags: The tags to use with this DevEndpoint. You may use tags to limit access to the DevEndpoint. For more information about tags in AWS Glue, see AWS Tags in AWS Glue in the developer guide.\n\n(string) --\n(string) --\n\n\n\n

    :type Arguments: dict
    :param Arguments: A map of arguments used to configure the DevEndpoint .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EndpointName': 'string',
    'Status': 'string',
    'SecurityGroupIds': [
        'string',
    ],
    'SubnetId': 'string',
    'RoleArn': 'string',
    'YarnEndpointAddress': 'string',
    'ZeppelinRemoteSparkInterpreterPort': 123,
    'NumberOfNodes': 123,
    'WorkerType': 'Standard'|'G.1X'|'G.2X',
    'GlueVersion': 'string',
    'NumberOfWorkers': 123,
    'AvailabilityZone': 'string',
    'VpcId': 'string',
    'ExtraPythonLibsS3Path': 'string',
    'ExtraJarsS3Path': 'string',
    'FailureReason': 'string',
    'SecurityConfiguration': 'string',
    'CreatedTimestamp': datetime(2015, 1, 1),
    'Arguments': {
        'string': 'string'
    }
}


Response Structure

(dict) --

EndpointName (string) --
The name assigned to the new DevEndpoint .

Status (string) --
The current status of the new DevEndpoint .

SecurityGroupIds (list) --
The security groups assigned to the new DevEndpoint .

(string) --


SubnetId (string) --
The subnet ID assigned to the new DevEndpoint .

RoleArn (string) --
The Amazon Resource Name (ARN) of the role assigned to the new DevEndpoint .

YarnEndpointAddress (string) --
The address of the YARN endpoint used by this DevEndpoint .

ZeppelinRemoteSparkInterpreterPort (integer) --
The Apache Zeppelin port for the remote Apache Spark interpreter.

NumberOfNodes (integer) --
The number of AWS Glue Data Processing Units (DPUs) allocated to this DevEndpoint.

WorkerType (string) --
The type of predefined worker that is allocated to the development endpoint. May be a value of Standard, G.1X, or G.2X.

GlueVersion (string) --
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints.

NumberOfWorkers (integer) --
The number of workers of a defined workerType that are allocated to the development endpoint.

AvailabilityZone (string) --
The AWS Availability Zone where this DevEndpoint is located.

VpcId (string) --
The ID of the virtual private cloud (VPC) used by this DevEndpoint .

ExtraPythonLibsS3Path (string) --
The paths to one or more Python libraries in an S3 bucket that will be loaded in your DevEndpoint .

ExtraJarsS3Path (string) --
Path to one or more Java .jar files in an S3 bucket that will be loaded in your DevEndpoint .

FailureReason (string) --
The reason for a current failure in this DevEndpoint .

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure being used with this DevEndpoint .

CreatedTimestamp (datetime) --
The point in time at which this DevEndpoint was created.

Arguments (dict) --
The map of arguments used to configure this DevEndpoint .
Valid arguments are:

"--enable-glue-datacatalog": ""
"GLUE_PYTHON_VERSION": "3"
"GLUE_PYTHON_VERSION": "2"

You can specify a version of Python support for development endpoints by using the Arguments parameter in the CreateDevEndpoint or UpdateDevEndpoint APIs. If no arguments are provided, the version defaults to Python 2.

(string) --
(string) --










Exceptions

Glue.Client.exceptions.AccessDeniedException
Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.IdempotentParameterMismatchException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.ValidationException
Glue.Client.exceptions.ResourceNumberLimitExceededException


    :return: {
        'EndpointName': 'string',
        'Status': 'string',
        'SecurityGroupIds': [
            'string',
        ],
        'SubnetId': 'string',
        'RoleArn': 'string',
        'YarnEndpointAddress': 'string',
        'ZeppelinRemoteSparkInterpreterPort': 123,
        'NumberOfNodes': 123,
        'WorkerType': 'Standard'|'G.1X'|'G.2X',
        'GlueVersion': 'string',
        'NumberOfWorkers': 123,
        'AvailabilityZone': 'string',
        'VpcId': 'string',
        'ExtraPythonLibsS3Path': 'string',
        'ExtraJarsS3Path': 'string',
        'FailureReason': 'string',
        'SecurityConfiguration': 'string',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'Arguments': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_job(Name=None, Description=None, LogUri=None, Role=None, ExecutionProperty=None, Command=None, DefaultArguments=None, NonOverridableArguments=None, Connections=None, MaxRetries=None, AllocatedCapacity=None, Timeout=None, MaxCapacity=None, SecurityConfiguration=None, Tags=None, NotificationProperty=None, GlueVersion=None, NumberOfWorkers=None, WorkerType=None):
    """
    Creates a new job definition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_job(
        Name='string',
        Description='string',
        LogUri='string',
        Role='string',
        ExecutionProperty={
            'MaxConcurrentRuns': 123
        },
        Command={
            'Name': 'string',
            'ScriptLocation': 'string',
            'PythonVersion': 'string'
        },
        DefaultArguments={
            'string': 'string'
        },
        NonOverridableArguments={
            'string': 'string'
        },
        Connections={
            'Connections': [
                'string',
            ]
        },
        MaxRetries=123,
        AllocatedCapacity=123,
        Timeout=123,
        MaxCapacity=123.0,
        SecurityConfiguration='string',
        Tags={
            'string': 'string'
        },
        NotificationProperty={
            'NotifyDelayAfter': 123
        },
        GlueVersion='string',
        NumberOfWorkers=123,
        WorkerType='Standard'|'G.1X'|'G.2X'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name you assign to this job definition. It must be unique in your account.\n

    :type Description: string
    :param Description: Description of the job being defined.

    :type LogUri: string
    :param LogUri: This field is reserved for future use.

    :type Role: string
    :param Role: [REQUIRED]\nThe name or Amazon Resource Name (ARN) of the IAM role associated with this job.\n

    :type ExecutionProperty: dict
    :param ExecutionProperty: An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job.\n\nMaxConcurrentRuns (integer) --The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.\n\n\n

    :type Command: dict
    :param Command: [REQUIRED]\nThe JobCommand that executes this job.\n\nName (string) --The name of the job command. For an Apache Spark ETL job, this must be glueetl . For a Python shell job, it must be pythonshell .\n\nScriptLocation (string) --Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that executes a job.\n\nPythonVersion (string) --The Python version being used to execute a Python shell job. Allowed values are 2 or 3.\n\n\n

    :type DefaultArguments: dict
    :param DefaultArguments: The default arguments for this job.\nYou can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.\nFor information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.\nFor information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.\n\n(string) --\n(string) --\n\n\n\n

    :type NonOverridableArguments: dict
    :param NonOverridableArguments: Non-overridable arguments for this job, specified as name-value pairs.\n\n(string) --\n(string) --\n\n\n\n

    :type Connections: dict
    :param Connections: The connections used for this job.\n\nConnections (list) --A list of connections used by the job.\n\n(string) --\n\n\n\n

    :type MaxRetries: integer
    :param MaxRetries: The maximum number of times to retry this job if it fails.

    :type AllocatedCapacity: integer
    :param AllocatedCapacity: This parameter is deprecated. Use MaxCapacity instead.\nThe number of AWS Glue data processing units (DPUs) to allocate to this Job. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .\n

    :type Timeout: integer
    :param Timeout: The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours).

    :type MaxCapacity: float
    :param MaxCapacity: The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .\nDo not set Max Capacity if using WorkerType and NumberOfWorkers .\nThe value that can be allocated for MaxCapacity depends on whether you are running a Python shell job or an Apache Spark ETL job:\n\nWhen you specify a Python shell job (JobCommand.Name ='pythonshell'), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.\nWhen you specify an Apache Spark ETL job (JobCommand.Name ='glueetl'), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.\n\n

    :type SecurityConfiguration: string
    :param SecurityConfiguration: The name of the SecurityConfiguration structure to be used with this job.

    :type Tags: dict
    :param Tags: The tags to use with this job. You may use tags to limit access to the job. For more information about tags in AWS Glue, see AWS Tags in AWS Glue in the developer guide.\n\n(string) --\n(string) --\n\n\n\n

    :type NotificationProperty: dict
    :param NotificationProperty: Specifies configuration properties of a job notification.\n\nNotifyDelayAfter (integer) --After a job run starts, the number of minutes to wait before sending a job run delay notification.\n\n\n

    :type GlueVersion: string
    :param GlueVersion: Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark.\nFor more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.\nJobs that are created without specifying a Glue version default to Glue 0.9.\n

    :type NumberOfWorkers: integer
    :param NumberOfWorkers: The number of workers of a defined workerType that are allocated when a job runs.\nThe maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .\n

    :type WorkerType: string
    :param WorkerType: The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.\n\nFor the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.\nFor the G.1X worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.\nFor the G.2X worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string'
}


Response Structure

(dict) --

Name (string) --
The unique name that was provided for this job definition.







Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.IdempotentParameterMismatchException
Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.ConcurrentModificationException


    :return: {
        'Name': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.IdempotentParameterMismatchException
    Glue.Client.exceptions.AlreadyExistsException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.ResourceNumberLimitExceededException
    Glue.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def create_ml_transform(Name=None, Description=None, InputRecordTables=None, Parameters=None, Role=None, GlueVersion=None, MaxCapacity=None, WorkerType=None, NumberOfWorkers=None, Timeout=None, MaxRetries=None, Tags=None):
    """
    Creates an AWS Glue machine learning transform. This operation creates the transform and all the necessary parameters to train it.
    Call this operation as the first step in the process of using a machine learning transform (such as the FindMatches transform) for deduplicating data. You can provide an optional Description , in addition to the parameters that you want to use for your algorithm.
    You must also specify certain parameters for the tasks that AWS Glue runs on your behalf as part of learning from your data and creating a high-quality machine learning transform. These parameters include Role , and optionally, AllocatedCapacity , Timeout , and MaxRetries . For more information, see Jobs .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_ml_transform(
        Name='string',
        Description='string',
        InputRecordTables=[
            {
                'DatabaseName': 'string',
                'TableName': 'string',
                'CatalogId': 'string',
                'ConnectionName': 'string'
            },
        ],
        Parameters={
            'TransformType': 'FIND_MATCHES',
            'FindMatchesParameters': {
                'PrimaryKeyColumnName': 'string',
                'PrecisionRecallTradeoff': 123.0,
                'AccuracyCostTradeoff': 123.0,
                'EnforceProvidedLabels': True|False
            }
        },
        Role='string',
        GlueVersion='string',
        MaxCapacity=123.0,
        WorkerType='Standard'|'G.1X'|'G.2X',
        NumberOfWorkers=123,
        Timeout=123,
        MaxRetries=123,
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe unique name that you give the transform when you create it.\n

    :type Description: string
    :param Description: A description of the machine learning transform that is being defined. The default is an empty string.

    :type InputRecordTables: list
    :param InputRecordTables: [REQUIRED]\nA list of AWS Glue table definitions used by the transform.\n\n(dict) --The database and table in the AWS Glue Data Catalog that is used for input or output data.\n\nDatabaseName (string) -- [REQUIRED]A database name in the AWS Glue Data Catalog.\n\nTableName (string) -- [REQUIRED]A table name in the AWS Glue Data Catalog.\n\nCatalogId (string) --A unique identifier for the AWS Glue Data Catalog.\n\nConnectionName (string) --The name of the connection to the AWS Glue Data Catalog.\n\n\n\n\n

    :type Parameters: dict
    :param Parameters: [REQUIRED]\nThe algorithmic parameters that are specific to the transform type used. Conditionally dependent on the transform type.\n\nTransformType (string) -- [REQUIRED]The type of machine learning transform.\nFor information about the types of machine learning transforms, see Creating Machine Learning Transforms .\n\nFindMatchesParameters (dict) --The parameters for the find matches algorithm.\n\nPrimaryKeyColumnName (string) --The name of a column that uniquely identifies rows in the source table. Used to help identify matching records.\n\nPrecisionRecallTradeoff (float) --The value selected when tuning your transform for a balance between precision and recall. A value of 0.5 means no preference; a value of 1.0 means a bias purely for precision, and a value of 0.0 means a bias for recall. Because this is a tradeoff, choosing values close to 1.0 means very low recall, and choosing values close to 0.0 results in very low precision.\nThe precision metric indicates how often your model is correct when it predicts a match.\nThe recall metric indicates that for an actual match, how often your model predicts the match.\n\nAccuracyCostTradeoff (float) --The value that is selected when tuning your transform for a balance between accuracy and cost. A value of 0.5 means that the system balances accuracy and cost concerns. A value of 1.0 means a bias purely for accuracy, which typically results in a higher cost, sometimes substantially higher. A value of 0.0 means a bias purely for cost, which results in a less accurate FindMatches transform, sometimes with unacceptable accuracy.\nAccuracy measures how well the transform finds true positives and true negatives. Increasing accuracy requires more machine resources and cost. But it also results in increased recall.\nCost measures how many compute resources, and thus money, are consumed to run the transform.\n\nEnforceProvidedLabels (boolean) --The value to switch on or off to force the output to match the provided labels from users. If the value is True , the find matches transform forces the output to match the provided labels. The results override the normal conflation results. If the value is False , the find matches transform does not ensure all the labels provided are respected, and the results rely on the trained model.\nNote that setting this value to true may increase the conflation execution time.\n\n\n\n\n

    :type Role: string
    :param Role: [REQUIRED]\nThe name or Amazon Resource Name (ARN) of the IAM role with the required permissions. The required permissions include both AWS Glue service role permissions to AWS Glue resources, and Amazon S3 permissions required by the transform.\n\nThis role needs AWS Glue service role permissions to allow access to resources in AWS Glue. See Attach a Policy to IAM Users That Access AWS Glue .\nThis role needs permission to your Amazon Simple Storage Service (Amazon S3) sources, targets, temporary directory, scripts, and any libraries used by the task run for this transform.\n\n

    :type GlueVersion: string
    :param GlueVersion: This value determines which version of AWS Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see AWS Glue Versions in the developer guide.

    :type MaxCapacity: float
    :param MaxCapacity: The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .\n\nMaxCapacity is a mutually exclusive option with NumberOfWorkers and WorkerType .\n\nIf either NumberOfWorkers or WorkerType is set, then MaxCapacity cannot be set.\nIf MaxCapacity is set then neither NumberOfWorkers or WorkerType can be set.\nIf WorkerType is set, then NumberOfWorkers is required (and vice versa).\nMaxCapacity and NumberOfWorkers must both be at least 1.\n\nWhen the WorkerType field is set to a value other than Standard , the MaxCapacity field is set automatically and becomes read-only.\nWhen the WorkerType field is set to a value other than Standard , the MaxCapacity field is set automatically and becomes read-only.\n

    :type WorkerType: string
    :param WorkerType: The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.\n\nFor the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.\nFor the G.1X worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.\nFor the G.2X worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.\n\n\nMaxCapacity is a mutually exclusive option with NumberOfWorkers and WorkerType .\n\nIf either NumberOfWorkers or WorkerType is set, then MaxCapacity cannot be set.\nIf MaxCapacity is set then neither NumberOfWorkers or WorkerType can be set.\nIf WorkerType is set, then NumberOfWorkers is required (and vice versa).\nMaxCapacity and NumberOfWorkers must both be at least 1.\n\n

    :type NumberOfWorkers: integer
    :param NumberOfWorkers: The number of workers of a defined workerType that are allocated when this task runs.\nIf WorkerType is set, then NumberOfWorkers is required (and vice versa).\n

    :type Timeout: integer
    :param Timeout: The timeout of the task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours).

    :type MaxRetries: integer
    :param MaxRetries: The maximum number of times to retry a task for this transform after a task run fails.

    :type Tags: dict
    :param Tags: The tags to use with this machine learning transform. You may use tags to limit access to the machine learning transform. For more information about tags in AWS Glue, see AWS Tags in AWS Glue in the developer guide.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TransformId': 'string'
}


Response Structure

(dict) --

TransformId (string) --
A unique identifier that is generated for the transform.







Exceptions

Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.AccessDeniedException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.IdempotentParameterMismatchException


    :return: {
        'TransformId': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.AlreadyExistsException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.AccessDeniedException
    Glue.Client.exceptions.ResourceNumberLimitExceededException
    Glue.Client.exceptions.IdempotentParameterMismatchException
    
    """
    pass

def create_partition(CatalogId=None, DatabaseName=None, TableName=None, PartitionInput=None):
    """
    Creates a new partition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_partition(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        PartitionInput={
            'Values': [
                'string',
            ],
            'LastAccessTime': datetime(2015, 1, 1),
            'StorageDescriptor': {
                'Columns': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'Location': 'string',
                'InputFormat': 'string',
                'OutputFormat': 'string',
                'Compressed': True|False,
                'NumberOfBuckets': 123,
                'SerdeInfo': {
                    'Name': 'string',
                    'SerializationLibrary': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
                'BucketColumns': [
                    'string',
                ],
                'SortColumns': [
                    {
                        'Column': 'string',
                        'SortOrder': 123
                    },
                ],
                'Parameters': {
                    'string': 'string'
                },
                'SkewedInfo': {
                    'SkewedColumnNames': [
                        'string',
                    ],
                    'SkewedColumnValues': [
                        'string',
                    ],
                    'SkewedColumnValueLocationMaps': {
                        'string': 'string'
                    }
                },
                'StoredAsSubDirectories': True|False
            },
            'Parameters': {
                'string': 'string'
            },
            'LastAnalyzedTime': datetime(2015, 1, 1)
        }
    )
    
    
    :type CatalogId: string
    :param CatalogId: The AWS account ID of the catalog in which the partition is to be created.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the metadata database in which the partition is to be created.\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the metadata table in which the partition is to be created.\n

    :type PartitionInput: dict
    :param PartitionInput: [REQUIRED]\nA PartitionInput structure defining the partition to be created.\n\nValues (list) --The values of the partition. Although this parameter is not required by the SDK, you must specify this parameter for a valid input.\nThe values for the keys for the new partition must be passed as an array of String objects that must be ordered in the same order as the partition keys appearing in the Amazon S3 prefix. Otherwise AWS Glue will add the values to the wrong keys.\n\n(string) --\n\n\nLastAccessTime (datetime) --The last time at which the partition was accessed.\n\nStorageDescriptor (dict) --Provides information about the physical location where the partition is stored.\n\nColumns (list) --A list of the Columns in the table.\n\n(dict) --A column in a Table .\n\nName (string) -- [REQUIRED]The name of the Column .\n\nType (string) --The data type of the Column .\n\nComment (string) --A free-form text comment.\n\nParameters (dict) --These key-value pairs define properties associated with the column.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\nLocation (string) --The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.\n\nInputFormat (string) --The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.\n\nOutputFormat (string) --The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.\n\nCompressed (boolean) --\nTrue if the data in the table is compressed, or False if not.\n\nNumberOfBuckets (integer) --Must be specified if the table contains any dimension columns.\n\nSerdeInfo (dict) --The serialization/deserialization (SerDe) information.\n\nName (string) --Name of the SerDe.\n\nSerializationLibrary (string) --Usually the class that implements the SerDe. An example is org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .\n\nParameters (dict) --These key-value pairs define initialization parameters for the SerDe.\n\n(string) --\n(string) --\n\n\n\n\n\n\nBucketColumns (list) --A list of reducer grouping columns, clustering columns, and bucketing columns in the table.\n\n(string) --\n\n\nSortColumns (list) --A list specifying the sort order of each bucket in the table.\n\n(dict) --Specifies the sort order of a sorted column.\n\nColumn (string) -- [REQUIRED]The name of the column.\n\nSortOrder (integer) -- [REQUIRED]Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).\n\n\n\n\n\nParameters (dict) --The user-supplied properties in key-value form.\n\n(string) --\n(string) --\n\n\n\n\nSkewedInfo (dict) --The information about values that appear frequently in a column (skewed values).\n\nSkewedColumnNames (list) --A list of names of columns that contain skewed values.\n\n(string) --\n\n\nSkewedColumnValues (list) --A list of values that appear so frequently as to be considered skewed.\n\n(string) --\n\n\nSkewedColumnValueLocationMaps (dict) --A mapping of skewed values to the columns that contain them.\n\n(string) --\n(string) --\n\n\n\n\n\n\nStoredAsSubDirectories (boolean) --\nTrue if the table data is stored in subdirectories, or False if not.\n\n\n\nParameters (dict) --These key-value pairs define partition parameters.\n\n(string) --\n(string) --\n\n\n\n\nLastAnalyzedTime (datetime) --The last time at which column statistics were computed for this partition.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.GlueEncryptionException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_script(DagNodes=None, DagEdges=None, Language=None):
    """
    Transforms a directed acyclic graph (DAG) into code.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_script(
        DagNodes=[
            {
                'Id': 'string',
                'NodeType': 'string',
                'Args': [
                    {
                        'Name': 'string',
                        'Value': 'string',
                        'Param': True|False
                    },
                ],
                'LineNumber': 123
            },
        ],
        DagEdges=[
            {
                'Source': 'string',
                'Target': 'string',
                'TargetParameter': 'string'
            },
        ],
        Language='PYTHON'|'SCALA'
    )
    
    
    :type DagNodes: list
    :param DagNodes: A list of the nodes in the DAG.\n\n(dict) --Represents a node in a directed acyclic graph (DAG)\n\nId (string) -- [REQUIRED]A node identifier that is unique within the node\'s graph.\n\nNodeType (string) -- [REQUIRED]The type of node that this is.\n\nArgs (list) -- [REQUIRED]Properties of the node, in the form of name-value pairs.\n\n(dict) --An argument or property of a node.\n\nName (string) -- [REQUIRED]The name of the argument or property.\n\nValue (string) -- [REQUIRED]The value of the argument or property.\n\nParam (boolean) --True if the value is used as a parameter.\n\n\n\n\n\nLineNumber (integer) --The line number of the node.\n\n\n\n\n

    :type DagEdges: list
    :param DagEdges: A list of the edges in the DAG.\n\n(dict) --Represents a directional edge in a directed acyclic graph (DAG).\n\nSource (string) -- [REQUIRED]The ID of the node at which the edge starts.\n\nTarget (string) -- [REQUIRED]The ID of the node at which the edge ends.\n\nTargetParameter (string) --The target of the edge.\n\n\n\n\n

    :type Language: string
    :param Language: The programming language of the resulting code from the DAG.

    :rtype: dict

ReturnsResponse Syntax
{
    'PythonScript': 'string',
    'ScalaCode': 'string'
}


Response Structure

(dict) --

PythonScript (string) --
The Python script generated from the DAG.

ScalaCode (string) --
The Scala code generated from the DAG.







Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'PythonScript': 'string',
        'ScalaCode': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def create_security_configuration(Name=None, EncryptionConfiguration=None):
    """
    Creates a new security configuration. A security configuration is a set of security properties that can be used by AWS Glue. You can use a security configuration to encrypt data at rest. For information about using security configurations in AWS Glue, see Encrypting Data Written by Crawlers, Jobs, and Development Endpoints .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_security_configuration(
        Name='string',
        EncryptionConfiguration={
            'S3Encryption': [
                {
                    'S3EncryptionMode': 'DISABLED'|'SSE-KMS'|'SSE-S3',
                    'KmsKeyArn': 'string'
                },
            ],
            'CloudWatchEncryption': {
                'CloudWatchEncryptionMode': 'DISABLED'|'SSE-KMS',
                'KmsKeyArn': 'string'
            },
            'JobBookmarksEncryption': {
                'JobBookmarksEncryptionMode': 'DISABLED'|'CSE-KMS',
                'KmsKeyArn': 'string'
            }
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name for the new security configuration.\n

    :type EncryptionConfiguration: dict
    :param EncryptionConfiguration: [REQUIRED]\nThe encryption configuration for the new security configuration.\n\nS3Encryption (list) --The encryption configuration for Amazon Simple Storage Service (Amazon S3) data.\n\n(dict) --Specifies how Amazon Simple Storage Service (Amazon S3) data should be encrypted.\n\nS3EncryptionMode (string) --The encryption mode to use for Amazon S3 data.\n\nKmsKeyArn (string) --The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.\n\n\n\n\n\nCloudWatchEncryption (dict) --The encryption configuration for Amazon CloudWatch.\n\nCloudWatchEncryptionMode (string) --The encryption mode to use for CloudWatch data.\n\nKmsKeyArn (string) --The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.\n\n\n\nJobBookmarksEncryption (dict) --The encryption configuration for job bookmarks.\n\nJobBookmarksEncryptionMode (string) --The encryption mode to use for job bookmarks data.\n\nKmsKeyArn (string) --The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string',
    'CreatedTimestamp': datetime(2015, 1, 1)
}


Response Structure

(dict) --

Name (string) --
The name assigned to the new security configuration.

CreatedTimestamp (datetime) --
The time at which the new security configuration was created.







Exceptions

Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ResourceNumberLimitExceededException


    :return: {
        'Name': 'string',
        'CreatedTimestamp': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    Glue.Client.exceptions.AlreadyExistsException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.ResourceNumberLimitExceededException
    
    """
    pass

def create_table(CatalogId=None, DatabaseName=None, TableInput=None):
    """
    Creates a new table definition in the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_table(
        CatalogId='string',
        DatabaseName='string',
        TableInput={
            'Name': 'string',
            'Description': 'string',
            'Owner': 'string',
            'LastAccessTime': datetime(2015, 1, 1),
            'LastAnalyzedTime': datetime(2015, 1, 1),
            'Retention': 123,
            'StorageDescriptor': {
                'Columns': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'Location': 'string',
                'InputFormat': 'string',
                'OutputFormat': 'string',
                'Compressed': True|False,
                'NumberOfBuckets': 123,
                'SerdeInfo': {
                    'Name': 'string',
                    'SerializationLibrary': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
                'BucketColumns': [
                    'string',
                ],
                'SortColumns': [
                    {
                        'Column': 'string',
                        'SortOrder': 123
                    },
                ],
                'Parameters': {
                    'string': 'string'
                },
                'SkewedInfo': {
                    'SkewedColumnNames': [
                        'string',
                    ],
                    'SkewedColumnValues': [
                        'string',
                    ],
                    'SkewedColumnValueLocationMaps': {
                        'string': 'string'
                    }
                },
                'StoredAsSubDirectories': True|False
            },
            'PartitionKeys': [
                {
                    'Name': 'string',
                    'Type': 'string',
                    'Comment': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
            ],
            'ViewOriginalText': 'string',
            'ViewExpandedText': 'string',
            'TableType': 'string',
            'Parameters': {
                'string': 'string'
            }
        }
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which to create the Table . If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe catalog database in which to create the new table. For Hive compatibility, this name is entirely lowercase.\n

    :type TableInput: dict
    :param TableInput: [REQUIRED]\nThe TableInput object that defines the metadata table to create in the catalog.\n\nName (string) -- [REQUIRED]The table name. For Hive compatibility, this is folded to lowercase when it is stored.\n\nDescription (string) --A description of the table.\n\nOwner (string) --The table owner.\n\nLastAccessTime (datetime) --The last time that the table was accessed.\n\nLastAnalyzedTime (datetime) --The last time that column statistics were computed for this table.\n\nRetention (integer) --The retention time for this table.\n\nStorageDescriptor (dict) --A storage descriptor containing information about the physical storage of this table.\n\nColumns (list) --A list of the Columns in the table.\n\n(dict) --A column in a Table .\n\nName (string) -- [REQUIRED]The name of the Column .\n\nType (string) --The data type of the Column .\n\nComment (string) --A free-form text comment.\n\nParameters (dict) --These key-value pairs define properties associated with the column.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\nLocation (string) --The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.\n\nInputFormat (string) --The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.\n\nOutputFormat (string) --The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.\n\nCompressed (boolean) --\nTrue if the data in the table is compressed, or False if not.\n\nNumberOfBuckets (integer) --Must be specified if the table contains any dimension columns.\n\nSerdeInfo (dict) --The serialization/deserialization (SerDe) information.\n\nName (string) --Name of the SerDe.\n\nSerializationLibrary (string) --Usually the class that implements the SerDe. An example is org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .\n\nParameters (dict) --These key-value pairs define initialization parameters for the SerDe.\n\n(string) --\n(string) --\n\n\n\n\n\n\nBucketColumns (list) --A list of reducer grouping columns, clustering columns, and bucketing columns in the table.\n\n(string) --\n\n\nSortColumns (list) --A list specifying the sort order of each bucket in the table.\n\n(dict) --Specifies the sort order of a sorted column.\n\nColumn (string) -- [REQUIRED]The name of the column.\n\nSortOrder (integer) -- [REQUIRED]Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).\n\n\n\n\n\nParameters (dict) --The user-supplied properties in key-value form.\n\n(string) --\n(string) --\n\n\n\n\nSkewedInfo (dict) --The information about values that appear frequently in a column (skewed values).\n\nSkewedColumnNames (list) --A list of names of columns that contain skewed values.\n\n(string) --\n\n\nSkewedColumnValues (list) --A list of values that appear so frequently as to be considered skewed.\n\n(string) --\n\n\nSkewedColumnValueLocationMaps (dict) --A mapping of skewed values to the columns that contain them.\n\n(string) --\n(string) --\n\n\n\n\n\n\nStoredAsSubDirectories (boolean) --\nTrue if the table data is stored in subdirectories, or False if not.\n\n\n\nPartitionKeys (list) --A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.\nWhen you create a table used by Amazon Athena, and you do not specify any partitionKeys , you must at least set the value of partitionKeys to an empty list. For example:\n\n'PartitionKeys': []\n\n(dict) --A column in a Table .\n\nName (string) -- [REQUIRED]The name of the Column .\n\nType (string) --The data type of the Column .\n\nComment (string) --A free-form text comment.\n\nParameters (dict) --These key-value pairs define properties associated with the column.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\nViewOriginalText (string) --If the table is a view, the original text of the view; otherwise null .\n\nViewExpandedText (string) --If the table is a view, the expanded text of the view; otherwise null .\n\nTableType (string) --The type of this table (EXTERNAL_TABLE , VIRTUAL_VIEW , etc.).\n\nParameters (dict) --These key-value pairs define properties associated with the table.\n\n(string) --\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.GlueEncryptionException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_trigger(Name=None, WorkflowName=None, Type=None, Schedule=None, Predicate=None, Actions=None, Description=None, StartOnCreation=None, Tags=None):
    """
    Creates a new trigger.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_trigger(
        Name='string',
        WorkflowName='string',
        Type='SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
        Schedule='string',
        Predicate={
            'Logical': 'AND'|'ANY',
            'Conditions': [
                {
                    'LogicalOperator': 'EQUALS',
                    'JobName': 'string',
                    'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                    'CrawlerName': 'string',
                    'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                },
            ]
        },
        Actions=[
            {
                'JobName': 'string',
                'Arguments': {
                    'string': 'string'
                },
                'Timeout': 123,
                'SecurityConfiguration': 'string',
                'NotificationProperty': {
                    'NotifyDelayAfter': 123
                },
                'CrawlerName': 'string'
            },
        ],
        Description='string',
        StartOnCreation=True|False,
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the trigger.\n

    :type WorkflowName: string
    :param WorkflowName: The name of the workflow associated with the trigger.

    :type Type: string
    :param Type: [REQUIRED]\nThe type of the new trigger.\n

    :type Schedule: string
    :param Schedule: A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .\nThis field is required when the trigger type is SCHEDULED.\n

    :type Predicate: dict
    :param Predicate: A predicate to specify when the new trigger should fire.\nThis field is required when the trigger type is CONDITIONAL .\n\nLogical (string) --An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.\n\nConditions (list) --A list of the conditions that determine when the trigger will fire.\n\n(dict) --Defines a condition under which a trigger fires.\n\nLogicalOperator (string) --A logical operator.\n\nJobName (string) --The name of the job whose JobRuns this condition applies to, and on which this trigger waits.\n\nState (string) --The condition state. Currently, the only job states that a trigger can listen for are SUCCEEDED , STOPPED , FAILED , and TIMEOUT . The only crawler states that a trigger can listen for are SUCCEEDED , FAILED , and CANCELLED .\n\nCrawlerName (string) --The name of the crawler to which this condition applies.\n\nCrawlState (string) --The state of the crawler to which this condition applies.\n\n\n\n\n\n\n

    :type Actions: list
    :param Actions: [REQUIRED]\nThe actions initiated by this trigger when it fires.\n\n(dict) --Defines an action to be initiated by a trigger.\n\nJobName (string) --The name of a job to be executed.\n\nArguments (dict) --The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.\nYou can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.\nFor information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.\nFor information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.\n\n(string) --\n(string) --\n\n\n\n\nTimeout (integer) --The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.\n\nSecurityConfiguration (string) --The name of the SecurityConfiguration structure to be used with this action.\n\nNotificationProperty (dict) --Specifies configuration properties of a job run notification.\n\nNotifyDelayAfter (integer) --After a job run starts, the number of minutes to wait before sending a job run delay notification.\n\n\n\nCrawlerName (string) --The name of the crawler to be used with this action.\n\n\n\n\n

    :type Description: string
    :param Description: A description of the new trigger.

    :type StartOnCreation: boolean
    :param StartOnCreation: Set to true to start SCHEDULED and CONDITIONAL triggers when created. True is not supported for ON_DEMAND triggers.

    :type Tags: dict
    :param Tags: The tags to use with this trigger. You may use tags to limit access to the trigger. For more information about tags in AWS Glue, see AWS Tags in AWS Glue in the developer guide.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string'
}


Response Structure

(dict) --

Name (string) --
The name of the trigger.







Exceptions

Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.IdempotentParameterMismatchException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.ConcurrentModificationException


    :return: {
        'Name': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.AlreadyExistsException
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.IdempotentParameterMismatchException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.ResourceNumberLimitExceededException
    Glue.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def create_user_defined_function(CatalogId=None, DatabaseName=None, FunctionInput=None):
    """
    Creates a new function definition in the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_user_defined_function(
        CatalogId='string',
        DatabaseName='string',
        FunctionInput={
            'FunctionName': 'string',
            'ClassName': 'string',
            'OwnerName': 'string',
            'OwnerType': 'USER'|'ROLE'|'GROUP',
            'ResourceUris': [
                {
                    'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                    'Uri': 'string'
                },
            ]
        }
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which to create the function. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the catalog database in which to create the function.\n

    :type FunctionInput: dict
    :param FunctionInput: [REQUIRED]\nA FunctionInput object that defines the function to create in the Data Catalog.\n\nFunctionName (string) --The name of the function.\n\nClassName (string) --The Java class that contains the function code.\n\nOwnerName (string) --The owner of the function.\n\nOwnerType (string) --The owner type.\n\nResourceUris (list) --The resource URIs for the function.\n\n(dict) --The URIs for function resources.\n\nResourceType (string) --The type of the resource.\n\nUri (string) --The URI for accessing the resource.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.GlueEncryptionException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_workflow(Name=None, Description=None, DefaultRunProperties=None, Tags=None):
    """
    Creates a new workflow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_workflow(
        Name='string',
        Description='string',
        DefaultRunProperties={
            'string': 'string'
        },
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name to be assigned to the workflow. It should be unique within your account.\n

    :type Description: string
    :param Description: A description of the workflow.

    :type DefaultRunProperties: dict
    :param DefaultRunProperties: A collection of properties to be used as part of each execution of the workflow.\n\n(string) --\n(string) --\n\n\n\n

    :type Tags: dict
    :param Tags: The tags to be used with this workflow.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string'
}


Response Structure

(dict) --

Name (string) --
The name of the workflow which was provided as part of the request.







Exceptions

Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.ConcurrentModificationException


    :return: {
        'Name': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.AlreadyExistsException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.ResourceNumberLimitExceededException
    Glue.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def delete_classifier(Name=None):
    """
    Removes a classifier from the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_classifier(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the classifier to remove.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def delete_connection(CatalogId=None, ConnectionName=None):
    """
    Deletes a connection from the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_connection(
        CatalogId='string',
        ConnectionName='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the connection resides. If none is provided, the AWS account ID is used by default.

    :type ConnectionName: string
    :param ConnectionName: [REQUIRED]\nThe name of the connection to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_crawler(Name=None):
    """
    Removes a specified crawler from the AWS Glue Data Catalog, unless the crawler state is RUNNING .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_crawler(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the crawler to remove.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.CrawlerRunningException
Glue.Client.exceptions.SchedulerTransitioningException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.CrawlerRunningException
    Glue.Client.exceptions.SchedulerTransitioningException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def delete_database(CatalogId=None, Name=None):
    """
    Removes a specified database from a Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_database(
        CatalogId='string',
        Name='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the database resides. If none is provided, the AWS account ID is used by default.

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the database to delete. For Hive compatibility, this must be all lowercase.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_dev_endpoint(EndpointName=None):
    """
    Deletes a specified development endpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_dev_endpoint(
        EndpointName='string'
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]\nThe name of the DevEndpoint .\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException


    :return: {}
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.InvalidInputException
    
    """
    pass

def delete_job(JobName=None):
    """
    Deletes a specified job definition. If the job definition is not found, no exception is thrown.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_job(
        JobName='string'
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]\nThe name of the job definition to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'JobName': 'string'
}


Response Structure

(dict) --
JobName (string) --The name of the job definition that was deleted.






Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'JobName': 'string'
    }
    
    
    """
    pass

def delete_ml_transform(TransformId=None):
    """
    Deletes an AWS Glue machine learning transform. Machine learning transforms are a special type of transform that use machine learning to learn the details of the transformation to be performed by learning from examples provided by humans. These transformations are then saved by AWS Glue. If you no longer need a transform, you can delete it by calling DeleteMLTransforms . However, any AWS Glue jobs that still reference the deleted transform will no longer succeed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_ml_transform(
        TransformId='string'
    )
    
    
    :type TransformId: string
    :param TransformId: [REQUIRED]\nThe unique identifier of the transform to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TransformId': 'string'
}


Response Structure

(dict) --
TransformId (string) --The unique identifier of the transform that was deleted.






Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException


    :return: {
        'TransformId': 'string'
    }
    
    
    """
    pass

def delete_partition(CatalogId=None, DatabaseName=None, TableName=None, PartitionValues=None):
    """
    Deletes a specified partition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_partition(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        PartitionValues=[
            'string',
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the partition to be deleted resides. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the catalog database in which the table in question resides.\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table that contains the partition to be deleted.\n

    :type PartitionValues: list
    :param PartitionValues: [REQUIRED]\nThe values that define the partition.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_resource_policy(PolicyHashCondition=None):
    """
    Deletes a specified policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_resource_policy(
        PolicyHashCondition='string'
    )
    
    
    :type PolicyHashCondition: string
    :param PolicyHashCondition: The hash value returned when this policy was set.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.ConditionCheckFailureException


    :return: {}
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.ConditionCheckFailureException
    
    """
    pass

def delete_security_configuration(Name=None):
    """
    Deletes a specified security configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_security_configuration(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the security configuration to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def delete_table(CatalogId=None, DatabaseName=None, Name=None):
    """
    Removes a table definition from the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_table(
        CatalogId='string',
        DatabaseName='string',
        Name='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the table resides. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the catalog database in which the table resides. For Hive compatibility, this name is entirely lowercase.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the table to be deleted. For Hive compatibility, this name is entirely lowercase.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_table_version(CatalogId=None, DatabaseName=None, TableName=None, VersionId=None):
    """
    Deletes a specified version of a table.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_table_version(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        VersionId='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the tables reside. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table. For Hive compatibility, this name is entirely lowercase.\n

    :type VersionId: string
    :param VersionId: [REQUIRED]\nThe ID of the table version to be deleted. A VersionID is a string representation of an integer. Each version is incremented by 1.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_trigger(Name=None):
    """
    Deletes a specified trigger. If the trigger is not found, no exception is thrown.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_trigger(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the trigger to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Name': 'string'
}


Response Structure

(dict) --
Name (string) --The name of the trigger that was deleted.






Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ConcurrentModificationException


    :return: {
        'Name': 'string'
    }
    
    
    """
    pass

def delete_user_defined_function(CatalogId=None, DatabaseName=None, FunctionName=None):
    """
    Deletes an existing function definition from the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user_defined_function(
        CatalogId='string',
        DatabaseName='string',
        FunctionName='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the function to be deleted is located. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the catalog database where the function is located.\n

    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the function definition to be deleted.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_workflow(Name=None):
    """
    Deletes a workflow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_workflow(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the workflow to be deleted.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Name': 'string'
}


Response Structure

(dict) --
Name (string) --Name of the workflow specified in input.






Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ConcurrentModificationException


    :return: {
        'Name': 'string'
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

def get_catalog_import_status(CatalogId=None):
    """
    Retrieves the status of a migration operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_catalog_import_status(
        CatalogId='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the catalog to migrate. Currently, this should be the AWS account ID.

    :rtype: dict
ReturnsResponse Syntax{
    'ImportStatus': {
        'ImportCompleted': True|False,
        'ImportTime': datetime(2015, 1, 1),
        'ImportedBy': 'string'
    }
}


Response Structure

(dict) --
ImportStatus (dict) --The status of the specified catalog migration.

ImportCompleted (boolean) --
True if the migration has completed, or False otherwise.

ImportTime (datetime) --The time that the migration was started.

ImportedBy (string) --The name of the person who initiated the migration.








Exceptions

Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'ImportStatus': {
            'ImportCompleted': True|False,
            'ImportTime': datetime(2015, 1, 1),
            'ImportedBy': 'string'
        }
    }
    
    
    """
    pass

def get_classifier(Name=None):
    """
    Retrieve a classifier by name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_classifier(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the classifier to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Classifier': {
        'GrokClassifier': {
            'Name': 'string',
            'Classification': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdated': datetime(2015, 1, 1),
            'Version': 123,
            'GrokPattern': 'string',
            'CustomPatterns': 'string'
        },
        'XMLClassifier': {
            'Name': 'string',
            'Classification': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdated': datetime(2015, 1, 1),
            'Version': 123,
            'RowTag': 'string'
        },
        'JsonClassifier': {
            'Name': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdated': datetime(2015, 1, 1),
            'Version': 123,
            'JsonPath': 'string'
        },
        'CsvClassifier': {
            'Name': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdated': datetime(2015, 1, 1),
            'Version': 123,
            'Delimiter': 'string',
            'QuoteSymbol': 'string',
            'ContainsHeader': 'UNKNOWN'|'PRESENT'|'ABSENT',
            'Header': [
                'string',
            ],
            'DisableValueTrimming': True|False,
            'AllowSingleColumn': True|False
        }
    }
}


Response Structure

(dict) --
Classifier (dict) --The requested classifier.

GrokClassifier (dict) --A classifier that uses grok .

Name (string) --The name of the classifier.

Classification (string) --An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, and so on.

CreationTime (datetime) --The time that this classifier was registered.

LastUpdated (datetime) --The time that this classifier was last updated.

Version (integer) --The version of this classifier.

GrokPattern (string) --The grok pattern applied to a data store by this classifier. For more information, see built-in patterns in Writing Custom Classifiers .

CustomPatterns (string) --Optional custom grok patterns defined by this classifier. For more information, see custom patterns in Writing Custom Classifiers .



XMLClassifier (dict) --A classifier for XML content.

Name (string) --The name of the classifier.

Classification (string) --An identifier of the data format that the classifier matches.

CreationTime (datetime) --The time that this classifier was registered.

LastUpdated (datetime) --The time that this classifier was last updated.

Version (integer) --The version of this classifier.

RowTag (string) --The XML tag designating the element that contains each record in an XML document being parsed. This can\'t identify a self-closing element (closed by /> ). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, <row item_a="A" item_b="B"></row> is okay, but <row item_a="A" item_b="B" /> is not).



JsonClassifier (dict) --A classifier for JSON content.

Name (string) --The name of the classifier.

CreationTime (datetime) --The time that this classifier was registered.

LastUpdated (datetime) --The time that this classifier was last updated.

Version (integer) --The version of this classifier.

JsonPath (string) --A JsonPath string defining the JSON data for the classifier to classify. AWS Glue supports a subset of JsonPath , as described in Writing JsonPath Custom Classifiers .



CsvClassifier (dict) --A classifier for comma-separated values (CSV).

Name (string) --The name of the classifier.

CreationTime (datetime) --The time that this classifier was registered.

LastUpdated (datetime) --The time that this classifier was last updated.

Version (integer) --The version of this classifier.

Delimiter (string) --A custom symbol to denote what separates each column entry in the row.

QuoteSymbol (string) --A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.

ContainsHeader (string) --Indicates whether the CSV file contains a header.

Header (list) --A list of strings representing column names.

(string) --


DisableValueTrimming (boolean) --Specifies not to trim values before identifying the type of column values. The default value is true .

AllowSingleColumn (boolean) --Enables the processing of files that contain only one column.










Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Classifier': {
            'GrokClassifier': {
                'Name': 'string',
                'Classification': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdated': datetime(2015, 1, 1),
                'Version': 123,
                'GrokPattern': 'string',
                'CustomPatterns': 'string'
            },
            'XMLClassifier': {
                'Name': 'string',
                'Classification': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdated': datetime(2015, 1, 1),
                'Version': 123,
                'RowTag': 'string'
            },
            'JsonClassifier': {
                'Name': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdated': datetime(2015, 1, 1),
                'Version': 123,
                'JsonPath': 'string'
            },
            'CsvClassifier': {
                'Name': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdated': datetime(2015, 1, 1),
                'Version': 123,
                'Delimiter': 'string',
                'QuoteSymbol': 'string',
                'ContainsHeader': 'UNKNOWN'|'PRESENT'|'ABSENT',
                'Header': [
                    'string',
                ],
                'DisableValueTrimming': True|False,
                'AllowSingleColumn': True|False
            }
        }
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def get_classifiers(MaxResults=None, NextToken=None):
    """
    Lists all classifier objects in the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_classifiers(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The size of the list to return (optional).

    :type NextToken: string
    :param NextToken: An optional continuation token.

    :rtype: dict

ReturnsResponse Syntax
{
    'Classifiers': [
        {
            'GrokClassifier': {
                'Name': 'string',
                'Classification': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdated': datetime(2015, 1, 1),
                'Version': 123,
                'GrokPattern': 'string',
                'CustomPatterns': 'string'
            },
            'XMLClassifier': {
                'Name': 'string',
                'Classification': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdated': datetime(2015, 1, 1),
                'Version': 123,
                'RowTag': 'string'
            },
            'JsonClassifier': {
                'Name': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdated': datetime(2015, 1, 1),
                'Version': 123,
                'JsonPath': 'string'
            },
            'CsvClassifier': {
                'Name': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdated': datetime(2015, 1, 1),
                'Version': 123,
                'Delimiter': 'string',
                'QuoteSymbol': 'string',
                'ContainsHeader': 'UNKNOWN'|'PRESENT'|'ABSENT',
                'Header': [
                    'string',
                ],
                'DisableValueTrimming': True|False,
                'AllowSingleColumn': True|False
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Classifiers (list) --
The requested list of classifier objects.

(dict) --
Classifiers are triggered during a crawl task. A classifier checks whether a given file is in a format it can handle. If it is, the classifier creates a schema in the form of a StructType object that matches that data format.
You can use the standard classifiers that AWS Glue provides, or you can write your own classifiers to best categorize your data sources and specify the appropriate schemas to use for them. A classifier can be a grok classifier, an XML classifier, a JSON classifier, or a custom CSV classifier, as specified in one of the fields in the Classifier object.

GrokClassifier (dict) --
A classifier that uses grok .

Name (string) --
The name of the classifier.

Classification (string) --
An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, and so on.

CreationTime (datetime) --
The time that this classifier was registered.

LastUpdated (datetime) --
The time that this classifier was last updated.

Version (integer) --
The version of this classifier.

GrokPattern (string) --
The grok pattern applied to a data store by this classifier. For more information, see built-in patterns in Writing Custom Classifiers .

CustomPatterns (string) --
Optional custom grok patterns defined by this classifier. For more information, see custom patterns in Writing Custom Classifiers .



XMLClassifier (dict) --
A classifier for XML content.

Name (string) --
The name of the classifier.

Classification (string) --
An identifier of the data format that the classifier matches.

CreationTime (datetime) --
The time that this classifier was registered.

LastUpdated (datetime) --
The time that this classifier was last updated.

Version (integer) --
The version of this classifier.

RowTag (string) --
The XML tag designating the element that contains each record in an XML document being parsed. This can\'t identify a self-closing element (closed by /> ). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, <row item_a="A" item_b="B"></row> is okay, but <row item_a="A" item_b="B" /> is not).



JsonClassifier (dict) --
A classifier for JSON content.

Name (string) --
The name of the classifier.

CreationTime (datetime) --
The time that this classifier was registered.

LastUpdated (datetime) --
The time that this classifier was last updated.

Version (integer) --
The version of this classifier.

JsonPath (string) --
A JsonPath string defining the JSON data for the classifier to classify. AWS Glue supports a subset of JsonPath , as described in Writing JsonPath Custom Classifiers .



CsvClassifier (dict) --
A classifier for comma-separated values (CSV).

Name (string) --
The name of the classifier.

CreationTime (datetime) --
The time that this classifier was registered.

LastUpdated (datetime) --
The time that this classifier was last updated.

Version (integer) --
The version of this classifier.

Delimiter (string) --
A custom symbol to denote what separates each column entry in the row.

QuoteSymbol (string) --
A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.

ContainsHeader (string) --
Indicates whether the CSV file contains a header.

Header (list) --
A list of strings representing column names.

(string) --


DisableValueTrimming (boolean) --
Specifies not to trim values before identifying the type of column values. The default value is true .

AllowSingleColumn (boolean) --
Enables the processing of files that contain only one column.







NextToken (string) --
A continuation token.







Exceptions

Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Classifiers': [
            {
                'GrokClassifier': {
                    'Name': 'string',
                    'Classification': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'LastUpdated': datetime(2015, 1, 1),
                    'Version': 123,
                    'GrokPattern': 'string',
                    'CustomPatterns': 'string'
                },
                'XMLClassifier': {
                    'Name': 'string',
                    'Classification': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'LastUpdated': datetime(2015, 1, 1),
                    'Version': 123,
                    'RowTag': 'string'
                },
                'JsonClassifier': {
                    'Name': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'LastUpdated': datetime(2015, 1, 1),
                    'Version': 123,
                    'JsonPath': 'string'
                },
                'CsvClassifier': {
                    'Name': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'LastUpdated': datetime(2015, 1, 1),
                    'Version': 123,
                    'Delimiter': 'string',
                    'QuoteSymbol': 'string',
                    'ContainsHeader': 'UNKNOWN'|'PRESENT'|'ABSENT',
                    'Header': [
                        'string',
                    ],
                    'DisableValueTrimming': True|False,
                    'AllowSingleColumn': True|False
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_connection(CatalogId=None, Name=None, HidePassword=None):
    """
    Retrieves a connection definition from the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_connection(
        CatalogId='string',
        Name='string',
        HidePassword=True|False
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the connection resides. If none is provided, the AWS account ID is used by default.

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the connection definition to retrieve.\n

    :type HidePassword: boolean
    :param HidePassword: Allows you to retrieve the connection metadata without returning the password. For instance, the AWS Glue console uses this flag to retrieve the connection, and does not display the password. Set this parameter when the caller might not have permission to use the AWS KMS key to decrypt the password, but it does have permission to access the rest of the connection properties.

    :rtype: dict

ReturnsResponse Syntax
{
    'Connection': {
        'Name': 'string',
        'Description': 'string',
        'ConnectionType': 'JDBC'|'SFTP'|'MONGODB'|'KAFKA',
        'MatchCriteria': [
            'string',
        ],
        'ConnectionProperties': {
            'string': 'string'
        },
        'PhysicalConnectionRequirements': {
            'SubnetId': 'string',
            'SecurityGroupIdList': [
                'string',
            ],
            'AvailabilityZone': 'string'
        },
        'CreationTime': datetime(2015, 1, 1),
        'LastUpdatedTime': datetime(2015, 1, 1),
        'LastUpdatedBy': 'string'
    }
}


Response Structure

(dict) --

Connection (dict) --
The requested connection definition.

Name (string) --
The name of the connection definition.

Description (string) --
The description of the connection.

ConnectionType (string) --
The type of the connection. Currently, only JDBC is supported; SFTP is not supported.

MatchCriteria (list) --
A list of criteria that can be used in selecting this connection.

(string) --


ConnectionProperties (dict) --
These key-value pairs define parameters for the connection:

HOST - The host URI: either the fully qualified domain name (FQDN) or the IPv4 address of the database host.
PORT - The port number, between 1024 and 65535, of the port on which the database host is listening for database connections.
USER_NAME - The name under which to log in to the database. The value string for USER_NAME is "USERNAME ".
PASSWORD - A password, if one is used, for the user name.
ENCRYPTED_PASSWORD - When you enable connection password protection by setting ConnectionPasswordEncryption in the Data Catalog encryption settings, this field stores the encrypted password.
JDBC_DRIVER_JAR_URI - The Amazon Simple Storage Service (Amazon S3) path of the JAR file that contains the JDBC driver to use.
JDBC_DRIVER_CLASS_NAME - The class name of the JDBC driver to use.
JDBC_ENGINE - The name of the JDBC engine to use.
JDBC_ENGINE_VERSION - The version of the JDBC engine to use.
CONFIG_FILES - (Reserved for future use.)
INSTANCE_ID - The instance ID to use.
JDBC_CONNECTION_URL - The URL for connecting to a JDBC data source.
JDBC_ENFORCE_SSL - A Boolean string (true, false) specifying whether Secure Sockets Layer (SSL) with hostname matching is enforced for the JDBC connection on the client. The default is false.
CUSTOM_JDBC_CERT - An Amazon S3 location specifying the customer\'s root certificate. AWS Glue uses this root certificate to validate the customer\xe2\x80\x99s certificate when connecting to the customer database. AWS Glue only handles X.509 certificates. The certificate provided must be DER-encoded and supplied in Base64 encoding PEM format.
SKIP_CUSTOM_JDBC_CERT_VALIDATION - By default, this is false . AWS Glue validates the Signature algorithm and Subject Public Key Algorithm for the customer certificate. The only permitted algorithms for the Signature algorithm are SHA256withRSA, SHA384withRSA or SHA512withRSA. For the Subject Public Key Algorithm, the key length must be at least 2048. You can set the value of this property to true to skip AWS Glue\xe2\x80\x99s validation of the customer certificate.
CUSTOM_JDBC_CERT_STRING - A custom JDBC certificate string which is used for domain match or distinguished name match to prevent a man-in-the-middle attack. In Oracle database, this is used as the SSL_SERVER_CERT_DN ; in Microsoft SQL Server, this is used as the hostNameInCertificate .
CONNECTION_URL - The URL for connecting to a general (non-JDBC) data source.
KAFKA_BOOTSTRAP_SERVERS - A comma-separated list of host and port pairs that are the addresses of the Apache Kafka brokers in a Kafka cluster to which a Kafka client will connect to and bootstrap itself.


(string) --
(string) --




PhysicalConnectionRequirements (dict) --
A map of physical connection requirements, such as virtual private cloud (VPC) and SecurityGroup , that are needed to make this connection successfully.

SubnetId (string) --
The subnet ID used by the connection.

SecurityGroupIdList (list) --
The security group ID list used by the connection.

(string) --


AvailabilityZone (string) --
The connection\'s Availability Zone. This field is redundant because the specified subnet implies the Availability Zone to be used. Currently the field must be populated, but it will be deprecated in the future.



CreationTime (datetime) --
The time that this connection definition was created.

LastUpdatedTime (datetime) --
The last time that this connection definition was updated.

LastUpdatedBy (string) --
The user, group, or role that last updated this connection definition.









Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.GlueEncryptionException


    :return: {
        'Connection': {
            'Name': 'string',
            'Description': 'string',
            'ConnectionType': 'JDBC'|'SFTP'|'MONGODB'|'KAFKA',
            'MatchCriteria': [
                'string',
            ],
            'ConnectionProperties': {
                'string': 'string'
            },
            'PhysicalConnectionRequirements': {
                'SubnetId': 'string',
                'SecurityGroupIdList': [
                    'string',
                ],
                'AvailabilityZone': 'string'
            },
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1),
            'LastUpdatedBy': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_connections(CatalogId=None, Filter=None, HidePassword=None, NextToken=None, MaxResults=None):
    """
    Retrieves a list of connection definitions from the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_connections(
        CatalogId='string',
        Filter={
            'MatchCriteria': [
                'string',
            ],
            'ConnectionType': 'JDBC'|'SFTP'|'MONGODB'|'KAFKA'
        },
        HidePassword=True|False,
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the connections reside. If none is provided, the AWS account ID is used by default.

    :type Filter: dict
    :param Filter: A filter that controls which connections are returned.\n\nMatchCriteria (list) --A criteria string that must match the criteria recorded in the connection definition for that connection definition to be returned.\n\n(string) --\n\n\nConnectionType (string) --The type of connections to return. Currently, only JDBC is supported; SFTP is not supported.\n\n\n

    :type HidePassword: boolean
    :param HidePassword: Allows you to retrieve the connection metadata without returning the password. For instance, the AWS Glue console uses this flag to retrieve the connection, and does not display the password. Set this parameter when the caller might not have permission to use the AWS KMS key to decrypt the password, but it does have permission to access the rest of the connection properties.

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of connections to return in one response.

    :rtype: dict

ReturnsResponse Syntax
{
    'ConnectionList': [
        {
            'Name': 'string',
            'Description': 'string',
            'ConnectionType': 'JDBC'|'SFTP'|'MONGODB'|'KAFKA',
            'MatchCriteria': [
                'string',
            ],
            'ConnectionProperties': {
                'string': 'string'
            },
            'PhysicalConnectionRequirements': {
                'SubnetId': 'string',
                'SecurityGroupIdList': [
                    'string',
                ],
                'AvailabilityZone': 'string'
            },
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1),
            'LastUpdatedBy': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ConnectionList (list) --
A list of requested connection definitions.

(dict) --
Defines a connection to a data source.

Name (string) --
The name of the connection definition.

Description (string) --
The description of the connection.

ConnectionType (string) --
The type of the connection. Currently, only JDBC is supported; SFTP is not supported.

MatchCriteria (list) --
A list of criteria that can be used in selecting this connection.

(string) --


ConnectionProperties (dict) --
These key-value pairs define parameters for the connection:

HOST - The host URI: either the fully qualified domain name (FQDN) or the IPv4 address of the database host.
PORT - The port number, between 1024 and 65535, of the port on which the database host is listening for database connections.
USER_NAME - The name under which to log in to the database. The value string for USER_NAME is "USERNAME ".
PASSWORD - A password, if one is used, for the user name.
ENCRYPTED_PASSWORD - When you enable connection password protection by setting ConnectionPasswordEncryption in the Data Catalog encryption settings, this field stores the encrypted password.
JDBC_DRIVER_JAR_URI - The Amazon Simple Storage Service (Amazon S3) path of the JAR file that contains the JDBC driver to use.
JDBC_DRIVER_CLASS_NAME - The class name of the JDBC driver to use.
JDBC_ENGINE - The name of the JDBC engine to use.
JDBC_ENGINE_VERSION - The version of the JDBC engine to use.
CONFIG_FILES - (Reserved for future use.)
INSTANCE_ID - The instance ID to use.
JDBC_CONNECTION_URL - The URL for connecting to a JDBC data source.
JDBC_ENFORCE_SSL - A Boolean string (true, false) specifying whether Secure Sockets Layer (SSL) with hostname matching is enforced for the JDBC connection on the client. The default is false.
CUSTOM_JDBC_CERT - An Amazon S3 location specifying the customer\'s root certificate. AWS Glue uses this root certificate to validate the customer\xe2\x80\x99s certificate when connecting to the customer database. AWS Glue only handles X.509 certificates. The certificate provided must be DER-encoded and supplied in Base64 encoding PEM format.
SKIP_CUSTOM_JDBC_CERT_VALIDATION - By default, this is false . AWS Glue validates the Signature algorithm and Subject Public Key Algorithm for the customer certificate. The only permitted algorithms for the Signature algorithm are SHA256withRSA, SHA384withRSA or SHA512withRSA. For the Subject Public Key Algorithm, the key length must be at least 2048. You can set the value of this property to true to skip AWS Glue\xe2\x80\x99s validation of the customer certificate.
CUSTOM_JDBC_CERT_STRING - A custom JDBC certificate string which is used for domain match or distinguished name match to prevent a man-in-the-middle attack. In Oracle database, this is used as the SSL_SERVER_CERT_DN ; in Microsoft SQL Server, this is used as the hostNameInCertificate .
CONNECTION_URL - The URL for connecting to a general (non-JDBC) data source.
KAFKA_BOOTSTRAP_SERVERS - A comma-separated list of host and port pairs that are the addresses of the Apache Kafka brokers in a Kafka cluster to which a Kafka client will connect to and bootstrap itself.


(string) --
(string) --




PhysicalConnectionRequirements (dict) --
A map of physical connection requirements, such as virtual private cloud (VPC) and SecurityGroup , that are needed to make this connection successfully.

SubnetId (string) --
The subnet ID used by the connection.

SecurityGroupIdList (list) --
The security group ID list used by the connection.

(string) --


AvailabilityZone (string) --
The connection\'s Availability Zone. This field is redundant because the specified subnet implies the Availability Zone to be used. Currently the field must be populated, but it will be deprecated in the future.



CreationTime (datetime) --
The time that this connection definition was created.

LastUpdatedTime (datetime) --
The last time that this connection definition was updated.

LastUpdatedBy (string) --
The user, group, or role that last updated this connection definition.





NextToken (string) --
A continuation token, if the list of connections returned does not include the last of the filtered connections.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.GlueEncryptionException


    :return: {
        'ConnectionList': [
            {
                'Name': 'string',
                'Description': 'string',
                'ConnectionType': 'JDBC'|'SFTP'|'MONGODB'|'KAFKA',
                'MatchCriteria': [
                    'string',
                ],
                'ConnectionProperties': {
                    'string': 'string'
                },
                'PhysicalConnectionRequirements': {
                    'SubnetId': 'string',
                    'SecurityGroupIdList': [
                        'string',
                    ],
                    'AvailabilityZone': 'string'
                },
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1),
                'LastUpdatedBy': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_crawler(Name=None):
    """
    Retrieves metadata for a specified crawler.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_crawler(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the crawler to retrieve metadata for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Crawler': {
        'Name': 'string',
        'Role': 'string',
        'Targets': {
            'S3Targets': [
                {
                    'Path': 'string',
                    'Exclusions': [
                        'string',
                    ]
                },
            ],
            'JdbcTargets': [
                {
                    'ConnectionName': 'string',
                    'Path': 'string',
                    'Exclusions': [
                        'string',
                    ]
                },
            ],
            'DynamoDBTargets': [
                {
                    'Path': 'string'
                },
            ],
            'CatalogTargets': [
                {
                    'DatabaseName': 'string',
                    'Tables': [
                        'string',
                    ]
                },
            ]
        },
        'DatabaseName': 'string',
        'Description': 'string',
        'Classifiers': [
            'string',
        ],
        'SchemaChangePolicy': {
            'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
            'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
        },
        'State': 'READY'|'RUNNING'|'STOPPING',
        'TablePrefix': 'string',
        'Schedule': {
            'ScheduleExpression': 'string',
            'State': 'SCHEDULED'|'NOT_SCHEDULED'|'TRANSITIONING'
        },
        'CrawlElapsedTime': 123,
        'CreationTime': datetime(2015, 1, 1),
        'LastUpdated': datetime(2015, 1, 1),
        'LastCrawl': {
            'Status': 'SUCCEEDED'|'CANCELLED'|'FAILED',
            'ErrorMessage': 'string',
            'LogGroup': 'string',
            'LogStream': 'string',
            'MessagePrefix': 'string',
            'StartTime': datetime(2015, 1, 1)
        },
        'Version': 123,
        'Configuration': 'string',
        'CrawlerSecurityConfiguration': 'string'
    }
}


Response Structure

(dict) --
Crawler (dict) --The metadata for the specified crawler.

Name (string) --The name of the crawler.

Role (string) --The Amazon Resource Name (ARN) of an IAM role that\'s used to access customer resources, such as Amazon Simple Storage Service (Amazon S3) data.

Targets (dict) --A collection of targets to crawl.

S3Targets (list) --Specifies Amazon Simple Storage Service (Amazon S3) targets.

(dict) --Specifies a data store in Amazon Simple Storage Service (Amazon S3).

Path (string) --The path to the Amazon S3 target.

Exclusions (list) --A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler .

(string) --






JdbcTargets (list) --Specifies JDBC targets.

(dict) --Specifies a JDBC data store to crawl.

ConnectionName (string) --The name of the connection to use to connect to the JDBC target.

Path (string) --The path of the JDBC target.

Exclusions (list) --A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler .

(string) --






DynamoDBTargets (list) --Specifies Amazon DynamoDB targets.

(dict) --Specifies an Amazon DynamoDB table to crawl.

Path (string) --The name of the DynamoDB table to crawl.





CatalogTargets (list) --Specifies AWS Glue Data Catalog targets.

(dict) --Specifies an AWS Glue Data Catalog target.

DatabaseName (string) --The name of the database to be synchronized.

Tables (list) --A list of the tables to be synchronized.

(string) --








DatabaseName (string) --The name of the database in which the crawler\'s output is stored.

Description (string) --A description of the crawler.

Classifiers (list) --A list of UTF-8 strings that specify the custom classifiers that are associated with the crawler.

(string) --


SchemaChangePolicy (dict) --The policy that specifies update and delete behaviors for the crawler.

UpdateBehavior (string) --The update behavior when the crawler finds a changed schema.

DeleteBehavior (string) --The deletion behavior when the crawler finds a deleted object.



State (string) --Indicates whether the crawler is running, or whether a run is pending.

TablePrefix (string) --The prefix added to the names of tables that are created.

Schedule (dict) --For scheduled crawlers, the schedule when the crawler runs.

ScheduleExpression (string) --A cron expression used to specify the schedule. For more information, see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, specify cron(15 12 * * ? *) .

State (string) --The state of the schedule.



CrawlElapsedTime (integer) --If the crawler is running, contains the total time elapsed since the last crawl began.

CreationTime (datetime) --The time that the crawler was created.

LastUpdated (datetime) --The time that the crawler was last updated.

LastCrawl (dict) --The status of the last crawl, and potentially error information if an error occurred.

Status (string) --Status of the last crawl.

ErrorMessage (string) --If an error occurred, the error information about the last crawl.

LogGroup (string) --The log group for the last crawl.

LogStream (string) --The log stream for the last crawl.

MessagePrefix (string) --The prefix for a message about this crawl.

StartTime (datetime) --The time at which the crawl started.



Version (integer) --The version of the crawler.

Configuration (string) --Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler\'s behavior. For more information, see Configuring a Crawler .

CrawlerSecurityConfiguration (string) --The name of the SecurityConfiguration structure to be used by this crawler.








Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Crawler': {
            'Name': 'string',
            'Role': 'string',
            'Targets': {
                'S3Targets': [
                    {
                        'Path': 'string',
                        'Exclusions': [
                            'string',
                        ]
                    },
                ],
                'JdbcTargets': [
                    {
                        'ConnectionName': 'string',
                        'Path': 'string',
                        'Exclusions': [
                            'string',
                        ]
                    },
                ],
                'DynamoDBTargets': [
                    {
                        'Path': 'string'
                    },
                ],
                'CatalogTargets': [
                    {
                        'DatabaseName': 'string',
                        'Tables': [
                            'string',
                        ]
                    },
                ]
            },
            'DatabaseName': 'string',
            'Description': 'string',
            'Classifiers': [
                'string',
            ],
            'SchemaChangePolicy': {
                'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
                'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
            },
            'State': 'READY'|'RUNNING'|'STOPPING',
            'TablePrefix': 'string',
            'Schedule': {
                'ScheduleExpression': 'string',
                'State': 'SCHEDULED'|'NOT_SCHEDULED'|'TRANSITIONING'
            },
            'CrawlElapsedTime': 123,
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdated': datetime(2015, 1, 1),
            'LastCrawl': {
                'Status': 'SUCCEEDED'|'CANCELLED'|'FAILED',
                'ErrorMessage': 'string',
                'LogGroup': 'string',
                'LogStream': 'string',
                'MessagePrefix': 'string',
                'StartTime': datetime(2015, 1, 1)
            },
            'Version': 123,
            'Configuration': 'string',
            'CrawlerSecurityConfiguration': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_crawler_metrics(CrawlerNameList=None, MaxResults=None, NextToken=None):
    """
    Retrieves metrics about specified crawlers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_crawler_metrics(
        CrawlerNameList=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type CrawlerNameList: list
    :param CrawlerNameList: A list of the names of crawlers about which to retrieve metrics.\n\n(string) --\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum size of a list to return.

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :rtype: dict

ReturnsResponse Syntax
{
    'CrawlerMetricsList': [
        {
            'CrawlerName': 'string',
            'TimeLeftSeconds': 123.0,
            'StillEstimating': True|False,
            'LastRuntimeSeconds': 123.0,
            'MedianRuntimeSeconds': 123.0,
            'TablesCreated': 123,
            'TablesUpdated': 123,
            'TablesDeleted': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

CrawlerMetricsList (list) --
A list of metrics for the specified crawler.

(dict) --
Metrics for a specified crawler.

CrawlerName (string) --
The name of the crawler.

TimeLeftSeconds (float) --
The estimated time left to complete a running crawl.

StillEstimating (boolean) --
True if the crawler is still estimating how long it will take to complete this run.

LastRuntimeSeconds (float) --
The duration of the crawler\'s most recent run, in seconds.

MedianRuntimeSeconds (float) --
The median duration of this crawler\'s runs, in seconds.

TablesCreated (integer) --
The number of tables created by this crawler.

TablesUpdated (integer) --
The number of tables updated by this crawler.

TablesDeleted (integer) --
The number of tables deleted by this crawler.





NextToken (string) --
A continuation token, if the returned list does not contain the last metric available.







Exceptions

Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'CrawlerMetricsList': [
            {
                'CrawlerName': 'string',
                'TimeLeftSeconds': 123.0,
                'StillEstimating': True|False,
                'LastRuntimeSeconds': 123.0,
                'MedianRuntimeSeconds': 123.0,
                'TablesCreated': 123,
                'TablesUpdated': 123,
                'TablesDeleted': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def get_crawlers(MaxResults=None, NextToken=None):
    """
    Retrieves metadata for all crawlers defined in the customer account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_crawlers(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The number of crawlers to return on each call.

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation request.

    :rtype: dict

ReturnsResponse Syntax
{
    'Crawlers': [
        {
            'Name': 'string',
            'Role': 'string',
            'Targets': {
                'S3Targets': [
                    {
                        'Path': 'string',
                        'Exclusions': [
                            'string',
                        ]
                    },
                ],
                'JdbcTargets': [
                    {
                        'ConnectionName': 'string',
                        'Path': 'string',
                        'Exclusions': [
                            'string',
                        ]
                    },
                ],
                'DynamoDBTargets': [
                    {
                        'Path': 'string'
                    },
                ],
                'CatalogTargets': [
                    {
                        'DatabaseName': 'string',
                        'Tables': [
                            'string',
                        ]
                    },
                ]
            },
            'DatabaseName': 'string',
            'Description': 'string',
            'Classifiers': [
                'string',
            ],
            'SchemaChangePolicy': {
                'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
                'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
            },
            'State': 'READY'|'RUNNING'|'STOPPING',
            'TablePrefix': 'string',
            'Schedule': {
                'ScheduleExpression': 'string',
                'State': 'SCHEDULED'|'NOT_SCHEDULED'|'TRANSITIONING'
            },
            'CrawlElapsedTime': 123,
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdated': datetime(2015, 1, 1),
            'LastCrawl': {
                'Status': 'SUCCEEDED'|'CANCELLED'|'FAILED',
                'ErrorMessage': 'string',
                'LogGroup': 'string',
                'LogStream': 'string',
                'MessagePrefix': 'string',
                'StartTime': datetime(2015, 1, 1)
            },
            'Version': 123,
            'Configuration': 'string',
            'CrawlerSecurityConfiguration': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Crawlers (list) --
A list of crawler metadata.

(dict) --
Specifies a crawler program that examines a data source and uses classifiers to try to determine its schema. If successful, the crawler records metadata concerning the data source in the AWS Glue Data Catalog.

Name (string) --
The name of the crawler.

Role (string) --
The Amazon Resource Name (ARN) of an IAM role that\'s used to access customer resources, such as Amazon Simple Storage Service (Amazon S3) data.

Targets (dict) --
A collection of targets to crawl.

S3Targets (list) --
Specifies Amazon Simple Storage Service (Amazon S3) targets.

(dict) --
Specifies a data store in Amazon Simple Storage Service (Amazon S3).

Path (string) --
The path to the Amazon S3 target.

Exclusions (list) --
A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler .

(string) --






JdbcTargets (list) --
Specifies JDBC targets.

(dict) --
Specifies a JDBC data store to crawl.

ConnectionName (string) --
The name of the connection to use to connect to the JDBC target.

Path (string) --
The path of the JDBC target.

Exclusions (list) --
A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler .

(string) --






DynamoDBTargets (list) --
Specifies Amazon DynamoDB targets.

(dict) --
Specifies an Amazon DynamoDB table to crawl.

Path (string) --
The name of the DynamoDB table to crawl.





CatalogTargets (list) --
Specifies AWS Glue Data Catalog targets.

(dict) --
Specifies an AWS Glue Data Catalog target.

DatabaseName (string) --
The name of the database to be synchronized.

Tables (list) --
A list of the tables to be synchronized.

(string) --








DatabaseName (string) --
The name of the database in which the crawler\'s output is stored.

Description (string) --
A description of the crawler.

Classifiers (list) --
A list of UTF-8 strings that specify the custom classifiers that are associated with the crawler.

(string) --


SchemaChangePolicy (dict) --
The policy that specifies update and delete behaviors for the crawler.

UpdateBehavior (string) --
The update behavior when the crawler finds a changed schema.

DeleteBehavior (string) --
The deletion behavior when the crawler finds a deleted object.



State (string) --
Indicates whether the crawler is running, or whether a run is pending.

TablePrefix (string) --
The prefix added to the names of tables that are created.

Schedule (dict) --
For scheduled crawlers, the schedule when the crawler runs.

ScheduleExpression (string) --
A cron expression used to specify the schedule. For more information, see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, specify cron(15 12 * * ? *) .

State (string) --
The state of the schedule.



CrawlElapsedTime (integer) --
If the crawler is running, contains the total time elapsed since the last crawl began.

CreationTime (datetime) --
The time that the crawler was created.

LastUpdated (datetime) --
The time that the crawler was last updated.

LastCrawl (dict) --
The status of the last crawl, and potentially error information if an error occurred.

Status (string) --
Status of the last crawl.

ErrorMessage (string) --
If an error occurred, the error information about the last crawl.

LogGroup (string) --
The log group for the last crawl.

LogStream (string) --
The log stream for the last crawl.

MessagePrefix (string) --
The prefix for a message about this crawl.

StartTime (datetime) --
The time at which the crawl started.



Version (integer) --
The version of the crawler.

Configuration (string) --
Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler\'s behavior. For more information, see Configuring a Crawler .

CrawlerSecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used by this crawler.





NextToken (string) --
A continuation token, if the returned list has not reached the end of those defined in this customer account.







Exceptions

Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Crawlers': [
            {
                'Name': 'string',
                'Role': 'string',
                'Targets': {
                    'S3Targets': [
                        {
                            'Path': 'string',
                            'Exclusions': [
                                'string',
                            ]
                        },
                    ],
                    'JdbcTargets': [
                        {
                            'ConnectionName': 'string',
                            'Path': 'string',
                            'Exclusions': [
                                'string',
                            ]
                        },
                    ],
                    'DynamoDBTargets': [
                        {
                            'Path': 'string'
                        },
                    ],
                    'CatalogTargets': [
                        {
                            'DatabaseName': 'string',
                            'Tables': [
                                'string',
                            ]
                        },
                    ]
                },
                'DatabaseName': 'string',
                'Description': 'string',
                'Classifiers': [
                    'string',
                ],
                'SchemaChangePolicy': {
                    'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
                    'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
                },
                'State': 'READY'|'RUNNING'|'STOPPING',
                'TablePrefix': 'string',
                'Schedule': {
                    'ScheduleExpression': 'string',
                    'State': 'SCHEDULED'|'NOT_SCHEDULED'|'TRANSITIONING'
                },
                'CrawlElapsedTime': 123,
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdated': datetime(2015, 1, 1),
                'LastCrawl': {
                    'Status': 'SUCCEEDED'|'CANCELLED'|'FAILED',
                    'ErrorMessage': 'string',
                    'LogGroup': 'string',
                    'LogStream': 'string',
                    'MessagePrefix': 'string',
                    'StartTime': datetime(2015, 1, 1)
                },
                'Version': 123,
                'Configuration': 'string',
                'CrawlerSecurityConfiguration': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_data_catalog_encryption_settings(CatalogId=None):
    """
    Retrieves the security configuration for a specified catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_data_catalog_encryption_settings(
        CatalogId='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog to retrieve the security configuration for. If none is provided, the AWS account ID is used by default.

    :rtype: dict
ReturnsResponse Syntax{
    'DataCatalogEncryptionSettings': {
        'EncryptionAtRest': {
            'CatalogEncryptionMode': 'DISABLED'|'SSE-KMS',
            'SseAwsKmsKeyId': 'string'
        },
        'ConnectionPasswordEncryption': {
            'ReturnConnectionPasswordEncrypted': True|False,
            'AwsKmsKeyId': 'string'
        }
    }
}


Response Structure

(dict) --
DataCatalogEncryptionSettings (dict) --The requested security configuration.

EncryptionAtRest (dict) --Specifies the encryption-at-rest configuration for the Data Catalog.

CatalogEncryptionMode (string) --The encryption-at-rest mode for encrypting Data Catalog data.

SseAwsKmsKeyId (string) --The ID of the AWS KMS key to use for encryption at rest.



ConnectionPasswordEncryption (dict) --When connection password protection is enabled, the Data Catalog uses a customer-provided key to encrypt the password as part of CreateConnection or UpdateConnection and store it in the ENCRYPTED_PASSWORD field in the connection properties. You can enable catalog encryption or only password encryption.

ReturnConnectionPasswordEncrypted (boolean) --When the ReturnConnectionPasswordEncrypted flag is set to "true", passwords remain encrypted in the responses of GetConnection and GetConnections . This encryption takes effect independently from catalog encryption.

AwsKmsKeyId (string) --An AWS KMS key that is used to encrypt the connection password.
If connection password protection is enabled, the caller of CreateConnection and UpdateConnection needs at least kms:Encrypt permission on the specified AWS KMS key, to encrypt passwords before storing them in the Data Catalog.
You can set the decrypt permission to enable or restrict access on the password key according to your security requirements.










Exceptions

Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'DataCatalogEncryptionSettings': {
            'EncryptionAtRest': {
                'CatalogEncryptionMode': 'DISABLED'|'SSE-KMS',
                'SseAwsKmsKeyId': 'string'
            },
            'ConnectionPasswordEncryption': {
                'ReturnConnectionPasswordEncrypted': True|False,
                'AwsKmsKeyId': 'string'
            }
        }
    }
    
    
    """
    pass

def get_database(CatalogId=None, Name=None):
    """
    Retrieves the definition of a specified database.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_database(
        CatalogId='string',
        Name='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the database resides. If none is provided, the AWS account ID is used by default.

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the database to retrieve. For Hive compatibility, this should be all lowercase.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Database': {
        'Name': 'string',
        'Description': 'string',
        'LocationUri': 'string',
        'Parameters': {
            'string': 'string'
        },
        'CreateTime': datetime(2015, 1, 1),
        'CreateTableDefaultPermissions': [
            {
                'Principal': {
                    'DataLakePrincipalIdentifier': 'string'
                },
                'Permissions': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ]
            },
        ]
    }
}


Response Structure

(dict) --

Database (dict) --
The definition of the specified database in the Data Catalog.

Name (string) --
The name of the database. For Hive compatibility, this is folded to lowercase when it is stored.

Description (string) --
A description of the database.

LocationUri (string) --
The location of the database (for example, an HDFS path).

Parameters (dict) --
These key-value pairs define parameters and properties of the database.

(string) --
(string) --




CreateTime (datetime) --
The time at which the metadata database was created in the catalog.

CreateTableDefaultPermissions (list) --
Creates a set of default permissions on the table for principals.

(dict) --
Permissions granted to a principal.

Principal (dict) --
The principal who is granted permissions.

DataLakePrincipalIdentifier (string) --
An identifier for the AWS Lake Formation principal.



Permissions (list) --
The permissions that are granted to the principal.

(string) --














Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.GlueEncryptionException


    :return: {
        'Database': {
            'Name': 'string',
            'Description': 'string',
            'LocationUri': 'string',
            'Parameters': {
                'string': 'string'
            },
            'CreateTime': datetime(2015, 1, 1),
            'CreateTableDefaultPermissions': [
                {
                    'Principal': {
                        'DataLakePrincipalIdentifier': 'string'
                    },
                    'Permissions': [
                        'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_databases(CatalogId=None, NextToken=None, MaxResults=None):
    """
    Retrieves all databases defined in a given Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_databases(
        CatalogId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog from which to retrieve Databases . If none is provided, the AWS account ID is used by default.

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of databases to return in one response.

    :rtype: dict

ReturnsResponse Syntax
{
    'DatabaseList': [
        {
            'Name': 'string',
            'Description': 'string',
            'LocationUri': 'string',
            'Parameters': {
                'string': 'string'
            },
            'CreateTime': datetime(2015, 1, 1),
            'CreateTableDefaultPermissions': [
                {
                    'Principal': {
                        'DataLakePrincipalIdentifier': 'string'
                    },
                    'Permissions': [
                        'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                    ]
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

DatabaseList (list) --
A list of Database objects from the specified catalog.

(dict) --
The Database object represents a logical grouping of tables that might reside in a Hive metastore or an RDBMS.

Name (string) --
The name of the database. For Hive compatibility, this is folded to lowercase when it is stored.

Description (string) --
A description of the database.

LocationUri (string) --
The location of the database (for example, an HDFS path).

Parameters (dict) --
These key-value pairs define parameters and properties of the database.

(string) --
(string) --




CreateTime (datetime) --
The time at which the metadata database was created in the catalog.

CreateTableDefaultPermissions (list) --
Creates a set of default permissions on the table for principals.

(dict) --
Permissions granted to a principal.

Principal (dict) --
The principal who is granted permissions.

DataLakePrincipalIdentifier (string) --
An identifier for the AWS Lake Formation principal.



Permissions (list) --
The permissions that are granted to the principal.

(string) --










NextToken (string) --
A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.







Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.GlueEncryptionException


    :return: {
        'DatabaseList': [
            {
                'Name': 'string',
                'Description': 'string',
                'LocationUri': 'string',
                'Parameters': {
                    'string': 'string'
                },
                'CreateTime': datetime(2015, 1, 1),
                'CreateTableDefaultPermissions': [
                    {
                        'Principal': {
                            'DataLakePrincipalIdentifier': 'string'
                        },
                        'Permissions': [
                            'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                        ]
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_dataflow_graph(PythonScript=None):
    """
    Transforms a Python script into a directed acyclic graph (DAG).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_dataflow_graph(
        PythonScript='string'
    )
    
    
    :type PythonScript: string
    :param PythonScript: The Python script to transform.

    :rtype: dict
ReturnsResponse Syntax{
    'DagNodes': [
        {
            'Id': 'string',
            'NodeType': 'string',
            'Args': [
                {
                    'Name': 'string',
                    'Value': 'string',
                    'Param': True|False
                },
            ],
            'LineNumber': 123
        },
    ],
    'DagEdges': [
        {
            'Source': 'string',
            'Target': 'string',
            'TargetParameter': 'string'
        },
    ]
}


Response Structure

(dict) --
DagNodes (list) --A list of the nodes in the resulting DAG.

(dict) --Represents a node in a directed acyclic graph (DAG)

Id (string) --A node identifier that is unique within the node\'s graph.

NodeType (string) --The type of node that this is.

Args (list) --Properties of the node, in the form of name-value pairs.

(dict) --An argument or property of a node.

Name (string) --The name of the argument or property.

Value (string) --The value of the argument or property.

Param (boolean) --True if the value is used as a parameter.





LineNumber (integer) --The line number of the node.





DagEdges (list) --A list of the edges in the resulting DAG.

(dict) --Represents a directional edge in a directed acyclic graph (DAG).

Source (string) --The ID of the node at which the edge starts.

Target (string) --The ID of the node at which the edge ends.

TargetParameter (string) --The target of the edge.










Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'DagNodes': [
            {
                'Id': 'string',
                'NodeType': 'string',
                'Args': [
                    {
                        'Name': 'string',
                        'Value': 'string',
                        'Param': True|False
                    },
                ],
                'LineNumber': 123
            },
        ],
        'DagEdges': [
            {
                'Source': 'string',
                'Target': 'string',
                'TargetParameter': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_dev_endpoint(EndpointName=None):
    """
    Retrieves information about a specified development endpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_dev_endpoint(
        EndpointName='string'
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]\nName of the DevEndpoint to retrieve information for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DevEndpoint': {
        'EndpointName': 'string',
        'RoleArn': 'string',
        'SecurityGroupIds': [
            'string',
        ],
        'SubnetId': 'string',
        'YarnEndpointAddress': 'string',
        'PrivateAddress': 'string',
        'ZeppelinRemoteSparkInterpreterPort': 123,
        'PublicAddress': 'string',
        'Status': 'string',
        'WorkerType': 'Standard'|'G.1X'|'G.2X',
        'GlueVersion': 'string',
        'NumberOfWorkers': 123,
        'NumberOfNodes': 123,
        'AvailabilityZone': 'string',
        'VpcId': 'string',
        'ExtraPythonLibsS3Path': 'string',
        'ExtraJarsS3Path': 'string',
        'FailureReason': 'string',
        'LastUpdateStatus': 'string',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'LastModifiedTimestamp': datetime(2015, 1, 1),
        'PublicKey': 'string',
        'PublicKeys': [
            'string',
        ],
        'SecurityConfiguration': 'string',
        'Arguments': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --
DevEndpoint (dict) --A DevEndpoint definition.

EndpointName (string) --The name of the DevEndpoint .

RoleArn (string) --The Amazon Resource Name (ARN) of the IAM role used in this DevEndpoint .

SecurityGroupIds (list) --A list of security group identifiers used in this DevEndpoint .

(string) --


SubnetId (string) --The subnet ID for this DevEndpoint .

YarnEndpointAddress (string) --The YARN endpoint address used by this DevEndpoint .

PrivateAddress (string) --A private IP address to access the DevEndpoint within a VPC if the DevEndpoint is created within one. The PrivateAddress field is present only when you create the DevEndpoint within your VPC.

ZeppelinRemoteSparkInterpreterPort (integer) --The Apache Zeppelin port for the remote Apache Spark interpreter.

PublicAddress (string) --The public IP address used by this DevEndpoint . The PublicAddress field is present only when you create a non-virtual private cloud (VPC) DevEndpoint .

Status (string) --The current status of this DevEndpoint .

WorkerType (string) --The type of predefined worker that is allocated to the development endpoint. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.
For the G.2X worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.

Known issue: when a development endpoint is created with the G.2X WorkerType configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB of memory, and a 64 GB disk.

GlueVersion (string) --Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.
Development endpoints that are created without specifying a Glue version default to Glue 0.9.
You can specify a version of Python support for development endpoints by using the Arguments parameter in the CreateDevEndpoint or UpdateDevEndpoint APIs. If no arguments are provided, the version defaults to Python 2.

NumberOfWorkers (integer) --The number of workers of a defined workerType that are allocated to the development endpoint.
The maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .

NumberOfNodes (integer) --The number of AWS Glue Data Processing Units (DPUs) allocated to this DevEndpoint .

AvailabilityZone (string) --The AWS Availability Zone where this DevEndpoint is located.

VpcId (string) --The ID of the virtual private cloud (VPC) used by this DevEndpoint .

ExtraPythonLibsS3Path (string) --The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your DevEndpoint . Multiple values must be complete paths separated by a comma.

Note
You can only use pure Python libraries with a DevEndpoint . Libraries that rely on C extensions, such as the pandas Python data analysis library, are not currently supported.


ExtraJarsS3Path (string) --The path to one or more Java .jar files in an S3 bucket that should be loaded in your DevEndpoint .

Note
You can only use pure Java/Scala libraries with a DevEndpoint .


FailureReason (string) --The reason for a current failure in this DevEndpoint .

LastUpdateStatus (string) --The status of the last update.

CreatedTimestamp (datetime) --The point in time at which this DevEndpoint was created.

LastModifiedTimestamp (datetime) --The point in time at which this DevEndpoint was last modified.

PublicKey (string) --The public key to be used by this DevEndpoint for authentication. This attribute is provided for backward compatibility because the recommended attribute to use is public keys.

PublicKeys (list) --A list of public keys to be used by the DevEndpoints for authentication. Using this attribute is preferred over a single public key because the public keys allow you to have a different private key per client.

Note
If you previously created an endpoint with a public key, you must remove that key to be able to set a list of public keys. Call the UpdateDevEndpoint API operation with the public key content in the deletePublicKeys attribute, and the list of new keys in the addPublicKeys attribute.


(string) --


SecurityConfiguration (string) --The name of the SecurityConfiguration structure to be used with this DevEndpoint .

Arguments (dict) --A map of arguments used to configure the DevEndpoint .
Valid arguments are:

"--enable-glue-datacatalog": ""
"GLUE_PYTHON_VERSION": "3"
"GLUE_PYTHON_VERSION": "2"

You can specify a version of Python support for development endpoints by using the Arguments parameter in the CreateDevEndpoint or UpdateDevEndpoint APIs. If no arguments are provided, the version defaults to Python 2.

(string) --
(string) --











Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException


    :return: {
        'DevEndpoint': {
            'EndpointName': 'string',
            'RoleArn': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'SubnetId': 'string',
            'YarnEndpointAddress': 'string',
            'PrivateAddress': 'string',
            'ZeppelinRemoteSparkInterpreterPort': 123,
            'PublicAddress': 'string',
            'Status': 'string',
            'WorkerType': 'Standard'|'G.1X'|'G.2X',
            'GlueVersion': 'string',
            'NumberOfWorkers': 123,
            'NumberOfNodes': 123,
            'AvailabilityZone': 'string',
            'VpcId': 'string',
            'ExtraPythonLibsS3Path': 'string',
            'ExtraJarsS3Path': 'string',
            'FailureReason': 'string',
            'LastUpdateStatus': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'LastModifiedTimestamp': datetime(2015, 1, 1),
            'PublicKey': 'string',
            'PublicKeys': [
                'string',
            ],
            'SecurityConfiguration': 'string',
            'Arguments': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
    For the G.1X worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.
    For the G.2X worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.
    
    """
    pass

def get_dev_endpoints(MaxResults=None, NextToken=None):
    """
    Retrieves all the development endpoints in this AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_dev_endpoints(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum size of information to return.

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :rtype: dict

ReturnsResponse Syntax
{
    'DevEndpoints': [
        {
            'EndpointName': 'string',
            'RoleArn': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'SubnetId': 'string',
            'YarnEndpointAddress': 'string',
            'PrivateAddress': 'string',
            'ZeppelinRemoteSparkInterpreterPort': 123,
            'PublicAddress': 'string',
            'Status': 'string',
            'WorkerType': 'Standard'|'G.1X'|'G.2X',
            'GlueVersion': 'string',
            'NumberOfWorkers': 123,
            'NumberOfNodes': 123,
            'AvailabilityZone': 'string',
            'VpcId': 'string',
            'ExtraPythonLibsS3Path': 'string',
            'ExtraJarsS3Path': 'string',
            'FailureReason': 'string',
            'LastUpdateStatus': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'LastModifiedTimestamp': datetime(2015, 1, 1),
            'PublicKey': 'string',
            'PublicKeys': [
                'string',
            ],
            'SecurityConfiguration': 'string',
            'Arguments': {
                'string': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

DevEndpoints (list) --
A list of DevEndpoint definitions.

(dict) --
A development endpoint where a developer can remotely debug extract, transform, and load (ETL) scripts.

EndpointName (string) --
The name of the DevEndpoint .

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role used in this DevEndpoint .

SecurityGroupIds (list) --
A list of security group identifiers used in this DevEndpoint .

(string) --


SubnetId (string) --
The subnet ID for this DevEndpoint .

YarnEndpointAddress (string) --
The YARN endpoint address used by this DevEndpoint .

PrivateAddress (string) --
A private IP address to access the DevEndpoint within a VPC if the DevEndpoint is created within one. The PrivateAddress field is present only when you create the DevEndpoint within your VPC.

ZeppelinRemoteSparkInterpreterPort (integer) --
The Apache Zeppelin port for the remote Apache Spark interpreter.

PublicAddress (string) --
The public IP address used by this DevEndpoint . The PublicAddress field is present only when you create a non-virtual private cloud (VPC) DevEndpoint .

Status (string) --
The current status of this DevEndpoint .

WorkerType (string) --
The type of predefined worker that is allocated to the development endpoint. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.
For the G.2X worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.

Known issue: when a development endpoint is created with the G.2X WorkerType configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB of memory, and a 64 GB disk.

GlueVersion (string) --
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.
Development endpoints that are created without specifying a Glue version default to Glue 0.9.
You can specify a version of Python support for development endpoints by using the Arguments parameter in the CreateDevEndpoint or UpdateDevEndpoint APIs. If no arguments are provided, the version defaults to Python 2.

NumberOfWorkers (integer) --
The number of workers of a defined workerType that are allocated to the development endpoint.
The maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .

NumberOfNodes (integer) --
The number of AWS Glue Data Processing Units (DPUs) allocated to this DevEndpoint .

AvailabilityZone (string) --
The AWS Availability Zone where this DevEndpoint is located.

VpcId (string) --
The ID of the virtual private cloud (VPC) used by this DevEndpoint .

ExtraPythonLibsS3Path (string) --
The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your DevEndpoint . Multiple values must be complete paths separated by a comma.

Note
You can only use pure Python libraries with a DevEndpoint . Libraries that rely on C extensions, such as the pandas Python data analysis library, are not currently supported.


ExtraJarsS3Path (string) --
The path to one or more Java .jar files in an S3 bucket that should be loaded in your DevEndpoint .

Note
You can only use pure Java/Scala libraries with a DevEndpoint .


FailureReason (string) --
The reason for a current failure in this DevEndpoint .

LastUpdateStatus (string) --
The status of the last update.

CreatedTimestamp (datetime) --
The point in time at which this DevEndpoint was created.

LastModifiedTimestamp (datetime) --
The point in time at which this DevEndpoint was last modified.

PublicKey (string) --
The public key to be used by this DevEndpoint for authentication. This attribute is provided for backward compatibility because the recommended attribute to use is public keys.

PublicKeys (list) --
A list of public keys to be used by the DevEndpoints for authentication. Using this attribute is preferred over a single public key because the public keys allow you to have a different private key per client.

Note
If you previously created an endpoint with a public key, you must remove that key to be able to set a list of public keys. Call the UpdateDevEndpoint API operation with the public key content in the deletePublicKeys attribute, and the list of new keys in the addPublicKeys attribute.


(string) --


SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this DevEndpoint .

Arguments (dict) --
A map of arguments used to configure the DevEndpoint .
Valid arguments are:

"--enable-glue-datacatalog": ""
"GLUE_PYTHON_VERSION": "3"
"GLUE_PYTHON_VERSION": "2"

You can specify a version of Python support for development endpoints by using the Arguments parameter in the CreateDevEndpoint or UpdateDevEndpoint APIs. If no arguments are provided, the version defaults to Python 2.

(string) --
(string) --








NextToken (string) --
A continuation token, if not all DevEndpoint definitions have yet been returned.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException


    :return: {
        'DevEndpoints': [
            {
                'EndpointName': 'string',
                'RoleArn': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'SubnetId': 'string',
                'YarnEndpointAddress': 'string',
                'PrivateAddress': 'string',
                'ZeppelinRemoteSparkInterpreterPort': 123,
                'PublicAddress': 'string',
                'Status': 'string',
                'WorkerType': 'Standard'|'G.1X'|'G.2X',
                'GlueVersion': 'string',
                'NumberOfWorkers': 123,
                'NumberOfNodes': 123,
                'AvailabilityZone': 'string',
                'VpcId': 'string',
                'ExtraPythonLibsS3Path': 'string',
                'ExtraJarsS3Path': 'string',
                'FailureReason': 'string',
                'LastUpdateStatus': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'LastModifiedTimestamp': datetime(2015, 1, 1),
                'PublicKey': 'string',
                'PublicKeys': [
                    'string',
                ],
                'SecurityConfiguration': 'string',
                'Arguments': {
                    'string': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_job(JobName=None):
    """
    Retrieves an existing job definition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_job(
        JobName='string'
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]\nThe name of the job definition to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Job': {
        'Name': 'string',
        'Description': 'string',
        'LogUri': 'string',
        'Role': 'string',
        'CreatedOn': datetime(2015, 1, 1),
        'LastModifiedOn': datetime(2015, 1, 1),
        'ExecutionProperty': {
            'MaxConcurrentRuns': 123
        },
        'Command': {
            'Name': 'string',
            'ScriptLocation': 'string',
            'PythonVersion': 'string'
        },
        'DefaultArguments': {
            'string': 'string'
        },
        'NonOverridableArguments': {
            'string': 'string'
        },
        'Connections': {
            'Connections': [
                'string',
            ]
        },
        'MaxRetries': 123,
        'AllocatedCapacity': 123,
        'Timeout': 123,
        'MaxCapacity': 123.0,
        'WorkerType': 'Standard'|'G.1X'|'G.2X',
        'NumberOfWorkers': 123,
        'SecurityConfiguration': 'string',
        'NotificationProperty': {
            'NotifyDelayAfter': 123
        },
        'GlueVersion': 'string'
    }
}


Response Structure

(dict) --
Job (dict) --The requested job definition.

Name (string) --The name you assign to this job definition.

Description (string) --A description of the job.

LogUri (string) --This field is reserved for future use.

Role (string) --The name or Amazon Resource Name (ARN) of the IAM role associated with this job.

CreatedOn (datetime) --The time and date that this job definition was created.

LastModifiedOn (datetime) --The last point in time when this job definition was modified.

ExecutionProperty (dict) --An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job.

MaxConcurrentRuns (integer) --The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.



Command (dict) --The JobCommand that executes this job.

Name (string) --The name of the job command. For an Apache Spark ETL job, this must be glueetl . For a Python shell job, it must be pythonshell .

ScriptLocation (string) --Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that executes a job.

PythonVersion (string) --The Python version being used to execute a Python shell job. Allowed values are 2 or 3.



DefaultArguments (dict) --The default arguments for this job, specified as name-value pairs.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




NonOverridableArguments (dict) --Non-overridable arguments for this job, specified as name-value pairs.

(string) --
(string) --




Connections (dict) --The connections used for this job.

Connections (list) --A list of connections used by the job.

(string) --




MaxRetries (integer) --The maximum number of times to retry this job after a JobRun fails.

AllocatedCapacity (integer) --This field is deprecated. Use MaxCapacity instead.
The number of AWS Glue data processing units (DPUs) allocated to runs of this job. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .

Timeout (integer) --The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours).

MaxCapacity (float) --The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .
Do not set Max Capacity if using WorkerType and NumberOfWorkers .
The value that can be allocated for MaxCapacity depends on whether you are running a Python shell job or an Apache Spark ETL job:

When you specify a Python shell job (JobCommand.Name ="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
When you specify an Apache Spark ETL job (JobCommand.Name ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.


WorkerType (string) --The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.
For the G.2X worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.


NumberOfWorkers (integer) --The number of workers of a defined workerType that are allocated when a job runs.
The maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .

SecurityConfiguration (string) --The name of the SecurityConfiguration structure to be used with this job.

NotificationProperty (dict) --Specifies configuration properties of a job notification.

NotifyDelayAfter (integer) --After a job run starts, the number of minutes to wait before sending a job run delay notification.



GlueVersion (string) --Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.
Jobs that are created without specifying a Glue version default to Glue 0.9.








Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Job': {
            'Name': 'string',
            'Description': 'string',
            'LogUri': 'string',
            'Role': 'string',
            'CreatedOn': datetime(2015, 1, 1),
            'LastModifiedOn': datetime(2015, 1, 1),
            'ExecutionProperty': {
                'MaxConcurrentRuns': 123
            },
            'Command': {
                'Name': 'string',
                'ScriptLocation': 'string',
                'PythonVersion': 'string'
            },
            'DefaultArguments': {
                'string': 'string'
            },
            'NonOverridableArguments': {
                'string': 'string'
            },
            'Connections': {
                'Connections': [
                    'string',
                ]
            },
            'MaxRetries': 123,
            'AllocatedCapacity': 123,
            'Timeout': 123,
            'MaxCapacity': 123.0,
            'WorkerType': 'Standard'|'G.1X'|'G.2X',
            'NumberOfWorkers': 123,
            'SecurityConfiguration': 'string',
            'NotificationProperty': {
                'NotifyDelayAfter': 123
            },
            'GlueVersion': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_job_bookmark(JobName=None, RunId=None):
    """
    Returns information on a job bookmark entry.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_job_bookmark(
        JobName='string',
        RunId='string'
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]\nThe name of the job in question.\n

    :type RunId: string
    :param RunId: The unique run identifier associated with this job run.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobBookmarkEntry': {
        'JobName': 'string',
        'Version': 123,
        'Run': 123,
        'Attempt': 123,
        'PreviousRunId': 'string',
        'RunId': 'string',
        'JobBookmark': 'string'
    }
}


Response Structure

(dict) --

JobBookmarkEntry (dict) --
A structure that defines a point that a job can resume processing.

JobName (string) --
The name of the job in question.

Version (integer) --
The version of the job.

Run (integer) --
The run ID number.

Attempt (integer) --
The attempt ID number.

PreviousRunId (string) --
The unique run identifier associated with the previous job run.

RunId (string) --
The run ID number.

JobBookmark (string) --
The bookmark itself.









Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ValidationException


    :return: {
        'JobBookmarkEntry': {
            'JobName': 'string',
            'Version': 123,
            'Run': 123,
            'Attempt': 123,
            'PreviousRunId': 'string',
            'RunId': 'string',
            'JobBookmark': 'string'
        }
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.ValidationException
    
    """
    pass

def get_job_run(JobName=None, RunId=None, PredecessorsIncluded=None):
    """
    Retrieves the metadata for a given job run.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_job_run(
        JobName='string',
        RunId='string',
        PredecessorsIncluded=True|False
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]\nName of the job definition being run.\n

    :type RunId: string
    :param RunId: [REQUIRED]\nThe ID of the job run.\n

    :type PredecessorsIncluded: boolean
    :param PredecessorsIncluded: True if a list of predecessor runs should be returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobRun': {
        'Id': 'string',
        'Attempt': 123,
        'PreviousRunId': 'string',
        'TriggerName': 'string',
        'JobName': 'string',
        'StartedOn': datetime(2015, 1, 1),
        'LastModifiedOn': datetime(2015, 1, 1),
        'CompletedOn': datetime(2015, 1, 1),
        'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
        'Arguments': {
            'string': 'string'
        },
        'ErrorMessage': 'string',
        'PredecessorRuns': [
            {
                'JobName': 'string',
                'RunId': 'string'
            },
        ],
        'AllocatedCapacity': 123,
        'ExecutionTime': 123,
        'Timeout': 123,
        'MaxCapacity': 123.0,
        'WorkerType': 'Standard'|'G.1X'|'G.2X',
        'NumberOfWorkers': 123,
        'SecurityConfiguration': 'string',
        'LogGroupName': 'string',
        'NotificationProperty': {
            'NotifyDelayAfter': 123
        },
        'GlueVersion': 'string'
    }
}


Response Structure

(dict) --

JobRun (dict) --
The requested job-run metadata.

Id (string) --
The ID of this job run.

Attempt (integer) --
The number of the attempt to run this job.

PreviousRunId (string) --
The ID of the previous run of this job. For example, the JobRunId specified in the StartJobRun action.

TriggerName (string) --
The name of the trigger that started this job run.

JobName (string) --
The name of the job definition being used in this run.

StartedOn (datetime) --
The date and time at which this job run was started.

LastModifiedOn (datetime) --
The last time that this job run was modified.

CompletedOn (datetime) --
The date and time that this job run completed.

JobRunState (string) --
The current state of the job run. For more information about the statuses of jobs that have terminated abnormally, see AWS Glue Job Run Statuses .

Arguments (dict) --
The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




ErrorMessage (string) --
An error message associated with this job run.

PredecessorRuns (list) --
A list of predecessors to this job run.

(dict) --
A job run that was used in the predicate of a conditional trigger that triggered this job run.

JobName (string) --
The name of the job definition used by the predecessor job run.

RunId (string) --
The job-run ID of the predecessor job run.





AllocatedCapacity (integer) --
This field is deprecated. Use MaxCapacity instead.
The number of AWS Glue data processing units (DPUs) allocated to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .

ExecutionTime (integer) --
The amount of time (in seconds) that the job run consumed resources.

Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

MaxCapacity (float) --
The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .
Do not set Max Capacity if using WorkerType and NumberOfWorkers .
The value that can be allocated for MaxCapacity depends on whether you are running a Python shell job or an Apache Spark ETL job:

When you specify a Python shell job (JobCommand.Name ="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
When you specify an Apache Spark ETL job (JobCommand.Name ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.


WorkerType (string) --
The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
For the G.2X worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.


NumberOfWorkers (integer) --
The number of workers of a defined workerType that are allocated when a job runs.
The maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this job run.

LogGroupName (string) --
The name of the log group for secure logging that can be server-side encrypted in Amazon CloudWatch using AWS KMS. This name can be /aws-glue/jobs/ , in which case the default encryption is NONE . If you add a role name and SecurityConfiguration name (in other words, /aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/ ), then that security configuration is used to encrypt the log group.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



GlueVersion (string) --
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.
Jobs that are created without specifying a Glue version default to Glue 0.9.









Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'JobRun': {
            'Id': 'string',
            'Attempt': 123,
            'PreviousRunId': 'string',
            'TriggerName': 'string',
            'JobName': 'string',
            'StartedOn': datetime(2015, 1, 1),
            'LastModifiedOn': datetime(2015, 1, 1),
            'CompletedOn': datetime(2015, 1, 1),
            'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
            'Arguments': {
                'string': 'string'
            },
            'ErrorMessage': 'string',
            'PredecessorRuns': [
                {
                    'JobName': 'string',
                    'RunId': 'string'
                },
            ],
            'AllocatedCapacity': 123,
            'ExecutionTime': 123,
            'Timeout': 123,
            'MaxCapacity': 123.0,
            'WorkerType': 'Standard'|'G.1X'|'G.2X',
            'NumberOfWorkers': 123,
            'SecurityConfiguration': 'string',
            'LogGroupName': 'string',
            'NotificationProperty': {
                'NotifyDelayAfter': 123
            },
            'GlueVersion': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_job_runs(JobName=None, NextToken=None, MaxResults=None):
    """
    Retrieves metadata for all runs of a given job definition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_job_runs(
        JobName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]\nThe name of the job definition for which to retrieve all job runs.\n

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :type MaxResults: integer
    :param MaxResults: The maximum size of the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobRuns': [
        {
            'Id': 'string',
            'Attempt': 123,
            'PreviousRunId': 'string',
            'TriggerName': 'string',
            'JobName': 'string',
            'StartedOn': datetime(2015, 1, 1),
            'LastModifiedOn': datetime(2015, 1, 1),
            'CompletedOn': datetime(2015, 1, 1),
            'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
            'Arguments': {
                'string': 'string'
            },
            'ErrorMessage': 'string',
            'PredecessorRuns': [
                {
                    'JobName': 'string',
                    'RunId': 'string'
                },
            ],
            'AllocatedCapacity': 123,
            'ExecutionTime': 123,
            'Timeout': 123,
            'MaxCapacity': 123.0,
            'WorkerType': 'Standard'|'G.1X'|'G.2X',
            'NumberOfWorkers': 123,
            'SecurityConfiguration': 'string',
            'LogGroupName': 'string',
            'NotificationProperty': {
                'NotifyDelayAfter': 123
            },
            'GlueVersion': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

JobRuns (list) --
A list of job-run metadata objects.

(dict) --
Contains information about a job run.

Id (string) --
The ID of this job run.

Attempt (integer) --
The number of the attempt to run this job.

PreviousRunId (string) --
The ID of the previous run of this job. For example, the JobRunId specified in the StartJobRun action.

TriggerName (string) --
The name of the trigger that started this job run.

JobName (string) --
The name of the job definition being used in this run.

StartedOn (datetime) --
The date and time at which this job run was started.

LastModifiedOn (datetime) --
The last time that this job run was modified.

CompletedOn (datetime) --
The date and time that this job run completed.

JobRunState (string) --
The current state of the job run. For more information about the statuses of jobs that have terminated abnormally, see AWS Glue Job Run Statuses .

Arguments (dict) --
The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




ErrorMessage (string) --
An error message associated with this job run.

PredecessorRuns (list) --
A list of predecessors to this job run.

(dict) --
A job run that was used in the predicate of a conditional trigger that triggered this job run.

JobName (string) --
The name of the job definition used by the predecessor job run.

RunId (string) --
The job-run ID of the predecessor job run.





AllocatedCapacity (integer) --
This field is deprecated. Use MaxCapacity instead.
The number of AWS Glue data processing units (DPUs) allocated to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .

ExecutionTime (integer) --
The amount of time (in seconds) that the job run consumed resources.

Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

MaxCapacity (float) --
The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .
Do not set Max Capacity if using WorkerType and NumberOfWorkers .
The value that can be allocated for MaxCapacity depends on whether you are running a Python shell job or an Apache Spark ETL job:

When you specify a Python shell job (JobCommand.Name ="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
When you specify an Apache Spark ETL job (JobCommand.Name ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.


WorkerType (string) --
The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
For the G.2X worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.


NumberOfWorkers (integer) --
The number of workers of a defined workerType that are allocated when a job runs.
The maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this job run.

LogGroupName (string) --
The name of the log group for secure logging that can be server-side encrypted in Amazon CloudWatch using AWS KMS. This name can be /aws-glue/jobs/ , in which case the default encryption is NONE . If you add a role name and SecurityConfiguration name (in other words, /aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/ ), then that security configuration is used to encrypt the log group.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



GlueVersion (string) --
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.
Jobs that are created without specifying a Glue version default to Glue 0.9.





NextToken (string) --
A continuation token, if not all requested job runs have been returned.







Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'JobRuns': [
            {
                'Id': 'string',
                'Attempt': 123,
                'PreviousRunId': 'string',
                'TriggerName': 'string',
                'JobName': 'string',
                'StartedOn': datetime(2015, 1, 1),
                'LastModifiedOn': datetime(2015, 1, 1),
                'CompletedOn': datetime(2015, 1, 1),
                'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                'Arguments': {
                    'string': 'string'
                },
                'ErrorMessage': 'string',
                'PredecessorRuns': [
                    {
                        'JobName': 'string',
                        'RunId': 'string'
                    },
                ],
                'AllocatedCapacity': 123,
                'ExecutionTime': 123,
                'Timeout': 123,
                'MaxCapacity': 123.0,
                'WorkerType': 'Standard'|'G.1X'|'G.2X',
                'NumberOfWorkers': 123,
                'SecurityConfiguration': 'string',
                'LogGroupName': 'string',
                'NotificationProperty': {
                    'NotifyDelayAfter': 123
                },
                'GlueVersion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_jobs(NextToken=None, MaxResults=None):
    """
    Retrieves all current job definitions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_jobs(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :type MaxResults: integer
    :param MaxResults: The maximum size of the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'Jobs': [
        {
            'Name': 'string',
            'Description': 'string',
            'LogUri': 'string',
            'Role': 'string',
            'CreatedOn': datetime(2015, 1, 1),
            'LastModifiedOn': datetime(2015, 1, 1),
            'ExecutionProperty': {
                'MaxConcurrentRuns': 123
            },
            'Command': {
                'Name': 'string',
                'ScriptLocation': 'string',
                'PythonVersion': 'string'
            },
            'DefaultArguments': {
                'string': 'string'
            },
            'NonOverridableArguments': {
                'string': 'string'
            },
            'Connections': {
                'Connections': [
                    'string',
                ]
            },
            'MaxRetries': 123,
            'AllocatedCapacity': 123,
            'Timeout': 123,
            'MaxCapacity': 123.0,
            'WorkerType': 'Standard'|'G.1X'|'G.2X',
            'NumberOfWorkers': 123,
            'SecurityConfiguration': 'string',
            'NotificationProperty': {
                'NotifyDelayAfter': 123
            },
            'GlueVersion': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Jobs (list) --
A list of job definitions.

(dict) --
Specifies a job definition.

Name (string) --
The name you assign to this job definition.

Description (string) --
A description of the job.

LogUri (string) --
This field is reserved for future use.

Role (string) --
The name or Amazon Resource Name (ARN) of the IAM role associated with this job.

CreatedOn (datetime) --
The time and date that this job definition was created.

LastModifiedOn (datetime) --
The last point in time when this job definition was modified.

ExecutionProperty (dict) --
An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job.

MaxConcurrentRuns (integer) --
The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.



Command (dict) --
The JobCommand that executes this job.

Name (string) --
The name of the job command. For an Apache Spark ETL job, this must be glueetl . For a Python shell job, it must be pythonshell .

ScriptLocation (string) --
Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that executes a job.

PythonVersion (string) --
The Python version being used to execute a Python shell job. Allowed values are 2 or 3.



DefaultArguments (dict) --
The default arguments for this job, specified as name-value pairs.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




NonOverridableArguments (dict) --
Non-overridable arguments for this job, specified as name-value pairs.

(string) --
(string) --




Connections (dict) --
The connections used for this job.

Connections (list) --
A list of connections used by the job.

(string) --




MaxRetries (integer) --
The maximum number of times to retry this job after a JobRun fails.

AllocatedCapacity (integer) --
This field is deprecated. Use MaxCapacity instead.
The number of AWS Glue data processing units (DPUs) allocated to runs of this job. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .

Timeout (integer) --
The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours).

MaxCapacity (float) --
The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .
Do not set Max Capacity if using WorkerType and NumberOfWorkers .
The value that can be allocated for MaxCapacity depends on whether you are running a Python shell job or an Apache Spark ETL job:

When you specify a Python shell job (JobCommand.Name ="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
When you specify an Apache Spark ETL job (JobCommand.Name ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.


WorkerType (string) --
The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.
For the G.2X worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.


NumberOfWorkers (integer) --
The number of workers of a defined workerType that are allocated when a job runs.
The maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this job.

NotificationProperty (dict) --
Specifies configuration properties of a job notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



GlueVersion (string) --
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.
Jobs that are created without specifying a Glue version default to Glue 0.9.





NextToken (string) --
A continuation token, if not all job definitions have yet been returned.







Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Jobs': [
            {
                'Name': 'string',
                'Description': 'string',
                'LogUri': 'string',
                'Role': 'string',
                'CreatedOn': datetime(2015, 1, 1),
                'LastModifiedOn': datetime(2015, 1, 1),
                'ExecutionProperty': {
                    'MaxConcurrentRuns': 123
                },
                'Command': {
                    'Name': 'string',
                    'ScriptLocation': 'string',
                    'PythonVersion': 'string'
                },
                'DefaultArguments': {
                    'string': 'string'
                },
                'NonOverridableArguments': {
                    'string': 'string'
                },
                'Connections': {
                    'Connections': [
                        'string',
                    ]
                },
                'MaxRetries': 123,
                'AllocatedCapacity': 123,
                'Timeout': 123,
                'MaxCapacity': 123.0,
                'WorkerType': 'Standard'|'G.1X'|'G.2X',
                'NumberOfWorkers': 123,
                'SecurityConfiguration': 'string',
                'NotificationProperty': {
                    'NotifyDelayAfter': 123
                },
                'GlueVersion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_mapping(Source=None, Sinks=None, Location=None):
    """
    Creates mappings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_mapping(
        Source={
            'DatabaseName': 'string',
            'TableName': 'string'
        },
        Sinks=[
            {
                'DatabaseName': 'string',
                'TableName': 'string'
            },
        ],
        Location={
            'Jdbc': [
                {
                    'Name': 'string',
                    'Value': 'string',
                    'Param': True|False
                },
            ],
            'S3': [
                {
                    'Name': 'string',
                    'Value': 'string',
                    'Param': True|False
                },
            ],
            'DynamoDB': [
                {
                    'Name': 'string',
                    'Value': 'string',
                    'Param': True|False
                },
            ]
        }
    )
    
    
    :type Source: dict
    :param Source: [REQUIRED]\nSpecifies the source table.\n\nDatabaseName (string) -- [REQUIRED]The database in which the table metadata resides.\n\nTableName (string) -- [REQUIRED]The name of the table in question.\n\n\n

    :type Sinks: list
    :param Sinks: A list of target tables.\n\n(dict) --Specifies a table definition in the AWS Glue Data Catalog.\n\nDatabaseName (string) -- [REQUIRED]The database in which the table metadata resides.\n\nTableName (string) -- [REQUIRED]The name of the table in question.\n\n\n\n\n

    :type Location: dict
    :param Location: Parameters for the mapping.\n\nJdbc (list) --A JDBC location.\n\n(dict) --An argument or property of a node.\n\nName (string) -- [REQUIRED]The name of the argument or property.\n\nValue (string) -- [REQUIRED]The value of the argument or property.\n\nParam (boolean) --True if the value is used as a parameter.\n\n\n\n\n\nS3 (list) --An Amazon Simple Storage Service (Amazon S3) location.\n\n(dict) --An argument or property of a node.\n\nName (string) -- [REQUIRED]The name of the argument or property.\n\nValue (string) -- [REQUIRED]The value of the argument or property.\n\nParam (boolean) --True if the value is used as a parameter.\n\n\n\n\n\nDynamoDB (list) --An Amazon DynamoDB table location.\n\n(dict) --An argument or property of a node.\n\nName (string) -- [REQUIRED]The name of the argument or property.\n\nValue (string) -- [REQUIRED]The value of the argument or property.\n\nParam (boolean) --True if the value is used as a parameter.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Mapping': [
        {
            'SourceTable': 'string',
            'SourcePath': 'string',
            'SourceType': 'string',
            'TargetTable': 'string',
            'TargetPath': 'string',
            'TargetType': 'string'
        },
    ]
}


Response Structure

(dict) --

Mapping (list) --
A list of mappings to the specified targets.

(dict) --
Defines a mapping.

SourceTable (string) --
The name of the source table.

SourcePath (string) --
The source path.

SourceType (string) --
The source type.

TargetTable (string) --
The target table.

TargetPath (string) --
The target path.

TargetType (string) --
The target type.











Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.EntityNotFoundException


    :return: {
        'Mapping': [
            {
                'SourceTable': 'string',
                'SourcePath': 'string',
                'SourceType': 'string',
                'TargetTable': 'string',
                'TargetPath': 'string',
                'TargetType': 'string'
            },
        ]
    }
    
    
    :returns: 
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.EntityNotFoundException
    
    """
    pass

def get_ml_task_run(TransformId=None, TaskRunId=None):
    """
    Gets details for a specific task run on a machine learning transform. Machine learning task runs are asynchronous tasks that AWS Glue runs on your behalf as part of various machine learning workflows. You can check the stats of any task run by calling GetMLTaskRun with the TaskRunID and its parent transform\'s TransformID .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_ml_task_run(
        TransformId='string',
        TaskRunId='string'
    )
    
    
    :type TransformId: string
    :param TransformId: [REQUIRED]\nThe unique identifier of the machine learning transform.\n

    :type TaskRunId: string
    :param TaskRunId: [REQUIRED]\nThe unique identifier of the task run.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TransformId': 'string',
    'TaskRunId': 'string',
    'Status': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
    'LogGroupName': 'string',
    'Properties': {
        'TaskType': 'EVALUATION'|'LABELING_SET_GENERATION'|'IMPORT_LABELS'|'EXPORT_LABELS'|'FIND_MATCHES',
        'ImportLabelsTaskRunProperties': {
            'InputS3Path': 'string',
            'Replace': True|False
        },
        'ExportLabelsTaskRunProperties': {
            'OutputS3Path': 'string'
        },
        'LabelingSetGenerationTaskRunProperties': {
            'OutputS3Path': 'string'
        },
        'FindMatchesTaskRunProperties': {
            'JobId': 'string',
            'JobName': 'string',
            'JobRunId': 'string'
        }
    },
    'ErrorString': 'string',
    'StartedOn': datetime(2015, 1, 1),
    'LastModifiedOn': datetime(2015, 1, 1),
    'CompletedOn': datetime(2015, 1, 1),
    'ExecutionTime': 123
}


Response Structure

(dict) --

TransformId (string) --
The unique identifier of the task run.

TaskRunId (string) --
The unique run identifier associated with this run.

Status (string) --
The status for this task run.

LogGroupName (string) --
The names of the log groups that are associated with the task run.

Properties (dict) --
The list of properties that are associated with the task run.

TaskType (string) --
The type of task run.

ImportLabelsTaskRunProperties (dict) --
The configuration properties for an importing labels task run.

InputS3Path (string) --
The Amazon Simple Storage Service (Amazon S3) path from where you will import the labels.

Replace (boolean) --
Indicates whether to overwrite your existing labels.



ExportLabelsTaskRunProperties (dict) --
The configuration properties for an exporting labels task run.

OutputS3Path (string) --
The Amazon Simple Storage Service (Amazon S3) path where you will export the labels.



LabelingSetGenerationTaskRunProperties (dict) --
The configuration properties for a labeling set generation task run.

OutputS3Path (string) --
The Amazon Simple Storage Service (Amazon S3) path where you will generate the labeling set.



FindMatchesTaskRunProperties (dict) --
The configuration properties for a find matches task run.

JobId (string) --
The job ID for the Find Matches task run.

JobName (string) --
The name assigned to the job for the Find Matches task run.

JobRunId (string) --
The job run ID for the Find Matches task run.





ErrorString (string) --
The error strings that are associated with the task run.

StartedOn (datetime) --
The date and time when this task run started.

LastModifiedOn (datetime) --
The date and time when this task run was last modified.

CompletedOn (datetime) --
The date and time when this task run was completed.

ExecutionTime (integer) --
The amount of time (in seconds) that the task run consumed resources.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException


    :return: {
        'TransformId': 'string',
        'TaskRunId': 'string',
        'Status': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
        'LogGroupName': 'string',
        'Properties': {
            'TaskType': 'EVALUATION'|'LABELING_SET_GENERATION'|'IMPORT_LABELS'|'EXPORT_LABELS'|'FIND_MATCHES',
            'ImportLabelsTaskRunProperties': {
                'InputS3Path': 'string',
                'Replace': True|False
            },
            'ExportLabelsTaskRunProperties': {
                'OutputS3Path': 'string'
            },
            'LabelingSetGenerationTaskRunProperties': {
                'OutputS3Path': 'string'
            },
            'FindMatchesTaskRunProperties': {
                'JobId': 'string',
                'JobName': 'string',
                'JobRunId': 'string'
            }
        },
        'ErrorString': 'string',
        'StartedOn': datetime(2015, 1, 1),
        'LastModifiedOn': datetime(2015, 1, 1),
        'CompletedOn': datetime(2015, 1, 1),
        'ExecutionTime': 123
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.InternalServiceException
    
    """
    pass

def get_ml_task_runs(TransformId=None, NextToken=None, MaxResults=None, Filter=None, Sort=None):
    """
    Gets a list of runs for a machine learning transform. Machine learning task runs are asynchronous tasks that AWS Glue runs on your behalf as part of various machine learning workflows. You can get a sortable, filterable list of machine learning task runs by calling GetMLTaskRuns with their parent transform\'s TransformID and other optional parameters as documented in this section.
    This operation returns a list of historic runs and must be paginated.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_ml_task_runs(
        TransformId='string',
        NextToken='string',
        MaxResults=123,
        Filter={
            'TaskRunType': 'EVALUATION'|'LABELING_SET_GENERATION'|'IMPORT_LABELS'|'EXPORT_LABELS'|'FIND_MATCHES',
            'Status': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
            'StartedBefore': datetime(2015, 1, 1),
            'StartedAfter': datetime(2015, 1, 1)
        },
        Sort={
            'Column': 'TASK_RUN_TYPE'|'STATUS'|'STARTED',
            'SortDirection': 'DESCENDING'|'ASCENDING'
        }
    )
    
    
    :type TransformId: string
    :param TransformId: [REQUIRED]\nThe unique identifier of the machine learning transform.\n

    :type NextToken: string
    :param NextToken: A token for pagination of the results. The default is empty.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :type Filter: dict
    :param Filter: The filter criteria, in the TaskRunFilterCriteria structure, for the task run.\n\nTaskRunType (string) --The type of task run.\n\nStatus (string) --The current status of the task run.\n\nStartedBefore (datetime) --Filter on task runs started before this date.\n\nStartedAfter (datetime) --Filter on task runs started after this date.\n\n\n

    :type Sort: dict
    :param Sort: The sorting criteria, in the TaskRunSortCriteria structure, for the task run.\n\nColumn (string) -- [REQUIRED]The column to be used to sort the list of task runs for the machine learning transform.\n\nSortDirection (string) -- [REQUIRED]The sort direction to be used to sort the list of task runs for the machine learning transform.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TaskRuns': [
        {
            'TransformId': 'string',
            'TaskRunId': 'string',
            'Status': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
            'LogGroupName': 'string',
            'Properties': {
                'TaskType': 'EVALUATION'|'LABELING_SET_GENERATION'|'IMPORT_LABELS'|'EXPORT_LABELS'|'FIND_MATCHES',
                'ImportLabelsTaskRunProperties': {
                    'InputS3Path': 'string',
                    'Replace': True|False
                },
                'ExportLabelsTaskRunProperties': {
                    'OutputS3Path': 'string'
                },
                'LabelingSetGenerationTaskRunProperties': {
                    'OutputS3Path': 'string'
                },
                'FindMatchesTaskRunProperties': {
                    'JobId': 'string',
                    'JobName': 'string',
                    'JobRunId': 'string'
                }
            },
            'ErrorString': 'string',
            'StartedOn': datetime(2015, 1, 1),
            'LastModifiedOn': datetime(2015, 1, 1),
            'CompletedOn': datetime(2015, 1, 1),
            'ExecutionTime': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

TaskRuns (list) --
A list of task runs that are associated with the transform.

(dict) --
The sampling parameters that are associated with the machine learning transform.

TransformId (string) --
The unique identifier for the transform.

TaskRunId (string) --
The unique identifier for this task run.

Status (string) --
The current status of the requested task run.

LogGroupName (string) --
The names of the log group for secure logging, associated with this task run.

Properties (dict) --
Specifies configuration properties associated with this task run.

TaskType (string) --
The type of task run.

ImportLabelsTaskRunProperties (dict) --
The configuration properties for an importing labels task run.

InputS3Path (string) --
The Amazon Simple Storage Service (Amazon S3) path from where you will import the labels.

Replace (boolean) --
Indicates whether to overwrite your existing labels.



ExportLabelsTaskRunProperties (dict) --
The configuration properties for an exporting labels task run.

OutputS3Path (string) --
The Amazon Simple Storage Service (Amazon S3) path where you will export the labels.



LabelingSetGenerationTaskRunProperties (dict) --
The configuration properties for a labeling set generation task run.

OutputS3Path (string) --
The Amazon Simple Storage Service (Amazon S3) path where you will generate the labeling set.



FindMatchesTaskRunProperties (dict) --
The configuration properties for a find matches task run.

JobId (string) --
The job ID for the Find Matches task run.

JobName (string) --
The name assigned to the job for the Find Matches task run.

JobRunId (string) --
The job run ID for the Find Matches task run.





ErrorString (string) --
The list of error strings associated with this task run.

StartedOn (datetime) --
The date and time that this task run started.

LastModifiedOn (datetime) --
The last point in time that the requested task run was updated.

CompletedOn (datetime) --
The last point in time that the requested task run was completed.

ExecutionTime (integer) --
The amount of time (in seconds) that the task run consumed resources.





NextToken (string) --
A pagination token, if more results are available.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException


    :return: {
        'TaskRuns': [
            {
                'TransformId': 'string',
                'TaskRunId': 'string',
                'Status': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                'LogGroupName': 'string',
                'Properties': {
                    'TaskType': 'EVALUATION'|'LABELING_SET_GENERATION'|'IMPORT_LABELS'|'EXPORT_LABELS'|'FIND_MATCHES',
                    'ImportLabelsTaskRunProperties': {
                        'InputS3Path': 'string',
                        'Replace': True|False
                    },
                    'ExportLabelsTaskRunProperties': {
                        'OutputS3Path': 'string'
                    },
                    'LabelingSetGenerationTaskRunProperties': {
                        'OutputS3Path': 'string'
                    },
                    'FindMatchesTaskRunProperties': {
                        'JobId': 'string',
                        'JobName': 'string',
                        'JobRunId': 'string'
                    }
                },
                'ErrorString': 'string',
                'StartedOn': datetime(2015, 1, 1),
                'LastModifiedOn': datetime(2015, 1, 1),
                'CompletedOn': datetime(2015, 1, 1),
                'ExecutionTime': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.InternalServiceException
    
    """
    pass

def get_ml_transform(TransformId=None):
    """
    Gets an AWS Glue machine learning transform artifact and all its corresponding metadata. Machine learning transforms are a special type of transform that use machine learning to learn the details of the transformation to be performed by learning from examples provided by humans. These transformations are then saved by AWS Glue. You can retrieve their metadata by calling GetMLTransform .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_ml_transform(
        TransformId='string'
    )
    
    
    :type TransformId: string
    :param TransformId: [REQUIRED]\nThe unique identifier of the transform, generated at the time that the transform was created.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TransformId': 'string',
    'Name': 'string',
    'Description': 'string',
    'Status': 'NOT_READY'|'READY'|'DELETING',
    'CreatedOn': datetime(2015, 1, 1),
    'LastModifiedOn': datetime(2015, 1, 1),
    'InputRecordTables': [
        {
            'DatabaseName': 'string',
            'TableName': 'string',
            'CatalogId': 'string',
            'ConnectionName': 'string'
        },
    ],
    'Parameters': {
        'TransformType': 'FIND_MATCHES',
        'FindMatchesParameters': {
            'PrimaryKeyColumnName': 'string',
            'PrecisionRecallTradeoff': 123.0,
            'AccuracyCostTradeoff': 123.0,
            'EnforceProvidedLabels': True|False
        }
    },
    'EvaluationMetrics': {
        'TransformType': 'FIND_MATCHES',
        'FindMatchesMetrics': {
            'AreaUnderPRCurve': 123.0,
            'Precision': 123.0,
            'Recall': 123.0,
            'F1': 123.0,
            'ConfusionMatrix': {
                'NumTruePositives': 123,
                'NumFalsePositives': 123,
                'NumTrueNegatives': 123,
                'NumFalseNegatives': 123
            }
        }
    },
    'LabelCount': 123,
    'Schema': [
        {
            'Name': 'string',
            'DataType': 'string'
        },
    ],
    'Role': 'string',
    'GlueVersion': 'string',
    'MaxCapacity': 123.0,
    'WorkerType': 'Standard'|'G.1X'|'G.2X',
    'NumberOfWorkers': 123,
    'Timeout': 123,
    'MaxRetries': 123
}


Response Structure

(dict) --
TransformId (string) --The unique identifier of the transform, generated at the time that the transform was created.

Name (string) --The unique name given to the transform when it was created.

Description (string) --A description of the transform.

Status (string) --The last known status of the transform (to indicate whether it can be used or not). One of "NOT_READY", "READY", or "DELETING".

CreatedOn (datetime) --The date and time when the transform was created.

LastModifiedOn (datetime) --The date and time when the transform was last modified.

InputRecordTables (list) --A list of AWS Glue table definitions used by the transform.

(dict) --The database and table in the AWS Glue Data Catalog that is used for input or output data.

DatabaseName (string) --A database name in the AWS Glue Data Catalog.

TableName (string) --A table name in the AWS Glue Data Catalog.

CatalogId (string) --A unique identifier for the AWS Glue Data Catalog.

ConnectionName (string) --The name of the connection to the AWS Glue Data Catalog.





Parameters (dict) --The configuration parameters that are specific to the algorithm used.

TransformType (string) --The type of machine learning transform.
For information about the types of machine learning transforms, see Creating Machine Learning Transforms .

FindMatchesParameters (dict) --The parameters for the find matches algorithm.

PrimaryKeyColumnName (string) --The name of a column that uniquely identifies rows in the source table. Used to help identify matching records.

PrecisionRecallTradeoff (float) --The value selected when tuning your transform for a balance between precision and recall. A value of 0.5 means no preference; a value of 1.0 means a bias purely for precision, and a value of 0.0 means a bias for recall. Because this is a tradeoff, choosing values close to 1.0 means very low recall, and choosing values close to 0.0 results in very low precision.
The precision metric indicates how often your model is correct when it predicts a match.
The recall metric indicates that for an actual match, how often your model predicts the match.

AccuracyCostTradeoff (float) --The value that is selected when tuning your transform for a balance between accuracy and cost. A value of 0.5 means that the system balances accuracy and cost concerns. A value of 1.0 means a bias purely for accuracy, which typically results in a higher cost, sometimes substantially higher. A value of 0.0 means a bias purely for cost, which results in a less accurate FindMatches transform, sometimes with unacceptable accuracy.
Accuracy measures how well the transform finds true positives and true negatives. Increasing accuracy requires more machine resources and cost. But it also results in increased recall.
Cost measures how many compute resources, and thus money, are consumed to run the transform.

EnforceProvidedLabels (boolean) --The value to switch on or off to force the output to match the provided labels from users. If the value is True , the find matches transform forces the output to match the provided labels. The results override the normal conflation results. If the value is False , the find matches transform does not ensure all the labels provided are respected, and the results rely on the trained model.
Note that setting this value to true may increase the conflation execution time.





EvaluationMetrics (dict) --The latest evaluation metrics.

TransformType (string) --The type of machine learning transform.

FindMatchesMetrics (dict) --The evaluation metrics for the find matches algorithm.

AreaUnderPRCurve (float) --The area under the precision/recall curve (AUPRC) is a single number measuring the overall quality of the transform, that is independent of the choice made for precision vs. recall. Higher values indicate that you have a more attractive precision vs. recall tradeoff.
For more information, see Precision and recall in Wikipedia.

Precision (float) --The precision metric indicates when often your transform is correct when it predicts a match. Specifically, it measures how well the transform finds true positives from the total true positives possible.
For more information, see Precision and recall in Wikipedia.

Recall (float) --The recall metric indicates that for an actual match, how often your transform predicts the match. Specifically, it measures how well the transform finds true positives from the total records in the source data.
For more information, see Precision and recall in Wikipedia.

F1 (float) --The maximum F1 metric indicates the transform\'s accuracy between 0 and 1, where 1 is the best accuracy.
For more information, see F1 score in Wikipedia.

ConfusionMatrix (dict) --The confusion matrix shows you what your transform is predicting accurately and what types of errors it is making.
For more information, see Confusion matrix in Wikipedia.

NumTruePositives (integer) --The number of matches in the data that the transform correctly found, in the confusion matrix for your transform.

NumFalsePositives (integer) --The number of nonmatches in the data that the transform incorrectly classified as a match, in the confusion matrix for your transform.

NumTrueNegatives (integer) --The number of nonmatches in the data that the transform correctly rejected, in the confusion matrix for your transform.

NumFalseNegatives (integer) --The number of matches in the data that the transform didn\'t find, in the confusion matrix for your transform.







LabelCount (integer) --The number of labels available for this transform.

Schema (list) --The Map<Column, Type> object that represents the schema that this transform accepts. Has an upper bound of 100 columns.

(dict) --A key-value pair representing a column and data type that this transform can run against. The Schema parameter of the MLTransform may contain up to 100 of these structures.

Name (string) --The name of the column.

DataType (string) --The type of data in the column.





Role (string) --The name or Amazon Resource Name (ARN) of the IAM role with the required permissions.

GlueVersion (string) --This value determines which version of AWS Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see AWS Glue Versions in the developer guide.

MaxCapacity (float) --The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .
When the WorkerType field is set to a value other than Standard , the MaxCapacity field is set automatically and becomes read-only.

WorkerType (string) --The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
For the G.2X worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.


NumberOfWorkers (integer) --The number of workers of a defined workerType that are allocated when this task runs.

Timeout (integer) --The timeout for a task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours).

MaxRetries (integer) --The maximum number of times to retry a task for this transform after a task run fails.






Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException


    :return: {
        'TransformId': 'string',
        'Name': 'string',
        'Description': 'string',
        'Status': 'NOT_READY'|'READY'|'DELETING',
        'CreatedOn': datetime(2015, 1, 1),
        'LastModifiedOn': datetime(2015, 1, 1),
        'InputRecordTables': [
            {
                'DatabaseName': 'string',
                'TableName': 'string',
                'CatalogId': 'string',
                'ConnectionName': 'string'
            },
        ],
        'Parameters': {
            'TransformType': 'FIND_MATCHES',
            'FindMatchesParameters': {
                'PrimaryKeyColumnName': 'string',
                'PrecisionRecallTradeoff': 123.0,
                'AccuracyCostTradeoff': 123.0,
                'EnforceProvidedLabels': True|False
            }
        },
        'EvaluationMetrics': {
            'TransformType': 'FIND_MATCHES',
            'FindMatchesMetrics': {
                'AreaUnderPRCurve': 123.0,
                'Precision': 123.0,
                'Recall': 123.0,
                'F1': 123.0,
                'ConfusionMatrix': {
                    'NumTruePositives': 123,
                    'NumFalsePositives': 123,
                    'NumTrueNegatives': 123,
                    'NumFalseNegatives': 123
                }
            }
        },
        'LabelCount': 123,
        'Schema': [
            {
                'Name': 'string',
                'DataType': 'string'
            },
        ],
        'Role': 'string',
        'GlueVersion': 'string',
        'MaxCapacity': 123.0,
        'WorkerType': 'Standard'|'G.1X'|'G.2X',
        'NumberOfWorkers': 123,
        'Timeout': 123,
        'MaxRetries': 123
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.InternalServiceException
    
    """
    pass

def get_ml_transforms(NextToken=None, MaxResults=None, Filter=None, Sort=None):
    """
    Gets a sortable, filterable list of existing AWS Glue machine learning transforms. Machine learning transforms are a special type of transform that use machine learning to learn the details of the transformation to be performed by learning from examples provided by humans. These transformations are then saved by AWS Glue, and you can retrieve their metadata by calling GetMLTransforms .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_ml_transforms(
        NextToken='string',
        MaxResults=123,
        Filter={
            'Name': 'string',
            'TransformType': 'FIND_MATCHES',
            'Status': 'NOT_READY'|'READY'|'DELETING',
            'GlueVersion': 'string',
            'CreatedBefore': datetime(2015, 1, 1),
            'CreatedAfter': datetime(2015, 1, 1),
            'LastModifiedBefore': datetime(2015, 1, 1),
            'LastModifiedAfter': datetime(2015, 1, 1),
            'Schema': [
                {
                    'Name': 'string',
                    'DataType': 'string'
                },
            ]
        },
        Sort={
            'Column': 'NAME'|'TRANSFORM_TYPE'|'STATUS'|'CREATED'|'LAST_MODIFIED',
            'SortDirection': 'DESCENDING'|'ASCENDING'
        }
    )
    
    
    :type NextToken: string
    :param NextToken: A paginated token to offset the results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :type Filter: dict
    :param Filter: The filter transformation criteria.\n\nName (string) --A unique transform name that is used to filter the machine learning transforms.\n\nTransformType (string) --The type of machine learning transform that is used to filter the machine learning transforms.\n\nStatus (string) --Filters the list of machine learning transforms by the last known status of the transforms (to indicate whether a transform can be used or not). One of 'NOT_READY', 'READY', or 'DELETING'.\n\nGlueVersion (string) --This value determines which version of AWS Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see AWS Glue Versions in the developer guide.\n\nCreatedBefore (datetime) --The time and date before which the transforms were created.\n\nCreatedAfter (datetime) --The time and date after which the transforms were created.\n\nLastModifiedBefore (datetime) --Filter on transforms last modified before this date.\n\nLastModifiedAfter (datetime) --Filter on transforms last modified after this date.\n\nSchema (list) --Filters on datasets with a specific schema. The Map<Column, Type> object is an array of key-value pairs representing the schema this transform accepts, where Column is the name of a column, and Type is the type of the data such as an integer or string. Has an upper bound of 100 columns.\n\n(dict) --A key-value pair representing a column and data type that this transform can run against. The Schema parameter of the MLTransform may contain up to 100 of these structures.\n\nName (string) --The name of the column.\n\nDataType (string) --The type of data in the column.\n\n\n\n\n\n\n

    :type Sort: dict
    :param Sort: The sorting criteria.\n\nColumn (string) -- [REQUIRED]The column to be used in the sorting criteria that are associated with the machine learning transform.\n\nSortDirection (string) -- [REQUIRED]The sort direction to be used in the sorting criteria that are associated with the machine learning transform.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Transforms': [
        {
            'TransformId': 'string',
            'Name': 'string',
            'Description': 'string',
            'Status': 'NOT_READY'|'READY'|'DELETING',
            'CreatedOn': datetime(2015, 1, 1),
            'LastModifiedOn': datetime(2015, 1, 1),
            'InputRecordTables': [
                {
                    'DatabaseName': 'string',
                    'TableName': 'string',
                    'CatalogId': 'string',
                    'ConnectionName': 'string'
                },
            ],
            'Parameters': {
                'TransformType': 'FIND_MATCHES',
                'FindMatchesParameters': {
                    'PrimaryKeyColumnName': 'string',
                    'PrecisionRecallTradeoff': 123.0,
                    'AccuracyCostTradeoff': 123.0,
                    'EnforceProvidedLabels': True|False
                }
            },
            'EvaluationMetrics': {
                'TransformType': 'FIND_MATCHES',
                'FindMatchesMetrics': {
                    'AreaUnderPRCurve': 123.0,
                    'Precision': 123.0,
                    'Recall': 123.0,
                    'F1': 123.0,
                    'ConfusionMatrix': {
                        'NumTruePositives': 123,
                        'NumFalsePositives': 123,
                        'NumTrueNegatives': 123,
                        'NumFalseNegatives': 123
                    }
                }
            },
            'LabelCount': 123,
            'Schema': [
                {
                    'Name': 'string',
                    'DataType': 'string'
                },
            ],
            'Role': 'string',
            'GlueVersion': 'string',
            'MaxCapacity': 123.0,
            'WorkerType': 'Standard'|'G.1X'|'G.2X',
            'NumberOfWorkers': 123,
            'Timeout': 123,
            'MaxRetries': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Transforms (list) --
A list of machine learning transforms.

(dict) --
A structure for a machine learning transform.

TransformId (string) --
The unique transform ID that is generated for the machine learning transform. The ID is guaranteed to be unique and does not change.

Name (string) --
A user-defined name for the machine learning transform. Names are not guaranteed unique and can be changed at any time.

Description (string) --
A user-defined, long-form description text for the machine learning transform. Descriptions are not guaranteed to be unique and can be changed at any time.

Status (string) --
The current status of the machine learning transform.

CreatedOn (datetime) --
A timestamp. The time and date that this machine learning transform was created.

LastModifiedOn (datetime) --
A timestamp. The last point in time when this machine learning transform was modified.

InputRecordTables (list) --
A list of AWS Glue table definitions used by the transform.

(dict) --
The database and table in the AWS Glue Data Catalog that is used for input or output data.

DatabaseName (string) --
A database name in the AWS Glue Data Catalog.

TableName (string) --
A table name in the AWS Glue Data Catalog.

CatalogId (string) --
A unique identifier for the AWS Glue Data Catalog.

ConnectionName (string) --
The name of the connection to the AWS Glue Data Catalog.





Parameters (dict) --
A TransformParameters object. You can use parameters to tune (customize) the behavior of the machine learning transform by specifying what data it learns from and your preference on various tradeoffs (such as precious vs. recall, or accuracy vs. cost).

TransformType (string) --
The type of machine learning transform.
For information about the types of machine learning transforms, see Creating Machine Learning Transforms .

FindMatchesParameters (dict) --
The parameters for the find matches algorithm.

PrimaryKeyColumnName (string) --
The name of a column that uniquely identifies rows in the source table. Used to help identify matching records.

PrecisionRecallTradeoff (float) --
The value selected when tuning your transform for a balance between precision and recall. A value of 0.5 means no preference; a value of 1.0 means a bias purely for precision, and a value of 0.0 means a bias for recall. Because this is a tradeoff, choosing values close to 1.0 means very low recall, and choosing values close to 0.0 results in very low precision.
The precision metric indicates how often your model is correct when it predicts a match.
The recall metric indicates that for an actual match, how often your model predicts the match.

AccuracyCostTradeoff (float) --
The value that is selected when tuning your transform for a balance between accuracy and cost. A value of 0.5 means that the system balances accuracy and cost concerns. A value of 1.0 means a bias purely for accuracy, which typically results in a higher cost, sometimes substantially higher. A value of 0.0 means a bias purely for cost, which results in a less accurate FindMatches transform, sometimes with unacceptable accuracy.
Accuracy measures how well the transform finds true positives and true negatives. Increasing accuracy requires more machine resources and cost. But it also results in increased recall.
Cost measures how many compute resources, and thus money, are consumed to run the transform.

EnforceProvidedLabels (boolean) --
The value to switch on or off to force the output to match the provided labels from users. If the value is True , the find matches transform forces the output to match the provided labels. The results override the normal conflation results. If the value is False , the find matches transform does not ensure all the labels provided are respected, and the results rely on the trained model.
Note that setting this value to true may increase the conflation execution time.





EvaluationMetrics (dict) --
An EvaluationMetrics object. Evaluation metrics provide an estimate of the quality of your machine learning transform.

TransformType (string) --
The type of machine learning transform.

FindMatchesMetrics (dict) --
The evaluation metrics for the find matches algorithm.

AreaUnderPRCurve (float) --
The area under the precision/recall curve (AUPRC) is a single number measuring the overall quality of the transform, that is independent of the choice made for precision vs. recall. Higher values indicate that you have a more attractive precision vs. recall tradeoff.
For more information, see Precision and recall in Wikipedia.

Precision (float) --
The precision metric indicates when often your transform is correct when it predicts a match. Specifically, it measures how well the transform finds true positives from the total true positives possible.
For more information, see Precision and recall in Wikipedia.

Recall (float) --
The recall metric indicates that for an actual match, how often your transform predicts the match. Specifically, it measures how well the transform finds true positives from the total records in the source data.
For more information, see Precision and recall in Wikipedia.

F1 (float) --
The maximum F1 metric indicates the transform\'s accuracy between 0 and 1, where 1 is the best accuracy.
For more information, see F1 score in Wikipedia.

ConfusionMatrix (dict) --
The confusion matrix shows you what your transform is predicting accurately and what types of errors it is making.
For more information, see Confusion matrix in Wikipedia.

NumTruePositives (integer) --
The number of matches in the data that the transform correctly found, in the confusion matrix for your transform.

NumFalsePositives (integer) --
The number of nonmatches in the data that the transform incorrectly classified as a match, in the confusion matrix for your transform.

NumTrueNegatives (integer) --
The number of nonmatches in the data that the transform correctly rejected, in the confusion matrix for your transform.

NumFalseNegatives (integer) --
The number of matches in the data that the transform didn\'t find, in the confusion matrix for your transform.







LabelCount (integer) --
A count identifier for the labeling files generated by AWS Glue for this transform. As you create a better transform, you can iteratively download, label, and upload the labeling file.

Schema (list) --
A map of key-value pairs representing the columns and data types that this transform can run against. Has an upper bound of 100 columns.

(dict) --
A key-value pair representing a column and data type that this transform can run against. The Schema parameter of the MLTransform may contain up to 100 of these structures.

Name (string) --
The name of the column.

DataType (string) --
The type of data in the column.





Role (string) --
The name or Amazon Resource Name (ARN) of the IAM role with the required permissions. The required permissions include both AWS Glue service role permissions to AWS Glue resources, and Amazon S3 permissions required by the transform.

This role needs AWS Glue service role permissions to allow access to resources in AWS Glue. See Attach a Policy to IAM Users That Access AWS Glue .
This role needs permission to your Amazon Simple Storage Service (Amazon S3) sources, targets, temporary directory, scripts, and any libraries used by the task run for this transform.


GlueVersion (string) --
This value determines which version of AWS Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see AWS Glue Versions in the developer guide.

MaxCapacity (float) --
The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .

MaxCapacity is a mutually exclusive option with NumberOfWorkers and WorkerType .


If either NumberOfWorkers or WorkerType is set, then MaxCapacity cannot be set.
If MaxCapacity is set then neither NumberOfWorkers or WorkerType can be set.
If WorkerType is set, then NumberOfWorkers is required (and vice versa).
MaxCapacity and NumberOfWorkers must both be at least 1.

When the WorkerType field is set to a value other than Standard , the MaxCapacity field is set automatically and becomes read-only.

WorkerType (string) --
The type of predefined worker that is allocated when a task of this transform runs. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
For the G.2X worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.


MaxCapacity is a mutually exclusive option with NumberOfWorkers and WorkerType .


If either NumberOfWorkers or WorkerType is set, then MaxCapacity cannot be set.
If MaxCapacity is set then neither NumberOfWorkers or WorkerType can be set.
If WorkerType is set, then NumberOfWorkers is required (and vice versa).
MaxCapacity and NumberOfWorkers must both be at least 1.


NumberOfWorkers (integer) --
The number of workers of a defined workerType that are allocated when a task of the transform runs.
If WorkerType is set, then NumberOfWorkers is required (and vice versa).

Timeout (integer) --
The timeout in minutes of the machine learning transform.

MaxRetries (integer) --
The maximum number of times to retry after an MLTaskRun of the machine learning transform fails.





NextToken (string) --
A pagination token, if more results are available.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException


    :return: {
        'Transforms': [
            {
                'TransformId': 'string',
                'Name': 'string',
                'Description': 'string',
                'Status': 'NOT_READY'|'READY'|'DELETING',
                'CreatedOn': datetime(2015, 1, 1),
                'LastModifiedOn': datetime(2015, 1, 1),
                'InputRecordTables': [
                    {
                        'DatabaseName': 'string',
                        'TableName': 'string',
                        'CatalogId': 'string',
                        'ConnectionName': 'string'
                    },
                ],
                'Parameters': {
                    'TransformType': 'FIND_MATCHES',
                    'FindMatchesParameters': {
                        'PrimaryKeyColumnName': 'string',
                        'PrecisionRecallTradeoff': 123.0,
                        'AccuracyCostTradeoff': 123.0,
                        'EnforceProvidedLabels': True|False
                    }
                },
                'EvaluationMetrics': {
                    'TransformType': 'FIND_MATCHES',
                    'FindMatchesMetrics': {
                        'AreaUnderPRCurve': 123.0,
                        'Precision': 123.0,
                        'Recall': 123.0,
                        'F1': 123.0,
                        'ConfusionMatrix': {
                            'NumTruePositives': 123,
                            'NumFalsePositives': 123,
                            'NumTrueNegatives': 123,
                            'NumFalseNegatives': 123
                        }
                    }
                },
                'LabelCount': 123,
                'Schema': [
                    {
                        'Name': 'string',
                        'DataType': 'string'
                    },
                ],
                'Role': 'string',
                'GlueVersion': 'string',
                'MaxCapacity': 123.0,
                'WorkerType': 'Standard'|'G.1X'|'G.2X',
                'NumberOfWorkers': 123,
                'Timeout': 123,
                'MaxRetries': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    This role needs AWS Glue service role permissions to allow access to resources in AWS Glue. See Attach a Policy to IAM Users That Access AWS Glue .
    This role needs permission to your Amazon Simple Storage Service (Amazon S3) sources, targets, temporary directory, scripts, and any libraries used by the task run for this transform.
    
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

def get_partition(CatalogId=None, DatabaseName=None, TableName=None, PartitionValues=None):
    """
    Retrieves information about a specified partition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_partition(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        PartitionValues=[
            'string',
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the partition in question resides. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the catalog database where the partition resides.\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the partition\'s table.\n

    :type PartitionValues: list
    :param PartitionValues: [REQUIRED]\nThe values that define the partition.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Partition': {
        'Values': [
            'string',
        ],
        'DatabaseName': 'string',
        'TableName': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'LastAccessTime': datetime(2015, 1, 1),
        'StorageDescriptor': {
            'Columns': [
                {
                    'Name': 'string',
                    'Type': 'string',
                    'Comment': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
            ],
            'Location': 'string',
            'InputFormat': 'string',
            'OutputFormat': 'string',
            'Compressed': True|False,
            'NumberOfBuckets': 123,
            'SerdeInfo': {
                'Name': 'string',
                'SerializationLibrary': 'string',
                'Parameters': {
                    'string': 'string'
                }
            },
            'BucketColumns': [
                'string',
            ],
            'SortColumns': [
                {
                    'Column': 'string',
                    'SortOrder': 123
                },
            ],
            'Parameters': {
                'string': 'string'
            },
            'SkewedInfo': {
                'SkewedColumnNames': [
                    'string',
                ],
                'SkewedColumnValues': [
                    'string',
                ],
                'SkewedColumnValueLocationMaps': {
                    'string': 'string'
                }
            },
            'StoredAsSubDirectories': True|False
        },
        'Parameters': {
            'string': 'string'
        },
        'LastAnalyzedTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Partition (dict) --
The requested information, in the form of a Partition object.

Values (list) --
The values of the partition.

(string) --


DatabaseName (string) --
The name of the catalog database in which to create the partition.

TableName (string) --
The name of the database table in which to create the partition.

CreationTime (datetime) --
The time at which the partition was created.

LastAccessTime (datetime) --
The last time at which the partition was accessed.

StorageDescriptor (dict) --
Provides information about the physical location where the partition is stored.

Columns (list) --
A list of the Columns in the table.

(dict) --
A column in a Table .

Name (string) --
The name of the Column .

Type (string) --
The data type of the Column .

Comment (string) --
A free-form text comment.

Parameters (dict) --
These key-value pairs define properties associated with the column.

(string) --
(string) --








Location (string) --
The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

InputFormat (string) --
The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.

OutputFormat (string) --
The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.

Compressed (boolean) --

True if the data in the table is compressed, or False if not.


NumberOfBuckets (integer) --
Must be specified if the table contains any dimension columns.

SerdeInfo (dict) --
The serialization/deserialization (SerDe) information.

Name (string) --
Name of the SerDe.

SerializationLibrary (string) --
Usually the class that implements the SerDe. An example is org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .

Parameters (dict) --
These key-value pairs define initialization parameters for the SerDe.

(string) --
(string) --






BucketColumns (list) --
A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

(string) --


SortColumns (list) --
A list specifying the sort order of each bucket in the table.

(dict) --
Specifies the sort order of a sorted column.

Column (string) --
The name of the column.

SortOrder (integer) --
Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).





Parameters (dict) --
The user-supplied properties in key-value form.

(string) --
(string) --




SkewedInfo (dict) --
The information about values that appear frequently in a column (skewed values).

SkewedColumnNames (list) --
A list of names of columns that contain skewed values.

(string) --


SkewedColumnValues (list) --
A list of values that appear so frequently as to be considered skewed.

(string) --


SkewedColumnValueLocationMaps (dict) --
A mapping of skewed values to the columns that contain them.

(string) --
(string) --






StoredAsSubDirectories (boolean) --

True if the table data is stored in subdirectories, or False if not.




Parameters (dict) --
These key-value pairs define partition parameters.

(string) --
(string) --




LastAnalyzedTime (datetime) --
The last time at which column statistics were computed for this partition.









Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.GlueEncryptionException


    :return: {
        'Partition': {
            'Values': [
                'string',
            ],
            'DatabaseName': 'string',
            'TableName': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'LastAccessTime': datetime(2015, 1, 1),
            'StorageDescriptor': {
                'Columns': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'Location': 'string',
                'InputFormat': 'string',
                'OutputFormat': 'string',
                'Compressed': True|False,
                'NumberOfBuckets': 123,
                'SerdeInfo': {
                    'Name': 'string',
                    'SerializationLibrary': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
                'BucketColumns': [
                    'string',
                ],
                'SortColumns': [
                    {
                        'Column': 'string',
                        'SortOrder': 123
                    },
                ],
                'Parameters': {
                    'string': 'string'
                },
                'SkewedInfo': {
                    'SkewedColumnNames': [
                        'string',
                    ],
                    'SkewedColumnValues': [
                        'string',
                    ],
                    'SkewedColumnValueLocationMaps': {
                        'string': 'string'
                    }
                },
                'StoredAsSubDirectories': True|False
            },
            'Parameters': {
                'string': 'string'
            },
            'LastAnalyzedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_partitions(CatalogId=None, DatabaseName=None, TableName=None, Expression=None, NextToken=None, Segment=None, MaxResults=None):
    """
    Retrieves information about the partitions in a table.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_partitions(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        Expression='string',
        NextToken='string',
        Segment={
            'SegmentNumber': 123,
            'TotalSegments': 123
        },
        MaxResults=123
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the partitions in question reside. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the catalog database where the partitions reside.\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the partitions\' table.\n

    :type Expression: string
    :param Expression: An expression that filters the partitions to be returned.\nThe expression uses SQL syntax similar to the SQL WHERE filter clause. The SQL statement parser JSQLParser parses the expression.\n\nOperators : The following are the operators that you can use in the Expression API call:\n=\n\nChecks whether the values of the two operands are equal; if yes, then the condition becomes true.\nExample: Assume \'variable a\' holds 10 and \'variable b\' holds 20.\n(a = b) is not true.\n\n< >\nChecks whether the values of two operands are equal; if the values are not equal, then the condition becomes true.\nExample: (a < > b) is true.\n\n>\nChecks whether the value of the left operand is greater than the value of the right operand; if yes, then the condition becomes true.\nExample: (a > b) is not true.\n\n<\nChecks whether the value of the left operand is less than the value of the right operand; if yes, then the condition becomes true.\nExample: (a < b) is true.\n\n>=\nChecks whether the value of the left operand is greater than or equal to the value of the right operand; if yes, then the condition becomes true.\nExample: (a >= b) is not true.\n\n<=\nChecks whether the value of the left operand is less than or equal to the value of the right operand; if yes, then the condition becomes true.\nExample: (a <= b) is true.\n\nAND, OR, IN, BETWEEN, LIKE, NOT, IS NULL\nLogical operators.\n\nSupported Partition Key Types : The following are the supported partition keys.\n\nstring\ndate\ntimestamp\nint\nbigint\nlong\ntinyint\nsmallint\ndecimal\n\nIf an invalid type is encountered, an exception is thrown.\nThe following list shows the valid operators on each type. When you define a crawler, the partitionKey type is created as a STRING , to be compatible with the catalog partitions.\n\nSample API Call :\n

    :type NextToken: string
    :param NextToken: A continuation token, if this is not the first call to retrieve these partitions.

    :type Segment: dict
    :param Segment: The segment of the table\'s partitions to scan in this request.\n\nSegmentNumber (integer) -- [REQUIRED]The zero-based index number of the segment. For example, if the total number of segments is 4, SegmentNumber values range from 0 through 3.\n\nTotalSegments (integer) -- [REQUIRED]The total number of segments.\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of partitions to return in a single response.

    :rtype: dict

ReturnsResponse Syntax
{
    'Partitions': [
        {
            'Values': [
                'string',
            ],
            'DatabaseName': 'string',
            'TableName': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'LastAccessTime': datetime(2015, 1, 1),
            'StorageDescriptor': {
                'Columns': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'Location': 'string',
                'InputFormat': 'string',
                'OutputFormat': 'string',
                'Compressed': True|False,
                'NumberOfBuckets': 123,
                'SerdeInfo': {
                    'Name': 'string',
                    'SerializationLibrary': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
                'BucketColumns': [
                    'string',
                ],
                'SortColumns': [
                    {
                        'Column': 'string',
                        'SortOrder': 123
                    },
                ],
                'Parameters': {
                    'string': 'string'
                },
                'SkewedInfo': {
                    'SkewedColumnNames': [
                        'string',
                    ],
                    'SkewedColumnValues': [
                        'string',
                    ],
                    'SkewedColumnValueLocationMaps': {
                        'string': 'string'
                    }
                },
                'StoredAsSubDirectories': True|False
            },
            'Parameters': {
                'string': 'string'
            },
            'LastAnalyzedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Partitions (list) --
A list of requested partitions.

(dict) --
Represents a slice of table data.

Values (list) --
The values of the partition.

(string) --


DatabaseName (string) --
The name of the catalog database in which to create the partition.

TableName (string) --
The name of the database table in which to create the partition.

CreationTime (datetime) --
The time at which the partition was created.

LastAccessTime (datetime) --
The last time at which the partition was accessed.

StorageDescriptor (dict) --
Provides information about the physical location where the partition is stored.

Columns (list) --
A list of the Columns in the table.

(dict) --
A column in a Table .

Name (string) --
The name of the Column .

Type (string) --
The data type of the Column .

Comment (string) --
A free-form text comment.

Parameters (dict) --
These key-value pairs define properties associated with the column.

(string) --
(string) --








Location (string) --
The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

InputFormat (string) --
The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.

OutputFormat (string) --
The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.

Compressed (boolean) --

True if the data in the table is compressed, or False if not.


NumberOfBuckets (integer) --
Must be specified if the table contains any dimension columns.

SerdeInfo (dict) --
The serialization/deserialization (SerDe) information.

Name (string) --
Name of the SerDe.

SerializationLibrary (string) --
Usually the class that implements the SerDe. An example is org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .

Parameters (dict) --
These key-value pairs define initialization parameters for the SerDe.

(string) --
(string) --






BucketColumns (list) --
A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

(string) --


SortColumns (list) --
A list specifying the sort order of each bucket in the table.

(dict) --
Specifies the sort order of a sorted column.

Column (string) --
The name of the column.

SortOrder (integer) --
Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).





Parameters (dict) --
The user-supplied properties in key-value form.

(string) --
(string) --




SkewedInfo (dict) --
The information about values that appear frequently in a column (skewed values).

SkewedColumnNames (list) --
A list of names of columns that contain skewed values.

(string) --


SkewedColumnValues (list) --
A list of values that appear so frequently as to be considered skewed.

(string) --


SkewedColumnValueLocationMaps (dict) --
A mapping of skewed values to the columns that contain them.

(string) --
(string) --






StoredAsSubDirectories (boolean) --

True if the table data is stored in subdirectories, or False if not.




Parameters (dict) --
These key-value pairs define partition parameters.

(string) --
(string) --




LastAnalyzedTime (datetime) --
The last time at which column statistics were computed for this partition.





NextToken (string) --
A continuation token, if the returned list of partitions does not include the last one.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.GlueEncryptionException


    :return: {
        'Partitions': [
            {
                'Values': [
                    'string',
                ],
                'DatabaseName': 'string',
                'TableName': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastAccessTime': datetime(2015, 1, 1),
                'StorageDescriptor': {
                    'Columns': [
                        {
                            'Name': 'string',
                            'Type': 'string',
                            'Comment': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                    ],
                    'Location': 'string',
                    'InputFormat': 'string',
                    'OutputFormat': 'string',
                    'Compressed': True|False,
                    'NumberOfBuckets': 123,
                    'SerdeInfo': {
                        'Name': 'string',
                        'SerializationLibrary': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                    'BucketColumns': [
                        'string',
                    ],
                    'SortColumns': [
                        {
                            'Column': 'string',
                            'SortOrder': 123
                        },
                    ],
                    'Parameters': {
                        'string': 'string'
                    },
                    'SkewedInfo': {
                        'SkewedColumnNames': [
                            'string',
                        ],
                        'SkewedColumnValues': [
                            'string',
                        ],
                        'SkewedColumnValueLocationMaps': {
                            'string': 'string'
                        }
                    },
                    'StoredAsSubDirectories': True|False
                },
                'Parameters': {
                    'string': 'string'
                },
                'LastAnalyzedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_plan(Mapping=None, Source=None, Sinks=None, Location=None, Language=None):
    """
    Gets code to perform a specified mapping.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_plan(
        Mapping=[
            {
                'SourceTable': 'string',
                'SourcePath': 'string',
                'SourceType': 'string',
                'TargetTable': 'string',
                'TargetPath': 'string',
                'TargetType': 'string'
            },
        ],
        Source={
            'DatabaseName': 'string',
            'TableName': 'string'
        },
        Sinks=[
            {
                'DatabaseName': 'string',
                'TableName': 'string'
            },
        ],
        Location={
            'Jdbc': [
                {
                    'Name': 'string',
                    'Value': 'string',
                    'Param': True|False
                },
            ],
            'S3': [
                {
                    'Name': 'string',
                    'Value': 'string',
                    'Param': True|False
                },
            ],
            'DynamoDB': [
                {
                    'Name': 'string',
                    'Value': 'string',
                    'Param': True|False
                },
            ]
        },
        Language='PYTHON'|'SCALA'
    )
    
    
    :type Mapping: list
    :param Mapping: [REQUIRED]\nThe list of mappings from a source table to target tables.\n\n(dict) --Defines a mapping.\n\nSourceTable (string) --The name of the source table.\n\nSourcePath (string) --The source path.\n\nSourceType (string) --The source type.\n\nTargetTable (string) --The target table.\n\nTargetPath (string) --The target path.\n\nTargetType (string) --The target type.\n\n\n\n\n

    :type Source: dict
    :param Source: [REQUIRED]\nThe source table.\n\nDatabaseName (string) -- [REQUIRED]The database in which the table metadata resides.\n\nTableName (string) -- [REQUIRED]The name of the table in question.\n\n\n

    :type Sinks: list
    :param Sinks: The target tables.\n\n(dict) --Specifies a table definition in the AWS Glue Data Catalog.\n\nDatabaseName (string) -- [REQUIRED]The database in which the table metadata resides.\n\nTableName (string) -- [REQUIRED]The name of the table in question.\n\n\n\n\n

    :type Location: dict
    :param Location: The parameters for the mapping.\n\nJdbc (list) --A JDBC location.\n\n(dict) --An argument or property of a node.\n\nName (string) -- [REQUIRED]The name of the argument or property.\n\nValue (string) -- [REQUIRED]The value of the argument or property.\n\nParam (boolean) --True if the value is used as a parameter.\n\n\n\n\n\nS3 (list) --An Amazon Simple Storage Service (Amazon S3) location.\n\n(dict) --An argument or property of a node.\n\nName (string) -- [REQUIRED]The name of the argument or property.\n\nValue (string) -- [REQUIRED]The value of the argument or property.\n\nParam (boolean) --True if the value is used as a parameter.\n\n\n\n\n\nDynamoDB (list) --An Amazon DynamoDB table location.\n\n(dict) --An argument or property of a node.\n\nName (string) -- [REQUIRED]The name of the argument or property.\n\nValue (string) -- [REQUIRED]The value of the argument or property.\n\nParam (boolean) --True if the value is used as a parameter.\n\n\n\n\n\n\n

    :type Language: string
    :param Language: The programming language of the code to perform the mapping.

    :rtype: dict

ReturnsResponse Syntax
{
    'PythonScript': 'string',
    'ScalaCode': 'string'
}


Response Structure

(dict) --

PythonScript (string) --
A Python script to perform the mapping.

ScalaCode (string) --
The Scala code to perform the mapping.







Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'PythonScript': 'string',
        'ScalaCode': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def get_resource_policy():
    """
    Retrieves a specified resource policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resource_policy()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'PolicyInJson': 'string',
    'PolicyHash': 'string',
    'CreateTime': datetime(2015, 1, 1),
    'UpdateTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --
PolicyInJson (string) --Contains the requested policy document, in JSON format.

PolicyHash (string) --Contains the hash value associated with this policy.

CreateTime (datetime) --The date and time at which the policy was created.

UpdateTime (datetime) --The date and time at which the policy was last updated.






Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException


    :return: {
        'PolicyInJson': 'string',
        'PolicyHash': 'string',
        'CreateTime': datetime(2015, 1, 1),
        'UpdateTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def get_security_configuration(Name=None):
    """
    Retrieves a specified security configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_security_configuration(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the security configuration to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'SecurityConfiguration': {
        'Name': 'string',
        'CreatedTimeStamp': datetime(2015, 1, 1),
        'EncryptionConfiguration': {
            'S3Encryption': [
                {
                    'S3EncryptionMode': 'DISABLED'|'SSE-KMS'|'SSE-S3',
                    'KmsKeyArn': 'string'
                },
            ],
            'CloudWatchEncryption': {
                'CloudWatchEncryptionMode': 'DISABLED'|'SSE-KMS',
                'KmsKeyArn': 'string'
            },
            'JobBookmarksEncryption': {
                'JobBookmarksEncryptionMode': 'DISABLED'|'CSE-KMS',
                'KmsKeyArn': 'string'
            }
        }
    }
}


Response Structure

(dict) --
SecurityConfiguration (dict) --The requested security configuration.

Name (string) --The name of the security configuration.

CreatedTimeStamp (datetime) --The time at which this security configuration was created.

EncryptionConfiguration (dict) --The encryption configuration associated with this security configuration.

S3Encryption (list) --The encryption configuration for Amazon Simple Storage Service (Amazon S3) data.

(dict) --Specifies how Amazon Simple Storage Service (Amazon S3) data should be encrypted.

S3EncryptionMode (string) --The encryption mode to use for Amazon S3 data.

KmsKeyArn (string) --The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.





CloudWatchEncryption (dict) --The encryption configuration for Amazon CloudWatch.

CloudWatchEncryptionMode (string) --The encryption mode to use for CloudWatch data.

KmsKeyArn (string) --The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.



JobBookmarksEncryption (dict) --The encryption configuration for job bookmarks.

JobBookmarksEncryptionMode (string) --The encryption mode to use for job bookmarks data.

KmsKeyArn (string) --The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.












Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'SecurityConfiguration': {
            'Name': 'string',
            'CreatedTimeStamp': datetime(2015, 1, 1),
            'EncryptionConfiguration': {
                'S3Encryption': [
                    {
                        'S3EncryptionMode': 'DISABLED'|'SSE-KMS'|'SSE-S3',
                        'KmsKeyArn': 'string'
                    },
                ],
                'CloudWatchEncryption': {
                    'CloudWatchEncryptionMode': 'DISABLED'|'SSE-KMS',
                    'KmsKeyArn': 'string'
                },
                'JobBookmarksEncryption': {
                    'JobBookmarksEncryptionMode': 'DISABLED'|'CSE-KMS',
                    'KmsKeyArn': 'string'
                }
            }
        }
    }
    
    
    """
    pass

def get_security_configurations(MaxResults=None, NextToken=None):
    """
    Retrieves a list of all security configurations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_security_configurations(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :rtype: dict

ReturnsResponse Syntax
{
    'SecurityConfigurations': [
        {
            'Name': 'string',
            'CreatedTimeStamp': datetime(2015, 1, 1),
            'EncryptionConfiguration': {
                'S3Encryption': [
                    {
                        'S3EncryptionMode': 'DISABLED'|'SSE-KMS'|'SSE-S3',
                        'KmsKeyArn': 'string'
                    },
                ],
                'CloudWatchEncryption': {
                    'CloudWatchEncryptionMode': 'DISABLED'|'SSE-KMS',
                    'KmsKeyArn': 'string'
                },
                'JobBookmarksEncryption': {
                    'JobBookmarksEncryptionMode': 'DISABLED'|'CSE-KMS',
                    'KmsKeyArn': 'string'
                }
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SecurityConfigurations (list) --
A list of security configurations.

(dict) --
Specifies a security configuration.

Name (string) --
The name of the security configuration.

CreatedTimeStamp (datetime) --
The time at which this security configuration was created.

EncryptionConfiguration (dict) --
The encryption configuration associated with this security configuration.

S3Encryption (list) --
The encryption configuration for Amazon Simple Storage Service (Amazon S3) data.

(dict) --
Specifies how Amazon Simple Storage Service (Amazon S3) data should be encrypted.

S3EncryptionMode (string) --
The encryption mode to use for Amazon S3 data.

KmsKeyArn (string) --
The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.





CloudWatchEncryption (dict) --
The encryption configuration for Amazon CloudWatch.

CloudWatchEncryptionMode (string) --
The encryption mode to use for CloudWatch data.

KmsKeyArn (string) --
The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.



JobBookmarksEncryption (dict) --
The encryption configuration for job bookmarks.

JobBookmarksEncryptionMode (string) --
The encryption mode to use for job bookmarks data.

KmsKeyArn (string) --
The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.









NextToken (string) --
A continuation token, if there are more security configurations to return.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'SecurityConfigurations': [
            {
                'Name': 'string',
                'CreatedTimeStamp': datetime(2015, 1, 1),
                'EncryptionConfiguration': {
                    'S3Encryption': [
                        {
                            'S3EncryptionMode': 'DISABLED'|'SSE-KMS'|'SSE-S3',
                            'KmsKeyArn': 'string'
                        },
                    ],
                    'CloudWatchEncryption': {
                        'CloudWatchEncryptionMode': 'DISABLED'|'SSE-KMS',
                        'KmsKeyArn': 'string'
                    },
                    'JobBookmarksEncryption': {
                        'JobBookmarksEncryptionMode': 'DISABLED'|'CSE-KMS',
                        'KmsKeyArn': 'string'
                    }
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def get_table(CatalogId=None, DatabaseName=None, Name=None):
    """
    Retrieves the Table definition in a Data Catalog for a specified table.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_table(
        CatalogId='string',
        DatabaseName='string',
        Name='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the table resides. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the table for which to retrieve the definition. For Hive compatibility, this name is entirely lowercase.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Table': {
        'Name': 'string',
        'DatabaseName': 'string',
        'Description': 'string',
        'Owner': 'string',
        'CreateTime': datetime(2015, 1, 1),
        'UpdateTime': datetime(2015, 1, 1),
        'LastAccessTime': datetime(2015, 1, 1),
        'LastAnalyzedTime': datetime(2015, 1, 1),
        'Retention': 123,
        'StorageDescriptor': {
            'Columns': [
                {
                    'Name': 'string',
                    'Type': 'string',
                    'Comment': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
            ],
            'Location': 'string',
            'InputFormat': 'string',
            'OutputFormat': 'string',
            'Compressed': True|False,
            'NumberOfBuckets': 123,
            'SerdeInfo': {
                'Name': 'string',
                'SerializationLibrary': 'string',
                'Parameters': {
                    'string': 'string'
                }
            },
            'BucketColumns': [
                'string',
            ],
            'SortColumns': [
                {
                    'Column': 'string',
                    'SortOrder': 123
                },
            ],
            'Parameters': {
                'string': 'string'
            },
            'SkewedInfo': {
                'SkewedColumnNames': [
                    'string',
                ],
                'SkewedColumnValues': [
                    'string',
                ],
                'SkewedColumnValueLocationMaps': {
                    'string': 'string'
                }
            },
            'StoredAsSubDirectories': True|False
        },
        'PartitionKeys': [
            {
                'Name': 'string',
                'Type': 'string',
                'Comment': 'string',
                'Parameters': {
                    'string': 'string'
                }
            },
        ],
        'ViewOriginalText': 'string',
        'ViewExpandedText': 'string',
        'TableType': 'string',
        'Parameters': {
            'string': 'string'
        },
        'CreatedBy': 'string',
        'IsRegisteredWithLakeFormation': True|False
    }
}


Response Structure

(dict) --

Table (dict) --
The Table object that defines the specified table.

Name (string) --
The table name. For Hive compatibility, this must be entirely lowercase.

DatabaseName (string) --
The name of the database where the table metadata resides. For Hive compatibility, this must be all lowercase.

Description (string) --
A description of the table.

Owner (string) --
The owner of the table.

CreateTime (datetime) --
The time when the table definition was created in the Data Catalog.

UpdateTime (datetime) --
The last time that the table was updated.

LastAccessTime (datetime) --
The last time that the table was accessed. This is usually taken from HDFS, and might not be reliable.

LastAnalyzedTime (datetime) --
The last time that column statistics were computed for this table.

Retention (integer) --
The retention time for this table.

StorageDescriptor (dict) --
A storage descriptor containing information about the physical storage of this table.

Columns (list) --
A list of the Columns in the table.

(dict) --
A column in a Table .

Name (string) --
The name of the Column .

Type (string) --
The data type of the Column .

Comment (string) --
A free-form text comment.

Parameters (dict) --
These key-value pairs define properties associated with the column.

(string) --
(string) --








Location (string) --
The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

InputFormat (string) --
The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.

OutputFormat (string) --
The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.

Compressed (boolean) --

True if the data in the table is compressed, or False if not.


NumberOfBuckets (integer) --
Must be specified if the table contains any dimension columns.

SerdeInfo (dict) --
The serialization/deserialization (SerDe) information.

Name (string) --
Name of the SerDe.

SerializationLibrary (string) --
Usually the class that implements the SerDe. An example is org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .

Parameters (dict) --
These key-value pairs define initialization parameters for the SerDe.

(string) --
(string) --






BucketColumns (list) --
A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

(string) --


SortColumns (list) --
A list specifying the sort order of each bucket in the table.

(dict) --
Specifies the sort order of a sorted column.

Column (string) --
The name of the column.

SortOrder (integer) --
Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).





Parameters (dict) --
The user-supplied properties in key-value form.

(string) --
(string) --




SkewedInfo (dict) --
The information about values that appear frequently in a column (skewed values).

SkewedColumnNames (list) --
A list of names of columns that contain skewed values.

(string) --


SkewedColumnValues (list) --
A list of values that appear so frequently as to be considered skewed.

(string) --


SkewedColumnValueLocationMaps (dict) --
A mapping of skewed values to the columns that contain them.

(string) --
(string) --






StoredAsSubDirectories (boolean) --

True if the table data is stored in subdirectories, or False if not.




PartitionKeys (list) --
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
When you create a table used by Amazon Athena, and you do not specify any partitionKeys , you must at least set the value of partitionKeys to an empty list. For example:

"PartitionKeys": []


(dict) --
A column in a Table .

Name (string) --
The name of the Column .

Type (string) --
The data type of the Column .

Comment (string) --
A free-form text comment.

Parameters (dict) --
These key-value pairs define properties associated with the column.

(string) --
(string) --








ViewOriginalText (string) --
If the table is a view, the original text of the view; otherwise null .

ViewExpandedText (string) --
If the table is a view, the expanded text of the view; otherwise null .

TableType (string) --
The type of this table (EXTERNAL_TABLE , VIRTUAL_VIEW , etc.).

Parameters (dict) --
These key-value pairs define properties associated with the table.

(string) --
(string) --




CreatedBy (string) --
The person or entity who created the table.

IsRegisteredWithLakeFormation (boolean) --
Indicates whether the table has been registered with AWS Lake Formation.









Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.GlueEncryptionException


    :return: {
        'Table': {
            'Name': 'string',
            'DatabaseName': 'string',
            'Description': 'string',
            'Owner': 'string',
            'CreateTime': datetime(2015, 1, 1),
            'UpdateTime': datetime(2015, 1, 1),
            'LastAccessTime': datetime(2015, 1, 1),
            'LastAnalyzedTime': datetime(2015, 1, 1),
            'Retention': 123,
            'StorageDescriptor': {
                'Columns': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'Location': 'string',
                'InputFormat': 'string',
                'OutputFormat': 'string',
                'Compressed': True|False,
                'NumberOfBuckets': 123,
                'SerdeInfo': {
                    'Name': 'string',
                    'SerializationLibrary': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
                'BucketColumns': [
                    'string',
                ],
                'SortColumns': [
                    {
                        'Column': 'string',
                        'SortOrder': 123
                    },
                ],
                'Parameters': {
                    'string': 'string'
                },
                'SkewedInfo': {
                    'SkewedColumnNames': [
                        'string',
                    ],
                    'SkewedColumnValues': [
                        'string',
                    ],
                    'SkewedColumnValueLocationMaps': {
                        'string': 'string'
                    }
                },
                'StoredAsSubDirectories': True|False
            },
            'PartitionKeys': [
                {
                    'Name': 'string',
                    'Type': 'string',
                    'Comment': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
            ],
            'ViewOriginalText': 'string',
            'ViewExpandedText': 'string',
            'TableType': 'string',
            'Parameters': {
                'string': 'string'
            },
            'CreatedBy': 'string',
            'IsRegisteredWithLakeFormation': True|False
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_table_version(CatalogId=None, DatabaseName=None, TableName=None, VersionId=None):
    """
    Retrieves a specified version of a table.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_table_version(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        VersionId='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the tables reside. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table. For Hive compatibility, this name is entirely lowercase.\n

    :type VersionId: string
    :param VersionId: The ID value of the table version to be retrieved. A VersionID is a string representation of an integer. Each version is incremented by 1.

    :rtype: dict

ReturnsResponse Syntax
{
    'TableVersion': {
        'Table': {
            'Name': 'string',
            'DatabaseName': 'string',
            'Description': 'string',
            'Owner': 'string',
            'CreateTime': datetime(2015, 1, 1),
            'UpdateTime': datetime(2015, 1, 1),
            'LastAccessTime': datetime(2015, 1, 1),
            'LastAnalyzedTime': datetime(2015, 1, 1),
            'Retention': 123,
            'StorageDescriptor': {
                'Columns': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'Location': 'string',
                'InputFormat': 'string',
                'OutputFormat': 'string',
                'Compressed': True|False,
                'NumberOfBuckets': 123,
                'SerdeInfo': {
                    'Name': 'string',
                    'SerializationLibrary': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
                'BucketColumns': [
                    'string',
                ],
                'SortColumns': [
                    {
                        'Column': 'string',
                        'SortOrder': 123
                    },
                ],
                'Parameters': {
                    'string': 'string'
                },
                'SkewedInfo': {
                    'SkewedColumnNames': [
                        'string',
                    ],
                    'SkewedColumnValues': [
                        'string',
                    ],
                    'SkewedColumnValueLocationMaps': {
                        'string': 'string'
                    }
                },
                'StoredAsSubDirectories': True|False
            },
            'PartitionKeys': [
                {
                    'Name': 'string',
                    'Type': 'string',
                    'Comment': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
            ],
            'ViewOriginalText': 'string',
            'ViewExpandedText': 'string',
            'TableType': 'string',
            'Parameters': {
                'string': 'string'
            },
            'CreatedBy': 'string',
            'IsRegisteredWithLakeFormation': True|False
        },
        'VersionId': 'string'
    }
}


Response Structure

(dict) --

TableVersion (dict) --
The requested table version.

Table (dict) --
The table in question.

Name (string) --
The table name. For Hive compatibility, this must be entirely lowercase.

DatabaseName (string) --
The name of the database where the table metadata resides. For Hive compatibility, this must be all lowercase.

Description (string) --
A description of the table.

Owner (string) --
The owner of the table.

CreateTime (datetime) --
The time when the table definition was created in the Data Catalog.

UpdateTime (datetime) --
The last time that the table was updated.

LastAccessTime (datetime) --
The last time that the table was accessed. This is usually taken from HDFS, and might not be reliable.

LastAnalyzedTime (datetime) --
The last time that column statistics were computed for this table.

Retention (integer) --
The retention time for this table.

StorageDescriptor (dict) --
A storage descriptor containing information about the physical storage of this table.

Columns (list) --
A list of the Columns in the table.

(dict) --
A column in a Table .

Name (string) --
The name of the Column .

Type (string) --
The data type of the Column .

Comment (string) --
A free-form text comment.

Parameters (dict) --
These key-value pairs define properties associated with the column.

(string) --
(string) --








Location (string) --
The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

InputFormat (string) --
The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.

OutputFormat (string) --
The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.

Compressed (boolean) --

True if the data in the table is compressed, or False if not.


NumberOfBuckets (integer) --
Must be specified if the table contains any dimension columns.

SerdeInfo (dict) --
The serialization/deserialization (SerDe) information.

Name (string) --
Name of the SerDe.

SerializationLibrary (string) --
Usually the class that implements the SerDe. An example is org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .

Parameters (dict) --
These key-value pairs define initialization parameters for the SerDe.

(string) --
(string) --






BucketColumns (list) --
A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

(string) --


SortColumns (list) --
A list specifying the sort order of each bucket in the table.

(dict) --
Specifies the sort order of a sorted column.

Column (string) --
The name of the column.

SortOrder (integer) --
Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).





Parameters (dict) --
The user-supplied properties in key-value form.

(string) --
(string) --




SkewedInfo (dict) --
The information about values that appear frequently in a column (skewed values).

SkewedColumnNames (list) --
A list of names of columns that contain skewed values.

(string) --


SkewedColumnValues (list) --
A list of values that appear so frequently as to be considered skewed.

(string) --


SkewedColumnValueLocationMaps (dict) --
A mapping of skewed values to the columns that contain them.

(string) --
(string) --






StoredAsSubDirectories (boolean) --

True if the table data is stored in subdirectories, or False if not.




PartitionKeys (list) --
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
When you create a table used by Amazon Athena, and you do not specify any partitionKeys , you must at least set the value of partitionKeys to an empty list. For example:

"PartitionKeys": []


(dict) --
A column in a Table .

Name (string) --
The name of the Column .

Type (string) --
The data type of the Column .

Comment (string) --
A free-form text comment.

Parameters (dict) --
These key-value pairs define properties associated with the column.

(string) --
(string) --








ViewOriginalText (string) --
If the table is a view, the original text of the view; otherwise null .

ViewExpandedText (string) --
If the table is a view, the expanded text of the view; otherwise null .

TableType (string) --
The type of this table (EXTERNAL_TABLE , VIRTUAL_VIEW , etc.).

Parameters (dict) --
These key-value pairs define properties associated with the table.

(string) --
(string) --




CreatedBy (string) --
The person or entity who created the table.

IsRegisteredWithLakeFormation (boolean) --
Indicates whether the table has been registered with AWS Lake Formation.



VersionId (string) --
The ID value that identifies this table version. A VersionId is a string representation of an integer. Each version is incremented by 1.









Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.GlueEncryptionException


    :return: {
        'TableVersion': {
            'Table': {
                'Name': 'string',
                'DatabaseName': 'string',
                'Description': 'string',
                'Owner': 'string',
                'CreateTime': datetime(2015, 1, 1),
                'UpdateTime': datetime(2015, 1, 1),
                'LastAccessTime': datetime(2015, 1, 1),
                'LastAnalyzedTime': datetime(2015, 1, 1),
                'Retention': 123,
                'StorageDescriptor': {
                    'Columns': [
                        {
                            'Name': 'string',
                            'Type': 'string',
                            'Comment': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                    ],
                    'Location': 'string',
                    'InputFormat': 'string',
                    'OutputFormat': 'string',
                    'Compressed': True|False,
                    'NumberOfBuckets': 123,
                    'SerdeInfo': {
                        'Name': 'string',
                        'SerializationLibrary': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                    'BucketColumns': [
                        'string',
                    ],
                    'SortColumns': [
                        {
                            'Column': 'string',
                            'SortOrder': 123
                        },
                    ],
                    'Parameters': {
                        'string': 'string'
                    },
                    'SkewedInfo': {
                        'SkewedColumnNames': [
                            'string',
                        ],
                        'SkewedColumnValues': [
                            'string',
                        ],
                        'SkewedColumnValueLocationMaps': {
                            'string': 'string'
                        }
                    },
                    'StoredAsSubDirectories': True|False
                },
                'PartitionKeys': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'ViewOriginalText': 'string',
                'ViewExpandedText': 'string',
                'TableType': 'string',
                'Parameters': {
                    'string': 'string'
                },
                'CreatedBy': 'string',
                'IsRegisteredWithLakeFormation': True|False
            },
            'VersionId': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_table_versions(CatalogId=None, DatabaseName=None, TableName=None, NextToken=None, MaxResults=None):
    """
    Retrieves a list of strings that identify available versions of a specified table.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_table_versions(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the tables reside. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table. For Hive compatibility, this name is entirely lowercase.\n

    :type NextToken: string
    :param NextToken: A continuation token, if this is not the first call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of table versions to return in one response.

    :rtype: dict

ReturnsResponse Syntax
{
    'TableVersions': [
        {
            'Table': {
                'Name': 'string',
                'DatabaseName': 'string',
                'Description': 'string',
                'Owner': 'string',
                'CreateTime': datetime(2015, 1, 1),
                'UpdateTime': datetime(2015, 1, 1),
                'LastAccessTime': datetime(2015, 1, 1),
                'LastAnalyzedTime': datetime(2015, 1, 1),
                'Retention': 123,
                'StorageDescriptor': {
                    'Columns': [
                        {
                            'Name': 'string',
                            'Type': 'string',
                            'Comment': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                    ],
                    'Location': 'string',
                    'InputFormat': 'string',
                    'OutputFormat': 'string',
                    'Compressed': True|False,
                    'NumberOfBuckets': 123,
                    'SerdeInfo': {
                        'Name': 'string',
                        'SerializationLibrary': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                    'BucketColumns': [
                        'string',
                    ],
                    'SortColumns': [
                        {
                            'Column': 'string',
                            'SortOrder': 123
                        },
                    ],
                    'Parameters': {
                        'string': 'string'
                    },
                    'SkewedInfo': {
                        'SkewedColumnNames': [
                            'string',
                        ],
                        'SkewedColumnValues': [
                            'string',
                        ],
                        'SkewedColumnValueLocationMaps': {
                            'string': 'string'
                        }
                    },
                    'StoredAsSubDirectories': True|False
                },
                'PartitionKeys': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'ViewOriginalText': 'string',
                'ViewExpandedText': 'string',
                'TableType': 'string',
                'Parameters': {
                    'string': 'string'
                },
                'CreatedBy': 'string',
                'IsRegisteredWithLakeFormation': True|False
            },
            'VersionId': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

TableVersions (list) --
A list of strings identifying available versions of the specified table.

(dict) --
Specifies a version of a table.

Table (dict) --
The table in question.

Name (string) --
The table name. For Hive compatibility, this must be entirely lowercase.

DatabaseName (string) --
The name of the database where the table metadata resides. For Hive compatibility, this must be all lowercase.

Description (string) --
A description of the table.

Owner (string) --
The owner of the table.

CreateTime (datetime) --
The time when the table definition was created in the Data Catalog.

UpdateTime (datetime) --
The last time that the table was updated.

LastAccessTime (datetime) --
The last time that the table was accessed. This is usually taken from HDFS, and might not be reliable.

LastAnalyzedTime (datetime) --
The last time that column statistics were computed for this table.

Retention (integer) --
The retention time for this table.

StorageDescriptor (dict) --
A storage descriptor containing information about the physical storage of this table.

Columns (list) --
A list of the Columns in the table.

(dict) --
A column in a Table .

Name (string) --
The name of the Column .

Type (string) --
The data type of the Column .

Comment (string) --
A free-form text comment.

Parameters (dict) --
These key-value pairs define properties associated with the column.

(string) --
(string) --








Location (string) --
The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

InputFormat (string) --
The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.

OutputFormat (string) --
The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.

Compressed (boolean) --

True if the data in the table is compressed, or False if not.


NumberOfBuckets (integer) --
Must be specified if the table contains any dimension columns.

SerdeInfo (dict) --
The serialization/deserialization (SerDe) information.

Name (string) --
Name of the SerDe.

SerializationLibrary (string) --
Usually the class that implements the SerDe. An example is org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .

Parameters (dict) --
These key-value pairs define initialization parameters for the SerDe.

(string) --
(string) --






BucketColumns (list) --
A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

(string) --


SortColumns (list) --
A list specifying the sort order of each bucket in the table.

(dict) --
Specifies the sort order of a sorted column.

Column (string) --
The name of the column.

SortOrder (integer) --
Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).





Parameters (dict) --
The user-supplied properties in key-value form.

(string) --
(string) --




SkewedInfo (dict) --
The information about values that appear frequently in a column (skewed values).

SkewedColumnNames (list) --
A list of names of columns that contain skewed values.

(string) --


SkewedColumnValues (list) --
A list of values that appear so frequently as to be considered skewed.

(string) --


SkewedColumnValueLocationMaps (dict) --
A mapping of skewed values to the columns that contain them.

(string) --
(string) --






StoredAsSubDirectories (boolean) --

True if the table data is stored in subdirectories, or False if not.




PartitionKeys (list) --
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
When you create a table used by Amazon Athena, and you do not specify any partitionKeys , you must at least set the value of partitionKeys to an empty list. For example:

"PartitionKeys": []


(dict) --
A column in a Table .

Name (string) --
The name of the Column .

Type (string) --
The data type of the Column .

Comment (string) --
A free-form text comment.

Parameters (dict) --
These key-value pairs define properties associated with the column.

(string) --
(string) --








ViewOriginalText (string) --
If the table is a view, the original text of the view; otherwise null .

ViewExpandedText (string) --
If the table is a view, the expanded text of the view; otherwise null .

TableType (string) --
The type of this table (EXTERNAL_TABLE , VIRTUAL_VIEW , etc.).

Parameters (dict) --
These key-value pairs define properties associated with the table.

(string) --
(string) --




CreatedBy (string) --
The person or entity who created the table.

IsRegisteredWithLakeFormation (boolean) --
Indicates whether the table has been registered with AWS Lake Formation.



VersionId (string) --
The ID value that identifies this table version. A VersionId is a string representation of an integer. Each version is incremented by 1.





NextToken (string) --
A continuation token, if the list of available versions does not include the last one.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.GlueEncryptionException


    :return: {
        'TableVersions': [
            {
                'Table': {
                    'Name': 'string',
                    'DatabaseName': 'string',
                    'Description': 'string',
                    'Owner': 'string',
                    'CreateTime': datetime(2015, 1, 1),
                    'UpdateTime': datetime(2015, 1, 1),
                    'LastAccessTime': datetime(2015, 1, 1),
                    'LastAnalyzedTime': datetime(2015, 1, 1),
                    'Retention': 123,
                    'StorageDescriptor': {
                        'Columns': [
                            {
                                'Name': 'string',
                                'Type': 'string',
                                'Comment': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                        ],
                        'Location': 'string',
                        'InputFormat': 'string',
                        'OutputFormat': 'string',
                        'Compressed': True|False,
                        'NumberOfBuckets': 123,
                        'SerdeInfo': {
                            'Name': 'string',
                            'SerializationLibrary': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                        'BucketColumns': [
                            'string',
                        ],
                        'SortColumns': [
                            {
                                'Column': 'string',
                                'SortOrder': 123
                            },
                        ],
                        'Parameters': {
                            'string': 'string'
                        },
                        'SkewedInfo': {
                            'SkewedColumnNames': [
                                'string',
                            ],
                            'SkewedColumnValues': [
                                'string',
                            ],
                            'SkewedColumnValueLocationMaps': {
                                'string': 'string'
                            }
                        },
                        'StoredAsSubDirectories': True|False
                    },
                    'PartitionKeys': [
                        {
                            'Name': 'string',
                            'Type': 'string',
                            'Comment': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                    ],
                    'ViewOriginalText': 'string',
                    'ViewExpandedText': 'string',
                    'TableType': 'string',
                    'Parameters': {
                        'string': 'string'
                    },
                    'CreatedBy': 'string',
                    'IsRegisteredWithLakeFormation': True|False
                },
                'VersionId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_tables(CatalogId=None, DatabaseName=None, Expression=None, NextToken=None, MaxResults=None):
    """
    Retrieves the definitions of some or all of the tables in a given Database .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_tables(
        CatalogId='string',
        DatabaseName='string',
        Expression='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the tables reside. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe database in the catalog whose tables to list. For Hive compatibility, this name is entirely lowercase.\n

    :type Expression: string
    :param Expression: A regular expression pattern. If present, only those tables whose names match the pattern are returned.

    :type NextToken: string
    :param NextToken: A continuation token, included if this is a continuation call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of tables to return in a single response.

    :rtype: dict

ReturnsResponse Syntax
{
    'TableList': [
        {
            'Name': 'string',
            'DatabaseName': 'string',
            'Description': 'string',
            'Owner': 'string',
            'CreateTime': datetime(2015, 1, 1),
            'UpdateTime': datetime(2015, 1, 1),
            'LastAccessTime': datetime(2015, 1, 1),
            'LastAnalyzedTime': datetime(2015, 1, 1),
            'Retention': 123,
            'StorageDescriptor': {
                'Columns': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'Location': 'string',
                'InputFormat': 'string',
                'OutputFormat': 'string',
                'Compressed': True|False,
                'NumberOfBuckets': 123,
                'SerdeInfo': {
                    'Name': 'string',
                    'SerializationLibrary': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
                'BucketColumns': [
                    'string',
                ],
                'SortColumns': [
                    {
                        'Column': 'string',
                        'SortOrder': 123
                    },
                ],
                'Parameters': {
                    'string': 'string'
                },
                'SkewedInfo': {
                    'SkewedColumnNames': [
                        'string',
                    ],
                    'SkewedColumnValues': [
                        'string',
                    ],
                    'SkewedColumnValueLocationMaps': {
                        'string': 'string'
                    }
                },
                'StoredAsSubDirectories': True|False
            },
            'PartitionKeys': [
                {
                    'Name': 'string',
                    'Type': 'string',
                    'Comment': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
            ],
            'ViewOriginalText': 'string',
            'ViewExpandedText': 'string',
            'TableType': 'string',
            'Parameters': {
                'string': 'string'
            },
            'CreatedBy': 'string',
            'IsRegisteredWithLakeFormation': True|False
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

TableList (list) --
A list of the requested Table objects.

(dict) --
Represents a collection of related data organized in columns and rows.

Name (string) --
The table name. For Hive compatibility, this must be entirely lowercase.

DatabaseName (string) --
The name of the database where the table metadata resides. For Hive compatibility, this must be all lowercase.

Description (string) --
A description of the table.

Owner (string) --
The owner of the table.

CreateTime (datetime) --
The time when the table definition was created in the Data Catalog.

UpdateTime (datetime) --
The last time that the table was updated.

LastAccessTime (datetime) --
The last time that the table was accessed. This is usually taken from HDFS, and might not be reliable.

LastAnalyzedTime (datetime) --
The last time that column statistics were computed for this table.

Retention (integer) --
The retention time for this table.

StorageDescriptor (dict) --
A storage descriptor containing information about the physical storage of this table.

Columns (list) --
A list of the Columns in the table.

(dict) --
A column in a Table .

Name (string) --
The name of the Column .

Type (string) --
The data type of the Column .

Comment (string) --
A free-form text comment.

Parameters (dict) --
These key-value pairs define properties associated with the column.

(string) --
(string) --








Location (string) --
The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

InputFormat (string) --
The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.

OutputFormat (string) --
The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.

Compressed (boolean) --

True if the data in the table is compressed, or False if not.


NumberOfBuckets (integer) --
Must be specified if the table contains any dimension columns.

SerdeInfo (dict) --
The serialization/deserialization (SerDe) information.

Name (string) --
Name of the SerDe.

SerializationLibrary (string) --
Usually the class that implements the SerDe. An example is org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .

Parameters (dict) --
These key-value pairs define initialization parameters for the SerDe.

(string) --
(string) --






BucketColumns (list) --
A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

(string) --


SortColumns (list) --
A list specifying the sort order of each bucket in the table.

(dict) --
Specifies the sort order of a sorted column.

Column (string) --
The name of the column.

SortOrder (integer) --
Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).





Parameters (dict) --
The user-supplied properties in key-value form.

(string) --
(string) --




SkewedInfo (dict) --
The information about values that appear frequently in a column (skewed values).

SkewedColumnNames (list) --
A list of names of columns that contain skewed values.

(string) --


SkewedColumnValues (list) --
A list of values that appear so frequently as to be considered skewed.

(string) --


SkewedColumnValueLocationMaps (dict) --
A mapping of skewed values to the columns that contain them.

(string) --
(string) --






StoredAsSubDirectories (boolean) --

True if the table data is stored in subdirectories, or False if not.




PartitionKeys (list) --
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
When you create a table used by Amazon Athena, and you do not specify any partitionKeys , you must at least set the value of partitionKeys to an empty list. For example:

"PartitionKeys": []


(dict) --
A column in a Table .

Name (string) --
The name of the Column .

Type (string) --
The data type of the Column .

Comment (string) --
A free-form text comment.

Parameters (dict) --
These key-value pairs define properties associated with the column.

(string) --
(string) --








ViewOriginalText (string) --
If the table is a view, the original text of the view; otherwise null .

ViewExpandedText (string) --
If the table is a view, the expanded text of the view; otherwise null .

TableType (string) --
The type of this table (EXTERNAL_TABLE , VIRTUAL_VIEW , etc.).

Parameters (dict) --
These key-value pairs define properties associated with the table.

(string) --
(string) --




CreatedBy (string) --
The person or entity who created the table.

IsRegisteredWithLakeFormation (boolean) --
Indicates whether the table has been registered with AWS Lake Formation.





NextToken (string) --
A continuation token, present if the current list segment is not the last.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.GlueEncryptionException


    :return: {
        'TableList': [
            {
                'Name': 'string',
                'DatabaseName': 'string',
                'Description': 'string',
                'Owner': 'string',
                'CreateTime': datetime(2015, 1, 1),
                'UpdateTime': datetime(2015, 1, 1),
                'LastAccessTime': datetime(2015, 1, 1),
                'LastAnalyzedTime': datetime(2015, 1, 1),
                'Retention': 123,
                'StorageDescriptor': {
                    'Columns': [
                        {
                            'Name': 'string',
                            'Type': 'string',
                            'Comment': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                    ],
                    'Location': 'string',
                    'InputFormat': 'string',
                    'OutputFormat': 'string',
                    'Compressed': True|False,
                    'NumberOfBuckets': 123,
                    'SerdeInfo': {
                        'Name': 'string',
                        'SerializationLibrary': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                    'BucketColumns': [
                        'string',
                    ],
                    'SortColumns': [
                        {
                            'Column': 'string',
                            'SortOrder': 123
                        },
                    ],
                    'Parameters': {
                        'string': 'string'
                    },
                    'SkewedInfo': {
                        'SkewedColumnNames': [
                            'string',
                        ],
                        'SkewedColumnValues': [
                            'string',
                        ],
                        'SkewedColumnValueLocationMaps': {
                            'string': 'string'
                        }
                    },
                    'StoredAsSubDirectories': True|False
                },
                'PartitionKeys': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'ViewOriginalText': 'string',
                'ViewExpandedText': 'string',
                'TableType': 'string',
                'Parameters': {
                    'string': 'string'
                },
                'CreatedBy': 'string',
                'IsRegisteredWithLakeFormation': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_tags(ResourceArn=None):
    """
    Retrieves a list of tags associated with a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_tags(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource for which to retrieve tags.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Tags (dict) --The requested tags.

(string) --
(string) --









Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.EntityNotFoundException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.EntityNotFoundException
    
    """
    pass

def get_trigger(Name=None):
    """
    Retrieves the definition of a trigger.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_trigger(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the trigger to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Trigger': {
        'Name': 'string',
        'WorkflowName': 'string',
        'Id': 'string',
        'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
        'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
        'Description': 'string',
        'Schedule': 'string',
        'Actions': [
            {
                'JobName': 'string',
                'Arguments': {
                    'string': 'string'
                },
                'Timeout': 123,
                'SecurityConfiguration': 'string',
                'NotificationProperty': {
                    'NotifyDelayAfter': 123
                },
                'CrawlerName': 'string'
            },
        ],
        'Predicate': {
            'Logical': 'AND'|'ANY',
            'Conditions': [
                {
                    'LogicalOperator': 'EQUALS',
                    'JobName': 'string',
                    'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                    'CrawlerName': 'string',
                    'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                },
            ]
        }
    }
}


Response Structure

(dict) --
Trigger (dict) --The requested trigger definition.

Name (string) --The name of the trigger.

WorkflowName (string) --The name of the workflow associated with the trigger.

Id (string) --Reserved for future use.

Type (string) --The type of trigger that this is.

State (string) --The current state of the trigger.

Description (string) --A description of this trigger.

Schedule (string) --A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .

Actions (list) --The actions initiated by this trigger.

(dict) --Defines an action to be initiated by a trigger.

JobName (string) --The name of a job to be executed.

Arguments (dict) --The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




Timeout (integer) --The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

SecurityConfiguration (string) --The name of the SecurityConfiguration structure to be used with this action.

NotificationProperty (dict) --Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --After a job run starts, the number of minutes to wait before sending a job run delay notification.



CrawlerName (string) --The name of the crawler to be used with this action.





Predicate (dict) --The predicate of this trigger, which defines when it will fire.

Logical (string) --An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.

Conditions (list) --A list of the conditions that determine when the trigger will fire.

(dict) --Defines a condition under which a trigger fires.

LogicalOperator (string) --A logical operator.

JobName (string) --The name of the job whose JobRuns this condition applies to, and on which this trigger waits.

State (string) --The condition state. Currently, the only job states that a trigger can listen for are SUCCEEDED , STOPPED , FAILED , and TIMEOUT . The only crawler states that a trigger can listen for are SUCCEEDED , FAILED , and CANCELLED .

CrawlerName (string) --The name of the crawler to which this condition applies.

CrawlState (string) --The state of the crawler to which this condition applies.














Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Trigger': {
            'Name': 'string',
            'WorkflowName': 'string',
            'Id': 'string',
            'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
            'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
            'Description': 'string',
            'Schedule': 'string',
            'Actions': [
                {
                    'JobName': 'string',
                    'Arguments': {
                        'string': 'string'
                    },
                    'Timeout': 123,
                    'SecurityConfiguration': 'string',
                    'NotificationProperty': {
                        'NotifyDelayAfter': 123
                    },
                    'CrawlerName': 'string'
                },
            ],
            'Predicate': {
                'Logical': 'AND'|'ANY',
                'Conditions': [
                    {
                        'LogicalOperator': 'EQUALS',
                        'JobName': 'string',
                        'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                        'CrawlerName': 'string',
                        'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def get_triggers(NextToken=None, DependentJobName=None, MaxResults=None):
    """
    Gets all the triggers associated with a job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_triggers(
        NextToken='string',
        DependentJobName='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :type DependentJobName: string
    :param DependentJobName: The name of the job to retrieve triggers for. The trigger that can start this job is returned, and if there is no such trigger, all triggers are returned.

    :type MaxResults: integer
    :param MaxResults: The maximum size of the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'Triggers': [
        {
            'Name': 'string',
            'WorkflowName': 'string',
            'Id': 'string',
            'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
            'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
            'Description': 'string',
            'Schedule': 'string',
            'Actions': [
                {
                    'JobName': 'string',
                    'Arguments': {
                        'string': 'string'
                    },
                    'Timeout': 123,
                    'SecurityConfiguration': 'string',
                    'NotificationProperty': {
                        'NotifyDelayAfter': 123
                    },
                    'CrawlerName': 'string'
                },
            ],
            'Predicate': {
                'Logical': 'AND'|'ANY',
                'Conditions': [
                    {
                        'LogicalOperator': 'EQUALS',
                        'JobName': 'string',
                        'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                        'CrawlerName': 'string',
                        'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                    },
                ]
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Triggers (list) --
A list of triggers for the specified job.

(dict) --
Information about a specific trigger.

Name (string) --
The name of the trigger.

WorkflowName (string) --
The name of the workflow associated with the trigger.

Id (string) --
Reserved for future use.

Type (string) --
The type of trigger that this is.

State (string) --
The current state of the trigger.

Description (string) --
A description of this trigger.

Schedule (string) --
A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .

Actions (list) --
The actions initiated by this trigger.

(dict) --
Defines an action to be initiated by a trigger.

JobName (string) --
The name of a job to be executed.

Arguments (dict) --
The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this action.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



CrawlerName (string) --
The name of the crawler to be used with this action.





Predicate (dict) --
The predicate of this trigger, which defines when it will fire.

Logical (string) --
An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.

Conditions (list) --
A list of the conditions that determine when the trigger will fire.

(dict) --
Defines a condition under which a trigger fires.

LogicalOperator (string) --
A logical operator.

JobName (string) --
The name of the job whose JobRuns this condition applies to, and on which this trigger waits.

State (string) --
The condition state. Currently, the only job states that a trigger can listen for are SUCCEEDED , STOPPED , FAILED , and TIMEOUT . The only crawler states that a trigger can listen for are SUCCEEDED , FAILED , and CANCELLED .

CrawlerName (string) --
The name of the crawler to which this condition applies.

CrawlState (string) --
The state of the crawler to which this condition applies.











NextToken (string) --
A continuation token, if not all the requested triggers have yet been returned.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Triggers': [
            {
                'Name': 'string',
                'WorkflowName': 'string',
                'Id': 'string',
                'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                'Description': 'string',
                'Schedule': 'string',
                'Actions': [
                    {
                        'JobName': 'string',
                        'Arguments': {
                            'string': 'string'
                        },
                        'Timeout': 123,
                        'SecurityConfiguration': 'string',
                        'NotificationProperty': {
                            'NotifyDelayAfter': 123
                        },
                        'CrawlerName': 'string'
                    },
                ],
                'Predicate': {
                    'Logical': 'AND'|'ANY',
                    'Conditions': [
                        {
                            'LogicalOperator': 'EQUALS',
                            'JobName': 'string',
                            'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                            'CrawlerName': 'string',
                            'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                        },
                    ]
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_user_defined_function(CatalogId=None, DatabaseName=None, FunctionName=None):
    """
    Retrieves a specified function definition from the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_user_defined_function(
        CatalogId='string',
        DatabaseName='string',
        FunctionName='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the function to be retrieved is located. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the catalog database where the function is located.\n

    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the function.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UserDefinedFunction': {
        'FunctionName': 'string',
        'ClassName': 'string',
        'OwnerName': 'string',
        'OwnerType': 'USER'|'ROLE'|'GROUP',
        'CreateTime': datetime(2015, 1, 1),
        'ResourceUris': [
            {
                'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                'Uri': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

UserDefinedFunction (dict) --
The requested function definition.

FunctionName (string) --
The name of the function.

ClassName (string) --
The Java class that contains the function code.

OwnerName (string) --
The owner of the function.

OwnerType (string) --
The owner type.

CreateTime (datetime) --
The time at which the function was created.

ResourceUris (list) --
The resource URIs for the function.

(dict) --
The URIs for function resources.

ResourceType (string) --
The type of the resource.

Uri (string) --
The URI for accessing the resource.













Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.GlueEncryptionException


    :return: {
        'UserDefinedFunction': {
            'FunctionName': 'string',
            'ClassName': 'string',
            'OwnerName': 'string',
            'OwnerType': 'USER'|'ROLE'|'GROUP',
            'CreateTime': datetime(2015, 1, 1),
            'ResourceUris': [
                {
                    'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                    'Uri': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.GlueEncryptionException
    
    """
    pass

def get_user_defined_functions(CatalogId=None, DatabaseName=None, Pattern=None, NextToken=None, MaxResults=None):
    """
    Retrieves multiple function definitions from the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_user_defined_functions(
        CatalogId='string',
        DatabaseName='string',
        Pattern='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the functions to be retrieved are located. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: The name of the catalog database where the functions are located.

    :type Pattern: string
    :param Pattern: [REQUIRED]\nAn optional function-name pattern string that filters the function definitions returned.\n

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of functions to return in one response.

    :rtype: dict

ReturnsResponse Syntax
{
    'UserDefinedFunctions': [
        {
            'FunctionName': 'string',
            'ClassName': 'string',
            'OwnerName': 'string',
            'OwnerType': 'USER'|'ROLE'|'GROUP',
            'CreateTime': datetime(2015, 1, 1),
            'ResourceUris': [
                {
                    'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                    'Uri': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

UserDefinedFunctions (list) --
A list of requested function definitions.

(dict) --
Represents the equivalent of a Hive user-defined function (UDF ) definition.

FunctionName (string) --
The name of the function.

ClassName (string) --
The Java class that contains the function code.

OwnerName (string) --
The owner of the function.

OwnerType (string) --
The owner type.

CreateTime (datetime) --
The time at which the function was created.

ResourceUris (list) --
The resource URIs for the function.

(dict) --
The URIs for function resources.

ResourceType (string) --
The type of the resource.

Uri (string) --
The URI for accessing the resource.









NextToken (string) --
A continuation token, if the list of functions returned does not include the last requested function.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.GlueEncryptionException


    :return: {
        'UserDefinedFunctions': [
            {
                'FunctionName': 'string',
                'ClassName': 'string',
                'OwnerName': 'string',
                'OwnerType': 'USER'|'ROLE'|'GROUP',
                'CreateTime': datetime(2015, 1, 1),
                'ResourceUris': [
                    {
                        'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                        'Uri': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.GlueEncryptionException
    
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

def get_workflow(Name=None, IncludeGraph=None):
    """
    Retrieves resource metadata for a workflow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_workflow(
        Name='string',
        IncludeGraph=True|False
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the workflow to retrieve.\n

    :type IncludeGraph: boolean
    :param IncludeGraph: Specifies whether to include a graph when returning the workflow resource metadata.

    :rtype: dict

ReturnsResponse Syntax
{
    'Workflow': {
        'Name': 'string',
        'Description': 'string',
        'DefaultRunProperties': {
            'string': 'string'
        },
        'CreatedOn': datetime(2015, 1, 1),
        'LastModifiedOn': datetime(2015, 1, 1),
        'LastRun': {
            'Name': 'string',
            'WorkflowRunId': 'string',
            'WorkflowRunProperties': {
                'string': 'string'
            },
            'StartedOn': datetime(2015, 1, 1),
            'CompletedOn': datetime(2015, 1, 1),
            'Status': 'RUNNING'|'COMPLETED'|'STOPPING'|'STOPPED',
            'Statistics': {
                'TotalActions': 123,
                'TimeoutActions': 123,
                'FailedActions': 123,
                'StoppedActions': 123,
                'SucceededActions': 123,
                'RunningActions': 123
            },
            'Graph': {
                'Nodes': [
                    {
                        'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                        'Name': 'string',
                        'UniqueId': 'string',
                        'TriggerDetails': {
                            'Trigger': {
                                'Name': 'string',
                                'WorkflowName': 'string',
                                'Id': 'string',
                                'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                                'Description': 'string',
                                'Schedule': 'string',
                                'Actions': [
                                    {
                                        'JobName': 'string',
                                        'Arguments': {
                                            'string': 'string'
                                        },
                                        'Timeout': 123,
                                        'SecurityConfiguration': 'string',
                                        'NotificationProperty': {
                                            'NotifyDelayAfter': 123
                                        },
                                        'CrawlerName': 'string'
                                    },
                                ],
                                'Predicate': {
                                    'Logical': 'AND'|'ANY',
                                    'Conditions': [
                                        {
                                            'LogicalOperator': 'EQUALS',
                                            'JobName': 'string',
                                            'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                            'CrawlerName': 'string',
                                            'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                                        },
                                    ]
                                }
                            }
                        },
                        'JobDetails': {
                            'JobRuns': [
                                {
                                    'Id': 'string',
                                    'Attempt': 123,
                                    'PreviousRunId': 'string',
                                    'TriggerName': 'string',
                                    'JobName': 'string',
                                    'StartedOn': datetime(2015, 1, 1),
                                    'LastModifiedOn': datetime(2015, 1, 1),
                                    'CompletedOn': datetime(2015, 1, 1),
                                    'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                    'Arguments': {
                                        'string': 'string'
                                    },
                                    'ErrorMessage': 'string',
                                    'PredecessorRuns': [
                                        {
                                            'JobName': 'string',
                                            'RunId': 'string'
                                        },
                                    ],
                                    'AllocatedCapacity': 123,
                                    'ExecutionTime': 123,
                                    'Timeout': 123,
                                    'MaxCapacity': 123.0,
                                    'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                    'NumberOfWorkers': 123,
                                    'SecurityConfiguration': 'string',
                                    'LogGroupName': 'string',
                                    'NotificationProperty': {
                                        'NotifyDelayAfter': 123
                                    },
                                    'GlueVersion': 'string'
                                },
                            ]
                        },
                        'CrawlerDetails': {
                            'Crawls': [
                                {
                                    'State': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED',
                                    'StartedOn': datetime(2015, 1, 1),
                                    'CompletedOn': datetime(2015, 1, 1),
                                    'ErrorMessage': 'string',
                                    'LogGroup': 'string',
                                    'LogStream': 'string'
                                },
                            ]
                        }
                    },
                ],
                'Edges': [
                    {
                        'SourceId': 'string',
                        'DestinationId': 'string'
                    },
                ]
            }
        },
        'Graph': {
            'Nodes': [
                {
                    'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                    'Name': 'string',
                    'UniqueId': 'string',
                    'TriggerDetails': {
                        'Trigger': {
                            'Name': 'string',
                            'WorkflowName': 'string',
                            'Id': 'string',
                            'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                            'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                            'Description': 'string',
                            'Schedule': 'string',
                            'Actions': [
                                {
                                    'JobName': 'string',
                                    'Arguments': {
                                        'string': 'string'
                                    },
                                    'Timeout': 123,
                                    'SecurityConfiguration': 'string',
                                    'NotificationProperty': {
                                        'NotifyDelayAfter': 123
                                    },
                                    'CrawlerName': 'string'
                                },
                            ],
                            'Predicate': {
                                'Logical': 'AND'|'ANY',
                                'Conditions': [
                                    {
                                        'LogicalOperator': 'EQUALS',
                                        'JobName': 'string',
                                        'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                        'CrawlerName': 'string',
                                        'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                                    },
                                ]
                            }
                        }
                    },
                    'JobDetails': {
                        'JobRuns': [
                            {
                                'Id': 'string',
                                'Attempt': 123,
                                'PreviousRunId': 'string',
                                'TriggerName': 'string',
                                'JobName': 'string',
                                'StartedOn': datetime(2015, 1, 1),
                                'LastModifiedOn': datetime(2015, 1, 1),
                                'CompletedOn': datetime(2015, 1, 1),
                                'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                'Arguments': {
                                    'string': 'string'
                                },
                                'ErrorMessage': 'string',
                                'PredecessorRuns': [
                                    {
                                        'JobName': 'string',
                                        'RunId': 'string'
                                    },
                                ],
                                'AllocatedCapacity': 123,
                                'ExecutionTime': 123,
                                'Timeout': 123,
                                'MaxCapacity': 123.0,
                                'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                'NumberOfWorkers': 123,
                                'SecurityConfiguration': 'string',
                                'LogGroupName': 'string',
                                'NotificationProperty': {
                                    'NotifyDelayAfter': 123
                                },
                                'GlueVersion': 'string'
                            },
                        ]
                    },
                    'CrawlerDetails': {
                        'Crawls': [
                            {
                                'State': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED',
                                'StartedOn': datetime(2015, 1, 1),
                                'CompletedOn': datetime(2015, 1, 1),
                                'ErrorMessage': 'string',
                                'LogGroup': 'string',
                                'LogStream': 'string'
                            },
                        ]
                    }
                },
            ],
            'Edges': [
                {
                    'SourceId': 'string',
                    'DestinationId': 'string'
                },
            ]
        }
    }
}


Response Structure

(dict) --

Workflow (dict) --
The resource metadata for the workflow.

Name (string) --
The name of the workflow representing the flow.

Description (string) --
A description of the workflow.

DefaultRunProperties (dict) --
A collection of properties to be used as part of each execution of the workflow.

(string) --
(string) --




CreatedOn (datetime) --
The date and time when the workflow was created.

LastModifiedOn (datetime) --
The date and time when the workflow was last modified.

LastRun (dict) --
The information about the last execution of the workflow.

Name (string) --
Name of the workflow which was executed.

WorkflowRunId (string) --
The ID of this workflow run.

WorkflowRunProperties (dict) --
The workflow run properties which were set during the run.

(string) --
(string) --




StartedOn (datetime) --
The date and time when the workflow run was started.

CompletedOn (datetime) --
The date and time when the workflow run completed.

Status (string) --
The status of the workflow run.

Statistics (dict) --
The statistics of the run.

TotalActions (integer) --
Total number of Actions in the workflow run.

TimeoutActions (integer) --
Total number of Actions which timed out.

FailedActions (integer) --
Total number of Actions which have failed.

StoppedActions (integer) --
Total number of Actions which have stopped.

SucceededActions (integer) --
Total number of Actions which have succeeded.

RunningActions (integer) --
Total number Actions in running state.



Graph (dict) --
The graph representing all the AWS Glue components that belong to the workflow as nodes and directed connections between them as edges.

Nodes (list) --
A list of the the AWS Glue components belong to the workflow represented as nodes.

(dict) --
A node represents an AWS Glue component like Trigger, Job etc. which is part of a workflow.

Type (string) --
The type of AWS Glue component represented by the node.

Name (string) --
The name of the AWS Glue component represented by the node.

UniqueId (string) --
The unique Id assigned to the node within the workflow.

TriggerDetails (dict) --
Details of the Trigger when the node represents a Trigger.

Trigger (dict) --
The information of the trigger represented by the trigger node.

Name (string) --
The name of the trigger.

WorkflowName (string) --
The name of the workflow associated with the trigger.

Id (string) --
Reserved for future use.

Type (string) --
The type of trigger that this is.

State (string) --
The current state of the trigger.

Description (string) --
A description of this trigger.

Schedule (string) --
A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .

Actions (list) --
The actions initiated by this trigger.

(dict) --
Defines an action to be initiated by a trigger.

JobName (string) --
The name of a job to be executed.

Arguments (dict) --
The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this action.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



CrawlerName (string) --
The name of the crawler to be used with this action.





Predicate (dict) --
The predicate of this trigger, which defines when it will fire.

Logical (string) --
An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.

Conditions (list) --
A list of the conditions that determine when the trigger will fire.

(dict) --
Defines a condition under which a trigger fires.

LogicalOperator (string) --
A logical operator.

JobName (string) --
The name of the job whose JobRuns this condition applies to, and on which this trigger waits.

State (string) --
The condition state. Currently, the only job states that a trigger can listen for are SUCCEEDED , STOPPED , FAILED , and TIMEOUT . The only crawler states that a trigger can listen for are SUCCEEDED , FAILED , and CANCELLED .

CrawlerName (string) --
The name of the crawler to which this condition applies.

CrawlState (string) --
The state of the crawler to which this condition applies.











JobDetails (dict) --
Details of the Job when the node represents a Job.

JobRuns (list) --
The information for the job runs represented by the job node.

(dict) --
Contains information about a job run.

Id (string) --
The ID of this job run.

Attempt (integer) --
The number of the attempt to run this job.

PreviousRunId (string) --
The ID of the previous run of this job. For example, the JobRunId specified in the StartJobRun action.

TriggerName (string) --
The name of the trigger that started this job run.

JobName (string) --
The name of the job definition being used in this run.

StartedOn (datetime) --
The date and time at which this job run was started.

LastModifiedOn (datetime) --
The last time that this job run was modified.

CompletedOn (datetime) --
The date and time that this job run completed.

JobRunState (string) --
The current state of the job run. For more information about the statuses of jobs that have terminated abnormally, see AWS Glue Job Run Statuses .

Arguments (dict) --
The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




ErrorMessage (string) --
An error message associated with this job run.

PredecessorRuns (list) --
A list of predecessors to this job run.

(dict) --
A job run that was used in the predicate of a conditional trigger that triggered this job run.

JobName (string) --
The name of the job definition used by the predecessor job run.

RunId (string) --
The job-run ID of the predecessor job run.





AllocatedCapacity (integer) --
This field is deprecated. Use MaxCapacity instead.
The number of AWS Glue data processing units (DPUs) allocated to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .

ExecutionTime (integer) --
The amount of time (in seconds) that the job run consumed resources.

Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

MaxCapacity (float) --
The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .
Do not set Max Capacity if using WorkerType and NumberOfWorkers .
The value that can be allocated for MaxCapacity depends on whether you are running a Python shell job or an Apache Spark ETL job:

When you specify a Python shell job (JobCommand.Name ="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
When you specify an Apache Spark ETL job (JobCommand.Name ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.


WorkerType (string) --
The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
For the G.2X worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.


NumberOfWorkers (integer) --
The number of workers of a defined workerType that are allocated when a job runs.
The maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this job run.

LogGroupName (string) --
The name of the log group for secure logging that can be server-side encrypted in Amazon CloudWatch using AWS KMS. This name can be /aws-glue/jobs/ , in which case the default encryption is NONE . If you add a role name and SecurityConfiguration name (in other words, /aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/ ), then that security configuration is used to encrypt the log group.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



GlueVersion (string) --
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.
Jobs that are created without specifying a Glue version default to Glue 0.9.







CrawlerDetails (dict) --
Details of the crawler when the node represents a crawler.

Crawls (list) --
A list of crawls represented by the crawl node.

(dict) --
The details of a crawl in the workflow.

State (string) --
The state of the crawler.

StartedOn (datetime) --
The date and time on which the crawl started.

CompletedOn (datetime) --
The date and time on which the crawl completed.

ErrorMessage (string) --
The error message associated with the crawl.

LogGroup (string) --
The log group associated with the crawl.

LogStream (string) --
The log stream associated with the crawl.











Edges (list) --
A list of all the directed connections between the nodes belonging to the workflow.

(dict) --
An edge represents a directed connection between two AWS Glue components which are part of the workflow the edge belongs to.

SourceId (string) --
The unique of the node within the workflow where the edge starts.

DestinationId (string) --
The unique of the node within the workflow where the edge ends.









Graph (dict) --
The graph representing all the AWS Glue components that belong to the workflow as nodes and directed connections between them as edges.

Nodes (list) --
A list of the the AWS Glue components belong to the workflow represented as nodes.

(dict) --
A node represents an AWS Glue component like Trigger, Job etc. which is part of a workflow.

Type (string) --
The type of AWS Glue component represented by the node.

Name (string) --
The name of the AWS Glue component represented by the node.

UniqueId (string) --
The unique Id assigned to the node within the workflow.

TriggerDetails (dict) --
Details of the Trigger when the node represents a Trigger.

Trigger (dict) --
The information of the trigger represented by the trigger node.

Name (string) --
The name of the trigger.

WorkflowName (string) --
The name of the workflow associated with the trigger.

Id (string) --
Reserved for future use.

Type (string) --
The type of trigger that this is.

State (string) --
The current state of the trigger.

Description (string) --
A description of this trigger.

Schedule (string) --
A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .

Actions (list) --
The actions initiated by this trigger.

(dict) --
Defines an action to be initiated by a trigger.

JobName (string) --
The name of a job to be executed.

Arguments (dict) --
The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this action.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



CrawlerName (string) --
The name of the crawler to be used with this action.





Predicate (dict) --
The predicate of this trigger, which defines when it will fire.

Logical (string) --
An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.

Conditions (list) --
A list of the conditions that determine when the trigger will fire.

(dict) --
Defines a condition under which a trigger fires.

LogicalOperator (string) --
A logical operator.

JobName (string) --
The name of the job whose JobRuns this condition applies to, and on which this trigger waits.

State (string) --
The condition state. Currently, the only job states that a trigger can listen for are SUCCEEDED , STOPPED , FAILED , and TIMEOUT . The only crawler states that a trigger can listen for are SUCCEEDED , FAILED , and CANCELLED .

CrawlerName (string) --
The name of the crawler to which this condition applies.

CrawlState (string) --
The state of the crawler to which this condition applies.











JobDetails (dict) --
Details of the Job when the node represents a Job.

JobRuns (list) --
The information for the job runs represented by the job node.

(dict) --
Contains information about a job run.

Id (string) --
The ID of this job run.

Attempt (integer) --
The number of the attempt to run this job.

PreviousRunId (string) --
The ID of the previous run of this job. For example, the JobRunId specified in the StartJobRun action.

TriggerName (string) --
The name of the trigger that started this job run.

JobName (string) --
The name of the job definition being used in this run.

StartedOn (datetime) --
The date and time at which this job run was started.

LastModifiedOn (datetime) --
The last time that this job run was modified.

CompletedOn (datetime) --
The date and time that this job run completed.

JobRunState (string) --
The current state of the job run. For more information about the statuses of jobs that have terminated abnormally, see AWS Glue Job Run Statuses .

Arguments (dict) --
The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




ErrorMessage (string) --
An error message associated with this job run.

PredecessorRuns (list) --
A list of predecessors to this job run.

(dict) --
A job run that was used in the predicate of a conditional trigger that triggered this job run.

JobName (string) --
The name of the job definition used by the predecessor job run.

RunId (string) --
The job-run ID of the predecessor job run.





AllocatedCapacity (integer) --
This field is deprecated. Use MaxCapacity instead.
The number of AWS Glue data processing units (DPUs) allocated to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .

ExecutionTime (integer) --
The amount of time (in seconds) that the job run consumed resources.

Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

MaxCapacity (float) --
The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .
Do not set Max Capacity if using WorkerType and NumberOfWorkers .
The value that can be allocated for MaxCapacity depends on whether you are running a Python shell job or an Apache Spark ETL job:

When you specify a Python shell job (JobCommand.Name ="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
When you specify an Apache Spark ETL job (JobCommand.Name ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.


WorkerType (string) --
The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
For the G.2X worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.


NumberOfWorkers (integer) --
The number of workers of a defined workerType that are allocated when a job runs.
The maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this job run.

LogGroupName (string) --
The name of the log group for secure logging that can be server-side encrypted in Amazon CloudWatch using AWS KMS. This name can be /aws-glue/jobs/ , in which case the default encryption is NONE . If you add a role name and SecurityConfiguration name (in other words, /aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/ ), then that security configuration is used to encrypt the log group.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



GlueVersion (string) --
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.
Jobs that are created without specifying a Glue version default to Glue 0.9.







CrawlerDetails (dict) --
Details of the crawler when the node represents a crawler.

Crawls (list) --
A list of crawls represented by the crawl node.

(dict) --
The details of a crawl in the workflow.

State (string) --
The state of the crawler.

StartedOn (datetime) --
The date and time on which the crawl started.

CompletedOn (datetime) --
The date and time on which the crawl completed.

ErrorMessage (string) --
The error message associated with the crawl.

LogGroup (string) --
The log group associated with the crawl.

LogStream (string) --
The log stream associated with the crawl.











Edges (list) --
A list of all the directed connections between the nodes belonging to the workflow.

(dict) --
An edge represents a directed connection between two AWS Glue components which are part of the workflow the edge belongs to.

SourceId (string) --
The unique of the node within the workflow where the edge starts.

DestinationId (string) --
The unique of the node within the workflow where the edge ends.















Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Workflow': {
            'Name': 'string',
            'Description': 'string',
            'DefaultRunProperties': {
                'string': 'string'
            },
            'CreatedOn': datetime(2015, 1, 1),
            'LastModifiedOn': datetime(2015, 1, 1),
            'LastRun': {
                'Name': 'string',
                'WorkflowRunId': 'string',
                'WorkflowRunProperties': {
                    'string': 'string'
                },
                'StartedOn': datetime(2015, 1, 1),
                'CompletedOn': datetime(2015, 1, 1),
                'Status': 'RUNNING'|'COMPLETED'|'STOPPING'|'STOPPED',
                'Statistics': {
                    'TotalActions': 123,
                    'TimeoutActions': 123,
                    'FailedActions': 123,
                    'StoppedActions': 123,
                    'SucceededActions': 123,
                    'RunningActions': 123
                },
                'Graph': {
                    'Nodes': [
                        {
                            'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                            'Name': 'string',
                            'UniqueId': 'string',
                            'TriggerDetails': {
                                'Trigger': {
                                    'Name': 'string',
                                    'WorkflowName': 'string',
                                    'Id': 'string',
                                    'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                    'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                                    'Description': 'string',
                                    'Schedule': 'string',
                                    'Actions': [
                                        {
                                            'JobName': 'string',
                                            'Arguments': {
                                                'string': 'string'
                                            },
                                            'Timeout': 123,
                                            'SecurityConfiguration': 'string',
                                            'NotificationProperty': {
                                                'NotifyDelayAfter': 123
                                            },
                                            'CrawlerName': 'string'
                                        },
                                    ],
                                    'Predicate': {
                                        'Logical': 'AND'|'ANY',
                                        'Conditions': [
                                            {
                                                'LogicalOperator': 'EQUALS',
                                                'JobName': 'string',
                                                'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                                'CrawlerName': 'string',
                                                'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                                            },
                                        ]
                                    }
                                }
                            },
                            'JobDetails': {
                                'JobRuns': [
                                    {
                                        'Id': 'string',
                                        'Attempt': 123,
                                        'PreviousRunId': 'string',
                                        'TriggerName': 'string',
                                        'JobName': 'string',
                                        'StartedOn': datetime(2015, 1, 1),
                                        'LastModifiedOn': datetime(2015, 1, 1),
                                        'CompletedOn': datetime(2015, 1, 1),
                                        'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                        'Arguments': {
                                            'string': 'string'
                                        },
                                        'ErrorMessage': 'string',
                                        'PredecessorRuns': [
                                            {
                                                'JobName': 'string',
                                                'RunId': 'string'
                                            },
                                        ],
                                        'AllocatedCapacity': 123,
                                        'ExecutionTime': 123,
                                        'Timeout': 123,
                                        'MaxCapacity': 123.0,
                                        'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                        'NumberOfWorkers': 123,
                                        'SecurityConfiguration': 'string',
                                        'LogGroupName': 'string',
                                        'NotificationProperty': {
                                            'NotifyDelayAfter': 123
                                        },
                                        'GlueVersion': 'string'
                                    },
                                ]
                            },
                            'CrawlerDetails': {
                                'Crawls': [
                                    {
                                        'State': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED',
                                        'StartedOn': datetime(2015, 1, 1),
                                        'CompletedOn': datetime(2015, 1, 1),
                                        'ErrorMessage': 'string',
                                        'LogGroup': 'string',
                                        'LogStream': 'string'
                                    },
                                ]
                            }
                        },
                    ],
                    'Edges': [
                        {
                            'SourceId': 'string',
                            'DestinationId': 'string'
                        },
                    ]
                }
            },
            'Graph': {
                'Nodes': [
                    {
                        'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                        'Name': 'string',
                        'UniqueId': 'string',
                        'TriggerDetails': {
                            'Trigger': {
                                'Name': 'string',
                                'WorkflowName': 'string',
                                'Id': 'string',
                                'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                                'Description': 'string',
                                'Schedule': 'string',
                                'Actions': [
                                    {
                                        'JobName': 'string',
                                        'Arguments': {
                                            'string': 'string'
                                        },
                                        'Timeout': 123,
                                        'SecurityConfiguration': 'string',
                                        'NotificationProperty': {
                                            'NotifyDelayAfter': 123
                                        },
                                        'CrawlerName': 'string'
                                    },
                                ],
                                'Predicate': {
                                    'Logical': 'AND'|'ANY',
                                    'Conditions': [
                                        {
                                            'LogicalOperator': 'EQUALS',
                                            'JobName': 'string',
                                            'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                            'CrawlerName': 'string',
                                            'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                                        },
                                    ]
                                }
                            }
                        },
                        'JobDetails': {
                            'JobRuns': [
                                {
                                    'Id': 'string',
                                    'Attempt': 123,
                                    'PreviousRunId': 'string',
                                    'TriggerName': 'string',
                                    'JobName': 'string',
                                    'StartedOn': datetime(2015, 1, 1),
                                    'LastModifiedOn': datetime(2015, 1, 1),
                                    'CompletedOn': datetime(2015, 1, 1),
                                    'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                    'Arguments': {
                                        'string': 'string'
                                    },
                                    'ErrorMessage': 'string',
                                    'PredecessorRuns': [
                                        {
                                            'JobName': 'string',
                                            'RunId': 'string'
                                        },
                                    ],
                                    'AllocatedCapacity': 123,
                                    'ExecutionTime': 123,
                                    'Timeout': 123,
                                    'MaxCapacity': 123.0,
                                    'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                    'NumberOfWorkers': 123,
                                    'SecurityConfiguration': 'string',
                                    'LogGroupName': 'string',
                                    'NotificationProperty': {
                                        'NotifyDelayAfter': 123
                                    },
                                    'GlueVersion': 'string'
                                },
                            ]
                        },
                        'CrawlerDetails': {
                            'Crawls': [
                                {
                                    'State': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED',
                                    'StartedOn': datetime(2015, 1, 1),
                                    'CompletedOn': datetime(2015, 1, 1),
                                    'ErrorMessage': 'string',
                                    'LogGroup': 'string',
                                    'LogStream': 'string'
                                },
                            ]
                        }
                    },
                ],
                'Edges': [
                    {
                        'SourceId': 'string',
                        'DestinationId': 'string'
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_workflow_run(Name=None, RunId=None, IncludeGraph=None):
    """
    Retrieves the metadata for a given workflow run.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_workflow_run(
        Name='string',
        RunId='string',
        IncludeGraph=True|False
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the workflow being run.\n

    :type RunId: string
    :param RunId: [REQUIRED]\nThe ID of the workflow run.\n

    :type IncludeGraph: boolean
    :param IncludeGraph: Specifies whether to include the workflow graph in response or not.

    :rtype: dict

ReturnsResponse Syntax
{
    'Run': {
        'Name': 'string',
        'WorkflowRunId': 'string',
        'WorkflowRunProperties': {
            'string': 'string'
        },
        'StartedOn': datetime(2015, 1, 1),
        'CompletedOn': datetime(2015, 1, 1),
        'Status': 'RUNNING'|'COMPLETED'|'STOPPING'|'STOPPED',
        'Statistics': {
            'TotalActions': 123,
            'TimeoutActions': 123,
            'FailedActions': 123,
            'StoppedActions': 123,
            'SucceededActions': 123,
            'RunningActions': 123
        },
        'Graph': {
            'Nodes': [
                {
                    'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                    'Name': 'string',
                    'UniqueId': 'string',
                    'TriggerDetails': {
                        'Trigger': {
                            'Name': 'string',
                            'WorkflowName': 'string',
                            'Id': 'string',
                            'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                            'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                            'Description': 'string',
                            'Schedule': 'string',
                            'Actions': [
                                {
                                    'JobName': 'string',
                                    'Arguments': {
                                        'string': 'string'
                                    },
                                    'Timeout': 123,
                                    'SecurityConfiguration': 'string',
                                    'NotificationProperty': {
                                        'NotifyDelayAfter': 123
                                    },
                                    'CrawlerName': 'string'
                                },
                            ],
                            'Predicate': {
                                'Logical': 'AND'|'ANY',
                                'Conditions': [
                                    {
                                        'LogicalOperator': 'EQUALS',
                                        'JobName': 'string',
                                        'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                        'CrawlerName': 'string',
                                        'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                                    },
                                ]
                            }
                        }
                    },
                    'JobDetails': {
                        'JobRuns': [
                            {
                                'Id': 'string',
                                'Attempt': 123,
                                'PreviousRunId': 'string',
                                'TriggerName': 'string',
                                'JobName': 'string',
                                'StartedOn': datetime(2015, 1, 1),
                                'LastModifiedOn': datetime(2015, 1, 1),
                                'CompletedOn': datetime(2015, 1, 1),
                                'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                'Arguments': {
                                    'string': 'string'
                                },
                                'ErrorMessage': 'string',
                                'PredecessorRuns': [
                                    {
                                        'JobName': 'string',
                                        'RunId': 'string'
                                    },
                                ],
                                'AllocatedCapacity': 123,
                                'ExecutionTime': 123,
                                'Timeout': 123,
                                'MaxCapacity': 123.0,
                                'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                'NumberOfWorkers': 123,
                                'SecurityConfiguration': 'string',
                                'LogGroupName': 'string',
                                'NotificationProperty': {
                                    'NotifyDelayAfter': 123
                                },
                                'GlueVersion': 'string'
                            },
                        ]
                    },
                    'CrawlerDetails': {
                        'Crawls': [
                            {
                                'State': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED',
                                'StartedOn': datetime(2015, 1, 1),
                                'CompletedOn': datetime(2015, 1, 1),
                                'ErrorMessage': 'string',
                                'LogGroup': 'string',
                                'LogStream': 'string'
                            },
                        ]
                    }
                },
            ],
            'Edges': [
                {
                    'SourceId': 'string',
                    'DestinationId': 'string'
                },
            ]
        }
    }
}


Response Structure

(dict) --

Run (dict) --
The requested workflow run metadata.

Name (string) --
Name of the workflow which was executed.

WorkflowRunId (string) --
The ID of this workflow run.

WorkflowRunProperties (dict) --
The workflow run properties which were set during the run.

(string) --
(string) --




StartedOn (datetime) --
The date and time when the workflow run was started.

CompletedOn (datetime) --
The date and time when the workflow run completed.

Status (string) --
The status of the workflow run.

Statistics (dict) --
The statistics of the run.

TotalActions (integer) --
Total number of Actions in the workflow run.

TimeoutActions (integer) --
Total number of Actions which timed out.

FailedActions (integer) --
Total number of Actions which have failed.

StoppedActions (integer) --
Total number of Actions which have stopped.

SucceededActions (integer) --
Total number of Actions which have succeeded.

RunningActions (integer) --
Total number Actions in running state.



Graph (dict) --
The graph representing all the AWS Glue components that belong to the workflow as nodes and directed connections between them as edges.

Nodes (list) --
A list of the the AWS Glue components belong to the workflow represented as nodes.

(dict) --
A node represents an AWS Glue component like Trigger, Job etc. which is part of a workflow.

Type (string) --
The type of AWS Glue component represented by the node.

Name (string) --
The name of the AWS Glue component represented by the node.

UniqueId (string) --
The unique Id assigned to the node within the workflow.

TriggerDetails (dict) --
Details of the Trigger when the node represents a Trigger.

Trigger (dict) --
The information of the trigger represented by the trigger node.

Name (string) --
The name of the trigger.

WorkflowName (string) --
The name of the workflow associated with the trigger.

Id (string) --
Reserved for future use.

Type (string) --
The type of trigger that this is.

State (string) --
The current state of the trigger.

Description (string) --
A description of this trigger.

Schedule (string) --
A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .

Actions (list) --
The actions initiated by this trigger.

(dict) --
Defines an action to be initiated by a trigger.

JobName (string) --
The name of a job to be executed.

Arguments (dict) --
The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this action.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



CrawlerName (string) --
The name of the crawler to be used with this action.





Predicate (dict) --
The predicate of this trigger, which defines when it will fire.

Logical (string) --
An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.

Conditions (list) --
A list of the conditions that determine when the trigger will fire.

(dict) --
Defines a condition under which a trigger fires.

LogicalOperator (string) --
A logical operator.

JobName (string) --
The name of the job whose JobRuns this condition applies to, and on which this trigger waits.

State (string) --
The condition state. Currently, the only job states that a trigger can listen for are SUCCEEDED , STOPPED , FAILED , and TIMEOUT . The only crawler states that a trigger can listen for are SUCCEEDED , FAILED , and CANCELLED .

CrawlerName (string) --
The name of the crawler to which this condition applies.

CrawlState (string) --
The state of the crawler to which this condition applies.











JobDetails (dict) --
Details of the Job when the node represents a Job.

JobRuns (list) --
The information for the job runs represented by the job node.

(dict) --
Contains information about a job run.

Id (string) --
The ID of this job run.

Attempt (integer) --
The number of the attempt to run this job.

PreviousRunId (string) --
The ID of the previous run of this job. For example, the JobRunId specified in the StartJobRun action.

TriggerName (string) --
The name of the trigger that started this job run.

JobName (string) --
The name of the job definition being used in this run.

StartedOn (datetime) --
The date and time at which this job run was started.

LastModifiedOn (datetime) --
The last time that this job run was modified.

CompletedOn (datetime) --
The date and time that this job run completed.

JobRunState (string) --
The current state of the job run. For more information about the statuses of jobs that have terminated abnormally, see AWS Glue Job Run Statuses .

Arguments (dict) --
The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




ErrorMessage (string) --
An error message associated with this job run.

PredecessorRuns (list) --
A list of predecessors to this job run.

(dict) --
A job run that was used in the predicate of a conditional trigger that triggered this job run.

JobName (string) --
The name of the job definition used by the predecessor job run.

RunId (string) --
The job-run ID of the predecessor job run.





AllocatedCapacity (integer) --
This field is deprecated. Use MaxCapacity instead.
The number of AWS Glue data processing units (DPUs) allocated to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .

ExecutionTime (integer) --
The amount of time (in seconds) that the job run consumed resources.

Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

MaxCapacity (float) --
The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .
Do not set Max Capacity if using WorkerType and NumberOfWorkers .
The value that can be allocated for MaxCapacity depends on whether you are running a Python shell job or an Apache Spark ETL job:

When you specify a Python shell job (JobCommand.Name ="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
When you specify an Apache Spark ETL job (JobCommand.Name ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.


WorkerType (string) --
The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
For the G.2X worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.


NumberOfWorkers (integer) --
The number of workers of a defined workerType that are allocated when a job runs.
The maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this job run.

LogGroupName (string) --
The name of the log group for secure logging that can be server-side encrypted in Amazon CloudWatch using AWS KMS. This name can be /aws-glue/jobs/ , in which case the default encryption is NONE . If you add a role name and SecurityConfiguration name (in other words, /aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/ ), then that security configuration is used to encrypt the log group.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



GlueVersion (string) --
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.
Jobs that are created without specifying a Glue version default to Glue 0.9.







CrawlerDetails (dict) --
Details of the crawler when the node represents a crawler.

Crawls (list) --
A list of crawls represented by the crawl node.

(dict) --
The details of a crawl in the workflow.

State (string) --
The state of the crawler.

StartedOn (datetime) --
The date and time on which the crawl started.

CompletedOn (datetime) --
The date and time on which the crawl completed.

ErrorMessage (string) --
The error message associated with the crawl.

LogGroup (string) --
The log group associated with the crawl.

LogStream (string) --
The log stream associated with the crawl.











Edges (list) --
A list of all the directed connections between the nodes belonging to the workflow.

(dict) --
An edge represents a directed connection between two AWS Glue components which are part of the workflow the edge belongs to.

SourceId (string) --
The unique of the node within the workflow where the edge starts.

DestinationId (string) --
The unique of the node within the workflow where the edge ends.















Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Run': {
            'Name': 'string',
            'WorkflowRunId': 'string',
            'WorkflowRunProperties': {
                'string': 'string'
            },
            'StartedOn': datetime(2015, 1, 1),
            'CompletedOn': datetime(2015, 1, 1),
            'Status': 'RUNNING'|'COMPLETED'|'STOPPING'|'STOPPED',
            'Statistics': {
                'TotalActions': 123,
                'TimeoutActions': 123,
                'FailedActions': 123,
                'StoppedActions': 123,
                'SucceededActions': 123,
                'RunningActions': 123
            },
            'Graph': {
                'Nodes': [
                    {
                        'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                        'Name': 'string',
                        'UniqueId': 'string',
                        'TriggerDetails': {
                            'Trigger': {
                                'Name': 'string',
                                'WorkflowName': 'string',
                                'Id': 'string',
                                'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                                'Description': 'string',
                                'Schedule': 'string',
                                'Actions': [
                                    {
                                        'JobName': 'string',
                                        'Arguments': {
                                            'string': 'string'
                                        },
                                        'Timeout': 123,
                                        'SecurityConfiguration': 'string',
                                        'NotificationProperty': {
                                            'NotifyDelayAfter': 123
                                        },
                                        'CrawlerName': 'string'
                                    },
                                ],
                                'Predicate': {
                                    'Logical': 'AND'|'ANY',
                                    'Conditions': [
                                        {
                                            'LogicalOperator': 'EQUALS',
                                            'JobName': 'string',
                                            'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                            'CrawlerName': 'string',
                                            'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                                        },
                                    ]
                                }
                            }
                        },
                        'JobDetails': {
                            'JobRuns': [
                                {
                                    'Id': 'string',
                                    'Attempt': 123,
                                    'PreviousRunId': 'string',
                                    'TriggerName': 'string',
                                    'JobName': 'string',
                                    'StartedOn': datetime(2015, 1, 1),
                                    'LastModifiedOn': datetime(2015, 1, 1),
                                    'CompletedOn': datetime(2015, 1, 1),
                                    'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                    'Arguments': {
                                        'string': 'string'
                                    },
                                    'ErrorMessage': 'string',
                                    'PredecessorRuns': [
                                        {
                                            'JobName': 'string',
                                            'RunId': 'string'
                                        },
                                    ],
                                    'AllocatedCapacity': 123,
                                    'ExecutionTime': 123,
                                    'Timeout': 123,
                                    'MaxCapacity': 123.0,
                                    'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                    'NumberOfWorkers': 123,
                                    'SecurityConfiguration': 'string',
                                    'LogGroupName': 'string',
                                    'NotificationProperty': {
                                        'NotifyDelayAfter': 123
                                    },
                                    'GlueVersion': 'string'
                                },
                            ]
                        },
                        'CrawlerDetails': {
                            'Crawls': [
                                {
                                    'State': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED',
                                    'StartedOn': datetime(2015, 1, 1),
                                    'CompletedOn': datetime(2015, 1, 1),
                                    'ErrorMessage': 'string',
                                    'LogGroup': 'string',
                                    'LogStream': 'string'
                                },
                            ]
                        }
                    },
                ],
                'Edges': [
                    {
                        'SourceId': 'string',
                        'DestinationId': 'string'
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_workflow_run_properties(Name=None, RunId=None):
    """
    Retrieves the workflow run properties which were set during the run.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_workflow_run_properties(
        Name='string',
        RunId='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the workflow which was run.\n

    :type RunId: string
    :param RunId: [REQUIRED]\nThe ID of the workflow run whose run properties should be returned.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RunProperties': {
        'string': 'string'
    }
}


Response Structure

(dict) --

RunProperties (dict) --
The workflow run properties which were set during the specified run.

(string) --
(string) --










Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'RunProperties': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_workflow_runs(Name=None, IncludeGraph=None, NextToken=None, MaxResults=None):
    """
    Retrieves metadata for all runs of a given workflow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_workflow_runs(
        Name='string',
        IncludeGraph=True|False,
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the workflow whose metadata of runs should be returned.\n

    :type IncludeGraph: boolean
    :param IncludeGraph: Specifies whether to include the workflow graph in response or not.

    :type NextToken: string
    :param NextToken: The maximum size of the response.

    :type MaxResults: integer
    :param MaxResults: The maximum number of workflow runs to be included in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'Runs': [
        {
            'Name': 'string',
            'WorkflowRunId': 'string',
            'WorkflowRunProperties': {
                'string': 'string'
            },
            'StartedOn': datetime(2015, 1, 1),
            'CompletedOn': datetime(2015, 1, 1),
            'Status': 'RUNNING'|'COMPLETED'|'STOPPING'|'STOPPED',
            'Statistics': {
                'TotalActions': 123,
                'TimeoutActions': 123,
                'FailedActions': 123,
                'StoppedActions': 123,
                'SucceededActions': 123,
                'RunningActions': 123
            },
            'Graph': {
                'Nodes': [
                    {
                        'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                        'Name': 'string',
                        'UniqueId': 'string',
                        'TriggerDetails': {
                            'Trigger': {
                                'Name': 'string',
                                'WorkflowName': 'string',
                                'Id': 'string',
                                'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                                'Description': 'string',
                                'Schedule': 'string',
                                'Actions': [
                                    {
                                        'JobName': 'string',
                                        'Arguments': {
                                            'string': 'string'
                                        },
                                        'Timeout': 123,
                                        'SecurityConfiguration': 'string',
                                        'NotificationProperty': {
                                            'NotifyDelayAfter': 123
                                        },
                                        'CrawlerName': 'string'
                                    },
                                ],
                                'Predicate': {
                                    'Logical': 'AND'|'ANY',
                                    'Conditions': [
                                        {
                                            'LogicalOperator': 'EQUALS',
                                            'JobName': 'string',
                                            'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                            'CrawlerName': 'string',
                                            'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                                        },
                                    ]
                                }
                            }
                        },
                        'JobDetails': {
                            'JobRuns': [
                                {
                                    'Id': 'string',
                                    'Attempt': 123,
                                    'PreviousRunId': 'string',
                                    'TriggerName': 'string',
                                    'JobName': 'string',
                                    'StartedOn': datetime(2015, 1, 1),
                                    'LastModifiedOn': datetime(2015, 1, 1),
                                    'CompletedOn': datetime(2015, 1, 1),
                                    'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                    'Arguments': {
                                        'string': 'string'
                                    },
                                    'ErrorMessage': 'string',
                                    'PredecessorRuns': [
                                        {
                                            'JobName': 'string',
                                            'RunId': 'string'
                                        },
                                    ],
                                    'AllocatedCapacity': 123,
                                    'ExecutionTime': 123,
                                    'Timeout': 123,
                                    'MaxCapacity': 123.0,
                                    'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                    'NumberOfWorkers': 123,
                                    'SecurityConfiguration': 'string',
                                    'LogGroupName': 'string',
                                    'NotificationProperty': {
                                        'NotifyDelayAfter': 123
                                    },
                                    'GlueVersion': 'string'
                                },
                            ]
                        },
                        'CrawlerDetails': {
                            'Crawls': [
                                {
                                    'State': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED',
                                    'StartedOn': datetime(2015, 1, 1),
                                    'CompletedOn': datetime(2015, 1, 1),
                                    'ErrorMessage': 'string',
                                    'LogGroup': 'string',
                                    'LogStream': 'string'
                                },
                            ]
                        }
                    },
                ],
                'Edges': [
                    {
                        'SourceId': 'string',
                        'DestinationId': 'string'
                    },
                ]
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Runs (list) --
A list of workflow run metadata objects.

(dict) --
A workflow run is an execution of a workflow providing all the runtime information.

Name (string) --
Name of the workflow which was executed.

WorkflowRunId (string) --
The ID of this workflow run.

WorkflowRunProperties (dict) --
The workflow run properties which were set during the run.

(string) --
(string) --




StartedOn (datetime) --
The date and time when the workflow run was started.

CompletedOn (datetime) --
The date and time when the workflow run completed.

Status (string) --
The status of the workflow run.

Statistics (dict) --
The statistics of the run.

TotalActions (integer) --
Total number of Actions in the workflow run.

TimeoutActions (integer) --
Total number of Actions which timed out.

FailedActions (integer) --
Total number of Actions which have failed.

StoppedActions (integer) --
Total number of Actions which have stopped.

SucceededActions (integer) --
Total number of Actions which have succeeded.

RunningActions (integer) --
Total number Actions in running state.



Graph (dict) --
The graph representing all the AWS Glue components that belong to the workflow as nodes and directed connections between them as edges.

Nodes (list) --
A list of the the AWS Glue components belong to the workflow represented as nodes.

(dict) --
A node represents an AWS Glue component like Trigger, Job etc. which is part of a workflow.

Type (string) --
The type of AWS Glue component represented by the node.

Name (string) --
The name of the AWS Glue component represented by the node.

UniqueId (string) --
The unique Id assigned to the node within the workflow.

TriggerDetails (dict) --
Details of the Trigger when the node represents a Trigger.

Trigger (dict) --
The information of the trigger represented by the trigger node.

Name (string) --
The name of the trigger.

WorkflowName (string) --
The name of the workflow associated with the trigger.

Id (string) --
Reserved for future use.

Type (string) --
The type of trigger that this is.

State (string) --
The current state of the trigger.

Description (string) --
A description of this trigger.

Schedule (string) --
A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .

Actions (list) --
The actions initiated by this trigger.

(dict) --
Defines an action to be initiated by a trigger.

JobName (string) --
The name of a job to be executed.

Arguments (dict) --
The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this action.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



CrawlerName (string) --
The name of the crawler to be used with this action.





Predicate (dict) --
The predicate of this trigger, which defines when it will fire.

Logical (string) --
An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.

Conditions (list) --
A list of the conditions that determine when the trigger will fire.

(dict) --
Defines a condition under which a trigger fires.

LogicalOperator (string) --
A logical operator.

JobName (string) --
The name of the job whose JobRuns this condition applies to, and on which this trigger waits.

State (string) --
The condition state. Currently, the only job states that a trigger can listen for are SUCCEEDED , STOPPED , FAILED , and TIMEOUT . The only crawler states that a trigger can listen for are SUCCEEDED , FAILED , and CANCELLED .

CrawlerName (string) --
The name of the crawler to which this condition applies.

CrawlState (string) --
The state of the crawler to which this condition applies.











JobDetails (dict) --
Details of the Job when the node represents a Job.

JobRuns (list) --
The information for the job runs represented by the job node.

(dict) --
Contains information about a job run.

Id (string) --
The ID of this job run.

Attempt (integer) --
The number of the attempt to run this job.

PreviousRunId (string) --
The ID of the previous run of this job. For example, the JobRunId specified in the StartJobRun action.

TriggerName (string) --
The name of the trigger that started this job run.

JobName (string) --
The name of the job definition being used in this run.

StartedOn (datetime) --
The date and time at which this job run was started.

LastModifiedOn (datetime) --
The last time that this job run was modified.

CompletedOn (datetime) --
The date and time that this job run completed.

JobRunState (string) --
The current state of the job run. For more information about the statuses of jobs that have terminated abnormally, see AWS Glue Job Run Statuses .

Arguments (dict) --
The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




ErrorMessage (string) --
An error message associated with this job run.

PredecessorRuns (list) --
A list of predecessors to this job run.

(dict) --
A job run that was used in the predicate of a conditional trigger that triggered this job run.

JobName (string) --
The name of the job definition used by the predecessor job run.

RunId (string) --
The job-run ID of the predecessor job run.





AllocatedCapacity (integer) --
This field is deprecated. Use MaxCapacity instead.
The number of AWS Glue data processing units (DPUs) allocated to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .

ExecutionTime (integer) --
The amount of time (in seconds) that the job run consumed resources.

Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

MaxCapacity (float) --
The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .
Do not set Max Capacity if using WorkerType and NumberOfWorkers .
The value that can be allocated for MaxCapacity depends on whether you are running a Python shell job or an Apache Spark ETL job:

When you specify a Python shell job (JobCommand.Name ="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
When you specify an Apache Spark ETL job (JobCommand.Name ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.


WorkerType (string) --
The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.

For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
For the G.1X worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
For the G.2X worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.


NumberOfWorkers (integer) --
The number of workers of a defined workerType that are allocated when a job runs.
The maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this job run.

LogGroupName (string) --
The name of the log group for secure logging that can be server-side encrypted in Amazon CloudWatch using AWS KMS. This name can be /aws-glue/jobs/ , in which case the default encryption is NONE . If you add a role name and SecurityConfiguration name (in other words, /aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/ ), then that security configuration is used to encrypt the log group.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



GlueVersion (string) --
Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark.
For more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.
Jobs that are created without specifying a Glue version default to Glue 0.9.







CrawlerDetails (dict) --
Details of the crawler when the node represents a crawler.

Crawls (list) --
A list of crawls represented by the crawl node.

(dict) --
The details of a crawl in the workflow.

State (string) --
The state of the crawler.

StartedOn (datetime) --
The date and time on which the crawl started.

CompletedOn (datetime) --
The date and time on which the crawl completed.

ErrorMessage (string) --
The error message associated with the crawl.

LogGroup (string) --
The log group associated with the crawl.

LogStream (string) --
The log stream associated with the crawl.











Edges (list) --
A list of all the directed connections between the nodes belonging to the workflow.

(dict) --
An edge represents a directed connection between two AWS Glue components which are part of the workflow the edge belongs to.

SourceId (string) --
The unique of the node within the workflow where the edge starts.

DestinationId (string) --
The unique of the node within the workflow where the edge ends.











NextToken (string) --
A continuation token, if not all requested workflow runs have been returned.







Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Runs': [
            {
                'Name': 'string',
                'WorkflowRunId': 'string',
                'WorkflowRunProperties': {
                    'string': 'string'
                },
                'StartedOn': datetime(2015, 1, 1),
                'CompletedOn': datetime(2015, 1, 1),
                'Status': 'RUNNING'|'COMPLETED'|'STOPPING'|'STOPPED',
                'Statistics': {
                    'TotalActions': 123,
                    'TimeoutActions': 123,
                    'FailedActions': 123,
                    'StoppedActions': 123,
                    'SucceededActions': 123,
                    'RunningActions': 123
                },
                'Graph': {
                    'Nodes': [
                        {
                            'Type': 'CRAWLER'|'JOB'|'TRIGGER',
                            'Name': 'string',
                            'UniqueId': 'string',
                            'TriggerDetails': {
                                'Trigger': {
                                    'Name': 'string',
                                    'WorkflowName': 'string',
                                    'Id': 'string',
                                    'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                                    'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
                                    'Description': 'string',
                                    'Schedule': 'string',
                                    'Actions': [
                                        {
                                            'JobName': 'string',
                                            'Arguments': {
                                                'string': 'string'
                                            },
                                            'Timeout': 123,
                                            'SecurityConfiguration': 'string',
                                            'NotificationProperty': {
                                                'NotifyDelayAfter': 123
                                            },
                                            'CrawlerName': 'string'
                                        },
                                    ],
                                    'Predicate': {
                                        'Logical': 'AND'|'ANY',
                                        'Conditions': [
                                            {
                                                'LogicalOperator': 'EQUALS',
                                                'JobName': 'string',
                                                'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                                'CrawlerName': 'string',
                                                'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                                            },
                                        ]
                                    }
                                }
                            },
                            'JobDetails': {
                                'JobRuns': [
                                    {
                                        'Id': 'string',
                                        'Attempt': 123,
                                        'PreviousRunId': 'string',
                                        'TriggerName': 'string',
                                        'JobName': 'string',
                                        'StartedOn': datetime(2015, 1, 1),
                                        'LastModifiedOn': datetime(2015, 1, 1),
                                        'CompletedOn': datetime(2015, 1, 1),
                                        'JobRunState': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                                        'Arguments': {
                                            'string': 'string'
                                        },
                                        'ErrorMessage': 'string',
                                        'PredecessorRuns': [
                                            {
                                                'JobName': 'string',
                                                'RunId': 'string'
                                            },
                                        ],
                                        'AllocatedCapacity': 123,
                                        'ExecutionTime': 123,
                                        'Timeout': 123,
                                        'MaxCapacity': 123.0,
                                        'WorkerType': 'Standard'|'G.1X'|'G.2X',
                                        'NumberOfWorkers': 123,
                                        'SecurityConfiguration': 'string',
                                        'LogGroupName': 'string',
                                        'NotificationProperty': {
                                            'NotifyDelayAfter': 123
                                        },
                                        'GlueVersion': 'string'
                                    },
                                ]
                            },
                            'CrawlerDetails': {
                                'Crawls': [
                                    {
                                        'State': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED',
                                        'StartedOn': datetime(2015, 1, 1),
                                        'CompletedOn': datetime(2015, 1, 1),
                                        'ErrorMessage': 'string',
                                        'LogGroup': 'string',
                                        'LogStream': 'string'
                                    },
                                ]
                            }
                        },
                    ],
                    'Edges': [
                        {
                            'SourceId': 'string',
                            'DestinationId': 'string'
                        },
                    ]
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def import_catalog_to_glue(CatalogId=None):
    """
    Imports an existing Amazon Athena Data Catalog to AWS Glue
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.import_catalog_to_glue(
        CatalogId='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the catalog to import. Currently, this should be the AWS account ID.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def list_crawlers(MaxResults=None, NextToken=None, Tags=None):
    """
    Retrieves the names of all crawler resources in this AWS account, or the resources with the specified tag. This operation allows you to see which resources are available in your account, and their names.
    This operation takes the optional Tags field, which you can use as a filter on the response so that tagged resources can be retrieved as a group. If you choose to use tags filtering, only resources with the tag are retrieved.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_crawlers(
        MaxResults=123,
        NextToken='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum size of a list to return.

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation request.

    :type Tags: dict
    :param Tags: Specifies to return only these tagged resources.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CrawlerNames': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

CrawlerNames (list) --
The names of all crawlers in the account, or the crawlers with the specified tags.

(string) --


NextToken (string) --
A continuation token, if the returned list does not contain the last metric available.







Exceptions

Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'CrawlerNames': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_dev_endpoints(NextToken=None, MaxResults=None, Tags=None):
    """
    Retrieves the names of all DevEndpoint resources in this AWS account, or the resources with the specified tag. This operation allows you to see which resources are available in your account, and their names.
    This operation takes the optional Tags field, which you can use as a filter on the response so that tagged resources can be retrieved as a group. If you choose to use tags filtering, only resources with the tag are retrieved.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_dev_endpoints(
        NextToken='string',
        MaxResults=123,
        Tags={
            'string': 'string'
        }
    )
    
    
    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation request.

    :type MaxResults: integer
    :param MaxResults: The maximum size of a list to return.

    :type Tags: dict
    :param Tags: Specifies to return only these tagged resources.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DevEndpointNames': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

DevEndpointNames (list) --
The names of all the DevEndpoint s in the account, or the DevEndpoint s with the specified tags.

(string) --


NextToken (string) --
A continuation token, if the returned list does not contain the last metric available.







Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'DevEndpointNames': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_jobs(NextToken=None, MaxResults=None, Tags=None):
    """
    Retrieves the names of all job resources in this AWS account, or the resources with the specified tag. This operation allows you to see which resources are available in your account, and their names.
    This operation takes the optional Tags field, which you can use as a filter on the response so that tagged resources can be retrieved as a group. If you choose to use tags filtering, only resources with the tag are retrieved.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_jobs(
        NextToken='string',
        MaxResults=123,
        Tags={
            'string': 'string'
        }
    )
    
    
    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation request.

    :type MaxResults: integer
    :param MaxResults: The maximum size of a list to return.

    :type Tags: dict
    :param Tags: Specifies to return only these tagged resources.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobNames': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

JobNames (list) --
The names of all jobs in the account, or the jobs with the specified tags.

(string) --


NextToken (string) --
A continuation token, if the returned list does not contain the last metric available.







Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'JobNames': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_ml_transforms(NextToken=None, MaxResults=None, Filter=None, Sort=None, Tags=None):
    """
    Retrieves a sortable, filterable list of existing AWS Glue machine learning transforms in this AWS account, or the resources with the specified tag. This operation takes the optional Tags field, which you can use as a filter of the responses so that tagged resources can be retrieved as a group. If you choose to use tag filtering, only resources with the tags are retrieved.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_ml_transforms(
        NextToken='string',
        MaxResults=123,
        Filter={
            'Name': 'string',
            'TransformType': 'FIND_MATCHES',
            'Status': 'NOT_READY'|'READY'|'DELETING',
            'GlueVersion': 'string',
            'CreatedBefore': datetime(2015, 1, 1),
            'CreatedAfter': datetime(2015, 1, 1),
            'LastModifiedBefore': datetime(2015, 1, 1),
            'LastModifiedAfter': datetime(2015, 1, 1),
            'Schema': [
                {
                    'Name': 'string',
                    'DataType': 'string'
                },
            ]
        },
        Sort={
            'Column': 'NAME'|'TRANSFORM_TYPE'|'STATUS'|'CREATED'|'LAST_MODIFIED',
            'SortDirection': 'DESCENDING'|'ASCENDING'
        },
        Tags={
            'string': 'string'
        }
    )
    
    
    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation request.

    :type MaxResults: integer
    :param MaxResults: The maximum size of a list to return.

    :type Filter: dict
    :param Filter: A TransformFilterCriteria used to filter the machine learning transforms.\n\nName (string) --A unique transform name that is used to filter the machine learning transforms.\n\nTransformType (string) --The type of machine learning transform that is used to filter the machine learning transforms.\n\nStatus (string) --Filters the list of machine learning transforms by the last known status of the transforms (to indicate whether a transform can be used or not). One of 'NOT_READY', 'READY', or 'DELETING'.\n\nGlueVersion (string) --This value determines which version of AWS Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see AWS Glue Versions in the developer guide.\n\nCreatedBefore (datetime) --The time and date before which the transforms were created.\n\nCreatedAfter (datetime) --The time and date after which the transforms were created.\n\nLastModifiedBefore (datetime) --Filter on transforms last modified before this date.\n\nLastModifiedAfter (datetime) --Filter on transforms last modified after this date.\n\nSchema (list) --Filters on datasets with a specific schema. The Map<Column, Type> object is an array of key-value pairs representing the schema this transform accepts, where Column is the name of a column, and Type is the type of the data such as an integer or string. Has an upper bound of 100 columns.\n\n(dict) --A key-value pair representing a column and data type that this transform can run against. The Schema parameter of the MLTransform may contain up to 100 of these structures.\n\nName (string) --The name of the column.\n\nDataType (string) --The type of data in the column.\n\n\n\n\n\n\n

    :type Sort: dict
    :param Sort: A TransformSortCriteria used to sort the machine learning transforms.\n\nColumn (string) -- [REQUIRED]The column to be used in the sorting criteria that are associated with the machine learning transform.\n\nSortDirection (string) -- [REQUIRED]The sort direction to be used in the sorting criteria that are associated with the machine learning transform.\n\n\n

    :type Tags: dict
    :param Tags: Specifies to return only these tagged resources.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TransformIds': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

TransformIds (list) --
The identifiers of all the machine learning transforms in the account, or the machine learning transforms with the specified tags.

(string) --


NextToken (string) --
A continuation token, if the returned list does not contain the last metric available.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException


    :return: {
        'TransformIds': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_triggers(NextToken=None, DependentJobName=None, MaxResults=None, Tags=None):
    """
    Retrieves the names of all trigger resources in this AWS account, or the resources with the specified tag. This operation allows you to see which resources are available in your account, and their names.
    This operation takes the optional Tags field, which you can use as a filter on the response so that tagged resources can be retrieved as a group. If you choose to use tags filtering, only resources with the tag are retrieved.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_triggers(
        NextToken='string',
        DependentJobName='string',
        MaxResults=123,
        Tags={
            'string': 'string'
        }
    )
    
    
    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation request.

    :type DependentJobName: string
    :param DependentJobName: The name of the job for which to retrieve triggers. The trigger that can start this job is returned. If there is no such trigger, all triggers are returned.

    :type MaxResults: integer
    :param MaxResults: The maximum size of a list to return.

    :type Tags: dict
    :param Tags: Specifies to return only these tagged resources.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TriggerNames': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

TriggerNames (list) --
The names of all triggers in the account, or the triggers with the specified tags.

(string) --


NextToken (string) --
A continuation token, if the returned list does not contain the last metric available.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'TriggerNames': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_workflows(NextToken=None, MaxResults=None):
    """
    Lists names of workflows created in the account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_workflows(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation request.

    :type MaxResults: integer
    :param MaxResults: The maximum size of a list to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'Workflows': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Workflows (list) --
List of names of workflows in the account.

(string) --


NextToken (string) --
A continuation token, if not all workflow names have been returned.







Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'Workflows': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_data_catalog_encryption_settings(CatalogId=None, DataCatalogEncryptionSettings=None):
    """
    Sets the security configuration for a specified catalog. After the configuration has been set, the specified encryption is applied to every catalog write thereafter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_data_catalog_encryption_settings(
        CatalogId='string',
        DataCatalogEncryptionSettings={
            'EncryptionAtRest': {
                'CatalogEncryptionMode': 'DISABLED'|'SSE-KMS',
                'SseAwsKmsKeyId': 'string'
            },
            'ConnectionPasswordEncryption': {
                'ReturnConnectionPasswordEncrypted': True|False,
                'AwsKmsKeyId': 'string'
            }
        }
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog to set the security configuration for. If none is provided, the AWS account ID is used by default.

    :type DataCatalogEncryptionSettings: dict
    :param DataCatalogEncryptionSettings: [REQUIRED]\nThe security configuration to set.\n\nEncryptionAtRest (dict) --Specifies the encryption-at-rest configuration for the Data Catalog.\n\nCatalogEncryptionMode (string) -- [REQUIRED]The encryption-at-rest mode for encrypting Data Catalog data.\n\nSseAwsKmsKeyId (string) --The ID of the AWS KMS key to use for encryption at rest.\n\n\n\nConnectionPasswordEncryption (dict) --When connection password protection is enabled, the Data Catalog uses a customer-provided key to encrypt the password as part of CreateConnection or UpdateConnection and store it in the ENCRYPTED_PASSWORD field in the connection properties. You can enable catalog encryption or only password encryption.\n\nReturnConnectionPasswordEncrypted (boolean) -- [REQUIRED]When the ReturnConnectionPasswordEncrypted flag is set to 'true', passwords remain encrypted in the responses of GetConnection and GetConnections . This encryption takes effect independently from catalog encryption.\n\nAwsKmsKeyId (string) --An AWS KMS key that is used to encrypt the connection password.\nIf connection password protection is enabled, the caller of CreateConnection and UpdateConnection needs at least kms:Encrypt permission on the specified AWS KMS key, to encrypt passwords before storing them in the Data Catalog.\nYou can set the decrypt permission to enable or restrict access on the password key according to your security requirements.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_resource_policy(PolicyInJson=None, PolicyHashCondition=None, PolicyExistsCondition=None):
    """
    Sets the Data Catalog resource policy for access control.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_resource_policy(
        PolicyInJson='string',
        PolicyHashCondition='string',
        PolicyExistsCondition='MUST_EXIST'|'NOT_EXIST'|'NONE'
    )
    
    
    :type PolicyInJson: string
    :param PolicyInJson: [REQUIRED]\nContains the policy document to set, in JSON format.\n

    :type PolicyHashCondition: string
    :param PolicyHashCondition: The hash value returned when the previous policy was set using PutResourcePolicy . Its purpose is to prevent concurrent modifications of a policy. Do not use this parameter if no previous policy has been set.

    :type PolicyExistsCondition: string
    :param PolicyExistsCondition: A value of MUST_EXIST is used to update a policy. A value of NOT_EXIST is used to create a new policy. If a value of NONE or a null value is used, the call will not depend on the existence of a policy.

    :rtype: dict

ReturnsResponse Syntax
{
    'PolicyHash': 'string'
}


Response Structure

(dict) --

PolicyHash (string) --
A hash of the policy that has just been set. This must be included in a subsequent call that overwrites or updates this policy.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.ConditionCheckFailureException


    :return: {
        'PolicyHash': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.ConditionCheckFailureException
    
    """
    pass

def put_workflow_run_properties(Name=None, RunId=None, RunProperties=None):
    """
    Puts the specified workflow run properties for the given workflow run. If a property already exists for the specified run, then it overrides the value otherwise adds the property to existing properties.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_workflow_run_properties(
        Name='string',
        RunId='string',
        RunProperties={
            'string': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the workflow which was run.\n

    :type RunId: string
    :param RunId: [REQUIRED]\nThe ID of the workflow run for which the run properties should be updated.\n

    :type RunProperties: dict
    :param RunProperties: [REQUIRED]\nThe properties to put for the specified run.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.AlreadyExistsException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def reset_job_bookmark(JobName=None, RunId=None):
    """
    Resets a bookmark entry.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reset_job_bookmark(
        JobName='string',
        RunId='string'
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]\nThe name of the job in question.\n

    :type RunId: string
    :param RunId: The unique run identifier associated with this job run.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobBookmarkEntry': {
        'JobName': 'string',
        'Version': 123,
        'Run': 123,
        'Attempt': 123,
        'PreviousRunId': 'string',
        'RunId': 'string',
        'JobBookmark': 'string'
    }
}


Response Structure

(dict) --

JobBookmarkEntry (dict) --
The reset bookmark entry.

JobName (string) --
The name of the job in question.

Version (integer) --
The version of the job.

Run (integer) --
The run ID number.

Attempt (integer) --
The attempt ID number.

PreviousRunId (string) --
The unique run identifier associated with the previous job run.

RunId (string) --
The run ID number.

JobBookmark (string) --
The bookmark itself.









Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'JobBookmarkEntry': {
            'JobName': 'string',
            'Version': 123,
            'Run': 123,
            'Attempt': 123,
            'PreviousRunId': 'string',
            'RunId': 'string',
            'JobBookmark': 'string'
        }
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def search_tables(CatalogId=None, NextToken=None, Filters=None, SearchText=None, SortCriteria=None, MaxResults=None):
    """
    Searches a set of tables based on properties in the table metadata as well as on the parent database. You can search against text or filter conditions.
    You can only get tables that you have access to based on the security policies defined in Lake Formation. You need at least a read-only access to the table for it to be returned. If you do not have access to all the columns in the table, these columns will not be searched against when returning the list of tables back to you. If you have access to the columns but not the data in the columns, those columns and the associated metadata for those columns will be included in the search.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.search_tables(
        CatalogId='string',
        NextToken='string',
        Filters=[
            {
                'Key': 'string',
                'Value': 'string',
                'Comparator': 'EQUALS'|'GREATER_THAN'|'LESS_THAN'|'GREATER_THAN_EQUALS'|'LESS_THAN_EQUALS'
            },
        ],
        SearchText='string',
        SortCriteria=[
            {
                'FieldName': 'string',
                'Sort': 'ASC'|'DESC'
            },
        ],
        MaxResults=123
    )
    
    
    :type CatalogId: string
    :param CatalogId: A unique identifier, consisting of `` account_id /datalake`` .

    :type NextToken: string
    :param NextToken: A continuation token, included if this is a continuation call.

    :type Filters: list
    :param Filters: A list of key-value pairs, and a comparator used to filter the search results. Returns all entities matching the predicate.\n\n(dict) --Defines a property predicate.\n\nKey (string) --The key of the property.\n\nValue (string) --The value of the property.\n\nComparator (string) --The comparator used to compare this property to others.\n\n\n\n\n

    :type SearchText: string
    :param SearchText: A string used for a text search.\nSpecifying a value in quotes filters based on an exact match to the value.\n

    :type SortCriteria: list
    :param SortCriteria: A list of criteria for sorting the results by a field name, in an ascending or descending order.\n\n(dict) --Specifies a field to sort by and a sort order.\n\nFieldName (string) --The name of the field on which to sort.\n\nSort (string) --An ascending or descending sort.\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of tables to return in a single response.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'TableList': [
        {
            'Name': 'string',
            'DatabaseName': 'string',
            'Description': 'string',
            'Owner': 'string',
            'CreateTime': datetime(2015, 1, 1),
            'UpdateTime': datetime(2015, 1, 1),
            'LastAccessTime': datetime(2015, 1, 1),
            'LastAnalyzedTime': datetime(2015, 1, 1),
            'Retention': 123,
            'StorageDescriptor': {
                'Columns': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'Location': 'string',
                'InputFormat': 'string',
                'OutputFormat': 'string',
                'Compressed': True|False,
                'NumberOfBuckets': 123,
                'SerdeInfo': {
                    'Name': 'string',
                    'SerializationLibrary': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
                'BucketColumns': [
                    'string',
                ],
                'SortColumns': [
                    {
                        'Column': 'string',
                        'SortOrder': 123
                    },
                ],
                'Parameters': {
                    'string': 'string'
                },
                'SkewedInfo': {
                    'SkewedColumnNames': [
                        'string',
                    ],
                    'SkewedColumnValues': [
                        'string',
                    ],
                    'SkewedColumnValueLocationMaps': {
                        'string': 'string'
                    }
                },
                'StoredAsSubDirectories': True|False
            },
            'PartitionKeys': [
                {
                    'Name': 'string',
                    'Type': 'string',
                    'Comment': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
            ],
            'ViewOriginalText': 'string',
            'ViewExpandedText': 'string',
            'TableType': 'string',
            'Parameters': {
                'string': 'string'
            },
            'CreatedBy': 'string',
            'IsRegisteredWithLakeFormation': True|False
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
A continuation token, present if the current list segment is not the last.

TableList (list) --
A list of the requested Table objects. The SearchTables response returns only the tables that you have access to.

(dict) --
Represents a collection of related data organized in columns and rows.

Name (string) --
The table name. For Hive compatibility, this must be entirely lowercase.

DatabaseName (string) --
The name of the database where the table metadata resides. For Hive compatibility, this must be all lowercase.

Description (string) --
A description of the table.

Owner (string) --
The owner of the table.

CreateTime (datetime) --
The time when the table definition was created in the Data Catalog.

UpdateTime (datetime) --
The last time that the table was updated.

LastAccessTime (datetime) --
The last time that the table was accessed. This is usually taken from HDFS, and might not be reliable.

LastAnalyzedTime (datetime) --
The last time that column statistics were computed for this table.

Retention (integer) --
The retention time for this table.

StorageDescriptor (dict) --
A storage descriptor containing information about the physical storage of this table.

Columns (list) --
A list of the Columns in the table.

(dict) --
A column in a Table .

Name (string) --
The name of the Column .

Type (string) --
The data type of the Column .

Comment (string) --
A free-form text comment.

Parameters (dict) --
These key-value pairs define properties associated with the column.

(string) --
(string) --








Location (string) --
The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

InputFormat (string) --
The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.

OutputFormat (string) --
The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.

Compressed (boolean) --

True if the data in the table is compressed, or False if not.


NumberOfBuckets (integer) --
Must be specified if the table contains any dimension columns.

SerdeInfo (dict) --
The serialization/deserialization (SerDe) information.

Name (string) --
Name of the SerDe.

SerializationLibrary (string) --
Usually the class that implements the SerDe. An example is org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .

Parameters (dict) --
These key-value pairs define initialization parameters for the SerDe.

(string) --
(string) --






BucketColumns (list) --
A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

(string) --


SortColumns (list) --
A list specifying the sort order of each bucket in the table.

(dict) --
Specifies the sort order of a sorted column.

Column (string) --
The name of the column.

SortOrder (integer) --
Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).





Parameters (dict) --
The user-supplied properties in key-value form.

(string) --
(string) --




SkewedInfo (dict) --
The information about values that appear frequently in a column (skewed values).

SkewedColumnNames (list) --
A list of names of columns that contain skewed values.

(string) --


SkewedColumnValues (list) --
A list of values that appear so frequently as to be considered skewed.

(string) --


SkewedColumnValueLocationMaps (dict) --
A mapping of skewed values to the columns that contain them.

(string) --
(string) --






StoredAsSubDirectories (boolean) --

True if the table data is stored in subdirectories, or False if not.




PartitionKeys (list) --
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
When you create a table used by Amazon Athena, and you do not specify any partitionKeys , you must at least set the value of partitionKeys to an empty list. For example:

"PartitionKeys": []


(dict) --
A column in a Table .

Name (string) --
The name of the Column .

Type (string) --
The data type of the Column .

Comment (string) --
A free-form text comment.

Parameters (dict) --
These key-value pairs define properties associated with the column.

(string) --
(string) --








ViewOriginalText (string) --
If the table is a view, the original text of the view; otherwise null .

ViewExpandedText (string) --
If the table is a view, the expanded text of the view; otherwise null .

TableType (string) --
The type of this table (EXTERNAL_TABLE , VIRTUAL_VIEW , etc.).

Parameters (dict) --
These key-value pairs define properties associated with the table.

(string) --
(string) --




CreatedBy (string) --
The person or entity who created the table.

IsRegisteredWithLakeFormation (boolean) --
Indicates whether the table has been registered with AWS Lake Formation.











Exceptions

Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException


    :return: {
        'NextToken': 'string',
        'TableList': [
            {
                'Name': 'string',
                'DatabaseName': 'string',
                'Description': 'string',
                'Owner': 'string',
                'CreateTime': datetime(2015, 1, 1),
                'UpdateTime': datetime(2015, 1, 1),
                'LastAccessTime': datetime(2015, 1, 1),
                'LastAnalyzedTime': datetime(2015, 1, 1),
                'Retention': 123,
                'StorageDescriptor': {
                    'Columns': [
                        {
                            'Name': 'string',
                            'Type': 'string',
                            'Comment': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                    ],
                    'Location': 'string',
                    'InputFormat': 'string',
                    'OutputFormat': 'string',
                    'Compressed': True|False,
                    'NumberOfBuckets': 123,
                    'SerdeInfo': {
                        'Name': 'string',
                        'SerializationLibrary': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                    'BucketColumns': [
                        'string',
                    ],
                    'SortColumns': [
                        {
                            'Column': 'string',
                            'SortOrder': 123
                        },
                    ],
                    'Parameters': {
                        'string': 'string'
                    },
                    'SkewedInfo': {
                        'SkewedColumnNames': [
                            'string',
                        ],
                        'SkewedColumnValues': [
                            'string',
                        ],
                        'SkewedColumnValueLocationMaps': {
                            'string': 'string'
                        }
                    },
                    'StoredAsSubDirectories': True|False
                },
                'PartitionKeys': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'ViewOriginalText': 'string',
                'ViewExpandedText': 'string',
                'TableType': 'string',
                'Parameters': {
                    'string': 'string'
                },
                'CreatedBy': 'string',
                'IsRegisteredWithLakeFormation': True|False
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def start_crawler(Name=None):
    """
    Starts a crawl using the specified crawler, regardless of what is scheduled. If the crawler is already running, returns a CrawlerRunningException .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_crawler(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the crawler to start.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.CrawlerRunningException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.CrawlerRunningException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def start_crawler_schedule(CrawlerName=None):
    """
    Changes the schedule state of the specified crawler to SCHEDULED , unless the crawler is already running or the schedule state is already SCHEDULED .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_crawler_schedule(
        CrawlerName='string'
    )
    
    
    :type CrawlerName: string
    :param CrawlerName: [REQUIRED]\nName of the crawler to schedule.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.SchedulerRunningException
Glue.Client.exceptions.SchedulerTransitioningException
Glue.Client.exceptions.NoScheduleException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.SchedulerRunningException
    Glue.Client.exceptions.SchedulerTransitioningException
    Glue.Client.exceptions.NoScheduleException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def start_export_labels_task_run(TransformId=None, OutputS3Path=None):
    """
    Begins an asynchronous task to export all labeled data for a particular transform. This task is the only label-related API call that is not part of the typical active learning workflow. You typically use StartExportLabelsTaskRun when you want to work with all of your existing labels at the same time, such as when you want to remove or change labels that were previously submitted as truth. This API operation accepts the TransformId whose labels you want to export and an Amazon Simple Storage Service (Amazon S3) path to export the labels to. The operation returns a TaskRunId . You can check on the status of your task run by calling the GetMLTaskRun API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_export_labels_task_run(
        TransformId='string',
        OutputS3Path='string'
    )
    
    
    :type TransformId: string
    :param TransformId: [REQUIRED]\nThe unique identifier of the machine learning transform.\n

    :type OutputS3Path: string
    :param OutputS3Path: [REQUIRED]\nThe Amazon S3 path where you export the labels.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TaskRunId': 'string'
}


Response Structure

(dict) --

TaskRunId (string) --
The unique identifier for the task run.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException


    :return: {
        'TaskRunId': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.InternalServiceException
    
    """
    pass

def start_import_labels_task_run(TransformId=None, InputS3Path=None, ReplaceAllLabels=None):
    """
    Enables you to provide additional labels (examples of truth) to be used to teach the machine learning transform and improve its quality. This API operation is generally used as part of the active learning workflow that starts with the StartMLLabelingSetGenerationTaskRun call and that ultimately results in improving the quality of your machine learning transform.
    After the StartMLLabelingSetGenerationTaskRun finishes, AWS Glue machine learning will have generated a series of questions for humans to answer. (Answering these questions is often called \'labeling\' in the machine learning workflows). In the case of the FindMatches transform, these questions are of the form, \xe2\x80\x9cWhat is the correct way to group these rows together into groups composed entirely of matching records?\xe2\x80\x9d After the labeling process is finished, users upload their answers/labels with a call to StartImportLabelsTaskRun . After StartImportLabelsTaskRun finishes, all future runs of the machine learning transform use the new and improved labels and perform a higher-quality transformation.
    By default, StartMLLabelingSetGenerationTaskRun continually learns from and combines all labels that you upload unless you set Replace to true. If you set Replace to true, StartImportLabelsTaskRun deletes and forgets all previously uploaded labels and learns only from the exact set that you upload. Replacing labels can be helpful if you realize that you previously uploaded incorrect labels, and you believe that they are having a negative effect on your transform quality.
    You can check on the status of your task run by calling the GetMLTaskRun operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_import_labels_task_run(
        TransformId='string',
        InputS3Path='string',
        ReplaceAllLabels=True|False
    )
    
    
    :type TransformId: string
    :param TransformId: [REQUIRED]\nThe unique identifier of the machine learning transform.\n

    :type InputS3Path: string
    :param InputS3Path: [REQUIRED]\nThe Amazon Simple Storage Service (Amazon S3) path from where you import the labels.\n

    :type ReplaceAllLabels: boolean
    :param ReplaceAllLabels: Indicates whether to overwrite your existing labels.

    :rtype: dict

ReturnsResponse Syntax
{
    'TaskRunId': 'string'
}


Response Structure

(dict) --

TaskRunId (string) --
The unique identifier for the task run.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.InternalServiceException


    :return: {
        'TaskRunId': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.ResourceNumberLimitExceededException
    Glue.Client.exceptions.InternalServiceException
    
    """
    pass

def start_job_run(JobName=None, JobRunId=None, Arguments=None, AllocatedCapacity=None, Timeout=None, MaxCapacity=None, SecurityConfiguration=None, NotificationProperty=None, WorkerType=None, NumberOfWorkers=None):
    """
    Starts a job run using a job definition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_job_run(
        JobName='string',
        JobRunId='string',
        Arguments={
            'string': 'string'
        },
        AllocatedCapacity=123,
        Timeout=123,
        MaxCapacity=123.0,
        SecurityConfiguration='string',
        NotificationProperty={
            'NotifyDelayAfter': 123
        },
        WorkerType='Standard'|'G.1X'|'G.2X',
        NumberOfWorkers=123
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]\nThe name of the job definition to use.\n

    :type JobRunId: string
    :param JobRunId: The ID of a previous JobRun to retry.

    :type Arguments: dict
    :param Arguments: The job arguments specifically for this run. For this job run, they replace the default arguments set in the job definition itself.\nYou can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.\nFor information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.\nFor information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.\n\n(string) --\n(string) --\n\n\n\n

    :type AllocatedCapacity: integer
    :param AllocatedCapacity: This field is deprecated. Use MaxCapacity instead.\nThe number of AWS Glue data processing units (DPUs) to allocate to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .\n

    :type Timeout: integer
    :param Timeout: The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

    :type MaxCapacity: float
    :param MaxCapacity: The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .\nDo not set Max Capacity if using WorkerType and NumberOfWorkers .\nThe value that can be allocated for MaxCapacity depends on whether you are running a Python shell job, or an Apache Spark ETL job:\n\nWhen you specify a Python shell job (JobCommand.Name ='pythonshell'), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.\nWhen you specify an Apache Spark ETL job (JobCommand.Name ='glueetl'), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.\n\n

    :type SecurityConfiguration: string
    :param SecurityConfiguration: The name of the SecurityConfiguration structure to be used with this job run.

    :type NotificationProperty: dict
    :param NotificationProperty: Specifies configuration properties of a job run notification.\n\nNotifyDelayAfter (integer) --After a job run starts, the number of minutes to wait before sending a job run delay notification.\n\n\n

    :type WorkerType: string
    :param WorkerType: The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.\n\nFor the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.\nFor the G.1X worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.\nFor the G.2X worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.\n\n

    :type NumberOfWorkers: integer
    :param NumberOfWorkers: The number of workers of a defined workerType that are allocated when a job runs.\nThe maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobRunId': 'string'
}


Response Structure

(dict) --

JobRunId (string) --
The ID assigned to this job run.







Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.ConcurrentRunsExceededException


    :return: {
        'JobRunId': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.ResourceNumberLimitExceededException
    Glue.Client.exceptions.ConcurrentRunsExceededException
    
    """
    pass

def start_ml_evaluation_task_run(TransformId=None):
    """
    Starts a task to estimate the quality of the transform.
    When you provide label sets as examples of truth, AWS Glue machine learning uses some of those examples to learn from them. The rest of the labels are used as a test to estimate quality.
    Returns a unique identifier for the run. You can call GetMLTaskRun to get more information about the stats of the EvaluationTaskRun .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_ml_evaluation_task_run(
        TransformId='string'
    )
    
    
    :type TransformId: string
    :param TransformId: [REQUIRED]\nThe unique identifier of the machine learning transform.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TaskRunId': 'string'
}


Response Structure

(dict) --
TaskRunId (string) --The unique identifier associated with this run.






Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.ConcurrentRunsExceededException
Glue.Client.exceptions.MLTransformNotReadyException


    :return: {
        'TaskRunId': 'string'
    }
    
    
    """
    pass

def start_ml_labeling_set_generation_task_run(TransformId=None, OutputS3Path=None):
    """
    Starts the active learning workflow for your machine learning transform to improve the transform\'s quality by generating label sets and adding labels.
    When the StartMLLabelingSetGenerationTaskRun finishes, AWS Glue will have generated a "labeling set" or a set of questions for humans to answer.
    In the case of the FindMatches transform, these questions are of the form, \xe2\x80\x9cWhat is the correct way to group these rows together into groups composed entirely of matching records?\xe2\x80\x9d
    After the labeling process is finished, you can upload your labels with a call to StartImportLabelsTaskRun . After StartImportLabelsTaskRun finishes, all future runs of the machine learning transform will use the new and improved labels and perform a higher-quality transformation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_ml_labeling_set_generation_task_run(
        TransformId='string',
        OutputS3Path='string'
    )
    
    
    :type TransformId: string
    :param TransformId: [REQUIRED]\nThe unique identifier of the machine learning transform.\n

    :type OutputS3Path: string
    :param OutputS3Path: [REQUIRED]\nThe Amazon Simple Storage Service (Amazon S3) path where you generate the labeling set.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TaskRunId': 'string'
}


Response Structure

(dict) --

TaskRunId (string) --
The unique run identifier that is associated with this task run.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.ConcurrentRunsExceededException


    :return: {
        'TaskRunId': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.ConcurrentRunsExceededException
    
    """
    pass

def start_trigger(Name=None):
    """
    Starts an existing trigger. See Triggering Jobs for information about how different types of trigger are started.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_trigger(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the trigger to start.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Name': 'string'
}


Response Structure

(dict) --
Name (string) --The name of the trigger that was started.






Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.ConcurrentRunsExceededException


    :return: {
        'Name': 'string'
    }
    
    
    """
    pass

def start_workflow_run(Name=None):
    """
    Starts a new run of the specified workflow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_workflow_run(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the workflow to start.\n

    :rtype: dict
ReturnsResponse Syntax{
    'RunId': 'string'
}


Response Structure

(dict) --
RunId (string) --An Id for the new run.






Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.ConcurrentRunsExceededException


    :return: {
        'RunId': 'string'
    }
    
    
    """
    pass

def stop_crawler(Name=None):
    """
    If the specified crawler is running, stops the crawl.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_crawler(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the crawler to stop.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.CrawlerNotRunningException
Glue.Client.exceptions.CrawlerStoppingException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.CrawlerNotRunningException
    Glue.Client.exceptions.CrawlerStoppingException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def stop_crawler_schedule(CrawlerName=None):
    """
    Sets the schedule state of the specified crawler to NOT_SCHEDULED , but does not stop the crawler if it is already running.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_crawler_schedule(
        CrawlerName='string'
    )
    
    
    :type CrawlerName: string
    :param CrawlerName: [REQUIRED]\nName of the crawler whose schedule state to set.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.SchedulerNotRunningException
Glue.Client.exceptions.SchedulerTransitioningException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.SchedulerNotRunningException
    Glue.Client.exceptions.SchedulerTransitioningException
    Glue.Client.exceptions.OperationTimeoutException
    
    """
    pass

def stop_trigger(Name=None):
    """
    Stops a specified trigger.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_trigger(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the trigger to stop.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Name': 'string'
}


Response Structure

(dict) --
Name (string) --The name of the trigger that was stopped.






Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ConcurrentModificationException


    :return: {
        'Name': 'string'
    }
    
    
    """
    pass

def stop_workflow_run(Name=None, RunId=None):
    """
    Stops the execution of the specified workflow run.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_workflow_run(
        Name='string',
        RunId='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the workflow to stop.\n

    :type RunId: string
    :param RunId: [REQUIRED]\nThe ID of the workflow run to stop.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.IllegalWorkflowStateException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def tag_resource(ResourceArn=None, TagsToAdd=None):
    """
    Adds tags to a resource. A tag is a label you can assign to an AWS resource. In AWS Glue, you can tag only certain resources. For information about what resources you can tag, see AWS Tags in AWS Glue .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        TagsToAdd={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the AWS Glue resource to which to add the tags. For more information about AWS Glue resource ARNs, see the AWS Glue ARN string pattern .\n

    :type TagsToAdd: dict
    :param TagsToAdd: [REQUIRED]\nTags to add to this resource.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.EntityNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagsToRemove=None):
    """
    Removes tags from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagsToRemove=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource from which to remove the tags.\n

    :type TagsToRemove: list
    :param TagsToRemove: [REQUIRED]\nTags to remove from this resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.EntityNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_classifier(GrokClassifier=None, XMLClassifier=None, JsonClassifier=None, CsvClassifier=None):
    """
    Modifies an existing classifier (a GrokClassifier , an XMLClassifier , a JsonClassifier , or a CsvClassifier , depending on which field is present).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_classifier(
        GrokClassifier={
            'Name': 'string',
            'Classification': 'string',
            'GrokPattern': 'string',
            'CustomPatterns': 'string'
        },
        XMLClassifier={
            'Name': 'string',
            'Classification': 'string',
            'RowTag': 'string'
        },
        JsonClassifier={
            'Name': 'string',
            'JsonPath': 'string'
        },
        CsvClassifier={
            'Name': 'string',
            'Delimiter': 'string',
            'QuoteSymbol': 'string',
            'ContainsHeader': 'UNKNOWN'|'PRESENT'|'ABSENT',
            'Header': [
                'string',
            ],
            'DisableValueTrimming': True|False,
            'AllowSingleColumn': True|False
        }
    )
    
    
    :type GrokClassifier: dict
    :param GrokClassifier: A GrokClassifier object with updated fields.\n\nName (string) -- [REQUIRED]The name of the GrokClassifier .\n\nClassification (string) --An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.\n\nGrokPattern (string) --The grok pattern used by this classifier.\n\nCustomPatterns (string) --Optional custom grok patterns used by this classifier.\n\n\n

    :type XMLClassifier: dict
    :param XMLClassifier: An XMLClassifier object with updated fields.\n\nName (string) -- [REQUIRED]The name of the classifier.\n\nClassification (string) --An identifier of the data format that the classifier matches.\n\nRowTag (string) --The XML tag designating the element that contains each record in an XML document being parsed. This cannot identify a self-closing element (closed by /> ). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, <row item_a='A' item_b='B'></row> is okay, but <row item_a='A' item_b='B' /> is not).\n\n\n

    :type JsonClassifier: dict
    :param JsonClassifier: A JsonClassifier object with updated fields.\n\nName (string) -- [REQUIRED]The name of the classifier.\n\nJsonPath (string) --A JsonPath string defining the JSON data for the classifier to classify. AWS Glue supports a subset of JsonPath , as described in Writing JsonPath Custom Classifiers .\n\n\n

    :type CsvClassifier: dict
    :param CsvClassifier: A CsvClassifier object with updated fields.\n\nName (string) -- [REQUIRED]The name of the classifier.\n\nDelimiter (string) --A custom symbol to denote what separates each column entry in the row.\n\nQuoteSymbol (string) --A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.\n\nContainsHeader (string) --Indicates whether the CSV file contains a header.\n\nHeader (list) --A list of strings representing column names.\n\n(string) --\n\n\nDisableValueTrimming (boolean) --Specifies not to trim values before identifying the type of column values. The default value is true.\n\nAllowSingleColumn (boolean) --Enables the processing of files that contain only one column.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.VersionMismatchException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_connection(CatalogId=None, Name=None, ConnectionInput=None):
    """
    Updates a connection definition in the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_connection(
        CatalogId='string',
        Name='string',
        ConnectionInput={
            'Name': 'string',
            'Description': 'string',
            'ConnectionType': 'JDBC'|'SFTP'|'MONGODB'|'KAFKA',
            'MatchCriteria': [
                'string',
            ],
            'ConnectionProperties': {
                'string': 'string'
            },
            'PhysicalConnectionRequirements': {
                'SubnetId': 'string',
                'SecurityGroupIdList': [
                    'string',
                ],
                'AvailabilityZone': 'string'
            }
        }
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the connection resides. If none is provided, the AWS account ID is used by default.

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the connection definition to update.\n

    :type ConnectionInput: dict
    :param ConnectionInput: [REQUIRED]\nA ConnectionInput object that redefines the connection in question.\n\nName (string) -- [REQUIRED]The name of the connection.\n\nDescription (string) --The description of the connection.\n\nConnectionType (string) -- [REQUIRED]The type of the connection. Currently, these types are supported:\n\nJDBC - Designates a connection to a database through Java Database Connectivity (JDBC).\nKAFKA - Designates a connection to an Apache Kafka streaming platform.\nMONGODB - Designates a connection to a MongoDB document database.\n\nSFTP is not supported.\n\nMatchCriteria (list) --A list of criteria that can be used in selecting this connection.\n\n(string) --\n\n\nConnectionProperties (dict) -- [REQUIRED]These key-value pairs define parameters for the connection.\n\n(string) --\n(string) --\n\n\n\n\nPhysicalConnectionRequirements (dict) --A map of physical connection requirements, such as virtual private cloud (VPC) and SecurityGroup , that are needed to successfully make this connection.\n\nSubnetId (string) --The subnet ID used by the connection.\n\nSecurityGroupIdList (list) --The security group ID list used by the connection.\n\n(string) --\n\n\nAvailabilityZone (string) --The connection\'s Availability Zone. This field is redundant because the specified subnet implies the Availability Zone to be used. Currently the field must be populated, but it will be deprecated in the future.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.GlueEncryptionException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_crawler(Name=None, Role=None, DatabaseName=None, Description=None, Targets=None, Schedule=None, Classifiers=None, TablePrefix=None, SchemaChangePolicy=None, Configuration=None, CrawlerSecurityConfiguration=None):
    """
    Updates a crawler. If a crawler is running, you must stop it using StopCrawler before updating it.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_crawler(
        Name='string',
        Role='string',
        DatabaseName='string',
        Description='string',
        Targets={
            'S3Targets': [
                {
                    'Path': 'string',
                    'Exclusions': [
                        'string',
                    ]
                },
            ],
            'JdbcTargets': [
                {
                    'ConnectionName': 'string',
                    'Path': 'string',
                    'Exclusions': [
                        'string',
                    ]
                },
            ],
            'DynamoDBTargets': [
                {
                    'Path': 'string'
                },
            ],
            'CatalogTargets': [
                {
                    'DatabaseName': 'string',
                    'Tables': [
                        'string',
                    ]
                },
            ]
        },
        Schedule='string',
        Classifiers=[
            'string',
        ],
        TablePrefix='string',
        SchemaChangePolicy={
            'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
            'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
        },
        Configuration='string',
        CrawlerSecurityConfiguration='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the new crawler.\n

    :type Role: string
    :param Role: The IAM role or Amazon Resource Name (ARN) of an IAM role that is used by the new crawler to access customer resources.

    :type DatabaseName: string
    :param DatabaseName: The AWS Glue database where results are stored, such as: arn:aws:daylight:us-east-1::database/sometable/* .

    :type Description: string
    :param Description: A description of the new crawler.

    :type Targets: dict
    :param Targets: A list of targets to crawl.\n\nS3Targets (list) --Specifies Amazon Simple Storage Service (Amazon S3) targets.\n\n(dict) --Specifies a data store in Amazon Simple Storage Service (Amazon S3).\n\nPath (string) --The path to the Amazon S3 target.\n\nExclusions (list) --A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler .\n\n(string) --\n\n\n\n\n\n\nJdbcTargets (list) --Specifies JDBC targets.\n\n(dict) --Specifies a JDBC data store to crawl.\n\nConnectionName (string) --The name of the connection to use to connect to the JDBC target.\n\nPath (string) --The path of the JDBC target.\n\nExclusions (list) --A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler .\n\n(string) --\n\n\n\n\n\n\nDynamoDBTargets (list) --Specifies Amazon DynamoDB targets.\n\n(dict) --Specifies an Amazon DynamoDB table to crawl.\n\nPath (string) --The name of the DynamoDB table to crawl.\n\n\n\n\n\nCatalogTargets (list) --Specifies AWS Glue Data Catalog targets.\n\n(dict) --Specifies an AWS Glue Data Catalog target.\n\nDatabaseName (string) -- [REQUIRED]The name of the database to be synchronized.\n\nTables (list) -- [REQUIRED]A list of the tables to be synchronized.\n\n(string) --\n\n\n\n\n\n\n\n

    :type Schedule: string
    :param Schedule: A cron expression used to specify the schedule. For more information, see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, specify cron(15 12 * * ? *) .

    :type Classifiers: list
    :param Classifiers: A list of custom classifiers that the user has registered. By default, all built-in classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.\n\n(string) --\n\n

    :type TablePrefix: string
    :param TablePrefix: The table prefix used for catalog tables that are created.

    :type SchemaChangePolicy: dict
    :param SchemaChangePolicy: The policy for the crawler\'s update and deletion behavior.\n\nUpdateBehavior (string) --The update behavior when the crawler finds a changed schema.\n\nDeleteBehavior (string) --The deletion behavior when the crawler finds a deleted object.\n\n\n

    :type Configuration: string
    :param Configuration: The crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler\'s behavior. For more information, see Configuring a Crawler .

    :type CrawlerSecurityConfiguration: string
    :param CrawlerSecurityConfiguration: The name of the SecurityConfiguration structure to be used by this crawler.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.VersionMismatchException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.CrawlerRunningException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_crawler_schedule(CrawlerName=None, Schedule=None):
    """
    Updates the schedule of a crawler using a cron expression.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_crawler_schedule(
        CrawlerName='string',
        Schedule='string'
    )
    
    
    :type CrawlerName: string
    :param CrawlerName: [REQUIRED]\nThe name of the crawler whose schedule to update.\n

    :type Schedule: string
    :param Schedule: The updated cron expression used to specify the schedule. For more information, see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, specify cron(15 12 * * ? *) .

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.VersionMismatchException
Glue.Client.exceptions.SchedulerTransitioningException
Glue.Client.exceptions.OperationTimeoutException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_database(CatalogId=None, Name=None, DatabaseInput=None):
    """
    Updates an existing database definition in a Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_database(
        CatalogId='string',
        Name='string',
        DatabaseInput={
            'Name': 'string',
            'Description': 'string',
            'LocationUri': 'string',
            'Parameters': {
                'string': 'string'
            },
            'CreateTableDefaultPermissions': [
                {
                    'Principal': {
                        'DataLakePrincipalIdentifier': 'string'
                    },
                    'Permissions': [
                        'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                    ]
                },
            ]
        }
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the metadata database resides. If none is provided, the AWS account ID is used by default.

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the database to update in the catalog. For Hive compatibility, this is folded to lowercase.\n

    :type DatabaseInput: dict
    :param DatabaseInput: [REQUIRED]\nA DatabaseInput object specifying the new definition of the metadata database in the catalog.\n\nName (string) -- [REQUIRED]The name of the database. For Hive compatibility, this is folded to lowercase when it is stored.\n\nDescription (string) --A description of the database.\n\nLocationUri (string) --The location of the database (for example, an HDFS path).\n\nParameters (dict) --These key-value pairs define parameters and properties of the database.\nThese key-value pairs define parameters and properties of the database.\n\n(string) --\n(string) --\n\n\n\n\nCreateTableDefaultPermissions (list) --Creates a set of default permissions on the table for principals.\n\n(dict) --Permissions granted to a principal.\n\nPrincipal (dict) --The principal who is granted permissions.\n\nDataLakePrincipalIdentifier (string) --An identifier for the AWS Lake Formation principal.\n\n\n\nPermissions (list) --The permissions that are granted to the principal.\n\n(string) --\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.GlueEncryptionException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_dev_endpoint(EndpointName=None, PublicKey=None, AddPublicKeys=None, DeletePublicKeys=None, CustomLibraries=None, UpdateEtlLibraries=None, DeleteArguments=None, AddArguments=None):
    """
    Updates a specified development endpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_dev_endpoint(
        EndpointName='string',
        PublicKey='string',
        AddPublicKeys=[
            'string',
        ],
        DeletePublicKeys=[
            'string',
        ],
        CustomLibraries={
            'ExtraPythonLibsS3Path': 'string',
            'ExtraJarsS3Path': 'string'
        },
        UpdateEtlLibraries=True|False,
        DeleteArguments=[
            'string',
        ],
        AddArguments={
            'string': 'string'
        }
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]\nThe name of the DevEndpoint to be updated.\n

    :type PublicKey: string
    :param PublicKey: The public key for the DevEndpoint to use.

    :type AddPublicKeys: list
    :param AddPublicKeys: The list of public keys for the DevEndpoint to use.\n\n(string) --\n\n

    :type DeletePublicKeys: list
    :param DeletePublicKeys: The list of public keys to be deleted from the DevEndpoint .\n\n(string) --\n\n

    :type CustomLibraries: dict
    :param CustomLibraries: Custom Python or Java libraries to be loaded in the DevEndpoint .\n\nExtraPythonLibsS3Path (string) --The paths to one or more Python libraries in an Amazon Simple Storage Service (Amazon S3) bucket that should be loaded in your DevEndpoint . Multiple values must be complete paths separated by a comma.\n\nNote\nYou can only use pure Python libraries with a DevEndpoint . Libraries that rely on C extensions, such as the pandas Python data analysis library, are not currently supported.\n\n\nExtraJarsS3Path (string) --The path to one or more Java .jar files in an S3 bucket that should be loaded in your DevEndpoint .\n\nNote\nYou can only use pure Java/Scala libraries with a DevEndpoint .\n\n\n\n

    :type UpdateEtlLibraries: boolean
    :param UpdateEtlLibraries: True if the list of custom libraries to be loaded in the development endpoint needs to be updated, or False if otherwise.

    :type DeleteArguments: list
    :param DeleteArguments: The list of argument keys to be deleted from the map of arguments used to configure the DevEndpoint .\n\n(string) --\n\n

    :type AddArguments: dict
    :param AddArguments: The map of arguments to add the map of arguments used to configure the DevEndpoint .\nValid arguments are:\n\n'--enable-glue-datacatalog': ''\n'GLUE_PYTHON_VERSION': '3'\n'GLUE_PYTHON_VERSION': '2'\n\nYou can specify a version of Python support for development endpoints by using the Arguments parameter in the CreateDevEndpoint or UpdateDevEndpoint APIs. If no arguments are provided, the version defaults to Python 2.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.ValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_job(JobName=None, JobUpdate=None):
    """
    Updates an existing job definition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_job(
        JobName='string',
        JobUpdate={
            'Description': 'string',
            'LogUri': 'string',
            'Role': 'string',
            'ExecutionProperty': {
                'MaxConcurrentRuns': 123
            },
            'Command': {
                'Name': 'string',
                'ScriptLocation': 'string',
                'PythonVersion': 'string'
            },
            'DefaultArguments': {
                'string': 'string'
            },
            'NonOverridableArguments': {
                'string': 'string'
            },
            'Connections': {
                'Connections': [
                    'string',
                ]
            },
            'MaxRetries': 123,
            'AllocatedCapacity': 123,
            'Timeout': 123,
            'MaxCapacity': 123.0,
            'WorkerType': 'Standard'|'G.1X'|'G.2X',
            'NumberOfWorkers': 123,
            'SecurityConfiguration': 'string',
            'NotificationProperty': {
                'NotifyDelayAfter': 123
            },
            'GlueVersion': 'string'
        }
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]\nThe name of the job definition to update.\n

    :type JobUpdate: dict
    :param JobUpdate: [REQUIRED]\nSpecifies the values with which to update the job definition.\n\nDescription (string) --Description of the job being defined.\n\nLogUri (string) --This field is reserved for future use.\n\nRole (string) --The name or Amazon Resource Name (ARN) of the IAM role associated with this job (required).\n\nExecutionProperty (dict) --An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job.\n\nMaxConcurrentRuns (integer) --The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.\n\n\n\nCommand (dict) --The JobCommand that executes this job (required).\n\nName (string) --The name of the job command. For an Apache Spark ETL job, this must be glueetl . For a Python shell job, it must be pythonshell .\n\nScriptLocation (string) --Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that executes a job.\n\nPythonVersion (string) --The Python version being used to execute a Python shell job. Allowed values are 2 or 3.\n\n\n\nDefaultArguments (dict) --The default arguments for this job.\nYou can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.\nFor information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.\nFor information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.\n\n(string) --\n(string) --\n\n\n\n\nNonOverridableArguments (dict) --Non-overridable arguments for this job, specified as name-value pairs.\n\n(string) --\n(string) --\n\n\n\n\nConnections (dict) --The connections used for this job.\n\nConnections (list) --A list of connections used by the job.\n\n(string) --\n\n\n\n\nMaxRetries (integer) --The maximum number of times to retry this job if it fails.\n\nAllocatedCapacity (integer) --This field is deprecated. Use MaxCapacity instead.\nThe number of AWS Glue data processing units (DPUs) to allocate to this job. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .\n\nTimeout (integer) --The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours).\n\nMaxCapacity (float) --The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .\nDo not set Max Capacity if using WorkerType and NumberOfWorkers .\nThe value that can be allocated for MaxCapacity depends on whether you are running a Python shell job or an Apache Spark ETL job:\n\nWhen you specify a Python shell job (JobCommand.Name ='pythonshell'), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.\nWhen you specify an Apache Spark ETL job (JobCommand.Name ='glueetl'), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.\n\n\nWorkerType (string) --The type of predefined worker that is allocated when a job runs. Accepts a value of Standard, G.1X, or G.2X.\n\nFor the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.\nFor the G.1X worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.\nFor the G.2X worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.\n\n\nNumberOfWorkers (integer) --The number of workers of a defined workerType that are allocated when a job runs.\nThe maximum number of workers you can define are 299 for G.1X , and 149 for G.2X .\n\nSecurityConfiguration (string) --The name of the SecurityConfiguration structure to be used with this job.\n\nNotificationProperty (dict) --Specifies the configuration properties of a job notification.\n\nNotifyDelayAfter (integer) --After a job run starts, the number of minutes to wait before sending a job run delay notification.\n\n\n\nGlueVersion (string) --Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark.\nFor more information about the available AWS Glue versions and corresponding Spark and Python versions, see Glue version in the developer guide.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobName': 'string'
}


Response Structure

(dict) --

JobName (string) --
Returns the name of the updated job definition.







Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ConcurrentModificationException


    :return: {
        'JobName': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def update_ml_transform(TransformId=None, Name=None, Description=None, Parameters=None, Role=None, GlueVersion=None, MaxCapacity=None, WorkerType=None, NumberOfWorkers=None, Timeout=None, MaxRetries=None):
    """
    Updates an existing machine learning transform. Call this operation to tune the algorithm parameters to achieve better results.
    After calling this operation, you can call the StartMLEvaluationTaskRun operation to assess how well your new parameters achieved your goals (such as improving the quality of your machine learning transform, or making it more cost-effective).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_ml_transform(
        TransformId='string',
        Name='string',
        Description='string',
        Parameters={
            'TransformType': 'FIND_MATCHES',
            'FindMatchesParameters': {
                'PrimaryKeyColumnName': 'string',
                'PrecisionRecallTradeoff': 123.0,
                'AccuracyCostTradeoff': 123.0,
                'EnforceProvidedLabels': True|False
            }
        },
        Role='string',
        GlueVersion='string',
        MaxCapacity=123.0,
        WorkerType='Standard'|'G.1X'|'G.2X',
        NumberOfWorkers=123,
        Timeout=123,
        MaxRetries=123
    )
    
    
    :type TransformId: string
    :param TransformId: [REQUIRED]\nA unique identifier that was generated when the transform was created.\n

    :type Name: string
    :param Name: The unique name that you gave the transform when you created it.

    :type Description: string
    :param Description: A description of the transform. The default is an empty string.

    :type Parameters: dict
    :param Parameters: The configuration parameters that are specific to the transform type (algorithm) used. Conditionally dependent on the transform type.\n\nTransformType (string) -- [REQUIRED]The type of machine learning transform.\nFor information about the types of machine learning transforms, see Creating Machine Learning Transforms .\n\nFindMatchesParameters (dict) --The parameters for the find matches algorithm.\n\nPrimaryKeyColumnName (string) --The name of a column that uniquely identifies rows in the source table. Used to help identify matching records.\n\nPrecisionRecallTradeoff (float) --The value selected when tuning your transform for a balance between precision and recall. A value of 0.5 means no preference; a value of 1.0 means a bias purely for precision, and a value of 0.0 means a bias for recall. Because this is a tradeoff, choosing values close to 1.0 means very low recall, and choosing values close to 0.0 results in very low precision.\nThe precision metric indicates how often your model is correct when it predicts a match.\nThe recall metric indicates that for an actual match, how often your model predicts the match.\n\nAccuracyCostTradeoff (float) --The value that is selected when tuning your transform for a balance between accuracy and cost. A value of 0.5 means that the system balances accuracy and cost concerns. A value of 1.0 means a bias purely for accuracy, which typically results in a higher cost, sometimes substantially higher. A value of 0.0 means a bias purely for cost, which results in a less accurate FindMatches transform, sometimes with unacceptable accuracy.\nAccuracy measures how well the transform finds true positives and true negatives. Increasing accuracy requires more machine resources and cost. But it also results in increased recall.\nCost measures how many compute resources, and thus money, are consumed to run the transform.\n\nEnforceProvidedLabels (boolean) --The value to switch on or off to force the output to match the provided labels from users. If the value is True , the find matches transform forces the output to match the provided labels. The results override the normal conflation results. If the value is False , the find matches transform does not ensure all the labels provided are respected, and the results rely on the trained model.\nNote that setting this value to true may increase the conflation execution time.\n\n\n\n\n

    :type Role: string
    :param Role: The name or Amazon Resource Name (ARN) of the IAM role with the required permissions.

    :type GlueVersion: string
    :param GlueVersion: This value determines which version of AWS Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see AWS Glue Versions in the developer guide.

    :type MaxCapacity: float
    :param MaxCapacity: The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .\nWhen the WorkerType field is set to a value other than Standard , the MaxCapacity field is set automatically and becomes read-only.\n

    :type WorkerType: string
    :param WorkerType: The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.\n\nFor the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.\nFor the G.1X worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.\nFor the G.2X worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.\n\n

    :type NumberOfWorkers: integer
    :param NumberOfWorkers: The number of workers of a defined workerType that are allocated when this task runs.

    :type Timeout: integer
    :param Timeout: The timeout for a task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours).

    :type MaxRetries: integer
    :param MaxRetries: The maximum number of times to retry a task for this transform after a task run fails.

    :rtype: dict

ReturnsResponse Syntax
{
    'TransformId': 'string'
}


Response Structure

(dict) --

TransformId (string) --
The unique identifier for the transform that was updated.







Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.AccessDeniedException


    :return: {
        'TransformId': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.AccessDeniedException
    
    """
    pass

def update_partition(CatalogId=None, DatabaseName=None, TableName=None, PartitionValueList=None, PartitionInput=None):
    """
    Updates a partition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_partition(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        PartitionValueList=[
            'string',
        ],
        PartitionInput={
            'Values': [
                'string',
            ],
            'LastAccessTime': datetime(2015, 1, 1),
            'StorageDescriptor': {
                'Columns': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'Location': 'string',
                'InputFormat': 'string',
                'OutputFormat': 'string',
                'Compressed': True|False,
                'NumberOfBuckets': 123,
                'SerdeInfo': {
                    'Name': 'string',
                    'SerializationLibrary': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
                'BucketColumns': [
                    'string',
                ],
                'SortColumns': [
                    {
                        'Column': 'string',
                        'SortOrder': 123
                    },
                ],
                'Parameters': {
                    'string': 'string'
                },
                'SkewedInfo': {
                    'SkewedColumnNames': [
                        'string',
                    ],
                    'SkewedColumnValues': [
                        'string',
                    ],
                    'SkewedColumnValueLocationMaps': {
                        'string': 'string'
                    }
                },
                'StoredAsSubDirectories': True|False
            },
            'Parameters': {
                'string': 'string'
            },
            'LastAnalyzedTime': datetime(2015, 1, 1)
        }
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the partition to be updated resides. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the catalog database in which the table in question resides.\n

    :type TableName: string
    :param TableName: [REQUIRED]\nThe name of the table in which the partition to be updated is located.\n

    :type PartitionValueList: list
    :param PartitionValueList: [REQUIRED]\nA list of the values defining the partition.\n\n(string) --\n\n

    :type PartitionInput: dict
    :param PartitionInput: [REQUIRED]\nThe new partition object to update the partition to.\n\nValues (list) --The values of the partition. Although this parameter is not required by the SDK, you must specify this parameter for a valid input.\nThe values for the keys for the new partition must be passed as an array of String objects that must be ordered in the same order as the partition keys appearing in the Amazon S3 prefix. Otherwise AWS Glue will add the values to the wrong keys.\n\n(string) --\n\n\nLastAccessTime (datetime) --The last time at which the partition was accessed.\n\nStorageDescriptor (dict) --Provides information about the physical location where the partition is stored.\n\nColumns (list) --A list of the Columns in the table.\n\n(dict) --A column in a Table .\n\nName (string) -- [REQUIRED]The name of the Column .\n\nType (string) --The data type of the Column .\n\nComment (string) --A free-form text comment.\n\nParameters (dict) --These key-value pairs define properties associated with the column.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\nLocation (string) --The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.\n\nInputFormat (string) --The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.\n\nOutputFormat (string) --The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.\n\nCompressed (boolean) --\nTrue if the data in the table is compressed, or False if not.\n\nNumberOfBuckets (integer) --Must be specified if the table contains any dimension columns.\n\nSerdeInfo (dict) --The serialization/deserialization (SerDe) information.\n\nName (string) --Name of the SerDe.\n\nSerializationLibrary (string) --Usually the class that implements the SerDe. An example is org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .\n\nParameters (dict) --These key-value pairs define initialization parameters for the SerDe.\n\n(string) --\n(string) --\n\n\n\n\n\n\nBucketColumns (list) --A list of reducer grouping columns, clustering columns, and bucketing columns in the table.\n\n(string) --\n\n\nSortColumns (list) --A list specifying the sort order of each bucket in the table.\n\n(dict) --Specifies the sort order of a sorted column.\n\nColumn (string) -- [REQUIRED]The name of the column.\n\nSortOrder (integer) -- [REQUIRED]Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).\n\n\n\n\n\nParameters (dict) --The user-supplied properties in key-value form.\n\n(string) --\n(string) --\n\n\n\n\nSkewedInfo (dict) --The information about values that appear frequently in a column (skewed values).\n\nSkewedColumnNames (list) --A list of names of columns that contain skewed values.\n\n(string) --\n\n\nSkewedColumnValues (list) --A list of values that appear so frequently as to be considered skewed.\n\n(string) --\n\n\nSkewedColumnValueLocationMaps (dict) --A mapping of skewed values to the columns that contain them.\n\n(string) --\n(string) --\n\n\n\n\n\n\nStoredAsSubDirectories (boolean) --\nTrue if the table data is stored in subdirectories, or False if not.\n\n\n\nParameters (dict) --These key-value pairs define partition parameters.\n\n(string) --\n(string) --\n\n\n\n\nLastAnalyzedTime (datetime) --The last time at which column statistics were computed for this partition.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.GlueEncryptionException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_table(CatalogId=None, DatabaseName=None, TableInput=None, SkipArchive=None):
    """
    Updates a metadata table in the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_table(
        CatalogId='string',
        DatabaseName='string',
        TableInput={
            'Name': 'string',
            'Description': 'string',
            'Owner': 'string',
            'LastAccessTime': datetime(2015, 1, 1),
            'LastAnalyzedTime': datetime(2015, 1, 1),
            'Retention': 123,
            'StorageDescriptor': {
                'Columns': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string',
                        'Parameters': {
                            'string': 'string'
                        }
                    },
                ],
                'Location': 'string',
                'InputFormat': 'string',
                'OutputFormat': 'string',
                'Compressed': True|False,
                'NumberOfBuckets': 123,
                'SerdeInfo': {
                    'Name': 'string',
                    'SerializationLibrary': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
                'BucketColumns': [
                    'string',
                ],
                'SortColumns': [
                    {
                        'Column': 'string',
                        'SortOrder': 123
                    },
                ],
                'Parameters': {
                    'string': 'string'
                },
                'SkewedInfo': {
                    'SkewedColumnNames': [
                        'string',
                    ],
                    'SkewedColumnValues': [
                        'string',
                    ],
                    'SkewedColumnValueLocationMaps': {
                        'string': 'string'
                    }
                },
                'StoredAsSubDirectories': True|False
            },
            'PartitionKeys': [
                {
                    'Name': 'string',
                    'Type': 'string',
                    'Comment': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                },
            ],
            'ViewOriginalText': 'string',
            'ViewExpandedText': 'string',
            'TableType': 'string',
            'Parameters': {
                'string': 'string'
            }
        },
        SkipArchive=True|False
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the table resides. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the catalog database in which the table resides. For Hive compatibility, this name is entirely lowercase.\n

    :type TableInput: dict
    :param TableInput: [REQUIRED]\nAn updated TableInput object to define the metadata table in the catalog.\n\nName (string) -- [REQUIRED]The table name. For Hive compatibility, this is folded to lowercase when it is stored.\n\nDescription (string) --A description of the table.\n\nOwner (string) --The table owner.\n\nLastAccessTime (datetime) --The last time that the table was accessed.\n\nLastAnalyzedTime (datetime) --The last time that column statistics were computed for this table.\n\nRetention (integer) --The retention time for this table.\n\nStorageDescriptor (dict) --A storage descriptor containing information about the physical storage of this table.\n\nColumns (list) --A list of the Columns in the table.\n\n(dict) --A column in a Table .\n\nName (string) -- [REQUIRED]The name of the Column .\n\nType (string) --The data type of the Column .\n\nComment (string) --A free-form text comment.\n\nParameters (dict) --These key-value pairs define properties associated with the column.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\nLocation (string) --The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.\n\nInputFormat (string) --The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.\n\nOutputFormat (string) --The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.\n\nCompressed (boolean) --\nTrue if the data in the table is compressed, or False if not.\n\nNumberOfBuckets (integer) --Must be specified if the table contains any dimension columns.\n\nSerdeInfo (dict) --The serialization/deserialization (SerDe) information.\n\nName (string) --Name of the SerDe.\n\nSerializationLibrary (string) --Usually the class that implements the SerDe. An example is org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .\n\nParameters (dict) --These key-value pairs define initialization parameters for the SerDe.\n\n(string) --\n(string) --\n\n\n\n\n\n\nBucketColumns (list) --A list of reducer grouping columns, clustering columns, and bucketing columns in the table.\n\n(string) --\n\n\nSortColumns (list) --A list specifying the sort order of each bucket in the table.\n\n(dict) --Specifies the sort order of a sorted column.\n\nColumn (string) -- [REQUIRED]The name of the column.\n\nSortOrder (integer) -- [REQUIRED]Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).\n\n\n\n\n\nParameters (dict) --The user-supplied properties in key-value form.\n\n(string) --\n(string) --\n\n\n\n\nSkewedInfo (dict) --The information about values that appear frequently in a column (skewed values).\n\nSkewedColumnNames (list) --A list of names of columns that contain skewed values.\n\n(string) --\n\n\nSkewedColumnValues (list) --A list of values that appear so frequently as to be considered skewed.\n\n(string) --\n\n\nSkewedColumnValueLocationMaps (dict) --A mapping of skewed values to the columns that contain them.\n\n(string) --\n(string) --\n\n\n\n\n\n\nStoredAsSubDirectories (boolean) --\nTrue if the table data is stored in subdirectories, or False if not.\n\n\n\nPartitionKeys (list) --A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.\nWhen you create a table used by Amazon Athena, and you do not specify any partitionKeys , you must at least set the value of partitionKeys to an empty list. For example:\n\n'PartitionKeys': []\n\n(dict) --A column in a Table .\n\nName (string) -- [REQUIRED]The name of the Column .\n\nType (string) --The data type of the Column .\n\nComment (string) --A free-form text comment.\n\nParameters (dict) --These key-value pairs define properties associated with the column.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\nViewOriginalText (string) --If the table is a view, the original text of the view; otherwise null .\n\nViewExpandedText (string) --If the table is a view, the expanded text of the view; otherwise null .\n\nTableType (string) --The type of this table (EXTERNAL_TABLE , VIRTUAL_VIEW , etc.).\n\nParameters (dict) --These key-value pairs define properties associated with the table.\n\n(string) --\n(string) --\n\n\n\n\n\n

    :type SkipArchive: boolean
    :param SkipArchive: By default, UpdateTable always creates an archived version of the table before updating it. However, if skipArchive is set to true, UpdateTable does not create the archived version.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ConcurrentModificationException
Glue.Client.exceptions.ResourceNumberLimitExceededException
Glue.Client.exceptions.GlueEncryptionException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_trigger(Name=None, TriggerUpdate=None):
    """
    Updates a trigger definition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_trigger(
        Name='string',
        TriggerUpdate={
            'Name': 'string',
            'Description': 'string',
            'Schedule': 'string',
            'Actions': [
                {
                    'JobName': 'string',
                    'Arguments': {
                        'string': 'string'
                    },
                    'Timeout': 123,
                    'SecurityConfiguration': 'string',
                    'NotificationProperty': {
                        'NotifyDelayAfter': 123
                    },
                    'CrawlerName': 'string'
                },
            ],
            'Predicate': {
                'Logical': 'AND'|'ANY',
                'Conditions': [
                    {
                        'LogicalOperator': 'EQUALS',
                        'JobName': 'string',
                        'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                        'CrawlerName': 'string',
                        'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                    },
                ]
            }
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the trigger to update.\n

    :type TriggerUpdate: dict
    :param TriggerUpdate: [REQUIRED]\nThe new values with which to update the trigger.\n\nName (string) --Reserved for future use.\n\nDescription (string) --A description of this trigger.\n\nSchedule (string) --A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .\n\nActions (list) --The actions initiated by this trigger.\n\n(dict) --Defines an action to be initiated by a trigger.\n\nJobName (string) --The name of a job to be executed.\n\nArguments (dict) --The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.\nYou can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.\nFor information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.\nFor information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.\n\n(string) --\n(string) --\n\n\n\n\nTimeout (integer) --The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.\n\nSecurityConfiguration (string) --The name of the SecurityConfiguration structure to be used with this action.\n\nNotificationProperty (dict) --Specifies configuration properties of a job run notification.\n\nNotifyDelayAfter (integer) --After a job run starts, the number of minutes to wait before sending a job run delay notification.\n\n\n\nCrawlerName (string) --The name of the crawler to be used with this action.\n\n\n\n\n\nPredicate (dict) --The predicate of this trigger, which defines when it will fire.\n\nLogical (string) --An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.\n\nConditions (list) --A list of the conditions that determine when the trigger will fire.\n\n(dict) --Defines a condition under which a trigger fires.\n\nLogicalOperator (string) --A logical operator.\n\nJobName (string) --The name of the job whose JobRuns this condition applies to, and on which this trigger waits.\n\nState (string) --The condition state. Currently, the only job states that a trigger can listen for are SUCCEEDED , STOPPED , FAILED , and TIMEOUT . The only crawler states that a trigger can listen for are SUCCEEDED , FAILED , and CANCELLED .\n\nCrawlerName (string) --The name of the crawler to which this condition applies.\n\nCrawlState (string) --The state of the crawler to which this condition applies.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Trigger': {
        'Name': 'string',
        'WorkflowName': 'string',
        'Id': 'string',
        'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
        'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
        'Description': 'string',
        'Schedule': 'string',
        'Actions': [
            {
                'JobName': 'string',
                'Arguments': {
                    'string': 'string'
                },
                'Timeout': 123,
                'SecurityConfiguration': 'string',
                'NotificationProperty': {
                    'NotifyDelayAfter': 123
                },
                'CrawlerName': 'string'
            },
        ],
        'Predicate': {
            'Logical': 'AND'|'ANY',
            'Conditions': [
                {
                    'LogicalOperator': 'EQUALS',
                    'JobName': 'string',
                    'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                    'CrawlerName': 'string',
                    'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                },
            ]
        }
    }
}


Response Structure

(dict) --

Trigger (dict) --
The resulting trigger definition.

Name (string) --
The name of the trigger.

WorkflowName (string) --
The name of the workflow associated with the trigger.

Id (string) --
Reserved for future use.

Type (string) --
The type of trigger that this is.

State (string) --
The current state of the trigger.

Description (string) --
A description of this trigger.

Schedule (string) --
A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .

Actions (list) --
The actions initiated by this trigger.

(dict) --
Defines an action to be initiated by a trigger.

JobName (string) --
The name of a job to be executed.

Arguments (dict) --
The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.

(string) --
(string) --




Timeout (integer) --
The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

SecurityConfiguration (string) --
The name of the SecurityConfiguration structure to be used with this action.

NotificationProperty (dict) --
Specifies configuration properties of a job run notification.

NotifyDelayAfter (integer) --
After a job run starts, the number of minutes to wait before sending a job run delay notification.



CrawlerName (string) --
The name of the crawler to be used with this action.





Predicate (dict) --
The predicate of this trigger, which defines when it will fire.

Logical (string) --
An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.

Conditions (list) --
A list of the conditions that determine when the trigger will fire.

(dict) --
Defines a condition under which a trigger fires.

LogicalOperator (string) --
A logical operator.

JobName (string) --
The name of the job whose JobRuns this condition applies to, and on which this trigger waits.

State (string) --
The condition state. Currently, the only job states that a trigger can listen for are SUCCEEDED , STOPPED , FAILED , and TIMEOUT . The only crawler states that a trigger can listen for are SUCCEEDED , FAILED , and CANCELLED .

CrawlerName (string) --
The name of the crawler to which this condition applies.

CrawlState (string) --
The state of the crawler to which this condition applies.















Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ConcurrentModificationException


    :return: {
        'Trigger': {
            'Name': 'string',
            'WorkflowName': 'string',
            'Id': 'string',
            'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
            'State': 'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'|'DEACTIVATED'|'DELETING'|'UPDATING',
            'Description': 'string',
            'Schedule': 'string',
            'Actions': [
                {
                    'JobName': 'string',
                    'Arguments': {
                        'string': 'string'
                    },
                    'Timeout': 123,
                    'SecurityConfiguration': 'string',
                    'NotificationProperty': {
                        'NotifyDelayAfter': 123
                    },
                    'CrawlerName': 'string'
                },
            ],
            'Predicate': {
                'Logical': 'AND'|'ANY',
                'Conditions': [
                    {
                        'LogicalOperator': 'EQUALS',
                        'JobName': 'string',
                        'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT',
                        'CrawlerName': 'string',
                        'CrawlState': 'RUNNING'|'CANCELLING'|'CANCELLED'|'SUCCEEDED'|'FAILED'
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_user_defined_function(CatalogId=None, DatabaseName=None, FunctionName=None, FunctionInput=None):
    """
    Updates an existing function definition in the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user_defined_function(
        CatalogId='string',
        DatabaseName='string',
        FunctionName='string',
        FunctionInput={
            'FunctionName': 'string',
            'ClassName': 'string',
            'OwnerName': 'string',
            'OwnerType': 'USER'|'ROLE'|'GROUP',
            'ResourceUris': [
                {
                    'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                    'Uri': 'string'
                },
            ]
        }
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the function to be updated is located. If none is provided, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]\nThe name of the catalog database where the function to be updated is located.\n

    :type FunctionName: string
    :param FunctionName: [REQUIRED]\nThe name of the function.\n

    :type FunctionInput: dict
    :param FunctionInput: [REQUIRED]\nA FunctionInput object that redefines the function in the Data Catalog.\n\nFunctionName (string) --The name of the function.\n\nClassName (string) --The Java class that contains the function code.\n\nOwnerName (string) --The owner of the function.\n\nOwnerType (string) --The owner type.\n\nResourceUris (list) --The resource URIs for the function.\n\n(dict) --The URIs for function resources.\n\nResourceType (string) --The type of the resource.\n\nUri (string) --The URI for accessing the resource.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.GlueEncryptionException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_workflow(Name=None, Description=None, DefaultRunProperties=None):
    """
    Updates an existing workflow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_workflow(
        Name='string',
        Description='string',
        DefaultRunProperties={
            'string': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the workflow to be updated.\n

    :type Description: string
    :param Description: The description of the workflow.

    :type DefaultRunProperties: dict
    :param DefaultRunProperties: A collection of properties to be used as part of each execution of the workflow.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string'
}


Response Structure

(dict) --

Name (string) --
The name of the workflow which was specified in input.







Exceptions

Glue.Client.exceptions.InvalidInputException
Glue.Client.exceptions.EntityNotFoundException
Glue.Client.exceptions.InternalServiceException
Glue.Client.exceptions.OperationTimeoutException
Glue.Client.exceptions.ConcurrentModificationException


    :return: {
        'Name': 'string'
    }
    
    
    :returns: 
    Glue.Client.exceptions.InvalidInputException
    Glue.Client.exceptions.EntityNotFoundException
    Glue.Client.exceptions.InternalServiceException
    Glue.Client.exceptions.OperationTimeoutException
    Glue.Client.exceptions.ConcurrentModificationException
    
    """
    pass

