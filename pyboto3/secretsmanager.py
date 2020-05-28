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

def cancel_rotate_secret(SecretId=None):
    """
    Disables automatic scheduled rotation and cancels the rotation of a secret if one is currently in progress.
    To re-enable scheduled rotation, call  RotateSecret with AutomaticallyRotateAfterDays set to a value greater than 0. This will immediately rotate your secret and then enable the automatic schedule.
    To successfully start a rotation, the staging label AWSPENDING must be in one of the following states:
    If the staging label AWSPENDING is attached to a different version than the version with AWSCURRENT then the attempt to rotate fails.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to cancel rotation for a secret. The operation sets the RotationEnabled field to false and cancels all scheduled rotations. To resume scheduled rotations, you must re-enable rotation by calling the rotate-secret operation.
    Expected Output:
    
    :example: response = client.cancel_rotate_secret(
        SecretId='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nSpecifies the secret for which you want to cancel a rotation request. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'ARN': 'string',
    'Name': 'string',
    'VersionId': 'string'
}


Response Structure

(dict) --
ARN (string) --The ARN of the secret for which rotation was canceled.

Name (string) --The friendly name of the secret for which rotation was canceled.

VersionId (string) --The unique identifier of the version of the secret that was created during the rotation. This version might not be complete, and should be evaluated for possible deletion. At the very least, you should remove the VersionStage value AWSPENDING to enable this version to be deleted. Failing to clean up a cancelled rotation can block you from successfully starting future rotations.






Exceptions

SecretsManager.Client.exceptions.ResourceNotFoundException
SecretsManager.Client.exceptions.InvalidParameterException
SecretsManager.Client.exceptions.InternalServiceError
SecretsManager.Client.exceptions.InvalidRequestException

Examples
The following example shows how to cancel rotation for a secret. The operation sets the RotationEnabled field to false and cancels all scheduled rotations. To resume scheduled rotations, you must re-enable rotation by calling the rotate-secret operation.
response = client.cancel_rotate_secret(
    SecretId='MyTestDatabaseSecret',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Name': 'Name',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ARN': 'string',
        'Name': 'string',
        'VersionId': 'string'
    }
    
    
    :returns: 
    secretsmanager:CancelRotateSecret
    
    """
    pass

def create_secret(Name=None, ClientRequestToken=None, Description=None, KmsKeyId=None, SecretBinary=None, SecretString=None, Tags=None):
    """
    Creates a new secret. A secret in Secrets Manager consists of both the protected secret data and the important information needed to manage the secret.
    Secrets Manager stores the encrypted secret data in one of a collection of "versions" associated with the secret. Each version contains a copy of the encrypted secret data. Each version is associated with one or more "staging labels" that identify where the version is in the rotation cycle. The SecretVersionsToStages field of the secret contains the mapping of staging labels to the active versions of the secret. Versions without a staging label are considered deprecated and are not included in the list.
    You provide the secret data to be encrypted by putting text in either the SecretString parameter or binary data in the SecretBinary parameter, but not both. If you include SecretString or SecretBinary then Secrets Manager also creates an initial secret version and automatically attaches the staging label AWSCURRENT to the new version.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to create a secret. The credentials stored in the encrypted secret value are retrieved from a file on disk named mycreds.json.
    Expected Output:
    
    :example: response = client.create_secret(
        Name='string',
        ClientRequestToken='string',
        Description='string',
        KmsKeyId='string',
        SecretBinary=b'bytes',
        SecretString='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nSpecifies the friendly name of the new secret.\nThe secret name must be ASCII letters, digits, or the following characters : /_+=.@-\n\nNote\nDon\'t end your secret name with a hyphen followed by six characters. If you do so, you risk confusion and unexpected results when searching for a secret by partial ARN. This is because Secrets Manager automatically adds a hyphen and six random characters at the end of the ARN.\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) If you include SecretString or SecretBinary , then an initial version is created as part of the secret, and this parameter specifies a unique identifier for the new version.\n\nNote\nIf you use the AWS CLI or one of the AWS SDK to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request. If you don\'t use the SDK and instead generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a ClientRequestToken yourself for the new version and include that value in the request.\n\nThis value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a UUID-type value to ensure uniqueness of your versions within the specified secret.\n\nIf the ClientRequestToken value isn\'t already associated with a version of the secret then a new version of the secret is created.\nIf a version with this value already exists and that version\'s SecretString and SecretBinary values are the same as those in the request, then the request is ignored (the operation is idempotent).\nIf a version with this value already exists and that version\'s SecretString and SecretBinary values are different from those in the request then the request fails because you cannot modify an existing version. Instead, use PutSecretValue to create a new version.\n\nThis value becomes the VersionId of the new version.\nThis field is autopopulated if not provided.\n

    :type Description: string
    :param Description: (Optional) Specifies a user-provided description of the secret.

    :type KmsKeyId: string
    :param KmsKeyId: (Optional) Specifies the ARN, Key ID, or alias of the AWS KMS customer master key (CMK) to be used to encrypt the SecretString or SecretBinary values in the versions stored in this secret.\nYou can specify any of the supported ways to identify a AWS KMS key ID. If you need to reference a CMK in a different account, you can use only the key ARN or the alias ARN.\nIf you don\'t specify this value, then Secrets Manager defaults to using the AWS account\'s default CMK (the one named aws/secretsmanager ). If a AWS KMS CMK with that name doesn\'t yet exist, then Secrets Manager creates it for you automatically the first time it needs to encrypt a version\'s SecretString or SecretBinary fields.\n\nWarning\nYou can use the account\'s default CMK to encrypt and decrypt only if you call this operation using credentials from the same account that owns the secret. If the secret is in a different account, then you must create a custom CMK and specify the ARN in this field.\n\n

    :type SecretBinary: bytes
    :param SecretBinary: (Optional) Specifies binary data that you want to encrypt and store in the new version of the secret. To use this parameter in the command-line tools, we recommend that you store your binary data in a file and then use the appropriate technique for your tool to pass the contents of the file as a parameter.\nEither SecretString or SecretBinary must have a value, but not both. They cannot both be empty.\nThis parameter is not available using the Secrets Manager console. It can be accessed only by using the AWS CLI or one of the AWS SDKs.\n

    :type SecretString: string
    :param SecretString: (Optional) Specifies text data that you want to encrypt and store in this new version of the secret.\nEither SecretString or SecretBinary must have a value, but not both. They cannot both be empty.\nIf you create a secret by using the Secrets Manager console then Secrets Manager puts the protected secret text in only the SecretString parameter. The Secrets Manager console stores the information as a JSON structure of key/value pairs that the Lambda rotation function knows how to parse.\nFor storing multiple values, we recommend that you use a JSON text string argument and specify key/value pairs. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide . For example:\n\n[{'username':'bob'},{'password':'abc123xyz456'}]\nIf your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text.\n

    :type Tags: list
    :param Tags: (Optional) Specifies a list of user-defined tags that are attached to the secret. Each tag is a 'Key' and 'Value' pair of strings. This operation only appends tags to the existing list of tags. To remove tags, you must use UntagResource .\n\nWarning\n\nSecrets Manager tag key names are case sensitive. A tag with the key 'ABC' is a different tag from one with key 'abc'.\nIf you check tags in IAM policy Condition elements as part of your security strategy, then adding or removing a tag can change permissions. If the successful completion of this operation would result in you losing your permissions for this secret, then this operation is blocked and returns an Access Denied error.\n\n\nThis parameter requires a JSON text string argument. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide . For example:\n\n[{'Key':'CostCenter','Value':'12345'},{'Key':'environment','Value':'production'}]\nIf your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text.\nThe following basic restrictions apply to tags:\n\nMaximum number of tags per secret\xe2\x80\x9450\nMaximum key length\xe2\x80\x94127 Unicode characters in UTF-8\nMaximum value length\xe2\x80\x94255 Unicode characters in UTF-8\nTag keys and values are case sensitive.\nDo not use the aws: prefix in your tag names or values because it is reserved for AWS use. You can\'t edit or delete tag names or values with this prefix. Tags with this prefix do not count against your tags per secret limit.\nIf your tagging schema will be used across multiple services and resources, remember that other services might have restrictions on allowed characters. Generally allowed characters are: letters, spaces, and numbers representable in UTF-8, plus the following special characters: + - = . _ : / @.\n\n\n(dict) --A structure that contains information about a tag.\n\nKey (string) --The key identifier, or name, of the tag.\n\nValue (string) --The string value that\'s associated with the key of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ARN': 'string',
    'Name': 'string',
    'VersionId': 'string'
}


Response Structure

(dict) --

ARN (string) --
The Amazon Resource Name (ARN) of the secret that you just created.

Note
Secrets Manager automatically adds several random characters to the name at the end of the ARN when you initially create a secret. This affects only the ARN and not the actual friendly name. This ensures that if you create a new secret with the same name as an old secret that you previously deleted, then users with access to the old secret don\'t automatically get access to the new secret because the ARNs are different.


Name (string) --
The friendly name of the secret that you just created.

VersionId (string) --
The unique identifier that\'s associated with the version of the secret you just created.







Exceptions

SecretsManager.Client.exceptions.InvalidParameterException
SecretsManager.Client.exceptions.InvalidRequestException
SecretsManager.Client.exceptions.LimitExceededException
SecretsManager.Client.exceptions.EncryptionFailure
SecretsManager.Client.exceptions.ResourceExistsException
SecretsManager.Client.exceptions.ResourceNotFoundException
SecretsManager.Client.exceptions.MalformedPolicyDocumentException
SecretsManager.Client.exceptions.InternalServiceError
SecretsManager.Client.exceptions.PreconditionNotMetException

Examples
The following example shows how to create a secret. The credentials stored in the encrypted secret value are retrieved from a file on disk named mycreds.json.
response = client.create_secret(
    ClientRequestToken='EXAMPLE1-90ab-cdef-fedc-ba987SECRET1',
    Description='My test database secret created with the CLI',
    Name='MyTestDatabaseSecret',
    SecretString='{"username":"david","password":"BnQw!XDWgaEeT9XGTT29"}',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Name': 'MyTestDatabaseSecret',
    'VersionId': 'EXAMPLE1-90ab-cdef-fedc-ba987SECRET1',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ARN': 'string',
        'Name': 'string',
        'VersionId': 'string'
    }
    
    
    :returns: 
    secretsmanager:CreateSecret
    kms:GenerateDataKey - needed only if you use a customer-managed AWS KMS key to encrypt the secret. You do not need this permission to use the account\'s default AWS managed CMK for Secrets Manager.
    kms:Decrypt - needed only if you use a customer-managed AWS KMS key to encrypt the secret. You do not need this permission to use the account\'s default AWS managed CMK for Secrets Manager.
    secretsmanager:TagResource - needed only if you include the Tags parameter.
    
    """
    pass

