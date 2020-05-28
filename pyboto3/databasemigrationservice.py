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

def add_tags_to_resource(ResourceArn=None, Tags=None):
    """
    Adds metadata tags to an AWS DMS resource, including replication instance, endpoint, security group, and migration task. These tags can also be used with cost allocation reporting to track cost associated with DMS resources, or used in a Condition statement in an IAM policy for DMS.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Adds metadata tags to an AWS DMS resource, including replication instance, endpoint, security group, and migration task. These tags can also be used with cost allocation reporting to track cost associated with AWS DMS resources, or used in a Condition statement in an IAM policy for AWS DMS.
    Expected Output:
    
    :example: response = client.add_tags_to_resource(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nIdentifies the AWS DMS resource to which tags should be added. The value for this parameter is an Amazon Resource Name (ARN).\nFor AWS DMS, you can tag a replication instance, an endpoint, or a replication task.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nOne or more tags to be assigned to the resource.\n\n(dict) --A user-defined key-value pair that describes metadata added to an AWS DMS resource and that is used by operations such as the following:\n\nAddTagsToResource\nListTagsForResource\nRemoveTagsFromResource\n\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault

Examples
Adds metadata tags to an AWS DMS resource, including replication instance, endpoint, security group, and migration task. These tags can also be used with cost allocation reporting to track cost associated with AWS DMS resources, or used in a Condition statement in an IAM policy for AWS DMS.
response = client.add_tags_to_resource(
    # Required. Use the ARN of the resource you want to tag.
    ResourceArn='arn:aws:dms:us-east-1:123456789012:endpoint:ASXWXJZLNWNT5HTWCGV2BUJQ7E',
    # Required. Use the Key/Value pair format.
    Tags=[
        {
            'Key': 'Acount',
            'Value': '1633456',
        },
    ],
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def apply_pending_maintenance_action(ReplicationInstanceArn=None, ApplyAction=None, OptInType=None):
    """
    Applies a pending maintenance action to a resource (for example, to a replication instance).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.apply_pending_maintenance_action(
        ReplicationInstanceArn='string',
        ApplyAction='string',
        OptInType='string'
    )
    
    
    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the AWS DMS resource that the pending maintenance action applies to.\n

    :type ApplyAction: string
    :param ApplyAction: [REQUIRED]\nThe pending maintenance action to apply to this resource.\n

    :type OptInType: string
    :param OptInType: [REQUIRED]\nA value that specifies the type of opt-in request, or undoes an opt-in request. You can\'t undo an opt-in request of type immediate .\nValid values:\n\nimmediate - Apply the maintenance action immediately.\nnext-maintenance - Apply the maintenance action during the next maintenance window for the resource.\nundo-opt-in - Cancel any existing next-maintenance opt-in requests.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourcePendingMaintenanceActions': {
        'ResourceIdentifier': 'string',
        'PendingMaintenanceActionDetails': [
            {
                'Action': 'string',
                'AutoAppliedAfterDate': datetime(2015, 1, 1),
                'ForcedApplyDate': datetime(2015, 1, 1),
                'OptInStatus': 'string',
                'CurrentApplyDate': datetime(2015, 1, 1),
                'Description': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

ResourcePendingMaintenanceActions (dict) --
The AWS DMS resource that the pending maintenance action will be applied to.

ResourceIdentifier (string) --
The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action applies to. For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) for AWS DMS in the DMS documentation.

PendingMaintenanceActionDetails (list) --
Detailed information about the pending maintenance action.

(dict) --
Describes a maintenance action pending for an AWS DMS resource, including when and how it will be applied. This data type is a response element to the DescribePendingMaintenanceActions operation.

Action (string) --
The type of pending maintenance action that is available for the resource.

AutoAppliedAfterDate (datetime) --
The date of the maintenance window when the action is to be applied. The maintenance action is applied to the resource during its first maintenance window after this date. If this date is specified, any next-maintenance opt-in requests are ignored.

ForcedApplyDate (datetime) --
The date when the maintenance action will be automatically applied. The maintenance action is applied to the resource on this date regardless of the maintenance window for the resource. If this date is specified, any immediate opt-in requests are ignored.

OptInStatus (string) --
The type of opt-in request that has been received for the resource.

CurrentApplyDate (datetime) --
The effective date when the pending maintenance action will be applied to the resource. This date takes into account opt-in requests received from the ApplyPendingMaintenanceAction API operation, and also the AutoAppliedAfterDate and ForcedApplyDate parameter values. This value is blank if an opt-in request has not been received and nothing has been specified for AutoAppliedAfterDate or ForcedApplyDate .

Description (string) --
A description providing more detail about the maintenance action.













Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault


    :return: {
        'ResourcePendingMaintenanceActions': {
            'ResourceIdentifier': 'string',
            'PendingMaintenanceActionDetails': [
                {
                    'Action': 'string',
                    'AutoAppliedAfterDate': datetime(2015, 1, 1),
                    'ForcedApplyDate': datetime(2015, 1, 1),
                    'OptInStatus': 'string',
                    'CurrentApplyDate': datetime(2015, 1, 1),
                    'Description': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_endpoint(EndpointIdentifier=None, EndpointType=None, EngineName=None, Username=None, Password=None, ServerName=None, Port=None, DatabaseName=None, ExtraConnectionAttributes=None, KmsKeyId=None, Tags=None, CertificateArn=None, SslMode=None, ServiceAccessRoleArn=None, ExternalTableDefinition=None, DynamoDbSettings=None, S3Settings=None, DmsTransferSettings=None, MongoDbSettings=None, KinesisSettings=None, KafkaSettings=None, ElasticsearchSettings=None, NeptuneSettings=None, RedshiftSettings=None):
    """
    Creates an endpoint using the provided settings.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates an endpoint using the provided settings.
    Expected Output:
    
    :example: response = client.create_endpoint(
        EndpointIdentifier='string',
        EndpointType='source'|'target',
        EngineName='string',
        Username='string',
        Password='string',
        ServerName='string',
        Port=123,
        DatabaseName='string',
        ExtraConnectionAttributes='string',
        KmsKeyId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        CertificateArn='string',
        SslMode='none'|'require'|'verify-ca'|'verify-full',
        ServiceAccessRoleArn='string',
        ExternalTableDefinition='string',
        DynamoDbSettings={
            'ServiceAccessRoleArn': 'string'
        },
        S3Settings={
            'ServiceAccessRoleArn': 'string',
            'ExternalTableDefinition': 'string',
            'CsvRowDelimiter': 'string',
            'CsvDelimiter': 'string',
            'BucketFolder': 'string',
            'BucketName': 'string',
            'CompressionType': 'none'|'gzip',
            'EncryptionMode': 'sse-s3'|'sse-kms',
            'ServerSideEncryptionKmsKeyId': 'string',
            'DataFormat': 'csv'|'parquet',
            'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
            'DictPageSizeLimit': 123,
            'RowGroupLength': 123,
            'DataPageSize': 123,
            'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
            'EnableStatistics': True|False,
            'IncludeOpForFullLoad': True|False,
            'CdcInsertsOnly': True|False,
            'TimestampColumnName': 'string',
            'ParquetTimestampInMillisecond': True|False,
            'CdcInsertsAndUpdates': True|False
        },
        DmsTransferSettings={
            'ServiceAccessRoleArn': 'string',
            'BucketName': 'string'
        },
        MongoDbSettings={
            'Username': 'string',
            'Password': 'string',
            'ServerName': 'string',
            'Port': 123,
            'DatabaseName': 'string',
            'AuthType': 'no'|'password',
            'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
            'NestingLevel': 'none'|'one',
            'ExtractDocId': 'string',
            'DocsToInvestigate': 'string',
            'AuthSource': 'string',
            'KmsKeyId': 'string'
        },
        KinesisSettings={
            'StreamArn': 'string',
            'MessageFormat': 'json'|'json-unformatted',
            'ServiceAccessRoleArn': 'string',
            'IncludeTransactionDetails': True|False,
            'IncludePartitionValue': True|False,
            'PartitionIncludeSchemaTable': True|False,
            'IncludeTableAlterOperations': True|False,
            'IncludeControlDetails': True|False
        },
        KafkaSettings={
            'Broker': 'string',
            'Topic': 'string'
        },
        ElasticsearchSettings={
            'ServiceAccessRoleArn': 'string',
            'EndpointUri': 'string',
            'FullLoadErrorPercentage': 123,
            'ErrorRetryDuration': 123
        },
        NeptuneSettings={
            'ServiceAccessRoleArn': 'string',
            'S3BucketName': 'string',
            'S3BucketFolder': 'string',
            'ErrorRetryDuration': 123,
            'MaxFileSize': 123,
            'MaxRetryCount': 123,
            'IamAuthEnabled': True|False
        },
        RedshiftSettings={
            'AcceptAnyDate': True|False,
            'AfterConnectScript': 'string',
            'BucketFolder': 'string',
            'BucketName': 'string',
            'ConnectionTimeout': 123,
            'DatabaseName': 'string',
            'DateFormat': 'string',
            'EmptyAsNull': True|False,
            'EncryptionMode': 'sse-s3'|'sse-kms',
            'FileTransferUploadStreams': 123,
            'LoadTimeout': 123,
            'MaxFileSize': 123,
            'Password': 'string',
            'Port': 123,
            'RemoveQuotes': True|False,
            'ReplaceInvalidChars': 'string',
            'ReplaceChars': 'string',
            'ServerName': 'string',
            'ServiceAccessRoleArn': 'string',
            'ServerSideEncryptionKmsKeyId': 'string',
            'TimeFormat': 'string',
            'TrimBlanks': True|False,
            'TruncateColumns': True|False,
            'Username': 'string',
            'WriteBufferSize': 123
        }
    )
    
    
    :type EndpointIdentifier: string
    :param EndpointIdentifier: [REQUIRED]\nThe database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can\'t end with a hyphen or contain two consecutive hyphens.\n

    :type EndpointType: string
    :param EndpointType: [REQUIRED]\nThe type of endpoint. Valid values are source and target .\n

    :type EngineName: string
    :param EngineName: [REQUIRED]\nThe type of engine for the endpoint. Valid values, depending on the EndpointType value, include 'mysql' , 'oracle' , 'postgres' , 'mariadb' , 'aurora' , 'aurora-postgresql' , 'redshift' , 's3' , 'db2' , 'azuredb' , 'sybase' , 'dynamodb' , 'mongodb' , 'kinesis' , 'kafka' , 'elasticsearch' , 'documentdb' , and 'sqlserver' .\n

    :type Username: string
    :param Username: The user name to be used to log in to the endpoint database.

    :type Password: string
    :param Password: The password to be used to log in to the endpoint database.

    :type ServerName: string
    :param ServerName: The name of the server where the endpoint database resides.

    :type Port: integer
    :param Port: The port used by the endpoint database.

    :type DatabaseName: string
    :param DatabaseName: The name of the endpoint database.

    :type ExtraConnectionAttributes: string
    :param ExtraConnectionAttributes: Additional attributes associated with the connection. Each attribute is specified as a name-value pair associated by an equal sign (=). Multiple attributes are separated by a semicolon (;) with no additional white space. For information on the attributes available for connecting your source or target endpoint, see Working with AWS DMS Endpoints in the AWS Database Migration Service User Guide.

    :type KmsKeyId: string
    :param KmsKeyId: An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint.\nIf you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key.\nAWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.\n

    :type Tags: list
    :param Tags: One or more tags to be assigned to the endpoint.\n\n(dict) --A user-defined key-value pair that describes metadata added to an AWS DMS resource and that is used by operations such as the following:\n\nAddTagsToResource\nListTagsForResource\nRemoveTagsFromResource\n\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :type CertificateArn: string
    :param CertificateArn: The Amazon Resource Name (ARN) for the certificate.

    :type SslMode: string
    :param SslMode: The Secure Sockets Layer (SSL) mode to use for the SSL connection. The default is none

    :type ServiceAccessRoleArn: string
    :param ServiceAccessRoleArn: The Amazon Resource Name (ARN) for the service access role that you want to use to create the endpoint.

    :type ExternalTableDefinition: string
    :param ExternalTableDefinition: The external table definition.

    :type DynamoDbSettings: dict
    :param DynamoDbSettings: Settings in JSON format for the target Amazon DynamoDB endpoint. For information about other available settings, see Using Object Mapping to Migrate Data to DynamoDB in the AWS Database Migration Service User Guide.\n\nServiceAccessRoleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) used by the service access IAM role.\n\n\n

    :type S3Settings: dict
    :param S3Settings: Settings in JSON format for the target Amazon S3 endpoint. For more information about the available settings, see Extra Connection Attributes When Using Amazon S3 as a Target for AWS DMS in the AWS Database Migration Service User Guide.\n\nServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) used by the service access IAM role.\n\nExternalTableDefinition (string) --The external table definition.\n\nCsvRowDelimiter (string) --The delimiter used to separate rows in the source files. The default is a carriage return (\\n ).\n\nCsvDelimiter (string) --The delimiter used to separate columns in the source files. The default is a comma.\n\nBucketFolder (string) --An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in the path `` bucketFolder /schema_name /table_name /`` . If this parameter isn\'t specified, then the path used is `` schema_name /table_name /`` .\n\nBucketName (string) --The name of the S3 bucket.\n\nCompressionType (string) --An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the target files. Either set this parameter to NONE (the default) or don\'t use it to leave the files uncompressed. This parameter applies to both .csv and .parquet file formats.\n\nEncryptionMode (string) --The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either SSE_S3 (the default) or SSE_KMS . To use SSE_S3 , you need an AWS Identity and Access Management (IAM) role with permission to allow 'arn:aws:s3:::dms-*' to use the following actions:\n\ns3:CreateBucket\ns3:ListBucket\ns3:DeleteBucket\ns3:GetBucketLocation\ns3:GetObject\ns3:PutObject\ns3:DeleteObject\ns3:GetObjectVersion\ns3:GetBucketPolicy\ns3:PutBucketPolicy\ns3:DeleteBucketPolicy\n\n\nServerSideEncryptionKmsKeyId (string) --If you are using SSE_KMS for the EncryptionMode , provide the AWS KMS key ID. The key that you use needs an attached policy that enables AWS Identity and Access Management (IAM) user permissions and allows use of the key.\nHere is a CLI example: ``aws dms create-endpoint --endpoint-identifier value --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value* ,BucketFolder=*value* ,BucketName=*value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``\n\nDataFormat (string) --The format of the data that you want to use for output. You can choose one of the following:\n\ncsv : This is a row-based file format with comma-separated values (.csv).\nparquet : Apache Parquet (.parquet) is a columnar storage file format that features efficient compression and provides faster query response.\n\n\nEncodingType (string) --The type of encoding you are using:\n\nRLE_DICTIONARY uses a combination of bit-packing and run-length encoding to store repeated values more efficiently. This is the default.\nPLAIN doesn\'t use encoding at all. Values are stored as they are.\nPLAIN_DICTIONARY builds a dictionary of the values encountered in a given column. The dictionary is stored in a dictionary page for each column chunk.\n\n\nDictPageSizeLimit (integer) --The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds this, this column is stored using an encoding type of PLAIN . This parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to PLAIN encoding. This size is used for .parquet file format only.\n\nRowGroupLength (integer) --The number of rows in a row group. A smaller row group size provides faster reads. But as the number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows. This number is used for .parquet file format only.\nIf you choose a value larger than the maximum, RowGroupLength is set to the max row group length in bytes (64 * 1024 * 1024).\n\nDataPageSize (integer) --The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This number is used for .parquet file format only.\n\nParquetVersion (string) --The version of the Apache Parquet format that you want to use: parquet_1_0 (the default) or parquet_2_0 .\n\nEnableStatistics (boolean) --A value that enables statistics for Parquet pages and row groups. Choose true to enable statistics, false to disable. Statistics include NULL , DISTINCT , MAX , and MIN values. This parameter defaults to true . This value is used for .parquet file format only.\n\nIncludeOpForFullLoad (boolean) --A value that enables a full load to write INSERT operations to the comma-separated value (.csv) output files only to indicate how the rows were added to the source database.\n\nNote\nAWS DMS supports the IncludeOpForFullLoad parameter in versions 3.1.4 and later.\n\nFor full load, records can only be inserted. By default (the false setting), no information is recorded in these output files for a full load to indicate that the rows were inserted at the source database. If IncludeOpForFullLoad is set to true or y , the INSERT is recorded as an I annotation in the first field of the .csv file. This allows the format of your target records from a full load to be consistent with the target records from a CDC load.\n\nNote\nThis setting works together with the CdcInsertsOnly and the CdcInsertsAndUpdates parameters for output to .csv files only. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .\n\n\nCdcInsertsOnly (boolean) --A value that enables a change data capture (CDC) load to write only INSERT operations to .csv or columnar storage (.parquet) output files. By default (the false setting), the first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated, or deleted at the source database for a CDC load to the target.\nIf CdcInsertsOnly is set to true or y , only INSERTs from the source database are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded depends on the value of IncludeOpForFullLoad . If IncludeOpForFullLoad is set to true , the first field of every CDC record is set to I to indicate the INSERT operation at the source. If IncludeOpForFullLoad is set to false , every CDC record is written without a first field to indicate the INSERT operation at the source. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .\n\nNote\nAWS DMS supports the interaction described preceding between the CdcInsertsOnly and IncludeOpForFullLoad parameters in versions 3.1.4 and later.\n\nCdcInsertsOnly and CdcInsertsAndUpdates can\'t both be set to true for the same endpoint. Set either CdcInsertsOnly or CdcInsertsAndUpdates to true for the same endpoint, but not both.\n\n\nTimestampColumnName (string) --A value that when nonblank causes AWS DMS to add a column with timestamp information to the endpoint data for an Amazon S3 target.\n\nNote\nAWS DMS supports the TimestampColumnName parameter in versions 3.1.4 and later.\n\nDMS includes an additional STRING column in the .csv or .parquet object files of your migrated data when you set TimestampColumnName to a nonblank value.\nFor a full load, each row of this timestamp column contains a timestamp for when the data was transferred from the source to the target by DMS.\nFor a change data capture (CDC) load, each row of the timestamp column contains the timestamp for the commit of that row in the source database.\nThe string format for this timestamp column value is yyyy-MM-dd HH:mm:ss.SSSSSS . By default, the precision of this value is in microseconds. For a CDC load, the rounding of the precision depends on the commit timestamp supported by DMS for the source database.\nWhen the AddColumnName parameter is set to true , DMS also includes a name for the timestamp column that you set with TimestampColumnName .\n\nParquetTimestampInMillisecond (boolean) --A value that specifies the precision of any TIMESTAMP column values that are written to an Amazon S3 object file in .parquet format.\n\nNote\nAWS DMS supports the ParquetTimestampInMillisecond parameter in versions 3.1.4 and later.\n\nWhen ParquetTimestampInMillisecond is set to true or y , AWS DMS writes all TIMESTAMP columns in a .parquet formatted file with millisecond precision. Otherwise, DMS writes them with microsecond precision.\nCurrently, Amazon Athena and AWS Glue can handle only millisecond precision for TIMESTAMP values. Set this parameter to true for S3 endpoint object files that are .parquet formatted only if you plan to query or process the data with Athena or AWS Glue.\n\nNote\nAWS DMS writes any TIMESTAMP column values written to an S3 file in .csv format with microsecond precision.\nSetting ParquetTimestampInMillisecond has no effect on the string format of the timestamp column value that is inserted by setting the TimestampColumnName parameter.\n\n\nCdcInsertsAndUpdates (boolean) --A value that enables a change data capture (CDC) load to write INSERT and UPDATE operations to .csv or .parquet (columnar storage) output files. The default setting is false , but when CdcInsertsAndUpdates is set to true or y , INSERTs and UPDATEs from the source database are migrated to the .csv or .parquet file.\nFor .csv file format only, how these INSERTs and UPDATEs are recorded depends on the value of the IncludeOpForFullLoad parameter. If IncludeOpForFullLoad is set to true , the first field of every CDC record is set to either I or U to indicate INSERT and UPDATE operations at the source. But if IncludeOpForFullLoad is set to false , CDC records are written without an indication of INSERT or UPDATE operations at the source. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .\n\nNote\nAWS DMS supports the use of the CdcInsertsAndUpdates parameter in versions 3.3.1 and later.\n\nCdcInsertsOnly and CdcInsertsAndUpdates can\'t both be set to true for the same endpoint. Set either CdcInsertsOnly or CdcInsertsAndUpdates to true for the same endpoint, but not both.\n\n\n\n

    :type DmsTransferSettings: dict
    :param DmsTransferSettings: The settings in JSON format for the DMS transfer type of source endpoint.\nPossible settings include the following:\n\nServiceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.\nBucketName - The name of the S3 bucket to use.\nCompressionType - An optional parameter to use GZIP to compress the target files. To use GZIP, set this value to NONE (the default). To keep the files uncompressed, don\'t use this value.\n\nShorthand syntax for these settings is as follows: ServiceAccessRoleArn=string,BucketName=string,CompressionType=string\nJSON syntax for these settings is as follows: { 'ServiceAccessRoleArn': 'string', 'BucketName': 'string', 'CompressionType': 'none'|'gzip' }\n\nServiceAccessRoleArn (string) --The IAM role that has permission to access the Amazon S3 bucket.\n\nBucketName (string) --The name of the S3 bucket to use.\n\n\n

    :type MongoDbSettings: dict
    :param MongoDbSettings: Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see Using MongoDB as a Target for AWS Database Migration Service in the AWS Database Migration Service User Guide.\n\nUsername (string) --The user name you use to access the MongoDB source endpoint.\n\nPassword (string) --The password for the user account you use to access the MongoDB source endpoint.\n\nServerName (string) --The name of the server on the MongoDB source endpoint.\n\nPort (integer) --The port value for the MongoDB source endpoint.\n\nDatabaseName (string) --The database name on the MongoDB source endpoint.\n\nAuthType (string) --The authentication type you use to access the MongoDB source endpoint.\nValid values: NO, PASSWORD\nWhen NO is selected, user name and password parameters are not used and can be empty.\n\nAuthMechanism (string) --The authentication mechanism you use to access the MongoDB source endpoint.\nValid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1\nDEFAULT \xe2\x80\x93 For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use SCRAM_SHA_1. This setting isn\'t used when authType=No.\n\nNestingLevel (string) --Specifies either document or table mode.\nValid values: NONE, ONE\nDefault value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.\n\nExtractDocId (string) --Specifies the document ID. Use this setting when NestingLevel is set to NONE.\nDefault value is false.\n\nDocsToInvestigate (string) --Indicates the number of documents to preview to determine the document organization. Use this setting when NestingLevel is set to ONE.\nMust be a positive value greater than 0. Default value is 1000.\n\nAuthSource (string) --The MongoDB database name. This setting isn\'t used when authType=NO .\nThe default is admin.\n\nKmsKeyId (string) --The AWS KMS key identifier that is used to encrypt the content on the replication instance. If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.\n\n\n

    :type KinesisSettings: dict
    :param KinesisSettings: Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams. For more information about the available settings, see Using Amazon Kinesis Data Streams as a Target for AWS Database Migration Service in the AWS Database Migration User Guide.\n\nStreamArn (string) --The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.\n\nMessageFormat (string) --The output format for the records created on the endpoint. The message format is JSON (default) or JSON_UNFORMATTED (a single line with no tab).\n\nServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) for the AWS Identity and Access Management (IAM) role that AWS DMS uses to write to the Kinesis data stream.\n\nIncludeTransactionDetails (boolean) --Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for transaction_id , previous transaction_id , and transaction_record_id (the record offset within a transaction). The default is False .\n\nIncludePartitionValue (boolean) --Shows the partition value within the Kinesis message output, unless the partition type is schema-table-type . The default is False .\n\nPartitionIncludeSchemaTable (boolean) --Prefixes schema and table names to partition values, when the partition type is primary-key-type . Doing this increases data distribution among Kinesis shards. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same shard, which causes throttling. The default is False .\n\nIncludeTableAlterOperations (boolean) --Includes any data definition language (DDL) operations that change the table in the control data, such as rename-table , drop-table , add-column , drop-column , and rename-column . The default is False .\n\nIncludeControlDetails (boolean) --Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output. The default is False .\n\n\n

    :type KafkaSettings: dict
    :param KafkaSettings: Settings in JSON format for the target Apache Kafka endpoint. For more information about the available settings, see Using Apache Kafka as a Target for AWS Database Migration Service in the AWS Database Migration User Guide.\n\nBroker (string) --The broker location and port of the Kafka broker that hosts your Kafka instance. Specify the broker in the form `` broker-hostname-or-ip :port `` . For example, 'ec2-12-345-678-901.compute-1.amazonaws.com:2345' .\n\nTopic (string) --The topic to which you migrate the data. If you don\'t specify a topic, AWS DMS specifies 'kafka-default-topic' as the migration topic.\n\n\n

    :type ElasticsearchSettings: dict
    :param ElasticsearchSettings: Settings in JSON format for the target Elasticsearch endpoint. For more information about the available settings, see Extra Connection Attributes When Using Elasticsearch as a Target for AWS DMS in the AWS Database Migration User Guide.\n\nServiceAccessRoleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) used by service to access the IAM role.\n\nEndpointUri (string) -- [REQUIRED]The endpoint for the Elasticsearch cluster.\n\nFullLoadErrorPercentage (integer) --The maximum percentage of records that can fail to be written before a full load operation stops.\n\nErrorRetryDuration (integer) --The maximum number of seconds for which DMS retries failed API requests to the Elasticsearch cluster.\n\n\n

    :type NeptuneSettings: dict
    :param NeptuneSettings: Settings in JSON format for the target Amazon Neptune endpoint. For more information about the available settings, see https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings in the AWS Database Migration Service User Guide.\n\nServiceAccessRoleArn (string) --The ARN of the service role you have created for the Neptune target endpoint. For more information, see https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.ServiceRole in the AWS Database Migration Service User Guide.\n\nS3BucketName (string) -- [REQUIRED]The name of the S3 bucket for AWS DMS to temporarily store migrated graph data in CSV files before bulk-loading it to the Neptune target database. AWS DMS maps the SQL source data to graph data before storing it in these CSV files.\n\nS3BucketFolder (string) -- [REQUIRED]A folder path where you where you want AWS DMS to store migrated graph data in the S3 bucket specified by S3BucketName\n\nErrorRetryDuration (integer) --The number of milliseconds for AWS DMS to wait to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 250.\n\nMaxFileSize (integer) --The maximum size in KB of migrated graph data stored in a CSV file before AWS DMS bulk-loads the data to the Neptune target database. The default is 1048576 KB. If successful, AWS DMS clears the bucket, ready to store the next batch of migrated graph data.\n\nMaxRetryCount (integer) --The number of times for AWS DMS to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 5.\n\nIamAuthEnabled (boolean) --If you want IAM authorization enabled for this endpoint, set this parameter to true and attach the appropriate role policy document to your service role specified by ServiceAccessRoleArn . The default is false .\n\n\n

    :type RedshiftSettings: dict
    :param RedshiftSettings: Provides information that defines an Amazon Redshift endpoint.\n\nAcceptAnyDate (boolean) --A value that indicates to allow any date format, including invalid formats such as 00/00/00 00:00:00, to be loaded without generating an error. You can choose true or false (the default).\nThis parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data doesn\'t match the DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.\n\nAfterConnectScript (string) --Code to run after connecting. This parameter should contain the code itself, not the name of a file containing the code.\n\nBucketFolder (string) --The location where the comma-separated value (.csv) files are stored before being uploaded to the S3 bucket.\n\nBucketName (string) --The name of the S3 bucket you want to use\n\nConnectionTimeout (integer) --A value that sets the amount of time to wait (in milliseconds) before timing out, beginning from when you initially establish a connection.\n\nDatabaseName (string) --The name of the Amazon Redshift data warehouse (service) that you are working with.\n\nDateFormat (string) --The date format that you are using. Valid values are auto (case-sensitive), your date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults to a format of \'YYYY-MM-DD\'. Using auto recognizes most strings, even some that aren\'t supported when you use a date format string.\nIf your date and time values use formats different from each other, set this to auto .\n\nEmptyAsNull (boolean) --A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL. A value of true sets empty CHAR and VARCHAR fields to null. The default is false .\n\nEncryptionMode (string) --The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either SSE_S3 (the default) or SSE_KMS . To use SSE_S3 , create an AWS Identity and Access Management (IAM) role with a policy that allows 'arn:aws:s3:::*' to use the following actions: 's3:PutObject', 's3:ListBucket'\n\nFileTransferUploadStreams (integer) --The number of threads used to upload a single file. This parameter accepts a value from 1 through 64. It defaults to 10.\n\nLoadTimeout (integer) --The amount of time to wait (in milliseconds) before timing out, beginning from when you begin loading.\n\nMaxFileSize (integer) --The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).\n\nPassword (string) --The password for the user named in the username property.\n\nPort (integer) --The port number for Amazon Redshift. The default value is 5439.\n\nRemoveQuotes (boolean) --A value that specifies to remove surrounding quotation marks from strings in the incoming data. All characters within the quotation marks, including delimiters, are retained. Choose true to remove quotation marks. The default is false .\n\nReplaceInvalidChars (string) --A list of characters that you want to replace. Use with ReplaceChars .\n\nReplaceChars (string) --A value that specifies to replaces the invalid characters specified in ReplaceInvalidChars , substituting the specified characters instead. The default is '?' .\n\nServerName (string) --The name of the Amazon Redshift cluster you are using.\n\nServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service.\n\nServerSideEncryptionKmsKeyId (string) --The AWS KMS key ID. If you are using SSE_KMS for the EncryptionMode , provide this key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.\n\nTimeFormat (string) --The time format that you want to use. Valid values are auto (case-sensitive), \'timeformat_string\' , \'epochsecs\' , or \'epochmillisecs\' . It defaults to 10. Using auto recognizes most strings, even some that aren\'t supported when you use a time format string.\nIf your date and time values use formats different from each other, set this parameter to auto .\n\nTrimBlanks (boolean) --A value that specifies to remove the trailing white space characters from a VARCHAR string. This parameter applies only to columns with a VARCHAR data type. Choose true to remove unneeded white space. The default is false .\n\nTruncateColumns (boolean) --A value that specifies to truncate data in columns to the appropriate number of characters, so that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose true to truncate data. The default is false .\n\nUsername (string) --An Amazon Redshift user name for a registered user.\n\nWriteBufferSize (integer) --The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The default is 1,024. Use this setting to tune performance.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Endpoint': {
        'EndpointIdentifier': 'string',
        'EndpointType': 'source'|'target',
        'EngineName': 'string',
        'EngineDisplayName': 'string',
        'Username': 'string',
        'ServerName': 'string',
        'Port': 123,
        'DatabaseName': 'string',
        'ExtraConnectionAttributes': 'string',
        'Status': 'string',
        'KmsKeyId': 'string',
        'EndpointArn': 'string',
        'CertificateArn': 'string',
        'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
        'ServiceAccessRoleArn': 'string',
        'ExternalTableDefinition': 'string',
        'ExternalId': 'string',
        'DynamoDbSettings': {
            'ServiceAccessRoleArn': 'string'
        },
        'S3Settings': {
            'ServiceAccessRoleArn': 'string',
            'ExternalTableDefinition': 'string',
            'CsvRowDelimiter': 'string',
            'CsvDelimiter': 'string',
            'BucketFolder': 'string',
            'BucketName': 'string',
            'CompressionType': 'none'|'gzip',
            'EncryptionMode': 'sse-s3'|'sse-kms',
            'ServerSideEncryptionKmsKeyId': 'string',
            'DataFormat': 'csv'|'parquet',
            'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
            'DictPageSizeLimit': 123,
            'RowGroupLength': 123,
            'DataPageSize': 123,
            'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
            'EnableStatistics': True|False,
            'IncludeOpForFullLoad': True|False,
            'CdcInsertsOnly': True|False,
            'TimestampColumnName': 'string',
            'ParquetTimestampInMillisecond': True|False,
            'CdcInsertsAndUpdates': True|False
        },
        'DmsTransferSettings': {
            'ServiceAccessRoleArn': 'string',
            'BucketName': 'string'
        },
        'MongoDbSettings': {
            'Username': 'string',
            'Password': 'string',
            'ServerName': 'string',
            'Port': 123,
            'DatabaseName': 'string',
            'AuthType': 'no'|'password',
            'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
            'NestingLevel': 'none'|'one',
            'ExtractDocId': 'string',
            'DocsToInvestigate': 'string',
            'AuthSource': 'string',
            'KmsKeyId': 'string'
        },
        'KinesisSettings': {
            'StreamArn': 'string',
            'MessageFormat': 'json'|'json-unformatted',
            'ServiceAccessRoleArn': 'string',
            'IncludeTransactionDetails': True|False,
            'IncludePartitionValue': True|False,
            'PartitionIncludeSchemaTable': True|False,
            'IncludeTableAlterOperations': True|False,
            'IncludeControlDetails': True|False
        },
        'KafkaSettings': {
            'Broker': 'string',
            'Topic': 'string'
        },
        'ElasticsearchSettings': {
            'ServiceAccessRoleArn': 'string',
            'EndpointUri': 'string',
            'FullLoadErrorPercentage': 123,
            'ErrorRetryDuration': 123
        },
        'NeptuneSettings': {
            'ServiceAccessRoleArn': 'string',
            'S3BucketName': 'string',
            'S3BucketFolder': 'string',
            'ErrorRetryDuration': 123,
            'MaxFileSize': 123,
            'MaxRetryCount': 123,
            'IamAuthEnabled': True|False
        },
        'RedshiftSettings': {
            'AcceptAnyDate': True|False,
            'AfterConnectScript': 'string',
            'BucketFolder': 'string',
            'BucketName': 'string',
            'ConnectionTimeout': 123,
            'DatabaseName': 'string',
            'DateFormat': 'string',
            'EmptyAsNull': True|False,
            'EncryptionMode': 'sse-s3'|'sse-kms',
            'FileTransferUploadStreams': 123,
            'LoadTimeout': 123,
            'MaxFileSize': 123,
            'Password': 'string',
            'Port': 123,
            'RemoveQuotes': True|False,
            'ReplaceInvalidChars': 'string',
            'ReplaceChars': 'string',
            'ServerName': 'string',
            'ServiceAccessRoleArn': 'string',
            'ServerSideEncryptionKmsKeyId': 'string',
            'TimeFormat': 'string',
            'TrimBlanks': True|False,
            'TruncateColumns': True|False,
            'Username': 'string',
            'WriteBufferSize': 123
        }
    }
}


Response Structure

(dict) --

Endpoint (dict) --
The endpoint that was created.

EndpointIdentifier (string) --
The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can\'t end with a hyphen or contain two consecutive hyphens.

EndpointType (string) --
The type of endpoint. Valid values are source and target .

EngineName (string) --
The database engine name. Valid values, depending on the EndpointType, include "mysql" , "oracle" , "postgres" , "mariadb" , "aurora" , "aurora-postgresql" , "redshift" , "s3" , "db2" , "azuredb" , "sybase" , "dynamodb" , "mongodb" , "kinesis" , "kafka" , "elasticsearch" , "documentdb" , and "sqlserver" .

EngineDisplayName (string) --
The expanded name for the engine name. For example, if the EngineName parameter is "aurora," this value would be "Amazon Aurora MySQL."

Username (string) --
The user name used to connect to the endpoint.

ServerName (string) --
The name of the server at the endpoint.

Port (integer) --
The port value used to access the endpoint.

DatabaseName (string) --
The name of the database at the endpoint.

ExtraConnectionAttributes (string) --
Additional connection attributes used to connect to the endpoint.

Status (string) --
The status of the endpoint.

KmsKeyId (string) --
An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint.
If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key.
AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.

EndpointArn (string) --
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

CertificateArn (string) --
The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

SslMode (string) --
The SSL mode used to connect to the endpoint. The default value is none .

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) used by the service access IAM role.

ExternalTableDefinition (string) --
The external table definition.

ExternalId (string) --
Value returned by a call to CreateEndpoint that can be used for cross-account validation. Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

DynamoDbSettings (dict) --
The settings for the target DynamoDB database. For more information, see the DynamoDBSettings structure.

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) used by the service access IAM role.



S3Settings (dict) --
The settings for the S3 target endpoint. For more information, see the S3Settings structure.

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) used by the service access IAM role.

ExternalTableDefinition (string) --
The external table definition.

CsvRowDelimiter (string) --
The delimiter used to separate rows in the source files. The default is a carriage return (\
 ).

CsvDelimiter (string) --
The delimiter used to separate columns in the source files. The default is a comma.

BucketFolder (string) --
An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in the path `` bucketFolder /schema_name /table_name /`` . If this parameter isn\'t specified, then the path used is `` schema_name /table_name /`` .

BucketName (string) --
The name of the S3 bucket.

CompressionType (string) --
An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the target files. Either set this parameter to NONE (the default) or don\'t use it to leave the files uncompressed. This parameter applies to both .csv and .parquet file formats.

EncryptionMode (string) --
The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either SSE_S3 (the default) or SSE_KMS . To use SSE_S3 , you need an AWS Identity and Access Management (IAM) role with permission to allow "arn:aws:s3:::dms-*" to use the following actions:

s3:CreateBucket
s3:ListBucket
s3:DeleteBucket
s3:GetBucketLocation
s3:GetObject
s3:PutObject
s3:DeleteObject
s3:GetObjectVersion
s3:GetBucketPolicy
s3:PutBucketPolicy
s3:DeleteBucketPolicy


ServerSideEncryptionKmsKeyId (string) --
If you are using SSE_KMS for the EncryptionMode , provide the AWS KMS key ID. The key that you use needs an attached policy that enables AWS Identity and Access Management (IAM) user permissions and allows use of the key.
Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier value --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value* ,BucketFolder=*value* ,BucketName=*value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

DataFormat (string) --
The format of the data that you want to use for output. You can choose one of the following:

csv : This is a row-based file format with comma-separated values (.csv).
parquet : Apache Parquet (.parquet) is a columnar storage file format that features efficient compression and provides faster query response.


EncodingType (string) --
The type of encoding you are using:

RLE_DICTIONARY uses a combination of bit-packing and run-length encoding to store repeated values more efficiently. This is the default.
PLAIN doesn\'t use encoding at all. Values are stored as they are.
PLAIN_DICTIONARY builds a dictionary of the values encountered in a given column. The dictionary is stored in a dictionary page for each column chunk.


DictPageSizeLimit (integer) --
The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds this, this column is stored using an encoding type of PLAIN . This parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to PLAIN encoding. This size is used for .parquet file format only.

RowGroupLength (integer) --
The number of rows in a row group. A smaller row group size provides faster reads. But as the number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows. This number is used for .parquet file format only.
If you choose a value larger than the maximum, RowGroupLength is set to the max row group length in bytes (64 * 1024 * 1024).

DataPageSize (integer) --
The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This number is used for .parquet file format only.

ParquetVersion (string) --
The version of the Apache Parquet format that you want to use: parquet_1_0 (the default) or parquet_2_0 .

EnableStatistics (boolean) --
A value that enables statistics for Parquet pages and row groups. Choose true to enable statistics, false to disable. Statistics include NULL , DISTINCT , MAX , and MIN values. This parameter defaults to true . This value is used for .parquet file format only.

IncludeOpForFullLoad (boolean) --
A value that enables a full load to write INSERT operations to the comma-separated value (.csv) output files only to indicate how the rows were added to the source database.

Note
AWS DMS supports the IncludeOpForFullLoad parameter in versions 3.1.4 and later.

For full load, records can only be inserted. By default (the false setting), no information is recorded in these output files for a full load to indicate that the rows were inserted at the source database. If IncludeOpForFullLoad is set to true or y , the INSERT is recorded as an I annotation in the first field of the .csv file. This allows the format of your target records from a full load to be consistent with the target records from a CDC load.

Note
This setting works together with the CdcInsertsOnly and the CdcInsertsAndUpdates parameters for output to .csv files only. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .


CdcInsertsOnly (boolean) --
A value that enables a change data capture (CDC) load to write only INSERT operations to .csv or columnar storage (.parquet) output files. By default (the false setting), the first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated, or deleted at the source database for a CDC load to the target.
If CdcInsertsOnly is set to true or y , only INSERTs from the source database are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded depends on the value of IncludeOpForFullLoad . If IncludeOpForFullLoad is set to true , the first field of every CDC record is set to I to indicate the INSERT operation at the source. If IncludeOpForFullLoad is set to false , every CDC record is written without a first field to indicate the INSERT operation at the source. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .

Note
AWS DMS supports the interaction described preceding between the CdcInsertsOnly and IncludeOpForFullLoad parameters in versions 3.1.4 and later.

CdcInsertsOnly and CdcInsertsAndUpdates can\'t both be set to true for the same endpoint. Set either CdcInsertsOnly or CdcInsertsAndUpdates to true for the same endpoint, but not both.



TimestampColumnName (string) --
A value that when nonblank causes AWS DMS to add a column with timestamp information to the endpoint data for an Amazon S3 target.

Note
AWS DMS supports the TimestampColumnName parameter in versions 3.1.4 and later.

DMS includes an additional STRING column in the .csv or .parquet object files of your migrated data when you set TimestampColumnName to a nonblank value.
For a full load, each row of this timestamp column contains a timestamp for when the data was transferred from the source to the target by DMS.
For a change data capture (CDC) load, each row of the timestamp column contains the timestamp for the commit of that row in the source database.
The string format for this timestamp column value is yyyy-MM-dd HH:mm:ss.SSSSSS . By default, the precision of this value is in microseconds. For a CDC load, the rounding of the precision depends on the commit timestamp supported by DMS for the source database.
When the AddColumnName parameter is set to true , DMS also includes a name for the timestamp column that you set with TimestampColumnName .

ParquetTimestampInMillisecond (boolean) --
A value that specifies the precision of any TIMESTAMP column values that are written to an Amazon S3 object file in .parquet format.

Note
AWS DMS supports the ParquetTimestampInMillisecond parameter in versions 3.1.4 and later.

When ParquetTimestampInMillisecond is set to true or y , AWS DMS writes all TIMESTAMP columns in a .parquet formatted file with millisecond precision. Otherwise, DMS writes them with microsecond precision.
Currently, Amazon Athena and AWS Glue can handle only millisecond precision for TIMESTAMP values. Set this parameter to true for S3 endpoint object files that are .parquet formatted only if you plan to query or process the data with Athena or AWS Glue.

Note
AWS DMS writes any TIMESTAMP column values written to an S3 file in .csv format with microsecond precision.
Setting ParquetTimestampInMillisecond has no effect on the string format of the timestamp column value that is inserted by setting the TimestampColumnName parameter.


CdcInsertsAndUpdates (boolean) --
A value that enables a change data capture (CDC) load to write INSERT and UPDATE operations to .csv or .parquet (columnar storage) output files. The default setting is false , but when CdcInsertsAndUpdates is set to true or y , INSERTs and UPDATEs from the source database are migrated to the .csv or .parquet file.
For .csv file format only, how these INSERTs and UPDATEs are recorded depends on the value of the IncludeOpForFullLoad parameter. If IncludeOpForFullLoad is set to true , the first field of every CDC record is set to either I or U to indicate INSERT and UPDATE operations at the source. But if IncludeOpForFullLoad is set to false , CDC records are written without an indication of INSERT or UPDATE operations at the source. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .

Note
AWS DMS supports the use of the CdcInsertsAndUpdates parameter in versions 3.3.1 and later.

CdcInsertsOnly and CdcInsertsAndUpdates can\'t both be set to true for the same endpoint. Set either CdcInsertsOnly or CdcInsertsAndUpdates to true for the same endpoint, but not both.





DmsTransferSettings (dict) --
The settings in JSON format for the DMS transfer type of source endpoint.
Possible settings include the following:

ServiceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.
BucketName - The name of the S3 bucket to use.
CompressionType - An optional parameter to use GZIP to compress the target files. To use GZIP, set this value to NONE (the default). To keep the files uncompressed, don\'t use this value.

Shorthand syntax for these settings is as follows: ServiceAccessRoleArn=string,BucketName=string,CompressionType=string
JSON syntax for these settings is as follows: { "ServiceAccessRoleArn": "string", "BucketName": "string", "CompressionType": "none"|"gzip" }

ServiceAccessRoleArn (string) --
The IAM role that has permission to access the Amazon S3 bucket.

BucketName (string) --
The name of the S3 bucket to use.



MongoDbSettings (dict) --
The settings for the MongoDB source endpoint. For more information, see the MongoDbSettings structure.

Username (string) --
The user name you use to access the MongoDB source endpoint.

Password (string) --
The password for the user account you use to access the MongoDB source endpoint.

ServerName (string) --
The name of the server on the MongoDB source endpoint.

Port (integer) --
The port value for the MongoDB source endpoint.

DatabaseName (string) --
The database name on the MongoDB source endpoint.

AuthType (string) --
The authentication type you use to access the MongoDB source endpoint.
Valid values: NO, PASSWORD
When NO is selected, user name and password parameters are not used and can be empty.

AuthMechanism (string) --
The authentication mechanism you use to access the MongoDB source endpoint.
Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1
DEFAULT \xe2\x80\x93 For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use SCRAM_SHA_1. This setting isn\'t used when authType=No.

NestingLevel (string) --
Specifies either document or table mode.
Valid values: NONE, ONE
Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

ExtractDocId (string) --
Specifies the document ID. Use this setting when NestingLevel is set to NONE.
Default value is false.

DocsToInvestigate (string) --
Indicates the number of documents to preview to determine the document organization. Use this setting when NestingLevel is set to ONE.
Must be a positive value greater than 0. Default value is 1000.

AuthSource (string) --
The MongoDB database name. This setting isn\'t used when authType=NO .
The default is admin.

KmsKeyId (string) --
The AWS KMS key identifier that is used to encrypt the content on the replication instance. If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.



KinesisSettings (dict) --
The settings for the Amazon Kinesis target endpoint. For more information, see the KinesisSettings structure.

StreamArn (string) --
The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

MessageFormat (string) --
The output format for the records created on the endpoint. The message format is JSON (default) or JSON_UNFORMATTED (a single line with no tab).

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) for the AWS Identity and Access Management (IAM) role that AWS DMS uses to write to the Kinesis data stream.

IncludeTransactionDetails (boolean) --
Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for transaction_id , previous transaction_id , and transaction_record_id (the record offset within a transaction). The default is False .

IncludePartitionValue (boolean) --
Shows the partition value within the Kinesis message output, unless the partition type is schema-table-type . The default is False .

PartitionIncludeSchemaTable (boolean) --
Prefixes schema and table names to partition values, when the partition type is primary-key-type . Doing this increases data distribution among Kinesis shards. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same shard, which causes throttling. The default is False .

IncludeTableAlterOperations (boolean) --
Includes any data definition language (DDL) operations that change the table in the control data, such as rename-table , drop-table , add-column , drop-column , and rename-column . The default is False .

IncludeControlDetails (boolean) --
Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output. The default is False .



KafkaSettings (dict) --
The settings for the Apache Kafka target endpoint. For more information, see the KafkaSettings structure.

Broker (string) --
The broker location and port of the Kafka broker that hosts your Kafka instance. Specify the broker in the form `` broker-hostname-or-ip :port `` . For example, "ec2-12-345-678-901.compute-1.amazonaws.com:2345" .

Topic (string) --
The topic to which you migrate the data. If you don\'t specify a topic, AWS DMS specifies "kafka-default-topic" as the migration topic.



ElasticsearchSettings (dict) --
The settings for the Elasticsearch source endpoint. For more information, see the ElasticsearchSettings structure.

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) used by service to access the IAM role.

EndpointUri (string) --
The endpoint for the Elasticsearch cluster.

FullLoadErrorPercentage (integer) --
The maximum percentage of records that can fail to be written before a full load operation stops.

ErrorRetryDuration (integer) --
The maximum number of seconds for which DMS retries failed API requests to the Elasticsearch cluster.



NeptuneSettings (dict) --
The settings for the MongoDB source endpoint. For more information, see the NeptuneSettings structure.

ServiceAccessRoleArn (string) --
The ARN of the service role you have created for the Neptune target endpoint. For more information, see https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.ServiceRole in the AWS Database Migration Service User Guide.

S3BucketName (string) --
The name of the S3 bucket for AWS DMS to temporarily store migrated graph data in CSV files before bulk-loading it to the Neptune target database. AWS DMS maps the SQL source data to graph data before storing it in these CSV files.

S3BucketFolder (string) --
A folder path where you where you want AWS DMS to store migrated graph data in the S3 bucket specified by S3BucketName

ErrorRetryDuration (integer) --
The number of milliseconds for AWS DMS to wait to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 250.

MaxFileSize (integer) --
The maximum size in KB of migrated graph data stored in a CSV file before AWS DMS bulk-loads the data to the Neptune target database. The default is 1048576 KB. If successful, AWS DMS clears the bucket, ready to store the next batch of migrated graph data.

MaxRetryCount (integer) --
The number of times for AWS DMS to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 5.

IamAuthEnabled (boolean) --
If you want IAM authorization enabled for this endpoint, set this parameter to true and attach the appropriate role policy document to your service role specified by ServiceAccessRoleArn . The default is false .



RedshiftSettings (dict) --
Settings for the Amazon Redshift endpoint.

AcceptAnyDate (boolean) --
A value that indicates to allow any date format, including invalid formats such as 00/00/00 00:00:00, to be loaded without generating an error. You can choose true or false (the default).
This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data doesn\'t match the DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

AfterConnectScript (string) --
Code to run after connecting. This parameter should contain the code itself, not the name of a file containing the code.

BucketFolder (string) --
The location where the comma-separated value (.csv) files are stored before being uploaded to the S3 bucket.

BucketName (string) --
The name of the S3 bucket you want to use

ConnectionTimeout (integer) --
A value that sets the amount of time to wait (in milliseconds) before timing out, beginning from when you initially establish a connection.

DatabaseName (string) --
The name of the Amazon Redshift data warehouse (service) that you are working with.

DateFormat (string) --
The date format that you are using. Valid values are auto (case-sensitive), your date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults to a format of \'YYYY-MM-DD\'. Using auto recognizes most strings, even some that aren\'t supported when you use a date format string.
If your date and time values use formats different from each other, set this to auto .

EmptyAsNull (boolean) --
A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL. A value of true sets empty CHAR and VARCHAR fields to null. The default is false .

EncryptionMode (string) --
The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either SSE_S3 (the default) or SSE_KMS . To use SSE_S3 , create an AWS Identity and Access Management (IAM) role with a policy that allows "arn:aws:s3:::*" to use the following actions: "s3:PutObject", "s3:ListBucket"

FileTransferUploadStreams (integer) --
The number of threads used to upload a single file. This parameter accepts a value from 1 through 64. It defaults to 10.

LoadTimeout (integer) --
The amount of time to wait (in milliseconds) before timing out, beginning from when you begin loading.

MaxFileSize (integer) --
The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

Password (string) --
The password for the user named in the username property.

Port (integer) --
The port number for Amazon Redshift. The default value is 5439.

RemoveQuotes (boolean) --
A value that specifies to remove surrounding quotation marks from strings in the incoming data. All characters within the quotation marks, including delimiters, are retained. Choose true to remove quotation marks. The default is false .

ReplaceInvalidChars (string) --
A list of characters that you want to replace. Use with ReplaceChars .

ReplaceChars (string) --
A value that specifies to replaces the invalid characters specified in ReplaceInvalidChars , substituting the specified characters instead. The default is "?" .

ServerName (string) --
The name of the Amazon Redshift cluster you are using.

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service.

ServerSideEncryptionKmsKeyId (string) --
The AWS KMS key ID. If you are using SSE_KMS for the EncryptionMode , provide this key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.

TimeFormat (string) --
The time format that you want to use. Valid values are auto (case-sensitive), \'timeformat_string\' , \'epochsecs\' , or \'epochmillisecs\' . It defaults to 10. Using auto recognizes most strings, even some that aren\'t supported when you use a time format string.
If your date and time values use formats different from each other, set this parameter to auto .

TrimBlanks (boolean) --
A value that specifies to remove the trailing white space characters from a VARCHAR string. This parameter applies only to columns with a VARCHAR data type. Choose true to remove unneeded white space. The default is false .

TruncateColumns (boolean) --
A value that specifies to truncate data in columns to the appropriate number of characters, so that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose true to truncate data. The default is false .

Username (string) --
An Amazon Redshift user name for a registered user.

WriteBufferSize (integer) --
The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The default is 1,024. Use this setting to tune performance.











Exceptions

DatabaseMigrationService.Client.exceptions.KMSKeyNotAccessibleFault
DatabaseMigrationService.Client.exceptions.ResourceAlreadyExistsFault
DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.AccessDeniedFault

Examples
Creates an endpoint using the provided settings.
response = client.create_endpoint(
    CertificateArn='',
    DatabaseName='testdb',
    EndpointIdentifier='test-endpoint-1',
    EndpointType='source',
    EngineName='mysql',
    ExtraConnectionAttributes='',
    KmsKeyId='arn:aws:kms:us-east-1:123456789012:key/4c1731d6-5435-ed4d-be13-d53411a7cfbd',
    Password='pasword',
    Port=3306,
    ServerName='mydb.cx1llnox7iyx.us-west-2.rds.amazonaws.com',
    SslMode='require',
    Tags=[
        {
            'Key': 'Acount',
            'Value': '143327655',
        },
    ],
    Username='username',
)

print(response)


Expected Output:
{
    'Endpoint': {
        'EndpointArn': 'arn:aws:dms:us-east-1:123456789012:endpoint:RAAR3R22XSH46S3PWLC3NJAWKM',
        'EndpointIdentifier': 'test-endpoint-1',
        'EndpointType': 'source',
        'EngineName': 'mysql',
        'KmsKeyId': 'arn:aws:kms:us-east-1:123456789012:key/4c1731d6-5435-ed4d-be13-d53411a7cfbd',
        'Port': 3306,
        'ServerName': 'mydb.cx1llnox7iyx.us-west-2.rds.amazonaws.com',
        'Status': 'active',
        'Username': 'username',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Endpoint': {
            'EndpointIdentifier': 'string',
            'EndpointType': 'source'|'target',
            'EngineName': 'string',
            'EngineDisplayName': 'string',
            'Username': 'string',
            'ServerName': 'string',
            'Port': 123,
            'DatabaseName': 'string',
            'ExtraConnectionAttributes': 'string',
            'Status': 'string',
            'KmsKeyId': 'string',
            'EndpointArn': 'string',
            'CertificateArn': 'string',
            'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
            'ServiceAccessRoleArn': 'string',
            'ExternalTableDefinition': 'string',
            'ExternalId': 'string',
            'DynamoDbSettings': {
                'ServiceAccessRoleArn': 'string'
            },
            'S3Settings': {
                'ServiceAccessRoleArn': 'string',
                'ExternalTableDefinition': 'string',
                'CsvRowDelimiter': 'string',
                'CsvDelimiter': 'string',
                'BucketFolder': 'string',
                'BucketName': 'string',
                'CompressionType': 'none'|'gzip',
                'EncryptionMode': 'sse-s3'|'sse-kms',
                'ServerSideEncryptionKmsKeyId': 'string',
                'DataFormat': 'csv'|'parquet',
                'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
                'DictPageSizeLimit': 123,
                'RowGroupLength': 123,
                'DataPageSize': 123,
                'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
                'EnableStatistics': True|False,
                'IncludeOpForFullLoad': True|False,
                'CdcInsertsOnly': True|False,
                'TimestampColumnName': 'string',
                'ParquetTimestampInMillisecond': True|False,
                'CdcInsertsAndUpdates': True|False
            },
            'DmsTransferSettings': {
                'ServiceAccessRoleArn': 'string',
                'BucketName': 'string'
            },
            'MongoDbSettings': {
                'Username': 'string',
                'Password': 'string',
                'ServerName': 'string',
                'Port': 123,
                'DatabaseName': 'string',
                'AuthType': 'no'|'password',
                'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                'NestingLevel': 'none'|'one',
                'ExtractDocId': 'string',
                'DocsToInvestigate': 'string',
                'AuthSource': 'string',
                'KmsKeyId': 'string'
            },
            'KinesisSettings': {
                'StreamArn': 'string',
                'MessageFormat': 'json'|'json-unformatted',
                'ServiceAccessRoleArn': 'string',
                'IncludeTransactionDetails': True|False,
                'IncludePartitionValue': True|False,
                'PartitionIncludeSchemaTable': True|False,
                'IncludeTableAlterOperations': True|False,
                'IncludeControlDetails': True|False
            },
            'KafkaSettings': {
                'Broker': 'string',
                'Topic': 'string'
            },
            'ElasticsearchSettings': {
                'ServiceAccessRoleArn': 'string',
                'EndpointUri': 'string',
                'FullLoadErrorPercentage': 123,
                'ErrorRetryDuration': 123
            },
            'NeptuneSettings': {
                'ServiceAccessRoleArn': 'string',
                'S3BucketName': 'string',
                'S3BucketFolder': 'string',
                'ErrorRetryDuration': 123,
                'MaxFileSize': 123,
                'MaxRetryCount': 123,
                'IamAuthEnabled': True|False
            },
            'RedshiftSettings': {
                'AcceptAnyDate': True|False,
                'AfterConnectScript': 'string',
                'BucketFolder': 'string',
                'BucketName': 'string',
                'ConnectionTimeout': 123,
                'DatabaseName': 'string',
                'DateFormat': 'string',
                'EmptyAsNull': True|False,
                'EncryptionMode': 'sse-s3'|'sse-kms',
                'FileTransferUploadStreams': 123,
                'LoadTimeout': 123,
                'MaxFileSize': 123,
                'Password': 'string',
                'Port': 123,
                'RemoveQuotes': True|False,
                'ReplaceInvalidChars': 'string',
                'ReplaceChars': 'string',
                'ServerName': 'string',
                'ServiceAccessRoleArn': 'string',
                'ServerSideEncryptionKmsKeyId': 'string',
                'TimeFormat': 'string',
                'TrimBlanks': True|False,
                'TruncateColumns': True|False,
                'Username': 'string',
                'WriteBufferSize': 123
            }
        }
    }
    
    
    :returns: 
    s3:CreateBucket
    s3:ListBucket
    s3:DeleteBucket
    s3:GetBucketLocation
    s3:GetObject
    s3:PutObject
    s3:DeleteObject
    s3:GetObjectVersion
    s3:GetBucketPolicy
    s3:PutBucketPolicy
    s3:DeleteBucketPolicy
    
    """
    pass

def create_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, EventCategories=None, SourceIds=None, Enabled=None, Tags=None):
    """
    Creates an AWS DMS event notification subscription.
    You can specify the type of source (SourceType ) you want to be notified of, provide a list of AWS DMS source IDs (SourceIds ) that triggers the events, and provide a list of event categories (EventCategories ) for events you want to be notified of. If you specify both the SourceType and SourceIds , such as SourceType = replication-instance and SourceIdentifier = my-replinstance , you will be notified of all the replication instance events for the specified source. If you specify a SourceType but don\'t specify a SourceIdentifier , you receive notice of the events for that source type for all your AWS DMS sources. If you don\'t specify either SourceType nor SourceIdentifier , you will be notified of events generated from all AWS DMS sources belonging to your customer account.
    For more information about AWS DMS events, see Working with Events and Notifications in the AWS Database Migration Service User Guide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_event_subscription(
        SubscriptionName='string',
        SnsTopicArn='string',
        SourceType='string',
        EventCategories=[
            'string',
        ],
        SourceIds=[
            'string',
        ],
        Enabled=True|False,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]\nThe name of the AWS DMS event notification subscription. This name must be less than 255 characters.\n

    :type SnsTopicArn: string
    :param SnsTopicArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.\n

    :type SourceType: string
    :param SourceType: The type of AWS DMS resource that generates the events. For example, if you want to be notified of events generated by a replication instance, you set this parameter to replication-instance . If this value isn\'t specified, all events are returned.\nValid values: replication-instance | replication-task\n

    :type EventCategories: list
    :param EventCategories: A list of event categories for a source type that you want to subscribe to. For more information, see Working with Events and Notifications in the AWS Database Migration Service User Guide.\n\n(string) --\n\n

    :type SourceIds: list
    :param SourceIds: A list of identifiers for which AWS DMS provides notification events.\nIf you don\'t specify a value, notifications are provided for all sources.\nIf you specify multiple values, they must be of the same type. For example, if you specify a database instance ID, then all of the other values must be database instance IDs.\n\n(string) --\n\n

    :type Enabled: boolean
    :param Enabled: A Boolean value; set to true to activate the subscription, or set to false to create the subscription but not activate it.

    :type Tags: list
    :param Tags: One or more tags to be assigned to the event subscription.\n\n(dict) --A user-defined key-value pair that describes metadata added to an AWS DMS resource and that is used by operations such as the following:\n\nAddTagsToResource\nListTagsForResource\nRemoveTagsFromResource\n\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EventSubscription': {
        'CustomerAwsId': 'string',
        'CustSubscriptionId': 'string',
        'SnsTopicArn': 'string',
        'Status': 'string',
        'SubscriptionCreationTime': 'string',
        'SourceType': 'string',
        'SourceIdsList': [
            'string',
        ],
        'EventCategoriesList': [
            'string',
        ],
        'Enabled': True|False
    }
}


Response Structure

(dict) --

EventSubscription (dict) --
The event subscription that was created.

CustomerAwsId (string) --
The AWS customer account associated with the AWS DMS event notification subscription.

CustSubscriptionId (string) --
The AWS DMS event notification subscription Id.

SnsTopicArn (string) --
The topic ARN of the AWS DMS event notification subscription.

Status (string) --
The status of the AWS DMS event notification subscription.
Constraints:
Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
The status "no-permission" indicates that AWS DMS no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.

SubscriptionCreationTime (string) --
The time the RDS event notification subscription was created.

SourceType (string) --
The type of AWS DMS resource that generates events.
Valid values: replication-instance | replication-server | security-group | replication-task

SourceIdsList (list) --
A list of source Ids for the event subscription.

(string) --


EventCategoriesList (list) --
A lists of event categories.

(string) --


Enabled (boolean) --
Boolean value that indicates if the event subscription is enabled.









Exceptions

DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.ResourceAlreadyExistsFault
DatabaseMigrationService.Client.exceptions.SNSInvalidTopicFault
DatabaseMigrationService.Client.exceptions.SNSNoAuthorizationFault
DatabaseMigrationService.Client.exceptions.KMSAccessDeniedFault
DatabaseMigrationService.Client.exceptions.KMSDisabledFault
DatabaseMigrationService.Client.exceptions.KMSInvalidStateFault
DatabaseMigrationService.Client.exceptions.KMSNotFoundFault
DatabaseMigrationService.Client.exceptions.KMSThrottlingFault


    :return: {
        'EventSubscription': {
            'CustomerAwsId': 'string',
            'CustSubscriptionId': 'string',
            'SnsTopicArn': 'string',
            'Status': 'string',
            'SubscriptionCreationTime': 'string',
            'SourceType': 'string',
            'SourceIdsList': [
                'string',
            ],
            'EventCategoriesList': [
                'string',
            ],
            'Enabled': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_replication_instance(ReplicationInstanceIdentifier=None, AllocatedStorage=None, ReplicationInstanceClass=None, VpcSecurityGroupIds=None, AvailabilityZone=None, ReplicationSubnetGroupIdentifier=None, PreferredMaintenanceWindow=None, MultiAZ=None, EngineVersion=None, AutoMinorVersionUpgrade=None, Tags=None, KmsKeyId=None, PubliclyAccessible=None, DnsNameServers=None):
    """
    Creates the replication instance using the specified parameters.
    AWS DMS requires that your account have certain roles with appropriate permissions before you can create a replication instance. For information on the required roles, see Creating the IAM Roles to Use With the AWS CLI and AWS DMS API . For information on the required permissions, see IAM Permissions Needed to Use AWS DMS .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates the replication instance using the specified parameters.
    Expected Output:
    
    :example: response = client.create_replication_instance(
        ReplicationInstanceIdentifier='string',
        AllocatedStorage=123,
        ReplicationInstanceClass='string',
        VpcSecurityGroupIds=[
            'string',
        ],
        AvailabilityZone='string',
        ReplicationSubnetGroupIdentifier='string',
        PreferredMaintenanceWindow='string',
        MultiAZ=True|False,
        EngineVersion='string',
        AutoMinorVersionUpgrade=True|False,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        KmsKeyId='string',
        PubliclyAccessible=True|False,
        DnsNameServers='string'
    )
    
    
    :type ReplicationInstanceIdentifier: string
    :param ReplicationInstanceIdentifier: [REQUIRED]\nThe replication instance identifier. This parameter is stored as a lowercase string.\nConstraints:\n\nMust contain from 1 to 63 alphanumeric characters or hyphens.\nFirst character must be a letter.\nCan\'t end with a hyphen or contain two consecutive hyphens.\n\nExample: myrepinstance\n

    :type AllocatedStorage: integer
    :param AllocatedStorage: The amount of storage (in gigabytes) to be initially allocated for the replication instance.

    :type ReplicationInstanceClass: string
    :param ReplicationInstanceClass: [REQUIRED]\nThe compute and memory capacity of the replication instance as specified by the replication instance class.\nValid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge\n

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance.\n\n(string) --\n\n

    :type AvailabilityZone: string
    :param AvailabilityZone: The Availability Zone where the replication instance will be created. The default value is a random, system-chosen Availability Zone in the endpoint\'s AWS Region, for example: us-east-1d

    :type ReplicationSubnetGroupIdentifier: string
    :param ReplicationSubnetGroupIdentifier: A subnet group to associate with the replication instance.

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).\nFormat: ddd:hh24:mi-ddd:hh24:mi\nDefault: A 30-minute window selected at random from an 8-hour block of time per AWS Region, occurring on a random day of the week.\nValid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun\nConstraints: Minimum 30-minute window.\n

    :type MultiAZ: boolean
    :param MultiAZ: Specifies whether the replication instance is a Multi-AZ deployment. You can\'t set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .

    :type EngineVersion: string
    :param EngineVersion: The engine version number of the replication instance.

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: A value that indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window. This parameter defaults to true .\nDefault: true\n

    :type Tags: list
    :param Tags: One or more tags to be assigned to the replication instance.\n\n(dict) --A user-defined key-value pair that describes metadata added to an AWS DMS resource and that is used by operations such as the following:\n\nAddTagsToResource\nListTagsForResource\nRemoveTagsFromResource\n\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :type KmsKeyId: string
    :param KmsKeyId: An AWS KMS key identifier that is used to encrypt the data on the replication instance.\nIf you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key.\nAWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.\n

    :type PubliclyAccessible: boolean
    :param PubliclyAccessible: Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address. The default value is true .

    :type DnsNameServers: string
    :param DnsNameServers: A list of DNS name servers supported for the replication instance.

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationInstance': {
        'ReplicationInstanceIdentifier': 'string',
        'ReplicationInstanceClass': 'string',
        'ReplicationInstanceStatus': 'string',
        'AllocatedStorage': 123,
        'InstanceCreateTime': datetime(2015, 1, 1),
        'VpcSecurityGroups': [
            {
                'VpcSecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'AvailabilityZone': 'string',
        'ReplicationSubnetGroup': {
            'ReplicationSubnetGroupIdentifier': 'string',
            'ReplicationSubnetGroupDescription': 'string',
            'VpcId': 'string',
            'SubnetGroupStatus': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': {
                        'Name': 'string'
                    },
                    'SubnetStatus': 'string'
                },
            ]
        },
        'PreferredMaintenanceWindow': 'string',
        'PendingModifiedValues': {
            'ReplicationInstanceClass': 'string',
            'AllocatedStorage': 123,
            'MultiAZ': True|False,
            'EngineVersion': 'string'
        },
        'MultiAZ': True|False,
        'EngineVersion': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'KmsKeyId': 'string',
        'ReplicationInstanceArn': 'string',
        'ReplicationInstancePublicIpAddress': 'string',
        'ReplicationInstancePrivateIpAddress': 'string',
        'ReplicationInstancePublicIpAddresses': [
            'string',
        ],
        'ReplicationInstancePrivateIpAddresses': [
            'string',
        ],
        'PubliclyAccessible': True|False,
        'SecondaryAvailabilityZone': 'string',
        'FreeUntil': datetime(2015, 1, 1),
        'DnsNameServers': 'string'
    }
}


Response Structure

(dict) --

ReplicationInstance (dict) --
The replication instance that was created.

ReplicationInstanceIdentifier (string) --
The replication instance identifier. This parameter is stored as a lowercase string.
Constraints:

Must contain from 1 to 63 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.

Example: myrepinstance

ReplicationInstanceClass (string) --
The compute and memory capacity of the replication instance.
Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge

ReplicationInstanceStatus (string) --
The status of the replication instance.

AllocatedStorage (integer) --
The amount of storage (in gigabytes) that is allocated for the replication instance.

InstanceCreateTime (datetime) --
The time the replication instance was created.

VpcSecurityGroups (list) --
The VPC security group for the instance.

(dict) --
Describes status of a security group associated with the virtual private cloud hosting your replication and DB instances.

VpcSecurityGroupId (string) --
The VPC security group Id.

Status (string) --
The status of the VPC security group.





AvailabilityZone (string) --
The Availability Zone for the instance.

ReplicationSubnetGroup (dict) --
The subnet group for the replication instance.

ReplicationSubnetGroupIdentifier (string) --
The identifier of the replication instance subnet group.

ReplicationSubnetGroupDescription (string) --
A description for the replication subnet group.

VpcId (string) --
The ID of the VPC.

SubnetGroupStatus (string) --
The status of the subnet group.

Subnets (list) --
The subnets that are in the subnet group.

(dict) --
In response to a request by the DescribeReplicationSubnetGroup operation, this object identifies a subnet by its given Availability Zone, subnet identifier, and status.

SubnetIdentifier (string) --
The subnet identifier.

SubnetAvailabilityZone (dict) --
The Availability Zone of the subnet.

Name (string) --
The name of the Availability Zone.



SubnetStatus (string) --
The status of the subnet.







PreferredMaintenanceWindow (string) --
The maintenance window times for the replication instance.

PendingModifiedValues (dict) --
The pending modification values.

ReplicationInstanceClass (string) --
The compute and memory capacity of the replication instance.
Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge

AllocatedStorage (integer) --
The amount of storage (in gigabytes) that is allocated for the replication instance.

MultiAZ (boolean) --
Specifies whether the replication instance is a Multi-AZ deployment. You can\'t set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .

EngineVersion (string) --
The engine version number of the replication instance.



MultiAZ (boolean) --
Specifies whether the replication instance is a Multi-AZ deployment. You can\'t set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .

EngineVersion (string) --
The engine version number of the replication instance.

AutoMinorVersionUpgrade (boolean) --
Boolean value indicating if minor version upgrades will be automatically applied to the instance.

KmsKeyId (string) --
An AWS KMS key identifier that is used to encrypt the data on the replication instance.
If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key.
AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.

ReplicationInstanceArn (string) --
The Amazon Resource Name (ARN) of the replication instance.

ReplicationInstancePublicIpAddress (string) --
The public IP address of the replication instance.

ReplicationInstancePrivateIpAddress (string) --
The private IP address of the replication instance.

ReplicationInstancePublicIpAddresses (list) --
One or more public IP addresses for the replication instance.

(string) --


ReplicationInstancePrivateIpAddresses (list) --
One or more private IP addresses for the replication instance.

(string) --


PubliclyAccessible (boolean) --
Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address. The default value is true .

SecondaryAvailabilityZone (string) --
The Availability Zone of the standby replication instance in a Multi-AZ deployment.

FreeUntil (datetime) --
The expiration date of the free replication instance that is part of the Free DMS program.

DnsNameServers (string) --
The DNS name servers for the replication instance.









Exceptions

DatabaseMigrationService.Client.exceptions.AccessDeniedFault
DatabaseMigrationService.Client.exceptions.ResourceAlreadyExistsFault
DatabaseMigrationService.Client.exceptions.InsufficientResourceCapacityFault
DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault
DatabaseMigrationService.Client.exceptions.StorageQuotaExceededFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.ReplicationSubnetGroupDoesNotCoverEnoughAZs
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
DatabaseMigrationService.Client.exceptions.InvalidSubnet
DatabaseMigrationService.Client.exceptions.KMSKeyNotAccessibleFault

Examples
Creates the replication instance using the specified parameters.
response = client.create_replication_instance(
    AllocatedStorage=123,
    AutoMinorVersionUpgrade=True,
    AvailabilityZone='',
    EngineVersion='',
    KmsKeyId='',
    MultiAZ=True,
    PreferredMaintenanceWindow='',
    PubliclyAccessible=True,
    ReplicationInstanceClass='',
    ReplicationInstanceIdentifier='',
    ReplicationSubnetGroupIdentifier='',
    Tags=[
        {
            'Key': 'string',
            'Value': 'string',
        },
    ],
    VpcSecurityGroupIds=[
    ],
)

print(response)


Expected Output:
{
    'ReplicationInstance': {
        'AllocatedStorage': 5,
        'AutoMinorVersionUpgrade': True,
        'EngineVersion': '1.5.0',
        'KmsKeyId': 'arn:aws:kms:us-east-1:123456789012:key/4c1731d6-5435-ed4d-be13-d53411a7cfbd',
        'PendingModifiedValues': {
        },
        'PreferredMaintenanceWindow': 'sun:06:00-sun:14:00',
        'PubliclyAccessible': True,
        'ReplicationInstanceArn': 'arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ',
        'ReplicationInstanceClass': 'dms.t2.micro',
        'ReplicationInstanceIdentifier': 'test-rep-1',
        'ReplicationInstanceStatus': 'creating',
        'ReplicationSubnetGroup': {
            'ReplicationSubnetGroupDescription': 'default',
            'ReplicationSubnetGroupIdentifier': 'default',
            'SubnetGroupStatus': 'Complete',
            'Subnets': [
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1d',
                    },
                    'SubnetIdentifier': 'subnet-f6dd91af',
                    'SubnetStatus': 'Active',
                },
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1b',
                    },
                    'SubnetIdentifier': 'subnet-3605751d',
                    'SubnetStatus': 'Active',
                },
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1c',
                    },
                    'SubnetIdentifier': 'subnet-c2daefb5',
                    'SubnetStatus': 'Active',
                },
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1e',
                    },
                    'SubnetIdentifier': 'subnet-85e90cb8',
                    'SubnetStatus': 'Active',
                },
            ],
            'VpcId': 'vpc-6741a603',
        },
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReplicationInstance': {
            'ReplicationInstanceIdentifier': 'string',
            'ReplicationInstanceClass': 'string',
            'ReplicationInstanceStatus': 'string',
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'ReplicationSubnetGroup': {
                'ReplicationSubnetGroupIdentifier': 'string',
                'ReplicationSubnetGroupDescription': 'string',
                'VpcId': 'string',
                'SubnetGroupStatus': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        },
                        'SubnetStatus': 'string'
                    },
                ]
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'ReplicationInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string'
            },
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'KmsKeyId': 'string',
            'ReplicationInstanceArn': 'string',
            'ReplicationInstancePublicIpAddress': 'string',
            'ReplicationInstancePrivateIpAddress': 'string',
            'ReplicationInstancePublicIpAddresses': [
                'string',
            ],
            'ReplicationInstancePrivateIpAddresses': [
                'string',
            ],
            'PubliclyAccessible': True|False,
            'SecondaryAvailabilityZone': 'string',
            'FreeUntil': datetime(2015, 1, 1),
            'DnsNameServers': 'string'
        }
    }
    
    
    :returns: 
    Must contain from 1 to 63 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def create_replication_subnet_group(ReplicationSubnetGroupIdentifier=None, ReplicationSubnetGroupDescription=None, SubnetIds=None, Tags=None):
    """
    Creates a replication subnet group given a list of the subnet IDs in a VPC.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates a replication subnet group given a list of the subnet IDs in a VPC.
    Expected Output:
    
    :example: response = client.create_replication_subnet_group(
        ReplicationSubnetGroupIdentifier='string',
        ReplicationSubnetGroupDescription='string',
        SubnetIds=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ReplicationSubnetGroupIdentifier: string
    :param ReplicationSubnetGroupIdentifier: [REQUIRED]\nThe name for the replication subnet group. This value is stored as a lowercase string.\nConstraints: Must contain no more than 255 alphanumeric characters, periods, spaces, underscores, or hyphens. Must not be 'default'.\nExample: mySubnetgroup\n

    :type ReplicationSubnetGroupDescription: string
    :param ReplicationSubnetGroupDescription: [REQUIRED]\nThe description for the subnet group.\n

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nOne or more subnet IDs to be assigned to the subnet group.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: One or more tags to be assigned to the subnet group.\n\n(dict) --A user-defined key-value pair that describes metadata added to an AWS DMS resource and that is used by operations such as the following:\n\nAddTagsToResource\nListTagsForResource\nRemoveTagsFromResource\n\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationSubnetGroup': {
        'ReplicationSubnetGroupIdentifier': 'string',
        'ReplicationSubnetGroupDescription': 'string',
        'VpcId': 'string',
        'SubnetGroupStatus': 'string',
        'Subnets': [
            {
                'SubnetIdentifier': 'string',
                'SubnetAvailabilityZone': {
                    'Name': 'string'
                },
                'SubnetStatus': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

ReplicationSubnetGroup (dict) --
The replication subnet group that was created.

ReplicationSubnetGroupIdentifier (string) --
The identifier of the replication instance subnet group.

ReplicationSubnetGroupDescription (string) --
A description for the replication subnet group.

VpcId (string) --
The ID of the VPC.

SubnetGroupStatus (string) --
The status of the subnet group.

Subnets (list) --
The subnets that are in the subnet group.

(dict) --
In response to a request by the DescribeReplicationSubnetGroup operation, this object identifies a subnet by its given Availability Zone, subnet identifier, and status.

SubnetIdentifier (string) --
The subnet identifier.

SubnetAvailabilityZone (dict) --
The Availability Zone of the subnet.

Name (string) --
The name of the Availability Zone.



SubnetStatus (string) --
The status of the subnet.













Exceptions

DatabaseMigrationService.Client.exceptions.AccessDeniedFault
DatabaseMigrationService.Client.exceptions.ResourceAlreadyExistsFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault
DatabaseMigrationService.Client.exceptions.ReplicationSubnetGroupDoesNotCoverEnoughAZs
DatabaseMigrationService.Client.exceptions.InvalidSubnet

Examples
Creates a replication subnet group given a list of the subnet IDs in a VPC.
response = client.create_replication_subnet_group(
    ReplicationSubnetGroupDescription='US West subnet group',
    ReplicationSubnetGroupIdentifier='us-west-2ab-vpc-215ds366',
    SubnetIds=[
        'subnet-e145356n',
        'subnet-58f79200',
    ],
    Tags=[
        {
            'Key': 'Acount',
            'Value': '145235',
        },
    ],
)

print(response)


Expected Output:
{
    'ReplicationSubnetGroup': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReplicationSubnetGroup': {
            'ReplicationSubnetGroupIdentifier': 'string',
            'ReplicationSubnetGroupDescription': 'string',
            'VpcId': 'string',
            'SubnetGroupStatus': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': {
                        'Name': 'string'
                    },
                    'SubnetStatus': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.AccessDeniedFault
    DatabaseMigrationService.Client.exceptions.ResourceAlreadyExistsFault
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault
    DatabaseMigrationService.Client.exceptions.ReplicationSubnetGroupDoesNotCoverEnoughAZs
    DatabaseMigrationService.Client.exceptions.InvalidSubnet
    
    """
    pass

def create_replication_task(ReplicationTaskIdentifier=None, SourceEndpointArn=None, TargetEndpointArn=None, ReplicationInstanceArn=None, MigrationType=None, TableMappings=None, ReplicationTaskSettings=None, CdcStartTime=None, CdcStartPosition=None, CdcStopPosition=None, Tags=None, TaskData=None):
    """
    Creates a replication task using the specified parameters.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates a replication task using the specified parameters.
    Expected Output:
    
    :example: response = client.create_replication_task(
        ReplicationTaskIdentifier='string',
        SourceEndpointArn='string',
        TargetEndpointArn='string',
        ReplicationInstanceArn='string',
        MigrationType='full-load'|'cdc'|'full-load-and-cdc',
        TableMappings='string',
        ReplicationTaskSettings='string',
        CdcStartTime=datetime(2015, 1, 1),
        CdcStartPosition='string',
        CdcStopPosition='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        TaskData='string'
    )
    
    
    :type ReplicationTaskIdentifier: string
    :param ReplicationTaskIdentifier: [REQUIRED]\nAn identifier for the replication task.\nConstraints:\n\nMust contain from 1 to 255 alphanumeric characters or hyphens.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\n

    :type SourceEndpointArn: string
    :param SourceEndpointArn: [REQUIRED]\nAn Amazon Resource Name (ARN) that uniquely identifies the source endpoint.\n

    :type TargetEndpointArn: string
    :param TargetEndpointArn: [REQUIRED]\nAn Amazon Resource Name (ARN) that uniquely identifies the target endpoint.\n

    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of a replication instance.\n

    :type MigrationType: string
    :param MigrationType: [REQUIRED]\nThe migration type. Valid values: full-load | cdc | full-load-and-cdc\n

    :type TableMappings: string
    :param TableMappings: [REQUIRED]\nThe table mappings for the task, in JSON format. For more information, see Using Table Mapping to Specify Task Settings in the AWS Database Migration User Guide.\n

    :type ReplicationTaskSettings: string
    :param ReplicationTaskSettings: Overall settings for the task, in JSON format. For more information, see Specifying Task Settings for AWS Database Migration Service Tasks in the AWS Database Migration User Guide.

    :type CdcStartTime: datetime
    :param CdcStartTime: Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.\nTimestamp Example: --cdc-start-time \xe2\x80\x9c2018-03-08T12:12:12\xe2\x80\x9d\n

    :type CdcStartPosition: string
    :param CdcStartPosition: Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.\nThe value can be in date, checkpoint, or LSN/SCN format.\nDate Example: --cdc-start-position \xe2\x80\x9c2018-03-08T12:12:12\xe2\x80\x9d\nCheckpoint Example: --cdc-start-position 'checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93'\nLSN Example: --cdc-start-position \xe2\x80\x9cmysql-bin-changelog.000024:373\xe2\x80\x9d\n\nNote\nWhen you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the slotName extra connection attribute to the name of this logical replication slot. For more information, see Extra Connection Attributes When Using PostgreSQL as a Source for AWS DMS .\n\n

    :type CdcStopPosition: string
    :param CdcStopPosition: Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.\nServer time example: --cdc-stop-position \xe2\x80\x9cserver_time:3018-02-09T12:12:12\xe2\x80\x9d\nCommit time example: --cdc-stop-position \xe2\x80\x9ccommit_time: 3018-02-09T12:12:12 \xe2\x80\x9c\n

    :type Tags: list
    :param Tags: One or more tags to be assigned to the replication task.\n\n(dict) --A user-defined key-value pair that describes metadata added to an AWS DMS resource and that is used by operations such as the following:\n\nAddTagsToResource\nListTagsForResource\nRemoveTagsFromResource\n\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :type TaskData: string
    :param TaskData: Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see Specifying Supplemental Data for Task Settings in the AWS Database Migration User Guide.

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationTask': {
        'ReplicationTaskIdentifier': 'string',
        'SourceEndpointArn': 'string',
        'TargetEndpointArn': 'string',
        'ReplicationInstanceArn': 'string',
        'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
        'TableMappings': 'string',
        'ReplicationTaskSettings': 'string',
        'Status': 'string',
        'LastFailureMessage': 'string',
        'StopReason': 'string',
        'ReplicationTaskCreationDate': datetime(2015, 1, 1),
        'ReplicationTaskStartDate': datetime(2015, 1, 1),
        'CdcStartPosition': 'string',
        'CdcStopPosition': 'string',
        'RecoveryCheckpoint': 'string',
        'ReplicationTaskArn': 'string',
        'ReplicationTaskStats': {
            'FullLoadProgressPercent': 123,
            'ElapsedTimeMillis': 123,
            'TablesLoaded': 123,
            'TablesLoading': 123,
            'TablesQueued': 123,
            'TablesErrored': 123,
            'FreshStartDate': datetime(2015, 1, 1),
            'StartDate': datetime(2015, 1, 1),
            'StopDate': datetime(2015, 1, 1),
            'FullLoadStartDate': datetime(2015, 1, 1),
            'FullLoadFinishDate': datetime(2015, 1, 1)
        },
        'TaskData': 'string'
    }
}


Response Structure

(dict) --

ReplicationTask (dict) --
The replication task that was created.

ReplicationTaskIdentifier (string) --
The user-assigned replication task identifier or name.
Constraints:

Must contain from 1 to 255 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.


SourceEndpointArn (string) --
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

TargetEndpointArn (string) --
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

ReplicationInstanceArn (string) --
The Amazon Resource Name (ARN) of the replication instance.

MigrationType (string) --
The type of migration.

TableMappings (string) --
Table mappings specified in the task.

ReplicationTaskSettings (string) --
The settings for the replication task.

Status (string) --
The status of the replication task.

LastFailureMessage (string) --
The last error (failure) message generated for the replication instance.

StopReason (string) --
The reason the replication task was stopped.

ReplicationTaskCreationDate (datetime) --
The date the replication task was created.

ReplicationTaskStartDate (datetime) --
The date the replication task is scheduled to start.

CdcStartPosition (string) --
Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want the CDC operation to start. Specifying both values results in an error.
The value can be in date, checkpoint, or LSN/SCN format.
Date Example: --cdc-start-position \xe2\x80\x9c2018-03-08T12:12:12\xe2\x80\x9d
Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
LSN Example: --cdc-start-position \xe2\x80\x9cmysql-bin-changelog.000024:373\xe2\x80\x9d

CdcStopPosition (string) --
Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
Server time example: --cdc-stop-position \xe2\x80\x9cserver_time:3018-02-09T12:12:12\xe2\x80\x9d
Commit time example: --cdc-stop-position \xe2\x80\x9ccommit_time: 3018-02-09T12:12:12 \xe2\x80\x9c

RecoveryCheckpoint (string) --
Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the CdcStartPosition parameter to start a CDC operation that begins at that checkpoint.

ReplicationTaskArn (string) --
The Amazon Resource Name (ARN) of the replication task.

ReplicationTaskStats (dict) --
The statistics for the task, including elapsed time, tables loaded, and table errors.

FullLoadProgressPercent (integer) --
The percent complete for the full load migration task.

ElapsedTimeMillis (integer) --
The elapsed time of the task, in milliseconds.

TablesLoaded (integer) --
The number of tables loaded for this task.

TablesLoading (integer) --
The number of tables currently loading for this task.

TablesQueued (integer) --
The number of tables queued for this task.

TablesErrored (integer) --
The number of errors that have occurred during this task.

FreshStartDate (datetime) --
The date the replication task was started either with a fresh start or a target reload.

StartDate (datetime) --
The date the replication task was started either with a fresh start or a resume. For more information, see StartReplicationTaskType .

StopDate (datetime) --
The date the replication task was stopped.

FullLoadStartDate (datetime) --
The date the replication task full load was started.

FullLoadFinishDate (datetime) --
The date the replication task full load was completed.



TaskData (string) --
Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see Specifying Supplemental Data for Task Settings in the AWS Database Migration User Guide.









Exceptions

DatabaseMigrationService.Client.exceptions.AccessDeniedFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
DatabaseMigrationService.Client.exceptions.ResourceAlreadyExistsFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.KMSKeyNotAccessibleFault
DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault

Examples
Creates a replication task using the specified parameters.
response = client.create_replication_task(
    CdcStartTime=datetime(2016, 12, 14, 18, 25, 43, 2, 349, 0),
    MigrationType='full-load',
    ReplicationInstanceArn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ',
    ReplicationTaskIdentifier='task1',
    ReplicationTaskSettings='',
    SourceEndpointArn='arn:aws:dms:us-east-1:123456789012:endpoint:ZW5UAN6P4E77EC7YWHK4RZZ3BE',
    TableMappings='file://mappingfile.json',
    Tags=[
        {
            'Key': 'Acount',
            'Value': '24352226',
        },
    ],
    TargetEndpointArn='arn:aws:dms:us-east-1:123456789012:endpoint:ASXWXJZLNWNT5HTWCGV2BUJQ7E',
)

print(response)


Expected Output:
{
    'ReplicationTask': {
        'MigrationType': 'full-load',
        'ReplicationInstanceArn': 'arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ',
        'ReplicationTaskArn': 'arn:aws:dms:us-east-1:123456789012:task:OEAMB3NXSTZ6LFYZFEPPBBXPYM',
        'ReplicationTaskCreationDate': datetime(2016, 12, 14, 18, 25, 43, 2, 349, 0),
        'ReplicationTaskIdentifier': 'task1',
        'ReplicationTaskSettings': '{"TargetMetadata":{"TargetSchema":"","SupportLobs":true,"FullLobMode":true,"LobChunkSize":64,"LimitedSizeLobMode":false,"LobMaxSize":0},"FullLoadSettings":{"FullLoadEnabled":true,"ApplyChangesEnabled":false,"TargetTablePrepMode":"DROP_AND_CREATE","CreatePkAfterFullLoad":false,"StopTaskCachedChangesApplied":false,"StopTaskCachedChangesNotApplied":false,"ResumeEnabled":false,"ResumeMinTableSize":100000,"ResumeOnlyClusteredPKTables":true,"MaxFullLoadSubTasks":8,"TransactionConsistencyTimeout":600,"CommitRate":10000},"Logging":{"EnableLogging":false}}',
        'SourceEndpointArn': 'arn:aws:dms:us-east-1:123456789012:endpoint:ZW5UAN6P4E77EC7YWHK4RZZ3BE',
        'Status': 'creating',
        'TableMappings': 'file://mappingfile.json',
        'TargetEndpointArn': 'arn:aws:dms:us-east-1:123456789012:endpoint:ASXWXJZLNWNT5HTWCGV2BUJQ7E',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReplicationTask': {
            'ReplicationTaskIdentifier': 'string',
            'SourceEndpointArn': 'string',
            'TargetEndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
            'TableMappings': 'string',
            'ReplicationTaskSettings': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'StopReason': 'string',
            'ReplicationTaskCreationDate': datetime(2015, 1, 1),
            'ReplicationTaskStartDate': datetime(2015, 1, 1),
            'CdcStartPosition': 'string',
            'CdcStopPosition': 'string',
            'RecoveryCheckpoint': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationTaskStats': {
                'FullLoadProgressPercent': 123,
                'ElapsedTimeMillis': 123,
                'TablesLoaded': 123,
                'TablesLoading': 123,
                'TablesQueued': 123,
                'TablesErrored': 123,
                'FreshStartDate': datetime(2015, 1, 1),
                'StartDate': datetime(2015, 1, 1),
                'StopDate': datetime(2015, 1, 1),
                'FullLoadStartDate': datetime(2015, 1, 1),
                'FullLoadFinishDate': datetime(2015, 1, 1)
            },
            'TaskData': 'string'
        }
    }
    
    
    :returns: 
    Must contain from 1 to 255 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def delete_certificate(CertificateArn=None):
    """
    Deletes the specified certificate.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes the specified certificate.
    Expected Output:
    
    :example: response = client.delete_certificate(
        CertificateArn='string'
    )
    
    
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the deleted certificate.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Certificate': {
        'CertificateIdentifier': 'string',
        'CertificateCreationDate': datetime(2015, 1, 1),
        'CertificatePem': 'string',
        'CertificateWallet': b'bytes',
        'CertificateArn': 'string',
        'CertificateOwner': 'string',
        'ValidFromDate': datetime(2015, 1, 1),
        'ValidToDate': datetime(2015, 1, 1),
        'SigningAlgorithm': 'string',
        'KeyLength': 123
    }
}


Response Structure

(dict) --
Certificate (dict) --The Secure Sockets Layer (SSL) certificate.

CertificateIdentifier (string) --A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can\'t end with a hyphen or contain two consecutive hyphens.

CertificateCreationDate (datetime) --The date that the certificate was created.

CertificatePem (string) --The contents of a .pem file, which contains an X.509 certificate.

CertificateWallet (bytes) --The location of an imported Oracle Wallet certificate for use with SSL.

CertificateArn (string) --The Amazon Resource Name (ARN) for the certificate.

CertificateOwner (string) --The owner of the certificate.

ValidFromDate (datetime) --The beginning date that the certificate is valid.

ValidToDate (datetime) --The final date that the certificate is valid.

SigningAlgorithm (string) --The signing algorithm for the certificate.

KeyLength (integer) --The key length of the cryptographic algorithm being used.








Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault

Examples
Deletes the specified certificate.
response = client.delete_certificate(
    CertificateArn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUSM457DE6XFJCJQ',
)

print(response)


Expected Output:
{
    'Certificate': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Certificate': {
            'CertificateIdentifier': 'string',
            'CertificateCreationDate': datetime(2015, 1, 1),
            'CertificatePem': 'string',
            'CertificateWallet': b'bytes',
            'CertificateArn': 'string',
            'CertificateOwner': 'string',
            'ValidFromDate': datetime(2015, 1, 1),
            'ValidToDate': datetime(2015, 1, 1),
            'SigningAlgorithm': 'string',
            'KeyLength': 123
        }
    }
    
    
    """
    pass

def delete_connection(EndpointArn=None, ReplicationInstanceArn=None):
    """
    Deletes the connection between a replication instance and an endpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_connection(
        EndpointArn='string',
        ReplicationInstanceArn='string'
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]\nThe Amazon Resource Name (ARN) string that uniquely identifies the endpoint.\n

    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the replication instance.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Connection': {
        'ReplicationInstanceArn': 'string',
        'EndpointArn': 'string',
        'Status': 'string',
        'LastFailureMessage': 'string',
        'EndpointIdentifier': 'string',
        'ReplicationInstanceIdentifier': 'string'
    }
}


Response Structure

(dict) --

Connection (dict) --
The connection that is being deleted.

ReplicationInstanceArn (string) --
The ARN of the replication instance.

EndpointArn (string) --
The ARN string that uniquely identifies the endpoint.

Status (string) --
The connection status.

LastFailureMessage (string) --
The error message when the connection last failed.

EndpointIdentifier (string) --
The identifier of the endpoint. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can\'t end with a hyphen or contain two consecutive hyphens.

ReplicationInstanceIdentifier (string) --
The replication instance identifier. This parameter is stored as a lowercase string.









Exceptions

DatabaseMigrationService.Client.exceptions.AccessDeniedFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault


    :return: {
        'Connection': {
            'ReplicationInstanceArn': 'string',
            'EndpointArn': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'EndpointIdentifier': 'string',
            'ReplicationInstanceIdentifier': 'string'
        }
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.AccessDeniedFault
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
    
    """
    pass

def delete_endpoint(EndpointArn=None):
    """
    Deletes the specified endpoint.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes the specified endpoint. All tasks associated with the endpoint must be deleted before you can delete the endpoint.
    Expected Output:
    
    :example: response = client.delete_endpoint(
        EndpointArn='string'
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]\nThe Amazon Resource Name (ARN) string that uniquely identifies the endpoint.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Endpoint': {
        'EndpointIdentifier': 'string',
        'EndpointType': 'source'|'target',
        'EngineName': 'string',
        'EngineDisplayName': 'string',
        'Username': 'string',
        'ServerName': 'string',
        'Port': 123,
        'DatabaseName': 'string',
        'ExtraConnectionAttributes': 'string',
        'Status': 'string',
        'KmsKeyId': 'string',
        'EndpointArn': 'string',
        'CertificateArn': 'string',
        'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
        'ServiceAccessRoleArn': 'string',
        'ExternalTableDefinition': 'string',
        'ExternalId': 'string',
        'DynamoDbSettings': {
            'ServiceAccessRoleArn': 'string'
        },
        'S3Settings': {
            'ServiceAccessRoleArn': 'string',
            'ExternalTableDefinition': 'string',
            'CsvRowDelimiter': 'string',
            'CsvDelimiter': 'string',
            'BucketFolder': 'string',
            'BucketName': 'string',
            'CompressionType': 'none'|'gzip',
            'EncryptionMode': 'sse-s3'|'sse-kms',
            'ServerSideEncryptionKmsKeyId': 'string',
            'DataFormat': 'csv'|'parquet',
            'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
            'DictPageSizeLimit': 123,
            'RowGroupLength': 123,
            'DataPageSize': 123,
            'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
            'EnableStatistics': True|False,
            'IncludeOpForFullLoad': True|False,
            'CdcInsertsOnly': True|False,
            'TimestampColumnName': 'string',
            'ParquetTimestampInMillisecond': True|False,
            'CdcInsertsAndUpdates': True|False
        },
        'DmsTransferSettings': {
            'ServiceAccessRoleArn': 'string',
            'BucketName': 'string'
        },
        'MongoDbSettings': {
            'Username': 'string',
            'Password': 'string',
            'ServerName': 'string',
            'Port': 123,
            'DatabaseName': 'string',
            'AuthType': 'no'|'password',
            'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
            'NestingLevel': 'none'|'one',
            'ExtractDocId': 'string',
            'DocsToInvestigate': 'string',
            'AuthSource': 'string',
            'KmsKeyId': 'string'
        },
        'KinesisSettings': {
            'StreamArn': 'string',
            'MessageFormat': 'json'|'json-unformatted',
            'ServiceAccessRoleArn': 'string',
            'IncludeTransactionDetails': True|False,
            'IncludePartitionValue': True|False,
            'PartitionIncludeSchemaTable': True|False,
            'IncludeTableAlterOperations': True|False,
            'IncludeControlDetails': True|False
        },
        'KafkaSettings': {
            'Broker': 'string',
            'Topic': 'string'
        },
        'ElasticsearchSettings': {
            'ServiceAccessRoleArn': 'string',
            'EndpointUri': 'string',
            'FullLoadErrorPercentage': 123,
            'ErrorRetryDuration': 123
        },
        'NeptuneSettings': {
            'ServiceAccessRoleArn': 'string',
            'S3BucketName': 'string',
            'S3BucketFolder': 'string',
            'ErrorRetryDuration': 123,
            'MaxFileSize': 123,
            'MaxRetryCount': 123,
            'IamAuthEnabled': True|False
        },
        'RedshiftSettings': {
            'AcceptAnyDate': True|False,
            'AfterConnectScript': 'string',
            'BucketFolder': 'string',
            'BucketName': 'string',
            'ConnectionTimeout': 123,
            'DatabaseName': 'string',
            'DateFormat': 'string',
            'EmptyAsNull': True|False,
            'EncryptionMode': 'sse-s3'|'sse-kms',
            'FileTransferUploadStreams': 123,
            'LoadTimeout': 123,
            'MaxFileSize': 123,
            'Password': 'string',
            'Port': 123,
            'RemoveQuotes': True|False,
            'ReplaceInvalidChars': 'string',
            'ReplaceChars': 'string',
            'ServerName': 'string',
            'ServiceAccessRoleArn': 'string',
            'ServerSideEncryptionKmsKeyId': 'string',
            'TimeFormat': 'string',
            'TrimBlanks': True|False,
            'TruncateColumns': True|False,
            'Username': 'string',
            'WriteBufferSize': 123
        }
    }
}


Response Structure

(dict) --
Endpoint (dict) --The endpoint that was deleted.

EndpointIdentifier (string) --The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can\'t end with a hyphen or contain two consecutive hyphens.

EndpointType (string) --The type of endpoint. Valid values are source and target .

EngineName (string) --The database engine name. Valid values, depending on the EndpointType, include "mysql" , "oracle" , "postgres" , "mariadb" , "aurora" , "aurora-postgresql" , "redshift" , "s3" , "db2" , "azuredb" , "sybase" , "dynamodb" , "mongodb" , "kinesis" , "kafka" , "elasticsearch" , "documentdb" , and "sqlserver" .

EngineDisplayName (string) --The expanded name for the engine name. For example, if the EngineName parameter is "aurora," this value would be "Amazon Aurora MySQL."

Username (string) --The user name used to connect to the endpoint.

ServerName (string) --The name of the server at the endpoint.

Port (integer) --The port value used to access the endpoint.

DatabaseName (string) --The name of the database at the endpoint.

ExtraConnectionAttributes (string) --Additional connection attributes used to connect to the endpoint.

Status (string) --The status of the endpoint.

KmsKeyId (string) --An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint.
If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key.
AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.

EndpointArn (string) --The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

CertificateArn (string) --The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

SslMode (string) --The SSL mode used to connect to the endpoint. The default value is none .

ServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) used by the service access IAM role.

ExternalTableDefinition (string) --The external table definition.

ExternalId (string) --Value returned by a call to CreateEndpoint that can be used for cross-account validation. Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

DynamoDbSettings (dict) --The settings for the target DynamoDB database. For more information, see the DynamoDBSettings structure.

ServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) used by the service access IAM role.



S3Settings (dict) --The settings for the S3 target endpoint. For more information, see the S3Settings structure.

ServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) used by the service access IAM role.

ExternalTableDefinition (string) --The external table definition.

CsvRowDelimiter (string) --The delimiter used to separate rows in the source files. The default is a carriage return (\
 ).

CsvDelimiter (string) --The delimiter used to separate columns in the source files. The default is a comma.

BucketFolder (string) --An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in the path `` bucketFolder /schema_name /table_name /`` . If this parameter isn\'t specified, then the path used is `` schema_name /table_name /`` .

BucketName (string) --The name of the S3 bucket.

CompressionType (string) --An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the target files. Either set this parameter to NONE (the default) or don\'t use it to leave the files uncompressed. This parameter applies to both .csv and .parquet file formats.

EncryptionMode (string) --The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either SSE_S3 (the default) or SSE_KMS . To use SSE_S3 , you need an AWS Identity and Access Management (IAM) role with permission to allow "arn:aws:s3:::dms-*" to use the following actions:

s3:CreateBucket
s3:ListBucket
s3:DeleteBucket
s3:GetBucketLocation
s3:GetObject
s3:PutObject
s3:DeleteObject
s3:GetObjectVersion
s3:GetBucketPolicy
s3:PutBucketPolicy
s3:DeleteBucketPolicy


ServerSideEncryptionKmsKeyId (string) --If you are using SSE_KMS for the EncryptionMode , provide the AWS KMS key ID. The key that you use needs an attached policy that enables AWS Identity and Access Management (IAM) user permissions and allows use of the key.
Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier value --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value* ,BucketFolder=*value* ,BucketName=*value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

DataFormat (string) --The format of the data that you want to use for output. You can choose one of the following:

csv : This is a row-based file format with comma-separated values (.csv).
parquet : Apache Parquet (.parquet) is a columnar storage file format that features efficient compression and provides faster query response.


EncodingType (string) --The type of encoding you are using:

RLE_DICTIONARY uses a combination of bit-packing and run-length encoding to store repeated values more efficiently. This is the default.
PLAIN doesn\'t use encoding at all. Values are stored as they are.
PLAIN_DICTIONARY builds a dictionary of the values encountered in a given column. The dictionary is stored in a dictionary page for each column chunk.


DictPageSizeLimit (integer) --The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds this, this column is stored using an encoding type of PLAIN . This parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to PLAIN encoding. This size is used for .parquet file format only.

RowGroupLength (integer) --The number of rows in a row group. A smaller row group size provides faster reads. But as the number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows. This number is used for .parquet file format only.
If you choose a value larger than the maximum, RowGroupLength is set to the max row group length in bytes (64 * 1024 * 1024).

DataPageSize (integer) --The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This number is used for .parquet file format only.

ParquetVersion (string) --The version of the Apache Parquet format that you want to use: parquet_1_0 (the default) or parquet_2_0 .

EnableStatistics (boolean) --A value that enables statistics for Parquet pages and row groups. Choose true to enable statistics, false to disable. Statistics include NULL , DISTINCT , MAX , and MIN values. This parameter defaults to true . This value is used for .parquet file format only.

IncludeOpForFullLoad (boolean) --A value that enables a full load to write INSERT operations to the comma-separated value (.csv) output files only to indicate how the rows were added to the source database.

Note
AWS DMS supports the IncludeOpForFullLoad parameter in versions 3.1.4 and later.

For full load, records can only be inserted. By default (the false setting), no information is recorded in these output files for a full load to indicate that the rows were inserted at the source database. If IncludeOpForFullLoad is set to true or y , the INSERT is recorded as an I annotation in the first field of the .csv file. This allows the format of your target records from a full load to be consistent with the target records from a CDC load.

Note
This setting works together with the CdcInsertsOnly and the CdcInsertsAndUpdates parameters for output to .csv files only. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .


CdcInsertsOnly (boolean) --A value that enables a change data capture (CDC) load to write only INSERT operations to .csv or columnar storage (.parquet) output files. By default (the false setting), the first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated, or deleted at the source database for a CDC load to the target.
If CdcInsertsOnly is set to true or y , only INSERTs from the source database are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded depends on the value of IncludeOpForFullLoad . If IncludeOpForFullLoad is set to true , the first field of every CDC record is set to I to indicate the INSERT operation at the source. If IncludeOpForFullLoad is set to false , every CDC record is written without a first field to indicate the INSERT operation at the source. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .

Note
AWS DMS supports the interaction described preceding between the CdcInsertsOnly and IncludeOpForFullLoad parameters in versions 3.1.4 and later.

CdcInsertsOnly and CdcInsertsAndUpdates can\'t both be set to true for the same endpoint. Set either CdcInsertsOnly or CdcInsertsAndUpdates to true for the same endpoint, but not both.


TimestampColumnName (string) --A value that when nonblank causes AWS DMS to add a column with timestamp information to the endpoint data for an Amazon S3 target.

Note
AWS DMS supports the TimestampColumnName parameter in versions 3.1.4 and later.

DMS includes an additional STRING column in the .csv or .parquet object files of your migrated data when you set TimestampColumnName to a nonblank value.
For a full load, each row of this timestamp column contains a timestamp for when the data was transferred from the source to the target by DMS.
For a change data capture (CDC) load, each row of the timestamp column contains the timestamp for the commit of that row in the source database.
The string format for this timestamp column value is yyyy-MM-dd HH:mm:ss.SSSSSS . By default, the precision of this value is in microseconds. For a CDC load, the rounding of the precision depends on the commit timestamp supported by DMS for the source database.
When the AddColumnName parameter is set to true , DMS also includes a name for the timestamp column that you set with TimestampColumnName .

ParquetTimestampInMillisecond (boolean) --A value that specifies the precision of any TIMESTAMP column values that are written to an Amazon S3 object file in .parquet format.

Note
AWS DMS supports the ParquetTimestampInMillisecond parameter in versions 3.1.4 and later.

When ParquetTimestampInMillisecond is set to true or y , AWS DMS writes all TIMESTAMP columns in a .parquet formatted file with millisecond precision. Otherwise, DMS writes them with microsecond precision.
Currently, Amazon Athena and AWS Glue can handle only millisecond precision for TIMESTAMP values. Set this parameter to true for S3 endpoint object files that are .parquet formatted only if you plan to query or process the data with Athena or AWS Glue.

Note
AWS DMS writes any TIMESTAMP column values written to an S3 file in .csv format with microsecond precision.
Setting ParquetTimestampInMillisecond has no effect on the string format of the timestamp column value that is inserted by setting the TimestampColumnName parameter.


CdcInsertsAndUpdates (boolean) --A value that enables a change data capture (CDC) load to write INSERT and UPDATE operations to .csv or .parquet (columnar storage) output files. The default setting is false , but when CdcInsertsAndUpdates is set to true or y , INSERTs and UPDATEs from the source database are migrated to the .csv or .parquet file.
For .csv file format only, how these INSERTs and UPDATEs are recorded depends on the value of the IncludeOpForFullLoad parameter. If IncludeOpForFullLoad is set to true , the first field of every CDC record is set to either I or U to indicate INSERT and UPDATE operations at the source. But if IncludeOpForFullLoad is set to false , CDC records are written without an indication of INSERT or UPDATE operations at the source. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .

Note
AWS DMS supports the use of the CdcInsertsAndUpdates parameter in versions 3.3.1 and later.

CdcInsertsOnly and CdcInsertsAndUpdates can\'t both be set to true for the same endpoint. Set either CdcInsertsOnly or CdcInsertsAndUpdates to true for the same endpoint, but not both.




DmsTransferSettings (dict) --The settings in JSON format for the DMS transfer type of source endpoint.
Possible settings include the following:

ServiceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.
BucketName - The name of the S3 bucket to use.
CompressionType - An optional parameter to use GZIP to compress the target files. To use GZIP, set this value to NONE (the default). To keep the files uncompressed, don\'t use this value.

Shorthand syntax for these settings is as follows: ServiceAccessRoleArn=string,BucketName=string,CompressionType=string
JSON syntax for these settings is as follows: { "ServiceAccessRoleArn": "string", "BucketName": "string", "CompressionType": "none"|"gzip" }

ServiceAccessRoleArn (string) --The IAM role that has permission to access the Amazon S3 bucket.

BucketName (string) --The name of the S3 bucket to use.



MongoDbSettings (dict) --The settings for the MongoDB source endpoint. For more information, see the MongoDbSettings structure.

Username (string) --The user name you use to access the MongoDB source endpoint.

Password (string) --The password for the user account you use to access the MongoDB source endpoint.

ServerName (string) --The name of the server on the MongoDB source endpoint.

Port (integer) --The port value for the MongoDB source endpoint.

DatabaseName (string) --The database name on the MongoDB source endpoint.

AuthType (string) --The authentication type you use to access the MongoDB source endpoint.
Valid values: NO, PASSWORD
When NO is selected, user name and password parameters are not used and can be empty.

AuthMechanism (string) --The authentication mechanism you use to access the MongoDB source endpoint.
Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1
DEFAULT \xe2\x80\x93 For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use SCRAM_SHA_1. This setting isn\'t used when authType=No.

NestingLevel (string) --Specifies either document or table mode.
Valid values: NONE, ONE
Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

ExtractDocId (string) --Specifies the document ID. Use this setting when NestingLevel is set to NONE.
Default value is false.

DocsToInvestigate (string) --Indicates the number of documents to preview to determine the document organization. Use this setting when NestingLevel is set to ONE.
Must be a positive value greater than 0. Default value is 1000.

AuthSource (string) --The MongoDB database name. This setting isn\'t used when authType=NO .
The default is admin.

KmsKeyId (string) --The AWS KMS key identifier that is used to encrypt the content on the replication instance. If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.



KinesisSettings (dict) --The settings for the Amazon Kinesis target endpoint. For more information, see the KinesisSettings structure.

StreamArn (string) --The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

MessageFormat (string) --The output format for the records created on the endpoint. The message format is JSON (default) or JSON_UNFORMATTED (a single line with no tab).

ServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) for the AWS Identity and Access Management (IAM) role that AWS DMS uses to write to the Kinesis data stream.

IncludeTransactionDetails (boolean) --Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for transaction_id , previous transaction_id , and transaction_record_id (the record offset within a transaction). The default is False .

IncludePartitionValue (boolean) --Shows the partition value within the Kinesis message output, unless the partition type is schema-table-type . The default is False .

PartitionIncludeSchemaTable (boolean) --Prefixes schema and table names to partition values, when the partition type is primary-key-type . Doing this increases data distribution among Kinesis shards. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same shard, which causes throttling. The default is False .

IncludeTableAlterOperations (boolean) --Includes any data definition language (DDL) operations that change the table in the control data, such as rename-table , drop-table , add-column , drop-column , and rename-column . The default is False .

IncludeControlDetails (boolean) --Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output. The default is False .



KafkaSettings (dict) --The settings for the Apache Kafka target endpoint. For more information, see the KafkaSettings structure.

Broker (string) --The broker location and port of the Kafka broker that hosts your Kafka instance. Specify the broker in the form `` broker-hostname-or-ip :port `` . For example, "ec2-12-345-678-901.compute-1.amazonaws.com:2345" .

Topic (string) --The topic to which you migrate the data. If you don\'t specify a topic, AWS DMS specifies "kafka-default-topic" as the migration topic.



ElasticsearchSettings (dict) --The settings for the Elasticsearch source endpoint. For more information, see the ElasticsearchSettings structure.

ServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) used by service to access the IAM role.

EndpointUri (string) --The endpoint for the Elasticsearch cluster.

FullLoadErrorPercentage (integer) --The maximum percentage of records that can fail to be written before a full load operation stops.

ErrorRetryDuration (integer) --The maximum number of seconds for which DMS retries failed API requests to the Elasticsearch cluster.



NeptuneSettings (dict) --The settings for the MongoDB source endpoint. For more information, see the NeptuneSettings structure.

ServiceAccessRoleArn (string) --The ARN of the service role you have created for the Neptune target endpoint. For more information, see https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.ServiceRole in the AWS Database Migration Service User Guide.

S3BucketName (string) --The name of the S3 bucket for AWS DMS to temporarily store migrated graph data in CSV files before bulk-loading it to the Neptune target database. AWS DMS maps the SQL source data to graph data before storing it in these CSV files.

S3BucketFolder (string) --A folder path where you where you want AWS DMS to store migrated graph data in the S3 bucket specified by S3BucketName

ErrorRetryDuration (integer) --The number of milliseconds for AWS DMS to wait to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 250.

MaxFileSize (integer) --The maximum size in KB of migrated graph data stored in a CSV file before AWS DMS bulk-loads the data to the Neptune target database. The default is 1048576 KB. If successful, AWS DMS clears the bucket, ready to store the next batch of migrated graph data.

MaxRetryCount (integer) --The number of times for AWS DMS to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 5.

IamAuthEnabled (boolean) --If you want IAM authorization enabled for this endpoint, set this parameter to true and attach the appropriate role policy document to your service role specified by ServiceAccessRoleArn . The default is false .



RedshiftSettings (dict) --Settings for the Amazon Redshift endpoint.

AcceptAnyDate (boolean) --A value that indicates to allow any date format, including invalid formats such as 00/00/00 00:00:00, to be loaded without generating an error. You can choose true or false (the default).
This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data doesn\'t match the DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

AfterConnectScript (string) --Code to run after connecting. This parameter should contain the code itself, not the name of a file containing the code.

BucketFolder (string) --The location where the comma-separated value (.csv) files are stored before being uploaded to the S3 bucket.

BucketName (string) --The name of the S3 bucket you want to use

ConnectionTimeout (integer) --A value that sets the amount of time to wait (in milliseconds) before timing out, beginning from when you initially establish a connection.

DatabaseName (string) --The name of the Amazon Redshift data warehouse (service) that you are working with.

DateFormat (string) --The date format that you are using. Valid values are auto (case-sensitive), your date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults to a format of \'YYYY-MM-DD\'. Using auto recognizes most strings, even some that aren\'t supported when you use a date format string.
If your date and time values use formats different from each other, set this to auto .

EmptyAsNull (boolean) --A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL. A value of true sets empty CHAR and VARCHAR fields to null. The default is false .

EncryptionMode (string) --The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either SSE_S3 (the default) or SSE_KMS . To use SSE_S3 , create an AWS Identity and Access Management (IAM) role with a policy that allows "arn:aws:s3:::*" to use the following actions: "s3:PutObject", "s3:ListBucket"

FileTransferUploadStreams (integer) --The number of threads used to upload a single file. This parameter accepts a value from 1 through 64. It defaults to 10.

LoadTimeout (integer) --The amount of time to wait (in milliseconds) before timing out, beginning from when you begin loading.

MaxFileSize (integer) --The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

Password (string) --The password for the user named in the username property.

Port (integer) --The port number for Amazon Redshift. The default value is 5439.

RemoveQuotes (boolean) --A value that specifies to remove surrounding quotation marks from strings in the incoming data. All characters within the quotation marks, including delimiters, are retained. Choose true to remove quotation marks. The default is false .

ReplaceInvalidChars (string) --A list of characters that you want to replace. Use with ReplaceChars .

ReplaceChars (string) --A value that specifies to replaces the invalid characters specified in ReplaceInvalidChars , substituting the specified characters instead. The default is "?" .

ServerName (string) --The name of the Amazon Redshift cluster you are using.

ServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service.

ServerSideEncryptionKmsKeyId (string) --The AWS KMS key ID. If you are using SSE_KMS for the EncryptionMode , provide this key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.

TimeFormat (string) --The time format that you want to use. Valid values are auto (case-sensitive), \'timeformat_string\' , \'epochsecs\' , or \'epochmillisecs\' . It defaults to 10. Using auto recognizes most strings, even some that aren\'t supported when you use a time format string.
If your date and time values use formats different from each other, set this parameter to auto .

TrimBlanks (boolean) --A value that specifies to remove the trailing white space characters from a VARCHAR string. This parameter applies only to columns with a VARCHAR data type. Choose true to remove unneeded white space. The default is false .

TruncateColumns (boolean) --A value that specifies to truncate data in columns to the appropriate number of characters, so that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose true to truncate data. The default is false .

Username (string) --An Amazon Redshift user name for a registered user.

WriteBufferSize (integer) --The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The default is 1,024. Use this setting to tune performance.










Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault

Examples
Deletes the specified endpoint. All tasks associated with the endpoint must be deleted before you can delete the endpoint.
response = client.delete_endpoint(
    EndpointArn='arn:aws:dms:us-east-1:123456789012:endpoint:RAAR3R22XSH46S3PWLC3NJAWKM',
)

print(response)


Expected Output:
{
    'Endpoint': {
        'EndpointArn': 'arn:aws:dms:us-east-1:123456789012:endpoint:RAAR3R22XSH46S3PWLC3NJAWKM',
        'EndpointIdentifier': 'test-endpoint-1',
        'EndpointType': 'source',
        'EngineName': 'mysql',
        'KmsKeyId': 'arn:aws:kms:us-east-1:123456789012:key/4c1731d6-5435-ed4d-be13-d53411a7cfbd',
        'Port': 3306,
        'ServerName': 'mydb.cx1llnox7iyx.us-west-2.rds.amazonaws.com',
        'Status': 'active',
        'Username': 'username',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Endpoint': {
            'EndpointIdentifier': 'string',
            'EndpointType': 'source'|'target',
            'EngineName': 'string',
            'EngineDisplayName': 'string',
            'Username': 'string',
            'ServerName': 'string',
            'Port': 123,
            'DatabaseName': 'string',
            'ExtraConnectionAttributes': 'string',
            'Status': 'string',
            'KmsKeyId': 'string',
            'EndpointArn': 'string',
            'CertificateArn': 'string',
            'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
            'ServiceAccessRoleArn': 'string',
            'ExternalTableDefinition': 'string',
            'ExternalId': 'string',
            'DynamoDbSettings': {
                'ServiceAccessRoleArn': 'string'
            },
            'S3Settings': {
                'ServiceAccessRoleArn': 'string',
                'ExternalTableDefinition': 'string',
                'CsvRowDelimiter': 'string',
                'CsvDelimiter': 'string',
                'BucketFolder': 'string',
                'BucketName': 'string',
                'CompressionType': 'none'|'gzip',
                'EncryptionMode': 'sse-s3'|'sse-kms',
                'ServerSideEncryptionKmsKeyId': 'string',
                'DataFormat': 'csv'|'parquet',
                'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
                'DictPageSizeLimit': 123,
                'RowGroupLength': 123,
                'DataPageSize': 123,
                'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
                'EnableStatistics': True|False,
                'IncludeOpForFullLoad': True|False,
                'CdcInsertsOnly': True|False,
                'TimestampColumnName': 'string',
                'ParquetTimestampInMillisecond': True|False,
                'CdcInsertsAndUpdates': True|False
            },
            'DmsTransferSettings': {
                'ServiceAccessRoleArn': 'string',
                'BucketName': 'string'
            },
            'MongoDbSettings': {
                'Username': 'string',
                'Password': 'string',
                'ServerName': 'string',
                'Port': 123,
                'DatabaseName': 'string',
                'AuthType': 'no'|'password',
                'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                'NestingLevel': 'none'|'one',
                'ExtractDocId': 'string',
                'DocsToInvestigate': 'string',
                'AuthSource': 'string',
                'KmsKeyId': 'string'
            },
            'KinesisSettings': {
                'StreamArn': 'string',
                'MessageFormat': 'json'|'json-unformatted',
                'ServiceAccessRoleArn': 'string',
                'IncludeTransactionDetails': True|False,
                'IncludePartitionValue': True|False,
                'PartitionIncludeSchemaTable': True|False,
                'IncludeTableAlterOperations': True|False,
                'IncludeControlDetails': True|False
            },
            'KafkaSettings': {
                'Broker': 'string',
                'Topic': 'string'
            },
            'ElasticsearchSettings': {
                'ServiceAccessRoleArn': 'string',
                'EndpointUri': 'string',
                'FullLoadErrorPercentage': 123,
                'ErrorRetryDuration': 123
            },
            'NeptuneSettings': {
                'ServiceAccessRoleArn': 'string',
                'S3BucketName': 'string',
                'S3BucketFolder': 'string',
                'ErrorRetryDuration': 123,
                'MaxFileSize': 123,
                'MaxRetryCount': 123,
                'IamAuthEnabled': True|False
            },
            'RedshiftSettings': {
                'AcceptAnyDate': True|False,
                'AfterConnectScript': 'string',
                'BucketFolder': 'string',
                'BucketName': 'string',
                'ConnectionTimeout': 123,
                'DatabaseName': 'string',
                'DateFormat': 'string',
                'EmptyAsNull': True|False,
                'EncryptionMode': 'sse-s3'|'sse-kms',
                'FileTransferUploadStreams': 123,
                'LoadTimeout': 123,
                'MaxFileSize': 123,
                'Password': 'string',
                'Port': 123,
                'RemoveQuotes': True|False,
                'ReplaceInvalidChars': 'string',
                'ReplaceChars': 'string',
                'ServerName': 'string',
                'ServiceAccessRoleArn': 'string',
                'ServerSideEncryptionKmsKeyId': 'string',
                'TimeFormat': 'string',
                'TrimBlanks': True|False,
                'TruncateColumns': True|False,
                'Username': 'string',
                'WriteBufferSize': 123
            }
        }
    }
    
    
    :returns: 
    csv : This is a row-based file format with comma-separated values (.csv).
    parquet : Apache Parquet (.parquet) is a columnar storage file format that features efficient compression and provides faster query response.
    
    """
    pass

def delete_event_subscription(SubscriptionName=None):
    """
    Deletes an AWS DMS event subscription.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_event_subscription(
        SubscriptionName='string'
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]\nThe name of the DMS event notification subscription to be deleted.\n

    :rtype: dict
ReturnsResponse Syntax{
    'EventSubscription': {
        'CustomerAwsId': 'string',
        'CustSubscriptionId': 'string',
        'SnsTopicArn': 'string',
        'Status': 'string',
        'SubscriptionCreationTime': 'string',
        'SourceType': 'string',
        'SourceIdsList': [
            'string',
        ],
        'EventCategoriesList': [
            'string',
        ],
        'Enabled': True|False
    }
}


Response Structure

(dict) --
EventSubscription (dict) --The event subscription that was deleted.

CustomerAwsId (string) --The AWS customer account associated with the AWS DMS event notification subscription.

CustSubscriptionId (string) --The AWS DMS event notification subscription Id.

SnsTopicArn (string) --The topic ARN of the AWS DMS event notification subscription.

Status (string) --The status of the AWS DMS event notification subscription.
Constraints:
Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
The status "no-permission" indicates that AWS DMS no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.

SubscriptionCreationTime (string) --The time the RDS event notification subscription was created.

SourceType (string) --The type of AWS DMS resource that generates events.
Valid values: replication-instance | replication-server | security-group | replication-task

SourceIdsList (list) --A list of source Ids for the event subscription.

(string) --


EventCategoriesList (list) --A lists of event categories.

(string) --


Enabled (boolean) --Boolean value that indicates if the event subscription is enabled.








Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault


    :return: {
        'EventSubscription': {
            'CustomerAwsId': 'string',
            'CustSubscriptionId': 'string',
            'SnsTopicArn': 'string',
            'Status': 'string',
            'SubscriptionCreationTime': 'string',
            'SourceType': 'string',
            'SourceIdsList': [
                'string',
            ],
            'EventCategoriesList': [
                'string',
            ],
            'Enabled': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_replication_instance(ReplicationInstanceArn=None):
    """
    Deletes the specified replication instance.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes the specified replication instance. You must delete any migration tasks that are associated with the replication instance before you can delete it.
    Expected Output:
    
    :example: response = client.delete_replication_instance(
        ReplicationInstanceArn='string'
    )
    
    
    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the replication instance to be deleted.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ReplicationInstance': {
        'ReplicationInstanceIdentifier': 'string',
        'ReplicationInstanceClass': 'string',
        'ReplicationInstanceStatus': 'string',
        'AllocatedStorage': 123,
        'InstanceCreateTime': datetime(2015, 1, 1),
        'VpcSecurityGroups': [
            {
                'VpcSecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'AvailabilityZone': 'string',
        'ReplicationSubnetGroup': {
            'ReplicationSubnetGroupIdentifier': 'string',
            'ReplicationSubnetGroupDescription': 'string',
            'VpcId': 'string',
            'SubnetGroupStatus': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': {
                        'Name': 'string'
                    },
                    'SubnetStatus': 'string'
                },
            ]
        },
        'PreferredMaintenanceWindow': 'string',
        'PendingModifiedValues': {
            'ReplicationInstanceClass': 'string',
            'AllocatedStorage': 123,
            'MultiAZ': True|False,
            'EngineVersion': 'string'
        },
        'MultiAZ': True|False,
        'EngineVersion': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'KmsKeyId': 'string',
        'ReplicationInstanceArn': 'string',
        'ReplicationInstancePublicIpAddress': 'string',
        'ReplicationInstancePrivateIpAddress': 'string',
        'ReplicationInstancePublicIpAddresses': [
            'string',
        ],
        'ReplicationInstancePrivateIpAddresses': [
            'string',
        ],
        'PubliclyAccessible': True|False,
        'SecondaryAvailabilityZone': 'string',
        'FreeUntil': datetime(2015, 1, 1),
        'DnsNameServers': 'string'
    }
}


Response Structure

(dict) --
ReplicationInstance (dict) --The replication instance that was deleted.

ReplicationInstanceIdentifier (string) --The replication instance identifier. This parameter is stored as a lowercase string.
Constraints:

Must contain from 1 to 63 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.

Example: myrepinstance

ReplicationInstanceClass (string) --The compute and memory capacity of the replication instance.
Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge

ReplicationInstanceStatus (string) --The status of the replication instance.

AllocatedStorage (integer) --The amount of storage (in gigabytes) that is allocated for the replication instance.

InstanceCreateTime (datetime) --The time the replication instance was created.

VpcSecurityGroups (list) --The VPC security group for the instance.

(dict) --Describes status of a security group associated with the virtual private cloud hosting your replication and DB instances.

VpcSecurityGroupId (string) --The VPC security group Id.

Status (string) --The status of the VPC security group.





AvailabilityZone (string) --The Availability Zone for the instance.

ReplicationSubnetGroup (dict) --The subnet group for the replication instance.

ReplicationSubnetGroupIdentifier (string) --The identifier of the replication instance subnet group.

ReplicationSubnetGroupDescription (string) --A description for the replication subnet group.

VpcId (string) --The ID of the VPC.

SubnetGroupStatus (string) --The status of the subnet group.

Subnets (list) --The subnets that are in the subnet group.

(dict) --In response to a request by the DescribeReplicationSubnetGroup operation, this object identifies a subnet by its given Availability Zone, subnet identifier, and status.

SubnetIdentifier (string) --The subnet identifier.

SubnetAvailabilityZone (dict) --The Availability Zone of the subnet.

Name (string) --The name of the Availability Zone.



SubnetStatus (string) --The status of the subnet.







PreferredMaintenanceWindow (string) --The maintenance window times for the replication instance.

PendingModifiedValues (dict) --The pending modification values.

ReplicationInstanceClass (string) --The compute and memory capacity of the replication instance.
Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge

AllocatedStorage (integer) --The amount of storage (in gigabytes) that is allocated for the replication instance.

MultiAZ (boolean) --Specifies whether the replication instance is a Multi-AZ deployment. You can\'t set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .

EngineVersion (string) --The engine version number of the replication instance.



MultiAZ (boolean) --Specifies whether the replication instance is a Multi-AZ deployment. You can\'t set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .

EngineVersion (string) --The engine version number of the replication instance.

AutoMinorVersionUpgrade (boolean) --Boolean value indicating if minor version upgrades will be automatically applied to the instance.

KmsKeyId (string) --An AWS KMS key identifier that is used to encrypt the data on the replication instance.
If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key.
AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.

ReplicationInstanceArn (string) --The Amazon Resource Name (ARN) of the replication instance.

ReplicationInstancePublicIpAddress (string) --The public IP address of the replication instance.

ReplicationInstancePrivateIpAddress (string) --The private IP address of the replication instance.

ReplicationInstancePublicIpAddresses (list) --One or more public IP addresses for the replication instance.

(string) --


ReplicationInstancePrivateIpAddresses (list) --One or more private IP addresses for the replication instance.

(string) --


PubliclyAccessible (boolean) --Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address. The default value is true .

SecondaryAvailabilityZone (string) --The Availability Zone of the standby replication instance in a Multi-AZ deployment.

FreeUntil (datetime) --The expiration date of the free replication instance that is part of the Free DMS program.

DnsNameServers (string) --The DNS name servers for the replication instance.








Exceptions

DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault

Examples
Deletes the specified replication instance. You must delete any migration tasks that are associated with the replication instance before you can delete it.
response = client.delete_replication_instance(
    ReplicationInstanceArn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ',
)

print(response)


Expected Output:
{
    'ReplicationInstance': {
        'AllocatedStorage': 5,
        'AutoMinorVersionUpgrade': True,
        'EngineVersion': '1.5.0',
        'KmsKeyId': 'arn:aws:kms:us-east-1:123456789012:key/4c1731d6-5435-ed4d-be13-d53411a7cfbd',
        'PendingModifiedValues': {
        },
        'PreferredMaintenanceWindow': 'sun:06:00-sun:14:00',
        'PubliclyAccessible': True,
        'ReplicationInstanceArn': 'arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ',
        'ReplicationInstanceClass': 'dms.t2.micro',
        'ReplicationInstanceIdentifier': 'test-rep-1',
        'ReplicationInstanceStatus': 'creating',
        'ReplicationSubnetGroup': {
            'ReplicationSubnetGroupDescription': 'default',
            'ReplicationSubnetGroupIdentifier': 'default',
            'SubnetGroupStatus': 'Complete',
            'Subnets': [
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1d',
                    },
                    'SubnetIdentifier': 'subnet-f6dd91af',
                    'SubnetStatus': 'Active',
                },
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1b',
                    },
                    'SubnetIdentifier': 'subnet-3605751d',
                    'SubnetStatus': 'Active',
                },
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1c',
                    },
                    'SubnetIdentifier': 'subnet-c2daefb5',
                    'SubnetStatus': 'Active',
                },
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1e',
                    },
                    'SubnetIdentifier': 'subnet-85e90cb8',
                    'SubnetStatus': 'Active',
                },
            ],
            'VpcId': 'vpc-6741a603',
        },
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReplicationInstance': {
            'ReplicationInstanceIdentifier': 'string',
            'ReplicationInstanceClass': 'string',
            'ReplicationInstanceStatus': 'string',
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'ReplicationSubnetGroup': {
                'ReplicationSubnetGroupIdentifier': 'string',
                'ReplicationSubnetGroupDescription': 'string',
                'VpcId': 'string',
                'SubnetGroupStatus': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        },
                        'SubnetStatus': 'string'
                    },
                ]
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'ReplicationInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string'
            },
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'KmsKeyId': 'string',
            'ReplicationInstanceArn': 'string',
            'ReplicationInstancePublicIpAddress': 'string',
            'ReplicationInstancePrivateIpAddress': 'string',
            'ReplicationInstancePublicIpAddresses': [
                'string',
            ],
            'ReplicationInstancePrivateIpAddresses': [
                'string',
            ],
            'PubliclyAccessible': True|False,
            'SecondaryAvailabilityZone': 'string',
            'FreeUntil': datetime(2015, 1, 1),
            'DnsNameServers': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_replication_subnet_group(ReplicationSubnetGroupIdentifier=None):
    """
    Deletes a subnet group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes a replication subnet group.
    Expected Output:
    
    :example: response = client.delete_replication_subnet_group(
        ReplicationSubnetGroupIdentifier='string'
    )
    
    
    :type ReplicationSubnetGroupIdentifier: string
    :param ReplicationSubnetGroupIdentifier: [REQUIRED]\nThe subnet group name of the replication instance.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault

Examples
Deletes a replication subnet group.
response = client.delete_replication_subnet_group(
    ReplicationSubnetGroupIdentifier='us-west-2ab-vpc-215ds366',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    
    """
    pass

def delete_replication_task(ReplicationTaskArn=None):
    """
    Deletes the specified replication task.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes the specified replication task.
    Expected Output:
    
    :example: response = client.delete_replication_task(
        ReplicationTaskArn='string'
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the replication task to be deleted.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ReplicationTask': {
        'ReplicationTaskIdentifier': 'string',
        'SourceEndpointArn': 'string',
        'TargetEndpointArn': 'string',
        'ReplicationInstanceArn': 'string',
        'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
        'TableMappings': 'string',
        'ReplicationTaskSettings': 'string',
        'Status': 'string',
        'LastFailureMessage': 'string',
        'StopReason': 'string',
        'ReplicationTaskCreationDate': datetime(2015, 1, 1),
        'ReplicationTaskStartDate': datetime(2015, 1, 1),
        'CdcStartPosition': 'string',
        'CdcStopPosition': 'string',
        'RecoveryCheckpoint': 'string',
        'ReplicationTaskArn': 'string',
        'ReplicationTaskStats': {
            'FullLoadProgressPercent': 123,
            'ElapsedTimeMillis': 123,
            'TablesLoaded': 123,
            'TablesLoading': 123,
            'TablesQueued': 123,
            'TablesErrored': 123,
            'FreshStartDate': datetime(2015, 1, 1),
            'StartDate': datetime(2015, 1, 1),
            'StopDate': datetime(2015, 1, 1),
            'FullLoadStartDate': datetime(2015, 1, 1),
            'FullLoadFinishDate': datetime(2015, 1, 1)
        },
        'TaskData': 'string'
    }
}


Response Structure

(dict) --
ReplicationTask (dict) --The deleted replication task.

ReplicationTaskIdentifier (string) --The user-assigned replication task identifier or name.
Constraints:

Must contain from 1 to 255 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.


SourceEndpointArn (string) --The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

TargetEndpointArn (string) --The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

ReplicationInstanceArn (string) --The Amazon Resource Name (ARN) of the replication instance.

MigrationType (string) --The type of migration.

TableMappings (string) --Table mappings specified in the task.

ReplicationTaskSettings (string) --The settings for the replication task.

Status (string) --The status of the replication task.

LastFailureMessage (string) --The last error (failure) message generated for the replication instance.

StopReason (string) --The reason the replication task was stopped.

ReplicationTaskCreationDate (datetime) --The date the replication task was created.

ReplicationTaskStartDate (datetime) --The date the replication task is scheduled to start.

CdcStartPosition (string) --Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want the CDC operation to start. Specifying both values results in an error.
The value can be in date, checkpoint, or LSN/SCN format.
Date Example: --cdc-start-position \xe2\x80\x9c2018-03-08T12:12:12\xe2\x80\x9d
Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
LSN Example: --cdc-start-position \xe2\x80\x9cmysql-bin-changelog.000024:373\xe2\x80\x9d

CdcStopPosition (string) --Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
Server time example: --cdc-stop-position \xe2\x80\x9cserver_time:3018-02-09T12:12:12\xe2\x80\x9d
Commit time example: --cdc-stop-position \xe2\x80\x9ccommit_time: 3018-02-09T12:12:12 \xe2\x80\x9c

RecoveryCheckpoint (string) --Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the CdcStartPosition parameter to start a CDC operation that begins at that checkpoint.

ReplicationTaskArn (string) --The Amazon Resource Name (ARN) of the replication task.

ReplicationTaskStats (dict) --The statistics for the task, including elapsed time, tables loaded, and table errors.

FullLoadProgressPercent (integer) --The percent complete for the full load migration task.

ElapsedTimeMillis (integer) --The elapsed time of the task, in milliseconds.

TablesLoaded (integer) --The number of tables loaded for this task.

TablesLoading (integer) --The number of tables currently loading for this task.

TablesQueued (integer) --The number of tables queued for this task.

TablesErrored (integer) --The number of errors that have occurred during this task.

FreshStartDate (datetime) --The date the replication task was started either with a fresh start or a target reload.

StartDate (datetime) --The date the replication task was started either with a fresh start or a resume. For more information, see StartReplicationTaskType .

StopDate (datetime) --The date the replication task was stopped.

FullLoadStartDate (datetime) --The date the replication task full load was started.

FullLoadFinishDate (datetime) --The date the replication task full load was completed.



TaskData (string) --Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see Specifying Supplemental Data for Task Settings in the AWS Database Migration User Guide.








Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault

Examples
Deletes the specified replication task.
response = client.delete_replication_task(
    ReplicationTaskArn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ',
)

print(response)


Expected Output:
{
    'ReplicationTask': {
        'MigrationType': 'full-load',
        'ReplicationInstanceArn': 'arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ',
        'ReplicationTaskArn': 'arn:aws:dms:us-east-1:123456789012:task:OEAMB3NXSTZ6LFYZFEPPBBXPYM',
        'ReplicationTaskCreationDate': datetime(2016, 12, 14, 18, 25, 43, 2, 349, 0),
        'ReplicationTaskIdentifier': 'task1',
        'ReplicationTaskSettings': '{"TargetMetadata":{"TargetSchema":"","SupportLobs":true,"FullLobMode":true,"LobChunkSize":64,"LimitedSizeLobMode":false,"LobMaxSize":0},"FullLoadSettings":{"FullLoadEnabled":true,"ApplyChangesEnabled":false,"TargetTablePrepMode":"DROP_AND_CREATE","CreatePkAfterFullLoad":false,"StopTaskCachedChangesApplied":false,"StopTaskCachedChangesNotApplied":false,"ResumeEnabled":false,"ResumeMinTableSize":100000,"ResumeOnlyClusteredPKTables":true,"MaxFullLoadSubTasks":8,"TransactionConsistencyTimeout":600,"CommitRate":10000},"Logging":{"EnableLogging":false}}',
        'SourceEndpointArn': 'arn:aws:dms:us-east-1:123456789012:endpoint:ZW5UAN6P4E77EC7YWHK4RZZ3BE',
        'Status': 'creating',
        'TableMappings': 'file://mappingfile.json',
        'TargetEndpointArn': 'arn:aws:dms:us-east-1:123456789012:endpoint:ASXWXJZLNWNT5HTWCGV2BUJQ7E',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReplicationTask': {
            'ReplicationTaskIdentifier': 'string',
            'SourceEndpointArn': 'string',
            'TargetEndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
            'TableMappings': 'string',
            'ReplicationTaskSettings': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'StopReason': 'string',
            'ReplicationTaskCreationDate': datetime(2015, 1, 1),
            'ReplicationTaskStartDate': datetime(2015, 1, 1),
            'CdcStartPosition': 'string',
            'CdcStopPosition': 'string',
            'RecoveryCheckpoint': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationTaskStats': {
                'FullLoadProgressPercent': 123,
                'ElapsedTimeMillis': 123,
                'TablesLoaded': 123,
                'TablesLoading': 123,
                'TablesQueued': 123,
                'TablesErrored': 123,
                'FreshStartDate': datetime(2015, 1, 1),
                'StartDate': datetime(2015, 1, 1),
                'StopDate': datetime(2015, 1, 1),
                'FullLoadStartDate': datetime(2015, 1, 1),
                'FullLoadFinishDate': datetime(2015, 1, 1)
            },
            'TaskData': 'string'
        }
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
    
    """
    pass

def describe_account_attributes():
    """
    Lists all of the AWS DMS attributes for a customer account. These attributes include AWS DMS quotas for the account and a unique account identifier in a particular DMS region. DMS quotas include a list of resource quotas supported by the account, such as the number of replication instances allowed. The description for each resource quota, includes the quota name, current usage toward that quota, and the quota\'s maximum value. DMS uses the unique account identifier to name each artifact used by DMS in the given region.
    This command does not take any parameters.
    See also: AWS API Documentation
    
    Examples
    Lists all of the AWS DMS attributes for a customer account. The attributes include AWS DMS quotas for the account, such as the number of replication instances allowed. The description for a quota includes the quota name, current usage toward that quota, and the quota\'s maximum value. This operation does not take any parameters.
    Expected Output:
    
    :example: response = client.describe_account_attributes()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'AccountQuotas': [
        {
            'AccountQuotaName': 'string',
            'Used': 123,
            'Max': 123
        },
    ],
    'UniqueAccountIdentifier': 'string'
}


Response Structure

(dict) --
AccountQuotas (list) --Account quota information.

(dict) --Describes a quota for an AWS account, for example, the number of replication instances allowed.

AccountQuotaName (string) --The name of the AWS DMS quota for this AWS account.

Used (integer) --The amount currently used toward the quota maximum.

Max (integer) --The maximum allowed value for the quota.





UniqueAccountIdentifier (string) --A unique AWS DMS identifier for an account in a particular AWS Region. The value of this identifier has the following format: c99999999999 . DMS uses this identifier to name artifacts. For example, DMS uses this identifier to name the default Amazon S3 bucket for storing task assessment reports in a given AWS Region. The format of this S3 bucket name is the following: dms-*AccountNumber* -*UniqueAccountIdentifier* . Here is an example name for this default S3 bucket: dms-111122223333-c44445555666 .

Note
AWS DMS supports the UniqueAccountIdentifier parameter in versions 3.1.4 and later.







Examples
Lists all of the AWS DMS attributes for a customer account. The attributes include AWS DMS quotas for the account, such as the number of replication instances allowed. The description for a quota includes the quota name, current usage toward that quota, and the quota\'s maximum value. This operation does not take any parameters.
response = client.describe_account_attributes(
)

print(response)


Expected Output:
{
    'AccountQuotas': [
        {
            'AccountQuotaName': 'ReplicationInstances',
            'Max': 20,
            'Used': 0,
        },
        {
            'AccountQuotaName': 'AllocatedStorage',
            'Max': 20,
            'Used': 0,
        },
        {
            'AccountQuotaName': 'Endpoints',
            'Max': 20,
            'Used': 0,
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AccountQuotas': [
            {
                'AccountQuotaName': 'string',
                'Used': 123,
                'Max': 123
            },
        ],
        'UniqueAccountIdentifier': 'string'
    }
    
    
    """
    pass

def describe_certificates(Filters=None, MaxRecords=None, Marker=None):
    """
    Provides a description of the certificate.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Provides a description of the certificate.
    Expected Output:
    
    :example: response = client.describe_certificates(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type Filters: list
    :param Filters: Filters applied to the certificate described in the form of key-value pairs.\n\n(dict) --Identifies the name and value of a source filter object used to limit the number and type of records transferred from your source to your target.\n\nName (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 10\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'Certificates': [
        {
            'CertificateIdentifier': 'string',
            'CertificateCreationDate': datetime(2015, 1, 1),
            'CertificatePem': 'string',
            'CertificateWallet': b'bytes',
            'CertificateArn': 'string',
            'CertificateOwner': 'string',
            'ValidFromDate': datetime(2015, 1, 1),
            'ValidToDate': datetime(2015, 1, 1),
            'SigningAlgorithm': 'string',
            'KeyLength': 123
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
The pagination token.

Certificates (list) --
The Secure Sockets Layer (SSL) certificates associated with the replication instance.

(dict) --
The SSL certificate that can be used to encrypt connections between the endpoints and the replication instance.

CertificateIdentifier (string) --
A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can\'t end with a hyphen or contain two consecutive hyphens.

CertificateCreationDate (datetime) --
The date that the certificate was created.

CertificatePem (string) --
The contents of a .pem file, which contains an X.509 certificate.

CertificateWallet (bytes) --
The location of an imported Oracle Wallet certificate for use with SSL.

CertificateArn (string) --
The Amazon Resource Name (ARN) for the certificate.

CertificateOwner (string) --
The owner of the certificate.

ValidFromDate (datetime) --
The beginning date that the certificate is valid.

ValidToDate (datetime) --
The final date that the certificate is valid.

SigningAlgorithm (string) --
The signing algorithm for the certificate.

KeyLength (integer) --
The key length of the cryptographic algorithm being used.











Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault

Examples
Provides a description of the certificate.
response = client.describe_certificates(
    Filters=[
        {
            'Name': 'string',
            'Values': [
                'string',
                'string',
            ],
        },
    ],
    Marker='',
    MaxRecords=123,
)

print(response)


Expected Output:
{
    'Certificates': [
    ],
    'Marker': '',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'Certificates': [
            {
                'CertificateIdentifier': 'string',
                'CertificateCreationDate': datetime(2015, 1, 1),
                'CertificatePem': 'string',
                'CertificateWallet': b'bytes',
                'CertificateArn': 'string',
                'CertificateOwner': 'string',
                'ValidFromDate': datetime(2015, 1, 1),
                'ValidToDate': datetime(2015, 1, 1),
                'SigningAlgorithm': 'string',
                'KeyLength': 123
            },
        ]
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    
    """
    pass

def describe_connections(Filters=None, MaxRecords=None, Marker=None):
    """
    Describes the status of the connections that have been made between the replication instance and an endpoint. Connections are created when you test an endpoint.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Describes the status of the connections that have been made between the replication instance and an endpoint. Connections are created when you test an endpoint.
    Expected Output:
    
    :example: response = client.describe_connections(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type Filters: list
    :param Filters: The filters applied to the connection.\nValid filter names: endpoint-arn | replication-instance-arn\n\n(dict) --Identifies the name and value of a source filter object used to limit the number and type of records transferred from your source to your target.\n\nName (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'Connections': [
        {
            'ReplicationInstanceArn': 'string',
            'EndpointArn': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'EndpointIdentifier': 'string',
            'ReplicationInstanceIdentifier': 'string'
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

Connections (list) --
A description of the connections.

(dict) --
Status of the connection between an endpoint and a replication instance, including Amazon Resource Names (ARNs) and the last error message issued.

ReplicationInstanceArn (string) --
The ARN of the replication instance.

EndpointArn (string) --
The ARN string that uniquely identifies the endpoint.

Status (string) --
The connection status.

LastFailureMessage (string) --
The error message when the connection last failed.

EndpointIdentifier (string) --
The identifier of the endpoint. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can\'t end with a hyphen or contain two consecutive hyphens.

ReplicationInstanceIdentifier (string) --
The replication instance identifier. This parameter is stored as a lowercase string.











Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault

Examples
Describes the status of the connections that have been made between the replication instance and an endpoint. Connections are created when you test an endpoint.
response = client.describe_connections(
    Filters=[
        {
            'Name': 'string',
            'Values': [
                'string',
                'string',
            ],
        },
    ],
    Marker='',
    MaxRecords=123,
)

print(response)


Expected Output:
{
    'Connections': [
        {
            'EndpointArn': 'arn:aws:dms:us-east-arn:aws:dms:us-east-1:123456789012:endpoint:ZW5UAN6P4E77EC7YWHK4RZZ3BE',
            'EndpointIdentifier': 'testsrc1',
            'ReplicationInstanceArn': 'arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ',
            'ReplicationInstanceIdentifier': 'test',
            'Status': 'successful',
        },
    ],
    'Marker': '',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'Connections': [
            {
                'ReplicationInstanceArn': 'string',
                'EndpointArn': 'string',
                'Status': 'string',
                'LastFailureMessage': 'string',
                'EndpointIdentifier': 'string',
                'ReplicationInstanceIdentifier': 'string'
            },
        ]
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    
    """
    pass

def describe_endpoint_types(Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about the type of endpoints available.
    See also: AWS API Documentation
    
    Examples
    Returns information about the type of endpoints available.
    Expected Output:
    
    :example: response = client.describe_endpoint_types(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type Filters: list
    :param Filters: Filters applied to the describe action.\nValid filter names: engine-name | endpoint-type\n\n(dict) --Identifies the name and value of a source filter object used to limit the number and type of records transferred from your source to your target.\n\nName (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'SupportedEndpointTypes': [
        {
            'EngineName': 'string',
            'SupportsCDC': True|False,
            'EndpointType': 'source'|'target',
            'ReplicationInstanceEngineMinimumVersion': 'string',
            'EngineDisplayName': 'string'
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

SupportedEndpointTypes (list) --
The types of endpoints that are supported.

(dict) --
Provides information about types of supported endpoints in response to a request by the DescribeEndpointTypes operation. This information includes the type of endpoint, the database engine name, and whether change data capture (CDC) is supported.

EngineName (string) --
The database engine name. Valid values, depending on the EndpointType, include "mysql" , "oracle" , "postgres" , "mariadb" , "aurora" , "aurora-postgresql" , "redshift" , "s3" , "db2" , "azuredb" , "sybase" , "dynamodb" , "mongodb" , "kinesis" , "kafka" , "elasticsearch" , "documentdb" , and "sqlserver" .

SupportsCDC (boolean) --
Indicates if Change Data Capture (CDC) is supported.

EndpointType (string) --
The type of endpoint. Valid values are source and target .

ReplicationInstanceEngineMinimumVersion (string) --
The earliest AWS DMS engine version that supports this endpoint engine. Note that endpoint engines released with AWS DMS versions earlier than 3.1.1 do not return a value for this parameter.

EngineDisplayName (string) --
The expanded name for the engine name. For example, if the EngineName parameter is "aurora," this value would be "Amazon Aurora MySQL."











Examples
Returns information about the type of endpoints available.
response = client.describe_endpoint_types(
    Filters=[
        {
            'Name': 'string',
            'Values': [
                'string',
                'string',
            ],
        },
    ],
    Marker='',
    MaxRecords=123,
)

print(response)


Expected Output:
{
    'Marker': '',
    'SupportedEndpointTypes': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'SupportedEndpointTypes': [
            {
                'EngineName': 'string',
                'SupportsCDC': True|False,
                'EndpointType': 'source'|'target',
                'ReplicationInstanceEngineMinimumVersion': 'string',
                'EngineDisplayName': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_endpoints(Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about the endpoints for your account in the current region.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns information about the endpoints for your account in the current region.
    Expected Output:
    
    :example: response = client.describe_endpoints(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type Filters: list
    :param Filters: Filters applied to the describe action.\nValid filter names: endpoint-arn | endpoint-type | endpoint-id | engine-name\n\n(dict) --Identifies the name and value of a source filter object used to limit the number and type of records transferred from your source to your target.\n\nName (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'Endpoints': [
        {
            'EndpointIdentifier': 'string',
            'EndpointType': 'source'|'target',
            'EngineName': 'string',
            'EngineDisplayName': 'string',
            'Username': 'string',
            'ServerName': 'string',
            'Port': 123,
            'DatabaseName': 'string',
            'ExtraConnectionAttributes': 'string',
            'Status': 'string',
            'KmsKeyId': 'string',
            'EndpointArn': 'string',
            'CertificateArn': 'string',
            'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
            'ServiceAccessRoleArn': 'string',
            'ExternalTableDefinition': 'string',
            'ExternalId': 'string',
            'DynamoDbSettings': {
                'ServiceAccessRoleArn': 'string'
            },
            'S3Settings': {
                'ServiceAccessRoleArn': 'string',
                'ExternalTableDefinition': 'string',
                'CsvRowDelimiter': 'string',
                'CsvDelimiter': 'string',
                'BucketFolder': 'string',
                'BucketName': 'string',
                'CompressionType': 'none'|'gzip',
                'EncryptionMode': 'sse-s3'|'sse-kms',
                'ServerSideEncryptionKmsKeyId': 'string',
                'DataFormat': 'csv'|'parquet',
                'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
                'DictPageSizeLimit': 123,
                'RowGroupLength': 123,
                'DataPageSize': 123,
                'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
                'EnableStatistics': True|False,
                'IncludeOpForFullLoad': True|False,
                'CdcInsertsOnly': True|False,
                'TimestampColumnName': 'string',
                'ParquetTimestampInMillisecond': True|False,
                'CdcInsertsAndUpdates': True|False
            },
            'DmsTransferSettings': {
                'ServiceAccessRoleArn': 'string',
                'BucketName': 'string'
            },
            'MongoDbSettings': {
                'Username': 'string',
                'Password': 'string',
                'ServerName': 'string',
                'Port': 123,
                'DatabaseName': 'string',
                'AuthType': 'no'|'password',
                'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                'NestingLevel': 'none'|'one',
                'ExtractDocId': 'string',
                'DocsToInvestigate': 'string',
                'AuthSource': 'string',
                'KmsKeyId': 'string'
            },
            'KinesisSettings': {
                'StreamArn': 'string',
                'MessageFormat': 'json'|'json-unformatted',
                'ServiceAccessRoleArn': 'string',
                'IncludeTransactionDetails': True|False,
                'IncludePartitionValue': True|False,
                'PartitionIncludeSchemaTable': True|False,
                'IncludeTableAlterOperations': True|False,
                'IncludeControlDetails': True|False
            },
            'KafkaSettings': {
                'Broker': 'string',
                'Topic': 'string'
            },
            'ElasticsearchSettings': {
                'ServiceAccessRoleArn': 'string',
                'EndpointUri': 'string',
                'FullLoadErrorPercentage': 123,
                'ErrorRetryDuration': 123
            },
            'NeptuneSettings': {
                'ServiceAccessRoleArn': 'string',
                'S3BucketName': 'string',
                'S3BucketFolder': 'string',
                'ErrorRetryDuration': 123,
                'MaxFileSize': 123,
                'MaxRetryCount': 123,
                'IamAuthEnabled': True|False
            },
            'RedshiftSettings': {
                'AcceptAnyDate': True|False,
                'AfterConnectScript': 'string',
                'BucketFolder': 'string',
                'BucketName': 'string',
                'ConnectionTimeout': 123,
                'DatabaseName': 'string',
                'DateFormat': 'string',
                'EmptyAsNull': True|False,
                'EncryptionMode': 'sse-s3'|'sse-kms',
                'FileTransferUploadStreams': 123,
                'LoadTimeout': 123,
                'MaxFileSize': 123,
                'Password': 'string',
                'Port': 123,
                'RemoveQuotes': True|False,
                'ReplaceInvalidChars': 'string',
                'ReplaceChars': 'string',
                'ServerName': 'string',
                'ServiceAccessRoleArn': 'string',
                'ServerSideEncryptionKmsKeyId': 'string',
                'TimeFormat': 'string',
                'TrimBlanks': True|False,
                'TruncateColumns': True|False,
                'Username': 'string',
                'WriteBufferSize': 123
            }
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

Endpoints (list) --
Endpoint description.

(dict) --
Describes an endpoint of a database instance in response to operations such as the following:

CreateEndpoint
DescribeEndpoint
DescribeEndpointTypes
ModifyEndpoint


EndpointIdentifier (string) --
The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can\'t end with a hyphen or contain two consecutive hyphens.

EndpointType (string) --
The type of endpoint. Valid values are source and target .

EngineName (string) --
The database engine name. Valid values, depending on the EndpointType, include "mysql" , "oracle" , "postgres" , "mariadb" , "aurora" , "aurora-postgresql" , "redshift" , "s3" , "db2" , "azuredb" , "sybase" , "dynamodb" , "mongodb" , "kinesis" , "kafka" , "elasticsearch" , "documentdb" , and "sqlserver" .

EngineDisplayName (string) --
The expanded name for the engine name. For example, if the EngineName parameter is "aurora," this value would be "Amazon Aurora MySQL."

Username (string) --
The user name used to connect to the endpoint.

ServerName (string) --
The name of the server at the endpoint.

Port (integer) --
The port value used to access the endpoint.

DatabaseName (string) --
The name of the database at the endpoint.

ExtraConnectionAttributes (string) --
Additional connection attributes used to connect to the endpoint.

Status (string) --
The status of the endpoint.

KmsKeyId (string) --
An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint.
If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key.
AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.

EndpointArn (string) --
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

CertificateArn (string) --
The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

SslMode (string) --
The SSL mode used to connect to the endpoint. The default value is none .

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) used by the service access IAM role.

ExternalTableDefinition (string) --
The external table definition.

ExternalId (string) --
Value returned by a call to CreateEndpoint that can be used for cross-account validation. Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

DynamoDbSettings (dict) --
The settings for the target DynamoDB database. For more information, see the DynamoDBSettings structure.

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) used by the service access IAM role.



S3Settings (dict) --
The settings for the S3 target endpoint. For more information, see the S3Settings structure.

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) used by the service access IAM role.

ExternalTableDefinition (string) --
The external table definition.

CsvRowDelimiter (string) --
The delimiter used to separate rows in the source files. The default is a carriage return (\
 ).

CsvDelimiter (string) --
The delimiter used to separate columns in the source files. The default is a comma.

BucketFolder (string) --
An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in the path `` bucketFolder /schema_name /table_name /`` . If this parameter isn\'t specified, then the path used is `` schema_name /table_name /`` .

BucketName (string) --
The name of the S3 bucket.

CompressionType (string) --
An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the target files. Either set this parameter to NONE (the default) or don\'t use it to leave the files uncompressed. This parameter applies to both .csv and .parquet file formats.

EncryptionMode (string) --
The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either SSE_S3 (the default) or SSE_KMS . To use SSE_S3 , you need an AWS Identity and Access Management (IAM) role with permission to allow "arn:aws:s3:::dms-*" to use the following actions:

s3:CreateBucket
s3:ListBucket
s3:DeleteBucket
s3:GetBucketLocation
s3:GetObject
s3:PutObject
s3:DeleteObject
s3:GetObjectVersion
s3:GetBucketPolicy
s3:PutBucketPolicy
s3:DeleteBucketPolicy


ServerSideEncryptionKmsKeyId (string) --
If you are using SSE_KMS for the EncryptionMode , provide the AWS KMS key ID. The key that you use needs an attached policy that enables AWS Identity and Access Management (IAM) user permissions and allows use of the key.
Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier value --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value* ,BucketFolder=*value* ,BucketName=*value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

DataFormat (string) --
The format of the data that you want to use for output. You can choose one of the following:

csv : This is a row-based file format with comma-separated values (.csv).
parquet : Apache Parquet (.parquet) is a columnar storage file format that features efficient compression and provides faster query response.


EncodingType (string) --
The type of encoding you are using:

RLE_DICTIONARY uses a combination of bit-packing and run-length encoding to store repeated values more efficiently. This is the default.
PLAIN doesn\'t use encoding at all. Values are stored as they are.
PLAIN_DICTIONARY builds a dictionary of the values encountered in a given column. The dictionary is stored in a dictionary page for each column chunk.


DictPageSizeLimit (integer) --
The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds this, this column is stored using an encoding type of PLAIN . This parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to PLAIN encoding. This size is used for .parquet file format only.

RowGroupLength (integer) --
The number of rows in a row group. A smaller row group size provides faster reads. But as the number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows. This number is used for .parquet file format only.
If you choose a value larger than the maximum, RowGroupLength is set to the max row group length in bytes (64 * 1024 * 1024).

DataPageSize (integer) --
The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This number is used for .parquet file format only.

ParquetVersion (string) --
The version of the Apache Parquet format that you want to use: parquet_1_0 (the default) or parquet_2_0 .

EnableStatistics (boolean) --
A value that enables statistics for Parquet pages and row groups. Choose true to enable statistics, false to disable. Statistics include NULL , DISTINCT , MAX , and MIN values. This parameter defaults to true . This value is used for .parquet file format only.

IncludeOpForFullLoad (boolean) --
A value that enables a full load to write INSERT operations to the comma-separated value (.csv) output files only to indicate how the rows were added to the source database.

Note
AWS DMS supports the IncludeOpForFullLoad parameter in versions 3.1.4 and later.

For full load, records can only be inserted. By default (the false setting), no information is recorded in these output files for a full load to indicate that the rows were inserted at the source database. If IncludeOpForFullLoad is set to true or y , the INSERT is recorded as an I annotation in the first field of the .csv file. This allows the format of your target records from a full load to be consistent with the target records from a CDC load.

Note
This setting works together with the CdcInsertsOnly and the CdcInsertsAndUpdates parameters for output to .csv files only. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .


CdcInsertsOnly (boolean) --
A value that enables a change data capture (CDC) load to write only INSERT operations to .csv or columnar storage (.parquet) output files. By default (the false setting), the first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated, or deleted at the source database for a CDC load to the target.
If CdcInsertsOnly is set to true or y , only INSERTs from the source database are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded depends on the value of IncludeOpForFullLoad . If IncludeOpForFullLoad is set to true , the first field of every CDC record is set to I to indicate the INSERT operation at the source. If IncludeOpForFullLoad is set to false , every CDC record is written without a first field to indicate the INSERT operation at the source. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .

Note
AWS DMS supports the interaction described preceding between the CdcInsertsOnly and IncludeOpForFullLoad parameters in versions 3.1.4 and later.

CdcInsertsOnly and CdcInsertsAndUpdates can\'t both be set to true for the same endpoint. Set either CdcInsertsOnly or CdcInsertsAndUpdates to true for the same endpoint, but not both.



TimestampColumnName (string) --
A value that when nonblank causes AWS DMS to add a column with timestamp information to the endpoint data for an Amazon S3 target.

Note
AWS DMS supports the TimestampColumnName parameter in versions 3.1.4 and later.

DMS includes an additional STRING column in the .csv or .parquet object files of your migrated data when you set TimestampColumnName to a nonblank value.
For a full load, each row of this timestamp column contains a timestamp for when the data was transferred from the source to the target by DMS.
For a change data capture (CDC) load, each row of the timestamp column contains the timestamp for the commit of that row in the source database.
The string format for this timestamp column value is yyyy-MM-dd HH:mm:ss.SSSSSS . By default, the precision of this value is in microseconds. For a CDC load, the rounding of the precision depends on the commit timestamp supported by DMS for the source database.
When the AddColumnName parameter is set to true , DMS also includes a name for the timestamp column that you set with TimestampColumnName .

ParquetTimestampInMillisecond (boolean) --
A value that specifies the precision of any TIMESTAMP column values that are written to an Amazon S3 object file in .parquet format.

Note
AWS DMS supports the ParquetTimestampInMillisecond parameter in versions 3.1.4 and later.

When ParquetTimestampInMillisecond is set to true or y , AWS DMS writes all TIMESTAMP columns in a .parquet formatted file with millisecond precision. Otherwise, DMS writes them with microsecond precision.
Currently, Amazon Athena and AWS Glue can handle only millisecond precision for TIMESTAMP values. Set this parameter to true for S3 endpoint object files that are .parquet formatted only if you plan to query or process the data with Athena or AWS Glue.

Note
AWS DMS writes any TIMESTAMP column values written to an S3 file in .csv format with microsecond precision.
Setting ParquetTimestampInMillisecond has no effect on the string format of the timestamp column value that is inserted by setting the TimestampColumnName parameter.


CdcInsertsAndUpdates (boolean) --
A value that enables a change data capture (CDC) load to write INSERT and UPDATE operations to .csv or .parquet (columnar storage) output files. The default setting is false , but when CdcInsertsAndUpdates is set to true or y , INSERTs and UPDATEs from the source database are migrated to the .csv or .parquet file.
For .csv file format only, how these INSERTs and UPDATEs are recorded depends on the value of the IncludeOpForFullLoad parameter. If IncludeOpForFullLoad is set to true , the first field of every CDC record is set to either I or U to indicate INSERT and UPDATE operations at the source. But if IncludeOpForFullLoad is set to false , CDC records are written without an indication of INSERT or UPDATE operations at the source. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .

Note
AWS DMS supports the use of the CdcInsertsAndUpdates parameter in versions 3.3.1 and later.

CdcInsertsOnly and CdcInsertsAndUpdates can\'t both be set to true for the same endpoint. Set either CdcInsertsOnly or CdcInsertsAndUpdates to true for the same endpoint, but not both.





DmsTransferSettings (dict) --
The settings in JSON format for the DMS transfer type of source endpoint.
Possible settings include the following:

ServiceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.
BucketName - The name of the S3 bucket to use.
CompressionType - An optional parameter to use GZIP to compress the target files. To use GZIP, set this value to NONE (the default). To keep the files uncompressed, don\'t use this value.

Shorthand syntax for these settings is as follows: ServiceAccessRoleArn=string,BucketName=string,CompressionType=string
JSON syntax for these settings is as follows: { "ServiceAccessRoleArn": "string", "BucketName": "string", "CompressionType": "none"|"gzip" }

ServiceAccessRoleArn (string) --
The IAM role that has permission to access the Amazon S3 bucket.

BucketName (string) --
The name of the S3 bucket to use.



MongoDbSettings (dict) --
The settings for the MongoDB source endpoint. For more information, see the MongoDbSettings structure.

Username (string) --
The user name you use to access the MongoDB source endpoint.

Password (string) --
The password for the user account you use to access the MongoDB source endpoint.

ServerName (string) --
The name of the server on the MongoDB source endpoint.

Port (integer) --
The port value for the MongoDB source endpoint.

DatabaseName (string) --
The database name on the MongoDB source endpoint.

AuthType (string) --
The authentication type you use to access the MongoDB source endpoint.
Valid values: NO, PASSWORD
When NO is selected, user name and password parameters are not used and can be empty.

AuthMechanism (string) --
The authentication mechanism you use to access the MongoDB source endpoint.
Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1
DEFAULT \xe2\x80\x93 For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use SCRAM_SHA_1. This setting isn\'t used when authType=No.

NestingLevel (string) --
Specifies either document or table mode.
Valid values: NONE, ONE
Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

ExtractDocId (string) --
Specifies the document ID. Use this setting when NestingLevel is set to NONE.
Default value is false.

DocsToInvestigate (string) --
Indicates the number of documents to preview to determine the document organization. Use this setting when NestingLevel is set to ONE.
Must be a positive value greater than 0. Default value is 1000.

AuthSource (string) --
The MongoDB database name. This setting isn\'t used when authType=NO .
The default is admin.

KmsKeyId (string) --
The AWS KMS key identifier that is used to encrypt the content on the replication instance. If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.



KinesisSettings (dict) --
The settings for the Amazon Kinesis target endpoint. For more information, see the KinesisSettings structure.

StreamArn (string) --
The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

MessageFormat (string) --
The output format for the records created on the endpoint. The message format is JSON (default) or JSON_UNFORMATTED (a single line with no tab).

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) for the AWS Identity and Access Management (IAM) role that AWS DMS uses to write to the Kinesis data stream.

IncludeTransactionDetails (boolean) --
Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for transaction_id , previous transaction_id , and transaction_record_id (the record offset within a transaction). The default is False .

IncludePartitionValue (boolean) --
Shows the partition value within the Kinesis message output, unless the partition type is schema-table-type . The default is False .

PartitionIncludeSchemaTable (boolean) --
Prefixes schema and table names to partition values, when the partition type is primary-key-type . Doing this increases data distribution among Kinesis shards. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same shard, which causes throttling. The default is False .

IncludeTableAlterOperations (boolean) --
Includes any data definition language (DDL) operations that change the table in the control data, such as rename-table , drop-table , add-column , drop-column , and rename-column . The default is False .

IncludeControlDetails (boolean) --
Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output. The default is False .



KafkaSettings (dict) --
The settings for the Apache Kafka target endpoint. For more information, see the KafkaSettings structure.

Broker (string) --
The broker location and port of the Kafka broker that hosts your Kafka instance. Specify the broker in the form `` broker-hostname-or-ip :port `` . For example, "ec2-12-345-678-901.compute-1.amazonaws.com:2345" .

Topic (string) --
The topic to which you migrate the data. If you don\'t specify a topic, AWS DMS specifies "kafka-default-topic" as the migration topic.



ElasticsearchSettings (dict) --
The settings for the Elasticsearch source endpoint. For more information, see the ElasticsearchSettings structure.

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) used by service to access the IAM role.

EndpointUri (string) --
The endpoint for the Elasticsearch cluster.

FullLoadErrorPercentage (integer) --
The maximum percentage of records that can fail to be written before a full load operation stops.

ErrorRetryDuration (integer) --
The maximum number of seconds for which DMS retries failed API requests to the Elasticsearch cluster.



NeptuneSettings (dict) --
The settings for the MongoDB source endpoint. For more information, see the NeptuneSettings structure.

ServiceAccessRoleArn (string) --
The ARN of the service role you have created for the Neptune target endpoint. For more information, see https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.ServiceRole in the AWS Database Migration Service User Guide.

S3BucketName (string) --
The name of the S3 bucket for AWS DMS to temporarily store migrated graph data in CSV files before bulk-loading it to the Neptune target database. AWS DMS maps the SQL source data to graph data before storing it in these CSV files.

S3BucketFolder (string) --
A folder path where you where you want AWS DMS to store migrated graph data in the S3 bucket specified by S3BucketName

ErrorRetryDuration (integer) --
The number of milliseconds for AWS DMS to wait to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 250.

MaxFileSize (integer) --
The maximum size in KB of migrated graph data stored in a CSV file before AWS DMS bulk-loads the data to the Neptune target database. The default is 1048576 KB. If successful, AWS DMS clears the bucket, ready to store the next batch of migrated graph data.

MaxRetryCount (integer) --
The number of times for AWS DMS to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 5.

IamAuthEnabled (boolean) --
If you want IAM authorization enabled for this endpoint, set this parameter to true and attach the appropriate role policy document to your service role specified by ServiceAccessRoleArn . The default is false .



RedshiftSettings (dict) --
Settings for the Amazon Redshift endpoint.

AcceptAnyDate (boolean) --
A value that indicates to allow any date format, including invalid formats such as 00/00/00 00:00:00, to be loaded without generating an error. You can choose true or false (the default).
This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data doesn\'t match the DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

AfterConnectScript (string) --
Code to run after connecting. This parameter should contain the code itself, not the name of a file containing the code.

BucketFolder (string) --
The location where the comma-separated value (.csv) files are stored before being uploaded to the S3 bucket.

BucketName (string) --
The name of the S3 bucket you want to use

ConnectionTimeout (integer) --
A value that sets the amount of time to wait (in milliseconds) before timing out, beginning from when you initially establish a connection.

DatabaseName (string) --
The name of the Amazon Redshift data warehouse (service) that you are working with.

DateFormat (string) --
The date format that you are using. Valid values are auto (case-sensitive), your date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults to a format of \'YYYY-MM-DD\'. Using auto recognizes most strings, even some that aren\'t supported when you use a date format string.
If your date and time values use formats different from each other, set this to auto .

EmptyAsNull (boolean) --
A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL. A value of true sets empty CHAR and VARCHAR fields to null. The default is false .

EncryptionMode (string) --
The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either SSE_S3 (the default) or SSE_KMS . To use SSE_S3 , create an AWS Identity and Access Management (IAM) role with a policy that allows "arn:aws:s3:::*" to use the following actions: "s3:PutObject", "s3:ListBucket"

FileTransferUploadStreams (integer) --
The number of threads used to upload a single file. This parameter accepts a value from 1 through 64. It defaults to 10.

LoadTimeout (integer) --
The amount of time to wait (in milliseconds) before timing out, beginning from when you begin loading.

MaxFileSize (integer) --
The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

Password (string) --
The password for the user named in the username property.

Port (integer) --
The port number for Amazon Redshift. The default value is 5439.

RemoveQuotes (boolean) --
A value that specifies to remove surrounding quotation marks from strings in the incoming data. All characters within the quotation marks, including delimiters, are retained. Choose true to remove quotation marks. The default is false .

ReplaceInvalidChars (string) --
A list of characters that you want to replace. Use with ReplaceChars .

ReplaceChars (string) --
A value that specifies to replaces the invalid characters specified in ReplaceInvalidChars , substituting the specified characters instead. The default is "?" .

ServerName (string) --
The name of the Amazon Redshift cluster you are using.

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service.

ServerSideEncryptionKmsKeyId (string) --
The AWS KMS key ID. If you are using SSE_KMS for the EncryptionMode , provide this key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.

TimeFormat (string) --
The time format that you want to use. Valid values are auto (case-sensitive), \'timeformat_string\' , \'epochsecs\' , or \'epochmillisecs\' . It defaults to 10. Using auto recognizes most strings, even some that aren\'t supported when you use a time format string.
If your date and time values use formats different from each other, set this parameter to auto .

TrimBlanks (boolean) --
A value that specifies to remove the trailing white space characters from a VARCHAR string. This parameter applies only to columns with a VARCHAR data type. Choose true to remove unneeded white space. The default is false .

TruncateColumns (boolean) --
A value that specifies to truncate data in columns to the appropriate number of characters, so that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose true to truncate data. The default is false .

Username (string) --
An Amazon Redshift user name for a registered user.

WriteBufferSize (integer) --
The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The default is 1,024. Use this setting to tune performance.













Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault

Examples
Returns information about the endpoints for your account in the current region.
response = client.describe_endpoints(
    Filters=[
        {
            'Name': 'string',
            'Values': [
                'string',
                'string',
            ],
        },
    ],
    Marker='',
    MaxRecords=123,
)

print(response)


Expected Output:
{
    'Endpoints': [
    ],
    'Marker': '',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'Endpoints': [
            {
                'EndpointIdentifier': 'string',
                'EndpointType': 'source'|'target',
                'EngineName': 'string',
                'EngineDisplayName': 'string',
                'Username': 'string',
                'ServerName': 'string',
                'Port': 123,
                'DatabaseName': 'string',
                'ExtraConnectionAttributes': 'string',
                'Status': 'string',
                'KmsKeyId': 'string',
                'EndpointArn': 'string',
                'CertificateArn': 'string',
                'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
                'ServiceAccessRoleArn': 'string',
                'ExternalTableDefinition': 'string',
                'ExternalId': 'string',
                'DynamoDbSettings': {
                    'ServiceAccessRoleArn': 'string'
                },
                'S3Settings': {
                    'ServiceAccessRoleArn': 'string',
                    'ExternalTableDefinition': 'string',
                    'CsvRowDelimiter': 'string',
                    'CsvDelimiter': 'string',
                    'BucketFolder': 'string',
                    'BucketName': 'string',
                    'CompressionType': 'none'|'gzip',
                    'EncryptionMode': 'sse-s3'|'sse-kms',
                    'ServerSideEncryptionKmsKeyId': 'string',
                    'DataFormat': 'csv'|'parquet',
                    'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
                    'DictPageSizeLimit': 123,
                    'RowGroupLength': 123,
                    'DataPageSize': 123,
                    'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
                    'EnableStatistics': True|False,
                    'IncludeOpForFullLoad': True|False,
                    'CdcInsertsOnly': True|False,
                    'TimestampColumnName': 'string',
                    'ParquetTimestampInMillisecond': True|False,
                    'CdcInsertsAndUpdates': True|False
                },
                'DmsTransferSettings': {
                    'ServiceAccessRoleArn': 'string',
                    'BucketName': 'string'
                },
                'MongoDbSettings': {
                    'Username': 'string',
                    'Password': 'string',
                    'ServerName': 'string',
                    'Port': 123,
                    'DatabaseName': 'string',
                    'AuthType': 'no'|'password',
                    'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                    'NestingLevel': 'none'|'one',
                    'ExtractDocId': 'string',
                    'DocsToInvestigate': 'string',
                    'AuthSource': 'string',
                    'KmsKeyId': 'string'
                },
                'KinesisSettings': {
                    'StreamArn': 'string',
                    'MessageFormat': 'json'|'json-unformatted',
                    'ServiceAccessRoleArn': 'string',
                    'IncludeTransactionDetails': True|False,
                    'IncludePartitionValue': True|False,
                    'PartitionIncludeSchemaTable': True|False,
                    'IncludeTableAlterOperations': True|False,
                    'IncludeControlDetails': True|False
                },
                'KafkaSettings': {
                    'Broker': 'string',
                    'Topic': 'string'
                },
                'ElasticsearchSettings': {
                    'ServiceAccessRoleArn': 'string',
                    'EndpointUri': 'string',
                    'FullLoadErrorPercentage': 123,
                    'ErrorRetryDuration': 123
                },
                'NeptuneSettings': {
                    'ServiceAccessRoleArn': 'string',
                    'S3BucketName': 'string',
                    'S3BucketFolder': 'string',
                    'ErrorRetryDuration': 123,
                    'MaxFileSize': 123,
                    'MaxRetryCount': 123,
                    'IamAuthEnabled': True|False
                },
                'RedshiftSettings': {
                    'AcceptAnyDate': True|False,
                    'AfterConnectScript': 'string',
                    'BucketFolder': 'string',
                    'BucketName': 'string',
                    'ConnectionTimeout': 123,
                    'DatabaseName': 'string',
                    'DateFormat': 'string',
                    'EmptyAsNull': True|False,
                    'EncryptionMode': 'sse-s3'|'sse-kms',
                    'FileTransferUploadStreams': 123,
                    'LoadTimeout': 123,
                    'MaxFileSize': 123,
                    'Password': 'string',
                    'Port': 123,
                    'RemoveQuotes': True|False,
                    'ReplaceInvalidChars': 'string',
                    'ReplaceChars': 'string',
                    'ServerName': 'string',
                    'ServiceAccessRoleArn': 'string',
                    'ServerSideEncryptionKmsKeyId': 'string',
                    'TimeFormat': 'string',
                    'TrimBlanks': True|False,
                    'TruncateColumns': True|False,
                    'Username': 'string',
                    'WriteBufferSize': 123
                }
            },
        ]
    }
    
    
    :returns: 
    CreateEndpoint
    DescribeEndpoint
    DescribeEndpointTypes
    ModifyEndpoint
    
    """
    pass

def describe_event_categories(SourceType=None, Filters=None):
    """
    Lists categories for all event source types, or, if specified, for a specified source type. You can see a list of the event categories and source types in Working with Events and Notifications in the AWS Database Migration Service User Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_event_categories(
        SourceType='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type SourceType: string
    :param SourceType: The type of AWS DMS resource that generates events.\nValid values: replication-instance | replication-task\n

    :type Filters: list
    :param Filters: Filters applied to the action.\n\n(dict) --Identifies the name and value of a source filter object used to limit the number and type of records transferred from your source to your target.\n\nName (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EventCategoryGroupList': [
        {
            'SourceType': 'string',
            'EventCategories': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --

EventCategoryGroupList (list) --
A list of event categories.

(dict) --
Lists categories of events subscribed to, and generated by, the applicable AWS DMS resource type.

SourceType (string) --
The type of AWS DMS resource that generates events.
Valid values: replication-instance | replication-server | security-group | replication-task

EventCategories (list) --
A list of event categories from a source type that you\'ve chosen.

(string) --













    :return: {
        'EventCategoryGroupList': [
            {
                'SourceType': 'string',
                'EventCategories': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_event_subscriptions(SubscriptionName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Lists all the event subscriptions for a customer account. The description of a subscription includes SubscriptionName , SNSTopicARN , CustomerID , SourceType , SourceID , CreationTime , and Status .
    If you specify SubscriptionName , this action lists the description for that subscription.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_event_subscriptions(
        SubscriptionName='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: The name of the AWS DMS event subscription to be described.

    :type Filters: list
    :param Filters: Filters applied to the action.\n\n(dict) --Identifies the name and value of a source filter object used to limit the number and type of records transferred from your source to your target.\n\nName (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'EventSubscriptionsList': [
        {
            'CustomerAwsId': 'string',
            'CustSubscriptionId': 'string',
            'SnsTopicArn': 'string',
            'Status': 'string',
            'SubscriptionCreationTime': 'string',
            'SourceType': 'string',
            'SourceIdsList': [
                'string',
            ],
            'EventCategoriesList': [
                'string',
            ],
            'Enabled': True|False
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

EventSubscriptionsList (list) --
A list of event subscriptions.

(dict) --
Describes an event notification subscription created by the CreateEventSubscription operation.

CustomerAwsId (string) --
The AWS customer account associated with the AWS DMS event notification subscription.

CustSubscriptionId (string) --
The AWS DMS event notification subscription Id.

SnsTopicArn (string) --
The topic ARN of the AWS DMS event notification subscription.

Status (string) --
The status of the AWS DMS event notification subscription.
Constraints:
Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
The status "no-permission" indicates that AWS DMS no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.

SubscriptionCreationTime (string) --
The time the RDS event notification subscription was created.

SourceType (string) --
The type of AWS DMS resource that generates events.
Valid values: replication-instance | replication-server | security-group | replication-task

SourceIdsList (list) --
A list of source Ids for the event subscription.

(string) --


EventCategoriesList (list) --
A lists of event categories.

(string) --


Enabled (boolean) --
Boolean value that indicates if the event subscription is enabled.











Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault


    :return: {
        'Marker': 'string',
        'EventSubscriptionsList': [
            {
                'CustomerAwsId': 'string',
                'CustSubscriptionId': 'string',
                'SnsTopicArn': 'string',
                'Status': 'string',
                'SubscriptionCreationTime': 'string',
                'SourceType': 'string',
                'SourceIdsList': [
                    'string',
                ],
                'EventCategoriesList': [
                    'string',
                ],
                'Enabled': True|False
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_events(SourceIdentifier=None, SourceType=None, StartTime=None, EndTime=None, Duration=None, EventCategories=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Lists events for a given source identifier and source type. You can also specify a start and end time. For more information on AWS DMS events, see Working with Events and Notifications in the AWS Database Migration User Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_events(
        SourceIdentifier='string',
        SourceType='replication-instance',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Duration=123,
        EventCategories=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type SourceIdentifier: string
    :param SourceIdentifier: The identifier of an event source.

    :type SourceType: string
    :param SourceType: The type of AWS DMS resource that generates events.\nValid values: replication-instance | replication-task\n

    :type StartTime: datetime
    :param StartTime: The start time for the events to be listed.

    :type EndTime: datetime
    :param EndTime: The end time for the events to be listed.

    :type Duration: integer
    :param Duration: The duration of the events to be listed.

    :type EventCategories: list
    :param EventCategories: A list of event categories for the source type that you\'ve chosen.\n\n(string) --\n\n

    :type Filters: list
    :param Filters: Filters applied to the action.\n\n(dict) --Identifies the name and value of a source filter object used to limit the number and type of records transferred from your source to your target.\n\nName (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'Events': [
        {
            'SourceIdentifier': 'string',
            'SourceType': 'replication-instance',
            'Message': 'string',
            'EventCategories': [
                'string',
            ],
            'Date': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

Events (list) --
The events described.

(dict) --
Describes an identifiable significant activity that affects a replication instance or task. This object can provide the message, the available event categories, the date and source of the event, and the AWS DMS resource type.

SourceIdentifier (string) --
The identifier of an event source.

SourceType (string) --
The type of AWS DMS resource that generates events.
Valid values: replication-instance | endpoint | replication-task

Message (string) --
The event message.

EventCategories (list) --
The event categories available for the specified source type.

(string) --


Date (datetime) --
The date of the event.












    :return: {
        'Marker': 'string',
        'Events': [
            {
                'SourceIdentifier': 'string',
                'SourceType': 'replication-instance',
                'Message': 'string',
                'EventCategories': [
                    'string',
                ],
                'Date': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_orderable_replication_instances(MaxRecords=None, Marker=None):
    """
    Returns information about the replication instance types that can be created in the specified region.
    See also: AWS API Documentation
    
    Examples
    Returns information about the replication instance types that can be created in the specified region.
    Expected Output:
    
    :example: response = client.describe_orderable_replication_instances(
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'OrderableReplicationInstances': [
        {
            'EngineVersion': 'string',
            'ReplicationInstanceClass': 'string',
            'StorageType': 'string',
            'MinAllocatedStorage': 123,
            'MaxAllocatedStorage': 123,
            'DefaultAllocatedStorage': 123,
            'IncludedAllocatedStorage': 123,
            'AvailabilityZones': [
                'string',
            ],
            'ReleaseStatus': 'beta'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

OrderableReplicationInstances (list) --
The order-able replication instances available.

(dict) --
In response to the DescribeOrderableReplicationInstances operation, this object describes an available replication instance. This description includes the replication instance\'s type, engine version, and allocated storage.

EngineVersion (string) --
The version of the replication engine.

ReplicationInstanceClass (string) --
The compute and memory capacity of the replication instance.
Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge

StorageType (string) --
The type of storage used by the replication instance.

MinAllocatedStorage (integer) --
The minimum amount of storage (in gigabytes) that can be allocated for the replication instance.

MaxAllocatedStorage (integer) --
The minimum amount of storage (in gigabytes) that can be allocated for the replication instance.

DefaultAllocatedStorage (integer) --
The default amount of storage (in gigabytes) that is allocated for the replication instance.

IncludedAllocatedStorage (integer) --
The amount of storage (in gigabytes) that is allocated for the replication instance.

AvailabilityZones (list) --
List of Availability Zones for this replication instance.

(string) --


ReleaseStatus (string) --
The value returned when the specified EngineVersion of the replication instance is in Beta or test mode. This indicates some features might not work as expected.

Note
AWS DMS supports the ReleaseStatus parameter in versions 3.1.4 and later.






Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .







Examples
Returns information about the replication instance types that can be created in the specified region.
response = client.describe_orderable_replication_instances(
    Marker='',
    MaxRecords=123,
)

print(response)


Expected Output:
{
    'Marker': '',
    'OrderableReplicationInstances': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'OrderableReplicationInstances': [
            {
                'EngineVersion': 'string',
                'ReplicationInstanceClass': 'string',
                'StorageType': 'string',
                'MinAllocatedStorage': 123,
                'MaxAllocatedStorage': 123,
                'DefaultAllocatedStorage': 123,
                'IncludedAllocatedStorage': 123,
                'AvailabilityZones': [
                    'string',
                ],
                'ReleaseStatus': 'beta'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_pending_maintenance_actions(ReplicationInstanceArn=None, Filters=None, Marker=None, MaxRecords=None):
    """
    For internal use only
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_pending_maintenance_actions(
        ReplicationInstanceArn='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        Marker='string',
        MaxRecords=123
    )
    
    
    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: The Amazon Resource Name (ARN) of the replication instance.

    :type Filters: list
    :param Filters: \n(dict) --Identifies the name and value of a source filter object used to limit the number and type of records transferred from your source to your target.\n\nName (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\n\n\n\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PendingMaintenanceActions': [
        {
            'ResourceIdentifier': 'string',
            'PendingMaintenanceActionDetails': [
                {
                    'Action': 'string',
                    'AutoAppliedAfterDate': datetime(2015, 1, 1),
                    'ForcedApplyDate': datetime(2015, 1, 1),
                    'OptInStatus': 'string',
                    'CurrentApplyDate': datetime(2015, 1, 1),
                    'Description': 'string'
                },
            ]
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

PendingMaintenanceActions (list) --
The pending maintenance action.

(dict) --
Identifies an AWS DMS resource and any pending actions for it.

ResourceIdentifier (string) --
The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action applies to. For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) for AWS DMS in the DMS documentation.

PendingMaintenanceActionDetails (list) --
Detailed information about the pending maintenance action.

(dict) --
Describes a maintenance action pending for an AWS DMS resource, including when and how it will be applied. This data type is a response element to the DescribePendingMaintenanceActions operation.

Action (string) --
The type of pending maintenance action that is available for the resource.

AutoAppliedAfterDate (datetime) --
The date of the maintenance window when the action is to be applied. The maintenance action is applied to the resource during its first maintenance window after this date. If this date is specified, any next-maintenance opt-in requests are ignored.

ForcedApplyDate (datetime) --
The date when the maintenance action will be automatically applied. The maintenance action is applied to the resource on this date regardless of the maintenance window for the resource. If this date is specified, any immediate opt-in requests are ignored.

OptInStatus (string) --
The type of opt-in request that has been received for the resource.

CurrentApplyDate (datetime) --
The effective date when the pending maintenance action will be applied to the resource. This date takes into account opt-in requests received from the ApplyPendingMaintenanceAction API operation, and also the AutoAppliedAfterDate and ForcedApplyDate parameter values. This value is blank if an opt-in request has not been received and nothing has been specified for AutoAppliedAfterDate or ForcedApplyDate .

Description (string) --
A description providing more detail about the maintenance action.









Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .







Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault


    :return: {
        'PendingMaintenanceActions': [
            {
                'ResourceIdentifier': 'string',
                'PendingMaintenanceActionDetails': [
                    {
                        'Action': 'string',
                        'AutoAppliedAfterDate': datetime(2015, 1, 1),
                        'ForcedApplyDate': datetime(2015, 1, 1),
                        'OptInStatus': 'string',
                        'CurrentApplyDate': datetime(2015, 1, 1),
                        'Description': 'string'
                    },
                ]
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    
    """
    pass

def describe_refresh_schemas_status(EndpointArn=None):
    """
    Returns the status of the RefreshSchemas operation.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns the status of the refresh-schemas operation.
    Expected Output:
    
    :example: response = client.describe_refresh_schemas_status(
        EndpointArn='string'
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]\nThe Amazon Resource Name (ARN) string that uniquely identifies the endpoint.\n

    :rtype: dict
ReturnsResponse Syntax{
    'RefreshSchemasStatus': {
        'EndpointArn': 'string',
        'ReplicationInstanceArn': 'string',
        'Status': 'successful'|'failed'|'refreshing',
        'LastRefreshDate': datetime(2015, 1, 1),
        'LastFailureMessage': 'string'
    }
}


Response Structure

(dict) --
RefreshSchemasStatus (dict) --The status of the schema.

EndpointArn (string) --The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

ReplicationInstanceArn (string) --The Amazon Resource Name (ARN) of the replication instance.

Status (string) --The status of the schema.

LastRefreshDate (datetime) --The date the schema was last refreshed.

LastFailureMessage (string) --The last failure message for the schema.








Exceptions

DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault

Examples
Returns the status of the refresh-schemas operation.
response = client.describe_refresh_schemas_status(
    EndpointArn='',
)

print(response)


Expected Output:
{
    'RefreshSchemasStatus': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'RefreshSchemasStatus': {
            'EndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'Status': 'successful'|'failed'|'refreshing',
            'LastRefreshDate': datetime(2015, 1, 1),
            'LastFailureMessage': 'string'
        }
    }
    
    
    """
    pass

def describe_replication_instance_task_logs(ReplicationInstanceArn=None, MaxRecords=None, Marker=None):
    """
    Returns information about the task logs for the specified task.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_replication_instance_task_logs(
        ReplicationInstanceArn='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the replication instance.\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationInstanceArn': 'string',
    'ReplicationInstanceTaskLogs': [
        {
            'ReplicationTaskName': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationInstanceTaskLogSize': 123
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

ReplicationInstanceArn (string) --
The Amazon Resource Name (ARN) of the replication instance.

ReplicationInstanceTaskLogs (list) --
An array of replication task log metadata. Each member of the array contains the replication task name, ARN, and task log size (in bytes).

(dict) --
Contains metadata for a replication instance task log.

ReplicationTaskName (string) --
The name of the replication task.

ReplicationTaskArn (string) --
The Amazon Resource Name (ARN) of the replication task.

ReplicationInstanceTaskLogSize (integer) --
The size, in bytes, of the replication task log.





Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .







Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault


    :return: {
        'ReplicationInstanceArn': 'string',
        'ReplicationInstanceTaskLogs': [
            {
                'ReplicationTaskName': 'string',
                'ReplicationTaskArn': 'string',
                'ReplicationInstanceTaskLogSize': 123
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
    
    """
    pass

def describe_replication_instances(Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about replication instances for your account in the current region.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns the status of the refresh-schemas operation.
    Expected Output:
    
    :example: response = client.describe_replication_instances(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type Filters: list
    :param Filters: Filters applied to the describe action.\nValid filter names: replication-instance-arn | replication-instance-id | replication-instance-class | engine-version\n\n(dict) --Identifies the name and value of a source filter object used to limit the number and type of records transferred from your source to your target.\n\nName (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'ReplicationInstances': [
        {
            'ReplicationInstanceIdentifier': 'string',
            'ReplicationInstanceClass': 'string',
            'ReplicationInstanceStatus': 'string',
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'ReplicationSubnetGroup': {
                'ReplicationSubnetGroupIdentifier': 'string',
                'ReplicationSubnetGroupDescription': 'string',
                'VpcId': 'string',
                'SubnetGroupStatus': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        },
                        'SubnetStatus': 'string'
                    },
                ]
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'ReplicationInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string'
            },
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'KmsKeyId': 'string',
            'ReplicationInstanceArn': 'string',
            'ReplicationInstancePublicIpAddress': 'string',
            'ReplicationInstancePrivateIpAddress': 'string',
            'ReplicationInstancePublicIpAddresses': [
                'string',
            ],
            'ReplicationInstancePrivateIpAddresses': [
                'string',
            ],
            'PubliclyAccessible': True|False,
            'SecondaryAvailabilityZone': 'string',
            'FreeUntil': datetime(2015, 1, 1),
            'DnsNameServers': 'string'
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

ReplicationInstances (list) --
The replication instances described.

(dict) --
Provides information that defines a replication instance.

ReplicationInstanceIdentifier (string) --
The replication instance identifier. This parameter is stored as a lowercase string.
Constraints:

Must contain from 1 to 63 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.

Example: myrepinstance

ReplicationInstanceClass (string) --
The compute and memory capacity of the replication instance.
Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge

ReplicationInstanceStatus (string) --
The status of the replication instance.

AllocatedStorage (integer) --
The amount of storage (in gigabytes) that is allocated for the replication instance.

InstanceCreateTime (datetime) --
The time the replication instance was created.

VpcSecurityGroups (list) --
The VPC security group for the instance.

(dict) --
Describes status of a security group associated with the virtual private cloud hosting your replication and DB instances.

VpcSecurityGroupId (string) --
The VPC security group Id.

Status (string) --
The status of the VPC security group.





AvailabilityZone (string) --
The Availability Zone for the instance.

ReplicationSubnetGroup (dict) --
The subnet group for the replication instance.

ReplicationSubnetGroupIdentifier (string) --
The identifier of the replication instance subnet group.

ReplicationSubnetGroupDescription (string) --
A description for the replication subnet group.

VpcId (string) --
The ID of the VPC.

SubnetGroupStatus (string) --
The status of the subnet group.

Subnets (list) --
The subnets that are in the subnet group.

(dict) --
In response to a request by the DescribeReplicationSubnetGroup operation, this object identifies a subnet by its given Availability Zone, subnet identifier, and status.

SubnetIdentifier (string) --
The subnet identifier.

SubnetAvailabilityZone (dict) --
The Availability Zone of the subnet.

Name (string) --
The name of the Availability Zone.



SubnetStatus (string) --
The status of the subnet.







PreferredMaintenanceWindow (string) --
The maintenance window times for the replication instance.

PendingModifiedValues (dict) --
The pending modification values.

ReplicationInstanceClass (string) --
The compute and memory capacity of the replication instance.
Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge

AllocatedStorage (integer) --
The amount of storage (in gigabytes) that is allocated for the replication instance.

MultiAZ (boolean) --
Specifies whether the replication instance is a Multi-AZ deployment. You can\'t set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .

EngineVersion (string) --
The engine version number of the replication instance.



MultiAZ (boolean) --
Specifies whether the replication instance is a Multi-AZ deployment. You can\'t set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .

EngineVersion (string) --
The engine version number of the replication instance.

AutoMinorVersionUpgrade (boolean) --
Boolean value indicating if minor version upgrades will be automatically applied to the instance.

KmsKeyId (string) --
An AWS KMS key identifier that is used to encrypt the data on the replication instance.
If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key.
AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.

ReplicationInstanceArn (string) --
The Amazon Resource Name (ARN) of the replication instance.

ReplicationInstancePublicIpAddress (string) --
The public IP address of the replication instance.

ReplicationInstancePrivateIpAddress (string) --
The private IP address of the replication instance.

ReplicationInstancePublicIpAddresses (list) --
One or more public IP addresses for the replication instance.

(string) --


ReplicationInstancePrivateIpAddresses (list) --
One or more private IP addresses for the replication instance.

(string) --


PubliclyAccessible (boolean) --
Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address. The default value is true .

SecondaryAvailabilityZone (string) --
The Availability Zone of the standby replication instance in a Multi-AZ deployment.

FreeUntil (datetime) --
The expiration date of the free replication instance that is part of the Free DMS program.

DnsNameServers (string) --
The DNS name servers for the replication instance.











Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault

Examples
Returns the status of the refresh-schemas operation.
response = client.describe_replication_instances(
    Filters=[
        {
            'Name': 'string',
            'Values': [
                'string',
                'string',
            ],
        },
    ],
    Marker='',
    MaxRecords=123,
)

print(response)


Expected Output:
{
    'Marker': '',
    'ReplicationInstances': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'ReplicationInstances': [
            {
                'ReplicationInstanceIdentifier': 'string',
                'ReplicationInstanceClass': 'string',
                'ReplicationInstanceStatus': 'string',
                'AllocatedStorage': 123,
                'InstanceCreateTime': datetime(2015, 1, 1),
                'VpcSecurityGroups': [
                    {
                        'VpcSecurityGroupId': 'string',
                        'Status': 'string'
                    },
                ],
                'AvailabilityZone': 'string',
                'ReplicationSubnetGroup': {
                    'ReplicationSubnetGroupIdentifier': 'string',
                    'ReplicationSubnetGroupDescription': 'string',
                    'VpcId': 'string',
                    'SubnetGroupStatus': 'string',
                    'Subnets': [
                        {
                            'SubnetIdentifier': 'string',
                            'SubnetAvailabilityZone': {
                                'Name': 'string'
                            },
                            'SubnetStatus': 'string'
                        },
                    ]
                },
                'PreferredMaintenanceWindow': 'string',
                'PendingModifiedValues': {
                    'ReplicationInstanceClass': 'string',
                    'AllocatedStorage': 123,
                    'MultiAZ': True|False,
                    'EngineVersion': 'string'
                },
                'MultiAZ': True|False,
                'EngineVersion': 'string',
                'AutoMinorVersionUpgrade': True|False,
                'KmsKeyId': 'string',
                'ReplicationInstanceArn': 'string',
                'ReplicationInstancePublicIpAddress': 'string',
                'ReplicationInstancePrivateIpAddress': 'string',
                'ReplicationInstancePublicIpAddresses': [
                    'string',
                ],
                'ReplicationInstancePrivateIpAddresses': [
                    'string',
                ],
                'PubliclyAccessible': True|False,
                'SecondaryAvailabilityZone': 'string',
                'FreeUntil': datetime(2015, 1, 1),
                'DnsNameServers': 'string'
            },
        ]
    }
    
    
    :returns: 
    Must contain from 1 to 63 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def describe_replication_subnet_groups(Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about the replication subnet groups.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns information about the replication subnet groups.
    Expected Output:
    
    :example: response = client.describe_replication_subnet_groups(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type Filters: list
    :param Filters: Filters applied to the describe action.\nValid filter names: replication-subnet-group-id\n\n(dict) --Identifies the name and value of a source filter object used to limit the number and type of records transferred from your source to your target.\n\nName (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'ReplicationSubnetGroups': [
        {
            'ReplicationSubnetGroupIdentifier': 'string',
            'ReplicationSubnetGroupDescription': 'string',
            'VpcId': 'string',
            'SubnetGroupStatus': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': {
                        'Name': 'string'
                    },
                    'SubnetStatus': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

ReplicationSubnetGroups (list) --
A description of the replication subnet groups.

(dict) --
Describes a subnet group in response to a request by the DescribeReplicationSubnetGroup operation.

ReplicationSubnetGroupIdentifier (string) --
The identifier of the replication instance subnet group.

ReplicationSubnetGroupDescription (string) --
A description for the replication subnet group.

VpcId (string) --
The ID of the VPC.

SubnetGroupStatus (string) --
The status of the subnet group.

Subnets (list) --
The subnets that are in the subnet group.

(dict) --
In response to a request by the DescribeReplicationSubnetGroup operation, this object identifies a subnet by its given Availability Zone, subnet identifier, and status.

SubnetIdentifier (string) --
The subnet identifier.

SubnetAvailabilityZone (dict) --
The Availability Zone of the subnet.

Name (string) --
The name of the Availability Zone.



SubnetStatus (string) --
The status of the subnet.















Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault

Examples
Returns information about the replication subnet groups.
response = client.describe_replication_subnet_groups(
    Filters=[
        {
            'Name': 'string',
            'Values': [
                'string',
                'string',
            ],
        },
    ],
    Marker='',
    MaxRecords=123,
)

print(response)


Expected Output:
{
    'Marker': '',
    'ReplicationSubnetGroups': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'ReplicationSubnetGroups': [
            {
                'ReplicationSubnetGroupIdentifier': 'string',
                'ReplicationSubnetGroupDescription': 'string',
                'VpcId': 'string',
                'SubnetGroupStatus': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        },
                        'SubnetStatus': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    
    """
    pass

def describe_replication_task_assessment_results(ReplicationTaskArn=None, MaxRecords=None, Marker=None):
    """
    Returns the task assessment results from Amazon S3. This action always returns the latest results.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_replication_task_assessment_results(
        ReplicationTaskArn='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: The Amazon Resource Name (ARN) string that uniquely identifies the task. When this input parameter is specified, the API returns only one result and ignore the values of the MaxRecords and Marker parameters.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'BucketName': 'string',
    'ReplicationTaskAssessmentResults': [
        {
            'ReplicationTaskIdentifier': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationTaskLastAssessmentDate': datetime(2015, 1, 1),
            'AssessmentStatus': 'string',
            'AssessmentResultsFile': 'string',
            'AssessmentResults': 'string',
            'S3ObjectUrl': 'string'
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

BucketName (string) --

The Amazon S3 bucket where the task assessment report is located.


ReplicationTaskAssessmentResults (list) --
The task assessment report.

(dict) --
The task assessment report in JSON format.

ReplicationTaskIdentifier (string) --
The replication task identifier of the task on which the task assessment was run.

ReplicationTaskArn (string) --
The Amazon Resource Name (ARN) of the replication task.

ReplicationTaskLastAssessmentDate (datetime) --
The date the task assessment was completed.

AssessmentStatus (string) --
The status of the task assessment.

AssessmentResultsFile (string) --
The file containing the results of the task assessment.

AssessmentResults (string) --
The task assessment results in JSON format.

S3ObjectUrl (string) --
The URL of the S3 object containing the task assessment results.











Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault


    :return: {
        'Marker': 'string',
        'BucketName': 'string',
        'ReplicationTaskAssessmentResults': [
            {
                'ReplicationTaskIdentifier': 'string',
                'ReplicationTaskArn': 'string',
                'ReplicationTaskLastAssessmentDate': datetime(2015, 1, 1),
                'AssessmentStatus': 'string',
                'AssessmentResultsFile': 'string',
                'AssessmentResults': 'string',
                'S3ObjectUrl': 'string'
            },
        ]
    }
    
    
    :returns: 
    The Amazon S3 bucket where the task assessment report is located.
    
    """
    pass

def describe_replication_tasks(Filters=None, MaxRecords=None, Marker=None, WithoutSettings=None):
    """
    Returns information about replication tasks for your account in the current region.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns information about replication tasks for your account in the current region.
    Expected Output:
    
    :example: response = client.describe_replication_tasks(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string',
        WithoutSettings=True|False
    )
    
    
    :type Filters: list
    :param Filters: Filters applied to the describe action.\nValid filter names: replication-task-arn | replication-task-id | migration-type | endpoint-arn | replication-instance-arn\n\n(dict) --Identifies the name and value of a source filter object used to limit the number and type of records transferred from your source to your target.\n\nName (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type WithoutSettings: boolean
    :param WithoutSettings: An option to set to avoid returning information about settings. Use this to reduce overhead when setting information is too large. To use this option, choose true ; otherwise, choose false (the default).

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'ReplicationTasks': [
        {
            'ReplicationTaskIdentifier': 'string',
            'SourceEndpointArn': 'string',
            'TargetEndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
            'TableMappings': 'string',
            'ReplicationTaskSettings': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'StopReason': 'string',
            'ReplicationTaskCreationDate': datetime(2015, 1, 1),
            'ReplicationTaskStartDate': datetime(2015, 1, 1),
            'CdcStartPosition': 'string',
            'CdcStopPosition': 'string',
            'RecoveryCheckpoint': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationTaskStats': {
                'FullLoadProgressPercent': 123,
                'ElapsedTimeMillis': 123,
                'TablesLoaded': 123,
                'TablesLoading': 123,
                'TablesQueued': 123,
                'TablesErrored': 123,
                'FreshStartDate': datetime(2015, 1, 1),
                'StartDate': datetime(2015, 1, 1),
                'StopDate': datetime(2015, 1, 1),
                'FullLoadStartDate': datetime(2015, 1, 1),
                'FullLoadFinishDate': datetime(2015, 1, 1)
            },
            'TaskData': 'string'
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

ReplicationTasks (list) --
A description of the replication tasks.

(dict) --
Provides information that describes a replication task created by the CreateReplicationTask operation.

ReplicationTaskIdentifier (string) --
The user-assigned replication task identifier or name.
Constraints:

Must contain from 1 to 255 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.


SourceEndpointArn (string) --
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

TargetEndpointArn (string) --
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

ReplicationInstanceArn (string) --
The Amazon Resource Name (ARN) of the replication instance.

MigrationType (string) --
The type of migration.

TableMappings (string) --
Table mappings specified in the task.

ReplicationTaskSettings (string) --
The settings for the replication task.

Status (string) --
The status of the replication task.

LastFailureMessage (string) --
The last error (failure) message generated for the replication instance.

StopReason (string) --
The reason the replication task was stopped.

ReplicationTaskCreationDate (datetime) --
The date the replication task was created.

ReplicationTaskStartDate (datetime) --
The date the replication task is scheduled to start.

CdcStartPosition (string) --
Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want the CDC operation to start. Specifying both values results in an error.
The value can be in date, checkpoint, or LSN/SCN format.
Date Example: --cdc-start-position \xe2\x80\x9c2018-03-08T12:12:12\xe2\x80\x9d
Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
LSN Example: --cdc-start-position \xe2\x80\x9cmysql-bin-changelog.000024:373\xe2\x80\x9d

CdcStopPosition (string) --
Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
Server time example: --cdc-stop-position \xe2\x80\x9cserver_time:3018-02-09T12:12:12\xe2\x80\x9d
Commit time example: --cdc-stop-position \xe2\x80\x9ccommit_time: 3018-02-09T12:12:12 \xe2\x80\x9c

RecoveryCheckpoint (string) --
Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the CdcStartPosition parameter to start a CDC operation that begins at that checkpoint.

ReplicationTaskArn (string) --
The Amazon Resource Name (ARN) of the replication task.

ReplicationTaskStats (dict) --
The statistics for the task, including elapsed time, tables loaded, and table errors.

FullLoadProgressPercent (integer) --
The percent complete for the full load migration task.

ElapsedTimeMillis (integer) --
The elapsed time of the task, in milliseconds.

TablesLoaded (integer) --
The number of tables loaded for this task.

TablesLoading (integer) --
The number of tables currently loading for this task.

TablesQueued (integer) --
The number of tables queued for this task.

TablesErrored (integer) --
The number of errors that have occurred during this task.

FreshStartDate (datetime) --
The date the replication task was started either with a fresh start or a target reload.

StartDate (datetime) --
The date the replication task was started either with a fresh start or a resume. For more information, see StartReplicationTaskType .

StopDate (datetime) --
The date the replication task was stopped.

FullLoadStartDate (datetime) --
The date the replication task full load was started.

FullLoadFinishDate (datetime) --
The date the replication task full load was completed.



TaskData (string) --
Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see Specifying Supplemental Data for Task Settings in the AWS Database Migration User Guide.











Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault

Examples
Returns information about replication tasks for your account in the current region.
response = client.describe_replication_tasks(
    Filters=[
        {
            'Name': 'string',
            'Values': [
                'string',
                'string',
            ],
        },
    ],
    Marker='',
    MaxRecords=123,
)

print(response)


Expected Output:
{
    'Marker': '',
    'ReplicationTasks': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'ReplicationTasks': [
            {
                'ReplicationTaskIdentifier': 'string',
                'SourceEndpointArn': 'string',
                'TargetEndpointArn': 'string',
                'ReplicationInstanceArn': 'string',
                'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
                'TableMappings': 'string',
                'ReplicationTaskSettings': 'string',
                'Status': 'string',
                'LastFailureMessage': 'string',
                'StopReason': 'string',
                'ReplicationTaskCreationDate': datetime(2015, 1, 1),
                'ReplicationTaskStartDate': datetime(2015, 1, 1),
                'CdcStartPosition': 'string',
                'CdcStopPosition': 'string',
                'RecoveryCheckpoint': 'string',
                'ReplicationTaskArn': 'string',
                'ReplicationTaskStats': {
                    'FullLoadProgressPercent': 123,
                    'ElapsedTimeMillis': 123,
                    'TablesLoaded': 123,
                    'TablesLoading': 123,
                    'TablesQueued': 123,
                    'TablesErrored': 123,
                    'FreshStartDate': datetime(2015, 1, 1),
                    'StartDate': datetime(2015, 1, 1),
                    'StopDate': datetime(2015, 1, 1),
                    'FullLoadStartDate': datetime(2015, 1, 1),
                    'FullLoadFinishDate': datetime(2015, 1, 1)
                },
                'TaskData': 'string'
            },
        ]
    }
    
    
    :returns: 
    Must contain from 1 to 255 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def describe_schemas(EndpointArn=None, MaxRecords=None, Marker=None):
    """
    Returns information about the schema for the specified endpoint.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns information about the schema for the specified endpoint.
    Expected Output:
    
    :example: response = client.describe_schemas(
        EndpointArn='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]\nThe Amazon Resource Name (ARN) string that uniquely identifies the endpoint.\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'Schemas': [
        'string',
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

Schemas (list) --
The described schema.

(string) --








Exceptions

DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault

Examples
Returns information about the schema for the specified endpoint.
response = client.describe_schemas(
    EndpointArn='',
    Marker='',
    MaxRecords=123,
)

print(response)


Expected Output:
{
    'Marker': '',
    'Schemas': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'Schemas': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_table_statistics(ReplicationTaskArn=None, MaxRecords=None, Marker=None, Filters=None):
    """
    Returns table statistics on the database migration task, including table name, rows inserted, rows updated, and rows deleted.
    Note that the "last updated" column the DMS console only indicates the time that AWS DMS last updated the table statistics record for a table. It does not indicate the time of the last update to the table.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns table statistics on the database migration task, including table name, rows inserted, rows updated, and rows deleted.
    Expected Output:
    
    :example: response = client.describe_table_statistics(
        ReplicationTaskArn='string',
        MaxRecords=123,
        Marker='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the replication task.\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 500.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type Filters: list
    :param Filters: Filters applied to the describe table statistics action.\nValid filter names: schema-name | table-name | table-state\nA combination of filters creates an AND condition where each record matches all specified filters.\n\n(dict) --Identifies the name and value of a source filter object used to limit the number and type of records transferred from your source to your target.\n\nName (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationTaskArn': 'string',
    'TableStatistics': [
        {
            'SchemaName': 'string',
            'TableName': 'string',
            'Inserts': 123,
            'Deletes': 123,
            'Updates': 123,
            'Ddls': 123,
            'FullLoadRows': 123,
            'FullLoadCondtnlChkFailedRows': 123,
            'FullLoadErrorRows': 123,
            'FullLoadStartTime': datetime(2015, 1, 1),
            'FullLoadEndTime': datetime(2015, 1, 1),
            'FullLoadReloaded': True|False,
            'LastUpdateTime': datetime(2015, 1, 1),
            'TableState': 'string',
            'ValidationPendingRecords': 123,
            'ValidationFailedRecords': 123,
            'ValidationSuspendedRecords': 123,
            'ValidationState': 'string',
            'ValidationStateDetails': 'string'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

ReplicationTaskArn (string) --
The Amazon Resource Name (ARN) of the replication task.

TableStatistics (list) --
The table statistics.

(dict) --
Provides a collection of table statistics in response to a request by the DescribeTableStatistics operation.

SchemaName (string) --
The schema name.

TableName (string) --
The name of the table.

Inserts (integer) --
The number of insert actions performed on a table.

Deletes (integer) --
The number of delete actions performed on a table.

Updates (integer) --
The number of update actions performed on a table.

Ddls (integer) --
The data definition language (DDL) used to build and modify the structure of your tables.

FullLoadRows (integer) --
The number of rows added during the full load operation.

FullLoadCondtnlChkFailedRows (integer) --
The number of rows that failed conditional checks during the full load operation (valid only for migrations where DynamoDB is the target).

FullLoadErrorRows (integer) --
The number of rows that failed to load during the full load operation (valid only for migrations where DynamoDB is the target).

FullLoadStartTime (datetime) --
The time when the full load operation started.

FullLoadEndTime (datetime) --
The time when the full load operation completed.

FullLoadReloaded (boolean) --
A value that indicates if the table was reloaded (true ) or loaded as part of a new full load operation (false ).

LastUpdateTime (datetime) --
The last time a table was updated.

TableState (string) --
The state of the tables described.
Valid states: Table does not exist | Before load | Full load | Table completed | Table cancelled | Table error | Table all | Table updates | Table is being reloaded

ValidationPendingRecords (integer) --
The number of records that have yet to be validated.

ValidationFailedRecords (integer) --
The number of records that failed validation.

ValidationSuspendedRecords (integer) --
The number of records that couldn\'t be validated.

ValidationState (string) --
The validation state of the table.
This parameter can have the following values:

Not enabled - Validation isn\'t enabled for the table in the migration task.
Pending records - Some records in the table are waiting for validation.
Mismatched records - Some records in the table don\'t match between the source and target.
Suspended records - Some records in the table couldn\'t be validated.
No primary key - The table couldn\'t be validated because it has no primary key.
Table error - The table wasn\'t validated because it\'s in an error state and some data wasn\'t migrated.
Validated - All rows in the table are validated. If the table is updated, the status can change from Validated.
Error - The table couldn\'t be validated because of an unexpected error.


ValidationStateDetails (string) --
Additional details about the state of validation.





Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .







Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault

Examples
Returns table statistics on the database migration task, including table name, rows inserted, rows updated, and rows deleted.
response = client.describe_table_statistics(
    Marker='',
    MaxRecords=123,
    ReplicationTaskArn='',
)

print(response)


Expected Output:
{
    'Marker': '',
    'ReplicationTaskArn': '',
    'TableStatistics': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReplicationTaskArn': 'string',
        'TableStatistics': [
            {
                'SchemaName': 'string',
                'TableName': 'string',
                'Inserts': 123,
                'Deletes': 123,
                'Updates': 123,
                'Ddls': 123,
                'FullLoadRows': 123,
                'FullLoadCondtnlChkFailedRows': 123,
                'FullLoadErrorRows': 123,
                'FullLoadStartTime': datetime(2015, 1, 1),
                'FullLoadEndTime': datetime(2015, 1, 1),
                'FullLoadReloaded': True|False,
                'LastUpdateTime': datetime(2015, 1, 1),
                'TableState': 'string',
                'ValidationPendingRecords': 123,
                'ValidationFailedRecords': 123,
                'ValidationSuspendedRecords': 123,
                'ValidationState': 'string',
                'ValidationStateDetails': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    Not enabled - Validation isn\'t enabled for the table in the migration task.
    Pending records - Some records in the table are waiting for validation.
    Mismatched records - Some records in the table don\'t match between the source and target.
    Suspended records - Some records in the table couldn\'t be validated.
    No primary key - The table couldn\'t be validated because it has no primary key.
    Table error - The table wasn\'t validated because it\'s in an error state and some data wasn\'t migrated.
    Validated - All rows in the table are validated. If the table is updated, the status can change from Validated.
    Error - The table couldn\'t be validated because of an unexpected error.
    
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

def import_certificate(CertificateIdentifier=None, CertificatePem=None, CertificateWallet=None, Tags=None):
    """
    Uploads the specified certificate.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Uploads the specified certificate.
    Expected Output:
    
    :example: response = client.import_certificate(
        CertificateIdentifier='string',
        CertificatePem='string',
        CertificateWallet=b'bytes',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type CertificateIdentifier: string
    :param CertificateIdentifier: [REQUIRED]\nA customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can\'t end with a hyphen or contain two consecutive hyphens.\n

    :type CertificatePem: string
    :param CertificatePem: The contents of a .pem file, which contains an X.509 certificate.

    :type CertificateWallet: bytes
    :param CertificateWallet: The location of an imported Oracle Wallet certificate for use with SSL.

    :type Tags: list
    :param Tags: The tags associated with the certificate.\n\n(dict) --A user-defined key-value pair that describes metadata added to an AWS DMS resource and that is used by operations such as the following:\n\nAddTagsToResource\nListTagsForResource\nRemoveTagsFromResource\n\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Certificate': {
        'CertificateIdentifier': 'string',
        'CertificateCreationDate': datetime(2015, 1, 1),
        'CertificatePem': 'string',
        'CertificateWallet': b'bytes',
        'CertificateArn': 'string',
        'CertificateOwner': 'string',
        'ValidFromDate': datetime(2015, 1, 1),
        'ValidToDate': datetime(2015, 1, 1),
        'SigningAlgorithm': 'string',
        'KeyLength': 123
    }
}


Response Structure

(dict) --

Certificate (dict) --
The certificate to be uploaded.

CertificateIdentifier (string) --
A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can\'t end with a hyphen or contain two consecutive hyphens.

CertificateCreationDate (datetime) --
The date that the certificate was created.

CertificatePem (string) --
The contents of a .pem file, which contains an X.509 certificate.

CertificateWallet (bytes) --
The location of an imported Oracle Wallet certificate for use with SSL.

CertificateArn (string) --
The Amazon Resource Name (ARN) for the certificate.

CertificateOwner (string) --
The owner of the certificate.

ValidFromDate (datetime) --
The beginning date that the certificate is valid.

ValidToDate (datetime) --
The final date that the certificate is valid.

SigningAlgorithm (string) --
The signing algorithm for the certificate.

KeyLength (integer) --
The key length of the cryptographic algorithm being used.









Exceptions

DatabaseMigrationService.Client.exceptions.ResourceAlreadyExistsFault
DatabaseMigrationService.Client.exceptions.InvalidCertificateFault
DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault

Examples
Uploads the specified certificate.
response = client.import_certificate(
    CertificateIdentifier='',
    CertificatePem='',
)

print(response)


Expected Output:
{
    'Certificate': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Certificate': {
            'CertificateIdentifier': 'string',
            'CertificateCreationDate': datetime(2015, 1, 1),
            'CertificatePem': 'string',
            'CertificateWallet': b'bytes',
            'CertificateArn': 'string',
            'CertificateOwner': 'string',
            'ValidFromDate': datetime(2015, 1, 1),
            'ValidToDate': datetime(2015, 1, 1),
            'SigningAlgorithm': 'string',
            'KeyLength': 123
        }
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.ResourceAlreadyExistsFault
    DatabaseMigrationService.Client.exceptions.InvalidCertificateFault
    DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Lists all tags for an AWS DMS resource.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists all tags for an AWS DMS resource.
    Expected Output:
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) string that uniquely identifies the AWS DMS resource.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TagList': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
TagList (list) --A list of tags for the resource.

(dict) --A user-defined key-value pair that describes metadata added to an AWS DMS resource and that is used by operations such as the following:

AddTagsToResource
ListTagsForResource
RemoveTagsFromResource


Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with "aws:" or "dms:". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with "aws:" or "dms:". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").










Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault

Examples
Lists all tags for an AWS DMS resource.
response = client.list_tags_for_resource(
    ResourceArn='',
)

print(response)


Expected Output:
{
    'TagList': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    
    """
    pass

def modify_endpoint(EndpointArn=None, EndpointIdentifier=None, EndpointType=None, EngineName=None, Username=None, Password=None, ServerName=None, Port=None, DatabaseName=None, ExtraConnectionAttributes=None, CertificateArn=None, SslMode=None, ServiceAccessRoleArn=None, ExternalTableDefinition=None, DynamoDbSettings=None, S3Settings=None, DmsTransferSettings=None, MongoDbSettings=None, KinesisSettings=None, KafkaSettings=None, ElasticsearchSettings=None, NeptuneSettings=None, RedshiftSettings=None):
    """
    Modifies the specified endpoint.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Modifies the specified endpoint.
    Expected Output:
    
    :example: response = client.modify_endpoint(
        EndpointArn='string',
        EndpointIdentifier='string',
        EndpointType='source'|'target',
        EngineName='string',
        Username='string',
        Password='string',
        ServerName='string',
        Port=123,
        DatabaseName='string',
        ExtraConnectionAttributes='string',
        CertificateArn='string',
        SslMode='none'|'require'|'verify-ca'|'verify-full',
        ServiceAccessRoleArn='string',
        ExternalTableDefinition='string',
        DynamoDbSettings={
            'ServiceAccessRoleArn': 'string'
        },
        S3Settings={
            'ServiceAccessRoleArn': 'string',
            'ExternalTableDefinition': 'string',
            'CsvRowDelimiter': 'string',
            'CsvDelimiter': 'string',
            'BucketFolder': 'string',
            'BucketName': 'string',
            'CompressionType': 'none'|'gzip',
            'EncryptionMode': 'sse-s3'|'sse-kms',
            'ServerSideEncryptionKmsKeyId': 'string',
            'DataFormat': 'csv'|'parquet',
            'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
            'DictPageSizeLimit': 123,
            'RowGroupLength': 123,
            'DataPageSize': 123,
            'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
            'EnableStatistics': True|False,
            'IncludeOpForFullLoad': True|False,
            'CdcInsertsOnly': True|False,
            'TimestampColumnName': 'string',
            'ParquetTimestampInMillisecond': True|False,
            'CdcInsertsAndUpdates': True|False
        },
        DmsTransferSettings={
            'ServiceAccessRoleArn': 'string',
            'BucketName': 'string'
        },
        MongoDbSettings={
            'Username': 'string',
            'Password': 'string',
            'ServerName': 'string',
            'Port': 123,
            'DatabaseName': 'string',
            'AuthType': 'no'|'password',
            'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
            'NestingLevel': 'none'|'one',
            'ExtractDocId': 'string',
            'DocsToInvestigate': 'string',
            'AuthSource': 'string',
            'KmsKeyId': 'string'
        },
        KinesisSettings={
            'StreamArn': 'string',
            'MessageFormat': 'json'|'json-unformatted',
            'ServiceAccessRoleArn': 'string',
            'IncludeTransactionDetails': True|False,
            'IncludePartitionValue': True|False,
            'PartitionIncludeSchemaTable': True|False,
            'IncludeTableAlterOperations': True|False,
            'IncludeControlDetails': True|False
        },
        KafkaSettings={
            'Broker': 'string',
            'Topic': 'string'
        },
        ElasticsearchSettings={
            'ServiceAccessRoleArn': 'string',
            'EndpointUri': 'string',
            'FullLoadErrorPercentage': 123,
            'ErrorRetryDuration': 123
        },
        NeptuneSettings={
            'ServiceAccessRoleArn': 'string',
            'S3BucketName': 'string',
            'S3BucketFolder': 'string',
            'ErrorRetryDuration': 123,
            'MaxFileSize': 123,
            'MaxRetryCount': 123,
            'IamAuthEnabled': True|False
        },
        RedshiftSettings={
            'AcceptAnyDate': True|False,
            'AfterConnectScript': 'string',
            'BucketFolder': 'string',
            'BucketName': 'string',
            'ConnectionTimeout': 123,
            'DatabaseName': 'string',
            'DateFormat': 'string',
            'EmptyAsNull': True|False,
            'EncryptionMode': 'sse-s3'|'sse-kms',
            'FileTransferUploadStreams': 123,
            'LoadTimeout': 123,
            'MaxFileSize': 123,
            'Password': 'string',
            'Port': 123,
            'RemoveQuotes': True|False,
            'ReplaceInvalidChars': 'string',
            'ReplaceChars': 'string',
            'ServerName': 'string',
            'ServiceAccessRoleArn': 'string',
            'ServerSideEncryptionKmsKeyId': 'string',
            'TimeFormat': 'string',
            'TrimBlanks': True|False,
            'TruncateColumns': True|False,
            'Username': 'string',
            'WriteBufferSize': 123
        }
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]\nThe Amazon Resource Name (ARN) string that uniquely identifies the endpoint.\n

    :type EndpointIdentifier: string
    :param EndpointIdentifier: The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can\'t end with a hyphen or contain two consecutive hyphens.

    :type EndpointType: string
    :param EndpointType: The type of endpoint. Valid values are source and target .

    :type EngineName: string
    :param EngineName: The type of engine for the endpoint. Valid values, depending on the EndpointType, include 'mysql' , 'oracle' , 'postgres' , 'mariadb' , 'aurora' , 'aurora-postgresql' , 'redshift' , 's3' , 'db2' , 'azuredb' , 'sybase' , 'dynamodb' , 'mongodb' , 'kinesis' , 'kafka' , 'elasticsearch' , 'documentdb' , and 'sqlserver' .

    :type Username: string
    :param Username: The user name to be used to login to the endpoint database.

    :type Password: string
    :param Password: The password to be used to login to the endpoint database.

    :type ServerName: string
    :param ServerName: The name of the server where the endpoint database resides.

    :type Port: integer
    :param Port: The port used by the endpoint database.

    :type DatabaseName: string
    :param DatabaseName: The name of the endpoint database.

    :type ExtraConnectionAttributes: string
    :param ExtraConnectionAttributes: Additional attributes associated with the connection. To reset this parameter, pass the empty string ('') as an argument.

    :type CertificateArn: string
    :param CertificateArn: The Amazon Resource Name (ARN) of the certificate used for SSL connection.

    :type SslMode: string
    :param SslMode: The SSL mode used to connect to the endpoint. The default value is none .

    :type ServiceAccessRoleArn: string
    :param ServiceAccessRoleArn: The Amazon Resource Name (ARN) for the service access role you want to use to modify the endpoint.

    :type ExternalTableDefinition: string
    :param ExternalTableDefinition: The external table definition.

    :type DynamoDbSettings: dict
    :param DynamoDbSettings: Settings in JSON format for the target Amazon DynamoDB endpoint. For information about other available settings, see Using Object Mapping to Migrate Data to DynamoDB in the AWS Database Migration Service User Guide.\n\nServiceAccessRoleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) used by the service access IAM role.\n\n\n

    :type S3Settings: dict
    :param S3Settings: Settings in JSON format for the target Amazon S3 endpoint. For more information about the available settings, see Extra Connection Attributes When Using Amazon S3 as a Target for AWS DMS in the AWS Database Migration Service User Guide.\n\nServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) used by the service access IAM role.\n\nExternalTableDefinition (string) --The external table definition.\n\nCsvRowDelimiter (string) --The delimiter used to separate rows in the source files. The default is a carriage return (\\n ).\n\nCsvDelimiter (string) --The delimiter used to separate columns in the source files. The default is a comma.\n\nBucketFolder (string) --An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in the path `` bucketFolder /schema_name /table_name /`` . If this parameter isn\'t specified, then the path used is `` schema_name /table_name /`` .\n\nBucketName (string) --The name of the S3 bucket.\n\nCompressionType (string) --An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the target files. Either set this parameter to NONE (the default) or don\'t use it to leave the files uncompressed. This parameter applies to both .csv and .parquet file formats.\n\nEncryptionMode (string) --The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either SSE_S3 (the default) or SSE_KMS . To use SSE_S3 , you need an AWS Identity and Access Management (IAM) role with permission to allow 'arn:aws:s3:::dms-*' to use the following actions:\n\ns3:CreateBucket\ns3:ListBucket\ns3:DeleteBucket\ns3:GetBucketLocation\ns3:GetObject\ns3:PutObject\ns3:DeleteObject\ns3:GetObjectVersion\ns3:GetBucketPolicy\ns3:PutBucketPolicy\ns3:DeleteBucketPolicy\n\n\nServerSideEncryptionKmsKeyId (string) --If you are using SSE_KMS for the EncryptionMode , provide the AWS KMS key ID. The key that you use needs an attached policy that enables AWS Identity and Access Management (IAM) user permissions and allows use of the key.\nHere is a CLI example: ``aws dms create-endpoint --endpoint-identifier value --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value* ,BucketFolder=*value* ,BucketName=*value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``\n\nDataFormat (string) --The format of the data that you want to use for output. You can choose one of the following:\n\ncsv : This is a row-based file format with comma-separated values (.csv).\nparquet : Apache Parquet (.parquet) is a columnar storage file format that features efficient compression and provides faster query response.\n\n\nEncodingType (string) --The type of encoding you are using:\n\nRLE_DICTIONARY uses a combination of bit-packing and run-length encoding to store repeated values more efficiently. This is the default.\nPLAIN doesn\'t use encoding at all. Values are stored as they are.\nPLAIN_DICTIONARY builds a dictionary of the values encountered in a given column. The dictionary is stored in a dictionary page for each column chunk.\n\n\nDictPageSizeLimit (integer) --The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds this, this column is stored using an encoding type of PLAIN . This parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to PLAIN encoding. This size is used for .parquet file format only.\n\nRowGroupLength (integer) --The number of rows in a row group. A smaller row group size provides faster reads. But as the number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows. This number is used for .parquet file format only.\nIf you choose a value larger than the maximum, RowGroupLength is set to the max row group length in bytes (64 * 1024 * 1024).\n\nDataPageSize (integer) --The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This number is used for .parquet file format only.\n\nParquetVersion (string) --The version of the Apache Parquet format that you want to use: parquet_1_0 (the default) or parquet_2_0 .\n\nEnableStatistics (boolean) --A value that enables statistics for Parquet pages and row groups. Choose true to enable statistics, false to disable. Statistics include NULL , DISTINCT , MAX , and MIN values. This parameter defaults to true . This value is used for .parquet file format only.\n\nIncludeOpForFullLoad (boolean) --A value that enables a full load to write INSERT operations to the comma-separated value (.csv) output files only to indicate how the rows were added to the source database.\n\nNote\nAWS DMS supports the IncludeOpForFullLoad parameter in versions 3.1.4 and later.\n\nFor full load, records can only be inserted. By default (the false setting), no information is recorded in these output files for a full load to indicate that the rows were inserted at the source database. If IncludeOpForFullLoad is set to true or y , the INSERT is recorded as an I annotation in the first field of the .csv file. This allows the format of your target records from a full load to be consistent with the target records from a CDC load.\n\nNote\nThis setting works together with the CdcInsertsOnly and the CdcInsertsAndUpdates parameters for output to .csv files only. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .\n\n\nCdcInsertsOnly (boolean) --A value that enables a change data capture (CDC) load to write only INSERT operations to .csv or columnar storage (.parquet) output files. By default (the false setting), the first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated, or deleted at the source database for a CDC load to the target.\nIf CdcInsertsOnly is set to true or y , only INSERTs from the source database are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded depends on the value of IncludeOpForFullLoad . If IncludeOpForFullLoad is set to true , the first field of every CDC record is set to I to indicate the INSERT operation at the source. If IncludeOpForFullLoad is set to false , every CDC record is written without a first field to indicate the INSERT operation at the source. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .\n\nNote\nAWS DMS supports the interaction described preceding between the CdcInsertsOnly and IncludeOpForFullLoad parameters in versions 3.1.4 and later.\n\nCdcInsertsOnly and CdcInsertsAndUpdates can\'t both be set to true for the same endpoint. Set either CdcInsertsOnly or CdcInsertsAndUpdates to true for the same endpoint, but not both.\n\n\nTimestampColumnName (string) --A value that when nonblank causes AWS DMS to add a column with timestamp information to the endpoint data for an Amazon S3 target.\n\nNote\nAWS DMS supports the TimestampColumnName parameter in versions 3.1.4 and later.\n\nDMS includes an additional STRING column in the .csv or .parquet object files of your migrated data when you set TimestampColumnName to a nonblank value.\nFor a full load, each row of this timestamp column contains a timestamp for when the data was transferred from the source to the target by DMS.\nFor a change data capture (CDC) load, each row of the timestamp column contains the timestamp for the commit of that row in the source database.\nThe string format for this timestamp column value is yyyy-MM-dd HH:mm:ss.SSSSSS . By default, the precision of this value is in microseconds. For a CDC load, the rounding of the precision depends on the commit timestamp supported by DMS for the source database.\nWhen the AddColumnName parameter is set to true , DMS also includes a name for the timestamp column that you set with TimestampColumnName .\n\nParquetTimestampInMillisecond (boolean) --A value that specifies the precision of any TIMESTAMP column values that are written to an Amazon S3 object file in .parquet format.\n\nNote\nAWS DMS supports the ParquetTimestampInMillisecond parameter in versions 3.1.4 and later.\n\nWhen ParquetTimestampInMillisecond is set to true or y , AWS DMS writes all TIMESTAMP columns in a .parquet formatted file with millisecond precision. Otherwise, DMS writes them with microsecond precision.\nCurrently, Amazon Athena and AWS Glue can handle only millisecond precision for TIMESTAMP values. Set this parameter to true for S3 endpoint object files that are .parquet formatted only if you plan to query or process the data with Athena or AWS Glue.\n\nNote\nAWS DMS writes any TIMESTAMP column values written to an S3 file in .csv format with microsecond precision.\nSetting ParquetTimestampInMillisecond has no effect on the string format of the timestamp column value that is inserted by setting the TimestampColumnName parameter.\n\n\nCdcInsertsAndUpdates (boolean) --A value that enables a change data capture (CDC) load to write INSERT and UPDATE operations to .csv or .parquet (columnar storage) output files. The default setting is false , but when CdcInsertsAndUpdates is set to true or y , INSERTs and UPDATEs from the source database are migrated to the .csv or .parquet file.\nFor .csv file format only, how these INSERTs and UPDATEs are recorded depends on the value of the IncludeOpForFullLoad parameter. If IncludeOpForFullLoad is set to true , the first field of every CDC record is set to either I or U to indicate INSERT and UPDATE operations at the source. But if IncludeOpForFullLoad is set to false , CDC records are written without an indication of INSERT or UPDATE operations at the source. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .\n\nNote\nAWS DMS supports the use of the CdcInsertsAndUpdates parameter in versions 3.3.1 and later.\n\nCdcInsertsOnly and CdcInsertsAndUpdates can\'t both be set to true for the same endpoint. Set either CdcInsertsOnly or CdcInsertsAndUpdates to true for the same endpoint, but not both.\n\n\n\n

    :type DmsTransferSettings: dict
    :param DmsTransferSettings: The settings in JSON format for the DMS transfer type of source endpoint.\nAttributes include the following:\n\nserviceAccessRoleArn - The AWS Identity and Access Management (IAM) role that has permission to access the Amazon S3 bucket.\nBucketName - The name of the S3 bucket to use.\ncompressionType - An optional parameter to use GZIP to compress the target files. Either set this parameter to NONE (the default) or don\'t use it to leave the files uncompressed.\n\nShorthand syntax for these settings is as follows: ServiceAccessRoleArn=string ,BucketName=string,CompressionType=string\nJSON syntax for these settings is as follows: { 'ServiceAccessRoleArn': 'string', 'BucketName': 'string', 'CompressionType': 'none'|'gzip' }\n\nServiceAccessRoleArn (string) --The IAM role that has permission to access the Amazon S3 bucket.\n\nBucketName (string) --The name of the S3 bucket to use.\n\n\n

    :type MongoDbSettings: dict
    :param MongoDbSettings: Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see the configuration properties section in Using MongoDB as a Target for AWS Database Migration Service in the AWS Database Migration Service User Guide.\n\nUsername (string) --The user name you use to access the MongoDB source endpoint.\n\nPassword (string) --The password for the user account you use to access the MongoDB source endpoint.\n\nServerName (string) --The name of the server on the MongoDB source endpoint.\n\nPort (integer) --The port value for the MongoDB source endpoint.\n\nDatabaseName (string) --The database name on the MongoDB source endpoint.\n\nAuthType (string) --The authentication type you use to access the MongoDB source endpoint.\nValid values: NO, PASSWORD\nWhen NO is selected, user name and password parameters are not used and can be empty.\n\nAuthMechanism (string) --The authentication mechanism you use to access the MongoDB source endpoint.\nValid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1\nDEFAULT \xe2\x80\x93 For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use SCRAM_SHA_1. This setting isn\'t used when authType=No.\n\nNestingLevel (string) --Specifies either document or table mode.\nValid values: NONE, ONE\nDefault value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.\n\nExtractDocId (string) --Specifies the document ID. Use this setting when NestingLevel is set to NONE.\nDefault value is false.\n\nDocsToInvestigate (string) --Indicates the number of documents to preview to determine the document organization. Use this setting when NestingLevel is set to ONE.\nMust be a positive value greater than 0. Default value is 1000.\n\nAuthSource (string) --The MongoDB database name. This setting isn\'t used when authType=NO .\nThe default is admin.\n\nKmsKeyId (string) --The AWS KMS key identifier that is used to encrypt the content on the replication instance. If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.\n\n\n

    :type KinesisSettings: dict
    :param KinesisSettings: Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams. For more information about the available settings, see Using Amazon Kinesis Data Streams as a Target for AWS Database Migration Service in the AWS Database Migration User Guide.\n\nStreamArn (string) --The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.\n\nMessageFormat (string) --The output format for the records created on the endpoint. The message format is JSON (default) or JSON_UNFORMATTED (a single line with no tab).\n\nServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) for the AWS Identity and Access Management (IAM) role that AWS DMS uses to write to the Kinesis data stream.\n\nIncludeTransactionDetails (boolean) --Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for transaction_id , previous transaction_id , and transaction_record_id (the record offset within a transaction). The default is False .\n\nIncludePartitionValue (boolean) --Shows the partition value within the Kinesis message output, unless the partition type is schema-table-type . The default is False .\n\nPartitionIncludeSchemaTable (boolean) --Prefixes schema and table names to partition values, when the partition type is primary-key-type . Doing this increases data distribution among Kinesis shards. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same shard, which causes throttling. The default is False .\n\nIncludeTableAlterOperations (boolean) --Includes any data definition language (DDL) operations that change the table in the control data, such as rename-table , drop-table , add-column , drop-column , and rename-column . The default is False .\n\nIncludeControlDetails (boolean) --Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output. The default is False .\n\n\n

    :type KafkaSettings: dict
    :param KafkaSettings: Settings in JSON format for the target Apache Kafka endpoint. For more information about the available settings, see Using Apache Kafka as a Target for AWS Database Migration Service in the AWS Database Migration User Guide.\n\nBroker (string) --The broker location and port of the Kafka broker that hosts your Kafka instance. Specify the broker in the form `` broker-hostname-or-ip :port `` . For example, 'ec2-12-345-678-901.compute-1.amazonaws.com:2345' .\n\nTopic (string) --The topic to which you migrate the data. If you don\'t specify a topic, AWS DMS specifies 'kafka-default-topic' as the migration topic.\n\n\n

    :type ElasticsearchSettings: dict
    :param ElasticsearchSettings: Settings in JSON format for the target Elasticsearch endpoint. For more information about the available settings, see Extra Connection Attributes When Using Elasticsearch as a Target for AWS DMS in the AWS Database Migration User Guide.\n\nServiceAccessRoleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) used by service to access the IAM role.\n\nEndpointUri (string) -- [REQUIRED]The endpoint for the Elasticsearch cluster.\n\nFullLoadErrorPercentage (integer) --The maximum percentage of records that can fail to be written before a full load operation stops.\n\nErrorRetryDuration (integer) --The maximum number of seconds for which DMS retries failed API requests to the Elasticsearch cluster.\n\n\n

    :type NeptuneSettings: dict
    :param NeptuneSettings: Settings in JSON format for the target Amazon Neptune endpoint. For more information about the available settings, see https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings in the AWS Database Migration Service User Guide.\n\nServiceAccessRoleArn (string) --The ARN of the service role you have created for the Neptune target endpoint. For more information, see https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.ServiceRole in the AWS Database Migration Service User Guide.\n\nS3BucketName (string) -- [REQUIRED]The name of the S3 bucket for AWS DMS to temporarily store migrated graph data in CSV files before bulk-loading it to the Neptune target database. AWS DMS maps the SQL source data to graph data before storing it in these CSV files.\n\nS3BucketFolder (string) -- [REQUIRED]A folder path where you where you want AWS DMS to store migrated graph data in the S3 bucket specified by S3BucketName\n\nErrorRetryDuration (integer) --The number of milliseconds for AWS DMS to wait to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 250.\n\nMaxFileSize (integer) --The maximum size in KB of migrated graph data stored in a CSV file before AWS DMS bulk-loads the data to the Neptune target database. The default is 1048576 KB. If successful, AWS DMS clears the bucket, ready to store the next batch of migrated graph data.\n\nMaxRetryCount (integer) --The number of times for AWS DMS to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 5.\n\nIamAuthEnabled (boolean) --If you want IAM authorization enabled for this endpoint, set this parameter to true and attach the appropriate role policy document to your service role specified by ServiceAccessRoleArn . The default is false .\n\n\n

    :type RedshiftSettings: dict
    :param RedshiftSettings: Provides information that defines an Amazon Redshift endpoint.\n\nAcceptAnyDate (boolean) --A value that indicates to allow any date format, including invalid formats such as 00/00/00 00:00:00, to be loaded without generating an error. You can choose true or false (the default).\nThis parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data doesn\'t match the DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.\n\nAfterConnectScript (string) --Code to run after connecting. This parameter should contain the code itself, not the name of a file containing the code.\n\nBucketFolder (string) --The location where the comma-separated value (.csv) files are stored before being uploaded to the S3 bucket.\n\nBucketName (string) --The name of the S3 bucket you want to use\n\nConnectionTimeout (integer) --A value that sets the amount of time to wait (in milliseconds) before timing out, beginning from when you initially establish a connection.\n\nDatabaseName (string) --The name of the Amazon Redshift data warehouse (service) that you are working with.\n\nDateFormat (string) --The date format that you are using. Valid values are auto (case-sensitive), your date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults to a format of \'YYYY-MM-DD\'. Using auto recognizes most strings, even some that aren\'t supported when you use a date format string.\nIf your date and time values use formats different from each other, set this to auto .\n\nEmptyAsNull (boolean) --A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL. A value of true sets empty CHAR and VARCHAR fields to null. The default is false .\n\nEncryptionMode (string) --The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either SSE_S3 (the default) or SSE_KMS . To use SSE_S3 , create an AWS Identity and Access Management (IAM) role with a policy that allows 'arn:aws:s3:::*' to use the following actions: 's3:PutObject', 's3:ListBucket'\n\nFileTransferUploadStreams (integer) --The number of threads used to upload a single file. This parameter accepts a value from 1 through 64. It defaults to 10.\n\nLoadTimeout (integer) --The amount of time to wait (in milliseconds) before timing out, beginning from when you begin loading.\n\nMaxFileSize (integer) --The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).\n\nPassword (string) --The password for the user named in the username property.\n\nPort (integer) --The port number for Amazon Redshift. The default value is 5439.\n\nRemoveQuotes (boolean) --A value that specifies to remove surrounding quotation marks from strings in the incoming data. All characters within the quotation marks, including delimiters, are retained. Choose true to remove quotation marks. The default is false .\n\nReplaceInvalidChars (string) --A list of characters that you want to replace. Use with ReplaceChars .\n\nReplaceChars (string) --A value that specifies to replaces the invalid characters specified in ReplaceInvalidChars , substituting the specified characters instead. The default is '?' .\n\nServerName (string) --The name of the Amazon Redshift cluster you are using.\n\nServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service.\n\nServerSideEncryptionKmsKeyId (string) --The AWS KMS key ID. If you are using SSE_KMS for the EncryptionMode , provide this key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.\n\nTimeFormat (string) --The time format that you want to use. Valid values are auto (case-sensitive), \'timeformat_string\' , \'epochsecs\' , or \'epochmillisecs\' . It defaults to 10. Using auto recognizes most strings, even some that aren\'t supported when you use a time format string.\nIf your date and time values use formats different from each other, set this parameter to auto .\n\nTrimBlanks (boolean) --A value that specifies to remove the trailing white space characters from a VARCHAR string. This parameter applies only to columns with a VARCHAR data type. Choose true to remove unneeded white space. The default is false .\n\nTruncateColumns (boolean) --A value that specifies to truncate data in columns to the appropriate number of characters, so that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose true to truncate data. The default is false .\n\nUsername (string) --An Amazon Redshift user name for a registered user.\n\nWriteBufferSize (integer) --The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The default is 1,024. Use this setting to tune performance.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Endpoint': {
        'EndpointIdentifier': 'string',
        'EndpointType': 'source'|'target',
        'EngineName': 'string',
        'EngineDisplayName': 'string',
        'Username': 'string',
        'ServerName': 'string',
        'Port': 123,
        'DatabaseName': 'string',
        'ExtraConnectionAttributes': 'string',
        'Status': 'string',
        'KmsKeyId': 'string',
        'EndpointArn': 'string',
        'CertificateArn': 'string',
        'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
        'ServiceAccessRoleArn': 'string',
        'ExternalTableDefinition': 'string',
        'ExternalId': 'string',
        'DynamoDbSettings': {
            'ServiceAccessRoleArn': 'string'
        },
        'S3Settings': {
            'ServiceAccessRoleArn': 'string',
            'ExternalTableDefinition': 'string',
            'CsvRowDelimiter': 'string',
            'CsvDelimiter': 'string',
            'BucketFolder': 'string',
            'BucketName': 'string',
            'CompressionType': 'none'|'gzip',
            'EncryptionMode': 'sse-s3'|'sse-kms',
            'ServerSideEncryptionKmsKeyId': 'string',
            'DataFormat': 'csv'|'parquet',
            'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
            'DictPageSizeLimit': 123,
            'RowGroupLength': 123,
            'DataPageSize': 123,
            'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
            'EnableStatistics': True|False,
            'IncludeOpForFullLoad': True|False,
            'CdcInsertsOnly': True|False,
            'TimestampColumnName': 'string',
            'ParquetTimestampInMillisecond': True|False,
            'CdcInsertsAndUpdates': True|False
        },
        'DmsTransferSettings': {
            'ServiceAccessRoleArn': 'string',
            'BucketName': 'string'
        },
        'MongoDbSettings': {
            'Username': 'string',
            'Password': 'string',
            'ServerName': 'string',
            'Port': 123,
            'DatabaseName': 'string',
            'AuthType': 'no'|'password',
            'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
            'NestingLevel': 'none'|'one',
            'ExtractDocId': 'string',
            'DocsToInvestigate': 'string',
            'AuthSource': 'string',
            'KmsKeyId': 'string'
        },
        'KinesisSettings': {
            'StreamArn': 'string',
            'MessageFormat': 'json'|'json-unformatted',
            'ServiceAccessRoleArn': 'string',
            'IncludeTransactionDetails': True|False,
            'IncludePartitionValue': True|False,
            'PartitionIncludeSchemaTable': True|False,
            'IncludeTableAlterOperations': True|False,
            'IncludeControlDetails': True|False
        },
        'KafkaSettings': {
            'Broker': 'string',
            'Topic': 'string'
        },
        'ElasticsearchSettings': {
            'ServiceAccessRoleArn': 'string',
            'EndpointUri': 'string',
            'FullLoadErrorPercentage': 123,
            'ErrorRetryDuration': 123
        },
        'NeptuneSettings': {
            'ServiceAccessRoleArn': 'string',
            'S3BucketName': 'string',
            'S3BucketFolder': 'string',
            'ErrorRetryDuration': 123,
            'MaxFileSize': 123,
            'MaxRetryCount': 123,
            'IamAuthEnabled': True|False
        },
        'RedshiftSettings': {
            'AcceptAnyDate': True|False,
            'AfterConnectScript': 'string',
            'BucketFolder': 'string',
            'BucketName': 'string',
            'ConnectionTimeout': 123,
            'DatabaseName': 'string',
            'DateFormat': 'string',
            'EmptyAsNull': True|False,
            'EncryptionMode': 'sse-s3'|'sse-kms',
            'FileTransferUploadStreams': 123,
            'LoadTimeout': 123,
            'MaxFileSize': 123,
            'Password': 'string',
            'Port': 123,
            'RemoveQuotes': True|False,
            'ReplaceInvalidChars': 'string',
            'ReplaceChars': 'string',
            'ServerName': 'string',
            'ServiceAccessRoleArn': 'string',
            'ServerSideEncryptionKmsKeyId': 'string',
            'TimeFormat': 'string',
            'TrimBlanks': True|False,
            'TruncateColumns': True|False,
            'Username': 'string',
            'WriteBufferSize': 123
        }
    }
}


Response Structure

(dict) --

Endpoint (dict) --
The modified endpoint.

EndpointIdentifier (string) --
The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can\'t end with a hyphen or contain two consecutive hyphens.

EndpointType (string) --
The type of endpoint. Valid values are source and target .

EngineName (string) --
The database engine name. Valid values, depending on the EndpointType, include "mysql" , "oracle" , "postgres" , "mariadb" , "aurora" , "aurora-postgresql" , "redshift" , "s3" , "db2" , "azuredb" , "sybase" , "dynamodb" , "mongodb" , "kinesis" , "kafka" , "elasticsearch" , "documentdb" , and "sqlserver" .

EngineDisplayName (string) --
The expanded name for the engine name. For example, if the EngineName parameter is "aurora," this value would be "Amazon Aurora MySQL."

Username (string) --
The user name used to connect to the endpoint.

ServerName (string) --
The name of the server at the endpoint.

Port (integer) --
The port value used to access the endpoint.

DatabaseName (string) --
The name of the database at the endpoint.

ExtraConnectionAttributes (string) --
Additional connection attributes used to connect to the endpoint.

Status (string) --
The status of the endpoint.

KmsKeyId (string) --
An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint.
If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key.
AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.

EndpointArn (string) --
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

CertificateArn (string) --
The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

SslMode (string) --
The SSL mode used to connect to the endpoint. The default value is none .

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) used by the service access IAM role.

ExternalTableDefinition (string) --
The external table definition.

ExternalId (string) --
Value returned by a call to CreateEndpoint that can be used for cross-account validation. Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

DynamoDbSettings (dict) --
The settings for the target DynamoDB database. For more information, see the DynamoDBSettings structure.

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) used by the service access IAM role.



S3Settings (dict) --
The settings for the S3 target endpoint. For more information, see the S3Settings structure.

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) used by the service access IAM role.

ExternalTableDefinition (string) --
The external table definition.

CsvRowDelimiter (string) --
The delimiter used to separate rows in the source files. The default is a carriage return (\
 ).

CsvDelimiter (string) --
The delimiter used to separate columns in the source files. The default is a comma.

BucketFolder (string) --
An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in the path `` bucketFolder /schema_name /table_name /`` . If this parameter isn\'t specified, then the path used is `` schema_name /table_name /`` .

BucketName (string) --
The name of the S3 bucket.

CompressionType (string) --
An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the target files. Either set this parameter to NONE (the default) or don\'t use it to leave the files uncompressed. This parameter applies to both .csv and .parquet file formats.

EncryptionMode (string) --
The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either SSE_S3 (the default) or SSE_KMS . To use SSE_S3 , you need an AWS Identity and Access Management (IAM) role with permission to allow "arn:aws:s3:::dms-*" to use the following actions:

s3:CreateBucket
s3:ListBucket
s3:DeleteBucket
s3:GetBucketLocation
s3:GetObject
s3:PutObject
s3:DeleteObject
s3:GetObjectVersion
s3:GetBucketPolicy
s3:PutBucketPolicy
s3:DeleteBucketPolicy


ServerSideEncryptionKmsKeyId (string) --
If you are using SSE_KMS for the EncryptionMode , provide the AWS KMS key ID. The key that you use needs an attached policy that enables AWS Identity and Access Management (IAM) user permissions and allows use of the key.
Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier value --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value* ,BucketFolder=*value* ,BucketName=*value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

DataFormat (string) --
The format of the data that you want to use for output. You can choose one of the following:

csv : This is a row-based file format with comma-separated values (.csv).
parquet : Apache Parquet (.parquet) is a columnar storage file format that features efficient compression and provides faster query response.


EncodingType (string) --
The type of encoding you are using:

RLE_DICTIONARY uses a combination of bit-packing and run-length encoding to store repeated values more efficiently. This is the default.
PLAIN doesn\'t use encoding at all. Values are stored as they are.
PLAIN_DICTIONARY builds a dictionary of the values encountered in a given column. The dictionary is stored in a dictionary page for each column chunk.


DictPageSizeLimit (integer) --
The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds this, this column is stored using an encoding type of PLAIN . This parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to PLAIN encoding. This size is used for .parquet file format only.

RowGroupLength (integer) --
The number of rows in a row group. A smaller row group size provides faster reads. But as the number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows. This number is used for .parquet file format only.
If you choose a value larger than the maximum, RowGroupLength is set to the max row group length in bytes (64 * 1024 * 1024).

DataPageSize (integer) --
The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This number is used for .parquet file format only.

ParquetVersion (string) --
The version of the Apache Parquet format that you want to use: parquet_1_0 (the default) or parquet_2_0 .

EnableStatistics (boolean) --
A value that enables statistics for Parquet pages and row groups. Choose true to enable statistics, false to disable. Statistics include NULL , DISTINCT , MAX , and MIN values. This parameter defaults to true . This value is used for .parquet file format only.

IncludeOpForFullLoad (boolean) --
A value that enables a full load to write INSERT operations to the comma-separated value (.csv) output files only to indicate how the rows were added to the source database.

Note
AWS DMS supports the IncludeOpForFullLoad parameter in versions 3.1.4 and later.

For full load, records can only be inserted. By default (the false setting), no information is recorded in these output files for a full load to indicate that the rows were inserted at the source database. If IncludeOpForFullLoad is set to true or y , the INSERT is recorded as an I annotation in the first field of the .csv file. This allows the format of your target records from a full load to be consistent with the target records from a CDC load.

Note
This setting works together with the CdcInsertsOnly and the CdcInsertsAndUpdates parameters for output to .csv files only. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .


CdcInsertsOnly (boolean) --
A value that enables a change data capture (CDC) load to write only INSERT operations to .csv or columnar storage (.parquet) output files. By default (the false setting), the first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated, or deleted at the source database for a CDC load to the target.
If CdcInsertsOnly is set to true or y , only INSERTs from the source database are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded depends on the value of IncludeOpForFullLoad . If IncludeOpForFullLoad is set to true , the first field of every CDC record is set to I to indicate the INSERT operation at the source. If IncludeOpForFullLoad is set to false , every CDC record is written without a first field to indicate the INSERT operation at the source. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .

Note
AWS DMS supports the interaction described preceding between the CdcInsertsOnly and IncludeOpForFullLoad parameters in versions 3.1.4 and later.

CdcInsertsOnly and CdcInsertsAndUpdates can\'t both be set to true for the same endpoint. Set either CdcInsertsOnly or CdcInsertsAndUpdates to true for the same endpoint, but not both.



TimestampColumnName (string) --
A value that when nonblank causes AWS DMS to add a column with timestamp information to the endpoint data for an Amazon S3 target.

Note
AWS DMS supports the TimestampColumnName parameter in versions 3.1.4 and later.

DMS includes an additional STRING column in the .csv or .parquet object files of your migrated data when you set TimestampColumnName to a nonblank value.
For a full load, each row of this timestamp column contains a timestamp for when the data was transferred from the source to the target by DMS.
For a change data capture (CDC) load, each row of the timestamp column contains the timestamp for the commit of that row in the source database.
The string format for this timestamp column value is yyyy-MM-dd HH:mm:ss.SSSSSS . By default, the precision of this value is in microseconds. For a CDC load, the rounding of the precision depends on the commit timestamp supported by DMS for the source database.
When the AddColumnName parameter is set to true , DMS also includes a name for the timestamp column that you set with TimestampColumnName .

ParquetTimestampInMillisecond (boolean) --
A value that specifies the precision of any TIMESTAMP column values that are written to an Amazon S3 object file in .parquet format.

Note
AWS DMS supports the ParquetTimestampInMillisecond parameter in versions 3.1.4 and later.

When ParquetTimestampInMillisecond is set to true or y , AWS DMS writes all TIMESTAMP columns in a .parquet formatted file with millisecond precision. Otherwise, DMS writes them with microsecond precision.
Currently, Amazon Athena and AWS Glue can handle only millisecond precision for TIMESTAMP values. Set this parameter to true for S3 endpoint object files that are .parquet formatted only if you plan to query or process the data with Athena or AWS Glue.

Note
AWS DMS writes any TIMESTAMP column values written to an S3 file in .csv format with microsecond precision.
Setting ParquetTimestampInMillisecond has no effect on the string format of the timestamp column value that is inserted by setting the TimestampColumnName parameter.


CdcInsertsAndUpdates (boolean) --
A value that enables a change data capture (CDC) load to write INSERT and UPDATE operations to .csv or .parquet (columnar storage) output files. The default setting is false , but when CdcInsertsAndUpdates is set to true or y , INSERTs and UPDATEs from the source database are migrated to the .csv or .parquet file.
For .csv file format only, how these INSERTs and UPDATEs are recorded depends on the value of the IncludeOpForFullLoad parameter. If IncludeOpForFullLoad is set to true , the first field of every CDC record is set to either I or U to indicate INSERT and UPDATE operations at the source. But if IncludeOpForFullLoad is set to false , CDC records are written without an indication of INSERT or UPDATE operations at the source. For more information about how these settings work together, see Indicating Source DB Operations in Migrated S3 Data in the AWS Database Migration Service User Guide. .

Note
AWS DMS supports the use of the CdcInsertsAndUpdates parameter in versions 3.3.1 and later.

CdcInsertsOnly and CdcInsertsAndUpdates can\'t both be set to true for the same endpoint. Set either CdcInsertsOnly or CdcInsertsAndUpdates to true for the same endpoint, but not both.





DmsTransferSettings (dict) --
The settings in JSON format for the DMS transfer type of source endpoint.
Possible settings include the following:

ServiceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.
BucketName - The name of the S3 bucket to use.
CompressionType - An optional parameter to use GZIP to compress the target files. To use GZIP, set this value to NONE (the default). To keep the files uncompressed, don\'t use this value.

Shorthand syntax for these settings is as follows: ServiceAccessRoleArn=string,BucketName=string,CompressionType=string
JSON syntax for these settings is as follows: { "ServiceAccessRoleArn": "string", "BucketName": "string", "CompressionType": "none"|"gzip" }

ServiceAccessRoleArn (string) --
The IAM role that has permission to access the Amazon S3 bucket.

BucketName (string) --
The name of the S3 bucket to use.



MongoDbSettings (dict) --
The settings for the MongoDB source endpoint. For more information, see the MongoDbSettings structure.

Username (string) --
The user name you use to access the MongoDB source endpoint.

Password (string) --
The password for the user account you use to access the MongoDB source endpoint.

ServerName (string) --
The name of the server on the MongoDB source endpoint.

Port (integer) --
The port value for the MongoDB source endpoint.

DatabaseName (string) --
The database name on the MongoDB source endpoint.

AuthType (string) --
The authentication type you use to access the MongoDB source endpoint.
Valid values: NO, PASSWORD
When NO is selected, user name and password parameters are not used and can be empty.

AuthMechanism (string) --
The authentication mechanism you use to access the MongoDB source endpoint.
Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1
DEFAULT \xe2\x80\x93 For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use SCRAM_SHA_1. This setting isn\'t used when authType=No.

NestingLevel (string) --
Specifies either document or table mode.
Valid values: NONE, ONE
Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

ExtractDocId (string) --
Specifies the document ID. Use this setting when NestingLevel is set to NONE.
Default value is false.

DocsToInvestigate (string) --
Indicates the number of documents to preview to determine the document organization. Use this setting when NestingLevel is set to ONE.
Must be a positive value greater than 0. Default value is 1000.

AuthSource (string) --
The MongoDB database name. This setting isn\'t used when authType=NO .
The default is admin.

KmsKeyId (string) --
The AWS KMS key identifier that is used to encrypt the content on the replication instance. If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.



KinesisSettings (dict) --
The settings for the Amazon Kinesis target endpoint. For more information, see the KinesisSettings structure.

StreamArn (string) --
The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

MessageFormat (string) --
The output format for the records created on the endpoint. The message format is JSON (default) or JSON_UNFORMATTED (a single line with no tab).

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) for the AWS Identity and Access Management (IAM) role that AWS DMS uses to write to the Kinesis data stream.

IncludeTransactionDetails (boolean) --
Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for transaction_id , previous transaction_id , and transaction_record_id (the record offset within a transaction). The default is False .

IncludePartitionValue (boolean) --
Shows the partition value within the Kinesis message output, unless the partition type is schema-table-type . The default is False .

PartitionIncludeSchemaTable (boolean) --
Prefixes schema and table names to partition values, when the partition type is primary-key-type . Doing this increases data distribution among Kinesis shards. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same shard, which causes throttling. The default is False .

IncludeTableAlterOperations (boolean) --
Includes any data definition language (DDL) operations that change the table in the control data, such as rename-table , drop-table , add-column , drop-column , and rename-column . The default is False .

IncludeControlDetails (boolean) --
Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output. The default is False .



KafkaSettings (dict) --
The settings for the Apache Kafka target endpoint. For more information, see the KafkaSettings structure.

Broker (string) --
The broker location and port of the Kafka broker that hosts your Kafka instance. Specify the broker in the form `` broker-hostname-or-ip :port `` . For example, "ec2-12-345-678-901.compute-1.amazonaws.com:2345" .

Topic (string) --
The topic to which you migrate the data. If you don\'t specify a topic, AWS DMS specifies "kafka-default-topic" as the migration topic.



ElasticsearchSettings (dict) --
The settings for the Elasticsearch source endpoint. For more information, see the ElasticsearchSettings structure.

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) used by service to access the IAM role.

EndpointUri (string) --
The endpoint for the Elasticsearch cluster.

FullLoadErrorPercentage (integer) --
The maximum percentage of records that can fail to be written before a full load operation stops.

ErrorRetryDuration (integer) --
The maximum number of seconds for which DMS retries failed API requests to the Elasticsearch cluster.



NeptuneSettings (dict) --
The settings for the MongoDB source endpoint. For more information, see the NeptuneSettings structure.

ServiceAccessRoleArn (string) --
The ARN of the service role you have created for the Neptune target endpoint. For more information, see https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.ServiceRole in the AWS Database Migration Service User Guide.

S3BucketName (string) --
The name of the S3 bucket for AWS DMS to temporarily store migrated graph data in CSV files before bulk-loading it to the Neptune target database. AWS DMS maps the SQL source data to graph data before storing it in these CSV files.

S3BucketFolder (string) --
A folder path where you where you want AWS DMS to store migrated graph data in the S3 bucket specified by S3BucketName

ErrorRetryDuration (integer) --
The number of milliseconds for AWS DMS to wait to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 250.

MaxFileSize (integer) --
The maximum size in KB of migrated graph data stored in a CSV file before AWS DMS bulk-loads the data to the Neptune target database. The default is 1048576 KB. If successful, AWS DMS clears the bucket, ready to store the next batch of migrated graph data.

MaxRetryCount (integer) --
The number of times for AWS DMS to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 5.

IamAuthEnabled (boolean) --
If you want IAM authorization enabled for this endpoint, set this parameter to true and attach the appropriate role policy document to your service role specified by ServiceAccessRoleArn . The default is false .



RedshiftSettings (dict) --
Settings for the Amazon Redshift endpoint.

AcceptAnyDate (boolean) --
A value that indicates to allow any date format, including invalid formats such as 00/00/00 00:00:00, to be loaded without generating an error. You can choose true or false (the default).
This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data doesn\'t match the DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

AfterConnectScript (string) --
Code to run after connecting. This parameter should contain the code itself, not the name of a file containing the code.

BucketFolder (string) --
The location where the comma-separated value (.csv) files are stored before being uploaded to the S3 bucket.

BucketName (string) --
The name of the S3 bucket you want to use

ConnectionTimeout (integer) --
A value that sets the amount of time to wait (in milliseconds) before timing out, beginning from when you initially establish a connection.

DatabaseName (string) --
The name of the Amazon Redshift data warehouse (service) that you are working with.

DateFormat (string) --
The date format that you are using. Valid values are auto (case-sensitive), your date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults to a format of \'YYYY-MM-DD\'. Using auto recognizes most strings, even some that aren\'t supported when you use a date format string.
If your date and time values use formats different from each other, set this to auto .

EmptyAsNull (boolean) --
A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL. A value of true sets empty CHAR and VARCHAR fields to null. The default is false .

EncryptionMode (string) --
The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either SSE_S3 (the default) or SSE_KMS . To use SSE_S3 , create an AWS Identity and Access Management (IAM) role with a policy that allows "arn:aws:s3:::*" to use the following actions: "s3:PutObject", "s3:ListBucket"

FileTransferUploadStreams (integer) --
The number of threads used to upload a single file. This parameter accepts a value from 1 through 64. It defaults to 10.

LoadTimeout (integer) --
The amount of time to wait (in milliseconds) before timing out, beginning from when you begin loading.

MaxFileSize (integer) --
The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

Password (string) --
The password for the user named in the username property.

Port (integer) --
The port number for Amazon Redshift. The default value is 5439.

RemoveQuotes (boolean) --
A value that specifies to remove surrounding quotation marks from strings in the incoming data. All characters within the quotation marks, including delimiters, are retained. Choose true to remove quotation marks. The default is false .

ReplaceInvalidChars (string) --
A list of characters that you want to replace. Use with ReplaceChars .

ReplaceChars (string) --
A value that specifies to replaces the invalid characters specified in ReplaceInvalidChars , substituting the specified characters instead. The default is "?" .

ServerName (string) --
The name of the Amazon Redshift cluster you are using.

ServiceAccessRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service.

ServerSideEncryptionKmsKeyId (string) --
The AWS KMS key ID. If you are using SSE_KMS for the EncryptionMode , provide this key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.

TimeFormat (string) --
The time format that you want to use. Valid values are auto (case-sensitive), \'timeformat_string\' , \'epochsecs\' , or \'epochmillisecs\' . It defaults to 10. Using auto recognizes most strings, even some that aren\'t supported when you use a time format string.
If your date and time values use formats different from each other, set this parameter to auto .

TrimBlanks (boolean) --
A value that specifies to remove the trailing white space characters from a VARCHAR string. This parameter applies only to columns with a VARCHAR data type. Choose true to remove unneeded white space. The default is false .

TruncateColumns (boolean) --
A value that specifies to truncate data in columns to the appropriate number of characters, so that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose true to truncate data. The default is false .

Username (string) --
An Amazon Redshift user name for a registered user.

WriteBufferSize (integer) --
The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The default is 1,024. Use this setting to tune performance.











Exceptions

DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.ResourceAlreadyExistsFault
DatabaseMigrationService.Client.exceptions.KMSKeyNotAccessibleFault
DatabaseMigrationService.Client.exceptions.AccessDeniedFault

Examples
Modifies the specified endpoint.
response = client.modify_endpoint(
    CertificateArn='',
    DatabaseName='',
    EndpointArn='',
    EndpointIdentifier='',
    EndpointType='source',
    EngineName='',
    ExtraConnectionAttributes='',
    Password='',
    Port=123,
    ServerName='',
    SslMode='require',
    Username='',
)

print(response)


Expected Output:
{
    'Endpoint': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Endpoint': {
            'EndpointIdentifier': 'string',
            'EndpointType': 'source'|'target',
            'EngineName': 'string',
            'EngineDisplayName': 'string',
            'Username': 'string',
            'ServerName': 'string',
            'Port': 123,
            'DatabaseName': 'string',
            'ExtraConnectionAttributes': 'string',
            'Status': 'string',
            'KmsKeyId': 'string',
            'EndpointArn': 'string',
            'CertificateArn': 'string',
            'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
            'ServiceAccessRoleArn': 'string',
            'ExternalTableDefinition': 'string',
            'ExternalId': 'string',
            'DynamoDbSettings': {
                'ServiceAccessRoleArn': 'string'
            },
            'S3Settings': {
                'ServiceAccessRoleArn': 'string',
                'ExternalTableDefinition': 'string',
                'CsvRowDelimiter': 'string',
                'CsvDelimiter': 'string',
                'BucketFolder': 'string',
                'BucketName': 'string',
                'CompressionType': 'none'|'gzip',
                'EncryptionMode': 'sse-s3'|'sse-kms',
                'ServerSideEncryptionKmsKeyId': 'string',
                'DataFormat': 'csv'|'parquet',
                'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
                'DictPageSizeLimit': 123,
                'RowGroupLength': 123,
                'DataPageSize': 123,
                'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
                'EnableStatistics': True|False,
                'IncludeOpForFullLoad': True|False,
                'CdcInsertsOnly': True|False,
                'TimestampColumnName': 'string',
                'ParquetTimestampInMillisecond': True|False,
                'CdcInsertsAndUpdates': True|False
            },
            'DmsTransferSettings': {
                'ServiceAccessRoleArn': 'string',
                'BucketName': 'string'
            },
            'MongoDbSettings': {
                'Username': 'string',
                'Password': 'string',
                'ServerName': 'string',
                'Port': 123,
                'DatabaseName': 'string',
                'AuthType': 'no'|'password',
                'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                'NestingLevel': 'none'|'one',
                'ExtractDocId': 'string',
                'DocsToInvestigate': 'string',
                'AuthSource': 'string',
                'KmsKeyId': 'string'
            },
            'KinesisSettings': {
                'StreamArn': 'string',
                'MessageFormat': 'json'|'json-unformatted',
                'ServiceAccessRoleArn': 'string',
                'IncludeTransactionDetails': True|False,
                'IncludePartitionValue': True|False,
                'PartitionIncludeSchemaTable': True|False,
                'IncludeTableAlterOperations': True|False,
                'IncludeControlDetails': True|False
            },
            'KafkaSettings': {
                'Broker': 'string',
                'Topic': 'string'
            },
            'ElasticsearchSettings': {
                'ServiceAccessRoleArn': 'string',
                'EndpointUri': 'string',
                'FullLoadErrorPercentage': 123,
                'ErrorRetryDuration': 123
            },
            'NeptuneSettings': {
                'ServiceAccessRoleArn': 'string',
                'S3BucketName': 'string',
                'S3BucketFolder': 'string',
                'ErrorRetryDuration': 123,
                'MaxFileSize': 123,
                'MaxRetryCount': 123,
                'IamAuthEnabled': True|False
            },
            'RedshiftSettings': {
                'AcceptAnyDate': True|False,
                'AfterConnectScript': 'string',
                'BucketFolder': 'string',
                'BucketName': 'string',
                'ConnectionTimeout': 123,
                'DatabaseName': 'string',
                'DateFormat': 'string',
                'EmptyAsNull': True|False,
                'EncryptionMode': 'sse-s3'|'sse-kms',
                'FileTransferUploadStreams': 123,
                'LoadTimeout': 123,
                'MaxFileSize': 123,
                'Password': 'string',
                'Port': 123,
                'RemoveQuotes': True|False,
                'ReplaceInvalidChars': 'string',
                'ReplaceChars': 'string',
                'ServerName': 'string',
                'ServiceAccessRoleArn': 'string',
                'ServerSideEncryptionKmsKeyId': 'string',
                'TimeFormat': 'string',
                'TrimBlanks': True|False,
                'TruncateColumns': True|False,
                'Username': 'string',
                'WriteBufferSize': 123
            }
        }
    }
    
    
    :returns: 
    s3:CreateBucket
    s3:ListBucket
    s3:DeleteBucket
    s3:GetBucketLocation
    s3:GetObject
    s3:PutObject
    s3:DeleteObject
    s3:GetObjectVersion
    s3:GetBucketPolicy
    s3:PutBucketPolicy
    s3:DeleteBucketPolicy
    
    """
    pass

def modify_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, EventCategories=None, Enabled=None):
    """
    Modifies an existing AWS DMS event notification subscription.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_event_subscription(
        SubscriptionName='string',
        SnsTopicArn='string',
        SourceType='string',
        EventCategories=[
            'string',
        ],
        Enabled=True|False
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]\nThe name of the AWS DMS event notification subscription to be modified.\n

    :type SnsTopicArn: string
    :param SnsTopicArn: The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.

    :type SourceType: string
    :param SourceType: The type of AWS DMS resource that generates the events you want to subscribe to.\nValid values: replication-instance | replication-task\n

    :type EventCategories: list
    :param EventCategories: A list of event categories for a source type that you want to subscribe to. Use the DescribeEventCategories action to see a list of event categories.\n\n(string) --\n\n

    :type Enabled: boolean
    :param Enabled: A Boolean value; set to true to activate the subscription.

    :rtype: dict

ReturnsResponse Syntax
{
    'EventSubscription': {
        'CustomerAwsId': 'string',
        'CustSubscriptionId': 'string',
        'SnsTopicArn': 'string',
        'Status': 'string',
        'SubscriptionCreationTime': 'string',
        'SourceType': 'string',
        'SourceIdsList': [
            'string',
        ],
        'EventCategoriesList': [
            'string',
        ],
        'Enabled': True|False
    }
}


Response Structure

(dict) --

EventSubscription (dict) --
The modified event subscription.

CustomerAwsId (string) --
The AWS customer account associated with the AWS DMS event notification subscription.

CustSubscriptionId (string) --
The AWS DMS event notification subscription Id.

SnsTopicArn (string) --
The topic ARN of the AWS DMS event notification subscription.

Status (string) --
The status of the AWS DMS event notification subscription.
Constraints:
Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
The status "no-permission" indicates that AWS DMS no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.

SubscriptionCreationTime (string) --
The time the RDS event notification subscription was created.

SourceType (string) --
The type of AWS DMS resource that generates events.
Valid values: replication-instance | replication-server | security-group | replication-task

SourceIdsList (list) --
A list of source Ids for the event subscription.

(string) --


EventCategoriesList (list) --
A lists of event categories.

(string) --


Enabled (boolean) --
Boolean value that indicates if the event subscription is enabled.









Exceptions

DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.SNSInvalidTopicFault
DatabaseMigrationService.Client.exceptions.SNSNoAuthorizationFault
DatabaseMigrationService.Client.exceptions.KMSAccessDeniedFault
DatabaseMigrationService.Client.exceptions.KMSDisabledFault
DatabaseMigrationService.Client.exceptions.KMSInvalidStateFault
DatabaseMigrationService.Client.exceptions.KMSNotFoundFault
DatabaseMigrationService.Client.exceptions.KMSThrottlingFault


    :return: {
        'EventSubscription': {
            'CustomerAwsId': 'string',
            'CustSubscriptionId': 'string',
            'SnsTopicArn': 'string',
            'Status': 'string',
            'SubscriptionCreationTime': 'string',
            'SourceType': 'string',
            'SourceIdsList': [
                'string',
            ],
            'EventCategoriesList': [
                'string',
            ],
            'Enabled': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def modify_replication_instance(ReplicationInstanceArn=None, AllocatedStorage=None, ApplyImmediately=None, ReplicationInstanceClass=None, VpcSecurityGroupIds=None, PreferredMaintenanceWindow=None, MultiAZ=None, EngineVersion=None, AllowMajorVersionUpgrade=None, AutoMinorVersionUpgrade=None, ReplicationInstanceIdentifier=None):
    """
    Modifies the replication instance to apply new settings. You can change one or more parameters by specifying these parameters and the new values in the request.
    Some settings are applied during the maintenance window.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Modifies the replication instance to apply new settings. You can change one or more parameters by specifying these parameters and the new values in the request. Some settings are applied during the maintenance window.
    Expected Output:
    
    :example: response = client.modify_replication_instance(
        ReplicationInstanceArn='string',
        AllocatedStorage=123,
        ApplyImmediately=True|False,
        ReplicationInstanceClass='string',
        VpcSecurityGroupIds=[
            'string',
        ],
        PreferredMaintenanceWindow='string',
        MultiAZ=True|False,
        EngineVersion='string',
        AllowMajorVersionUpgrade=True|False,
        AutoMinorVersionUpgrade=True|False,
        ReplicationInstanceIdentifier='string'
    )
    
    
    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the replication instance.\n

    :type AllocatedStorage: integer
    :param AllocatedStorage: The amount of storage (in gigabytes) to be allocated for the replication instance.

    :type ApplyImmediately: boolean
    :param ApplyImmediately: Indicates whether the changes should be applied immediately or during the next maintenance window.

    :type ReplicationInstanceClass: string
    :param ReplicationInstanceClass: The compute and memory capacity of the replication instance.\nValid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge\n

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance.\n\n(string) --\n\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter does not result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.\nDefault: Uses existing setting\nFormat: ddd:hh24:mi-ddd:hh24:mi\nValid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun\nConstraints: Must be at least 30 minutes\n

    :type MultiAZ: boolean
    :param MultiAZ: Specifies whether the replication instance is a Multi-AZ deployment. You can\'t set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .

    :type EngineVersion: string
    :param EngineVersion: The engine version number of the replication instance.

    :type AllowMajorVersionUpgrade: boolean
    :param AllowMajorVersionUpgrade: Indicates that major version upgrades are allowed. Changing this parameter does not result in an outage, and the change is asynchronously applied as soon as possible.\nThis parameter must be set to true when specifying a value for the EngineVersion parameter that is a different major version than the replication instance\'s current version.\n

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: A value that indicates that minor version upgrades are applied automatically to the replication instance during the maintenance window. Changing this parameter doesn\'t result in an outage, except in the case dsecribed following. The change is asynchronously applied as soon as possible.\nAn outage does result if these factors apply:\n\nThis parameter is set to true during the maintenance window.\nA newer minor version is available.\nAWS DMS has enabled automatic patching for the given engine version.\n\n

    :type ReplicationInstanceIdentifier: string
    :param ReplicationInstanceIdentifier: The replication instance identifier. This parameter is stored as a lowercase string.

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationInstance': {
        'ReplicationInstanceIdentifier': 'string',
        'ReplicationInstanceClass': 'string',
        'ReplicationInstanceStatus': 'string',
        'AllocatedStorage': 123,
        'InstanceCreateTime': datetime(2015, 1, 1),
        'VpcSecurityGroups': [
            {
                'VpcSecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'AvailabilityZone': 'string',
        'ReplicationSubnetGroup': {
            'ReplicationSubnetGroupIdentifier': 'string',
            'ReplicationSubnetGroupDescription': 'string',
            'VpcId': 'string',
            'SubnetGroupStatus': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': {
                        'Name': 'string'
                    },
                    'SubnetStatus': 'string'
                },
            ]
        },
        'PreferredMaintenanceWindow': 'string',
        'PendingModifiedValues': {
            'ReplicationInstanceClass': 'string',
            'AllocatedStorage': 123,
            'MultiAZ': True|False,
            'EngineVersion': 'string'
        },
        'MultiAZ': True|False,
        'EngineVersion': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'KmsKeyId': 'string',
        'ReplicationInstanceArn': 'string',
        'ReplicationInstancePublicIpAddress': 'string',
        'ReplicationInstancePrivateIpAddress': 'string',
        'ReplicationInstancePublicIpAddresses': [
            'string',
        ],
        'ReplicationInstancePrivateIpAddresses': [
            'string',
        ],
        'PubliclyAccessible': True|False,
        'SecondaryAvailabilityZone': 'string',
        'FreeUntil': datetime(2015, 1, 1),
        'DnsNameServers': 'string'
    }
}


Response Structure

(dict) --

ReplicationInstance (dict) --
The modified replication instance.

ReplicationInstanceIdentifier (string) --
The replication instance identifier. This parameter is stored as a lowercase string.
Constraints:

Must contain from 1 to 63 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.

Example: myrepinstance

ReplicationInstanceClass (string) --
The compute and memory capacity of the replication instance.
Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge

ReplicationInstanceStatus (string) --
The status of the replication instance.

AllocatedStorage (integer) --
The amount of storage (in gigabytes) that is allocated for the replication instance.

InstanceCreateTime (datetime) --
The time the replication instance was created.

VpcSecurityGroups (list) --
The VPC security group for the instance.

(dict) --
Describes status of a security group associated with the virtual private cloud hosting your replication and DB instances.

VpcSecurityGroupId (string) --
The VPC security group Id.

Status (string) --
The status of the VPC security group.





AvailabilityZone (string) --
The Availability Zone for the instance.

ReplicationSubnetGroup (dict) --
The subnet group for the replication instance.

ReplicationSubnetGroupIdentifier (string) --
The identifier of the replication instance subnet group.

ReplicationSubnetGroupDescription (string) --
A description for the replication subnet group.

VpcId (string) --
The ID of the VPC.

SubnetGroupStatus (string) --
The status of the subnet group.

Subnets (list) --
The subnets that are in the subnet group.

(dict) --
In response to a request by the DescribeReplicationSubnetGroup operation, this object identifies a subnet by its given Availability Zone, subnet identifier, and status.

SubnetIdentifier (string) --
The subnet identifier.

SubnetAvailabilityZone (dict) --
The Availability Zone of the subnet.

Name (string) --
The name of the Availability Zone.



SubnetStatus (string) --
The status of the subnet.







PreferredMaintenanceWindow (string) --
The maintenance window times for the replication instance.

PendingModifiedValues (dict) --
The pending modification values.

ReplicationInstanceClass (string) --
The compute and memory capacity of the replication instance.
Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge

AllocatedStorage (integer) --
The amount of storage (in gigabytes) that is allocated for the replication instance.

MultiAZ (boolean) --
Specifies whether the replication instance is a Multi-AZ deployment. You can\'t set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .

EngineVersion (string) --
The engine version number of the replication instance.



MultiAZ (boolean) --
Specifies whether the replication instance is a Multi-AZ deployment. You can\'t set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .

EngineVersion (string) --
The engine version number of the replication instance.

AutoMinorVersionUpgrade (boolean) --
Boolean value indicating if minor version upgrades will be automatically applied to the instance.

KmsKeyId (string) --
An AWS KMS key identifier that is used to encrypt the data on the replication instance.
If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key.
AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.

ReplicationInstanceArn (string) --
The Amazon Resource Name (ARN) of the replication instance.

ReplicationInstancePublicIpAddress (string) --
The public IP address of the replication instance.

ReplicationInstancePrivateIpAddress (string) --
The private IP address of the replication instance.

ReplicationInstancePublicIpAddresses (list) --
One or more public IP addresses for the replication instance.

(string) --


ReplicationInstancePrivateIpAddresses (list) --
One or more private IP addresses for the replication instance.

(string) --


PubliclyAccessible (boolean) --
Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address. The default value is true .

SecondaryAvailabilityZone (string) --
The Availability Zone of the standby replication instance in a Multi-AZ deployment.

FreeUntil (datetime) --
The expiration date of the free replication instance that is part of the Free DMS program.

DnsNameServers (string) --
The DNS name servers for the replication instance.









Exceptions

DatabaseMigrationService.Client.exceptions.AccessDeniedFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
DatabaseMigrationService.Client.exceptions.ResourceAlreadyExistsFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.InsufficientResourceCapacityFault
DatabaseMigrationService.Client.exceptions.StorageQuotaExceededFault
DatabaseMigrationService.Client.exceptions.UpgradeDependencyFailureFault

Examples
Modifies the replication instance to apply new settings. You can change one or more parameters by specifying these parameters and the new values in the request. Some settings are applied during the maintenance window.
response = client.modify_replication_instance(
    AllocatedStorage=123,
    AllowMajorVersionUpgrade=True,
    ApplyImmediately=True,
    AutoMinorVersionUpgrade=True,
    EngineVersion='1.5.0',
    MultiAZ=True,
    PreferredMaintenanceWindow='sun:06:00-sun:14:00',
    ReplicationInstanceArn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ',
    ReplicationInstanceClass='dms.t2.micro',
    ReplicationInstanceIdentifier='test-rep-1',
    VpcSecurityGroupIds=[
    ],
)

print(response)


Expected Output:
{
    'ReplicationInstance': {
        'AllocatedStorage': 5,
        'AutoMinorVersionUpgrade': True,
        'EngineVersion': '1.5.0',
        'KmsKeyId': 'arn:aws:kms:us-east-1:123456789012:key/4c1731d6-5435-ed4d-be13-d53411a7cfbd',
        'PendingModifiedValues': {
        },
        'PreferredMaintenanceWindow': 'sun:06:00-sun:14:00',
        'PubliclyAccessible': True,
        'ReplicationInstanceArn': 'arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ',
        'ReplicationInstanceClass': 'dms.t2.micro',
        'ReplicationInstanceIdentifier': 'test-rep-1',
        'ReplicationInstanceStatus': 'available',
        'ReplicationSubnetGroup': {
            'ReplicationSubnetGroupDescription': 'default',
            'ReplicationSubnetGroupIdentifier': 'default',
            'SubnetGroupStatus': 'Complete',
            'Subnets': [
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1d',
                    },
                    'SubnetIdentifier': 'subnet-f6dd91af',
                    'SubnetStatus': 'Active',
                },
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1b',
                    },
                    'SubnetIdentifier': 'subnet-3605751d',
                    'SubnetStatus': 'Active',
                },
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1c',
                    },
                    'SubnetIdentifier': 'subnet-c2daefb5',
                    'SubnetStatus': 'Active',
                },
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1e',
                    },
                    'SubnetIdentifier': 'subnet-85e90cb8',
                    'SubnetStatus': 'Active',
                },
            ],
            'VpcId': 'vpc-6741a603',
        },
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReplicationInstance': {
            'ReplicationInstanceIdentifier': 'string',
            'ReplicationInstanceClass': 'string',
            'ReplicationInstanceStatus': 'string',
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'ReplicationSubnetGroup': {
                'ReplicationSubnetGroupIdentifier': 'string',
                'ReplicationSubnetGroupDescription': 'string',
                'VpcId': 'string',
                'SubnetGroupStatus': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        },
                        'SubnetStatus': 'string'
                    },
                ]
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'ReplicationInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string'
            },
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'KmsKeyId': 'string',
            'ReplicationInstanceArn': 'string',
            'ReplicationInstancePublicIpAddress': 'string',
            'ReplicationInstancePrivateIpAddress': 'string',
            'ReplicationInstancePublicIpAddresses': [
                'string',
            ],
            'ReplicationInstancePrivateIpAddresses': [
                'string',
            ],
            'PubliclyAccessible': True|False,
            'SecondaryAvailabilityZone': 'string',
            'FreeUntil': datetime(2015, 1, 1),
            'DnsNameServers': 'string'
        }
    }
    
    
    :returns: 
    Must contain from 1 to 63 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def modify_replication_subnet_group(ReplicationSubnetGroupIdentifier=None, ReplicationSubnetGroupDescription=None, SubnetIds=None):
    """
    Modifies the settings for the specified replication subnet group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Modifies the settings for the specified replication subnet group.
    Expected Output:
    
    :example: response = client.modify_replication_subnet_group(
        ReplicationSubnetGroupIdentifier='string',
        ReplicationSubnetGroupDescription='string',
        SubnetIds=[
            'string',
        ]
    )
    
    
    :type ReplicationSubnetGroupIdentifier: string
    :param ReplicationSubnetGroupIdentifier: [REQUIRED]\nThe name of the replication instance subnet group.\n

    :type ReplicationSubnetGroupDescription: string
    :param ReplicationSubnetGroupDescription: A description for the replication instance subnet group.

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nA list of subnet IDs.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationSubnetGroup': {
        'ReplicationSubnetGroupIdentifier': 'string',
        'ReplicationSubnetGroupDescription': 'string',
        'VpcId': 'string',
        'SubnetGroupStatus': 'string',
        'Subnets': [
            {
                'SubnetIdentifier': 'string',
                'SubnetAvailabilityZone': {
                    'Name': 'string'
                },
                'SubnetStatus': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

ReplicationSubnetGroup (dict) --
The modified replication subnet group.

ReplicationSubnetGroupIdentifier (string) --
The identifier of the replication instance subnet group.

ReplicationSubnetGroupDescription (string) --
A description for the replication subnet group.

VpcId (string) --
The ID of the VPC.

SubnetGroupStatus (string) --
The status of the subnet group.

Subnets (list) --
The subnets that are in the subnet group.

(dict) --
In response to a request by the DescribeReplicationSubnetGroup operation, this object identifies a subnet by its given Availability Zone, subnet identifier, and status.

SubnetIdentifier (string) --
The subnet identifier.

SubnetAvailabilityZone (dict) --
The Availability Zone of the subnet.

Name (string) --
The name of the Availability Zone.



SubnetStatus (string) --
The status of the subnet.













Exceptions

DatabaseMigrationService.Client.exceptions.AccessDeniedFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault
DatabaseMigrationService.Client.exceptions.SubnetAlreadyInUse
DatabaseMigrationService.Client.exceptions.ReplicationSubnetGroupDoesNotCoverEnoughAZs
DatabaseMigrationService.Client.exceptions.InvalidSubnet

Examples
Modifies the settings for the specified replication subnet group.
response = client.modify_replication_subnet_group(
    ReplicationSubnetGroupDescription='',
    ReplicationSubnetGroupIdentifier='',
    SubnetIds=[
    ],
)

print(response)


Expected Output:
{
    'ReplicationSubnetGroup': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReplicationSubnetGroup': {
            'ReplicationSubnetGroupIdentifier': 'string',
            'ReplicationSubnetGroupDescription': 'string',
            'VpcId': 'string',
            'SubnetGroupStatus': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': {
                        'Name': 'string'
                    },
                    'SubnetStatus': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.AccessDeniedFault
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault
    DatabaseMigrationService.Client.exceptions.SubnetAlreadyInUse
    DatabaseMigrationService.Client.exceptions.ReplicationSubnetGroupDoesNotCoverEnoughAZs
    DatabaseMigrationService.Client.exceptions.InvalidSubnet
    
    """
    pass

def modify_replication_task(ReplicationTaskArn=None, ReplicationTaskIdentifier=None, MigrationType=None, TableMappings=None, ReplicationTaskSettings=None, CdcStartTime=None, CdcStartPosition=None, CdcStopPosition=None, TaskData=None):
    """
    Modifies the specified replication task.
    You can\'t modify the task endpoints. The task must be stopped before you can modify it.
    For more information about AWS DMS tasks, see Working with Migration Tasks in the AWS Database Migration Service User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_replication_task(
        ReplicationTaskArn='string',
        ReplicationTaskIdentifier='string',
        MigrationType='full-load'|'cdc'|'full-load-and-cdc',
        TableMappings='string',
        ReplicationTaskSettings='string',
        CdcStartTime=datetime(2015, 1, 1),
        CdcStartPosition='string',
        CdcStopPosition='string',
        TaskData='string'
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the replication task.\n

    :type ReplicationTaskIdentifier: string
    :param ReplicationTaskIdentifier: The replication task identifier.\nConstraints:\n\nMust contain from 1 to 255 alphanumeric characters or hyphens.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\n

    :type MigrationType: string
    :param MigrationType: The migration type. Valid values: full-load | cdc | full-load-and-cdc

    :type TableMappings: string
    :param TableMappings: When using the AWS CLI or boto3, provide the path of the JSON file that contains the table mappings. Precede the path with file:// . When working with the DMS API, provide the JSON as the parameter value, for example: --table-mappings file://mappingfile.json

    :type ReplicationTaskSettings: string
    :param ReplicationTaskSettings: JSON file that contains settings for the task, such as task metadata settings.

    :type CdcStartTime: datetime
    :param CdcStartTime: Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.\nTimestamp Example: --cdc-start-time \xe2\x80\x9c2018-03-08T12:12:12\xe2\x80\x9d\n

    :type CdcStartPosition: string
    :param CdcStartPosition: Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.\nThe value can be in date, checkpoint, or LSN/SCN format.\nDate Example: --cdc-start-position \xe2\x80\x9c2018-03-08T12:12:12\xe2\x80\x9d\nCheckpoint Example: --cdc-start-position 'checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93'\nLSN Example: --cdc-start-position \xe2\x80\x9cmysql-bin-changelog.000024:373\xe2\x80\x9d\n\nNote\nWhen you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the slotName extra connection attribute to the name of this logical replication slot. For more information, see Extra Connection Attributes When Using PostgreSQL as a Source for AWS DMS .\n\n

    :type CdcStopPosition: string
    :param CdcStopPosition: Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.\nServer time example: --cdc-stop-position \xe2\x80\x9cserver_time:3018-02-09T12:12:12\xe2\x80\x9d\nCommit time example: --cdc-stop-position \xe2\x80\x9ccommit_time: 3018-02-09T12:12:12 \xe2\x80\x9c\n

    :type TaskData: string
    :param TaskData: Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see Specifying Supplemental Data for Task Settings in the AWS Database Migration User Guide.

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationTask': {
        'ReplicationTaskIdentifier': 'string',
        'SourceEndpointArn': 'string',
        'TargetEndpointArn': 'string',
        'ReplicationInstanceArn': 'string',
        'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
        'TableMappings': 'string',
        'ReplicationTaskSettings': 'string',
        'Status': 'string',
        'LastFailureMessage': 'string',
        'StopReason': 'string',
        'ReplicationTaskCreationDate': datetime(2015, 1, 1),
        'ReplicationTaskStartDate': datetime(2015, 1, 1),
        'CdcStartPosition': 'string',
        'CdcStopPosition': 'string',
        'RecoveryCheckpoint': 'string',
        'ReplicationTaskArn': 'string',
        'ReplicationTaskStats': {
            'FullLoadProgressPercent': 123,
            'ElapsedTimeMillis': 123,
            'TablesLoaded': 123,
            'TablesLoading': 123,
            'TablesQueued': 123,
            'TablesErrored': 123,
            'FreshStartDate': datetime(2015, 1, 1),
            'StartDate': datetime(2015, 1, 1),
            'StopDate': datetime(2015, 1, 1),
            'FullLoadStartDate': datetime(2015, 1, 1),
            'FullLoadFinishDate': datetime(2015, 1, 1)
        },
        'TaskData': 'string'
    }
}


Response Structure

(dict) --

ReplicationTask (dict) --
The replication task that was modified.

ReplicationTaskIdentifier (string) --
The user-assigned replication task identifier or name.
Constraints:

Must contain from 1 to 255 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.


SourceEndpointArn (string) --
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

TargetEndpointArn (string) --
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

ReplicationInstanceArn (string) --
The Amazon Resource Name (ARN) of the replication instance.

MigrationType (string) --
The type of migration.

TableMappings (string) --
Table mappings specified in the task.

ReplicationTaskSettings (string) --
The settings for the replication task.

Status (string) --
The status of the replication task.

LastFailureMessage (string) --
The last error (failure) message generated for the replication instance.

StopReason (string) --
The reason the replication task was stopped.

ReplicationTaskCreationDate (datetime) --
The date the replication task was created.

ReplicationTaskStartDate (datetime) --
The date the replication task is scheduled to start.

CdcStartPosition (string) --
Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want the CDC operation to start. Specifying both values results in an error.
The value can be in date, checkpoint, or LSN/SCN format.
Date Example: --cdc-start-position \xe2\x80\x9c2018-03-08T12:12:12\xe2\x80\x9d
Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
LSN Example: --cdc-start-position \xe2\x80\x9cmysql-bin-changelog.000024:373\xe2\x80\x9d

CdcStopPosition (string) --
Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
Server time example: --cdc-stop-position \xe2\x80\x9cserver_time:3018-02-09T12:12:12\xe2\x80\x9d
Commit time example: --cdc-stop-position \xe2\x80\x9ccommit_time: 3018-02-09T12:12:12 \xe2\x80\x9c

RecoveryCheckpoint (string) --
Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the CdcStartPosition parameter to start a CDC operation that begins at that checkpoint.

ReplicationTaskArn (string) --
The Amazon Resource Name (ARN) of the replication task.

ReplicationTaskStats (dict) --
The statistics for the task, including elapsed time, tables loaded, and table errors.

FullLoadProgressPercent (integer) --
The percent complete for the full load migration task.

ElapsedTimeMillis (integer) --
The elapsed time of the task, in milliseconds.

TablesLoaded (integer) --
The number of tables loaded for this task.

TablesLoading (integer) --
The number of tables currently loading for this task.

TablesQueued (integer) --
The number of tables queued for this task.

TablesErrored (integer) --
The number of errors that have occurred during this task.

FreshStartDate (datetime) --
The date the replication task was started either with a fresh start or a target reload.

StartDate (datetime) --
The date the replication task was started either with a fresh start or a resume. For more information, see StartReplicationTaskType .

StopDate (datetime) --
The date the replication task was stopped.

FullLoadStartDate (datetime) --
The date the replication task full load was started.

FullLoadFinishDate (datetime) --
The date the replication task full load was completed.



TaskData (string) --
Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see Specifying Supplemental Data for Task Settings in the AWS Database Migration User Guide.









Exceptions

DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.ResourceAlreadyExistsFault
DatabaseMigrationService.Client.exceptions.KMSKeyNotAccessibleFault


    :return: {
        'ReplicationTask': {
            'ReplicationTaskIdentifier': 'string',
            'SourceEndpointArn': 'string',
            'TargetEndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
            'TableMappings': 'string',
            'ReplicationTaskSettings': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'StopReason': 'string',
            'ReplicationTaskCreationDate': datetime(2015, 1, 1),
            'ReplicationTaskStartDate': datetime(2015, 1, 1),
            'CdcStartPosition': 'string',
            'CdcStopPosition': 'string',
            'RecoveryCheckpoint': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationTaskStats': {
                'FullLoadProgressPercent': 123,
                'ElapsedTimeMillis': 123,
                'TablesLoaded': 123,
                'TablesLoading': 123,
                'TablesQueued': 123,
                'TablesErrored': 123,
                'FreshStartDate': datetime(2015, 1, 1),
                'StartDate': datetime(2015, 1, 1),
                'StopDate': datetime(2015, 1, 1),
                'FullLoadStartDate': datetime(2015, 1, 1),
                'FullLoadFinishDate': datetime(2015, 1, 1)
            },
            'TaskData': 'string'
        }
    }
    
    
    :returns: 
    Must contain from 1 to 255 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def reboot_replication_instance(ReplicationInstanceArn=None, ForceFailover=None):
    """
    Reboots a replication instance. Rebooting results in a momentary outage, until the replication instance becomes available again.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reboot_replication_instance(
        ReplicationInstanceArn='string',
        ForceFailover=True|False
    )
    
    
    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the replication instance.\n

    :type ForceFailover: boolean
    :param ForceFailover: If this parameter is true , the reboot is conducted through a Multi-AZ failover. (If the instance isn\'t configured for Multi-AZ, then you can\'t specify true .)

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationInstance': {
        'ReplicationInstanceIdentifier': 'string',
        'ReplicationInstanceClass': 'string',
        'ReplicationInstanceStatus': 'string',
        'AllocatedStorage': 123,
        'InstanceCreateTime': datetime(2015, 1, 1),
        'VpcSecurityGroups': [
            {
                'VpcSecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'AvailabilityZone': 'string',
        'ReplicationSubnetGroup': {
            'ReplicationSubnetGroupIdentifier': 'string',
            'ReplicationSubnetGroupDescription': 'string',
            'VpcId': 'string',
            'SubnetGroupStatus': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': {
                        'Name': 'string'
                    },
                    'SubnetStatus': 'string'
                },
            ]
        },
        'PreferredMaintenanceWindow': 'string',
        'PendingModifiedValues': {
            'ReplicationInstanceClass': 'string',
            'AllocatedStorage': 123,
            'MultiAZ': True|False,
            'EngineVersion': 'string'
        },
        'MultiAZ': True|False,
        'EngineVersion': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'KmsKeyId': 'string',
        'ReplicationInstanceArn': 'string',
        'ReplicationInstancePublicIpAddress': 'string',
        'ReplicationInstancePrivateIpAddress': 'string',
        'ReplicationInstancePublicIpAddresses': [
            'string',
        ],
        'ReplicationInstancePrivateIpAddresses': [
            'string',
        ],
        'PubliclyAccessible': True|False,
        'SecondaryAvailabilityZone': 'string',
        'FreeUntil': datetime(2015, 1, 1),
        'DnsNameServers': 'string'
    }
}


Response Structure

(dict) --

ReplicationInstance (dict) --
The replication instance that is being rebooted.

ReplicationInstanceIdentifier (string) --
The replication instance identifier. This parameter is stored as a lowercase string.
Constraints:

Must contain from 1 to 63 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.

Example: myrepinstance

ReplicationInstanceClass (string) --
The compute and memory capacity of the replication instance.
Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge

ReplicationInstanceStatus (string) --
The status of the replication instance.

AllocatedStorage (integer) --
The amount of storage (in gigabytes) that is allocated for the replication instance.

InstanceCreateTime (datetime) --
The time the replication instance was created.

VpcSecurityGroups (list) --
The VPC security group for the instance.

(dict) --
Describes status of a security group associated with the virtual private cloud hosting your replication and DB instances.

VpcSecurityGroupId (string) --
The VPC security group Id.

Status (string) --
The status of the VPC security group.





AvailabilityZone (string) --
The Availability Zone for the instance.

ReplicationSubnetGroup (dict) --
The subnet group for the replication instance.

ReplicationSubnetGroupIdentifier (string) --
The identifier of the replication instance subnet group.

ReplicationSubnetGroupDescription (string) --
A description for the replication subnet group.

VpcId (string) --
The ID of the VPC.

SubnetGroupStatus (string) --
The status of the subnet group.

Subnets (list) --
The subnets that are in the subnet group.

(dict) --
In response to a request by the DescribeReplicationSubnetGroup operation, this object identifies a subnet by its given Availability Zone, subnet identifier, and status.

SubnetIdentifier (string) --
The subnet identifier.

SubnetAvailabilityZone (dict) --
The Availability Zone of the subnet.

Name (string) --
The name of the Availability Zone.



SubnetStatus (string) --
The status of the subnet.







PreferredMaintenanceWindow (string) --
The maintenance window times for the replication instance.

PendingModifiedValues (dict) --
The pending modification values.

ReplicationInstanceClass (string) --
The compute and memory capacity of the replication instance.
Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge

AllocatedStorage (integer) --
The amount of storage (in gigabytes) that is allocated for the replication instance.

MultiAZ (boolean) --
Specifies whether the replication instance is a Multi-AZ deployment. You can\'t set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .

EngineVersion (string) --
The engine version number of the replication instance.



MultiAZ (boolean) --
Specifies whether the replication instance is a Multi-AZ deployment. You can\'t set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .

EngineVersion (string) --
The engine version number of the replication instance.

AutoMinorVersionUpgrade (boolean) --
Boolean value indicating if minor version upgrades will be automatically applied to the instance.

KmsKeyId (string) --
An AWS KMS key identifier that is used to encrypt the data on the replication instance.
If you don\'t specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key.
AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.

ReplicationInstanceArn (string) --
The Amazon Resource Name (ARN) of the replication instance.

ReplicationInstancePublicIpAddress (string) --
The public IP address of the replication instance.

ReplicationInstancePrivateIpAddress (string) --
The private IP address of the replication instance.

ReplicationInstancePublicIpAddresses (list) --
One or more public IP addresses for the replication instance.

(string) --


ReplicationInstancePrivateIpAddresses (list) --
One or more private IP addresses for the replication instance.

(string) --


PubliclyAccessible (boolean) --
Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address. The default value is true .

SecondaryAvailabilityZone (string) --
The Availability Zone of the standby replication instance in a Multi-AZ deployment.

FreeUntil (datetime) --
The expiration date of the free replication instance that is part of the Free DMS program.

DnsNameServers (string) --
The DNS name servers for the replication instance.









Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault


    :return: {
        'ReplicationInstance': {
            'ReplicationInstanceIdentifier': 'string',
            'ReplicationInstanceClass': 'string',
            'ReplicationInstanceStatus': 'string',
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'ReplicationSubnetGroup': {
                'ReplicationSubnetGroupIdentifier': 'string',
                'ReplicationSubnetGroupDescription': 'string',
                'VpcId': 'string',
                'SubnetGroupStatus': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        },
                        'SubnetStatus': 'string'
                    },
                ]
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'ReplicationInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string'
            },
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'KmsKeyId': 'string',
            'ReplicationInstanceArn': 'string',
            'ReplicationInstancePublicIpAddress': 'string',
            'ReplicationInstancePrivateIpAddress': 'string',
            'ReplicationInstancePublicIpAddresses': [
                'string',
            ],
            'ReplicationInstancePrivateIpAddresses': [
                'string',
            ],
            'PubliclyAccessible': True|False,
            'SecondaryAvailabilityZone': 'string',
            'FreeUntil': datetime(2015, 1, 1),
            'DnsNameServers': 'string'
        }
    }
    
    
    :returns: 
    Must contain from 1 to 63 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def refresh_schemas(EndpointArn=None, ReplicationInstanceArn=None):
    """
    Populates the schema for the specified endpoint. This is an asynchronous operation and can take several minutes. You can check the status of this operation by calling the DescribeRefreshSchemasStatus operation.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Populates the schema for the specified endpoint. This is an asynchronous operation and can take several minutes. You can check the status of this operation by calling the describe-refresh-schemas-status operation.
    Expected Output:
    
    :example: response = client.refresh_schemas(
        EndpointArn='string',
        ReplicationInstanceArn='string'
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]\nThe Amazon Resource Name (ARN) string that uniquely identifies the endpoint.\n

    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the replication instance.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RefreshSchemasStatus': {
        'EndpointArn': 'string',
        'ReplicationInstanceArn': 'string',
        'Status': 'successful'|'failed'|'refreshing',
        'LastRefreshDate': datetime(2015, 1, 1),
        'LastFailureMessage': 'string'
    }
}


Response Structure

(dict) --

RefreshSchemasStatus (dict) --
The status of the refreshed schema.

EndpointArn (string) --
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

ReplicationInstanceArn (string) --
The Amazon Resource Name (ARN) of the replication instance.

Status (string) --
The status of the schema.

LastRefreshDate (datetime) --
The date the schema was last refreshed.

LastFailureMessage (string) --
The last failure message for the schema.









Exceptions

DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.KMSKeyNotAccessibleFault
DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault

Examples
Populates the schema for the specified endpoint. This is an asynchronous operation and can take several minutes. You can check the status of this operation by calling the describe-refresh-schemas-status operation.
response = client.refresh_schemas(
    EndpointArn='',
    ReplicationInstanceArn='',
)

print(response)


Expected Output:
{
    'RefreshSchemasStatus': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'RefreshSchemasStatus': {
            'EndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'Status': 'successful'|'failed'|'refreshing',
            'LastRefreshDate': datetime(2015, 1, 1),
            'LastFailureMessage': 'string'
        }
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    DatabaseMigrationService.Client.exceptions.KMSKeyNotAccessibleFault
    DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault
    
    """
    pass

def reload_tables(ReplicationTaskArn=None, TablesToReload=None, ReloadOption=None):
    """
    Reloads the target database table with the source data.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reload_tables(
        ReplicationTaskArn='string',
        TablesToReload=[
            {
                'SchemaName': 'string',
                'TableName': 'string'
            },
        ],
        ReloadOption='data-reload'|'validate-only'
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the replication task.\n

    :type TablesToReload: list
    :param TablesToReload: [REQUIRED]\nThe name and schema of the table to be reloaded.\n\n(dict) --Provides the name of the schema and table to be reloaded.\n\nSchemaName (string) --The schema name of the table to be reloaded.\n\nTableName (string) --The table name of the table to be reloaded.\n\n\n\n\n

    :type ReloadOption: string
    :param ReloadOption: Options for reload. Specify data-reload to reload the data and re-validate it if validation is enabled. Specify validate-only to re-validate the table. This option applies only when validation is enabled for the task.\nValid values: data-reload, validate-only\nDefault value is data-reload.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationTaskArn': 'string'
}


Response Structure

(dict) --

ReplicationTaskArn (string) --
The Amazon Resource Name (ARN) of the replication task.







Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault


    :return: {
        'ReplicationTaskArn': 'string'
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
    
    """
    pass

def remove_tags_from_resource(ResourceArn=None, TagKeys=None):
    """
    Removes metadata tags from a DMS resource.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Removes metadata tags from an AWS DMS resource.
    Expected Output:
    
    :example: response = client.remove_tags_from_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nAn AWS DMS resource from which you want to remove tag(s). The value for this parameter is an Amazon Resource Name (ARN).\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag key (name) of the tag to be removed.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault

Examples
Removes metadata tags from an AWS DMS resource.
response = client.remove_tags_from_resource(
    ResourceArn='arn:aws:dms:us-east-1:123456789012:endpoint:ASXWXJZLNWNT5HTWCGV2BUJQ7E',
    TagKeys=[
    ],
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def start_replication_task(ReplicationTaskArn=None, StartReplicationTaskType=None, CdcStartTime=None, CdcStartPosition=None, CdcStopPosition=None):
    """
    Starts the replication task.
    For more information about AWS DMS tasks, see Working with Migration Tasks in the AWS Database Migration Service User Guide.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Starts the replication task.
    Expected Output:
    
    :example: response = client.start_replication_task(
        ReplicationTaskArn='string',
        StartReplicationTaskType='start-replication'|'resume-processing'|'reload-target',
        CdcStartTime=datetime(2015, 1, 1),
        CdcStartPosition='string',
        CdcStopPosition='string'
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the replication task to be started.\n

    :type StartReplicationTaskType: string
    :param StartReplicationTaskType: [REQUIRED]\nThe type of replication task.\n

    :type CdcStartTime: datetime
    :param CdcStartTime: Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.\nTimestamp Example: --cdc-start-time \xe2\x80\x9c2018-03-08T12:12:12\xe2\x80\x9d\n

    :type CdcStartPosition: string
    :param CdcStartPosition: Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.\nThe value can be in date, checkpoint, or LSN/SCN format.\nDate Example: --cdc-start-position \xe2\x80\x9c2018-03-08T12:12:12\xe2\x80\x9d\nCheckpoint Example: --cdc-start-position 'checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93'\nLSN Example: --cdc-start-position \xe2\x80\x9cmysql-bin-changelog.000024:373\xe2\x80\x9d\n\nNote\nWhen you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the slotName extra connection attribute to the name of this logical replication slot. For more information, see Extra Connection Attributes When Using PostgreSQL as a Source for AWS DMS .\n\n

    :type CdcStopPosition: string
    :param CdcStopPosition: Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.\nServer time example: --cdc-stop-position \xe2\x80\x9cserver_time:3018-02-09T12:12:12\xe2\x80\x9d\nCommit time example: --cdc-stop-position \xe2\x80\x9ccommit_time: 3018-02-09T12:12:12 \xe2\x80\x9c\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationTask': {
        'ReplicationTaskIdentifier': 'string',
        'SourceEndpointArn': 'string',
        'TargetEndpointArn': 'string',
        'ReplicationInstanceArn': 'string',
        'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
        'TableMappings': 'string',
        'ReplicationTaskSettings': 'string',
        'Status': 'string',
        'LastFailureMessage': 'string',
        'StopReason': 'string',
        'ReplicationTaskCreationDate': datetime(2015, 1, 1),
        'ReplicationTaskStartDate': datetime(2015, 1, 1),
        'CdcStartPosition': 'string',
        'CdcStopPosition': 'string',
        'RecoveryCheckpoint': 'string',
        'ReplicationTaskArn': 'string',
        'ReplicationTaskStats': {
            'FullLoadProgressPercent': 123,
            'ElapsedTimeMillis': 123,
            'TablesLoaded': 123,
            'TablesLoading': 123,
            'TablesQueued': 123,
            'TablesErrored': 123,
            'FreshStartDate': datetime(2015, 1, 1),
            'StartDate': datetime(2015, 1, 1),
            'StopDate': datetime(2015, 1, 1),
            'FullLoadStartDate': datetime(2015, 1, 1),
            'FullLoadFinishDate': datetime(2015, 1, 1)
        },
        'TaskData': 'string'
    }
}


Response Structure

(dict) --

ReplicationTask (dict) --
The replication task started.

ReplicationTaskIdentifier (string) --
The user-assigned replication task identifier or name.
Constraints:

Must contain from 1 to 255 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.


SourceEndpointArn (string) --
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

TargetEndpointArn (string) --
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

ReplicationInstanceArn (string) --
The Amazon Resource Name (ARN) of the replication instance.

MigrationType (string) --
The type of migration.

TableMappings (string) --
Table mappings specified in the task.

ReplicationTaskSettings (string) --
The settings for the replication task.

Status (string) --
The status of the replication task.

LastFailureMessage (string) --
The last error (failure) message generated for the replication instance.

StopReason (string) --
The reason the replication task was stopped.

ReplicationTaskCreationDate (datetime) --
The date the replication task was created.

ReplicationTaskStartDate (datetime) --
The date the replication task is scheduled to start.

CdcStartPosition (string) --
Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want the CDC operation to start. Specifying both values results in an error.
The value can be in date, checkpoint, or LSN/SCN format.
Date Example: --cdc-start-position \xe2\x80\x9c2018-03-08T12:12:12\xe2\x80\x9d
Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
LSN Example: --cdc-start-position \xe2\x80\x9cmysql-bin-changelog.000024:373\xe2\x80\x9d

CdcStopPosition (string) --
Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
Server time example: --cdc-stop-position \xe2\x80\x9cserver_time:3018-02-09T12:12:12\xe2\x80\x9d
Commit time example: --cdc-stop-position \xe2\x80\x9ccommit_time: 3018-02-09T12:12:12 \xe2\x80\x9c

RecoveryCheckpoint (string) --
Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the CdcStartPosition parameter to start a CDC operation that begins at that checkpoint.

ReplicationTaskArn (string) --
The Amazon Resource Name (ARN) of the replication task.

ReplicationTaskStats (dict) --
The statistics for the task, including elapsed time, tables loaded, and table errors.

FullLoadProgressPercent (integer) --
The percent complete for the full load migration task.

ElapsedTimeMillis (integer) --
The elapsed time of the task, in milliseconds.

TablesLoaded (integer) --
The number of tables loaded for this task.

TablesLoading (integer) --
The number of tables currently loading for this task.

TablesQueued (integer) --
The number of tables queued for this task.

TablesErrored (integer) --
The number of errors that have occurred during this task.

FreshStartDate (datetime) --
The date the replication task was started either with a fresh start or a target reload.

StartDate (datetime) --
The date the replication task was started either with a fresh start or a resume. For more information, see StartReplicationTaskType .

StopDate (datetime) --
The date the replication task was stopped.

FullLoadStartDate (datetime) --
The date the replication task full load was started.

FullLoadFinishDate (datetime) --
The date the replication task full load was completed.



TaskData (string) --
Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see Specifying Supplemental Data for Task Settings in the AWS Database Migration User Guide.









Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
DatabaseMigrationService.Client.exceptions.AccessDeniedFault

Examples
Starts the replication task.
response = client.start_replication_task(
    CdcStartTime=datetime(2016, 12, 14, 13, 33, 20, 2, 349, 0),
    ReplicationTaskArn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ',
    StartReplicationTaskType='start-replication',
)

print(response)


Expected Output:
{
    'ReplicationTask': {
        'MigrationType': 'full-load',
        'ReplicationInstanceArn': 'arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ',
        'ReplicationTaskArn': 'arn:aws:dms:us-east-1:123456789012:task:OEAMB3NXSTZ6LFYZFEPPBBXPYM',
        'ReplicationTaskCreationDate': datetime(2016, 12, 14, 18, 25, 43, 2, 349, 0),
        'ReplicationTaskIdentifier': 'task1',
        'ReplicationTaskSettings': '{"TargetMetadata":{"TargetSchema":"","SupportLobs":true,"FullLobMode":true,"LobChunkSize":64,"LimitedSizeLobMode":false,"LobMaxSize":0},"FullLoadSettings":{"FullLoadEnabled":true,"ApplyChangesEnabled":false,"TargetTablePrepMode":"DROP_AND_CREATE","CreatePkAfterFullLoad":false,"StopTaskCachedChangesApplied":false,"StopTaskCachedChangesNotApplied":false,"ResumeEnabled":false,"ResumeMinTableSize":100000,"ResumeOnlyClusteredPKTables":true,"MaxFullLoadSubTasks":8,"TransactionConsistencyTimeout":600,"CommitRate":10000},"Logging":{"EnableLogging":false}}',
        'SourceEndpointArn': 'arn:aws:dms:us-east-1:123456789012:endpoint:ZW5UAN6P4E77EC7YWHK4RZZ3BE',
        'Status': 'creating',
        'TableMappings': 'file://mappingfile.json',
        'TargetEndpointArn': 'arn:aws:dms:us-east-1:123456789012:endpoint:ASXWXJZLNWNT5HTWCGV2BUJQ7E',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReplicationTask': {
            'ReplicationTaskIdentifier': 'string',
            'SourceEndpointArn': 'string',
            'TargetEndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
            'TableMappings': 'string',
            'ReplicationTaskSettings': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'StopReason': 'string',
            'ReplicationTaskCreationDate': datetime(2015, 1, 1),
            'ReplicationTaskStartDate': datetime(2015, 1, 1),
            'CdcStartPosition': 'string',
            'CdcStopPosition': 'string',
            'RecoveryCheckpoint': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationTaskStats': {
                'FullLoadProgressPercent': 123,
                'ElapsedTimeMillis': 123,
                'TablesLoaded': 123,
                'TablesLoading': 123,
                'TablesQueued': 123,
                'TablesErrored': 123,
                'FreshStartDate': datetime(2015, 1, 1),
                'StartDate': datetime(2015, 1, 1),
                'StopDate': datetime(2015, 1, 1),
                'FullLoadStartDate': datetime(2015, 1, 1),
                'FullLoadFinishDate': datetime(2015, 1, 1)
            },
            'TaskData': 'string'
        }
    }
    
    
    :returns: 
    Must contain from 1 to 255 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def start_replication_task_assessment(ReplicationTaskArn=None):
    """
    Starts the replication task assessment for unsupported data types in the source database.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_replication_task_assessment(
        ReplicationTaskArn='string'
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the replication task.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ReplicationTask': {
        'ReplicationTaskIdentifier': 'string',
        'SourceEndpointArn': 'string',
        'TargetEndpointArn': 'string',
        'ReplicationInstanceArn': 'string',
        'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
        'TableMappings': 'string',
        'ReplicationTaskSettings': 'string',
        'Status': 'string',
        'LastFailureMessage': 'string',
        'StopReason': 'string',
        'ReplicationTaskCreationDate': datetime(2015, 1, 1),
        'ReplicationTaskStartDate': datetime(2015, 1, 1),
        'CdcStartPosition': 'string',
        'CdcStopPosition': 'string',
        'RecoveryCheckpoint': 'string',
        'ReplicationTaskArn': 'string',
        'ReplicationTaskStats': {
            'FullLoadProgressPercent': 123,
            'ElapsedTimeMillis': 123,
            'TablesLoaded': 123,
            'TablesLoading': 123,
            'TablesQueued': 123,
            'TablesErrored': 123,
            'FreshStartDate': datetime(2015, 1, 1),
            'StartDate': datetime(2015, 1, 1),
            'StopDate': datetime(2015, 1, 1),
            'FullLoadStartDate': datetime(2015, 1, 1),
            'FullLoadFinishDate': datetime(2015, 1, 1)
        },
        'TaskData': 'string'
    }
}


Response Structure

(dict) --
ReplicationTask (dict) --The assessed replication task.

ReplicationTaskIdentifier (string) --The user-assigned replication task identifier or name.
Constraints:

Must contain from 1 to 255 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.


SourceEndpointArn (string) --The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

TargetEndpointArn (string) --The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

ReplicationInstanceArn (string) --The Amazon Resource Name (ARN) of the replication instance.

MigrationType (string) --The type of migration.

TableMappings (string) --Table mappings specified in the task.

ReplicationTaskSettings (string) --The settings for the replication task.

Status (string) --The status of the replication task.

LastFailureMessage (string) --The last error (failure) message generated for the replication instance.

StopReason (string) --The reason the replication task was stopped.

ReplicationTaskCreationDate (datetime) --The date the replication task was created.

ReplicationTaskStartDate (datetime) --The date the replication task is scheduled to start.

CdcStartPosition (string) --Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want the CDC operation to start. Specifying both values results in an error.
The value can be in date, checkpoint, or LSN/SCN format.
Date Example: --cdc-start-position \xe2\x80\x9c2018-03-08T12:12:12\xe2\x80\x9d
Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
LSN Example: --cdc-start-position \xe2\x80\x9cmysql-bin-changelog.000024:373\xe2\x80\x9d

CdcStopPosition (string) --Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
Server time example: --cdc-stop-position \xe2\x80\x9cserver_time:3018-02-09T12:12:12\xe2\x80\x9d
Commit time example: --cdc-stop-position \xe2\x80\x9ccommit_time: 3018-02-09T12:12:12 \xe2\x80\x9c

RecoveryCheckpoint (string) --Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the CdcStartPosition parameter to start a CDC operation that begins at that checkpoint.

ReplicationTaskArn (string) --The Amazon Resource Name (ARN) of the replication task.

ReplicationTaskStats (dict) --The statistics for the task, including elapsed time, tables loaded, and table errors.

FullLoadProgressPercent (integer) --The percent complete for the full load migration task.

ElapsedTimeMillis (integer) --The elapsed time of the task, in milliseconds.

TablesLoaded (integer) --The number of tables loaded for this task.

TablesLoading (integer) --The number of tables currently loading for this task.

TablesQueued (integer) --The number of tables queued for this task.

TablesErrored (integer) --The number of errors that have occurred during this task.

FreshStartDate (datetime) --The date the replication task was started either with a fresh start or a target reload.

StartDate (datetime) --The date the replication task was started either with a fresh start or a resume. For more information, see StartReplicationTaskType .

StopDate (datetime) --The date the replication task was stopped.

FullLoadStartDate (datetime) --The date the replication task full load was started.

FullLoadFinishDate (datetime) --The date the replication task full load was completed.



TaskData (string) --Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see Specifying Supplemental Data for Task Settings in the AWS Database Migration User Guide.








Exceptions

DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault


    :return: {
        'ReplicationTask': {
            'ReplicationTaskIdentifier': 'string',
            'SourceEndpointArn': 'string',
            'TargetEndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
            'TableMappings': 'string',
            'ReplicationTaskSettings': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'StopReason': 'string',
            'ReplicationTaskCreationDate': datetime(2015, 1, 1),
            'ReplicationTaskStartDate': datetime(2015, 1, 1),
            'CdcStartPosition': 'string',
            'CdcStopPosition': 'string',
            'RecoveryCheckpoint': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationTaskStats': {
                'FullLoadProgressPercent': 123,
                'ElapsedTimeMillis': 123,
                'TablesLoaded': 123,
                'TablesLoading': 123,
                'TablesQueued': 123,
                'TablesErrored': 123,
                'FreshStartDate': datetime(2015, 1, 1),
                'StartDate': datetime(2015, 1, 1),
                'StopDate': datetime(2015, 1, 1),
                'FullLoadStartDate': datetime(2015, 1, 1),
                'FullLoadFinishDate': datetime(2015, 1, 1)
            },
            'TaskData': 'string'
        }
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    
    """
    pass

def stop_replication_task(ReplicationTaskArn=None):
    """
    Stops the replication task.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Stops the replication task.
    Expected Output:
    
    :example: response = client.stop_replication_task(
        ReplicationTaskArn='string'
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: [REQUIRED]\nThe Amazon Resource Name(ARN) of the replication task to be stopped.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ReplicationTask': {
        'ReplicationTaskIdentifier': 'string',
        'SourceEndpointArn': 'string',
        'TargetEndpointArn': 'string',
        'ReplicationInstanceArn': 'string',
        'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
        'TableMappings': 'string',
        'ReplicationTaskSettings': 'string',
        'Status': 'string',
        'LastFailureMessage': 'string',
        'StopReason': 'string',
        'ReplicationTaskCreationDate': datetime(2015, 1, 1),
        'ReplicationTaskStartDate': datetime(2015, 1, 1),
        'CdcStartPosition': 'string',
        'CdcStopPosition': 'string',
        'RecoveryCheckpoint': 'string',
        'ReplicationTaskArn': 'string',
        'ReplicationTaskStats': {
            'FullLoadProgressPercent': 123,
            'ElapsedTimeMillis': 123,
            'TablesLoaded': 123,
            'TablesLoading': 123,
            'TablesQueued': 123,
            'TablesErrored': 123,
            'FreshStartDate': datetime(2015, 1, 1),
            'StartDate': datetime(2015, 1, 1),
            'StopDate': datetime(2015, 1, 1),
            'FullLoadStartDate': datetime(2015, 1, 1),
            'FullLoadFinishDate': datetime(2015, 1, 1)
        },
        'TaskData': 'string'
    }
}


Response Structure

(dict) --
ReplicationTask (dict) --The replication task stopped.

ReplicationTaskIdentifier (string) --The user-assigned replication task identifier or name.
Constraints:

Must contain from 1 to 255 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.


SourceEndpointArn (string) --The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

TargetEndpointArn (string) --The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

ReplicationInstanceArn (string) --The Amazon Resource Name (ARN) of the replication instance.

MigrationType (string) --The type of migration.

TableMappings (string) --Table mappings specified in the task.

ReplicationTaskSettings (string) --The settings for the replication task.

Status (string) --The status of the replication task.

LastFailureMessage (string) --The last error (failure) message generated for the replication instance.

StopReason (string) --The reason the replication task was stopped.

ReplicationTaskCreationDate (datetime) --The date the replication task was created.

ReplicationTaskStartDate (datetime) --The date the replication task is scheduled to start.

CdcStartPosition (string) --Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want the CDC operation to start. Specifying both values results in an error.
The value can be in date, checkpoint, or LSN/SCN format.
Date Example: --cdc-start-position \xe2\x80\x9c2018-03-08T12:12:12\xe2\x80\x9d
Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
LSN Example: --cdc-start-position \xe2\x80\x9cmysql-bin-changelog.000024:373\xe2\x80\x9d

CdcStopPosition (string) --Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
Server time example: --cdc-stop-position \xe2\x80\x9cserver_time:3018-02-09T12:12:12\xe2\x80\x9d
Commit time example: --cdc-stop-position \xe2\x80\x9ccommit_time: 3018-02-09T12:12:12 \xe2\x80\x9c

RecoveryCheckpoint (string) --Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the CdcStartPosition parameter to start a CDC operation that begins at that checkpoint.

ReplicationTaskArn (string) --The Amazon Resource Name (ARN) of the replication task.

ReplicationTaskStats (dict) --The statistics for the task, including elapsed time, tables loaded, and table errors.

FullLoadProgressPercent (integer) --The percent complete for the full load migration task.

ElapsedTimeMillis (integer) --The elapsed time of the task, in milliseconds.

TablesLoaded (integer) --The number of tables loaded for this task.

TablesLoading (integer) --The number of tables currently loading for this task.

TablesQueued (integer) --The number of tables queued for this task.

TablesErrored (integer) --The number of errors that have occurred during this task.

FreshStartDate (datetime) --The date the replication task was started either with a fresh start or a target reload.

StartDate (datetime) --The date the replication task was started either with a fresh start or a resume. For more information, see StartReplicationTaskType .

StopDate (datetime) --The date the replication task was stopped.

FullLoadStartDate (datetime) --The date the replication task full load was started.

FullLoadFinishDate (datetime) --The date the replication task full load was completed.



TaskData (string) --Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see Specifying Supplemental Data for Task Settings in the AWS Database Migration User Guide.








Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault

Examples
Stops the replication task.
response = client.stop_replication_task(
    ReplicationTaskArn='arn:aws:dms:us-east-1:123456789012:endpoint:ASXWXJZLNWNT5HTWCGV2BUJQ7E',
)

print(response)


Expected Output:
{
    'ReplicationTask': {
        'MigrationType': 'full-load',
        'ReplicationInstanceArn': 'arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ',
        'ReplicationTaskArn': 'arn:aws:dms:us-east-1:123456789012:task:OEAMB3NXSTZ6LFYZFEPPBBXPYM',
        'ReplicationTaskCreationDate': datetime(2016, 12, 14, 18, 25, 43, 2, 349, 0),
        'ReplicationTaskIdentifier': 'task1',
        'ReplicationTaskSettings': '{"TargetMetadata":{"TargetSchema":"","SupportLobs":true,"FullLobMode":true,"LobChunkSize":64,"LimitedSizeLobMode":false,"LobMaxSize":0},"FullLoadSettings":{"FullLoadEnabled":true,"ApplyChangesEnabled":false,"TargetTablePrepMode":"DROP_AND_CREATE","CreatePkAfterFullLoad":false,"StopTaskCachedChangesApplied":false,"StopTaskCachedChangesNotApplied":false,"ResumeEnabled":false,"ResumeMinTableSize":100000,"ResumeOnlyClusteredPKTables":true,"MaxFullLoadSubTasks":8,"TransactionConsistencyTimeout":600,"CommitRate":10000},"Logging":{"EnableLogging":false}}',
        'SourceEndpointArn': 'arn:aws:dms:us-east-1:123456789012:endpoint:ZW5UAN6P4E77EC7YWHK4RZZ3BE',
        'Status': 'creating',
        'TableMappings': 'file://mappingfile.json',
        'TargetEndpointArn': 'arn:aws:dms:us-east-1:123456789012:endpoint:ASXWXJZLNWNT5HTWCGV2BUJQ7E',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReplicationTask': {
            'ReplicationTaskIdentifier': 'string',
            'SourceEndpointArn': 'string',
            'TargetEndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
            'TableMappings': 'string',
            'ReplicationTaskSettings': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'StopReason': 'string',
            'ReplicationTaskCreationDate': datetime(2015, 1, 1),
            'ReplicationTaskStartDate': datetime(2015, 1, 1),
            'CdcStartPosition': 'string',
            'CdcStopPosition': 'string',
            'RecoveryCheckpoint': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationTaskStats': {
                'FullLoadProgressPercent': 123,
                'ElapsedTimeMillis': 123,
                'TablesLoaded': 123,
                'TablesLoading': 123,
                'TablesQueued': 123,
                'TablesErrored': 123,
                'FreshStartDate': datetime(2015, 1, 1),
                'StartDate': datetime(2015, 1, 1),
                'StopDate': datetime(2015, 1, 1),
                'FullLoadStartDate': datetime(2015, 1, 1),
                'FullLoadFinishDate': datetime(2015, 1, 1)
            },
            'TaskData': 'string'
        }
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
    
    """
    pass

def test_connection(ReplicationInstanceArn=None, EndpointArn=None):
    """
    Tests the connection between the replication instance and the endpoint.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Tests the connection between the replication instance and the endpoint.
    Expected Output:
    
    :example: response = client.test_connection(
        ReplicationInstanceArn='string',
        EndpointArn='string'
    )
    
    
    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the replication instance.\n

    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]\nThe Amazon Resource Name (ARN) string that uniquely identifies the endpoint.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Connection': {
        'ReplicationInstanceArn': 'string',
        'EndpointArn': 'string',
        'Status': 'string',
        'LastFailureMessage': 'string',
        'EndpointIdentifier': 'string',
        'ReplicationInstanceIdentifier': 'string'
    }
}


Response Structure

(dict) --

Connection (dict) --
The connection tested.

ReplicationInstanceArn (string) --
The ARN of the replication instance.

EndpointArn (string) --
The ARN string that uniquely identifies the endpoint.

Status (string) --
The connection status.

LastFailureMessage (string) --
The error message when the connection last failed.

EndpointIdentifier (string) --
The identifier of the endpoint. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can\'t end with a hyphen or contain two consecutive hyphens.

ReplicationInstanceIdentifier (string) --
The replication instance identifier. This parameter is stored as a lowercase string.









Exceptions

DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
DatabaseMigrationService.Client.exceptions.KMSKeyNotAccessibleFault
DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault

Examples
Tests the connection between the replication instance and the endpoint.
response = client.test_connection(
    EndpointArn='arn:aws:dms:us-east-1:123456789012:endpoint:RAAR3R22XSH46S3PWLC3NJAWKM',
    ReplicationInstanceArn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ',
)

print(response)


Expected Output:
{
    'Connection': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Connection': {
            'ReplicationInstanceArn': 'string',
            'EndpointArn': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'EndpointIdentifier': 'string',
            'ReplicationInstanceIdentifier': 'string'
        }
    }
    
    
    :returns: 
    DatabaseMigrationService.Client.exceptions.ResourceNotFoundFault
    DatabaseMigrationService.Client.exceptions.InvalidResourceStateFault
    DatabaseMigrationService.Client.exceptions.KMSKeyNotAccessibleFault
    DatabaseMigrationService.Client.exceptions.ResourceQuotaExceededFault
    
    """
    pass

