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


def cancel_key_deletion(KeyId=None):
    """
    :param KeyId: [REQUIRED]
            The unique identifier for the customer master key (CMK) for which to cancel deletion.
            To specify this value, use the unique key ID or the Amazon Resource Name (ARN) of the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            Key ARN: arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            To obtain the unique key ID and key ARN for a given CMK, use ListKeys or DescribeKey .
            Return typedict
            ReturnsResponse Syntax{
              'KeyId': 'string'
            }
            Response Structure
            (dict) --
            KeyId (string) --The unique identifier of the master key for which deletion is canceled.
            
            
    :type KeyId: string
    """
    pass


def create_alias(AliasName=None, TargetKeyId=None):
    """
    :param AliasName: [REQUIRED]
            String that contains the display name. The name must start with the word 'alias' followed by a forward slash (alias/). Aliases that begin with 'alias/AWS' are reserved.
            
    :type AliasName: string
    :param TargetKeyId: [REQUIRED]
            An identifier of the key for which you are creating the alias. This value cannot be another alias but can be a globally unique identifier or a fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            
    :type TargetKeyId: string
    """
    pass


def create_grant(KeyId=None, GranteePrincipal=None, RetiringPrincipal=None, Operations=None, Constraints=None,
                 GrantTokens=None, Name=None):
    """
    :param KeyId: [REQUIRED]
            The unique identifier for the customer master key (CMK) that the grant applies to.
            To specify this value, use the globally unique key ID or the Amazon Resource Name (ARN) of the key. Examples:
            Globally unique key ID: 12345678-1234-1234-1234-123456789012
            Key ARN: arn:aws:kms:us-west-2:123456789012:key/12345678-1234-1234-1234-123456789012
            
    :type KeyId: string
    :param GranteePrincipal: [REQUIRED]
            The principal that is given permission to perform the operations that the grant permits.
            To specify the principal, use the Amazon Resource Name (ARN) of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, federated users, and assumed role users. For examples of the ARN syntax to use for specifying a principal, see AWS Identity and Access Management (IAM) in the Example ARNs section of the AWS General Reference .
            
    :type GranteePrincipal: string
    :param RetiringPrincipal: The principal that is given permission to retire the grant by using RetireGrant operation.
            To specify the principal, use the Amazon Resource Name (ARN) of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, federated users, and assumed role users. For examples of the ARN syntax to use for specifying a principal, see AWS Identity and Access Management (IAM) in the Example ARNs section of the AWS General Reference .
            
    :type RetiringPrincipal: string
    :param Operations: A list of operations that the grant permits. The list can contain any combination of one or more of the following values:
            Decrypt
            Encrypt
            GenerateDataKey
            GenerateDataKeyWithoutPlaintext
            ReEncryptFrom
            ReEncryptTo
            CreateGrant
            RetireGrant
            DescribeKey
            (string) --
            
    :type Operations: list
    :param Constraints: The conditions under which the operations permitted by the grant are allowed.
            You can use this value to allow the operations permitted by the grant only when a specified encryption context is present. For more information, see Encryption Context in the AWS Key Management Service Developer Guide .
            EncryptionContextSubset (dict) --Contains a list of key-value pairs, a subset of which must be present in the encryption context of a subsequent operation permitted by the grant. When a subsequent operation permitted by the grant includes an encryption context that matches this list or is a subset of this list, the grant allows the operation. Otherwise, the operation is not allowed.
            (string) --
            (string) --
            
            EncryptionContextEquals (dict) --Contains a list of key-value pairs that must be present in the encryption context of a subsequent operation permitted by the grant. When a subsequent operation permitted by the grant includes an encryption context that matches this list, the grant allows the operation. Otherwise, the operation is not allowed.
            (string) --
            (string) --
            
            
    :type Constraints: dict
    :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            
    :type GrantTokens: list
    :param Name: A friendly name for identifying the grant. Use this value to prevent unintended creation of duplicate grants when retrying this request.
            When this value is absent, all CreateGrant requests result in a new grant with a unique GrantId even if all the supplied parameters are identical. This can result in unintended duplicates when you retry the CreateGrant request.
            When this value is present, you can retry a CreateGrant request with identical parameters; if the grant already exists, the original GrantId is returned without creating a new grant. Note that the returned grant token is unique with every CreateGrant request, even when a duplicate GrantId is returned. All grant tokens obtained in this way can be used interchangeably.
            
    :type Name: string
    """
    pass


