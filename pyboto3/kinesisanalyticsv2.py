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

def add_application_cloud_watch_logging_option(ApplicationName=None, CurrentApplicationVersionId=None, CloudWatchLoggingOption=None):
    """
    Adds an Amazon CloudWatch log stream to monitor application configuration errors.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_application_cloud_watch_logging_option(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        CloudWatchLoggingOption={
            'LogStreamARN': 'string'
        }
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe Kinesis Data Analytics application name.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe version ID of the Kinesis Data Analytics application. You can retrieve the application version ID using DescribeApplication .\n

    :type CloudWatchLoggingOption: dict
    :param CloudWatchLoggingOption: [REQUIRED]\nProvides the Amazon CloudWatch log stream Amazon Resource Name (ARN).\n\nLogStreamARN (string) -- [REQUIRED]The ARN of the CloudWatch log to receive application messages.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationARN': 'string',
    'ApplicationVersionId': 123,
    'CloudWatchLoggingOptionDescriptions': [
        {
            'CloudWatchLoggingOptionId': 'string',
            'LogStreamARN': 'string',
            'RoleARN': 'string'
        },
    ]
}


Response Structure

(dict) --

ApplicationARN (string) --
The application\'s ARN.

ApplicationVersionId (integer) --
The new version ID of the Kinesis Data Analytics application. Kinesis Data Analytics updates the ApplicationVersionId each time you change the CloudWatch logging options.

CloudWatchLoggingOptionDescriptions (list) --
The descriptions of the current CloudWatch logging options for the Kinesis Data Analytics application.

(dict) --
Describes the Amazon CloudWatch logging option.

CloudWatchLoggingOptionId (string) --
The ID of the CloudWatch logging option description.

LogStreamARN (string) --
The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

RoleARN (string) --
The IAM ARN of the role to use to send application messages.

Note
Provided for backward compatibility. Applications created with the current API version have an application-level service execution role rather than a resource-level role.












Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
KinesisAnalyticsV2.Client.exceptions.InvalidApplicationConfigurationException


    :return: {
        'ApplicationARN': 'string',
        'ApplicationVersionId': 123,
        'CloudWatchLoggingOptionDescriptions': [
            {
                'CloudWatchLoggingOptionId': 'string',
                'LogStreamARN': 'string',
                'RoleARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
    KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
    KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
    KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
    KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
    KinesisAnalyticsV2.Client.exceptions.InvalidApplicationConfigurationException
    
    """
    pass

def add_application_input(ApplicationName=None, CurrentApplicationVersionId=None, Input=None):
    """
    Adds a streaming source to your SQL-based Amazon Kinesis Data Analytics application.
    You can add a streaming source when you create an application, or you can use this operation to add a streaming source after you create an application. For more information, see  CreateApplication .
    Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the  DescribeApplication operation to find the current application version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_application_input(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        Input={
            'NamePrefix': 'string',
            'InputProcessingConfiguration': {
                'InputLambdaProcessor': {
                    'ResourceARN': 'string'
                }
            },
            'KinesisStreamsInput': {
                'ResourceARN': 'string'
            },
            'KinesisFirehoseInput': {
                'ResourceARN': 'string'
            },
            'InputParallelism': {
                'Count': 123
            },
            'InputSchema': {
                'RecordFormat': {
                    'RecordFormatType': 'JSON'|'CSV',
                    'MappingParameters': {
                        'JSONMappingParameters': {
                            'RecordRowPath': 'string'
                        },
                        'CSVMappingParameters': {
                            'RecordRowDelimiter': 'string',
                            'RecordColumnDelimiter': 'string'
                        }
                    }
                },
                'RecordEncoding': 'string',
                'RecordColumns': [
                    {
                        'Name': 'string',
                        'Mapping': 'string',
                        'SqlType': 'string'
                    },
                ]
            }
        }
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of your existing application to which you want to add the streaming source.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe current version of your application. You can use the DescribeApplication operation to find the current application version.\n

    :type Input: dict
    :param Input: [REQUIRED]\nThe Input to add.\n\nNamePrefix (string) -- [REQUIRED]The name prefix to use when creating an in-application stream. Suppose that you specify a prefix 'MyInApplicationStream .' Kinesis Data Analytics then creates one or more (as per the InputParallelism count you specified) in-application streams with the names 'MyInApplicationStream_001 ,' 'MyInApplicationStream_002 ,' and so on.\n\nInputProcessingConfiguration (dict) --The InputProcessingConfiguration for the input. An input processor transforms records as they are received from the stream, before the application\'s SQL code executes. Currently, the only input processing configuration available is InputLambdaProcessor .\n\nInputLambdaProcessor (dict) -- [REQUIRED]The InputLambdaProcessor that is used to preprocess the records in the stream before being processed by your application code.\n\nResourceARN (string) -- [REQUIRED]The ARN of the AWS Lambda function that operates on records in the stream.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\n\n\n\n\nKinesisStreamsInput (dict) --If the streaming source is an Amazon Kinesis data stream, identifies the stream\'s Amazon Resource Name (ARN).\n\nResourceARN (string) -- [REQUIRED]The ARN of the input Kinesis data stream to read.\n\n\n\nKinesisFirehoseInput (dict) --If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies the delivery stream\'s ARN.\n\nResourceARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the delivery stream.\n\n\n\nInputParallelism (dict) --Describes the number of in-application streams to create.\n\nCount (integer) --The number of in-application streams to create.\n\n\n\nInputSchema (dict) -- [REQUIRED]Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.\nAlso used to describe the format of the reference data source.\n\nRecordFormat (dict) -- [REQUIRED]Specifies the format of the records on the streaming source.\n\nRecordFormatType (string) -- [REQUIRED]The type of record format.\n\nMappingParameters (dict) --When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.\n\nJSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.\n\nRecordRowPath (string) -- [REQUIRED]The path to the top-level parent that contains the records.\n\n\n\nCSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).\n\nRecordRowDelimiter (string) -- [REQUIRED]The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.\n\nRecordColumnDelimiter (string) -- [REQUIRED]The column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.\n\n\n\n\n\n\n\nRecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.\n\nRecordColumns (list) -- [REQUIRED]A list of RecordColumn objects.\n\n(dict) --For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.\nAlso used to describe the format of the reference data source.\n\nName (string) -- [REQUIRED]The name of the column that is created in the in-application input stream or reference table.\n\nMapping (string) --A reference to the data element in the streaming input or the reference data source.\n\nSqlType (string) -- [REQUIRED]The type of column created in the in-application input stream or reference table.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationARN': 'string',
    'ApplicationVersionId': 123,
    'InputDescriptions': [
        {
            'InputId': 'string',
            'NamePrefix': 'string',
            'InAppStreamNames': [
                'string',
            ],
            'InputProcessingConfigurationDescription': {
                'InputLambdaProcessorDescription': {
                    'ResourceARN': 'string',
                    'RoleARN': 'string'
                }
            },
            'KinesisStreamsInputDescription': {
                'ResourceARN': 'string',
                'RoleARN': 'string'
            },
            'KinesisFirehoseInputDescription': {
                'ResourceARN': 'string',
                'RoleARN': 'string'
            },
            'InputSchema': {
                'RecordFormat': {
                    'RecordFormatType': 'JSON'|'CSV',
                    'MappingParameters': {
                        'JSONMappingParameters': {
                            'RecordRowPath': 'string'
                        },
                        'CSVMappingParameters': {
                            'RecordRowDelimiter': 'string',
                            'RecordColumnDelimiter': 'string'
                        }
                    }
                },
                'RecordEncoding': 'string',
                'RecordColumns': [
                    {
                        'Name': 'string',
                        'Mapping': 'string',
                        'SqlType': 'string'
                    },
                ]
            },
            'InputParallelism': {
                'Count': 123
            },
            'InputStartingPositionConfiguration': {
                'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
            }
        },
    ]
}


Response Structure

(dict) --

ApplicationARN (string) --
The Amazon Resource Name (ARN) of the application.

ApplicationVersionId (integer) --
Provides the current application version.

InputDescriptions (list) --
Describes the application input configuration.

(dict) --
Describes the application input configuration for an SQL-based Amazon Kinesis Data Analytics application.

InputId (string) --
The input ID that is associated with the application input. This is the ID that Kinesis Data Analytics assigns to each input configuration that you add to your application.

NamePrefix (string) --
The in-application name prefix.

InAppStreamNames (list) --
Returns the in-application stream names that are mapped to the stream source.

(string) --


InputProcessingConfigurationDescription (dict) --
The description of the preprocessor that executes on records in this input before the application\'s code is run.

InputLambdaProcessorDescription (dict) --
Provides configuration information about the associated  InputLambdaProcessorDescription

ResourceARN (string) --
The ARN of the AWS Lambda function that is used to preprocess the records in the stream.

Note
To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda


RoleARN (string) --
The ARN of the IAM role that is used to access the AWS Lambda function.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.






KinesisStreamsInputDescription (dict) --
If a Kinesis data stream is configured as a streaming source, provides the Kinesis data stream\'s Amazon Resource Name (ARN).

ResourceARN (string) --
The Amazon Resource Name (ARN) of the Kinesis data stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




KinesisFirehoseInputDescription (dict) --
If a Kinesis Data Firehose delivery stream is configured as a streaming source, provides the delivery stream\'s ARN.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the delivery stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




InputSchema (dict) --
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.

RecordFormat (dict) --
Specifies the format of the records on the streaming source.

RecordFormatType (string) --
The type of record format.

MappingParameters (dict) --
When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters (dict) --
Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath (string) --
The path to the top-level parent that contains the records.



CSVMappingParameters (dict) --
Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter (string) --
The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.

RecordColumnDelimiter (string) --
The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.







RecordEncoding (string) --
Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns (list) --
A list of RecordColumn objects.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
Also used to describe the format of the reference data source.

Name (string) --
The name of the column that is created in the in-application input stream or reference table.

Mapping (string) --
A reference to the data element in the streaming input or the reference data source.

SqlType (string) --
The type of column created in the in-application input stream or reference table.







InputParallelism (dict) --
Describes the configured parallelism (number of in-application streams mapped to the streaming source).

Count (integer) --
The number of in-application streams to create.



InputStartingPositionConfiguration (dict) --
The point at which the application is configured to read from the input stream.

InputStartingPosition (string) --
The starting position on the stream.

NOW - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued.
TRIM_HORIZON - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream.
LAST_STOPPED_POINT - Resume reading from where the application last stopped reading.














Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
KinesisAnalyticsV2.Client.exceptions.CodeValidationException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException


    :return: {
        'ApplicationARN': 'string',
        'ApplicationVersionId': 123,
        'InputDescriptions': [
            {
                'InputId': 'string',
                'NamePrefix': 'string',
                'InAppStreamNames': [
                    'string',
                ],
                'InputProcessingConfigurationDescription': {
                    'InputLambdaProcessorDescription': {
                        'ResourceARN': 'string',
                        'RoleARN': 'string'
                    }
                },
                'KinesisStreamsInputDescription': {
                    'ResourceARN': 'string',
                    'RoleARN': 'string'
                },
                'KinesisFirehoseInputDescription': {
                    'ResourceARN': 'string',
                    'RoleARN': 'string'
                },
                'InputSchema': {
                    'RecordFormat': {
                        'RecordFormatType': 'JSON'|'CSV',
                        'MappingParameters': {
                            'JSONMappingParameters': {
                                'RecordRowPath': 'string'
                            },
                            'CSVMappingParameters': {
                                'RecordRowDelimiter': 'string',
                                'RecordColumnDelimiter': 'string'
                            }
                        }
                    },
                    'RecordEncoding': 'string',
                    'RecordColumns': [
                        {
                            'Name': 'string',
                            'Mapping': 'string',
                            'SqlType': 'string'
                        },
                    ]
                },
                'InputParallelism': {
                    'Count': 123
                },
                'InputStartingPositionConfiguration': {
                    'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def add_application_input_processing_configuration(ApplicationName=None, CurrentApplicationVersionId=None, InputId=None, InputProcessingConfiguration=None):
    """
    Adds an  InputProcessingConfiguration to an SQL-based Kinesis Data Analytics application. An input processor pre-processes records on the input stream before the application\'s SQL code executes. Currently, the only input processor available is AWS Lambda .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_application_input_processing_configuration(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        InputId='string',
        InputProcessingConfiguration={
            'InputLambdaProcessor': {
                'ResourceARN': 'string'
            }
        }
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of the application to which you want to add the input processing configuration.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe version of the application to which you want to add the input processing configuration. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.\n

    :type InputId: string
    :param InputId: [REQUIRED]\nThe ID of the input configuration to add the input processing configuration to. You can get a list of the input IDs for an application using the DescribeApplication operation.\n

    :type InputProcessingConfiguration: dict
    :param InputProcessingConfiguration: [REQUIRED]\nThe InputProcessingConfiguration to add to the application.\n\nInputLambdaProcessor (dict) -- [REQUIRED]The InputLambdaProcessor that is used to preprocess the records in the stream before being processed by your application code.\n\nResourceARN (string) -- [REQUIRED]The ARN of the AWS Lambda function that operates on records in the stream.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationARN': 'string',
    'ApplicationVersionId': 123,
    'InputId': 'string',
    'InputProcessingConfigurationDescription': {
        'InputLambdaProcessorDescription': {
            'ResourceARN': 'string',
            'RoleARN': 'string'
        }
    }
}


Response Structure

(dict) --

ApplicationARN (string) --
The Amazon Resource Name (ARN) of the application.

ApplicationVersionId (integer) --
Provides the current application version.

InputId (string) --
The input ID that is associated with the application input. This is the ID that Amazon Kinesis Data Analytics assigns to each input configuration that you add to your application.

InputProcessingConfigurationDescription (dict) --
The description of the preprocessor that executes on records in this input before the application\'s code is run.

InputLambdaProcessorDescription (dict) --
Provides configuration information about the associated  InputLambdaProcessorDescription

ResourceARN (string) --
The ARN of the AWS Lambda function that is used to preprocess the records in the stream.

Note
To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda


RoleARN (string) --
The ARN of the IAM role that is used to access the AWS Lambda function.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.












Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException


    :return: {
        'ApplicationARN': 'string',
        'ApplicationVersionId': 123,
        'InputId': 'string',
        'InputProcessingConfigurationDescription': {
            'InputLambdaProcessorDescription': {
                'ResourceARN': 'string',
                'RoleARN': 'string'
            }
        }
    }
    
    
    :returns: 
    KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
    KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
    KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
    KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
    KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
    
    """
    pass

def add_application_output(ApplicationName=None, CurrentApplicationVersionId=None, Output=None):
    """
    Adds an external destination to your SQL-based Amazon Kinesis Data Analytics application.
    If you want Kinesis Data Analytics to deliver data from an in-application stream within your application to an external destination (such as an Kinesis data stream, a Kinesis Data Firehose delivery stream, or an AWS Lambda function), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.
    You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors.
    Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the  DescribeApplication operation to find the current application version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_application_output(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        Output={
            'Name': 'string',
            'KinesisStreamsOutput': {
                'ResourceARN': 'string'
            },
            'KinesisFirehoseOutput': {
                'ResourceARN': 'string'
            },
            'LambdaOutput': {
                'ResourceARN': 'string'
            },
            'DestinationSchema': {
                'RecordFormatType': 'JSON'|'CSV'
            }
        }
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of the application to which you want to add the output configuration.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe version of the application to which you want to add the output configuration. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.\n

    :type Output: dict
    :param Output: [REQUIRED]\nAn array of objects, each describing one output configuration. In the output configuration, you specify the name of an in-application stream, a destination (that is, a Kinesis data stream, a Kinesis Data Firehose delivery stream, or an AWS Lambda function), and record the formation to use when writing to the destination.\n\nName (string) -- [REQUIRED]The name of the in-application stream.\n\nKinesisStreamsOutput (dict) --Identifies an Amazon Kinesis data stream as the destination.\n\nResourceARN (string) -- [REQUIRED]The ARN of the destination Kinesis data stream to write to.\n\n\n\nKinesisFirehoseOutput (dict) --Identifies an Amazon Kinesis Data Firehose delivery stream as the destination.\n\nResourceARN (string) -- [REQUIRED]The ARN of the destination delivery stream to write to.\n\n\n\nLambdaOutput (dict) --Identifies an AWS Lambda function as the destination.\n\nResourceARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the destination Lambda function to write to.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\n\n\nDestinationSchema (dict) -- [REQUIRED]Describes the data format when records are written to the destination.\n\nRecordFormatType (string) -- [REQUIRED]Specifies the format of the records on the output stream.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationARN': 'string',
    'ApplicationVersionId': 123,
    'OutputDescriptions': [
        {
            'OutputId': 'string',
            'Name': 'string',
            'KinesisStreamsOutputDescription': {
                'ResourceARN': 'string',
                'RoleARN': 'string'
            },
            'KinesisFirehoseOutputDescription': {
                'ResourceARN': 'string',
                'RoleARN': 'string'
            },
            'LambdaOutputDescription': {
                'ResourceARN': 'string',
                'RoleARN': 'string'
            },
            'DestinationSchema': {
                'RecordFormatType': 'JSON'|'CSV'
            }
        },
    ]
}


Response Structure

(dict) --

ApplicationARN (string) --
The application Amazon Resource Name (ARN).

ApplicationVersionId (integer) --
The updated application version ID. Kinesis Data Analytics increments this ID when the application is updated.

OutputDescriptions (list) --
Describes the application output configuration. For more information, see Configuring Application Output .

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

OutputId (string) --
A unique identifier for the output configuration.

Name (string) --
The name of the in-application stream that is configured as output.

KinesisStreamsOutputDescription (dict) --
Describes the Kinesis data stream that is configured as the destination where output is written.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the Kinesis data stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




KinesisFirehoseOutputDescription (dict) --
Describes the Kinesis Data Firehose delivery stream that is configured as the destination where output is written.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the delivery stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




LambdaOutputDescription (dict) --
Describes the Lambda function that is configured as the destination where output is written.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the destination Lambda function.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to write to the destination function.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




DestinationSchema (dict) --
The data format used for writing data to the destination.

