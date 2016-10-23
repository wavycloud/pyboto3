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


def abort_multipart_upload(Bucket=None, Key=None, UploadId=None, RequestPayer=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param Key: [REQUIRED]
:type Key: string
:param UploadId: [REQUIRED]
:type UploadId: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
"""


def can_paginate(operation_name=None): pass


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


def complete_multipart_upload(Bucket=None, Key=None, MultipartUpload=None, UploadId=None, RequestPayer=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param Key: [REQUIRED]
:type Key: string
:param MultipartUpload: 
            Parts (list) --
            (dict) --
            ETag (string) -- Entity tag returned when the part was uploaded.
            PartNumber (integer) -- Part number that identifies the part. This is a positive integer between 1 and 10,000.
            
            
:type MultipartUpload: dict
:param UploadId: [REQUIRED]
:type UploadId: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
"""


def copy(CopySource=None, Bucket=None, Key=None, ExtraArgs=None, Callback=None, SourceClient=None, Config=None): pass


"""
:param CopySource: The name of the source bucket, key name of the
            source object, and optional version ID of the source object. The
            dictionary format is:
            {'Bucket': 'bucket', 'Key': 'key', 'VersionId': 'id'}. Note
            that the VersionId key is optional and may be omitted.
:type CopySource: dict
:param Bucket: The name of the bucket to copy to
:type Bucket: str
:param Key: The name of the key to copy to
:type Key: str
:param ExtraArgs: Extra arguments that may be passed to the
            client operation
:type ExtraArgs: dict
:param Callback: A method which takes a number of bytes transferred to
            be periodically called during the copy.
:type Callback: method
:param SourceClient: The client to be used for operation that
            may happen at the source object. For example, this client is
            used for the head_object that determines the size of the copy.
            If no client is provided, the current client is used as the client
            for the source object.
:type SourceClient: botocore or boto3 Client
:param Config: The transfer configuration to be used when performing the
            copy.
:type Config: boto3.s3.transfer.TransferConfig
"""


def copy_object(ACL=None, Bucket=None, CacheControl=None, ContentDisposition=None, ContentEncoding=None,
                ContentLanguage=None, ContentType=None, CopySource=None, CopySourceIfMatch=None,
                CopySourceIfModifiedSince=None, CopySourceIfNoneMatch=None, CopySourceIfUnmodifiedSince=None,
                Expires=None, GrantFullControl=None, GrantRead=None, GrantReadACP=None, GrantWriteACP=None, Key=None,
                Metadata=None, MetadataDirective=None, ServerSideEncryption=None, StorageClass=None,
                WebsiteRedirectLocation=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None,
                SSEKMSKeyId=None, CopySourceSSECustomerAlgorithm=None, CopySourceSSECustomerKey=None,
                CopySourceSSECustomerKeyMD5=None, RequestPayer=None): pass


"""
:param ACL: The canned ACL to apply to the object.
:type ACL: string
:param Bucket: [REQUIRED]
:type Bucket: string
:param CacheControl: Specifies caching behavior along the request/reply chain.
:type CacheControl: string
:param ContentDisposition: Specifies presentational information for the object.
:type ContentDisposition: string
:param ContentEncoding: Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
:type ContentEncoding: string
:param ContentLanguage: The language the content is in.
:type ContentLanguage: string
:param ContentType: A standard MIME type describing the format of the object data.
:type ContentType: string
:param CopySource: [REQUIRED] The name of the source bucket, key name of the source object, and optional version ID of the source object. You can either provide this value as a string or a dictionary. The string form is {bucket}/{key} or {bucket}/{key}?versionId={versionId} if you want to copy a specific version. You can also provide this value as a dictionary. The dictionary format is recommended over the string format because it is more explicit. The dictionary format is: {'Bucket': 'bucket', 'Key': 'key', 'VersionId': 'id'}. Note that the VersionId key is optional and may be omitted.
:type CopySource: str or dict
:param CopySourceIfMatch: Copies the object if its entity tag (ETag) matches the specified tag.
:type CopySourceIfMatch: string
:param CopySourceIfModifiedSince: Copies the object if it has been modified since the specified time.
:type CopySourceIfModifiedSince: datetime
:param CopySourceIfNoneMatch: Copies the object if its entity tag (ETag) is different than the specified ETag.
:type CopySourceIfNoneMatch: string
:param CopySourceIfUnmodifiedSince: Copies the object if it hasn't been modified since the specified time.
:type CopySourceIfUnmodifiedSince: datetime
:param Expires: The date and time at which the object is no longer cacheable.
:type Expires: datetime
:param GrantFullControl: Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
:type GrantFullControl: string
:param GrantRead: Allows grantee to read the object data and its metadata.
:type GrantRead: string
:param GrantReadACP: Allows grantee to read the object ACL.
:type GrantReadACP: string
:param GrantWriteACP: Allows grantee to write the ACL for the applicable object.
:type GrantWriteACP: string
:param Key: [REQUIRED]
:type Key: string
:param Metadata: A map of metadata to store with the object in S3.
            (string) --
            (string) --
            
:type Metadata: dict
:param MetadataDirective: Specifies whether the metadata is copied from the source object or replaced with metadata provided in the request.
:type MetadataDirective: string
:param ServerSideEncryption: The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
:type ServerSideEncryption: string
:param StorageClass: The type of storage to use for the object. Defaults to 'STANDARD'.
:type StorageClass: string
:param WebsiteRedirectLocation: If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
:type WebsiteRedirectLocation: string
:param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (e.g., AES256).
:type SSECustomerAlgorithm: string
:param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side -encryption -customer-algorithm header.
:type SSECustomerKey: string
:param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
:type SSECustomerKeyMD5: string
:param SSEKMSKeyId: Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version
:type SSEKMSKeyId: string
:param CopySourceSSECustomerAlgorithm: Specifies the algorithm to use when decrypting the source object (e.g., AES256).
:type CopySourceSSECustomerAlgorithm: string
:param CopySourceSSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.
:type CopySourceSSECustomerKey: string
:param CopySourceSSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
:type CopySourceSSECustomerKeyMD5: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
"""


def create_bucket(ACL=None, Bucket=None, CreateBucketConfiguration=None, GrantFullControl=None, GrantRead=None,
                  GrantReadACP=None, GrantWrite=None, GrantWriteACP=None): pass


"""
:param ACL: The canned ACL to apply to the bucket.
:type ACL: string
:param Bucket: [REQUIRED]
:type Bucket: string
:param CreateBucketConfiguration: 
            LocationConstraint (string) -- Specifies the region where the bucket will be created. If you don't specify a region, the bucket will be created in US Standard.
            
:type CreateBucketConfiguration: dict
:param GrantFullControl: Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.
:type GrantFullControl: string
:param GrantRead: Allows grantee to list the objects in the bucket.
:type GrantRead: string
:param GrantReadACP: Allows grantee to read the bucket ACL.
:type GrantReadACP: string
:param GrantWrite: Allows grantee to create, overwrite, and delete any object in the bucket.
:type GrantWrite: string
:param GrantWriteACP: Allows grantee to write the ACL for the applicable bucket.
:type GrantWriteACP: string
"""


def create_multipart_upload(ACL=None, Bucket=None, CacheControl=None, ContentDisposition=None, ContentEncoding=None,
                            ContentLanguage=None, ContentType=None, Expires=None, GrantFullControl=None, GrantRead=None,
                            GrantReadACP=None, GrantWriteACP=None, Key=None, Metadata=None, ServerSideEncryption=None,
                            StorageClass=None, WebsiteRedirectLocation=None, SSECustomerAlgorithm=None,
                            SSECustomerKey=None, SSECustomerKeyMD5=None, SSEKMSKeyId=None, RequestPayer=None): pass


"""
:param ACL: The canned ACL to apply to the object.
:type ACL: string
:param Bucket: [REQUIRED]
:type Bucket: string
:param CacheControl: Specifies caching behavior along the request/reply chain.
:type CacheControl: string
:param ContentDisposition: Specifies presentational information for the object.
:type ContentDisposition: string
:param ContentEncoding: Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
:type ContentEncoding: string
:param ContentLanguage: The language the content is in.
:type ContentLanguage: string
:param ContentType: A standard MIME type describing the format of the object data.
:type ContentType: string
:param Expires: The date and time at which the object is no longer cacheable.
:type Expires: datetime
:param GrantFullControl: Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
:type GrantFullControl: string
:param GrantRead: Allows grantee to read the object data and its metadata.
:type GrantRead: string
:param GrantReadACP: Allows grantee to read the object ACL.
:type GrantReadACP: string
:param GrantWriteACP: Allows grantee to write the ACL for the applicable object.
:type GrantWriteACP: string
:param Key: [REQUIRED]
:type Key: string
:param Metadata: A map of metadata to store with the object in S3.
            (string) --
            (string) --
            
:type Metadata: dict
:param ServerSideEncryption: The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
:type ServerSideEncryption: string
:param StorageClass: The type of storage to use for the object. Defaults to 'STANDARD'.
:type StorageClass: string
:param WebsiteRedirectLocation: If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
:type WebsiteRedirectLocation: string
:param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (e.g., AES256).
:type SSECustomerAlgorithm: string
:param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side -encryption -customer-algorithm header.
:type SSECustomerKey: string
:param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
:type SSECustomerKeyMD5: string
:param SSEKMSKeyId: Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version
:type SSEKMSKeyId: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
"""


def delete_bucket(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            ReturnsNone
            
:type Bucket: string
"""


def delete_bucket_cors(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            ReturnsNone
            
:type Bucket: string
"""


def delete_bucket_lifecycle(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            ReturnsNone
            
:type Bucket: string
"""


def delete_bucket_policy(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            ReturnsNone
            
:type Bucket: string
"""


def delete_bucket_replication(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            ReturnsNone
            
:type Bucket: string
"""


def delete_bucket_tagging(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            ReturnsNone
            
:type Bucket: string
"""


def delete_bucket_website(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            ReturnsNone
            
:type Bucket: string
"""


def delete_object(Bucket=None, Key=None, MFA=None, VersionId=None, RequestPayer=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param Key: [REQUIRED]
:type Key: string
:param MFA: The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device.
:type MFA: string
:param VersionId: VersionId used to reference a specific version of the object.
:type VersionId: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
"""


def delete_objects(Bucket=None, Delete=None, MFA=None, RequestPayer=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param Delete: [REQUIRED]
            Objects (list) -- [REQUIRED]
            (dict) --
            Key (string) -- [REQUIRED] Key name of the object to delete.
            VersionId (string) -- VersionId for the specific version of the object to delete.
            
            Quiet (boolean) -- Element to enable quiet mode for the request. When you add this element, you must set its value to true.
            
:type Delete: dict
:param MFA: The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device.
:type MFA: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
"""


def download_file(): pass


"""
"""


def download_fileobj(Fileobj=None, Bucket=None, Key=None, ExtraArgs=None, Callback=None, Config=None): pass


"""
:param Fileobj: A file-like object to download into. At a minimum, it must
            implement the write method and must accept bytes.
:type Fileobj: a file-like object
:param Bucket: The name of the bucket to download from.
:type Bucket: str
:param Key: The name of the key to download from.
:type Key: str
:param ExtraArgs: Extra arguments that may be passed to the
            client operation.
:type ExtraArgs: dict
:param Callback: A method which takes a number of bytes transferred to
            be periodically called during the download.
:type Callback: method
:param Config: The transfer configuration to be used when performing the
            download.
:type Config: boto3.s3.transfer.TransferConfig
"""


def generate_presigned_post(Bucket=None, Key=None, Fields=None, Conditions=None, ExpiresIn=None): pass


"""
:param Bucket: The name of the bucket to presign the post to. Note that
            bucket related conditions should not be included in the
            conditions parameter.
:type Bucket: string
:param Key: Key name, optionally add ${filename} to the end to
            attach the submitted filename. Note that key related conditions and
            fields are filled out for you and should not be included in the
            Fields or Conditions parameter.
:type Key: string
:param Fields: A dictionary of prefilled form fields to build on top
            of. Elements that may be included are acl, Cache-Control,
            Content-Type, Content-Disposition, Content-Encoding, Expires,
            success_action_redirect, redirect, success_action_status,
            and x-amz-meta-.
            Note that if a particular element is included in the fields
            dictionary it will not be automatically added to the conditions
            list. You must specify a condition for the element as well.
            
:type Fields: dict
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
            
:type Conditions: list
:param ExpiresIn: The number of seconds the presigned post
            is valid for.
:type ExpiresIn: int
"""


def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None): pass


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


def get_bucket_accelerate_configuration(Bucket=None): pass


"""
:param Bucket: [REQUIRED] Name of the bucket for which the accelerate configuration is retrieved.
            Return typedict
            ReturnsResponse Syntax{
              'Status': 'Enabled'|'Suspended'
            }
            Response Structure
            (dict) --
            Status (string) -- The accelerate configuration of the bucket.
            
            
:type Bucket: string
"""


def get_bucket_acl(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            Return typedict
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
            
            
            
:type Bucket: string
"""


def get_bucket_cors(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            Return typedict
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
            CORSRules (list) --
            (dict) --
            AllowedHeaders (list) -- Specifies which headers are allowed in a pre-flight OPTIONS request.
            (string) --
            AllowedMethods (list) -- Identifies HTTP methods that the domain/origin specified in the rule is allowed to execute.
            (string) --
            AllowedOrigins (list) -- One or more origins you want customers to be able to access the bucket from.
            (string) --
            ExposeHeaders (list) -- One or more headers in the response that you want customers to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).
            (string) --
            MaxAgeSeconds (integer) -- The time in seconds that your browser is to cache the preflight response for the specified resource.
            
            
            
:type Bucket: string
"""


def get_bucket_lifecycle(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            Return typedict
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
            Response Structure
            (dict) --
            Rules (list) --
            (dict) --
            Expiration (dict) --
            Date (datetime) -- Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.
            Days (integer) -- Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
            ExpiredObjectDeleteMarker (boolean) -- Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.
            ID (string) -- Unique identifier for the rule. The value cannot be longer than 255 characters.
            Prefix (string) -- Prefix identifying one or more objects to which the rule applies.
            Status (string) -- If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not currently being applied.
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
            
            
            
:type Bucket: string
"""


def get_bucket_lifecycle_configuration(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            Return typedict
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
            Response Structure
            (dict) --
            Rules (list) --
            (dict) --
            Expiration (dict) --
            Date (datetime) -- Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.
            Days (integer) -- Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
            ExpiredObjectDeleteMarker (boolean) -- Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.
            ID (string) -- Unique identifier for the rule. The value cannot be longer than 255 characters.
            Prefix (string) -- Prefix identifying one or more objects to which the rule applies.
            Status (string) -- If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not currently being applied.
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
            
            
            
:type Bucket: string
"""


def get_bucket_location(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            Return typedict
            ReturnsResponse Syntax{
              'LocationConstraint': 'EU'|'eu-west-1'|'us-west-1'|'us-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1'|'cn-north-1'|'eu-central-1'
            }
            Response Structure
            (dict) --
            LocationConstraint (string) --
            
            
:type Bucket: string
"""


def get_bucket_logging(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            Return typedict
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
            LoggingEnabled (dict) --
            TargetBucket (string) -- Specifies the bucket where you want Amazon S3 to store server access logs. You can have your logs delivered to any bucket that you own, including the same bucket that is being logged. You can also configure multiple buckets to deliver their logs to the same target bucket. In this case you should choose a different TargetPrefix for each source bucket so that the delivered log files can be distinguished by key.
            TargetGrants (list) --
            (dict) --
            Grantee (dict) --
            DisplayName (string) -- Screen name of the grantee.
            EmailAddress (string) -- Email address of the grantee.
            ID (string) -- The canonical user ID of the grantee.
            Type (string) -- Type of grantee
            URI (string) -- URI of the grantee group.
            Permission (string) -- Logging permissions assigned to the Grantee for the bucket.
            
            TargetPrefix (string) -- This element lets you specify a prefix for the keys that the log files will be stored under.
            
            
:type Bucket: string
"""


def get_bucket_notification(Bucket=None): pass


"""
:param Bucket: [REQUIRED] Name of the bucket to get the notification configuration for.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --
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
            
            
:type Bucket: string
"""


def get_bucket_notification_configuration(Bucket=None): pass


"""
:param Bucket: [REQUIRED] Name of the bucket to get the notification configuration for.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) -- Container for specifying the notification configuration of the bucket. If this element is empty, notifications are turned off on the bucket.
            TopicConfigurations (list) --
            (dict) -- Container for specifying the configuration when you want Amazon S3 to publish events to an Amazon Simple Notification Service (Amazon SNS) topic.
            Id (string) -- Optional unique identifier for configurations in a notification configuration. If you don't provide one, Amazon S3 will assign an ID.
            TopicArn (string) -- Amazon SNS topic ARN to which Amazon S3 will publish a message when it detects events of specified type.
            Events (list) --
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
            QueueArn (string) -- Amazon SQS queue ARN to which Amazon S3 will publish a message when it detects events of specified type.
            Events (list) --
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
            LambdaFunctionArn (string) -- Lambda cloud function ARN that Amazon S3 can invoke when it detects events of the specified type.
            Events (list) --
            (string) -- Bucket event for which to send notifications.
            Filter (dict) -- Container for object key name filtering rules. For information about key name filtering, go to Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide.
            Key (dict) -- Container for object key name prefix and suffix filtering rules.
            FilterRules (list) -- A list of containers for key value pair that defines the criteria for the filter rule.
            (dict) -- Container for key value pair that defines the criteria for the filter rule.
            Name (string) -- Object key name prefix or suffix identifying one or more objects to which the filtering rule applies. Maximum prefix length can be up to 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, go to Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide.
            Value (string) --
            
            
            
            
            
:type Bucket: string
"""


def get_bucket_policy(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            Return typedict
            ReturnsResponse Syntax{
              'Policy': 'string'
            }
            Response Structure
            (dict) --
            Policy (string) -- The bucket policy as a JSON document.
            
            
:type Bucket: string
"""


def get_bucket_replication(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --
            ReplicationConfiguration (dict) -- Container for replication rules. You can add as many as 1,000 rules. Total replication configuration size can be up to 2 MB.
            Role (string) -- Amazon Resource Name (ARN) of an IAM role for Amazon S3 to assume when replicating the objects.
            Rules (list) -- Container for information about a particular replication rule. Replication configuration must have at least one rule and can contain up to 1,000 rules.
            (dict) --
            ID (string) -- Unique identifier for the rule. The value cannot be longer than 255 characters.
            Prefix (string) -- Object keyname prefix identifying one or more objects to which the rule applies. Maximum prefix length can be up to 1,024 characters. Overlapping prefixes are not supported.
            Status (string) -- The rule is ignored if status is not Enabled.
            Destination (dict) --
            Bucket (string) -- Amazon resource name (ARN) of the bucket where you want Amazon S3 to store replicas of the object identified by the rule.
            StorageClass (string) -- The class of storage used to store the object.
            
            
            
            
:type Bucket: string
"""


def get_bucket_request_payment(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            Return typedict
            ReturnsResponse Syntax{
              'Payer': 'Requester'|'BucketOwner'
            }
            Response Structure
            (dict) --
            Payer (string) -- Specifies who pays for the download and request fees.
            
            
:type Bucket: string
"""


def get_bucket_tagging(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            Return typedict
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
            TagSet (list) --
            (dict) --
            Key (string) -- Name of the tag.
            Value (string) -- Value of the tag.
            
            
            
:type Bucket: string
"""


def get_bucket_versioning(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            Return typedict
            ReturnsResponse Syntax{
              'Status': 'Enabled'|'Suspended',
              'MFADelete': 'Enabled'|'Disabled'
            }
            Response Structure
            (dict) --
            Status (string) -- The versioning state of the bucket.
            MFADelete (string) -- Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned.
            
            
:type Bucket: string
"""


def get_bucket_website(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            Return typedict
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
            RedirectAllRequestsTo (dict) --
            HostName (string) -- Name of the host where requests will be redirected.
            Protocol (string) -- Protocol to use (http, https) when redirecting requests. The default is the protocol that is used in the original request.
            IndexDocument (dict) --
            Suffix (string) -- A suffix that is appended to a request that is for a directory on the website endpoint (e.g. if the suffix is index.html and you make a request to samplebucket/images/ the data that is returned will be for the object with the key name images/index.html) The suffix must not be empty and must not include a slash character.
            ErrorDocument (dict) --
            Key (string) -- The object key name to use when a 4XX class error occurs.
            RoutingRules (list) --
            (dict) --
            Condition (dict) -- A container for describing a condition that must be met for the specified redirect to apply. For example, 1. If request is for pages in the /docs folder, redirect to the /documents folder. 2. If request results in HTTP error 4xx, redirect request to another host where you might process the error.
            HttpErrorCodeReturnedEquals (string) -- The HTTP error code when the redirect is applied. In the event of an error, if the error code equals this value, then the specified redirect is applied. Required when parent element Condition is specified and sibling KeyPrefixEquals is not specified. If both are specified, then both must be true for the redirect to be applied.
            KeyPrefixEquals (string) -- The object key name prefix when the redirect is applied. For example, to redirect requests for ExamplePage.html, the key prefix will be ExamplePage.html. To redirect request for all pages with the prefix docs/, the key prefix will be /docs, which identifies all objects in the docs/ folder. Required when the parent element Condition is specified and sibling HttpErrorCodeReturnedEquals is not specified. If both conditions are specified, both must be true for the redirect to be applied.
            Redirect (dict) -- Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can can specify a different error code to return.
            HostName (string) -- The host name to use in the redirect request.
            HttpRedirectCode (string) -- The HTTP redirect code to use on the response. Not required if one of the siblings is present.
            Protocol (string) -- Protocol to use (http, https) when redirecting requests. The default is the protocol that is used in the original request.
            ReplaceKeyPrefixWith (string) -- The object key prefix to use in the redirect request. For example, to redirect requests for all pages with prefix docs/ (objects in the docs/ folder) to documents/, you can set a condition block with KeyPrefixEquals set to docs/ and in the Redirect set ReplaceKeyPrefixWith to /documents. Not required if one of the siblings is present. Can be present only if ReplaceKeyWith is not provided.
            ReplaceKeyWith (string) -- The specific object key to use in the redirect request. For example, redirect request to error.html. Not required if one of the sibling is present. Can be present only if ReplaceKeyPrefixWith is not provided.
            
            
            
:type Bucket: string
"""


def get_object(Bucket=None, IfMatch=None, IfModifiedSince=None, IfNoneMatch=None, IfUnmodifiedSince=None, Key=None,
               Range=None, ResponseCacheControl=None, ResponseContentDisposition=None, ResponseContentEncoding=None,
               ResponseContentLanguage=None, ResponseContentType=None, ResponseExpires=None, VersionId=None,
               SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, RequestPayer=None,
               PartNumber=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param IfMatch: Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).
:type IfMatch: string
:param IfModifiedSince: Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).
:type IfModifiedSince: datetime
:param IfNoneMatch: Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).
:type IfNoneMatch: string
:param IfUnmodifiedSince: Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).
:type IfUnmodifiedSince: datetime
:param Key: [REQUIRED]
:type Key: string
:param Range: Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
:type Range: string
:param ResponseCacheControl: Sets the Cache-Control header of the response.
:type ResponseCacheControl: string
:param ResponseContentDisposition: Sets the Content-Disposition header of the response
:type ResponseContentDisposition: string
:param ResponseContentEncoding: Sets the Content-Encoding header of the response.
:type ResponseContentEncoding: string
:param ResponseContentLanguage: Sets the Content-Language header of the response.
:type ResponseContentLanguage: string
:param ResponseContentType: Sets the Content-Type header of the response.
:type ResponseContentType: string
:param ResponseExpires: Sets the Expires header of the response.
:type ResponseExpires: datetime
:param VersionId: VersionId used to reference a specific version of the object.
:type VersionId: string
:param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (e.g., AES256).
:type SSECustomerAlgorithm: string
:param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side -encryption -customer-algorithm header.
:type SSECustomerKey: string
:param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
:type SSECustomerKeyMD5: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
:param PartNumber: Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a 'ranged' GET request for the part specified. Useful for downloading just a part of an object.
:type PartNumber: integer
"""


def get_object_acl(Bucket=None, Key=None, VersionId=None, RequestPayer=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param Key: [REQUIRED]
:type Key: string
:param VersionId: VersionId used to reference a specific version of the object.
:type VersionId: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
"""


def get_object_torrent(Bucket=None, Key=None, RequestPayer=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param Key: [REQUIRED]
:type Key: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
"""


def get_paginator(operation_name=None): pass


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


def get_waiter(): pass


"""
"""


def head_bucket(Bucket=None): pass


"""
:param Bucket: [REQUIRED]
            ReturnsNone
            
:type Bucket: string
"""


def head_object(Bucket=None, IfMatch=None, IfModifiedSince=None, IfNoneMatch=None, IfUnmodifiedSince=None, Key=None,
                Range=None, VersionId=None, SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None,
                RequestPayer=None, PartNumber=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param IfMatch: Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).
:type IfMatch: string
:param IfModifiedSince: Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).
:type IfModifiedSince: datetime
:param IfNoneMatch: Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).
:type IfNoneMatch: string
:param IfUnmodifiedSince: Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).
:type IfUnmodifiedSince: datetime
:param Key: [REQUIRED]
:type Key: string
:param Range: Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
:type Range: string
:param VersionId: VersionId used to reference a specific version of the object.
:type VersionId: string
:param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (e.g., AES256).
:type SSECustomerAlgorithm: string
:param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side -encryption -customer-algorithm header.
:type SSECustomerKey: string
:param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
:type SSECustomerKeyMD5: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
:param PartNumber: Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a 'ranged' HEAD request for the part specified. Useful querying about the size of the part and the number of parts in this object.
:type PartNumber: integer
"""


def list_buckets(): pass


"""
"""


def list_multipart_uploads(Bucket=None, Delimiter=None, EncodingType=None, KeyMarker=None, MaxUploads=None, Prefix=None,
                           UploadIdMarker=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param Delimiter: Character you use to group keys.
:type Delimiter: string
:param EncodingType: Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.
:type EncodingType: string
:param KeyMarker: Together with upload-id-marker, this parameter specifies the multipart upload after which listing should begin.
:type KeyMarker: string
:param MaxUploads: Sets the maximum number of multipart uploads, from 1 to 1,000, to return in the response body. 1,000 is the maximum number of uploads that can be returned in a response.
:type MaxUploads: integer
:param Prefix: Lists in-progress uploads only for those keys that begin with the specified prefix.
:type Prefix: string
:param UploadIdMarker: Together with key-marker, specifies the multipart upload after which listing should begin. If key-marker is not specified, the upload-id-marker parameter is ignored.
:type UploadIdMarker: string
"""


def list_object_versions(Bucket=None, Delimiter=None, EncodingType=None, KeyMarker=None, MaxKeys=None, Prefix=None,
                         VersionIdMarker=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param Delimiter: A delimiter is a character you use to group keys.
:type Delimiter: string
:param EncodingType: Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.
:type EncodingType: string
:param KeyMarker: Specifies the key to start with when listing objects in a bucket.
:type KeyMarker: string
:param MaxKeys: Sets the maximum number of keys returned in the response. The response might contain fewer keys but will never contain more.
:type MaxKeys: integer
:param Prefix: Limits the response to keys that begin with the specified prefix.
:type Prefix: string
:param VersionIdMarker: Specifies the object version you want to start listing from.
:type VersionIdMarker: string
"""


def list_objects(Bucket=None, Delimiter=None, EncodingType=None, Marker=None, MaxKeys=None, Prefix=None,
                 RequestPayer=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param Delimiter: A delimiter is a character you use to group keys.
:type Delimiter: string
:param EncodingType: Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.
:type EncodingType: string
:param Marker: Specifies the key to start with when listing objects in a bucket.
:type Marker: string
:param MaxKeys: Sets the maximum number of keys returned in the response. The response might contain fewer keys but will never contain more.
:type MaxKeys: integer
:param Prefix: Limits the response to keys that begin with the specified prefix.
:type Prefix: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the list objects request. Bucket owners need not specify this parameter in their requests.
:type RequestPayer: string
"""


def list_objects_v2(Bucket=None, Delimiter=None, EncodingType=None, MaxKeys=None, Prefix=None, ContinuationToken=None,
                    FetchOwner=None, StartAfter=None, RequestPayer=None): pass


"""
:param Bucket: [REQUIRED] Name of the bucket to list.
:type Bucket: string
:param Delimiter: A delimiter is a character you use to group keys.
:type Delimiter: string
:param EncodingType: Encoding type used by Amazon S3 to encode object keys in the response.
:type EncodingType: string
:param MaxKeys: Sets the maximum number of keys returned in the response. The response might contain fewer keys but will never contain more.
:type MaxKeys: integer
:param Prefix: Limits the response to keys that begin with the specified prefix.
:type Prefix: string
:param ContinuationToken: ContinuationToken indicates Amazon S3 that the list is being continued on this bucket with a token. ContinuationToken is obfuscated and is not a real key
:type ContinuationToken: string
:param FetchOwner: The owner field is not present in listV2 by default, if you want to return owner field with each key in the result then set the fetch owner field to true
:type FetchOwner: boolean
:param StartAfter: StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified key. StartAfter can be any key in the bucket
:type StartAfter: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the list objects request in V2 style. Bucket owners need not specify this parameter in their requests.
:type RequestPayer: string
"""


def list_parts(Bucket=None, Key=None, MaxParts=None, PartNumberMarker=None, UploadId=None, RequestPayer=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param Key: [REQUIRED]
:type Key: string
:param MaxParts: Sets the maximum number of parts to return.
:type MaxParts: integer
:param PartNumberMarker: Specifies the part after which listing should begin. Only parts with higher part numbers will be listed.
:type PartNumberMarker: integer
:param UploadId: [REQUIRED] Upload ID identifying the multipart upload whose parts are being listed.
:type UploadId: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
"""


def put_bucket_accelerate_configuration(Bucket=None, AccelerateConfiguration=None): pass


"""
:param Bucket: [REQUIRED] Name of the bucket for which the accelerate configuration is set.
:type Bucket: string
:param AccelerateConfiguration: [REQUIRED] Specifies the Accelerate Configuration you want to set for the bucket.
            Status (string) -- The accelerate configuration of the bucket.
            
:type AccelerateConfiguration: dict
"""


def put_bucket_acl(ACL=None, AccessControlPolicy=None, Bucket=None, GrantFullControl=None, GrantRead=None,
                   GrantReadACP=None, GrantWrite=None, GrantWriteACP=None): pass


"""
:param ACL: The canned ACL to apply to the bucket.
:type ACL: string
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
            
:type AccessControlPolicy: dict
:param Bucket: [REQUIRED]
:type Bucket: string
:param GrantFullControl: Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.
:type GrantFullControl: string
:param GrantRead: Allows grantee to list the objects in the bucket.
:type GrantRead: string
:param GrantReadACP: Allows grantee to read the bucket ACL.
:type GrantReadACP: string
:param GrantWrite: Allows grantee to create, overwrite, and delete any object in the bucket.
:type GrantWrite: string
:param GrantWriteACP: Allows grantee to write the ACL for the applicable bucket.
:type GrantWriteACP: string
"""


def put_bucket_cors(Bucket=None, CORSConfiguration=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
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
            
            
:type CORSConfiguration: dict
"""


def put_bucket_lifecycle(Bucket=None, LifecycleConfiguration=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
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
            
            
:type LifecycleConfiguration: dict
"""


def put_bucket_lifecycle_configuration(Bucket=None, LifecycleConfiguration=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
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
            
            
:type LifecycleConfiguration: dict
"""


def put_bucket_logging(Bucket=None, BucketLoggingStatus=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
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
            
:type BucketLoggingStatus: dict
"""


def put_bucket_notification(Bucket=None, NotificationConfiguration=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
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
            
:type NotificationConfiguration: dict
"""


def put_bucket_notification_configuration(Bucket=None, NotificationConfiguration=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
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
            
            
            
            
:type NotificationConfiguration: dict
"""


def put_bucket_policy(Bucket=None, Policy=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param Policy: [REQUIRED] The bucket policy as a JSON document.
:type Policy: string
"""


def put_bucket_replication(Bucket=None, ReplicationConfiguration=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
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
            
            
:type ReplicationConfiguration: dict
"""


def put_bucket_request_payment(Bucket=None, RequestPaymentConfiguration=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param RequestPaymentConfiguration: [REQUIRED]
            Payer (string) -- [REQUIRED] Specifies who pays for the download and request fees.
            
:type RequestPaymentConfiguration: dict
"""


def put_bucket_tagging(Bucket=None, Tagging=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param Tagging: [REQUIRED]
            TagSet (list) -- [REQUIRED]
            (dict) --
            Key (string) -- [REQUIRED] Name of the tag.
            Value (string) -- [REQUIRED] Value of the tag.
            
            
:type Tagging: dict
"""


def put_bucket_versioning(Bucket=None, MFA=None, VersioningConfiguration=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param MFA: The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device.
:type MFA: string
:param VersioningConfiguration: [REQUIRED]
            MFADelete (string) -- Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned.
            Status (string) -- The versioning state of the bucket.
            
:type VersioningConfiguration: dict
"""


def put_bucket_website(Bucket=None, WebsiteConfiguration=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
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
            
            
:type WebsiteConfiguration: dict
"""


def put_object(ACL=None, Body=None, Bucket=None, CacheControl=None, ContentDisposition=None, ContentEncoding=None,
               ContentLanguage=None, ContentLength=None, ContentMD5=None, ContentType=None, Expires=None,
               GrantFullControl=None, GrantRead=None, GrantReadACP=None, GrantWriteACP=None, Key=None, Metadata=None,
               ServerSideEncryption=None, StorageClass=None, WebsiteRedirectLocation=None, SSECustomerAlgorithm=None,
               SSECustomerKey=None, SSECustomerKeyMD5=None, SSEKMSKeyId=None, RequestPayer=None): pass


"""
:param ACL: The canned ACL to apply to the object.
:type ACL: string
:param Body: Object data.
:type Body: bytes or seekable file-like object
:param Bucket: [REQUIRED] Name of the bucket to which the PUT operation was initiated.
:type Bucket: string
:param CacheControl: Specifies caching behavior along the request/reply chain.
:type CacheControl: string
:param ContentDisposition: Specifies presentational information for the object.
:type ContentDisposition: string
:param ContentEncoding: Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
:type ContentEncoding: string
:param ContentLanguage: The language the content is in.
:type ContentLanguage: string
:param ContentLength: Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically.
:type ContentLength: integer
:param ContentMD5: The base64-encoded 128-bit MD5 digest of the part data.
:type ContentMD5: string
:param ContentType: A standard MIME type describing the format of the object data.
:type ContentType: string
:param Expires: The date and time at which the object is no longer cacheable.
:type Expires: datetime
:param GrantFullControl: Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
:type GrantFullControl: string
:param GrantRead: Allows grantee to read the object data and its metadata.
:type GrantRead: string
:param GrantReadACP: Allows grantee to read the object ACL.
:type GrantReadACP: string
:param GrantWriteACP: Allows grantee to write the ACL for the applicable object.
:type GrantWriteACP: string
:param Key: [REQUIRED] Object key for which the PUT operation was initiated.
:type Key: string
:param Metadata: A map of metadata to store with the object in S3.
            (string) --
            (string) --
            
:type Metadata: dict
:param ServerSideEncryption: The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
:type ServerSideEncryption: string
:param StorageClass: The type of storage to use for the object. Defaults to 'STANDARD'.
:type StorageClass: string
:param WebsiteRedirectLocation: If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
:type WebsiteRedirectLocation: string
:param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (e.g., AES256).
:type SSECustomerAlgorithm: string
:param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side -encryption -customer-algorithm header.
:type SSECustomerKey: string
:param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
:type SSECustomerKeyMD5: string
:param SSEKMSKeyId: Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version
:type SSEKMSKeyId: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
"""


def put_object_acl(ACL=None, AccessControlPolicy=None, Bucket=None, GrantFullControl=None, GrantRead=None,
                   GrantReadACP=None, GrantWrite=None, GrantWriteACP=None, Key=None, RequestPayer=None,
                   VersionId=None): pass


"""
:param ACL: The canned ACL to apply to the object.
:type ACL: string
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
            
:type AccessControlPolicy: dict
:param Bucket: [REQUIRED]
:type Bucket: string
:param GrantFullControl: Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.
:type GrantFullControl: string
:param GrantRead: Allows grantee to list the objects in the bucket.
:type GrantRead: string
:param GrantReadACP: Allows grantee to read the bucket ACL.
:type GrantReadACP: string
:param GrantWrite: Allows grantee to create, overwrite, and delete any object in the bucket.
:type GrantWrite: string
:param GrantWriteACP: Allows grantee to write the ACL for the applicable bucket.
:type GrantWriteACP: string
:param Key: [REQUIRED]
:type Key: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
:param VersionId: VersionId used to reference a specific version of the object.
:type VersionId: string
"""


def restore_object(Bucket=None, Key=None, VersionId=None, RestoreRequest=None, RequestPayer=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param Key: [REQUIRED]
:type Key: string
:param VersionId: 
:type VersionId: string
:param RestoreRequest: 
            Days (integer) -- [REQUIRED] Lifetime of the active copy in days
            
:type RestoreRequest: dict
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
"""


def upload_file(): pass


"""
"""


def upload_fileobj(Fileobj=None, Bucket=None, Key=None, ExtraArgs=None, Callback=None, Config=None): pass


"""
:param Fileobj: A file-like object to upload. At a minimum, it must
            implement the read method, and must return bytes.
:type Fileobj: a file-like object
:param Bucket: The name of the bucket to upload to.
:type Bucket: str
:param Key: The name of the key to upload to.
:type Key: str
:param ExtraArgs: Extra arguments that may be passed to the
            client operation.
:type ExtraArgs: dict
:param Callback: A method which takes a number of bytes transferred to
            be periodically called during the upload.
:type Callback: method
:param Config: The transfer configuration to be used when performing the
            upload.
:type Config: boto3.s3.transfer.TransferConfig
"""


def upload_part(Body=None, Bucket=None, ContentLength=None, ContentMD5=None, Key=None, PartNumber=None, UploadId=None,
                SSECustomerAlgorithm=None, SSECustomerKey=None, SSECustomerKeyMD5=None, RequestPayer=None): pass


"""
:param Body: Object data.
:type Body: bytes or seekable file-like object
:param Bucket: [REQUIRED] Name of the bucket to which the multipart upload was initiated.
:type Bucket: string
:param ContentLength: Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically.
:type ContentLength: integer
:param ContentMD5: The base64-encoded 128-bit MD5 digest of the part data.
:type ContentMD5: string
:param Key: [REQUIRED] Object key for which the multipart upload was initiated.
:type Key: string
:param PartNumber: [REQUIRED] Part number of part being uploaded. This is a positive integer between 1 and 10,000.
:type PartNumber: integer
:param UploadId: [REQUIRED] Upload ID identifying the multipart upload whose part is being uploaded.
:type UploadId: string
:param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (e.g., AES256).
:type SSECustomerAlgorithm: string
:param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side -encryption -customer-algorithm header. This must be the same encryption key specified in the initiate multipart upload request.
:type SSECustomerKey: string
:param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
:type SSECustomerKeyMD5: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
"""


def upload_part_copy(Bucket=None, CopySource=None, CopySourceIfMatch=None, CopySourceIfModifiedSince=None,
                     CopySourceIfNoneMatch=None, CopySourceIfUnmodifiedSince=None, CopySourceRange=None, Key=None,
                     PartNumber=None, UploadId=None, SSECustomerAlgorithm=None, SSECustomerKey=None,
                     SSECustomerKeyMD5=None, CopySourceSSECustomerAlgorithm=None, CopySourceSSECustomerKey=None,
                     CopySourceSSECustomerKeyMD5=None, RequestPayer=None): pass


"""
:param Bucket: [REQUIRED]
:type Bucket: string
:param CopySource: [REQUIRED] The name of the source bucket, key name of the source object, and optional version ID of the source object. You can either provide this value as a string or a dictionary. The string form is {bucket}/{key} or {bucket}/{key}?versionId={versionId} if you want to copy a specific version. You can also provide this value as a dictionary. The dictionary format is recommended over the string format because it is more explicit. The dictionary format is: {'Bucket': 'bucket', 'Key': 'key', 'VersionId': 'id'}. Note that the VersionId key is optional and may be omitted.
:type CopySource: str or dict
:param CopySourceIfMatch: Copies the object if its entity tag (ETag) matches the specified tag.
:type CopySourceIfMatch: string
:param CopySourceIfModifiedSince: Copies the object if it has been modified since the specified time.
:type CopySourceIfModifiedSince: datetime
:param CopySourceIfNoneMatch: Copies the object if its entity tag (ETag) is different than the specified ETag.
:type CopySourceIfNoneMatch: string
:param CopySourceIfUnmodifiedSince: Copies the object if it hasn't been modified since the specified time.
:type CopySourceIfUnmodifiedSince: datetime
:param CopySourceRange: The range of bytes to copy from the source object. The range value must use the form bytes=first-last, where the first and last are the zero-based byte offsets to copy. For example, bytes=0-9 indicates that you want to copy the first ten bytes of the source. You can copy a range only if the source object is greater than 5 GB.
:type CopySourceRange: string
:param Key: [REQUIRED]
:type Key: string
:param PartNumber: [REQUIRED] Part number of part being copied. This is a positive integer between 1 and 10,000.
:type PartNumber: integer
:param UploadId: [REQUIRED] Upload ID identifying the multipart upload whose part is being copied.
:type UploadId: string
:param SSECustomerAlgorithm: Specifies the algorithm to use to when encrypting the object (e.g., AES256).
:type SSECustomerAlgorithm: string
:param SSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side -encryption -customer-algorithm header. This must be the same encryption key specified in the initiate multipart upload request.
:type SSECustomerKey: string
:param SSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
:type SSECustomerKeyMD5: string
:param CopySourceSSECustomerAlgorithm: Specifies the algorithm to use when decrypting the source object (e.g., AES256).
:type CopySourceSSECustomerAlgorithm: string
:param CopySourceSSECustomerKey: Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.
:type CopySourceSSECustomerKey: string
:param CopySourceSSECustomerKeyMD5: Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.   Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
:type CopySourceSSECustomerKeyMD5: string
:param RequestPayer: Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
:type RequestPayer: string
"""
