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

def cancel_job(JobId=None):
    """
    This operation cancels a job. Jobs can be cancelled only when they are in the WAITING state.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe unique identifier for a job.\n

    """
    pass

def create_data_set(AssetType=None, Description=None, Name=None, Tags=None):
    """
    This operation creates a data set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_data_set(
        AssetType='S3_SNAPSHOT',
        Description='string',
        Name='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type AssetType: string
    :param AssetType: [REQUIRED]\nThe type of file your data is stored in. Currently, the supported asset type is S3_SNAPSHOT.\n

    :type Description: string
    :param Description: [REQUIRED]\nA description for the data set. This value can be up to 16,348 characters long.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the data set.\n

    :type Tags: dict
    :param Tags: A data set tag is an optional label that you can assign to a data set when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to these data sets and revisions.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'AssetType': 'S3_SNAPSHOT',
    'CreatedAt': datetime(2015, 1, 1),
    'Description': 'string',
    'Id': 'string',
    'Name': 'string',
    'Origin': 'OWNED'|'ENTITLED',
    'OriginDetails': {
        'ProductId': 'string'
    },
    'SourceId': 'string',
    'Tags': {
        'string': 'string'
    },
    'UpdatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --
201 response

Arn (string) --
The ARN for the data set.

AssetType (string) --
The type of file your data is stored in. Currently, the supported asset type is S3_SNAPSHOT.

CreatedAt (datetime) --
The date and time that the data set was created, in ISO 8601 format.

Description (string) --
The description for the data set.

Id (string) --
The unique identifier for the data set.

Name (string) --
The name of the data set.

Origin (string) --
A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).

OriginDetails (dict) --
If the origin of this data set is ENTITLED, includes the details for the product on AWS Marketplace.

ProductId (string) --


SourceId (string) --
The data set ID of the owned data set corresponding to the entitled data set being viewed. This parameter is returned when a data set owner is viewing the entitled copy of its owned data set.

Tags (dict) --
The tags for the data set.

(string) --
(string) --




UpdatedAt (datetime) --
The date and time that the data set was last updated, in ISO 8601 format.







Exceptions

DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException
DataExchange.Client.exceptions.ServiceLimitExceededException
DataExchange.Client.exceptions.AccessDeniedException


    :return: {
        'Arn': 'string',
        'AssetType': 'S3_SNAPSHOT',
        'CreatedAt': datetime(2015, 1, 1),
        'Description': 'string',
        'Id': 'string',
        'Name': 'string',
        'Origin': 'OWNED'|'ENTITLED',
        'OriginDetails': {
            'ProductId': 'string'
        },
        'SourceId': 'string',
        'Tags': {
            'string': 'string'
        },
        'UpdatedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    ProductId (string) --
    
    """
    pass