def delete_resource_policy(SecretId=None):
    """
    Deletes the resource-based permission policy that\'s attached to the secret.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to delete the resource-based policy that is attached to a secret.
    Expected Output:
    
    :example: response = client.delete_resource_policy(
        SecretId='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nSpecifies the secret that you want to delete the attached resource-based policy for. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'ARN': 'string',
    'Name': 'string'
}


Response Structure

(dict) --
ARN (string) --The ARN of the secret that the resource-based policy was deleted for.

Name (string) --The friendly name of the secret that the resource-based policy was deleted for.






Exceptions

SecretsManager.Client.exceptions.ResourceNotFoundException
SecretsManager.Client.exceptions.InternalServiceError
SecretsManager.Client.exceptions.InvalidRequestException

Examples
The following example shows how to delete the resource-based policy that is attached to a secret.
response = client.delete_resource_policy(
    SecretId='MyTestDatabaseSecret',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseMasterSecret-a1b2c3',
    'Name': 'MyTestDatabaseSecret',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ARN': 'string',
        'Name': 'string'
    }
    
    
    :returns: 
    To attach a resource policy to a secret, use  PutResourcePolicy .
    To retrieve the current resource-based policy that\'s attached to a secret, use  GetResourcePolicy .
    To list all of the currently available secrets, use  ListSecrets .
    
    """
    pass

def delete_secret(SecretId=None, RecoveryWindowInDays=None, ForceDeleteWithoutRecovery=None):
    """
    Deletes an entire secret and all of its versions. You can optionally include a recovery window during which you can restore the secret. If you don\'t specify a recovery window value, the operation defaults to 30 days. Secrets Manager attaches a DeletionDate stamp to the secret that specifies the end of the recovery window. At the end of the recovery window, Secrets Manager deletes the secret permanently.
    At any time before recovery window ends, you can use  RestoreSecret to remove the DeletionDate and cancel the deletion of the secret.
    You cannot access the encrypted secret information in any secret that is scheduled for deletion. If you need to access that information, you must cancel the deletion with  RestoreSecret and then retrieve the information.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to delete a secret. The secret stays in your account in a deprecated and inaccessible state until the recovery window ends. After the date and time in the DeletionDate response field has passed, you can no longer recover this secret with restore-secret.
    Expected Output:
    
    :example: response = client.delete_secret(
        SecretId='string',
        RecoveryWindowInDays=123,
        ForceDeleteWithoutRecovery=True|False
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nSpecifies the secret that you want to delete. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :type RecoveryWindowInDays: integer
    :param RecoveryWindowInDays: (Optional) Specifies the number of days that Secrets Manager waits before it can delete the secret. You can\'t use both this parameter and the ForceDeleteWithoutRecovery parameter in the same API call.\nThis value can range from 7 to 30 days. The default value is 30.\n

    :type ForceDeleteWithoutRecovery: boolean
    :param ForceDeleteWithoutRecovery: (Optional) Specifies that the secret is to be deleted without any recovery window. You can\'t use both this parameter and the RecoveryWindowInDays parameter in the same API call.\nAn asynchronous background process performs the actual deletion, so there can be a short delay before the operation completes. If you write code to delete and then immediately recreate a secret with the same name, ensure that your code includes appropriate back off and retry logic.\n\nWarning\nUse this parameter with caution. This parameter causes the operation to skip the normal waiting period before the permanent deletion that AWS would normally impose with the RecoveryWindowInDays parameter. If you delete a secret with the ForceDeleteWithouRecovery parameter, then you have no opportunity to recover the secret. It is permanently lost.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ARN': 'string',
    'Name': 'string',
    'DeletionDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

ARN (string) --
The ARN of the secret that is now scheduled for deletion.

Name (string) --
The friendly name of the secret that is now scheduled for deletion.

DeletionDate (datetime) --
The date and time after which this secret can be deleted by Secrets Manager and can no longer be restored. This value is the date and time of the delete request plus the number of days specified in RecoveryWindowInDays .







Exceptions

SecretsManager.Client.exceptions.ResourceNotFoundException
SecretsManager.Client.exceptions.InvalidParameterException
SecretsManager.Client.exceptions.InvalidRequestException
SecretsManager.Client.exceptions.InternalServiceError

Examples
The following example shows how to delete a secret. The secret stays in your account in a deprecated and inaccessible state until the recovery window ends. After the date and time in the DeletionDate response field has passed, you can no longer recover this secret with restore-secret.
response = client.delete_secret(
    RecoveryWindowInDays=7,
    SecretId='MyTestDatabaseSecret1',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'DeletionDate': datetime(2018, 4, 18, 21, 2, 29, 2, 108, 0),
    'Name': 'MyTestDatabaseSecret',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ARN': 'string',
        'Name': 'string',
        'DeletionDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    secretsmanager:DeleteSecret
    
    """
    pass

