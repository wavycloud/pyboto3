"""
The MIT License (MIT)

Copyright (c) 2016 Gehad Shaat

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
"""


def add_application_input(ApplicationName=None, CurrentApplicationVersionId=None, Input=None):
    """
    :param ApplicationName: [REQUIRED]
            Name of your existing Amazon Kinesis Analytics application to which you want to add the streaming source.
            
    :type ApplicationName: string
    :param CurrentApplicationVersionId: [REQUIRED]
            Current version of your Amazon Kinesis Analytics application. You can use the DescribeApplication operation to find the current application version.
            
    :type CurrentApplicationVersionId: integer
    :param Input: [REQUIRED]
            When you configure the application input, you specify the streaming source, the in-application stream name that is created, and the mapping between the two. For more information, see Configuring Application Input .
            NamePrefix (string) -- [REQUIRED]Name prefix to use when creating in-application stream. Suppose you specify a prefix 'MyInApplicationStream'. Kinesis Analytics will then create one or more (as per the InputParallelism count you specified) in-application streams with names 'MyInApplicationStream_001', 'MyInApplicationStream_002' and so on.
            KinesisStreamsInput (dict) --If the streaming source is an Amazon Kinesis stream, identifies the stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.
            ResourceARN (string) -- [REQUIRED]ARN of the input Amazon Kinesis stream to read.
            RoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.
            KinesisFirehoseInput (dict) --If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the Firehose delivery stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.
            ResourceARN (string) -- [REQUIRED]ARN of the input Firehose delivery stream.
            RoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to make sure the role has necessary permissions to access the stream.
            InputParallelism (dict) --Describes the number of in-application streams to create.
            Data from your source will be routed to these in-application input streams.
            (see Configuring Application Input .
            Count (integer) --Number of in-application streams to create. For more information, see Limits .
            InputSchema (dict) -- [REQUIRED]Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.
            Also used to describe the format of the reference data source.
            RecordFormat (dict) -- [REQUIRED]Specifies the format of the records on the streaming source.
            RecordFormatType (string) -- [REQUIRED]The type of record format.
            MappingParameters (dict) --When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
            JSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.
            RecordRowPath (string) -- [REQUIRED]Path to the top-level parent that contains the records.
            For example, consider the following JSON record:
            In the RecordRowPath , '$' refers to the root and path '$.vehicle.Model' refers to the specific 'Model' key in the JSON.
            CSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).
            RecordRowDelimiter (string) -- [REQUIRED]Row delimiter. For example, in a CSV format, 'n' is the typical row delimiter.
            RecordColumnDelimiter (string) -- [REQUIRED]Column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.
            
            RecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.
            RecordColumns (list) -- [REQUIRED]A list of RecordColumn objects.
            (dict) --Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
            Also used to describe the format of the reference data source.
            Name (string) -- [REQUIRED]Name of the column created in the in-application input stream or reference table.
            Mapping (string) --Reference to the data element in the streaming input of the reference data source.
            SqlType (string) -- [REQUIRED]Type of column created in the in-application input stream or reference table.
            
            
            
    :type Input: dict
    """
    pass


def add_application_output(ApplicationName=None, CurrentApplicationVersionId=None, Output=None):
    """
    :param ApplicationName: [REQUIRED]
            Name of the application to which you want to add the output configuration.
            
    :type ApplicationName: string
    :param CurrentApplicationVersionId: [REQUIRED]
            Version of the application to which you want add the output configuration. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.
            
    :type CurrentApplicationVersionId: integer
    :param Output: [REQUIRED]
            An array of objects, each describing one output configuration. In the output configuration, you specify the name of an in-application stream, a destination (that is, an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream), and record the formation to use when writing to the destination.
            Name (string) -- [REQUIRED]Name of the in-application stream.
            KinesisStreamsOutput (dict) --Identifies an Amazon Kinesis stream as the destination.
            ResourceARN (string) -- [REQUIRED]ARN of the destination Amazon Kinesis stream to write to.
            RoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.
            KinesisFirehoseOutput (dict) --Identifies an Amazon Kinesis Firehose delivery stream as the destination.
            ResourceARN (string) -- [REQUIRED]ARN of the destination Amazon Kinesis Firehose delivery stream to write to.
            RoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.
            DestinationSchema (dict) -- [REQUIRED]Describes the data format when records are written to the destination. For more information, see Configuring Application Output .
            RecordFormatType (string) --Specifies the format of the records on the output stream.
            
            
    :type Output: dict
    """
    pass


