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


def add_client_id_to_open_id_connect_provider(OpenIDConnectProviderArn=None, ClientID=None):
    """
    :param OpenIDConnectProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM OpenID Connect (OIDC) provider resource to add the client ID to. You can get a list of OIDC provider ARNs by using the ListOpenIDConnectProviders action.
            
    :type OpenIDConnectProviderArn: string
    :param ClientID: [REQUIRED]
            The client ID (also known as audience) to add to the IAM OpenID Connect provider resource.
            
    :type ClientID: string
    """
    pass


def add_role_to_instance_profile(InstanceProfileName=None, RoleName=None):
    """
    :param InstanceProfileName: [REQUIRED]
            The name of the instance profile to update.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type InstanceProfileName: string
    :param RoleName: [REQUIRED]
            The name of the role to add.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type RoleName: string
    """
    pass


def add_user_to_group(GroupName=None, UserName=None):
    """
    :param GroupName: [REQUIRED]
            The name of the group to update.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type GroupName: string
    :param UserName: [REQUIRED]
            The name of the user to add.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    """
    pass


def attach_group_policy(GroupName=None, PolicyArn=None):
    """
    :param GroupName: [REQUIRED]
            The name (friendly name, not ARN) of the group to attach the policy to.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type GroupName: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy you want to attach.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type PolicyArn: string
    """
    pass


def attach_role_policy(RoleName=None, PolicyArn=None):
    """
    :param RoleName: [REQUIRED]
            The name (friendly name, not ARN) of the role to attach the policy to.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type RoleName: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy you want to attach.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type PolicyArn: string
    """
    pass


