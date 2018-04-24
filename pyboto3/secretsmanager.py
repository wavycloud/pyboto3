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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

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
    
    
    :example: response = client.cancel_rotate_secret(
        SecretId='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]
            Specifies the secret for which you want to cancel a rotation request. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
            

    :rtype: dict
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
    Creates a new secret. A secret in AWS Secrets Manager consists of both the protected secret data and the important information needed to manage the secret.
    Secrets Manager stores the encrypted secret data in one of a collection of "versions" associated with the secret. Each version contains a copy of the encrypted secret data. Each version is associated with one or more "staging labels" that identify where the version is in the rotation cycle. The SecretVersionsToStages field of the secret contains the mapping of staging labels to the active versions of the secret. Versions without a staging label are considered deprecated and are not included in the list.
    You provide the secret data to be encrypted by putting text in the SecretString parameter or binary data in the SecretBinary parameter. If you include SecretString or SecretBinary then Secrets Manager also creates an initial secret version and, if you don't supply a staging label, automatically maps the new version's ID to the staging label AWSCURRENT .
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    
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
    :param Name: [REQUIRED]
            Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: /_+=.@- Spaces are not permitted.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) If you include SecretString or SecretBinary , then an initial version is created as part of the secret, and this parameter specifies a unique identifier for the new version.
            Note
            If you use the AWS CLI or one of the AWS SDK to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes as the value for this parameter in the request. If you don't use the SDK and instead generate a raw HTTP request to the AWS Secrets Manager service endpoint, then you must generate a ClientRequestToken yourself for the new version and include that value in the request.
            This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a UUID-type value to ensure uniqueness of your versions within the specified secret.
            If the ClientRequestToken value isn't already associated with a version of the secret then a new version of the secret is created.
            If a version with this value already exists and that version's SecretString and SecretBinary values are the same as those in the request, then the request is ignored (the operation is idempotent).
            If a version with this value already exists and that version's SecretString and SecretBinary values are different from those in the request then the request fails because you cannot modify an existing version. Instead, use PutSecretValue to create a new version.
            This value becomes the SecretVersionId of the new version.
            This field is autopopulated if not provided.
            

    :type Description: string
    :param Description: (Optional) Specifies a user-provided description of the secret.

    :type KmsKeyId: string
    :param KmsKeyId: (Optional) Specifies the ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the SecretString and SecretBinary values in the versions stored in this secret.
            If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named aws/secretsmanager ). If a KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time it needs to encrypt a version's SecretString or SecretBinary fields.
            Warning
            You can use the account's default CMK to encrypt and decrypt only if you call this operation using credentials from the same account that owns the secret. If the secret is in a different account, then you must create a custom CMK and specify the ARN in this field.
            

    :type SecretBinary: bytes
    :param SecretBinary: (Optional) Specifies binary data that you want to encrypt and store in the new version of the secret. To use this parameter in the command-line tools, we recommend that you store your binary data in a file and then use the appropriate technique for your tool to pass the contents of the file as a parameter.
            Either SecretString , SecretBinary , or both must have a value. They cannot both be empty.
            This SecretBinary value is stored separately from the SecretString , but the two parameters jointly share a maximum size limit.
            This parameter is not available using the Secrets Manager console. It can be accessed only by using the AWS CLI or one of the AWS SDKs.
            

    :type SecretString: string
    :param SecretString: (Optional) Specifies text data that you want to encrypt and store in this new version of the secret.
            Either SecretString , SecretBinary , or both must have a value. They cannot both be empty.
            This string value is stored separately from the SecretBinary , but the two parameters jointly share a maximum size limit.
            If you create a secret by using the Secrets Manager console then Secrets Manager puts the protected secret text in only the SecretString parameter. The Secrets Manager console stores the information as a JSON structure of key/value pairs that the Lambda rotation function knows how to parse.
            For storing multiple values, we recommend that you use a JSON text string argument and specify key/value pairs. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide . For example:
            [{'Key':'username','Value':'bob'},{'Key':'password','Value':'abc123xyz456'}]
            If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text.
            

    :type Tags: list
    :param Tags: (Optional) Specifies a list of user-defined tags that are attached to the secret. Each tag is a 'Key' and 'Value' pair of strings. This operation only appends tags to the existing list of tags. To remove tags, you must use UntagResource .
            Warning
            AWS Secrets Manager tag key names are case sensitive. A tag with the key 'ABC' is a different tag from one with key 'abc'.
            If you check tags in IAM policy Condition elements as part of your security strategy, then adding or removing a tag can change permissions. If the successful completion of this operation would result in you losing your permissions for this secret, then this operation is blocked and returns an Access Denied error.
            This parameter requires a JSON text string argument. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide . For example:
            [{'Key':'CostCenter','Value':'12345'},{'Key':'environment','Value':'production'}]
            If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text.
            The following basic restrictions apply to tags:
            Maximum number of tags per secret 50
            Maximum key length 127 Unicode characters in UTF-8
            Maximum value length 255 Unicode characters in UTF-8
            Tag keys and values are case sensitive.
            Do not use the aws: prefix in your tag names or values because it is reserved for AWS use. You can't edit or delete tag names or values with this prefix. Tags with this prefix do not count against your tags per secret limit.
            If your tagging schema will be used across multiple services and resources, remember that other services might have restrictions on allowed characters. Generally allowed characters are: letters, spaces, and numbers representable in UTF-8, plus the following special characters: + - = . _ : / @.
            (dict) --A structure that contains information about a tag.
            Key (string) --The key identifier, or name, of the tag.
            Value (string) --The string value that's associated with the key of the tag.
            
            

    :rtype: dict
    :return: {
        'ARN': 'string',
        'Name': 'string',
        'VersionId': 'string'
    }
    
    
    :returns: 
    secretsmanager:CreateSecret
    kms:GenerateDataKey - needed only if you use a customer-created KMS key to encrypt the secret. You do not need this permission to use the account's default AWS managed CMK for Secrets Manager.
    kms:Encrypt - needed only if you use a customer-created KMS key to encrypt the secret. You do not need this permission to use the account's default AWS managed CMK for Secrets Manager.
    
    """
    pass

def delete_secret(SecretId=None, RecoveryWindowInDays=None):
    """
    Deletes an entire secret and all of its versions. You can optionally include a recovery window during which you can restore the secret. If you don't provide a recovery window value, the operation defaults to 30 days. Secrets Manager attaches a DeletionDate stamp to the secret that specifies the end of the recovery window. At the end of the recovery window, Secrets Manager deletes the secret permanently.
    At any time before recovery period ends, you can use  RestoreSecret to remove the DeletionDate and cancel the deletion of the secret.
    You cannot access the encrypted secret information in any secret that is scheduled for deletion. If you need to access that information, you can cancel the deletion with  RestoreSecret and then retrieve the information.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    
    :example: response = client.delete_secret(
        SecretId='string',
        RecoveryWindowInDays=123
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]
            Specifies the secret that you want to delete. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
            

    :type RecoveryWindowInDays: integer
    :param RecoveryWindowInDays: (Optional) Specifies the number of days that AWS Secrets Manager waits before it can delete the secret.
            This value can range from 7 to 30 days. The default value is 30.
            

    :rtype: dict
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
    
    
    :example: response = client.describe_secret(
        SecretId='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]
            The identifier of the secret whose details you want to retrieve. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
            

    :rtype: dict
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
        }
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

