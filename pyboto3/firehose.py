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


def create_delivery_stream(DeliveryStreamName=None, S3DestinationConfiguration=None,
                           RedshiftDestinationConfiguration=None, ElasticsearchDestinationConfiguration=None):
    """
    :param DeliveryStreamName: [REQUIRED]
            The name of the delivery stream.
            
    :type DeliveryStreamName: string
    :param S3DestinationConfiguration: The destination in Amazon S3. This value must be specified if ElasticsearchDestinationConfiguration or RedshiftDestinationConfiguration is specified (see restrictions listed above).
            RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
            BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --Describes CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if Enabled is true.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if Enabled is true.
            
            
    :type S3DestinationConfiguration: dict
    :param RedshiftDestinationConfiguration: The destination in Amazon Redshift. This value cannot be specified if Amazon S3 or Amazon Elasticsearch is the desired destination (see restrictions listed above).
            RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
            ClusterJDBCURL (string) -- [REQUIRED]The database connection string.
            CopyCommand (dict) -- [REQUIRED]The COPY command.
            DataTableName (string) -- [REQUIRED]The name of the target table. The table must already exist in the database.
            DataTableColumns (string) --A comma-separated list of column names.
            CopyOptions (string) --Optional parameters to use with the Amazon Redshift COPY command. For more information, see the 'Optional Parameters' section of Amazon Redshift COPY command . Some possible examples that would apply to Firehose are as follows.
            delimiter '\t' lzop; - fields are delimited with 't' (TAB character) and compressed using lzop.delimiter '| - fields are delimited with '|' (this is the default delimiter).
            delimiter '|' escape - the delimiter should be escaped.
            fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6' - fields are fixed width in the source, with each width specified after every column in the table.
            JSON 's3://mybucket/jsonpaths.txt' - data is in JSON format, and the path specified is the format of the data.
            For more examples, see Amazon Redshift COPY command examples .
            Username (string) -- [REQUIRED]The name of the user.
            Password (string) -- [REQUIRED]The user password.
            RetryOptions (dict) --Configures retry behavior in the event that Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).
            DurationInSeconds (integer) --The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value.
            S3Configuration (dict) -- [REQUIRED]The S3 configuration for the intermediate location from which Amazon Redshift obtains data. Restrictions are described in the topic for CreateDeliveryStream .
            The compression formats SNAPPY or ZIP cannot be specified in RedshiftDestinationConfiguration.S3Configuration because the Amazon Redshift COPY operation that reads from the S3 bucket doesn't support these compression formats.
            RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
            BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --Describes CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if Enabled is true.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if Enabled is true.
            
            CloudWatchLoggingOptions (dict) --Describes CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if Enabled is true.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if Enabled is true.
            
            
    :type RedshiftDestinationConfiguration: dict
    :param ElasticsearchDestinationConfiguration: The destination in Amazon ES. This value cannot be specified if Amazon S3 or Amazon Redshift is the desired destination (see restrictions listed above).
            RoleARN (string) -- [REQUIRED]The ARN of the IAM role to be assumed by Firehose for calling the Amazon ES Configuration API and for indexing documents. For more information, see Amazon S3 Bucket Access .
            DomainARN (string) -- [REQUIRED]The ARN of the Amazon ES domain. The IAM role must have permission for DescribeElasticsearchDomain , DescribeElasticsearchDomains , and DescribeElasticsearchDomainConfig after assuming RoleARN .
            IndexName (string) -- [REQUIRED]The Elasticsearch index name.
            TypeName (string) -- [REQUIRED]The Elasticsearch type name.
            IndexRotationPeriod (string) --The Elasticsearch index rotation period. Index rotation appends a timestamp to the IndexName to facilitate expiration of old data. For more information, see Index Rotation for Amazon Elasticsearch Service Destination . Default value is OneDay .
            BufferingHints (dict) --Buffering options. If no value is specified, ElasticsearchBufferingHints object default values are used.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, set SizeInMBs to be 10 MB or higher.
            RetryOptions (dict) --Configures retry behavior in the event that Firehose is unable to deliver documents to Amazon ES. Default value is 300 (5 minutes).
            DurationInSeconds (integer) --After an initial failure to deliver to Amazon ES, the total amount of time during which Firehose re-attempts delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.
            S3BackupMode (string) --Defines how documents should be delivered to Amazon S3. When set to FailedDocumentsOnly, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with elasticsearch-failed/ appended to the key prefix. When set to AllDocuments, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with elasticsearch-failed/ appended to the prefix. For more information, see Amazon S3 Backup for Amazon Elasticsearch Service Destination . Default value is FailedDocumentsOnly.
            S3Configuration (dict) -- [REQUIRED]Describes the configuration of a destination in Amazon S3.
            RoleARN (string) -- [REQUIRED]The ARN of the AWS credentials.
            BucketARN (string) -- [REQUIRED]The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is UNCOMPRESSED .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --Describes CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if Enabled is true.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if Enabled is true.
            
            CloudWatchLoggingOptions (dict) --Describes CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if Enabled is true.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if Enabled is true.
            
            
    :type ElasticsearchDestinationConfiguration: dict
    """
    pass