def attach_user_policy(UserName=None, PolicyArn=None):
    """
    :param UserName: [REQUIRED]
            The name (friendly name, not ARN) of the IAM user to attach the policy to.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy you want to attach.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type PolicyArn: string
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


def change_password(OldPassword=None, NewPassword=None):
    """
    :param OldPassword: [REQUIRED]
            The IAM user's current password.
            
    :type OldPassword: string
    :param NewPassword: [REQUIRED]
            The new password. The new password must conform to the AWS account's password policy, if one exists.
            The regex pattern for this parameter is a string of characters consisting of almost any printable ASCII character from the space (u0020) through the end of the ASCII character range (u00FF). You can also include the tab (u0009), line feed (u000A), and carriage return (u000D) characters. Although any of these characters are valid in a password, note that many tools, such as the AWS Management Console, might restrict the ability to enter certain characters because they have special meaning within that tool.
            
    :type NewPassword: string
    """
    pass


def create_access_key(UserName=None):
    """
    :param UserName: The name of the IAM user that the new key will belong to.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            Return typedict
            ReturnsResponse Syntax{
              'AccessKey': {
                'UserName': 'string',
                'AccessKeyId': 'string',
                'Status': 'Active'|'Inactive',
                'SecretAccessKey': 'string',
                'CreateDate': datetime(2015, 1, 1)
              }
            }
            Response Structure
            (dict) --Contains the response to a successful CreateAccessKey request.
            AccessKey (dict) --A structure with details about the access key.
            UserName (string) --The name of the IAM user that the access key is associated with.
            AccessKeyId (string) --The ID for this access key.
            Status (string) --The status of the access key. Active means the key is valid for API calls, while Inactive means it is not.
            SecretAccessKey (string) --The secret key used to sign requests.
            CreateDate (datetime) --The date when the access key was created.
            
            
            
    :type UserName: string
    """
    pass


def create_account_alias(AccountAlias=None):
    """
    :param AccountAlias: [REQUIRED]
            The account alias to create.
            The regex pattern for this parameter is a string of characters consisting of lowercase letters, digits, and dashes. You cannot start or finish with a dash, nor can you have two dashes in a row.
            ReturnsNone
            
    :type AccountAlias: string
    """
    pass


def create_group(Path=None, GroupName=None):
    """
    :param Path: The path to the group. For more information about paths, see IAM Identifiers in the IAM User Guide .
            This parameter is optional. If it is not included, it defaults to a slash (/).
            The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type Path: string
    :param GroupName: [REQUIRED]
            The name of the group to create. Do not include the path in this value.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-. The group name must be unique within the account. Group names are not distinguished by case. For example, you cannot create groups named both 'ADMINS' and 'admins'.
            
    :type GroupName: string
    """
    pass


def create_instance_profile(InstanceProfileName=None, Path=None):
    """
    :param InstanceProfileName: [REQUIRED]
            The name of the instance profile to create.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type InstanceProfileName: string
    :param Path: The path to the instance profile. For more information about paths, see IAM Identifiers in the IAM User Guide .
            This parameter is optional. If it is not included, it defaults to a slash (/).
            The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type Path: string
    """
    pass


def create_login_profile(UserName=None, Password=None, PasswordResetRequired=None):
    """
    :param UserName: [REQUIRED]
            The name of the IAM user to create a password for. The user must already exist.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param Password: [REQUIRED]
            The new password for the user.
            The regex pattern for this parameter is a string of characters consisting of almost any printable ASCII character from the space (u0020) through the end of the ASCII character range (u00FF). You can also include the tab (u0009), line feed (u000A), and carriage return (u000D) characters. Although any of these characters are valid in a password, note that many tools, such as the AWS Management Console, might restrict the ability to enter certain characters because they have special meaning within that tool.
            
    :type Password: string
    :param PasswordResetRequired: Specifies whether the user is required to set a new password on next sign-in.
    :type PasswordResetRequired: boolean
    """
    pass


def create_open_id_connect_provider(Url=None, ClientIDList=None, ThumbprintList=None):
    """
    :param Url: [REQUIRED]
            The URL of the identity provider. The URL must begin with 'https://' and should correspond to the iss claim in the provider's OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a host name, like 'https://server.example.org' or 'https://example.com'.
            You cannot register the same provider multiple times in a single AWS account. If you try to submit a URL that has already been used for an OpenID Connect provider in the AWS account, you will get an error.
            
    :type Url: string
    :param ClientIDList: A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.)
            You can register multiple client IDs with the same provider. For example, you might have multiple applications that use the same OIDC provider. You cannot register more than 100 client IDs with a single IAM OIDC provider.
            There is no defined format for a client ID. The CreateOpenIDConnectProviderRequest action accepts client IDs up to 255 characters long.
            (string) --
            
    :type ClientIDList: list
    :param ThumbprintList: [REQUIRED]
            A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificate(s). Typically this list includes only one entry. However, IAM lets you have up to five thumbprints for an OIDC provider. This lets you maintain multiple thumbprints if the identity provider is rotating certificates.
            The server certificate thumbprint is the hex-encoded SHA-1 hash value of the X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string.
            You must provide at least one thumbprint when creating an IAM OIDC provider. For example, if the OIDC provider is server.example.com and the provider stores its keys at 'https://keys.server.example.com/openid-connect', the thumbprint string would be the hex-encoded SHA-1 hash value of the certificate used by https://keys.server.example.com.
            For more information about obtaining the OIDC provider's thumbprint, see Obtaining the Thumbprint for an OpenID Connect Provider in the IAM User Guide .
            (string) --Contains a thumbprint for an identity provider's server certificate.
            The identity provider's server certificate thumbprint is the hex-encoded SHA-1 hash value of the self-signed X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string.
            
    :type ThumbprintList: list
    """
    pass


def create_policy(PolicyName=None, Path=None, PolicyDocument=None, Description=None):
    """
    :param PolicyName: [REQUIRED]
            The friendly name of the policy.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type PolicyName: string
    :param Path: The path for the policy.
            For more information about paths, see IAM Identifiers in the IAM User Guide .
            This parameter is optional. If it is not included, it defaults to a slash (/).
            The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type Path: string
    :param PolicyDocument: [REQUIRED]
            The JSON policy document that you want to use as the content for the new policy.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            
    :type PolicyDocument: string
    :param Description: A friendly description of the policy.
            Typically used to store information about the permissions defined in the policy. For example, 'Grants access to production DynamoDB tables.'
            The policy description is immutable. After a value is assigned, it cannot be changed.
            
    :type Description: string
    """
    pass


def create_policy_version(PolicyArn=None, PolicyDocument=None, SetAsDefault=None):
    """
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy to which you want to add a new version.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type PolicyArn: string
    :param PolicyDocument: [REQUIRED]
            The JSON policy document that you want to use as the content for this new version of the policy.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            
    :type PolicyDocument: string
    :param SetAsDefault: Specifies whether to set this version as the policy's default version.
            When this parameter is true , the new policy version becomes the operative version; that is, the version that is in effect for the IAM users, groups, and roles that the policy is attached to.
            For more information about managed policy versions, see Versioning for Managed Policies in the IAM User Guide .
            
    :type SetAsDefault: boolean
    """
    pass


def create_role(Path=None, RoleName=None, AssumeRolePolicyDocument=None):
    """
    :param Path: The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide .
            This parameter is optional. If it is not included, it defaults to a slash (/).
            The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type Path: string
    :param RoleName: [REQUIRED]
            The name of the role to create.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-. Role names are not distinguished by case. For example, you cannot create roles named both 'PRODROLE' and 'prodrole'.
            
    :type RoleName: string
    :param AssumeRolePolicyDocument: [REQUIRED]
            The trust relationship policy document that grants an entity permission to assume the role.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            
    :type AssumeRolePolicyDocument: string
    """
    pass


def create_saml_provider(SAMLMetadataDocument=None, Name=None):
    """
    :param SAMLMetadataDocument: [REQUIRED]
            An XML document generated by an identity provider (IdP) that supports SAML 2.0. The document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that are received from the IdP. You must generate the metadata document using the identity management software that is used as your organization's IdP.
            For more information, see About SAML 2.0-based Federation in the IAM User Guide
            
    :type SAMLMetadataDocument: string
    :param Name: [REQUIRED]
            The name of the provider to create.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type Name: string
    """
    pass


def create_user(Path=None, UserName=None):
    """
    :param Path: The path for the user name. For more information about paths, see IAM Identifiers in the IAM User Guide .
            This parameter is optional. If it is not included, it defaults to a slash (/).
            The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type Path: string
    :param UserName: [REQUIRED]
            The name of the user to create.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-. User names are not distinguished by case. For example, you cannot create users named both 'TESTUSER' and 'testuser'.
            
    :type UserName: string
    """
    pass


def create_virtual_mfa_device(Path=None, VirtualMFADeviceName=None):
    """
    :param Path: The path for the virtual MFA device. For more information about paths, see IAM Identifiers in the IAM User Guide .
            This parameter is optional. If it is not included, it defaults to a slash (/).
            The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type Path: string
    :param VirtualMFADeviceName: [REQUIRED]
            The name of the virtual MFA device. Use with path to uniquely identify a virtual MFA device.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type VirtualMFADeviceName: string
    """
    pass


def deactivate_mfa_device(UserName=None, SerialNumber=None):
    """
    :param UserName: [REQUIRED]
            The name of the user whose MFA device you want to deactivate.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param SerialNumber: [REQUIRED]
            The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =/:,.@-
            
    :type SerialNumber: string
    """
    pass


def delete_access_key(UserName=None, AccessKeyId=None):
    """
    :param UserName: The name of the user whose access key pair you want to delete.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param AccessKeyId: [REQUIRED]
            The access key ID for the access key ID and secret access key you want to delete.
            The regex pattern for this parameter is a string of characters that can consist of any upper or lowercased letter or digit.
            
    :type AccessKeyId: string
    """
    pass


def delete_account_alias(AccountAlias=None):
    """
    :param AccountAlias: [REQUIRED]
            The name of the account alias to delete.
            The regex pattern for this parameter is a string of characters consisting of lowercase letters, digits, and dashes. You cannot start or finish with a dash, nor can you have two dashes in a row.
            ReturnsNone
            
    :type AccountAlias: string
    """
    pass


def delete_account_password_policy():
    """
    """
    pass


def delete_group(GroupName=None):
    """
    :param GroupName: [REQUIRED]
            The name of the IAM group to delete.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            ReturnsNone
            
    :type GroupName: string
    """
    pass


def delete_group_policy(GroupName=None, PolicyName=None):
    """
    :param GroupName: [REQUIRED]
            The name (friendly name, not ARN) identifying the group that the policy is embedded in.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type GroupName: string
    :param PolicyName: [REQUIRED]
            The name identifying the policy document to delete.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type PolicyName: string
    """
    pass


def delete_instance_profile(InstanceProfileName=None):
    """
    :param InstanceProfileName: [REQUIRED]
            The name of the instance profile to delete.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            ReturnsNone
            
    :type InstanceProfileName: string
    """
    pass


def delete_login_profile(UserName=None):
    """
    :param UserName: [REQUIRED]
            The name of the user whose password you want to delete.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            ReturnsNone
            
    :type UserName: string
    """
    pass


def delete_open_id_connect_provider(OpenIDConnectProviderArn=None):
    """
    :param OpenIDConnectProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM OpenID Connect provider resource object to delete. You can get a list of OpenID Connect provider resource ARNs by using the ListOpenIDConnectProviders action.
            ReturnsNone
            
    :type OpenIDConnectProviderArn: string
    """
    pass


def delete_policy(PolicyArn=None):
    """
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy you want to delete.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            ReturnsNone
            
    :type PolicyArn: string
    """
    pass


def delete_policy_version(PolicyArn=None, VersionId=None):
    """
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy from which you want to delete a version.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type PolicyArn: string
    :param VersionId: [REQUIRED]
            The policy version to delete.
            The regex pattern for this parameter is a string of characters that consists of the lowercase letter 'v' followed by one or two digits, and optionally followed by a period '.' and a string of letters and digits.
            For more information about managed policy versions, see Versioning for Managed Policies in the IAM User Guide .
            
    :type VersionId: string
    """
    pass


def delete_role(RoleName=None):
    """
    :param RoleName: [REQUIRED]
            The name of the role to delete.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            ReturnsNone
            
    :type RoleName: string
    """
    pass


def delete_role_policy(RoleName=None, PolicyName=None):
    """
    :param RoleName: [REQUIRED]
            The name (friendly name, not ARN) identifying the role that the policy is embedded in.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type RoleName: string
    :param PolicyName: [REQUIRED]
            The name of the inline policy to delete from the specified IAM role.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type PolicyName: string
    """
    pass


def delete_saml_provider(SAMLProviderArn=None):
    """
    :param SAMLProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the SAML provider to delete.
            ReturnsNone
            
    :type SAMLProviderArn: string
    """
    pass


def delete_server_certificate(ServerCertificateName=None):
    """
    :param ServerCertificateName: [REQUIRED]
            The name of the server certificate you want to delete.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            ReturnsNone
            
    :type ServerCertificateName: string
    """
    pass


def delete_signing_certificate(UserName=None, CertificateId=None):
    """
    :param UserName: The name of the user the signing certificate belongs to.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param CertificateId: [REQUIRED]
            The ID of the signing certificate to delete.
            The format of this parameter, as described by its regex pattern, is a string of characters that can be upper- or lower-cased letters or digits.
            
    :type CertificateId: string
    """
    pass


def delete_ssh_public_key(UserName=None, SSHPublicKeyId=None):
    """
    :param UserName: [REQUIRED]
            The name of the IAM user associated with the SSH public key.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param SSHPublicKeyId: [REQUIRED]
            The unique identifier for the SSH public key.
            The regex pattern for this parameter is a string of characters that can consist of any upper or lowercased letter or digit.
            
    :type SSHPublicKeyId: string
    """
    pass


def delete_user(UserName=None):
    """
    :param UserName: [REQUIRED]
            The name of the user to delete.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            ReturnsNone
            
    :type UserName: string
    """
    pass


def delete_user_policy(UserName=None, PolicyName=None):
    """
    :param UserName: [REQUIRED]
            The name (friendly name, not ARN) identifying the user that the policy is embedded in.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param PolicyName: [REQUIRED]
            The name identifying the policy document to delete.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type PolicyName: string
    """
    pass


def delete_virtual_mfa_device(SerialNumber=None):
    """
    :param SerialNumber: [REQUIRED]
            The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the same as the ARN.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =/:,.@-
            ReturnsNone
            
    :type SerialNumber: string
    """
    pass


def detach_group_policy(GroupName=None, PolicyArn=None):
    """
    :param GroupName: [REQUIRED]
            The name (friendly name, not ARN) of the IAM group to detach the policy from.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type GroupName: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy you want to detach.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type PolicyArn: string
    """
    pass


def detach_role_policy(RoleName=None, PolicyArn=None):
    """
    :param RoleName: [REQUIRED]
            The name (friendly name, not ARN) of the IAM role to detach the policy from.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type RoleName: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy you want to detach.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type PolicyArn: string
    """
    pass


def detach_user_policy(UserName=None, PolicyArn=None):
    """
    :param UserName: [REQUIRED]
            The name (friendly name, not ARN) of the IAM user to detach the policy from.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy you want to detach.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type PolicyArn: string
    """
    pass


def enable_mfa_device(UserName=None, SerialNumber=None, AuthenticationCode1=None, AuthenticationCode2=None):
    """
    :param UserName: [REQUIRED]
            The name of the IAM user for whom you want to enable the MFA device.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param SerialNumber: [REQUIRED]
            The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =/:,.@-
            
    :type SerialNumber: string
    :param AuthenticationCode1: [REQUIRED]
            An authentication code emitted by the device.
            The format for this parameter is a string of 6 digits.
            
    :type AuthenticationCode1: string
    :param AuthenticationCode2: [REQUIRED]
            A subsequent authentication code emitted by the device.
            The format for this parameter is a string of 6 digits.
            
    :type AuthenticationCode2: string
    """
    pass


def generate_credential_report():
    """
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


