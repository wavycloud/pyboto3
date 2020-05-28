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

def cancel_key_deletion(KeyId=None):
    """
    Cancels the deletion of a customer master key (CMK). When this operation succeeds, the key state of the CMK is Disabled . To enable the CMK, use  EnableKey . You cannot perform this operation on a CMK in a different AWS account.
    For more information about scheduling and canceling deletion of a CMK, see Deleting Customer Master Keys in the AWS Key Management Service Developer Guide .
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example cancels deletion of the specified CMK.
    Expected Output:
    
    :example: response = client.cancel_key_deletion(
        KeyId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nThe unique identifier for the customer master key (CMK) for which to cancel deletion.\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :rtype: dict
ReturnsResponse Syntax{
    'KeyId': 'string'
}


Response Structure

(dict) --
KeyId (string) --The unique identifier of the master key for which deletion is canceled.






Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException

Examples
The following example cancels deletion of the specified CMK.
response = client.cancel_key_deletion(
    # The identifier of the CMK whose deletion you are canceling. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
    KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
)

print(response)


Expected Output:
{
    # The ARN of the CMK whose deletion you canceled.
    'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'KeyId': 'string'
    }
    
    
    :returns: 
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.KMSInvalidStateException
    
    """
    pass

def connect_custom_key_store(CustomKeyStoreId=None):
    """
    Connects or reconnects a custom key store to its associated AWS CloudHSM cluster.
    The custom key store must be connected before you can create customer master keys (CMKs) in the key store or use the CMKs it contains. You can disconnect and reconnect a custom key store at any time.
    To connect a custom key store, its associated AWS CloudHSM cluster must have at least one active HSM. To get the number of active HSMs in a cluster, use the DescribeClusters operation. To add HSMs to the cluster, use the CreateHsm operation. Also, the ` kmsuser crypto user <https://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser>`__ (CU) must not be logged into the cluster. This prevents AWS KMS from using this account to log in.
    The connection process can take an extended amount of time to complete; up to 20 minutes. This operation starts the connection process, but it does not wait for it to complete. When it succeeds, this operation quickly returns an HTTP 200 response and a JSON object with no properties. However, this response does not indicate that the custom key store is connected. To get the connection state of the custom key store, use the  DescribeCustomKeyStores operation.
    During the connection process, AWS KMS finds the AWS CloudHSM cluster that is associated with the custom key store, creates the connection infrastructure, connects to the cluster, logs into the AWS CloudHSM client as the kmsuser CU, and rotates its password.
    The ConnectCustomKeyStore operation might fail for various reasons. To find the reason, use the  DescribeCustomKeyStores operation and see the ConnectionErrorCode in the response. For help interpreting the ConnectionErrorCode , see  CustomKeyStoresListEntry .
    To fix the failure, use the  DisconnectCustomKeyStore operation to disconnect the custom key store, correct the error, use the  UpdateCustomKeyStore operation if necessary, and then use ConnectCustomKeyStore again.
    If you are having trouble connecting or disconnecting a custom key store, see Troubleshooting a Custom Key Store in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.connect_custom_key_store(
        CustomKeyStoreId='string'
    )
    
    
    :type CustomKeyStoreId: string
    :param CustomKeyStoreId: [REQUIRED]\nEnter the key store ID of the custom key store that you want to connect. To find the ID of a custom key store, use the DescribeCustomKeyStores operation.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

KMS.Client.exceptions.CloudHsmClusterNotActiveException
KMS.Client.exceptions.CustomKeyStoreInvalidStateException
KMS.Client.exceptions.CustomKeyStoreNotFoundException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.CloudHsmClusterInvalidConfigurationException


    :return: {}
    
    
    :returns: 
    KMS.Client.exceptions.CloudHsmClusterNotActiveException
    KMS.Client.exceptions.CustomKeyStoreInvalidStateException
    KMS.Client.exceptions.CustomKeyStoreNotFoundException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.CloudHsmClusterInvalidConfigurationException
    
    """
    pass

def create_alias(AliasName=None, TargetKeyId=None):
    """
    Creates a display name for a customer managed customer master key (CMK). You can use an alias to identify a CMK in cryptographic operations, such as  Encrypt and  GenerateDataKey . You can change the CMK associated with the alias at any time.
    Aliases are easier to remember than key IDs. They can also help to simplify your applications. For example, if you use an alias in your code, you can change the CMK your code uses by associating a given alias with a different CMK.
    To run the same code in multiple AWS regions, use an alias in your code, such as alias/ApplicationKey . Then, in each AWS Region, create an alias/ApplicationKey alias that is associated with a CMK in that Region. When you run your code, it uses the alias/ApplicationKey CMK for that AWS Region without any Region-specific code.
    This operation does not return a response. To get the alias that you created, use the  ListAliases operation.
    To use aliases successfully, be aware of the following information.
    Because an alias is not a property of a CMK, you can delete and change the aliases of a CMK without affecting the CMK. Also, aliases do not appear in the response from the  DescribeKey operation. To get the aliases and alias ARNs of CMKs in each AWS account and Region, use the  ListAliases operation.
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates an alias for the specified customer master key (CMK).
    Expected Output:
    
    :example: response = client.create_alias(
        AliasName='string',
        TargetKeyId='string'
    )
    
    
    :type AliasName: string
    :param AliasName: [REQUIRED]\nSpecifies the alias name. This value must begin with alias/ followed by a name, such as alias/ExampleAlias . The alias name cannot begin with alias/aws/ . The alias/aws/ prefix is reserved for AWS managed CMKs.\n

    :type TargetKeyId: string
    :param TargetKeyId: [REQUIRED]\nIdentifies the CMK to which the alias refers. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. You cannot specify another alias. For help finding the key ID and ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide .\n

    :return: response = client.create_alias(
        # The alias to create. Aliases must begin with 'alias/'. Do not use aliases that begin with 'alias/aws' because they are reserved for use by AWS.
        AliasName='alias/ExampleAlias',
        # The identifier of the CMK whose alias you are creating. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
        TargetKeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
    )
    
    print(response)
    
    
    :returns: 
    AliasName (string) -- [REQUIRED]
    Specifies the alias name. This value must begin with alias/ followed by a name, such as alias/ExampleAlias . The alias name cannot begin with alias/aws/ . The alias/aws/ prefix is reserved for AWS managed CMKs.
    
    TargetKeyId (string) -- [REQUIRED]
    Identifies the CMK to which the alias refers. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. You cannot specify another alias. For help finding the key ID and ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide .
    
    
    """
    pass

def create_custom_key_store(CustomKeyStoreName=None, CloudHsmClusterId=None, TrustAnchorCertificate=None, KeyStorePassword=None):
    """
    Creates a custom key store that is associated with an AWS CloudHSM cluster that you own and manage.
    This operation is part of the Custom Key Store feature feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a single-tenant key store.
    Before you create the custom key store, you must assemble the required elements, including an AWS CloudHSM cluster that fulfills the requirements for a custom key store. For details about the required elements, see Assemble the Prerequisites in the AWS Key Management Service Developer Guide .
    When the operation completes successfully, it returns the ID of the new custom key store. Before you can use your new custom key store, you need to use the  ConnectCustomKeyStore operation to connect the new key store to its AWS CloudHSM cluster. Even if you are not going to use your custom key store immediately, you might want to connect it to verify that all settings are correct and then disconnect it until you are ready to use it.
    For help with failures, see Troubleshooting a Custom Key Store in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_custom_key_store(
        CustomKeyStoreName='string',
        CloudHsmClusterId='string',
        TrustAnchorCertificate='string',
        KeyStorePassword='string'
    )
    
    
    :type CustomKeyStoreName: string
    :param CustomKeyStoreName: [REQUIRED]\nSpecifies a friendly name for the custom key store. The name must be unique in your AWS account.\n

    :type CloudHsmClusterId: string
    :param CloudHsmClusterId: [REQUIRED]\nIdentifies the AWS CloudHSM cluster for the custom key store. Enter the cluster ID of any active AWS CloudHSM cluster that is not already associated with a custom key store. To find the cluster ID, use the DescribeClusters operation.\n

    :type TrustAnchorCertificate: string
    :param TrustAnchorCertificate: [REQUIRED]\nEnter the content of the trust anchor certificate for the cluster. This is the content of the customerCA.crt file that you created when you initialized the cluster .\n

    :type KeyStorePassword: string
    :param KeyStorePassword: [REQUIRED]\nEnter the password of the ` kmsuser crypto user (CU) account <https://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser>`__ in the specified AWS CloudHSM cluster. AWS KMS logs into the cluster as this user to manage key material on your behalf.\nThe password must be a string of 7 to 32 characters. Its value is case sensitive.\nThis parameter tells AWS KMS the kmsuser account password; it does not change the password in the AWS CloudHSM cluster.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CustomKeyStoreId': 'string'
}


Response Structure

(dict) --

CustomKeyStoreId (string) --
A unique identifier for the new custom key store.







Exceptions

KMS.Client.exceptions.CloudHsmClusterInUseException
KMS.Client.exceptions.CustomKeyStoreNameInUseException
KMS.Client.exceptions.CloudHsmClusterNotFoundException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.CloudHsmClusterNotActiveException
KMS.Client.exceptions.IncorrectTrustAnchorException
KMS.Client.exceptions.CloudHsmClusterInvalidConfigurationException


    :return: {
        'CustomKeyStoreId': 'string'
    }
    
    
    :returns: 
    KMS.Client.exceptions.CloudHsmClusterInUseException
    KMS.Client.exceptions.CustomKeyStoreNameInUseException
    KMS.Client.exceptions.CloudHsmClusterNotFoundException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.CloudHsmClusterNotActiveException
    KMS.Client.exceptions.IncorrectTrustAnchorException
    KMS.Client.exceptions.CloudHsmClusterInvalidConfigurationException
    
    """
    pass

def create_grant(KeyId=None, GranteePrincipal=None, RetiringPrincipal=None, Operations=None, Constraints=None, GrantTokens=None, Name=None):
    """
    Adds a grant to a customer master key (CMK). The grant allows the grantee principal to use the CMK when the conditions specified in the grant are met. When setting permissions, grants are an alternative to key policies.
    To create a grant that allows a cryptographic operation only when the request includes a particular encryption context , use the Constraints parameter. For details, see  GrantConstraints .
    You can create grants on symmetric and asymmetric CMKs. However, if the grant allows an operation that the CMK does not support, CreateGrant fails with a ValidationException .
    For information about symmetric and asymmetric CMKs, see Using Symmetric and Asymmetric CMKs in the AWS Key Management Service Developer Guide .
    To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the KeyId parameter. For more information about grants, see Grants in the * AWS Key Management Service Developer Guide * .
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a grant that allows the specified IAM role to encrypt data with the specified customer master key (CMK).
    Expected Output:
    
    :example: response = client.create_grant(
        KeyId='string',
        GranteePrincipal='string',
        RetiringPrincipal='string',
        Operations=[
            'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'Sign'|'Verify'|'GetPublicKey'|'CreateGrant'|'RetireGrant'|'DescribeKey'|'GenerateDataKeyPair'|'GenerateDataKeyPairWithoutPlaintext',
        ],
        Constraints={
            'EncryptionContextSubset': {
                'string': 'string'
            },
            'EncryptionContextEquals': {
                'string': 'string'
            }
        },
        GrantTokens=[
            'string',
        ],
        Name='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nThe unique identifier for the customer master key (CMK) that the grant applies to.\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :type GranteePrincipal: string
    :param GranteePrincipal: [REQUIRED]\nThe principal that is given permission to perform the operations that the grant permits.\nTo specify the principal, use the Amazon Resource Name (ARN) of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, IAM roles, federated users, and assumed role users. For examples of the ARN syntax to use for specifying a principal, see AWS Identity and Access Management (IAM) in the Example ARNs section of the AWS General Reference .\n

    :type RetiringPrincipal: string
    :param RetiringPrincipal: The principal that is given permission to retire the grant by using RetireGrant operation.\nTo specify the principal, use the Amazon Resource Name (ARN) of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, federated users, and assumed role users. For examples of the ARN syntax to use for specifying a principal, see AWS Identity and Access Management (IAM) in the Example ARNs section of the AWS General Reference .\n

    :type Operations: list
    :param Operations: [REQUIRED]\nA list of operations that the grant permits.\n\n(string) --\n\n

    :type Constraints: dict
    :param Constraints: Allows a cryptographic operation only when the encryption context matches or includes the encryption context specified in this structure. For more information about encryption context, see Encryption Context in the * AWS Key Management Service Developer Guide * .\n\nEncryptionContextSubset (dict) --A list of key-value pairs that must be included in the encryption context of the cryptographic operation request. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs.\n\n(string) --\n(string) --\n\n\n\n\nEncryptionContextEquals (dict) --A list of key-value pairs that must match the encryption context in the cryptographic operation request. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint.\n\n(string) --\n(string) --\n\n\n\n\n\n

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.\nFor more information, see Grant Tokens in the AWS Key Management Service Developer Guide .\n\n(string) --\n\n

    :type Name: string
    :param Name: A friendly name for identifying the grant. Use this value to prevent the unintended creation of duplicate grants when retrying this request.\nWhen this value is absent, all CreateGrant requests result in a new grant with a unique GrantId even if all the supplied parameters are identical. This can result in unintended duplicates when you retry the CreateGrant request.\nWhen this value is present, you can retry a CreateGrant request with identical parameters; if the grant already exists, the original GrantId is returned without creating a new grant. Note that the returned grant token is unique with every CreateGrant request, even when a duplicate GrantId is returned. All grant tokens obtained in this way can be used interchangeably.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GrantToken': 'string',
    'GrantId': 'string'
}


Response Structure

(dict) --

GrantToken (string) --
The grant token.
For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .

GrantId (string) --
The unique identifier for the grant.
You can use the GrantId in a subsequent  RetireGrant or  RevokeGrant operation.







Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.DisabledException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.InvalidGrantTokenException
KMS.Client.exceptions.LimitExceededException
KMS.Client.exceptions.KMSInvalidStateException

Examples
The following example creates a grant that allows the specified IAM role to encrypt data with the specified customer master key (CMK).
response = client.create_grant(
    # The identity that is given permission to perform the operations specified in the grant.
    GranteePrincipal='arn:aws:iam::111122223333:role/ExampleRole',
    # The identifier of the CMK to which the grant applies. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
    KeyId='arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab',
    # A list of operations that the grant allows.
    Operations=[
        'Encrypt',
        'Decrypt',
    ],
)

print(response)


Expected Output:
{
    # The unique identifier of the grant.
    'GrantId': '0c237476b39f8bc44e45212e08498fbe3151305030726c0590dd8d3e9f3d6a60',
    # The grant token.
    'GrantToken': 'AQpAM2RhZTk1MGMyNTk2ZmZmMzEyYWVhOWViN2I1MWM4Mzc0MWFiYjc0ZDE1ODkyNGFlNTIzODZhMzgyZjBlNGY3NiKIAgEBAgB4Pa6VDCWW__MSrqnre1HIN0Grt00ViSSuUjhqOC8OT3YAAADfMIHcBgkqhkiG9w0BBwaggc4wgcsCAQAwgcUGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMmqLyBTAegIn9XlK5AgEQgIGXZQjkBcl1dykDdqZBUQ6L1OfUivQy7JVYO2-ZJP7m6f1g8GzV47HX5phdtONAP7K_HQIflcgpkoCqd_fUnE114mSmiagWkbQ5sqAVV3ov-VeqgrvMe5ZFEWLMSluvBAqdjHEdMIkHMlhlj4ENZbzBfo9Wxk8b8SnwP4kc4gGivedzFXo-dwN8fxjjq_ZZ9JFOj2ijIbj5FyogDCN0drOfi8RORSEuCEmPvjFRMFAwcmwFkN2NPp89amA',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GrantToken': 'string',
        'GrantId': 'string'
    }
    
    
    :returns: 
    KeyId (string) -- [REQUIRED]
    The unique identifier for the customer master key (CMK) that the grant applies to.
    Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
    For example:
    
    Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
    Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
    
    To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
    
    GranteePrincipal (string) -- [REQUIRED]
    The principal that is given permission to perform the operations that the grant permits.
    To specify the principal, use the Amazon Resource Name (ARN) of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, IAM roles, federated users, and assumed role users. For examples of the ARN syntax to use for specifying a principal, see AWS Identity and Access Management (IAM) in the Example ARNs section of the AWS General Reference .
    
    RetiringPrincipal (string) -- The principal that is given permission to retire the grant by using  RetireGrant operation.
    To specify the principal, use the Amazon Resource Name (ARN) of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, federated users, and assumed role users. For examples of the ARN syntax to use for specifying a principal, see AWS Identity and Access Management (IAM) in the Example ARNs section of the AWS General Reference .
    
    Operations (list) -- [REQUIRED]
    A list of operations that the grant permits.
    
    (string) --
    
    
    Constraints (dict) -- Allows a cryptographic operation only when the encryption context matches or includes the encryption context specified in this structure. For more information about encryption context, see Encryption Context in the * AWS Key Management Service Developer Guide * .
    
    EncryptionContextSubset (dict) --A list of key-value pairs that must be included in the encryption context of the cryptographic operation request. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs.
    
    (string) --
    (string) --
    
    
    
    
    EncryptionContextEquals (dict) --A list of key-value pairs that must match the encryption context in the cryptographic operation request. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint.
    
    (string) --
    (string) --
    
    
    
    
    
    
    GrantTokens (list) -- A list of grant tokens.
    For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
    
    (string) --
    
    
    Name (string) -- A friendly name for identifying the grant. Use this value to prevent the unintended creation of duplicate grants when retrying this request.
    When this value is absent, all CreateGrant requests result in a new grant with a unique GrantId even if all the supplied parameters are identical. This can result in unintended duplicates when you retry the CreateGrant request.
    When this value is present, you can retry a CreateGrant request with identical parameters; if the grant already exists, the original GrantId is returned without creating a new grant. Note that the returned grant token is unique with every CreateGrant request, even when a duplicate GrantId is returned. All grant tokens obtained in this way can be used interchangeably.
    
    
    """
    pass

