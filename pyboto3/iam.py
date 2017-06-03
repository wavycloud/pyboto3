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

def add_client_id_to_open_id_connect_provider(OpenIDConnectProviderArn=None, ClientID=None):
    """
    Adds a new client ID (also known as audience) to the list of client IDs already registered for the specified IAM OpenID Connect (OIDC) provider resource.
    This action is idempotent; it does not fail or return an error if you add an existing client ID to the provider.
    See also: AWS API Documentation
    
    Examples
    The following add-client-id-to-open-id-connect-provider command adds the client ID my-application-ID to the OIDC provider named server.example.com:
    Expected Output:
    
    :example: response = client.add_client_id_to_open_id_connect_provider(
        OpenIDConnectProviderArn='string',
        ClientID='string'
    )
    
    
    :type OpenIDConnectProviderArn: string
    :param OpenIDConnectProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM OpenID Connect (OIDC) provider resource to add the client ID to. You can get a list of OIDC provider ARNs by using the ListOpenIDConnectProviders action.
            

    :type ClientID: string
    :param ClientID: [REQUIRED]
            The client ID (also known as audience) to add to the IAM OpenID Connect provider resource.
            

    :return: response = client.add_client_id_to_open_id_connect_provider(
        ClientID='my-application-ID',
        OpenIDConnectProviderArn='arn:aws:iam::123456789012:oidc-provider/server.example.com',
    )
    
    print(response)
    
    
    """
    pass

def add_role_to_instance_profile(InstanceProfileName=None, RoleName=None):
    """
    Adds the specified IAM role to the specified instance profile. An instance profile can contain only one role, and this limit cannot be increased.
    For more information about roles, go to Working with Roles . For more information about instance profiles, go to About Instance Profiles .
    See also: AWS API Documentation
    
    Examples
    The following command adds the role named S3Access to the instance profile named Webserver:
    Expected Output:
    
    :example: response = client.add_role_to_instance_profile(
        InstanceProfileName='string',
        RoleName='string'
    )
    
    
    :type InstanceProfileName: string
    :param InstanceProfileName: [REQUIRED]
            The name of the instance profile to update.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name of the role to add.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
            

    :return: response = client.add_role_to_instance_profile(
        InstanceProfileName='Webserver',
        RoleName='S3Access',
    )
    
    print(response)
    
    
    """
    pass

def add_user_to_group(GroupName=None, UserName=None):
    """
    Adds the specified user to the specified group.
    See also: AWS API Documentation
    
    Examples
    The following command adds an IAM user named Bob to the IAM group named Admins:
    Expected Output:
    
    :example: response = client.add_user_to_group(
        GroupName='string',
        UserName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group to update.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user to add.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :return: response = client.add_user_to_group(
        GroupName='Admins',
        UserName='Bob',
    )
    
    print(response)
    
    
    """
    pass

def attach_group_policy(GroupName=None, PolicyArn=None):
    """
    Attaches the specified managed policy to the specified IAM group.
    You use this API to attach a managed policy to a group. To embed an inline policy in a group, use  PutGroupPolicy .
    For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command attaches the AWS managed policy named ReadOnlyAccess to the IAM group named Finance.
    Expected Output:
    
    :example: response = client.attach_group_policy(
        GroupName='string',
        PolicyArn='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name (friendly name, not ARN) of the group to attach the policy to.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy you want to attach.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :return: response = client.attach_group_policy(
        GroupName='Finance',
        PolicyArn='arn:aws:iam::aws:policy/ReadOnlyAccess',
    )
    
    print(response)
    
    
    """
    pass

def attach_role_policy(RoleName=None, PolicyArn=None):
    """
    Attaches the specified managed policy to the specified IAM role. When you attach a managed policy to a role, the managed policy becomes part of the role's permission (access) policy.
    Use this API to attach a managed policy to a role. To embed an inline policy in a role, use  PutRolePolicy . For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command attaches the AWS managed policy named ReadOnlyAccess to the IAM role named ReadOnlyRole.
    Expected Output:
    
    :example: response = client.attach_role_policy(
        RoleName='string',
        PolicyArn='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name (friendly name, not ARN) of the role to attach the policy to.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
            

    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy you want to attach.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :return: response = client.attach_role_policy(
        PolicyArn='arn:aws:iam::aws:policy/ReadOnlyAccess',
        RoleName='ReadOnlyRole',
    )
    
    print(response)
    
    
    """
    pass