def create_job(Details=None, Type=None):
    """
    This operation creates a job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_job(
        Details={
            'ExportAssetToSignedUrl': {
                'AssetId': 'string',
                'DataSetId': 'string',
                'RevisionId': 'string'
            },
            'ExportAssetsToS3': {
                'AssetDestinations': [
                    {
                        'AssetId': 'string',
                        'Bucket': 'string',
                        'Key': 'string'
                    },
                ],
                'DataSetId': 'string',
                'Encryption': {
                    'KmsKeyArn': 'string',
                    'Type': 'aws:kms'|'AES256'
                },
                'RevisionId': 'string'
            },
            'ImportAssetFromSignedUrl': {
                'AssetName': 'string',
                'DataSetId': 'string',
                'Md5Hash': 'string',
                'RevisionId': 'string'
            },
            'ImportAssetsFromS3': {
                'AssetSources': [
                    {
                        'Bucket': 'string',
                        'Key': 'string'
                    },
                ],
                'DataSetId': 'string',
                'RevisionId': 'string'
            }
        },
        Type='IMPORT_ASSETS_FROM_S3'|'IMPORT_ASSET_FROM_SIGNED_URL'|'EXPORT_ASSETS_TO_S3'|'EXPORT_ASSET_TO_SIGNED_URL'
    )
    
    
    :type Details: dict
    :param Details: [REQUIRED]\nThe details for the CreateJob request.\n\nExportAssetToSignedUrl (dict) --Details about the export to signed URL request.\n\nAssetId (string) -- [REQUIRED]The unique identifier for the asset that is exported to a signed URL.\n\nDataSetId (string) -- [REQUIRED]The unique identifier for the data set associated with this export job.\n\nRevisionId (string) -- [REQUIRED]The unique identifier for the revision associated with this export request.\n\n\n\nExportAssetsToS3 (dict) --Details about the export to Amazon S3 request.\n\nAssetDestinations (list) -- [REQUIRED]The destination for the asset.\n\n(dict) --The destination for the asset.\n\nAssetId (string) -- [REQUIRED]The unique identifier for the asset.\n\nBucket (string) -- [REQUIRED]The S3 bucket that is the destination for the asset.\n\nKey (string) --The name of the object in Amazon S3 for the asset.\n\n\n\n\n\nDataSetId (string) -- [REQUIRED]The unique identifier for the data set associated with this export job.\n\nEncryption (dict) --Encryption configuration for the export job.\n\nKmsKeyArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the the AWS KMS key you want to use to encrypt the Amazon S3 objects. This parameter is required if you choose aws:kms as an encryption type.\n\nType (string) -- [REQUIRED]The type of server side encryption used for encrypting the objects in Amazon S3.\n\n\n\nRevisionId (string) -- [REQUIRED]The unique identifier for the revision associated with this export request.\n\n\n\nImportAssetFromSignedUrl (dict) --Details about the import from signed URL request.\n\nAssetName (string) -- [REQUIRED]The name of the asset. When importing from Amazon S3, the S3 object key is used as the asset name.\n\nDataSetId (string) -- [REQUIRED]The unique identifier for the data set associated with this import job.\n\nMd5Hash (string) -- [REQUIRED]The Base64-encoded Md5 hash for the asset, used to ensure the integrity of the file at that location.\n\nRevisionId (string) -- [REQUIRED]The unique identifier for the revision associated with this import request.\n\n\n\nImportAssetsFromS3 (dict) --Details about the import from Amazon S3 request.\n\nAssetSources (list) -- [REQUIRED]Is a list of S3 bucket and object key pairs.\n\n(dict) --The source of the assets.\n\nBucket (string) -- [REQUIRED]The S3 bucket that\'s part of the source of the asset.\n\nKey (string) -- [REQUIRED]The name of the object in Amazon S3 for the asset.\n\n\n\n\n\nDataSetId (string) -- [REQUIRED]The unique identifier for the data set associated with this import job.\n\nRevisionId (string) -- [REQUIRED]The unique identifier for the revision associated with this import request.\n\n\n\n\n

    :type Type: string
    :param Type: [REQUIRED]\nThe type of job to be created.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'CreatedAt': datetime(2015, 1, 1),
    'Details': {
        'ExportAssetToSignedUrl': {
            'AssetId': 'string',
            'DataSetId': 'string',
            'RevisionId': 'string',
            'SignedUrl': 'string',
            'SignedUrlExpiresAt': datetime(2015, 1, 1)
        },
        'ExportAssetsToS3': {
            'AssetDestinations': [
                {
                    'AssetId': 'string',
                    'Bucket': 'string',
                    'Key': 'string'
                },
            ],
            'DataSetId': 'string',
            'Encryption': {
                'KmsKeyArn': 'string',
                'Type': 'aws:kms'|'AES256'
            },
            'RevisionId': 'string'
        },
        'ImportAssetFromSignedUrl': {
            'AssetName': 'string',
            'DataSetId': 'string',
            'Md5Hash': 'string',
            'RevisionId': 'string',
            'SignedUrl': 'string',
            'SignedUrlExpiresAt': datetime(2015, 1, 1)
        },
        'ImportAssetsFromS3': {
            'AssetSources': [
                {
                    'Bucket': 'string',
                    'Key': 'string'
                },
            ],
            'DataSetId': 'string',
            'RevisionId': 'string'
        }
    },
    'Errors': [
        {
            'Code': 'ACCESS_DENIED_EXCEPTION'|'INTERNAL_SERVER_EXCEPTION'|'MALWARE_DETECTED'|'RESOURCE_NOT_FOUND_EXCEPTION'|'SERVICE_QUOTA_EXCEEDED_EXCEPTION'|'VALIDATION_EXCEPTION'|'MALWARE_SCAN_ENCRYPTED_FILE',
            'Details': {
                'ImportAssetFromSignedUrlJobErrorDetails': {
                    'AssetName': 'string'
                },
                'ImportAssetsFromS3JobErrorDetails': [
                    {
                        'Bucket': 'string',
                        'Key': 'string'
                    },
                ]
            },
            'LimitName': 'Assets per revision'|'Asset size in GB',
            'LimitValue': 123.0,
            'Message': 'string',
            'ResourceId': 'string',
            'ResourceType': 'REVISION'|'ASSET'
        },
    ],
    'Id': 'string',
    'State': 'WAITING'|'IN_PROGRESS'|'ERROR'|'COMPLETED'|'CANCELLED'|'TIMED_OUT',
    'Type': 'IMPORT_ASSETS_FROM_S3'|'IMPORT_ASSET_FROM_SIGNED_URL'|'EXPORT_ASSETS_TO_S3'|'EXPORT_ASSET_TO_SIGNED_URL',
    'UpdatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --
201 response

Arn (string) --
The ARN for the job.

CreatedAt (datetime) --
The date and time that the job was created, in ISO 8601 format.

Details (dict) --
Details about the job.

ExportAssetToSignedUrl (dict) --
Details for the export to signed URL response.

AssetId (string) --
The unique identifier for the asset associated with this export job.

DataSetId (string) --
The unique identifier for the data set associated with this export job.

RevisionId (string) --
The unique identifier for the revision associated with this export response.

SignedUrl (string) --
The signed URL for the export request.

SignedUrlExpiresAt (datetime) --
The date and time that the signed URL expires, in ISO 8601 format.



ExportAssetsToS3 (dict) --
Details for the export to Amazon S3 response.

AssetDestinations (list) --
The destination in Amazon S3 where the asset is exported.

(dict) --
The destination for the asset.

AssetId (string) --
The unique identifier for the asset.

Bucket (string) --
The S3 bucket that is the destination for the asset.

Key (string) --
The name of the object in Amazon S3 for the asset.





DataSetId (string) --
The unique identifier for the data set associated with this export job.

Encryption (dict) --
Encryption configuration of the export job.

KmsKeyArn (string) --
The Amazon Resource Name (ARN) of the the AWS KMS key you want to use to encrypt the Amazon S3 objects. This parameter is required if you choose aws:kms as an encryption type.

Type (string) --
The type of server side encryption used for encrypting the objects in Amazon S3.



RevisionId (string) --
The unique identifier for the revision associated with this export response.



ImportAssetFromSignedUrl (dict) --
Details for the import from signed URL response.

AssetName (string) --
The name for the asset associated with this import response.

DataSetId (string) --
The unique identifier for the data set associated with this import job.

Md5Hash (string) --
The Base64-encoded Md5 hash for the asset, used to ensure the integrity of the file at that location.

RevisionId (string) --
The unique identifier for the revision associated with this import response.

SignedUrl (string) --
The signed URL.

SignedUrlExpiresAt (datetime) --
The time and date at which the signed URL expires, in ISO 8601 format.



ImportAssetsFromS3 (dict) --
Details for the import from Amazon S3 response.

AssetSources (list) --
Is a list of Amazon S3 bucket and object key pairs.

(dict) --
The source of the assets.

Bucket (string) --
The S3 bucket that\'s part of the source of the asset.

Key (string) --
The name of the object in Amazon S3 for the asset.





DataSetId (string) --
The unique identifier for the data set associated with this import job.

RevisionId (string) --
The unique identifier for the revision associated with this import response.





Errors (list) --
The errors associated with jobs.

(dict) -- An error that occurred with the job request.

Code (string) -- The code for the job error.

Details (dict) --

ImportAssetFromSignedUrlJobErrorDetails (dict) --

AssetName (string) --
The name of the asset. When importing from Amazon S3, the S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target S3 object key.



ImportAssetsFromS3JobErrorDetails (list) --
The list of sources for the assets.

(dict) --
The source of the assets.

Bucket (string) --
The S3 bucket that\'s part of the source of the asset.

Key (string) --
The name of the object in Amazon S3 for the asset.







LimitName (string) --
The name of the limit that was reached.

LimitValue (float) -- The value of the exceeded limit.

Message (string) -- The message related to the job error.

ResourceId (string) -- The unique identifier for the resource related to the error.

ResourceType (string) -- The type of resource related to the error.





Id (string) --
The unique identifier for the job.

State (string) --
The state of the job.

Type (string) --
The job type.

UpdatedAt (datetime) --
The date and time that the job was last updated, in ISO 8601 format.







Exceptions

DataExchange.Client.exceptions.ResourceNotFoundException
DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException
DataExchange.Client.exceptions.AccessDeniedException


    :return: {
        'Arn': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'Details': {
            'ExportAssetToSignedUrl': {
                'AssetId': 'string',
                'DataSetId': 'string',
                'RevisionId': 'string',
                'SignedUrl': 'string',
                'SignedUrlExpiresAt': datetime(2015, 1, 1)
            },
            'ExportAssetsToS3': {
                'AssetDestinations': [
                    {
                        'AssetId': 'string',
                        'Bucket': 'string',
                        'Key': 'string'
                    },
                ],
                'DataSetId': 'string',
                'Encryption': {
                    'KmsKeyArn': 'string',
                    'Type': 'aws:kms'|'AES256'
                },
                'RevisionId': 'string'
            },
            'ImportAssetFromSignedUrl': {
                'AssetName': 'string',
                'DataSetId': 'string',
                'Md5Hash': 'string',
                'RevisionId': 'string',
                'SignedUrl': 'string',
                'SignedUrlExpiresAt': datetime(2015, 1, 1)
            },
            'ImportAssetsFromS3': {
                'AssetSources': [
                    {
                        'Bucket': 'string',
                        'Key': 'string'
                    },
                ],
                'DataSetId': 'string',
                'RevisionId': 'string'
            }
        },
        'Errors': [
            {
                'Code': 'ACCESS_DENIED_EXCEPTION'|'INTERNAL_SERVER_EXCEPTION'|'MALWARE_DETECTED'|'RESOURCE_NOT_FOUND_EXCEPTION'|'SERVICE_QUOTA_EXCEEDED_EXCEPTION'|'VALIDATION_EXCEPTION'|'MALWARE_SCAN_ENCRYPTED_FILE',
                'Details': {
                    'ImportAssetFromSignedUrlJobErrorDetails': {
                        'AssetName': 'string'
                    },
                    'ImportAssetsFromS3JobErrorDetails': [
                        {
                            'Bucket': 'string',
                            'Key': 'string'
                        },
                    ]
                },
                'LimitName': 'Assets per revision'|'Asset size in GB',
                'LimitValue': 123.0,
                'Message': 'string',
                'ResourceId': 'string',
                'ResourceType': 'REVISION'|'ASSET'
            },
        ],
        'Id': 'string',
        'State': 'WAITING'|'IN_PROGRESS'|'ERROR'|'COMPLETED'|'CANCELLED'|'TIMED_OUT',
        'Type': 'IMPORT_ASSETS_FROM_S3'|'IMPORT_ASSET_FROM_SIGNED_URL'|'EXPORT_ASSETS_TO_S3'|'EXPORT_ASSET_TO_SIGNED_URL',
        'UpdatedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    DataExchange.Client.exceptions.ResourceNotFoundException
    DataExchange.Client.exceptions.ThrottlingException
    DataExchange.Client.exceptions.ValidationException
    DataExchange.Client.exceptions.InternalServerException
    DataExchange.Client.exceptions.AccessDeniedException
    
    """
    pass

