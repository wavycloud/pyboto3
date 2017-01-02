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

def abort_multipart_upload(Bucket=None, Key=None, UploadId=None, RequestPayer=None):
    """
    Aborts a multipart upload.
    To verify that all parts have been removed, so you don't get charged for the part storage, you should call the List Parts operation and ensure the parts list is empty.
    See also: AWS API Documentation
    
    
    :example: response = client.abort_multipart_upload(
        Bucket='string',
        Key='string',
        UploadId='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Key: string
    :param Key: [REQUIRED]

    :type UploadId: string
    :param UploadId: [REQUIRED]

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :rtype: dict
    :return: {
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    (dict) --
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    
    
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    """
    pass

def complete_multipart_upload(Bucket=None, Key=None, MultipartUpload=None, UploadId=None, RequestPayer=None):
    """
    Completes a multipart upload by assembling previously uploaded parts.
    See also: AWS API Documentation
    
    
    :example: response = client.complete_multipart_upload(
        Bucket='string',
        Key='string',
        MultipartUpload={
            'Parts': [
                {
                    'ETag': 'string',
                    'PartNumber': 123
                },
            ]
        },
        UploadId='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Key: string
    :param Key: [REQUIRED]

    :type MultipartUpload: dict
    :param MultipartUpload: 
            Parts (list) --
            (dict) --
            ETag (string) -- Entity tag returned when the part was uploaded.
            PartNumber (integer) -- Part number that identifies the part. This is a positive integer between 1 and 10,000.
            
            

    :type UploadId: string
    :param UploadId: [REQUIRED]

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :rtype: dict
    :return: {
        'Location': 'string',
        'Bucket': 'string',
        'Key': 'string',
        'Expiration': 'string',
        'ETag': 'string',
        'ServerSideEncryption': 'AES256'|'aws:kms',
        'VersionId': 'string',
        'SSEKMSKeyId': 'string',
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    (dict) --
    Location (string) --
    Bucket (string) --
    Key (string) --
    Expiration (string) -- If the object expiration is configured, this will contain the expiration date (expiry-date) and rule ID (rule-id). The value of rule-id is URL encoded.
    ETag (string) -- Entity tag of the object.
    ServerSideEncryption (string) -- The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
    VersionId (string) -- Version of the object.
    SSEKMSKeyId (string) -- If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    
    
    
    """
    pass

def copy(CopySource=None, Bucket=None, Key=None, ExtraArgs=None, Callback=None, SourceClient=None, Config=None):
    """
    Copy an object from one S3 location to another.
    This is a managed transfer which will perform a multipart copy in
    multiple threads if necessary.
    :
    
    :example: import boto3
    s3 = boto3.resource('s3')
    copy_source = {
        'Bucket': 'mybucket',
        'Key': 'mykey'
    }
    s3.meta.client.copy(copy_source, 'otherbucket', 'otherkey')
    
    
    :type CopySource: dict
    :param CopySource: The name of the source bucket, key name of the
            source object, and optional version ID of the source object. The
            dictionary format is:
            {'Bucket': 'bucket', 'Key': 'key', 'VersionId': 'id'}. Note
            that the VersionId key is optional and may be omitted.

    :type Bucket: str
    :param Bucket: The name of the bucket to copy to

    :type Key: str
    :param Key: The name of the key to copy to

    :type ExtraArgs: dict
    :param ExtraArgs: Extra arguments that may be passed to the
            client operation

    :type Callback: method
    :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the copy.

    :type SourceClient: botocore or boto3 Client
    :param SourceClient: The client to be used for operation that
            may happen at the source object. For example, this client is
            used for the head_object that determines the size of the copy.
            If no client is provided, the current client is used as the client
            for the source object.

    :type Config: boto3.s3.transfer.TransferConfig
    :param Config: The transfer configuration to be used when performing the
            copy.

    """
    pass

def copy_object(ACL=None, Bucket=None, CacheControl=None, ContentDisposition=None, ContentEncoding=None, ContentLanguage=None, ContentType=None, CopySource=None, CopySourceIfMatch=None, CopySourceIfModifiedSince=None, CopySourceIfNoneMatch=None, CopySourceIfUnmodifiedSince=None, Expires=None, GrantFullControl=None, GrantRead=None, GrantReadACP=None, GrantWriteACP=None, Key=None, Metadata=None, MetadataDirective=None, TaggingDirective=None, ServerSideEncryption=None, StorageClass=None, WebsiteRedirectLocation=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, SSEKMSKeyId=None, CopySourceSSECustomerAlgorithm=None, CopySourceSSECustomerKey=None, CopySourceSSECustomerKeyMD5=None, RequestPayer=None, Tagging=None):
    """
    Creates a copy of an object that is already stored in Amazon S3.
    See also: AWS API Documentation
    
    
    :example: response = client.copy_object(
        ACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'|'bucket-owner-read'|'bucket-owner-full-control',
        Bucket='string',
        CacheControl='string',
        ContentDisposition='string',
        ContentEncoding='string',
        ContentLanguage='string',
        ContentType='string',
        CopySource='string' or {'Bucket': 'string', 'Key': 'string', 'VersionId': 'string'},
        CopySourceIfMatch='string',
        CopySourceIfModifiedSince=datetime(2015, 1, 1),
        CopySourceIfNoneMatch='string',
        CopySourceIfUnmodifiedSince=datetime(2015, 1, 1),
        Expires=datetime(2015, 1, 1),
        GrantFullControl='string',
        GrantRead='string',
        GrantReadACP='string',
        GrantWriteACP='string',
        Key='string',
        Metadata={
            'string': 'string'
        },
        MetadataDirective='COPY'|'REPLACE',
        TaggingDirective='COPY'|'REPLACE',
        ServerSideEncryption='AES256'|'aws:kms',
        StorageClass='STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA',
        WebsiteRedirectLocation='string',
        SSECustomerAlgorithm='string',
        SSECustomerKey='string',
        SSEKMSKeyId='string',
        CopySourceSSECustomerAlgorithm='string',
        CopySourceSSECustomerKey='string',
        RequestPayer='requester',
        Tagging='string'
    )
    
    
    :type ACL: string
    :param ACL: The canned ACL to apply to the object.

    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type CacheControl: string
    :param CacheControl: Specifies caching behavior along the request/reply chain.

    :type ContentDisposition: string
    :param ContentDisposition: Specifies presentational information for the object.

    :type ContentEncoding: string
    :param ContentEncoding: Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

    :type ContentLanguage: string
    :param ContentLanguage: The language the content is in.

    :type ContentType: string
    :param ContentType: A standard MIME type describing the format of the object data.

    :type CopySource: str or dict
    :param CopySource: [REQUIRED] The name of the source bucket, key name of the source object, and optional version ID of the source object. You can either provide this value as a string or a dictionary. The string form is {bucket}/{key} or {bucket}/{key}?versionId={versionId} if you want to copy a specific version. You can also provide this value as a dictionary. The dictionary format is recommended over the string format because it is more explicit. The dictionary format is: {'Bucket': 'bucket', 'Key': 'key', 'VersionId': 'id'}. Note that the VersionId key is optional and may be omitted.

    :type CopySourceIfMatch: string
    :param CopySourceIfMatch: Copies the object if its entity tag (ETag) matches the specified tag.

    :type CopySourceIfModifiedSince: datetime
    :param CopySourceIfModifiedSince: Copies the object if it has been modified since the specified time.

    :type CopySourceIfNoneMatch: string
    :param CopySourceIfNoneMatch: Copies the object if its entity tag (ETag) is different than the specified ETag.

    :type CopySourceIfUnmodifiedSince: datetime
    :param CopySourceIfUnmodifiedSince: Copies the object if it hasn't been modified since the specified time.

    :type Expires: datetime
    :param Expires: The date and time at which the object is no longer cacheable.

    :type GrantFullControl: string
    :param GrantFullControl: Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.

    :type GrantRead: string
    :param GrantRead: Allows grantee to read the object data and its metadata.

    :type GrantReadACP: string
    :param GrantReadACP: Allows grantee to read the object ACL.

    :type GrantWriteACP: string
    :param GrantWriteACP: Allows grantee to write the ACL for the applicable object.

    :type Key: string
    :param Key: [REQUIRED]

    :type Metadata: dict
    :param Metadata: A map of metadata to store with the object in S3.
            (string) --
            (string) --
            

    :type MetadataDirective: string
    :param MetadataDirective: Specifies whether the metadata is copied from the source object or replaced with metadata provided in the request.

    :type TaggingDirective: string
    :param TaggingDirective: Specifies whether the object tag-set are copied from the source object or replaced with tag-set provided in the request.

    :type ServerSideEncryption: string
    :param ServerSideEncryption: The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).

    :type StorageClass: string
    :param StorageClass: The type of storage to use for the object. Defaults to 'STANDARD'.

    :type WebsiteRedirectLocation: string
    :param WebsiteRedirectLocation: If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.

    :type SSECustomerAlgorithm: string
    :param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (e.g., AES256).

    :type SSECustomerKey: string
    :param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side -encryption -customer-algorithm header.

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required

    :type SSEKMSKeyId: string
    :param SSEKMSKeyId: Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version

    :type CopySourceSSECustomerAlgorithm: string
    :param CopySourceSSECustomerAlgorithm: Specifies the algorithm to use when decrypting the source object (e.g., AES256).

    :type CopySourceSSECustomerKey: string
    :param CopySourceSSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.

    :type CopySourceSSECustomerKeyMD5: string
    :param CopySourceSSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :type Tagging: string
    :param Tagging: The tag-set for the object destination object this value must be used in conjunction with the TaggingDirective. The tag-set must be encoded as URL Query parameters

    :rtype: dict
    :return: {
        'CopyObjectResult': {
            'ETag': 'string',
            'LastModified': datetime(2015, 1, 1)
        },
        'Expiration': 'string',
        'CopySourceVersionId': 'string',
        'VersionId': 'string',
        'ServerSideEncryption': 'AES256'|'aws:kms',
        'SSECustomerAlgorithm': 'string',
        'SSECustomerKeyMD5': 'string',
        'SSEKMSKeyId': 'string',
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    (dict) --
    CopyObjectResult (dict) --
    ETag (string) --
    LastModified (datetime) --
    
    
    Expiration (string) -- If the object expiration is configured, the response includes this header.
    CopySourceVersionId (string) --
    VersionId (string) -- Version ID of the newly created copy.
    ServerSideEncryption (string) -- The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
    SSECustomerAlgorithm (string) -- If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
    SSECustomerKeyMD5 (string) -- If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
    SSEKMSKeyId (string) -- If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    
    
    
    """
    pass

def create_bucket(ACL=None, Bucket=None, CreateBucketConfiguration=None, GrantFullControl=None, GrantRead=None, GrantReadACP=None, GrantWrite=None, GrantWriteACP=None):
    """
    Creates a new bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.create_bucket(
        ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
        Bucket='string',
        CreateBucketConfiguration={
            'LocationConstraint': 'EU'|'eu-west-1'|'us-west-1'|'us-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1'|'cn-north-1'|'eu-central-1'
        },
        GrantFullControl='string',
        GrantRead='string',
        GrantReadACP='string',
        GrantWrite='string',
        GrantWriteACP='string'
    )
    
    
    :type ACL: string
    :param ACL: The canned ACL to apply to the bucket.

    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type CreateBucketConfiguration: dict
    :param CreateBucketConfiguration: 
            LocationConstraint (string) -- Specifies the region where the bucket will be created. If you don't specify a region, the bucket will be created in US Standard.
            

    :type GrantFullControl: string
    :param GrantFullControl: Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.

    :type GrantRead: string
    :param GrantRead: Allows grantee to list the objects in the bucket.

    :type GrantReadACP: string
    :param GrantReadACP: Allows grantee to read the bucket ACL.

    :type GrantWrite: string
    :param GrantWrite: Allows grantee to create, overwrite, and delete any object in the bucket.

    :type GrantWriteACP: string
    :param GrantWriteACP: Allows grantee to write the ACL for the applicable bucket.

    :rtype: dict
    :return: {
        'Location': 'string'
    }
    
    
    :returns: 
    (dict) --
    Location (string) --
    
    
    
    """
    pass

def create_multipart_upload(ACL=None, Bucket=None, CacheControl=None, ContentDisposition=None, ContentEncoding=None, ContentLanguage=None, ContentType=None, Expires=None, GrantFullControl=None, GrantRead=None, GrantReadACP=None, GrantWriteACP=None, Key=None, Metadata=None, ServerSideEncryption=None, StorageClass=None, WebsiteRedirectLocation=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, SSEKMSKeyId=None, RequestPayer=None):
    """
    Initiates a multipart upload and returns an upload ID.
    Note: After you initiate multipart upload and upload one or more parts, you must either complete or abort multipart upload in order to stop getting charged for storage of the uploaded parts. Only after you either complete or abort multipart upload, Amazon S3 frees up the parts storage and stops charging you for the parts storage.
    See also: AWS API Documentation
    
    
    :example: response = client.create_multipart_upload(
        ACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'|'bucket-owner-read'|'bucket-owner-full-control',
        Bucket='string',
        CacheControl='string',
        ContentDisposition='string',
        ContentEncoding='string',
        ContentLanguage='string',
        ContentType='string',
        Expires=datetime(2015, 1, 1),
        GrantFullControl='string',
        GrantRead='string',
        GrantReadACP='string',
        GrantWriteACP='string',
        Key='string',
        Metadata={
            'string': 'string'
        },
        ServerSideEncryption='AES256'|'aws:kms',
        StorageClass='STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA',
        WebsiteRedirectLocation='string',
        SSECustomerAlgorithm='string',
        SSECustomerKey='string',
        SSEKMSKeyId='string',
        RequestPayer='requester'
    )
    
    
    :type ACL: string
    :param ACL: The canned ACL to apply to the object.

    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type CacheControl: string
    :param CacheControl: Specifies caching behavior along the request/reply chain.

    :type ContentDisposition: string
    :param ContentDisposition: Specifies presentational information for the object.

    :type ContentEncoding: string
    :param ContentEncoding: Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

    :type ContentLanguage: string
    :param ContentLanguage: The language the content is in.

    :type ContentType: string
    :param ContentType: A standard MIME type describing the format of the object data.

    :type Expires: datetime
    :param Expires: The date and time at which the object is no longer cacheable.

    :type GrantFullControl: string
    :param GrantFullControl: Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.

    :type GrantRead: string
    :param GrantRead: Allows grantee to read the object data and its metadata.

    :type GrantReadACP: string
    :param GrantReadACP: Allows grantee to read the object ACL.

    :type GrantWriteACP: string
    :param GrantWriteACP: Allows grantee to write the ACL for the applicable object.

    :type Key: string
    :param Key: [REQUIRED]

    :type Metadata: dict
    :param Metadata: A map of metadata to store with the object in S3.
            (string) --
            (string) --
            

    :type ServerSideEncryption: string
    :param ServerSideEncryption: The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).

    :type StorageClass: string
    :param StorageClass: The type of storage to use for the object. Defaults to 'STANDARD'.

    :type WebsiteRedirectLocation: string
    :param WebsiteRedirectLocation: If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.

    :type SSECustomerAlgorithm: string
    :param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (e.g., AES256).

    :type SSECustomerKey: string
    :param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side -encryption -customer-algorithm header.

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required

    :type SSEKMSKeyId: string
    :param SSEKMSKeyId: Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :rtype: dict
    :return: {
        'AbortDate': datetime(2015, 1, 1),
        'AbortRuleId': 'string',
        'Bucket': 'string',
        'Key': 'string',
        'UploadId': 'string',
        'ServerSideEncryption': 'AES256'|'aws:kms',
        'SSECustomerAlgorithm': 'string',
        'SSECustomerKeyMD5': 'string',
        'SSEKMSKeyId': 'string',
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    (dict) --
    AbortDate (datetime) -- Date when multipart upload will become eligible for abort operation by lifecycle.
    AbortRuleId (string) -- Id of the lifecycle rule that makes a multipart upload eligible for abort operation.
    Bucket (string) -- Name of the bucket to which the multipart upload was initiated.
    Key (string) -- Object key for which the multipart upload was initiated.
    UploadId (string) -- ID for the initiated multipart upload.
    ServerSideEncryption (string) -- The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
    SSECustomerAlgorithm (string) -- If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
    SSECustomerKeyMD5 (string) -- If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
    SSEKMSKeyId (string) -- If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    
    
    
    """
    pass