def add_application_reference_data_source(ApplicationName=None, CurrentApplicationVersionId=None,
                                          ReferenceDataSource=None):
    """
    :param ApplicationName: [REQUIRED]
            Name of an existing application.
            
    :type ApplicationName: string
    :param CurrentApplicationVersionId: [REQUIRED]
            Version of the application for which you are adding the reference data source. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.
            
    :type CurrentApplicationVersionId: integer
    :param ReferenceDataSource: [REQUIRED]
            The reference data source can be an object in your Amazon S3 bucket. Amazon Kinesis Analytics reads the object and copies the data into the in-application table that is created. You provide an S3 bucket, object key name, and the resulting in-application table that is created. You must also provide an IAM role with the necessary permissions that Amazon Kinesis Analytics can assume to read the object from your S3 bucket on your behalf.
            TableName (string) -- [REQUIRED]Name of the in-application table to create.
            S3ReferenceDataSource (dict) --Identifies the S3 bucket and object that contains the reference data. Also identifies the IAM role Amazon Kinesis Analytics can assume to read this object on your behalf.
            An Amazon Kinesis Analytics application loads reference data only once. If the data changes, you call the UpdateApplication operation to trigger reloading of data into your application.
            BucketARN (string) -- [REQUIRED]Amazon Resource Name (ARN) of the S3 bucket.
            FileKey (string) -- [REQUIRED]Object key name containing reference data.
            ReferenceRoleARN (string) -- [REQUIRED]ARN of the IAM role that the service can assume to read data on your behalf. This role must have permission for the s3:GetObject action on the object and trust policy that allows Amazon Kinesis Analytics service principal to assume this role.
            ReferenceSchema (dict) -- [REQUIRED]Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
            RecordFormat (dict) -- [REQUIRED]Specifies the format of the records on the streaming source.
            RecordFormatType (string) -- [REQUIRED]The type of record format.
            MappingParameters (dict) --When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
            JSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.
            RecordRowPath (string) -- [REQUIRED]Path to the top-level parent that contains the records.
            For example, consider the following JSON record:
            In the RecordRowPath , '$' refers to the root and path '$.vehicle.Model' refers to the specific 'Model' key in the JSON.
            CSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).
            RecordRowDelimiter (string) -- [REQUIRED]Row delimiter. For example, in a CSV format, 'n' is the typical row delimiter.
            RecordColumnDelimiter (string) -- [REQUIRED]Column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.
            
            RecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.
            RecordColumns (list) -- [REQUIRED]A list of RecordColumn objects.
            (dict) --Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
            Also used to describe the format of the reference data source.
            Name (string) -- [REQUIRED]Name of the column created in the in-application input stream or reference table.
            Mapping (string) --Reference to the data element in the streaming input of the reference data source.
            SqlType (string) -- [REQUIRED]Type of column created in the in-application input stream or reference table.
            
            
            
    :type ReferenceDataSource: dict
    """
    pass