def attach_user_policy(UserName=None, PolicyArn=None):
    """
    Attaches the specified managed policy to the specified user.
    You use this API to attach a managed policy to a user. To embed an inline policy in a user, use  PutUserPolicy .
    For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command attaches the AWS managed policy named AdministratorAccess to the IAM user named Alice.
    Expected Output:
    
    :example: response = client.attach_user_policy(
        UserName='string',
        PolicyArn='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name (friendly name, not ARN) of the IAM user to attach the policy to.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy you want to attach.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :return: response = client.attach_user_policy(
        PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess',
        UserName='Alice',
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

def change_password(OldPassword=None, NewPassword=None):
    """
    Changes the password of the IAM user who is calling this action. The root account password is not affected by this action.
    To change the password for a different user, see  UpdateLoginProfile . For more information about modifying passwords, see Managing Passwords in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command changes the password for the current IAM user.
    Expected Output:
    
    :example: response = client.change_password(
        OldPassword='string',
        NewPassword='string'
    )
    
    
    :type OldPassword: string
    :param OldPassword: [REQUIRED]
            The IAM user's current password.
            

    :type NewPassword: string
    :param NewPassword: [REQUIRED]
            The new password. The new password must conform to the AWS account's password policy, if one exists.
            The regex pattern used to validate this parameter is a string of characters consisting of almost any printable ASCII character from the space (u0020) through the end of the ASCII character range (u00FF). You can also include the tab (u0009), line feed (u000A), and carriage return (u000D) characters. Although any of these characters are valid in a password, note that many tools, such as the AWS Management Console, might restrict the ability to enter certain characters because they have special meaning within that tool.
            

    :return: response = client.change_password(
        NewPassword=']35d/{pB9Fo9wJ',
        OldPassword='3s0K_;xh4~8XXI',
    )
    
    print(response)
    
    
    """
    pass

def create_access_key(UserName=None):
    """
    Creates a new AWS secret access key and corresponding AWS access key ID for the specified user. The default status for new keys is Active .
    If you do not specify a user name, IAM determines the user name implicitly based on the AWS access key ID signing the request. Because this action works for access keys under the AWS account, you can use this action to manage root credentials even if the AWS account has no associated users.
    For information about limits on the number of keys you can create, see Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command creates an access key (access key ID and secret access key) for the IAM user named Bob.
    Expected Output:
    
    :example: response = client.create_access_key(
        UserName='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the IAM user that the new key will belong to.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :rtype: dict
    :return: {
        'AccessKey': {
            'UserName': 'string',
            'AccessKeyId': 'string',
            'Status': 'Active'|'Inactive',
            'SecretAccessKey': 'string',
            'CreateDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def create_account_alias(AccountAlias=None):
    """
    Creates an alias for your AWS account. For information about using an AWS account alias, see Using an Alias for Your AWS Account ID in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command associates the alias examplecorp to your AWS account.
    Expected Output:
    
    :example: response = client.create_account_alias(
        AccountAlias='string'
    )
    
    
    :type AccountAlias: string
    :param AccountAlias: [REQUIRED]
            The account alias to create.
            This parameter allows (per its regex pattern ) a string of characters consisting of lowercase letters, digits, and dashes. You cannot start or finish with a dash, nor can you have two dashes in a row.
            

    :return: response = client.create_account_alias(
        AccountAlias='examplecorp',
    )
    
    print(response)
    
    
    """
    pass

def create_group(Path=None, GroupName=None):
    """
    Creates a new group.
    For information about the number of groups you can create, see Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command creates an IAM group named Admins.
    Expected Output:
    
    :example: response = client.create_group(
        Path='string',
        GroupName='string'
    )
    
    
    :type Path: string
    :param Path: The path to the group. For more information about paths, see IAM Identifiers in the IAM User Guide .
            This parameter is optional. If it is not included, it defaults to a slash (/).
            This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group to create. Do not include the path in this value.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-. The group name must be unique within the account. Group names are not distinguished by case. For example, you cannot create groups named both 'ADMINS' and 'admins'.
            

    :rtype: dict
    :return: {
        'Group': {
            'Path': 'string',
            'GroupName': 'string',
            'GroupId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def create_instance_profile(InstanceProfileName=None, Path=None):
    """
    Creates a new instance profile. For information about instance profiles, go to About Instance Profiles .
    For information about the number of instance profiles you can create, see Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command creates an instance profile named Webserver that is ready to have a role attached and then be associated with an EC2 instance.
    Expected Output:
    
    :example: response = client.create_instance_profile(
        InstanceProfileName='string',
        Path='string'
    )
    
    
    :type InstanceProfileName: string
    :param InstanceProfileName: [REQUIRED]
            The name of the instance profile to create.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type Path: string
    :param Path: The path to the instance profile. For more information about paths, see IAM Identifiers in the IAM User Guide .
            This parameter is optional. If it is not included, it defaults to a slash (/).
            This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :rtype: dict
    :return: {
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
                    'AssumeRolePolicyDocument': 'string',
                    'Description': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def create_login_profile(UserName=None, Password=None, PasswordResetRequired=None):
    """
    Creates a password for the specified user, giving the user the ability to access AWS services through the AWS Management Console. For more information about managing passwords, see Managing Passwords in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command changes IAM user Bob's password and sets the flag that required Bob to change the password the next time he signs in.
    Expected Output:
    
    :example: response = client.create_login_profile(
        UserName='string',
        Password='string',
        PasswordResetRequired=True|False
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the IAM user to create a password for. The user must already exist.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type Password: string
    :param Password: [REQUIRED]
            The new password for the user.
            The regex pattern used to validate this parameter is a string of characters consisting of almost any printable ASCII character from the space (u0020) through the end of the ASCII character range (u00FF). You can also include the tab (u0009), line feed (u000A), and carriage return (u000D) characters. Although any of these characters are valid in a password, note that many tools, such as the AWS Management Console, might restrict the ability to enter certain characters because they have special meaning within that tool.
            

    :type PasswordResetRequired: boolean
    :param PasswordResetRequired: Specifies whether the user is required to set a new password on next sign-in.

    :rtype: dict
    :return: {
        'LoginProfile': {
            'UserName': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'PasswordResetRequired': True|False
        }
    }
    
    
    """
    pass

def create_open_id_connect_provider(Url=None, ClientIDList=None, ThumbprintList=None):
    """
    Creates an IAM entity to describe an identity provider (IdP) that supports OpenID Connect (OIDC) .
    The OIDC provider that you create with this operation can be used as a principal in a role's trust policy to establish a trust relationship between AWS and the OIDC provider.
    When you create the IAM OIDC provider, you specify the URL of the OIDC identity provider (IdP) to trust, a list of client IDs (also known as audiences) that identify the application or applications that are allowed to authenticate using the OIDC provider, and a list of thumbprints of the server certificate(s) that the IdP uses. You get all of this information from the OIDC IdP that you want to use for access to AWS.
    See also: AWS API Documentation
    
    Examples
    The following example defines a new OIDC provider in IAM with a client ID of my-application-id and pointing at the server with a URL of https://server.example.com.
    Expected Output:
    
    :example: response = client.create_open_id_connect_provider(
        Url='string',
        ClientIDList=[
            'string',
        ],
        ThumbprintList=[
            'string',
        ]
    )
    
    
    :type Url: string
    :param Url: [REQUIRED]
            The URL of the identity provider. The URL must begin with 'https://' and should correspond to the iss claim in the provider's OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a host name, like 'https://server.example.org' or 'https://example.com'.
            You cannot register the same provider multiple times in a single AWS account. If you try to submit a URL that has already been used for an OpenID Connect provider in the AWS account, you will get an error.
            

    :type ClientIDList: list
    :param ClientIDList: A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.)
            You can register multiple client IDs with the same provider. For example, you might have multiple applications that use the same OIDC provider. You cannot register more than 100 client IDs with a single IAM OIDC provider.
            There is no defined format for a client ID. The CreateOpenIDConnectProviderRequest action accepts client IDs up to 255 characters long.
            (string) --
            

    :type ThumbprintList: list
    :param ThumbprintList: [REQUIRED]
            A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificate(s). Typically this list includes only one entry. However, IAM lets you have up to five thumbprints for an OIDC provider. This lets you maintain multiple thumbprints if the identity provider is rotating certificates.
            The server certificate thumbprint is the hex-encoded SHA-1 hash value of the X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string.
            You must provide at least one thumbprint when creating an IAM OIDC provider. For example, if the OIDC provider is server.example.com and the provider stores its keys at 'https://keys.server.example.com/openid-connect', the thumbprint string would be the hex-encoded SHA-1 hash value of the certificate used by https://keys.server.example.com.
            For more information about obtaining the OIDC provider's thumbprint, see Obtaining the Thumbprint for an OpenID Connect Provider in the IAM User Guide .
            (string) --Contains a thumbprint for an identity provider's server certificate.
            The identity provider's server certificate thumbprint is the hex-encoded SHA-1 hash value of the self-signed X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string.
            

    :rtype: dict
    :return: {
        'OpenIDConnectProviderArn': 'string'
    }
    
    
    """
    pass

def create_policy(PolicyName=None, Path=None, PolicyDocument=None, Description=None):
    """
    Creates a new managed policy for your AWS account.
    This operation creates a policy version with a version identifier of v1 and sets v1 as the policy's default version. For more information about policy versions, see Versioning for Managed Policies in the IAM User Guide .
    For more information about managed policies in general, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_policy(
        PolicyName='string',
        Path='string',
        PolicyDocument='string',
        Description='string'
    )
    
    
    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The friendly name of the policy.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type Path: string
    :param Path: The path for the policy.
            For more information about paths, see IAM Identifiers in the IAM User Guide .
            This parameter is optional. If it is not included, it defaults to a slash (/).
            This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type PolicyDocument: string
    :param PolicyDocument: [REQUIRED]
            The JSON policy document that you want to use as the content for the new policy.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            

    :type Description: string
    :param Description: A friendly description of the policy.
            Typically used to store information about the permissions defined in the policy. For example, 'Grants access to production DynamoDB tables.'
            The policy description is immutable. After a value is assigned, it cannot be changed.
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def create_policy_version(PolicyArn=None, PolicyDocument=None, SetAsDefault=None):
    """
    Creates a new version of the specified managed policy. To update a managed policy, you create a new policy version. A managed policy can have up to five versions. If the policy has five versions, you must delete an existing version using  DeletePolicyVersion before you create a new version.
    Optionally, you can set the new version as the policy's default version. The default version is the version that is in effect for the IAM users, groups, and roles to which the policy is attached.
    For more information about managed policy versions, see Versioning for Managed Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_policy_version(
        PolicyArn='string',
        PolicyDocument='string',
        SetAsDefault=True|False
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy to which you want to add a new version.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :type PolicyDocument: string
    :param PolicyDocument: [REQUIRED]
            The JSON policy document that you want to use as the content for this new version of the policy.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            

    :type SetAsDefault: boolean
    :param SetAsDefault: Specifies whether to set this version as the policy's default version.
            When this parameter is true , the new policy version becomes the operative version; that is, the version that is in effect for the IAM users, groups, and roles that the policy is attached to.
            For more information about managed policy versions, see Versioning for Managed Policies in the IAM User Guide .
            

    :rtype: dict
    :return: {
        'PolicyVersion': {
            'Document': 'string',
            'VersionId': 'string',
            'IsDefaultVersion': True|False,
            'CreateDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def create_role(Path=None, RoleName=None, AssumeRolePolicyDocument=None, Description=None):
    """
    Creates a new role for your AWS account. For more information about roles, go to Working with Roles . For information about limitations on role names and the number of roles you can create, go to Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command creates a role named Test-Role and attaches a trust policy to it that is provided as a URL-encoded JSON string.
    Expected Output:
    
    :example: response = client.create_role(
        Path='string',
        RoleName='string',
        AssumeRolePolicyDocument='string',
        Description='string'
    )
    
    
    :type Path: string
    :param Path: The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide .
            This parameter is optional. If it is not included, it defaults to a slash (/).
            This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name of the role to create.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
            Role names are not distinguished by case. For example, you cannot create roles named both 'PRODROLE' and 'prodrole'.
            

    :type AssumeRolePolicyDocument: string
    :param AssumeRolePolicyDocument: [REQUIRED]
            The trust relationship policy document that grants an entity permission to assume the role.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            

    :type Description: string
    :param Description: A customer-provided description of the role.

    :rtype: dict
    :return: {
        'Role': {
            'Path': 'string',
            'RoleName': 'string',
            'RoleId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'AssumeRolePolicyDocument': 'string',
            'Description': 'string'
        }
    }
    
    
    """
    pass

def create_saml_provider(SAMLMetadataDocument=None, Name=None):
    """
    Creates an IAM resource that describes an identity provider (IdP) that supports SAML 2.0.
    The SAML provider resource that you create with this operation can be used as a principal in an IAM role's trust policy to enable federated users who sign-in using the SAML IdP to assume the role. You can create an IAM role that supports Web-based single sign-on (SSO) to the AWS Management Console or one that supports API access to AWS.
    When you create the SAML provider resource, you upload an a SAML metadata document that you get from your IdP and that includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that the IdP sends. You must generate the metadata document using the identity management software that is used as your organization's IdP.
    For more information, see Enabling SAML 2.0 Federated Users to Access the AWS Management Console and About SAML 2.0-based Federation in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_saml_provider(
        SAMLMetadataDocument='string',
        Name='string'
    )
    
    
    :type SAMLMetadataDocument: string
    :param SAMLMetadataDocument: [REQUIRED]
            An XML document generated by an identity provider (IdP) that supports SAML 2.0. The document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that are received from the IdP. You must generate the metadata document using the identity management software that is used as your organization's IdP.
            For more information, see About SAML 2.0-based Federation in the IAM User Guide
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the provider to create.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :rtype: dict
    :return: {
        'SAMLProviderArn': 'string'
    }
    
    
    """
    pass

def create_service_linked_role(AWSServiceName=None, Description=None, CustomSuffix=None):
    """
    Creates an IAM role that is linked to a specific AWS service. The service controls the attached policies and when the role can be deleted. This helps ensure that the service is not broken by an unexpectedly changed or deleted role, which could put your AWS resources into an unknown state. Allowing the service to control the role helps improve service stability and proper cleanup when a service and its role are no longer needed.
    The name of the role is autogenerated by combining the string that you specify for the AWSServiceName parameter with the string that you specify for the CustomSuffix parameter. The resulting name must be unique in your account or the request fails.
    To attach a policy to this service-linked role, you must make the request using the AWS service that depends on this role.
    See also: AWS API Documentation
    
    
    :example: response = client.create_service_linked_role(
        AWSServiceName='string',
        Description='string',
        CustomSuffix='string'
    )
    
    
    :type AWSServiceName: string
    :param AWSServiceName: [REQUIRED]
            The AWS service to which this role is attached. You use a string similar to a URL but without the http:// in front. For example: elasticbeanstalk.amazonaws.com
            

    :type Description: string
    :param Description: The description of the role.

    :type CustomSuffix: string
    :param CustomSuffix: A string that you provide, which is combined with the service name to form the complete role name. If you make multiple requests for the same service, then you must supply a different CustomSuffix for each request. Otherwise the request fails with a duplicate role name error. For example, you could add -1 or -debug to the suffix.

    :rtype: dict
    :return: {
        'Role': {
            'Path': 'string',
            'RoleName': 'string',
            'RoleId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'AssumeRolePolicyDocument': 'string',
            'Description': 'string'
        }
    }
    
    
    """
    pass

def create_service_specific_credential(UserName=None, ServiceName=None):
    """
    Generates a set of credentials consisting of a user name and password that can be used to access the service specified in the request. These credentials are generated by IAM, and can be used only for the specified service.
    You can have a maximum of two sets of service-specific credentials for each supported service per user.
    The only supported service at this time is AWS CodeCommit.
    You can reset the password to a new service-generated value by calling  ResetServiceSpecificCredential .
    For more information about service-specific credentials, see Using IAM with AWS CodeCommit: Git Credentials, SSH Keys, and AWS Access Keys in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_service_specific_credential(
        UserName='string',
        ServiceName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the IAM user that is to be associated with the credentials. The new service-specific credentials have the same permissions as the associated user except that they can be used only to access the specified service.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type ServiceName: string
    :param ServiceName: [REQUIRED]
            The name of the AWS service that is to be associated with the credentials. The service you specify here is the only service that can be accessed using these credentials.
            

    :rtype: dict
    :return: {
        'ServiceSpecificCredential': {
            'CreateDate': datetime(2015, 1, 1),
            'ServiceName': 'string',
            'ServiceUserName': 'string',
            'ServicePassword': 'string',
            'ServiceSpecificCredentialId': 'string',
            'UserName': 'string',
            'Status': 'Active'|'Inactive'
        }
    }
    
    
    """
    pass

def create_user(Path=None, UserName=None):
    """
    Creates a new IAM user for your AWS account.
    For information about limitations on the number of IAM users you can create, see Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following create-user command creates an IAM user named Bob in the current account.
    Expected Output:
    
    :example: response = client.create_user(
        Path='string',
        UserName='string'
    )
    
    
    :type Path: string
    :param Path: The path for the user name. For more information about paths, see IAM Identifiers in the IAM User Guide .
            This parameter is optional. If it is not included, it defaults to a slash (/).
            This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user to create.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-. User names are not distinguished by case. For example, you cannot create users named both 'TESTUSER' and 'testuser'.
            

    :rtype: dict
    :return: {
        'User': {
            'Path': 'string',
            'UserName': 'string',
            'UserId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'PasswordLastUsed': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    The user does not have a password
    The password exists but has never been used (at least not since IAM started tracking this information on October 20th, 2014
    there is no sign-in data associated with the user
    
    """
    pass

def create_virtual_mfa_device(Path=None, VirtualMFADeviceName=None):
    """
    Creates a new virtual MFA device for the AWS account. After creating the virtual MFA, use  EnableMFADevice to attach the MFA device to an IAM user. For more information about creating and working with virtual MFA devices, go to Using a Virtual MFA Device in the IAM User Guide .
    For information about limits on the number of MFA devices you can create, see Limitations on Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_virtual_mfa_device(
        Path='string',
        VirtualMFADeviceName='string'
    )
    
    
    :type Path: string
    :param Path: The path for the virtual MFA device. For more information about paths, see IAM Identifiers in the IAM User Guide .
            This parameter is optional. If it is not included, it defaults to a slash (/).
            This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type VirtualMFADeviceName: string
    :param VirtualMFADeviceName: [REQUIRED]
            The name of the virtual MFA device. Use with path to uniquely identify a virtual MFA device.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :rtype: dict
    :return: {
        'VirtualMFADevice': {
            'SerialNumber': 'string',
            'Base32StringSeed': b'bytes',
            'QRCodePNG': b'bytes',
            'User': {
                'Path': 'string',
                'UserName': 'string',
                'UserId': 'string',
                'Arn': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'PasswordLastUsed': datetime(2015, 1, 1)
            },
            'EnableDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    The user does not have a password
    The password exists but has never been used (at least not since IAM started tracking this information on October 20th, 2014
    there is no sign-in data associated with the user
    
    """
    pass

def deactivate_mfa_device(UserName=None, SerialNumber=None):
    """
    Deactivates the specified MFA device and removes it from association with the user name for which it was originally enabled.
    For more information about creating and working with virtual MFA devices, go to Using a Virtual MFA Device in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.deactivate_mfa_device(
        UserName='string',
        SerialNumber='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user whose MFA device you want to deactivate.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type SerialNumber: string
    :param SerialNumber: [REQUIRED]
            The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@:/-
            

    """
    pass

def delete_access_key(UserName=None, AccessKeyId=None):
    """
    Deletes the access key pair associated with the specified IAM user.
    If you do not specify a user name, IAM determines the user name implicitly based on the AWS access key ID signing the request. Because this action works for access keys under the AWS account, you can use this action to manage root credentials even if the AWS account has no associated users.
    See also: AWS API Documentation
    
    Examples
    The following command deletes one access key (access key ID and secret access key) assigned to the IAM user named Bob.
    Expected Output:
    
    :example: response = client.delete_access_key(
        UserName='string',
        AccessKeyId='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the user whose access key pair you want to delete.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type AccessKeyId: string
    :param AccessKeyId: [REQUIRED]
            The access key ID for the access key ID and secret access key you want to delete.
            This parameter allows (per its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
            

    :return: response = client.delete_access_key(
        AccessKeyId='AKIDPMS9RO4H3FEXAMPLE',
        UserName='Bob',
    )
    
    print(response)
    
    
    """
    pass

def delete_account_alias(AccountAlias=None):
    """
    Deletes the specified AWS account alias. For information about using an AWS account alias, see Using an Alias for Your AWS Account ID in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command removes the alias mycompany from the current AWS account:
    Expected Output:
    
    :example: response = client.delete_account_alias(
        AccountAlias='string'
    )
    
    
    :type AccountAlias: string
    :param AccountAlias: [REQUIRED]
            The name of the account alias to delete.
            This parameter allows (per its regex pattern ) a string of characters consisting of lowercase letters, digits, and dashes. You cannot start or finish with a dash, nor can you have two dashes in a row.
            

    :return: response = client.delete_account_alias(
        AccountAlias='mycompany',
    )
    
    print(response)
    
    
    """
    pass

def delete_account_password_policy():
    """
    Deletes the password policy for the AWS account. There are no parameters.
    See also: AWS API Documentation
    
    Examples
    The following command removes the password policy from the current AWS account:
    Expected Output:
    
    :example: response = client.delete_account_password_policy()
    
    
    :return: response = client.delete_account_password_policy(
    )
    
    print(response)
    
    
    """
    pass

def delete_group(GroupName=None):
    """
    Deletes the specified IAM group. The group must not contain any users or have any attached policies.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_group(
        GroupName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the IAM group to delete.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    """
    pass

def delete_group_policy(GroupName=None, PolicyName=None):
    """
    Deletes the specified inline policy that is embedded in the specified IAM group.
    A group can also have managed policies attached to it. To detach a managed policy from a group, use  DetachGroupPolicy . For more information about policies, refer to Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command deletes the policy named ExamplePolicy from the group named Admins:
    Expected Output:
    
    :example: response = client.delete_group_policy(
        GroupName='string',
        PolicyName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name (friendly name, not ARN) identifying the group that the policy is embedded in.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name identifying the policy document to delete.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :return: response = client.delete_group_policy(
        GroupName='Admins',
        PolicyName='ExamplePolicy',
    )
    
    print(response)
    
    
    """
    pass

def delete_instance_profile(InstanceProfileName=None):
    """
    Deletes the specified instance profile. The instance profile must not have an associated role.
    For more information about instance profiles, go to About Instance Profiles .
    See also: AWS API Documentation
    
    Examples
    The following command deletes the instance profile named ExampleInstanceProfile
    Expected Output:
    
    :example: response = client.delete_instance_profile(
        InstanceProfileName='string'
    )
    
    
    :type InstanceProfileName: string
    :param InstanceProfileName: [REQUIRED]
            The name of the instance profile to delete.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :return: response = client.delete_instance_profile(
        InstanceProfileName='ExampleInstanceProfile',
    )
    
    print(response)
    
    
    """
    pass

def delete_login_profile(UserName=None):
    """
    Deletes the password for the specified IAM user, which terminates the user's ability to access AWS services through the AWS Management Console.
    See also: AWS API Documentation
    
    Examples
    The following command deletes the password for the IAM user named Bob.
    Expected Output:
    
    :example: response = client.delete_login_profile(
        UserName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user whose password you want to delete.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :return: response = client.delete_login_profile(
        UserName='Bob',
    )
    
    print(response)
    
    
    """
    pass

def delete_open_id_connect_provider(OpenIDConnectProviderArn=None):
    """
    Deletes an OpenID Connect identity provider (IdP) resource object in IAM.
    Deleting an IAM OIDC provider resource does not update any roles that reference the provider as a principal in their trust policies. Any attempt to assume a role that references a deleted provider fails.
    This action is idempotent; it does not fail or return an error if you call the action for a provider that does not exist.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_open_id_connect_provider(
        OpenIDConnectProviderArn='string'
    )
    
    
    :type OpenIDConnectProviderArn: string
    :param OpenIDConnectProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM OpenID Connect provider resource object to delete. You can get a list of OpenID Connect provider resource ARNs by using the ListOpenIDConnectProviders action.
            

    """
    pass

def delete_policy(PolicyArn=None):
    """
    Deletes the specified managed policy.
    Before you can delete a managed policy, you must first detach the policy from all users, groups, and roles that it is attached to, and you must delete all of the policy's versions. The following steps describe the process for deleting a managed policy:
    For information about managed policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_policy(
        PolicyArn='string'
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy you want to delete.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    """
    pass

def delete_policy_version(PolicyArn=None, VersionId=None):
    """
    Deletes the specified version from the specified managed policy.
    You cannot delete the default version from a policy using this API. To delete the default version from a policy, use  DeletePolicy . To find out which version of a policy is marked as the default version, use  ListPolicyVersions .
    For information about versions for managed policies, see Versioning for Managed Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_policy_version(
        PolicyArn='string',
        VersionId='string'
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy from which you want to delete a version.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :type VersionId: string
    :param VersionId: [REQUIRED]
            The policy version to delete.
            This parameter allows (per its regex pattern ) a string of characters that consists of the lowercase letter 'v' followed by one or two digits, and optionally followed by a period '.' and a string of letters and digits.
            For more information about managed policy versions, see Versioning for Managed Policies in the IAM User Guide .
            

    """
    pass

def delete_role(RoleName=None):
    """
    Deletes the specified role. The role must not have any policies attached. For more information about roles, go to Working with Roles .
    See also: AWS API Documentation
    
    Examples
    The following command removes the role named Test-Role.
    Expected Output:
    
    :example: response = client.delete_role(
        RoleName='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name of the role to delete.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
            

    :return: response = client.delete_role(
        RoleName='Test-Role',
    )
    
    print(response)
    
    
    """
    pass

def delete_role_policy(RoleName=None, PolicyName=None):
    """
    Deletes the specified inline policy that is embedded in the specified IAM role.
    A role can also have managed policies attached to it. To detach a managed policy from a role, use  DetachRolePolicy . For more information about policies, refer to Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command removes the policy named ExamplePolicy from the role named Test-Role.
    Expected Output:
    
    :example: response = client.delete_role_policy(
        RoleName='string',
        PolicyName='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name (friendly name, not ARN) identifying the role that the policy is embedded in.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the inline policy to delete from the specified IAM role.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :return: response = client.delete_role_policy(
        PolicyName='ExamplePolicy',
        RoleName='Test-Role',
    )
    
    print(response)
    
    
    """
    pass

def delete_saml_provider(SAMLProviderArn=None):
    """
    Deletes a SAML provider resource in IAM.
    Deleting the provider resource from IAM does not update any roles that reference the SAML provider resource's ARN as a principal in their trust policies. Any attempt to assume a role that references a non-existent provider resource ARN fails.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_saml_provider(
        SAMLProviderArn='string'
    )
    
    
    :type SAMLProviderArn: string
    :param SAMLProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the SAML provider to delete.
            

    """
    pass

def delete_server_certificate(ServerCertificateName=None):
    """
    Deletes the specified server certificate.
    For more information about working with server certificates, including a list of AWS services that can use the server certificates that you manage with IAM, go to Working with Server Certificates in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_server_certificate(
        ServerCertificateName='string'
    )
    
    
    :type ServerCertificateName: string
    :param ServerCertificateName: [REQUIRED]
            The name of the server certificate you want to delete.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    """
    pass

def delete_service_specific_credential(UserName=None, ServiceSpecificCredentialId=None):
    """
    Deletes the specified service-specific credential.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_service_specific_credential(
        UserName='string',
        ServiceSpecificCredentialId='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the IAM user associated with the service-specific credential. If this value is not specified, then the operation assumes the user whose credentials are used to call the operation.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type ServiceSpecificCredentialId: string
    :param ServiceSpecificCredentialId: [REQUIRED]
            The unique identifier of the service-specific credential. You can get this value by calling ListServiceSpecificCredentials .
            This parameter allows (per its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
            

    """
    pass

def delete_signing_certificate(UserName=None, CertificateId=None):
    """
    Deletes a signing certificate associated with the specified IAM user.
    If you do not specify a user name, IAM determines the user name implicitly based on the AWS access key ID signing the request. Because this action works for access keys under the AWS account, you can use this action to manage root credentials even if the AWS account has no associated IAM users.
    See also: AWS API Documentation
    
    Examples
    The following command deletes the specified signing certificate for the IAM user named Anika.
    Expected Output:
    
    :example: response = client.delete_signing_certificate(
        UserName='string',
        CertificateId='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the user the signing certificate belongs to.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type CertificateId: string
    :param CertificateId: [REQUIRED]
            The ID of the signing certificate to delete.
            The format of this parameter, as described by its regex pattern, is a string of characters that can be upper- or lower-cased letters or digits.
            

    :return: response = client.delete_signing_certificate(
        CertificateId='TA7SMP42TDN5Z26OBPJE7EXAMPLE',
        UserName='Anika',
    )
    
    print(response)
    
    
    """
    pass

def delete_ssh_public_key(UserName=None, SSHPublicKeyId=None):
    """
    Deletes the specified SSH public key.
    The SSH public key deleted by this action is used only for authenticating the associated IAM user to an AWS CodeCommit repository. For more information about using SSH keys to authenticate to an AWS CodeCommit repository, see Set up AWS CodeCommit for SSH Connections in the AWS CodeCommit User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_ssh_public_key(
        UserName='string',
        SSHPublicKeyId='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the IAM user associated with the SSH public key.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type SSHPublicKeyId: string
    :param SSHPublicKeyId: [REQUIRED]
            The unique identifier for the SSH public key.
            This parameter allows (per its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
            

    """
    pass

def delete_user(UserName=None):
    """
    Deletes the specified IAM user. The user must not belong to any groups or have any access keys, signing certificates, or attached policies.
    See also: AWS API Documentation
    
    Examples
    The following command removes the IAM user named Bob from the current account.
    Expected Output:
    
    :example: response = client.delete_user(
        UserName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user to delete.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :return: response = client.delete_user(
        UserName='Bob',
    )
    
    print(response)
    
    
    """
    pass

def delete_user_policy(UserName=None, PolicyName=None):
    """
    Deletes the specified inline policy that is embedded in the specified IAM user.
    A user can also have managed policies attached to it. To detach a managed policy from a user, use  DetachUserPolicy . For more information about policies, refer to Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following delete-user-policy command removes the specified policy from the IAM user named Juan:
    Expected Output:
    
    :example: response = client.delete_user_policy(
        UserName='string',
        PolicyName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name (friendly name, not ARN) identifying the user that the policy is embedded in.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name identifying the policy document to delete.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :return: response = client.delete_user_policy(
        PolicyName='ExamplePolicy',
        UserName='Juan',
    )
    
    print(response)
    
    
    """
    pass

def delete_virtual_mfa_device(SerialNumber=None):
    """
    Deletes a virtual MFA device.
    See also: AWS API Documentation
    
    Examples
    The following delete-virtual-mfa-device command removes the specified MFA device from the current AWS account.
    Expected Output:
    
    :example: response = client.delete_virtual_mfa_device(
        SerialNumber='string'
    )
    
    
    :type SerialNumber: string
    :param SerialNumber: [REQUIRED]
            The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the same as the ARN.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@:/-
            

    :return: response = client.delete_virtual_mfa_device(
        SerialNumber='arn:aws:iam::123456789012:mfa/ExampleName',
    )
    
    print(response)
    
    
    """
    pass

def detach_group_policy(GroupName=None, PolicyArn=None):
    """
    Removes the specified managed policy from the specified IAM group.
    A group can also have inline policies embedded with it. To delete an inline policy, use the  DeleteGroupPolicy API. For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.detach_group_policy(
        GroupName='string',
        PolicyArn='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name (friendly name, not ARN) of the IAM group to detach the policy from.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy you want to detach.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    """
    pass

def detach_role_policy(RoleName=None, PolicyArn=None):
    """
    Removes the specified managed policy from the specified role.
    A role can also have inline policies embedded with it. To delete an inline policy, use the  DeleteRolePolicy API. For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.detach_role_policy(
        RoleName='string',
        PolicyArn='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name (friendly name, not ARN) of the IAM role to detach the policy from.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
            

    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy you want to detach.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    """
    pass

def detach_user_policy(UserName=None, PolicyArn=None):
    """
    Removes the specified managed policy from the specified user.
    A user can also have inline policies embedded with it. To delete an inline policy, use the  DeleteUserPolicy API. For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.detach_user_policy(
        UserName='string',
        PolicyArn='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name (friendly name, not ARN) of the IAM user to detach the policy from.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy you want to detach.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    """
    pass

def enable_mfa_device(UserName=None, SerialNumber=None, AuthenticationCode1=None, AuthenticationCode2=None):
    """
    Enables the specified MFA device and associates it with the specified IAM user. When enabled, the MFA device is required for every subsequent login by the IAM user associated with the device.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_mfa_device(
        UserName='string',
        SerialNumber='string',
        AuthenticationCode1='string',
        AuthenticationCode2='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the IAM user for whom you want to enable the MFA device.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type SerialNumber: string
    :param SerialNumber: [REQUIRED]
            The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@:/-
            

    :type AuthenticationCode1: string
    :param AuthenticationCode1: [REQUIRED]
            An authentication code emitted by the device.
            The format for this parameter is a string of 6 digits.
            Warning
            Submit your request immediately after generating the authentication codes. If you generate the codes and then wait too long to submit the request, the MFA device successfully associates with the user but the MFA device becomes out of sync. This happens because time-based one-time passwords (TOTP) expire after a short period of time. If this happens, you can resync the device .
            

    :type AuthenticationCode2: string
    :param AuthenticationCode2: [REQUIRED]
            A subsequent authentication code emitted by the device.
            The format for this parameter is a string of 6 digits.
            Warning
            Submit your request immediately after generating the authentication codes. If you generate the codes and then wait too long to submit the request, the MFA device successfully associates with the user but the MFA device becomes out of sync. This happens because time-based one-time passwords (TOTP) expire after a short period of time. If this happens, you can resync the device .
            

    """
    pass

def generate_credential_report():
    """
    Generates a credential report for the AWS account. For more information about the credential report, see Getting Credential Reports in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.generate_credential_report()
    
    
    :rtype: dict
    :return: {
        'State': 'STARTED'|'INPROGRESS'|'COMPLETE',
        'Description': 'string'
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

def get_access_key_last_used(AccessKeyId=None):
    """
    Retrieves information about when the specified access key was last used. The information includes the date and time of last use, along with the AWS service and region that were specified in the last request made with that key.
    See also: AWS API Documentation
    
    
    :example: response = client.get_access_key_last_used(
        AccessKeyId='string'
    )
    
    
    :type AccessKeyId: string
    :param AccessKeyId: [REQUIRED]
            The identifier of an access key.
            This parameter allows (per its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
            

    :rtype: dict
    :return: {
        'UserName': 'string',
        'AccessKeyLastUsed': {
            'LastUsedDate': datetime(2015, 1, 1),
            'ServiceName': 'string',
            'Region': 'string'
        }
    }
    
    
    :returns: 
    The user does not have an access key.
    An access key exists but has never been used, at least not since IAM started tracking this information on April 22nd, 2015.
    There is no sign-in data associated with the user
    
    """
    pass

def get_account_authorization_details(Filter=None, MaxItems=None, Marker=None):
    """
    Retrieves information about all IAM users, groups, roles, and policies in your AWS account, including their relationships to one another. Use this API to obtain a snapshot of the configuration of IAM permissions (users, groups, roles, and policies) in your account.
    You can optionally filter the results using the Filter parameter. You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.get_account_authorization_details(
        Filter=[
            'User'|'Role'|'Group'|'LocalManagedPolicy'|'AWSManagedPolicy',
        ],
        MaxItems=123,
        Marker='string'
    )
    
    
    :type Filter: list
    :param Filter: A list of entity types used to filter the results. Only the entities that match the types you specify are included in the output. Use the value LocalManagedPolicy to include customer managed policies.
            The format for this parameter is a comma-separated (if more than one) list of strings. Each string value in the list must be one of the valid values listed below.
            (string) --
            

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :rtype: dict
    :return: {
        'UserDetailList': [
            {
                'Path': 'string',
                'UserName': 'string',
                'UserId': 'string',
                'Arn': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'UserPolicyList': [
                    {
                        'PolicyName': 'string',
                        'PolicyDocument': 'string'
                    },
                ],
                'GroupList': [
                    'string',
                ],
                'AttachedManagedPolicies': [
                    {
                        'PolicyName': 'string',
                        'PolicyArn': 'string'
                    },
                ]
            },
        ],
        'GroupDetailList': [
            {
                'Path': 'string',
                'GroupName': 'string',
                'GroupId': 'string',
                'Arn': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'GroupPolicyList': [
                    {
                        'PolicyName': 'string',
                        'PolicyDocument': 'string'
                    },
                ],
                'AttachedManagedPolicies': [
                    {
                        'PolicyName': 'string',
                        'PolicyArn': 'string'
                    },
                ]
            },
        ],
        'RoleDetailList': [
            {
                'Path': 'string',
                'RoleName': 'string',
                'RoleId': 'string',
                'Arn': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'AssumeRolePolicyDocument': 'string',
                'InstanceProfileList': [
                    {
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
                                'AssumeRolePolicyDocument': 'string',
                                'Description': 'string'
                            },
                        ]
                    },
                ],
                'RolePolicyList': [
                    {
                        'PolicyName': 'string',
                        'PolicyDocument': 'string'
                    },
                ],
                'AttachedManagedPolicies': [
                    {
                        'PolicyName': 'string',
                        'PolicyArn': 'string'
                    },
                ]
            },
        ],
        'Policies': [
            {
                'PolicyName': 'string',
                'PolicyId': 'string',
                'Arn': 'string',
                'Path': 'string',
                'DefaultVersionId': 'string',
                'AttachmentCount': 123,
                'IsAttachable': True|False,
                'Description': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'UpdateDate': datetime(2015, 1, 1),
                'PolicyVersionList': [
                    {
                        'Document': 'string',
                        'VersionId': 'string',
                        'IsDefaultVersion': True|False,
                        'CreateDate': datetime(2015, 1, 1)
                    },
                ]
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_account_password_policy():
    """
    Retrieves the password policy for the AWS account. For more information about using a password policy, go to Managing an IAM Password Policy .
    See also: AWS API Documentation
    
    Examples
    The following command displays details about the password policy for the current AWS account.
    Expected Output:
    
    :example: response = client.get_account_password_policy()
    
    
    :rtype: dict
    :return: {
        'PasswordPolicy': {
            'MinimumPasswordLength': 123,
            'RequireSymbols': True|False,
            'RequireNumbers': True|False,
            'RequireUppercaseCharacters': True|False,
            'RequireLowercaseCharacters': True|False,
            'AllowUsersToChangePassword': True|False,
            'ExpirePasswords': True|False,
            'MaxPasswordAge': 123,
            'PasswordReusePrevention': 123,
            'HardExpiry': True|False
        }
    }
    
    
    """
    pass

def get_account_summary():
    """
    Retrieves information about IAM entity usage and IAM quotas in the AWS account.
    For information about limitations on IAM entities, see Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command returns information about the IAM entity quotas and usage in the current AWS account.
    Expected Output:
    
    :example: response = client.get_account_summary()
    
    
    :rtype: dict
    :return: {
        'SummaryMap': {
            'string': 123
        }
    }
    
    
    """
    pass

def get_context_keys_for_custom_policy(PolicyInputList=None):
    """
    Gets a list of all of the context keys referenced in the input policies. The policies are supplied as a list of one or more strings. To get the context keys from policies associated with an IAM user, group, or role, use  GetContextKeysForPrincipalPolicy .
    Context keys are variables maintained by AWS and its services that provide details about the context of an API query request, and can be evaluated by testing against a value specified in an IAM policy. Use GetContextKeysForCustomPolicy to understand what key names and values you must supply when you call  SimulateCustomPolicy . Note that all parameters are shown in unencoded form here for clarity, but must be URL encoded to be included as a part of a real HTML request.
    See also: AWS API Documentation
    
    
    :example: response = client.get_context_keys_for_custom_policy(
        PolicyInputList=[
            'string',
        ]
    )
    
    
    :type PolicyInputList: list
    :param PolicyInputList: [REQUIRED]
            A list of policies for which you want the list of context keys referenced in those policies. Each document is specified as a string containing the complete, valid JSON text of an IAM policy.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            (string) --
            

    :rtype: dict
    :return: {
        'ContextKeyNames': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_context_keys_for_principal_policy(PolicySourceArn=None, PolicyInputList=None):
    """
    Gets a list of all of the context keys referenced in all of the IAM policies attached to the specified IAM entity. The entity can be an IAM user, group, or role. If you specify a user, then the request also includes all of the policies attached to groups that the user is a member of.
    You can optionally include a list of one or more additional policies, specified as strings. If you want to include only a list of policies by string, use  GetContextKeysForCustomPolicy instead.
    Context keys are variables maintained by AWS and its services that provide details about the context of an API query request, and can be evaluated by testing against a value in an IAM policy. Use  GetContextKeysForPrincipalPolicy to understand what key names and values you must supply when you call  SimulatePrincipalPolicy .
    See also: AWS API Documentation
    
    
    :example: response = client.get_context_keys_for_principal_policy(
        PolicySourceArn='string',
        PolicyInputList=[
            'string',
        ]
    )
    
    
    :type PolicySourceArn: string
    :param PolicySourceArn: [REQUIRED]
            The ARN of a user, group, or role whose policies contain the context keys that you want listed. If you specify a user, the list includes context keys that are found in all policies attached to the user as well as to all groups that the user is a member of. If you pick a group or a role, then it includes only those context keys that are found in policies attached to that entity. Note that all parameters are shown in unencoded form here for clarity, but must be URL encoded to be included as a part of a real HTML request.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :type PolicyInputList: list
    :param PolicyInputList: An optional list of additional policies for which you want the list of context keys that are referenced.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            (string) --
            

    :rtype: dict
    :return: {
        'ContextKeyNames': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_credential_report():
    """
    Retrieves a credential report for the AWS account. For more information about the credential report, see Getting Credential Reports in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_credential_report()
    
    
    :rtype: dict
    :return: {
        'Content': b'bytes',
        'ReportFormat': 'text/csv',
        'GeneratedTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def get_group(GroupName=None, Marker=None, MaxItems=None):
    """
    Returns a list of IAM users that are in the specified IAM group. You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.get_group(
        GroupName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'Group': {
            'Path': 'string',
            'GroupName': 'string',
            'GroupId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1)
        },
        'Users': [
            {
                'Path': 'string',
                'UserName': 'string',
                'UserId': 'string',
                'Arn': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'PasswordLastUsed': datetime(2015, 1, 1)
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    CreateUser
    GetUser
    ListUsers
    
    """
    pass

def get_group_policy(GroupName=None, PolicyName=None):
    """
    Retrieves the specified inline policy document that is embedded in the specified IAM group.
    An IAM group can also have managed policies attached to it. To retrieve a managed policy document that is attached to a group, use  GetPolicy to determine the policy's default version, then use  GetPolicyVersion to retrieve the policy document.
    For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_group_policy(
        GroupName='string',
        PolicyName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group the policy is associated with.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the policy document to get.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :rtype: dict
    :return: {
        'GroupName': 'string',
        'PolicyName': 'string',
        'PolicyDocument': 'string'
    }
    
    
    """
    pass

def get_instance_profile(InstanceProfileName=None):
    """
    Retrieves information about the specified instance profile, including the instance profile's path, GUID, ARN, and role. For more information about instance profiles, see About Instance Profiles in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command gets information about the instance profile named ExampleInstanceProfile.
    Expected Output:
    
    :example: response = client.get_instance_profile(
        InstanceProfileName='string'
    )
    
    
    :type InstanceProfileName: string
    :param InstanceProfileName: [REQUIRED]
            The name of the instance profile to get information about.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :rtype: dict
    :return: {
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
                    'AssumeRolePolicyDocument': 'string',
                    'Description': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def get_login_profile(UserName=None):
    """
    Retrieves the user name and password-creation date for the specified IAM user. If the user has not been assigned a password, the action returns a 404 (NoSuchEntity ) error.
    See also: AWS API Documentation
    
    Examples
    The following command gets information about the password for the IAM user named Anika.
    Expected Output:
    
    :example: response = client.get_login_profile(
        UserName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user whose login profile you want to retrieve.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :rtype: dict
    :return: {
        'LoginProfile': {
            'UserName': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'PasswordResetRequired': True|False
        }
    }
    
    
    """
    pass

def get_open_id_connect_provider(OpenIDConnectProviderArn=None):
    """
    Returns information about the specified OpenID Connect (OIDC) provider resource object in IAM.
    See also: AWS API Documentation
    
    
    :example: response = client.get_open_id_connect_provider(
        OpenIDConnectProviderArn='string'
    )
    
    
    :type OpenIDConnectProviderArn: string
    :param OpenIDConnectProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the OIDC provider resource object in IAM to get information for. You can get a list of OIDC provider resource ARNs by using the ListOpenIDConnectProviders action.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :rtype: dict
    :return: {
        'Url': 'string',
        'ClientIDList': [
            'string',
        ],
        'ThumbprintList': [
            'string',
        ],
        'CreateDate': datetime(2015, 1, 1)
    }
    
    
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

def get_policy(PolicyArn=None):
    """
    Retrieves information about the specified managed policy, including the policy's default version and the total number of IAM users, groups, and roles to which the policy is attached. To retrieve the list of the specific users, groups, and roles that the policy is attached to, use the  ListEntitiesForPolicy API. This API returns metadata about the policy. To retrieve the actual policy document for a specific version of the policy, use  GetPolicyVersion .
    This API retrieves information about managed policies. To retrieve information about an inline policy that is embedded with an IAM user, group, or role, use the  GetUserPolicy ,  GetGroupPolicy , or  GetRolePolicy API.
    For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_policy(
        PolicyArn='string'
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the managed policy that you want information about.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def get_policy_version(PolicyArn=None, VersionId=None):
    """
    Retrieves information about the specified version of the specified managed policy, including the policy document.
    To list the available versions for a policy, use  ListPolicyVersions .
    This API retrieves information about managed policies. To retrieve information about an inline policy that is embedded in a user, group, or role, use the  GetUserPolicy ,  GetGroupPolicy , or  GetRolePolicy API.
    For more information about the types of policies, see Managed Policies and Inline Policies in the IAM User Guide .
    For more information about managed policy versions, see Versioning for Managed Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_policy_version(
        PolicyArn='string',
        VersionId='string'
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the managed policy that you want information about.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :type VersionId: string
    :param VersionId: [REQUIRED]
            Identifies the policy version to retrieve.
            This parameter allows (per its regex pattern ) a string of characters that consists of the lowercase letter 'v' followed by one or two digits, and optionally followed by a period '.' and a string of letters and digits.
            

    :rtype: dict
    :return: {
        'PolicyVersion': {
            'Document': 'string',
            'VersionId': 'string',
            'IsDefaultVersion': True|False,
            'CreateDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_role(RoleName=None):
    """
    Retrieves information about the specified role, including the role's path, GUID, ARN, and the role's trust policy that grants permission to assume the role. For more information about roles, see Working with Roles .
    See also: AWS API Documentation
    
    Examples
    The following command gets information about the role named Test-Role.
    Expected Output:
    
    :example: response = client.get_role(
        RoleName='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name of the IAM role to get information about.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
            

    :rtype: dict
    :return: {
        'Role': {
            'Path': 'string',
            'RoleName': 'string',
            'RoleId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'AssumeRolePolicyDocument': 'string',
            'Description': 'string'
        }
    }
    
    
    """
    pass

def get_role_policy(RoleName=None, PolicyName=None):
    """
    Retrieves the specified inline policy document that is embedded with the specified IAM role.
    An IAM role can also have managed policies attached to it. To retrieve a managed policy document that is attached to a role, use  GetPolicy to determine the policy's default version, then use  GetPolicyVersion to retrieve the policy document.
    For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    For more information about roles, see Using Roles to Delegate Permissions and Federate Identities .
    See also: AWS API Documentation
    
    
    :example: response = client.get_role_policy(
        RoleName='string',
        PolicyName='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name of the role associated with the policy.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the policy document to get.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :rtype: dict
    :return: {
        'RoleName': 'string',
        'PolicyName': 'string',
        'PolicyDocument': 'string'
    }
    
    
    """
    pass

def get_saml_provider(SAMLProviderArn=None):
    """
    Returns the SAML provider metadocument that was uploaded when the IAM SAML provider resource object was created or updated.
    See also: AWS API Documentation
    
    
    :example: response = client.get_saml_provider(
        SAMLProviderArn='string'
    )
    
    
    :type SAMLProviderArn: string
    :param SAMLProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the SAML provider resource object in IAM to get information about.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :rtype: dict
    :return: {
        'SAMLMetadataDocument': 'string',
        'CreateDate': datetime(2015, 1, 1),
        'ValidUntil': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def get_server_certificate(ServerCertificateName=None):
    """
    Retrieves information about the specified server certificate stored in IAM.
    For more information about working with server certificates, including a list of AWS services that can use the server certificates that you manage with IAM, go to Working with Server Certificates in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_server_certificate(
        ServerCertificateName='string'
    )
    
    
    :type ServerCertificateName: string
    :param ServerCertificateName: [REQUIRED]
            The name of the server certificate you want to retrieve information about.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def get_ssh_public_key(UserName=None, SSHPublicKeyId=None, Encoding=None):
    """
    Retrieves the specified SSH public key, including metadata about the key.
    The SSH public key retrieved by this action is used only for authenticating the associated IAM user to an AWS CodeCommit repository. For more information about using SSH keys to authenticate to an AWS CodeCommit repository, see Set up AWS CodeCommit for SSH Connections in the AWS CodeCommit User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_ssh_public_key(
        UserName='string',
        SSHPublicKeyId='string',
        Encoding='SSH'|'PEM'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the IAM user associated with the SSH public key.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type SSHPublicKeyId: string
    :param SSHPublicKeyId: [REQUIRED]
            The unique identifier for the SSH public key.
            This parameter allows (per its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
            

    :type Encoding: string
    :param Encoding: [REQUIRED]
            Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use SSH . To retrieve the public key in PEM format, use PEM .
            

    :rtype: dict
    :return: {
        'SSHPublicKey': {
            'UserName': 'string',
            'SSHPublicKeyId': 'string',
            'Fingerprint': 'string',
            'SSHPublicKeyBody': 'string',
            'Status': 'Active'|'Inactive',
            'UploadDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_user(UserName=None):
    """
    Retrieves information about the specified IAM user, including the user's creation date, path, unique ID, and ARN.
    If you do not specify a user name, IAM determines the user name implicitly based on the AWS access key ID used to sign the request to this API.
    See also: AWS API Documentation
    
    Examples
    The following command gets information about the IAM user named Bob.
    Expected Output:
    
    :example: response = client.get_user(
        UserName='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the user to get information about.
            This parameter is optional. If it is not included, it defaults to the user making the request. This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :rtype: dict
    :return: {
        'User': {
            'Path': 'string',
            'UserName': 'string',
            'UserId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'PasswordLastUsed': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_user_policy(UserName=None, PolicyName=None):
    """
    Retrieves the specified inline policy document that is embedded in the specified IAM user.
    An IAM user can also have managed policies attached to it. To retrieve a managed policy document that is attached to a user, use  GetPolicy to determine the policy's default version, then use  GetPolicyVersion to retrieve the policy document.
    For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_user_policy(
        UserName='string',
        PolicyName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user who the policy is associated with.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the policy document to get.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :rtype: dict
    :return: {
        'UserName': 'string',
        'PolicyName': 'string',
        'PolicyDocument': 'string'
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_access_keys(UserName=None, Marker=None, MaxItems=None):
    """
    Returns information about the access key IDs associated with the specified IAM user. If there are none, the action returns an empty list.
    Although each user is limited to a small number of keys, you can still paginate the results using the MaxItems and Marker parameters.
    If the UserName field is not specified, the UserName is determined implicitly based on the AWS access key ID used to sign the request. Because this action works for access keys under the AWS account, you can use this action to manage root credentials even if the AWS account has no associated users.
    See also: AWS API Documentation
    
    Examples
    The following command lists the access keys IDs for the IAM user named Alice.
    Expected Output:
    
    :example: response = client.list_access_keys(
        UserName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: The name of the user.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'AccessKeyMetadata': [
            {
                'UserName': 'string',
                'AccessKeyId': 'string',
                'Status': 'Active'|'Inactive',
                'CreateDate': datetime(2015, 1, 1)
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    """
    pass

def list_account_aliases(Marker=None, MaxItems=None):
    """
    Lists the account alias associated with the AWS account (Note: you can have only one). For information about using an AWS account alias, see Using an Alias for Your AWS Account ID in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command lists the aliases for the current account.
    Expected Output:
    
    :example: response = client.list_account_aliases(
        Marker='string',
        MaxItems=123
    )
    
    
    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'AccountAliases': [
            'string',
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_attached_group_policies(GroupName=None, PathPrefix=None, Marker=None, MaxItems=None):
    """
    Lists all managed policies that are attached to the specified IAM group.
    An IAM group can also have inline policies embedded with it. To list the inline policies for a group, use the  ListGroupPolicies API. For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    You can paginate the results using the MaxItems and Marker parameters. You can use the PathPrefix parameter to limit the list of policies to only those matching the specified path prefix. If there are no policies attached to the specified group (or none that match the specified path prefix), the action returns an empty list.
    See also: AWS API Documentation
    
    
    :example: response = client.list_attached_group_policies(
        GroupName='string',
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name (friendly name, not ARN) of the group to list attached policies for.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies.
            This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'AttachedPolicies': [
            {
                'PolicyName': 'string',
                'PolicyArn': 'string'
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    """
    pass

def list_attached_role_policies(RoleName=None, PathPrefix=None, Marker=None, MaxItems=None):
    """
    Lists all managed policies that are attached to the specified IAM role.
    An IAM role can also have inline policies embedded with it. To list the inline policies for a role, use the  ListRolePolicies API. For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    You can paginate the results using the MaxItems and Marker parameters. You can use the PathPrefix parameter to limit the list of policies to only those matching the specified path prefix. If there are no policies attached to the specified role (or none that match the specified path prefix), the action returns an empty list.
    See also: AWS API Documentation
    
    
    :example: response = client.list_attached_role_policies(
        RoleName='string',
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name (friendly name, not ARN) of the role to list attached policies for.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
            

    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies.
            This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'AttachedPolicies': [
            {
                'PolicyName': 'string',
                'PolicyArn': 'string'
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    """
    pass

def list_attached_user_policies(UserName=None, PathPrefix=None, Marker=None, MaxItems=None):
    """
    Lists all managed policies that are attached to the specified IAM user.
    An IAM user can also have inline policies embedded with it. To list the inline policies for a user, use the  ListUserPolicies API. For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    You can paginate the results using the MaxItems and Marker parameters. You can use the PathPrefix parameter to limit the list of policies to only those matching the specified path prefix. If there are no policies attached to the specified group (or none that match the specified path prefix), the action returns an empty list.
    See also: AWS API Documentation
    
    
    :example: response = client.list_attached_user_policies(
        UserName='string',
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name (friendly name, not ARN) of the user to list attached policies for.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies.
            This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'AttachedPolicies': [
            {
                'PolicyName': 'string',
                'PolicyArn': 'string'
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    """
    pass

def list_entities_for_policy(PolicyArn=None, EntityFilter=None, PathPrefix=None, Marker=None, MaxItems=None):
    """
    Lists all IAM users, groups, and roles that the specified managed policy is attached to.
    You can use the optional EntityFilter parameter to limit the results to a particular type of entity (users, groups, or roles). For example, to list only the roles that are attached to the specified policy, set EntityFilter to Role .
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.list_entities_for_policy(
        PolicyArn='string',
        EntityFilter='User'|'Role'|'Group'|'LocalManagedPolicy'|'AWSManagedPolicy',
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy for which you want the versions.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :type EntityFilter: string
    :param EntityFilter: The entity type to use for filtering the results.
            For example, when EntityFilter is Role , only the roles that are attached to the specified policy are returned. This parameter is optional. If it is not included, all attached entities (users, groups, and roles) are returned. The argument for this parameter must be one of the valid values listed below.
            

    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all entities.
            This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'PolicyGroups': [
            {
                'GroupName': 'string',
                'GroupId': 'string'
            },
        ],
        'PolicyUsers': [
            {
                'UserName': 'string',
                'UserId': 'string'
            },
        ],
        'PolicyRoles': [
            {
                'RoleName': 'string',
                'RoleId': 'string'
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    """
    pass

def list_group_policies(GroupName=None, Marker=None, MaxItems=None):
    """
    Lists the names of the inline policies that are embedded in the specified IAM group.
    An IAM group can also have managed policies attached to it. To list the managed policies that are attached to a group, use  ListAttachedGroupPolicies . For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    You can paginate the results using the MaxItems and Marker parameters. If there are no inline policies embedded with the specified group, the action returns an empty list.
    See also: AWS API Documentation
    
    Examples
    The following command lists the names of in-line policies that are embedded in the IAM group named Admins.
    Expected Output:
    
    :example: response = client.list_group_policies(
        GroupName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group to list policies for.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'PolicyNames': [
            'string',
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_groups(PathPrefix=None, Marker=None, MaxItems=None):
    """
    Lists the IAM groups that have the specified path prefix.
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    Examples
    The following command lists the IAM groups in the current account:
    Expected Output:
    
    :example: response = client.list_groups(
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. For example, the prefix /division_abc/subdivision_xyz/ gets all groups whose path starts with /division_abc/subdivision_xyz/ .
            This parameter is optional. If it is not included, it defaults to a slash (/), listing all groups. This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'Groups': [
            {
                'Path': 'string',
                'GroupName': 'string',
                'GroupId': 'string',
                'Arn': 'string',
                'CreateDate': datetime(2015, 1, 1)
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    CreateGroup
    GetGroup
    ListGroups
    
    """
    pass

def list_groups_for_user(UserName=None, Marker=None, MaxItems=None):
    """
    Lists the IAM groups that the specified IAM user belongs to.
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    Examples
    The following command displays the groups that the IAM user named Bob belongs to.
    Expected Output:
    
    :example: response = client.list_groups_for_user(
        UserName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user to list groups for.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'Groups': [
            {
                'Path': 'string',
                'GroupName': 'string',
                'GroupId': 'string',
                'Arn': 'string',
                'CreateDate': datetime(2015, 1, 1)
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    CreateGroup
    GetGroup
    ListGroups
    
    """
    pass

def list_instance_profiles(PathPrefix=None, Marker=None, MaxItems=None):
    """
    Lists the instance profiles that have the specified path prefix. If there are none, the action returns an empty list. For more information about instance profiles, go to About Instance Profiles .
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.list_instance_profiles(
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. For example, the prefix /application_abc/component_xyz/ gets all instance profiles whose path starts with /application_abc/component_xyz/ .
            This parameter is optional. If it is not included, it defaults to a slash (/), listing all instance profiles. This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'InstanceProfiles': [
            {
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
                        'AssumeRolePolicyDocument': 'string',
                        'Description': 'string'
                    },
                ]
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    CreateInstanceProfile
    GetInstanceProfile
    ListInstanceProfiles
    ListInstanceProfilesForRole
    
    """
    pass

def list_instance_profiles_for_role(RoleName=None, Marker=None, MaxItems=None):
    """
    Lists the instance profiles that have the specified associated IAM role. If there are none, the action returns an empty list. For more information about instance profiles, go to About Instance Profiles .
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.list_instance_profiles_for_role(
        RoleName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name of the role to list instance profiles for.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'InstanceProfiles': [
            {
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
                        'AssumeRolePolicyDocument': 'string',
                        'Description': 'string'
                    },
                ]
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    CreateInstanceProfile
    GetInstanceProfile
    ListInstanceProfiles
    ListInstanceProfilesForRole
    
    """
    pass

def list_mfa_devices(UserName=None, Marker=None, MaxItems=None):
    """
    Lists the MFA devices for an IAM user. If the request includes a IAM user name, then this action lists all the MFA devices associated with the specified user. If you do not specify a user name, IAM determines the user name implicitly based on the AWS access key ID signing the request for this API.
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.list_mfa_devices(
        UserName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: The name of the user whose MFA devices you want to list.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'MFADevices': [
            {
                'UserName': 'string',
                'SerialNumber': 'string',
                'EnableDate': datetime(2015, 1, 1)
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    """
    pass

def list_open_id_connect_providers():
    """
    Lists information about the IAM OpenID Connect (OIDC) provider resource objects defined in the AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_open_id_connect_providers()
    
    
    :rtype: dict
    :return: {
        'OpenIDConnectProviderList': [
            {
                'Arn': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_policies(Scope=None, OnlyAttached=None, PathPrefix=None, Marker=None, MaxItems=None):
    """
    Lists all the managed policies that are available in your AWS account, including your own customer-defined managed policies and all AWS managed policies.
    You can filter the list of policies that is returned using the optional OnlyAttached , Scope , and PathPrefix parameters. For example, to list only the customer managed policies in your AWS account, set Scope to Local . To list only AWS managed policies, set Scope to AWS .
    You can paginate the results using the MaxItems and Marker parameters.
    For more information about managed policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.list_policies(
        Scope='All'|'AWS'|'Local',
        OnlyAttached=True|False,
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type Scope: string
    :param Scope: The scope to use for filtering the results.
            To list only AWS managed policies, set Scope to AWS . To list only the customer managed policies in your AWS account, set Scope to Local .
            This parameter is optional. If it is not included, or if it is set to All , all policies are returned.
            

    :type OnlyAttached: boolean
    :param OnlyAttached: A flag to filter the results to only the attached policies.
            When OnlyAttached is true , the returned list contains only the policies that are attached to an IAM user, group, or role. When OnlyAttached is false , or when the parameter is not included, all policies are returned.
            

    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies. This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'Policies': [
            {
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
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    """
    pass

def list_policy_versions(PolicyArn=None, Marker=None, MaxItems=None):
    """
    Lists information about the versions of the specified managed policy, including the version that is currently set as the policy's default version.
    For more information about managed policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.list_policy_versions(
        PolicyArn='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy for which you want the versions.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'Versions': [
            {
                'Document': 'string',
                'VersionId': 'string',
                'IsDefaultVersion': True|False,
                'CreateDate': datetime(2015, 1, 1)
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    """
    pass

def list_role_policies(RoleName=None, Marker=None, MaxItems=None):
    """
    Lists the names of the inline policies that are embedded in the specified IAM role.
    An IAM role can also have managed policies attached to it. To list the managed policies that are attached to a role, use  ListAttachedRolePolicies . For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    You can paginate the results using the MaxItems and Marker parameters. If there are no inline policies embedded with the specified role, the action returns an empty list.
    See also: AWS API Documentation
    
    
    :example: response = client.list_role_policies(
        RoleName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name of the role to list policies for.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'PolicyNames': [
            'string',
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_roles(PathPrefix=None, Marker=None, MaxItems=None):
    """
    Lists the IAM roles that have the specified path prefix. If there are none, the action returns an empty list. For more information about roles, go to Working with Roles .
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.list_roles(
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. For example, the prefix /application_abc/component_xyz/ gets all roles whose path starts with /application_abc/component_xyz/ .
            This parameter is optional. If it is not included, it defaults to a slash (/), listing all roles. This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'Roles': [
            {
                'Path': 'string',
                'RoleName': 'string',
                'RoleId': 'string',
                'Arn': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'AssumeRolePolicyDocument': 'string',
                'Description': 'string'
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    """
    pass

def list_saml_providers():
    """
    Lists the SAML provider resource objects defined in IAM in the account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_saml_providers()
    
    
    :rtype: dict
    :return: {
        'SAMLProviderList': [
            {
                'Arn': 'string',
                'ValidUntil': datetime(2015, 1, 1),
                'CreateDate': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def list_server_certificates(PathPrefix=None, Marker=None, MaxItems=None):
    """
    Lists the server certificates stored in IAM that have the specified path prefix. If none exist, the action returns an empty list.
    You can paginate the results using the MaxItems and Marker parameters.
    For more information about working with server certificates, including a list of AWS services that can use the server certificates that you manage with IAM, go to Working with Server Certificates in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.list_server_certificates(
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. For example: /company/servercerts would get all server certificates for which the path starts with /company/servercerts .
            This parameter is optional. If it is not included, it defaults to a slash (/), listing all server certificates. This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'ServerCertificateMetadataList': [
            {
                'Path': 'string',
                'ServerCertificateName': 'string',
                'ServerCertificateId': 'string',
                'Arn': 'string',
                'UploadDate': datetime(2015, 1, 1),
                'Expiration': datetime(2015, 1, 1)
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    """
    pass

def list_service_specific_credentials(UserName=None, ServiceName=None):
    """
    Returns information about the service-specific credentials associated with the specified IAM user. If there are none, the action returns an empty list. The service-specific credentials returned by this action are used only for authenticating the IAM user to a specific service. For more information about using service-specific credentials to authenticate to an AWS service, see Set Up service-specific credentials in the AWS CodeCommit User Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.list_service_specific_credentials(
        UserName='string',
        ServiceName='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the user whose service-specific credentials you want information about. If this value is not specified then the operation assumes the user whose credentials are used to call the operation.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type ServiceName: string
    :param ServiceName: Filters the returned results to only those for the specified AWS service. If not specified, then AWS returns service-specific credentials for all services.

    :rtype: dict
    :return: {
        'ServiceSpecificCredentials': [
            {
                'UserName': 'string',
                'Status': 'Active'|'Inactive',
                'ServiceUserName': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'ServiceSpecificCredentialId': 'string',
                'ServiceName': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_signing_certificates(UserName=None, Marker=None, MaxItems=None):
    """
    Returns information about the signing certificates associated with the specified IAM user. If there are none, the action returns an empty list.
    Although each user is limited to a small number of signing certificates, you can still paginate the results using the MaxItems and Marker parameters.
    If the UserName field is not specified, the user name is determined implicitly based on the AWS access key ID used to sign the request for this API. Because this action works for access keys under the AWS account, you can use this action to manage root credentials even if the AWS account has no associated users.
    See also: AWS API Documentation
    
    Examples
    The following command lists the signing certificates for the IAM user named Bob.
    Expected Output:
    
    :example: response = client.list_signing_certificates(
        UserName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: The name of the IAM user whose signing certificates you want to examine.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'Certificates': [
            {
                'UserName': 'string',
                'CertificateId': 'string',
                'CertificateBody': 'string',
                'Status': 'Active'|'Inactive',
                'UploadDate': datetime(2015, 1, 1)
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    """
    pass

def list_ssh_public_keys(UserName=None, Marker=None, MaxItems=None):
    """
    Returns information about the SSH public keys associated with the specified IAM user. If there are none, the action returns an empty list.
    The SSH public keys returned by this action are used only for authenticating the IAM user to an AWS CodeCommit repository. For more information about using SSH keys to authenticate to an AWS CodeCommit repository, see Set up AWS CodeCommit for SSH Connections in the AWS CodeCommit User Guide .
    Although each user is limited to a small number of keys, you can still paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.list_ssh_public_keys(
        UserName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: The name of the IAM user to list SSH public keys for. If none is specified, the UserName field is determined implicitly based on the AWS access key used to sign the request.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'SSHPublicKeys': [
            {
                'UserName': 'string',
                'SSHPublicKeyId': 'string',
                'Status': 'Active'|'Inactive',
                'UploadDate': datetime(2015, 1, 1)
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    """
    pass

def list_user_policies(UserName=None, Marker=None, MaxItems=None):
    """
    Lists the names of the inline policies embedded in the specified IAM user.
    An IAM user can also have managed policies attached to it. To list the managed policies that are attached to a user, use  ListAttachedUserPolicies . For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    You can paginate the results using the MaxItems and Marker parameters. If there are no inline policies embedded with the specified user, the action returns an empty list.
    See also: AWS API Documentation
    
    
    :example: response = client.list_user_policies(
        UserName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user to list policies for.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'PolicyNames': [
            'string',
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_users(PathPrefix=None, Marker=None, MaxItems=None):
    """
    Lists the IAM users that have the specified path prefix. If no path prefix is specified, the action returns all users in the AWS account. If there are none, the action returns an empty list.
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    Examples
    The following command lists the IAM users in the current account.
    Expected Output:
    
    :example: response = client.list_users(
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. For example: /division_abc/subdivision_xyz/ , which would get all user names whose path starts with /division_abc/subdivision_xyz/ .
            This parameter is optional. If it is not included, it defaults to a slash (/), listing all user names. This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'Users': [
            {
                'Path': 'string',
                'UserName': 'string',
                'UserId': 'string',
                'Arn': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'PasswordLastUsed': datetime(2015, 1, 1)
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    CreateUser
    GetUser
    ListUsers
    
    """
    pass

def list_virtual_mfa_devices(AssignmentStatus=None, Marker=None, MaxItems=None):
    """
    Lists the virtual MFA devices defined in the AWS account by assignment status. If you do not specify an assignment status, the action returns a list of all virtual MFA devices. Assignment status can be Assigned , Unassigned , or Any .
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    Examples
    The following command lists the virtual MFA devices that have been configured for the current account.
    Expected Output:
    
    :example: response = client.list_virtual_mfa_devices(
        AssignmentStatus='Assigned'|'Unassigned'|'Any',
        Marker='string',
        MaxItems=123
    )
    
    
    :type AssignmentStatus: string
    :param AssignmentStatus: The status (Unassigned or Assigned ) of the devices to list. If you do not specify an AssignmentStatus , the action defaults to Any which lists both assigned and unassigned virtual MFA devices.

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :rtype: dict
    :return: {
        'VirtualMFADevices': [
            {
                'SerialNumber': 'string',
                'Base32StringSeed': b'bytes',
                'QRCodePNG': b'bytes',
                'User': {
                    'Path': 'string',
                    'UserName': 'string',
                    'UserId': 'string',
                    'Arn': 'string',
                    'CreateDate': datetime(2015, 1, 1),
                    'PasswordLastUsed': datetime(2015, 1, 1)
                },
                'EnableDate': datetime(2015, 1, 1)
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    The user does not have a password
    The password exists but has never been used (at least not since IAM started tracking this information on October 20th, 2014
    there is no sign-in data associated with the user
    
    """
    pass

def put_group_policy(GroupName=None, PolicyName=None, PolicyDocument=None):
    """
    Adds or updates an inline policy document that is embedded in the specified IAM group.
    A user can also have managed policies attached to it. To attach a managed policy to a group, use  AttachGroupPolicy . To create a new managed policy, use  CreatePolicy . For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    For information about limits on the number of inline policies that you can embed in a group, see Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command adds a policy named AllPerms to the IAM group named Admins.
    Expected Output:
    
    :example: response = client.put_group_policy(
        GroupName='string',
        PolicyName='string',
        PolicyDocument='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group to associate the policy with.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the policy document.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PolicyDocument: string
    :param PolicyDocument: [REQUIRED]
            The policy document.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            

    :return: response = client.put_group_policy(
        GroupName='Admins',
        PolicyDocument='{"Version":"2012-10-17","Statement":{"Effect":"Allow","Action":"*","Resource":"*"}}',
        PolicyName='AllPerms',
    )
    
    print(response)
    
    
    """
    pass

def put_role_policy(RoleName=None, PolicyName=None, PolicyDocument=None):
    """
    Adds or updates an inline policy document that is embedded in the specified IAM role.
    When you embed an inline policy in a role, the inline policy is used as part of the role's access (permissions) policy. The role's trust policy is created at the same time as the role, using  CreateRole . You can update a role's trust policy using  UpdateAssumeRolePolicy . For more information about IAM roles, go to Using Roles to Delegate Permissions and Federate Identities .
    A role can also have a managed policy attached to it. To attach a managed policy to a role, use  AttachRolePolicy . To create a new managed policy, use  CreatePolicy . For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    For information about limits on the number of inline policies that you can embed with a role, see Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command adds a permissions policy to the role named Test-Role.
    Expected Output:
    
    :example: response = client.put_role_policy(
        RoleName='string',
        PolicyName='string',
        PolicyDocument='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name of the role to associate the policy with.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the policy document.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PolicyDocument: string
    :param PolicyDocument: [REQUIRED]
            The policy document.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            

    :return: response = client.put_role_policy(
        PolicyDocument='{"Version":"2012-10-17","Statement":{"Effect":"Allow","Action":"s3:*","Resource":"*"}}',
        PolicyName='S3AccessPolicy',
        RoleName='S3Access',
    )
    
    print(response)
    
    
    """
    pass

def put_user_policy(UserName=None, PolicyName=None, PolicyDocument=None):
    """
    Adds or updates an inline policy document that is embedded in the specified IAM user.
    An IAM user can also have a managed policy attached to it. To attach a managed policy to a user, use  AttachUserPolicy . To create a new managed policy, use  CreatePolicy . For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    For information about limits on the number of inline policies that you can embed in a user, see Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command attaches a policy to the IAM user named Bob.
    Expected Output:
    
    :example: response = client.put_user_policy(
        UserName='string',
        PolicyName='string',
        PolicyDocument='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user to associate the policy with.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the policy document.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type PolicyDocument: string
    :param PolicyDocument: [REQUIRED]
            The policy document.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            

    :return: response = client.put_user_policy(
        PolicyDocument='{"Version":"2012-10-17","Statement":{"Effect":"Allow","Action":"*","Resource":"*"}}',
        PolicyName='AllAccessPolicy',
        UserName='Bob',
    )
    
    print(response)
    
    
    """
    pass

def remove_client_id_from_open_id_connect_provider(OpenIDConnectProviderArn=None, ClientID=None):
    """
    Removes the specified client ID (also known as audience) from the list of client IDs registered for the specified IAM OpenID Connect (OIDC) provider resource object.
    This action is idempotent; it does not fail or return an error if you try to remove a client ID that does not exist.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_client_id_from_open_id_connect_provider(
        OpenIDConnectProviderArn='string',
        ClientID='string'
    )
    
    
    :type OpenIDConnectProviderArn: string
    :param OpenIDConnectProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM OIDC provider resource to remove the client ID from. You can get a list of OIDC provider ARNs by using the ListOpenIDConnectProviders action.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :type ClientID: string
    :param ClientID: [REQUIRED]
            The client ID (also known as audience) to remove from the IAM OIDC provider resource. For more information about client IDs, see CreateOpenIDConnectProvider .
            

    """
    pass

def remove_role_from_instance_profile(InstanceProfileName=None, RoleName=None):
    """
    Removes the specified IAM role from the specified EC2 instance profile.
    For more information about IAM roles, go to Working with Roles . For more information about instance profiles, go to About Instance Profiles .
    See also: AWS API Documentation
    
    Examples
    The following command removes the role named Test-Role from the instance profile named ExampleInstanceProfile.
    Expected Output:
    
    :example: response = client.remove_role_from_instance_profile(
        InstanceProfileName='string',
        RoleName='string'
    )
    
    
    :type InstanceProfileName: string
    :param InstanceProfileName: [REQUIRED]
            The name of the instance profile to update.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name of the role to remove.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
            

    :return: response = client.remove_role_from_instance_profile(
        InstanceProfileName='ExampleInstanceProfile',
        RoleName='Test-Role',
    )
    
    print(response)
    
    
    """
    pass

def remove_user_from_group(GroupName=None, UserName=None):
    """
    Removes the specified user from the specified group.
    See also: AWS API Documentation
    
    Examples
    The following command removes the user named Bob from the IAM group named Admins.
    Expected Output:
    
    :example: response = client.remove_user_from_group(
        GroupName='string',
        UserName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group to update.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user to remove.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :return: response = client.remove_user_from_group(
        GroupName='Admins',
        UserName='Bob',
    )
    
    print(response)
    
    
    """
    pass

def reset_service_specific_credential(UserName=None, ServiceSpecificCredentialId=None):
    """
    Resets the password for a service-specific credential. The new password is AWS generated and cryptographically strong. It cannot be configured by the user. Resetting the password immediately invalidates the previous password associated with this user.
    See also: AWS API Documentation
    
    
    :example: response = client.reset_service_specific_credential(
        UserName='string',
        ServiceSpecificCredentialId='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the IAM user associated with the service-specific credential. If this value is not specified, then the operation assumes the user whose credentials are used to call the operation.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type ServiceSpecificCredentialId: string
    :param ServiceSpecificCredentialId: [REQUIRED]
            The unique identifier of the service-specific credential.
            This parameter allows (per its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
            

    :rtype: dict
    :return: {
        'ServiceSpecificCredential': {
            'CreateDate': datetime(2015, 1, 1),
            'ServiceName': 'string',
            'ServiceUserName': 'string',
            'ServicePassword': 'string',
            'ServiceSpecificCredentialId': 'string',
            'UserName': 'string',
            'Status': 'Active'|'Inactive'
        }
    }
    
    
    """
    pass

def resync_mfa_device(UserName=None, SerialNumber=None, AuthenticationCode1=None, AuthenticationCode2=None):
    """
    Synchronizes the specified MFA device with its IAM resource object on the AWS servers.
    For more information about creating and working with virtual MFA devices, go to Using a Virtual MFA Device in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.resync_mfa_device(
        UserName='string',
        SerialNumber='string',
        AuthenticationCode1='string',
        AuthenticationCode2='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user whose MFA device you want to resynchronize.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type SerialNumber: string
    :param SerialNumber: [REQUIRED]
            Serial number that uniquely identifies the MFA device.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type AuthenticationCode1: string
    :param AuthenticationCode1: [REQUIRED]
            An authentication code emitted by the device.
            The format for this parameter is a sequence of six digits.
            

    :type AuthenticationCode2: string
    :param AuthenticationCode2: [REQUIRED]
            A subsequent authentication code emitted by the device.
            The format for this parameter is a sequence of six digits.
            

    """
    pass

def set_default_policy_version(PolicyArn=None, VersionId=None):
    """
    Sets the specified version of the specified policy as the policy's default (operative) version.
    This action affects all users, groups, and roles that the policy is attached to. To list the users, groups, and roles that the policy is attached to, use the  ListEntitiesForPolicy API.
    For information about managed policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.set_default_policy_version(
        PolicyArn='string',
        VersionId='string'
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM policy whose default version you want to set.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :type VersionId: string
    :param VersionId: [REQUIRED]
            The version of the policy to set as the default (operative) version.
            For more information about managed policy versions, see Versioning for Managed Policies in the IAM User Guide .
            

    """
    pass

def simulate_custom_policy(PolicyInputList=None, ActionNames=None, ResourceArns=None, ResourcePolicy=None, ResourceOwner=None, CallerArn=None, ContextEntries=None, ResourceHandlingOption=None, MaxItems=None, Marker=None):
    """
    Simulate how a set of IAM policies and optionally a resource-based policy works with a list of API actions and AWS resources to determine the policies' effective permissions. The policies are provided as strings.
    The simulation does not perform the API actions; it only checks the authorization to determine if the simulated policies allow or deny the actions.
    If you want to simulate existing policies attached to an IAM user, group, or role, use  SimulatePrincipalPolicy instead.
    Context keys are variables maintained by AWS and its services that provide details about the context of an API query request. You can use the Condition element of an IAM policy to evaluate context keys. To get the list of context keys that the policies require for correct simulation, use  GetContextKeysForCustomPolicy .
    If the output is long, you can use MaxItems and Marker parameters to paginate the results.
    See also: AWS API Documentation
    
    
    :example: response = client.simulate_custom_policy(
        PolicyInputList=[
            'string',
        ],
        ActionNames=[
            'string',
        ],
        ResourceArns=[
            'string',
        ],
        ResourcePolicy='string',
        ResourceOwner='string',
        CallerArn='string',
        ContextEntries=[
            {
                'ContextKeyName': 'string',
                'ContextKeyValues': [
                    'string',
                ],
                'ContextKeyType': 'string'|'stringList'|'numeric'|'numericList'|'boolean'|'booleanList'|'ip'|'ipList'|'binary'|'binaryList'|'date'|'dateList'
            },
        ],
        ResourceHandlingOption='string',
        MaxItems=123,
        Marker='string'
    )
    
    
    :type PolicyInputList: list
    :param PolicyInputList: [REQUIRED]
            A list of policy documents to include in the simulation. Each document is specified as a string containing the complete, valid JSON text of an IAM policy. Do not include any resource-based policies in this parameter. Any resource-based policy must be submitted with the ResourcePolicy parameter. The policies cannot be 'scope-down' policies, such as you could include in a call to GetFederationToken or one of the AssumeRole APIs to restrict what a user can do while using the temporary credentials.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            (string) --
            

    :type ActionNames: list
    :param ActionNames: [REQUIRED]
            A list of names of API actions to evaluate in the simulation. Each action is evaluated against each resource. Each action must include the service identifier, such as iam:CreateUser .
            (string) --
            

    :type ResourceArns: list
    :param ResourceArns: A list of ARNs of AWS resources to include in the simulation. If this parameter is not provided then the value defaults to * (all resources). Each API in the ActionNames parameter is evaluated for each resource in this list. The simulation determines the access result (allowed or denied) of each combination and reports it in the response.
            The simulation does not automatically retrieve policies for the specified resources. If you want to include a resource policy in the simulation, then you must include the policy as a string in the ResourcePolicy parameter.
            If you include a ResourcePolicy , then it must be applicable to all of the resources included in the simulation or you receive an invalid input error.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            (string) --
            

    :type ResourcePolicy: string
    :param ResourcePolicy: A resource-based policy to include in the simulation provided as a string. Each resource in the simulation is treated as if it had this policy attached. You can include only one resource-based policy in a simulation.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            

    :type ResourceOwner: string
    :param ResourceOwner: An AWS account ID that specifies the owner of any simulated resource that does not identify its owner in the resource ARN, such as an S3 bucket or object. If ResourceOwner is specified, it is also used as the account owner of any ResourcePolicy included in the simulation. If the ResourceOwner parameter is not specified, then the owner of the resources and the resource policy defaults to the account of the identity provided in CallerArn . This parameter is required only if you specify a resource-based policy and account that owns the resource is different from the account that owns the simulated calling user CallerArn .

    :type CallerArn: string
    :param CallerArn: The ARN of the IAM user that you want to use as the simulated caller of the APIs. CallerArn is required if you include a ResourcePolicy so that the policy's Principal element has a value to use in evaluating the policy.
            You can specify only the ARN of an IAM user. You cannot specify the ARN of an assumed role, federated user, or a service principal.
            

    :type ContextEntries: list
    :param ContextEntries: A list of context keys and corresponding values for the simulation to use. Whenever a context key is evaluated in one of the simulated IAM permission policies, the corresponding value is supplied.
            (dict) --Contains information about a condition context key. It includes the name of the key and specifies the value (or values, if the context key supports multiple values) to use in the simulation. This information is used when evaluating the Condition elements of the input policies.
            This data type is used as an input parameter to `` SimulateCustomPolicy `` and `` SimulateCustomPolicy `` .
            ContextKeyName (string) --The full name of a condition context key, including the service prefix. For example, aws:SourceIp or s3:VersionId .
            ContextKeyValues (list) --The value (or values, if the condition context key supports multiple values) to provide to the simulation for use when the key is referenced by a Condition element in an input policy.
            (string) --
            ContextKeyType (string) --The data type of the value (or values) specified in the ContextKeyValues parameter.
            
            

    :type ResourceHandlingOption: string
    :param ResourceHandlingOption: Specifies the type of simulation to run. Different APIs that support resource-based policies require different combinations of resources. By specifying the type of simulation to run, you enable the policy simulator to enforce the presence of the required resources to ensure reliable simulation results. If your simulation does not match one of the following scenarios, then you can omit this parameter. The following list shows each of the supported scenario values and the resources that you must define to run the simulation.
            Each of the EC2 scenarios requires that you specify instance, image, and security-group resources. If your scenario includes an EBS volume, then you must specify that volume as a resource. If the EC2 scenario includes VPC, then you must supply the network-interface resource. If it includes an IP subnet, then you must specify the subnet resource. For more information on the EC2 scenario options, see Supported Platforms in the AWS EC2 User Guide .
            EC2-Classic-InstanceStore  instance, image, security-group
            EC2-Classic-EBS  instance, image, security-group, volume
            EC2-VPC-InstanceStore  instance, image, security-group, network-interface
            EC2-VPC-InstanceStore-Subnet  instance, image, security-group, network-interface, subnet
            EC2-VPC-EBS  instance, image, security-group, network-interface, volume
            EC2-VPC-EBS-Subnet  instance, image, security-group, network-interface, subnet, volume
            

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :rtype: dict
    :return: {
        'EvaluationResults': [
            {
                'EvalActionName': 'string',
                'EvalResourceName': 'string',
                'EvalDecision': 'allowed'|'explicitDeny'|'implicitDeny',
                'MatchedStatements': [
                    {
                        'SourcePolicyId': 'string',
                        'SourcePolicyType': 'user'|'group'|'role'|'aws-managed'|'user-managed'|'resource'|'none',
                        'StartPosition': {
                            'Line': 123,
                            'Column': 123
                        },
                        'EndPosition': {
                            'Line': 123,
                            'Column': 123
                        }
                    },
                ],
                'MissingContextValues': [
                    'string',
                ],
                'OrganizationsDecisionDetail': {
                    'AllowedByOrganizations': True|False
                },
                'EvalDecisionDetails': {
                    'string': 'allowed'|'explicitDeny'|'implicitDeny'
                },
                'ResourceSpecificResults': [
                    {
                        'EvalResourceName': 'string',
                        'EvalResourceDecision': 'allowed'|'explicitDeny'|'implicitDeny',
                        'MatchedStatements': [
                            {
                                'SourcePolicyId': 'string',
                                'SourcePolicyType': 'user'|'group'|'role'|'aws-managed'|'user-managed'|'resource'|'none',
                                'StartPosition': {
                                    'Line': 123,
                                    'Column': 123
                                },
                                'EndPosition': {
                                    'Line': 123,
                                    'Column': 123
                                }
                            },
                        ],
                        'MissingContextValues': [
                            'string',
                        ],
                        'EvalDecisionDetails': {
                            'string': 'allowed'|'explicitDeny'|'implicitDeny'
                        }
                    },
                ]
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def simulate_principal_policy(PolicySourceArn=None, PolicyInputList=None, ActionNames=None, ResourceArns=None, ResourcePolicy=None, ResourceOwner=None, CallerArn=None, ContextEntries=None, ResourceHandlingOption=None, MaxItems=None, Marker=None):
    """
    Simulate how a set of IAM policies attached to an IAM entity works with a list of API actions and AWS resources to determine the policies' effective permissions. The entity can be an IAM user, group, or role. If you specify a user, then the simulation also includes all of the policies that are attached to groups that the user belongs to .
    You can optionally include a list of one or more additional policies specified as strings to include in the simulation. If you want to simulate only policies specified as strings, use  SimulateCustomPolicy instead.
    You can also optionally include one resource-based policy to be evaluated with each of the resources included in the simulation.
    The simulation does not perform the API actions, it only checks the authorization to determine if the simulated policies allow or deny the actions.
    Context keys are variables maintained by AWS and its services that provide details about the context of an API query request. You can use the Condition element of an IAM policy to evaluate context keys. To get the list of context keys that the policies require for correct simulation, use  GetContextKeysForPrincipalPolicy .
    If the output is long, you can use the MaxItems and Marker parameters to paginate the results.
    See also: AWS API Documentation
    
    
    :example: response = client.simulate_principal_policy(
        PolicySourceArn='string',
        PolicyInputList=[
            'string',
        ],
        ActionNames=[
            'string',
        ],
        ResourceArns=[
            'string',
        ],
        ResourcePolicy='string',
        ResourceOwner='string',
        CallerArn='string',
        ContextEntries=[
            {
                'ContextKeyName': 'string',
                'ContextKeyValues': [
                    'string',
                ],
                'ContextKeyType': 'string'|'stringList'|'numeric'|'numericList'|'boolean'|'booleanList'|'ip'|'ipList'|'binary'|'binaryList'|'date'|'dateList'
            },
        ],
        ResourceHandlingOption='string',
        MaxItems=123,
        Marker='string'
    )
    
    
    :type PolicySourceArn: string
    :param PolicySourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of a user, group, or role whose policies you want to include in the simulation. If you specify a user, group, or role, the simulation includes all policies that are associated with that entity. If you specify a user, the simulation also includes all policies that are attached to any groups the user belongs to.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :type PolicyInputList: list
    :param PolicyInputList: An optional list of additional policy documents to include in the simulation. Each document is specified as a string containing the complete, valid JSON text of an IAM policy.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            (string) --
            

    :type ActionNames: list
    :param ActionNames: [REQUIRED]
            A list of names of API actions to evaluate in the simulation. Each action is evaluated for each resource. Each action must include the service identifier, such as iam:CreateUser .
            (string) --
            

    :type ResourceArns: list
    :param ResourceArns: A list of ARNs of AWS resources to include in the simulation. If this parameter is not provided then the value defaults to * (all resources). Each API in the ActionNames parameter is evaluated for each resource in this list. The simulation determines the access result (allowed or denied) of each combination and reports it in the response.
            The simulation does not automatically retrieve policies for the specified resources. If you want to include a resource policy in the simulation, then you must include the policy as a string in the ResourcePolicy parameter.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            (string) --
            

    :type ResourcePolicy: string
    :param ResourcePolicy: A resource-based policy to include in the simulation provided as a string. Each resource in the simulation is treated as if it had this policy attached. You can include only one resource-based policy in a simulation.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            

    :type ResourceOwner: string
    :param ResourceOwner: An AWS account ID that specifies the owner of any simulated resource that does not identify its owner in the resource ARN, such as an S3 bucket or object. If ResourceOwner is specified, it is also used as the account owner of any ResourcePolicy included in the simulation. If the ResourceOwner parameter is not specified, then the owner of the resources and the resource policy defaults to the account of the identity provided in CallerArn . This parameter is required only if you specify a resource-based policy and account that owns the resource is different from the account that owns the simulated calling user CallerArn .

    :type CallerArn: string
    :param CallerArn: The ARN of the IAM user that you want to specify as the simulated caller of the APIs. If you do not specify a CallerArn , it defaults to the ARN of the user that you specify in PolicySourceArn , if you specified a user. If you include both a PolicySourceArn (for example, arn:aws:iam::123456789012:user/David ) and a CallerArn (for example, arn:aws:iam::123456789012:user/Bob ), the result is that you simulate calling the APIs as Bob, as if Bob had David's policies.
            You can specify only the ARN of an IAM user. You cannot specify the ARN of an assumed role, federated user, or a service principal.
            CallerArn is required if you include a ResourcePolicy and the PolicySourceArn is not the ARN for an IAM user. This is required so that the resource-based policy's Principal element has a value to use in evaluating the policy.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :type ContextEntries: list
    :param ContextEntries: A list of context keys and corresponding values for the simulation to use. Whenever a context key is evaluated in one of the simulated IAM permission policies, the corresponding value is supplied.
            (dict) --Contains information about a condition context key. It includes the name of the key and specifies the value (or values, if the context key supports multiple values) to use in the simulation. This information is used when evaluating the Condition elements of the input policies.
            This data type is used as an input parameter to `` SimulateCustomPolicy `` and `` SimulateCustomPolicy `` .
            ContextKeyName (string) --The full name of a condition context key, including the service prefix. For example, aws:SourceIp or s3:VersionId .
            ContextKeyValues (list) --The value (or values, if the condition context key supports multiple values) to provide to the simulation for use when the key is referenced by a Condition element in an input policy.
            (string) --
            ContextKeyType (string) --The data type of the value (or values) specified in the ContextKeyValues parameter.
            
            

    :type ResourceHandlingOption: string
    :param ResourceHandlingOption: Specifies the type of simulation to run. Different APIs that support resource-based policies require different combinations of resources. By specifying the type of simulation to run, you enable the policy simulator to enforce the presence of the required resources to ensure reliable simulation results. If your simulation does not match one of the following scenarios, then you can omit this parameter. The following list shows each of the supported scenario values and the resources that you must define to run the simulation.
            Each of the EC2 scenarios requires that you specify instance, image, and security-group resources. If your scenario includes an EBS volume, then you must specify that volume as a resource. If the EC2 scenario includes VPC, then you must supply the network-interface resource. If it includes an IP subnet, then you must specify the subnet resource. For more information on the EC2 scenario options, see Supported Platforms in the AWS EC2 User Guide .
            EC2-Classic-InstanceStore  instance, image, security-group
            EC2-Classic-EBS  instance, image, security-group, volume
            EC2-VPC-InstanceStore  instance, image, security-group, network-interface
            EC2-VPC-InstanceStore-Subnet  instance, image, security-group, network-interface, subnet
            EC2-VPC-EBS  instance, image, security-group, network-interface, volume
            EC2-VPC-EBS-Subnet  instance, image, security-group, network-interface, subnet, volume
            

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
            If you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true and Marker contains a value to include in the subsequent call that tells the service where to continue from.
            

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :rtype: dict
    :return: {
        'EvaluationResults': [
            {
                'EvalActionName': 'string',
                'EvalResourceName': 'string',
                'EvalDecision': 'allowed'|'explicitDeny'|'implicitDeny',
                'MatchedStatements': [
                    {
                        'SourcePolicyId': 'string',
                        'SourcePolicyType': 'user'|'group'|'role'|'aws-managed'|'user-managed'|'resource'|'none',
                        'StartPosition': {
                            'Line': 123,
                            'Column': 123
                        },
                        'EndPosition': {
                            'Line': 123,
                            'Column': 123
                        }
                    },
                ],
                'MissingContextValues': [
                    'string',
                ],
                'OrganizationsDecisionDetail': {
                    'AllowedByOrganizations': True|False
                },
                'EvalDecisionDetails': {
                    'string': 'allowed'|'explicitDeny'|'implicitDeny'
                },
                'ResourceSpecificResults': [
                    {
                        'EvalResourceName': 'string',
                        'EvalResourceDecision': 'allowed'|'explicitDeny'|'implicitDeny',
                        'MatchedStatements': [
                            {
                                'SourcePolicyId': 'string',
                                'SourcePolicyType': 'user'|'group'|'role'|'aws-managed'|'user-managed'|'resource'|'none',
                                'StartPosition': {
                                    'Line': 123,
                                    'Column': 123
                                },
                                'EndPosition': {
                                    'Line': 123,
                                    'Column': 123
                                }
                            },
                        ],
                        'MissingContextValues': [
                            'string',
                        ],
                        'EvalDecisionDetails': {
                            'string': 'allowed'|'explicitDeny'|'implicitDeny'
                        }
                    },
                ]
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_access_key(UserName=None, AccessKeyId=None, Status=None):
    """
    Changes the status of the specified access key from Active to Inactive, or vice versa. This action can be used to disable a user's key as part of a key rotation work flow.
    If the UserName field is not specified, the UserName is determined implicitly based on the AWS access key ID used to sign the request. Because this action works for access keys under the AWS account, you can use this action to manage root credentials even if the AWS account has no associated users.
    For information about rotating keys, see Managing Keys and Certificates in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command deactivates the specified access key (access key ID and secret access key) for the IAM user named Bob.
    Expected Output:
    
    :example: response = client.update_access_key(
        UserName='string',
        AccessKeyId='string',
        Status='Active'|'Inactive'
    )
    
    
    :type UserName: string
    :param UserName: The name of the user whose key you want to update.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type AccessKeyId: string
    :param AccessKeyId: [REQUIRED]
            The access key ID of the secret access key you want to update.
            This parameter allows (per its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
            

    :type Status: string
    :param Status: [REQUIRED]
            The status you want to assign to the secret access key. Active means the key can be used for API calls to AWS, while Inactive means the key cannot be used.
            

    :return: response = client.update_access_key(
        AccessKeyId='AKIAIOSFODNN7EXAMPLE',
        Status='Inactive',
        UserName='Bob',
    )
    
    print(response)
    
    
    """
    pass

def update_account_password_policy(MinimumPasswordLength=None, RequireSymbols=None, RequireNumbers=None, RequireUppercaseCharacters=None, RequireLowercaseCharacters=None, AllowUsersToChangePassword=None, MaxPasswordAge=None, PasswordReusePrevention=None, HardExpiry=None):
    """
    Updates the password policy settings for the AWS account.
    For more information about using a password policy, see Managing an IAM Password Policy in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command sets the password policy to require a minimum length of eight characters and to require one or more numbers in the password:
    Expected Output:
    
    :example: response = client.update_account_password_policy(
        MinimumPasswordLength=123,
        RequireSymbols=True|False,
        RequireNumbers=True|False,
        RequireUppercaseCharacters=True|False,
        RequireLowercaseCharacters=True|False,
        AllowUsersToChangePassword=True|False,
        MaxPasswordAge=123,
        PasswordReusePrevention=123,
        HardExpiry=True|False
    )
    
    
    :type MinimumPasswordLength: integer
    :param MinimumPasswordLength: The minimum number of characters allowed in an IAM user password.
            Default value: 6
            

    :type RequireSymbols: boolean
    :param RequireSymbols: Specifies whether IAM user passwords must contain at least one of the following non-alphanumeric characters:
            ! @ # $ % ^ amp; * ( ) _ + - = [ ] { } | '
            Default value: false
            

    :type RequireNumbers: boolean
    :param RequireNumbers: Specifies whether IAM user passwords must contain at least one numeric character (0 to 9).
            Default value: false
            

    :type RequireUppercaseCharacters: boolean
    :param RequireUppercaseCharacters: Specifies whether IAM user passwords must contain at least one uppercase character from the ISO basic Latin alphabet (A to Z).
            Default value: false
            

    :type RequireLowercaseCharacters: boolean
    :param RequireLowercaseCharacters: Specifies whether IAM user passwords must contain at least one lowercase character from the ISO basic Latin alphabet (a to z).
            Default value: false
            

    :type AllowUsersToChangePassword: boolean
    :param AllowUsersToChangePassword: Allows all IAM users in your account to use the AWS Management Console to change their own passwords. For more information, see Letting IAM Users Change Their Own Passwords in the IAM User Guide .
            Default value: false
            

    :type MaxPasswordAge: integer
    :param MaxPasswordAge: The number of days that an IAM user password is valid. The default value of 0 means IAM user passwords never expire.
            Default value: 0
            

    :type PasswordReusePrevention: integer
    :param PasswordReusePrevention: Specifies the number of previous passwords that IAM users are prevented from reusing. The default value of 0 means IAM users are not prevented from reusing previous passwords.
            Default value: 0
            

    :type HardExpiry: boolean
    :param HardExpiry: Prevents IAM users from setting a new password after their password has expired.
            Default value: false
            

    :return: response = client.update_account_password_policy(
        MinimumPasswordLength=8,
        RequireNumbers=True,
    )
    
    print(response)
    
    
    """
    pass

def update_assume_role_policy(RoleName=None, PolicyDocument=None):
    """
    Updates the policy that grants an IAM entity permission to assume a role. This is typically referred to as the "role trust policy". For more information about roles, go to Using Roles to Delegate Permissions and Federate Identities .
    See also: AWS API Documentation
    
    Examples
    The following command updates the role trust policy for the role named Test-Role:
    Expected Output:
    
    :example: response = client.update_assume_role_policy(
        RoleName='string',
        PolicyDocument='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name of the role to update with the new policy.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
            

    :type PolicyDocument: string
    :param PolicyDocument: [REQUIRED]
            The policy that grants an entity permission to assume the role.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            

    :return: response = client.update_assume_role_policy(
        PolicyDocument='{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":["ec2.amazonaws.com"]},"Action":["sts:AssumeRole"]}]}',
        RoleName='S3AccessForEC2Instances',
    )
    
    print(response)
    
    
    """
    pass

def update_group(GroupName=None, NewPath=None, NewGroupName=None):
    """
    Updates the name and/or the path of the specified IAM group.
    See also: AWS API Documentation
    
    Examples
    The following command changes the name of the IAM group Test to Test-1.
    Expected Output:
    
    :example: response = client.update_group(
        GroupName='string',
        NewPath='string',
        NewGroupName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            Name of the IAM group to update. If you're changing the name of the group, this is the original name.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type NewPath: string
    :param NewPath: New path for the IAM group. Only include this if changing the group's path.
            This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type NewGroupName: string
    :param NewGroupName: New name for the IAM group. Only include this if changing the group's name.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :return: response = client.update_group(
        GroupName='Test',
        NewGroupName='Test-1',
    )
    
    print(response)
    
    
    """
    pass

def update_login_profile(UserName=None, Password=None, PasswordResetRequired=None):
    """
    Changes the password for the specified IAM user.
    IAM users can change their own passwords by calling  ChangePassword . For more information about modifying passwords, see Managing Passwords in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following command creates or changes the password for the IAM user named Bob.
    Expected Output:
    
    :example: response = client.update_login_profile(
        UserName='string',
        Password='string',
        PasswordResetRequired=True|False
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user whose password you want to update.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type Password: string
    :param Password: The new password for the specified IAM user.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D). However, the format can be further restricted by the account administrator by setting a password policy on the AWS account. For more information, see UpdateAccountPasswordPolicy .
            

    :type PasswordResetRequired: boolean
    :param PasswordResetRequired: Allows this new password to be used only once by requiring the specified IAM user to set a new password on next sign-in.

    :return: response = client.update_login_profile(
        Password='SomeKindOfPassword123!@#',
        UserName='Bob',
    )
    
    print(response)
    
    
    """
    pass

def update_open_id_connect_provider_thumbprint(OpenIDConnectProviderArn=None, ThumbprintList=None):
    """
    Replaces the existing list of server certificate thumbprints associated with an OpenID Connect (OIDC) provider resource object with a new list of thumbprints.
    The list that you pass with this action completely replaces the existing list of thumbprints. (The lists are not merged.)
    Typically, you need to update a thumbprint only when the identity provider's certificate changes, which occurs rarely. However, if the provider's certificate does change, any attempt to assume an IAM role that specifies the OIDC provider as a principal fails until the certificate thumbprint is updated.
    See also: AWS API Documentation
    
    
    :example: response = client.update_open_id_connect_provider_thumbprint(
        OpenIDConnectProviderArn='string',
        ThumbprintList=[
            'string',
        ]
    )
    
    
    :type OpenIDConnectProviderArn: string
    :param OpenIDConnectProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM OIDC provider resource object for which you want to update the thumbprint. You can get a list of OIDC provider ARNs by using the ListOpenIDConnectProviders action.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :type ThumbprintList: list
    :param ThumbprintList: [REQUIRED]
            A list of certificate thumbprints that are associated with the specified IAM OpenID Connect provider. For more information, see CreateOpenIDConnectProvider .
            (string) --Contains a thumbprint for an identity provider's server certificate.
            The identity provider's server certificate thumbprint is the hex-encoded SHA-1 hash value of the self-signed X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string.
            

    """
    pass

def update_role_description(RoleName=None, Description=None):
    """
    Modifies the description of a role.
    See also: AWS API Documentation
    
    
    :example: response = client.update_role_description(
        RoleName='string',
        Description='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]
            The name of the role that you want to modify.
            

    :type Description: string
    :param Description: [REQUIRED]
            The new description that you want to apply to the specified role.
            

    :rtype: dict
    :return: {
        'Role': {
            'Path': 'string',
            'RoleName': 'string',
            'RoleId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'AssumeRolePolicyDocument': 'string',
            'Description': 'string'
        }
    }
    
    
    """
    pass

def update_saml_provider(SAMLMetadataDocument=None, SAMLProviderArn=None):
    """
    Updates the metadata document for an existing SAML provider resource object.
    See also: AWS API Documentation
    
    
    :example: response = client.update_saml_provider(
        SAMLMetadataDocument='string',
        SAMLProviderArn='string'
    )
    
    
    :type SAMLMetadataDocument: string
    :param SAMLMetadataDocument: [REQUIRED]
            An XML document generated by an identity provider (IdP) that supports SAML 2.0. The document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that are received from the IdP. You must generate the metadata document using the identity management software that is used as your organization's IdP.
            

    :type SAMLProviderArn: string
    :param SAMLProviderArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the SAML provider to update.
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
            

    :rtype: dict
    :return: {
        'SAMLProviderArn': 'string'
    }
    
    
    """
    pass

def update_server_certificate(ServerCertificateName=None, NewPath=None, NewServerCertificateName=None):
    """
    Updates the name and/or the path of the specified server certificate stored in IAM.
    For more information about working with server certificates, including a list of AWS services that can use the server certificates that you manage with IAM, go to Working with Server Certificates in the IAM User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.update_server_certificate(
        ServerCertificateName='string',
        NewPath='string',
        NewServerCertificateName='string'
    )
    
    
    :type ServerCertificateName: string
    :param ServerCertificateName: [REQUIRED]
            The name of the server certificate that you want to update.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type NewPath: string
    :param NewPath: The new path for the server certificate. Include this only if you are updating the server certificate's path.
            This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type NewServerCertificateName: string
    :param NewServerCertificateName: The new name for the server certificate. Include this only if you are updating the server certificate's name. The name of the certificate cannot contain any spaces.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    """
    pass

def update_service_specific_credential(UserName=None, ServiceSpecificCredentialId=None, Status=None):
    """
    Sets the status of a service-specific credential to Active or Inactive . Service-specific credentials that are inactive cannot be used for authentication to the service. This action can be used to disable a users service-specific credential as part of a credential rotation work flow.
    See also: AWS API Documentation
    
    
    :example: response = client.update_service_specific_credential(
        UserName='string',
        ServiceSpecificCredentialId='string',
        Status='Active'|'Inactive'
    )
    
    
    :type UserName: string
    :param UserName: The name of the IAM user associated with the service-specific credential. If you do not specify this value, then the operation assumes the user whose credentials are used to call the operation.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type ServiceSpecificCredentialId: string
    :param ServiceSpecificCredentialId: [REQUIRED]
            The unique identifier of the service-specific credential.
            This parameter allows (per its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
            

    :type Status: string
    :param Status: [REQUIRED]
            The status to be assigned to the service-specific credential.
            

    """
    pass

def update_signing_certificate(UserName=None, CertificateId=None, Status=None):
    """
    Changes the status of the specified user signing certificate from active to disabled, or vice versa. This action can be used to disable an IAM user's signing certificate as part of a certificate rotation work flow.
    If the UserName field is not specified, the UserName is determined implicitly based on the AWS access key ID used to sign the request. Because this action works for access keys under the AWS account, you can use this action to manage root credentials even if the AWS account has no associated users.
    See also: AWS API Documentation
    
    Examples
    The following command changes the status of a signing certificate for a user named Bob to Inactive.
    Expected Output:
    
    :example: response = client.update_signing_certificate(
        UserName='string',
        CertificateId='string',
        Status='Active'|'Inactive'
    )
    
    
    :type UserName: string
    :param UserName: The name of the IAM user the signing certificate belongs to.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type CertificateId: string
    :param CertificateId: [REQUIRED]
            The ID of the signing certificate you want to update.
            This parameter allows (per its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
            

    :type Status: string
    :param Status: [REQUIRED]
            The status you want to assign to the certificate. Active means the certificate can be used for API calls to AWS, while Inactive means the certificate cannot be used.
            

    :return: response = client.update_signing_certificate(
        CertificateId='TA7SMP42TDN5Z26OBPJE7EXAMPLE',
        Status='Inactive',
        UserName='Bob',
    )
    
    print(response)
    
    
    """
    pass

def update_ssh_public_key(UserName=None, SSHPublicKeyId=None, Status=None):
    """
    Sets the status of an IAM user's SSH public key to active or inactive. SSH public keys that are inactive cannot be used for authentication. This action can be used to disable a user's SSH public key as part of a key rotation work flow.
    The SSH public key affected by this action is used only for authenticating the associated IAM user to an AWS CodeCommit repository. For more information about using SSH keys to authenticate to an AWS CodeCommit repository, see Set up AWS CodeCommit for SSH Connections in the AWS CodeCommit User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.update_ssh_public_key(
        UserName='string',
        SSHPublicKeyId='string',
        Status='Active'|'Inactive'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the IAM user associated with the SSH public key.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type SSHPublicKeyId: string
    :param SSHPublicKeyId: [REQUIRED]
            The unique identifier for the SSH public key.
            This parameter allows (per its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
            

    :type Status: string
    :param Status: [REQUIRED]
            The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used.
            

    """
    pass

def update_user(UserName=None, NewPath=None, NewUserName=None):
    """
    Updates the name and/or the path of the specified IAM user.
    See also: AWS API Documentation
    
    Examples
    The following command changes the name of the IAM user Bob to Robert. It does not change the user's path.
    Expected Output:
    
    :example: response = client.update_user(
        UserName='string',
        NewPath='string',
        NewUserName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            Name of the user to update. If you're changing the name of the user, this is the original user name.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type NewPath: string
    :param NewPath: New path for the IAM user. Include this parameter only if you're changing the user's path.
            This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            

    :type NewUserName: string
    :param NewUserName: New name for the user. Include this parameter only if you're changing the user's name.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :return: response = client.update_user(
        NewUserName='Robert',
        UserName='Bob',
    )
    
    print(response)
    
    
    """
    pass

def upload_server_certificate(Path=None, ServerCertificateName=None, CertificateBody=None, PrivateKey=None, CertificateChain=None):
    """
    Uploads a server certificate entity for the AWS account. The server certificate entity includes a public key certificate, a private key, and an optional certificate chain, which should all be PEM-encoded.
    We recommend that you use AWS Certificate Manager to provision, manage, and deploy your server certificates. With ACM you can request a certificate, deploy it to AWS resources, and let ACM handle certificate renewals for you. Certificates provided by ACM are free. For more information about using ACM, see the AWS Certificate Manager User Guide .
    For more information about working with server certificates, including a list of AWS services that can use the server certificates that you manage with IAM, go to Working with Server Certificates in the IAM User Guide .
    For information about the number of server certificates you can upload, see Limitations on IAM Entities and Objects in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    The following upload-server-certificate command uploads a server certificate to your AWS account:
    Expected Output:
    
    :example: response = client.upload_server_certificate(
        Path='string',
        ServerCertificateName='string',
        CertificateBody='string',
        PrivateKey='string',
        CertificateChain='string'
    )
    
    
    :type Path: string
    :param Path: The path for the server certificate. For more information about paths, see IAM Identifiers in the IAM User Guide .
            This parameter is optional. If it is not included, it defaults to a slash (/). This paramater allows (per its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes, containing any ASCII character from the ! (u0021) thru the DEL character (u007F), including most punctuation characters, digits, and upper and lowercased letters.
            Note
            If you are uploading a server certificate specifically for use with Amazon CloudFront distributions, you must specify a path using the --path option. The path must begin with /cloudfront and must include a trailing slash (for example, /cloudfront/test/ ).
            

    :type ServerCertificateName: string
    :param ServerCertificateName: [REQUIRED]
            The name for the server certificate. Do not include the path in this value. The name of the certificate cannot contain any spaces.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type CertificateBody: string
    :param CertificateBody: [REQUIRED]
            The contents of the public key certificate in PEM-encoded format.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            

    :type PrivateKey: string
    :param PrivateKey: [REQUIRED]
            The contents of the private key in PEM-encoded format.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            

    :type CertificateChain: string
    :param CertificateChain: The contents of the certificate chain. This is typically a concatenation of the PEM-encoded public key certificates of the chain.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            

    :rtype: dict
    :return: {
        'ServerCertificateMetadata': {
            'Path': 'string',
            'ServerCertificateName': 'string',
            'ServerCertificateId': 'string',
            'Arn': 'string',
            'UploadDate': datetime(2015, 1, 1),
            'Expiration': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def upload_signing_certificate(UserName=None, CertificateBody=None):
    """
    Uploads an X.509 signing certificate and associates it with the specified IAM user. Some AWS services use X.509 signing certificates to validate requests that are signed with a corresponding private key. When you upload the certificate, its default status is Active .
    If the UserName field is not specified, the IAM user name is determined implicitly based on the AWS access key ID used to sign the request. Because this action works for access keys under the AWS account, you can use this action to manage root credentials even if the AWS account has no associated users.
    See also: AWS API Documentation
    
    Examples
    The following command uploads a signing certificate for the IAM user named Bob.
    Expected Output:
    
    :example: response = client.upload_signing_certificate(
        UserName='string',
        CertificateBody='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the user the signing certificate is for.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type CertificateBody: string
    :param CertificateBody: [REQUIRED]
            The contents of the signing certificate.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            

    :rtype: dict
    :return: {
        'Certificate': {
            'UserName': 'string',
            'CertificateId': 'string',
            'CertificateBody': 'string',
            'Status': 'Active'|'Inactive',
            'UploadDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def upload_ssh_public_key(UserName=None, SSHPublicKeyBody=None):
    """
    Uploads an SSH public key and associates it with the specified IAM user.
    The SSH public key uploaded by this action can be used only for authenticating the associated IAM user to an AWS CodeCommit repository. For more information about using SSH keys to authenticate to an AWS CodeCommit repository, see Set up AWS CodeCommit for SSH Connections in the AWS CodeCommit User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.upload_ssh_public_key(
        UserName='string',
        SSHPublicKeyBody='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the IAM user to associate the SSH public key with.
            This parameter allows (per its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
            

    :type SSHPublicKeyBody: string
    :param SSHPublicKeyBody: [REQUIRED]
            The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.
            The regex pattern used to validate this parameter is a string of characters consisting of any printable ASCII character ranging from the space character (u0020) through end of the ASCII character range as well as the printable characters in the Basic Latin and Latin-1 Supplement character set (through u00FF). It also includes the special characters tab (u0009), line feed (u000A), and carriage return (u000D).
            

    :rtype: dict
    :return: {
        'SSHPublicKey': {
            'UserName': 'string',
            'SSHPublicKeyId': 'string',
            'Fingerprint': 'string',
            'SSHPublicKeyBody': 'string',
            'Status': 'Active'|'Inactive',
            'UploadDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

