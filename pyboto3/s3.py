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
    This operation aborts a multipart upload. After a multipart upload is aborted, no additional parts can be uploaded using that upload ID. The storage consumed by any previously uploaded parts will be freed. However, if any part uploads are currently in progress, those part uploads might or might not succeed. As a result, it might be necessary to abort a given multipart upload multiple times in order to completely free all storage consumed by all parts.
    To verify that all parts have been removed, so you don\'t get charged for the part storage, you should call the  ListParts operation and ensure that the parts list is empty.
    For information about permissions required to use the multipart upload API, see Multipart Upload API and Permissions .
    The following operations are related to AbortMultipartUpload :
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example aborts a multipart upload.
    Expected Output:
    
    :example: response = client.abort_multipart_upload(
        Bucket='string',
        Key='string',
        UploadId='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name to which the upload was taking place.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Key: string
    :param Key: [REQUIRED]\nKey of the object for which the multipart upload was initiated.\n

    :type UploadId: string
    :param UploadId: [REQUIRED]\nUpload ID that identifies the multipart upload.\n

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestCharged': 'requester'
}


Response Structure

(dict) --

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.







Exceptions

S3.Client.exceptions.NoSuchUpload

Examples
The following example aborts a multipart upload.
response = client.abort_multipart_upload(
    Bucket='examplebucket',
    Key='bigobject',
    UploadId='xadcOB_7YPBOJuoFiQ9cz4P3Pe6FIZwO4f7wN93uHsNBEw97pl5eNwzExg0LAT2dUN91cOmrEQHDsP3WA60CEg--',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    Bucket (string) -- [REQUIRED]
    The bucket name to which the upload was taking place.
    When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
    
    Key (string) -- [REQUIRED]
    Key of the object for which the multipart upload was initiated.
    
    UploadId (string) -- [REQUIRED]
    Upload ID that identifies the multipart upload.
    
    RequestPayer (string) -- Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def complete_multipart_upload(Bucket=None, Key=None, MultipartUpload=None, UploadId=None, RequestPayer=None):
    """
    Completes a multipart upload by assembling previously uploaded parts.
    You first initiate the multipart upload and then upload all parts using the  UploadPart operation. After successfully uploading all relevant parts of an upload, you call this operation to complete the upload. Upon receiving this request, Amazon S3 concatenates all the parts in ascending order by part number to create a new object. In the Complete Multipart Upload request, you must provide the parts list. You must ensure that the parts list is complete. This operation concatenates the parts that you provide in the list. For each part in the list, you must provide the part number and the ETag value, returned after that part was uploaded.
    Processing of a Complete Multipart Upload request could take several minutes to complete. After Amazon S3 begins processing the request, it sends an HTTP response header that specifies a 200 OK response. While processing is in progress, Amazon S3 periodically sends white space characters to keep the connection from timing out. Because a request could fail after the initial 200 OK response has been sent, it is important that you check the response body to determine whether the request succeeded.
    Note that if CompleteMultipartUpload fails, applications should be prepared to retry the failed requests. For more information, see Amazon S3 Error Best Practices .
    For more information about multipart uploads, see Uploading Objects Using Multipart Upload .
    For information about permissions required to use the multipart upload API, see Multipart Upload API and Permissions .
    The following operations are related to CompleteMultipartUpload :
    See also: AWS API Documentation
    
    Examples
    The following example completes a multipart upload.
    Expected Output:
    
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
    :param Bucket: [REQUIRED]\nName of the bucket to which the multipart upload was initiated.\n

    :type Key: string
    :param Key: [REQUIRED]\nObject key for which the multipart upload was initiated.\n

    :type MultipartUpload: dict
    :param MultipartUpload: The container for the multipart upload request information.\n\nParts (list) --Array of CompletedPart data types.\n\n(dict) --Details of the parts that were uploaded.\n\nETag (string) --Entity tag returned when the part was uploaded.\n\nPartNumber (integer) --Part number that identifies the part. This is a positive integer between 1 and 10,000.\n\n\n\n\n\n\n

    :type UploadId: string
    :param UploadId: [REQUIRED]\nID for the initiated multipart upload.\n

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Location (string) --
The URI that identifies the newly created object.

Bucket (string) --
The name of the bucket that contains the newly created object.

Key (string) --
The object key of the newly created object.

Expiration (string) --
If the object expiration is configured, this will contain the expiration date (expiry-date) and rule ID (rule-id). The value of rule-id is URL encoded.

ETag (string) --
Entity tag that identifies the newly created object\'s data. Objects with different object data will have different entity tags. The entity tag is an opaque string. The entity tag may or may not be an MD5 digest of the object data. If the entity tag is not an MD5 digest of the object data, it will contain one or more nonhexadecimal characters and/or will consist of less than 32 or more than 32 hexadecimal digits.

ServerSideEncryption (string) --
If you specified server-side encryption either with an Amazon S3-managed encryption key or an AWS KMS customer master key (CMK) in your initiate multipart upload request, the response includes this header. It confirms the encryption algorithm that Amazon S3 used to encrypt the object.

VersionId (string) --
Version ID of the newly created object, in case the bucket has versioning turned on.

SSEKMSKeyId (string) --
If present, specifies the ID of the AWS Key Management Service (AWS KMS) symmetric customer managed customer master key (CMK) that was used for the object.

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.







Examples
The following example completes a multipart upload.
response = client.complete_multipart_upload(
    Bucket='examplebucket',
    Key='bigobject',
    MultipartUpload={
        'Parts': [
            {
                'ETag': '"d8c2eafd90c266e19ab9dcacc479f8af"',
                'PartNumber': '1',
            },
            {
                'ETag': '"d8c2eafd90c266e19ab9dcacc479f8af"',
                'PartNumber': '2',
            },
        ],
    },
    UploadId='7YPBOJuoFiQ9cz4P3Pe6FIZwO4f7wN93uHsNBEw97pl5eNwzExg0LAT2dUN91cOmrEQHDsP3WA60CEg--',
)

print(response)


Expected Output:
{
    'Bucket': 'acexamplebucket',
    'ETag': '"4d9031c7644d8081c2829f4ea23c55f7-2"',
    'Key': 'bigobject',
    'Location': 'https://examplebucket.s3.amazonaws.com/bigobject',
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    CreateMultipartUpload
    UploadPart
    AbortMultipartUpload
    ListParts
    ListMultipartUploads
    
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
    :param CopySource: The name of the source bucket, key name of the\nsource object, and optional version ID of the source object. The\ndictionary format is:\n{\'Bucket\': \'bucket\', \'Key\': \'key\', \'VersionId\': \'id\'}. Note\nthat the VersionId key is optional and may be omitted.

    :type Bucket: str
    :param Bucket: The name of the bucket to copy to

    :type Key: str
    :param Key: The name of the key to copy to

    :type ExtraArgs: dict
    :param ExtraArgs: Extra arguments that may be passed to the\nclient operation

    :type Callback: function
    :param Callback: A method which takes a number of bytes transferred to\nbe periodically called during the copy.

    :type SourceClient: botocore or boto3 Client
    :param SourceClient: The client to be used for operation that\nmay happen at the source object. For example, this client is\nused for the head_object that determines the size of the copy.\nIf no client is provided, the current client is used as the client\nfor the source object.

    :type Config: boto3.s3.transfer.TransferConfig
    :param Config: The transfer configuration to be used when performing the\ncopy.

    """
    pass

def copy_object(ACL=None, Bucket=None, CacheControl=None, ContentDisposition=None, ContentEncoding=None, ContentLanguage=None, ContentType=None, CopySource=None, CopySourceIfMatch=None, CopySourceIfModifiedSince=None, CopySourceIfNoneMatch=None, CopySourceIfUnmodifiedSince=None, Expires=None, GrantFullControl=None, GrantRead=None, GrantReadACP=None, GrantWriteACP=None, Key=None, Metadata=None, MetadataDirective=None, TaggingDirective=None, ServerSideEncryption=None, StorageClass=None, WebsiteRedirectLocation=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, SSEKMSKeyId=None, SSEKMSEncryptionContext=None, CopySourceSSECustomerAlgorithm=None, CopySourceSSECustomerKey=None, CopySourceSSECustomerKeyMD5=None, RequestPayer=None, Tagging=None, ObjectLockMode=None, ObjectLockRetainUntilDate=None, ObjectLockLegalHoldStatus=None):
    """
    Creates a copy of an object that is already stored in Amazon S3.
    All copy requests must be authenticated. Additionally, you must have read access to the source object and write access to the destination bucket. For more information, see REST Authentication . Both the Region that you want to copy the object from and the Region that you want to copy the object to must be enabled for your account.
    A copy request might return an error when Amazon S3 receives the copy request or while Amazon S3 is copying the files. If the error occurs before the copy operation starts, you receive a standard Amazon S3 error. If the error occurs during the copy operation, the error response is embedded in the 200 OK response. This means that a 200 OK response can contain either a success or an error. Design your application to parse the contents of the response and handle it appropriately.
    If the copy is successful, you receive a response with information about the copied object.
    The copy request charge is based on the storage class and Region that you specify for the destination object. For pricing information, see Amazon S3 pricing .
    When copying an object, you can preserve all metadata (default) or specify new metadata. However, the ACL is not preserved and is set to private for the user making the request. To override the default ACL setting, specify a new ACL when generating a copy request. For more information, see Using ACLs .
    To specify whether you want the object metadata copied from the source object or replaced with metadata provided in the request, you can optionally add the x-amz-metadata-directive header. When you grant permissions, you can use the s3:x-amz-metadata-directive condition key to enforce certain metadata behavior when objects are uploaded. For more information, see Specifying Conditions in a Policy in the Amazon S3 Developer Guide . For a complete list of Amazon S3-specific condition keys, see Actions, Resources, and Condition Keys for Amazon S3 .
    To only copy an object under certain conditions, such as whether the Etag matches or whether the object was modified before or after a specified date, use the following request parameters:
    If both the x-amz-copy-source-if-match and x-amz-copy-source-if-unmodified-since headers are present in the request and evaluate as follows, Amazon S3 returns 200 OK and copies the data:
    If both the x-amz-copy-source-if-none-match and x-amz-copy-source-if-modified-since headers are present in the request and evaluate as follows, Amazon S3 returns the 412 Precondition Failed response code:
    The source object that you are copying can be encrypted or unencrypted. The source object can be encrypted with server-side encryption using AWS managed encryption keys (SSE-S3 or SSE-KMS) or by using a customer-provided encryption key. With server-side encryption, Amazon S3 encrypts your data as it writes it to disks in its data centers and decrypts the data when you access it.
    You can optionally use the appropriate encryption-related headers to request server-side encryption for the target object. You have the option to provide your own encryption key or use SSE-S3 or SSE-KMS, regardless of the form of server-side encryption that was used to encrypt the source object. You can even request encryption if the source object was not encrypted. For more information about server-side encryption, see Using Server-Side Encryption .
    When copying an object, you can optionally use headers to grant ACL-based permissions. By default, all objects are private. Only the owner has full access control. When adding a new object, you can grant permissions to individual AWS accounts or to predefined groups defined by Amazon S3. These permissions are then added to the ACL on the object. For more information, see Access Control List (ACL) Overview and Managing ACLs Using the REST API .
    You can use the CopyObject operation to change the storage class of an object that is already stored in Amazon S3 using the StorageClass parameter. For more information, see Storage Classes in the Amazon S3 Service Developer Guide .
    By default, x-amz-copy-source identifies the current version of an object to copy. If the current version is a delete marker, Amazon S3 behaves as if the object was deleted. To copy a different version, use the versionId subresource.
    If you enable versioning on the target bucket, Amazon S3 generates a unique version ID for the object being copied. This version ID is different from the version ID of the source object. Amazon S3 returns the version ID of the copied object in the x-amz-version-id response header in the response.
    If you do not enable versioning or suspend it on the target bucket, the version ID that Amazon S3 generates is always null.
    If the source object\'s storage class is GLACIER, you must restore a copy of this object before you can use it as a source object for the copy operation. For more information, see .
    The following operations are related to CopyObject :
    For more information, see Copying Objects .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example copies an object from one bucket to another.
    Expected Output:
    
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
        StorageClass='STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
        WebsiteRedirectLocation='string',
        SSECustomerAlgorithm='string',
        SSECustomerKey='string',
        SSEKMSKeyId='string',
        SSEKMSEncryptionContext='string',
        CopySourceSSECustomerAlgorithm='string',
        CopySourceSSECustomerKey='string',
        RequestPayer='requester',
        Tagging='string',
        ObjectLockMode='GOVERNANCE'|'COMPLIANCE',
        ObjectLockRetainUntilDate=datetime(2015, 1, 1),
        ObjectLockLegalHoldStatus='ON'|'OFF'
    )
    
    
    :type ACL: string
    :param ACL: The canned ACL to apply to the object.

    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the destination bucket.\n

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
    :param CopySource: [REQUIRED] The name of the source bucket, key name of the source object, and optional version ID of the source object. You can either provide this value as a string or a dictionary. The string form is {bucket}/{key} or {bucket}/{key}?versionId={versionId} if you want to copy a specific version. You can also provide this value as a dictionary. The dictionary format is recommended over the string format because it is more explicit. The dictionary format is: {\'Bucket\': \'bucket\', \'Key\': \'key\', \'VersionId\': \'id\'}. Note that the VersionId key is optional and may be omitted.

    :type CopySourceIfMatch: string
    :param CopySourceIfMatch: Copies the object if its entity tag (ETag) matches the specified tag.

    :type CopySourceIfModifiedSince: datetime
    :param CopySourceIfModifiedSince: Copies the object if it has been modified since the specified time.

    :type CopySourceIfNoneMatch: string
    :param CopySourceIfNoneMatch: Copies the object if its entity tag (ETag) is different than the specified ETag.

    :type CopySourceIfUnmodifiedSince: datetime
    :param CopySourceIfUnmodifiedSince: Copies the object if it hasn\'t been modified since the specified time.

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
    :param Key: [REQUIRED]\nThe key of the destination object.\n

    :type Metadata: dict
    :param Metadata: A map of metadata to store with the object in S3.\n\n(string) --\n(string) --\n\n\n\n

    :type MetadataDirective: string
    :param MetadataDirective: Specifies whether the metadata is copied from the source object or replaced with metadata provided in the request.

    :type TaggingDirective: string
    :param TaggingDirective: Specifies whether the object tag-set are copied from the source object or replaced with tag-set provided in the request.

    :type ServerSideEncryption: string
    :param ServerSideEncryption: The server-side encryption algorithm used when storing this object in Amazon S3 (for example, AES256, aws:kms).

    :type StorageClass: string
    :param StorageClass: The type of storage to use for the object. Defaults to \'STANDARD\'.

    :type WebsiteRedirectLocation: string
    :param WebsiteRedirectLocation: If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.

    :type SSECustomerAlgorithm: string
    :param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (for example, AES256).

    :type SSECustomerKey: string
    :param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side\xe2\x80\x8b-encryption\xe2\x80\x8b-customer-algorithm header.

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.\n\nPlease note that this parameter is automatically populated if it is not provided. Including this parameter is not required\n

    :type SSEKMSKeyId: string
    :param SSEKMSKeyId: Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. For information about configuring using any of the officially supported AWS SDKs and AWS CLI, see Specifying the Signature Version in Request Authentication in the Amazon S3 Developer Guide .

    :type SSEKMSEncryptionContext: string
    :param SSEKMSEncryptionContext: Specifies the AWS KMS Encryption Context to use for object encryption. The value of this header is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.

    :type CopySourceSSECustomerAlgorithm: string
    :param CopySourceSSECustomerAlgorithm: Specifies the algorithm to use when decrypting the source object (for example, AES256).

    :type CopySourceSSECustomerKey: string
    :param CopySourceSSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.

    :type CopySourceSSECustomerKeyMD5: string
    :param CopySourceSSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.\n\nPlease note that this parameter is automatically populated if it is not provided. Including this parameter is not required\n

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :type Tagging: string
    :param Tagging: The tag-set for the object destination object this value must be used in conjunction with the TaggingDirective . The tag-set must be encoded as URL Query parameters.

    :type ObjectLockMode: string
    :param ObjectLockMode: The Object Lock mode that you want to apply to the copied object.

    :type ObjectLockRetainUntilDate: datetime
    :param ObjectLockRetainUntilDate: The date and time when you want the copied object\'s Object Lock to expire.

    :type ObjectLockLegalHoldStatus: string
    :param ObjectLockLegalHoldStatus: Specifies whether you want to apply a Legal Hold to the copied object.

    :rtype: dict

ReturnsResponse Syntax
{
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
    'SSEKMSEncryptionContext': 'string',
    'RequestCharged': 'requester'
}


Response Structure

(dict) --

CopyObjectResult (dict) --
Container for all response elements.

ETag (string) --
Returns the ETag of the new object. The ETag reflects only changes to the contents of an object, not its metadata. The source and destination ETag is identical for a successfully copied object.

LastModified (datetime) --
Returns the date that the object was last modified.



Expiration (string) --
If the object expiration is configured, the response includes this header.

CopySourceVersionId (string) --
Version of the copied object in the destination bucket.

VersionId (string) --
Version ID of the newly created copy.

ServerSideEncryption (string) --
The server-side encryption algorithm used when storing this object in Amazon S3 (for example, AES256, aws:kms).

SSECustomerAlgorithm (string) --
If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.

SSECustomerKeyMD5 (string) --
If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round-trip message integrity verification of the customer-provided encryption key.

SSEKMSKeyId (string) --
If present, specifies the ID of the AWS Key Management Service (AWS KMS) symmetric customer managed customer master key (CMK) that was used for the object.

SSEKMSEncryptionContext (string) --
If present, specifies the AWS KMS Encryption Context to use for object encryption. The value of this header is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.







Exceptions

S3.Client.exceptions.ObjectNotInActiveTierError

Examples
The following example copies an object from one bucket to another.
response = client.copy_object(
    Bucket='destinationbucket',
    CopySource='/sourcebucket/HappyFacejpg',
    Key='HappyFaceCopyjpg',
)

print(response)


Expected Output:
{
    'CopyObjectResult': {
        'ETag': '"6805f2cfc46c0f04559748bb039d69ae"',
        'LastModified': datetime(2016, 12, 15, 17, 38, 53, 3, 350, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
        'SSEKMSEncryptionContext': 'string',
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    x-amz-copy-source-if-match condition evaluates to true
    x-amz-copy-source-if-unmodified-since condition evaluates to false
    
    """
    pass

def create_bucket(ACL=None, Bucket=None, CreateBucketConfiguration=None, GrantFullControl=None, GrantRead=None, GrantReadACP=None, GrantWrite=None, GrantWriteACP=None, ObjectLockEnabledForBucket=None):
    """
    Creates a new bucket. To create a bucket, you must register with Amazon S3 and have a valid AWS Access Key ID to authenticate requests. Anonymous requests are never allowed to create buckets. By creating the bucket, you become the bucket owner.
    Not every string is an acceptable bucket name. For information on bucket naming restrictions, see Working with Amazon S3 Buckets .
    By default, the bucket is created in the US East (N. Virginia) Region. You can optionally specify a Region in the request body. You might choose a Region to optimize latency, minimize costs, or address regulatory requirements. For example, if you reside in Europe, you will probably find it advantageous to create buckets in the Europe (Ireland) Region. For more information, see How to Select a Region for Your Buckets .
    When creating a bucket using this operation, you can optionally specify the accounts or groups that should be granted specific permissions on the bucket. There are two ways to grant the appropriate permissions using the request headers.
    For example, the following x-amz-grant-read header grants the AWS accounts identified by account IDs permissions to read object data and its metadata:
    The following operations are related to CreateBucket :
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a bucket. The request specifies an AWS region where to create the bucket.
    Expected Output:
    The following example creates a bucket.
    Expected Output:
    
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
        GrantWriteACP='string',
        ObjectLockEnabledForBucket=True|False
    )
    
    
    :type ACL: string
    :param ACL: The canned ACL to apply to the bucket.

    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket to create.\n

    :type CreateBucketConfiguration: dict
    :param CreateBucketConfiguration: The configuration information for the bucket.\n\nLocationConstraint (string) --Specifies the Region where the bucket will be created. If you don\'t specify a Region, the bucket is created in the US East (N. Virginia) Region (us-east-1).\n\n\n

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

    :type ObjectLockEnabledForBucket: boolean
    :param ObjectLockEnabledForBucket: Specifies whether you want S3 Object Lock to be enabled for the new bucket.

    :rtype: dict

ReturnsResponse Syntax
{
    'Location': 'string'
}


Response Structure

(dict) --

Location (string) --
Specifies the Region where the bucket will be created. If you are creating a bucket on the US East (N. Virginia) Region (us-east-1), you do not need to specify the location.







Exceptions

S3.Client.exceptions.BucketAlreadyExists
S3.Client.exceptions.BucketAlreadyOwnedByYou

Examples
The following example creates a bucket. The request specifies an AWS region where to create the bucket.
response = client.create_bucket(
    Bucket='examplebucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1',
    },
)

print(response)


Expected Output:
{
    'Location': 'http://examplebucket.s3.amazonaws.com/',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example creates a bucket.
response = client.create_bucket(
    Bucket='examplebucket',
)

print(response)


Expected Output:
{
    'Location': '/examplebucket',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Location': 'string'
    }
    
    
    :returns: 
    US East (N. Virginia)
    US West (N. California)
    US West (Oregon)
    Asia Pacific (Singapore)
    Asia Pacific (Sydney)
    Asia Pacific (Tokyo)
    Europe (Ireland)
    South America (S\xc3\xa3o Paulo)
    
    """
    pass

def create_multipart_upload(ACL=None, Bucket=None, CacheControl=None, ContentDisposition=None, ContentEncoding=None, ContentLanguage=None, ContentType=None, Expires=None, GrantFullControl=None, GrantRead=None, GrantReadACP=None, GrantWriteACP=None, Key=None, Metadata=None, ServerSideEncryption=None, StorageClass=None, WebsiteRedirectLocation=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, SSEKMSKeyId=None, SSEKMSEncryptionContext=None, RequestPayer=None, Tagging=None, ObjectLockMode=None, ObjectLockRetainUntilDate=None, ObjectLockLegalHoldStatus=None):
    """
    This operation initiates a multipart upload and returns an upload ID. This upload ID is used to associate all of the parts in the specific multipart upload. You specify this upload ID in each of your subsequent upload part requests (see  UploadPart ). You also include this upload ID in the final request to either complete or abort the multipart upload request.
    For more information about multipart uploads, see Multipart Upload Overview .
    If you have configured a lifecycle rule to abort incomplete multipart uploads, the upload must complete within the number of days specified in the bucket lifecycle configuration. Otherwise, the incomplete multipart upload becomes eligible for an abort operation and Amazon S3 aborts the multipart upload. For more information, see Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Policy .
    For information about the permissions required to use the multipart upload API, see Multipart Upload API and Permissions .
    For request signing, multipart upload is just a series of regular requests. You initiate a multipart upload, send one or more requests to upload parts, and then complete the multipart upload process. You sign each request individually. There is nothing special about signing multipart upload requests. For more information about signing, see Authenticating Requests (AWS Signature Version 4) .
    You can optionally request server-side encryption. For server-side encryption, Amazon S3 encrypts your data as it writes it to disks in its data centers and decrypts it when you access it. You can provide your own encryption key, or use AWS Key Management Service (AWS KMS) customer master keys (CMKs) or Amazon S3-managed encryption keys. If you choose to provide your own encryption key, the request headers you provide in  UploadPart ) and  UploadPartCopy ) requests must match the headers you used in the request to initiate the upload by using CreateMultipartUpload .
    To perform a multipart upload with encryption using an AWS KMS CMK, the requester must have permission to the kms:Encrypt , kms:Decrypt , kms:ReEncrypt* , kms:GenerateDataKey* , and kms:DescribeKey actions on the key. These permissions are required because Amazon S3 must decrypt and read data from the encrypted file parts before it completes the multipart upload.
    If your AWS Identity and Access Management (IAM) user or role is in the same AWS account as the AWS KMS CMK, then you must have these permissions on the key policy. If your IAM user or role belongs to a different account than the key, then you must have the permissions on both the key policy and your IAM user or role.
    For more information, see Protecting Data Using Server-Side Encryption .
    When copying an object, you can optionally specify the accounts or groups that should be granted specific permissions on the new object. There are two ways to grant the permissions using the request headers:
    You can use either a canned ACL or specify access permissions explicitly. You cannot do both.
    You can optionally tell Amazon S3 to encrypt data at rest using server-side encryption. Server-side encryption is for data encryption at rest. Amazon S3 encrypts your data as it writes it to disks in its data centers and decrypts it when you access it. The option you use depends on whether you want to use AWS managed encryption keys or provide your own encryption key.
    For more information about server-side encryption with CMKs stored in AWS KMS (SSE-KMS), see Protecting Data Using Server-Side Encryption with CMKs stored in AWS KMS .
    For more information about server-side encryption with CMKs stored in AWS KMS (SSE-KMS), see Protecting Data Using Server-Side Encryption with CMKs stored in AWS KMS .
    You also can use the following access control\xe2\x80\x93related headers with this operation. By default, all objects are private. Only the owner has full access control. When adding a new object, you can grant permissions to individual AWS accounts or to predefined groups defined by Amazon S3. These permissions are then added to the access control list (ACL) on the object. For more information, see Using ACLs . With this operation, you can grant access permissions using one of the following two methods:
    You specify each grantee as a type=value pair, where the type is one of the following:
    For example, the following x-amz-grant-read header grants the AWS accounts identified by account IDs permissions to read object data and its metadata:
    The following operations are related to CreateMultipartUpload :
    See also: AWS API Documentation
    
    Examples
    The following example initiates a multipart upload.
    Expected Output:
    
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
        StorageClass='STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
        WebsiteRedirectLocation='string',
        SSECustomerAlgorithm='string',
        SSECustomerKey='string',
        SSEKMSKeyId='string',
        SSEKMSEncryptionContext='string',
        RequestPayer='requester',
        Tagging='string',
        ObjectLockMode='GOVERNANCE'|'COMPLIANCE',
        ObjectLockRetainUntilDate=datetime(2015, 1, 1),
        ObjectLockLegalHoldStatus='ON'|'OFF'
    )
    
    
    :type ACL: string
    :param ACL: The canned ACL to apply to the object.

    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket to which to initiate the upload\n

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
    :param Key: [REQUIRED]\nObject key for which the multipart upload is to be initiated.\n

    :type Metadata: dict
    :param Metadata: A map of metadata to store with the object in S3.\n\n(string) --\n(string) --\n\n\n\n

    :type ServerSideEncryption: string
    :param ServerSideEncryption: The server-side encryption algorithm used when storing this object in Amazon S3 (for example, AES256, aws:kms).

    :type StorageClass: string
    :param StorageClass: The type of storage to use for the object. Defaults to \'STANDARD\'.

    :type WebsiteRedirectLocation: string
    :param WebsiteRedirectLocation: If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.

    :type SSECustomerAlgorithm: string
    :param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (for example, AES256).

    :type SSECustomerKey: string
    :param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side\xe2\x80\x8b-encryption\xe2\x80\x8b-customer-algorithm header.

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.\n\nPlease note that this parameter is automatically populated if it is not provided. Including this parameter is not required\n

    :type SSEKMSKeyId: string
    :param SSEKMSKeyId: Specifies the ID of the symmetric customer managed AWS KMS CMK to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. For information about configuring using any of the officially supported AWS SDKs and AWS CLI, see Specifying the Signature Version in Request Authentication in the Amazon S3 Developer Guide .

    :type SSEKMSEncryptionContext: string
    :param SSEKMSEncryptionContext: Specifies the AWS KMS Encryption Context to use for object encryption. The value of this header is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :type Tagging: string
    :param Tagging: The tag-set for the object. The tag-set must be encoded as URL Query parameters.

    :type ObjectLockMode: string
    :param ObjectLockMode: Specifies the Object Lock mode that you want to apply to the uploaded object.

    :type ObjectLockRetainUntilDate: datetime
    :param ObjectLockRetainUntilDate: Specifies the date and time when you want the Object Lock to expire.

    :type ObjectLockLegalHoldStatus: string
    :param ObjectLockLegalHoldStatus: Specifies whether you want to apply a Legal Hold to the uploaded object.

    :rtype: dict

ReturnsResponse Syntax
{
    'AbortDate': datetime(2015, 1, 1),
    'AbortRuleId': 'string',
    'Bucket': 'string',
    'Key': 'string',
    'UploadId': 'string',
    'ServerSideEncryption': 'AES256'|'aws:kms',
    'SSECustomerAlgorithm': 'string',
    'SSECustomerKeyMD5': 'string',
    'SSEKMSKeyId': 'string',
    'SSEKMSEncryptionContext': 'string',
    'RequestCharged': 'requester'
}


Response Structure

(dict) --

AbortDate (datetime) --
If the bucket has a lifecycle rule configured with an action to abort incomplete multipart uploads and the prefix in the lifecycle rule matches the object name in the request, the response includes this header. The header indicates when the initiated multipart upload becomes eligible for an abort operation. For more information, see Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Policy .
The response also includes the x-amz-abort-rule-id header that provides the ID of the lifecycle configuration rule that defines this action.

AbortRuleId (string) --
This header is returned along with the x-amz-abort-date header. It identifies the applicable lifecycle configuration rule that defines the action to abort incomplete multipart uploads.

Bucket (string) --
Name of the bucket to which the multipart upload was initiated.
When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .

Key (string) --
Object key for which the multipart upload was initiated.

UploadId (string) --
ID for the initiated multipart upload.

ServerSideEncryption (string) --
The server-side encryption algorithm used when storing this object in Amazon S3 (for example, AES256, aws:kms).

SSECustomerAlgorithm (string) --
If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.

SSECustomerKeyMD5 (string) --
If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round-trip message integrity verification of the customer-provided encryption key.

SSEKMSKeyId (string) --
If present, specifies the ID of the AWS Key Management Service (AWS KMS) symmetric customer managed customer master key (CMK) that was used for the object.

SSEKMSEncryptionContext (string) --
If present, specifies the AWS KMS Encryption Context to use for object encryption. The value of this header is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.







Examples
The following example initiates a multipart upload.
response = client.create_multipart_upload(
    Bucket='examplebucket',
    Key='largeobject',
)

print(response)


Expected Output:
{
    'Bucket': 'examplebucket',
    'Key': 'largeobject',
    'UploadId': 'ibZBv_75gd9r8lH_gqXatLdxMVpAlj6ZQjEs.OwyF3953YdwbcQnMA2BLGn8Lx12fQNICtMw5KyteFeHw.Sjng--',
    'ResponseMetadata': {
        '...': '...',
    },
}



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
        'SSEKMSEncryptionContext': 'string',
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    Use encryption keys managed by Amazon S3 or customer master keys (CMKs) stored in AWS Key Management Service (AWS KMS) \xe2\x80\x93 If you want AWS to manage the keys used to encrypt data, specify the following headers in the request.
    x-amz-server-side\xe2\x80\x8b-encryption
    x-amz-server-side-encryption-aws-kms-key-id
    x-amz-server-side-encryption-context
    
    
    
    """
    pass

def delete_bucket(Bucket=None):
    """
    Deletes the bucket. All objects (including all object versions and delete markers) in the bucket must be deleted before the bucket itself can be deleted.
    See also: AWS API Documentation
    
    Examples
    The following example deletes the specified bucket.
    Expected Output:
    
    :example: response = client.delete_bucket(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nSpecifies the bucket being deleted.\n

    :return: response = client.delete_bucket(
        Bucket='forrandall2',
    )
    
    print(response)
    
    
    """
    pass

def delete_bucket_analytics_configuration(Bucket=None, Id=None):
    """
    Deletes an analytics configuration for the bucket (specified by the analytics configuration ID).
    To use this operation, you must have permissions to perform the s3:PutAnalyticsConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    For information about the Amazon S3 analytics feature, see Amazon S3 Analytics \xe2\x80\x93 Storage Class Analysis .
    The following operations are related to DeleteBucketAnalyticsConfiguration :
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bucket_analytics_configuration(
        Bucket='string',
        Id='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket from which an analytics configuration is deleted.\n

    :type Id: string
    :param Id: [REQUIRED]\nThe ID that identifies the analytics configuration.\n

    :returns: 
    Bucket (string) -- [REQUIRED]
    The name of the bucket from which an analytics configuration is deleted.
    
    Id (string) -- [REQUIRED]
    The ID that identifies the analytics configuration.
    
    
    """
    pass

def delete_bucket_cors(Bucket=None):
    """
    Deletes the cors configuration information set for the bucket.
    To use this operation, you must have permission to perform the s3:PutBucketCORS action. The bucket owner has this permission by default and can grant this permission to others.
    For information about cors , see Enabling Cross-Origin Resource Sharing in the Amazon Simple Storage Service Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example deletes CORS configuration on a bucket.
    Expected Output:
    
    :example: response = client.delete_bucket_cors(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nSpecifies the bucket whose cors configuration is being deleted.\n

    :return: response = client.delete_bucket_cors(
        Bucket='examplebucket',
    )
    
    print(response)
    
    
    """
    pass

def delete_bucket_encryption(Bucket=None):
    """
    This implementation of the DELETE operation removes default encryption from the bucket. For information about the Amazon S3 default encryption feature, see Amazon S3 Default Bucket Encryption in the Amazon Simple Storage Service Developer Guide .
    To use this operation, you must have permissions to perform the s3:PutEncryptionConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to your Amazon S3 Resources in the Amazon Simple Storage Service Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bucket_encryption(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket containing the server-side encryption configuration to delete.\n

    """
    pass

def delete_bucket_inventory_configuration(Bucket=None, Id=None):
    """
    Deletes an inventory configuration (identified by the inventory ID) from the bucket.
    To use this operation, you must have permissions to perform the s3:PutInventoryConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    For information about the Amazon S3 inventory feature, see Amazon S3 Inventory .
    Operations related to DeleteBucketInventoryConfiguration include:
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bucket_inventory_configuration(
        Bucket='string',
        Id='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket containing the inventory configuration to delete.\n

    :type Id: string
    :param Id: [REQUIRED]\nThe ID used to identify the inventory configuration.\n

    :returns: 
    Bucket (string) -- [REQUIRED]
    The name of the bucket containing the inventory configuration to delete.
    
    Id (string) -- [REQUIRED]
    The ID used to identify the inventory configuration.
    
    
    """
    pass

def delete_bucket_lifecycle(Bucket=None):
    """
    Deletes the lifecycle configuration from the specified bucket. Amazon S3 removes all the lifecycle configuration rules in the lifecycle subresource associated with the bucket. Your objects never expire, and Amazon S3 no longer automatically deletes any objects on the basis of rules contained in the deleted lifecycle configuration.
    To use this operation, you must have permission to perform the s3:PutLifecycleConfiguration action. By default, the bucket owner has this permission and the bucket owner can grant this permission to others.
    There is usually some time lag before lifecycle configuration deletion is fully propagated to all the Amazon S3 systems.
    For more information about the object expiration, see Elements to Describe Lifecycle Actions .
    Related actions include:
    See also: AWS API Documentation
    
    Examples
    The following example deletes lifecycle configuration on a bucket.
    Expected Output:
    
    :example: response = client.delete_bucket_lifecycle(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name of the lifecycle to delete.\n

    :return: response = client.delete_bucket_lifecycle(
        Bucket='examplebucket',
    )
    
    print(response)
    
    
    """
    pass

def delete_bucket_metrics_configuration(Bucket=None, Id=None):
    """
    Deletes a metrics configuration for the Amazon CloudWatch request metrics (specified by the metrics configuration ID) from the bucket. Note that this doesn\'t include the daily storage metrics.
    To use this operation, you must have permissions to perform the s3:PutMetricsConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    For information about CloudWatch request metrics for Amazon S3, see Monitoring Metrics with Amazon CloudWatch .
    The following operations are related to DeleteBucketMetricsConfiguration :
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bucket_metrics_configuration(
        Bucket='string',
        Id='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket containing the metrics configuration to delete.\n

    :type Id: string
    :param Id: [REQUIRED]\nThe ID used to identify the metrics configuration.\n

    :returns: 
    Bucket (string) -- [REQUIRED]
    The name of the bucket containing the metrics configuration to delete.
    
    Id (string) -- [REQUIRED]
    The ID used to identify the metrics configuration.
    
    
    """
    pass

def delete_bucket_policy(Bucket=None):
    """
    This implementation of the DELETE operation uses the policy subresource to delete the policy of a specified bucket. If you are using an identity other than the root user of the AWS account that owns the bucket, the calling identity must have the DeleteBucketPolicy permissions on the specified bucket and belong to the bucket owner\'s account to use this operation.
    If you don\'t have DeleteBucketPolicy permissions, Amazon S3 returns a 403 Access Denied error. If you have the correct permissions, but you\'re not using an identity that belongs to the bucket owner\'s account, Amazon S3 returns a 405 Method Not Allowed error.
    For more information about bucket policies, see `Using Bucket Policies and UserPolicies < https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html>`__ .
    The following operations are related to DeleteBucketPolicy
    See also: AWS API Documentation
    
    Examples
    The following example deletes bucket policy on the specified bucket.
    Expected Output:
    
    :example: response = client.delete_bucket_policy(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name.\n

    :return: response = client.delete_bucket_policy(
        Bucket='examplebucket',
    )
    
    print(response)
    
    
    """
    pass

def delete_bucket_replication(Bucket=None):
    """
    Deletes the replication configuration from the bucket.
    To use this operation, you must have permissions to perform the s3:PutReplicationConfiguration action. The bucket owner has these permissions by default and can grant it to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    For information about replication configuration, see `Replication < https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html>`__ in the Amazon S3 Developer Guide .
    The following operations are related to DeleteBucketReplication :
    See also: AWS API Documentation
    
    Examples
    The following example deletes replication configuration set on bucket.
    Expected Output:
    
    :example: response = client.delete_bucket_replication(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name.\n

    :return: response = client.delete_bucket_replication(
        Bucket='example',
    )
    
    print(response)
    
    
    """
    pass

def delete_bucket_tagging(Bucket=None):
    """
    Deletes the tags from the bucket.
    To use this operation, you must have permission to perform the s3:PutBucketTagging action. By default, the bucket owner has this permission and can grant this permission to others.
    The following operations are related to DeleteBucketTagging :
    See also: AWS API Documentation
    
    Examples
    The following example deletes bucket tags.
    Expected Output:
    
    :example: response = client.delete_bucket_tagging(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket that has the tag set to be removed.\n

    :return: response = client.delete_bucket_tagging(
        Bucket='examplebucket',
    )
    
    print(response)
    
    
    """
    pass

def delete_bucket_website(Bucket=None):
    """
    This operation removes the website configuration for a bucket. Amazon S3 returns a 200 OK response upon successfully deleting a website configuration on the specified bucket. You will get a 200 OK response if the website configuration you are trying to delete does not exist on the bucket. Amazon S3 returns a 404 response if the bucket specified in the request does not exist.
    This DELETE operation requires the S3:DeleteBucketWebsite permission. By default, only the bucket owner can delete the website configuration attached to a bucket. However, bucket owners can grant other users permission to delete the website configuration by writing a bucket policy granting them the S3:DeleteBucketWebsite permission.
    For more information about hosting websites, see Hosting Websites on Amazon S3 .
    The following operations are related to DeleteBucketWebsite :
    See also: AWS API Documentation
    
    Examples
    The following example deletes bucket website configuration.
    Expected Output:
    
    :example: response = client.delete_bucket_website(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name for which you want to remove the website configuration.\n

    :return: response = client.delete_bucket_website(
        Bucket='examplebucket',
    )
    
    print(response)
    
    
    """
    pass

def delete_object(Bucket=None, Key=None, MFA=None, VersionId=None, RequestPayer=None, BypassGovernanceRetention=None):
    """
    Removes the null version (if there is one) of an object and inserts a delete marker, which becomes the latest version of the object. If there isn\'t a null version, Amazon S3 does not remove any objects.
    To remove a specific version, you must be the bucket owner and you must use the version Id subresource. Using this subresource permanently deletes the version. If the object deleted is a delete marker, Amazon S3 sets the response header, x-amz-delete-marker , to true.
    If the object you want to delete is in a bucket where the bucket versioning configuration is MFA Delete enabled, you must include the x-amz-mfa request header in the DELETE versionId request. Requests that include x-amz-mfa must use HTTPS.
    For more information about MFA Delete, see Using MFA Delete . To see sample requests that use versioning, see Sample Request .
    You can delete objects by explicitly calling the DELETE Object API or configure its lifecycle ( PutBucketLifecycle ) to enable Amazon S3 to remove them for you. If you want to block users or accounts from removing or deleting objects from your bucket, you must deny them the s3:DeleteObject , s3:DeleteObjectVersion , and s3:PutLifeCycleConfiguration actions.
    The following operation is related to DeleteObject :
    See also: AWS API Documentation
    
    Examples
    The following example deletes an object from an S3 bucket.
    Expected Output:
    The following example deletes an object from a non-versioned bucket.
    Expected Output:
    
    :example: response = client.delete_object(
        Bucket='string',
        Key='string',
        MFA='string',
        VersionId='string',
        RequestPayer='requester',
        BypassGovernanceRetention=True|False
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name of the bucket containing the object.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Key: string
    :param Key: [REQUIRED]\nKey name of the object to delete.\n

    :type MFA: string
    :param MFA: The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device. Required to permanently delete a versioned object if versioning is configured with MFA delete enabled.

    :type VersionId: string
    :param VersionId: VersionId used to reference a specific version of the object.

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :type BypassGovernanceRetention: boolean
    :param BypassGovernanceRetention: Indicates whether S3 Object Lock should bypass Governance-mode restrictions to process this operation.

    :rtype: dict

ReturnsResponse Syntax
{
    'DeleteMarker': True|False,
    'VersionId': 'string',
    'RequestCharged': 'requester'
}


Response Structure

(dict) --

DeleteMarker (boolean) --
Specifies whether the versioned object that was permanently deleted was (true) or was not (false) a delete marker.

VersionId (string) --
Returns the version ID of the delete marker created as a result of the DELETE operation.

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.







Examples
The following example deletes an object from an S3 bucket.
response = client.delete_object(
    Bucket='examplebucket',
    Key='objectkey.jpg',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example deletes an object from a non-versioned bucket.
response = client.delete_object(
    Bucket='ExampleBucket',
    Key='HappyFace.jpg',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'DeleteMarker': True|False,
        'VersionId': 'string',
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    Bucket (string) -- [REQUIRED]
    The bucket name of the bucket containing the object.
    When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
    
    Key (string) -- [REQUIRED]
    Key name of the object to delete.
    
    MFA (string) -- The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device. Required to permanently delete a versioned object if versioning is configured with MFA delete enabled.
    VersionId (string) -- VersionId used to reference a specific version of the object.
    RequestPayer (string) -- Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .
    BypassGovernanceRetention (boolean) -- Indicates whether S3 Object Lock should bypass Governance-mode restrictions to process this operation.
    
    """
    pass

def delete_object_tagging(Bucket=None, Key=None, VersionId=None):
    """
    Removes the entire tag set from the specified object. For more information about managing object tags, see Object Tagging .
    To use this operation, you must have permission to perform the s3:DeleteObjectTagging action.
    To delete tags of a specific object version, add the versionId query parameter in the request. You will need permission for the s3:DeleteObjectVersionTagging action.
    The following operations are related to DeleteBucketMetricsConfiguration :
    See also: AWS API Documentation
    
    Examples
    The following example removes tag set associated with the specified object version. The request specifies both the object key and object version.
    Expected Output:
    The following example removes tag set associated with the specified object. If the bucket is versioning enabled, the operation removes tag set from the latest object version.
    Expected Output:
    
    :example: response = client.delete_object_tagging(
        Bucket='string',
        Key='string',
        VersionId='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name containing the objects from which to remove the tags.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Key: string
    :param Key: [REQUIRED]\nName of the tag.\n

    :type VersionId: string
    :param VersionId: The versionId of the object that the tag-set will be removed from.

    :rtype: dict

ReturnsResponse Syntax
{
    'VersionId': 'string'
}


Response Structure

(dict) --

VersionId (string) --
The versionId of the object the tag-set was removed from.







Examples
The following example removes tag set associated with the specified object version. The request specifies both the object key and object version.
response = client.delete_object_tagging(
    Bucket='examplebucket',
    Key='HappyFace.jpg',
    VersionId='ydlaNkwWm0SfKJR.T1b1fIdPRbldTYRI',
)

print(response)


Expected Output:
{
    'VersionId': 'ydlaNkwWm0SfKJR.T1b1fIdPRbldTYRI',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example removes tag set associated with the specified object. If the bucket is versioning enabled, the operation removes tag set from the latest object version.
response = client.delete_object_tagging(
    Bucket='examplebucket',
    Key='HappyFace.jpg',
)

print(response)


Expected Output:
{
    'VersionId': 'null',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'VersionId': 'string'
    }
    
    
    :returns: 
    Bucket (string) -- [REQUIRED]
    The bucket name containing the objects from which to remove the tags.
    When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
    
    Key (string) -- [REQUIRED]
    Name of the tag.
    
    VersionId (string) -- The versionId of the object that the tag-set will be removed from.
    
    """
    pass

def delete_objects(Bucket=None, Delete=None, MFA=None, RequestPayer=None, BypassGovernanceRetention=None):
    """
    This operation enables you to delete multiple objects from a bucket using a single HTTP request. If you know the object keys that you want to delete, then this operation provides a suitable alternative to sending individual delete requests, reducing per-request overhead.
    The request contains a list of up to 1000 keys that you want to delete. In the XML, you provide the object key names, and optionally, version IDs if you want to delete a specific version of the object from a versioning-enabled bucket. For each key, Amazon S3 performs a delete operation and returns the result of that delete, success, or failure, in the response. Note that if the object specified in the request is not found, Amazon S3 returns the result as deleted.
    The operation supports two modes for the response: verbose and quiet. By default, the operation uses verbose mode in which the response includes the result of deletion of each key in your request. In quiet mode the response includes only keys where the delete operation encountered an error. For a successful deletion, the operation does not return any information about the delete in the response body.
    When performing this operation on an MFA Delete enabled bucket, that attempts to delete any versioned objects, you must include an MFA token. If you do not provide one, the entire request will fail, even if there are non-versioned objects you are trying to delete. If you provide an invalid token, whether there are versioned keys in the request or not, the entire Multi-Object Delete request will fail. For information about MFA Delete, see MFA Delete .
    Finally, the Content-MD5 header is required for all Multi-Object Delete requests. Amazon S3 uses the header value to ensure that your request body has not been altered in transit.
    The following operations are related to DeleteObjects :
    See also: AWS API Documentation
    
    Examples
    The following example deletes objects from a bucket. The request specifies object versions. S3 deletes specific object versions and returns the key and versions of deleted objects in the response.
    Expected Output:
    The following example deletes objects from a bucket. The bucket is versioned, and the request does not specify the object version to delete. In this case, all versions remain in the bucket and S3 adds a delete marker.
    Expected Output:
    
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
        RequestPayer='requester',
        BypassGovernanceRetention=True|False
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name containing the objects to delete.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Delete: dict
    :param Delete: [REQUIRED]\nContainer for the request.\n\nObjects (list) -- [REQUIRED]The objects to delete.\n\n(dict) --Object Identifier is unique value to identify objects.\n\nKey (string) -- [REQUIRED]Key name of the object to delete.\n\nVersionId (string) --VersionId for the specific version of the object to delete.\n\n\n\n\n\nQuiet (boolean) --Element to enable quiet mode for the request. When you add this element, you must set its value to true.\n\n\n

    :type MFA: string
    :param MFA: The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device. Required to permanently delete a versioned object if versioning is configured with MFA delete enabled.

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :type BypassGovernanceRetention: boolean
    :param BypassGovernanceRetention: Specifies whether you want to delete this object even if it has a Governance-type Object Lock in place. You must have sufficient permissions to perform this operation.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Deleted (list) --
Container element for a successful delete. It identifies the object that was successfully deleted.

(dict) --
Information about the deleted object.

Key (string) --
The name of the deleted object.

VersionId (string) --
The version ID of the deleted object.

DeleteMarker (boolean) --
Specifies whether the versioned object that was permanently deleted was (true) or was not (false) a delete marker. In a simple DELETE, this header indicates whether (true) or not (false) a delete marker was created.

DeleteMarkerVersionId (string) --
The version ID of the delete marker created as a result of the DELETE operation. If you delete a specific object version, the value returned by this header is the version ID of the object version deleted.





RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.

Errors (list) --
Container for a failed delete operation that describes the object that Amazon S3 attempted to delete and the error it encountered.

(dict) --
Container for all error elements.

Key (string) --
The error key.

VersionId (string) --
The version ID of the error.

Code (string) --
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.

Amazon S3 error codes



Code: AccessDenied
Description: Access Denied
HTTP Status Code: 403 Forbidden
SOAP Fault Code Prefix: Client



Code: AccountProblem
Description: There is a problem with your AWS account that prevents the operation from completing successfully. Contact AWS Support for further assistance.
HTTP Status Code: 403 Forbidden
SOAP Fault Code Prefix: Client



Code: AllAccessDisabled
Description: All access to this Amazon S3 resource has been disabled. Contact AWS Support for further assistance.
HTTP Status Code: 403 Forbidden
SOAP Fault Code Prefix: Client



Code: AmbiguousGrantByEmailAddress
Description: The email address you provided is associated with more than one account.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: AuthorizationHeaderMalformed
Description: The authorization header you provided is invalid.
HTTP Status Code: 400 Bad Request
HTTP Status Code: N/A



Code: BadDigest
Description: The Content-MD5 you specified did not match what we received.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: BucketAlreadyExists
Description: The requested bucket name is not available. The bucket namespace is shared by all users of the system. Please select a different name and try again.
HTTP Status Code: 409 Conflict
SOAP Fault Code Prefix: Client



Code: BucketAlreadyOwnedByYou
Description: The bucket you tried to create already exists, and you own it. Amazon S3 returns this error in all AWS Regions except in the North Virginia Region. For legacy compatibility, if you re-create an existing bucket that you already own in the North Virginia Region, Amazon S3 returns 200 OK and resets the bucket access control lists (ACLs).
Code: 409 Conflict (in all Regions except the North Virginia Region)
SOAP Fault Code Prefix: Client



Code: BucketNotEmpty
Description: The bucket you tried to delete is not empty.
HTTP Status Code: 409 Conflict
SOAP Fault Code Prefix: Client



Code: CredentialsNotSupported
Description: This request does not support credentials.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: CrossLocationLoggingProhibited
Description: Cross-location logging not allowed. Buckets in one geographic location cannot log information to a bucket in another location.
HTTP Status Code: 403 Forbidden
SOAP Fault Code Prefix: Client



Code: EntityTooSmall
Description: Your proposed upload is smaller than the minimum allowed object size.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: EntityTooLarge
Description: Your proposed upload exceeds the maximum allowed object size.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: ExpiredToken
Description: The provided token has expired.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: IllegalVersioningConfigurationException
Description: Indicates that the versioning configuration specified in the request is invalid.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: IncompleteBody
Description: You did not provide the number of bytes specified by the Content-Length HTTP header
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: IncorrectNumberOfFilesInPostRequest
Description: POST requires exactly one file upload per request.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InlineDataTooLarge
Description: Inline data exceeds the maximum allowed size.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InternalError
Description: We encountered an internal error. Please try again.
HTTP Status Code: 500 Internal Server Error
SOAP Fault Code Prefix: Server



Code: InvalidAccessKeyId
Description: The AWS access key ID you provided does not exist in our records.
HTTP Status Code: 403 Forbidden
SOAP Fault Code Prefix: Client



Code: InvalidAddressingHeader
Description: You must specify the Anonymous role.
HTTP Status Code: N/A
SOAP Fault Code Prefix: Client



Code: InvalidArgument
Description: Invalid Argument
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InvalidBucketName
Description: The specified bucket is not valid.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InvalidBucketState
Description: The request is not valid with the current state of the bucket.
HTTP Status Code: 409 Conflict
SOAP Fault Code Prefix: Client



Code: InvalidDigest
Description: The Content-MD5 you specified is not valid.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InvalidEncryptionAlgorithmError
Description: The encryption request you specified is not valid. The valid value is AES256.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InvalidLocationConstraint
Description: The specified location constraint is not valid. For more information about Regions, see How to Select a Region for Your Buckets .
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InvalidObjectState
Description: The operation is not valid for the current state of the object.
HTTP Status Code: 403 Forbidden
SOAP Fault Code Prefix: Client



Code: InvalidPart
Description: One or more of the specified parts could not be found. The part might not have been uploaded, or the specified entity tag might not have matched the part\'s entity tag.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InvalidPartOrder
Description: The list of parts was not in ascending order. Parts list must be specified in order by part number.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InvalidPayer
Description: All access to this object has been disabled. Please contact AWS Support for further assistance.
HTTP Status Code: 403 Forbidden
SOAP Fault Code Prefix: Client



Code: InvalidPolicyDocument
Description: The content of the form does not meet the conditions specified in the policy document.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InvalidRange
Description: The requested range cannot be satisfied.
HTTP Status Code: 416 Requested Range Not Satisfiable
SOAP Fault Code Prefix: Client



Code: InvalidRequest
Description: Please use AWS4-HMAC-SHA256.
HTTP Status Code: 400 Bad Request
Code: N/A



Code: InvalidRequest
Description: SOAP requests must be made over an HTTPS connection.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InvalidRequest
Description: Amazon S3 Transfer Acceleration is not supported for buckets with non-DNS compliant names.
HTTP Status Code: 400 Bad Request
Code: N/A



Code: InvalidRequest
Description: Amazon S3 Transfer Acceleration is not supported for buckets with periods (.) in their names.
HTTP Status Code: 400 Bad Request
Code: N/A



Code: InvalidRequest
Description: Amazon S3 Transfer Accelerate endpoint only supports virtual style requests.
HTTP Status Code: 400 Bad Request
Code: N/A



Code: InvalidRequest
Description: Amazon S3 Transfer Accelerate is not configured on this bucket.
HTTP Status Code: 400 Bad Request
Code: N/A



Code: InvalidRequest
Description: Amazon S3 Transfer Accelerate is disabled on this bucket.
HTTP Status Code: 400 Bad Request
Code: N/A



Code: InvalidRequest
Description: Amazon S3 Transfer Acceleration is not supported on this bucket. Contact AWS Support for more information.
HTTP Status Code: 400 Bad Request
Code: N/A



Code: InvalidRequest
Description: Amazon S3 Transfer Acceleration cannot be enabled on this bucket. Contact AWS Support for more information.
HTTP Status Code: 400 Bad Request
Code: N/A



Code: InvalidSecurity
Description: The provided security credentials are not valid.
HTTP Status Code: 403 Forbidden
SOAP Fault Code Prefix: Client



Code: InvalidSOAPRequest
Description: The SOAP request body is invalid.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InvalidStorageClass
Description: The storage class you specified is not valid.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InvalidTargetBucketForLogging
Description: The target bucket for logging does not exist, is not owned by you, or does not have the appropriate grants for the log-delivery group.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InvalidToken
Description: The provided token is malformed or otherwise invalid.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: InvalidURI
Description: Couldn\'t parse the specified URI.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: KeyTooLongError
Description: Your key is too long.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: MalformedACLError
Description: The XML you provided was not well-formed or did not validate against our published schema.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: MalformedPOSTRequest
Description: The body of your POST request is not well-formed multipart/form-data.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: MalformedXML
Description: This happens when the user sends malformed XML (XML that doesn\'t conform to the published XSD) for the configuration. The error message is, "The XML you provided was not well-formed or did not validate against our published schema."
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: MaxMessageLengthExceeded
Description: Your request was too big.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: MaxPostPreDataLengthExceededError
Description: Your POST request fields preceding the upload file were too large.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: MetadataTooLarge
Description: Your metadata headers exceed the maximum allowed metadata size.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: MethodNotAllowed
Description: The specified method is not allowed against this resource.
HTTP Status Code: 405 Method Not Allowed
SOAP Fault Code Prefix: Client



Code: MissingAttachment
Description: A SOAP attachment was expected, but none were found.
HTTP Status Code: N/A
SOAP Fault Code Prefix: Client



Code: MissingContentLength
Description: You must provide the Content-Length HTTP header.
HTTP Status Code: 411 Length Required
SOAP Fault Code Prefix: Client



Code: MissingRequestBodyError
Description: This happens when the user sends an empty XML document as a request. The error message is, "Request body is empty."
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: MissingSecurityElement
Description: The SOAP 1.1 request is missing a security element.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: MissingSecurityHeader
Description: Your request is missing a required header.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: NoLoggingStatusForKey
Description: There is no such thing as a logging status subresource for a key.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: NoSuchBucket
Description: The specified bucket does not exist.
HTTP Status Code: 404 Not Found
SOAP Fault Code Prefix: Client



Code: NoSuchBucketPolicy
Description: The specified bucket does not have a bucket policy.
HTTP Status Code: 404 Not Found
SOAP Fault Code Prefix: Client



Code: NoSuchKey
Description: The specified key does not exist.
HTTP Status Code: 404 Not Found
SOAP Fault Code Prefix: Client



Code: NoSuchLifecycleConfiguration
Description: The lifecycle configuration does not exist.
HTTP Status Code: 404 Not Found
SOAP Fault Code Prefix: Client



Code: NoSuchUpload
Description: The specified multipart upload does not exist. The upload ID might be invalid, or the multipart upload might have been aborted or completed.
HTTP Status Code: 404 Not Found
SOAP Fault Code Prefix: Client



Code: NoSuchVersion
Description: Indicates that the version ID specified in the request does not match an existing version.
HTTP Status Code: 404 Not Found
SOAP Fault Code Prefix: Client



Code: NotImplemented
Description: A header you provided implies functionality that is not implemented.
HTTP Status Code: 501 Not Implemented
SOAP Fault Code Prefix: Server



Code: NotSignedUp
Description: Your account is not signed up for the Amazon S3 service. You must sign up before you can use Amazon S3. You can sign up at the following URL: https://aws.amazon.com/s3
HTTP Status Code: 403 Forbidden
SOAP Fault Code Prefix: Client



Code: OperationAborted
Description: A conflicting conditional operation is currently in progress against this resource. Try again.
HTTP Status Code: 409 Conflict
SOAP Fault Code Prefix: Client



Code: PermanentRedirect
Description: The bucket you are attempting to access must be addressed using the specified endpoint. Send all future requests to this endpoint.
HTTP Status Code: 301 Moved Permanently
SOAP Fault Code Prefix: Client



Code: PreconditionFailed
Description: At least one of the preconditions you specified did not hold.
HTTP Status Code: 412 Precondition Failed
SOAP Fault Code Prefix: Client



Code: Redirect
Description: Temporary redirect.
HTTP Status Code: 307 Moved Temporarily
SOAP Fault Code Prefix: Client



Code: RestoreAlreadyInProgress
Description: Object restore is already in progress.
HTTP Status Code: 409 Conflict
SOAP Fault Code Prefix: Client



Code: RequestIsNotMultiPartContent
Description: Bucket POST must be of the enclosure-type multipart/form-data.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: RequestTimeout
Description: Your socket connection to the server was not read from or written to within the timeout period.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: RequestTimeTooSkewed
Description: The difference between the request time and the server\'s time is too large.
HTTP Status Code: 403 Forbidden
SOAP Fault Code Prefix: Client



Code: RequestTorrentOfBucketError
Description: Requesting the torrent file of a bucket is not permitted.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: SignatureDoesNotMatch
Description: The request signature we calculated does not match the signature you provided. Check your AWS secret access key and signing method. For more information, see REST Authentication and SOAP Authentication for details.
HTTP Status Code: 403 Forbidden
SOAP Fault Code Prefix: Client



Code: ServiceUnavailable
Description: Reduce your request rate.
HTTP Status Code: 503 Service Unavailable
SOAP Fault Code Prefix: Server



Code: SlowDown
Description: Reduce your request rate.
HTTP Status Code: 503 Slow Down
SOAP Fault Code Prefix: Server



Code: TemporaryRedirect
Description: You are being redirected to the bucket while DNS updates.
HTTP Status Code: 307 Moved Temporarily
SOAP Fault Code Prefix: Client



Code: TokenRefreshRequired
Description: The provided token must be refreshed.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: TooManyBuckets
Description: You have attempted to create more buckets than allowed.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: UnexpectedContent
Description: This request does not support content.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: UnresolvableGrantByEmailAddress
Description: The email address you provided does not match any account on record.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client



Code: UserKeyMustBeSpecified
Description: The bucket POST must contain the specified field name. If it is specified, check the order of the fields.
HTTP Status Code: 400 Bad Request
SOAP Fault Code Prefix: Client




Message (string) --
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don\'t know how or don\'t care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.











Examples
The following example deletes objects from a bucket. The request specifies object versions. S3 deletes specific object versions and returns the key and versions of deleted objects in the response.
response = client.delete_objects(
    Bucket='examplebucket',
    Delete={
        'Objects': [
            {
                'Key': 'HappyFace.jpg',
                'VersionId': '2LWg7lQLnY41.maGB5Z6SWW.dcq0vx7b',
            },
            {
                'Key': 'HappyFace.jpg',
                'VersionId': 'yoz3HB.ZhCS_tKVEmIOr7qYyyAaZSKVd',
            },
        ],
        'Quiet': False,
    },
)

print(response)


Expected Output:
{
    'Deleted': [
        {
            'Key': 'HappyFace.jpg',
            'VersionId': 'yoz3HB.ZhCS_tKVEmIOr7qYyyAaZSKVd',
        },
        {
            'Key': 'HappyFace.jpg',
            'VersionId': '2LWg7lQLnY41.maGB5Z6SWW.dcq0vx7b',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example deletes objects from a bucket. The bucket is versioned, and the request does not specify the object version to delete. In this case, all versions remain in the bucket and S3 adds a delete marker.
response = client.delete_objects(
    Bucket='examplebucket',
    Delete={
        'Objects': [
            {
                'Key': 'objectkey1',
            },
            {
                'Key': 'objectkey2',
            },
        ],
        'Quiet': False,
    },
)

print(response)


Expected Output:
{
    'Deleted': [
        {
            'DeleteMarker': 'true',
            'DeleteMarkerVersionId': 'A._w1z6EFiCF5uhtQMDal9JDkID9tQ7F',
            'Key': 'objectkey1',
        },
        {
            'DeleteMarker': 'true',
            'DeleteMarkerVersionId': 'iOd_ORxhkKe_e8G8_oSGxt2PjsCZKlkt',
            'Key': 'objectkey2',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    Bucket (string) -- [REQUIRED]
    The bucket name containing the objects to delete.
    When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
    
    Delete (dict) -- [REQUIRED]
    Container for the request.
    
    Objects (list) -- [REQUIRED]The objects to delete.
    
    (dict) --Object Identifier is unique value to identify objects.
    
    Key (string) -- [REQUIRED]Key name of the object to delete.
    
    VersionId (string) --VersionId for the specific version of the object to delete.
    
    
    
    
    
    Quiet (boolean) --Element to enable quiet mode for the request. When you add this element, you must set its value to true.
    
    
    
    MFA (string) -- The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device. Required to permanently delete a versioned object if versioning is configured with MFA delete enabled.
    RequestPayer (string) -- Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .
    BypassGovernanceRetention (boolean) -- Specifies whether you want to delete this object even if it has a Governance-type Object Lock in place. You must have sufficient permissions to perform this operation.
    
    """
    pass

def delete_public_access_block(Bucket=None):
    """
    Removes the PublicAccessBlock configuration for an Amazon S3 bucket. To use this operation, you must have the s3:PutBucketPublicAccessBlock permission. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    The following operations are related to DeletePublicAccessBlock :
    See also: AWS API Documentation
    
    
    :example: response = client.delete_public_access_block(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe Amazon S3 bucket whose PublicAccessBlock configuration you want to delete.\n

    """
    pass

def download_file(Bucket=None, Key=None, Filename=None, ExtraArgs=None, Callback=None, Config=None):
    """
    Download an S3 object to a file.
    :
    Similar behavior as S3Transfer\'s download_file() method,
    except that parameters are capitalized. Detailed examples can be found at
    S3Transfer\'s .
    
    :example: import boto3
    s3 = boto3.resource('s3')
    s3.meta.client.download_file('mybucket', 'hello.txt', '/tmp/hello.txt')
    
    
    :type Bucket: str
    :param Bucket: The name of the bucket to download from.

    :type Key: str
    :param Key: The name of the key to download from.

    :type Filename: str
    :param Filename: The path to the file to download to.

    :type ExtraArgs: dict
    :param ExtraArgs: Extra arguments that may be passed to the\nclient operation.

    :type Callback: function
    :param Callback: A method which takes a number of bytes transferred to\nbe periodically called during the download.

    :type Config: boto3.s3.transfer.TransferConfig
    :param Config: The transfer configuration to be used when performing the\ntransfer.

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
    :param Fileobj: A file-like object to download into. At a minimum, it must\nimplement the write method and must accept bytes.

    :type Bucket: str
    :param Bucket: The name of the bucket to download from.

    :type Key: str
    :param Key: The name of the key to download from.

    :type ExtraArgs: dict
    :param ExtraArgs: Extra arguments that may be passed to the\nclient operation.

    :type Callback: function
    :param Callback: A method which takes a number of bytes transferred to\nbe periodically called during the download.

    :type Config: boto3.s3.transfer.TransferConfig
    :param Config: The transfer configuration to be used when performing the\ndownload.

    """
    pass

def generate_presigned_post(Bucket=None, Key=None, Fields=None, Conditions=None, ExpiresIn=None):
    """
    Builds the url and the form fields used for a presigned s3 post
    
    :type Bucket: string
    :param Bucket: The name of the bucket to presign the post to. Note that\nbucket related conditions should not be included in the\nconditions parameter.

    :type Key: string
    :param Key: Key name, optionally add ${filename} to the end to\nattach the submitted filename. Note that key related conditions and\nfields are filled out for you and should not be included in the\nFields or Conditions parameter.

    :type Fields: dict
    :param Fields: A dictionary of prefilled form fields to build on top\nof. Elements that may be included are acl, Cache-Control,\nContent-Type, Content-Disposition, Content-Encoding, Expires,\nsuccess_action_redirect, redirect, success_action_status,\nand x-amz-meta-.\nNote that if a particular element is included in the fields\ndictionary it will not be automatically added to the conditions\nlist. You must specify a condition for the element as well.\n

    :type Conditions: list
    :param Conditions: A list of conditions to include in the policy. Each\nelement can be either a list or a structure. For example:\n\n[\n{'acl': 'public-read'},\n['content-length-range', 2, 5],\n['starts-with', '$success_action_redirect', '']\n\n]\nConditions that are included may pertain to acl,\ncontent-length-range, Cache-Control, Content-Type,\nContent-Disposition, Content-Encoding, Expires,\nsuccess_action_redirect, redirect, success_action_status,\nand/or x-amz-meta-.\nNote that if you include a condition, you must specify\nthe a valid value in the fields dictionary as well. A value will\nnot be added automatically to the fields dictionary based on the\nconditions.\n

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned post\nis valid for.

    :rtype: dict

ReturnsA dictionary with two elements: url and fields.
Url is the url to post to. Fields is a dictionary filled with
the form fields and respective values to use when submitting the
post. For example:

{\'url\': \'https://mybucket.s3.amazonaws.com

\'fields\': {\'acl\': \'public-read\',
\'key\': \'mykey\',
\'signature\': \'mysignature\',
\'policy\': \'mybase64 encoded policy\'}




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

def get_bucket_accelerate_configuration(Bucket=None):
    """
    This implementation of the GET operation uses the accelerate subresource to return the Transfer Acceleration state of a bucket, which is either Enabled or Suspended . Amazon S3 Transfer Acceleration is a bucket-level feature that enables you to perform faster data transfers to and from Amazon S3.
    To use this operation, you must have permission to perform the s3:GetAccelerateConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to your Amazon S3 Resources in the Amazon Simple Storage Service Developer Guide .
    You set the Transfer Acceleration state of an existing bucket to Enabled or Suspended by using the  PutBucketAccelerateConfiguration operation.
    A GET accelerate request does not return a state value for a bucket that has no transfer acceleration state. A bucket has no Transfer Acceleration state if a state has never been set on the bucket.
    For more information about transfer acceleration, see Transfer Acceleration in the Amazon Simple Storage Service Developer Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_accelerate_configuration(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nName of the bucket for which the accelerate configuration is retrieved.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Status': 'Enabled'|'Suspended'
}


Response Structure

(dict) --
Status (string) --The accelerate configuration of the bucket.







    :return: {
        'Status': 'Enabled'|'Suspended'
    }
    
    
    """
    pass

def get_bucket_acl(Bucket=None):
    """
    This implementation of the GET operation uses the acl subresource to return the access control list (ACL) of a bucket. To use GET to return the ACL of the bucket, you must have READ_ACP access to the bucket. If READ_ACP permission is granted to the anonymous user, you can return the ACL of the bucket without using an authorization header.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_acl(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nSpecifies the S3 bucket whose ACL is being requested.\n

    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --
Owner (dict) --Container for the bucket owner\'s display name and ID.

DisplayName (string) --Container for the display name of the owner.

ID (string) --Container for the ID of the owner.



Grants (list) --A list of grants.

(dict) --Container for grant information.

Grantee (dict) --The person being granted permissions.

DisplayName (string) --Screen name of the grantee.

EmailAddress (string) --Email address of the grantee.

Note
Using email addresses to specify a grantee is only supported in the following AWS Regions:

US East (N. Virginia)
US West (N. California)
US West (Oregon)
Asia Pacific (Singapore)
Asia Pacific (Sydney)
Asia Pacific (Tokyo)
Europe (Ireland)
South America (S\xc3\xa3o Paulo)

For a list of all the Amazon S3 supported Regions and endpoints, see Regions and Endpoints in the AWS General Reference.


ID (string) --The canonical user ID of the grantee.

Type (string) --Type of grantee

URI (string) --URI of the grantee group.



Permission (string) --Specifies the permission given to the grantee.











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
    
    
    :returns: 
    US East (N. Virginia)
    US West (N. California)
    US West (Oregon)
    Asia Pacific (Singapore)
    Asia Pacific (Sydney)
    Asia Pacific (Tokyo)
    Europe (Ireland)
    South America (S\xc3\xa3o Paulo)
    
    """
    pass

def get_bucket_analytics_configuration(Bucket=None, Id=None):
    """
    This implementation of the GET operation returns an analytics configuration (identified by the analytics configuration ID) from the bucket.
    To use this operation, you must have permissions to perform the s3:GetAnalyticsConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources in the Amazon Simple Storage Service Developer Guide .
    For information about Amazon S3 analytics feature, see Amazon S3 Analytics \xe2\x80\x93 Storage Class Analysis in the Amazon Simple Storage Service Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_analytics_configuration(
        Bucket='string',
        Id='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket from which an analytics configuration is retrieved.\n

    :type Id: string
    :param Id: [REQUIRED]\nThe ID that identifies the analytics configuration.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

AnalyticsConfiguration (dict) --
The configuration and any analyses for the analytics filter.

Id (string) --
The ID that identifies the analytics configuration.

Filter (dict) --
The filter used to describe a set of objects for analyses. A filter must have exactly one prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be considered in any analysis.

Prefix (string) --
The prefix to use when evaluating an analytics filter.

Tag (dict) --
The tag to use when evaluating an analytics filter.

Key (string) --
Name of the tag.

Value (string) --
Value of the tag.



And (dict) --
A conjunction (logical AND) of predicates, which is used in evaluating an analytics filter. The operator must have at least two predicates.

Prefix (string) --
The prefix to use when evaluating an AND predicate: The prefix that an object must have to be included in the metrics results.

Tags (list) --
The list of tags to use when evaluating an AND predicate.

(dict) --
A container of a key value name pair.

Key (string) --
Name of the tag.

Value (string) --
Value of the tag.









StorageClassAnalysis (dict) --
Contains data related to access patterns to be collected and made available to analyze the tradeoffs between different storage classes.

DataExport (dict) --
Specifies how data related to the storage class analysis for an Amazon S3 bucket should be exported.

OutputSchemaVersion (string) --
The version of the output schema to use when exporting data. Must be V_1 .

Destination (dict) --
The place to store the data for an analysis.

S3BucketDestination (dict) --
A destination signifying output to an S3 bucket.

Format (string) --
Specifies the file format used when exporting data to Amazon S3.

BucketAccountId (string) --
The account ID that owns the destination S3 bucket. If no account ID is provided, the owner is not validated before exporting data.

Note
Although this value is optional, we strongly recommend that you set it to help prevent problems if the destination bucket ownership changes.


Bucket (string) --
The Amazon Resource Name (ARN) of the bucket to which data is exported.

Prefix (string) --
The prefix to use when exporting data. The prefix is prepended to all results.


















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
    Bucket (string) -- [REQUIRED]
    The name of the bucket from which an analytics configuration is retrieved.
    
    Id (string) -- [REQUIRED]
    The ID that identifies the analytics configuration.
    
    
    """
    pass

def get_bucket_cors(Bucket=None):
    """
    Returns the cors configuration information set for the bucket.
    To use this operation, you must have permission to perform the s3:GetBucketCORS action. By default, the bucket owner has this permission and can grant it to others.
    For more information about cors, see Enabling Cross-Origin Resource Sharing .
    The following operations are related to GetBucketCors :
    See also: AWS API Documentation
    
    Examples
    The following example returns cross-origin resource sharing (CORS) configuration set on a bucket.
    Expected Output:
    
    :example: response = client.get_bucket_cors(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name for which to get the cors configuration.\n

    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --
CORSRules (list) --A set of origins and methods (cross-origin access that you want to allow). You can add up to 100 rules to the configuration.

(dict) --Specifies a cross-origin access rule for an Amazon S3 bucket.

AllowedHeaders (list) --Headers that are specified in the Access-Control-Request-Headers header. These headers are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS request, Amazon S3 returns any requested headers that are allowed.

(string) --


AllowedMethods (list) --An HTTP method that you allow the origin to execute. Valid values are GET , PUT , HEAD , POST , and DELETE .

(string) --


AllowedOrigins (list) --One or more origins you want customers to be able to access the bucket from.

(string) --


ExposeHeaders (list) --One or more headers in the response that you want customers to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).

(string) --


MaxAgeSeconds (integer) --The time in seconds that your browser is to cache the preflight response for the specified resource.










Examples
The following example returns cross-origin resource sharing (CORS) configuration set on a bucket.
response = client.get_bucket_cors(
    Bucket='examplebucket',
)

print(response)


Expected Output:
{
    'CORSRules': [
        {
            'AllowedHeaders': [
                'Authorization',
            ],
            'AllowedMethods': [
                'GET',
            ],
            'AllowedOrigins': [
                '*',
            ],
            'MaxAgeSeconds': 3000,
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_bucket_encryption(Bucket=None):
    """
    Returns the default encryption configuration for an Amazon S3 bucket. For information about the Amazon S3 default encryption feature, see Amazon S3 Default Bucket Encryption .
    To use this operation, you must have permission to perform the s3:GetEncryptionConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    The following operations are related to GetBucketEncryption :
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_encryption(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket from which the server-side encryption configuration is retrieved.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ServerSideEncryptionConfiguration': {
        'Rules': [
            {
                'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm': 'AES256'|'aws:kms',
                    'KMSMasterKeyID': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --
ServerSideEncryptionConfiguration (dict) --Specifies the default server-side-encryption configuration.

Rules (list) --Container for information about a particular server-side encryption configuration rule.

(dict) --Specifies the default server-side encryption configuration.

ApplyServerSideEncryptionByDefault (dict) --Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT Object request doesn\'t specify any server-side encryption, this default encryption will be applied.

SSEAlgorithm (string) --Server-side encryption algorithm to use for the default encryption.

KMSMasterKeyID (string) --AWS Key Management Service (KMS) customer master key ID to use for the default encryption. This parameter is allowed if and only if SSEAlgorithm is set to aws:kms .
You can specify the key ID or the Amazon Resource Name (ARN) of the CMK. However, if you are using encryption with cross-account operations, you must use a fully qualified CMK ARN. For more information, see Using encryption for cross-account operations .

For example:

Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab


Warning
Amazon S3 only supports symmetric CMKs and not asymmetric CMKs. For more information, see Using Symmetric and Asymmetric Keys in the AWS Key Management Service Developer Guide .
















    :return: {
        'ServerSideEncryptionConfiguration': {
            'Rules': [
                {
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'AES256'|'aws:kms',
                        'KMSMasterKeyID': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
    Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
    
    """
    pass

def get_bucket_inventory_configuration(Bucket=None, Id=None):
    """
    Returns an inventory configuration (identified by the inventory configuration ID) from the bucket.
    To use this operation, you must have permissions to perform the s3:GetInventoryConfiguration action. The bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    For information about the Amazon S3 inventory feature, see Amazon S3 Inventory .
    The following operations are related to GetBucketInventoryConfiguration :
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_inventory_configuration(
        Bucket='string',
        Id='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket containing the inventory configuration to retrieve.\n

    :type Id: string
    :param Id: [REQUIRED]\nThe ID used to identify the inventory configuration.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'InventoryConfiguration': {
        'Destination': {
            'S3BucketDestination': {
                'AccountId': 'string',
                'Bucket': 'string',
                'Format': 'CSV'|'ORC'|'Parquet',
                'Prefix': 'string',
                'Encryption': {
                    'SSES3': {},
                    'SSEKMS': {
                        'KeyId': 'string'
                    }
                }
            }
        },
        'IsEnabled': True|False,
        'Filter': {
            'Prefix': 'string'
        },
        'Id': 'string',
        'IncludedObjectVersions': 'All'|'Current',
        'OptionalFields': [
            'Size'|'LastModifiedDate'|'StorageClass'|'ETag'|'IsMultipartUploaded'|'ReplicationStatus'|'EncryptionStatus'|'ObjectLockRetainUntilDate'|'ObjectLockMode'|'ObjectLockLegalHoldStatus'|'IntelligentTieringAccessTier',
        ],
        'Schedule': {
            'Frequency': 'Daily'|'Weekly'
        }
    }
}


Response Structure

(dict) --

InventoryConfiguration (dict) --
Specifies the inventory configuration.

Destination (dict) --
Contains information about where to publish the inventory results.

S3BucketDestination (dict) --
Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where inventory results are published.

AccountId (string) --
The account ID that owns the destination S3 bucket. If no account ID is provided, the owner is not validated before exporting data.

Note
Although this value is optional, we strongly recommend that you set it to help prevent problems if the destination bucket ownership changes.


Bucket (string) --
The Amazon Resource Name (ARN) of the bucket where inventory results will be published.

Format (string) --
Specifies the output format of the inventory results.

Prefix (string) --
The prefix that is prepended to all inventory results.

Encryption (dict) --
Contains the type of server-side encryption used to encrypt the inventory results.

SSES3 (dict) --
Specifies the use of SSE-S3 to encrypt delivered inventory reports.

SSEKMS (dict) --
Specifies the use of SSE-KMS to encrypt delivered inventory reports.

KeyId (string) --
Specifies the ID of the AWS Key Management Service (AWS KMS) symmetric customer managed customer master key (CMK) to use for encrypting inventory reports.









IsEnabled (boolean) --
Specifies whether the inventory is enabled or disabled. If set to True , an inventory list is generated. If set to False , no inventory list is generated.

Filter (dict) --
Specifies an inventory filter. The inventory only includes objects that meet the filter\'s criteria.

Prefix (string) --
The prefix that an object must have to be included in the inventory results.



Id (string) --
The ID used to identify the inventory configuration.

IncludedObjectVersions (string) --
Object versions to include in the inventory list. If set to All , the list includes all the object versions, which adds the version-related fields VersionId , IsLatest , and DeleteMarker to the list. If set to Current , the list does not contain these version-related fields.

OptionalFields (list) --
Contains the optional fields that are included in the inventory results.

(string) --


Schedule (dict) --
Specifies the schedule for generating inventory results.

Frequency (string) --
Specifies how frequently inventory results are produced.












    :return: {
        'InventoryConfiguration': {
            'Destination': {
                'S3BucketDestination': {
                    'AccountId': 'string',
                    'Bucket': 'string',
                    'Format': 'CSV'|'ORC'|'Parquet',
                    'Prefix': 'string',
                    'Encryption': {
                        'SSES3': {},
                        'SSEKMS': {
                            'KeyId': 'string'
                        }
                    }
                }
            },
            'IsEnabled': True|False,
            'Filter': {
                'Prefix': 'string'
            },
            'Id': 'string',
            'IncludedObjectVersions': 'All'|'Current',
            'OptionalFields': [
                'Size'|'LastModifiedDate'|'StorageClass'|'ETag'|'IsMultipartUploaded'|'ReplicationStatus'|'EncryptionStatus'|'ObjectLockRetainUntilDate'|'ObjectLockMode'|'ObjectLockLegalHoldStatus'|'IntelligentTieringAccessTier',
            ],
            'Schedule': {
                'Frequency': 'Daily'|'Weekly'
            }
        }
    }
    
    
    :returns: 
    Bucket (string) -- [REQUIRED]
    The name of the bucket containing the inventory configuration to retrieve.
    
    Id (string) -- [REQUIRED]
    The ID used to identify the inventory configuration.
    
    
    """
    pass

def get_bucket_lifecycle(Bucket=None):
    """
    Returns the lifecycle configuration information set on the bucket. For information about lifecycle configuration, see Object Lifecycle Management .
    To use this operation, you must have permission to perform the s3:GetLifecycleConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    The following operations are related to GetBucketLifecycle :
    See also: AWS API Documentation
    
    Examples
    The following example gets ACL on the specified bucket.
    Expected Output:
    
    :example: response = client.get_bucket_lifecycle(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket for which to get the lifecycle information.\n

    :rtype: dict
ReturnsResponse Syntax{
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
                'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
            },
            'NoncurrentVersionTransition': {
                'NoncurrentDays': 123,
                'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
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


Response Structure

(dict) --
Rules (list) --Container for a lifecycle rule.

(dict) --Specifies lifecycle rules for an Amazon S3 bucket. For more information, see Put Bucket Lifecycle Configuration in the Amazon Simple Storage Service API Reference . For examples, see Put Bucket Lifecycle Configuration Examples

Expiration (dict) --Specifies the expiration for the lifecycle of the object.

Date (datetime) --Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.

Days (integer) --Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.

ExpiredObjectDeleteMarker (boolean) --Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.



ID (string) --Unique identifier for the rule. The value can\'t be longer than 255 characters.

Prefix (string) --Object key prefix that identifies one or more objects to which this rule applies.

Status (string) --If Enabled , the rule is currently being applied. If Disabled , the rule is not currently being applied.

Transition (dict) --Specifies when an object transitions to a specified storage class. For more information about Amazon S3 lifecycle configuration rules, see Transitioning Objects Using Amazon S3 Lifecycle in the Amazon Simple Storage Service Developer Guide .

Date (datetime) --Indicates when objects are transitioned to the specified storage class. The date value must be in ISO 8601 format. The time is always midnight UTC.

Days (integer) --Indicates the number of days after creation when objects are transitioned to the specified storage class. The value must be a positive integer.

StorageClass (string) --The storage class to which you want the object to transition.



NoncurrentVersionTransition (dict) --Container for the transition rule that describes when noncurrent objects transition to the STANDARD_IA , ONEZONE_IA , INTELLIGENT_TIERING , GLACIER , or DEEP_ARCHIVE storage class. If your bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to the STANDARD_IA , ONEZONE_IA , INTELLIGENT_TIERING , GLACIER , or DEEP_ARCHIVE storage class at a specific period in the object\'s lifetime.

NoncurrentDays (integer) --Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates How Long an Object Has Been Noncurrent in the Amazon Simple Storage Service Developer Guide .

StorageClass (string) --The class of storage used to store the object.



NoncurrentVersionExpiration (dict) --Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes the noncurrent object versions. You set this lifecycle configuration action on a bucket that has versioning enabled (or suspended) to request that Amazon S3 delete noncurrent object versions at a specific period in the object\'s lifetime.

NoncurrentDays (integer) --Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates When an Object Became Noncurrent in the Amazon Simple Storage Service Developer Guide .



AbortIncompleteMultipartUpload (dict) --Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before permanently removing all parts of the upload. For more information, see Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Policy in the Amazon Simple Storage Service Developer Guide .

DaysAfterInitiation (integer) --Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.












Examples
The following example gets ACL on the specified bucket.
response = client.get_bucket_lifecycle(
    Bucket='acl1',
)

print(response)


Expected Output:
{
    'Rules': [
        {
            'Expiration': {
                'Days': 1,
            },
            'ID': 'delete logs',
            'Prefix': '123/',
            'Status': 'Enabled',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                    'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                },
                'NoncurrentVersionTransition': {
                    'NoncurrentDays': 123,
                    'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
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
    
    
    :returns: 
    GetBucketLifecycleConfiguration
    PutBucketLifecycle
    DeleteBucketLifecycle
    
    """
    pass

def get_bucket_lifecycle_configuration(Bucket=None):
    """
    Returns the lifecycle configuration information set on the bucket. For information about lifecycle configuration, see Object Lifecycle Management .
    To use this operation, you must have permission to perform the s3:GetLifecycleConfiguration action. The bucket owner has this permission, by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    The following operations are related to GetBucketLifecycleConfiguration :
    See also: AWS API Documentation
    
    Examples
    The following example retrieves lifecycle configuration on set on a bucket.
    Expected Output:
    
    :example: response = client.get_bucket_lifecycle_configuration(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket for which to get the lifecycle information.\n

    :rtype: dict
ReturnsResponse Syntax{
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
                    'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                },
            ],
            'NoncurrentVersionTransitions': [
                {
                    'NoncurrentDays': 123,
                    'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
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


Response Structure

(dict) --
Rules (list) --Container for a lifecycle rule.

(dict) --A lifecycle rule for individual objects in an Amazon S3 bucket.

Expiration (dict) --Specifies the expiration for the lifecycle of the object in the form of date, days and, whether the object has a delete marker.

Date (datetime) --Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.

Days (integer) --Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.

ExpiredObjectDeleteMarker (boolean) --Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.



ID (string) --Unique identifier for the rule. The value cannot be longer than 255 characters.

Prefix (string) --Prefix identifying one or more objects to which the rule applies. This is No longer used; use Filter instead.

Filter (dict) --The Filter is used to identify objects that a Lifecycle Rule applies to. A Filter must have exactly one of Prefix , Tag , or And specified.

Prefix (string) --Prefix identifying one or more objects to which the rule applies.

Tag (dict) --This tag must exist in the object\'s tag set in order for the rule to apply.

Key (string) --Name of the tag.

Value (string) --Value of the tag.



And (dict) --This is used in a Lifecycle Rule Filter to apply a logical AND to two or more predicates. The Lifecycle Rule will apply to any object matching all of the predicates configured inside the And operator.

Prefix (string) --Prefix identifying one or more objects to which the rule applies.

Tags (list) --All of these tags must exist in the object\'s tag set in order for the rule to apply.

(dict) --A container of a key value name pair.

Key (string) --Name of the tag.

Value (string) --Value of the tag.









Status (string) --If \'Enabled\', the rule is currently being applied. If \'Disabled\', the rule is not currently being applied.

Transitions (list) --Specifies when an Amazon S3 object transitions to a specified storage class.

(dict) --Specifies when an object transitions to a specified storage class. For more information about Amazon S3 lifecycle configuration rules, see Transitioning Objects Using Amazon S3 Lifecycle in the Amazon Simple Storage Service Developer Guide .

Date (datetime) --Indicates when objects are transitioned to the specified storage class. The date value must be in ISO 8601 format. The time is always midnight UTC.

Days (integer) --Indicates the number of days after creation when objects are transitioned to the specified storage class. The value must be a positive integer.

StorageClass (string) --The storage class to which you want the object to transition.





NoncurrentVersionTransitions (list) --Specifies the transition rule for the lifecycle rule that describes when noncurrent objects transition to a specific storage class. If your bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to a specific storage class at a set period in the object\'s lifetime.

(dict) --Container for the transition rule that describes when noncurrent objects transition to the STANDARD_IA , ONEZONE_IA , INTELLIGENT_TIERING , GLACIER , or DEEP_ARCHIVE storage class. If your bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to the STANDARD_IA , ONEZONE_IA , INTELLIGENT_TIERING , GLACIER , or DEEP_ARCHIVE storage class at a specific period in the object\'s lifetime.

NoncurrentDays (integer) --Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates How Long an Object Has Been Noncurrent in the Amazon Simple Storage Service Developer Guide .

StorageClass (string) --The class of storage used to store the object.





NoncurrentVersionExpiration (dict) --Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes the noncurrent object versions. You set this lifecycle configuration action on a bucket that has versioning enabled (or suspended) to request that Amazon S3 delete noncurrent object versions at a specific period in the object\'s lifetime.

NoncurrentDays (integer) --Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates When an Object Became Noncurrent in the Amazon Simple Storage Service Developer Guide .



AbortIncompleteMultipartUpload (dict) --Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before permanently removing all parts of the upload. For more information, see Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Policy in the Amazon Simple Storage Service Developer Guide .

DaysAfterInitiation (integer) --Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.












Examples
The following example retrieves lifecycle configuration on set on a bucket.
response = client.get_bucket_lifecycle_configuration(
    Bucket='examplebucket',
)

print(response)


Expected Output:
{
    'Rules': [
        {
            'ID': 'Rule for TaxDocs/',
            'Prefix': 'TaxDocs',
            'Status': 'Enabled',
            'Transitions': [
                {
                    'Days': 365,
                    'StorageClass': 'STANDARD_IA',
                },
            ],
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                        'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                    },
                ],
                'NoncurrentVersionTransitions': [
                    {
                        'NoncurrentDays': 123,
                        'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
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
    
    
    :returns: 
    GetBucketLifecycle
    PutBucketLifecycle
    DeleteBucketLifecycle
    
    """
    pass

def get_bucket_location(Bucket=None):
    """
    Returns the Region the bucket resides in. You set the bucket\'s Region using the LocationConstraint request parameter in a CreateBucket request. For more information, see  CreateBucket .
    To use this implementation of the operation, you must be the bucket owner.
    The following operations are related to GetBucketLocation :
    See also: AWS API Documentation
    
    Examples
    The following example returns bucket location.
    Expected Output:
    
    :example: response = client.get_bucket_location(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket for which to get the location.\n

    :rtype: dict
ReturnsResponse Syntax{
    'LocationConstraint': 'EU'|'eu-west-1'|'us-west-1'|'us-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1'|'cn-north-1'|'eu-central-1'
}


Response Structure

(dict) --
LocationConstraint (string) --Specifies the Region where the bucket resides. For a list of all the Amazon S3 supported location constraints by Region, see Regions and Endpoints . Buckets in Region us-east-1 have a LocationConstraint of null .






Examples
The following example returns bucket location.
response = client.get_bucket_location(
    Bucket='examplebucket',
)

print(response)


Expected Output:
{
    'LocationConstraint': 'us-west-2',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LocationConstraint': 'EU'|'eu-west-1'|'us-west-1'|'us-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1'|'cn-north-1'|'eu-central-1'
    }
    
    
    """
    pass

def get_bucket_logging(Bucket=None):
    """
    Returns the logging status of a bucket and the permissions users have to view and modify that status. To use GET, you must be the bucket owner.
    The following operations are related to GetBucketLogging :
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_logging(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name for which to get the logging information.\n

    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --
LoggingEnabled (dict) --Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys for a bucket. For more information, see PUT Bucket logging in the Amazon Simple Storage Service API Reference .

TargetBucket (string) --Specifies the bucket where you want Amazon S3 to store server access logs. You can have your logs delivered to any bucket that you own, including the same bucket that is being logged. You can also configure multiple buckets to deliver their logs to the same target bucket. In this case, you should choose a different TargetPrefix for each source bucket so that the delivered log files can be distinguished by key.

TargetGrants (list) --Container for granting information.

(dict) --Container for granting information.

Grantee (dict) --Container for the person being granted permissions.

DisplayName (string) --Screen name of the grantee.

EmailAddress (string) --Email address of the grantee.

Note
Using email addresses to specify a grantee is only supported in the following AWS Regions:

US East (N. Virginia)
US West (N. California)
US West (Oregon)
Asia Pacific (Singapore)
Asia Pacific (Sydney)
Asia Pacific (Tokyo)
Europe (Ireland)
South America (S\xc3\xa3o Paulo)

For a list of all the Amazon S3 supported Regions and endpoints, see Regions and Endpoints in the AWS General Reference.


ID (string) --The canonical user ID of the grantee.

Type (string) --Type of grantee

URI (string) --URI of the grantee group.



Permission (string) --Logging permissions assigned to the Grantee for the bucket.





TargetPrefix (string) --A prefix for all log object keys. If you store log files from multiple Amazon S3 buckets in a single bucket, you can use a prefix to distinguish which log files came from which bucket.









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
    
    
    :returns: 
    US East (N. Virginia)
    US West (N. California)
    US West (Oregon)
    Asia Pacific (Singapore)
    Asia Pacific (Sydney)
    Asia Pacific (Tokyo)
    Europe (Ireland)
    South America (S\xc3\xa3o Paulo)
    
    """
    pass

def get_bucket_metrics_configuration(Bucket=None, Id=None):
    """
    Gets a metrics configuration (specified by the metrics configuration ID) from the bucket. Note that this doesn\'t include the daily storage metrics.
    To use this operation, you must have permissions to perform the s3:GetMetricsConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    For information about CloudWatch request metrics for Amazon S3, see Monitoring Metrics with Amazon CloudWatch .
    The following operations are related to GetBucketMetricsConfiguration :
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_metrics_configuration(
        Bucket='string',
        Id='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket containing the metrics configuration to retrieve.\n

    :type Id: string
    :param Id: [REQUIRED]\nThe ID used to identify the metrics configuration.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

MetricsConfiguration (dict) --
Specifies the metrics configuration.

Id (string) --
The ID used to identify the metrics configuration.

Filter (dict) --
Specifies a metrics configuration filter. The metrics configuration will only include objects that meet the filter\'s criteria. A filter must be a prefix, a tag, or a conjunction (MetricsAndOperator).

Prefix (string) --
The prefix used when evaluating a metrics filter.

Tag (dict) --
The tag used when evaluating a metrics filter.

Key (string) --
Name of the tag.

Value (string) --
Value of the tag.



And (dict) --
A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The operator must have at least two predicates, and an object must match all of the predicates in order for the filter to apply.

Prefix (string) --
The prefix used when evaluating an AND predicate.

Tags (list) --
The list of tags used when evaluating an AND predicate.

(dict) --
A container of a key value name pair.

Key (string) --
Name of the tag.

Value (string) --
Value of the tag.


















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
    Bucket (string) -- [REQUIRED]
    The name of the bucket containing the metrics configuration to retrieve.
    
    Id (string) -- [REQUIRED]
    The ID used to identify the metrics configuration.
    
    
    """
    pass

def get_bucket_notification(Bucket=None):
    """
    No longer used, see  GetBucketNotificationConfiguration .
    See also: AWS API Documentation
    
    Examples
    The following example returns notification configuration set on a bucket.
    Expected Output:
    
    :example: response = client.get_bucket_notification(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nName of the bucket for which to get the notification configuration.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TopicConfiguration': {
        'Id': 'string',
        'Events': [
            's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
        ],
        'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
        'Topic': 'string'
    },
    'QueueConfiguration': {
        'Id': 'string',
        'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
        'Events': [
            's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
        ],
        'Queue': 'string'
    },
    'CloudFunctionConfiguration': {
        'Id': 'string',
        'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
        'Events': [
            's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
        ],
        'CloudFunction': 'string',
        'InvocationRole': 'string'
    }
}


Response Structure

(dict) --
TopicConfiguration (dict) --This data type is deprecated. A container for specifying the configuration for publication of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.

Id (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.

Events (list) --A collection of events related to objects

(string) --The bucket event for which to send notifications.



Event (string) --Bucket event for which to send notifications.

Topic (string) --Amazon SNS topic to which Amazon S3 will publish a message to report the specified events for the bucket.



QueueConfiguration (dict) --This data type is deprecated. This data type specifies the configuration for publishing messages to an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified events.

Id (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.

Event (string) --The bucket event for which to send notifications.

Events (list) --A collection of bucket events for which to send notifications

(string) --The bucket event for which to send notifications.



Queue (string) --The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message when it detects events of the specified type.



CloudFunctionConfiguration (dict) --Container for specifying the AWS Lambda notification configuration.

Id (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.

Event (string) --The bucket event for which to send notifications.

Events (list) --Bucket events for which to send notifications.

(string) --The bucket event for which to send notifications.



CloudFunction (string) --Lambda cloud function ARN that Amazon S3 can invoke when it detects events of the specified type.

InvocationRole (string) --The role supporting the invocation of the Lambda function








Examples
The following example returns notification configuration set on a bucket.
response = client.get_bucket_notification(
    Bucket='examplebucket',
)

print(response)


Expected Output:
{
    'QueueConfiguration': {
        'Event': 's3:ObjectCreated:Put',
        'Events': [
            's3:ObjectCreated:Put',
        ],
        'Id': 'MDQ2OGQ4NDEtOTBmNi00YTM4LTk0NzYtZDIwN2I3NWQ1NjIx',
        'Queue': 'arn:aws:sqs:us-east-1:acct-id:S3ObjectCreatedEventQueue',
    },
    'TopicConfiguration': {
        'Event': 's3:ObjectCreated:Copy',
        'Events': [
            's3:ObjectCreated:Copy',
        ],
        'Id': 'YTVkMWEzZGUtNTY1NS00ZmE2LWJjYjktMmRlY2QwODFkNTJi',
        'Topic': 'arn:aws:sns:us-east-1:acct-id:S3ObjectCreatedEventTopic',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TopicConfiguration': {
            'Id': 'string',
            'Events': [
                's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
            ],
            'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
            'Topic': 'string'
        },
        'QueueConfiguration': {
            'Id': 'string',
            'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
            'Events': [
                's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
            ],
            'Queue': 'string'
        },
        'CloudFunctionConfiguration': {
            'Id': 'string',
            'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
            'Events': [
                's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
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
    If notifications are not enabled on the bucket, the operation returns an empty NotificationConfiguration element.
    By default, you must be the bucket owner to read the notification configuration of a bucket. However, the bucket owner can use a bucket policy to grant permission to other users to read this configuration with the s3:GetBucketNotification permission.
    For more information about setting and reading the notification configuration on a bucket, see Setting Up Notification of Bucket Events . For more information about bucket policies, see Using Bucket Policies .
    The following operation is related to GetBucketNotification :
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_notification_configuration(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nName of the bucket for which to get the notification configuration.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TopicConfigurations': [
        {
            'Id': 'string',
            'TopicArn': 'string',
            'Events': [
                's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
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
                's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
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
                's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
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


Response Structure

(dict) --A container for specifying the notification configuration of the bucket. If this element is empty, notifications are turned off for the bucket.

TopicConfigurations (list) --The topic to which notifications are sent and the events for which notifications are generated.

(dict) --A container for specifying the configuration for publication of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.

Id (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.

TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to which Amazon S3 publishes a message when it detects events of the specified type.

Events (list) --The Amazon S3 bucket event about which to send notifications. For more information, see Supported Event Types in the Amazon Simple Storage Service Developer Guide .

(string) --The bucket event for which to send notifications.



Filter (dict) --Specifies object key name filtering rules. For information about key name filtering, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .

Key (dict) --A container for object key name prefix and suffix filtering rules.

FilterRules (list) --A list of containers for the key-value pair that defines the criteria for the filter rule.

(dict) --Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.

Name (string) --The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .

Value (string) --The value that the filter searches for in object key names.













QueueConfigurations (list) --The Amazon Simple Queue Service queues to publish messages to and the events for which to publish messages.

(dict) --Specifies the configuration for publishing messages to an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified events.

Id (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.

QueueArn (string) --The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message when it detects events of the specified type.

Events (list) --A collection of bucket events for which to send notifications

(string) --The bucket event for which to send notifications.



Filter (dict) --Specifies object key name filtering rules. For information about key name filtering, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .

Key (dict) --A container for object key name prefix and suffix filtering rules.

FilterRules (list) --A list of containers for the key-value pair that defines the criteria for the filter rule.

(dict) --Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.

Name (string) --The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .

Value (string) --The value that the filter searches for in object key names.













LambdaFunctionConfigurations (list) --Describes the AWS Lambda functions to invoke and the events for which to invoke them.

(dict) --A container for specifying the configuration for AWS Lambda notifications.

Id (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.

LambdaFunctionArn (string) --The Amazon Resource Name (ARN) of the AWS Lambda function that Amazon S3 invokes when the specified event type occurs.

Events (list) --The Amazon S3 bucket event for which to invoke the AWS Lambda function. For more information, see Supported Event Types in the Amazon Simple Storage Service Developer Guide .

(string) --The bucket event for which to send notifications.



Filter (dict) --Specifies object key name filtering rules. For information about key name filtering, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .

Key (dict) --A container for object key name prefix and suffix filtering rules.

FilterRules (list) --A list of containers for the key-value pair that defines the criteria for the filter rule.

(dict) --Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.

Name (string) --The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .

Value (string) --The value that the filter searches for in object key names.



















    :return: {
        'TopicConfigurations': [
            {
                'Id': 'string',
                'TopicArn': 'string',
                'Events': [
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
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
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
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
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
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
    Returns the policy of a specified bucket. If you are using an identity other than the root user of the AWS account that owns the bucket, the calling identity must have the GetBucketPolicy permissions on the specified bucket and belong to the bucket owner\'s account in order to use this operation.
    If you don\'t have GetBucketPolicy permissions, Amazon S3 returns a 403 Access Denied error. If you have the correct permissions, but you\'re not using an identity that belongs to the bucket owner\'s account, Amazon S3 returns a 405 Method Not Allowed error.
    For more information about bucket policies, see Using Bucket Policies and User Policies .
    The following operation is related to GetBucketPolicy :
    See also: AWS API Documentation
    
    Examples
    The following example returns bucket policy associated with a bucket.
    Expected Output:
    
    :example: response = client.get_bucket_policy(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name for which to get the bucket policy.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Policy': 'string'
}


Response Structure

(dict) --
Policy (string) --The bucket policy as a JSON document.






Examples
The following example returns bucket policy associated with a bucket.
response = client.get_bucket_policy(
    Bucket='examplebucket',
)

print(response)


Expected Output:
{
    'Policy': '{"Version":"2008-10-17","Id":"LogPolicy","Statement":[{"Sid":"Enables the log delivery group to publish logs to your bucket ","Effect":"Allow","Principal":{"AWS":"111122223333"},"Action":["s3:GetBucketAcl","s3:GetObjectAcl","s3:PutObject"],"Resource":["arn:aws:s3:::policytest1/*","arn:aws:s3:::policytest1"]}]}',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Policy': 'string'
    }
    
    
    """
    pass

def get_bucket_policy_status(Bucket=None):
    """
    Retrieves the policy status for an Amazon S3 bucket, indicating whether the bucket is public. In order to use this operation, you must have the s3:GetBucketPolicyStatus permission. For more information about Amazon S3 permissions, see Specifying Permissions in a Policy .
    For more information about when Amazon S3 considers a bucket public, see The Meaning of "Public" .
    The following operations are related to GetBucketPolicyStatus :
    See also: AWS API Documentation
    
    
    :example: response = client.get_bucket_policy_status(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the Amazon S3 bucket whose policy status you want to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'PolicyStatus': {
        'IsPublic': True|False
    }
}


Response Structure

(dict) --
PolicyStatus (dict) --The policy status for the specified bucket.

IsPublic (boolean) --The policy status for this bucket. TRUE indicates that this bucket is public. FALSE indicates that the bucket is not public.









    :return: {
        'PolicyStatus': {
            'IsPublic': True|False
        }
    }
    
    
    """
    pass

def get_bucket_replication(Bucket=None):
    """
    Returns the replication configuration of a bucket.
    For information about replication configuration, see Replication in the Amazon Simple Storage Service Developer Guide .
    This operation requires permissions for the s3:GetReplicationConfiguration action. For more information about permissions, see Using Bucket Policies and User Policies .
    If you include the Filter element in a replication configuration, you must also include the DeleteMarkerReplication and Priority elements. The response also returns those elements.
    For information about GetBucketReplication errors, see  ReplicationErrorCodeList
    The following operations are related to GetBucketReplication :
    See also: AWS API Documentation
    
    Examples
    The following example returns replication configuration set on a bucket.
    Expected Output:
    
    :example: response = client.get_bucket_replication(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name for which to get the replication information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ReplicationConfiguration': {
        'Role': 'string',
        'Rules': [
            {
                'ID': 'string',
                'Priority': 123,
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
                'SourceSelectionCriteria': {
                    'SseKmsEncryptedObjects': {
                        'Status': 'Enabled'|'Disabled'
                    }
                },
                'ExistingObjectReplication': {
                    'Status': 'Enabled'|'Disabled'
                },
                'Destination': {
                    'Bucket': 'string',
                    'Account': 'string',
                    'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
                    'AccessControlTranslation': {
                        'Owner': 'Destination'
                    },
                    'EncryptionConfiguration': {
                        'ReplicaKmsKeyID': 'string'
                    },
                    'ReplicationTime': {
                        'Status': 'Enabled'|'Disabled',
                        'Time': {
                            'Minutes': 123
                        }
                    },
                    'Metrics': {
                        'Status': 'Enabled'|'Disabled',
                        'EventThreshold': {
                            'Minutes': 123
                        }
                    }
                },
                'DeleteMarkerReplication': {
                    'Status': 'Enabled'|'Disabled'
                }
            },
        ]
    }
}


Response Structure

(dict) --
ReplicationConfiguration (dict) --A container for replication rules. You can add up to 1,000 rules. The maximum size of a replication configuration is 2 MB.

Role (string) --The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that Amazon S3 assumes when replicating objects. For more information, see How to Set Up Replication in the Amazon Simple Storage Service Developer Guide .

Rules (list) --A container for one or more replication rules. A replication configuration must have at least one rule and can contain a maximum of 1,000 rules.

(dict) --Specifies which Amazon S3 objects to replicate and where to store the replicas.

ID (string) --A unique identifier for the rule. The maximum value is 255 characters.

Priority (integer) --The priority associated with the rule. If you specify multiple rules in a replication configuration, Amazon S3 prioritizes the rules to prevent conflicts when filtering. If two or more rules identify the same object based on a specified filter, the rule with higher priority takes precedence. For example:

Same object quality prefix-based filter criteria if prefixes you specified in multiple rules overlap
Same object qualify tag-based filter criteria specified in multiple rules

For more information, see `Replication < https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html>`__ in the Amazon Simple Storage Service Developer Guide .

Prefix (string) --An object key name prefix that identifies the object or objects to which the rule applies. The maximum prefix length is 1,024 characters. To include all objects in a bucket, specify an empty string.

Filter (dict) --A filter that identifies the subset of objects to which the replication rule applies. A Filter must specify exactly one Prefix , Tag , or an And child element.

Prefix (string) --An object key name prefix that identifies the subset of objects to which the rule applies.

Tag (dict) --A container for specifying a tag key and value.
The rule applies only to objects that have the tag in their tag set.

Key (string) --Name of the tag.

Value (string) --Value of the tag.



And (dict) --A container for specifying rule filters. The filters determine the subset of objects to which the rule applies. This element is required only if you specify more than one filter. For example:

If you specify both a Prefix and a Tag filter, wrap these filters in an And tag.
If you specify a filter based on multiple tags, wrap the Tag elements in an And tag.


Prefix (string) --An object key name prefix that identifies the subset of objects to which the rule applies.

Tags (list) --An array of tags containing key and value pairs.

(dict) --A container of a key value name pair.

Key (string) --Name of the tag.

Value (string) --Value of the tag.









Status (string) --Specifies whether the rule is enabled.

SourceSelectionCriteria (dict) --A container that describes additional filters for identifying the source objects that you want to replicate. You can choose to enable or disable the replication of these objects. Currently, Amazon S3 supports only the filter that you can specify for objects created with server-side encryption using a customer master key (CMK) stored in AWS Key Management Service (SSE-KMS).

SseKmsEncryptedObjects (dict) --A container for filter information for the selection of Amazon S3 objects encrypted with AWS KMS. If you include SourceSelectionCriteria in the replication configuration, this element is required.

Status (string) --Specifies whether Amazon S3 replicates objects created with server-side encryption using a customer master key (CMK) stored in AWS Key Management Service.





ExistingObjectReplication (dict) --
Status (string) --


Destination (dict) --A container for information about the replication destination and its configurations including enabling the S3 Replication Time Control (S3 RTC).

Bucket (string) --The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store the results.

Account (string) --Destination bucket owner account ID. In a cross-account scenario, if you direct Amazon S3 to change replica ownership to the AWS account that owns the destination bucket by specifying the AccessControlTranslation property, this is the account ID of the destination bucket owner. For more information, see Replication Additional Configuration: Changing the Replica Owner in the Amazon Simple Storage Service Developer Guide .

StorageClass (string) --The storage class to use when replicating objects, such as S3 Standard or reduced redundancy. By default, Amazon S3 uses the storage class of the source object to create the object replica.
For valid values, see the StorageClass element of the PUT Bucket replication action in the Amazon Simple Storage Service API Reference .

AccessControlTranslation (dict) --Specify this only in a cross-account scenario (where source and destination bucket owners are not the same), and you want to change replica ownership to the AWS account that owns the destination bucket. If this is not specified in the replication configuration, the replicas are owned by same AWS account that owns the source object.

Owner (string) --Specifies the replica ownership. For default and valid values, see PUT bucket replication in the Amazon Simple Storage Service API Reference .



EncryptionConfiguration (dict) --A container that provides information about encryption. If SourceSelectionCriteria is specified, you must specify this element.

ReplicaKmsKeyID (string) --Specifies the ID (Key ARN or Alias ARN) of the customer managed customer master key (CMK) stored in AWS Key Management Service (KMS) for the destination bucket. Amazon S3 uses this key to encrypt replica objects. Amazon S3 only supports symmetric customer managed CMKs. For more information, see Using Symmetric and Asymmetric Keys in the AWS Key Management Service Developer Guide .



ReplicationTime (dict) --A container specifying S3 Replication Time Control (S3 RTC), including whether S3 RTC is enabled and the time when all objects and operations on objects must be replicated. Must be specified together with a Metrics block.

Status (string) --Specifies whether the replication time is enabled.

Time (dict) --A container specifying the time by which replication should be complete for all objects and operations on objects.

Minutes (integer) --Contains an integer specifying time in minutes.
Valid values: 15 minutes.





Metrics (dict) --A container specifying replication metrics-related settings enabling metrics and Amazon S3 events for S3 Replication Time Control (S3 RTC). Must be specified together with a ReplicationTime block.

Status (string) --Specifies whether the replication metrics are enabled.

EventThreshold (dict) --A container specifying the time threshold for emitting the s3:Replication:OperationMissedThreshold event.

Minutes (integer) --Contains an integer specifying time in minutes.
Valid values: 15 minutes.







DeleteMarkerReplication (dict) --Specifies whether Amazon S3 replicates the delete markers. If you specify a Filter , you must specify this element. However, in the latest version of replication configuration (when Filter is specified), Amazon S3 doesn\'t replicate delete markers. Therefore, the DeleteMarkerReplication element can contain only <Status>Disabled</Status>. For an example configuration, see Basic Rule Configuration .

Note
If you don\'t specify the Filter element, Amazon S3 assumes that the replication configuration is the earlier version, V1. In the earlier version, Amazon S3 handled replication of delete markers differently. For more information, see Backward Compatibility .


Status (string) --Indicates whether to replicate delete markers.

Note
In the current implementation, Amazon S3 doesn\'t replicate the delete markers. The status must be Disabled .















Examples
The following example returns replication configuration set on a bucket.
response = client.get_bucket_replication(
    Bucket='examplebucket',
)

print(response)


Expected Output:
{
    'ReplicationConfiguration': {
        'Role': 'arn:aws:iam::acct-id:role/example-role',
        'Rules': [
            {
                'Destination': {
                    'Bucket': 'arn:aws:s3:::destination-bucket',
                },
                'ID': 'MWIwNTkwZmItMTE3MS00ZTc3LWJkZDEtNzRmODQwYzc1OTQy',
                'Prefix': 'Tax',
                'Status': 'Enabled',
            },
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReplicationConfiguration': {
            'Role': 'string',
            'Rules': [
                {
                    'ID': 'string',
                    'Priority': 123,
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
                    'SourceSelectionCriteria': {
                        'SseKmsEncryptedObjects': {
                            'Status': 'Enabled'|'Disabled'
                        }
                    },
                    'ExistingObjectReplication': {
                        'Status': 'Enabled'|'Disabled'
                    },
                    'Destination': {
                        'Bucket': 'string',
                        'Account': 'string',
                        'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
                        'AccessControlTranslation': {
                            'Owner': 'Destination'
                        },
                        'EncryptionConfiguration': {
                            'ReplicaKmsKeyID': 'string'
                        },
                        'ReplicationTime': {
                            'Status': 'Enabled'|'Disabled',
                            'Time': {
                                'Minutes': 123
                            }
                        },
                        'Metrics': {
                            'Status': 'Enabled'|'Disabled',
                            'EventThreshold': {
                                'Minutes': 123
                            }
                        }
                    },
                    'DeleteMarkerReplication': {
                        'Status': 'Enabled'|'Disabled'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    Same object quality prefix-based filter criteria if prefixes you specified in multiple rules overlap
    Same object qualify tag-based filter criteria specified in multiple rules
    
    """
    pass

def get_bucket_request_payment(Bucket=None):
    """
    Returns the request payment configuration of a bucket. To use this version of the operation, you must be the bucket owner. For more information, see Requester Pays Buckets .
    The following operations are related to GetBucketRequestPayment :
    See also: AWS API Documentation
    
    Examples
    The following example retrieves bucket versioning configuration.
    Expected Output:
    
    :example: response = client.get_bucket_request_payment(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket for which to get the payment request configuration\n

    :rtype: dict
ReturnsResponse Syntax{
    'Payer': 'Requester'|'BucketOwner'
}


Response Structure

(dict) --
Payer (string) --Specifies who pays for the download and request fees.






Examples
The following example retrieves bucket versioning configuration.
response = client.get_bucket_request_payment(
    Bucket='examplebucket',
)

print(response)


Expected Output:
{
    'Payer': 'BucketOwner',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Payer': 'Requester'|'BucketOwner'
    }
    
    
    """
    pass

def get_bucket_tagging(Bucket=None):
    """
    Returns the tag set associated with the bucket.
    To use this operation, you must have permission to perform the s3:GetBucketTagging action. By default, the bucket owner has this permission and can grant this permission to others.
    The following operations are related to GetBucketTagging :
    See also: AWS API Documentation
    
    Examples
    The following example returns tag set associated with a bucket
    Expected Output:
    
    :example: response = client.get_bucket_tagging(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket for which to get the tagging information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TagSet': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
TagSet (list) --Contains the tag set.

(dict) --A container of a key value name pair.

Key (string) --Name of the tag.

Value (string) --Value of the tag.










Examples
The following example returns tag set associated with a bucket
response = client.get_bucket_tagging(
    Bucket='examplebucket',
)

print(response)


Expected Output:
{
    'TagSet': [
        {
            'Key': 'key1',
            'Value': 'value1',
        },
        {
            'Key': 'key2',
            'Value': 'value2',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TagSet': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    PutBucketTagging
    DeleteBucketTagging
    
    """
    pass

def get_bucket_versioning(Bucket=None):
    """
    Returns the versioning state of a bucket.
    To retrieve the versioning state of a bucket, you must be the bucket owner.
    This implementation also returns the MFA Delete status of the versioning state. If the MFA Delete status is enabled , the bucket owner must use an authentication device to change the versioning state of the bucket.
    The following operations are related to GetBucketVersioning :
    See also: AWS API Documentation
    
    Examples
    The following example retrieves bucket versioning configuration.
    Expected Output:
    
    :example: response = client.get_bucket_versioning(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket for which to get the versioning information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Status': 'Enabled'|'Suspended',
    'MFADelete': 'Enabled'|'Disabled'
}


Response Structure

(dict) --
Status (string) --The versioning state of the bucket.

MFADelete (string) --Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned.






Examples
The following example retrieves bucket versioning configuration.
response = client.get_bucket_versioning(
    Bucket='examplebucket',
)

print(response)


Expected Output:
{
    'MFADelete': 'Disabled',
    'Status': 'Enabled',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Status': 'Enabled'|'Suspended',
        'MFADelete': 'Enabled'|'Disabled'
    }
    
    
    """
    pass

def get_bucket_website(Bucket=None):
    """
    Returns the website configuration for a bucket. To host website on Amazon S3, you can configure a bucket as website by adding a website configuration. For more information about hosting websites, see Hosting Websites on Amazon S3 .
    This GET operation requires the S3:GetBucketWebsite permission. By default, only the bucket owner can read the bucket website configuration. However, bucket owners can allow other users to read the website configuration by writing a bucket policy granting them the S3:GetBucketWebsite permission.
    The following operations are related to DeleteBucketWebsite :
    See also: AWS API Documentation
    
    Examples
    The following example retrieves website configuration of a bucket.
    Expected Output:
    
    :example: response = client.get_bucket_website(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name for which to get the website configuration.\n

    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --
RedirectAllRequestsTo (dict) --Specifies the redirect behavior of all requests to a website endpoint of an Amazon S3 bucket.

HostName (string) --Name of the host where requests are redirected.

Protocol (string) --Protocol to use when redirecting requests. The default is the protocol that is used in the original request.



IndexDocument (dict) --The name of the index document for the website (for example index.html ).

Suffix (string) --A suffix that is appended to a request that is for a directory on the website endpoint (for example,if the suffix is index.html and you make a request to samplebucket/images/ the data that is returned will be for the object with the key name images/index.html) The suffix must not be empty and must not include a slash character.



ErrorDocument (dict) --The object key name of the website error document to use for 4XX class errors.

Key (string) --The object key name to use when a 4XX class error occurs.



RoutingRules (list) --Rules that define when a redirect is applied and the redirect behavior.

(dict) --Specifies the redirect behavior and when a redirect is applied.

Condition (dict) --A container for describing a condition that must be met for the specified redirect to apply. For example, 1. If request is for pages in the /docs folder, redirect to the /documents folder. 2. If request results in HTTP error 4xx, redirect request to another host where you might process the error.

HttpErrorCodeReturnedEquals (string) --The HTTP error code when the redirect is applied. In the event of an error, if the error code equals this value, then the specified redirect is applied. Required when parent element Condition is specified and sibling KeyPrefixEquals is not specified. If both are specified, then both must be true for the redirect to be applied.

KeyPrefixEquals (string) --The object key name prefix when the redirect is applied. For example, to redirect requests for ExamplePage.html , the key prefix will be ExamplePage.html . To redirect request for all pages with the prefix docs/ , the key prefix will be /docs , which identifies all objects in the docs/ folder. Required when the parent element Condition is specified and sibling HttpErrorCodeReturnedEquals is not specified. If both conditions are specified, both must be true for the redirect to be applied.



Redirect (dict) --Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can specify a different error code to return.

HostName (string) --The host name to use in the redirect request.

HttpRedirectCode (string) --The HTTP redirect code to use on the response. Not required if one of the siblings is present.

Protocol (string) --Protocol to use when redirecting requests. The default is the protocol that is used in the original request.

ReplaceKeyPrefixWith (string) --The object key prefix to use in the redirect request. For example, to redirect requests for all pages with prefix docs/ (objects in the docs/ folder) to documents/ , you can set a condition block with KeyPrefixEquals set to docs/ and in the Redirect set ReplaceKeyPrefixWith to /documents . Not required if one of the siblings is present. Can be present only if ReplaceKeyWith is not provided.

ReplaceKeyWith (string) --The specific object key to use in the redirect request. For example, redirect request to error.html . Not required if one of the siblings is present. Can be present only if ReplaceKeyPrefixWith is not provided.












Examples
The following example retrieves website configuration of a bucket.
response = client.get_bucket_website(
    Bucket='examplebucket',
)

print(response)


Expected Output:
{
    'ErrorDocument': {
        'Key': 'error.html',
    },
    'IndexDocument': {
        'Suffix': 'index.html',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    Retrieves objects from Amazon S3. To use GET , you must have READ access to the object. If you grant READ access to the anonymous user, you can return the object without using an authorization header.
    An Amazon S3 bucket has no directory hierarchy such as you would find in a typical computer file system. You can, however, create a logical hierarchy by using object key names that imply a folder structure. For example, instead of naming an object sample.jpg , you can name it photos/2006/February/sample.jpg .
    To get an object from such a logical hierarchy, specify the full key name for the object in the GET operation. For a virtual hosted-style request example, if you have the object photos/2006/February/sample.jpg , specify the resource as /photos/2006/February/sample.jpg . For a path-style request example, if you have the object photos/2006/February/sample.jpg in the bucket named examplebucket , specify the resource as /examplebucket/photos/2006/February/sample.jpg . For more information about request types, see HTTP Host Header Bucket Specification .
    To distribute large files to many people, you can save bandwidth costs by using BitTorrent. For more information, see Amazon S3 Torrent . For more information about returning the ACL of an object, see  GetObjectAcl .
    If the object you are retrieving is stored in the GLACIER or DEEP_ARCHIVE storage classes, before you can retrieve the object you must first restore a copy using . Otherwise, this operation returns an InvalidObjectStateError error. For information about restoring archived objects, see Restoring Archived Objects .
    Encryption request headers, like x-amz-server-side-encryption , should not be sent for GET requests if your object uses server-side encryption with CMKs stored in AWS KMS (SSE-KMS) or server-side encryption with Amazon S3\xe2\x80\x93managed encryption keys (SSE-S3). If your object does use these types of keys, you\xe2\x80\x99ll get an HTTP 400 BadRequest error.
    If you encrypt an object by using server-side encryption with customer-provided encryption keys (SSE-C) when you store the object in Amazon S3, then when you GET the object, you must use the following headers:
    For more information about SSE-C, see Server-Side Encryption (Using Customer-Provided Encryption Keys) .
    Assuming you have permission to read object tags (permission for the s3:GetObjectVersionTagging action), the response also returns the x-amz-tagging-count header that provides the count of number of tags associated with the object. You can use  GetObjectTagging to retrieve the tag set associated with an object.
    You need the s3:GetObject permission for this operation. For more information, see Specifying Permissions in a Policy . If the object you request does not exist, the error Amazon S3 returns depends on whether you also have the s3:ListBucket permission.
    By default, the GET operation returns the current version of an object. To return a different version, use the versionId subresource.
    For more information about versioning, see  PutBucketVersioning .
    There are times when you want to override certain response header values in a GET response. For example, you might override the Content-Disposition response header value in your GET request.
    You can override values for a set of response headers using the following query parameters. These response header values are sent only on a successful request, that is, when status code 200 OK is returned. The set of headers you can override using these parameters is a subset of the headers that Amazon S3 accepts when you create an object. The response headers that you can override for the GET response are Content-Type , Content-Language , Expires , Cache-Control , Content-Disposition , and Content-Encoding . To override these header values in the GET response, you use the following request parameters.
    If both of the If-Match and If-Unmodified-Since headers are present in the request as follows: If-Match condition evaluates to true , and; If-Unmodified-Since condition evaluates to false ; then, S3 returns 200 OK and the data requested.
    If both of the If-None-Match and If-Modified-Since headers are present in the request as follows:If-None-Match condition evaluates to false , and; If-Modified-Since condition evaluates to true ; then, S3 returns 304 Not Modified response code.
    For more information about conditional requests, see RFC 7232 .
    The following operations are related to GetObject :
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example retrieves an object for an S3 bucket.
    Expected Output:
    The following example retrieves an object for an S3 bucket. The request specifies the range header to retrieve a specific byte range.
    Expected Output:
    
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
    :param Bucket: [REQUIRED]\nThe bucket name containing the object.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type IfMatch: string
    :param IfMatch: Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).

    :type IfModifiedSince: datetime
    :param IfModifiedSince: Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).

    :type IfNoneMatch: string
    :param IfNoneMatch: Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).

    :type IfUnmodifiedSince: datetime
    :param IfUnmodifiedSince: Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).

    :type Key: string
    :param Key: [REQUIRED]\nKey of the object to get.\n

    :type Range: string
    :param Range: Downloads the specified range bytes of an object. For more information about the HTTP Range header, see https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35 .\n\nNote\nAmazon S3 doesn\'t support retrieving multiple ranges of data per GET request.\n\n

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
    :param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (for example, AES256).

    :type SSECustomerKey: string
    :param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side\xe2\x80\x8b-encryption\xe2\x80\x8b-customer-algorithm header.

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.\n\nPlease note that this parameter is automatically populated if it is not provided. Including this parameter is not required\n

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :type PartNumber: integer
    :param PartNumber: Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a \'ranged\' GET request for the part specified. Useful for downloading just a part of an object.

    :rtype: dict

ReturnsResponse Syntax
{
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
    'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
    'RequestCharged': 'requester',
    'ReplicationStatus': 'COMPLETE'|'PENDING'|'FAILED'|'REPLICA',
    'PartsCount': 123,
    'TagCount': 123,
    'ObjectLockMode': 'GOVERNANCE'|'COMPLIANCE',
    'ObjectLockRetainUntilDate': datetime(2015, 1, 1),
    'ObjectLockLegalHoldStatus': 'ON'|'OFF'
}


Response Structure

(dict) --

Body (StreamingBody) --
Object data.

DeleteMarker (boolean) --
Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If false, this response header does not appear in the response.

AcceptRanges (string) --
Indicates that a range of bytes was specified.

Expiration (string) --
If the object expiration is configured (see PUT Bucket lifecycle), the response includes this header. It includes the expiry-date and rule-id key-value pairs providing object expiration information. The value of the rule-id is URL encoded.

Restore (string) --
Provides information about object restoration operation and expiration time of the restored object copy.

LastModified (datetime) --
Last modified date of the object

ContentLength (integer) --
Size of the body in bytes.

ETag (string) --
An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL.

MissingMeta (integer) --
This is set to the number of metadata entries not returned in x-amz-meta headers. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.

VersionId (string) --
Version of the object.

CacheControl (string) --
Specifies caching behavior along the request/reply chain.

ContentDisposition (string) --
Specifies presentational information for the object.

ContentEncoding (string) --
Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

ContentLanguage (string) --
The language the content is in.

ContentRange (string) --
The portion of the object returned in the response.

ContentType (string) --
A standard MIME type describing the format of the object data.

Expires (datetime) --
The date and time at which the object is no longer cacheable.

WebsiteRedirectLocation (string) --
If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.

ServerSideEncryption (string) --
The server-side encryption algorithm used when storing this object in Amazon S3 (for example, AES256, aws:kms).

Metadata (dict) --
A map of metadata to store with the object in S3.

(string) --
(string) --




SSECustomerAlgorithm (string) --
If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.

SSECustomerKeyMD5 (string) --
If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round-trip message integrity verification of the customer-provided encryption key.

SSEKMSKeyId (string) --
If present, specifies the ID of the AWS Key Management Service (AWS KMS) symmetric customer managed customer master key (CMK) that was used for the object.

StorageClass (string) --
Provides storage class information of the object. Amazon S3 returns this header for all objects except for S3 Standard storage class objects.

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.

ReplicationStatus (string) --
Amazon S3 can return this if your request involves a bucket that is either a source or destination in a replication rule.

PartsCount (integer) --
The count of parts this object has.

TagCount (integer) --
The number of tags, if any, on the object.

ObjectLockMode (string) --
The Object Lock mode currently in place for this object.

ObjectLockRetainUntilDate (datetime) --
The date and time when this object\'s Object Lock will expire.

ObjectLockLegalHoldStatus (string) --
Indicates whether this object has an active legal hold. This field is only returned if you have permission to view an object\'s legal hold status.







Exceptions

S3.Client.exceptions.NoSuchKey

Examples
The following example retrieves an object for an S3 bucket.
response = client.get_object(
    Bucket='examplebucket',
    Key='HappyFace.jpg',
)

print(response)


Expected Output:
{
    'AcceptRanges': 'bytes',
    'ContentLength': '3191',
    'ContentType': 'image/jpeg',
    'ETag': '"6805f2cfc46c0f04559748bb039d69ae"',
    'LastModified': datetime(2016, 12, 15, 1, 19, 41, 3, 350, 0),
    'Metadata': {
    },
    'TagCount': 2,
    'VersionId': 'null',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example retrieves an object for an S3 bucket. The request specifies the range header to retrieve a specific byte range.
response = client.get_object(
    Bucket='examplebucket',
    Key='SampleFile.txt',
    Range='bytes=0-9',
)

print(response)


Expected Output:
{
    'AcceptRanges': 'bytes',
    'ContentLength': '10',
    'ContentRange': 'bytes 0-9/43',
    'ContentType': 'text/plain',
    'ETag': '"0d94420ffd0bc68cd3d152506b97a9cc"',
    'LastModified': datetime(2014, 10, 9, 22, 57, 28, 3, 282, 0),
    'Metadata': {
    },
    'VersionId': 'null',
    'ResponseMetadata': {
        '...': '...',
    },
}



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
        'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
        'RequestCharged': 'requester',
        'ReplicationStatus': 'COMPLETE'|'PENDING'|'FAILED'|'REPLICA',
        'PartsCount': 123,
        'TagCount': 123,
        'ObjectLockMode': 'GOVERNANCE'|'COMPLIANCE',
        'ObjectLockRetainUntilDate': datetime(2015, 1, 1),
        'ObjectLockLegalHoldStatus': 'ON'|'OFF'
    }
    
    
    :returns: 
    If you have the s3:ListBucket permission on the bucket, Amazon S3 will return an HTTP status code 404 ("no such key") error.
    If you don\xe2\x80\x99t have the s3:ListBucket permission, Amazon S3 will return an HTTP status code 403 ("access denied") error.
    
    """
    pass

def get_object_acl(Bucket=None, Key=None, VersionId=None, RequestPayer=None):
    """
    Returns the access control list (ACL) of an object. To use this operation, you must have READ_ACP access to the object.
    By default, GET returns ACL information about the current version of an object. To return ACL information about a different version, use the versionId subresource.
    The following operations are related to GetObjectAcl :
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example retrieves access control list (ACL) of an object.
    Expected Output:
    
    :example: response = client.get_object_acl(
        Bucket='string',
        Key='string',
        VersionId='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name that contains the object for which to get the ACL information.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Key: string
    :param Key: [REQUIRED]\nThe key of the object for which to get the ACL information.\n

    :type VersionId: string
    :param VersionId: VersionId used to reference a specific version of the object.

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Owner (dict) --
Container for the bucket owner\'s display name and ID.

DisplayName (string) --
Container for the display name of the owner.

ID (string) --
Container for the ID of the owner.



Grants (list) --
A list of grants.

(dict) --
Container for grant information.

Grantee (dict) --
The person being granted permissions.

DisplayName (string) --
Screen name of the grantee.

EmailAddress (string) --
Email address of the grantee.

Note
Using email addresses to specify a grantee is only supported in the following AWS Regions:

US East (N. Virginia)
US West (N. California)
US West (Oregon)
Asia Pacific (Singapore)
Asia Pacific (Sydney)
Asia Pacific (Tokyo)
Europe (Ireland)
South America (S\xc3\xa3o Paulo)

For a list of all the Amazon S3 supported Regions and endpoints, see Regions and Endpoints in the AWS General Reference.


ID (string) --
The canonical user ID of the grantee.

Type (string) --
Type of grantee

URI (string) --
URI of the grantee group.



Permission (string) --
Specifies the permission given to the grantee.





RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.







Exceptions

S3.Client.exceptions.NoSuchKey

Examples
The following example retrieves access control list (ACL) of an object.
response = client.get_object_acl(
    Bucket='examplebucket',
    Key='HappyFace.jpg',
)

print(response)


Expected Output:
{
    'Grants': [
        {
            'Grantee': {
                'DisplayName': 'owner-display-name',
                'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
                'Type': 'CanonicalUser',
            },
            'Permission': 'WRITE',
        },
        {
            'Grantee': {
                'DisplayName': 'owner-display-name',
                'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
                'Type': 'CanonicalUser',
            },
            'Permission': 'WRITE_ACP',
        },
        {
            'Grantee': {
                'DisplayName': 'owner-display-name',
                'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
                'Type': 'CanonicalUser',
            },
            'Permission': 'READ',
        },
        {
            'Grantee': {
                'DisplayName': 'owner-display-name',
                'ID': '852b113eexamplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
                'Type': 'CanonicalUser',
            },
            'Permission': 'READ_ACP',
        },
    ],
    'Owner': {
        'DisplayName': 'owner-display-name',
        'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    Bucket (string) -- [REQUIRED]
    The bucket name that contains the object for which to get the ACL information.
    When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
    
    Key (string) -- [REQUIRED]
    The key of the object for which to get the ACL information.
    
    VersionId (string) -- VersionId used to reference a specific version of the object.
    RequestPayer (string) -- Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .
    
    """
    pass

def get_object_legal_hold(Bucket=None, Key=None, VersionId=None, RequestPayer=None):
    """
    Gets an object\'s current Legal Hold status. For more information, see Locking Objects .
    See also: AWS API Documentation
    
    
    :example: response = client.get_object_legal_hold(
        Bucket='string',
        Key='string',
        VersionId='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name containing the object whose Legal Hold status you want to retrieve.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Key: string
    :param Key: [REQUIRED]\nThe key name for the object whose Legal Hold status you want to retrieve.\n

    :type VersionId: string
    :param VersionId: The version ID of the object whose Legal Hold status you want to retrieve.

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :rtype: dict

ReturnsResponse Syntax
{
    'LegalHold': {
        'Status': 'ON'|'OFF'
    }
}


Response Structure

(dict) --

LegalHold (dict) --
The current Legal Hold status for the specified object.

Status (string) --
Indicates whether the specified object has a Legal Hold in place.










    :return: {
        'LegalHold': {
            'Status': 'ON'|'OFF'
        }
    }
    
    
    """
    pass

def get_object_lock_configuration(Bucket=None):
    """
    Gets the Object Lock configuration for a bucket. The rule specified in the Object Lock configuration will be applied by default to every new object placed in the specified bucket. For more information, see Locking Objects .
    See also: AWS API Documentation
    
    
    :example: response = client.get_object_lock_configuration(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket whose Object Lock configuration you want to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ObjectLockConfiguration': {
        'ObjectLockEnabled': 'Enabled',
        'Rule': {
            'DefaultRetention': {
                'Mode': 'GOVERNANCE'|'COMPLIANCE',
                'Days': 123,
                'Years': 123
            }
        }
    }
}


Response Structure

(dict) --
ObjectLockConfiguration (dict) --The specified bucket\'s Object Lock configuration.

ObjectLockEnabled (string) --Indicates whether this bucket has an Object Lock configuration enabled.

Rule (dict) --The Object Lock rule in place for the specified object.

DefaultRetention (dict) --The default retention period that you want to apply to new objects placed in the specified bucket.

Mode (string) --The default Object Lock retention mode you want to apply to new objects placed in the specified bucket.

Days (integer) --The number of days that you want to specify for the default retention period.

Years (integer) --The number of years that you want to specify for the default retention period.













    :return: {
        'ObjectLockConfiguration': {
            'ObjectLockEnabled': 'Enabled',
            'Rule': {
                'DefaultRetention': {
                    'Mode': 'GOVERNANCE'|'COMPLIANCE',
                    'Days': 123,
                    'Years': 123
                }
            }
        }
    }
    
    
    """
    pass

def get_object_retention(Bucket=None, Key=None, VersionId=None, RequestPayer=None):
    """
    Retrieves an object\'s retention settings. For more information, see Locking Objects .
    See also: AWS API Documentation
    
    
    :example: response = client.get_object_retention(
        Bucket='string',
        Key='string',
        VersionId='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name containing the object whose retention settings you want to retrieve.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Key: string
    :param Key: [REQUIRED]\nThe key name for the object whose retention settings you want to retrieve.\n

    :type VersionId: string
    :param VersionId: The version ID for the object whose retention settings you want to retrieve.

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :rtype: dict

ReturnsResponse Syntax
{
    'Retention': {
        'Mode': 'GOVERNANCE'|'COMPLIANCE',
        'RetainUntilDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Retention (dict) --
The container element for an object\'s retention settings.

Mode (string) --
Indicates the Retention mode for the specified object.

RetainUntilDate (datetime) --
The date on which this Object Lock Retention will expire.










    :return: {
        'Retention': {
            'Mode': 'GOVERNANCE'|'COMPLIANCE',
            'RetainUntilDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_object_tagging(Bucket=None, Key=None, VersionId=None):
    """
    Returns the tag-set of an object. You send the GET request against the tagging subresource associated with the object.
    To use this operation, you must have permission to perform the s3:GetObjectTagging action. By default, the GET operation returns information about current version of an object. For a versioned bucket, you can have multiple versions of an object in your bucket. To retrieve tags of any other version, use the versionId query parameter. You also need permission for the s3:GetObjectVersionTagging action.
    By default, the bucket owner has this permission and can grant this permission to others.
    For information about the Amazon S3 object tagging feature, see Object Tagging .
    The following operation is related to GetObjectTagging :
    See also: AWS API Documentation
    
    Examples
    The following example retrieves tag set of an object.
    Expected Output:
    The following example retrieves tag set of an object. The request specifies object version.
    Expected Output:
    
    :example: response = client.get_object_tagging(
        Bucket='string',
        Key='string',
        VersionId='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name containing the object for which to get the tagging information.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Key: string
    :param Key: [REQUIRED]\nObject key for which to get the tagging information.\n

    :type VersionId: string
    :param VersionId: The versionId of the object for which to get the tagging information.

    :rtype: dict

ReturnsResponse Syntax
{
    'VersionId': 'string',
    'TagSet': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --

VersionId (string) --
The versionId of the object for which you got the tagging information.

TagSet (list) --
Contains the tag set.

(dict) --
A container of a key value name pair.

Key (string) --
Name of the tag.

Value (string) --
Value of the tag.











Examples
The following example retrieves tag set of an object.
response = client.get_object_tagging(
    Bucket='examplebucket',
    Key='HappyFace.jpg',
)

print(response)


Expected Output:
{
    'TagSet': [
        {
            'Key': 'Key4',
            'Value': 'Value4',
        },
        {
            'Key': 'Key3',
            'Value': 'Value3',
        },
    ],
    'VersionId': 'null',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example retrieves tag set of an object. The request specifies object version.
response = client.get_object_tagging(
    Bucket='examplebucket',
    Key='exampleobject',
    VersionId='ydlaNkwWm0SfKJR.T1b1fIdPRbldTYRI',
)

print(response)


Expected Output:
{
    'TagSet': [
        {
            'Key': 'Key1',
            'Value': 'Value1',
        },
    ],
    'VersionId': 'ydlaNkwWm0SfKJR.T1b1fIdPRbldTYRI',
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    Bucket (string) -- [REQUIRED]
    The bucket name containing the object for which to get the tagging information.
    When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
    
    Key (string) -- [REQUIRED]
    Object key for which to get the tagging information.
    
    VersionId (string) -- The versionId of the object for which to get the tagging information.
    
    """
    pass

def get_object_torrent(Bucket=None, Key=None, RequestPayer=None):
    """
    Return torrent files from a bucket. BitTorrent can save you bandwidth when you\'re distributing large files. For more information about BitTorrent, see Amazon S3 Torrent .
    To use GET, you must have READ access to the object.
    The following operation is related to GetObjectTorrent :
    See also: AWS API Documentation
    
    Examples
    The following example retrieves torrent files of an object.
    Expected Output:
    
    :example: response = client.get_object_torrent(
        Bucket='string',
        Key='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket containing the object for which to get the torrent files.\n

    :type Key: string
    :param Key: [REQUIRED]\nThe object key for which to get the information.\n

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :rtype: dict

ReturnsResponse Syntax
{
    'Body': StreamingBody(),
    'RequestCharged': 'requester'
}


Response Structure

(dict) --

Body (StreamingBody) --
A Bencoded dictionary as defined by the BitTorrent specification

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.







Examples
The following example retrieves torrent files of an object.
response = client.get_object_torrent(
    Bucket='examplebucket',
    Key='HappyFace.jpg',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Body': StreamingBody(),
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    Bucket (string) -- [REQUIRED]
    The name of the bucket containing the object for which to get the torrent files.
    
    Key (string) -- [REQUIRED]
    The object key for which to get the information.
    
    RequestPayer (string) -- Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .
    
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

def get_public_access_block(Bucket=None):
    """
    Retrieves the PublicAccessBlock configuration for an Amazon S3 bucket. To use this operation, you must have the s3:GetBucketPublicAccessBlock permission. For more information about Amazon S3 permissions, see Specifying Permissions in a Policy .
    For more information about when Amazon S3 considers a bucket or an object public, see The Meaning of "Public" .
    The following operations are related to GetPublicAccessBlock :
    See also: AWS API Documentation
    
    
    :example: response = client.get_public_access_block(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the Amazon S3 bucket whose PublicAccessBlock configuration you want to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'PublicAccessBlockConfiguration': {
        'BlockPublicAcls': True|False,
        'IgnorePublicAcls': True|False,
        'BlockPublicPolicy': True|False,
        'RestrictPublicBuckets': True|False
    }
}


Response Structure

(dict) --
PublicAccessBlockConfiguration (dict) --The PublicAccessBlock configuration currently in effect for this Amazon S3 bucket.

BlockPublicAcls (boolean) --Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket and objects in this bucket. Setting this element to TRUE causes the following behavior:

PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
PUT Object calls fail if the request includes a public ACL.
PUT Bucket calls fail if the request includes a public ACL.

Enabling this setting doesn\'t affect existing policies or ACLs.

IgnorePublicAcls (boolean) --Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket. Setting this element to TRUE causes Amazon S3 to ignore all public ACLs on this bucket and objects in this bucket.
Enabling this setting doesn\'t affect the persistence of any existing ACLs and doesn\'t prevent new public ACLs from being set.

BlockPublicPolicy (boolean) --Specifies whether Amazon S3 should block public bucket policies for this bucket. Setting this element to TRUE causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.
Enabling this setting doesn\'t affect existing bucket policies.

RestrictPublicBuckets (boolean) --Specifies whether Amazon S3 should restrict public bucket policies for this bucket. Setting this element to TRUE restricts access to this bucket to only AWS services and authorized users within this account if the bucket has a public policy.
Enabling this setting doesn\'t affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.









    :return: {
        'PublicAccessBlockConfiguration': {
            'BlockPublicAcls': True|False,
            'IgnorePublicAcls': True|False,
            'BlockPublicPolicy': True|False,
            'RestrictPublicBuckets': True|False
        }
    }
    
    
    :returns: 
    PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
    PUT Object calls fail if the request includes a public ACL.
    PUT Bucket calls fail if the request includes a public ACL.
    
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

def head_bucket(Bucket=None):
    """
    This operation is useful to determine if a bucket exists and you have permission to access it. The operation returns a 200 OK if the bucket exists and you have permission to access it. Otherwise, the operation might return responses such as 404 Not Found and 403 Forbidden .
    To use this operation, you must have permissions to perform the s3:ListBucket action. The bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation checks to see if a bucket exists.
    Expected Output:
    
    :example: response = client.head_bucket(
        Bucket='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name.\n

    :return: response = client.head_bucket(
        Bucket='acl1',
    )
    
    print(response)
    
    
    """
    pass

def head_object(Bucket=None, IfMatch=None, IfModifiedSince=None, IfNoneMatch=None, IfUnmodifiedSince=None, Key=None, Range=None, VersionId=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, RequestPayer=None, PartNumber=None):
    """
    The HEAD operation retrieves metadata from an object without returning the object itself. This operation is useful if you\'re only interested in an object\'s metadata. To use HEAD, you must have READ access to the object.
    A HEAD request has the same options as a GET operation on an object. The response is identical to the GET response except that there is no response body.
    If you encrypt an object by using server-side encryption with customer-provided encryption keys (SSE-C) when you store the object in Amazon S3, then when you retrieve the metadata from the object, you must use the following headers:
    For more information about SSE-C, see Server-Side Encryption (Using Customer-Provided Encryption Keys) .
    Request headers are limited to 8 KB in size. For more information, see Common Request Headers .
    Consider the following when using request headers:
    Then Amazon S3 returns 200 OK and the data requested.
    Then Amazon S3 returns the 304 Not Modified response code.
    For more information about conditional requests, see RFC 7232 .
    You need the s3:GetObject permission for this operation. For more information, see Specifying Permissions in a Policy . If the object you request does not exist, the error Amazon S3 returns depends on whether you also have the s3:ListBucket permission.
    The following operation is related to HeadObject :
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example retrieves an object metadata.
    Expected Output:
    
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
    :param Bucket: [REQUIRED]\nThe name of the bucket containing the object.\n

    :type IfMatch: string
    :param IfMatch: Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).

    :type IfModifiedSince: datetime
    :param IfModifiedSince: Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).

    :type IfNoneMatch: string
    :param IfNoneMatch: Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).

    :type IfUnmodifiedSince: datetime
    :param IfUnmodifiedSince: Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).

    :type Key: string
    :param Key: [REQUIRED]\nThe object key.\n

    :type Range: string
    :param Range: Downloads the specified range bytes of an object. For more information about the HTTP Range header, see `http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35 .\n\nNote\nAmazon S3 doesn\'t support retrieving multiple ranges of data per GET request.\n\n

    :type VersionId: string
    :param VersionId: VersionId used to reference a specific version of the object.

    :type SSECustomerAlgorithm: string
    :param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (for example, AES256).

    :type SSECustomerKey: string
    :param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side\xe2\x80\x8b-encryption\xe2\x80\x8b-customer-algorithm header.

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.\n\nPlease note that this parameter is automatically populated if it is not provided. Including this parameter is not required\n

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :type PartNumber: integer
    :param PartNumber: Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a \'ranged\' HEAD request for the part specified. Useful querying about the size of the part and the number of parts in this object.

    :rtype: dict

ReturnsResponse Syntax
{
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
    'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
    'RequestCharged': 'requester',
    'ReplicationStatus': 'COMPLETE'|'PENDING'|'FAILED'|'REPLICA',
    'PartsCount': 123,
    'ObjectLockMode': 'GOVERNANCE'|'COMPLIANCE',
    'ObjectLockRetainUntilDate': datetime(2015, 1, 1),
    'ObjectLockLegalHoldStatus': 'ON'|'OFF'
}


Response Structure

(dict) --

DeleteMarker (boolean) --
Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If false, this response header does not appear in the response.

AcceptRanges (string) --
Indicates that a range of bytes was specified.

Expiration (string) --
If the object expiration is configured (see PUT Bucket lifecycle), the response includes this header. It includes the expiry-date and rule-id key-value pairs providing object expiration information. The value of the rule-id is URL encoded.

Restore (string) --
If the object is an archived object (an object whose storage class is GLACIER), the response includes this header if either the archive restoration is in progress (see  RestoreObject or an archive copy is already restored.
If an archive copy is already restored, the header value indicates when Amazon S3 is scheduled to delete the object copy. For example:

x-amz-restore: ongoing-request="false", expiry-date="Fri, 23 Dec 2012 00:00:00 GMT"

If the object restoration is in progress, the header returns the value ongoing-request="true" .
For more information about archiving objects, see Transitioning Objects: General Considerations .

LastModified (datetime) --
Last modified date of the object

ContentLength (integer) --
Size of the body in bytes.

ETag (string) --
An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL.

MissingMeta (integer) --
This is set to the number of metadata entries not returned in x-amz-meta headers. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.

VersionId (string) --
Version of the object.

CacheControl (string) --
Specifies caching behavior along the request/reply chain.

ContentDisposition (string) --
Specifies presentational information for the object.

ContentEncoding (string) --
Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

ContentLanguage (string) --
The language the content is in.

ContentType (string) --
A standard MIME type describing the format of the object data.

Expires (datetime) --
The date and time at which the object is no longer cacheable.

WebsiteRedirectLocation (string) --
If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.

ServerSideEncryption (string) --
If the object is stored using server-side encryption either with an AWS KMS customer master key (CMK) or an Amazon S3-managed encryption key, the response includes this header with the value of the server-side encryption algorithm used when storing this object in Amazon S3 (for example, AES256, aws:kms).

Metadata (dict) --
A map of metadata to store with the object in S3.

(string) --
(string) --




SSECustomerAlgorithm (string) --
If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.

SSECustomerKeyMD5 (string) --
If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round-trip message integrity verification of the customer-provided encryption key.

SSEKMSKeyId (string) --
If present, specifies the ID of the AWS Key Management Service (AWS KMS) symmetric customer managed customer master key (CMK) that was used for the object.

StorageClass (string) --
Provides storage class information of the object. Amazon S3 returns this header for all objects except for S3 Standard storage class objects.
For more information, see Storage Classes .

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.

ReplicationStatus (string) --
Amazon S3 can return this header if your request involves a bucket that is either a source or destination in a replication rule.
In replication, you have a source bucket on which you configure replication and destination bucket where Amazon S3 stores object replicas. When you request an object (GetObject ) or object metadata (HeadObject ) from these buckets, Amazon S3 will return the x-amz-replication-status header in the response as follows:

If requesting an object from the source bucket \xe2\x80\x94 Amazon S3 will return the x-amz-replication-status header if the object in your request is eligible for replication. For example, suppose that in your replication configuration, you specify object prefix TaxDocs requesting Amazon S3 to replicate objects with key prefix TaxDocs . Any objects you upload with this key name prefix, for example TaxDocs/document1.pdf , are eligible for replication. For any object request with this key name prefix, Amazon S3 will return the x-amz-replication-status header with value PENDING, COMPLETED or FAILED indicating object replication status.
If requesting an object from the destination bucket \xe2\x80\x94 Amazon S3 will return the x-amz-replication-status header with value REPLICA if the object in your request is a replica that Amazon S3 created.

For more information, see Replication .

PartsCount (integer) --
The count of parts this object has.

ObjectLockMode (string) --
The Object Lock mode, if any, that\'s in effect for this object. This header is only returned if the requester has the s3:GetObjectRetention permission. For more information about S3 Object Lock, see Object Lock .

ObjectLockRetainUntilDate (datetime) --
The date and time when the Object Lock retention period expires. This header is only returned if the requester has the s3:GetObjectRetention permission.

ObjectLockLegalHoldStatus (string) --
Specifies whether a legal hold is in effect for this object. This header is only returned if the requester has the s3:GetObjectLegalHold permission. This header is not returned if the specified version of this object has never had a legal hold applied. For more information about S3 Object Lock, see Object Lock .







Exceptions

S3.Client.exceptions.NoSuchKey

Examples
The following example retrieves an object metadata.
response = client.head_object(
    Bucket='examplebucket',
    Key='HappyFace.jpg',
)

print(response)


Expected Output:
{
    'AcceptRanges': 'bytes',
    'ContentLength': '3191',
    'ContentType': 'image/jpeg',
    'ETag': '"6805f2cfc46c0f04559748bb039d69ae"',
    'LastModified': datetime(2016, 12, 15, 1, 19, 41, 3, 350, 0),
    'Metadata': {
    },
    'VersionId': 'null',
    'ResponseMetadata': {
        '...': '...',
    },
}



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
        'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
        'RequestCharged': 'requester',
        'ReplicationStatus': 'COMPLETE'|'PENDING'|'FAILED'|'REPLICA',
        'PartsCount': 123,
        'ObjectLockMode': 'GOVERNANCE'|'COMPLIANCE',
        'ObjectLockRetainUntilDate': datetime(2015, 1, 1),
        'ObjectLockLegalHoldStatus': 'ON'|'OFF'
    }
    
    
    :returns: 
    Consideration 1 \xe2\x80\x93 If both of the If-Match and If-Unmodified-Since headers are present in the request as follows:
    If-Match condition evaluates to true , and;
    If-Unmodified-Since condition evaluates to false ;
    
    
    
    """
    pass

def list_bucket_analytics_configurations(Bucket=None, ContinuationToken=None):
    """
    Lists the analytics configurations for the bucket. You can have up to 1,000 analytics configurations per bucket.
    This operation supports list pagination and does not return more than 100 configurations at a time. You should always check the IsTruncated element in the response. If there are no more configurations to list, IsTruncated is set to false. If there are more configurations to list, IsTruncated is set to true, and there will be a value in NextContinuationToken . You use the NextContinuationToken value to continue the pagination of the list by passing the value in continuation-token in the request to GET the next page.
    To use this operation, you must have permissions to perform the s3:GetAnalyticsConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    For information about Amazon S3 analytics feature, see Amazon S3 Analytics \xe2\x80\x93 Storage Class Analysis .
    The following operations are related to ListBucketAnalyticsConfigurations :
    See also: AWS API Documentation
    
    
    :example: response = client.list_bucket_analytics_configurations(
        Bucket='string',
        ContinuationToken='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket from which analytics configurations are retrieved.\n

    :type ContinuationToken: string
    :param ContinuationToken: The ContinuationToken that represents a placeholder from where this request should begin.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

IsTruncated (boolean) --
Indicates whether the returned list of analytics configurations is complete. A value of true indicates that the list is not complete and the NextContinuationToken will be provided for a subsequent request.

ContinuationToken (string) --
The marker that is used as a starting point for this analytics configuration list response. This value is present if it was sent in the request.

NextContinuationToken (string) --

NextContinuationToken is sent when isTruncated is true, which indicates that there are more analytics configurations to list. The next request must include this NextContinuationToken . The token is obfuscated and is not a usable value.


AnalyticsConfigurationList (list) --
The list of analytics configurations for a bucket.

(dict) --
Specifies the configuration and any analyses for the analytics filter of an Amazon S3 bucket.

Id (string) --
The ID that identifies the analytics configuration.

Filter (dict) --
The filter used to describe a set of objects for analyses. A filter must have exactly one prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be considered in any analysis.

Prefix (string) --
The prefix to use when evaluating an analytics filter.

Tag (dict) --
The tag to use when evaluating an analytics filter.

Key (string) --
Name of the tag.

Value (string) --
Value of the tag.



And (dict) --
A conjunction (logical AND) of predicates, which is used in evaluating an analytics filter. The operator must have at least two predicates.

Prefix (string) --
The prefix to use when evaluating an AND predicate: The prefix that an object must have to be included in the metrics results.

Tags (list) --
The list of tags to use when evaluating an AND predicate.

(dict) --
A container of a key value name pair.

Key (string) --
Name of the tag.

Value (string) --
Value of the tag.









StorageClassAnalysis (dict) --
Contains data related to access patterns to be collected and made available to analyze the tradeoffs between different storage classes.

DataExport (dict) --
Specifies how data related to the storage class analysis for an Amazon S3 bucket should be exported.

OutputSchemaVersion (string) --
The version of the output schema to use when exporting data. Must be V_1 .

Destination (dict) --
The place to store the data for an analysis.

S3BucketDestination (dict) --
A destination signifying output to an S3 bucket.

Format (string) --
Specifies the file format used when exporting data to Amazon S3.

BucketAccountId (string) --
The account ID that owns the destination S3 bucket. If no account ID is provided, the owner is not validated before exporting data.

Note
Although this value is optional, we strongly recommend that you set it to help prevent problems if the destination bucket ownership changes.


Bucket (string) --
The Amazon Resource Name (ARN) of the bucket to which data is exported.

Prefix (string) --
The prefix to use when exporting data. The prefix is prepended to all results.




















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
    Bucket (string) -- [REQUIRED]
    The name of the bucket from which analytics configurations are retrieved.
    
    ContinuationToken (string) -- The ContinuationToken that represents a placeholder from where this request should begin.
    
    """
    pass

def list_bucket_inventory_configurations(Bucket=None, ContinuationToken=None):
    """
    Returns a list of inventory configurations for the bucket. You can have up to 1,000 analytics configurations per bucket.
    This operation supports list pagination and does not return more than 100 configurations at a time. Always check the IsTruncated element in the response. If there are no more configurations to list, IsTruncated is set to false. If there are more configurations to list, IsTruncated is set to true, and there is a value in NextContinuationToken . You use the NextContinuationToken value to continue the pagination of the list by passing the value in continuation-token in the request to GET the next page.
    To use this operation, you must have permissions to perform the s3:GetInventoryConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    For information about the Amazon S3 inventory feature, see Amazon S3 Inventory
    The following operations are related to ListBucketInventoryConfigurations :
    See also: AWS API Documentation
    
    
    :example: response = client.list_bucket_inventory_configurations(
        Bucket='string',
        ContinuationToken='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket containing the inventory configurations to retrieve.\n

    :type ContinuationToken: string
    :param ContinuationToken: The marker used to continue an inventory configuration listing that has been truncated. Use the NextContinuationToken from a previously truncated list response to continue the listing. The continuation token is an opaque value that Amazon S3 understands.

    :rtype: dict

ReturnsResponse Syntax
{
    'ContinuationToken': 'string',
    'InventoryConfigurationList': [
        {
            'Destination': {
                'S3BucketDestination': {
                    'AccountId': 'string',
                    'Bucket': 'string',
                    'Format': 'CSV'|'ORC'|'Parquet',
                    'Prefix': 'string',
                    'Encryption': {
                        'SSES3': {},
                        'SSEKMS': {
                            'KeyId': 'string'
                        }
                    }
                }
            },
            'IsEnabled': True|False,
            'Filter': {
                'Prefix': 'string'
            },
            'Id': 'string',
            'IncludedObjectVersions': 'All'|'Current',
            'OptionalFields': [
                'Size'|'LastModifiedDate'|'StorageClass'|'ETag'|'IsMultipartUploaded'|'ReplicationStatus'|'EncryptionStatus'|'ObjectLockRetainUntilDate'|'ObjectLockMode'|'ObjectLockLegalHoldStatus'|'IntelligentTieringAccessTier',
            ],
            'Schedule': {
                'Frequency': 'Daily'|'Weekly'
            }
        },
    ],
    'IsTruncated': True|False,
    'NextContinuationToken': 'string'
}


Response Structure

(dict) --

ContinuationToken (string) --
If sent in the request, the marker that is used as a starting point for this inventory configuration list response.

InventoryConfigurationList (list) --
The list of inventory configurations for a bucket.

(dict) --
Specifies the inventory configuration for an Amazon S3 bucket. For more information, see GET Bucket inventory in the Amazon Simple Storage Service API Reference .

Destination (dict) --
Contains information about where to publish the inventory results.

S3BucketDestination (dict) --
Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where inventory results are published.

AccountId (string) --
The account ID that owns the destination S3 bucket. If no account ID is provided, the owner is not validated before exporting data.

Note
Although this value is optional, we strongly recommend that you set it to help prevent problems if the destination bucket ownership changes.


Bucket (string) --
The Amazon Resource Name (ARN) of the bucket where inventory results will be published.

Format (string) --
Specifies the output format of the inventory results.

Prefix (string) --
The prefix that is prepended to all inventory results.

Encryption (dict) --
Contains the type of server-side encryption used to encrypt the inventory results.

SSES3 (dict) --
Specifies the use of SSE-S3 to encrypt delivered inventory reports.

SSEKMS (dict) --
Specifies the use of SSE-KMS to encrypt delivered inventory reports.

KeyId (string) --
Specifies the ID of the AWS Key Management Service (AWS KMS) symmetric customer managed customer master key (CMK) to use for encrypting inventory reports.









IsEnabled (boolean) --
Specifies whether the inventory is enabled or disabled. If set to True , an inventory list is generated. If set to False , no inventory list is generated.

Filter (dict) --
Specifies an inventory filter. The inventory only includes objects that meet the filter\'s criteria.

Prefix (string) --
The prefix that an object must have to be included in the inventory results.



Id (string) --
The ID used to identify the inventory configuration.

IncludedObjectVersions (string) --
Object versions to include in the inventory list. If set to All , the list includes all the object versions, which adds the version-related fields VersionId , IsLatest , and DeleteMarker to the list. If set to Current , the list does not contain these version-related fields.

OptionalFields (list) --
Contains the optional fields that are included in the inventory results.

(string) --


Schedule (dict) --
Specifies the schedule for generating inventory results.

Frequency (string) --
Specifies how frequently inventory results are produced.







IsTruncated (boolean) --
Tells whether the returned list of inventory configurations is complete. A value of true indicates that the list is not complete and the NextContinuationToken is provided for a subsequent request.

NextContinuationToken (string) --
The marker used to continue this inventory configuration listing. Use the NextContinuationToken from this response to continue the listing in a subsequent request. The continuation token is an opaque value that Amazon S3 understands.








    :return: {
        'ContinuationToken': 'string',
        'InventoryConfigurationList': [
            {
                'Destination': {
                    'S3BucketDestination': {
                        'AccountId': 'string',
                        'Bucket': 'string',
                        'Format': 'CSV'|'ORC'|'Parquet',
                        'Prefix': 'string',
                        'Encryption': {
                            'SSES3': {},
                            'SSEKMS': {
                                'KeyId': 'string'
                            }
                        }
                    }
                },
                'IsEnabled': True|False,
                'Filter': {
                    'Prefix': 'string'
                },
                'Id': 'string',
                'IncludedObjectVersions': 'All'|'Current',
                'OptionalFields': [
                    'Size'|'LastModifiedDate'|'StorageClass'|'ETag'|'IsMultipartUploaded'|'ReplicationStatus'|'EncryptionStatus'|'ObjectLockRetainUntilDate'|'ObjectLockMode'|'ObjectLockLegalHoldStatus'|'IntelligentTieringAccessTier',
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
    Bucket (string) -- [REQUIRED]
    The name of the bucket containing the inventory configurations to retrieve.
    
    ContinuationToken (string) -- The marker used to continue an inventory configuration listing that has been truncated. Use the NextContinuationToken from a previously truncated list response to continue the listing. The continuation token is an opaque value that Amazon S3 understands.
    
    """
    pass

def list_bucket_metrics_configurations(Bucket=None, ContinuationToken=None):
    """
    Lists the metrics configurations for the bucket. The metrics configurations are only for the request metrics of the bucket and do not provide information on daily storage metrics. You can have up to 1,000 configurations per bucket.
    This operation supports list pagination and does not return more than 100 configurations at a time. Always check the IsTruncated element in the response. If there are no more configurations to list, IsTruncated is set to false. If there are more configurations to list, IsTruncated is set to true, and there is a value in NextContinuationToken . You use the NextContinuationToken value to continue the pagination of the list by passing the value in continuation-token in the request to GET the next page.
    To use this operation, you must have permissions to perform the s3:GetMetricsConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    For more information about metrics configurations and CloudWatch request metrics, see Monitoring Metrics with Amazon CloudWatch .
    The following operations are related to ListBucketMetricsConfigurations :
    See also: AWS API Documentation
    
    
    :example: response = client.list_bucket_metrics_configurations(
        Bucket='string',
        ContinuationToken='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket containing the metrics configurations to retrieve.\n

    :type ContinuationToken: string
    :param ContinuationToken: The marker that is used to continue a metrics configuration listing that has been truncated. Use the NextContinuationToken from a previously truncated list response to continue the listing. The continuation token is an opaque value that Amazon S3 understands.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

IsTruncated (boolean) --
Indicates whether the returned list of metrics configurations is complete. A value of true indicates that the list is not complete and the NextContinuationToken will be provided for a subsequent request.

ContinuationToken (string) --
The marker that is used as a starting point for this metrics configuration list response. This value is present if it was sent in the request.

NextContinuationToken (string) --
The marker used to continue a metrics configuration listing that has been truncated. Use the NextContinuationToken from a previously truncated list response to continue the listing. The continuation token is an opaque value that Amazon S3 understands.

MetricsConfigurationList (list) --
The list of metrics configurations for a bucket.

(dict) --
Specifies a metrics configuration for the CloudWatch request metrics (specified by the metrics configuration ID) from an Amazon S3 bucket. If you\'re updating an existing metrics configuration, note that this is a full replacement of the existing metrics configuration. If you don\'t include the elements you want to keep, they are erased. For more information, see PUT Bucket metrics in the Amazon Simple Storage Service API Reference .

Id (string) --
The ID used to identify the metrics configuration.

Filter (dict) --
Specifies a metrics configuration filter. The metrics configuration will only include objects that meet the filter\'s criteria. A filter must be a prefix, a tag, or a conjunction (MetricsAndOperator).

Prefix (string) --
The prefix used when evaluating a metrics filter.

Tag (dict) --
The tag used when evaluating a metrics filter.

Key (string) --
Name of the tag.

Value (string) --
Value of the tag.



And (dict) --
A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The operator must have at least two predicates, and an object must match all of the predicates in order for the filter to apply.

Prefix (string) --
The prefix used when evaluating an AND predicate.

Tags (list) --
The list of tags used when evaluating an AND predicate.

(dict) --
A container of a key value name pair.

Key (string) --
Name of the tag.

Value (string) --
Value of the tag.




















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
    Bucket (string) -- [REQUIRED]
    The name of the bucket containing the metrics configurations to retrieve.
    
    ContinuationToken (string) -- The marker that is used to continue a metrics configuration listing that has been truncated. Use the NextContinuationToken from a previously truncated list response to continue the listing. The continuation token is an opaque value that Amazon S3 understands.
    
    """
    pass

def list_buckets():
    """
    Returns a list of all buckets owned by the authenticated sender of the request.
    See also: AWS API Documentation
    
    
    :example: response = client.list_buckets()
    
    
    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --
Buckets (list) --The list of buckets owned by the requestor.

(dict) --In terms of implementation, a Bucket is a resource. An Amazon S3 bucket name is globally unique, and the namespace is shared by all AWS accounts.

Name (string) --The name of the bucket.

CreationDate (datetime) --Date the bucket was created.





Owner (dict) --The owner of the buckets listed.

DisplayName (string) --Container for the display name of the owner.

ID (string) --Container for the ID of the owner.









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
    This operation lists in-progress multipart uploads. An in-progress multipart upload is a multipart upload that has been initiated using the Initiate Multipart Upload request, but has not yet been completed or aborted.
    This operation returns at most 1,000 multipart uploads in the response. 1,000 multipart uploads is the maximum number of uploads a response can include, which is also the default value. You can further limit the number of uploads in a response by specifying the max-uploads parameter in the response. If additional multipart uploads satisfy the list criteria, the response will contain an IsTruncated element with the value true. To list the additional multipart uploads, use the key-marker and upload-id-marker request parameters.
    In the response, the uploads are sorted by key. If your application has initiated more than one multipart upload using the same object key, then uploads in the response are first sorted by key. Additionally, uploads are sorted in ascending order within each key by the upload initiation time.
    For more information on multipart uploads, see Uploading Objects Using Multipart Upload .
    For information on permissions required to use the multipart upload API, see Multipart Upload API and Permissions .
    The following operations are related to ListMultipartUploads :
    See also: AWS API Documentation
    
    Examples
    The following example lists in-progress multipart uploads on a specific bucket.
    Expected Output:
    The following example specifies the upload-id-marker and key-marker from previous truncated response to retrieve next setup of multipart uploads.
    Expected Output:
    
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
    :param Bucket: [REQUIRED]\nName of the bucket to which the multipart upload was initiated.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Delimiter: string
    :param Delimiter: Character you use to group keys.\nAll keys that contain the same string between the prefix, if specified, and the first occurrence of the delimiter after the prefix are grouped under a single result element, CommonPrefixes . If you don\'t specify the prefix parameter, then the substring starts at the beginning of the key. The keys that are grouped under CommonPrefixes result element are not returned elsewhere in the response.\n

    :type EncodingType: string
    :param EncodingType: Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.

    :type KeyMarker: string
    :param KeyMarker: Together with upload-id-marker, this parameter specifies the multipart upload after which listing should begin.\nIf upload-id-marker is not specified, only the keys lexicographically greater than the specified key-marker will be included in the list.\nIf upload-id-marker is specified, any multipart uploads for a key equal to the key-marker might also be included, provided those multipart uploads have upload IDs lexicographically greater than the specified upload-id-marker .\n

    :type MaxUploads: integer
    :param MaxUploads: Sets the maximum number of multipart uploads, from 1 to 1,000, to return in the response body. 1,000 is the maximum number of uploads that can be returned in a response.

    :type Prefix: string
    :param Prefix: Lists in-progress uploads only for those keys that begin with the specified prefix. You can use prefixes to separate a bucket into different grouping of keys. (You can think of using prefix to make groups in the same way you\'d use a folder in a file system.)

    :type UploadIdMarker: string
    :param UploadIdMarker: Together with key-marker, specifies the multipart upload after which listing should begin. If key-marker is not specified, the upload-id-marker parameter is ignored. Otherwise, any multipart uploads for a key equal to the key-marker might be included in the list only if they have an upload ID lexicographically greater than the specified upload-id-marker .

    :rtype: dict

ReturnsResponse Syntax
{
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
            'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
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


Response Structure

(dict) --

Bucket (string) --
Name of the bucket to which the multipart upload was initiated.

KeyMarker (string) --
The key at or after which the listing began.

UploadIdMarker (string) --
Upload ID after which listing began.

NextKeyMarker (string) --
When a list is truncated, this element specifies the value that should be used for the key-marker request parameter in a subsequent request.

Prefix (string) --
When a prefix is provided in the request, this field contains the specified prefix. The result contains only keys starting with the specified prefix.

Delimiter (string) --
Contains the delimiter you specified in the request. If you don\'t specify a delimiter in your request, this element is absent from the response.

NextUploadIdMarker (string) --
When a list is truncated, this element specifies the value that should be used for the upload-id-marker request parameter in a subsequent request.

MaxUploads (integer) --
Maximum number of multipart uploads that could have been included in the response.

IsTruncated (boolean) --
Indicates whether the returned list of multipart uploads is truncated. A value of true indicates that the list was truncated. The list can be truncated if the number of multipart uploads exceeds the limit allowed or specified by max uploads.

Uploads (list) --
Container for elements related to a particular multipart upload. A response can contain zero or more Upload elements.

(dict) --
Container for the MultipartUpload for the Amazon S3 object.

UploadId (string) --
Upload ID that identifies the multipart upload.

Key (string) --
Key of the object for which the multipart upload was initiated.

Initiated (datetime) --
Date and time at which the multipart upload was initiated.

StorageClass (string) --
The class of storage used to store the object.

Owner (dict) --
Specifies the owner of the object that is part of the multipart upload.

DisplayName (string) --
Container for the display name of the owner.

ID (string) --
Container for the ID of the owner.



Initiator (dict) --
Identifies who initiated the multipart upload.

ID (string) --
If the principal is an AWS account, it provides the Canonical User ID. If the principal is an IAM User, it provides a user ARN value.

DisplayName (string) --
Name of the Principal.







CommonPrefixes (list) --
If you specify a delimiter in the request, then the result returns each distinct key prefix containing the delimiter in a CommonPrefixes element. The distinct key prefixes are returned in the Prefix child element.

(dict) --
Container for all (if there are any) keys between Prefix and the next occurrence of the string specified by a delimiter. CommonPrefixes lists keys that act like subdirectories in the directory specified by Prefix. For example, if the prefix is notes/ and the delimiter is a slash (/) as in notes/summer/july, the common prefix is notes/summer/.

Prefix (string) --
Container for the specified common prefix.





EncodingType (string) --
Encoding type used by Amazon S3 to encode object keys in the response.
If you specify encoding-type request parameter, Amazon S3 includes this element in the response, and returns encoded key name values in the following response elements:

Delimiter , KeyMarker , Prefix , NextKeyMarker , Key .








Examples
The following example lists in-progress multipart uploads on a specific bucket.
response = client.list_multipart_uploads(
    Bucket='examplebucket',
)

print(response)


Expected Output:
{
    'Uploads': [
        {
            'Initiated': datetime(2014, 5, 1, 5, 40, 58, 3, 121, 0),
            'Initiator': {
                'DisplayName': 'display-name',
                'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
            },
            'Key': 'JavaFile',
            'Owner': {
                'DisplayName': 'display-name',
                'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
            },
            'StorageClass': 'STANDARD',
            'UploadId': 'examplelUa.CInXklLQtSMJITdUnoZ1Y5GACB5UckOtspm5zbDMCkPF_qkfZzMiFZ6dksmcnqxJyIBvQMG9X9Q--',
        },
        {
            'Initiated': datetime(2014, 5, 1, 5, 41, 27, 3, 121, 0),
            'Initiator': {
                'DisplayName': 'display-name',
                'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
            },
            'Key': 'JavaFile',
            'Owner': {
                'DisplayName': 'display-name',
                'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
            },
            'StorageClass': 'STANDARD',
            'UploadId': 'examplelo91lv1iwvWpvCiJWugw2xXLPAD7Z8cJyX9.WiIRgNrdG6Ldsn.9FtS63TCl1Uf5faTB.1U5Ckcbmdw--',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example specifies the upload-id-marker and key-marker from previous truncated response to retrieve next setup of multipart uploads.
response = client.list_multipart_uploads(
    Bucket='examplebucket',
    KeyMarker='nextkeyfrompreviousresponse',
    MaxUploads='2',
    UploadIdMarker='valuefrompreviousresponse',
)

print(response)


Expected Output:
{
    'Bucket': 'acl1',
    'IsTruncated': True,
    'KeyMarker': '',
    'MaxUploads': '2',
    'NextKeyMarker': 'someobjectkey',
    'NextUploadIdMarker': 'examplelo91lv1iwvWpvCiJWugw2xXLPAD7Z8cJyX9.WiIRgNrdG6Ldsn.9FtS63TCl1Uf5faTB.1U5Ckcbmdw--',
    'UploadIdMarker': '',
    'Uploads': [
        {
            'Initiated': datetime(2014, 5, 1, 5, 40, 58, 3, 121, 0),
            'Initiator': {
                'DisplayName': 'ownder-display-name',
                'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
            },
            'Key': 'JavaFile',
            'Owner': {
                'DisplayName': 'mohanataws',
                'ID': '852b113e7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
            },
            'StorageClass': 'STANDARD',
            'UploadId': 'gZ30jIqlUa.CInXklLQtSMJITdUnoZ1Y5GACB5UckOtspm5zbDMCkPF_qkfZzMiFZ6dksmcnqxJyIBvQMG9X9Q--',
        },
        {
            'Initiated': datetime(2014, 5, 1, 5, 41, 27, 3, 121, 0),
            'Initiator': {
                'DisplayName': 'ownder-display-name',
                'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
            },
            'Key': 'JavaFile',
            'Owner': {
                'DisplayName': 'ownder-display-name',
                'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
            },
            'StorageClass': 'STANDARD',
            'UploadId': 'b7tZSqIlo91lv1iwvWpvCiJWugw2xXLPAD7Z8cJyX9.WiIRgNrdG6Ldsn.9FtS63TCl1Uf5faTB.1U5Ckcbmdw--',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
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
    Bucket (string) -- [REQUIRED]
    Name of the bucket to which the multipart upload was initiated.
    When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
    
    Delimiter (string) -- Character you use to group keys.
    All keys that contain the same string between the prefix, if specified, and the first occurrence of the delimiter after the prefix are grouped under a single result element, CommonPrefixes . If you don\'t specify the prefix parameter, then the substring starts at the beginning of the key. The keys that are grouped under CommonPrefixes result element are not returned elsewhere in the response.
    
    EncodingType (string) -- Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.
    KeyMarker (string) -- Together with upload-id-marker, this parameter specifies the multipart upload after which listing should begin.
    If upload-id-marker is not specified, only the keys lexicographically greater than the specified key-marker will be included in the list.
    If upload-id-marker is specified, any multipart uploads for a key equal to the key-marker might also be included, provided those multipart uploads have upload IDs lexicographically greater than the specified upload-id-marker .
    
    MaxUploads (integer) -- Sets the maximum number of multipart uploads, from 1 to 1,000, to return in the response body. 1,000 is the maximum number of uploads that can be returned in a response.
    Prefix (string) -- Lists in-progress uploads only for those keys that begin with the specified prefix. You can use prefixes to separate a bucket into different grouping of keys. (You can think of using prefix to make groups in the same way you\'d use a folder in a file system.)
    UploadIdMarker (string) -- Together with key-marker, specifies the multipart upload after which listing should begin. If key-marker is not specified, the upload-id-marker parameter is ignored. Otherwise, any multipart uploads for a key equal to the key-marker might be included in the list only if they have an upload ID lexicographically greater than the specified upload-id-marker .
    
    """
    pass

def list_object_versions(Bucket=None, Delimiter=None, EncodingType=None, KeyMarker=None, MaxKeys=None, Prefix=None, VersionIdMarker=None):
    """
    Returns metadata about all of the versions of objects in a bucket. You can also use request parameters as selection criteria to return metadata about a subset of all the object versions.
    To use this operation, you must have READ access to the bucket.
    The following operations are related to ListObjectVersions :
    See also: AWS API Documentation
    
    Examples
    The following example return versions of an object with specific key name prefix. The request limits the number of items returned to two. If there are are more than two object version, S3 returns NextToken in the response. You can specify this token value in your next request to fetch next set of object versions.
    Expected Output:
    
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
    :param Bucket: [REQUIRED]\nThe bucket name that contains the objects.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Delimiter: string
    :param Delimiter: A delimiter is a character that you specify to group keys. All keys that contain the same string between the prefix and the first occurrence of the delimiter are grouped under a single result element in CommonPrefixes. These groups are counted as one result against the max-keys limitation. These keys are not returned elsewhere in the response.

    :type EncodingType: string
    :param EncodingType: Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.

    :type KeyMarker: string
    :param KeyMarker: Specifies the key to start with when listing objects in a bucket.

    :type MaxKeys: integer
    :param MaxKeys: Sets the maximum number of keys returned in the response. By default the API returns up to 1,000 key names. The response might contain fewer keys but will never contain more. If additional keys satisfy the search criteria, but were not returned because max-keys was exceeded, the response contains <isTruncated>true</isTruncated>. To return the additional keys, see key-marker and version-id-marker.

    :type Prefix: string
    :param Prefix: Use this parameter to select only those keys that begin with the specified prefix. You can use prefixes to separate a bucket into different groupings of keys. (You can think of using prefix to make groups in the same way you\'d use a folder in a file system.) You can use prefix with delimiter to roll up numerous objects into a single result under CommonPrefixes.

    :type VersionIdMarker: string
    :param VersionIdMarker: Specifies the object version you want to start listing from.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

IsTruncated (boolean) --
A flag that indicates whether Amazon S3 returned all of the results that satisfied the search criteria. If your results were truncated, you can make a follow-up paginated request using the NextKeyMarker and NextVersionIdMarker response parameters as a starting place in another request to return the rest of the results.

KeyMarker (string) --
Marks the last key returned in a truncated response.

VersionIdMarker (string) --
Marks the last version of the key returned in a truncated response.

NextKeyMarker (string) --
When the number of responses exceeds the value of MaxKeys , NextKeyMarker specifies the first key not returned that satisfies the search criteria. Use this value for the key-marker request parameter in a subsequent request.

NextVersionIdMarker (string) --
When the number of responses exceeds the value of MaxKeys , NextVersionIdMarker specifies the first object version not returned that satisfies the search criteria. Use this value for the version-id-marker request parameter in a subsequent request.

Versions (list) --
Container for version information.

(dict) --
The version of an object.

ETag (string) --
The entity tag is an MD5 hash of that version of the object.

Size (integer) --
Size in bytes of the object.

StorageClass (string) --
The class of storage used to store the object.

Key (string) --
The object key.

VersionId (string) --
Version ID of an object.

IsLatest (boolean) --
Specifies whether the object is (true) or is not (false) the latest version of an object.

LastModified (datetime) --
Date and time the object was last modified.

Owner (dict) --
Specifies the owner of the object.

DisplayName (string) --
Container for the display name of the owner.

ID (string) --
Container for the ID of the owner.







DeleteMarkers (list) --
Container for an object that is a delete marker.

(dict) --
Information about the delete marker.

Owner (dict) --
The account that created the delete marker.>

DisplayName (string) --
Container for the display name of the owner.

ID (string) --
Container for the ID of the owner.



Key (string) --
The object key.

VersionId (string) --
Version ID of an object.

IsLatest (boolean) --
Specifies whether the object is (true) or is not (false) the latest version of an object.

LastModified (datetime) --
Date and time the object was last modified.





Name (string) --
Bucket name.

Prefix (string) --
Selects objects that start with the value supplied by this parameter.

Delimiter (string) --
The delimiter grouping the included keys. A delimiter is a character that you specify to group keys. All keys that contain the same string between the prefix and the first occurrence of the delimiter are grouped under a single result element in CommonPrefixes . These groups are counted as one result against the max-keys limitation. These keys are not returned elsewhere in the response.

MaxKeys (integer) --
Specifies the maximum number of objects to return.

CommonPrefixes (list) --
All of the keys rolled up into a common prefix count as a single return when calculating the number of returns.

(dict) --
Container for all (if there are any) keys between Prefix and the next occurrence of the string specified by a delimiter. CommonPrefixes lists keys that act like subdirectories in the directory specified by Prefix. For example, if the prefix is notes/ and the delimiter is a slash (/) as in notes/summer/july, the common prefix is notes/summer/.

Prefix (string) --
Container for the specified common prefix.





EncodingType (string) --
Encoding type used by Amazon S3 to encode object key names in the XML response.
If you specify encoding-type request parameter, Amazon S3 includes this element in the response, and returns encoded key name values in the following response elements:

KeyMarker, NextKeyMarker, Prefix, Key , and Delimiter .








Examples
The following example return versions of an object with specific key name prefix. The request limits the number of items returned to two. If there are are more than two object version, S3 returns NextToken in the response. You can specify this token value in your next request to fetch next set of object versions.
response = client.list_object_versions(
    Bucket='examplebucket',
    Prefix='HappyFace.jpg',
)

print(response)


Expected Output:
{
    'Versions': [
        {
            'ETag': '"6805f2cfc46c0f04559748bb039d69ae"',
            'IsLatest': True,
            'Key': 'HappyFace.jpg',
            'LastModified': datetime(2016, 12, 15, 1, 19, 41, 3, 350, 0),
            'Owner': {
                'DisplayName': 'owner-display-name',
                'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
            },
            'Size': 3191,
            'StorageClass': 'STANDARD',
            'VersionId': 'null',
        },
        {
            'ETag': '"6805f2cfc46c0f04559748bb039d69ae"',
            'IsLatest': False,
            'Key': 'HappyFace.jpg',
            'LastModified': datetime(2016, 12, 13, 0, 58, 26, 1, 348, 0),
            'Owner': {
                'DisplayName': 'owner-display-name',
                'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
            },
            'Size': 3191,
            'StorageClass': 'STANDARD',
            'VersionId': 'PHtexPGjH2y.zBgT8LmB7wwLI2mpbz.k',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    Bucket (string) -- [REQUIRED]
    The bucket name that contains the objects.
    When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
    
    Delimiter (string) -- A delimiter is a character that you specify to group keys. All keys that contain the same string between the prefix and the first occurrence of the delimiter are grouped under a single result element in CommonPrefixes. These groups are counted as one result against the max-keys limitation. These keys are not returned elsewhere in the response.
    EncodingType (string) -- Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.
    KeyMarker (string) -- Specifies the key to start with when listing objects in a bucket.
    MaxKeys (integer) -- Sets the maximum number of keys returned in the response. By default the API returns up to 1,000 key names. The response might contain fewer keys but will never contain more. If additional keys satisfy the search criteria, but were not returned because max-keys was exceeded, the response contains <isTruncated>true</isTruncated>. To return the additional keys, see key-marker and version-id-marker.
    Prefix (string) -- Use this parameter to select only those keys that begin with the specified prefix. You can use prefixes to separate a bucket into different groupings of keys. (You can think of using prefix to make groups in the same way you\'d use a folder in a file system.) You can use prefix with delimiter to roll up numerous objects into a single result under CommonPrefixes.
    VersionIdMarker (string) -- Specifies the object version you want to start listing from.
    
    """
    pass

def list_objects(Bucket=None, Delimiter=None, EncodingType=None, Marker=None, MaxKeys=None, Prefix=None, RequestPayer=None):
    """
    Returns some or all (up to 1,000) of the objects in a bucket. You can use the request parameters as selection criteria to return a subset of the objects in a bucket. A 200 OK response can contain valid or invalid XML. Be sure to design your application to parse the contents of the response and handle it appropriately.
    The following operations are related to ListObjects :
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example list two objects in a bucket.
    Expected Output:
    
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
    :param Bucket: [REQUIRED]\nThe name of the bucket containing the objects.\n

    :type Delimiter: string
    :param Delimiter: A delimiter is a character you use to group keys.

    :type EncodingType: string
    :param EncodingType: Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.

    :type Marker: string
    :param Marker: Specifies the key to start with when listing objects in a bucket.

    :type MaxKeys: integer
    :param MaxKeys: Sets the maximum number of keys returned in the response. By default the API returns up to 1,000 key names. The response might contain fewer keys but will never contain more.

    :type Prefix: string
    :param Prefix: Limits the response to keys that begin with the specified prefix.

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the list objects request. Bucket owners need not specify this parameter in their requests.

    :rtype: dict

ReturnsResponse Syntax
{
    'IsTruncated': True|False,
    'Marker': 'string',
    'NextMarker': 'string',
    'Contents': [
        {
            'Key': 'string',
            'LastModified': datetime(2015, 1, 1),
            'ETag': 'string',
            'Size': 123,
            'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
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


Response Structure

(dict) --

IsTruncated (boolean) --
A flag that indicates whether Amazon S3 returned all of the results that satisfied the search criteria.

Marker (string) --
Indicates where in the bucket listing begins. Marker is included in the response if it was sent with the request.

NextMarker (string) --
When response is truncated (the IsTruncated element value in the response is true), you can use the key name in this field as marker in the subsequent request to get next set of objects. Amazon S3 lists objects in alphabetical order Note: This element is returned only if you have delimiter request parameter specified. If response does not include the NextMaker and it is truncated, you can use the value of the last Key in the response as the marker in the subsequent request to get the next set of object keys.

Contents (list) --
Metadata about each object returned.

(dict) --
An object consists of data and its descriptive metadata.

Key (string) --
The name that you assign to an object. You use the object key to retrieve the object.

LastModified (datetime) --
The date the Object was Last Modified

ETag (string) --
The entity tag is an MD5 hash of the object. ETag reflects only changes to the contents of an object, not its metadata.

Size (integer) --
Size in bytes of the object

StorageClass (string) --
The class of storage used to store the object.

Owner (dict) --
The owner of the object

DisplayName (string) --
Container for the display name of the owner.

ID (string) --
Container for the ID of the owner.







Name (string) --
Bucket name.

Prefix (string) --
Keys that begin with the indicated prefix.

Delimiter (string) --
Causes keys that contain the same string between the prefix and the first occurrence of the delimiter to be rolled up into a single result element in the CommonPrefixes collection. These rolled-up keys are not returned elsewhere in the response. Each rolled-up result counts as only one return against the MaxKeys value.

MaxKeys (integer) --
The maximum number of keys returned in the response body.

CommonPrefixes (list) --
All of the keys rolled up in a common prefix count as a single return when calculating the number of returns.
A response can contain CommonPrefixes only if you specify a delimiter.
CommonPrefixes contains all (if there are any) keys between Prefix and the next occurrence of the string specified by the delimiter.
CommonPrefixes lists keys that act like subdirectories in the directory specified by Prefix.
For example, if the prefix is notes/ and the delimiter is a slash (/) as in notes/summer/july, the common prefix is notes/summer/. All of the keys that roll up into a common prefix count as a single return when calculating the number of returns.

(dict) --
Container for all (if there are any) keys between Prefix and the next occurrence of the string specified by a delimiter. CommonPrefixes lists keys that act like subdirectories in the directory specified by Prefix. For example, if the prefix is notes/ and the delimiter is a slash (/) as in notes/summer/july, the common prefix is notes/summer/.

Prefix (string) --
Container for the specified common prefix.





EncodingType (string) --
Encoding type used by Amazon S3 to encode object keys in the response.







Exceptions

S3.Client.exceptions.NoSuchBucket

Examples
The following example list two objects in a bucket.
response = client.list_objects(
    Bucket='examplebucket',
    MaxKeys='2',
)

print(response)


Expected Output:
{
    'Contents': [
        {
            'ETag': '"70ee1738b6b21e2c8a43f3a5ab0eee71"',
            'Key': 'example1.jpg',
            'LastModified': datetime(2014, 11, 21, 19, 40, 5, 4, 325, 0),
            'Owner': {
                'DisplayName': 'myname',
                'ID': '12345example25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
            },
            'Size': 11,
            'StorageClass': 'STANDARD',
        },
        {
            'ETag': '"9c8af9a76df052144598c115ef33e511"',
            'Key': 'example2.jpg',
            'LastModified': datetime(2013, 11, 15, 1, 10, 49, 4, 319, 0),
            'Owner': {
                'DisplayName': 'myname',
                'ID': '12345example25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
            },
            'Size': 713193,
            'StorageClass': 'STANDARD',
        },
    ],
    'NextMarker': 'eyJNYXJrZXIiOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ==',
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
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
    Bucket (string) -- [REQUIRED]
    The name of the bucket containing the objects.
    
    Delimiter (string) -- A delimiter is a character you use to group keys.
    EncodingType (string) -- Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.
    Marker (string) -- Specifies the key to start with when listing objects in a bucket.
    MaxKeys (integer) -- Sets the maximum number of keys returned in the response. By default the API returns up to 1,000 key names. The response might contain fewer keys but will never contain more.
    Prefix (string) -- Limits the response to keys that begin with the specified prefix.
    RequestPayer (string) -- Confirms that the requester knows that she or he will be charged for the list objects request. Bucket owners need not specify this parameter in their requests.
    
    """
    pass

def list_objects_v2(Bucket=None, Delimiter=None, EncodingType=None, MaxKeys=None, Prefix=None, ContinuationToken=None, FetchOwner=None, StartAfter=None, RequestPayer=None):
    """
    Returns some or all (up to 1,000) of the objects in a bucket. You can use the request parameters as selection criteria to return a subset of the objects in a bucket. A 200 OK response can contain valid or invalid XML. Make sure to design your application to parse the contents of the response and handle it appropriately.
    To use this operation, you must have READ access to the bucket.
    To use this operation in an AWS Identity and Access Management (IAM) policy, you must have permissions to perform the s3:ListBucket action. The bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    To get a list of your buckets, see  ListBuckets .
    The following operations are related to ListObjectsV2 :
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example retrieves object list. The request specifies max keys to limit response to include only 2 object keys.
    Expected Output:
    
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
    :param Bucket: [REQUIRED]\nBucket name to list.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Delimiter: string
    :param Delimiter: A delimiter is a character you use to group keys.

    :type EncodingType: string
    :param EncodingType: Encoding type used by Amazon S3 to encode object keys in the response.

    :type MaxKeys: integer
    :param MaxKeys: Sets the maximum number of keys returned in the response. By default the API returns up to 1,000 key names. The response might contain fewer keys but will never contain more.

    :type Prefix: string
    :param Prefix: Limits the response to keys that begin with the specified prefix.

    :type ContinuationToken: string
    :param ContinuationToken: ContinuationToken indicates Amazon S3 that the list is being continued on this bucket with a token. ContinuationToken is obfuscated and is not a real key.

    :type FetchOwner: boolean
    :param FetchOwner: The owner field is not present in listV2 by default, if you want to return owner field with each key in the result then set the fetch owner field to true.

    :type StartAfter: string
    :param StartAfter: StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified key. StartAfter can be any key in the bucket.

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that she or he will be charged for the list objects request in V2 style. Bucket owners need not specify this parameter in their requests.

    :rtype: dict

ReturnsResponse Syntax
{
    'IsTruncated': True|False,
    'Contents': [
        {
            'Key': 'string',
            'LastModified': datetime(2015, 1, 1),
            'ETag': 'string',
            'Size': 123,
            'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
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


Response Structure

(dict) --

IsTruncated (boolean) --
Set to false if all of the results were returned. Set to true if more keys are available to return. If the number of results exceeds that specified by MaxKeys, all of the results might not be returned.

Contents (list) --
Metadata about each object returned.

(dict) --
An object consists of data and its descriptive metadata.

Key (string) --
The name that you assign to an object. You use the object key to retrieve the object.

LastModified (datetime) --
The date the Object was Last Modified

ETag (string) --
The entity tag is an MD5 hash of the object. ETag reflects only changes to the contents of an object, not its metadata.

Size (integer) --
Size in bytes of the object

StorageClass (string) --
The class of storage used to store the object.

Owner (dict) --
The owner of the object

DisplayName (string) --
Container for the display name of the owner.

ID (string) --
Container for the ID of the owner.







Name (string) --
Bucket name.
When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .

Prefix (string) --
Keys that begin with the indicated prefix.

Delimiter (string) --
Causes keys that contain the same string between the prefix and the first occurrence of the delimiter to be rolled up into a single result element in the CommonPrefixes collection. These rolled-up keys are not returned elsewhere in the response. Each rolled-up result counts as only one return against the MaxKeys value.

MaxKeys (integer) --
Sets the maximum number of keys returned in the response. By default the API returns up to 1,000 key names. The response might contain fewer keys but will never contain more.

CommonPrefixes (list) --
All of the keys rolled up into a common prefix count as a single return when calculating the number of returns.
A response can contain CommonPrefixes only if you specify a delimiter.

CommonPrefixes contains all (if there are any) keys between Prefix and the next occurrence of the string specified by a delimiter.
CommonPrefixes lists keys that act like subdirectories in the directory specified by Prefix .

For example, if the prefix is notes/ and the delimiter is a slash (/ ) as in notes/summer/july , the common prefix is notes/summer/ . All of the keys that roll up into a common prefix count as a single return when calculating the number of returns.

(dict) --
Container for all (if there are any) keys between Prefix and the next occurrence of the string specified by a delimiter. CommonPrefixes lists keys that act like subdirectories in the directory specified by Prefix. For example, if the prefix is notes/ and the delimiter is a slash (/) as in notes/summer/july, the common prefix is notes/summer/.

Prefix (string) --
Container for the specified common prefix.





EncodingType (string) --
Encoding type used by Amazon S3 to encode object key names in the XML response.
If you specify the encoding-type request parameter, Amazon S3 includes this element in the response, and returns encoded key name values in the following response elements:

Delimiter, Prefix, Key, and StartAfter .


KeyCount (integer) --
KeyCount is the number of keys returned with this request. KeyCount will always be less than equals to MaxKeys field. Say you ask for 50 keys, your result will include less than equals 50 keys

ContinuationToken (string) --
If ContinuationToken was sent with the request, it is included in the response.

NextContinuationToken (string) --

NextContinuationToken is sent when isTruncated is true, which means there are more keys in the bucket that can be listed. The next list requests to Amazon S3 can be continued with this NextContinuationToken . NextContinuationToken is obfuscated and is not a real key


StartAfter (string) --
If StartAfter was sent with the request, it is included in the response.







Exceptions

S3.Client.exceptions.NoSuchBucket

Examples
The following example retrieves object list. The request specifies max keys to limit response to include only 2 object keys.
response = client.list_objects_v2(
    Bucket='examplebucket',
    MaxKeys='2',
)

print(response)


Expected Output:
{
    'Contents': [
        {
            'ETag': '"70ee1738b6b21e2c8a43f3a5ab0eee71"',
            'Key': 'happyface.jpg',
            'LastModified': datetime(2014, 11, 21, 19, 40, 5, 4, 325, 0),
            'Size': 11,
            'StorageClass': 'STANDARD',
        },
        {
            'ETag': '"becf17f89c30367a9a44495d62ed521a-1"',
            'Key': 'test.jpg',
            'LastModified': datetime(2014, 5, 2, 4, 51, 50, 4, 122, 0),
            'Size': 4192256,
            'StorageClass': 'STANDARD',
        },
    ],
    'IsTruncated': True,
    'KeyCount': '2',
    'MaxKeys': '2',
    'Name': 'examplebucket',
    'NextContinuationToken': '1w41l63U0xa8q7smH50vCxyTQqdxo69O3EmK28Bi5PcROI4wI/EyIJg==',
    'Prefix': '',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'IsTruncated': True|False,
        'Contents': [
            {
                'Key': 'string',
                'LastModified': datetime(2015, 1, 1),
                'ETag': 'string',
                'Size': 123,
                'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
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
    Bucket (string) -- [REQUIRED]
    Bucket name to list.
    When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
    
    Delimiter (string) -- A delimiter is a character you use to group keys.
    EncodingType (string) -- Encoding type used by Amazon S3 to encode object keys in the response.
    MaxKeys (integer) -- Sets the maximum number of keys returned in the response. By default the API returns up to 1,000 key names. The response might contain fewer keys but will never contain more.
    Prefix (string) -- Limits the response to keys that begin with the specified prefix.
    ContinuationToken (string) -- ContinuationToken indicates Amazon S3 that the list is being continued on this bucket with a token. ContinuationToken is obfuscated and is not a real key.
    FetchOwner (boolean) -- The owner field is not present in listV2 by default, if you want to return owner field with each key in the result then set the fetch owner field to true.
    StartAfter (string) -- StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified key. StartAfter can be any key in the bucket.
    RequestPayer (string) -- Confirms that the requester knows that she or he will be charged for the list objects request in V2 style. Bucket owners need not specify this parameter in their requests.
    
    """
    pass

def list_parts(Bucket=None, Key=None, MaxParts=None, PartNumberMarker=None, UploadId=None, RequestPayer=None):
    """
    Lists the parts that have been uploaded for a specific multipart upload. This operation must include the upload ID, which you obtain by sending the initiate multipart upload request (see  CreateMultipartUpload ). This request returns a maximum of 1,000 uploaded parts. The default number of parts returned is 1,000 parts. You can restrict the number of parts returned by specifying the max-parts request parameter. If your multipart upload consists of more than 1,000 parts, the response returns an IsTruncated field with the value of true, and a NextPartNumberMarker element. In subsequent ListParts requests you can include the part-number-marker query string parameter and set its value to the NextPartNumberMarker field value from the previous response.
    For more information on multipart uploads, see Uploading Objects Using Multipart Upload .
    For information on permissions required to use the multipart upload API, see Multipart Upload API and Permissions .
    The following operations are related to ListParts :
    See also: AWS API Documentation
    
    Examples
    The following example lists parts uploaded for a specific multipart upload.
    Expected Output:
    
    :example: response = client.list_parts(
        Bucket='string',
        Key='string',
        MaxParts=123,
        PartNumberMarker=123,
        UploadId='string',
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nName of the bucket to which the parts are being uploaded.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Key: string
    :param Key: [REQUIRED]\nObject key for which the multipart upload was initiated.\n

    :type MaxParts: integer
    :param MaxParts: Sets the maximum number of parts to return.

    :type PartNumberMarker: integer
    :param PartNumberMarker: Specifies the part after which listing should begin. Only parts with higher part numbers will be listed.

    :type UploadId: string
    :param UploadId: [REQUIRED]\nUpload ID identifying the multipart upload whose parts are being listed.\n

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :rtype: dict

ReturnsResponse Syntax
{
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
    'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
    'RequestCharged': 'requester'
}


Response Structure

(dict) --

AbortDate (datetime) --
If the bucket has a lifecycle rule configured with an action to abort incomplete multipart uploads and the prefix in the lifecycle rule matches the object name in the request, then the response includes this header indicating when the initiated multipart upload will become eligible for abort operation. For more information, see Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Policy .
The response will also include the x-amz-abort-rule-id header that will provide the ID of the lifecycle configuration rule that defines this action.

AbortRuleId (string) --
This header is returned along with the x-amz-abort-date header. It identifies applicable lifecycle configuration rule that defines the action to abort incomplete multipart uploads.

Bucket (string) --
Name of the bucket to which the multipart upload was initiated.

Key (string) --
Object key for which the multipart upload was initiated.

UploadId (string) --
Upload ID identifying the multipart upload whose parts are being listed.

PartNumberMarker (integer) --
When a list is truncated, this element specifies the last part in the list, as well as the value to use for the part-number-marker request parameter in a subsequent request.

NextPartNumberMarker (integer) --
When a list is truncated, this element specifies the last part in the list, as well as the value to use for the part-number-marker request parameter in a subsequent request.

MaxParts (integer) --
Maximum number of parts that were allowed in the response.

IsTruncated (boolean) --
Indicates whether the returned list of parts is truncated. A true value indicates that the list was truncated. A list can be truncated if the number of parts exceeds the limit returned in the MaxParts element.

Parts (list) --
Container for elements related to a particular part. A response can contain zero or more Part elements.

(dict) --
Container for elements related to a part.

PartNumber (integer) --
Part number identifying the part. This is a positive integer between 1 and 10,000.

LastModified (datetime) --
Date and time at which the part was uploaded.

ETag (string) --
Entity tag returned when the part was uploaded.

Size (integer) --
Size in bytes of the uploaded part data.





Initiator (dict) --
Container element that identifies who initiated the multipart upload. If the initiator is an AWS account, this element provides the same information as the Owner element. If the initiator is an IAM User, this element provides the user ARN and display name.

ID (string) --
If the principal is an AWS account, it provides the Canonical User ID. If the principal is an IAM User, it provides a user ARN value.

DisplayName (string) --
Name of the Principal.



Owner (dict) --
Container element that identifies the object owner, after the object is created. If multipart upload is initiated by an IAM user, this element provides the parent account ID and display name.

DisplayName (string) --
Container for the display name of the owner.

ID (string) --
Container for the ID of the owner.



StorageClass (string) --
Class of storage (STANDARD or REDUCED_REDUNDANCY) used to store the uploaded object.

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.







Examples
The following example lists parts uploaded for a specific multipart upload.
response = client.list_parts(
    Bucket='examplebucket',
    Key='bigobject',
    UploadId='example7YPBOJuoFiQ9cz4P3Pe6FIZwO4f7wN93uHsNBEw97pl5eNwzExg0LAT2dUN91cOmrEQHDsP3WA60CEg--',
)

print(response)


Expected Output:
{
    'Initiator': {
        'DisplayName': 'owner-display-name',
        'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
    },
    'Owner': {
        'DisplayName': 'owner-display-name',
        'ID': 'examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484be31bebcc',
    },
    'Parts': [
        {
            'ETag': '"d8c2eafd90c266e19ab9dcacc479f8af"',
            'LastModified': datetime(2016, 12, 16, 0, 11, 42, 4, 351, 0),
            'PartNumber': '1',
            'Size': 26246026,
        },
        {
            'ETag': '"d8c2eafd90c266e19ab9dcacc479f8af"',
            'LastModified': datetime(2016, 12, 16, 0, 15, 1, 4, 351, 0),
            'PartNumber': '2',
            'Size': 26246026,
        },
    ],
    'StorageClass': 'STANDARD',
    'ResponseMetadata': {
        '...': '...',
    },
}



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
        'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    Bucket (string) -- [REQUIRED]
    Name of the bucket to which the parts are being uploaded.
    When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
    
    Key (string) -- [REQUIRED]
    Object key for which the multipart upload was initiated.
    
    MaxParts (integer) -- Sets the maximum number of parts to return.
    PartNumberMarker (integer) -- Specifies the part after which listing should begin. Only parts with higher part numbers will be listed.
    UploadId (string) -- [REQUIRED]
    Upload ID identifying the multipart upload whose parts are being listed.
    
    RequestPayer (string) -- Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .
    
    """
    pass

def put_bucket_accelerate_configuration(Bucket=None, AccelerateConfiguration=None):
    """
    Sets the accelerate configuration of an existing bucket. Amazon S3 Transfer Acceleration is a bucket-level feature that enables you to perform faster data transfers to Amazon S3.
    To use this operation, you must have permission to perform the s3:PutAccelerateConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    The Transfer Acceleration state of a bucket can be set to one of the following two values:
    The  GetBucketAccelerateConfiguration operation returns the transfer acceleration state of a bucket.
    After setting the Transfer Acceleration state of a bucket to Enabled, it might take up to thirty minutes before the data transfer rates to the bucket increase.
    The name of the bucket used for Transfer Acceleration must be DNS-compliant and must not contain periods (".").
    For more information about transfer acceleration, see Transfer Acceleration .
    The following operations are related to PutBucketAccelerateConfiguration :
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_accelerate_configuration(
        Bucket='string',
        AccelerateConfiguration={
            'Status': 'Enabled'|'Suspended'
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nName of the bucket for which the accelerate configuration is set.\n

    :type AccelerateConfiguration: dict
    :param AccelerateConfiguration: [REQUIRED]\nContainer for setting the transfer acceleration state.\n\nStatus (string) --Specifies the transfer acceleration status of the bucket.\n\n\n

    :returns: 
    GetBucketAccelerateConfiguration
    CreateBucket
    
    """
    pass

def put_bucket_acl(ACL=None, AccessControlPolicy=None, Bucket=None, GrantFullControl=None, GrantRead=None, GrantReadACP=None, GrantWrite=None, GrantWriteACP=None):
    """
    Sets the permissions on an existing bucket using access control lists (ACL). For more information, see Using ACLs . To set the ACL of a bucket, you must have WRITE_ACP permission.
    You can use one of the following two ways to set a bucket\'s permissions:
    Depending on your application needs, you may choose to set the ACL on a bucket using either the request body or the headers. For example, if you have an existing application that updates a bucket ACL using the request body, then you can continue to use that approach.
    You can set access permissions using one of the following methods:
    For example, the following x-amz-grant-write header grants create, overwrite, and delete objects permission to LogDelivery group predefined by Amazon S3 and two AWS accounts identified by their email addresses.
    You can use either a canned ACL or specify access permissions explicitly. You cannot do both.
    You can specify the person (grantee) to whom you\'re assigning access rights (using request elements) in the following ways:
    See also: AWS API Documentation
    
    Examples
    The following example replaces existing ACL on a bucket. The ACL grants the bucket owner (specified using the owner ID) and write permission to the LogDelivery group. Because this is a replace operation, you must specify all the grants in your request. To incrementally add or remove ACL grants, you might use the console.
    Expected Output:
    
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
    :param AccessControlPolicy: Contains the elements that set the ACL permissions for an object per grantee.\n\nGrants (list) --A list of grants.\n\n(dict) --Container for grant information.\n\nGrantee (dict) --The person being granted permissions.\n\nDisplayName (string) --Screen name of the grantee.\n\nEmailAddress (string) --Email address of the grantee.\n\nNote\nUsing email addresses to specify a grantee is only supported in the following AWS Regions:\n\nUS East (N. Virginia)\nUS West (N. California)\nUS West (Oregon)\nAsia Pacific (Singapore)\nAsia Pacific (Sydney)\nAsia Pacific (Tokyo)\nEurope (Ireland)\nSouth America (S\xc3\xa3o Paulo)\n\nFor a list of all the Amazon S3 supported Regions and endpoints, see Regions and Endpoints in the AWS General Reference.\n\n\nID (string) --The canonical user ID of the grantee.\n\nType (string) -- [REQUIRED]Type of grantee\n\nURI (string) --URI of the grantee group.\n\n\n\nPermission (string) --Specifies the permission given to the grantee.\n\n\n\n\n\nOwner (dict) --Container for the bucket owner\'s display name and ID.\n\nDisplayName (string) --Container for the display name of the owner.\n\nID (string) --Container for the ID of the owner.\n\n\n\n\n

    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket to which to apply the ACL.\n

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

    :return: response = client.put_bucket_acl(
        Bucket='examplebucket',
        GrantFullControl='id=examplee7a2f25102679df27bb0ae12b3f85be6f290b936c4393484',
        GrantWrite='uri=http://acs.amazonaws.com/groups/s3/LogDelivery',
    )
    
    print(response)
    
    
    :returns: 
    id \xe2\x80\x93 if the value specified is the canonical user ID of an AWS account
    uri \xe2\x80\x93 if you are granting permissions to a predefined group
    emailAddress \xe2\x80\x93 if the value specified is the email address of an AWS account
    
    """
    pass

def put_bucket_analytics_configuration(Bucket=None, Id=None, AnalyticsConfiguration=None):
    """
    Sets an analytics configuration for the bucket (specified by the analytics configuration ID). You can have up to 1,000 analytics configurations per bucket.
    You can choose to have storage class analysis export analysis reports sent to a comma-separated values (CSV) flat file. See the DataExport request element. Reports are updated daily and are based on the object filters that you configure. When selecting data export, you specify a destination bucket and an optional destination prefix where the file is written. You can export the data to a destination bucket in a different account. However, the destination bucket must be in the same Region as the bucket that you are making the PUT analytics configuration to. For more information, see Amazon S3 Analytics \xe2\x80\x93 Storage Class Analysis .
    To use this operation, you must have permissions to perform the s3:PutAnalyticsConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
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
    :param Bucket: [REQUIRED]\nThe name of the bucket to which an analytics configuration is stored.\n

    :type Id: string
    :param Id: [REQUIRED]\nThe ID that identifies the analytics configuration.\n

    :type AnalyticsConfiguration: dict
    :param AnalyticsConfiguration: [REQUIRED]\nThe configuration and any analyses for the analytics filter.\n\nId (string) -- [REQUIRED]The ID that identifies the analytics configuration.\n\nFilter (dict) --The filter used to describe a set of objects for analyses. A filter must have exactly one prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be considered in any analysis.\n\nPrefix (string) --The prefix to use when evaluating an analytics filter.\n\nTag (dict) --The tag to use when evaluating an analytics filter.\n\nKey (string) -- [REQUIRED]Name of the tag.\n\nValue (string) -- [REQUIRED]Value of the tag.\n\n\n\nAnd (dict) --A conjunction (logical AND) of predicates, which is used in evaluating an analytics filter. The operator must have at least two predicates.\n\nPrefix (string) --The prefix to use when evaluating an AND predicate: The prefix that an object must have to be included in the metrics results.\n\nTags (list) --The list of tags to use when evaluating an AND predicate.\n\n(dict) --A container of a key value name pair.\n\nKey (string) -- [REQUIRED]Name of the tag.\n\nValue (string) -- [REQUIRED]Value of the tag.\n\n\n\n\n\n\n\n\n\nStorageClassAnalysis (dict) -- [REQUIRED]Contains data related to access patterns to be collected and made available to analyze the tradeoffs between different storage classes.\n\nDataExport (dict) --Specifies how data related to the storage class analysis for an Amazon S3 bucket should be exported.\n\nOutputSchemaVersion (string) -- [REQUIRED]The version of the output schema to use when exporting data. Must be V_1 .\n\nDestination (dict) -- [REQUIRED]The place to store the data for an analysis.\n\nS3BucketDestination (dict) -- [REQUIRED]A destination signifying output to an S3 bucket.\n\nFormat (string) -- [REQUIRED]Specifies the file format used when exporting data to Amazon S3.\n\nBucketAccountId (string) --The account ID that owns the destination S3 bucket. If no account ID is provided, the owner is not validated before exporting data.\n\nNote\nAlthough this value is optional, we strongly recommend that you set it to help prevent problems if the destination bucket ownership changes.\n\n\nBucket (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the bucket to which data is exported.\n\nPrefix (string) --The prefix to use when exporting data. The prefix is prepended to all results.\n\n\n\n\n\n\n\n\n\n\n

    :returns: 
    HTTP Error: HTTP 400 Bad Request
    Code: TooManyConfigurations
    Cause: You are attempting to create a new configuration but have already reached the 1,000-configuration limit.
    
    """
    pass

def put_bucket_cors(Bucket=None, CORSConfiguration=None):
    """
    Sets the cors configuration for your bucket. If the configuration exists, Amazon S3 replaces it.
    To use this operation, you must be allowed to perform the s3:PutBucketCORS action. By default, the bucket owner has this permission and can grant it to others.
    You set this configuration on a bucket so that the bucket can service cross-origin requests. For example, you might want to enable a request whose origin is http://www.example.com to access your Amazon S3 bucket at my.example.bucket.com by using the browser\'s XMLHttpRequest capability.
    To enable cross-origin resource sharing (CORS) on a bucket, you add the cors subresource to the bucket. The cors subresource is an XML document in which you configure rules that identify origins and the HTTP methods that can be executed on your bucket. The document is limited to 64 KB in size.
    When Amazon S3 receives a cross-origin request (or a pre-flight OPTIONS request) against a bucket, it evaluates the cors configuration on the bucket and uses the first CORSRule rule that matches the incoming browser request to enable a cross-origin request. For a rule to match, the following conditions must be met:
    For more information about CORS, go to Enabling Cross-Origin Resource Sharing in the Amazon Simple Storage Service Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example enables PUT, POST, and DELETE requests from www.example.com, and enables GET requests from any domain.
    Expected Output:
    
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
    :param Bucket: [REQUIRED]\nSpecifies the bucket impacted by the cors configuration.\n

    :type CORSConfiguration: dict
    :param CORSConfiguration: [REQUIRED]\nDescribes the cross-origin access configuration for objects in an Amazon S3 bucket. For more information, see Enabling Cross-Origin Resource Sharing in the Amazon Simple Storage Service Developer Guide .\n\nCORSRules (list) -- [REQUIRED]A set of origins and methods (cross-origin access that you want to allow). You can add up to 100 rules to the configuration.\n\n(dict) --Specifies a cross-origin access rule for an Amazon S3 bucket.\n\nAllowedHeaders (list) --Headers that are specified in the Access-Control-Request-Headers header. These headers are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS request, Amazon S3 returns any requested headers that are allowed.\n\n(string) --\n\n\nAllowedMethods (list) -- [REQUIRED]An HTTP method that you allow the origin to execute. Valid values are GET , PUT , HEAD , POST , and DELETE .\n\n(string) --\n\n\nAllowedOrigins (list) -- [REQUIRED]One or more origins you want customers to be able to access the bucket from.\n\n(string) --\n\n\nExposeHeaders (list) --One or more headers in the response that you want customers to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).\n\n(string) --\n\n\nMaxAgeSeconds (integer) --The time in seconds that your browser is to cache the preflight response for the specified resource.\n\n\n\n\n\n\n

    :return: response = client.put_bucket_cors(
        Bucket='',
        CORSConfiguration={
            'CORSRules': [
                {
                    'AllowedHeaders': [
                        '*',
                    ],
                    'AllowedMethods': [
                        'PUT',
                        'POST',
                        'DELETE',
                    ],
                    'AllowedOrigins': [
                        'http://www.example.com',
                    ],
                    'ExposeHeaders': [
                        'x-amz-server-side-encryption',
                    ],
                    'MaxAgeSeconds': 3000,
                },
                {
                    'AllowedHeaders': [
                        'Authorization',
                    ],
                    'AllowedMethods': [
                        'GET',
                    ],
                    'AllowedOrigins': [
                        '*',
                    ],
                    'MaxAgeSeconds': 3000,
                },
            ],
        },
        ContentMD5='',
    )
    
    print(response)
    
    
    :returns: 
    GetBucketCors
    DeleteBucketCors
    RESTOPTIONSobject
    
    """
    pass

def put_bucket_encryption(Bucket=None, ContentMD5=None, ServerSideEncryptionConfiguration=None):
    """
    This implementation of the PUT operation uses the encryption subresource to set the default encryption state of an existing bucket.
    This implementation of the PUT operation sets default encryption for a bucket using server-side encryption with Amazon S3-managed keys SSE-S3 or AWS KMS customer master keys (CMKs) (SSE-KMS). For information about the Amazon S3 default encryption feature, see Amazon S3 Default Bucket Encryption .
    To use this operation, you must have permissions to perform the s3:PutEncryptionConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources in the Amazon Simple Storage Service Developer Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_encryption(
        Bucket='string',
        ContentMD5='string',
        ServerSideEncryptionConfiguration={
            'Rules': [
                {
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'AES256'|'aws:kms',
                        'KMSMasterKeyID': 'string'
                    }
                },
            ]
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nSpecifies default encryption for a bucket using server-side encryption with Amazon S3-managed keys (SSE-S3) or customer master keys stored in AWS KMS (SSE-KMS). For information about the Amazon S3 default encryption feature, see Amazon S3 Default Bucket Encryption in the Amazon Simple Storage Service Developer Guide .\n

    :type ContentMD5: string
    :param ContentMD5: The base64-encoded 128-bit MD5 digest of the server-side encryption configuration. This parameter is auto-populated when using the command from the CLI.

    :type ServerSideEncryptionConfiguration: dict
    :param ServerSideEncryptionConfiguration: [REQUIRED]\nSpecifies the default server-side-encryption configuration.\n\nRules (list) -- [REQUIRED]Container for information about a particular server-side encryption configuration rule.\n\n(dict) --Specifies the default server-side encryption configuration.\n\nApplyServerSideEncryptionByDefault (dict) --Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT Object request doesn\'t specify any server-side encryption, this default encryption will be applied.\n\nSSEAlgorithm (string) -- [REQUIRED]Server-side encryption algorithm to use for the default encryption.\n\nKMSMasterKeyID (string) --AWS Key Management Service (KMS) customer master key ID to use for the default encryption. This parameter is allowed if and only if SSEAlgorithm is set to aws:kms .\nYou can specify the key ID or the Amazon Resource Name (ARN) of the CMK. However, if you are using encryption with cross-account operations, you must use a fully qualified CMK ARN. For more information, see Using encryption for cross-account operations .\n\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\n\nWarning\nAmazon S3 only supports symmetric CMKs and not asymmetric CMKs. For more information, see Using Symmetric and Asymmetric Keys in the AWS Key Management Service Developer Guide .\n\n\n\n\n\n\n\n\n\n

    :returns: 
    Bucket (string) -- [REQUIRED]
    Specifies default encryption for a bucket using server-side encryption with Amazon S3-managed keys (SSE-S3) or customer master keys stored in AWS KMS (SSE-KMS). For information about the Amazon S3 default encryption feature, see Amazon S3 Default Bucket Encryption in the Amazon Simple Storage Service Developer Guide .
    
    ContentMD5 (string) -- The base64-encoded 128-bit MD5 digest of the server-side encryption configuration. This parameter is auto-populated when using the command from the CLI.
    ServerSideEncryptionConfiguration (dict) -- [REQUIRED]
    Specifies the default server-side-encryption configuration.
    
    Rules (list) -- [REQUIRED]Container for information about a particular server-side encryption configuration rule.
    
    (dict) --Specifies the default server-side encryption configuration.
    
    ApplyServerSideEncryptionByDefault (dict) --Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT Object request doesn\'t specify any server-side encryption, this default encryption will be applied.
    
    SSEAlgorithm (string) -- [REQUIRED]Server-side encryption algorithm to use for the default encryption.
    
    KMSMasterKeyID (string) --AWS Key Management Service (KMS) customer master key ID to use for the default encryption. This parameter is allowed if and only if SSEAlgorithm is set to aws:kms .
    You can specify the key ID or the Amazon Resource Name (ARN) of the CMK. However, if you are using encryption with cross-account operations, you must use a fully qualified CMK ARN. For more information, see Using encryption for cross-account operations .
    
    For example:
    
    Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
    Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
    
    
    Warning
    Amazon S3 only supports symmetric CMKs and not asymmetric CMKs. For more information, see Using Symmetric and Asymmetric Keys in the AWS Key Management Service Developer Guide .
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def put_bucket_inventory_configuration(Bucket=None, Id=None, InventoryConfiguration=None):
    """
    This implementation of the PUT operation adds an inventory configuration (identified by the inventory ID) to the bucket. You can have up to 1,000 inventory configurations per bucket.
    Amazon S3 inventory generates inventories of the objects in the bucket on a daily or weekly basis, and the results are published to a flat file. The bucket that is inventoried is called the source bucket, and the bucket where the inventory flat file is stored is called the destination bucket. The destination bucket must be in the same AWS Region as the source bucket.
    When you configure an inventory for a source bucket, you specify the destination bucket where you want the inventory to be stored, and whether to generate the inventory daily or weekly. You can also configure what object metadata to include and whether to inventory all object versions or only current versions. For more information, see Amazon S3 Inventory in the Amazon Simple Storage Service Developer Guide.
    To use this operation, you must have permissions to perform the s3:PutInventoryConfiguration action. The bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources in the Amazon Simple Storage Service Developer Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_inventory_configuration(
        Bucket='string',
        Id='string',
        InventoryConfiguration={
            'Destination': {
                'S3BucketDestination': {
                    'AccountId': 'string',
                    'Bucket': 'string',
                    'Format': 'CSV'|'ORC'|'Parquet',
                    'Prefix': 'string',
                    'Encryption': {
                        'SSES3': {}
                        ,
                        'SSEKMS': {
                            'KeyId': 'string'
                        }
                    }
                }
            },
            'IsEnabled': True|False,
            'Filter': {
                'Prefix': 'string'
            },
            'Id': 'string',
            'IncludedObjectVersions': 'All'|'Current',
            'OptionalFields': [
                'Size'|'LastModifiedDate'|'StorageClass'|'ETag'|'IsMultipartUploaded'|'ReplicationStatus'|'EncryptionStatus'|'ObjectLockRetainUntilDate'|'ObjectLockMode'|'ObjectLockLegalHoldStatus'|'IntelligentTieringAccessTier',
            ],
            'Schedule': {
                'Frequency': 'Daily'|'Weekly'
            }
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket where the inventory configuration will be stored.\n

    :type Id: string
    :param Id: [REQUIRED]\nThe ID used to identify the inventory configuration.\n

    :type InventoryConfiguration: dict
    :param InventoryConfiguration: [REQUIRED]\nSpecifies the inventory configuration.\n\nDestination (dict) -- [REQUIRED]Contains information about where to publish the inventory results.\n\nS3BucketDestination (dict) -- [REQUIRED]Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where inventory results are published.\n\nAccountId (string) --The account ID that owns the destination S3 bucket. If no account ID is provided, the owner is not validated before exporting data.\n\nNote\nAlthough this value is optional, we strongly recommend that you set it to help prevent problems if the destination bucket ownership changes.\n\n\nBucket (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the bucket where inventory results will be published.\n\nFormat (string) -- [REQUIRED]Specifies the output format of the inventory results.\n\nPrefix (string) --The prefix that is prepended to all inventory results.\n\nEncryption (dict) --Contains the type of server-side encryption used to encrypt the inventory results.\n\nSSES3 (dict) --Specifies the use of SSE-S3 to encrypt delivered inventory reports.\n\nSSEKMS (dict) --Specifies the use of SSE-KMS to encrypt delivered inventory reports.\n\nKeyId (string) -- [REQUIRED]Specifies the ID of the AWS Key Management Service (AWS KMS) symmetric customer managed customer master key (CMK) to use for encrypting inventory reports.\n\n\n\n\n\n\n\n\n\nIsEnabled (boolean) -- [REQUIRED]Specifies whether the inventory is enabled or disabled. If set to True , an inventory list is generated. If set to False , no inventory list is generated.\n\nFilter (dict) --Specifies an inventory filter. The inventory only includes objects that meet the filter\'s criteria.\n\nPrefix (string) -- [REQUIRED]The prefix that an object must have to be included in the inventory results.\n\n\n\nId (string) -- [REQUIRED]The ID used to identify the inventory configuration.\n\nIncludedObjectVersions (string) -- [REQUIRED]Object versions to include in the inventory list. If set to All , the list includes all the object versions, which adds the version-related fields VersionId , IsLatest , and DeleteMarker to the list. If set to Current , the list does not contain these version-related fields.\n\nOptionalFields (list) --Contains the optional fields that are included in the inventory results.\n\n(string) --\n\n\nSchedule (dict) -- [REQUIRED]Specifies the schedule for generating inventory results.\n\nFrequency (string) -- [REQUIRED]Specifies how frequently inventory results are produced.\n\n\n\n\n

    :returns: 
    GetBucketInventoryConfiguration
    DeleteBucketInventoryConfiguration
    ListBucketInventoryConfigurations
    
    """
    pass

def put_bucket_lifecycle(Bucket=None, LifecycleConfiguration=None):
    """
    Creates a new lifecycle configuration for the bucket or replaces an existing lifecycle configuration. For information about lifecycle configuration, see Object Lifecycle Management in the Amazon Simple Storage Service Developer Guide .
    By default, all Amazon S3 resources, including buckets, objects, and related subresources (for example, lifecycle configuration and website configuration) are private. Only the resource owner, the AWS account that created the resource, can access it. The resource owner can optionally grant access permissions to others by writing an access policy. For this operation, users must get the s3:PutLifecycleConfiguration permission.
    You can also explicitly deny permissions. Explicit denial also supersedes any other permissions. If you want to prevent users or accounts from removing or deleting objects from your bucket, you must deny them permissions for the following actions:
    For more information about permissions, see Managing Access Permissions to your Amazon S3 Resources in the Amazon Simple Storage Service Developer Guide .
    For more examples of transitioning objects to storage classes such as STANDARD_IA or ONEZONE_IA, see Examples of Lifecycle Configuration .
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
                        'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                    },
                    'NoncurrentVersionTransition': {
                        'NoncurrentDays': 123,
                        'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
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
    :param LifecycleConfiguration: \nRules (list) -- [REQUIRED]Specifies lifecycle configuration rules for an Amazon S3 bucket.\n\n(dict) --Specifies lifecycle rules for an Amazon S3 bucket. For more information, see Put Bucket Lifecycle Configuration in the Amazon Simple Storage Service API Reference . For examples, see Put Bucket Lifecycle Configuration Examples\n\nExpiration (dict) --Specifies the expiration for the lifecycle of the object.\n\nDate (datetime) --Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.\n\nDays (integer) --Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.\n\nExpiredObjectDeleteMarker (boolean) --Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.\n\n\n\nID (string) --Unique identifier for the rule. The value can\'t be longer than 255 characters.\n\nPrefix (string) -- [REQUIRED]Object key prefix that identifies one or more objects to which this rule applies.\n\nStatus (string) -- [REQUIRED]If Enabled , the rule is currently being applied. If Disabled , the rule is not currently being applied.\n\nTransition (dict) --Specifies when an object transitions to a specified storage class. For more information about Amazon S3 lifecycle configuration rules, see Transitioning Objects Using Amazon S3 Lifecycle in the Amazon Simple Storage Service Developer Guide .\n\nDate (datetime) --Indicates when objects are transitioned to the specified storage class. The date value must be in ISO 8601 format. The time is always midnight UTC.\n\nDays (integer) --Indicates the number of days after creation when objects are transitioned to the specified storage class. The value must be a positive integer.\n\nStorageClass (string) --The storage class to which you want the object to transition.\n\n\n\nNoncurrentVersionTransition (dict) --Container for the transition rule that describes when noncurrent objects transition to the STANDARD_IA , ONEZONE_IA , INTELLIGENT_TIERING , GLACIER , or DEEP_ARCHIVE storage class. If your bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to the STANDARD_IA , ONEZONE_IA , INTELLIGENT_TIERING , GLACIER , or DEEP_ARCHIVE storage class at a specific period in the object\'s lifetime.\n\nNoncurrentDays (integer) --Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates How Long an Object Has Been Noncurrent in the Amazon Simple Storage Service Developer Guide .\n\nStorageClass (string) --The class of storage used to store the object.\n\n\n\nNoncurrentVersionExpiration (dict) --Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes the noncurrent object versions. You set this lifecycle configuration action on a bucket that has versioning enabled (or suspended) to request that Amazon S3 delete noncurrent object versions at a specific period in the object\'s lifetime.\n\nNoncurrentDays (integer) --Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates When an Object Became Noncurrent in the Amazon Simple Storage Service Developer Guide .\n\n\n\nAbortIncompleteMultipartUpload (dict) --Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before permanently removing all parts of the upload. For more information, see Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Policy in the Amazon Simple Storage Service Developer Guide .\n\nDaysAfterInitiation (integer) --Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.\n\n\n\n\n\n\n\n\n

    :returns: 
    GetBucketLifecycle (Deprecated)
    GetBucketLifecycleConfiguration
    
    By default, a resource owner\xe2\x80\x94in this case, a bucket owner, which is the AWS account that created the bucket\xe2\x80\x94can perform any of the operations. A resource owner can also grant others permission to perform the operation. For more information, see the following topics in the Amazon Simple Storage Service Developer Guide:
    Specifying Permissions in a Policy
    Managing Access Permissions to your Amazon S3 Resources
    
    
    
    """
    pass

def put_bucket_lifecycle_configuration(Bucket=None, LifecycleConfiguration=None):
    """
    Creates a new lifecycle configuration for the bucket or replaces an existing lifecycle configuration. For information about lifecycle configuration, see Managing Access Permissions to Your Amazon S3 Resources .
    You specify the lifecycle configuration in your request body. The lifecycle configuration is specified as XML consisting of one or more rules. Each rule consists of the following:
    For more information, see Object Lifecycle Management and Lifecycle Configuration Elements .
    By default, all Amazon S3 resources are private, including buckets, objects, and related subresources (for example, lifecycle configuration and website configuration). Only the resource owner (that is, the AWS account that created it) can access the resource. The resource owner can optionally grant access permissions to others by writing an access policy. For this operation, a user must get the s3:PutLifecycleConfiguration permission.
    You can also explicitly deny permissions. Explicit deny also supersedes any other permissions. If you want to block users or accounts from removing or deleting objects from your bucket, you must deny them permissions for the following actions:
    For more information about permissions, see Managing Access Permissions to Your Amazon S3 Resources .
    The following are related to PutBucketLifecycleConfiguration :
    See also: AWS API Documentation
    
    Examples
    The following example replaces existing lifecycle configuration, if any, on the specified bucket.
    Expected Output:
    
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
                            'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                        },
                    ],
                    'NoncurrentVersionTransitions': [
                        {
                            'NoncurrentDays': 123,
                            'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
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
    :param Bucket: [REQUIRED]\nThe name of the bucket for which to set the configuration.\n

    :type LifecycleConfiguration: dict
    :param LifecycleConfiguration: Container for lifecycle rules. You can add as many as 1,000 rules.\n\nRules (list) -- [REQUIRED]A lifecycle rule for individual objects in an Amazon S3 bucket.\n\n(dict) --A lifecycle rule for individual objects in an Amazon S3 bucket.\n\nExpiration (dict) --Specifies the expiration for the lifecycle of the object in the form of date, days and, whether the object has a delete marker.\n\nDate (datetime) --Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.\n\nDays (integer) --Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.\n\nExpiredObjectDeleteMarker (boolean) --Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.\n\n\n\nID (string) --Unique identifier for the rule. The value cannot be longer than 255 characters.\n\nPrefix (string) --Prefix identifying one or more objects to which the rule applies. This is No longer used; use Filter instead.\n\nFilter (dict) --The Filter is used to identify objects that a Lifecycle Rule applies to. A Filter must have exactly one of Prefix , Tag , or And specified.\n\nPrefix (string) --Prefix identifying one or more objects to which the rule applies.\n\nTag (dict) --This tag must exist in the object\'s tag set in order for the rule to apply.\n\nKey (string) -- [REQUIRED]Name of the tag.\n\nValue (string) -- [REQUIRED]Value of the tag.\n\n\n\nAnd (dict) --This is used in a Lifecycle Rule Filter to apply a logical AND to two or more predicates. The Lifecycle Rule will apply to any object matching all of the predicates configured inside the And operator.\n\nPrefix (string) --Prefix identifying one or more objects to which the rule applies.\n\nTags (list) --All of these tags must exist in the object\'s tag set in order for the rule to apply.\n\n(dict) --A container of a key value name pair.\n\nKey (string) -- [REQUIRED]Name of the tag.\n\nValue (string) -- [REQUIRED]Value of the tag.\n\n\n\n\n\n\n\n\n\nStatus (string) -- [REQUIRED]If \'Enabled\', the rule is currently being applied. If \'Disabled\', the rule is not currently being applied.\n\nTransitions (list) --Specifies when an Amazon S3 object transitions to a specified storage class.\n\n(dict) --Specifies when an object transitions to a specified storage class. For more information about Amazon S3 lifecycle configuration rules, see Transitioning Objects Using Amazon S3 Lifecycle in the Amazon Simple Storage Service Developer Guide .\n\nDate (datetime) --Indicates when objects are transitioned to the specified storage class. The date value must be in ISO 8601 format. The time is always midnight UTC.\n\nDays (integer) --Indicates the number of days after creation when objects are transitioned to the specified storage class. The value must be a positive integer.\n\nStorageClass (string) --The storage class to which you want the object to transition.\n\n\n\n\n\nNoncurrentVersionTransitions (list) --Specifies the transition rule for the lifecycle rule that describes when noncurrent objects transition to a specific storage class. If your bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to a specific storage class at a set period in the object\'s lifetime.\n\n(dict) --Container for the transition rule that describes when noncurrent objects transition to the STANDARD_IA , ONEZONE_IA , INTELLIGENT_TIERING , GLACIER , or DEEP_ARCHIVE storage class. If your bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to the STANDARD_IA , ONEZONE_IA , INTELLIGENT_TIERING , GLACIER , or DEEP_ARCHIVE storage class at a specific period in the object\'s lifetime.\n\nNoncurrentDays (integer) --Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates How Long an Object Has Been Noncurrent in the Amazon Simple Storage Service Developer Guide .\n\nStorageClass (string) --The class of storage used to store the object.\n\n\n\n\n\nNoncurrentVersionExpiration (dict) --Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes the noncurrent object versions. You set this lifecycle configuration action on a bucket that has versioning enabled (or suspended) to request that Amazon S3 delete noncurrent object versions at a specific period in the object\'s lifetime.\n\nNoncurrentDays (integer) --Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates When an Object Became Noncurrent in the Amazon Simple Storage Service Developer Guide .\n\n\n\nAbortIncompleteMultipartUpload (dict) --Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before permanently removing all parts of the upload. For more information, see Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Policy in the Amazon Simple Storage Service Developer Guide .\n\nDaysAfterInitiation (integer) --Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.\n\n\n\n\n\n\n\n\n

    :return: response = client.put_bucket_lifecycle_configuration(
        Bucket='examplebucket',
        LifecycleConfiguration={
            'Rules': [
                {
                    'Expiration': {
                        'Days': 3650,
                    },
                    'Filter': {
                        'Prefix': 'documents/',
                    },
                    'ID': 'TestOnly',
                    'Status': 'Enabled',
                    'Transitions': [
                        {
                            'Days': 365,
                            'StorageClass': 'GLACIER',
                        },
                    ],
                },
            ],
        },
    )
    
    print(response)
    
    
    :returns: 
    s3:DeleteObject
    s3:DeleteObjectVersion
    s3:PutLifecycleConfiguration
    
    """
    pass

def put_bucket_logging(Bucket=None, BucketLoggingStatus=None):
    """
    Set the logging parameters for a bucket and to specify permissions for who can view and modify the logging parameters. All logs are saved to buckets in the same AWS Region as the source bucket. To set the logging status of a bucket, you must be the bucket owner.
    The bucket owner is automatically granted FULL_CONTROL to all logs. You use the Grantee request element to grant access to other people. The Permissions request element specifies the kind of access the grantee has to the logs.
    You can specify the person (grantee) to whom you\'re assigning access rights (using request elements) in the following ways:
    To enable logging, you use LoggingEnabled and its children request elements. To disable logging, you use an empty BucketLoggingStatus request element:
    For more information about server access logging, see Server Access Logging .
    For more information about creating a bucket, see  CreateBucket . For more information about returning the logging status of a bucket, see  GetBucketLogging .
    The following operations are related to PutBucketLogging :
    See also: AWS API Documentation
    
    Examples
    The following example sets logging policy on a bucket. For the Log Delivery group to deliver logs to the destination bucket, it needs permission for the READ_ACP action which the policy grants.
    Expected Output:
    
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
    :param Bucket: [REQUIRED]\nThe name of the bucket for which to set the logging parameters.\n

    :type BucketLoggingStatus: dict
    :param BucketLoggingStatus: [REQUIRED]\nContainer for logging status information.\n\nLoggingEnabled (dict) --Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys for a bucket. For more information, see PUT Bucket logging in the Amazon Simple Storage Service API Reference .\n\nTargetBucket (string) -- [REQUIRED]Specifies the bucket where you want Amazon S3 to store server access logs. You can have your logs delivered to any bucket that you own, including the same bucket that is being logged. You can also configure multiple buckets to deliver their logs to the same target bucket. In this case, you should choose a different TargetPrefix for each source bucket so that the delivered log files can be distinguished by key.\n\nTargetGrants (list) --Container for granting information.\n\n(dict) --Container for granting information.\n\nGrantee (dict) --Container for the person being granted permissions.\n\nDisplayName (string) --Screen name of the grantee.\n\nEmailAddress (string) --Email address of the grantee.\n\nNote\nUsing email addresses to specify a grantee is only supported in the following AWS Regions:\n\nUS East (N. Virginia)\nUS West (N. California)\nUS West (Oregon)\nAsia Pacific (Singapore)\nAsia Pacific (Sydney)\nAsia Pacific (Tokyo)\nEurope (Ireland)\nSouth America (S\xc3\xa3o Paulo)\n\nFor a list of all the Amazon S3 supported Regions and endpoints, see Regions and Endpoints in the AWS General Reference.\n\n\nID (string) --The canonical user ID of the grantee.\n\nType (string) -- [REQUIRED]Type of grantee\n\nURI (string) --URI of the grantee group.\n\n\n\nPermission (string) --Logging permissions assigned to the Grantee for the bucket.\n\n\n\n\n\nTargetPrefix (string) -- [REQUIRED]A prefix for all log object keys. If you store log files from multiple Amazon S3 buckets in a single bucket, you can use a prefix to distinguish which log files came from which bucket.\n\n\n\n\n

    :return: response = client.put_bucket_logging(
        Bucket='sourcebucket',
        BucketLoggingStatus={
            'LoggingEnabled': {
                'TargetBucket': 'targetbucket',
                'TargetGrants': [
                    {
                        'Grantee': {
                            'Type': 'Group',
                            'URI': 'http://acs.amazonaws.com/groups/global/AllUsers',
                        },
                        'Permission': 'READ',
                    },
                ],
                'TargetPrefix': 'MyBucketLogs/',
            },
        },
    )
    
    print(response)
    
    
    :returns: 
    PutObject
    DeleteBucket
    CreateBucket
    GetBucketLogging
    
    """
    pass

def put_bucket_metrics_configuration(Bucket=None, Id=None, MetricsConfiguration=None):
    """
    Sets a metrics configuration (specified by the metrics configuration ID) for the bucket. You can have up to 1,000 metrics configurations per bucket. If you\'re updating an existing metrics configuration, note that this is a full replacement of the existing metrics configuration. If you don\'t include the elements you want to keep, they are erased.
    To use this operation, you must have permissions to perform the s3:PutMetricsConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    For information about CloudWatch request metrics for Amazon S3, see Monitoring Metrics with Amazon CloudWatch .
    The following operations are related to PutBucketMetricsConfiguration :
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
    :param Bucket: [REQUIRED]\nThe name of the bucket for which the metrics configuration is set.\n

    :type Id: string
    :param Id: [REQUIRED]\nThe ID used to identify the metrics configuration.\n

    :type MetricsConfiguration: dict
    :param MetricsConfiguration: [REQUIRED]\nSpecifies the metrics configuration.\n\nId (string) -- [REQUIRED]The ID used to identify the metrics configuration.\n\nFilter (dict) --Specifies a metrics configuration filter. The metrics configuration will only include objects that meet the filter\'s criteria. A filter must be a prefix, a tag, or a conjunction (MetricsAndOperator).\n\nPrefix (string) --The prefix used when evaluating a metrics filter.\n\nTag (dict) --The tag used when evaluating a metrics filter.\n\nKey (string) -- [REQUIRED]Name of the tag.\n\nValue (string) -- [REQUIRED]Value of the tag.\n\n\n\nAnd (dict) --A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The operator must have at least two predicates, and an object must match all of the predicates in order for the filter to apply.\n\nPrefix (string) --The prefix used when evaluating an AND predicate.\n\nTags (list) --The list of tags used when evaluating an AND predicate.\n\n(dict) --A container of a key value name pair.\n\nKey (string) -- [REQUIRED]Name of the tag.\n\nValue (string) -- [REQUIRED]Value of the tag.\n\n\n\n\n\n\n\n\n\n\n

    :returns: 
    Error code: TooManyConfigurations
    Description: You are attempting to create a new configuration but have already reached the 1,000-configuration limit.
    HTTP Status Code: HTTP 400 Bad Request
    
    
    
    """
    pass

def put_bucket_notification(Bucket=None, NotificationConfiguration=None):
    """
    No longer used, see the  PutBucketNotificationConfiguration operation.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bucket_notification(
        Bucket='string',
        NotificationConfiguration={
            'TopicConfiguration': {
                'Id': 'string',
                'Events': [
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
                ],
                'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
                'Topic': 'string'
            },
            'QueueConfiguration': {
                'Id': 'string',
                'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
                'Events': [
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
                ],
                'Queue': 'string'
            },
            'CloudFunctionConfiguration': {
                'Id': 'string',
                'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
                'Events': [
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
                ],
                'CloudFunction': 'string',
                'InvocationRole': 'string'
            }
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket.\n

    :type NotificationConfiguration: dict
    :param NotificationConfiguration: [REQUIRED]\nThe container for the configuration.\n\nTopicConfiguration (dict) --This data type is deprecated. A container for specifying the configuration for publication of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.\n\nId (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.\n\nEvents (list) --A collection of events related to objects\n\n(string) --The bucket event for which to send notifications.\n\n\n\nEvent (string) --Bucket event for which to send notifications.\n\nTopic (string) --Amazon SNS topic to which Amazon S3 will publish a message to report the specified events for the bucket.\n\n\n\nQueueConfiguration (dict) --This data type is deprecated. This data type specifies the configuration for publishing messages to an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified events.\n\nId (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.\n\nEvent (string) --The bucket event for which to send notifications.\n\nEvents (list) --A collection of bucket events for which to send notifications\n\n(string) --The bucket event for which to send notifications.\n\n\n\nQueue (string) --The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message when it detects events of the specified type.\n\n\n\nCloudFunctionConfiguration (dict) --Container for specifying the AWS Lambda notification configuration.\n\nId (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.\n\nEvent (string) --The bucket event for which to send notifications.\n\nEvents (list) --Bucket events for which to send notifications.\n\n(string) --The bucket event for which to send notifications.\n\n\n\nCloudFunction (string) --Lambda cloud function ARN that Amazon S3 can invoke when it detects events of the specified type.\n\nInvocationRole (string) --The role supporting the invocation of the Lambda function\n\n\n\n\n

    """
    pass

def put_bucket_notification_configuration(Bucket=None, NotificationConfiguration=None):
    """
    Enables notifications of specified events for a bucket. For more information about event notifications, see Configuring Event Notifications .
    Using this API, you can replace an existing notification configuration. The configuration is an XML file that defines the event types that you want Amazon S3 to publish and the destination where you want Amazon S3 to publish an event notification when it detects an event of the specified type.
    By default, your bucket has no event notifications configured. That is, the notification configuration will be an empty NotificationConfiguration .
    This operation replaces the existing notification configuration with the configuration you include in the request body.
    After Amazon S3 receives this request, it first verifies that any Amazon Simple Notification Service (Amazon SNS) or Amazon Simple Queue Service (Amazon SQS) destination exists, and that the bucket owner has permission to publish to it by sending a test notification. In the case of AWS Lambda destinations, Amazon S3 verifies that the Lambda function permissions grant Amazon S3 permission to invoke the function from the Amazon S3 bucket. For more information, see Configuring Notifications for Amazon S3 Events .
    You can disable notifications by adding the empty NotificationConfiguration element.
    By default, only the bucket owner can configure notifications on a bucket. However, bucket owners can use a bucket policy to grant permission to other users to set this configuration with s3:PutBucketNotification permission.
    If the configuration in the request body includes only one TopicConfiguration specifying only the s3:ReducedRedundancyLostObject event type, the response will also include the x-amz-sns-test-message-id header containing the message ID of the test notification sent to the topic.
    The following operation is related to PutBucketNotificationConfiguration :
    See also: AWS API Documentation
    
    Examples
    The following example sets notification configuration on a bucket to publish the object created events to an SNS topic.
    Expected Output:
    
    :example: response = client.put_bucket_notification_configuration(
        Bucket='string',
        NotificationConfiguration={
            'TopicConfigurations': [
                {
                    'Id': 'string',
                    'TopicArn': 'string',
                    'Events': [
                        's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
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
                        's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
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
                        's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:*'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed'|'s3:Replication:*'|'s3:Replication:OperationFailedReplication'|'s3:Replication:OperationNotTracked'|'s3:Replication:OperationMissedThreshold'|'s3:Replication:OperationReplicatedAfterThreshold',
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
    :param Bucket: [REQUIRED]\nThe name of the bucket.\n

    :type NotificationConfiguration: dict
    :param NotificationConfiguration: [REQUIRED]\nA container for specifying the notification configuration of the bucket. If this element is empty, notifications are turned off for the bucket.\n\nTopicConfigurations (list) --The topic to which notifications are sent and the events for which notifications are generated.\n\n(dict) --A container for specifying the configuration for publication of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.\n\nId (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.\n\nTopicArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon SNS topic to which Amazon S3 publishes a message when it detects events of the specified type.\n\nEvents (list) -- [REQUIRED]The Amazon S3 bucket event about which to send notifications. For more information, see Supported Event Types in the Amazon Simple Storage Service Developer Guide .\n\n(string) --The bucket event for which to send notifications.\n\n\n\nFilter (dict) --Specifies object key name filtering rules. For information about key name filtering, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .\n\nKey (dict) --A container for object key name prefix and suffix filtering rules.\n\nFilterRules (list) --A list of containers for the key-value pair that defines the criteria for the filter rule.\n\n(dict) --Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.\n\nName (string) --The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .\n\nValue (string) --The value that the filter searches for in object key names.\n\n\n\n\n\n\n\n\n\n\n\n\n\nQueueConfigurations (list) --The Amazon Simple Queue Service queues to publish messages to and the events for which to publish messages.\n\n(dict) --Specifies the configuration for publishing messages to an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified events.\n\nId (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.\n\nQueueArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message when it detects events of the specified type.\n\nEvents (list) -- [REQUIRED]A collection of bucket events for which to send notifications\n\n(string) --The bucket event for which to send notifications.\n\n\n\nFilter (dict) --Specifies object key name filtering rules. For information about key name filtering, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .\n\nKey (dict) --A container for object key name prefix and suffix filtering rules.\n\nFilterRules (list) --A list of containers for the key-value pair that defines the criteria for the filter rule.\n\n(dict) --Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.\n\nName (string) --The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .\n\nValue (string) --The value that the filter searches for in object key names.\n\n\n\n\n\n\n\n\n\n\n\n\n\nLambdaFunctionConfigurations (list) --Describes the AWS Lambda functions to invoke and the events for which to invoke them.\n\n(dict) --A container for specifying the configuration for AWS Lambda notifications.\n\nId (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.\n\nLambdaFunctionArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS Lambda function that Amazon S3 invokes when the specified event type occurs.\n\nEvents (list) -- [REQUIRED]The Amazon S3 bucket event for which to invoke the AWS Lambda function. For more information, see Supported Event Types in the Amazon Simple Storage Service Developer Guide .\n\n(string) --The bucket event for which to send notifications.\n\n\n\nFilter (dict) --Specifies object key name filtering rules. For information about key name filtering, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .\n\nKey (dict) --A container for object key name prefix and suffix filtering rules.\n\nFilterRules (list) --A list of containers for the key-value pair that defines the criteria for the filter rule.\n\n(dict) --Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.\n\nName (string) --The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .\n\nValue (string) --The value that the filter searches for in object key names.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

    :return: response = client.put_bucket_notification_configuration(
        Bucket='examplebucket',
        NotificationConfiguration={
            'TopicConfigurations': [
                {
                    'Events': [
                        's3:ObjectCreated:*',
                    ],
                    'TopicArn': 'arn:aws:sns:us-west-2:123456789012:s3-notification-topic',
                },
            ],
        },
    )
    
    print(response)
    
    
    :returns: 
    Bucket (string) -- [REQUIRED]
    The name of the bucket.
    
    NotificationConfiguration (dict) -- [REQUIRED]
    A container for specifying the notification configuration of the bucket. If this element is empty, notifications are turned off for the bucket.
    
    TopicConfigurations (list) --The topic to which notifications are sent and the events for which notifications are generated.
    
    (dict) --A container for specifying the configuration for publication of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
    
    Id (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.
    
    TopicArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon SNS topic to which Amazon S3 publishes a message when it detects events of the specified type.
    
    Events (list) -- [REQUIRED]The Amazon S3 bucket event about which to send notifications. For more information, see Supported Event Types in the Amazon Simple Storage Service Developer Guide .
    
    (string) --The bucket event for which to send notifications.
    
    
    
    Filter (dict) --Specifies object key name filtering rules. For information about key name filtering, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .
    
    Key (dict) --A container for object key name prefix and suffix filtering rules.
    
    FilterRules (list) --A list of containers for the key-value pair that defines the criteria for the filter rule.
    
    (dict) --Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.
    
    Name (string) --The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .
    
    Value (string) --The value that the filter searches for in object key names.
    
    
    
    
    
    
    
    
    
    
    
    
    
    QueueConfigurations (list) --The Amazon Simple Queue Service queues to publish messages to and the events for which to publish messages.
    
    (dict) --Specifies the configuration for publishing messages to an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified events.
    
    Id (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.
    
    QueueArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message when it detects events of the specified type.
    
    Events (list) -- [REQUIRED]A collection of bucket events for which to send notifications
    
    (string) --The bucket event for which to send notifications.
    
    
    
    Filter (dict) --Specifies object key name filtering rules. For information about key name filtering, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .
    
    Key (dict) --A container for object key name prefix and suffix filtering rules.
    
    FilterRules (list) --A list of containers for the key-value pair that defines the criteria for the filter rule.
    
    (dict) --Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.
    
    Name (string) --The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .
    
    Value (string) --The value that the filter searches for in object key names.
    
    
    
    
    
    
    
    
    
    
    
    
    
    LambdaFunctionConfigurations (list) --Describes the AWS Lambda functions to invoke and the events for which to invoke them.
    
    (dict) --A container for specifying the configuration for AWS Lambda notifications.
    
    Id (string) --An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.
    
    LambdaFunctionArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS Lambda function that Amazon S3 invokes when the specified event type occurs.
    
    Events (list) -- [REQUIRED]The Amazon S3 bucket event for which to invoke the AWS Lambda function. For more information, see Supported Event Types in the Amazon Simple Storage Service Developer Guide .
    
    (string) --The bucket event for which to send notifications.
    
    
    
    Filter (dict) --Specifies object key name filtering rules. For information about key name filtering, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .
    
    Key (dict) --A container for object key name prefix and suffix filtering rules.
    
    FilterRules (list) --A list of containers for the key-value pair that defines the criteria for the filter rule.
    
    (dict) --Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.
    
    Name (string) --The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide .
    
    Value (string) --The value that the filter searches for in object key names.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def put_bucket_policy(Bucket=None, ConfirmRemoveSelfBucketAccess=None, Policy=None):
    """
    Applies an Amazon S3 bucket policy to an Amazon S3 bucket. If you are using an identity other than the root user of the AWS account that owns the bucket, the calling identity must have the PutBucketPolicy permissions on the specified bucket and belong to the bucket owner\'s account in order to use this operation.
    If you don\'t have PutBucketPolicy permissions, Amazon S3 returns a 403 Access Denied error. If you have the correct permissions, but you\'re not using an identity that belongs to the bucket owner\'s account, Amazon S3 returns a 405 Method Not Allowed error.
    For more information about bucket policies, see Using Bucket Policies and User Policies .
    The following operations are related to PutBucketPolicy :
    See also: AWS API Documentation
    
    Examples
    The following example sets a permission policy on a bucket.
    Expected Output:
    
    :example: response = client.put_bucket_policy(
        Bucket='string',
        ConfirmRemoveSelfBucketAccess=True|False,
        Policy='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket.\n

    :type ConfirmRemoveSelfBucketAccess: boolean
    :param ConfirmRemoveSelfBucketAccess: Set this parameter to true to confirm that you want to remove your permissions to change this bucket policy in the future.

    :type Policy: string
    :param Policy: [REQUIRED]\nThe bucket policy as a JSON document.\n

    :return: response = client.put_bucket_policy(
        Bucket='examplebucket',
        Policy='{"Version": "2012-10-17", "Statement": [{ "Sid": "id-1","Effect": "Allow","Principal": {"AWS": "arn:aws:iam::123456789012:root"}, "Action": [ "s3:PutObject","s3:PutObjectAcl"], "Resource": ["arn:aws:s3:::acl3/*" ] } ]}',
    )
    
    print(response)
    
    
    :returns: 
    Bucket (string) -- [REQUIRED]
    The name of the bucket.
    
    ConfirmRemoveSelfBucketAccess (boolean) -- Set this parameter to true to confirm that you want to remove your permissions to change this bucket policy in the future.
    Policy (string) -- [REQUIRED]
    The bucket policy as a JSON document.
    
    
    """
    pass

def put_bucket_replication(Bucket=None, ReplicationConfiguration=None, Token=None):
    """
    Creates a replication configuration or replaces an existing one. For more information, see Replication in the Amazon S3 Developer Guide .
    Specify the replication configuration in the request body. In the replication configuration, you provide the name of the destination bucket where you want Amazon S3 to replicate objects, the IAM role that Amazon S3 can assume to replicate objects on your behalf, and other relevant information.
    A replication configuration must include at least one rule, and can contain a maximum of 1,000. Each rule identifies a subset of objects to replicate by filtering the objects in the source bucket. To choose additional subsets of objects to replicate, add a rule for each subset. All rules must specify the same destination bucket.
    To specify a subset of the objects in the source bucket to apply a replication rule to, add the Filter element as a child of the Rule element. You can filter objects based on an object key prefix, one or more object tags, or both. When you add the Filter element in the configuration, you must also add the following elements: DeleteMarkerReplication , Status , and Priority .
    For information about enabling versioning on a bucket, see Using Versioning .
    By default, a resource owner, in this case the AWS account that created the bucket, can perform this operation. The resource owner can also grant others permissions to perform the operation. For more information about permissions, see Specifying Permissions in a Policy and Managing Access Permissions to Your Amazon S3 Resources .
    By default, Amazon S3 doesn\'t replicate objects that are stored at rest using server-side encryption with CMKs stored in AWS KMS. To replicate AWS KMS-encrypted objects, add the following: SourceSelectionCriteria , SseKmsEncryptedObjects , Status , EncryptionConfiguration , and ReplicaKmsKeyID . For information about replication configuration, see Replicating Objects Created with SSE Using CMKs stored in AWS KMS .
    For information on PutBucketReplication errors, see  ReplicationErrorCodeList
    The following operations are related to PutBucketReplication :
    See also: AWS API Documentation
    
    Examples
    The following example sets replication configuration on a bucket.
    Expected Output:
    
    :example: response = client.put_bucket_replication(
        Bucket='string',
        ReplicationConfiguration={
            'Role': 'string',
            'Rules': [
                {
                    'ID': 'string',
                    'Priority': 123,
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
                    'SourceSelectionCriteria': {
                        'SseKmsEncryptedObjects': {
                            'Status': 'Enabled'|'Disabled'
                        }
                    },
                    'ExistingObjectReplication': {
                        'Status': 'Enabled'|'Disabled'
                    },
                    'Destination': {
                        'Bucket': 'string',
                        'Account': 'string',
                        'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
                        'AccessControlTranslation': {
                            'Owner': 'Destination'
                        },
                        'EncryptionConfiguration': {
                            'ReplicaKmsKeyID': 'string'
                        },
                        'ReplicationTime': {
                            'Status': 'Enabled'|'Disabled',
                            'Time': {
                                'Minutes': 123
                            }
                        },
                        'Metrics': {
                            'Status': 'Enabled'|'Disabled',
                            'EventThreshold': {
                                'Minutes': 123
                            }
                        }
                    },
                    'DeleteMarkerReplication': {
                        'Status': 'Enabled'|'Disabled'
                    }
                },
            ]
        },
        Token='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket\n

    :type ReplicationConfiguration: dict
    :param ReplicationConfiguration: [REQUIRED]\nA container for replication rules. You can add up to 1,000 rules. The maximum size of a replication configuration is 2 MB.\n\nRole (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that Amazon S3 assumes when replicating objects. For more information, see How to Set Up Replication in the Amazon Simple Storage Service Developer Guide .\n\nRules (list) -- [REQUIRED]A container for one or more replication rules. A replication configuration must have at least one rule and can contain a maximum of 1,000 rules.\n\n(dict) --Specifies which Amazon S3 objects to replicate and where to store the replicas.\n\nID (string) --A unique identifier for the rule. The maximum value is 255 characters.\n\nPriority (integer) --The priority associated with the rule. If you specify multiple rules in a replication configuration, Amazon S3 prioritizes the rules to prevent conflicts when filtering. If two or more rules identify the same object based on a specified filter, the rule with higher priority takes precedence. For example:\n\nSame object quality prefix-based filter criteria if prefixes you specified in multiple rules overlap\nSame object qualify tag-based filter criteria specified in multiple rules\n\nFor more information, see `Replication < https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html>`__ in the Amazon Simple Storage Service Developer Guide .\n\nPrefix (string) --An object key name prefix that identifies the object or objects to which the rule applies. The maximum prefix length is 1,024 characters. To include all objects in a bucket, specify an empty string.\n\nFilter (dict) --A filter that identifies the subset of objects to which the replication rule applies. A Filter must specify exactly one Prefix , Tag , or an And child element.\n\nPrefix (string) --An object key name prefix that identifies the subset of objects to which the rule applies.\n\nTag (dict) --A container for specifying a tag key and value.\nThe rule applies only to objects that have the tag in their tag set.\n\nKey (string) -- [REQUIRED]Name of the tag.\n\nValue (string) -- [REQUIRED]Value of the tag.\n\n\n\nAnd (dict) --A container for specifying rule filters. The filters determine the subset of objects to which the rule applies. This element is required only if you specify more than one filter. For example:\n\nIf you specify both a Prefix and a Tag filter, wrap these filters in an And tag.\nIf you specify a filter based on multiple tags, wrap the Tag elements in an And tag.\n\n\nPrefix (string) --An object key name prefix that identifies the subset of objects to which the rule applies.\n\nTags (list) --An array of tags containing key and value pairs.\n\n(dict) --A container of a key value name pair.\n\nKey (string) -- [REQUIRED]Name of the tag.\n\nValue (string) -- [REQUIRED]Value of the tag.\n\n\n\n\n\n\n\n\n\nStatus (string) -- [REQUIRED]Specifies whether the rule is enabled.\n\nSourceSelectionCriteria (dict) --A container that describes additional filters for identifying the source objects that you want to replicate. You can choose to enable or disable the replication of these objects. Currently, Amazon S3 supports only the filter that you can specify for objects created with server-side encryption using a customer master key (CMK) stored in AWS Key Management Service (SSE-KMS).\n\nSseKmsEncryptedObjects (dict) --A container for filter information for the selection of Amazon S3 objects encrypted with AWS KMS. If you include SourceSelectionCriteria in the replication configuration, this element is required.\n\nStatus (string) -- [REQUIRED]Specifies whether Amazon S3 replicates objects created with server-side encryption using a customer master key (CMK) stored in AWS Key Management Service.\n\n\n\n\n\nExistingObjectReplication (dict) --\nStatus (string) -- [REQUIRED]\n\n\nDestination (dict) -- [REQUIRED]A container for information about the replication destination and its configurations including enabling the S3 Replication Time Control (S3 RTC).\n\nBucket (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store the results.\n\nAccount (string) --Destination bucket owner account ID. In a cross-account scenario, if you direct Amazon S3 to change replica ownership to the AWS account that owns the destination bucket by specifying the AccessControlTranslation property, this is the account ID of the destination bucket owner. For more information, see Replication Additional Configuration: Changing the Replica Owner in the Amazon Simple Storage Service Developer Guide .\n\nStorageClass (string) --The storage class to use when replicating objects, such as S3 Standard or reduced redundancy. By default, Amazon S3 uses the storage class of the source object to create the object replica.\nFor valid values, see the StorageClass element of the PUT Bucket replication action in the Amazon Simple Storage Service API Reference .\n\nAccessControlTranslation (dict) --Specify this only in a cross-account scenario (where source and destination bucket owners are not the same), and you want to change replica ownership to the AWS account that owns the destination bucket. If this is not specified in the replication configuration, the replicas are owned by same AWS account that owns the source object.\n\nOwner (string) -- [REQUIRED]Specifies the replica ownership. For default and valid values, see PUT bucket replication in the Amazon Simple Storage Service API Reference .\n\n\n\nEncryptionConfiguration (dict) --A container that provides information about encryption. If SourceSelectionCriteria is specified, you must specify this element.\n\nReplicaKmsKeyID (string) --Specifies the ID (Key ARN or Alias ARN) of the customer managed customer master key (CMK) stored in AWS Key Management Service (KMS) for the destination bucket. Amazon S3 uses this key to encrypt replica objects. Amazon S3 only supports symmetric customer managed CMKs. For more information, see Using Symmetric and Asymmetric Keys in the AWS Key Management Service Developer Guide .\n\n\n\nReplicationTime (dict) --A container specifying S3 Replication Time Control (S3 RTC), including whether S3 RTC is enabled and the time when all objects and operations on objects must be replicated. Must be specified together with a Metrics block.\n\nStatus (string) -- [REQUIRED]Specifies whether the replication time is enabled.\n\nTime (dict) -- [REQUIRED]A container specifying the time by which replication should be complete for all objects and operations on objects.\n\nMinutes (integer) --Contains an integer specifying time in minutes.\nValid values: 15 minutes.\n\n\n\n\n\nMetrics (dict) --A container specifying replication metrics-related settings enabling metrics and Amazon S3 events for S3 Replication Time Control (S3 RTC). Must be specified together with a ReplicationTime block.\n\nStatus (string) -- [REQUIRED]Specifies whether the replication metrics are enabled.\n\nEventThreshold (dict) -- [REQUIRED]A container specifying the time threshold for emitting the s3:Replication:OperationMissedThreshold event.\n\nMinutes (integer) --Contains an integer specifying time in minutes.\nValid values: 15 minutes.\n\n\n\n\n\n\n\nDeleteMarkerReplication (dict) --Specifies whether Amazon S3 replicates the delete markers. If you specify a Filter , you must specify this element. However, in the latest version of replication configuration (when Filter is specified), Amazon S3 doesn\'t replicate delete markers. Therefore, the DeleteMarkerReplication element can contain only <Status>Disabled</Status>. For an example configuration, see Basic Rule Configuration .\n\nNote\nIf you don\'t specify the Filter element, Amazon S3 assumes that the replication configuration is the earlier version, V1. In the earlier version, Amazon S3 handled replication of delete markers differently. For more information, see Backward Compatibility .\n\n\nStatus (string) --Indicates whether to replicate delete markers.\n\nNote\nIn the current implementation, Amazon S3 doesn\'t replicate the delete markers. The status must be Disabled .\n\n\n\n\n\n\n\n\n\n

    :type Token: string
    :param Token: 

    :return: response = client.put_bucket_replication(
        Bucket='examplebucket',
        ReplicationConfiguration={
            'Role': 'arn:aws:iam::123456789012:role/examplerole',
            'Rules': [
                {
                    'Destination': {
                        'Bucket': 'arn:aws:s3:::destinationbucket',
                        'StorageClass': 'STANDARD',
                    },
                    'Prefix': '',
                    'Status': 'Enabled',
                },
            ],
        },
    )
    
    print(response)
    
    
    :returns: 
    Bucket (string) -- [REQUIRED]
    The name of the bucket
    
    ReplicationConfiguration (dict) -- [REQUIRED]
    A container for replication rules. You can add up to 1,000 rules. The maximum size of a replication configuration is 2 MB.
    
    Role (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that Amazon S3 assumes when replicating objects. For more information, see How to Set Up Replication in the Amazon Simple Storage Service Developer Guide .
    
    Rules (list) -- [REQUIRED]A container for one or more replication rules. A replication configuration must have at least one rule and can contain a maximum of 1,000 rules.
    
    (dict) --Specifies which Amazon S3 objects to replicate and where to store the replicas.
    
    ID (string) --A unique identifier for the rule. The maximum value is 255 characters.
    
    Priority (integer) --The priority associated with the rule. If you specify multiple rules in a replication configuration, Amazon S3 prioritizes the rules to prevent conflicts when filtering. If two or more rules identify the same object based on a specified filter, the rule with higher priority takes precedence. For example:
    
    Same object quality prefix-based filter criteria if prefixes you specified in multiple rules overlap
    Same object qualify tag-based filter criteria specified in multiple rules
    
    For more information, see `Replication < https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html>`__ in the Amazon Simple Storage Service Developer Guide .
    
    Prefix (string) --An object key name prefix that identifies the object or objects to which the rule applies. The maximum prefix length is 1,024 characters. To include all objects in a bucket, specify an empty string.
    
    Filter (dict) --A filter that identifies the subset of objects to which the replication rule applies. A Filter must specify exactly one Prefix , Tag , or an And child element.
    
    Prefix (string) --An object key name prefix that identifies the subset of objects to which the rule applies.
    
    Tag (dict) --A container for specifying a tag key and value.
    The rule applies only to objects that have the tag in their tag set.
    
    Key (string) -- [REQUIRED]Name of the tag.
    
    Value (string) -- [REQUIRED]Value of the tag.
    
    
    
    And (dict) --A container for specifying rule filters. The filters determine the subset of objects to which the rule applies. This element is required only if you specify more than one filter. For example:
    
    If you specify both a Prefix and a Tag filter, wrap these filters in an And tag.
    If you specify a filter based on multiple tags, wrap the Tag elements in an And tag.
    
    
    Prefix (string) --An object key name prefix that identifies the subset of objects to which the rule applies.
    
    Tags (list) --An array of tags containing key and value pairs.
    
    (dict) --A container of a key value name pair.
    
    Key (string) -- [REQUIRED]Name of the tag.
    
    Value (string) -- [REQUIRED]Value of the tag.
    
    
    
    
    
    
    
    
    
    Status (string) -- [REQUIRED]Specifies whether the rule is enabled.
    
    SourceSelectionCriteria (dict) --A container that describes additional filters for identifying the source objects that you want to replicate. You can choose to enable or disable the replication of these objects. Currently, Amazon S3 supports only the filter that you can specify for objects created with server-side encryption using a customer master key (CMK) stored in AWS Key Management Service (SSE-KMS).
    
    SseKmsEncryptedObjects (dict) --A container for filter information for the selection of Amazon S3 objects encrypted with AWS KMS. If you include SourceSelectionCriteria in the replication configuration, this element is required.
    
    Status (string) -- [REQUIRED]Specifies whether Amazon S3 replicates objects created with server-side encryption using a customer master key (CMK) stored in AWS Key Management Service.
    
    
    
    
    
    ExistingObjectReplication (dict) --
    Status (string) -- [REQUIRED]
    
    
    Destination (dict) -- [REQUIRED]A container for information about the replication destination and its configurations including enabling the S3 Replication Time Control (S3 RTC).
    
    Bucket (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store the results.
    
    Account (string) --Destination bucket owner account ID. In a cross-account scenario, if you direct Amazon S3 to change replica ownership to the AWS account that owns the destination bucket by specifying the AccessControlTranslation property, this is the account ID of the destination bucket owner. For more information, see Replication Additional Configuration: Changing the Replica Owner in the Amazon Simple Storage Service Developer Guide .
    
    StorageClass (string) --The storage class to use when replicating objects, such as S3 Standard or reduced redundancy. By default, Amazon S3 uses the storage class of the source object to create the object replica.
    For valid values, see the StorageClass element of the PUT Bucket replication action in the Amazon Simple Storage Service API Reference .
    
    AccessControlTranslation (dict) --Specify this only in a cross-account scenario (where source and destination bucket owners are not the same), and you want to change replica ownership to the AWS account that owns the destination bucket. If this is not specified in the replication configuration, the replicas are owned by same AWS account that owns the source object.
    
    Owner (string) -- [REQUIRED]Specifies the replica ownership. For default and valid values, see PUT bucket replication in the Amazon Simple Storage Service API Reference .
    
    
    
    EncryptionConfiguration (dict) --A container that provides information about encryption. If SourceSelectionCriteria is specified, you must specify this element.
    
    ReplicaKmsKeyID (string) --Specifies the ID (Key ARN or Alias ARN) of the customer managed customer master key (CMK) stored in AWS Key Management Service (KMS) for the destination bucket. Amazon S3 uses this key to encrypt replica objects. Amazon S3 only supports symmetric customer managed CMKs. For more information, see Using Symmetric and Asymmetric Keys in the AWS Key Management Service Developer Guide .
    
    
    
    ReplicationTime (dict) --A container specifying S3 Replication Time Control (S3 RTC), including whether S3 RTC is enabled and the time when all objects and operations on objects must be replicated. Must be specified together with a Metrics block.
    
    Status (string) -- [REQUIRED]Specifies whether the replication time is enabled.
    
    Time (dict) -- [REQUIRED]A container specifying the time by which replication should be complete for all objects and operations on objects.
    
    Minutes (integer) --Contains an integer specifying time in minutes.
    Valid values: 15 minutes.
    
    
    
    
    
    Metrics (dict) --A container specifying replication metrics-related settings enabling metrics and Amazon S3 events for S3 Replication Time Control (S3 RTC). Must be specified together with a ReplicationTime block.
    
    Status (string) -- [REQUIRED]Specifies whether the replication metrics are enabled.
    
    EventThreshold (dict) -- [REQUIRED]A container specifying the time threshold for emitting the s3:Replication:OperationMissedThreshold event.
    
    Minutes (integer) --Contains an integer specifying time in minutes.
    Valid values: 15 minutes.
    
    
    
    
    
    
    
    DeleteMarkerReplication (dict) --Specifies whether Amazon S3 replicates the delete markers. If you specify a Filter , you must specify this element. However, in the latest version of replication configuration (when Filter is specified), Amazon S3 doesn\'t replicate delete markers. Therefore, the DeleteMarkerReplication element can contain only <Status>Disabled</Status>. For an example configuration, see Basic Rule Configuration .
    
    Note
    If you don\'t specify the Filter element, Amazon S3 assumes that the replication configuration is the earlier version, V1. In the earlier version, Amazon S3 handled replication of delete markers differently. For more information, see Backward Compatibility .
    
    
    Status (string) --Indicates whether to replicate delete markers.
    
    Note
    In the current implementation, Amazon S3 doesn\'t replicate the delete markers. The status must be Disabled .
    
    
    
    
    
    
    
    
    
    
    Token (string) -- 
    
    """
    pass

def put_bucket_request_payment(Bucket=None, RequestPaymentConfiguration=None):
    """
    Sets the request payment configuration for a bucket. By default, the bucket owner pays for downloads from the bucket. This configuration parameter enables the bucket owner (only) to specify that the person requesting the download will be charged for the download. For more information, see Requester Pays Buckets .
    The following operations are related to PutBucketRequestPayment :
    See also: AWS API Documentation
    
    Examples
    The following example sets request payment configuration on a bucket so that person requesting the download is charged.
    Expected Output:
    
    :example: response = client.put_bucket_request_payment(
        Bucket='string',
        RequestPaymentConfiguration={
            'Payer': 'Requester'|'BucketOwner'
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name.\n

    :type RequestPaymentConfiguration: dict
    :param RequestPaymentConfiguration: [REQUIRED]\nContainer for Payer.\n\nPayer (string) -- [REQUIRED]Specifies who pays for the download and request fees.\n\n\n

    :return: response = client.put_bucket_request_payment(
        Bucket='examplebucket',
        RequestPaymentConfiguration={
            'Payer': 'Requester',
        },
    )
    
    print(response)
    
    
    :returns: 
    Bucket (string) -- [REQUIRED]
    The bucket name.
    
    RequestPaymentConfiguration (dict) -- [REQUIRED]
    Container for Payer.
    
    Payer (string) -- [REQUIRED]Specifies who pays for the download and request fees.
    
    
    
    
    """
    pass

def put_bucket_tagging(Bucket=None, Tagging=None):
    """
    Sets the tags for a bucket.
    Use tags to organize your AWS bill to reflect your own cost structure. To do this, sign up to get your AWS account bill with tag key values included. Then, to see the cost of combined resources, organize your billing information according to resources with the same tag key values. For example, you can tag several resources with a specific application name, and then organize your billing information to see the total cost of that application across several services. For more information, see Cost Allocation and Tagging .
    To use this operation, you must have permissions to perform the s3:PutBucketTagging action. The bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources .
    The following operations are related to PutBucketTagging :
    See also: AWS API Documentation
    
    Examples
    The following example sets tags on a bucket. Any existing tags are replaced.
    Expected Output:
    
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
    :param Bucket: [REQUIRED]\nThe bucket name.\n

    :type Tagging: dict
    :param Tagging: [REQUIRED]\nContainer for the TagSet and Tag elements.\n\nTagSet (list) -- [REQUIRED]A collection for a set of tags\n\n(dict) --A container of a key value name pair.\n\nKey (string) -- [REQUIRED]Name of the tag.\n\nValue (string) -- [REQUIRED]Value of the tag.\n\n\n\n\n\n\n

    :return: response = client.put_bucket_tagging(
        Bucket='examplebucket',
        Tagging={
            'TagSet': [
                {
                    'Key': 'Key1',
                    'Value': 'Value1',
                },
                {
                    'Key': 'Key2',
                    'Value': 'Value2',
                },
            ],
        },
    )
    
    print(response)
    
    
    :returns: 
    GetBucketTagging
    DeleteBucketTagging
    
    """
    pass

def put_bucket_versioning(Bucket=None, MFA=None, VersioningConfiguration=None):
    """
    Sets the versioning state of an existing bucket. To set the versioning state, you must be the bucket owner.
    You can set the versioning state with one of the following values:
    If the versioning state has never been set on a bucket, it has no versioning state; a  GetBucketVersioning request does not return a versioning state value.
    If the bucket owner enables MFA Delete in the bucket versioning configuration, the bucket owner must include the x-amz-mfa request header and the Status and the MfaDelete request elements in a request to set the versioning state of the bucket.
    See also: AWS API Documentation
    
    Examples
    The following example sets versioning configuration on bucket. The configuration enables versioning on the bucket.
    Expected Output:
    
    :example: response = client.put_bucket_versioning(
        Bucket='string',
        MFA='string',
        VersioningConfiguration={
            'MFADelete': 'Enabled'|'Disabled',
            'Status': 'Enabled'|'Suspended'
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name.\n

    :type MFA: string
    :param MFA: The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device.

    :type VersioningConfiguration: dict
    :param VersioningConfiguration: [REQUIRED]\nContainer for setting the versioning state.\n\nMFADelete (string) --Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned.\n\nStatus (string) --The versioning state of the bucket.\n\n\n

    :return: response = client.put_bucket_versioning(
        Bucket='examplebucket',
        VersioningConfiguration={
            'MFADelete': 'Disabled',
            'Status': 'Enabled',
        },
    )
    
    print(response)
    
    
    :returns: 
    Bucket (string) -- [REQUIRED]
    The bucket name.
    
    MFA (string) -- The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device.
    VersioningConfiguration (dict) -- [REQUIRED]
    Container for setting the versioning state.
    
    MFADelete (string) --Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned.
    
    Status (string) --The versioning state of the bucket.
    
    
    
    
    """
    pass

def put_bucket_website(Bucket=None, WebsiteConfiguration=None):
    """
    Sets the configuration of the website that is specified in the website subresource. To configure a bucket as a website, you can add this subresource on the bucket with website configuration information such as the file name of the index document and any redirect rules. For more information, see Hosting Websites on Amazon S3 .
    This PUT operation requires the S3:PutBucketWebsite permission. By default, only the bucket owner can configure the website attached to a bucket; however, bucket owners can allow other users to set the website configuration by writing a bucket policy that grants them the S3:PutBucketWebsite permission.
    To redirect all website requests sent to the bucket\'s website endpoint, you add a website configuration with the following elements. Because all requests are sent to another website, you don\'t need to provide index document name for the bucket.
    If you want granular control over redirects, you can use the following elements to add routing rules that describe conditions for redirecting requests and information about the redirect destination. In this case, the website configuration must provide an index document for the bucket, because some requests might not be redirected.
    Amazon S3 has a limitation of 50 routing rules per website configuration. If you require more than 50 routing rules, you can use object redirect. For more information, see Configuring an Object Redirect in the Amazon Simple Storage Service Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example adds website configuration to a bucket.
    Expected Output:
    
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
    :param Bucket: [REQUIRED]\nThe bucket name.\n

    :type WebsiteConfiguration: dict
    :param WebsiteConfiguration: [REQUIRED]\nContainer for the request.\n\nErrorDocument (dict) --The name of the error document for the website.\n\nKey (string) -- [REQUIRED]The object key name to use when a 4XX class error occurs.\n\n\n\nIndexDocument (dict) --The name of the index document for the website.\n\nSuffix (string) -- [REQUIRED]A suffix that is appended to a request that is for a directory on the website endpoint (for example,if the suffix is index.html and you make a request to samplebucket/images/ the data that is returned will be for the object with the key name images/index.html) The suffix must not be empty and must not include a slash character.\n\n\n\nRedirectAllRequestsTo (dict) --The redirect behavior for every request to this bucket\'s website endpoint.\n\nWarning\nIf you specify this property, you can\'t specify any other property.\n\n\nHostName (string) -- [REQUIRED]Name of the host where requests are redirected.\n\nProtocol (string) --Protocol to use when redirecting requests. The default is the protocol that is used in the original request.\n\n\n\nRoutingRules (list) --Rules that define when a redirect is applied and the redirect behavior.\n\n(dict) --Specifies the redirect behavior and when a redirect is applied.\n\nCondition (dict) --A container for describing a condition that must be met for the specified redirect to apply. For example, 1. If request is for pages in the /docs folder, redirect to the /documents folder. 2. If request results in HTTP error 4xx, redirect request to another host where you might process the error.\n\nHttpErrorCodeReturnedEquals (string) --The HTTP error code when the redirect is applied. In the event of an error, if the error code equals this value, then the specified redirect is applied. Required when parent element Condition is specified and sibling KeyPrefixEquals is not specified. If both are specified, then both must be true for the redirect to be applied.\n\nKeyPrefixEquals (string) --The object key name prefix when the redirect is applied. For example, to redirect requests for ExamplePage.html , the key prefix will be ExamplePage.html . To redirect request for all pages with the prefix docs/ , the key prefix will be /docs , which identifies all objects in the docs/ folder. Required when the parent element Condition is specified and sibling HttpErrorCodeReturnedEquals is not specified. If both conditions are specified, both must be true for the redirect to be applied.\n\n\n\nRedirect (dict) -- [REQUIRED]Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can specify a different error code to return.\n\nHostName (string) --The host name to use in the redirect request.\n\nHttpRedirectCode (string) --The HTTP redirect code to use on the response. Not required if one of the siblings is present.\n\nProtocol (string) --Protocol to use when redirecting requests. The default is the protocol that is used in the original request.\n\nReplaceKeyPrefixWith (string) --The object key prefix to use in the redirect request. For example, to redirect requests for all pages with prefix docs/ (objects in the docs/ folder) to documents/ , you can set a condition block with KeyPrefixEquals set to docs/ and in the Redirect set ReplaceKeyPrefixWith to /documents . Not required if one of the siblings is present. Can be present only if ReplaceKeyWith is not provided.\n\nReplaceKeyWith (string) --The specific object key to use in the redirect request. For example, redirect request to error.html . Not required if one of the siblings is present. Can be present only if ReplaceKeyPrefixWith is not provided.\n\n\n\n\n\n\n\n\n

    :return: response = client.put_bucket_website(
        Bucket='examplebucket',
        ContentMD5='',
        WebsiteConfiguration={
            'ErrorDocument': {
                'Key': 'error.html',
            },
            'IndexDocument': {
                'Suffix': 'index.html',
            },
        },
    )
    
    print(response)
    
    
    :returns: 
    WebsiteConfiguration
    IndexDocument
    Suffix
    ErrorDocument
    Key
    RoutingRules
    RoutingRule
    Condition
    HttpErrorCodeReturnedEquals
    KeyPrefixEquals
    Redirect
    Protocol
    HostName
    ReplaceKeyPrefixWith
    ReplaceKeyWith
    HttpRedirectCode
    
    """
    pass

def put_object(ACL=None, Body=None, Bucket=None, CacheControl=None, ContentDisposition=None, ContentEncoding=None, ContentLanguage=None, ContentLength=None, ContentMD5=None, ContentType=None, Expires=None, GrantFullControl=None, GrantRead=None, GrantReadACP=None, GrantWriteACP=None, Key=None, Metadata=None, ServerSideEncryption=None, StorageClass=None, WebsiteRedirectLocation=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, SSEKMSKeyId=None, SSEKMSEncryptionContext=None, RequestPayer=None, Tagging=None, ObjectLockMode=None, ObjectLockRetainUntilDate=None, ObjectLockLegalHoldStatus=None):
    """
    Adds an object to a bucket. You must have WRITE permissions on a bucket to add an object to it.
    Amazon S3 never adds partial objects; if you receive a success response, Amazon S3 added the entire object to the bucket.
    Amazon S3 is a distributed system. If it receives multiple write requests for the same object simultaneously, it overwrites all but the last object written. Amazon S3 does not provide object locking; if you need this, make sure to build it into your application layer or use versioning instead.
    To ensure that data is not corrupted traversing the network, use the Content-MD5 header. When you use this header, Amazon S3 checks the object against the provided MD5 value and, if they do not match, returns an error. Additionally, you can calculate the MD5 while putting an object to Amazon S3 and compare the returned ETag to the calculated MD5 value.
    You can optionally request server-side encryption. With server-side encryption, Amazon S3 encrypts your data as it writes it to disks in its data centers and decrypts the data when you access it. You have the option to provide your own encryption key or use AWS managed encryption keys. For more information, see Using Server-Side Encryption .
    You can use headers to grant ACL- based permissions. By default, all objects are private. Only the owner has full access control. When adding a new object, you can grant permissions to individual AWS accounts or to predefined groups defined by Amazon S3. These permissions are then added to the ACL on the object. For more information, see Access Control List (ACL) Overview and Managing ACLs Using the REST API .
    By default, Amazon S3 uses the STANDARD storage class to store newly created objects. The STANDARD storage class provides high durability and high availability. Depending on performance needs, you can specify a different storage class. For more information, see Storage Classes in the Amazon S3 Service Developer Guide .
    If you enable versioning for a bucket, Amazon S3 automatically generates a unique version ID for the object being stored. Amazon S3 returns this ID in the response. When you enable versioning for a bucket, if Amazon S3 receives multiple write requests for the same object simultaneously, it stores all of the objects.
    For more information about versioning, see Adding Objects to Versioning Enabled Buckets . For information about returning the versioning state of a bucket, see  GetBucketVersioning .
    See also: AWS API Documentation
    
    Examples
    The following example creates an object. If the bucket is versioning enabled, S3 returns version ID in response.
    Expected Output:
    The following example uploads an object. The request specifies optional request headers to directs S3 to use specific storage class and use server-side encryption.
    Expected Output:
    The following example uploads and object. The request specifies optional canned ACL (access control list) to all READ access to authenticated users. If the bucket is versioning enabled, S3 returns version ID in response.
    Expected Output:
    The following example uploads an object to a versioning-enabled bucket. The source file is specified using Windows file syntax. S3 returns VersionId of the newly created object.
    Expected Output:
    The following example creates an object. The request also specifies optional metadata. If the bucket is versioning enabled, S3 returns version ID in response.
    Expected Output:
    The following example uploads an object. The request specifies optional object tags. The bucket is versioned, therefore S3 returns version ID of the newly created object.
    Expected Output:
    The following example uploads and object. The request specifies the optional server-side encryption option. The request also specifies optional object tags. If the bucket is versioning enabled, S3 returns version ID in response.
    Expected Output:
    
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
        StorageClass='STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
        WebsiteRedirectLocation='string',
        SSECustomerAlgorithm='string',
        SSECustomerKey='string',
        SSEKMSKeyId='string',
        SSEKMSEncryptionContext='string',
        RequestPayer='requester',
        Tagging='string',
        ObjectLockMode='GOVERNANCE'|'COMPLIANCE',
        ObjectLockRetainUntilDate=datetime(2015, 1, 1),
        ObjectLockLegalHoldStatus='ON'|'OFF'
    )
    
    
    :type ACL: string
    :param ACL: The canned ACL to apply to the object. For more information, see Canned ACL .

    :type Body: bytes or seekable file-like object
    :param Body: Object data.

    :type Bucket: string
    :param Bucket: [REQUIRED]\nBucket name to which the PUT operation was initiated.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type CacheControl: string
    :param CacheControl: Can be used to specify caching behavior along the request/reply chain. For more information, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9 .

    :type ContentDisposition: string
    :param ContentDisposition: Specifies presentational information for the object. For more information, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1 .

    :type ContentEncoding: string
    :param ContentEncoding: Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. For more information, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11 .

    :type ContentLanguage: string
    :param ContentLanguage: The language the content is in.

    :type ContentLength: integer
    :param ContentLength: Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically. For more information, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.13 .

    :type ContentMD5: string
    :param ContentMD5: The base64-encoded 128-bit MD5 digest of the message (without the headers) according to RFC 1864. This header can be used as a message integrity check to verify that the data is the same data that was originally sent. Although it is optional, we recommend using the Content-MD5 mechanism as an end-to-end integrity check. For more information about REST request authentication, see REST Authentication .

    :type ContentType: string
    :param ContentType: A standard MIME type describing the format of the contents. For more information, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17 .

    :type Expires: datetime
    :param Expires: The date and time at which the object is no longer cacheable. For more information, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.21 .

    :type GrantFullControl: string
    :param GrantFullControl: Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.

    :type GrantRead: string
    :param GrantRead: Allows grantee to read the object data and its metadata.

    :type GrantReadACP: string
    :param GrantReadACP: Allows grantee to read the object ACL.

    :type GrantWriteACP: string
    :param GrantWriteACP: Allows grantee to write the ACL for the applicable object.

    :type Key: string
    :param Key: [REQUIRED]\nObject key for which the PUT operation was initiated.\n

    :type Metadata: dict
    :param Metadata: A map of metadata to store with the object in S3.\n\n(string) --\n(string) --\n\n\n\n

    :type ServerSideEncryption: string
    :param ServerSideEncryption: The server-side encryption algorithm used when storing this object in Amazon S3 (for example, AES256, aws:kms).

    :type StorageClass: string
    :param StorageClass: If you don\'t specify, S3 Standard is the default storage class. Amazon S3 supports other storage classes.

    :type WebsiteRedirectLocation: string
    :param WebsiteRedirectLocation: If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata. For information about object metadata, see Object Key and Metadata .\nIn the following example, the request header sets the redirect to an object (anotherPage.html) in the same bucket:\n\nx-amz-website-redirect-location: /anotherPage.html\nIn the following example, the request header sets the object redirect to another website:\n\nx-amz-website-redirect-location: http://www.example.com/\nFor more information about website hosting in Amazon S3, see Hosting Websites on Amazon S3 and How to Configure Website Page Redirects .\n

    :type SSECustomerAlgorithm: string
    :param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (for example, AES256).

    :type SSECustomerKey: string
    :param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side\xe2\x80\x8b-encryption\xe2\x80\x8b-customer-algorithm header.

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.\n\nPlease note that this parameter is automatically populated if it is not provided. Including this parameter is not required\n

    :type SSEKMSKeyId: string
    :param SSEKMSKeyId: If x-amz-server-side-encryption is present and has the value of aws:kms , this header specifies the ID of the AWS Key Management Service (AWS KMS) symmetrical customer managed customer master key (CMK) that was used for the object.\nIf the value of x-amz-server-side-encryption is aws:kms , this header specifies the ID of the symmetric customer managed AWS KMS CMK that will be used for the object. If you specify x-amz-server-side-encryption:aws:kms , but do not provide``x-amz-server-side-encryption-aws-kms-key-id`` , Amazon S3 uses the AWS managed CMK in AWS to protect the data.\n

    :type SSEKMSEncryptionContext: string
    :param SSEKMSEncryptionContext: Specifies the AWS KMS Encryption Context to use for object encryption. The value of this header is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :type Tagging: string
    :param Tagging: The tag-set for the object. The tag-set must be encoded as URL Query parameters. (For example, 'Key1=Value1')

    :type ObjectLockMode: string
    :param ObjectLockMode: The Object Lock mode that you want to apply to this object.

    :type ObjectLockRetainUntilDate: datetime
    :param ObjectLockRetainUntilDate: The date and time when you want this object\'s Object Lock to expire.

    :type ObjectLockLegalHoldStatus: string
    :param ObjectLockLegalHoldStatus: Specifies whether a legal hold will be applied to this object. For more information about S3 Object Lock, see Object Lock .

    :rtype: dict

ReturnsResponse Syntax
{
    'Expiration': 'string',
    'ETag': 'string',
    'ServerSideEncryption': 'AES256'|'aws:kms',
    'VersionId': 'string',
    'SSECustomerAlgorithm': 'string',
    'SSECustomerKeyMD5': 'string',
    'SSEKMSKeyId': 'string',
    'SSEKMSEncryptionContext': 'string',
    'RequestCharged': 'requester'
}


Response Structure

(dict) --

Expiration (string) --
If the expiration is configured for the object (see  PutBucketLifecycleConfiguration ), the response includes this header. It includes the expiry-date and rule-id key-value pairs that provide information about object expiration. The value of the rule-id is URL encoded.

ETag (string) --
Entity tag for the uploaded object.

ServerSideEncryption (string) --
If you specified server-side encryption either with an AWS KMS customer master key (CMK) or Amazon S3-managed encryption key in your PUT request, the response includes this header. It confirms the encryption algorithm that Amazon S3 used to encrypt the object.

VersionId (string) --
Version of the object.

SSECustomerAlgorithm (string) --
If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.

SSECustomerKeyMD5 (string) --
If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round-trip message integrity verification of the customer-provided encryption key.

SSEKMSKeyId (string) --
If x-amz-server-side-encryption is present and has the value of aws:kms , this header specifies the ID of the AWS Key Management Service (AWS KMS) symmetric customer managed customer master key (CMK) that was used for the object.

SSEKMSEncryptionContext (string) --
If present, specifies the AWS KMS Encryption Context to use for object encryption. The value of this header is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.







Examples
The following example creates an object. If the bucket is versioning enabled, S3 returns version ID in response.
response = client.put_object(
    Body='filetoupload',
    Bucket='examplebucket',
    Key='objectkey',
)

print(response)


Expected Output:
{
    'ETag': '"6805f2cfc46c0f04559748bb039d69ae"',
    'VersionId': 'Bvq0EDKxOcXLJXNo_Lkz37eM3R4pfzyQ',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example uploads an object. The request specifies optional request headers to directs S3 to use specific storage class and use server-side encryption.
response = client.put_object(
    Body='HappyFace.jpg',
    Bucket='examplebucket',
    Key='HappyFace.jpg',
    ServerSideEncryption='AES256',
    StorageClass='STANDARD_IA',
)

print(response)


Expected Output:
{
    'ETag': '"6805f2cfc46c0f04559748bb039d69ae"',
    'ServerSideEncryption': 'AES256',
    'VersionId': 'CG612hodqujkf8FaaNfp8U..FIhLROcp',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example uploads and object. The request specifies optional canned ACL (access control list) to all READ access to authenticated users. If the bucket is versioning enabled, S3 returns version ID in response.
response = client.put_object(
    ACL='authenticated-read',
    Body='filetoupload',
    Bucket='examplebucket',
    Key='exampleobject',
)

print(response)


Expected Output:
{
    'ETag': '"6805f2cfc46c0f04559748bb039d69ae"',
    'VersionId': 'Kirh.unyZwjQ69YxcQLA8z4F5j3kJJKr',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example uploads an object to a versioning-enabled bucket. The source file is specified using Windows file syntax. S3 returns VersionId of the newly created object.
response = client.put_object(
    Body='HappyFace.jpg',
    Bucket='examplebucket',
    Key='HappyFace.jpg',
)

print(response)


Expected Output:
{
    'ETag': '"6805f2cfc46c0f04559748bb039d69ae"',
    'VersionId': 'tpf3zF08nBplQK1XLOefGskR7mGDwcDk',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example creates an object. The request also specifies optional metadata. If the bucket is versioning enabled, S3 returns version ID in response.
response = client.put_object(
    Body='filetoupload',
    Bucket='examplebucket',
    Key='exampleobject',
    Metadata={
        'metadata1': 'value1',
        'metadata2': 'value2',
    },
)

print(response)


Expected Output:
{
    'ETag': '"6805f2cfc46c0f04559748bb039d69ae"',
    'VersionId': 'pSKidl4pHBiNwukdbcPXAIs.sshFFOc0',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example uploads an object. The request specifies optional object tags. The bucket is versioned, therefore S3 returns version ID of the newly created object.
response = client.put_object(
    Body='c:\\HappyFace.jpg',
    Bucket='examplebucket',
    Key='HappyFace.jpg',
    Tagging='key1=value1&key2=value2',
)

print(response)


Expected Output:
{
    'ETag': '"6805f2cfc46c0f04559748bb039d69ae"',
    'VersionId': 'psM2sYY4.o1501dSx8wMvnkOzSBB.V4a',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example uploads and object. The request specifies the optional server-side encryption option. The request also specifies optional object tags. If the bucket is versioning enabled, S3 returns version ID in response.
response = client.put_object(
    Body='filetoupload',
    Bucket='examplebucket',
    Key='exampleobject',
    ServerSideEncryption='AES256',
    Tagging='key1=value1&key2=value2',
)

print(response)


Expected Output:
{
    'ETag': '"6805f2cfc46c0f04559748bb039d69ae"',
    'ServerSideEncryption': 'AES256',
    'VersionId': 'Ri.vC6qVlA4dEnjgRV4ZHsHoFIjqEMNt',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Expiration': 'string',
        'ETag': 'string',
        'ServerSideEncryption': 'AES256'|'aws:kms',
        'VersionId': 'string',
        'SSECustomerAlgorithm': 'string',
        'SSECustomerKeyMD5': 'string',
        'SSEKMSKeyId': 'string',
        'SSEKMSEncryptionContext': 'string',
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    ACL (string) -- The canned ACL to apply to the object. For more information, see Canned ACL .
    Body (bytes or seekable file-like object) -- Object data.
    Bucket (string) -- [REQUIRED]
    Bucket name to which the PUT operation was initiated.
    When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
    
    CacheControl (string) -- Can be used to specify caching behavior along the request/reply chain. For more information, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9 .
    ContentDisposition (string) -- Specifies presentational information for the object. For more information, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1 .
    ContentEncoding (string) -- Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. For more information, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11 .
    ContentLanguage (string) -- The language the content is in.
    ContentLength (integer) -- Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically. For more information, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.13 .
    ContentMD5 (string) -- The base64-encoded 128-bit MD5 digest of the message (without the headers) according to RFC 1864. This header can be used as a message integrity check to verify that the data is the same data that was originally sent. Although it is optional, we recommend using the Content-MD5 mechanism as an end-to-end integrity check. For more information about REST request authentication, see REST Authentication .
    ContentType (string) -- A standard MIME type describing the format of the contents. For more information, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17 .
    Expires (datetime) -- The date and time at which the object is no longer cacheable. For more information, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.21 .
    GrantFullControl (string) -- Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
    GrantRead (string) -- Allows grantee to read the object data and its metadata.
    GrantReadACP (string) -- Allows grantee to read the object ACL.
    GrantWriteACP (string) -- Allows grantee to write the ACL for the applicable object.
    Key (string) -- [REQUIRED]
    Object key for which the PUT operation was initiated.
    
    Metadata (dict) -- A map of metadata to store with the object in S3.
    
    (string) --
    (string) --
    
    
    
    
    ServerSideEncryption (string) -- The server-side encryption algorithm used when storing this object in Amazon S3 (for example, AES256, aws:kms).
    StorageClass (string) -- If you don\'t specify, S3 Standard is the default storage class. Amazon S3 supports other storage classes.
    WebsiteRedirectLocation (string) -- If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata. For information about object metadata, see Object Key and Metadata .
    In the following example, the request header sets the redirect to an object (anotherPage.html) in the same bucket:
    
    x-amz-website-redirect-location: /anotherPage.html
    In the following example, the request header sets the object redirect to another website:
    
    x-amz-website-redirect-location: http://www.example.com/
    For more information about website hosting in Amazon S3, see Hosting Websites on Amazon S3 and How to Configure Website Page Redirects .
    
    SSECustomerAlgorithm (string) -- Specifies the algorithm to use to when encrypting the object (for example, AES256).
    SSECustomerKey (string) -- Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side\xe2\x80\x8b-encryption\xe2\x80\x8b-customer-algorithm header.
    SSECustomerKeyMD5 (string) -- Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.
    
    Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
    
    SSEKMSKeyId (string) -- If x-amz-server-side-encryption is present and has the value of aws:kms , this header specifies the ID of the AWS Key Management Service (AWS KMS) symmetrical customer managed customer master key (CMK) that was used for the object.
    If the value of x-amz-server-side-encryption is aws:kms , this header specifies the ID of the symmetric customer managed AWS KMS CMK that will be used for the object. If you specify x-amz-server-side-encryption:aws:kms , but do not provide``x-amz-server-side-encryption-aws-kms-key-id`` , Amazon S3 uses the AWS managed CMK in AWS to protect the data.
    
    SSEKMSEncryptionContext (string) -- Specifies the AWS KMS Encryption Context to use for object encryption. The value of this header is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.
    RequestPayer (string) -- Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .
    Tagging (string) -- The tag-set for the object. The tag-set must be encoded as URL Query parameters. (For example, "Key1=Value1")
    ObjectLockMode (string) -- The Object Lock mode that you want to apply to this object.
    ObjectLockRetainUntilDate (datetime) -- The date and time when you want this object\'s Object Lock to expire.
    ObjectLockLegalHoldStatus (string) -- Specifies whether a legal hold will be applied to this object. For more information about S3 Object Lock, see Object Lock .
    
    """
    pass

def put_object_acl(ACL=None, AccessControlPolicy=None, Bucket=None, GrantFullControl=None, GrantRead=None, GrantReadACP=None, GrantWrite=None, GrantWriteACP=None, Key=None, RequestPayer=None, VersionId=None):
    """
    Uses the acl subresource to set the access control list (ACL) permissions for an object that already exists in a bucket. You must have WRITE_ACP permission to set the ACL of an object.
    Depending on your application needs, you can choose to set the ACL on an object using either the request body or the headers. For example, if you have an existing application that updates a bucket ACL using the request body, you can continue to use that approach. For more information, see Access Control List (ACL) Overview in the Amazon S3 Developer Guide .
    You can set access permissions using one of the following methods:
    For example, the following x-amz-grant-read header grants list objects permission to the two AWS accounts identified by their email addresses.
    You can use either a canned ACL or specify access permissions explicitly. You cannot do both.
    You can specify the person (grantee) to whom you\'re assigning access rights (using request elements) in the following ways:
    The ACL of an object is set at the object version level. By default, PUT sets the ACL of the current version of an object. To set the ACL of a different version, use the versionId subresource.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example adds grants to an object ACL. The first permission grants user1 and user2 FULL_CONTROL and the AllUsers group READ permission.
    Expected Output:
    
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
    :param ACL: The canned ACL to apply to the object. For more information, see Canned ACL .

    :type AccessControlPolicy: dict
    :param AccessControlPolicy: Contains the elements that set the ACL permissions for an object per grantee.\n\nGrants (list) --A list of grants.\n\n(dict) --Container for grant information.\n\nGrantee (dict) --The person being granted permissions.\n\nDisplayName (string) --Screen name of the grantee.\n\nEmailAddress (string) --Email address of the grantee.\n\nNote\nUsing email addresses to specify a grantee is only supported in the following AWS Regions:\n\nUS East (N. Virginia)\nUS West (N. California)\nUS West (Oregon)\nAsia Pacific (Singapore)\nAsia Pacific (Sydney)\nAsia Pacific (Tokyo)\nEurope (Ireland)\nSouth America (S\xc3\xa3o Paulo)\n\nFor a list of all the Amazon S3 supported Regions and endpoints, see Regions and Endpoints in the AWS General Reference.\n\n\nID (string) --The canonical user ID of the grantee.\n\nType (string) -- [REQUIRED]Type of grantee\n\nURI (string) --URI of the grantee group.\n\n\n\nPermission (string) --Specifies the permission given to the grantee.\n\n\n\n\n\nOwner (dict) --Container for the bucket owner\'s display name and ID.\n\nDisplayName (string) --Container for the display name of the owner.\n\nID (string) --Container for the ID of the owner.\n\n\n\n\n

    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name that contains the object to which you want to attach the ACL.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

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
    :param Key: [REQUIRED]\nKey for which the PUT operation was initiated.\n

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :type VersionId: string
    :param VersionId: VersionId used to reference a specific version of the object.

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestCharged': 'requester'
}


Response Structure

(dict) --

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.







Exceptions

S3.Client.exceptions.NoSuchKey

Examples
The following example adds grants to an object ACL. The first permission grants user1 and user2 FULL_CONTROL and the AllUsers group READ permission.
response = client.put_object_acl(
    AccessControlPolicy={
    },
    Bucket='examplebucket',
    GrantFullControl='emailaddress=user1@example.com,emailaddress=user2@example.com',
    GrantRead='uri=http://acs.amazonaws.com/groups/global/AllUsers',
    Key='HappyFace.jpg',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    US East (N. Virginia)
    US West (N. California)
    US West (Oregon)
    Asia Pacific (Singapore)
    Asia Pacific (Sydney)
    Asia Pacific (Tokyo)
    Europe (Ireland)
    South America (S\xc3\xa3o Paulo)
    
    """
    pass

def put_object_legal_hold(Bucket=None, Key=None, LegalHold=None, RequestPayer=None, VersionId=None, ContentMD5=None):
    """
    Applies a Legal Hold configuration to the specified object.
    See also: AWS API Documentation
    
    
    :example: response = client.put_object_legal_hold(
        Bucket='string',
        Key='string',
        LegalHold={
            'Status': 'ON'|'OFF'
        },
        RequestPayer='requester',
        VersionId='string',
        ContentMD5='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name containing the object that you want to place a Legal Hold on.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Key: string
    :param Key: [REQUIRED]\nThe key name for the object that you want to place a Legal Hold on.\n

    :type LegalHold: dict
    :param LegalHold: Container element for the Legal Hold configuration you want to apply to the specified object.\n\nStatus (string) --Indicates whether the specified object has a Legal Hold in place.\n\n\n

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :type VersionId: string
    :param VersionId: The version ID of the object that you want to place a Legal Hold on.

    :type ContentMD5: string
    :param ContentMD5: The MD5 hash for the request body.

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestCharged': 'requester'
}


Response Structure

(dict) --

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.








    :return: {
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    Bucket (string) -- [REQUIRED]
    The bucket name containing the object that you want to place a Legal Hold on.
    When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
    
    Key (string) -- [REQUIRED]
    The key name for the object that you want to place a Legal Hold on.
    
    LegalHold (dict) -- Container element for the Legal Hold configuration you want to apply to the specified object.
    
    Status (string) --Indicates whether the specified object has a Legal Hold in place.
    
    
    
    RequestPayer (string) -- Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .
    VersionId (string) -- The version ID of the object that you want to place a Legal Hold on.
    ContentMD5 (string) -- The MD5 hash for the request body.
    
    """
    pass

def put_object_lock_configuration(Bucket=None, ObjectLockConfiguration=None, RequestPayer=None, Token=None, ContentMD5=None):
    """
    Places an Object Lock configuration on the specified bucket. The rule specified in the Object Lock configuration will be applied by default to every new object placed in the specified bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.put_object_lock_configuration(
        Bucket='string',
        ObjectLockConfiguration={
            'ObjectLockEnabled': 'Enabled',
            'Rule': {
                'DefaultRetention': {
                    'Mode': 'GOVERNANCE'|'COMPLIANCE',
                    'Days': 123,
                    'Years': 123
                }
            }
        },
        RequestPayer='requester',
        Token='string',
        ContentMD5='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket whose Object Lock configuration you want to create or replace.\n

    :type ObjectLockConfiguration: dict
    :param ObjectLockConfiguration: The Object Lock configuration that you want to apply to the specified bucket.\n\nObjectLockEnabled (string) --Indicates whether this bucket has an Object Lock configuration enabled.\n\nRule (dict) --The Object Lock rule in place for the specified object.\n\nDefaultRetention (dict) --The default retention period that you want to apply to new objects placed in the specified bucket.\n\nMode (string) --The default Object Lock retention mode you want to apply to new objects placed in the specified bucket.\n\nDays (integer) --The number of days that you want to specify for the default retention period.\n\nYears (integer) --The number of years that you want to specify for the default retention period.\n\n\n\n\n\n\n

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :type Token: string
    :param Token: A token to allow Object Lock to be enabled for an existing bucket.

    :type ContentMD5: string
    :param ContentMD5: The MD5 hash for the request body.

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestCharged': 'requester'
}


Response Structure

(dict) --

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.








    :return: {
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    Bucket (string) -- [REQUIRED]
    The bucket whose Object Lock configuration you want to create or replace.
    
    ObjectLockConfiguration (dict) -- The Object Lock configuration that you want to apply to the specified bucket.
    
    ObjectLockEnabled (string) --Indicates whether this bucket has an Object Lock configuration enabled.
    
    Rule (dict) --The Object Lock rule in place for the specified object.
    
    DefaultRetention (dict) --The default retention period that you want to apply to new objects placed in the specified bucket.
    
    Mode (string) --The default Object Lock retention mode you want to apply to new objects placed in the specified bucket.
    
    Days (integer) --The number of days that you want to specify for the default retention period.
    
    Years (integer) --The number of years that you want to specify for the default retention period.
    
    
    
    
    
    
    
    RequestPayer (string) -- Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .
    Token (string) -- A token to allow Object Lock to be enabled for an existing bucket.
    ContentMD5 (string) -- The MD5 hash for the request body.
    
    """
    pass

def put_object_retention(Bucket=None, Key=None, Retention=None, RequestPayer=None, VersionId=None, BypassGovernanceRetention=None, ContentMD5=None):
    """
    Places an Object Retention configuration on an object.
    See also: AWS API Documentation
    
    
    :example: response = client.put_object_retention(
        Bucket='string',
        Key='string',
        Retention={
            'Mode': 'GOVERNANCE'|'COMPLIANCE',
            'RetainUntilDate': datetime(2015, 1, 1)
        },
        RequestPayer='requester',
        VersionId='string',
        BypassGovernanceRetention=True|False,
        ContentMD5='string'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name that contains the object you want to apply this Object Retention configuration to.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Key: string
    :param Key: [REQUIRED]\nThe key name for the object that you want to apply this Object Retention configuration to.\n

    :type Retention: dict
    :param Retention: The container element for the Object Retention configuration.\n\nMode (string) --Indicates the Retention mode for the specified object.\n\nRetainUntilDate (datetime) --The date on which this Object Lock Retention will expire.\n\n\n

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :type VersionId: string
    :param VersionId: The version ID for the object that you want to apply this Object Retention configuration to.

    :type BypassGovernanceRetention: boolean
    :param BypassGovernanceRetention: Indicates whether this operation should bypass Governance-mode restrictions.

    :type ContentMD5: string
    :param ContentMD5: The MD5 hash for the request body.

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestCharged': 'requester'
}


Response Structure

(dict) --

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.








    :return: {
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    Bucket (string) -- [REQUIRED]
    The bucket name that contains the object you want to apply this Object Retention configuration to.
    When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
    
    Key (string) -- [REQUIRED]
    The key name for the object that you want to apply this Object Retention configuration to.
    
    Retention (dict) -- The container element for the Object Retention configuration.
    
    Mode (string) --Indicates the Retention mode for the specified object.
    
    RetainUntilDate (datetime) --The date on which this Object Lock Retention will expire.
    
    
    
    RequestPayer (string) -- Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .
    VersionId (string) -- The version ID for the object that you want to apply this Object Retention configuration to.
    BypassGovernanceRetention (boolean) -- Indicates whether this operation should bypass Governance-mode restrictions.
    ContentMD5 (string) -- The MD5 hash for the request body.
    
    """
    pass

def put_object_tagging(Bucket=None, Key=None, VersionId=None, ContentMD5=None, Tagging=None):
    """
    Sets the supplied tag-set to an object that already exists in a bucket.
    A tag is a key-value pair. You can associate tags with an object by sending a PUT request against the tagging subresource that is associated with the object. You can retrieve tags by sending a GET request. For more information, see  GetObjectTagging .
    For tagging-related restrictions related to characters and encodings, see Tag Restrictions . Note that Amazon S3 limits the maximum number of tags to 10 tags per object.
    To use this operation, you must have permission to perform the s3:PutObjectTagging action. By default, the bucket owner has this permission and can grant this permission to others.
    To put tags of any other version, use the versionId query parameter. You also need permission for the s3:PutObjectVersionTagging action.
    For information about the Amazon S3 object tagging feature, see Object Tagging .
    See also: AWS API Documentation
    
    Examples
    The following example adds tags to an existing object.
    Expected Output:
    
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
    :param Bucket: [REQUIRED]\nThe bucket name containing the object.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Key: string
    :param Key: [REQUIRED]\nName of the tag.\n

    :type VersionId: string
    :param VersionId: The versionId of the object that the tag-set will be added to.

    :type ContentMD5: string
    :param ContentMD5: The MD5 hash for the request body.

    :type Tagging: dict
    :param Tagging: [REQUIRED]\nContainer for the TagSet and Tag elements\n\nTagSet (list) -- [REQUIRED]A collection for a set of tags\n\n(dict) --A container of a key value name pair.\n\nKey (string) -- [REQUIRED]Name of the tag.\n\nValue (string) -- [REQUIRED]Value of the tag.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VersionId': 'string'
}


Response Structure

(dict) --

VersionId (string) --
The versionId of the object the tag-set was added to.







Examples
The following example adds tags to an existing object.
response = client.put_object_tagging(
    Bucket='examplebucket',
    Key='HappyFace.jpg',
    Tagging={
        'TagSet': [
            {
                'Key': 'Key3',
                'Value': 'Value3',
            },
            {
                'Key': 'Key4',
                'Value': 'Value4',
            },
        ],
    },
)

print(response)


Expected Output:
{
    'VersionId': 'null',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'VersionId': 'string'
    }
    
    
    :returns: 
    Code: MalformedXMLError
    Cause: The XML provided does not match the schema.
    
    """
    pass

def put_public_access_block(Bucket=None, ContentMD5=None, PublicAccessBlockConfiguration=None):
    """
    Creates or modifies the PublicAccessBlock configuration for an Amazon S3 bucket. To use this operation, you must have the s3:PutBucketPublicAccessBlock permission. For more information about Amazon S3 permissions, see Specifying Permissions in a Policy .
    For more information about when Amazon S3 considers a bucket or an object public, see The Meaning of "Public" .
    See also: AWS API Documentation
    
    
    :example: response = client.put_public_access_block(
        Bucket='string',
        ContentMD5='string',
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True|False,
            'IgnorePublicAcls': True|False,
            'BlockPublicPolicy': True|False,
            'RestrictPublicBuckets': True|False
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the Amazon S3 bucket whose PublicAccessBlock configuration you want to set.\n

    :type ContentMD5: string
    :param ContentMD5: The MD5 hash of the PutPublicAccessBlock request body.

    :type PublicAccessBlockConfiguration: dict
    :param PublicAccessBlockConfiguration: [REQUIRED]\nThe PublicAccessBlock configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see The Meaning of 'Public' in the Amazon Simple Storage Service Developer Guide .\n\nBlockPublicAcls (boolean) --Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket and objects in this bucket. Setting this element to TRUE causes the following behavior:\n\nPUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.\nPUT Object calls fail if the request includes a public ACL.\nPUT Bucket calls fail if the request includes a public ACL.\n\nEnabling this setting doesn\'t affect existing policies or ACLs.\n\nIgnorePublicAcls (boolean) --Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket. Setting this element to TRUE causes Amazon S3 to ignore all public ACLs on this bucket and objects in this bucket.\nEnabling this setting doesn\'t affect the persistence of any existing ACLs and doesn\'t prevent new public ACLs from being set.\n\nBlockPublicPolicy (boolean) --Specifies whether Amazon S3 should block public bucket policies for this bucket. Setting this element to TRUE causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.\nEnabling this setting doesn\'t affect existing bucket policies.\n\nRestrictPublicBuckets (boolean) --Specifies whether Amazon S3 should restrict public bucket policies for this bucket. Setting this element to TRUE restricts access to this bucket to only AWS services and authorized users within this account if the bucket has a public policy.\nEnabling this setting doesn\'t affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.\n\n\n

    :returns: 
    Bucket (string) -- [REQUIRED]
    The name of the Amazon S3 bucket whose PublicAccessBlock configuration you want to set.
    
    ContentMD5 (string) -- The MD5 hash of the PutPublicAccessBlock request body.
    PublicAccessBlockConfiguration (dict) -- [REQUIRED]
    The PublicAccessBlock configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see The Meaning of "Public" in the Amazon Simple Storage Service Developer Guide .
    
    BlockPublicAcls (boolean) --Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket and objects in this bucket. Setting this element to TRUE causes the following behavior:
    
    PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
    PUT Object calls fail if the request includes a public ACL.
    PUT Bucket calls fail if the request includes a public ACL.
    
    Enabling this setting doesn\'t affect existing policies or ACLs.
    
    IgnorePublicAcls (boolean) --Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket. Setting this element to TRUE causes Amazon S3 to ignore all public ACLs on this bucket and objects in this bucket.
    Enabling this setting doesn\'t affect the persistence of any existing ACLs and doesn\'t prevent new public ACLs from being set.
    
    BlockPublicPolicy (boolean) --Specifies whether Amazon S3 should block public bucket policies for this bucket. Setting this element to TRUE causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.
    Enabling this setting doesn\'t affect existing bucket policies.
    
    RestrictPublicBuckets (boolean) --Specifies whether Amazon S3 should restrict public bucket policies for this bucket. Setting this element to TRUE restricts access to this bucket to only AWS services and authorized users within this account if the bucket has a public policy.
    Enabling this setting doesn\'t affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.
    
    
    
    
    """
    pass

def restore_object(Bucket=None, Key=None, VersionId=None, RestoreRequest=None, RequestPayer=None):
    """
    Restores an archived copy of an object back into Amazon S3
    This operation performs the following types of requests:
    To use this operation, you must have permissions to perform the s3:RestoreObject action. The bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see Permissions Related to Bucket Subresource Operations and Managing Access Permissions to Your Amazon S3 Resources in the Amazon Simple Storage Service Developer Guide .
    You use a select type of request to perform SQL queries on archived objects. The archived objects that are being queried by the select request must be formatted as uncompressed comma-separated values (CSV) files. You can run queries and custom analytics on your archived data without having to restore your data to a hotter Amazon S3 tier. For an overview about select requests, see Querying Archived Objects in the Amazon Simple Storage Service Developer Guide .
    When making a select request, do the following:
    For more information about using SQL with S3 Glacier Select restore, see SQL Reference for Amazon S3 Select and S3 Glacier Select in the Amazon Simple Storage Service Developer Guide .
    When making a select request, you can also do the following:
    The following are additional important facts about the select feature:
    Objects in the GLACIER and DEEP_ARCHIVE storage classes are archived. To access an archived object, you must first initiate a restore request. This restores a temporary copy of the archived object. In a restore request, you specify the number of days that you want the restored copy to exist. After the specified period, Amazon S3 deletes the temporary copy but the object remains archived in the GLACIER or DEEP_ARCHIVE storage class that object was restored from.
    To restore a specific object version, you can provide a version ID. If you don\'t provide a version ID, Amazon S3 restores the current version.
    The time it takes restore jobs to finish depends on which storage class the object is being restored from and which data access tier you specify.
    When restoring an archived object (or using a select request), you can specify one of the following data access tier options in the Tier element of the request body:
    For more information about archive retrieval options and provisioned capacity for Expedited data access, see Restoring Archived Objects in the Amazon Simple Storage Service Developer Guide .
    You can use Amazon S3 restore speed upgrade to change the restore speed to a faster speed while it is in progress. You upgrade the speed of an in-progress restoration by issuing another restore request to the same object, setting a new Tier request element. When issuing a request to upgrade the restore tier, you must choose a tier that is faster than the tier that the in-progress restore is using. You must not change any other parameters, such as the Days request element. For more information, see Upgrading the Speed of an In-Progress Restore in the Amazon Simple Storage Service Developer Guide .
    To get the status of object restoration, you can send a HEAD request. Operations return the x-amz-restore header, which provides information about the restoration status, in the response. You can use Amazon S3 event notifications to notify you when a restore is initiated or completed. For more information, see Configuring Amazon S3 Event Notifications in the Amazon Simple Storage Service Developer Guide .
    After restoring an archived object, you can update the restoration period by reissuing the request with a new period. Amazon S3 updates the restoration period relative to the current time and charges only for the request-there are no data transfer charges. You cannot update the restoration period when Amazon S3 is actively processing your current restore request for the object.
    If your bucket has a lifecycle configuration with a rule that includes an expiration action, the object expiration overrides the life span that you specify in a restore request. For example, if you restore an object copy for 10 days, but the object is scheduled to expire in 3 days, Amazon S3 deletes the object in 3 days. For more information about lifecycle configuration, see  PutBucketLifecycleConfiguration and Object Lifecycle Management in Amazon Simple Storage Service Developer Guide .
    A successful operation returns either the 200 OK or 202 Accepted status code.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example restores for one day an archived copy of an object back into Amazon S3 bucket.
    Expected Output:
    
    :example: response = client.restore_object(
        Bucket='string',
        Key='string',
        VersionId='string',
        RestoreRequest={
            'Days': 123,
            'GlacierJobParameters': {
                'Tier': 'Standard'|'Bulk'|'Expedited'
            },
            'Type': 'SELECT',
            'Tier': 'Standard'|'Bulk'|'Expedited',
            'Description': 'string',
            'SelectParameters': {
                'InputSerialization': {
                    'CSV': {
                        'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                        'Comments': 'string',
                        'QuoteEscapeCharacter': 'string',
                        'RecordDelimiter': 'string',
                        'FieldDelimiter': 'string',
                        'QuoteCharacter': 'string',
                        'AllowQuotedRecordDelimiter': True|False
                    },
                    'CompressionType': 'NONE'|'GZIP'|'BZIP2',
                    'JSON': {
                        'Type': 'DOCUMENT'|'LINES'
                    },
                    'Parquet': {}
    
                },
                'ExpressionType': 'SQL',
                'Expression': 'string',
                'OutputSerialization': {
                    'CSV': {
                        'QuoteFields': 'ALWAYS'|'ASNEEDED',
                        'QuoteEscapeCharacter': 'string',
                        'RecordDelimiter': 'string',
                        'FieldDelimiter': 'string',
                        'QuoteCharacter': 'string'
                    },
                    'JSON': {
                        'RecordDelimiter': 'string'
                    }
                }
            },
            'OutputLocation': {
                'S3': {
                    'BucketName': 'string',
                    'Prefix': 'string',
                    'Encryption': {
                        'EncryptionType': 'AES256'|'aws:kms',
                        'KMSKeyId': 'string',
                        'KMSContext': 'string'
                    },
                    'CannedACL': 'private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'|'bucket-owner-read'|'bucket-owner-full-control',
                    'AccessControlList': [
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
                    'Tagging': {
                        'TagSet': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                    'UserMetadata': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ],
                    'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE'
                }
            }
        },
        RequestPayer='requester'
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe bucket name or containing the object to restore.\nWhen using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation using an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .\n

    :type Key: string
    :param Key: [REQUIRED]\nObject key for which the operation was initiated.\n

    :type VersionId: string
    :param VersionId: VersionId used to reference a specific version of the object.

    :type RestoreRequest: dict
    :param RestoreRequest: Container for restore job parameters.\n\nDays (integer) --Lifetime of the active copy in days. Do not use with restores that specify OutputLocation .\n\nGlacierJobParameters (dict) --S3 Glacier related parameters pertaining to this job. Do not use with restores that specify OutputLocation .\n\nTier (string) -- [REQUIRED]S3 Glacier retrieval tier at which the restore will be processed.\n\n\n\nType (string) --Type of restore request.\n\nTier (string) --S3 Glacier retrieval tier at which the restore will be processed.\n\nDescription (string) --The optional description for the job.\n\nSelectParameters (dict) --Describes the parameters for Select job types.\n\nInputSerialization (dict) -- [REQUIRED]Describes the serialization format of the object.\n\nCSV (dict) --Describes the serialization of a CSV-encoded object.\n\nFileHeaderInfo (string) --Describes the first line of input. Valid values are:\n\nNONE : First line is not a header.\nIGNORE : First line is a header, but you can\'t use the header values to indicate the column in an expression. You can use column position (such as _1, _2, \xe2\x80\xa6) to indicate the column (SELECT s._1 FROM OBJECT s ).\nUse : First line is a header, and you can use the header value to identify a column in an expression (SELECT 'name' FROM OBJECT ).\n\n\nComments (string) --A single character used to indicate that a row should be ignored when the character is present at the start of that row. You can specify any character to indicate a comment line.\n\nQuoteEscapeCharacter (string) --A single character used for escaping the quotation mark character inside an already escaped value. For example, the value ''' a , b ''' is parsed as ' a , b '.\n\nRecordDelimiter (string) --A single character used to separate individual records in the input. Instead of the default value, you can specify an arbitrary delimiter.\n\nFieldDelimiter (string) --A single character used to separate individual fields in a record. You can specify an arbitrary delimiter.\n\nQuoteCharacter (string) --A single character used for escaping when the field delimiter is part of the value. For example, if the value is a, b , Amazon S3 wraps this field value in quotation marks, as follows: ' a , b ' .\nType: String\nDefault: '\nAncestors: CSV\n\nAllowQuotedRecordDelimiter (boolean) --Specifies that CSV field values may contain quoted record delimiters and such records should be allowed. Default value is FALSE. Setting this value to TRUE may lower performance.\n\n\n\nCompressionType (string) --Specifies object\'s compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE.\n\nJSON (dict) --Specifies JSON as object\'s input serialization format.\n\nType (string) --The type of JSON. Valid values: Document, Lines.\n\n\n\nParquet (dict) --Specifies Parquet as object\'s input serialization format.\n\n\n\nExpressionType (string) -- [REQUIRED]The type of the provided expression (for example, SQL).\n\nExpression (string) -- [REQUIRED]The expression that is used to query the object.\n\nOutputSerialization (dict) -- [REQUIRED]Describes how the results of the Select job are serialized.\n\nCSV (dict) --Describes the serialization of CSV-encoded Select results.\n\nQuoteFields (string) --Indicates whether to use quotation marks around output fields.\n\nALWAYS : Always use quotation marks for output fields.\nASNEEDED : Use quotation marks for output fields when needed.\n\n\nQuoteEscapeCharacter (string) --The single character used for escaping the quote character inside an already escaped value.\n\nRecordDelimiter (string) --A single character used to separate individual records in the output. Instead of the default value, you can specify an arbitrary delimiter.\n\nFieldDelimiter (string) --The value used to separate individual fields in a record. You can specify an arbitrary delimiter.\n\nQuoteCharacter (string) --A single character used for escaping when the field delimiter is part of the value. For example, if the value is a, b , Amazon S3 wraps this field value in quotation marks, as follows: ' a , b ' .\n\n\n\nJSON (dict) --Specifies JSON as request\'s output serialization format.\n\nRecordDelimiter (string) --The value used to separate individual records in the output. If no value is specified, Amazon S3 uses a newline character (\'n\').\n\n\n\n\n\n\n\nOutputLocation (dict) --Describes the location where the restore job\'s output is stored.\n\nS3 (dict) --Describes an S3 location that will receive the results of the restore request.\n\nBucketName (string) -- [REQUIRED]The name of the bucket where the restore results will be placed.\n\nPrefix (string) -- [REQUIRED]The prefix that is prepended to the restore results for this request.\n\nEncryption (dict) --Contains the type of server-side encryption used.\n\nEncryptionType (string) -- [REQUIRED]The server-side encryption algorithm used when storing job results in Amazon S3 (for example, AES256, aws:kms).\n\nKMSKeyId (string) --If the encryption type is aws:kms , this optional value specifies the ID of the symmetric customer managed AWS KMS CMK to use for encryption of job results. Amazon S3 only supports symmetric CMKs. For more information, see Using Symmetric and Asymmetric Keys in the AWS Key Management Service Developer Guide .\n\nKMSContext (string) --If the encryption type is aws:kms , this optional value can be used to specify the encryption context for the restore results.\n\n\n\nCannedACL (string) --The canned ACL to apply to the restore results.\n\nAccessControlList (list) --A list of grants that control access to the staged results.\n\n(dict) --Container for grant information.\n\nGrantee (dict) --The person being granted permissions.\n\nDisplayName (string) --Screen name of the grantee.\n\nEmailAddress (string) --Email address of the grantee.\n\nNote\nUsing email addresses to specify a grantee is only supported in the following AWS Regions:\n\nUS East (N. Virginia)\nUS West (N. California)\nUS West (Oregon)\nAsia Pacific (Singapore)\nAsia Pacific (Sydney)\nAsia Pacific (Tokyo)\nEurope (Ireland)\nSouth America (S\xc3\xa3o Paulo)\n\nFor a list of all the Amazon S3 supported Regions and endpoints, see Regions and Endpoints in the AWS General Reference.\n\n\nID (string) --The canonical user ID of the grantee.\n\nType (string) -- [REQUIRED]Type of grantee\n\nURI (string) --URI of the grantee group.\n\n\n\nPermission (string) --Specifies the permission given to the grantee.\n\n\n\n\n\nTagging (dict) --The tag-set that is applied to the restore results.\n\nTagSet (list) -- [REQUIRED]A collection for a set of tags\n\n(dict) --A container of a key value name pair.\n\nKey (string) -- [REQUIRED]Name of the tag.\n\nValue (string) -- [REQUIRED]Value of the tag.\n\n\n\n\n\n\n\nUserMetadata (list) --A list of metadata to store with the restore results in S3.\n\n(dict) --A metadata key-value pair to store with an object.\n\nName (string) --Name of the Object.\n\nValue (string) --Value of the Object.\n\n\n\n\n\nStorageClass (string) --The class of storage used to store the restore results.\n\n\n\n\n\n\n

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestCharged': 'requester',
    'RestoreOutputPath': 'string'
}


Response Structure

(dict) --

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.

RestoreOutputPath (string) --
Indicates the path in the provided S3 output location where Select results will be restored to.







Exceptions

S3.Client.exceptions.ObjectAlreadyInActiveTierError

Examples
The following example restores for one day an archived copy of an object back into Amazon S3 bucket.
response = client.restore_object(
    Bucket='examplebucket',
    Key='archivedobjectkey',
    RestoreRequest={
        'Days': 1,
        'GlacierJobParameters': {
            'Tier': 'Expedited',
        },
    },
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'RequestCharged': 'requester',
        'RestoreOutputPath': 'string'
    }
    
    
    :returns: 
    Define an output location for the select query\'s output. This must be an Amazon S3 bucket in the same AWS Region as the bucket that contains the archive object that is being queried. The AWS account that initiates the job must have permissions to write to the S3 bucket. You can specify the storage class and encryption for the output objects stored in the bucket. For more information about output, see Querying Archived Objects in the Amazon Simple Storage Service Developer Guide . For more information about the S3 structure in the request body, see the following:
    PutObject
    Managing Access with ACLs in the Amazon Simple Storage Service Developer Guide
    Protecting Data Using Server-Side Encryption in the Amazon Simple Storage Service Developer Guide
    
    
    Define the SQL expression for the SELECT type of restoration for your query in the request body\'s SelectParameters structure. You can use expressions like the following examples.
    The following expression returns all records from the specified object.  SELECT * FROM Object
    Assuming that you are not using any headers for data stored in the object, you can specify columns with positional headers.  SELECT s._1, s._2 FROM Object s WHERE s._3 > 100
    If you have headers and you set the fileHeaderInfo in the CSV structure in the request body to USE , you can specify headers in the query. (If you set the fileHeaderInfo field to IGNORE , the first row is skipped for the query.) You cannot mix ordinal positions with header column names.   SELECT s.Id, s.FirstName, s.SSN FROM S3Object s
    
    
    
    """
    pass

def select_object_content(Bucket=None, Key=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, Expression=None, ExpressionType=None, RequestProgress=None, InputSerialization=None, OutputSerialization=None, ScanRange=None):
    """
    This operation filters the contents of an Amazon S3 object based on a simple structured query language (SQL) statement. In the request, along with the SQL expression, you must also specify a data serialization format (JSON, CSV, or Apache Parquet) of the object. Amazon S3 uses this format to parse object data into records, and returns only records that match the specified SQL expression. You must also specify the data serialization format for the response.
    For more information about Amazon S3 Select, see Selecting Content from Objects in the Amazon Simple Storage Service Developer Guide .
    For more information about using SQL with Amazon S3 Select, see SQL Reference for Amazon S3 Select and S3 Glacier Select in the Amazon Simple Storage Service Developer Guide .
    You must have s3:GetObject permission for this operation. Amazon S3 Select does not support anonymous access. For more information about permissions, see Specifying Permissions in a Policy in the Amazon Simple Storage Service Developer Guide .
    You can use Amazon S3 Select to query objects that have the following format properties:
    Given the response size is unknown, Amazon S3 Select streams the response as a series of messages and includes a Transfer-Encoding header with chunked as its value in the response. For more information, see  RESTSelectObjectAppendix .
    The SelectObjectContent operation does not support the following GetObject functionality. For more information, see  GetObject .
    For a list of special errors for this operation, see  SelectObjectContentErrorCodeList
    See also: AWS API Documentation
    
    
    :example: response = client.select_object_content(
        Bucket='string',
        Key='string',
        SSECustomerAlgorithm='string',
        SSECustomerKey='string',
        Expression='string',
        ExpressionType='SQL',
        RequestProgress={
            'Enabled': True|False
        },
        InputSerialization={
            'CSV': {
                'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                'Comments': 'string',
                'QuoteEscapeCharacter': 'string',
                'RecordDelimiter': 'string',
                'FieldDelimiter': 'string',
                'QuoteCharacter': 'string',
                'AllowQuotedRecordDelimiter': True|False
            },
            'CompressionType': 'NONE'|'GZIP'|'BZIP2',
            'JSON': {
                'Type': 'DOCUMENT'|'LINES'
            },
            'Parquet': {}
    
        },
        OutputSerialization={
            'CSV': {
                'QuoteFields': 'ALWAYS'|'ASNEEDED',
                'QuoteEscapeCharacter': 'string',
                'RecordDelimiter': 'string',
                'FieldDelimiter': 'string',
                'QuoteCharacter': 'string'
            },
            'JSON': {
                'RecordDelimiter': 'string'
            }
        },
        ScanRange={
            'Start': 123,
            'End': 123
        }
    )
    
    
    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe S3 bucket.\n

    :type Key: string
    :param Key: [REQUIRED]\nThe object key.\n

    :type SSECustomerAlgorithm: string
    :param SSECustomerAlgorithm: The SSE Algorithm used to encrypt the object. For more information, see Server-Side Encryption (Using Customer-Provided Encryption Keys .

    :type SSECustomerKey: string
    :param SSECustomerKey: The SSE Customer Key. For more information, see Server-Side Encryption (Using Customer-Provided Encryption Keys .

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: The SSE Customer Key MD5. For more information, see Server-Side Encryption (Using Customer-Provided Encryption Keys .\n\nPlease note that this parameter is automatically populated if it is not provided. Including this parameter is not required\n

    :type Expression: string
    :param Expression: [REQUIRED]\nThe expression that is used to query the object.\n

    :type ExpressionType: string
    :param ExpressionType: [REQUIRED]\nThe type of the provided expression (for example, SQL).\n

    :type RequestProgress: dict
    :param RequestProgress: Specifies if periodic request progress information should be enabled.\n\nEnabled (boolean) --Specifies whether periodic QueryProgress frames should be sent. Valid values: TRUE, FALSE. Default value: FALSE.\n\n\n

    :type InputSerialization: dict
    :param InputSerialization: [REQUIRED]\nDescribes the format of the data in the object that is being queried.\n\nCSV (dict) --Describes the serialization of a CSV-encoded object.\n\nFileHeaderInfo (string) --Describes the first line of input. Valid values are:\n\nNONE : First line is not a header.\nIGNORE : First line is a header, but you can\'t use the header values to indicate the column in an expression. You can use column position (such as _1, _2, \xe2\x80\xa6) to indicate the column (SELECT s._1 FROM OBJECT s ).\nUse : First line is a header, and you can use the header value to identify a column in an expression (SELECT 'name' FROM OBJECT ).\n\n\nComments (string) --A single character used to indicate that a row should be ignored when the character is present at the start of that row. You can specify any character to indicate a comment line.\n\nQuoteEscapeCharacter (string) --A single character used for escaping the quotation mark character inside an already escaped value. For example, the value ''' a , b ''' is parsed as ' a , b '.\n\nRecordDelimiter (string) --A single character used to separate individual records in the input. Instead of the default value, you can specify an arbitrary delimiter.\n\nFieldDelimiter (string) --A single character used to separate individual fields in a record. You can specify an arbitrary delimiter.\n\nQuoteCharacter (string) --A single character used for escaping when the field delimiter is part of the value. For example, if the value is a, b , Amazon S3 wraps this field value in quotation marks, as follows: ' a , b ' .\nType: String\nDefault: '\nAncestors: CSV\n\nAllowQuotedRecordDelimiter (boolean) --Specifies that CSV field values may contain quoted record delimiters and such records should be allowed. Default value is FALSE. Setting this value to TRUE may lower performance.\n\n\n\nCompressionType (string) --Specifies object\'s compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE.\n\nJSON (dict) --Specifies JSON as object\'s input serialization format.\n\nType (string) --The type of JSON. Valid values: Document, Lines.\n\n\n\nParquet (dict) --Specifies Parquet as object\'s input serialization format.\n\n\n

    :type OutputSerialization: dict
    :param OutputSerialization: [REQUIRED]\nDescribes the format of the data that you want Amazon S3 to return in response.\n\nCSV (dict) --Describes the serialization of CSV-encoded Select results.\n\nQuoteFields (string) --Indicates whether to use quotation marks around output fields.\n\nALWAYS : Always use quotation marks for output fields.\nASNEEDED : Use quotation marks for output fields when needed.\n\n\nQuoteEscapeCharacter (string) --The single character used for escaping the quote character inside an already escaped value.\n\nRecordDelimiter (string) --A single character used to separate individual records in the output. Instead of the default value, you can specify an arbitrary delimiter.\n\nFieldDelimiter (string) --The value used to separate individual fields in a record. You can specify an arbitrary delimiter.\n\nQuoteCharacter (string) --A single character used for escaping when the field delimiter is part of the value. For example, if the value is a, b , Amazon S3 wraps this field value in quotation marks, as follows: ' a , b ' .\n\n\n\nJSON (dict) --Specifies JSON as request\'s output serialization format.\n\nRecordDelimiter (string) --The value used to separate individual records in the output. If no value is specified, Amazon S3 uses a newline character (\'n\').\n\n\n\n\n

    :type ScanRange: dict
    :param ScanRange: Specifies the byte range of the object to get the records from. A record is processed when its first byte is contained by the range. This parameter is optional, but when specified, it must not be empty. See RFC 2616, Section 14.35.1 about how to specify the start and end of the range.\n\nScanRange may be used in the following ways:\n\n<scanrange><start>50</start><end>100</end></scanrange> - process only the records starting between the bytes 50 and 100 (inclusive, counting from zero)\n<scanrange><start>50</start></scanrange> - process only the records starting after the byte 50\n<scanrange><end>50</end></scanrange> - process only the records within the last 50 bytes of the file.\n\n\nStart (integer) --Specifies the start of the byte range. This parameter is optional. Valid values: non-negative integers. The default value is 0. If only start is supplied, it means scan from that point to the end of the file.For example; <scanrange><start>50</start></scanrange> means scan from byte 50 until the end of the file.\n\nEnd (integer) --Specifies the end of the byte range. This parameter is optional. Valid values: non-negative integers. The default value is one less than the size of the object being queried. If only the End parameter is supplied, it is interpreted to mean scan the last N bytes of the file. For example, <scanrange><end>50</end></scanrange> means scan the last 50 bytes.\n\n\n

    :rtype: dict

ReturnsThe response of this operation contains an EventStream member. When iterated the EventStream will yield events based on the structure below, where only one of the top level keys will be present for any given event.
Response Syntax
{
    'Payload': EventStream({
        'Records': {
            'Payload': b'bytes'
        },
        'Stats': {
            'Details': {
                'BytesScanned': 123,
                'BytesProcessed': 123,
                'BytesReturned': 123
            }
        },
        'Progress': {
            'Details': {
                'BytesScanned': 123,
                'BytesProcessed': 123,
                'BytesReturned': 123
            }
        },
        'Cont': {},
        'End': {}
    })
}


Response Structure

(dict) --

Payload (EventStream) --
The array of results.

Records (dict) --
The Records Event.

Payload (bytes) --
The byte array of partial, one or more result records.



Stats (dict) --
The Stats Event.

Details (dict) --
The Stats event details.

BytesScanned (integer) --
The total number of object bytes scanned.

BytesProcessed (integer) --
The total number of uncompressed object bytes processed.

BytesReturned (integer) --
The total number of bytes of records payload data returned.





Progress (dict) --
The Progress Event.

Details (dict) --
The Progress event details.

BytesScanned (integer) --
The current number of object bytes scanned.

BytesProcessed (integer) --
The current number of uncompressed object bytes processed.

BytesReturned (integer) --
The current number of bytes of records payload data returned.





Cont (dict) --
The Continuation Event.

End (dict) --
The End Event.










    :return: {
        'Payload': EventStream({
            'Records': {
                'Payload': b'bytes'
            },
            'Stats': {
                'Details': {
                    'BytesScanned': 123,
                    'BytesProcessed': 123,
                    'BytesReturned': 123
                }
            },
            'Progress': {
                'Details': {
                    'BytesScanned': 123,
                    'BytesProcessed': 123,
                    'BytesReturned': 123
                }
            },
            'Cont': {},
            'End': {}
        })
    }
    
    
    :returns: 
    Range : Although you can specify a scan range for an Amazon S3 Select request (see  SelectObjectContentRequest$ScanRange in the request parameters), you cannot specify the range of bytes of an object to return.
    GLACIER, DEEP_ARCHIVE and REDUCED_REDUNDANCY storage classes: You cannot specify the GLACIER, DEEP_ARCHIVE, or REDUCED_REDUNDANCY storage classes. For more information, about storage classes see Storage Classes in the Amazon Simple Storage Service Developer Guide .
    
    """
    pass

def upload_file(Filename=None, Bucket=None, Key=None, ExtraArgs=None, Callback=None, Config=None):
    """
    Upload a file to an S3 object.
    :
    Similar behavior as S3Transfer\'s upload_file() method,
    except that parameters are capitalized. Detailed examples can be found at
    S3Transfer\'s .
    
    :example: import boto3
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')
    
    
    :type Filename: str
    :param Filename: The path to the file to upload.

    :type Bucket: str
    :param Bucket: The name of the bucket to upload to.

    :type Key: str
    :param Key: The name of the key to upload to.

    :type ExtraArgs: dict
    :param ExtraArgs: Extra arguments that may be passed to the\nclient operation.

    :type Callback: function
    :param Callback: A method which takes a number of bytes transferred to\nbe periodically called during the upload.

    :type Config: boto3.s3.transfer.TransferConfig
    :param Config: The transfer configuration to be used when performing the\ntransfer.

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
    :param Fileobj: A file-like object to upload. At a minimum, it must\nimplement the read method, and must return bytes.

    :type Bucket: str
    :param Bucket: The name of the bucket to upload to.

    :type Key: str
    :param Key: The name of the key to upload to.

    :type ExtraArgs: dict
    :param ExtraArgs: Extra arguments that may be passed to the\nclient operation.

    :type Callback: function
    :param Callback: A method which takes a number of bytes transferred to\nbe periodically called during the upload.

    :type Config: boto3.s3.transfer.TransferConfig
    :param Config: The transfer configuration to be used when performing the\nupload.

    """
    pass

def upload_part(Body=None, Bucket=None, ContentLength=None, ContentMD5=None, Key=None, PartNumber=None, UploadId=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, RequestPayer=None):
    """
    Uploads a part in a multipart upload.
    You must initiate a multipart upload (see  CreateMultipartUpload ) before you can upload any part. In response to your initiate request, Amazon S3 returns an upload ID, a unique identifier, that you must include in your upload part request.
    Part numbers can be any number from 1 to 10,000, inclusive. A part number uniquely identifies a part and also defines its position within the object being created. If you upload a new part using the same part number that was used with a previous part, the previously uploaded part is overwritten. Each part must be at least 5 MB in size, except the last part. There is no size limit on the last part of your multipart upload.
    To ensure that data is not corrupted when traversing the network, specify the Content-MD5 header in the upload part request. Amazon S3 checks the part data against the provided MD5 value. If they do not match, Amazon S3 returns an error.
    For more information on multipart uploads, go to Multipart Upload Overview in the Amazon Simple Storage Service Developer Guide .
    For information on the permissions required to use the multipart upload API, go to Multipart Upload API and Permissions in the Amazon Simple Storage Service Developer Guide .
    You can optionally request server-side encryption where Amazon S3 encrypts your data as it writes it to disks in its data centers and decrypts it for you when you access it. You have the option of providing your own encryption key, or you can use the AWS managed encryption keys. If you choose to provide your own encryption key, the request headers you provide in the request must match the headers you used in the request to initiate the upload by using  CreateMultipartUpload . For more information, go to Using Server-Side Encryption in the Amazon Simple Storage Service Developer Guide .
    Server-side encryption is supported by the S3 Multipart Upload actions. Unless you are using a customer-provided encryption key, you don\'t need to specify the encryption parameters in each UploadPart request. Instead, you only need to specify the server-side encryption parameters in the initial Initiate Multipart request. For more information, see  CreateMultipartUpload .
    If you requested server-side encryption using a customer-provided encryption key in your initiate multipart upload request, you must provide identical encryption information in each part upload using the following headers.
    See also: AWS API Documentation
    
    Examples
    The following example uploads part 1 of a multipart upload. The example specifies a file name for the part data. The Upload ID is same that is returned by the initiate multipart upload.
    Expected Output:
    
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
    :param Bucket: [REQUIRED]\nName of the bucket to which the multipart upload was initiated.\n

    :type ContentLength: integer
    :param ContentLength: Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically.

    :type ContentMD5: string
    :param ContentMD5: The base64-encoded 128-bit MD5 digest of the part data. This parameter is auto-populated when using the command from the CLI. This parameter is required if object lock parameters are specified.

    :type Key: string
    :param Key: [REQUIRED]\nObject key for which the multipart upload was initiated.\n

    :type PartNumber: integer
    :param PartNumber: [REQUIRED]\nPart number of part being uploaded. This is a positive integer between 1 and 10,000.\n

    :type UploadId: string
    :param UploadId: [REQUIRED]\nUpload ID identifying the multipart upload whose part is being uploaded.\n

    :type SSECustomerAlgorithm: string
    :param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (for example, AES256).

    :type SSECustomerKey: string
    :param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side\xe2\x80\x8b-encryption\xe2\x80\x8b-customer-algorithm header . This must be the same encryption key specified in the initiate multipart upload request.

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.\n\nPlease note that this parameter is automatically populated if it is not provided. Including this parameter is not required\n

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :rtype: dict

ReturnsResponse Syntax
{
    'ServerSideEncryption': 'AES256'|'aws:kms',
    'ETag': 'string',
    'SSECustomerAlgorithm': 'string',
    'SSECustomerKeyMD5': 'string',
    'SSEKMSKeyId': 'string',
    'RequestCharged': 'requester'
}


Response Structure

(dict) --

ServerSideEncryption (string) --
The server-side encryption algorithm used when storing this object in Amazon S3 (for example, AES256, aws:kms).

ETag (string) --
Entity tag for the uploaded object.

SSECustomerAlgorithm (string) --
If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.

SSECustomerKeyMD5 (string) --
If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round-trip message integrity verification of the customer-provided encryption key.

SSEKMSKeyId (string) --
If present, specifies the ID of the AWS Key Management Service (AWS KMS) symmetric customer managed customer master key (CMK) was used for the object.

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.







Examples
The following example uploads part 1 of a multipart upload. The example specifies a file name for the part data. The Upload ID is same that is returned by the initiate multipart upload.
response = client.upload_part(
    Body='fileToUpload',
    Bucket='examplebucket',
    Key='examplelargeobject',
    PartNumber='1',
    UploadId='xadcOB_7YPBOJuoFiQ9cz4P3Pe6FIZwO4f7wN93uHsNBEw97pl5eNwzExg0LAT2dUN91cOmrEQHDsP3WA60CEg--',
)

print(response)


Expected Output:
{
    'ETag': '"d8c2eafd90c266e19ab9dcacc479f8af"',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ServerSideEncryption': 'AES256'|'aws:kms',
        'ETag': 'string',
        'SSECustomerAlgorithm': 'string',
        'SSECustomerKeyMD5': 'string',
        'SSEKMSKeyId': 'string',
        'RequestCharged': 'requester'
    }
    
    
    :returns: 
    Code: NoSuchUpload
    Cause: The specified multipart upload does not exist. The upload ID might be invalid, or the multipart upload might have been aborted or completed.
    HTTP Status Code: 404 Not Found
    SOAP Fault Code Prefix: Client
    
    """
    pass

def upload_part_copy(Bucket=None, CopySource=None, CopySourceIfMatch=None, CopySourceIfModifiedSince=None, CopySourceIfNoneMatch=None, CopySourceIfUnmodifiedSince=None, CopySourceRange=None, Key=None, PartNumber=None, UploadId=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, CopySourceSSECustomerAlgorithm=None, CopySourceSSECustomerKey=None, CopySourceSSECustomerKeyMD5=None, RequestPayer=None):
    """
    Uploads a part by copying data from an existing object as data source. You specify the data source by adding the request header x-amz-copy-source in your request and a byte range by adding the request header x-amz-copy-source-range in your request.
    The minimum allowable part size for a multipart upload is 5 MB. For more information about multipart upload limits, go to Quick Facts in the Amazon Simple Storage Service Developer Guide .
    You must initiate a multipart upload before you can upload any part. In response to your initiate request. Amazon S3 returns a unique identifier, the upload ID, that you must include in your upload part request.
    For more information about using the UploadPartCopy operation, see the following:
    Note the following additional considerations about the request headers x-amz-copy-source-if-match , x-amz-copy-source-if-none-match , x-amz-copy-source-if-unmodified-since , and x-amz-copy-source-if-modified-since :
    If your bucket has versioning enabled, you could have multiple versions of the same object. By default, x-amz-copy-source identifies the current version of the object to copy. If the current version is a delete marker and you don\'t specify a versionId in the x-amz-copy-source , Amazon S3 returns a 404 error, because the object does not exist. If you specify versionId in the x-amz-copy-source and the versionId is a delete marker, Amazon S3 returns an HTTP 400 error, because you are not allowed to specify a delete marker as a version for the x-amz-copy-source .
    You can optionally specify a specific version of the source object to copy by adding the versionId subresource as shown in the following example:
    See also: AWS API Documentation
    
    Examples
    The following example uploads a part of a multipart upload by copying data from an existing object as data source.
    Expected Output:
    The following example uploads a part of a multipart upload by copying a specified byte range from an existing object as data source.
    Expected Output:
    
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
    :param Bucket: [REQUIRED]\nThe bucket name.\n

    :type CopySource: str or dict
    :param CopySource: [REQUIRED] The name of the source bucket, key name of the source object, and optional version ID of the source object. You can either provide this value as a string or a dictionary. The string form is {bucket}/{key} or {bucket}/{key}?versionId={versionId} if you want to copy a specific version. You can also provide this value as a dictionary. The dictionary format is recommended over the string format because it is more explicit. The dictionary format is: {\'Bucket\': \'bucket\', \'Key\': \'key\', \'VersionId\': \'id\'}. Note that the VersionId key is optional and may be omitted.

    :type CopySourceIfMatch: string
    :param CopySourceIfMatch: Copies the object if its entity tag (ETag) matches the specified tag.

    :type CopySourceIfModifiedSince: datetime
    :param CopySourceIfModifiedSince: Copies the object if it has been modified since the specified time.

    :type CopySourceIfNoneMatch: string
    :param CopySourceIfNoneMatch: Copies the object if its entity tag (ETag) is different than the specified ETag.

    :type CopySourceIfUnmodifiedSince: datetime
    :param CopySourceIfUnmodifiedSince: Copies the object if it hasn\'t been modified since the specified time.

    :type CopySourceRange: string
    :param CopySourceRange: The range of bytes to copy from the source object. The range value must use the form bytes=first-last, where the first and last are the zero-based byte offsets to copy. For example, bytes=0-9 indicates that you want to copy the first 10 bytes of the source. You can copy a range only if the source object is greater than 5 MB.

    :type Key: string
    :param Key: [REQUIRED]\nObject key for which the multipart upload was initiated.\n

    :type PartNumber: integer
    :param PartNumber: [REQUIRED]\nPart number of part being copied. This is a positive integer between 1 and 10,000.\n

    :type UploadId: string
    :param UploadId: [REQUIRED]\nUpload ID identifying the multipart upload whose part is being copied.\n

    :type SSECustomerAlgorithm: string
    :param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (for example, AES256).

    :type SSECustomerKey: string
    :param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side\xe2\x80\x8b-encryption\xe2\x80\x8b-customer-algorithm header. This must be the same encryption key specified in the initiate multipart upload request.

    :type SSECustomerKeyMD5: string
    :param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.\n\nPlease note that this parameter is automatically populated if it is not provided. Including this parameter is not required\n

    :type CopySourceSSECustomerAlgorithm: string
    :param CopySourceSSECustomerAlgorithm: Specifies the algorithm to use when decrypting the source object (for example, AES256).

    :type CopySourceSSECustomerKey: string
    :param CopySourceSSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.

    :type CopySourceSSECustomerKeyMD5: string
    :param CopySourceSSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.\n\nPlease note that this parameter is automatically populated if it is not provided. Including this parameter is not required\n

    :type RequestPayer: string
    :param RequestPayer: Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets in the Amazon S3 Developer Guide .

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

CopySourceVersionId (string) --
The version of the source object that was copied, if you have enabled versioning on the source bucket.

CopyPartResult (dict) --
Container for all response elements.

ETag (string) --
Entity tag of the object.

LastModified (datetime) --
Date and time at which the object was uploaded.



ServerSideEncryption (string) --
The server-side encryption algorithm used when storing this object in Amazon S3 (for example, AES256, aws:kms).

SSECustomerAlgorithm (string) --
If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.

SSECustomerKeyMD5 (string) --
If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round-trip message integrity verification of the customer-provided encryption key.

SSEKMSKeyId (string) --
If present, specifies the ID of the AWS Key Management Service (AWS KMS) symmetric customer managed customer master key (CMK) that was used for the object.

RequestCharged (string) --
If present, indicates that the requester was successfully charged for the request.







Examples
The following example uploads a part of a multipart upload by copying data from an existing object as data source.
response = client.upload_part_copy(
    Bucket='examplebucket',
    CopySource='/bucketname/sourceobjectkey',
    Key='examplelargeobject',
    PartNumber='1',
    UploadId='exampleuoh_10OhKhT7YukE9bjzTPRiuaCotmZM_pFngJFir9OZNrSr5cWa3cq3LZSUsfjI4FI7PkP91We7Nrw--',
)

print(response)


Expected Output:
{
    'CopyPartResult': {
        'ETag': '"b0c6f0e7e054ab8fa2536a2677f8734d"',
        'LastModified': datetime(2016, 12, 29, 21, 24, 43, 3, 364, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example uploads a part of a multipart upload by copying a specified byte range from an existing object as data source.
response = client.upload_part_copy(
    Bucket='examplebucket',
    CopySource='/bucketname/sourceobjectkey',
    CopySourceRange='bytes=1-100000',
    Key='examplelargeobject',
    PartNumber='2',
    UploadId='exampleuoh_10OhKhT7YukE9bjzTPRiuaCotmZM_pFngJFir9OZNrSr5cWa3cq3LZSUsfjI4FI7PkP91We7Nrw--',
)

print(response)


Expected Output:
{
    'CopyPartResult': {
        'ETag': '"65d16d19e65a7508a51f043180edcc36"',
        'LastModified': datetime(2016, 12, 29, 21, 44, 28, 3, 364, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    Consideration 1 - If both of the x-amz-copy-source-if-match and x-amz-copy-source-if-unmodified-since headers are present in the request as follows:  x-amz-copy-source-if-match condition evaluates to true , and;  x-amz-copy-source-if-unmodified-since condition evaluates to false ; Amazon S3 returns 200 OK and copies the data.
    Consideration 2 - If both of the x-amz-copy-source-if-none-match and x-amz-copy-source-if-modified-since headers are present in the request as follows:  x-amz-copy-source-if-none-match condition evaluates to false , and;  x-amz-copy-source-if-modified-since condition evaluates to true ; Amazon S3 returns 412 Precondition Failed response code.
    
    """
    pass