def describe_secret(SecretId=None):
    """
    Retrieves the details of a secret. It does not include the encrypted fields. Only those fields that are populated with a value are returned in the response.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to get the details about a secret.
    Expected Output:
    
    :example: response = client.describe_secret(
        SecretId='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nThe identifier of the secret whose details you want to retrieve. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'ARN': 'string',
    'Name': 'string',
    'Description': 'string',
    'KmsKeyId': 'string',
    'RotationEnabled': True|False,
    'RotationLambdaARN': 'string',
    'RotationRules': {
        'AutomaticallyAfterDays': 123
    },
    'LastRotatedDate': datetime(2015, 1, 1),
    'LastChangedDate': datetime(2015, 1, 1),
    'LastAccessedDate': datetime(2015, 1, 1),
    'DeletedDate': datetime(2015, 1, 1),
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'VersionIdsToStages': {
        'string': [
            'string',
        ]
    },
    'OwningService': 'string'
}


Response Structure

(dict) --
ARN (string) --The ARN of the secret.

Name (string) --The user-provided friendly name of the secret.

Description (string) --The user-provided description of the secret.

KmsKeyId (string) --The ARN or alias of the AWS KMS customer master key (CMK) that\'s used to encrypt the SecretString or SecretBinary fields in each version of the secret. If you don\'t provide a key, then Secrets Manager defaults to encrypting the secret fields with the default AWS KMS CMK (the one named awssecretsmanager ) for this account.

RotationEnabled (boolean) --Specifies whether automatic rotation is enabled for this secret.
To enable rotation, use  RotateSecret with AutomaticallyRotateAfterDays set to a value greater than 0. To disable rotation, use  CancelRotateSecret .

RotationLambdaARN (string) --The ARN of a Lambda function that\'s invoked by Secrets Manager to rotate the secret either automatically per the schedule or manually by a call to RotateSecret .

RotationRules (dict) --A structure that contains the rotation configuration for this secret.

AutomaticallyAfterDays (integer) --Specifies the number of days between automatic scheduled rotations of the secret.
Secrets Manager schedules the next rotation when the previous one is complete. Secrets Manager schedules the date by adding the rotation interval (number of days) to the actual date of the last rotation. The service chooses the hour within that 24-hour date window randomly. The minute is also chosen somewhat randomly, but weighted towards the top of the hour and influenced by a variety of factors that help distribute load.



LastRotatedDate (datetime) --The most recent date and time that the Secrets Manager rotation process was successfully completed. This value is null if the secret has never rotated.

LastChangedDate (datetime) --The last date and time that this secret was modified in any way.

LastAccessedDate (datetime) --The last date that this secret was accessed. This value is truncated to midnight of the date and therefore shows only the date, not the time.

DeletedDate (datetime) --This value exists if the secret is scheduled for deletion. Some time after the specified date and time, Secrets Manager deletes the secret and all of its versions.
If a secret is scheduled for deletion, then its details, including the encrypted secret information, is not accessible. To cancel a scheduled deletion and restore access, use  RestoreSecret .

Tags (list) --The list of user-defined tags that are associated with the secret. To add tags to a secret, use  TagResource . To remove tags, use  UntagResource .

(dict) --A structure that contains information about a tag.

Key (string) --The key identifier, or name, of the tag.

Value (string) --The string value that\'s associated with the key of the tag.





VersionIdsToStages (dict) --A list of all of the currently assigned VersionStage staging labels and the VersionId that each is attached to. Staging labels are used to keep track of the different versions during the rotation process.

Note
A version that does not have any staging labels attached is considered deprecated and subject to deletion. Such versions are not included in this list.


(string) --
(list) --
(string) --






OwningService (string) --Returns the name of the service that created this secret.






Exceptions

SecretsManager.Client.exceptions.ResourceNotFoundException
SecretsManager.Client.exceptions.InternalServiceError

Examples
The following example shows how to get the details about a secret.
response = client.describe_secret(
    SecretId='MyTestDatabaseSecret',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Description': 'My test database secret',
    'KmsKeyId': 'arn:aws:kms:us-west-2:123456789012:key/EXAMPLE1-90ab-cdef-fedc-ba987KMSKEY1',
    'LastAccessedDate': datetime(2018, 4, 17, 0, 0, 0, 1, 107, 0),
    'LastChangedDate': 1523477145.729,
    'LastRotatedDate': 1525747253.72,
    'Name': 'MyTestDatabaseSecret',
    'RotationEnabled': True,
    'RotationLambdaARN': 'arn:aws:lambda:us-west-2:123456789012:function:MyTestRotationLambda',
    'RotationRules': {
        'AutomaticallyAfterDays': 30,
    },
    'Tags': [
        {
            'Key': 'SecondTag',
            'Value': 'AnotherValue',
        },
        {
            'Key': 'FirstTag',
            'Value': 'SomeValue',
        },
    ],
    'VersionIdsToStages': {
        'EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE': [
            'AWSPREVIOUS',
        ],
        'EXAMPLE2-90ab-cdef-fedc-ba987EXAMPLE': [
            'AWSCURRENT',
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ARN': 'string',
        'Name': 'string',
        'Description': 'string',
        'KmsKeyId': 'string',
        'RotationEnabled': True|False,
        'RotationLambdaARN': 'string',
        'RotationRules': {
            'AutomaticallyAfterDays': 123
        },
        'LastRotatedDate': datetime(2015, 1, 1),
        'LastChangedDate': datetime(2015, 1, 1),
        'LastAccessedDate': datetime(2015, 1, 1),
        'DeletedDate': datetime(2015, 1, 1),
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'VersionIdsToStages': {
            'string': [
                'string',
            ]
        },
        'OwningService': 'string'
    }
    
    
    :returns: 
    To create a secret, use  CreateSecret .
    To modify a secret, use  UpdateSecret .
    To retrieve the encrypted secret information in a version of the secret, use  GetSecretValue .
    To list all of the secrets in the AWS account, use  ListSecrets .
    
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

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
ReturnsA paginator object.


    """
    pass

def get_random_password(PasswordLength=None, ExcludeCharacters=None, ExcludeNumbers=None, ExcludePunctuation=None, ExcludeUppercase=None, ExcludeLowercase=None, IncludeSpace=None, RequireEachIncludedType=None):
    """
    Generates a random password of the specified complexity. This operation is intended for use in the Lambda rotation function. Per best practice, we recommend that you specify the maximum length and include every character type that the system you are generating a password for can support.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to request a randomly generated password. This example includes the optional flags to require spaces and at least one character of each included type. It specifies a length of 20 characters.
    Expected Output:
    
    :example: response = client.get_random_password(
        PasswordLength=123,
        ExcludeCharacters='string',
        ExcludeNumbers=True|False,
        ExcludePunctuation=True|False,
        ExcludeUppercase=True|False,
        ExcludeLowercase=True|False,
        IncludeSpace=True|False,
        RequireEachIncludedType=True|False
    )
    
    
    :type PasswordLength: integer
    :param PasswordLength: The desired length of the generated password. The default value if you do not include this parameter is 32 characters.

    :type ExcludeCharacters: string
    :param ExcludeCharacters: A string that includes characters that should not be included in the generated password. The default is that all characters from the included sets can be used.

    :type ExcludeNumbers: boolean
    :param ExcludeNumbers: Specifies that the generated password should not include digits. The default if you do not include this switch parameter is that digits can be included.

    :type ExcludePunctuation: boolean
    :param ExcludePunctuation: Specifies that the generated password should not include punctuation characters. The default if you do not include this switch parameter is that punctuation characters can be included.\nThe following are the punctuation characters that can be included in the generated password if you don\'t explicitly exclude them with ExcludeCharacters or ExcludePunctuation :\n\n! ' # $ % & \' ( ) * + , - . / : ; < = > ? @ [ \\ ] ^ _ ` { | } ~\n

    :type ExcludeUppercase: boolean
    :param ExcludeUppercase: Specifies that the generated password should not include uppercase letters. The default if you do not include this switch parameter is that uppercase letters can be included.

    :type ExcludeLowercase: boolean
    :param ExcludeLowercase: Specifies that the generated password should not include lowercase letters. The default if you do not include this switch parameter is that lowercase letters can be included.

    :type IncludeSpace: boolean
    :param IncludeSpace: Specifies that the generated password can include the space character. The default if you do not include this switch parameter is that the space character is not included.

    :type RequireEachIncludedType: boolean
    :param RequireEachIncludedType: A boolean value that specifies whether the generated password must include at least one of every allowed character type. The default value is True and the operation requires at least one of every character type.

    :rtype: dict

ReturnsResponse Syntax
{
    'RandomPassword': 'string'
}


Response Structure

(dict) --

RandomPassword (string) --
A string with the generated password.







Exceptions

SecretsManager.Client.exceptions.InvalidParameterException
SecretsManager.Client.exceptions.InvalidRequestException
SecretsManager.Client.exceptions.InternalServiceError

Examples
The following example shows how to request a randomly generated password. This example includes the optional flags to require spaces and at least one character of each included type. It specifies a length of 20 characters.
response = client.get_random_password(
    IncludeSpace=True,
    PasswordLength=20,
    RequireEachIncludedType=True,
)

print(response)


Expected Output:
{
    'RandomPassword': 'N+Z43a,>vx7j O8^*<8i3',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'RandomPassword': 'string'
    }
    
    
    :returns: 
    PasswordLength (integer) -- The desired length of the generated password. The default value if you do not include this parameter is 32 characters.
    ExcludeCharacters (string) -- A string that includes characters that should not be included in the generated password. The default is that all characters from the included sets can be used.
    ExcludeNumbers (boolean) -- Specifies that the generated password should not include digits. The default if you do not include this switch parameter is that digits can be included.
    ExcludePunctuation (boolean) -- Specifies that the generated password should not include punctuation characters. The default if you do not include this switch parameter is that punctuation characters can be included.
    The following are the punctuation characters that can be included in the generated password if you don\'t explicitly exclude them with ExcludeCharacters or ExcludePunctuation :
    
    ! " # $ % & \' ( ) * + , - . / : ; < = > ? @ [ \\ ] ^ _ ` { | } ~
    
    ExcludeUppercase (boolean) -- Specifies that the generated password should not include uppercase letters. The default if you do not include this switch parameter is that uppercase letters can be included.
    ExcludeLowercase (boolean) -- Specifies that the generated password should not include lowercase letters. The default if you do not include this switch parameter is that lowercase letters can be included.
    IncludeSpace (boolean) -- Specifies that the generated password can include the space character. The default if you do not include this switch parameter is that the space character is not included.
    RequireEachIncludedType (boolean) -- A boolean value that specifies whether the generated password must include at least one of every allowed character type. The default value is True and the operation requires at least one of every character type.
    
    """
    pass

