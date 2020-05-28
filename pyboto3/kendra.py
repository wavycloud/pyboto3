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

def batch_delete_document(IndexId=None, DocumentIdList=None, DataSourceSyncJobMetricTarget=None):
    """
    Removes one or more documents from an index. The documents must have been added with the  BatchPutDocument operation.
    The documents are deleted asynchronously. You can see the progress of the deletion by using AWS CloudWatch. Any error messages releated to the processing of the batch are sent to you CloudWatch log.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_delete_document(
        IndexId='string',
        DocumentIdList=[
            'string',
        ],
        DataSourceSyncJobMetricTarget={
            'DataSourceId': 'string',
            'DataSourceSyncJobId': 'string'
        }
    )
    
    
    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe identifier of the index that contains the documents to delete.\n

    :type DocumentIdList: list
    :param DocumentIdList: [REQUIRED]\nOne or more identifiers for documents to delete from the index.\n\n(string) --\n\n

    :type DataSourceSyncJobMetricTarget: dict
    :param DataSourceSyncJobMetricTarget: Maps a particular data source sync job to a particular data source.\n\nDataSourceId (string) -- [REQUIRED]The ID of the data source that is running the sync job.\n\nDataSourceSyncJobId (string) -- [REQUIRED]The ID of the sync job that is running on the data source.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FailedDocuments': [
        {
            'Id': 'string',
            'ErrorCode': 'InternalError'|'InvalidRequest',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

FailedDocuments (list) --
A list of documents that could not be removed from the index. Each entry contains an error message that indicates why the document couldn\'t be removed from the index.

(dict) --
Provides information about documents that could not be removed from an index by the  BatchDeleteDocument operation.

Id (string) --
The identifier of the document that couldn\'t be removed from the index.

ErrorCode (string) --
The error code for why the document couldn\'t be removed from the index.

ErrorMessage (string) --
An explanation for why the document couldn\'t be removed from the index.











Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ConflictException
kendra.Client.exceptions.ResourceNotFoundException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.InternalServerException


    :return: {
        'FailedDocuments': [
            {
                'Id': 'string',
                'ErrorCode': 'InternalError'|'InvalidRequest',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ConflictException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def batch_put_document(IndexId=None, RoleArn=None, Documents=None):
    """
    Adds one or more documents to an index.
    The BatchPutDocument operation enables you to ingest inline documents or a set of documents stored in an Amazon S3 bucket. Use this operation to ingest your text and unstructured text into an index, add custom attributes to the documents, and to attach an access control list to the documents added to the index.
    The documents are indexed asynchronously. You can see the progress of the batch using AWS CloudWatch. Any error messages related to processing the batch are sent to your AWS CloudWatch log.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_put_document(
        IndexId='string',
        RoleArn='string',
        Documents=[
            {
                'Id': 'string',
                'Title': 'string',
                'Blob': b'bytes',
                'S3Path': {
                    'Bucket': 'string',
                    'Key': 'string'
                },
                'Attributes': [
                    {
                        'Key': 'string',
                        'Value': {
                            'StringValue': 'string',
                            'StringListValue': [
                                'string',
                            ],
                            'LongValue': 123,
                            'DateValue': datetime(2015, 1, 1)
                        }
                    },
                ],
                'AccessControlList': [
                    {
                        'Name': 'string',
                        'Type': 'USER'|'GROUP',
                        'Access': 'ALLOW'|'DENY'
                    },
                ],
                'ContentType': 'PDF'|'HTML'|'MS_WORD'|'PLAIN_TEXT'|'PPT'
            },
        ]
    )
    
    
    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe identifier of the index to add the documents to. You need to create the index first using the CreateIndex operation.\n

    :type RoleArn: string
    :param RoleArn: The Amazon Resource Name (ARN) of a role that is allowed to run the BatchPutDocument operation. For more information, see IAM Roles for Amazon Kendra .

    :type Documents: list
    :param Documents: [REQUIRED]\nOne or more documents to add to the index.\nDocuments have the following file size limits.\n\n5 MB total size for inline documents\n50 MB total size for files from an S3 bucket\n5 MB extracted text for any file\n\nFor more information about file size and transaction per second quotas, see Quotas .\n\n(dict) --A document in an index.\n\nId (string) -- [REQUIRED]A unique identifier of the document in the index.\n\nTitle (string) --The title of the document.\n\nBlob (bytes) --The contents of the document.\nDocuments passed to the Blob parameter must be base64 encoded. Your code might not need to encode the document file bytes if you\'re using an AWS SDK to call Amazon Kendra operations. If you are calling the Amazon Kendra endpoint directly using REST, you must base64 encode the contents before sending.\n\nS3Path (dict) --Information required to find a specific file in an Amazon S3 bucket.\n\nBucket (string) -- [REQUIRED]The name of the S3 bucket that contains the file.\n\nKey (string) -- [REQUIRED]The name of the file.\n\n\n\nAttributes (list) --Custom attributes to apply to the document. Use the custom attributes to provide additional information for searching, to provide facets for refining searches, and to provide additional information in the query response.\n\n(dict) --A custom attribute value assigned to a document.\n\nKey (string) -- [REQUIRED]The identifier for the attribute.\n\nValue (dict) -- [REQUIRED]The value of the attribute.\n\nStringValue (string) --A string, such as 'department'.\n\nStringListValue (list) --A list of strings.\n\n(string) --\n\n\nLongValue (integer) --A long integer value.\n\nDateValue (datetime) --A date value expressed as seconds from the Unix epoch.\n\n\n\n\n\n\n\nAccessControlList (list) --Information to use for user context filtering.\n\n(dict) --Provides user and group information for document access filtering.\n\nName (string) -- [REQUIRED]The name of the user or group.\n\nType (string) -- [REQUIRED]The type of principal.\n\nAccess (string) -- [REQUIRED]Whether to allow or deny access to the principal.\n\n\n\n\n\nContentType (string) --The file type of the document in the Blob field.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FailedDocuments': [
        {
            'Id': 'string',
            'ErrorCode': 'InternalError'|'InvalidRequest',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

FailedDocuments (list) --
A list of documents that were not added to the index because the document failed a validation check. Each document contains an error message that indicates why the document couldn\'t be added to the index.
If there was an error adding a document to an index the error is reported in your AWS CloudWatch log. For more information, see Monitoring Amazon Kendra with Amazon CloudWatch Logs

(dict) --
Provides information about a document that could not be indexed.

Id (string) --
The unique identifier of the document.

ErrorCode (string) --
The type of error that caused the document to fail to be indexed.

ErrorMessage (string) --
A description of the reason why the document could not be indexed.











Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ConflictException
kendra.Client.exceptions.ResourceNotFoundException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.ServiceQuotaExceededException
kendra.Client.exceptions.InternalServerException


    :return: {
        'FailedDocuments': [
            {
                'Id': 'string',
                'ErrorCode': 'InternalError'|'InvalidRequest',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ConflictException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.ServiceQuotaExceededException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_data_source(Name=None, IndexId=None, Type=None, Configuration=None, Description=None, Schedule=None, RoleArn=None, Tags=None):
    """
    Creates a data source that you use to with an Amazon Kendra index.
    You specify a name, connector type and description for your data source. You can choose between an S3 connector, a SharePoint Online connector, and a database connector.
    You also specify configuration information such as document metadata (author, source URI, and so on) and user context information.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_data_source(
        Name='string',
        IndexId='string',
        Type='S3'|'SHAREPOINT'|'DATABASE'|'SALESFORCE'|'ONEDRIVE'|'SERVICENOW',
        Configuration={
            'S3Configuration': {
                'BucketName': 'string',
                'InclusionPrefixes': [
                    'string',
                ],
                'ExclusionPatterns': [
                    'string',
                ],
                'DocumentsMetadataConfiguration': {
                    'S3Prefix': 'string'
                },
                'AccessControlListConfiguration': {
                    'KeyPath': 'string'
                }
            },
            'SharePointConfiguration': {
                'SharePointVersion': 'SHAREPOINT_ONLINE',
                'Urls': [
                    'string',
                ],
                'SecretArn': 'string',
                'CrawlAttachments': True|False,
                'UseChangeLog': True|False,
                'InclusionPatterns': [
                    'string',
                ],
                'ExclusionPatterns': [
                    'string',
                ],
                'VpcConfiguration': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'FieldMappings': [
                    {
                        'DataSourceFieldName': 'string',
                        'DateFieldFormat': 'string',
                        'IndexFieldName': 'string'
                    },
                ],
                'DocumentTitleFieldName': 'string'
            },
            'DatabaseConfiguration': {
                'DatabaseEngineType': 'RDS_AURORA_MYSQL'|'RDS_AURORA_POSTGRESQL'|'RDS_MYSQL'|'RDS_POSTGRESQL',
                'ConnectionConfiguration': {
                    'DatabaseHost': 'string',
                    'DatabasePort': 123,
                    'DatabaseName': 'string',
                    'TableName': 'string',
                    'SecretArn': 'string'
                },
                'VpcConfiguration': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'ColumnConfiguration': {
                    'DocumentIdColumnName': 'string',
                    'DocumentDataColumnName': 'string',
                    'DocumentTitleColumnName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ],
                    'ChangeDetectingColumns': [
                        'string',
                    ]
                },
                'AclConfiguration': {
                    'AllowedGroupsColumnName': 'string'
                }
            },
            'SalesforceConfiguration': {
                'ServerUrl': 'string',
                'SecretArn': 'string',
                'StandardObjectConfigurations': [
                    {
                        'Name': 'ACCOUNT'|'CAMPAIGN'|'CASE'|'CONTACT'|'CONTRACT'|'DOCUMENT'|'GROUP'|'IDEA'|'LEAD'|'OPPORTUNITY'|'PARTNER'|'PRICEBOOK'|'PRODUCT'|'PROFILE'|'SOLUTION'|'TASK'|'USER',
                        'DocumentDataFieldName': 'string',
                        'DocumentTitleFieldName': 'string',
                        'FieldMappings': [
                            {
                                'DataSourceFieldName': 'string',
                                'DateFieldFormat': 'string',
                                'IndexFieldName': 'string'
                            },
                        ]
                    },
                ],
                'KnowledgeArticleConfiguration': {
                    'IncludedStates': [
                        'DRAFT'|'PUBLISHED'|'ARCHIVED',
                    ],
                    'StandardKnowledgeArticleTypeConfiguration': {
                        'DocumentDataFieldName': 'string',
                        'DocumentTitleFieldName': 'string',
                        'FieldMappings': [
                            {
                                'DataSourceFieldName': 'string',
                                'DateFieldFormat': 'string',
                                'IndexFieldName': 'string'
                            },
                        ]
                    },
                    'CustomKnowledgeArticleTypeConfigurations': [
                        {
                            'Name': 'string',
                            'DocumentDataFieldName': 'string',
                            'DocumentTitleFieldName': 'string',
                            'FieldMappings': [
                                {
                                    'DataSourceFieldName': 'string',
                                    'DateFieldFormat': 'string',
                                    'IndexFieldName': 'string'
                                },
                            ]
                        },
                    ]
                },
                'ChatterFeedConfiguration': {
                    'DocumentDataFieldName': 'string',
                    'DocumentTitleFieldName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ],
                    'IncludeFilterTypes': [
                        'ACTIVE_USER'|'STANDARD_USER',
                    ]
                },
                'CrawlAttachments': True|False,
                'StandardObjectAttachmentConfiguration': {
                    'DocumentTitleFieldName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ]
                },
                'IncludeAttachmentFilePatterns': [
                    'string',
                ],
                'ExcludeAttachmentFilePatterns': [
                    'string',
                ]
            },
            'OneDriveConfiguration': {
                'TenantDomain': 'string',
                'SecretArn': 'string',
                'OneDriveUsers': {
                    'OneDriveUserList': [
                        'string',
                    ],
                    'OneDriveUserS3Path': {
                        'Bucket': 'string',
                        'Key': 'string'
                    }
                },
                'InclusionPatterns': [
                    'string',
                ],
                'ExclusionPatterns': [
                    'string',
                ],
                'FieldMappings': [
                    {
                        'DataSourceFieldName': 'string',
                        'DateFieldFormat': 'string',
                        'IndexFieldName': 'string'
                    },
                ]
            },
            'ServiceNowConfiguration': {
                'HostUrl': 'string',
                'SecretArn': 'string',
                'ServiceNowBuildVersion': 'LONDON'|'OTHERS',
                'KnowledgeArticleConfiguration': {
                    'CrawlAttachments': True|False,
                    'IncludeAttachmentFilePatterns': [
                        'string',
                    ],
                    'ExcludeAttachmentFilePatterns': [
                        'string',
                    ],
                    'DocumentDataFieldName': 'string',
                    'DocumentTitleFieldName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ]
                },
                'ServiceCatalogConfiguration': {
                    'CrawlAttachments': True|False,
                    'IncludeAttachmentFilePatterns': [
                        'string',
                    ],
                    'ExcludeAttachmentFilePatterns': [
                        'string',
                    ],
                    'DocumentDataFieldName': 'string',
                    'DocumentTitleFieldName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ]
                }
            }
        },
        Description='string',
        Schedule='string',
        RoleArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA unique name for the data source. A data source name can\'t be changed without deleting and recreating the data source.\n

    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe identifier of the index that should be associated with this data source.\n

    :type Type: string
    :param Type: [REQUIRED]\nThe type of repository that contains the data source.\n

    :type Configuration: dict
    :param Configuration: [REQUIRED]\nThe connector configuration information that is required to access the repository.\n\nS3Configuration (dict) --Provides information to create a connector for a document repository in an Amazon S3 bucket.\n\nBucketName (string) -- [REQUIRED]The name of the bucket that contains the documents.\n\nInclusionPrefixes (list) --A list of S3 prefixes for the documents that should be included in the index.\n\n(string) --\n\n\nExclusionPatterns (list) --A list of glob patterns for documents that should not be indexed. If a document that matches an inclusion prefix also matches an exclusion pattern, the document is not indexed.\nFor more information about glob patterns, see glob (programming) in Wikipedia .\n\n(string) --\n\n\nDocumentsMetadataConfiguration (dict) --Document metadata files that contain information such as the document access control information, source URI, document author, and custom attributes. Each metadata file contains metadata about a single document.\n\nS3Prefix (string) --A prefix used to filter metadata configuration files in the AWS S3 bucket. The S3 bucket might contain multiple metadata files. Use S3Prefix to include only the desired metadata files.\n\n\n\nAccessControlListConfiguration (dict) --Provides the path to the S3 bucket that contains the user context filtering files for the data source.\n\nKeyPath (string) --Path to the AWS S3 bucket that contains the ACL files.\n\n\n\n\n\nSharePointConfiguration (dict) --Provides information necessary to create a connector for a Microsoft SharePoint site.\n\nSharePointVersion (string) -- [REQUIRED]The version of Microsoft SharePoint that you are using as a data source.\n\nUrls (list) -- [REQUIRED]The URLs of the Microsoft SharePoint site that contains the documents that should be indexed.\n\n(string) --\n\n\nSecretArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of credentials stored in AWS Secrets Manager. The credentials should be a user/password pair. For more information, see Using a Microsoft SharePoint Data Source . For more information about AWS Secrets Manager, see What Is AWS Secrets Manager in the AWS Secrets Manager user guide.\n\nCrawlAttachments (boolean) --\nTRUE to include attachments to documents stored in your Microsoft SharePoint site in the index; otherwise, FALSE .\n\nUseChangeLog (boolean) --Set to TRUE to use the Microsoft SharePoint change log to determine the documents that need to be updated in the index. Depending on the size of the SharePoint change log, it may take longer for Amazon Kendra to use the change log than it takes it to determine the changed documents using the Amazon Kendra document crawler.\n\nInclusionPatterns (list) --A list of regular expression patterns. Documents that match the patterns are included in the index. Documents that don\'t match the patterns are excluded from the index. If a document matches both an inclusion pattern and an exclusion pattern, the document is not included in the index.\nThe regex is applied to the display URL of the SharePoint document.\n\n(string) --\n\n\nExclusionPatterns (list) --A list of regulary expression patterns. Documents that match the patterns are excluded from the index. Documents that don\'t match the patterns are included in the index. If a document matches both an exclusion pattern and an inclusion pattern, the document is not included in the index.\nThe regex is applied to the display URL of the SharePoint document.\n\n(string) --\n\n\nVpcConfiguration (dict) --Provides information for connecting to an Amazon VPC.\n\nSubnetIds (list) -- [REQUIRED]A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.\n\n(string) --\n\n\nSecurityGroupIds (list) -- [REQUIRED]A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.\n\n(string) --\n\n\n\n\nFieldMappings (list) --A list of DataSourceToIndexFieldMapping objects that map Microsoft SharePoint attributes to custom fields in the Amazon Kendra index. You must first create the index fields using the operation before you map SharePoint attributes. For more information, see Mapping Data Source Fields .\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\nDocumentTitleFieldName (string) --The Microsoft SharePoint attribute field that contains the title of the document.\n\n\n\nDatabaseConfiguration (dict) --Provides information necessary to create a connector for a database.\n\nDatabaseEngineType (string) -- [REQUIRED]The type of database engine that runs the database.\n\nConnectionConfiguration (dict) -- [REQUIRED]The information necessary to connect to a database.\n\nDatabaseHost (string) -- [REQUIRED]The name of the host for the database. Can be either a string (host.subdomain.domain.tld) or an IPv4 or IPv6 address.\n\nDatabasePort (integer) -- [REQUIRED]The port that the database uses for connections.\n\nDatabaseName (string) -- [REQUIRED]The name of the database containing the document data.\n\nTableName (string) -- [REQUIRED]The name of the table that contains the document data.\n\nSecretArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of credentials stored in AWS Secrets Manager. The credentials should be a user/password pair. For more information, see Using a Database Data Source . For more information about AWS Secrets Manager, see What Is AWS Secrets Manager in the AWS Secrets Manager user guide.\n\n\n\nVpcConfiguration (dict) --Provides information for connecting to an Amazon VPC.\n\nSubnetIds (list) -- [REQUIRED]A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.\n\n(string) --\n\n\nSecurityGroupIds (list) -- [REQUIRED]A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.\n\n(string) --\n\n\n\n\nColumnConfiguration (dict) -- [REQUIRED]Information about where the index should get the document information from the database.\n\nDocumentIdColumnName (string) -- [REQUIRED]The column that provides the document\'s unique identifier.\n\nDocumentDataColumnName (string) -- [REQUIRED]The column that contains the contents of the document.\n\nDocumentTitleColumnName (string) --The column that contains the title of the document.\n\nFieldMappings (list) --An array of objects that map database column names to the corresponding fields in an index. You must first create the fields in the index using the UpdateIndex operation.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\nChangeDetectingColumns (list) -- [REQUIRED]One to five columns that indicate when a document in the database has changed.\n\n(string) --\n\n\n\n\nAclConfiguration (dict) --Information about the database column that provides information for user context filtering.\n\nAllowedGroupsColumnName (string) -- [REQUIRED]A list of groups, separated by semi-colons, that filters a query response based on user context. The document is only returned to users that are in one of the groups specified in the UserContext field of the Query operation.\n\n\n\n\n\nSalesforceConfiguration (dict) --Provides configuration information for data sources that connect to a Salesforce site.\n\nServerUrl (string) -- [REQUIRED]The instance URL for the Salesforce site that you want to index.\n\nSecretArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the key/value pairs required to connect to your Salesforce instance. The secret must contain a JSON structure with the following keys:\n\nauthenticationUrl - The OAUTH endpoint that Amazon Kendra connects to get an OAUTH token.\nconsumerKey - The application public key generated when you created your Salesforce application.\nconsumerSecret - The application private key generated when you created your Salesforce application.\npassword - The password associated with the user logging in to the Salesforce instance.\nsecurityToken - The token associated with the user account logging in to the Salesforce instance.\nusername - The user name of the user logging in to the Salesforce instance.\n\n\nStandardObjectConfigurations (list) --Specifies the Salesforce standard objects that Amazon Kendra indexes.\n\n(dict) --Specifies confguration information for indexing a single standard object.\n\nName (string) -- [REQUIRED]The name of the standard object.\n\nDocumentDataFieldName (string) -- [REQUIRED]The name of the field in the standard object table that contains the document contents.\n\nDocumentTitleFieldName (string) --The name of the field in the standard object table that contains the document titleB.\n\nFieldMappings (list) --One or more objects that map fields in the standard object to Amazon Kendra index fields. The index field must exist before you can map a Salesforce field to it.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\n\n\n\n\nKnowledgeArticleConfiguration (dict) --Specifies configuration information for the knowlege article types that Amazon Kendra indexes. Amazon Kendra indexes standard knowledge articles and the standard fields of knowledge articles, or the custom fields of custom knowledge articles, but not both.\n\nIncludedStates (list) -- [REQUIRED]Specifies the document states that should be included when Amazon Kendra indexes knowledge articles. You must specify at least one state.\n\n(string) --\n\n\nStandardKnowledgeArticleTypeConfiguration (dict) --Provides configuration information for standard Salesforce knowledge articles.\n\nDocumentDataFieldName (string) -- [REQUIRED]The name of the field that contains the document data to index.\n\nDocumentTitleFieldName (string) --The name of the field that contains the document title.\n\nFieldMappings (list) --One or more objects that map fields in the knowledge article to Amazon Kendra index fields. The index field must exist before you can map a Salesforce field to it.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\n\n\nCustomKnowledgeArticleTypeConfigurations (list) --Provides configuration information for custom Salesforce knowledge articles.\n\n(dict) --Provides configuration information for indexing Salesforce custom articles.\n\nName (string) -- [REQUIRED]The name of the configuration.\n\nDocumentDataFieldName (string) -- [REQUIRED]The name of the field in the custom knowledge article that contains the document data to index.\n\nDocumentTitleFieldName (string) --The name of the field in the custom knowledge article that contains the document title.\n\nFieldMappings (list) --One or more objects that map fields in the custom knowledge article to fields in the Amazon Kendra index.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\n\n\n\n\n\n\nChatterFeedConfiguration (dict) --Specifies configuration information for Salesforce chatter feeds.\n\nDocumentDataFieldName (string) -- [REQUIRED]The name of the column in the Salesforce FeedItem table that contains the content to index. Typically this is the Body column.\n\nDocumentTitleFieldName (string) --The name of the column in the Salesforce FeedItem table that contains the title of the document. This is typically the Title collumn.\n\nFieldMappings (list) --Maps fields from a Salesforce chatter feed into Amazon Kendra index fields.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\nIncludeFilterTypes (list) --Filters the documents in the feed based on status of the user. When you specify ACTIVE_USERS only documents from users who have an active account are indexed. When you specify STANDARD_USER only documents for Salesforce standard users are documented. You can specify both.\n\n(string) --\n\n\n\n\nCrawlAttachments (boolean) --Indicates whether Amazon Kendra should index attachments to Salesforce objects.\n\nStandardObjectAttachmentConfiguration (dict) --Provides configuration information for processing attachments to Salesforce standard objects.\n\nDocumentTitleFieldName (string) --The name of the field used for the document title.\n\nFieldMappings (list) --One or more objects that map fields in attachments to Amazon Kendra index fields.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\n\n\nIncludeAttachmentFilePatterns (list) --A list of regular expression patterns. Documents that match the patterns are included in the index. Documents that don\'t match the patterns are excluded from the index. If a document matches both an inclusion pattern and an exclusion pattern, the document is not included in the index.\nThe regex is applied to the name of the attached file.\n\n(string) --\n\n\nExcludeAttachmentFilePatterns (list) --A list of regular expression patterns. Documents that match the patterns are excluded from the index. Documents that don\'t match the patterns are included in the index. If a document matches both an exclusion pattern and an inclusion pattern, the document is not included in the index.\nThe regex is applied to the name of the attached file.\n\n(string) --\n\n\n\n\nOneDriveConfiguration (dict) --Provided configuration for data sources that connect to Microsoft OneDrive.\n\nTenantDomain (string) -- [REQUIRED]Tha Azure Active Directory domain of the organization.\n\nSecretArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the user name and password to connect to OneDrive. The user namd should be the application ID for the OneDrive application, and the password is the application key for the OneDrive application.\n\nOneDriveUsers (dict) -- [REQUIRED]A list of user accounts whose documents should be indexed.\n\nOneDriveUserList (list) --A list of users whose documents should be indexed. Specify the user names in email format, for example, username@tenantdomain . If you need to index the documents of more than 100 users, use the OneDriveUserS3Path field to specify the location of a file containing a list of users.\n\n(string) --\n\n\nOneDriveUserS3Path (dict) --The S3 bucket location of a file containing a list of users whose documents should be indexed.\n\nBucket (string) -- [REQUIRED]The name of the S3 bucket that contains the file.\n\nKey (string) -- [REQUIRED]The name of the file.\n\n\n\n\n\nInclusionPatterns (list) --A list of regular expression patterns. Documents that match the pattern are included in the index. Documents that don\'t match the pattern are excluded from the index. If a document matches both an inclusion pattern and an exclusion pattern, the document is not included in the index.\nThe exclusion pattern is applied to the file name.\n\n(string) --\n\n\nExclusionPatterns (list) --List of regular expressions applied to documents. Items that match the exclusion pattern are not indexed. If you provide both an inclusion pattern and an exclusion pattern, any item that matches the exclusion pattern isn\'t indexed.\nThe exclusion pattern is applied to the file name.\n\n(string) --\n\n\nFieldMappings (list) --A list of DataSourceToIndexFieldMapping objects that map Microsoft OneDrive fields to custom fields in the Amazon Kendra index. You must first create the index fields before you map OneDrive fields.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\n\n\nServiceNowConfiguration (dict) --Provides configuration for data sources that connect to ServiceNow instances.\n\nHostUrl (string) -- [REQUIRED]The ServiceNow instance that the data source connects to. The host endpoint should look like the following: {instance}.service-now.com.\n\nSecretArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS Secret Manager secret that contains the user name and password required to connect to the ServiceNow instance.\n\nServiceNowBuildVersion (string) -- [REQUIRED]The identifier of the release that the ServiceNow host is running. If the host is not running the LONDON release, use OTHERS .\n\nKnowledgeArticleConfiguration (dict) --Provides configuration information for crawling knowledge articles in the ServiceNow site.\n\nCrawlAttachments (boolean) --Indicates whether Amazon Kendra should index attachments to knowledge articles.\n\nIncludeAttachmentFilePatterns (list) --List of regular expressions applied to knowledge articles. Items that don\'t match the inclusion pattern are not indexed. The regex is applied to the field specified in the PatternTargetField .\n\n(string) --\n\n\nExcludeAttachmentFilePatterns (list) --List of regular expressions applied to knowledge articles. Items that don\'t match the inclusion pattern are not indexed. The regex is applied to the field specified in the PatternTargetField\n\n(string) --\n\n\nDocumentDataFieldName (string) -- [REQUIRED]The name of the ServiceNow field that is mapped to the index document contents field in the Amazon Kendra index.\n\nDocumentTitleFieldName (string) --The name of the ServiceNow field that is mapped to the index document title field.\n\nFieldMappings (list) --Mapping between ServiceNow fields and Amazon Kendra index fields. You must create the index field before you map the field.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\n\n\nServiceCatalogConfiguration (dict) --Provides configuration information for crawling service catalogs in the ServiceNow site.\n\nCrawlAttachments (boolean) --Indicates whether Amazon Kendra should crawl attachments to the service catalog items.\n\nIncludeAttachmentFilePatterns (list) --Determines the types of file attachments that are included in the index.\n\n(string) --\n\n\nExcludeAttachmentFilePatterns (list) --Determines the types of file attachments that are excluded from the index.\n\n(string) --\n\n\nDocumentDataFieldName (string) -- [REQUIRED]The name of the ServiceNow field that is mapped to the index document contents field in the Amazon Kendra index.\n\nDocumentTitleFieldName (string) --The name of the ServiceNow field that is mapped to the index document title field.\n\nFieldMappings (list) --Mapping between ServiceNow fields and Amazon Kendra index fields. You must create the index field before you map the field.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\n\n\n\n\n\n

    :type Description: string
    :param Description: A description for the data source.

    :type Schedule: string
    :param Schedule: Sets the frequency that Amazon Kendra will check the documents in your repository and update the index. If you don\'t set a schedule Amazon Kendra will not periodically update the index. You can call the StartDataSourceSyncJob operation to update the index.

    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of a role with permission to access the data source. For more information, see IAM Roles for Amazon Kendra .\n

    :type Tags: list
    :param Tags: A list of key-value pairs that identify the data source. You can use the tags to identify and organize your resources and to control access to resources.\n\n(dict) --A list of key/value pairs that identify an index, FAQ, or data source. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.\n\nKey (string) -- [REQUIRED]The key for the tag. Keys are not case sensitive and must be unique for the index, FAQ, or data source.\n\nValue (string) -- [REQUIRED]The value associated with the tag. The value may be an empty string but it can\'t be null.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Id': 'string'
}


Response Structure

(dict) --

Id (string) --
A unique identifier for the data source.







Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ConflictException
kendra.Client.exceptions.ResourceNotFoundException
kendra.Client.exceptions.ResourceAlreadyExistException
kendra.Client.exceptions.ServiceQuotaExceededException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.InternalServerException


    :return: {
        'Id': 'string'
    }
    
    
    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ConflictException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ResourceAlreadyExistException
    kendra.Client.exceptions.ServiceQuotaExceededException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def create_faq(IndexId=None, Name=None, Description=None, S3Path=None, RoleArn=None, Tags=None):
    """
    Creates an new set of frequently asked question (FAQ) questions and answers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_faq(
        IndexId='string',
        Name='string',
        Description='string',
        S3Path={
            'Bucket': 'string',
            'Key': 'string'
        },
        RoleArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe identifier of the index that contains the FAQ.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name that should be associated with the FAQ.\n

    :type Description: string
    :param Description: A description of the FAQ.

    :type S3Path: dict
    :param S3Path: [REQUIRED]\nThe S3 location of the FAQ input data.\n\nBucket (string) -- [REQUIRED]The name of the S3 bucket that contains the file.\n\nKey (string) -- [REQUIRED]The name of the file.\n\n\n

    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of a role with permission to access the S3 bucket that contains the FAQs. For more information, see IAM Roles for Amazon Kendra .\n

    :type Tags: list
    :param Tags: A list of key-value pairs that identify the FAQ. You can use the tags to identify and organize your resources and to control access to resources.\n\n(dict) --A list of key/value pairs that identify an index, FAQ, or data source. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.\n\nKey (string) -- [REQUIRED]The key for the tag. Keys are not case sensitive and must be unique for the index, FAQ, or data source.\n\nValue (string) -- [REQUIRED]The value associated with the tag. The value may be an empty string but it can\'t be null.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Id': 'string'
}


Response Structure

(dict) --

Id (string) --
The unique identifier of the FAQ.







Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ConflictException
kendra.Client.exceptions.ResourceNotFoundException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.ServiceQuotaExceededException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.InternalServerException


    :return: {
        'Id': 'string'
    }
    
    
    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ConflictException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.ServiceQuotaExceededException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def create_index(Name=None, Edition=None, RoleArn=None, ServerSideEncryptionConfiguration=None, Description=None, ClientToken=None, Tags=None):
    """
    Creates a new Amazon Kendra index. Index creation is an asynchronous operation. To determine if index creation has completed, check the Status field returned from a call to . The Status field is set to ACTIVE when the index is ready to use.
    Once the index is active you can index your documents using the operation or using one of the supported data sources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_index(
        Name='string',
        Edition='DEVELOPER_EDITION'|'ENTERPRISE_EDITION',
        RoleArn='string',
        ServerSideEncryptionConfiguration={
            'KmsKeyId': 'string'
        },
        Description='string',
        ClientToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name for the new index.\n

    :type Edition: string
    :param Edition: The Amazon Kendra edition to use for the index. Choose DEVELOPER_EDITION for indexes intended for development, testing, or proof of concept. Use ENTERPRISE_EDITION for your production databases. Once you set the edition for an index, it can\'t be changed.

    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nAn IAM role that gives Amazon Kendra permissions to access your Amazon CloudWatch logs and metrics. This is also the role used when you use the BatchPutDocument operation to index documents from an Amazon S3 bucket.\n

    :type ServerSideEncryptionConfiguration: dict
    :param ServerSideEncryptionConfiguration: The identifier of the AWS KMS customer managed key (CMK) to use to encrypt data indexed by Amazon Kendra. Amazon Kendra doesn\'t support asymmetric CMKs.\n\nKmsKeyId (string) --The identifier of the AWS KMS customer master key (CMK). Amazon Kendra doesn\'t support asymmetric CMKs.\n\n\n

    :type Description: string
    :param Description: A description for the index.

    :type ClientToken: string
    :param ClientToken: A token that you provide to identify the request to create an index. Multiple calls to the CreateIndex operation with the same client token will create only one index.\xe2\x80\x9d\nThis field is autopopulated if not provided.\n

    :type Tags: list
    :param Tags: A list of key-value pairs that identify the index. You can use the tags to identify and organize your resources and to control access to resources.\n\n(dict) --A list of key/value pairs that identify an index, FAQ, or data source. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.\n\nKey (string) -- [REQUIRED]The key for the tag. Keys are not case sensitive and must be unique for the index, FAQ, or data source.\n\nValue (string) -- [REQUIRED]The value associated with the tag. The value may be an empty string but it can\'t be null.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Id': 'string'
}


Response Structure

(dict) --

Id (string) --
The unique identifier of the index. Use this identifier when you query an index, set up a data source, or index a document.







Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ResourceAlreadyExistException
kendra.Client.exceptions.ServiceQuotaExceededException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.ConflictException
kendra.Client.exceptions.InternalServerException


    :return: {
        'Id': 'string'
    }
    
    
    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ResourceAlreadyExistException
    kendra.Client.exceptions.ServiceQuotaExceededException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.ConflictException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def delete_data_source(Id=None, IndexId=None):
    """
    Deletes an Amazon Kendra data source. An exception is not thrown if the data source is already being deleted. While the data source is being deleted, the Status field returned by a call to the operation is set to DELETING . For more information, see Deleting Data Sources .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_data_source(
        Id='string',
        IndexId='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe unique identifier of the data source to delete.\n

    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe unique identifier of the index associated with the data source.\n

    :returns: 
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ConflictException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def delete_faq(Id=None, IndexId=None):
    """
    Removes an FAQ from an index.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_faq(
        Id='string',
        IndexId='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe identifier of the FAQ to remove.\n

    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe index to remove the FAQ from.\n

    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ConflictException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def delete_index(Id=None):
    """
    Deletes an existing Amazon Kendra index. An exception is not thrown if the index is already being deleted. While the index is being deleted, the Status field returned by a call to the  DescribeIndex operation is set to DELETING .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_index(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe identifier of the index to delete.\n

    """
    pass

def describe_data_source(Id=None, IndexId=None):
    """
    Gets information about a Amazon Kendra data source.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_data_source(
        Id='string',
        IndexId='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe unique identifier of the data source to describe.\n

    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe identifier of the index that contains the data source.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Id': 'string',
    'IndexId': 'string',
    'Name': 'string',
    'Type': 'S3'|'SHAREPOINT'|'DATABASE'|'SALESFORCE'|'ONEDRIVE'|'SERVICENOW',
    'Configuration': {
        'S3Configuration': {
            'BucketName': 'string',
            'InclusionPrefixes': [
                'string',
            ],
            'ExclusionPatterns': [
                'string',
            ],
            'DocumentsMetadataConfiguration': {
                'S3Prefix': 'string'
            },
            'AccessControlListConfiguration': {
                'KeyPath': 'string'
            }
        },
        'SharePointConfiguration': {
            'SharePointVersion': 'SHAREPOINT_ONLINE',
            'Urls': [
                'string',
            ],
            'SecretArn': 'string',
            'CrawlAttachments': True|False,
            'UseChangeLog': True|False,
            'InclusionPatterns': [
                'string',
            ],
            'ExclusionPatterns': [
                'string',
            ],
            'VpcConfiguration': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            },
            'FieldMappings': [
                {
                    'DataSourceFieldName': 'string',
                    'DateFieldFormat': 'string',
                    'IndexFieldName': 'string'
                },
            ],
            'DocumentTitleFieldName': 'string'
        },
        'DatabaseConfiguration': {
            'DatabaseEngineType': 'RDS_AURORA_MYSQL'|'RDS_AURORA_POSTGRESQL'|'RDS_MYSQL'|'RDS_POSTGRESQL',
            'ConnectionConfiguration': {
                'DatabaseHost': 'string',
                'DatabasePort': 123,
                'DatabaseName': 'string',
                'TableName': 'string',
                'SecretArn': 'string'
            },
            'VpcConfiguration': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            },
            'ColumnConfiguration': {
                'DocumentIdColumnName': 'string',
                'DocumentDataColumnName': 'string',
                'DocumentTitleColumnName': 'string',
                'FieldMappings': [
                    {
                        'DataSourceFieldName': 'string',
                        'DateFieldFormat': 'string',
                        'IndexFieldName': 'string'
                    },
                ],
                'ChangeDetectingColumns': [
                    'string',
                ]
            },
            'AclConfiguration': {
                'AllowedGroupsColumnName': 'string'
            }
        },
        'SalesforceConfiguration': {
            'ServerUrl': 'string',
            'SecretArn': 'string',
            'StandardObjectConfigurations': [
                {
                    'Name': 'ACCOUNT'|'CAMPAIGN'|'CASE'|'CONTACT'|'CONTRACT'|'DOCUMENT'|'GROUP'|'IDEA'|'LEAD'|'OPPORTUNITY'|'PARTNER'|'PRICEBOOK'|'PRODUCT'|'PROFILE'|'SOLUTION'|'TASK'|'USER',
                    'DocumentDataFieldName': 'string',
                    'DocumentTitleFieldName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ]
                },
            ],
            'KnowledgeArticleConfiguration': {
                'IncludedStates': [
                    'DRAFT'|'PUBLISHED'|'ARCHIVED',
                ],
                'StandardKnowledgeArticleTypeConfiguration': {
                    'DocumentDataFieldName': 'string',
                    'DocumentTitleFieldName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ]
                },
                'CustomKnowledgeArticleTypeConfigurations': [
                    {
                        'Name': 'string',
                        'DocumentDataFieldName': 'string',
                        'DocumentTitleFieldName': 'string',
                        'FieldMappings': [
                            {
                                'DataSourceFieldName': 'string',
                                'DateFieldFormat': 'string',
                                'IndexFieldName': 'string'
                            },
                        ]
                    },
                ]
            },
            'ChatterFeedConfiguration': {
                'DocumentDataFieldName': 'string',
                'DocumentTitleFieldName': 'string',
                'FieldMappings': [
                    {
                        'DataSourceFieldName': 'string',
                        'DateFieldFormat': 'string',
                        'IndexFieldName': 'string'
                    },
                ],
                'IncludeFilterTypes': [
                    'ACTIVE_USER'|'STANDARD_USER',
                ]
            },
            'CrawlAttachments': True|False,
            'StandardObjectAttachmentConfiguration': {
                'DocumentTitleFieldName': 'string',
                'FieldMappings': [
                    {
                        'DataSourceFieldName': 'string',
                        'DateFieldFormat': 'string',
                        'IndexFieldName': 'string'
                    },
                ]
            },
            'IncludeAttachmentFilePatterns': [
                'string',
            ],
            'ExcludeAttachmentFilePatterns': [
                'string',
            ]
        },
        'OneDriveConfiguration': {
            'TenantDomain': 'string',
            'SecretArn': 'string',
            'OneDriveUsers': {
                'OneDriveUserList': [
                    'string',
                ],
                'OneDriveUserS3Path': {
                    'Bucket': 'string',
                    'Key': 'string'
                }
            },
            'InclusionPatterns': [
                'string',
            ],
            'ExclusionPatterns': [
                'string',
            ],
            'FieldMappings': [
                {
                    'DataSourceFieldName': 'string',
                    'DateFieldFormat': 'string',
                    'IndexFieldName': 'string'
                },
            ]
        },
        'ServiceNowConfiguration': {
            'HostUrl': 'string',
            'SecretArn': 'string',
            'ServiceNowBuildVersion': 'LONDON'|'OTHERS',
            'KnowledgeArticleConfiguration': {
                'CrawlAttachments': True|False,
                'IncludeAttachmentFilePatterns': [
                    'string',
                ],
                'ExcludeAttachmentFilePatterns': [
                    'string',
                ],
                'DocumentDataFieldName': 'string',
                'DocumentTitleFieldName': 'string',
                'FieldMappings': [
                    {
                        'DataSourceFieldName': 'string',
                        'DateFieldFormat': 'string',
                        'IndexFieldName': 'string'
                    },
                ]
            },
            'ServiceCatalogConfiguration': {
                'CrawlAttachments': True|False,
                'IncludeAttachmentFilePatterns': [
                    'string',
                ],
                'ExcludeAttachmentFilePatterns': [
                    'string',
                ],
                'DocumentDataFieldName': 'string',
                'DocumentTitleFieldName': 'string',
                'FieldMappings': [
                    {
                        'DataSourceFieldName': 'string',
                        'DateFieldFormat': 'string',
                        'IndexFieldName': 'string'
                    },
                ]
            }
        }
    },
    'CreatedAt': datetime(2015, 1, 1),
    'UpdatedAt': datetime(2015, 1, 1),
    'Description': 'string',
    'Status': 'CREATING'|'DELETING'|'FAILED'|'UPDATING'|'ACTIVE',
    'Schedule': 'string',
    'RoleArn': 'string',
    'ErrorMessage': 'string'
}


Response Structure

(dict) --

Id (string) --
The identifier of the data source.

IndexId (string) --
The identifier of the index that contains the data source.

Name (string) --
The name that you gave the data source when it was created.

Type (string) --
The type of the data source.

Configuration (dict) --
Information that describes where the data source is located and how the data source is configured. The specific information in the description depends on the data source provider.

S3Configuration (dict) --
Provides information to create a connector for a document repository in an Amazon S3 bucket.

BucketName (string) --
The name of the bucket that contains the documents.

InclusionPrefixes (list) --
A list of S3 prefixes for the documents that should be included in the index.

(string) --


ExclusionPatterns (list) --
A list of glob patterns for documents that should not be indexed. If a document that matches an inclusion prefix also matches an exclusion pattern, the document is not indexed.
For more information about glob patterns, see glob (programming) in Wikipedia .

(string) --


DocumentsMetadataConfiguration (dict) --
Document metadata files that contain information such as the document access control information, source URI, document author, and custom attributes. Each metadata file contains metadata about a single document.

S3Prefix (string) --
A prefix used to filter metadata configuration files in the AWS S3 bucket. The S3 bucket might contain multiple metadata files. Use S3Prefix to include only the desired metadata files.



AccessControlListConfiguration (dict) --
Provides the path to the S3 bucket that contains the user context filtering files for the data source.

KeyPath (string) --
Path to the AWS S3 bucket that contains the ACL files.





SharePointConfiguration (dict) --
Provides information necessary to create a connector for a Microsoft SharePoint site.

SharePointVersion (string) --
The version of Microsoft SharePoint that you are using as a data source.

Urls (list) --
The URLs of the Microsoft SharePoint site that contains the documents that should be indexed.

(string) --


SecretArn (string) --
The Amazon Resource Name (ARN) of credentials stored in AWS Secrets Manager. The credentials should be a user/password pair. For more information, see Using a Microsoft SharePoint Data Source . For more information about AWS Secrets Manager, see What Is AWS Secrets Manager in the AWS Secrets Manager user guide.

CrawlAttachments (boolean) --

TRUE to include attachments to documents stored in your Microsoft SharePoint site in the index; otherwise, FALSE .


UseChangeLog (boolean) --
Set to TRUE to use the Microsoft SharePoint change log to determine the documents that need to be updated in the index. Depending on the size of the SharePoint change log, it may take longer for Amazon Kendra to use the change log than it takes it to determine the changed documents using the Amazon Kendra document crawler.

InclusionPatterns (list) --
A list of regular expression patterns. Documents that match the patterns are included in the index. Documents that don\'t match the patterns are excluded from the index. If a document matches both an inclusion pattern and an exclusion pattern, the document is not included in the index.
The regex is applied to the display URL of the SharePoint document.

(string) --


ExclusionPatterns (list) --
A list of regulary expression patterns. Documents that match the patterns are excluded from the index. Documents that don\'t match the patterns are included in the index. If a document matches both an exclusion pattern and an inclusion pattern, the document is not included in the index.
The regex is applied to the display URL of the SharePoint document.

(string) --


VpcConfiguration (dict) --
Provides information for connecting to an Amazon VPC.

SubnetIds (list) --
A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

(string) --


SecurityGroupIds (list) --
A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.

(string) --




FieldMappings (list) --
A list of DataSourceToIndexFieldMapping objects that map Microsoft SharePoint attributes to custom fields in the Amazon Kendra index. You must first create the index fields using the operation before you map SharePoint attributes. For more information, see Mapping Data Source Fields .

(dict) --
Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the  UpdateIndex operation.

DataSourceFieldName (string) --
The name of the column or attribute in the data source.

DateFieldFormat (string) --
The type of data stored in the column or attribute.

IndexFieldName (string) --
The name of the field in the index.





DocumentTitleFieldName (string) --
The Microsoft SharePoint attribute field that contains the title of the document.



DatabaseConfiguration (dict) --
Provides information necessary to create a connector for a database.

DatabaseEngineType (string) --
The type of database engine that runs the database.

ConnectionConfiguration (dict) --
The information necessary to connect to a database.

DatabaseHost (string) --
The name of the host for the database. Can be either a string (host.subdomain.domain.tld) or an IPv4 or IPv6 address.

DatabasePort (integer) --
The port that the database uses for connections.

DatabaseName (string) --
The name of the database containing the document data.

TableName (string) --
The name of the table that contains the document data.

SecretArn (string) --
The Amazon Resource Name (ARN) of credentials stored in AWS Secrets Manager. The credentials should be a user/password pair. For more information, see Using a Database Data Source . For more information about AWS Secrets Manager, see What Is AWS Secrets Manager in the AWS Secrets Manager user guide.



VpcConfiguration (dict) --
Provides information for connecting to an Amazon VPC.

SubnetIds (list) --
A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

(string) --


SecurityGroupIds (list) --
A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.

(string) --




ColumnConfiguration (dict) --
Information about where the index should get the document information from the database.

DocumentIdColumnName (string) --
The column that provides the document\'s unique identifier.

DocumentDataColumnName (string) --
The column that contains the contents of the document.

DocumentTitleColumnName (string) --
The column that contains the title of the document.

FieldMappings (list) --
An array of objects that map database column names to the corresponding fields in an index. You must first create the fields in the index using the  UpdateIndex operation.

(dict) --
Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the  UpdateIndex operation.

DataSourceFieldName (string) --
The name of the column or attribute in the data source.

DateFieldFormat (string) --
The type of data stored in the column or attribute.

IndexFieldName (string) --
The name of the field in the index.





ChangeDetectingColumns (list) --
One to five columns that indicate when a document in the database has changed.

(string) --




AclConfiguration (dict) --
Information about the database column that provides information for user context filtering.

AllowedGroupsColumnName (string) --
A list of groups, separated by semi-colons, that filters a query response based on user context. The document is only returned to users that are in one of the groups specified in the UserContext field of the  Query operation.





SalesforceConfiguration (dict) --
Provides configuration information for data sources that connect to a Salesforce site.

ServerUrl (string) --
The instance URL for the Salesforce site that you want to index.

SecretArn (string) --
The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the key/value pairs required to connect to your Salesforce instance. The secret must contain a JSON structure with the following keys:

authenticationUrl - The OAUTH endpoint that Amazon Kendra connects to get an OAUTH token.
consumerKey - The application public key generated when you created your Salesforce application.
consumerSecret - The application private key generated when you created your Salesforce application.
password - The password associated with the user logging in to the Salesforce instance.
securityToken - The token associated with the user account logging in to the Salesforce instance.
username - The user name of the user logging in to the Salesforce instance.


StandardObjectConfigurations (list) --
Specifies the Salesforce standard objects that Amazon Kendra indexes.

(dict) --
Specifies confguration information for indexing a single standard object.

Name (string) --
The name of the standard object.

DocumentDataFieldName (string) --
The name of the field in the standard object table that contains the document contents.

DocumentTitleFieldName (string) --
The name of the field in the standard object table that contains the document titleB.

FieldMappings (list) --
One or more objects that map fields in the standard object to Amazon Kendra index fields. The index field must exist before you can map a Salesforce field to it.

(dict) --
Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the  UpdateIndex operation.

DataSourceFieldName (string) --
The name of the column or attribute in the data source.

DateFieldFormat (string) --
The type of data stored in the column or attribute.

IndexFieldName (string) --
The name of the field in the index.









KnowledgeArticleConfiguration (dict) --
Specifies configuration information for the knowlege article types that Amazon Kendra indexes. Amazon Kendra indexes standard knowledge articles and the standard fields of knowledge articles, or the custom fields of custom knowledge articles, but not both.

IncludedStates (list) --
Specifies the document states that should be included when Amazon Kendra indexes knowledge articles. You must specify at least one state.

(string) --


StandardKnowledgeArticleTypeConfiguration (dict) --
Provides configuration information for standard Salesforce knowledge articles.

DocumentDataFieldName (string) --
The name of the field that contains the document data to index.

DocumentTitleFieldName (string) --
The name of the field that contains the document title.

FieldMappings (list) --
One or more objects that map fields in the knowledge article to Amazon Kendra index fields. The index field must exist before you can map a Salesforce field to it.

(dict) --
Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the  UpdateIndex operation.

DataSourceFieldName (string) --
The name of the column or attribute in the data source.

DateFieldFormat (string) --
The type of data stored in the column or attribute.

IndexFieldName (string) --
The name of the field in the index.







CustomKnowledgeArticleTypeConfigurations (list) --
Provides configuration information for custom Salesforce knowledge articles.

(dict) --
Provides configuration information for indexing Salesforce custom articles.

Name (string) --
The name of the configuration.

DocumentDataFieldName (string) --
The name of the field in the custom knowledge article that contains the document data to index.

DocumentTitleFieldName (string) --
The name of the field in the custom knowledge article that contains the document title.

FieldMappings (list) --
One or more objects that map fields in the custom knowledge article to fields in the Amazon Kendra index.

(dict) --
Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the  UpdateIndex operation.

DataSourceFieldName (string) --
The name of the column or attribute in the data source.

DateFieldFormat (string) --
The type of data stored in the column or attribute.

IndexFieldName (string) --
The name of the field in the index.











ChatterFeedConfiguration (dict) --
Specifies configuration information for Salesforce chatter feeds.

DocumentDataFieldName (string) --
The name of the column in the Salesforce FeedItem table that contains the content to index. Typically this is the Body column.

DocumentTitleFieldName (string) --
The name of the column in the Salesforce FeedItem table that contains the title of the document. This is typically the Title collumn.

FieldMappings (list) --
Maps fields from a Salesforce chatter feed into Amazon Kendra index fields.

(dict) --
Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the  UpdateIndex operation.

DataSourceFieldName (string) --
The name of the column or attribute in the data source.

DateFieldFormat (string) --
The type of data stored in the column or attribute.

IndexFieldName (string) --
The name of the field in the index.





IncludeFilterTypes (list) --
Filters the documents in the feed based on status of the user. When you specify ACTIVE_USERS only documents from users who have an active account are indexed. When you specify STANDARD_USER only documents for Salesforce standard users are documented. You can specify both.

(string) --




CrawlAttachments (boolean) --
Indicates whether Amazon Kendra should index attachments to Salesforce objects.

StandardObjectAttachmentConfiguration (dict) --
Provides configuration information for processing attachments to Salesforce standard objects.

DocumentTitleFieldName (string) --
The name of the field used for the document title.

FieldMappings (list) --
One or more objects that map fields in attachments to Amazon Kendra index fields.

(dict) --
Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the  UpdateIndex operation.

DataSourceFieldName (string) --
The name of the column or attribute in the data source.

DateFieldFormat (string) --
The type of data stored in the column or attribute.

IndexFieldName (string) --
The name of the field in the index.







IncludeAttachmentFilePatterns (list) --
A list of regular expression patterns. Documents that match the patterns are included in the index. Documents that don\'t match the patterns are excluded from the index. If a document matches both an inclusion pattern and an exclusion pattern, the document is not included in the index.
The regex is applied to the name of the attached file.

(string) --


ExcludeAttachmentFilePatterns (list) --
A list of regular expression patterns. Documents that match the patterns are excluded from the index. Documents that don\'t match the patterns are included in the index. If a document matches both an exclusion pattern and an inclusion pattern, the document is not included in the index.
The regex is applied to the name of the attached file.

(string) --




OneDriveConfiguration (dict) --
Provided configuration for data sources that connect to Microsoft OneDrive.

TenantDomain (string) --
Tha Azure Active Directory domain of the organization.

SecretArn (string) --
The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the user name and password to connect to OneDrive. The user namd should be the application ID for the OneDrive application, and the password is the application key for the OneDrive application.

OneDriveUsers (dict) --
A list of user accounts whose documents should be indexed.

OneDriveUserList (list) --
A list of users whose documents should be indexed. Specify the user names in email format, for example, username@tenantdomain . If you need to index the documents of more than 100 users, use the OneDriveUserS3Path field to specify the location of a file containing a list of users.

(string) --


OneDriveUserS3Path (dict) --
The S3 bucket location of a file containing a list of users whose documents should be indexed.

Bucket (string) --
The name of the S3 bucket that contains the file.

Key (string) --
The name of the file.





InclusionPatterns (list) --
A list of regular expression patterns. Documents that match the pattern are included in the index. Documents that don\'t match the pattern are excluded from the index. If a document matches both an inclusion pattern and an exclusion pattern, the document is not included in the index.
The exclusion pattern is applied to the file name.

(string) --


ExclusionPatterns (list) --
List of regular expressions applied to documents. Items that match the exclusion pattern are not indexed. If you provide both an inclusion pattern and an exclusion pattern, any item that matches the exclusion pattern isn\'t indexed.
The exclusion pattern is applied to the file name.

(string) --


FieldMappings (list) --
A list of DataSourceToIndexFieldMapping objects that map Microsoft OneDrive fields to custom fields in the Amazon Kendra index. You must first create the index fields before you map OneDrive fields.

(dict) --
Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the  UpdateIndex operation.

DataSourceFieldName (string) --
The name of the column or attribute in the data source.

DateFieldFormat (string) --
The type of data stored in the column or attribute.

IndexFieldName (string) --
The name of the field in the index.







ServiceNowConfiguration (dict) --
Provides configuration for data sources that connect to ServiceNow instances.

HostUrl (string) --
The ServiceNow instance that the data source connects to. The host endpoint should look like the following: {instance}.service-now.com.

SecretArn (string) --
The Amazon Resource Name (ARN) of the AWS Secret Manager secret that contains the user name and password required to connect to the ServiceNow instance.

ServiceNowBuildVersion (string) --
The identifier of the release that the ServiceNow host is running. If the host is not running the LONDON release, use OTHERS .

KnowledgeArticleConfiguration (dict) --
Provides configuration information for crawling knowledge articles in the ServiceNow site.

CrawlAttachments (boolean) --
Indicates whether Amazon Kendra should index attachments to knowledge articles.

IncludeAttachmentFilePatterns (list) --
List of regular expressions applied to knowledge articles. Items that don\'t match the inclusion pattern are not indexed. The regex is applied to the field specified in the PatternTargetField .

(string) --


ExcludeAttachmentFilePatterns (list) --
List of regular expressions applied to knowledge articles. Items that don\'t match the inclusion pattern are not indexed. The regex is applied to the field specified in the PatternTargetField

(string) --


DocumentDataFieldName (string) --
The name of the ServiceNow field that is mapped to the index document contents field in the Amazon Kendra index.

DocumentTitleFieldName (string) --
The name of the ServiceNow field that is mapped to the index document title field.

FieldMappings (list) --
Mapping between ServiceNow fields and Amazon Kendra index fields. You must create the index field before you map the field.

(dict) --
Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the  UpdateIndex operation.

DataSourceFieldName (string) --
The name of the column or attribute in the data source.

DateFieldFormat (string) --
The type of data stored in the column or attribute.

IndexFieldName (string) --
The name of the field in the index.







ServiceCatalogConfiguration (dict) --
Provides configuration information for crawling service catalogs in the ServiceNow site.

CrawlAttachments (boolean) --
Indicates whether Amazon Kendra should crawl attachments to the service catalog items.

IncludeAttachmentFilePatterns (list) --
Determines the types of file attachments that are included in the index.

(string) --


ExcludeAttachmentFilePatterns (list) --
Determines the types of file attachments that are excluded from the index.

(string) --


DocumentDataFieldName (string) --
The name of the ServiceNow field that is mapped to the index document contents field in the Amazon Kendra index.

DocumentTitleFieldName (string) --
The name of the ServiceNow field that is mapped to the index document title field.

FieldMappings (list) --
Mapping between ServiceNow fields and Amazon Kendra index fields. You must create the index field before you map the field.

(dict) --
Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the  UpdateIndex operation.

DataSourceFieldName (string) --
The name of the column or attribute in the data source.

DateFieldFormat (string) --
The type of data stored in the column or attribute.

IndexFieldName (string) --
The name of the field in the index.











CreatedAt (datetime) --
The Unix timestamp of when the data source was created.

UpdatedAt (datetime) --
The Unix timestamp of when the data source was last updated.

Description (string) --
The description of the data source.

Status (string) --
The current status of the data source. When the status is ACTIVE the data source is ready to use. When the status is FAILED , the ErrorMessage field contains the reason that the data source failed.

Schedule (string) --
The schedule that Amazon Kendra will update the data source.

RoleArn (string) --
The Amazon Resource Name (ARN) of the role that enables the data source to access its resources.

ErrorMessage (string) --
When the Status field value is FAILED , the ErrorMessage field contains a description of the error that caused the data source to fail.







Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ResourceNotFoundException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.InternalServerException


    :return: {
        'Id': 'string',
        'IndexId': 'string',
        'Name': 'string',
        'Type': 'S3'|'SHAREPOINT'|'DATABASE'|'SALESFORCE'|'ONEDRIVE'|'SERVICENOW',
        'Configuration': {
            'S3Configuration': {
                'BucketName': 'string',
                'InclusionPrefixes': [
                    'string',
                ],
                'ExclusionPatterns': [
                    'string',
                ],
                'DocumentsMetadataConfiguration': {
                    'S3Prefix': 'string'
                },
                'AccessControlListConfiguration': {
                    'KeyPath': 'string'
                }
            },
            'SharePointConfiguration': {
                'SharePointVersion': 'SHAREPOINT_ONLINE',
                'Urls': [
                    'string',
                ],
                'SecretArn': 'string',
                'CrawlAttachments': True|False,
                'UseChangeLog': True|False,
                'InclusionPatterns': [
                    'string',
                ],
                'ExclusionPatterns': [
                    'string',
                ],
                'VpcConfiguration': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'FieldMappings': [
                    {
                        'DataSourceFieldName': 'string',
                        'DateFieldFormat': 'string',
                        'IndexFieldName': 'string'
                    },
                ],
                'DocumentTitleFieldName': 'string'
            },
            'DatabaseConfiguration': {
                'DatabaseEngineType': 'RDS_AURORA_MYSQL'|'RDS_AURORA_POSTGRESQL'|'RDS_MYSQL'|'RDS_POSTGRESQL',
                'ConnectionConfiguration': {
                    'DatabaseHost': 'string',
                    'DatabasePort': 123,
                    'DatabaseName': 'string',
                    'TableName': 'string',
                    'SecretArn': 'string'
                },
                'VpcConfiguration': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'ColumnConfiguration': {
                    'DocumentIdColumnName': 'string',
                    'DocumentDataColumnName': 'string',
                    'DocumentTitleColumnName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ],
                    'ChangeDetectingColumns': [
                        'string',
                    ]
                },
                'AclConfiguration': {
                    'AllowedGroupsColumnName': 'string'
                }
            },
            'SalesforceConfiguration': {
                'ServerUrl': 'string',
                'SecretArn': 'string',
                'StandardObjectConfigurations': [
                    {
                        'Name': 'ACCOUNT'|'CAMPAIGN'|'CASE'|'CONTACT'|'CONTRACT'|'DOCUMENT'|'GROUP'|'IDEA'|'LEAD'|'OPPORTUNITY'|'PARTNER'|'PRICEBOOK'|'PRODUCT'|'PROFILE'|'SOLUTION'|'TASK'|'USER',
                        'DocumentDataFieldName': 'string',
                        'DocumentTitleFieldName': 'string',
                        'FieldMappings': [
                            {
                                'DataSourceFieldName': 'string',
                                'DateFieldFormat': 'string',
                                'IndexFieldName': 'string'
                            },
                        ]
                    },
                ],
                'KnowledgeArticleConfiguration': {
                    'IncludedStates': [
                        'DRAFT'|'PUBLISHED'|'ARCHIVED',
                    ],
                    'StandardKnowledgeArticleTypeConfiguration': {
                        'DocumentDataFieldName': 'string',
                        'DocumentTitleFieldName': 'string',
                        'FieldMappings': [
                            {
                                'DataSourceFieldName': 'string',
                                'DateFieldFormat': 'string',
                                'IndexFieldName': 'string'
                            },
                        ]
                    },
                    'CustomKnowledgeArticleTypeConfigurations': [
                        {
                            'Name': 'string',
                            'DocumentDataFieldName': 'string',
                            'DocumentTitleFieldName': 'string',
                            'FieldMappings': [
                                {
                                    'DataSourceFieldName': 'string',
                                    'DateFieldFormat': 'string',
                                    'IndexFieldName': 'string'
                                },
                            ]
                        },
                    ]
                },
                'ChatterFeedConfiguration': {
                    'DocumentDataFieldName': 'string',
                    'DocumentTitleFieldName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ],
                    'IncludeFilterTypes': [
                        'ACTIVE_USER'|'STANDARD_USER',
                    ]
                },
                'CrawlAttachments': True|False,
                'StandardObjectAttachmentConfiguration': {
                    'DocumentTitleFieldName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ]
                },
                'IncludeAttachmentFilePatterns': [
                    'string',
                ],
                'ExcludeAttachmentFilePatterns': [
                    'string',
                ]
            },
            'OneDriveConfiguration': {
                'TenantDomain': 'string',
                'SecretArn': 'string',
                'OneDriveUsers': {
                    'OneDriveUserList': [
                        'string',
                    ],
                    'OneDriveUserS3Path': {
                        'Bucket': 'string',
                        'Key': 'string'
                    }
                },
                'InclusionPatterns': [
                    'string',
                ],
                'ExclusionPatterns': [
                    'string',
                ],
                'FieldMappings': [
                    {
                        'DataSourceFieldName': 'string',
                        'DateFieldFormat': 'string',
                        'IndexFieldName': 'string'
                    },
                ]
            },
            'ServiceNowConfiguration': {
                'HostUrl': 'string',
                'SecretArn': 'string',
                'ServiceNowBuildVersion': 'LONDON'|'OTHERS',
                'KnowledgeArticleConfiguration': {
                    'CrawlAttachments': True|False,
                    'IncludeAttachmentFilePatterns': [
                        'string',
                    ],
                    'ExcludeAttachmentFilePatterns': [
                        'string',
                    ],
                    'DocumentDataFieldName': 'string',
                    'DocumentTitleFieldName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ]
                },
                'ServiceCatalogConfiguration': {
                    'CrawlAttachments': True|False,
                    'IncludeAttachmentFilePatterns': [
                        'string',
                    ],
                    'ExcludeAttachmentFilePatterns': [
                        'string',
                    ],
                    'DocumentDataFieldName': 'string',
                    'DocumentTitleFieldName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ]
                }
            }
        },
        'CreatedAt': datetime(2015, 1, 1),
        'UpdatedAt': datetime(2015, 1, 1),
        'Description': 'string',
        'Status': 'CREATING'|'DELETING'|'FAILED'|'UPDATING'|'ACTIVE',
        'Schedule': 'string',
        'RoleArn': 'string',
        'ErrorMessage': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_faq(Id=None, IndexId=None):
    """
    Gets information about an FAQ list.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_faq(
        Id='string',
        IndexId='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe unique identifier of the FAQ.\n

    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe identifier of the index that contains the FAQ.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Id': 'string',
    'IndexId': 'string',
    'Name': 'string',
    'Description': 'string',
    'CreatedAt': datetime(2015, 1, 1),
    'UpdatedAt': datetime(2015, 1, 1),
    'S3Path': {
        'Bucket': 'string',
        'Key': 'string'
    },
    'Status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'|'FAILED',
    'RoleArn': 'string',
    'ErrorMessage': 'string'
}


Response Structure

(dict) --

Id (string) --
The identifier of the FAQ.

IndexId (string) --
The identifier of the index that contains the FAQ.

Name (string) --
The name that you gave the FAQ when it was created.

Description (string) --
The description of the FAQ that you provided when it was created.

CreatedAt (datetime) --
The date and time that the FAQ was created.

UpdatedAt (datetime) --
The date and time that the FAQ was last updated.

S3Path (dict) --
Information required to find a specific file in an Amazon S3 bucket.

Bucket (string) --
The name of the S3 bucket that contains the file.

Key (string) --
The name of the file.



Status (string) --
The status of the FAQ. It is ready to use when the status is ACTIVE .

RoleArn (string) --
The Amazon Resource Name (ARN) of the role that provides access to the S3 bucket containing the input files for the FAQ.

ErrorMessage (string) --
If the Status field is FAILED , the ErrorMessage field contains the reason why the FAQ failed.







Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ResourceNotFoundException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.InternalServerException


    :return: {
        'Id': 'string',
        'IndexId': 'string',
        'Name': 'string',
        'Description': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'UpdatedAt': datetime(2015, 1, 1),
        'S3Path': {
            'Bucket': 'string',
            'Key': 'string'
        },
        'Status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'|'FAILED',
        'RoleArn': 'string',
        'ErrorMessage': 'string'
    }
    
    
    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def describe_index(Id=None):
    """
    Describes an existing Amazon Kendra index
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_index(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe name of the index to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Name': 'string',
    'Id': 'string',
    'Edition': 'DEVELOPER_EDITION'|'ENTERPRISE_EDITION',
    'RoleArn': 'string',
    'ServerSideEncryptionConfiguration': {
        'KmsKeyId': 'string'
    },
    'Status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED'|'UPDATING'|'SYSTEM_UPDATING',
    'Description': 'string',
    'CreatedAt': datetime(2015, 1, 1),
    'UpdatedAt': datetime(2015, 1, 1),
    'DocumentMetadataConfigurations': [
        {
            'Name': 'string',
            'Type': 'STRING_VALUE'|'STRING_LIST_VALUE'|'LONG_VALUE'|'DATE_VALUE',
            'Relevance': {
                'Freshness': True|False,
                'Importance': 123,
                'Duration': 'string',
                'RankOrder': 'ASCENDING'|'DESCENDING',
                'ValueImportanceMap': {
                    'string': 123
                }
            },
            'Search': {
                'Facetable': True|False,
                'Searchable': True|False,
                'Displayable': True|False
            }
        },
    ],
    'IndexStatistics': {
        'FaqStatistics': {
            'IndexedQuestionAnswersCount': 123
        },
        'TextDocumentStatistics': {
            'IndexedTextDocumentsCount': 123,
            'IndexedTextBytes': 123
        }
    },
    'ErrorMessage': 'string',
    'CapacityUnits': {
        'StorageCapacityUnits': 123,
        'QueryCapacityUnits': 123
    }
}


Response Structure

(dict) --
Name (string) --The name of the index.

Id (string) --the name of the index.

Edition (string) --The Amazon Kendra edition used for the index. You decide the edition when you create the index.

RoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that gives Amazon Kendra permission to write to your Amazon Cloudwatch logs.

ServerSideEncryptionConfiguration (dict) --The identifier of the AWS KMS customer master key (CMK) used to encrypt your data. Amazon Kendra doesn\'t support asymmetric CMKs.

KmsKeyId (string) --The identifier of the AWS KMS customer master key (CMK). Amazon Kendra doesn\'t support asymmetric CMKs.



Status (string) --The current status of the index. When the value is ACTIVE , the index is ready for use. If the Status field value is FAILED , the ErrorMessage field contains a message that explains why.

Description (string) --The description of the index.

CreatedAt (datetime) --The Unix datetime that the index was created.

UpdatedAt (datetime) --The Unix datetime that the index was last updated.

DocumentMetadataConfigurations (list) --Configuration settings for any metadata applied to the documents in the index.

(dict) --Specifies the properties of a custom index field.

Name (string) --The name of the index field.

Type (string) --The data type of the index field.

Relevance (dict) --Provides manual tuning parameters to determine how the field affects the search results.

Freshness (boolean) --Indicates that this field determines how "fresh" a document is. For example, if document 1 was created on November 5, and document 2 was created on October 31, document 1 is "fresher" than document 2. You can only set the Freshness field on one DATE type field. Only applies to DATE fields.

Importance (integer) --The relative importance of the field in the search. Larger numbers provide more of a boost than smaller numbers.

Duration (string) --Specifies the time period that the boost applies to. For example, to make the boost apply to documents with the field value within the last month, you would use "2628000s". Once the field value is beyond the specified range, the effect of the boost drops off. The higher the importance, the faster the effect drops off. If you don\'t specify a value, the default is 3 months. The value of the field is a numeric string followed by the character "s", for example "86400s" for one day, or "604800s" for one week.
Only applies to DATE fields.

RankOrder (string) --Determines how values should be interpreted.
When the RankOrder field is ASCENDING , higher numbers are better. For example, a document with a rating score of 10 is higher ranking than a document with a rating score of 1.
When the RankOrder field is DESCENDING , lower numbers are better. For example, in a task tracking application, a priority 1 task is more important than a priority 5 task.
Only applies to LONG and DOUBLE fields.

ValueImportanceMap (dict) --A list of values that should be given a different boost when they appear in the result list. For example, if you are boosting a field called "department," query terms that match the department field are boosted in the result. However, you can add entries from the department field to boost documents with those values higher.
For example, you can add entries to the map with names of departments. If you add "HR",5 and "Legal",3 those departments are given special attention when they appear in the metadata of a document. When those terms appear they are given the specified importance instead of the regular importance for the boost.

(string) --
(integer) --






Search (dict) --Provides information about how the field is used during a search.

Facetable (boolean) --Indicates that the field can be used to create search facets, a count of results for each value in the field. The default is false .

Searchable (boolean) --Determines whether the field is used in the search. If the Searchable field is true , you can use relevance tuning to manually tune how Amazon Kendra weights the field in the search. The default is true for string fields and false for number and date fields.

Displayable (boolean) --Determines whether the field is returned in the query response. The default is true .







IndexStatistics (dict) --Provides information about the number of FAQ questions and answers and the number of text documents indexed.

FaqStatistics (dict) --The number of question and answer topics in the index.

IndexedQuestionAnswersCount (integer) --The total number of FAQ questions and answers contained in the index.



TextDocumentStatistics (dict) --The number of text documents indexed.

IndexedTextDocumentsCount (integer) --The number of text documents indexed.

IndexedTextBytes (integer) --The total size, in bytes, of the indexed documents.





ErrorMessage (string) --When th e``Status`` field value is FAILED , the ErrorMessage field contains a message that explains why.

CapacityUnits (dict) --For enterprise edtion indexes, you can choose to use additional capacity to meet the needs of your application. This contains the capacity units used for the index. A 0 for the query capacity or the storage capacity indicates that the index is using the default capacity for the index.

StorageCapacityUnits (integer) --The amount of extra storage capacity for an index. Each capacity unit provides 150 Gb of storage space or 500,000 documents, whichever is reached first.

QueryCapacityUnits (integer) --The amount of extra query capacity for an index. Each capacity unit provides 0.5 queries per second and 40,000 queries per day.








Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ResourceNotFoundException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.InternalServerException


    :return: {
        'Name': 'string',
        'Id': 'string',
        'Edition': 'DEVELOPER_EDITION'|'ENTERPRISE_EDITION',
        'RoleArn': 'string',
        'ServerSideEncryptionConfiguration': {
            'KmsKeyId': 'string'
        },
        'Status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED'|'UPDATING'|'SYSTEM_UPDATING',
        'Description': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'UpdatedAt': datetime(2015, 1, 1),
        'DocumentMetadataConfigurations': [
            {
                'Name': 'string',
                'Type': 'STRING_VALUE'|'STRING_LIST_VALUE'|'LONG_VALUE'|'DATE_VALUE',
                'Relevance': {
                    'Freshness': True|False,
                    'Importance': 123,
                    'Duration': 'string',
                    'RankOrder': 'ASCENDING'|'DESCENDING',
                    'ValueImportanceMap': {
                        'string': 123
                    }
                },
                'Search': {
                    'Facetable': True|False,
                    'Searchable': True|False,
                    'Displayable': True|False
                }
            },
        ],
        'IndexStatistics': {
            'FaqStatistics': {
                'IndexedQuestionAnswersCount': 123
            },
            'TextDocumentStatistics': {
                'IndexedTextDocumentsCount': 123,
                'IndexedTextBytes': 123
            }
        },
        'ErrorMessage': 'string',
        'CapacityUnits': {
            'StorageCapacityUnits': 123,
            'QueryCapacityUnits': 123
        }
    }
    
    
    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.InternalServerException
    
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

def list_data_source_sync_jobs(Id=None, IndexId=None, NextToken=None, MaxResults=None, StartTimeFilter=None, StatusFilter=None):
    """
    Gets statistics about synchronizing Amazon Kendra with a data source.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_data_source_sync_jobs(
        Id='string',
        IndexId='string',
        NextToken='string',
        MaxResults=123,
        StartTimeFilter={
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1)
        },
        StatusFilter='FAILED'|'SUCCEEDED'|'SYNCING'|'INCOMPLETE'|'STOPPING'|'ABORTED'|'SYNCING_INDEXING'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe identifier of the data source.\n

    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe identifier of the index that contains the data source.\n

    :type NextToken: string
    :param NextToken: If the result of the previous request to GetDataSourceSyncJobHistory was truncated, include the NextToken to fetch the next set of jobs.

    :type MaxResults: integer
    :param MaxResults: The maximum number of synchronization jobs to return in the response. If there are fewer results in the list, this response contains only the actual results.

    :type StartTimeFilter: dict
    :param StartTimeFilter: When specified, the synchronization jobs returned in the list are limited to jobs between the specified dates.\n\nStartTime (datetime) --The UNIX datetime of the beginning of the time range.\n\nEndTime (datetime) --The UNIX datetime of the end of the time range.\n\n\n

    :type StatusFilter: string
    :param StatusFilter: When specified, only returns synchronization jobs with the Status field equal to the specified status.

    :rtype: dict

ReturnsResponse Syntax
{
    'History': [
        {
            'ExecutionId': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'Status': 'FAILED'|'SUCCEEDED'|'SYNCING'|'INCOMPLETE'|'STOPPING'|'ABORTED'|'SYNCING_INDEXING',
            'ErrorMessage': 'string',
            'ErrorCode': 'InternalError'|'InvalidRequest',
            'DataSourceErrorCode': 'string',
            'Metrics': {
                'DocumentsAdded': 'string',
                'DocumentsModified': 'string',
                'DocumentsDeleted': 'string',
                'DocumentsFailed': 'string',
                'DocumentsScanned': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

History (list) --
A history of synchronization jobs for the data source.

(dict) --
Provides information about a synchronization job.

ExecutionId (string) --
A unique identifier for the synchronization job.

StartTime (datetime) --
The UNIX datetime that the synchronization job was started.

EndTime (datetime) --
The UNIX datetime that the synchronization job was completed.

Status (string) --
The execution status of the synchronization job. When the Status field is set to SUCCEEDED , the synchronization job is done. If the status code is set to FAILED , the ErrorCode and ErrorMessage fields give you the reason for the failure.

ErrorMessage (string) --
If the Status field is set to ERROR , the ErrorMessage field contains a description of the error that caused the synchronization to fail.

ErrorCode (string) --
If the Status field is set to FAILED , the ErrorCode field contains a the reason that the synchronization failed.

DataSourceErrorCode (string) --
If the reason that the synchronization failed is due to an error with the underlying data source, this field contains a code that identifies the error.

Metrics (dict) --
Maps a batch delete document request to a specific data source sync job. This is optional and should only be supplied when documents are deleted by a connector.

DocumentsAdded (string) --
The number of documents added from the data source up to now in the data source sync.

DocumentsModified (string) --
The number of documents modified in the data source up to now in the data source sync run.

DocumentsDeleted (string) --
The number of documents deleted from the data source up to now in the data source sync run.

DocumentsFailed (string) --
The number of documents that failed to sync from the data source up to now in the data source sync run.

DocumentsScanned (string) --
The current number of documents crawled by the current sync job in the data source.







NextToken (string) --
The GetDataSourceSyncJobHistory operation returns a page of vocabularies at a time. The maximum size of the page is set by the MaxResults parameter. If there are more jobs in the list than the page size, Amazon Kendra returns the NextPage token. Include the token in the next request to the GetDataSourceSyncJobHistory operation to return in the next page of jobs.







Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ResourceNotFoundException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.ConflictException
kendra.Client.exceptions.InternalServerException


    :return: {
        'History': [
            {
                'ExecutionId': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'Status': 'FAILED'|'SUCCEEDED'|'SYNCING'|'INCOMPLETE'|'STOPPING'|'ABORTED'|'SYNCING_INDEXING',
                'ErrorMessage': 'string',
                'ErrorCode': 'InternalError'|'InvalidRequest',
                'DataSourceErrorCode': 'string',
                'Metrics': {
                    'DocumentsAdded': 'string',
                    'DocumentsModified': 'string',
                    'DocumentsDeleted': 'string',
                    'DocumentsFailed': 'string',
                    'DocumentsScanned': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.ConflictException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def list_data_sources(IndexId=None, NextToken=None, MaxResults=None):
    """
    Lists the data sources that you have created.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_data_sources(
        IndexId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe identifier of the index that contains the data source.\n

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of data sources (DataSourceSummaryItems ).

    :type MaxResults: integer
    :param MaxResults: The maximum number of data sources to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'SummaryItems': [
        {
            'Name': 'string',
            'Id': 'string',
            'Type': 'S3'|'SHAREPOINT'|'DATABASE'|'SALESFORCE'|'ONEDRIVE'|'SERVICENOW',
            'CreatedAt': datetime(2015, 1, 1),
            'UpdatedAt': datetime(2015, 1, 1),
            'Status': 'CREATING'|'DELETING'|'FAILED'|'UPDATING'|'ACTIVE'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SummaryItems (list) --
An array of summary information for one or more data sources.

(dict) --
Summary information for a Amazon Kendra data source. Returned in a call to .

Name (string) --
The name of the data source.

Id (string) --
The unique identifier for the data source.

Type (string) --
The type of the data source.

CreatedAt (datetime) --
The UNIX datetime that the data source was created.

UpdatedAt (datetime) --
The UNIX datetime that the data source was lasted updated.

Status (string) --
The status of the data source. When the status is ATIVE the data source is ready to use.





NextToken (string) --
If the response is truncated, Amazon Kendra returns this token that you can use in the subsequent request to retrieve the next set of data sources.







Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ResourceNotFoundException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.InternalServerException


    :return: {
        'SummaryItems': [
            {
                'Name': 'string',
                'Id': 'string',
                'Type': 'S3'|'SHAREPOINT'|'DATABASE'|'SALESFORCE'|'ONEDRIVE'|'SERVICENOW',
                'CreatedAt': datetime(2015, 1, 1),
                'UpdatedAt': datetime(2015, 1, 1),
                'Status': 'CREATING'|'DELETING'|'FAILED'|'UPDATING'|'ACTIVE'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def list_faqs(IndexId=None, NextToken=None, MaxResults=None):
    """
    Gets a list of FAQ lists associated with an index.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_faqs(
        IndexId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe index that contains the FAQ lists.\n

    :type NextToken: string
    :param NextToken: If the result of the previous request to ListFaqs was truncated, include the NextToken to fetch the next set of FAQs.

    :type MaxResults: integer
    :param MaxResults: The maximum number of FAQs to return in the response. If there are fewer results in the list, this response contains only the actual results.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'FaqSummaryItems': [
        {
            'Id': 'string',
            'Name': 'string',
            'Status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'|'FAILED',
            'CreatedAt': datetime(2015, 1, 1),
            'UpdatedAt': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
The ListFaqs operation returns a page of FAQs at a time. The maximum size of the page is set by the MaxResults parameter. If there are more jobs in the list than the page size, Amazon Kendra returns the NextPage token. Include the token in the next request to the ListFaqs operation to return the next page of FAQs.

FaqSummaryItems (list) --
information about the FAQs associated with the specified index.

(dict) --
Provides information about a frequently asked questions and answer contained in an index.

Id (string) --
The unique identifier of the FAQ.

Name (string) --
The name that you assigned the FAQ when you created or updated the FAQ.

Status (string) --
The current status of the FAQ. When the status is ACTIVE the FAQ is ready for use.

CreatedAt (datetime) --
The UNIX datetime that the FAQ was added to the index.

UpdatedAt (datetime) --
The UNIX datetime that the FAQ was last updated.











Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ResourceNotFoundException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.InternalServerException


    :return: {
        'NextToken': 'string',
        'FaqSummaryItems': [
            {
                'Id': 'string',
                'Name': 'string',
                'Status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'|'FAILED',
                'CreatedAt': datetime(2015, 1, 1),
                'UpdatedAt': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def list_indices(NextToken=None, MaxResults=None):
    """
    Lists the Amazon Kendra indexes that you have created.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_indices(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of indexes (DataSourceSummaryItems ).

    :type MaxResults: integer
    :param MaxResults: The maximum number of data sources to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'IndexConfigurationSummaryItems': [
        {
            'Name': 'string',
            'Id': 'string',
            'Edition': 'DEVELOPER_EDITION'|'ENTERPRISE_EDITION',
            'CreatedAt': datetime(2015, 1, 1),
            'UpdatedAt': datetime(2015, 1, 1),
            'Status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED'|'UPDATING'|'SYSTEM_UPDATING'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

IndexConfigurationSummaryItems (list) --
An array of summary information for one or more indexes.

(dict) --
A summary of information about an index.

Name (string) --
The name of the index.

Id (string) --
A unique identifier for the index. Use this to identify the index when you are using operations such as Query , DescribeIndex , UpdateIndex , and DeleteIndex .

Edition (string) --
Indicates whether the index is a enterprise edition index or a developer edition index.

CreatedAt (datetime) --
The Unix timestamp when the index was created.

UpdatedAt (datetime) --
The Unix timestamp when the index was last updated by the UpdateIndex operation.

Status (string) --
The current status of the index. When the status is ACTIVE , the index is ready to search.





NextToken (string) --
If the response is truncated, Amazon Kendra returns this token that you can use in the subsequent request to retrieve the next set of indexes.







Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.InternalServerException


    :return: {
        'IndexConfigurationSummaryItems': [
            {
                'Name': 'string',
                'Id': 'string',
                'Edition': 'DEVELOPER_EDITION'|'ENTERPRISE_EDITION',
                'CreatedAt': datetime(2015, 1, 1),
                'UpdatedAt': datetime(2015, 1, 1),
                'Status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED'|'UPDATING'|'SYSTEM_UPDATING'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def list_tags_for_resource(ResourceARN=None):
    """
    Gets a list of tags associated with a specified resource. Indexes, FAQs, and data sources can have tags associated with them.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceARN='string'
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the index, FAQ, or data source to get a list of tags for.\n

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
Tags (list) --A list of tags associated with the index, FAQ, or data source.

(dict) --A list of key/value pairs that identify an index, FAQ, or data source. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

Key (string) --The key for the tag. Keys are not case sensitive and must be unique for the index, FAQ, or data source.

Value (string) --The value associated with the tag. The value may be an empty string but it can\'t be null.










Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ResourceUnavailableException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.InternalServerException


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

def query(IndexId=None, QueryText=None, AttributeFilter=None, Facets=None, RequestedDocumentAttributes=None, QueryResultTypeFilter=None, PageNumber=None, PageSize=None):
    """
    Searches an active index. Use this API to search your documents using query. The Query operation enables to do faceted search and to filter results based on document attributes.
    It also enables you to provide user context that Amazon Kendra uses to enforce document access control in the search results.
    Amazon Kendra searches your index for text content and question and answer (FAQ) content. By default the response contains three types of results.
    You can specify that the query return only one type of result using the QueryResultTypeConfig parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.query(
        IndexId='string',
        QueryText='string',
        AttributeFilter={
            'AndAllFilters': [
                {'... recursive ...'},
            ],
            'OrAllFilters': [
                {'... recursive ...'},
            ],
            'NotFilter': {'... recursive ...'},
            'EqualsTo': {
                'Key': 'string',
                'Value': {
                    'StringValue': 'string',
                    'StringListValue': [
                        'string',
                    ],
                    'LongValue': 123,
                    'DateValue': datetime(2015, 1, 1)
                }
            },
            'ContainsAll': {
                'Key': 'string',
                'Value': {
                    'StringValue': 'string',
                    'StringListValue': [
                        'string',
                    ],
                    'LongValue': 123,
                    'DateValue': datetime(2015, 1, 1)
                }
            },
            'ContainsAny': {
                'Key': 'string',
                'Value': {
                    'StringValue': 'string',
                    'StringListValue': [
                        'string',
                    ],
                    'LongValue': 123,
                    'DateValue': datetime(2015, 1, 1)
                }
            },
            'GreaterThan': {
                'Key': 'string',
                'Value': {
                    'StringValue': 'string',
                    'StringListValue': [
                        'string',
                    ],
                    'LongValue': 123,
                    'DateValue': datetime(2015, 1, 1)
                }
            },
            'GreaterThanOrEquals': {
                'Key': 'string',
                'Value': {
                    'StringValue': 'string',
                    'StringListValue': [
                        'string',
                    ],
                    'LongValue': 123,
                    'DateValue': datetime(2015, 1, 1)
                }
            },
            'LessThan': {
                'Key': 'string',
                'Value': {
                    'StringValue': 'string',
                    'StringListValue': [
                        'string',
                    ],
                    'LongValue': 123,
                    'DateValue': datetime(2015, 1, 1)
                }
            },
            'LessThanOrEquals': {
                'Key': 'string',
                'Value': {
                    'StringValue': 'string',
                    'StringListValue': [
                        'string',
                    ],
                    'LongValue': 123,
                    'DateValue': datetime(2015, 1, 1)
                }
            }
        },
        Facets=[
            {
                'DocumentAttributeKey': 'string'
            },
        ],
        RequestedDocumentAttributes=[
            'string',
        ],
        QueryResultTypeFilter='DOCUMENT'|'QUESTION_ANSWER'|'ANSWER',
        PageNumber=123,
        PageSize=123
    )
    
    
    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe unique identifier of the index to search. The identifier is returned in the response from the operation.\n

    :type QueryText: string
    :param QueryText: [REQUIRED]\nThe text to search for.\n

    :type AttributeFilter: dict
    :param AttributeFilter: Enables filtered searches based on document attributes. You can only provide one attribute filter; however, the AndAllFilters , NotFilter , and OrAllFilters parameters contain a list of other filters.\nThe AttributeFilter parameter enables you to create a set of filtering rules that a document must satisfy to be included in the query results.\n\nAndAllFilters (list) --Performs a logical AND operation on all supplied filters.\n\n(dict) --Provides filtering the query results based on document attributes.\nWhen you use the AndAllFilters or OrAllFilters , filters you can use 2 layers under the first attribute filter. For example, you can use:\n\n<AndAllFilters>\n\n<OrAllFilters>\n<EqualTo>\n\nIf you use more than 2 layers, you receive a ValidationException exception with the message 'AttributeFilter cannot have a depth of more than 2.'\n\n\n\nOrAllFilters (list) --Performs a logical OR operation on all supplied filters.\n\n(dict) --Provides filtering the query results based on document attributes.\nWhen you use the AndAllFilters or OrAllFilters , filters you can use 2 layers under the first attribute filter. For example, you can use:\n\n<AndAllFilters>\n\n<OrAllFilters>\n<EqualTo>\n\nIf you use more than 2 layers, you receive a ValidationException exception with the message 'AttributeFilter cannot have a depth of more than 2.'\n\n\n\nNotFilter (dict) --Performs a logical NOT operation on all supplied filters.\n\nEqualsTo (dict) --Performs an equals operation on two document attributes.\n\nKey (string) -- [REQUIRED]The identifier for the attribute.\n\nValue (dict) -- [REQUIRED]The value of the attribute.\n\nStringValue (string) --A string, such as 'department'.\n\nStringListValue (list) --A list of strings.\n\n(string) --\n\n\nLongValue (integer) --A long integer value.\n\nDateValue (datetime) --A date value expressed as seconds from the Unix epoch.\n\n\n\n\n\nContainsAll (dict) --Returns true when a document contains all of the specified document attributes. This filter is only appicable to StringListValue metadata.\n\nKey (string) -- [REQUIRED]The identifier for the attribute.\n\nValue (dict) -- [REQUIRED]The value of the attribute.\n\nStringValue (string) --A string, such as 'department'.\n\nStringListValue (list) --A list of strings.\n\n(string) --\n\n\nLongValue (integer) --A long integer value.\n\nDateValue (datetime) --A date value expressed as seconds from the Unix epoch.\n\n\n\n\n\nContainsAny (dict) --Returns true when a document contains any of the specified document attributes.This filter is only appicable to StringListValue metadata.\n\nKey (string) -- [REQUIRED]The identifier for the attribute.\n\nValue (dict) -- [REQUIRED]The value of the attribute.\n\nStringValue (string) --A string, such as 'department'.\n\nStringListValue (list) --A list of strings.\n\n(string) --\n\n\nLongValue (integer) --A long integer value.\n\nDateValue (datetime) --A date value expressed as seconds from the Unix epoch.\n\n\n\n\n\nGreaterThan (dict) --Performs a greater than operation on two document attributes. Use with a document attribute of type Integer or Long .\n\nKey (string) -- [REQUIRED]The identifier for the attribute.\n\nValue (dict) -- [REQUIRED]The value of the attribute.\n\nStringValue (string) --A string, such as 'department'.\n\nStringListValue (list) --A list of strings.\n\n(string) --\n\n\nLongValue (integer) --A long integer value.\n\nDateValue (datetime) --A date value expressed as seconds from the Unix epoch.\n\n\n\n\n\nGreaterThanOrEquals (dict) --Performs a greater or equals than operation on two document attributes. Use with a document attribute of type Integer or Long .\n\nKey (string) -- [REQUIRED]The identifier for the attribute.\n\nValue (dict) -- [REQUIRED]The value of the attribute.\n\nStringValue (string) --A string, such as 'department'.\n\nStringListValue (list) --A list of strings.\n\n(string) --\n\n\nLongValue (integer) --A long integer value.\n\nDateValue (datetime) --A date value expressed as seconds from the Unix epoch.\n\n\n\n\n\nLessThan (dict) --Performs a less than operation on two document attributes. Use with a document attribute of type Integer or Long .\n\nKey (string) -- [REQUIRED]The identifier for the attribute.\n\nValue (dict) -- [REQUIRED]The value of the attribute.\n\nStringValue (string) --A string, such as 'department'.\n\nStringListValue (list) --A list of strings.\n\n(string) --\n\n\nLongValue (integer) --A long integer value.\n\nDateValue (datetime) --A date value expressed as seconds from the Unix epoch.\n\n\n\n\n\nLessThanOrEquals (dict) --Performs a less than or equals operation on two document attributes. Use with a document attribute of type Integer or Long .\n\nKey (string) -- [REQUIRED]The identifier for the attribute.\n\nValue (dict) -- [REQUIRED]The value of the attribute.\n\nStringValue (string) --A string, such as 'department'.\n\nStringListValue (list) --A list of strings.\n\n(string) --\n\n\nLongValue (integer) --A long integer value.\n\nDateValue (datetime) --A date value expressed as seconds from the Unix epoch.\n\n\n\n\n\n\n

    :type Facets: list
    :param Facets: An array of documents attributes. Amazon Kendra returns a count for each attribute key specified. You can use this information to help narrow the search for your user.\n\n(dict) --Information about a document attribute\n\nDocumentAttributeKey (string) --The unique key for the document attribute.\n\n\n\n\n

    :type RequestedDocumentAttributes: list
    :param RequestedDocumentAttributes: An array of document attributes to include in the response. No other document attributes are included in the response. By default all document attributes are included in the response.\n\n(string) --\n\n

    :type QueryResultTypeFilter: string
    :param QueryResultTypeFilter: Sets the type of query. Only results for the specified query type are returned.

    :type PageNumber: integer
    :param PageNumber: Query results are returned in pages the size of the PageSize parameter. By default, Amazon Kendra returns the first page of results. Use this parameter to get result pages after the first one.

    :type PageSize: integer
    :param PageSize: Sets the number of results that are returned in each page of results. The default page size is 10. The maximum number of results returned is 100. If you ask for more than 100 results, only 100 are returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'QueryId': 'string',
    'ResultItems': [
        {
            'Id': 'string',
            'Type': 'DOCUMENT'|'QUESTION_ANSWER'|'ANSWER',
            'AdditionalAttributes': [
                {
                    'Key': 'string',
                    'ValueType': 'TEXT_WITH_HIGHLIGHTS_VALUE',
                    'Value': {
                        'TextWithHighlightsValue': {
                            'Text': 'string',
                            'Highlights': [
                                {
                                    'BeginOffset': 123,
                                    'EndOffset': 123,
                                    'TopAnswer': True|False
                                },
                            ]
                        }
                    }
                },
            ],
            'DocumentId': 'string',
            'DocumentTitle': {
                'Text': 'string',
                'Highlights': [
                    {
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'TopAnswer': True|False
                    },
                ]
            },
            'DocumentExcerpt': {
                'Text': 'string',
                'Highlights': [
                    {
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'TopAnswer': True|False
                    },
                ]
            },
            'DocumentURI': 'string',
            'DocumentAttributes': [
                {
                    'Key': 'string',
                    'Value': {
                        'StringValue': 'string',
                        'StringListValue': [
                            'string',
                        ],
                        'LongValue': 123,
                        'DateValue': datetime(2015, 1, 1)
                    }
                },
            ]
        },
    ],
    'FacetResults': [
        {
            'DocumentAttributeKey': 'string',
            'DocumentAttributeValueCountPairs': [
                {
                    'DocumentAttributeValue': {
                        'StringValue': 'string',
                        'StringListValue': [
                            'string',
                        ],
                        'LongValue': 123,
                        'DateValue': datetime(2015, 1, 1)
                    },
                    'Count': 123
                },
            ]
        },
    ],
    'TotalNumberOfResults': 123
}


Response Structure

(dict) --

QueryId (string) --
The unique identifier for the search. You use QueryId to identify the search when using the feedback API.

ResultItems (list) --
The results of the search.

(dict) --
A single query result.
A query result contains information about a document returned by the query. This includes the original location of the document, a list of attributes assigned to the document, and relevant text from the document that satisfies the query.

Id (string) --
The unique identifier for the query result.

Type (string) --
The type of document.

AdditionalAttributes (list) --
One or more additional attribues associated with the query result.

(dict) --
An attribute returned from an index query.

Key (string) --
The key that identifies the attribute.

ValueType (string) --
The data type of the Value property.

Value (dict) --
An object that contains the attribute value.

TextWithHighlightsValue (dict) --
The text associated with the attribute and information about the highlight to apply to the text.

Text (string) --
The text to display to the user.

Highlights (list) --
The beginning and end of the text that should be highlighted.

(dict) --
Provides information that you can use to highlight a search result so that your users can quickly identify terms in the response.

BeginOffset (integer) --
The zero-based location in the response string where the highlight starts.

EndOffset (integer) --
The zero-based location in the response string where the highlight ends.

TopAnswer (boolean) --
Indicates whether the response is the best response. True if this is the best response; otherwise, false.













DocumentId (string) --
The unique identifier for the document.

DocumentTitle (dict) --
The title of the document. Contains the text of the title and information for highlighting the relevant terms in the title.

Text (string) --
The text to display to the user.

Highlights (list) --
The beginning and end of the text that should be highlighted.

(dict) --
Provides information that you can use to highlight a search result so that your users can quickly identify terms in the response.

BeginOffset (integer) --
The zero-based location in the response string where the highlight starts.

EndOffset (integer) --
The zero-based location in the response string where the highlight ends.

TopAnswer (boolean) --
Indicates whether the response is the best response. True if this is the best response; otherwise, false.







DocumentExcerpt (dict) --
An extract of the text in the document. Contains information about highlighting the relevant terms in the excerpt.

Text (string) --
The text to display to the user.

Highlights (list) --
The beginning and end of the text that should be highlighted.

(dict) --
Provides information that you can use to highlight a search result so that your users can quickly identify terms in the response.

BeginOffset (integer) --
The zero-based location in the response string where the highlight starts.

EndOffset (integer) --
The zero-based location in the response string where the highlight ends.

TopAnswer (boolean) --
Indicates whether the response is the best response. True if this is the best response; otherwise, false.







DocumentURI (string) --
The URI of the original location of the document.

DocumentAttributes (list) --
An array of document attributes for the document that the query result maps to. For example, the document author (Author) or the source URI (SourceUri) of the document.

(dict) --
A custom attribute value assigned to a document.

Key (string) --
The identifier for the attribute.

Value (dict) --
The value of the attribute.

StringValue (string) --
A string, such as "department".

StringListValue (list) --
A list of strings.

(string) --


LongValue (integer) --
A long integer value.

DateValue (datetime) --
A date value expressed as seconds from the Unix epoch.











FacetResults (list) --
Contains the facet results. A FacetResult contains the counts for each attribute key that was specified in the Facets input parameter.

(dict) --
The facet values for the documents in the response.

DocumentAttributeKey (string) --
The key for the facet values. This is the same as the DocumentAttributeKey provided in the query.

DocumentAttributeValueCountPairs (list) --
An array of key/value pairs, where the key is the value of the attribute and the count is the number of documents that share the key value.

(dict) --
Provides the count of documents that match a particular attribute when doing a faceted search.

DocumentAttributeValue (dict) --
The value of the attribute. For example, "HR."

StringValue (string) --
A string, such as "department".

StringListValue (list) --
A list of strings.

(string) --


LongValue (integer) --
A long integer value.

DateValue (datetime) --
A date value expressed as seconds from the Unix epoch.



Count (integer) --
The number of documents in the response that have the attribute value for the key.









TotalNumberOfResults (integer) --
The number of items returned by the search. Use this to determine when you have requested the last set of results.







Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ConflictException
kendra.Client.exceptions.ResourceNotFoundException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.ServiceQuotaExceededException
kendra.Client.exceptions.InternalServerException


    :return: {
        'QueryId': 'string',
        'ResultItems': [
            {
                'Id': 'string',
                'Type': 'DOCUMENT'|'QUESTION_ANSWER'|'ANSWER',
                'AdditionalAttributes': [
                    {
                        'Key': 'string',
                        'ValueType': 'TEXT_WITH_HIGHLIGHTS_VALUE',
                        'Value': {
                            'TextWithHighlightsValue': {
                                'Text': 'string',
                                'Highlights': [
                                    {
                                        'BeginOffset': 123,
                                        'EndOffset': 123,
                                        'TopAnswer': True|False
                                    },
                                ]
                            }
                        }
                    },
                ],
                'DocumentId': 'string',
                'DocumentTitle': {
                    'Text': 'string',
                    'Highlights': [
                        {
                            'BeginOffset': 123,
                            'EndOffset': 123,
                            'TopAnswer': True|False
                        },
                    ]
                },
                'DocumentExcerpt': {
                    'Text': 'string',
                    'Highlights': [
                        {
                            'BeginOffset': 123,
                            'EndOffset': 123,
                            'TopAnswer': True|False
                        },
                    ]
                },
                'DocumentURI': 'string',
                'DocumentAttributes': [
                    {
                        'Key': 'string',
                        'Value': {
                            'StringValue': 'string',
                            'StringListValue': [
                                'string',
                            ],
                            'LongValue': 123,
                            'DateValue': datetime(2015, 1, 1)
                        }
                    },
                ]
            },
        ],
        'FacetResults': [
            {
                'DocumentAttributeKey': 'string',
                'DocumentAttributeValueCountPairs': [
                    {
                        'DocumentAttributeValue': {
                            'StringValue': 'string',
                            'StringListValue': [
                                'string',
                            ],
                            'LongValue': 123,
                            'DateValue': datetime(2015, 1, 1)
                        },
                        'Count': 123
                    },
                ]
            },
        ],
        'TotalNumberOfResults': 123
    }
    
    
    :returns: 
    IndexId (string) -- [REQUIRED]
    The unique identifier of the index to search. The identifier is returned in the response from the operation.
    
    QueryText (string) -- [REQUIRED]
    The text to search for.
    
    AttributeFilter (dict) -- Enables filtered searches based on document attributes. You can only provide one attribute filter; however, the AndAllFilters , NotFilter , and OrAllFilters parameters contain a list of other filters.
    The AttributeFilter parameter enables you to create a set of filtering rules that a document must satisfy to be included in the query results.
    
    AndAllFilters (list) --Performs a logical AND operation on all supplied filters.
    
    (dict) --Provides filtering the query results based on document attributes.
    When you use the AndAllFilters or OrAllFilters , filters you can use 2 layers under the first attribute filter. For example, you can use:
    
    <AndAllFilters>
    
    <OrAllFilters>
    <EqualTo>
    
    If you use more than 2 layers, you receive a ValidationException exception with the message "AttributeFilter cannot have a depth of more than 2."
    
    
    
    OrAllFilters (list) --Performs a logical OR operation on all supplied filters.
    
    (dict) --Provides filtering the query results based on document attributes.
    When you use the AndAllFilters or OrAllFilters , filters you can use 2 layers under the first attribute filter. For example, you can use:
    
    <AndAllFilters>
    
    <OrAllFilters>
    <EqualTo>
    
    If you use more than 2 layers, you receive a ValidationException exception with the message "AttributeFilter cannot have a depth of more than 2."
    
    
    
    NotFilter (dict) --Performs a logical NOT operation on all supplied filters.
    
    EqualsTo (dict) --Performs an equals operation on two document attributes.
    
    Key (string) -- [REQUIRED]The identifier for the attribute.
    
    Value (dict) -- [REQUIRED]The value of the attribute.
    
    StringValue (string) --A string, such as "department".
    
    StringListValue (list) --A list of strings.
    
    (string) --
    
    
    LongValue (integer) --A long integer value.
    
    DateValue (datetime) --A date value expressed as seconds from the Unix epoch.
    
    
    
    
    
    ContainsAll (dict) --Returns true when a document contains all of the specified document attributes. This filter is only appicable to StringListValue metadata.
    
    Key (string) -- [REQUIRED]The identifier for the attribute.
    
    Value (dict) -- [REQUIRED]The value of the attribute.
    
    StringValue (string) --A string, such as "department".
    
    StringListValue (list) --A list of strings.
    
    (string) --
    
    
    LongValue (integer) --A long integer value.
    
    DateValue (datetime) --A date value expressed as seconds from the Unix epoch.
    
    
    
    
    
    ContainsAny (dict) --Returns true when a document contains any of the specified document attributes.This filter is only appicable to StringListValue metadata.
    
    Key (string) -- [REQUIRED]The identifier for the attribute.
    
    Value (dict) -- [REQUIRED]The value of the attribute.
    
    StringValue (string) --A string, such as "department".
    
    StringListValue (list) --A list of strings.
    
    (string) --
    
    
    LongValue (integer) --A long integer value.
    
    DateValue (datetime) --A date value expressed as seconds from the Unix epoch.
    
    
    
    
    
    GreaterThan (dict) --Performs a greater than operation on two document attributes. Use with a document attribute of type Integer or Long .
    
    Key (string) -- [REQUIRED]The identifier for the attribute.
    
    Value (dict) -- [REQUIRED]The value of the attribute.
    
    StringValue (string) --A string, such as "department".
    
    StringListValue (list) --A list of strings.
    
    (string) --
    
    
    LongValue (integer) --A long integer value.
    
    DateValue (datetime) --A date value expressed as seconds from the Unix epoch.
    
    
    
    
    
    GreaterThanOrEquals (dict) --Performs a greater or equals than operation on two document attributes. Use with a document attribute of type Integer or Long .
    
    Key (string) -- [REQUIRED]The identifier for the attribute.
    
    Value (dict) -- [REQUIRED]The value of the attribute.
    
    StringValue (string) --A string, such as "department".
    
    StringListValue (list) --A list of strings.
    
    (string) --
    
    
    LongValue (integer) --A long integer value.
    
    DateValue (datetime) --A date value expressed as seconds from the Unix epoch.
    
    
    
    
    
    LessThan (dict) --Performs a less than operation on two document attributes. Use with a document attribute of type Integer or Long .
    
    Key (string) -- [REQUIRED]The identifier for the attribute.
    
    Value (dict) -- [REQUIRED]The value of the attribute.
    
    StringValue (string) --A string, such as "department".
    
    StringListValue (list) --A list of strings.
    
    (string) --
    
    
    LongValue (integer) --A long integer value.
    
    DateValue (datetime) --A date value expressed as seconds from the Unix epoch.
    
    
    
    
    
    LessThanOrEquals (dict) --Performs a less than or equals operation on two document attributes. Use with a document attribute of type Integer or Long .
    
    Key (string) -- [REQUIRED]The identifier for the attribute.
    
    Value (dict) -- [REQUIRED]The value of the attribute.
    
    StringValue (string) --A string, such as "department".
    
    StringListValue (list) --A list of strings.
    
    (string) --
    
    
    LongValue (integer) --A long integer value.
    
    DateValue (datetime) --A date value expressed as seconds from the Unix epoch.
    
    
    
    
    
    
    
    Facets (list) -- An array of documents attributes. Amazon Kendra returns a count for each attribute key specified. You can use this information to help narrow the search for your user.
    
    (dict) --Information about a document attribute
    
    DocumentAttributeKey (string) --The unique key for the document attribute.
    
    
    
    
    
    RequestedDocumentAttributes (list) -- An array of document attributes to include in the response. No other document attributes are included in the response. By default all document attributes are included in the response.
    
    (string) --
    
    
    QueryResultTypeFilter (string) -- Sets the type of query. Only results for the specified query type are returned.
    PageNumber (integer) -- Query results are returned in pages the size of the PageSize parameter. By default, Amazon Kendra returns the first page of results. Use this parameter to get result pages after the first one.
    PageSize (integer) -- Sets the number of results that are returned in each page of results. The default page size is 10. The maximum number of results returned is 100. If you ask for more than 100 results, only 100 are returned.
    
    """
    pass

def start_data_source_sync_job(Id=None, IndexId=None):
    """
    Starts a synchronization job for a data source. If a synchronization job is already in progress, Amazon Kendra returns a ResourceInUseException exception.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_data_source_sync_job(
        Id='string',
        IndexId='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe identifier of the data source to synchronize.\n

    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe identifier of the index that contains the data source.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ExecutionId': 'string'
}


Response Structure

(dict) --

ExecutionId (string) --
Identifies a particular synchronization job.







Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ResourceNotFoundException
kendra.Client.exceptions.ResourceInUseException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.ConflictException
kendra.Client.exceptions.InternalServerException


    :return: {
        'ExecutionId': 'string'
    }
    
    
    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ResourceInUseException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.ConflictException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def stop_data_source_sync_job(Id=None, IndexId=None):
    """
    Stops a running synchronization job. You can\'t stop a scheduled synchronization job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_data_source_sync_job(
        Id='string',
        IndexId='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe identifier of the data source for which to stop the synchronization jobs.\n

    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe identifier of the index that contains the data source.\n

    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def submit_feedback(IndexId=None, QueryId=None, ClickFeedbackItems=None, RelevanceFeedbackItems=None):
    """
    Enables you to provide feedback to Amazon Kendra to improve the performance of the service.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.submit_feedback(
        IndexId='string',
        QueryId='string',
        ClickFeedbackItems=[
            {
                'ResultId': 'string',
                'ClickTime': datetime(2015, 1, 1)
            },
        ],
        RelevanceFeedbackItems=[
            {
                'ResultId': 'string',
                'RelevanceValue': 'RELEVANT'|'NOT_RELEVANT'
            },
        ]
    )
    
    
    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe identifier of the index that was queried.\n

    :type QueryId: string
    :param QueryId: [REQUIRED]\nThe identifier of the specific query for which you are submitting feedback. The query ID is returned in the response to the operation.\n

    :type ClickFeedbackItems: list
    :param ClickFeedbackItems: Tells Amazon Kendra that a particular search result link was chosen by the user.\n\n(dict) --Gathers information about when a particular result was clicked by a user. Your application uses the SubmitFeedback operation to provide click information.\n\nResultId (string) -- [REQUIRED]The unique identifier of the search result that was clicked.\n\nClickTime (datetime) -- [REQUIRED]The Unix timestamp of the date and time that the result was clicked.\n\n\n\n\n

    :type RelevanceFeedbackItems: list
    :param RelevanceFeedbackItems: Provides Amazon Kendra with relevant or not relevant feedback for whether a particular item was relevant to the search.\n\n(dict) --Provides feedback on how relevant a document is to a search. Your application uses the SubmitFeedback operation to provide relevance information.\n\nResultId (string) -- [REQUIRED]The unique identifier of the search result that the user provided relevance feedback for.\n\nRelevanceValue (string) -- [REQUIRED]Whether to document was relevant or not relevant to the search.\n\n\n\n\n

    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ResourceUnavailableException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def tag_resource(ResourceARN=None, Tags=None):
    """
    Adds the specified tag to the specified index, FAQ, or data source resource. If the tag already exists, the existing value is replaced with the new value.
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
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the index, FAQ, or data source to tag.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nA list of tag keys to add to the index, FAQ, or data source. If a tag already exists, the existing value is replaced with the new value.\n\n(dict) --A list of key/value pairs that identify an index, FAQ, or data source. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.\n\nKey (string) -- [REQUIRED]The key for the tag. Keys are not case sensitive and must be unique for the index, FAQ, or data source.\n\nValue (string) -- [REQUIRED]The value associated with the tag. The value may be an empty string but it can\'t be null.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ResourceUnavailableException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceARN=None, TagKeys=None):
    """
    Removes a tag from an index, FAQ, or a data source.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the index, FAQ, or data source to remove the tag from.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of tag keys to remove from the index, FAQ, or data source. If a tag key does not exist on the resource, it is ignored.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

kendra.Client.exceptions.ValidationException
kendra.Client.exceptions.ResourceUnavailableException
kendra.Client.exceptions.ThrottlingException
kendra.Client.exceptions.AccessDeniedException
kendra.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_data_source(Id=None, Name=None, IndexId=None, Configuration=None, Description=None, Schedule=None, RoleArn=None):
    """
    Updates an existing Amazon Kendra data source.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_data_source(
        Id='string',
        Name='string',
        IndexId='string',
        Configuration={
            'S3Configuration': {
                'BucketName': 'string',
                'InclusionPrefixes': [
                    'string',
                ],
                'ExclusionPatterns': [
                    'string',
                ],
                'DocumentsMetadataConfiguration': {
                    'S3Prefix': 'string'
                },
                'AccessControlListConfiguration': {
                    'KeyPath': 'string'
                }
            },
            'SharePointConfiguration': {
                'SharePointVersion': 'SHAREPOINT_ONLINE',
                'Urls': [
                    'string',
                ],
                'SecretArn': 'string',
                'CrawlAttachments': True|False,
                'UseChangeLog': True|False,
                'InclusionPatterns': [
                    'string',
                ],
                'ExclusionPatterns': [
                    'string',
                ],
                'VpcConfiguration': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'FieldMappings': [
                    {
                        'DataSourceFieldName': 'string',
                        'DateFieldFormat': 'string',
                        'IndexFieldName': 'string'
                    },
                ],
                'DocumentTitleFieldName': 'string'
            },
            'DatabaseConfiguration': {
                'DatabaseEngineType': 'RDS_AURORA_MYSQL'|'RDS_AURORA_POSTGRESQL'|'RDS_MYSQL'|'RDS_POSTGRESQL',
                'ConnectionConfiguration': {
                    'DatabaseHost': 'string',
                    'DatabasePort': 123,
                    'DatabaseName': 'string',
                    'TableName': 'string',
                    'SecretArn': 'string'
                },
                'VpcConfiguration': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'ColumnConfiguration': {
                    'DocumentIdColumnName': 'string',
                    'DocumentDataColumnName': 'string',
                    'DocumentTitleColumnName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ],
                    'ChangeDetectingColumns': [
                        'string',
                    ]
                },
                'AclConfiguration': {
                    'AllowedGroupsColumnName': 'string'
                }
            },
            'SalesforceConfiguration': {
                'ServerUrl': 'string',
                'SecretArn': 'string',
                'StandardObjectConfigurations': [
                    {
                        'Name': 'ACCOUNT'|'CAMPAIGN'|'CASE'|'CONTACT'|'CONTRACT'|'DOCUMENT'|'GROUP'|'IDEA'|'LEAD'|'OPPORTUNITY'|'PARTNER'|'PRICEBOOK'|'PRODUCT'|'PROFILE'|'SOLUTION'|'TASK'|'USER',
                        'DocumentDataFieldName': 'string',
                        'DocumentTitleFieldName': 'string',
                        'FieldMappings': [
                            {
                                'DataSourceFieldName': 'string',
                                'DateFieldFormat': 'string',
                                'IndexFieldName': 'string'
                            },
                        ]
                    },
                ],
                'KnowledgeArticleConfiguration': {
                    'IncludedStates': [
                        'DRAFT'|'PUBLISHED'|'ARCHIVED',
                    ],
                    'StandardKnowledgeArticleTypeConfiguration': {
                        'DocumentDataFieldName': 'string',
                        'DocumentTitleFieldName': 'string',
                        'FieldMappings': [
                            {
                                'DataSourceFieldName': 'string',
                                'DateFieldFormat': 'string',
                                'IndexFieldName': 'string'
                            },
                        ]
                    },
                    'CustomKnowledgeArticleTypeConfigurations': [
                        {
                            'Name': 'string',
                            'DocumentDataFieldName': 'string',
                            'DocumentTitleFieldName': 'string',
                            'FieldMappings': [
                                {
                                    'DataSourceFieldName': 'string',
                                    'DateFieldFormat': 'string',
                                    'IndexFieldName': 'string'
                                },
                            ]
                        },
                    ]
                },
                'ChatterFeedConfiguration': {
                    'DocumentDataFieldName': 'string',
                    'DocumentTitleFieldName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ],
                    'IncludeFilterTypes': [
                        'ACTIVE_USER'|'STANDARD_USER',
                    ]
                },
                'CrawlAttachments': True|False,
                'StandardObjectAttachmentConfiguration': {
                    'DocumentTitleFieldName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ]
                },
                'IncludeAttachmentFilePatterns': [
                    'string',
                ],
                'ExcludeAttachmentFilePatterns': [
                    'string',
                ]
            },
            'OneDriveConfiguration': {
                'TenantDomain': 'string',
                'SecretArn': 'string',
                'OneDriveUsers': {
                    'OneDriveUserList': [
                        'string',
                    ],
                    'OneDriveUserS3Path': {
                        'Bucket': 'string',
                        'Key': 'string'
                    }
                },
                'InclusionPatterns': [
                    'string',
                ],
                'ExclusionPatterns': [
                    'string',
                ],
                'FieldMappings': [
                    {
                        'DataSourceFieldName': 'string',
                        'DateFieldFormat': 'string',
                        'IndexFieldName': 'string'
                    },
                ]
            },
            'ServiceNowConfiguration': {
                'HostUrl': 'string',
                'SecretArn': 'string',
                'ServiceNowBuildVersion': 'LONDON'|'OTHERS',
                'KnowledgeArticleConfiguration': {
                    'CrawlAttachments': True|False,
                    'IncludeAttachmentFilePatterns': [
                        'string',
                    ],
                    'ExcludeAttachmentFilePatterns': [
                        'string',
                    ],
                    'DocumentDataFieldName': 'string',
                    'DocumentTitleFieldName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ]
                },
                'ServiceCatalogConfiguration': {
                    'CrawlAttachments': True|False,
                    'IncludeAttachmentFilePatterns': [
                        'string',
                    ],
                    'ExcludeAttachmentFilePatterns': [
                        'string',
                    ],
                    'DocumentDataFieldName': 'string',
                    'DocumentTitleFieldName': 'string',
                    'FieldMappings': [
                        {
                            'DataSourceFieldName': 'string',
                            'DateFieldFormat': 'string',
                            'IndexFieldName': 'string'
                        },
                    ]
                }
            }
        },
        Description='string',
        Schedule='string',
        RoleArn='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe unique identifier of the data source to update.\n

    :type Name: string
    :param Name: The name of the data source to update. The name of the data source can\'t be updated. To rename a data source you must delete the data source and re-create it.

    :type IndexId: string
    :param IndexId: [REQUIRED]\nThe identifier of the index that contains the data source to update.\n

    :type Configuration: dict
    :param Configuration: Configuration information for a Amazon Kendra data source.\n\nS3Configuration (dict) --Provides information to create a connector for a document repository in an Amazon S3 bucket.\n\nBucketName (string) -- [REQUIRED]The name of the bucket that contains the documents.\n\nInclusionPrefixes (list) --A list of S3 prefixes for the documents that should be included in the index.\n\n(string) --\n\n\nExclusionPatterns (list) --A list of glob patterns for documents that should not be indexed. If a document that matches an inclusion prefix also matches an exclusion pattern, the document is not indexed.\nFor more information about glob patterns, see glob (programming) in Wikipedia .\n\n(string) --\n\n\nDocumentsMetadataConfiguration (dict) --Document metadata files that contain information such as the document access control information, source URI, document author, and custom attributes. Each metadata file contains metadata about a single document.\n\nS3Prefix (string) --A prefix used to filter metadata configuration files in the AWS S3 bucket. The S3 bucket might contain multiple metadata files. Use S3Prefix to include only the desired metadata files.\n\n\n\nAccessControlListConfiguration (dict) --Provides the path to the S3 bucket that contains the user context filtering files for the data source.\n\nKeyPath (string) --Path to the AWS S3 bucket that contains the ACL files.\n\n\n\n\n\nSharePointConfiguration (dict) --Provides information necessary to create a connector for a Microsoft SharePoint site.\n\nSharePointVersion (string) -- [REQUIRED]The version of Microsoft SharePoint that you are using as a data source.\n\nUrls (list) -- [REQUIRED]The URLs of the Microsoft SharePoint site that contains the documents that should be indexed.\n\n(string) --\n\n\nSecretArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of credentials stored in AWS Secrets Manager. The credentials should be a user/password pair. For more information, see Using a Microsoft SharePoint Data Source . For more information about AWS Secrets Manager, see What Is AWS Secrets Manager in the AWS Secrets Manager user guide.\n\nCrawlAttachments (boolean) --\nTRUE to include attachments to documents stored in your Microsoft SharePoint site in the index; otherwise, FALSE .\n\nUseChangeLog (boolean) --Set to TRUE to use the Microsoft SharePoint change log to determine the documents that need to be updated in the index. Depending on the size of the SharePoint change log, it may take longer for Amazon Kendra to use the change log than it takes it to determine the changed documents using the Amazon Kendra document crawler.\n\nInclusionPatterns (list) --A list of regular expression patterns. Documents that match the patterns are included in the index. Documents that don\'t match the patterns are excluded from the index. If a document matches both an inclusion pattern and an exclusion pattern, the document is not included in the index.\nThe regex is applied to the display URL of the SharePoint document.\n\n(string) --\n\n\nExclusionPatterns (list) --A list of regulary expression patterns. Documents that match the patterns are excluded from the index. Documents that don\'t match the patterns are included in the index. If a document matches both an exclusion pattern and an inclusion pattern, the document is not included in the index.\nThe regex is applied to the display URL of the SharePoint document.\n\n(string) --\n\n\nVpcConfiguration (dict) --Provides information for connecting to an Amazon VPC.\n\nSubnetIds (list) -- [REQUIRED]A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.\n\n(string) --\n\n\nSecurityGroupIds (list) -- [REQUIRED]A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.\n\n(string) --\n\n\n\n\nFieldMappings (list) --A list of DataSourceToIndexFieldMapping objects that map Microsoft SharePoint attributes to custom fields in the Amazon Kendra index. You must first create the index fields using the operation before you map SharePoint attributes. For more information, see Mapping Data Source Fields .\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\nDocumentTitleFieldName (string) --The Microsoft SharePoint attribute field that contains the title of the document.\n\n\n\nDatabaseConfiguration (dict) --Provides information necessary to create a connector for a database.\n\nDatabaseEngineType (string) -- [REQUIRED]The type of database engine that runs the database.\n\nConnectionConfiguration (dict) -- [REQUIRED]The information necessary to connect to a database.\n\nDatabaseHost (string) -- [REQUIRED]The name of the host for the database. Can be either a string (host.subdomain.domain.tld) or an IPv4 or IPv6 address.\n\nDatabasePort (integer) -- [REQUIRED]The port that the database uses for connections.\n\nDatabaseName (string) -- [REQUIRED]The name of the database containing the document data.\n\nTableName (string) -- [REQUIRED]The name of the table that contains the document data.\n\nSecretArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of credentials stored in AWS Secrets Manager. The credentials should be a user/password pair. For more information, see Using a Database Data Source . For more information about AWS Secrets Manager, see What Is AWS Secrets Manager in the AWS Secrets Manager user guide.\n\n\n\nVpcConfiguration (dict) --Provides information for connecting to an Amazon VPC.\n\nSubnetIds (list) -- [REQUIRED]A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.\n\n(string) --\n\n\nSecurityGroupIds (list) -- [REQUIRED]A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.\n\n(string) --\n\n\n\n\nColumnConfiguration (dict) -- [REQUIRED]Information about where the index should get the document information from the database.\n\nDocumentIdColumnName (string) -- [REQUIRED]The column that provides the document\'s unique identifier.\n\nDocumentDataColumnName (string) -- [REQUIRED]The column that contains the contents of the document.\n\nDocumentTitleColumnName (string) --The column that contains the title of the document.\n\nFieldMappings (list) --An array of objects that map database column names to the corresponding fields in an index. You must first create the fields in the index using the UpdateIndex operation.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\nChangeDetectingColumns (list) -- [REQUIRED]One to five columns that indicate when a document in the database has changed.\n\n(string) --\n\n\n\n\nAclConfiguration (dict) --Information about the database column that provides information for user context filtering.\n\nAllowedGroupsColumnName (string) -- [REQUIRED]A list of groups, separated by semi-colons, that filters a query response based on user context. The document is only returned to users that are in one of the groups specified in the UserContext field of the Query operation.\n\n\n\n\n\nSalesforceConfiguration (dict) --Provides configuration information for data sources that connect to a Salesforce site.\n\nServerUrl (string) -- [REQUIRED]The instance URL for the Salesforce site that you want to index.\n\nSecretArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the key/value pairs required to connect to your Salesforce instance. The secret must contain a JSON structure with the following keys:\n\nauthenticationUrl - The OAUTH endpoint that Amazon Kendra connects to get an OAUTH token.\nconsumerKey - The application public key generated when you created your Salesforce application.\nconsumerSecret - The application private key generated when you created your Salesforce application.\npassword - The password associated with the user logging in to the Salesforce instance.\nsecurityToken - The token associated with the user account logging in to the Salesforce instance.\nusername - The user name of the user logging in to the Salesforce instance.\n\n\nStandardObjectConfigurations (list) --Specifies the Salesforce standard objects that Amazon Kendra indexes.\n\n(dict) --Specifies confguration information for indexing a single standard object.\n\nName (string) -- [REQUIRED]The name of the standard object.\n\nDocumentDataFieldName (string) -- [REQUIRED]The name of the field in the standard object table that contains the document contents.\n\nDocumentTitleFieldName (string) --The name of the field in the standard object table that contains the document titleB.\n\nFieldMappings (list) --One or more objects that map fields in the standard object to Amazon Kendra index fields. The index field must exist before you can map a Salesforce field to it.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\n\n\n\n\nKnowledgeArticleConfiguration (dict) --Specifies configuration information for the knowlege article types that Amazon Kendra indexes. Amazon Kendra indexes standard knowledge articles and the standard fields of knowledge articles, or the custom fields of custom knowledge articles, but not both.\n\nIncludedStates (list) -- [REQUIRED]Specifies the document states that should be included when Amazon Kendra indexes knowledge articles. You must specify at least one state.\n\n(string) --\n\n\nStandardKnowledgeArticleTypeConfiguration (dict) --Provides configuration information for standard Salesforce knowledge articles.\n\nDocumentDataFieldName (string) -- [REQUIRED]The name of the field that contains the document data to index.\n\nDocumentTitleFieldName (string) --The name of the field that contains the document title.\n\nFieldMappings (list) --One or more objects that map fields in the knowledge article to Amazon Kendra index fields. The index field must exist before you can map a Salesforce field to it.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\n\n\nCustomKnowledgeArticleTypeConfigurations (list) --Provides configuration information for custom Salesforce knowledge articles.\n\n(dict) --Provides configuration information for indexing Salesforce custom articles.\n\nName (string) -- [REQUIRED]The name of the configuration.\n\nDocumentDataFieldName (string) -- [REQUIRED]The name of the field in the custom knowledge article that contains the document data to index.\n\nDocumentTitleFieldName (string) --The name of the field in the custom knowledge article that contains the document title.\n\nFieldMappings (list) --One or more objects that map fields in the custom knowledge article to fields in the Amazon Kendra index.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\n\n\n\n\n\n\nChatterFeedConfiguration (dict) --Specifies configuration information for Salesforce chatter feeds.\n\nDocumentDataFieldName (string) -- [REQUIRED]The name of the column in the Salesforce FeedItem table that contains the content to index. Typically this is the Body column.\n\nDocumentTitleFieldName (string) --The name of the column in the Salesforce FeedItem table that contains the title of the document. This is typically the Title collumn.\n\nFieldMappings (list) --Maps fields from a Salesforce chatter feed into Amazon Kendra index fields.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\nIncludeFilterTypes (list) --Filters the documents in the feed based on status of the user. When you specify ACTIVE_USERS only documents from users who have an active account are indexed. When you specify STANDARD_USER only documents for Salesforce standard users are documented. You can specify both.\n\n(string) --\n\n\n\n\nCrawlAttachments (boolean) --Indicates whether Amazon Kendra should index attachments to Salesforce objects.\n\nStandardObjectAttachmentConfiguration (dict) --Provides configuration information for processing attachments to Salesforce standard objects.\n\nDocumentTitleFieldName (string) --The name of the field used for the document title.\n\nFieldMappings (list) --One or more objects that map fields in attachments to Amazon Kendra index fields.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\n\n\nIncludeAttachmentFilePatterns (list) --A list of regular expression patterns. Documents that match the patterns are included in the index. Documents that don\'t match the patterns are excluded from the index. If a document matches both an inclusion pattern and an exclusion pattern, the document is not included in the index.\nThe regex is applied to the name of the attached file.\n\n(string) --\n\n\nExcludeAttachmentFilePatterns (list) --A list of regular expression patterns. Documents that match the patterns are excluded from the index. Documents that don\'t match the patterns are included in the index. If a document matches both an exclusion pattern and an inclusion pattern, the document is not included in the index.\nThe regex is applied to the name of the attached file.\n\n(string) --\n\n\n\n\nOneDriveConfiguration (dict) --Provided configuration for data sources that connect to Microsoft OneDrive.\n\nTenantDomain (string) -- [REQUIRED]Tha Azure Active Directory domain of the organization.\n\nSecretArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the user name and password to connect to OneDrive. The user namd should be the application ID for the OneDrive application, and the password is the application key for the OneDrive application.\n\nOneDriveUsers (dict) -- [REQUIRED]A list of user accounts whose documents should be indexed.\n\nOneDriveUserList (list) --A list of users whose documents should be indexed. Specify the user names in email format, for example, username@tenantdomain . If you need to index the documents of more than 100 users, use the OneDriveUserS3Path field to specify the location of a file containing a list of users.\n\n(string) --\n\n\nOneDriveUserS3Path (dict) --The S3 bucket location of a file containing a list of users whose documents should be indexed.\n\nBucket (string) -- [REQUIRED]The name of the S3 bucket that contains the file.\n\nKey (string) -- [REQUIRED]The name of the file.\n\n\n\n\n\nInclusionPatterns (list) --A list of regular expression patterns. Documents that match the pattern are included in the index. Documents that don\'t match the pattern are excluded from the index. If a document matches both an inclusion pattern and an exclusion pattern, the document is not included in the index.\nThe exclusion pattern is applied to the file name.\n\n(string) --\n\n\nExclusionPatterns (list) --List of regular expressions applied to documents. Items that match the exclusion pattern are not indexed. If you provide both an inclusion pattern and an exclusion pattern, any item that matches the exclusion pattern isn\'t indexed.\nThe exclusion pattern is applied to the file name.\n\n(string) --\n\n\nFieldMappings (list) --A list of DataSourceToIndexFieldMapping objects that map Microsoft OneDrive fields to custom fields in the Amazon Kendra index. You must first create the index fields before you map OneDrive fields.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\n\n\nServiceNowConfiguration (dict) --Provides configuration for data sources that connect to ServiceNow instances.\n\nHostUrl (string) -- [REQUIRED]The ServiceNow instance that the data source connects to. The host endpoint should look like the following: {instance}.service-now.com.\n\nSecretArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS Secret Manager secret that contains the user name and password required to connect to the ServiceNow instance.\n\nServiceNowBuildVersion (string) -- [REQUIRED]The identifier of the release that the ServiceNow host is running. If the host is not running the LONDON release, use OTHERS .\n\nKnowledgeArticleConfiguration (dict) --Provides configuration information for crawling knowledge articles in the ServiceNow site.\n\nCrawlAttachments (boolean) --Indicates whether Amazon Kendra should index attachments to knowledge articles.\n\nIncludeAttachmentFilePatterns (list) --List of regular expressions applied to knowledge articles. Items that don\'t match the inclusion pattern are not indexed. The regex is applied to the field specified in the PatternTargetField .\n\n(string) --\n\n\nExcludeAttachmentFilePatterns (list) --List of regular expressions applied to knowledge articles. Items that don\'t match the inclusion pattern are not indexed. The regex is applied to the field specified in the PatternTargetField\n\n(string) --\n\n\nDocumentDataFieldName (string) -- [REQUIRED]The name of the ServiceNow field that is mapped to the index document contents field in the Amazon Kendra index.\n\nDocumentTitleFieldName (string) --The name of the ServiceNow field that is mapped to the index document title field.\n\nFieldMappings (list) --Mapping between ServiceNow fields and Amazon Kendra index fields. You must create the index field before you map the field.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\n\n\nServiceCatalogConfiguration (dict) --Provides configuration information for crawling service catalogs in the ServiceNow site.\n\nCrawlAttachments (boolean) --Indicates whether Amazon Kendra should crawl attachments to the service catalog items.\n\nIncludeAttachmentFilePatterns (list) --Determines the types of file attachments that are included in the index.\n\n(string) --\n\n\nExcludeAttachmentFilePatterns (list) --Determines the types of file attachments that are excluded from the index.\n\n(string) --\n\n\nDocumentDataFieldName (string) -- [REQUIRED]The name of the ServiceNow field that is mapped to the index document contents field in the Amazon Kendra index.\n\nDocumentTitleFieldName (string) --The name of the ServiceNow field that is mapped to the index document title field.\n\nFieldMappings (list) --Mapping between ServiceNow fields and Amazon Kendra index fields. You must create the index field before you map the field.\n\n(dict) --Maps a column or attribute in the data source to an index field. You must first create the fields in the index using the UpdateIndex operation.\n\nDataSourceFieldName (string) -- [REQUIRED]The name of the column or attribute in the data source.\n\nDateFieldFormat (string) --The type of data stored in the column or attribute.\n\nIndexFieldName (string) -- [REQUIRED]The name of the field in the index.\n\n\n\n\n\n\n\n\n\n\n

    :type Description: string
    :param Description: The new description for the data source.

    :type Schedule: string
    :param Schedule: The new update schedule for the data source.

    :type RoleArn: string
    :param RoleArn: The Amazon Resource Name (ARN) of the new role to use when the data source is accessing resources on your behalf.

    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ConflictException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

def update_index(Id=None, Name=None, RoleArn=None, Description=None, DocumentMetadataConfigurationUpdates=None, CapacityUnits=None):
    """
    Updates an existing Amazon Kendra index.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_index(
        Id='string',
        Name='string',
        RoleArn='string',
        Description='string',
        DocumentMetadataConfigurationUpdates=[
            {
                'Name': 'string',
                'Type': 'STRING_VALUE'|'STRING_LIST_VALUE'|'LONG_VALUE'|'DATE_VALUE',
                'Relevance': {
                    'Freshness': True|False,
                    'Importance': 123,
                    'Duration': 'string',
                    'RankOrder': 'ASCENDING'|'DESCENDING',
                    'ValueImportanceMap': {
                        'string': 123
                    }
                },
                'Search': {
                    'Facetable': True|False,
                    'Searchable': True|False,
                    'Displayable': True|False
                }
            },
        ],
        CapacityUnits={
            'StorageCapacityUnits': 123,
            'QueryCapacityUnits': 123
        }
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe identifier of the index to update.\n

    :type Name: string
    :param Name: The name of the index to update.

    :type RoleArn: string
    :param RoleArn: A new IAM role that gives Amazon Kendra permission to access your Amazon CloudWatch logs.

    :type Description: string
    :param Description: A new description for the index.

    :type DocumentMetadataConfigurationUpdates: list
    :param DocumentMetadataConfigurationUpdates: The document metadata to update.\n\n(dict) --Specifies the properties of a custom index field.\n\nName (string) -- [REQUIRED]The name of the index field.\n\nType (string) -- [REQUIRED]The data type of the index field.\n\nRelevance (dict) --Provides manual tuning parameters to determine how the field affects the search results.\n\nFreshness (boolean) --Indicates that this field determines how 'fresh' a document is. For example, if document 1 was created on November 5, and document 2 was created on October 31, document 1 is 'fresher' than document 2. You can only set the Freshness field on one DATE type field. Only applies to DATE fields.\n\nImportance (integer) --The relative importance of the field in the search. Larger numbers provide more of a boost than smaller numbers.\n\nDuration (string) --Specifies the time period that the boost applies to. For example, to make the boost apply to documents with the field value within the last month, you would use '2628000s'. Once the field value is beyond the specified range, the effect of the boost drops off. The higher the importance, the faster the effect drops off. If you don\'t specify a value, the default is 3 months. The value of the field is a numeric string followed by the character 's', for example '86400s' for one day, or '604800s' for one week.\nOnly applies to DATE fields.\n\nRankOrder (string) --Determines how values should be interpreted.\nWhen the RankOrder field is ASCENDING , higher numbers are better. For example, a document with a rating score of 10 is higher ranking than a document with a rating score of 1.\nWhen the RankOrder field is DESCENDING , lower numbers are better. For example, in a task tracking application, a priority 1 task is more important than a priority 5 task.\nOnly applies to LONG and DOUBLE fields.\n\nValueImportanceMap (dict) --A list of values that should be given a different boost when they appear in the result list. For example, if you are boosting a field called 'department,' query terms that match the department field are boosted in the result. However, you can add entries from the department field to boost documents with those values higher.\nFor example, you can add entries to the map with names of departments. If you add 'HR',5 and 'Legal',3 those departments are given special attention when they appear in the metadata of a document. When those terms appear they are given the specified importance instead of the regular importance for the boost.\n\n(string) --\n(integer) --\n\n\n\n\n\n\nSearch (dict) --Provides information about how the field is used during a search.\n\nFacetable (boolean) --Indicates that the field can be used to create search facets, a count of results for each value in the field. The default is false .\n\nSearchable (boolean) --Determines whether the field is used in the search. If the Searchable field is true , you can use relevance tuning to manually tune how Amazon Kendra weights the field in the search. The default is true for string fields and false for number and date fields.\n\nDisplayable (boolean) --Determines whether the field is returned in the query response. The default is true .\n\n\n\n\n\n\n

    :type CapacityUnits: dict
    :param CapacityUnits: Sets the number of addtional storage and query capacity units that should be used by the index. You can change the capacity of the index up to 5 times per day.\nIf you are using extra storage units, you can\'t reduce the storage capacity below that required to meet the storage needs for your index.\n\nStorageCapacityUnits (integer) -- [REQUIRED]The amount of extra storage capacity for an index. Each capacity unit provides 150 Gb of storage space or 500,000 documents, whichever is reached first.\n\nQueryCapacityUnits (integer) -- [REQUIRED]The amount of extra query capacity for an index. Each capacity unit provides 0.5 queries per second and 40,000 queries per day.\n\n\n

    :returns: 
    kendra.Client.exceptions.ValidationException
    kendra.Client.exceptions.ConflictException
    kendra.Client.exceptions.ResourceNotFoundException
    kendra.Client.exceptions.ThrottlingException
    kendra.Client.exceptions.AccessDeniedException
    kendra.Client.exceptions.ServiceQuotaExceededException
    kendra.Client.exceptions.InternalServerException
    
    """
    pass