def get_random_password(PasswordLength=None, ExcludeCharacters=None, ExcludeNumbers=None, ExcludePunctuation=None, ExcludeUppercase=None, ExcludeLowercase=None, IncludeSpace=None, RequireEachIncludedType=None):
    """
    Generates a random password of the specified complexity. This operation is intended for use in the Lambda rotation function. Per best practice, we recommend that you specify the maximum length and include every character type that the system you are generating a password for can support.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    
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
    :param ExcludePunctuation: Specifies that the generated password should not include punctuation characters. The default if you do not include this switch parameter is that punctuation characters can be included.

    :type ExcludeUppercase: boolean
    :param ExcludeUppercase: Specifies that the generated password should not include uppercase letters. The default if you do not include this switch parameter is that uppercase letters can be included.

    :type ExcludeLowercase: boolean
    :param ExcludeLowercase: Specifies that the generated password should not include lowercase letters. The default if you do not include this switch parameter is that lowercase letters can be included.

    :type IncludeSpace: boolean
    :param IncludeSpace: Specifies that the generated password can include the space character. The default if you do not include this switch parameter is that the space character is not included.

    :type RequireEachIncludedType: boolean
    :param RequireEachIncludedType: A boolean value that specifies whether the generated password must include at least one of every allowed character type. The default value is True and the operation requires at least one of every character type.

    :rtype: dict
    :return: {
        'RandomPassword': 'string'
    }
    
    
    :returns: 
    PasswordLength (integer) -- The desired length of the generated password. The default value if you do not include this parameter is 32 characters.
    ExcludeCharacters (string) -- A string that includes characters that should not be included in the generated password. The default is that all characters from the included sets can be used.
    ExcludeNumbers (boolean) -- Specifies that the generated password should not include digits. The default if you do not include this switch parameter is that digits can be included.
    ExcludePunctuation (boolean) -- Specifies that the generated password should not include punctuation characters. The default if you do not include this switch parameter is that punctuation characters can be included.
    ExcludeUppercase (boolean) -- Specifies that the generated password should not include uppercase letters. The default if you do not include this switch parameter is that uppercase letters can be included.
    ExcludeLowercase (boolean) -- Specifies that the generated password should not include lowercase letters. The default if you do not include this switch parameter is that lowercase letters can be included.
    IncludeSpace (boolean) -- Specifies that the generated password can include the space character. The default if you do not include this switch parameter is that the space character is not included.
    RequireEachIncludedType (boolean) -- A boolean value that specifies whether the generated password must include at least one of every allowed character type. The default value is True and the operation requires at least one of every character type.
    
    """
    pass

