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

def abort_multipart_upload(accountId=None, vaultName=None, uploadId=None):
    """
    This operation aborts a multipart upload identified by the upload ID.
    After the Abort Multipart Upload request succeeds, you cannot upload any more parts to the multipart upload or complete the multipart upload. Aborting a completed upload fails. However, aborting an already-aborted upload will succeed, for a short time. For more information about uploading a part and completing a multipart upload, see  UploadMultipartPart and  CompleteMultipartUpload .
    This operation is idempotent.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Working with Archives in Amazon Glacier and Abort Multipart Upload in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The example deletes an in-progress multipart upload to a vault named my-vault:
    Expected Output:
    
    :example: response = client.abort_multipart_upload(
        vaultName='string',
        uploadId='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type uploadId: string
    :param uploadId: [REQUIRED]
            The upload ID of the multipart upload to delete.
            

    :return: response = client.abort_multipart_upload(
        accountId='-',
        uploadId='19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ',
        vaultName='my-vault',
    )
    
    print(response)
    
    
    """
    pass

def abort_vault_lock(accountId=None, vaultName=None):
    """
    This operation aborts the vault locking process if the vault lock is not in the Locked state. If the vault lock is in the Locked state when this operation is requested, the operation returns an AccessDeniedException error. Aborting the vault locking process removes the vault lock policy from the specified vault.
    A vault lock is put into the InProgress state by calling  InitiateVaultLock . A vault lock is put into the Locked state by calling  CompleteVaultLock . You can get the state of a vault lock by calling  GetVaultLock . For more information about the vault locking process, see Amazon Glacier Vault Lock . For more information about vault lock policies, see Amazon Glacier Access Control with Vault Lock Policies .
    This operation is idempotent. You can successfully invoke this operation multiple times, if the vault lock is in the InProgress state or if there is no policy associated with the vault.
    See also: AWS API Documentation
    
    Examples
    The example aborts the vault locking process if the vault lock is not in the Locked state for the vault named examplevault.
    Expected Output:
    
    :example: response = client.abort_vault_lock(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :return: response = client.abort_vault_lock(
        accountId='-',
        vaultName='examplevault',
    )
    
    print(response)
    
    
    """
    pass

