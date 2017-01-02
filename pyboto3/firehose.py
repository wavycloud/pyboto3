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

def create_delivery_stream(DeliveryStreamName=None, S3DestinationConfiguration=None, ExtendedS3DestinationConfiguration=None, RedshiftDestinationConfiguration=None, ElasticsearchDestinationConfiguration=None):
    """
    Creates a delivery stream.
    By default, you can create up to 20 delivery streams per region.
    This is an asynchronous operation that immediately returns. The initial status of the delivery stream is CREATING . After the delivery stream is created, its status is ACTIVE and it now accepts data. Attempts to send data to a delivery stream that is not in the ACTIVE state cause an exception. To check the state of a delivery stream, use  DescribeDeliveryStream .
    A delivery stream is configured with a single destination: Amazon S3, Amazon Elasticsearch Service, or Amazon Redshift. You must specify only one of the following destination configuration parameters: ExtendedS3DestinationConfiguration , S3DestinationConfiguration , ElasticsearchDestinationConfiguration , or RedshiftDestinationConfiguration .
    When you specify S3DestinationConfiguration , you can also provide the following optional values: BufferingHints , EncryptionConfiguration , and CompressionFormat . By default, if no BufferingHints value is provided, Firehose buffers data up to 5 MB or for 5 minutes, whichever condition is satisfied first. Note that BufferingHints is a hint, so there are some cases where the service cannot adhere to these conditions strictly; for example, record boundaries are such that the size is a little over or under the configured buffering size. By default, no encryption is performed. We strongly recommend that you enable encryption to ensure secure data storage in Amazon S3.
    A few notes about Amazon Redshift as a destination:
    Firehose assumes the IAM role that is configured as part of the destination. The role should allow the Firehose principal to assume the role, and the role should have permissions that allows the service to deliver the data. For more information, see Amazon S3 Bucket Access in the Amazon Kinesis Firehose Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_delivery_stream(
        DeliveryStreamName='string',
        S3DestinationConfiguration={
            'RoleARN': 'string',
            'BucketARN': 'string',
            'Prefix': 'string',
            'BufferingHints': {
                'SizeInMBs': 123,
                'IntervalInSeconds': 123
            },
            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
            'EncryptionConfiguration': {
                'NoEncryptionConfig': 'NoEncryption',
                'KMSEncryptionConfig': {
                    'AWSKMSKeyARN': 'string'
                }
            },
            'CloudWatchLoggingOptions': {
                'Enabled': True|False,
                'LogGroupName': 'string',
                'LogStreamName': 'string'
            }
        },
        ExtendedS3DestinationConfiguration={
            'RoleARN': 'string',
            'BucketARN': 'string',
            'Prefix': 'string',
            'BufferingHints': {
                'SizeInMBs': 123,
                'IntervalInSeconds': 123
            },
            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
            'EncryptionConfiguration': {
                'NoEncryptionConfig': 'NoEncryption',
                'KMSEncryptionConfig': {
                    'AWSKMSKeyARN': 'string'
                }
            },
            'CloudWatchLoggingOptions': {
                'Enabled': True|False,
                'LogGroupName': 'string',
                'LogStreamName': 'string'
            },
            'ProcessingConfiguration': {
                'Enabled': True|False,
                'Processors': [
                    {
                        'Type': 'Lambda',
                        'Parameters': [
                            {
                                'ParameterName': 'LambdaArn'|'NumberOfRetries',
                                'ParameterValue': 'string'
                            },
                        ]
                    },
                ]
            },
            'S3BackupMode': 'Disabled'|'Enabled',
            'S3BackupConfiguration': {
                'RoleARN': 'string',
                'BucketARN': 'string',
                'Prefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
                'EncryptionConfiguration': {
                    'NoEncryptionConfig': 'NoEncryption',
                    'KMSEncryptionConfig': {
                        'AWSKMSKeyARN': 'string'
                    }
                },
                'CloudWatchLoggingOptions': {
                    'Enabled': True|False,
                    'LogGroupName': 'string',
                    'LogStreamName': 'string'
                }
            }
        },
        RedshiftDestinationConfiguration={
            'RoleARN': 'string',
            'ClusterJDBCURL': 'string',
            'CopyCommand': {
                'DataTableName': 'string',
                'DataTableColumns': 'string',
                'CopyOptions': 'string'
            },
            'Username': 'string',
            'Password': 'string',
            'RetryOptions': {
                'DurationInSeconds': 123
            },
            'S3Configuration': {
                'RoleARN': 'string',
                'BucketARN': 'string',
                'Prefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
                'EncryptionConfiguration': {
                    'NoEncryptionConfig': 'NoEncryption',
                    'KMSEncryptionConfig': {
                        'AWSKMSKeyARN': 'string'
                    }
                },
                'CloudWatchLoggingOptions': {
                    'Enabled': True|False,
                    'LogGroupName': 'string',
                    'LogStreamName': 'string'
                }
            },
            'ProcessingConfiguration': {
                'Enabled': True|False,
                'Processors': [
                    {
                        'Type': 'Lambda',
                        'Parameters': [
                            {
                                'ParameterName': 'LambdaArn'|'NumberOfRetries',
                                'ParameterValue': 'string'
                            },
                        ]
                    },
                ]
            },
            'S3BackupMode': 'Disabled'|'Enabled',
            'S3BackupConfiguration': {
                'RoleARN': 'string',
                'BucketARN': 'string',
                'Prefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
                'EncryptionConfiguration': {
                    'NoEncryptionConfig': 'NoEncryption',
                    'KMSEncryptionConfig': {
                        'AWSKMSKeyARN': 'string'
                    }
                },
                'CloudWatchLoggingOptions': {
                    'Enabled': True|False,
                    'LogGroupName': 'string',
                    'LogStreamName': 'string'
                }
            },
            'CloudWatchLoggingOptions': {
                'Enabled': True|False,
                'LogGroupName': 'string',
                'LogStreamName': 'string'
            }
        },
        ElasticsearchDestinationConfiguration={
            'RoleARN': 'string',
            'DomainARN': 'string',
            'IndexName': 'string',
            'TypeName': 'string',
            'IndexRotationPeriod': 'NoRotation'|'OneHour'|'OneDay'|'OneWeek'|'OneMonth',
            'BufferingHints': {
                'IntervalInSeconds': 123,
                'SizeInMBs': 123
            },
            'RetryOptions': {
                'DurationInSeconds': 123
            },
            'S3BackupMode': 'FailedDocumentsOnly'|'AllDocuments',
            'S3Configuration': {
                'RoleARN': 'string',
                'BucketARN': 'string',
                'Prefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
                'EncryptionConfiguration': {
                    'NoEncryptionConfig': 'NoEncryption',
                    'KMSEncryptionConfig': {
                        'AWSKMSKeyARN': 'string'
                    }
                },
                'CloudWatchLoggingOptions': {
                    'Enabled': True|False,
                    'LogGroupName': 'string',
                    'LogStreamName': 'string'
                }
            },
            'ProcessingConfiguration': {
                'Enabled': True|False,
                'Processors': [
                    {
                        'Type': 'Lambda',
                        'Parameters': [
                            {
                                'ParameterName': 'LambdaArn'|'NumberOfRetries',
                                'ParameterValue': 'string'
                            },
                        ]
                    },
                ]
            },
            'CloudWatchLoggingOptions': {
                'Enabled': True|False,
                'LogGroupName': 'string',
                'LogStreamName': 'string'
            }
        }
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]
            The name of the delivery stream. This name must be unique per AWS account in the same region. You can have multiple delivery streams with the same name if they are in different accounts or different regions.
            

    :type S3DestinationConfiguration: dict
    :param S3DestinationConfiguration: [Deprecated] The destination in Amazon S3. You can specify only one destination.
            RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
            BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            
            

    :type ExtendedS3DestinationConfiguration: dict
    :param ExtendedS3DestinationConfiguration: The destination in Amazon S3. You can specify only one destination.
            RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
            BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            ProcessingConfiguration (dict) --The data processing configuration.
            Enabled (boolean) --Enables or disables data processing.
            Processors (list) --The data processors.
            (dict) --Describes a data processor.
            Type (string) -- [REQUIRED]The type of processor.
            Parameters (list) --The processor parameters.
            (dict) --Describes the processor parameter.
            ParameterName (string) -- [REQUIRED]The name of the parameter.
            ParameterValue (string) -- [REQUIRED]The parameter value.
            
            
            S3BackupMode (string) --The Amazon S3 backup mode.
            S3BackupConfiguration (dict) --The configuration for backup in Amazon S3.
            RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
            BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            
            

    :type RedshiftDestinationConfiguration: dict
    :param RedshiftDestinationConfiguration: The destination in Amazon Redshift. You can specify only one destination.
            RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
            ClusterJDBCURL (string) -- [REQUIRED]The database connection string.
            CopyCommand (dict) -- [REQUIRED]The COPY command.
            DataTableName (string) -- [REQUIRED]The name of the target table. The table must already exist in the database.
            DataTableColumns (string) --A comma-separated list of column names.
            CopyOptions (string) --Optional parameters to use with the Amazon Redshift COPY command. For more information, see the 'Optional Parameters' section of Amazon Redshift COPY command . Some possible examples that would apply to Firehose are as follows:
            delimiter '\t' lzop; - fields are delimited with 't' (TAB character) and compressed using lzop.delimiter '| - fields are delimited with '|' (this is the default delimiter).
            delimiter '|' escape - the delimiter should be escaped.
            fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6' - fields are fixed width in the source, with each width specified after every column in the table.
            JSON 's3://mybucket/jsonpaths.txt' - data is in JSON format, and the path specified is the format of the data.
            For more examples, see Amazon Redshift COPY command examples .
            Username (string) -- [REQUIRED]The name of the user.
            Password (string) -- [REQUIRED]The user password.
            RetryOptions (dict) --The retry behavior in the event that Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).
            DurationInSeconds (integer) --The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value.
            S3Configuration (dict) -- [REQUIRED]The configuration for the intermediate Amazon S3 location from which Amazon Redshift obtains data. Restrictions are described in the topic for CreateDeliveryStream .
            The compression formats SNAPPY or ZIP cannot be specified in RedshiftDestinationConfiguration.S3Configuration because the Amazon Redshift COPY operation that reads from the S3 bucket doesn't support these compression formats.
            RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
            BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            
            ProcessingConfiguration (dict) --The data processing configuration.
            Enabled (boolean) --Enables or disables data processing.
            Processors (list) --The data processors.
            (dict) --Describes a data processor.
            Type (string) -- [REQUIRED]The type of processor.
            Parameters (list) --The processor parameters.
            (dict) --Describes the processor parameter.
            ParameterName (string) -- [REQUIRED]The name of the parameter.
            ParameterValue (string) -- [REQUIRED]The parameter value.
            
            
            S3BackupMode (string) --The Amazon S3 backup mode.
            S3BackupConfiguration (dict) --The configuration for backup in Amazon S3.
            RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
            BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            
            

    :type ElasticsearchDestinationConfiguration: dict
    :param ElasticsearchDestinationConfiguration: The destination in Amazon ES. You can specify only one destination.
            RoleARN (string) -- [REQUIRED]The ARN of the IAM role to be assumed by Firehose for calling the Amazon ES Configuration API and for indexing documents. For more information, see Amazon S3 Bucket Access .
            DomainARN (string) -- [REQUIRED]The ARN of the Amazon ES domain. The IAM role must have permissions for DescribeElasticsearchDomain , DescribeElasticsearchDomains , and DescribeElasticsearchDomainConfig after assuming the role specified in RoleARN .
            IndexName (string) -- [REQUIRED]The Elasticsearch index name.
            TypeName (string) -- [REQUIRED]The Elasticsearch type name.
            IndexRotationPeriod (string) --The Elasticsearch index rotation period. Index rotation appends a timestamp to the IndexName to facilitate expiration of old data. For more information, see Index Rotation for Amazon Elasticsearch Service Destination . The default value is OneDay .
            BufferingHints (dict) --The buffering options. If no value is specified, the default values for ElasticsearchBufferingHints are used.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
            RetryOptions (dict) --The retry behavior in the event that Firehose is unable to deliver documents to Amazon ES. The default value is 300 (5 minutes).
            DurationInSeconds (integer) --After an initial failure to deliver to Amazon ES, the total amount of time during which Firehose re-attempts delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.
            S3BackupMode (string) --Defines how documents should be delivered to Amazon S3. When set to FailedDocumentsOnly, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with elasticsearch-failed/ appended to the key prefix. When set to AllDocuments, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with elasticsearch-failed/ appended to the prefix. For more information, see Amazon S3 Backup for Amazon Elasticsearch Service Destination . Default value is FailedDocumentsOnly.
            S3Configuration (dict) -- [REQUIRED]The configuration for the intermediate Amazon S3 location from which Amazon ES obtains data.
            RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
            BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            
            ProcessingConfiguration (dict) --The data processing configuration.
            Enabled (boolean) --Enables or disables data processing.
            Processors (list) --The data processors.
            (dict) --Describes a data processor.
            Type (string) -- [REQUIRED]The type of processor.
            Parameters (list) --The processor parameters.
            (dict) --Describes the processor parameter.
            ParameterName (string) -- [REQUIRED]The name of the parameter.
            ParameterValue (string) -- [REQUIRED]The parameter value.
            
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            
            

    :rtype: dict
    :return: {
        'DeliveryStreamARN': 'string'
    }
    
    
    :returns: 
    DeliveryStreamName (string) -- [REQUIRED]
    The name of the delivery stream. This name must be unique per AWS account in the same region. You can have multiple delivery streams with the same name if they are in different accounts or different regions.
    
    S3DestinationConfiguration (dict) -- [Deprecated] The destination in Amazon S3. You can specify only one destination.
    
    RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
    
    BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
    
    Prefix (string) --The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
    
    BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
    
    
    
    CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
    The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
    
    EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
    
    NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
    
    KMSEncryptionConfig (dict) --The encryption key.
    
    AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
    
    Enabled (boolean) --Enables or disables CloudWatch logging.
    
    LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
    
    LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
    
    
    
    
    
    ExtendedS3DestinationConfiguration (dict) -- The destination in Amazon S3. You can specify only one destination.
    
    RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
    
    BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
    
    Prefix (string) --The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
    
    BufferingHints (dict) --The buffering option.
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
    
    
    
    CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED.
    
    EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
    
    NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
    
    KMSEncryptionConfig (dict) --The encryption key.
    
    AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
    
    Enabled (boolean) --Enables or disables CloudWatch logging.
    
    LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
    
    LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
    
    
    
    ProcessingConfiguration (dict) --The data processing configuration.
    
    Enabled (boolean) --Enables or disables data processing.
    
    Processors (list) --The data processors.
    
    (dict) --Describes a data processor.
    
    Type (string) -- [REQUIRED]The type of processor.
    
    Parameters (list) --The processor parameters.
    
    (dict) --Describes the processor parameter.
    
    ParameterName (string) -- [REQUIRED]The name of the parameter.
    
    ParameterValue (string) -- [REQUIRED]The parameter value.
    
    
    
    
    
    
    
    
    
    
    
    S3BackupMode (string) --The Amazon S3 backup mode.
    
    S3BackupConfiguration (dict) --The configuration for backup in Amazon S3.
    
    RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
    
    BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
    
    Prefix (string) --The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
    
    BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
    
    
    
    CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
    The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
    
    EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
    
    NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
    
    KMSEncryptionConfig (dict) --The encryption key.
    
    AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
    
    Enabled (boolean) --Enables or disables CloudWatch logging.
    
    LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
    
    LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
    
    
    
    
    
    
    
    RedshiftDestinationConfiguration (dict) -- The destination in Amazon Redshift. You can specify only one destination.
    
    RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
    
    ClusterJDBCURL (string) -- [REQUIRED]The database connection string.
    
    CopyCommand (dict) -- [REQUIRED]The COPY command.
    
    DataTableName (string) -- [REQUIRED]The name of the target table. The table must already exist in the database.
    
    DataTableColumns (string) --A comma-separated list of column names.
    
    CopyOptions (string) --Optional parameters to use with the Amazon Redshift COPY command. For more information, see the "Optional Parameters" section of Amazon Redshift COPY command . Some possible examples that would apply to Firehose are as follows:
    
    delimiter '\t' lzop; - fields are delimited with "t" (TAB character) and compressed using lzop.delimiter '| - fields are delimited with "|" (this is the default delimiter).
    delimiter '|' escape - the delimiter should be escaped.
    fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6' - fields are fixed width in the source, with each width specified after every column in the table.
    JSON 's3://mybucket/jsonpaths.txt' - data is in JSON format, and the path specified is the format of the data.
    
    For more examples, see Amazon Redshift COPY command examples .
    
    
    
    Username (string) -- [REQUIRED]The name of the user.
    
    Password (string) -- [REQUIRED]The user password.
    
    RetryOptions (dict) --The retry behavior in the event that Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).
    
    DurationInSeconds (integer) --The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value.
    
    
    
    S3Configuration (dict) -- [REQUIRED]The configuration for the intermediate Amazon S3 location from which Amazon Redshift obtains data. Restrictions are described in the topic for  CreateDeliveryStream .
    The compression formats SNAPPY or ZIP cannot be specified in RedshiftDestinationConfiguration.S3Configuration because the Amazon Redshift COPY operation that reads from the S3 bucket doesn't support these compression formats.
    
    RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
    
    BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
    
    Prefix (string) --The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
    
    BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
    
    
    
    CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
    The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
    
    EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
    
    NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
    
    KMSEncryptionConfig (dict) --The encryption key.
    
    AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
    
    Enabled (boolean) --Enables or disables CloudWatch logging.
    
    LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
    
    LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
    
    
    
    
    
    ProcessingConfiguration (dict) --The data processing configuration.
    
    Enabled (boolean) --Enables or disables data processing.
    
    Processors (list) --The data processors.
    
    (dict) --Describes a data processor.
    
    Type (string) -- [REQUIRED]The type of processor.
    
    Parameters (list) --The processor parameters.
    
    (dict) --Describes the processor parameter.
    
    ParameterName (string) -- [REQUIRED]The name of the parameter.
    
    ParameterValue (string) -- [REQUIRED]The parameter value.
    
    
    
    
    
    
    
    
    
    
    
    S3BackupMode (string) --The Amazon S3 backup mode.
    
    S3BackupConfiguration (dict) --The configuration for backup in Amazon S3.
    
    RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
    
    BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
    
    Prefix (string) --The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
    
    BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
    
    
    
    CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
    The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
    
    EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
    
    NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
    
    KMSEncryptionConfig (dict) --The encryption key.
    
    AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
    
    Enabled (boolean) --Enables or disables CloudWatch logging.
    
    LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
    
    LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
    
    Enabled (boolean) --Enables or disables CloudWatch logging.
    
    LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
    
    LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
    
    
    
    
    
    ElasticsearchDestinationConfiguration (dict) -- The destination in Amazon ES. You can specify only one destination.
    
    RoleARN (string) -- [REQUIRED]The ARN of the IAM role to be assumed by Firehose for calling the Amazon ES Configuration API and for indexing documents. For more information, see Amazon S3 Bucket Access .
    
    DomainARN (string) -- [REQUIRED]The ARN of the Amazon ES domain. The IAM role must have permissions for DescribeElasticsearchDomain , DescribeElasticsearchDomains , and DescribeElasticsearchDomainConfig after assuming the role specified in RoleARN .
    
    IndexName (string) -- [REQUIRED]The Elasticsearch index name.
    
    TypeName (string) -- [REQUIRED]The Elasticsearch type name.
    
    IndexRotationPeriod (string) --The Elasticsearch index rotation period. Index rotation appends a timestamp to the IndexName to facilitate expiration of old data. For more information, see Index Rotation for Amazon Elasticsearch Service Destination . The default value is OneDay .
    
    BufferingHints (dict) --The buffering options. If no value is specified, the default values for ElasticsearchBufferingHints are used.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
    
    
    
    RetryOptions (dict) --The retry behavior in the event that Firehose is unable to deliver documents to Amazon ES. The default value is 300 (5 minutes).
    
    DurationInSeconds (integer) --After an initial failure to deliver to Amazon ES, the total amount of time during which Firehose re-attempts delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.
    
    
    
    S3BackupMode (string) --Defines how documents should be delivered to Amazon S3. When set to FailedDocumentsOnly, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with elasticsearch-failed/ appended to the key prefix. When set to AllDocuments, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with elasticsearch-failed/ appended to the prefix. For more information, see Amazon S3 Backup for Amazon Elasticsearch Service Destination . Default value is FailedDocumentsOnly.
    
    S3Configuration (dict) -- [REQUIRED]The configuration for the intermediate Amazon S3 location from which Amazon ES obtains data.
    
    RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
    
    BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
    
    Prefix (string) --The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
    
    BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
    
    
    
    CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
    The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
    
    EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
    
    NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
    
    KMSEncryptionConfig (dict) --The encryption key.
    
    AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
    
    Enabled (boolean) --Enables or disables CloudWatch logging.
    
    LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
    
    LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
    
    
    
    
    
    ProcessingConfiguration (dict) --The data processing configuration.
    
    Enabled (boolean) --Enables or disables data processing.
    
    Processors (list) --The data processors.
    
    (dict) --Describes a data processor.
    
    Type (string) -- [REQUIRED]The type of processor.
    
    Parameters (list) --The processor parameters.
    
    (dict) --Describes the processor parameter.
    
    ParameterName (string) -- [REQUIRED]The name of the parameter.
    
    ParameterValue (string) -- [REQUIRED]The parameter value.
    
    
    
    
    
    
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
    
    Enabled (boolean) --Enables or disables CloudWatch logging.
    
    LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
    
    LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
    
    
    
    
    
    
    """
    pass