def create_key(Policy=None, Description=None, KeyUsage=None, Origin=None, BypassPolicyLockoutSafetyCheck=None):
    """
    :param Policy: The key policy to attach to the CMK.
            If you specify a policy and do not set BypassPolicyLockoutSafetyCheck to true, the policy must meet the following criteria:
            It must allow the principal making the CreateKey request to make a subsequent PutKeyPolicy request on the CMK. This reduces the likelihood that the CMK becomes unmanageable. For more information, refer to the scenario in the Default Key Policy section in the AWS Key Management Service Developer Guide .
            The principal(s) specified in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before specifying the new principal in a key policy because the new principal might not immediately be visible to AWS KMS. For more information, see Changes that I make are not always immediately visible in the IAM User Guide .
            If you do not specify a policy, AWS KMS attaches a default key policy to the CMK. For more information, see Default Key Policy in the AWS Key Management Service Developer Guide .
            The policy size limit is 32 KiB (32768 bytes).
            
    :type Policy: string
    :param Description: A description of the CMK.
            Use a description that helps you decide whether the CMK is appropriate for a task.
            
    :type Description: string
    :param KeyUsage: The intended use of the CMK.
            You can use CMKs only for symmetric encryption and decryption.
            
    :type KeyUsage: string
    :param Origin: The source of the CMK's key material.
            The default is AWS_KMS , which means AWS KMS creates the key material. When this parameter is set to EXTERNAL , the request creates a CMK without key material so that you can import key material from your existing key management infrastructure. For more information about importing key material into AWS KMS, see Importing Key Material in the AWS Key Management Service Developer Guide .
            The CMK's Origin is immutable and is set when the CMK is created.
            
    :type Origin: string
    :param BypassPolicyLockoutSafetyCheck: A flag to indicate whether to bypass the key policy lockout safety check.
            Warning
            Setting this value to true increases the likelihood that the CMK becomes unmanageable. Do not set this value to true indiscriminately.
            For more information, refer to the scenario in the Default Key Policy section in the AWS Key Management Service Developer Guide .
            Use this parameter only when you include a policy in the request and you intend to prevent the principal making the request from making a subsequent PutKeyPolicy request on the CMK.
            The default value is false.
            
    :type BypassPolicyLockoutSafetyCheck: boolean
    """
    pass


def decrypt(CiphertextBlob=None, EncryptionContext=None, GrantTokens=None):
    """
    :param CiphertextBlob: [REQUIRED]
            Ciphertext to be decrypted. The blob includes metadata.
            
    :type CiphertextBlob: bytes
    :param EncryptionContext: The encryption context. If this was specified in the Encrypt function, it must be specified here or the decryption operation will fail. For more information, see Encryption Context .
            (string) --
            (string) --
            
    :type EncryptionContext: dict
    :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            
    :type GrantTokens: list
    """
    pass


def delete_alias(AliasName=None):
    """
    :param AliasName: [REQUIRED]
            The alias to be deleted. The name must start with the word 'alias' followed by a forward slash (alias/). Aliases that begin with 'alias/AWS' are reserved.
            ReturnsNone
            
    :type AliasName: string
    """
    pass


def delete_imported_key_material(KeyId=None):
    """
    :param KeyId: [REQUIRED]
            The identifier of the CMK whose key material to delete. The CMK's Origin must be EXTERNAL .
            A valid identifier is the unique key ID or the Amazon Resource Name (ARN) of the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            Key ARN: arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            ReturnsNone
            
    :type KeyId: string
    """
    pass


def describe_key(KeyId=None, GrantTokens=None):
    """
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by 'alias/'.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Alias ARN Example - arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            Alias Name Example - alias/MyAliasName
            
    :type KeyId: string
    :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            
    :type GrantTokens: list
    """
    pass


def disable_key(KeyId=None):
    """
    :param KeyId: [REQUIRED]
            A unique identifier for the CMK.
            Use the CMK's unique identifier or its Amazon Resource Name (ARN). For example:
            Unique ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            ARN: arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            ReturnsNone
            
    :type KeyId: string
    """
    pass


def disable_key_rotation(KeyId=None):
    """
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            ReturnsNone
            
    :type KeyId: string
    """
    pass


def enable_key(KeyId=None):
    """
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            ReturnsNone
            
    :type KeyId: string
    """
    pass


def enable_key_rotation(KeyId=None):
    """
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            ReturnsNone
            
    :type KeyId: string
    """
    pass