def create_revision(Comment=None, DataSetId=None, Tags=None):
    """
    This operation creates a revision for a data set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_revision(
        Comment='string',
        DataSetId='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Comment: string
    :param Comment: An optional comment about the revision.

    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe unique identifier for a data set.\n

    :type Tags: dict
    :param Tags: A revision tag is an optional label that you can assign to a revision when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to these data sets and revisions.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'Comment': 'string',
    'CreatedAt': datetime(2015, 1, 1),
    'DataSetId': 'string',
    'Finalized': True|False,
    'Id': 'string',
    'SourceId': 'string',
    'Tags': {
        'string': 'string'
    },
    'UpdatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --
201 response

Arn (string) --
The ARN for the revision

Comment (string) --
An optional comment about the revision.

CreatedAt (datetime) --
The date and time that the revision was created, in ISO 8601 format.

DataSetId (string) --
The unique identifier for the data set associated with this revision.

Finalized (boolean) --
To publish a revision to a data set in a product, the revision must first be finalized. Finalizing a revision tells AWS Data Exchange that your changes to the assets in the revision are complete. After it\'s in this read-only state, you can publish the revision to your products.
Finalized revisions can be published through the AWS Data Exchange console or the AWS Marketplace Catalog API, using the StartChangeSet AWS Marketplace Catalog API action. When using the API, revisions are uniquely identified by their ARN.

Id (string) --
The unique identifier for the revision.

SourceId (string) --
The revision ID of the owned revision corresponding to the entitled revision being viewed. This parameter is returned when a revision owner is viewing the entitled copy of its owned revision.

Tags (dict) --
The tags for the revision.

(string) --
(string) --




UpdatedAt (datetime) --
The date and time that the revision was last updated, in ISO 8601 format.







Exceptions

DataExchange.Client.exceptions.ResourceNotFoundException
DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException
DataExchange.Client.exceptions.AccessDeniedException


    :return: {
        'Arn': 'string',
        'Comment': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'DataSetId': 'string',
        'Finalized': True|False,
        'Id': 'string',
        'SourceId': 'string',
        'Tags': {
            'string': 'string'
        },
        'UpdatedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def delete_asset(AssetId=None, DataSetId=None, RevisionId=None):
    """
    This operation deletes an asset.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_asset(
        AssetId='string',
        DataSetId='string',
        RevisionId='string'
    )
    
    
    :type AssetId: string
    :param AssetId: [REQUIRED]\nThe unique identifier for an asset.\n

    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe unique identifier for a data set.\n

    :type RevisionId: string
    :param RevisionId: [REQUIRED]\nThe unique identifier for a revision.\n

    :returns: 
    DataExchange.Client.exceptions.ValidationException
    DataExchange.Client.exceptions.InternalServerException
    DataExchange.Client.exceptions.AccessDeniedException
    DataExchange.Client.exceptions.ResourceNotFoundException
    DataExchange.Client.exceptions.ThrottlingException
    DataExchange.Client.exceptions.ConflictException
    
    """
    pass

def delete_data_set(DataSetId=None):
    """
    This operation deletes a data set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_data_set(
        DataSetId='string'
    )
    
    
    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe unique identifier for a data set.\n

    """
    pass

def delete_revision(DataSetId=None, RevisionId=None):
    """
    This operation deletes a revision.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_revision(
        DataSetId='string',
        RevisionId='string'
    )
    
    
    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe unique identifier for a data set.\n

    :type RevisionId: string
    :param RevisionId: [REQUIRED]\nThe unique identifier for a revision.\n

    :returns: 
    DataExchange.Client.exceptions.ValidationException
    DataExchange.Client.exceptions.InternalServerException
    DataExchange.Client.exceptions.AccessDeniedException
    DataExchange.Client.exceptions.ResourceNotFoundException
    DataExchange.Client.exceptions.ThrottlingException
    DataExchange.Client.exceptions.ConflictException
    
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

def get_asset(AssetId=None, DataSetId=None, RevisionId=None):
    """
    This operation returns information about an asset.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_asset(
        AssetId='string',
        DataSetId='string',
        RevisionId='string'
    )
    
    
    :type AssetId: string
    :param AssetId: [REQUIRED]\nThe unique identifier for an asset.\n

    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe unique identifier for a data set.\n

    :type RevisionId: string
    :param RevisionId: [REQUIRED]\nThe unique identifier for a revision.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'AssetDetails': {
        'S3SnapshotAsset': {
            'Size': 123.0
        }
    },
    'AssetType': 'S3_SNAPSHOT',
    'CreatedAt': datetime(2015, 1, 1),
    'DataSetId': 'string',
    'Id': 'string',
    'Name': 'string',
    'RevisionId': 'string',
    'SourceId': 'string',
    'UpdatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --
200 response

Arn (string) --
The ARN for the asset.

AssetDetails (dict) --
Information about the asset, including its size.

S3SnapshotAsset (dict) --
The S3 object that is the asset.

Size (float) --
The size of the S3 object that is the object.





AssetType (string) --
The type of file your data is stored in. Currently, the supported asset type is S3_SNAPSHOT.

CreatedAt (datetime) --
The date and time that the asset was created, in ISO 8601 format.

DataSetId (string) --
The unique identifier for the data set associated with this asset.

Id (string) --
The unique identifier for the asset.

Name (string) --
The name of the asset When importing from Amazon S3, the S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target S3 object key.

RevisionId (string) --
The unique identifier for the revision associated with this asset.

SourceId (string) --
The asset ID of the owned asset corresponding to the entitled asset being viewed. This parameter is returned when an asset owner is viewing the entitled copy of its owned asset.

UpdatedAt (datetime) --
The date and time that the asset was last updated, in ISO 8601 format.







Exceptions

DataExchange.Client.exceptions.ResourceNotFoundException
DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException


    :return: {
        'Arn': 'string',
        'AssetDetails': {
            'S3SnapshotAsset': {
                'Size': 123.0
            }
        },
        'AssetType': 'S3_SNAPSHOT',
        'CreatedAt': datetime(2015, 1, 1),
        'DataSetId': 'string',
        'Id': 'string',
        'Name': 'string',
        'RevisionId': 'string',
        'SourceId': 'string',
        'UpdatedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    DataExchange.Client.exceptions.ResourceNotFoundException
    DataExchange.Client.exceptions.ThrottlingException
    DataExchange.Client.exceptions.ValidationException
    DataExchange.Client.exceptions.InternalServerException
    
    """
    pass

