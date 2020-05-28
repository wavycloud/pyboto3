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

def batch_grant_permissions(CatalogId=None, Entries=None):
    """
    Batch operation to grant permissions to the principal.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_grant_permissions(
        CatalogId='string',
        Entries=[
            {
                'Id': 'string',
                'Principal': {
                    'DataLakePrincipalIdentifier': 'string'
                },
                'Resource': {
                    'Catalog': {}
                    ,
                    'Database': {
                        'Name': 'string'
                    },
                    'Table': {
                        'DatabaseName': 'string',
                        'Name': 'string'
                    },
                    'TableWithColumns': {
                        'DatabaseName': 'string',
                        'Name': 'string',
                        'ColumnNames': [
                            'string',
                        ],
                        'ColumnWildcard': {
                            'ExcludedColumnNames': [
                                'string',
                            ]
                        }
                    },
                    'DataLocation': {
                        'ResourceArn': 'string'
                    }
                },
                'Permissions': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ],
                'PermissionsWithGrantOption': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ]
            },
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

    :type Entries: list
    :param Entries: [REQUIRED]\nA list of up to 20 entries for resource permissions to be granted by batch operation to the principal.\n\n(dict) --A permission to a resource granted by batch operation to the principal.\n\nId (string) -- [REQUIRED]A unique identifier for the batch permissions request entry.\n\nPrincipal (dict) --The principal to be granted a permission.\n\nDataLakePrincipalIdentifier (string) --An identifier for the AWS Lake Formation principal.\n\n\n\nResource (dict) --The resource to which the principal is to be granted a permission.\n\nCatalog (dict) --The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.\n\nDatabase (dict) --The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.\n\nName (string) -- [REQUIRED]The name of the database resource. Unique to the Data Catalog.\n\n\n\nTable (dict) --The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.\n\nDatabaseName (string) -- [REQUIRED]The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.\n\nName (string) -- [REQUIRED]The name of the table.\n\n\n\nTableWithColumns (dict) --The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.\n\nDatabaseName (string) --The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.\n\nName (string) --The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.\n\nColumnNames (list) --The list of column names for the table. At least one of ColumnNames or ColumnWildcard is required.\n\n(string) --\n\n\nColumnWildcard (dict) --A wildcard specified by a ColumnWildcard object. At least one of ColumnNames or ColumnWildcard is required.\n\nExcludedColumnNames (list) --Excludes column names. Any column with this name will be excluded.\n\n(string) --\n\n\n\n\n\n\nDataLocation (dict) --The location of an Amazon S3 path where permissions are granted or revoked.\n\nResourceArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that uniquely identifies the data location resource.\n\n\n\n\n\nPermissions (list) --The permissions to be granted.\n\n(string) --\n\n\nPermissionsWithGrantOption (list) --Indicates if the option to pass permissions is granted.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Failures': [
        {
            'RequestEntry': {
                'Id': 'string',
                'Principal': {
                    'DataLakePrincipalIdentifier': 'string'
                },
                'Resource': {
                    'Catalog': {},
                    'Database': {
                        'Name': 'string'
                    },
                    'Table': {
                        'DatabaseName': 'string',
                        'Name': 'string'
                    },
                    'TableWithColumns': {
                        'DatabaseName': 'string',
                        'Name': 'string',
                        'ColumnNames': [
                            'string',
                        ],
                        'ColumnWildcard': {
                            'ExcludedColumnNames': [
                                'string',
                            ]
                        }
                    },
                    'DataLocation': {
                        'ResourceArn': 'string'
                    }
                },
                'Permissions': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ],
                'PermissionsWithGrantOption': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ]
            },
            'Error': {
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

Failures (list) --
A list of failures to grant permissions to the resources.

(dict) --
A list of failures when performing a batch grant or batch revoke operation.

RequestEntry (dict) --
An identifier for an entry of the batch request.

Id (string) --
A unique identifier for the batch permissions request entry.

Principal (dict) --
The principal to be granted a permission.

DataLakePrincipalIdentifier (string) --
An identifier for the AWS Lake Formation principal.



Resource (dict) --
The resource to which the principal is to be granted a permission.

Catalog (dict) --
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

Database (dict) --
The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.

Name (string) --
The name of the database resource. Unique to the Data Catalog.



Table (dict) --
The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

DatabaseName (string) --
The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

Name (string) --
The name of the table.



TableWithColumns (dict) --
The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.

DatabaseName (string) --
The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

Name (string) --
The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

ColumnNames (list) --
The list of column names for the table. At least one of ColumnNames or ColumnWildcard is required.

(string) --


ColumnWildcard (dict) --
A wildcard specified by a ColumnWildcard object. At least one of ColumnNames or ColumnWildcard is required.

ExcludedColumnNames (list) --
Excludes column names. Any column with this name will be excluded.

(string) --






DataLocation (dict) --
The location of an Amazon S3 path where permissions are granted or revoked.

ResourceArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the data location resource.





Permissions (list) --
The permissions to be granted.

(string) --


PermissionsWithGrantOption (list) --
Indicates if the option to pass permissions is granted.

(string) --




Error (dict) --
An error message that applies to the failure of the entry.

ErrorCode (string) --
The code associated with this error.

ErrorMessage (string) --
A message describing the error.













Exceptions

LakeFormation.Client.exceptions.InvalidInputException
LakeFormation.Client.exceptions.OperationTimeoutException


    :return: {
        'Failures': [
            {
                'RequestEntry': {
                    'Id': 'string',
                    'Principal': {
                        'DataLakePrincipalIdentifier': 'string'
                    },
                    'Resource': {
                        'Catalog': {},
                        'Database': {
                            'Name': 'string'
                        },
                        'Table': {
                            'DatabaseName': 'string',
                            'Name': 'string'
                        },
                        'TableWithColumns': {
                            'DatabaseName': 'string',
                            'Name': 'string',
                            'ColumnNames': [
                                'string',
                            ],
                            'ColumnWildcard': {
                                'ExcludedColumnNames': [
                                    'string',
                                ]
                            }
                        },
                        'DataLocation': {
                            'ResourceArn': 'string'
                        }
                    },
                    'Permissions': [
                        'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                    ],
                    'PermissionsWithGrantOption': [
                        'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                    ]
                },
                'Error': {
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

def batch_revoke_permissions(CatalogId=None, Entries=None):
    """
    Batch operation to revoke permissions from the principal.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_revoke_permissions(
        CatalogId='string',
        Entries=[
            {
                'Id': 'string',
                'Principal': {
                    'DataLakePrincipalIdentifier': 'string'
                },
                'Resource': {
                    'Catalog': {}
                    ,
                    'Database': {
                        'Name': 'string'
                    },
                    'Table': {
                        'DatabaseName': 'string',
                        'Name': 'string'
                    },
                    'TableWithColumns': {
                        'DatabaseName': 'string',
                        'Name': 'string',
                        'ColumnNames': [
                            'string',
                        ],
                        'ColumnWildcard': {
                            'ExcludedColumnNames': [
                                'string',
                            ]
                        }
                    },
                    'DataLocation': {
                        'ResourceArn': 'string'
                    }
                },
                'Permissions': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ],
                'PermissionsWithGrantOption': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ]
            },
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

    :type Entries: list
    :param Entries: [REQUIRED]\nA list of up to 20 entries for resource permissions to be revoked by batch operation to the principal.\n\n(dict) --A permission to a resource granted by batch operation to the principal.\n\nId (string) -- [REQUIRED]A unique identifier for the batch permissions request entry.\n\nPrincipal (dict) --The principal to be granted a permission.\n\nDataLakePrincipalIdentifier (string) --An identifier for the AWS Lake Formation principal.\n\n\n\nResource (dict) --The resource to which the principal is to be granted a permission.\n\nCatalog (dict) --The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.\n\nDatabase (dict) --The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.\n\nName (string) -- [REQUIRED]The name of the database resource. Unique to the Data Catalog.\n\n\n\nTable (dict) --The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.\n\nDatabaseName (string) -- [REQUIRED]The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.\n\nName (string) -- [REQUIRED]The name of the table.\n\n\n\nTableWithColumns (dict) --The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.\n\nDatabaseName (string) --The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.\n\nName (string) --The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.\n\nColumnNames (list) --The list of column names for the table. At least one of ColumnNames or ColumnWildcard is required.\n\n(string) --\n\n\nColumnWildcard (dict) --A wildcard specified by a ColumnWildcard object. At least one of ColumnNames or ColumnWildcard is required.\n\nExcludedColumnNames (list) --Excludes column names. Any column with this name will be excluded.\n\n(string) --\n\n\n\n\n\n\nDataLocation (dict) --The location of an Amazon S3 path where permissions are granted or revoked.\n\nResourceArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that uniquely identifies the data location resource.\n\n\n\n\n\nPermissions (list) --The permissions to be granted.\n\n(string) --\n\n\nPermissionsWithGrantOption (list) --Indicates if the option to pass permissions is granted.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Failures': [
        {
            'RequestEntry': {
                'Id': 'string',
                'Principal': {
                    'DataLakePrincipalIdentifier': 'string'
                },
                'Resource': {
                    'Catalog': {},
                    'Database': {
                        'Name': 'string'
                    },
                    'Table': {
                        'DatabaseName': 'string',
                        'Name': 'string'
                    },
                    'TableWithColumns': {
                        'DatabaseName': 'string',
                        'Name': 'string',
                        'ColumnNames': [
                            'string',
                        ],
                        'ColumnWildcard': {
                            'ExcludedColumnNames': [
                                'string',
                            ]
                        }
                    },
                    'DataLocation': {
                        'ResourceArn': 'string'
                    }
                },
                'Permissions': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ],
                'PermissionsWithGrantOption': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ]
            },
            'Error': {
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

Failures (list) --
A list of failures to revoke permissions to the resources.

(dict) --
A list of failures when performing a batch grant or batch revoke operation.

RequestEntry (dict) --
An identifier for an entry of the batch request.

Id (string) --
A unique identifier for the batch permissions request entry.

Principal (dict) --
The principal to be granted a permission.

DataLakePrincipalIdentifier (string) --
An identifier for the AWS Lake Formation principal.



Resource (dict) --
The resource to which the principal is to be granted a permission.

Catalog (dict) --
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

Database (dict) --
The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.

Name (string) --
The name of the database resource. Unique to the Data Catalog.



Table (dict) --
The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

DatabaseName (string) --
The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

Name (string) --
The name of the table.



TableWithColumns (dict) --
The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.

DatabaseName (string) --
The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

Name (string) --
The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

ColumnNames (list) --
The list of column names for the table. At least one of ColumnNames or ColumnWildcard is required.

(string) --


ColumnWildcard (dict) --
A wildcard specified by a ColumnWildcard object. At least one of ColumnNames or ColumnWildcard is required.

ExcludedColumnNames (list) --
Excludes column names. Any column with this name will be excluded.

(string) --






DataLocation (dict) --
The location of an Amazon S3 path where permissions are granted or revoked.

ResourceArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the data location resource.





Permissions (list) --
The permissions to be granted.

(string) --


PermissionsWithGrantOption (list) --
Indicates if the option to pass permissions is granted.

(string) --




Error (dict) --
An error message that applies to the failure of the entry.

ErrorCode (string) --
The code associated with this error.

ErrorMessage (string) --
A message describing the error.













Exceptions

LakeFormation.Client.exceptions.InvalidInputException
LakeFormation.Client.exceptions.OperationTimeoutException


    :return: {
        'Failures': [
            {
                'RequestEntry': {
                    'Id': 'string',
                    'Principal': {
                        'DataLakePrincipalIdentifier': 'string'
                    },
                    'Resource': {
                        'Catalog': {},
                        'Database': {
                            'Name': 'string'
                        },
                        'Table': {
                            'DatabaseName': 'string',
                            'Name': 'string'
                        },
                        'TableWithColumns': {
                            'DatabaseName': 'string',
                            'Name': 'string',
                            'ColumnNames': [
                                'string',
                            ],
                            'ColumnWildcard': {
                                'ExcludedColumnNames': [
                                    'string',
                                ]
                            }
                        },
                        'DataLocation': {
                            'ResourceArn': 'string'
                        }
                    },
                    'Permissions': [
                        'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                    ],
                    'PermissionsWithGrantOption': [
                        'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                    ]
                },
                'Error': {
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

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def deregister_resource(ResourceArn=None):
    """
    Deregisters the resource as managed by the Data Catalog.
    When you deregister a path, Lake Formation removes the path from the inline policy attached to your service-linked role.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource that you want to deregister.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

LakeFormation.Client.exceptions.InvalidInputException
LakeFormation.Client.exceptions.InternalServiceException
LakeFormation.Client.exceptions.OperationTimeoutException
LakeFormation.Client.exceptions.EntityNotFoundException


    :return: {}
    
    
    :returns: 
    LakeFormation.Client.exceptions.InvalidInputException
    LakeFormation.Client.exceptions.InternalServiceException
    LakeFormation.Client.exceptions.OperationTimeoutException
    LakeFormation.Client.exceptions.EntityNotFoundException
    
    """
    pass

def describe_resource(ResourceArn=None):
    """
    Retrieves the current data access role for the given resource registered in AWS Lake Formation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe resource ARN.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ResourceInfo': {
        'ResourceArn': 'string',
        'RoleArn': 'string',
        'LastModified': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
ResourceInfo (dict) --A structure containing information about an AWS Lake Formation resource.

ResourceArn (string) --The Amazon Resource Name (ARN) of the resource.

RoleArn (string) --The IAM role that registered a resource.

LastModified (datetime) --The date and time the resource was last modified.








Exceptions

LakeFormation.Client.exceptions.InvalidInputException
LakeFormation.Client.exceptions.InternalServiceException
LakeFormation.Client.exceptions.OperationTimeoutException
LakeFormation.Client.exceptions.EntityNotFoundException


    :return: {
        'ResourceInfo': {
            'ResourceArn': 'string',
            'RoleArn': 'string',
            'LastModified': datetime(2015, 1, 1)
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
    :param Params: The parameters normally passed to\nClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid\nfor. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By\ndefault, the http method is whatever is used in the method\'s model.

    """
    pass

def get_data_lake_settings(CatalogId=None):
    """
    The AWS Lake Formation principal.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_data_lake_settings(
        CatalogId='string'
    )
    
    
    :type CatalogId: string
    :param CatalogId: The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

    :rtype: dict
ReturnsResponse Syntax{
    'DataLakeSettings': {
        'DataLakeAdmins': [
            {
                'DataLakePrincipalIdentifier': 'string'
            },
        ],
        'CreateDatabaseDefaultPermissions': [
            {
                'Principal': {
                    'DataLakePrincipalIdentifier': 'string'
                },
                'Permissions': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ]
            },
        ],
        'CreateTableDefaultPermissions': [
            {
                'Principal': {
                    'DataLakePrincipalIdentifier': 'string'
                },
                'Permissions': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ]
            },
        ]
    }
}


Response Structure

(dict) --
DataLakeSettings (dict) --A list of AWS Lake Formation principals.

DataLakeAdmins (list) --A list of AWS Lake Formation principals.

(dict) --The AWS Lake Formation principal.

DataLakePrincipalIdentifier (string) --An identifier for the AWS Lake Formation principal.





CreateDatabaseDefaultPermissions (list) --A list of up to three principal permissions entries for default create database permissions.

(dict) --Permissions granted to a principal.

Principal (dict) --The principal who is granted permissions.

DataLakePrincipalIdentifier (string) --An identifier for the AWS Lake Formation principal.



Permissions (list) --The permissions that are granted to the principal.

(string) --






CreateTableDefaultPermissions (list) --A list of up to three principal permissions entries for default create table permissions.

(dict) --Permissions granted to a principal.

Principal (dict) --The principal who is granted permissions.

DataLakePrincipalIdentifier (string) --An identifier for the AWS Lake Formation principal.



Permissions (list) --The permissions that are granted to the principal.

(string) --













Exceptions

LakeFormation.Client.exceptions.InternalServiceException
LakeFormation.Client.exceptions.InvalidInputException
LakeFormation.Client.exceptions.EntityNotFoundException


    :return: {
        'DataLakeSettings': {
            'DataLakeAdmins': [
                {
                    'DataLakePrincipalIdentifier': 'string'
                },
            ],
            'CreateDatabaseDefaultPermissions': [
                {
                    'Principal': {
                        'DataLakePrincipalIdentifier': 'string'
                    },
                    'Permissions': [
                        'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                    ]
                },
            ],
            'CreateTableDefaultPermissions': [
                {
                    'Principal': {
                        'DataLakePrincipalIdentifier': 'string'
                    },
                    'Permissions': [
                        'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_effective_permissions_for_path(CatalogId=None, ResourceArn=None, NextToken=None, MaxResults=None):
    """
    Returns the permissions for a specified table or database resource located at a path in Amazon S3.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_effective_permissions_for_path(
        CatalogId='string',
        ResourceArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CatalogId: string
    :param CatalogId: The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource for which you want to get permissions.\n

    :type NextToken: string
    :param NextToken: A continuation token, if this is not the first call to retrieve this list.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'Permissions': [
        {
            'Principal': {
                'DataLakePrincipalIdentifier': 'string'
            },
            'Resource': {
                'Catalog': {},
                'Database': {
                    'Name': 'string'
                },
                'Table': {
                    'DatabaseName': 'string',
                    'Name': 'string'
                },
                'TableWithColumns': {
                    'DatabaseName': 'string',
                    'Name': 'string',
                    'ColumnNames': [
                        'string',
                    ],
                    'ColumnWildcard': {
                        'ExcludedColumnNames': [
                            'string',
                        ]
                    }
                },
                'DataLocation': {
                    'ResourceArn': 'string'
                }
            },
            'Permissions': [
                'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
            ],
            'PermissionsWithGrantOption': [
                'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Permissions (list) --
A list of the permissions for the specified table or database resource located at the path in Amazon S3.

(dict) --
The permissions granted or revoked on a resource.

Principal (dict) --
The Data Lake principal to be granted or revoked permissions.

DataLakePrincipalIdentifier (string) --
An identifier for the AWS Lake Formation principal.



Resource (dict) --
The resource where permissions are to be granted or revoked.

Catalog (dict) --
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

Database (dict) --
The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.

Name (string) --
The name of the database resource. Unique to the Data Catalog.



Table (dict) --
The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

DatabaseName (string) --
The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

Name (string) --
The name of the table.



TableWithColumns (dict) --
The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.

DatabaseName (string) --
The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

Name (string) --
The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

ColumnNames (list) --
The list of column names for the table. At least one of ColumnNames or ColumnWildcard is required.

(string) --


ColumnWildcard (dict) --
A wildcard specified by a ColumnWildcard object. At least one of ColumnNames or ColumnWildcard is required.

ExcludedColumnNames (list) --
Excludes column names. Any column with this name will be excluded.

(string) --






DataLocation (dict) --
The location of an Amazon S3 path where permissions are granted or revoked.

ResourceArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the data location resource.





Permissions (list) --
The permissions to be granted or revoked on the resource.

(string) --


PermissionsWithGrantOption (list) --
Indicates whether to grant the ability to grant permissions (as a subset of permissions granted).

(string) --






NextToken (string) --
A continuation token, if this is not the first call to retrieve this list.







Exceptions

LakeFormation.Client.exceptions.InvalidInputException
LakeFormation.Client.exceptions.EntityNotFoundException
LakeFormation.Client.exceptions.OperationTimeoutException
LakeFormation.Client.exceptions.InternalServiceException


    :return: {
        'Permissions': [
            {
                'Principal': {
                    'DataLakePrincipalIdentifier': 'string'
                },
                'Resource': {
                    'Catalog': {},
                    'Database': {
                        'Name': 'string'
                    },
                    'Table': {
                        'DatabaseName': 'string',
                        'Name': 'string'
                    },
                    'TableWithColumns': {
                        'DatabaseName': 'string',
                        'Name': 'string',
                        'ColumnNames': [
                            'string',
                        ],
                        'ColumnWildcard': {
                            'ExcludedColumnNames': [
                                'string',
                            ]
                        }
                    },
                    'DataLocation': {
                        'ResourceArn': 'string'
                    }
                },
                'Permissions': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ],
                'PermissionsWithGrantOption': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
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

def grant_permissions(CatalogId=None, Principal=None, Resource=None, Permissions=None, PermissionsWithGrantOption=None):
    """
    Grants permissions to the principal to access metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3.
    For information about permissions, see Security and Access Control to Metadata and Data .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.grant_permissions(
        CatalogId='string',
        Principal={
            'DataLakePrincipalIdentifier': 'string'
        },
        Resource={
            'Catalog': {}
            ,
            'Database': {
                'Name': 'string'
            },
            'Table': {
                'DatabaseName': 'string',
                'Name': 'string'
            },
            'TableWithColumns': {
                'DatabaseName': 'string',
                'Name': 'string',
                'ColumnNames': [
                    'string',
                ],
                'ColumnWildcard': {
                    'ExcludedColumnNames': [
                        'string',
                    ]
                }
            },
            'DataLocation': {
                'ResourceArn': 'string'
            }
        },
        Permissions=[
            'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
        ],
        PermissionsWithGrantOption=[
            'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

    :type Principal: dict
    :param Principal: [REQUIRED]\nThe principal to be granted the permissions on the resource. Supported principals are IAM users or IAM roles, and they are defined by their principal type and their ARN.\nNote that if you define a resource with a particular ARN, then later delete, and recreate a resource with that same ARN, the resource maintains the permissions already granted.\n\nDataLakePrincipalIdentifier (string) --An identifier for the AWS Lake Formation principal.\n\n\n

    :type Resource: dict
    :param Resource: [REQUIRED]\nThe resource to which permissions are to be granted. Resources in AWS Lake Formation are the Data Catalog, databases, and tables.\n\nCatalog (dict) --The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.\n\nDatabase (dict) --The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.\n\nName (string) -- [REQUIRED]The name of the database resource. Unique to the Data Catalog.\n\n\n\nTable (dict) --The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.\n\nDatabaseName (string) -- [REQUIRED]The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.\n\nName (string) -- [REQUIRED]The name of the table.\n\n\n\nTableWithColumns (dict) --The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.\n\nDatabaseName (string) --The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.\n\nName (string) --The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.\n\nColumnNames (list) --The list of column names for the table. At least one of ColumnNames or ColumnWildcard is required.\n\n(string) --\n\n\nColumnWildcard (dict) --A wildcard specified by a ColumnWildcard object. At least one of ColumnNames or ColumnWildcard is required.\n\nExcludedColumnNames (list) --Excludes column names. Any column with this name will be excluded.\n\n(string) --\n\n\n\n\n\n\nDataLocation (dict) --The location of an Amazon S3 path where permissions are granted or revoked.\n\nResourceArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that uniquely identifies the data location resource.\n\n\n\n\n

    :type Permissions: list
    :param Permissions: [REQUIRED]\nThe permissions granted to the principal on the resource. AWS Lake Formation defines privileges to grant and revoke access to metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3. AWS Lake Formation requires that each principal be authorized to perform a specific task on AWS Lake Formation resources.\n\n(string) --\n\n

    :type PermissionsWithGrantOption: list
    :param PermissionsWithGrantOption: Indicates a list of the granted permissions that the principal may pass to other users. These permissions may only be a subset of the permissions granted in the Privileges .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

LakeFormation.Client.exceptions.ConcurrentModificationException
LakeFormation.Client.exceptions.EntityNotFoundException
LakeFormation.Client.exceptions.InvalidInputException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def list_permissions(CatalogId=None, Principal=None, ResourceType=None, Resource=None, NextToken=None, MaxResults=None):
    """
    Returns a list of the principal permissions on the resource, filtered by the permissions of the caller. For example, if you are granted an ALTER permission, you are able to see only the principal permissions for ALTER.
    This operation returns only those permissions that have been explicitly granted.
    For information about permissions, see Security and Access Control to Metadata and Data .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_permissions(
        CatalogId='string',
        Principal={
            'DataLakePrincipalIdentifier': 'string'
        },
        ResourceType='CATALOG'|'DATABASE'|'TABLE'|'DATA_LOCATION',
        Resource={
            'Catalog': {}
            ,
            'Database': {
                'Name': 'string'
            },
            'Table': {
                'DatabaseName': 'string',
                'Name': 'string'
            },
            'TableWithColumns': {
                'DatabaseName': 'string',
                'Name': 'string',
                'ColumnNames': [
                    'string',
                ],
                'ColumnWildcard': {
                    'ExcludedColumnNames': [
                        'string',
                    ]
                }
            },
            'DataLocation': {
                'ResourceArn': 'string'
            }
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CatalogId: string
    :param CatalogId: The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

    :type Principal: dict
    :param Principal: Specifies a principal to filter the permissions returned.\n\nDataLakePrincipalIdentifier (string) --An identifier for the AWS Lake Formation principal.\n\n\n

    :type ResourceType: string
    :param ResourceType: Specifies a resource type to filter the permissions returned.

    :type Resource: dict
    :param Resource: A resource where you will get a list of the principal permissions.\nThis operation does not support getting privileges on a table with columns. Instead, call this operation on the table, and the operation returns the table and the table w columns.\n\nCatalog (dict) --The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.\n\nDatabase (dict) --The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.\n\nName (string) -- [REQUIRED]The name of the database resource. Unique to the Data Catalog.\n\n\n\nTable (dict) --The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.\n\nDatabaseName (string) -- [REQUIRED]The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.\n\nName (string) -- [REQUIRED]The name of the table.\n\n\n\nTableWithColumns (dict) --The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.\n\nDatabaseName (string) --The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.\n\nName (string) --The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.\n\nColumnNames (list) --The list of column names for the table. At least one of ColumnNames or ColumnWildcard is required.\n\n(string) --\n\n\nColumnWildcard (dict) --A wildcard specified by a ColumnWildcard object. At least one of ColumnNames or ColumnWildcard is required.\n\nExcludedColumnNames (list) --Excludes column names. Any column with this name will be excluded.\n\n(string) --\n\n\n\n\n\n\nDataLocation (dict) --The location of an Amazon S3 path where permissions are granted or revoked.\n\nResourceArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that uniquely identifies the data location resource.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: A continuation token, if this is not the first call to retrieve this list.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'PrincipalResourcePermissions': [
        {
            'Principal': {
                'DataLakePrincipalIdentifier': 'string'
            },
            'Resource': {
                'Catalog': {},
                'Database': {
                    'Name': 'string'
                },
                'Table': {
                    'DatabaseName': 'string',
                    'Name': 'string'
                },
                'TableWithColumns': {
                    'DatabaseName': 'string',
                    'Name': 'string',
                    'ColumnNames': [
                        'string',
                    ],
                    'ColumnWildcard': {
                        'ExcludedColumnNames': [
                            'string',
                        ]
                    }
                },
                'DataLocation': {
                    'ResourceArn': 'string'
                }
            },
            'Permissions': [
                'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
            ],
            'PermissionsWithGrantOption': [
                'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

PrincipalResourcePermissions (list) --
A list of principals and their permissions on the resource for the specified principal and resource types.

(dict) --
The permissions granted or revoked on a resource.

Principal (dict) --
The Data Lake principal to be granted or revoked permissions.

DataLakePrincipalIdentifier (string) --
An identifier for the AWS Lake Formation principal.



Resource (dict) --
The resource where permissions are to be granted or revoked.

Catalog (dict) --
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

Database (dict) --
The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.

Name (string) --
The name of the database resource. Unique to the Data Catalog.



Table (dict) --
The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

DatabaseName (string) --
The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

Name (string) --
The name of the table.



TableWithColumns (dict) --
The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.

DatabaseName (string) --
The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

Name (string) --
The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

ColumnNames (list) --
The list of column names for the table. At least one of ColumnNames or ColumnWildcard is required.

(string) --


ColumnWildcard (dict) --
A wildcard specified by a ColumnWildcard object. At least one of ColumnNames or ColumnWildcard is required.

ExcludedColumnNames (list) --
Excludes column names. Any column with this name will be excluded.

(string) --






DataLocation (dict) --
The location of an Amazon S3 path where permissions are granted or revoked.

ResourceArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the data location resource.





Permissions (list) --
The permissions to be granted or revoked on the resource.

(string) --


PermissionsWithGrantOption (list) --
Indicates whether to grant the ability to grant permissions (as a subset of permissions granted).

(string) --






NextToken (string) --
A continuation token, if this is not the first call to retrieve this list.







Exceptions

LakeFormation.Client.exceptions.InvalidInputException
LakeFormation.Client.exceptions.OperationTimeoutException
LakeFormation.Client.exceptions.InternalServiceException


    :return: {
        'PrincipalResourcePermissions': [
            {
                'Principal': {
                    'DataLakePrincipalIdentifier': 'string'
                },
                'Resource': {
                    'Catalog': {},
                    'Database': {
                        'Name': 'string'
                    },
                    'Table': {
                        'DatabaseName': 'string',
                        'Name': 'string'
                    },
                    'TableWithColumns': {
                        'DatabaseName': 'string',
                        'Name': 'string',
                        'ColumnNames': [
                            'string',
                        ],
                        'ColumnWildcard': {
                            'ExcludedColumnNames': [
                                'string',
                            ]
                        }
                    },
                    'DataLocation': {
                        'ResourceArn': 'string'
                    }
                },
                'Permissions': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ],
                'PermissionsWithGrantOption': [
                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_resources(FilterConditionList=None, MaxResults=None, NextToken=None):
    """
    Lists the resources registered to be managed by the Data Catalog.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resources(
        FilterConditionList=[
            {
                'Field': 'RESOURCE_ARN'|'ROLE_ARN'|'LAST_MODIFIED',
                'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH'|'IN'|'BETWEEN',
                'StringValueList': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type FilterConditionList: list
    :param FilterConditionList: Any applicable row-level and/or column-level filtering conditions for the resources.\n\n(dict) --This structure describes the filtering of columns in a table based on a filter condition.\n\nField (string) --The field to filter in the filter condition.\n\nComparisonOperator (string) --The comparison operator used in the filter condition.\n\nStringValueList (list) --A string with values used in evaluating the filter condition.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of resource results.

    :type NextToken: string
    :param NextToken: A continuation token, if this is not the first call to retrieve these resources.

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceInfoList': [
        {
            'ResourceArn': 'string',
            'RoleArn': 'string',
            'LastModified': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ResourceInfoList (list) --
A summary of the data lake resources.

(dict) --
A structure containing information about an AWS Lake Formation resource.

ResourceArn (string) --
The Amazon Resource Name (ARN) of the resource.

RoleArn (string) --
The IAM role that registered a resource.

LastModified (datetime) --
The date and time the resource was last modified.





NextToken (string) --
A continuation token, if this is not the first call to retrieve these resources.







Exceptions

LakeFormation.Client.exceptions.InvalidInputException
LakeFormation.Client.exceptions.InternalServiceException
LakeFormation.Client.exceptions.OperationTimeoutException


    :return: {
        'ResourceInfoList': [
            {
                'ResourceArn': 'string',
                'RoleArn': 'string',
                'LastModified': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    LakeFormation.Client.exceptions.InvalidInputException
    LakeFormation.Client.exceptions.InternalServiceException
    LakeFormation.Client.exceptions.OperationTimeoutException
    
    """
    pass

def put_data_lake_settings(CatalogId=None, DataLakeSettings=None):
    """
    The AWS Lake Formation principal.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_data_lake_settings(
        CatalogId='string',
        DataLakeSettings={
            'DataLakeAdmins': [
                {
                    'DataLakePrincipalIdentifier': 'string'
                },
            ],
            'CreateDatabaseDefaultPermissions': [
                {
                    'Principal': {
                        'DataLakePrincipalIdentifier': 'string'
                    },
                    'Permissions': [
                        'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                    ]
                },
            ],
            'CreateTableDefaultPermissions': [
                {
                    'Principal': {
                        'DataLakePrincipalIdentifier': 'string'
                    },
                    'Permissions': [
                        'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                    ]
                },
            ]
        }
    )
    
    
    :type CatalogId: string
    :param CatalogId: The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

    :type DataLakeSettings: dict
    :param DataLakeSettings: [REQUIRED]\nA list of AWS Lake Formation principals.\n\nDataLakeAdmins (list) --A list of AWS Lake Formation principals.\n\n(dict) --The AWS Lake Formation principal.\n\nDataLakePrincipalIdentifier (string) --An identifier for the AWS Lake Formation principal.\n\n\n\n\n\nCreateDatabaseDefaultPermissions (list) --A list of up to three principal permissions entries for default create database permissions.\n\n(dict) --Permissions granted to a principal.\n\nPrincipal (dict) --The principal who is granted permissions.\n\nDataLakePrincipalIdentifier (string) --An identifier for the AWS Lake Formation principal.\n\n\n\nPermissions (list) --The permissions that are granted to the principal.\n\n(string) --\n\n\n\n\n\n\nCreateTableDefaultPermissions (list) --A list of up to three principal permissions entries for default create table permissions.\n\n(dict) --Permissions granted to a principal.\n\nPrincipal (dict) --The principal who is granted permissions.\n\nDataLakePrincipalIdentifier (string) --An identifier for the AWS Lake Formation principal.\n\n\n\nPermissions (list) --The permissions that are granted to the principal.\n\n(string) --\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

LakeFormation.Client.exceptions.InternalServiceException
LakeFormation.Client.exceptions.InvalidInputException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def register_resource(ResourceArn=None, UseServiceLinkedRole=None, RoleArn=None):
    """
    Registers the resource as managed by the Data Catalog.
    To add or update data, Lake Formation needs read/write access to the chosen Amazon S3 path. Choose a role that you know has permission to do this, or choose the AWSServiceRoleForLakeFormationDataAccess service-linked role. When you register the first Amazon S3 path, the service-linked role and a new inline policy are created on your behalf. Lake Formation adds the first path to the inline policy and attaches it to the service-linked role. When you register subsequent paths, Lake Formation adds the path to the existing policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_resource(
        ResourceArn='string',
        UseServiceLinkedRole=True|False,
        RoleArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource that you want to register.\n

    :type UseServiceLinkedRole: boolean
    :param UseServiceLinkedRole: Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog.

    :type RoleArn: string
    :param RoleArn: The identifier for the role.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

LakeFormation.Client.exceptions.InvalidInputException
LakeFormation.Client.exceptions.InternalServiceException
LakeFormation.Client.exceptions.OperationTimeoutException
LakeFormation.Client.exceptions.AlreadyExistsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def revoke_permissions(CatalogId=None, Principal=None, Resource=None, Permissions=None, PermissionsWithGrantOption=None):
    """
    Revokes permissions to the principal to access metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.revoke_permissions(
        CatalogId='string',
        Principal={
            'DataLakePrincipalIdentifier': 'string'
        },
        Resource={
            'Catalog': {}
            ,
            'Database': {
                'Name': 'string'
            },
            'Table': {
                'DatabaseName': 'string',
                'Name': 'string'
            },
            'TableWithColumns': {
                'DatabaseName': 'string',
                'Name': 'string',
                'ColumnNames': [
                    'string',
                ],
                'ColumnWildcard': {
                    'ExcludedColumnNames': [
                        'string',
                    ]
                }
            },
            'DataLocation': {
                'ResourceArn': 'string'
            }
        },
        Permissions=[
            'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
        ],
        PermissionsWithGrantOption=[
            'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
        ]
    )
    
    
    :type CatalogId: string
    :param CatalogId: The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

    :type Principal: dict
    :param Principal: [REQUIRED]\nThe principal to be revoked permissions on the resource.\n\nDataLakePrincipalIdentifier (string) --An identifier for the AWS Lake Formation principal.\n\n\n

    :type Resource: dict
    :param Resource: [REQUIRED]\nThe resource to which permissions are to be revoked.\n\nCatalog (dict) --The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.\n\nDatabase (dict) --The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.\n\nName (string) -- [REQUIRED]The name of the database resource. Unique to the Data Catalog.\n\n\n\nTable (dict) --The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.\n\nDatabaseName (string) -- [REQUIRED]The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.\n\nName (string) -- [REQUIRED]The name of the table.\n\n\n\nTableWithColumns (dict) --The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.\n\nDatabaseName (string) --The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.\n\nName (string) --The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.\n\nColumnNames (list) --The list of column names for the table. At least one of ColumnNames or ColumnWildcard is required.\n\n(string) --\n\n\nColumnWildcard (dict) --A wildcard specified by a ColumnWildcard object. At least one of ColumnNames or ColumnWildcard is required.\n\nExcludedColumnNames (list) --Excludes column names. Any column with this name will be excluded.\n\n(string) --\n\n\n\n\n\n\nDataLocation (dict) --The location of an Amazon S3 path where permissions are granted or revoked.\n\nResourceArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) that uniquely identifies the data location resource.\n\n\n\n\n

    :type Permissions: list
    :param Permissions: [REQUIRED]\nThe permissions revoked to the principal on the resource. For information about permissions, see Security and Access Control to Metadata and Data .\n\n(string) --\n\n

    :type PermissionsWithGrantOption: list
    :param PermissionsWithGrantOption: Indicates a list of permissions for which to revoke the grant option allowing the principal to pass permissions to other principals.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

LakeFormation.Client.exceptions.ConcurrentModificationException
LakeFormation.Client.exceptions.EntityNotFoundException
LakeFormation.Client.exceptions.InvalidInputException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_resource(RoleArn=None, ResourceArn=None):
    """
    Updates the data access role used for vending access to the given (registered) resource in AWS Lake Formation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_resource(
        RoleArn='string',
        ResourceArn='string'
    )
    
    
    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nThe new role to use for the given resource registered in AWS Lake Formation.\n

    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe resource ARN.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

LakeFormation.Client.exceptions.InvalidInputException
LakeFormation.Client.exceptions.InternalServiceException
LakeFormation.Client.exceptions.OperationTimeoutException
LakeFormation.Client.exceptions.EntityNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