def can_paginate(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            ReturnsTrue if the operation can be paginated,
            False otherwise.
            
    :type operation_name: string
    """
    pass


def create_application(ApplicationName=None, ApplicationDescription=None, Inputs=None, Outputs=None,
                       ApplicationCode=None):
    """
    :param ApplicationName: [REQUIRED]
            Name of your Amazon Kinesis Analytics application (for example, sample-app ).
            
    :type ApplicationName: string
    :param ApplicationDescription: Summary description of the application.
    :type ApplicationDescription: string
    :param Inputs: Use this parameter to configure the application input.
            You can configure your application to receive input from a single streaming source. In this configuration, you map this streaming source to an in-application stream that is created. Your application code can then query the in-application stream like a table (you can think of it as a constantly updating table).
            For the streaming source, you provide its Amazon Resource Name (ARN) and format of data on the stream (for example, JSON, CSV, etc). You also must provide an IAM role that Amazon Kinesis Analytics can assume to read this stream on your behalf.
            To create the in-application stream, you need to specify a schema to transform your data into a schematized version used in SQL. In the schema, you provide the necessary mapping of the data elements in the streaming source to record columns in the in-app stream.
            (dict) --When you configure the application input, you specify the streaming source, the in-application stream name that is created, and the mapping between the two. For more information, see Configuring Application Input .
            NamePrefix (string) -- [REQUIRED]Name prefix to use when creating in-application stream. Suppose you specify a prefix 'MyInApplicationStream'. Kinesis Analytics will then create one or more (as per the InputParallelism count you specified) in-application streams with names 'MyInApplicationStream_001', 'MyInApplicationStream_002' and so on.
            KinesisStreamsInput (dict) --If the streaming source is an Amazon Kinesis stream, identifies the stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.
            ResourceARN (string) -- [REQUIRED]ARN of the input Amazon Kinesis stream to read.
            RoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.
            KinesisFirehoseInput (dict) --If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the Firehose delivery stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.
            ResourceARN (string) -- [REQUIRED]ARN of the input Firehose delivery stream.
            RoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to make sure the role has necessary permissions to access the stream.
            InputParallelism (dict) --Describes the number of in-application streams to create.
            Data from your source will be routed to these in-application input streams.
            (see Configuring Application Input .
            Count (integer) --Number of in-application streams to create. For more information, see Limits .
            InputSchema (dict) -- [REQUIRED]Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.
            Also used to describe the format of the reference data source.
            RecordFormat (dict) -- [REQUIRED]Specifies the format of the records on the streaming source.
            RecordFormatType (string) -- [REQUIRED]The type of record format.
            MappingParameters (dict) --When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
            JSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.
            RecordRowPath (string) -- [REQUIRED]Path to the top-level parent that contains the records.
            For example, consider the following JSON record:
            In the RecordRowPath , '$' refers to the root and path '$.vehicle.Model' refers to the specific 'Model' key in the JSON.
            CSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).
            RecordRowDelimiter (string) -- [REQUIRED]Row delimiter. For example, in a CSV format, 'n' is the typical row delimiter.
            RecordColumnDelimiter (string) -- [REQUIRED]Column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.
            
            RecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.
            RecordColumns (list) -- [REQUIRED]A list of RecordColumn objects.
            (dict) --Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
            Also used to describe the format of the reference data source.
            Name (string) -- [REQUIRED]Name of the column created in the in-application input stream or reference table.
            Mapping (string) --Reference to the data element in the streaming input of the reference data source.
            SqlType (string) -- [REQUIRED]Type of column created in the in-application input stream or reference table.
            
            
            
    :type Inputs: list
    :param Outputs: You can configure application output to write data from any of the in-application streams to up to five destinations.
            These destinations can be Amazon Kinesis streams, Amazon Kinesis Firehose delivery streams, or both.
            In the configuration, you specify the in-application stream name, the destination stream Amazon Resource Name (ARN), and the format to use when writing data. You must also provide an IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf.
            In the output configuration, you also provide the output stream Amazon Resource Name (ARN) and the format of data in the stream (for example, JSON, CSV). You also must provide an IAM role that Amazon Kinesis Analytics can assume to write to this stream on your behalf.
            (dict) --Describes application output configuration in which you identify an in-application stream and a destination where you want the in-application stream data to be written. The destination can be an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream.
            You can configure your application to write output to up to five destinations.
            Name (string) -- [REQUIRED]Name of the in-application stream.
            KinesisStreamsOutput (dict) --Identifies an Amazon Kinesis stream as the destination.
            ResourceARN (string) -- [REQUIRED]ARN of the destination Amazon Kinesis stream to write to.
            RoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.
            KinesisFirehoseOutput (dict) --Identifies an Amazon Kinesis Firehose delivery stream as the destination.
            ResourceARN (string) -- [REQUIRED]ARN of the destination Amazon Kinesis Firehose delivery stream to write to.
            RoleARN (string) -- [REQUIRED]ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.
            DestinationSchema (dict) -- [REQUIRED]Describes the data format when records are written to the destination. For more information, see Configuring Application Output .
            RecordFormatType (string) --Specifies the format of the records on the output stream.
            
            
    :type Outputs: list
    :param ApplicationCode: One or more SQL statements that read input data, transform it, and generate output. For example, you can write a SQL statement that reads input data and generates a running average of the number of advertisement clicks by vendor.
            You can also provide a series of SQL statements, where output of one statement can be used as the input for the next statement.
            Note that the application code must create the streams with names specified in the Outputs . For example, if your Outputs defines output streams named ExampleOutputStream1 and ExampleOutputStream2 , then your application code must create these streams.
            
    :type ApplicationCode: string
    """
    pass


def delete_application(ApplicationName=None, CreateTimestamp=None):
    """
    :param ApplicationName: [REQUIRED]
            Name of the Amazon Kinesis Analytics application to delete.
            
    :type ApplicationName: string
    :param CreateTimestamp: [REQUIRED]
            You can use the DescribeApplication operation to get this value.
            
    :type CreateTimestamp: datetime
    """
    pass


def delete_application_output(ApplicationName=None, CurrentApplicationVersionId=None, OutputId=None):
    """
    :param ApplicationName: [REQUIRED]
            Amazon Kinesis Analytics application name.
            
    :type ApplicationName: string
    :param CurrentApplicationVersionId: [REQUIRED]
            Amazon Kinesis Analytics application version. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.
            
    :type CurrentApplicationVersionId: integer
    :param OutputId: [REQUIRED]
            The ID of the configuration to delete. Each output configuration that is added to the application, either when the application is created or later using the AddApplicationOutput operation, has a unique ID. You need to provide the ID to uniquely identify the output configuration that you want to delete from the application configuration. You can use the DescribeApplication operation to get the specific OutputId .
            
    :type OutputId: string
    """
    pass


def delete_application_reference_data_source(ApplicationName=None, CurrentApplicationVersionId=None, ReferenceId=None):
    """
    :param ApplicationName: [REQUIRED]
            Name of an existing application.
            
    :type ApplicationName: string
    :param CurrentApplicationVersionId: [REQUIRED]
            Version of the application. You can use the DescribeApplication operation to get the current application version. If the version specified is not the current version, the ConcurrentModificationException is returned.
            
    :type CurrentApplicationVersionId: integer
    :param ReferenceId: [REQUIRED]
            ID of the reference data source. When you add a reference data source to your application using the AddApplicationReferenceDataSource , Amazon Kinesis Analytics assigns an ID. You can use the DescribeApplication operation to get the reference ID.
            
    :type ReferenceId: string
    """
    pass


def describe_application(ApplicationName=None):
    """
    :param ApplicationName: [REQUIRED]
            Name of the application.
            Return typedict
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
            CreateTimestamp (datetime) --Timestamp when the application version was created.
            LastUpdateTimestamp (datetime) --Timestamp when the application was last updated.
            InputDescriptions (list) --Describes the application input configuration. For more information, see Configuring Application Input .
            (dict) --Describes the application input configuration. For more information, see Configuring Application Input .
            InputId (string) --Input ID associated with the application input. This is the ID that Amazon Kinesis Analytics assigns to each input configuration you add to your application.
            NamePrefix (string) --In-application name prefix.
            InAppStreamNames (list) --Returns the in-application stream names that are mapped to the stream source.
            (string) --
            KinesisStreamsInputDescription (dict) --If an Amazon Kinesis stream is configured as streaming source, provides Amazon Kinesis stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.
            ResourceARN (string) --Amazon Resource Name (ARN) of the Amazon Kinesis stream.
            RoleARN (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream.
            KinesisFirehoseInputDescription (dict) --If an Amazon Kinesis Firehose delivery stream is configured as a streaming source, provides the Firehose delivery stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.
            ResourceARN (string) --Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream.
            RoleARN (string) --ARN of the IAM role that Amazon Kinesis Analytics assumes to access the stream.
            InputSchema (dict) --Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
            RecordFormat (dict) --Specifies the format of the records on the streaming source.
            RecordFormatType (string) --The type of record format.
            MappingParameters (dict) --When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
            JSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.
            RecordRowPath (string) --Path to the top-level parent that contains the records.
            For example, consider the following JSON record:
            In the RecordRowPath , '$' refers to the root and path '$.vehicle.Model' refers to the specific 'Model' key in the JSON.
            CSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).
            RecordRowDelimiter (string) --Row delimiter. For example, in a CSV format, 'n' is the typical row delimiter.
            RecordColumnDelimiter (string) --Column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.
            
            RecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.
            RecordColumns (list) --A list of RecordColumn objects.
            (dict) --Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
            Also used to describe the format of the reference data source.
            Name (string) --Name of the column created in the in-application input stream or reference table.
            Mapping (string) --Reference to the data element in the streaming input of the reference data source.
            SqlType (string) --Type of column created in the in-application input stream or reference table.
            
            InputParallelism (dict) --Describes the configured parallelism (number of in-application streams mapped to the streaming source).
            Count (integer) --Number of in-application streams to create. For more information, see Limits .
            InputStartingPositionConfiguration (dict) --Point at which the application is configured to read from the input stream.
            InputStartingPosition (string) --The starting position on the stream.
            LATEST - Start reading just after the most recent record in the stream.
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
            For example, consider the following JSON record:
            In the RecordRowPath , '$' refers to the root and path '$.vehicle.Model' refers to the specific 'Model' key in the JSON.
            CSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).
            RecordRowDelimiter (string) --Row delimiter. For example, in a CSV format, 'n' is the typical row delimiter.
            RecordColumnDelimiter (string) --Column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.
            
            RecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.
            RecordColumns (list) --A list of RecordColumn objects.
            (dict) --Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
            Also used to describe the format of the reference data source.
            Name (string) --Name of the column created in the in-application input stream or reference table.
            Mapping (string) --Reference to the data element in the streaming input of the reference data source.
            SqlType (string) --Type of column created in the in-application input stream or reference table.
            
            
            ApplicationCode (string) --Returns the application code that you provided to perform data analysis on any of the in-application streams in your application.
            ApplicationVersionId (integer) --Provides the current application version.
            
            
            
    :type ApplicationName: string
    """
    pass


def discover_input_schema(ResourceARN=None, RoleARN=None, InputStartingPositionConfiguration=None):
    """
    :param ResourceARN: [REQUIRED]
            Amazon Resource Name (ARN) of the streaming source.
            
    :type ResourceARN: string
    :param RoleARN: [REQUIRED]
            ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf.
            
    :type RoleARN: string
    :param InputStartingPositionConfiguration: [REQUIRED]
            Point at which you want Amazon Kinesis Analytics to start reading records from the specified streaming source discovery purposes.
            InputStartingPosition (string) --The starting position on the stream.
            LATEST - Start reading just after the most recent record in the stream.
            TRIM_HORIZON - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Firehose delivery stream.
            LAST_STOPPED_POINT - Resume reading from where the application last stopped reading.
            
    :type InputStartingPositionConfiguration: dict
    """
    pass


def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    :param ClientMethod: The client method to presign for
    :type ClientMethod: string
    :param Params: The parameters normally passed to
            ClientMethod.
    :type Params: dict
    :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
    :type ExpiresIn: int
    :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.
    :type HttpMethod: string
    """
    pass