def get_data_set(DataSetId=None):
    """
    This operation returns information about a data set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_data_set(
        DataSetId='string'
    )
    
    
    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe unique identifier for a data set.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Arn': 'string',
    'AssetType': 'S3_SNAPSHOT',
    'CreatedAt': datetime(2015, 1, 1),
    'Description': 'string',
    'Id': 'string',
    'Name': 'string',
    'Origin': 'OWNED'|'ENTITLED',
    'OriginDetails': {
        'ProductId': 'string'
    },
    'SourceId': 'string',
    'Tags': {
        'string': 'string'
    },
    'UpdatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --200 response

Arn (string) --The ARN for the data set.

AssetType (string) --The type of file your data is stored in. Currently, the supported asset type is S3_SNAPSHOT.

CreatedAt (datetime) --The date and time that the data set was created, in ISO 8601 format.

Description (string) --The description for the data set.

Id (string) --The unique identifier for the data set.

Name (string) --The name of the data set.

Origin (string) --A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).

OriginDetails (dict) --If the origin of this data set is ENTITLED, includes the details for the product on AWS Marketplace.

ProductId (string) --


SourceId (string) --The data set ID of the owned data set corresponding to the entitled data set being viewed. This parameter is returned when a data set owner is viewing the entitled copy of its owned data set.

Tags (dict) --The tags for the data set.

(string) --
(string) --




UpdatedAt (datetime) --The date and time that the data set was last updated, in ISO 8601 format.






Exceptions

DataExchange.Client.exceptions.ResourceNotFoundException
DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException


    :return: {
        'Arn': 'string',
        'AssetType': 'S3_SNAPSHOT',
        'CreatedAt': datetime(2015, 1, 1),
        'Description': 'string',
        'Id': 'string',
        'Name': 'string',
        'Origin': 'OWNED'|'ENTITLED',
        'OriginDetails': {
            'ProductId': 'string'
        },
        'SourceId': 'string',
        'Tags': {
            'string': 'string'
        },
        'UpdatedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_job(JobId=None):
    """
    This operation returns information about a job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe unique identifier for a job.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Arn': 'string',
    'CreatedAt': datetime(2015, 1, 1),
    'Details': {
        'ExportAssetToSignedUrl': {
            'AssetId': 'string',
            'DataSetId': 'string',
            'RevisionId': 'string',
            'SignedUrl': 'string',
            'SignedUrlExpiresAt': datetime(2015, 1, 1)
        },
        'ExportAssetsToS3': {
            'AssetDestinations': [
                {
                    'AssetId': 'string',
                    'Bucket': 'string',
                    'Key': 'string'
                },
            ],
            'DataSetId': 'string',
            'Encryption': {
                'KmsKeyArn': 'string',
                'Type': 'aws:kms'|'AES256'
            },
            'RevisionId': 'string'
        },
        'ImportAssetFromSignedUrl': {
            'AssetName': 'string',
            'DataSetId': 'string',
            'Md5Hash': 'string',
            'RevisionId': 'string',
            'SignedUrl': 'string',
            'SignedUrlExpiresAt': datetime(2015, 1, 1)
        },
        'ImportAssetsFromS3': {
            'AssetSources': [
                {
                    'Bucket': 'string',
                    'Key': 'string'
                },
            ],
            'DataSetId': 'string',
            'RevisionId': 'string'
        }
    },
    'Errors': [
        {
            'Code': 'ACCESS_DENIED_EXCEPTION'|'INTERNAL_SERVER_EXCEPTION'|'MALWARE_DETECTED'|'RESOURCE_NOT_FOUND_EXCEPTION'|'SERVICE_QUOTA_EXCEEDED_EXCEPTION'|'VALIDATION_EXCEPTION'|'MALWARE_SCAN_ENCRYPTED_FILE',
            'Details': {
                'ImportAssetFromSignedUrlJobErrorDetails': {
                    'AssetName': 'string'
                },
                'ImportAssetsFromS3JobErrorDetails': [
                    {
                        'Bucket': 'string',
                        'Key': 'string'
                    },
                ]
            },
            'LimitName': 'Assets per revision'|'Asset size in GB',
            'LimitValue': 123.0,
            'Message': 'string',
            'ResourceId': 'string',
            'ResourceType': 'REVISION'|'ASSET'
        },
    ],
    'Id': 'string',
    'State': 'WAITING'|'IN_PROGRESS'|'ERROR'|'COMPLETED'|'CANCELLED'|'TIMED_OUT',
    'Type': 'IMPORT_ASSETS_FROM_S3'|'IMPORT_ASSET_FROM_SIGNED_URL'|'EXPORT_ASSETS_TO_S3'|'EXPORT_ASSET_TO_SIGNED_URL',
    'UpdatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --200 response

Arn (string) --The ARN for the job.

CreatedAt (datetime) --The date and time that the job was created, in ISO 8601 format.

Details (dict) --Details about the job.

ExportAssetToSignedUrl (dict) --Details for the export to signed URL response.

AssetId (string) --The unique identifier for the asset associated with this export job.

DataSetId (string) --The unique identifier for the data set associated with this export job.

RevisionId (string) --The unique identifier for the revision associated with this export response.

SignedUrl (string) --The signed URL for the export request.

SignedUrlExpiresAt (datetime) --The date and time that the signed URL expires, in ISO 8601 format.



ExportAssetsToS3 (dict) --Details for the export to Amazon S3 response.

AssetDestinations (list) --The destination in Amazon S3 where the asset is exported.

(dict) --The destination for the asset.

AssetId (string) --The unique identifier for the asset.

Bucket (string) --The S3 bucket that is the destination for the asset.

Key (string) --The name of the object in Amazon S3 for the asset.





DataSetId (string) --The unique identifier for the data set associated with this export job.

Encryption (dict) --Encryption configuration of the export job.

KmsKeyArn (string) --The Amazon Resource Name (ARN) of the the AWS KMS key you want to use to encrypt the Amazon S3 objects. This parameter is required if you choose aws:kms as an encryption type.

Type (string) --The type of server side encryption used for encrypting the objects in Amazon S3.



RevisionId (string) --The unique identifier for the revision associated with this export response.



ImportAssetFromSignedUrl (dict) --Details for the import from signed URL response.

AssetName (string) --The name for the asset associated with this import response.

DataSetId (string) --The unique identifier for the data set associated with this import job.

Md5Hash (string) --The Base64-encoded Md5 hash for the asset, used to ensure the integrity of the file at that location.

RevisionId (string) --The unique identifier for the revision associated with this import response.

SignedUrl (string) --The signed URL.

SignedUrlExpiresAt (datetime) --The time and date at which the signed URL expires, in ISO 8601 format.



ImportAssetsFromS3 (dict) --Details for the import from Amazon S3 response.

AssetSources (list) --Is a list of Amazon S3 bucket and object key pairs.

(dict) --The source of the assets.

Bucket (string) --The S3 bucket that\'s part of the source of the asset.

Key (string) --The name of the object in Amazon S3 for the asset.





DataSetId (string) --The unique identifier for the data set associated with this import job.

RevisionId (string) --The unique identifier for the revision associated with this import response.





Errors (list) --The errors associated with jobs.

(dict) -- An error that occurred with the job request.
Code (string) -- The code for the job error.
Details (dict) --
ImportAssetFromSignedUrlJobErrorDetails (dict) --
AssetName (string) --The name of the asset. When importing from Amazon S3, the S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target S3 object key.



ImportAssetsFromS3JobErrorDetails (list) --The list of sources for the assets.

(dict) --The source of the assets.

Bucket (string) --The S3 bucket that\'s part of the source of the asset.

Key (string) --The name of the object in Amazon S3 for the asset.







LimitName (string) --The name of the limit that was reached.

LimitValue (float) -- The value of the exceeded limit.
Message (string) -- The message related to the job error.
ResourceId (string) -- The unique identifier for the resource related to the error.
ResourceType (string) -- The type of resource related to the error.




Id (string) --The unique identifier for the job.

State (string) --The state of the job.

Type (string) --The job type.

UpdatedAt (datetime) --The date and time that the job was last updated, in ISO 8601 format.






Exceptions