def encrypt(KeyId=None, Plaintext=None, EncryptionContext=None, GrantTokens=None):
    """
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by 'alias/'.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Alias ARN Example - arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            Alias Name Example - alias/MyAliasName
            
    :type KeyId: string
    :param Plaintext: [REQUIRED]
            Data to be encrypted.
            
    :type Plaintext: bytes
    :param EncryptionContext: Name-value pair that specifies the encryption context to be used for authenticated encryption. If used here, the same value must be supplied to the Decrypt API or decryption will fail. For more information, see Encryption Context .
            (string) --
            (string) --
            
    :type EncryptionContext: dict
    :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            
    :type GrantTokens: list
    """
    pass


def generate_data_key(KeyId=None, EncryptionContext=None, NumberOfBytes=None, KeySpec=None, GrantTokens=None):
    """
    :param KeyId: [REQUIRED]
            The identifier of the CMK under which to generate and encrypt the data encryption key.
            A valid identifier is the unique key ID or the Amazon Resource Name (ARN) of the CMK, or the alias name or ARN of an alias that points to the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            CMK ARN: arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            Alias name: alias/ExampleAlias
            Alias ARN: arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias
            
    :type KeyId: string
    :param EncryptionContext: A set of key-value pairs that represents additional authenticated data.
            For more information, see Encryption Context in the AWS Key Management Service Developer Guide .
            (string) --
            (string) --
            
    :type EncryptionContext: dict
    :param NumberOfBytes: The length of the data encryption key in bytes. For example, use the value 64 to generate a 512-bit data key (64 bytes is 512 bits). For common key lengths (128-bit and 256-bit symmetric keys), we recommend that you use the KeySpec field instead of this one.
    :type NumberOfBytes: integer
    :param KeySpec: The length of the data encryption key. Use AES_128 to generate a 128-bit symmetric key, or AES_256 to generate a 256-bit symmetric key.
    :type KeySpec: string
    :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            
    :type GrantTokens: list
    """
    pass


def generate_data_key_without_plaintext(KeyId=None, EncryptionContext=None, KeySpec=None, NumberOfBytes=None,
                                        GrantTokens=None):
    """
    :param KeyId: [REQUIRED]
            The identifier of the CMK under which to generate and encrypt the data encryption key.
            A valid identifier is the unique key ID or the Amazon Resource Name (ARN) of the CMK, or the alias name or ARN of an alias that points to the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            CMK ARN: arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            Alias name: alias/ExampleAlias
            Alias ARN: arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias
            
    :type KeyId: string
    :param EncryptionContext: A set of key-value pairs that represents additional authenticated data.
            For more information, see Encryption Context in the AWS Key Management Service Developer Guide .
            (string) --
            (string) --
            
    :type EncryptionContext: dict
    :param KeySpec: The length of the data encryption key. Use AES_128 to generate a 128-bit symmetric key, or AES_256 to generate a 256-bit symmetric key.
    :type KeySpec: string
    :param NumberOfBytes: The length of the data encryption key in bytes. For example, use the value 64 to generate a 512-bit data key (64 bytes is 512 bits). For common key lengths (128-bit and 256-bit symmetric keys), we recommend that you use the KeySpec field instead of this one.
    :type NumberOfBytes: integer
    :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            
    :type GrantTokens: list
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


def generate_random(NumberOfBytes=None):
    """
    :param NumberOfBytes: The length of the byte string.
            Return typedict
            ReturnsResponse Syntax{
              'Plaintext': b'bytes'
            }
            Response Structure
            (dict) --
            Plaintext (bytes) --The unpredictable byte string.
            
            
    :type NumberOfBytes: integer
    """
    pass


def get_key_policy(KeyId=None, PolicyName=None):
    """
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            
    :type KeyId: string
    :param PolicyName: [REQUIRED]
            String that contains the name of the policy. Currently, this must be 'default'. Policy names can be discovered by calling ListKeyPolicies .
            
    :type PolicyName: string
    """
    pass


def get_key_rotation_status(KeyId=None):
    """
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            Return typedict
            ReturnsResponse Syntax{
              'KeyRotationEnabled': True|False
            }
            Response Structure
            (dict) --
            KeyRotationEnabled (boolean) --A Boolean value that specifies whether key rotation is enabled.
            
            
    :type KeyId: string
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