def create_key(Policy=None, Description=None, KeyUsage=None, CustomerMasterKeySpec=None, Origin=None, CustomKeyStoreId=None, BypassPolicyLockoutSafetyCheck=None, Tags=None):
    """
    Creates a unique customer managed customer master key (CMK) in your AWS account and Region. You cannot use this operation to create a CMK in a different AWS account.
    You can use the CreateKey operation to create symmetric or asymmetric CMKs.
    For information about symmetric and asymmetric CMKs, see Using Symmetric and Asymmetric CMKs in the AWS Key Management Service Developer Guide .
    To create different types of CMKs, use the following guidance:
    To create an asymmetric CMK, use the CustomerMasterKeySpec parameter to specify the type of key material in the CMK. Then, use the Key parameter to determine whether the CMK will be used to encrypt and decrypt or sign and verify. You can\'t change these properties after the CMK is created.
    When creating a symmetric CMK, you don\'t need to specify the CustomerMasterKeySpec or Key parameters. The default value for CustomerMasterKeySpec , SYMMETRIC_DEFAULT , and the default value for KeyUsage , ENCRYPT_DECRYPT , are the only valid values for symmetric CMKs.
    To import your own key material, begin by creating a symmetric CMK with no key material. To do this, use the Origin parameter of CreateKey with a value of EXTERNAL . Next, use  GetParametersForImport operation to get a public key and import token, and use the public key to encrypt your key material. Then, use  ImportKeyMaterial with your import token to import the key material. For step-by-step instructions, see Importing Key Material in the * AWS Key Management Service Developer Guide * . You cannot import the key material into an asymmetric CMK.
    To create a symmetric CMK in a custom key store , use the CustomKeyStoreId parameter to specify the custom key store. You must also use the Origin parameter with a value of AWS_CLOUDHSM . The AWS CloudHSM cluster that is associated with the custom key store must have at least two active HSMs in different Availability Zones in the AWS Region.
    You cannot create an asymmetric CMK in a custom key store. For information about custom key stores in AWS KMS see Using Custom Key Stores in the * AWS Key Management Service Developer Guide * .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a CMK.
    Expected Output:
    
    :example: response = client.create_key(
        Policy='string',
        Description='string',
        KeyUsage='SIGN_VERIFY'|'ENCRYPT_DECRYPT',
        CustomerMasterKeySpec='RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'|'ECC_SECG_P256K1'|'SYMMETRIC_DEFAULT',
        Origin='AWS_KMS'|'EXTERNAL'|'AWS_CLOUDHSM',
        CustomKeyStoreId='string',
        BypassPolicyLockoutSafetyCheck=True|False,
        Tags=[
            {
                'TagKey': 'string',
                'TagValue': 'string'
            },
        ]
    )
    
    
    :type Policy: string
    :param Policy: The key policy to attach to the CMK.\nIf you provide a key policy, it must meet the following criteria:\n\nIf you don\'t set BypassPolicyLockoutSafetyCheck to true, the key policy must allow the principal that is making the CreateKey request to make a subsequent PutKeyPolicy request on the CMK. This reduces the risk that the CMK becomes unmanageable. For more information, refer to the scenario in the Default Key Policy section of the * AWS Key Management Service Developer Guide * .\nEach statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to AWS KMS. For more information, see Changes that I make are not always immediately visible in the AWS Identity and Access Management User Guide .\n\nIf you do not provide a key policy, AWS KMS attaches a default key policy to the CMK. For more information, see Default Key Policy in the AWS Key Management Service Developer Guide .\nThe key policy size quota is 32 kilobytes (32768 bytes).\n

    :type Description: string
    :param Description: A description of the CMK.\nUse a description that helps you decide whether the CMK is appropriate for a task.\n

    :type KeyUsage: string
    :param KeyUsage: Determines the cryptographic operations for which you can use the CMK. The default value is ENCRYPT_DECRYPT . This parameter is required only for asymmetric CMKs. You can\'t change the KeyUsage value after the CMK is created.\nSelect only one valid value.\n\nFor symmetric CMKs, omit the parameter or specify ENCRYPT_DECRYPT .\nFor asymmetric CMKs with RSA key material, specify ENCRYPT_DECRYPT or SIGN_VERIFY .\nFor asymmetric CMKs with ECC key material, specify SIGN_VERIFY .\n\n

    :type CustomerMasterKeySpec: string
    :param CustomerMasterKeySpec: Specifies the type of CMK to create. The default value, SYMMETRIC_DEFAULT , creates a CMK with a 256-bit symmetric key for encryption and decryption. For help choosing a key spec for your CMK, see How to Choose Your CMK Configuration in the AWS Key Management Service Developer Guide .\nThe CustomerMasterKeySpec determines whether the CMK contains a symmetric key or an asymmetric key pair. It also determines the encryption algorithms or signing algorithms that the CMK supports. You can\'t change the CustomerMasterKeySpec after the CMK is created. To further restrict the algorithms that can be used with the CMK, use a condition key in its key policy or IAM policy. For more information, see kms:EncryptionAlgorithm or kms:Signing Algorithm in the AWS Key Management Service Developer Guide .\n\nWarning\nAWS services that are integrated with AWS KMS use symmetric CMKs to protect your data. These services do not support asymmetric CMKs. For help determining whether a CMK is symmetric or asymmetric, see Identifying Symmetric and Asymmetric CMKs in the AWS Key Management Service Developer Guide .\n\nAWS KMS supports the following key specs for CMKs:\n\nSymmetric key (default)\nSYMMETRIC_DEFAULT (AES-256-GCM)\n\n\nAsymmetric RSA key pairs\nRSA_2048\nRSA_3072\nRSA_4096\n\n\nAsymmetric NIST-recommended elliptic curve key pairs\nECC_NIST_P256 (secp256r1)\nECC_NIST_P384 (secp384r1)\nECC_NIST_P521 (secp521r1)\n\n\nOther asymmetric elliptic curve key pairs\nECC_SECG_P256K1 (secp256k1), commonly used for cryptocurrencies.\n\n\n\n

    :type Origin: string
    :param Origin: The source of the key material for the CMK. You cannot change the origin after you create the CMK. The default is AWS_KMS , which means AWS KMS creates the key material.\nWhen the parameter value is EXTERNAL , AWS KMS creates a CMK without key material so that you can import key material from your existing key management infrastructure. For more information about importing key material into AWS KMS, see Importing Key Material in the AWS Key Management Service Developer Guide . This value is valid only for symmetric CMKs.\nWhen the parameter value is AWS_CLOUDHSM , AWS KMS creates the CMK in an AWS KMS custom key store and creates its key material in the associated AWS CloudHSM cluster. You must also use the CustomKeyStoreId parameter to identify the custom key store. This value is valid only for symmetric CMKs.\n

    :type CustomKeyStoreId: string
    :param CustomKeyStoreId: Creates the CMK in the specified custom key store and the key material in its associated AWS CloudHSM cluster. To create a CMK in a custom key store, you must also specify the Origin parameter with a value of AWS_CLOUDHSM . The AWS CloudHSM cluster that is associated with the custom key store must have at least two active HSMs, each in a different Availability Zone in the Region.\nThis parameter is valid only for symmetric CMKs. You cannot create an asymmetric CMK in a custom key store.\nTo find the ID of a custom key store, use the DescribeCustomKeyStores operation.\nThe response includes the custom key store ID and the ID of the AWS CloudHSM cluster.\nThis operation is part of the Custom Key Store feature feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a single-tenant key store.\n

    :type BypassPolicyLockoutSafetyCheck: boolean
    :param BypassPolicyLockoutSafetyCheck: A flag to indicate whether to bypass the key policy lockout safety check.\n\nWarning\nSetting this value to true increases the risk that the CMK becomes unmanageable. Do not set this value to true indiscriminately.\nFor more information, refer to the scenario in the Default Key Policy section in the * AWS Key Management Service Developer Guide * .\n\nUse this parameter only when you include a policy in the request and you intend to prevent the principal that is making the request from making a subsequent PutKeyPolicy request on the CMK.\nThe default value is false.\n

    :type Tags: list
    :param Tags: One or more tags. Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string.\nWhen you add tags to an AWS resource, AWS generates a cost allocation report with usage and costs aggregated by tags. For information about adding, changing, deleting and listing tags for CMKs, see Tagging Keys .\nUse this parameter to tag the CMK when it is created. To add tags to an existing CMK, use the TagResource operation.\n\n(dict) --A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.\nFor information about the rules that apply to tag keys and tag values, see User-Defined Tag Restrictions in the AWS Billing and Cost Management User Guide .\n\nTagKey (string) -- [REQUIRED]The key of the tag.\n\nTagValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'KeyMetadata': {
        'AWSAccountId': 'string',
        'KeyId': 'string',
        'Arn': 'string',
        'CreationDate': datetime(2015, 1, 1),
        'Enabled': True|False,
        'Description': 'string',
        'KeyUsage': 'SIGN_VERIFY'|'ENCRYPT_DECRYPT',
        'KeyState': 'Enabled'|'Disabled'|'PendingDeletion'|'PendingImport'|'Unavailable',
        'DeletionDate': datetime(2015, 1, 1),
        'ValidTo': datetime(2015, 1, 1),
        'Origin': 'AWS_KMS'|'EXTERNAL'|'AWS_CLOUDHSM',
        'CustomKeyStoreId': 'string',
        'CloudHsmClusterId': 'string',
        'ExpirationModel': 'KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE',
        'KeyManager': 'AWS'|'CUSTOMER',
        'CustomerMasterKeySpec': 'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'|'ECC_SECG_P256K1'|'SYMMETRIC_DEFAULT',
        'EncryptionAlgorithms': [
            'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
        ],
        'SigningAlgorithms': [
            'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'|'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'|'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512',
        ]
    }
}


Response Structure

(dict) --

KeyMetadata (dict) --
Metadata associated with the CMK.

AWSAccountId (string) --
The twelve-digit account ID of the AWS account that owns the CMK.

KeyId (string) --
The globally unique identifier for the CMK.

Arn (string) --
The Amazon Resource Name (ARN) of the CMK. For examples, see AWS Key Management Service (AWS KMS) in the Example ARNs section of the AWS General Reference .

CreationDate (datetime) --
The date and time when the CMK was created.

Enabled (boolean) --
Specifies whether the CMK is enabled. When KeyState is Enabled this value is true, otherwise it is false.

Description (string) --
The description of the CMK.

KeyUsage (string) --
The cryptographic operations for which you can use the CMK.

KeyState (string) --
The state of the CMK.
For more information about how key state affects the use of a CMK, see How Key State Affects the Use of a Customer Master Key in the AWS Key Management Service Developer Guide .

DeletionDate (datetime) --
The date and time after which AWS KMS deletes the CMK. This value is present only when KeyState is PendingDeletion .

ValidTo (datetime) --
The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. This value is present only for CMKs whose Origin is EXTERNAL and whose ExpirationModel is KEY_MATERIAL_EXPIRES , otherwise this value is omitted.

Origin (string) --
The source of the CMK\'s key material. When this value is AWS_KMS , AWS KMS created the key material. When this value is EXTERNAL , the key material was imported from your existing key management infrastructure or the CMK lacks key material. When this value is AWS_CLOUDHSM , the key material was created in the AWS CloudHSM cluster associated with a custom key store.

CustomKeyStoreId (string) --
A unique identifier for the custom key store that contains the CMK. This value is present only when the CMK is created in a custom key store.

CloudHsmClusterId (string) --
The cluster ID of the AWS CloudHSM cluster that contains the key material for the CMK. When you create a CMK in a custom key store , AWS KMS creates the key material for the CMK in the associated AWS CloudHSM cluster. This value is present only when the CMK is created in a custom key store.

ExpirationModel (string) --
Specifies whether the CMK\'s key material expires. This value is present only when Origin is EXTERNAL , otherwise this value is omitted.

KeyManager (string) --
The manager of the CMK. CMKs in your AWS account are either customer managed or AWS managed. For more information about the difference, see Customer Master Keys in the AWS Key Management Service Developer Guide .

CustomerMasterKeySpec (string) --
Describes the type of key material in the CMK.

EncryptionAlgorithms (list) --
A list of encryption algorithms that the CMK supports. You cannot use the CMK with other encryption algorithms within AWS KMS.
This field appears only when the KeyUsage of the CMK is ENCRYPT_DECRYPT .

(string) --


SigningAlgorithms (list) --
A list of signing algorithms that the CMK supports. You cannot use the CMK with other signing algorithms within AWS KMS.
This field appears only when the KeyUsage of the CMK is SIGN_VERIFY .

(string) --










Exceptions

KMS.Client.exceptions.MalformedPolicyDocumentException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.UnsupportedOperationException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.LimitExceededException
KMS.Client.exceptions.TagException
KMS.Client.exceptions.CustomKeyStoreNotFoundException
KMS.Client.exceptions.CustomKeyStoreInvalidStateException
KMS.Client.exceptions.CloudHsmClusterInvalidConfigurationException

Examples
The following example creates a CMK.
response = client.create_key(
    # One or more tags. Each tag consists of a tag key and a tag value.
    Tags=[
        {
            'TagKey': 'CreatedBy',
            'TagValue': 'ExampleUser',
        },
    ],
)

print(response)


Expected Output:
{
    # An object that contains information about the CMK created by this operation.
    'KeyMetadata': {
        'AWSAccountId': '111122223333',
        'Arn': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
        'CreationDate': datetime(2017, 7, 5, 14, 4, 55, 2, 186, 0),
        'Description': '',
        'Enabled': True,
        'KeyId': '1234abcd-12ab-34cd-56ef-1234567890ab',
        'KeyManager': 'CUSTOMER',
        'KeyState': 'Enabled',
        'KeyUsage': 'ENCRYPT_DECRYPT',
        'Origin': 'AWS_KMS',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'KeyMetadata': {
            'AWSAccountId': 'string',
            'KeyId': 'string',
            'Arn': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'Enabled': True|False,
            'Description': 'string',
            'KeyUsage': 'SIGN_VERIFY'|'ENCRYPT_DECRYPT',
            'KeyState': 'Enabled'|'Disabled'|'PendingDeletion'|'PendingImport'|'Unavailable',
            'DeletionDate': datetime(2015, 1, 1),
            'ValidTo': datetime(2015, 1, 1),
            'Origin': 'AWS_KMS'|'EXTERNAL'|'AWS_CLOUDHSM',
            'CustomKeyStoreId': 'string',
            'CloudHsmClusterId': 'string',
            'ExpirationModel': 'KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE',
            'KeyManager': 'AWS'|'CUSTOMER',
            'CustomerMasterKeySpec': 'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'|'ECC_SECG_P256K1'|'SYMMETRIC_DEFAULT',
            'EncryptionAlgorithms': [
                'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
            ],
            'SigningAlgorithms': [
                'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'|'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'|'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512',
            ]
        }
    }
    
    
    :returns: 
    Policy (string) -- The key policy to attach to the CMK.
    If you provide a key policy, it must meet the following criteria:
    
    If you don\'t set BypassPolicyLockoutSafetyCheck to true, the key policy must allow the principal that is making the CreateKey request to make a subsequent  PutKeyPolicy request on the CMK. This reduces the risk that the CMK becomes unmanageable. For more information, refer to the scenario in the Default Key Policy section of the * AWS Key Management Service Developer Guide * .
    Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to AWS KMS. For more information, see Changes that I make are not always immediately visible in the AWS Identity and Access Management User Guide .
    
    If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK. For more information, see Default Key Policy in the AWS Key Management Service Developer Guide .
    The key policy size quota is 32 kilobytes (32768 bytes).
    
    Description (string) -- A description of the CMK.
    Use a description that helps you decide whether the CMK is appropriate for a task.
    
    KeyUsage (string) -- Determines the cryptographic operations for which you can use the CMK. The default value is ENCRYPT_DECRYPT . This parameter is required only for asymmetric CMKs. You can\'t change the KeyUsage value after the CMK is created.
    Select only one valid value.
    
    For symmetric CMKs, omit the parameter or specify ENCRYPT_DECRYPT .
    For asymmetric CMKs with RSA key material, specify ENCRYPT_DECRYPT or SIGN_VERIFY .
    For asymmetric CMKs with ECC key material, specify SIGN_VERIFY .
    
    
    CustomerMasterKeySpec (string) -- Specifies the type of CMK to create. The default value, SYMMETRIC_DEFAULT , creates a CMK with a 256-bit symmetric key for encryption and decryption. For help choosing a key spec for your CMK, see How to Choose Your CMK Configuration in the AWS Key Management Service Developer Guide .
    The CustomerMasterKeySpec determines whether the CMK contains a symmetric key or an asymmetric key pair. It also determines the encryption algorithms or signing algorithms that the CMK supports. You can\'t change the CustomerMasterKeySpec after the CMK is created. To further restrict the algorithms that can be used with the CMK, use a condition key in its key policy or IAM policy. For more information, see kms:EncryptionAlgorithm or kms:Signing Algorithm in the AWS Key Management Service Developer Guide .
    
    Warning
    AWS services that are integrated with AWS KMS use symmetric CMKs to protect your data. These services do not support asymmetric CMKs. For help determining whether a CMK is symmetric or asymmetric, see Identifying Symmetric and Asymmetric CMKs in the AWS Key Management Service Developer Guide .
    
    AWS KMS supports the following key specs for CMKs:
    
    Symmetric key (default)
    SYMMETRIC_DEFAULT (AES-256-GCM)
    
    
    Asymmetric RSA key pairs
    RSA_2048
    RSA_3072
    RSA_4096
    
    
    Asymmetric NIST-recommended elliptic curve key pairs
    ECC_NIST_P256 (secp256r1)
    ECC_NIST_P384 (secp384r1)
    ECC_NIST_P521 (secp521r1)
    
    
    Other asymmetric elliptic curve key pairs
    ECC_SECG_P256K1 (secp256k1), commonly used for cryptocurrencies.
    
    
    
    
    Origin (string) -- The source of the key material for the CMK. You cannot change the origin after you create the CMK. The default is AWS_KMS , which means AWS KMS creates the key material.
    When the parameter value is EXTERNAL , AWS KMS creates a CMK without key material so that you can import key material from your existing key management infrastructure. For more information about importing key material into AWS KMS, see Importing Key Material in the AWS Key Management Service Developer Guide . This value is valid only for symmetric CMKs.
    When the parameter value is AWS_CLOUDHSM , AWS KMS creates the CMK in an AWS KMS custom key store and creates its key material in the associated AWS CloudHSM cluster. You must also use the CustomKeyStoreId parameter to identify the custom key store. This value is valid only for symmetric CMKs.
    
    CustomKeyStoreId (string) -- Creates the CMK in the specified custom key store and the key material in its associated AWS CloudHSM cluster. To create a CMK in a custom key store, you must also specify the Origin parameter with a value of AWS_CLOUDHSM . The AWS CloudHSM cluster that is associated with the custom key store must have at least two active HSMs, each in a different Availability Zone in the Region.
    This parameter is valid only for symmetric CMKs. You cannot create an asymmetric CMK in a custom key store.
    To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.
    The response includes the custom key store ID and the ID of the AWS CloudHSM cluster.
    This operation is part of the Custom Key Store feature feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a single-tenant key store.
    
    BypassPolicyLockoutSafetyCheck (boolean) -- A flag to indicate whether to bypass the key policy lockout safety check.
    
    Warning
    Setting this value to true increases the risk that the CMK becomes unmanageable. Do not set this value to true indiscriminately.
    For more information, refer to the scenario in the Default Key Policy section in the * AWS Key Management Service Developer Guide * .
    
    Use this parameter only when you include a policy in the request and you intend to prevent the principal that is making the request from making a subsequent  PutKeyPolicy request on the CMK.
    The default value is false.
    
    Tags (list) -- One or more tags. Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string.
    When you add tags to an AWS resource, AWS generates a cost allocation report with usage and costs aggregated by tags. For information about adding, changing, deleting and listing tags for CMKs, see Tagging Keys .
    Use this parameter to tag the CMK when it is created. To add tags to an existing CMK, use the  TagResource operation.
    
    (dict) --A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.
    For information about the rules that apply to tag keys and tag values, see User-Defined Tag Restrictions in the AWS Billing and Cost Management User Guide .
    
    TagKey (string) -- [REQUIRED]The key of the tag.
    
    TagValue (string) -- [REQUIRED]The value of the tag.
    
    
    
    
    
    
    """
    pass

def decrypt(CiphertextBlob=None, EncryptionContext=None, GrantTokens=None, KeyId=None, EncryptionAlgorithm=None):
    """
    Decrypts ciphertext that was encrypted by a AWS KMS customer master key (CMK) using any of the following operations:
    You can use this operation to decrypt ciphertext that was encrypted under a symmetric or asymmetric CMK. When the CMK is asymmetric, you must specify the CMK and the encryption algorithm that was used to encrypt the ciphertext. For information about symmetric and asymmetric CMKs, see Using Symmetric and Asymmetric CMKs in the AWS Key Management Service Developer Guide .
    The Decrypt operation also decrypts ciphertext that was encrypted outside of AWS KMS by the public key in an AWS KMS asymmetric CMK. However, it cannot decrypt ciphertext produced by other libraries, such as the AWS Encryption SDK or Amazon S3 client-side encryption . These libraries return a ciphertext format that is incompatible with AWS KMS.
    If the ciphertext was encrypted under a symmetric CMK, you do not need to specify the CMK or the encryption algorithm. AWS KMS can get this information from metadata that it adds to the symmetric ciphertext blob. However, if you prefer, you can specify the KeyId to ensure that a particular CMK is used to decrypt the ciphertext. If you specify a different CMK than the one used to encrypt the ciphertext, the Decrypt operation fails.
    Whenever possible, use key policies to give users permission to call the Decrypt operation on a particular CMK, instead of using IAM policies. Otherwise, you might create an IAM user policy that gives the user Decrypt permission on all CMKs. This user could decrypt ciphertext that was encrypted by CMKs in other accounts if the key policy for the cross-account CMK permits it. If you must use an IAM policy for Decrypt permissions, limit the user to particular CMKs or particular trusted accounts.
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example decrypts data that was encrypted with a customer master key (CMK) in AWS KMS.
    Expected Output:
    
    :example: response = client.decrypt(
        CiphertextBlob=b'bytes',
        EncryptionContext={
            'string': 'string'
        },
        GrantTokens=[
            'string',
        ],
        KeyId='string',
        EncryptionAlgorithm='SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256'
    )
    
    
    :type CiphertextBlob: bytes
    :param CiphertextBlob: [REQUIRED]\nCiphertext to be decrypted. The blob includes metadata.\n

    :type EncryptionContext: dict
    :param EncryptionContext: Specifies the encryption context to use when decrypting the data. An encryption context is valid only for cryptographic operations with a symmetric CMK. The standard asymmetric encryption algorithms that AWS KMS uses do not support an encryption context.\nAn encryption context is a collection of non-secret key-value pairs that represents additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is optional when encrypting with a symmetric CMK, but it is highly recommended.\nFor more information, see Encryption Context in the AWS Key Management Service Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.\nFor more information, see Grant Tokens in the AWS Key Management Service Developer Guide .\n\n(string) --\n\n

    :type KeyId: string
    :param KeyId: Specifies the customer master key (CMK) that AWS KMS will use to decrypt the ciphertext. Enter a key ID of the CMK that was used to encrypt the ciphertext.\nIf you specify a KeyId value, the Decrypt operation succeeds only if the specified CMK was used to encrypt the ciphertext.\nThis parameter is required only when the ciphertext was encrypted under an asymmetric CMK. Otherwise, AWS KMS uses the metadata that it adds to the ciphertext blob to determine which CMK was used to encrypt the ciphertext. However, you can use this parameter to ensure that a particular CMK (of any kind) is used to decrypt the ciphertext.\nTo specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with 'alias/' .\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\nAlias name: alias/ExampleAlias\nAlias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey . To get the alias name and alias ARN, use ListAliases .\n

    :type EncryptionAlgorithm: string
    :param EncryptionAlgorithm: Specifies the encryption algorithm that will be used to decrypt the ciphertext. Specify the same algorithm that was used to encrypt the data. If you specify a different algorithm, the Decrypt operation fails.\nThis parameter is required only when the ciphertext was encrypted under an asymmetric CMK. The default value, SYMMETRIC_DEFAULT , represents the only supported algorithm that is valid for symmetric CMKs.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'KeyId': 'string',
    'Plaintext': b'bytes',
    'EncryptionAlgorithm': 'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256'
}


Response Structure

(dict) --

KeyId (string) --
The ARN of the customer master key that was used to perform the decryption.

Plaintext (bytes) --
Decrypted plaintext data. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.

EncryptionAlgorithm (string) --
The encryption algorithm that was used to decrypt the ciphertext.







Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.DisabledException
KMS.Client.exceptions.InvalidCiphertextException
KMS.Client.exceptions.KeyUnavailableException
KMS.Client.exceptions.IncorrectKeyException
KMS.Client.exceptions.InvalidKeyUsageException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.InvalidGrantTokenException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException

Examples
The following example decrypts data that was encrypted with a customer master key (CMK) in AWS KMS.
response = client.decrypt(
    # The encrypted data (ciphertext).
    CiphertextBlob='<binary data>',
)

print(response)


Expected Output:
{
    # The Amazon Resource Name (ARN) of the CMK that was used to decrypt the data.
    'KeyId': 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
    # The decrypted (plaintext) data.
    'Plaintext': '<binary data>',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'KeyId': 'string',
        'Plaintext': b'bytes',
        'EncryptionAlgorithm': 'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256'
    }
    
    
    :returns: 
    CiphertextBlob (bytes) -- [REQUIRED]
    Ciphertext to be decrypted. The blob includes metadata.
    
    EncryptionContext (dict) -- Specifies the encryption context to use when decrypting the data. An encryption context is valid only for cryptographic operations with a symmetric CMK. The standard asymmetric encryption algorithms that AWS KMS uses do not support an encryption context.
    An encryption context is a collection of non-secret key-value pairs that represents additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is optional when encrypting with a symmetric CMK, but it is highly recommended.
    For more information, see Encryption Context in the AWS Key Management Service Developer Guide .
    
    (string) --
    (string) --
    
    
    
    
    GrantTokens (list) -- A list of grant tokens.
    For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
    
    (string) --
    
    
    KeyId (string) -- Specifies the customer master key (CMK) that AWS KMS will use to decrypt the ciphertext. Enter a key ID of the CMK that was used to encrypt the ciphertext.
    If you specify a KeyId value, the Decrypt operation succeeds only if the specified CMK was used to encrypt the ciphertext.
    This parameter is required only when the ciphertext was encrypted under an asymmetric CMK. Otherwise, AWS KMS uses the metadata that it adds to the ciphertext blob to determine which CMK was used to encrypt the ciphertext. However, you can use this parameter to ensure that a particular CMK (of any kind) is used to decrypt the ciphertext.
    To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with "alias/" .
    For example:
    
    Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
    Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
    Alias name: alias/ExampleAlias
    Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias
    
    To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .
    
    EncryptionAlgorithm (string) -- Specifies the encryption algorithm that will be used to decrypt the ciphertext. Specify the same algorithm that was used to encrypt the data. If you specify a different algorithm, the Decrypt operation fails.
    This parameter is required only when the ciphertext was encrypted under an asymmetric CMK. The default value, SYMMETRIC_DEFAULT , represents the only supported algorithm that is valid for symmetric CMKs.
    
    
    """
    pass

