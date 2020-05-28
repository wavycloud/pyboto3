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
    Adds a CloudWatch log stream to monitor application configuration errors. For more information about using CloudWatch log streams with Amazon Kinesis Analytics applications, see Working with Amazon CloudWatch Logs .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_application_cloud_watch_logging_option(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        CloudWatchLoggingOption={
            'LogStreamARN': 'string',
            'RoleARN': 'string'
        }
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe Kinesis Analytics application name.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe version ID of the Kinesis Analytics application.\n

    :type CloudWatchLoggingOption: dict
    :param CloudWatchLoggingOption: [REQUIRED]\nProvides the CloudWatch log stream Amazon Resource Name (ARN) and the IAM role ARN. Note: To write application messages to CloudWatch, the IAM role that is used must have the PutLogEvents policy action enabled.\n\nLogStreamARN (string) -- [REQUIRED]ARN of the CloudWatch log to receive application messages.\n\nRoleARN (string) -- [REQUIRED]IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role that is used must have the PutLogEvents policy action enabled.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.ConcurrentModificationException
KinesisAnalytics.Client.exceptions.UnsupportedOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def add_application_input(ApplicationName=None, CurrentApplicationVersionId=None, Input=None):
    """
    Adds a streaming source to your Amazon Kinesis application. For conceptual information, see Configuring Application Input .
    You can add a streaming source either when you create an application or you can use this operation to add a streaming source after you create an application. For more information, see CreateApplication .
    Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the DescribeApplication operation to find the current application version.
    This operation requires permissions to perform the kinesisanalytics:AddApplicationInput action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_application_input(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        Input={
            'NamePrefix': 'string',
            'InputProcessingConfiguration': {
                'InputLambdaProcessor': {
                    'ResourceARN': 'string',
                    'RoleARN': 'string'
                }
            },
            'KinesisStreamsInput': {
                'ResourceARN': 'string',
                'RoleARN': 'string'
            },
            'KinesisFirehoseInput': {
                'ResourceARN': 'string',
                'RoleARN': 'string'
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
    :param ApplicationName: [REQUIRED]\nName of your existing Amazon Kinesis Analytics application to which you want to add the streaming source.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nCurrent version of your Amazon Kinesis Analytics application. You can use the DescribeApplication operation to find the current application version.\n

    :type Input: dict
    :param Input: [REQUIRED]\nThe Input to add.\n\nNamePrefix (string) -- [REQUIRED]Name prefix to use when creating an in-application stream. Suppose that you specify a prefix 'MyInApplicationStream.' Amazon Kinesis Analytics then creates one or more (as per the InputParallelism count you specified) in-application streams with names 'MyInApplicationStream_001,' 'MyInApplicationStream_002,' and so on.\n\nInputProcessingConfiguration (dict) --The InputProcessingConfiguration for the input. An input processor transforms records as they are received from the stream, before the application\'s SQL code executes. Currently, the only input processing configuration available is InputLambdaProcessor .\n\nInputLambdaProcessor (dict) -- [REQUIRED]The InputLambdaProcessor that is used to preprocess the records in the stream before being processed by your application code.\n\nResourceARN (string) -- [REQUIRED]The ARN of the AWS Lambda function that operates on records in the stream.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\nRoleARN (string) -- [REQUIRED]The ARN of the IAM role that is used to access the AWS Lambda function.\n\n\n\n\n\nKinesisStreamsInput (dict) --If the streaming source is an Amazon Kinesis stream, identifies the stream\'s Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.\nNote: Either KinesisStreamsInput or KinesisFirehoseInput is required.\n\nResourceARN (string) -- [REQUIRED]ARN of the input Amazon Kinesis stream to read.\n\nRoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.\n\n\n\nKinesisFirehoseInput (dict) --If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the delivery stream\'s ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.\nNote: Either KinesisStreamsInput or KinesisFirehoseInput is required.\n\nResourceARN (string) -- [REQUIRED]ARN of the input delivery stream.\n\nRoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to make sure that the role has the necessary permissions to access the stream.\n\n\n\nInputParallelism (dict) --Describes the number of in-application streams to create.\nData from your source is routed to these in-application input streams.\n(see Configuring Application Input .\n\nCount (integer) --Number of in-application streams to create. For more information, see Limits .\n\n\n\nInputSchema (dict) -- [REQUIRED]Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.\nAlso used to describe the format of the reference data source.\n\nRecordFormat (dict) -- [REQUIRED]Specifies the format of the records on the streaming source.\n\nRecordFormatType (string) -- [REQUIRED]The type of record format.\n\nMappingParameters (dict) --When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.\n\nJSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.\n\nRecordRowPath (string) -- [REQUIRED]Path to the top-level parent that contains the records.\n\n\n\nCSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).\n\nRecordRowDelimiter (string) -- [REQUIRED]Row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.\n\nRecordColumnDelimiter (string) -- [REQUIRED]Column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.\n\n\n\n\n\n\n\nRecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.\n\nRecordColumns (list) -- [REQUIRED]A list of RecordColumn objects.\n\n(dict) --Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.\nAlso used to describe the format of the reference data source.\n\nName (string) -- [REQUIRED]Name of the column created in the in-application input stream or reference table.\n\nMapping (string) --Reference to the data element in the streaming input or the reference data source. This element is required if the RecordFormatType is JSON .\n\nSqlType (string) -- [REQUIRED]Type of column created in the in-application input stream or reference table.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.ConcurrentModificationException
KinesisAnalytics.Client.exceptions.CodeValidationException
KinesisAnalytics.Client.exceptions.UnsupportedOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def add_application_input_processing_configuration(ApplicationName=None, CurrentApplicationVersionId=None, InputId=None, InputProcessingConfiguration=None):
    """
    Adds an InputProcessingConfiguration to an application. An input processor preprocesses records on the input stream before the application\'s SQL code executes. Currently, the only input processor available is AWS Lambda .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_application_input_processing_configuration(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        InputId='string',
        InputProcessingConfiguration={
            'InputLambdaProcessor': {
                'ResourceARN': 'string',
                'RoleARN': 'string'
            }
        }
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nName of the application to which you want to add the input processing configuration.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nVersion of the application to which you want to add the input processing configuration. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.\n

    :type InputId: string
    :param InputId: [REQUIRED]\nThe ID of the input configuration to add the input processing configuration to. You can get a list of the input IDs for an application using the DescribeApplication operation.\n

    :type InputProcessingConfiguration: dict
    :param InputProcessingConfiguration: [REQUIRED]\nThe InputProcessingConfiguration to add to the application.\n\nInputLambdaProcessor (dict) -- [REQUIRED]The InputLambdaProcessor that is used to preprocess the records in the stream before being processed by your application code.\n\nResourceARN (string) -- [REQUIRED]The ARN of the AWS Lambda function that operates on records in the stream.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\nRoleARN (string) -- [REQUIRED]The ARN of the IAM role that is used to access the AWS Lambda function.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.ConcurrentModificationException
KinesisAnalytics.Client.exceptions.UnsupportedOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def add_application_output(ApplicationName=None, CurrentApplicationVersionId=None, Output=None):
    """
    Adds an external destination to your Amazon Kinesis Analytics application.
    If you want Amazon Kinesis Analytics to deliver data from an in-application stream within your application to an external destination (such as an Amazon Kinesis stream, an Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.
    You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors. For more information, see Understanding Application Output (Destination) .
    Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the DescribeApplication operation to find the current application version.
    For the limits on the number of application inputs and outputs you can configure, see Limits .
    This operation requires permissions to perform the kinesisanalytics:AddApplicationOutput action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_application_output(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        Output={
            'Name': 'string',
            'KinesisStreamsOutput': {
                'ResourceARN': 'string',
                'RoleARN': 'string'
            },
            'KinesisFirehoseOutput': {
                'ResourceARN': 'string',
                'RoleARN': 'string'
            },
            'LambdaOutput': {
                'ResourceARN': 'string',
                'RoleARN': 'string'
            },
            'DestinationSchema': {
                'RecordFormatType': 'JSON'|'CSV'
            }
        }
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nName of the application to which you want to add the output configuration.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nVersion of the application to which you want to add the output configuration. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.\n

    :type Output: dict
    :param Output: [REQUIRED]\nAn array of objects, each describing one output configuration. In the output configuration, you specify the name of an in-application stream, a destination (that is, an Amazon Kinesis stream, an Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), and record the formation to use when writing to the destination.\n\nName (string) -- [REQUIRED]Name of the in-application stream.\n\nKinesisStreamsOutput (dict) --Identifies an Amazon Kinesis stream as the destination.\n\nResourceARN (string) -- [REQUIRED]ARN of the destination Amazon Kinesis stream to write to.\n\nRoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.\n\n\n\nKinesisFirehoseOutput (dict) --Identifies an Amazon Kinesis Firehose delivery stream as the destination.\n\nResourceARN (string) -- [REQUIRED]ARN of the destination Amazon Kinesis Firehose delivery stream to write to.\n\nRoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.\n\n\n\nLambdaOutput (dict) --Identifies an AWS Lambda function as the destination.\n\nResourceARN (string) -- [REQUIRED]Amazon Resource Name (ARN) of the destination Lambda function to write to.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\nRoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination function on your behalf. You need to grant the necessary permissions to this role.\n\n\n\nDestinationSchema (dict) -- [REQUIRED]Describes the data format when records are written to the destination. For more information, see Configuring Application Output .\n\nRecordFormatType (string) -- [REQUIRED]Specifies the format of the records on the output stream.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.ConcurrentModificationException
KinesisAnalytics.Client.exceptions.UnsupportedOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def add_application_reference_data_source(ApplicationName=None, CurrentApplicationVersionId=None, ReferenceDataSource=None):
    """
    Adds a reference data source to an existing application.
    Amazon Kinesis Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in Amazon S3 object maps to columns in the resulting in-application table.
    For conceptual information, see Configuring Application Input . For the limits on data sources you can add to your application, see Limits .
    This operation requires permissions to perform the kinesisanalytics:AddApplicationOutput action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_application_reference_data_source(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        ReferenceDataSource={
            'TableName': 'string',
            'S3ReferenceDataSource': {
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
        }
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nName of an existing application.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nVersion of the application for which you are adding the reference data source. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.\n

    :type ReferenceDataSource: dict
    :param ReferenceDataSource: [REQUIRED]\nThe reference data source can be an object in your Amazon S3 bucket. Amazon Kinesis Analytics reads the object and copies the data into the in-application table that is created. You provide an S3 bucket, object key name, and the resulting in-application table that is created. You must also provide an IAM role with the necessary permissions that Amazon Kinesis Analytics can assume to read the object from your S3 bucket on your behalf.\n\nTableName (string) -- [REQUIRED]Name of the in-application table to create.\n\nS3ReferenceDataSource (dict) --Identifies the S3 bucket and object that contains the reference data. Also identifies the IAM role Amazon Kinesis Analytics can assume to read this object on your behalf. An Amazon Kinesis Analytics application loads reference data only once. If the data changes, you call the UpdateApplication operation to trigger reloading of data into your application.\n\nBucketARN (string) -- [REQUIRED]Amazon Resource Name (ARN) of the S3 bucket.\n\nFileKey (string) -- [REQUIRED]Object key name containing reference data.\n\nReferenceRoleARN (string) -- [REQUIRED]ARN of the IAM role that the service can assume to read data on your behalf. This role must have permission for the s3:GetObject action on the object and trust policy that allows Amazon Kinesis Analytics service principal to assume this role.\n\n\n\nReferenceSchema (dict) -- [REQUIRED]Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.\n\nRecordFormat (dict) -- [REQUIRED]Specifies the format of the records on the streaming source.\n\nRecordFormatType (string) -- [REQUIRED]The type of record format.\n\nMappingParameters (dict) --When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.\n\nJSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.\n\nRecordRowPath (string) -- [REQUIRED]Path to the top-level parent that contains the records.\n\n\n\nCSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).\n\nRecordRowDelimiter (string) -- [REQUIRED]Row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.\n\nRecordColumnDelimiter (string) -- [REQUIRED]Column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.\n\n\n\n\n\n\n\nRecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.\n\nRecordColumns (list) -- [REQUIRED]A list of RecordColumn objects.\n\n(dict) --Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.\nAlso used to describe the format of the reference data source.\n\nName (string) -- [REQUIRED]Name of the column created in the in-application input stream or reference table.\n\nMapping (string) --Reference to the data element in the streaming input or the reference data source. This element is required if the RecordFormatType is JSON .\n\nSqlType (string) -- [REQUIRED]Type of column created in the in-application input stream or reference table.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.ConcurrentModificationException
KinesisAnalytics.Client.exceptions.UnsupportedOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_application(ApplicationName=None, ApplicationDescription=None, Inputs=None, Outputs=None, CloudWatchLoggingOptions=None, ApplicationCode=None, Tags=None):
    """
    Creates an Amazon Kinesis Analytics application. You can configure each application with one streaming source as input, application code to process the input, and up to three destinations where you want Amazon Kinesis Analytics to write the output data from your application. For an overview, see How it Works .
    In the input configuration, you map the streaming source to an in-application stream, which you can think of as a constantly updating table. In the mapping, you must provide a schema for the in-application stream and map each data column in the in-application stream to a data element in the streaming source.
    Your application code is one or more SQL statements that read input data, transform it, and generate output. Your application code can create one or more SQL artifacts like SQL streams or pumps.
    In the output configuration, you can configure the application to write data from in-application streams created in your applications to up to three destinations.
    To read data from your source stream or write data to destination streams, Amazon Kinesis Analytics needs your permissions. You grant these permissions by creating IAM roles. This operation requires permissions to perform the kinesisanalytics:CreateApplication action.
    For introductory exercises to create an Amazon Kinesis Analytics application, see Getting Started .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_application(
        ApplicationName='string',
        ApplicationDescription='string',
        Inputs=[
            {
                'NamePrefix': 'string',
                'InputProcessingConfiguration': {
                    'InputLambdaProcessor': {
                        'ResourceARN': 'string',
                        'RoleARN': 'string'
                    }
                },
                'KinesisStreamsInput': {
                    'ResourceARN': 'string',
                    'RoleARN': 'string'
                },
                'KinesisFirehoseInput': {
                    'ResourceARN': 'string',
                    'RoleARN': 'string'
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
        Outputs=[
            {
                'Name': 'string',
                'KinesisStreamsOutput': {
                    'ResourceARN': 'string',
                    'RoleARN': 'string'
                },
                'KinesisFirehoseOutput': {
                    'ResourceARN': 'string',
                    'RoleARN': 'string'
                },
                'LambdaOutput': {
                    'ResourceARN': 'string',
                    'RoleARN': 'string'
                },
                'DestinationSchema': {
                    'RecordFormatType': 'JSON'|'CSV'
                }
            },
        ],
        CloudWatchLoggingOptions=[
            {
                'LogStreamARN': 'string',
                'RoleARN': 'string'
            },
        ],
        ApplicationCode='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nName of your Amazon Kinesis Analytics application (for example, sample-app ).\n

    :type ApplicationDescription: string
    :param ApplicationDescription: Summary description of the application.

    :type Inputs: list
    :param Inputs: Use this parameter to configure the application input.\nYou can configure your application to receive input from a single streaming source. In this configuration, you map this streaming source to an in-application stream that is created. Your application code can then query the in-application stream like a table (you can think of it as a constantly updating table).\nFor the streaming source, you provide its Amazon Resource Name (ARN) and format of data on the stream (for example, JSON, CSV, etc.). You also must provide an IAM role that Amazon Kinesis Analytics can assume to read this stream on your behalf.\nTo create the in-application stream, you need to specify a schema to transform your data into a schematized version used in SQL. In the schema, you provide the necessary mapping of the data elements in the streaming source to record columns in the in-app stream.\n\n(dict) --When you configure the application input, you specify the streaming source, the in-application stream name that is created, and the mapping between the two. For more information, see Configuring Application Input .\n\nNamePrefix (string) -- [REQUIRED]Name prefix to use when creating an in-application stream. Suppose that you specify a prefix 'MyInApplicationStream.' Amazon Kinesis Analytics then creates one or more (as per the InputParallelism count you specified) in-application streams with names 'MyInApplicationStream_001,' 'MyInApplicationStream_002,' and so on.\n\nInputProcessingConfiguration (dict) --The InputProcessingConfiguration for the input. An input processor transforms records as they are received from the stream, before the application\'s SQL code executes. Currently, the only input processing configuration available is InputLambdaProcessor .\n\nInputLambdaProcessor (dict) -- [REQUIRED]The InputLambdaProcessor that is used to preprocess the records in the stream before being processed by your application code.\n\nResourceARN (string) -- [REQUIRED]The ARN of the AWS Lambda function that operates on records in the stream.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\nRoleARN (string) -- [REQUIRED]The ARN of the IAM role that is used to access the AWS Lambda function.\n\n\n\n\n\nKinesisStreamsInput (dict) --If the streaming source is an Amazon Kinesis stream, identifies the stream\'s Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.\nNote: Either KinesisStreamsInput or KinesisFirehoseInput is required.\n\nResourceARN (string) -- [REQUIRED]ARN of the input Amazon Kinesis stream to read.\n\nRoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.\n\n\n\nKinesisFirehoseInput (dict) --If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the delivery stream\'s ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.\nNote: Either KinesisStreamsInput or KinesisFirehoseInput is required.\n\nResourceARN (string) -- [REQUIRED]ARN of the input delivery stream.\n\nRoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to make sure that the role has the necessary permissions to access the stream.\n\n\n\nInputParallelism (dict) --Describes the number of in-application streams to create.\nData from your source is routed to these in-application input streams.\n(see Configuring Application Input .\n\nCount (integer) --Number of in-application streams to create. For more information, see Limits .\n\n\n\nInputSchema (dict) -- [REQUIRED]Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.\nAlso used to describe the format of the reference data source.\n\nRecordFormat (dict) -- [REQUIRED]Specifies the format of the records on the streaming source.\n\nRecordFormatType (string) -- [REQUIRED]The type of record format.\n\nMappingParameters (dict) --When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.\n\nJSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.\n\nRecordRowPath (string) -- [REQUIRED]Path to the top-level parent that contains the records.\n\n\n\nCSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).\n\nRecordRowDelimiter (string) -- [REQUIRED]Row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.\n\nRecordColumnDelimiter (string) -- [REQUIRED]Column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.\n\n\n\n\n\n\n\nRecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.\n\nRecordColumns (list) -- [REQUIRED]A list of RecordColumn objects.\n\n(dict) --Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.\nAlso used to describe the format of the reference data source.\n\nName (string) -- [REQUIRED]Name of the column created in the in-application input stream or reference table.\n\nMapping (string) --Reference to the data element in the streaming input or the reference data source. This element is required if the RecordFormatType is JSON .\n\nSqlType (string) -- [REQUIRED]Type of column created in the in-application input stream or reference table.\n\n\n\n\n\n\n\n\n\n\n

    :type Outputs: list
    :param Outputs: You can configure application output to write data from any of the in-application streams to up to three destinations.\nThese destinations can be Amazon Kinesis streams, Amazon Kinesis Firehose delivery streams, AWS Lambda destinations, or any combination of the three.\nIn the configuration, you specify the in-application stream name, the destination stream or Lambda function Amazon Resource Name (ARN), and the format to use when writing data. You must also provide an IAM role that Amazon Kinesis Analytics can assume to write to the destination stream or Lambda function on your behalf.\nIn the output configuration, you also provide the output stream or Lambda function ARN. For stream destinations, you provide the format of data in the stream (for example, JSON, CSV). You also must provide an IAM role that Amazon Kinesis Analytics can assume to write to the stream or Lambda function on your behalf.\n\n(dict) --Describes application output configuration in which you identify an in-application stream and a destination where you want the in-application stream data to be written. The destination can be an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream.\nFor limits on how many destinations an application can write and other limitations, see Limits .\n\nName (string) -- [REQUIRED]Name of the in-application stream.\n\nKinesisStreamsOutput (dict) --Identifies an Amazon Kinesis stream as the destination.\n\nResourceARN (string) -- [REQUIRED]ARN of the destination Amazon Kinesis stream to write to.\n\nRoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.\n\n\n\nKinesisFirehoseOutput (dict) --Identifies an Amazon Kinesis Firehose delivery stream as the destination.\n\nResourceARN (string) -- [REQUIRED]ARN of the destination Amazon Kinesis Firehose delivery stream to write to.\n\nRoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.\n\n\n\nLambdaOutput (dict) --Identifies an AWS Lambda function as the destination.\n\nResourceARN (string) -- [REQUIRED]Amazon Resource Name (ARN) of the destination Lambda function to write to.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\nRoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination function on your behalf. You need to grant the necessary permissions to this role.\n\n\n\nDestinationSchema (dict) -- [REQUIRED]Describes the data format when records are written to the destination. For more information, see Configuring Application Output .\n\nRecordFormatType (string) -- [REQUIRED]Specifies the format of the records on the output stream.\n\n\n\n\n\n\n

    :type CloudWatchLoggingOptions: list
    :param CloudWatchLoggingOptions: Use this parameter to configure a CloudWatch log stream to monitor application configuration errors. For more information, see Working with Amazon CloudWatch Logs .\n\n(dict) --Provides a description of CloudWatch logging options, including the log stream Amazon Resource Name (ARN) and the role ARN.\n\nLogStreamARN (string) -- [REQUIRED]ARN of the CloudWatch log to receive application messages.\n\nRoleARN (string) -- [REQUIRED]IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role that is used must have the PutLogEvents policy action enabled.\n\n\n\n\n

    :type ApplicationCode: string
    :param ApplicationCode: One or more SQL statements that read input data, transform it, and generate output. For example, you can write a SQL statement that reads data from one in-application stream, generates a running average of the number of advertisement clicks by vendor, and insert resulting rows in another in-application stream using pumps. For more information about the typical pattern, see Application Code .\nYou can provide such series of SQL statements, where output of one statement can be used as the input for the next statement. You store intermediate results by creating in-application streams and pumps.\nNote that the application code must create the streams with names specified in the Outputs . For example, if your Outputs defines output streams named ExampleOutputStream1 and ExampleOutputStream2 , then your application code must create these streams.\n

    :type Tags: list
    :param Tags: A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see Using Tagging .\n\n(dict) --A key-value pair (the value is optional) that you can define and assign to AWS resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see Using Tagging .\n\nKey (string) -- [REQUIRED]The key of the key-value tag.\n\nValue (string) --The value of the key-value tag. The value is optional.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationSummary': {
        'ApplicationName': 'string',
        'ApplicationARN': 'string',
        'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING'
    }
}


Response Structure

(dict) --
TBD

ApplicationSummary (dict) --
In response to your CreateApplication request, Amazon Kinesis Analytics returns a response with a summary of the application it created, including the application Amazon Resource Name (ARN), name, and status.

ApplicationName (string) --
Name of the application.

ApplicationARN (string) --
ARN of the application.

ApplicationStatus (string) --
Status of the application.









Exceptions

KinesisAnalytics.Client.exceptions.CodeValidationException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.LimitExceededException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.TooManyTagsException
KinesisAnalytics.Client.exceptions.ConcurrentModificationException


    :return: {
        'ApplicationSummary': {
            'ApplicationName': 'string',
            'ApplicationARN': 'string',
            'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING'
        }
    }
    
    
    :returns: 
    KinesisAnalytics.Client.exceptions.CodeValidationException
    KinesisAnalytics.Client.exceptions.ResourceInUseException
    KinesisAnalytics.Client.exceptions.LimitExceededException
    KinesisAnalytics.Client.exceptions.InvalidArgumentException
    KinesisAnalytics.Client.exceptions.TooManyTagsException
    KinesisAnalytics.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def delete_application(ApplicationName=None, CreateTimestamp=None):
    """
    Deletes the specified application. Amazon Kinesis Analytics halts application execution and deletes the application, including any application artifacts (such as in-application streams, reference table, and application code).
    This operation requires permissions to perform the kinesisanalytics:DeleteApplication action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application(
        ApplicationName='string',
        CreateTimestamp=datetime(2015, 1, 1)
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nName of the Amazon Kinesis Analytics application to delete.\n

    :type CreateTimestamp: datetime
    :param CreateTimestamp: [REQUIRED]\nYou can use the DescribeApplication operation to get this value.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalytics.Client.exceptions.ConcurrentModificationException
KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.UnsupportedOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_application_cloud_watch_logging_option(ApplicationName=None, CurrentApplicationVersionId=None, CloudWatchLoggingOptionId=None):
    """
    Deletes a CloudWatch log stream from an application. For more information about using CloudWatch log streams with Amazon Kinesis Analytics applications, see Working with Amazon CloudWatch Logs .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application_cloud_watch_logging_option(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        CloudWatchLoggingOptionId='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe Kinesis Analytics application name.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe version ID of the Kinesis Analytics application.\n

    :type CloudWatchLoggingOptionId: string
    :param CloudWatchLoggingOptionId: [REQUIRED]\nThe CloudWatchLoggingOptionId of the CloudWatch logging option to delete. You can get the CloudWatchLoggingOptionId by using the DescribeApplication operation.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.ConcurrentModificationException
KinesisAnalytics.Client.exceptions.UnsupportedOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_application_input_processing_configuration(ApplicationName=None, CurrentApplicationVersionId=None, InputId=None):
    """
    Deletes an InputProcessingConfiguration from an input.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application_input_processing_configuration(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        InputId='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nThe Kinesis Analytics application name.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe version ID of the Kinesis Analytics application.\n

    :type InputId: string
    :param InputId: [REQUIRED]\nThe ID of the input configuration from which to delete the input processing configuration. You can get a list of the input IDs for an application by using the DescribeApplication operation.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.ConcurrentModificationException
KinesisAnalytics.Client.exceptions.UnsupportedOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_application_output(ApplicationName=None, CurrentApplicationVersionId=None, OutputId=None):
    """
    Deletes output destination configuration from your application configuration. Amazon Kinesis Analytics will no longer write data from the corresponding in-application stream to the external output destination.
    This operation requires permissions to perform the kinesisanalytics:DeleteApplicationOutput action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application_output(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        OutputId='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nAmazon Kinesis Analytics application name.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nAmazon Kinesis Analytics application version. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.\n

    :type OutputId: string
    :param OutputId: [REQUIRED]\nThe ID of the configuration to delete. Each output configuration that is added to the application, either when the application is created or later using the AddApplicationOutput operation, has a unique ID. You need to provide the ID to uniquely identify the output configuration that you want to delete from the application configuration. You can use the DescribeApplication operation to get the specific OutputId .\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.ConcurrentModificationException
KinesisAnalytics.Client.exceptions.UnsupportedOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_application_reference_data_source(ApplicationName=None, CurrentApplicationVersionId=None, ReferenceId=None):
    """
    Deletes a reference data source configuration from the specified application configuration.
    If the application is running, Amazon Kinesis Analytics immediately removes the in-application table that you created using the AddApplicationReferenceDataSource operation.
    This operation requires permissions to perform the kinesisanalytics.DeleteApplicationReferenceDataSource action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application_reference_data_source(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        ReferenceId='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nName of an existing application.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nVersion of the application. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.\n

    :type ReferenceId: string
    :param ReferenceId: [REQUIRED]\nID of the reference data source. When you add a reference data source to your application using the AddApplicationReferenceDataSource , Amazon Kinesis Analytics assigns an ID. You can use the DescribeApplication operation to get the reference ID.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.ConcurrentModificationException
KinesisAnalytics.Client.exceptions.UnsupportedOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_application(ApplicationName=None):
    """
    Returns information about a specific Amazon Kinesis Analytics application.
    If you want to retrieve a list of all applications in your account, use the ListApplications operation.
    This operation requires permissions to perform the kinesisanalytics:DescribeApplication action. You can use DescribeApplication to get the current application versionId, which you need to call other operations such as Update .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_application(
        ApplicationName='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nName of the application.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ApplicationDetail': {
        'ApplicationName': 'string',
        'ApplicationDescription': 'string',
        'ApplicationARN': 'string',
        'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
        'CreateTimestamp': datetime(2015, 1, 1),
        'LastUpdateTimestamp': datetime(2015, 1, 1),
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
        ],
        'CloudWatchLoggingOptionDescriptions': [
            {
                'CloudWatchLoggingOptionId': 'string',
                'LogStreamARN': 'string',
                'RoleARN': 'string'
            },
        ],
        'ApplicationCode': 'string',
        'ApplicationVersionId': 123
    }
}


Response Structure

(dict) --
ApplicationDetail (dict) --Provides a description of the application, such as the application Amazon Resource Name (ARN), status, latest version, and input and output configuration details.

ApplicationName (string) --Name of the application.

ApplicationDescription (string) --Description of the application.

ApplicationARN (string) --ARN of the application.

ApplicationStatus (string) --Status of the application.

CreateTimestamp (datetime) --Time stamp when the application version was created.

LastUpdateTimestamp (datetime) --Time stamp when the application was last updated.

InputDescriptions (list) --Describes the application input configuration. For more information, see Configuring Application Input .

(dict) --Describes the application input configuration. For more information, see Configuring Application Input .

InputId (string) --Input ID associated with the application input. This is the ID that Amazon Kinesis Analytics assigns to each input configuration you add to your application.

NamePrefix (string) --In-application name prefix.

InAppStreamNames (list) --Returns the in-application stream names that are mapped to the stream source.

(string) --


InputProcessingConfigurationDescription (dict) --The description of the preprocessor that executes on records in this input before the application\'s code is run.

InputLambdaProcessorDescription (dict) --Provides configuration information about the associated InputLambdaProcessorDescription .

ResourceARN (string) --The ARN of the AWS Lambda function that is used to preprocess the records in the stream.

RoleARN (string) --The ARN of the IAM role that is used to access the AWS Lambda function.





KinesisStreamsInputDescription (dict) --If an Amazon Kinesis stream is configured as streaming source, provides Amazon Kinesis stream\'s Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.

ResourceARN (string) --Amazon Resource Name (ARN) of the Amazon Kinesis stream.

RoleARN (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.



KinesisFirehoseInputDescription (dict) --If an Amazon Kinesis Firehose delivery stream is configured as a streaming source, provides the delivery stream\'s ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.

ResourceARN (string) --Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.

RoleARN (string) --ARN of the IAM role that Amazon Kinesis Analytics assumes to access the stream.



InputSchema (dict) --Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.

RecordFormat (dict) --Specifies the format of the records on the streaming source.

RecordFormatType (string) --The type of record format.

MappingParameters (dict) --When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath (string) --Path to the top-level parent that contains the records.



CSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter (string) --Row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.

RecordColumnDelimiter (string) --Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.







RecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns (list) --A list of RecordColumn objects.

(dict) --Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
Also used to describe the format of the reference data source.

Name (string) --Name of the column created in the in-application input stream or reference table.

Mapping (string) --Reference to the data element in the streaming input or the reference data source. This element is required if the RecordFormatType is JSON .

SqlType (string) --Type of column created in the in-application input stream or reference table.







InputParallelism (dict) --Describes the configured parallelism (number of in-application streams mapped to the streaming source).

Count (integer) --Number of in-application streams to create. For more information, see Limits .



InputStartingPositionConfiguration (dict) --Point at which the application is configured to read from the input stream.

InputStartingPosition (string) --The starting position on the stream.

NOW - Start reading just after the most recent record in the stream, start at the request time stamp that the customer issued.
TRIM_HORIZON - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Firehose delivery stream.
LAST_STOPPED_POINT - Resume reading from where the application last stopped reading.








OutputDescriptions (list) --Describes the application output configuration. For more information, see Configuring Application Output .

(dict) --Describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream.

OutputId (string) --A unique identifier for the output configuration.

Name (string) --Name of the in-application stream configured as output.

KinesisStreamsOutputDescription (dict) --Describes Amazon Kinesis stream configured as the destination where output is written.

ResourceARN (string) --Amazon Resource Name (ARN) of the Amazon Kinesis stream.

RoleARN (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.



KinesisFirehoseOutputDescription (dict) --Describes the Amazon Kinesis Firehose delivery stream configured as the destination where output is written.

ResourceARN (string) --Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.

RoleARN (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.



LambdaOutputDescription (dict) --Describes the AWS Lambda function configured as the destination where output is written.

ResourceARN (string) --Amazon Resource Name (ARN) of the destination Lambda function.

RoleARN (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination function.



DestinationSchema (dict) --Data format used for writing data to the destination.

RecordFormatType (string) --Specifies the format of the records on the output stream.







ReferenceDataSourceDescriptions (list) --Describes reference data sources configured for the application. For more information, see Configuring Application Input .

(dict) --Describes the reference data source configured for an application.

ReferenceId (string) --ID of the reference data source. This is the ID that Amazon Kinesis Analytics assigns when you add the reference data source to your application using the AddApplicationReferenceDataSource operation.

TableName (string) --The in-application table name created by the specific reference data source configuration.

S3ReferenceDataSourceDescription (dict) --Provides the S3 bucket name, the object key name that contains the reference data. It also provides the Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object and populate the in-application reference table.

BucketARN (string) --Amazon Resource Name (ARN) of the S3 bucket.

FileKey (string) --Amazon S3 object key name.

ReferenceRoleARN (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table.



ReferenceSchema (dict) --Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

RecordFormat (dict) --Specifies the format of the records on the streaming source.

RecordFormatType (string) --The type of record format.

MappingParameters (dict) --When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath (string) --Path to the top-level parent that contains the records.



CSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter (string) --Row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.

RecordColumnDelimiter (string) --Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.







RecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns (list) --A list of RecordColumn objects.

(dict) --Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
Also used to describe the format of the reference data source.

Name (string) --Name of the column created in the in-application input stream or reference table.

Mapping (string) --Reference to the data element in the streaming input or the reference data source. This element is required if the RecordFormatType is JSON .

SqlType (string) --Type of column created in the in-application input stream or reference table.











CloudWatchLoggingOptionDescriptions (list) --Describes the CloudWatch log streams that are configured to receive application messages. For more information about using CloudWatch log streams with Amazon Kinesis Analytics applications, see Working with Amazon CloudWatch Logs .

(dict) --Description of the CloudWatch logging option.

CloudWatchLoggingOptionId (string) --ID of the CloudWatch logging option description.

LogStreamARN (string) --ARN of the CloudWatch log to receive application messages.

RoleARN (string) --IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role used must have the PutLogEvents policy action enabled.





ApplicationCode (string) --Returns the application code that you provided to perform data analysis on any of the in-application streams in your application.

ApplicationVersionId (integer) --Provides the current application version.








Exceptions

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.UnsupportedOperationException


    :return: {
        'ApplicationDetail': {
            'ApplicationName': 'string',
            'ApplicationDescription': 'string',
            'ApplicationARN': 'string',
            'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING',
            'CreateTimestamp': datetime(2015, 1, 1),
            'LastUpdateTimestamp': datetime(2015, 1, 1),
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
            ],
            'CloudWatchLoggingOptionDescriptions': [
                {
                    'CloudWatchLoggingOptionId': 'string',
                    'LogStreamARN': 'string',
                    'RoleARN': 'string'
                },
            ],
            'ApplicationCode': 'string',
            'ApplicationVersionId': 123
        }
    }
    
    
    :returns: 
    NOW - Start reading just after the most recent record in the stream, start at the request time stamp that the customer issued.
    TRIM_HORIZON - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Firehose delivery stream.
    LAST_STOPPED_POINT - Resume reading from where the application last stopped reading.
    
    """
    pass

def discover_input_schema(ResourceARN=None, RoleARN=None, InputStartingPositionConfiguration=None, S3Configuration=None, InputProcessingConfiguration=None):
    """
    Infers a schema by evaluating sample records on the specified streaming source (Amazon Kinesis stream or Amazon Kinesis Firehose delivery stream) or S3 object. In the response, the operation returns the inferred schema and also the sample records that the operation used to infer the schema.
    You can use the inferred schema when configuring a streaming source for your application. For conceptual information, see Configuring Application Input . Note that when you create an application using the Amazon Kinesis Analytics console, the console uses this operation to infer a schema and show it in the console user interface.
    This operation requires permissions to perform the kinesisanalytics:DiscoverInputSchema action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.discover_input_schema(
        ResourceARN='string',
        RoleARN='string',
        InputStartingPositionConfiguration={
            'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
        },
        S3Configuration={
            'RoleARN': 'string',
            'BucketARN': 'string',
            'FileKey': 'string'
        },
        InputProcessingConfiguration={
            'InputLambdaProcessor': {
                'ResourceARN': 'string',
                'RoleARN': 'string'
            }
        }
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: Amazon Resource Name (ARN) of the streaming source.

    :type RoleARN: string
    :param RoleARN: ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf.

    :type InputStartingPositionConfiguration: dict
    :param InputStartingPositionConfiguration: Point at which you want Amazon Kinesis Analytics to start reading records from the specified streaming source discovery purposes.\n\nInputStartingPosition (string) --The starting position on the stream.\n\nNOW - Start reading just after the most recent record in the stream, start at the request time stamp that the customer issued.\nTRIM_HORIZON - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Firehose delivery stream.\nLAST_STOPPED_POINT - Resume reading from where the application last stopped reading.\n\n\n\n

    :type S3Configuration: dict
    :param S3Configuration: Specify this parameter to discover a schema from data in an Amazon S3 object.\n\nRoleARN (string) -- [REQUIRED]IAM ARN of the role used to access the data.\n\nBucketARN (string) -- [REQUIRED]ARN of the S3 bucket that contains the data.\n\nFileKey (string) -- [REQUIRED]The name of the object that contains the data.\n\n\n

    :type InputProcessingConfiguration: dict
    :param InputProcessingConfiguration: The InputProcessingConfiguration to use to preprocess the records before discovering the schema of the records.\n\nInputLambdaProcessor (dict) -- [REQUIRED]The InputLambdaProcessor that is used to preprocess the records in the stream before being processed by your application code.\n\nResourceARN (string) -- [REQUIRED]The ARN of the AWS Lambda function that operates on records in the stream.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\nRoleARN (string) -- [REQUIRED]The ARN of the IAM role that is used to access the AWS Lambda function.\n\n\n\n\n

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
Schema inferred from the streaming source. It identifies the format of the data in the streaming source and how each data element maps to corresponding columns in the in-application stream that you can create.

RecordFormat (dict) --
Specifies the format of the records on the streaming source.

RecordFormatType (string) --
The type of record format.

MappingParameters (dict) --
When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters (dict) --
Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath (string) --
Path to the top-level parent that contains the records.



CSVMappingParameters (dict) --
Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter (string) --
Row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.

RecordColumnDelimiter (string) --
Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.







RecordEncoding (string) --
Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns (list) --
A list of RecordColumn objects.

(dict) --
Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
Also used to describe the format of the reference data source.

Name (string) --
Name of the column created in the in-application input stream or reference table.

Mapping (string) --
Reference to the data element in the streaming input or the reference data source. This element is required if the RecordFormatType is JSON .

SqlType (string) --
Type of column created in the in-application input stream or reference table.







ParsedInputRecords (list) --
An array of elements, where each element corresponds to a row in a stream record (a stream record can have more than one row).

(list) --
(string) --




ProcessedInputRecords (list) --
Stream data that was modified by the processor specified in the InputProcessingConfiguration parameter.

(string) --


RawInputRecords (list) --
Raw stream data that was sampled to infer the schema.

(string) --








Exceptions

KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.UnableToDetectSchemaException
KinesisAnalytics.Client.exceptions.ResourceProvisionedThroughputExceededException
KinesisAnalytics.Client.exceptions.ServiceUnavailableException


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

def list_applications(Limit=None, ExclusiveStartApplicationName=None):
    """
    Returns a list of Amazon Kinesis Analytics applications in your account. For each application, the response includes the application name, Amazon Resource Name (ARN), and status. If the response returns the HasMoreApplications value as true, you can send another request by adding the ExclusiveStartApplicationName in the request body, and set the value of this to the last application name from the previous response.
    If you want detailed information about a specific application, use DescribeApplication .
    This operation requires permissions to perform the kinesisanalytics:ListApplications action.
    See also: AWS API Documentation
    
    
    :example: response = client.list_applications(
        Limit=123,
        ExclusiveStartApplicationName='string'
    )
    
    
    :type Limit: integer
    :param Limit: Maximum number of applications to list.

    :type ExclusiveStartApplicationName: string
    :param ExclusiveStartApplicationName: Name of the application to start the list with. When using pagination to retrieve the list, you don\'t need to specify this parameter in the first request. However, in subsequent requests, you add the last application name from the previous response to get the next page of applications.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationSummaries': [
        {
            'ApplicationName': 'string',
            'ApplicationARN': 'string',
            'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING'
        },
    ],
    'HasMoreApplications': True|False
}


Response Structure

(dict) --

ApplicationSummaries (list) --
List of ApplicationSummary objects.

(dict) --

Note
This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see Amazon Kinesis Data Analytics API V2 Documentation .

Provides application summary information, including the application Amazon Resource Name (ARN), name, and status.

ApplicationName (string) --
Name of the application.

ApplicationARN (string) --
ARN of the application.

ApplicationStatus (string) --
Status of the application.





HasMoreApplications (boolean) --
Returns true if there are more applications to retrieve.








    :return: {
        'ApplicationSummaries': [
            {
                'ApplicationName': 'string',
                'ApplicationARN': 'string',
                'ApplicationStatus': 'DELETING'|'STARTING'|'STOPPING'|'READY'|'RUNNING'|'UPDATING'
            },
        ],
        'HasMoreApplications': True|False
    }
    
    
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

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.ConcurrentModificationException


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

def start_application(ApplicationName=None, InputConfigurations=None):
    """
    Starts the specified Amazon Kinesis Analytics application. After creating an application, you must exclusively call this operation to start your application.
    After the application starts, it begins consuming the input data, processes it, and writes the output to the configured destination.
    The application status must be READY for you to start an application. You can get the application status in the console or using the DescribeApplication operation.
    After you start the application, you can stop the application from processing the input by calling the StopApplication operation.
    This operation requires permissions to perform the kinesisanalytics:StartApplication action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_application(
        ApplicationName='string',
        InputConfigurations=[
            {
                'Id': 'string',
                'InputStartingPositionConfiguration': {
                    'InputStartingPosition': 'NOW'|'TRIM_HORIZON'|'LAST_STOPPED_POINT'
                }
            },
        ]
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nName of the application.\n

    :type InputConfigurations: list
    :param InputConfigurations: [REQUIRED]\nIdentifies the specific input, by ID, that the application starts consuming. Amazon Kinesis Analytics starts reading the streaming source associated with the input. You can also specify where in the streaming source you want Amazon Kinesis Analytics to start reading.\n\n(dict) --When you start your application, you provide this configuration, which identifies the input source and the point in the input source at which you want the application to start processing records.\n\nId (string) -- [REQUIRED]Input source ID. You can get this ID by calling the DescribeApplication operation.\n\nInputStartingPositionConfiguration (dict) -- [REQUIRED]Point at which you want the application to start processing records from the streaming source.\n\nInputStartingPosition (string) --The starting position on the stream.\n\nNOW - Start reading just after the most recent record in the stream, start at the request time stamp that the customer issued.\nTRIM_HORIZON - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Firehose delivery stream.\nLAST_STOPPED_POINT - Resume reading from where the application last stopped reading.\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.InvalidApplicationConfigurationException
KinesisAnalytics.Client.exceptions.UnsupportedOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def stop_application(ApplicationName=None):
    """
    Stops the application from processing input data. You can stop an application only if it is in the running state. You can use the DescribeApplication operation to find the application state. After the application is stopped, Amazon Kinesis Analytics stops reading data from the input, the application stops processing data, and there is no output written to the destination.
    This operation requires permissions to perform the kinesisanalytics:StopApplication action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_application(
        ApplicationName='string'
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nName of the running application to stop.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.UnsupportedOperationException


    :return: {}
    
    
    :returns: 
    KinesisAnalytics.Client.exceptions.ResourceNotFoundException
    KinesisAnalytics.Client.exceptions.ResourceInUseException
    KinesisAnalytics.Client.exceptions.UnsupportedOperationException
    
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

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.TooManyTagsException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.ConcurrentModificationException


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

KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.TooManyTagsException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_application(ApplicationName=None, CurrentApplicationVersionId=None, ApplicationUpdate=None):
    """
    Updates an existing Amazon Kinesis Analytics application. Using this API, you can update application code, input configuration, and output configuration.
    Note that Amazon Kinesis Analytics updates the CurrentApplicationVersionId each time you update your application.
    This operation requires permission for the kinesisanalytics:UpdateApplication action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_application(
        ApplicationName='string',
        CurrentApplicationVersionId=123,
        ApplicationUpdate={
            'InputUpdates': [
                {
                    'InputId': 'string',
                    'NamePrefixUpdate': 'string',
                    'InputProcessingConfigurationUpdate': {
                        'InputLambdaProcessorUpdate': {
                            'ResourceARNUpdate': 'string',
                            'RoleARNUpdate': 'string'
                        }
                    },
                    'KinesisStreamsInputUpdate': {
                        'ResourceARNUpdate': 'string',
                        'RoleARNUpdate': 'string'
                    },
                    'KinesisFirehoseInputUpdate': {
                        'ResourceARNUpdate': 'string',
                        'RoleARNUpdate': 'string'
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
            'ApplicationCodeUpdate': 'string',
            'OutputUpdates': [
                {
                    'OutputId': 'string',
                    'NameUpdate': 'string',
                    'KinesisStreamsOutputUpdate': {
                        'ResourceARNUpdate': 'string',
                        'RoleARNUpdate': 'string'
                    },
                    'KinesisFirehoseOutputUpdate': {
                        'ResourceARNUpdate': 'string',
                        'RoleARNUpdate': 'string'
                    },
                    'LambdaOutputUpdate': {
                        'ResourceARNUpdate': 'string',
                        'RoleARNUpdate': 'string'
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
                        'FileKeyUpdate': 'string',
                        'ReferenceRoleARNUpdate': 'string'
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
            ],
            'CloudWatchLoggingOptionUpdates': [
                {
                    'CloudWatchLoggingOptionId': 'string',
                    'LogStreamARNUpdate': 'string',
                    'RoleARNUpdate': 'string'
                },
            ]
        }
    )
    
    
    :type ApplicationName: string
    :param ApplicationName: [REQUIRED]\nName of the Amazon Kinesis Analytics application to update.\n

    :type CurrentApplicationVersionId: integer
    :param CurrentApplicationVersionId: [REQUIRED]\nThe current application version ID. You can use the DescribeApplication operation to get this value.\n

    :type ApplicationUpdate: dict
    :param ApplicationUpdate: [REQUIRED]\nDescribes application updates.\n\nInputUpdates (list) --Describes application input configuration updates.\n\n(dict) --Describes updates to a specific input configuration (identified by the InputId of an application).\n\nInputId (string) -- [REQUIRED]Input ID of the application input to be updated.\n\nNamePrefixUpdate (string) --Name prefix for in-application streams that Amazon Kinesis Analytics creates for the specific streaming source.\n\nInputProcessingConfigurationUpdate (dict) --Describes updates for an input processing configuration.\n\nInputLambdaProcessorUpdate (dict) -- [REQUIRED]Provides update information for an InputLambdaProcessor .\n\nResourceARNUpdate (string) --The Amazon Resource Name (ARN) of the new AWS Lambda function that is used to preprocess the records in the stream.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\nRoleARNUpdate (string) --The ARN of the new IAM role that is used to access the AWS Lambda function.\n\n\n\n\n\nKinesisStreamsInputUpdate (dict) --If an Amazon Kinesis stream is the streaming source to be updated, provides an updated stream Amazon Resource Name (ARN) and IAM role ARN.\n\nResourceARNUpdate (string) --Amazon Resource Name (ARN) of the input Amazon Kinesis stream to read.\n\nRoleARNUpdate (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.\n\n\n\nKinesisFirehoseInputUpdate (dict) --If an Amazon Kinesis Firehose delivery stream is the streaming source to be updated, provides an updated stream ARN and IAM role ARN.\n\nResourceARNUpdate (string) --Amazon Resource Name (ARN) of the input Amazon Kinesis Firehose delivery stream to read.\n\nRoleARNUpdate (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.\n\n\n\nInputSchemaUpdate (dict) --Describes the data format on the streaming source, and how record elements on the streaming source map to columns of the in-application stream that is created.\n\nRecordFormatUpdate (dict) --Specifies the format of the records on the streaming source.\n\nRecordFormatType (string) -- [REQUIRED]The type of record format.\n\nMappingParameters (dict) --When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.\n\nJSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.\n\nRecordRowPath (string) -- [REQUIRED]Path to the top-level parent that contains the records.\n\n\n\nCSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).\n\nRecordRowDelimiter (string) -- [REQUIRED]Row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.\n\nRecordColumnDelimiter (string) -- [REQUIRED]Column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.\n\n\n\n\n\n\n\nRecordEncodingUpdate (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.\n\nRecordColumnUpdates (list) --A list of RecordColumn objects. Each object describes the mapping of the streaming source element to the corresponding column in the in-application stream.\n\n(dict) --Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.\nAlso used to describe the format of the reference data source.\n\nName (string) -- [REQUIRED]Name of the column created in the in-application input stream or reference table.\n\nMapping (string) --Reference to the data element in the streaming input or the reference data source. This element is required if the RecordFormatType is JSON .\n\nSqlType (string) -- [REQUIRED]Type of column created in the in-application input stream or reference table.\n\n\n\n\n\n\n\nInputParallelismUpdate (dict) --Describes the parallelism updates (the number in-application streams Amazon Kinesis Analytics creates for the specific streaming source).\n\nCountUpdate (integer) --Number of in-application streams to create for the specified streaming source.\n\n\n\n\n\n\n\nApplicationCodeUpdate (string) --Describes application code updates.\n\nOutputUpdates (list) --Describes application output configuration updates.\n\n(dict) --Describes updates to the output configuration identified by the OutputId .\n\nOutputId (string) -- [REQUIRED]Identifies the specific output configuration that you want to update.\n\nNameUpdate (string) --If you want to specify a different in-application stream for this output configuration, use this field to specify the new in-application stream name.\n\nKinesisStreamsOutputUpdate (dict) --Describes an Amazon Kinesis stream as the destination for the output.\n\nResourceARNUpdate (string) --Amazon Resource Name (ARN) of the Amazon Kinesis stream where you want to write the output.\n\nRoleARNUpdate (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.\n\n\n\nKinesisFirehoseOutputUpdate (dict) --Describes an Amazon Kinesis Firehose delivery stream as the destination for the output.\n\nResourceARNUpdate (string) --Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream to write to.\n\nRoleARNUpdate (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.\n\n\n\nLambdaOutputUpdate (dict) --Describes an AWS Lambda function as the destination for the output.\n\nResourceARNUpdate (string) --Amazon Resource Name (ARN) of the destination Lambda function.\n\nNote\nTo specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see Example ARNs: AWS Lambda\n\n\nRoleARNUpdate (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination function on your behalf. You need to grant the necessary permissions to this role.\n\n\n\nDestinationSchemaUpdate (dict) --Describes the data format when records are written to the destination. For more information, see Configuring Application Output .\n\nRecordFormatType (string) -- [REQUIRED]Specifies the format of the records on the output stream.\n\n\n\n\n\n\n\nReferenceDataSourceUpdates (list) --Describes application reference data source updates.\n\n(dict) --When you update a reference data source configuration for an application, this object provides all the updated values (such as the source bucket name and object key name), the in-application table name that is created, and updated mapping information that maps the data in the Amazon S3 object to the in-application reference table that is created.\n\nReferenceId (string) -- [REQUIRED]ID of the reference data source being updated. You can use the DescribeApplication operation to get this value.\n\nTableNameUpdate (string) --In-application table name that is created by this update.\n\nS3ReferenceDataSourceUpdate (dict) --Describes the S3 bucket name, object key name, and IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object on your behalf and populate the in-application reference table.\n\nBucketARNUpdate (string) --Amazon Resource Name (ARN) of the S3 bucket.\n\nFileKeyUpdate (string) --Object key name.\n\nReferenceRoleARNUpdate (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object and populate the in-application.\n\n\n\nReferenceSchemaUpdate (dict) --Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.\n\nRecordFormat (dict) -- [REQUIRED]Specifies the format of the records on the streaming source.\n\nRecordFormatType (string) -- [REQUIRED]The type of record format.\n\nMappingParameters (dict) --When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.\n\nJSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.\n\nRecordRowPath (string) -- [REQUIRED]Path to the top-level parent that contains the records.\n\n\n\nCSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).\n\nRecordRowDelimiter (string) -- [REQUIRED]Row delimiter. For example, in a CSV format, \'n\' is the typical row delimiter.\n\nRecordColumnDelimiter (string) -- [REQUIRED]Column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.\n\n\n\n\n\n\n\nRecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.\n\nRecordColumns (list) -- [REQUIRED]A list of RecordColumn objects.\n\n(dict) --Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.\nAlso used to describe the format of the reference data source.\n\nName (string) -- [REQUIRED]Name of the column created in the in-application input stream or reference table.\n\nMapping (string) --Reference to the data element in the streaming input or the reference data source. This element is required if the RecordFormatType is JSON .\n\nSqlType (string) -- [REQUIRED]Type of column created in the in-application input stream or reference table.\n\n\n\n\n\n\n\n\n\n\n\nCloudWatchLoggingOptionUpdates (list) --Describes application CloudWatch logging option updates.\n\n(dict) --Describes CloudWatch logging option updates.\n\nCloudWatchLoggingOptionId (string) -- [REQUIRED]ID of the CloudWatch logging option to update\n\nLogStreamARNUpdate (string) --ARN of the CloudWatch log to receive application messages.\n\nRoleARNUpdate (string) --IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role used must have the PutLogEvents policy action enabled.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisAnalytics.Client.exceptions.CodeValidationException
KinesisAnalytics.Client.exceptions.ResourceNotFoundException
KinesisAnalytics.Client.exceptions.ResourceInUseException
KinesisAnalytics.Client.exceptions.InvalidArgumentException
KinesisAnalytics.Client.exceptions.ConcurrentModificationException
KinesisAnalytics.Client.exceptions.UnsupportedOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