def get_secret_value(SecretId=None, VersionId=None, VersionStage=None):
    """
    Retrieves the contents of the encrypted fields SecretString and SecretBinary from the specified version of a secret.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    
    :example: response = client.get_secret_value(
        SecretId='string',
        VersionId='string',
        VersionStage='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]
            Specifies the secret containing the version that you want to retrieve. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
            

    :type VersionId: string
    :param VersionId: Specifies the unique identifier of the version of the secret that you want to retrieve. If you specify this parameter then don't specify VersionStage . If you don't specify either a VersionStage or SecretVersionId then the default is to perform the operation on the version with the VersionStage value of AWSCURRENT .
            This value is typically a UUID-type value with 32 hexadecimal digits.
            

    :type VersionStage: string
    :param VersionStage: Specifies the secret version that you want to retrieve by the staging label attached to the version.
            Staging labels are used to keep track of different versions during the rotation process. If you use this parameter then don't specify SecretVersionId . If you don't specify either a VersionStage or SecretVersionId , then the default is to perform the operation on the version with the VersionStage value of AWSCURRENT .
            

    :rtype: dict
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

def get_waiter():
    """
    
    """
    pass

def list_secret_version_ids(SecretId=None, MaxResults=None, NextToken=None, IncludeDeprecated=None):
    """
    Lists all of the versions attached to the specified secret. The output does not include the SecretString or SecretBinary fields. By default, the list includes only versions that have at least one staging label in VersionStage attached.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    
    :example: response = client.list_secret_version_ids(
        SecretId='string',
        MaxResults=123,
        NextToken='string',
        IncludeDeprecated=True|False
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]
            The identifier for the secret containing the versions you want to list. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
            

    :type MaxResults: integer
    :param MaxResults: (Optional) Limits the number of results that you want to include in the response. If you don't include this parameter, it defaults to a value that's specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (isn't null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that AWS Secrets Manager might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :type NextToken: string
    :param NextToken: (Optional) Use this parameter in a request if you receive a NextToken response in a previous request that indicates that there's more output available. In a subsequent call, set it to the value of the previous call's NextToken response to indicate where the output should continue from.

    :type IncludeDeprecated: boolean
    :param IncludeDeprecated: (Optional) Specifies that you want the results to include versions that do not have any staging labels attached to them. Such versions are considered deprecated and are subject to deletion by Secrets Manager as needed.

    :rtype: dict
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
    Lists all of the secrets that are stored by AWS Secrets Manager in the AWS account. To list the versions currently stored for a specific secret, use  ListSecretVersionIds . The encrypted fields SecretString and SecretBinary are not included in the output. To get that information, call the  GetSecretValue operation.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    
    :example: response = client.list_secrets(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: (Optional) Limits the number of results that you want to include in the response. If you don't include this parameter, it defaults to a value that's specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (isn't null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that AWS Secrets Manager might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :type NextToken: string
    :param NextToken: (Optional) Use this parameter in a request if you receive a NextToken response in a previous request that indicates that there's more output available. In a subsequent call, set it to the value of the previous call's NextToken response to indicate where the output should continue from.

    :rtype: dict
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
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    To list the versions attached to a secret, use  ListSecretVersionIds .
    
    """
    pass

def put_secret_value(SecretId=None, ClientRequestToken=None, SecretBinary=None, SecretString=None, VersionStages=None):
    """
    Stores a new encrypted secret value in the specified secret. To do this, the operation creates a new version and attaches it to the secret. The version can contain a new SecretString value or a new SecretBinary value.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    
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
    :param SecretId: [REQUIRED]
            Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.
            The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: /_+=.@- Spaces are not permitted.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) Specifies a unique identifier for the new version of the secret.
            Note
            If you use the AWS CLI or one of the AWS SDK to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes that in the request. If you don't use the SDK and instead generate a raw HTTP request to the AWS Secrets Manager service endpoint, then you must generate a ClientRequestToken yourself for new versions and include that value in the request.
            This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during the Lambda rotation function's processing. We recommend that you generate a UUID-type value to ensure uniqueness within the specified secret.
            If the ClientRequestToken value isn't already associated with a version of the secret then a new version of the secret is created.
            If a version with this value already exists and that version's SecretString or SecretBinary values are the same as those in the request then the request is ignored (the operation is idempotent).
            If a version with this value already exists and that version's SecretString and SecretBinary values are different from those in the request then the request fails because you cannot modify an existing secret version. You can only create new versions to store new secret values.
            This value becomes the SecretVersionId of the new version.
            This field is autopopulated if not provided.
            

    :type SecretBinary: bytes
    :param SecretBinary: (Optional) Specifies binary data that you want to encrypt and store in the new version of the secret. To use this parameter in the command-line tools, we recommend that you store your binary data in a file and then use the appropriate technique for your tool to pass the contents of the file as a parameter. Either SecretBinary or SecretString must have a value. They cannot both be empty.
            This parameter is not accessible if the secret using the Secrets Manager console.
            

    :type SecretString: string
    :param SecretString: (Optional) Specifies text data that you want to encrypt and store in this new version of the secret. Either SecretString or SecretBinary must have a value. They cannot both be empty.
            If you create this secret by using the Secrets Manager console then Secrets Manager puts the protected secret text in only the SecretString parameter. The Secrets Manager console stores the information as a JSON structure of key/value pairs that the default Lambda rotation function knows how to parse.
            For storing multiple values, we recommend that you use a JSON text string argument and specify key/value pairs. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide .
            

    :type VersionStages: list
    :param VersionStages: (Optional) Specifies a list of staging labels that are attached to this version of the secret. These staging labels are used to track the versions through the rotation process by the Lambda rotation function.
            A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version.
            If you do not specify a value for VersionStages then AWS Secrets Manager automatically moves the staging label AWSCURRENT to this new version.
            (string) --
            

    :rtype: dict
    :return: {
        'ARN': 'string',
        'Name': 'string',
        'VersionId': 'string',
        'VersionStages': [
            'string',
        ]
    }
    
    
    :returns: 
    If you call an operation that needs to encrypt or decrypt the SecretString and SecretBinary for a secret in the same account as the calling user and that secret doesn't specify a KMS encryption key, AWS Secrets Manager uses the account's default AWS managed customer master key (CMK) with the alias aws/secretsmanager . If this key doesn't already exist in your account then AWS Secrets Manager creates it for you automatically. All users in the same AWS account automatically have access to use the default CMK. Note that if an AWS Secrets Manager API call results in AWS having to create the account's AWS-managed CMK, it can result in a one-time significant delay in returning the result.
    If the secret is in a different AWS account from the credentials calling an API that requires encryption or decryption of the secret value then you must create and use a custom KMS CMK because you can't access the default CMK for the account using credentials from a different AWS account. Store the ARN of the CMK in the secret when you create the secret or when you update it by including it in the KMSKeyId . If you call an API that must encrypt or decrypt SecretString or SecretBinary using credentials from a different account then the KMS key policy must grant cross-account access to that other account's user or role.
    
    """
    pass

def restore_secret(SecretId=None):
    """
    Cancels the scheduled deletion of a secret by removing the DeletedDate time stamp. This makes the secret accessible to query once again.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    
    :example: response = client.restore_secret(
        SecretId='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]
            Specifies the secret that you want to restore from a previously scheduled deletion. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
            

    :rtype: dict
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
    The rotation function must end with the versions of the secret in one of two states:
    If instead the AWSPENDING staging label is present but is not attached to the same version as AWSCURRENT then any later invocation of RotateSecret assumes that a previous rotation request is still in progress and returns an error.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    
    :example: response = client.rotate_secret(
        SecretId='string',
        ClientRequestToken='string',
        RotationLambdaARN='string',
        RotationRules={
            'AutomaticallyAfterDays': 123
        }
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]
            Specifies the secret that you want to rotate. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) Specifies a unique identifier for the new version of the secret that helps ensure idempotency.
            If you use the AWS CLI or one of the AWS SDK to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes that in the request for this parameter. If you don't use the SDK and instead generate a raw HTTP request to the AWS Secrets Manager service endpoint, then you must generate a ClientRequestToken yourself for new versions and include that value in the request.
            You only need to specify your own value if you are implementing your own retry logic and want to ensure that a given secret is not created twice. We recommend that you generate a UUID-type value to ensure uniqueness within the specified secret.
            Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during the function's processing.
            If the ClientRequestToken value isn't already associated with a version of the secret then a new version of the secret is created.
            If a version with this value already exists and that version's SecretString and SecretBinary values are the same as the request, then the request is ignored (the operation is idempotent).
            If a version with this value already exists and that version's SecretString and SecretBinary values are different from the request then an error occurs because you cannot modify an existing secret value.
            This value becomes the SecretVersionId of the new version.
            This field is autopopulated if not provided.
            

    :type RotationLambdaARN: string
    :param RotationLambdaARN: (Optional) Specifies the ARN of the Lambda function that can rotate the secret.

    :type RotationRules: dict
    :param RotationRules: A structure that defines the rotation configuration for this secret.
            AutomaticallyAfterDays (integer) --Specifies the number of days between automatic scheduled rotations of the secret.
            

    :rtype: dict
    :return: {
        'ARN': 'string',
        'Name': 'string',
        'VersionId': 'string'
    }
    
    
    :returns: 
    secretsmanager:RotateSecret
    lambda:InvokeFunction (on the function specified in the secret's metadata)
    
    """
    pass

def tag_resource(SecretId=None, Tags=None):
    """
    Attaches one or more tags, each consisting of a key name and a value, to the specified secret. Tags are part of the secret's overall metadata, and are not associated with any specific version of the secret. This operation only appends tags to the existing list of tags. To remove tags, you must use  UntagResource .
    The following basic restrictions apply to tags:
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    
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
    :param SecretId: [REQUIRED]
            The identifier for the secret that you want to attach tags to. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The tags to attach to the secret. Each element in the list consists of a Key and a Value .
            This parameter to the API requires a JSON text string argument. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide . For the AWS CLI, you can also use the syntax: --Tags Key='Key1',Value='Value1',Key='Key2',Value='Value2'[, ]
            (dict) --A structure that contains information about a tag.
            Key (string) --The key identifier, or name, of the tag.
            Value (string) --The string value that's associated with the key of the tag.
            
            

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
    
    
    :example: response = client.untag_resource(
        SecretId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]
            The identifier for the secret that you want to remove tags from. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            A list of tag key names to remove from the secret. You don't specify the value. Both the key and its associated value are removed.
            This parameter to the API requires a JSON text string argument. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide .
            (string) --
            

    :returns: 
    To add one or more tags to the collection attached to a secret, use  TagResource .
    To view the list of tags attached to a secret, use  DescribeSecret .
    
    """
    pass

def update_secret(SecretId=None, ClientRequestToken=None, Description=None, KmsKeyId=None, SecretBinary=None, SecretString=None):
    """
    Modifies many of the details of a secret. If you include a ClientRequestToken and either SecretString or SecretBinary then it also creates a new version attached to the secret.
    To modify the rotation configuration of a secret, use  RotateSecret instead.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    
    :example: response = client.update_secret(
        SecretId='string',
        ClientRequestToken='string',
        Description='string',
        KmsKeyId='string',
        SecretBinary=b'bytes',
        SecretString='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]
            Specifies the secret that you want to update or to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) If you want to add a new version to the secret, this parameter specifies a unique identifier for the new version that helps ensure idempotency.
            If you use the AWS CLI or one of the AWS SDK to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes that in the request. If you don't use the SDK and instead generate a raw HTTP request to the AWS Secrets Manager service endpoint, then you must generate a ClientRequestToken yourself for new versions and include that value in the request.
            You typically only need to interact with this value if you implement your own retry logic and want to ensure that a given secret is not created twice. We recommend that you generate a UUID-type value to ensure uniqueness within the specified secret.
            Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during the Lambda rotation function's processing.
            If the ClientRequestToken value isn't already associated with a version of the secret then a new version of the secret is created.
            If a version with this value already exists and that version's SecretString and SecretBinary values are the same as those in the request then the request is ignored (the operation is idempotent).
            If a version with this value already exists and that version's SecretString and SecretBinary values are different from the request then an error occurs because you cannot modify an existing secret value.
            This value becomes the SecretVersionId of the new version.
            This field is autopopulated if not provided.
            

    :type Description: string
    :param Description: (Optional) Specifies a user-provided description of the secret.

    :type KmsKeyId: string
    :param KmsKeyId: (Optional) Specifies the ARN or alias of the KMS customer master key (CMK) to be used to encrypt the protected text in the versions of this secret.
            If you don't specify this value, then Secrets Manager defaults to using the default CMK in the account (the one named aws/secretsmanager ). If a KMS CMK with that name doesn't exist, then AWS Secrets Manager creates it for you automatically the first time it needs to encrypt a version's Plaintext or PlaintextString fields.
            Warning
            You can only use the account's default CMK to encrypt and decrypt if you call this operation using credentials from the same account that owns the secret. If the secret is in a different account, then you must create a custom CMK and provide the ARN in this field.
            

    :type SecretBinary: bytes
    :param SecretBinary: (Optional) Specifies binary data that you want to encrypt and store in the new version of the secret. To use this parameter in the command-line tools, we recommend that you store your binary data in a file and then use the appropriate technique for your tool to pass the contents of the file as a parameter. Either SecretBinary or SecretString must have a value. They cannot both be empty.
            This parameter is not accessible using the Secrets Manager console.
            

    :type SecretString: string
    :param SecretString: (Optional) Specifies text data that you want to encrypt and store in this new version of the secret. Either SecretBinary or SecretString must have a value. They cannot both be empty.
            If you create this secret by using the Secrets Manager console then Secrets Manager puts the protected secret text in only the SecretString parameter. The Secrets Manager console stores the information as a JSON structure of key/value pairs that the default Lambda rotation function knows how to parse.
            For storing multiple values, we recommend that you use a JSON text string argument and specify key/value pairs. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide .
            

    :rtype: dict
    :return: {
        'ARN': 'string',
        'Name': 'string',
        'VersionId': 'string'
    }
    
    
    :returns: 
    If you call an operation that needs to encrypt or decrypt the SecretString and SecretBinary for a secret in the same account as the calling user and that secret doesn't specify a KMS encryption key, AWS Secrets Manager uses the account's default AWS managed customer master key (CMK) with the alias aws/secretsmanager . If this key doesn't already exist in your account then AWS Secrets Manager creates it for you automatically. All users in the same AWS account automatically have access to use the default CMK. Note that if an AWS Secrets Manager API call results in AWS having to create the account's AWS-managed CMK, it can result in a one-time significant delay in returning the result.
    If the secret is in a different AWS account from the credentials calling an API that requires encryption or decryption of the secret value then you must create and use a custom KMS CMK because you can't access the default CMK for the account using credentials from a different AWS account. Store the ARN of the CMK in the secret when you create the secret or when you update it by including it in the KMSKeyId . If you call an API that must encrypt or decrypt SecretString or SecretBinary using credentials from a different account then the KMS key policy must grant cross-account access to that other account's user or role.
    
    """
    pass

def update_secret_version_stage(SecretId=None, VersionStage=None, RemoveFromVersionId=None, MoveToVersionId=None):
    """
    Modifies the staging labels attached to a version of a secret. Staging labels are used to track a version as it progresses through the secret rotation process. You can attach a staging label to only one version of a secret at a time. If a staging label to be added is already attached to another version, then it is moved--removed from the other version first and then attached to this one. For more information about staging labels, see Staging Labels in the AWS Secrets Manager User Guide .
    The staging labels that you specify in the VersionStage parameter are added to the existing list of staging labels--they don't replace it.
    You can move the AWSCURRENT staging label to this version by including it in this call.
    If this action results in the last label being removed from a version, then the version is considered to be 'deprecated' and can be deleted by Secrets Manager.
    To run this command, you must have the following permissions:
    See also: AWS API Documentation
    
    
    :example: response = client.update_secret_version_stage(
        SecretId='string',
        VersionStage='string',
        RemoveFromVersionId='string',
        MoveToVersionId='string'
    )
    
    
    :type SecretId: string
    :param SecretId: [REQUIRED]
            Specifies the secret with the version whose list of staging labels you want to modify. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
            

    :type VersionStage: string
    :param VersionStage: [REQUIRED]
            The list of staging labels to add to this version.
            

    :type RemoveFromVersionId: string
    :param RemoveFromVersionId: (Optional) Specifies the secret version ID of the version that the staging labels are to be removed from.
            If you want to move a label to a new version, you do not have to explicitly remove it with this parameter. Adding a label using the MoveToVersionId parameter automatically removes it from the old version. However, if you do include both the 'MoveTo' and 'RemoveFrom' parameters, then the move is successful only if the staging labels are actually present on the 'RemoveFrom' version. If a staging label was on a different version than 'RemoveFrom', then the request fails.
            

    :type MoveToVersionId: string
    :param MoveToVersionId: (Optional) The secret version ID that you want to add the staging labels to.
            If any of the staging labels are already attached to a different version of the secret, then they are removed from that version before adding them to this version.
            

    :rtype: dict
    :return: {
        'ARN': 'string',
        'Name': 'string'
    }
    
    
    :returns: 
    To get the list of staging labels that are currently associated with a version of a secret, use ``  DescribeSecret `` and examine the SecretVersionsToStages response value.
    
    """
    pass