def delete_alias(AliasName=None):
    """
    Deletes the specified alias. You cannot perform this operation on an alias in a different AWS account.
    Because an alias is not a property of a CMK, you can delete and change the aliases of a CMK without affecting the CMK. Also, aliases do not appear in the response from the  DescribeKey operation. To get the aliases of all CMKs, use the  ListAliases operation.
    Each CMK can have multiple aliases. To change the alias of a CMK, use  DeleteAlias to delete the current alias and  CreateAlias to create a new alias. To associate an existing alias with a different customer master key (CMK), call  UpdateAlias .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes the specified alias.
    Expected Output:
    
    :example: response = client.delete_alias(
        AliasName='string'
    )
    
    
    :type AliasName: string
    :param AliasName: [REQUIRED]\nThe alias to be deleted. The alias name must begin with alias/ followed by the alias name, such as alias/ExampleAlias .\n

    :return: response = client.delete_alias(
        # The alias to delete.
        AliasName='alias/ExampleAlias',
    )
    
    print(response)
    
    
    """
    pass

def delete_custom_key_store(CustomKeyStoreId=None):
    """
    Deletes a custom key store . This operation does not delete the AWS CloudHSM cluster that is associated with the custom key store, or affect any users or keys in the cluster.
    The custom key store that you delete cannot contain any AWS KMS customer master keys (CMKs) . Before deleting the key store, verify that you will never need to use any of the CMKs in the key store for any cryptographic operations. Then, use  ScheduleKeyDeletion to delete the AWS KMS customer master keys (CMKs) from the key store. When the scheduled waiting period expires, the ScheduleKeyDeletion operation deletes the CMKs. Then it makes a best effort to delete the key material from the associated cluster. However, you might need to manually delete the orphaned key material from the cluster and its backups.
    After all CMKs are deleted from AWS KMS, use  DisconnectCustomKeyStore to disconnect the key store from AWS KMS. Then, you can delete the custom key store.
    Instead of deleting the custom key store, consider using  DisconnectCustomKeyStore to disconnect it from AWS KMS. While the key store is disconnected, you cannot create or use the CMKs in the key store. But, you do not need to delete CMKs and you can reconnect a disconnected custom key store at any time.
    If the operation succeeds, it returns a JSON object with no properties.
    This operation is part of the Custom Key Store feature feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a single-tenant key store.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_custom_key_store(
        CustomKeyStoreId='string'
    )
    
    
    :type CustomKeyStoreId: string
    :param CustomKeyStoreId: [REQUIRED]\nEnter the ID of the custom key store you want to delete. To find the ID of a custom key store, use the DescribeCustomKeyStores operation.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

KMS.Client.exceptions.CustomKeyStoreHasCMKsException
KMS.Client.exceptions.CustomKeyStoreInvalidStateException
KMS.Client.exceptions.CustomKeyStoreNotFoundException
KMS.Client.exceptions.KMSInternalException


    :return: {}
    
    
    :returns: 
    KMS.Client.exceptions.CustomKeyStoreHasCMKsException
    KMS.Client.exceptions.CustomKeyStoreInvalidStateException
    KMS.Client.exceptions.CustomKeyStoreNotFoundException
    KMS.Client.exceptions.KMSInternalException
    
    """
    pass

def delete_imported_key_material(KeyId=None):
    """
    Deletes key material that you previously imported. This operation makes the specified customer master key (CMK) unusable. For more information about importing key material into AWS KMS, see Importing Key Material in the AWS Key Management Service Developer Guide . You cannot perform this operation on a CMK in a different AWS account.
    When the specified CMK is in the PendingDeletion state, this operation does not change the CMK\'s state. Otherwise, it changes the CMK\'s state to PendingImport .
    After you delete key material, you can use  ImportKeyMaterial to reimport the same key material into the CMK.
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes the imported key material from the specified customer master key (CMK).
    Expected Output:
    
    :example: response = client.delete_imported_key_material(
        KeyId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nIdentifies the CMK from which you are deleting imported key material. The Origin of the CMK must be EXTERNAL .\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :return: response = client.delete_imported_key_material(
        # The identifier of the CMK whose imported key material you are deleting. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
        KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
    )
    
    print(response)
    
    
    :returns: 
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.UnsupportedOperationException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.KMSInvalidStateException
    
    """
    pass

def describe_custom_key_stores(CustomKeyStoreId=None, CustomKeyStoreName=None, Limit=None, Marker=None):
    """
    Gets information about custom key stores in the account and region.
    This operation is part of the Custom Key Store feature feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a single-tenant key store.
    By default, this operation returns information about all custom key stores in the account and region. To get only information about a particular custom key store, use either the CustomKeyStoreName or CustomKeyStoreId parameter (but not both).
    To determine whether the custom key store is connected to its AWS CloudHSM cluster, use the ConnectionState element in the response. If an attempt to connect the custom key store failed, the ConnectionState value is FAILED and the ConnectionErrorCode element in the response indicates the cause of the failure. For help interpreting the ConnectionErrorCode , see  CustomKeyStoresListEntry .
    Custom key stores have a DISCONNECTED connection state if the key store has never been connected or you use the  DisconnectCustomKeyStore operation to disconnect it. If your custom key store state is CONNECTED but you are having trouble using it, make sure that its associated AWS CloudHSM cluster is active and contains the minimum number of HSMs required for the operation, if any.
    For help repairing your custom key store, see the Troubleshooting Custom Key Stores topic in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_custom_key_stores(
        CustomKeyStoreId='string',
        CustomKeyStoreName='string',
        Limit=123,
        Marker='string'
    )
    
    
    :type CustomKeyStoreId: string
    :param CustomKeyStoreId: Gets only information about the specified custom key store. Enter the key store ID.\nBy default, this operation gets information about all custom key stores in the account and region. To limit the output to a particular custom key store, you can use either the CustomKeyStoreId or CustomKeyStoreName parameter, but not both.\n

    :type CustomKeyStoreName: string
    :param CustomKeyStoreName: Gets only information about the specified custom key store. Enter the friendly name of the custom key store.\nBy default, this operation gets information about all custom key stores in the account and region. To limit the output to a particular custom key store, you can use either the CustomKeyStoreId or CustomKeyStoreName parameter, but not both.\n

    :type Limit: integer
    :param Limit: Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.

    :type Marker: string
    :param Marker: Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the truncated response you just received.

    :rtype: dict

ReturnsResponse Syntax
{
    'CustomKeyStores': [
        {
            'CustomKeyStoreId': 'string',
            'CustomKeyStoreName': 'string',
            'CloudHsmClusterId': 'string',
            'TrustAnchorCertificate': 'string',
            'ConnectionState': 'CONNECTED'|'CONNECTING'|'FAILED'|'DISCONNECTED'|'DISCONNECTING',
            'ConnectionErrorCode': 'INVALID_CREDENTIALS'|'CLUSTER_NOT_FOUND'|'NETWORK_ERRORS'|'INTERNAL_ERROR'|'INSUFFICIENT_CLOUDHSM_HSMS'|'USER_LOCKED_OUT'|'USER_NOT_FOUND'|'USER_LOGGED_IN'|'SUBNET_NOT_FOUND',
            'CreationDate': datetime(2015, 1, 1)
        },
    ],
    'NextMarker': 'string',
    'Truncated': True|False
}


Response Structure

(dict) --

CustomKeyStores (list) --
Contains metadata about each custom key store.

(dict) --
Contains information about each custom key store in the custom key store list.

CustomKeyStoreId (string) --
A unique identifier for the custom key store.

CustomKeyStoreName (string) --
The user-specified friendly name for the custom key store.

CloudHsmClusterId (string) --
A unique identifier for the AWS CloudHSM cluster that is associated with the custom key store.

TrustAnchorCertificate (string) --
The trust anchor certificate of the associated AWS CloudHSM cluster. When you initialize the cluster , you create this certificate and save it in the customerCA.crt file.

ConnectionState (string) --
Indicates whether the custom key store is connected to its AWS CloudHSM cluster.
You can create and use CMKs in your custom key stores only when its connection state is CONNECTED .
The value is DISCONNECTED if the key store has never been connected or you use the  DisconnectCustomKeyStore operation to disconnect it. If the value is CONNECTED but you are having trouble using the custom key store, make sure that its associated AWS CloudHSM cluster is active and contains at least one active HSM.
A value of FAILED indicates that an attempt to connect was unsuccessful. The ConnectionErrorCode field in the response indicates the cause of the failure. For help resolving a connection failure, see Troubleshooting a Custom Key Store in the AWS Key Management Service Developer Guide .

ConnectionErrorCode (string) --
Describes the connection error. This field appears in the response only when the ConnectionState is FAILED . For help resolving these errors, see How to Fix a Connection Failure in AWS Key Management Service Developer Guide .
Valid values are:

CLUSTER_NOT_FOUND - AWS KMS cannot find the AWS CloudHSM cluster with the specified cluster ID.
INSUFFICIENT_CLOUDHSM_HSMS - The associated AWS CloudHSM cluster does not contain any active HSMs. To connect a custom key store to its AWS CloudHSM cluster, the cluster must contain at least one active HSM.
INTERNAL_ERROR - AWS KMS could not complete the request due to an internal error. Retry the request. For ConnectCustomKeyStore requests, disconnect the custom key store before trying to connect again.
INVALID_CREDENTIALS - AWS KMS does not have the correct password for the kmsuser crypto user in the AWS CloudHSM cluster. Before you can connect your custom key store to its AWS CloudHSM cluster, you must change the kmsuser account password and update the key store password value for the custom key store.
NETWORK_ERRORS - Network errors are preventing AWS KMS from connecting to the custom key store.
SUBNET_NOT_FOUND - A subnet in the AWS CloudHSM cluster configuration was deleted. If AWS KMS cannot find all of the subnets that were configured for the cluster when the custom key store was created, attempts to connect fail. To fix this error, create a cluster from a backup and associate it with your custom key store. This process includes selecting a VPC and subnets. For details, see How to Fix a Connection Failure in the AWS Key Management Service Developer Guide .
USER_LOCKED_OUT - The kmsuser CU account is locked out of the associated AWS CloudHSM cluster due to too many failed password attempts. Before you can connect your custom key store to its AWS CloudHSM cluster, you must change the kmsuser account password and update the key store password value for the custom key store.
USER_LOGGED_IN - The kmsuser CU account is logged into the the associated AWS CloudHSM cluster. This prevents AWS KMS from rotating the kmsuser account password and logging into the cluster. Before you can connect your custom key store to its AWS CloudHSM cluster, you must log the kmsuser CU out of the cluster. If you changed the kmsuser password to log into the cluster, you must also and update the key store password value for the custom key store. For help, see How to Log Out and Reconnect in the AWS Key Management Service Developer Guide .
USER_NOT_FOUND - AWS KMS cannot find a kmsuser CU account in the associated AWS CloudHSM cluster. Before you can connect your custom key store to its AWS CloudHSM cluster, you must create a kmsuser CU account in the cluster, and then update the key store password value for the custom key store.


CreationDate (datetime) --
The date and time when the custom key store was created.





NextMarker (string) --
When Truncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent request.

Truncated (boolean) --
A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the NextMarker element in thisresponse to the Marker parameter in a subsequent request.







Exceptions

KMS.Client.exceptions.CustomKeyStoreNotFoundException
KMS.Client.exceptions.KMSInternalException


    :return: {
        'CustomKeyStores': [
            {
                'CustomKeyStoreId': 'string',
                'CustomKeyStoreName': 'string',
                'CloudHsmClusterId': 'string',
                'TrustAnchorCertificate': 'string',
                'ConnectionState': 'CONNECTED'|'CONNECTING'|'FAILED'|'DISCONNECTED'|'DISCONNECTING',
                'ConnectionErrorCode': 'INVALID_CREDENTIALS'|'CLUSTER_NOT_FOUND'|'NETWORK_ERRORS'|'INTERNAL_ERROR'|'INSUFFICIENT_CLOUDHSM_HSMS'|'USER_LOCKED_OUT'|'USER_NOT_FOUND'|'USER_LOGGED_IN'|'SUBNET_NOT_FOUND',
                'CreationDate': datetime(2015, 1, 1)
            },
        ],
        'NextMarker': 'string',
        'Truncated': True|False
    }
    
    
    :returns: 
    CLUSTER_NOT_FOUND - AWS KMS cannot find the AWS CloudHSM cluster with the specified cluster ID.
    INSUFFICIENT_CLOUDHSM_HSMS - The associated AWS CloudHSM cluster does not contain any active HSMs. To connect a custom key store to its AWS CloudHSM cluster, the cluster must contain at least one active HSM.
    INTERNAL_ERROR - AWS KMS could not complete the request due to an internal error. Retry the request. For ConnectCustomKeyStore requests, disconnect the custom key store before trying to connect again.
    INVALID_CREDENTIALS - AWS KMS does not have the correct password for the kmsuser crypto user in the AWS CloudHSM cluster. Before you can connect your custom key store to its AWS CloudHSM cluster, you must change the kmsuser account password and update the key store password value for the custom key store.
    NETWORK_ERRORS - Network errors are preventing AWS KMS from connecting to the custom key store.
    SUBNET_NOT_FOUND - A subnet in the AWS CloudHSM cluster configuration was deleted. If AWS KMS cannot find all of the subnets that were configured for the cluster when the custom key store was created, attempts to connect fail. To fix this error, create a cluster from a backup and associate it with your custom key store. This process includes selecting a VPC and subnets. For details, see How to Fix a Connection Failure in the AWS Key Management Service Developer Guide .
    USER_LOCKED_OUT - The kmsuser CU account is locked out of the associated AWS CloudHSM cluster due to too many failed password attempts. Before you can connect your custom key store to its AWS CloudHSM cluster, you must change the kmsuser account password and update the key store password value for the custom key store.
    USER_LOGGED_IN - The kmsuser CU account is logged into the the associated AWS CloudHSM cluster. This prevents AWS KMS from rotating the kmsuser account password and logging into the cluster. Before you can connect your custom key store to its AWS CloudHSM cluster, you must log the kmsuser CU out of the cluster. If you changed the kmsuser password to log into the cluster, you must also and update the key store password value for the custom key store. For help, see How to Log Out and Reconnect in the AWS Key Management Service Developer Guide .
    USER_NOT_FOUND - AWS KMS cannot find a kmsuser CU account in the associated AWS CloudHSM cluster. Before you can connect your custom key store to its AWS CloudHSM cluster, you must create a kmsuser CU account in the cluster, and then update the key store password value for the custom key store.
    
    """
    pass