RecordFormatType (string) --
Specifies the format of the records on the output stream.













Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException


    :return: {
        'ApplicationARN': 'string',
        'ApplicationVersionId': 123,
        'OutputDescriptions': [
            {
                'OutputId': 'string',
                'Name': 'string',
                'KinesisStreamsOutputDescription': {
                    'ResourceARN': 'string',
                    'RoleARN': 'string'
                },
                'KinesisFirehoseOutputDescription': {
                    'ResourceARN': 'string',
                    'RoleARN': 'string'
                },
                'LambdaOutputDescription': {
                    'ResourceARN': 'string',
                    'RoleARN': 'string'
                },
                'DestinationSchema': {
                    'RecordFormatType': 'JSON'|'CSV'
                }
            },
        ]
    }
    
    
    :returns: 
    KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
    KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
    KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
    KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
    KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
    
    """
    pass

def add_application_reference_data_source(ApplicationName=None, CurrentApplicationVersionId=None, ReferenceDataSource=None):
    """
    Adds a reference data source to an existing SQL-based Amazon Kinesis Data Analytics application.
    Kinesis Data Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in an Amazon S3 object maps to columns in the resulting in-application table.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_application_reference_data_source(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        ReferenceDataSource={
            'TableName': 'string',
            'S3ReferenceDataSource': {
                'BucketARN': 'string',
                'FileKey': 'string'
            },
            'ReferenceSchema': {
                'RecordFormat': {
                    'RecordFormatType': 'JSON'|'CSV',
                    'MappingParameters': {
                        'JSONMappingParameters': {
                            'RecordRowPath': 'string'
                        },
                        'CSVMappingParameters': {
                            'RecordRowDelimiter': 'string',
                            'RecordColumnDelimiter': 'string'
                        }
                    }
                },
                'RecordEncoding': 'string',
                'RecordColumns': [
                    {
                        'Name': 'string',
                        'Mapping': 'string',
                        'SqlType': 'string'
                    },
                ]
            }
        }
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of an existing application.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe version of the application for which you are adding the reference data source. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.\n

    :type ReferenceDataSource: dict
    :param ReferenceDataSource: [REQUIRED]\nThe reference data source can be an object in your Amazon S3 bucket. Kinesis Data Analytics reads the object and copies the data into the in-application table that is created. You provide an S3 bucket, object key name, and the resulting in-application table that is created.\n\nTableName (string) -- [REQUIRED]The name of the in-application table to create.\n\nS3ReferenceDataSource (dict) --Identifies the S3 bucket and object that contains the reference data. A Kinesis Data Analytics application loads reference data only once. If the data changes, you call the UpdateApplication operation to trigger reloading of data into your application.\n\nBucketARN (string) --The Amazon Resource Name (ARN) of the S3 bucket.\n\nFileKey (string) --The object key name containing the reference data.\n\n\n\nReferenceSchema (dict) -- [REQUIRED]Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.\n\nRecordFormat (dict) -- [REQUIRED]Specifies the format of the records on the streaming source.\n\nRecordFormatType (string) -- [REQUIRED]The type of record format.\n\nMappingParameters (dict) --When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.\n\nJSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.\n\nRecordRowPath (string) -- [REQUIRED]The path to the top-level parent that contains the records.\n\n\n\nCSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).\n\nRecordRowDelimiter (string) -- [REQUIRED]The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.\n\nRecordColumnDelimiter (string) -- [REQUIRED]The column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.\n\n\n\n\n\n\n\nRecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.\n\nRecordColumns (list) -- [REQUIRED]A list of RecordColumn objects.\n\n(dict) --For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.\nAlso used to describe the format of the reference data source.\n\nName (string) -- [REQUIRED]The name of the column that is created in the in-application input stream or reference table.\n\nMapping (string) --A reference to the data element in the streaming input or the reference data source.\n\nSqlType (string) -- [REQUIRED]The type of column created in the in-application input stream or reference table.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationARN': 'string',
    'ApplicationVersionId': 123,
    'ReferenceDataSourceDescriptions': [
        {
            'ReferenceId': 'string',
            'TableName': 'string',
            'S3ReferenceDataSourceDescription': {
                'BucketARN': 'string',
                'FileKey': 'string',
                'ReferenceRoleARN': 'string'
            },
            'ReferenceSchema': {
                'RecordFormat': {
                    'RecordFormatType': 'JSON'|'CSV',
                    'MappingParameters': {
                        'JSONMappingParameters': {
                            'RecordRowPath': 'string'
                        },
                        'CSVMappingParameters': {
                            'RecordRowDelimiter': 'string',
                            'RecordColumnDelimiter': 'string'
                        }
                    }
                },
                'RecordEncoding': 'string',
                'RecordColumns': [
                    {
                        'Name': 'string',
                        'Mapping': 'string',
                        'SqlType': 'string'
                    },
                ]
            }
        },
    ]
}


Response Structure

(dict) --

ApplicationARN (string) --
The application Amazon Resource Name (ARN).

ApplicationVersionId (integer) --
The updated application version ID. Amazon Kinesis Data Analytics increments this ID when the application is updated.

ReferenceDataSourceDescriptions (list) --
Describes reference data sources configured for the application.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data source configured for an application.

ReferenceId (string) --
The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns when you add the reference data source to your application using the  CreateApplication or  UpdateApplication operation.

TableName (string) --
The in-application table name created by the specific reference data source configuration.

S3ReferenceDataSourceDescription (dict) --
Provides the Amazon S3 bucket name, the object key name that contains the reference data.

BucketARN (string) --
The Amazon Resource Name (ARN) of the S3 bucket.

FileKey (string) --
Amazon S3 object key name.

ReferenceRoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




ReferenceSchema (dict) --
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

RecordFormat (dict) --
Specifies the format of the records on the streaming source.

RecordFormatType (string) --
The type of record format.

MappingParameters (dict) --
When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters (dict) --
Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath (string) --
The path to the top-level parent that contains the records.



CSVMappingParameters (dict) --
Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter (string) --
The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.

RecordColumnDelimiter (string) --
The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.







RecordEncoding (string) --
Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns (list) --
A list of RecordColumn objects.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
Also used to describe the format of the reference data source.

Name (string) --
The name of the column that is created in the in-application input stream or reference table.

Mapping (string) --
A reference to the data element in the streaming input or the reference data source.

SqlType (string) --
The type of column created in the in-application input stream or reference table.

















Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException


    :return: {
        'ApplicationARN': 'string',
        'ApplicationVersionId': 123,
        'ReferenceDataSourceDescriptions': [
            {
                'ReferenceId': 'string',
                'TableName': 'string',
                'S3ReferenceDataSourceDescription': {
                    'BucketARN': 'string',
                    'FileKey': 'string',
                    'ReferenceRoleARN': 'string'
                },
                'ReferenceSchema': {
                    'RecordFormat': {
                        'RecordFormatType': 'JSON'|'CSV',
                        'MappingParameters': {
                            'JSONMappingParameters': {
                                'RecordRowPath': 'string'
                            },
                            'CSVMappingParameters': {
                                'RecordRowDelimiter': 'string',
                                'RecordColumnDelimiter': 'string'
                            }
                        }
                    },
                    'RecordEncoding': 'string',
                    'RecordColumns': [
                        {
                            'Name': 'string',
                            'Mapping': 'string',
                            'SqlType': 'string'
                        },
                    ]
                }
            },
        ]
    }
    
    
    :returns: 
    KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
    KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
    KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
    KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
    KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
    
    """
    pass

def add_application_vpc_configuration(ApplicationName=None, CurrentApplicationVersionId=None, VpcConfiguration=None):
    """
    Adds a Virtual Private Cloud (VPC) configuration to the application. Applications can use VPCs to store and access resources securely.
    Note the following about VPC configurations for Kinesis Data Analytics applications:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_application_vpc_configuration(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        VpcConfiguration={
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        }
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of an existing application.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe version of the application to which you want to add the input processing configuration. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.\n

    :type VpcConfiguration: dict
    :param VpcConfiguration: [REQUIRED]\nDescription of the VPC to add to the application.\n\nSubnetIds (list) -- [REQUIRED]The array of Subnet IDs used by the VPC configuration.\n\n(string) --\n\n\nSecurityGroupIds (list) -- [REQUIRED]The array of SecurityGroup IDs used by the VPC configuration.\n\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationARN': 'string',
    'ApplicationVersionId': 123,
    'VpcConfigurationDescription': {
        'VpcConfigurationId': 'string',
        'VpcId': 'string',
        'SubnetIds': [
            'string',
        ],
        'SecurityGroupIds': [
            'string',
        ]
    }
}


Response Structure

(dict) --

ApplicationARN (string) --
The ARN of the application.

ApplicationVersionId (integer) --
Provides the current application version. Kinesis Data Analytics updates the ApplicationVersionId each time you update the application.

VpcConfigurationDescription (dict) --
The parameters of the new VPC configuration.

VpcConfigurationId (string) --
The ID of the VPC configuration.

VpcId (string) --
The ID of the associated VPC.

SubnetIds (list) --
The array of Subnet IDs used by the VPC configuration.

(string) --


SecurityGroupIds (list) --
The array of SecurityGroup IDs used by the VPC configuration.

