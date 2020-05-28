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

def create_access_point(AccountId=None, Name=None, Bucket=None, VpcConfiguration=None, PublicAccessBlockConfiguration=None):
    """
    Creates an access point and associates it with the specified bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.create_access_point(
        AccountId='string',
        Name='string',
        Bucket='string',
        VpcConfiguration={
            'VpcId': 'string'
        },
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True|False,
            'IgnorePublicAcls': True|False,
            'BlockPublicPolicy': True|False,
            'RestrictPublicBuckets': True|False
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe AWS account ID for the owner of the bucket for which you want to create an access point.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name you want to assign to this access point.\n

    :type Bucket: string
    :param Bucket: [REQUIRED]\nThe name of the bucket that you want to associate this access point with.\n

    :type VpcConfiguration: dict
    :param VpcConfiguration: If you include this field, Amazon S3 restricts access to this access point to requests from the specified virtual private cloud (VPC).\n\nVpcId (string) -- [REQUIRED]If this field is specified, this access point will only allow connections from the specified VPC ID.\n\n\n

    :type PublicAccessBlockConfiguration: dict
    :param PublicAccessBlockConfiguration: The PublicAccessBlock configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see The Meaning of 'Public' in the Amazon Simple Storage Service Developer Guide.\n\nBlockPublicAcls (boolean) --Specifies whether Amazon S3 should block public access control lists (ACLs) for buckets in this account. Setting this element to TRUE causes the following behavior:\n\nPUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.\nPUT Object calls fail if the request includes a public ACL.\nPUT Bucket calls fail if the request includes a public ACL.\n\nEnabling this setting doesn\'t affect existing policies or ACLs.\n\nIgnorePublicAcls (boolean) --Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting this element to TRUE causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain.\nEnabling this setting doesn\'t affect the persistence of any existing ACLs and doesn\'t prevent new public ACLs from being set.\n\nBlockPublicPolicy (boolean) --Specifies whether Amazon S3 should block public bucket policies for buckets in this account. Setting this element to TRUE causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.\nEnabling this setting doesn\'t affect existing bucket policies.\n\nRestrictPublicBuckets (boolean) --Specifies whether Amazon S3 should restrict public bucket policies for buckets in this account. Setting this element to TRUE restricts access to buckets with public policies to only AWS services and authorized users within this account.\nEnabling this setting doesn\'t affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.\n\n\n

    """
    pass