def add_tags_to_vault(accountId=None, vaultName=None, Tags=None):
    """
    This operation adds the specified tags to a vault. Each tag is composed of a key and a value. Each vault can have up to 10 tags. If your request would cause the tag limit for the vault to be exceeded, the operation throws the LimitExceededException error. If a tag already exists on the vault under a specified key, the existing key value will be overwritten. For more information about tags, see Tagging Amazon Glacier Resources .
    See also: AWS API Documentation
    
    Examples
    The example adds two tags to a my-vault.
    Expected Output:
    
    :example: response = client.add_tags_to_vault(
        vaultName='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type Tags: dict
    :param Tags: The tags to add to the vault. Each tag is composed of a key and a value. The value can be an empty string.
            (string) --
            (string) --
            

    :return: response = client.add_tags_to_vault(
        Tags={
            'examplekey1': 'examplevalue1',
            'examplekey2': 'examplevalue2',
        },
        accountId='-',
        vaultName='my-vault',
    )
    
    print(response)
    
    
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

def complete_multipart_upload(accountId=None, vaultName=None, uploadId=None, archiveSize=None, checksum=None):
    """
    You call this operation to inform Amazon Glacier that all the archive parts have been uploaded and that Amazon Glacier can now assemble the archive from the uploaded parts. After assembling and saving the archive to the vault, Amazon Glacier returns the URI path of the newly created archive resource. Using the URI path, you can then access the archive. After you upload an archive, you should save the archive ID returned to retrieve the archive at a later point. You can also get the vault inventory to obtain a list of archive IDs in a vault. For more information, see  InitiateJob .
    In the request, you must include the computed SHA256 tree hash of the entire archive you have uploaded. For information about computing a SHA256 tree hash, see Computing Checksums . On the server side, Amazon Glacier also constructs the SHA256 tree hash of the assembled archive. If the values match, Amazon Glacier saves the archive to the vault; otherwise, it returns an error, and the operation fails. The  ListParts operation returns a list of parts uploaded for a specific multipart upload. It includes checksum information for each uploaded part that can be used to debug a bad checksum issue.
    Additionally, Amazon Glacier also checks for any missing content ranges when assembling the archive, if missing content ranges are found, Amazon Glacier returns an error and the operation fails.
    Complete Multipart Upload is an idempotent operation. After your first successful complete multipart upload, if you call the operation again within a short period, the operation will succeed and return the same archive ID. This is useful in the event you experience a network issue that causes an aborted connection or receive a 500 server error, in which case you can repeat your Complete Multipart Upload request and get the same archive ID without creating duplicate archives. Note, however, that after the multipart upload completes, you cannot call the List Parts operation and the multipart upload will not appear in List Multipart Uploads response, even if idempotent complete is possible.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Uploading Large Archives in Parts (Multipart Upload) and Complete Multipart Upload in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The example completes a multipart upload for a 3 MiB archive.
    Expected Output:
    
    :example: response = client.complete_multipart_upload(
        vaultName='string',
        uploadId='string',
        archiveSize='string',
        checksum='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type uploadId: string
    :param uploadId: [REQUIRED]
            The upload ID of the multipart upload.
            

    :type archiveSize: string
    :param archiveSize: The total size, in bytes, of the entire archive. This value should be the sum of all the sizes of the individual parts that you uploaded.

    :type checksum: string
    :param checksum: The SHA256 tree hash of the entire archive. It is the tree hash of SHA256 tree hash of the individual parts. If the value you specify in the request does not match the SHA256 tree hash of the final assembled archive as computed by Amazon Glacier, Amazon Glacier returns an error and the request fails.
            This is a required field.Ideally you will want to compute this value with checksums from
            previous uploaded parts, using the algorithm described in
            Glacier documentation.
            But if you prefer, you can also use botocore.utils.calculate_tree_hash()
            to compute it from raw file by:
            checksum = calculate_tree_hash(open('your_file.txt', 'rb'))
            

    :rtype: dict
    :return: checksum = calculate_tree_hash(open('your_file.txt', 'rb'))
    
    
    """
    pass

def complete_vault_lock(accountId=None, vaultName=None, lockId=None):
    """
    This operation completes the vault locking process by transitioning the vault lock from the InProgress state to the Locked state, which causes the vault lock policy to become unchangeable. A vault lock is put into the InProgress state by calling  InitiateVaultLock . You can obtain the state of the vault lock by calling  GetVaultLock . For more information about the vault locking process, Amazon Glacier Vault Lock .
    This operation is idempotent. This request is always successful if the vault lock is in the Locked state and the provided lock ID matches the lock ID originally used to lock the vault.
    If an invalid lock ID is passed in the request when the vault lock is in the Locked state, the operation returns an AccessDeniedException error. If an invalid lock ID is passed in the request when the vault lock is in the InProgress state, the operation throws an InvalidParameter error.
    See also: AWS API Documentation
    
    Examples
    The example completes the vault locking process by transitioning the vault lock from the InProgress state to the Locked state.
    Expected Output:
    
    :example: response = client.complete_vault_lock(
        vaultName='string',
        lockId='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type lockId: string
    :param lockId: [REQUIRED]
            The lockId value is the lock ID obtained from a InitiateVaultLock request.
            

    :return: response = client.complete_vault_lock(
        accountId='-',
        lockId='AE863rKkWZU53SLW5be4DUcW',
        vaultName='example-vault',
    )
    
    print(response)
    
    
    """
    pass

def create_vault(accountId=None, vaultName=None):
    """
    This operation creates a new vault with the specified name. The name of the vault must be unique within a region for an AWS account. You can create up to 1,000 vaults per account. If you need to create more vaults, contact Amazon Glacier.
    You must use the following guidelines when naming a vault.
    This operation is idempotent.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Creating a Vault in Amazon Glacier and Create Vault in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example creates a new vault named my-vault.
    Expected Output:
    
    :example: response = client.create_vault(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :rtype: dict
    :return: {
        'location': 'string'
    }
    
    
    :returns: 
    accountId (string) -- The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
    
    Note: this parameter is set to "-" bydefault if no value is not specified.
    
    vaultName (string) -- [REQUIRED]
    The name of the vault.
    
    
    """
    pass

def delete_archive(accountId=None, vaultName=None, archiveId=None):
    """
    This operation deletes an archive from a vault. Subsequent requests to initiate a retrieval of this archive will fail. Archive retrievals that are in progress for this archive ID may or may not succeed according to the following scenarios:
    This operation is idempotent. Attempting to delete an already-deleted archive does not result in an error.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Deleting an Archive in Amazon Glacier and Delete Archive in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The example deletes the archive specified by the archive ID.
    Expected Output:
    
    :example: response = client.delete_archive(
        vaultName='string',
        archiveId='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type archiveId: string
    :param archiveId: [REQUIRED]
            The ID of the archive to delete.
            

    :return: response = client.delete_archive(
        accountId='-',
        archiveId='NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId',
        vaultName='examplevault',
    )
    
    print(response)
    
    
    :returns: 
    accountId (string) -- The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    
    Note: this parameter is set to "-" bydefault if no value is not specified.
    
    vaultName (string) -- [REQUIRED]
    The name of the vault.
    
    archiveId (string) -- [REQUIRED]
    The ID of the archive to delete.
    
    
    """
    pass

def delete_vault(accountId=None, vaultName=None):
    """
    This operation deletes a vault. Amazon Glacier will delete a vault only if there are no archives in the vault as of the last inventory and there have been no writes to the vault since the last inventory. If either of these conditions is not satisfied, the vault deletion fails (that is, the vault is not removed) and Amazon Glacier returns an error. You can use  DescribeVault to return the number of archives in a vault, and you can use Initiate a Job (POST jobs) to initiate a new inventory retrieval for a vault. The inventory contains the archive IDs you use to delete archives using Delete Archive (DELETE archive) .
    This operation is idempotent.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Deleting a Vault in Amazon Glacier and Delete Vault in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The example deletes a vault named my-vault:
    Expected Output:
    
    :example: response = client.delete_vault(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :return: response = client.delete_vault(
        accountId='-',
        vaultName='my-vault',
    )
    
    print(response)
    
    
    """
    pass

def delete_vault_access_policy(accountId=None, vaultName=None):
    """
    This operation deletes the access policy associated with the specified vault. The operation is eventually consistent; that is, it might take some time for Amazon Glacier to completely remove the access policy, and you might still see the effect of the policy for a short time after you send the delete request.
    This operation is idempotent. You can invoke delete multiple times, even if there is no policy associated with the vault. For more information about vault access policies, see Amazon Glacier Access Control with Vault Access Policies .
    See also: AWS API Documentation
    
    Examples
    The example deletes the access policy associated with the vault named examplevault.
    Expected Output:
    
    :example: response = client.delete_vault_access_policy(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :return: response = client.delete_vault_access_policy(
        accountId='-',
        vaultName='examplevault',
    )
    
    print(response)
    
    
    """
    pass

def delete_vault_notifications(accountId=None, vaultName=None):
    """
    This operation deletes the notification configuration set for a vault. The operation is eventually consistent; that is, it might take some time for Amazon Glacier to completely disable the notifications and you might still receive some notifications for a short time after you send the delete request.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Configuring Vault Notifications in Amazon Glacier and Delete Vault Notification Configuration in the Amazon Glacier Developer Guide.
    See also: AWS API Documentation
    
    Examples
    The example deletes the notification configuration set for the vault named examplevault.
    Expected Output:
    
    :example: response = client.delete_vault_notifications(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :return: response = client.delete_vault_notifications(
        accountId='-',
        vaultName='examplevault',
    )
    
    print(response)
    
    
    """
    pass

def describe_job(accountId=None, vaultName=None, jobId=None):
    """
    This operation returns information about a job you previously initiated, including the job initiation date, the user who initiated the job, the job status code/message and the Amazon SNS topic to notify after Amazon Glacier completes the job. For more information about initiating a job, see  InitiateJob .
    A job ID will not expire for at least 24 hours after Amazon Glacier completes the job.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For information about the underlying REST API, see Working with Archives in Amazon Glacier in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The example returns information about the previously initiated job specified by the job ID.
    Expected Output:
    
    :example: response = client.describe_job(
        vaultName='string',
        jobId='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type jobId: string
    :param jobId: [REQUIRED]
            The ID of the job to describe.
            

    :rtype: dict
    :return: {
        'JobId': 'string',
        'JobDescription': 'string',
        'Action': 'ArchiveRetrieval'|'InventoryRetrieval',
        'ArchiveId': 'string',
        'VaultARN': 'string',
        'CreationDate': 'string',
        'Completed': True|False,
        'StatusCode': 'InProgress'|'Succeeded'|'Failed',
        'StatusMessage': 'string',
        'ArchiveSizeInBytes': 123,
        'InventorySizeInBytes': 123,
        'SNSTopic': 'string',
        'CompletionDate': 'string',
        'SHA256TreeHash': 'string',
        'ArchiveSHA256TreeHash': 'string',
        'RetrievalByteRange': 'string',
        'Tier': 'string',
        'InventoryRetrievalParameters': {
            'Format': 'string',
            'StartDate': 'string',
            'EndDate': 'string',
            'Limit': 'string',
            'Marker': 'string'
        }
    }
    
    
    :returns: 
    Archive retrieval jobs that specify a range that is not tree-hash aligned.
    Archival jobs that specify a range that is equal to the whole archive and the job status is InProgress.
    Inventory jobs.
    
    """
    pass

def describe_vault(accountId=None, vaultName=None):
    """
    This operation returns information about a vault, including the vault's Amazon Resource Name (ARN), the date the vault was created, the number of archives it contains, and the total size of all the archives in the vault. The number of archives and their total size are as of the last inventory generation. This means that if you add or remove an archive from a vault, and then immediately use Describe Vault, the change in contents will not be immediately reflected. If you want to retrieve the latest inventory of the vault, use  InitiateJob . Amazon Glacier generates vault inventories approximately daily. For more information, see Downloading a Vault Inventory in Amazon Glacier .
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Retrieving Vault Metadata in Amazon Glacier and Describe Vault in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The example retrieves data about a vault named my-vault.
    Expected Output:
    
    :example: response = client.describe_vault(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :rtype: dict
    :return: {
        'VaultARN': 'string',
        'VaultName': 'string',
        'CreationDate': 'string',
        'LastInventoryDate': 'string',
        'NumberOfArchives': 123,
        'SizeInBytes': 123
    }
    
    
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

def get_data_retrieval_policy(accountId=None):
    """
    This operation returns the current data retrieval policy for the account and region specified in the GET request. For more information about data retrieval policies, see Amazon Glacier Data Retrieval Policies .
    See also: AWS API Documentation
    
    Examples
    The example returns the current data retrieval policy for the account.
    Expected Output:
    
    :example: response = client.get_data_retrieval_policy(
    
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :rtype: dict
    :return: {
        'Policy': {
            'Rules': [
                {
                    'Strategy': 'string',
                    'BytesPerHour': 123
                },
            ]
        }
    }
    
    
    """
    pass

def get_job_output(accountId=None, vaultName=None, jobId=None, range=None):
    """
    This operation downloads the output of the job you initiated using  InitiateJob . Depending on the job type you specified when you initiated the job, the output will be either the content of an archive or a vault inventory.
    You can download all the job output or download a portion of the output by specifying a byte range. In the case of an archive retrieval job, depending on the byte range you specify, Amazon Glacier returns the checksum for the portion of the data. You can compute the checksum on the client and verify that the values match to ensure the portion you downloaded is the correct data.
    A job ID will not expire for at least 24 hours after Amazon Glacier completes the job. That a byte range. For both archive and inventory retrieval jobs, you should verify the downloaded size against the size returned in the headers from the Get Job Output response.
    For archive retrieval jobs, you should also verify that the size is what you expected. If you download a portion of the output, the expected size is based on the range of bytes you specified. For example, if you specify a range of bytes=0-1048575 , you should verify your download size is 1,048,576 bytes. If you download an entire archive, the expected size is the size of the archive when you uploaded it to Amazon Glacier The expected size is also returned in the headers from the Get Job Output response.
    In the case of an archive retrieval job, depending on the byte range you specify, Amazon Glacier returns the checksum for the portion of the data. To ensure the portion you downloaded is the correct data, compute the checksum on the client, verify that the values match, and verify that the size is what you expected.
    A job ID does not expire for at least 24 hours after Amazon Glacier completes the job. That is, you can download the job output within the 24 hours period after Amazon Glacier completes the job.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and the underlying REST API, see Downloading a Vault Inventory , Downloading an Archive , and Get Job Output
    See also: AWS API Documentation
    
    Examples
    The example downloads the output of a previously initiated inventory retrieval job that is identified by the job ID.
    Expected Output:
    
    :example: response = client.get_job_output(
        vaultName='string',
        jobId='string',
        range='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type jobId: string
    :param jobId: [REQUIRED]
            The job ID whose data is downloaded.
            

    :type range: string
    :param range: The range of bytes to retrieve from the output. For example, if you want to download the first 1,048,576 bytes, specify the range as bytes=0-1048575 . By default, this operation downloads the entire output.
            If the job output is large, then you can use a range to retrieve a portion of the output. This allows you to download the entire output in smaller chunks of bytes. For example, suppose you have 1 GB of job output you want to download and you decide to download 128 MB chunks of data at a time, which is a total of eight Get Job Output requests. You use the following process to download the job output:
            Download a 128 MB chunk of output by specifying the appropriate byte range. Verify that all 128 MB of data was received.
            Along with the data, the response includes a SHA256 tree hash of the payload. You compute the checksum of the payload on the client and compare it with the checksum you received in the response to ensure you received all the expected data.
            Repeat steps 1 and 2 for all the eight 128 MB chunks of output data, each time specifying the appropriate byte range.
            After downloading all the parts of the job output, you have a list of eight checksum values. Compute the tree hash of these values to find the checksum of the entire output. Using the DescribeJob API, obtain job information of the job that provided you the output. The response includes the checksum of the entire archive stored in Amazon Glacier. You compare this value with the checksum you computed to ensure you have downloaded the entire archive content with no errors.
            

    :rtype: dict
    :return: {
        'body': StreamingBody(),
        'checksum': 'string',
        'status': 123,
        'contentRange': 'string',
        'acceptRanges': 'string',
        'contentType': 'string',
        'archiveDescription': 'string'
    }
    
    
    :returns: 
    You get the entire range of the archive.
    You request a range to return of the archive that starts and ends on a multiple of 1 MB. For example, if you have an 3.1 MB archive and you specify a range to return that starts at 1 MB and ends at 2 MB, then the x-amz-sha256-tree-hash is returned as a response header.
    You request a range of the archive to return that starts on a multiple of 1 MB and goes to the end of the archive. For example, if you have a 3.1 MB archive and you specify a range that starts at 2 MB and ends at 3.1 MB (the end of the archive), then the x-amz-sha256-tree-hash is returned as a response header.
    
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

def get_vault_access_policy(accountId=None, vaultName=None):
    """
    This operation retrieves the access-policy subresource set on the vault; for more information on setting this subresource, see Set Vault Access Policy (PUT access-policy) . If there is no access policy set on the vault, the operation returns a 404 Not found error. For more information about vault access policies, see Amazon Glacier Access Control with Vault Access Policies .
    See also: AWS API Documentation
    
    Examples
    The example retrieves the access-policy set on the vault named example-vault.
    Expected Output:
    
    :example: response = client.get_vault_access_policy(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :rtype: dict
    :return: {
        'policy': {
            'Policy': 'string'
        }
    }
    
    
    """
    pass

def get_vault_lock(accountId=None, vaultName=None):
    """
    This operation retrieves the following attributes from the lock-policy subresource set on the specified vault:
    A vault lock is put into the InProgress state by calling  InitiateVaultLock . A vault lock is put into the Locked state by calling  CompleteVaultLock . You can abort the vault locking process by calling  AbortVaultLock . For more information about the vault locking process, Amazon Glacier Vault Lock .
    If there is no vault lock policy set on the vault, the operation returns a 404 Not found error. For more information about vault lock policies, Amazon Glacier Access Control with Vault Lock Policies .
    See also: AWS API Documentation
    
    Examples
    The example retrieves the attributes from the lock-policy subresource set on the vault named examplevault.
    Expected Output:
    
    :example: response = client.get_vault_lock(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :rtype: dict
    :return: {
        'Policy': 'string',
        'State': 'string',
        'ExpirationDate': 'string',
        'CreationDate': 'string'
    }
    
    
    :returns: 
    accountId (string) -- The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    
    Note: this parameter is set to "-" bydefault if no value is not specified.
    
    vaultName (string) -- [REQUIRED]
    The name of the vault.
    
    
    """
    pass

def get_vault_notifications(accountId=None, vaultName=None):
    """
    This operation retrieves the notification-configuration subresource of the specified vault.
    For information about setting a notification configuration on a vault, see  SetVaultNotifications . If a notification configuration for a vault is not set, the operation returns a 404 Not Found error. For more information about vault notifications, see Configuring Vault Notifications in Amazon Glacier .
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Configuring Vault Notifications in Amazon Glacier and Get Vault Notification Configuration in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The example retrieves the notification-configuration for the vault named my-vault.
    Expected Output:
    
    :example: response = client.get_vault_notifications(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :rtype: dict
    :return: {
        'vaultNotificationConfig': {
            'SNSTopic': 'string',
            'Events': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def initiate_job(accountId=None, vaultName=None, jobParameters=None):
    """
    This operation initiates a job of the specified type. In this release, you can initiate a job to retrieve either an archive or a vault inventory (a list of archives in a vault).
    Retrieving data from Amazon Glacier is a two-step process:
    The retrieval request is executed asynchronously. When you initiate a retrieval job, Amazon Glacier creates a job and returns a job ID in the response. When Amazon Glacier completes the job, you can get the job output (archive or inventory data). For information about getting job output, see  GetJobOutput operation.
    The job must complete before you can get its output. To determine when a job is complete, you have the following options:
    If for a specific event, you add both the notification configuration on the vault and also specify an SNS topic in your initiate job request, Amazon Glacier sends both notifications. For more information, see  SetVaultNotifications .
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    Amazon Glacier prepares an inventory for each vault periodically, every 24 hours. When you initiate a job for a vault inventory, Amazon Glacier returns the last inventory for the vault. The inventory data you get might be up to a day or two days old. Also, the initiate inventory job might take some time to complete before you can download the vault inventory. So you do not want to retrieve a vault inventory for each vault operation. However, in some scenarios, you might find the vault inventory useful. For example, when you upload an archive, you can provide an archive description but not an archive name. Amazon Glacier provides you a unique archive ID, an opaque string of characters. So, you might maintain your own database that maps archive names to their corresponding Amazon Glacier assigned archive IDs. You might find the vault inventory useful in the event you need to reconcile information in your database with the actual vault inventory.
    You can limit the number of inventory items retrieved by filtering on the archive creation date or by setting a limit.
    You can retrieve inventory items for archives created between StartDate and EndDate by specifying values for these parameters in the InitiateJob request. Archives created on or after the StartDate and before the EndDate will be returned. If you only provide the StartDate without the EndDate , you will retrieve the inventory for all archives created on or after the StartDate . If you only provide the EndDate without the StartDate , you will get back the inventory for all archives created before the EndDate .
    You can limit the number of inventory items returned by setting the Limit parameter in the InitiateJob request. The inventory job output will contain inventory items up to the specified Limit . If there are more inventory items available, the result is paginated. After a job is complete you can use the  DescribeJob operation to get a marker that you use in a subsequent InitiateJob request. The marker will indicate the starting point to retrieve the next set of inventory items. You can page through your entire inventory by repeatedly making InitiateJob requests with the marker from the previous DescribeJob output, until you get a marker from DescribeJob that returns null, indicating that there are no more inventory items available.
    You can use the Limit parameter together with the date range parameters.
    You can initiate an archive retrieval for the whole archive or a range of the archive. In the case of ranged archive retrieval, you specify a byte range to return or the whole archive. The range specified must be megabyte (MB) aligned, that is the range start value must be divisible by 1 MB and range end value plus 1 must be divisible by 1 MB or equal the end of the archive. If the ranged archive retrieval is not megabyte aligned, this operation returns a 400 response. Furthermore, to ensure you get checksum values for data you download using Get Job Output API, the range must be tree hash aligned.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and the underlying REST API, see Initiate a Job and Downloading a Vault Inventory
    When retrieving an archive, you can specify one of the following options in the Tier field of the request body:
    For more information about expedited and bulk retrievals, see Retrieving Amazon Glacier Archives .
    See also: AWS API Documentation
    
    Examples
    The example initiates an inventory-retrieval job for the vault named examplevault.
    Expected Output:
    
    :example: response = client.initiate_job(
        vaultName='string',
        jobParameters={
            'Format': 'string',
            'Type': 'string',
            'ArchiveId': 'string',
            'Description': 'string',
            'SNSTopic': 'string',
            'RetrievalByteRange': 'string',
            'Tier': 'string',
            'InventoryRetrievalParameters': {
                'StartDate': 'string',
                'EndDate': 'string',
                'Limit': 'string',
                'Marker': 'string'
            }
        }
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type jobParameters: dict
    :param jobParameters: Provides options for specifying job information.
            Format (string) --When initiating a job to retrieve a vault inventory, you can optionally add this parameter to your request to specify the output format. If you are initiating an inventory job and do not specify a Format field, JSON is the default format. Valid values are 'CSV' and 'JSON'.
            Type (string) --The job type. You can initiate a job to retrieve an archive or get an inventory of a vault. Valid values are 'archive-retrieval' and 'inventory-retrieval'.
            ArchiveId (string) --The ID of the archive that you want to retrieve. This field is required only if Type is set to archive-retrieval. An error occurs if you specify this request parameter for an inventory retrieval job request.
            Description (string) --The optional description for the job. The description must be less than or equal to 1,024 bytes. The allowable characters are 7-bit ASCII without control codes-specifically, ASCII values 32-126 decimal or 0x20-0x7E hexadecimal.
            SNSTopic (string) --The Amazon SNS topic ARN to which Amazon Glacier sends a notification when the job is completed and the output is ready for you to download. The specified topic publishes the notification to its subscribers. The SNS topic must exist.
            RetrievalByteRange (string) --The byte range to retrieve for an archive retrieval. in the form 'StartByteValue -EndByteValue ' If not specified, the whole archive is retrieved. If specified, the byte range must be megabyte (1024*1024) aligned which means that StartByteValue must be divisible by 1 MB and EndByteValue plus 1 must be divisible by 1 MB or be the end of the archive specified as the archive byte size value minus 1. If RetrievalByteRange is not megabyte aligned, this operation returns a 400 response.
            An error occurs if you specify this field for an inventory retrieval job request.
            Tier (string) --The retrieval option to use for the archive retrieval. Valid values are Expedited , Standard , or Bulk . Standard is the default.
            InventoryRetrievalParameters (dict) --Input parameters used for range inventory retrieval.
            StartDate (string) --The start of the date range in UTC for vault inventory retrieval that includes archives created on or after this date. This value should be a string in the ISO 8601 date format, for example 2013-03-20T17:03:43Z .
            EndDate (string) --The end of the date range in UTC for vault inventory retrieval that includes archives created before this date. This value should be a string in the ISO 8601 date format, for example 2013-03-20T17:03:43Z .
            Limit (string) --Specifies the maximum number of inventory items returned per vault inventory retrieval request. Valid values are greater than or equal to 1.
            Marker (string) --An opaque string that represents where to continue pagination of the vault inventory retrieval results. You use the marker in a new InitiateJob request to obtain additional inventory items. If there are no more inventory items, this value is null .
            
            

    :rtype: dict
    :return: {
        'location': 'string',
        'jobId': 'string'
    }
    
    
    :returns: 
    After the job completes, download the bytes.
    
    """
    pass

def initiate_multipart_upload(accountId=None, vaultName=None, archiveDescription=None, partSize=None):
    """
    This operation initiates a multipart upload. Amazon Glacier creates a multipart upload resource and returns its ID in the response. The multipart upload ID is used in subsequent requests to upload parts of an archive (see  UploadMultipartPart ).
    When you initiate a multipart upload, you specify the part size in number of bytes. The part size must be a megabyte (1024 KB) multiplied by a power of 2-for example, 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB.
    Every part you upload to this resource (see  UploadMultipartPart ), except the last one, must have the same size. The last one can be the same size or smaller. For example, suppose you want to upload a 16.2 MB file. If you initiate the multipart upload with a part size of 4 MB, you will upload four parts of 4 MB each and one part of 0.2 MB.
    After you complete the multipart upload, Amazon Glacier removes the multipart upload resource referenced by the ID. Amazon Glacier also removes the multipart upload resource if you cancel the multipart upload or it may be removed if there is no activity for a period of 24 hours.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Uploading Large Archives in Parts (Multipart Upload) and Initiate Multipart Upload in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The example initiates a multipart upload to a vault named my-vault with a part size of 1 MiB (1024 x 1024 bytes) per file.
    Expected Output:
    
    :example: response = client.initiate_multipart_upload(
        vaultName='string',
        archiveDescription='string',
        partSize='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type archiveDescription: string
    :param archiveDescription: The archive description that you are uploading in parts.
            The part size must be a megabyte (1024 KB) multiplied by a power of 2, for example 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB (4096 MB).
            

    :type partSize: string
    :param partSize: The size of each part except the last, in bytes. The last part can be smaller than this part size.

    :rtype: dict
    :return: {
        'location': 'string',
        'uploadId': 'string'
    }
    
    
    """
    pass

def initiate_vault_lock(accountId=None, vaultName=None, policy=None):
    """
    This operation initiates the vault locking process by doing the following:
    You can set one vault lock policy for each vault and this policy can be up to 20 KB in size. For more information about vault lock policies, see Amazon Glacier Access Control with Vault Lock Policies .
    You must complete the vault locking process within 24 hours after the vault lock enters the InProgress state. After the 24 hour window ends, the lock ID expires, the vault automatically exits the InProgress state, and the vault lock policy is removed from the vault. You call  CompleteVaultLock to complete the vault locking process by setting the state of the vault lock to Locked .
    After a vault lock is in the Locked state, you cannot initiate a new vault lock for the vault.
    You can abort the vault locking process by calling  AbortVaultLock . You can get the state of the vault lock by calling  GetVaultLock . For more information about the vault locking process, Amazon Glacier Vault Lock .
    If this operation is called when the vault lock is in the InProgress state, the operation returns an AccessDeniedException error. When the vault lock is in the InProgress state you must call  AbortVaultLock before you can initiate a new vault lock policy.
    See also: AWS API Documentation
    
    Examples
    The example initiates the vault locking process for the vault named my-vault.
    Expected Output:
    
    :example: response = client.initiate_vault_lock(
        vaultName='string',
        policy={
            'Policy': 'string'
        }
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type policy: dict
    :param policy: The vault lock policy as a JSON string, which uses '' as an escape character.
            Policy (string) --The vault lock policy.
            

    :rtype: dict
    :return: {
        'lockId': 'string'
    }
    
    
    :returns: 
    accountId (string) -- The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
    
    Note: this parameter is set to "-" bydefault if no value is not specified.
    
    vaultName (string) -- [REQUIRED]
    The name of the vault.
    
    policy (dict) -- The vault lock policy as a JSON string, which uses "" as an escape character.
    
    Policy (string) --The vault lock policy.
    
    
    
    
    """
    pass

def list_jobs(accountId=None, vaultName=None, limit=None, marker=None, statuscode=None, completed=None):
    """
    This operation lists jobs for a vault, including jobs that are in-progress and jobs that have recently finished.
    To retrieve an archive or retrieve a vault inventory from Amazon Glacier, you first initiate a job, and after the job completes, you download the data. For an archive retrieval, the output is the archive data. For an inventory retrieval, it is the inventory list. The List Job operation returns a list of these jobs sorted by job initiation time.
    The List Jobs operation supports pagination. You should always check the response Marker field. If there are no more jobs to list, the Marker field is set to null . If there are more jobs to list, the Marker field is set to a non-null value, which you can use to continue the pagination of the list. To return a list of jobs that begins at a specific job, set the marker request parameter to the Marker value for that job that you obtained from a previous List Jobs request.
    You can set a maximum limit for the number of jobs returned in the response by specifying the limit parameter in the request. The default limit is 1000. The number of jobs returned might be fewer than the limit, but the number of returned jobs never exceeds the limit.
    Additionally, you can filter the jobs list returned by specifying the optional statuscode parameter or completed parameter, or both. Using the statuscode parameter, you can specify to return only jobs that match either the InProgress , Succeeded , or Failed status. Using the completed parameter, you can specify to return only jobs that were completed (true ) or jobs that were not completed (false ).
    For the underlying REST API, see List Jobs .
    See also: AWS API Documentation
    
    Examples
    The example lists jobs for the vault named my-vault.
    Expected Output:
    
    :example: response = client.list_jobs(
        vaultName='string',
        limit='string',
        marker='string',
        statuscode='string',
        completed='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type limit: string
    :param limit: The maximum number of jobs to be returned. The default limit is 1000. The number of jobs returned might be fewer than the specified limit, but the number of returned jobs never exceeds the limit.

    :type marker: string
    :param marker: An opaque string used for pagination. This value specifies the job at which the listing of jobs should begin. Get the marker value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of results started in a previous List Jobs request.

    :type statuscode: string
    :param statuscode: The type of job status to return. You can specify the following values: InProgress , Succeeded , or Failed .

    :type completed: string
    :param completed: The state of the jobs to return. You can specify true or false .

    :rtype: dict
    :return: {
        'JobList': [
            {
                'JobId': 'string',
                'JobDescription': 'string',
                'Action': 'ArchiveRetrieval'|'InventoryRetrieval',
                'ArchiveId': 'string',
                'VaultARN': 'string',
                'CreationDate': 'string',
                'Completed': True|False,
                'StatusCode': 'InProgress'|'Succeeded'|'Failed',
                'StatusMessage': 'string',
                'ArchiveSizeInBytes': 123,
                'InventorySizeInBytes': 123,
                'SNSTopic': 'string',
                'CompletionDate': 'string',
                'SHA256TreeHash': 'string',
                'ArchiveSHA256TreeHash': 'string',
                'RetrievalByteRange': 'string',
                'Tier': 'string',
                'InventoryRetrievalParameters': {
                    'Format': 'string',
                    'StartDate': 'string',
                    'EndDate': 'string',
                    'Limit': 'string',
                    'Marker': 'string'
                }
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    Archive retrieval jobs that specify a range that is not tree-hash aligned.
    Archival jobs that specify a range that is equal to the whole archive and the job status is InProgress.
    Inventory jobs.
    
    """
    pass

def list_multipart_uploads(accountId=None, vaultName=None, marker=None, limit=None):
    """
    This operation lists in-progress multipart uploads for the specified vault. An in-progress multipart upload is a multipart upload that has been initiated by an  InitiateMultipartUpload request, but has not yet been completed or aborted. The list returned in the List Multipart Upload response has no guaranteed order.
    The List Multipart Uploads operation supports pagination. By default, this operation returns up to 1,000 multipart uploads in the response. You should always check the response for a marker at which to continue the list; if there are no more items the marker is null . To return a list of multipart uploads that begins at a specific upload, set the marker request parameter to the value you obtained from a previous List Multipart Upload request. You can also limit the number of uploads returned in the response by specifying the limit parameter in the request.
    Note the difference between this operation and listing parts ( ListParts ). The List Multipart Uploads operation lists all multipart uploads for a vault and does not require a multipart upload ID. The List Parts operation requires a multipart upload ID since parts are associated with a single upload.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and the underlying REST API, see Working with Archives in Amazon Glacier and List Multipart Uploads in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The example lists all the in-progress multipart uploads for the vault named examplevault.
    Expected Output:
    
    :example: response = client.list_multipart_uploads(
        vaultName='string',
        marker='string',
        limit='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type marker: string
    :param marker: An opaque string used for pagination. This value specifies the upload at which the listing of uploads should begin. Get the marker value from a previous List Uploads response. You need only include the marker if you are continuing the pagination of results started in a previous List Uploads request.

    :type limit: string
    :param limit: Specifies the maximum number of uploads returned in the response body. If this value is not specified, the List Uploads operation returns up to 1,000 uploads.

    :rtype: dict
    :return: {
        'UploadsList': [
            {
                'MultipartUploadId': 'string',
                'VaultARN': 'string',
                'ArchiveDescription': 'string',
                'PartSizeInBytes': 123,
                'CreationDate': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def list_parts(accountId=None, vaultName=None, uploadId=None, marker=None, limit=None):
    """
    This operation lists the parts of an archive that have been uploaded in a specific multipart upload. You can make this request at any time during an in-progress multipart upload before you complete the upload (see  CompleteMultipartUpload . List Parts returns an error for completed uploads. The list returned in the List Parts response is sorted by part range.
    The List Parts operation supports pagination. By default, this operation returns up to 1,000 uploaded parts in the response. You should always check the response for a marker at which to continue the list; if there are no more items the marker is null . To return a list of parts that begins at a specific part, set the marker request parameter to the value you obtained from a previous List Parts request. You can also limit the number of parts returned in the response by specifying the limit parameter in the request.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and the underlying REST API, see Working with Archives in Amazon Glacier and List Parts in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The example lists all the parts of a multipart upload.
    Expected Output:
    
    :example: response = client.list_parts(
        vaultName='string',
        uploadId='string',
        marker='string',
        limit='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type uploadId: string
    :param uploadId: [REQUIRED]
            The upload ID of the multipart upload.
            

    :type marker: string
    :param marker: An opaque string used for pagination. This value specifies the part at which the listing of parts should begin. Get the marker value from the response of a previous List Parts response. You need only include the marker if you are continuing the pagination of results started in a previous List Parts request.

    :type limit: string
    :param limit: The maximum number of parts to be returned. The default limit is 1000. The number of parts returned might be fewer than the specified limit, but the number of returned parts never exceeds the limit.

    :rtype: dict
    :return: {
        'MultipartUploadId': 'string',
        'VaultARN': 'string',
        'ArchiveDescription': 'string',
        'PartSizeInBytes': 123,
        'CreationDate': 'string',
        'Parts': [
            {
                'RangeInBytes': 'string',
                'SHA256TreeHash': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def list_provisioned_capacity(accountId=None):
    """
    This operation lists the provisioned capacity for the specified AWS account.
    See also: AWS API Documentation
    
    Examples
    The example lists the provisioned capacity units for an account.
    Expected Output:
    
    :example: response = client.list_provisioned_capacity(
    
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '-' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, don't include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :rtype: dict
    :return: {
        'ProvisionedCapacityList': [
            {
                'CapacityId': 'string',
                'StartDate': 'string',
                'ExpirationDate': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_tags_for_vault(accountId=None, vaultName=None):
    """
    This operation lists all the tags attached to a vault. The operation returns an empty map if there are no tags. For more information about tags, see Tagging Amazon Glacier Resources .
    See also: AWS API Documentation
    
    Examples
    The example lists all the tags attached to the vault examplevault.
    Expected Output:
    
    :example: response = client.list_tags_for_vault(
        vaultName='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :rtype: dict
    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_vaults(accountId=None, marker=None, limit=None):
    """
    This operation lists all vaults owned by the calling user's account. The list returned in the response is ASCII-sorted by vault name.
    By default, this operation returns up to 1,000 items. If there are more vaults to list, the response marker field contains the vault Amazon Resource Name (ARN) at which to continue the list with a new List Vaults request; otherwise, the marker field is null . To return a list of vaults that begins at a specific vault, set the marker request parameter to the vault ARN you obtained from a previous List Vaults request. You can also limit the number of vaults returned in the response by specifying the limit parameter in the request.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Retrieving Vault Metadata in Amazon Glacier and List Vaults in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The example lists all vaults owned by the specified AWS account.
    Expected Output:
    
    :example: response = client.list_vaults(
        marker='string',
        limit='string'
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type marker: string
    :param marker: A string used for pagination. The marker specifies the vault ARN after which the listing of vaults should begin.

    :type limit: string
    :param limit: The maximum number of vaults to be returned. The default limit is 1000. The number of vaults returned might be fewer than the specified limit, but the number of returned vaults never exceeds the limit.

    :rtype: dict
    :return: {
        'VaultList': [
            {
                'VaultARN': 'string',
                'VaultName': 'string',
                'CreationDate': 'string',
                'LastInventoryDate': 'string',
                'NumberOfArchives': 123,
                'SizeInBytes': 123
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def purchase_provisioned_capacity(accountId=None):
    """
    This operation purchases a provisioned capacity unit for an AWS account.
    See also: AWS API Documentation
    
    Examples
    The example purchases provisioned capacity unit for an AWS account.
    Expected Output:
    
    :example: response = client.purchase_provisioned_capacity(
    
    )
    
    
    :type accountId: string
    :param accountId: The AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '-' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, don't include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :rtype: dict
    :return: {
        'capacityId': 'string'
    }
    
    
    """
    pass

def remove_tags_from_vault(accountId=None, vaultName=None, TagKeys=None):
    """
    This operation removes one or more tags from the set of tags attached to a vault. For more information about tags, see Tagging Amazon Glacier Resources . This operation is idempotent. The operation will be successful, even if there are no tags attached to the vault.
    See also: AWS API Documentation
    
    Examples
    The example removes two tags from the vault named examplevault.
    Expected Output:
    
    :example: response = client.remove_tags_from_vault(
        vaultName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type TagKeys: list
    :param TagKeys: A list of tag keys. Each corresponding tag is removed from the vault.
            (string) --
            

    :return: response = client.remove_tags_from_vault(
        TagKeys=[
            'examplekey1',
            'examplekey2',
        ],
        accountId='-',
        vaultName='examplevault',
    )
    
    print(response)
    
    
    """
    pass

def set_data_retrieval_policy(accountId=None, Policy=None):
    """
    This operation sets and then enacts a data retrieval policy in the region specified in the PUT request. You can set one policy per region for an AWS account. The policy is enacted within a few minutes of a successful PUT operation.
    The set policy operation does not affect retrieval jobs that were in progress before the policy was enacted. For more information about data retrieval policies, see Amazon Glacier Data Retrieval Policies .
    See also: AWS API Documentation
    
    Examples
    The example sets and then enacts a data retrieval policy.
    Expected Output:
    
    :example: response = client.set_data_retrieval_policy(
        Policy={
            'Rules': [
                {
                    'Strategy': 'string',
                    'BytesPerHour': 123
                },
            ]
        }
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type Policy: dict
    :param Policy: The data retrieval policy in JSON format.
            Rules (list) --The policy rule. Although this is a list type, currently there must be only one rule, which contains a Strategy field and optionally a BytesPerHour field.
            (dict) --Data retrieval policy rule.
            Strategy (string) --The type of data retrieval policy to set.
            Valid values: BytesPerHour|FreeTier|None
            BytesPerHour (integer) --The maximum number of bytes that can be retrieved in an hour.
            This field is required only if the value of the Strategy field is BytesPerHour . Your PUT operation will be rejected if the Strategy field is not set to BytesPerHour and you set this field.
            
            

    :return: response = client.set_data_retrieval_policy(
        Policy={
            'Rules': [
                {
                    'BytesPerHour': 10737418240,
                    'Strategy': 'BytesPerHour',
                },
            ],
        },
        accountId='-',
    )
    
    print(response)
    
    
    """
    pass

def set_vault_access_policy(accountId=None, vaultName=None, policy=None):
    """
    This operation configures an access policy for a vault and will overwrite an existing policy. To configure a vault access policy, send a PUT request to the access-policy subresource of the vault. An access policy is specific to a vault and is also called a vault subresource. You can set one access policy per vault and the policy can be up to 20 KB in size. For more information about vault access policies, see Amazon Glacier Access Control with Vault Access Policies .
    See also: AWS API Documentation
    
    Examples
    The example configures an access policy for the vault named examplevault.
    Expected Output:
    
    :example: response = client.set_vault_access_policy(
        vaultName='string',
        policy={
            'Policy': 'string'
        }
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type policy: dict
    :param policy: The vault access policy as a JSON string.
            Policy (string) --The vault access policy.
            

    :return: response = client.set_vault_access_policy(
        accountId='-',
        policy={
            'Policy': '{"Version":"2012-10-17","Statement":[{"Sid":"Define-owner-access-rights","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::999999999999:root"},"Action":"glacier:DeleteArchive","Resource":"arn:aws:glacier:us-west-2:999999999999:vaults/examplevault"}]}',
        },
        vaultName='examplevault',
    )
    
    print(response)
    
    
    """
    pass

def set_vault_notifications(accountId=None, vaultName=None, vaultNotificationConfig=None):
    """
    This operation configures notifications that will be sent when specific events happen to a vault. By default, you don't get any notifications.
    To configure vault notifications, send a PUT request to the notification-configuration subresource of the vault. The request should include a JSON document that provides an Amazon SNS topic and specific events for which you want Amazon Glacier to send notifications to the topic.
    Amazon SNS topics must grant permission to the vault to be allowed to publish notifications to the topic. You can configure a vault to publish a notification for the following vault events:
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Configuring Vault Notifications in Amazon Glacier and Set Vault Notification Configuration in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The example sets the examplevault notification configuration.
    Expected Output:
    
    :example: response = client.set_vault_notifications(
        vaultName='string',
        vaultNotificationConfig={
            'SNSTopic': 'string',
            'Events': [
                'string',
            ]
        }
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type vaultNotificationConfig: dict
    :param vaultNotificationConfig: Provides options for specifying notification configuration.
            SNSTopic (string) --The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).
            Events (list) --A list of one or more events for which Amazon Glacier will send a notification to the specified Amazon SNS topic.
            (string) --
            

    :return: response = client.set_vault_notifications(
        accountId='-',
        vaultName='examplevault',
        vaultNotificationConfig={
            'Events': [
                'ArchiveRetrievalCompleted',
                'InventoryRetrievalCompleted',
            ],
            'SNSTopic': 'arn:aws:sns:us-west-2:012345678901:mytopic',
        },
    )
    
    print(response)
    
    
    :returns: 
    accountId (string) -- The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
    
    Note: this parameter is set to "-" bydefault if no value is not specified.
    
    vaultName (string) -- [REQUIRED]
    The name of the vault.
    
    vaultNotificationConfig (dict) -- Provides options for specifying notification configuration.
    
    SNSTopic (string) --The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).
    
    Events (list) --A list of one or more events for which Amazon Glacier will send a notification to the specified Amazon SNS topic.
    
    (string) --
    
    
    
    
    
    """
    pass

def upload_archive(vaultName=None, accountId=None, archiveDescription=None, checksum=None, body=None):
    """
    This operation adds an archive to a vault. This is a synchronous operation, and for a successful upload, your data is durably persisted. Amazon Glacier returns the archive ID in the x-amz-archive-id header of the response.
    You must use the archive ID to access your data in Amazon Glacier. After you upload an archive, you should save the archive ID returned so that you can retrieve or delete the archive later. Besides saving the archive ID, you can also index it and give it a friendly name to allow for better searching. You can also use the optional archive description field to specify how the archive is referred to in an external index of archives, such as you might create in Amazon DynamoDB. You can also get the vault inventory to obtain a list of archive IDs in a vault. For more information, see  InitiateJob .
    You must provide a SHA256 tree hash of the data you are uploading. For information about computing a SHA256 tree hash, see Computing Checksums .
    You can optionally specify an archive description of up to 1,024 printable ASCII characters. You can get the archive description when you either retrieve the archive or get the vault inventory. For more information, see  InitiateJob . Amazon Glacier does not interpret the description in any way. An archive description does not need to be unique. You cannot use the description to retrieve or sort the archive list.
    Archives are immutable. After you upload an archive, you cannot edit the archive or its description.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Uploading an Archive in Amazon Glacier and Upload Archive in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The example adds an archive to a vault.
    Expected Output:
    
    :example: response = client.upload_archive(
        vaultName='string',
        archiveDescription='string',
        body=b'bytes'|file
    )
    
    
    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type archiveDescription: string
    :param archiveDescription: The optional description of the archive you are uploading.

    :type checksum: string
    :param checksum: The SHA256 tree hash of the data being uploaded.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
            

    :type body: bytes or seekable file-like object
    :param body: The data to upload.

    :rtype: dict
    :return: {
        'location': 'string',
        'checksum': 'string',
        'archiveId': 'string'
    }
    
    
    """
    pass

def upload_multipart_part(accountId=None, vaultName=None, uploadId=None, checksum=None, range=None, body=None):
    """
    This operation uploads a part of an archive. You can upload archive parts in any order. You can also upload them in parallel. You can upload up to 10,000 parts for a multipart upload.
    Amazon Glacier rejects your upload part request if any of the following conditions is true:
    This operation is idempotent. If you upload the same part multiple times, the data included in the most recent request overwrites the previously uploaded data.
    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see Access Control Using AWS Identity and Access Management (IAM) .
    For conceptual information and underlying REST API, see Uploading Large Archives in Parts (Multipart Upload) and Upload Part in the Amazon Glacier Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The example uploads the first 1 MiB (1024 x 1024 bytes) part of an archive.
    Expected Output:
    
    :example: response = client.upload_multipart_part(
        vaultName='string',
        uploadId='string',
        range='string',
        body=b'bytes'|file
    )
    
    
    :type accountId: string
    :param accountId: The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '- ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.
            Note: this parameter is set to '-' bydefault if no value is not specified.
            

    :type vaultName: string
    :param vaultName: [REQUIRED]
            The name of the vault.
            

    :type uploadId: string
    :param uploadId: [REQUIRED]
            The upload ID of the multipart upload.
            

    :type checksum: string
    :param checksum: The SHA256 tree hash of the data being uploaded.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
            

    :type range: string
    :param range: Identifies the range of bytes in the assembled archive that will be uploaded in this part. Amazon Glacier uses this information to assemble the archive in the proper sequence. The format of this header follows RFC 2616. An example header is Content-Range:bytes 0-4194303/*.

    :type body: bytes or seekable file-like object
    :param body: The data to upload.

    :rtype: dict
    :return: {
        'checksum': 'string'
    }
    
    
    :returns: 
    Range does not align The byte range value in the request does not align with the part size specified in the corresponding initiate request. For example, if you specify a part size of 4194304 bytes (4 MB), then 0 to 4194303 bytes (4 MB - 1) and 4194304 (4 MB) to 8388607 (8 MB - 1) are valid part ranges. However, if you set a range value of 2 MB to 6 MB, the range does not align with the part size and the upload will fail.
    
    """
    pass