def describe_key(KeyId=None, GrantTokens=None):
    """
    Provides detailed information about a customer master key (CMK). You can run DescribeKey on a customer managed CMK or an AWS managed CMK .
    This detailed information includes the key ARN, creation date (and deletion date, if applicable), the key state, and the origin and expiration date (if any) of the key material. For CMKs in custom key stores, it includes information about the custom key store, such as the key store ID and the AWS CloudHSM cluster ID. It includes fields, like KeySpec , that help you distinguish symmetric from asymmetric CMKs. It also provides information that is particularly important to asymmetric CMKs, such as the key usage (encryption or signing) and the encryption algorithms or signing algorithms that the CMK supports.
    If you call the DescribeKey operation on a predefined AWS alias , that is, an AWS alias with no key ID, AWS KMS creates an AWS managed CMK . Then, it associates the alias with the new CMK, and returns the KeyId and Arn of the new CMK in the response.
    To perform this operation on a CMK in a different AWS account, specify the key ARN or alias ARN in the value of the KeyId parameter.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information (metadata) about the specified CMK.
    Expected Output:
    
    :example: response = client.describe_key(
        KeyId='string',
        GrantTokens=[
            'string',
        ]
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nDescribes the specified customer master key (CMK).\nIf you specify a predefined AWS alias (an AWS alias with no key ID), KMS associates the alias with an AWS managed CMK and returns its KeyId and Arn in the response.\nTo specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with 'alias/' . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\nAlias name: alias/ExampleAlias\nAlias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey . To get the alias name and alias ARN, use ListAliases .\n

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.\nFor more information, see Grant Tokens in the AWS Key Management Service Developer Guide .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'KeyMetadata': {
        'AWSAccountId': 'string',
        'KeyId': 'string',
        'Arn': 'string',
        'CreationDate': datetime(2015, 1, 1),
        'Enabled': True|False,
        'Description': 'string',
        'KeyUsage': 'SIGN_VERIFY'|'ENCRYPT_DECRYPT',
        'KeyState': 'Enabled'|'Disabled'|'PendingDeletion'|'PendingImport'|'Unavailable',
        'DeletionDate': datetime(2015, 1, 1),
        'ValidTo': datetime(2015, 1, 1),
        'Origin': 'AWS_KMS'|'EXTERNAL'|'AWS_CLOUDHSM',
        'CustomKeyStoreId': 'string',
        'CloudHsmClusterId': 'string',
        'ExpirationModel': 'KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE',
        'KeyManager': 'AWS'|'CUSTOMER',
        'CustomerMasterKeySpec': 'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'|'ECC_SECG_P256K1'|'SYMMETRIC_DEFAULT',
        'EncryptionAlgorithms': [
            'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
        ],
        'SigningAlgorithms': [
            'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'|'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'|'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512',
        ]
    }
}


Response Structure

(dict) --

KeyMetadata (dict) --
Metadata associated with the key.

AWSAccountId (string) --
The twelve-digit account ID of the AWS account that owns the CMK.

KeyId (string) --
The globally unique identifier for the CMK.

Arn (string) --
The Amazon Resource Name (ARN) of the CMK. For examples, see AWS Key Management Service (AWS KMS) in the Example ARNs section of the AWS General Reference .

CreationDate (datetime) --
The date and time when the CMK was created.

Enabled (boolean) --
Specifies whether the CMK is enabled. When KeyState is Enabled this value is true, otherwise it is false.

Description (string) --
The description of the CMK.

KeyUsage (string) --
The cryptographic operations for which you can use the CMK.

KeyState (string) --
The state of the CMK.
For more information about how key state affects the use of a CMK, see How Key State Affects the Use of a Customer Master Key in the AWS Key Management Service Developer Guide .

DeletionDate (datetime) --
The date and time after which AWS KMS deletes the CMK. This value is present only when KeyState is PendingDeletion .

ValidTo (datetime) --
The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. This value is present only for CMKs whose Origin is EXTERNAL and whose ExpirationModel is KEY_MATERIAL_EXPIRES , otherwise this value is omitted.

Origin (string) --
The source of the CMK\'s key material. When this value is AWS_KMS , AWS KMS created the key material. When this value is EXTERNAL , the key material was imported from your existing key management infrastructure or the CMK lacks key material. When this value is AWS_CLOUDHSM , the key material was created in the AWS CloudHSM cluster associated with a custom key store.

CustomKeyStoreId (string) --
A unique identifier for the custom key store that contains the CMK. This value is present only when the CMK is created in a custom key store.

CloudHsmClusterId (string) --
The cluster ID of the AWS CloudHSM cluster that contains the key material for the CMK. When you create a CMK in a custom key store , AWS KMS creates the key material for the CMK in the associated AWS CloudHSM cluster. This value is present only when the CMK is created in a custom key store.

ExpirationModel (string) --
Specifies whether the CMK\'s key material expires. This value is present only when Origin is EXTERNAL , otherwise this value is omitted.

KeyManager (string) --
The manager of the CMK. CMKs in your AWS account are either customer managed or AWS managed. For more information about the difference, see Customer Master Keys in the AWS Key Management Service Developer Guide .

CustomerMasterKeySpec (string) --
Describes the type of key material in the CMK.

EncryptionAlgorithms (list) --
A list of encryption algorithms that the CMK supports. You cannot use the CMK with other encryption algorithms within AWS KMS.
This field appears only when the KeyUsage of the CMK is ENCRYPT_DECRYPT .

(string) --


SigningAlgorithms (list) --
A list of signing algorithms that the CMK supports. You cannot use the CMK with other signing algorithms within AWS KMS.
This field appears only when the KeyUsage of the CMK is SIGN_VERIFY .

(string) --










Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.KMSInternalException

Examples
The following example returns information (metadata) about the specified CMK.
response = client.describe_key(
    # The identifier of the CMK that you want information about. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
    KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
)

print(response)


Expected Output:
{
    # An object that contains information about the specified CMK.
    'KeyMetadata': {
        'AWSAccountId': '111122223333',
        'Arn': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
        'CreationDate': datetime(2017, 7, 5, 14, 4, 55, 2, 186, 0),
        'Description': '',
        'Enabled': True,
        'KeyId': '1234abcd-12ab-34cd-56ef-1234567890ab',
        'KeyManager': 'CUSTOMER',
        'KeyState': 'Enabled',
        'KeyUsage': 'ENCRYPT_DECRYPT',
        'Origin': 'AWS_KMS',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'KeyMetadata': {
            'AWSAccountId': 'string',
            'KeyId': 'string',
            'Arn': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'Enabled': True|False,
            'Description': 'string',
            'KeyUsage': 'SIGN_VERIFY'|'ENCRYPT_DECRYPT',
            'KeyState': 'Enabled'|'Disabled'|'PendingDeletion'|'PendingImport'|'Unavailable',
            'DeletionDate': datetime(2015, 1, 1),
            'ValidTo': datetime(2015, 1, 1),
            'Origin': 'AWS_KMS'|'EXTERNAL'|'AWS_CLOUDHSM',
            'CustomKeyStoreId': 'string',
            'CloudHsmClusterId': 'string',
            'ExpirationModel': 'KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE',
            'KeyManager': 'AWS'|'CUSTOMER',
            'CustomerMasterKeySpec': 'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'|'ECC_SECG_P256K1'|'SYMMETRIC_DEFAULT',
            'EncryptionAlgorithms': [
                'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
            ],
            'SigningAlgorithms': [
                'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'|'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'|'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512',
            ]
        }
    }
    
    
    :returns: 
    KeyId (string) -- [REQUIRED]
    Describes the specified customer master key (CMK).
    If you specify a predefined AWS alias (an AWS alias with no key ID), KMS associates the alias with an AWS managed CMK and returns its KeyId and Arn in the response.
    To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with "alias/" . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.
    For example:
    
    Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
    Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
    Alias name: alias/ExampleAlias
    Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias
    
    To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .
    
    GrantTokens (list) -- A list of grant tokens.
    For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
    
    (string) --
    
    
    
    """
    pass

def disable_key(KeyId=None):
    """
    Sets the state of a customer master key (CMK) to disabled, thereby preventing its use for cryptographic operations. You cannot perform this operation on a CMK in a different AWS account.
    For more information about how key state affects the use of a CMK, see How Key State Affects the Use of a Customer Master Key in the * AWS Key Management Service Developer Guide * .
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example disables the specified CMK.
    Expected Output:
    
    :example: response = client.disable_key(
        KeyId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nA unique identifier for the customer master key (CMK).\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :return: response = client.disable_key(
        # The identifier of the CMK to disable. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
        KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
    )
    
    print(response)
    
    
    :returns: 
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.KMSInvalidStateException
    
    """
    pass

def disable_key_rotation(KeyId=None):
    """
    Disables automatic rotation of the key material for the specified symmetric customer master key (CMK).
    You cannot enable automatic rotation of asymmetric CMKs, CMKs with imported key material, or CMKs in a custom key store . You cannot perform this operation on a CMK in a different AWS account.
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example disables automatic annual rotation of the key material for the specified CMK.
    Expected Output:
    
    :example: response = client.disable_key_rotation(
        KeyId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nIdentifies a symmetric customer master key (CMK). You cannot enable automatic rotation of asymmetric CMKs , CMKs with imported key material , or CMKs in a custom key store .\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :return: response = client.disable_key_rotation(
        # The identifier of the CMK whose key material will no longer be rotated. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
        KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
    )
    
    print(response)
    
    
    :returns: 
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.DisabledException
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.KMSInvalidStateException
    KMS.Client.exceptions.UnsupportedOperationException
    
    """
    pass

def disconnect_custom_key_store(CustomKeyStoreId=None):
    """
    Disconnects the custom key store from its associated AWS CloudHSM cluster. While a custom key store is disconnected, you can manage the custom key store and its customer master keys (CMKs), but you cannot create or use CMKs in the custom key store. You can reconnect the custom key store at any time.
    To find the connection state of a custom key store, use the  DescribeCustomKeyStores operation. To reconnect a custom key store, use the  ConnectCustomKeyStore operation.
    If the operation succeeds, it returns a JSON object with no properties.
    This operation is part of the Custom Key Store feature feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a single-tenant key store.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disconnect_custom_key_store(
        CustomKeyStoreId='string'
    )
    
    
    :type CustomKeyStoreId: string
    :param CustomKeyStoreId: [REQUIRED]\nEnter the ID of the custom key store you want to disconnect. To find the ID of a custom key store, use the DescribeCustomKeyStores operation.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

KMS.Client.exceptions.CustomKeyStoreInvalidStateException
KMS.Client.exceptions.CustomKeyStoreNotFoundException
KMS.Client.exceptions.KMSInternalException


    :return: {}
    
    
    :returns: 
    KMS.Client.exceptions.CustomKeyStoreInvalidStateException
    KMS.Client.exceptions.CustomKeyStoreNotFoundException
    KMS.Client.exceptions.KMSInternalException
    
    """
    pass

def enable_key(KeyId=None):
    """
    Sets the key state of a customer master key (CMK) to enabled. This allows you to use the CMK for cryptographic operations. You cannot perform this operation on a CMK in a different AWS account.
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example enables the specified CMK.
    Expected Output:
    
    :example: response = client.enable_key(
        KeyId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nA unique identifier for the customer master key (CMK).\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :return: response = client.enable_key(
        # The identifier of the CMK to enable. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
        KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
    )
    
    print(response)
    
    
    :returns: 
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.LimitExceededException
    KMS.Client.exceptions.KMSInvalidStateException
    
    """
    pass

def enable_key_rotation(KeyId=None):
    """
    Enables automatic rotation of the key material for the specified symmetric customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.
    You cannot enable automatic rotation of asymmetric CMKs, CMKs with imported key material, or CMKs in a custom key store .
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example enables automatic annual rotation of the key material for the specified CMK.
    Expected Output:
    
    :example: response = client.enable_key_rotation(
        KeyId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nIdentifies a symmetric customer master key (CMK). You cannot enable automatic rotation of asymmetric CMKs, CMKs with imported key material, or CMKs in a custom key store .\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :return: response = client.enable_key_rotation(
        # The identifier of the CMK whose key material will be rotated annually. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
        KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
    )
    
    print(response)
    
    
    :returns: 
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.DisabledException
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.KMSInvalidStateException
    KMS.Client.exceptions.UnsupportedOperationException
    
    """
    pass

def encrypt(KeyId=None, Plaintext=None, EncryptionContext=None, GrantTokens=None, EncryptionAlgorithm=None):
    """
    Encrypts plaintext into ciphertext by using a customer master key (CMK). The Encrypt operation has two primary use cases:
    You don\'t need to use the Encrypt operation to encrypt a data key. The  GenerateDataKey and  GenerateDataKeyPair operations return a plaintext data key and an encrypted copy of that data key.
    When you encrypt data, you must specify a symmetric or asymmetric CMK to use in the encryption operation. The CMK must have a Key value of ENCRYPT_DECRYPT. To find the Key of a CMK, use the  DescribeKey operation.
    If you use a symmetric CMK, you can use an encryption context to add additional security to your encryption operation. If you specify an EncryptionContext when encrypting data, you must specify the same encryption context (a case-sensitive exact match) when decrypting the data. Otherwise, the request to decrypt fails with an InvalidCiphertextException . For more information, see Encryption Context in the AWS Key Management Service Developer Guide .
    If you specify an asymmetric CMK, you must also specify the encryption algorithm. The algorithm must be compatible with the CMK type.
    The maximum size of the data that you can encrypt varies with the type of CMK and the encryption algorithm that you choose.
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    To perform this operation on a CMK in a different AWS account, specify the key ARN or alias ARN in the value of the KeyId parameter.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example encrypts data with the specified customer master key (CMK).
    Expected Output:
    
    :example: response = client.encrypt(
        KeyId='string',
        Plaintext=b'bytes',
        EncryptionContext={
            'string': 'string'
        },
        GrantTokens=[
            'string',
        ],
        EncryptionAlgorithm='SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nA unique identifier for the customer master key (CMK).\nTo specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with 'alias/' . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\nAlias name: alias/ExampleAlias\nAlias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey . To get the alias name and alias ARN, use ListAliases .\n

    :type Plaintext: bytes
    :param Plaintext: [REQUIRED]\nData to be encrypted.\n

    :type EncryptionContext: dict
    :param EncryptionContext: Specifies the encryption context that will be used to encrypt the data. An encryption context is valid only for cryptographic operations with a symmetric CMK. The standard asymmetric encryption algorithms that AWS KMS uses do not support an encryption context.\nAn encryption context is a collection of non-secret key-value pairs that represents additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is optional when encrypting with a symmetric CMK, but it is highly recommended.\nFor more information, see Encryption Context in the AWS Key Management Service Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.\nFor more information, see Grant Tokens in the AWS Key Management Service Developer Guide .\n\n(string) --\n\n

    :type EncryptionAlgorithm: string
    :param EncryptionAlgorithm: Specifies the encryption algorithm that AWS KMS will use to encrypt the plaintext message. The algorithm must be compatible with the CMK that you specify.\nThis parameter is required only for asymmetric CMKs. The default value, SYMMETRIC_DEFAULT , is the algorithm used for symmetric CMKs. If you are using an asymmetric CMK, we recommend RSAES_OAEP_SHA_256.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CiphertextBlob': b'bytes',
    'KeyId': 'string',
    'EncryptionAlgorithm': 'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256'
}


Response Structure

(dict) --

CiphertextBlob (bytes) --
The encrypted plaintext. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.

KeyId (string) --
The ID of the key used during encryption.

EncryptionAlgorithm (string) --
The encryption algorithm that was used to encrypt the plaintext.







Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.DisabledException
KMS.Client.exceptions.KeyUnavailableException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.InvalidKeyUsageException
KMS.Client.exceptions.InvalidGrantTokenException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException

Examples
The following example encrypts data with the specified customer master key (CMK).
response = client.encrypt(
    # The identifier of the CMK to use for encryption. You can use the key ID or Amazon Resource Name (ARN) of the CMK, or the name or ARN of an alias that refers to the CMK.
    KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
    # The data to encrypt.
    Plaintext='<binary data>',
)

print(response)


Expected Output:
{
    # The encrypted data (ciphertext).
    'CiphertextBlob': '<binary data>',
    # The ARN of the CMK that was used to encrypt the data.
    'KeyId': 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CiphertextBlob': b'bytes',
        'KeyId': 'string',
        'EncryptionAlgorithm': 'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256'
    }
    
    
    :returns: 
    Symmetric CMKs
    SYMMETRIC_DEFAULT : 4096 bytes
    
    
    RSA_2048
    RSAES_OAEP_SHA_1 : 214 bytes
    RSAES_OAEP_SHA_256 : 190 bytes
    
    
    RSA_3072
    RSAES_OAEP_SHA_1 : 342 bytes
    RSAES_OAEP_SHA_256 : 318 bytes
    
    
    RSA_4096
    RSAES_OAEP_SHA_1 : 470 bytes
    RSAES_OAEP_SHA_256 : 446 bytes
    
    
    
    """
    pass

def generate_data_key(KeyId=None, EncryptionContext=None, NumberOfBytes=None, KeySpec=None, GrantTokens=None):
    """
    Generates a unique symmetric data key. This operation returns a plaintext copy of the data key and a copy that is encrypted under a customer master key (CMK) that you specify. You can use the plaintext key to encrypt your data outside of AWS KMS and store the encrypted data key with the encrypted data.
    To generate a data key, specify the symmetric CMK that will be used to encrypt the data key. You cannot use an asymmetric CMK to generate data keys. To get the type of your CMK, use the  DescribeKey operation.
    You must also specify the length of the data key. Use either the KeySpec or NumberOfBytes parameters (but not both). For 128-bit and 256-bit data keys, use the KeySpec parameter.
    If the operation succeeds, the plaintext copy of the data key is in the Plaintext field of the response, and the encrypted copy of the data key in the CiphertextBlob field.
    To get only an encrypted copy of the data key, use  GenerateDataKeyWithoutPlaintext . To generate an asymmetric data key pair, use the  GenerateDataKeyPair or  GenerateDataKeyPairWithoutPlaintext operation. To get a cryptographically secure random byte string, use  GenerateRandom .
    You can use the optional encryption context to add additional security to the encryption operation. If you specify an EncryptionContext , you must specify the same encryption context (a case-sensitive exact match) when decrypting the encrypted data key. Otherwise, the request to decrypt fails with an InvalidCiphertextException. For more information, see Encryption Context in the AWS Key Management Service Developer Guide .
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    We recommend that you use the following pattern to encrypt data locally in your application:
    To decrypt data locally:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example generates a 256-bit symmetric data encryption key (data key) in two formats. One is the unencrypted (plainext) data key, and the other is the data key encrypted with the specified customer master key (CMK).
    Expected Output:
    
    :example: response = client.generate_data_key(
        KeyId='string',
        EncryptionContext={
            'string': 'string'
        },
        NumberOfBytes=123,
        KeySpec='AES_256'|'AES_128',
        GrantTokens=[
            'string',
        ]
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nIdentifies the symmetric CMK that encrypts the data key.\nTo specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with 'alias/' . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\nAlias name: alias/ExampleAlias\nAlias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey . To get the alias name and alias ARN, use ListAliases .\n

    :type EncryptionContext: dict
    :param EncryptionContext: Specifies the encryption context that will be used when encrypting the data key.\nAn encryption context is a collection of non-secret key-value pairs that represents additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is optional when encrypting with a symmetric CMK, but it is highly recommended.\nFor more information, see Encryption Context in the AWS Key Management Service Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type NumberOfBytes: integer
    :param NumberOfBytes: Specifies the length of the data key in bytes. For example, use the value 64 to generate a 512-bit data key (64 bytes is 512 bits). For 128-bit (16-byte) and 256-bit (32-byte) data keys, use the KeySpec parameter.\nYou must specify either the KeySpec or the NumberOfBytes parameter (but not both) in every GenerateDataKey request.\n

    :type KeySpec: string
    :param KeySpec: Specifies the length of the data key. Use AES_128 to generate a 128-bit symmetric key, or AES_256 to generate a 256-bit symmetric key.\nYou must specify either the KeySpec or the NumberOfBytes parameter (but not both) in every GenerateDataKey request.\n

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.\nFor more information, see Grant Tokens in the AWS Key Management Service Developer Guide .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CiphertextBlob': b'bytes',
    'Plaintext': b'bytes',
    'KeyId': 'string'
}


Response Structure

(dict) --

CiphertextBlob (bytes) --
The encrypted copy of the data key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.

Plaintext (bytes) --
The plaintext data key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded. Use this data key to encrypt your data outside of KMS. Then, remove it from memory as soon as possible.

KeyId (string) --
The identifier of the CMK that encrypted the data key.







Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.DisabledException
KMS.Client.exceptions.KeyUnavailableException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.InvalidKeyUsageException
KMS.Client.exceptions.InvalidGrantTokenException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException

Examples
The following example generates a 256-bit symmetric data encryption key (data key) in two formats. One is the unencrypted (plainext) data key, and the other is the data key encrypted with the specified customer master key (CMK).
response = client.generate_data_key(
    # The identifier of the CMK to use to encrypt the data key. You can use the key ID or Amazon Resource Name (ARN) of the CMK, or the name or ARN of an alias that refers to the CMK.
    KeyId='alias/ExampleAlias',
    # Specifies the type of data key to return.
    KeySpec='AES_256',
)

print(response)


Expected Output:
{
    # The encrypted data key.
    'CiphertextBlob': '<binary data>',
    # The ARN of the CMK that was used to encrypt the data key.
    'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
    # The unencrypted (plaintext) data key.
    'Plaintext': '<binary data>',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CiphertextBlob': b'bytes',
        'Plaintext': b'bytes',
        'KeyId': 'string'
    }
    
    
    :returns: 
    Use the  Decrypt operation to decrypt the encrypted data key. The operation returns a plaintext copy of the data key.
    Use the plaintext data key to decrypt data locally, then erase the plaintext data key from memory.
    
    """
    pass

def generate_data_key_pair(EncryptionContext=None, KeyId=None, KeyPairSpec=None, GrantTokens=None):
    """
    Generates a unique asymmetric data key pair. The GenerateDataKeyPair operation returns a plaintext public key, a plaintext private key, and a copy of the private key that is encrypted under the symmetric CMK you specify. You can use the data key pair to perform asymmetric cryptography outside of AWS KMS.
    You can use the public key that GenerateDataKeyPair returns to encrypt data or verify a signature outside of AWS KMS. Then, store the encrypted private key with the data. When you are ready to decrypt data or sign a message, you can use the  Decrypt operation to decrypt the encrypted private key.
    To generate a data key pair, you must specify a symmetric customer master key (CMK) to encrypt the private key in a data key pair. You cannot use an asymmetric CMK. To get the type of your CMK, use the  DescribeKey operation.
    If you are using the data key pair to encrypt data, or for any operation where you don\'t immediately need a private key, consider using the  GenerateDataKeyPairWithoutPlaintext operation. GenerateDataKeyPairWithoutPlaintext returns a plaintext public key and an encrypted private key, but omits the plaintext private key that you need only to decrypt ciphertext or sign a message. Later, when you need to decrypt the data or sign a message, use the  Decrypt operation to decrypt the encrypted private key in the data key pair.
    You can use the optional encryption context to add additional security to the encryption operation. If you specify an EncryptionContext , you must specify the same encryption context (a case-sensitive exact match) when decrypting the encrypted data key. Otherwise, the request to decrypt fails with an InvalidCiphertextException. For more information, see Encryption Context in the AWS Key Management Service Developer Guide .
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.generate_data_key_pair(
        EncryptionContext={
            'string': 'string'
        },
        KeyId='string',
        KeyPairSpec='RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'|'ECC_SECG_P256K1',
        GrantTokens=[
            'string',
        ]
    )
    
    
    :type EncryptionContext: dict
    :param EncryptionContext: Specifies the encryption context that will be used when encrypting the private key in the data key pair.\nAn encryption context is a collection of non-secret key-value pairs that represents additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is optional when encrypting with a symmetric CMK, but it is highly recommended.\nFor more information, see Encryption Context in the AWS Key Management Service Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type KeyId: string
    :param KeyId: [REQUIRED]\nSpecifies the symmetric CMK that encrypts the private key in the data key pair. You cannot specify an asymmetric CMKs.\nTo specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with 'alias/' . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\nAlias name: alias/ExampleAlias\nAlias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey . To get the alias name and alias ARN, use ListAliases .\n

    :type KeyPairSpec: string
    :param KeyPairSpec: [REQUIRED]\nDetermines the type of data key pair that is generated.\nThe AWS KMS rule that restricts the use of asymmetric RSA CMKs to encrypt and decrypt or to sign and verify (but not both), and the rule that permits you to use ECC CMKs only to sign and verify, are not effective outside of AWS KMS.\n

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.\nFor more information, see Grant Tokens in the AWS Key Management Service Developer Guide .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PrivateKeyCiphertextBlob': b'bytes',
    'PrivateKeyPlaintext': b'bytes',
    'PublicKey': b'bytes',
    'KeyId': 'string',
    'KeyPairSpec': 'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'|'ECC_SECG_P256K1'
}


Response Structure

(dict) --

PrivateKeyCiphertextBlob (bytes) --
The encrypted copy of the private key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.

PrivateKeyPlaintext (bytes) --
The plaintext copy of the private key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.

PublicKey (bytes) --
The public key (in plaintext).

KeyId (string) --
The identifier of the CMK that encrypted the private key.

KeyPairSpec (string) --
The type of data key pair that was generated.







Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.DisabledException
KMS.Client.exceptions.KeyUnavailableException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.InvalidKeyUsageException
KMS.Client.exceptions.InvalidGrantTokenException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException


    :return: {
        'PrivateKeyCiphertextBlob': b'bytes',
        'PrivateKeyPlaintext': b'bytes',
        'PublicKey': b'bytes',
        'KeyId': 'string',
        'KeyPairSpec': 'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'|'ECC_SECG_P256K1'
    }
    
    
    :returns: 
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.DisabledException
    KMS.Client.exceptions.KeyUnavailableException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.InvalidKeyUsageException
    KMS.Client.exceptions.InvalidGrantTokenException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.KMSInvalidStateException
    
    """
    pass

