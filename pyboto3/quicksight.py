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

def cancel_ingestion(AwsAccountId=None, DataSetId=None, IngestionId=None):
    """
    Cancels an ongoing ingestion of data into SPICE.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_ingestion(
        AwsAccountId='string',
        DataSetId='string',
        IngestionId='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe ID of the dataset used in the ingestion.\n

    :type IngestionId: string
    :param IngestionId: [REQUIRED]\nAn ID for the ingestion.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'IngestionId': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

Arn (string) --
The Amazon Resource Name (ARN) for the data ingestion.

IngestionId (string) --
An ID for the ingestion.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Arn': 'string',
        'IngestionId': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def create_dashboard(AwsAccountId=None, DashboardId=None, Name=None, Parameters=None, Permissions=None, SourceEntity=None, Tags=None, VersionDescription=None, DashboardPublishOptions=None):
    """
    Creates a dashboard from a template. To first create a template, see the CreateTemplate API operation.
    A dashboard is an entity in QuickSight that identifies QuickSight reports, created from analyses. You can share QuickSight dashboards. With the right permissions, you can create scheduled email reports from them. The CreateDashboard , DescribeDashboard , and ListDashboardsByUser API operations act on the dashboard entity. If you have the correct permissions, you can create a dashboard from a template that exists in a different AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_dashboard(
        AwsAccountId='string',
        DashboardId='string',
        Name='string',
        Parameters={
            'StringParameters': [
                {
                    'Name': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            'IntegerParameters': [
                {
                    'Name': 'string',
                    'Values': [
                        123,
                    ]
                },
            ],
            'DecimalParameters': [
                {
                    'Name': 'string',
                    'Values': [
                        123.0,
                    ]
                },
            ],
            'DateTimeParameters': [
                {
                    'Name': 'string',
                    'Values': [
                        datetime(2015, 1, 1),
                    ]
                },
            ]
        },
        Permissions=[
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ],
        SourceEntity={
            'SourceTemplate': {
                'DataSetReferences': [
                    {
                        'DataSetPlaceholder': 'string',
                        'DataSetArn': 'string'
                    },
                ],
                'Arn': 'string'
            }
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        VersionDescription='string',
        DashboardPublishOptions={
            'AdHocFilteringOption': {
                'AvailabilityStatus': 'ENABLED'|'DISABLED'
            },
            'ExportToCSVOption': {
                'AvailabilityStatus': 'ENABLED'|'DISABLED'
            },
            'SheetControlsOption': {
                'VisibilityState': 'EXPANDED'|'COLLAPSED'
            }
        }
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account where you want to create the dashboard.\n

    :type DashboardId: string
    :param DashboardId: [REQUIRED]\nThe ID for the dashboard, also added to the IAM policy.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe display name of the dashboard.\n

    :type Parameters: dict
    :param Parameters: A structure that contains the parameters of the dashboard. These are parameter overrides for a dashboard. A dashboard can have any type of parameters, and some parameters might accept multiple values. You can use the dashboard permissions structure described following to override two string parameters that accept multiple values.\n\nStringParameters (list) --String parameters.\n\n(dict) --String parameter.\n\nName (string) -- [REQUIRED]A display name for the dataset.\n\nValues (list) -- [REQUIRED]Values.\n\n(string) --\n\n\n\n\n\n\nIntegerParameters (list) --Integer parameters.\n\n(dict) --Integer parameter.\n\nName (string) -- [REQUIRED]A display name for the dataset.\n\nValues (list) -- [REQUIRED]Values.\n\n(integer) --\n\n\n\n\n\n\nDecimalParameters (list) --Decimal parameters.\n\n(dict) --Decimal parameter.\n\nName (string) -- [REQUIRED]A display name for the dataset.\n\nValues (list) -- [REQUIRED]Values.\n\n(float) --\n\n\n\n\n\n\nDateTimeParameters (list) --DateTime parameters.\n\n(dict) --Date time parameter.\n\nName (string) -- [REQUIRED]A display name for the dataset.\n\nValues (list) -- [REQUIRED]Values.\n\n(datetime) --\n\n\n\n\n\n\n\n

    :type Permissions: list
    :param Permissions: A structure that contains the permissions of the dashboard. You can use this structure for granting permissions with principal and action information.\n\n(dict) --Permission for the resource.\n\nPrincipal (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .\n\nActions (list) -- [REQUIRED]The action to grant or revoke permissions on, for example 'quicksight:DescribeDashboard' .\n\n(string) --\n\n\n\n\n\n

    :type SourceEntity: dict
    :param SourceEntity: [REQUIRED]\nThe source entity from which the dashboard is created. The source entity accepts the Amazon Resource Name (ARN) of the source template or analysis and also references the replacement datasets for the placeholders set when creating the template. The replacement datasets need to follow the same schema as the datasets for which placeholders were created when creating the template.\nIf you are creating a dashboard from a source entity in a different AWS account, use the ARN of the source template.\n\nSourceTemplate (dict) --Source template.\n\nDataSetReferences (list) -- [REQUIRED]Dataset references.\n\n(dict) --Dataset reference.\n\nDataSetPlaceholder (string) -- [REQUIRED]Dataset placeholder.\n\nDataSetArn (string) -- [REQUIRED]Dataset Amazon Resource Name (ARN).\n\n\n\n\n\nArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the resource.\n\n\n\n\n

    :type Tags: list
    :param Tags: Contains a map of the key-value pairs for the resource tag or tags assigned to the dashboard.\n\n(dict) --The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.\n\nKey (string) -- [REQUIRED]Tag key.\n\nValue (string) -- [REQUIRED]Tag value.\n\n\n\n\n

    :type VersionDescription: string
    :param VersionDescription: A description for the first version of the dashboard being created.

    :type DashboardPublishOptions: dict
    :param DashboardPublishOptions: Options for publishing the dashboard when you create it:\n\nAvailabilityStatus for AdHocFilteringOption - This status can be either ENABLED or DISABLED . When this is set to DISABLED , QuickSight disables the left filter pane on the published dashboard, which can be used for ad hoc (one-time) filtering. This option is ENABLED by default.\nAvailabilityStatus for ExportToCSVOption - This status can be either ENABLED or DISABLED . The visual option to export data to .csv format isn\'t enabled when this is set to DISABLED . This option is ENABLED by default.\nVisibilityState for SheetControlsOption - This visibility state can be either COLLAPSED or EXPANDED . The sheet controls pane is collapsed by default when set to true. This option is COLLAPSED by default.\n\n\nAdHocFilteringOption (dict) --Ad hoc (one-time) filtering option.\n\nAvailabilityStatus (string) --Availability status.\n\n\n\nExportToCSVOption (dict) --Export to .csv option.\n\nAvailabilityStatus (string) --Availability status.\n\n\n\nSheetControlsOption (dict) --Sheet controls option.\n\nVisibilityState (string) --Visibility state.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'VersionArn': 'string',
    'DashboardId': 'string',
    'CreationStatus': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

Arn (string) --
The Amazon Resource Name (ARN) of the dashboard.

VersionArn (string) --
The ARN of the dashboard, including the version number of the first version that is created.

DashboardId (string) --
The ID for the dashboard.

CreationStatus (string) --
The status of the dashboard creation request.

Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Arn': 'string',
        'VersionArn': 'string',
        'DashboardId': 'string',
        'CreationStatus': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def create_data_set(AwsAccountId=None, DataSetId=None, Name=None, PhysicalTableMap=None, LogicalTableMap=None, ImportMode=None, ColumnGroups=None, Permissions=None, RowLevelPermissionDataSet=None, Tags=None):
    """
    Creates a dataset.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_data_set(
        AwsAccountId='string',
        DataSetId='string',
        Name='string',
        PhysicalTableMap={
            'string': {
                'RelationalTable': {
                    'DataSourceArn': 'string',
                    'Schema': 'string',
                    'Name': 'string',
                    'InputColumns': [
                        {
                            'Name': 'string',
                            'Type': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME'|'BIT'|'BOOLEAN'|'JSON'
                        },
                    ]
                },
                'CustomSql': {
                    'DataSourceArn': 'string',
                    'Name': 'string',
                    'SqlQuery': 'string',
                    'Columns': [
                        {
                            'Name': 'string',
                            'Type': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME'|'BIT'|'BOOLEAN'|'JSON'
                        },
                    ]
                },
                'S3Source': {
                    'DataSourceArn': 'string',
                    'UploadSettings': {
                        'Format': 'CSV'|'TSV'|'CLF'|'ELF'|'XLSX'|'JSON',
                        'StartFromRow': 123,
                        'ContainsHeader': True|False,
                        'TextQualifier': 'DOUBLE_QUOTE'|'SINGLE_QUOTE',
                        'Delimiter': 'string'
                    },
                    'InputColumns': [
                        {
                            'Name': 'string',
                            'Type': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME'|'BIT'|'BOOLEAN'|'JSON'
                        },
                    ]
                }
            }
        },
        LogicalTableMap={
            'string': {
                'Alias': 'string',
                'DataTransforms': [
                    {
                        'ProjectOperation': {
                            'ProjectedColumns': [
                                'string',
                            ]
                        },
                        'FilterOperation': {
                            'ConditionExpression': 'string'
                        },
                        'CreateColumnsOperation': {
                            'Columns': [
                                {
                                    'ColumnName': 'string',
                                    'ColumnId': 'string',
                                    'Expression': 'string'
                                },
                            ]
                        },
                        'RenameColumnOperation': {
                            'ColumnName': 'string',
                            'NewColumnName': 'string'
                        },
                        'CastColumnTypeOperation': {
                            'ColumnName': 'string',
                            'NewColumnType': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME',
                            'Format': 'string'
                        },
                        'TagColumnOperation': {
                            'ColumnName': 'string',
                            'Tags': [
                                {
                                    'ColumnGeographicRole': 'COUNTRY'|'STATE'|'COUNTY'|'CITY'|'POSTCODE'|'LONGITUDE'|'LATITUDE'
                                },
                            ]
                        }
                    },
                ],
                'Source': {
                    'JoinInstruction': {
                        'LeftOperand': 'string',
                        'RightOperand': 'string',
                        'Type': 'INNER'|'OUTER'|'LEFT'|'RIGHT',
                        'OnClause': 'string'
                    },
                    'PhysicalTableId': 'string'
                }
            }
        },
        ImportMode='SPICE'|'DIRECT_QUERY',
        ColumnGroups=[
            {
                'GeoSpatialColumnGroup': {
                    'Name': 'string',
                    'CountryCode': 'US',
                    'Columns': [
                        'string',
                    ]
                }
            },
        ],
        Permissions=[
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ],
        RowLevelPermissionDataSet={
            'Arn': 'string',
            'PermissionPolicy': 'GRANT_ACCESS'|'DENY_ACCESS'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nAn ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe display name for the dataset.\n

    :type PhysicalTableMap: dict
    :param PhysicalTableMap: [REQUIRED]\nDeclares the physical tables that are available in the underlying data sources.\n\n(string) --\n(dict) --A view of a data source that contains information about the shape of the data in the underlying source. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.\n\nRelationalTable (dict) --A physical table type for relational data sources.\n\nDataSourceArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) for the data source.\n\nSchema (string) --The schema name. This name applies to certain relational database engines.\n\nName (string) -- [REQUIRED]The name of the relational table.\n\nInputColumns (list) -- [REQUIRED]The column schema of the table.\n\n(dict) --Metadata for a column that is used as the input of a transform operation.\n\nName (string) -- [REQUIRED]The name of this column in the underlying data source.\n\nType (string) -- [REQUIRED]The data type of the column.\n\n\n\n\n\n\n\nCustomSql (dict) --A physical table type built from the results of the custom SQL query.\n\nDataSourceArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the data source.\n\nName (string) -- [REQUIRED]A display name for the SQL query result.\n\nSqlQuery (string) -- [REQUIRED]The SQL query.\n\nColumns (list) --The column schema from the SQL query result set.\n\n(dict) --Metadata for a column that is used as the input of a transform operation.\n\nName (string) -- [REQUIRED]The name of this column in the underlying data source.\n\nType (string) -- [REQUIRED]The data type of the column.\n\n\n\n\n\n\n\nS3Source (dict) --A physical table type for as S3 data source.\n\nDataSourceArn (string) -- [REQUIRED]The amazon Resource Name (ARN) for the data source.\n\nUploadSettings (dict) --Information about the format for the S3 source file or files.\n\nFormat (string) --File format.\n\nStartFromRow (integer) --A row number to start reading data from.\n\nContainsHeader (boolean) --Whether the file has a header row, or the files each have a header row.\n\nTextQualifier (string) --Text qualifier.\n\nDelimiter (string) --The delimiter between values in the file.\n\n\n\nInputColumns (list) -- [REQUIRED]A physical table type for as S3 data source.\n\n(dict) --Metadata for a column that is used as the input of a transform operation.\n\nName (string) -- [REQUIRED]The name of this column in the underlying data source.\n\nType (string) -- [REQUIRED]The data type of the column.\n\n\n\n\n\n\n\n\n\n\n\n\n

    :type LogicalTableMap: dict
    :param LogicalTableMap: Configures the combination and transformation of the data from the physical tables.\n\n(string) --\n(dict) --A logical table is a unit that joins and that data transformations operate on. A logical table has a source, which can be either a physical table or result of a join. When a logical table points to a physical table, the logical table acts as a mutable copy of that physical table through transform operations.\n\nAlias (string) -- [REQUIRED]A display name for the logical table.\n\nDataTransforms (list) --Transform operations that act on this logical table.\n\n(dict) --A data transformation on a logical table. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.\n\nProjectOperation (dict) --An operation that projects columns. Operations that come after a projection can only refer to projected columns.\n\nProjectedColumns (list) -- [REQUIRED]Projected columns.\n\n(string) --\n\n\n\n\nFilterOperation (dict) --An operation that filters rows based on some condition.\n\nConditionExpression (string) -- [REQUIRED]An expression that must evaluate to a Boolean value. Rows for which the expression evaluates to true are kept in the dataset.\n\n\n\nCreateColumnsOperation (dict) --An operation that creates calculated columns. Columns created in one such operation form a lexical closure.\n\nColumns (list) -- [REQUIRED]Calculated columns to create.\n\n(dict) --A calculated column for a dataset.\n\nColumnName (string) -- [REQUIRED]Column name.\n\nColumnId (string) -- [REQUIRED]A unique ID to identify a calculated column. During a dataset update, if the column ID of a calculated column matches that of an existing calculated column, Amazon QuickSight preserves the existing calculated column.\n\nExpression (string) -- [REQUIRED]An expression that defines the calculated column.\n\n\n\n\n\n\n\nRenameColumnOperation (dict) --An operation that renames a column.\n\nColumnName (string) -- [REQUIRED]The name of the column to be renamed.\n\nNewColumnName (string) -- [REQUIRED]The new name for the column.\n\n\n\nCastColumnTypeOperation (dict) --A transform operation that casts a column to a different type.\n\nColumnName (string) -- [REQUIRED]Column name.\n\nNewColumnType (string) -- [REQUIRED]New column data type.\n\nFormat (string) --When casting a column from string to datetime type, you can supply a string in a format supported by Amazon QuickSight to denote the source data format.\n\n\n\nTagColumnOperation (dict) --An operation that tags a column with additional information.\n\nColumnName (string) -- [REQUIRED]The column that this operation acts on.\n\nTags (list) -- [REQUIRED]The dataset column tag, currently only used for geospatial type tagging. .\n\nNote\nThis is not tags for the AWS tagging feature. .\n\n\n(dict) --A tag for a column in a TagColumnOperation structure. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.\n\nColumnGeographicRole (string) --A geospatial role for a column.\n\n\n\n\n\n\n\n\n\n\n\nSource (dict) -- [REQUIRED]Source of this logical table.\n\nJoinInstruction (dict) --Specifies the result of a join of two logical tables.\n\nLeftOperand (string) -- [REQUIRED]Left operand.\n\nRightOperand (string) -- [REQUIRED]Right operand.\n\nType (string) -- [REQUIRED]Type.\n\nOnClause (string) -- [REQUIRED]On Clause.\n\n\n\nPhysicalTableId (string) --Physical table ID.\n\n\n\n\n\n\n\n\n

    :type ImportMode: string
    :param ImportMode: [REQUIRED]\nIndicates whether you want to import the data into SPICE.\n

    :type ColumnGroups: list
    :param ColumnGroups: Groupings of columns that work together in certain QuickSight features. Currently, only geospatial hierarchy is supported.\n\n(dict) --Groupings of columns that work together in certain Amazon QuickSight features. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.\n\nGeoSpatialColumnGroup (dict) --Geospatial column group that denotes a hierarchy.\n\nName (string) -- [REQUIRED]A display name for the hierarchy.\n\nCountryCode (string) -- [REQUIRED]Country code.\n\nColumns (list) -- [REQUIRED]Columns in this hierarchy.\n\n(string) --\n\n\n\n\n\n\n\n

    :type Permissions: list
    :param Permissions: A list of resource permissions on the dataset.\n\n(dict) --Permission for the resource.\n\nPrincipal (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .\n\nActions (list) -- [REQUIRED]The action to grant or revoke permissions on, for example 'quicksight:DescribeDashboard' .\n\n(string) --\n\n\n\n\n\n

    :type RowLevelPermissionDataSet: dict
    :param RowLevelPermissionDataSet: The row-level security configuration for the data that you want to create.\n\nArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the permission dataset.\n\nPermissionPolicy (string) -- [REQUIRED]Permission policy.\n\n\n

    :type Tags: list
    :param Tags: Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.\n\n(dict) --The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.\n\nKey (string) -- [REQUIRED]Tag key.\n\nValue (string) -- [REQUIRED]Tag value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'DataSetId': 'string',
    'IngestionArn': 'string',
    'IngestionId': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

Arn (string) --
The Amazon Resource Name (ARN) of the dataset.

DataSetId (string) --
The ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.

IngestionArn (string) --
The ARN for the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.

IngestionId (string) --
The ID of the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.LimitExceededException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Arn': 'string',
        'DataSetId': 'string',
        'IngestionArn': 'string',
        'IngestionId': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.LimitExceededException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def create_data_source(AwsAccountId=None, DataSourceId=None, Name=None, Type=None, DataSourceParameters=None, Credentials=None, Permissions=None, VpcConnectionProperties=None, SslProperties=None, Tags=None):
    """
    Creates a data source.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_data_source(
        AwsAccountId='string',
        DataSourceId='string',
        Name='string',
        Type='ADOBE_ANALYTICS'|'AMAZON_ELASTICSEARCH'|'ATHENA'|'AURORA'|'AURORA_POSTGRESQL'|'AWS_IOT_ANALYTICS'|'GITHUB'|'JIRA'|'MARIADB'|'MYSQL'|'POSTGRESQL'|'PRESTO'|'REDSHIFT'|'S3'|'SALESFORCE'|'SERVICENOW'|'SNOWFLAKE'|'SPARK'|'SQLSERVER'|'TERADATA'|'TWITTER',
        DataSourceParameters={
            'AmazonElasticsearchParameters': {
                'Domain': 'string'
            },
            'AthenaParameters': {
                'WorkGroup': 'string'
            },
            'AuroraParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'AuroraPostgreSqlParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'AwsIotAnalyticsParameters': {
                'DataSetName': 'string'
            },
            'JiraParameters': {
                'SiteBaseUrl': 'string'
            },
            'MariaDbParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'MySqlParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'PostgreSqlParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'PrestoParameters': {
                'Host': 'string',
                'Port': 123,
                'Catalog': 'string'
            },
            'RdsParameters': {
                'InstanceId': 'string',
                'Database': 'string'
            },
            'RedshiftParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string',
                'ClusterId': 'string'
            },
            'S3Parameters': {
                'ManifestFileLocation': {
                    'Bucket': 'string',
                    'Key': 'string'
                }
            },
            'ServiceNowParameters': {
                'SiteBaseUrl': 'string'
            },
            'SnowflakeParameters': {
                'Host': 'string',
                'Database': 'string',
                'Warehouse': 'string'
            },
            'SparkParameters': {
                'Host': 'string',
                'Port': 123
            },
            'SqlServerParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'TeradataParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'TwitterParameters': {
                'Query': 'string',
                'MaxRows': 123
            }
        },
        Credentials={
            'CredentialPair': {
                'Username': 'string',
                'Password': 'string'
            }
        },
        Permissions=[
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ],
        VpcConnectionProperties={
            'VpcConnectionArn': 'string'
        },
        SslProperties={
            'DisableSsl': True|False
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type DataSourceId: string
    :param DataSourceId: [REQUIRED]\nAn ID for the data source. This ID is unique per AWS Region for each AWS account.\n

    :type Name: string
    :param Name: [REQUIRED]\nA display name for the data source.\n

    :type Type: string
    :param Type: [REQUIRED]\nThe type of the data source. Currently, the supported types for this operation are: ATHENA, AURORA, AURORA_POSTGRESQL, MARIADB, MYSQL, POSTGRESQL, PRESTO, REDSHIFT, S3, SNOWFLAKE, SPARK, SQLSERVER, TERADATA . Use ListDataSources to return a list of all data sources.\n

    :type DataSourceParameters: dict
    :param DataSourceParameters: The parameters that QuickSight uses to connect to your underlying source.\n\nAmazonElasticsearchParameters (dict) --Amazon Elasticsearch Service parameters.\n\nDomain (string) -- [REQUIRED]The Amazon Elasticsearch Service domain.\n\n\n\nAthenaParameters (dict) --Amazon Athena parameters.\n\nWorkGroup (string) --The workgroup that Amazon Athena uses.\n\n\n\nAuroraParameters (dict) --Amazon Aurora MySQL parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nAuroraPostgreSqlParameters (dict) --Aurora PostgreSQL parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nAwsIotAnalyticsParameters (dict) --AWS IoT Analytics parameters.\n\nDataSetName (string) -- [REQUIRED]Dataset name.\n\n\n\nJiraParameters (dict) --Jira parameters.\n\nSiteBaseUrl (string) -- [REQUIRED]The base URL of the Jira site.\n\n\n\nMariaDbParameters (dict) --MariaDB parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nMySqlParameters (dict) --MySQL parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nPostgreSqlParameters (dict) --PostgreSQL parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nPrestoParameters (dict) --Presto parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nCatalog (string) -- [REQUIRED]Catalog.\n\n\n\nRdsParameters (dict) --Amazon RDS parameters.\n\nInstanceId (string) -- [REQUIRED]Instance ID.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nRedshiftParameters (dict) --Amazon Redshift parameters.\n\nHost (string) --Host. This field can be blank if ClusterId is provided.\n\nPort (integer) --Port. This field can be blank if the ClusterId is provided.\n\nDatabase (string) -- [REQUIRED]Database.\n\nClusterId (string) --Cluster ID. This field can be blank if the Host and Port are provided.\n\n\n\nS3Parameters (dict) --S3 parameters.\n\nManifestFileLocation (dict) -- [REQUIRED]Location of the Amazon S3 manifest file. This is NULL if the manifest file was uploaded in the console.\n\nBucket (string) -- [REQUIRED]Amazon S3 bucket.\n\nKey (string) -- [REQUIRED]Amazon S3 key that identifies an object.\n\n\n\n\n\nServiceNowParameters (dict) --ServiceNow parameters.\n\nSiteBaseUrl (string) -- [REQUIRED]URL of the base site.\n\n\n\nSnowflakeParameters (dict) --Snowflake parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nDatabase (string) -- [REQUIRED]Database.\n\nWarehouse (string) -- [REQUIRED]Warehouse.\n\n\n\nSparkParameters (dict) --Spark parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\n\n\nSqlServerParameters (dict) --SQL Server parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nTeradataParameters (dict) --Teradata parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nTwitterParameters (dict) --Twitter parameters.\n\nQuery (string) -- [REQUIRED]Twitter query string.\n\nMaxRows (integer) -- [REQUIRED]Maximum number of rows to query Twitter.\n\n\n\n\n

    :type Credentials: dict
    :param Credentials: The credentials QuickSight that uses to connect to your underlying source. Currently, only credentials based on user name and password are supported.\n\nCredentialPair (dict) --Credential pair.\n\nUsername (string) -- [REQUIRED]User name.\n\nPassword (string) -- [REQUIRED]Password.\n\n\n\n\n

    :type Permissions: list
    :param Permissions: A list of resource permissions on the data source.\n\n(dict) --Permission for the resource.\n\nPrincipal (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .\n\nActions (list) -- [REQUIRED]The action to grant or revoke permissions on, for example 'quicksight:DescribeDashboard' .\n\n(string) --\n\n\n\n\n\n

    :type VpcConnectionProperties: dict
    :param VpcConnectionProperties: Use this parameter only when you want QuickSight to use a VPC connection when connecting to your underlying source.\n\nVpcConnectionArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) for the VPC connection.\n\n\n

    :type SslProperties: dict
    :param SslProperties: Secure Socket Layer (SSL) properties that apply when QuickSight connects to your underlying source.\n\nDisableSsl (boolean) --A Boolean option to control whether SSL should be disabled.\n\n\n

    :type Tags: list
    :param Tags: Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.\n\n(dict) --The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.\n\nKey (string) -- [REQUIRED]Tag key.\n\nValue (string) -- [REQUIRED]Tag value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'DataSourceId': 'string',
    'CreationStatus': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

Arn (string) --
The Amazon Resource Name (ARN) of the data source.

DataSourceId (string) --
The ID of the data source. This ID is unique per AWS Region for each AWS account.

CreationStatus (string) --
The status of creating the data source.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.LimitExceededException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Arn': 'string',
        'DataSourceId': 'string',
        'CreationStatus': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.LimitExceededException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def create_group(GroupName=None, Description=None, AwsAccountId=None, Namespace=None):
    """
    Creates an Amazon QuickSight group.
    The permissions resource is ``arn:aws:quicksight:us-east-1:<relevant-aws-account-id> :group/default/<group-name> `` .
    The response is a group object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_group(
        GroupName='string',
        Description='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nA name for the group that you want to create.\n

    :type Description: string
    :param Description: A description for the group that you want to create.

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Group': {
        'Arn': 'string',
        'GroupName': 'string',
        'Description': 'string',
        'PrincipalId': 'string'
    },
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --
The response object for this operation.

Group (dict) --
The name of the group.

Arn (string) --
The Amazon Resource Name (ARN) for the group.

GroupName (string) --
The name of the group.

Description (string) --
The group description.

PrincipalId (string) --
The principal ID of the group.



RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.PreconditionNotMetException
QuickSight.Client.exceptions.LimitExceededException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'Group': {
            'Arn': 'string',
            'GroupName': 'string',
            'Description': 'string',
            'PrincipalId': 'string'
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.PreconditionNotMetException
    QuickSight.Client.exceptions.LimitExceededException
    QuickSight.Client.exceptions.InternalFailureException
    QuickSight.Client.exceptions.ResourceUnavailableException
    
    """
    pass

def create_group_membership(MemberName=None, GroupName=None, AwsAccountId=None, Namespace=None):
    """
    Adds an Amazon QuickSight user to an Amazon QuickSight group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_group_membership(
        MemberName='string',
        GroupName='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type MemberName: string
    :param MemberName: [REQUIRED]\nThe name of the user that you want to add to the group membership.\n

    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group that you want to add the user to.\n

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GroupMember': {
        'Arn': 'string',
        'MemberName': 'string'
    },
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

GroupMember (dict) --
The group member.

Arn (string) --
The Amazon Resource Name (ARN) for the group member (user).

MemberName (string) --
The name of the group member (user).



RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.PreconditionNotMetException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'GroupMember': {
            'Arn': 'string',
            'MemberName': 'string'
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.PreconditionNotMetException
    QuickSight.Client.exceptions.InternalFailureException
    QuickSight.Client.exceptions.ResourceUnavailableException
    
    """
    pass

def create_iam_policy_assignment(AwsAccountId=None, AssignmentName=None, AssignmentStatus=None, PolicyArn=None, Identities=None, Namespace=None):
    """
    Creates an assignment with one specified IAM policy, identified by its Amazon Resource Name (ARN). This policy will be assigned to specified groups or users of Amazon QuickSight. The users and groups need to be in the same namespace.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_iam_policy_assignment(
        AwsAccountId='string',
        AssignmentName='string',
        AssignmentStatus='ENABLED'|'DRAFT'|'DISABLED',
        PolicyArn='string',
        Identities={
            'string': [
                'string',
            ]
        },
        Namespace='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account where you want to assign an IAM policy to QuickSight users or groups.\n

    :type AssignmentName: string
    :param AssignmentName: [REQUIRED]\nThe name of the assignment. It must be unique within an AWS account.\n

    :type AssignmentStatus: string
    :param AssignmentStatus: [REQUIRED]\nThe status of the assignment. Possible values are as follows:\n\nENABLED - Anything specified in this assignment is used when creating the data source.\nDISABLED - This assignment isn\'t used when creating the data source.\nDRAFT - This assignment is an unfinished draft and isn\'t used when creating the data source.\n\n

    :type PolicyArn: string
    :param PolicyArn: The ARN for the IAM policy to apply to the QuickSight users and groups specified in this assignment.

    :type Identities: dict
    :param Identities: The QuickSight users, groups, or both that you want to assign the policy to.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace that contains the assignment.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AssignmentName': 'string',
    'AssignmentId': 'string',
    'AssignmentStatus': 'ENABLED'|'DRAFT'|'DISABLED',
    'PolicyArn': 'string',
    'Identities': {
        'string': [
            'string',
        ]
    },
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

AssignmentName (string) --
The name of the assignment. This name must be unique within the AWS account.

AssignmentId (string) --
The ID for the assignment.

AssignmentStatus (string) --
The status of the assignment. Possible values are as follows:

ENABLED - Anything specified in this assignment is used when creating the data source.
DISABLED - This assignment isn\'t used when creating the data source.
DRAFT - This assignment is an unfinished draft and isn\'t used when creating the data source.


PolicyArn (string) --
The ARN for the IAM policy that is applied to the QuickSight users and groups specified in this assignment.

Identities (dict) --
The QuickSight users, groups, or both that the IAM policy is assigned to.

(string) --
(list) --
(string) --






RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ConcurrentUpdatingException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'AssignmentName': 'string',
        'AssignmentId': 'string',
        'AssignmentStatus': 'ENABLED'|'DRAFT'|'DISABLED',
        'PolicyArn': 'string',
        'Identities': {
            'string': [
                'string',
            ]
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    ENABLED - Anything specified in this assignment is used when creating the data source.
    DISABLED - This assignment isn\'t used when creating the data source.
    DRAFT - This assignment is an unfinished draft and isn\'t used when creating the data source.
    
    """
    pass

def create_ingestion(DataSetId=None, IngestionId=None, AwsAccountId=None):
    """
    Creates and starts a new SPICE ingestion on a dataset
    Any ingestions operating on tagged datasets inherit the same tags automatically for use in access control. For an example, see How do I create an IAM policy to control access to Amazon EC2 resources using tags? in the AWS Knowledge Center. Tags are visible on the tagged dataset, but not on the ingestion resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_ingestion(
        DataSetId='string',
        IngestionId='string',
        AwsAccountId='string'
    )
    
    
    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe ID of the dataset used in the ingestion.\n

    :type IngestionId: string
    :param IngestionId: [REQUIRED]\nAn ID for the ingestion.\n

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'IngestionId': 'string',
    'IngestionStatus': 'INITIALIZED'|'QUEUED'|'RUNNING'|'FAILED'|'COMPLETED'|'CANCELLED',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

Arn (string) --
The Amazon Resource Name (ARN) for the data ingestion.

IngestionId (string) --
An ID for the ingestion.

IngestionStatus (string) --
The ingestion status.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.LimitExceededException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Arn': 'string',
        'IngestionId': 'string',
        'IngestionStatus': 'INITIALIZED'|'QUEUED'|'RUNNING'|'FAILED'|'COMPLETED'|'CANCELLED',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.LimitExceededException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def create_template(AwsAccountId=None, TemplateId=None, Name=None, Permissions=None, SourceEntity=None, Tags=None, VersionDescription=None):
    """
    Creates a template from an existing QuickSight analysis or template. You can use the resulting template to create a dashboard.
    A template is an entity in QuickSight that encapsulates the metadata required to create an analysis and that you can use to create s dashboard. A template adds a layer of abstraction by using placeholders to replace the dataset associated with the analysis. You can use templates to create dashboards by replacing dataset placeholders with datasets that follow the same schema that was used to create the source analysis and template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_template(
        AwsAccountId='string',
        TemplateId='string',
        Name='string',
        Permissions=[
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ],
        SourceEntity={
            'SourceAnalysis': {
                'Arn': 'string',
                'DataSetReferences': [
                    {
                        'DataSetPlaceholder': 'string',
                        'DataSetArn': 'string'
                    },
                ]
            },
            'SourceTemplate': {
                'Arn': 'string'
            }
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        VersionDescription='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type TemplateId: string
    :param TemplateId: [REQUIRED]\nAn ID for the template that you want to create. This template is unique per AWS Region in each AWS account.\n

    :type Name: string
    :param Name: A display name for the template.

    :type Permissions: list
    :param Permissions: A list of resource permissions to be set on the template.\n\n(dict) --Permission for the resource.\n\nPrincipal (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .\n\nActions (list) -- [REQUIRED]The action to grant or revoke permissions on, for example 'quicksight:DescribeDashboard' .\n\n(string) --\n\n\n\n\n\n

    :type SourceEntity: dict
    :param SourceEntity: [REQUIRED]\nThe Amazon Resource Name (ARN) of the source entity from which this template is being created. Currently, you can create a template from an analysis or another template. If the ARN is for an analysis, include its dataset references.\n\nSourceAnalysis (dict) --The source analysis, if it is based on an analysis.\n\nArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the resource.\n\nDataSetReferences (list) -- [REQUIRED]A structure containing information about the dataset references used as placeholders in the template.\n\n(dict) --Dataset reference.\n\nDataSetPlaceholder (string) -- [REQUIRED]Dataset placeholder.\n\nDataSetArn (string) -- [REQUIRED]Dataset Amazon Resource Name (ARN).\n\n\n\n\n\n\n\nSourceTemplate (dict) --The source template, if it is based on an template.\n\nArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the resource.\n\n\n\n\n

    :type Tags: list
    :param Tags: Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.\n\n(dict) --The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.\n\nKey (string) -- [REQUIRED]Tag key.\n\nValue (string) -- [REQUIRED]Tag value.\n\n\n\n\n

    :type VersionDescription: string
    :param VersionDescription: A description of the current template version being created. This API operation creates the first version of the template. Every time UpdateTemplate is called, a new version is created. Each version of the template maintains a description of the version in the VersionDescription field.

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'VersionArn': 'string',
    'TemplateId': 'string',
    'CreationStatus': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

Arn (string) --
The ARN for the template.

VersionArn (string) --
The ARN for the template, including the version information of the first version.

TemplateId (string) --
The ID of the template.

CreationStatus (string) --
The template creation status.

Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.LimitExceededException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Arn': 'string',
        'VersionArn': 'string',
        'TemplateId': 'string',
        'CreationStatus': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.LimitExceededException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def create_template_alias(AwsAccountId=None, TemplateId=None, AliasName=None, TemplateVersionNumber=None):
    """
    Creates a template alias for a template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_template_alias(
        AwsAccountId='string',
        TemplateId='string',
        AliasName='string',
        TemplateVersionNumber=123
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the template that you creating an alias for.\n

    :type TemplateId: string
    :param TemplateId: [REQUIRED]\nAn ID for the template.\n

    :type AliasName: string
    :param AliasName: [REQUIRED]\nThe name that you want to give to the template alias that you\'re creating. Don\'t start the alias name with the $ character. Alias names that start with $ are reserved by QuickSight.\n

    :type TemplateVersionNumber: integer
    :param TemplateVersionNumber: [REQUIRED]\nThe version number of the template.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TemplateAlias': {
        'AliasName': 'string',
        'Arn': 'string',
        'TemplateVersionNumber': 123
    },
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

TemplateAlias (dict) --
Information about the template alias.

AliasName (string) --
The display name of the template alias.

Arn (string) --
The Amazon Resource Name (ARN) of the template alias.

TemplateVersionNumber (integer) --
The version number of the template alias.



Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.LimitExceededException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'TemplateAlias': {
            'AliasName': 'string',
            'Arn': 'string',
            'TemplateVersionNumber': 123
        },
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.LimitExceededException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_dashboard(AwsAccountId=None, DashboardId=None, VersionNumber=None):
    """
    Deletes a dashboard.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_dashboard(
        AwsAccountId='string',
        DashboardId='string',
        VersionNumber=123
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the dashboard that you\'re deleting.\n

    :type DashboardId: string
    :param DashboardId: [REQUIRED]\nThe ID for the dashboard.\n

    :type VersionNumber: integer
    :param VersionNumber: The version number of the dashboard. If the version number property is provided, only the specified version of the dashboard is deleted.

    :rtype: dict

ReturnsResponse Syntax
{
    'Status': 123,
    'Arn': 'string',
    'DashboardId': 'string',
    'RequestId': 'string'
}


Response Structure

(dict) --

Status (integer) --
The HTTP status of the request.

Arn (string) --
The Secure Socket Layer (SSL) properties that apply for the resource.

DashboardId (string) --
The ID of the dashboard.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Status': 123,
        'Arn': 'string',
        'DashboardId': 'string',
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_data_set(AwsAccountId=None, DataSetId=None):
    """
    Deletes a dataset.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_data_set(
        AwsAccountId='string',
        DataSetId='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'DataSetId': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

Arn (string) --
The Amazon Resource Name (ARN) of the dataset.

DataSetId (string) --
The ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Arn': 'string',
        'DataSetId': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_data_source(AwsAccountId=None, DataSourceId=None):
    """
    Deletes the data source permanently. This action breaks all the datasets that reference the deleted data source.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_data_source(
        AwsAccountId='string',
        DataSourceId='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type DataSourceId: string
    :param DataSourceId: [REQUIRED]\nThe ID of the data source. This ID is unique per AWS Region for each AWS account.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'DataSourceId': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

Arn (string) --
The Amazon Resource Name (ARN) of the data source that you deleted.

DataSourceId (string) --
The ID of the data source. This ID is unique per AWS Region for each AWS account.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Arn': 'string',
        'DataSourceId': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_group(GroupName=None, AwsAccountId=None, Namespace=None):
    """
    Removes a user group from Amazon QuickSight.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_group(
        GroupName='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group that you want to delete.\n

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.PreconditionNotMetException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.PreconditionNotMetException
    QuickSight.Client.exceptions.InternalFailureException
    QuickSight.Client.exceptions.ResourceUnavailableException
    
    """
    pass

def delete_group_membership(MemberName=None, GroupName=None, AwsAccountId=None, Namespace=None):
    """
    Removes a user from a group so that the user is no longer a member of the group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_group_membership(
        MemberName='string',
        GroupName='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type MemberName: string
    :param MemberName: [REQUIRED]\nThe name of the user that you want to delete from the group membership.\n

    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group that you want to delete the user from.\n

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.PreconditionNotMetException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.PreconditionNotMetException
    QuickSight.Client.exceptions.InternalFailureException
    QuickSight.Client.exceptions.ResourceUnavailableException
    
    """
    pass

def delete_iam_policy_assignment(AwsAccountId=None, AssignmentName=None, Namespace=None):
    """
    Deletes an existing IAM policy assignment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_iam_policy_assignment(
        AwsAccountId='string',
        AssignmentName='string',
        Namespace='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID where you want to delete the IAM policy assignment.\n

    :type AssignmentName: string
    :param AssignmentName: [REQUIRED]\nThe name of the assignment.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace that contains the assignment.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AssignmentName': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

AssignmentName (string) --
The name of the assignment.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ConcurrentUpdatingException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'AssignmentName': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ConcurrentUpdatingException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_template(AwsAccountId=None, TemplateId=None, VersionNumber=None):
    """
    Deletes a template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_template(
        AwsAccountId='string',
        TemplateId='string',
        VersionNumber=123
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the template that you\'re deleting.\n

    :type TemplateId: string
    :param TemplateId: [REQUIRED]\nAn ID for the template you want to delete.\n

    :type VersionNumber: integer
    :param VersionNumber: Specifies the version of the template that you want to delete. If you don\'t provide a version number, DeleteTemplate deletes all versions of the template.

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestId': 'string',
    'Arn': 'string',
    'TemplateId': 'string',
    'Status': 123
}


Response Structure

(dict) --

RequestId (string) --
The AWS request ID for this operation.

Arn (string) --
The Amazon Resource Name (ARN) of the resource.

TemplateId (string) --
An ID for the template.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.LimitExceededException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'RequestId': 'string',
        'Arn': 'string',
        'TemplateId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.LimitExceededException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_template_alias(AwsAccountId=None, TemplateId=None, AliasName=None):
    """
    Deletes the item that the specified template alias points to. If you provide a specific alias, you delete the version of the template that the alias points to.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_template_alias(
        AwsAccountId='string',
        TemplateId='string',
        AliasName='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the item to delete.\n

    :type TemplateId: string
    :param TemplateId: [REQUIRED]\nThe ID for the template that the specified alias is for.\n

    :type AliasName: string
    :param AliasName: [REQUIRED]\nThe name for the template alias. If you name a specific alias, you delete the version that the alias points to. You can specify the latest version of the template by providing the keyword $LATEST in the AliasName parameter.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Status': 123,
    'TemplateId': 'string',
    'AliasName': 'string',
    'Arn': 'string',
    'RequestId': 'string'
}


Response Structure

(dict) --

Status (integer) --
The HTTP status of the request.

TemplateId (string) --
An ID for the template associated with the deletion.

AliasName (string) --
The name for the template alias.

Arn (string) --
The Amazon Resource Name (ARN) of the resource.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Status': 123,
        'TemplateId': 'string',
        'AliasName': 'string',
        'Arn': 'string',
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_user(UserName=None, AwsAccountId=None, Namespace=None):
    """
    Deletes the Amazon QuickSight user that is associated with the identity of the AWS Identity and Access Management (IAM) user or role that\'s making the call. The IAM user isn\'t deleted as a result of this call.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user(
        UserName='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user that you want to delete.\n

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InternalFailureException
    QuickSight.Client.exceptions.ResourceUnavailableException
    
    """
    pass

def delete_user_by_principal_id(PrincipalId=None, AwsAccountId=None, Namespace=None):
    """
    Deletes a user identified by its principal ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user_by_principal_id(
        PrincipalId='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type PrincipalId: string
    :param PrincipalId: [REQUIRED]\nThe principal ID of the user.\n

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InternalFailureException
    QuickSight.Client.exceptions.ResourceUnavailableException
    
    """
    pass

def describe_dashboard(AwsAccountId=None, DashboardId=None, VersionNumber=None, AliasName=None):
    """
    Provides a summary for a dashboard.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_dashboard(
        AwsAccountId='string',
        DashboardId='string',
        VersionNumber=123,
        AliasName='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the dashboard that you\'re describing.\n

    :type DashboardId: string
    :param DashboardId: [REQUIRED]\nThe ID for the dashboard.\n

    :type VersionNumber: integer
    :param VersionNumber: The version number for the dashboard. If a version number isn\'t passed, the latest published dashboard version is described.

    :type AliasName: string
    :param AliasName: The alias name.

    :rtype: dict

ReturnsResponse Syntax
{
    'Dashboard': {
        'DashboardId': 'string',
        'Arn': 'string',
        'Name': 'string',
        'Version': {
            'CreatedTime': datetime(2015, 1, 1),
            'Errors': [
                {
                    'Type': 'ACCESS_DENIED'|'SOURCE_NOT_FOUND'|'DATA_SET_NOT_FOUND'|'INTERNAL_FAILURE'|'PARAMETER_VALUE_INCOMPATIBLE'|'PARAMETER_TYPE_INVALID'|'PARAMETER_NOT_FOUND'|'COLUMN_TYPE_MISMATCH'|'COLUMN_GEOGRAPHIC_ROLE_MISMATCH'|'COLUMN_REPLACEMENT_MISSING',
                    'Message': 'string'
                },
            ],
            'VersionNumber': 123,
            'Status': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
            'Arn': 'string',
            'SourceEntityArn': 'string',
            'DataSetArns': [
                'string',
            ],
            'Description': 'string'
        },
        'CreatedTime': datetime(2015, 1, 1),
        'LastPublishedTime': datetime(2015, 1, 1),
        'LastUpdatedTime': datetime(2015, 1, 1)
    },
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

Dashboard (dict) --
Information about the dashboard.

DashboardId (string) --
Dashboard ID.

Arn (string) --
The Amazon Resource Name (ARN) of the resource.

Name (string) --
A display name for the dashboard.

Version (dict) --
Version.

CreatedTime (datetime) --
The time that this dashboard version was created.

Errors (list) --
Errors.

(dict) --
Dashboard error.

Type (string) --
Type.

Message (string) --
Message.





VersionNumber (integer) --
Version number.

Status (string) --
The HTTP status of the request.

Arn (string) --
The Amazon Resource Name (ARN) of the resource.

SourceEntityArn (string) --
Source entity ARN.

DataSetArns (list) --
The Amazon Resource Numbers (ARNs) for the datasets that are associated with a version of the dashboard.

(string) --


Description (string) --
Description.



CreatedTime (datetime) --
The time that this dataset was created.

LastPublishedTime (datetime) --
The last time that this dataset was published.

LastUpdatedTime (datetime) --
The last time that this dataset was updated.



Status (integer) --
The HTTP status of this request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Dashboard': {
            'DashboardId': 'string',
            'Arn': 'string',
            'Name': 'string',
            'Version': {
                'CreatedTime': datetime(2015, 1, 1),
                'Errors': [
                    {
                        'Type': 'ACCESS_DENIED'|'SOURCE_NOT_FOUND'|'DATA_SET_NOT_FOUND'|'INTERNAL_FAILURE'|'PARAMETER_VALUE_INCOMPATIBLE'|'PARAMETER_TYPE_INVALID'|'PARAMETER_NOT_FOUND'|'COLUMN_TYPE_MISMATCH'|'COLUMN_GEOGRAPHIC_ROLE_MISMATCH'|'COLUMN_REPLACEMENT_MISSING',
                        'Message': 'string'
                    },
                ],
                'VersionNumber': 123,
                'Status': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
                'Arn': 'string',
                'SourceEntityArn': 'string',
                'DataSetArns': [
                    'string',
                ],
                'Description': 'string'
            },
            'CreatedTime': datetime(2015, 1, 1),
            'LastPublishedTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1)
        },
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_dashboard_permissions(AwsAccountId=None, DashboardId=None):
    """
    Describes read and write permissions for a dashboard.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_dashboard_permissions(
        AwsAccountId='string',
        DashboardId='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the dashboard that you\'re describing permissions for.\n

    :type DashboardId: string
    :param DashboardId: [REQUIRED]\nThe ID for the dashboard, also added to the IAM policy.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DashboardId': 'string',
    'DashboardArn': 'string',
    'Permissions': [
        {
            'Principal': 'string',
            'Actions': [
                'string',
            ]
        },
    ],
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

DashboardId (string) --
The ID for the dashboard.

DashboardArn (string) --
The Amazon Resource Name (ARN) of the dashboard.

Permissions (list) --
A structure that contains the permissions for the dashboard.

(dict) --
Permission for the resource.

Principal (string) --
The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .

Actions (list) --
The action to grant or revoke permissions on, for example "quicksight:DescribeDashboard" .

(string) --






Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'DashboardId': 'string',
        'DashboardArn': 'string',
        'Permissions': [
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ],
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_data_set(AwsAccountId=None, DataSetId=None):
    """
    Describes a dataset.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_data_set(
        AwsAccountId='string',
        DataSetId='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DataSet': {
        'Arn': 'string',
        'DataSetId': 'string',
        'Name': 'string',
        'CreatedTime': datetime(2015, 1, 1),
        'LastUpdatedTime': datetime(2015, 1, 1),
        'PhysicalTableMap': {
            'string': {
                'RelationalTable': {
                    'DataSourceArn': 'string',
                    'Schema': 'string',
                    'Name': 'string',
                    'InputColumns': [
                        {
                            'Name': 'string',
                            'Type': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME'|'BIT'|'BOOLEAN'|'JSON'
                        },
                    ]
                },
                'CustomSql': {
                    'DataSourceArn': 'string',
                    'Name': 'string',
                    'SqlQuery': 'string',
                    'Columns': [
                        {
                            'Name': 'string',
                            'Type': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME'|'BIT'|'BOOLEAN'|'JSON'
                        },
                    ]
                },
                'S3Source': {
                    'DataSourceArn': 'string',
                    'UploadSettings': {
                        'Format': 'CSV'|'TSV'|'CLF'|'ELF'|'XLSX'|'JSON',
                        'StartFromRow': 123,
                        'ContainsHeader': True|False,
                        'TextQualifier': 'DOUBLE_QUOTE'|'SINGLE_QUOTE',
                        'Delimiter': 'string'
                    },
                    'InputColumns': [
                        {
                            'Name': 'string',
                            'Type': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME'|'BIT'|'BOOLEAN'|'JSON'
                        },
                    ]
                }
            }
        },
        'LogicalTableMap': {
            'string': {
                'Alias': 'string',
                'DataTransforms': [
                    {
                        'ProjectOperation': {
                            'ProjectedColumns': [
                                'string',
                            ]
                        },
                        'FilterOperation': {
                            'ConditionExpression': 'string'
                        },
                        'CreateColumnsOperation': {
                            'Columns': [
                                {
                                    'ColumnName': 'string',
                                    'ColumnId': 'string',
                                    'Expression': 'string'
                                },
                            ]
                        },
                        'RenameColumnOperation': {
                            'ColumnName': 'string',
                            'NewColumnName': 'string'
                        },
                        'CastColumnTypeOperation': {
                            'ColumnName': 'string',
                            'NewColumnType': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME',
                            'Format': 'string'
                        },
                        'TagColumnOperation': {
                            'ColumnName': 'string',
                            'Tags': [
                                {
                                    'ColumnGeographicRole': 'COUNTRY'|'STATE'|'COUNTY'|'CITY'|'POSTCODE'|'LONGITUDE'|'LATITUDE'
                                },
                            ]
                        }
                    },
                ],
                'Source': {
                    'JoinInstruction': {
                        'LeftOperand': 'string',
                        'RightOperand': 'string',
                        'Type': 'INNER'|'OUTER'|'LEFT'|'RIGHT',
                        'OnClause': 'string'
                    },
                    'PhysicalTableId': 'string'
                }
            }
        },
        'OutputColumns': [
            {
                'Name': 'string',
                'Type': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME'
            },
        ],
        'ImportMode': 'SPICE'|'DIRECT_QUERY',
        'ConsumedSpiceCapacityInBytes': 123,
        'ColumnGroups': [
            {
                'GeoSpatialColumnGroup': {
                    'Name': 'string',
                    'CountryCode': 'US',
                    'Columns': [
                        'string',
                    ]
                }
            },
        ],
        'RowLevelPermissionDataSet': {
            'Arn': 'string',
            'PermissionPolicy': 'GRANT_ACCESS'|'DENY_ACCESS'
        }
    },
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

DataSet (dict) --
Information on the dataset.

Arn (string) --
The Amazon Resource Name (ARN) of the resource.

DataSetId (string) --
The ID of the dataset.

Name (string) --
A display name for the dataset.

CreatedTime (datetime) --
The time that this dataset was created.

LastUpdatedTime (datetime) --
The last time that this dataset was updated.

PhysicalTableMap (dict) --
Declares the physical tables that are available in the underlying data sources.

(string) --

(dict) --
A view of a data source that contains information about the shape of the data in the underlying source. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

RelationalTable (dict) --
A physical table type for relational data sources.

DataSourceArn (string) --
The Amazon Resource Name (ARN) for the data source.

Schema (string) --
The schema name. This name applies to certain relational database engines.

Name (string) --
The name of the relational table.

InputColumns (list) --
The column schema of the table.

(dict) --
Metadata for a column that is used as the input of a transform operation.

Name (string) --
The name of this column in the underlying data source.

Type (string) --
The data type of the column.







CustomSql (dict) --
A physical table type built from the results of the custom SQL query.

DataSourceArn (string) --
The Amazon Resource Name (ARN) of the data source.

Name (string) --
A display name for the SQL query result.

SqlQuery (string) --
The SQL query.

Columns (list) --
The column schema from the SQL query result set.

(dict) --
Metadata for a column that is used as the input of a transform operation.

Name (string) --
The name of this column in the underlying data source.

Type (string) --
The data type of the column.







S3Source (dict) --
A physical table type for as S3 data source.

DataSourceArn (string) --
The amazon Resource Name (ARN) for the data source.

UploadSettings (dict) --
Information about the format for the S3 source file or files.

Format (string) --
File format.

StartFromRow (integer) --
A row number to start reading data from.

ContainsHeader (boolean) --
Whether the file has a header row, or the files each have a header row.

TextQualifier (string) --
Text qualifier.

Delimiter (string) --
The delimiter between values in the file.



InputColumns (list) --
A physical table type for as S3 data source.

(dict) --
Metadata for a column that is used as the input of a transform operation.

Name (string) --
The name of this column in the underlying data source.

Type (string) --
The data type of the column.













LogicalTableMap (dict) --
Configures the combination and transformation of the data from the physical tables.

(string) --

(dict) --
A logical table is a unit that joins and that data transformations operate on. A logical table has a source, which can be either a physical table or result of a join. When a logical table points to a physical table, the logical table acts as a mutable copy of that physical table through transform operations.

Alias (string) --
A display name for the logical table.

DataTransforms (list) --
Transform operations that act on this logical table.

(dict) --
A data transformation on a logical table. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

ProjectOperation (dict) --
An operation that projects columns. Operations that come after a projection can only refer to projected columns.

ProjectedColumns (list) --
Projected columns.

(string) --




FilterOperation (dict) --
An operation that filters rows based on some condition.

ConditionExpression (string) --
An expression that must evaluate to a Boolean value. Rows for which the expression evaluates to true are kept in the dataset.



CreateColumnsOperation (dict) --
An operation that creates calculated columns. Columns created in one such operation form a lexical closure.

Columns (list) --
Calculated columns to create.

(dict) --
A calculated column for a dataset.

ColumnName (string) --
Column name.

ColumnId (string) --
A unique ID to identify a calculated column. During a dataset update, if the column ID of a calculated column matches that of an existing calculated column, Amazon QuickSight preserves the existing calculated column.

Expression (string) --
An expression that defines the calculated column.







RenameColumnOperation (dict) --
An operation that renames a column.

ColumnName (string) --
The name of the column to be renamed.

NewColumnName (string) --
The new name for the column.



CastColumnTypeOperation (dict) --
A transform operation that casts a column to a different type.

ColumnName (string) --
Column name.

NewColumnType (string) --
New column data type.

Format (string) --
When casting a column from string to datetime type, you can supply a string in a format supported by Amazon QuickSight to denote the source data format.



TagColumnOperation (dict) --
An operation that tags a column with additional information.

ColumnName (string) --
The column that this operation acts on.

Tags (list) --
The dataset column tag, currently only used for geospatial type tagging. .

Note
This is not tags for the AWS tagging feature. .


(dict) --
A tag for a column in a TagColumnOperation structure. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

ColumnGeographicRole (string) --
A geospatial role for a column.











Source (dict) --
Source of this logical table.

JoinInstruction (dict) --
Specifies the result of a join of two logical tables.

LeftOperand (string) --
Left operand.

RightOperand (string) --
Right operand.

Type (string) --
Type.

OnClause (string) --
On Clause.



PhysicalTableId (string) --
Physical table ID.









OutputColumns (list) --
The list of columns after all transforms. These columns are available in templates, analyses, and dashboards.

(dict) --
Output column.

Name (string) --
A display name for the dataset.

Type (string) --
Type.





ImportMode (string) --
Indicates whether you want to import the data into SPICE.

ConsumedSpiceCapacityInBytes (integer) --
The amount of SPICE capacity used by this dataset. This is 0 if the dataset isn\'t imported into SPICE.

ColumnGroups (list) --
Groupings of columns that work together in certain Amazon QuickSight features. Currently, only geospatial hierarchy is supported.

(dict) --
Groupings of columns that work together in certain Amazon QuickSight features. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

GeoSpatialColumnGroup (dict) --
Geospatial column group that denotes a hierarchy.

Name (string) --
A display name for the hierarchy.

CountryCode (string) --
Country code.

Columns (list) --
Columns in this hierarchy.

(string) --








RowLevelPermissionDataSet (dict) --
The row-level security configuration for the dataset.

Arn (string) --
The Amazon Resource Name (ARN) of the permission dataset.

PermissionPolicy (string) --
Permission policy.





RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'DataSet': {
            'Arn': 'string',
            'DataSetId': 'string',
            'Name': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1),
            'PhysicalTableMap': {
                'string': {
                    'RelationalTable': {
                        'DataSourceArn': 'string',
                        'Schema': 'string',
                        'Name': 'string',
                        'InputColumns': [
                            {
                                'Name': 'string',
                                'Type': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME'|'BIT'|'BOOLEAN'|'JSON'
                            },
                        ]
                    },
                    'CustomSql': {
                        'DataSourceArn': 'string',
                        'Name': 'string',
                        'SqlQuery': 'string',
                        'Columns': [
                            {
                                'Name': 'string',
                                'Type': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME'|'BIT'|'BOOLEAN'|'JSON'
                            },
                        ]
                    },
                    'S3Source': {
                        'DataSourceArn': 'string',
                        'UploadSettings': {
                            'Format': 'CSV'|'TSV'|'CLF'|'ELF'|'XLSX'|'JSON',
                            'StartFromRow': 123,
                            'ContainsHeader': True|False,
                            'TextQualifier': 'DOUBLE_QUOTE'|'SINGLE_QUOTE',
                            'Delimiter': 'string'
                        },
                        'InputColumns': [
                            {
                                'Name': 'string',
                                'Type': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME'|'BIT'|'BOOLEAN'|'JSON'
                            },
                        ]
                    }
                }
            },
            'LogicalTableMap': {
                'string': {
                    'Alias': 'string',
                    'DataTransforms': [
                        {
                            'ProjectOperation': {
                                'ProjectedColumns': [
                                    'string',
                                ]
                            },
                            'FilterOperation': {
                                'ConditionExpression': 'string'
                            },
                            'CreateColumnsOperation': {
                                'Columns': [
                                    {
                                        'ColumnName': 'string',
                                        'ColumnId': 'string',
                                        'Expression': 'string'
                                    },
                                ]
                            },
                            'RenameColumnOperation': {
                                'ColumnName': 'string',
                                'NewColumnName': 'string'
                            },
                            'CastColumnTypeOperation': {
                                'ColumnName': 'string',
                                'NewColumnType': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME',
                                'Format': 'string'
                            },
                            'TagColumnOperation': {
                                'ColumnName': 'string',
                                'Tags': [
                                    {
                                        'ColumnGeographicRole': 'COUNTRY'|'STATE'|'COUNTY'|'CITY'|'POSTCODE'|'LONGITUDE'|'LATITUDE'
                                    },
                                ]
                            }
                        },
                    ],
                    'Source': {
                        'JoinInstruction': {
                            'LeftOperand': 'string',
                            'RightOperand': 'string',
                            'Type': 'INNER'|'OUTER'|'LEFT'|'RIGHT',
                            'OnClause': 'string'
                        },
                        'PhysicalTableId': 'string'
                    }
                }
            },
            'OutputColumns': [
                {
                    'Name': 'string',
                    'Type': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME'
                },
            ],
            'ImportMode': 'SPICE'|'DIRECT_QUERY',
            'ConsumedSpiceCapacityInBytes': 123,
            'ColumnGroups': [
                {
                    'GeoSpatialColumnGroup': {
                        'Name': 'string',
                        'CountryCode': 'US',
                        'Columns': [
                            'string',
                        ]
                    }
                },
            ],
            'RowLevelPermissionDataSet': {
                'Arn': 'string',
                'PermissionPolicy': 'GRANT_ACCESS'|'DENY_ACCESS'
            }
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_data_set_permissions(AwsAccountId=None, DataSetId=None):
    """
    Describes the permissions on a dataset.
    The permissions resource is arn:aws:quicksight:region:aws-account-id:dataset/data-set-id .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_data_set_permissions(
        AwsAccountId='string',
        DataSetId='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DataSetArn': 'string',
    'DataSetId': 'string',
    'Permissions': [
        {
            'Principal': 'string',
            'Actions': [
                'string',
            ]
        },
    ],
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

DataSetArn (string) --
The Amazon Resource Name (ARN) of the dataset.

DataSetId (string) --
The ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.

Permissions (list) --
A list of resource permissions on the dataset.

(dict) --
Permission for the resource.

Principal (string) --
The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .

Actions (list) --
The action to grant or revoke permissions on, for example "quicksight:DescribeDashboard" .

(string) --






RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'DataSetArn': 'string',
        'DataSetId': 'string',
        'Permissions': [
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ],
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_data_source(AwsAccountId=None, DataSourceId=None):
    """
    Describes a data source.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_data_source(
        AwsAccountId='string',
        DataSourceId='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type DataSourceId: string
    :param DataSourceId: [REQUIRED]\nThe ID of the data source. This ID is unique per AWS Region for each AWS account.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DataSource': {
        'Arn': 'string',
        'DataSourceId': 'string',
        'Name': 'string',
        'Type': 'ADOBE_ANALYTICS'|'AMAZON_ELASTICSEARCH'|'ATHENA'|'AURORA'|'AURORA_POSTGRESQL'|'AWS_IOT_ANALYTICS'|'GITHUB'|'JIRA'|'MARIADB'|'MYSQL'|'POSTGRESQL'|'PRESTO'|'REDSHIFT'|'S3'|'SALESFORCE'|'SERVICENOW'|'SNOWFLAKE'|'SPARK'|'SQLSERVER'|'TERADATA'|'TWITTER',
        'Status': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
        'CreatedTime': datetime(2015, 1, 1),
        'LastUpdatedTime': datetime(2015, 1, 1),
        'DataSourceParameters': {
            'AmazonElasticsearchParameters': {
                'Domain': 'string'
            },
            'AthenaParameters': {
                'WorkGroup': 'string'
            },
            'AuroraParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'AuroraPostgreSqlParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'AwsIotAnalyticsParameters': {
                'DataSetName': 'string'
            },
            'JiraParameters': {
                'SiteBaseUrl': 'string'
            },
            'MariaDbParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'MySqlParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'PostgreSqlParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'PrestoParameters': {
                'Host': 'string',
                'Port': 123,
                'Catalog': 'string'
            },
            'RdsParameters': {
                'InstanceId': 'string',
                'Database': 'string'
            },
            'RedshiftParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string',
                'ClusterId': 'string'
            },
            'S3Parameters': {
                'ManifestFileLocation': {
                    'Bucket': 'string',
                    'Key': 'string'
                }
            },
            'ServiceNowParameters': {
                'SiteBaseUrl': 'string'
            },
            'SnowflakeParameters': {
                'Host': 'string',
                'Database': 'string',
                'Warehouse': 'string'
            },
            'SparkParameters': {
                'Host': 'string',
                'Port': 123
            },
            'SqlServerParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'TeradataParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'TwitterParameters': {
                'Query': 'string',
                'MaxRows': 123
            }
        },
        'VpcConnectionProperties': {
            'VpcConnectionArn': 'string'
        },
        'SslProperties': {
            'DisableSsl': True|False
        },
        'ErrorInfo': {
            'Type': 'TIMEOUT'|'ENGINE_VERSION_NOT_SUPPORTED'|'UNKNOWN_HOST'|'GENERIC_SQL_FAILURE'|'CONFLICT'|'UNKNOWN',
            'Message': 'string'
        }
    },
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

DataSource (dict) --
The information on the data source.

Arn (string) --
The Amazon Resource Name (ARN) of the data source.

DataSourceId (string) --
The ID of the data source. This ID is unique per AWS Region for each AWS account.

Name (string) --
A display name for the data source.

Type (string) --
The type of the data source. This type indicates which database engine the data source connects to.

Status (string) --
The HTTP status of the request.

CreatedTime (datetime) --
The time that this data source was created.

LastUpdatedTime (datetime) --
The last time that this data source was updated.

DataSourceParameters (dict) --
The parameters that Amazon QuickSight uses to connect to your underlying source. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

AmazonElasticsearchParameters (dict) --
Amazon Elasticsearch Service parameters.

Domain (string) --
The Amazon Elasticsearch Service domain.



AthenaParameters (dict) --
Amazon Athena parameters.

WorkGroup (string) --
The workgroup that Amazon Athena uses.



AuroraParameters (dict) --
Amazon Aurora MySQL parameters.

Host (string) --
Host.

Port (integer) --
Port.

Database (string) --
Database.



AuroraPostgreSqlParameters (dict) --
Aurora PostgreSQL parameters.

Host (string) --
Host.

Port (integer) --
Port.

Database (string) --
Database.



AwsIotAnalyticsParameters (dict) --
AWS IoT Analytics parameters.

DataSetName (string) --
Dataset name.



JiraParameters (dict) --
Jira parameters.

SiteBaseUrl (string) --
The base URL of the Jira site.



MariaDbParameters (dict) --
MariaDB parameters.

Host (string) --
Host.

Port (integer) --
Port.

Database (string) --
Database.



MySqlParameters (dict) --
MySQL parameters.

Host (string) --
Host.

Port (integer) --
Port.

Database (string) --
Database.



PostgreSqlParameters (dict) --
PostgreSQL parameters.

Host (string) --
Host.

Port (integer) --
Port.

Database (string) --
Database.



PrestoParameters (dict) --
Presto parameters.

Host (string) --
Host.

Port (integer) --
Port.

Catalog (string) --
Catalog.



RdsParameters (dict) --
Amazon RDS parameters.

InstanceId (string) --
Instance ID.

Database (string) --
Database.



RedshiftParameters (dict) --
Amazon Redshift parameters.

Host (string) --
Host. This field can be blank if ClusterId is provided.

Port (integer) --
Port. This field can be blank if the ClusterId is provided.

Database (string) --
Database.

ClusterId (string) --
Cluster ID. This field can be blank if the Host and Port are provided.



S3Parameters (dict) --
S3 parameters.

ManifestFileLocation (dict) --
Location of the Amazon S3 manifest file. This is NULL if the manifest file was uploaded in the console.

Bucket (string) --
Amazon S3 bucket.

Key (string) --
Amazon S3 key that identifies an object.





ServiceNowParameters (dict) --
ServiceNow parameters.

SiteBaseUrl (string) --
URL of the base site.



SnowflakeParameters (dict) --
Snowflake parameters.

Host (string) --
Host.

Database (string) --
Database.

Warehouse (string) --
Warehouse.



SparkParameters (dict) --
Spark parameters.

Host (string) --
Host.

Port (integer) --
Port.



SqlServerParameters (dict) --
SQL Server parameters.

Host (string) --
Host.

Port (integer) --
Port.

Database (string) --
Database.



TeradataParameters (dict) --
Teradata parameters.

Host (string) --
Host.

Port (integer) --
Port.

Database (string) --
Database.



TwitterParameters (dict) --
Twitter parameters.

Query (string) --
Twitter query string.

MaxRows (integer) --
Maximum number of rows to query Twitter.





VpcConnectionProperties (dict) --
The VPC connection information. You need to use this parameter only when you want QuickSight to use a VPC connection when connecting to your underlying source.

VpcConnectionArn (string) --
The Amazon Resource Name (ARN) for the VPC connection.



SslProperties (dict) --
Secure Socket Layer (SSL) properties that apply when QuickSight connects to your underlying source.

DisableSsl (boolean) --
A Boolean option to control whether SSL should be disabled.



ErrorInfo (dict) --
Error information from the last update or the creation of the data source.

Type (string) --
Error type.

Message (string) --
Error message.





RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'DataSource': {
            'Arn': 'string',
            'DataSourceId': 'string',
            'Name': 'string',
            'Type': 'ADOBE_ANALYTICS'|'AMAZON_ELASTICSEARCH'|'ATHENA'|'AURORA'|'AURORA_POSTGRESQL'|'AWS_IOT_ANALYTICS'|'GITHUB'|'JIRA'|'MARIADB'|'MYSQL'|'POSTGRESQL'|'PRESTO'|'REDSHIFT'|'S3'|'SALESFORCE'|'SERVICENOW'|'SNOWFLAKE'|'SPARK'|'SQLSERVER'|'TERADATA'|'TWITTER',
            'Status': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
            'CreatedTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1),
            'DataSourceParameters': {
                'AmazonElasticsearchParameters': {
                    'Domain': 'string'
                },
                'AthenaParameters': {
                    'WorkGroup': 'string'
                },
                'AuroraParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string'
                },
                'AuroraPostgreSqlParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string'
                },
                'AwsIotAnalyticsParameters': {
                    'DataSetName': 'string'
                },
                'JiraParameters': {
                    'SiteBaseUrl': 'string'
                },
                'MariaDbParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string'
                },
                'MySqlParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string'
                },
                'PostgreSqlParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string'
                },
                'PrestoParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Catalog': 'string'
                },
                'RdsParameters': {
                    'InstanceId': 'string',
                    'Database': 'string'
                },
                'RedshiftParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string',
                    'ClusterId': 'string'
                },
                'S3Parameters': {
                    'ManifestFileLocation': {
                        'Bucket': 'string',
                        'Key': 'string'
                    }
                },
                'ServiceNowParameters': {
                    'SiteBaseUrl': 'string'
                },
                'SnowflakeParameters': {
                    'Host': 'string',
                    'Database': 'string',
                    'Warehouse': 'string'
                },
                'SparkParameters': {
                    'Host': 'string',
                    'Port': 123
                },
                'SqlServerParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string'
                },
                'TeradataParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string'
                },
                'TwitterParameters': {
                    'Query': 'string',
                    'MaxRows': 123
                }
            },
            'VpcConnectionProperties': {
                'VpcConnectionArn': 'string'
            },
            'SslProperties': {
                'DisableSsl': True|False
            },
            'ErrorInfo': {
                'Type': 'TIMEOUT'|'ENGINE_VERSION_NOT_SUPPORTED'|'UNKNOWN_HOST'|'GENERIC_SQL_FAILURE'|'CONFLICT'|'UNKNOWN',
                'Message': 'string'
            }
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def describe_data_source_permissions(AwsAccountId=None, DataSourceId=None):
    """
    Describes the resource permissions for a data source.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_data_source_permissions(
        AwsAccountId='string',
        DataSourceId='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type DataSourceId: string
    :param DataSourceId: [REQUIRED]\nThe ID of the data source. This ID is unique per AWS Region for each AWS account.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DataSourceArn': 'string',
    'DataSourceId': 'string',
    'Permissions': [
        {
            'Principal': 'string',
            'Actions': [
                'string',
            ]
        },
    ],
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

DataSourceArn (string) --
The Amazon Resource Name (ARN) of the data source.

DataSourceId (string) --
The ID of the data source. This ID is unique per AWS Region for each AWS account.

Permissions (list) --
A list of resource permissions on the data source.

(dict) --
Permission for the resource.

Principal (string) --
The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .

Actions (list) --
The action to grant or revoke permissions on, for example "quicksight:DescribeDashboard" .

(string) --






RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'DataSourceArn': 'string',
        'DataSourceId': 'string',
        'Permissions': [
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ],
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_group(GroupName=None, AwsAccountId=None, Namespace=None):
    """
    Returns an Amazon QuickSight group\'s description and Amazon Resource Name (ARN).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_group(
        GroupName='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group that you want to describe.\n

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Group': {
        'Arn': 'string',
        'GroupName': 'string',
        'Description': 'string',
        'PrincipalId': 'string'
    },
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

Group (dict) --
The name of the group.

Arn (string) --
The Amazon Resource Name (ARN) for the group.

GroupName (string) --
The name of the group.

Description (string) --
The group description.

PrincipalId (string) --
The principal ID of the group.



RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.PreconditionNotMetException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'Group': {
            'Arn': 'string',
            'GroupName': 'string',
            'Description': 'string',
            'PrincipalId': 'string'
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.PreconditionNotMetException
    QuickSight.Client.exceptions.InternalFailureException
    QuickSight.Client.exceptions.ResourceUnavailableException
    
    """
    pass

def describe_iam_policy_assignment(AwsAccountId=None, AssignmentName=None, Namespace=None):
    """
    Describes an existing IAM policy assignment, as specified by the assignment name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_iam_policy_assignment(
        AwsAccountId='string',
        AssignmentName='string',
        Namespace='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the assignment that you want to describe.\n

    :type AssignmentName: string
    :param AssignmentName: [REQUIRED]\nThe name of the assignment.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace that contains the assignment.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IAMPolicyAssignment': {
        'AwsAccountId': 'string',
        'AssignmentId': 'string',
        'AssignmentName': 'string',
        'PolicyArn': 'string',
        'Identities': {
            'string': [
                'string',
            ]
        },
        'AssignmentStatus': 'ENABLED'|'DRAFT'|'DISABLED'
    },
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

IAMPolicyAssignment (dict) --
Information describing the IAM policy assignment.

AwsAccountId (string) --
The AWS account ID.

AssignmentId (string) --
Assignment ID.

AssignmentName (string) --
Assignment name.

PolicyArn (string) --
The Amazon Resource Name (ARN) for the IAM policy.

Identities (dict) --
Identities.

(string) --
(list) --
(string) --






AssignmentStatus (string) --
Assignment status.



RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidNextTokenException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'IAMPolicyAssignment': {
            'AwsAccountId': 'string',
            'AssignmentId': 'string',
            'AssignmentName': 'string',
            'PolicyArn': 'string',
            'Identities': {
                'string': [
                    'string',
                ]
            },
            'AssignmentStatus': 'ENABLED'|'DRAFT'|'DISABLED'
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def describe_ingestion(AwsAccountId=None, DataSetId=None, IngestionId=None):
    """
    Describes a SPICE ingestion.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_ingestion(
        AwsAccountId='string',
        DataSetId='string',
        IngestionId='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe ID of the dataset used in the ingestion.\n

    :type IngestionId: string
    :param IngestionId: [REQUIRED]\nAn ID for the ingestion.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Ingestion': {
        'Arn': 'string',
        'IngestionId': 'string',
        'IngestionStatus': 'INITIALIZED'|'QUEUED'|'RUNNING'|'FAILED'|'COMPLETED'|'CANCELLED',
        'ErrorInfo': {
            'Type': 'FAILURE_TO_ASSUME_ROLE'|'INGESTION_SUPERSEDED'|'INGESTION_CANCELED'|'DATA_SET_DELETED'|'DATA_SET_NOT_SPICE'|'S3_UPLOADED_FILE_DELETED'|'S3_MANIFEST_ERROR'|'DATA_TOLERANCE_EXCEPTION'|'SPICE_TABLE_NOT_FOUND'|'DATA_SET_SIZE_LIMIT_EXCEEDED'|'ROW_SIZE_LIMIT_EXCEEDED'|'ACCOUNT_CAPACITY_LIMIT_EXCEEDED'|'CUSTOMER_ERROR'|'DATA_SOURCE_NOT_FOUND'|'IAM_ROLE_NOT_AVAILABLE'|'CONNECTION_FAILURE'|'SQL_TABLE_NOT_FOUND'|'PERMISSION_DENIED'|'SSL_CERTIFICATE_VALIDATION_FAILURE'|'OAUTH_TOKEN_FAILURE'|'SOURCE_API_LIMIT_EXCEEDED_FAILURE'|'PASSWORD_AUTHENTICATION_FAILURE'|'SQL_SCHEMA_MISMATCH_ERROR'|'INVALID_DATE_FORMAT'|'INVALID_DATAPREP_SYNTAX'|'SOURCE_RESOURCE_LIMIT_EXCEEDED'|'SQL_INVALID_PARAMETER_VALUE'|'QUERY_TIMEOUT'|'SQL_NUMERIC_OVERFLOW'|'UNRESOLVABLE_HOST'|'UNROUTABLE_HOST'|'SQL_EXCEPTION'|'S3_FILE_INACCESSIBLE'|'IOT_FILE_NOT_FOUND'|'IOT_DATA_SET_FILE_EMPTY'|'INVALID_DATA_SOURCE_CONFIG'|'DATA_SOURCE_AUTH_FAILED'|'DATA_SOURCE_CONNECTION_FAILED'|'FAILURE_TO_PROCESS_JSON_FILE'|'INTERNAL_SERVICE_ERROR',
            'Message': 'string'
        },
        'RowInfo': {
            'RowsIngested': 123,
            'RowsDropped': 123
        },
        'QueueInfo': {
            'WaitingOnIngestion': 'string',
            'QueuedIngestion': 'string'
        },
        'CreatedTime': datetime(2015, 1, 1),
        'IngestionTimeInSeconds': 123,
        'IngestionSizeInBytes': 123,
        'RequestSource': 'MANUAL'|'SCHEDULED',
        'RequestType': 'INITIAL_INGESTION'|'EDIT'|'INCREMENTAL_REFRESH'|'FULL_REFRESH'
    },
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

Ingestion (dict) --
Information about the ingestion.

Arn (string) --
The Amazon Resource Name (ARN) of the resource.

IngestionId (string) --
Ingestion ID.

IngestionStatus (string) --
Ingestion status.

ErrorInfo (dict) --
Error information for this ingestion.

Type (string) --
Error type.

Message (string) --
Error message.



RowInfo (dict) --
Information about rows for a data set SPICE ingestion.

RowsIngested (integer) --
The number of rows that were ingested.

RowsDropped (integer) --
The number of rows that were not ingested.



QueueInfo (dict) --
Information about a queued dataset SPICE ingestion.

WaitingOnIngestion (string) --
The ID of the queued ingestion.

QueuedIngestion (string) --
The ID of the ongoing ingestion. The queued ingestion is waiting for the ongoing ingestion to complete.



CreatedTime (datetime) --
The time that this ingestion started.

IngestionTimeInSeconds (integer) --
The time that this ingestion took, measured in seconds.

IngestionSizeInBytes (integer) --
The size of the data ingested, in bytes.

RequestSource (string) --
Event source for this ingestion.

RequestType (string) --
Type of this ingestion.



RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Ingestion': {
            'Arn': 'string',
            'IngestionId': 'string',
            'IngestionStatus': 'INITIALIZED'|'QUEUED'|'RUNNING'|'FAILED'|'COMPLETED'|'CANCELLED',
            'ErrorInfo': {
                'Type': 'FAILURE_TO_ASSUME_ROLE'|'INGESTION_SUPERSEDED'|'INGESTION_CANCELED'|'DATA_SET_DELETED'|'DATA_SET_NOT_SPICE'|'S3_UPLOADED_FILE_DELETED'|'S3_MANIFEST_ERROR'|'DATA_TOLERANCE_EXCEPTION'|'SPICE_TABLE_NOT_FOUND'|'DATA_SET_SIZE_LIMIT_EXCEEDED'|'ROW_SIZE_LIMIT_EXCEEDED'|'ACCOUNT_CAPACITY_LIMIT_EXCEEDED'|'CUSTOMER_ERROR'|'DATA_SOURCE_NOT_FOUND'|'IAM_ROLE_NOT_AVAILABLE'|'CONNECTION_FAILURE'|'SQL_TABLE_NOT_FOUND'|'PERMISSION_DENIED'|'SSL_CERTIFICATE_VALIDATION_FAILURE'|'OAUTH_TOKEN_FAILURE'|'SOURCE_API_LIMIT_EXCEEDED_FAILURE'|'PASSWORD_AUTHENTICATION_FAILURE'|'SQL_SCHEMA_MISMATCH_ERROR'|'INVALID_DATE_FORMAT'|'INVALID_DATAPREP_SYNTAX'|'SOURCE_RESOURCE_LIMIT_EXCEEDED'|'SQL_INVALID_PARAMETER_VALUE'|'QUERY_TIMEOUT'|'SQL_NUMERIC_OVERFLOW'|'UNRESOLVABLE_HOST'|'UNROUTABLE_HOST'|'SQL_EXCEPTION'|'S3_FILE_INACCESSIBLE'|'IOT_FILE_NOT_FOUND'|'IOT_DATA_SET_FILE_EMPTY'|'INVALID_DATA_SOURCE_CONFIG'|'DATA_SOURCE_AUTH_FAILED'|'DATA_SOURCE_CONNECTION_FAILED'|'FAILURE_TO_PROCESS_JSON_FILE'|'INTERNAL_SERVICE_ERROR',
                'Message': 'string'
            },
            'RowInfo': {
                'RowsIngested': 123,
                'RowsDropped': 123
            },
            'QueueInfo': {
                'WaitingOnIngestion': 'string',
                'QueuedIngestion': 'string'
            },
            'CreatedTime': datetime(2015, 1, 1),
            'IngestionTimeInSeconds': 123,
            'IngestionSizeInBytes': 123,
            'RequestSource': 'MANUAL'|'SCHEDULED',
            'RequestType': 'INITIAL_INGESTION'|'EDIT'|'INCREMENTAL_REFRESH'|'FULL_REFRESH'
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def describe_template(AwsAccountId=None, TemplateId=None, VersionNumber=None, AliasName=None):
    """
    Describes a template\'s metadata.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_template(
        AwsAccountId='string',
        TemplateId='string',
        VersionNumber=123,
        AliasName='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the template that you\'re describing.\n

    :type TemplateId: string
    :param TemplateId: [REQUIRED]\nThe ID for the template.\n

    :type VersionNumber: integer
    :param VersionNumber: (Optional) The number for the version to describe. If a VersionNumber parameter value isn\'t provided, the latest version of the template is described.

    :type AliasName: string
    :param AliasName: The alias of the template that you want to describe. If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the template by providing the keyword $LATEST in the AliasName parameter. The keyword $PUBLISHED doesn\'t apply to templates.

    :rtype: dict

ReturnsResponse Syntax
{
    'Template': {
        'Arn': 'string',
        'Name': 'string',
        'Version': {
            'CreatedTime': datetime(2015, 1, 1),
            'Errors': [
                {
                    'Type': 'SOURCE_NOT_FOUND'|'DATA_SET_NOT_FOUND'|'INTERNAL_FAILURE',
                    'Message': 'string'
                },
            ],
            'VersionNumber': 123,
            'Status': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
            'DataSetConfigurations': [
                {
                    'Placeholder': 'string',
                    'DataSetSchema': {
                        'ColumnSchemaList': [
                            {
                                'Name': 'string',
                                'DataType': 'string',
                                'GeographicRole': 'string'
                            },
                        ]
                    },
                    'ColumnGroupSchemaList': [
                        {
                            'Name': 'string',
                            'ColumnGroupColumnSchemaList': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        },
                    ]
                },
            ],
            'Description': 'string',
            'SourceEntityArn': 'string'
        },
        'TemplateId': 'string',
        'LastUpdatedTime': datetime(2015, 1, 1),
        'CreatedTime': datetime(2015, 1, 1)
    },
    'Status': 123
}


Response Structure

(dict) --

Template (dict) --
The template structure for the object you want to describe.

Arn (string) --
The Amazon Resource Name (ARN) of the template.

Name (string) --
The display name of the template.

Version (dict) --
A structure describing the versions of the template.

CreatedTime (datetime) --
The time that this template version was created.

Errors (list) --
Errors associated with the template.

(dict) --
List of errors that occurred when the template version creation failed.

Type (string) --
Type of error.

Message (string) --
Description of the error type.





VersionNumber (integer) --
The version number of the template.

Status (string) --
The HTTP status of the request.

DataSetConfigurations (list) --
Schema of the dataset identified by the placeholder. The idea is that any dashboard created from the template should be bound to new datasets matching the same schema described through this API. .

(dict) --
Dataset configuration.

Placeholder (string) --
Placeholder.

DataSetSchema (dict) --
Dataset schema.

ColumnSchemaList (list) --
A structure containing the list of column schemas.

(dict) --
The column schema.

Name (string) --
The name of the column schema.

DataType (string) --
The data type of the column schema.

GeographicRole (string) --
The geographic role of the column schema.







ColumnGroupSchemaList (list) --
A structure containing the list of column group schemas.

(dict) --
The column group schema.

Name (string) --
The name of the column group schema.

ColumnGroupColumnSchemaList (list) --
A structure containing the list of schemas for column group columns.

(dict) --
A structure describing the name, data type, and geographic role of the columns.

Name (string) --
The name of the column group\'s column schema.













Description (string) --
The description of the template.

SourceEntityArn (string) --
The Amazon Resource Name (ARN) of the analysis or template which was used to create this template.



TemplateId (string) --
The ID for the template. This is unique per AWS Region for each AWS account.

LastUpdatedTime (datetime) --
Time when this was last updated.

CreatedTime (datetime) --
Time when this was created.



Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Template': {
            'Arn': 'string',
            'Name': 'string',
            'Version': {
                'CreatedTime': datetime(2015, 1, 1),
                'Errors': [
                    {
                        'Type': 'SOURCE_NOT_FOUND'|'DATA_SET_NOT_FOUND'|'INTERNAL_FAILURE',
                        'Message': 'string'
                    },
                ],
                'VersionNumber': 123,
                'Status': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
                'DataSetConfigurations': [
                    {
                        'Placeholder': 'string',
                        'DataSetSchema': {
                            'ColumnSchemaList': [
                                {
                                    'Name': 'string',
                                    'DataType': 'string',
                                    'GeographicRole': 'string'
                                },
                            ]
                        },
                        'ColumnGroupSchemaList': [
                            {
                                'Name': 'string',
                                'ColumnGroupColumnSchemaList': [
                                    {
                                        'Name': 'string'
                                    },
                                ]
                            },
                        ]
                    },
                ],
                'Description': 'string',
                'SourceEntityArn': 'string'
            },
            'TemplateId': 'string',
            'LastUpdatedTime': datetime(2015, 1, 1),
            'CreatedTime': datetime(2015, 1, 1)
        },
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def describe_template_alias(AwsAccountId=None, TemplateId=None, AliasName=None):
    """
    Describes the template alias for a template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_template_alias(
        AwsAccountId='string',
        TemplateId='string',
        AliasName='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the template alias that you\'re describing.\n

    :type TemplateId: string
    :param TemplateId: [REQUIRED]\nThe ID for the template.\n

    :type AliasName: string
    :param AliasName: [REQUIRED]\nThe name of the template alias that you want to describe. If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the template by providing the keyword $LATEST in the AliasName parameter. The keyword $PUBLISHED doesn\'t apply to templates.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TemplateAlias': {
        'AliasName': 'string',
        'Arn': 'string',
        'TemplateVersionNumber': 123
    },
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

TemplateAlias (dict) --
Information about the template alias.

AliasName (string) --
The display name of the template alias.

Arn (string) --
The Amazon Resource Name (ARN) of the template alias.

TemplateVersionNumber (integer) --
The version number of the template alias.



Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'TemplateAlias': {
            'AliasName': 'string',
            'Arn': 'string',
            'TemplateVersionNumber': 123
        },
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def describe_template_permissions(AwsAccountId=None, TemplateId=None):
    """
    Describes read and write permissions on a template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_template_permissions(
        AwsAccountId='string',
        TemplateId='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the template that you\'re describing.\n

    :type TemplateId: string
    :param TemplateId: [REQUIRED]\nThe ID for the template.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TemplateId': 'string',
    'TemplateArn': 'string',
    'Permissions': [
        {
            'Principal': 'string',
            'Actions': [
                'string',
            ]
        },
    ],
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

TemplateId (string) --
The ID for the template.

TemplateArn (string) --
The Amazon Resource Name (ARN) of the template.

Permissions (list) --
A list of resource permissions to be set on the template.

(dict) --
Permission for the resource.

Principal (string) --
The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .

Actions (list) --
The action to grant or revoke permissions on, for example "quicksight:DescribeDashboard" .

(string) --






RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'TemplateId': 'string',
        'TemplateArn': 'string',
        'Permissions': [
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ],
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_user(UserName=None, AwsAccountId=None, Namespace=None):
    """
    Returns information about a user, given the user name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_user(
        UserName='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user that you want to describe.\n

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'User': {
        'Arn': 'string',
        'UserName': 'string',
        'Email': 'string',
        'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
        'IdentityType': 'IAM'|'QUICKSIGHT',
        'Active': True|False,
        'PrincipalId': 'string'
    },
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

User (dict) --
The user name.

Arn (string) --
The Amazon Resource Name (ARN) for the user.

UserName (string) --
The user\'s user name.

Email (string) --
The user\'s email address.

Role (string) --
The Amazon QuickSight role for the user. The user role can be one of the following:.

READER : A user who has read-only access to dashboards.
AUTHOR : A user who can create data sources, datasets, analyses, and dashboards.
ADMIN : A user who is an author, who can also manage Amazon QuickSight settings.
RESTRICTED_READER : This role isn\'t currently available for use.
RESTRICTED_AUTHOR : This role isn\'t currently available for use.


IdentityType (string) --
The type of identity authentication used by the user.

Active (boolean) --
The active status of user. When you create an Amazon QuickSight user that\xe2\x80\x99s not an IAM user or an Active Directory user, that user is inactive until they sign in and provide a password.

PrincipalId (string) --
The principal ID of the user.



RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'User': {
            'Arn': 'string',
            'UserName': 'string',
            'Email': 'string',
            'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
            'IdentityType': 'IAM'|'QUICKSIGHT',
            'Active': True|False,
            'PrincipalId': 'string'
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    READER : A user who has read-only access to dashboards.
    AUTHOR : A user who can create data sources, datasets, analyses, and dashboards.
    ADMIN : A user who is an author, who can also manage Amazon QuickSight settings.
    RESTRICTED_READER : This role isn\'t currently available for use.
    RESTRICTED_AUTHOR : This role isn\'t currently available for use.
    
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

def get_dashboard_embed_url(AwsAccountId=None, DashboardId=None, IdentityType=None, SessionLifetimeInMinutes=None, UndoRedoDisabled=None, ResetDisabled=None, UserArn=None):
    """
    Generates a server-side embeddable URL and authorization code. For this process to work properly, first configure the dashboards and user permissions. For more information, see Embedding Amazon QuickSight Dashboards in the Amazon QuickSight User Guide or Embedding Amazon QuickSight Dashboards in the Amazon QuickSight API Reference .
    Currently, you can use GetDashboardEmbedURL only from the server, not from the user\xe2\x80\x99s browser.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_dashboard_embed_url(
        AwsAccountId='string',
        DashboardId='string',
        IdentityType='IAM'|'QUICKSIGHT',
        SessionLifetimeInMinutes=123,
        UndoRedoDisabled=True|False,
        ResetDisabled=True|False,
        UserArn='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that contains the dashboard that you\'re embedding.\n

    :type DashboardId: string
    :param DashboardId: [REQUIRED]\nThe ID for the dashboard, also added to the IAM policy.\n

    :type IdentityType: string
    :param IdentityType: [REQUIRED]\nThe authentication method that the user uses to sign in.\n

    :type SessionLifetimeInMinutes: integer
    :param SessionLifetimeInMinutes: How many minutes the session is valid. The session lifetime must be 15-600 minutes.

    :type UndoRedoDisabled: boolean
    :param UndoRedoDisabled: Remove the undo/redo button on the embedded dashboard. The default is FALSE, which enables the undo/redo button.

    :type ResetDisabled: boolean
    :param ResetDisabled: Remove the reset button on the embedded dashboard. The default is FALSE, which enables the reset button.

    :type UserArn: string
    :param UserArn: The Amazon QuickSight user\'s Amazon Resource Name (ARN), for use with QUICKSIGHT identity type. You can use this for any Amazon QuickSight users in your account (readers, authors, or admins) authenticated as one of the following:\n\nActive Directory (AD) users or group members\nInvited nonfederated users\nIAM users and IAM role-based sessions authenticated through Federated Single Sign-On using SAML, OpenID Connect, or IAM federation.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EmbedUrl': 'string',
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

EmbedUrl (string) --
An URL that you can put into your server-side webpage to embed your dashboard. This URL is valid for 5 minutes, and the resulting session is valid for 10 hours. The API provides the URL with an auth_code value that enables a single sign-on session.

Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.DomainNotWhitelistedException
QuickSight.Client.exceptions.QuickSightUserNotFoundException
QuickSight.Client.exceptions.IdentityTypeNotSupportedException
QuickSight.Client.exceptions.SessionLifetimeInMinutesInvalidException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'EmbedUrl': 'string',
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.DomainNotWhitelistedException
    QuickSight.Client.exceptions.QuickSightUserNotFoundException
    QuickSight.Client.exceptions.IdentityTypeNotSupportedException
    QuickSight.Client.exceptions.SessionLifetimeInMinutesInvalidException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
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

def list_dashboard_versions(AwsAccountId=None, DashboardId=None, NextToken=None, MaxResults=None):
    """
    Lists all the versions of the dashboards in the QuickSight subscription.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_dashboard_versions(
        AwsAccountId='string',
        DashboardId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the dashboard that you\'re listing versions for.\n

    :type DashboardId: string
    :param DashboardId: [REQUIRED]\nThe ID for the dashboard.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results, or null if there are no more results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned per request.

    :rtype: dict

ReturnsResponse Syntax
{
    'DashboardVersionSummaryList': [
        {
            'Arn': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'VersionNumber': 123,
            'Status': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
            'SourceEntityArn': 'string',
            'Description': 'string'
        },
    ],
    'NextToken': 'string',
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

DashboardVersionSummaryList (list) --
A structure that contains information about each version of the dashboard.

(dict) --
Dashboard version summary.

Arn (string) --
The Amazon Resource Name (ARN) of the resource.

CreatedTime (datetime) --
The time that this dashboard version was created.

VersionNumber (integer) --
Version number.

Status (string) --
The HTTP status of the request.

SourceEntityArn (string) --
Source entity ARN.

Description (string) --
Description.





NextToken (string) --
The token for the next set of results, or null if there are no more results.

Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidNextTokenException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'DashboardVersionSummaryList': [
            {
                'Arn': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'VersionNumber': 123,
                'Status': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
                'SourceEntityArn': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string',
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InvalidNextTokenException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def list_dashboards(AwsAccountId=None, NextToken=None, MaxResults=None):
    """
    Lists dashboards in an AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_dashboards(
        AwsAccountId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the dashboards that you\'re listing.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results, or null if there are no more results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned per request.

    :rtype: dict

ReturnsResponse Syntax
{
    'DashboardSummaryList': [
        {
            'Arn': 'string',
            'DashboardId': 'string',
            'Name': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1),
            'PublishedVersionNumber': 123,
            'LastPublishedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string',
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

DashboardSummaryList (list) --
A structure that contains all of the dashboards in your AWS account. This structure provides basic information about the dashboards.

(dict) --
Dashboard summary.

Arn (string) --
The Amazon Resource Name (ARN) of the resource.

DashboardId (string) --
Dashboard ID.

Name (string) --
A display name for the dashboard.

CreatedTime (datetime) --
The time that this dashboard was created.

LastUpdatedTime (datetime) --
The last time that this dashboard was updated.

PublishedVersionNumber (integer) --
Published version number.

LastPublishedTime (datetime) --
The last time that this dashboard was published.





NextToken (string) --
The token for the next set of results, or null if there are no more results.

Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidNextTokenException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'DashboardSummaryList': [
            {
                'Arn': 'string',
                'DashboardId': 'string',
                'Name': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1),
                'PublishedVersionNumber': 123,
                'LastPublishedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string',
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InvalidNextTokenException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def list_data_sets(AwsAccountId=None, NextToken=None, MaxResults=None):
    """
    Lists all of the datasets belonging to the current AWS account in an AWS Region.
    The permissions resource is arn:aws:quicksight:region:aws-account-id:dataset/* .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_data_sets(
        AwsAccountId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results, or null if there are no more results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned per request.

    :rtype: dict

ReturnsResponse Syntax
{
    'DataSetSummaries': [
        {
            'Arn': 'string',
            'DataSetId': 'string',
            'Name': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1),
            'ImportMode': 'SPICE'|'DIRECT_QUERY',
            'RowLevelPermissionDataSet': {
                'Arn': 'string',
                'PermissionPolicy': 'GRANT_ACCESS'|'DENY_ACCESS'
            }
        },
    ],
    'NextToken': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

DataSetSummaries (list) --
The list of dataset summaries.

(dict) --
Dataset summary.

Arn (string) --
The Amazon Resource Name (ARN) of the dataset.

DataSetId (string) --
The ID of the dataset.

Name (string) --
A display name for the dataset.

CreatedTime (datetime) --
The time that this dataset was created.

LastUpdatedTime (datetime) --
The last time that this dataset was updated.

ImportMode (string) --
Indicates whether you want to import the data into SPICE.

RowLevelPermissionDataSet (dict) --
The row-level security configuration for the dataset.

Arn (string) --
The Amazon Resource Name (ARN) of the permission dataset.

PermissionPolicy (string) --
Permission policy.







NextToken (string) --
The token for the next set of results, or null if there are no more results.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidNextTokenException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'DataSetSummaries': [
            {
                'Arn': 'string',
                'DataSetId': 'string',
                'Name': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1),
                'ImportMode': 'SPICE'|'DIRECT_QUERY',
                'RowLevelPermissionDataSet': {
                    'Arn': 'string',
                    'PermissionPolicy': 'GRANT_ACCESS'|'DENY_ACCESS'
                }
            },
        ],
        'NextToken': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InvalidNextTokenException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def list_data_sources(AwsAccountId=None, NextToken=None, MaxResults=None):
    """
    Lists data sources in current AWS Region that belong to this AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_data_sources(
        AwsAccountId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results, or null if there are no more results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned per request.

    :rtype: dict

ReturnsResponse Syntax
{
    'DataSources': [
        {
            'Arn': 'string',
            'DataSourceId': 'string',
            'Name': 'string',
            'Type': 'ADOBE_ANALYTICS'|'AMAZON_ELASTICSEARCH'|'ATHENA'|'AURORA'|'AURORA_POSTGRESQL'|'AWS_IOT_ANALYTICS'|'GITHUB'|'JIRA'|'MARIADB'|'MYSQL'|'POSTGRESQL'|'PRESTO'|'REDSHIFT'|'S3'|'SALESFORCE'|'SERVICENOW'|'SNOWFLAKE'|'SPARK'|'SQLSERVER'|'TERADATA'|'TWITTER',
            'Status': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
            'CreatedTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1),
            'DataSourceParameters': {
                'AmazonElasticsearchParameters': {
                    'Domain': 'string'
                },
                'AthenaParameters': {
                    'WorkGroup': 'string'
                },
                'AuroraParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string'
                },
                'AuroraPostgreSqlParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string'
                },
                'AwsIotAnalyticsParameters': {
                    'DataSetName': 'string'
                },
                'JiraParameters': {
                    'SiteBaseUrl': 'string'
                },
                'MariaDbParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string'
                },
                'MySqlParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string'
                },
                'PostgreSqlParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string'
                },
                'PrestoParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Catalog': 'string'
                },
                'RdsParameters': {
                    'InstanceId': 'string',
                    'Database': 'string'
                },
                'RedshiftParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string',
                    'ClusterId': 'string'
                },
                'S3Parameters': {
                    'ManifestFileLocation': {
                        'Bucket': 'string',
                        'Key': 'string'
                    }
                },
                'ServiceNowParameters': {
                    'SiteBaseUrl': 'string'
                },
                'SnowflakeParameters': {
                    'Host': 'string',
                    'Database': 'string',
                    'Warehouse': 'string'
                },
                'SparkParameters': {
                    'Host': 'string',
                    'Port': 123
                },
                'SqlServerParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string'
                },
                'TeradataParameters': {
                    'Host': 'string',
                    'Port': 123,
                    'Database': 'string'
                },
                'TwitterParameters': {
                    'Query': 'string',
                    'MaxRows': 123
                }
            },
            'VpcConnectionProperties': {
                'VpcConnectionArn': 'string'
            },
            'SslProperties': {
                'DisableSsl': True|False
            },
            'ErrorInfo': {
                'Type': 'TIMEOUT'|'ENGINE_VERSION_NOT_SUPPORTED'|'UNKNOWN_HOST'|'GENERIC_SQL_FAILURE'|'CONFLICT'|'UNKNOWN',
                'Message': 'string'
            }
        },
    ],
    'NextToken': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

DataSources (list) --
A list of data sources.

(dict) --
The structure of a data source.

Arn (string) --
The Amazon Resource Name (ARN) of the data source.

DataSourceId (string) --
The ID of the data source. This ID is unique per AWS Region for each AWS account.

Name (string) --
A display name for the data source.

Type (string) --
The type of the data source. This type indicates which database engine the data source connects to.

Status (string) --
The HTTP status of the request.

CreatedTime (datetime) --
The time that this data source was created.

LastUpdatedTime (datetime) --
The last time that this data source was updated.

DataSourceParameters (dict) --
The parameters that Amazon QuickSight uses to connect to your underlying source. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

AmazonElasticsearchParameters (dict) --
Amazon Elasticsearch Service parameters.

Domain (string) --
The Amazon Elasticsearch Service domain.



AthenaParameters (dict) --
Amazon Athena parameters.

WorkGroup (string) --
The workgroup that Amazon Athena uses.



AuroraParameters (dict) --
Amazon Aurora MySQL parameters.

Host (string) --
Host.

Port (integer) --
Port.

Database (string) --
Database.



AuroraPostgreSqlParameters (dict) --
Aurora PostgreSQL parameters.

Host (string) --
Host.

Port (integer) --
Port.

Database (string) --
Database.



AwsIotAnalyticsParameters (dict) --
AWS IoT Analytics parameters.

DataSetName (string) --
Dataset name.



JiraParameters (dict) --
Jira parameters.

SiteBaseUrl (string) --
The base URL of the Jira site.



MariaDbParameters (dict) --
MariaDB parameters.

Host (string) --
Host.

Port (integer) --
Port.

Database (string) --
Database.



MySqlParameters (dict) --
MySQL parameters.

Host (string) --
Host.

Port (integer) --
Port.

Database (string) --
Database.



PostgreSqlParameters (dict) --
PostgreSQL parameters.

Host (string) --
Host.

Port (integer) --
Port.

Database (string) --
Database.



PrestoParameters (dict) --
Presto parameters.

Host (string) --
Host.

Port (integer) --
Port.

Catalog (string) --
Catalog.



RdsParameters (dict) --
Amazon RDS parameters.

InstanceId (string) --
Instance ID.

Database (string) --
Database.



RedshiftParameters (dict) --
Amazon Redshift parameters.

Host (string) --
Host. This field can be blank if ClusterId is provided.

Port (integer) --
Port. This field can be blank if the ClusterId is provided.

Database (string) --
Database.

ClusterId (string) --
Cluster ID. This field can be blank if the Host and Port are provided.



S3Parameters (dict) --
S3 parameters.

ManifestFileLocation (dict) --
Location of the Amazon S3 manifest file. This is NULL if the manifest file was uploaded in the console.

Bucket (string) --
Amazon S3 bucket.

Key (string) --
Amazon S3 key that identifies an object.





ServiceNowParameters (dict) --
ServiceNow parameters.

SiteBaseUrl (string) --
URL of the base site.



SnowflakeParameters (dict) --
Snowflake parameters.

Host (string) --
Host.

Database (string) --
Database.

Warehouse (string) --
Warehouse.



SparkParameters (dict) --
Spark parameters.

Host (string) --
Host.

Port (integer) --
Port.



SqlServerParameters (dict) --
SQL Server parameters.

Host (string) --
Host.

Port (integer) --
Port.

Database (string) --
Database.



TeradataParameters (dict) --
Teradata parameters.

Host (string) --
Host.

Port (integer) --
Port.

Database (string) --
Database.



TwitterParameters (dict) --
Twitter parameters.

Query (string) --
Twitter query string.

MaxRows (integer) --
Maximum number of rows to query Twitter.





VpcConnectionProperties (dict) --
The VPC connection information. You need to use this parameter only when you want QuickSight to use a VPC connection when connecting to your underlying source.

VpcConnectionArn (string) --
The Amazon Resource Name (ARN) for the VPC connection.



SslProperties (dict) --
Secure Socket Layer (SSL) properties that apply when QuickSight connects to your underlying source.

DisableSsl (boolean) --
A Boolean option to control whether SSL should be disabled.



ErrorInfo (dict) --
Error information from the last update or the creation of the data source.

Type (string) --
Error type.

Message (string) --
Error message.







NextToken (string) --
The token for the next set of results, or null if there are no more results.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidNextTokenException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'DataSources': [
            {
                'Arn': 'string',
                'DataSourceId': 'string',
                'Name': 'string',
                'Type': 'ADOBE_ANALYTICS'|'AMAZON_ELASTICSEARCH'|'ATHENA'|'AURORA'|'AURORA_POSTGRESQL'|'AWS_IOT_ANALYTICS'|'GITHUB'|'JIRA'|'MARIADB'|'MYSQL'|'POSTGRESQL'|'PRESTO'|'REDSHIFT'|'S3'|'SALESFORCE'|'SERVICENOW'|'SNOWFLAKE'|'SPARK'|'SQLSERVER'|'TERADATA'|'TWITTER',
                'Status': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
                'CreatedTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1),
                'DataSourceParameters': {
                    'AmazonElasticsearchParameters': {
                        'Domain': 'string'
                    },
                    'AthenaParameters': {
                        'WorkGroup': 'string'
                    },
                    'AuroraParameters': {
                        'Host': 'string',
                        'Port': 123,
                        'Database': 'string'
                    },
                    'AuroraPostgreSqlParameters': {
                        'Host': 'string',
                        'Port': 123,
                        'Database': 'string'
                    },
                    'AwsIotAnalyticsParameters': {
                        'DataSetName': 'string'
                    },
                    'JiraParameters': {
                        'SiteBaseUrl': 'string'
                    },
                    'MariaDbParameters': {
                        'Host': 'string',
                        'Port': 123,
                        'Database': 'string'
                    },
                    'MySqlParameters': {
                        'Host': 'string',
                        'Port': 123,
                        'Database': 'string'
                    },
                    'PostgreSqlParameters': {
                        'Host': 'string',
                        'Port': 123,
                        'Database': 'string'
                    },
                    'PrestoParameters': {
                        'Host': 'string',
                        'Port': 123,
                        'Catalog': 'string'
                    },
                    'RdsParameters': {
                        'InstanceId': 'string',
                        'Database': 'string'
                    },
                    'RedshiftParameters': {
                        'Host': 'string',
                        'Port': 123,
                        'Database': 'string',
                        'ClusterId': 'string'
                    },
                    'S3Parameters': {
                        'ManifestFileLocation': {
                            'Bucket': 'string',
                            'Key': 'string'
                        }
                    },
                    'ServiceNowParameters': {
                        'SiteBaseUrl': 'string'
                    },
                    'SnowflakeParameters': {
                        'Host': 'string',
                        'Database': 'string',
                        'Warehouse': 'string'
                    },
                    'SparkParameters': {
                        'Host': 'string',
                        'Port': 123
                    },
                    'SqlServerParameters': {
                        'Host': 'string',
                        'Port': 123,
                        'Database': 'string'
                    },
                    'TeradataParameters': {
                        'Host': 'string',
                        'Port': 123,
                        'Database': 'string'
                    },
                    'TwitterParameters': {
                        'Query': 'string',
                        'MaxRows': 123
                    }
                },
                'VpcConnectionProperties': {
                    'VpcConnectionArn': 'string'
                },
                'SslProperties': {
                    'DisableSsl': True|False
                },
                'ErrorInfo': {
                    'Type': 'TIMEOUT'|'ENGINE_VERSION_NOT_SUPPORTED'|'UNKNOWN_HOST'|'GENERIC_SQL_FAILURE'|'CONFLICT'|'UNKNOWN',
                    'Message': 'string'
                }
            },
        ],
        'NextToken': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InvalidNextTokenException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def list_group_memberships(GroupName=None, NextToken=None, MaxResults=None, AwsAccountId=None, Namespace=None):
    """
    Lists member users in a group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_group_memberships(
        GroupName='string',
        NextToken='string',
        MaxResults=123,
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group that you want to see a membership list of.\n

    :type NextToken: string
    :param NextToken: A pagination token that can be used in a subsequent request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return from this request.

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GroupMemberList': [
        {
            'Arn': 'string',
            'MemberName': 'string'
        },
    ],
    'NextToken': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

GroupMemberList (list) --
The list of the members of the group.

(dict) --
A member of an Amazon QuickSight group. Currently, group members must be users. Groups can\'t be members of another group. .

Arn (string) --
The Amazon Resource Name (ARN) for the group member (user).

MemberName (string) --
The name of the group member (user).





NextToken (string) --
A pagination token that can be used in a subsequent request.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidNextTokenException
QuickSight.Client.exceptions.PreconditionNotMetException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'GroupMemberList': [
            {
                'Arn': 'string',
                'MemberName': 'string'
            },
        ],
        'NextToken': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InvalidNextTokenException
    QuickSight.Client.exceptions.PreconditionNotMetException
    QuickSight.Client.exceptions.InternalFailureException
    QuickSight.Client.exceptions.ResourceUnavailableException
    
    """
    pass

def list_groups(AwsAccountId=None, NextToken=None, MaxResults=None, Namespace=None):
    """
    Lists all user groups in Amazon QuickSight.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_groups(
        AwsAccountId='string',
        NextToken='string',
        MaxResults=123,
        Namespace='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type NextToken: string
    :param NextToken: A pagination token that can be used in a subsequent request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GroupList': [
        {
            'Arn': 'string',
            'GroupName': 'string',
            'Description': 'string',
            'PrincipalId': 'string'
        },
    ],
    'NextToken': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

GroupList (list) --
The list of the groups.

(dict) --
A group in Amazon QuickSight consists of a set of users. You can use groups to make it easier to manage access and security. Currently, an Amazon QuickSight subscription can\'t contain more than 500 Amazon QuickSight groups.

Arn (string) --
The Amazon Resource Name (ARN) for the group.

GroupName (string) --
The name of the group.

Description (string) --
The group description.

PrincipalId (string) --
The principal ID of the group.





NextToken (string) --
A pagination token that can be used in a subsequent request.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidNextTokenException
QuickSight.Client.exceptions.PreconditionNotMetException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'GroupList': [
            {
                'Arn': 'string',
                'GroupName': 'string',
                'Description': 'string',
                'PrincipalId': 'string'
            },
        ],
        'NextToken': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InvalidNextTokenException
    QuickSight.Client.exceptions.PreconditionNotMetException
    QuickSight.Client.exceptions.InternalFailureException
    QuickSight.Client.exceptions.ResourceUnavailableException
    
    """
    pass

def list_iam_policy_assignments(AwsAccountId=None, AssignmentStatus=None, Namespace=None, NextToken=None, MaxResults=None):
    """
    Lists IAM policy assignments in the current Amazon QuickSight account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_iam_policy_assignments(
        AwsAccountId='string',
        AssignmentStatus='ENABLED'|'DRAFT'|'DISABLED',
        Namespace='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains these IAM policy assignments.\n

    :type AssignmentStatus: string
    :param AssignmentStatus: The status of the assignments.

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace for the assignments.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results, or null if there are no more results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned per request.

    :rtype: dict

ReturnsResponse Syntax
{
    'IAMPolicyAssignments': [
        {
            'AssignmentName': 'string',
            'AssignmentStatus': 'ENABLED'|'DRAFT'|'DISABLED'
        },
    ],
    'NextToken': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

IAMPolicyAssignments (list) --
Information describing the IAM policy assignments.

(dict) --
IAM policy assignment summary.

AssignmentName (string) --
Assignment name.

AssignmentStatus (string) --
Assignment status.





NextToken (string) --
The token for the next set of results, or null if there are no more results.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidNextTokenException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'IAMPolicyAssignments': [
            {
                'AssignmentName': 'string',
                'AssignmentStatus': 'ENABLED'|'DRAFT'|'DISABLED'
            },
        ],
        'NextToken': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InvalidNextTokenException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def list_iam_policy_assignments_for_user(AwsAccountId=None, UserName=None, NextToken=None, MaxResults=None, Namespace=None):
    """
    Lists all the IAM policy assignments, including the Amazon Resource Names (ARNs) for the IAM policies assigned to the specified user and group or groups that the user belongs to.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_iam_policy_assignments_for_user(
        AwsAccountId='string',
        UserName='string',
        NextToken='string',
        MaxResults=123,
        Namespace='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the assignments.\n

    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results, or null if there are no more results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned per request.

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace of the assignment.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ActiveAssignments': [
        {
            'AssignmentName': 'string',
            'PolicyArn': 'string'
        },
    ],
    'RequestId': 'string',
    'NextToken': 'string',
    'Status': 123
}


Response Structure

(dict) --

ActiveAssignments (list) --
The active assignments for this user.

(dict) --
The active AWS Identity and Access Management (IAM) policy assignment.

AssignmentName (string) --
A name for the IAM policy assignment.

PolicyArn (string) --
The Amazon Resource Name (ARN) of the resource.





RequestId (string) --
The AWS request ID for this operation.

NextToken (string) --
The token for the next set of results, or null if there are no more results.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ConcurrentUpdatingException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'ActiveAssignments': [
            {
                'AssignmentName': 'string',
                'PolicyArn': 'string'
            },
        ],
        'RequestId': 'string',
        'NextToken': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ConcurrentUpdatingException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def list_ingestions(DataSetId=None, NextToken=None, AwsAccountId=None, MaxResults=None):
    """
    Lists the history of SPICE ingestions for a dataset.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_ingestions(
        DataSetId='string',
        NextToken='string',
        AwsAccountId='string',
        MaxResults=123
    )
    
    
    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe ID of the dataset used in the ingestion.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results, or null if there are no more results.

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned per request.

    :rtype: dict

ReturnsResponse Syntax
{
    'Ingestions': [
        {
            'Arn': 'string',
            'IngestionId': 'string',
            'IngestionStatus': 'INITIALIZED'|'QUEUED'|'RUNNING'|'FAILED'|'COMPLETED'|'CANCELLED',
            'ErrorInfo': {
                'Type': 'FAILURE_TO_ASSUME_ROLE'|'INGESTION_SUPERSEDED'|'INGESTION_CANCELED'|'DATA_SET_DELETED'|'DATA_SET_NOT_SPICE'|'S3_UPLOADED_FILE_DELETED'|'S3_MANIFEST_ERROR'|'DATA_TOLERANCE_EXCEPTION'|'SPICE_TABLE_NOT_FOUND'|'DATA_SET_SIZE_LIMIT_EXCEEDED'|'ROW_SIZE_LIMIT_EXCEEDED'|'ACCOUNT_CAPACITY_LIMIT_EXCEEDED'|'CUSTOMER_ERROR'|'DATA_SOURCE_NOT_FOUND'|'IAM_ROLE_NOT_AVAILABLE'|'CONNECTION_FAILURE'|'SQL_TABLE_NOT_FOUND'|'PERMISSION_DENIED'|'SSL_CERTIFICATE_VALIDATION_FAILURE'|'OAUTH_TOKEN_FAILURE'|'SOURCE_API_LIMIT_EXCEEDED_FAILURE'|'PASSWORD_AUTHENTICATION_FAILURE'|'SQL_SCHEMA_MISMATCH_ERROR'|'INVALID_DATE_FORMAT'|'INVALID_DATAPREP_SYNTAX'|'SOURCE_RESOURCE_LIMIT_EXCEEDED'|'SQL_INVALID_PARAMETER_VALUE'|'QUERY_TIMEOUT'|'SQL_NUMERIC_OVERFLOW'|'UNRESOLVABLE_HOST'|'UNROUTABLE_HOST'|'SQL_EXCEPTION'|'S3_FILE_INACCESSIBLE'|'IOT_FILE_NOT_FOUND'|'IOT_DATA_SET_FILE_EMPTY'|'INVALID_DATA_SOURCE_CONFIG'|'DATA_SOURCE_AUTH_FAILED'|'DATA_SOURCE_CONNECTION_FAILED'|'FAILURE_TO_PROCESS_JSON_FILE'|'INTERNAL_SERVICE_ERROR',
                'Message': 'string'
            },
            'RowInfo': {
                'RowsIngested': 123,
                'RowsDropped': 123
            },
            'QueueInfo': {
                'WaitingOnIngestion': 'string',
                'QueuedIngestion': 'string'
            },
            'CreatedTime': datetime(2015, 1, 1),
            'IngestionTimeInSeconds': 123,
            'IngestionSizeInBytes': 123,
            'RequestSource': 'MANUAL'|'SCHEDULED',
            'RequestType': 'INITIAL_INGESTION'|'EDIT'|'INCREMENTAL_REFRESH'|'FULL_REFRESH'
        },
    ],
    'NextToken': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

Ingestions (list) --
A list of the ingestions.

(dict) --
Information about the SPICE ingestion for a dataset.

Arn (string) --
The Amazon Resource Name (ARN) of the resource.

IngestionId (string) --
Ingestion ID.

IngestionStatus (string) --
Ingestion status.

ErrorInfo (dict) --
Error information for this ingestion.

Type (string) --
Error type.

Message (string) --
Error message.



RowInfo (dict) --
Information about rows for a data set SPICE ingestion.

RowsIngested (integer) --
The number of rows that were ingested.

RowsDropped (integer) --
The number of rows that were not ingested.



QueueInfo (dict) --
Information about a queued dataset SPICE ingestion.

WaitingOnIngestion (string) --
The ID of the queued ingestion.

QueuedIngestion (string) --
The ID of the ongoing ingestion. The queued ingestion is waiting for the ongoing ingestion to complete.



CreatedTime (datetime) --
The time that this ingestion started.

IngestionTimeInSeconds (integer) --
The time that this ingestion took, measured in seconds.

IngestionSizeInBytes (integer) --
The size of the data ingested, in bytes.

RequestSource (string) --
Event source for this ingestion.

RequestType (string) --
Type of this ingestion.





NextToken (string) --
The token for the next set of results, or null if there are no more results.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.InvalidNextTokenException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Ingestions': [
            {
                'Arn': 'string',
                'IngestionId': 'string',
                'IngestionStatus': 'INITIALIZED'|'QUEUED'|'RUNNING'|'FAILED'|'COMPLETED'|'CANCELLED',
                'ErrorInfo': {
                    'Type': 'FAILURE_TO_ASSUME_ROLE'|'INGESTION_SUPERSEDED'|'INGESTION_CANCELED'|'DATA_SET_DELETED'|'DATA_SET_NOT_SPICE'|'S3_UPLOADED_FILE_DELETED'|'S3_MANIFEST_ERROR'|'DATA_TOLERANCE_EXCEPTION'|'SPICE_TABLE_NOT_FOUND'|'DATA_SET_SIZE_LIMIT_EXCEEDED'|'ROW_SIZE_LIMIT_EXCEEDED'|'ACCOUNT_CAPACITY_LIMIT_EXCEEDED'|'CUSTOMER_ERROR'|'DATA_SOURCE_NOT_FOUND'|'IAM_ROLE_NOT_AVAILABLE'|'CONNECTION_FAILURE'|'SQL_TABLE_NOT_FOUND'|'PERMISSION_DENIED'|'SSL_CERTIFICATE_VALIDATION_FAILURE'|'OAUTH_TOKEN_FAILURE'|'SOURCE_API_LIMIT_EXCEEDED_FAILURE'|'PASSWORD_AUTHENTICATION_FAILURE'|'SQL_SCHEMA_MISMATCH_ERROR'|'INVALID_DATE_FORMAT'|'INVALID_DATAPREP_SYNTAX'|'SOURCE_RESOURCE_LIMIT_EXCEEDED'|'SQL_INVALID_PARAMETER_VALUE'|'QUERY_TIMEOUT'|'SQL_NUMERIC_OVERFLOW'|'UNRESOLVABLE_HOST'|'UNROUTABLE_HOST'|'SQL_EXCEPTION'|'S3_FILE_INACCESSIBLE'|'IOT_FILE_NOT_FOUND'|'IOT_DATA_SET_FILE_EMPTY'|'INVALID_DATA_SOURCE_CONFIG'|'DATA_SOURCE_AUTH_FAILED'|'DATA_SOURCE_CONNECTION_FAILED'|'FAILURE_TO_PROCESS_JSON_FILE'|'INTERNAL_SERVICE_ERROR',
                    'Message': 'string'
                },
                'RowInfo': {
                    'RowsIngested': 123,
                    'RowsDropped': 123
                },
                'QueueInfo': {
                    'WaitingOnIngestion': 'string',
                    'QueuedIngestion': 'string'
                },
                'CreatedTime': datetime(2015, 1, 1),
                'IngestionTimeInSeconds': 123,
                'IngestionSizeInBytes': 123,
                'RequestSource': 'MANUAL'|'SCHEDULED',
                'RequestType': 'INITIAL_INGESTION'|'EDIT'|'INCREMENTAL_REFRESH'|'FULL_REFRESH'
            },
        ],
        'NextToken': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.InvalidNextTokenException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Lists the tags assigned to a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource that you want a list of tags for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --
Tags (list) --Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.

(dict) --The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.

Key (string) --Tag key.

Value (string) --Tag value.





RequestId (string) --The AWS request ID for this operation.

Status (integer) --The HTTP status of the request.






Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'RequestId': 'string',
        'Status': 123
    }
    
    
    """
    pass

def list_template_aliases(AwsAccountId=None, TemplateId=None, NextToken=None, MaxResults=None):
    """
    Lists all the aliases of a template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_template_aliases(
        AwsAccountId='string',
        TemplateId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the template aliases that you\'re listing.\n

    :type TemplateId: string
    :param TemplateId: [REQUIRED]\nThe ID for the template.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results, or null if there are no more results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned per request.

    :rtype: dict

ReturnsResponse Syntax
{
    'TemplateAliasList': [
        {
            'AliasName': 'string',
            'Arn': 'string',
            'TemplateVersionNumber': 123
        },
    ],
    'Status': 123,
    'RequestId': 'string',
    'NextToken': 'string'
}


Response Structure

(dict) --

TemplateAliasList (list) --
A structure containing the list of the template\'s aliases.

(dict) --
The template alias.

AliasName (string) --
The display name of the template alias.

Arn (string) --
The Amazon Resource Name (ARN) of the template alias.

TemplateVersionNumber (integer) --
The version number of the template alias.





Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.

NextToken (string) --
The token for the next set of results, or null if there are no more results.







Exceptions

QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'TemplateAliasList': [
            {
                'AliasName': 'string',
                'Arn': 'string',
                'TemplateVersionNumber': 123
            },
        ],
        'Status': 123,
        'RequestId': 'string',
        'NextToken': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def list_template_versions(AwsAccountId=None, TemplateId=None, NextToken=None, MaxResults=None):
    """
    Lists all the versions of the templates in the current Amazon QuickSight account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_template_versions(
        AwsAccountId='string',
        TemplateId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the templates that you\'re listing.\n

    :type TemplateId: string
    :param TemplateId: [REQUIRED]\nThe ID for the template.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results, or null if there are no more results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned per request.

    :rtype: dict

ReturnsResponse Syntax
{
    'TemplateVersionSummaryList': [
        {
            'Arn': 'string',
            'VersionNumber': 123,
            'CreatedTime': datetime(2015, 1, 1),
            'Status': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
            'Description': 'string'
        },
    ],
    'NextToken': 'string',
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

TemplateVersionSummaryList (list) --
A structure containing a list of all the versions of the specified template.

(dict) --
The template version.

Arn (string) --
The Amazon Resource Name (ARN) of the template version.

VersionNumber (integer) --
The version number of the template version.

CreatedTime (datetime) --
The time that this template version was created.

Status (string) --
The status of the template version.

Description (string) --
The description of the template version.





NextToken (string) --
The token for the next set of results, or null if there are no more results.

Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.InvalidNextTokenException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'TemplateVersionSummaryList': [
            {
                'Arn': 'string',
                'VersionNumber': 123,
                'CreatedTime': datetime(2015, 1, 1),
                'Status': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
                'Description': 'string'
            },
        ],
        'NextToken': 'string',
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.InvalidNextTokenException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def list_templates(AwsAccountId=None, NextToken=None, MaxResults=None):
    """
    Lists all the templates in the current Amazon QuickSight account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_templates(
        AwsAccountId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the templates that you\'re listing.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results, or null if there are no more results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned per request.

    :rtype: dict

ReturnsResponse Syntax
{
    'TemplateSummaryList': [
        {
            'Arn': 'string',
            'TemplateId': 'string',
            'Name': 'string',
            'LatestVersionNumber': 123,
            'CreatedTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string',
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

TemplateSummaryList (list) --
A structure containing information about the templates in the list.

(dict) --
The template summary.

Arn (string) --
A summary of a template.

TemplateId (string) --
The ID of the template. This ID is unique per AWS Region for each AWS account.

Name (string) --
A display name for the template.

LatestVersionNumber (integer) --
A structure containing a list of version numbers for the template summary.

CreatedTime (datetime) --
The last time that this template was created.

LastUpdatedTime (datetime) --
The last time that this template was updated.





NextToken (string) --
The token for the next set of results, or null if there are no more results.

Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.InvalidNextTokenException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'TemplateSummaryList': [
            {
                'Arn': 'string',
                'TemplateId': 'string',
                'Name': 'string',
                'LatestVersionNumber': 123,
                'CreatedTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string',
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.InvalidNextTokenException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def list_user_groups(UserName=None, AwsAccountId=None, Namespace=None, NextToken=None, MaxResults=None):
    """
    Lists the Amazon QuickSight groups that an Amazon QuickSight user is a member of.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_user_groups(
        UserName='string',
        AwsAccountId='string',
        Namespace='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe Amazon QuickSight user name that you want to list group memberships for.\n

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :type NextToken: string
    :param NextToken: A pagination token that can be used in a subsequent request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return from this request.

    :rtype: dict

ReturnsResponse Syntax
{
    'GroupList': [
        {
            'Arn': 'string',
            'GroupName': 'string',
            'Description': 'string',
            'PrincipalId': 'string'
        },
    ],
    'NextToken': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

GroupList (list) --
The list of groups the user is a member of.

(dict) --
A group in Amazon QuickSight consists of a set of users. You can use groups to make it easier to manage access and security. Currently, an Amazon QuickSight subscription can\'t contain more than 500 Amazon QuickSight groups.

Arn (string) --
The Amazon Resource Name (ARN) for the group.

GroupName (string) --
The name of the group.

Description (string) --
The group description.

PrincipalId (string) --
The principal ID of the group.





NextToken (string) --
A pagination token that can be used in a subsequent request.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'GroupList': [
            {
                'Arn': 'string',
                'GroupName': 'string',
                'Description': 'string',
                'PrincipalId': 'string'
            },
        ],
        'NextToken': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InternalFailureException
    QuickSight.Client.exceptions.ResourceUnavailableException
    
    """
    pass

def list_users(AwsAccountId=None, NextToken=None, MaxResults=None, Namespace=None):
    """
    Returns a list of all of the Amazon QuickSight users belonging to this account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_users(
        AwsAccountId='string',
        NextToken='string',
        MaxResults=123,
        Namespace='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type NextToken: string
    :param NextToken: A pagination token that can be used in a subsequent request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return from this request.

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UserList': [
        {
            'Arn': 'string',
            'UserName': 'string',
            'Email': 'string',
            'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
            'IdentityType': 'IAM'|'QUICKSIGHT',
            'Active': True|False,
            'PrincipalId': 'string'
        },
    ],
    'NextToken': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

UserList (list) --
The list of users.

(dict) --
A registered user of Amazon QuickSight. Currently, an Amazon QuickSight subscription can\'t contain more than 20 million users.

Arn (string) --
The Amazon Resource Name (ARN) for the user.

UserName (string) --
The user\'s user name.

Email (string) --
The user\'s email address.

Role (string) --
The Amazon QuickSight role for the user. The user role can be one of the following:.

READER : A user who has read-only access to dashboards.
AUTHOR : A user who can create data sources, datasets, analyses, and dashboards.
ADMIN : A user who is an author, who can also manage Amazon QuickSight settings.
RESTRICTED_READER : This role isn\'t currently available for use.
RESTRICTED_AUTHOR : This role isn\'t currently available for use.


IdentityType (string) --
The type of identity authentication used by the user.

Active (boolean) --
The active status of user. When you create an Amazon QuickSight user that\xe2\x80\x99s not an IAM user or an Active Directory user, that user is inactive until they sign in and provide a password.

PrincipalId (string) --
The principal ID of the user.





NextToken (string) --
A pagination token that can be used in a subsequent request.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidNextTokenException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'UserList': [
            {
                'Arn': 'string',
                'UserName': 'string',
                'Email': 'string',
                'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
                'IdentityType': 'IAM'|'QUICKSIGHT',
                'Active': True|False,
                'PrincipalId': 'string'
            },
        ],
        'NextToken': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    READER : A user who has read-only access to dashboards.
    AUTHOR : A user who can create data sources, datasets, analyses, and dashboards.
    ADMIN : A user who is an author, who can also manage Amazon QuickSight settings.
    RESTRICTED_READER : This role isn\'t currently available for use.
    RESTRICTED_AUTHOR : This role isn\'t currently available for use.
    
    """
    pass

def register_user(IdentityType=None, Email=None, UserRole=None, IamArn=None, SessionName=None, AwsAccountId=None, Namespace=None, UserName=None):
    """
    Creates an Amazon QuickSight user, whose identity is associated with the AWS Identity and Access Management (IAM) identity or role specified in the request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_user(
        IdentityType='IAM'|'QUICKSIGHT',
        Email='string',
        UserRole='ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
        IamArn='string',
        SessionName='string',
        AwsAccountId='string',
        Namespace='string',
        UserName='string'
    )
    
    
    :type IdentityType: string
    :param IdentityType: [REQUIRED]\nAmazon QuickSight supports several ways of managing the identity of users. This parameter accepts two values:\n\nIAM : A user whose identity maps to an existing IAM user or role.\nQUICKSIGHT : A user whose identity is owned and managed internally by Amazon QuickSight.\n\n

    :type Email: string
    :param Email: [REQUIRED]\nThe email address of the user that you want to register.\n

    :type UserRole: string
    :param UserRole: [REQUIRED]\nThe Amazon QuickSight role for the user. The user role can be one of the following:\n\nREADER : A user who has read-only access to dashboards.\nAUTHOR : A user who can create data sources, datasets, analyses, and dashboards.\nADMIN : A user who is an author, who can also manage Amazon QuickSight settings.\nRESTRICTED_READER : This role isn\'t currently available for use.\nRESTRICTED_AUTHOR : This role isn\'t currently available for use.\n\n

    :type IamArn: string
    :param IamArn: The ARN of the IAM user or role that you are registering with Amazon QuickSight.

    :type SessionName: string
    :param SessionName: You need to use this parameter only when you register one or more users using an assumed IAM role. You don\'t need to provide the session name for other scenarios, for example when you are registering an IAM user or an Amazon QuickSight user. You can register multiple users using the same IAM role if each user has a different session name. For more information on assuming IAM roles, see ` assume-role https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role.html`__ in the AWS CLI Reference.

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :type UserName: string
    :param UserName: The Amazon QuickSight user name that you want to create for the user you are registering.

    :rtype: dict

ReturnsResponse Syntax
{
    'User': {
        'Arn': 'string',
        'UserName': 'string',
        'Email': 'string',
        'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
        'IdentityType': 'IAM'|'QUICKSIGHT',
        'Active': True|False,
        'PrincipalId': 'string'
    },
    'UserInvitationUrl': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

User (dict) --
The user name.

Arn (string) --
The Amazon Resource Name (ARN) for the user.

UserName (string) --
The user\'s user name.

Email (string) --
The user\'s email address.

Role (string) --
The Amazon QuickSight role for the user. The user role can be one of the following:.

READER : A user who has read-only access to dashboards.
AUTHOR : A user who can create data sources, datasets, analyses, and dashboards.
ADMIN : A user who is an author, who can also manage Amazon QuickSight settings.
RESTRICTED_READER : This role isn\'t currently available for use.
RESTRICTED_AUTHOR : This role isn\'t currently available for use.


IdentityType (string) --
The type of identity authentication used by the user.

Active (boolean) --
The active status of user. When you create an Amazon QuickSight user that\xe2\x80\x99s not an IAM user or an Active Directory user, that user is inactive until they sign in and provide a password.

PrincipalId (string) --
The principal ID of the user.



UserInvitationUrl (string) --
The URL the user visits to complete registration and provide a password. This is returned only for users with an identity type of QUICKSIGHT .

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.LimitExceededException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.PreconditionNotMetException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'User': {
            'Arn': 'string',
            'UserName': 'string',
            'Email': 'string',
            'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
            'IdentityType': 'IAM'|'QUICKSIGHT',
            'Active': True|False,
            'PrincipalId': 'string'
        },
        'UserInvitationUrl': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    READER : A user who has read-only access to dashboards.
    AUTHOR : A user who can create data sources, datasets, analyses, and dashboards.
    ADMIN : A user who is an author, who can also manage Amazon QuickSight settings.
    RESTRICTED_READER : This role isn\'t currently available for use.
    RESTRICTED_AUTHOR : This role isn\'t currently available for use.
    
    """
    pass

def search_dashboards(AwsAccountId=None, Filters=None, NextToken=None, MaxResults=None):
    """
    Searchs for dashboards that belong to a user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.search_dashboards(
        AwsAccountId='string',
        Filters=[
            {
                'Operator': 'StringEquals',
                'Name': 'QUICKSIGHT_USER',
                'Value': 'string'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the user whose dashboards you\'re searching for.\n

    :type Filters: list
    :param Filters: [REQUIRED]\nThe filters to apply to the search. Currently, you can search only by user name. For example, 'Filters': [ { 'Name': 'QUICKSIGHT_USER', 'Operator': 'StringEquals', 'Value': 'arn:aws:quicksight:us-east-1:1:user/default/UserName1' } ]\n\n(dict) --A filter that you apply when searching for dashboards.\n\nOperator (string) -- [REQUIRED]The comparison operator that you want to use as a filter. For example, 'Operator': 'StringEquals' .\n\nName (string) --The name of the value that you want to use as a filter. For example, 'Name': 'QUICKSIGHT_USER' .\n\nValue (string) --The value of the named item, in this case QUICKSIGHT_USER , that you want to use as a filter. For example, 'Value': 'arn:aws:quicksight:us-east-1:1:user/default/UserName1' .\n\n\n\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of results, or null if there are no more results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned per request.

    :rtype: dict

ReturnsResponse Syntax
{
    'DashboardSummaryList': [
        {
            'Arn': 'string',
            'DashboardId': 'string',
            'Name': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1),
            'PublishedVersionNumber': 123,
            'LastPublishedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string',
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

DashboardSummaryList (list) --
The list of dashboards owned by the user specified in Filters in your request.

(dict) --
Dashboard summary.

Arn (string) --
The Amazon Resource Name (ARN) of the resource.

DashboardId (string) --
Dashboard ID.

Name (string) --
A display name for the dashboard.

CreatedTime (datetime) --
The time that this dashboard was created.

LastUpdatedTime (datetime) --
The last time that this dashboard was updated.

PublishedVersionNumber (integer) --
Published version number.

LastPublishedTime (datetime) --
The last time that this dashboard was published.





NextToken (string) --
The token for the next set of results, or null if there are no more results.

Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InvalidNextTokenException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'DashboardSummaryList': [
            {
                'Arn': 'string',
                'DashboardId': 'string',
                'Name': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1),
                'PublishedVersionNumber': 123,
                'LastPublishedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string',
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InvalidNextTokenException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Assigns one or more tags (key-value pairs) to the specified QuickSight resource.
    Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values. You can use the TagResource operation with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.
    You can associate as many as 50 tags with a resource. QuickSight supports tagging on data set, data source, dashboard, and template.
    Tagging for QuickSight works in a similar way to tagging for other AWS services, except for the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource that you want to tag.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nContains a map of the key-value pairs for the resource tag or tags assigned to the resource.\n\n(dict) --The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.\n\nKey (string) -- [REQUIRED]Tag key.\n\nValue (string) -- [REQUIRED]Tag value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.LimitExceededException
QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    ResourceArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of the resource that you want to tag.
    
    Tags (list) -- [REQUIRED]
    Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.
    
    (dict) --The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.
    
    Key (string) -- [REQUIRED]Tag key.
    
    Value (string) -- [REQUIRED]Tag value.
    
    
    
    
    
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes a tag or tags from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource that you want to untag.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe keys of the key-value pairs for the resource tag or tags assigned to the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def update_dashboard(AwsAccountId=None, DashboardId=None, Name=None, SourceEntity=None, Parameters=None, VersionDescription=None, DashboardPublishOptions=None):
    """
    Updates a dashboard in an AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_dashboard(
        AwsAccountId='string',
        DashboardId='string',
        Name='string',
        SourceEntity={
            'SourceTemplate': {
                'DataSetReferences': [
                    {
                        'DataSetPlaceholder': 'string',
                        'DataSetArn': 'string'
                    },
                ],
                'Arn': 'string'
            }
        },
        Parameters={
            'StringParameters': [
                {
                    'Name': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            'IntegerParameters': [
                {
                    'Name': 'string',
                    'Values': [
                        123,
                    ]
                },
            ],
            'DecimalParameters': [
                {
                    'Name': 'string',
                    'Values': [
                        123.0,
                    ]
                },
            ],
            'DateTimeParameters': [
                {
                    'Name': 'string',
                    'Values': [
                        datetime(2015, 1, 1),
                    ]
                },
            ]
        },
        VersionDescription='string',
        DashboardPublishOptions={
            'AdHocFilteringOption': {
                'AvailabilityStatus': 'ENABLED'|'DISABLED'
            },
            'ExportToCSVOption': {
                'AvailabilityStatus': 'ENABLED'|'DISABLED'
            },
            'SheetControlsOption': {
                'VisibilityState': 'EXPANDED'|'COLLAPSED'
            }
        }
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the dashboard that you\'re updating.\n

    :type DashboardId: string
    :param DashboardId: [REQUIRED]\nThe ID for the dashboard.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe display name of the dashboard.\n

    :type SourceEntity: dict
    :param SourceEntity: [REQUIRED]\nThe template or analysis from which the dashboard is created. The SouceTemplate entity accepts the Amazon Resource Name (ARN) of the template and also references to replacement datasets for the placeholders set when creating the template. The replacement datasets need to follow the same schema as the datasets for which placeholders were created when creating the template.\n\nSourceTemplate (dict) --Source template.\n\nDataSetReferences (list) -- [REQUIRED]Dataset references.\n\n(dict) --Dataset reference.\n\nDataSetPlaceholder (string) -- [REQUIRED]Dataset placeholder.\n\nDataSetArn (string) -- [REQUIRED]Dataset Amazon Resource Name (ARN).\n\n\n\n\n\nArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the resource.\n\n\n\n\n

    :type Parameters: dict
    :param Parameters: A structure that contains the parameters of the dashboard.\n\nStringParameters (list) --String parameters.\n\n(dict) --String parameter.\n\nName (string) -- [REQUIRED]A display name for the dataset.\n\nValues (list) -- [REQUIRED]Values.\n\n(string) --\n\n\n\n\n\n\nIntegerParameters (list) --Integer parameters.\n\n(dict) --Integer parameter.\n\nName (string) -- [REQUIRED]A display name for the dataset.\n\nValues (list) -- [REQUIRED]Values.\n\n(integer) --\n\n\n\n\n\n\nDecimalParameters (list) --Decimal parameters.\n\n(dict) --Decimal parameter.\n\nName (string) -- [REQUIRED]A display name for the dataset.\n\nValues (list) -- [REQUIRED]Values.\n\n(float) --\n\n\n\n\n\n\nDateTimeParameters (list) --DateTime parameters.\n\n(dict) --Date time parameter.\n\nName (string) -- [REQUIRED]A display name for the dataset.\n\nValues (list) -- [REQUIRED]Values.\n\n(datetime) --\n\n\n\n\n\n\n\n

    :type VersionDescription: string
    :param VersionDescription: A description for the first version of the dashboard being created.

    :type DashboardPublishOptions: dict
    :param DashboardPublishOptions: Options for publishing the dashboard when you create it:\n\nAvailabilityStatus for AdHocFilteringOption - This status can be either ENABLED or DISABLED . When this is set to DISABLED , QuickSight disables the left filter pane on the published dashboard, which can be used for ad hoc (one-time) filtering. This option is ENABLED by default.\nAvailabilityStatus for ExportToCSVOption - This status can be either ENABLED or DISABLED . The visual option to export data to .csv format isn\'t enabled when this is set to DISABLED . This option is ENABLED by default.\nVisibilityState for SheetControlsOption - This visibility state can be either COLLAPSED or EXPANDED . The sheet controls pane is collapsed by default when set to true. This option is COLLAPSED by default.\n\n\nAdHocFilteringOption (dict) --Ad hoc (one-time) filtering option.\n\nAvailabilityStatus (string) --Availability status.\n\n\n\nExportToCSVOption (dict) --Export to .csv option.\n\nAvailabilityStatus (string) --Availability status.\n\n\n\nSheetControlsOption (dict) --Sheet controls option.\n\nVisibilityState (string) --Visibility state.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'VersionArn': 'string',
    'DashboardId': 'string',
    'CreationStatus': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

Arn (string) --
The Amazon Resource Name (ARN) of the resource.

VersionArn (string) --
The ARN of the dashboard, including the version number.

DashboardId (string) --
The ID for the dashboard.

CreationStatus (string) --
The creation status of the request.

Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.LimitExceededException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Arn': 'string',
        'VersionArn': 'string',
        'DashboardId': 'string',
        'CreationStatus': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.LimitExceededException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def update_dashboard_permissions(AwsAccountId=None, DashboardId=None, GrantPermissions=None, RevokePermissions=None):
    """
    Updates read and write permissions on a dashboard.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_dashboard_permissions(
        AwsAccountId='string',
        DashboardId='string',
        GrantPermissions=[
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ],
        RevokePermissions=[
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the dashboard whose permissions you\'re updating.\n

    :type DashboardId: string
    :param DashboardId: [REQUIRED]\nThe ID for the dashboard.\n

    :type GrantPermissions: list
    :param GrantPermissions: The permissions that you want to grant on this resource.\n\n(dict) --Permission for the resource.\n\nPrincipal (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .\n\nActions (list) -- [REQUIRED]The action to grant or revoke permissions on, for example 'quicksight:DescribeDashboard' .\n\n(string) --\n\n\n\n\n\n

    :type RevokePermissions: list
    :param RevokePermissions: The permissions that you want to revoke from this resource.\n\n(dict) --Permission for the resource.\n\nPrincipal (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .\n\nActions (list) -- [REQUIRED]The action to grant or revoke permissions on, for example 'quicksight:DescribeDashboard' .\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DashboardArn': 'string',
    'DashboardId': 'string',
    'Permissions': [
        {
            'Principal': 'string',
            'Actions': [
                'string',
            ]
        },
    ],
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

DashboardArn (string) --
The Amazon Resource Name (ARN) of the dashboard.

DashboardId (string) --
The ID for the dashboard.

Permissions (list) --
Information about the permissions on the dashboard.

(dict) --
Permission for the resource.

Principal (string) --
The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .

Actions (list) --
The action to grant or revoke permissions on, for example "quicksight:DescribeDashboard" .

(string) --






RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'DashboardArn': 'string',
        'DashboardId': 'string',
        'Permissions': [
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ],
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_dashboard_published_version(AwsAccountId=None, DashboardId=None, VersionNumber=None):
    """
    Updates the published version of a dashboard.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_dashboard_published_version(
        AwsAccountId='string',
        DashboardId='string',
        VersionNumber=123
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the dashboard that you\'re updating.\n

    :type DashboardId: string
    :param DashboardId: [REQUIRED]\nThe ID for the dashboard.\n

    :type VersionNumber: integer
    :param VersionNumber: [REQUIRED]\nThe version number of the dashboard.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DashboardId': 'string',
    'DashboardArn': 'string',
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

DashboardId (string) --
The ID for the dashboard.

DashboardArn (string) --
The Amazon Resource Name (ARN) of the dashboard.

Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'DashboardId': 'string',
        'DashboardArn': 'string',
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def update_data_set(AwsAccountId=None, DataSetId=None, Name=None, PhysicalTableMap=None, LogicalTableMap=None, ImportMode=None, ColumnGroups=None, RowLevelPermissionDataSet=None):
    """
    Updates a dataset.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_data_set(
        AwsAccountId='string',
        DataSetId='string',
        Name='string',
        PhysicalTableMap={
            'string': {
                'RelationalTable': {
                    'DataSourceArn': 'string',
                    'Schema': 'string',
                    'Name': 'string',
                    'InputColumns': [
                        {
                            'Name': 'string',
                            'Type': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME'|'BIT'|'BOOLEAN'|'JSON'
                        },
                    ]
                },
                'CustomSql': {
                    'DataSourceArn': 'string',
                    'Name': 'string',
                    'SqlQuery': 'string',
                    'Columns': [
                        {
                            'Name': 'string',
                            'Type': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME'|'BIT'|'BOOLEAN'|'JSON'
                        },
                    ]
                },
                'S3Source': {
                    'DataSourceArn': 'string',
                    'UploadSettings': {
                        'Format': 'CSV'|'TSV'|'CLF'|'ELF'|'XLSX'|'JSON',
                        'StartFromRow': 123,
                        'ContainsHeader': True|False,
                        'TextQualifier': 'DOUBLE_QUOTE'|'SINGLE_QUOTE',
                        'Delimiter': 'string'
                    },
                    'InputColumns': [
                        {
                            'Name': 'string',
                            'Type': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME'|'BIT'|'BOOLEAN'|'JSON'
                        },
                    ]
                }
            }
        },
        LogicalTableMap={
            'string': {
                'Alias': 'string',
                'DataTransforms': [
                    {
                        'ProjectOperation': {
                            'ProjectedColumns': [
                                'string',
                            ]
                        },
                        'FilterOperation': {
                            'ConditionExpression': 'string'
                        },
                        'CreateColumnsOperation': {
                            'Columns': [
                                {
                                    'ColumnName': 'string',
                                    'ColumnId': 'string',
                                    'Expression': 'string'
                                },
                            ]
                        },
                        'RenameColumnOperation': {
                            'ColumnName': 'string',
                            'NewColumnName': 'string'
                        },
                        'CastColumnTypeOperation': {
                            'ColumnName': 'string',
                            'NewColumnType': 'STRING'|'INTEGER'|'DECIMAL'|'DATETIME',
                            'Format': 'string'
                        },
                        'TagColumnOperation': {
                            'ColumnName': 'string',
                            'Tags': [
                                {
                                    'ColumnGeographicRole': 'COUNTRY'|'STATE'|'COUNTY'|'CITY'|'POSTCODE'|'LONGITUDE'|'LATITUDE'
                                },
                            ]
                        }
                    },
                ],
                'Source': {
                    'JoinInstruction': {
                        'LeftOperand': 'string',
                        'RightOperand': 'string',
                        'Type': 'INNER'|'OUTER'|'LEFT'|'RIGHT',
                        'OnClause': 'string'
                    },
                    'PhysicalTableId': 'string'
                }
            }
        },
        ImportMode='SPICE'|'DIRECT_QUERY',
        ColumnGroups=[
            {
                'GeoSpatialColumnGroup': {
                    'Name': 'string',
                    'CountryCode': 'US',
                    'Columns': [
                        'string',
                    ]
                }
            },
        ],
        RowLevelPermissionDataSet={
            'Arn': 'string',
            'PermissionPolicy': 'GRANT_ACCESS'|'DENY_ACCESS'
        }
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe ID for the dataset that you want to update. This ID is unique per AWS Region for each AWS account.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe display name for the dataset.\n

    :type PhysicalTableMap: dict
    :param PhysicalTableMap: [REQUIRED]\nDeclares the physical tables that are available in the underlying data sources.\n\n(string) --\n(dict) --A view of a data source that contains information about the shape of the data in the underlying source. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.\n\nRelationalTable (dict) --A physical table type for relational data sources.\n\nDataSourceArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) for the data source.\n\nSchema (string) --The schema name. This name applies to certain relational database engines.\n\nName (string) -- [REQUIRED]The name of the relational table.\n\nInputColumns (list) -- [REQUIRED]The column schema of the table.\n\n(dict) --Metadata for a column that is used as the input of a transform operation.\n\nName (string) -- [REQUIRED]The name of this column in the underlying data source.\n\nType (string) -- [REQUIRED]The data type of the column.\n\n\n\n\n\n\n\nCustomSql (dict) --A physical table type built from the results of the custom SQL query.\n\nDataSourceArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the data source.\n\nName (string) -- [REQUIRED]A display name for the SQL query result.\n\nSqlQuery (string) -- [REQUIRED]The SQL query.\n\nColumns (list) --The column schema from the SQL query result set.\n\n(dict) --Metadata for a column that is used as the input of a transform operation.\n\nName (string) -- [REQUIRED]The name of this column in the underlying data source.\n\nType (string) -- [REQUIRED]The data type of the column.\n\n\n\n\n\n\n\nS3Source (dict) --A physical table type for as S3 data source.\n\nDataSourceArn (string) -- [REQUIRED]The amazon Resource Name (ARN) for the data source.\n\nUploadSettings (dict) --Information about the format for the S3 source file or files.\n\nFormat (string) --File format.\n\nStartFromRow (integer) --A row number to start reading data from.\n\nContainsHeader (boolean) --Whether the file has a header row, or the files each have a header row.\n\nTextQualifier (string) --Text qualifier.\n\nDelimiter (string) --The delimiter between values in the file.\n\n\n\nInputColumns (list) -- [REQUIRED]A physical table type for as S3 data source.\n\n(dict) --Metadata for a column that is used as the input of a transform operation.\n\nName (string) -- [REQUIRED]The name of this column in the underlying data source.\n\nType (string) -- [REQUIRED]The data type of the column.\n\n\n\n\n\n\n\n\n\n\n\n\n

    :type LogicalTableMap: dict
    :param LogicalTableMap: Configures the combination and transformation of the data from the physical tables.\n\n(string) --\n(dict) --A logical table is a unit that joins and that data transformations operate on. A logical table has a source, which can be either a physical table or result of a join. When a logical table points to a physical table, the logical table acts as a mutable copy of that physical table through transform operations.\n\nAlias (string) -- [REQUIRED]A display name for the logical table.\n\nDataTransforms (list) --Transform operations that act on this logical table.\n\n(dict) --A data transformation on a logical table. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.\n\nProjectOperation (dict) --An operation that projects columns. Operations that come after a projection can only refer to projected columns.\n\nProjectedColumns (list) -- [REQUIRED]Projected columns.\n\n(string) --\n\n\n\n\nFilterOperation (dict) --An operation that filters rows based on some condition.\n\nConditionExpression (string) -- [REQUIRED]An expression that must evaluate to a Boolean value. Rows for which the expression evaluates to true are kept in the dataset.\n\n\n\nCreateColumnsOperation (dict) --An operation that creates calculated columns. Columns created in one such operation form a lexical closure.\n\nColumns (list) -- [REQUIRED]Calculated columns to create.\n\n(dict) --A calculated column for a dataset.\n\nColumnName (string) -- [REQUIRED]Column name.\n\nColumnId (string) -- [REQUIRED]A unique ID to identify a calculated column. During a dataset update, if the column ID of a calculated column matches that of an existing calculated column, Amazon QuickSight preserves the existing calculated column.\n\nExpression (string) -- [REQUIRED]An expression that defines the calculated column.\n\n\n\n\n\n\n\nRenameColumnOperation (dict) --An operation that renames a column.\n\nColumnName (string) -- [REQUIRED]The name of the column to be renamed.\n\nNewColumnName (string) -- [REQUIRED]The new name for the column.\n\n\n\nCastColumnTypeOperation (dict) --A transform operation that casts a column to a different type.\n\nColumnName (string) -- [REQUIRED]Column name.\n\nNewColumnType (string) -- [REQUIRED]New column data type.\n\nFormat (string) --When casting a column from string to datetime type, you can supply a string in a format supported by Amazon QuickSight to denote the source data format.\n\n\n\nTagColumnOperation (dict) --An operation that tags a column with additional information.\n\nColumnName (string) -- [REQUIRED]The column that this operation acts on.\n\nTags (list) -- [REQUIRED]The dataset column tag, currently only used for geospatial type tagging. .\n\nNote\nThis is not tags for the AWS tagging feature. .\n\n\n(dict) --A tag for a column in a TagColumnOperation structure. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.\n\nColumnGeographicRole (string) --A geospatial role for a column.\n\n\n\n\n\n\n\n\n\n\n\nSource (dict) -- [REQUIRED]Source of this logical table.\n\nJoinInstruction (dict) --Specifies the result of a join of two logical tables.\n\nLeftOperand (string) -- [REQUIRED]Left operand.\n\nRightOperand (string) -- [REQUIRED]Right operand.\n\nType (string) -- [REQUIRED]Type.\n\nOnClause (string) -- [REQUIRED]On Clause.\n\n\n\nPhysicalTableId (string) --Physical table ID.\n\n\n\n\n\n\n\n\n

    :type ImportMode: string
    :param ImportMode: [REQUIRED]\nIndicates whether you want to import the data into SPICE.\n

    :type ColumnGroups: list
    :param ColumnGroups: Groupings of columns that work together in certain QuickSight features. Currently, only geospatial hierarchy is supported.\n\n(dict) --Groupings of columns that work together in certain Amazon QuickSight features. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.\n\nGeoSpatialColumnGroup (dict) --Geospatial column group that denotes a hierarchy.\n\nName (string) -- [REQUIRED]A display name for the hierarchy.\n\nCountryCode (string) -- [REQUIRED]Country code.\n\nColumns (list) -- [REQUIRED]Columns in this hierarchy.\n\n(string) --\n\n\n\n\n\n\n\n

    :type RowLevelPermissionDataSet: dict
    :param RowLevelPermissionDataSet: The row-level security configuration for the data you want to create.\n\nArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the permission dataset.\n\nPermissionPolicy (string) -- [REQUIRED]Permission policy.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'DataSetId': 'string',
    'IngestionArn': 'string',
    'IngestionId': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

Arn (string) --
The Amazon Resource Name (ARN) of the dataset.

DataSetId (string) --
The ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.

IngestionArn (string) --
The ARN for the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.

IngestionId (string) --
The ID of the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.LimitExceededException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Arn': 'string',
        'DataSetId': 'string',
        'IngestionArn': 'string',
        'IngestionId': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.LimitExceededException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def update_data_set_permissions(AwsAccountId=None, DataSetId=None, GrantPermissions=None, RevokePermissions=None):
    """
    Updates the permissions on a dataset.
    The permissions resource is arn:aws:quicksight:region:aws-account-id:dataset/data-set-id .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_data_set_permissions(
        AwsAccountId='string',
        DataSetId='string',
        GrantPermissions=[
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ],
        RevokePermissions=[
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe ID for the dataset whose permissions you want to update. This ID is unique per AWS Region for each AWS account.\n

    :type GrantPermissions: list
    :param GrantPermissions: The resource permissions that you want to grant to the dataset.\n\n(dict) --Permission for the resource.\n\nPrincipal (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .\n\nActions (list) -- [REQUIRED]The action to grant or revoke permissions on, for example 'quicksight:DescribeDashboard' .\n\n(string) --\n\n\n\n\n\n

    :type RevokePermissions: list
    :param RevokePermissions: The resource permissions that you want to revoke from the dataset.\n\n(dict) --Permission for the resource.\n\nPrincipal (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .\n\nActions (list) -- [REQUIRED]The action to grant or revoke permissions on, for example 'quicksight:DescribeDashboard' .\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DataSetArn': 'string',
    'DataSetId': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

DataSetArn (string) --
The Amazon Resource Name (ARN) of the dataset.

DataSetId (string) --
The ID for the dataset whose permissions you want to update. This ID is unique per AWS Region for each AWS account.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'DataSetArn': 'string',
        'DataSetId': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def update_data_source(AwsAccountId=None, DataSourceId=None, Name=None, DataSourceParameters=None, Credentials=None, VpcConnectionProperties=None, SslProperties=None):
    """
    Updates a data source.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_data_source(
        AwsAccountId='string',
        DataSourceId='string',
        Name='string',
        DataSourceParameters={
            'AmazonElasticsearchParameters': {
                'Domain': 'string'
            },
            'AthenaParameters': {
                'WorkGroup': 'string'
            },
            'AuroraParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'AuroraPostgreSqlParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'AwsIotAnalyticsParameters': {
                'DataSetName': 'string'
            },
            'JiraParameters': {
                'SiteBaseUrl': 'string'
            },
            'MariaDbParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'MySqlParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'PostgreSqlParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'PrestoParameters': {
                'Host': 'string',
                'Port': 123,
                'Catalog': 'string'
            },
            'RdsParameters': {
                'InstanceId': 'string',
                'Database': 'string'
            },
            'RedshiftParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string',
                'ClusterId': 'string'
            },
            'S3Parameters': {
                'ManifestFileLocation': {
                    'Bucket': 'string',
                    'Key': 'string'
                }
            },
            'ServiceNowParameters': {
                'SiteBaseUrl': 'string'
            },
            'SnowflakeParameters': {
                'Host': 'string',
                'Database': 'string',
                'Warehouse': 'string'
            },
            'SparkParameters': {
                'Host': 'string',
                'Port': 123
            },
            'SqlServerParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'TeradataParameters': {
                'Host': 'string',
                'Port': 123,
                'Database': 'string'
            },
            'TwitterParameters': {
                'Query': 'string',
                'MaxRows': 123
            }
        },
        Credentials={
            'CredentialPair': {
                'Username': 'string',
                'Password': 'string'
            }
        },
        VpcConnectionProperties={
            'VpcConnectionArn': 'string'
        },
        SslProperties={
            'DisableSsl': True|False
        }
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type DataSourceId: string
    :param DataSourceId: [REQUIRED]\nThe ID of the data source. This ID is unique per AWS Region for each AWS account.\n

    :type Name: string
    :param Name: [REQUIRED]\nA display name for the data source.\n

    :type DataSourceParameters: dict
    :param DataSourceParameters: The parameters that QuickSight uses to connect to your underlying source.\n\nAmazonElasticsearchParameters (dict) --Amazon Elasticsearch Service parameters.\n\nDomain (string) -- [REQUIRED]The Amazon Elasticsearch Service domain.\n\n\n\nAthenaParameters (dict) --Amazon Athena parameters.\n\nWorkGroup (string) --The workgroup that Amazon Athena uses.\n\n\n\nAuroraParameters (dict) --Amazon Aurora MySQL parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nAuroraPostgreSqlParameters (dict) --Aurora PostgreSQL parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nAwsIotAnalyticsParameters (dict) --AWS IoT Analytics parameters.\n\nDataSetName (string) -- [REQUIRED]Dataset name.\n\n\n\nJiraParameters (dict) --Jira parameters.\n\nSiteBaseUrl (string) -- [REQUIRED]The base URL of the Jira site.\n\n\n\nMariaDbParameters (dict) --MariaDB parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nMySqlParameters (dict) --MySQL parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nPostgreSqlParameters (dict) --PostgreSQL parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nPrestoParameters (dict) --Presto parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nCatalog (string) -- [REQUIRED]Catalog.\n\n\n\nRdsParameters (dict) --Amazon RDS parameters.\n\nInstanceId (string) -- [REQUIRED]Instance ID.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nRedshiftParameters (dict) --Amazon Redshift parameters.\n\nHost (string) --Host. This field can be blank if ClusterId is provided.\n\nPort (integer) --Port. This field can be blank if the ClusterId is provided.\n\nDatabase (string) -- [REQUIRED]Database.\n\nClusterId (string) --Cluster ID. This field can be blank if the Host and Port are provided.\n\n\n\nS3Parameters (dict) --S3 parameters.\n\nManifestFileLocation (dict) -- [REQUIRED]Location of the Amazon S3 manifest file. This is NULL if the manifest file was uploaded in the console.\n\nBucket (string) -- [REQUIRED]Amazon S3 bucket.\n\nKey (string) -- [REQUIRED]Amazon S3 key that identifies an object.\n\n\n\n\n\nServiceNowParameters (dict) --ServiceNow parameters.\n\nSiteBaseUrl (string) -- [REQUIRED]URL of the base site.\n\n\n\nSnowflakeParameters (dict) --Snowflake parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nDatabase (string) -- [REQUIRED]Database.\n\nWarehouse (string) -- [REQUIRED]Warehouse.\n\n\n\nSparkParameters (dict) --Spark parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\n\n\nSqlServerParameters (dict) --SQL Server parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nTeradataParameters (dict) --Teradata parameters.\n\nHost (string) -- [REQUIRED]Host.\n\nPort (integer) -- [REQUIRED]Port.\n\nDatabase (string) -- [REQUIRED]Database.\n\n\n\nTwitterParameters (dict) --Twitter parameters.\n\nQuery (string) -- [REQUIRED]Twitter query string.\n\nMaxRows (integer) -- [REQUIRED]Maximum number of rows to query Twitter.\n\n\n\n\n

    :type Credentials: dict
    :param Credentials: The credentials that QuickSight that uses to connect to your underlying source. Currently, only credentials based on user name and password are supported.\n\nCredentialPair (dict) --Credential pair.\n\nUsername (string) -- [REQUIRED]User name.\n\nPassword (string) -- [REQUIRED]Password.\n\n\n\n\n

    :type VpcConnectionProperties: dict
    :param VpcConnectionProperties: Use this parameter only when you want QuickSight to use a VPC connection when connecting to your underlying source.\n\nVpcConnectionArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) for the VPC connection.\n\n\n

    :type SslProperties: dict
    :param SslProperties: Secure Socket Layer (SSL) properties that apply when QuickSight connects to your underlying source.\n\nDisableSsl (boolean) --A Boolean option to control whether SSL should be disabled.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'DataSourceId': 'string',
    'UpdateStatus': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

Arn (string) --
The Amazon Resource Name (ARN) of the data source.

DataSourceId (string) --
The ID of the data source. This ID is unique per AWS Region for each AWS account.

UpdateStatus (string) --
The update status of the data source\'s last update.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'Arn': 'string',
        'DataSourceId': 'string',
        'UpdateStatus': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def update_data_source_permissions(AwsAccountId=None, DataSourceId=None, GrantPermissions=None, RevokePermissions=None):
    """
    Updates the permissions to a data source.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_data_source_permissions(
        AwsAccountId='string',
        DataSourceId='string',
        GrantPermissions=[
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ],
        RevokePermissions=[
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe AWS account ID.\n

    :type DataSourceId: string
    :param DataSourceId: [REQUIRED]\nThe ID of the data source. This ID is unique per AWS Region for each AWS account.\n

    :type GrantPermissions: list
    :param GrantPermissions: A list of resource permissions that you want to grant on the data source.\n\n(dict) --Permission for the resource.\n\nPrincipal (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .\n\nActions (list) -- [REQUIRED]The action to grant or revoke permissions on, for example 'quicksight:DescribeDashboard' .\n\n(string) --\n\n\n\n\n\n

    :type RevokePermissions: list
    :param RevokePermissions: A list of resource permissions that you want to revoke on the data source.\n\n(dict) --Permission for the resource.\n\nPrincipal (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .\n\nActions (list) -- [REQUIRED]The action to grant or revoke permissions on, for example 'quicksight:DescribeDashboard' .\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DataSourceArn': 'string',
    'DataSourceId': 'string',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

DataSourceArn (string) --
The Amazon Resource Name (ARN) of the data source.

DataSourceId (string) --
The ID of the data source. This ID is unique per AWS Region for each AWS account.

RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'DataSourceArn': 'string',
        'DataSourceId': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def update_group(GroupName=None, Description=None, AwsAccountId=None, Namespace=None):
    """
    Changes a group description.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_group(
        GroupName='string',
        Description='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group that you want to update.\n

    :type Description: string
    :param Description: The description for the group that you want to update.

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Group': {
        'Arn': 'string',
        'GroupName': 'string',
        'Description': 'string',
        'PrincipalId': 'string'
    },
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

Group (dict) --
The name of the group.

Arn (string) --
The Amazon Resource Name (ARN) for the group.

GroupName (string) --
The name of the group.

Description (string) --
The group description.

PrincipalId (string) --
The principal ID of the group.



RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.PreconditionNotMetException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'Group': {
            'Arn': 'string',
            'GroupName': 'string',
            'Description': 'string',
            'PrincipalId': 'string'
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.AccessDeniedException
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.PreconditionNotMetException
    QuickSight.Client.exceptions.InternalFailureException
    QuickSight.Client.exceptions.ResourceUnavailableException
    
    """
    pass

def update_iam_policy_assignment(AwsAccountId=None, AssignmentName=None, Namespace=None, AssignmentStatus=None, PolicyArn=None, Identities=None):
    """
    Updates an existing IAM policy assignment. This operation updates only the optional parameter or parameters that are specified in the request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_iam_policy_assignment(
        AwsAccountId='string',
        AssignmentName='string',
        Namespace='string',
        AssignmentStatus='ENABLED'|'DRAFT'|'DISABLED',
        PolicyArn='string',
        Identities={
            'string': [
                'string',
            ]
        }
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the IAM policy assignment.\n

    :type AssignmentName: string
    :param AssignmentName: [REQUIRED]\nThe name of the assignment. This name must be unique within an AWS account.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace of the assignment.\n

    :type AssignmentStatus: string
    :param AssignmentStatus: The status of the assignment. Possible values are as follows:\n\nENABLED - Anything specified in this assignment is used when creating the data source.\nDISABLED - This assignment isn\'t used when creating the data source.\nDRAFT - This assignment is an unfinished draft and isn\'t used when creating the data source.\n\n

    :type PolicyArn: string
    :param PolicyArn: The ARN for the IAM policy to apply to the QuickSight users and groups specified in this assignment.

    :type Identities: dict
    :param Identities: The QuickSight users, groups, or both that you want to assign the policy to.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AssignmentName': 'string',
    'AssignmentId': 'string',
    'PolicyArn': 'string',
    'Identities': {
        'string': [
            'string',
        ]
    },
    'AssignmentStatus': 'ENABLED'|'DRAFT'|'DISABLED',
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

AssignmentName (string) --
The name of the assignment.

AssignmentId (string) --
The ID of the assignment.

PolicyArn (string) --
The ARN for the IAM policy applied to the QuickSight users and groups specified in this assignment.

Identities (dict) --
The QuickSight users, groups, or both that the IAM policy is assigned to.

(string) --
(list) --
(string) --






AssignmentStatus (string) --
The status of the assignment. Possible values are as follows:

ENABLED - Anything specified in this assignment is used when creating the data source.
DISABLED - This assignment isn\'t used when creating the data source.
DRAFT - This assignment is an unfinished draft and isn\'t used when creating the data source.


RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ConcurrentUpdatingException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'AssignmentName': 'string',
        'AssignmentId': 'string',
        'PolicyArn': 'string',
        'Identities': {
            'string': [
                'string',
            ]
        },
        'AssignmentStatus': 'ENABLED'|'DRAFT'|'DISABLED',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def update_template(AwsAccountId=None, TemplateId=None, SourceEntity=None, VersionDescription=None, Name=None):
    """
    Updates a template from an existing Amazon QuickSight analysis or another template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_template(
        AwsAccountId='string',
        TemplateId='string',
        SourceEntity={
            'SourceAnalysis': {
                'Arn': 'string',
                'DataSetReferences': [
                    {
                        'DataSetPlaceholder': 'string',
                        'DataSetArn': 'string'
                    },
                ]
            },
            'SourceTemplate': {
                'Arn': 'string'
            }
        },
        VersionDescription='string',
        Name='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the template that you\'re updating.\n

    :type TemplateId: string
    :param TemplateId: [REQUIRED]\nThe ID for the template.\n

    :type SourceEntity: dict
    :param SourceEntity: [REQUIRED]\nThe source QuickSight entity from which this template is being updated. You can currently update templates from an Analysis or another template.\n\nSourceAnalysis (dict) --The source analysis, if it is based on an analysis.\n\nArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the resource.\n\nDataSetReferences (list) -- [REQUIRED]A structure containing information about the dataset references used as placeholders in the template.\n\n(dict) --Dataset reference.\n\nDataSetPlaceholder (string) -- [REQUIRED]Dataset placeholder.\n\nDataSetArn (string) -- [REQUIRED]Dataset Amazon Resource Name (ARN).\n\n\n\n\n\n\n\nSourceTemplate (dict) --The source template, if it is based on an template.\n\nArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the resource.\n\n\n\n\n

    :type VersionDescription: string
    :param VersionDescription: A description of the current template version that is being updated. Every time you call UpdateTemplate , you create a new version of the template. Each version of the template maintains a description of the version in the VersionDescription field.

    :type Name: string
    :param Name: The name for the template.

    :rtype: dict

ReturnsResponse Syntax
{
    'TemplateId': 'string',
    'Arn': 'string',
    'VersionArn': 'string',
    'CreationStatus': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

TemplateId (string) --
The ID for the template.

Arn (string) --
The Amazon Resource Name (ARN) for the template.

VersionArn (string) --
The ARN for the template, including the version information of the first version.

CreationStatus (string) --
The creation status of the template.

Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceExistsException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.LimitExceededException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'TemplateId': 'string',
        'Arn': 'string',
        'VersionArn': 'string',
        'CreationStatus': 'CREATION_IN_PROGRESS'|'CREATION_SUCCESSFUL'|'CREATION_FAILED'|'UPDATE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_FAILED',
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.InvalidParameterValueException
    QuickSight.Client.exceptions.ResourceExistsException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.LimitExceededException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def update_template_alias(AwsAccountId=None, TemplateId=None, AliasName=None, TemplateVersionNumber=None):
    """
    Updates the template alias of a template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_template_alias(
        AwsAccountId='string',
        TemplateId='string',
        AliasName='string',
        TemplateVersionNumber=123
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the template alias that you\'re updating.\n

    :type TemplateId: string
    :param TemplateId: [REQUIRED]\nThe ID for the template.\n

    :type AliasName: string
    :param AliasName: [REQUIRED]\nThe alias of the template that you want to update. If you name a specific alias, you update the version that the alias points to. You can specify the latest version of the template by providing the keyword $LATEST in the AliasName parameter. The keyword $PUBLISHED doesn\'t apply to templates.\n

    :type TemplateVersionNumber: integer
    :param TemplateVersionNumber: [REQUIRED]\nThe version number of the template.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TemplateAlias': {
        'AliasName': 'string',
        'Arn': 'string',
        'TemplateVersionNumber': 123
    },
    'Status': 123,
    'RequestId': 'string'
}


Response Structure

(dict) --

TemplateAlias (dict) --
The template alias.

AliasName (string) --
The display name of the template alias.

Arn (string) --
The Amazon Resource Name (ARN) of the template alias.

TemplateVersionNumber (integer) --
The version number of the template alias.



Status (integer) --
The HTTP status of the request.

RequestId (string) --
The AWS request ID for this operation.







Exceptions

QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'TemplateAlias': {
            'AliasName': 'string',
            'Arn': 'string',
            'TemplateVersionNumber': 123
        },
        'Status': 123,
        'RequestId': 'string'
    }
    
    
    :returns: 
    QuickSight.Client.exceptions.ThrottlingException
    QuickSight.Client.exceptions.ResourceNotFoundException
    QuickSight.Client.exceptions.ConflictException
    QuickSight.Client.exceptions.UnsupportedUserEditionException
    QuickSight.Client.exceptions.InternalFailureException
    
    """
    pass

def update_template_permissions(AwsAccountId=None, TemplateId=None, GrantPermissions=None, RevokePermissions=None):
    """
    Updates the resource permissions for a template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_template_permissions(
        AwsAccountId='string',
        TemplateId='string',
        GrantPermissions=[
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ],
        RevokePermissions=[
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID of the AWS account that contains the template.\n

    :type TemplateId: string
    :param TemplateId: [REQUIRED]\nThe ID for the template.\n

    :type GrantPermissions: list
    :param GrantPermissions: A list of resource permissions to be granted on the template.\n\n(dict) --Permission for the resource.\n\nPrincipal (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .\n\nActions (list) -- [REQUIRED]The action to grant or revoke permissions on, for example 'quicksight:DescribeDashboard' .\n\n(string) --\n\n\n\n\n\n

    :type RevokePermissions: list
    :param RevokePermissions: A list of resource permissions to be revoked from the template.\n\n(dict) --Permission for the resource.\n\nPrincipal (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .\n\nActions (list) -- [REQUIRED]The action to grant or revoke permissions on, for example 'quicksight:DescribeDashboard' .\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TemplateId': 'string',
    'TemplateArn': 'string',
    'Permissions': [
        {
            'Principal': 'string',
            'Actions': [
                'string',
            ]
        },
    ],
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

TemplateId (string) --
The ID for the template.

TemplateArn (string) --
The Amazon Resource Name (ARN) of the template.

Permissions (list) --
A list of resource permissions to be set on the template.

(dict) --
Permission for the resource.

Principal (string) --
The Amazon Resource Name (ARN) of an Amazon QuickSight user or group, or an IAM ARN. If you are using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it is the ARN of a QuickSight user or group. .

Actions (list) --
The action to grant or revoke permissions on, for example "quicksight:DescribeDashboard" .

(string) --






RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ConflictException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.UnsupportedUserEditionException
QuickSight.Client.exceptions.InternalFailureException


    :return: {
        'TemplateId': 'string',
        'TemplateArn': 'string',
        'Permissions': [
            {
                'Principal': 'string',
                'Actions': [
                    'string',
                ]
            },
        ],
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_user(UserName=None, AwsAccountId=None, Namespace=None, Email=None, Role=None):
    """
    Updates an Amazon QuickSight user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user(
        UserName='string',
        AwsAccountId='string',
        Namespace='string',
        Email='string',
        Role='ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe Amazon QuickSight user name that you want to update.\n

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]\nThe ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace. Currently, you should set this to default .\n

    :type Email: string
    :param Email: [REQUIRED]\nThe email address of the user that you want to update.\n

    :type Role: string
    :param Role: [REQUIRED]\nThe Amazon QuickSight role of the user. The user role can be one of the following:\n\nREADER : A user who has read-only access to dashboards.\nAUTHOR : A user who can create data sources, datasets, analyses, and dashboards.\nADMIN : A user who is an author, who can also manage Amazon QuickSight settings.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'User': {
        'Arn': 'string',
        'UserName': 'string',
        'Email': 'string',
        'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
        'IdentityType': 'IAM'|'QUICKSIGHT',
        'Active': True|False,
        'PrincipalId': 'string'
    },
    'RequestId': 'string',
    'Status': 123
}


Response Structure

(dict) --

User (dict) --
The Amazon QuickSight user.

Arn (string) --
The Amazon Resource Name (ARN) for the user.

UserName (string) --
The user\'s user name.

Email (string) --
The user\'s email address.

Role (string) --
The Amazon QuickSight role for the user. The user role can be one of the following:.

READER : A user who has read-only access to dashboards.
AUTHOR : A user who can create data sources, datasets, analyses, and dashboards.
ADMIN : A user who is an author, who can also manage Amazon QuickSight settings.
RESTRICTED_READER : This role isn\'t currently available for use.
RESTRICTED_AUTHOR : This role isn\'t currently available for use.


IdentityType (string) --
The type of identity authentication used by the user.

Active (boolean) --
The active status of user. When you create an Amazon QuickSight user that\xe2\x80\x99s not an IAM user or an Active Directory user, that user is inactive until they sign in and provide a password.

PrincipalId (string) --
The principal ID of the user.



RequestId (string) --
The AWS request ID for this operation.

Status (integer) --
The HTTP status of the request.







Exceptions

QuickSight.Client.exceptions.AccessDeniedException
QuickSight.Client.exceptions.InvalidParameterValueException
QuickSight.Client.exceptions.ResourceNotFoundException
QuickSight.Client.exceptions.ThrottlingException
QuickSight.Client.exceptions.InternalFailureException
QuickSight.Client.exceptions.ResourceUnavailableException


    :return: {
        'User': {
            'Arn': 'string',
            'UserName': 'string',
            'Email': 'string',
            'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
            'IdentityType': 'IAM'|'QUICKSIGHT',
            'Active': True|False,
            'PrincipalId': 'string'
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    :returns: 
    READER : A user who has read-only access to dashboards.
    AUTHOR : A user who can create data sources, datasets, analyses, and dashboards.
    ADMIN : A user who is an author, who can also manage Amazon QuickSight settings.
    RESTRICTED_READER : This role isn\'t currently available for use.
    RESTRICTED_AUTHOR : This role isn\'t currently available for use.
    
    """
    pass

