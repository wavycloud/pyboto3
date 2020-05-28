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

def create_backup_plan(BackupPlan=None, BackupPlanTags=None, CreatorRequestId=None):
    """
    Backup plans are documents that contain information that AWS Backup uses to schedule tasks that create recovery points of resources.
    If you call CreateBackupPlan with a plan that already exists, an AlreadyExistsException is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_backup_plan(
        BackupPlan={
            'BackupPlanName': 'string',
            'Rules': [
                {
                    'RuleName': 'string',
                    'TargetBackupVaultName': 'string',
                    'ScheduleExpression': 'string',
                    'StartWindowMinutes': 123,
                    'CompletionWindowMinutes': 123,
                    'Lifecycle': {
                        'MoveToColdStorageAfterDays': 123,
                        'DeleteAfterDays': 123
                    },
                    'RecoveryPointTags': {
                        'string': 'string'
                    },
                    'CopyActions': [
                        {
                            'Lifecycle': {
                                'MoveToColdStorageAfterDays': 123,
                                'DeleteAfterDays': 123
                            },
                            'DestinationBackupVaultArn': 'string'
                        },
                    ]
                },
            ]
        },
        BackupPlanTags={
            'string': 'string'
        },
        CreatorRequestId='string'
    )
    
    
    :type BackupPlan: dict
    :param BackupPlan: [REQUIRED]\nSpecifies the body of a backup plan. Includes a BackupPlanName and one or more sets of Rules .\n\nBackupPlanName (string) -- [REQUIRED]The display name of a backup plan.\n\nRules (list) -- [REQUIRED]An array of BackupRule objects, each of which specifies a scheduled task that is used to back up a selection of resources.\n\n(dict) --Specifies a scheduled task used to back up a selection of resources.\n\nRuleName (string) -- [REQUIRED]An optional display name for a backup rule.\n\nTargetBackupVaultName (string) -- [REQUIRED]The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n\nScheduleExpression (string) --A CRON expression specifying when AWS Backup initiates a backup job.\n\nStartWindowMinutes (integer) --A value in minutes after a backup is scheduled before a job will be canceled if it doesn\'t start successfully. This value is optional.\n\nCompletionWindowMinutes (integer) --A value in minutes after a backup job is successfully started before it must be completed or it will be canceled by AWS Backup. This value is optional.\n\nLifecycle (dict) --The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup will transition and expire backups automatically according to the lifecycle that you define.\nBackups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.\n\nMoveToColdStorageAfterDays (integer) --Specifies the number of days after creation that a recovery point is moved to cold storage.\n\nDeleteAfterDays (integer) --Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .\n\n\n\nRecoveryPointTags (dict) --To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair.\n\n(string) --\n(string) --\n\n\n\n\nCopyActions (list) --An array of CopyAction objects, which contains the details of the copy operation.\n\n(dict) --The details of the copy operation.\n\nLifecycle (dict) --Contains an array of Transition objects specifying how long in days before a recovery point transitions to cold storage or is deleted.\nBackups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, on the console, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.\n\nMoveToColdStorageAfterDays (integer) --Specifies the number of days after creation that a recovery point is moved to cold storage.\n\nDeleteAfterDays (integer) --Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .\n\n\n\nDestinationBackupVaultArn (string) -- [REQUIRED]An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup. For example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .\n\n\n\n\n\n\n\n\n\n\n

    :type BackupPlanTags: dict
    :param BackupPlanTags: To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair. The specified tags are assigned to all backups created with this plan.\n\n(string) --\n(string) --\n\n\n\n

    :type CreatorRequestId: string
    :param CreatorRequestId: Identifies the request and allows failed requests to be retried without the risk of executing the operation twice. If the request includes a CreatorRequestId that matches an existing backup plan, that plan is returned. This parameter is optional.

    :rtype: dict

ReturnsResponse Syntax
{
    'BackupPlanId': 'string',
    'BackupPlanArn': 'string',
    'CreationDate': datetime(2015, 1, 1),
    'VersionId': 'string'
}


Response Structure

(dict) --

BackupPlanId (string) --
Uniquely identifies a backup plan.

BackupPlanArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50 .

CreationDate (datetime) --
The date and time that a backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

VersionId (string) --
Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.







Exceptions

Backup.Client.exceptions.LimitExceededException
Backup.Client.exceptions.AlreadyExistsException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'BackupPlanId': 'string',
        'BackupPlanArn': 'string',
        'CreationDate': datetime(2015, 1, 1),
        'VersionId': 'string'
    }
    
    
    :returns: 
    Backup.Client.exceptions.LimitExceededException
    Backup.Client.exceptions.AlreadyExistsException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def create_backup_selection(BackupPlanId=None, BackupSelection=None, CreatorRequestId=None):
    """
    Creates a JSON document that specifies a set of resources to assign to a backup plan. Resources can be included by specifying patterns for a ListOfTags and selected Resources .
    For example, consider the following patterns:
    Using these patterns would back up all Amazon Elastic Block Store (Amazon EBS) volumes that are tagged as "department=finance" , "importance=critical" , in addition to an EBS volume with the specified volume Id.
    Resources and conditions are additive in that all resources that match the pattern are selected. This shouldn\'t be confused with a logical AND, where all conditions must match. The matching patterns are logically \'put together using the OR operator. In other words, all patterns that match are selected for backup.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_backup_selection(
        BackupPlanId='string',
        BackupSelection={
            'SelectionName': 'string',
            'IamRoleArn': 'string',
            'Resources': [
                'string',
            ],
            'ListOfTags': [
                {
                    'ConditionType': 'STRINGEQUALS',
                    'ConditionKey': 'string',
                    'ConditionValue': 'string'
                },
            ]
        },
        CreatorRequestId='string'
    )
    
    
    :type BackupPlanId: string
    :param BackupPlanId: [REQUIRED]\nUniquely identifies the backup plan to be associated with the selection of resources.\n

    :type BackupSelection: dict
    :param BackupSelection: [REQUIRED]\nSpecifies the body of a request to assign a set of resources to a backup plan.\n\nSelectionName (string) -- [REQUIRED]The display name of a resource selection document.\n\nIamRoleArn (string) -- [REQUIRED]The ARN of the IAM role that AWS Backup uses to authenticate when restoring the target resource; for example, arn:aws:iam::123456789012:role/S3Access .\n\nResources (list) --An array of strings that contain Amazon Resource Names (ARNs) of resources to assign to a backup plan.\n\n(string) --\n\n\nListOfTags (list) --An array of conditions used to specify a set of resources to assign to a backup plan; for example, 'STRINGEQUALS': {'ec2:ResourceTag/Department': 'accounting' .\n\n(dict) --Contains an array of triplets made up of a condition type (such as STRINGEQUALS ), a key, and a value. Conditions are used to filter resources in a selection that is assigned to a backup plan.\n\nConditionType (string) -- [REQUIRED]An operation, such as STRINGEQUALS , that is applied to a key-value pair used to filter resources in a selection.\n\nConditionKey (string) -- [REQUIRED]The key in a key-value pair. For example, in 'ec2:ResourceTag/Department': 'accounting' , 'ec2:ResourceTag/Department' is the key.\n\nConditionValue (string) -- [REQUIRED]The value in a key-value pair. For example, in 'ec2:ResourceTag/Department': 'accounting' , 'accounting' is the value.\n\n\n\n\n\n\n

    :type CreatorRequestId: string
    :param CreatorRequestId: A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.

    :rtype: dict

ReturnsResponse Syntax
{
    'SelectionId': 'string',
    'BackupPlanId': 'string',
    'CreationDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

SelectionId (string) --
Uniquely identifies the body of a request to assign a set of resources to a backup plan.

BackupPlanId (string) --
Uniquely identifies a backup plan.

CreationDate (datetime) --
The date and time a backup selection is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.







Exceptions

Backup.Client.exceptions.LimitExceededException
Backup.Client.exceptions.AlreadyExistsException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'SelectionId': 'string',
        'BackupPlanId': 'string',
        'CreationDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    BackupPlanId (string) -- [REQUIRED]
    Uniquely identifies the backup plan to be associated with the selection of resources.
    
    BackupSelection (dict) -- [REQUIRED]
    Specifies the body of a request to assign a set of resources to a backup plan.
    
    SelectionName (string) -- [REQUIRED]The display name of a resource selection document.
    
    IamRoleArn (string) -- [REQUIRED]The ARN of the IAM role that AWS Backup uses to authenticate when restoring the target resource; for example, arn:aws:iam::123456789012:role/S3Access .
    
    Resources (list) --An array of strings that contain Amazon Resource Names (ARNs) of resources to assign to a backup plan.
    
    (string) --
    
    
    ListOfTags (list) --An array of conditions used to specify a set of resources to assign to a backup plan; for example, "STRINGEQUALS": {"ec2:ResourceTag/Department": "accounting" .
    
    (dict) --Contains an array of triplets made up of a condition type (such as STRINGEQUALS ), a key, and a value. Conditions are used to filter resources in a selection that is assigned to a backup plan.
    
    ConditionType (string) -- [REQUIRED]An operation, such as STRINGEQUALS , that is applied to a key-value pair used to filter resources in a selection.
    
    ConditionKey (string) -- [REQUIRED]The key in a key-value pair. For example, in "ec2:ResourceTag/Department": "accounting" , "ec2:ResourceTag/Department" is the key.
    
    ConditionValue (string) -- [REQUIRED]The value in a key-value pair. For example, in "ec2:ResourceTag/Department": "accounting" , "accounting" is the value.
    
    
    
    
    
    
    
    CreatorRequestId (string) -- A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.
    
    """
    pass

def create_backup_vault(BackupVaultName=None, BackupVaultTags=None, EncryptionKeyArn=None, CreatorRequestId=None):
    """
    Creates a logical container where backups are stored. A CreateBackupVault request includes a name, optionally one or more resource tags, an encryption key, and a request ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_backup_vault(
        BackupVaultName='string',
        BackupVaultTags={
            'string': 'string'
        },
        EncryptionKeyArn='string',
        CreatorRequestId='string'
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    :type BackupVaultTags: dict
    :param BackupVaultTags: Metadata that you can assign to help organize the resources that you create. Each tag is a key-value pair.\n\n(string) --\n(string) --\n\n\n\n

    :type EncryptionKeyArn: string
    :param EncryptionKeyArn: The server-side encryption key that is used to protect your backups; for example, arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab .

    :type CreatorRequestId: string
    :param CreatorRequestId: A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.

    :rtype: dict

ReturnsResponse Syntax
{
    'BackupVaultName': 'string',
    'BackupVaultArn': 'string',
    'CreationDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

BackupVaultName (string) --
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.

BackupVaultArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

CreationDate (datetime) --
The date and time a backup vault is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.







Exceptions

Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException
Backup.Client.exceptions.LimitExceededException
Backup.Client.exceptions.AlreadyExistsException


    :return: {
        'BackupVaultName': 'string',
        'BackupVaultArn': 'string',
        'CreationDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    Backup.Client.exceptions.LimitExceededException
    Backup.Client.exceptions.AlreadyExistsException
    
    """
    pass

def delete_backup_plan(BackupPlanId=None):
    """
    Deletes a backup plan. A backup plan can only be deleted after all associated selections of resources have been deleted. Deleting a backup plan deletes the current version of a backup plan. Previous versions, if any, will still exist.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_backup_plan(
        BackupPlanId='string'
    )
    
    
    :type BackupPlanId: string
    :param BackupPlanId: [REQUIRED]\nUniquely identifies a backup plan.\n

    :rtype: dict
ReturnsResponse Syntax{
    'BackupPlanId': 'string',
    'BackupPlanArn': 'string',
    'DeletionDate': datetime(2015, 1, 1),
    'VersionId': 'string'
}


Response Structure

(dict) --
BackupPlanId (string) --Uniquely identifies a backup plan.

BackupPlanArn (string) --An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50 .

DeletionDate (datetime) --The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

VersionId (string) --Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version Ids cannot be edited.






Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException
Backup.Client.exceptions.InvalidRequestException


    :return: {
        'BackupPlanId': 'string',
        'BackupPlanArn': 'string',
        'DeletionDate': datetime(2015, 1, 1),
        'VersionId': 'string'
    }
    
    
    """
    pass

def delete_backup_selection(BackupPlanId=None, SelectionId=None):
    """
    Deletes the resource selection associated with a backup plan that is specified by the SelectionId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_backup_selection(
        BackupPlanId='string',
        SelectionId='string'
    )
    
    
    :type BackupPlanId: string
    :param BackupPlanId: [REQUIRED]\nUniquely identifies a backup plan.\n

    :type SelectionId: string
    :param SelectionId: [REQUIRED]\nUniquely identifies the body of a request to assign a set of resources to a backup plan.\n

    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def delete_backup_vault(BackupVaultName=None):
    """
    Deletes the backup vault identified by its name. A vault can be deleted only if it is empty.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_backup_vault(
        BackupVaultName='string'
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    """
    pass

def delete_backup_vault_access_policy(BackupVaultName=None):
    """
    Deletes the policy document that manages permissions on a backup vault.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_backup_vault_access_policy(
        BackupVaultName='string'
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    """
    pass

def delete_backup_vault_notifications(BackupVaultName=None):
    """
    Deletes event notifications for the specified backup vault.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_backup_vault_notifications(
        BackupVaultName='string'
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    """
    pass

def delete_recovery_point(BackupVaultName=None, RecoveryPointArn=None):
    """
    Deletes the recovery point specified by a recovery point ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_recovery_point(
        BackupVaultName='string',
        RecoveryPointArn='string'
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    :type RecoveryPointArn: string
    :param RecoveryPointArn: [REQUIRED]\nAn Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .\n

    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    Backup.Client.exceptions.InvalidRequestException
    
    """
    pass

def describe_backup_job(BackupJobId=None):
    """
    Returns metadata associated with creating a backup of a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_backup_job(
        BackupJobId='string'
    )
    
    
    :type BackupJobId: string
    :param BackupJobId: [REQUIRED]\nUniquely identifies a request to AWS Backup to back up a resource.\n

    :rtype: dict
ReturnsResponse Syntax{
    'BackupJobId': 'string',
    'BackupVaultName': 'string',
    'BackupVaultArn': 'string',
    'RecoveryPointArn': 'string',
    'ResourceArn': 'string',
    'CreationDate': datetime(2015, 1, 1),
    'CompletionDate': datetime(2015, 1, 1),
    'State': 'CREATED'|'PENDING'|'RUNNING'|'ABORTING'|'ABORTED'|'COMPLETED'|'FAILED'|'EXPIRED',
    'StatusMessage': 'string',
    'PercentDone': 'string',
    'BackupSizeInBytes': 123,
    'IamRoleArn': 'string',
    'CreatedBy': {
        'BackupPlanId': 'string',
        'BackupPlanArn': 'string',
        'BackupPlanVersion': 'string',
        'BackupRuleId': 'string'
    },
    'ResourceType': 'string',
    'BytesTransferred': 123,
    'ExpectedCompletionDate': datetime(2015, 1, 1),
    'StartBy': datetime(2015, 1, 1)
}


Response Structure

(dict) --
BackupJobId (string) --Uniquely identifies a request to AWS Backup to back up a resource.

BackupVaultName (string) --The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.

BackupVaultArn (string) --An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

RecoveryPointArn (string) --An ARN that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .

ResourceArn (string) --An ARN that uniquely identifies a saved resource. The format of the ARN depends on the resource type.

CreationDate (datetime) --The date and time that a backup job is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CompletionDate (datetime) --The date and time that a job to create a backup job is completed, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

State (string) --The current state of a resource recovery point.

StatusMessage (string) --A detailed message explaining the status of the job to back up a resource.

PercentDone (string) --Contains an estimated percentage that is complete of a job at the time the job status was queried.

BackupSizeInBytes (integer) --The size, in bytes, of a backup.

IamRoleArn (string) --Specifies the IAM role ARN used to create the target recovery point; for example, arn:aws:iam::123456789012:role/S3Access .

CreatedBy (dict) --Contains identifying information about the creation of a backup job, including the BackupPlanArn , BackupPlanId , BackupPlanVersion , and BackupRuleId of the backup plan that is used to create it.

BackupPlanId (string) --Uniquely identifies a backup plan.

BackupPlanArn (string) --An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50 .

BackupPlanVersion (string) --Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.

BackupRuleId (string) --Uniquely identifies a rule used to schedule the backup of a selection of resources.



ResourceType (string) --The type of AWS resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

BytesTransferred (integer) --The size in bytes transferred to a backup vault at the time that the job status was queried.

ExpectedCompletionDate (datetime) --The date and time that a job to back up resources is expected to be completed, in Unix format and Coordinated Universal Time (UTC). The value of ExpectedCompletionDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

StartBy (datetime) --Specifies the time in Unix format and Coordinated Universal Time (UTC) when a backup job must be started before it is canceled. The value is calculated by adding the start window to the scheduled time. So if the scheduled time were 6:00 PM and the start window is 2 hours, the StartBy time would be 8:00 PM on the date specified. The value of StartBy is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.






Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException
Backup.Client.exceptions.DependencyFailureException


    :return: {
        'BackupJobId': 'string',
        'BackupVaultName': 'string',
        'BackupVaultArn': 'string',
        'RecoveryPointArn': 'string',
        'ResourceArn': 'string',
        'CreationDate': datetime(2015, 1, 1),
        'CompletionDate': datetime(2015, 1, 1),
        'State': 'CREATED'|'PENDING'|'RUNNING'|'ABORTING'|'ABORTED'|'COMPLETED'|'FAILED'|'EXPIRED',
        'StatusMessage': 'string',
        'PercentDone': 'string',
        'BackupSizeInBytes': 123,
        'IamRoleArn': 'string',
        'CreatedBy': {
            'BackupPlanId': 'string',
            'BackupPlanArn': 'string',
            'BackupPlanVersion': 'string',
            'BackupRuleId': 'string'
        },
        'ResourceType': 'string',
        'BytesTransferred': 123,
        'ExpectedCompletionDate': datetime(2015, 1, 1),
        'StartBy': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_backup_vault(BackupVaultName=None):
    """
    Returns metadata about a backup vault specified by its name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_backup_vault(
        BackupVaultName='string'
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    :rtype: dict
ReturnsResponse Syntax{
    'BackupVaultName': 'string',
    'BackupVaultArn': 'string',
    'EncryptionKeyArn': 'string',
    'CreationDate': datetime(2015, 1, 1),
    'CreatorRequestId': 'string',
    'NumberOfRecoveryPoints': 123
}


Response Structure

(dict) --
BackupVaultName (string) --The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.

BackupVaultArn (string) --An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

EncryptionKeyArn (string) --The server-side encryption key that is used to protect your backups; for example, arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab .

CreationDate (datetime) --The date and time that a backup vault is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CreatorRequestId (string) --A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.

NumberOfRecoveryPoints (integer) --The number of recovery points that are stored in a backup vault.






Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'BackupVaultName': 'string',
        'BackupVaultArn': 'string',
        'EncryptionKeyArn': 'string',
        'CreationDate': datetime(2015, 1, 1),
        'CreatorRequestId': 'string',
        'NumberOfRecoveryPoints': 123
    }
    
    
    """
    pass

def describe_copy_job(CopyJobId=None):
    """
    Returns metadata associated with creating a copy of a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_copy_job(
        CopyJobId='string'
    )
    
    
    :type CopyJobId: string
    :param CopyJobId: [REQUIRED]\nUniquely identifies a copy job.\n

    :rtype: dict
ReturnsResponse Syntax{
    'CopyJob': {
        'CopyJobId': 'string',
        'SourceBackupVaultArn': 'string',
        'SourceRecoveryPointArn': 'string',
        'DestinationBackupVaultArn': 'string',
        'DestinationRecoveryPointArn': 'string',
        'ResourceArn': 'string',
        'CreationDate': datetime(2015, 1, 1),
        'CompletionDate': datetime(2015, 1, 1),
        'State': 'CREATED'|'RUNNING'|'COMPLETED'|'FAILED',
        'StatusMessage': 'string',
        'BackupSizeInBytes': 123,
        'IamRoleArn': 'string',
        'CreatedBy': {
            'BackupPlanId': 'string',
            'BackupPlanArn': 'string',
            'BackupPlanVersion': 'string',
            'BackupRuleId': 'string'
        },
        'ResourceType': 'string'
    }
}


Response Structure

(dict) --
CopyJob (dict) --Contains detailed information about a copy job.

CopyJobId (string) --Uniquely identifies a copy job.

SourceBackupVaultArn (string) --An Amazon Resource Name (ARN) that uniquely identifies a source copy vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

SourceRecoveryPointArn (string) --An ARN that uniquely identifies a source recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .

DestinationBackupVaultArn (string) --An Amazon Resource Name (ARN) that uniquely identifies a destination copy vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

DestinationRecoveryPointArn (string) --An ARN that uniquely identifies a destination recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .

ResourceArn (string) --The AWS resource to be copied; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

CreationDate (datetime) --The date and time a copy job is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CompletionDate (datetime) --The date and time a copy job is completed, in Unix format and Coordinated Universal Time (UTC). The value of CompletionDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

State (string) --The current state of a copy job.

StatusMessage (string) --A detailed message explaining the status of the job to copy a resource.

BackupSizeInBytes (integer) --The size, in bytes, of a copy job.

IamRoleArn (string) --Specifies the IAM role ARN used to copy the target recovery point; for example, arn:aws:iam::123456789012:role/S3Access .

CreatedBy (dict) --Contains information about the backup plan and rule that AWS Backup used to initiate the recovery point backup.

BackupPlanId (string) --Uniquely identifies a backup plan.

BackupPlanArn (string) --An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50 .

BackupPlanVersion (string) --Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.

BackupRuleId (string) --Uniquely identifies a rule used to schedule the backup of a selection of resources.



ResourceType (string) --The type of AWS resource to be copied; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.








Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'CopyJob': {
            'CopyJobId': 'string',
            'SourceBackupVaultArn': 'string',
            'SourceRecoveryPointArn': 'string',
            'DestinationBackupVaultArn': 'string',
            'DestinationRecoveryPointArn': 'string',
            'ResourceArn': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'CompletionDate': datetime(2015, 1, 1),
            'State': 'CREATED'|'RUNNING'|'COMPLETED'|'FAILED',
            'StatusMessage': 'string',
            'BackupSizeInBytes': 123,
            'IamRoleArn': 'string',
            'CreatedBy': {
                'BackupPlanId': 'string',
                'BackupPlanArn': 'string',
                'BackupPlanVersion': 'string',
                'BackupRuleId': 'string'
            },
            'ResourceType': 'string'
        }
    }
    
    
    """
    pass

def describe_protected_resource(ResourceArn=None):
    """
    Returns information about a saved resource, including the last time it was backed up, its Amazon Resource Name (ARN), and the AWS service type of the saved resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_protected_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nAn Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ResourceArn': 'string',
    'ResourceType': 'string',
    'LastBackupTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --
ResourceArn (string) --An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.

ResourceType (string) --The type of AWS resource saved as a recovery point; for example, an EBS volume or an Amazon RDS database.

LastBackupTime (datetime) --The date and time that a resource was last backed up, in Unix format and Coordinated Universal Time (UTC). The value of LastBackupTime is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.






Exceptions

Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.ServiceUnavailableException
Backup.Client.exceptions.ResourceNotFoundException


    :return: {
        'ResourceArn': 'string',
        'ResourceType': 'string',
        'LastBackupTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_recovery_point(BackupVaultName=None, RecoveryPointArn=None):
    """
    Returns metadata associated with a recovery point, including ID, status, encryption, and lifecycle.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_recovery_point(
        BackupVaultName='string',
        RecoveryPointArn='string'
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    :type RecoveryPointArn: string
    :param RecoveryPointArn: [REQUIRED]\nAn Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RecoveryPointArn': 'string',
    'BackupVaultName': 'string',
    'BackupVaultArn': 'string',
    'ResourceArn': 'string',
    'ResourceType': 'string',
    'CreatedBy': {
        'BackupPlanId': 'string',
        'BackupPlanArn': 'string',
        'BackupPlanVersion': 'string',
        'BackupRuleId': 'string'
    },
    'IamRoleArn': 'string',
    'Status': 'COMPLETED'|'PARTIAL'|'DELETING'|'EXPIRED',
    'CreationDate': datetime(2015, 1, 1),
    'CompletionDate': datetime(2015, 1, 1),
    'BackupSizeInBytes': 123,
    'CalculatedLifecycle': {
        'MoveToColdStorageAt': datetime(2015, 1, 1),
        'DeleteAt': datetime(2015, 1, 1)
    },
    'Lifecycle': {
        'MoveToColdStorageAfterDays': 123,
        'DeleteAfterDays': 123
    },
    'EncryptionKeyArn': 'string',
    'IsEncrypted': True|False,
    'StorageClass': 'WARM'|'COLD'|'DELETED',
    'LastRestoreTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --

RecoveryPointArn (string) --
An ARN that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .

BackupVaultName (string) --
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.

BackupVaultArn (string) --
An ARN that uniquely identifies a backup vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

ResourceArn (string) --
An ARN that uniquely identifies a saved resource. The format of the ARN depends on the resource type.

ResourceType (string) --
The type of AWS resource to save as a recovery point; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

CreatedBy (dict) --
Contains identifying information about the creation of a recovery point, including the BackupPlanArn , BackupPlanId , BackupPlanVersion , and BackupRuleId of the backup plan used to create it.

BackupPlanId (string) --
Uniquely identifies a backup plan.

BackupPlanArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50 .

BackupPlanVersion (string) --
Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.

BackupRuleId (string) --
Uniquely identifies a rule used to schedule the backup of a selection of resources.



IamRoleArn (string) --
Specifies the IAM role ARN used to create the target recovery point; for example, arn:aws:iam::123456789012:role/S3Access .

Status (string) --
A status code specifying the state of the recovery point.

Note
A partial status indicates that the recovery point was not successfully re-created and must be retried.


CreationDate (datetime) --
The date and time that a recovery point is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CompletionDate (datetime) --
The date and time that a job to create a recovery point is completed, in Unix format and Coordinated Universal Time (UTC). The value of CompletionDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

BackupSizeInBytes (integer) --
The size, in bytes, of a backup.

CalculatedLifecycle (dict) --
A CalculatedLifecycle object containing DeleteAt and MoveToColdStorageAt timestamps.

MoveToColdStorageAt (datetime) --
A timestamp that specifies when to transition a recovery point to cold storage.

DeleteAt (datetime) --
A timestamp that specifies when to delete a recovery point.



Lifecycle (dict) --
The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.
Backups that are transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.

MoveToColdStorageAfterDays (integer) --
Specifies the number of days after creation that a recovery point is moved to cold storage.

DeleteAfterDays (integer) --
Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .



EncryptionKeyArn (string) --
The server-side encryption key used to protect your backups; for example, arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab .

IsEncrypted (boolean) --
A Boolean value that is returned as TRUE if the specified recovery point is encrypted, or FALSE if the recovery point is not encrypted.

StorageClass (string) --
Specifies the storage class of the recovery point. Valid values are WARM or COLD .

LastRestoreTime (datetime) --
The date and time that a recovery point was last restored, in Unix format and Coordinated Universal Time (UTC). The value of LastRestoreTime is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.







Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'RecoveryPointArn': 'string',
        'BackupVaultName': 'string',
        'BackupVaultArn': 'string',
        'ResourceArn': 'string',
        'ResourceType': 'string',
        'CreatedBy': {
            'BackupPlanId': 'string',
            'BackupPlanArn': 'string',
            'BackupPlanVersion': 'string',
            'BackupRuleId': 'string'
        },
        'IamRoleArn': 'string',
        'Status': 'COMPLETED'|'PARTIAL'|'DELETING'|'EXPIRED',
        'CreationDate': datetime(2015, 1, 1),
        'CompletionDate': datetime(2015, 1, 1),
        'BackupSizeInBytes': 123,
        'CalculatedLifecycle': {
            'MoveToColdStorageAt': datetime(2015, 1, 1),
            'DeleteAt': datetime(2015, 1, 1)
        },
        'Lifecycle': {
            'MoveToColdStorageAfterDays': 123,
            'DeleteAfterDays': 123
        },
        'EncryptionKeyArn': 'string',
        'IsEncrypted': True|False,
        'StorageClass': 'WARM'|'COLD'|'DELETED',
        'LastRestoreTime': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def describe_region_settings():
    """
    Returns the current service opt-in settings for the region. If the service has a value set to true, AWS Backup will attempt to protect that service\'s resources in this region, when included in an on-demand backup or scheduled backup plan. If the value is set to false for a service, AWS Backup will not attempt to protect that service\'s resources in this region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_region_settings()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'ResourceTypeOptInPreference': {
        'string': True|False
    }
}


Response Structure

(dict) --
ResourceTypeOptInPreference (dict) --Returns a list of all services along with the opt-in preferences in the region.

(string) --
(boolean) --









Exceptions

Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'ResourceTypeOptInPreference': {
            'string': True|False
        }
    }
    
    
    :returns: 
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def describe_restore_job(RestoreJobId=None):
    """
    Returns metadata associated with a restore job that is specified by a job ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_restore_job(
        RestoreJobId='string'
    )
    
    
    :type RestoreJobId: string
    :param RestoreJobId: [REQUIRED]\nUniquely identifies the job that restores a recovery point.\n

    :rtype: dict
ReturnsResponse Syntax{
    'RestoreJobId': 'string',
    'RecoveryPointArn': 'string',
    'CreationDate': datetime(2015, 1, 1),
    'CompletionDate': datetime(2015, 1, 1),
    'Status': 'PENDING'|'RUNNING'|'COMPLETED'|'ABORTED'|'FAILED',
    'StatusMessage': 'string',
    'PercentDone': 'string',
    'BackupSizeInBytes': 123,
    'IamRoleArn': 'string',
    'ExpectedCompletionTimeMinutes': 123,
    'CreatedResourceArn': 'string'
}


Response Structure

(dict) --
RestoreJobId (string) --Uniquely identifies the job that restores a recovery point.

RecoveryPointArn (string) --An ARN that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .

CreationDate (datetime) --The date and time that a restore job is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CompletionDate (datetime) --The date and time that a job to restore a recovery point is completed, in Unix format and Coordinated Universal Time (UTC). The value of CompletionDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Status (string) --Status code specifying the state of the job that is initiated by AWS Backup to restore a recovery point.

StatusMessage (string) --A detailed message explaining the status of a job to restore a recovery point.

PercentDone (string) --Contains an estimated percentage that is complete of a job at the time the job status was queried.

BackupSizeInBytes (integer) --The size, in bytes, of the restored resource.

IamRoleArn (string) --Specifies the IAM role ARN used to create the target recovery point; for example, arn:aws:iam::123456789012:role/S3Access .

ExpectedCompletionTimeMinutes (integer) --The amount of time in minutes that a job restoring a recovery point is expected to take.

CreatedResourceArn (string) --An Amazon Resource Name (ARN) that uniquely identifies a resource whose recovery point is being restored. The format of the ARN depends on the resource type of the backed-up resource.






Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException
Backup.Client.exceptions.DependencyFailureException


    :return: {
        'RestoreJobId': 'string',
        'RecoveryPointArn': 'string',
        'CreationDate': datetime(2015, 1, 1),
        'CompletionDate': datetime(2015, 1, 1),
        'Status': 'PENDING'|'RUNNING'|'COMPLETED'|'ABORTED'|'FAILED',
        'StatusMessage': 'string',
        'PercentDone': 'string',
        'BackupSizeInBytes': 123,
        'IamRoleArn': 'string',
        'ExpectedCompletionTimeMinutes': 123,
        'CreatedResourceArn': 'string'
    }
    
    
    """
    pass

def export_backup_plan_template(BackupPlanId=None):
    """
    Returns the backup plan that is specified by the plan ID as a backup template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.export_backup_plan_template(
        BackupPlanId='string'
    )
    
    
    :type BackupPlanId: string
    :param BackupPlanId: [REQUIRED]\nUniquely identifies a backup plan.\n

    :rtype: dict
ReturnsResponse Syntax{
    'BackupPlanTemplateJson': 'string'
}


Response Structure

(dict) --
BackupPlanTemplateJson (string) --The body of a backup plan template in JSON format.

Note
This is a signed JSON document that cannot be modified before being passed to GetBackupPlanFromJSON.







Exceptions

Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException
Backup.Client.exceptions.ResourceNotFoundException


    :return: {
        'BackupPlanTemplateJson': 'string'
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

def get_backup_plan(BackupPlanId=None, VersionId=None):
    """
    Returns the body of a backup plan in JSON format, in addition to plan metadata.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_backup_plan(
        BackupPlanId='string',
        VersionId='string'
    )
    
    
    :type BackupPlanId: string
    :param BackupPlanId: [REQUIRED]\nUniquely identifies a backup plan.\n

    :type VersionId: string
    :param VersionId: Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.

    :rtype: dict

ReturnsResponse Syntax
{
    'BackupPlan': {
        'BackupPlanName': 'string',
        'Rules': [
            {
                'RuleName': 'string',
                'TargetBackupVaultName': 'string',
                'ScheduleExpression': 'string',
                'StartWindowMinutes': 123,
                'CompletionWindowMinutes': 123,
                'Lifecycle': {
                    'MoveToColdStorageAfterDays': 123,
                    'DeleteAfterDays': 123
                },
                'RecoveryPointTags': {
                    'string': 'string'
                },
                'RuleId': 'string',
                'CopyActions': [
                    {
                        'Lifecycle': {
                            'MoveToColdStorageAfterDays': 123,
                            'DeleteAfterDays': 123
                        },
                        'DestinationBackupVaultArn': 'string'
                    },
                ]
            },
        ]
    },
    'BackupPlanId': 'string',
    'BackupPlanArn': 'string',
    'VersionId': 'string',
    'CreatorRequestId': 'string',
    'CreationDate': datetime(2015, 1, 1),
    'DeletionDate': datetime(2015, 1, 1),
    'LastExecutionDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

BackupPlan (dict) --
Specifies the body of a backup plan. Includes a BackupPlanName and one or more sets of Rules .

BackupPlanName (string) --
The display name of a backup plan.

Rules (list) --
An array of BackupRule objects, each of which specifies a scheduled task that is used to back up a selection of resources.

(dict) --
Specifies a scheduled task used to back up a selection of resources.

RuleName (string) --
An optional display name for a backup rule.

TargetBackupVaultName (string) --
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.

ScheduleExpression (string) --
A CRON expression specifying when AWS Backup initiates a backup job.

StartWindowMinutes (integer) --
A value in minutes after a backup is scheduled before a job will be canceled if it doesn\'t start successfully. This value is optional.

CompletionWindowMinutes (integer) --
A value in minutes after a backup job is successfully started before it must be completed or it will be canceled by AWS Backup. This value is optional.

Lifecycle (dict) --
The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.
Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.

MoveToColdStorageAfterDays (integer) --
Specifies the number of days after creation that a recovery point is moved to cold storage.

DeleteAfterDays (integer) --
Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .



RecoveryPointTags (dict) --
An array of key-value pair strings that are assigned to resources that are associated with this rule when restored from backup.

(string) --
(string) --




RuleId (string) --
Uniquely identifies a rule that is used to schedule the backup of a selection of resources.

CopyActions (list) --
An array of CopyAction objects, which contains the details of the copy operation.

(dict) --
The details of the copy operation.

Lifecycle (dict) --
Contains an array of Transition objects specifying how long in days before a recovery point transitions to cold storage or is deleted.
Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, on the console, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.

MoveToColdStorageAfterDays (integer) --
Specifies the number of days after creation that a recovery point is moved to cold storage.

DeleteAfterDays (integer) --
Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .



DestinationBackupVaultArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup. For example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .











BackupPlanId (string) --
Uniquely identifies a backup plan.

BackupPlanArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50 .

VersionId (string) --
Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.

CreatorRequestId (string) --
A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.

CreationDate (datetime) --
The date and time that a backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

DeletionDate (datetime) --
The date and time that a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

LastExecutionDate (datetime) --
The last time a job to back up resources was executed with this backup plan. A date and time, in Unix format and Coordinated Universal Time (UTC). The value of LastExecutionDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.







Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'BackupPlan': {
            'BackupPlanName': 'string',
            'Rules': [
                {
                    'RuleName': 'string',
                    'TargetBackupVaultName': 'string',
                    'ScheduleExpression': 'string',
                    'StartWindowMinutes': 123,
                    'CompletionWindowMinutes': 123,
                    'Lifecycle': {
                        'MoveToColdStorageAfterDays': 123,
                        'DeleteAfterDays': 123
                    },
                    'RecoveryPointTags': {
                        'string': 'string'
                    },
                    'RuleId': 'string',
                    'CopyActions': [
                        {
                            'Lifecycle': {
                                'MoveToColdStorageAfterDays': 123,
                                'DeleteAfterDays': 123
                            },
                            'DestinationBackupVaultArn': 'string'
                        },
                    ]
                },
            ]
        },
        'BackupPlanId': 'string',
        'BackupPlanArn': 'string',
        'VersionId': 'string',
        'CreatorRequestId': 'string',
        'CreationDate': datetime(2015, 1, 1),
        'DeletionDate': datetime(2015, 1, 1),
        'LastExecutionDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_backup_plan_from_json(BackupPlanTemplateJson=None):
    """
    Returns a valid JSON document specifying a backup plan or an error.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_backup_plan_from_json(
        BackupPlanTemplateJson='string'
    )
    
    
    :type BackupPlanTemplateJson: string
    :param BackupPlanTemplateJson: [REQUIRED]\nA customer-supplied backup plan document in JSON format.\n

    :rtype: dict
ReturnsResponse Syntax{
    'BackupPlan': {
        'BackupPlanName': 'string',
        'Rules': [
            {
                'RuleName': 'string',
                'TargetBackupVaultName': 'string',
                'ScheduleExpression': 'string',
                'StartWindowMinutes': 123,
                'CompletionWindowMinutes': 123,
                'Lifecycle': {
                    'MoveToColdStorageAfterDays': 123,
                    'DeleteAfterDays': 123
                },
                'RecoveryPointTags': {
                    'string': 'string'
                },
                'RuleId': 'string',
                'CopyActions': [
                    {
                        'Lifecycle': {
                            'MoveToColdStorageAfterDays': 123,
                            'DeleteAfterDays': 123
                        },
                        'DestinationBackupVaultArn': 'string'
                    },
                ]
            },
        ]
    }
}


Response Structure

(dict) --
BackupPlan (dict) --Specifies the body of a backup plan. Includes a BackupPlanName and one or more sets of Rules .

BackupPlanName (string) --The display name of a backup plan.

Rules (list) --An array of BackupRule objects, each of which specifies a scheduled task that is used to back up a selection of resources.

(dict) --Specifies a scheduled task used to back up a selection of resources.

RuleName (string) --An optional display name for a backup rule.

TargetBackupVaultName (string) --The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.

ScheduleExpression (string) --A CRON expression specifying when AWS Backup initiates a backup job.

StartWindowMinutes (integer) --A value in minutes after a backup is scheduled before a job will be canceled if it doesn\'t start successfully. This value is optional.

CompletionWindowMinutes (integer) --A value in minutes after a backup job is successfully started before it must be completed or it will be canceled by AWS Backup. This value is optional.

Lifecycle (dict) --The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.
Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.

MoveToColdStorageAfterDays (integer) --Specifies the number of days after creation that a recovery point is moved to cold storage.

DeleteAfterDays (integer) --Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .



RecoveryPointTags (dict) --An array of key-value pair strings that are assigned to resources that are associated with this rule when restored from backup.

(string) --
(string) --




RuleId (string) --Uniquely identifies a rule that is used to schedule the backup of a selection of resources.

CopyActions (list) --An array of CopyAction objects, which contains the details of the copy operation.

(dict) --The details of the copy operation.

Lifecycle (dict) --Contains an array of Transition objects specifying how long in days before a recovery point transitions to cold storage or is deleted.
Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, on the console, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.

MoveToColdStorageAfterDays (integer) --Specifies the number of days after creation that a recovery point is moved to cold storage.

DeleteAfterDays (integer) --Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .



DestinationBackupVaultArn (string) --An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup. For example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .
















Exceptions

Backup.Client.exceptions.LimitExceededException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException
Backup.Client.exceptions.InvalidRequestException


    :return: {
        'BackupPlan': {
            'BackupPlanName': 'string',
            'Rules': [
                {
                    'RuleName': 'string',
                    'TargetBackupVaultName': 'string',
                    'ScheduleExpression': 'string',
                    'StartWindowMinutes': 123,
                    'CompletionWindowMinutes': 123,
                    'Lifecycle': {
                        'MoveToColdStorageAfterDays': 123,
                        'DeleteAfterDays': 123
                    },
                    'RecoveryPointTags': {
                        'string': 'string'
                    },
                    'RuleId': 'string',
                    'CopyActions': [
                        {
                            'Lifecycle': {
                                'MoveToColdStorageAfterDays': 123,
                                'DeleteAfterDays': 123
                            },
                            'DestinationBackupVaultArn': 'string'
                        },
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    Backup.Client.exceptions.LimitExceededException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    Backup.Client.exceptions.InvalidRequestException
    
    """
    pass

def get_backup_plan_from_template(BackupPlanTemplateId=None):
    """
    Returns the template specified by its templateId as a backup plan.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_backup_plan_from_template(
        BackupPlanTemplateId='string'
    )
    
    
    :type BackupPlanTemplateId: string
    :param BackupPlanTemplateId: [REQUIRED]\nUniquely identifies a stored backup plan template.\n

    :rtype: dict
ReturnsResponse Syntax{
    'BackupPlanDocument': {
        'BackupPlanName': 'string',
        'Rules': [
            {
                'RuleName': 'string',
                'TargetBackupVaultName': 'string',
                'ScheduleExpression': 'string',
                'StartWindowMinutes': 123,
                'CompletionWindowMinutes': 123,
                'Lifecycle': {
                    'MoveToColdStorageAfterDays': 123,
                    'DeleteAfterDays': 123
                },
                'RecoveryPointTags': {
                    'string': 'string'
                },
                'RuleId': 'string',
                'CopyActions': [
                    {
                        'Lifecycle': {
                            'MoveToColdStorageAfterDays': 123,
                            'DeleteAfterDays': 123
                        },
                        'DestinationBackupVaultArn': 'string'
                    },
                ]
            },
        ]
    }
}


Response Structure

(dict) --
BackupPlanDocument (dict) --Returns the body of a backup plan based on the target template, including the name, rules, and backup vault of the plan.

BackupPlanName (string) --The display name of a backup plan.

Rules (list) --An array of BackupRule objects, each of which specifies a scheduled task that is used to back up a selection of resources.

(dict) --Specifies a scheduled task used to back up a selection of resources.

RuleName (string) --An optional display name for a backup rule.

TargetBackupVaultName (string) --The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.

ScheduleExpression (string) --A CRON expression specifying when AWS Backup initiates a backup job.

StartWindowMinutes (integer) --A value in minutes after a backup is scheduled before a job will be canceled if it doesn\'t start successfully. This value is optional.

CompletionWindowMinutes (integer) --A value in minutes after a backup job is successfully started before it must be completed or it will be canceled by AWS Backup. This value is optional.

Lifecycle (dict) --The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.
Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.

MoveToColdStorageAfterDays (integer) --Specifies the number of days after creation that a recovery point is moved to cold storage.

DeleteAfterDays (integer) --Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .



RecoveryPointTags (dict) --An array of key-value pair strings that are assigned to resources that are associated with this rule when restored from backup.

(string) --
(string) --




RuleId (string) --Uniquely identifies a rule that is used to schedule the backup of a selection of resources.

CopyActions (list) --An array of CopyAction objects, which contains the details of the copy operation.

(dict) --The details of the copy operation.

Lifecycle (dict) --Contains an array of Transition objects specifying how long in days before a recovery point transitions to cold storage or is deleted.
Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, on the console, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.

MoveToColdStorageAfterDays (integer) --Specifies the number of days after creation that a recovery point is moved to cold storage.

DeleteAfterDays (integer) --Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .



DestinationBackupVaultArn (string) --An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup. For example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .
















Exceptions

Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException
Backup.Client.exceptions.ResourceNotFoundException


    :return: {
        'BackupPlanDocument': {
            'BackupPlanName': 'string',
            'Rules': [
                {
                    'RuleName': 'string',
                    'TargetBackupVaultName': 'string',
                    'ScheduleExpression': 'string',
                    'StartWindowMinutes': 123,
                    'CompletionWindowMinutes': 123,
                    'Lifecycle': {
                        'MoveToColdStorageAfterDays': 123,
                        'DeleteAfterDays': 123
                    },
                    'RecoveryPointTags': {
                        'string': 'string'
                    },
                    'RuleId': 'string',
                    'CopyActions': [
                        {
                            'Lifecycle': {
                                'MoveToColdStorageAfterDays': 123,
                                'DeleteAfterDays': 123
                            },
                            'DestinationBackupVaultArn': 'string'
                        },
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    Backup.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def get_backup_selection(BackupPlanId=None, SelectionId=None):
    """
    Returns selection metadata and a document in JSON format that specifies a list of resources that are associated with a backup plan.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_backup_selection(
        BackupPlanId='string',
        SelectionId='string'
    )
    
    
    :type BackupPlanId: string
    :param BackupPlanId: [REQUIRED]\nUniquely identifies a backup plan.\n

    :type SelectionId: string
    :param SelectionId: [REQUIRED]\nUniquely identifies the body of a request to assign a set of resources to a backup plan.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'BackupSelection': {
        'SelectionName': 'string',
        'IamRoleArn': 'string',
        'Resources': [
            'string',
        ],
        'ListOfTags': [
            {
                'ConditionType': 'STRINGEQUALS',
                'ConditionKey': 'string',
                'ConditionValue': 'string'
            },
        ]
    },
    'SelectionId': 'string',
    'BackupPlanId': 'string',
    'CreationDate': datetime(2015, 1, 1),
    'CreatorRequestId': 'string'
}


Response Structure

(dict) --

BackupSelection (dict) --
Specifies the body of a request to assign a set of resources to a backup plan.

SelectionName (string) --
The display name of a resource selection document.

IamRoleArn (string) --
The ARN of the IAM role that AWS Backup uses to authenticate when restoring the target resource; for example, arn:aws:iam::123456789012:role/S3Access .

Resources (list) --
An array of strings that contain Amazon Resource Names (ARNs) of resources to assign to a backup plan.

(string) --


ListOfTags (list) --
An array of conditions used to specify a set of resources to assign to a backup plan; for example, "STRINGEQUALS": {"ec2:ResourceTag/Department": "accounting" .

(dict) --
Contains an array of triplets made up of a condition type (such as STRINGEQUALS ), a key, and a value. Conditions are used to filter resources in a selection that is assigned to a backup plan.

ConditionType (string) --
An operation, such as STRINGEQUALS , that is applied to a key-value pair used to filter resources in a selection.

ConditionKey (string) --
The key in a key-value pair. For example, in "ec2:ResourceTag/Department": "accounting" , "ec2:ResourceTag/Department" is the key.

ConditionValue (string) --
The value in a key-value pair. For example, in "ec2:ResourceTag/Department": "accounting" , "accounting" is the value.







SelectionId (string) --
Uniquely identifies the body of a request to assign a set of resources to a backup plan.

BackupPlanId (string) --
Uniquely identifies a backup plan.

CreationDate (datetime) --
The date and time a backup selection is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CreatorRequestId (string) --
A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.







Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'BackupSelection': {
            'SelectionName': 'string',
            'IamRoleArn': 'string',
            'Resources': [
                'string',
            ],
            'ListOfTags': [
                {
                    'ConditionType': 'STRINGEQUALS',
                    'ConditionKey': 'string',
                    'ConditionValue': 'string'
                },
            ]
        },
        'SelectionId': 'string',
        'BackupPlanId': 'string',
        'CreationDate': datetime(2015, 1, 1),
        'CreatorRequestId': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_backup_vault_access_policy(BackupVaultName=None):
    """
    Returns the access policy document that is associated with the named backup vault.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_backup_vault_access_policy(
        BackupVaultName='string'
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    :rtype: dict
ReturnsResponse Syntax{
    'BackupVaultName': 'string',
    'BackupVaultArn': 'string',
    'Policy': 'string'
}


Response Structure

(dict) --
BackupVaultName (string) --The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.

BackupVaultArn (string) --An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

Policy (string) --The backup vault access policy document in JSON format.






Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'BackupVaultName': 'string',
        'BackupVaultArn': 'string',
        'Policy': 'string'
    }
    
    
    """
    pass

def get_backup_vault_notifications(BackupVaultName=None):
    """
    Returns event notifications for the specified backup vault.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_backup_vault_notifications(
        BackupVaultName='string'
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    :rtype: dict
ReturnsResponse Syntax{
    'BackupVaultName': 'string',
    'BackupVaultArn': 'string',
    'SNSTopicArn': 'string',
    'BackupVaultEvents': [
        'BACKUP_JOB_STARTED'|'BACKUP_JOB_COMPLETED'|'BACKUP_JOB_SUCCESSFUL'|'BACKUP_JOB_FAILED'|'BACKUP_JOB_EXPIRED'|'RESTORE_JOB_STARTED'|'RESTORE_JOB_COMPLETED'|'RESTORE_JOB_SUCCESSFUL'|'RESTORE_JOB_FAILED'|'COPY_JOB_STARTED'|'COPY_JOB_SUCCESSFUL'|'COPY_JOB_FAILED'|'RECOVERY_POINT_MODIFIED'|'BACKUP_PLAN_CREATED'|'BACKUP_PLAN_MODIFIED',
    ]
}


Response Structure

(dict) --
BackupVaultName (string) --The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.

BackupVaultArn (string) --An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

SNSTopicArn (string) --An ARN that uniquely identifies an Amazon Simple Notification Service (Amazon SNS) topic; for example, arn:aws:sns:us-west-2:111122223333:MyTopic .

BackupVaultEvents (list) --An array of events that indicate the status of jobs to back up resources to the backup vault.

(string) --







Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'BackupVaultName': 'string',
        'BackupVaultArn': 'string',
        'SNSTopicArn': 'string',
        'BackupVaultEvents': [
            'BACKUP_JOB_STARTED'|'BACKUP_JOB_COMPLETED'|'BACKUP_JOB_SUCCESSFUL'|'BACKUP_JOB_FAILED'|'BACKUP_JOB_EXPIRED'|'RESTORE_JOB_STARTED'|'RESTORE_JOB_COMPLETED'|'RESTORE_JOB_SUCCESSFUL'|'RESTORE_JOB_FAILED'|'COPY_JOB_STARTED'|'COPY_JOB_SUCCESSFUL'|'COPY_JOB_FAILED'|'RECOVERY_POINT_MODIFIED'|'BACKUP_PLAN_CREATED'|'BACKUP_PLAN_MODIFIED',
        ]
    }
    
    
    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
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

def get_recovery_point_restore_metadata(BackupVaultName=None, RecoveryPointArn=None):
    """
    Returns a set of metadata key-value pairs that were used to create the backup.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_recovery_point_restore_metadata(
        BackupVaultName='string',
        RecoveryPointArn='string'
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    :type RecoveryPointArn: string
    :param RecoveryPointArn: [REQUIRED]\nAn Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'BackupVaultArn': 'string',
    'RecoveryPointArn': 'string',
    'RestoreMetadata': {
        'string': 'string'
    }
}


Response Structure

(dict) --

BackupVaultArn (string) --
An ARN that uniquely identifies a backup vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

RecoveryPointArn (string) --
An ARN that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .

RestoreMetadata (dict) --
The set of metadata key-value pairs that describes the original configuration of the backed-up resource. These values vary depending on the service that is being restored.

(string) --
(string) --










Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'BackupVaultArn': 'string',
        'RecoveryPointArn': 'string',
        'RestoreMetadata': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_supported_resource_types():
    """
    Returns the AWS resource types supported by AWS Backup.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_supported_resource_types()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'ResourceTypes': [
        'string',
    ]
}


Response Structure

(dict) --
ResourceTypes (list) --Contains a string with the supported AWS resource types:

EBS for Amazon Elastic Block Store
Storage Gateway for AWS Storage Gateway
RDS for Amazon Relational Database Service
DDB for Amazon DynamoDB
EFS for Amazon Elastic File System


(string) --







Exceptions

Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'ResourceTypes': [
            'string',
        ]
    }
    
    
    :returns: 
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

def list_backup_jobs(NextToken=None, MaxResults=None, ByResourceArn=None, ByState=None, ByBackupVaultName=None, ByCreatedBefore=None, ByCreatedAfter=None, ByResourceType=None):
    """
    Returns metadata about your backup jobs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_backup_jobs(
        NextToken='string',
        MaxResults=123,
        ByResourceArn='string',
        ByState='CREATED'|'PENDING'|'RUNNING'|'ABORTING'|'ABORTED'|'COMPLETED'|'FAILED'|'EXPIRED',
        ByBackupVaultName='string',
        ByCreatedBefore=datetime(2015, 1, 1),
        ByCreatedAfter=datetime(2015, 1, 1),
        ByResourceType='string'
    )
    
    
    :type NextToken: string
    :param NextToken: The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be returned.

    :type ByResourceArn: string
    :param ByResourceArn: Returns only backup jobs that match the specified resource Amazon Resource Name (ARN).

    :type ByState: string
    :param ByState: Returns only backup jobs that are in the specified state.

    :type ByBackupVaultName: string
    :param ByBackupVaultName: Returns only backup jobs that will be stored in the specified backup vault. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.

    :type ByCreatedBefore: datetime
    :param ByCreatedBefore: Returns only backup jobs that were created before the specified date.

    :type ByCreatedAfter: datetime
    :param ByCreatedAfter: Returns only backup jobs that were created after the specified date.

    :type ByResourceType: string
    :param ByResourceType: Returns only backup jobs for the specified resources:\n\nDynamoDB for Amazon DynamoDB\nEBS for Amazon Elastic Block Store\nEFS for Amazon Elastic File System\nRDS for Amazon Relational Database Service\nStorage Gateway for AWS Storage Gateway\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'BackupJobs': [
        {
            'BackupJobId': 'string',
            'BackupVaultName': 'string',
            'BackupVaultArn': 'string',
            'RecoveryPointArn': 'string',
            'ResourceArn': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'CompletionDate': datetime(2015, 1, 1),
            'State': 'CREATED'|'PENDING'|'RUNNING'|'ABORTING'|'ABORTED'|'COMPLETED'|'FAILED'|'EXPIRED',
            'StatusMessage': 'string',
            'PercentDone': 'string',
            'BackupSizeInBytes': 123,
            'IamRoleArn': 'string',
            'CreatedBy': {
                'BackupPlanId': 'string',
                'BackupPlanArn': 'string',
                'BackupPlanVersion': 'string',
                'BackupRuleId': 'string'
            },
            'ExpectedCompletionDate': datetime(2015, 1, 1),
            'StartBy': datetime(2015, 1, 1),
            'ResourceType': 'string',
            'BytesTransferred': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

BackupJobs (list) --
An array of structures containing metadata about your backup jobs returned in JSON format.

(dict) --
Contains detailed information about a backup job.

BackupJobId (string) --
Uniquely identifies a request to AWS Backup to back up a resource.

BackupVaultName (string) --
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.

BackupVaultArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

RecoveryPointArn (string) --
An ARN that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .

ResourceArn (string) --
An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.

CreationDate (datetime) --
The date and time a backup job is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CompletionDate (datetime) --
The date and time a job to create a backup job is completed, in Unix format and Coordinated Universal Time (UTC). The value of CompletionDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

State (string) --
The current state of a resource recovery point.

StatusMessage (string) --
A detailed message explaining the status of the job to back up a resource.

PercentDone (string) --
Contains an estimated percentage complete of a job at the time the job status was queried.

BackupSizeInBytes (integer) --
The size, in bytes, of a backup.

IamRoleArn (string) --
Specifies the IAM role ARN used to create the target recovery point; for example, arn:aws:iam::123456789012:role/S3Access .

CreatedBy (dict) --
Contains identifying information about the creation of a backup job, including the BackupPlanArn , BackupPlanId , BackupPlanVersion , and BackupRuleId of the backup plan used to create it.

BackupPlanId (string) --
Uniquely identifies a backup plan.

BackupPlanArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50 .

BackupPlanVersion (string) --
Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.

BackupRuleId (string) --
Uniquely identifies a rule used to schedule the backup of a selection of resources.



ExpectedCompletionDate (datetime) --
The date and time a job to back up resources is expected to be completed, in Unix format and Coordinated Universal Time (UTC). The value of ExpectedCompletionDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

StartBy (datetime) --
Specifies the time in Unix format and Coordinated Universal Time (UTC) when a backup job must be started before it is canceled. The value is calculated by adding the start window to the scheduled time. So if the scheduled time were 6:00 PM and the start window is 2 hours, the StartBy time would be 8:00 PM on the date specified. The value of StartBy is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

ResourceType (string) --
The type of AWS resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

BytesTransferred (integer) --
The size in bytes transferred to a backup vault at the time that the job status was queried.





NextToken (string) --
The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.







Exceptions

Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.InvalidRequestException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'BackupJobs': [
            {
                'BackupJobId': 'string',
                'BackupVaultName': 'string',
                'BackupVaultArn': 'string',
                'RecoveryPointArn': 'string',
                'ResourceArn': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'CompletionDate': datetime(2015, 1, 1),
                'State': 'CREATED'|'PENDING'|'RUNNING'|'ABORTING'|'ABORTED'|'COMPLETED'|'FAILED'|'EXPIRED',
                'StatusMessage': 'string',
                'PercentDone': 'string',
                'BackupSizeInBytes': 123,
                'IamRoleArn': 'string',
                'CreatedBy': {
                    'BackupPlanId': 'string',
                    'BackupPlanArn': 'string',
                    'BackupPlanVersion': 'string',
                    'BackupRuleId': 'string'
                },
                'ExpectedCompletionDate': datetime(2015, 1, 1),
                'StartBy': datetime(2015, 1, 1),
                'ResourceType': 'string',
                'BytesTransferred': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.InvalidRequestException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_backup_plan_templates(NextToken=None, MaxResults=None):
    """
    Returns metadata of your saved backup plan templates, including the template ID, name, and the creation and deletion dates.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_backup_plan_templates(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'BackupPlanTemplatesList': [
        {
            'BackupPlanTemplateId': 'string',
            'BackupPlanTemplateName': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

BackupPlanTemplatesList (list) --
An array of template list items containing metadata about your saved templates.

(dict) --
An object specifying metadata associated with a backup plan template.

BackupPlanTemplateId (string) --
Uniquely identifies a stored backup plan template.

BackupPlanTemplateName (string) --
The optional display name of a backup plan template.











Exceptions

Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException
Backup.Client.exceptions.ResourceNotFoundException


    :return: {
        'NextToken': 'string',
        'BackupPlanTemplatesList': [
            {
                'BackupPlanTemplateId': 'string',
                'BackupPlanTemplateName': 'string'
            },
        ]
    }
    
    
    :returns: 
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    Backup.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_backup_plan_versions(BackupPlanId=None, NextToken=None, MaxResults=None):
    """
    Returns version metadata of your backup plans, including Amazon Resource Names (ARNs), backup plan IDs, creation and deletion dates, plan names, and version IDs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_backup_plan_versions(
        BackupPlanId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type BackupPlanId: string
    :param BackupPlanId: [REQUIRED]\nUniquely identifies a backup plan.\n

    :type NextToken: string
    :param NextToken: The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'BackupPlanVersionsList': [
        {
            'BackupPlanArn': 'string',
            'BackupPlanId': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'DeletionDate': datetime(2015, 1, 1),
            'VersionId': 'string',
            'BackupPlanName': 'string',
            'CreatorRequestId': 'string',
            'LastExecutionDate': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

BackupPlanVersionsList (list) --
An array of version list items containing metadata about your backup plans.

(dict) --
Contains metadata about a backup plan.

BackupPlanArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50 .

BackupPlanId (string) --
Uniquely identifies a backup plan.

CreationDate (datetime) --
The date and time a resource backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

DeletionDate (datetime) --
The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of DeletionDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

VersionId (string) --
Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.

BackupPlanName (string) --
The display name of a saved backup plan.

CreatorRequestId (string) --
A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.

LastExecutionDate (datetime) --
The last time a job to back up resources was executed with this rule. A date and time, in Unix format and Coordinated Universal Time (UTC). The value of LastExecutionDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.











Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'NextToken': 'string',
        'BackupPlanVersionsList': [
            {
                'BackupPlanArn': 'string',
                'BackupPlanId': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'DeletionDate': datetime(2015, 1, 1),
                'VersionId': 'string',
                'BackupPlanName': 'string',
                'CreatorRequestId': 'string',
                'LastExecutionDate': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_backup_plans(NextToken=None, MaxResults=None, IncludeDeleted=None):
    """
    Returns metadata of your saved backup plans, including Amazon Resource Names (ARNs), plan IDs, creation and deletion dates, version IDs, plan names, and creator request IDs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_backup_plans(
        NextToken='string',
        MaxResults=123,
        IncludeDeleted=True|False
    )
    
    
    :type NextToken: string
    :param NextToken: The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be returned.

    :type IncludeDeleted: boolean
    :param IncludeDeleted: A Boolean value with a default value of FALSE that returns deleted backup plans when set to TRUE .

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'BackupPlansList': [
        {
            'BackupPlanArn': 'string',
            'BackupPlanId': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'DeletionDate': datetime(2015, 1, 1),
            'VersionId': 'string',
            'BackupPlanName': 'string',
            'CreatorRequestId': 'string',
            'LastExecutionDate': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

BackupPlansList (list) --
An array of backup plan list items containing metadata about your saved backup plans.

(dict) --
Contains metadata about a backup plan.

BackupPlanArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50 .

BackupPlanId (string) --
Uniquely identifies a backup plan.

CreationDate (datetime) --
The date and time a resource backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

DeletionDate (datetime) --
The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of DeletionDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

VersionId (string) --
Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.

BackupPlanName (string) --
The display name of a saved backup plan.

CreatorRequestId (string) --
A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.

LastExecutionDate (datetime) --
The last time a job to back up resources was executed with this rule. A date and time, in Unix format and Coordinated Universal Time (UTC). The value of LastExecutionDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.











Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'NextToken': 'string',
        'BackupPlansList': [
            {
                'BackupPlanArn': 'string',
                'BackupPlanId': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'DeletionDate': datetime(2015, 1, 1),
                'VersionId': 'string',
                'BackupPlanName': 'string',
                'CreatorRequestId': 'string',
                'LastExecutionDate': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_backup_selections(BackupPlanId=None, NextToken=None, MaxResults=None):
    """
    Returns an array containing metadata of the resources associated with the target backup plan.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_backup_selections(
        BackupPlanId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type BackupPlanId: string
    :param BackupPlanId: [REQUIRED]\nUniquely identifies a backup plan.\n

    :type NextToken: string
    :param NextToken: The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'BackupSelectionsList': [
        {
            'SelectionId': 'string',
            'SelectionName': 'string',
            'BackupPlanId': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'CreatorRequestId': 'string',
            'IamRoleArn': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

BackupSelectionsList (list) --
An array of backup selection list items containing metadata about each resource in the list.

(dict) --
Contains metadata about a BackupSelection object.

SelectionId (string) --
Uniquely identifies a request to assign a set of resources to a backup plan.

SelectionName (string) --
The display name of a resource selection document.

BackupPlanId (string) --
Uniquely identifies a backup plan.

CreationDate (datetime) --
The date and time a backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CreatorRequestId (string) --
A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.

IamRoleArn (string) --
Specifies the IAM role Amazon Resource Name (ARN) to create the target recovery point; for example, arn:aws:iam::123456789012:role/S3Access .











Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'NextToken': 'string',
        'BackupSelectionsList': [
            {
                'SelectionId': 'string',
                'SelectionName': 'string',
                'BackupPlanId': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'CreatorRequestId': 'string',
                'IamRoleArn': 'string'
            },
        ]
    }
    
    
    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_backup_vaults(NextToken=None, MaxResults=None):
    """
    Returns a list of recovery point storage containers along with information about them.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_backup_vaults(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'BackupVaultList': [
        {
            'BackupVaultName': 'string',
            'BackupVaultArn': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'EncryptionKeyArn': 'string',
            'CreatorRequestId': 'string',
            'NumberOfRecoveryPoints': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

BackupVaultList (list) --
An array of backup vault list members containing vault metadata, including Amazon Resource Name (ARN), display name, creation date, number of saved recovery points, and encryption information if the resources saved in the backup vault are encrypted.

(dict) --
Contains metadata about a backup vault.

BackupVaultName (string) --
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.

BackupVaultArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

CreationDate (datetime) --
The date and time a resource backup is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

EncryptionKeyArn (string) --
The server-side encryption key that is used to protect your backups; for example, arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab .

CreatorRequestId (string) --
A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.

NumberOfRecoveryPoints (integer) --
The number of recovery points that are stored in a backup vault.





NextToken (string) --
The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.







Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'BackupVaultList': [
            {
                'BackupVaultName': 'string',
                'BackupVaultArn': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'EncryptionKeyArn': 'string',
                'CreatorRequestId': 'string',
                'NumberOfRecoveryPoints': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_copy_jobs(NextToken=None, MaxResults=None, ByResourceArn=None, ByState=None, ByCreatedBefore=None, ByCreatedAfter=None, ByResourceType=None, ByDestinationVaultArn=None):
    """
    Returns metadata about your copy jobs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_copy_jobs(
        NextToken='string',
        MaxResults=123,
        ByResourceArn='string',
        ByState='CREATED'|'RUNNING'|'COMPLETED'|'FAILED',
        ByCreatedBefore=datetime(2015, 1, 1),
        ByCreatedAfter=datetime(2015, 1, 1),
        ByResourceType='string',
        ByDestinationVaultArn='string'
    )
    
    
    :type NextToken: string
    :param NextToken: The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be returned.

    :type ByResourceArn: string
    :param ByResourceArn: Returns only copy jobs that match the specified resource Amazon Resource Name (ARN).

    :type ByState: string
    :param ByState: Returns only copy jobs that are in the specified state.

    :type ByCreatedBefore: datetime
    :param ByCreatedBefore: Returns only copy jobs that were created before the specified date.

    :type ByCreatedAfter: datetime
    :param ByCreatedAfter: Returns only copy jobs that were created after the specified date.

    :type ByResourceType: string
    :param ByResourceType: Returns only backup jobs for the specified resources:\n\nEBS for Amazon Elastic Block Store\nEFS for Amazon Elastic File System\nRDS for Amazon Relational Database Service\nStorage Gateway for AWS Storage Gateway\n\n

    :type ByDestinationVaultArn: string
    :param ByDestinationVaultArn: An Amazon Resource Name (ARN) that uniquely identifies a source backup vault to copy from; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

    :rtype: dict

ReturnsResponse Syntax
{
    'CopyJobs': [
        {
            'CopyJobId': 'string',
            'SourceBackupVaultArn': 'string',
            'SourceRecoveryPointArn': 'string',
            'DestinationBackupVaultArn': 'string',
            'DestinationRecoveryPointArn': 'string',
            'ResourceArn': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'CompletionDate': datetime(2015, 1, 1),
            'State': 'CREATED'|'RUNNING'|'COMPLETED'|'FAILED',
            'StatusMessage': 'string',
            'BackupSizeInBytes': 123,
            'IamRoleArn': 'string',
            'CreatedBy': {
                'BackupPlanId': 'string',
                'BackupPlanArn': 'string',
                'BackupPlanVersion': 'string',
                'BackupRuleId': 'string'
            },
            'ResourceType': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

CopyJobs (list) --
An array of structures containing metadata about your copy jobs returned in JSON format.

(dict) --
Contains detailed information about a copy job.

CopyJobId (string) --
Uniquely identifies a copy job.

SourceBackupVaultArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a source copy vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

SourceRecoveryPointArn (string) --
An ARN that uniquely identifies a source recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .

DestinationBackupVaultArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a destination copy vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

DestinationRecoveryPointArn (string) --
An ARN that uniquely identifies a destination recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .

ResourceArn (string) --
The AWS resource to be copied; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

CreationDate (datetime) --
The date and time a copy job is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CompletionDate (datetime) --
The date and time a copy job is completed, in Unix format and Coordinated Universal Time (UTC). The value of CompletionDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

State (string) --
The current state of a copy job.

StatusMessage (string) --
A detailed message explaining the status of the job to copy a resource.

BackupSizeInBytes (integer) --
The size, in bytes, of a copy job.

IamRoleArn (string) --
Specifies the IAM role ARN used to copy the target recovery point; for example, arn:aws:iam::123456789012:role/S3Access .

CreatedBy (dict) --
Contains information about the backup plan and rule that AWS Backup used to initiate the recovery point backup.

BackupPlanId (string) --
Uniquely identifies a backup plan.

BackupPlanArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50 .

BackupPlanVersion (string) --
Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.

BackupRuleId (string) --
Uniquely identifies a rule used to schedule the backup of a selection of resources.



ResourceType (string) --
The type of AWS resource to be copied; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.





NextToken (string) --
The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.







Exceptions

Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'CopyJobs': [
            {
                'CopyJobId': 'string',
                'SourceBackupVaultArn': 'string',
                'SourceRecoveryPointArn': 'string',
                'DestinationBackupVaultArn': 'string',
                'DestinationRecoveryPointArn': 'string',
                'ResourceArn': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'CompletionDate': datetime(2015, 1, 1),
                'State': 'CREATED'|'RUNNING'|'COMPLETED'|'FAILED',
                'StatusMessage': 'string',
                'BackupSizeInBytes': 123,
                'IamRoleArn': 'string',
                'CreatedBy': {
                    'BackupPlanId': 'string',
                    'BackupPlanArn': 'string',
                    'BackupPlanVersion': 'string',
                    'BackupRuleId': 'string'
                },
                'ResourceType': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_protected_resources(NextToken=None, MaxResults=None):
    """
    Returns an array of resources successfully backed up by AWS Backup, including the time the resource was saved, an Amazon Resource Name (ARN) of the resource, and a resource type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_protected_resources(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'Results': [
        {
            'ResourceArn': 'string',
            'ResourceType': 'string',
            'LastBackupTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Results (list) --
An array of resources successfully backed up by AWS Backup including the time the resource was saved, an Amazon Resource Name (ARN) of the resource, and a resource type.

(dict) --
A structure that contains information about a backed-up resource.

ResourceArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.

ResourceType (string) --
The type of AWS resource; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

LastBackupTime (datetime) --
The date and time a resource was last backed up, in Unix format and Coordinated Universal Time (UTC). The value of LastBackupTime is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.





NextToken (string) --
The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.







Exceptions

Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'Results': [
            {
                'ResourceArn': 'string',
                'ResourceType': 'string',
                'LastBackupTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_recovery_points_by_backup_vault(BackupVaultName=None, NextToken=None, MaxResults=None, ByResourceArn=None, ByResourceType=None, ByBackupPlanId=None, ByCreatedBefore=None, ByCreatedAfter=None):
    """
    Returns detailed information about the recovery points stored in a backup vault.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_recovery_points_by_backup_vault(
        BackupVaultName='string',
        NextToken='string',
        MaxResults=123,
        ByResourceArn='string',
        ByResourceType='string',
        ByBackupPlanId='string',
        ByCreatedBefore=datetime(2015, 1, 1),
        ByCreatedAfter=datetime(2015, 1, 1)
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    :type NextToken: string
    :param NextToken: The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be returned.

    :type ByResourceArn: string
    :param ByResourceArn: Returns only recovery points that match the specified resource Amazon Resource Name (ARN).

    :type ByResourceType: string
    :param ByResourceType: Returns only recovery points that match the specified resource type.

    :type ByBackupPlanId: string
    :param ByBackupPlanId: Returns only recovery points that match the specified backup plan ID.

    :type ByCreatedBefore: datetime
    :param ByCreatedBefore: Returns only recovery points that were created before the specified timestamp.

    :type ByCreatedAfter: datetime
    :param ByCreatedAfter: Returns only recovery points that were created after the specified timestamp.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'RecoveryPoints': [
        {
            'RecoveryPointArn': 'string',
            'BackupVaultName': 'string',
            'BackupVaultArn': 'string',
            'ResourceArn': 'string',
            'ResourceType': 'string',
            'CreatedBy': {
                'BackupPlanId': 'string',
                'BackupPlanArn': 'string',
                'BackupPlanVersion': 'string',
                'BackupRuleId': 'string'
            },
            'IamRoleArn': 'string',
            'Status': 'COMPLETED'|'PARTIAL'|'DELETING'|'EXPIRED',
            'CreationDate': datetime(2015, 1, 1),
            'CompletionDate': datetime(2015, 1, 1),
            'BackupSizeInBytes': 123,
            'CalculatedLifecycle': {
                'MoveToColdStorageAt': datetime(2015, 1, 1),
                'DeleteAt': datetime(2015, 1, 1)
            },
            'Lifecycle': {
                'MoveToColdStorageAfterDays': 123,
                'DeleteAfterDays': 123
            },
            'EncryptionKeyArn': 'string',
            'IsEncrypted': True|False,
            'LastRestoreTime': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

RecoveryPoints (list) --
An array of objects that contain detailed information about recovery points saved in a backup vault.

(dict) --
Contains detailed information about the recovery points stored in a backup vault.

RecoveryPointArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .

BackupVaultName (string) --
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.

BackupVaultArn (string) --
An ARN that uniquely identifies a backup vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

ResourceArn (string) --
An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.

ResourceType (string) --
The type of AWS resource saved as a recovery point; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

CreatedBy (dict) --
Contains identifying information about the creation of a recovery point, including the BackupPlanArn , BackupPlanId , BackupPlanVersion , and BackupRuleId of the backup plan that is used to create it.

BackupPlanId (string) --
Uniquely identifies a backup plan.

BackupPlanArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50 .

BackupPlanVersion (string) --
Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.

BackupRuleId (string) --
Uniquely identifies a rule used to schedule the backup of a selection of resources.



IamRoleArn (string) --
Specifies the IAM role ARN used to create the target recovery point; for example, arn:aws:iam::123456789012:role/S3Access .

Status (string) --
A status code specifying the state of the recovery point.

CreationDate (datetime) --
The date and time a recovery point is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CompletionDate (datetime) --
The date and time a job to restore a recovery point is completed, in Unix format and Coordinated Universal Time (UTC). The value of CompletionDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

BackupSizeInBytes (integer) --
The size, in bytes, of a backup.

CalculatedLifecycle (dict) --
A CalculatedLifecycle object containing DeleteAt and MoveToColdStorageAt timestamps.

MoveToColdStorageAt (datetime) --
A timestamp that specifies when to transition a recovery point to cold storage.

DeleteAt (datetime) --
A timestamp that specifies when to delete a recovery point.



Lifecycle (dict) --
The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.
Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.

MoveToColdStorageAfterDays (integer) --
Specifies the number of days after creation that a recovery point is moved to cold storage.

DeleteAfterDays (integer) --
Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .



EncryptionKeyArn (string) --
The server-side encryption key that is used to protect your backups; for example, arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab .

IsEncrypted (boolean) --
A Boolean value that is returned as TRUE if the specified recovery point is encrypted, or FALSE if the recovery point is not encrypted.

LastRestoreTime (datetime) --
The date and time a recovery point was last restored, in Unix format and Coordinated Universal Time (UTC). The value of LastRestoreTime is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.











Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'NextToken': 'string',
        'RecoveryPoints': [
            {
                'RecoveryPointArn': 'string',
                'BackupVaultName': 'string',
                'BackupVaultArn': 'string',
                'ResourceArn': 'string',
                'ResourceType': 'string',
                'CreatedBy': {
                    'BackupPlanId': 'string',
                    'BackupPlanArn': 'string',
                    'BackupPlanVersion': 'string',
                    'BackupRuleId': 'string'
                },
                'IamRoleArn': 'string',
                'Status': 'COMPLETED'|'PARTIAL'|'DELETING'|'EXPIRED',
                'CreationDate': datetime(2015, 1, 1),
                'CompletionDate': datetime(2015, 1, 1),
                'BackupSizeInBytes': 123,
                'CalculatedLifecycle': {
                    'MoveToColdStorageAt': datetime(2015, 1, 1),
                    'DeleteAt': datetime(2015, 1, 1)
                },
                'Lifecycle': {
                    'MoveToColdStorageAfterDays': 123,
                    'DeleteAfterDays': 123
                },
                'EncryptionKeyArn': 'string',
                'IsEncrypted': True|False,
                'LastRestoreTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_recovery_points_by_resource(ResourceArn=None, NextToken=None, MaxResults=None):
    """
    Returns detailed information about recovery points of the type specified by a resource Amazon Resource Name (ARN).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_recovery_points_by_resource(
        ResourceArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nAn ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.\n

    :type NextToken: string
    :param NextToken: The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'RecoveryPoints': [
        {
            'RecoveryPointArn': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'Status': 'COMPLETED'|'PARTIAL'|'DELETING'|'EXPIRED',
            'EncryptionKeyArn': 'string',
            'BackupSizeBytes': 123,
            'BackupVaultName': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

RecoveryPoints (list) --
An array of objects that contain detailed information about recovery points of the specified resource type.

(dict) --
Contains detailed information about a saved recovery point.

RecoveryPointArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .

CreationDate (datetime) --
The date and time a recovery point is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Status (string) --
A status code specifying the state of the recovery point.

EncryptionKeyArn (string) --
The server-side encryption key that is used to protect your backups; for example, arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab .

BackupSizeBytes (integer) --
The size, in bytes, of a backup.

BackupVaultName (string) --
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.











Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'NextToken': 'string',
        'RecoveryPoints': [
            {
                'RecoveryPointArn': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'Status': 'COMPLETED'|'PARTIAL'|'DELETING'|'EXPIRED',
                'EncryptionKeyArn': 'string',
                'BackupSizeBytes': 123,
                'BackupVaultName': 'string'
            },
        ]
    }
    
    
    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_restore_jobs(NextToken=None, MaxResults=None):
    """
    Returns a list of jobs that AWS Backup initiated to restore a saved resource, including metadata about the recovery process.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_restore_jobs(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'RestoreJobs': [
        {
            'RestoreJobId': 'string',
            'RecoveryPointArn': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'CompletionDate': datetime(2015, 1, 1),
            'Status': 'PENDING'|'RUNNING'|'COMPLETED'|'ABORTED'|'FAILED',
            'StatusMessage': 'string',
            'PercentDone': 'string',
            'BackupSizeInBytes': 123,
            'IamRoleArn': 'string',
            'ExpectedCompletionTimeMinutes': 123,
            'CreatedResourceArn': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

RestoreJobs (list) --
An array of objects that contain detailed information about jobs to restore saved resources.

(dict) --
Contains metadata about a restore job.

RestoreJobId (string) --
Uniquely identifies the job that restores a recovery point.

RecoveryPointArn (string) --
An ARN that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .

CreationDate (datetime) --
The date and time a restore job is created, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CompletionDate (datetime) --
The date and time a job to restore a recovery point is completed, in Unix format and Coordinated Universal Time (UTC). The value of CompletionDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Status (string) --
A status code specifying the state of the job initiated by AWS Backup to restore a recovery point.

StatusMessage (string) --
A detailed message explaining the status of the job to restore a recovery point.

PercentDone (string) --
Contains an estimated percentage complete of a job at the time the job status was queried.

BackupSizeInBytes (integer) --
The size, in bytes, of the restored resource.

IamRoleArn (string) --
Specifies the IAM role ARN used to create the target recovery point; for example, arn:aws:iam::123456789012:role/S3Access .

ExpectedCompletionTimeMinutes (integer) --
The amount of time in minutes that a job restoring a recovery point is expected to take.

CreatedResourceArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.





NextToken (string) --
The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.







Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'RestoreJobs': [
            {
                'RestoreJobId': 'string',
                'RecoveryPointArn': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'CompletionDate': datetime(2015, 1, 1),
                'Status': 'PENDING'|'RUNNING'|'COMPLETED'|'ABORTED'|'FAILED',
                'StatusMessage': 'string',
                'PercentDone': 'string',
                'BackupSizeInBytes': 123,
                'IamRoleArn': 'string',
                'ExpectedCompletionTimeMinutes': 123,
                'CreatedResourceArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_tags(ResourceArn=None, NextToken=None, MaxResults=None):
    """
    Returns a list of key-value pairs assigned to a target recovery point, backup plan, or backup vault.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags(
        ResourceArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nAn Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the type of resource. Valid targets for ListTags are recovery points, backup plans, and backup vaults.\n

    :type NextToken: string
    :param NextToken: The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to be returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

NextToken (string) --
The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token.

Tags (dict) --
To help organize your resources, you can assign your own metadata to the resources you create. Each tag is a key-value pair.

(string) --
(string) --










Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'NextToken': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def put_backup_vault_access_policy(BackupVaultName=None, Policy=None):
    """
    Sets a resource-based policy that is used to manage access permissions on the target backup vault. Requires a backup vault name and an access policy document in JSON format.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_backup_vault_access_policy(
        BackupVaultName='string',
        Policy='string'
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    :type Policy: string
    :param Policy: The backup vault access policy document in JSON format.

    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def put_backup_vault_notifications(BackupVaultName=None, SNSTopicArn=None, BackupVaultEvents=None):
    """
    Turns on notifications on a backup vault for the specified topic and events.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_backup_vault_notifications(
        BackupVaultName='string',
        SNSTopicArn='string',
        BackupVaultEvents=[
            'BACKUP_JOB_STARTED'|'BACKUP_JOB_COMPLETED'|'BACKUP_JOB_SUCCESSFUL'|'BACKUP_JOB_FAILED'|'BACKUP_JOB_EXPIRED'|'RESTORE_JOB_STARTED'|'RESTORE_JOB_COMPLETED'|'RESTORE_JOB_SUCCESSFUL'|'RESTORE_JOB_FAILED'|'COPY_JOB_STARTED'|'COPY_JOB_SUCCESSFUL'|'COPY_JOB_FAILED'|'RECOVERY_POINT_MODIFIED'|'BACKUP_PLAN_CREATED'|'BACKUP_PLAN_MODIFIED',
        ]
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    :type SNSTopicArn: string
    :param SNSTopicArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that specifies the topic for a backup vault\xe2\x80\x99s events; for example, arn:aws:sns:us-west-2:111122223333:MyVaultTopic .\n

    :type BackupVaultEvents: list
    :param BackupVaultEvents: [REQUIRED]\nAn array of events that indicate the status of jobs to back up resources to the backup vault.\n\n(string) --\n\n

    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def start_backup_job(BackupVaultName=None, ResourceArn=None, IamRoleArn=None, IdempotencyToken=None, StartWindowMinutes=None, CompleteWindowMinutes=None, Lifecycle=None, RecoveryPointTags=None):
    """
    Starts a job to create a one-time backup of the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_backup_job(
        BackupVaultName='string',
        ResourceArn='string',
        IamRoleArn='string',
        IdempotencyToken='string',
        StartWindowMinutes=123,
        CompleteWindowMinutes=123,
        Lifecycle={
            'MoveToColdStorageAfterDays': 123,
            'DeleteAfterDays': 123
        },
        RecoveryPointTags={
            'string': 'string'
        }
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nAn Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.\n

    :type IamRoleArn: string
    :param IamRoleArn: [REQUIRED]\nSpecifies the IAM role ARN used to create the target recovery point; for example, arn:aws:iam::123456789012:role/S3Access .\n

    :type IdempotencyToken: string
    :param IdempotencyToken: A customer chosen string that can be used to distinguish between calls to StartBackupJob .

    :type StartWindowMinutes: integer
    :param StartWindowMinutes: A value in minutes after a backup is scheduled before a job will be canceled if it doesn\'t start successfully. This value is optional.

    :type CompleteWindowMinutes: integer
    :param CompleteWindowMinutes: A value in minutes after a backup job is successfully started before it must be completed or it will be canceled by AWS Backup. This value is optional.

    :type Lifecycle: dict
    :param Lifecycle: The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup will transition and expire backups automatically according to the lifecycle that you define.\nBackups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.\n\nMoveToColdStorageAfterDays (integer) --Specifies the number of days after creation that a recovery point is moved to cold storage.\n\nDeleteAfterDays (integer) --Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .\n\n\n

    :type RecoveryPointTags: dict
    :param RecoveryPointTags: To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'BackupJobId': 'string',
    'RecoveryPointArn': 'string',
    'CreationDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

BackupJobId (string) --
Uniquely identifies a request to AWS Backup to back up a resource.

RecoveryPointArn (string) --
An ARN that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .

CreationDate (datetime) --
The date and time that a backup job is started, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.







Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException
Backup.Client.exceptions.LimitExceededException


    :return: {
        'BackupJobId': 'string',
        'RecoveryPointArn': 'string',
        'CreationDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    Backup.Client.exceptions.LimitExceededException
    
    """
    pass

def start_copy_job(RecoveryPointArn=None, SourceBackupVaultName=None, DestinationBackupVaultArn=None, IamRoleArn=None, IdempotencyToken=None, Lifecycle=None):
    """
    Starts a job to create a one-time copy of the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_copy_job(
        RecoveryPointArn='string',
        SourceBackupVaultName='string',
        DestinationBackupVaultArn='string',
        IamRoleArn='string',
        IdempotencyToken='string',
        Lifecycle={
            'MoveToColdStorageAfterDays': 123,
            'DeleteAfterDays': 123
        }
    )
    
    
    :type RecoveryPointArn: string
    :param RecoveryPointArn: [REQUIRED]\nAn ARN that uniquely identifies a recovery point to use for the copy job; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45.\n

    :type SourceBackupVaultName: string
    :param SourceBackupVaultName: [REQUIRED]\nThe name of a logical source container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    :type DestinationBackupVaultArn: string
    :param DestinationBackupVaultArn: [REQUIRED]\nAn Amazon Resource Name (ARN) that uniquely identifies a destination backup vault to copy to; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .\n

    :type IamRoleArn: string
    :param IamRoleArn: [REQUIRED]\nSpecifies the IAM role ARN used to copy the target recovery point; for example, arn:aws:iam::123456789012:role/S3Access .\n

    :type IdempotencyToken: string
    :param IdempotencyToken: A customer chosen string that can be used to distinguish between calls to StartCopyJob .

    :type Lifecycle: dict
    :param Lifecycle: Contains an array of Transition objects specifying how long in days before a recovery point transitions to cold storage or is deleted.\nBackups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, on the console, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.\n\nMoveToColdStorageAfterDays (integer) --Specifies the number of days after creation that a recovery point is moved to cold storage.\n\nDeleteAfterDays (integer) --Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CopyJobId': 'string',
    'CreationDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

CopyJobId (string) --
Uniquely identifies a copy job.

CreationDate (datetime) --
The date and time that a copy job is started, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.







Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException
Backup.Client.exceptions.LimitExceededException


    :return: {
        'CopyJobId': 'string',
        'CreationDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    Backup.Client.exceptions.LimitExceededException
    
    """
    pass

def start_restore_job(RecoveryPointArn=None, Metadata=None, IamRoleArn=None, IdempotencyToken=None, ResourceType=None):
    """
    Recovers the saved resource identified by an Amazon Resource Name (ARN).
    If the resource ARN is included in the request, then the last complete backup of that resource is recovered. If the ARN of a recovery point is supplied, then that recovery point is restored.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_restore_job(
        RecoveryPointArn='string',
        Metadata={
            'string': 'string'
        },
        IamRoleArn='string',
        IdempotencyToken='string',
        ResourceType='string'
    )
    
    
    :type RecoveryPointArn: string
    :param RecoveryPointArn: [REQUIRED]\nAn ARN that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .\n

    :type Metadata: dict
    :param Metadata: [REQUIRED]\nA set of metadata key-value pairs. Contains information, such as a resource name, required to restore a recovery point.\nYou can get configuration metadata about a resource at the time it was backed up by calling GetRecoveryPointRestoreMetadata . However, values in addition to those provided by GetRecoveryPointRestoreMetadata might be required to restore a resource. For example, you might need to provide a new resource name if the original already exists.\nYou need to specify specific metadata to restore an Amazon Elastic File System (Amazon EFS) instance:\n\nfile-system-id : ID of the Amazon EFS file system that is backed up by AWS Backup. Returned in GetRecoveryPointRestoreMetadata .\nEncrypted : A Boolean value that, if true, specifies that the file system is encrypted. If KmsKeyId is specified, Encrypted must be set to true .\nKmsKeyId : Specifies the AWS KMS key that is used to encrypt the restored file system.\nPerformanceMode : Specifies the throughput mode of the file system.\nCreationToken : A user-supplied value that ensures the uniqueness (idempotency) of the request.\nnewFileSystem : A Boolean value that, if true, specifies that the recovery point is restored to a new Amazon EFS file system.\n\n\n(string) --\n(string) --\n\n\n\n

    :type IamRoleArn: string
    :param IamRoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM role that AWS Backup uses to create the target recovery point; for example, arn:aws:iam::123456789012:role/S3Access .\n

    :type IdempotencyToken: string
    :param IdempotencyToken: A customer chosen string that can be used to distinguish between calls to StartRestoreJob .

    :type ResourceType: string
    :param ResourceType: Starts a job to restore a recovery point for one of the following resources:\n\nEBS for Amazon Elastic Block Store\nStorage Gateway for AWS Storage Gateway\nRDS for Amazon Relational Database Service\nDDB for Amazon DynamoDB\nEFS for Amazon Elastic File System\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RestoreJobId': 'string'
}


Response Structure

(dict) --

RestoreJobId (string) --
Uniquely identifies the job that restores a recovery point.







Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'RestoreJobId': 'string'
    }
    
    
    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def stop_backup_job(BackupJobId=None):
    """
    Attempts to cancel a job to create a one-time backup of a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_backup_job(
        BackupJobId='string'
    )
    
    
    :type BackupJobId: string
    :param BackupJobId: [REQUIRED]\nUniquely identifies a request to AWS Backup to back up a resource.\n

    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Assigns a set of key-value pairs to a recovery point, backup plan, or backup vault identified by an Amazon Resource Name (ARN).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nAn ARN that uniquely identifies a resource. The format of the ARN depends on the type of the tagged resource.\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nKey-value pairs that are used to help organize your resources. You can assign your own metadata to the resources you create.\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    Backup.Client.exceptions.LimitExceededException
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeyList=None):
    """
    Removes a set of key-value pairs from a recovery point, backup plan, or backup vault identified by an Amazon Resource Name (ARN)
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeyList=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nAn ARN that uniquely identifies a resource. The format of the ARN depends on the type of the tagged resource.\n

    :type TagKeyList: list
    :param TagKeyList: [REQUIRED]\nA list of keys to identify which key-value tags to remove from a resource.\n\n(string) --\n\n

    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def update_backup_plan(BackupPlanId=None, BackupPlan=None):
    """
    Replaces the body of a saved backup plan identified by its backupPlanId with the input document in JSON format. The new version is uniquely identified by a VersionId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_backup_plan(
        BackupPlanId='string',
        BackupPlan={
            'BackupPlanName': 'string',
            'Rules': [
                {
                    'RuleName': 'string',
                    'TargetBackupVaultName': 'string',
                    'ScheduleExpression': 'string',
                    'StartWindowMinutes': 123,
                    'CompletionWindowMinutes': 123,
                    'Lifecycle': {
                        'MoveToColdStorageAfterDays': 123,
                        'DeleteAfterDays': 123
                    },
                    'RecoveryPointTags': {
                        'string': 'string'
                    },
                    'CopyActions': [
                        {
                            'Lifecycle': {
                                'MoveToColdStorageAfterDays': 123,
                                'DeleteAfterDays': 123
                            },
                            'DestinationBackupVaultArn': 'string'
                        },
                    ]
                },
            ]
        }
    )
    
    
    :type BackupPlanId: string
    :param BackupPlanId: [REQUIRED]\nUniquely identifies a backup plan.\n

    :type BackupPlan: dict
    :param BackupPlan: [REQUIRED]\nSpecifies the body of a backup plan. Includes a BackupPlanName and one or more sets of Rules .\n\nBackupPlanName (string) -- [REQUIRED]The display name of a backup plan.\n\nRules (list) -- [REQUIRED]An array of BackupRule objects, each of which specifies a scheduled task that is used to back up a selection of resources.\n\n(dict) --Specifies a scheduled task used to back up a selection of resources.\n\nRuleName (string) -- [REQUIRED]An optional display name for a backup rule.\n\nTargetBackupVaultName (string) -- [REQUIRED]The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n\nScheduleExpression (string) --A CRON expression specifying when AWS Backup initiates a backup job.\n\nStartWindowMinutes (integer) --A value in minutes after a backup is scheduled before a job will be canceled if it doesn\'t start successfully. This value is optional.\n\nCompletionWindowMinutes (integer) --A value in minutes after a backup job is successfully started before it must be completed or it will be canceled by AWS Backup. This value is optional.\n\nLifecycle (dict) --The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup will transition and expire backups automatically according to the lifecycle that you define.\nBackups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.\n\nMoveToColdStorageAfterDays (integer) --Specifies the number of days after creation that a recovery point is moved to cold storage.\n\nDeleteAfterDays (integer) --Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .\n\n\n\nRecoveryPointTags (dict) --To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair.\n\n(string) --\n(string) --\n\n\n\n\nCopyActions (list) --An array of CopyAction objects, which contains the details of the copy operation.\n\n(dict) --The details of the copy operation.\n\nLifecycle (dict) --Contains an array of Transition objects specifying how long in days before a recovery point transitions to cold storage or is deleted.\nBackups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, on the console, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.\n\nMoveToColdStorageAfterDays (integer) --Specifies the number of days after creation that a recovery point is moved to cold storage.\n\nDeleteAfterDays (integer) --Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .\n\n\n\nDestinationBackupVaultArn (string) -- [REQUIRED]An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup. For example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .\n\n\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'BackupPlanId': 'string',
    'BackupPlanArn': 'string',
    'CreationDate': datetime(2015, 1, 1),
    'VersionId': 'string'
}


Response Structure

(dict) --

BackupPlanId (string) --
Uniquely identifies a backup plan.

BackupPlanArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50 .

CreationDate (datetime) --
The date and time a backup plan is updated, in Unix format and Coordinated Universal Time (UTC). The value of CreationDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

VersionId (string) --
Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version Ids cannot be edited.







Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'BackupPlanId': 'string',
        'BackupPlanArn': 'string',
        'CreationDate': datetime(2015, 1, 1),
        'VersionId': 'string'
    }
    
    
    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def update_recovery_point_lifecycle(BackupVaultName=None, RecoveryPointArn=None, Lifecycle=None):
    """
    Sets the transition lifecycle of a recovery point.
    The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.
    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_recovery_point_lifecycle(
        BackupVaultName='string',
        RecoveryPointArn='string',
        Lifecycle={
            'MoveToColdStorageAfterDays': 123,
            'DeleteAfterDays': 123
        }
    )
    
    
    :type BackupVaultName: string
    :param BackupVaultName: [REQUIRED]\nThe name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.\n

    :type RecoveryPointArn: string
    :param RecoveryPointArn: [REQUIRED]\nAn Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .\n

    :type Lifecycle: dict
    :param Lifecycle: The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.\nBackups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.\n\nMoveToColdStorageAfterDays (integer) --Specifies the number of days after creation that a recovery point is moved to cold storage.\n\nDeleteAfterDays (integer) --Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'BackupVaultArn': 'string',
    'RecoveryPointArn': 'string',
    'Lifecycle': {
        'MoveToColdStorageAfterDays': 123,
        'DeleteAfterDays': 123
    },
    'CalculatedLifecycle': {
        'MoveToColdStorageAt': datetime(2015, 1, 1),
        'DeleteAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

BackupVaultArn (string) --
An ARN that uniquely identifies a backup vault; for example, arn:aws:backup:us-east-1:123456789012:vault:aBackupVault .

RecoveryPointArn (string) --
An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 .

Lifecycle (dict) --
The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.
Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the \xe2\x80\x9cexpire after days\xe2\x80\x9d setting must be 90 days greater than the \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting. The \xe2\x80\x9ctransition to cold after days\xe2\x80\x9d setting cannot be changed after a backup has been transitioned to cold.

MoveToColdStorageAfterDays (integer) --
Specifies the number of days after creation that a recovery point is moved to cold storage.

DeleteAfterDays (integer) --
Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus MoveToColdStorageAfterDays .



CalculatedLifecycle (dict) --
A CalculatedLifecycle object containing DeleteAt and MoveToColdStorageAt timestamps.

MoveToColdStorageAt (datetime) --
A timestamp that specifies when to transition a recovery point to cold storage.

DeleteAt (datetime) --
A timestamp that specifies when to delete a recovery point.









Exceptions

Backup.Client.exceptions.ResourceNotFoundException
Backup.Client.exceptions.InvalidParameterValueException
Backup.Client.exceptions.MissingParameterValueException
Backup.Client.exceptions.ServiceUnavailableException


    :return: {
        'BackupVaultArn': 'string',
        'RecoveryPointArn': 'string',
        'Lifecycle': {
            'MoveToColdStorageAfterDays': 123,
            'DeleteAfterDays': 123
        },
        'CalculatedLifecycle': {
            'MoveToColdStorageAt': datetime(2015, 1, 1),
            'DeleteAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Backup.Client.exceptions.ResourceNotFoundException
    Backup.Client.exceptions.InvalidParameterValueException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def update_region_settings(ResourceTypeOptInPreference=None):
    """
    Updates the current service opt-in settings for the region. If the service has a value set to true, AWS Backup will attempt to protect that service\'s resources in this region, when included in an on-demand backup or scheduled backup plan. If the value is set to false for a service, AWS Backup will not attempt to protect that service\'s resources in this region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_region_settings(
        ResourceTypeOptInPreference={
            'string': True|False
        }
    )
    
    
    :type ResourceTypeOptInPreference: dict
    :param ResourceTypeOptInPreference: Updates the list of services along with the opt-in preferences for the region.\n\n(string) --\n(boolean) --\n\n\n\n

    :returns: 
    Backup.Client.exceptions.ServiceUnavailableException
    Backup.Client.exceptions.MissingParameterValueException
    Backup.Client.exceptions.InvalidParameterValueException
    
    """
    pass

