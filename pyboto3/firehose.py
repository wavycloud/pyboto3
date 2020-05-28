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

def create_delivery_stream(DeliveryStreamName=None, DeliveryStreamType=None, KinesisStreamSourceConfiguration=None, DeliveryStreamEncryptionConfigurationInput=None, S3DestinationConfiguration=None, ExtendedS3DestinationConfiguration=None, RedshiftDestinationConfiguration=None, ElasticsearchDestinationConfiguration=None, SplunkDestinationConfiguration=None, Tags=None):
    """
    Creates a Kinesis Data Firehose delivery stream.
    By default, you can create up to 50 delivery streams per AWS Region.
    This is an asynchronous operation that immediately returns. The initial status of the delivery stream is CREATING . After the delivery stream is created, its status is ACTIVE and it now accepts data. If the delivery stream creation fails, the status transitions to CREATING_FAILED . Attempts to send data to a delivery stream that is not in the ACTIVE state cause an exception. To check the state of a delivery stream, use  DescribeDeliveryStream .
    If the status of a delivery stream is CREATING_FAILED , this status doesn\'t change, and you can\'t invoke CreateDeliveryStream again on it. However, you can invoke the  DeleteDeliveryStream operation to delete it.
    A Kinesis Data Firehose delivery stream can be configured to receive records directly from providers using  PutRecord or  PutRecordBatch , or it can be configured to use an existing Kinesis stream as its source. To specify a Kinesis data stream as input, set the DeliveryStreamType parameter to KinesisStreamAsSource , and provide the Kinesis stream Amazon Resource Name (ARN) and role ARN in the KinesisStreamSourceConfiguration parameter.
    To create a delivery stream with server-side encryption (SSE) enabled, include  DeliveryStreamEncryptionConfigurationInput in your request. This is optional. You can also invoke  StartDeliveryStreamEncryption to turn on SSE for an existing delivery stream that doesn\'t have SSE enabled.
    A delivery stream is configured with a single destination: Amazon S3, Amazon ES, Amazon Redshift, or Splunk. You must specify only one of the following destination configuration parameters: ExtendedS3DestinationConfiguration , S3DestinationConfiguration , ElasticsearchDestinationConfiguration , RedshiftDestinationConfiguration , or SplunkDestinationConfiguration .
    When you specify S3DestinationConfiguration , you can also provide the following optional values: BufferingHints, EncryptionConfiguration , and CompressionFormat . By default, if no BufferingHints value is provided, Kinesis Data Firehose buffers data up to 5 MB or for 5 minutes, whichever condition is satisfied first. BufferingHints is a hint, so there are some cases where the service cannot adhere to these conditions strictly. For example, record boundaries might be such that the size is a little over or under the configured buffering size. By default, no encryption is performed. We strongly recommend that you enable encryption to ensure secure data storage in Amazon S3.
    A few notes about Amazon Redshift as a destination:
    Kinesis Data Firehose assumes the IAM role that is configured as part of the destination. The role should allow the Kinesis Data Firehose principal to assume the role, and the role should have permissions that allow the service to deliver the data. For more information, see Grant Kinesis Data Firehose Access to an Amazon S3 Destination in the Amazon Kinesis Data Firehose Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_delivery_stream(
        DeliveryStreamName='string',
        DeliveryStreamType='DirectPut'|'KinesisStreamAsSource',
        KinesisStreamSourceConfiguration={
            'KinesisStreamARN': 'string',
            'RoleARN': 'string'
        },
        DeliveryStreamEncryptionConfigurationInput={
            'KeyARN': 'string',
            'KeyType': 'AWS_OWNED_CMK'|'CUSTOMER_MANAGED_CMK'
        },
        S3DestinationConfiguration={
            'RoleARN': 'string',
            'BucketARN': 'string',
            'Prefix': 'string',
            'ErrorOutputPrefix': 'string',
            'BufferingHints': {
                'SizeInMBs': 123,
                'IntervalInSeconds': 123
            },
            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
            'ErrorOutputPrefix': 'string',
            'BufferingHints': {
                'SizeInMBs': 123,
                'IntervalInSeconds': 123
            },
            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
                'ErrorOutputPrefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
            'DataFormatConversionConfiguration': {
                'SchemaConfiguration': {
                    'RoleARN': 'string',
                    'CatalogId': 'string',
                    'DatabaseName': 'string',
                    'TableName': 'string',
                    'Region': 'string',
                    'VersionId': 'string'
                },
                'InputFormatConfiguration': {
                    'Deserializer': {
                        'OpenXJsonSerDe': {
                            'ConvertDotsInJsonKeysToUnderscores': True|False,
                            'CaseInsensitive': True|False,
                            'ColumnToJsonKeyMappings': {
                                'string': 'string'
                            }
                        },
                        'HiveJsonSerDe': {
                            'TimestampFormats': [
                                'string',
                            ]
                        }
                    }
                },
                'OutputFormatConfiguration': {
                    'Serializer': {
                        'ParquetSerDe': {
                            'BlockSizeBytes': 123,
                            'PageSizeBytes': 123,
                            'Compression': 'UNCOMPRESSED'|'GZIP'|'SNAPPY',
                            'EnableDictionaryCompression': True|False,
                            'MaxPaddingBytes': 123,
                            'WriterVersion': 'V1'|'V2'
                        },
                        'OrcSerDe': {
                            'StripeSizeBytes': 123,
                            'BlockSizeBytes': 123,
                            'RowIndexStride': 123,
                            'EnablePadding': True|False,
                            'PaddingTolerance': 123.0,
                            'Compression': 'NONE'|'ZLIB'|'SNAPPY',
                            'BloomFilterColumns': [
                                'string',
                            ],
                            'BloomFilterFalsePositiveProbability': 123.0,
                            'DictionaryKeyThreshold': 123.0,
                            'FormatVersion': 'V0_11'|'V0_12'
                        }
                    }
                },
                'Enabled': True|False
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
                'ErrorOutputPrefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
                'ErrorOutputPrefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
            'ClusterEndpoint': 'string',
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
                'ErrorOutputPrefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
            },
            'VpcConfiguration': {
                'SubnetIds': [
                    'string',
                ],
                'RoleARN': 'string',
                'SecurityGroupIds': [
                    'string',
                ]
            }
        },
        SplunkDestinationConfiguration={
            'HECEndpoint': 'string',
            'HECEndpointType': 'Raw'|'Event',
            'HECToken': 'string',
            'HECAcknowledgmentTimeoutInSeconds': 123,
            'RetryOptions': {
                'DurationInSeconds': 123
            },
            'S3BackupMode': 'FailedEventsOnly'|'AllEvents',
            'S3Configuration': {
                'RoleARN': 'string',
                'BucketARN': 'string',
                'Prefix': 'string',
                'ErrorOutputPrefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]\nThe name of the delivery stream. This name must be unique per AWS account in the same AWS Region. If the delivery streams are in different accounts or different Regions, you can have multiple delivery streams with the same name.\n

    :type DeliveryStreamType: string
    :param DeliveryStreamType: The delivery stream type. This parameter can be one of the following values:\n\nDirectPut : Provider applications access the delivery stream directly.\nKinesisStreamAsSource : The delivery stream uses a Kinesis data stream as a source.\n\n

    :type KinesisStreamSourceConfiguration: dict
    :param KinesisStreamSourceConfiguration: When a Kinesis data stream is used as the source for the delivery stream, a KinesisStreamSourceConfiguration containing the Kinesis data stream Amazon Resource Name (ARN) and the role ARN for the source stream.\n\nKinesisStreamARN (string) -- [REQUIRED]The ARN of the source Kinesis data stream. For more information, see Amazon Kinesis Data Streams ARN Format .\n\nRoleARN (string) -- [REQUIRED]The ARN of the role that provides access to the source Kinesis data stream. For more information, see AWS Identity and Access Management (IAM) ARN Format .\n\n\n

    :type DeliveryStreamEncryptionConfigurationInput: dict
    :param DeliveryStreamEncryptionConfigurationInput: Used to specify the type and Amazon Resource Name (ARN) of the KMS key needed for Server-Side Encryption (SSE).\n\nKeyARN (string) --If you set KeyType to CUSTOMER_MANAGED_CMK , you must specify the Amazon Resource Name (ARN) of the CMK. If you set KeyType to AWS_OWNED_CMK , Kinesis Data Firehose uses a service-account CMK.\n\nKeyType (string) -- [REQUIRED]Indicates the type of customer master key (CMK) to use for encryption. The default setting is AWS_OWNED_CMK . For more information about CMKs, see Customer Master Keys (CMKs) . When you invoke CreateDeliveryStream or StartDeliveryStreamEncryption with KeyType set to CUSTOMER_MANAGED_CMK, Kinesis Data Firehose invokes the Amazon KMS operation CreateGrant to create a grant that allows the Kinesis Data Firehose service to use the customer managed CMK to perform encryption and decryption. Kinesis Data Firehose manages that grant.\nWhen you invoke StartDeliveryStreamEncryption to change the CMK for a delivery stream that is encrypted with a customer managed CMK, Kinesis Data Firehose schedules the grant it had on the old CMK for retirement.\nYou can use a CMK of type CUSTOMER_MANAGED_CMK to encrypt up to 500 delivery streams. If a CreateDeliveryStream or StartDeliveryStreamEncryption operation exceeds this limit, Kinesis Data Firehose throws a LimitExceededException .\n\nWarning\nTo encrypt your delivery stream, use symmetric CMKs. Kinesis Data Firehose doesn\'t support asymmetric CMKs. For information about symmetric and asymmetric CMKs, see About Symmetric and Asymmetric CMKs in the AWS Key Management Service developer guide.\n\n\n\n

    :type S3DestinationConfiguration: dict
    :param S3DestinationConfiguration: [Deprecated] The destination in Amazon S3. You can specify only one destination.\n\nRoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nBucketARN (string) -- [REQUIRED]The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nPrefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .\n\nErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .\n\nBufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.\n\n\n\nCompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .\nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.\n\nEncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.\n\nNoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.\n\nKMSEncryptionConfig (dict) --The encryption key.\n\nAWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n

    :type ExtendedS3DestinationConfiguration: dict
    :param ExtendedS3DestinationConfiguration: The destination in Amazon S3. You can specify only one destination.\n\nRoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nBucketARN (string) -- [REQUIRED]The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nPrefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .\n\nErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .\n\nBufferingHints (dict) --The buffering option.\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.\n\n\n\nCompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED.\n\nEncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.\n\nNoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.\n\nKMSEncryptionConfig (dict) --The encryption key.\n\nAWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The Amazon CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\nProcessingConfiguration (dict) --The data processing configuration.\n\nEnabled (boolean) --Enables or disables data processing.\n\nProcessors (list) --The data processors.\n\n(dict) --Describes a data processor.\n\nType (string) -- [REQUIRED]The type of processor.\n\nParameters (list) --The processor parameters.\n\n(dict) --Describes the processor parameter.\n\nParameterName (string) -- [REQUIRED]The name of the parameter.\n\nParameterValue (string) -- [REQUIRED]The parameter value.\n\n\n\n\n\n\n\n\n\n\n\nS3BackupMode (string) --The Amazon S3 backup mode.\n\nS3BackupConfiguration (dict) --The configuration for backup in Amazon S3.\n\nRoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nBucketARN (string) -- [REQUIRED]The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nPrefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .\n\nErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .\n\nBufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.\n\n\n\nCompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .\nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.\n\nEncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.\n\nNoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.\n\nKMSEncryptionConfig (dict) --The encryption key.\n\nAWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n\nDataFormatConversionConfiguration (dict) --The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.\n\nSchemaConfiguration (dict) --Specifies the AWS Glue Data Catalog table that contains the column information. This parameter is required if Enabled is set to true.\n\nRoleARN (string) --The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren\'t allowed.\n\nCatalogId (string) --The ID of the AWS Glue Data Catalog. If you don\'t supply this, the AWS account ID is used by default.\n\nDatabaseName (string) --Specifies the name of the AWS Glue database that contains the schema for the output data.\n\nTableName (string) --Specifies the AWS Glue table that contains the column information that constitutes your data schema.\n\nRegion (string) --If you don\'t specify an AWS Region, the default is the current Region.\n\nVersionId (string) --Specifies the table version for the output data schema. If you don\'t specify this version ID, or if you set it to LATEST , Kinesis Data Firehose uses the most recent version. This means that any updates to the table are automatically picked up.\n\n\n\nInputFormatConfiguration (dict) --Specifies the deserializer that you want Kinesis Data Firehose to use to convert the format of your data from JSON. This parameter is required if Enabled is set to true.\n\nDeserializer (dict) --Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.\n\nOpenXJsonSerDe (dict) --The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.\n\nConvertDotsInJsonKeysToUnderscores (boolean) --When set to true , specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is 'a.b', you can define the column name to be 'a_b' when using this option.\nThe default is false .\n\nCaseInsensitive (boolean) --When set to true , which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them.\n\nColumnToJsonKeyMappings (dict) --Maps column names to JSON keys that aren\'t identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, timestamp is a Hive keyword. If you have a JSON key named timestamp , set this parameter to {'ts': 'timestamp'} to map this key to a column named ts .\n\n(string) --\n(string) --\n\n\n\n\n\n\nHiveJsonSerDe (dict) --The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.\n\nTimestampFormats (list) --Indicates how you want Kinesis Data Firehose to parse the date and timestamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime\'s DateTimeFormat format strings. For more information, see Class DateTimeFormat . You can also use the special value millis to parse timestamps in epoch milliseconds. If you don\'t specify a format, Kinesis Data Firehose uses java.sql.Timestamp::valueOf by default.\n\n(string) --\n\n\n\n\n\n\n\n\nOutputFormatConfiguration (dict) --Specifies the serializer that you want Kinesis Data Firehose to use to convert the format of your data to the Parquet or ORC format. This parameter is required if Enabled is set to true.\n\nSerializer (dict) --Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.\n\nParquetSerDe (dict) --A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see Apache Parquet .\n\nBlockSizeBytes (integer) --The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.\n\nPageSizeBytes (integer) --The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.\n\nCompression (string) --The compression code to use over data blocks. The possible values are UNCOMPRESSED , SNAPPY , and GZIP , with the default being SNAPPY . Use SNAPPY for higher decompression speed. Use GZIP if the compression ratio is more important than speed.\n\nEnableDictionaryCompression (boolean) --Indicates whether to enable dictionary compression.\n\nMaxPaddingBytes (integer) --The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.\n\nWriterVersion (string) --Indicates the version of row format to output. The possible values are V1 and V2 . The default is V1 .\n\n\n\nOrcSerDe (dict) --A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see Apache ORC .\n\nStripeSizeBytes (integer) --The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.\n\nBlockSizeBytes (integer) --The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.\n\nRowIndexStride (integer) --The number of rows between index entries. The default is 10,000 and the minimum is 1,000.\n\nEnablePadding (boolean) --Set this to true to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is false .\n\nPaddingTolerance (float) --A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is 0.05, which means 5 percent of stripe size.\nFor the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task.\nKinesis Data Firehose ignores this parameter when OrcSerDe$EnablePadding is false .\n\nCompression (string) --The compression code to use over data blocks. The default is SNAPPY .\n\nBloomFilterColumns (list) --The column names for which you want Kinesis Data Firehose to create bloom filters. The default is null .\n\n(string) --\n\n\nBloomFilterFalsePositiveProbability (float) --The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.\n\nDictionaryKeyThreshold (float) --Represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1.\n\nFormatVersion (string) --The version of the file to write. The possible values are V0_11 and V0_12 . The default is V0_12 .\n\n\n\n\n\n\n\nEnabled (boolean) --Defaults to true . Set it to false if you want to disable format conversion while preserving the configuration details.\n\n\n\n\n

    :type RedshiftDestinationConfiguration: dict
    :param RedshiftDestinationConfiguration: The destination in Amazon Redshift. You can specify only one destination.\n\nRoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nClusterJDBCURL (string) -- [REQUIRED]The database connection string.\n\nCopyCommand (dict) -- [REQUIRED]The COPY command.\n\nDataTableName (string) -- [REQUIRED]The name of the target table. The table must already exist in the database.\n\nDataTableColumns (string) --A comma-separated list of column names.\n\nCopyOptions (string) --Optional parameters to use with the Amazon Redshift COPY command. For more information, see the 'Optional Parameters' section of Amazon Redshift COPY command . Some possible examples that would apply to Kinesis Data Firehose are as follows:\n\ndelimiter \'\\t\' lzop; - fields are delimited with 't' (TAB character) and compressed using lzop.delimiter \'|\' - fields are delimited with '|' (this is the default delimiter).\ndelimiter \'|\' escape - the delimiter should be escaped.\nfixedwidth \'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6\' - fields are fixed width in the source, with each width specified after every column in the table.\nJSON \'s3://mybucket/jsonpaths.txt\' - data is in JSON format, and the path specified is the format of the data.\n\nFor more examples, see Amazon Redshift COPY command examples .\n\n\n\nUsername (string) -- [REQUIRED]The name of the user.\n\nPassword (string) -- [REQUIRED]The user password.\n\nRetryOptions (dict) --The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).\n\nDurationInSeconds (integer) --The length of time during which Kinesis Data Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Kinesis Data Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value.\n\n\n\nS3Configuration (dict) -- [REQUIRED]The configuration for the intermediate Amazon S3 location from which Amazon Redshift obtains data. Restrictions are described in the topic for CreateDeliveryStream .\nThe compression formats SNAPPY or ZIP cannot be specified in RedshiftDestinationConfiguration.S3Configuration because the Amazon Redshift COPY operation that reads from the S3 bucket doesn\'t support these compression formats.\n\nRoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nBucketARN (string) -- [REQUIRED]The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nPrefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .\n\nErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .\n\nBufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.\n\n\n\nCompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .\nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.\n\nEncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.\n\nNoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.\n\nKMSEncryptionConfig (dict) --The encryption key.\n\nAWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n\nProcessingConfiguration (dict) --The data processing configuration.\n\nEnabled (boolean) --Enables or disables data processing.\n\nProcessors (list) --The data processors.\n\n(dict) --Describes a data processor.\n\nType (string) -- [REQUIRED]The type of processor.\n\nParameters (list) --The processor parameters.\n\n(dict) --Describes the processor parameter.\n\nParameterName (string) -- [REQUIRED]The name of the parameter.\n\nParameterValue (string) -- [REQUIRED]The parameter value.\n\n\n\n\n\n\n\n\n\n\n\nS3BackupMode (string) --The Amazon S3 backup mode.\n\nS3BackupConfiguration (dict) --The configuration for backup in Amazon S3.\n\nRoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nBucketARN (string) -- [REQUIRED]The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nPrefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .\n\nErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .\n\nBufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.\n\n\n\nCompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .\nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.\n\nEncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.\n\nNoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.\n\nKMSEncryptionConfig (dict) --The encryption key.\n\nAWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n

    :type ElasticsearchDestinationConfiguration: dict
    :param ElasticsearchDestinationConfiguration: The destination in Amazon ES. You can specify only one destination.\n\nRoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon ES Configuration API and for indexing documents. For more information, see Grant Kinesis Data Firehose Access to an Amazon S3 Destination and Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nDomainARN (string) --The ARN of the Amazon ES domain. The IAM role must have permissions for DescribeElasticsearchDomain , DescribeElasticsearchDomains , and DescribeElasticsearchDomainConfig after assuming the role specified in RoleARN . For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\nSpecify either ClusterEndpoint or DomainARN .\n\nClusterEndpoint (string) --The endpoint to use when communicating with the cluster. Specify either this ClusterEndpoint or the DomainARN field.\n\nIndexName (string) -- [REQUIRED]The Elasticsearch index name.\n\nTypeName (string) --The Elasticsearch type name. For Elasticsearch 6.x, there can be only one type per index. If you try to specify a new type for an existing index that already has another type, Kinesis Data Firehose returns an error during run time.\nFor Elasticsearch 7.x, don\'t specify a TypeName .\n\nIndexRotationPeriod (string) --The Elasticsearch index rotation period. Index rotation appends a timestamp to the IndexName to facilitate the expiration of old data. For more information, see Index Rotation for the Amazon ES Destination . The default value is OneDay .\n\nBufferingHints (dict) --The buffering options. If no value is specified, the default values for ElasticsearchBufferingHints are used.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.\n\n\n\nRetryOptions (dict) --The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon ES. The default value is 300 (5 minutes).\n\nDurationInSeconds (integer) --After an initial failure to deliver to Amazon ES, the total amount of time during which Kinesis Data Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.\n\n\n\nS3BackupMode (string) --Defines how documents should be delivered to Amazon S3. When it is set to FailedDocumentsOnly , Kinesis Data Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with elasticsearch-failed/ appended to the key prefix. When set to AllDocuments , Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes failed documents with elasticsearch-failed/ appended to the prefix. For more information, see Amazon S3 Backup for the Amazon ES Destination . Default value is FailedDocumentsOnly .\n\nS3Configuration (dict) -- [REQUIRED]The configuration for the backup Amazon S3 location.\n\nRoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nBucketARN (string) -- [REQUIRED]The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nPrefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .\n\nErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .\n\nBufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.\n\n\n\nCompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .\nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.\n\nEncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.\n\nNoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.\n\nKMSEncryptionConfig (dict) --The encryption key.\n\nAWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n\nProcessingConfiguration (dict) --The data processing configuration.\n\nEnabled (boolean) --Enables or disables data processing.\n\nProcessors (list) --The data processors.\n\n(dict) --Describes a data processor.\n\nType (string) -- [REQUIRED]The type of processor.\n\nParameters (list) --The processor parameters.\n\n(dict) --Describes the processor parameter.\n\nParameterName (string) -- [REQUIRED]The name of the parameter.\n\nParameterValue (string) -- [REQUIRED]The parameter value.\n\n\n\n\n\n\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The Amazon CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\nVpcConfiguration (dict) --The details of the VPC of the Amazon ES destination.\n\nSubnetIds (list) -- [REQUIRED]The IDs of the subnets that you want Kinesis Data Firehose to use to create ENIs in the VPC of the Amazon ES destination. Make sure that the routing tables and inbound and outbound rules allow traffic to flow from the subnets whose IDs are specified here to the subnets that have the destination Amazon ES endpoints. Kinesis Data Firehose creates at least one ENI in each of the subnets that are specified here. Do not delete or modify these ENIs.\nThe number of ENIs that Kinesis Data Firehose creates in the subnets specified here scales up and down automatically based on throughput. To enable Kinesis Data Firehose to scale up the number of ENIs to match throughput, ensure that you have sufficient quota. To help you calculate the quota you need, assume that Kinesis Data Firehose can create up to three ENIs for this delivery stream for each of the subnets specified here. For more information about ENI quota, see Network Interfaces in the Amazon VPC Quotas topic.\n\n(string) --\n\n\nRoleARN (string) -- [REQUIRED]The ARN of the IAM role that you want the delivery stream to use to create endpoints in the destination VPC.\n\nSecurityGroupIds (list) -- [REQUIRED]The IDs of the security groups that you want Kinesis Data Firehose to use when it creates ENIs in the VPC of the Amazon ES destination.\n\n(string) --\n\n\n\n\n\n

    :type SplunkDestinationConfiguration: dict
    :param SplunkDestinationConfiguration: The destination in Splunk. You can specify only one destination.\n\nHECEndpoint (string) -- [REQUIRED]The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your data.\n\nHECEndpointType (string) -- [REQUIRED]This type can be either 'Raw' or 'Event.'\n\nHECToken (string) -- [REQUIRED]This is a GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.\n\nHECAcknowledgmentTimeoutInSeconds (integer) --The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from Splunk after it sends it data. At the end of the timeout period, Kinesis Data Firehose either tries to send the data again or considers it an error, based on your retry settings.\n\nRetryOptions (dict) --The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk, or if it doesn\'t receive an acknowledgment of receipt from Splunk.\n\nDurationInSeconds (integer) --The total amount of time that Kinesis Data Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesn\'t include the periods during which Kinesis Data Firehose waits for acknowledgment from Splunk after each attempt.\n\n\n\nS3BackupMode (string) --Defines how documents should be delivered to Amazon S3. When set to FailedDocumentsOnly , Kinesis Data Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to AllDocuments , Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. Default value is FailedDocumentsOnly .\n\nS3Configuration (dict) -- [REQUIRED]The configuration for the backup Amazon S3 location.\n\nRoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nBucketARN (string) -- [REQUIRED]The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nPrefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .\n\nErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .\n\nBufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.\n\n\n\nCompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .\nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.\n\nEncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.\n\nNoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.\n\nKMSEncryptionConfig (dict) --The encryption key.\n\nAWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n\nProcessingConfiguration (dict) --The data processing configuration.\n\nEnabled (boolean) --Enables or disables data processing.\n\nProcessors (list) --The data processors.\n\n(dict) --Describes a data processor.\n\nType (string) -- [REQUIRED]The type of processor.\n\nParameters (list) --The processor parameters.\n\n(dict) --Describes the processor parameter.\n\nParameterName (string) -- [REQUIRED]The name of the parameter.\n\nParameterValue (string) -- [REQUIRED]The parameter value.\n\n\n\n\n\n\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The Amazon CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n

    :type Tags: list
    :param Tags: A set of tags to assign to the delivery stream. A tag is a key-value pair that you can define and assign to AWS resources. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the delivery stream. For more information about tags, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide.\nYou can specify up to 50 tags when creating a delivery stream.\n\n(dict) --Metadata that you can assign to a delivery stream, consisting of a key-value pair.\n\nKey (string) -- [REQUIRED]A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @\n\nValue (string) --An optional string, which you can use to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DeliveryStreamARN': 'string'
}


Response Structure

(dict) --

DeliveryStreamARN (string) --
The ARN of the delivery stream.







Exceptions

Firehose.Client.exceptions.InvalidArgumentException
Firehose.Client.exceptions.LimitExceededException
Firehose.Client.exceptions.ResourceInUseException
Firehose.Client.exceptions.InvalidKMSResourceException


    :return: {
        'DeliveryStreamARN': 'string'
    }
    
    
    :returns: 
    DeliveryStreamName (string) -- [REQUIRED]
    The name of the delivery stream. This name must be unique per AWS account in the same AWS Region. If the delivery streams are in different accounts or different Regions, you can have multiple delivery streams with the same name.
    
    DeliveryStreamType (string) -- The delivery stream type. This parameter can be one of the following values:
    
    DirectPut : Provider applications access the delivery stream directly.
    KinesisStreamAsSource : The delivery stream uses a Kinesis data stream as a source.
    
    
    KinesisStreamSourceConfiguration (dict) -- When a Kinesis data stream is used as the source for the delivery stream, a  KinesisStreamSourceConfiguration containing the Kinesis data stream Amazon Resource Name (ARN) and the role ARN for the source stream.
    
    KinesisStreamARN (string) -- [REQUIRED]The ARN of the source Kinesis data stream. For more information, see Amazon Kinesis Data Streams ARN Format .
    
    RoleARN (string) -- [REQUIRED]The ARN of the role that provides access to the source Kinesis data stream. For more information, see AWS Identity and Access Management (IAM) ARN Format .
    
    
    
    DeliveryStreamEncryptionConfigurationInput (dict) -- Used to specify the type and Amazon Resource Name (ARN) of the KMS key needed for Server-Side Encryption (SSE).
    
    KeyARN (string) --If you set KeyType to CUSTOMER_MANAGED_CMK , you must specify the Amazon Resource Name (ARN) of the CMK. If you set KeyType to AWS_OWNED_CMK , Kinesis Data Firehose uses a service-account CMK.
    
    KeyType (string) -- [REQUIRED]Indicates the type of customer master key (CMK) to use for encryption. The default setting is AWS_OWNED_CMK . For more information about CMKs, see Customer Master Keys (CMKs) . When you invoke  CreateDeliveryStream or  StartDeliveryStreamEncryption with KeyType set to CUSTOMER_MANAGED_CMK, Kinesis Data Firehose invokes the Amazon KMS operation CreateGrant to create a grant that allows the Kinesis Data Firehose service to use the customer managed CMK to perform encryption and decryption. Kinesis Data Firehose manages that grant.
    When you invoke  StartDeliveryStreamEncryption to change the CMK for a delivery stream that is encrypted with a customer managed CMK, Kinesis Data Firehose schedules the grant it had on the old CMK for retirement.
    You can use a CMK of type CUSTOMER_MANAGED_CMK to encrypt up to 500 delivery streams. If a  CreateDeliveryStream or  StartDeliveryStreamEncryption operation exceeds this limit, Kinesis Data Firehose throws a LimitExceededException .
    
    Warning
    To encrypt your delivery stream, use symmetric CMKs. Kinesis Data Firehose doesn\'t support asymmetric CMKs. For information about symmetric and asymmetric CMKs, see About Symmetric and Asymmetric CMKs in the AWS Key Management Service developer guide.
    
    
    
    
    S3DestinationConfiguration (dict) -- [Deprecated] The destination in Amazon S3. You can specify only one destination.
    
    RoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    Prefix (string) --The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .
    
    ErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .
    
    BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.
    
    
    
    CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
    The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
    
    EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
    
    NoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.
    
    KMSEncryptionConfig (dict) --The encryption key.
    
    AWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
    
    Enabled (boolean) --Enables or disables CloudWatch logging.
    
    LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
    
    LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
    
    
    
    
    
    ExtendedS3DestinationConfiguration (dict) -- The destination in Amazon S3. You can specify only one destination.
    
    RoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    Prefix (string) --The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .
    
    ErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .
    
    BufferingHints (dict) --The buffering option.
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.
    
    
    
    CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED.
    
    EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
    
    NoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.
    
    KMSEncryptionConfig (dict) --The encryption key.
    
    AWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The Amazon CloudWatch logging options for your delivery stream.
    
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
    
    RoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    Prefix (string) --The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .
    
    ErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .
    
    BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.
    
    
    
    CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
    The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
    
    EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
    
    NoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.
    
    KMSEncryptionConfig (dict) --The encryption key.
    
    AWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
    
    Enabled (boolean) --Enables or disables CloudWatch logging.
    
    LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
    
    LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
    
    
    
    
    
    DataFormatConversionConfiguration (dict) --The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.
    
    SchemaConfiguration (dict) --Specifies the AWS Glue Data Catalog table that contains the column information. This parameter is required if Enabled is set to true.
    
    RoleARN (string) --The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren\'t allowed.
    
    CatalogId (string) --The ID of the AWS Glue Data Catalog. If you don\'t supply this, the AWS account ID is used by default.
    
    DatabaseName (string) --Specifies the name of the AWS Glue database that contains the schema for the output data.
    
    TableName (string) --Specifies the AWS Glue table that contains the column information that constitutes your data schema.
    
    Region (string) --If you don\'t specify an AWS Region, the default is the current Region.
    
    VersionId (string) --Specifies the table version for the output data schema. If you don\'t specify this version ID, or if you set it to LATEST , Kinesis Data Firehose uses the most recent version. This means that any updates to the table are automatically picked up.
    
    
    
    InputFormatConfiguration (dict) --Specifies the deserializer that you want Kinesis Data Firehose to use to convert the format of your data from JSON. This parameter is required if Enabled is set to true.
    
    Deserializer (dict) --Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.
    
    OpenXJsonSerDe (dict) --The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.
    
    ConvertDotsInJsonKeysToUnderscores (boolean) --When set to true , specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is "a.b", you can define the column name to be "a_b" when using this option.
    The default is false .
    
    CaseInsensitive (boolean) --When set to true , which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them.
    
    ColumnToJsonKeyMappings (dict) --Maps column names to JSON keys that aren\'t identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, timestamp is a Hive keyword. If you have a JSON key named timestamp , set this parameter to {"ts": "timestamp"} to map this key to a column named ts .
    
    (string) --
    (string) --
    
    
    
    
    
    
    HiveJsonSerDe (dict) --The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.
    
    TimestampFormats (list) --Indicates how you want Kinesis Data Firehose to parse the date and timestamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime\'s DateTimeFormat format strings. For more information, see Class DateTimeFormat . You can also use the special value millis to parse timestamps in epoch milliseconds. If you don\'t specify a format, Kinesis Data Firehose uses java.sql.Timestamp::valueOf by default.
    
    (string) --
    
    
    
    
    
    
    
    
    OutputFormatConfiguration (dict) --Specifies the serializer that you want Kinesis Data Firehose to use to convert the format of your data to the Parquet or ORC format. This parameter is required if Enabled is set to true.
    
    Serializer (dict) --Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.
    
    ParquetSerDe (dict) --A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see Apache Parquet .
    
    BlockSizeBytes (integer) --The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
    
    PageSizeBytes (integer) --The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.
    
    Compression (string) --The compression code to use over data blocks. The possible values are UNCOMPRESSED , SNAPPY , and GZIP , with the default being SNAPPY . Use SNAPPY for higher decompression speed. Use GZIP if the compression ratio is more important than speed.
    
    EnableDictionaryCompression (boolean) --Indicates whether to enable dictionary compression.
    
    MaxPaddingBytes (integer) --The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.
    
    WriterVersion (string) --Indicates the version of row format to output. The possible values are V1 and V2 . The default is V1 .
    
    
    
    OrcSerDe (dict) --A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see Apache ORC .
    
    StripeSizeBytes (integer) --The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.
    
    BlockSizeBytes (integer) --The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
    
    RowIndexStride (integer) --The number of rows between index entries. The default is 10,000 and the minimum is 1,000.
    
    EnablePadding (boolean) --Set this to true to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is false .
    
    PaddingTolerance (float) --A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is 0.05, which means 5 percent of stripe size.
    For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task.
    Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is false .
    
    Compression (string) --The compression code to use over data blocks. The default is SNAPPY .
    
    BloomFilterColumns (list) --The column names for which you want Kinesis Data Firehose to create bloom filters. The default is null .
    
    (string) --
    
    
    BloomFilterFalsePositiveProbability (float) --The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.
    
    DictionaryKeyThreshold (float) --Represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1.
    
    FormatVersion (string) --The version of the file to write. The possible values are V0_11 and V0_12 . The default is V0_12 .
    
    
    
    
    
    
    
    Enabled (boolean) --Defaults to true . Set it to false if you want to disable format conversion while preserving the configuration details.
    
    
    
    
    
    RedshiftDestinationConfiguration (dict) -- The destination in Amazon Redshift. You can specify only one destination.
    
    RoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    ClusterJDBCURL (string) -- [REQUIRED]The database connection string.
    
    CopyCommand (dict) -- [REQUIRED]The COPY command.
    
    DataTableName (string) -- [REQUIRED]The name of the target table. The table must already exist in the database.
    
    DataTableColumns (string) --A comma-separated list of column names.
    
    CopyOptions (string) --Optional parameters to use with the Amazon Redshift COPY command. For more information, see the "Optional Parameters" section of Amazon Redshift COPY command . Some possible examples that would apply to Kinesis Data Firehose are as follows:
    
    delimiter \'\\t\' lzop; - fields are delimited with "t" (TAB character) and compressed using lzop.delimiter \'|\' - fields are delimited with "|" (this is the default delimiter).
    delimiter \'|\' escape - the delimiter should be escaped.
    fixedwidth \'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6\' - fields are fixed width in the source, with each width specified after every column in the table.
    JSON \'s3://mybucket/jsonpaths.txt\' - data is in JSON format, and the path specified is the format of the data.
    
    For more examples, see Amazon Redshift COPY command examples .
    
    
    
    Username (string) -- [REQUIRED]The name of the user.
    
    Password (string) -- [REQUIRED]The user password.
    
    RetryOptions (dict) --The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).
    
    DurationInSeconds (integer) --The length of time during which Kinesis Data Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Kinesis Data Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value.
    
    
    
    S3Configuration (dict) -- [REQUIRED]The configuration for the intermediate Amazon S3 location from which Amazon Redshift obtains data. Restrictions are described in the topic for  CreateDeliveryStream .
    The compression formats SNAPPY or ZIP cannot be specified in RedshiftDestinationConfiguration.S3Configuration because the Amazon Redshift COPY operation that reads from the S3 bucket doesn\'t support these compression formats.
    
    RoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    Prefix (string) --The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .
    
    ErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .
    
    BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.
    
    
    
    CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
    The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
    
    EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
    
    NoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.
    
    KMSEncryptionConfig (dict) --The encryption key.
    
    AWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    
    
    
    
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
    
    RoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    Prefix (string) --The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .
    
    ErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .
    
    BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.
    
    
    
    CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
    The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
    
    EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
    
    NoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.
    
    KMSEncryptionConfig (dict) --The encryption key.
    
    AWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
    
    Enabled (boolean) --Enables or disables CloudWatch logging.
    
    LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
    
    LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.
    
    Enabled (boolean) --Enables or disables CloudWatch logging.
    
    LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
    
    LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
    
    
    
    
    
    ElasticsearchDestinationConfiguration (dict) -- The destination in Amazon ES. You can specify only one destination.
    
    RoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon ES Configuration API and for indexing documents. For more information, see Grant Kinesis Data Firehose Access to an Amazon S3 Destination and Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    DomainARN (string) --The ARN of the Amazon ES domain. The IAM role must have permissions for DescribeElasticsearchDomain , DescribeElasticsearchDomains , and DescribeElasticsearchDomainConfig after assuming the role specified in RoleARN . For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    Specify either ClusterEndpoint or DomainARN .
    
    ClusterEndpoint (string) --The endpoint to use when communicating with the cluster. Specify either this ClusterEndpoint or the DomainARN field.
    
    IndexName (string) -- [REQUIRED]The Elasticsearch index name.
    
    TypeName (string) --The Elasticsearch type name. For Elasticsearch 6.x, there can be only one type per index. If you try to specify a new type for an existing index that already has another type, Kinesis Data Firehose returns an error during run time.
    For Elasticsearch 7.x, don\'t specify a TypeName .
    
    IndexRotationPeriod (string) --The Elasticsearch index rotation period. Index rotation appends a timestamp to the IndexName to facilitate the expiration of old data. For more information, see Index Rotation for the Amazon ES Destination . The default value is OneDay .
    
    BufferingHints (dict) --The buffering options. If no value is specified, the default values for ElasticsearchBufferingHints are used.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
    
    
    
    RetryOptions (dict) --The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon ES. The default value is 300 (5 minutes).
    
    DurationInSeconds (integer) --After an initial failure to deliver to Amazon ES, the total amount of time during which Kinesis Data Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.
    
    
    
    S3BackupMode (string) --Defines how documents should be delivered to Amazon S3. When it is set to FailedDocumentsOnly , Kinesis Data Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with elasticsearch-failed/ appended to the key prefix. When set to AllDocuments , Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes failed documents with elasticsearch-failed/ appended to the prefix. For more information, see Amazon S3 Backup for the Amazon ES Destination . Default value is FailedDocumentsOnly .
    
    S3Configuration (dict) -- [REQUIRED]The configuration for the backup Amazon S3 location.
    
    RoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    Prefix (string) --The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .
    
    ErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .
    
    BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.
    
    
    
    CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
    The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
    
    EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
    
    NoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.
    
    KMSEncryptionConfig (dict) --The encryption key.
    
    AWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    
    
    
    
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
    
    
    
    
    
    
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The Amazon CloudWatch logging options for your delivery stream.
    
    Enabled (boolean) --Enables or disables CloudWatch logging.
    
    LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
    
    LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
    
    
    
    VpcConfiguration (dict) --The details of the VPC of the Amazon ES destination.
    
    SubnetIds (list) -- [REQUIRED]The IDs of the subnets that you want Kinesis Data Firehose to use to create ENIs in the VPC of the Amazon ES destination. Make sure that the routing tables and inbound and outbound rules allow traffic to flow from the subnets whose IDs are specified here to the subnets that have the destination Amazon ES endpoints. Kinesis Data Firehose creates at least one ENI in each of the subnets that are specified here. Do not delete or modify these ENIs.
    The number of ENIs that Kinesis Data Firehose creates in the subnets specified here scales up and down automatically based on throughput. To enable Kinesis Data Firehose to scale up the number of ENIs to match throughput, ensure that you have sufficient quota. To help you calculate the quota you need, assume that Kinesis Data Firehose can create up to three ENIs for this delivery stream for each of the subnets specified here. For more information about ENI quota, see Network Interfaces in the Amazon VPC Quotas topic.
    
    (string) --
    
    
    RoleARN (string) -- [REQUIRED]The ARN of the IAM role that you want the delivery stream to use to create endpoints in the destination VPC.
    
    SecurityGroupIds (list) -- [REQUIRED]The IDs of the security groups that you want Kinesis Data Firehose to use when it creates ENIs in the VPC of the Amazon ES destination.
    
    (string) --
    
    
    
    
    
    
    SplunkDestinationConfiguration (dict) -- The destination in Splunk. You can specify only one destination.
    
    HECEndpoint (string) -- [REQUIRED]The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your data.
    
    HECEndpointType (string) -- [REQUIRED]This type can be either "Raw" or "Event."
    
    HECToken (string) -- [REQUIRED]This is a GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.
    
    HECAcknowledgmentTimeoutInSeconds (integer) --The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from Splunk after it sends it data. At the end of the timeout period, Kinesis Data Firehose either tries to send the data again or considers it an error, based on your retry settings.
    
    RetryOptions (dict) --The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk, or if it doesn\'t receive an acknowledgment of receipt from Splunk.
    
    DurationInSeconds (integer) --The total amount of time that Kinesis Data Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesn\'t include the periods during which Kinesis Data Firehose waits for acknowledgment from Splunk after each attempt.
    
    
    
    S3BackupMode (string) --Defines how documents should be delivered to Amazon S3. When set to FailedDocumentsOnly , Kinesis Data Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to AllDocuments , Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. Default value is FailedDocumentsOnly .
    
    S3Configuration (dict) -- [REQUIRED]The configuration for the backup Amazon S3 location.
    
    RoleARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    Prefix (string) --The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .
    
    ErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .
    
    BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
    
    SizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.
    We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.
    
    IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.
    
    
    
    CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
    The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
    
    EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
    
    NoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.
    
    KMSEncryptionConfig (dict) --The encryption key.
    
    AWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    
    
    
    
    
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
    
    
    
    
    
    
    
    
    
    
    
    CloudWatchLoggingOptions (dict) --The Amazon CloudWatch logging options for your delivery stream.
    
    Enabled (boolean) --Enables or disables CloudWatch logging.
    
    LogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.
    
    LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.
    
    
    
    
    
    Tags (list) -- A set of tags to assign to the delivery stream. A tag is a key-value pair that you can define and assign to AWS resources. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the delivery stream. For more information about tags, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide.
    You can specify up to 50 tags when creating a delivery stream.
    
    (dict) --Metadata that you can assign to a delivery stream, consisting of a key-value pair.
    
    Key (string) -- [REQUIRED]A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @
    
    Value (string) --An optional string, which you can use to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @
    
    
    
    
    
    
    """
    pass