def delete_delivery_stream(DeliveryStreamName=None):
    """
    :param DeliveryStreamName: [REQUIRED]
            The name of the delivery stream.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Contains the output of DeleteDeliveryStream .
            
            
    :type DeliveryStreamName: string
    """
    pass


def describe_delivery_stream(DeliveryStreamName=None, Limit=None, ExclusiveStartDestinationId=None):
    """
    :param DeliveryStreamName: [REQUIRED]
            The name of the delivery stream.
            
    :type DeliveryStreamName: string
    :param Limit: The limit on the number of destinations to return. Currently, you can have one destination per delivery stream.
    :type Limit: integer
    :param ExclusiveStartDestinationId: Specifies the destination ID to start returning the destination information. Currently Firehose supports one destination per delivery stream.
    :type ExclusiveStartDestinationId: string
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


def list_delivery_streams(Limit=None, ExclusiveStartDeliveryStreamName=None):
    """
    :param Limit: The maximum number of delivery streams to list.
    :type Limit: integer
    :param ExclusiveStartDeliveryStreamName: The name of the delivery stream to start the list with.
    :type ExclusiveStartDeliveryStreamName: string
    """
    pass


def put_record(DeliveryStreamName=None, Record=None):
    """
    :param DeliveryStreamName: [REQUIRED]
            The name of the delivery stream.
            
    :type DeliveryStreamName: string
    :param Record: [REQUIRED]
            The record.
            Data (bytes) -- [REQUIRED]The data blob, which is base64-encoded when the blob is serialized. The maximum size of the data blob, before base64-encoding, is 1,000 KB.
            
    :type Record: dict
    """
    pass


def put_record_batch(DeliveryStreamName=None, Records=None):
    """
    :param DeliveryStreamName: [REQUIRED]
            The name of the delivery stream.
            
    :type DeliveryStreamName: string
    :param Records: [REQUIRED]
            One or more records.
            (dict) --The unit of data in a delivery stream.
            Data (bytes) -- [REQUIRED]The data blob, which is base64-encoded when the blob is serialized. The maximum size of the data blob, before base64-encoding, is 1,000 KB.
            
            
    :type Records: list
    """
    pass


def update_destination(DeliveryStreamName=None, CurrentDeliveryStreamVersionId=None, DestinationId=None,
                       S3DestinationUpdate=None, RedshiftDestinationUpdate=None, ElasticsearchDestinationUpdate=None):
    """
    :param DeliveryStreamName: [REQUIRED]
            The name of the delivery stream.
            
    :type DeliveryStreamName: string
    :param CurrentDeliveryStreamVersionId: [REQUIRED]
            Obtain this value from the VersionId result of the DeliveryStreamDescription operation. This value is required, and helps the service to perform conditional operations. For example, if there is a interleaving update and this value is null, then the update destination fails. After the update is successful, the VersionId value is updated. The service then performs a merge of the old configuration with the new configuration.
            
    :type CurrentDeliveryStreamVersionId: string
    :param DestinationId: [REQUIRED]
            The ID of the destination.
            
    :type DestinationId: string
    :param S3DestinationUpdate: Describes an update for a destination in Amazon S3.
            RoleARN (string) --The ARN of the AWS credentials.
            BucketARN (string) --The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is NOCOMPRESSION .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --Describes CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if Enabled is true.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if Enabled is true.
            
            
    :type S3DestinationUpdate: dict
    :param RedshiftDestinationUpdate: Describes an update for a destination in Amazon Redshift.
            RoleARN (string) --The ARN of the AWS credentials.
            ClusterJDBCURL (string) --The database connection string.
            CopyCommand (dict) --The COPY command.
            DataTableName (string) -- [REQUIRED]The name of the target table. The table must already exist in the database.
            DataTableColumns (string) --A comma-separated list of column names.
            CopyOptions (string) --Optional parameters to use with the Amazon Redshift COPY command. For more information, see the 'Optional Parameters' section of Amazon Redshift COPY command . Some possible examples that would apply to Firehose are as follows.
            delimiter '\t' lzop; - fields are delimited with 't' (TAB character) and compressed using lzop.delimiter '| - fields are delimited with '|' (this is the default delimiter).
            delimiter '|' escape - the delimiter should be escaped.
            fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6' - fields are fixed width in the source, with each width specified after every column in the table.
            JSON 's3://mybucket/jsonpaths.txt' - data is in JSON format, and the path specified is the format of the data.
            For more examples, see Amazon Redshift COPY command examples .
            Username (string) --The name of the user.
            Password (string) --The user password.
            RetryOptions (dict) --Configures retry behavior in the event that Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).
            DurationInSeconds (integer) --The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value.
            S3Update (dict) --The Amazon S3 destination.
            The compression formats SNAPPY or ZIP cannot be specified in RedshiftDestinationUpdate.S3Update because the Amazon Redshift COPY operation that reads from the S3 bucket doesn't support these compression formats.
            RoleARN (string) --The ARN of the AWS credentials.
            BucketARN (string) --The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is NOCOMPRESSION .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --Describes CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if Enabled is true.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if Enabled is true.
            
            CloudWatchLoggingOptions (dict) --Describes CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if Enabled is true.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if Enabled is true.
            
            
    :type RedshiftDestinationUpdate: dict
    :param ElasticsearchDestinationUpdate: Describes an update for a destination in Amazon ES.
            RoleARN (string) --The ARN of the IAM role to be assumed by Firehose for calling the Amazon ES Configuration API and for indexing documents. For more information, see Amazon S3 Bucket Access .
            DomainARN (string) --The ARN of the Amazon ES domain. The IAM role must have permission for DescribeElasticsearchDomain, DescribeElasticsearchDomains , and DescribeElasticsearchDomainConfig after assuming RoleARN .
            IndexName (string) --The Elasticsearch index name.
            TypeName (string) --The Elasticsearch type name.
            IndexRotationPeriod (string) --The Elasticsearch index rotation period. Index rotation appends a timestamp to the IndexName to facilitate the expiration of old data. For more information, see Index Rotation for Amazon Elasticsearch Service Destination . Default value is OneDay .
            BufferingHints (dict) --Buffering options. If no value is specified, ElasticsearchBufferingHints object default values are used.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, set SizeInMBs to be 10 MB or higher.
            RetryOptions (dict) --Configures retry behavior in the event that Firehose is unable to deliver documents to Amazon ES. Default value is 300 (5 minutes).
            DurationInSeconds (integer) --After an initial failure to deliver to Amazon ES, the total amount of time during which Firehose re-attempts delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.
            S3Update (dict) --Describes an update for a destination in Amazon S3.
            RoleARN (string) --The ARN of the AWS credentials.
            BucketARN (string) --The ARN of the S3 bucket.
            Prefix (string) --The 'YYYY/MM/DD/HH' time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Firehose Developer Guide .
            BufferingHints (dict) --The buffering option. If no value is specified, BufferingHints object default values are used.
            SizeInMBs (integer) --Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
            We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
            IntervalInSeconds (integer) --Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
            CompressionFormat (string) --The compression format. If no value is specified, the default is NOCOMPRESSION .
            The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.
            EncryptionConfiguration (dict) --The encryption configuration. If no value is specified, the default is no encryption.
            NoEncryptionConfig (string) --Specifically override existing encryption information to ensure no encryption is used.
            KMSEncryptionConfig (dict) --The encryption key.
            AWSKMSKeyARN (string) -- [REQUIRED]The ARN of the encryption key. Must belong to the same region as the destination Amazon S3 bucket.
            
            CloudWatchLoggingOptions (dict) --Describes CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if Enabled is true.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if Enabled is true.
            
            CloudWatchLoggingOptions (dict) --Describes CloudWatch logging options for your delivery stream.
            Enabled (boolean) --Enables or disables CloudWatch logging.
            LogGroupName (string) --The CloudWatch group name for logging. This value is required if Enabled is true.
            LogStreamName (string) --The CloudWatch log stream name for logging. This value is required if Enabled is true.
            
            
    :type ElasticsearchDestinationUpdate: dict
    """
    pass
