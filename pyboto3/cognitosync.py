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


def bulk_publish(IdentityPoolId=None):
    """
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            Return typedict
            ReturnsResponse Syntax{
              'IdentityPoolId': 'string'
            }
            Response Structure
            (dict) -- The output for the BulkPublish operation.
            IdentityPoolId (string) -- A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            
            
    :type IdentityPoolId: string
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


def delete_dataset(IdentityPoolId=None, IdentityId=None, DatasetName=None):
    """
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type IdentityPoolId: string
    :param IdentityId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type IdentityId: string
    :param DatasetName: [REQUIRED] A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
    :type DatasetName: string
    """
    pass


def describe_dataset(IdentityPoolId=None, IdentityId=None, DatasetName=None):
    """
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type IdentityPoolId: string
    :param IdentityId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type IdentityId: string
    :param DatasetName: [REQUIRED] A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
    :type DatasetName: string
    """
    pass


def describe_identity_pool_usage(IdentityPoolId=None):
    """
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            Return typedict
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
            
            
    :type IdentityPoolId: string
    """
    pass


def describe_identity_usage(IdentityPoolId=None, IdentityId=None):
    """
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type IdentityPoolId: string
    :param IdentityId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type IdentityId: string
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


def get_bulk_publish_details(IdentityPoolId=None):
    """
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            Return typedict
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
            
            
    :type IdentityPoolId: string
    """
    pass


def get_cognito_events(IdentityPoolId=None):
    """
    :param IdentityPoolId: [REQUIRED]
            The Cognito Identity Pool ID for the request
            Return typedict
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
            
            
            
    :type IdentityPoolId: string
    """
    pass