def delete_delivery_stream(DeliveryStreamName=None, AllowForceDelete=None):
    """
    Deletes a delivery stream and its data.
    To check the state of a delivery stream, use  DescribeDeliveryStream . You can delete a delivery stream only if it is in one of the following states: ACTIVE , DELETING , CREATING_FAILED , or DELETING_FAILED . You can\'t delete a delivery stream that is in the CREATING state. While the deletion request is in process, the delivery stream is in the DELETING state.
    While the delivery stream is in the DELETING state, the service might continue to accept records, but it doesn\'t make any guarantees with respect to delivering the data. Therefore, as a best practice, first stop any applications that are sending records before you delete a delivery stream.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_delivery_stream(
        DeliveryStreamName='string',
        AllowForceDelete=True|False
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]\nThe name of the delivery stream.\n

    :type AllowForceDelete: boolean
    :param AllowForceDelete: Set this to true if you want to delete the delivery stream even if Kinesis Data Firehose is unable to retire the grant for the CMK. Kinesis Data Firehose might be unable to retire the grant due to a customer error, such as when the CMK or the grant are in an invalid state. If you force deletion, you can then use the RevokeGrant operation to revoke the grant you gave to Kinesis Data Firehose. If a failure to retire the grant happens due to an AWS KMS issue, Kinesis Data Firehose keeps retrying the delete operation.\nThe default value is false.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Firehose.Client.exceptions.ResourceInUseException
Firehose.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_delivery_stream(DeliveryStreamName=None, Limit=None, ExclusiveStartDestinationId=None):
    """
    Describes the specified delivery stream and its status. For example, after your delivery stream is created, call DescribeDeliveryStream to see whether the delivery stream is ACTIVE and therefore ready for data to be sent to it.
    If the status of a delivery stream is CREATING_FAILED , this status doesn\'t change, and you can\'t invoke  CreateDeliveryStream again on it. However, you can invoke the  DeleteDeliveryStream operation to delete it. If the status is DELETING_FAILED , you can force deletion by invoking  DeleteDeliveryStream again but with  DeleteDeliveryStreamInput$AllowForceDelete set to true.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_delivery_stream(
        DeliveryStreamName='string',
        Limit=123,
        ExclusiveStartDestinationId='string'
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]\nThe name of the delivery stream.\n

    :type Limit: integer
    :param Limit: The limit on the number of destinations to return. You can have one destination per delivery stream.

    :type ExclusiveStartDestinationId: string
    :param ExclusiveStartDestinationId: The ID of the destination to start returning the destination information. Kinesis Data Firehose supports one destination per delivery stream.

    :rtype: dict