def get_access_key_last_used(AccessKeyId=None):
    """
    :param AccessKeyId: [REQUIRED]
            The identifier of an access key.
            The regex pattern for this parameter is a string of characters that can consist of any upper or lowercased letter or digit.
            Return typedict
            ReturnsResponse Syntax{
              'UserName': 'string',
              'AccessKeyLastUsed': {
                'LastUsedDate': datetime(2015, 1, 1),
                'ServiceName': 'string',
                'Region': 'string'
              }
            }
            Response Structure
            (dict) --Contains the response to a successful GetAccessKeyLastUsed request. It is also returned as a member of the AccessKeyMetaData structure returned by the ListAccessKeys action.
            UserName (string) --The name of the AWS IAM user that owns this access key.
            AccessKeyLastUsed (dict) --Contains information about the last time the access key was used.
            LastUsedDate (datetime) --The date and time, in ISO 8601 date-time format , when the access key was most recently used. This field is null when:
            The user does not have an access key.
            An access key exists but has never been used, at least not since IAM started tracking this information on April 22nd, 2015.
            There is no sign-in data associated with the user
            ServiceName (string) --The name of the AWS service with which this access key was most recently used. This field is null when:
            The user does not have an access key.
            An access key exists but has never been used, at least not since IAM started tracking this information on April 22nd, 2015.
            There is no sign-in data associated with the user
            Region (string) --The AWS region where this access key was most recently used. This field is null when:
            The user does not have an access key.
            An access key exists but has never been used, at least not since IAM started tracking this information on April 22nd, 2015.
            There is no sign-in data associated with the user
            For more information about AWS regions, see Regions and Endpoints in the Amazon Web Services General Reference.
            
            
            
    :type AccessKeyId: string
    """
    pass


def get_account_authorization_details(Filter=None, MaxItems=None, Marker=None):
    """
    :param Filter: A list of entity types used to filter the results. Only the entities that match the types you specify are included in the output. Use the value LocalManagedPolicy to include customer managed policies.
            The format for this parameter is a comma-separated (if more than one) list of strings. Each string value in the list must be one of the valid values listed below.
            (string) --
            
    :type Filter: list
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    """
    pass


def get_account_password_policy():
    """
    """
    pass


def get_account_summary():
    """
    """
    pass


def get_context_keys_for_custom_policy(PolicyInputList=None):
    """
    :param PolicyInputList: [REQUIRED]
            A list of policies for which you want the list of context keys referenced in those policies. Each document is specified as a string containing the complete, valid JSON text of an IAM policy.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'ContextKeyNames': [
                'string',
              ]
            }
            Response Structure
            (dict) --Contains the response to a successful GetContextKeysForPrincipalPolicy or GetContextKeysForCustomPolicy request.
            ContextKeyNames (list) --The list of context keys that are referenced in the input policies.
            (string) --
            
            
    :type PolicyInputList: list
    """
    pass


def get_context_keys_for_principal_policy(PolicySourceArn=None, PolicyInputList=None):
    """
    :param PolicySourceArn: [REQUIRED]
            The ARN of a user, group, or role whose policies contain the context keys that you want listed. If you specify a user, the list includes context keys that are found in all policies attached to the user as well as to all groups that the user is a member of. If you pick a group or a role, then it includes only those context keys that are found in policies attached to that entity. Note that all parameters are shown in unencoded form here for clarity, but must be URL encoded to be included as a part of a real HTML request.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type PolicySourceArn: string
    :param PolicyInputList: An optional list of additional policies for which you want the list of context keys that are referenced.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            (string) --
            
    :type PolicyInputList: list
    """
    pass


def get_credential_report():
    """
    """
    pass


