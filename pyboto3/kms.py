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

import boto3


class Kms(object):
    def __init__(self):
        self.client = boto3.client('Kms')

    def can_paginate(self, operation_name=None):
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
        self.client.can_paginate(operation_name=operation_name)

    def cancel_key_deletion(self, KeyId=None):
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
        self.client.cancel_key_deletion(KeyId=KeyId)

    def create_alias(self, AliasName=None, TargetKeyId=None):
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
        self.client.create_alias(AliasName=AliasName, TargetKeyId=TargetKeyId)

    def create_grant(self, KeyId=None, GranteePrincipal=None, RetiringPrincipal=None, Operations=None, Constraints=None,
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
        self.client.create_grant(KeyId=KeyId, GranteePrincipal=GranteePrincipal, RetiringPrincipal=RetiringPrincipal,
                                 Operations=Operations, Constraints=Constraints, GrantTokens=GrantTokens, Name=Name)

    def create_key(self, Policy=None, Description=None, KeyUsage=None, BypassPolicyLockoutSafetyCheck=None):
        """
        :param Policy: The key policy to attach to the CMK.
            If you specify a key policy, it must meet the following criteria:
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
        :param BypassPolicyLockoutSafetyCheck: A flag to indicate whether to bypass the key policy lockout safety check.
            Warning
            Setting this value to true increases the likelihood that the CMK becomes unmanageable. Do not set this value to true indiscriminately.
            For more information, refer to the scenario in the Default Key Policy section in the AWS Key Management Service Developer Guide .
            Use this parameter only when you include a policy in the request and you intend to prevent the principal making the request from making a subsequent PutKeyPolicy request on the CMK.
            The default value is false.
            
        :type BypassPolicyLockoutSafetyCheck: boolean
        """
        self.client.create_key(Policy=Policy, Description=Description, KeyUsage=KeyUsage,
                               BypassPolicyLockoutSafetyCheck=BypassPolicyLockoutSafetyCheck)

    def decrypt(self, CiphertextBlob=None, EncryptionContext=None, GrantTokens=None):
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
        self.client.decrypt(CiphertextBlob=CiphertextBlob, EncryptionContext=EncryptionContext, GrantTokens=GrantTokens)

    def delete_alias(self, AliasName=None):
        """
        :param AliasName: [REQUIRED]
            The alias to be deleted. The name must start with the word 'alias' followed by a forward slash (alias/). Aliases that begin with 'alias/AWS' are reserved.
            ReturnsNone
            
        :type AliasName: string
        """
        self.client.delete_alias(AliasName=AliasName)

    def describe_key(self, KeyId=None, GrantTokens=None):
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
        self.client.describe_key(KeyId=KeyId, GrantTokens=GrantTokens)

    def disable_key(self, KeyId=None):
        """
        :param KeyId: [REQUIRED]
            A unique identifier for the CMK.
            Use the CMK's unique identifier or its Amazon Resource Name (ARN). For example:
            Unique ID: 1234abcd-12ab-34cd-56ef-1234567890ab
            ARN: arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
            ReturnsNone
            
        :type KeyId: string
        """
        self.client.disable_key(KeyId=KeyId)

    def disable_key_rotation(self, KeyId=None):
        """
        :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            ReturnsNone
            
        :type KeyId: string
        """
        self.client.disable_key_rotation(KeyId=KeyId)

    def enable_key(self, KeyId=None):
        """
        :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            ReturnsNone
            
        :type KeyId: string
        """
        self.client.enable_key(KeyId=KeyId)

    def enable_key_rotation(self, KeyId=None):
        """
        :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier or the fully specified ARN to a key.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            ReturnsNone
            
        :type KeyId: string
        """
        self.client.enable_key_rotation(KeyId=KeyId)

    def encrypt(self, KeyId=None, Plaintext=None, EncryptionContext=None, GrantTokens=None):
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
        :param EncryptionContext: Name/value pair that specifies the encryption context to be used for authenticated encryption. If used here, the same value must be supplied to the Decrypt API or decryption will fail. For more information, see Encryption Context .
            (string) --
            (string) --
            
        :type EncryptionContext: dict
        :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            
        :type GrantTokens: list
        """
        self.client.encrypt(KeyId=KeyId, Plaintext=Plaintext, EncryptionContext=EncryptionContext,
                            GrantTokens=GrantTokens)

    def generate_data_key(self, KeyId=None, EncryptionContext=None, NumberOfBytes=None, KeySpec=None, GrantTokens=None):
        """
        :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by 'alias/'.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Alias ARN Example - arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            Alias Name Example - alias/MyAliasName
            
        :type KeyId: string
        :param EncryptionContext: Name/value pair that contains additional data to be authenticated during the encryption and decryption processes that use the key. This value is logged by AWS CloudTrail to provide context around the data encrypted by the key.
            (string) --
            (string) --
            
        :type EncryptionContext: dict
        :param NumberOfBytes: Integer that contains the number of bytes to generate. Common values are 128, 256, 512, and 1024. 1024 is the current limit. We recommend that you use the KeySpec parameter instead.
        :type NumberOfBytes: integer
        :param KeySpec: Value that identifies the encryption algorithm and key size to generate a data key for. Currently this can be AES_128 or AES_256.
        :type KeySpec: string
        :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            
        :type GrantTokens: list
        """
        self.client.generate_data_key(KeyId=KeyId, EncryptionContext=EncryptionContext, NumberOfBytes=NumberOfBytes,
                                      KeySpec=KeySpec, GrantTokens=GrantTokens)

    def generate_data_key_without_plaintext(self, KeyId=None, EncryptionContext=None, KeySpec=None, NumberOfBytes=None,
                                            GrantTokens=None):
        """
        :param KeyId: [REQUIRED]
            A unique identifier for the customer master key. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by 'alias/'.
            Key ARN Example - arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            Alias ARN Example - arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
            Globally Unique Key ID Example - 12345678-1234-1234-1234-123456789012
            Alias Name Example - alias/MyAliasName
            
        :type KeyId: string
        :param EncryptionContext: Name:value pair that contains additional data to be authenticated during the encryption and decryption processes.
            (string) --
            (string) --
            
        :type EncryptionContext: dict
        :param KeySpec: Value that identifies the encryption algorithm and key size. Currently this can be AES_128 or AES_256.
        :type KeySpec: string
        :param NumberOfBytes: Integer that contains the number of bytes to generate. Common values are 128, 256, 512, 1024 and so on. We recommend that you use the KeySpec parameter instead.
        :type NumberOfBytes: integer
        :param GrantTokens: A list of grant tokens.
            For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
            (string) --
            
        :type GrantTokens: list
        """
        self.client.generate_data_key_without_plaintext(KeyId=KeyId, EncryptionContext=EncryptionContext,
                                                        KeySpec=KeySpec, NumberOfBytes=NumberOfBytes,
                                                        GrantTokens=GrantTokens)

    def generate_presigned_url(self, ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
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
        self.client.generate_presigned_url(ClientMethod=ClientMethod, Params=Params, ExpiresIn=ExpiresIn,
                                           HttpMethod=HttpMethod)

    def generate_random(self, NumberOfBytes=None):
        """
        :param NumberOfBytes: Integer that contains the number of bytes to generate. Common values are 128, 256, 512, 1024 and so on. The current limit is 1024 bytes.
            Return typedict
            ReturnsResponse Syntax{
              'Plaintext': b'bytes'
            }
            Response Structure
            (dict) --
            Plaintext (bytes) --Plaintext that contains the unpredictable byte string.
            
            
        :type NumberOfBytes: integer
        """
        self.client.generate_random(NumberOfBytes=NumberOfBytes)

    def get_key_policy(self, KeyId=None, PolicyName=None):
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
        self.client.get_key_policy(KeyId=KeyId, PolicyName=PolicyName)

    def get_key_rotation_status(self, KeyId=None):
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
        self.client.get_key_rotation_status(KeyId=KeyId)

    def get_paginator(self, operation_name=None):
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
        self.client.get_paginator(operation_name=operation_name)

    def get_waiter(self):
        """
        """
        self.client.get_waiter()

    def list_aliases(self, Limit=None, Marker=None):
        """
        :param Limit: When paginating results, specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the Truncated element in the response is set to true.
            This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.
            
        :type Limit: integer
        :param Marker: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the response you just received.
        :type Marker: string
        """
        self.client.list_aliases(Limit=Limit, Marker=Marker)

    def list_grants(self, Limit=None, Marker=None, KeyId=None):
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
        self.client.list_grants(Limit=Limit, Marker=Marker, KeyId=KeyId)

    def list_key_policies(self, KeyId=None, Limit=None, Marker=None):
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
        self.client.list_key_policies(KeyId=KeyId, Limit=Limit, Marker=Marker)

    def list_keys(self, Limit=None, Marker=None):
        """
        :param Limit: When paginating results, specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the Truncated element in the response is set to true.
            This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.
            
        :type Limit: integer
        :param Marker: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the response you just received.
        :type Marker: string
        """
        self.client.list_keys(Limit=Limit, Marker=Marker)

    def list_retirable_grants(self, Limit=None, Marker=None, RetiringPrincipal=None):
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
        self.client.list_retirable_grants(Limit=Limit, Marker=Marker, RetiringPrincipal=RetiringPrincipal)

    def put_key_policy(self, KeyId=None, PolicyName=None, Policy=None, BypassPolicyLockoutSafetyCheck=None):
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
            The key policy must meet the following criteria:
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
        self.client.put_key_policy(KeyId=KeyId, PolicyName=PolicyName, Policy=Policy,
                                   BypassPolicyLockoutSafetyCheck=BypassPolicyLockoutSafetyCheck)

    def re_encrypt(self, CiphertextBlob=None, SourceEncryptionContext=None, DestinationKeyId=None,
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
        self.client.re_encrypt(CiphertextBlob=CiphertextBlob, SourceEncryptionContext=SourceEncryptionContext,
                               DestinationKeyId=DestinationKeyId,
                               DestinationEncryptionContext=DestinationEncryptionContext, GrantTokens=GrantTokens)

    def retire_grant(self, GrantToken=None, KeyId=None, GrantId=None):
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
        self.client.retire_grant(GrantToken=GrantToken, KeyId=KeyId, GrantId=GrantId)

    def revoke_grant(self, KeyId=None, GrantId=None):
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
        self.client.revoke_grant(KeyId=KeyId, GrantId=GrantId)

    def schedule_key_deletion(self, KeyId=None, PendingWindowInDays=None):
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
        self.client.schedule_key_deletion(KeyId=KeyId, PendingWindowInDays=PendingWindowInDays)

    def update_alias(self, AliasName=None, TargetKeyId=None):
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
        self.client.update_alias(AliasName=AliasName, TargetKeyId=TargetKeyId)

    def update_key_description(self, KeyId=None, Description=None):
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
        self.client.update_key_description(KeyId=KeyId, Description=Description)