def generate_data_key_pair_without_plaintext(EncryptionContext=None, KeyId=None, KeyPairSpec=None, GrantTokens=None):
    """
    Generates a unique asymmetric data key pair. The GenerateDataKeyPairWithoutPlaintext operation returns a plaintext public key and a copy of the private key that is encrypted under the symmetric CMK you specify. Unlike  GenerateDataKeyPair , this operation does not return a plaintext private key.
    To generate a data key pair, you must specify a symmetric customer master key (CMK) to encrypt the private key in the data key pair. You cannot use an asymmetric CMK. To get the type of your CMK, use the KeySpec field in the  DescribeKey response.
    You can use the public key that GenerateDataKeyPairWithoutPlaintext returns to encrypt data or verify a signature outside of AWS KMS. Then, store the encrypted private key with the data. When you are ready to decrypt data or sign a message, you can use the  Decrypt operation to decrypt the encrypted private key.
    You can use the optional encryption context to add additional security to the encryption operation. If you specify an EncryptionContext , you must specify the same encryption context (a case-sensitive exact match) when decrypting the encrypted data key. Otherwise, the request to decrypt fails with an InvalidCiphertextException. For more information, see Encryption Context in the AWS Key Management Service Developer Guide .
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.generate_data_key_pair_without_plaintext(
        EncryptionContext={
            'string': 'string'
        },
        KeyId='string',
        KeyPairSpec='RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'|'ECC_SECG_P256K1',
        GrantTokens=[
            'string',
        ]
    )
    
    
    :type EncryptionContext: dict
    :param EncryptionContext: Specifies the encryption context that will be used when encrypting the private key in the data key pair.\nAn encryption context is a collection of non-secret key-value pairs that represents additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is optional when encrypting with a symmetric CMK, but it is highly recommended.\nFor more information, see Encryption Context in the AWS Key Management Service Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type KeyId: string
    :param KeyId: [REQUIRED]\nSpecifies the CMK that encrypts the private key in the data key pair. You must specify a symmetric CMK. You cannot use an asymmetric CMK. To get the type of your CMK, use the DescribeKey operation.\nTo specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with 'alias/' .\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\nAlias name: alias/ExampleAlias\nAlias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey . To get the alias name and alias ARN, use ListAliases .\n

    :type KeyPairSpec: string
    :param KeyPairSpec: [REQUIRED]\nDetermines the type of data key pair that is generated.\nThe AWS KMS rule that restricts the use of asymmetric RSA CMKs to encrypt and decrypt or to sign and verify (but not both), and the rule that permits you to use ECC CMKs only to sign and verify, are not effective outside of AWS KMS.\n

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.\nFor more information, see Grant Tokens in the AWS Key Management Service Developer Guide .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PrivateKeyCiphertextBlob': b'bytes',
    'PublicKey': b'bytes',
    'KeyId': 'string',
    'KeyPairSpec': 'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'|'ECC_SECG_P256K1'
}


Response Structure

(dict) --

PrivateKeyCiphertextBlob (bytes) --
The encrypted copy of the private key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.

PublicKey (bytes) --
The public key (in plaintext).

KeyId (string) --
Specifies the CMK that encrypted the private key in the data key pair. You must specify a symmetric CMK. You cannot use an asymmetric CMK. To get the type of your CMK, use the  DescribeKey operation.
To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with "alias/" .
For example:

Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
Alias name: alias/ExampleAlias
Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias

To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .

KeyPairSpec (string) --
The type of data key pair that was generated.







Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.DisabledException
KMS.Client.exceptions.KeyUnavailableException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.InvalidKeyUsageException
KMS.Client.exceptions.InvalidGrantTokenException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException


    :return: {
        'PrivateKeyCiphertextBlob': b'bytes',
        'PublicKey': b'bytes',
        'KeyId': 'string',
        'KeyPairSpec': 'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'|'ECC_SECG_P256K1'
    }
    
    
    :returns: 
    Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
    Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
    Alias name: alias/ExampleAlias
    Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias
    
    """
    pass

def generate_data_key_without_plaintext(KeyId=None, EncryptionContext=None, KeySpec=None, NumberOfBytes=None, GrantTokens=None):
    """
    Generates a unique symmetric data key. This operation returns a data key that is encrypted under a customer master key (CMK) that you specify. To request an asymmetric data key pair, use the  GenerateDataKeyPair or  GenerateDataKeyPairWithoutPlaintext operations.
    It\'s also useful in distributed systems with different levels of trust. For example, you might store encrypted data in containers. One component of your system creates new containers and stores an encrypted data key with each container. Then, a different component puts the data into the containers. That component first decrypts the data key, uses the plaintext data key to encrypt data, puts the encrypted data into the container, and then destroys the plaintext data key. In this system, the component that creates the containers never sees the plaintext data key.
    To generate a data key, you must specify the symmetric customer master key (CMK) that is used to encrypt the data key. You cannot use an asymmetric CMK to generate a data key. To get the type of your CMK, use the  DescribeKey operation.
    If the operation succeeds, you will find the encrypted copy of the data key in the CiphertextBlob field.
    You can use the optional encryption context to add additional security to the encryption operation. If you specify an EncryptionContext , you must specify the same encryption context (a case-sensitive exact match) when decrypting the encrypted data key. Otherwise, the request to decrypt fails with an InvalidCiphertextException. For more information, see Encryption Context in the AWS Key Management Service Developer Guide .
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example generates an encrypted copy of a 256-bit symmetric data encryption key (data key). The data key is encrypted with the specified customer master key (CMK).
    Expected Output:
    
    :example: response = client.generate_data_key_without_plaintext(
        KeyId='string',
        EncryptionContext={
            'string': 'string'
        },
        KeySpec='AES_256'|'AES_128',
        NumberOfBytes=123,
        GrantTokens=[
            'string',
        ]
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nThe identifier of the symmetric customer master key (CMK) that encrypts the data key.\nTo specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with 'alias/' . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\nAlias name: alias/ExampleAlias\nAlias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey . To get the alias name and alias ARN, use ListAliases .\n

    :type EncryptionContext: dict
    :param EncryptionContext: Specifies the encryption context that will be used when encrypting the data key.\nAn encryption context is a collection of non-secret key-value pairs that represents additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is optional when encrypting with a symmetric CMK, but it is highly recommended.\nFor more information, see Encryption Context in the AWS Key Management Service Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type KeySpec: string
    :param KeySpec: The length of the data key. Use AES_128 to generate a 128-bit symmetric key, or AES_256 to generate a 256-bit symmetric key.

    :type NumberOfBytes: integer
    :param NumberOfBytes: The length of the data key in bytes. For example, use the value 64 to generate a 512-bit data key (64 bytes is 512 bits). For common key lengths (128-bit and 256-bit symmetric keys), we recommend that you use the KeySpec field instead of this one.

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.\nFor more information, see Grant Tokens in the AWS Key Management Service Developer Guide .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CiphertextBlob': b'bytes',
    'KeyId': 'string'
}


Response Structure

(dict) --

CiphertextBlob (bytes) --
The encrypted data key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.

KeyId (string) --
The identifier of the CMK that encrypted the data key.







Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.DisabledException
KMS.Client.exceptions.KeyUnavailableException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.InvalidKeyUsageException
KMS.Client.exceptions.InvalidGrantTokenException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException

Examples
The following example generates an encrypted copy of a 256-bit symmetric data encryption key (data key). The data key is encrypted with the specified customer master key (CMK).
response = client.generate_data_key_without_plaintext(
    # The identifier of the CMK to use to encrypt the data key. You can use the key ID or Amazon Resource Name (ARN) of the CMK, or the name or ARN of an alias that refers to the CMK.
    KeyId='alias/ExampleAlias',
    # Specifies the type of data key to return.
    KeySpec='AES_256',
)

print(response)


Expected Output:
{
    # The encrypted data key.
    'CiphertextBlob': '<binary data>',
    # The ARN of the CMK that was used to encrypt the data key.
    'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CiphertextBlob': b'bytes',
        'KeyId': 'string'
    }
    
    
    :returns: 
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.DisabledException
    KMS.Client.exceptions.KeyUnavailableException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.InvalidKeyUsageException
    KMS.Client.exceptions.InvalidGrantTokenException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.KMSInvalidStateException
    
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

def generate_random(NumberOfBytes=None, CustomKeyStoreId=None):
    """
    Returns a random byte string that is cryptographically secure.
    By default, the random byte string is generated in AWS KMS. To generate the byte string in the AWS CloudHSM cluster that is associated with a custom key store , specify the custom key store ID.
    For more information about entropy and random number generation, see the AWS Key Management Service Cryptographic Details whitepaper.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example uses AWS KMS to generate 32 bytes of random data.
    Expected Output:
    
    :example: response = client.generate_random(
        NumberOfBytes=123,
        CustomKeyStoreId='string'
    )
    
    
    :type NumberOfBytes: integer
    :param NumberOfBytes: The length of the byte string.

    :type CustomKeyStoreId: string
    :param CustomKeyStoreId: Generates the random byte string in the AWS CloudHSM cluster that is associated with the specified custom key store . To find the ID of a custom key store, use the DescribeCustomKeyStores operation.

    :rtype: dict

ReturnsResponse Syntax
{
    'Plaintext': b'bytes'
}


Response Structure

(dict) --

Plaintext (bytes) --
The random byte string. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.







Exceptions

KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.CustomKeyStoreNotFoundException
KMS.Client.exceptions.CustomKeyStoreInvalidStateException

Examples
The following example uses AWS KMS to generate 32 bytes of random data.
response = client.generate_random(
    # The length of the random data, specified in number of bytes.
    NumberOfBytes=32,
)

print(response)


Expected Output:
{
    # The random data.
    'Plaintext': '<binary data>',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Plaintext': b'bytes'
    }
    
    
    :returns: 
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.CustomKeyStoreNotFoundException
    KMS.Client.exceptions.CustomKeyStoreInvalidStateException
    
    """
    pass

def get_key_policy(KeyId=None, PolicyName=None):
    """
    Gets a key policy attached to the specified customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example retrieves the key policy for the specified customer master key (CMK).
    Expected Output:
    
    :example: response = client.get_key_policy(
        KeyId='string',
        PolicyName='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nA unique identifier for the customer master key (CMK).\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nSpecifies the name of the key policy. The only valid name is default . To get the names of key policies, use ListKeyPolicies .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Policy': 'string'
}


Response Structure

(dict) --

Policy (string) --
A key policy document in JSON format.







Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException

Examples
The following example retrieves the key policy for the specified customer master key (CMK).
response = client.get_key_policy(
    # The identifier of the CMK whose key policy you want to retrieve. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
    KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
    # The name of the key policy to retrieve.
    PolicyName='default',
)

print(response)