def get_group(GroupName=None, Marker=None, MaxItems=None):
    """
    :param GroupName: [REQUIRED]
            The name of the group.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type GroupName: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def get_group_policy(GroupName=None, PolicyName=None):
    """
    :param GroupName: [REQUIRED]
            The name of the group the policy is associated with.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type GroupName: string
    :param PolicyName: [REQUIRED]
            The name of the policy document to get.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type PolicyName: string
    """
    pass


def get_instance_profile(InstanceProfileName=None):
    """
    :param InstanceProfileName: [REQUIRED]
            The name of the instance profile to get information about.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            Return typedict
            ReturnsResponse Syntax{
              'InstanceProfile': {
                'Path': 'string',
                'InstanceProfileName': 'string',
                'InstanceProfileId': 'string',
                'Arn': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'Roles': [
                  {
                    'Path': 'string',
                    'RoleName': 'string',
                    'RoleId': 'string',
                    'Arn': 'string',
                    'CreateDate': datetime(2015, 1, 1),
                    'AssumeRolePolicyDocument': 'string'
                  },
                ]
              }
            }
            Response Structure
            (dict) --Contains the response to a successful GetInstanceProfile request.
            InstanceProfile (dict) --A structure containing details about the instance profile.
            Path (string) --The path to the instance profile. For more information about paths, see IAM Identifiers in the Using IAM guide.
            InstanceProfileName (string) --The name identifying the instance profile.
            InstanceProfileId (string) --The stable and unique string identifying the instance profile. For more information about IDs, see IAM Identifiers in the Using IAM guide.
            Arn (string) --The Amazon Resource Name (ARN) specifying the instance profile. For more information about ARNs and how to use them in policies, see IAM Identifiers in the Using IAM guide.
            CreateDate (datetime) --The date when the instance profile was created.
            Roles (list) --The role associated with the instance profile.
            (dict) --Contains information about an IAM role.
            This data type is used as a response element in the following actions:
            CreateRole
            GetRole
            ListRoles
            Path (string) --The path to the role. For more information about paths, see IAM Identifiers in the Using IAM guide.
            RoleName (string) --The friendly name that identifies the role.
            RoleId (string) --The stable and unique string identifying the role. For more information about IDs, see IAM Identifiers in the Using IAM guide.
            Arn (string) --The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see IAM Identifiers in the Using IAM guide.
            CreateDate (datetime) --The date and time, in ISO 8601 date-time format , when the role was created.
            AssumeRolePolicyDocument (string) --The policy that grants an entity permission to assume the role.
            
            
            
            
    :type InstanceProfileName: string
    """
    pass


def get_login_profile(UserName=None):
    """
    :param UserName: [REQUIRED]
            The name of the user whose login profile you want to retrieve.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            Return typedict
            ReturnsResponse Syntax{
              'LoginProfile': {
                'UserName': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'PasswordResetRequired': True|False
              }
            }
            Response Structure
            (dict) --Contains the response to a successful GetLoginProfile request.
            LoginProfile (dict) --A structure containing the user name and password create date for the user.
            UserName (string) --The name of the user, which can be used for signing in to the AWS Management Console.
            CreateDate (datetime) --The date when the password for the user was created.
            PasswordResetRequired (boolean) --Specifies whether the user is required to set a new password on next sign-in.
            
            
            
    :type UserName: string
    """
    pass


def get_open_id_connect_provider(OpenIDConnectProviderArn=None):
    """
    :param OpenIDConnectProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the OIDC provider resource object in IAM to get information for. You can get a list of OIDC provider resource ARNs by using the ListOpenIDConnectProviders action.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            Return typedict
            ReturnsResponse Syntax{
              'Url': 'string',
              'ClientIDList': [
                'string',
              ],
              'ThumbprintList': [
                'string',
              ],
              'CreateDate': datetime(2015, 1, 1)
            }
            Response Structure
            (dict) --Contains the response to a successful GetOpenIDConnectProvider request.
            Url (string) --The URL that the IAM OIDC provider resource object is associated with. For more information, see CreateOpenIDConnectProvider .
            ClientIDList (list) --A list of client IDs (also known as audiences) that are associated with the specified IAM OIDC provider resource object. For more information, see CreateOpenIDConnectProvider .
            (string) --
            ThumbprintList (list) --A list of certificate thumbprints that are associated with the specified IAM OIDC provider resource object. For more information, see CreateOpenIDConnectProvider .
            (string) --Contains a thumbprint for an identity provider's server certificate.
            The identity provider's server certificate thumbprint is the hex-encoded SHA-1 hash value of the self-signed X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string.
            CreateDate (datetime) --The date and time when the IAM OIDC provider resource object was created in the AWS account.
            
            
    :type OpenIDConnectProviderArn: string
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


def get_policy(PolicyArn=None):
    """
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the managed policy that you want information about.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            Return typedict
            ReturnsResponse Syntax{
              'Policy': {
                'PolicyName': 'string',
                'PolicyId': 'string',
                'Arn': 'string',
                'Path': 'string',
                'DefaultVersionId': 'string',
                'AttachmentCount': 123,
                'IsAttachable': True|False,
                'Description': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'UpdateDate': datetime(2015, 1, 1)
              }
            }
            Response Structure
            (dict) --Contains the response to a successful GetPolicy request.
            Policy (dict) --A structure containing details about the policy.
            PolicyName (string) --The friendly name (not ARN) identifying the policy.
            PolicyId (string) --The stable and unique string identifying the policy.
            For more information about IDs, see IAM Identifiers in the Using IAM guide.
            Arn (string) --The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
            For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            Path (string) --The path to the policy.
            For more information about paths, see IAM Identifiers in the Using IAM guide.
            DefaultVersionId (string) --The identifier for the version of the policy that is set as the default version.
            AttachmentCount (integer) --The number of entities (users, groups, and roles) that the policy is attached to.
            IsAttachable (boolean) --Specifies whether the policy can be attached to an IAM user, group, or role.
            Description (string) --A friendly description of the policy.
            This element is included in the response to the GetPolicy operation. It is not included in the response to the ListPolicies operation.
            CreateDate (datetime) --The date and time, in ISO 8601 date-time format , when the policy was created.
            UpdateDate (datetime) --The date and time, in ISO 8601 date-time format , when the policy was last updated.
            When a policy has only one version, this field contains the date and time when the policy was created. When a policy has more than one version, this field contains the date and time when the most recent policy version was created.
            
            
            
    :type PolicyArn: string
    """
    pass


def get_policy_version(PolicyArn=None, VersionId=None):
    """
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the managed policy that you want information about.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type PolicyArn: string
    :param VersionId: [REQUIRED]
            Identifies the policy version to retrieve.
            The regex pattern for this parameter is a string of characters that consists of the lowercase letter 'v' followed by one or two digits, and optionally followed by a period '.' and a string of letters and digits.
            
    :type VersionId: string
    """
    pass


def get_role(RoleName=None):
    """
    :param RoleName: [REQUIRED]
            The name of the IAM role to get information about.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            Return typedict
            ReturnsResponse Syntax{
              'Role': {
                'Path': 'string',
                'RoleName': 'string',
                'RoleId': 'string',
                'Arn': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'AssumeRolePolicyDocument': 'string'
              }
            }
            Response Structure
            (dict) --Contains the response to a successful GetRole request.
            Role (dict) --A structure containing details about the IAM role.
            Path (string) --The path to the role. For more information about paths, see IAM Identifiers in the Using IAM guide.
            RoleName (string) --The friendly name that identifies the role.
            RoleId (string) --The stable and unique string identifying the role. For more information about IDs, see IAM Identifiers in the Using IAM guide.
            Arn (string) --The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see IAM Identifiers in the Using IAM guide.
            CreateDate (datetime) --The date and time, in ISO 8601 date-time format , when the role was created.
            AssumeRolePolicyDocument (string) --The policy that grants an entity permission to assume the role.
            
            
            
    :type RoleName: string
    """
    pass


def get_role_policy(RoleName=None, PolicyName=None):
    """
    :param RoleName: [REQUIRED]
            The name of the role associated with the policy.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type RoleName: string
    :param PolicyName: [REQUIRED]
            The name of the policy document to get.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type PolicyName: string
    """
    pass


def get_saml_provider(SAMLProviderArn=None):
    """
    :param SAMLProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the SAML provider resource object in IAM to get information about.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            Return typedict
            ReturnsResponse Syntax{
              'SAMLMetadataDocument': 'string',
              'CreateDate': datetime(2015, 1, 1),
              'ValidUntil': datetime(2015, 1, 1)
            }
            Response Structure
            (dict) --Contains the response to a successful GetSAMLProvider request.
            SAMLMetadataDocument (string) --The XML metadata document that includes information about an identity provider.
            CreateDate (datetime) --The date and time when the SAML provider was created.
            ValidUntil (datetime) --The expiration date and time for the SAML provider.
            
            
    :type SAMLProviderArn: string
    """
    pass


def get_server_certificate(ServerCertificateName=None):
    """
    :param ServerCertificateName: [REQUIRED]
            The name of the server certificate you want to retrieve information about.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            Return typedict
            ReturnsResponse Syntax{
              'ServerCertificate': {
                'ServerCertificateMetadata': {
                  'Path': 'string',
                  'ServerCertificateName': 'string',
                  'ServerCertificateId': 'string',
                  'Arn': 'string',
                  'UploadDate': datetime(2015, 1, 1),
                  'Expiration': datetime(2015, 1, 1)
                },
                'CertificateBody': 'string',
                'CertificateChain': 'string'
              }
            }
            Response Structure
            (dict) --Contains the response to a successful GetServerCertificate request.
            ServerCertificate (dict) --A structure containing details about the server certificate.
            ServerCertificateMetadata (dict) --The meta information of the server certificate, such as its name, path, ID, and ARN.
            Path (string) --The path to the server certificate. For more information about paths, see IAM Identifiers in the Using IAM guide.
            ServerCertificateName (string) --The name that identifies the server certificate.
            ServerCertificateId (string) --The stable and unique string identifying the server certificate. For more information about IDs, see IAM Identifiers in the Using IAM guide.
            Arn (string) --The Amazon Resource Name (ARN) specifying the server certificate. For more information about ARNs and how to use them in policies, see IAM Identifiers in the Using IAM guide.
            UploadDate (datetime) --The date when the server certificate was uploaded.
            Expiration (datetime) --The date on which the certificate is set to expire.
            CertificateBody (string) --The contents of the public key certificate.
            CertificateChain (string) --The contents of the public key certificate chain.
            
            
            
    :type ServerCertificateName: string
    """
    pass


