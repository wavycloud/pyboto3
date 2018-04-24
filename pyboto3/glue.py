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
                            'Comment': 'string'
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
    :param CatalogId: The ID of the catalog in which the partion is to be created. Currently, this should be the AWS account ID.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the metadata database in which the partition is to be created.
            

    :type TableName: string
    :param TableName: [REQUIRED]
            The name of the metadata table in which the partition is to be created.
            

    :type PartitionInputList: list
    :param PartitionInputList: [REQUIRED]
            A list of PartitionInput structures that define the partitions to be created.
            (dict) --The structure used to create and update a partion.
            Values (list) --The values of the partition.
            (string) --
            LastAccessTime (datetime) --The last time at which the partition was accessed.
            StorageDescriptor (dict) --Provides information about the physical location where the partition is stored.
            Columns (list) --A list of the Columns in the table.
            (dict) --A column in a Table .
            Name (string) -- [REQUIRED]The name of the Column .
            Type (string) --The datatype of data in the Column .
            Comment (string) --Free-form text comment.
            
            Location (string) --The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
            InputFormat (string) --The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.
            OutputFormat (string) --The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.
            Compressed (boolean) --True if the data in the table is compressed, or False if not.
            NumberOfBuckets (integer) --Must be specified if the table contains any dimension columns.
            SerdeInfo (dict) --Serialization/deserialization (SerDe) information.
            Name (string) --Name of the SerDe.
            SerializationLibrary (string) --Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .
            Parameters (dict) --A list of initialization parameters for the SerDe, in key-value form.
            (string) --
            (string) --
            
            BucketColumns (list) --A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
            (string) --
            SortColumns (list) --A list specifying the sort order of each bucket in the table.
            (dict) --Specifies the sort order of a sorted column.
            Column (string) -- [REQUIRED]The name of the column.
            SortOrder (integer) -- [REQUIRED]Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).
            
            Parameters (dict) --User-supplied properties in key-value form.
            (string) --
            (string) --
            
            SkewedInfo (dict) --Information about values that appear very frequently in a column (skewed values).
            SkewedColumnNames (list) --A list of names of columns that contain skewed values.
            (string) --
            SkewedColumnValues (list) --A list of values that appear so frequently as to be considered skewed.
            (string) --
            SkewedColumnValueLocationMaps (dict) --A mapping of skewed values to the columns that contain them.
            (string) --
            (string) --
            
            StoredAsSubDirectories (boolean) --True if the table data is stored in subdirectories, or False if not.
            Parameters (dict) --Partition parameters, in the form of a list of key-value pairs.
            (string) --
            (string) --
            
            LastAnalyzedTime (datetime) --The last time at which column statistics were computed for this partition.
            
            

    :rtype: dict
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
    
    
    :example: response = client.batch_delete_connection(
        CatalogId='string',
        ConnectionNameList=[
            'string',
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the connections reside. If none is supplied, the AWS account ID is used by default.

    :type ConnectionNameList: list
    :param ConnectionNameList: [REQUIRED]
            A list of names of the connections to delete.
            (string) --
            

    :rtype: dict
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
    :param CatalogId: The ID of the Data Catalog where the partition to be deleted resides. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the catalog database in which the table in question resides.
            

    :type TableName: string
    :param TableName: [REQUIRED]
            The name of the table where the partitions to be deleted is located.
            

    :type PartitionsToDelete: list
    :param PartitionsToDelete: [REQUIRED]
            A list of PartitionInput structures that define the partitions to be deleted.
            (dict) --Contains a list of values defining partitions.
            Values (list) -- [REQUIRED]The list of values.
            (string) --
            
            

    :rtype: dict
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
    
    
    :example: response = client.batch_delete_table(
        CatalogId='string',
        DatabaseName='string',
        TablesToDelete=[
            'string',
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the table resides. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the catalog database where the tables to delete reside. For Hive compatibility, this name is entirely lowercase.
            

    :type TablesToDelete: list
    :param TablesToDelete: [REQUIRED]
            A list of the table to delete.
            (string) --
            

    :rtype: dict
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
    
    
    """
    pass

def batch_delete_table_version(CatalogId=None, DatabaseName=None, TableName=None, VersionIds=None):
    """
    Deletes a specified batch of versions of a table.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_delete_table_version(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        VersionIds=[
            'string',
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the tables reside. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.
            

    :type TableName: string
    :param TableName: [REQUIRED]
            The name of the table. For Hive compatibility, this name is entirely lowercase.
            

    :type VersionIds: list
    :param VersionIds: [REQUIRED]
            A list of the IDs of versions to be deleted.
            (string) --
            

    :rtype: dict
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
    
    
    """
    pass

def batch_get_partition(CatalogId=None, DatabaseName=None, TableName=None, PartitionsToGet=None):
    """
    Retrieves partitions in a batch request.
    See also: AWS API Documentation
    
    
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
    :param DatabaseName: [REQUIRED]
            The name of the catalog database where the partitions reside.
            

    :type TableName: string
    :param TableName: [REQUIRED]
            The name of the partitions' table.
            

    :type PartitionsToGet: list
    :param PartitionsToGet: [REQUIRED]
            A list of partition values identifying the partitions to retrieve.
            (dict) --Contains a list of values defining partitions.
            Values (list) -- [REQUIRED]The list of values.
            (string) --
            
            

    :rtype: dict
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
                            'Comment': 'string'
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

def batch_stop_job_run(JobName=None, JobRunIds=None):
    """
    Stops one or more job runs for a specified job definition.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_stop_job_run(
        JobName='string',
        JobRunIds=[
            'string',
        ]
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]
            The name of the job definition for which to stop job runs.
            

    :type JobRunIds: list
    :param JobRunIds: [REQUIRED]
            A list of the JobRunIds that should be stopped for that job definition.
            (string) --
            

    :rtype: dict
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

def create_classifier(GrokClassifier=None, XMLClassifier=None, JsonClassifier=None):
    """
    Creates a classifier in the user's account. This may be a GrokClassifier , an XMLClassifier , or abbrev JsonClassifier , depending on which field of the request is present.
    See also: AWS API Documentation
    
    
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
        }
    )
    
    
    :type GrokClassifier: dict
    :param GrokClassifier: A GrokClassifier object specifying the classifier to create.
            Classification (string) -- [REQUIRED]An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.
            Name (string) -- [REQUIRED]The name of the new classifier.
            GrokPattern (string) -- [REQUIRED]The grok pattern used by this classifier.
            CustomPatterns (string) --Optional custom grok patterns used by this classifier.
            

    :type XMLClassifier: dict
    :param XMLClassifier: An XMLClassifier object specifying the classifier to create.
            Classification (string) -- [REQUIRED]An identifier of the data format that the classifier matches.
            Name (string) -- [REQUIRED]The name of the classifier.
            RowTag (string) --The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by / ). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, row item_a='A' item_b='B'/row is okay, but row item_a='A' item_b='B' / is not).
            

    :type JsonClassifier: dict
    :param JsonClassifier: A JsonClassifier object specifying the classifier to create.
            Name (string) -- [REQUIRED]The name of the classifier.
            JsonPath (string) -- [REQUIRED]A JsonPath string defining the JSON data for the classifier to classify. AWS Glue supports a subset of JsonPath, as described in Writing JsonPath Custom Classifiers .
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_connection(CatalogId=None, ConnectionInput=None):
    """
    Creates a connection definition in the Data Catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.create_connection(
        CatalogId='string',
        ConnectionInput={
            'Name': 'string',
            'Description': 'string',
            'ConnectionType': 'JDBC'|'SFTP',
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
    :param CatalogId: The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.

    :type ConnectionInput: dict
    :param ConnectionInput: [REQUIRED]
            A ConnectionInput object defining the connection to create.
            Name (string) -- [REQUIRED]The name of the connection.
            Description (string) --Description of the connection.
            ConnectionType (string) -- [REQUIRED]The type of the connection. Currently, only JDBC is supported; SFTP is not supported.
            MatchCriteria (list) --A list of criteria that can be used in selecting this connection.
            (string) --
            ConnectionProperties (dict) -- [REQUIRED]A list of key-value pairs used as parameters for this connection.
            (string) --
            (string) --
            
            PhysicalConnectionRequirements (dict) --A map of physical connection requirements, such as VPC and SecurityGroup, needed for making this connection successfully.
            SubnetId (string) --The subnet ID used by the connection.
            SecurityGroupIdList (list) --The security group ID list used by the connection.
            (string) --
            AvailabilityZone (string) --The connection's availability zone. This field is deprecated and has no effect.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_crawler(Name=None, Role=None, DatabaseName=None, Description=None, Targets=None, Schedule=None, Classifiers=None, TablePrefix=None, SchemaChangePolicy=None, Configuration=None):
    """
    Creates a new crawler with specified targets, role, configuration, and optional schedule. At least one crawl target must be specified, in either the s3Targets or the jdbcTargets field.
    See also: AWS API Documentation
    
    
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
        Configuration='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Name of the new crawler.
            

    :type Role: string
    :param Role: [REQUIRED]
            The IAM role (or ARN of an IAM role) used by the new crawler to access customer resources.
            

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The AWS Glue database where results are written, such as: arn:aws:daylight:us-east-1::database/sometable/* .
            

    :type Description: string
    :param Description: A description of the new crawler.

    :type Targets: dict
    :param Targets: [REQUIRED]
            A list of collection of targets to crawl.
            S3Targets (list) --Specifies Amazon S3 targets.
            (dict) --Specifies a data store in Amazon S3.
            Path (string) --The path to the Amazon S3 target.
            Exclusions (list) --A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler .
            (string) --
            
            JdbcTargets (list) --Specifies JDBC targets.
            (dict) --Specifies a JDBC data store to crawl.
            ConnectionName (string) --The name of the connection to use to connect to the JDBC target.
            Path (string) --The path of the JDBC target.
            Exclusions (list) --A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler .
            (string) --
            
            

    :type Schedule: string
    :param Schedule: A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .

    :type Classifiers: list
    :param Classifiers: A list of custom classifiers that the user has registered. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.
            (string) --
            

    :type TablePrefix: string
    :param TablePrefix: The table prefix used for catalog tables that are created.

    :type SchemaChangePolicy: dict
    :param SchemaChangePolicy: Policy for the crawler's update and deletion behavior.
            UpdateBehavior (string) --The update behavior when the crawler finds a changed schema.
            DeleteBehavior (string) --The deletion behavior when the crawler finds a deleted object.
            

    :type Configuration: string
    :param Configuration: Crawler configuration information. This versioned JSON string allows users to specify aspects of a Crawler's behavior.
            You can use this field to force partitions to inherit metadata such as classification, input format, output format, serde information, and schema from their parent table, rather than detect this information separately for each partition. Use the following JSON string to specify that behavior:
            Example: '{ 'Version': 1.0, 'CrawlerOutput': { 'Partitions': { 'AddOrUpdateBehavior': 'InheritFromTable' } } }'
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_database(CatalogId=None, DatabaseInput=None):
    """
    Creates a new database in a Data Catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.create_database(
        CatalogId='string',
        DatabaseInput={
            'Name': 'string',
            'Description': 'string',
            'LocationUri': 'string',
            'Parameters': {
                'string': 'string'
            }
        }
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which to create the database. If none is supplied, the AWS account ID is used by default.

    :type DatabaseInput: dict
    :param DatabaseInput: [REQUIRED]
            A DatabaseInput object defining the metadata database to create in the catalog.
            Name (string) -- [REQUIRED]Name of the database. For Hive compatibility, this is folded to lowercase when it is stored.
            Description (string) --Description of the database
            LocationUri (string) --The location of the database (for example, an HDFS path).
            Parameters (dict) --A list of key-value pairs that define parameters and properties of the database.
            (string) --
            (string) --
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_dev_endpoint(EndpointName=None, RoleArn=None, SecurityGroupIds=None, SubnetId=None, PublicKey=None, NumberOfNodes=None, ExtraPythonLibsS3Path=None, ExtraJarsS3Path=None):
    """
    Creates a new DevEndpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.create_dev_endpoint(
        EndpointName='string',
        RoleArn='string',
        SecurityGroupIds=[
            'string',
        ],
        SubnetId='string',
        PublicKey='string',
        NumberOfNodes=123,
        ExtraPythonLibsS3Path='string',
        ExtraJarsS3Path='string'
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]
            The name to be assigned to the new DevEndpoint.
            

    :type RoleArn: string
    :param RoleArn: [REQUIRED]
            The IAM role for the DevEndpoint.
            

    :type SecurityGroupIds: list
    :param SecurityGroupIds: Security group IDs for the security groups to be used by the new DevEndpoint.
            (string) --
            

    :type SubnetId: string
    :param SubnetId: The subnet ID for the new DevEndpoint to use.

    :type PublicKey: string
    :param PublicKey: The public key to use for authentication.

    :type NumberOfNodes: integer
    :param NumberOfNodes: The number of AWS Glue Data Processing Units (DPUs) to allocate to this DevEndpoint.

    :type ExtraPythonLibsS3Path: string
    :param ExtraPythonLibsS3Path: Path(s) to one or more Python libraries in an S3 bucket that should be loaded in your DevEndpoint. Multiple values must be complete paths separated by a comma.
            Please note that only pure Python libraries can currently be used on a DevEndpoint. Libraries that rely on C extensions, such as the pandas Python data analysis library, are not yet supported.
            

    :type ExtraJarsS3Path: string
    :param ExtraJarsS3Path: Path to one or more Java Jars in an S3 bucket that should be loaded in your DevEndpoint.

    :rtype: dict
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
        'AvailabilityZone': 'string',
        'VpcId': 'string',
        'ExtraPythonLibsS3Path': 'string',
        'ExtraJarsS3Path': 'string',
        'FailureReason': 'string',
        'CreatedTimestamp': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_job(Name=None, Description=None, LogUri=None, Role=None, ExecutionProperty=None, Command=None, DefaultArguments=None, Connections=None, MaxRetries=None, AllocatedCapacity=None, Timeout=None):
    """
    Creates a new job definition.
    See also: AWS API Documentation
    
    
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
            'ScriptLocation': 'string'
        },
        DefaultArguments={
            'string': 'string'
        },
        Connections={
            'Connections': [
                'string',
            ]
        },
        MaxRetries=123,
        AllocatedCapacity=123,
        Timeout=123
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name you assign to this job definition. It must be unique in your account.
            

    :type Description: string
    :param Description: Description of the job being defined.

    :type LogUri: string
    :param LogUri: This field is reserved for future use.

    :type Role: string
    :param Role: [REQUIRED]
            The name or ARN of the IAM role associated with this job.
            

    :type ExecutionProperty: dict
    :param ExecutionProperty: An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job.
            MaxConcurrentRuns (integer) --The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.
            

    :type Command: dict
    :param Command: [REQUIRED]
            The JobCommand that executes this job.
            Name (string) --The name of the job command: this must be glueetl .
            ScriptLocation (string) --Specifies the S3 path to a script that executes a job (required).
            

    :type DefaultArguments: dict
    :param DefaultArguments: The default arguments for this job.
            You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
            For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
            For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.
            (string) --
            (string) --
            

    :type Connections: dict
    :param Connections: The connections used for this job.
            Connections (list) --A list of connections used by the job.
            (string) --
            

    :type MaxRetries: integer
    :param MaxRetries: The maximum number of times to retry this job if it fails.

    :type AllocatedCapacity: integer
    :param AllocatedCapacity: The number of AWS Glue data processing units (DPUs) to allocate to this Job. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .

    :type Timeout: integer
    :param Timeout: The job timeout in minutes. The default is 2880 minutes (48 hours).

    :rtype: dict
    :return: {
        'Name': 'string'
    }
    
    
    """
    pass

def create_partition(CatalogId=None, DatabaseName=None, TableName=None, PartitionInput=None):
    """
    Creates a new partition.
    See also: AWS API Documentation
    
    
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
                        'Comment': 'string'
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
    :param CatalogId: The ID of the catalog in which the partion is to be created. Currently, this should be the AWS account ID.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the metadata database in which the partition is to be created.
            

    :type TableName: string
    :param TableName: [REQUIRED]
            The name of the metadata table in which the partition is to be created.
            

    :type PartitionInput: dict
    :param PartitionInput: [REQUIRED]
            A PartitionInput structure defining the partition to be created.
            Values (list) --The values of the partition.
            (string) --
            LastAccessTime (datetime) --The last time at which the partition was accessed.
            StorageDescriptor (dict) --Provides information about the physical location where the partition is stored.
            Columns (list) --A list of the Columns in the table.
            (dict) --A column in a Table .
            Name (string) -- [REQUIRED]The name of the Column .
            Type (string) --The datatype of data in the Column .
            Comment (string) --Free-form text comment.
            
            Location (string) --The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
            InputFormat (string) --The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.
            OutputFormat (string) --The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.
            Compressed (boolean) --True if the data in the table is compressed, or False if not.
            NumberOfBuckets (integer) --Must be specified if the table contains any dimension columns.
            SerdeInfo (dict) --Serialization/deserialization (SerDe) information.
            Name (string) --Name of the SerDe.
            SerializationLibrary (string) --Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .
            Parameters (dict) --A list of initialization parameters for the SerDe, in key-value form.
            (string) --
            (string) --
            
            BucketColumns (list) --A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
            (string) --
            SortColumns (list) --A list specifying the sort order of each bucket in the table.
            (dict) --Specifies the sort order of a sorted column.
            Column (string) -- [REQUIRED]The name of the column.
            SortOrder (integer) -- [REQUIRED]Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).
            
            Parameters (dict) --User-supplied properties in key-value form.
            (string) --
            (string) --
            
            SkewedInfo (dict) --Information about values that appear very frequently in a column (skewed values).
            SkewedColumnNames (list) --A list of names of columns that contain skewed values.
            (string) --
            SkewedColumnValues (list) --A list of values that appear so frequently as to be considered skewed.
            (string) --
            SkewedColumnValueLocationMaps (dict) --A mapping of skewed values to the columns that contain them.
            (string) --
            (string) --
            
            StoredAsSubDirectories (boolean) --True if the table data is stored in subdirectories, or False if not.
            Parameters (dict) --Partition parameters, in the form of a list of key-value pairs.
            (string) --
            (string) --
            
            LastAnalyzedTime (datetime) --The last time at which column statistics were computed for this partition.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_script(DagNodes=None, DagEdges=None, Language=None):
    """
    Transforms a directed acyclic graph (DAG) into code.
    See also: AWS API Documentation
    
    
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
    :param DagNodes: A list of the nodes in the DAG.
            (dict) --Represents a node in a directed acyclic graph (DAG)
            Id (string) -- [REQUIRED]A node identifier that is unique within the node's graph.
            NodeType (string) -- [REQUIRED]The type of node this is.
            Args (list) -- [REQUIRED]Properties of the node, in the form of name-value pairs.
            (dict) --An argument or property of a node.
            Name (string) -- [REQUIRED]The name of the argument or property.
            Value (string) -- [REQUIRED]The value of the argument or property.
            Param (boolean) --True if the value is used as a parameter.
            
            LineNumber (integer) --The line number of the node.
            
            

    :type DagEdges: list
    :param DagEdges: A list of the edges in the DAG.
            (dict) --Represents a directional edge in a directed acyclic graph (DAG).
            Source (string) -- [REQUIRED]The ID of the node at which the edge starts.
            Target (string) -- [REQUIRED]The ID of the node at which the edge ends.
            TargetParameter (string) --The target of the edge.
            
            

    :type Language: string
    :param Language: The programming language of the resulting code from the DAG.

    :rtype: dict
    :return: {
        'PythonScript': 'string',
        'ScalaCode': 'string'
    }
    
    
    """
    pass

def create_table(CatalogId=None, DatabaseName=None, TableInput=None):
    """
    Creates a new table definition in the Data Catalog.
    See also: AWS API Documentation
    
    
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
                        'Comment': 'string'
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
                    'Comment': 'string'
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
    :param DatabaseName: [REQUIRED]
            The catalog database in which to create the new table. For Hive compatibility, this name is entirely lowercase.
            

    :type TableInput: dict
    :param TableInput: [REQUIRED]
            The TableInput object that defines the metadata table to create in the catalog.
            Name (string) -- [REQUIRED]Name of the table. For Hive compatibility, this is folded to lowercase when it is stored.
            Description (string) --Description of the table.
            Owner (string) --Owner of the table.
            LastAccessTime (datetime) --Last time the table was accessed.
            LastAnalyzedTime (datetime) --Last time column statistics were computed for this table.
            Retention (integer) --Retention time for this table.
            StorageDescriptor (dict) --A storage descriptor containing information about the physical storage of this table.
            Columns (list) --A list of the Columns in the table.
            (dict) --A column in a Table .
            Name (string) -- [REQUIRED]The name of the Column .
            Type (string) --The datatype of data in the Column .
            Comment (string) --Free-form text comment.
            
            Location (string) --The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
            InputFormat (string) --The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.
            OutputFormat (string) --The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.
            Compressed (boolean) --True if the data in the table is compressed, or False if not.
            NumberOfBuckets (integer) --Must be specified if the table contains any dimension columns.
            SerdeInfo (dict) --Serialization/deserialization (SerDe) information.
            Name (string) --Name of the SerDe.
            SerializationLibrary (string) --Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .
            Parameters (dict) --A list of initialization parameters for the SerDe, in key-value form.
            (string) --
            (string) --
            
            BucketColumns (list) --A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
            (string) --
            SortColumns (list) --A list specifying the sort order of each bucket in the table.
            (dict) --Specifies the sort order of a sorted column.
            Column (string) -- [REQUIRED]The name of the column.
            SortOrder (integer) -- [REQUIRED]Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).
            
            Parameters (dict) --User-supplied properties in key-value form.
            (string) --
            (string) --
            
            SkewedInfo (dict) --Information about values that appear very frequently in a column (skewed values).
            SkewedColumnNames (list) --A list of names of columns that contain skewed values.
            (string) --
            SkewedColumnValues (list) --A list of values that appear so frequently as to be considered skewed.
            (string) --
            SkewedColumnValueLocationMaps (dict) --A mapping of skewed values to the columns that contain them.
            (string) --
            (string) --
            
            StoredAsSubDirectories (boolean) --True if the table data is stored in subdirectories, or False if not.
            PartitionKeys (list) --A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
            (dict) --A column in a Table .
            Name (string) -- [REQUIRED]The name of the Column .
            Type (string) --The datatype of data in the Column .
            Comment (string) --Free-form text comment.
            
            ViewOriginalText (string) --If the table is a view, the original text of the view; otherwise null .
            ViewExpandedText (string) --If the table is a view, the expanded text of the view; otherwise null .
            TableType (string) --The type of this table (EXTERNAL_TABLE , VIRTUAL_VIEW , etc.).
            Parameters (dict) --Properties associated with this table, as a list of key-value pairs.
            (string) --
            (string) --
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_trigger(Name=None, Type=None, Schedule=None, Predicate=None, Actions=None, Description=None, StartOnCreation=None):
    """
    Creates a new trigger.
    See also: AWS API Documentation
    
    
    :example: response = client.create_trigger(
        Name='string',
        Type='SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
        Schedule='string',
        Predicate={
            'Logical': 'AND'|'ANY',
            'Conditions': [
                {
                    'LogicalOperator': 'EQUALS',
                    'JobName': 'string',
                    'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT'
                },
            ]
        },
        Actions=[
            {
                'JobName': 'string',
                'Arguments': {
                    'string': 'string'
                },
                'Timeout': 123
            },
        ],
        Description='string',
        StartOnCreation=True|False
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the trigger.
            

    :type Type: string
    :param Type: [REQUIRED]
            The type of the new trigger.
            

    :type Schedule: string
    :param Schedule: A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .
            This field is required when the trigger type is SCHEDULED.
            

    :type Predicate: dict
    :param Predicate: A predicate to specify when the new trigger should fire.
            This field is required when the trigger type is CONDITIONAL.
            Logical (string) --Optional field if only one condition is listed. If multiple conditions are listed, then this field is required.
            Conditions (list) --A list of the conditions that determine when the trigger will fire.
            (dict) --Defines a condition under which a trigger fires.
            LogicalOperator (string) --A logical operator.
            JobName (string) --The name of the Job to whose JobRuns this condition applies and on which this trigger waits.
            State (string) --The condition state. Currently, the values supported are SUCCEEDED, STOPPED, TIMEOUT and FAILED.
            
            

    :type Actions: list
    :param Actions: [REQUIRED]
            The actions initiated by this trigger when it fires.
            (dict) --Defines an action to be initiated by a trigger.
            JobName (string) --The name of a job to be executed.
            Arguments (dict) --Arguments to be passed to the job.
            You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
            For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
            For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.
            (string) --
            (string) --
            
            Timeout (integer) --The job run timeout in minutes. It overrides the timeout value of the job.
            
            

    :type Description: string
    :param Description: A description of the new trigger.

    :type StartOnCreation: boolean
    :param StartOnCreation: Set to true to start SCHEDULED and CONDITIONAL triggers when created. True not supported for ON_DEMAND triggers.

    :rtype: dict
    :return: {
        'Name': 'string'
    }
    
    
    """
    pass

def create_user_defined_function(CatalogId=None, DatabaseName=None, FunctionInput=None):
    """
    Creates a new function definition in the Data Catalog.
    See also: AWS API Documentation
    
    
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
    :param CatalogId: The ID of the Data Catalog in which to create the function. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the catalog database in which to create the function.
            

    :type FunctionInput: dict
    :param FunctionInput: [REQUIRED]
            A FunctionInput object that defines the function to create in the Data Catalog.
            FunctionName (string) --The name of the function.
            ClassName (string) --The Java class that contains the function code.
            OwnerName (string) --The owner of the function.
            OwnerType (string) --The owner type.
            ResourceUris (list) --The resource URIs for the function.
            (dict) --URIs for function resources.
            ResourceType (string) --The type of the resource.
            Uri (string) --The URI for accessing the resource.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_classifier(Name=None):
    """
    Removes a classifier from the Data Catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_classifier(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Name of the classifier to remove.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_connection(CatalogId=None, ConnectionName=None):
    """
    Deletes a connection from the Data Catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_connection(
        CatalogId='string',
        ConnectionName='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the connection resides. If none is supplied, the AWS account ID is used by default.

    :type ConnectionName: string
    :param ConnectionName: [REQUIRED]
            The name of the connection to delete.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_crawler(Name=None):
    """
    Removes a specified crawler from the Data Catalog, unless the crawler state is RUNNING .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_crawler(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Name of the crawler to remove.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_database(CatalogId=None, Name=None):
    """
    Removes a specified Database from a Data Catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_database(
        CatalogId='string',
        Name='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the database resides. If none is supplied, the AWS account ID is used by default.

    :type Name: string
    :param Name: [REQUIRED]
            The name of the Database to delete. For Hive compatibility, this must be all lowercase.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_dev_endpoint(EndpointName=None):
    """
    Deletes a specified DevEndpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_dev_endpoint(
        EndpointName='string'
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]
            The name of the DevEndpoint.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_job(JobName=None):
    """
    Deletes a specified job definition. If the job definition is not found, no exception is thrown.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_job(
        JobName='string'
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]
            The name of the job definition to delete.
            

    :rtype: dict
    :return: {
        'JobName': 'string'
    }
    
    
    """
    pass

def delete_partition(CatalogId=None, DatabaseName=None, TableName=None, PartitionValues=None):
    """
    Deletes a specified partition.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_partition(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        PartitionValues=[
            'string',
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the partition to be deleted resides. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the catalog database in which the table in question resides.
            

    :type TableName: string
    :param TableName: [REQUIRED]
            The name of the table where the partition to be deleted is located.
            

    :type PartitionValues: list
    :param PartitionValues: [REQUIRED]
            The values that define the partition.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_table(CatalogId=None, DatabaseName=None, Name=None):
    """
    Removes a table definition from the Data Catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_table(
        CatalogId='string',
        DatabaseName='string',
        Name='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the table resides. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the catalog database in which the table resides. For Hive compatibility, this name is entirely lowercase.
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the table to be deleted. For Hive compatibility, this name is entirely lowercase.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_table_version(CatalogId=None, DatabaseName=None, TableName=None, VersionId=None):
    """
    Deletes a specified version of a table.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_table_version(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        VersionId='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the tables reside. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.
            

    :type TableName: string
    :param TableName: [REQUIRED]
            The name of the table. For Hive compatibility, this name is entirely lowercase.
            

    :type VersionId: string
    :param VersionId: [REQUIRED]
            The ID of the table version to be deleted.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_trigger(Name=None):
    """
    Deletes a specified trigger. If the trigger is not found, no exception is thrown.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_trigger(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the trigger to delete.
            

    :rtype: dict
    :return: {
        'Name': 'string'
    }
    
    
    """
    pass

def delete_user_defined_function(CatalogId=None, DatabaseName=None, FunctionName=None):
    """
    Deletes an existing function definition from the Data Catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_user_defined_function(
        CatalogId='string',
        DatabaseName='string',
        FunctionName='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the function to be deleted is located. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the catalog database where the function is located.
            

    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the function definition to be deleted.
            

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

def get_catalog_import_status(CatalogId=None):
    """
    Retrieves the status of a migration operation.
    See also: AWS API Documentation
    
    
    :example: response = client.get_catalog_import_status(
        CatalogId='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the catalog to migrate. Currently, this should be the AWS account ID.

    :rtype: dict
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
    
    
    :example: response = client.get_classifier(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Name of the classifier to retrieve.
            

    :rtype: dict
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
            }
        }
    }
    
    
    """
    pass

def get_classifiers(MaxResults=None, NextToken=None):
    """
    Lists all classifier objects in the Data Catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.get_classifiers(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Size of the list to return (optional).

    :type NextToken: string
    :param NextToken: An optional continuation token.

    :rtype: dict
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
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def get_connection(CatalogId=None, Name=None):
    """
    Retrieves a connection definition from the Data Catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.get_connection(
        CatalogId='string',
        Name='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the connection resides. If none is supplied, the AWS account ID is used by default.

    :type Name: string
    :param Name: [REQUIRED]
            The name of the connection definition to retrieve.
            

    :rtype: dict
    :return: {
        'Connection': {
            'Name': 'string',
            'Description': 'string',
            'ConnectionType': 'JDBC'|'SFTP',
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

def get_connections(CatalogId=None, Filter=None, NextToken=None, MaxResults=None):
    """
    Retrieves a list of connection definitions from the Data Catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.get_connections(
        CatalogId='string',
        Filter={
            'MatchCriteria': [
                'string',
            ],
            'ConnectionType': 'JDBC'|'SFTP'
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the connections reside. If none is supplied, the AWS account ID is used by default.

    :type Filter: dict
    :param Filter: A filter that controls which connections will be returned.
            MatchCriteria (list) --A criteria string that must match the criteria recorded in the connection definition for that connection definition to be returned.
            (string) --
            ConnectionType (string) --The type of connections to return. Currently, only JDBC is supported; SFTP is not supported.
            

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of connections to return in one response.

    :rtype: dict
    :return: {
        'ConnectionList': [
            {
                'Name': 'string',
                'Description': 'string',
                'ConnectionType': 'JDBC'|'SFTP',
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
    
    
    :example: response = client.get_crawler(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Name of the crawler to retrieve metadata for.
            

    :rtype: dict
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
            'Configuration': 'string'
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
    
    
    :example: response = client.get_crawler_metrics(
        CrawlerNameList=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type CrawlerNameList: list
    :param CrawlerNameList: A list of the names of crawlers about which to retrieve metrics.
            (string) --
            

    :type MaxResults: integer
    :param MaxResults: The maximum size of a list to return.

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :rtype: dict
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
    
    
    """
    pass

def get_crawlers(MaxResults=None, NextToken=None):
    """
    Retrieves metadata for all crawlers defined in the customer account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_crawlers(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The number of crawlers to return on each call.

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation request.

    :rtype: dict
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
                'Configuration': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_database(CatalogId=None, Name=None):
    """
    Retrieves the definition of a specified database.
    See also: AWS API Documentation
    
    
    :example: response = client.get_database(
        CatalogId='string',
        Name='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the database resides. If none is supplied, the AWS account ID is used by default.

    :type Name: string
    :param Name: [REQUIRED]
            The name of the database to retrieve. For Hive compatibility, this should be all lowercase.
            

    :rtype: dict
    :return: {
        'Database': {
            'Name': 'string',
            'Description': 'string',
            'LocationUri': 'string',
            'Parameters': {
                'string': 'string'
            },
            'CreateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_databases(CatalogId=None, NextToken=None, MaxResults=None):
    """
    Retrieves all Databases defined in a given Data Catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.get_databases(
        CatalogId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog from which to retrieve Databases . If none is supplied, the AWS account ID is used by default.

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of databases to return in one response.

    :rtype: dict
    :return: {
        'DatabaseList': [
            {
                'Name': 'string',
                'Description': 'string',
                'LocationUri': 'string',
                'Parameters': {
                    'string': 'string'
                },
                'CreateTime': datetime(2015, 1, 1)
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
    
    
    :example: response = client.get_dataflow_graph(
        PythonScript='string'
    )
    
    
    :type PythonScript: string
    :param PythonScript: The Python script to transform.

    :rtype: dict
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
    Retrieves information about a specified DevEndpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.get_dev_endpoint(
        EndpointName='string'
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]
            Name of the DevEndpoint for which to retrieve information.
            

    :rtype: dict
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
            'NumberOfNodes': 123,
            'AvailabilityZone': 'string',
            'VpcId': 'string',
            'ExtraPythonLibsS3Path': 'string',
            'ExtraJarsS3Path': 'string',
            'FailureReason': 'string',
            'LastUpdateStatus': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'LastModifiedTimestamp': datetime(2015, 1, 1),
            'PublicKey': 'string'
        }
    }
    
    
    """
    pass

def get_dev_endpoints(MaxResults=None, NextToken=None):
    """
    Retrieves all the DevEndpoints in this AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_dev_endpoints(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum size of information to return.

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :rtype: dict
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
                'NumberOfNodes': 123,
                'AvailabilityZone': 'string',
                'VpcId': 'string',
                'ExtraPythonLibsS3Path': 'string',
                'ExtraJarsS3Path': 'string',
                'FailureReason': 'string',
                'LastUpdateStatus': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'LastModifiedTimestamp': datetime(2015, 1, 1),
                'PublicKey': 'string'
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
    
    
    :example: response = client.get_job(
        JobName='string'
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]
            The name of the job definition to retrieve.
            

    :rtype: dict
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
                'ScriptLocation': 'string'
            },
            'DefaultArguments': {
                'string': 'string'
            },
            'Connections': {
                'Connections': [
                    'string',
                ]
            },
            'MaxRetries': 123,
            'AllocatedCapacity': 123,
            'Timeout': 123
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_job_run(JobName=None, RunId=None, PredecessorsIncluded=None):
    """
    Retrieves the metadata for a given job run.
    See also: AWS API Documentation
    
    
    :example: response = client.get_job_run(
        JobName='string',
        RunId='string',
        PredecessorsIncluded=True|False
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]
            Name of the job definition being run.
            

    :type RunId: string
    :param RunId: [REQUIRED]
            The ID of the job run.
            

    :type PredecessorsIncluded: boolean
    :param PredecessorsIncluded: True if a list of predecessor runs should be returned.

    :rtype: dict
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
            'Timeout': 123
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
    
    
    :example: response = client.get_job_runs(
        JobName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]
            The name of the job definition for which to retrieve all job runs.
            

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :type MaxResults: integer
    :param MaxResults: The maximum size of the response.

    :rtype: dict
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
                'Timeout': 123
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
    
    
    :example: response = client.get_jobs(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :type MaxResults: integer
    :param MaxResults: The maximum size of the response.

    :rtype: dict
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
                    'ScriptLocation': 'string'
                },
                'DefaultArguments': {
                    'string': 'string'
                },
                'Connections': {
                    'Connections': [
                        'string',
                    ]
                },
                'MaxRetries': 123,
                'AllocatedCapacity': 123,
                'Timeout': 123
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
            ]
        }
    )
    
    
    :type Source: dict
    :param Source: [REQUIRED]
            Specifies the source table.
            DatabaseName (string) -- [REQUIRED]The database in which the table metadata resides.
            TableName (string) -- [REQUIRED]The name of the table in question.
            

    :type Sinks: list
    :param Sinks: A list of target tables.
            (dict) --Specifies a table definition in the Data Catalog.
            DatabaseName (string) -- [REQUIRED]The database in which the table metadata resides.
            TableName (string) -- [REQUIRED]The name of the table in question.
            
            

    :type Location: dict
    :param Location: Parameters for the mapping.
            Jdbc (list) --A JDBC location.
            (dict) --An argument or property of a node.
            Name (string) -- [REQUIRED]The name of the argument or property.
            Value (string) -- [REQUIRED]The value of the argument or property.
            Param (boolean) --True if the value is used as a parameter.
            
            S3 (list) --An Amazon S3 location.
            (dict) --An argument or property of a node.
            Name (string) -- [REQUIRED]The name of the argument or property.
            Value (string) -- [REQUIRED]The value of the argument or property.
            Param (boolean) --True if the value is used as a parameter.
            
            

    :rtype: dict
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

def get_partition(CatalogId=None, DatabaseName=None, TableName=None, PartitionValues=None):
    """
    Retrieves information about a specified partition.
    See also: AWS API Documentation
    
    
    :example: response = client.get_partition(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        PartitionValues=[
            'string',
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the partition in question resides. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the catalog database where the partition resides.
            

    :type TableName: string
    :param TableName: [REQUIRED]
            The name of the partition's table.
            

    :type PartitionValues: list
    :param PartitionValues: [REQUIRED]
            The values that define the partition.
            (string) --
            

    :rtype: dict
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
                        'Comment': 'string'
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
    :param CatalogId: The ID of the Data Catalog where the partitions in question reside. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the catalog database where the partitions reside.
            

    :type TableName: string
    :param TableName: [REQUIRED]
            The name of the partitions' table.
            

    :type Expression: string
    :param Expression: An expression filtering the partitions to be returned.

    :type NextToken: string
    :param NextToken: A continuation token, if this is not the first call to retrieve these partitions.

    :type Segment: dict
    :param Segment: The segment of the table's partitions to scan in this request.
            SegmentNumber (integer) -- [REQUIRED]The zero-based index number of the this segment. For example, if the total number of segments is 4, SegmentNumber values will range from zero through three.
            TotalSegments (integer) -- [REQUIRED]The total numer of segments.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of partitions to return in a single response.

    :rtype: dict
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
                            'Comment': 'string'
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
            ]
        },
        Language='PYTHON'|'SCALA'
    )
    
    
    :type Mapping: list
    :param Mapping: [REQUIRED]
            The list of mappings from a source table to target tables.
            (dict) --Defines a mapping.
            SourceTable (string) --The name of the source table.
            SourcePath (string) --The source path.
            SourceType (string) --The source type.
            TargetTable (string) --The target table.
            TargetPath (string) --The target path.
            TargetType (string) --The target type.
            
            

    :type Source: dict
    :param Source: [REQUIRED]
            The source table.
            DatabaseName (string) -- [REQUIRED]The database in which the table metadata resides.
            TableName (string) -- [REQUIRED]The name of the table in question.
            

    :type Sinks: list
    :param Sinks: The target tables.
            (dict) --Specifies a table definition in the Data Catalog.
            DatabaseName (string) -- [REQUIRED]The database in which the table metadata resides.
            TableName (string) -- [REQUIRED]The name of the table in question.
            
            

    :type Location: dict
    :param Location: Parameters for the mapping.
            Jdbc (list) --A JDBC location.
            (dict) --An argument or property of a node.
            Name (string) -- [REQUIRED]The name of the argument or property.
            Value (string) -- [REQUIRED]The value of the argument or property.
            Param (boolean) --True if the value is used as a parameter.
            
            S3 (list) --An Amazon S3 location.
            (dict) --An argument or property of a node.
            Name (string) -- [REQUIRED]The name of the argument or property.
            Value (string) -- [REQUIRED]The value of the argument or property.
            Param (boolean) --True if the value is used as a parameter.
            
            

    :type Language: string
    :param Language: The programming language of the code to perform the mapping.

    :rtype: dict
    :return: {
        'PythonScript': 'string',
        'ScalaCode': 'string'
    }
    
    
    """
    pass

def get_table(CatalogId=None, DatabaseName=None, Name=None):
    """
    Retrieves the Table definition in a Data Catalog for a specified table.
    See also: AWS API Documentation
    
    
    :example: response = client.get_table(
        CatalogId='string',
        DatabaseName='string',
        Name='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the table resides. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the table for which to retrieve the definition. For Hive compatibility, this name is entirely lowercase.
            

    :rtype: dict
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
                        'Comment': 'string'
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
                    'Comment': 'string'
                },
            ],
            'ViewOriginalText': 'string',
            'ViewExpandedText': 'string',
            'TableType': 'string',
            'Parameters': {
                'string': 'string'
            },
            'CreatedBy': 'string'
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
    
    
    :example: response = client.get_table_version(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        VersionId='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the tables reside. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.
            

    :type TableName: string
    :param TableName: [REQUIRED]
            The name of the table. For Hive compatibility, this name is entirely lowercase.
            

    :type VersionId: string
    :param VersionId: The ID value of the table version to be retrieved.

    :rtype: dict
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
                            'Comment': 'string'
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
                        'Comment': 'string'
                    },
                ],
                'ViewOriginalText': 'string',
                'ViewExpandedText': 'string',
                'TableType': 'string',
                'Parameters': {
                    'string': 'string'
                },
                'CreatedBy': 'string'
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
    
    
    :example: response = client.get_table_versions(
        CatalogId='string',
        DatabaseName='string',
        TableName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the tables reside. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.
            

    :type TableName: string
    :param TableName: [REQUIRED]
            The name of the table. For Hive compatibility, this name is entirely lowercase.
            

    :type NextToken: string
    :param NextToken: A continuation token, if this is not the first call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of table versions to return in one response.

    :rtype: dict
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
                                'Comment': 'string'
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
                            'Comment': 'string'
                        },
                    ],
                    'ViewOriginalText': 'string',
                    'ViewExpandedText': 'string',
                    'TableType': 'string',
                    'Parameters': {
                        'string': 'string'
                    },
                    'CreatedBy': 'string'
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
    
    
    :example: response = client.get_tables(
        CatalogId='string',
        DatabaseName='string',
        Expression='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the tables reside. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The database in the catalog whose tables to list. For Hive compatibility, this name is entirely lowercase.
            

    :type Expression: string
    :param Expression: A regular expression pattern. If present, only those tables whose names match the pattern are returned.

    :type NextToken: string
    :param NextToken: A continuation token, included if this is a continuation call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of tables to return in a single response.

    :rtype: dict
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
                            'Comment': 'string'
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
                        'Comment': 'string'
                    },
                ],
                'ViewOriginalText': 'string',
                'ViewExpandedText': 'string',
                'TableType': 'string',
                'Parameters': {
                    'string': 'string'
                },
                'CreatedBy': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_trigger(Name=None):
    """
    Retrieves the definition of a trigger.
    See also: AWS API Documentation
    
    
    :example: response = client.get_trigger(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the trigger to retrieve.
            

    :rtype: dict
    :return: {
        'Trigger': {
            'Name': 'string',
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
                    'Timeout': 123
                },
            ],
            'Predicate': {
                'Logical': 'AND'|'ANY',
                'Conditions': [
                    {
                        'LogicalOperator': 'EQUALS',
                        'JobName': 'string',
                        'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT'
                    },
                ]
            }
        }
    }
    
    
    """
    pass

def get_triggers(NextToken=None, DependentJobName=None, MaxResults=None):
    """
    Gets all the triggers associated with a job.
    See also: AWS API Documentation
    
    
    :example: response = client.get_triggers(
        NextToken='string',
        DependentJobName='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :type DependentJobName: string
    :param DependentJobName: The name of the job for which to retrieve triggers. The trigger that can start this job will be returned, and if there is no such trigger, all triggers will be returned.

    :type MaxResults: integer
    :param MaxResults: The maximum size of the response.

    :rtype: dict
    :return: {
        'Triggers': [
            {
                'Name': 'string',
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
                        'Timeout': 123
                    },
                ],
                'Predicate': {
                    'Logical': 'AND'|'ANY',
                    'Conditions': [
                        {
                            'LogicalOperator': 'EQUALS',
                            'JobName': 'string',
                            'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT'
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
    
    
    :example: response = client.get_user_defined_function(
        CatalogId='string',
        DatabaseName='string',
        FunctionName='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the function to be retrieved is located. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the catalog database where the function is located.
            

    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the function.
            

    :rtype: dict
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
    
    
    """
    pass

def get_user_defined_functions(CatalogId=None, DatabaseName=None, Pattern=None, NextToken=None, MaxResults=None):
    """
    Retrieves a multiple function definitions from the Data Catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.get_user_defined_functions(
        CatalogId='string',
        DatabaseName='string',
        Pattern='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog where the functions to be retrieved are located. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the catalog database where the functions are located.
            

    :type Pattern: string
    :param Pattern: [REQUIRED]
            An optional function-name pattern string that filters the function definitions returned.
            

    :type NextToken: string
    :param NextToken: A continuation token, if this is a continuation call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of functions to return in one response.

    :rtype: dict
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
    
    
    """
    pass

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def import_catalog_to_glue(CatalogId=None):
    """
    Imports an existing Athena Data Catalog to AWS Glue
    See also: AWS API Documentation
    
    
    :example: response = client.import_catalog_to_glue(
        CatalogId='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the catalog to import. Currently, this should be the AWS account ID.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def reset_job_bookmark(JobName=None):
    """
    Resets a bookmark entry.
    See also: AWS API Documentation
    
    
    :example: response = client.reset_job_bookmark(
        JobName='string'
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]
            The name of the job in question.
            

    :rtype: dict
    :return: {
        'JobBookmarkEntry': {
            'JobName': 'string',
            'Version': 123,
            'Run': 123,
            'Attempt': 123,
            'JobBookmark': 'string'
        }
    }
    
    
    """
    pass

def start_crawler(Name=None):
    """
    Starts a crawl using the specified crawler, regardless of what is scheduled. If the crawler is already running, does nothing.
    See also: AWS API Documentation
    
    
    :example: response = client.start_crawler(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Name of the crawler to start.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def start_crawler_schedule(CrawlerName=None):
    """
    Changes the schedule state of the specified crawler to SCHEDULED , unless the crawler is already running or the schedule state is already SCHEDULED .
    See also: AWS API Documentation
    
    
    :example: response = client.start_crawler_schedule(
        CrawlerName='string'
    )
    
    
    :type CrawlerName: string
    :param CrawlerName: [REQUIRED]
            Name of the crawler to schedule.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def start_job_run(JobName=None, JobRunId=None, Arguments=None, AllocatedCapacity=None, Timeout=None):
    """
    Starts a job run using a job definition.
    See also: AWS API Documentation
    
    
    :example: response = client.start_job_run(
        JobName='string',
        JobRunId='string',
        Arguments={
            'string': 'string'
        },
        AllocatedCapacity=123,
        Timeout=123
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]
            The name of the job definition to use.
            

    :type JobRunId: string
    :param JobRunId: The ID of a previous JobRun to retry.

    :type Arguments: dict
    :param Arguments: The job arguments specifically for this run. They override the equivalent default arguments set for in the job definition itself.
            You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
            For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
            For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.
            (string) --
            (string) --
            

    :type AllocatedCapacity: integer
    :param AllocatedCapacity: The number of AWS Glue data processing units (DPUs) to allocate to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .

    :type Timeout: integer
    :param Timeout: The job run timeout in minutes. It overrides the timeout value of the job.

    :rtype: dict
    :return: {
        'JobRunId': 'string'
    }
    
    
    """
    pass

def start_trigger(Name=None):
    """
    Starts an existing trigger. See Triggering Jobs for information about how different types of trigger are started.
    See also: AWS API Documentation
    
    
    :example: response = client.start_trigger(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the trigger to start.
            

    :rtype: dict
    :return: {
        'Name': 'string'
    }
    
    
    """
    pass

def stop_crawler(Name=None):
    """
    If the specified crawler is running, stops the crawl.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_crawler(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Name of the crawler to stop.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def stop_crawler_schedule(CrawlerName=None):
    """
    Sets the schedule state of the specified crawler to NOT_SCHEDULED , but does not stop the crawler if it is already running.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_crawler_schedule(
        CrawlerName='string'
    )
    
    
    :type CrawlerName: string
    :param CrawlerName: [REQUIRED]
            Name of the crawler whose schedule state to set.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def stop_trigger(Name=None):
    """
    Stops a specified trigger.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_trigger(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the trigger to stop.
            

    :rtype: dict
    :return: {
        'Name': 'string'
    }
    
    
    """
    pass

def update_classifier(GrokClassifier=None, XMLClassifier=None, JsonClassifier=None):
    """
    Modifies an existing classifier (a GrokClassifier , XMLClassifier , or JsonClassifier , depending on which field is present).
    See also: AWS API Documentation
    
    
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
        }
    )
    
    
    :type GrokClassifier: dict
    :param GrokClassifier: A GrokClassifier object with updated fields.
            Name (string) -- [REQUIRED]The name of the GrokClassifier .
            Classification (string) --An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.
            GrokPattern (string) --The grok pattern used by this classifier.
            CustomPatterns (string) --Optional custom grok patterns used by this classifier.
            

    :type XMLClassifier: dict
    :param XMLClassifier: An XMLClassifier object with updated fields.
            Name (string) -- [REQUIRED]The name of the classifier.
            Classification (string) --An identifier of the data format that the classifier matches.
            RowTag (string) --The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by / ). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, row item_a='A' item_b='B'/row is okay, but row item_a='A' item_b='B' / is not).
            

    :type JsonClassifier: dict
    :param JsonClassifier: A JsonClassifier object with updated fields.
            Name (string) -- [REQUIRED]The name of the classifier.
            JsonPath (string) --A JsonPath string defining the JSON data for the classifier to classify. AWS Glue supports a subset of JsonPath, as described in Writing JsonPath Custom Classifiers .
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_connection(CatalogId=None, Name=None, ConnectionInput=None):
    """
    Updates a connection definition in the Data Catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.update_connection(
        CatalogId='string',
        Name='string',
        ConnectionInput={
            'Name': 'string',
            'Description': 'string',
            'ConnectionType': 'JDBC'|'SFTP',
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
    :param CatalogId: The ID of the Data Catalog in which the connection resides. If none is supplied, the AWS account ID is used by default.

    :type Name: string
    :param Name: [REQUIRED]
            The name of the connection definition to update.
            

    :type ConnectionInput: dict
    :param ConnectionInput: [REQUIRED]
            A ConnectionInput object that redefines the connection in question.
            Name (string) -- [REQUIRED]The name of the connection.
            Description (string) --Description of the connection.
            ConnectionType (string) -- [REQUIRED]The type of the connection. Currently, only JDBC is supported; SFTP is not supported.
            MatchCriteria (list) --A list of criteria that can be used in selecting this connection.
            (string) --
            ConnectionProperties (dict) -- [REQUIRED]A list of key-value pairs used as parameters for this connection.
            (string) --
            (string) --
            
            PhysicalConnectionRequirements (dict) --A map of physical connection requirements, such as VPC and SecurityGroup, needed for making this connection successfully.
            SubnetId (string) --The subnet ID used by the connection.
            SecurityGroupIdList (list) --The security group ID list used by the connection.
            (string) --
            AvailabilityZone (string) --The connection's availability zone. This field is deprecated and has no effect.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_crawler(Name=None, Role=None, DatabaseName=None, Description=None, Targets=None, Schedule=None, Classifiers=None, TablePrefix=None, SchemaChangePolicy=None, Configuration=None):
    """
    Updates a crawler. If a crawler is running, you must stop it using StopCrawler before updating it.
    See also: AWS API Documentation
    
    
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
        Configuration='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Name of the new crawler.
            

    :type Role: string
    :param Role: The IAM role (or ARN of an IAM role) used by the new crawler to access customer resources.

    :type DatabaseName: string
    :param DatabaseName: The AWS Glue database where results are stored, such as: arn:aws:daylight:us-east-1::database/sometable/* .

    :type Description: string
    :param Description: A description of the new crawler.

    :type Targets: dict
    :param Targets: A list of targets to crawl.
            S3Targets (list) --Specifies Amazon S3 targets.
            (dict) --Specifies a data store in Amazon S3.
            Path (string) --The path to the Amazon S3 target.
            Exclusions (list) --A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler .
            (string) --
            
            JdbcTargets (list) --Specifies JDBC targets.
            (dict) --Specifies a JDBC data store to crawl.
            ConnectionName (string) --The name of the connection to use to connect to the JDBC target.
            Path (string) --The path of the JDBC target.
            Exclusions (list) --A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler .
            (string) --
            
            

    :type Schedule: string
    :param Schedule: A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .

    :type Classifiers: list
    :param Classifiers: A list of custom classifiers that the user has registered. By default, all classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.
            (string) --
            

    :type TablePrefix: string
    :param TablePrefix: The table prefix used for catalog tables that are created.

    :type SchemaChangePolicy: dict
    :param SchemaChangePolicy: Policy for the crawler's update and deletion behavior.
            UpdateBehavior (string) --The update behavior when the crawler finds a changed schema.
            DeleteBehavior (string) --The deletion behavior when the crawler finds a deleted object.
            

    :type Configuration: string
    :param Configuration: Crawler configuration information. This versioned JSON string allows users to specify aspects of a Crawler's behavior.
            You can use this field to force partitions to inherit metadata such as classification, input format, output format, serde information, and schema from their parent table, rather than detect this information separately for each partition. Use the following JSON string to specify that behavior:
            Example: '{ 'Version': 1.0, 'CrawlerOutput': { 'Partitions': { 'AddOrUpdateBehavior': 'InheritFromTable' } } }'
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_crawler_schedule(CrawlerName=None, Schedule=None):
    """
    Updates the schedule of a crawler using a cron expression.
    See also: AWS API Documentation
    
    
    :example: response = client.update_crawler_schedule(
        CrawlerName='string',
        Schedule='string'
    )
    
    
    :type CrawlerName: string
    :param CrawlerName: [REQUIRED]
            Name of the crawler whose schedule to update.
            

    :type Schedule: string
    :param Schedule: The updated cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_database(CatalogId=None, Name=None, DatabaseInput=None):
    """
    Updates an existing database definition in a Data Catalog.
    See also: AWS API Documentation
    
    
    :example: response = client.update_database(
        CatalogId='string',
        Name='string',
        DatabaseInput={
            'Name': 'string',
            'Description': 'string',
            'LocationUri': 'string',
            'Parameters': {
                'string': 'string'
            }
        }
    )
    
    
    :type CatalogId: string
    :param CatalogId: The ID of the Data Catalog in which the metadata database resides. If none is supplied, the AWS account ID is used by default.

    :type Name: string
    :param Name: [REQUIRED]
            The name of the database to update in the catalog. For Hive compatibility, this is folded to lowercase.
            

    :type DatabaseInput: dict
    :param DatabaseInput: [REQUIRED]
            A DatabaseInput object specifying the new definition of the metadata database in the catalog.
            Name (string) -- [REQUIRED]Name of the database. For Hive compatibility, this is folded to lowercase when it is stored.
            Description (string) --Description of the database
            LocationUri (string) --The location of the database (for example, an HDFS path).
            Parameters (dict) --A list of key-value pairs that define parameters and properties of the database.
            (string) --
            (string) --
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_dev_endpoint(EndpointName=None, PublicKey=None, CustomLibraries=None, UpdateEtlLibraries=None):
    """
    Updates a specified DevEndpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.update_dev_endpoint(
        EndpointName='string',
        PublicKey='string',
        CustomLibraries={
            'ExtraPythonLibsS3Path': 'string',
            'ExtraJarsS3Path': 'string'
        },
        UpdateEtlLibraries=True|False
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]
            The name of the DevEndpoint to be updated.
            

    :type PublicKey: string
    :param PublicKey: The public key for the DevEndpoint to use.

    :type CustomLibraries: dict
    :param CustomLibraries: Custom Python or Java libraries to be loaded in the DevEndpoint.
            ExtraPythonLibsS3Path (string) --Path(s) to one or more Python libraries in an S3 bucket that should be loaded in your DevEndpoint. Multiple values must be complete paths separated by a comma.
            Please note that only pure Python libraries can currently be used on a DevEndpoint. Libraries that rely on C extensions, such as the pandas Python data analysis library, are not yet supported.
            ExtraJarsS3Path (string) --Path to one or more Java Jars in an S3 bucket that should be loaded in your DevEndpoint.
            Please note that only pure Java/Scala libraries can currently be used on a DevEndpoint.
            

    :type UpdateEtlLibraries: boolean
    :param UpdateEtlLibraries: True if the list of custom libraries to be loaded in the development endpoint needs to be updated, or False otherwise.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_job(JobName=None, JobUpdate=None):
    """
    Updates an existing job definition.
    See also: AWS API Documentation
    
    
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
                'ScriptLocation': 'string'
            },
            'DefaultArguments': {
                'string': 'string'
            },
            'Connections': {
                'Connections': [
                    'string',
                ]
            },
            'MaxRetries': 123,
            'AllocatedCapacity': 123,
            'Timeout': 123
        }
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]
            Name of the job definition to update.
            

    :type JobUpdate: dict
    :param JobUpdate: [REQUIRED]
            Specifies the values with which to update the job definition.
            Description (string) --Description of the job being defined.
            LogUri (string) --This field is reserved for future use.
            Role (string) --The name or ARN of the IAM role associated with this job (required).
            ExecutionProperty (dict) --An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job.
            MaxConcurrentRuns (integer) --The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.
            Command (dict) --The JobCommand that executes this job (required).
            Name (string) --The name of the job command: this must be glueetl .
            ScriptLocation (string) --Specifies the S3 path to a script that executes a job (required).
            DefaultArguments (dict) --The default arguments for this job.
            You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
            For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
            For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.
            (string) --
            (string) --
            
            Connections (dict) --The connections used for this job.
            Connections (list) --A list of connections used by the job.
            (string) --
            
            MaxRetries (integer) --The maximum number of times to retry this job if it fails.
            AllocatedCapacity (integer) --The number of AWS Glue data processing units (DPUs) to allocate to this Job. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the AWS Glue pricing page .
            Timeout (integer) --The job timeout in minutes. The default is 2880 minutes (48 hours).
            

    :rtype: dict
    :return: {
        'JobName': 'string'
    }
    
    
    """
    pass

def update_partition(CatalogId=None, DatabaseName=None, TableName=None, PartitionValueList=None, PartitionInput=None):
    """
    Updates a partition.
    See also: AWS API Documentation
    
    
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
                        'Comment': 'string'
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
    :param CatalogId: The ID of the Data Catalog where the partition to be updated resides. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the catalog database in which the table in question resides.
            

    :type TableName: string
    :param TableName: [REQUIRED]
            The name of the table where the partition to be updated is located.
            

    :type PartitionValueList: list
    :param PartitionValueList: [REQUIRED]
            A list of the values defining the partition.
            (string) --
            

    :type PartitionInput: dict
    :param PartitionInput: [REQUIRED]
            The new partition object to which to update the partition.
            Values (list) --The values of the partition.
            (string) --
            LastAccessTime (datetime) --The last time at which the partition was accessed.
            StorageDescriptor (dict) --Provides information about the physical location where the partition is stored.
            Columns (list) --A list of the Columns in the table.
            (dict) --A column in a Table .
            Name (string) -- [REQUIRED]The name of the Column .
            Type (string) --The datatype of data in the Column .
            Comment (string) --Free-form text comment.
            
            Location (string) --The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
            InputFormat (string) --The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.
            OutputFormat (string) --The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.
            Compressed (boolean) --True if the data in the table is compressed, or False if not.
            NumberOfBuckets (integer) --Must be specified if the table contains any dimension columns.
            SerdeInfo (dict) --Serialization/deserialization (SerDe) information.
            Name (string) --Name of the SerDe.
            SerializationLibrary (string) --Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .
            Parameters (dict) --A list of initialization parameters for the SerDe, in key-value form.
            (string) --
            (string) --
            
            BucketColumns (list) --A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
            (string) --
            SortColumns (list) --A list specifying the sort order of each bucket in the table.
            (dict) --Specifies the sort order of a sorted column.
            Column (string) -- [REQUIRED]The name of the column.
            SortOrder (integer) -- [REQUIRED]Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).
            
            Parameters (dict) --User-supplied properties in key-value form.
            (string) --
            (string) --
            
            SkewedInfo (dict) --Information about values that appear very frequently in a column (skewed values).
            SkewedColumnNames (list) --A list of names of columns that contain skewed values.
            (string) --
            SkewedColumnValues (list) --A list of values that appear so frequently as to be considered skewed.
            (string) --
            SkewedColumnValueLocationMaps (dict) --A mapping of skewed values to the columns that contain them.
            (string) --
            (string) --
            
            StoredAsSubDirectories (boolean) --True if the table data is stored in subdirectories, or False if not.
            Parameters (dict) --Partition parameters, in the form of a list of key-value pairs.
            (string) --
            (string) --
            
            LastAnalyzedTime (datetime) --The last time at which column statistics were computed for this partition.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_table(CatalogId=None, DatabaseName=None, TableInput=None, SkipArchive=None):
    """
    Updates a metadata table in the Data Catalog.
    See also: AWS API Documentation
    
    
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
                        'Comment': 'string'
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
                    'Comment': 'string'
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
    :param CatalogId: The ID of the Data Catalog where the table resides. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the catalog database in which the table resides. For Hive compatibility, this name is entirely lowercase.
            

    :type TableInput: dict
    :param TableInput: [REQUIRED]
            An updated TableInput object to define the metadata table in the catalog.
            Name (string) -- [REQUIRED]Name of the table. For Hive compatibility, this is folded to lowercase when it is stored.
            Description (string) --Description of the table.
            Owner (string) --Owner of the table.
            LastAccessTime (datetime) --Last time the table was accessed.
            LastAnalyzedTime (datetime) --Last time column statistics were computed for this table.
            Retention (integer) --Retention time for this table.
            StorageDescriptor (dict) --A storage descriptor containing information about the physical storage of this table.
            Columns (list) --A list of the Columns in the table.
            (dict) --A column in a Table .
            Name (string) -- [REQUIRED]The name of the Column .
            Type (string) --The datatype of data in the Column .
            Comment (string) --Free-form text comment.
            
            Location (string) --The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
            InputFormat (string) --The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.
            OutputFormat (string) --The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.
            Compressed (boolean) --True if the data in the table is compressed, or False if not.
            NumberOfBuckets (integer) --Must be specified if the table contains any dimension columns.
            SerdeInfo (dict) --Serialization/deserialization (SerDe) information.
            Name (string) --Name of the SerDe.
            SerializationLibrary (string) --Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .
            Parameters (dict) --A list of initialization parameters for the SerDe, in key-value form.
            (string) --
            (string) --
            
            BucketColumns (list) --A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
            (string) --
            SortColumns (list) --A list specifying the sort order of each bucket in the table.
            (dict) --Specifies the sort order of a sorted column.
            Column (string) -- [REQUIRED]The name of the column.
            SortOrder (integer) -- [REQUIRED]Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).
            
            Parameters (dict) --User-supplied properties in key-value form.
            (string) --
            (string) --
            
            SkewedInfo (dict) --Information about values that appear very frequently in a column (skewed values).
            SkewedColumnNames (list) --A list of names of columns that contain skewed values.
            (string) --
            SkewedColumnValues (list) --A list of values that appear so frequently as to be considered skewed.
            (string) --
            SkewedColumnValueLocationMaps (dict) --A mapping of skewed values to the columns that contain them.
            (string) --
            (string) --
            
            StoredAsSubDirectories (boolean) --True if the table data is stored in subdirectories, or False if not.
            PartitionKeys (list) --A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
            (dict) --A column in a Table .
            Name (string) -- [REQUIRED]The name of the Column .
            Type (string) --The datatype of data in the Column .
            Comment (string) --Free-form text comment.
            
            ViewOriginalText (string) --If the table is a view, the original text of the view; otherwise null .
            ViewExpandedText (string) --If the table is a view, the expanded text of the view; otherwise null .
            TableType (string) --The type of this table (EXTERNAL_TABLE , VIRTUAL_VIEW , etc.).
            Parameters (dict) --Properties associated with this table, as a list of key-value pairs.
            (string) --
            (string) --
            
            

    :type SkipArchive: boolean
    :param SkipArchive: By default, UpdateTable always creates an archived version of the table before updating it. If skipArchive is set to true, however, UpdateTable does not create the archived version.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_trigger(Name=None, TriggerUpdate=None):
    """
    Updates a trigger definition.
    See also: AWS API Documentation
    
    
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
                    'Timeout': 123
                },
            ],
            'Predicate': {
                'Logical': 'AND'|'ANY',
                'Conditions': [
                    {
                        'LogicalOperator': 'EQUALS',
                        'JobName': 'string',
                        'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT'
                    },
                ]
            }
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the trigger to update.
            

    :type TriggerUpdate: dict
    :param TriggerUpdate: [REQUIRED]
            The new values with which to update the trigger.
            Name (string) --Reserved for future use.
            Description (string) --A description of this trigger.
            Schedule (string) --A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers . For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *) .
            Actions (list) --The actions initiated by this trigger.
            (dict) --Defines an action to be initiated by a trigger.
            JobName (string) --The name of a job to be executed.
            Arguments (dict) --Arguments to be passed to the job.
            You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
            For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
            For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.
            (string) --
            (string) --
            
            Timeout (integer) --The job run timeout in minutes. It overrides the timeout value of the job.
            
            Predicate (dict) --The predicate of this trigger, which defines when it will fire.
            Logical (string) --Optional field if only one condition is listed. If multiple conditions are listed, then this field is required.
            Conditions (list) --A list of the conditions that determine when the trigger will fire.
            (dict) --Defines a condition under which a trigger fires.
            LogicalOperator (string) --A logical operator.
            JobName (string) --The name of the Job to whose JobRuns this condition applies and on which this trigger waits.
            State (string) --The condition state. Currently, the values supported are SUCCEEDED, STOPPED, TIMEOUT and FAILED.
            
            
            

    :rtype: dict
    :return: {
        'Trigger': {
            'Name': 'string',
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
                    'Timeout': 123
                },
            ],
            'Predicate': {
                'Logical': 'AND'|'ANY',
                'Conditions': [
                    {
                        'LogicalOperator': 'EQUALS',
                        'JobName': 'string',
                        'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'|'FAILED'|'TIMEOUT'
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
    :param CatalogId: The ID of the Data Catalog where the function to be updated is located. If none is supplied, the AWS account ID is used by default.

    :type DatabaseName: string
    :param DatabaseName: [REQUIRED]
            The name of the catalog database where the function to be updated is located.
            

    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the function.
            

    :type FunctionInput: dict
    :param FunctionInput: [REQUIRED]
            A FunctionInput object that re-defines the function in the Data Catalog.
            FunctionName (string) --The name of the function.
            ClassName (string) --The Java class that contains the function code.
            OwnerName (string) --The owner of the function.
            OwnerType (string) --The owner type.
            ResourceUris (list) --The resource URIs for the function.
            (dict) --URIs for function resources.
            ResourceType (string) --The type of the resource.
            Uri (string) --The URI for accessing the resource.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