(string) --










Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException


    :return: {
        'ApplicationARN': 'string',
        'ApplicationVersionId': 123,
        'VpcConfigurationDescription': {
            'VpcConfigurationId': 'string',
            'VpcId': 'string',
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    ApplicationName (string) -- [REQUIRED]
    The name of an existing application.
    
    CurrentApplicationVersionId (integer) -- [REQUIRED]
    The version of the application to which you want to add the input processing configuration. You can use the  DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.
    
    VpcConfiguration (dict) -- [REQUIRED]
    Description of the VPC to add to the application.
    
    SubnetIds (list) -- [REQUIRED]The array of Subnet IDs used by the VPC configuration.
    
    (string) --
    
    
    SecurityGroupIds (list) -- [REQUIRED]The array of SecurityGroup IDs used by the VPC configuration.
    
    (string) --
    
    
    
    
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_application(ApplicationName=None, ApplicationDescription=None, RuntimeEnvironment=None, ServiceExecutionRole=None, ApplicationConfiguration=None, CloudWatchLoggingOptions=None, Tags=None):
    """
    Creates an Amazon Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see Creating an Application .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_application(
        ApplicationName='string',
        ApplicationDescription='string',
        RuntimeEnvironment='SQL-1_0'|'FLINK-1_6'|'FLINK-1_8',
        ServiceExecutionRole='string',
        ApplicationConfiguration={
            'SqlApplicationConfiguration': {
                'Inputs': [
                    {
                        'NamePrefix': 'string',
                        'InputProcessingConfiguration': {
                            'InputLambdaProcessor': {
                                'ResourceARN': 'string'
                            }
                        },
                        'KinesisStreamsInput': {
                            'ResourceARN': 'string'
                        },
                        'KinesisFirehoseInput': {
                            'ResourceARN': 'string'
                        },
                        'InputParallelism': {
                            'Count': 123
                        },
                        'InputSchema': {
                            'RecordFormat': {
                                'RecordFormatType': 'JSON'|'CSV',
                                'MappingParameters': {
                                    'JSONMappingParameters': {
                                        'RecordRowPath': 'string'
                                    },
                                    'CSVMappingParameters': {
                                        'RecordRowDelimiter': 'string',
                                        'RecordColumnDelimiter': 'string'
                                    }
                                }
                            },
                            'RecordEncoding': 'string',
                            'RecordColumns': [
                                {
                                    'Name': 'string',
                                    'Mapping': 'string',
                                    'SqlType': 'string'
                                },
                            ]
                        }
                    },
                ],
                'Outputs': [
                    {
                        'Name': 'string',
                        'KinesisStreamsOutput': {
                            'ResourceARN': 'string'
                        },
                        'KinesisFirehoseOutput': {
                            'ResourceARN': 'string'
                        },
                        'LambdaOutput': {
                            'ResourceARN': 'string'
                        },
                        'DestinationSchema': {
                            'RecordFormatType': 'JSON'|'CSV'
                        }
                    },
                ],
                'ReferenceDataSources': [
                    {
                        'TableName': 'string',
                        'S3ReferenceDataSource': {
                            'BucketARN': 'string',
                            'FileKey': 'string'
                        },
                        'ReferenceSchema': {
                            'RecordFormat': {
                                'RecordFormatType': 'JSON'|'CSV',
                                'MappingParameters': {
                                    'JSONMappingParameters': {
                                        'RecordRowPath': 'string'
                                    },
                                    'CSVMappingParameters': {
                                        'RecordRowDelimiter': 'string',
                                        'RecordColumnDelimiter': 'string'
                                    }
                                }
                            },
                            'RecordEncoding': 'string',
                            'RecordColumns': [
                                {
                                    'Name': 'string',
                                    'Mapping': 'string',
                                    'SqlType': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'FlinkApplicationConfiguration': {
                'CheckpointConfiguration': {
                    'ConfigurationType': 'DEFAULT'|'CUSTOM',
                    'CheckpointingEnabled': True|False,
                    'CheckpointInterval': 123,
                    'MinPauseBetweenCheckpoints': 123
                },
                'MonitoringConfiguration': {
                    'ConfigurationType': 'DEFAULT'|'CUSTOM',
                    'MetricsLevel': 'APPLICATION'|'TASK'|'OPERATOR'|'PARALLELISM',
                    'LogLevel': 'INFO'|'WARN'|'ERROR'|'DEBUG'
                },
                'ParallelismConfiguration': {
                    'ConfigurationType': 'DEFAULT'|'CUSTOM',
                    'Parallelism': 123,
                    'ParallelismPerKPU': 123,
                    'AutoScalingEnabled': True|False
                }
            },
            'EnvironmentProperties': {
                'PropertyGroups': [
                    {
                        'PropertyGroupId': 'string',
                        'PropertyMap': {
                            'string': 'string'
                        }
                    },
                ]
            },
            'ApplicationCodeConfiguration': {
                'CodeContent': {
                    'TextContent': 'string',
                    'ZipFileContent': b'bytes',
                    'S3ContentLocation': {
                        'BucketARN': 'string',
                        'FileKey': 'string',
                        'ObjectVersion': 'string'
                    }
                },
                'CodeContentType': 'PLAINTEXT'|'ZIPFILE'
            },
            'ApplicationSnapshotConfiguration': {
                'SnapshotsEnabled': True|False
            },
            'VpcConfigurations': [
                {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
            ]
        },
        CloudWatchLoggingOptions=[
            {
                'LogStreamARN': 'string'
            },
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of your application (for example, sample-app ).\n

    :type ApplicationDescription: string
    :param ApplicationDescription: A summary description of the application.

    :type RuntimeEnvironment: string
    :param RuntimeEnvironment: [REQUIRED]\nThe runtime environment for the application (SQL-1.0 or FLINK-1_6 ).\n

    :type ServiceExecutionRole: string
    :param ServiceExecutionRole: [REQUIRED]\nThe IAM role used by the application to access Kinesis data streams, Kinesis Data Firehose delivery streams, Amazon S3 objects, and other external resources.\n

    :type ApplicationConfiguration: dict
    :param ApplicationConfiguration: Use this parameter to configure the application.\n\nSqlApplicationConfiguration (dict) --The creation and update parameters for an SQL-based Kinesis Data Analytics application.\n\nInputs (list) --The array of Input objects describing the input streams used by the application.\n\n(dict) --When you configure the application input for an SQL-based Amazon Kinesis Data Analytics application, you specify the streaming source, the in-application stream name that is created, and the mapping between the two.\n\nNamePrefix (string) -- [REQUIRED]The name prefix to use when creating an in-application stream. Suppose that you specify a prefix 'MyInApplicationStream .' Kinesis Data Analytics then creates one or more (as per the InputParallelism count you specified) in-application streams with the names 'MyInApplicationStream_001 ,' 'MyInApplicationStream_002 ,' and so on.\n\nInputProcessingConfiguration (dict) --The InputProcessingConfiguration for the input. An input processor transforms records as they are received from the stream, before the application\'s SQL code executes. Currently, the only input processing configuration available is InputLambdaProcessor .\n\nInputLambdaProcessor (dict) -- [REQUIRED]The InputLambdaProcessor that is used to preprocess the records in the stream before being processed by your application code.\n\nResourceARN (string) -- [REQUIRED]The ARN of the AWS Lambda function that operates on records in the stream.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\n\n\n\n\nKinesisStreamsInput (dict) --If the streaming source is an Amazon Kinesis data stream, identifies the stream\'s Amazon Resource Name (ARN).\n\nResourceARN (string) -- [REQUIRED]The ARN of the input Kinesis data stream to read.\n\n\n\nKinesisFirehoseInput (dict) --If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies the delivery stream\'s ARN.\n\nResourceARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the delivery stream.\n\n\n\nInputParallelism (dict) --Describes the number of in-application streams to create.\n\nCount (integer) --The number of in-application streams to create.\n\n\n\nInputSchema (dict) -- [REQUIRED]Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.\nAlso used to describe the format of the reference data source.\n\nRecordFormat (dict) -- [REQUIRED]Specifies the format of the records on the streaming source.\n\nRecordFormatType (string) -- [REQUIRED]The type of record format.\n\nMappingParameters (dict) --When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.\n\nJSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.\n\nRecordRowPath (string) -- [REQUIRED]The path to the top-level parent that contains the records.\n\n\n\nCSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).\n\nRecordRowDelimiter (string) -- [REQUIRED]The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.\n\nRecordColumnDelimiter (string) -- [REQUIRED]The column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.\n\n\n\n\n\n\n\nRecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.\n\nRecordColumns (list) -- [REQUIRED]A list of RecordColumn objects.\n\n(dict) --For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.\nAlso used to describe the format of the reference data source.\n\nName (string) -- [REQUIRED]The name of the column that is created in the in-application input stream or reference table.\n\nMapping (string) --A reference to the data element in the streaming input or the reference data source.\n\nSqlType (string) -- [REQUIRED]The type of column created in the in-application input stream or reference table.\n\n\n\n\n\n\n\n\n\n\n\nOutputs (list) --The array of Output objects describing the destination streams used by the application.\n\n(dict) --Describes an SQL-based Amazon Kinesis Data Analytics application\'s output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.\n\nName (string) -- [REQUIRED]The name of the in-application stream.\n\nKinesisStreamsOutput (dict) --Identifies an Amazon Kinesis data stream as the destination.\n\nResourceARN (string) -- [REQUIRED]The ARN of the destination Kinesis data stream to write to.\n\n\n\nKinesisFirehoseOutput (dict) --Identifies an Amazon Kinesis Data Firehose delivery stream as the destination.\n\nResourceARN (string) -- [REQUIRED]The ARN of the destination delivery stream to write to.\n\n\n\nLambdaOutput (dict) --Identifies an AWS Lambda function as the destination.\n\nResourceARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the destination Lambda function to write to.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\n\n\nDestinationSchema (dict) -- [REQUIRED]Describes the data format when records are written to the destination.\n\nRecordFormatType (string) -- [REQUIRED]Specifies the format of the records on the output stream.\n\n\n\n\n\n\n\nReferenceDataSources (list) --The array of ReferenceDataSource objects describing the reference data sources used by the application.\n\n(dict) --For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data source by providing the source information (Amazon S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.\n\nTableName (string) -- [REQUIRED]The name of the in-application table to create.\n\nS3ReferenceDataSource (dict) --Identifies the S3 bucket and object that contains the reference data. A Kinesis Data Analytics application loads reference data only once. If the data changes, you call the UpdateApplication operation to trigger reloading of data into your application.\n\nBucketARN (string) --The Amazon Resource Name (ARN) of the S3 bucket.\n\nFileKey (string) --The object key name containing the reference data.\n\n\n\nReferenceSchema (dict) -- [REQUIRED]Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.\n\nRecordFormat (dict) -- [REQUIRED]Specifies the format of the records on the streaming source.\n\nRecordFormatType (string) -- [REQUIRED]The type of record format.\n\nMappingParameters (dict) --When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.\n\nJSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.\n\nRecordRowPath (string) -- [REQUIRED]The path to the top-level parent that contains the records.\n\n\n\nCSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).\n\nRecordRowDelimiter (string) -- [REQUIRED]The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.\n\nRecordColumnDelimiter (string) -- [REQUIRED]The column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.\n\n\n\n\n\n\n\nRecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.\n\nRecordColumns (list) -- [REQUIRED]A list of RecordColumn objects.\n\n(dict) --For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.\nAlso used to describe the format of the reference data source.\n\nName (string) -- [REQUIRED]The name of the column that is created in the in-application input stream or reference table.\n\nMapping (string) --A reference to the data element in the streaming input or the reference data source.\n\nSqlType (string) -- [REQUIRED]The type of column created in the in-application input stream or reference table.\n\n\n\n\n\n\n\n\n\n\n\n\n\nFlinkApplicationConfiguration (dict) --The creation and update parameters for a Java-based Kinesis Data Analytics application.\n\nCheckpointConfiguration (dict) --Describes an application\'s checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance. For more information, see Checkpoints for Fault Tolerance in the Apache Flink Documentation .\n\nConfigurationType (string) -- [REQUIRED]Describes whether the application uses Amazon Kinesis Data Analytics\' default checkpointing behavior. You must set this property to CUSTOM in order to set the CheckpointingEnabled , CheckpointInterval , or MinPauseBetweenCheckpoints parameters.\n\nNote\nIf this value is set to DEFAULT , the application will use the following values, even if they are set to other values using APIs or application code:\n\nCheckpointingEnabled: true\nCheckpointInterval: 60000\nMinPauseBetweenCheckpoints: 5000\n\n\n\nCheckpointingEnabled (boolean) --Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics application.\n\nNote\nIf CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a CheckpointingEnabled value of true , even if this value is set to another value using this API or in application code.\n\n\nCheckpointInterval (integer) --Describes the interval in milliseconds between checkpoint operations.\n\nNote\nIf CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a CheckpointInterval vaue of 60000, even if this value is set to another value using this API or in application code.\n\n\nMinPauseBetweenCheckpoints (integer) --Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start. If a checkpoint operation takes longer than the CheckpointInterval , the application otherwise performs continual checkpoint operations. For more information, see Tuning Checkpointing in the Apache Flink Documentation .\n\nNote\nIf CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a MinPauseBetweenCheckpoints value of 5000, even if this value is set using this API or in application code.\n\n\n\n\nMonitoringConfiguration (dict) --Describes configuration parameters for Amazon CloudWatch logging for an application.\n\nConfigurationType (string) -- [REQUIRED]Describes whether to use the default CloudWatch logging configuration for an application. You must set this property to CUSTOM in order to set the LogLevel or MetricsLevel parameters.\n\nMetricsLevel (string) --Describes the granularity of the CloudWatch Logs for an application.\n\nLogLevel (string) --Describes the verbosity of the CloudWatch Logs for an application.\n\n\n\nParallelismConfiguration (dict) --Describes parameters for how an application executes multiple tasks simultaneously.\n\nConfigurationType (string) -- [REQUIRED]Describes whether the application uses the default parallelism for the Kinesis Data Analytics service. You must set this property to CUSTOM in order to change your application\'s AutoScalingEnabled , Parallelism , or ParallelismPerKPU properties.\n\nParallelism (integer) --Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics application can perform. If AutoScalingEnabled is set to True, Kinesis Data Analytics increases the CurrentParallelism value in response to application load. The service can increase the CurrentParallelism value up to the maximum parallelism, which is ParalellismPerKPU times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the CurrentParallelism value down to the Parallelism setting.\n\nParallelismPerKPU (integer) --Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application can perform per Kinesis Processing Unit (KPU) used by the application. For more information about KPUs, see Amazon Kinesis Data Analytics Pricing .\n\nAutoScalingEnabled (boolean) --Describes whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.\n\n\n\n\n\nEnvironmentProperties (dict) --Describes execution properties for a Java-based Kinesis Data Analytics application.\n\nPropertyGroups (list) -- [REQUIRED]Describes the execution property groups.\n\n(dict) --Property key-value pairs passed into a Java-based Kinesis Data Analytics application.\n\nPropertyGroupId (string) -- [REQUIRED]Describes the key of an application execution property key-value pair.\n\nPropertyMap (dict) -- [REQUIRED]Describes the value of an application execution property key-value pair.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\n\n\nApplicationCodeConfiguration (dict) -- [REQUIRED]The code location and type parameters for a Java-based Kinesis Data Analytics application.\n\nCodeContent (dict) --The location and type of the application code.\n\nTextContent (string) --The text-format code for a Java-based Kinesis Data Analytics application.\n\nZipFileContent (bytes) --The zip-format code for a Java-based Kinesis Data Analytics application.\n\nS3ContentLocation (dict) --Information about the Amazon S3 bucket containing the application code.\n\nBucketARN (string) -- [REQUIRED]The Amazon Resource Name (ARN) for the S3 bucket containing the application code.\n\nFileKey (string) -- [REQUIRED]The file key for the object containing the application code.\n\nObjectVersion (string) --The version of the object containing the application code.\n\n\n\n\n\nCodeContentType (string) -- [REQUIRED]Specifies whether the code content is in text or zip format.\n\n\n\nApplicationSnapshotConfiguration (dict) --Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.\n\nSnapshotsEnabled (boolean) -- [REQUIRED]Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.\n\n\n\nVpcConfigurations (list) --The array of descriptions of VPC configurations available to the application.\n\n(dict) --Describes the parameters of a VPC used by the application.\n\nSubnetIds (list) -- [REQUIRED]The array of Subnet IDs used by the VPC configuration.\n\n(string) --\n\n\nSecurityGroupIds (list) -- [REQUIRED]The array of SecurityGroup IDs used by the VPC configuration.\n\n(string) --\n\n\n\n\n\n\n\n

    :type CloudWatchLoggingOptions: list
    :param CloudWatchLoggingOptions: Use this parameter to configure an Amazon CloudWatch log stream to monitor application configuration errors.\n\n(dict) --Provides a description of Amazon CloudWatch logging options, including the log stream Amazon Resource Name (ARN).\n\nLogStreamARN (string) -- [REQUIRED]The ARN of the CloudWatch log to receive application messages.\n\n\n\n\n

    :type Tags: list
    :param Tags: A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see Using Tagging .\n\n(dict) --A key-value pair (the value is optional) that you can define and assign to AWS resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see Using Tagging .\n\nKey (string) -- [REQUIRED]The key of the key-value tag.\n\nValue (string) --The value of the key-value tag. The value is optional.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationDetail': {
        'ApplicationARN': 'string',
        'ApplicationDescription': 'string',
        'ApplicationName': 'string',
        'RuntimeEnvironment': 'SQL-1_0'|'FLINK-1_6'|'FLINK-1_8',
        'ServiceExecutionRole': 'string',
        'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
        'ApplicationVersionId': 123,
        'CreateTimestamp': datetime(2015, 1, 1),
        'LastUpdateTimestamp': datetime(2015, 1, 1),
        'ApplicationConfigurationDescription': {
            'SqlApplicationConfigurationDescription': {
                'InputDescriptions': [
                    {
                        'InputId': 'string',
                        'NamePrefix': 'string',
                        'InAppStreamNames': [
                            'string',
                        ],
                        'InputProcessingConfigurationDescription': {
                            'InputLambdaProcessorDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            }
                        },
                        'KinesisStreamsInputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'KinesisFirehoseInputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'InputSchema': {
                            'RecordFormat': {
                                'RecordFormatType': 'JSON'|'CSV',
                                'MappingParameters': {
                                    'JSONMappingParameters': {
                                        'RecordRowPath': 'string'
                                    },
                                    'CSVMappingParameters': {
                                        'RecordRowDelimiter': 'string',
                                        'RecordColumnDelimiter': 'string'
                                    }
                                }
                            },
                            'RecordEncoding': 'string',
                            'RecordColumns': [
                                {
                                    'Name': 'string',
                                    'Mapping': 'string',
                                    'SqlType': 'string'
                                },
                            ]
                        },
                        'InputParallelism': {
                            'Count': 123
                        },
                        'InputStartingPositionConfiguration': {
                            'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                        }
                    },
                ],
                'OutputDescriptions': [
                    {
                        'OutputId': 'string',
                        'Name': 'string',
                        'KinesisStreamsOutputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'KinesisFirehoseOutputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'LambdaOutputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'DestinationSchema': {
                            'RecordFormatType': 'JSON'|'CSV'
                        }
                    },
                ],
                'ReferenceDataSourceDescriptions': [
                    {
                        'ReferenceId': 'string',
                        'TableName': 'string',
                        'S3ReferenceDataSourceDescription': {
                            'BucketARN': 'string',
                            'FileKey': 'string',
                            'ReferenceRoleARN': 'string'
                        },
                        'ReferenceSchema': {
                            'RecordFormat': {
                                'RecordFormatType': 'JSON'|'CSV',
                                'MappingParameters': {
                                    'JSONMappingParameters': {
                                        'RecordRowPath': 'string'
                                    },
                                    'CSVMappingParameters': {
                                        'RecordRowDelimiter': 'string',
                                        'RecordColumnDelimiter': 'string'
                                    }
                                }
                            },
                            'RecordEncoding': 'string',
                            'RecordColumns': [
                                {
                                    'Name': 'string',
                                    'Mapping': 'string',
                                    'SqlType': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'ApplicationCodeConfigurationDescription': {
                'CodeContentType': 'PLAINTEXT'|'ZIPFILE',
                'CodeContentDescription': {
                    'TextContent': 'string',
                    'CodeMD5': 'string',
                    'CodeSize': 123,
                    'S3ApplicationCodeLocationDescription': {
                        'BucketARN': 'string',
                        'FileKey': 'string',
                        'ObjectVersion': 'string'
                    }
                }
            },
            'RunConfigurationDescription': {
                'ApplicationRestoreConfigurationDescription': {
                    'ApplicationRestoreType': 'SKIP_RESTORE_FROM_SNAPSHOT'|'RESTORE_FROM_LATEST_SNAPSHOT'|'RESTORE_FROM_CUSTOM_SNAPSHOT',
                    'SnapshotName': 'string'
                }
            },
            'FlinkApplicationConfigurationDescription': {
                'CheckpointConfigurationDescription': {
                    'ConfigurationType': 'DEFAULT'|'CUSTOM',
                    'CheckpointingEnabled': True|False,
                    'CheckpointInterval': 123,
                    'MinPauseBetweenCheckpoints': 123
                },
                'MonitoringConfigurationDescription': {
                    'ConfigurationType': 'DEFAULT'|'CUSTOM',
                    'MetricsLevel': 'APPLICATION'|'TASK'|'OPERATOR'|'PARALLELISM',
                    'LogLevel': 'INFO'|'WARN'|'ERROR'|'DEBUG'
                },
                'ParallelismConfigurationDescription': {
                    'ConfigurationType': 'DEFAULT'|'CUSTOM',
                    'Parallelism': 123,
                    'ParallelismPerKPU': 123,
                    'CurrentParallelism': 123,
                    'AutoScalingEnabled': True|False
                },
                'JobPlanDescription': 'string'
            },
            'EnvironmentPropertyDescriptions': {
                'PropertyGroupDescriptions': [
                    {
                        'PropertyGroupId': 'string',
                        'PropertyMap': {
                            'string': 'string'
                        }
                    },
                ]
            },
            'ApplicationSnapshotConfigurationDescription': {
                'SnapshotsEnabled': True|False
            },
            'VpcConfigurationDescriptions': [
                {
                    'VpcConfigurationId': 'string',
                    'VpcId': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
            ]
        },
        'CloudWatchLoggingOptionDescriptions': [
            {
                'CloudWatchLoggingOptionId': 'string',
                'LogStreamARN': 'string',
                'RoleARN': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

ApplicationDetail (dict) --
In response to your CreateApplication request, Kinesis Data Analytics returns a response with details of the application it created.

ApplicationARN (string) --
The ARN of the application.

ApplicationDescription (string) --
The description of the application.

ApplicationName (string) --
The name of the application.

RuntimeEnvironment (string) --
The runtime environment for the application (SQL-1.0 or FLINK-1_6 ).

ServiceExecutionRole (string) --
Specifies the IAM role that the application uses to access external resources.

ApplicationStatus (string) --
The status of the application.

ApplicationVersionId (integer) --
Provides the current application version. Kinesis Data Analytics updates the ApplicationVersionId each time you update the application.

CreateTimestamp (datetime) --
The current timestamp when the application was created.

LastUpdateTimestamp (datetime) --
The current timestamp when the application was last updated.

ApplicationConfigurationDescription (dict) --
Provides details about the application\'s SQL or Java code and starting parameters.

SqlApplicationConfigurationDescription (dict) --
The details about inputs, outputs, and reference data sources for an SQL-based Kinesis Data Analytics application.

InputDescriptions (list) --
The array of  InputDescription objects describing the input streams used by the application.

(dict) --
Describes the application input configuration for an SQL-based Amazon Kinesis Data Analytics application.

InputId (string) --
The input ID that is associated with the application input. This is the ID that Kinesis Data Analytics assigns to each input configuration that you add to your application.

NamePrefix (string) --
The in-application name prefix.

InAppStreamNames (list) --
Returns the in-application stream names that are mapped to the stream source.

(string) --


InputProcessingConfigurationDescription (dict) --
The description of the preprocessor that executes on records in this input before the application\'s code is run.

InputLambdaProcessorDescription (dict) --
Provides configuration information about the associated  InputLambdaProcessorDescription

ResourceARN (string) --
The ARN of the AWS Lambda function that is used to preprocess the records in the stream.

Note
To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda


RoleARN (string) --
The ARN of the IAM role that is used to access the AWS Lambda function.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.






KinesisStreamsInputDescription (dict) --
If a Kinesis data stream is configured as a streaming source, provides the Kinesis data stream\'s Amazon Resource Name (ARN).

ResourceARN (string) --
The Amazon Resource Name (ARN) of the Kinesis data stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




KinesisFirehoseInputDescription (dict) --
If a Kinesis Data Firehose delivery stream is configured as a streaming source, provides the delivery stream\'s ARN.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the delivery stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




InputSchema (dict) --
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.

RecordFormat (dict) --
Specifies the format of the records on the streaming source.

RecordFormatType (string) --
The type of record format.

MappingParameters (dict) --
When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters (dict) --
Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath (string) --
The path to the top-level parent that contains the records.



CSVMappingParameters (dict) --
Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter (string) --
The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.

RecordColumnDelimiter (string) --
The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.







RecordEncoding (string) --
Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns (list) --
A list of RecordColumn objects.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
Also used to describe the format of the reference data source.

Name (string) --
The name of the column that is created in the in-application input stream or reference table.

Mapping (string) --
A reference to the data element in the streaming input or the reference data source.

SqlType (string) --
The type of column created in the in-application input stream or reference table.







InputParallelism (dict) --
Describes the configured parallelism (number of in-application streams mapped to the streaming source).

Count (integer) --
The number of in-application streams to create.



InputStartingPositionConfiguration (dict) --
The point at which the application is configured to read from the input stream.

InputStartingPosition (string) --
The starting position on the stream.

NOW - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued.
TRIM_HORIZON - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream.
LAST_STOPPED_POINT - Resume reading from where the application last stopped reading.








OutputDescriptions (list) --
The array of  OutputDescription objects describing the destination streams used by the application.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

OutputId (string) --
A unique identifier for the output configuration.

Name (string) --
The name of the in-application stream that is configured as output.

KinesisStreamsOutputDescription (dict) --
Describes the Kinesis data stream that is configured as the destination where output is written.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the Kinesis data stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




KinesisFirehoseOutputDescription (dict) --
Describes the Kinesis Data Firehose delivery stream that is configured as the destination where output is written.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the delivery stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




LambdaOutputDescription (dict) --
Describes the Lambda function that is configured as the destination where output is written.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the destination Lambda function.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to write to the destination function.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




DestinationSchema (dict) --
The data format used for writing data to the destination.

RecordFormatType (string) --
Specifies the format of the records on the output stream.







ReferenceDataSourceDescriptions (list) --
The array of  ReferenceDataSourceDescription objects describing the reference data sources used by the application.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data source configured for an application.

ReferenceId (string) --
The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns when you add the reference data source to your application using the  CreateApplication or  UpdateApplication operation.

TableName (string) --
The in-application table name created by the specific reference data source configuration.

S3ReferenceDataSourceDescription (dict) --
Provides the Amazon S3 bucket name, the object key name that contains the reference data.

BucketARN (string) --
The Amazon Resource Name (ARN) of the S3 bucket.

FileKey (string) --
Amazon S3 object key name.

ReferenceRoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




ReferenceSchema (dict) --
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

RecordFormat (dict) --
Specifies the format of the records on the streaming source.

RecordFormatType (string) --
The type of record format.

MappingParameters (dict) --
When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters (dict) --
Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath (string) --
The path to the top-level parent that contains the records.



CSVMappingParameters (dict) --
Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter (string) --
The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.

RecordColumnDelimiter (string) --
The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.







RecordEncoding (string) --
Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns (list) --
A list of RecordColumn objects.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
Also used to describe the format of the reference data source.

Name (string) --
The name of the column that is created in the in-application input stream or reference table.

Mapping (string) --
A reference to the data element in the streaming input or the reference data source.

SqlType (string) --
The type of column created in the in-application input stream or reference table.













ApplicationCodeConfigurationDescription (dict) --
The details about the application code for a Java-based Kinesis Data Analytics application.

CodeContentType (string) --
Specifies whether the code content is in text or zip format.

CodeContentDescription (dict) --
Describes details about the location and format of the application code.

TextContent (string) --
The text-format code

CodeMD5 (string) --
The checksum that can be used to validate zip-format code.

CodeSize (integer) --
The size in bytes of the application code. Can be used to validate zip-format code.

S3ApplicationCodeLocationDescription (dict) --
The S3 bucket Amazon Resource Name (ARN), file key, and object version of the application code stored in Amazon S3.

BucketARN (string) --
The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

FileKey (string) --
The file key for the object containing the application code.

ObjectVersion (string) --
The version of the object containing the application code.







RunConfigurationDescription (dict) --
The details about the starting properties for a Kinesis Data Analytics application.

ApplicationRestoreConfigurationDescription (dict) --
Describes the restore behavior of a restarting application.

ApplicationRestoreType (string) --
Specifies how the application should be restored.

SnapshotName (string) --
The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if RESTORE_FROM_CUSTOM_SNAPSHOT is specified for the ApplicationRestoreType .





FlinkApplicationConfigurationDescription (dict) --
The details about a Java-based Kinesis Data Analytics application.

CheckpointConfigurationDescription (dict) --
Describes an application\'s checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance.

ConfigurationType (string) --
Describes whether the application uses the default checkpointing behavior in Kinesis Data Analytics.

Note
If this value is set to DEFAULT , the application will use the following values, even if they are set to other values using APIs or application code:

CheckpointingEnabled: true
CheckpointInterval: 60000
MinPauseBetweenCheckpoints: 5000



CheckpointingEnabled (boolean) --
Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics application.

Note
If CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a CheckpointingEnabled value of true , even if this value is set to another value using this API or in application code.


CheckpointInterval (integer) --
Describes the interval in milliseconds between checkpoint operations.

Note
If CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a CheckpointInterval vaue of 60000, even if this value is set to another value using this API or in application code.


MinPauseBetweenCheckpoints (integer) --
Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.

Note
If CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a MinPauseBetweenCheckpoints value of 5000, even if this value is set using this API or in application code.




MonitoringConfigurationDescription (dict) --
Describes configuration parameters for Amazon CloudWatch logging for an application.

ConfigurationType (string) --
Describes whether to use the default CloudWatch logging configuration for an application.

MetricsLevel (string) --
Describes the granularity of the CloudWatch Logs for an application.

LogLevel (string) --
Describes the verbosity of the CloudWatch Logs for an application.



ParallelismConfigurationDescription (dict) --
Describes parameters for how an application executes multiple tasks simultaneously.

ConfigurationType (string) --
Describes whether the application uses the default parallelism for the Kinesis Data Analytics service.

Parallelism (integer) --
Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics application can perform. If AutoScalingEnabled is set to True, then Kinesis Data Analytics can increase the CurrentParallelism value in response to application load. The service can increase CurrentParallelism up to the maximum parallelism, which is ParalellismPerKPU times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the CurrentParallelism value down to the Parallelism setting.

ParallelismPerKPU (integer) --
Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application can perform per Kinesis Processing Unit (KPU) used by the application.

CurrentParallelism (integer) --
Describes the current number of parallel tasks that a Java-based Kinesis Data Analytics application can perform. If AutoScalingEnabled is set to True, Kinesis Data Analytics can increase this value in response to application load. The service can increase this value up to the maximum parallelism, which is ParalellismPerKPU times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the CurrentParallelism value down to the Parallelism setting.

AutoScalingEnabled (boolean) --
Describes whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.



JobPlanDescription (string) --
The job plan for an application. For more information about the job plan, see Jobs and Scheduling in the Apache Flink Documentation . To retrieve the job plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails parameter of the  DescribeApplication operation.



EnvironmentPropertyDescriptions (dict) --
Describes execution properties for a Java-based Kinesis Data Analytics application.

PropertyGroupDescriptions (list) --
Describes the execution property groups.

(dict) --
Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

PropertyGroupId (string) --
Describes the key of an application execution property key-value pair.

PropertyMap (dict) --
Describes the value of an application execution property key-value pair.

(string) --
(string) --










ApplicationSnapshotConfigurationDescription (dict) --
Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.

SnapshotsEnabled (boolean) --
Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.



VpcConfigurationDescriptions (list) --
The array of descriptions of VPC configurations available to the application.

(dict) --
Describes the parameters of a VPC used by the application.

VpcConfigurationId (string) --
The ID of the VPC configuration.

VpcId (string) --
The ID of the associated VPC.

SubnetIds (list) --
The array of Subnet IDs used by the VPC configuration.

(string) --


SecurityGroupIds (list) --
The array of SecurityGroup IDs used by the VPC configuration.

(string) --








CloudWatchLoggingOptionDescriptions (list) --
Describes the application Amazon CloudWatch logging options.

(dict) --
Describes the Amazon CloudWatch logging option.

CloudWatchLoggingOptionId (string) --
The ID of the CloudWatch logging option description.

LogStreamARN (string) --
The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

RoleARN (string) --
The IAM ARN of the role to use to send application messages.

Note
Provided for backward compatibility. Applications created with the current API version have an application-level service execution role rather than a resource-level role.














Exceptions

KinesisAnalyticsV2.Client.exceptions.CodeValidationException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.LimitExceededException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
KinesisAnalyticsV2.Client.exceptions.TooManyTagsException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException


    :return: {
        'ApplicationDetail': {
            'ApplicationARN': 'string',
            'ApplicationDescription': 'string',
            'ApplicationName': 'string',
            'RuntimeEnvironment': 'SQL-1_0'|'FLINK-1_6'|'FLINK-1_8',
            'ServiceExecutionRole': 'string',
            'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
            'ApplicationVersionId': 123,
            'CreateTimestamp': datetime(2015, 1, 1),
            'LastUpdateTimestamp': datetime(2015, 1, 1),
            'ApplicationConfigurationDescription': {
                'SqlApplicationConfigurationDescription': {
                    'InputDescriptions': [
                        {
                            'InputId': 'string',
                            'NamePrefix': 'string',
                            'InAppStreamNames': [
                                'string',
                            ],
                            'InputProcessingConfigurationDescription': {
                                'InputLambdaProcessorDescription': {
                                    'ResourceARN': 'string',
                                    'RoleARN': 'string'
                                }
                            },
                            'KinesisStreamsInputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'KinesisFirehoseInputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'InputSchema': {
                                'RecordFormat': {
                                    'RecordFormatType': 'JSON'|'CSV',
                                    'MappingParameters': {
                                        'JSONMappingParameters': {
                                            'RecordRowPath': 'string'
                                        },
                                        'CSVMappingParameters': {
                                            'RecordRowDelimiter': 'string',
                                            'RecordColumnDelimiter': 'string'
                                        }
                                    }
                                },
                                'RecordEncoding': 'string',
                                'RecordColumns': [
                                    {
                                        'Name': 'string',
                                        'Mapping': 'string',
                                        'SqlType': 'string'
                                    },
                                ]
                            },
                            'InputParallelism': {
                                'Count': 123
                            },
                            'InputStartingPositionConfiguration': {
                                'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                            }
                        },
                    ],
                    'OutputDescriptions': [
                        {
                            'OutputId': 'string',
                            'Name': 'string',
                            'KinesisStreamsOutputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'KinesisFirehoseOutputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'LambdaOutputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'DestinationSchema': {
                                'RecordFormatType': 'JSON'|'CSV'
                            }
                        },
                    ],
                    'ReferenceDataSourceDescriptions': [
                        {
                            'ReferenceId': 'string',
                            'TableName': 'string',
                            'S3ReferenceDataSourceDescription': {
                                'BucketARN': 'string',
                                'FileKey': 'string',
                                'ReferenceRoleARN': 'string'
                            },
                            'ReferenceSchema': {
                                'RecordFormat': {
                                    'RecordFormatType': 'JSON'|'CSV',
                                    'MappingParameters': {
                                        'JSONMappingParameters': {
                                            'RecordRowPath': 'string'
                                        },
                                        'CSVMappingParameters': {
                                            'RecordRowDelimiter': 'string',
                                            'RecordColumnDelimiter': 'string'
                                        }
                                    }
                                },
                                'RecordEncoding': 'string',
                                'RecordColumns': [
                                    {
                                        'Name': 'string',
                                        'Mapping': 'string',
                                        'SqlType': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'ApplicationCodeConfigurationDescription': {
                    'CodeContentType': 'PLAINTEXT'|'ZIPFILE',
                    'CodeContentDescription': {
                        'TextContent': 'string',
                        'CodeMD5': 'string',
                        'CodeSize': 123,
                        'S3ApplicationCodeLocationDescription': {
                            'BucketARN': 'string',
                            'FileKey': 'string',
                            'ObjectVersion': 'string'
                        }
                    }
                },
                'RunConfigurationDescription': {
                    'ApplicationRestoreConfigurationDescription': {
                        'ApplicationRestoreType': 'SKIP_RESTORE_FROM_SNAPSHOT'|'RESTORE_FROM_LATEST_SNAPSHOT'|'RESTORE_FROM_CUSTOM_SNAPSHOT',
                        'SnapshotName': 'string'
                    }
                },
                'FlinkApplicationConfigurationDescription': {
                    'CheckpointConfigurationDescription': {
                        'ConfigurationType': 'DEFAULT'|'CUSTOM',
                        'CheckpointingEnabled': True|False,
                        'CheckpointInterval': 123,
                        'MinPauseBetweenCheckpoints': 123
                    },
                    'MonitoringConfigurationDescription': {
                        'ConfigurationType': 'DEFAULT'|'CUSTOM',
                        'MetricsLevel': 'APPLICATION'|'TASK'|'OPERATOR'|'PARALLELISM',
                        'LogLevel': 'INFO'|'WARN'|'ERROR'|'DEBUG'
                    },
                    'ParallelismConfigurationDescription': {
                        'ConfigurationType': 'DEFAULT'|'CUSTOM',
                        'Parallelism': 123,
                        'ParallelismPerKPU': 123,
                        'CurrentParallelism': 123,
                        'AutoScalingEnabled': True|False
                    },
                    'JobPlanDescription': 'string'
                },
                'EnvironmentPropertyDescriptions': {
                    'PropertyGroupDescriptions': [
                        {
                            'PropertyGroupId': 'string',
                            'PropertyMap': {
                                'string': 'string'
                            }
                        },
                    ]
                },
                'ApplicationSnapshotConfigurationDescription': {
                    'SnapshotsEnabled': True|False
                },
                'VpcConfigurationDescriptions': [
                    {
                        'VpcConfigurationId': 'string',
                        'VpcId': 'string',
                        'SubnetIds': [
                            'string',
                        ],
                        'SecurityGroupIds': [
                            'string',
                        ]
                    },
                ]
            },
            'CloudWatchLoggingOptionDescriptions': [
                {
                    'CloudWatchLoggingOptionId': 'string',
                    'LogStreamARN': 'string',
                    'RoleARN': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_application_snapshot(ApplicationName=None, SnapshotName=None):
    """
    Creates a snapshot of the application\'s state data.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_application_snapshot(
        ApplicationName='string',
        SnapshotName='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of an existing application\n

    :type SnapshotName: string
    :param SnapshotName: [REQUIRED]\nAn identifier for the application snapshot.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.LimitExceededException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.UnsupportedOperationException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_application(ApplicationName=None, CreateTimestamp=None):
    """
    Deletes the specified application. Kinesis Data Analytics halts application execution and deletes the application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application(
        ApplicationName='string',
        CreateTimestamp=datetime(2015, 1, 1)
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of the application to delete.\n

    :type CreateTimestamp: datetime
    :param CreateTimestamp: [REQUIRED]\nUse the DescribeApplication operation to get this value.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
KinesisAnalyticsV2.Client.exceptions.InvalidApplicationConfigurationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_application_cloud_watch_logging_option(ApplicationName=None, CurrentApplicationVersionId=None, CloudWatchLoggingOptionId=None):
    """
    Deletes an Amazon CloudWatch log stream from an Amazon Kinesis Data Analytics application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application_cloud_watch_logging_option(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        CloudWatchLoggingOptionId='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe application name.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe version ID of the application. You can retrieve the application version ID using DescribeApplication .\n

    :type CloudWatchLoggingOptionId: string
    :param CloudWatchLoggingOptionId: [REQUIRED]\nThe CloudWatchLoggingOptionId of the Amazon CloudWatch logging option to delete. You can get the CloudWatchLoggingOptionId by using the DescribeApplication operation.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationARN': 'string',
    'ApplicationVersionId': 123,
    'CloudWatchLoggingOptionDescriptions': [
        {
            'CloudWatchLoggingOptionId': 'string',
            'LogStreamARN': 'string',
            'RoleARN': 'string'
        },
    ]
}


Response Structure

(dict) --

ApplicationARN (string) --
The application\'s Amazon Resource Name (ARN).

ApplicationVersionId (integer) --
The version ID of the application. Kinesis Data Analytics updates the ApplicationVersionId each time you change the CloudWatch logging options.

CloudWatchLoggingOptionDescriptions (list) --
The descriptions of the remaining CloudWatch logging options for the application.

(dict) --
Describes the Amazon CloudWatch logging option.

CloudWatchLoggingOptionId (string) --
The ID of the CloudWatch logging option description.

LogStreamARN (string) --
The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

RoleARN (string) --
The IAM ARN of the role to use to send application messages.

Note
Provided for backward compatibility. Applications created with the current API version have an application-level service execution role rather than a resource-level role.












Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
KinesisAnalyticsV2.Client.exceptions.InvalidApplicationConfigurationException


    :return: {
        'ApplicationARN': 'string',
        'ApplicationVersionId': 123,
        'CloudWatchLoggingOptionDescriptions': [
            {
                'CloudWatchLoggingOptionId': 'string',
                'LogStreamARN': 'string',
                'RoleARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
    KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
    KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
    KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
    KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
    KinesisAnalyticsV2.Client.exceptions.InvalidApplicationConfigurationException
    
    """
    pass

def delete_application_input_processing_configuration(ApplicationName=None, CurrentApplicationVersionId=None, InputId=None):
    """
    Deletes an  InputProcessingConfiguration from an input.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application_input_processing_configuration(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        InputId='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of the application.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe application version. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.\n

    :type InputId: string
    :param InputId: [REQUIRED]\nThe ID of the input configuration from which to delete the input processing configuration. You can get a list of the input IDs for an application by using the DescribeApplication operation.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationARN': 'string',
    'ApplicationVersionId': 123
}


Response Structure

(dict) --

ApplicationARN (string) --
The Amazon Resource Name (ARN) of the application.

ApplicationVersionId (integer) --
The current application version ID.







Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException


    :return: {
        'ApplicationARN': 'string',
        'ApplicationVersionId': 123
    }
    
    
    :returns: 
    KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
    KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
    KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
    KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
    KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
    
    """
    pass

def delete_application_output(ApplicationName=None, CurrentApplicationVersionId=None, OutputId=None):
    """
    Deletes the output destination configuration from your SQL-based Amazon Kinesis Data Analytics application\'s configuration. Kinesis Data Analytics will no longer write data from the corresponding in-application stream to the external output destination.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application_output(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        OutputId='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe application name.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe application version. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.\n

    :type OutputId: string
    :param OutputId: [REQUIRED]\nThe ID of the configuration to delete. Each output configuration that is added to the application (either when the application is created or later) using the AddApplicationOutput operation has a unique ID. You need to provide the ID to uniquely identify the output configuration that you want to delete from the application configuration. You can use the DescribeApplication operation to get the specific OutputId .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationARN': 'string',
    'ApplicationVersionId': 123
}


Response Structure

(dict) --

ApplicationARN (string) --
The application Amazon Resource Name (ARN).

ApplicationVersionId (integer) --
The current application version ID.







Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException


    :return: {
        'ApplicationARN': 'string',
        'ApplicationVersionId': 123
    }
    
    
    :returns: 
    KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
    KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
    KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
    KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
    KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
    
    """
    pass

def delete_application_reference_data_source(ApplicationName=None, CurrentApplicationVersionId=None, ReferenceId=None):
    """
    Deletes a reference data source configuration from the specified SQL-based Amazon Kinesis Data Analytics application\'s configuration.
    If the application is running, Kinesis Data Analytics immediately removes the in-application table that you created using the  AddApplicationReferenceDataSource operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application_reference_data_source(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        ReferenceId='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of an existing application.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe current application version. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.\n

    :type ReferenceId: string
    :param ReferenceId: [REQUIRED]\nThe ID of the reference data source. When you add a reference data source to your application using the AddApplicationReferenceDataSource , Kinesis Data Analytics assigns an ID. You can use the DescribeApplication operation to get the reference ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationARN': 'string',
    'ApplicationVersionId': 123
}


Response Structure

(dict) --

ApplicationARN (string) --
The application Amazon Resource Name (ARN).

ApplicationVersionId (integer) --
The updated version ID of the application.







Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException


    :return: {
        'ApplicationARN': 'string',
        'ApplicationVersionId': 123
    }
    
    
    :returns: 
    KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
    KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
    KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
    KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
    KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
    
    """
    pass

def delete_application_snapshot(ApplicationName=None, SnapshotName=None, SnapshotCreationTimestamp=None):
    """
    Deletes a snapshot of application state.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application_snapshot(
        ApplicationName='string',
        SnapshotName='string',
        SnapshotCreationTimestamp=datetime(2015, 1, 1)
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of an existing application.\n

    :type SnapshotName: string
    :param SnapshotName: [REQUIRED]\nThe identifier for the snapshot delete.\n

    :type SnapshotCreationTimestamp: datetime
    :param SnapshotCreationTimestamp: [REQUIRED]\nThe creation timestamp of the application snapshot to delete. You can retrieve this value using or .\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.UnsupportedOperationException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_application_vpc_configuration(ApplicationName=None, CurrentApplicationVersionId=None, VpcConfigurationId=None):
    """
    Removes a VPC configuration from a Kinesis Data Analytics application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application_vpc_configuration(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        VpcConfigurationId='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of an existing application.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe current application version ID. You can retrieve the application version ID using DescribeApplication .\n

    :type VpcConfigurationId: string
    :param VpcConfigurationId: [REQUIRED]\nThe ID of the VPC configuration to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationARN': 'string',
    'ApplicationVersionId': 123
}


Response Structure

(dict) --

ApplicationARN (string) --
The ARN of the Kinesis Data Analytics application.

ApplicationVersionId (integer) --
The updated version ID of the application.







Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException


    :return: {
        'ApplicationARN': 'string',
        'ApplicationVersionId': 123
    }
    
    
    :returns: 
    KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
    KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
    KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
    KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def describe_application(ApplicationName=None, IncludeAdditionalDetails=None):
    """
    Returns information about a specific Amazon Kinesis Data Analytics application.
    If you want to retrieve a list of all applications in your account, use the  ListApplications operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_application(
        ApplicationName='string',
        IncludeAdditionalDetails=True|False
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of the application.\n

    :type IncludeAdditionalDetails: boolean
    :param IncludeAdditionalDetails: Displays verbose information about a Kinesis Data Analytics application, including the application\'s job plan.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationDetail': {
        'ApplicationARN': 'string',
        'ApplicationDescription': 'string',
        'ApplicationName': 'string',
        'RuntimeEnvironment': 'SQL-1_0'|'FLINK-1_6'|'FLINK-1_8',
        'ServiceExecutionRole': 'string',
        'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
        'ApplicationVersionId': 123,
        'CreateTimestamp': datetime(2015, 1, 1),
        'LastUpdateTimestamp': datetime(2015, 1, 1),
        'ApplicationConfigurationDescription': {
            'SqlApplicationConfigurationDescription': {
                'InputDescriptions': [
                    {
                        'InputId': 'string',
                        'NamePrefix': 'string',
                        'InAppStreamNames': [
                            'string',
                        ],
                        'InputProcessingConfigurationDescription': {
                            'InputLambdaProcessorDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            }
                        },
                        'KinesisStreamsInputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'KinesisFirehoseInputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'InputSchema': {
                            'RecordFormat': {
                                'RecordFormatType': 'JSON'|'CSV',
                                'MappingParameters': {
                                    'JSONMappingParameters': {
                                        'RecordRowPath': 'string'
                                    },
                                    'CSVMappingParameters': {
                                        'RecordRowDelimiter': 'string',
                                        'RecordColumnDelimiter': 'string'
                                    }
                                }
                            },
                            'RecordEncoding': 'string',
                            'RecordColumns': [
                                {
                                    'Name': 'string',
                                    'Mapping': 'string',
                                    'SqlType': 'string'
                                },
                            ]
                        },
                        'InputParallelism': {
                            'Count': 123
                        },
                        'InputStartingPositionConfiguration': {
                            'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                        }
                    },
                ],
                'OutputDescriptions': [
                    {
                        'OutputId': 'string',
                        'Name': 'string',
                        'KinesisStreamsOutputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'KinesisFirehoseOutputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'LambdaOutputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'DestinationSchema': {
                            'RecordFormatType': 'JSON'|'CSV'
                        }
                    },
                ],
                'ReferenceDataSourceDescriptions': [
                    {
                        'ReferenceId': 'string',
                        'TableName': 'string',
                        'S3ReferenceDataSourceDescription': {
                            'BucketARN': 'string',
                            'FileKey': 'string',
                            'ReferenceRoleARN': 'string'
                        },
                        'ReferenceSchema': {
                            'RecordFormat': {
                                'RecordFormatType': 'JSON'|'CSV',
                                'MappingParameters': {
                                    'JSONMappingParameters': {
                                        'RecordRowPath': 'string'
                                    },
                                    'CSVMappingParameters': {
                                        'RecordRowDelimiter': 'string',
                                        'RecordColumnDelimiter': 'string'
                                    }
                                }
                            },
                            'RecordEncoding': 'string',
                            'RecordColumns': [
                                {
                                    'Name': 'string',
                                    'Mapping': 'string',
                                    'SqlType': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'ApplicationCodeConfigurationDescription': {
                'CodeContentType': 'PLAINTEXT'|'ZIPFILE',
                'CodeContentDescription': {
                    'TextContent': 'string',
                    'CodeMD5': 'string',
                    'CodeSize': 123,
                    'S3ApplicationCodeLocationDescription': {
                        'BucketARN': 'string',
                        'FileKey': 'string',
                        'ObjectVersion': 'string'
                    }
                }
            },
            'RunConfigurationDescription': {
                'ApplicationRestoreConfigurationDescription': {
                    'ApplicationRestoreType': 'SKIP_RESTORE_FROM_SNAPSHOT'|'RESTORE_FROM_LATEST_SNAPSHOT'|'RESTORE_FROM_CUSTOM_SNAPSHOT',
                    'SnapshotName': 'string'
                }
            },
            'FlinkApplicationConfigurationDescription': {
                'CheckpointConfigurationDescription': {
                    'ConfigurationType': 'DEFAULT'|'CUSTOM',
                    'CheckpointingEnabled': True|False,
                    'CheckpointInterval': 123,
                    'MinPauseBetweenCheckpoints': 123
                },
                'MonitoringConfigurationDescription': {
                    'ConfigurationType': 'DEFAULT'|'CUSTOM',
                    'MetricsLevel': 'APPLICATION'|'TASK'|'OPERATOR'|'PARALLELISM',
                    'LogLevel': 'INFO'|'WARN'|'ERROR'|'DEBUG'
                },
                'ParallelismConfigurationDescription': {
                    'ConfigurationType': 'DEFAULT'|'CUSTOM',
                    'Parallelism': 123,
                    'ParallelismPerKPU': 123,
                    'CurrentParallelism': 123,
                    'AutoScalingEnabled': True|False
                },
                'JobPlanDescription': 'string'
            },
            'EnvironmentPropertyDescriptions': {
                'PropertyGroupDescriptions': [
                    {
                        'PropertyGroupId': 'string',
                        'PropertyMap': {
                            'string': 'string'
                        }
                    },
                ]
            },
            'ApplicationSnapshotConfigurationDescription': {
                'SnapshotsEnabled': True|False
            },
            'VpcConfigurationDescriptions': [
                {
                    'VpcConfigurationId': 'string',
                    'VpcId': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
            ]
        },
        'CloudWatchLoggingOptionDescriptions': [
            {
                'CloudWatchLoggingOptionId': 'string',
                'LogStreamARN': 'string',
                'RoleARN': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

ApplicationDetail (dict) --
Provides a description of the application, such as the application\'s Amazon Resource Name (ARN), status, and latest version.

ApplicationARN (string) --
The ARN of the application.

ApplicationDescription (string) --
The description of the application.

ApplicationName (string) --
The name of the application.

RuntimeEnvironment (string) --
The runtime environment for the application (SQL-1.0 or FLINK-1_6 ).

ServiceExecutionRole (string) --
Specifies the IAM role that the application uses to access external resources.

ApplicationStatus (string) --
The status of the application.

ApplicationVersionId (integer) --
Provides the current application version. Kinesis Data Analytics updates the ApplicationVersionId each time you update the application.

CreateTimestamp (datetime) --
The current timestamp when the application was created.

LastUpdateTimestamp (datetime) --
The current timestamp when the application was last updated.

ApplicationConfigurationDescription (dict) --
Provides details about the application\'s SQL or Java code and starting parameters.

SqlApplicationConfigurationDescription (dict) --
The details about inputs, outputs, and reference data sources for an SQL-based Kinesis Data Analytics application.

InputDescriptions (list) --
The array of  InputDescription objects describing the input streams used by the application.

(dict) --
Describes the application input configuration for an SQL-based Amazon Kinesis Data Analytics application.

InputId (string) --
The input ID that is associated with the application input. This is the ID that Kinesis Data Analytics assigns to each input configuration that you add to your application.

NamePrefix (string) --
The in-application name prefix.

InAppStreamNames (list) --
Returns the in-application stream names that are mapped to the stream source.

(string) --


InputProcessingConfigurationDescription (dict) --
The description of the preprocessor that executes on records in this input before the application\'s code is run.

InputLambdaProcessorDescription (dict) --
Provides configuration information about the associated  InputLambdaProcessorDescription

ResourceARN (string) --
The ARN of the AWS Lambda function that is used to preprocess the records in the stream.

Note
To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda


RoleARN (string) --
The ARN of the IAM role that is used to access the AWS Lambda function.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.






KinesisStreamsInputDescription (dict) --
If a Kinesis data stream is configured as a streaming source, provides the Kinesis data stream\'s Amazon Resource Name (ARN).

ResourceARN (string) --
The Amazon Resource Name (ARN) of the Kinesis data stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




KinesisFirehoseInputDescription (dict) --
If a Kinesis Data Firehose delivery stream is configured as a streaming source, provides the delivery stream\'s ARN.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the delivery stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




InputSchema (dict) --
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.

RecordFormat (dict) --
Specifies the format of the records on the streaming source.

RecordFormatType (string) --
The type of record format.

MappingParameters (dict) --
When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters (dict) --
Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath (string) --
The path to the top-level parent that contains the records.



CSVMappingParameters (dict) --
Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter (string) --
The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.

RecordColumnDelimiter (string) --
The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.







RecordEncoding (string) --
Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns (list) --
A list of RecordColumn objects.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
Also used to describe the format of the reference data source.

Name (string) --
The name of the column that is created in the in-application input stream or reference table.

Mapping (string) --
A reference to the data element in the streaming input or the reference data source.

SqlType (string) --
The type of column created in the in-application input stream or reference table.







InputParallelism (dict) --
Describes the configured parallelism (number of in-application streams mapped to the streaming source).

Count (integer) --
The number of in-application streams to create.



InputStartingPositionConfiguration (dict) --
The point at which the application is configured to read from the input stream.

InputStartingPosition (string) --
The starting position on the stream.

NOW - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued.
TRIM_HORIZON - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream.
LAST_STOPPED_POINT - Resume reading from where the application last stopped reading.








OutputDescriptions (list) --
The array of  OutputDescription objects describing the destination streams used by the application.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

OutputId (string) --
A unique identifier for the output configuration.

Name (string) --
The name of the in-application stream that is configured as output.

KinesisStreamsOutputDescription (dict) --
Describes the Kinesis data stream that is configured as the destination where output is written.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the Kinesis data stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




KinesisFirehoseOutputDescription (dict) --
Describes the Kinesis Data Firehose delivery stream that is configured as the destination where output is written.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the delivery stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




LambdaOutputDescription (dict) --
Describes the Lambda function that is configured as the destination where output is written.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the destination Lambda function.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to write to the destination function.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




DestinationSchema (dict) --
The data format used for writing data to the destination.

RecordFormatType (string) --
Specifies the format of the records on the output stream.







ReferenceDataSourceDescriptions (list) --
The array of  ReferenceDataSourceDescription objects describing the reference data sources used by the application.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data source configured for an application.

ReferenceId (string) --
The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns when you add the reference data source to your application using the  CreateApplication or  UpdateApplication operation.

TableName (string) --
The in-application table name created by the specific reference data source configuration.

S3ReferenceDataSourceDescription (dict) --
Provides the Amazon S3 bucket name, the object key name that contains the reference data.

BucketARN (string) --
The Amazon Resource Name (ARN) of the S3 bucket.

FileKey (string) --
Amazon S3 object key name.

ReferenceRoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




ReferenceSchema (dict) --
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

RecordFormat (dict) --
Specifies the format of the records on the streaming source.

RecordFormatType (string) --
The type of record format.

MappingParameters (dict) --
When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters (dict) --
Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath (string) --
The path to the top-level parent that contains the records.



CSVMappingParameters (dict) --
Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter (string) --
The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.

RecordColumnDelimiter (string) --
The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.







RecordEncoding (string) --
Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns (list) --
A list of RecordColumn objects.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
Also used to describe the format of the reference data source.

Name (string) --
The name of the column that is created in the in-application input stream or reference table.

Mapping (string) --
A reference to the data element in the streaming input or the reference data source.

SqlType (string) --
The type of column created in the in-application input stream or reference table.













ApplicationCodeConfigurationDescription (dict) --
The details about the application code for a Java-based Kinesis Data Analytics application.

CodeContentType (string) --
Specifies whether the code content is in text or zip format.

CodeContentDescription (dict) --
Describes details about the location and format of the application code.

TextContent (string) --
The text-format code

CodeMD5 (string) --
The checksum that can be used to validate zip-format code.

CodeSize (integer) --
The size in bytes of the application code. Can be used to validate zip-format code.

S3ApplicationCodeLocationDescription (dict) --
The S3 bucket Amazon Resource Name (ARN), file key, and object version of the application code stored in Amazon S3.

BucketARN (string) --
The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

FileKey (string) --
The file key for the object containing the application code.

ObjectVersion (string) --
The version of the object containing the application code.







RunConfigurationDescription (dict) --
The details about the starting properties for a Kinesis Data Analytics application.

ApplicationRestoreConfigurationDescription (dict) --
Describes the restore behavior of a restarting application.

ApplicationRestoreType (string) --
Specifies how the application should be restored.

SnapshotName (string) --
The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if RESTORE_FROM_CUSTOM_SNAPSHOT is specified for the ApplicationRestoreType .





FlinkApplicationConfigurationDescription (dict) --
The details about a Java-based Kinesis Data Analytics application.

CheckpointConfigurationDescription (dict) --
Describes an application\'s checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance.

ConfigurationType (string) --
Describes whether the application uses the default checkpointing behavior in Kinesis Data Analytics.

Note
If this value is set to DEFAULT , the application will use the following values, even if they are set to other values using APIs or application code:

CheckpointingEnabled: true
CheckpointInterval: 60000
MinPauseBetweenCheckpoints: 5000



CheckpointingEnabled (boolean) --
Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics application.

Note
If CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a CheckpointingEnabled value of true , even if this value is set to another value using this API or in application code.


CheckpointInterval (integer) --
Describes the interval in milliseconds between checkpoint operations.

Note
If CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a CheckpointInterval vaue of 60000, even if this value is set to another value using this API or in application code.


MinPauseBetweenCheckpoints (integer) --
Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.

Note
If CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a MinPauseBetweenCheckpoints value of 5000, even if this value is set using this API or in application code.




MonitoringConfigurationDescription (dict) --
Describes configuration parameters for Amazon CloudWatch logging for an application.

ConfigurationType (string) --
Describes whether to use the default CloudWatch logging configuration for an application.

MetricsLevel (string) --
Describes the granularity of the CloudWatch Logs for an application.

LogLevel (string) --
Describes the verbosity of the CloudWatch Logs for an application.



ParallelismConfigurationDescription (dict) --
Describes parameters for how an application executes multiple tasks simultaneously.

ConfigurationType (string) --
Describes whether the application uses the default parallelism for the Kinesis Data Analytics service.

Parallelism (integer) --
Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics application can perform. If AutoScalingEnabled is set to True, then Kinesis Data Analytics can increase the CurrentParallelism value in response to application load. The service can increase CurrentParallelism up to the maximum parallelism, which is ParalellismPerKPU times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the CurrentParallelism value down to the Parallelism setting.

ParallelismPerKPU (integer) --
Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application can perform per Kinesis Processing Unit (KPU) used by the application.

CurrentParallelism (integer) --
Describes the current number of parallel tasks that a Java-based Kinesis Data Analytics application can perform. If AutoScalingEnabled is set to True, Kinesis Data Analytics can increase this value in response to application load. The service can increase this value up to the maximum parallelism, which is ParalellismPerKPU times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the CurrentParallelism value down to the Parallelism setting.

AutoScalingEnabled (boolean) --
Describes whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.



JobPlanDescription (string) --
The job plan for an application. For more information about the job plan, see Jobs and Scheduling in the Apache Flink Documentation . To retrieve the job plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails parameter of the  DescribeApplication operation.



EnvironmentPropertyDescriptions (dict) --
Describes execution properties for a Java-based Kinesis Data Analytics application.

PropertyGroupDescriptions (list) --
Describes the execution property groups.

(dict) --
Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

PropertyGroupId (string) --
Describes the key of an application execution property key-value pair.

PropertyMap (dict) --
Describes the value of an application execution property key-value pair.

(string) --
(string) --










ApplicationSnapshotConfigurationDescription (dict) --
Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.

SnapshotsEnabled (boolean) --
Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.



VpcConfigurationDescriptions (list) --
The array of descriptions of VPC configurations available to the application.

(dict) --
Describes the parameters of a VPC used by the application.

VpcConfigurationId (string) --
The ID of the VPC configuration.

VpcId (string) --
The ID of the associated VPC.

SubnetIds (list) --
The array of Subnet IDs used by the VPC configuration.

(string) --


SecurityGroupIds (list) --
The array of SecurityGroup IDs used by the VPC configuration.

(string) --








CloudWatchLoggingOptionDescriptions (list) --
Describes the application Amazon CloudWatch logging options.

(dict) --
Describes the Amazon CloudWatch logging option.

CloudWatchLoggingOptionId (string) --
The ID of the CloudWatch logging option description.

LogStreamARN (string) --
The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

RoleARN (string) --
The IAM ARN of the role to use to send application messages.

Note
Provided for backward compatibility. Applications created with the current API version have an application-level service execution role rather than a resource-level role.














Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException


    :return: {
        'ApplicationDetail': {
            'ApplicationARN': 'string',
            'ApplicationDescription': 'string',
            'ApplicationName': 'string',
            'RuntimeEnvironment': 'SQL-1_0'|'FLINK-1_6'|'FLINK-1_8',
            'ServiceExecutionRole': 'string',
            'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
            'ApplicationVersionId': 123,
            'CreateTimestamp': datetime(2015, 1, 1),
            'LastUpdateTimestamp': datetime(2015, 1, 1),
            'ApplicationConfigurationDescription': {
                'SqlApplicationConfigurationDescription': {
                    'InputDescriptions': [
                        {
                            'InputId': 'string',
                            'NamePrefix': 'string',
                            'InAppStreamNames': [
                                'string',
                            ],
                            'InputProcessingConfigurationDescription': {
                                'InputLambdaProcessorDescription': {
                                    'ResourceARN': 'string',
                                    'RoleARN': 'string'
                                }
                            },
                            'KinesisStreamsInputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'KinesisFirehoseInputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'InputSchema': {
                                'RecordFormat': {
                                    'RecordFormatType': 'JSON'|'CSV',
                                    'MappingParameters': {
                                        'JSONMappingParameters': {
                                            'RecordRowPath': 'string'
                                        },
                                        'CSVMappingParameters': {
                                            'RecordRowDelimiter': 'string',
                                            'RecordColumnDelimiter': 'string'
                                        }
                                    }
                                },
                                'RecordEncoding': 'string',
                                'RecordColumns': [
                                    {
                                        'Name': 'string',
                                        'Mapping': 'string',
                                        'SqlType': 'string'
                                    },
                                ]
                            },
                            'InputParallelism': {
                                'Count': 123
                            },
                            'InputStartingPositionConfiguration': {
                                'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                            }
                        },
                    ],
                    'OutputDescriptions': [
                        {
                            'OutputId': 'string',
                            'Name': 'string',
                            'KinesisStreamsOutputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'KinesisFirehoseOutputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'LambdaOutputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'DestinationSchema': {
                                'RecordFormatType': 'JSON'|'CSV'
                            }
                        },
                    ],
                    'ReferenceDataSourceDescriptions': [
                        {
                            'ReferenceId': 'string',
                            'TableName': 'string',
                            'S3ReferenceDataSourceDescription': {
                                'BucketARN': 'string',
                                'FileKey': 'string',
                                'ReferenceRoleARN': 'string'
                            },
                            'ReferenceSchema': {
                                'RecordFormat': {
                                    'RecordFormatType': 'JSON'|'CSV',
                                    'MappingParameters': {
                                        'JSONMappingParameters': {
                                            'RecordRowPath': 'string'
                                        },
                                        'CSVMappingParameters': {
                                            'RecordRowDelimiter': 'string',
                                            'RecordColumnDelimiter': 'string'
                                        }
                                    }
                                },
                                'RecordEncoding': 'string',
                                'RecordColumns': [
                                    {
                                        'Name': 'string',
                                        'Mapping': 'string',
                                        'SqlType': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'ApplicationCodeConfigurationDescription': {
                    'CodeContentType': 'PLAINTEXT'|'ZIPFILE',
                    'CodeContentDescription': {
                        'TextContent': 'string',
                        'CodeMD5': 'string',
                        'CodeSize': 123,
                        'S3ApplicationCodeLocationDescription': {
                            'BucketARN': 'string',
                            'FileKey': 'string',
                            'ObjectVersion': 'string'
                        }
                    }
                },
                'RunConfigurationDescription': {
                    'ApplicationRestoreConfigurationDescription': {
                        'ApplicationRestoreType': 'SKIP_RESTORE_FROM_SNAPSHOT'|'RESTORE_FROM_LATEST_SNAPSHOT'|'RESTORE_FROM_CUSTOM_SNAPSHOT',
                        'SnapshotName': 'string'
                    }
                },
                'FlinkApplicationConfigurationDescription': {
                    'CheckpointConfigurationDescription': {
                        'ConfigurationType': 'DEFAULT'|'CUSTOM',
                        'CheckpointingEnabled': True|False,
                        'CheckpointInterval': 123,
                        'MinPauseBetweenCheckpoints': 123
                    },
                    'MonitoringConfigurationDescription': {
                        'ConfigurationType': 'DEFAULT'|'CUSTOM',
                        'MetricsLevel': 'APPLICATION'|'TASK'|'OPERATOR'|'PARALLELISM',
                        'LogLevel': 'INFO'|'WARN'|'ERROR'|'DEBUG'
                    },
                    'ParallelismConfigurationDescription': {
                        'ConfigurationType': 'DEFAULT'|'CUSTOM',
                        'Parallelism': 123,
                        'ParallelismPerKPU': 123,
                        'CurrentParallelism': 123,
                        'AutoScalingEnabled': True|False
                    },
                    'JobPlanDescription': 'string'
                },
                'EnvironmentPropertyDescriptions': {
                    'PropertyGroupDescriptions': [
                        {
                            'PropertyGroupId': 'string',
                            'PropertyMap': {
                                'string': 'string'
                            }
                        },
                    ]
                },
                'ApplicationSnapshotConfigurationDescription': {
                    'SnapshotsEnabled': True|False
                },
                'VpcConfigurationDescriptions': [
                    {
                        'VpcConfigurationId': 'string',
                        'VpcId': 'string',
                        'SubnetIds': [
                            'string',
                        ],
                        'SecurityGroupIds': [
                            'string',
                        ]
                    },
                ]
            },
            'CloudWatchLoggingOptionDescriptions': [
                {
                    'CloudWatchLoggingOptionId': 'string',
                    'LogStreamARN': 'string',
                    'RoleARN': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_application_snapshot(ApplicationName=None, SnapshotName=None):
    """
    Returns information about a snapshot of application state data.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_application_snapshot(
        ApplicationName='string',
        SnapshotName='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of an existing application.\n

    :type SnapshotName: string
    :param SnapshotName: [REQUIRED]\nThe identifier of an application snapshot. You can retrieve this value using .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SnapshotDetails': {
        'SnapshotName': 'string',
        'SnapshotStatus': 'CREATING'|'READY'|'DELETING'|'FAILED',
        'ApplicationVersionId': 123,
        'SnapshotCreationTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

SnapshotDetails (dict) --
An object containing information about the application snapshot.

SnapshotName (string) --
The identifier for the application snapshot.

SnapshotStatus (string) --
The status of the application snapshot.

ApplicationVersionId (integer) --
The current application version ID when the snapshot was created.

SnapshotCreationTimestamp (datetime) --
The timestamp of the application snapshot.









Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.UnsupportedOperationException


    :return: {
        'SnapshotDetails': {
            'SnapshotName': 'string',
            'SnapshotStatus': 'CREATING'|'READY'|'DELETING'|'FAILED',
            'ApplicationVersionId': 123,
            'SnapshotCreationTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
    KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
    KinesisAnalyticsV2.Client.exceptions.UnsupportedOperationException
    
    """
    pass

def discover_input_schema(ResourceARN=None, ServiceExecutionRole=None, InputStartingPositionConfiguration=None, S3Configuration=None, InputProcessingConfiguration=None):
    """
    Infers a schema for an SQL-based Amazon Kinesis Data Analytics application by evaluating sample records on the specified streaming source (Kinesis data stream or Kinesis Data Firehose delivery stream) or Amazon S3 object. In the response, the operation returns the inferred schema and also the sample records that the operation used to infer the schema.
    You can use the inferred schema when configuring a streaming source for your application. When you create an application using the Kinesis Data Analytics console, the console uses this operation to infer a schema and show it in the console user interface.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.discover_input_schema(
        ResourceARN='string',
        ServiceExecutionRole='string',
        InputStartingPositionConfiguration={
            'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
        },
        S3Configuration={
            'BucketARN': 'string',
            'FileKey': 'string'
        },
        InputProcessingConfiguration={
            'InputLambdaProcessor': {
                'ResourceARN': 'string'
            }
        }
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: The Amazon Resource Name (ARN) of the streaming source.

    :type ServiceExecutionRole: string
    :param ServiceExecutionRole: [REQUIRED]\nThe ARN of the role that is used to access the streaming source.\n

    :type InputStartingPositionConfiguration: dict
    :param InputStartingPositionConfiguration: The point at which you want Kinesis Data Analytics to start reading records from the specified streaming source discovery purposes.\n\nInputStartingPosition (string) --The starting position on the stream.\n\nNOW - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued.\nTRIM_HORIZON - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream.\nLAST_STOPPED_POINT - Resume reading from where the application last stopped reading.\n\n\n\n

    :type S3Configuration: dict
    :param S3Configuration: Specify this parameter to discover a schema from data in an Amazon S3 object.\n\nBucketARN (string) -- [REQUIRED]The ARN of the S3 bucket that contains the data.\n\nFileKey (string) -- [REQUIRED]The name of the object that contains the data.\n\n\n

    :type InputProcessingConfiguration: dict
    :param InputProcessingConfiguration: The InputProcessingConfiguration to use to preprocess the records before discovering the schema of the records.\n\nInputLambdaProcessor (dict) -- [REQUIRED]The InputLambdaProcessor that is used to preprocess the records in the stream before being processed by your application code.\n\nResourceARN (string) -- [REQUIRED]The ARN of the AWS Lambda function that operates on records in the stream.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'InputSchema': {
        'RecordFormat': {
            'RecordFormatType': 'JSON'|'CSV',
            'MappingParameters': {
                'JSONMappingParameters': {
                    'RecordRowPath': 'string'
                },
                'CSVMappingParameters': {
                    'RecordRowDelimiter': 'string',
                    'RecordColumnDelimiter': 'string'
                }
            }
        },
        'RecordEncoding': 'string',
        'RecordColumns': [
            {
                'Name': 'string',
                'Mapping': 'string',
                'SqlType': 'string'
            },
        ]
    },
    'ParsedInputRecords': [
        [
            'string',
        ],
    ],
    'ProcessedInputRecords': [
        'string',
    ],
    'RawInputRecords': [
        'string',
    ]
}


Response Structure

(dict) --

InputSchema (dict) --
The schema inferred from the streaming source. It identifies the format of the data in the streaming source and how each data element maps to corresponding columns in the in-application stream that you can create.

RecordFormat (dict) --
Specifies the format of the records on the streaming source.

RecordFormatType (string) --
The type of record format.

MappingParameters (dict) --
When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters (dict) --
Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath (string) --
The path to the top-level parent that contains the records.



CSVMappingParameters (dict) --
Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter (string) --
The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.

RecordColumnDelimiter (string) --
The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.







RecordEncoding (string) --
Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns (list) --
A list of RecordColumn objects.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
Also used to describe the format of the reference data source.

Name (string) --
The name of the column that is created in the in-application input stream or reference table.

Mapping (string) --
A reference to the data element in the streaming input or the reference data source.

SqlType (string) --
The type of column created in the in-application input stream or reference table.







ParsedInputRecords (list) --
An array of elements, where each element corresponds to a row in a stream record (a stream record can have more than one row).

(list) --
(string) --




ProcessedInputRecords (list) --
The stream data that was modified by the processor specified in the InputProcessingConfiguration parameter.

(string) --


RawInputRecords (list) --
The raw stream data that was sampled to infer the schema.

(string) --








Exceptions

KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.UnableToDetectSchemaException
KinesisAnalyticsV2.Client.exceptions.ResourceProvisionedThroughputExceededException
KinesisAnalyticsV2.Client.exceptions.ServiceUnavailableException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException


    :return: {
        'InputSchema': {
            'RecordFormat': {
                'RecordFormatType': 'JSON'|'CSV',
                'MappingParameters': {
                    'JSONMappingParameters': {
                        'RecordRowPath': 'string'
                    },
                    'CSVMappingParameters': {
                        'RecordRowDelimiter': 'string',
                        'RecordColumnDelimiter': 'string'
                    }
                }
            },
            'RecordEncoding': 'string',
            'RecordColumns': [
                {
                    'Name': 'string',
                    'Mapping': 'string',
                    'SqlType': 'string'
                },
            ]
        },
        'ParsedInputRecords': [
            [
                'string',
            ],
        ],
        'ProcessedInputRecords': [
            'string',
        ],
        'RawInputRecords': [
            'string',
        ]
    }
    
    
    :returns: 
    (list) --
    (string) --
    
    
    
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

def list_application_snapshots(ApplicationName=None, Limit=None, NextToken=None):
    """
    Lists information about the current application snapshots.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_application_snapshots(
        ApplicationName='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of an existing application.\n

    :type Limit: integer
    :param Limit: The maximum number of application snapshots to list.

    :type NextToken: string
    :param NextToken: Use this parameter if you receive a NextToken response in a previous request that indicates that there is more output available. Set it to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :rtype: dict

ReturnsResponse Syntax
{
    'SnapshotSummaries': [
        {
            'SnapshotName': 'string',
            'SnapshotStatus': 'CREATING'|'READY'|'DELETING'|'FAILED',
            'ApplicationVersionId': 123,
            'SnapshotCreationTimestamp': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SnapshotSummaries (list) --
A collection of objects containing information about the application snapshots.

(dict) --
Provides details about a snapshot of application state.

SnapshotName (string) --
The identifier for the application snapshot.

SnapshotStatus (string) --
The status of the application snapshot.

ApplicationVersionId (integer) --
The current application version ID when the snapshot was created.

SnapshotCreationTimestamp (datetime) --
The timestamp of the application snapshot.





NextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.UnsupportedOperationException


    :return: {
        'SnapshotSummaries': [
            {
                'SnapshotName': 'string',
                'SnapshotStatus': 'CREATING'|'READY'|'DELETING'|'FAILED',
                'ApplicationVersionId': 123,
                'SnapshotCreationTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
    KinesisAnalyticsV2.Client.exceptions.UnsupportedOperationException
    
    """
    pass

def list_applications(Limit=None, NextToken=None):
    """
    Returns a list of Amazon Kinesis Data Analytics applications in your account. For each application, the response includes the application name, Amazon Resource Name (ARN), and status.
    If you want detailed information about a specific application, use  DescribeApplication .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_applications(
        Limit=123,
        NextToken='string'
    )
    
    
    :type Limit: integer
    :param Limit: The maximum number of applications to list.

    :type NextToken: string
    :param NextToken: If a previous command returned a pagination token, pass it into this value to retrieve the next set of results. For more information about pagination, see Using the AWS Command Line Interface\'s Pagination Options .

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationSummaries': [
        {
            'ApplicationName': 'string',
            'ApplicationARN': 'string',
            'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
            'ApplicationVersionId': 123,
            'RuntimeEnvironment': 'SQL-1_0'|'FLINK-1_6'|'FLINK-1_8'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ApplicationSummaries (list) --
A list of ApplicationSummary objects.

(dict) --
Provides application summary information, including the application Amazon Resource Name (ARN), name, and status.

ApplicationName (string) --
The name of the application.

ApplicationARN (string) --
The ARN of the application.

ApplicationStatus (string) --
The status of the application.

ApplicationVersionId (integer) --
Provides the current application version.

RuntimeEnvironment (string) --
The runtime environment for the application (SQL-1.0 or FLINK-1_6 ).





NextToken (string) --
The pagination token for the next set of results, or null if there are no additional results. Pass this token into a subsequent command to retrieve the next set of items For more information about pagination, see Using the AWS Command Line Interface\'s Pagination Options .







Exceptions

KinesisAnalyticsV2.Client.exceptions.InvalidRequestException


    :return: {
        'ApplicationSummaries': [
            {
                'ApplicationName': 'string',
                'ApplicationARN': 'string',
                'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
                'ApplicationVersionId': 123,
                'RuntimeEnvironment': 'SQL-1_0'|'FLINK-1_6'|'FLINK-1_8'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
    
    """
    pass

def list_tags_for_resource(ResourceARN=None):
    """
    Retrieves the list of key-value tags assigned to the application. For more information, see Using Tagging .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceARN='string'
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe ARN of the application for which to retrieve tags.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Tags (list) --The key-value tags assigned to the application.

(dict) --A key-value pair (the value is optional) that you can define and assign to AWS resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see Using Tagging .

Key (string) --The key of the key-value tag.

Value (string) --The value of the key-value tag. The value is optional.










Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def start_application(ApplicationName=None, RunConfiguration=None):
    """
    Starts the specified Amazon Kinesis Data Analytics application. After creating an application, you must exclusively call this operation to start your application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_application(
        ApplicationName='string',
        RunConfiguration={
            'FlinkRunConfiguration': {
                'AllowNonRestoredState': True|False
            },
            'SqlRunConfigurations': [
                {
                    'InputId': 'string',
                    'InputStartingPositionConfiguration': {
                        'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                    }
                },
            ],
            'ApplicationRestoreConfiguration': {
                'ApplicationRestoreType': 'SKIP_RESTORE_FROM_SNAPSHOT'|'RESTORE_FROM_LATEST_SNAPSHOT'|'RESTORE_FROM_CUSTOM_SNAPSHOT',
                'SnapshotName': 'string'
            }
        }
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of the application.\n

    :type RunConfiguration: dict
    :param RunConfiguration: [REQUIRED]\nIdentifies the run configuration (start parameters) of a Kinesis Data Analytics application.\n\nFlinkRunConfiguration (dict) --Describes the starting parameters for an Apache Flink-based Kinesis Data Analytics application.\n\nAllowNonRestoredState (boolean) --When restoring from a savepoint, specifies whether the runtime is allowed to skip a state that cannot be mapped to the new program. This will happen if the program is updated between savepoints to remove stateful parameters, and state data in the savepoint no longer corresponds to valid application data. For more information, see Allowing Non-Restored State in the Apache Flink documentation .\n\n\n\nSqlRunConfigurations (list) --Describes the starting parameters for an SQL-based Kinesis Data Analytics application.\n\n(dict) --Describes the starting parameters for an SQL-based Kinesis Data Analytics application.\n\nInputId (string) -- [REQUIRED]The input source ID. You can get this ID by calling the DescribeApplication operation.\n\nInputStartingPositionConfiguration (dict) -- [REQUIRED]The point at which you want the application to start processing records from the streaming source.\n\nInputStartingPosition (string) --The starting position on the stream.\n\nNOW - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued.\nTRIM_HORIZON - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream.\nLAST_STOPPED_POINT - Resume reading from where the application last stopped reading.\n\n\n\n\n\n\n\n\nApplicationRestoreConfiguration (dict) --Describes the restore behavior of a restarting application.\n\nApplicationRestoreType (string) -- [REQUIRED]Specifies how the application should be restored.\n\nSnapshotName (string) --The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if RESTORE_FROM_CUSTOM_SNAPSHOT is specified for the ApplicationRestoreType .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.InvalidApplicationConfigurationException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def stop_application(ApplicationName=None):
    """
    Stops the application from processing data. You can stop an application only if it is in the running state. You can use the  DescribeApplication operation to find the application state.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_application(
        ApplicationName='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of the running application to stop.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
KinesisAnalyticsV2.Client.exceptions.InvalidApplicationConfigurationException


    :return: {}
    
    
    :returns: 
    KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
    KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
    KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
    KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
    KinesisAnalyticsV2.Client.exceptions.InvalidApplicationConfigurationException
    
    """
    pass

def tag_resource(ResourceARN=None, Tags=None):
    """
    Adds one or more key-value tags to a Kinesis Analytics application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see Using Tagging .
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
    :param ResourceARN: [REQUIRED]\nThe ARN of the application to assign the tags.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe key-value tags to assign to the application.\n\n(dict) --A key-value pair (the value is optional) that you can define and assign to AWS resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see Using Tagging .\n\nKey (string) -- [REQUIRED]The key of the key-value tag.\n\nValue (string) --The value of the key-value tag. The value is optional.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.TooManyTagsException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceARN=None, TagKeys=None):
    """
    Removes one or more tags from a Kinesis Analytics application. For more information, see Using Tagging .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe ARN of the Kinesis Analytics application from which to remove the tags.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of keys of tags to remove from the specified application.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.TooManyTagsException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_application(ApplicationName=None, CurrentApplicationVersionId=None, ApplicationConfigurationUpdate=None, ServiceExecutionRoleUpdate=None, RunConfigurationUpdate=None, CloudWatchLoggingOptionUpdates=None):
    """
    Updates an existing Amazon Kinesis Data Analytics application. Using this operation, you can update application code, input configuration, and output configuration.
    Kinesis Data Analytics updates the ApplicationVersionId each time you update your application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_application(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        ApplicationConfigurationUpdate={
            'SqlApplicationConfigurationUpdate': {
                'InputUpdates': [
                    {
                        'InputId': 'string',
                        'NamePrefixUpdate': 'string',
                        'InputProcessingConfigurationUpdate': {
                            'InputLambdaProcessorUpdate': {
                                'ResourceARNUpdate': 'string'
                            }
                        },
                        'KinesisStreamsInputUpdate': {
                            'ResourceARNUpdate': 'string'
                        },
                        'KinesisFirehoseInputUpdate': {
                            'ResourceARNUpdate': 'string'
                        },
                        'InputSchemaUpdate': {
                            'RecordFormatUpdate': {
                                'RecordFormatType': 'JSON'|'CSV',
                                'MappingParameters': {
                                    'JSONMappingParameters': {
                                        'RecordRowPath': 'string'
                                    },
                                    'CSVMappingParameters': {
                                        'RecordRowDelimiter': 'string',
                                        'RecordColumnDelimiter': 'string'
                                    }
                                }
                            },
                            'RecordEncodingUpdate': 'string',
                            'RecordColumnUpdates': [
                                {
                                    'Name': 'string',
                                    'Mapping': 'string',
                                    'SqlType': 'string'
                                },
                            ]
                        },
                        'InputParallelismUpdate': {
                            'CountUpdate': 123
                        }
                    },
                ],
                'OutputUpdates': [
                    {
                        'OutputId': 'string',
                        'NameUpdate': 'string',
                        'KinesisStreamsOutputUpdate': {
                            'ResourceARNUpdate': 'string'
                        },
                        'KinesisFirehoseOutputUpdate': {
                            'ResourceARNUpdate': 'string'
                        },
                        'LambdaOutputUpdate': {
                            'ResourceARNUpdate': 'string'
                        },
                        'DestinationSchemaUpdate': {
                            'RecordFormatType': 'JSON'|'CSV'
                        }
                    },
                ],
                'ReferenceDataSourceUpdates': [
                    {
                        'ReferenceId': 'string',
                        'TableNameUpdate': 'string',
                        'S3ReferenceDataSourceUpdate': {
                            'BucketARNUpdate': 'string',
                            'FileKeyUpdate': 'string'
                        },
                        'ReferenceSchemaUpdate': {
                            'RecordFormat': {
                                'RecordFormatType': 'JSON'|'CSV',
                                'MappingParameters': {
                                    'JSONMappingParameters': {
                                        'RecordRowPath': 'string'
                                    },
                                    'CSVMappingParameters': {
                                        'RecordRowDelimiter': 'string',
                                        'RecordColumnDelimiter': 'string'
                                    }
                                }
                            },
                            'RecordEncoding': 'string',
                            'RecordColumns': [
                                {
                                    'Name': 'string',
                                    'Mapping': 'string',
                                    'SqlType': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'ApplicationCodeConfigurationUpdate': {
                'CodeContentTypeUpdate': 'PLAINTEXT'|'ZIPFILE',
                'CodeContentUpdate': {
                    'TextContentUpdate': 'string',
                    'ZipFileContentUpdate': b'bytes',
                    'S3ContentLocationUpdate': {
                        'BucketARNUpdate': 'string',
                        'FileKeyUpdate': 'string',
                        'ObjectVersionUpdate': 'string'
                    }
                }
            },
            'FlinkApplicationConfigurationUpdate': {
                'CheckpointConfigurationUpdate': {
                    'ConfigurationTypeUpdate': 'DEFAULT'|'CUSTOM',
                    'CheckpointingEnabledUpdate': True|False,
                    'CheckpointIntervalUpdate': 123,
                    'MinPauseBetweenCheckpointsUpdate': 123
                },
                'MonitoringConfigurationUpdate': {
                    'ConfigurationTypeUpdate': 'DEFAULT'|'CUSTOM',
                    'MetricsLevelUpdate': 'APPLICATION'|'TASK'|'OPERATOR'|'PARALLELISM',
                    'LogLevelUpdate': 'INFO'|'WARN'|'ERROR'|'DEBUG'
                },
                'ParallelismConfigurationUpdate': {
                    'ConfigurationTypeUpdate': 'DEFAULT'|'CUSTOM',
                    'ParallelismUpdate': 123,
                    'ParallelismPerKPUUpdate': 123,
                    'AutoScalingEnabledUpdate': True|False
                }
            },
            'EnvironmentPropertyUpdates': {
                'PropertyGroups': [
                    {
                        'PropertyGroupId': 'string',
                        'PropertyMap': {
                            'string': 'string'
                        }
                    },
                ]
            },
            'ApplicationSnapshotConfigurationUpdate': {
                'SnapshotsEnabledUpdate': True|False
            },
            'VpcConfigurationUpdates': [
                {
                    'VpcConfigurationId': 'string',
                    'SubnetIdUpdates': [
                        'string',
                    ],
                    'SecurityGroupIdUpdates': [
                        'string',
                    ]
                },
            ]
        },
        ServiceExecutionRoleUpdate='string',
        RunConfigurationUpdate={
            'FlinkRunConfiguration': {
                'AllowNonRestoredState': True|False
            },
            'ApplicationRestoreConfiguration': {
                'ApplicationRestoreType': 'SKIP_RESTORE_FROM_SNAPSHOT'|'RESTORE_FROM_LATEST_SNAPSHOT'|'RESTORE_FROM_CUSTOM_SNAPSHOT',
                'SnapshotName': 'string'
            }
        },
        CloudWatchLoggingOptionUpdates=[
            {
                'CloudWatchLoggingOptionId': 'string',
                'LogStreamARNUpdate': 'string'
            },
        ]
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe name of the application to update.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe current application version ID. You can retrieve the application version ID using DescribeApplication .\n

    :type ApplicationConfigurationUpdate: dict
    :param ApplicationConfigurationUpdate: Describes application configuration updates.\n\nSqlApplicationConfigurationUpdate (dict) --Describes updates to an SQL-based Kinesis Data Analytics application\'s configuration.\n\nInputUpdates (list) --The array of InputUpdate objects describing the new input streams used by the application.\n\n(dict) --For an SQL-based Amazon Kinesis Data Analytics application, describes updates to a specific input configuration (identified by the InputId of an application).\n\nInputId (string) -- [REQUIRED]The input ID of the application input to be updated.\n\nNamePrefixUpdate (string) --The name prefix for in-application streams that Kinesis Data Analytics creates for the specific streaming source.\n\nInputProcessingConfigurationUpdate (dict) --Describes updates to an InputProcessingConfiguration .\n\nInputLambdaProcessorUpdate (dict) -- [REQUIRED]Provides update information for an InputLambdaProcessor .\n\nResourceARNUpdate (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the new AWS Lambda function that is used to preprocess the records in the stream.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\n\n\n\n\nKinesisStreamsInputUpdate (dict) --If a Kinesis data stream is the streaming source to be updated, provides an updated stream Amazon Resource Name (ARN).\n\nResourceARNUpdate (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the input Kinesis data stream to read.\n\n\n\nKinesisFirehoseInputUpdate (dict) --If a Kinesis Data Firehose delivery stream is the streaming source to be updated, provides an updated stream ARN.\n\nResourceARNUpdate (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the input delivery stream to read.\n\n\n\nInputSchemaUpdate (dict) --Describes the data format on the streaming source, and how record elements on the streaming source map to columns of the in-application stream that is created.\n\nRecordFormatUpdate (dict) --Specifies the format of the records on the streaming source.\n\nRecordFormatType (string) -- [REQUIRED]The type of record format.\n\nMappingParameters (dict) --When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.\n\nJSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.\n\nRecordRowPath (string) -- [REQUIRED]The path to the top-level parent that contains the records.\n\n\n\nCSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).\n\nRecordRowDelimiter (string) -- [REQUIRED]The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.\n\nRecordColumnDelimiter (string) -- [REQUIRED]The column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.\n\n\n\n\n\n\n\nRecordEncodingUpdate (string) --Specifies the encoding of the records in the streaming source; for example, UTF-8.\n\nRecordColumnUpdates (list) --A list of RecordColumn objects. Each object describes the mapping of the streaming source element to the corresponding column in the in-application stream.\n\n(dict) --For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.\nAlso used to describe the format of the reference data source.\n\nName (string) -- [REQUIRED]The name of the column that is created in the in-application input stream or reference table.\n\nMapping (string) --A reference to the data element in the streaming input or the reference data source.\n\nSqlType (string) -- [REQUIRED]The type of column created in the in-application input stream or reference table.\n\n\n\n\n\n\n\nInputParallelismUpdate (dict) --Describes the parallelism updates (the number of in-application streams Kinesis Data Analytics creates for the specific streaming source).\n\nCountUpdate (integer) -- [REQUIRED]The number of in-application streams to create for the specified streaming source.\n\n\n\n\n\n\n\nOutputUpdates (list) --The array of OutputUpdate objects describing the new destination streams used by the application.\n\n(dict) --For an SQL-based Amazon Kinesis Data Analytics application, describes updates to the output configuration identified by the OutputId .\n\nOutputId (string) -- [REQUIRED]Identifies the specific output configuration that you want to update.\n\nNameUpdate (string) --If you want to specify a different in-application stream for this output configuration, use this field to specify the new in-application stream name.\n\nKinesisStreamsOutputUpdate (dict) --Describes a Kinesis data stream as the destination for the output.\n\nResourceARNUpdate (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Kinesis data stream where you want to write the output.\n\n\n\nKinesisFirehoseOutputUpdate (dict) --Describes a Kinesis Data Firehose delivery stream as the destination for the output.\n\nResourceARNUpdate (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the delivery stream to write to.\n\n\n\nLambdaOutputUpdate (dict) --Describes an AWS Lambda function as the destination for the output.\n\nResourceARNUpdate (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the destination AWS Lambda function.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\n\n\nDestinationSchemaUpdate (dict) --Describes the data format when records are written to the destination.\n\nRecordFormatType (string) -- [REQUIRED]Specifies the format of the records on the output stream.\n\n\n\n\n\n\n\nReferenceDataSourceUpdates (list) --The array of ReferenceDataSourceUpdate objects describing the new reference data sources used by the application.\n\n(dict) --When you update a reference data source configuration for a SQL-based Amazon Kinesis Data Analytics application, this object provides all the updated values (such as the source bucket name and object key name), the in-application table name that is created, and updated mapping information that maps the data in the Amazon S3 object to the in-application reference table that is created.\n\nReferenceId (string) -- [REQUIRED]The ID of the reference data source that is being updated. You can use the DescribeApplication operation to get this value.\n\nTableNameUpdate (string) --The in-application table name that is created by this update.\n\nS3ReferenceDataSourceUpdate (dict) --Describes the S3 bucket name, object key name, and IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf and populate the in-application reference table.\n\nBucketARNUpdate (string) --The Amazon Resource Name (ARN) of the S3 bucket.\n\nFileKeyUpdate (string) --The object key name.\n\n\n\nReferenceSchemaUpdate (dict) --Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.\n\nRecordFormat (dict) -- [REQUIRED]Specifies the format of the records on the streaming source.\n\nRecordFormatType (string) -- [REQUIRED]The type of record format.\n\nMappingParameters (dict) --When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.\n\nJSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.\n\nRecordRowPath (string) -- [REQUIRED]The path to the top-level parent that contains the records.\n\n\n\nCSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).\n\nRecordRowDelimiter (string) -- [REQUIRED]The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.\n\nRecordColumnDelimiter (string) -- [REQUIRED]The column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.\n\n\n\n\n\n\n\nRecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.\n\nRecordColumns (list) -- [REQUIRED]A list of RecordColumn objects.\n\n(dict) --For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.\nAlso used to describe the format of the reference data source.\n\nName (string) -- [REQUIRED]The name of the column that is created in the in-application input stream or reference table.\n\nMapping (string) --A reference to the data element in the streaming input or the reference data source.\n\nSqlType (string) -- [REQUIRED]The type of column created in the in-application input stream or reference table.\n\n\n\n\n\n\n\n\n\n\n\n\n\nApplicationCodeConfigurationUpdate (dict) --Describes updates to a Java-based Kinesis Data Analytics application\'s code configuration.\n\nCodeContentTypeUpdate (string) --Describes updates to the code content type.\n\nCodeContentUpdate (dict) --Describes updates to the code content of an application.\n\nTextContentUpdate (string) --Describes an update to the text code for an application.\n\nZipFileContentUpdate (bytes) --Describes an update to the zipped code for an application.\n\nS3ContentLocationUpdate (dict) --Describes an update to the location of code for an application.\n\nBucketARNUpdate (string) --The new Amazon Resource Name (ARN) for the S3 bucket containing the application code.\n\nFileKeyUpdate (string) --The new file key for the object containing the application code.\n\nObjectVersionUpdate (string) --The new version of the object containing the application code.\n\n\n\n\n\n\n\nFlinkApplicationConfigurationUpdate (dict) --Describes updates to a Java-based Kinesis Data Analytics application\'s configuration.\n\nCheckpointConfigurationUpdate (dict) --Describes updates to an application\'s checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance.\n\nConfigurationTypeUpdate (string) --Describes updates to whether the application uses the default checkpointing behavior of Kinesis Data Analytics. You must set this property to CUSTOM in order to set the CheckpointingEnabled , CheckpointInterval , or MinPauseBetweenCheckpoints parameters.\n\nNote\nIf this value is set to DEFAULT , the application will use the following values, even if they are set to other values using APIs or application code:\n\nCheckpointingEnabled: true\nCheckpointInterval: 60000\nMinPauseBetweenCheckpoints: 5000\n\n\n\nCheckpointingEnabledUpdate (boolean) --Describes updates to whether checkpointing is enabled for an application.\n\nNote\nIf CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a CheckpointingEnabled value of true , even if this value is set to another value using this API or in application code.\n\n\nCheckpointIntervalUpdate (integer) --Describes updates to the interval in milliseconds between checkpoint operations.\n\nNote\nIf CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a CheckpointInterval vaue of 60000, even if this value is set to another value using this API or in application code.\n\n\nMinPauseBetweenCheckpointsUpdate (integer) --Describes updates to the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.\n\nNote\nIf CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a MinPauseBetweenCheckpoints value of 5000, even if this value is set using this API or in application code.\n\n\n\n\nMonitoringConfigurationUpdate (dict) --Describes updates to the configuration parameters for Amazon CloudWatch logging for an application.\n\nConfigurationTypeUpdate (string) --Describes updates to whether to use the default CloudWatch logging configuration for an application. You must set this property to CUSTOM in order to set the LogLevel or MetricsLevel parameters.\n\nMetricsLevelUpdate (string) --Describes updates to the granularity of the CloudWatch Logs for an application.\n\nLogLevelUpdate (string) --Describes updates to the verbosity of the CloudWatch Logs for an application.\n\n\n\nParallelismConfigurationUpdate (dict) --Describes updates to the parameters for how an application executes multiple tasks simultaneously.\n\nConfigurationTypeUpdate (string) --Describes updates to whether the application uses the default parallelism for the Kinesis Data Analytics service, or if a custom parallelism is used. You must set this property to CUSTOM in order to change your application\'s AutoScalingEnabled , Parallelism , or ParallelismPerKPU properties.\n\nParallelismUpdate (integer) --Describes updates to the initial number of parallel tasks an application can perform. If AutoScalingEnabled is set to True, then Kinesis Data Analytics can increase the CurrentParallelism value in response to application load. The service can increase CurrentParallelism up to the maximum parallelism, which is ParalellismPerKPU times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service will reduce CurrentParallelism down to the Parallelism setting.\n\nParallelismPerKPUUpdate (integer) --Describes updates to the number of parallel tasks an application can perform per Kinesis Processing Unit (KPU) used by the application.\n\nAutoScalingEnabledUpdate (boolean) --Describes updates to whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.\n\n\n\n\n\nEnvironmentPropertyUpdates (dict) --Describes updates to the environment properties for a Java-based Kinesis Data Analytics application.\n\nPropertyGroups (list) -- [REQUIRED]Describes updates to the execution property groups.\n\n(dict) --Property key-value pairs passed into a Java-based Kinesis Data Analytics application.\n\nPropertyGroupId (string) -- [REQUIRED]Describes the key of an application execution property key-value pair.\n\nPropertyMap (dict) -- [REQUIRED]Describes the value of an application execution property key-value pair.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\n\n\nApplicationSnapshotConfigurationUpdate (dict) --Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.\n\nSnapshotsEnabledUpdate (boolean) -- [REQUIRED]Describes updates to whether snapshots are enabled for a Java-based Kinesis Data Analytics application.\n\n\n\nVpcConfigurationUpdates (list) --Updates to the array of descriptions of VPC configurations available to the application.\n\n(dict) --Describes updates to the VPC configuration used by the application.\n\nVpcConfigurationId (string) -- [REQUIRED]Describes an update to the ID of the VPC configuration.\n\nSubnetIdUpdates (list) --Describes updates to the array of Subnet IDs used by the VPC configuration.\n\n(string) --\n\n\nSecurityGroupIdUpdates (list) --Describes updates to the array of SecurityGroup IDs used by the VPC configuration.\n\n(string) --\n\n\n\n\n\n\n\n

    :type ServiceExecutionRoleUpdate: string
    :param ServiceExecutionRoleUpdate: Describes updates to the service execution role.

    :type RunConfigurationUpdate: dict
    :param RunConfigurationUpdate: Describes updates to the application\'s starting parameters.\n\nFlinkRunConfiguration (dict) --Describes the starting parameters for an Apache Flink-based Kinesis Data Analytics application.\n\nAllowNonRestoredState (boolean) --When restoring from a savepoint, specifies whether the runtime is allowed to skip a state that cannot be mapped to the new program. This will happen if the program is updated between savepoints to remove stateful parameters, and state data in the savepoint no longer corresponds to valid application data. For more information, see Allowing Non-Restored State in the Apache Flink documentation .\n\n\n\nApplicationRestoreConfiguration (dict) --Describes updates to the restore behavior of a restarting application.\n\nApplicationRestoreType (string) -- [REQUIRED]Specifies how the application should be restored.\n\nSnapshotName (string) --The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if RESTORE_FROM_CUSTOM_SNAPSHOT is specified for the ApplicationRestoreType .\n\n\n\n\n

    :type CloudWatchLoggingOptionUpdates: list
    :param CloudWatchLoggingOptionUpdates: Describes application Amazon CloudWatch logging option updates. You can only update existing CloudWatch logging options with this action. To add a new CloudWatch logging option, use AddApplicationCloudWatchLoggingOption .\n\n(dict) --Describes the Amazon CloudWatch logging option updates.\n\nCloudWatchLoggingOptionId (string) -- [REQUIRED]The ID of the CloudWatch logging option to update\n\nLogStreamARNUpdate (string) --The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationDetail': {
        'ApplicationARN': 'string',
        'ApplicationDescription': 'string',
        'ApplicationName': 'string',
        'RuntimeEnvironment': 'SQL-1_0'|'FLINK-1_6'|'FLINK-1_8',
        'ServiceExecutionRole': 'string',
        'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
        'ApplicationVersionId': 123,
        'CreateTimestamp': datetime(2015, 1, 1),
        'LastUpdateTimestamp': datetime(2015, 1, 1),
        'ApplicationConfigurationDescription': {
            'SqlApplicationConfigurationDescription': {
                'InputDescriptions': [
                    {
                        'InputId': 'string',
                        'NamePrefix': 'string',
                        'InAppStreamNames': [
                            'string',
                        ],
                        'InputProcessingConfigurationDescription': {
                            'InputLambdaProcessorDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            }
                        },
                        'KinesisStreamsInputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'KinesisFirehoseInputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'InputSchema': {
                            'RecordFormat': {
                                'RecordFormatType': 'JSON'|'CSV',
                                'MappingParameters': {
                                    'JSONMappingParameters': {
                                        'RecordRowPath': 'string'
                                    },
                                    'CSVMappingParameters': {
                                        'RecordRowDelimiter': 'string',
                                        'RecordColumnDelimiter': 'string'
                                    }
                                }
                            },
                            'RecordEncoding': 'string',
                            'RecordColumns': [
                                {
                                    'Name': 'string',
                                    'Mapping': 'string',
                                    'SqlType': 'string'
                                },
                            ]
                        },
                        'InputParallelism': {
                            'Count': 123
                        },
                        'InputStartingPositionConfiguration': {
                            'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                        }
                    },
                ],
                'OutputDescriptions': [
                    {
                        'OutputId': 'string',
                        'Name': 'string',
                        'KinesisStreamsOutputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'KinesisFirehoseOutputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'LambdaOutputDescription': {
                            'ResourceARN': 'string',
                            'RoleARN': 'string'
                        },
                        'DestinationSchema': {
                            'RecordFormatType': 'JSON'|'CSV'
                        }
                    },
                ],
                'ReferenceDataSourceDescriptions': [
                    {
                        'ReferenceId': 'string',
                        'TableName': 'string',
                        'S3ReferenceDataSourceDescription': {
                            'BucketARN': 'string',
                            'FileKey': 'string',
                            'ReferenceRoleARN': 'string'
                        },
                        'ReferenceSchema': {
                            'RecordFormat': {
                                'RecordFormatType': 'JSON'|'CSV',
                                'MappingParameters': {
                                    'JSONMappingParameters': {
                                        'RecordRowPath': 'string'
                                    },
                                    'CSVMappingParameters': {
                                        'RecordRowDelimiter': 'string',
                                        'RecordColumnDelimiter': 'string'
                                    }
                                }
                            },
                            'RecordEncoding': 'string',
                            'RecordColumns': [
                                {
                                    'Name': 'string',
                                    'Mapping': 'string',
                                    'SqlType': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'ApplicationCodeConfigurationDescription': {
                'CodeContentType': 'PLAINTEXT'|'ZIPFILE',
                'CodeContentDescription': {
                    'TextContent': 'string',
                    'CodeMD5': 'string',
                    'CodeSize': 123,
                    'S3ApplicationCodeLocationDescription': {
                        'BucketARN': 'string',
                        'FileKey': 'string',
                        'ObjectVersion': 'string'
                    }
                }
            },
            'RunConfigurationDescription': {
                'ApplicationRestoreConfigurationDescription': {
                    'ApplicationRestoreType': 'SKIP_RESTORE_FROM_SNAPSHOT'|'RESTORE_FROM_LATEST_SNAPSHOT'|'RESTORE_FROM_CUSTOM_SNAPSHOT',
                    'SnapshotName': 'string'
                }
            },
            'FlinkApplicationConfigurationDescription': {
                'CheckpointConfigurationDescription': {
                    'ConfigurationType': 'DEFAULT'|'CUSTOM',
                    'CheckpointingEnabled': True|False,
                    'CheckpointInterval': 123,
                    'MinPauseBetweenCheckpoints': 123
                },
                'MonitoringConfigurationDescription': {
                    'ConfigurationType': 'DEFAULT'|'CUSTOM',
                    'MetricsLevel': 'APPLICATION'|'TASK'|'OPERATOR'|'PARALLELISM',
                    'LogLevel': 'INFO'|'WARN'|'ERROR'|'DEBUG'
                },
                'ParallelismConfigurationDescription': {
                    'ConfigurationType': 'DEFAULT'|'CUSTOM',
                    'Parallelism': 123,
                    'ParallelismPerKPU': 123,
                    'CurrentParallelism': 123,
                    'AutoScalingEnabled': True|False
                },
                'JobPlanDescription': 'string'
            },
            'EnvironmentPropertyDescriptions': {
                'PropertyGroupDescriptions': [
                    {
                        'PropertyGroupId': 'string',
                        'PropertyMap': {
                            'string': 'string'
                        }
                    },
                ]
            },
            'ApplicationSnapshotConfigurationDescription': {
                'SnapshotsEnabled': True|False
            },
            'VpcConfigurationDescriptions': [
                {
                    'VpcConfigurationId': 'string',
                    'VpcId': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
            ]
        },
        'CloudWatchLoggingOptionDescriptions': [
            {
                'CloudWatchLoggingOptionId': 'string',
                'LogStreamARN': 'string',
                'RoleARN': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

ApplicationDetail (dict) --
Describes application updates.

ApplicationARN (string) --
The ARN of the application.

ApplicationDescription (string) --
The description of the application.

ApplicationName (string) --
The name of the application.

RuntimeEnvironment (string) --
The runtime environment for the application (SQL-1.0 or FLINK-1_6 ).

ServiceExecutionRole (string) --
Specifies the IAM role that the application uses to access external resources.

ApplicationStatus (string) --
The status of the application.

ApplicationVersionId (integer) --
Provides the current application version. Kinesis Data Analytics updates the ApplicationVersionId each time you update the application.

CreateTimestamp (datetime) --
The current timestamp when the application was created.

LastUpdateTimestamp (datetime) --
The current timestamp when the application was last updated.

ApplicationConfigurationDescription (dict) --
Provides details about the application\'s SQL or Java code and starting parameters.

SqlApplicationConfigurationDescription (dict) --
The details about inputs, outputs, and reference data sources for an SQL-based Kinesis Data Analytics application.

InputDescriptions (list) --
The array of  InputDescription objects describing the input streams used by the application.

(dict) --
Describes the application input configuration for an SQL-based Amazon Kinesis Data Analytics application.

InputId (string) --
The input ID that is associated with the application input. This is the ID that Kinesis Data Analytics assigns to each input configuration that you add to your application.

NamePrefix (string) --
The in-application name prefix.

InAppStreamNames (list) --
Returns the in-application stream names that are mapped to the stream source.

(string) --


InputProcessingConfigurationDescription (dict) --
The description of the preprocessor that executes on records in this input before the application\'s code is run.

InputLambdaProcessorDescription (dict) --
Provides configuration information about the associated  InputLambdaProcessorDescription

ResourceARN (string) --
The ARN of the AWS Lambda function that is used to preprocess the records in the stream.

Note
To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda


RoleARN (string) --
The ARN of the IAM role that is used to access the AWS Lambda function.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.






KinesisStreamsInputDescription (dict) --
If a Kinesis data stream is configured as a streaming source, provides the Kinesis data stream\'s Amazon Resource Name (ARN).

ResourceARN (string) --
The Amazon Resource Name (ARN) of the Kinesis data stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




KinesisFirehoseInputDescription (dict) --
If a Kinesis Data Firehose delivery stream is configured as a streaming source, provides the delivery stream\'s ARN.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the delivery stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




InputSchema (dict) --
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.

RecordFormat (dict) --
Specifies the format of the records on the streaming source.

RecordFormatType (string) --
The type of record format.

MappingParameters (dict) --
When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters (dict) --
Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath (string) --
The path to the top-level parent that contains the records.



CSVMappingParameters (dict) --
Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter (string) --
The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.

RecordColumnDelimiter (string) --
The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.







RecordEncoding (string) --
Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns (list) --
A list of RecordColumn objects.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
Also used to describe the format of the reference data source.

Name (string) --
The name of the column that is created in the in-application input stream or reference table.

Mapping (string) --
A reference to the data element in the streaming input or the reference data source.

SqlType (string) --
The type of column created in the in-application input stream or reference table.







InputParallelism (dict) --
Describes the configured parallelism (number of in-application streams mapped to the streaming source).

Count (integer) --
The number of in-application streams to create.



InputStartingPositionConfiguration (dict) --
The point at which the application is configured to read from the input stream.

InputStartingPosition (string) --
The starting position on the stream.

NOW - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued.
TRIM_HORIZON - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream.
LAST_STOPPED_POINT - Resume reading from where the application last stopped reading.








OutputDescriptions (list) --
The array of  OutputDescription objects describing the destination streams used by the application.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

OutputId (string) --
A unique identifier for the output configuration.

Name (string) --
The name of the in-application stream that is configured as output.

KinesisStreamsOutputDescription (dict) --
Describes the Kinesis data stream that is configured as the destination where output is written.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the Kinesis data stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




KinesisFirehoseOutputDescription (dict) --
Describes the Kinesis Data Firehose delivery stream that is configured as the destination where output is written.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the delivery stream.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




LambdaOutputDescription (dict) --
Describes the Lambda function that is configured as the destination where output is written.

ResourceARN (string) --
The Amazon Resource Name (ARN) of the destination Lambda function.

RoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to write to the destination function.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




DestinationSchema (dict) --
The data format used for writing data to the destination.

RecordFormatType (string) --
Specifies the format of the records on the output stream.







ReferenceDataSourceDescriptions (list) --
The array of  ReferenceDataSourceDescription objects describing the reference data sources used by the application.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the reference data source configured for an application.

ReferenceId (string) --
The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns when you add the reference data source to your application using the  CreateApplication or  UpdateApplication operation.

TableName (string) --
The in-application table name created by the specific reference data source configuration.

S3ReferenceDataSourceDescription (dict) --
Provides the Amazon S3 bucket name, the object key name that contains the reference data.

BucketARN (string) --
The Amazon Resource Name (ARN) of the S3 bucket.

FileKey (string) --
Amazon S3 object key name.

ReferenceRoleARN (string) --
The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table.

Note
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.




ReferenceSchema (dict) --
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

RecordFormat (dict) --
Specifies the format of the records on the streaming source.

RecordFormatType (string) --
The type of record format.

MappingParameters (dict) --
When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters (dict) --
Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath (string) --
The path to the top-level parent that contains the records.



CSVMappingParameters (dict) --
Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter (string) --
The row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.

RecordColumnDelimiter (string) --
The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.







RecordEncoding (string) --
Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns (list) --
A list of RecordColumn objects.

(dict) --
For an SQL-based Amazon Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
Also used to describe the format of the reference data source.

Name (string) --
The name of the column that is created in the in-application input stream or reference table.

Mapping (string) --
A reference to the data element in the streaming input or the reference data source.

SqlType (string) --
The type of column created in the in-application input stream or reference table.













ApplicationCodeConfigurationDescription (dict) --
The details about the application code for a Java-based Kinesis Data Analytics application.

CodeContentType (string) --
Specifies whether the code content is in text or zip format.

CodeContentDescription (dict) --
Describes details about the location and format of the application code.

TextContent (string) --
The text-format code

CodeMD5 (string) --
The checksum that can be used to validate zip-format code.

CodeSize (integer) --
The size in bytes of the application code. Can be used to validate zip-format code.

S3ApplicationCodeLocationDescription (dict) --
The S3 bucket Amazon Resource Name (ARN), file key, and object version of the application code stored in Amazon S3.

BucketARN (string) --
The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

FileKey (string) --
The file key for the object containing the application code.

ObjectVersion (string) --
The version of the object containing the application code.







RunConfigurationDescription (dict) --
The details about the starting properties for a Kinesis Data Analytics application.

ApplicationRestoreConfigurationDescription (dict) --
Describes the restore behavior of a restarting application.

ApplicationRestoreType (string) --
Specifies how the application should be restored.

SnapshotName (string) --
The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if RESTORE_FROM_CUSTOM_SNAPSHOT is specified for the ApplicationRestoreType .





FlinkApplicationConfigurationDescription (dict) --
The details about a Java-based Kinesis Data Analytics application.

CheckpointConfigurationDescription (dict) --
Describes an application\'s checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance.

ConfigurationType (string) --
Describes whether the application uses the default checkpointing behavior in Kinesis Data Analytics.

Note
If this value is set to DEFAULT , the application will use the following values, even if they are set to other values using APIs or application code:

CheckpointingEnabled: true
CheckpointInterval: 60000
MinPauseBetweenCheckpoints: 5000



CheckpointingEnabled (boolean) --
Describes whether checkpointing is enabled for a Java-based Kinesis Data Analytics application.

Note
If CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a CheckpointingEnabled value of true , even if this value is set to another value using this API or in application code.


CheckpointInterval (integer) --
Describes the interval in milliseconds between checkpoint operations.

Note
If CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a CheckpointInterval vaue of 60000, even if this value is set to another value using this API or in application code.


MinPauseBetweenCheckpoints (integer) --
Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.

Note
If CheckpointConfiguration.ConfigurationType is DEFAULT , the application will use a MinPauseBetweenCheckpoints value of 5000, even if this value is set using this API or in application code.




MonitoringConfigurationDescription (dict) --
Describes configuration parameters for Amazon CloudWatch logging for an application.

ConfigurationType (string) --
Describes whether to use the default CloudWatch logging configuration for an application.

MetricsLevel (string) --
Describes the granularity of the CloudWatch Logs for an application.

LogLevel (string) --
Describes the verbosity of the CloudWatch Logs for an application.



ParallelismConfigurationDescription (dict) --
Describes parameters for how an application executes multiple tasks simultaneously.

ConfigurationType (string) --
Describes whether the application uses the default parallelism for the Kinesis Data Analytics service.

Parallelism (integer) --
Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics application can perform. If AutoScalingEnabled is set to True, then Kinesis Data Analytics can increase the CurrentParallelism value in response to application load. The service can increase CurrentParallelism up to the maximum parallelism, which is ParalellismPerKPU times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the CurrentParallelism value down to the Parallelism setting.

ParallelismPerKPU (integer) --
Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application can perform per Kinesis Processing Unit (KPU) used by the application.

CurrentParallelism (integer) --
Describes the current number of parallel tasks that a Java-based Kinesis Data Analytics application can perform. If AutoScalingEnabled is set to True, Kinesis Data Analytics can increase this value in response to application load. The service can increase this value up to the maximum parallelism, which is ParalellismPerKPU times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the CurrentParallelism value down to the Parallelism setting.

AutoScalingEnabled (boolean) --
Describes whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.



JobPlanDescription (string) --
The job plan for an application. For more information about the job plan, see Jobs and Scheduling in the Apache Flink Documentation . To retrieve the job plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails parameter of the  DescribeApplication operation.



EnvironmentPropertyDescriptions (dict) --
Describes execution properties for a Java-based Kinesis Data Analytics application.

PropertyGroupDescriptions (list) --
Describes the execution property groups.

(dict) --
Property key-value pairs passed into a Java-based Kinesis Data Analytics application.

PropertyGroupId (string) --
Describes the key of an application execution property key-value pair.

PropertyMap (dict) --
Describes the value of an application execution property key-value pair.

(string) --
(string) --










ApplicationSnapshotConfigurationDescription (dict) --
Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.

SnapshotsEnabled (boolean) --
Describes whether snapshots are enabled for a Java-based Kinesis Data Analytics application.



VpcConfigurationDescriptions (list) --
The array of descriptions of VPC configurations available to the application.

(dict) --
Describes the parameters of a VPC used by the application.

VpcConfigurationId (string) --
The ID of the VPC configuration.

VpcId (string) --
The ID of the associated VPC.

SubnetIds (list) --
The array of Subnet IDs used by the VPC configuration.

(string) --


SecurityGroupIds (list) --
The array of SecurityGroup IDs used by the VPC configuration.

(string) --








CloudWatchLoggingOptionDescriptions (list) --
Describes the application Amazon CloudWatch logging options.

(dict) --
Describes the Amazon CloudWatch logging option.

CloudWatchLoggingOptionId (string) --
The ID of the CloudWatch logging option description.

LogStreamARN (string) --
The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

RoleARN (string) --
The IAM ARN of the role to use to send application messages.

Note
Provided for backward compatibility. Applications created with the current API version have an application-level service execution role rather than a resource-level role.














Exceptions

KinesisAnalyticsV2.Client.exceptions.CodeValidationException
KinesisAnalyticsV2.Client.exceptions.ResourceNotFoundException
KinesisAnalyticsV2.Client.exceptions.ResourceInUseException
KinesisAnalyticsV2.Client.exceptions.InvalidArgumentException
KinesisAnalyticsV2.Client.exceptions.ConcurrentModificationException
KinesisAnalyticsV2.Client.exceptions.InvalidRequestException
KinesisAnalyticsV2.Client.exceptions.InvalidApplicationConfigurationException


    :return: {
        'ApplicationDetail': {
            'ApplicationARN': 'string',
            'ApplicationDescription': 'string',
            'ApplicationName': 'string',
            'RuntimeEnvironment': 'SQL-1_0'|'FLINK-1_6'|'FLINK-1_8',
            'ServiceExecutionRole': 'string',
            'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
            'ApplicationVersionId': 123,
            'CreateTimestamp': datetime(2015, 1, 1),
            'LastUpdateTimestamp': datetime(2015, 1, 1),
            'ApplicationConfigurationDescription': {
                'SqlApplicationConfigurationDescription': {
                    'InputDescriptions': [
                        {
                            'InputId': 'string',
                            'NamePrefix': 'string',
                            'InAppStreamNames': [
                                'string',
                            ],
                            'InputProcessingConfigurationDescription': {
                                'InputLambdaProcessorDescription': {
                                    'ResourceARN': 'string',
                                    'RoleARN': 'string'
                                }
                            },
                            'KinesisStreamsInputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'KinesisFirehoseInputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'InputSchema': {
                                'RecordFormat': {
                                    'RecordFormatType': 'JSON'|'CSV',
                                    'MappingParameters': {
                                        'JSONMappingParameters': {
                                            'RecordRowPath': 'string'
                                        },
                                        'CSVMappingParameters': {
                                            'RecordRowDelimiter': 'string',
                                            'RecordColumnDelimiter': 'string'
                                        }
                                    }
                                },
                                'RecordEncoding': 'string',
                                'RecordColumns': [
                                    {
                                        'Name': 'string',
                                        'Mapping': 'string',
                                        'SqlType': 'string'
                                    },
                                ]
                            },
                            'InputParallelism': {
                                'Count': 123
                            },
                            'InputStartingPositionConfiguration': {
                                'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                            }
                        },
                    ],
                    'OutputDescriptions': [
                        {
                            'OutputId': 'string',
                            'Name': 'string',
                            'KinesisStreamsOutputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'KinesisFirehoseOutputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'LambdaOutputDescription': {
                                'ResourceARN': 'string',
                                'RoleARN': 'string'
                            },
                            'DestinationSchema': {
                                'RecordFormatType': 'JSON'|'CSV'
                            }
                        },
                    ],
                    'ReferenceDataSourceDescriptions': [
                        {
                            'ReferenceId': 'string',
                            'TableName': 'string',
                            'S3ReferenceDataSourceDescription': {
                                'BucketARN': 'string',
                                'FileKey': 'string',
                                'ReferenceRoleARN': 'string'
                            },
                            'ReferenceSchema': {
                                'RecordFormat': {
                                    'RecordFormatType': 'JSON'|'CSV',
                                    'MappingParameters': {
                                        'JSONMappingParameters': {
                                            'RecordRowPath': 'string'
                                        },
                                        'CSVMappingParameters': {
                                            'RecordRowDelimiter': 'string',
                                            'RecordColumnDelimiter': 'string'
                                        }
                                    }
                                },
                                'RecordEncoding': 'string',
                                'RecordColumns': [
                                    {
                                        'Name': 'string',
                                        'Mapping': 'string',
                                        'SqlType': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'ApplicationCodeConfigurationDescription': {
                    'CodeContentType': 'PLAINTEXT'|'ZIPFILE',
                    'CodeContentDescription': {
                        'TextContent': 'string',
                        'CodeMD5': 'string',
                        'CodeSize': 123,
                        'S3ApplicationCodeLocationDescription': {
                            'BucketARN': 'string',
                            'FileKey': 'string',
                            'ObjectVersion': 'string'
                        }
                    }
                },
                'RunConfigurationDescription': {
                    'ApplicationRestoreConfigurationDescription': {
                        'ApplicationRestoreType': 'SKIP_RESTORE_FROM_SNAPSHOT'|'RESTORE_FROM_LATEST_SNAPSHOT'|'RESTORE_FROM_CUSTOM_SNAPSHOT',
                        'SnapshotName': 'string'
                    }
                },
                'FlinkApplicationConfigurationDescription': {
                    'CheckpointConfigurationDescription': {
                        'ConfigurationType': 'DEFAULT'|'CUSTOM',
                        'CheckpointingEnabled': True|False,
                        'CheckpointInterval': 123,
                        'MinPauseBetweenCheckpoints': 123
                    },
                    'MonitoringConfigurationDescription': {
                        'ConfigurationType': 'DEFAULT'|'CUSTOM',
                        'MetricsLevel': 'APPLICATION'|'TASK'|'OPERATOR'|'PARALLELISM',
                        'LogLevel': 'INFO'|'WARN'|'ERROR'|'DEBUG'
                    },
                    'ParallelismConfigurationDescription': {
                        'ConfigurationType': 'DEFAULT'|'CUSTOM',
                        'Parallelism': 123,
                        'ParallelismPerKPU': 123,
                        'CurrentParallelism': 123,
                        'AutoScalingEnabled': True|False
                    },
                    'JobPlanDescription': 'string'
                },
                'EnvironmentPropertyDescriptions': {
                    'PropertyGroupDescriptions': [
                        {
                            'PropertyGroupId': 'string',
                            'PropertyMap': {
                                'string': 'string'
                            }
                        },
                    ]
                },
                'ApplicationSnapshotConfigurationDescription': {
                    'SnapshotsEnabled': True|False
                },
                'VpcConfigurationDescriptions': [
                    {
                        'VpcConfigurationId': 'string',
                        'VpcId': 'string',
                        'SubnetIds': [
                            'string',
                        ],
                        'SecurityGroupIds': [
                            'string',
                        ]
                    },
                ]
            },
            'CloudWatchLoggingOptionDescriptions': [
                {
                    'CloudWatchLoggingOptionId': 'string',
                    'LogStreamARN': 'string',
                    'RoleARN': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