def get_ssh_public_key(UserName=None, SSHPublicKeyId=None, Encoding=None):
    """
    :param UserName: [REQUIRED]
            The name of the IAM user associated with the SSH public key.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param SSHPublicKeyId: [REQUIRED]
            The unique identifier for the SSH public key.
            The regex pattern for this parameter is a string of characters that can consist of any upper or lowercased letter or digit.
            
    :type SSHPublicKeyId: string
    :param Encoding: [REQUIRED]
            Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use SSH . To retrieve the public key in PEM format, use PEM .
            
    :type Encoding: string
    """
    pass


def get_user(UserName=None):
    """
    :param UserName: The name of the user to get information about.
            This parameter is optional. If it is not included, it defaults to the user making the request. The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            Return typedict
            ReturnsResponse Syntax{
              'User': {
                'Path': 'string',
                'UserName': 'string',
                'UserId': 'string',
                'Arn': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'PasswordLastUsed': datetime(2015, 1, 1)
              }
            }
            Response Structure
            (dict) --Contains the response to a successful GetUser request.
            User (dict) --A structure containing details about the IAM user.
            Path (string) --The path to the user. For more information about paths, see IAM Identifiers in the Using IAM guide.
            UserName (string) --The friendly name identifying the user.
            UserId (string) --The stable and unique string identifying the user. For more information about IDs, see IAM Identifiers in the Using IAM guide.
            Arn (string) --The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see IAM Identifiers in the Using IAM guide.
            CreateDate (datetime) --The date and time, in ISO 8601 date-time format , when the user was created.
            PasswordLastUsed (datetime) --The date and time, in ISO 8601 date-time format , when the user's password was last used to sign in to an AWS website. For a list of AWS websites that capture a user's last sign-in time, see the Credential Reports topic in the Using IAM guide. If a password is used more than once in a five-minute span, only the first use is returned in this field. This field is null (not present) when:
            The user does not have a password
            The password exists but has never been used (at least not since IAM started tracking this information on October 20th, 2014
            there is no sign-in data associated with the user
            This value is returned only in the GetUser and ListUsers actions.
            
            
            
    :type UserName: string
    """
    pass


def get_user_policy(UserName=None, PolicyName=None):
    """
    :param UserName: [REQUIRED]
            The name of the user who the policy is associated with.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param PolicyName: [REQUIRED]
            The name of the policy document to get.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type PolicyName: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_access_keys(UserName=None, Marker=None, MaxItems=None):
    """
    :param UserName: The name of the user.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_account_aliases(Marker=None, MaxItems=None):
    """
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_attached_group_policies(GroupName=None, PathPrefix=None, Marker=None, MaxItems=None):
    """
    :param GroupName: [REQUIRED]
            The name (friendly name, not ARN) of the group to list attached policies for.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type GroupName: string
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies.
            The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type PathPrefix: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_attached_role_policies(RoleName=None, PathPrefix=None, Marker=None, MaxItems=None):
    """
    :param RoleName: [REQUIRED]
            The name (friendly name, not ARN) of the role to list attached policies for.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type RoleName: string
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies.
            The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type PathPrefix: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_attached_user_policies(UserName=None, PathPrefix=None, Marker=None, MaxItems=None):
    """
    :param UserName: [REQUIRED]
            The name (friendly name, not ARN) of the user to list attached policies for.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies.
            The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type PathPrefix: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_entities_for_policy(PolicyArn=None, EntityFilter=None, PathPrefix=None, Marker=None, MaxItems=None):
    """
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy for which you want the versions.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type PolicyArn: string
    :param EntityFilter: The entity type to use for filtering the results.
            For example, when EntityFilter is Role , only the roles that are attached to the specified policy are returned. This parameter is optional. If it is not included, all attached entities (users, groups, and roles) are returned. The argument for this parameter must be one of the valid values listed below.
            
    :type EntityFilter: string
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all entities.
            The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type PathPrefix: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_group_policies(GroupName=None, Marker=None, MaxItems=None):
    """
    :param GroupName: [REQUIRED]
            The name of the group to list policies for.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type GroupName: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_groups(PathPrefix=None, Marker=None, MaxItems=None):
    """
    :param PathPrefix: The path prefix for filtering the results. For example, the prefix /division_abc/subdivision_xyz/ gets all groups whose path starts with /division_abc/subdivision_xyz/ .
            This parameter is optional. If it is not included, it defaults to a slash (/), listing all groups. The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type PathPrefix: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_groups_for_user(UserName=None, Marker=None, MaxItems=None):
    """
    :param UserName: [REQUIRED]
            The name of the user to list groups for.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_instance_profiles(PathPrefix=None, Marker=None, MaxItems=None):
    """
    :param PathPrefix: The path prefix for filtering the results. For example, the prefix /application_abc/component_xyz/ gets all instance profiles whose path starts with /application_abc/component_xyz/ .
            This parameter is optional. If it is not included, it defaults to a slash (/), listing all instance profiles. The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type PathPrefix: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_instance_profiles_for_role(RoleName=None, Marker=None, MaxItems=None):
    """
    :param RoleName: [REQUIRED]
            The name of the role to list instance profiles for.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type RoleName: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_mfa_devices(UserName=None, Marker=None, MaxItems=None):
    """
    :param UserName: The name of the user whose MFA devices you want to list.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_open_id_connect_providers():
    """
    """
    pass


def list_policies(Scope=None, OnlyAttached=None, PathPrefix=None, Marker=None, MaxItems=None):
    """
    :param Scope: The scope to use for filtering the results.
            To list only AWS managed policies, set Scope to AWS . To list only the customer managed policies in your AWS account, set Scope to Local .
            This parameter is optional. If it is not included, or if it is set to All , all policies are returned.
            
    :type Scope: string
    :param OnlyAttached: A flag to filter the results to only the attached policies.
            When OnlyAttached is true , the returned list contains only the policies that are attached to an IAM user, group, or role. When OnlyAttached is false , or when the parameter is not included, all policies are returned.
            
    :type OnlyAttached: boolean
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies. The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
    :type PathPrefix: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_policy_versions(PolicyArn=None, Marker=None, MaxItems=None):
    """
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy for which you want the versions.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type PolicyArn: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_role_policies(RoleName=None, Marker=None, MaxItems=None):
    """
    :param RoleName: [REQUIRED]
            The name of the role to list policies for.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type RoleName: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_roles(PathPrefix=None, Marker=None, MaxItems=None):
    """
    :param PathPrefix: The path prefix for filtering the results. For example, the prefix /application_abc/component_xyz/ gets all roles whose path starts with /application_abc/component_xyz/ .
            This parameter is optional. If it is not included, it defaults to a slash (/), listing all roles. The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type PathPrefix: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_saml_providers():
    """
    """
    pass


def list_server_certificates(PathPrefix=None, Marker=None, MaxItems=None):
    """
    :param PathPrefix: The path prefix for filtering the results. For example: /company/servercerts would get all server certificates for which the path starts with /company/servercerts .
            This parameter is optional. If it is not included, it defaults to a slash (/), listing all server certificates. The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type PathPrefix: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_signing_certificates(UserName=None, Marker=None, MaxItems=None):
    """
    :param UserName: The name of the IAM user whose signing certificates you want to examine.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_ssh_public_keys(UserName=None, Marker=None, MaxItems=None):
    """
    :param UserName: The name of the IAM user to list SSH public keys for. If none is specified, the UserName field is determined implicitly based on the AWS access key used to sign the request.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_user_policies(UserName=None, Marker=None, MaxItems=None):
    """
    :param UserName: [REQUIRED]
            The name of the user to list policies for.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_users(PathPrefix=None, Marker=None, MaxItems=None):
    """
    :param PathPrefix: The path prefix for filtering the results. For example: /division_abc/subdivision_xyz/ , which would get all user names whose path starts with /division_abc/subdivision_xyz/ .
            This parameter is optional. If it is not included, it defaults to a slash (/), listing all user names. The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type PathPrefix: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def list_virtual_mfa_devices(AssignmentStatus=None, Marker=None, MaxItems=None):
    """
    :param AssignmentStatus: The status (Unassigned or Assigned ) of the devices to list. If you do not specify an AssignmentStatus , the action defaults to Any which lists both assigned and unassigned virtual MFA devices.
    :type AssignmentStatus: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    """
    pass