def create_job(AccountId=None, ConfirmationRequired=None, Operation=None, Report=None, ClientRequestToken=None, Manifest=None, Description=None, Priority=None, RoleArn=None, Tags=None):
    """
    You can use Amazon S3 Batch Operations to perform large-scale Batch Operations on Amazon S3 objects. Amazon S3 Batch Operations can execute a single operation or action on lists of Amazon S3 objects that you specify. For more information, see Amazon S3 Batch Operations in the Amazon Simple Storage Service Developer Guide.
    Related actions include:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_job(
        AccountId='string',
        ConfirmationRequired=True|False,
        Operation={
            'LambdaInvoke': {
                'FunctionArn': 'string'
            },
            'S3PutObjectCopy': {
                'TargetResource': 'string',
                'CannedAccessControlList': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control',
                'AccessControlGrants': [
                    {
                        'Grantee': {
                            'TypeIdentifier': 'id'|'emailAddress'|'uri',
                            'Identifier': 'string',
                            'DisplayName': 'string'
                        },
                        'Permission': 'FULL_CONTROL'|'READ'|'WRITE'|'READ_ACP'|'WRITE_ACP'
                    },
                ],
                'MetadataDirective': 'COPY'|'REPLACE',
                'ModifiedSinceConstraint': datetime(2015, 1, 1),
                'NewObjectMetadata': {
                    'CacheControl': 'string',
                    'ContentDisposition': 'string',
                    'ContentEncoding': 'string',
                    'ContentLanguage': 'string',
                    'UserMetadata': {
                        'string': 'string'
                    },
                    'ContentLength': 123,
                    'ContentMD5': 'string',
                    'ContentType': 'string',
                    'HttpExpiresDate': datetime(2015, 1, 1),
                    'RequesterCharged': True|False,
                    'SSEAlgorithm': 'AES256'|'KMS'
                },
                'NewObjectTagging': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'RedirectLocation': 'string',
                'RequesterPays': True|False,
                'StorageClass': 'STANDARD'|'STANDARD_IA'|'ONEZONE_IA'|'GLACIER'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
                'UnModifiedSinceConstraint': datetime(2015, 1, 1),
                'SSEAwsKmsKeyId': 'string',
                'TargetKeyPrefix': 'string',
                'ObjectLockLegalHoldStatus': 'OFF'|'ON',
                'ObjectLockMode': 'COMPLIANCE'|'GOVERNANCE',
                'ObjectLockRetainUntilDate': datetime(2015, 1, 1)
            },
            'S3PutObjectAcl': {
                'AccessControlPolicy': {
                    'AccessControlList': {
                        'Owner': {
                            'ID': 'string',
                            'DisplayName': 'string'
                        },
                        'Grants': [
                            {
                                'Grantee': {
                                    'TypeIdentifier': 'id'|'emailAddress'|'uri',
                                    'Identifier': 'string',
                                    'DisplayName': 'string'
                                },
                                'Permission': 'FULL_CONTROL'|'READ'|'WRITE'|'READ_ACP'|'WRITE_ACP'
                            },
                        ]
                    },
                    'CannedAccessControlList': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'
                }
            },
            'S3PutObjectTagging': {
                'TagSet': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
            'S3InitiateRestoreObject': {
                'ExpirationInDays': 123,
                'GlacierJobTier': 'BULK'|'STANDARD'
            },
            'S3PutObjectLegalHold': {
                'LegalHold': {
                    'Status': 'OFF'|'ON'
                }
            },
            'S3PutObjectRetention': {
                'BypassGovernanceRetention': True|False,
                'Retention': {
                    'RetainUntilDate': datetime(2015, 1, 1),
                    'Mode': 'COMPLIANCE'|'GOVERNANCE'
                }
            }
        },
        Report={
            'Bucket': 'string',
            'Format': 'Report_CSV_20180820',
            'Enabled': True|False,
            'Prefix': 'string',
            'ReportScope': 'AllTasks'|'FailedTasksOnly'
        },
        ClientRequestToken='string',
        Manifest={
            'Spec': {
                'Format': 'S3BatchOperations_CSV_20180820'|'S3InventoryReport_CSV_20161130',
                'Fields': [
                    'Ignore'|'Bucket'|'Key'|'VersionId',
                ]
            },
            'Location': {
                'ObjectArn': 'string',
                'ObjectVersionId': 'string',
                'ETag': 'string'
            }
        },
        Description='string',
        Priority=123,
        RoleArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]

    :type ConfirmationRequired: boolean
    :param ConfirmationRequired: Indicates whether confirmation is required before Amazon S3 runs the job. Confirmation is only required for jobs created through the Amazon S3 console.

    :type Operation: dict
    :param Operation: [REQUIRED]\nThe operation that you want this job to perform on each object listed in the manifest. For more information about the available operations, see Available Operations in the Amazon Simple Storage Service Developer Guide .\n\nLambdaInvoke (dict) --Directs the specified job to invoke an AWS Lambda function on each object in the manifest.\n\nFunctionArn (string) --The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will invoke for each object in the manifest.\n\n\n\nS3PutObjectCopy (dict) --Directs the specified job to execute a PUT Copy object call on each object in the manifest.\n\nTargetResource (string) --\nCannedAccessControlList (string) --\nAccessControlGrants (list) --\n(dict) --\nGrantee (dict) --\nTypeIdentifier (string) --\nIdentifier (string) --\nDisplayName (string) --\n\n\nPermission (string) --\n\n\n\n\nMetadataDirective (string) --\nModifiedSinceConstraint (datetime) --\nNewObjectMetadata (dict) --\nCacheControl (string) --\nContentDisposition (string) --\nContentEncoding (string) --\nContentLanguage (string) --\nUserMetadata (dict) --\n(string) --\n(string) --\n\n\n\n\nContentLength (integer) --\nContentMD5 (string) --\nContentType (string) --\nHttpExpiresDate (datetime) --\nRequesterCharged (boolean) --\nSSEAlgorithm (string) --\n\n\nNewObjectTagging (list) --\n(dict) --\nKey (string) -- [REQUIRED]\nValue (string) -- [REQUIRED]\n\n\n\n\nRedirectLocation (string) --\nRequesterPays (boolean) --\nStorageClass (string) --\nUnModifiedSinceConstraint (datetime) --\nSSEAwsKmsKeyId (string) --\nTargetKeyPrefix (string) --\nObjectLockLegalHoldStatus (string) --The Legal Hold status to be applied to all objects in the Batch Operations job.\n\nObjectLockMode (string) --The Retention mode to be applied to all objects in the Batch Operations job.\n\nObjectLockRetainUntilDate (datetime) --The date when the applied Object Retention configuration will expire on all objects in the Batch Operations job.\n\n\n\nS3PutObjectAcl (dict) --Directs the specified job to execute a PUT Object acl call on each object in the manifest.\n\nAccessControlPolicy (dict) --\nAccessControlList (dict) --\nOwner (dict) -- [REQUIRED]\nID (string) --\nDisplayName (string) --\n\n\nGrants (list) --\n(dict) --\nGrantee (dict) --\nTypeIdentifier (string) --\nIdentifier (string) --\nDisplayName (string) --\n\n\nPermission (string) --\n\n\n\n\n\n\nCannedAccessControlList (string) --\n\n\n\n\nS3PutObjectTagging (dict) --Directs the specified job to execute a PUT Object tagging call on each object in the manifest.\n\nTagSet (list) --\n(dict) --\nKey (string) -- [REQUIRED]\nValue (string) -- [REQUIRED]\n\n\n\n\n\n\nS3InitiateRestoreObject (dict) --Directs the specified job to execute an Initiate Glacier Restore call on each object in the manifest.\n\nExpirationInDays (integer) --\nGlacierJobTier (string) --\n\n\nS3PutObjectLegalHold (dict) --Contains the configuration parameters for a Set Object Legal Hold operation. Amazon S3 Batch Operations passes each value through to the underlying PUT Object Legal Hold API. For more information about the parameters for this operation, see PUT Object Legal Hold .\n\nLegalHold (dict) -- [REQUIRED]The Legal Hold contains the status to be applied to all objects in the Batch Operations job.\n\nStatus (string) -- [REQUIRED]The Legal Hold status to be applied to all objects in the Batch Operations job.\n\n\n\n\n\nS3PutObjectRetention (dict) --Contains the configuration parameters for a Set Object Retention operation. Amazon S3 Batch Operations passes each value through to the underlying PUT Object Retention API. For more information about the parameters for this operation, see PUT Object Retention .\n\nBypassGovernanceRetention (boolean) --Indicates if the operation should be applied to objects in the Batch Operations job even if they have Governance-type Object Lock in place.\n\nRetention (dict) -- [REQUIRED]Amazon S3 object lock Retention contains the retention mode to be applied to all objects in the Batch Operations job.\n\nRetainUntilDate (datetime) --The date when the applied Object Retention will expire on all objects in the Batch Operations job.\n\nMode (string) --The Retention mode to be applied to all objects in the Batch Operations job.\n\n\n\n\n\n\n

    :type Report: dict
    :param Report: [REQUIRED]\nConfiguration parameters for the optional job-completion report.\n\nBucket (string) --The Amazon Resource Name (ARN) for the bucket where specified job-completion report will be stored.\n\nFormat (string) --The format of the specified job-completion report.\n\nEnabled (boolean) -- [REQUIRED]Indicates whether the specified job will generate a job-completion report.\n\nPrefix (string) --An optional prefix to describe where in the specified bucket the job-completion report will be stored. Amazon S3 will store the job-completion report at <prefix>/job-<job-id>/report.json.\n\nReportScope (string) --Indicates whether the job-completion report will include details of all tasks or only failed tasks.\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: [REQUIRED]\nAn idempotency token to ensure that you don\'t accidentally submit the same request twice. You can use any string up to the maximum length.\nThis field is autopopulated if not provided.\n

    :type Manifest: dict
    :param Manifest: [REQUIRED]\nConfiguration parameters for the manifest.\n\nSpec (dict) -- [REQUIRED]Describes the format of the specified job\'s manifest. If the manifest is in CSV format, also describes the columns contained within the manifest.\n\nFormat (string) -- [REQUIRED]Indicates which of the available formats the specified manifest uses.\n\nFields (list) --If the specified manifest object is in the S3BatchOperations_CSV_20180820 format, this element describes which columns contain the required data.\n\n(string) --\n\n\n\n\nLocation (dict) -- [REQUIRED]Contains the information required to locate the specified job\'s manifest.\n\nObjectArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) for a manifest object.\n\nObjectVersionId (string) --The optional version ID to identify a specific version of the manifest object.\n\nETag (string) -- [REQUIRED]The ETag for the specified manifest object.\n\n\n\n\n

    :type Description: string
    :param Description: A description for this job. You can use any string within the permitted length. Descriptions don\'t need to be unique and can be used for multiple jobs.

    :type Priority: integer
    :param Priority: [REQUIRED]\nThe numerical priority for this job. Higher numbers indicate higher priority.\n

    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the AWS Identity and Access Management (IAM) role that Batch Operations will use to execute this job\'s operation on each object in the manifest.\n

    :type Tags: list
    :param Tags: A set of tags to associate with the Amazon S3 Batch Operations job. This is an optional parameter.\n\n(dict) --\nKey (string) -- [REQUIRED]\nValue (string) -- [REQUIRED]\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The ID for this job. Amazon S3 generates this ID automatically and returns it after a successful Create Job request.







Exceptions

S3Control.Client.exceptions.TooManyRequestsException
S3Control.Client.exceptions.BadRequestException
S3Control.Client.exceptions.IdempotencyException
S3Control.Client.exceptions.InternalServiceException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    AccountId (string) -- [REQUIRED]
    ConfirmationRequired (boolean) -- Indicates whether confirmation is required before Amazon S3 runs the job. Confirmation is only required for jobs created through the Amazon S3 console.
    Operation (dict) -- [REQUIRED]
    The operation that you want this job to perform on each object listed in the manifest. For more information about the available operations, see Available Operations in the Amazon Simple Storage Service Developer Guide .
    
    LambdaInvoke (dict) --Directs the specified job to invoke an AWS Lambda function on each object in the manifest.
    
    FunctionArn (string) --The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will invoke for each object in the manifest.
    
    
    
    S3PutObjectCopy (dict) --Directs the specified job to execute a PUT Copy object call on each object in the manifest.
    
    TargetResource (string) --
    CannedAccessControlList (string) --
    AccessControlGrants (list) --
    (dict) --
    Grantee (dict) --
    TypeIdentifier (string) --
    Identifier (string) --
    DisplayName (string) --
    
    
    Permission (string) --
    
    
    
    
    MetadataDirective (string) --
    ModifiedSinceConstraint (datetime) --
    NewObjectMetadata (dict) --
    CacheControl (string) --
    ContentDisposition (string) --
    ContentEncoding (string) --
    ContentLanguage (string) --
    UserMetadata (dict) --
    (string) --
    (string) --
    
    
    
    
    ContentLength (integer) --
    ContentMD5 (string) --
    ContentType (string) --
    HttpExpiresDate (datetime) --
    RequesterCharged (boolean) --
    SSEAlgorithm (string) --
    
    
    NewObjectTagging (list) --
    (dict) --
    Key (string) -- [REQUIRED]
    Value (string) -- [REQUIRED]
    
    
    
    
    RedirectLocation (string) --
    RequesterPays (boolean) --
    StorageClass (string) --
    UnModifiedSinceConstraint (datetime) --
    SSEAwsKmsKeyId (string) --
    TargetKeyPrefix (string) --
    ObjectLockLegalHoldStatus (string) --The Legal Hold status to be applied to all objects in the Batch Operations job.
    
    ObjectLockMode (string) --The Retention mode to be applied to all objects in the Batch Operations job.
    
    ObjectLockRetainUntilDate (datetime) --The date when the applied Object Retention configuration will expire on all objects in the Batch Operations job.
    
    
    
    S3PutObjectAcl (dict) --Directs the specified job to execute a PUT Object acl call on each object in the manifest.
    
    AccessControlPolicy (dict) --
    AccessControlList (dict) --
    Owner (dict) -- [REQUIRED]
    ID (string) --
    DisplayName (string) --
    
    
    Grants (list) --
    (dict) --
    Grantee (dict) --
    TypeIdentifier (string) --
    Identifier (string) --
    DisplayName (string) --
    
    
    Permission (string) --
    
    
    
    
    
    
    CannedAccessControlList (string) --
    
    
    
    
    S3PutObjectTagging (dict) --Directs the specified job to execute a PUT Object tagging call on each object in the manifest.
    
    TagSet (list) --
    (dict) --
    Key (string) -- [REQUIRED]
    Value (string) -- [REQUIRED]
    
    
    
    
    
    
    S3InitiateRestoreObject (dict) --Directs the specified job to execute an Initiate Glacier Restore call on each object in the manifest.
    
    ExpirationInDays (integer) --
    GlacierJobTier (string) --
    
    
    S3PutObjectLegalHold (dict) --Contains the configuration parameters for a Set Object Legal Hold operation. Amazon S3 Batch Operations passes each value through to the underlying PUT Object Legal Hold API. For more information about the parameters for this operation, see PUT Object Legal Hold .
    
    LegalHold (dict) -- [REQUIRED]The Legal Hold contains the status to be applied to all objects in the Batch Operations job.
    
    Status (string) -- [REQUIRED]The Legal Hold status to be applied to all objects in the Batch Operations job.
    
    
    
    
    
    S3PutObjectRetention (dict) --Contains the configuration parameters for a Set Object Retention operation. Amazon S3 Batch Operations passes each value through to the underlying PUT Object Retention API. For more information about the parameters for this operation, see PUT Object Retention .
    
    BypassGovernanceRetention (boolean) --Indicates if the operation should be applied to objects in the Batch Operations job even if they have Governance-type Object Lock in place.
    
    Retention (dict) -- [REQUIRED]Amazon S3 object lock Retention contains the retention mode to be applied to all objects in the Batch Operations job.
    
    RetainUntilDate (datetime) --The date when the applied Object Retention will expire on all objects in the Batch Operations job.
    
    Mode (string) --The Retention mode to be applied to all objects in the Batch Operations job.
    
    
    
    
    
    
    
    Report (dict) -- [REQUIRED]
    Configuration parameters for the optional job-completion report.
    
    Bucket (string) --The Amazon Resource Name (ARN) for the bucket where specified job-completion report will be stored.
    
    Format (string) --The format of the specified job-completion report.
    
    Enabled (boolean) -- [REQUIRED]Indicates whether the specified job will generate a job-completion report.
    
    Prefix (string) --An optional prefix to describe where in the specified bucket the job-completion report will be stored. Amazon S3 will store the job-completion report at <prefix>/job-<job-id>/report.json.
    
    ReportScope (string) --Indicates whether the job-completion report will include details of all tasks or only failed tasks.
    
    
    
    ClientRequestToken (string) -- [REQUIRED]
    An idempotency token to ensure that you don\'t accidentally submit the same request twice. You can use any string up to the maximum length.
    This field is autopopulated if not provided.
    
    Manifest (dict) -- [REQUIRED]
    Configuration parameters for the manifest.
    
    Spec (dict) -- [REQUIRED]Describes the format of the specified job\'s manifest. If the manifest is in CSV format, also describes the columns contained within the manifest.
    
    Format (string) -- [REQUIRED]Indicates which of the available formats the specified manifest uses.
    
    Fields (list) --If the specified manifest object is in the S3BatchOperations_CSV_20180820 format, this element describes which columns contain the required data.
    
    (string) --
    
    
    
    
    Location (dict) -- [REQUIRED]Contains the information required to locate the specified job\'s manifest.
    
    ObjectArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) for a manifest object.
    
    ObjectVersionId (string) --The optional version ID to identify a specific version of the manifest object.
    
    ETag (string) -- [REQUIRED]The ETag for the specified manifest object.
    
    
    
    
    
    Description (string) -- A description for this job. You can use any string within the permitted length. Descriptions don\'t need to be unique and can be used for multiple jobs.
    Priority (integer) -- [REQUIRED]
    The numerical priority for this job. Higher numbers indicate higher priority.
    
    RoleArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) for the AWS Identity and Access Management (IAM) role that Batch Operations will use to execute this job\'s operation on each object in the manifest.
    
    Tags (list) -- A set of tags to associate with the Amazon S3 Batch Operations job. This is an optional parameter.
    
    (dict) --
    Key (string) -- [REQUIRED]
    Value (string) -- [REQUIRED]
    
    
    
    
    
    """
    pass