def get_resource_policy(SecretId=None):
    """
    Retrieves the JSON text of the resource-based policy document that\'s attached to the specified secret. The JSON request string input and response output are shown formatted with white space and line breaks for better readability. Submit your input as a single line JSON string.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to retrieve the resource-based policy that is attached to a secret.
    Expected Output:
    
    :example: response = client.get_resource_policy(
        SecretId='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nSpecifies the secret that you want to retrieve the attached resource-based policy for. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'ARN': 'string',
    'Name': 'string',
    'ResourcePolicy': 'string'
}


Response Structure

(dict) --
ARN (string) --The ARN of the secret that the resource-based policy was retrieved for.

Name (string) --The friendly name of the secret that the resource-based policy was retrieved for.

ResourcePolicy (string) --A JSON-formatted string that describes the permissions that are associated with the attached secret. These permissions are combined with any permissions that are associated with the user or role that attempts to access this secret. The combined permissions specify who can access the secret and what actions they can perform. For more information, see Authentication and Access Control for AWS Secrets Manager in the AWS Secrets Manager User Guide .






Exceptions

SecretsManager.Client.exceptions.ResourceNotFoundException
SecretsManager.Client.exceptions.InternalServiceError
SecretsManager.Client.exceptions.InvalidRequestException

Examples
The following example shows how to retrieve the resource-based policy that is attached to a secret.
response = client.get_resource_policy(
    SecretId='MyTestDatabaseSecret',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Name': 'MyTestDatabaseSecret',
    'ResourcePolicy': '{\
"Version":"2012-10-17",\
"Statement":[{\
"Effect":"Allow",\
"Principal":{\
"AWS":"arn:aws:iam::123456789012:root"\
},\
"Action":"secretsmanager:GetSecretValue",\
"Resource":"*"\
}]\
}',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ARN': 'string',
        'Name': 'string',
        'ResourcePolicy': 'string'
    }
    
    
    :returns: 
    To attach a resource policy to a secret, use  PutResourcePolicy .
    To delete the resource-based policy that\'s attached to a secret, use  DeleteResourcePolicy .
    To list all of the currently available secrets, use  ListSecrets .
    
    """
    pass