def put_group_policy(GroupName=None, PolicyName=None, PolicyDocument=None):
    """
    :param GroupName: [REQUIRED]
            The name of the group to associate the policy with.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type GroupName: string
    :param PolicyName: [REQUIRED]
            The name of the policy document.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type PolicyName: string
    :param PolicyDocument: [REQUIRED]
            The policy document.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            
    :type PolicyDocument: string
    """
    pass


def put_role_policy(RoleName=None, PolicyName=None, PolicyDocument=None):
    """
    :param RoleName: [REQUIRED]
            The name of the role to associate the policy with.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type RoleName: string
    :param PolicyName: [REQUIRED]
            The name of the policy document.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type PolicyName: string
    :param PolicyDocument: [REQUIRED]
            The policy document.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            
    :type PolicyDocument: string
    """
    pass


def put_user_policy(UserName=None, PolicyName=None, PolicyDocument=None):
    """
    :param UserName: [REQUIRED]
            The name of the user to associate the policy with.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param PolicyName: [REQUIRED]
            The name of the policy document.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type PolicyName: string
    :param PolicyDocument: [REQUIRED]
            The policy document.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            
    :type PolicyDocument: string
    """
    pass


def remove_client_id_from_open_id_connect_provider(OpenIDConnectProviderArn=None, ClientID=None):
    """
    :param OpenIDConnectProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM OIDC provider resource to remove the client ID from. You can get a list of OIDC provider ARNs by using the ListOpenIDConnectProviders action.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type OpenIDConnectProviderArn: string
    :param ClientID: [REQUIRED]
            The client ID (also known as audience) to remove from the IAM OIDC provider resource. For more information about client IDs, see CreateOpenIDConnectProvider .
            
    :type ClientID: string
    """
    pass


def remove_role_from_instance_profile(InstanceProfileName=None, RoleName=None):
    """
    :param InstanceProfileName: [REQUIRED]
            The name of the instance profile to update.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type InstanceProfileName: string
    :param RoleName: [REQUIRED]
            The name of the role to remove.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type RoleName: string
    """
    pass


def remove_user_from_group(GroupName=None, UserName=None):
    """
    :param GroupName: [REQUIRED]
            The name of the group to update.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type GroupName: string
    :param UserName: [REQUIRED]
            The name of the user to remove.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    """
    pass


def resync_mfa_device(UserName=None, SerialNumber=None, AuthenticationCode1=None, AuthenticationCode2=None):
    """
    :param UserName: [REQUIRED]
            The name of the user whose MFA device you want to resynchronize.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param SerialNumber: [REQUIRED]
            Serial number that uniquely identifies the MFA device.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type SerialNumber: string
    :param AuthenticationCode1: [REQUIRED]
            An authentication code emitted by the device.
            The format for this parameter is a sequence of six digits.
            
    :type AuthenticationCode1: string
    :param AuthenticationCode2: [REQUIRED]
            A subsequent authentication code emitted by the device.
            The format for this parameter is a sequence of six digits.
            
    :type AuthenticationCode2: string
    """
    pass


def set_default_policy_version(PolicyArn=None, VersionId=None):
    """
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy whose default version you want to set.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type PolicyArn: string
    :param VersionId: [REQUIRED]
            The version of the policy to set as the default (operative) version.
            For more information about managed policy versions, see Versioning for Managed Policies in the IAM User Guide .
            
    :type VersionId: string
    """
    pass


def simulate_custom_policy(PolicyInputList=None, ActionNames=None, ResourceArns=None, ResourcePolicy=None,
                           ResourceOwner=None, CallerArn=None, ContextEntries=None, ResourceHandlingOption=None,
                           MaxItems=None, Marker=None):
    """
    :param PolicyInputList: [REQUIRED]
            A list of policy documents to include in the simulation. Each document is specified as a string containing the complete, valid JSON text of an IAM policy. Do not include any resource-based policies in this parameter. Any resource-based policy must be submitted with the ResourcePolicy parameter. The policies cannot be 'scope-down' policies, such as you could include in a call to GetFederationToken or one of the AssumeRole APIs to restrict what a user can do while using the temporary credentials.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            (string) --
            
    :type PolicyInputList: list
    :param ActionNames: [REQUIRED]
            A list of names of API actions to evaluate in the simulation. Each action is evaluated against each resource. Each action must include the service identifier, such as iam:CreateUser .
            (string) --
            
    :type ActionNames: list
    :param ResourceArns: A list of ARNs of AWS resources to include in the simulation. If this parameter is not provided then the value defaults to * (all resources). Each API in the ActionNames parameter is evaluated for each resource in this list. The simulation determines the access result (allowed or denied) of each combination and reports it in the response.
            The simulation does not automatically retrieve policies for the specified resources. If you want to include a resource policy in the simulation, then you must include the policy as a string in the ResourcePolicy parameter.
            If you include a ResourcePolicy , then it must be applicable to all of the resources included in the simulation or you receive an invalid input error.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            (string) --
            
    :type ResourceArns: list
    :param ResourcePolicy: A resource-based policy to include in the simulation provided as a string. Each resource in the simulation is treated as if it had this policy attached. You can include only one resource-based policy in a simulation.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            
    :type ResourcePolicy: string
    :param ResourceOwner: An AWS account ID that specifies the owner of any simulated resource that does not identify its owner in the resource ARN, such as an S3 bucket or object. If ResourceOwner is specified, it is also used as the account owner of any ResourcePolicy included in the simulation. If the ResourceOwner parameter is not specified, then the owner of the resources and the resource policy defaults to the account of the identity provided in CallerArn . This parameter is required only if you specify a resource-based policy and account that owns the resource is different from the account that owns the simulated calling user CallerArn .
    :type ResourceOwner: string
    :param CallerArn: The ARN of the IAM user that you want to use as the simulated caller of the APIs. CallerArn is required if you include a ResourcePolicy so that the policy's Principal element has a value to use in evaluating the policy.
            You can specify only the ARN of an IAM user. You cannot specify the ARN of an assumed role, federated user, or a service principal.
            
    :type CallerArn: string
    :param ContextEntries: A list of context keys and corresponding values for the simulation to use. Whenever a context key is evaluated in one of the simulated IAM permission policies, the corresponding value is supplied.
            (dict) --Contains information about a condition context key. It includes the name of the key and specifies the value (or values, if the context key supports multiple values) to use in the simulation. This information is used when evaluating the Condition elements of the input policies.
            This data type is used as an input parameter to `` SimulateCustomPolicy `` and `` SimulateCustomPolicy `` .
            ContextKeyName (string) --The full name of a condition context key, including the service prefix. For example, aws:SourceIp or s3:VersionId .
            ContextKeyValues (list) --The value (or values, if the condition context key supports multiple values) to provide to the simulation for use when the key is referenced by a Condition element in an input policy.
            (string) --
            ContextKeyType (string) --The data type of the value (or values) specified in the ContextKeyValues parameter.
            
            
    :type ContextEntries: list
    :param ResourceHandlingOption: Specifies the type of simulation to run. Different APIs that support resource-based policies require different combinations of resources. By specifying the type of simulation to run, you enable the policy simulator to enforce the presence of the required resources to ensure reliable simulation results. If your simulation does not match one of the following scenarios, then you can omit this parameter. The following list shows each of the supported scenario values and the resources that you must define to run the simulation.
            Each of the EC2 scenarios requires that you specify instance, image, and security-group resources. If your scenario includes an EBS volume, then you must specify that volume as a resource. If the EC2 scenario includes VPC, then you must supply the network-interface resource. If it includes an IP subnet, then you must specify the subnet resource. For more information on the EC2 scenario options, see Supported Platforms in the AWS EC2 User Guide .
            EC2-Classic-InstanceStore  instance, image, security-group
            EC2-Classic-EBS  instance, image, security-group, volume
            EC2-VPC-InstanceStore  instance, image, security-group, network-interface
            EC2-VPC-InstanceStore-Subnet  instance, image, security-group, network-interface, subnet
            EC2-VPC-EBS  instance, image, security-group, network-interface, volume
            EC2-VPC-EBS-Subnet  instance, image, security-group, network-interface, subnet, volume
            
    :type ResourceHandlingOption: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    """
    pass


