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

def bulk_publish(IdentityPoolId=None):
    """
    Initiates a bulk publish of all existing datasets for an Identity Pool to the configured stream. Customers are limited to one successful bulk publish per 24 hours. Bulk publish is an asynchronous request, customers can see the status of the request via the GetBulkPublishDetails operation.
    This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.bulk_publish(
        IdentityPoolId='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :rtype: dict
ReturnsResponse Syntax{
    'IdentityPoolId': 'string'
}


Response Structure

(dict) -- The output for the BulkPublish operation.
IdentityPoolId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.





Exceptions

CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.ResourceNotFoundException
CognitoSync.Client.exceptions.InternalErrorException
CognitoSync.Client.exceptions.DuplicateRequestException
CognitoSync.Client.exceptions.AlreadyStreamedException


    :return: {
        'IdentityPoolId': 'string'
    }
    
    
    :returns: 
    CognitoSync.Client.exceptions.NotAuthorizedException
    CognitoSync.Client.exceptions.InvalidParameterException
    CognitoSync.Client.exceptions.ResourceNotFoundException
    CognitoSync.Client.exceptions.InternalErrorException
    CognitoSync.Client.exceptions.DuplicateRequestException
    CognitoSync.Client.exceptions.AlreadyStreamedException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def delete_dataset(IdentityPoolId=None, IdentityId=None, DatasetName=None):
    """
    Deletes the specific dataset. The dataset will be deleted permanently, and the action can\'t be undone. Datasets that this dataset was merged with will no longer report the merge. Any subsequent operation on this dataset will result in a ResourceNotFoundException.
    This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_dataset(
        IdentityPoolId='string',
        IdentityId='string',
        DatasetName='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :type IdentityId: string
    :param IdentityId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :type DatasetName: string
    :param DatasetName: [REQUIRED] A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).

    :rtype: dict

ReturnsResponse Syntax
{
    'Dataset': {
        'IdentityId': 'string',
        'DatasetName': 'string',
        'CreationDate': datetime(2015, 1, 1),
        'LastModifiedDate': datetime(2015, 1, 1),
        'LastModifiedBy': 'string',
        'DataStorage': 123,
        'NumRecords': 123
    }
}


Response Structure

(dict) -- Response to a successful DeleteDataset request.
Dataset (dict) -- A collection of data for an identity pool. An identity pool can have multiple datasets. A dataset is per identity and can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don\'t exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.
IdentityId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
DatasetName (string) -- A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).
CreationDate (datetime) -- Date on which the dataset was created.
LastModifiedDate (datetime) -- Date when the dataset was last modified.
LastModifiedBy (string) -- The device that made the last change to this dataset.
DataStorage (integer) -- Total size in bytes of the records in this dataset.
NumRecords (integer) -- Number of records in this dataset.








Exceptions

CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.ResourceNotFoundException
CognitoSync.Client.exceptions.InternalErrorException
CognitoSync.Client.exceptions.TooManyRequestsException
CognitoSync.Client.exceptions.ResourceConflictException


    :return: {
        'Dataset': {
            'IdentityId': 'string',
            'DatasetName': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'LastModifiedDate': datetime(2015, 1, 1),
            'LastModifiedBy': 'string',
            'DataStorage': 123,
            'NumRecords': 123
        }
    }
    
    
    :returns: 
    (dict) -- Response to a successful DeleteDataset request.
    Dataset (dict) -- A collection of data for an identity pool. An identity pool can have multiple datasets. A dataset is per identity and can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don\'t exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.
    IdentityId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    DatasetName (string) -- A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).
    CreationDate (datetime) -- Date on which the dataset was created.
    LastModifiedDate (datetime) -- Date when the dataset was last modified.
    LastModifiedBy (string) -- The device that made the last change to this dataset.
    DataStorage (integer) -- Total size in bytes of the records in this dataset.
    NumRecords (integer) -- Number of records in this dataset.
    
    
    
    
    
    """
    pass

def describe_dataset(IdentityPoolId=None, IdentityId=None, DatasetName=None):
    """
    Gets meta data about a dataset by identity and dataset name. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.
    This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use Cognito Identity credentials to make this API call.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_dataset(
        IdentityPoolId='string',
        IdentityId='string',
        DatasetName='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :type IdentityId: string
    :param IdentityId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :type DatasetName: string
    :param DatasetName: [REQUIRED] A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).

    :rtype: dict

ReturnsResponse Syntax
{
    'Dataset': {
        'IdentityId': 'string',
        'DatasetName': 'string',
        'CreationDate': datetime(2015, 1, 1),
        'LastModifiedDate': datetime(2015, 1, 1),
        'LastModifiedBy': 'string',
        'DataStorage': 123,
        'NumRecords': 123
    }
}