def delete_bucket(Bucket=None):
    """
    Deletes the bucket. All objects (including all object versions and Delete Markers) in the bucket must be deleted before the bucket itself can be deleted.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bucket(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    """
    pass

def delete_bucket_analytics_configuration(Bucket=None, Id=None):
    """
    Deletes an analytics configuration for the bucket (specified by the analytics configuration ID).
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bucket_analytics_configuration(
        Bucket='string',
        Id='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] The name of the bucket from which an analytics configuration is deleted.

    :type Id: string
    :param Id: [REQUIRED] The identifier used to represent an analytics configuration.

    """
    pass

def delete_bucket_cors(Bucket=None):
    """
    Deletes the cors configuration information set for the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bucket_cors(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    """
    pass

def delete_bucket_inventory_configuration(Bucket=None, Id=None):
    """
    Deletes an inventory configuration (identified by the inventory ID) from the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bucket_inventory_configuration(
        Bucket='string',
        Id='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] The name of the bucket containing the inventory configuration to delete.

    :type Id: string
    :param Id: [REQUIRED] The ID used to identify the inventory configuration.

    """
    pass

def delete_bucket_lifecycle(Bucket=None):
    """
    Deletes the lifecycle configuration from the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bucket_lifecycle(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    """
    pass

def delete_bucket_metrics_configuration(Bucket=None, Id=None):
    """
    Deletes a metrics configuration (specified by the metrics configuration ID) from the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bucket_metrics_configuration(
        Bucket='string',
        Id='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] The name of the bucket containing the metrics configuration to delete.

    :type Id: string
    :param Id: [REQUIRED] The ID used to identify the metrics configuration.

    """
    pass

def delete_bucket_policy(Bucket=None):
    """
    Deletes the policy from the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bucket_policy(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    """
    pass

def delete_bucket_replication(Bucket=None):
    """
    Deletes the replication configuration from the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bucket_replication(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    """
    pass

def delete_bucket_tagging(Bucket=None):
    """
    Deletes the tags from the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bucket_tagging(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    """
    pass

def delete_bucket_website(Bucket=None):
    """
    This operation removes the website configuration from the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bucket_website(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    """
    pass

def delete_object(Bucket=None, Key=None, MFA=None, VersionId=None, RequestPayer=None):
    """
    Removes the null version (if there is one) of an object and inserts a delete marker, which becomes the latest version of the object. If there isn't a null version, Amazon S3 does not remove any objects.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_object(
        Bucket='string',
        Key='string',
        MFA='string',
        VersionId='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Key: string
    :param Key: [REQUIRED]

    :type MFA: string
    :param MFA: The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device.

    :type VersionId: string
    :param VersionId: VersionId used to reference a specific version of the object.

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :rtype: dict
    :return: {
        'DeleteMarker': True|False,
        'VersionId': 'string',
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    (dict) --
    DeleteMarker (boolean) -- Specifies whether the versioned object that was permanently deleted was (true) or was not (false) a delete marker.
    VersionId (string) -- Returns the version ID of the delete marker created as a result of the DELETE operation.
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    
    
    
    """
    pass

def delete_object_tagging(Bucket=None, Key=None, VersionId=None):
    """
    Removes the tag-set from an existing object.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_object_tagging(
        Bucket='string',
        Key='string',
        VersionId='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Key: string
    :param Key: [REQUIRED]

    :type VersionId: string
    :param VersionId: The versionId of the object that the tag-set will be removed from.

    :rtype: dict
    :return: {
        'VersionId': 'string'
    }
    
    
    :returns: 
    (dict) --
    VersionId (string) -- The versionId of the object the tag-set was removed from.
    
    
    
    """
    pass

def delete_objects(Bucket=None, Delete=None, MFA=None, RequestPayer=None):
    """
    This operation enables you to delete multiple objects from a bucket using a single HTTP request. You may specify up to 1000 keys.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_objects(
        Bucket='string',
        Delete={
            'Objects': [
                {
                    'Key': 'string',
                    'VersionId': 'string'
                },
            ],
            'Quiet': True|False
        },
        MFA='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Delete: dict
    :param Delete: [REQUIRED]
            Objects (list) -- [REQUIRED]
            (dict) --
            Key (string) -- [REQUIRED] Key name of the object to delete.
            VersionId (string) -- VersionId for the specific version of the object to delete.
            
            Quiet (boolean) -- Element to enable quiet mode for the request. When you add this element, you must set its value to true.
            

    :type MFA: string
    :param MFA: The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device.

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :rtype: dict
    :return: {
        'Deleted': [
            {
                'Key': 'string',
                'VersionId': 'string',
                'DeleteMarker': True|False,
                'DeleteMarkerVersionId': 'string'
            },
        ],
        'RequestCharged': 'requester',
        'Errors': [
            {
                'Key': 'string',
                'VersionId': 'string',
                'Code': 'string',
                'Message': 'string'
            },
        ]
    }
    
    
    :returns: 
    (dict) --
    Deleted (list) --
    (dict) --
    Key (string) --
    VersionId (string) --
    DeleteMarker (boolean) --
    DeleteMarkerVersionId (string) --
    
    
    
    
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    Errors (list) --
    (dict) --
    Key (string) --
    VersionId (string) --
    Code (string) --
    Message (string) --
    
    
    
    
    
    
    
    """
    pass

def download_file():
    """
    Download an S3 object to a file.
    :
    Similar behavior as S3Transfer's download_file() method,
    except that parameters are capitalized. Detailed examples can be found at
    S3Transfer's .
    
    :example: import boto3
    s3 = boto3.resource('s3')
    s3.meta.client.download_file('mybucket', 'hello.txt', '/tmp/hello.txt')
    
    
    """
    pass

def download_fileobj(Fileobj=None, Bucket=None, Key=None, ExtraArgs=None, Callback=None, Config=None):
    """
    Download an object from S3 to a file-like object.
    The file-like object must be in binary mode.
    This is a managed transfer which will perform a multipart download in
    multiple threads if necessary.
    :
    
    :example: import boto3
    s3 = boto3.client('s3')
    
    with open('filename', 'wb') as data:
        s3.download_fileobj('mybucket', 'mykey', data)
    
    
    :type Fileobj: a file-like object
    :param Fileobj: A file-like object to download into. At a minimum, it must
            implement the write method and must accept bytes.

    :type Bucket: str
    :param Bucket: The name of the bucket to download from.

    :type Key: str
    :param Key: The name of the key to download from.

    :type ExtraArgs: dict
    :param ExtraArgs: Extra arguments that may be passed to the
            client operation.

    :type Callback: method
    :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the download.

    :type Config: boto3.s3.transfer.TransferConfig
    :param Config: The transfer configuration to be used when performing the
            download.

    """
    pass

def generate_presigned_post(Bucket=None, Key=None, Fields=None, Conditions=None, ExpiresIn=None):
    """
    Builds the url and the form fields used for a presigned s3 post
    
    :type Bucket: string
    :param Bucket: The name of the bucket to presign the post to. Note that
            bucket related conditions should not be included in the
            conditions parameter.

    :type Key: string
    :param Key: Key name, optionally add ${filename} to the end to
            attach the submitted filename. Note that key related conditions and
            fields are filled out for you and should not be included in the
            Fields or Conditions parameter.

    :type Fields: dict
    :param Fields: A dictionary of prefilled form fields to build on top
            of. Elements that may be included are acl, Cache-Control,
            Content-Type, Content-Disposition, Content-Encoding, Expires,
            success_action_redirect, redirect, success_action_status,
            and x-amz-meta-.
            Note that if a particular element is included in the fields
            dictionary it will not be automatically added to the conditions
            list. You must specify a condition for the element as well.
            

    :type Conditions: list
    :param Conditions: A list of conditions to include in the policy. Each
            element can be either a list or a structure. For example:
            [
            {'acl': 'public-read'},
            ['content-length-range', 2, 5],
            ['starts-with', '$success_action_redirect', '']
            ]
            Conditions that are included may pertain to acl,
            content-length-range, Cache-Control, Content-Type,
            Content-Disposition, Content-Encoding, Expires,
            success_action_redirect, redirect, success_action_status,
            and/or x-amz-meta-.
            Note that if you include a condition, you must specify
            the a valid value in the fields dictionary as well. A value will
            not be added automatically to the fields dictionary based on the
            conditions.
            

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned post
            is valid for.

    :rtype: dict
    """
    pass