Expected Output:
{
    # The key policy document.
    'Policy': '{\
  "Version" : "2012-10-17",\
  "Id" : "key-default-1",\
  "Statement" : [ {\
    "Sid" : "Enable IAM User Permissions",\
    "Effect" : "Allow",\
    "Principal" : {\
      "AWS" : "arn:aws:iam::111122223333:root"\
    },\
    "Action" : "kms:*",\
    "Resource" : "*"\
  } ]\
}',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Policy': 'string'
    }
    
    
    :returns: 
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.KMSInvalidStateException
    
    """
    pass

def get_key_rotation_status(KeyId=None):
    """
    Gets a Boolean value that indicates whether automatic rotation of the key material is enabled for the specified customer master key (CMK).
    You cannot enable automatic rotation of asymmetric CMKs, CMKs with imported key material, or CMKs in a custom key store . The key rotation status for these CMKs is always false .
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the KeyId parameter.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example retrieves the status of automatic annual rotation of the key material for the specified CMK.
    Expected Output:
    
    :example: response = client.get_key_rotation_status(
        KeyId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nA unique identifier for the customer master key (CMK).\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :rtype: dict
ReturnsResponse Syntax{
    'KeyRotationEnabled': True|False
}


Response Structure

(dict) --
KeyRotationEnabled (boolean) --A Boolean value that specifies whether key rotation is enabled.






Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException
KMS.Client.exceptions.UnsupportedOperationException

Examples
The following example retrieves the status of automatic annual rotation of the key material for the specified CMK.
response = client.get_key_rotation_status(
    # The identifier of the CMK whose key material rotation status you want to retrieve. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
    KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
)

print(response)


Expected Output:
{
    # A boolean that indicates the key material rotation status. Returns true when automatic annual rotation of the key material is enabled, or false when it is not.
    'KeyRotationEnabled': True,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'KeyRotationEnabled': True|False
    }
    
    
    :returns: 
    Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
    Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
    
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

def get_parameters_for_import(KeyId=None, WrappingAlgorithm=None, WrappingKeySpec=None):
    """
    Returns the items you need to import key material into a symmetric, customer managed customer master key (CMK). For more information about importing key material into AWS KMS, see Importing Key Material in the AWS Key Management Service Developer Guide .
    This operation returns a public key and an import token. Use the public key to encrypt the symmetric key material. Store the import token to send with a subsequent  ImportKeyMaterial request.
    You must specify the key ID of the symmetric CMK into which you will import key material. This CMK\'s Origin must be EXTERNAL . You must also specify the wrapping algorithm and type of wrapping key (public key) that you will use to encrypt the key material. You cannot perform this operation on an asymmetric CMK or on any CMK in a different AWS account.
    To import key material, you must use the public key and import token from the same response. These items are valid for 24 hours. The expiration date and time appear in the GetParametersForImport response. You cannot use an expired token in an  ImportKeyMaterial request. If your key and token expire, send another GetParametersForImport request.
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example retrieves the public key and import token for the specified CMK.
    Expected Output:
    
    :example: response = client.get_parameters_for_import(
        KeyId='string',
        WrappingAlgorithm='RSAES_PKCS1_V1_5'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
        WrappingKeySpec='RSA_2048'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nThe identifier of the symmetric CMK into which you will import key material. The Origin of the CMK must be EXTERNAL .\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :type WrappingAlgorithm: string
    :param WrappingAlgorithm: [REQUIRED]\nThe algorithm you will use to encrypt the key material before importing it with ImportKeyMaterial . For more information, see Encrypt the Key Material in the AWS Key Management Service Developer Guide .\n

    :type WrappingKeySpec: string
    :param WrappingKeySpec: [REQUIRED]\nThe type of wrapping key (public key) to return in the response. Only 2048-bit RSA public keys are supported.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'KeyId': 'string',
    'ImportToken': b'bytes',
    'PublicKey': b'bytes',
    'ParametersValidTo': datetime(2015, 1, 1)
}


Response Structure

(dict) --

KeyId (string) --
The identifier of the CMK to use in a subsequent  ImportKeyMaterial request. This is the same CMK specified in the GetParametersForImport request.

ImportToken (bytes) --
The import token to send in a subsequent  ImportKeyMaterial request.

PublicKey (bytes) --
The public key to use to encrypt the key material before importing it with  ImportKeyMaterial .

ParametersValidTo (datetime) --
The time at which the import token and public key are no longer valid. After this time, you cannot use them to make an  ImportKeyMaterial request and you must send another GetParametersForImport request to get new ones.







Exceptions

KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.UnsupportedOperationException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException

Examples
The following example retrieves the public key and import token for the specified CMK.
response = client.get_parameters_for_import(
    # The identifier of the CMK for which to retrieve the public key and import token. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
    KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
    # The algorithm that you will use to encrypt the key material before importing it.
    WrappingAlgorithm='RSAES_OAEP_SHA_1',
    # The type of wrapping key (public key) to return in the response.
    WrappingKeySpec='RSA_2048',
)

print(response)


Expected Output:
{
    # The import token to send with a subsequent ImportKeyMaterial request.
    'ImportToken': '<binary data>',
    # The ARN of the CMK for which you are retrieving the public key and import token. This is the same CMK specified in the request.
    'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
    # The time at which the import token and public key are no longer valid.
    'ParametersValidTo': datetime(2016, 12, 1, 14, 52, 17, 3, 336, 0),
    # The public key to use to encrypt the key material before importing it.
    'PublicKey': '<binary data>',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'KeyId': 'string',
        'ImportToken': b'bytes',
        'PublicKey': b'bytes',
        'ParametersValidTo': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.UnsupportedOperationException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.KMSInvalidStateException
    
    """
    pass

def get_public_key(KeyId=None, GrantTokens=None):
    """
    Returns the public key of an asymmetric CMK. Unlike the private key of a asymmetric CMK, which never leaves AWS KMS unencrypted, callers with kms:GetPublicKey permission can download the public key of an asymmetric CMK. You can share the public key to allow others to encrypt messages and verify signatures outside of AWS KMS. For information about symmetric and asymmetric CMKs, see Using Symmetric and Asymmetric CMKs in the AWS Key Management Service Developer Guide .
    You do not need to download the public key. Instead, you can use the public key within AWS KMS by calling the  Encrypt ,  ReEncrypt , or  Verify operations with the identifier of an asymmetric CMK. When you use the public key within AWS KMS, you benefit from the authentication, authorization, and logging that are part of every AWS KMS operation. You also reduce of risk of encrypting data that cannot be decrypted. These features are not effective outside of AWS KMS. For details, see Special Considerations for Downloading Public Keys .
    To help you use the public key safely outside of AWS KMS, GetPublicKey returns important information about the public key in the response, including:
    Although AWS KMS cannot enforce these restrictions on external operations, it is crucial that you use this information to prevent the public key from being used improperly. For example, you can prevent a public signing key from being used encrypt data, or prevent a public key from being used with an encryption algorithm that is not supported by AWS KMS. You can also avoid errors, such as using the wrong signing algorithm in a verification operation.
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_public_key(
        KeyId='string',
        GrantTokens=[
            'string',
        ]
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nIdentifies the asymmetric CMK that includes the public key.\nTo specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with 'alias/' . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\nAlias name: alias/ExampleAlias\nAlias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey . To get the alias name and alias ARN, use ListAliases .\n

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.\nFor more information, see Grant Tokens in the AWS Key Management Service Developer Guide .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'KeyId': 'string',
    'PublicKey': b'bytes',
    'CustomerMasterKeySpec': 'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'|'ECC_SECG_P256K1'|'SYMMETRIC_DEFAULT',
    'KeyUsage': 'SIGN_VERIFY'|'ENCRYPT_DECRYPT',
    'EncryptionAlgorithms': [
        'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
    ],
    'SigningAlgorithms': [
        'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'|'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'|'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512',
    ]
}


Response Structure

(dict) --

KeyId (string) --
The identifier of the asymmetric CMK from which the public key was downloaded.

PublicKey (bytes) --
The exported public key.
The value is a DER-encoded X.509 public key, also known as SubjectPublicKeyInfo (SPKI), as defined in RFC 5280 . When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.

CustomerMasterKeySpec (string) --
The type of the of the public key that was downloaded.

KeyUsage (string) --
The permitted use of the public key. Valid values are ENCRYPT_DECRYPT or SIGN_VERIFY .
This information is critical. If a public key with SIGN_VERIFY key usage encrypts data outside of AWS KMS, the ciphertext cannot be decrypted.

EncryptionAlgorithms (list) --
The encryption algorithms that AWS KMS supports for this key.
This information is critical. If a public key encrypts data outside of AWS KMS by using an unsupported encryption algorithm, the ciphertext cannot be decrypted.
This field appears in the response only when the KeyUsage of the public key is ENCRYPT_DECRYPT .

(string) --


SigningAlgorithms (list) --
The signing algorithms that AWS KMS supports for this key.
This field appears in the response only when the KeyUsage of the public key is SIGN_VERIFY .

(string) --








Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.DisabledException
KMS.Client.exceptions.KeyUnavailableException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.UnsupportedOperationException
KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.InvalidGrantTokenException
KMS.Client.exceptions.InvalidKeyUsageException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException


    :return: {
        'KeyId': 'string',
        'PublicKey': b'bytes',
        'CustomerMasterKeySpec': 'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'|'ECC_SECG_P256K1'|'SYMMETRIC_DEFAULT',
        'KeyUsage': 'SIGN_VERIFY'|'ENCRYPT_DECRYPT',
        'EncryptionAlgorithms': [
            'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
        ],
        'SigningAlgorithms': [
            'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'|'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'|'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512',
        ]
    }
    
    
    :returns: 
    KeyId (string) -- [REQUIRED]
    Identifies the asymmetric CMK that includes the public key.
    To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with "alias/" . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.
    For example:
    
    Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
    Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
    Alias name: alias/ExampleAlias
    Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias
    
    To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .
    
    GrantTokens (list) -- A list of grant tokens.
    For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
    
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

def import_key_material(KeyId=None, ImportToken=None, EncryptedKeyMaterial=None, ValidTo=None, ExpirationModel=None):
    """
    Imports key material into an existing symmetric AWS KMS customer master key (CMK) that was created without key material. After you successfully import key material into a CMK, you can reimport the same key material into that CMK, but you cannot import different key material.
    You cannot perform this operation on an asymmetric CMK or on any CMK in a different AWS account. For more information about creating CMKs with no key material and then importing key material, see Importing Key Material in the AWS Key Management Service Developer Guide .
    Before using this operation, call  GetParametersForImport . Its response includes a public key and an import token. Use the public key to encrypt the key material. Then, submit the import token from the same GetParametersForImport response.
    When calling this operation, you must specify the following values:
    When this operation is successful, the key state of the CMK changes from PendingImport to Enabled , and you can use the CMK.
    If this operation fails, use the exception to help determine the problem. If the error is related to the key material, the import token, or wrapping key, use  GetParametersForImport to get a new public key and import token for the CMK and repeat the import procedure. For help, see How To Import Key Material in the AWS Key Management Service Developer Guide .
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example imports key material into the specified CMK.
    Expected Output:
    
    :example: response = client.import_key_material(
        KeyId='string',
        ImportToken=b'bytes',
        EncryptedKeyMaterial=b'bytes',
        ValidTo=datetime(2015, 1, 1),
        ExpirationModel='KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nThe identifier of the symmetric CMK that receives the imported key material. The CMK\'s Origin must be EXTERNAL . This must be the same CMK specified in the KeyID parameter of the corresponding GetParametersForImport request.\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :type ImportToken: bytes
    :param ImportToken: [REQUIRED]\nThe import token that you received in the response to a previous GetParametersForImport request. It must be from the same response that contained the public key that you used to encrypt the key material.\n

    :type EncryptedKeyMaterial: bytes
    :param EncryptedKeyMaterial: [REQUIRED]\nThe encrypted key material to import. The key material must be encrypted with the public wrapping key that GetParametersForImport returned, using the wrapping algorithm that you specified in the same GetParametersForImport request.\n

    :type ValidTo: datetime
    :param ValidTo: The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. You must omit this parameter when the ExpirationModel parameter is set to KEY_MATERIAL_DOES_NOT_EXPIRE . Otherwise it is required.

    :type ExpirationModel: string
    :param ExpirationModel: Specifies whether the key material expires. The default is KEY_MATERIAL_EXPIRES , in which case you must include the ValidTo parameter. When this parameter is set to KEY_MATERIAL_DOES_NOT_EXPIRE , you must omit the ValidTo parameter.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.UnsupportedOperationException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException
KMS.Client.exceptions.InvalidCiphertextException
KMS.Client.exceptions.IncorrectKeyMaterialException
KMS.Client.exceptions.ExpiredImportTokenException
KMS.Client.exceptions.InvalidImportTokenException

Examples
The following example imports key material into the specified CMK.
response = client.import_key_material(
    # The encrypted key material to import.
    EncryptedKeyMaterial='<binary data>',
    # A value that specifies whether the key material expires.
    ExpirationModel='KEY_MATERIAL_DOES_NOT_EXPIRE',
    # The import token that you received in the response to a previous GetParametersForImport request.
    ImportToken='<binary data>',
    # The identifier of the CMK to import the key material into. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
    KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    KeyId (string) -- [REQUIRED]
    The identifier of the symmetric CMK that receives the imported key material. The CMK\'s Origin must be EXTERNAL . This must be the same CMK specified in the KeyID parameter of the corresponding  GetParametersForImport request.
    Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
    For example:
    
    Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
    Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
    
    To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
    
    ImportToken (bytes) -- [REQUIRED]
    The import token that you received in the response to a previous  GetParametersForImport request. It must be from the same response that contained the public key that you used to encrypt the key material.
    
    EncryptedKeyMaterial (bytes) -- [REQUIRED]
    The encrypted key material to import. The key material must be encrypted with the public wrapping key that  GetParametersForImport returned, using the wrapping algorithm that you specified in the same GetParametersForImport request.
    
    ValidTo (datetime) -- The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. You must omit this parameter when the ExpirationModel parameter is set to KEY_MATERIAL_DOES_NOT_EXPIRE . Otherwise it is required.
    ExpirationModel (string) -- Specifies whether the key material expires. The default is KEY_MATERIAL_EXPIRES , in which case you must include the ValidTo parameter. When this parameter is set to KEY_MATERIAL_DOES_NOT_EXPIRE , you must omit the ValidTo parameter.
    
    """
    pass

def list_aliases(KeyId=None, Limit=None, Marker=None):
    """
    Gets a list of aliases in the caller\'s AWS account and region. You cannot list aliases in other accounts. For more information about aliases, see  CreateAlias .
    By default, the ListAliases command returns all aliases in the account and region. To get only the aliases that point to a particular customer master key (CMK), use the KeyId parameter.
    The ListAliases response can include aliases that you created and associated with your customer managed CMKs, and aliases that AWS created and associated with AWS managed CMKs in your account. You can recognize AWS aliases because their names have the format aws/<service-name> , such as aws/dynamodb .
    The response might also include aliases that have no TargetKeyId field. These are predefined aliases that AWS has created but has not yet associated with a CMK. Aliases that AWS creates in your account, including predefined aliases, do not count against your AWS KMS aliases quota .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example lists aliases.
    Expected Output:
    
    :example: response = client.list_aliases(
        KeyId='string',
        Limit=123,
        Marker='string'
    )
    
    
    :type KeyId: string
    :param KeyId: Lists only aliases that refer to the specified CMK. The value of this parameter can be the ID or Amazon Resource Name (ARN) of a CMK in the caller\'s account and region. You cannot use an alias name or alias ARN in this value.\nThis parameter is optional. If you omit it, ListAliases returns all aliases in the account and region.\n

    :type Limit: integer
    :param Limit: Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.\nThis value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.\n

    :type Marker: string
    :param Marker: Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the truncated response you just received.

    :rtype: dict

ReturnsResponse Syntax
{
    'Aliases': [
        {
            'AliasName': 'string',
            'AliasArn': 'string',
            'TargetKeyId': 'string'
        },
    ],
    'NextMarker': 'string',
    'Truncated': True|False
}


Response Structure

(dict) --

Aliases (list) --
A list of aliases.

(dict) --
Contains information about an alias.

AliasName (string) --
String that contains the alias. This value begins with alias/ .

AliasArn (string) --
String that contains the key ARN.

TargetKeyId (string) --
String that contains the key identifier referred to by the alias.





NextMarker (string) --
When Truncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent request.

Truncated (boolean) --
A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the NextMarker element in thisresponse to the Marker parameter in a subsequent request.







Exceptions

KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.InvalidMarkerException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.NotFoundException

Examples
The following example lists aliases.
response = client.list_aliases(
)

print(response)


Expected Output:
{
    # A list of aliases, including the key ID of the customer master key (CMK) that each alias refers to.
    'Aliases': [
        {
            'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/aws/acm',
            'AliasName': 'alias/aws/acm',
            'TargetKeyId': 'da03f6f7-d279-427a-9cae-de48d07e5b66',
        },
        {
            'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/aws/ebs',
            'AliasName': 'alias/aws/ebs',
            'TargetKeyId': '25a217e7-7170-4b8c-8bf6-045ea5f70e5b',
        },
        {
            'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/aws/rds',
            'AliasName': 'alias/aws/rds',
            'TargetKeyId': '7ec3104e-c3f2-4b5c-bf42-bfc4772c6685',
        },
        {
            'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/aws/redshift',
            'AliasName': 'alias/aws/redshift',
            'TargetKeyId': '08f7a25a-69e2-4fb5-8f10-393db27326fa',
        },
        {
            'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/aws/s3',
            'AliasName': 'alias/aws/s3',
            'TargetKeyId': 'd2b0f1a3-580d-4f79-b836-bc983be8cfa5',
        },
        {
            'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/example1',
            'AliasName': 'alias/example1',
            'TargetKeyId': '4da1e216-62d0-46c5-a7c0-5f3a3d2f8046',
        },
        {
            'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/example2',
            'AliasName': 'alias/example2',
            'TargetKeyId': 'f32fef59-2cc2-445b-8573-2d73328acbee',
        },
        {
            'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/example3',
            'AliasName': 'alias/example3',
            'TargetKeyId': '1374ef38-d34e-4d5f-b2c9-4e0daee38855',
        },
    ],
    # A boolean that indicates whether there are more items in the list. Returns true when there are more items, or false when there are not.
    'Truncated': False,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Aliases': [
            {
                'AliasName': 'string',
                'AliasArn': 'string',
                'TargetKeyId': 'string'
            },
        ],
        'NextMarker': 'string',
        'Truncated': True|False
    }
    
    
    :returns: 
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.InvalidMarkerException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.NotFoundException
    
    """
    pass

def list_grants(Limit=None, Marker=None, KeyId=None):
    """
    Gets a list of all grants for the specified customer master key (CMK).
    To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the KeyId parameter.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example lists grants for the specified CMK.
    Expected Output:
    
    :example: response = client.list_grants(
        Limit=123,
        Marker='string',
        KeyId='string'
    )
    
    
    :type Limit: integer
    :param Limit: Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.\nThis value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.\n

    :type Marker: string
    :param Marker: Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the truncated response you just received.

    :type KeyId: string
    :param KeyId: [REQUIRED]\nA unique identifier for the customer master key (CMK).\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Grants': [
        {
            'KeyId': 'string',
            'GrantId': 'string',
            'Name': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'GranteePrincipal': 'string',
            'RetiringPrincipal': 'string',
            'IssuingAccount': 'string',
            'Operations': [
                'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'Sign'|'Verify'|'GetPublicKey'|'CreateGrant'|'RetireGrant'|'DescribeKey'|'GenerateDataKeyPair'|'GenerateDataKeyPairWithoutPlaintext',
            ],
            'Constraints': {
                'EncryptionContextSubset': {
                    'string': 'string'
                },
                'EncryptionContextEquals': {
                    'string': 'string'
                }
            }
        },
    ],
    'NextMarker': 'string',
    'Truncated': True|False
}


Response Structure

(dict) --

Grants (list) --
A list of grants.

(dict) --
Contains information about an entry in a list of grants.

KeyId (string) --
The unique identifier for the customer master key (CMK) to which the grant applies.

GrantId (string) --
The unique identifier for the grant.

Name (string) --
The friendly name that identifies the grant. If a name was provided in the  CreateGrant request, that name is returned. Otherwise this value is null.

CreationDate (datetime) --
The date and time when the grant was created.

GranteePrincipal (string) --
The principal that receives the grant\'s permissions.

RetiringPrincipal (string) --
The principal that can retire the grant.

IssuingAccount (string) --
The AWS account under which the grant was issued.

Operations (list) --
The list of operations permitted by the grant.

(string) --


Constraints (dict) --
A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows.

EncryptionContextSubset (dict) --
A list of key-value pairs that must be included in the encryption context of the cryptographic operation request. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs.

(string) --
(string) --




EncryptionContextEquals (dict) --
A list of key-value pairs that must match the encryption context in the cryptographic operation request. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint.

(string) --
(string) --










NextMarker (string) --
When Truncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent request.

Truncated (boolean) --
A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the NextMarker element in thisresponse to the Marker parameter in a subsequent request.







Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.InvalidMarkerException
KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException

Examples
The following example lists grants for the specified CMK.
response = client.list_grants(
    # The identifier of the CMK whose grants you want to list. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
    KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
)

print(response)


Expected Output:
{
    # A list of grants.
    'Grants': [
        {
            'CreationDate': datetime(2016, 10, 25, 14, 37, 41, 1, 299, 0),
            'GrantId': '91ad875e49b04a9d1f3bdeb84d821f9db6ea95e1098813f6d47f0c65fbe2a172',
            'GranteePrincipal': 'acm.us-east-2.amazonaws.com',
            'IssuingAccount': 'arn:aws:iam::111122223333:root',
            'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
            'Operations': [
                'Encrypt',
                'ReEncryptFrom',
                'ReEncryptTo',
            ],
            'RetiringPrincipal': 'acm.us-east-2.amazonaws.com',
        },
        {
            'CreationDate': datetime(2016, 10, 25, 14, 37, 41, 1, 299, 0),
            'GrantId': 'a5d67d3e207a8fc1f4928749ee3e52eb0440493a8b9cf05bbfad91655b056200',
            'GranteePrincipal': 'acm.us-east-2.amazonaws.com',
            'IssuingAccount': 'arn:aws:iam::111122223333:root',
            'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
            'Operations': [
                'ReEncryptFrom',
                'ReEncryptTo',
            ],
            'RetiringPrincipal': 'acm.us-east-2.amazonaws.com',
        },
        {
            'CreationDate': datetime(2016, 10, 25, 14, 37, 41, 1, 299, 0),
            'GrantId': 'c541aaf05d90cb78846a73b346fc43e65be28b7163129488c738e0c9e0628f4f',
            'GranteePrincipal': 'acm.us-east-2.amazonaws.com',
            'IssuingAccount': 'arn:aws:iam::111122223333:root',
            'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
            'Operations': [
                'Encrypt',
                'ReEncryptFrom',
                'ReEncryptTo',
            ],
            'RetiringPrincipal': 'acm.us-east-2.amazonaws.com',
        },
        {
            'CreationDate': datetime(2016, 10, 25, 14, 37, 41, 1, 299, 0),
            'GrantId': 'dd2052c67b4c76ee45caf1dc6a1e2d24e8dc744a51b36ae2f067dc540ce0105c',
            'GranteePrincipal': 'acm.us-east-2.amazonaws.com',
            'IssuingAccount': 'arn:aws:iam::111122223333:root',
            'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
            'Operations': [
                'Encrypt',
                'ReEncryptFrom',
                'ReEncryptTo',
            ],
            'RetiringPrincipal': 'acm.us-east-2.amazonaws.com',
        },
    ],
    # A boolean that indicates whether there are more items in the list. Returns true when there are more items, or false when there are not.
    'Truncated': True,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Grants': [
            {
                'KeyId': 'string',
                'GrantId': 'string',
                'Name': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'GranteePrincipal': 'string',
                'RetiringPrincipal': 'string',
                'IssuingAccount': 'string',
                'Operations': [
                    'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'Sign'|'Verify'|'GetPublicKey'|'CreateGrant'|'RetireGrant'|'DescribeKey'|'GenerateDataKeyPair'|'GenerateDataKeyPairWithoutPlaintext',
                ],
                'Constraints': {
                    'EncryptionContextSubset': {
                        'string': 'string'
                    },
                    'EncryptionContextEquals': {
                        'string': 'string'
                    }
                }
            },
        ],
        'NextMarker': 'string',
        'Truncated': True|False
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_key_policies(KeyId=None, Limit=None, Marker=None):
    """
    Gets the names of the key policies that are attached to a customer master key (CMK). This operation is designed to get policy names that you can use in a  GetKeyPolicy operation. However, the only valid policy name is default . You cannot perform this operation on a CMK in a different AWS account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example lists key policies for the specified CMK.
    Expected Output:
    
    :example: response = client.list_key_policies(
        KeyId='string',
        Limit=123,
        Marker='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nA unique identifier for the customer master key (CMK).\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :type Limit: integer
    :param Limit: Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.\nThis value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.\nOnly one policy can be attached to a key.\n

    :type Marker: string
    :param Marker: Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the truncated response you just received.

    :rtype: dict

ReturnsResponse Syntax
{
    'PolicyNames': [
        'string',
    ],
    'NextMarker': 'string',
    'Truncated': True|False
}


Response Structure

(dict) --

PolicyNames (list) --
A list of key policy names. The only valid value is default .

(string) --


NextMarker (string) --
When Truncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent request.

Truncated (boolean) --
A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the NextMarker element in thisresponse to the Marker parameter in a subsequent request.







Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException

Examples
The following example lists key policies for the specified CMK.
response = client.list_key_policies(
    # The identifier of the CMK whose key policies you want to list. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
    KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
)

print(response)


Expected Output:
{
    # A list of key policy names.
    'PolicyNames': [
        'default',
    ],
    # A boolean that indicates whether there are more items in the list. Returns true when there are more items, or false when there are not.
    'Truncated': False,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'PolicyNames': [
            'string',
        ],
        'NextMarker': 'string',
        'Truncated': True|False
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_keys(Limit=None, Marker=None):
    """
    Gets a list of all customer master keys (CMKs) in the caller\'s AWS account and Region.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example lists CMKs.
    Expected Output:
    
    :example: response = client.list_keys(
        Limit=123,
        Marker='string'
    )
    
    
    :type Limit: integer
    :param Limit: Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.\nThis value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.\n

    :type Marker: string
    :param Marker: Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the truncated response you just received.

    :rtype: dict

ReturnsResponse Syntax
{
    'Keys': [
        {
            'KeyId': 'string',
            'KeyArn': 'string'
        },
    ],
    'NextMarker': 'string',
    'Truncated': True|False
}


Response Structure

(dict) --

Keys (list) --
A list of customer master keys (CMKs).

(dict) --
Contains information about each entry in the key list.

KeyId (string) --
Unique identifier of the key.

KeyArn (string) --
ARN of the key.





NextMarker (string) --
When Truncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent request.

Truncated (boolean) --
A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the NextMarker element in thisresponse to the Marker parameter in a subsequent request.







Exceptions

KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.InvalidMarkerException

Examples
The following example lists CMKs.
response = client.list_keys(
)

print(response)


Expected Output:
{
    # A list of CMKs, including the key ID and Amazon Resource Name (ARN) of each one.
    'Keys': [
        {
            'KeyArn': 'arn:aws:kms:us-east-2:111122223333:key/0d990263-018e-4e65-a703-eff731de951e',
            'KeyId': '0d990263-018e-4e65-a703-eff731de951e',
        },
        {
            'KeyArn': 'arn:aws:kms:us-east-2:111122223333:key/144be297-0ae1-44ac-9c8f-93cd8c82f841',
            'KeyId': '144be297-0ae1-44ac-9c8f-93cd8c82f841',
        },
        {
            'KeyArn': 'arn:aws:kms:us-east-2:111122223333:key/21184251-b765-428e-b852-2c7353e72571',
            'KeyId': '21184251-b765-428e-b852-2c7353e72571',
        },
        {
            'KeyArn': 'arn:aws:kms:us-east-2:111122223333:key/214fe92f-5b03-4ae1-b350-db2a45dbe10c',
            'KeyId': '214fe92f-5b03-4ae1-b350-db2a45dbe10c',
        },
        {
            'KeyArn': 'arn:aws:kms:us-east-2:111122223333:key/339963f2-e523-49d3-af24-a0fe752aa458',
            'KeyId': '339963f2-e523-49d3-af24-a0fe752aa458',
        },
        {
            'KeyArn': 'arn:aws:kms:us-east-2:111122223333:key/b776a44b-df37-4438-9be4-a27494e4271a',
            'KeyId': 'b776a44b-df37-4438-9be4-a27494e4271a',
        },
        {
            'KeyArn': 'arn:aws:kms:us-east-2:111122223333:key/deaf6c9e-cf2c-46a6-bf6d-0b6d487cffbb',
            'KeyId': 'deaf6c9e-cf2c-46a6-bf6d-0b6d487cffbb',
        },
    ],
    # A boolean that indicates whether there are more items in the list. Returns true when there are more items, or false when there are not.
    'Truncated': False,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Keys': [
            {
                'KeyId': 'string',
                'KeyArn': 'string'
            },
        ],
        'NextMarker': 'string',
        'Truncated': True|False
    }
    
    
    :returns: 
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.InvalidMarkerException
    
    """
    pass

def list_resource_tags(KeyId=None, Limit=None, Marker=None):
    """
    Returns a list of all tags for the specified customer master key (CMK).
    You cannot perform this operation on a CMK in a different AWS account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example lists tags for a CMK.
    Expected Output:
    
    :example: response = client.list_resource_tags(
        KeyId='string',
        Limit=123,
        Marker='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nA unique identifier for the customer master key (CMK).\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :type Limit: integer
    :param Limit: Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.\nThis value is optional. If you include a value, it must be between 1 and 50, inclusive. If you do not include a value, it defaults to 50.\n

    :type Marker: string
    :param Marker: Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the truncated response you just received.\nDo not attempt to construct this value. Use only the value of NextMarker from the truncated response you just received.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'TagKey': 'string',
            'TagValue': 'string'
        },
    ],
    'NextMarker': 'string',
    'Truncated': True|False
}


