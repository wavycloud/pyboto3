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


def abort_multipart_upload(accountId=None, vaultName=None, uploadId=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param uploadId: [REQUIRED]
            The upload ID of the multipart upload to delete.
            
    :type uploadId: string
    """
    pass


def abort_vault_lock(accountId=None, vaultName=None):
    """
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    """
    pass


def add_tags_to_vault(accountId=None, vaultName=None, Tags=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param Tags: The tags to add to the vault. Each tag is composed of a key and a value. The value can be an empty string.
            (string) --
            (string) --
            
    :type Tags: dict
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


def complete_multipart_upload(accountId=None, vaultName=None, uploadId=None, archiveSize=None, checksum=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param uploadId: [REQUIRED]
            The upload ID of the multipart upload.
            
    :type uploadId: string
    :param archiveSize: The total size, in bytes, of the entire archive. This value should be the sum of all the sizes of the individual parts that you uploaded.
    :type archiveSize: string
    :param checksum: The SHA256 tree hash of the entire archive. It is the tree hash of SHA256 tree hash of the individual parts. If the value you specify in the request does not match the SHA256 tree hash of the final assembled archive as computed by Amazon Glacier, Amazon Glacier returns an error and the request fails.
            This is a required field.Ideally you will want to compute this value with checksums from
            previous uploaded parts, using the algorithm described in
            Glacier documentation.
            But if you prefer, you can also use botocore.util.calculate_tree_hash()
            to compute it from raw file by:
            checksum = calculate_tree_hash(open('your_file.txt', 'rb'))
            
    :type checksum: string
    """
    pass


def complete_vault_lock(accountId=None, vaultName=None, lockId=None):
    """
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param lockId: [REQUIRED]
            The lockId value is the lock ID obtained from a InitiateVaultLock request.
            
    :type lockId: string
    """
    pass


def create_vault(accountId=None, vaultName=None):
    """
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    """
    pass


def delete_archive(accountId=None, vaultName=None, archiveId=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param archiveId: [REQUIRED]
            The ID of the archive to delete.
            
    :type archiveId: string
    """
    pass


def delete_vault(accountId=None, vaultName=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    """
    pass


def delete_vault_access_policy(accountId=None, vaultName=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    """
    pass


def delete_vault_notifications(accountId=None, vaultName=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    """
    pass


def describe_job(accountId=None, vaultName=None, jobId=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param jobId: [REQUIRED]
            The ID of the job to describe.
            
    :type jobId: string
    """
    pass


def describe_vault(accountId=None, vaultName=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
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


def get_data_retrieval_policy(accountId=None):
    """
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            Return typedict
            ReturnsResponse Syntax{
              'Policy': {
                'Rules': [
                  {
                    'Strategy': 'string',
                    'BytesPerHour': 123
                  },
                ]
              }
            }
            Response Structure
            (dict) --Contains the Amazon Glacier response to the GetDataRetrievalPolicy request.
            Policy (dict) --Contains the returned data retrieval policy in JSON format.
            Rules (list) --The policy rule. Although this is a list type, currently there must be only one rule, which contains a Strategy field and optionally a BytesPerHour field.
            (dict) --Data retrieval policy rule.
            Strategy (string) --The type of data retrieval policy to set.
            Valid values: BytesPerHour|FreeTier|None
            BytesPerHour (integer) --The maximum number of bytes that can be retrieved in an hour.
            This field is required only if the value of the Strategy field is BytesPerHour . Your PUT operation will be rejected if the Strategy field is not set to BytesPerHour and you set this field.
            
            
            
            
    :type accountId: string
    """
    pass


def get_job_output(accountId=None, vaultName=None, jobId=None, range=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param jobId: [REQUIRED]
            The job ID whose data is downloaded.
            
    :type jobId: string
    :param range: The range of bytes to retrieve from the output. For example, if you want to download the first 1,048,576 bytes, specify 'Range: bytes=0-1048575'. By default, this operation downloads the entire output.
    :type range: string
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


def get_vault_access_policy(accountId=None, vaultName=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    """
    pass


def get_vault_lock(accountId=None, vaultName=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    """
    pass


def get_vault_notifications(accountId=None, vaultName=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    """
    pass


def get_waiter():
    """
    """
    pass


def initiate_job(accountId=None, vaultName=None, jobParameters=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param jobParameters: Provides options for specifying job information.
            Format (string) --When initiating a job to retrieve a vault inventory, you can optionally add this parameter to your request to specify the output format. If you are initiating an inventory job and do not specify a Format field, JSON is the default format. Valid values are 'CSV' and 'JSON'.
            Type (string) --The job type. You can initiate a job to retrieve an archive or get an inventory of a vault. Valid values are 'archive-retrieval' and 'inventory-retrieval'.
            ArchiveId (string) --The ID of the archive that you want to retrieve. This field is required only if Type is set to archive-retrieval. An error occurs if you specify this request parameter for an inventory retrieval job request.
            Description (string) --The optional description for the job. The description must be less than or equal to 1,024 bytes. The allowable characters are 7-bit ASCII without control codes-specifically, ASCII values 32-126 decimal or 0x20-0x7E hexadecimal.
            SNSTopic (string) --The Amazon SNS topic ARN to which Amazon Glacier sends a notification when the job is completed and the output is ready for you to download. The specified topic publishes the notification to its subscribers. The SNS topic must exist.
            RetrievalByteRange (string) --The byte range to retrieve for an archive retrieval. in the form 'StartByteValue -EndByteValue ' If not specified, the whole archive is retrieved. If specified, the byte range must be megabyte (1024*1024) aligned which means that StartByteValue must be divisible by 1 MB and EndByteValue plus 1 must be divisible by 1 MB or be the end of the archive specified as the archive byte size value minus 1. If RetrievalByteRange is not megabyte aligned, this operation returns a 400 response.
            An error occurs if you specify this field for an inventory retrieval job request.
            InventoryRetrievalParameters (dict) --Input parameters used for range inventory retrieval.
            StartDate (string) --The start of the date range in UTC for vault inventory retrieval that includes archives created on or after this date. A string representation of ISO 8601 date format, for example, 2013-03-20T17:03:43Z.
            EndDate (string) --The end of the date range in UTC for vault inventory retrieval that includes archives created before this date. A string representation of ISO 8601 date format, for example, 2013-03-20T17:03:43Z.
            Limit (string) --Specifies the maximum number of inventory items returned per vault inventory retrieval request. Valid values are greater than or equal to 1.
            Marker (string) --An opaque string that represents where to continue pagination of the vault inventory retrieval results. You use the marker in a new InitiateJob request to obtain additional inventory items. If there are no more inventory items, this value is null .
            
            
    :type jobParameters: dict
    """
    pass


def initiate_multipart_upload(accountId=None, vaultName=None, archiveDescription=None, partSize=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param archiveDescription: The archive description that you are uploading in parts.
            The part size must be a megabyte (1024 KB) multiplied by a power of 2, for example 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB (4096 MB).
            
    :type archiveDescription: string
    :param partSize: The size of each part except the last, in bytes. The last part can be smaller than this part size.
    :type partSize: string
    """
    pass


def initiate_vault_lock(accountId=None, vaultName=None, policy=None):
    """
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param policy: The vault lock policy as a JSON string, which uses '' as an escape character.
            Policy (string) --The vault lock policy.
            
    :type policy: dict
    """
    pass


def list_jobs(accountId=None, vaultName=None, limit=None, marker=None, statuscode=None, completed=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param limit: Specifies that the response be limited to the specified number of items or fewer. If not specified, the List Jobs operation returns up to 1,000 jobs.
    :type limit: string
    :param marker: An opaque string used for pagination. This value specifies the job at which the listing of jobs should begin. Get the marker value from a previous List Jobs response. You need only include the marker if you are continuing the pagination of results started in a previous List Jobs request.
    :type marker: string
    :param statuscode: Specifies the type of job status to return. You can specify the following values: 'InProgress', 'Succeeded', or 'Failed'.
    :type statuscode: string
    :param completed: Specifies the state of the jobs to return. You can specify true or false .
    :type completed: string
    """
    pass


def list_multipart_uploads(accountId=None, vaultName=None, marker=None, limit=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param marker: An opaque string used for pagination. This value specifies the upload at which the listing of uploads should begin. Get the marker value from a previous List Uploads response. You need only include the marker if you are continuing the pagination of results started in a previous List Uploads request.
    :type marker: string
    :param limit: Specifies the maximum number of uploads returned in the response body. If this value is not specified, the List Uploads operation returns up to 1,000 uploads.
    :type limit: string
    """
    pass


def list_parts(accountId=None, vaultName=None, uploadId=None, marker=None, limit=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param uploadId: [REQUIRED]
            The upload ID of the multipart upload.
            
    :type uploadId: string
    :param marker: An opaque string used for pagination. This value specifies the part at which the listing of parts should begin. Get the marker value from the response of a previous List Parts response. You need only include the marker if you are continuing the pagination of results started in a previous List Parts request.
    :type marker: string
    :param limit: Specifies the maximum number of parts returned in the response body. If this value is not specified, the List Parts operation returns up to 1,000 uploads.
    :type limit: string
    """
    pass


def list_tags_for_vault(accountId=None, vaultName=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    """
    pass


def list_vaults(accountId=None, marker=None, limit=None):
    """
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param marker: A string used for pagination. The marker specifies the vault ARN after which the listing of vaults should begin.
    :type marker: string
    :param limit: The maximum number of items returned in the response. If you don't specify a value, the List Vaults operation returns up to 1,000 items.
    :type limit: string
    """
    pass


def remove_tags_from_vault(accountId=None, vaultName=None, TagKeys=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param TagKeys: A list of tag keys. Each corresponding tag is removed from the vault.
            (string) --
            
    :type TagKeys: list
    """
    pass


def set_data_retrieval_policy(accountId=None, Policy=None):
    """
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param Policy: The data retrieval policy in JSON format.
            Rules (list) --The policy rule. Although this is a list type, currently there must be only one rule, which contains a Strategy field and optionally a BytesPerHour field.
            (dict) --Data retrieval policy rule.
            Strategy (string) --The type of data retrieval policy to set.
            Valid values: BytesPerHour|FreeTier|None
            BytesPerHour (integer) --The maximum number of bytes that can be retrieved in an hour.
            This field is required only if the value of the Strategy field is BytesPerHour . Your PUT operation will be rejected if the Strategy field is not set to BytesPerHour and you set this field.
            
            
    :type Policy: dict
    """
    pass


def set_vault_access_policy(accountId=None, vaultName=None, policy=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param policy: The vault access policy as a JSON string.
            Policy (string) --The vault access policy.
            
    :type policy: dict
    """
    pass


def set_vault_notifications(accountId=None, vaultName=None, vaultNotificationConfig=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param vaultNotificationConfig: Provides options for specifying notification configuration.
            SNSTopic (string) --The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).
            Events (list) --A list of one or more events for which Amazon Glacier will send a notification to the specified Amazon SNS topic.
            (string) --
            
    :type vaultNotificationConfig: dict
    """
    pass


def upload_archive(vaultName=None, accountId=None, archiveDescription=None, checksum=None, body=None):
    """
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param archiveDescription: The optional description of the archive you are uploading.
    :type archiveDescription: string
    :param checksum: The SHA256 tree hash of the data being uploaded.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
            
    :type checksum: string
    :param body: The data to upload.
    :type body: bytes or seekable file-like object
    """
    pass


def upload_multipart_part(accountId=None, vaultName=None, uploadId=None, checksum=None, range=None, body=None):
    """
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single apos``-`` apos (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (apos-apos) in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            
    :type accountId: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            
    :type vaultName: string
    :param uploadId: [REQUIRED]
            The upload ID of the multipart upload.
            
    :type uploadId: string
    :param checksum: The SHA256 tree hash of the data being uploaded.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
            
    :type checksum: string
    :param range: Identifies the range of bytes in the assembled archive that will be uploaded in this part. Amazon Glacier uses this information to assemble the archive in the proper sequence. The format of this header follows RFC 2616. An example header is Content-Range:bytes 0-4194303/*.
    :type range: string
    :param body: The data to upload.
    :type body: bytes or seekable file-like object
    """
    pass