def simulate_principal_policy(PolicySourceArn=None, PolicyInputList=None, ActionNames=None, ResourceArns=None,
                              ResourcePolicy=None, ResourceOwner=None, CallerArn=None, ContextEntries=None,
                              ResourceHandlingOption=None, MaxItems=None, Marker=None):
    """
    :param PolicySourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of a user, group, or role whose policies you want to include in the simulation. If you specify a user, group, or role, the simulation includes all policies that are associated with that entity. If you specify a user, the simulation also includes all policies that are attached to any groups the user belongs to.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type PolicySourceArn: string
    :param PolicyInputList: An optional list of additional policy documents to include in the simulation. Each document is specified as a string containing the complete, valid JSON text of an IAM policy.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            (string) --
            
    :type PolicyInputList: list
    :param ActionNames: [REQUIRED]
            A list of names of API actions to evaluate in the simulation. Each action is evaluated for each resource. Each action must include the service identifier, such as iam:CreateUser .
            (string) --
            
    :type ActionNames: list
    :param ResourceArns: A list of ARNs of AWS resources to include in the simulation. If this parameter is not provided then the value defaults to * (all resources). Each API in the ActionNames parameter is evaluated for each resource in this list. The simulation determines the access result (allowed or denied) of each combination and reports it in the response.
            The simulation does not automatically retrieve policies for the specified resources. If you want to include a resource policy in the simulation, then you must include the policy as a string in the ResourcePolicy parameter.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            (string) --
            
    :type ResourceArns: list
    :param ResourcePolicy: A resource-based policy to include in the simulation provided as a string. Each resource in the simulation is treated as if it had this policy attached. You can include only one resource-based policy in a simulation.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            
    :type ResourcePolicy: string
    :param ResourceOwner: An AWS account ID that specifies the owner of any simulated resource that does not identify its owner in the resource ARN, such as an S3 bucket or object. If ResourceOwner is specified, it is also used as the account owner of any ResourcePolicy included in the simulation. If the ResourceOwner parameter is not specified, then the owner of the resources and the resource policy defaults to the account of the identity provided in CallerArn . This parameter is required only if you specify a resource-based policy and account that owns the resource is different from the account that owns the simulated calling user CallerArn .
    :type ResourceOwner: string
    :param CallerArn: The ARN of the IAM user that you want to specify as the simulated caller of the APIs. If you do not specify a CallerArn , it defaults to the ARN of the user that you specify in PolicySourceArn , if you specified a user. If you include both a PolicySourceArn (for example, arn:aws:iam::123456789012:user/David ) and a CallerArn (for example, arn:aws:iam::123456789012:user/Bob ), the result is that you simulate calling the APIs as Bob, as if Bob had David's policies.
            You can specify only the ARN of an IAM user. You cannot specify the ARN of an assumed role, federated user, or a service principal.
            CallerArn is required if you include a ResourcePolicy and the PolicySourceArn is not the ARN for an IAM user. This is required so that the resource-based policy's Principal element has a value to use in evaluating the policy.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type CallerArn: string
    :param ContextEntries: A list of context keys and corresponding values for the simulation to use. Whenever a context key is evaluated in one of the simulated IAM permission policies, the corresponding value is supplied.
            (dict) --Contains information about a condition context key. It includes the name of the key and specifies the value (or values, if the context key supports multiple values) to use in the simulation. This information is used when evaluating the Condition elements of the input policies.
            This data type is used as an input parameter to `` SimulateCustomPolicy `` and `` SimulateCustomPolicy `` .
            ContextKeyName (string) --The full name of a condition context key, including the service prefix. For example, aws:SourceIp or s3:VersionId .
            ContextKeyValues (list) --The value (or values, if the condition context key supports multiple values) to provide to the simulation for use when the key is referenced by a Condition element in an input policy.
            (string) --
            ContextKeyType (string) --The data type of the value (or values) specified in the ContextKeyValues parameter.
            
            
    :type ContextEntries: list
    :param ResourceHandlingOption: Specifies the type of simulation to run. Different APIs that support resource-based policies require different combinations of resources. By specifying the type of simulation to run, you enable the policy simulator to enforce the presence of the required resources to ensure reliable simulation results. If your simulation does not match one of the following scenarios, then you can omit this parameter. The following list shows each of the supported scenario values and the resources that you must define to run the simulation.
            Each of the EC2 scenarios requires that you specify instance, image, and security-group resources. If your scenario includes an EBS volume, then you must specify that volume as a resource. If the EC2 scenario includes VPC, then you must supply the network-interface resource. If it includes an IP subnet, then you must specify the subnet resource. For more information on the EC2 scenario options, see Supported Platforms in the AWS EC2 User Guide .
            EC2-Classic-InstanceStore  instance, image, security-group
            EC2-Classic-EBS  instance, image, security-group, volume
            EC2-VPC-InstanceStore  instance, image, security-group, network-interface
            EC2-VPC-InstanceStore-Subnet  instance, image, security-group, network-interface, subnet
            EC2-VPC-EBS  instance, image, security-group, network-interface, volume
            EC2-VPC-EBS-Subnet  instance, image, security-group, network-interface, subnet, volume
            
    :type ResourceHandlingOption: string
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            This parameter is optional. If you do not include it, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            
    :type MaxItems: integer
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    :type Marker: string
    """
    pass


def update_access_key(UserName=None, AccessKeyId=None, Status=None):
    """
    :param UserName: The name of the user whose key you want to update.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param AccessKeyId: [REQUIRED]
            The access key ID of the secret access key you want to update.
            The regex pattern for this parameter is a string of characters that can consist of any upper or lowercased letter or digit.
            
    :type AccessKeyId: string
    :param Status: [REQUIRED]
            The status you want to assign to the secret access key. Active means the key can be used for API calls to AWS, while Inactive means the key cannot be used.
            
    :type Status: string
    """
    pass