Response Structure

(dict) -- Response to a successful DescribeDataset request.
Dataset (dict) -- Meta data for a collection of data for an identity. An identity can have multiple datasets. A dataset can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don\'t exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.
IdentityId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
DatasetName (string) -- A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).
CreationDate (datetime) -- Date on which the dataset was created.
LastModifiedDate (datetime) -- Date when the dataset was last modified.
LastModifiedBy (string) -- The device that made the last change to this dataset.
DataStorage (integer) -- Total size in bytes of the records in this dataset.
NumRecords (integer) -- Number of records in this dataset.








Exceptions

CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.ResourceNotFoundException
CognitoSync.Client.exceptions.InternalErrorException
CognitoSync.Client.exceptions.TooManyRequestsException


    :return: {
        'Dataset': {
            'IdentityId': 'string',
            'DatasetName': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'LastModifiedDate': datetime(2015, 1, 1),
            'LastModifiedBy': 'string',
            'DataStorage': 123,
            'NumRecords': 123
        }
    }
    
    
    :returns: 
    (dict) -- Response to a successful DescribeDataset request.
    Dataset (dict) -- Meta data for a collection of data for an identity. An identity can have multiple datasets. A dataset can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don\'t exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.
    IdentityId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    DatasetName (string) -- A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).
    CreationDate (datetime) -- Date on which the dataset was created.
    LastModifiedDate (datetime) -- Date when the dataset was last modified.
    LastModifiedBy (string) -- The device that made the last change to this dataset.
    DataStorage (integer) -- Total size in bytes of the records in this dataset.
    NumRecords (integer) -- Number of records in this dataset.
    
    
    
    
    
    """
    pass

def describe_identity_pool_usage(IdentityPoolId=None):
    """
    Gets usage details (for example, data storage) about a particular identity pool.
    This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_identity_pool_usage(
        IdentityPoolId='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :rtype: dict
ReturnsResponse Syntax{
    'IdentityPoolUsage': {
        'IdentityPoolId': 'string',
        'SyncSessionsCount': 123,
        'DataStorage': 123,
        'LastModifiedDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) -- Response to a successful DescribeIdentityPoolUsage request.
IdentityPoolUsage (dict) -- Information about the usage of the identity pool.
IdentityPoolId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
SyncSessionsCount (integer) -- Number of sync sessions for the identity pool.
DataStorage (integer) -- Data storage information for the identity pool.
LastModifiedDate (datetime) -- Date on which the identity pool was last modified.







Exceptions

CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.ResourceNotFoundException
CognitoSync.Client.exceptions.InternalErrorException
CognitoSync.Client.exceptions.TooManyRequestsException


    :return: {
        'IdentityPoolUsage': {
            'IdentityPoolId': 'string',
            'SyncSessionsCount': 123,
            'DataStorage': 123,
            'LastModifiedDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CognitoSync.Client.exceptions.NotAuthorizedException
    CognitoSync.Client.exceptions.InvalidParameterException
    CognitoSync.Client.exceptions.ResourceNotFoundException
    CognitoSync.Client.exceptions.InternalErrorException
    CognitoSync.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_identity_usage(IdentityPoolId=None, IdentityId=None):
    """
    Gets usage information for an identity, including number of datasets and data usage.
    This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_identity_usage(
        IdentityPoolId='string',
        IdentityId='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :type IdentityId: string
    :param IdentityId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityUsage': {
        'IdentityId': 'string',
        'IdentityPoolId': 'string',
        'LastModifiedDate': datetime(2015, 1, 1),
        'DatasetCount': 123,
        'DataStorage': 123
    }
}


Response Structure

(dict) -- The response to a successful DescribeIdentityUsage request.
IdentityUsage (dict) -- Usage information for the identity.
IdentityId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
IdentityPoolId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
LastModifiedDate (datetime) -- Date on which the identity was last modified.
DatasetCount (integer) -- Number of datasets for the identity.
DataStorage (integer) -- Total data storage for this identity.








Exceptions

CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.ResourceNotFoundException
CognitoSync.Client.exceptions.InternalErrorException
CognitoSync.Client.exceptions.TooManyRequestsException


    :return: {
        'IdentityUsage': {
            'IdentityId': 'string',
            'IdentityPoolId': 'string',
            'LastModifiedDate': datetime(2015, 1, 1),
            'DatasetCount': 123,
            'DataStorage': 123
        }
    }
    
    
    :returns: 
    (dict) -- The response to a successful DescribeIdentityUsage request.
    IdentityUsage (dict) -- Usage information for the identity.
    IdentityId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    IdentityPoolId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    LastModifiedDate (datetime) -- Date on which the identity was last modified.
    DatasetCount (integer) -- Number of datasets for the identity.
    DataStorage (integer) -- Total data storage for this identity.
    
    
    
    
    
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

def get_bulk_publish_details(IdentityPoolId=None):
    """
    Get the status of the last BulkPublish operation for an identity pool.
    This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_bulk_publish_details(
        IdentityPoolId='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :rtype: dict
ReturnsResponse Syntax{
    'IdentityPoolId': 'string',
    'BulkPublishStartTime': datetime(2015, 1, 1),
    'BulkPublishCompleteTime': datetime(2015, 1, 1),
    'BulkPublishStatus': 'NOT_STARTED'|'IN_PROGRESS'|'FAILED'|'SUCCEEDED',
    'FailureMessage': 'string'
}


Response Structure

(dict) -- The output for the GetBulkPublishDetails operation.
IdentityPoolId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
BulkPublishStartTime (datetime) -- The date/time at which the last bulk publish was initiated.
BulkPublishCompleteTime (datetime) -- If BulkPublishStatus is SUCCEEDED, the time the last bulk publish operation completed.
BulkPublishStatus (string) -- Status of the last bulk publish operation, valid values are:NOT_STARTED - No bulk publish has been requested for this identity pool
IN_PROGRESS - Data is being published to the configured stream
SUCCEEDED - All data for the identity pool has been published to the configured stream
FAILED - Some portion of the data has failed to publish, check FailureMessage for the cause.

FailureMessage (string) -- If BulkPublishStatus is FAILED this field will contain the error message that caused the bulk publish to fail.





Exceptions

CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.ResourceNotFoundException
CognitoSync.Client.exceptions.InternalErrorException


    :return: {
        'IdentityPoolId': 'string',
        'BulkPublishStartTime': datetime(2015, 1, 1),
        'BulkPublishCompleteTime': datetime(2015, 1, 1),
        'BulkPublishStatus': 'NOT_STARTED'|'IN_PROGRESS'|'FAILED'|'SUCCEEDED',
        'FailureMessage': 'string'
    }
    
    
    """
    pass

def get_cognito_events(IdentityPoolId=None):
    """
    Gets the events and the corresponding Lambda functions associated with an identity pool.
    This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_cognito_events(
        IdentityPoolId='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nThe Cognito Identity Pool ID for the request\n

    :rtype: dict
ReturnsResponse Syntax{
    'Events': {
        'string': 'string'
    }
}


Response Structure

(dict) --The response from the GetCognitoEvents request

Events (dict) --The Cognito Events returned from the GetCognitoEvents request

(string) --
(string) --









Exceptions

CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.ResourceNotFoundException
CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.InternalErrorException
CognitoSync.Client.exceptions.TooManyRequestsException


    :return: {
        'Events': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    CognitoSync.Client.exceptions.InvalidParameterException
    CognitoSync.Client.exceptions.ResourceNotFoundException
    CognitoSync.Client.exceptions.NotAuthorizedException
    CognitoSync.Client.exceptions.InternalErrorException
    CognitoSync.Client.exceptions.TooManyRequestsException
    
    """
    pass

def get_identity_pool_configuration(IdentityPoolId=None):
    """
    Gets the configuration settings of an identity pool.
    This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_identity_pool_configuration(
        IdentityPoolId='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nA name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool for which to return a configuration.\n

    :rtype: dict
ReturnsResponse Syntax{
    'IdentityPoolId': 'string',
    'PushSync': {
        'ApplicationArns': [
            'string',
        ],
        'RoleArn': 'string'
    },
    'CognitoStreams': {
        'StreamName': 'string',
        'RoleArn': 'string',
        'StreamingStatus': 'ENABLED'|'DISABLED'
    }
}


Response Structure

(dict) --The output for the GetIdentityPoolConfiguration operation.

IdentityPoolId (string) --A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.

PushSync (dict) --Options to apply to this identity pool for push synchronization.

ApplicationArns (list) --List of SNS platform application ARNs that could be used by clients.

(string) --


RoleArn (string) --A role configured to allow Cognito to call SNS on behalf of the developer.



CognitoStreams (dict) -- Options to apply to this identity pool for Amazon Cognito streams.
StreamName (string) -- The name of the Cognito stream to receive updates. This stream must be in the developers account and in the same region as the identity pool.
RoleArn (string) -- The ARN of the role Amazon Cognito can assume in order to publish to the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke PutRecord on your Cognito stream.
StreamingStatus (string) -- Status of the Cognito streams. Valid values are:ENABLED - Streaming of updates to identity pool is enabled.
DISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail if StreamingStatus is DISABLED.








Exceptions

CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.ResourceNotFoundException
CognitoSync.Client.exceptions.InternalErrorException
CognitoSync.Client.exceptions.TooManyRequestsException


    :return: {
        'IdentityPoolId': 'string',
        'PushSync': {
            'ApplicationArns': [
                'string',
            ],
            'RoleArn': 'string'
        },
        'CognitoStreams': {
            'StreamName': 'string',
            'RoleArn': 'string',
            'StreamingStatus': 'ENABLED'|'DISABLED'
        }
    }
    
    
    :returns: 
    CognitoSync.Client.exceptions.NotAuthorizedException
    CognitoSync.Client.exceptions.InvalidParameterException
    CognitoSync.Client.exceptions.ResourceNotFoundException
    CognitoSync.Client.exceptions.InternalErrorException
    CognitoSync.Client.exceptions.TooManyRequestsException
    
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

def list_datasets(IdentityPoolId=None, IdentityId=None, NextToken=None, MaxResults=None):
    """
    Lists datasets for an identity. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.
    ListDatasets can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use the Cognito Identity credentials to make this API call.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_datasets(
        IdentityPoolId='string',
        IdentityId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :type IdentityId: string
    :param IdentityId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :type NextToken: string
    :param NextToken: A pagination token for obtaining the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'Datasets': [
        {
            'IdentityId': 'string',
            'DatasetName': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'LastModifiedDate': datetime(2015, 1, 1),
            'LastModifiedBy': 'string',
            'DataStorage': 123,
            'NumRecords': 123
        },
    ],
    'Count': 123,
    'NextToken': 'string'
}


Response Structure

(dict) -- Returned for a successful ListDatasets request.
Datasets (list) -- A set of datasets.
(dict) -- A collection of data for an identity pool. An identity pool can have multiple datasets. A dataset is per identity and can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don\'t exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.
IdentityId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
DatasetName (string) -- A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).
CreationDate (datetime) -- Date on which the dataset was created.
LastModifiedDate (datetime) -- Date when the dataset was last modified.
LastModifiedBy (string) -- The device that made the last change to this dataset.
DataStorage (integer) -- Total size in bytes of the records in this dataset.
NumRecords (integer) -- Number of records in this dataset.




Count (integer) -- Number of datasets returned.
NextToken (string) -- A pagination token for obtaining the next page of results.






Exceptions

CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.InternalErrorException
CognitoSync.Client.exceptions.TooManyRequestsException


    :return: {
        'Datasets': [
            {
                'IdentityId': 'string',
                'DatasetName': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'LastModifiedDate': datetime(2015, 1, 1),
                'LastModifiedBy': 'string',
                'DataStorage': 123,
                'NumRecords': 123
            },
        ],
        'Count': 123,
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- Returned for a successful ListDatasets request.
    Datasets (list) -- A set of datasets.
    (dict) -- A collection of data for an identity pool. An identity pool can have multiple datasets. A dataset is per identity and can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don\'t exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.
    IdentityId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    DatasetName (string) -- A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).
    CreationDate (datetime) -- Date on which the dataset was created.
    LastModifiedDate (datetime) -- Date when the dataset was last modified.
    LastModifiedBy (string) -- The device that made the last change to this dataset.
    DataStorage (integer) -- Total size in bytes of the records in this dataset.
    NumRecords (integer) -- Number of records in this dataset.
    
    
    
    
    Count (integer) -- Number of datasets returned.
    NextToken (string) -- A pagination token for obtaining the next page of results.
    
    
    
    """
    pass

def list_identity_pool_usage(NextToken=None, MaxResults=None):
    """
    Gets a list of identity pools registered with Cognito.
    ListIdentityPool can only be called with developer credentials. You cannot make this API call with the temporary user credentials provided by Cognito Identity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_identity_pool_usage(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: A pagination token for obtaining the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityPoolUsages': [
        {
            'IdentityPoolId': 'string',
            'SyncSessionsCount': 123,
            'DataStorage': 123,
            'LastModifiedDate': datetime(2015, 1, 1)
        },
    ],
    'MaxResults': 123,
    'Count': 123,
    'NextToken': 'string'
}


Response Structure

(dict) -- Returned for a successful ListIdentityPoolUsage request.
IdentityPoolUsages (list) -- Usage information for the identity pools.
(dict) -- Usage information for the identity pool.
IdentityPoolId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
SyncSessionsCount (integer) -- Number of sync sessions for the identity pool.
DataStorage (integer) -- Data storage information for the identity pool.
LastModifiedDate (datetime) -- Date on which the identity pool was last modified.




MaxResults (integer) -- The maximum number of results to be returned.
Count (integer) -- Total number of identities for the identity pool.
NextToken (string) -- A pagination token for obtaining the next page of results.






Exceptions

CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.InternalErrorException
CognitoSync.Client.exceptions.TooManyRequestsException


    :return: {
        'IdentityPoolUsages': [
            {
                'IdentityPoolId': 'string',
                'SyncSessionsCount': 123,
                'DataStorage': 123,
                'LastModifiedDate': datetime(2015, 1, 1)
            },
        ],
        'MaxResults': 123,
        'Count': 123,
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- Returned for a successful ListIdentityPoolUsage request.
    IdentityPoolUsages (list) -- Usage information for the identity pools.
    (dict) -- Usage information for the identity pool.
    IdentityPoolId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    SyncSessionsCount (integer) -- Number of sync sessions for the identity pool.
    DataStorage (integer) -- Data storage information for the identity pool.
    LastModifiedDate (datetime) -- Date on which the identity pool was last modified.
    
    
    
    
    MaxResults (integer) -- The maximum number of results to be returned.
    Count (integer) -- Total number of identities for the identity pool.
    NextToken (string) -- A pagination token for obtaining the next page of results.
    
    
    
    """
    pass

def list_records(IdentityPoolId=None, IdentityId=None, DatasetName=None, LastSyncCount=None, NextToken=None, MaxResults=None, SyncSessionToken=None):
    """
    Gets paginated records, optionally changed after a particular sync count for a dataset and identity. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.
    ListRecords can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use Cognito Identity credentials to make this API call.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_records(
        IdentityPoolId='string',
        IdentityId='string',
        DatasetName='string',
        LastSyncCount=123,
        NextToken='string',
        MaxResults=123,
        SyncSessionToken='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :type IdentityId: string
    :param IdentityId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :type DatasetName: string
    :param DatasetName: [REQUIRED] A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).

    :type LastSyncCount: integer
    :param LastSyncCount: The last server sync count for this record.

    :type NextToken: string
    :param NextToken: A pagination token for obtaining the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned.

    :type SyncSessionToken: string
    :param SyncSessionToken: A token containing a session ID, identity ID, and expiration.

    :rtype: dict

ReturnsResponse Syntax
{
    'Records': [
        {
            'Key': 'string',
            'Value': 'string',
            'SyncCount': 123,
            'LastModifiedDate': datetime(2015, 1, 1),
            'LastModifiedBy': 'string',
            'DeviceLastModifiedDate': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string',
    'Count': 123,
    'DatasetSyncCount': 123,
    'LastModifiedBy': 'string',
    'MergedDatasetNames': [
        'string',
    ],
    'DatasetExists': True|False,
    'DatasetDeletedAfterRequestedSyncCount': True|False,
    'SyncSessionToken': 'string'
}


Response Structure

(dict) -- Returned for a successful ListRecordsRequest.
Records (list) -- A list of all records.
(dict) -- The basic data structure of a dataset.
Key (string) -- The key for the record.
Value (string) -- The value for the record.
SyncCount (integer) -- The server sync count for this record.
LastModifiedDate (datetime) -- The date on which the record was last modified.
LastModifiedBy (string) -- The user/device that made the last change to this record.
DeviceLastModifiedDate (datetime) -- The last modified date of the client device.




NextToken (string) -- A pagination token for obtaining the next page of results.
Count (integer) -- Total number of records.
DatasetSyncCount (integer) -- Server sync count for this dataset.
LastModifiedBy (string) -- The user/device that made the last change to this record.
MergedDatasetNames (list) -- Names of merged datasets.
(string) --


DatasetExists (boolean) -- Indicates whether the dataset exists.
DatasetDeletedAfterRequestedSyncCount (boolean) -- A boolean value specifying whether to delete the dataset locally.
SyncSessionToken (string) -- A token containing a session ID, identity ID, and expiration.






Exceptions

CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.TooManyRequestsException
CognitoSync.Client.exceptions.InternalErrorException


    :return: {
        'Records': [
            {
                'Key': 'string',
                'Value': 'string',
                'SyncCount': 123,
                'LastModifiedDate': datetime(2015, 1, 1),
                'LastModifiedBy': 'string',
                'DeviceLastModifiedDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string',
        'Count': 123,
        'DatasetSyncCount': 123,
        'LastModifiedBy': 'string',
        'MergedDatasetNames': [
            'string',
        ],
        'DatasetExists': True|False,
        'DatasetDeletedAfterRequestedSyncCount': True|False,
        'SyncSessionToken': 'string'
    }
    
    
    :returns: 
    (dict) -- Returned for a successful ListRecordsRequest.
    Records (list) -- A list of all records.
    (dict) -- The basic data structure of a dataset.
    Key (string) -- The key for the record.
    Value (string) -- The value for the record.
    SyncCount (integer) -- The server sync count for this record.
    LastModifiedDate (datetime) -- The date on which the record was last modified.
    LastModifiedBy (string) -- The user/device that made the last change to this record.
    DeviceLastModifiedDate (datetime) -- The last modified date of the client device.
    
    
    
    
    NextToken (string) -- A pagination token for obtaining the next page of results.
    Count (integer) -- Total number of records.
    DatasetSyncCount (integer) -- Server sync count for this dataset.
    LastModifiedBy (string) -- The user/device that made the last change to this record.
    MergedDatasetNames (list) -- Names of merged datasets.
    (string) --
    
    
    DatasetExists (boolean) -- Indicates whether the dataset exists.
    DatasetDeletedAfterRequestedSyncCount (boolean) -- A boolean value specifying whether to delete the dataset locally.
    SyncSessionToken (string) -- A token containing a session ID, identity ID, and expiration.
    
    
    
    """
    pass

def register_device(IdentityPoolId=None, IdentityId=None, Platform=None, Token=None):
    """
    Registers a device to receive push sync notifications.
    This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_device(
        IdentityPoolId='string',
        IdentityId='string',
        Platform='APNS'|'APNS_SANDBOX'|'GCM'|'ADM',
        Token='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nA name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. Here, the ID of the pool that the identity belongs to.\n

    :type IdentityId: string
    :param IdentityId: [REQUIRED]\nThe unique ID for this identity.\n

    :type Platform: string
    :param Platform: [REQUIRED]\nThe SNS platform type (e.g. GCM, SDM, APNS, APNS_SANDBOX).\n

    :type Token: string
    :param Token: [REQUIRED]\nThe push token.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DeviceId': 'string'
}


Response Structure

(dict) --
Response to a RegisterDevice request.

DeviceId (string) --
The unique ID generated for this device by Cognito.







Exceptions

CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.ResourceNotFoundException
CognitoSync.Client.exceptions.InternalErrorException
CognitoSync.Client.exceptions.InvalidConfigurationException
CognitoSync.Client.exceptions.TooManyRequestsException


    :return: {
        'DeviceId': 'string'
    }
    
    
    :returns: 
    CognitoSync.Client.exceptions.NotAuthorizedException
    CognitoSync.Client.exceptions.InvalidParameterException
    CognitoSync.Client.exceptions.ResourceNotFoundException
    CognitoSync.Client.exceptions.InternalErrorException
    CognitoSync.Client.exceptions.InvalidConfigurationException
    CognitoSync.Client.exceptions.TooManyRequestsException
    
    """
    pass

def set_cognito_events(IdentityPoolId=None, Events=None):
    """
    Sets the AWS Lambda function for a given event type for an identity pool. This request only updates the key/value pair specified. Other key/values pairs are not updated. To remove a key value pair, pass a empty value for the particular key.
    This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_cognito_events(
        IdentityPoolId='string',
        Events={
            'string': 'string'
        }
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nThe Cognito Identity Pool to use when configuring Cognito Events\n

    :type Events: dict
    :param Events: [REQUIRED]\nThe events to configure\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    CognitoSync.Client.exceptions.InvalidParameterException
    CognitoSync.Client.exceptions.ResourceNotFoundException
    CognitoSync.Client.exceptions.NotAuthorizedException
    CognitoSync.Client.exceptions.InternalErrorException
    CognitoSync.Client.exceptions.TooManyRequestsException
    
    """
    pass

def set_identity_pool_configuration(IdentityPoolId=None, PushSync=None, CognitoStreams=None):
    """
    Sets the necessary configuration for push sync.
    This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_identity_pool_configuration(
        IdentityPoolId='string',
        PushSync={
            'ApplicationArns': [
                'string',
            ],
            'RoleArn': 'string'
        },
        CognitoStreams={
            'StreamName': 'string',
            'RoleArn': 'string',
            'StreamingStatus': 'ENABLED'|'DISABLED'
        }
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nA name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool to modify.\n

    :type PushSync: dict
    :param PushSync: Options to apply to this identity pool for push synchronization.\n\nApplicationArns (list) --List of SNS platform application ARNs that could be used by clients.\n\n(string) --\n\n\nRoleArn (string) --A role configured to allow Cognito to call SNS on behalf of the developer.\n\n\n

    :type CognitoStreams: dict
    :param CognitoStreams: Options to apply to this identity pool for Amazon Cognito streams.\n\nStreamName (string) -- The name of the Cognito stream to receive updates. This stream must be in the developers account and in the same region as the identity pool.\nRoleArn (string) -- The ARN of the role Amazon Cognito can assume in order to publish to the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke PutRecord on your Cognito stream.\nStreamingStatus (string) -- Status of the Cognito streams. Valid values are:ENABLED - Streaming of updates to identity pool is enabled.\nDISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail if StreamingStatus is DISABLED.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityPoolId': 'string',
    'PushSync': {
        'ApplicationArns': [
            'string',
        ],
        'RoleArn': 'string'
    },
    'CognitoStreams': {
        'StreamName': 'string',
        'RoleArn': 'string',
        'StreamingStatus': 'ENABLED'|'DISABLED'
    }
}


Response Structure

(dict) --
The output for the SetIdentityPoolConfiguration operation

IdentityPoolId (string) --
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.

PushSync (dict) --
Options to apply to this identity pool for push synchronization.

ApplicationArns (list) --
List of SNS platform application ARNs that could be used by clients.

(string) --


RoleArn (string) --
A role configured to allow Cognito to call SNS on behalf of the developer.



CognitoStreams (dict) -- Options to apply to this identity pool for Amazon Cognito streams.

StreamName (string) -- The name of the Cognito stream to receive updates. This stream must be in the developers account and in the same region as the identity pool.

RoleArn (string) -- The ARN of the role Amazon Cognito can assume in order to publish to the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke PutRecord on your Cognito stream.

StreamingStatus (string) -- Status of the Cognito streams. Valid values are:
ENABLED - Streaming of updates to identity pool is enabled.
DISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail if StreamingStatus is DISABLED.









Exceptions

CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.ResourceNotFoundException
CognitoSync.Client.exceptions.InternalErrorException
CognitoSync.Client.exceptions.TooManyRequestsException
CognitoSync.Client.exceptions.ConcurrentModificationException


    :return: {
        'IdentityPoolId': 'string',
        'PushSync': {
            'ApplicationArns': [
                'string',
            ],
            'RoleArn': 'string'
        },
        'CognitoStreams': {
            'StreamName': 'string',
            'RoleArn': 'string',
            'StreamingStatus': 'ENABLED'|'DISABLED'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def subscribe_to_dataset(IdentityPoolId=None, IdentityId=None, DatasetName=None, DeviceId=None):
    """
    Subscribes to receive notifications when a dataset is modified by another device.
    This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.subscribe_to_dataset(
        IdentityPoolId='string',
        IdentityId='string',
        DatasetName='string',
        DeviceId='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nA name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which the identity belongs.\n

    :type IdentityId: string
    :param IdentityId: [REQUIRED]\nUnique ID for this identity.\n

    :type DatasetName: string
    :param DatasetName: [REQUIRED]\nThe name of the dataset to subcribe to.\n

    :type DeviceId: string
    :param DeviceId: [REQUIRED]\nThe unique ID generated for this device by Cognito.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Response to a SubscribeToDataset request.





Exceptions

CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.ResourceNotFoundException
CognitoSync.Client.exceptions.InternalErrorException
CognitoSync.Client.exceptions.InvalidConfigurationException
CognitoSync.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    CognitoSync.Client.exceptions.NotAuthorizedException
    CognitoSync.Client.exceptions.InvalidParameterException
    CognitoSync.Client.exceptions.ResourceNotFoundException
    CognitoSync.Client.exceptions.InternalErrorException
    CognitoSync.Client.exceptions.InvalidConfigurationException
    CognitoSync.Client.exceptions.TooManyRequestsException
    
    """
    pass

def unsubscribe_from_dataset(IdentityPoolId=None, IdentityId=None, DatasetName=None, DeviceId=None):
    """
    Unsubscribes from receiving notifications when a dataset is modified by another device.
    This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.unsubscribe_from_dataset(
        IdentityPoolId='string',
        IdentityId='string',
        DatasetName='string',
        DeviceId='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED]\nA name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which this identity belongs.\n

    :type IdentityId: string
    :param IdentityId: [REQUIRED]\nUnique ID for this identity.\n

    :type DatasetName: string
    :param DatasetName: [REQUIRED]\nThe name of the dataset from which to unsubcribe.\n

    :type DeviceId: string
    :param DeviceId: [REQUIRED]\nThe unique ID generated for this device by Cognito.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Response to an UnsubscribeFromDataset request.





Exceptions

CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.ResourceNotFoundException
CognitoSync.Client.exceptions.InternalErrorException
CognitoSync.Client.exceptions.InvalidConfigurationException
CognitoSync.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    CognitoSync.Client.exceptions.NotAuthorizedException
    CognitoSync.Client.exceptions.InvalidParameterException
    CognitoSync.Client.exceptions.ResourceNotFoundException
    CognitoSync.Client.exceptions.InternalErrorException
    CognitoSync.Client.exceptions.InvalidConfigurationException
    CognitoSync.Client.exceptions.TooManyRequestsException
    
    """
    pass

def update_records(IdentityPoolId=None, IdentityId=None, DatasetName=None, DeviceId=None, RecordPatches=None, SyncSessionToken=None, ClientContext=None):
    """
    Posts updates to records and adds and deletes records for a dataset and user.
    The sync count in the record patch is your last known sync count for that record. The server will reject an UpdateRecords request with a ResourceConflictException if you try to patch a record with a new value but a stale sync count.
    For example, if the sync count on the server is 5 for a key called highScore and you try and submit a new highScore with sync count of 4, the request will be rejected. To obtain the current sync count for a record, call ListRecords. On a successful update of the record, the response returns the new sync count for that record. You should present that sync count the next time you try to update that same record. When the record does not exist, specify the sync count as 0.
    This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_records(
        IdentityPoolId='string',
        IdentityId='string',
        DatasetName='string',
        DeviceId='string',
        RecordPatches=[
            {
                'Op': 'replace'|'remove',
                'Key': 'string',
                'Value': 'string',
                'SyncCount': 123,
                'DeviceLastModifiedDate': datetime(2015, 1, 1)
            },
        ],
        SyncSessionToken='string',
        ClientContext='string'
    )
    
    
    :type IdentityPoolId: string
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :type IdentityId: string
    :param IdentityId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.

    :type DatasetName: string
    :param DatasetName: [REQUIRED] A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).

    :type DeviceId: string
    :param DeviceId: The unique ID generated for this device by Cognito.

    :type RecordPatches: list
    :param RecordPatches: A list of patch operations.\n\n(dict) -- An update operation for a record.\nOp (string) -- [REQUIRED] An operation, either replace or remove.\nKey (string) -- [REQUIRED] The key associated with the record patch.\nValue (string) -- The value associated with the record patch.\nSyncCount (integer) -- [REQUIRED] Last known server sync count for this record. Set to 0 if unknown.\nDeviceLastModifiedDate (datetime) -- The last modified date of the client device.\n\n\n\n

    :type SyncSessionToken: string
    :param SyncSessionToken: [REQUIRED] The SyncSessionToken returned by a previous call to ListRecords for this dataset and identity.

    :type ClientContext: string
    :param ClientContext: Intended to supply a device ID that will populate the lastModifiedBy field referenced in other methods. The ClientContext field is not yet implemented.

    :rtype: dict

ReturnsResponse Syntax
{
    'Records': [
        {
            'Key': 'string',
            'Value': 'string',
            'SyncCount': 123,
            'LastModifiedDate': datetime(2015, 1, 1),
            'LastModifiedBy': 'string',
            'DeviceLastModifiedDate': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) -- Returned for a successful UpdateRecordsRequest.
Records (list) -- A list of records that have been updated.
(dict) -- The basic data structure of a dataset.
Key (string) -- The key for the record.
Value (string) -- The value for the record.
SyncCount (integer) -- The server sync count for this record.
LastModifiedDate (datetime) -- The date on which the record was last modified.
LastModifiedBy (string) -- The user/device that made the last change to this record.
DeviceLastModifiedDate (datetime) -- The last modified date of the client device.










Exceptions

CognitoSync.Client.exceptions.InvalidParameterException
CognitoSync.Client.exceptions.LimitExceededException
CognitoSync.Client.exceptions.NotAuthorizedException
CognitoSync.Client.exceptions.ResourceNotFoundException
CognitoSync.Client.exceptions.ResourceConflictException
CognitoSync.Client.exceptions.InvalidLambdaFunctionOutputException
CognitoSync.Client.exceptions.LambdaThrottledException
CognitoSync.Client.exceptions.TooManyRequestsException
CognitoSync.Client.exceptions.InternalErrorException


    :return: {
        'Records': [
            {
                'Key': 'string',
                'Value': 'string',
                'SyncCount': 123,
                'LastModifiedDate': datetime(2015, 1, 1),
                'LastModifiedBy': 'string',
                'DeviceLastModifiedDate': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    (dict) -- Returned for a successful UpdateRecordsRequest.
    Records (list) -- A list of records that have been updated.
    (dict) -- The basic data structure of a dataset.
    Key (string) -- The key for the record.
    Value (string) -- The value for the record.
    SyncCount (integer) -- The server sync count for this record.
    LastModifiedDate (datetime) -- The date on which the record was last modified.
    LastModifiedBy (string) -- The user/device that made the last change to this record.
    DeviceLastModifiedDate (datetime) -- The last modified date of the client device.
    
    
    
    
    
    
    
    """
    pass