def get_parameters_for_import(KeyId=None, WrappingAlgorithm=None, WrappingKeySpec=None):
    """
    :param KeyId: [REQUIRED]
            The identifier of the CMK into which you will import key material. The CMK's Origin must be EXTERNAL .
            A valid identifier is the unique key ID or the Amazon Resource Name (ARN) of the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            Key ARN: arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            
    :type KeyId: string
    :param WrappingAlgorithm: [REQUIRED]
            The algorithm you will use to encrypt the key material before importing it with ImportKeyMaterial . For more information, see Encrypt the Key Material in the AWS Key Management Service Developer Guide .
            
    :type WrappingAlgorithm: string
    :param WrappingKeySpec: [REQUIRED]
            The type of wrapping key (public key) to return in the response. Only 2048-bit RSA public keys are supported.
            
    :type WrappingKeySpec: string
    """
    pass


def get_waiter():
    """
    """
    pass


def import_key_material(KeyId=None, ImportToken=None, EncryptedKeyMaterial=None, ValidTo=None, ExpirationModel=None):
    """
    :param KeyId: [REQUIRED]
            The identifier of the CMK to import the key material into. The CMK's Origin must be EXTERNAL .
            A valid identifier is the unique key ID or the Amazon Resource Name (ARN) of the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            Key ARN: arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            
    :type KeyId: string
    :param ImportToken: [REQUIRED]
            The import token that you received in the response to a previous GetParametersForImport request. It must be from the same response that contained the public key that you used to encrypt the key material.
            
    :type ImportToken: bytes
    :param EncryptedKeyMaterial: [REQUIRED]
            The encrypted key material to import. It must be encrypted with the public key that you received in the response to a previous GetParametersForImport request, using the wrapping algorithm that you specified in that request.
            
    :type EncryptedKeyMaterial: bytes
    :param ValidTo: The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. You must omit this parameter when the ExpirationModel parameter is set to KEY_MATERIAL_DOES_NOT_EXPIRE . Otherwise it is required.
    :type ValidTo: datetime
    :param ExpirationModel: Specifies whether the key material expires. The default is KEY_MATERIAL_EXPIRES , in which case you must include the ValidTo parameter. When this parameter is set to KEY_MATERIAL_DOES_NOT_EXPIRE , you must omit the ValidTo parameter.
    :type ExpirationModel: string
    """
    pass


def list_aliases(Limit=None, Marker=None):
    """
    :param Limit: When paginating results, specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the Truncated element in the response is set to true.
            This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.
            
    :type Limit: integer
    :param Marker: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the response you just received.
    :type Marker: string
    """
    pass


def list_grants(Limit=None, Marker=None, KeyId=None):
    """
    :param Limit: When paginating results, specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the Truncated element in the response is set to true.
            This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.
            
    :type Limit: integer
    :param Marker: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the response you just received.
    :type Marker: string
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            
    :type KeyId: string
    """
    pass


def list_key_policies(KeyId=None, Limit=None, Marker=None):
    """
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by 'alias/'.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Alias ARN Example - arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            Alias Name Example - alias/MyAliasName
            
    :type KeyId: string
    :param Limit: When paginating results, specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the Truncated element in the response is set to true.
            This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.
            Currently only 1 policy can be attached to a key.
            
    :type Limit: integer
    :param Marker: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the response you just received.
    :type Marker: string
    """
    pass


def list_keys(Limit=None, Marker=None):
    """
    :param Limit: When paginating results, specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the Truncated element in the response is set to true.
            This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.
            
    :type Limit: integer
    :param Marker: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the response you just received.
    :type Marker: string
    """
    pass


def list_retirable_grants(Limit=None, Marker=None, RetiringPrincipal=None):
    """
    :param Limit: When paginating results, specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the Truncated element in the response is set to true.
            This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.
            
    :type Limit: integer
    :param Marker: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the response you just received.
    :type Marker: string
    :param RetiringPrincipal: [REQUIRED]
            The retiring principal for which to list grants.
            To specify the retiring principal, use the Amazon Resource Name (ARN) of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, federated users, and assumed role users. For examples of the ARN syntax for specifying a principal, see AWS Identity and Access Management (IAM) in the Example ARNs section of the Amazon Web Services General Reference .
            
    :type RetiringPrincipal: string
    """
    pass