def delete_delivery_stream(DeliveryStreamName=None):
    """
    Deletes a delivery stream and its data.
    You can delete a delivery stream only if it is in ACTIVE or DELETING state, and not in the CREATING state. While the deletion request is in process, the delivery stream is in the DELETING state.
    To check the state of a delivery stream, use  DescribeDeliveryStream .
    While the delivery stream is DELETING state, the service may continue to accept the records, but the service doesn't make any guarantees with respect to delivering the data. Therefore, as a best practice, you should first stop any applications that are sending records before deleting a delivery stream.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_delivery_stream(
        DeliveryStreamName='string'
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]
            The name of the delivery stream.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_delivery_stream(DeliveryStreamName=None, Limit=None, ExclusiveStartDestinationId=None):
    """
    Describes the specified delivery stream and gets the status. For example, after your delivery stream is created, call  DescribeDeliveryStream to see if the delivery stream is ACTIVE and therefore ready for data to be sent to it.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_delivery_stream(
        DeliveryStreamName='string',
        Limit=123,
        ExclusiveStartDestinationId='string'
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]
            The name of the delivery stream.
            

    :type Limit: integer
    :param Limit: The limit on the number of destinations to return. Currently, you can have one destination per delivery stream.

    :type ExclusiveStartDestinationId: string
    :param ExclusiveStartDestinationId: The ID of the destination to start returning the destination information. Currently Firehose supports one destination per delivery stream.

    :rtype: dict
    :return: {
        'DeliveryStreamDescription': {
            'DeliveryStreamName': 'string',
            'DeliveryStreamARN': 'string',
            'DeliveryStreamStatus': 'CREATING'|'DELETING'|'ACTIVE',
            'VersionId': 'string',
            'CreateTimestamp': datetime(2015, 1, 1),
            'LastUpdateTimestamp': datetime(2015, 1, 1),
            'Destinations': [
                {
                    'DestinationId': 'string',
                    'S3DestinationDescription': {
                        'RoleARN': 'string',
                        'BucketARN': 'string',
                        'Prefix': 'string',
                        'BufferingHints': {
                            'SizeInMBs': 123,
                            'IntervalInSeconds': 123
                        },
                        'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
                        'EncryptionConfiguration': {
                            'NoEncryptionConfig': 'NoEncryption',
                            'KMSEncryptionConfig': {
                                'AWSKMSKeyARN': 'string'
                            }
                        },
                        'CloudWatchLoggingOptions': {
                            'Enabled': True|False,
                            'LogGroupName': 'string',
                            'LogStreamName': 'string'
                        }
                    },
                    'ExtendedS3DestinationDescription': {
                        'RoleARN': 'string',
                        'BucketARN': 'string',
                        'Prefix': 'string',
                        'BufferingHints': {
                            'SizeInMBs': 123,
                            'IntervalInSeconds': 123
                        },
                        'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
                        'EncryptionConfiguration': {
                            'NoEncryptionConfig': 'NoEncryption',
                            'KMSEncryptionConfig': {
                                'AWSKMSKeyARN': 'string'
                            }
                        },
                        'CloudWatchLoggingOptions': {
                            'Enabled': True|False,
                            'LogGroupName': 'string',
                            'LogStreamName': 'string'
                        },
                        'ProcessingConfiguration': {
                            'Enabled': True|False,
                            'Processors': [
                                {
                                    'Type': 'Lambda',
                                    'Parameters': [
                                        {
                                            'ParameterName': 'LambdaArn'|'NumberOfRetries',
                                            'ParameterValue': 'string'
                                        },
                                    ]
                                },
                            ]
                        },
                        'S3BackupMode': 'Disabled'|'Enabled',
                        'S3BackupDescription': {
                            'RoleARN': 'string',
                            'BucketARN': 'string',
                            'Prefix': 'string',
                            'BufferingHints': {
                                'SizeInMBs': 123,
                                'IntervalInSeconds': 123
                            },
                            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
                            'EncryptionConfiguration': {
                                'NoEncryptionConfig': 'NoEncryption',
                                'KMSEncryptionConfig': {
                                    'AWSKMSKeyARN': 'string'
                                }
                            },
                            'CloudWatchLoggingOptions': {
                                'Enabled': True|False,
                                'LogGroupName': 'string',
                                'LogStreamName': 'string'
                            }
                        }
                    },
                    'RedshiftDestinationDescription': {
                        'RoleARN': 'string',
                        'ClusterJDBCURL': 'string',
                        'CopyCommand': {
                            'DataTableName': 'string',
                            'DataTableColumns': 'string',
                            'CopyOptions': 'string'
                        },
                        'Username': 'string',
                        'RetryOptions': {
                            'DurationInSeconds': 123
                        },
                        'S3DestinationDescription': {
                            'RoleARN': 'string',
                            'BucketARN': 'string',
                            'Prefix': 'string',
                            'BufferingHints': {
                                'SizeInMBs': 123,
                                'IntervalInSeconds': 123
                            },
                            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
                            'EncryptionConfiguration': {
                                'NoEncryptionConfig': 'NoEncryption',
                                'KMSEncryptionConfig': {
                                    'AWSKMSKeyARN': 'string'
                                }
                            },
                            'CloudWatchLoggingOptions': {
                                'Enabled': True|False,
                                'LogGroupName': 'string',
                                'LogStreamName': 'string'
                            }
                        },
                        'ProcessingConfiguration': {
                            'Enabled': True|False,
                            'Processors': [
                                {
                                    'Type': 'Lambda',
                                    'Parameters': [
                                        {
                                            'ParameterName': 'LambdaArn'|'NumberOfRetries',
                                            'ParameterValue': 'string'
                                        },
                                    ]
                                },
                            ]
                        },
                        'S3BackupMode': 'Disabled'|'Enabled',
                        'S3BackupDescription': {
                            'RoleARN': 'string',
                            'BucketARN': 'string',
                            'Prefix': 'string',
                            'BufferingHints': {
                                'SizeInMBs': 123,
                                'IntervalInSeconds': 123
                            },
                            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
                            'EncryptionConfiguration': {
                                'NoEncryptionConfig': 'NoEncryption',
                                'KMSEncryptionConfig': {
                                    'AWSKMSKeyARN': 'string'
                                }
                            },
                            'CloudWatchLoggingOptions': {
                                'Enabled': True|False,
                                'LogGroupName': 'string',
                                'LogStreamName': 'string'
                            }
                        },
                        'CloudWatchLoggingOptions': {
                            'Enabled': True|False,
                            'LogGroupName': 'string',
                            'LogStreamName': 'string'
                        }
                    },
                    'ElasticsearchDestinationDescription': {
                        'RoleARN': 'string',
                        'DomainARN': 'string',
                        'IndexName': 'string',
                        'TypeName': 'string',
                        'IndexRotationPeriod': 'NoRotation'|'OneHour'|'OneDay'|'OneWeek'|'OneMonth',
                        'BufferingHints': {
                            'IntervalInSeconds': 123,
                            'SizeInMBs': 123
                        },
                        'RetryOptions': {
                            'DurationInSeconds': 123
                        },
                        'S3BackupMode': 'FailedDocumentsOnly'|'AllDocuments',
                        'S3DestinationDescription': {
                            'RoleARN': 'string',
                            'BucketARN': 'string',
                            'Prefix': 'string',
                            'BufferingHints': {
                                'SizeInMBs': 123,
                                'IntervalInSeconds': 123
                            },
                            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
                            'EncryptionConfiguration': {
                                'NoEncryptionConfig': 'NoEncryption',
                                'KMSEncryptionConfig': {
                                    'AWSKMSKeyARN': 'string'
                                }
                            },
                            'CloudWatchLoggingOptions': {
                                'Enabled': True|False,
                                'LogGroupName': 'string',
                                'LogStreamName': 'string'
                            }
                        },
                        'ProcessingConfiguration': {
                            'Enabled': True|False,
                            'Processors': [
                                {
                                    'Type': 'Lambda',
                                    'Parameters': [
                                        {
                                            'ParameterName': 'LambdaArn'|'NumberOfRetries',
                                            'ParameterValue': 'string'
                                        },
                                    ]
                                },
                            ]
                        },
                        'CloudWatchLoggingOptions': {
                            'Enabled': True|False,
                            'LogGroupName': 'string',
                            'LogStreamName': 'string'
                        }
                    }
                },
            ],
            'HasMoreDestinations': True|False
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

def get_waiter():
    """
    
    """
    pass

def list_delivery_streams(Limit=None, ExclusiveStartDeliveryStreamName=None):
    """
    Lists your delivery streams.
    The number of delivery streams might be too large to return using a single call to  ListDeliveryStreams . You can limit the number of delivery streams returned, using the Limit parameter. To determine whether there are more delivery streams to list, check the value of HasMoreDeliveryStreams in the output. If there are more delivery streams to list, you can request them by specifying the name of the last delivery stream returned in the call in the ExclusiveStartDeliveryStreamName parameter of a subsequent call.
    See also: AWS API Documentation
    
    
    :example: response = client.list_delivery_streams(
        Limit=123,
        ExclusiveStartDeliveryStreamName='string'
    )
    
    
    :type Limit: integer
    :param Limit: The maximum number of delivery streams to list.

    :type ExclusiveStartDeliveryStreamName: string
    :param ExclusiveStartDeliveryStreamName: The name of the delivery stream to start the list with.

    :rtype: dict
    :return: {
        'DeliveryStreamNames': [
            'string',
        ],
        'HasMoreDeliveryStreams': True|False
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_record(DeliveryStreamName=None, Record=None):
    """
    Writes a single data record into an Amazon Kinesis Firehose delivery stream. To write multiple data records into a delivery stream, use  PutRecordBatch . Applications using these operations are referred to as producers.
    By default, each delivery stream can take in up to 2,000 transactions per second, 5,000 records per second, or 5 MB per second. Note that if you use  PutRecord and  PutRecordBatch , the limits are an aggregate across these two operations for each delivery stream. For more information about limits and how to request an increase, see Amazon Kinesis Firehose Limits .
    You must specify the name of the delivery stream and the data record when using  PutRecord . The data record consists of a data blob that can be up to 1,000 KB in size, and any kind of data, for example, a segment from a log file, geographic location data, web site clickstream data, etc.
    Firehose buffers records before delivering them to the destination. To disambiguate the data blobs at the destination, a common solution is to use delimiters in the data, such as a newline (\n ) or some other character unique within the data. This allows the consumer application(s) to parse individual data items when reading the data from the destination.
    The  PutRecord operation returns a RecordId , which is a unique string assigned to each record. Producer applications can use this ID for purposes such as auditability and investigation.
    If the  PutRecord operation throws a ServiceUnavailableException , back off and retry. If the exception persists, it is possible that the throughput limits have been exceeded for the delivery stream.
    Data records sent to Firehose are stored for 24 hours from the time they are added to a delivery stream as it attempts to send the records to the destination. If the destination is unreachable for more than 24 hours, the data is no longer available.
    See also: AWS API Documentation
    
    
    :example: response = client.put_record(
        DeliveryStreamName='string',
        Record={
            'Data': b'bytes'
        }
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]
            The name of the delivery stream.
            

    :type Record: dict
    :param Record: [REQUIRED]
            The record.
            Data (bytes) -- [REQUIRED]The data blob, which is base64-encoded when the blob is serialized. The maximum size of the data blob, before base64-encoding, is 1,000 KB.
            

    :rtype: dict
    :return: {
        'RecordId': 'string'
    }
    
    
    """
    pass

def put_record_batch(DeliveryStreamName=None, Records=None):
    """
    Writes multiple data records into a delivery stream in a single call, which can achieve higher throughput per producer than when writing single records. To write single data records into a delivery stream, use  PutRecord . Applications using these operations are referred to as producers.
    By default, each delivery stream can take in up to 2,000 transactions per second, 5,000 records per second, or 5 MB per second. Note that if you use  PutRecord and  PutRecordBatch , the limits are an aggregate across these two operations for each delivery stream. For more information about limits, see Amazon Kinesis Firehose Limits .
    Each  PutRecordBatch request supports up to 500 records. Each record in the request can be as large as 1,000 KB (before 64-bit encoding), up to a limit of 4 MB for the entire request. These limits cannot be changed.
    You must specify the name of the delivery stream and the data record when using  PutRecord . The data record consists of a data blob that can be up to 1,000 KB in size, and any kind of data, for example, a segment from a log file, geographic location data, web site clickstream data, and so on.
    Firehose buffers records before delivering them to the destination. To disambiguate the data blobs at the destination, a common solution is to use delimiters in the data, such as a newline (\n ) or some other character unique within the data. This allows the consumer application(s) to parse individual data items when reading the data from the destination.
    The  PutRecordBatch response includes a count of failed records, FailedPutCount , and an array of responses, RequestResponses . Each entry in the RequestResponses array provides additional information about the processed record, and directly correlates with a record in the request array using the same ordering, from the top to the bottom. The response array always includes the same number of records as the request array. RequestResponses includes both successfully and unsuccessfully processed records. Firehose attempts to process all records in each  PutRecordBatch request. A single record failure does not stop the processing of subsequent records.
    A successfully processed record includes a RecordId value, which is unique for the record. An unsuccessfully processed record includes ErrorCode and ErrorMessage values. ErrorCode reflects the type of error, and is one of the following values: ServiceUnavailable or InternalFailure . ErrorMessage provides more detailed information about the error.
    If there is an internal server error or a timeout, the write might have completed or it might have failed. If FailedPutCount is greater than 0, retry the request, resending only those records that might have failed processing. This minimizes the possible duplicate records and also reduces the total bytes sent (and corresponding charges). We recommend that you handle any duplicates at the destination.
    If  PutRecordBatch throws ServiceUnavailableException , back off and retry. If the exception persists, it is possible that the throughput limits have been exceeded for the delivery stream.
    Data records sent to Firehose are stored for 24 hours from the time they are added to a delivery stream as it attempts to send the records to the destination. If the destination is unreachable for more than 24 hours, the data is no longer available.
    See also: AWS API Documentation
    
    
    :example: response = client.put_record_batch(
        DeliveryStreamName='string',
        Records=[
            {
                'Data': b'bytes'
            },
        ]
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]
            The name of the delivery stream.
            

    :type Records: list
    :param Records: [REQUIRED]
            One or more records.
            (dict) --The unit of data in a delivery stream.
            Data (bytes) -- [REQUIRED]The data blob, which is base64-encoded when the blob is serialized. The maximum size of the data blob, before base64-encoding, is 1,000 KB.
            
            

    :rtype: dict
    :return: {
        'FailedPutCount': 123,
        'RequestResponses': [
            {
                'RecordId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def update_destination(DeliveryStreamName=None, CurrentDeliveryStreamVersionId=None, DestinationId=None, S3DestinationUpdate=None, ExtendedS3DestinationUpdate=None, RedshiftDestinationUpdate=None, ElasticsearchDestinationUpdate=None):
    """
    Updates the specified destination of the specified delivery stream.
    You can use this operation to change the destination type (for example, to replace the Amazon S3 destination with Amazon Redshift) or change the parameters associated with a destination (for example, to change the bucket name of the Amazon S3 destination). The update might not occur immediately. The target delivery stream remains active while the configurations are updated, so data writes to the delivery stream can continue during this process. The updated configurations are usually effective within a few minutes.
    Note that switching between Amazon ES and other services is not supported. For an Amazon ES destination, you can only update to another Amazon ES destination.
    If the destination type is the same, Firehose merges the configuration parameters specified with the destination configuration that already exists on the delivery stream. If any of the parameters are not specified in the call, the existing values are retained. For example, in the Amazon S3 destination, if  EncryptionConfiguration is not specified then the existing  EncryptionConfiguration is maintained on the destination.
    If the destination type is not the same, for example, changing the destination from Amazon S3 to Amazon Redshift, Firehose does not merge any parameters. In this case, all parameters must be specified.
    Firehose uses CurrentDeliveryStreamVersionId to avoid race conditions and conflicting merges. This is a required field, and the service updates the configuration only if the existing configuration has a version ID that matches. After the update is applied successfully, the version ID is updated, and can be retrieved using  DescribeDeliveryStream . You should use the new version ID to set CurrentDeliveryStreamVersionId in the next call.
    See also: AWS API Documentation
    
    
    :example: response = client.update_destination(
        DeliveryStreamName='string',
        CurrentDeliveryStreamVersionId='string',
        DestinationId='string',
        S3DestinationUpdate={
            'RoleARN': 'string',
            'BucketARN': 'string',
            'Prefix': 'string',
            'BufferingHints': {
                'SizeInMBs': 123,
                'IntervalInSeconds': 123
            },
            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
            'EncryptionConfiguration': {
                'NoEncryptionConfig': 'NoEncryption',
                'KMSEncryptionConfig': {
                    'AWSKMSKeyARN': 'string'
                }
            },
            'CloudWatchLoggingOptions': {
                'Enabled': True|False,
                'LogGroupName': 'string',
                'LogStreamName': 'string'
            }
        },
        ExtendedS3DestinationUpdate={
            'RoleARN': 'string',
            'BucketARN': 'string',
            'Prefix': 'string',
            'BufferingHints': {
                'SizeInMBs': 123,
                'IntervalInSeconds': 123
            },
            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
            'EncryptionConfiguration': {
                'NoEncryptionConfig': 'NoEncryption',
                'KMSEncryptionConfig': {
                    'AWSKMSKeyARN': 'string'
                }
            },
            'CloudWatchLoggingOptions': {
                'Enabled': True|False,
                'LogGroupName': 'string',
                'LogStreamName': 'string'
            },
            'ProcessingConfiguration': {
                'Enabled': True|False,
                'Processors': [
                    {
                        'Type': 'Lambda',
                        'Parameters': [
                            {
                                'ParameterName': 'LambdaArn'|'NumberOfRetries',
                                'ParameterValue': 'string'
                            },
                        ]
                    },
                ]
            },
            'S3BackupMode': 'Disabled'|'Enabled',
            'S3BackupUpdate': {
                'RoleARN': 'string',
                'BucketARN': 'string',
                'Prefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
                'EncryptionConfiguration': {
                    'NoEncryptionConfig': 'NoEncryption',
                    'KMSEncryptionConfig': {
                        'AWSKMSKeyARN': 'string'
                    }
                },
                'CloudWatchLoggingOptions': {
                    'Enabled': True|False,
                    'LogGroupName': 'string',
                    'LogStreamName': 'string'
                }
            }
        },
        RedshiftDestinationUpdate={
            'RoleARN': 'string',
            'ClusterJDBCURL': 'string',
            'CopyCommand': {
                'DataTableName': 'string',
                'DataTableColumns': 'string',
                'CopyOptions': 'string'
            },
            'Username': 'string',
            'Password': 'string',
            'RetryOptions': {
                'DurationInSeconds': 123
            },
            'S3Update': {
                'RoleARN': 'string',
                'BucketARN': 'string',
                'Prefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
                'EncryptionConfiguration': {
                    'NoEncryptionConfig': 'NoEncryption',
                    'KMSEncryptionConfig': {
                        'AWSKMSKeyARN': 'string'
                    }
                },
                'CloudWatchLoggingOptions': {
                    'Enabled': True|False,
                    'LogGroupName': 'string',
                    'LogStreamName': 'string'
                }
            },
            'ProcessingConfiguration': {
                'Enabled': True|False,
                'Processors': [
                    {
                        'Type': 'Lambda',
                        'Parameters': [
                            {
                                'ParameterName': 'LambdaArn'|'NumberOfRetries',
                                'ParameterValue': 'string'
                            },
                        ]
                    },
                ]
            },
            'S3BackupMode': 'Disabled'|'Enabled',
            'S3BackupUpdate': {
                'RoleARN': 'string',
                'BucketARN': 'string',
                'Prefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
                'EncryptionConfiguration': {
                    'NoEncryptionConfig': 'NoEncryption',
                    'KMSEncryptionConfig': {
                        'AWSKMSKeyARN': 'string'
                    }
                },
                'CloudWatchLoggingOptions': {
                    'Enabled': True|False,
                    'LogGroupName': 'string',
                    'LogStreamName': 'string'
                }
            },
            'CloudWatchLoggingOptions': {
                'Enabled': True|False,
                'LogGroupName': 'string',
                'LogStreamName': 'string'
            }
        },
        ElasticsearchDestinationUpdate={
            'RoleARN': 'string',
            'DomainARN': 'string',
            'IndexName': 'string',
            'TypeName': 'string',
            'IndexRotationPeriod': 'NoRotation'|'OneHour'|'OneDay'|'OneWeek'|'OneMonth',
            'BufferingHints': {
                'IntervalInSeconds': 123,
                'SizeInMBs': 123
            },
            'RetryOptions': {
                'DurationInSeconds': 123
            },
            'S3Update': {
                'RoleARN': 'string',
                'BucketARN': 'string',
                'Prefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy',
                'EncryptionConfiguration': {
                    'NoEncryptionConfig': 'NoEncryption',
                    'KMSEncryptionConfig': {
                        'AWSKMSKeyARN': 'string'
                    }
                },
                'CloudWatchLoggingOptions': {
                    'Enabled': True|False,
                    'LogGroupName': 'string',
                    'LogStreamName': 'string'
                }
            },
            'ProcessingConfiguration': {
                'Enabled': True|False,
                'Processors': [
                    {
                        'Type': 'Lambda',
                        'Parameters': [
                            {
                                'ParameterName': 'LambdaArn'|'NumberOfRetries',
                                'ParameterValue': 'string'
                            },
                        ]
                    },
                ]
            },
            'CloudWatchLoggingOptions': {
                'Enabled': True|False,
                'LogGroupName': 'string',
                'LogStreamName': 'string'
            }
        }
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]
            The name of the delivery stream.
            

    :type CurrentDeliveryStreamVersionId: string
    :param CurrentDeliveryStreamVersionId: [REQUIRED]
            Obtain this value from the VersionId result of DeliveryStreamDescription . This value is required, and helps the service to perform conditional operations. For example, if there is a interleaving update and this value is null, then the update destination fails. After the update is successful, the VersionId value is updated. The service then performs a merge of the old configuration with the new configuration.
            

    :type DestinationId: string
    :param DestinationId: [REQUIRED]
            The ID of the destination.
            

    :type S3DestinationUpdate: dict
    :param S3DestinationUpdate: [Deprecated] Describes an update for a destination in Amazon S3.
            RoleARN (string) --The ARN of the AWS credentials.
            BucketARN (string) --The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            
            

    :type ExtendedS3DestinationUpdate: dict
    :param ExtendedS3DestinationUpdate: Describes an update for a destination in Amazon S3.
            RoleARN (string) --The ARN of the AWS credentials.
            BucketARN (string) --The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            ProcessingConfiguration (dict) --The data processing configuration.
            Enabled (boolean) --Enables or disables data processing.
            Processors (list) --The data processors.
            (dict) --Describes a data processor.
            Type (string) -- [REQUIRED]The type of processor.
            Parameters (list) --The processor parameters.
            (dict) --Describes the processor parameter.
            ParameterName (string) -- [REQUIRED]The name of the parameter.
            ParameterValue (string) -- [REQUIRED]The parameter value.
            
            
            S3BackupMode (string) --Enables or disables Amazon S3 backup mode.
            S3BackupUpdate (dict) --The Amazon S3 destination for backup.
            RoleARN (string) --The ARN of the AWS credentials.
            BucketARN (string) --The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            
            

    :type RedshiftDestinationUpdate: dict
    :param RedshiftDestinationUpdate: Describes an update for a destination in Amazon Redshift.
            RoleARN (string) --The ARN of the AWS credentials.
            ClusterJDBCURL (string) --The database connection string.
            CopyCommand (dict) --The COPY command.
            DataTableName (string) -- [REQUIRED]The name of the target table. The table must already exist in the database.
            DataTableColumns (string) --A comma-separated list of column names.
            CopyOptions (string) --Optional parameters to use with the Amazon Redshift COPY command. For more information, see the 'Optional Parameters' section of Amazon Redshift COPY command . Some possible examples that would apply to Firehose are as follows:
            delimiter '\t' lzop; - fields are delimited with 't' (TAB character) and compressed using lzop.delimiter '| - fields are delimited with '|' (this is the default delimiter).
            delimiter '|' escape - the delimiter should be escaped.
            fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6' - fields are fixed width in the source, with each width specified after every column in the table.
            JSON 's3://mybucket/jsonpaths.txt' - data is in JSON format, and the path specified is the format of the data.
            For more examples, see Amazon Redshift COPY command examples .
            Username (string) --The name of the user.
            Password (string) --The user password.
            RetryOptions (dict) --The retry behavior in the event that Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).
            DurationInSeconds (integer) --The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value.
            S3Update (dict) --The Amazon S3 destination.
            The compression formats SNAPPY or ZIP cannot be specified in RedshiftDestinationUpdate.S3Update because the Amazon Redshift COPY operation that reads from the S3 bucket doesn't support these compression formats.
            RoleARN (string) --The ARN of the AWS credentials.
            BucketARN (string) --The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            
            ProcessingConfiguration (dict) --The data processing configuration.
            Enabled (boolean) --Enables or disables data processing.
            Processors (list) --The data processors.
            (dict) --Describes a data processor.
            Type (string) -- [REQUIRED]The type of processor.
            Parameters (list) --The processor parameters.
            (dict) --Describes the processor parameter.
            ParameterName (string) -- [REQUIRED]The name of the parameter.
            ParameterValue (string) -- [REQUIRED]The parameter value.
            
            
            S3BackupMode (string) --The Amazon S3 backup mode.
            S3BackupUpdate (dict) --The Amazon S3 destination for backup.
            RoleARN (string) --The ARN of the AWS credentials.
            BucketARN (string) --The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            
            

    :type ElasticsearchDestinationUpdate: dict
    :param ElasticsearchDestinationUpdate: Describes an update for a destination in Amazon ES.
            RoleARN (string) --The ARN of the IAM role to be assumed by Firehose for calling the Amazon ES Configuration API and for indexing documents. For more information, see Amazon S3 Bucket Access .
            DomainARN (string) --The ARN of the Amazon ES domain. The IAM role must have permissions for DescribeElasticsearchDomain , DescribeElasticsearchDomains , and DescribeElasticsearchDomainConfig after assuming the IAM role specified in RoleARN .
            IndexName (string) --The Elasticsearch index name.
            TypeName (string) --The Elasticsearch type name.
            IndexRotationPeriod (string) --The Elasticsearch index rotation period. Index rotation appends a timestamp to IndexName to facilitate the expiration of old data. For more information, see Index Rotation for Amazon Elasticsearch Service Destination . Default value is OneDay .
            BufferingHints (dict) --The buffering options. If no value is specified, ElasticsearchBufferingHints object default values are used.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
            RetryOptions (dict) --The retry behavior in the event that Firehose is unable to deliver documents to Amazon ES. Default value is 300 (5 minutes).
            DurationInSeconds (integer) --After an initial failure to deliver to Amazon ES, the total amount of time during which Firehose re-attempts delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.
            S3Update (dict) --The Amazon S3 destination.
            RoleARN (string) --The ARN of the AWS credentials.
            BucketARN (string) --The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            
            ProcessingConfiguration (dict) --The data processing configuration.
            Enabled (boolean) --Enables or disables data processing.
            Processors (list) --The data processors.
            (dict) --Describes a data processor.
            Type (string) -- [REQUIRED]The type of processor.
            Parameters (list) --The processor parameters.
            (dict) --Describes the processor parameter.
            ParameterName (string) -- [REQUIRED]The name of the parameter.
            ParameterValue (string) -- [REQUIRED]The parameter value.
            
            
            CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