DataExchange.Client.exceptions.ResourceNotFoundException
DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException


    :return: {
        'Arn': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'Details': {
            'ExportAssetToSignedUrl': {
                'AssetId': 'string',
                'DataSetId': 'string',
                'RevisionId': 'string',
                'SignedUrl': 'string',
                'SignedUrlExpiresAt': datetime(2015, 1, 1)
            },
            'ExportAssetsToS3': {
                'AssetDestinations': [
                    {
                        'AssetId': 'string',
                        'Bucket': 'string',
                        'Key': 'string'
                    },
                ],
                'DataSetId': 'string',
                'Encryption': {
                    'KmsKeyArn': 'string',
                    'Type': 'aws:kms'|'AES256'
                },
                'RevisionId': 'string'
            },
            'ImportAssetFromSignedUrl': {
                'AssetName': 'string',
                'DataSetId': 'string',
                'Md5Hash': 'string',
                'RevisionId': 'string',
                'SignedUrl': 'string',
                'SignedUrlExpiresAt': datetime(2015, 1, 1)
            },
            'ImportAssetsFromS3': {
                'AssetSources': [
                    {
                        'Bucket': 'string',
                        'Key': 'string'
                    },
                ],
                'DataSetId': 'string',
                'RevisionId': 'string'
            }
        },
        'Errors': [
            {
                'Code': 'ACCESS_DENIED_EXCEPTION'|'INTERNAL_SERVER_EXCEPTION'|'MALWARE_DETECTED'|'RESOURCE_NOT_FOUND_EXCEPTION'|'SERVICE_QUOTA_EXCEEDED_EXCEPTION'|'VALIDATION_EXCEPTION'|'MALWARE_SCAN_ENCRYPTED_FILE',
                'Details': {
                    'ImportAssetFromSignedUrlJobErrorDetails': {
                        'AssetName': 'string'
                    },
                    'ImportAssetsFromS3JobErrorDetails': [
                        {
                            'Bucket': 'string',
                            'Key': 'string'
                        },
                    ]
                },
                'LimitName': 'Assets per revision'|'Asset size in GB',
                'LimitValue': 123.0,
                'Message': 'string',
                'ResourceId': 'string',
                'ResourceType': 'REVISION'|'ASSET'
            },
        ],
        'Id': 'string',
        'State': 'WAITING'|'IN_PROGRESS'|'ERROR'|'COMPLETED'|'CANCELLED'|'TIMED_OUT',
        'Type': 'IMPORT_ASSETS_FROM_S3'|'IMPORT_ASSET_FROM_SIGNED_URL'|'EXPORT_ASSETS_TO_S3'|'EXPORT_ASSET_TO_SIGNED_URL',
        'UpdatedAt': datetime(2015, 1, 1)
    }
    
    
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