def get_secret_value(SecretId=None, VersionId=None, VersionStage=None):
    """
    Retrieves the contents of the encrypted fields SecretString or SecretBinary from the specified version of a secret, whichever contains content.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to retrieve the secret string value from the version of the secret that has the AWSPREVIOUS staging label attached. If you want to retrieve the AWSCURRENT version of the secret, then you can omit the VersionStage parameter because it defaults to AWSCURRENT.
    Expected Output:
    
    :example: response = client.get_secret_value(
        SecretId='string',
        VersionId='string',
        VersionStage='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nSpecifies the secret containing the version that you want to retrieve. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :type VersionId: string
    :param VersionId: Specifies the unique identifier of the version of the secret that you want to retrieve. If you specify this parameter then don\'t specify VersionStage . If you don\'t specify either a VersionStage or VersionId then the default is to perform the operation on the version with the VersionStage value of AWSCURRENT .\nThis value is typically a UUID-type value with 32 hexadecimal digits.\n

    :type VersionStage: string
    :param VersionStage: Specifies the secret version that you want to retrieve by the staging label attached to the version.\nStaging labels are used to keep track of different versions during the rotation process. If you use this parameter then don\'t specify VersionId . If you don\'t specify either a VersionStage or VersionId , then the default is to perform the operation on the version with the VersionStage value of AWSCURRENT .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ARN': 'string',
    'Name': 'string',
    'VersionId': 'string',
    'SecretBinary': b'bytes',
    'SecretString': 'string',
    'VersionStages': [
        'string',
    ],
    'CreatedDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

ARN (string) --
The ARN of the secret.

Name (string) --
The friendly name of the secret.

VersionId (string) --
The unique identifier of this version of the secret.

SecretBinary (bytes) --
The decrypted part of the protected secret information that was originally provided as binary data in the form of a byte array. The response parameter represents the binary data as a base64-encoded string.
This parameter is not used if the secret is created by the Secrets Manager console.
If you store custom information in this field of the secret, then you must code your Lambda rotation function to parse and interpret whatever you store in the SecretString or SecretBinary fields.

SecretString (string) --
The decrypted part of the protected secret information that was originally provided as a string.
If you create this secret by using the Secrets Manager console then only the SecretString parameter contains data. Secrets Manager stores the information as a JSON structure of key/value pairs that the Lambda rotation function knows how to parse.
If you store custom information in the secret by using the  CreateSecret ,  UpdateSecret , or  PutSecretValue API operations instead of the Secrets Manager console, or by using the Other secret type in the console, then you must code your Lambda rotation function to parse and interpret those values.

VersionStages (list) --
A list of all of the staging labels currently attached to this version of the secret.

(string) --


CreatedDate (datetime) --
The date and time that this version of the secret was created.







Exceptions

SecretsManager.Client.exceptions.ResourceNotFoundException
SecretsManager.Client.exceptions.InvalidParameterException
SecretsManager.Client.exceptions.InvalidRequestException
SecretsManager.Client.exceptions.DecryptionFailure
SecretsManager.Client.exceptions.InternalServiceError

Examples
The following example shows how to retrieve the secret string value from the version of the secret that has the AWSPREVIOUS staging label attached. If you want to retrieve the AWSCURRENT version of the secret, then you can omit the VersionStage parameter because it defaults to AWSCURRENT.
response = client.get_secret_value(
    SecretId='MyTestDatabaseSecret',
    VersionStage='AWSPREVIOUS',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'CreatedDate': 1523477145.713,
    'Name': 'MyTestDatabaseSecret',
    'SecretString': '{\
  "username":"david",\
  "password":"BnQw&XDWgaEeT9XGTT29"\
}\
',
    'VersionId': 'EXAMPLE1-90ab-cdef-fedc-ba987SECRET1',
    'VersionStages': [
        'AWSPREVIOUS',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ARN': 'string',
        'Name': 'string',
        'VersionId': 'string',
        'SecretBinary': b'bytes',
        'SecretString': 'string',
        'VersionStages': [
            'string',
        ],
        'CreatedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    To create a new version of the secret with different encrypted information, use  PutSecretValue .
    To retrieve the non-encrypted details for the secret, use  DescribeSecret .
    
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

def list_secret_version_ids(SecretId=None, MaxResults=None, NextToken=None, IncludeDeprecated=None):
    """
    Lists all of the versions attached to the specified secret. The output does not include the SecretString or SecretBinary fields. By default, the list includes only versions that have at least one staging label in VersionStage attached.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to retrieve a list of all of the versions of a secret, including those without any staging labels.
    Expected Output:
    
    :example: response = client.list_secret_version_ids(
        SecretId='string',
        MaxResults=123,
        NextToken='string',
        IncludeDeprecated=True|False
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nThe identifier for the secret containing the versions you want to list. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :type MaxResults: integer
    :param MaxResults: (Optional) Limits the number of results that you want to include in the response. If you don\'t include this parameter, it defaults to a value that\'s specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (isn\'t null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Secrets Manager might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :type NextToken: string
    :param NextToken: (Optional) Use this parameter in a request if you receive a NextToken response in a previous request that indicates that there\'s more output available. In a subsequent call, set it to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type IncludeDeprecated: boolean
    :param IncludeDeprecated: (Optional) Specifies that you want the results to include versions that do not have any staging labels attached to them. Such versions are considered deprecated and are subject to deletion by Secrets Manager as needed.

    :rtype: dict

ReturnsResponse Syntax
{
    'Versions': [
        {
            'VersionId': 'string',
            'VersionStages': [
                'string',
            ],
            'LastAccessedDate': datetime(2015, 1, 1),
            'CreatedDate': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string',
    'ARN': 'string',
    'Name': 'string'
}


Response Structure

(dict) --

Versions (list) --
The list of the currently available versions of the specified secret.

(dict) --
A structure that contains information about one version of a secret.

VersionId (string) --
The unique version identifier of this version of the secret.

VersionStages (list) --
An array of staging labels that are currently associated with this version of the secret.

(string) --


LastAccessedDate (datetime) --
The date that this version of the secret was last accessed. Note that the resolution of this field is at the date level and does not include the time.

CreatedDate (datetime) --
The date and time this version of the secret was created.





NextToken (string) --
If present in the response, this value indicates that there\'s more output available than what\'s included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a very long list. Use this value in the NextToken request parameter in a subsequent call to the operation to continue processing and get the next part of the output. You should repeat this until the NextToken response element comes back empty (as null ).

ARN (string) --
The Amazon Resource Name (ARN) for the secret.

Note
Secrets Manager automatically adds several random characters to the name at the end of the ARN when you initially create a secret. This affects only the ARN and not the actual friendly name. This ensures that if you create a new secret with the same name as an old secret that you previously deleted, then users with access to the old secret don\'t automatically get access to the new secret because the ARNs are different.


Name (string) --
The friendly name of the secret.







Exceptions

SecretsManager.Client.exceptions.InvalidNextTokenException
SecretsManager.Client.exceptions.ResourceNotFoundException
SecretsManager.Client.exceptions.InternalServiceError

Examples
The following example shows how to retrieve a list of all of the versions of a secret, including those without any staging labels.
response = client.list_secret_version_ids(
    IncludeDeprecated=True,
    SecretId='MyTestDatabaseSecret',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Name': 'MyTestDatabaseSecret',
    'Versions': [
        {
            'CreatedDate': 1523477145.713,
            'VersionId': 'EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE',
            'VersionStages': [
                'AWSPREVIOUS',
            ],
        },
        {
            'CreatedDate': 1523486221.391,
            'VersionId': 'EXAMPLE2-90ab-cdef-fedc-ba987EXAMPLE',
            'VersionStages': [
                'AWSCURRENT',
            ],
        },
        {
            'CreatedDate': 1511974462.36,
            'VersionId': 'EXAMPLE3-90ab-cdef-fedc-ba987EXAMPLE;',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Versions': [
            {
                'VersionId': 'string',
                'VersionStages': [
                    'string',
                ],
                'LastAccessedDate': datetime(2015, 1, 1),
                'CreatedDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string',
        'ARN': 'string',
        'Name': 'string'
    }
    
    
    :returns: 
    To list the secrets in an account, use  ListSecrets .
    
    """
    pass

def list_secrets(MaxResults=None, NextToken=None):
    """
    Lists all of the secrets that are stored by Secrets Manager in the AWS account. To list the versions currently stored for a specific secret, use  ListSecretVersionIds . The encrypted fields SecretString and SecretBinary are not included in the output. To get that information, call the  GetSecretValue operation.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to list all of the secrets in your account.
    Expected Output:
    
    :example: response = client.list_secrets(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: (Optional) Limits the number of results that you want to include in the response. If you don\'t include this parameter, it defaults to a value that\'s specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (isn\'t null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Secrets Manager might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :type NextToken: string
    :param NextToken: (Optional) Use this parameter in a request if you receive a NextToken response in a previous request that indicates that there\'s more output available. In a subsequent call, set it to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :rtype: dict

ReturnsResponse Syntax
{
    'SecretList': [
        {
            'ARN': 'string',
            'Name': 'string',
            'Description': 'string',
            'KmsKeyId': 'string',
            'RotationEnabled': True|False,
            'RotationLambdaARN': 'string',
            'RotationRules': {
                'AutomaticallyAfterDays': 123
            },
            'LastRotatedDate': datetime(2015, 1, 1),
            'LastChangedDate': datetime(2015, 1, 1),
            'LastAccessedDate': datetime(2015, 1, 1),
            'DeletedDate': datetime(2015, 1, 1),
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'SecretVersionsToStages': {
                'string': [
                    'string',
                ]
            },
            'OwningService': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SecretList (list) --
A list of the secrets in the account.

(dict) --
A structure that contains the details about a secret. It does not include the encrypted SecretString and SecretBinary values. To get those values, use the  GetSecretValue operation.

ARN (string) --
The Amazon Resource Name (ARN) of the secret.
For more information about ARNs in Secrets Manager, see Policy Resources in the AWS Secrets Manager User Guide .

Name (string) --
The friendly name of the secret. You can use forward slashes in the name to represent a path hierarchy. For example, /prod/databases/dbserver1 could represent the secret for a server named dbserver1 in the folder databases in the folder prod .

Description (string) --
The user-provided description of the secret.

KmsKeyId (string) --
The ARN or alias of the AWS KMS customer master key (CMK) that\'s used to encrypt the SecretString and SecretBinary fields in each version of the secret. If you don\'t provide a key, then Secrets Manager defaults to encrypting the secret fields with the default KMS CMK (the one named awssecretsmanager ) for this account.

RotationEnabled (boolean) --
Indicates whether automatic, scheduled rotation is enabled for this secret.

RotationLambdaARN (string) --
The ARN of an AWS Lambda function that\'s invoked by Secrets Manager to rotate and expire the secret either automatically per the schedule or manually by a call to  RotateSecret .

RotationRules (dict) --
A structure that defines the rotation configuration for the secret.

AutomaticallyAfterDays (integer) --
Specifies the number of days between automatic scheduled rotations of the secret.
Secrets Manager schedules the next rotation when the previous one is complete. Secrets Manager schedules the date by adding the rotation interval (number of days) to the actual date of the last rotation. The service chooses the hour within that 24-hour date window randomly. The minute is also chosen somewhat randomly, but weighted towards the top of the hour and influenced by a variety of factors that help distribute load.



LastRotatedDate (datetime) --
The last date and time that the rotation process for this secret was invoked.

LastChangedDate (datetime) --
The last date and time that this secret was modified in any way.

LastAccessedDate (datetime) --
The last date that this secret was accessed. This value is truncated to midnight of the date and therefore shows only the date, not the time.

DeletedDate (datetime) --
The date and time on which this secret was deleted. Not present on active secrets. The secret can be recovered until the number of days in the recovery window has passed, as specified in the RecoveryWindowInDays parameter of the  DeleteSecret operation.

Tags (list) --
The list of user-defined tags that are associated with the secret. To add tags to a secret, use  TagResource . To remove tags, use  UntagResource .

(dict) --
A structure that contains information about a tag.

Key (string) --
The key identifier, or name, of the tag.

Value (string) --
The string value that\'s associated with the key of the tag.





SecretVersionsToStages (dict) --
A list of all of the currently assigned SecretVersionStage staging labels and the SecretVersionId that each is attached to. Staging labels are used to keep track of the different versions during the rotation process.

Note
A version that does not have any SecretVersionStage is considered deprecated and subject to deletion. Such versions are not included in this list.


(string) --
(list) --
(string) --






OwningService (string) --
Returns the name of the service that created the secret.





NextToken (string) --
If present in the response, this value indicates that there\'s more output available than what\'s included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a very long list. Use this value in the NextToken request parameter in a subsequent call to the operation to continue processing and get the next part of the output. You should repeat this until the NextToken response element comes back empty (as null ).







Exceptions

SecretsManager.Client.exceptions.InvalidParameterException
SecretsManager.Client.exceptions.InvalidNextTokenException
SecretsManager.Client.exceptions.InternalServiceError

Examples
The following example shows how to list all of the secrets in your account.
response = client.list_secrets(
)

print(response)


Expected Output:
{
    'SecretList': [
        {
            'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
            'Description': 'My test database secret',
            'LastChangedDate': 1523477145.729,
            'Name': 'MyTestDatabaseSecret',
            'SecretVersionsToStages': {
                'EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE': [
                    'AWSCURRENT',
                ],
            },
        },
        {
            'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret1-d4e5f6',
            'Description': 'Another secret created for a different database',
            'LastChangedDate': 1523482025.685,
            'Name': 'MyTestDatabaseSecret1',
            'SecretVersionsToStages': {
                'EXAMPLE2-90ab-cdef-fedc-ba987EXAMPLE': [
                    'AWSCURRENT',
                ],
            },
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'SecretList': [
            {
                'ARN': 'string',
                'Name': 'string',
                'Description': 'string',
                'KmsKeyId': 'string',
                'RotationEnabled': True|False,
                'RotationLambdaARN': 'string',
                'RotationRules': {
                    'AutomaticallyAfterDays': 123
                },
                'LastRotatedDate': datetime(2015, 1, 1),
                'LastChangedDate': datetime(2015, 1, 1),
                'LastAccessedDate': datetime(2015, 1, 1),
                'DeletedDate': datetime(2015, 1, 1),
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'SecretVersionsToStages': {
                    'string': [
                        'string',
                    ]
                },
                'OwningService': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    To list the versions attached to a secret, use  ListSecretVersionIds .
    
    """
    pass

def put_resource_policy(SecretId=None, ResourcePolicy=None):
    """
    Attaches the contents of the specified resource-based permission policy to a secret. A resource-based policy is optional. Alternatively, you can use IAM identity-based policies that specify the secret\'s Amazon Resource Name (ARN) in the policy statement\'s Resources element. You can also use a combination of both identity-based and resource-based policies. The affected users and roles receive the permissions that are permitted by all of the relevant policies. For more information, see Using Resource-Based Policies for AWS Secrets Manager . For the complete description of the AWS policy syntax and grammar, see IAM JSON Policy Reference in the IAM User Guide .
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to add a resource-based policy to a secret.
    Expected Output:
    
    :example: response = client.put_resource_policy(
        SecretId='string',
        ResourcePolicy='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nSpecifies the secret that you want to attach the resource-based policy to. You can specify either the ARN or the friendly name of the secret.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :type ResourcePolicy: string
    :param ResourcePolicy: [REQUIRED]\nA JSON-formatted string that\'s constructed according to the grammar and syntax for an AWS resource-based policy. The policy in the string identifies who can access or manage this secret and its versions. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ARN': 'string',
    'Name': 'string'
}


Response Structure

(dict) --

ARN (string) --
The ARN of the secret that the resource-based policy was retrieved for.

Name (string) --
The friendly name of the secret that the resource-based policy was retrieved for.







Exceptions

SecretsManager.Client.exceptions.MalformedPolicyDocumentException
SecretsManager.Client.exceptions.ResourceNotFoundException
SecretsManager.Client.exceptions.InvalidParameterException
SecretsManager.Client.exceptions.InternalServiceError
SecretsManager.Client.exceptions.InvalidRequestException

Examples
The following example shows how to add a resource-based policy to a secret.
response = client.put_resource_policy(
    ResourcePolicy='{\
"Version":"2012-10-17",\
"Statement":[{\
"Effect":"Allow",\
"Principal":{\
"AWS":"arn:aws:iam::123456789012:root"\
},\
"Action":"secretsmanager:GetSecretValue",\
"Resource":"*"\
}]\
}',
    SecretId='MyTestDatabaseSecret',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Name': 'MyTestDatabaseSecret',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ARN': 'string',
        'Name': 'string'
    }
    
    
    :returns: 
    To retrieve the resource policy that\'s attached to a secret, use  GetResourcePolicy .
    To delete the resource-based policy that\'s attached to a secret, use  DeleteResourcePolicy .
    To list all of the currently available secrets, use  ListSecrets .
    
    """
    pass

def put_secret_value(SecretId=None, ClientRequestToken=None, SecretBinary=None, SecretString=None, VersionStages=None):
    """
    Stores a new encrypted secret value in the specified secret. To do this, the operation creates a new version and attaches it to the secret. The version can contain a new SecretString value or a new SecretBinary value. You can also specify the staging labels that are initially attached to the new version.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to create a new version of the secret. Alternatively, you can use the update-secret command.
    Expected Output:
    
    :example: response = client.put_secret_value(
        SecretId='string',
        ClientRequestToken='string',
        SecretBinary=b'bytes',
        SecretString='string',
        VersionStages=[
            'string',
        ]
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nSpecifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) Specifies a unique identifier for the new version of the secret.\n\nNote\nIf you use the AWS CLI or one of the AWS SDK to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes that in the request. If you don\'t use the SDK and instead generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a ClientRequestToken yourself for new versions and include that value in the request.\n\nThis value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during the Lambda rotation function\'s processing. We recommend that you generate a UUID-type value to ensure uniqueness within the specified secret.\n\nIf the ClientRequestToken value isn\'t already associated with a version of the secret then a new version of the secret is created.\nIf a version with this value already exists and that version\'s SecretString or SecretBinary values are the same as those in the request then the request is ignored (the operation is idempotent).\nIf a version with this value already exists and that version\'s SecretString and SecretBinary values are different from those in the request then the request fails because you cannot modify an existing secret version. You can only create new versions to store new secret values.\n\nThis value becomes the VersionId of the new version.\nThis field is autopopulated if not provided.\n

    :type SecretBinary: bytes
    :param SecretBinary: (Optional) Specifies binary data that you want to encrypt and store in the new version of the secret. To use this parameter in the command-line tools, we recommend that you store your binary data in a file and then use the appropriate technique for your tool to pass the contents of the file as a parameter. Either SecretBinary or SecretString must have a value, but not both. They cannot both be empty.\nThis parameter is not accessible if the secret using the Secrets Manager console.\n

    :type SecretString: string
    :param SecretString: (Optional) Specifies text data that you want to encrypt and store in this new version of the secret. Either SecretString or SecretBinary must have a value, but not both. They cannot both be empty.\nIf you create this secret by using the Secrets Manager console then Secrets Manager puts the protected secret text in only the SecretString parameter. The Secrets Manager console stores the information as a JSON structure of key/value pairs that the default Lambda rotation function knows how to parse.\nFor storing multiple values, we recommend that you use a JSON text string argument and specify key/value pairs. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide .\nFor example:\n\n[{'username':'bob'},{'password':'abc123xyz456'}]\nIf your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text.\n

    :type VersionStages: list
    :param VersionStages: (Optional) Specifies a list of staging labels that are attached to this version of the secret. These staging labels are used to track the versions through the rotation process by the Lambda rotation function.\nA staging label must be unique to a single version of the secret. If you specify a staging label that\'s already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version.\nIf you do not specify a value for VersionStages then Secrets Manager automatically moves the staging label AWSCURRENT to this new version.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ARN': 'string',
    'Name': 'string',
    'VersionId': 'string',
    'VersionStages': [
        'string',
    ]
}


Response Structure

(dict) --

ARN (string) --
The Amazon Resource Name (ARN) for the secret for which you just created a version.

Name (string) --
The friendly name of the secret for which you just created or updated a version.

VersionId (string) --
The unique identifier of the version of the secret you just created or updated.

VersionStages (list) --
The list of staging labels that are currently attached to this version of the secret. Staging labels are used to track a version as it progresses through the secret rotation process.

(string) --








Exceptions

SecretsManager.Client.exceptions.InvalidParameterException
SecretsManager.Client.exceptions.InvalidRequestException
SecretsManager.Client.exceptions.LimitExceededException
SecretsManager.Client.exceptions.EncryptionFailure
SecretsManager.Client.exceptions.ResourceExistsException
SecretsManager.Client.exceptions.ResourceNotFoundException
SecretsManager.Client.exceptions.InternalServiceError

Examples
The following example shows how to create a new version of the secret. Alternatively, you can use the update-secret command.
response = client.put_secret_value(
    ClientRequestToken='EXAMPLE2-90ab-cdef-fedc-ba987EXAMPLE',
    SecretId='MyTestDatabaseSecret',
    SecretString='{"username":"david","password":"BnQw!XDWgaEeT9XGTT29"}',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Name': 'MyTestDatabaseSecret',
    'VersionId': 'EXAMPLE2-90ab-cdef-fedc-ba987EXAMPLE',
    'VersionStages': [
        'AWSCURRENT',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ARN': 'string',
        'Name': 'string',
        'VersionId': 'string',
        'VersionStages': [
            'string',
        ]
    }
    
    
    :returns: 
    If you call an operation that needs to encrypt or decrypt the SecretString or SecretBinary for a secret in the same account as the calling user and that secret doesn\'t specify a AWS KMS encryption key, Secrets Manager uses the account\'s default AWS managed customer master key (CMK) with the alias aws/secretsmanager . If this key doesn\'t already exist in your account then Secrets Manager creates it for you automatically. All users and roles in the same AWS account automatically have access to use the default CMK. Note that if an Secrets Manager API call results in AWS having to create the account\'s AWS-managed CMK, it can result in a one-time significant delay in returning the result.
    If the secret is in a different AWS account from the credentials calling an API that requires encryption or decryption of the secret value then you must create and use a custom AWS KMS CMK because you can\'t access the default CMK for the account using credentials from a different AWS account. Store the ARN of the CMK in the secret when you create the secret or when you update it by including it in the KMSKeyId . If you call an API that must encrypt or decrypt SecretString or SecretBinary using credentials from a different account then the AWS KMS key policy must grant cross-account access to that other account\'s user or role for both the kms:GenerateDataKey and kms:Decrypt operations.
    
    """
    pass

def restore_secret(SecretId=None):
    """
    Cancels the scheduled deletion of a secret by removing the DeletedDate time stamp. This makes the secret accessible to query once again.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to restore a secret that you previously scheduled for deletion.
    Expected Output:
    
    :example: response = client.restore_secret(
        SecretId='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nSpecifies the secret that you want to restore from a previously scheduled deletion. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'ARN': 'string',
    'Name': 'string'
}


Response Structure

(dict) --
ARN (string) --The ARN of the secret that was restored.

Name (string) --The friendly name of the secret that was restored.






Exceptions

SecretsManager.Client.exceptions.ResourceNotFoundException
SecretsManager.Client.exceptions.InvalidParameterException
SecretsManager.Client.exceptions.InvalidRequestException
SecretsManager.Client.exceptions.InternalServiceError

Examples
The following example shows how to restore a secret that you previously scheduled for deletion.
response = client.restore_secret(
    SecretId='MyTestDatabaseSecret',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Name': 'MyTestDatabaseSecret',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ARN': 'string',
        'Name': 'string'
    }
    
    
    :returns: 
    To delete a secret, use  DeleteSecret .
    
    """
    pass

def rotate_secret(SecretId=None, ClientRequestToken=None, RotationLambdaARN=None, RotationRules=None):
    """
    Configures and starts the asynchronous process of rotating this secret. If you include the configuration parameters, the operation sets those values for the secret and then immediately starts a rotation. If you do not include the configuration parameters, the operation starts a rotation with the values already stored in the secret. After the rotation completes, the protected service and its clients all use the new version of the secret.
    This required configuration information includes the ARN of an AWS Lambda function and the time between scheduled rotations. The Lambda rotation function creates a new version of the secret and creates or updates the credentials on the protected service to match. After testing the new credentials, the function marks the new secret with the staging label AWSCURRENT so that your clients all immediately begin to use the new version. For more information about rotating secrets and how to configure a Lambda function to rotate the secrets for your protected service, see Rotating Secrets in AWS Secrets Manager in the AWS Secrets Manager User Guide .
    Secrets Manager schedules the next rotation when the previous one is complete. Secrets Manager schedules the date by adding the rotation interval (number of days) to the actual date of the last rotation. The service chooses the hour within that 24-hour date window randomly. The minute is also chosen somewhat randomly, but weighted towards the top of the hour and influenced by a variety of factors that help distribute load.
    The rotation function must end with the versions of the secret in one of two states:
    If instead the AWSPENDING staging label is present but is not attached to the same version as AWSCURRENT then any later invocation of RotateSecret assumes that a previous rotation request is still in progress and returns an error.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example configures rotation for a secret by providing the ARN of a Lambda rotation function (which must already exist) and the number of days between rotation. The first rotation happens immediately upon completion of this command. The rotation function runs asynchronously in the background.
    Expected Output:
    
    :example: response = client.rotate_secret(
        SecretId='string',
        ClientRequestToken='string',
        RotationLambdaARN='string',
        RotationRules={
            'AutomaticallyAfterDays': 123
        }
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nSpecifies the secret that you want to rotate. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) Specifies a unique identifier for the new version of the secret that helps ensure idempotency.\nIf you use the AWS CLI or one of the AWS SDK to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes that in the request for this parameter. If you don\'t use the SDK and instead generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a ClientRequestToken yourself for new versions and include that value in the request.\nYou only need to specify your own value if you are implementing your own retry logic and want to ensure that a given secret is not created twice. We recommend that you generate a UUID-type value to ensure uniqueness within the specified secret.\nSecrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during the function\'s processing. This value becomes the VersionId of the new version.\nThis field is autopopulated if not provided.\n

    :type RotationLambdaARN: string
    :param RotationLambdaARN: (Optional) Specifies the ARN of the Lambda function that can rotate the secret.

    :type RotationRules: dict
    :param RotationRules: A structure that defines the rotation configuration for this secret.\n\nAutomaticallyAfterDays (integer) --Specifies the number of days between automatic scheduled rotations of the secret.\nSecrets Manager schedules the next rotation when the previous one is complete. Secrets Manager schedules the date by adding the rotation interval (number of days) to the actual date of the last rotation. The service chooses the hour within that 24-hour date window randomly. The minute is also chosen somewhat randomly, but weighted towards the top of the hour and influenced by a variety of factors that help distribute load.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ARN': 'string',
    'Name': 'string',
    'VersionId': 'string'
}


Response Structure

(dict) --

ARN (string) --
The ARN of the secret.

Name (string) --
The friendly name of the secret.

VersionId (string) --
The ID of the new version of the secret created by the rotation started by this request.







Exceptions

SecretsManager.Client.exceptions.ResourceNotFoundException
SecretsManager.Client.exceptions.InvalidParameterException
SecretsManager.Client.exceptions.InternalServiceError
SecretsManager.Client.exceptions.InvalidRequestException

Examples
The following example configures rotation for a secret by providing the ARN of a Lambda rotation function (which must already exist) and the number of days between rotation. The first rotation happens immediately upon completion of this command. The rotation function runs asynchronously in the background.
response = client.rotate_secret(
    RotationLambdaARN='arn:aws:lambda:us-west-2:123456789012:function:MyTestDatabaseRotationLambda',
    RotationRules={
        'AutomaticallyAfterDays': 30,
    },
    SecretId='MyTestDatabaseSecret',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Name': 'MyTestDatabaseSecret',
    'VersionId': 'EXAMPLE2-90ab-cdef-fedc-ba987SECRET2',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ARN': 'string',
        'Name': 'string',
        'VersionId': 'string'
    }
    
    
    :returns: 
    secretsmanager:RotateSecret
    lambda:InvokeFunction (on the function specified in the secret\'s metadata)
    
    """
    pass

def tag_resource(SecretId=None, Tags=None):
    """
    Attaches one or more tags, each consisting of a key name and a value, to the specified secret. Tags are part of the secret\'s overall metadata, and are not associated with any specific version of the secret. This operation only appends tags to the existing list of tags. To remove tags, you must use  UntagResource .
    The following basic restrictions apply to tags:
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to attach two tags each with a Key and Value to a secret. There is no output from this API. To see the result, use the DescribeSecret operation.
    Expected Output:
    
    :example: response = client.tag_resource(
        SecretId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nThe identifier for the secret that you want to attach tags to. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags to attach to the secret. Each element in the list consists of a Key and a Value .\nThis parameter to the API requires a JSON text string argument. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide . For the AWS CLI, you can also use the syntax: --Tags Key='Key1',Value='Value1',Key='Key2',Value='Value2'[,\xe2\x80\xa6]\n\n(dict) --A structure that contains information about a tag.\n\nKey (string) --The key identifier, or name, of the tag.\n\nValue (string) --The string value that\'s associated with the key of the tag.\n\n\n\n\n

    :return: response = client.tag_resource(
        SecretId='MyExampleSecret',
        Tags=[
            {
                'Key': 'FirstTag',
                'Value': 'SomeValue',
            },
            {
                'Key': 'SecondTag',
                'Value': 'AnotherValue',
            },
        ],
    )
    
    print(response)
    
    
    :returns: 
    secretsmanager:TagResource
    
    """
    pass

def untag_resource(SecretId=None, TagKeys=None):
    """
    Removes one or more tags from the specified secret.
    This operation is idempotent. If a requested tag is not attached to the secret, no error is returned and the secret metadata is unchanged.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to remove two tags from a secret\'s metadata. For each, both the tag and the associated value are removed. There is no output from this API. To see the result, use the DescribeSecret operation.
    Expected Output:
    
    :example: response = client.untag_resource(
        SecretId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nThe identifier for the secret that you want to remove tags from. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of tag key names to remove from the secret. You don\'t specify the value. Both the key and its associated value are removed.\nThis parameter to the API requires a JSON text string argument. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide .\n\n(string) --\n\n

    :return: response = client.untag_resource(
        SecretId='MyTestDatabaseSecret',
        TagKeys=[
            'FirstTag',
            'SecondTag',
        ],
    )
    
    print(response)
    
    
    :returns: 
    To add one or more tags to the collection attached to a secret, use  TagResource .
    To view the list of tags attached to a secret, use  DescribeSecret .
    
    """
    pass

def update_secret(SecretId=None, ClientRequestToken=None, Description=None, KmsKeyId=None, SecretBinary=None, SecretString=None):
    """
    Modifies many of the details of the specified secret. If you include a ClientRequestToken and either SecretString or SecretBinary then it also creates a new version attached to the secret.
    To modify the rotation configuration of a secret, use  RotateSecret instead.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to modify the description of a secret.
    Expected Output:
    This example shows how to update the KMS customer managed key (CMK) used to encrypt the secret value. The KMS CMK must be in the same region as the secret.
    Expected Output:
    The following example shows how to create a new version of the secret by updating the SecretString field. Alternatively, you can use the put-secret-value operation.
    Expected Output:
    
    :example: response = client.update_secret(
        SecretId='string',
        ClientRequestToken='string',
        Description='string',
        KmsKeyId='string',
        SecretBinary=b'bytes',
        SecretString='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nSpecifies the secret that you want to modify or to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) If you want to add a new version to the secret, this parameter specifies a unique identifier for the new version that helps ensure idempotency.\nIf you use the AWS CLI or one of the AWS SDK to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes that in the request. If you don\'t use the SDK and instead generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a ClientRequestToken yourself for new versions and include that value in the request.\nYou typically only need to interact with this value if you implement your own retry logic and want to ensure that a given secret is not created twice. We recommend that you generate a UUID-type value to ensure uniqueness within the specified secret.\nSecrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during the Lambda rotation function\'s processing.\n\nIf the ClientRequestToken value isn\'t already associated with a version of the secret then a new version of the secret is created.\nIf a version with this value already exists and that version\'s SecretString and SecretBinary values are the same as those in the request then the request is ignored (the operation is idempotent).\nIf a version with this value already exists and that version\'s SecretString and SecretBinary values are different from the request then an error occurs because you cannot modify an existing secret value.\n\nThis value becomes the VersionId of the new version.\nThis field is autopopulated if not provided.\n

    :type Description: string
    :param Description: (Optional) Specifies an updated user-provided description of the secret.

    :type KmsKeyId: string
    :param KmsKeyId: (Optional) Specifies an updated ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the protected text in new versions of this secret.\n\nWarning\nYou can only use the account\'s default CMK to encrypt and decrypt if you call this operation using credentials from the same account that owns the secret. If the secret is in a different account, then you must create a custom CMK and provide the ARN of that CMK in this field. The user making the call must have permissions to both the secret and the CMK in their respective accounts.\n\n

    :type SecretBinary: bytes
    :param SecretBinary: (Optional) Specifies updated binary data that you want to encrypt and store in the new version of the secret. To use this parameter in the command-line tools, we recommend that you store your binary data in a file and then use the appropriate technique for your tool to pass the contents of the file as a parameter. Either SecretBinary or SecretString must have a value, but not both. They cannot both be empty.\nThis parameter is not accessible using the Secrets Manager console.\n

    :type SecretString: string
    :param SecretString: (Optional) Specifies updated text data that you want to encrypt and store in this new version of the secret. Either SecretBinary or SecretString must have a value, but not both. They cannot both be empty.\nIf you create this secret by using the Secrets Manager console then Secrets Manager puts the protected secret text in only the SecretString parameter. The Secrets Manager console stores the information as a JSON structure of key/value pairs that the default Lambda rotation function knows how to parse.\nFor storing multiple values, we recommend that you use a JSON text string argument and specify key/value pairs. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide . For example:\n\n[{'username':'bob'},{'password':'abc123xyz456'}]\nIf your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text. You can also \'escape\' the double quote character in the embedded JSON text by prefacing each with a backslash. For example, the following string is surrounded by double-quotes. All of the embedded double quotes are escaped:\n\n'[{\\'username\\':\\'bob\\'},{\\'password\\':\\'abc123xyz456\\'}]'\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ARN': 'string',
    'Name': 'string',
    'VersionId': 'string'
}


Response Structure

(dict) --

ARN (string) --
The ARN of the secret that was updated.

Note
Secrets Manager automatically adds several random characters to the name at the end of the ARN when you initially create a secret. This affects only the ARN and not the actual friendly name. This ensures that if you create a new secret with the same name as an old secret that you previously deleted, then users with access to the old secret don\'t automatically get access to the new secret because the ARNs are different.


Name (string) --
The friendly name of the secret that was updated.

VersionId (string) --
If a new version of the secret was created by this operation, then VersionId contains the unique identifier of the new version.







Exceptions

SecretsManager.Client.exceptions.InvalidParameterException
SecretsManager.Client.exceptions.InvalidRequestException
SecretsManager.Client.exceptions.LimitExceededException
SecretsManager.Client.exceptions.EncryptionFailure
SecretsManager.Client.exceptions.ResourceExistsException
SecretsManager.Client.exceptions.ResourceNotFoundException
SecretsManager.Client.exceptions.MalformedPolicyDocumentException
SecretsManager.Client.exceptions.InternalServiceError
SecretsManager.Client.exceptions.PreconditionNotMetException

Examples
The following example shows how to modify the description of a secret.
response = client.update_secret(
    ClientRequestToken='EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE',
    Description='This is a new description for the secret.',
    SecretId='MyTestDatabaseSecret',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Name': 'MyTestDatabaseSecret',
    'ResponseMetadata': {
        '...': '...',
    },
}


This example shows how to update the KMS customer managed key (CMK) used to encrypt the secret value. The KMS CMK must be in the same region as the secret.
response = client.update_secret(
    KmsKeyId='arn:aws:kms:us-west-2:123456789012:key/EXAMPLE2-90ab-cdef-fedc-ba987EXAMPLE',
    SecretId='MyTestDatabaseSecret',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Name': 'MyTestDatabaseSecret',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example shows how to create a new version of the secret by updating the SecretString field. Alternatively, you can use the put-secret-value operation.
response = client.update_secret(
    SecretId='MyTestDatabaseSecret',
    SecretString='{JSON STRING WITH CREDENTIALS}',
)

print(response)


Expected Output:
{
    'ARN': 'aws:arn:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Name': 'MyTestDatabaseSecret',
    'VersionId': 'EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ARN': 'string',
        'Name': 'string',
        'VersionId': 'string'
    }
    
    
    :returns: 
    If you call an operation that needs to encrypt or decrypt the SecretString or SecretBinary for a secret in the same account as the calling user and that secret doesn\'t specify a AWS KMS encryption key, Secrets Manager uses the account\'s default AWS managed customer master key (CMK) with the alias aws/secretsmanager . If this key doesn\'t already exist in your account then Secrets Manager creates it for you automatically. All users and roles in the same AWS account automatically have access to use the default CMK. Note that if an Secrets Manager API call results in AWS having to create the account\'s AWS-managed CMK, it can result in a one-time significant delay in returning the result.
    If the secret is in a different AWS account from the credentials calling an API that requires encryption or decryption of the secret value then you must create and use a custom AWS KMS CMK because you can\'t access the default CMK for the account using credentials from a different AWS account. Store the ARN of the CMK in the secret when you create the secret or when you update it by including it in the KMSKeyId . If you call an API that must encrypt or decrypt SecretString or SecretBinary using credentials from a different account then the AWS KMS key policy must grant cross-account access to that other account\'s user or role for both the kms:GenerateDataKey and kms:Decrypt operations.
    
    """
    pass

def update_secret_version_stage(SecretId=None, VersionStage=None, RemoveFromVersionId=None, MoveToVersionId=None):
    """
    Modifies the staging labels attached to a version of a secret. Staging labels are used to track a version as it progresses through the secret rotation process. You can attach a staging label to only one version of a secret at a time. If a staging label to be added is already attached to another version, then it is moved--removed from the other version first and then attached to this one. For more information about staging labels, see Staging Labels in the AWS Secrets Manager User Guide .
    The staging labels that you specify in the VersionStage parameter are added to the existing list of staging labels--they don\'t replace it.
    You can move the AWSCURRENT staging label to this version by including it in this call.
    If this action results in the last label being removed from a version, then the version is considered to be \'deprecated\' and can be deleted by Secrets Manager.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows you how to add a staging label to a version of a secret. You can review the results by running the operation ListSecretVersionIds and viewing the VersionStages response field for the affected version.
    Expected Output:
    The following example shows you how to delete a staging label that is attached to a version of a secret. You can review the results by running the operation ListSecretVersionIds and viewing the VersionStages response field for the affected version.
    Expected Output:
    The following example shows you how to move a staging label that is attached to one version of a secret to a different version. You can review the results by running the operation ListSecretVersionIds and viewing the VersionStages response field for the affected version.
    Expected Output:
    
    :example: response = client.update_secret_version_stage(
        SecretId='string',
        VersionStage='string',
        RemoveFromVersionId='string',
        MoveToVersionId='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]\nSpecifies the secret with the version whose list of staging labels you want to modify. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.\n\nNote\nIf you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too\xe2\x80\x94for example, if you don\xe2\x80\x99t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you\xe2\x80\x99re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don\xe2\x80\x99t create secret names that end with a hyphen followed by six characters.\n\n

    :type VersionStage: string
    :param VersionStage: [REQUIRED]\nThe staging label to add to this version.\n

    :type RemoveFromVersionId: string
    :param RemoveFromVersionId: Specifies the secret version ID of the version that the staging label is to be removed from. If the staging label you are trying to attach to one version is already attached to a different version, then you must include this parameter and specify the version that the label is to be removed from. If the label is attached and you either do not specify this parameter, or the version ID does not match, then the operation fails.

    :type MoveToVersionId: string
    :param MoveToVersionId: (Optional) The secret version ID that you want to add the staging label to. If you want to remove a label from a version, then do not specify this parameter.\nIf the staging label is already attached to a different version of the secret, then you must also specify the RemoveFromVersionId parameter.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ARN': 'string',
    'Name': 'string'
}


Response Structure

(dict) --

ARN (string) --
The ARN of the secret with the staging label that was modified.

Name (string) --
The friendly name of the secret with the staging label that was modified.







Exceptions

SecretsManager.Client.exceptions.ResourceNotFoundException
SecretsManager.Client.exceptions.InvalidParameterException
SecretsManager.Client.exceptions.InvalidRequestException
SecretsManager.Client.exceptions.LimitExceededException
SecretsManager.Client.exceptions.InternalServiceError

Examples
The following example shows you how to add a staging label to a version of a secret. You can review the results by running the operation ListSecretVersionIds and viewing the VersionStages response field for the affected version.
response = client.update_secret_version_stage(
    MoveToVersionId='EXAMPLE1-90ab-cdef-fedc-ba987SECRET1',
    SecretId='MyTestDatabaseSecret',
    VersionStage='STAGINGLABEL1',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Name': 'MyTestDatabaseSecret',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example shows you how to delete a staging label that is attached to a version of a secret. You can review the results by running the operation ListSecretVersionIds and viewing the VersionStages response field for the affected version.
response = client.update_secret_version_stage(
    RemoveFromVersionId='EXAMPLE1-90ab-cdef-fedc-ba987SECRET1',
    SecretId='MyTestDatabaseSecret',
    VersionStage='STAGINGLABEL1',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Name': 'MyTestDatabaseSecret',
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example shows you how to move a staging label that is attached to one version of a secret to a different version. You can review the results by running the operation ListSecretVersionIds and viewing the VersionStages response field for the affected version.
response = client.update_secret_version_stage(
    MoveToVersionId='EXAMPLE2-90ab-cdef-fedc-ba987SECRET2',
    RemoveFromVersionId='EXAMPLE1-90ab-cdef-fedc-ba987SECRET1',
    SecretId='MyTestDatabaseSecret',
    VersionStage='AWSCURRENT',
)

print(response)


Expected Output:
{
    'ARN': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3',
    'Name': 'MyTestDatabaseSecret',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ARN': 'string',
        'Name': 'string'
    }
    
    
    :returns: 
    To get the list of staging labels that are currently associated with a version of a secret, use ``  DescribeSecret `` and examine the SecretVersionsToStages response value.
    
    """
    pass