ReturnsResponse Syntax
{
    'DeliveryStreamDescription': {
        'DeliveryStreamName': 'string',
        'DeliveryStreamARN': 'string',
        'DeliveryStreamStatus': 'CREATING'|'CREATING_FAILED'|'DELETING'|'DELETING_FAILED'|'ACTIVE',
        'FailureDescription': {
            'Type': 'RETIRE_KMS_GRANT_FAILED'|'CREATE_KMS_GRANT_FAILED'|'KMS_ACCESS_DENIED'|'DISABLED_KMS_KEY'|'INVALID_KMS_KEY'|'KMS_KEY_NOT_FOUND'|'KMS_OPT_IN_REQUIRED'|'CREATE_ENI_FAILED'|'DELETE_ENI_FAILED'|'SUBNET_NOT_FOUND'|'SECURITY_GROUP_NOT_FOUND'|'ENI_ACCESS_DENIED'|'SUBNET_ACCESS_DENIED'|'SECURITY_GROUP_ACCESS_DENIED'|'UNKNOWN_ERROR',
            'Details': 'string'
        },
        'DeliveryStreamEncryptionConfiguration': {
            'KeyARN': 'string',
            'KeyType': 'AWS_OWNED_CMK'|'CUSTOMER_MANAGED_CMK',
            'Status': 'ENABLED'|'ENABLING'|'ENABLING_FAILED'|'DISABLED'|'DISABLING'|'DISABLING_FAILED',
            'FailureDescription': {
                'Type': 'RETIRE_KMS_GRANT_FAILED'|'CREATE_KMS_GRANT_FAILED'|'KMS_ACCESS_DENIED'|'DISABLED_KMS_KEY'|'INVALID_KMS_KEY'|'KMS_KEY_NOT_FOUND'|'KMS_OPT_IN_REQUIRED'|'CREATE_ENI_FAILED'|'DELETE_ENI_FAILED'|'SUBNET_NOT_FOUND'|'SECURITY_GROUP_NOT_FOUND'|'ENI_ACCESS_DENIED'|'SUBNET_ACCESS_DENIED'|'SECURITY_GROUP_ACCESS_DENIED'|'UNKNOWN_ERROR',
                'Details': 'string'
            }
        },
        'DeliveryStreamType': 'DirectPut'|'KinesisStreamAsSource',
        'VersionId': 'string',
        'CreateTimestamp': datetime(2015, 1, 1),
        'LastUpdateTimestamp': datetime(2015, 1, 1),
        'Source': {
            'KinesisStreamSourceDescription': {
                'KinesisStreamARN': 'string',
                'RoleARN': 'string',
                'DeliveryStartTimestamp': datetime(2015, 1, 1)
            }
        },
        'Destinations': [
            {
                'DestinationId': 'string',
                'S3DestinationDescription': {
                    'RoleARN': 'string',
                    'BucketARN': 'string',
                    'Prefix': 'string',
                    'ErrorOutputPrefix': 'string',
                    'BufferingHints': {
                        'SizeInMBs': 123,
                        'IntervalInSeconds': 123
                    },
                    'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                    'ErrorOutputPrefix': 'string',
                    'BufferingHints': {
                        'SizeInMBs': 123,
                        'IntervalInSeconds': 123
                    },
                    'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                        'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
                        'ErrorOutputPrefix': 'string',
                        'BufferingHints': {
                            'SizeInMBs': 123,
                            'IntervalInSeconds': 123
                        },
                        'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                    'DataFormatConversionConfiguration': {
                        'SchemaConfiguration': {
                            'RoleARN': 'string',
                            'CatalogId': 'string',
                            'DatabaseName': 'string',
                            'TableName': 'string',
                            'Region': 'string',
                            'VersionId': 'string'
                        },
                        'InputFormatConfiguration': {
                            'Deserializer': {
                                'OpenXJsonSerDe': {
                                    'ConvertDotsInJsonKeysToUnderscores': True|False,
                                    'CaseInsensitive': True|False,
                                    'ColumnToJsonKeyMappings': {
                                        'string': 'string'
                                    }
                                },
                                'HiveJsonSerDe': {
                                    'TimestampFormats': [
                                        'string',
                                    ]
                                }
                            }
                        },
                        'OutputFormatConfiguration': {
                            'Serializer': {
                                'ParquetSerDe': {
                                    'BlockSizeBytes': 123,
                                    'PageSizeBytes': 123,
                                    'Compression': 'UNCOMPRESSED'|'GZIP'|'SNAPPY',
                                    'EnableDictionaryCompression': True|False,
                                    'MaxPaddingBytes': 123,
                                    'WriterVersion': 'V1'|'V2'
                                },
                                'OrcSerDe': {
                                    'StripeSizeBytes': 123,
                                    'BlockSizeBytes': 123,
                                    'RowIndexStride': 123,
                                    'EnablePadding': True|False,
                                    'PaddingTolerance': 123.0,
                                    'Compression': 'NONE'|'ZLIB'|'SNAPPY',
                                    'BloomFilterColumns': [
                                        'string',
                                    ],
                                    'BloomFilterFalsePositiveProbability': 123.0,
                                    'DictionaryKeyThreshold': 123.0,
                                    'FormatVersion': 'V0_11'|'V0_12'
                                }
                            }
                        },
                        'Enabled': True|False
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
                        'ErrorOutputPrefix': 'string',
                        'BufferingHints': {
                            'SizeInMBs': 123,
                            'IntervalInSeconds': 123
                        },
                        'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                        'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
                        'ErrorOutputPrefix': 'string',
                        'BufferingHints': {
                            'SizeInMBs': 123,
                            'IntervalInSeconds': 123
                        },
                        'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                    'ClusterEndpoint': 'string',
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
                        'ErrorOutputPrefix': 'string',
                        'BufferingHints': {
                            'SizeInMBs': 123,
                            'IntervalInSeconds': 123
                        },
                        'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                        'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
                    },
                    'VpcConfigurationDescription': {
                        'SubnetIds': [
                            'string',
                        ],
                        'RoleARN': 'string',
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'VpcId': 'string'
                    }
                },
                'SplunkDestinationDescription': {
                    'HECEndpoint': 'string',
                    'HECEndpointType': 'Raw'|'Event',
                    'HECToken': 'string',
                    'HECAcknowledgmentTimeoutInSeconds': 123,
                    'RetryOptions': {
                        'DurationInSeconds': 123
                    },
                    'S3BackupMode': 'FailedEventsOnly'|'AllEvents',
                    'S3DestinationDescription': {
                        'RoleARN': 'string',
                        'BucketARN': 'string',
                        'Prefix': 'string',
                        'ErrorOutputPrefix': 'string',
                        'BufferingHints': {
                            'SizeInMBs': 123,
                            'IntervalInSeconds': 123
                        },
                        'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                        'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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


Response Structure

(dict) --

DeliveryStreamDescription (dict) --
Information about the delivery stream.

DeliveryStreamName (string) --
The name of the delivery stream.

DeliveryStreamARN (string) --
The Amazon Resource Name (ARN) of the delivery stream. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

DeliveryStreamStatus (string) --
The status of the delivery stream. If the status of a delivery stream is CREATING_FAILED , this status doesn\'t change, and you can\'t invoke CreateDeliveryStream again on it. However, you can invoke the  DeleteDeliveryStream operation to delete it.

FailureDescription (dict) --
Provides details in case one of the following operations fails due to an error related to KMS:  CreateDeliveryStream ,  DeleteDeliveryStream ,  StartDeliveryStreamEncryption ,  StopDeliveryStreamEncryption .

Type (string) --
The type of error that caused the failure.

Details (string) --
A message providing details about the error that caused the failure.



DeliveryStreamEncryptionConfiguration (dict) --
Indicates the server-side encryption (SSE) status for the delivery stream.

KeyARN (string) --
If KeyType is CUSTOMER_MANAGED_CMK , this field contains the ARN of the customer managed CMK. If KeyType is AWS_OWNED_CMK , DeliveryStreamEncryptionConfiguration doesn\'t contain a value for KeyARN .

KeyType (string) --
Indicates the type of customer master key (CMK) that is used for encryption. The default setting is AWS_OWNED_CMK . For more information about CMKs, see Customer Master Keys (CMKs) .

Status (string) --
This is the server-side encryption (SSE) status for the delivery stream. For a full description of the different values of this status, see  StartDeliveryStreamEncryption and  StopDeliveryStreamEncryption . If this status is ENABLING_FAILED or DISABLING_FAILED , it is the status of the most recent attempt to enable or disable SSE, respectively.

FailureDescription (dict) --
Provides details in case one of the following operations fails due to an error related to KMS:  CreateDeliveryStream ,  DeleteDeliveryStream ,  StartDeliveryStreamEncryption ,  StopDeliveryStreamEncryption .

Type (string) --
The type of error that caused the failure.

Details (string) --
A message providing details about the error that caused the failure.





DeliveryStreamType (string) --
The delivery stream type. This can be one of the following values:

DirectPut : Provider applications access the delivery stream directly.
KinesisStreamAsSource : The delivery stream uses a Kinesis data stream as a source.


VersionId (string) --
Each time the destination is updated for a delivery stream, the version ID is changed, and the current version ID is required when updating the destination. This is so that the service knows it is applying the changes to the correct version of the delivery stream.

CreateTimestamp (datetime) --
The date and time that the delivery stream was created.

LastUpdateTimestamp (datetime) --
The date and time that the delivery stream was last updated.

Source (dict) --
If the DeliveryStreamType parameter is KinesisStreamAsSource , a  SourceDescription object describing the source Kinesis data stream.

KinesisStreamSourceDescription (dict) --
The  KinesisStreamSourceDescription value for the source Kinesis data stream.

KinesisStreamARN (string) --
The Amazon Resource Name (ARN) of the source Kinesis data stream. For more information, see Amazon Kinesis Data Streams ARN Format .

RoleARN (string) --
The ARN of the role used by the source Kinesis data stream. For more information, see AWS Identity and Access Management (IAM) ARN Format .

DeliveryStartTimestamp (datetime) --
Kinesis Data Firehose starts retrieving records from the Kinesis data stream starting with this timestamp.





Destinations (list) --
The destinations.

(dict) --
Describes the destination for a delivery stream.

DestinationId (string) --
The ID of the destination.

S3DestinationDescription (dict) --
[Deprecated] The destination in Amazon S3.

RoleARN (string) --
The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

BucketARN (string) --
The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

Prefix (string) --
The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .

ErrorOutputPrefix (string) --
A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .

BufferingHints (dict) --
The buffering option. If no value is specified, BufferingHints object default values are used.

SizeInMBs (integer) --
Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.
We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds (integer) --
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.



CompressionFormat (string) --
The compression format. If no value is specified, the default is UNCOMPRESSED .

EncryptionConfiguration (dict) --
The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig (string) --
Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig (dict) --
The encryption key.

AWSKMSKeyARN (string) --
The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .





CloudWatchLoggingOptions (dict) --
The Amazon CloudWatch logging options for your delivery stream.

Enabled (boolean) --
Enables or disables CloudWatch logging.

LogGroupName (string) --
The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName (string) --
The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.





ExtendedS3DestinationDescription (dict) --
The destination in Amazon S3.

RoleARN (string) --
The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

BucketARN (string) --
The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

Prefix (string) --
The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .

ErrorOutputPrefix (string) --
A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .

BufferingHints (dict) --
The buffering option.

SizeInMBs (integer) --
Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.
We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds (integer) --
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.



CompressionFormat (string) --
The compression format. If no value is specified, the default is UNCOMPRESSED .

EncryptionConfiguration (dict) --
The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig (string) --
Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig (dict) --
The encryption key.

AWSKMSKeyARN (string) --
The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .





CloudWatchLoggingOptions (dict) --
The Amazon CloudWatch logging options for your delivery stream.

Enabled (boolean) --
Enables or disables CloudWatch logging.

LogGroupName (string) --
The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName (string) --
The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.



ProcessingConfiguration (dict) --
The data processing configuration.

Enabled (boolean) --
Enables or disables data processing.

Processors (list) --
The data processors.

(dict) --
Describes a data processor.

Type (string) --
The type of processor.

Parameters (list) --
The processor parameters.

(dict) --
Describes the processor parameter.

ParameterName (string) --
The name of the parameter.

ParameterValue (string) --
The parameter value.











S3BackupMode (string) --
The Amazon S3 backup mode.

S3BackupDescription (dict) --
The configuration for backup in Amazon S3.

RoleARN (string) --
The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

BucketARN (string) --
The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

Prefix (string) --
The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .

ErrorOutputPrefix (string) --
A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .

BufferingHints (dict) --
The buffering option. If no value is specified, BufferingHints object default values are used.

SizeInMBs (integer) --
Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.
We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds (integer) --
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.



CompressionFormat (string) --
The compression format. If no value is specified, the default is UNCOMPRESSED .

EncryptionConfiguration (dict) --
The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig (string) --
Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig (dict) --
The encryption key.

AWSKMSKeyARN (string) --
The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .





CloudWatchLoggingOptions (dict) --
The Amazon CloudWatch logging options for your delivery stream.

Enabled (boolean) --
Enables or disables CloudWatch logging.

LogGroupName (string) --
The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName (string) --
The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.





DataFormatConversionConfiguration (dict) --
The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.

SchemaConfiguration (dict) --
Specifies the AWS Glue Data Catalog table that contains the column information. This parameter is required if Enabled is set to true.

RoleARN (string) --
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren\'t allowed.

CatalogId (string) --
The ID of the AWS Glue Data Catalog. If you don\'t supply this, the AWS account ID is used by default.

DatabaseName (string) --
Specifies the name of the AWS Glue database that contains the schema for the output data.

TableName (string) --
Specifies the AWS Glue table that contains the column information that constitutes your data schema.

Region (string) --
If you don\'t specify an AWS Region, the default is the current Region.

VersionId (string) --
Specifies the table version for the output data schema. If you don\'t specify this version ID, or if you set it to LATEST , Kinesis Data Firehose uses the most recent version. This means that any updates to the table are automatically picked up.



InputFormatConfiguration (dict) --
Specifies the deserializer that you want Kinesis Data Firehose to use to convert the format of your data from JSON. This parameter is required if Enabled is set to true.

Deserializer (dict) --
Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.

OpenXJsonSerDe (dict) --
The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.

ConvertDotsInJsonKeysToUnderscores (boolean) --
When set to true , specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is "a.b", you can define the column name to be "a_b" when using this option.
The default is false .

CaseInsensitive (boolean) --
When set to true , which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them.

ColumnToJsonKeyMappings (dict) --
Maps column names to JSON keys that aren\'t identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, timestamp is a Hive keyword. If you have a JSON key named timestamp , set this parameter to {"ts": "timestamp"} to map this key to a column named ts .

(string) --
(string) --






HiveJsonSerDe (dict) --
The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.

TimestampFormats (list) --
Indicates how you want Kinesis Data Firehose to parse the date and timestamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime\'s DateTimeFormat format strings. For more information, see Class DateTimeFormat . You can also use the special value millis to parse timestamps in epoch milliseconds. If you don\'t specify a format, Kinesis Data Firehose uses java.sql.Timestamp::valueOf by default.

(string) --








OutputFormatConfiguration (dict) --
Specifies the serializer that you want Kinesis Data Firehose to use to convert the format of your data to the Parquet or ORC format. This parameter is required if Enabled is set to true.

Serializer (dict) --
Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.

ParquetSerDe (dict) --
A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see Apache Parquet .

BlockSizeBytes (integer) --
The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

PageSizeBytes (integer) --
The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.

Compression (string) --
The compression code to use over data blocks. The possible values are UNCOMPRESSED , SNAPPY , and GZIP , with the default being SNAPPY . Use SNAPPY for higher decompression speed. Use GZIP if the compression ratio is more important than speed.

EnableDictionaryCompression (boolean) --
Indicates whether to enable dictionary compression.

MaxPaddingBytes (integer) --
The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.

WriterVersion (string) --
Indicates the version of row format to output. The possible values are V1 and V2 . The default is V1 .



OrcSerDe (dict) --
A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see Apache ORC .

StripeSizeBytes (integer) --
The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.

BlockSizeBytes (integer) --
The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.

RowIndexStride (integer) --
The number of rows between index entries. The default is 10,000 and the minimum is 1,000.

EnablePadding (boolean) --
Set this to true to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is false .

PaddingTolerance (float) --
A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is 0.05, which means 5 percent of stripe size.
For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task.
Kinesis Data Firehose ignores this parameter when  OrcSerDe$EnablePadding is false .

Compression (string) --
The compression code to use over data blocks. The default is SNAPPY .

BloomFilterColumns (list) --
The column names for which you want Kinesis Data Firehose to create bloom filters. The default is null .

(string) --


BloomFilterFalsePositiveProbability (float) --
The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.

DictionaryKeyThreshold (float) --
Represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1.

FormatVersion (string) --
The version of the file to write. The possible values are V0_11 and V0_12 . The default is V0_12 .







Enabled (boolean) --
Defaults to true . Set it to false if you want to disable format conversion while preserving the configuration details.





RedshiftDestinationDescription (dict) --
The destination in Amazon Redshift.

RoleARN (string) --
The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

ClusterJDBCURL (string) --
The database connection string.

CopyCommand (dict) --
The COPY command.

DataTableName (string) --
The name of the target table. The table must already exist in the database.

DataTableColumns (string) --
A comma-separated list of column names.

CopyOptions (string) --
Optional parameters to use with the Amazon Redshift COPY command. For more information, see the "Optional Parameters" section of Amazon Redshift COPY command . Some possible examples that would apply to Kinesis Data Firehose are as follows:

delimiter \'\\t\' lzop; - fields are delimited with "t" (TAB character) and compressed using lzop.
delimiter \'|\' - fields are delimited with "|" (this is the default delimiter).
delimiter \'|\' escape - the delimiter should be escaped.
fixedwidth \'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6\' - fields are fixed width in the source, with each width specified after every column in the table.
JSON \'s3://mybucket/jsonpaths.txt\' - data is in JSON format, and the path specified is the format of the data.

For more examples, see Amazon Redshift COPY command examples .



Username (string) --
The name of the user.

RetryOptions (dict) --
The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).

DurationInSeconds (integer) --
The length of time during which Kinesis Data Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Kinesis Data Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value.



S3DestinationDescription (dict) --
The Amazon S3 destination.

RoleARN (string) --
The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

BucketARN (string) --
The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

Prefix (string) --
The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .

ErrorOutputPrefix (string) --
A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .

BufferingHints (dict) --
The buffering option. If no value is specified, BufferingHints object default values are used.

SizeInMBs (integer) --
Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.
We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds (integer) --
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.



CompressionFormat (string) --
The compression format. If no value is specified, the default is UNCOMPRESSED .

EncryptionConfiguration (dict) --
The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig (string) --
Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig (dict) --
The encryption key.

AWSKMSKeyARN (string) --
The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .





CloudWatchLoggingOptions (dict) --
The Amazon CloudWatch logging options for your delivery stream.

Enabled (boolean) --
Enables or disables CloudWatch logging.

LogGroupName (string) --
The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName (string) --
The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.





ProcessingConfiguration (dict) --
The data processing configuration.

Enabled (boolean) --
Enables or disables data processing.

Processors (list) --
The data processors.

(dict) --
Describes a data processor.

Type (string) --
The type of processor.

Parameters (list) --
The processor parameters.

(dict) --
Describes the processor parameter.

ParameterName (string) --
The name of the parameter.

ParameterValue (string) --
The parameter value.











S3BackupMode (string) --
The Amazon S3 backup mode.

S3BackupDescription (dict) --
The configuration for backup in Amazon S3.

RoleARN (string) --
The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

BucketARN (string) --
The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

Prefix (string) --
The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .

ErrorOutputPrefix (string) --
A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .

BufferingHints (dict) --
The buffering option. If no value is specified, BufferingHints object default values are used.

SizeInMBs (integer) --
Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.
We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds (integer) --
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.



CompressionFormat (string) --
The compression format. If no value is specified, the default is UNCOMPRESSED .

EncryptionConfiguration (dict) --
The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig (string) --
Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig (dict) --
The encryption key.

AWSKMSKeyARN (string) --
The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .





CloudWatchLoggingOptions (dict) --
The Amazon CloudWatch logging options for your delivery stream.

Enabled (boolean) --
Enables or disables CloudWatch logging.

LogGroupName (string) --
The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName (string) --
The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.





CloudWatchLoggingOptions (dict) --
The Amazon CloudWatch logging options for your delivery stream.

Enabled (boolean) --
Enables or disables CloudWatch logging.

LogGroupName (string) --
The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName (string) --
The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.





ElasticsearchDestinationDescription (dict) --
The destination in Amazon ES.

RoleARN (string) --
The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

DomainARN (string) --
The ARN of the Amazon ES domain. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
Kinesis Data Firehose uses either ClusterEndpoint or DomainARN to send data to Amazon ES.

ClusterEndpoint (string) --
The endpoint to use when communicating with the cluster. Kinesis Data Firehose uses either this ClusterEndpoint or the DomainARN field to send data to Amazon ES.

IndexName (string) --
The Elasticsearch index name.

TypeName (string) --
The Elasticsearch type name. This applies to Elasticsearch 6.x and lower versions. For Elasticsearch 7.x, there\'s no value for TypeName .

IndexRotationPeriod (string) --
The Elasticsearch index rotation period

BufferingHints (dict) --
The buffering options.

IntervalInSeconds (integer) --
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).

SizeInMBs (integer) --
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.



RetryOptions (dict) --
The Amazon ES retry options.

DurationInSeconds (integer) --
After an initial failure to deliver to Amazon ES, the total amount of time during which Kinesis Data Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.



S3BackupMode (string) --
The Amazon S3 backup mode.

S3DestinationDescription (dict) --
The Amazon S3 destination.

RoleARN (string) --
The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

BucketARN (string) --
The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

Prefix (string) --
The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .

ErrorOutputPrefix (string) --
A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .

BufferingHints (dict) --
The buffering option. If no value is specified, BufferingHints object default values are used.

SizeInMBs (integer) --
Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.
We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds (integer) --
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.



CompressionFormat (string) --
The compression format. If no value is specified, the default is UNCOMPRESSED .

EncryptionConfiguration (dict) --
The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig (string) --
Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig (dict) --
The encryption key.

AWSKMSKeyARN (string) --
The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .





CloudWatchLoggingOptions (dict) --
The Amazon CloudWatch logging options for your delivery stream.

Enabled (boolean) --
Enables or disables CloudWatch logging.

LogGroupName (string) --
The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName (string) --
The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.





ProcessingConfiguration (dict) --
The data processing configuration.

Enabled (boolean) --
Enables or disables data processing.

Processors (list) --
The data processors.

(dict) --
Describes a data processor.

Type (string) --
The type of processor.

Parameters (list) --
The processor parameters.

(dict) --
Describes the processor parameter.

ParameterName (string) --
The name of the parameter.

ParameterValue (string) --
The parameter value.











CloudWatchLoggingOptions (dict) --
The Amazon CloudWatch logging options.

Enabled (boolean) --
Enables or disables CloudWatch logging.

LogGroupName (string) --
The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName (string) --
The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.



VpcConfigurationDescription (dict) --
The details of the VPC of the Amazon ES destination.

SubnetIds (list) --
The IDs of the subnets that Kinesis Data Firehose uses to create ENIs in the VPC of the Amazon ES destination. Make sure that the routing tables and inbound and outbound rules allow traffic to flow from the subnets whose IDs are specified here to the subnets that have the destination Amazon ES endpoints. Kinesis Data Firehose creates at least one ENI in each of the subnets that are specified here. Do not delete or modify these ENIs.
The number of ENIs that Kinesis Data Firehose creates in the subnets specified here scales up and down automatically based on throughput. To enable Kinesis Data Firehose to scale up the number of ENIs to match throughput, ensure that you have sufficient quota. To help you calculate the quota you need, assume that Kinesis Data Firehose can create up to three ENIs for this delivery stream for each of the subnets specified here. For more information about ENI quota, see Network Interfaces in the Amazon VPC Quotas topic.

(string) --


RoleARN (string) --
The ARN of the IAM role that you want the delivery stream uses to create endpoints in the destination VPC.

SecurityGroupIds (list) --
The IDs of the security groups that Kinesis Data Firehose uses when it creates ENIs in the VPC of the Amazon ES destination.

(string) --


VpcId (string) --
The ID of the Amazon ES destination\'s VPC.





SplunkDestinationDescription (dict) --
The destination in Splunk.

HECEndpoint (string) --
The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your data.

HECEndpointType (string) --
This type can be either "Raw" or "Event."

HECToken (string) --
A GUID you obtain from your Splunk cluster when you create a new HEC endpoint.

HECAcknowledgmentTimeoutInSeconds (integer) --
The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from Splunk after it sends it data. At the end of the timeout period, Kinesis Data Firehose either tries to send the data again or considers it an error, based on your retry settings.

RetryOptions (dict) --
The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk or if it doesn\'t receive an acknowledgment of receipt from Splunk.

DurationInSeconds (integer) --
The total amount of time that Kinesis Data Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesn\'t include the periods during which Kinesis Data Firehose waits for acknowledgment from Splunk after each attempt.



S3BackupMode (string) --
Defines how documents should be delivered to Amazon S3. When set to FailedDocumentsOnly , Kinesis Data Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to AllDocuments , Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. Default value is FailedDocumentsOnly .

S3DestinationDescription (dict) --
The Amazon S3 destination.>

RoleARN (string) --
The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

BucketARN (string) --
The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .

Prefix (string) --
The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .

ErrorOutputPrefix (string) --
A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .

BufferingHints (dict) --
The buffering option. If no value is specified, BufferingHints object default values are used.

SizeInMBs (integer) --
Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.
We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds (integer) --
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.



CompressionFormat (string) --
The compression format. If no value is specified, the default is UNCOMPRESSED .

EncryptionConfiguration (dict) --
The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig (string) --
Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig (dict) --
The encryption key.

AWSKMSKeyARN (string) --
The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .





CloudWatchLoggingOptions (dict) --
The Amazon CloudWatch logging options for your delivery stream.

Enabled (boolean) --
Enables or disables CloudWatch logging.

LogGroupName (string) --
The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName (string) --
The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.





ProcessingConfiguration (dict) --
The data processing configuration.

Enabled (boolean) --
Enables or disables data processing.

Processors (list) --
The data processors.

(dict) --
Describes a data processor.

Type (string) --
The type of processor.

Parameters (list) --
The processor parameters.

(dict) --
Describes the processor parameter.

ParameterName (string) --
The name of the parameter.

ParameterValue (string) --
The parameter value.











CloudWatchLoggingOptions (dict) --
The Amazon CloudWatch logging options for your delivery stream.

Enabled (boolean) --
Enables or disables CloudWatch logging.

LogGroupName (string) --
The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName (string) --
The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.









HasMoreDestinations (boolean) --
Indicates whether there are more destinations available to list.









Exceptions

Firehose.Client.exceptions.ResourceNotFoundException


    :return: {
        'DeliveryStreamDescription': {
            'DeliveryStreamName': 'string',
            'DeliveryStreamARN': 'string',
            'DeliveryStreamStatus': 'CREATING'|'CREATING_FAILED'|'DELETING'|'DELETING_FAILED'|'ACTIVE',
            'FailureDescription': {
                'Type': 'RETIRE_KMS_GRANT_FAILED'|'CREATE_KMS_GRANT_FAILED'|'KMS_ACCESS_DENIED'|'DISABLED_KMS_KEY'|'INVALID_KMS_KEY'|'KMS_KEY_NOT_FOUND'|'KMS_OPT_IN_REQUIRED'|'CREATE_ENI_FAILED'|'DELETE_ENI_FAILED'|'SUBNET_NOT_FOUND'|'SECURITY_GROUP_NOT_FOUND'|'ENI_ACCESS_DENIED'|'SUBNET_ACCESS_DENIED'|'SECURITY_GROUP_ACCESS_DENIED'|'UNKNOWN_ERROR',
                'Details': 'string'
            },
            'DeliveryStreamEncryptionConfiguration': {
                'KeyARN': 'string',
                'KeyType': 'AWS_OWNED_CMK'|'CUSTOMER_MANAGED_CMK',
                'Status': 'ENABLED'|'ENABLING'|'ENABLING_FAILED'|'DISABLED'|'DISABLING'|'DISABLING_FAILED',
                'FailureDescription': {
                    'Type': 'RETIRE_KMS_GRANT_FAILED'|'CREATE_KMS_GRANT_FAILED'|'KMS_ACCESS_DENIED'|'DISABLED_KMS_KEY'|'INVALID_KMS_KEY'|'KMS_KEY_NOT_FOUND'|'KMS_OPT_IN_REQUIRED'|'CREATE_ENI_FAILED'|'DELETE_ENI_FAILED'|'SUBNET_NOT_FOUND'|'SECURITY_GROUP_NOT_FOUND'|'ENI_ACCESS_DENIED'|'SUBNET_ACCESS_DENIED'|'SECURITY_GROUP_ACCESS_DENIED'|'UNKNOWN_ERROR',
                    'Details': 'string'
                }
            },
            'DeliveryStreamType': 'DirectPut'|'KinesisStreamAsSource',
            'VersionId': 'string',
            'CreateTimestamp': datetime(2015, 1, 1),
            'LastUpdateTimestamp': datetime(2015, 1, 1),
            'Source': {
                'KinesisStreamSourceDescription': {
                    'KinesisStreamARN': 'string',
                    'RoleARN': 'string',
                    'DeliveryStartTimestamp': datetime(2015, 1, 1)
                }
            },
            'Destinations': [
                {
                    'DestinationId': 'string',
                    'S3DestinationDescription': {
                        'RoleARN': 'string',
                        'BucketARN': 'string',
                        'Prefix': 'string',
                        'ErrorOutputPrefix': 'string',
                        'BufferingHints': {
                            'SizeInMBs': 123,
                            'IntervalInSeconds': 123
                        },
                        'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                        'ErrorOutputPrefix': 'string',
                        'BufferingHints': {
                            'SizeInMBs': 123,
                            'IntervalInSeconds': 123
                        },
                        'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                            'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
                            'ErrorOutputPrefix': 'string',
                            'BufferingHints': {
                                'SizeInMBs': 123,
                                'IntervalInSeconds': 123
                            },
                            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                        'DataFormatConversionConfiguration': {
                            'SchemaConfiguration': {
                                'RoleARN': 'string',
                                'CatalogId': 'string',
                                'DatabaseName': 'string',
                                'TableName': 'string',
                                'Region': 'string',
                                'VersionId': 'string'
                            },
                            'InputFormatConfiguration': {
                                'Deserializer': {
                                    'OpenXJsonSerDe': {
                                        'ConvertDotsInJsonKeysToUnderscores': True|False,
                                        'CaseInsensitive': True|False,
                                        'ColumnToJsonKeyMappings': {
                                            'string': 'string'
                                        }
                                    },
                                    'HiveJsonSerDe': {
                                        'TimestampFormats': [
                                            'string',
                                        ]
                                    }
                                }
                            },
                            'OutputFormatConfiguration': {
                                'Serializer': {
                                    'ParquetSerDe': {
                                        'BlockSizeBytes': 123,
                                        'PageSizeBytes': 123,
                                        'Compression': 'UNCOMPRESSED'|'GZIP'|'SNAPPY',
                                        'EnableDictionaryCompression': True|False,
                                        'MaxPaddingBytes': 123,
                                        'WriterVersion': 'V1'|'V2'
                                    },
                                    'OrcSerDe': {
                                        'StripeSizeBytes': 123,
                                        'BlockSizeBytes': 123,
                                        'RowIndexStride': 123,
                                        'EnablePadding': True|False,
                                        'PaddingTolerance': 123.0,
                                        'Compression': 'NONE'|'ZLIB'|'SNAPPY',
                                        'BloomFilterColumns': [
                                            'string',
                                        ],
                                        'BloomFilterFalsePositiveProbability': 123.0,
                                        'DictionaryKeyThreshold': 123.0,
                                        'FormatVersion': 'V0_11'|'V0_12'
                                    }
                                }
                            },
                            'Enabled': True|False
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
                            'ErrorOutputPrefix': 'string',
                            'BufferingHints': {
                                'SizeInMBs': 123,
                                'IntervalInSeconds': 123
                            },
                            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                            'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
                            'ErrorOutputPrefix': 'string',
                            'BufferingHints': {
                                'SizeInMBs': 123,
                                'IntervalInSeconds': 123
                            },
                            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                        'ClusterEndpoint': 'string',
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
                            'ErrorOutputPrefix': 'string',
                            'BufferingHints': {
                                'SizeInMBs': 123,
                                'IntervalInSeconds': 123
                            },
                            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                            'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
                        },
                        'VpcConfigurationDescription': {
                            'SubnetIds': [
                                'string',
                            ],
                            'RoleARN': 'string',
                            'SecurityGroupIds': [
                                'string',
                            ],
                            'VpcId': 'string'
                        }
                    },
                    'SplunkDestinationDescription': {
                        'HECEndpoint': 'string',
                        'HECEndpointType': 'Raw'|'Event',
                        'HECToken': 'string',
                        'HECAcknowledgmentTimeoutInSeconds': 123,
                        'RetryOptions': {
                            'DurationInSeconds': 123
                        },
                        'S3BackupMode': 'FailedEventsOnly'|'AllEvents',
                        'S3DestinationDescription': {
                            'RoleARN': 'string',
                            'BucketARN': 'string',
                            'Prefix': 'string',
                            'ErrorOutputPrefix': 'string',
                            'BufferingHints': {
                                'SizeInMBs': 123,
                                'IntervalInSeconds': 123
                            },
                            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                            'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
    
    
    :returns: 
    DirectPut : Provider applications access the delivery stream directly.
    KinesisStreamAsSource : The delivery stream uses a Kinesis data stream as a source.
    
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

def list_delivery_streams(Limit=None, DeliveryStreamType=None, ExclusiveStartDeliveryStreamName=None):
    """
    Lists your delivery streams in alphabetical order of their names.
    The number of delivery streams might be too large to return using a single call to ListDeliveryStreams . You can limit the number of delivery streams returned, using the Limit parameter. To determine whether there are more delivery streams to list, check the value of HasMoreDeliveryStreams in the output. If there are more delivery streams to list, you can request them by calling this operation again and setting the ExclusiveStartDeliveryStreamName parameter to the name of the last delivery stream returned in the last call.
    See also: AWS API Documentation
    
    
    :example: response = client.list_delivery_streams(
        Limit=123,
        DeliveryStreamType='DirectPut'|'KinesisStreamAsSource',
        ExclusiveStartDeliveryStreamName='string'
    )
    
    
    :type Limit: integer
    :param Limit: The maximum number of delivery streams to list. The default value is 10.

    :type DeliveryStreamType: string
    :param DeliveryStreamType: The delivery stream type. This can be one of the following values:\n\nDirectPut : Provider applications access the delivery stream directly.\nKinesisStreamAsSource : The delivery stream uses a Kinesis data stream as a source.\n\nThis parameter is optional. If this parameter is omitted, delivery streams of all types are returned.\n

    :type ExclusiveStartDeliveryStreamName: string
    :param ExclusiveStartDeliveryStreamName: The list of delivery streams returned by this call to ListDeliveryStreams will start with the delivery stream whose name comes alphabetically immediately after the name you specify in ExclusiveStartDeliveryStreamName .

    :rtype: dict

ReturnsResponse Syntax
{
    'DeliveryStreamNames': [
        'string',
    ],
    'HasMoreDeliveryStreams': True|False
}


Response Structure

(dict) --

DeliveryStreamNames (list) --
The names of the delivery streams.

(string) --


HasMoreDeliveryStreams (boolean) --
Indicates whether there are more delivery streams available to list.








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

def list_tags_for_delivery_stream(DeliveryStreamName=None, ExclusiveStartTagKey=None, Limit=None):
    """
    Lists the tags for the specified delivery stream. This operation has a limit of five transactions per second per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_delivery_stream(
        DeliveryStreamName='string',
        ExclusiveStartTagKey='string',
        Limit=123
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]\nThe name of the delivery stream whose tags you want to list.\n

    :type ExclusiveStartTagKey: string
    :param ExclusiveStartTagKey: The key to use as the starting point for the list of tags. If you set this parameter, ListTagsForDeliveryStream gets all tags that occur after ExclusiveStartTagKey .

    :type Limit: integer
    :param Limit: The number of tags to return. If this number is less than the total number of tags associated with the delivery stream, HasMoreTags is set to true in the response. To list additional tags, set ExclusiveStartTagKey to the last key in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'HasMoreTags': True|False
}


Response Structure

(dict) --

Tags (list) --
A list of tags associated with DeliveryStreamName , starting with the first tag after ExclusiveStartTagKey and up to the specified Limit .

(dict) --
Metadata that you can assign to a delivery stream, consisting of a key-value pair.

Key (string) --
A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @

Value (string) --
An optional string, which you can use to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @





HasMoreTags (boolean) --
If this is true in the response, more tags are available. To list the remaining tags, set ExclusiveStartTagKey to the key of the last tag returned and call ListTagsForDeliveryStream again.







Exceptions

Firehose.Client.exceptions.ResourceNotFoundException
Firehose.Client.exceptions.InvalidArgumentException
Firehose.Client.exceptions.LimitExceededException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'HasMoreTags': True|False
    }
    
    
    :returns: 
    Firehose.Client.exceptions.ResourceNotFoundException
    Firehose.Client.exceptions.InvalidArgumentException
    Firehose.Client.exceptions.LimitExceededException
    
    """
    pass

def put_record(DeliveryStreamName=None, Record=None):
    """
    Writes a single data record into an Amazon Kinesis Data Firehose delivery stream. To write multiple data records into a delivery stream, use  PutRecordBatch . Applications using these operations are referred to as producers.
    By default, each delivery stream can take in up to 2,000 transactions per second, 5,000 records per second, or 5 MB per second. If you use  PutRecord and  PutRecordBatch , the limits are an aggregate across these two operations for each delivery stream. For more information about limits and how to request an increase, see Amazon Kinesis Data Firehose Limits .
    You must specify the name of the delivery stream and the data record when using  PutRecord . The data record consists of a data blob that can be up to 1,000 KB in size, and any kind of data. For example, it can be a segment from a log file, geographic location data, website clickstream data, and so on.
    Kinesis Data Firehose buffers records before delivering them to the destination. To disambiguate the data blobs at the destination, a common solution is to use delimiters in the data, such as a newline (\
     ) or some other character unique within the data. This allows the consumer application to parse individual data items when reading the data from the destination.
    The PutRecord operation returns a RecordId , which is a unique string assigned to each record. Producer applications can use this ID for purposes such as auditability and investigation.
    If the PutRecord operation throws a ServiceUnavailableException , back off and retry. If the exception persists, it is possible that the throughput limits have been exceeded for the delivery stream.
    Data records sent to Kinesis Data Firehose are stored for 24 hours from the time they are added to a delivery stream as it tries to send the records to the destination. If the destination is unreachable for more than 24 hours, the data is no longer available.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_record(
        DeliveryStreamName='string',
        Record={
            'Data': b'bytes'
        }
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]\nThe name of the delivery stream.\n

    :type Record: dict
    :param Record: [REQUIRED]\nThe record.\n\nData (bytes) -- [REQUIRED]The data blob, which is base64-encoded when the blob is serialized. The maximum size of the data blob, before base64-encoding, is 1,000 KiB.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RecordId': 'string',
    'Encrypted': True|False
}


Response Structure

(dict) --

RecordId (string) --
The ID of the record.

Encrypted (boolean) --
Indicates whether server-side encryption (SSE) was enabled during this operation.







Exceptions

Firehose.Client.exceptions.ResourceNotFoundException
Firehose.Client.exceptions.InvalidArgumentException
Firehose.Client.exceptions.InvalidKMSResourceException
Firehose.Client.exceptions.ServiceUnavailableException


    :return: {
        'RecordId': 'string',
        'Encrypted': True|False
    }
    
    
    :returns: 
    Firehose.Client.exceptions.ResourceNotFoundException
    Firehose.Client.exceptions.InvalidArgumentException
    Firehose.Client.exceptions.InvalidKMSResourceException
    Firehose.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def put_record_batch(DeliveryStreamName=None, Records=None):
    """
    Writes multiple data records into a delivery stream in a single call, which can achieve higher throughput per producer than when writing single records. To write single data records into a delivery stream, use  PutRecord . Applications using these operations are referred to as producers.
    By default, each delivery stream can take in up to 2,000 transactions per second, 5,000 records per second, or 5 MB per second. If you use  PutRecord and  PutRecordBatch , the limits are an aggregate across these two operations for each delivery stream. For more information about limits, see Amazon Kinesis Data Firehose Limits .
    Each  PutRecordBatch request supports up to 500 records. Each record in the request can be as large as 1,000 KB (before 64-bit encoding), up to a limit of 4 MB for the entire request. These limits cannot be changed.
    You must specify the name of the delivery stream and the data record when using  PutRecord . The data record consists of a data blob that can be up to 1,000 KB in size, and any kind of data. For example, it could be a segment from a log file, geographic location data, website clickstream data, and so on.
    Kinesis Data Firehose buffers records before delivering them to the destination. To disambiguate the data blobs at the destination, a common solution is to use delimiters in the data, such as a newline (\
     ) or some other character unique within the data. This allows the consumer application to parse individual data items when reading the data from the destination.
    The  PutRecordBatch response includes a count of failed records, FailedPutCount , and an array of responses, RequestResponses . Even if the  PutRecordBatch call succeeds, the value of FailedPutCount may be greater than 0, indicating that there are records for which the operation didn\'t succeed. Each entry in the RequestResponses array provides additional information about the processed record. It directly correlates with a record in the request array using the same ordering, from the top to the bottom. The response array always includes the same number of records as the request array. RequestResponses includes both successfully and unsuccessfully processed records. Kinesis Data Firehose tries to process all records in each  PutRecordBatch request. A single record failure does not stop the processing of subsequent records.
    A successfully processed record includes a RecordId value, which is unique for the record. An unsuccessfully processed record includes ErrorCode and ErrorMessage values. ErrorCode reflects the type of error, and is one of the following values: ServiceUnavailableException or InternalFailure . ErrorMessage provides more detailed information about the error.
    If there is an internal server error or a timeout, the write might have completed or it might have failed. If FailedPutCount is greater than 0, retry the request, resending only those records that might have failed processing. This minimizes the possible duplicate records and also reduces the total bytes sent (and corresponding charges). We recommend that you handle any duplicates at the destination.
    If  PutRecordBatch throws ServiceUnavailableException , back off and retry. If the exception persists, it is possible that the throughput limits have been exceeded for the delivery stream.
    Data records sent to Kinesis Data Firehose are stored for 24 hours from the time they are added to a delivery stream as it attempts to send the records to the destination. If the destination is unreachable for more than 24 hours, the data is no longer available.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_record_batch(
        DeliveryStreamName='string',
        Records=[
            {
                'Data': b'bytes'
            },
        ]
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]\nThe name of the delivery stream.\n

    :type Records: list
    :param Records: [REQUIRED]\nOne or more records.\n\n(dict) --The unit of data in a delivery stream.\n\nData (bytes) -- [REQUIRED]The data blob, which is base64-encoded when the blob is serialized. The maximum size of the data blob, before base64-encoding, is 1,000 KiB.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FailedPutCount': 123,
    'Encrypted': True|False,
    'RequestResponses': [
        {
            'RecordId': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

FailedPutCount (integer) --
The number of records that might have failed processing. This number might be greater than 0 even if the  PutRecordBatch call succeeds. Check FailedPutCount to determine whether there are records that you need to resend.

Encrypted (boolean) --
Indicates whether server-side encryption (SSE) was enabled during this operation.

RequestResponses (list) --
The results array. For each record, the index of the response element is the same as the index used in the request array.

(dict) --
Contains the result for an individual record from a  PutRecordBatch request. If the record is successfully added to your delivery stream, it receives a record ID. If the record fails to be added to your delivery stream, the result includes an error code and an error message.

RecordId (string) --
The ID of the record.

ErrorCode (string) --
The error code for an individual record result.

ErrorMessage (string) --
The error message for an individual record result.











Exceptions

Firehose.Client.exceptions.ResourceNotFoundException
Firehose.Client.exceptions.InvalidArgumentException
Firehose.Client.exceptions.InvalidKMSResourceException
Firehose.Client.exceptions.ServiceUnavailableException


    :return: {
        'FailedPutCount': 123,
        'Encrypted': True|False,
        'RequestResponses': [
            {
                'RecordId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Firehose.Client.exceptions.ResourceNotFoundException
    Firehose.Client.exceptions.InvalidArgumentException
    Firehose.Client.exceptions.InvalidKMSResourceException
    Firehose.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def start_delivery_stream_encryption(DeliveryStreamName=None, DeliveryStreamEncryptionConfigurationInput=None):
    """
    Enables server-side encryption (SSE) for the delivery stream.
    This operation is asynchronous. It returns immediately. When you invoke it, Kinesis Data Firehose first sets the encryption status of the stream to ENABLING , and then to ENABLED . The encryption status of a delivery stream is the Status property in  DeliveryStreamEncryptionConfiguration . If the operation fails, the encryption status changes to ENABLING_FAILED . You can continue to read and write data to your delivery stream while the encryption status is ENABLING , but the data is not encrypted. It can take up to 5 seconds after the encryption status changes to ENABLED before all records written to the delivery stream are encrypted. To find out whether a record or a batch of records was encrypted, check the response elements  PutRecordOutput$Encrypted and  PutRecordBatchOutput$Encrypted , respectively.
    To check the encryption status of a delivery stream, use  DescribeDeliveryStream .
    Even if encryption is currently enabled for a delivery stream, you can still invoke this operation on it to change the ARN of the CMK or both its type and ARN. If you invoke this method to change the CMK, and the old CMK is of type CUSTOMER_MANAGED_CMK , Kinesis Data Firehose schedules the grant it had on the old CMK for retirement. If the new CMK is of type CUSTOMER_MANAGED_CMK , Kinesis Data Firehose creates a grant that enables it to use the new CMK to encrypt and decrypt data and to manage the grant.
    If a delivery stream already has encryption enabled and then you invoke this operation to change the ARN of the CMK or both its type and ARN and you get ENABLING_FAILED , this only means that the attempt to change the CMK failed. In this case, encryption remains enabled with the old CMK.
    If the encryption status of your delivery stream is ENABLING_FAILED , you can invoke this operation again with a valid CMK. The CMK must be enabled and the key policy mustn\'t explicitly deny the permission for Kinesis Data Firehose to invoke KMS encrypt and decrypt operations.
    You can enable SSE for a delivery stream only if it\'s a delivery stream that uses DirectPut as its source.
    The StartDeliveryStreamEncryption and StopDeliveryStreamEncryption operations have a combined limit of 25 calls per delivery stream per 24 hours. For example, you reach the limit if you call StartDeliveryStreamEncryption 13 times and StopDeliveryStreamEncryption 12 times for the same delivery stream in a 24-hour period.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_delivery_stream_encryption(
        DeliveryStreamName='string',
        DeliveryStreamEncryptionConfigurationInput={
            'KeyARN': 'string',
            'KeyType': 'AWS_OWNED_CMK'|'CUSTOMER_MANAGED_CMK'
        }
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]\nThe name of the delivery stream for which you want to enable server-side encryption (SSE).\n

    :type DeliveryStreamEncryptionConfigurationInput: dict
    :param DeliveryStreamEncryptionConfigurationInput: Used to specify the type and Amazon Resource Name (ARN) of the KMS key needed for Server-Side Encryption (SSE).\n\nKeyARN (string) --If you set KeyType to CUSTOMER_MANAGED_CMK , you must specify the Amazon Resource Name (ARN) of the CMK. If you set KeyType to AWS_OWNED_CMK , Kinesis Data Firehose uses a service-account CMK.\n\nKeyType (string) -- [REQUIRED]Indicates the type of customer master key (CMK) to use for encryption. The default setting is AWS_OWNED_CMK . For more information about CMKs, see Customer Master Keys (CMKs) . When you invoke CreateDeliveryStream or StartDeliveryStreamEncryption with KeyType set to CUSTOMER_MANAGED_CMK, Kinesis Data Firehose invokes the Amazon KMS operation CreateGrant to create a grant that allows the Kinesis Data Firehose service to use the customer managed CMK to perform encryption and decryption. Kinesis Data Firehose manages that grant.\nWhen you invoke StartDeliveryStreamEncryption to change the CMK for a delivery stream that is encrypted with a customer managed CMK, Kinesis Data Firehose schedules the grant it had on the old CMK for retirement.\nYou can use a CMK of type CUSTOMER_MANAGED_CMK to encrypt up to 500 delivery streams. If a CreateDeliveryStream or StartDeliveryStreamEncryption operation exceeds this limit, Kinesis Data Firehose throws a LimitExceededException .\n\nWarning\nTo encrypt your delivery stream, use symmetric CMKs. Kinesis Data Firehose doesn\'t support asymmetric CMKs. For information about symmetric and asymmetric CMKs, see About Symmetric and Asymmetric CMKs in the AWS Key Management Service developer guide.\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Firehose.Client.exceptions.ResourceNotFoundException
Firehose.Client.exceptions.ResourceInUseException
Firehose.Client.exceptions.InvalidArgumentException
Firehose.Client.exceptions.LimitExceededException
Firehose.Client.exceptions.InvalidKMSResourceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def stop_delivery_stream_encryption(DeliveryStreamName=None):
    """
    Disables server-side encryption (SSE) for the delivery stream.
    This operation is asynchronous. It returns immediately. When you invoke it, Kinesis Data Firehose first sets the encryption status of the stream to DISABLING , and then to DISABLED . You can continue to read and write data to your stream while its status is DISABLING . It can take up to 5 seconds after the encryption status changes to DISABLED before all records written to the delivery stream are no longer subject to encryption. To find out whether a record or a batch of records was encrypted, check the response elements  PutRecordOutput$Encrypted and  PutRecordBatchOutput$Encrypted , respectively.
    To check the encryption state of a delivery stream, use  DescribeDeliveryStream .
    If SSE is enabled using a customer managed CMK and then you invoke StopDeliveryStreamEncryption , Kinesis Data Firehose schedules the related KMS grant for retirement and then retires it after it ensures that it is finished delivering records to the destination.
    The StartDeliveryStreamEncryption and StopDeliveryStreamEncryption operations have a combined limit of 25 calls per delivery stream per 24 hours. For example, you reach the limit if you call StartDeliveryStreamEncryption 13 times and StopDeliveryStreamEncryption 12 times for the same delivery stream in a 24-hour period.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_delivery_stream_encryption(
        DeliveryStreamName='string'
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]\nThe name of the delivery stream for which you want to disable server-side encryption (SSE).\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Firehose.Client.exceptions.ResourceNotFoundException
Firehose.Client.exceptions.ResourceInUseException
Firehose.Client.exceptions.InvalidArgumentException
Firehose.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    Firehose.Client.exceptions.ResourceNotFoundException
    Firehose.Client.exceptions.ResourceInUseException
    Firehose.Client.exceptions.InvalidArgumentException
    Firehose.Client.exceptions.LimitExceededException
    
    """
    pass

def tag_delivery_stream(DeliveryStreamName=None, Tags=None):
    """
    Adds or updates tags for the specified delivery stream. A tag is a key-value pair that you can define and assign to AWS resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the delivery stream. For more information about tags, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
    Each delivery stream can have up to 50 tags.
    This operation has a limit of five transactions per second per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_delivery_stream(
        DeliveryStreamName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]\nThe name of the delivery stream to which you want to add the tags.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nA set of key-value pairs to use to create the tags.\n\n(dict) --Metadata that you can assign to a delivery stream, consisting of a key-value pair.\n\nKey (string) -- [REQUIRED]A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @\n\nValue (string) --An optional string, which you can use to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Firehose.Client.exceptions.ResourceNotFoundException
Firehose.Client.exceptions.ResourceInUseException
Firehose.Client.exceptions.InvalidArgumentException
Firehose.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_delivery_stream(DeliveryStreamName=None, TagKeys=None):
    """
    Removes tags from the specified delivery stream. Removed tags are deleted, and you can\'t recover them after this operation successfully completes.
    If you specify a tag that doesn\'t exist, the operation ignores it.
    This operation has a limit of five transactions per second per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_delivery_stream(
        DeliveryStreamName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type DeliveryStreamName: string
    :param DeliveryStreamName: [REQUIRED]\nThe name of the delivery stream.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of tag keys. Each corresponding tag is removed from the delivery stream.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Firehose.Client.exceptions.ResourceNotFoundException
Firehose.Client.exceptions.ResourceInUseException
Firehose.Client.exceptions.InvalidArgumentException
Firehose.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_destination(DeliveryStreamName=None, CurrentDeliveryStreamVersionId=None, DestinationId=None, S3DestinationUpdate=None, ExtendedS3DestinationUpdate=None, RedshiftDestinationUpdate=None, ElasticsearchDestinationUpdate=None, SplunkDestinationUpdate=None):
    """
    Updates the specified destination of the specified delivery stream.
    Use this operation to change the destination type (for example, to replace the Amazon S3 destination with Amazon Redshift) or change the parameters associated with a destination (for example, to change the bucket name of the Amazon S3 destination). The update might not occur immediately. The target delivery stream remains active while the configurations are updated, so data writes to the delivery stream can continue during this process. The updated configurations are usually effective within a few minutes.
    Switching between Amazon ES and other services is not supported. For an Amazon ES destination, you can only update to another Amazon ES destination.
    If the destination type is the same, Kinesis Data Firehose merges the configuration parameters specified with the destination configuration that already exists on the delivery stream. If any of the parameters are not specified in the call, the existing values are retained. For example, in the Amazon S3 destination, if  EncryptionConfiguration is not specified, then the existing EncryptionConfiguration is maintained on the destination.
    If the destination type is not the same, for example, changing the destination from Amazon S3 to Amazon Redshift, Kinesis Data Firehose does not merge any parameters. In this case, all parameters must be specified.
    Kinesis Data Firehose uses CurrentDeliveryStreamVersionId to avoid race conditions and conflicting merges. This is a required field, and the service updates the configuration only if the existing configuration has a version ID that matches. After the update is applied successfully, the version ID is updated, and can be retrieved using  DescribeDeliveryStream . Use the new version ID to set CurrentDeliveryStreamVersionId in the next call.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_destination(
        DeliveryStreamName='string',
        CurrentDeliveryStreamVersionId='string',
        DestinationId='string',
        S3DestinationUpdate={
            'RoleARN': 'string',
            'BucketARN': 'string',
            'Prefix': 'string',
            'ErrorOutputPrefix': 'string',
            'BufferingHints': {
                'SizeInMBs': 123,
                'IntervalInSeconds': 123
            },
            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
            'ErrorOutputPrefix': 'string',
            'BufferingHints': {
                'SizeInMBs': 123,
                'IntervalInSeconds': 123
            },
            'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
                'ErrorOutputPrefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
            'DataFormatConversionConfiguration': {
                'SchemaConfiguration': {
                    'RoleARN': 'string',
                    'CatalogId': 'string',
                    'DatabaseName': 'string',
                    'TableName': 'string',
                    'Region': 'string',
                    'VersionId': 'string'
                },
                'InputFormatConfiguration': {
                    'Deserializer': {
                        'OpenXJsonSerDe': {
                            'ConvertDotsInJsonKeysToUnderscores': True|False,
                            'CaseInsensitive': True|False,
                            'ColumnToJsonKeyMappings': {
                                'string': 'string'
                            }
                        },
                        'HiveJsonSerDe': {
                            'TimestampFormats': [
                                'string',
                            ]
                        }
                    }
                },
                'OutputFormatConfiguration': {
                    'Serializer': {
                        'ParquetSerDe': {
                            'BlockSizeBytes': 123,
                            'PageSizeBytes': 123,
                            'Compression': 'UNCOMPRESSED'|'GZIP'|'SNAPPY',
                            'EnableDictionaryCompression': True|False,
                            'MaxPaddingBytes': 123,
                            'WriterVersion': 'V1'|'V2'
                        },
                        'OrcSerDe': {
                            'StripeSizeBytes': 123,
                            'BlockSizeBytes': 123,
                            'RowIndexStride': 123,
                            'EnablePadding': True|False,
                            'PaddingTolerance': 123.0,
                            'Compression': 'NONE'|'ZLIB'|'SNAPPY',
                            'BloomFilterColumns': [
                                'string',
                            ],
                            'BloomFilterFalsePositiveProbability': 123.0,
                            'DictionaryKeyThreshold': 123.0,
                            'FormatVersion': 'V0_11'|'V0_12'
                        }
                    }
                },
                'Enabled': True|False
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
                'ErrorOutputPrefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
                'ErrorOutputPrefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
            'ClusterEndpoint': 'string',
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
                'ErrorOutputPrefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
        },
        SplunkDestinationUpdate={
            'HECEndpoint': 'string',
            'HECEndpointType': 'Raw'|'Event',
            'HECToken': 'string',
            'HECAcknowledgmentTimeoutInSeconds': 123,
            'RetryOptions': {
                'DurationInSeconds': 123
            },
            'S3BackupMode': 'FailedEventsOnly'|'AllEvents',
            'S3Update': {
                'RoleARN': 'string',
                'BucketARN': 'string',
                'Prefix': 'string',
                'ErrorOutputPrefix': 'string',
                'BufferingHints': {
                    'SizeInMBs': 123,
                    'IntervalInSeconds': 123
                },
                'CompressionFormat': 'UNCOMPRESSED'|'GZIP'|'ZIP'|'Snappy'|'HADOOP_SNAPPY',
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
                                'ParameterName': 'LambdaArn'|'NumberOfRetries'|'RoleArn'|'BufferSizeInMBs'|'BufferIntervalInSeconds',
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
    :param DeliveryStreamName: [REQUIRED]\nThe name of the delivery stream.\n

    :type CurrentDeliveryStreamVersionId: string
    :param CurrentDeliveryStreamVersionId: [REQUIRED]\nObtain this value from the VersionId result of DeliveryStreamDescription . This value is required, and helps the service perform conditional operations. For example, if there is an interleaving update and this value is null, then the update destination fails. After the update is successful, the VersionId value is updated. The service then performs a merge of the old configuration with the new configuration.\n

    :type DestinationId: string
    :param DestinationId: [REQUIRED]\nThe ID of the destination.\n

    :type S3DestinationUpdate: dict
    :param S3DestinationUpdate: [Deprecated] Describes an update for a destination in Amazon S3.\n\nRoleARN (string) --The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nBucketARN (string) --The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nPrefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .\n\nErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .\n\nBufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.\n\n\n\nCompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .\nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.\n\nEncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.\n\nNoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.\n\nKMSEncryptionConfig (dict) --The encryption key.\n\nAWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n

    :type ExtendedS3DestinationUpdate: dict
    :param ExtendedS3DestinationUpdate: Describes an update for a destination in Amazon S3.\n\nRoleARN (string) --The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nBucketARN (string) --The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nPrefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .\n\nErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .\n\nBufferingHints (dict) --The buffering option.\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.\n\n\n\nCompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .\n\nEncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.\n\nNoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.\n\nKMSEncryptionConfig (dict) --The encryption key.\n\nAWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The Amazon CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\nProcessingConfiguration (dict) --The data processing configuration.\n\nEnabled (boolean) --Enables or disables data processing.\n\nProcessors (list) --The data processors.\n\n(dict) --Describes a data processor.\n\nType (string) -- [REQUIRED]The type of processor.\n\nParameters (list) --The processor parameters.\n\n(dict) --Describes the processor parameter.\n\nParameterName (string) -- [REQUIRED]The name of the parameter.\n\nParameterValue (string) -- [REQUIRED]The parameter value.\n\n\n\n\n\n\n\n\n\n\n\nS3BackupMode (string) --Enables or disables Amazon S3 backup mode.\n\nS3BackupUpdate (dict) --The Amazon S3 destination for backup.\n\nRoleARN (string) --The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nBucketARN (string) --The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nPrefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .\n\nErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .\n\nBufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.\n\n\n\nCompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .\nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.\n\nEncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.\n\nNoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.\n\nKMSEncryptionConfig (dict) --The encryption key.\n\nAWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n\nDataFormatConversionConfiguration (dict) --The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.\n\nSchemaConfiguration (dict) --Specifies the AWS Glue Data Catalog table that contains the column information. This parameter is required if Enabled is set to true.\n\nRoleARN (string) --The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren\'t allowed.\n\nCatalogId (string) --The ID of the AWS Glue Data Catalog. If you don\'t supply this, the AWS account ID is used by default.\n\nDatabaseName (string) --Specifies the name of the AWS Glue database that contains the schema for the output data.\n\nTableName (string) --Specifies the AWS Glue table that contains the column information that constitutes your data schema.\n\nRegion (string) --If you don\'t specify an AWS Region, the default is the current Region.\n\nVersionId (string) --Specifies the table version for the output data schema. If you don\'t specify this version ID, or if you set it to LATEST , Kinesis Data Firehose uses the most recent version. This means that any updates to the table are automatically picked up.\n\n\n\nInputFormatConfiguration (dict) --Specifies the deserializer that you want Kinesis Data Firehose to use to convert the format of your data from JSON. This parameter is required if Enabled is set to true.\n\nDeserializer (dict) --Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.\n\nOpenXJsonSerDe (dict) --The OpenX SerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.\n\nConvertDotsInJsonKeysToUnderscores (boolean) --When set to true , specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is 'a.b', you can define the column name to be 'a_b' when using this option.\nThe default is false .\n\nCaseInsensitive (boolean) --When set to true , which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them.\n\nColumnToJsonKeyMappings (dict) --Maps column names to JSON keys that aren\'t identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, timestamp is a Hive keyword. If you have a JSON key named timestamp , set this parameter to {'ts': 'timestamp'} to map this key to a column named ts .\n\n(string) --\n(string) --\n\n\n\n\n\n\nHiveJsonSerDe (dict) --The native Hive / HCatalog JsonSerDe. Used by Kinesis Data Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.\n\nTimestampFormats (list) --Indicates how you want Kinesis Data Firehose to parse the date and timestamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime\'s DateTimeFormat format strings. For more information, see Class DateTimeFormat . You can also use the special value millis to parse timestamps in epoch milliseconds. If you don\'t specify a format, Kinesis Data Firehose uses java.sql.Timestamp::valueOf by default.\n\n(string) --\n\n\n\n\n\n\n\n\nOutputFormatConfiguration (dict) --Specifies the serializer that you want Kinesis Data Firehose to use to convert the format of your data to the Parquet or ORC format. This parameter is required if Enabled is set to true.\n\nSerializer (dict) --Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.\n\nParquetSerDe (dict) --A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see Apache Parquet .\n\nBlockSizeBytes (integer) --The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.\n\nPageSizeBytes (integer) --The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.\n\nCompression (string) --The compression code to use over data blocks. The possible values are UNCOMPRESSED , SNAPPY , and GZIP , with the default being SNAPPY . Use SNAPPY for higher decompression speed. Use GZIP if the compression ratio is more important than speed.\n\nEnableDictionaryCompression (boolean) --Indicates whether to enable dictionary compression.\n\nMaxPaddingBytes (integer) --The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.\n\nWriterVersion (string) --Indicates the version of row format to output. The possible values are V1 and V2 . The default is V1 .\n\n\n\nOrcSerDe (dict) --A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see Apache ORC .\n\nStripeSizeBytes (integer) --The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.\n\nBlockSizeBytes (integer) --The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.\n\nRowIndexStride (integer) --The number of rows between index entries. The default is 10,000 and the minimum is 1,000.\n\nEnablePadding (boolean) --Set this to true to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is false .\n\nPaddingTolerance (float) --A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is 0.05, which means 5 percent of stripe size.\nFor the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task.\nKinesis Data Firehose ignores this parameter when OrcSerDe$EnablePadding is false .\n\nCompression (string) --The compression code to use over data blocks. The default is SNAPPY .\n\nBloomFilterColumns (list) --The column names for which you want Kinesis Data Firehose to create bloom filters. The default is null .\n\n(string) --\n\n\nBloomFilterFalsePositiveProbability (float) --The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.\n\nDictionaryKeyThreshold (float) --Represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1.\n\nFormatVersion (string) --The version of the file to write. The possible values are V0_11 and V0_12 . The default is V0_12 .\n\n\n\n\n\n\n\nEnabled (boolean) --Defaults to true . Set it to false if you want to disable format conversion while preserving the configuration details.\n\n\n\n\n

    :type RedshiftDestinationUpdate: dict
    :param RedshiftDestinationUpdate: Describes an update for a destination in Amazon Redshift.\n\nRoleARN (string) --The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nClusterJDBCURL (string) --The database connection string.\n\nCopyCommand (dict) --The COPY command.\n\nDataTableName (string) -- [REQUIRED]The name of the target table. The table must already exist in the database.\n\nDataTableColumns (string) --A comma-separated list of column names.\n\nCopyOptions (string) --Optional parameters to use with the Amazon Redshift COPY command. For more information, see the 'Optional Parameters' section of Amazon Redshift COPY command . Some possible examples that would apply to Kinesis Data Firehose are as follows:\n\ndelimiter \'\\t\' lzop; - fields are delimited with 't' (TAB character) and compressed using lzop.delimiter \'|\' - fields are delimited with '|' (this is the default delimiter).\ndelimiter \'|\' escape - the delimiter should be escaped.\nfixedwidth \'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6\' - fields are fixed width in the source, with each width specified after every column in the table.\nJSON \'s3://mybucket/jsonpaths.txt\' - data is in JSON format, and the path specified is the format of the data.\n\nFor more examples, see Amazon Redshift COPY command examples .\n\n\n\nUsername (string) --The name of the user.\n\nPassword (string) --The user password.\n\nRetryOptions (dict) --The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).\n\nDurationInSeconds (integer) --The length of time during which Kinesis Data Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Kinesis Data Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value.\n\n\n\nS3Update (dict) --The Amazon S3 destination.\nThe compression formats SNAPPY or ZIP cannot be specified in RedshiftDestinationUpdate.S3Update because the Amazon Redshift COPY operation that reads from the S3 bucket doesn\'t support these compression formats.\n\nRoleARN (string) --The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nBucketARN (string) --The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nPrefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .\n\nErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .\n\nBufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.\n\n\n\nCompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .\nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.\n\nEncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.\n\nNoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.\n\nKMSEncryptionConfig (dict) --The encryption key.\n\nAWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n\nProcessingConfiguration (dict) --The data processing configuration.\n\nEnabled (boolean) --Enables or disables data processing.\n\nProcessors (list) --The data processors.\n\n(dict) --Describes a data processor.\n\nType (string) -- [REQUIRED]The type of processor.\n\nParameters (list) --The processor parameters.\n\n(dict) --Describes the processor parameter.\n\nParameterName (string) -- [REQUIRED]The name of the parameter.\n\nParameterValue (string) -- [REQUIRED]The parameter value.\n\n\n\n\n\n\n\n\n\n\n\nS3BackupMode (string) --The Amazon S3 backup mode.\n\nS3BackupUpdate (dict) --The Amazon S3 destination for backup.\n\nRoleARN (string) --The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nBucketARN (string) --The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nPrefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .\n\nErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .\n\nBufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.\n\n\n\nCompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .\nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.\n\nEncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.\n\nNoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.\n\nKMSEncryptionConfig (dict) --The encryption key.\n\nAWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The Amazon CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n

    :type ElasticsearchDestinationUpdate: dict
    :param ElasticsearchDestinationUpdate: Describes an update for a destination in Amazon ES.\n\nRoleARN (string) --The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon ES Configuration API and for indexing documents. For more information, see Grant Kinesis Data Firehose Access to an Amazon S3 Destination and Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nDomainARN (string) --The ARN of the Amazon ES domain. The IAM role must have permissions for DescribeElasticsearchDomain , DescribeElasticsearchDomains , and DescribeElasticsearchDomainConfig after assuming the IAM role specified in RoleARN . For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\nSpecify either ClusterEndpoint or DomainARN .\n\nClusterEndpoint (string) --The endpoint to use when communicating with the cluster. Specify either this ClusterEndpoint or the DomainARN field.\n\nIndexName (string) --The Elasticsearch index name.\n\nTypeName (string) --The Elasticsearch type name. For Elasticsearch 6.x, there can be only one type per index. If you try to specify a new type for an existing index that already has another type, Kinesis Data Firehose returns an error during runtime.\nIf you upgrade Elasticsearch from 6.x to 7.x and don\xe2\x80\x99t update your delivery stream, Kinesis Data Firehose still delivers data to Elasticsearch with the old index name and type name. If you want to update your delivery stream with a new index name, provide an empty string for TypeName .\n\nIndexRotationPeriod (string) --The Elasticsearch index rotation period. Index rotation appends a timestamp to IndexName to facilitate the expiration of old data. For more information, see Index Rotation for the Amazon ES Destination . Default value is OneDay .\n\nBufferingHints (dict) --The buffering options. If no value is specified, ElasticsearchBufferingHints object default values are used.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.\n\n\n\nRetryOptions (dict) --The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon ES. The default value is 300 (5 minutes).\n\nDurationInSeconds (integer) --After an initial failure to deliver to Amazon ES, the total amount of time during which Kinesis Data Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.\n\n\n\nS3Update (dict) --The Amazon S3 destination.\n\nRoleARN (string) --The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nBucketARN (string) --The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nPrefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .\n\nErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .\n\nBufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.\n\n\n\nCompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .\nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.\n\nEncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.\n\nNoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.\n\nKMSEncryptionConfig (dict) --The encryption key.\n\nAWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n\nProcessingConfiguration (dict) --The data processing configuration.\n\nEnabled (boolean) --Enables or disables data processing.\n\nProcessors (list) --The data processors.\n\n(dict) --Describes a data processor.\n\nType (string) -- [REQUIRED]The type of processor.\n\nParameters (list) --The processor parameters.\n\n(dict) --Describes the processor parameter.\n\nParameterName (string) -- [REQUIRED]The name of the parameter.\n\nParameterValue (string) -- [REQUIRED]The parameter value.\n\n\n\n\n\n\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n

    :type SplunkDestinationUpdate: dict
    :param SplunkDestinationUpdate: Describes an update for a destination in Splunk.\n\nHECEndpoint (string) --The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your data.\n\nHECEndpointType (string) --This type can be either 'Raw' or 'Event.'\n\nHECToken (string) --A GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.\n\nHECAcknowledgmentTimeoutInSeconds (integer) --The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from Splunk after it sends data. At the end of the timeout period, Kinesis Data Firehose either tries to send the data again or considers it an error, based on your retry settings.\n\nRetryOptions (dict) --The retry behavior in case Kinesis Data Firehose is unable to deliver data to Splunk or if it doesn\'t receive an acknowledgment of receipt from Splunk.\n\nDurationInSeconds (integer) --The total amount of time that Kinesis Data Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesn\'t include the periods during which Kinesis Data Firehose waits for acknowledgment from Splunk after each attempt.\n\n\n\nS3BackupMode (string) --Defines how documents should be delivered to Amazon S3. When set to FailedDocumentsOnly , Kinesis Data Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to AllDocuments , Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. Default value is FailedDocumentsOnly .\n\nS3Update (dict) --Your update to the configuration of the backup Amazon S3 location.\n\nRoleARN (string) --The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nBucketARN (string) --The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nPrefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in Custom Prefixes for Amazon S3 Objects .\n\nErrorOutputPrefix (string) --A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see Custom Prefixes for Amazon S3 Objects .\n\nBufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.\n\nSizeInMBs (integer) --Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for IntervalInSeconds , and vice versa.\nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.\n\nIntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for SizeInMBs , and vice versa.\n\n\n\nCompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .\nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.\n\nEncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.\n\nNoEncryptionConfig (string) --Specifically override existing encryption information to ensure that no encryption is used.\n\nKMSEncryptionConfig (dict) --The encryption key.\n\nAWSKMSKeyARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n\nProcessingConfiguration (dict) --The data processing configuration.\n\nEnabled (boolean) --Enables or disables data processing.\n\nProcessors (list) --The data processors.\n\n(dict) --Describes a data processor.\n\nType (string) -- [REQUIRED]The type of processor.\n\nParameters (list) --The processor parameters.\n\n(dict) --Describes the processor parameter.\n\nParameterName (string) -- [REQUIRED]The name of the parameter.\n\nParameterValue (string) -- [REQUIRED]The parameter value.\n\n\n\n\n\n\n\n\n\n\n\nCloudWatchLoggingOptions (dict) --The Amazon CloudWatch logging options for your delivery stream.\n\nEnabled (boolean) --Enables or disables CloudWatch logging.\n\nLogGroupName (string) --The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.\n\nLogStreamName (string) --The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Firehose.Client.exceptions.InvalidArgumentException
Firehose.Client.exceptions.ResourceInUseException
Firehose.Client.exceptions.ResourceNotFoundException
Firehose.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