def get_paginator(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            Raises OperationNotPageableErrorRaised if the operation is not
            pageable. You can use the client.can_paginate method to
            check if an operation is pageable.
            Return typeL{botocore.paginate.Paginator}
            ReturnsA paginator object.
            
    :type operation_name: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_applications(Limit=None, ExclusiveStartApplicationName=None):
    """
    :param Limit: Maximum number of applications to list.
    :type Limit: integer
    :param ExclusiveStartApplicationName: Name of the application to start the list with. When using pagination to retrieve the list, you don't need to specify this parameter in the first request. However, in subsequent requests, you add the last application name from the previous response to get the next page of applications.
    :type ExclusiveStartApplicationName: string
    """
    pass


def start_application(ApplicationName=None, InputConfigurations=None):
    """
    :param ApplicationName: [REQUIRED]
            Name of the application.
            
    :type ApplicationName: string
    :param InputConfigurations: [REQUIRED]
            Identifies the specific input, by ID, that the application starts consuming. Amazon Kinesis Analytics starts reading the streaming source associated with the input. You can also specify where in the streaming source you want Amazon Kinesis Analytics to start reading.
            (dict) --When you start your application, you provide this configuration, which identifies the input source and the point in the input source at which you want the application to start processing records.
            Id (string) -- [REQUIRED]Input source ID. You can get this ID by calling the DescribeApplication operation.
            InputStartingPositionConfiguration (dict) -- [REQUIRED]Point at which you want the application to start processing records from the streaming source.
            InputStartingPosition (string) --The starting position on the stream.
            LATEST - Start reading just after the most recent record in the stream.
            TRIM_HORIZON - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Firehose delivery stream.
            LAST_STOPPED_POINT - Resume reading from where the application last stopped reading.
            
            
    :type InputConfigurations: list
    """
    pass


def stop_application(ApplicationName=None):
    """
    :param ApplicationName: [REQUIRED]
            Name of the running application to stop.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --
            
    :type ApplicationName: string
    """
    pass


def update_application(ApplicationName=None, CurrentApplicationVersionId=None, ApplicationUpdate=None):
    """
    :param ApplicationName: [REQUIRED]
            Name of the Kinesis Analytics application to update.
            
    :type ApplicationName: string
    :param CurrentApplicationVersionId: [REQUIRED]
            The current application version ID. You can use the DescribeApplication operation to get this value.
            
    :type CurrentApplicationVersionId: integer
    :param ApplicationUpdate: [REQUIRED]
            Describes application updates.
            InputUpdates (list) --Describes application input configuration updates.
            (dict) --Describes updates to a specific input configuration (identified by the InputId of an application).
            InputId (string) -- [REQUIRED]Input ID of the application input to be updated.
            NamePrefixUpdate (string) --Name prefix for in-application stream(s) that Kinesis Analytics creates for the specific streaming source.
            KinesisStreamsInputUpdate (dict) --If a Amazon Kinesis stream is the streaming source to be updated, provides an updated stream ARN and IAM role ARN.
            ResourceARNUpdate (string) --Amazon Resource Name (ARN) of the input Amazon Kinesis stream to read.
            RoleARNUpdate (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.
            KinesisFirehoseInputUpdate (dict) --If an Amazon Kinesis Firehose delivery stream is the streaming source to be updated, provides an updated stream Amazon Resource Name (ARN) and IAM role ARN.
            ResourceARNUpdate (string) --ARN of the input Amazon Kinesis Firehose delivery stream to read.
            RoleARNUpdate (string) --Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant necessary permissions to this role.
            InputSchemaUpdate (dict) --Describes the data format on the streaming source, and how record elements on the streaming source map to columns of the in-application stream that is created.
            RecordFormatUpdate (dict) --Specifies the format of the records on the streaming source.
            RecordFormatType (string) -- [REQUIRED]The type of record format.
            MappingParameters (dict) --When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
            JSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.
            RecordRowPath (string) -- [REQUIRED]Path to the top-level parent that contains the records.
            For example, consider the following JSON record:
            In the RecordRowPath , '$' refers to the root and path '$.vehicle.Model' refers to the specific 'Model' key in the JSON.
            CSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).
            RecordRowDelimiter (string) -- [REQUIRED]Row delimiter. For example, in a CSV format, 'n' is the typical row delimiter.
            RecordColumnDelimiter (string) -- [REQUIRED]Column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.
            
            RecordEncodingUpdate (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.
            RecordColumnUpdates (list) --A list of RecordColumn objects. Each object describes the mapping of the streaming source element to the corresponding column in the in-application stream.
            (dict) --Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
            Also used to describe the format of the reference data source.
            Name (string) -- [REQUIRED]Name of the column created in the in-application input stream or reference table.
            Mapping (string) --Reference to the data element in the streaming input of the reference data source.
            SqlType (string) -- [REQUIRED]Type of column created in the in-application input stream or reference table.
            
            InputParallelismUpdate (dict) --Describes the parallelism updates (the number in-application streams Kinesis Analytics creates for the specific streaming source).
            CountUpdate (integer) --Number of in-application streams to create for the specified streaming source.
            
            ApplicationCodeUpdate (string) --Describes application code updates.
            OutputUpdates (list) --Describes application output configuration updates.
            (dict) --Describes updates to the output configuration identified by the OutputId .
            OutputId (string) -- [REQUIRED]Identifies the specific output configuration that you want to update.
            NameUpdate (string) --If you want to specify a different in-application stream for this output configuration, use this field to specify the new in-application stream name.
            KinesisStreamsOutputUpdate (dict) --Describes an Amazon Kinesis stream as the destination for the output.
            ResourceARNUpdate (string) --Amazon Resource Name (ARN) of the Amazon Kinesis stream where you want to write the output.
            RoleARNUpdate (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.
            KinesisFirehoseOutputUpdate (dict) --Describes a Amazon Kinesis Firehose delivery stream as the destination for the output.
            ResourceARNUpdate (string) --Amazon Resource Name (ARN) of the Amazon Kinesis Firehose delivery stream to write to.
            RoleARNUpdate (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant necessary permissions to this role.
            DestinationSchemaUpdate (dict) --Describes the data format when records are written to the destination. For more information, see Configuring Application Output .
            RecordFormatType (string) --Specifies the format of the records on the output stream.
            
            ReferenceDataSourceUpdates (list) --Describes application reference data source updates.
            (dict) --When you update a reference data source configuration for an application, this object provides all the updated values (such as the source bucket name and object key name), the in-application table name that is created, and updated mapping information that maps the data in the Amazon S3 object to the in-application reference table that is created.
            ReferenceId (string) -- [REQUIRED]ID of the reference data source being updated. You can use the DescribeApplication operation to get this value.
            TableNameUpdate (string) --In-application table name that is created by this update.
            S3ReferenceDataSourceUpdate (dict) --Describes the S3 bucket name, object key name, and IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object on your behalf and populate the in-application reference table.
            BucketARNUpdate (string) --Amazon Resource Name (ARN) of the S3 bucket.
            FileKeyUpdate (string) --Object key name.
            ReferenceRoleARNUpdate (string) --ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object and populate the in-application.
            ReferenceSchemaUpdate (dict) --Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
            RecordFormat (dict) -- [REQUIRED]Specifies the format of the records on the streaming source.
            RecordFormatType (string) -- [REQUIRED]The type of record format.
            MappingParameters (dict) --When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
            JSONMappingParameters (dict) --Provides additional mapping information when JSON is the record format on the streaming source.
            RecordRowPath (string) -- [REQUIRED]Path to the top-level parent that contains the records.
            For example, consider the following JSON record:
            In the RecordRowPath , '$' refers to the root and path '$.vehicle.Model' refers to the specific 'Model' key in the JSON.
            CSVMappingParameters (dict) --Provides additional mapping information when the record format uses delimiters (for example, CSV).
            RecordRowDelimiter (string) -- [REQUIRED]Row delimiter. For example, in a CSV format, 'n' is the typical row delimiter.
            RecordColumnDelimiter (string) -- [REQUIRED]Column delimiter. For example, in a CSV format, a comma (',') is the typical column delimiter.
            
            RecordEncoding (string) --Specifies the encoding of the records in the streaming source. For example, UTF-8.
            RecordColumns (list) -- [REQUIRED]A list of RecordColumn objects.
            (dict) --Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.
            Also used to describe the format of the reference data source.
            Name (string) -- [REQUIRED]Name of the column created in the in-application input stream or reference table.
            Mapping (string) --Reference to the data element in the streaming input of the reference data source.
            SqlType (string) -- [REQUIRED]Type of column created in the in-application input stream or reference table.
            
            
            
            
    :type ApplicationUpdate: dict
    """
    pass