Response Structure

(dict) --

Tags (list) --
A list of tags. Each tag consists of a tag key and a tag value.

(dict) --
A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.
For information about the rules that apply to tag keys and tag values, see User-Defined Tag Restrictions in the AWS Billing and Cost Management User Guide .

TagKey (string) --
The key of the tag.

TagValue (string) --
The value of the tag.





NextMarker (string) --
When Truncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent request.
Do not assume or infer any information from this value.

Truncated (boolean) --
A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the NextMarker element in thisresponse to the Marker parameter in a subsequent request.







Exceptions

KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.InvalidMarkerException

Examples
The following example lists tags for a CMK.
response = client.list_resource_tags(
    # The identifier of the CMK whose tags you are listing. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
    KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
)

print(response)


Expected Output:
{
    # A list of tags.
    'Tags': [
        {
            'TagKey': 'CostCenter',
            'TagValue': '87654',
        },
        {
            'TagKey': 'CreatedBy',
            'TagValue': 'ExampleUser',
        },
        {
            'TagKey': 'Purpose',
            'TagValue': 'Test',
        },
    ],
    # A boolean that indicates whether there are more items in the list. Returns true when there are more items, or false when there are not.
    'Truncated': False,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Tags': [
            {
                'TagKey': 'string',
                'TagValue': 'string'
            },
        ],
        'NextMarker': 'string',
        'Truncated': True|False
    }
    
    
    :returns: 
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.InvalidMarkerException
    
    """
    pass

def list_retirable_grants(Limit=None, Marker=None, RetiringPrincipal=None):
    """
    Returns a list of all grants for which the grant\'s RetiringPrincipal matches the one specified.
    A typical use is to list all grants that you are able to retire. To retire a grant, use  RetireGrant .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example lists the grants that the specified principal (identity) can retire.
    Expected Output:
    
    :example: response = client.list_retirable_grants(
        Limit=123,
        Marker='string',
        RetiringPrincipal='string'
    )
    
    
    :type Limit: integer
    :param Limit: Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.\nThis value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.\n

    :type Marker: string
    :param Marker: Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the truncated response you just received.

    :type RetiringPrincipal: string
    :param RetiringPrincipal: [REQUIRED]\nThe retiring principal for which to list grants.\nTo specify the retiring principal, use the Amazon Resource Name (ARN) of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, federated users, and assumed role users. For examples of the ARN syntax for specifying a principal, see AWS Identity and Access Management (IAM) in the Example ARNs section of the Amazon Web Services General Reference .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Grants': [
        {
            'KeyId': 'string',
            'GrantId': 'string',
            'Name': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'GranteePrincipal': 'string',
            'RetiringPrincipal': 'string',
            'IssuingAccount': 'string',
            'Operations': [
                'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'Sign'|'Verify'|'GetPublicKey'|'CreateGrant'|'RetireGrant'|'DescribeKey'|'GenerateDataKeyPair'|'GenerateDataKeyPairWithoutPlaintext',
            ],
            'Constraints': {
                'EncryptionContextSubset': {
                    'string': 'string'
                },
                'EncryptionContextEquals': {
                    'string': 'string'
                }
            }
        },
    ],
    'NextMarker': 'string',
    'Truncated': True|False
}


Response Structure

(dict) --

Grants (list) --
A list of grants.

(dict) --
Contains information about an entry in a list of grants.

KeyId (string) --
The unique identifier for the customer master key (CMK) to which the grant applies.

GrantId (string) --
The unique identifier for the grant.

Name (string) --
The friendly name that identifies the grant. If a name was provided in the  CreateGrant request, that name is returned. Otherwise this value is null.

CreationDate (datetime) --
The date and time when the grant was created.

GranteePrincipal (string) --
The principal that receives the grant\'s permissions.

RetiringPrincipal (string) --
The principal that can retire the grant.

IssuingAccount (string) --
The AWS account under which the grant was issued.

Operations (list) --
The list of operations permitted by the grant.

(string) --


Constraints (dict) --
A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows.

EncryptionContextSubset (dict) --
A list of key-value pairs that must be included in the encryption context of the cryptographic operation request. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs.

(string) --
(string) --




EncryptionContextEquals (dict) --
A list of key-value pairs that must match the encryption context in the cryptographic operation request. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint.

(string) --
(string) --










NextMarker (string) --
When Truncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent request.

Truncated (boolean) --
A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the NextMarker element in thisresponse to the Marker parameter in a subsequent request.







Exceptions

KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.InvalidMarkerException
KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.KMSInternalException

Examples
The following example lists the grants that the specified principal (identity) can retire.
response = client.list_retirable_grants(
    # The retiring principal whose grants you want to list. Use the Amazon Resource Name (ARN) of an AWS principal such as an AWS account (root), IAM user, federated user, or assumed role user.
    RetiringPrincipal='arn:aws:iam::111122223333:role/ExampleRole',
)

print(response)


Expected Output:
{
    # A list of grants that the specified principal can retire.
    'Grants': [
        {
            'CreationDate': datetime(2016, 12, 7, 11, 9, 35, 2, 342, 0),
            'GrantId': '0c237476b39f8bc44e45212e08498fbe3151305030726c0590dd8d3e9f3d6a60',
            'GranteePrincipal': 'arn:aws:iam::111122223333:role/ExampleRole',
            'IssuingAccount': 'arn:aws:iam::444455556666:root',
            'KeyId': 'arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab',
            'Operations': [
                'Decrypt',
                'Encrypt',
            ],
            'RetiringPrincipal': 'arn:aws:iam::111122223333:role/ExampleRole',
        },
    ],
    # A boolean that indicates whether there are more items in the list. Returns true when there are more items, or false when there are not.
    'Truncated': False,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Grants': [
            {
                'KeyId': 'string',
                'GrantId': 'string',
                'Name': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'GranteePrincipal': 'string',
                'RetiringPrincipal': 'string',
                'IssuingAccount': 'string',
                'Operations': [
                    'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'Sign'|'Verify'|'GetPublicKey'|'CreateGrant'|'RetireGrant'|'DescribeKey'|'GenerateDataKeyPair'|'GenerateDataKeyPairWithoutPlaintext',
                ],
                'Constraints': {
                    'EncryptionContextSubset': {
                        'string': 'string'
                    },
                    'EncryptionContextEquals': {
                        'string': 'string'
                    }
                }
            },
        ],
        'NextMarker': 'string',
        'Truncated': True|False
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_key_policy(KeyId=None, PolicyName=None, Policy=None, BypassPolicyLockoutSafetyCheck=None):
    """
    Attaches a key policy to the specified customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.
    For more information about key policies, see Key Policies in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example attaches a key policy to the specified CMK.
    Expected Output:
    
    :example: response = client.put_key_policy(
        KeyId='string',
        PolicyName='string',
        Policy='string',
        BypassPolicyLockoutSafetyCheck=True|False
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nA unique identifier for the customer master key (CMK).\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the key policy. The only valid value is default .\n

    :type Policy: string
    :param Policy: [REQUIRED]\nThe key policy to attach to the CMK.\nThe key policy must meet the following criteria:\n\nIf you don\'t set BypassPolicyLockoutSafetyCheck to true, the key policy must allow the principal that is making the PutKeyPolicy request to make a subsequent PutKeyPolicy request on the CMK. This reduces the risk that the CMK becomes unmanageable. For more information, refer to the scenario in the Default Key Policy section of the AWS Key Management Service Developer Guide .\nEach statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to AWS KMS. For more information, see Changes that I make are not always immediately visible in the AWS Identity and Access Management User Guide .\n\nThe key policy cannot exceed 32 kilobytes (32768 bytes). For more information, see Resource Quotas in the AWS Key Management Service Developer Guide .\n

    :type BypassPolicyLockoutSafetyCheck: boolean
    :param BypassPolicyLockoutSafetyCheck: A flag to indicate whether to bypass the key policy lockout safety check.\n\nWarning\nSetting this value to true increases the risk that the CMK becomes unmanageable. Do not set this value to true indiscriminately.\nFor more information, refer to the scenario in the Default Key Policy section in the AWS Key Management Service Developer Guide .\n\nUse this parameter only when you intend to prevent the principal that is making the request from making a subsequent PutKeyPolicy request on the CMK.\nThe default value is false.\n

    :return: response = client.put_key_policy(
        # The identifier of the CMK to attach the key policy to. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
        KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
        # The key policy document.
        Policy='{\
        "Version": "2012-10-17",\
        "Id": "custom-policy-2016-12-07",\
        "Statement": [\
            {\
                "Sid": "Enable IAM User Permissions",\
                "Effect": "Allow",\
                "Principal": {\
                    "AWS": "arn:aws:iam::111122223333:root"\
                },\
                "Action": "kms:*",\
                "Resource": "*"\
            },\
            {\
                "Sid": "Allow access for Key Administrators",\
                "Effect": "Allow",\
                "Principal": {\
                    "AWS": [\
                        "arn:aws:iam::111122223333:user/ExampleAdminUser",\
                        "arn:aws:iam::111122223333:role/ExampleAdminRole"\
                    ]\
                },\
                "Action": [\
                    "kms:Create*",\
                    "kms:Describe*",\
                    "kms:Enable*",\
                    "kms:List*",\
                    "kms:Put*",\
                    "kms:Update*",\
                    "kms:Revoke*",\
                    "kms:Disable*",\
                    "kms:Get*",\
                    "kms:Delete*",\
                    "kms:ScheduleKeyDeletion",\
                    "kms:CancelKeyDeletion"\
                ],\
                "Resource": "*"\
            },\
            {\
                "Sid": "Allow use of the key",\
                "Effect": "Allow",\
                "Principal": {\
                    "AWS": "arn:aws:iam::111122223333:role/ExamplePowerUserRole"\
                },\
                "Action": [\
                    "kms:Encrypt",\
                    "kms:Decrypt",\
                    "kms:ReEncrypt*",\
                    "kms:GenerateDataKey*",\
                    "kms:DescribeKey"\
                ],\
                "Resource": "*"\
            },\
            {\
                "Sid": "Allow attachment of persistent resources",\
                "Effect": "Allow",\
                "Principal": {\
                    "AWS": "arn:aws:iam::111122223333:role/ExamplePowerUserRole"\
                },\
                "Action": [\
                    "kms:CreateGrant",\
                    "kms:ListGrants",\
                    "kms:RevokeGrant"\
                ],\
                "Resource": "*",\
                "Condition": {\
                    "Bool": {\
                        "kms:GrantIsForAWSResource": "true"\
                    }\
                }\
            }\
        ]\
    }\
    ',
        # The name of the key policy.
        PolicyName='default',
    )
    
    print(response)
    
    
    :returns: 
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.MalformedPolicyDocumentException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.UnsupportedOperationException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.LimitExceededException
    KMS.Client.exceptions.KMSInvalidStateException
    
    """
    pass

def re_encrypt(CiphertextBlob=None, SourceEncryptionContext=None, SourceKeyId=None, DestinationKeyId=None, DestinationEncryptionContext=None, SourceEncryptionAlgorithm=None, DestinationEncryptionAlgorithm=None, GrantTokens=None):
    """
    Decrypts ciphertext and then reencrypts it entirely within AWS KMS. You can use this operation to change the customer master key (CMK) under which data is encrypted, such as when you manually rotate a CMK or change the CMK that protects a ciphertext. You can also use it to reencrypt ciphertext under the same CMK, such as to change the encryption context of a ciphertext.
    The ReEncrypt operation can decrypt ciphertext that was encrypted by using an AWS KMS CMK in an AWS KMS operation, such as  Encrypt or  GenerateDataKey . It can also decrypt ciphertext that was encrypted by using the public key of an asymmetric CMK outside of AWS KMS. However, it cannot decrypt ciphertext produced by other libraries, such as the AWS Encryption SDK or Amazon S3 client-side encryption . These libraries return a ciphertext format that is incompatible with AWS KMS.
    When you use the ReEncrypt operation, you need to provide information for the decrypt operation and the subsequent encrypt operation.
    Unlike other AWS KMS API operations, ReEncrypt callers must have two permissions:
    To permit reencryption from
    or to a CMK, include the "kms:ReEncrypt*" permission in your key policy . This permission is automatically included in the key policy when you use the console to create a CMK. But you must include it manually when you create a CMK programmatically or when you use the  PutKeyPolicy operation set a key policy.
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example reencrypts data with the specified CMK.
    Expected Output:
    
    :example: response = client.re_encrypt(
        CiphertextBlob=b'bytes',
        SourceEncryptionContext={
            'string': 'string'
        },
        SourceKeyId='string',
        DestinationKeyId='string',
        DestinationEncryptionContext={
            'string': 'string'
        },
        SourceEncryptionAlgorithm='SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
        DestinationEncryptionAlgorithm='SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
        GrantTokens=[
            'string',
        ]
    )
    
    
    :type CiphertextBlob: bytes
    :param CiphertextBlob: [REQUIRED]\nCiphertext of the data to reencrypt.\n

    :type SourceEncryptionContext: dict
    :param SourceEncryptionContext: Specifies the encryption context to use to decrypt the ciphertext. Enter the same encryption context that was used to encrypt the ciphertext.\nAn encryption context is a collection of non-secret key-value pairs that represents additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is optional when encrypting with a symmetric CMK, but it is highly recommended.\nFor more information, see Encryption Context in the AWS Key Management Service Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type SourceKeyId: string
    :param SourceKeyId: A unique identifier for the CMK that is used to decrypt the ciphertext before it reencrypts it using the destination CMK.\nThis parameter is required only when the ciphertext was encrypted under an asymmetric CMK. Otherwise, AWS KMS uses the metadata that it adds to the ciphertext blob to determine which CMK was used to encrypt the ciphertext. However, you can use this parameter to ensure that a particular CMK (of any kind) is used to decrypt the ciphertext before it is reencrypted.\nIf you specify a KeyId value, the decrypt part of the ReEncrypt operation succeeds only if the specified CMK was used to encrypt the ciphertext.\nTo specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with 'alias/' .\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\nAlias name: alias/ExampleAlias\nAlias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey . To get the alias name and alias ARN, use ListAliases .\n

    :type DestinationKeyId: string
    :param DestinationKeyId: [REQUIRED]\nA unique identifier for the CMK that is used to reencrypt the data. Specify a symmetric or asymmetric CMK with a KeyUsage value of ENCRYPT_DECRYPT . To find the KeyUsage value of a CMK, use the DescribeKey operation.\nTo specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with 'alias/' . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\nAlias name: alias/ExampleAlias\nAlias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey . To get the alias name and alias ARN, use ListAliases .\n

    :type DestinationEncryptionContext: dict
    :param DestinationEncryptionContext: Specifies that encryption context to use when the reencrypting the data.\nA destination encryption context is valid only when the destination CMK is a symmetric CMK. The standard ciphertext format for asymmetric CMKs does not include fields for metadata.\nAn encryption context is a collection of non-secret key-value pairs that represents additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is optional when encrypting with a symmetric CMK, but it is highly recommended.\nFor more information, see Encryption Context in the AWS Key Management Service Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type SourceEncryptionAlgorithm: string
    :param SourceEncryptionAlgorithm: Specifies the encryption algorithm that AWS KMS will use to decrypt the ciphertext before it is reencrypted. The default value, SYMMETRIC_DEFAULT , represents the algorithm used for symmetric CMKs.\nSpecify the same algorithm that was used to encrypt the ciphertext. If you specify a different algorithm, the decrypt attempt fails.\nThis parameter is required only when the ciphertext was encrypted under an asymmetric CMK.\n

    :type DestinationEncryptionAlgorithm: string
    :param DestinationEncryptionAlgorithm: Specifies the encryption algorithm that AWS KMS will use to reecrypt the data after it has decrypted it. The default value, SYMMETRIC_DEFAULT , represents the encryption algorithm used for symmetric CMKs.\nThis parameter is required only when the destination CMK is an asymmetric CMK.\n

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.\nFor more information, see Grant Tokens in the AWS Key Management Service Developer Guide .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CiphertextBlob': b'bytes',
    'SourceKeyId': 'string',
    'KeyId': 'string',
    'SourceEncryptionAlgorithm': 'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
    'DestinationEncryptionAlgorithm': 'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256'
}


Response Structure

(dict) --

CiphertextBlob (bytes) --
The reencrypted data. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.

SourceKeyId (string) --
Unique identifier of the CMK used to originally encrypt the data.

KeyId (string) --
Unique identifier of the CMK used to reencrypt the data.

SourceEncryptionAlgorithm (string) --
The encryption algorithm that was used to decrypt the ciphertext before it was reencrypted.

DestinationEncryptionAlgorithm (string) --
The encryption algorithm that was used to reencrypt the data.







Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.DisabledException
KMS.Client.exceptions.InvalidCiphertextException
KMS.Client.exceptions.KeyUnavailableException
KMS.Client.exceptions.IncorrectKeyException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.InvalidKeyUsageException
KMS.Client.exceptions.InvalidGrantTokenException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException

Examples
The following example reencrypts data with the specified CMK.
response = client.re_encrypt(
    # The data to reencrypt.
    CiphertextBlob='<binary data>',
    # The identifier of the CMK to use to reencrypt the data. You can use the key ID or Amazon Resource Name (ARN) of the CMK, or the name or ARN of an alias that refers to the CMK.
    DestinationKeyId='0987dcba-09fe-87dc-65ba-ab0987654321',
)

print(response)


Expected Output:
{
    # The reencrypted data.
    'CiphertextBlob': '<binary data>',
    # The ARN of the CMK that was used to reencrypt the data.
    'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321',
    # The ARN of the CMK that was used to originally encrypt the data.
    'SourceKeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CiphertextBlob': b'bytes',
        'SourceKeyId': 'string',
        'KeyId': 'string',
        'SourceEncryptionAlgorithm': 'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
        'DestinationEncryptionAlgorithm': 'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256'
    }
    
    
    :returns: 
    kms:EncryptFrom permission on the source CMK
    kms:EncryptTo permission on the destination CMK
    
    """
    pass

def retire_grant(GrantToken=None, KeyId=None, GrantId=None):
    """
    Retires a grant. To clean up, you can retire a grant when you\'re done using it. You should revoke a grant when you intend to actively deny operations that depend on it. The following are permitted to call this API:
    You must identify the grant to retire by its grant token or by a combination of the grant ID and the Amazon Resource Name (ARN) of the customer master key (CMK). A grant token is a unique variable-length base64-encoded string. A grant ID is a 64 character unique identifier of a grant. The  CreateGrant operation returns both.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example retires a grant.
    Expected Output:
    
    :example: response = client.retire_grant(
        GrantToken='string',
        KeyId='string',
        GrantId='string'
    )
    
    
    :type GrantToken: string
    :param GrantToken: Token that identifies the grant to be retired.

    :type KeyId: string
    :param KeyId: The Amazon Resource Name (ARN) of the CMK associated with the grant.\nFor example: arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab\n

    :type GrantId: string
    :param GrantId: Unique identifier of the grant to retire. The grant ID is returned in the response to a CreateGrant operation.\n\nGrant ID Example - 0123456789012345678901234567890123456789012345678901234567890123\n\n

    :return: response = client.retire_grant(
        # The identifier of the grant to retire.
        GrantId='0c237476b39f8bc44e45212e08498fbe3151305030726c0590dd8d3e9f3d6a60',
        # The Amazon Resource Name (ARN) of the customer master key (CMK) associated with the grant.
        KeyId='arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab',
    )
    
    print(response)
    
    
    :returns: 
    GrantToken (string) -- Token that identifies the grant to be retired.
    KeyId (string) -- The Amazon Resource Name (ARN) of the CMK associated with the grant.
    For example: arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab
    
    GrantId (string) -- Unique identifier of the grant to retire. The grant ID is returned in the response to a CreateGrant operation.
    
    Grant ID Example - 0123456789012345678901234567890123456789012345678901234567890123
    
    
    
    """
    pass

def revoke_grant(KeyId=None, GrantId=None):
    """
    Revokes the specified grant for the specified customer master key (CMK). You can revoke a grant to actively deny operations that depend on it.
    To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the KeyId parameter.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example revokes a grant.
    Expected Output:
    
    :example: response = client.revoke_grant(
        KeyId='string',
        GrantId='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nA unique identifier for the customer master key associated with the grant.\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :type GrantId: string
    :param GrantId: [REQUIRED]\nIdentifier of the grant to be revoked.\n

    :return: response = client.revoke_grant(
        # The identifier of the grant to revoke.
        GrantId='0c237476b39f8bc44e45212e08498fbe3151305030726c0590dd8d3e9f3d6a60',
        # The identifier of the customer master key (CMK) associated with the grant. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
        KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
    )
    
    print(response)
    
    
    :returns: 
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.InvalidGrantIdException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.KMSInvalidStateException
    
    """
    pass