def update_account_password_policy(MinimumPasswordLength=None, RequireSymbols=None, RequireNumbers=None,
                                   RequireUppercaseCharacters=None, RequireLowercaseCharacters=None,
                                   AllowUsersToChangePassword=None, MaxPasswordAge=None, PasswordReusePrevention=None,
                                   HardExpiry=None):
    """
    :param MinimumPasswordLength: The minimum number of characters allowed in an IAM user password.
            Default value: 6
            
    :type MinimumPasswordLength: integer
    :param RequireSymbols: Specifies whether IAM user passwords must contain at least one of the following non-alphanumeric characters:
            ! @ # $ % ^ amp; * ( ) _ + - = [ ] { } | '
            Default value: false
            
    :type RequireSymbols: boolean
    :param RequireNumbers: Specifies whether IAM user passwords must contain at least one numeric character (0 to 9).
            Default value: false
            
    :type RequireNumbers: boolean
    :param RequireUppercaseCharacters: Specifies whether IAM user passwords must contain at least one uppercase character from the ISO basic Latin alphabet (A to Z).
            Default value: false
            
    :type RequireUppercaseCharacters: boolean
    :param RequireLowercaseCharacters: Specifies whether IAM user passwords must contain at least one lowercase character from the ISO basic Latin alphabet (a to z).
            Default value: false
            
    :type RequireLowercaseCharacters: boolean
    :param AllowUsersToChangePassword: Allows all IAM users in your account to use the AWS Management Console to change their own passwords. For more information, see Letting IAM Users Change Their Own Passwords in the IAM User Guide .
            Default value: false
            
    :type AllowUsersToChangePassword: boolean
    :param MaxPasswordAge: The number of days that an IAM user password is valid. The default value of 0 means IAM user passwords never expire.
            Default value: 0
            
    :type MaxPasswordAge: integer
    :param PasswordReusePrevention: Specifies the number of previous passwords that IAM users are prevented from reusing. The default value of 0 means IAM users are not prevented from reusing previous passwords.
            Default value: 0
            
    :type PasswordReusePrevention: integer
    :param HardExpiry: Prevents IAM users from setting a new password after their password has expired.
            Default value: false
            
    :type HardExpiry: boolean
    """
    pass


def update_assume_role_policy(RoleName=None, PolicyDocument=None):
    """
    :param RoleName: [REQUIRED]
            The name of the role to update with the new policy.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type RoleName: string
    :param PolicyDocument: [REQUIRED]
            The policy that grants an entity permission to assume the role.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            
    :type PolicyDocument: string
    """
    pass


def update_group(GroupName=None, NewPath=None, NewGroupName=None):
    """
    :param GroupName: [REQUIRED]
            Name of the IAM group to update. If you're changing the name of the group, this is the original name.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type GroupName: string
    :param NewPath: New path for the IAM group. Only include this if changing the group's path.
            The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type NewPath: string
    :param NewGroupName: New name for the IAM group. Only include this if changing the group's name.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type NewGroupName: string
    """
    pass


def update_login_profile(UserName=None, Password=None, PasswordResetRequired=None):
    """
    :param UserName: [REQUIRED]
            The name of the user whose password you want to update.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param Password: The new password for the specified IAM user.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D). However, the format can be further restricted by the account administrator by setting a password policy on the AWS account. For more information, see UpdateAccountPasswordPolicy .
            
    :type Password: string
    :param PasswordResetRequired: Allows this new password to be used only once by requiring the specified IAM user to set a new password on next sign-in.
    :type PasswordResetRequired: boolean
    """
    pass


def update_open_id_connect_provider_thumbprint(OpenIDConnectProviderArn=None, ThumbprintList=None):
    """
    :param OpenIDConnectProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM OIDC provider resource object for which you want to update the thumbprint. You can get a list of OIDC provider ARNs by using the ListOpenIDConnectProviders action.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type OpenIDConnectProviderArn: string
    :param ThumbprintList: [REQUIRED]
            A list of certificate thumbprints that are associated with the specified IAM OpenID Connect provider. For more information, see CreateOpenIDConnectProvider .
            (string) --Contains a thumbprint for an identity provider's server certificate.
            The identity provider's server certificate thumbprint is the hex-encoded SHA-1 hash value of the self-signed X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string.
            
    :type ThumbprintList: list
    """
    pass


def update_saml_provider(SAMLMetadataDocument=None, SAMLProviderArn=None):
    """
    :param SAMLMetadataDocument: [REQUIRED]
            An XML document generated by an identity provider (IdP) that supports SAML 2.0. The document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that are received from the IdP. You must generate the metadata document using the identity management software that is used as your organization's IdP.
            
    :type SAMLMetadataDocument: string
    :param SAMLProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the SAML provider to update.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            
    :type SAMLProviderArn: string
    """
    pass


def update_server_certificate(ServerCertificateName=None, NewPath=None, NewServerCertificateName=None):
    """
    :param ServerCertificateName: [REQUIRED]
            The name of the server certificate that you want to update.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type ServerCertificateName: string
    :param NewPath: The new path for the server certificate. Include this only if you are updating the server certificate's path.
            The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type NewPath: string
    :param NewServerCertificateName: The new name for the server certificate. Include this only if you are updating the server certificate's name. The name of the certificate cannot contain any spaces.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type NewServerCertificateName: string
    """
    pass


def update_signing_certificate(UserName=None, CertificateId=None, Status=None):
    """
    :param UserName: The name of the IAM user the signing certificate belongs to.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param CertificateId: [REQUIRED]
            The ID of the signing certificate you want to update.
            The regex pattern for this parameter is a string of characters that can consist of any upper or lowercased letter or digit.
            
    :type CertificateId: string
    :param Status: [REQUIRED]
            The status you want to assign to the certificate. Active means the certificate can be used for API calls to AWS, while Inactive means the certificate cannot be used.
            
    :type Status: string
    """
    pass


def update_ssh_public_key(UserName=None, SSHPublicKeyId=None, Status=None):
    """
    :param UserName: [REQUIRED]
            The name of the IAM user associated with the SSH public key.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param SSHPublicKeyId: [REQUIRED]
            The unique identifier for the SSH public key.
            The regex pattern for this parameter is a string of characters that can consist of any upper or lowercased letter or digit.
            
    :type SSHPublicKeyId: string
    :param Status: [REQUIRED]
            The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used.
            
    :type Status: string
    """
    pass


def update_user(UserName=None, NewPath=None, NewUserName=None):
    """
    :param UserName: [REQUIRED]
            Name of the user to update. If you're changing the name of the user, this is the original user name.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param NewPath: New path for the IAM user. Include this parameter only if you're changing the user's path.
            The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            
    :type NewPath: string
    :param NewUserName: New name for the user. Include this parameter only if you're changing the user's name.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type NewUserName: string
    """
    pass


def upload_server_certificate(Path=None, ServerCertificateName=None, CertificateBody=None, PrivateKey=None,
                              CertificateChain=None):
    """
    :param Path: The path for the server certificate. For more information about paths, see IAM Identifiers in the IAM User Guide .
            This parameter is optional. If it is not included, it defaults to a slash (/). The regex pattern for this parameter is a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            Note
            If you are uploading a server certificate specifically for use with Amazon CloudFront distributions, you must specify a path using the --path option. The path must begin with /cloudfront and must include a trailing slash (for example, /cloudfront/test/ ).
            
    :type Path: string
    :param ServerCertificateName: [REQUIRED]
            The name for the server certificate. Do not include the path in this value. The name of the certificate cannot contain any spaces.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type ServerCertificateName: string
    :param CertificateBody: [REQUIRED]
            The contents of the public key certificate in PEM-encoded format.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            
    :type CertificateBody: string
    :param PrivateKey: [REQUIRED]
            The contents of the private key in PEM-encoded format.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            
    :type PrivateKey: string
    :param CertificateChain: The contents of the certificate chain. This is typically a concatenation of the PEM-encoded public key certificates of the chain.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            
    :type CertificateChain: string
    """
    pass


def upload_signing_certificate(UserName=None, CertificateBody=None):
    """
    :param UserName: The name of the user the signing certificate is for.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param CertificateBody: [REQUIRED]
            The contents of the signing certificate.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            
    :type CertificateBody: string
    """
    pass


def upload_ssh_public_key(UserName=None, SSHPublicKeyBody=None):
    """
    :param UserName: [REQUIRED]
            The name of the IAM user to associate the SSH public key with.
            The regex pattern for this parameter is a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            
    :type UserName: string
    :param SSHPublicKeyBody: [REQUIRED]
            The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.
            The regex pattern for this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range (u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            
    :type SSHPublicKeyBody: string
    """
    pass