def get_identity_pool_configuration(IdentityPoolId=None):
    """
    :param IdentityPoolId: [REQUIRED]
            A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool for which to return a configuration.
            Return typedict
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
            
            
            
    :type IdentityPoolId: string
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


def list_datasets(IdentityPoolId=None, IdentityId=None, NextToken=None, MaxResults=None):
    """
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type IdentityPoolId: string
    :param IdentityId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type IdentityId: string
    :param NextToken: A pagination token for obtaining the next page of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to be returned.
    :type MaxResults: integer
    """
    pass


def list_identity_pool_usage(NextToken=None, MaxResults=None):
    """
    :param NextToken: A pagination token for obtaining the next page of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to be returned.
    :type MaxResults: integer
    """
    pass


def list_records(IdentityPoolId=None, IdentityId=None, DatasetName=None, LastSyncCount=None, NextToken=None,
                 MaxResults=None, SyncSessionToken=None):
    """
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type IdentityPoolId: string
    :param IdentityId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type IdentityId: string
    :param DatasetName: [REQUIRED] A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
    :type DatasetName: string
    :param LastSyncCount: The last server sync count for this record.
    :type LastSyncCount: integer
    :param NextToken: A pagination token for obtaining the next page of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to be returned.
    :type MaxResults: integer
    :param SyncSessionToken: A token containing a session ID, identity ID, and expiration.
    :type SyncSessionToken: string
    """
    pass


def register_device(IdentityPoolId=None, IdentityId=None, Platform=None, Token=None):
    """
    :param IdentityPoolId: [REQUIRED]
            A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. Here, the ID of the pool that the identity belongs to.
            
    :type IdentityPoolId: string
    :param IdentityId: [REQUIRED]
            The unique ID for this identity.
            
    :type IdentityId: string
    :param Platform: [REQUIRED]
            The SNS platform type (e.g. GCM, SDM, APNS, APNS_SANDBOX).
            
    :type Platform: string
    :param Token: [REQUIRED]
            The push token.
            
    :type Token: string
    """
    pass


def set_cognito_events(IdentityPoolId=None, Events=None):
    """
    :param IdentityPoolId: [REQUIRED]
            The Cognito Identity Pool to use when configuring Cognito Events
            
    :type IdentityPoolId: string
    :param Events: [REQUIRED]
            The events to configure
            (string) --
            (string) --
            
    :type Events: dict
    """
    pass


def set_identity_pool_configuration(IdentityPoolId=None, PushSync=None, CognitoStreams=None):
    """
    :param IdentityPoolId: [REQUIRED]
            A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool to modify.
            
    :type IdentityPoolId: string
    :param PushSync: Options to apply to this identity pool for push synchronization.
            ApplicationArns (list) --List of SNS platform application ARNs that could be used by clients.
            (string) --
            RoleArn (string) --A role configured to allow Cognito to call SNS on behalf of the developer.
            
    :type PushSync: dict
    :param CognitoStreams: Options to apply to this identity pool for Amazon Cognito streams.
            StreamName (string) -- The name of the Cognito stream to receive updates. This stream must be in the developers account and in the same region as the identity pool.
            RoleArn (string) -- The ARN of the role Amazon Cognito can assume in order to publish to the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke PutRecord on your Cognito stream.
            StreamingStatus (string) -- Status of the Cognito streams. Valid values are:ENABLED - Streaming of updates to identity pool is enabled.
            DISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail if StreamingStatus is DISABLED.
            
    :type CognitoStreams: dict
    """
    pass


def subscribe_to_dataset(IdentityPoolId=None, IdentityId=None, DatasetName=None, DeviceId=None):
    """
    :param IdentityPoolId: [REQUIRED]
            A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which the identity belongs.
            
    :type IdentityPoolId: string
    :param IdentityId: [REQUIRED]
            Unique ID for this identity.
            
    :type IdentityId: string
    :param DatasetName: [REQUIRED]
            The name of the dataset to subcribe to.
            
    :type DatasetName: string
    :param DeviceId: [REQUIRED]
            The unique ID generated for this device by Cognito.
            
    :type DeviceId: string
    """
    pass


def unsubscribe_from_dataset(IdentityPoolId=None, IdentityId=None, DatasetName=None, DeviceId=None):
    """
    :param IdentityPoolId: [REQUIRED]
            A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which this identity belongs.
            
    :type IdentityPoolId: string
    :param IdentityId: [REQUIRED]
            Unique ID for this identity.
            
    :type IdentityId: string
    :param DatasetName: [REQUIRED]
            The name of the dataset from which to unsubcribe.
            
    :type DatasetName: string
    :param DeviceId: [REQUIRED]
            The unique ID generated for this device by Cognito.
            
    :type DeviceId: string
    """
    pass


def update_records(IdentityPoolId=None, IdentityId=None, DatasetName=None, DeviceId=None, RecordPatches=None,
                   SyncSessionToken=None, ClientContext=None):
    """
    :param IdentityPoolId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type IdentityPoolId: string
    :param IdentityId: [REQUIRED] A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type IdentityId: string
    :param DatasetName: [REQUIRED] A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
    :type DatasetName: string
    :param DeviceId: The unique ID generated for this device by Cognito.
    :type DeviceId: string
    :param RecordPatches: A list of patch operations.
            (dict) -- An update operation for a record.
            Op (string) -- [REQUIRED] An operation, either replace or remove.
            Key (string) -- [REQUIRED] The key associated with the record patch.
            Value (string) -- The value associated with the record patch.
            SyncCount (integer) -- [REQUIRED] Last known server sync count for this record. Set to 0 if unknown.
            DeviceLastModifiedDate (datetime) -- The last modified date of the client device.
            
    :type RecordPatches: list
    :param SyncSessionToken: [REQUIRED] The SyncSessionToken returned by a previous call to ListRecords for this dataset and identity.
    :type SyncSessionToken: string
    :param ClientContext: Intended to supply a device ID that will populate the lastModifiedBy field referenced in other methods. The ClientContext field is not yet implemented.
    :type ClientContext: string
    """
    pass