def delete_access_point(AccountId=None, Name=None):
    """
    Deletes the specified access point.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_access_point(
        AccountId='string',
        Name='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe account ID for the account that owns the specified access point.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the access point you want to delete.\n

    """
    pass

def delete_access_point_policy(AccountId=None, Name=None):
    """
    Deletes the access point policy for the specified access point.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_access_point_policy(
        AccountId='string',
        Name='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe account ID for the account that owns the specified access point.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the access point whose policy you want to delete.\n

    """
    pass

def delete_job_tagging(AccountId=None, JobId=None):
    """
    Removes the entire tag set from the specified Amazon S3 Batch Operations job. To use this operation, you must have permission to perform the s3:DeleteJobTagging action. For more information, see Using Job Tags in the Amazon Simple Storage Service Developer Guide.
    Related actions include:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_job_tagging(
        AccountId='string',
        JobId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe AWS account ID associated with the Amazon S3 Batch Operations job.\n

    :type JobId: string
    :param JobId: [REQUIRED]\nThe ID for the Amazon S3 Batch Operations job whose tags you want to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

S3Control.Client.exceptions.InternalServiceException
S3Control.Client.exceptions.TooManyRequestsException
S3Control.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    AccountId (string) -- [REQUIRED]
    The AWS account ID associated with the Amazon S3 Batch Operations job.
    
    JobId (string) -- [REQUIRED]
    The ID for the Amazon S3 Batch Operations job whose tags you want to delete.
    
    
    """
    pass

def delete_public_access_block(AccountId=None):
    """
    Removes the PublicAccessBlock configuration for an Amazon Web Services account.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_public_access_block(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe account ID for the Amazon Web Services account whose PublicAccessBlock configuration you want to remove.\n

    """
    pass