def get_revision(DataSetId=None, RevisionId=None):
    """
    This operation returns information about a revision.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_revision(
        DataSetId='string',
        RevisionId='string'
    )
    
    
    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe unique identifier for a data set.\n

    :type RevisionId: string
    :param RevisionId: [REQUIRED]\nThe unique identifier for a revision.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'Comment': 'string',
    'CreatedAt': datetime(2015, 1, 1),
    'DataSetId': 'string',
    'Finalized': True|False,
    'Id': 'string',
    'SourceId': 'string',
    'Tags': {
        'string': 'string'
    },
    'UpdatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --
200 response

Arn (string) --
The ARN for the revision

Comment (string) --
An optional comment about the revision.

CreatedAt (datetime) --
The date and time that the revision was created, in ISO 8601 format.

DataSetId (string) --
The unique identifier for the data set associated with this revision.

Finalized (boolean) --
To publish a revision to a data set in a product, the revision must first be finalized. Finalizing a revision tells AWS Data Exchange that your changes to the assets in the revision are complete. After it\'s in this read-only state, you can publish the revision to your products.
Finalized revisions can be published through the AWS Data Exchange console or the AWS Marketplace Catalog API, using the StartChangeSet AWS Marketplace Catalog API action. When using the API, revisions are uniquely identified by their ARN.

Id (string) --
The unique identifier for the revision.

SourceId (string) --
The revision ID of the owned revision corresponding to the entitled revision being viewed. This parameter is returned when a revision owner is viewing the entitled copy of its owned revision.

Tags (dict) --
The tags for the revision.

(string) --
(string) --




UpdatedAt (datetime) --
The date and time that the revision was last updated, in ISO 8601 format.







Exceptions

DataExchange.Client.exceptions.ResourceNotFoundException
DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException


    :return: {
        'Arn': 'string',
        'Comment': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'DataSetId': 'string',
        'Finalized': True|False,
        'Id': 'string',
        'SourceId': 'string',
        'Tags': {
            'string': 'string'
        },
        'UpdatedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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

def list_data_set_revisions(DataSetId=None, MaxResults=None, NextToken=None):
    """
    This operation lists a data set\'s revisions sorted by CreatedAt in descending order.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_data_set_revisions(
        DataSetId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe unique identifier for a data set.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results returned by a single call.

    :type NextToken: string
    :param NextToken: The token value retrieved from a previous call to access the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Revisions': [
        {
            'Arn': 'string',
            'Comment': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'DataSetId': 'string',
            'Finalized': True|False,
            'Id': 'string',
            'SourceId': 'string',
            'UpdatedAt': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --
200 response

NextToken (string) --
The token value retrieved from a previous call to access the next page of results.

Revisions (list) --
The asset objects listed by the request.

(dict) --
A revision is a container for one or more assets.

Arn (string) --
The ARN for the revision.

Comment (string) --
An optional comment about the revision.

CreatedAt (datetime) --
The date and time that the revision was created, in ISO 8601 format.

DataSetId (string) --
The unique identifier for the data set associated with this revision.

Finalized (boolean) --
To publish a revision to a data set in a product, the revision must first be finalized. Finalizing a revision tells AWS Data Exchange that your changes to the assets in the revision are complete. After it\'s in this read-only state, you can publish the revision to your products.
Finalized revisions can be published through the AWS Data Exchange console or the AWS Marketplace Catalog API, using the StartChangeSet AWS Marketplace Catalog API action. When using the API, revisions are uniquely identified by their ARN.

Id (string) --
The unique identifier for the revision.

SourceId (string) --
The revision ID of the owned revision corresponding to the entitled revision being viewed. This parameter is returned when a revision owner is viewing the entitled copy of its owned revision.

UpdatedAt (datetime) --
The date and time that the revision was last updated, in ISO 8601 format.











Exceptions

DataExchange.Client.exceptions.ResourceNotFoundException
DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException


    :return: {
        'NextToken': 'string',
        'Revisions': [
            {
                'Arn': 'string',
                'Comment': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'DataSetId': 'string',
                'Finalized': True|False,
                'Id': 'string',
                'SourceId': 'string',
                'UpdatedAt': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    DataExchange.Client.exceptions.ResourceNotFoundException
    DataExchange.Client.exceptions.ThrottlingException
    DataExchange.Client.exceptions.ValidationException
    DataExchange.Client.exceptions.InternalServerException
    
    """
    pass

def list_data_sets(MaxResults=None, NextToken=None, Origin=None):
    """
    This operation lists your data sets. When listing by origin OWNED, results are sorted by CreatedAt in descending order. When listing by origin ENTITLED, there is no order and the maxResults parameter is ignored.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_data_sets(
        MaxResults=123,
        NextToken='string',
        Origin='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results returned by a single call.

    :type NextToken: string
    :param NextToken: The token value retrieved from a previous call to access the next page of results.

    :type Origin: string
    :param Origin: A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).

    :rtype: dict

ReturnsResponse Syntax
{
    'DataSets': [
        {
            'Arn': 'string',
            'AssetType': 'S3_SNAPSHOT',
            'CreatedAt': datetime(2015, 1, 1),
            'Description': 'string',
            'Id': 'string',
            'Name': 'string',
            'Origin': 'OWNED'|'ENTITLED',
            'OriginDetails': {
                'ProductId': 'string'
            },
            'SourceId': 'string',
            'UpdatedAt': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
200 response

DataSets (list) --
The data set objects listed by the request.

(dict) --
A data set is an AWS resource with one or more revisions.

Arn (string) --
The ARN for the data set.

AssetType (string) --
The type of file your data is stored in. Currently, the supported asset type is S3_SNAPSHOT.

CreatedAt (datetime) --
The date and time that the data set was created, in ISO 8601 format.

Description (string) --
The description for the data set.

Id (string) --
The unique identifier for the data set.

Name (string) --
The name of the data set.

Origin (string) --
A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).

OriginDetails (dict) --
If the origin of this data set is ENTITLED, includes the details for the product on AWS Marketplace.

ProductId (string) --


SourceId (string) --
The data set ID of the owned data set corresponding to the entitled data set being viewed. This parameter is returned when a data set owner is viewing the entitled copy of its owned data set.

UpdatedAt (datetime) --
The date and time that the data set was last updated, in ISO 8601 format.





NextToken (string) --
The token value retrieved from a previous call to access the next page of results.







Exceptions

DataExchange.Client.exceptions.ResourceNotFoundException
DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException


    :return: {
        'DataSets': [
            {
                'Arn': 'string',
                'AssetType': 'S3_SNAPSHOT',
                'CreatedAt': datetime(2015, 1, 1),
                'Description': 'string',
                'Id': 'string',
                'Name': 'string',
                'Origin': 'OWNED'|'ENTITLED',
                'OriginDetails': {
                    'ProductId': 'string'
                },
                'SourceId': 'string',
                'UpdatedAt': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ProductId (string) --
    
    """
    pass

def list_jobs(DataSetId=None, MaxResults=None, NextToken=None, RevisionId=None):
    """
    This operation lists your jobs sorted by CreatedAt in descending order.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_jobs(
        DataSetId='string',
        MaxResults=123,
        NextToken='string',
        RevisionId='string'
    )
    
    
    :type DataSetId: string
    :param DataSetId: The unique identifier for a data set.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results returned by a single call.

    :type NextToken: string
    :param NextToken: The token value retrieved from a previous call to access the next page of results.

    :type RevisionId: string
    :param RevisionId: The unique identifier for a revision.

    :rtype: dict

ReturnsResponse Syntax
{
    'Jobs': [
        {
            'Arn': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'Details': {
                'ExportAssetToSignedUrl': {
                    'AssetId': 'string',
                    'DataSetId': 'string',
                    'RevisionId': 'string',
                    'SignedUrl': 'string',
                    'SignedUrlExpiresAt': datetime(2015, 1, 1)
                },
                'ExportAssetsToS3': {
                    'AssetDestinations': [
                        {
                            'AssetId': 'string',
                            'Bucket': 'string',
                            'Key': 'string'
                        },
                    ],
                    'DataSetId': 'string',
                    'Encryption': {
                        'KmsKeyArn': 'string',
                        'Type': 'aws:kms'|'AES256'
                    },
                    'RevisionId': 'string'
                },
                'ImportAssetFromSignedUrl': {
                    'AssetName': 'string',
                    'DataSetId': 'string',
                    'Md5Hash': 'string',
                    'RevisionId': 'string',
                    'SignedUrl': 'string',
                    'SignedUrlExpiresAt': datetime(2015, 1, 1)
                },
                'ImportAssetsFromS3': {
                    'AssetSources': [
                        {
                            'Bucket': 'string',
                            'Key': 'string'
                        },
                    ],
                    'DataSetId': 'string',
                    'RevisionId': 'string'
                }
            },
            'Errors': [
                {
                    'Code': 'ACCESS_DENIED_EXCEPTION'|'INTERNAL_SERVER_EXCEPTION'|'MALWARE_DETECTED'|'RESOURCE_NOT_FOUND_EXCEPTION'|'SERVICE_QUOTA_EXCEEDED_EXCEPTION'|'VALIDATION_EXCEPTION'|'MALWARE_SCAN_ENCRYPTED_FILE',
                    'Details': {
                        'ImportAssetFromSignedUrlJobErrorDetails': {
                            'AssetName': 'string'
                        },
                        'ImportAssetsFromS3JobErrorDetails': [
                            {
                                'Bucket': 'string',
                                'Key': 'string'
                            },
                        ]
                    },
                    'LimitName': 'Assets per revision'|'Asset size in GB',
                    'LimitValue': 123.0,
                    'Message': 'string',
                    'ResourceId': 'string',
                    'ResourceType': 'REVISION'|'ASSET'
                },
            ],
            'Id': 'string',
            'State': 'WAITING'|'IN_PROGRESS'|'ERROR'|'COMPLETED'|'CANCELLED'|'TIMED_OUT',
            'Type': 'IMPORT_ASSETS_FROM_S3'|'IMPORT_ASSET_FROM_SIGNED_URL'|'EXPORT_ASSETS_TO_S3'|'EXPORT_ASSET_TO_SIGNED_URL',
            'UpdatedAt': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
200 response

Jobs (list) --
The jobs listed by the request.

(dict) -- AWS Data Exchange Jobs are asynchronous import or export operations used to create or copy assets. A data set owner can both import and export as they see fit. Someone with an entitlement to a data set can only export. Jobs are deleted 90 days after they are created.

Arn (string) --
The ARN for the job.

CreatedAt (datetime) --
The date and time that the job was created, in ISO 8601 format.

Details (dict) --
Details of the operation to be performed by the job, such as export destination details or import source details.

ExportAssetToSignedUrl (dict) --
Details for the export to signed URL response.

AssetId (string) --
The unique identifier for the asset associated with this export job.

DataSetId (string) --
The unique identifier for the data set associated with this export job.

RevisionId (string) --
The unique identifier for the revision associated with this export response.

SignedUrl (string) --
The signed URL for the export request.

SignedUrlExpiresAt (datetime) --
The date and time that the signed URL expires, in ISO 8601 format.



ExportAssetsToS3 (dict) --
Details for the export to Amazon S3 response.

AssetDestinations (list) --
The destination in Amazon S3 where the asset is exported.

(dict) --
The destination for the asset.

AssetId (string) --
The unique identifier for the asset.

Bucket (string) --
The S3 bucket that is the destination for the asset.

Key (string) --
The name of the object in Amazon S3 for the asset.





DataSetId (string) --
The unique identifier for the data set associated with this export job.

Encryption (dict) --
Encryption configuration of the export job.

KmsKeyArn (string) --
The Amazon Resource Name (ARN) of the the AWS KMS key you want to use to encrypt the Amazon S3 objects. This parameter is required if you choose aws:kms as an encryption type.

Type (string) --
The type of server side encryption used for encrypting the objects in Amazon S3.



RevisionId (string) --
The unique identifier for the revision associated with this export response.



ImportAssetFromSignedUrl (dict) --
Details for the import from signed URL response.

AssetName (string) --
The name for the asset associated with this import response.

DataSetId (string) --
The unique identifier for the data set associated with this import job.

Md5Hash (string) --
The Base64-encoded Md5 hash for the asset, used to ensure the integrity of the file at that location.

RevisionId (string) --
The unique identifier for the revision associated with this import response.

SignedUrl (string) --
The signed URL.

SignedUrlExpiresAt (datetime) --
The time and date at which the signed URL expires, in ISO 8601 format.



ImportAssetsFromS3 (dict) --
Details for the import from Amazon S3 response.

AssetSources (list) --
Is a list of Amazon S3 bucket and object key pairs.

(dict) --
The source of the assets.

Bucket (string) --
The S3 bucket that\'s part of the source of the asset.

Key (string) --
The name of the object in Amazon S3 for the asset.





DataSetId (string) --
The unique identifier for the data set associated with this import job.

RevisionId (string) --
The unique identifier for the revision associated with this import response.





Errors (list) --
Errors for jobs.

(dict) -- An error that occurred with the job request.

Code (string) -- The code for the job error.

Details (dict) --

ImportAssetFromSignedUrlJobErrorDetails (dict) --

AssetName (string) --
The name of the asset. When importing from Amazon S3, the S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target S3 object key.



ImportAssetsFromS3JobErrorDetails (list) --
The list of sources for the assets.

(dict) --
The source of the assets.

Bucket (string) --
The S3 bucket that\'s part of the source of the asset.

Key (string) --
The name of the object in Amazon S3 for the asset.







LimitName (string) --
The name of the limit that was reached.

LimitValue (float) -- The value of the exceeded limit.

Message (string) -- The message related to the job error.

ResourceId (string) -- The unique identifier for the resource related to the error.

ResourceType (string) -- The type of resource related to the error.





Id (string) --
The unique identifier for the job.

State (string) --
The state of the job.

Type (string) --
The job type.

UpdatedAt (datetime) --
The date and time that the job was last updated, in ISO 8601 format.





NextToken (string) --
The token value retrieved from a previous call to access the next page of results.







Exceptions

DataExchange.Client.exceptions.ResourceNotFoundException
DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException


    :return: {
        'Jobs': [
            {
                'Arn': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'Details': {
                    'ExportAssetToSignedUrl': {
                        'AssetId': 'string',
                        'DataSetId': 'string',
                        'RevisionId': 'string',
                        'SignedUrl': 'string',
                        'SignedUrlExpiresAt': datetime(2015, 1, 1)
                    },
                    'ExportAssetsToS3': {
                        'AssetDestinations': [
                            {
                                'AssetId': 'string',
                                'Bucket': 'string',
                                'Key': 'string'
                            },
                        ],
                        'DataSetId': 'string',
                        'Encryption': {
                            'KmsKeyArn': 'string',
                            'Type': 'aws:kms'|'AES256'
                        },
                        'RevisionId': 'string'
                    },
                    'ImportAssetFromSignedUrl': {
                        'AssetName': 'string',
                        'DataSetId': 'string',
                        'Md5Hash': 'string',
                        'RevisionId': 'string',
                        'SignedUrl': 'string',
                        'SignedUrlExpiresAt': datetime(2015, 1, 1)
                    },
                    'ImportAssetsFromS3': {
                        'AssetSources': [
                            {
                                'Bucket': 'string',
                                'Key': 'string'
                            },
                        ],
                        'DataSetId': 'string',
                        'RevisionId': 'string'
                    }
                },
                'Errors': [
                    {
                        'Code': 'ACCESS_DENIED_EXCEPTION'|'INTERNAL_SERVER_EXCEPTION'|'MALWARE_DETECTED'|'RESOURCE_NOT_FOUND_EXCEPTION'|'SERVICE_QUOTA_EXCEEDED_EXCEPTION'|'VALIDATION_EXCEPTION'|'MALWARE_SCAN_ENCRYPTED_FILE',
                        'Details': {
                            'ImportAssetFromSignedUrlJobErrorDetails': {
                                'AssetName': 'string'
                            },
                            'ImportAssetsFromS3JobErrorDetails': [
                                {
                                    'Bucket': 'string',
                                    'Key': 'string'
                                },
                            ]
                        },
                        'LimitName': 'Assets per revision'|'Asset size in GB',
                        'LimitValue': 123.0,
                        'Message': 'string',
                        'ResourceId': 'string',
                        'ResourceType': 'REVISION'|'ASSET'
                    },
                ],
                'Id': 'string',
                'State': 'WAITING'|'IN_PROGRESS'|'ERROR'|'COMPLETED'|'CANCELLED'|'TIMED_OUT',
                'Type': 'IMPORT_ASSETS_FROM_S3'|'IMPORT_ASSET_FROM_SIGNED_URL'|'EXPORT_ASSETS_TO_S3'|'EXPORT_ASSET_TO_SIGNED_URL',
                'UpdatedAt': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DataExchange.Client.exceptions.ResourceNotFoundException
    DataExchange.Client.exceptions.ThrottlingException
    DataExchange.Client.exceptions.ValidationException
    DataExchange.Client.exceptions.InternalServerException
    
    """
    pass

def list_revision_assets(DataSetId=None, MaxResults=None, NextToken=None, RevisionId=None):
    """
    This operation lists a revision\'s assets sorted alphabetically in descending order.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_revision_assets(
        DataSetId='string',
        MaxResults=123,
        NextToken='string',
        RevisionId='string'
    )
    
    
    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe unique identifier for a data set.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results returned by a single call.

    :type NextToken: string
    :param NextToken: The token value retrieved from a previous call to access the next page of results.

    :type RevisionId: string
    :param RevisionId: [REQUIRED]\nThe unique identifier for a revision.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Assets': [
        {
            'Arn': 'string',
            'AssetDetails': {
                'S3SnapshotAsset': {
                    'Size': 123.0
                }
            },
            'AssetType': 'S3_SNAPSHOT',
            'CreatedAt': datetime(2015, 1, 1),
            'DataSetId': 'string',
            'Id': 'string',
            'Name': 'string',
            'RevisionId': 'string',
            'SourceId': 'string',
            'UpdatedAt': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
200 response

Assets (list) --
The asset objects listed by the request.

(dict) --
An asset in AWS Data Exchange is a piece of data that can be stored as an S3 object. The asset can be a structured data file, an image file, or some other data file. When you create an import job for your files, you create an asset in AWS Data Exchange for each of those files.

Arn (string) --
The ARN for the asset.

AssetDetails (dict) --
Information about the asset, including its size.

S3SnapshotAsset (dict) --
The S3 object that is the asset.

Size (float) --
The size of the S3 object that is the object.





AssetType (string) --
The type of file your data is stored in. Currently, the supported asset type is S3_SNAPSHOT.

CreatedAt (datetime) --
The date and time that the asset was created, in ISO 8601 format.

DataSetId (string) --
The unique identifier for the data set associated with this asset.

Id (string) --
The unique identifier for the asset.

Name (string) --
The name of the asset. When importing from Amazon S3, the S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target S3 object key.

RevisionId (string) --
The unique identifier for the revision associated with this asset.

SourceId (string) --
The asset ID of the owned asset corresponding to the entitled asset being viewed. This parameter is returned when an asset owner is viewing the entitled copy of its owned asset.

UpdatedAt (datetime) --
The date and time that the asset was last updated, in ISO 8601 format.





NextToken (string) --
The token value retrieved from a previous call to access the next page of results.







Exceptions

DataExchange.Client.exceptions.ResourceNotFoundException
DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException


    :return: {
        'Assets': [
            {
                'Arn': 'string',
                'AssetDetails': {
                    'S3SnapshotAsset': {
                        'Size': 123.0
                    }
                },
                'AssetType': 'S3_SNAPSHOT',
                'CreatedAt': datetime(2015, 1, 1),
                'DataSetId': 'string',
                'Id': 'string',
                'Name': 'string',
                'RevisionId': 'string',
                'SourceId': 'string',
                'UpdatedAt': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DataExchange.Client.exceptions.ResourceNotFoundException
    DataExchange.Client.exceptions.ThrottlingException
    DataExchange.Client.exceptions.ValidationException
    DataExchange.Client.exceptions.InternalServerException
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    This operation lists the tags on the resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nAn Amazon Resource Name (ARN) that uniquely identifies an AWS resource.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --200 response

Tags (dict) -- A label that consists of a customer-defined key and an optional value.
(string) --
(string) --










    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    """
    pass

def start_job(JobId=None):
    """
    This operation starts a job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe unique identifier for a job.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --202 response




Exceptions

DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException
DataExchange.Client.exceptions.AccessDeniedException
DataExchange.Client.exceptions.ResourceNotFoundException
DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ConflictException


    :return: {}
    
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    This operation tags a resource.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nAn Amazon Resource Name (ARN) that uniquely identifies an AWS resource.\n

    :type Tags: dict
    :param Tags: [REQUIRED] A label that consists of a customer-defined key and an optional value.\n\n(string) --\n(string) --\n\n\n\n

    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    This operation removes one or more tags from a resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nAn Amazon Resource Name (ARN) that uniquely identifies an AWS resource.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED] The key tags.\n\n(string) --\n\n

    """
    pass

def update_asset(AssetId=None, DataSetId=None, Name=None, RevisionId=None):
    """
    This operation updates an asset.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_asset(
        AssetId='string',
        DataSetId='string',
        Name='string',
        RevisionId='string'
    )
    
    
    :type AssetId: string
    :param AssetId: [REQUIRED]\nThe unique identifier for an asset.\n

    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe unique identifier for a data set.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the asset. When importing from Amazon S3, the S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target S3 object key.\n

    :type RevisionId: string
    :param RevisionId: [REQUIRED]\nThe unique identifier for a revision.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'AssetDetails': {
        'S3SnapshotAsset': {
            'Size': 123.0
        }
    },
    'AssetType': 'S3_SNAPSHOT',
    'CreatedAt': datetime(2015, 1, 1),
    'DataSetId': 'string',
    'Id': 'string',
    'Name': 'string',
    'RevisionId': 'string',
    'SourceId': 'string',
    'UpdatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --
200 response

Arn (string) --
The ARN for the asset.

AssetDetails (dict) --
Information about the asset, including its size.

S3SnapshotAsset (dict) --
The S3 object that is the asset.

Size (float) --
The size of the S3 object that is the object.





AssetType (string) --
The type of file your data is stored in. Currently, the supported asset type is S3_SNAPSHOT.

CreatedAt (datetime) --
The date and time that the asset was created, in ISO 8601 format.

DataSetId (string) --
The unique identifier for the data set associated with this asset.

Id (string) --
The unique identifier for the asset.

Name (string) --
The name of the asset When importing from Amazon S3, the S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target S3 object key.

RevisionId (string) --
The unique identifier for the revision associated with this asset.

SourceId (string) --
The asset ID of the owned asset corresponding to the entitled asset being viewed. This parameter is returned when an asset owner is viewing the entitled copy of its owned asset.

UpdatedAt (datetime) --
The date and time that the asset was last updated, in ISO 8601 format.







Exceptions

DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException
DataExchange.Client.exceptions.AccessDeniedException
DataExchange.Client.exceptions.ResourceNotFoundException
DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ConflictException


    :return: {
        'Arn': 'string',
        'AssetDetails': {
            'S3SnapshotAsset': {
                'Size': 123.0
            }
        },
        'AssetType': 'S3_SNAPSHOT',
        'CreatedAt': datetime(2015, 1, 1),
        'DataSetId': 'string',
        'Id': 'string',
        'Name': 'string',
        'RevisionId': 'string',
        'SourceId': 'string',
        'UpdatedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    DataExchange.Client.exceptions.ValidationException
    DataExchange.Client.exceptions.InternalServerException
    DataExchange.Client.exceptions.AccessDeniedException
    DataExchange.Client.exceptions.ResourceNotFoundException
    DataExchange.Client.exceptions.ThrottlingException
    DataExchange.Client.exceptions.ConflictException
    
    """
    pass

def update_data_set(DataSetId=None, Description=None, Name=None):
    """
    This operation updates a data set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_data_set(
        DataSetId='string',
        Description='string',
        Name='string'
    )
    
    
    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe unique identifier for a data set.\n

    :type Description: string
    :param Description: The description for the data set.

    :type Name: string
    :param Name: The name of the data set.

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'AssetType': 'S3_SNAPSHOT',
    'CreatedAt': datetime(2015, 1, 1),
    'Description': 'string',
    'Id': 'string',
    'Name': 'string',
    'Origin': 'OWNED'|'ENTITLED',
    'OriginDetails': {
        'ProductId': 'string'
    },
    'SourceId': 'string',
    'UpdatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --
200 response

Arn (string) --
The ARN for the data set.

AssetType (string) --
The type of file your data is stored in. Currently, the supported asset type is S3_SNAPSHOT.

CreatedAt (datetime) --
The date and time that the data set was created, in ISO 8601 format.

Description (string) --
The description for the data set.

Id (string) --
The unique identifier for the data set.

Name (string) --
The name of the data set.

Origin (string) --
A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).

OriginDetails (dict) --
If the origin of this data set is ENTITLED, includes the details for the product on AWS Marketplace.

ProductId (string) --


SourceId (string) --
The data set ID of the owned data set corresponding to the entitled data set being viewed. This parameter is returned when a data set owner is viewing the entitled copy of its owned data set.

UpdatedAt (datetime) --
The date and time that the data set was last updated, in ISO 8601 format.







Exceptions

DataExchange.Client.exceptions.ResourceNotFoundException
DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException
DataExchange.Client.exceptions.AccessDeniedException


    :return: {
        'Arn': 'string',
        'AssetType': 'S3_SNAPSHOT',
        'CreatedAt': datetime(2015, 1, 1),
        'Description': 'string',
        'Id': 'string',
        'Name': 'string',
        'Origin': 'OWNED'|'ENTITLED',
        'OriginDetails': {
            'ProductId': 'string'
        },
        'SourceId': 'string',
        'UpdatedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    ProductId (string) --
    
    """
    pass

def update_revision(Comment=None, DataSetId=None, Finalized=None, RevisionId=None):
    """
    This operation updates a revision.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_revision(
        Comment='string',
        DataSetId='string',
        Finalized=True|False,
        RevisionId='string'
    )
    
    
    :type Comment: string
    :param Comment: An optional comment about the revision.

    :type DataSetId: string
    :param DataSetId: [REQUIRED]\nThe unique identifier for a data set.\n

    :type Finalized: boolean
    :param Finalized: Finalizing a revision tells AWS Data Exchange that your changes to the assets in the revision are complete. After it\'s in this read-only state, you can publish the revision to your products.

    :type RevisionId: string
    :param RevisionId: [REQUIRED]\nThe unique identifier for a revision.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'Comment': 'string',
    'CreatedAt': datetime(2015, 1, 1),
    'DataSetId': 'string',
    'Finalized': True|False,
    'Id': 'string',
    'SourceId': 'string',
    'UpdatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --
200 response

Arn (string) --
The ARN for the revision.

Comment (string) --
An optional comment about the revision.

CreatedAt (datetime) --
The date and time that the revision was created, in ISO 8601 format.

DataSetId (string) --
The unique identifier for the data set associated with this revision.

Finalized (boolean) --
To publish a revision to a data set in a product, the revision must first be finalized. Finalizing a revision tells AWS Data Exchange that changes to the assets in the revision are complete. After it\'s in this read-only state, you can publish the revision to your products.
Finalized revisions can be published through the AWS Data Exchange console or the AWS Marketplace Catalog API, using the StartChangeSet AWS Marketplace Catalog API action. When using the API, revisions are uniquely identified by their ARN.

Id (string) --
The unique identifier for the revision.

SourceId (string) --
The revision ID of the owned revision corresponding to the entitled revision being viewed. This parameter is returned when a revision owner is viewing the entitled copy of its owned revision.

UpdatedAt (datetime) --
The date and time that the revision was last updated, in ISO 8601 format.







Exceptions

DataExchange.Client.exceptions.ValidationException
DataExchange.Client.exceptions.InternalServerException
DataExchange.Client.exceptions.AccessDeniedException
DataExchange.Client.exceptions.ResourceNotFoundException
DataExchange.Client.exceptions.ThrottlingException
DataExchange.Client.exceptions.ConflictException


    :return: {
        'Arn': 'string',
        'Comment': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'DataSetId': 'string',
        'Finalized': True|False,
        'Id': 'string',
        'SourceId': 'string',
        'UpdatedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    DataExchange.Client.exceptions.ValidationException
    DataExchange.Client.exceptions.InternalServerException
    DataExchange.Client.exceptions.AccessDeniedException
    DataExchange.Client.exceptions.ResourceNotFoundException
    DataExchange.Client.exceptions.ThrottlingException
    DataExchange.Client.exceptions.ConflictException
    
    """
    pass