def put_key_policy(KeyId=None, PolicyName=None, Policy=None, BypassPolicyLockoutSafetyCheck=None):
    """
    :param KeyId: [REQUIRED]
            A unique identifier for the CMK.
            Use the CMK's unique identifier or its Amazon Resource Name (ARN). For example:
            Unique ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            ARN: arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            
    :type KeyId: string
    :param PolicyName: [REQUIRED]
            The name of the key policy.
            This value must be default .
            
    :type PolicyName: string
    :param Policy: [REQUIRED]
            The key policy to attach to the CMK.
            If you do not set BypassPolicyLockoutSafetyCheck to true, the policy must meet the following criteria:
            It must allow the principal making the PutKeyPolicy request to make a subsequent PutKeyPolicy request on the CMK. This reduces the likelihood that the CMK becomes unmanageable. For more information, refer to the scenario in the Default Key Policy section in the AWS Key Management Service Developer Guide .
            The principal(s) specified in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before specifying the new principal in a key policy because the new principal might not immediately be visible to AWS KMS. For more information, see Changes that I make are not always immediately visible in the IAM User Guide .
            The policy size limit is 32 KiB (32768 bytes).
            
    :type Policy: string
    :param BypassPolicyLockoutSafetyCheck: A flag to indicate whether to bypass the key policy lockout safety check.
            Warning
            Setting this value to true increases the likelihood that the CMK becomes unmanageable. Do not set this value to true indiscriminately.
            For more information, refer to the scenario in the Default Key Policy section in the AWS Key Management Service Developer Guide .
            Use this parameter only when you intend to prevent the principal making the request from making a subsequent PutKeyPolicy request on the CMK.
            The default value is false.
            
    :type BypassPolicyLockoutSafetyCheck: boolean
    """
    pass


def re_encrypt(CiphertextBlob=None, SourceEncryptionContext=None, DestinationKeyId=None,
               DestinationEncryptionContext=None, GrantTokens=None):
    """
    :param CiphertextBlob: [REQUIRED]
            Ciphertext of the data to re-encrypt.
            
    :type CiphertextBlob: bytes
    :param SourceEncryptionContext: Encryption context used to encrypt and decrypt the data specified in the CiphertextBlob parameter.
            (string) --
            (string) --
            
    :type SourceEncryptionContext: dict
    :param DestinationKeyId: [REQUIRED]
            A unique identifier for the customer master key used to re-encrypt the data. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by 'alias/'.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Alias ARN Example - arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            Alias Name Example - alias/MyAliasName
            
    :type DestinationKeyId: string
    :param DestinationEncryptionContext: Encryption context to be used when the data is re-encrypted.
            (string) --
            (string) --
            
    :type DestinationEncryptionContext: dict
    :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            
    :type GrantTokens: list
    """
    pass


def retire_grant(GrantToken=None, KeyId=None, GrantId=None):
    """
    :param GrantToken: Token that identifies the grant to be retired.
    :type GrantToken: string
    :param KeyId: A unique identifier for the customer master key associated with the grant. This value can be a globally unique identifier or a fully specified ARN of the key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            
    :type KeyId: string
    :param GrantId: Unique identifier of the grant to be retired. The grant ID is returned by the CreateGrant function.
            Grant ID Example - 0123456789012345678901234567890123456789012345678901234567890123
            
    :type GrantId: string
    """
    pass


def revoke_grant(KeyId=None, GrantId=None):
    """
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key associated with the grant. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            
    :type KeyId: string
    :param GrantId: [REQUIRED]
            Identifier of the grant to be revoked.
            
    :type GrantId: string
    """
    pass


def schedule_key_deletion(KeyId=None, PendingWindowInDays=None):
    """
    :param KeyId: [REQUIRED]
            The unique identifier for the customer master key (CMK) to delete.
            To specify this value, use the unique key ID or the Amazon Resource Name (ARN) of the CMK. Examples:
            Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            Key ARN: arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            To obtain the unique key ID and key ARN for a given CMK, use ListKeys or DescribeKey .
            
    :type KeyId: string
    :param PendingWindowInDays: The waiting period, specified in number of days. After the waiting period ends, AWS KMS deletes the customer master key (CMK).
            This value is optional. If you include a value, it must be between 7 and 30, inclusive. If you do not include a value, it defaults to 30.
            
    :type PendingWindowInDays: integer
    """
    pass


def update_alias(AliasName=None, TargetKeyId=None):
    """
    :param AliasName: [REQUIRED]
            String that contains the name of the alias to be modified. The name must start with the word 'alias' followed by a forward slash (alias/). Aliases that begin with 'alias/aws' are reserved.
            
    :type AliasName: string
    :param TargetKeyId: [REQUIRED]
            Unique identifier of the customer master key to be mapped to the alias. This value can be a globally unique identifier or the fully specified ARN of a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            You can call ListAliases to verify that the alias is mapped to the correct TargetKeyId .
            
    :type TargetKeyId: string
    """
    pass


def update_key_description(KeyId=None, Description=None):
    """
    :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            
    :type KeyId: string
    :param Description: [REQUIRED]
            New description for the key.
            
    :type Description: string
    """
    pass