def describe_job(AccountId=None, JobId=None):
    """
    Retrieves the configuration parameters and status for a Batch Operations job. For more information, see Amazon S3 Batch Operations in the Amazon Simple Storage Service Developer Guide.
    Related actions include:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_job(
        AccountId='string',
        JobId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]

    :type JobId: string
    :param JobId: [REQUIRED]\nThe ID for the job whose information you want to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Job': {
        'JobId': 'string',
        'ConfirmationRequired': True|False,
        'Description': 'string',
        'JobArn': 'string',
        'Status': 'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'|'Failed'|'Failing'|'New'|'Paused'|'Pausing'|'Preparing'|'Ready'|'Suspended',
        'Manifest': {
            'Spec': {
                'Format': 'S3BatchOperations_CSV_20180820'|'S3InventoryReport_CSV_20161130',
                'Fields': [
                    'Ignore'|'Bucket'|'Key'|'VersionId',
                ]
            },
            'Location': {
                'ObjectArn': 'string',
                'ObjectVersionId': 'string',
                'ETag': 'string'
            }
        },
        'Operation': {
            'LambdaInvoke': {
                'FunctionArn': 'string'
            },
            'S3PutObjectCopy': {
                'TargetResource': 'string',
                'CannedAccessControlList': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control',
                'AccessControlGrants': [
                    {
                        'Grantee': {
                            'TypeIdentifier': 'id'|'emailAddress'|'uri',
                            'Identifier': 'string',
                            'DisplayName': 'string'
                        },
                        'Permission': 'FULL_CONTROL'|'READ'|'WRITE'|'READ_ACP'|'WRITE_ACP'
                    },
                ],
                'MetadataDirective': 'COPY'|'REPLACE',
                'ModifiedSinceConstraint': datetime(2015, 1, 1),
                'NewObjectMetadata': {
                    'CacheControl': 'string',
                    'ContentDisposition': 'string',
                    'ContentEncoding': 'string',
                    'ContentLanguage': 'string',
                    'UserMetadata': {
                        'string': 'string'
                    },
                    'ContentLength': 123,
                    'ContentMD5': 'string',
                    'ContentType': 'string',
                    'HttpExpiresDate': datetime(2015, 1, 1),
                    'RequesterCharged': True|False,
                    'SSEAlgorithm': 'AES256'|'KMS'
                },
                'NewObjectTagging': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'RedirectLocation': 'string',
                'RequesterPays': True|False,
                'StorageClass': 'STANDARD'|'STANDARD_IA'|'ONEZONE_IA'|'GLACIER'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
                'UnModifiedSinceConstraint': datetime(2015, 1, 1),
                'SSEAwsKmsKeyId': 'string',
                'TargetKeyPrefix': 'string',
                'ObjectLockLegalHoldStatus': 'OFF'|'ON',
                'ObjectLockMode': 'COMPLIANCE'|'GOVERNANCE',
                'ObjectLockRetainUntilDate': datetime(2015, 1, 1)
            },
            'S3PutObjectAcl': {
                'AccessControlPolicy': {
                    'AccessControlList': {
                        'Owner': {
                            'ID': 'string',
                            'DisplayName': 'string'
                        },
                        'Grants': [
                            {
                                'Grantee': {
                                    'TypeIdentifier': 'id'|'emailAddress'|'uri',
                                    'Identifier': 'string',
                                    'DisplayName': 'string'
                                },
                                'Permission': 'FULL_CONTROL'|'READ'|'WRITE'|'READ_ACP'|'WRITE_ACP'
                            },
                        ]
                    },
                    'CannedAccessControlList': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'
                }
            },
            'S3PutObjectTagging': {
                'TagSet': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
            'S3InitiateRestoreObject': {
                'ExpirationInDays': 123,
                'GlacierJobTier': 'BULK'|'STANDARD'
            },
            'S3PutObjectLegalHold': {
                'LegalHold': {
                    'Status': 'OFF'|'ON'
                }
            },
            'S3PutObjectRetention': {
                'BypassGovernanceRetention': True|False,
                'Retention': {
                    'RetainUntilDate': datetime(2015, 1, 1),
                    'Mode': 'COMPLIANCE'|'GOVERNANCE'
                }
            }
        },
        'Priority': 123,
        'ProgressSummary': {
            'TotalNumberOfTasks': 123,
            'NumberOfTasksSucceeded': 123,
            'NumberOfTasksFailed': 123
        },
        'StatusUpdateReason': 'string',
        'FailureReasons': [
            {
                'FailureCode': 'string',
                'FailureReason': 'string'
            },
        ],
        'Report': {
            'Bucket': 'string',
            'Format': 'Report_CSV_20180820',
            'Enabled': True|False,
            'Prefix': 'string',
            'ReportScope': 'AllTasks'|'FailedTasksOnly'
        },
        'CreationTime': datetime(2015, 1, 1),
        'TerminationDate': datetime(2015, 1, 1),
        'RoleArn': 'string',
        'SuspendedDate': datetime(2015, 1, 1),
        'SuspendedCause': 'string'
    }
}


Response Structure

(dict) --

Job (dict) --
Contains the configuration parameters and status for the job specified in the Describe Job request.

JobId (string) --
The ID for the specified job.

ConfirmationRequired (boolean) --
Indicates whether confirmation is required before Amazon S3 begins running the specified job. Confirmation is required only for jobs created through the Amazon S3 console.

Description (string) --
The description for this job, if one was provided in this job\'s Create Job request.

JobArn (string) --
The Amazon Resource Name (ARN) for this job.

Status (string) --
The current status of the specified job.

Manifest (dict) --
The configuration information for the specified job\'s manifest object.

Spec (dict) --
Describes the format of the specified job\'s manifest. If the manifest is in CSV format, also describes the columns contained within the manifest.

Format (string) --
Indicates which of the available formats the specified manifest uses.

Fields (list) --
If the specified manifest object is in the S3BatchOperations_CSV_20180820 format, this element describes which columns contain the required data.

(string) --




Location (dict) --
Contains the information required to locate the specified job\'s manifest.

ObjectArn (string) --
The Amazon Resource Name (ARN) for a manifest object.

ObjectVersionId (string) --
The optional version ID to identify a specific version of the manifest object.

ETag (string) --
The ETag for the specified manifest object.





Operation (dict) --
The operation that the specified job is configured to execute on the objects listed in the manifest.

LambdaInvoke (dict) --
Directs the specified job to invoke an AWS Lambda function on each object in the manifest.

FunctionArn (string) --
The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will invoke for each object in the manifest.



S3PutObjectCopy (dict) --
Directs the specified job to execute a PUT Copy object call on each object in the manifest.

TargetResource (string) --

CannedAccessControlList (string) --

AccessControlGrants (list) --

(dict) --
Grantee (dict) --
TypeIdentifier (string) --
Identifier (string) --
DisplayName (string) --


Permission (string) --




MetadataDirective (string) --

ModifiedSinceConstraint (datetime) --

NewObjectMetadata (dict) --

CacheControl (string) --
ContentDisposition (string) --
ContentEncoding (string) --
ContentLanguage (string) --
UserMetadata (dict) --
(string) --
(string) --




ContentLength (integer) --
ContentMD5 (string) --
ContentType (string) --
HttpExpiresDate (datetime) --
RequesterCharged (boolean) --
SSEAlgorithm (string) --


NewObjectTagging (list) --

(dict) --
Key (string) --
Value (string) --




RedirectLocation (string) --

RequesterPays (boolean) --

StorageClass (string) --

UnModifiedSinceConstraint (datetime) --

SSEAwsKmsKeyId (string) --

TargetKeyPrefix (string) --

ObjectLockLegalHoldStatus (string) --
The Legal Hold status to be applied to all objects in the Batch Operations job.

ObjectLockMode (string) --
The Retention mode to be applied to all objects in the Batch Operations job.

ObjectLockRetainUntilDate (datetime) --
The date when the applied Object Retention configuration will expire on all objects in the Batch Operations job.



S3PutObjectAcl (dict) --
Directs the specified job to execute a PUT Object acl call on each object in the manifest.

AccessControlPolicy (dict) --
AccessControlList (dict) --
Owner (dict) --
ID (string) --
DisplayName (string) --


Grants (list) --
(dict) --
Grantee (dict) --
TypeIdentifier (string) --
Identifier (string) --
DisplayName (string) --


Permission (string) --






CannedAccessControlList (string) --




S3PutObjectTagging (dict) --
Directs the specified job to execute a PUT Object tagging call on each object in the manifest.

TagSet (list) --
(dict) --
Key (string) --
Value (string) --






S3InitiateRestoreObject (dict) --
Directs the specified job to execute an Initiate Glacier Restore call on each object in the manifest.

ExpirationInDays (integer) --
GlacierJobTier (string) --


S3PutObjectLegalHold (dict) --
Contains the configuration parameters for a Set Object Legal Hold operation. Amazon S3 Batch Operations passes each value through to the underlying PUT Object Legal Hold API. For more information about the parameters for this operation, see PUT Object Legal Hold .

LegalHold (dict) --
The Legal Hold contains the status to be applied to all objects in the Batch Operations job.

Status (string) --
The Legal Hold status to be applied to all objects in the Batch Operations job.





S3PutObjectRetention (dict) --
Contains the configuration parameters for a Set Object Retention operation. Amazon S3 Batch Operations passes each value through to the underlying PUT Object Retention API. For more information about the parameters for this operation, see PUT Object Retention .

BypassGovernanceRetention (boolean) --
Indicates if the operation should be applied to objects in the Batch Operations job even if they have Governance-type Object Lock in place.

Retention (dict) --
Amazon S3 object lock Retention contains the retention mode to be applied to all objects in the Batch Operations job.

RetainUntilDate (datetime) --
The date when the applied Object Retention will expire on all objects in the Batch Operations job.

Mode (string) --
The Retention mode to be applied to all objects in the Batch Operations job.







Priority (integer) --
The priority of the specified job.

ProgressSummary (dict) --
Describes the total number of tasks that the specified job has executed, the number of tasks that succeeded, and the number of tasks that failed.

TotalNumberOfTasks (integer) --
NumberOfTasksSucceeded (integer) --
NumberOfTasksFailed (integer) --


StatusUpdateReason (string) --

FailureReasons (list) --
If the specified job failed, this field contains information describing the failure.

(dict) --
If this job failed, this element indicates why the job failed.

FailureCode (string) --
The failure code, if any, for the specified job.

FailureReason (string) --
The failure reason, if any, for the specified job.





Report (dict) --
Contains the configuration information for the job-completion report if you requested one in the Create Job request.

Bucket (string) --
The Amazon Resource Name (ARN) for the bucket where specified job-completion report will be stored.

Format (string) --
The format of the specified job-completion report.

Enabled (boolean) --
Indicates whether the specified job will generate a job-completion report.

Prefix (string) --
An optional prefix to describe where in the specified bucket the job-completion report will be stored. Amazon S3 will store the job-completion report at <prefix>/job-<job-id>/report.json.

ReportScope (string) --
Indicates whether the job-completion report will include details of all tasks or only failed tasks.



CreationTime (datetime) --
A timestamp indicating when this job was created.

TerminationDate (datetime) --
A timestamp indicating when this job terminated. A job\'s termination date is the date and time when it succeeded, failed, or was canceled.

RoleArn (string) --
The Amazon Resource Name (ARN) for the AWS Identity and Access Management (IAM) role assigned to execute the tasks for this job.

SuspendedDate (datetime) --
The timestamp when this job was suspended, if it has been suspended.

SuspendedCause (string) --
The reason why the specified job was suspended. A job is only suspended if you create it through the Amazon S3 console. When you create the job, it enters the Suspended state to await confirmation before running. After you confirm the job, it automatically exits the Suspended state.









Exceptions

S3Control.Client.exceptions.BadRequestException
S3Control.Client.exceptions.TooManyRequestsException
S3Control.Client.exceptions.NotFoundException
S3Control.Client.exceptions.InternalServiceException


    :return: {
        'Job': {
            'JobId': 'string',
            'ConfirmationRequired': True|False,
            'Description': 'string',
            'JobArn': 'string',
            'Status': 'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'|'Failed'|'Failing'|'New'|'Paused'|'Pausing'|'Preparing'|'Ready'|'Suspended',
            'Manifest': {
                'Spec': {
                    'Format': 'S3BatchOperations_CSV_20180820'|'S3InventoryReport_CSV_20161130',
                    'Fields': [
                        'Ignore'|'Bucket'|'Key'|'VersionId',
                    ]
                },
                'Location': {
                    'ObjectArn': 'string',
                    'ObjectVersionId': 'string',
                    'ETag': 'string'
                }
            },
            'Operation': {
                'LambdaInvoke': {
                    'FunctionArn': 'string'
                },
                'S3PutObjectCopy': {
                    'TargetResource': 'string',
                    'CannedAccessControlList': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control',
                    'AccessControlGrants': [
                        {
                            'Grantee': {
                                'TypeIdentifier': 'id'|'emailAddress'|'uri',
                                'Identifier': 'string',
                                'DisplayName': 'string'
                            },
                            'Permission': 'FULL_CONTROL'|'READ'|'WRITE'|'READ_ACP'|'WRITE_ACP'
                        },
                    ],
                    'MetadataDirective': 'COPY'|'REPLACE',
                    'ModifiedSinceConstraint': datetime(2015, 1, 1),
                    'NewObjectMetadata': {
                        'CacheControl': 'string',
                        'ContentDisposition': 'string',
                        'ContentEncoding': 'string',
                        'ContentLanguage': 'string',
                        'UserMetadata': {
                            'string': 'string'
                        },
                        'ContentLength': 123,
                        'ContentMD5': 'string',
                        'ContentType': 'string',
                        'HttpExpiresDate': datetime(2015, 1, 1),
                        'RequesterCharged': True|False,
                        'SSEAlgorithm': 'AES256'|'KMS'
                    },
                    'NewObjectTagging': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'RedirectLocation': 'string',
                    'RequesterPays': True|False,
                    'StorageClass': 'STANDARD'|'STANDARD_IA'|'ONEZONE_IA'|'GLACIER'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
                    'UnModifiedSinceConstraint': datetime(2015, 1, 1),
                    'SSEAwsKmsKeyId': 'string',
                    'TargetKeyPrefix': 'string',
                    'ObjectLockLegalHoldStatus': 'OFF'|'ON',
                    'ObjectLockMode': 'COMPLIANCE'|'GOVERNANCE',
                    'ObjectLockRetainUntilDate': datetime(2015, 1, 1)
                },
                'S3PutObjectAcl': {
                    'AccessControlPolicy': {
                        'AccessControlList': {
                            'Owner': {
                                'ID': 'string',
                                'DisplayName': 'string'
                            },
                            'Grants': [
                                {
                                    'Grantee': {
                                        'TypeIdentifier': 'id'|'emailAddress'|'uri',
                                        'Identifier': 'string',
                                        'DisplayName': 'string'
                                    },
                                    'Permission': 'FULL_CONTROL'|'READ'|'WRITE'|'READ_ACP'|'WRITE_ACP'
                                },
                            ]
                        },
                        'CannedAccessControlList': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'
                    }
                },
                'S3PutObjectTagging': {
                    'TagSet': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
                'S3InitiateRestoreObject': {
                    'ExpirationInDays': 123,
                    'GlacierJobTier': 'BULK'|'STANDARD'
                },
                'S3PutObjectLegalHold': {
                    'LegalHold': {
                        'Status': 'OFF'|'ON'
                    }
                },
                'S3PutObjectRetention': {
                    'BypassGovernanceRetention': True|False,
                    'Retention': {
                        'RetainUntilDate': datetime(2015, 1, 1),
                        'Mode': 'COMPLIANCE'|'GOVERNANCE'
                    }
                }
            },
            'Priority': 123,
            'ProgressSummary': {
                'TotalNumberOfTasks': 123,
                'NumberOfTasksSucceeded': 123,
                'NumberOfTasksFailed': 123
            },
            'StatusUpdateReason': 'string',
            'FailureReasons': [
                {
                    'FailureCode': 'string',
                    'FailureReason': 'string'
                },
            ],
            'Report': {
                'Bucket': 'string',
                'Format': 'Report_CSV_20180820',
                'Enabled': True|False,
                'Prefix': 'string',
                'ReportScope': 'AllTasks'|'FailedTasksOnly'
            },
            'CreationTime': datetime(2015, 1, 1),
            'TerminationDate': datetime(2015, 1, 1),
            'RoleArn': 'string',
            'SuspendedDate': datetime(2015, 1, 1),
            'SuspendedCause': 'string'
        }
    }
    
    
    :returns: 
    AccountId (string) -- [REQUIRED]
    JobId (string) -- [REQUIRED]
    The ID for the job whose information you want to retrieve.
    
    
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

def get_access_point(AccountId=None, Name=None):
    """
    Returns configuration information about the specified access point.
    See also: AWS API Documentation
    
    
    :example: response = client.get_access_point(
        AccountId='string',
        Name='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe account ID for the account that owns the specified access point.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the access point whose configuration information you want to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string',
    'Bucket': 'string',
    'NetworkOrigin': 'Internet'|'VPC',
    'VpcConfiguration': {
        'VpcId': 'string'
    },
    'PublicAccessBlockConfiguration': {
        'BlockPublicAcls': True|False,
        'IgnorePublicAcls': True|False,
        'BlockPublicPolicy': True|False,
        'RestrictPublicBuckets': True|False
    },
    'CreationDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

Name (string) --
The name of the specified access point.

Bucket (string) --
The name of the bucket associated with the specified access point.

NetworkOrigin (string) --
Indicates whether this access point allows access from the public internet. If VpcConfiguration is specified for this access point, then NetworkOrigin is VPC , and the access point doesn\'t allow access from the public internet. Otherwise, NetworkOrigin is Internet , and the access point allows access from the public internet, subject to the access point and bucket access policies.

VpcConfiguration (dict) --
Contains the virtual private cloud (VPC) configuration for the specified access point.

VpcId (string) --
If this field is specified, this access point will only allow connections from the specified VPC ID.



PublicAccessBlockConfiguration (dict) --
The PublicAccessBlock configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see The Meaning of "Public" in the Amazon Simple Storage Service Developer Guide.

BlockPublicAcls (boolean) --
Specifies whether Amazon S3 should block public access control lists (ACLs) for buckets in this account. Setting this element to TRUE causes the following behavior:

PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
PUT Object calls fail if the request includes a public ACL.
PUT Bucket calls fail if the request includes a public ACL.

Enabling this setting doesn\'t affect existing policies or ACLs.

IgnorePublicAcls (boolean) --
Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting this element to TRUE causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain.
Enabling this setting doesn\'t affect the persistence of any existing ACLs and doesn\'t prevent new public ACLs from being set.

BlockPublicPolicy (boolean) --
Specifies whether Amazon S3 should block public bucket policies for buckets in this account. Setting this element to TRUE causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.
Enabling this setting doesn\'t affect existing bucket policies.

RestrictPublicBuckets (boolean) --
Specifies whether Amazon S3 should restrict public bucket policies for buckets in this account. Setting this element to TRUE restricts access to buckets with public policies to only AWS services and authorized users within this account.
Enabling this setting doesn\'t affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.



CreationDate (datetime) --
The date and time when the specified access point was created.








    :return: {
        'Name': 'string',
        'Bucket': 'string',
        'NetworkOrigin': 'Internet'|'VPC',
        'VpcConfiguration': {
            'VpcId': 'string'
        },
        'PublicAccessBlockConfiguration': {
            'BlockPublicAcls': True|False,
            'IgnorePublicAcls': True|False,
            'BlockPublicPolicy': True|False,
            'RestrictPublicBuckets': True|False
        },
        'CreationDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
    PUT Object calls fail if the request includes a public ACL.
    PUT Bucket calls fail if the request includes a public ACL.
    
    """
    pass

def get_access_point_policy(AccountId=None, Name=None):
    """
    Returns the access point policy associated with the specified access point.
    See also: AWS API Documentation
    
    
    :example: response = client.get_access_point_policy(
        AccountId='string',
        Name='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe account ID for the account that owns the specified access point.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the access point whose policy you want to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Policy': 'string'
}


Response Structure

(dict) --

Policy (string) --
The access point policy associated with the specified access point.








    :return: {
        'Policy': 'string'
    }
    
    
    """
    pass

def get_access_point_policy_status(AccountId=None, Name=None):
    """
    Indicates whether the specified access point currently has a policy that allows public access. For more information about public access through access points, see Managing Data Access with Amazon S3 Access Points in the Amazon Simple Storage Service Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_access_point_policy_status(
        AccountId='string',
        Name='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe account ID for the account that owns the specified access point.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the access point whose policy status you want to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PolicyStatus': {
        'IsPublic': True|False
    }
}


Response Structure

(dict) --

PolicyStatus (dict) --
Indicates the current policy status of the specified access point.

IsPublic (boolean) --









    :return: {
        'PolicyStatus': {
            'IsPublic': True|False
        }
    }
    
    
    :returns: 
    IsPublic (boolean) --
    
    """
    pass

def get_job_tagging(AccountId=None, JobId=None):
    """
    Returns the tags on an Amazon S3 Batch Operations job. To use this operation, you must have permission to perform the s3:GetJobTagging action. For more information, see Using Job Tags in the Amazon Simple Storage Service Developer Guide .
    Related actions include:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_job_tagging(
        AccountId='string',
        JobId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe AWS account ID associated with the Amazon S3 Batch Operations job.\n

    :type JobId: string
    :param JobId: [REQUIRED]\nThe ID for the Amazon S3 Batch Operations job whose tags you want to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --

Tags (list) --
The set of tags associated with the Amazon S3 Batch Operations job.

(dict) --
Key (string) --
Value (string) --










Exceptions

S3Control.Client.exceptions.InternalServiceException
S3Control.Client.exceptions.TooManyRequestsException
S3Control.Client.exceptions.NotFoundException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    AccountId (string) -- [REQUIRED]
    The AWS account ID associated with the Amazon S3 Batch Operations job.
    
    JobId (string) -- [REQUIRED]
    The ID for the Amazon S3 Batch Operations job whose tags you want to retrieve.
    
    
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

def get_public_access_block(AccountId=None):
    """
    Retrieves the PublicAccessBlock configuration for an Amazon Web Services account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_public_access_block(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe account ID for the Amazon Web Services account whose PublicAccessBlock configuration you want to retrieve.\n

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
PublicAccessBlockConfiguration (dict) --The PublicAccessBlock configuration currently in effect for this Amazon Web Services account.

BlockPublicAcls (boolean) --Specifies whether Amazon S3 should block public access control lists (ACLs) for buckets in this account. Setting this element to TRUE causes the following behavior:

PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
PUT Object calls fail if the request includes a public ACL.
PUT Bucket calls fail if the request includes a public ACL.

Enabling this setting doesn\'t affect existing policies or ACLs.

IgnorePublicAcls (boolean) --Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting this element to TRUE causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain.
Enabling this setting doesn\'t affect the persistence of any existing ACLs and doesn\'t prevent new public ACLs from being set.

BlockPublicPolicy (boolean) --Specifies whether Amazon S3 should block public bucket policies for buckets in this account. Setting this element to TRUE causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.
Enabling this setting doesn\'t affect existing bucket policies.

RestrictPublicBuckets (boolean) --Specifies whether Amazon S3 should restrict public bucket policies for buckets in this account. Setting this element to TRUE restricts access to buckets with public policies to only AWS services and authorized users within this account.
Enabling this setting doesn\'t affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.








Exceptions

S3Control.Client.exceptions.NoSuchPublicAccessBlockConfiguration


    :return: {
        'PublicAccessBlockConfiguration': {
            'BlockPublicAcls': True|False,
            'IgnorePublicAcls': True|False,
            'BlockPublicPolicy': True|False,
            'RestrictPublicBuckets': True|False
        }
    }
    
    
    :returns: 
    S3Control.Client.exceptions.NoSuchPublicAccessBlockConfiguration
    
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

def list_access_points(AccountId=None, Bucket=None, NextToken=None, MaxResults=None):
    """
    Returns a list of the access points currently associated with the specified bucket. You can retrieve up to 1000 access points per call. If the specified bucket has more than 1,000 access points (or the number specified in maxResults , whichever is less), the response will include a continuation token that you can use to list the additional access points.
    See also: AWS API Documentation
    
    
    :example: response = client.list_access_points(
        AccountId='string',
        Bucket='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe AWS account ID for owner of the bucket whose access points you want to list.\n

    :type Bucket: string
    :param Bucket: The name of the bucket whose associated access points you want to list.

    :type NextToken: string
    :param NextToken: A continuation token. If a previous call to ListAccessPoints returned a continuation token in the NextToken field, then providing that value here causes Amazon S3 to retrieve the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of access points that you want to include in the list. If the specified bucket has more than this number of access points, then the response will include a continuation token in the NextToken field that you can use to retrieve the next page of access points.

    :rtype: dict

ReturnsResponse Syntax
{
    'AccessPointList': [
        {
            'Name': 'string',
            'NetworkOrigin': 'Internet'|'VPC',
            'VpcConfiguration': {
                'VpcId': 'string'
            },
            'Bucket': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AccessPointList (list) --
Contains identification and configuration information for one or more access points associated with the specified bucket.

(dict) --
An access point used to access a bucket.

Name (string) --
The name of this access point.

NetworkOrigin (string) --
Indicates whether this access point allows access from the public internet. If VpcConfiguration is specified for this access point, then NetworkOrigin is VPC , and the access point doesn\'t allow access from the public internet. Otherwise, NetworkOrigin is Internet , and the access point allows access from the public internet, subject to the access point and bucket access policies.

VpcConfiguration (dict) --
The virtual private cloud (VPC) configuration for this access point, if one exists.

VpcId (string) --
If this field is specified, this access point will only allow connections from the specified VPC ID.



Bucket (string) --
The name of the bucket associated with this access point.





NextToken (string) --
If the specified bucket has more access points than can be returned in one call to this API, then this field contains a continuation token that you can provide in subsequent calls to this API to retrieve additional access points.








    :return: {
        'AccessPointList': [
            {
                'Name': 'string',
                'NetworkOrigin': 'Internet'|'VPC',
                'VpcConfiguration': {
                    'VpcId': 'string'
                },
                'Bucket': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_jobs(AccountId=None, JobStatuses=None, NextToken=None, MaxResults=None):
    """
    Lists current Amazon S3 Batch Operations jobs and jobs that have ended within the last 30 days for the AWS account making the request. For more information, see Amazon S3 Batch Operations in the Amazon Simple Storage Service Developer Guide .
    Related actions include:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_jobs(
        AccountId='string',
        JobStatuses=[
            'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'|'Failed'|'Failing'|'New'|'Paused'|'Pausing'|'Preparing'|'Ready'|'Suspended',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]

    :type JobStatuses: list
    :param JobStatuses: The List Jobs request returns jobs that match the statuses listed in this element.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: A pagination token to request the next page of results. Use the token that Amazon S3 returned in the NextToken element of the ListJobsResult from the previous List Jobs request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of jobs that Amazon S3 will include in the List Jobs response. If there are more jobs than this number, the response will include a pagination token in the NextToken field to enable you to retrieve the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Jobs': [
        {
            'JobId': 'string',
            'Description': 'string',
            'Operation': 'LambdaInvoke'|'S3PutObjectCopy'|'S3PutObjectAcl'|'S3PutObjectTagging'|'S3InitiateRestoreObject'|'S3PutObjectLegalHold'|'S3PutObjectRetention',
            'Priority': 123,
            'Status': 'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'|'Failed'|'Failing'|'New'|'Paused'|'Pausing'|'Preparing'|'Ready'|'Suspended',
            'CreationTime': datetime(2015, 1, 1),
            'TerminationDate': datetime(2015, 1, 1),
            'ProgressSummary': {
                'TotalNumberOfTasks': 123,
                'NumberOfTasksSucceeded': 123,
                'NumberOfTasksFailed': 123
            }
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If the List Jobs request produced more than the maximum number of results, you can pass this value into a subsequent List Jobs request in order to retrieve the next page of results.

Jobs (list) --
The list of current jobs and jobs that have ended within the last 30 days.

(dict) --
Contains the configuration and status information for a single job retrieved as part of a job list.

JobId (string) --
The ID for the specified job.

Description (string) --
The user-specified description that was included in the specified job\'s Create Job request.

Operation (string) --
The operation that the specified job is configured to run on each object listed in the manifest.

Priority (integer) --
The current priority for the specified job.

Status (string) --
The specified job\'s current status.

CreationTime (datetime) --
A timestamp indicating when the specified job was created.

TerminationDate (datetime) --
A timestamp indicating when the specified job terminated. A job\'s termination date is the date and time when it succeeded, failed, or was canceled.

ProgressSummary (dict) --
Describes the total number of tasks that the specified job has executed, the number of tasks that succeeded, and the number of tasks that failed.

TotalNumberOfTasks (integer) --
NumberOfTasksSucceeded (integer) --
NumberOfTasksFailed (integer) --












Exceptions

S3Control.Client.exceptions.InvalidRequestException
S3Control.Client.exceptions.InternalServiceException
S3Control.Client.exceptions.InvalidNextTokenException


    :return: {
        'NextToken': 'string',
        'Jobs': [
            {
                'JobId': 'string',
                'Description': 'string',
                'Operation': 'LambdaInvoke'|'S3PutObjectCopy'|'S3PutObjectAcl'|'S3PutObjectTagging'|'S3InitiateRestoreObject'|'S3PutObjectLegalHold'|'S3PutObjectRetention',
                'Priority': 123,
                'Status': 'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'|'Failed'|'Failing'|'New'|'Paused'|'Pausing'|'Preparing'|'Ready'|'Suspended',
                'CreationTime': datetime(2015, 1, 1),
                'TerminationDate': datetime(2015, 1, 1),
                'ProgressSummary': {
                    'TotalNumberOfTasks': 123,
                    'NumberOfTasksSucceeded': 123,
                    'NumberOfTasksFailed': 123
                }
            },
        ]
    }
    
    
    :returns: 
    AccountId (string) -- [REQUIRED]
    JobStatuses (list) -- The List Jobs request returns jobs that match the statuses listed in this element.
    
    (string) --
    
    
    NextToken (string) -- A pagination token to request the next page of results. Use the token that Amazon S3 returned in the NextToken element of the ListJobsResult from the previous List Jobs request.
    MaxResults (integer) -- The maximum number of jobs that Amazon S3 will include in the List Jobs response. If there are more jobs than this number, the response will include a pagination token in the NextToken field to enable you to retrieve the next page of results.
    
    """
    pass

def put_access_point_policy(AccountId=None, Name=None, Policy=None):
    """
    Associates an access policy with the specified access point. Each access point can have only one policy, so a request made to this API replaces any existing policy associated with the specified access point.
    See also: AWS API Documentation
    
    
    :example: response = client.put_access_point_policy(
        AccountId='string',
        Name='string',
        Policy='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe AWS account ID for owner of the bucket associated with the specified access point.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the access point that you want to associate with the specified policy.\n

    :type Policy: string
    :param Policy: [REQUIRED]\nThe policy that you want to apply to the specified access point. For more information about access point policies, see Managing Data Access with Amazon S3 Access Points in the Amazon Simple Storage Service Developer Guide .\n

    """
    pass

def put_job_tagging(AccountId=None, JobId=None, Tags=None):
    """
    Set the supplied tag-set on an Amazon S3 Batch Operations job.
    A tag is a key-value pair. You can associate Amazon S3 Batch Operations tags with any job by sending a PUT request against the tagging subresource that is associated with the job. To modify the existing tag set, you can either replace the existing tag set entirely, or make changes within the existing tag set by retrieving the existing tag set using  GetJobTagging , modify that tag set, and use this API action to replace the tag set with the one you have modified.. For more information, see Using Job Tags in the Amazon Simple Storage Service Developer Guide.
    To use this operation, you must have permission to perform the s3:PutJobTagging action.
    Related actions include:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_job_tagging(
        AccountId='string',
        JobId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe AWS account ID associated with the Amazon S3 Batch Operations job.\n

    :type JobId: string
    :param JobId: [REQUIRED]\nThe ID for the Amazon S3 Batch Operations job whose tags you want to replace.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe set of tags to associate with the Amazon S3 Batch Operations job.\n\n(dict) --\nKey (string) -- [REQUIRED]\nValue (string) -- [REQUIRED]\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

S3Control.Client.exceptions.InternalServiceException
S3Control.Client.exceptions.TooManyRequestsException
S3Control.Client.exceptions.NotFoundException
S3Control.Client.exceptions.TooManyTagsException


    :return: {}
    
    
    :returns: 
    CreateJob
    GetJobTagging
    DeleteJobTagging
    
    """
    pass

def put_public_access_block(PublicAccessBlockConfiguration=None, AccountId=None):
    """
    Creates or modifies the PublicAccessBlock configuration for an Amazon Web Services account.
    See also: AWS API Documentation
    
    
    :example: response = client.put_public_access_block(
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True|False,
            'IgnorePublicAcls': True|False,
            'BlockPublicPolicy': True|False,
            'RestrictPublicBuckets': True|False
        },
        AccountId='string'
    )
    
    
    :type PublicAccessBlockConfiguration: dict
    :param PublicAccessBlockConfiguration: [REQUIRED]\nThe PublicAccessBlock configuration that you want to apply to the specified Amazon Web Services account.\n\nBlockPublicAcls (boolean) --Specifies whether Amazon S3 should block public access control lists (ACLs) for buckets in this account. Setting this element to TRUE causes the following behavior:\n\nPUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.\nPUT Object calls fail if the request includes a public ACL.\nPUT Bucket calls fail if the request includes a public ACL.\n\nEnabling this setting doesn\'t affect existing policies or ACLs.\n\nIgnorePublicAcls (boolean) --Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting this element to TRUE causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain.\nEnabling this setting doesn\'t affect the persistence of any existing ACLs and doesn\'t prevent new public ACLs from being set.\n\nBlockPublicPolicy (boolean) --Specifies whether Amazon S3 should block public bucket policies for buckets in this account. Setting this element to TRUE causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.\nEnabling this setting doesn\'t affect existing bucket policies.\n\nRestrictPublicBuckets (boolean) --Specifies whether Amazon S3 should restrict public bucket policies for buckets in this account. Setting this element to TRUE restricts access to buckets with public policies to only AWS services and authorized users within this account.\nEnabling this setting doesn\'t affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.\n\n\n

    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe account ID for the Amazon Web Services account whose PublicAccessBlock configuration you want to set.\n

    """
    pass

def update_job_priority(AccountId=None, JobId=None, Priority=None):
    """
    Updates an existing Amazon S3 Batch Operations job\'s priority. For more information, see Amazon S3 Batch Operations in the Amazon Simple Storage Service Developer Guide.
    Related actions include:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_job_priority(
        AccountId='string',
        JobId='string',
        Priority=123
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]

    :type JobId: string
    :param JobId: [REQUIRED]\nThe ID for the job whose priority you want to update.\n

    :type Priority: integer
    :param Priority: [REQUIRED]\nThe priority you want to assign to this job.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string',
    'Priority': 123
}


Response Structure

(dict) --

JobId (string) --
The ID for the job whose priority Amazon S3 updated.

Priority (integer) --
The new priority assigned to the specified job.







Exceptions

S3Control.Client.exceptions.BadRequestException
S3Control.Client.exceptions.TooManyRequestsException
S3Control.Client.exceptions.NotFoundException
S3Control.Client.exceptions.InternalServiceException


    :return: {
        'JobId': 'string',
        'Priority': 123
    }
    
    
    :returns: 
    AccountId (string) -- [REQUIRED]
    JobId (string) -- [REQUIRED]
    The ID for the job whose priority you want to update.
    
    Priority (integer) -- [REQUIRED]
    The priority you want to assign to this job.
    
    
    """
    pass

def update_job_status(AccountId=None, JobId=None, RequestedJobStatus=None, StatusUpdateReason=None):
    """
    Updates the status for the specified job. Use this operation to confirm that you want to run a job or to cancel an existing job. For more information, see Amazon S3 Batch Operations in the Amazon Simple Storage Service Developer Guide.
    Related actions include:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_job_status(
        AccountId='string',
        JobId='string',
        RequestedJobStatus='Cancelled'|'Ready',
        StatusUpdateReason='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]

    :type JobId: string
    :param JobId: [REQUIRED]\nThe ID of the job whose status you want to update.\n

    :type RequestedJobStatus: string
    :param RequestedJobStatus: [REQUIRED]\nThe status that you want to move the specified job to.\n

    :type StatusUpdateReason: string
    :param StatusUpdateReason: A description of the reason why you want to change the specified job\'s status. This field can be any string up to the maximum length.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string',
    'Status': 'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'|'Failed'|'Failing'|'New'|'Paused'|'Pausing'|'Preparing'|'Ready'|'Suspended',
    'StatusUpdateReason': 'string'
}


Response Structure

(dict) --

JobId (string) --
The ID for the job whose status was updated.

Status (string) --
The current status for the specified job.

StatusUpdateReason (string) --
The reason that the specified job\'s status was updated.







Exceptions

S3Control.Client.exceptions.BadRequestException
S3Control.Client.exceptions.TooManyRequestsException
S3Control.Client.exceptions.NotFoundException
S3Control.Client.exceptions.JobStatusException
S3Control.Client.exceptions.InternalServiceException


    :return: {
        'JobId': 'string',
        'Status': 'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'|'Failed'|'Failing'|'New'|'Paused'|'Pausing'|'Preparing'|'Ready'|'Suspended',
        'StatusUpdateReason': 'string'
    }
    
    
    :returns: 
    AccountId (string) -- [REQUIRED]
    JobId (string) -- [REQUIRED]
    The ID of the job whose status you want to update.
    
    RequestedJobStatus (string) -- [REQUIRED]
    The status that you want to move the specified job to.
    
    StatusUpdateReason (string) -- A description of the reason why you want to change the specified job\'s status. This field can be any string up to the maximum length.
    
    """
    pass