def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    Generate a presigned url given a client, its method, and arguments
    
    :type ClientMethod: string
    :param ClientMethod: The client method to presign for

    :type Params: dict
    :param Params: The parameters normally passed to
            ClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

    """
    pass

def get_bucket_accelerate_configuration(Bucket=None):
    """
    Returns the accelerate configuration of a bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_accelerate_configuration(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] Name of the bucket for which the accelerate configuration is retrieved.

    :rtype: dict
    :return: {
        'Status': 'Enabled'|'Suspended'
    }
    
    
    """
    pass

def get_bucket_acl(Bucket=None):
    """
    Gets the access control policy for the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_acl(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :rtype: dict
    :return: {
        'Owner': {
            'DisplayName': 'string',
            'ID': 'string'
        },
        'Grants': [
            {
                'Grantee': {
                    'DisplayName': 'string',
                    'EmailAddress': 'string',
                    'ID': 'string',
                    'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                    'URI': 'string'
                },
                'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
            },
        ]
    }
    
    
    """
    pass

def get_bucket_analytics_configuration(Bucket=None, Id=None):
    """
    Gets an analytics configuration for the bucket (specified by the analytics configuration ID).
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_analytics_configuration(
        Bucket='string',
        Id='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] The name of the bucket from which an analytics configuration is retrieved.

    :type Id: string
    :param Id: [REQUIRED] The identifier used to represent an analytics configuration.

    :rtype: dict
    :return: {
        'AnalyticsConfiguration': {
            'Id': 'string',
            'Filter': {
                'Prefix': 'string',
                'Tag': {
                    'Key': 'string',
                    'Value': 'string'
                },
                'And': {
                    'Prefix': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                }
            },
            'StorageClassAnalysis': {
                'DataExport': {
                    'OutputSchemaVersion': 'V_1',
                    'Destination': {
                        'S3BucketDestination': {
                            'Format': 'CSV',
                            'BucketAccountId': 'string',
                            'Bucket': 'string',
                            'Prefix': 'string'
                        }
                    }
                }
            }
        }
    }
    
    
    :returns: 
    (dict) --
    AnalyticsConfiguration (dict) -- The configuration and any analyses for the analytics filter.
    Id (string) -- The identifier used to represent an analytics configuration.
    Filter (dict) -- The filter used to describe a set of objects for analyses. A filter must have exactly one prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be considered in any analysis.
    Prefix (string) -- The prefix to use when evaluating an analytics filter.
    Tag (dict) -- The tag to use when evaluating an analytics filter.
    Key (string) -- Name of the tag.
    Value (string) -- Value of the tag.
    
    
    And (dict) -- A conjunction (logical AND) of predicates, which is used in evaluating an analytics filter. The operator must have at least two predicates.
    Prefix (string) -- The prefix to use when evaluating an AND predicate.
    Tags (list) -- The list of tags to use when evaluating an AND predicate.
    (dict) --
    Key (string) -- Name of the tag.
    Value (string) -- Value of the tag.
    
    
    
    
    
    
    
    
    StorageClassAnalysis (dict) -- If present, it indicates that data related to access patterns will be collected and made available to analyze the tradeoffs between different storage classes.
    DataExport (dict) -- A container used to describe how data related to the storage class analysis should be exported.
    OutputSchemaVersion (string) -- The version of the output schema to use when exporting data. Must be V_1.
    Destination (dict) -- The place to store the data for an analysis.
    S3BucketDestination (dict) -- A destination signifying output to an S3 bucket.
    Format (string) -- The file format used when exporting data to Amazon S3.
    BucketAccountId (string) -- The account ID that owns the destination bucket. If no account ID is provided, the owner will not be validated prior to exporting data.
    Bucket (string) -- The Amazon resource name (ARN) of the bucket to which data is exported.
    Prefix (string) -- The prefix to use when exporting data. The exported data begins with this prefix.
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def get_bucket_cors(Bucket=None):
    """
    Returns the cors configuration for the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_cors(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :rtype: dict
    :return: {
        'CORSRules': [
            {
                'AllowedHeaders': [
                    'string',
                ],
                'AllowedMethods': [
                    'string',
                ],
                'AllowedOrigins': [
                    'string',
                ],
                'ExposeHeaders': [
                    'string',
                ],
                'MaxAgeSeconds': 123
            },
        ]
    }
    
    
    """
    pass

def get_bucket_inventory_configuration(Bucket=None, Id=None):
    """
    Returns an inventory configuration (identified by the inventory ID) from the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_inventory_configuration(
        Bucket='string',
        Id='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] The name of the bucket containing the inventory configuration to retrieve.

    :type Id: string
    :param Id: [REQUIRED] The ID used to identify the inventory configuration.

    :rtype: dict
    :return: {
        'InventoryConfiguration': {
            'Destination': {
                'S3BucketDestination': {
                    'AccountId': 'string',
                    'Bucket': 'string',
                    'Format': 'CSV',
                    'Prefix': 'string'
                }
            },
            'IsEnabled': True|False,
            'Filter': {
                'Prefix': 'string'
            },
            'Id': 'string',
            'IncludedObjectVersions': 'All'|'Current',
            'OptionalFields': [
                'Size'|'LastModifiedDate'|'StorageClass'|'ETag'|'IsMultipartUploaded'|'ReplicationStatus',
            ],
            'Schedule': {
                'Frequency': 'Daily'|'Weekly'
            }
        }
    }
    
    
    :returns: 
    (dict) --
    InventoryConfiguration (dict) -- Specifies the inventory configuration.
    Destination (dict) -- Contains information about where to publish the inventory results.
    S3BucketDestination (dict) -- Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where inventory results are published.
    AccountId (string) -- The ID of the account that owns the destination bucket.
    Bucket (string) -- The Amazon resource name (ARN) of the bucket where inventory results will be published.
    Format (string) -- Specifies the output format of the inventory results.
    Prefix (string) -- The prefix that is prepended to all inventory results.
    
    
    
    
    IsEnabled (boolean) -- Specifies whether the inventory is enabled or disabled.
    Filter (dict) -- Specifies an inventory filter. The inventory only includes objects that meet the filter's criteria.
    Prefix (string) -- The prefix that an object must have to be included in the inventory results.
    
    
    Id (string) -- The ID used to identify the inventory configuration.
    IncludedObjectVersions (string) -- Specifies which object version(s) to included in the inventory results.
    OptionalFields (list) -- Contains the optional fields that are included in the inventory results.
    (string) --
    
    
    Schedule (dict) -- Specifies the schedule for generating inventory results.
    Frequency (string) -- Specifies how frequently inventory results are produced.
    
    
    
    
    
    
    
    """
    pass

def get_bucket_lifecycle(Bucket=None):
    """
    Deprecated, see the GetBucketLifecycleConfiguration operation.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_lifecycle(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :rtype: dict
    :return: {
        'Rules': [
            {
                'Expiration': {
                    'Date': datetime(2015, 1, 1),
                    'Days': 123,
                    'ExpiredObjectDeleteMarker': True|False
                },
                'ID': 'string',
                'Prefix': 'string',
                'Status': 'Enabled'|'Disabled',
                'Transition': {
                    'Date': datetime(2015, 1, 1),
                    'Days': 123,
                    'StorageClass': 'GLACIER'|'STANDARD_IA'
                },
                'NoncurrentVersionTransition': {
                    'NoncurrentDays': 123,
                    'StorageClass': 'GLACIER'|'STANDARD_IA'
                },
                'NoncurrentVersionExpiration': {
                    'NoncurrentDays': 123
                },
                'AbortIncompleteMultipartUpload': {
                    'DaysAfterInitiation': 123
                }
            },
        ]
    }
    
    
    """
    pass

def get_bucket_lifecycle_configuration(Bucket=None):
    """
    Returns the lifecycle configuration information set on the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_lifecycle_configuration(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :rtype: dict
    :return: {
        'Rules': [
            {
                'Expiration': {
                    'Date': datetime(2015, 1, 1),
                    'Days': 123,
                    'ExpiredObjectDeleteMarker': True|False
                },
                'ID': 'string',
                'Prefix': 'string',
                'Filter': {
                    'Prefix': 'string',
                    'Tag': {
                        'Key': 'string',
                        'Value': 'string'
                    },
                    'And': {
                        'Prefix': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    }
                },
                'Status': 'Enabled'|'Disabled',
                'Transitions': [
                    {
                        'Date': datetime(2015, 1, 1),
                        'Days': 123,
                        'StorageClass': 'GLACIER'|'STANDARD_IA'
                    },
                ],
                'NoncurrentVersionTransitions': [
                    {
                        'NoncurrentDays': 123,
                        'StorageClass': 'GLACIER'|'STANDARD_IA'
                    },
                ],
                'NoncurrentVersionExpiration': {
                    'NoncurrentDays': 123
                },
                'AbortIncompleteMultipartUpload': {
                    'DaysAfterInitiation': 123
                }
            },
        ]
    }
    
    
    """
    pass

def get_bucket_location(Bucket=None):
    """
    Returns the region the bucket resides in.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_location(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :rtype: dict
    :return: {
        'LocationConstraint': 'EU'|'eu-west-1'|'us-west-1'|'us-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1'|'cn-north-1'|'eu-central-1'
    }
    
    
    """
    pass

def get_bucket_logging(Bucket=None):
    """
    Returns the logging status of a bucket and the permissions users have to view and modify that status. To use GET, you must be the bucket owner.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_logging(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :rtype: dict
    :return: {
        'LoggingEnabled': {
            'TargetBucket': 'string',
            'TargetGrants': [
                {
                    'Grantee': {
                        'DisplayName': 'string',
                        'EmailAddress': 'string',
                        'ID': 'string',
                        'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                        'URI': 'string'
                    },
                    'Permission': 'FULL_CONTROL'|'READ'|'WRITE'
                },
            ],
            'TargetPrefix': 'string'
        }
    }
    
    
    """
    pass

def get_bucket_metrics_configuration(Bucket=None, Id=None):
    """
    Gets a metrics configuration (specified by the metrics configuration ID) from the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_metrics_configuration(
        Bucket='string',
        Id='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] The name of the bucket containing the metrics configuration to retrieve.

    :type Id: string
    :param Id: [REQUIRED] The ID used to identify the metrics configuration.

    :rtype: dict
    :return: {
        'MetricsConfiguration': {
            'Id': 'string',
            'Filter': {
                'Prefix': 'string',
                'Tag': {
                    'Key': 'string',
                    'Value': 'string'
                },
                'And': {
                    'Prefix': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                }
            }
        }
    }
    
    
    :returns: 
    (dict) --
    MetricsConfiguration (dict) -- Specifies the metrics configuration.
    Id (string) -- The ID used to identify the metrics configuration.
    Filter (dict) -- Specifies a metrics configuration filter. The metrics configuration will only include objects that meet the filter's criteria. A filter must be a prefix, a tag, or a conjunction (MetricsAndOperator).
    Prefix (string) -- The prefix used when evaluating a metrics filter.
    Tag (dict) -- The tag used when evaluating a metrics filter.
    Key (string) -- Name of the tag.
    Value (string) -- Value of the tag.
    
    
    And (dict) -- A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The operator must have at least two predicates, and an object must match all of the predicates in order for the filter to apply.
    Prefix (string) -- The prefix used when evaluating an AND predicate.
    Tags (list) -- The list of tags used when evaluating an AND predicate.
    (dict) --
    Key (string) -- Name of the tag.
    Value (string) -- Value of the tag.
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def get_bucket_notification(Bucket=None):
    """
    Deprecated, see the GetBucketNotificationConfiguration operation.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_notification(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] Name of the bucket to get the notification configuration for.

    :rtype: dict
    :return: {
        'TopicConfiguration': {
            'Id': 'string',
            'Events': [
                's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
            ],
            'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
            'Topic': 'string'
        },
        'QueueConfiguration': {
            'Id': 'string',
            'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
            'Events': [
                's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
            ],
            'Queue': 'string'
        },
        'CloudFunctionConfiguration': {
            'Id': 'string',
            'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
            'Events': [
                's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
            ],
            'CloudFunction': 'string',
            'InvocationRole': 'string'
        }
    }
    
    
    """
    pass

def get_bucket_notification_configuration(Bucket=None):
    """
    Returns the notification configuration of a bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_notification_configuration(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] Name of the bucket to get the notification configuration for.

    :rtype: dict
    :return: {
        'TopicConfigurations': [
            {
                'Id': 'string',
                'TopicArn': 'string',
                'Events': [
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
                ],
                'Filter': {
                    'Key': {
                        'FilterRules': [
                            {
                                'Name': 'prefix'|'suffix',
                                'Value': 'string'
                            },
                        ]
                    }
                }
            },
        ],
        'QueueConfigurations': [
            {
                'Id': 'string',
                'QueueArn': 'string',
                'Events': [
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
                ],
                'Filter': {
                    'Key': {
                        'FilterRules': [
                            {
                                'Name': 'prefix'|'suffix',
                                'Value': 'string'
                            },
                        ]
                    }
                }
            },
        ],
        'LambdaFunctionConfigurations': [
            {
                'Id': 'string',
                'LambdaFunctionArn': 'string',
                'Events': [
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
                ],
                'Filter': {
                    'Key': {
                        'FilterRules': [
                            {
                                'Name': 'prefix'|'suffix',
                                'Value': 'string'
                            },
                        ]
                    }
                }
            },
        ]
    }
    
    
    """
    pass

def get_bucket_policy(Bucket=None):
    """
    Returns the policy of a specified bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_policy(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :rtype: dict
    :return: {
        'Policy': 'string'
    }
    
    
    """
    pass

def get_bucket_replication(Bucket=None):
    """
    Returns the replication configuration of a bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_replication(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :rtype: dict
    :return: {
        'ReplicationConfiguration': {
            'Role': 'string',
            'Rules': [
                {
                    'ID': 'string',
                    'Prefix': 'string',
                    'Status': 'Enabled'|'Disabled',
                    'Destination': {
                        'Bucket': 'string',
                        'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'
                    }
                },
            ]
        }
    }
    
    
    """
    pass

def get_bucket_request_payment(Bucket=None):
    """
    Returns the request payment configuration of a bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_request_payment(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :rtype: dict
    :return: {
        'Payer': 'Requester'|'BucketOwner'
    }
    
    
    """
    pass

def get_bucket_tagging(Bucket=None):
    """
    Returns the tag set associated with the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_tagging(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :rtype: dict
    :return: {
        'TagSet': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_bucket_versioning(Bucket=None):
    """
    Returns the versioning state of a bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_versioning(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :rtype: dict
    :return: {
        'Status': 'Enabled'|'Suspended',
        'MFADelete': 'Enabled'|'Disabled'
    }
    
    
    """
    pass

def get_bucket_website(Bucket=None):
    """
    Returns the website configuration for a bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_website(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :rtype: dict
    :return: {
        'RedirectAllRequestsTo': {
            'HostName': 'string',
            'Protocol': 'http'|'https'
        },
        'IndexDocument': {
            'Suffix': 'string'
        },
        'ErrorDocument': {
            'Key': 'string'
        },
        'RoutingRules': [
            {
                'Condition': {
                    'HttpErrorCodeReturnedEquals': 'string',
                    'KeyPrefixEquals': 'string'
                },
                'Redirect': {
                    'HostName': 'string',
                    'HttpRedirectCode': 'string',
                    'Protocol': 'http'|'https',
                    'ReplaceKeyPrefixWith': 'string',
                    'ReplaceKeyWith': 'string'
                }
            },
        ]
    }
    
    
    """
    pass

def get_object(Bucket=None, IfMatch=None, IfModifiedSince=None, IfNoneMatch=None, IfUnmodifiedSince=None, Key=None, Range=None, ResponseCacheControl=None, ResponseContentDisposition=None, ResponseContentEncoding=None, ResponseContentLanguage=None, ResponseContentType=None, ResponseExpires=None, VersionId=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, RequestPayer=None, PartNumber=None):
    """
    Retrieves objects from Amazon S3.
    See also: AWS API Documentation
    
    
    :example: response = client.get_object(
        Bucket='string',
        IfMatch='string',
        IfModifiedSince=datetime(2015, 1, 1),
        IfNoneMatch='string',
        IfUnmodifiedSince=datetime(2015, 1, 1),
        Key='string',
        Range='string',
        ResponseCacheControl='string',
        ResponseContentDisposition='string',
        ResponseContentEncoding='string',
        ResponseContentLanguage='string',
        ResponseContentType='string',
        ResponseExpires=datetime(2015, 1, 1),
        VersionId='string',
        SSECustomerAlgorithm='string',
        SSECustomerKey='string',
        RequestPayer='requester',
        PartNumber=123
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type IfMatch: string
    :param IfMatch: Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).

    :type IfModifiedSince: datetime
    :param IfModifiedSince: Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).

    :type IfNoneMatch: string
    :param IfNoneMatch: Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).

    :type IfUnmodifiedSince: datetime
    :param IfUnmodifiedSince: Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).

    :type Key: string
    :param Key: [REQUIRED]

    :type Range: string
    :param Range: Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.

    :type ResponseCacheControl: string
    :param ResponseCacheControl: Sets the Cache-Control header of the response.

    :type ResponseContentDisposition: string
    :param ResponseContentDisposition: Sets the Content-Disposition header of the response

    :type ResponseContentEncoding: string
    :param ResponseContentEncoding: Sets the Content-Encoding header of the response.

    :type ResponseContentLanguage: string
    :param ResponseContentLanguage: Sets the Content-Language header of the response.

    :type ResponseContentType: string
    :param ResponseContentType: Sets the Content-Type header of the response.

    :type ResponseExpires: datetime
    :param ResponseExpires: Sets the Expires header of the response.

    :type VersionId: string
    :param VersionId: VersionId used to reference a specific version of the object.

    :type SSECustomerAlgorithm: string
    :param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (e.g., AES256).

    :type SSECustomerKey: string
    :param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side -encryption -customer-algorithm header.

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :type PartNumber: integer
    :param PartNumber: Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a 'ranged' GET request for the part specified. Useful for downloading just a part of an object.

    :rtype: dict
    :return: {
        'Body': StreamingBody(),
        'DeleteMarker': True|False,
        'AcceptRanges': 'string',
        'Expiration': 'string',
        'Restore': 'string',
        'LastModified': datetime(2015, 1, 1),
        'ContentLength': 123,
        'ETag': 'string',
        'MissingMeta': 123,
        'VersionId': 'string',
        'CacheControl': 'string',
        'ContentDisposition': 'string',
        'ContentEncoding': 'string',
        'ContentLanguage': 'string',
        'ContentRange': 'string',
        'ContentType': 'string',
        'Expires': datetime(2015, 1, 1),
        'WebsiteRedirectLocation': 'string',
        'ServerSideEncryption': 'AES256'|'aws:kms',
        'Metadata': {
            'string': 'string'
        },
        'SSECustomerAlgorithm': 'string',
        'SSECustomerKeyMD5': 'string',
        'SSEKMSKeyId': 'string',
        'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA',
        'RequestCharged': 'requester',
        'ReplicationStatus': 'COMPLETE'|'PENDING'|'FAILED'|'REPLICA',
        'PartsCount': 123,
        'TagCount': 123
    }
    
    
    :returns: 
    (dict) --
    Body (StreamingBody) -- Object data.
    DeleteMarker (boolean) -- Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If false, this response header does not appear in the response.
    AcceptRanges (string) --
    Expiration (string) -- If the object expiration is configured (see PUT Bucket lifecycle), the response includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.
    Restore (string) -- Provides information about object restoration operation and expiration time of the restored object copy.
    LastModified (datetime) -- Last modified date of the object
    ContentLength (integer) -- Size of the body in bytes.
    ETag (string) -- An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL
    MissingMeta (integer) -- This is set to the number of metadata entries not returned in x-amz-meta headers. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.
    VersionId (string) -- Version of the object.
    CacheControl (string) -- Specifies caching behavior along the request/reply chain.
    ContentDisposition (string) -- Specifies presentational information for the object.
    ContentEncoding (string) -- Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
    ContentLanguage (string) -- The language the content is in.
    ContentRange (string) -- The portion of the object returned in the response.
    ContentType (string) -- A standard MIME type describing the format of the object data.
    Expires (datetime) -- The date and time at which the object is no longer cacheable.
    WebsiteRedirectLocation (string) -- If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
    ServerSideEncryption (string) -- The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
    Metadata (dict) -- A map of metadata to store with the object in S3.
    (string) --
    (string) --
    
    
    
    
    SSECustomerAlgorithm (string) -- If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
    SSECustomerKeyMD5 (string) -- If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
    SSEKMSKeyId (string) -- If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
    StorageClass (string) --
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    ReplicationStatus (string) --
    PartsCount (integer) -- The count of parts this object has.
    TagCount (integer) -- The number of tags, if any, on the object.
    
    
    
    """
    pass

def get_object_acl(Bucket=None, Key=None, VersionId=None, RequestPayer=None):
    """
    Returns the access control list (ACL) of an object.
    See also: AWS API Documentation
    
    
    :example: response = client.get_object_acl(
        Bucket='string',
        Key='string',
        VersionId='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Key: string
    :param Key: [REQUIRED]

    :type VersionId: string
    :param VersionId: VersionId used to reference a specific version of the object.

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :rtype: dict
    :return: {
        'Owner': {
            'DisplayName': 'string',
            'ID': 'string'
        },
        'Grants': [
            {
                'Grantee': {
                    'DisplayName': 'string',
                    'EmailAddress': 'string',
                    'ID': 'string',
                    'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                    'URI': 'string'
                },
                'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
            },
        ],
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    (dict) --
    Owner (dict) --
    DisplayName (string) --
    ID (string) --
    
    
    Grants (list) -- A list of grants.
    (dict) --
    Grantee (dict) --
    DisplayName (string) -- Screen name of the grantee.
    EmailAddress (string) -- Email address of the grantee.
    ID (string) -- The canonical user ID of the grantee.
    Type (string) -- Type of grantee
    URI (string) -- URI of the grantee group.
    
    
    Permission (string) -- Specifies the permission given to the grantee.
    
    
    
    
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    
    
    
    """
    pass

def get_object_tagging(Bucket=None, Key=None, VersionId=None):
    """
    Returns the tag-set of an object.
    See also: AWS API Documentation
    
    
    :example: response = client.get_object_tagging(
        Bucket='string',
        Key='string',
        VersionId='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Key: string
    :param Key: [REQUIRED]

    :type VersionId: string
    :param VersionId: 

    :rtype: dict
    :return: {
        'VersionId': 'string',
        'TagSet': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    (dict) --
    VersionId (string) --
    TagSet (list) --
    (dict) --
    Key (string) -- Name of the tag.
    Value (string) -- Value of the tag.
    
    
    
    
    
    
    
    """
    pass

def get_object_torrent(Bucket=None, Key=None, RequestPayer=None):
    """
    Return torrent files from a bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.get_object_torrent(
        Bucket='string',
        Key='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Key: string
    :param Key: [REQUIRED]

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :rtype: dict
    :return: {
        'Body': StreamingBody(),
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    (dict) --
    Body (StreamingBody) --
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    
    
    
    """
    pass

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
    """
    pass

def get_waiter():
    """
    
    """
    pass

def head_bucket(Bucket=None):
    """
    This operation is useful to determine if a bucket exists and you have permission to access it.
    See also: AWS API Documentation
    
    
    :example: response = client.head_bucket(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    """
    pass

def head_object(Bucket=None, IfMatch=None, IfModifiedSince=None, IfNoneMatch=None, IfUnmodifiedSince=None, Key=None, Range=None, VersionId=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, RequestPayer=None, PartNumber=None):
    """
    The HEAD operation retrieves metadata from an object without returning the object itself. This operation is useful if you're only interested in an object's metadata. To use HEAD, you must have READ access to the object.
    See also: AWS API Documentation
    
    
    :example: response = client.head_object(
        Bucket='string',
        IfMatch='string',
        IfModifiedSince=datetime(2015, 1, 1),
        IfNoneMatch='string',
        IfUnmodifiedSince=datetime(2015, 1, 1),
        Key='string',
        Range='string',
        VersionId='string',
        SSECustomerAlgorithm='string',
        SSECustomerKey='string',
        RequestPayer='requester',
        PartNumber=123
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type IfMatch: string
    :param IfMatch: Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).

    :type IfModifiedSince: datetime
    :param IfModifiedSince: Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).

    :type IfNoneMatch: string
    :param IfNoneMatch: Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).

    :type IfUnmodifiedSince: datetime
    :param IfUnmodifiedSince: Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).

    :type Key: string
    :param Key: [REQUIRED]

    :type Range: string
    :param Range: Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.

    :type VersionId: string
    :param VersionId: VersionId used to reference a specific version of the object.

    :type SSECustomerAlgorithm: string
    :param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (e.g., AES256).

    :type SSECustomerKey: string
    :param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side -encryption -customer-algorithm header.

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :type PartNumber: integer
    :param PartNumber: Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a 'ranged' HEAD request for the part specified. Useful querying about the size of the part and the number of parts in this object.

    :rtype: dict
    :return: {
        'DeleteMarker': True|False,
        'AcceptRanges': 'string',
        'Expiration': 'string',
        'Restore': 'string',
        'LastModified': datetime(2015, 1, 1),
        'ContentLength': 123,
        'ETag': 'string',
        'MissingMeta': 123,
        'VersionId': 'string',
        'CacheControl': 'string',
        'ContentDisposition': 'string',
        'ContentEncoding': 'string',
        'ContentLanguage': 'string',
        'ContentType': 'string',
        'Expires': datetime(2015, 1, 1),
        'WebsiteRedirectLocation': 'string',
        'ServerSideEncryption': 'AES256'|'aws:kms',
        'Metadata': {
            'string': 'string'
        },
        'SSECustomerAlgorithm': 'string',
        'SSECustomerKeyMD5': 'string',
        'SSEKMSKeyId': 'string',
        'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA',
        'RequestCharged': 'requester',
        'ReplicationStatus': 'COMPLETE'|'PENDING'|'FAILED'|'REPLICA',
        'PartsCount': 123
    }
    
    
    :returns: 
    (dict) --
    DeleteMarker (boolean) -- Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If false, this response header does not appear in the response.
    AcceptRanges (string) --
    Expiration (string) -- If the object expiration is configured (see PUT Bucket lifecycle), the response includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.
    Restore (string) -- Provides information about object restoration operation and expiration time of the restored object copy.
    LastModified (datetime) -- Last modified date of the object
    ContentLength (integer) -- Size of the body in bytes.
    ETag (string) -- An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL
    MissingMeta (integer) -- This is set to the number of metadata entries not returned in x-amz-meta headers. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.
    VersionId (string) -- Version of the object.
    CacheControl (string) -- Specifies caching behavior along the request/reply chain.
    ContentDisposition (string) -- Specifies presentational information for the object.
    ContentEncoding (string) -- Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
    ContentLanguage (string) -- The language the content is in.
    ContentType (string) -- A standard MIME type describing the format of the object data.
    Expires (datetime) -- The date and time at which the object is no longer cacheable.
    WebsiteRedirectLocation (string) -- If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
    ServerSideEncryption (string) -- The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
    Metadata (dict) -- A map of metadata to store with the object in S3.
    (string) --
    (string) --
    
    
    
    
    SSECustomerAlgorithm (string) -- If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
    SSECustomerKeyMD5 (string) -- If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
    SSEKMSKeyId (string) -- If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
    StorageClass (string) --
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    ReplicationStatus (string) --
    PartsCount (integer) -- The count of parts this object has.
    
    
    
    """
    pass

def list_bucket_analytics_configurations(Bucket=None, ContinuationToken=None):
    """
    Lists the analytics configurations for the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.list_bucket_analytics_configurations(
        Bucket='string',
        ContinuationToken='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] The name of the bucket from which analytics configurations are retrieved.

    :type ContinuationToken: string
    :param ContinuationToken: The ContinuationToken that represents a placeholder from where this request should begin.

    :rtype: dict
    :return: {
        'IsTruncated': True|False,
        'ContinuationToken': 'string',
        'NextContinuationToken': 'string',
        'AnalyticsConfigurationList': [
            {
                'Id': 'string',
                'Filter': {
                    'Prefix': 'string',
                    'Tag': {
                        'Key': 'string',
                        'Value': 'string'
                    },
                    'And': {
                        'Prefix': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    }
                },
                'StorageClassAnalysis': {
                    'DataExport': {
                        'OutputSchemaVersion': 'V_1',
                        'Destination': {
                            'S3BucketDestination': {
                                'Format': 'CSV',
                                'BucketAccountId': 'string',
                                'Bucket': 'string',
                                'Prefix': 'string'
                            }
                        }
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    (dict) --
    IsTruncated (boolean) -- Indicates whether the returned list of analytics configurations is complete. A value of true indicates that the list is not complete and the NextContinuationToken will be provided for a subsequent request.
    ContinuationToken (string) -- The ContinuationToken that represents where this request began.
    NextContinuationToken (string) -- NextContinuationToken is sent when isTruncated is true, which indicates that there are more analytics configurations to list. The next request must include this NextContinuationToken. The token is obfuscated and is not a usable value.
    AnalyticsConfigurationList (list) -- The list of analytics configurations for a bucket.
    (dict) --
    Id (string) -- The identifier used to represent an analytics configuration.
    Filter (dict) -- The filter used to describe a set of objects for analyses. A filter must have exactly one prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be considered in any analysis.
    Prefix (string) -- The prefix to use when evaluating an analytics filter.
    Tag (dict) -- The tag to use when evaluating an analytics filter.
    Key (string) -- Name of the tag.
    Value (string) -- Value of the tag.
    
    
    And (dict) -- A conjunction (logical AND) of predicates, which is used in evaluating an analytics filter. The operator must have at least two predicates.
    Prefix (string) -- The prefix to use when evaluating an AND predicate.
    Tags (list) -- The list of tags to use when evaluating an AND predicate.
    (dict) --
    Key (string) -- Name of the tag.
    Value (string) -- Value of the tag.
    
    
    
    
    
    
    
    
    StorageClassAnalysis (dict) -- If present, it indicates that data related to access patterns will be collected and made available to analyze the tradeoffs between different storage classes.
    DataExport (dict) -- A container used to describe how data related to the storage class analysis should be exported.
    OutputSchemaVersion (string) -- The version of the output schema to use when exporting data. Must be V_1.
    Destination (dict) -- The place to store the data for an analysis.
    S3BucketDestination (dict) -- A destination signifying output to an S3 bucket.
    Format (string) -- The file format used when exporting data to Amazon S3.
    BucketAccountId (string) -- The account ID that owns the destination bucket. If no account ID is provided, the owner will not be validated prior to exporting data.
    Bucket (string) -- The Amazon resource name (ARN) of the bucket to which data is exported.
    Prefix (string) -- The prefix to use when exporting data. The exported data begins with this prefix.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def list_bucket_inventory_configurations(Bucket=None, ContinuationToken=None):
    """
    Returns a list of inventory configurations for the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.list_bucket_inventory_configurations(
        Bucket='string',
        ContinuationToken='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] The name of the bucket containing the inventory configurations to retrieve.

    :type ContinuationToken: string
    :param ContinuationToken: The marker used to continue an inventory configuration listing that has been truncated. Use the NextContinuationToken from a previously truncated list response to continue the listing. The continuation token is an opaque value that Amazon S3 understands.

    :rtype: dict
    :return: {
        'ContinuationToken': 'string',
        'InventoryConfigurationList': [
            {
                'Destination': {
                    'S3BucketDestination': {
                        'AccountId': 'string',
                        'Bucket': 'string',
                        'Format': 'CSV',
                        'Prefix': 'string'
                    }
                },
                'IsEnabled': True|False,
                'Filter': {
                    'Prefix': 'string'
                },
                'Id': 'string',
                'IncludedObjectVersions': 'All'|'Current',
                'OptionalFields': [
                    'Size'|'LastModifiedDate'|'StorageClass'|'ETag'|'IsMultipartUploaded'|'ReplicationStatus',
                ],
                'Schedule': {
                    'Frequency': 'Daily'|'Weekly'
                }
            },
        ],
        'IsTruncated': True|False,
        'NextContinuationToken': 'string'
    }
    
    
    :returns: 
    (dict) --
    ContinuationToken (string) -- If sent in the request, the marker that is used as a starting point for this inventory configuration list response.
    InventoryConfigurationList (list) -- The list of inventory configurations for a bucket.
    (dict) --
    Destination (dict) -- Contains information about where to publish the inventory results.
    S3BucketDestination (dict) -- Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where inventory results are published.
    AccountId (string) -- The ID of the account that owns the destination bucket.
    Bucket (string) -- The Amazon resource name (ARN) of the bucket where inventory results will be published.
    Format (string) -- Specifies the output format of the inventory results.
    Prefix (string) -- The prefix that is prepended to all inventory results.
    
    
    
    
    IsEnabled (boolean) -- Specifies whether the inventory is enabled or disabled.
    Filter (dict) -- Specifies an inventory filter. The inventory only includes objects that meet the filter's criteria.
    Prefix (string) -- The prefix that an object must have to be included in the inventory results.
    
    
    Id (string) -- The ID used to identify the inventory configuration.
    IncludedObjectVersions (string) -- Specifies which object version(s) to included in the inventory results.
    OptionalFields (list) -- Contains the optional fields that are included in the inventory results.
    (string) --
    
    
    Schedule (dict) -- Specifies the schedule for generating inventory results.
    Frequency (string) -- Specifies how frequently inventory results are produced.
    
    
    
    
    
    
    IsTruncated (boolean) -- Indicates whether the returned list of inventory configurations is truncated in this response. A value of true indicates that the list is truncated.
    NextContinuationToken (string) -- The marker used to continue this inventory configuration listing. Use the NextContinuationToken from this response to continue the listing in a subsequent request. The continuation token is an opaque value that Amazon S3 understands.
    
    
    
    """
    pass

def list_bucket_metrics_configurations(Bucket=None, ContinuationToken=None):
    """
    Lists the metrics configurations for the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.list_bucket_metrics_configurations(
        Bucket='string',
        ContinuationToken='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] The name of the bucket containing the metrics configurations to retrieve.

    :type ContinuationToken: string
    :param ContinuationToken: The marker that is used to continue a metrics configuration listing that has been truncated. Use the NextContinuationToken from a previously truncated list response to continue the listing. The continuation token is an opaque value that Amazon S3 understands.

    :rtype: dict
    :return: {
        'IsTruncated': True|False,
        'ContinuationToken': 'string',
        'NextContinuationToken': 'string',
        'MetricsConfigurationList': [
            {
                'Id': 'string',
                'Filter': {
                    'Prefix': 'string',
                    'Tag': {
                        'Key': 'string',
                        'Value': 'string'
                    },
                    'And': {
                        'Prefix': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    (dict) --
    IsTruncated (boolean) -- Indicates whether the returned list of metrics configurations is complete. A value of true indicates that the list is not complete and the NextContinuationToken will be provided for a subsequent request.
    ContinuationToken (string) -- The marker that is used as a starting point for this metrics configuration list response. This value is present if it was sent in the request.
    NextContinuationToken (string) -- The marker used to continue a metrics configuration listing that has been truncated. Use the NextContinuationToken from a previously truncated list response to continue the listing. The continuation token is an opaque value that Amazon S3 understands.
    MetricsConfigurationList (list) -- The list of metrics configurations for a bucket.
    (dict) --
    Id (string) -- The ID used to identify the metrics configuration.
    Filter (dict) -- Specifies a metrics configuration filter. The metrics configuration will only include objects that meet the filter's criteria. A filter must be a prefix, a tag, or a conjunction (MetricsAndOperator).
    Prefix (string) -- The prefix used when evaluating a metrics filter.
    Tag (dict) -- The tag used when evaluating a metrics filter.
    Key (string) -- Name of the tag.
    Value (string) -- Value of the tag.
    
    
    And (dict) -- A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The operator must have at least two predicates, and an object must match all of the predicates in order for the filter to apply.
    Prefix (string) -- The prefix used when evaluating an AND predicate.
    Tags (list) -- The list of tags used when evaluating an AND predicate.
    (dict) --
    Key (string) -- Name of the tag.
    Value (string) -- Value of the tag.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def list_buckets():
    """
    Returns a list of all buckets owned by the authenticated sender of the request.
    See also: AWS API Documentation
    
    
    :example: response = client.list_buckets()
    
    
    :rtype: dict
    :return: {
        'Buckets': [
            {
                'Name': 'string',
                'CreationDate': datetime(2015, 1, 1)
            },
        ],
        'Owner': {
            'DisplayName': 'string',
            'ID': 'string'
        }
    }
    
    
    """
    pass

def list_multipart_uploads(Bucket=None, Delimiter=None, EncodingType=None, KeyMarker=None, MaxUploads=None, Prefix=None, UploadIdMarker=None):
    """
    This operation lists in-progress multipart uploads.
    See also: AWS API Documentation
    
    
    :example: response = client.list_multipart_uploads(
        Bucket='string',
        Delimiter='string',
        EncodingType='url',
        KeyMarker='string',
        MaxUploads=123,
        Prefix='string',
        UploadIdMarker='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Delimiter: string
    :param Delimiter: Character you use to group keys.

    :type EncodingType: string
    :param EncodingType: Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.

    :type KeyMarker: string
    :param KeyMarker: Together with upload-id-marker, this parameter specifies the multipart upload after which listing should begin.

    :type MaxUploads: integer
    :param MaxUploads: Sets the maximum number of multipart uploads, from 1 to 1,000, to return in the response body. 1,000 is the maximum number of uploads that can be returned in a response.

    :type Prefix: string
    :param Prefix: Lists in-progress uploads only for those keys that begin with the specified prefix.

    :type UploadIdMarker: string
    :param UploadIdMarker: Together with key-marker, specifies the multipart upload after which listing should begin. If key-marker is not specified, the upload-id-marker parameter is ignored.

    :rtype: dict
    :return: {
        'Bucket': 'string',
        'KeyMarker': 'string',
        'UploadIdMarker': 'string',
        'NextKeyMarker': 'string',
        'Prefix': 'string',
        'Delimiter': 'string',
        'NextUploadIdMarker': 'string',
        'MaxUploads': 123,
        'IsTruncated': True|False,
        'Uploads': [
            {
                'UploadId': 'string',
                'Key': 'string',
                'Initiated': datetime(2015, 1, 1),
                'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA',
                'Owner': {
                    'DisplayName': 'string',
                    'ID': 'string'
                },
                'Initiator': {
                    'ID': 'string',
                    'DisplayName': 'string'
                }
            },
        ],
        'CommonPrefixes': [
            {
                'Prefix': 'string'
            },
        ],
        'EncodingType': 'url'
    }
    
    
    :returns: 
    (dict) --
    Bucket (string) -- Name of the bucket to which the multipart upload was initiated.
    KeyMarker (string) -- The key at or after which the listing began.
    UploadIdMarker (string) -- Upload ID after which listing began.
    NextKeyMarker (string) -- When a list is truncated, this element specifies the value that should be used for the key-marker request parameter in a subsequent request.
    Prefix (string) -- When a prefix is provided in the request, this field contains the specified prefix. The result contains only keys starting with the specified prefix.
    Delimiter (string) --
    NextUploadIdMarker (string) -- When a list is truncated, this element specifies the value that should be used for the upload-id-marker request parameter in a subsequent request.
    MaxUploads (integer) -- Maximum number of multipart uploads that could have been included in the response.
    IsTruncated (boolean) -- Indicates whether the returned list of multipart uploads is truncated. A value of true indicates that the list was truncated. The list can be truncated if the number of multipart uploads exceeds the limit allowed or specified by max uploads.
    Uploads (list) --
    (dict) --
    UploadId (string) -- Upload ID that identifies the multipart upload.
    Key (string) -- Key of the object for which the multipart upload was initiated.
    Initiated (datetime) -- Date and time at which the multipart upload was initiated.
    StorageClass (string) -- The class of storage used to store the object.
    Owner (dict) --
    DisplayName (string) --
    ID (string) --
    
    
    Initiator (dict) -- Identifies who initiated the multipart upload.
    ID (string) -- If the principal is an AWS account, it provides the Canonical User ID. If the principal is an IAM User, it provides a user ARN value.
    DisplayName (string) -- Name of the Principal.
    
    
    
    
    
    
    CommonPrefixes (list) --
    (dict) --
    Prefix (string) --
    
    
    
    
    EncodingType (string) -- Encoding type used by Amazon S3 to encode object keys in the response.
    
    
    
    """
    pass

def list_object_versions(Bucket=None, Delimiter=None, EncodingType=None, KeyMarker=None, MaxKeys=None, Prefix=None, VersionIdMarker=None):
    """
    Returns metadata about all of the versions of objects in a bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.list_object_versions(
        Bucket='string',
        Delimiter='string',
        EncodingType='url',
        KeyMarker='string',
        MaxKeys=123,
        Prefix='string',
        VersionIdMarker='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Delimiter: string
    :param Delimiter: A delimiter is a character you use to group keys.

    :type EncodingType: string
    :param EncodingType: Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.

    :type KeyMarker: string
    :param KeyMarker: Specifies the key to start with when listing objects in a bucket.

    :type MaxKeys: integer
    :param MaxKeys: Sets the maximum number of keys returned in the response. The response might contain fewer keys but will never contain more.

    :type Prefix: string
    :param Prefix: Limits the response to keys that begin with the specified prefix.

    :type VersionIdMarker: string
    :param VersionIdMarker: Specifies the object version you want to start listing from.

    :rtype: dict
    :return: {
        'IsTruncated': True|False,
        'KeyMarker': 'string',
        'VersionIdMarker': 'string',
        'NextKeyMarker': 'string',
        'NextVersionIdMarker': 'string',
        'Versions': [
            {
                'ETag': 'string',
                'Size': 123,
                'StorageClass': 'STANDARD',
                'Key': 'string',
                'VersionId': 'string',
                'IsLatest': True|False,
                'LastModified': datetime(2015, 1, 1),
                'Owner': {
                    'DisplayName': 'string',
                    'ID': 'string'
                }
            },
        ],
        'DeleteMarkers': [
            {
                'Owner': {
                    'DisplayName': 'string',
                    'ID': 'string'
                },
                'Key': 'string',
                'VersionId': 'string',
                'IsLatest': True|False,
                'LastModified': datetime(2015, 1, 1)
            },
        ],
        'Name': 'string',
        'Prefix': 'string',
        'Delimiter': 'string',
        'MaxKeys': 123,
        'CommonPrefixes': [
            {
                'Prefix': 'string'
            },
        ],
        'EncodingType': 'url'
    }
    
    
    :returns: 
    (dict) --
    IsTruncated (boolean) -- A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the search criteria. If your results were truncated, you can make a follow-up paginated request using the NextKeyMarker and NextVersionIdMarker response parameters as a starting place in another request to return the rest of the results.
    KeyMarker (string) -- Marks the last Key returned in a truncated response.
    VersionIdMarker (string) --
    NextKeyMarker (string) -- Use this value for the key marker request parameter in a subsequent request.
    NextVersionIdMarker (string) -- Use this value for the next version id marker parameter in a subsequent request.
    Versions (list) --
    (dict) --
    ETag (string) --
    Size (integer) -- Size in bytes of the object.
    StorageClass (string) -- The class of storage used to store the object.
    Key (string) -- The object key.
    VersionId (string) -- Version ID of an object.
    IsLatest (boolean) -- Specifies whether the object is (true) or is not (false) the latest version of an object.
    LastModified (datetime) -- Date and time the object was last modified.
    Owner (dict) --
    DisplayName (string) --
    ID (string) --
    
    
    
    
    
    
    DeleteMarkers (list) --
    (dict) --
    Owner (dict) --
    DisplayName (string) --
    ID (string) --
    
    
    Key (string) -- The object key.
    VersionId (string) -- Version ID of an object.
    IsLatest (boolean) -- Specifies whether the object is (true) or is not (false) the latest version of an object.
    LastModified (datetime) -- Date and time the object was last modified.
    
    
    
    
    Name (string) --
    Prefix (string) --
    Delimiter (string) --
    MaxKeys (integer) --
    CommonPrefixes (list) --
    (dict) --
    Prefix (string) --
    
    
    
    
    EncodingType (string) -- Encoding type used by Amazon S3 to encode object keys in the response.
    
    
    
    """
    pass

def list_objects(Bucket=None, Delimiter=None, EncodingType=None, Marker=None, MaxKeys=None, Prefix=None, RequestPayer=None):
    """
    Returns some or all (up to 1000) of the objects in a bucket. You can use the request parameters as selection criteria to return a subset of the objects in a bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.list_objects(
        Bucket='string',
        Delimiter='string',
        EncodingType='url',
        Marker='string',
        MaxKeys=123,
        Prefix='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Delimiter: string
    :param Delimiter: A delimiter is a character you use to group keys.

    :type EncodingType: string
    :param EncodingType: Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.

    :type Marker: string
    :param Marker: Specifies the key to start with when listing objects in a bucket.

    :type MaxKeys: integer
    :param MaxKeys: Sets the maximum number of keys returned in the response. The response might contain fewer keys but will never contain more.

    :type Prefix: string
    :param Prefix: Limits the response to keys that begin with the specified prefix.

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the list objects request. Bucket owners need not specify this parameter in their requests.

    :rtype: dict
    :return: {
        'IsTruncated': True|False,
        'Marker': 'string',
        'NextMarker': 'string',
        'Contents': [
            {
                'Key': 'string',
                'LastModified': datetime(2015, 1, 1),
                'ETag': 'string',
                'Size': 123,
                'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER',
                'Owner': {
                    'DisplayName': 'string',
                    'ID': 'string'
                }
            },
        ],
        'Name': 'string',
        'Prefix': 'string',
        'Delimiter': 'string',
        'MaxKeys': 123,
        'CommonPrefixes': [
            {
                'Prefix': 'string'
            },
        ],
        'EncodingType': 'url'
    }
    
    
    :returns: 
    (dict) --
    IsTruncated (boolean) -- A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the search criteria.
    Marker (string) --
    NextMarker (string) -- When response is truncated (the IsTruncated element value in the response is true), you can use the key name in this field as marker in the subsequent request to get next set of objects. Amazon S3 lists objects in alphabetical order Note: This element is returned only if you have delimiter request parameter specified. If response does not include the NextMaker and it is truncated, you can use the value of the last Key in the response as the marker in the subsequent request to get the next set of object keys.
    Contents (list) --
    (dict) --
    Key (string) --
    LastModified (datetime) --
    ETag (string) --
    Size (integer) --
    StorageClass (string) -- The class of storage used to store the object.
    Owner (dict) --
    DisplayName (string) --
    ID (string) --
    
    
    
    
    
    
    Name (string) --
    Prefix (string) --
    Delimiter (string) --
    MaxKeys (integer) --
    CommonPrefixes (list) --
    (dict) --
    Prefix (string) --
    
    
    
    
    EncodingType (string) -- Encoding type used by Amazon S3 to encode object keys in the response.
    
    
    
    """
    pass

def list_objects_v2(Bucket=None, Delimiter=None, EncodingType=None, MaxKeys=None, Prefix=None, ContinuationToken=None, FetchOwner=None, StartAfter=None, RequestPayer=None):
    """
    Returns some or all (up to 1000) of the objects in a bucket. You can use the request parameters as selection criteria to return a subset of the objects in a bucket. Note: ListObjectsV2 is the revised List Objects API and we recommend you use this revised API for new application development.
    See also: AWS API Documentation
    
    
    :example: response = client.list_objects_v2(
        Bucket='string',
        Delimiter='string',
        EncodingType='url',
        MaxKeys=123,
        Prefix='string',
        ContinuationToken='string',
        FetchOwner=True|False,
        StartAfter='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] Name of the bucket to list.

    :type Delimiter: string
    :param Delimiter: A delimiter is a character you use to group keys.

    :type EncodingType: string
    :param EncodingType: Encoding type used by Amazon S3 to encode object keys in the response.

    :type MaxKeys: integer
    :param MaxKeys: Sets the maximum number of keys returned in the response. The response might contain fewer keys but will never contain more.

    :type Prefix: string
    :param Prefix: Limits the response to keys that begin with the specified prefix.

    :type ContinuationToken: string
    :param ContinuationToken: ContinuationToken indicates Amazon S3 that the list is being continued on this bucket with a token. ContinuationToken is obfuscated and is not a real key

    :type FetchOwner: boolean
    :param FetchOwner: The owner field is not present in listV2 by default, if you want to return owner field with each key in the result then set the fetch owner field to true

    :type StartAfter: string
    :param StartAfter: StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified key. StartAfter can be any key in the bucket

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the list objects request in V2 style. Bucket owners need not specify this parameter in their requests.

    :rtype: dict
    :return: {
        'IsTruncated': True|False,
        'Contents': [
            {
                'Key': 'string',
                'LastModified': datetime(2015, 1, 1),
                'ETag': 'string',
                'Size': 123,
                'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER',
                'Owner': {
                    'DisplayName': 'string',
                    'ID': 'string'
                }
            },
        ],
        'Name': 'string',
        'Prefix': 'string',
        'Delimiter': 'string',
        'MaxKeys': 123,
        'CommonPrefixes': [
            {
                'Prefix': 'string'
            },
        ],
        'EncodingType': 'url',
        'KeyCount': 123,
        'ContinuationToken': 'string',
        'NextContinuationToken': 'string',
        'StartAfter': 'string'
    }
    
    
    :returns: 
    (dict) --
    IsTruncated (boolean) -- A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the search criteria.
    Contents (list) -- Metadata about each object returned.
    (dict) --
    Key (string) --
    LastModified (datetime) --
    ETag (string) --
    Size (integer) --
    StorageClass (string) -- The class of storage used to store the object.
    Owner (dict) --
    DisplayName (string) --
    ID (string) --
    
    
    
    
    
    
    Name (string) -- Name of the bucket to list.
    Prefix (string) -- Limits the response to keys that begin with the specified prefix.
    Delimiter (string) -- A delimiter is a character you use to group keys.
    MaxKeys (integer) -- Sets the maximum number of keys returned in the response. The response might contain fewer keys but will never contain more.
    CommonPrefixes (list) -- CommonPrefixes contains all (if there are any) keys between Prefix and the next occurrence of the string specified by delimiter
    (dict) --
    Prefix (string) --
    
    
    
    
    EncodingType (string) -- Encoding type used by Amazon S3 to encode object keys in the response.
    KeyCount (integer) -- KeyCount is the number of keys returned with this request. KeyCount will always be less than equals to MaxKeys field. Say you ask for 50 keys, your result will include less than equals 50 keys
    ContinuationToken (string) -- ContinuationToken indicates Amazon S3 that the list is being continued on this bucket with a token. ContinuationToken is obfuscated and is not a real key
    NextContinuationToken (string) -- NextContinuationToken is sent when isTruncated is true which means there are more keys in the bucket that can be listed. The next list requests to Amazon S3 can be continued with this NextContinuationToken. NextContinuationToken is obfuscated and is not a real key
    StartAfter (string) -- StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified key. StartAfter can be any key in the bucket
    
    
    
    """
    pass

def list_parts(Bucket=None, Key=None, MaxParts=None, PartNumberMarker=None, UploadId=None, RequestPayer=None):
    """
    Lists the parts that have been uploaded for a specific multipart upload.
    See also: AWS API Documentation
    
    
    :example: response = client.list_parts(
        Bucket='string',
        Key='string',
        MaxParts=123,
        PartNumberMarker=123,
        UploadId='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Key: string
    :param Key: [REQUIRED]

    :type MaxParts: integer
    :param MaxParts: Sets the maximum number of parts to return.

    :type PartNumberMarker: integer
    :param PartNumberMarker: Specifies the part after which listing should begin. Only parts with higher part numbers will be listed.

    :type UploadId: string
    :param UploadId: [REQUIRED] Upload ID identifying the multipart upload whose parts are being listed.

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :rtype: dict
    :return: {
        'AbortDate': datetime(2015, 1, 1),
        'AbortRuleId': 'string',
        'Bucket': 'string',
        'Key': 'string',
        'UploadId': 'string',
        'PartNumberMarker': 123,
        'NextPartNumberMarker': 123,
        'MaxParts': 123,
        'IsTruncated': True|False,
        'Parts': [
            {
                'PartNumber': 123,
                'LastModified': datetime(2015, 1, 1),
                'ETag': 'string',
                'Size': 123
            },
        ],
        'Initiator': {
            'ID': 'string',
            'DisplayName': 'string'
        },
        'Owner': {
            'DisplayName': 'string',
            'ID': 'string'
        },
        'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA',
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    (dict) --
    AbortDate (datetime) -- Date when multipart upload will become eligible for abort operation by lifecycle.
    AbortRuleId (string) -- Id of the lifecycle rule that makes a multipart upload eligible for abort operation.
    Bucket (string) -- Name of the bucket to which the multipart upload was initiated.
    Key (string) -- Object key for which the multipart upload was initiated.
    UploadId (string) -- Upload ID identifying the multipart upload whose parts are being listed.
    PartNumberMarker (integer) -- Part number after which listing begins.
    NextPartNumberMarker (integer) -- When a list is truncated, this element specifies the last part in the list, as well as the value to use for the part-number-marker request parameter in a subsequent request.
    MaxParts (integer) -- Maximum number of parts that were allowed in the response.
    IsTruncated (boolean) -- Indicates whether the returned list of parts is truncated.
    Parts (list) --
    (dict) --
    PartNumber (integer) -- Part number identifying the part. This is a positive integer between 1 and 10,000.
    LastModified (datetime) -- Date and time at which the part was uploaded.
    ETag (string) -- Entity tag returned when the part was uploaded.
    Size (integer) -- Size of the uploaded part data.
    
    
    
    
    Initiator (dict) -- Identifies who initiated the multipart upload.
    ID (string) -- If the principal is an AWS account, it provides the Canonical User ID. If the principal is an IAM User, it provides a user ARN value.
    DisplayName (string) -- Name of the Principal.
    
    
    Owner (dict) --
    DisplayName (string) --
    ID (string) --
    
    
    StorageClass (string) -- The class of storage used to store the object.
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    
    
    
    """
    pass

def put_bucket_accelerate_configuration(Bucket=None, AccelerateConfiguration=None):
    """
    Sets the accelerate configuration of an existing bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_accelerate_configuration(
        Bucket='string',
        AccelerateConfiguration={
            'Status': 'Enabled'|'Suspended'
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] Name of the bucket for which the accelerate configuration is set.

    :type AccelerateConfiguration: dict
    :param AccelerateConfiguration: [REQUIRED] Specifies the Accelerate Configuration you want to set for the bucket.
            Status (string) -- The accelerate configuration of the bucket.
            

    """
    pass

def put_bucket_acl(ACL=None, AccessControlPolicy=None, Bucket=None, GrantFullControl=None, GrantRead=None, GrantReadACP=None, GrantWrite=None, GrantWriteACP=None):
    """
    Sets the permissions on a bucket using access control lists (ACL).
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_acl(
        ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
        AccessControlPolicy={
            'Grants': [
                {
                    'Grantee': {
                        'DisplayName': 'string',
                        'EmailAddress': 'string',
                        'ID': 'string',
                        'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                        'URI': 'string'
                    },
                    'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                },
            ],
            'Owner': {
                'DisplayName': 'string',
                'ID': 'string'
            }
        },
        Bucket='string',
        GrantFullControl='string',
        GrantRead='string',
        GrantReadACP='string',
        GrantWrite='string',
        GrantWriteACP='string'
    )
    
    
    :type ACL: string
    :param ACL: The canned ACL to apply to the bucket.

    :type AccessControlPolicy: dict
    :param AccessControlPolicy: 
            Grants (list) -- A list of grants.
            (dict) --
            Grantee (dict) --
            DisplayName (string) -- Screen name of the grantee.
            EmailAddress (string) -- Email address of the grantee.
            ID (string) -- The canonical user ID of the grantee.
            Type (string) -- [REQUIRED] Type of grantee
            URI (string) -- URI of the grantee group.
            Permission (string) -- Specifies the permission given to the grantee.
            
            Owner (dict) --
            DisplayName (string) --
            ID (string) --
            

    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type GrantFullControl: string
    :param GrantFullControl: Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.

    :type GrantRead: string
    :param GrantRead: Allows grantee to list the objects in the bucket.

    :type GrantReadACP: string
    :param GrantReadACP: Allows grantee to read the bucket ACL.

    :type GrantWrite: string
    :param GrantWrite: Allows grantee to create, overwrite, and delete any object in the bucket.

    :type GrantWriteACP: string
    :param GrantWriteACP: Allows grantee to write the ACL for the applicable bucket.

    """
    pass

def put_bucket_analytics_configuration(Bucket=None, Id=None, AnalyticsConfiguration=None):
    """
    Sets an analytics configuration for the bucket (specified by the analytics configuration ID).
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_analytics_configuration(
        Bucket='string',
        Id='string',
        AnalyticsConfiguration={
            'Id': 'string',
            'Filter': {
                'Prefix': 'string',
                'Tag': {
                    'Key': 'string',
                    'Value': 'string'
                },
                'And': {
                    'Prefix': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                }
            },
            'StorageClassAnalysis': {
                'DataExport': {
                    'OutputSchemaVersion': 'V_1',
                    'Destination': {
                        'S3BucketDestination': {
                            'Format': 'CSV',
                            'BucketAccountId': 'string',
                            'Bucket': 'string',
                            'Prefix': 'string'
                        }
                    }
                }
            }
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] The name of the bucket to which an analytics configuration is stored.

    :type Id: string
    :param Id: [REQUIRED] The identifier used to represent an analytics configuration.

    :type AnalyticsConfiguration: dict
    :param AnalyticsConfiguration: [REQUIRED] The configuration and any analyses for the analytics filter.
            Id (string) -- [REQUIRED] The identifier used to represent an analytics configuration.
            Filter (dict) -- The filter used to describe a set of objects for analyses. A filter must have exactly one prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be considered in any analysis.
            Prefix (string) -- The prefix to use when evaluating an analytics filter.
            Tag (dict) -- The tag to use when evaluating an analytics filter.
            Key (string) -- [REQUIRED] Name of the tag.
            Value (string) -- [REQUIRED] Value of the tag.
            And (dict) -- A conjunction (logical AND) of predicates, which is used in evaluating an analytics filter. The operator must have at least two predicates.
            Prefix (string) -- The prefix to use when evaluating an AND predicate.
            Tags (list) -- The list of tags to use when evaluating an AND predicate.
            (dict) --
            Key (string) -- [REQUIRED] Name of the tag.
            Value (string) -- [REQUIRED] Value of the tag.
            
            
            StorageClassAnalysis (dict) -- [REQUIRED] If present, it indicates that data related to access patterns will be collected and made available to analyze the tradeoffs between different storage classes.
            DataExport (dict) -- A container used to describe how data related to the storage class analysis should be exported.
            OutputSchemaVersion (string) -- [REQUIRED] The version of the output schema to use when exporting data. Must be V_1.
            Destination (dict) -- [REQUIRED] The place to store the data for an analysis.
            S3BucketDestination (dict) -- [REQUIRED] A destination signifying output to an S3 bucket.
            Format (string) -- [REQUIRED] The file format used when exporting data to Amazon S3.
            BucketAccountId (string) -- The account ID that owns the destination bucket. If no account ID is provided, the owner will not be validated prior to exporting data.
            Bucket (string) -- [REQUIRED] The Amazon resource name (ARN) of the bucket to which data is exported.
            Prefix (string) -- The prefix to use when exporting data. The exported data begins with this prefix.
            
            
            

    """
    pass

def put_bucket_cors(Bucket=None, CORSConfiguration=None):
    """
    Sets the cors configuration for a bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_cors(
        Bucket='string',
        CORSConfiguration={
            'CORSRules': [
                {
                    'AllowedHeaders': [
                        'string',
                    ],
                    'AllowedMethods': [
                        'string',
                    ],
                    'AllowedOrigins': [
                        'string',
                    ],
                    'ExposeHeaders': [
                        'string',
                    ],
                    'MaxAgeSeconds': 123
                },
            ]
        },
    
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type CORSConfiguration: dict
    :param CORSConfiguration: [REQUIRED]
            CORSRules (list) -- [REQUIRED]
            (dict) --
            AllowedHeaders (list) -- Specifies which headers are allowed in a pre-flight OPTIONS request.
            (string) --
            AllowedMethods (list) -- [REQUIRED] Identifies HTTP methods that the domain/origin specified in the rule is allowed to execute.
            (string) --
            AllowedOrigins (list) -- [REQUIRED] One or more origins you want customers to be able to access the bucket from.
            (string) --
            ExposeHeaders (list) -- One or more headers in the response that you want customers to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).
            (string) --
            MaxAgeSeconds (integer) -- The time in seconds that your browser is to cache the preflight response for the specified resource.
            
            

    """
    pass

def put_bucket_inventory_configuration(Bucket=None, Id=None, InventoryConfiguration=None):
    """
    Adds an inventory configuration (identified by the inventory ID) from the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_inventory_configuration(
        Bucket='string',
        Id='string',
        InventoryConfiguration={
            'Destination': {
                'S3BucketDestination': {
                    'AccountId': 'string',
                    'Bucket': 'string',
                    'Format': 'CSV',
                    'Prefix': 'string'
                }
            },
            'IsEnabled': True|False,
            'Filter': {
                'Prefix': 'string'
            },
            'Id': 'string',
            'IncludedObjectVersions': 'All'|'Current',
            'OptionalFields': [
                'Size'|'LastModifiedDate'|'StorageClass'|'ETag'|'IsMultipartUploaded'|'ReplicationStatus',
            ],
            'Schedule': {
                'Frequency': 'Daily'|'Weekly'
            }
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] The name of the bucket where the inventory configuration will be stored.

    :type Id: string
    :param Id: [REQUIRED] The ID used to identify the inventory configuration.

    :type InventoryConfiguration: dict
    :param InventoryConfiguration: [REQUIRED] Specifies the inventory configuration.
            Destination (dict) -- [REQUIRED] Contains information about where to publish the inventory results.
            S3BucketDestination (dict) -- [REQUIRED] Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where inventory results are published.
            AccountId (string) -- The ID of the account that owns the destination bucket.
            Bucket (string) -- [REQUIRED] The Amazon resource name (ARN) of the bucket where inventory results will be published.
            Format (string) -- [REQUIRED] Specifies the output format of the inventory results.
            Prefix (string) -- The prefix that is prepended to all inventory results.
            
            IsEnabled (boolean) -- [REQUIRED] Specifies whether the inventory is enabled or disabled.
            Filter (dict) -- Specifies an inventory filter. The inventory only includes objects that meet the filter's criteria.
            Prefix (string) -- [REQUIRED] The prefix that an object must have to be included in the inventory results.
            Id (string) -- [REQUIRED] The ID used to identify the inventory configuration.
            IncludedObjectVersions (string) -- [REQUIRED] Specifies which object version(s) to included in the inventory results.
            OptionalFields (list) -- Contains the optional fields that are included in the inventory results.
            (string) --
            Schedule (dict) -- [REQUIRED] Specifies the schedule for generating inventory results.
            Frequency (string) -- [REQUIRED] Specifies how frequently inventory results are produced.
            

    """
    pass

def put_bucket_lifecycle(Bucket=None, LifecycleConfiguration=None):
    """
    Deprecated, see the PutBucketLifecycleConfiguration operation.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_lifecycle(
        Bucket='string',
        LifecycleConfiguration={
            'Rules': [
                {
                    'Expiration': {
                        'Date': datetime(2015, 1, 1),
                        'Days': 123,
                        'ExpiredObjectDeleteMarker': True|False
                    },
                    'ID': 'string',
                    'Prefix': 'string',
                    'Status': 'Enabled'|'Disabled',
                    'Transition': {
                        'Date': datetime(2015, 1, 1),
                        'Days': 123,
                        'StorageClass': 'GLACIER'|'STANDARD_IA'
                    },
                    'NoncurrentVersionTransition': {
                        'NoncurrentDays': 123,
                        'StorageClass': 'GLACIER'|'STANDARD_IA'
                    },
                    'NoncurrentVersionExpiration': {
                        'NoncurrentDays': 123
                    },
                    'AbortIncompleteMultipartUpload': {
                        'DaysAfterInitiation': 123
                    }
                },
            ]
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type LifecycleConfiguration: dict
    :param LifecycleConfiguration: 
            Rules (list) -- [REQUIRED]
            (dict) --
            Expiration (dict) --
            Date (datetime) -- Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.
            Days (integer) -- Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
            ExpiredObjectDeleteMarker (boolean) -- Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.
            ID (string) -- Unique identifier for the rule. The value cannot be longer than 255 characters.
            Prefix (string) -- [REQUIRED] Prefix identifying one or more objects to which the rule applies.
            Status (string) -- [REQUIRED] If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not currently being applied.
            Transition (dict) --
            Date (datetime) -- Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.
            Days (integer) -- Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
            StorageClass (string) -- The class of storage used to store the object.
            NoncurrentVersionTransition (dict) -- Container for the transition rule that describes when noncurrent objects transition to the STANDARD_IA or GLACIER storage class. If your bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to the STANDARD_IA or GLACIER storage class at a specific period in the object's lifetime.
            NoncurrentDays (integer) -- Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates When an Object Became Noncurrent in the Amazon Simple Storage Service Developer Guide.
            StorageClass (string) -- The class of storage used to store the object.
            NoncurrentVersionExpiration (dict) -- Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes the noncurrent object versions. You set this lifecycle configuration action on a bucket that has versioning enabled (or suspended) to request that Amazon S3 delete noncurrent object versions at a specific period in the object's lifetime.
            NoncurrentDays (integer) -- Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates When an Object Became Noncurrent in the Amazon Simple Storage Service Developer Guide.
            AbortIncompleteMultipartUpload (dict) -- Specifies the days since the initiation of an Incomplete Multipart Upload that Lifecycle will wait before permanently removing all parts of the upload.
            DaysAfterInitiation (integer) -- Indicates the number of days that must pass since initiation for Lifecycle to abort an Incomplete Multipart Upload.
            
            

    """
    pass

def put_bucket_lifecycle_configuration(Bucket=None, LifecycleConfiguration=None):
    """
    Sets lifecycle configuration for your bucket. If a lifecycle configuration exists, it replaces it.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_lifecycle_configuration(
        Bucket='string',
        LifecycleConfiguration={
            'Rules': [
                {
                    'Expiration': {
                        'Date': datetime(2015, 1, 1),
                        'Days': 123,
                        'ExpiredObjectDeleteMarker': True|False
                    },
                    'ID': 'string',
                    'Prefix': 'string',
                    'Filter': {
                        'Prefix': 'string',
                        'Tag': {
                            'Key': 'string',
                            'Value': 'string'
                        },
                        'And': {
                            'Prefix': 'string',
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        }
                    },
                    'Status': 'Enabled'|'Disabled',
                    'Transitions': [
                        {
                            'Date': datetime(2015, 1, 1),
                            'Days': 123,
                            'StorageClass': 'GLACIER'|'STANDARD_IA'
                        },
                    ],
                    'NoncurrentVersionTransitions': [
                        {
                            'NoncurrentDays': 123,
                            'StorageClass': 'GLACIER'|'STANDARD_IA'
                        },
                    ],
                    'NoncurrentVersionExpiration': {
                        'NoncurrentDays': 123
                    },
                    'AbortIncompleteMultipartUpload': {
                        'DaysAfterInitiation': 123
                    }
                },
            ]
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type LifecycleConfiguration: dict
    :param LifecycleConfiguration: 
            Rules (list) -- [REQUIRED]
            (dict) --
            Expiration (dict) --
            Date (datetime) -- Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.
            Days (integer) -- Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
            ExpiredObjectDeleteMarker (boolean) -- Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.
            ID (string) -- Unique identifier for the rule. The value cannot be longer than 255 characters.
            Prefix (string) -- Prefix identifying one or more objects to which the rule applies. This is deprecated; use Filter instead.
            Filter (dict) -- The Filter is used to identify objects that a Lifecycle Rule applies to. A Filter must have exactly one of Prefix, Tag, or And specified.
            Prefix (string) -- Prefix identifying one or more objects to which the rule applies.
            Tag (dict) -- This tag must exist in the object's tag set in order for the rule to apply.
            Key (string) -- [REQUIRED] Name of the tag.
            Value (string) -- [REQUIRED] Value of the tag.
            And (dict) -- This is used in a Lifecycle Rule Filter to apply a logical AND to two or more predicates. The Lifecycle Rule will apply to any object matching all of the predicates configured inside the And operator.
            Prefix (string) --
            Tags (list) -- All of these tags must exist in the object's tag set in order for the rule to apply.
            (dict) --
            Key (string) -- [REQUIRED] Name of the tag.
            Value (string) -- [REQUIRED] Value of the tag.
            
            
            Status (string) -- [REQUIRED] If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not currently being applied.
            Transitions (list) --
            (dict) --
            Date (datetime) -- Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.
            Days (integer) -- Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
            StorageClass (string) -- The class of storage used to store the object.
            
            NoncurrentVersionTransitions (list) --
            (dict) -- Container for the transition rule that describes when noncurrent objects transition to the STANDARD_IA or GLACIER storage class. If your bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to the STANDARD_IA or GLACIER storage class at a specific period in the object's lifetime.
            NoncurrentDays (integer) -- Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates When an Object Became Noncurrent in the Amazon Simple Storage Service Developer Guide.
            StorageClass (string) -- The class of storage used to store the object.
            
            NoncurrentVersionExpiration (dict) -- Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes the noncurrent object versions. You set this lifecycle configuration action on a bucket that has versioning enabled (or suspended) to request that Amazon S3 delete noncurrent object versions at a specific period in the object's lifetime.
            NoncurrentDays (integer) -- Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates When an Object Became Noncurrent in the Amazon Simple Storage Service Developer Guide.
            AbortIncompleteMultipartUpload (dict) -- Specifies the days since the initiation of an Incomplete Multipart Upload that Lifecycle will wait before permanently removing all parts of the upload.
            DaysAfterInitiation (integer) -- Indicates the number of days that must pass since initiation for Lifecycle to abort an Incomplete Multipart Upload.
            
            

    """
    pass

def put_bucket_logging(Bucket=None, BucketLoggingStatus=None):
    """
    Set the logging parameters for a bucket and to specify permissions for who can view and modify the logging parameters. To set the logging status of a bucket, you must be the bucket owner.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_logging(
        Bucket='string',
        BucketLoggingStatus={
            'LoggingEnabled': {
                'TargetBucket': 'string',
                'TargetGrants': [
                    {
                        'Grantee': {
                            'DisplayName': 'string',
                            'EmailAddress': 'string',
                            'ID': 'string',
                            'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                            'URI': 'string'
                        },
                        'Permission': 'FULL_CONTROL'|'READ'|'WRITE'
                    },
                ],
                'TargetPrefix': 'string'
            }
        },
    
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type BucketLoggingStatus: dict
    :param BucketLoggingStatus: [REQUIRED]
            LoggingEnabled (dict) --
            TargetBucket (string) -- Specifies the bucket where you want Amazon S3 to store server access logs. You can have your logs delivered to any bucket that you own, including the same bucket that is being logged. You can also configure multiple buckets to deliver their logs to the same target bucket. In this case you should choose a different TargetPrefix for each source bucket so that the delivered log files can be distinguished by key.
            TargetGrants (list) --
            (dict) --
            Grantee (dict) --
            DisplayName (string) -- Screen name of the grantee.
            EmailAddress (string) -- Email address of the grantee.
            ID (string) -- The canonical user ID of the grantee.
            Type (string) -- [REQUIRED] Type of grantee
            URI (string) -- URI of the grantee group.
            Permission (string) -- Logging permissions assigned to the Grantee for the bucket.
            
            TargetPrefix (string) -- This element lets you specify a prefix for the keys that the log files will be stored under.
            

    """
    pass

def put_bucket_metrics_configuration(Bucket=None, Id=None, MetricsConfiguration=None):
    """
    Sets a metrics configuration (specified by the metrics configuration ID) for the bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_metrics_configuration(
        Bucket='string',
        Id='string',
        MetricsConfiguration={
            'Id': 'string',
            'Filter': {
                'Prefix': 'string',
                'Tag': {
                    'Key': 'string',
                    'Value': 'string'
                },
                'And': {
                    'Prefix': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                }
            }
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED] The name of the bucket for which the metrics configuration is set.

    :type Id: string
    :param Id: [REQUIRED] The ID used to identify the metrics configuration.

    :type MetricsConfiguration: dict
    :param MetricsConfiguration: [REQUIRED] Specifies the metrics configuration.
            Id (string) -- [REQUIRED] The ID used to identify the metrics configuration.
            Filter (dict) -- Specifies a metrics configuration filter. The metrics configuration will only include objects that meet the filter's criteria. A filter must be a prefix, a tag, or a conjunction (MetricsAndOperator).
            Prefix (string) -- The prefix used when evaluating a metrics filter.
            Tag (dict) -- The tag used when evaluating a metrics filter.
            Key (string) -- [REQUIRED] Name of the tag.
            Value (string) -- [REQUIRED] Value of the tag.
            And (dict) -- A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The operator must have at least two predicates, and an object must match all of the predicates in order for the filter to apply.
            Prefix (string) -- The prefix used when evaluating an AND predicate.
            Tags (list) -- The list of tags used when evaluating an AND predicate.
            (dict) --
            Key (string) -- [REQUIRED] Name of the tag.
            Value (string) -- [REQUIRED] Value of the tag.
            
            
            

    """
    pass

def put_bucket_notification(Bucket=None, NotificationConfiguration=None):
    """
    Deprecated, see the PutBucketNotificationConfiguraiton operation.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_notification(
        Bucket='string',
        NotificationConfiguration={
            'TopicConfiguration': {
                'Id': 'string',
                'Events': [
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
                ],
                'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
                'Topic': 'string'
            },
            'QueueConfiguration': {
                'Id': 'string',
                'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
                'Events': [
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
                ],
                'Queue': 'string'
            },
            'CloudFunctionConfiguration': {
                'Id': 'string',
                'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
                'Events': [
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
                ],
                'CloudFunction': 'string',
                'InvocationRole': 'string'
            }
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type NotificationConfiguration: dict
    :param NotificationConfiguration: [REQUIRED]
            TopicConfiguration (dict) --
            Id (string) -- Optional unique identifier for configurations in a notification configuration. If you don't provide one, Amazon S3 will assign an ID.
            Events (list) --
            (string) -- Bucket event for which to send notifications.
            Event (string) -- Bucket event for which to send notifications.
            Topic (string) -- Amazon SNS topic to which Amazon S3 will publish a message to report the specified events for the bucket.
            QueueConfiguration (dict) --
            Id (string) -- Optional unique identifier for configurations in a notification configuration. If you don't provide one, Amazon S3 will assign an ID.
            Event (string) -- Bucket event for which to send notifications.
            Events (list) --
            (string) -- Bucket event for which to send notifications.
            Queue (string) --
            CloudFunctionConfiguration (dict) --
            Id (string) -- Optional unique identifier for configurations in a notification configuration. If you don't provide one, Amazon S3 will assign an ID.
            Event (string) -- Bucket event for which to send notifications.
            Events (list) --
            (string) -- Bucket event for which to send notifications.
            CloudFunction (string) --
            InvocationRole (string) --
            

    """
    pass

def put_bucket_notification_configuration(Bucket=None, NotificationConfiguration=None):
    """
    Enables notifications of specified events for a bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_notification_configuration(
        Bucket='string',
        NotificationConfiguration={
            'TopicConfigurations': [
                {
                    'Id': 'string',
                    'TopicArn': 'string',
                    'Events': [
                        's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
                    ],
                    'Filter': {
                        'Key': {
                            'FilterRules': [
                                {
                                    'Name': 'prefix'|'suffix',
                                    'Value': 'string'
                                },
                            ]
                        }
                    }
                },
            ],
            'QueueConfigurations': [
                {
                    'Id': 'string',
                    'QueueArn': 'string',
                    'Events': [
                        's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
                    ],
                    'Filter': {
                        'Key': {
                            'FilterRules': [
                                {
                                    'Name': 'prefix'|'suffix',
                                    'Value': 'string'
                                },
                            ]
                        }
                    }
                },
            ],
            'LambdaFunctionConfigurations': [
                {
                    'Id': 'string',
                    'LambdaFunctionArn': 'string',
                    'Events': [
                        's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated',
                    ],
                    'Filter': {
                        'Key': {
                            'FilterRules': [
                                {
                                    'Name': 'prefix'|'suffix',
                                    'Value': 'string'
                                },
                            ]
                        }
                    }
                },
            ]
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type NotificationConfiguration: dict
    :param NotificationConfiguration: [REQUIRED] Container for specifying the notification configuration of the bucket. If this element is empty, notifications are turned off on the bucket.
            TopicConfigurations (list) --
            (dict) -- Container for specifying the configuration when you want Amazon S3 to publish events to an Amazon Simple Notification Service (Amazon SNS) topic.
            Id (string) -- Optional unique identifier for configurations in a notification configuration. If you don't provide one, Amazon S3 will assign an ID.
            TopicArn (string) -- [REQUIRED] Amazon SNS topic ARN to which Amazon S3 will publish a message when it detects events of specified type.
            Events (list) -- [REQUIRED]
            (string) -- Bucket event for which to send notifications.
            Filter (dict) -- Container for object key name filtering rules. For information about key name filtering, go to Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide.
            Key (dict) -- Container for object key name prefix and suffix filtering rules.
            FilterRules (list) -- A list of containers for key value pair that defines the criteria for the filter rule.
            (dict) -- Container for key value pair that defines the criteria for the filter rule.
            Name (string) -- Object key name prefix or suffix identifying one or more objects to which the filtering rule applies. Maximum prefix length can be up to 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, go to Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide.
            Value (string) --
            
            
            
            QueueConfigurations (list) --
            (dict) -- Container for specifying an configuration when you want Amazon S3 to publish events to an Amazon Simple Queue Service (Amazon SQS) queue.
            Id (string) -- Optional unique identifier for configurations in a notification configuration. If you don't provide one, Amazon S3 will assign an ID.
            QueueArn (string) -- [REQUIRED] Amazon SQS queue ARN to which Amazon S3 will publish a message when it detects events of specified type.
            Events (list) -- [REQUIRED]
            (string) -- Bucket event for which to send notifications.
            Filter (dict) -- Container for object key name filtering rules. For information about key name filtering, go to Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide.
            Key (dict) -- Container for object key name prefix and suffix filtering rules.
            FilterRules (list) -- A list of containers for key value pair that defines the criteria for the filter rule.
            (dict) -- Container for key value pair that defines the criteria for the filter rule.
            Name (string) -- Object key name prefix or suffix identifying one or more objects to which the filtering rule applies. Maximum prefix length can be up to 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, go to Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide.
            Value (string) --
            
            
            
            LambdaFunctionConfigurations (list) --
            (dict) -- Container for specifying the AWS Lambda notification configuration.
            Id (string) -- Optional unique identifier for configurations in a notification configuration. If you don't provide one, Amazon S3 will assign an ID.
            LambdaFunctionArn (string) -- [REQUIRED] Lambda cloud function ARN that Amazon S3 can invoke when it detects events of the specified type.
            Events (list) -- [REQUIRED]
            (string) -- Bucket event for which to send notifications.
            Filter (dict) -- Container for object key name filtering rules. For information about key name filtering, go to Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide.
            Key (dict) -- Container for object key name prefix and suffix filtering rules.
            FilterRules (list) -- A list of containers for key value pair that defines the criteria for the filter rule.
            (dict) -- Container for key value pair that defines the criteria for the filter rule.
            Name (string) -- Object key name prefix or suffix identifying one or more objects to which the filtering rule applies. Maximum prefix length can be up to 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, go to Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide.
            Value (string) --
            
            
            
            

    """
    pass

def put_bucket_policy(Bucket=None, Policy=None):
    """
    Replaces a policy on a bucket. If the bucket already has a policy, the one in this request completely replaces it.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_policy(
        Bucket='string',
        Policy='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Policy: string
    :param Policy: [REQUIRED] The bucket policy as a JSON document.

    """
    pass

def put_bucket_replication(Bucket=None, ReplicationConfiguration=None):
    """
    Creates a new replication configuration (or replaces an existing one, if present).
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_replication(
        Bucket='string',
        ReplicationConfiguration={
            'Role': 'string',
            'Rules': [
                {
                    'ID': 'string',
                    'Prefix': 'string',
                    'Status': 'Enabled'|'Disabled',
                    'Destination': {
                        'Bucket': 'string',
                        'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'
                    }
                },
            ]
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type ReplicationConfiguration: dict
    :param ReplicationConfiguration: [REQUIRED] Container for replication rules. You can add as many as 1,000 rules. Total replication configuration size can be up to 2 MB.
            Role (string) -- [REQUIRED] Amazon Resource Name (ARN) of an IAM role for Amazon S3 to assume when replicating the objects.
            Rules (list) -- [REQUIRED] Container for information about a particular replication rule. Replication configuration must have at least one rule and can contain up to 1,000 rules.
            (dict) --
            ID (string) -- Unique identifier for the rule. The value cannot be longer than 255 characters.
            Prefix (string) -- [REQUIRED] Object keyname prefix identifying one or more objects to which the rule applies. Maximum prefix length can be up to 1,024 characters. Overlapping prefixes are not supported.
            Status (string) -- [REQUIRED] The rule is ignored if status is not Enabled.
            Destination (dict) -- [REQUIRED]
            Bucket (string) -- [REQUIRED] Amazon resource name (ARN) of the bucket where you want Amazon S3 to store replicas of the object identified by the rule.
            StorageClass (string) -- The class of storage used to store the object.
            
            

    """
    pass

def put_bucket_request_payment(Bucket=None, RequestPaymentConfiguration=None):
    """
    Sets the request payment configuration for a bucket. By default, the bucket owner pays for downloads from the bucket. This configuration parameter enables the bucket owner (only) to specify that the person requesting the download will be charged for the download. Documentation on requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_request_payment(
        Bucket='string',
        RequestPaymentConfiguration={
            'Payer': 'Requester'|'BucketOwner'
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type RequestPaymentConfiguration: dict
    :param RequestPaymentConfiguration: [REQUIRED]
            Payer (string) -- [REQUIRED] Specifies who pays for the download and request fees.
            

    """
    pass

def put_bucket_tagging(Bucket=None, Tagging=None):
    """
    Sets the tags for a bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_tagging(
        Bucket='string',
        Tagging={
            'TagSet': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Tagging: dict
    :param Tagging: [REQUIRED]
            TagSet (list) -- [REQUIRED]
            (dict) --
            Key (string) -- [REQUIRED] Name of the tag.
            Value (string) -- [REQUIRED] Value of the tag.
            
            

    """
    pass

def put_bucket_versioning(Bucket=None, MFA=None, VersioningConfiguration=None):
    """
    Sets the versioning state of an existing bucket. To set the versioning state, you must be the bucket owner.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_versioning(
        Bucket='string',
        MFA='string',
        VersioningConfiguration={
            'MFADelete': 'Enabled'|'Disabled',
            'Status': 'Enabled'|'Suspended'
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type MFA: string
    :param MFA: The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device.

    :type VersioningConfiguration: dict
    :param VersioningConfiguration: [REQUIRED]
            MFADelete (string) -- Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned.
            Status (string) -- The versioning state of the bucket.
            

    """
    pass

def put_bucket_website(Bucket=None, WebsiteConfiguration=None):
    """
    Set the website configuration for a bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_website(
        Bucket='string',
        WebsiteConfiguration={
            'ErrorDocument': {
                'Key': 'string'
            },
            'IndexDocument': {
                'Suffix': 'string'
            },
            'RedirectAllRequestsTo': {
                'HostName': 'string',
                'Protocol': 'http'|'https'
            },
            'RoutingRules': [
                {
                    'Condition': {
                        'HttpErrorCodeReturnedEquals': 'string',
                        'KeyPrefixEquals': 'string'
                    },
                    'Redirect': {
                        'HostName': 'string',
                        'HttpRedirectCode': 'string',
                        'Protocol': 'http'|'https',
                        'ReplaceKeyPrefixWith': 'string',
                        'ReplaceKeyWith': 'string'
                    }
                },
            ]
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type WebsiteConfiguration: dict
    :param WebsiteConfiguration: [REQUIRED]
            ErrorDocument (dict) --
            Key (string) -- [REQUIRED] The object key name to use when a 4XX class error occurs.
            IndexDocument (dict) --
            Suffix (string) -- [REQUIRED] A suffix that is appended to a request that is for a directory on the website endpoint (e.g. if the suffix is index.html and you make a request to samplebucket/images/ the data that is returned will be for the object with the key name images/index.html) The suffix must not be empty and must not include a slash character.
            RedirectAllRequestsTo (dict) --
            HostName (string) -- [REQUIRED] Name of the host where requests will be redirected.
            Protocol (string) -- Protocol to use (http, https) when redirecting requests. The default is the protocol that is used in the original request.
            RoutingRules (list) --
            (dict) --
            Condition (dict) -- A container for describing a condition that must be met for the specified redirect to apply. For example, 1. If request is for pages in the /docs folder, redirect to the /documents folder. 2. If request results in HTTP error 4xx, redirect request to another host where you might process the error.
            HttpErrorCodeReturnedEquals (string) -- The HTTP error code when the redirect is applied. In the event of an error, if the error code equals this value, then the specified redirect is applied. Required when parent element Condition is specified and sibling KeyPrefixEquals is not specified. If both are specified, then both must be true for the redirect to be applied.
            KeyPrefixEquals (string) -- The object key name prefix when the redirect is applied. For example, to redirect requests for ExamplePage.html, the key prefix will be ExamplePage.html. To redirect request for all pages with the prefix docs/, the key prefix will be /docs, which identifies all objects in the docs/ folder. Required when the parent element Condition is specified and sibling HttpErrorCodeReturnedEquals is not specified. If both conditions are specified, both must be true for the redirect to be applied.
            Redirect (dict) -- [REQUIRED] Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can can specify a different error code to return.
            HostName (string) -- The host name to use in the redirect request.
            HttpRedirectCode (string) -- The HTTP redirect code to use on the response. Not required if one of the siblings is present.
            Protocol (string) -- Protocol to use (http, https) when redirecting requests. The default is the protocol that is used in the original request.
            ReplaceKeyPrefixWith (string) -- The object key prefix to use in the redirect request. For example, to redirect requests for all pages with prefix docs/ (objects in the docs/ folder) to documents/, you can set a condition block with KeyPrefixEquals set to docs/ and in the Redirect set ReplaceKeyPrefixWith to /documents. Not required if one of the siblings is present. Can be present only if ReplaceKeyWith is not provided.
            ReplaceKeyWith (string) -- The specific object key to use in the redirect request. For example, redirect request to error.html. Not required if one of the sibling is present. Can be present only if ReplaceKeyPrefixWith is not provided.
            
            

    """
    pass

def put_object(ACL=None, Body=None, Bucket=None, CacheControl=None, ContentDisposition=None, ContentEncoding=None, ContentLanguage=None, ContentLength=None, ContentMD5=None, ContentType=None, Expires=None, GrantFullControl=None, GrantRead=None, GrantReadACP=None, GrantWriteACP=None, Key=None, Metadata=None, ServerSideEncryption=None, StorageClass=None, WebsiteRedirectLocation=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, SSEKMSKeyId=None, RequestPayer=None, Tagging=None):
    """
    Adds an object to a bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.put_object(
        ACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'|'bucket-owner-read'|'bucket-owner-full-control',
        Body=b'bytes'|file,
        Bucket='string',
        CacheControl='string',
        ContentDisposition='string',
        ContentEncoding='string',
        ContentLanguage='string',
        ContentLength=123,
        ContentMD5='string',
        ContentType='string',
        Expires=datetime(2015, 1, 1),
        GrantFullControl='string',
        GrantRead='string',
        GrantReadACP='string',
        GrantWriteACP='string',
        Key='string',
        Metadata={
            'string': 'string'
        },
        ServerSideEncryption='AES256'|'aws:kms',
        StorageClass='STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA',
        WebsiteRedirectLocation='string',
        SSECustomerAlgorithm='string',
        SSECustomerKey='string',
        SSEKMSKeyId='string',
        RequestPayer='requester',
        Tagging='string'
    )
    
    
    :type ACL: string
    :param ACL: The canned ACL to apply to the object.

    :type Body: bytes or seekable file-like object
    :param Body: Object data.

    :type Bucket: string
    :param Bucket: [REQUIRED] Name of the bucket to which the PUT operation was initiated.

    :type CacheControl: string
    :param CacheControl: Specifies caching behavior along the request/reply chain.

    :type ContentDisposition: string
    :param ContentDisposition: Specifies presentational information for the object.

    :type ContentEncoding: string
    :param ContentEncoding: Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

    :type ContentLanguage: string
    :param ContentLanguage: The language the content is in.

    :type ContentLength: integer
    :param ContentLength: Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically.

    :type ContentMD5: string
    :param ContentMD5: The base64-encoded 128-bit MD5 digest of the part data.

    :type ContentType: string
    :param ContentType: A standard MIME type describing the format of the object data.

    :type Expires: datetime
    :param Expires: The date and time at which the object is no longer cacheable.

    :type GrantFullControl: string
    :param GrantFullControl: Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.

    :type GrantRead: string
    :param GrantRead: Allows grantee to read the object data and its metadata.

    :type GrantReadACP: string
    :param GrantReadACP: Allows grantee to read the object ACL.

    :type GrantWriteACP: string
    :param GrantWriteACP: Allows grantee to write the ACL for the applicable object.

    :type Key: string
    :param Key: [REQUIRED] Object key for which the PUT operation was initiated.

    :type Metadata: dict
    :param Metadata: A map of metadata to store with the object in S3.
            (string) --
            (string) --
            

    :type ServerSideEncryption: string
    :param ServerSideEncryption: The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).

    :type StorageClass: string
    :param StorageClass: The type of storage to use for the object. Defaults to 'STANDARD'.

    :type WebsiteRedirectLocation: string
    :param WebsiteRedirectLocation: If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.

    :type SSECustomerAlgorithm: string
    :param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (e.g., AES256).

    :type SSECustomerKey: string
    :param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side -encryption -customer-algorithm header.

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required

    :type SSEKMSKeyId: string
    :param SSEKMSKeyId: Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :type Tagging: string
    :param Tagging: The tag-set for the object. The tag-set must be encoded as URL Query parameters

    :rtype: dict
    :return: {
        'Expiration': 'string',
        'ETag': 'string',
        'ServerSideEncryption': 'AES256'|'aws:kms',
        'VersionId': 'string',
        'SSECustomerAlgorithm': 'string',
        'SSECustomerKeyMD5': 'string',
        'SSEKMSKeyId': 'string',
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    (dict) --
    Expiration (string) -- If the object expiration is configured, this will contain the expiration date (expiry-date) and rule ID (rule-id). The value of rule-id is URL encoded.
    ETag (string) -- Entity tag for the uploaded object.
    ServerSideEncryption (string) -- The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
    VersionId (string) -- Version of the object.
    SSECustomerAlgorithm (string) -- If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
    SSECustomerKeyMD5 (string) -- If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
    SSEKMSKeyId (string) -- If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    
    
    
    """
    pass

def put_object_acl(ACL=None, AccessControlPolicy=None, Bucket=None, GrantFullControl=None, GrantRead=None, GrantReadACP=None, GrantWrite=None, GrantWriteACP=None, Key=None, RequestPayer=None, VersionId=None):
    """
    uses the acl subresource to set the access control list (ACL) permissions for an object that already exists in a bucket
    See also: AWS API Documentation
    
    
    :example: response = client.put_object_acl(
        ACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'|'bucket-owner-read'|'bucket-owner-full-control',
        AccessControlPolicy={
            'Grants': [
                {
                    'Grantee': {
                        'DisplayName': 'string',
                        'EmailAddress': 'string',
                        'ID': 'string',
                        'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                        'URI': 'string'
                    },
                    'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                },
            ],
            'Owner': {
                'DisplayName': 'string',
                'ID': 'string'
            }
        },
        Bucket='string',
        GrantFullControl='string',
        GrantRead='string',
        GrantReadACP='string',
        GrantWrite='string',
        GrantWriteACP='string',
        Key='string',
        RequestPayer='requester',
        VersionId='string'
    )
    
    
    :type ACL: string
    :param ACL: The canned ACL to apply to the object.

    :type AccessControlPolicy: dict
    :param AccessControlPolicy: 
            Grants (list) -- A list of grants.
            (dict) --
            Grantee (dict) --
            DisplayName (string) -- Screen name of the grantee.
            EmailAddress (string) -- Email address of the grantee.
            ID (string) -- The canonical user ID of the grantee.
            Type (string) -- [REQUIRED] Type of grantee
            URI (string) -- URI of the grantee group.
            Permission (string) -- Specifies the permission given to the grantee.
            
            Owner (dict) --
            DisplayName (string) --
            ID (string) --
            

    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type GrantFullControl: string
    :param GrantFullControl: Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.

    :type GrantRead: string
    :param GrantRead: Allows grantee to list the objects in the bucket.

    :type GrantReadACP: string
    :param GrantReadACP: Allows grantee to read the bucket ACL.

    :type GrantWrite: string
    :param GrantWrite: Allows grantee to create, overwrite, and delete any object in the bucket.

    :type GrantWriteACP: string
    :param GrantWriteACP: Allows grantee to write the ACL for the applicable bucket.

    :type Key: string
    :param Key: [REQUIRED]

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :type VersionId: string
    :param VersionId: VersionId used to reference a specific version of the object.

    :rtype: dict
    :return: {
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    (dict) --
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    
    
    
    """
    pass

def put_object_tagging(Bucket=None, Key=None, VersionId=None, ContentMD5=None, Tagging=None):
    """
    Sets the supplied tag-set to an object that already exists in a bucket
    See also: AWS API Documentation
    
    
    :example: response = client.put_object_tagging(
        Bucket='string',
        Key='string',
        VersionId='string',
        ContentMD5='string',
        Tagging={
            'TagSet': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Key: string
    :param Key: [REQUIRED]

    :type VersionId: string
    :param VersionId: 

    :type ContentMD5: string
    :param ContentMD5: 

    :type Tagging: dict
    :param Tagging: [REQUIRED]
            TagSet (list) -- [REQUIRED]
            (dict) --
            Key (string) -- [REQUIRED] Name of the tag.
            Value (string) -- [REQUIRED] Value of the tag.
            
            

    :rtype: dict
    :return: {
        'VersionId': 'string'
    }
    
    
    :returns: 
    (dict) --
    VersionId (string) --
    
    
    
    """
    pass

def restore_object(Bucket=None, Key=None, VersionId=None, RestoreRequest=None, RequestPayer=None):
    """
    Restores an archived copy of an object back into Amazon S3
    See also: AWS API Documentation
    
    
    :example: response = client.restore_object(
        Bucket='string',
        Key='string',
        VersionId='string',
        RestoreRequest={
            'Days': 123,
            'GlacierJobParameters': {
                'Tier': 'Standard'|'Bulk'|'Expedited'
            }
        },
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type Key: string
    :param Key: [REQUIRED]

    :type VersionId: string
    :param VersionId: 

    :type RestoreRequest: dict
    :param RestoreRequest: 
            Days (integer) -- [REQUIRED] Lifetime of the active copy in days
            GlacierJobParameters (dict) -- Glacier related prameters pertaining to this job.
            Tier (string) -- [REQUIRED] Glacier retrieval tier at which the restore will be processed.
            

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :rtype: dict
    :return: {
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    (dict) --
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    
    
    
    """
    pass

def upload_file():
    """
    Upload a file to an S3 object.
    :
    Similar behavior as S3Transfer's upload_file() method,
    except that parameters are capitalized. Detailed examples can be found at
    S3Transfer's .
    
    :example: import boto3
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')
    
    
    """
    pass

def upload_fileobj(Fileobj=None, Bucket=None, Key=None, ExtraArgs=None, Callback=None, Config=None):
    """
    Upload a file-like object to S3.
    The file-like object must be in binary mode.
    This is a managed transfer which will perform a multipart upload in
    multiple threads if necessary.
    :
    
    :example: import boto3
    s3 = boto3.client('s3')
    
    with open('filename', 'rb') as data:
        s3.upload_fileobj(data, 'mybucket', 'mykey')
    
    
    :type Fileobj: a file-like object
    :param Fileobj: A file-like object to upload. At a minimum, it must
            implement the read method, and must return bytes.

    :type Bucket: str
    :param Bucket: The name of the bucket to upload to.

    :type Key: str
    :param Key: The name of the key to upload to.

    :type ExtraArgs: dict
    :param ExtraArgs: Extra arguments that may be passed to the
            client operation.

    :type Callback: method
    :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the upload.

    :type Config: boto3.s3.transfer.TransferConfig
    :param Config: The transfer configuration to be used when performing the
            upload.

    """
    pass

def upload_part(Body=None, Bucket=None, ContentLength=None, ContentMD5=None, Key=None, PartNumber=None, UploadId=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, RequestPayer=None):
    """
    Uploads a part in a multipart upload.
    Note: After you initiate multipart upload and upload one or more parts, you must either complete or abort multipart upload in order to stop getting charged for storage of the uploaded parts. Only after you either complete or abort multipart upload, Amazon S3 frees up the parts storage and stops charging you for the parts storage.
    See also: AWS API Documentation
    
    
    :example: response = client.upload_part(
        Body=b'bytes'|file,
        Bucket='string',
        ContentLength=123,
        ContentMD5='string',
        Key='string',
        PartNumber=123,
        UploadId='string',
        SSECustomerAlgorithm='string',
        SSECustomerKey='string',
        RequestPayer='requester'
    )
    
    
    :type Body: bytes or seekable file-like object
    :param Body: Object data.

    :type Bucket: string
    :param Bucket: [REQUIRED] Name of the bucket to which the multipart upload was initiated.

    :type ContentLength: integer
    :param ContentLength: Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically.

    :type ContentMD5: string
    :param ContentMD5: The base64-encoded 128-bit MD5 digest of the part data.

    :type Key: string
    :param Key: [REQUIRED] Object key for which the multipart upload was initiated.

    :type PartNumber: integer
    :param PartNumber: [REQUIRED] Part number of part being uploaded. This is a positive integer between 1 and 10,000.

    :type UploadId: string
    :param UploadId: [REQUIRED] Upload ID identifying the multipart upload whose part is being uploaded.

    :type SSECustomerAlgorithm: string
    :param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (e.g., AES256).

    :type SSECustomerKey: string
    :param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side -encryption -customer-algorithm header. This must be the same encryption key specified in the initiate multipart upload request.

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :rtype: dict
    :return: {
        'ServerSideEncryption': 'AES256'|'aws:kms',
        'ETag': 'string',
        'SSECustomerAlgorithm': 'string',
        'SSECustomerKeyMD5': 'string',
        'SSEKMSKeyId': 'string',
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    (dict) --
    ServerSideEncryption (string) -- The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
    ETag (string) -- Entity tag for the uploaded object.
    SSECustomerAlgorithm (string) -- If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
    SSECustomerKeyMD5 (string) -- If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
    SSEKMSKeyId (string) -- If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    
    
    
    """
    pass

def upload_part_copy(Bucket=None, CopySource=None, CopySourceIfMatch=None, CopySourceIfModifiedSince=None, CopySourceIfNoneMatch=None, CopySourceIfUnmodifiedSince=None, CopySourceRange=None, Key=None, PartNumber=None, UploadId=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, CopySourceSSECustomerAlgorithm=None, CopySourceSSECustomerKey=None, CopySourceSSECustomerKeyMD5=None, RequestPayer=None):
    """
    Uploads a part by copying data from an existing object as data source.
    See also: AWS API Documentation
    
    
    :example: response = client.upload_part_copy(
        Bucket='string',
        CopySource='string' or {'Bucket': 'string', 'Key': 'string', 'VersionId': 'string'},
        CopySourceIfMatch='string',
        CopySourceIfModifiedSince=datetime(2015, 1, 1),
        CopySourceIfNoneMatch='string',
        CopySourceIfUnmodifiedSince=datetime(2015, 1, 1),
        CopySourceRange='string',
        Key='string',
        PartNumber=123,
        UploadId='string',
        SSECustomerAlgorithm='string',
        SSECustomerKey='string',
        CopySourceSSECustomerAlgorithm='string',
        CopySourceSSECustomerKey='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]

    :type CopySource: str or dict
    :param CopySource: [REQUIRED] The name of the source bucket, key name of the source object, and optional version ID of the source object. You can either provide this value as a string or a dictionary. The string form is {bucket}/{key} or {bucket}/{key}?versionId={versionId} if you want to copy a specific version. You can also provide this value as a dictionary. The dictionary format is recommended over the string format because it is more explicit. The dictionary format is: {'Bucket': 'bucket', 'Key': 'key', 'VersionId': 'id'}. Note that the VersionId key is optional and may be omitted.

    :type CopySourceIfMatch: string
    :param CopySourceIfMatch: Copies the object if its entity tag (ETag) matches the specified tag.

    :type CopySourceIfModifiedSince: datetime
    :param CopySourceIfModifiedSince: Copies the object if it has been modified since the specified time.

    :type CopySourceIfNoneMatch: string
    :param CopySourceIfNoneMatch: Copies the object if its entity tag (ETag) is different than the specified ETag.

    :type CopySourceIfUnmodifiedSince: datetime
    :param CopySourceIfUnmodifiedSince: Copies the object if it hasn't been modified since the specified time.

    :type CopySourceRange: string
    :param CopySourceRange: The range of bytes to copy from the source object. The range value must use the form bytes=first-last, where the first and last are the zero-based byte offsets to copy. For example, bytes=0-9 indicates that you want to copy the first ten bytes of the source. You can copy a range only if the source object is greater than 5 GB.

    :type Key: string
    :param Key: [REQUIRED]

    :type PartNumber: integer
    :param PartNumber: [REQUIRED] Part number of part being copied. This is a positive integer between 1 and 10,000.

    :type UploadId: string
    :param UploadId: [REQUIRED] Upload ID identifying the multipart upload whose part is being copied.

    :type SSECustomerAlgorithm: string
    :param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (e.g., AES256).

    :type SSECustomerKey: string
    :param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side -encryption -customer-algorithm header. This must be the same encryption key specified in the initiate multipart upload request.

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required

    :type CopySourceSSECustomerAlgorithm: string
    :param CopySourceSSECustomerAlgorithm: Specifies the algorithm to use when decrypting the source object (e.g., AES256).

    :type CopySourceSSECustomerKey: string
    :param CopySourceSSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.

    :type CopySourceSSECustomerKeyMD5: string
    :param CopySourceSSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

    :rtype: dict
    :return: {
        'CopySourceVersionId': 'string',
        'CopyPartResult': {
            'ETag': 'string',
            'LastModified': datetime(2015, 1, 1)
        },
        'ServerSideEncryption': 'AES256'|'aws:kms',
        'SSECustomerAlgorithm': 'string',
        'SSECustomerKeyMD5': 'string',
        'SSEKMSKeyId': 'string',
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    (dict) --
    CopySourceVersionId (string) -- The version of the source object that was copied, if you have enabled versioning on the source bucket.
    CopyPartResult (dict) --
    ETag (string) -- Entity tag of the object.
    LastModified (datetime) -- Date and time at which the object was uploaded.
    
    
    ServerSideEncryption (string) -- The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
    SSECustomerAlgorithm (string) -- If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
    SSECustomerKeyMD5 (string) -- If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
    SSEKMSKeyId (string) -- If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
    RequestCharged (string) -- If present, indicates that the requester was successfully charged for the request.
    
    
    
    """
    pass