def schedule_key_deletion(KeyId=None, PendingWindowInDays=None):
    """
    Schedules the deletion of a customer master key (CMK). You may provide a waiting period, specified in days, before deletion occurs. If you do not provide a waiting period, the default period of 30 days is used. When this operation is successful, the key state of the CMK changes to PendingDeletion . Before the waiting period ends, you can use  CancelKeyDeletion to cancel the deletion of the CMK. After the waiting period ends, AWS KMS deletes the CMK and all AWS KMS data associated with it, including all aliases that refer to it.
    If you schedule deletion of a CMK from a custom key store , when the waiting period expires, ScheduleKeyDeletion deletes the CMK from AWS KMS. Then AWS KMS makes a best effort to delete the key material from the associated AWS CloudHSM cluster. However, you might need to manually delete the orphaned key material from the cluster and its backups.
    You cannot perform this operation on a CMK in a different AWS account.
    For more information about scheduling a CMK for deletion, see Deleting Customer Master Keys in the AWS Key Management Service Developer Guide .
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example schedules the specified CMK for deletion.
    Expected Output:
    
    :example: response = client.schedule_key_deletion(
        KeyId='string',
        PendingWindowInDays=123
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nThe unique identifier of the customer master key (CMK) to delete.\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :type PendingWindowInDays: integer
    :param PendingWindowInDays: The waiting period, specified in number of days. After the waiting period ends, AWS KMS deletes the customer master key (CMK).\nThis value is optional. If you include a value, it must be between 7 and 30, inclusive. If you do not include a value, it defaults to 30.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'KeyId': 'string',
    'DeletionDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

KeyId (string) --
The unique identifier of the customer master key (CMK) for which deletion is scheduled.

DeletionDate (datetime) --
The date and time after which AWS KMS deletes the customer master key (CMK).







Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.InvalidArnException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException

Examples
The following example schedules the specified CMK for deletion.
response = client.schedule_key_deletion(
    # The identifier of the CMK to schedule for deletion. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
    KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
    # The waiting period, specified in number of days. After the waiting period ends, AWS KMS deletes the CMK.
    PendingWindowInDays=7,
)

print(response)


Expected Output:
{
    # The date and time after which AWS KMS deletes the CMK.
    'DeletionDate': datetime(2016, 12, 17, 16, 0, 0, 5, 352, 0),
    # The ARN of the CMK that is scheduled for deletion.
    'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'KeyId': 'string',
        'DeletionDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.KMSInvalidStateException
    
    """
    pass

def sign(KeyId=None, Message=None, MessageType=None, GrantTokens=None, SigningAlgorithm=None):
    """
    Creates a digital signature for a message or message digest by using the private key in an asymmetric CMK. To verify the signature, use the  Verify operation, or use the public key in the same asymmetric CMK outside of AWS KMS. For information about symmetric and asymmetric CMKs, see Using Symmetric and Asymmetric CMKs in the AWS Key Management Service Developer Guide .
    Digital signatures are generated and verified by using asymmetric key pair, such as an RSA or ECC pair that is represented by an asymmetric customer master key (CMK). The key owner (or an authorized user) uses their private key to sign a message. Anyone with the public key can verify that the message was signed with that particular private key and that the message hasn\'t changed since it was signed.
    To use the Sign operation, provide the following information:
    To verify the signature that this operation generates, use the  Verify operation. Or use the  GetPublicKey operation to download the public key and then use the public key to verify the signature outside of AWS KMS.
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.sign(
        KeyId='string',
        Message=b'bytes',
        MessageType='RAW'|'DIGEST',
        GrantTokens=[
            'string',
        ],
        SigningAlgorithm='RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'|'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'|'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nIdentifies an asymmetric CMK. AWS KMS uses the private key in the asymmetric CMK to sign the message. The KeyUsage type of the CMK must be SIGN_VERIFY . To find the KeyUsage of a CMK, use the DescribeKey operation.\nTo specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with 'alias/' . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\nAlias name: alias/ExampleAlias\nAlias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey . To get the alias name and alias ARN, use ListAliases .\n

    :type Message: bytes
    :param Message: [REQUIRED]\nSpecifies the message or message digest to sign. Messages can be 0-4096 bytes. To sign a larger message, provide the message digest.\nIf you provide a message, AWS KMS generates a hash digest of the message and then signs it.\n

    :type MessageType: string
    :param MessageType: Tells AWS KMS whether the value of the Message parameter is a message or message digest. The default value, RAW, indicates a message. To indicate a message digest, enter DIGEST .

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.\nFor more information, see Grant Tokens in the AWS Key Management Service Developer Guide .\n\n(string) --\n\n

    :type SigningAlgorithm: string
    :param SigningAlgorithm: [REQUIRED]\nSpecifies the signing algorithm to use when signing the message.\nChoose an algorithm that is compatible with the type and size of the specified asymmetric CMK.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'KeyId': 'string',
    'Signature': b'bytes',
    'SigningAlgorithm': 'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'|'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'|'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512'
}


Response Structure

(dict) --

KeyId (string) --
The Amazon Resource Name (ARN) of the asymmetric CMK that was used to sign the message.

Signature (bytes) --
The cryptographic signature that was generated for the message.

When used with the supported RSA signing algorithms, the encoding of this value is defined by PKCS #1 in RFC 8017 .
When used with the ECDSA_SHA_256 , ECDSA_SHA_384 , or ECDSA_SHA_512 signing algorithms, this value is a DER-encoded object as defined by ANS X9.62\xe2\x80\x932005 and RFC 3279 Section 2.2.3 . This is the most commonly used signature format and is appropriate for most uses.

When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.

SigningAlgorithm (string) --
The signing algorithm that was used to sign the message.







Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.DisabledException
KMS.Client.exceptions.KeyUnavailableException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.InvalidKeyUsageException
KMS.Client.exceptions.InvalidGrantTokenException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException


    :return: {
        'KeyId': 'string',
        'Signature': b'bytes',
        'SigningAlgorithm': 'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'|'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'|'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512'
    }
    
    
    :returns: 
    KeyId (string) -- [REQUIRED]
    Identifies an asymmetric CMK. AWS KMS uses the private key in the asymmetric CMK to sign the message. The KeyUsage type of the CMK must be SIGN_VERIFY . To find the KeyUsage of a CMK, use the  DescribeKey operation.
    To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with "alias/" . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.
    For example:
    
    Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
    Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
    Alias name: alias/ExampleAlias
    Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias
    
    To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .
    
    Message (bytes) -- [REQUIRED]
    Specifies the message or message digest to sign. Messages can be 0-4096 bytes. To sign a larger message, provide the message digest.
    If you provide a message, AWS KMS generates a hash digest of the message and then signs it.
    
    MessageType (string) -- Tells AWS KMS whether the value of the Message parameter is a message or message digest. The default value, RAW, indicates a message. To indicate a message digest, enter DIGEST .
    GrantTokens (list) -- A list of grant tokens.
    For more information, see Grant Tokens in the AWS Key Management Service Developer Guide .
    
    (string) --
    
    
    SigningAlgorithm (string) -- [REQUIRED]
    Specifies the signing algorithm to use when signing the message.
    Choose an algorithm that is compatible with the type and size of the specified asymmetric CMK.
    
    
    """
    pass

def tag_resource(KeyId=None, Tags=None):
    """
    Adds or edits tags for a customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.
    Each tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.
    You can only use a tag key once for each CMK. If you use the tag key again, AWS KMS replaces the current tag value with the specified value.
    For information about the rules that apply to tag keys and tag values, see User-Defined Tag Restrictions in the AWS Billing and Cost Management User Guide .
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example tags a CMK.
    Expected Output:
    
    :example: response = client.tag_resource(
        KeyId='string',
        Tags=[
            {
                'TagKey': 'string',
                'TagValue': 'string'
            },
        ]
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nA unique identifier for the CMK you are tagging.\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :type Tags: list
    :param Tags: [REQUIRED]\nOne or more tags. Each tag consists of a tag key and a tag value.\n\n(dict) --A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.\nFor information about the rules that apply to tag keys and tag values, see User-Defined Tag Restrictions in the AWS Billing and Cost Management User Guide .\n\nTagKey (string) -- [REQUIRED]The key of the tag.\n\nTagValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :return: response = client.tag_resource(
        # The identifier of the CMK you are tagging. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
        KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
        # A list of tags.
        Tags=[
            {
                'TagKey': 'Purpose',
                'TagValue': 'Test',
            },
        ],
    )
    
    print(response)
    
    
    :returns: 
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.KMSInvalidStateException
    KMS.Client.exceptions.LimitExceededException
    KMS.Client.exceptions.TagException
    
    """
    pass

def untag_resource(KeyId=None, TagKeys=None):
    """
    Removes the specified tags from the specified customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.
    To remove a tag, specify the tag key. To change the tag value of an existing tag key, use  TagResource .
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example removes tags from a CMK.
    Expected Output:
    
    :example: response = client.untag_resource(
        KeyId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nA unique identifier for the CMK from which you are removing tags.\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nOne or more tag keys. Specify only the tag keys, not the tag values.\n\n(string) --\n\n

    :return: response = client.untag_resource(
        # The identifier of the CMK whose tags you are removing.
        KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
        # A list of tag keys. Provide only the tag keys, not the tag values.
        TagKeys=[
            'Purpose',
            'CostCenter',
        ],
    )
    
    print(response)
    
    
    :returns: 
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.KMSInvalidStateException
    KMS.Client.exceptions.TagException
    
    """
    pass

def update_alias(AliasName=None, TargetKeyId=None):
    """
    Associates an existing AWS KMS alias with a different customer master key (CMK). Each alias is associated with only one CMK at a time, although a CMK can have multiple aliases. The alias and the CMK must be in the same AWS account and region. You cannot perform this operation on an alias in a different AWS account.
    The current and new CMK must be the same type (both symmetric or both asymmetric), and they must have the same key usage (ENCRYPT_DECRYPT or SIGN_VERIFY ). This restriction prevents errors in code that uses aliases. If you must assign an alias to a different type of CMK, use  DeleteAlias to delete the old alias and  CreateAlias to create a new alias.
    You cannot use UpdateAlias to change an alias name. To change an alias name, use  DeleteAlias to delete the old alias and  CreateAlias to create a new alias.
    Because an alias is not a property of a CMK, you can create, update, and delete the aliases of a CMK without affecting the CMK. Also, aliases do not appear in the response from the  DescribeKey operation. To get the aliases of all CMKs in the account, use the  ListAliases operation.
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example updates the specified alias to refer to the specified customer master key (CMK).
    Expected Output:
    
    :example: response = client.update_alias(
        AliasName='string',
        TargetKeyId='string'
    )
    
    
    :type AliasName: string
    :param AliasName: [REQUIRED]\nIdentifies the alias that is changing its CMK. This value must begin with alias/ followed by the alias name, such as alias/ExampleAlias . You cannot use UpdateAlias to change the alias name.\n

    :type TargetKeyId: string
    :param TargetKeyId: [REQUIRED]\nIdentifies the CMK to associate with the alias. When the update operation completes, the alias will point to this CMK.\nThe CMK must be in the same AWS account and Region as the alias. Also, the new target CMK must be the same type as the current target CMK (both symmetric or both asymmetric) and they must have the same key usage.\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\nTo verify that the alias is mapped to the correct CMK, use ListAliases .\n

    :return: response = client.update_alias(
        # The alias to update.
        AliasName='alias/ExampleAlias',
        # The identifier of the CMK that the alias will refer to after this operation succeeds. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
        TargetKeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
    )
    
    print(response)
    
    
    :returns: 
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.KMSInvalidStateException
    
    """
    pass

def update_custom_key_store(CustomKeyStoreId=None, NewCustomKeyStoreName=None, KeyStorePassword=None, CloudHsmClusterId=None):
    """
    Changes the properties of a custom key store. Use the CustomKeyStoreId parameter to identify the custom key store you want to edit. Use the remaining parameters to change the properties of the custom key store.
    You can only update a custom key store that is disconnected. To disconnect the custom key store, use  DisconnectCustomKeyStore . To reconnect the custom key store after the update completes, use  ConnectCustomKeyStore . To find the connection state of a custom key store, use the  DescribeCustomKeyStores operation.
    Use the parameters of UpdateCustomKeyStore to edit your keystore settings.
    If the operation succeeds, it returns a JSON object with no properties.
    This operation is part of the Custom Key Store feature feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a single-tenant key store.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_custom_key_store(
        CustomKeyStoreId='string',
        NewCustomKeyStoreName='string',
        KeyStorePassword='string',
        CloudHsmClusterId='string'
    )
    
    
    :type CustomKeyStoreId: string
    :param CustomKeyStoreId: [REQUIRED]\nIdentifies the custom key store that you want to update. Enter the ID of the custom key store. To find the ID of a custom key store, use the DescribeCustomKeyStores operation.\n

    :type NewCustomKeyStoreName: string
    :param NewCustomKeyStoreName: Changes the friendly name of the custom key store to the value that you specify. The custom key store name must be unique in the AWS account.

    :type KeyStorePassword: string
    :param KeyStorePassword: Enter the current password of the kmsuser crypto user (CU) in the AWS CloudHSM cluster that is associated with the custom key store.\nThis parameter tells AWS KMS the current password of the kmsuser crypto user (CU). It does not set or change the password of any users in the AWS CloudHSM cluster.\n

    :type CloudHsmClusterId: string
    :param CloudHsmClusterId: Associates the custom key store with a related AWS CloudHSM cluster.\nEnter the cluster ID of the cluster that you used to create the custom key store or a cluster that shares a backup history and has the same cluster certificate as the original cluster. You cannot use this parameter to associate a custom key store with an unrelated cluster. In addition, the replacement cluster must fulfill the requirements for a cluster associated with a custom key store. To view the cluster certificate of a cluster, use the DescribeClusters operation.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KMS.Client.exceptions.CustomKeyStoreNotFoundException
KMS.Client.exceptions.CustomKeyStoreNameInUseException
KMS.Client.exceptions.CloudHsmClusterNotFoundException
KMS.Client.exceptions.CloudHsmClusterNotRelatedException
KMS.Client.exceptions.CustomKeyStoreInvalidStateException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.CloudHsmClusterNotActiveException
KMS.Client.exceptions.CloudHsmClusterInvalidConfigurationException


    :return: {}
    
    
    :returns: 
    CustomKeyStoreId (string) -- [REQUIRED]
    Identifies the custom key store that you want to update. Enter the ID of the custom key store. To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.
    
    NewCustomKeyStoreName (string) -- Changes the friendly name of the custom key store to the value that you specify. The custom key store name must be unique in the AWS account.
    KeyStorePassword (string) -- Enter the current password of the kmsuser crypto user (CU) in the AWS CloudHSM cluster that is associated with the custom key store.
    This parameter tells AWS KMS the current password of the kmsuser crypto user (CU). It does not set or change the password of any users in the AWS CloudHSM cluster.
    
    CloudHsmClusterId (string) -- Associates the custom key store with a related AWS CloudHSM cluster.
    Enter the cluster ID of the cluster that you used to create the custom key store or a cluster that shares a backup history and has the same cluster certificate as the original cluster. You cannot use this parameter to associate a custom key store with an unrelated cluster. In addition, the replacement cluster must fulfill the requirements for a cluster associated with a custom key store. To view the cluster certificate of a cluster, use the DescribeClusters operation.
    
    
    """
    pass

def update_key_description(KeyId=None, Description=None):
    """
    Updates the description of a customer master key (CMK). To see the description of a CMK, use  DescribeKey .
    You cannot perform this operation on a CMK in a different AWS account.
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example updates the description of the specified CMK.
    Expected Output:
    
    :example: response = client.update_key_description(
        KeyId='string',
        Description='string'
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nA unique identifier for the customer master key (CMK).\nSpecify the key ID or the Amazon Resource Name (ARN) of the CMK.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey .\n

    :type Description: string
    :param Description: [REQUIRED]\nNew description for the CMK.\n

    :return: response = client.update_key_description(
        # The updated description.
        Description='Example description that indicates the intended use of this CMK.',
        # The identifier of the CMK whose description you are updating. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
        KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
    )
    
    print(response)
    
    
    :returns: 
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.InvalidArnException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.KMSInvalidStateException
    
    """
    pass

def verify(KeyId=None, Message=None, MessageType=None, Signature=None, SigningAlgorithm=None, GrantTokens=None):
    """
    Verifies a digital signature that was generated by the  Sign operation.
    Verification confirms that an authorized user signed the message with the specified CMK and signing algorithm, and the message hasn\'t changed since it was signed. If the signature is verified, the value of the SignatureValid field in the response is True . If the signature verification fails, the Verify operation fails with an KMSInvalidSignatureException exception.
    A digital signature is generated by using the private key in an asymmetric CMK. The signature is verified by using the public key in the same asymmetric CMK. For information about symmetric and asymmetric CMKs, see Using Symmetric and Asymmetric CMKs in the AWS Key Management Service Developer Guide .
    To verify a digital signature, you can use the Verify operation. Specify the same asymmetric CMK, message, and signing algorithm that were used to produce the signature.
    You can also verify the digital signature by using the public key of the CMK outside of AWS KMS. Use the  GetPublicKey operation to download the public key in the asymmetric CMK and then use the public key to verify the signature outside of AWS KMS. The advantage of using the Verify operation is that it is performed within AWS KMS. As a result, it\'s easy to call, the operation is performed within the FIPS boundary, it is logged in AWS CloudTrail, and you can use key policy and IAM policy to determine who is authorized to use the CMK to verify signatures.
    The CMK that you use for this operation must be in a compatible key state. For details, see How Key State Affects Use of a Customer Master Key in the AWS Key Management Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.verify(
        KeyId='string',
        Message=b'bytes',
        MessageType='RAW'|'DIGEST',
        Signature=b'bytes',
        SigningAlgorithm='RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'|'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'|'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512',
        GrantTokens=[
            'string',
        ]
    )
    
    
    :type KeyId: string
    :param KeyId: [REQUIRED]\nIdentifies the asymmetric CMK that will be used to verify the signature. This must be the same CMK that was used to generate the signature. If you specify a different CMK, the signature verification fails.\nTo specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with 'alias/' . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.\nFor example:\n\nKey ID: 1234abcd-12ab-34cd-56ef-1234567890ab\nKey ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\nAlias name: alias/ExampleAlias\nAlias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias\n\nTo get the key ID and key ARN for a CMK, use ListKeys or DescribeKey . To get the alias name and alias ARN, use ListAliases .\n

    :type Message: bytes
    :param Message: [REQUIRED]\nSpecifies the message that was signed. You can submit a raw message of up to 4096 bytes, or a hash digest of the message. If you submit a digest, use the MessageType parameter with a value of DIGEST .\nIf the message specified here is different from the message that was signed, the signature verification fails. A message and its hash digest are considered to be the same message.\n

    :type MessageType: string
    :param MessageType: Tells AWS KMS whether the value of the Message parameter is a message or message digest. The default value, RAW, indicates a message. To indicate a message digest, enter DIGEST .\n\nWarning\nUse the DIGEST value only when the value of the Message parameter is a message digest. If you use the DIGEST value with a raw message, the security of the verification operation can be compromised.\n\n

    :type Signature: bytes
    :param Signature: [REQUIRED]\nThe signature that the Sign operation generated.\n

    :type SigningAlgorithm: string
    :param SigningAlgorithm: [REQUIRED]\nThe signing algorithm that was used to sign the message. If you submit a different algorithm, the signature verification fails.\n

    :type GrantTokens: list
    :param GrantTokens: A list of grant tokens.\nFor more information, see Grant Tokens in the AWS Key Management Service Developer Guide .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'KeyId': 'string',
    'SignatureValid': True|False,
    'SigningAlgorithm': 'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'|'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'|'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512'
}


Response Structure

(dict) --

KeyId (string) --
The unique identifier for the asymmetric CMK that was used to verify the signature.

SignatureValid (boolean) --
A Boolean value that indicates whether the signature was verified. A value of True indicates that the Signature was produced by signing the Message with the specified KeyID and SigningAlgorithm. If the signature is not verified, the Verify operation fails with a KMSInvalidSignatureException exception.

SigningAlgorithm (string) --
The signing algorithm that was used to verify the signature.







Exceptions

KMS.Client.exceptions.NotFoundException
KMS.Client.exceptions.DisabledException
KMS.Client.exceptions.KeyUnavailableException
KMS.Client.exceptions.DependencyTimeoutException
KMS.Client.exceptions.InvalidKeyUsageException
KMS.Client.exceptions.InvalidGrantTokenException
KMS.Client.exceptions.KMSInternalException
KMS.Client.exceptions.KMSInvalidStateException
KMS.Client.exceptions.KMSInvalidSignatureException


    :return: {
        'KeyId': 'string',
        'SignatureValid': True|False,
        'SigningAlgorithm': 'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'|'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'|'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512'
    }
    
    
    :returns: 
    KMS.Client.exceptions.NotFoundException
    KMS.Client.exceptions.DisabledException
    KMS.Client.exceptions.KeyUnavailableException
    KMS.Client.exceptions.DependencyTimeoutException
    KMS.Client.exceptions.InvalidKeyUsageException
    KMS.Client.exceptions.InvalidGrantTokenException
    KMS.Client.exceptions.KMSInternalException
    KMS.Client.exceptions.KMSInvalidStateException
    KMS.Client.exceptions.KMSInvalidSignatureException
    
    """
    pass

