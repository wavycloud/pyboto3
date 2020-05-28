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
    This operation is idempotent; it does not fail or return an error if you add an existing client ID to the provider.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following add-client-id-to-open-id-connect-provider command adds the client ID my-application-ID to the OIDC provider named server.example.com:
    Expected Output:
    
    :example: response = client.add_client_id_to_open_id_connect_provider(
        OpenIDConnectProviderArn='string',
        ClientID='string'
    )
    
    
    :type OpenIDConnectProviderArn: string
    :param OpenIDConnectProviderArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM OpenID Connect (OIDC) provider resource to add the client ID to. You can get a list of OIDC provider ARNs by using the ListOpenIDConnectProviders operation.\n

    :type ClientID: string
    :param ClientID: [REQUIRED]\nThe client ID (also known as audience) to add to the IAM OpenID Connect provider resource.\n

    :return: response = client.add_client_id_to_open_id_connect_provider(
        ClientID='my-application-ID',
        OpenIDConnectProviderArn='arn:aws:iam::123456789012:oidc-provider/server.example.com',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def add_role_to_instance_profile(InstanceProfileName=None, RoleName=None):
    """
    Adds the specified IAM role to the specified instance profile. An instance profile can contain only one role, and this limit cannot be increased. You can remove the existing role and then add a different role to an instance profile. You must then wait for the change to appear across all of AWS because of eventual consistency . To force the change, you must disassociate the instance profile and then associate the instance profile , or you can stop your instance and then restart it.
    For more information about roles, go to Working with Roles . For more information about instance profiles, go to About Instance Profiles .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command adds the role named S3Access to the instance profile named Webserver:
    Expected Output:
    
    :example: response = client.add_role_to_instance_profile(
        InstanceProfileName='string',
        RoleName='string'
    )
    
    
    :type InstanceProfileName: string
    :param InstanceProfileName: [REQUIRED]\nThe name of the instance profile to update.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the role to add.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :return: response = client.add_role_to_instance_profile(
        InstanceProfileName='Webserver',
        RoleName='S3Access',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.EntityAlreadyExistsException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.UnmodifiableEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def add_user_to_group(GroupName=None, UserName=None):
    """
    Adds the specified user to the specified group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command adds an IAM user named Bob to the IAM group named Admins:
    Expected Output:
    
    :example: response = client.add_user_to_group(
        GroupName='string',
        UserName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group to update.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user to add.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :return: response = client.add_user_to_group(
        GroupName='Admins',
        UserName='Bob',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def attach_group_policy(GroupName=None, PolicyArn=None):
    """
    Attaches the specified managed policy to the specified IAM group.
    You use this API to attach a managed policy to a group. To embed an inline policy in a group, use  PutGroupPolicy .
    For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command attaches the AWS managed policy named ReadOnlyAccess to the IAM group named Finance.
    Expected Output:
    
    :example: response = client.attach_group_policy(
        GroupName='string',
        PolicyArn='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name (friendly name, not ARN) of the group to attach the policy to.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM policy you want to attach.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :return: response = client.attach_group_policy(
        GroupName='Finance',
        PolicyArn='arn:aws:iam::aws:policy/ReadOnlyAccess',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.PolicyNotAttachableException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def attach_role_policy(RoleName=None, PolicyArn=None):
    """
    Attaches the specified managed policy to the specified IAM role. When you attach a managed policy to a role, the managed policy becomes part of the role\'s permission (access) policy.
    Use this API to attach a managed policy to a role. To embed an inline policy in a role, use  PutRolePolicy . For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command attaches the AWS managed policy named ReadOnlyAccess to the IAM role named ReadOnlyRole.
    Expected Output:
    
    :example: response = client.attach_role_policy(
        RoleName='string',
        PolicyArn='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name (friendly name, not ARN) of the role to attach the policy to.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM policy you want to attach.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :return: response = client.attach_role_policy(
        PolicyArn='arn:aws:iam::aws:policy/ReadOnlyAccess',
        RoleName='ReadOnlyRole',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.UnmodifiableEntityException
    IAM.Client.exceptions.PolicyNotAttachableException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def attach_user_policy(UserName=None, PolicyArn=None):
    """
    Attaches the specified managed policy to the specified user.
    You use this API to attach a managed policy to a user. To embed an inline policy in a user, use  PutUserPolicy .
    For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command attaches the AWS managed policy named AdministratorAccess to the IAM user named Alice.
    Expected Output:
    
    :example: response = client.attach_user_policy(
        UserName='string',
        PolicyArn='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name (friendly name, not ARN) of the IAM user to attach the policy to.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM policy you want to attach.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :return: response = client.attach_user_policy(
        PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess',
        UserName='Alice',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.PolicyNotAttachableException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def change_password(OldPassword=None, NewPassword=None):
    """
    Changes the password of the IAM user who is calling this operation. The AWS account root user password is not affected by this operation.
    To change the password for a different user, see  UpdateLoginProfile . For more information about modifying passwords, see Managing Passwords in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command changes the password for the current IAM user.
    Expected Output:
    
    :example: response = client.change_password(
        OldPassword='string',
        NewPassword='string'
    )
    
    
    :type OldPassword: string
    :param OldPassword: [REQUIRED]\nThe IAM user\'s current password.\n

    :type NewPassword: string
    :param NewPassword: [REQUIRED]\nThe new password. The new password must conform to the AWS account\'s password policy, if one exists.\nThe regex pattern that is used to validate this parameter is a string of characters. That string can include almost any printable ASCII character from the space (\\u0020 ) through the end of the ASCII character range (\\u00FF ). You can also include the tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D ) characters. Any of these characters are valid in a password. However, many tools, such as the AWS Management Console, might restrict the ability to type certain characters because they have special meaning within that tool.\n

    :return: response = client.change_password(
        NewPassword=']35d/{pB9Fo9wJ',
        OldPassword='3s0K_;xh4~8XXI',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.InvalidUserTypeException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.EntityTemporarilyUnmodifiableException
    IAM.Client.exceptions.PasswordPolicyViolationException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_access_key(UserName=None):
    """
    Creates a new AWS secret access key and corresponding AWS access key ID for the specified user. The default status for new keys is Active .
    If you do not specify a user name, IAM determines the user name implicitly based on the AWS access key ID signing the request. This operation works for access keys under the AWS account. Consequently, you can use this operation to manage AWS account root user credentials. This is true even if the AWS account has no associated users.
    For information about limits on the number of keys you can create, see Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command creates an access key (access key ID and secret access key) for the IAM user named Bob.
    Expected Output:
    
    :example: response = client.create_access_key(
        UserName='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the IAM user that the new key will belong to.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :rtype: dict
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

(dict) --Contains the response to a successful  CreateAccessKey request.

AccessKey (dict) --A structure with details about the access key.

UserName (string) --The name of the IAM user that the access key is associated with.

AccessKeyId (string) --The ID for this access key.

Status (string) --The status of the access key. Active means that the key is valid for API calls, while Inactive means it is not.

SecretAccessKey (string) --The secret key used to sign requests.

CreateDate (datetime) --The date when the access key was created.








Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command creates an access key (access key ID and secret access key) for the IAM user named Bob.
response = client.create_access_key(
    UserName='Bob',
)

print(response)


Expected Output:
{
    'AccessKey': {
        'AccessKeyId': 'AKIAIOSFODNN7EXAMPLE',
        'CreateDate': datetime(2015, 3, 9, 18, 39, 23, 0, 68, 0),
        'SecretAccessKey': 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY',
        'Status': 'Active',
        'UserName': 'Bob',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    Exceptions
    Examples
    The following command associates the alias examplecorp to your AWS account.
    Expected Output:
    
    :example: response = client.create_account_alias(
        AccountAlias='string'
    )
    
    
    :type AccountAlias: string
    :param AccountAlias: [REQUIRED]\nThe account alias to create.\nThis parameter allows (through its regex pattern ) a string of characters consisting of lowercase letters, digits, and dashes. You cannot start or finish with a dash, nor can you have two dashes in a row.\n

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
    
    Exceptions
    Examples
    The following command creates an IAM group named Admins.
    Expected Output:
    
    :example: response = client.create_group(
        Path='string',
        GroupName='string'
    )
    
    
    :type Path: string
    :param Path: The path to the group. For more information about paths, see IAM Identifiers in the IAM User Guide .\nThis parameter is optional. If it is not included, it defaults to a slash (/).\nThis parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group to create. Do not include the path in this value.\nIAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both 'MyResource' and 'myresource'.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Group': {
        'Path': 'string',
        'GroupName': 'string',
        'GroupId': 'string',
        'Arn': 'string',
        'CreateDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Contains the response to a successful  CreateGroup request.

Group (dict) --
A structure containing details about the new group.

Path (string) --
The path to the group. For more information about paths, see IAM Identifiers in the IAM User Guide .

GroupName (string) --
The friendly name that identifies the group.

GroupId (string) --
The stable and unique string identifying the group. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the group was created.









Exceptions

IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.EntityAlreadyExistsException
IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command creates an IAM group named Admins.
response = client.create_group(
    GroupName='Admins',
)

print(response)


Expected Output:
{
    'Group': {
        'Arn': 'arn:aws:iam::123456789012:group/Admins',
        'CreateDate': datetime(2015, 3, 9, 20, 30, 24, 0, 68, 0),
        'GroupId': 'AIDGPMS9RO4H3FEXAMPLE',
        'GroupName': 'Admins',
        'Path': '/',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Group': {
            'Path': 'string',
            'GroupName': 'string',
            'GroupId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.EntityAlreadyExistsException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_instance_profile(InstanceProfileName=None, Path=None):
    """
    Creates a new instance profile. For information about instance profiles, go to About Instance Profiles .
    For information about the number of instance profiles you can create, see Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command creates an instance profile named Webserver that is ready to have a role attached and then be associated with an EC2 instance.
    Expected Output:
    
    :example: response = client.create_instance_profile(
        InstanceProfileName='string',
        Path='string'
    )
    
    
    :type InstanceProfileName: string
    :param InstanceProfileName: [REQUIRED]\nThe name of the instance profile to create.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Path: string
    :param Path: The path to the instance profile. For more information about paths, see IAM Identifiers in the IAM User Guide .\nThis parameter is optional. If it is not included, it defaults to a slash (/).\nThis parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
                'Description': 'string',
                'MaxSessionDuration': 123,
                'PermissionsBoundary': {
                    'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                    'PermissionsBoundaryArn': 'string'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'RoleLastUsed': {
                    'LastUsedDate': datetime(2015, 1, 1),
                    'Region': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --
Contains the response to a successful  CreateInstanceProfile request.

InstanceProfile (dict) --
A structure containing details about the new instance profile.

Path (string) --
The path to the instance profile. For more information about paths, see IAM Identifiers in the IAM User Guide .

InstanceProfileName (string) --
The name identifying the instance profile.

InstanceProfileId (string) --
The stable and unique string identifying the instance profile. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the instance profile. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --
The date when the instance profile was created.

Roles (list) --
The role associated with the instance profile.

(dict) --
Contains information about an IAM role. This structure is returned as a response element in several API operations that interact with roles.

Path (string) --
The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide .

RoleName (string) --
The friendly name that identifies the role.

RoleId (string) --
The stable and unique string identifying the role. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide guide.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the role was created.

AssumeRolePolicyDocument (string) --
The policy that grants an entity permission to assume the role.

Description (string) --
A description of the role that you provide.

MaxSessionDuration (integer) --
The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI, or API to assume the role can specify the duration using the optional DurationSeconds API parameter or duration-seconds CLI parameter.

PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the role.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are attached to the specified role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.






RoleLastUsed (dict) --
Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see Regions Where Data Is Tracked in the IAM User Guide .

LastUsedDate (datetime) --
The date and time, in ISO 8601 date-time format that the role was last used.
This field is null if the role has not been used within the IAM tracking period. For more information about the tracking period, see Regions Where Data Is Tracked in the IAM User Guide .

Region (string) --
The name of the AWS Region in which the role was last used.















Exceptions

IAM.Client.exceptions.EntityAlreadyExistsException
IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command creates an instance profile named Webserver that is ready to have a role attached and then be associated with an EC2 instance.
response = client.create_instance_profile(
    InstanceProfileName='Webserver',
)

print(response)


Expected Output:
{
    'InstanceProfile': {
        'Arn': 'arn:aws:iam::123456789012:instance-profile/Webserver',
        'CreateDate': datetime(2015, 3, 9, 20, 33, 19, 0, 68, 0),
        'InstanceProfileId': 'AIPAJMBYC7DLSPEXAMPLE',
        'InstanceProfileName': 'Webserver',
        'Path': '/',
        'Roles': [
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                    'Description': 'string',
                    'MaxSessionDuration': 123,
                    'PermissionsBoundary': {
                        'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                        'PermissionsBoundaryArn': 'string'
                    },
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'RoleLastUsed': {
                        'LastUsedDate': datetime(2015, 1, 1),
                        'Region': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    IAM.Client.exceptions.EntityAlreadyExistsException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_login_profile(UserName=None, Password=None, PasswordResetRequired=None):
    """
    Creates a password for the specified user, giving the user the ability to access AWS services through the AWS Management Console. For more information about managing passwords, see Managing Passwords in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command changes IAM user Bob\'s password and sets the flag that required Bob to change the password the next time he signs in.
    Expected Output:
    
    :example: response = client.create_login_profile(
        UserName='string',
        Password='string',
        PasswordResetRequired=True|False
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the IAM user to create a password for. The user must already exist.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Password: string
    :param Password: [REQUIRED]\nThe new password for the user.\nThe regex pattern that is used to validate this parameter is a string of characters. That string can include almost any printable ASCII character from the space (\\u0020 ) through the end of the ASCII character range (\\u00FF ). You can also include the tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D ) characters. Any of these characters are valid in a password. However, many tools, such as the AWS Management Console, might restrict the ability to type certain characters because they have special meaning within that tool.\n

    :type PasswordResetRequired: boolean
    :param PasswordResetRequired: Specifies whether the user is required to set a new password on next sign-in.

    :rtype: dict

ReturnsResponse Syntax
{
    'LoginProfile': {
        'UserName': 'string',
        'CreateDate': datetime(2015, 1, 1),
        'PasswordResetRequired': True|False
    }
}


Response Structure

(dict) --
Contains the response to a successful  CreateLoginProfile request.

LoginProfile (dict) --
A structure containing the user name and password create date.

UserName (string) --
The name of the user, which can be used for signing in to the AWS Management Console.

CreateDate (datetime) --
The date when the password for the user was created.

PasswordResetRequired (boolean) --
Specifies whether the user is required to set a new password on next sign-in.









Exceptions

IAM.Client.exceptions.EntityAlreadyExistsException
IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.PasswordPolicyViolationException
IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command changes IAM user Bob\'s password and sets the flag that required Bob to change the password the next time he signs in.
response = client.create_login_profile(
    Password='h]6EszR}vJ*m',
    PasswordResetRequired=True,
    UserName='Bob',
)

print(response)


Expected Output:
{
    'LoginProfile': {
        'CreateDate': datetime(2015, 3, 10, 20, 55, 40, 1, 69, 0),
        'PasswordResetRequired': True,
        'UserName': 'Bob',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LoginProfile': {
            'UserName': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'PasswordResetRequired': True|False
        }
    }
    
    
    :returns: 
    IAM.Client.exceptions.EntityAlreadyExistsException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.PasswordPolicyViolationException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_open_id_connect_provider(Url=None, ClientIDList=None, ThumbprintList=None):
    """
    Creates an IAM entity to describe an identity provider (IdP) that supports OpenID Connect (OIDC) .
    The OIDC provider that you create with this operation can be used as a principal in a role\'s trust policy. Such a policy establishes a trust relationship between AWS and the OIDC provider.
    When you create the IAM OIDC provider, you specify the following:
    You get all of this information from the OIDC IdP that you want to use to access AWS.
    See also: AWS API Documentation
    
    Exceptions
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
    :param Url: [REQUIRED]\nThe URL of the identity provider. The URL must begin with https:// and should correspond to the iss claim in the provider\'s OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like https://server.example.org or https://example.com .\nYou cannot register the same provider multiple times in a single AWS account. If you try to submit a URL that has already been used for an OpenID Connect provider in the AWS account, you will get an error.\n

    :type ClientIDList: list
    :param ClientIDList: A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that\'s sent as the client_id parameter on OAuth requests.)\nYou can register multiple client IDs with the same provider. For example, you might have multiple applications that use the same OIDC provider. You cannot register more than 100 client IDs with a single IAM OIDC provider.\nThere is no defined format for a client ID. The CreateOpenIDConnectProviderRequest operation accepts client IDs up to 255 characters long.\n\n(string) --\n\n

    :type ThumbprintList: list
    :param ThumbprintList: [REQUIRED]\nA list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider\'s server certificates. Typically this list includes only one entry. However, IAM lets you have up to five thumbprints for an OIDC provider. This lets you maintain multiple thumbprints if the identity provider is rotating certificates.\nThe server certificate thumbprint is the hex-encoded SHA-1 hash value of the X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string.\nYou must provide at least one thumbprint when creating an IAM OIDC provider. For example, assume that the OIDC provider is server.example.com and the provider stores its keys at https://keys.server.example.com/openid-connect. In that case, the thumbprint string would be the hex-encoded SHA-1 hash value of the certificate used by https://keys.server.example.com.\nFor more information about obtaining the OIDC provider\'s thumbprint, see Obtaining the Thumbprint for an OpenID Connect Provider in the IAM User Guide .\n\n(string) --Contains a thumbprint for an identity provider\'s server certificate.\nThe identity provider\'s server certificate thumbprint is the hex-encoded SHA-1 hash value of the self-signed X.509 certificate. This thumbprint is used by the domain where the OpenID Connect provider makes its keys available. The thumbprint is always a 40-character string.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OpenIDConnectProviderArn': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  CreateOpenIDConnectProvider request.

OpenIDConnectProviderArn (string) --
The Amazon Resource Name (ARN) of the new IAM OpenID Connect provider that is created. For more information, see  OpenIDConnectProviderListEntry .







Exceptions

IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.EntityAlreadyExistsException
IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.ServiceFailureException

Examples
The following example defines a new OIDC provider in IAM with a client ID of my-application-id and pointing at the server with a URL of https://server.example.com.
response = client.create_open_id_connect_provider(
    ClientIDList=[
        'my-application-id',
    ],
    ThumbprintList=[
        '3768084dfb3d2b68b7897bf5f565da8efEXAMPLE',
    ],
    Url='https://server.example.com',
)

print(response)


Expected Output:
{
    'OpenIDConnectProviderArn': 'arn:aws:iam::123456789012:oidc-provider/server.example.com',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'OpenIDConnectProviderArn': 'string'
    }
    
    
    :returns: 
    Url (string) -- [REQUIRED]
    The URL of the identity provider. The URL must begin with https:// and should correspond to the iss claim in the provider\'s OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like https://server.example.org or https://example.com .
    You cannot register the same provider multiple times in a single AWS account. If you try to submit a URL that has already been used for an OpenID Connect provider in the AWS account, you will get an error.
    
    ClientIDList (list) -- A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that\'s sent as the client_id parameter on OAuth requests.)
    You can register multiple client IDs with the same provider. For example, you might have multiple applications that use the same OIDC provider. You cannot register more than 100 client IDs with a single IAM OIDC provider.
    There is no defined format for a client ID. The CreateOpenIDConnectProviderRequest operation accepts client IDs up to 255 characters long.
    
    (string) --
    
    
    ThumbprintList (list) -- [REQUIRED]
    A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider\'s server certificates. Typically this list includes only one entry. However, IAM lets you have up to five thumbprints for an OIDC provider. This lets you maintain multiple thumbprints if the identity provider is rotating certificates.
    The server certificate thumbprint is the hex-encoded SHA-1 hash value of the X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string.
    You must provide at least one thumbprint when creating an IAM OIDC provider. For example, assume that the OIDC provider is server.example.com and the provider stores its keys at https://keys.server.example.com/openid-connect. In that case, the thumbprint string would be the hex-encoded SHA-1 hash value of the certificate used by https://keys.server.example.com.
    For more information about obtaining the OIDC provider\'s thumbprint, see Obtaining the Thumbprint for an OpenID Connect Provider in the IAM User Guide .
    
    (string) --Contains a thumbprint for an identity provider\'s server certificate.
    The identity provider\'s server certificate thumbprint is the hex-encoded SHA-1 hash value of the self-signed X.509 certificate. This thumbprint is used by the domain where the OpenID Connect provider makes its keys available. The thumbprint is always a 40-character string.
    
    
    
    
    """
    pass

def create_policy(PolicyName=None, Path=None, PolicyDocument=None, Description=None):
    """
    Creates a new managed policy for your AWS account.
    This operation creates a policy version with a version identifier of v1 and sets v1 as the policy\'s default version. For more information about policy versions, see Versioning for Managed Policies in the IAM User Guide .
    For more information about managed policies in general, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_policy(
        PolicyName='string',
        Path='string',
        PolicyDocument='string',
        Description='string'
    )
    
    
    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe friendly name of the policy.\nIAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both 'MyResource' and 'myresource'.\n

    :type Path: string
    :param Path: The path for the policy.\nFor more information about paths, see IAM Identifiers in the IAM User Guide .\nThis parameter is optional. If it is not included, it defaults to a slash (/).\nThis parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type PolicyDocument: string
    :param PolicyDocument: [REQUIRED]\nThe JSON policy document that you want to use as the content for the new policy.\nYou must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n

    :type Description: string
    :param Description: A friendly description of the policy.\nTypically used to store information about the permissions defined in the policy. For example, 'Grants access to production DynamoDB tables.'\nThe policy description is immutable. After a value is assigned, it cannot be changed.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Policy': {
        'PolicyName': 'string',
        'PolicyId': 'string',
        'Arn': 'string',
        'Path': 'string',
        'DefaultVersionId': 'string',
        'AttachmentCount': 123,
        'PermissionsBoundaryUsageCount': 123,
        'IsAttachable': True|False,
        'Description': 'string',
        'CreateDate': datetime(2015, 1, 1),
        'UpdateDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Contains the response to a successful  CreatePolicy request.

Policy (dict) --
A structure containing details about the new policy.

PolicyName (string) --
The friendly name (not ARN) identifying the policy.

PolicyId (string) --
The stable and unique string identifying the policy.
For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .

Path (string) --
The path to the policy.
For more information about paths, see IAM Identifiers in the IAM User Guide .

DefaultVersionId (string) --
The identifier for the version of the policy that is set as the default version.

AttachmentCount (integer) --
The number of entities (users, groups, and roles) that the policy is attached to.

PermissionsBoundaryUsageCount (integer) --
The number of entities (users and roles) for which the policy is used to set the permissions boundary.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

IsAttachable (boolean) --
Specifies whether the policy can be attached to an IAM user, group, or role.

Description (string) --
A friendly description of the policy.
This element is included in the response to the  GetPolicy operation. It is not included in the response to the  ListPolicies operation.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the policy was created.

UpdateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the policy was last updated.
When a policy has only one version, this field contains the date and time when the policy was created. When a policy has more than one version, this field contains the date and time when the most recent policy version was created.









Exceptions

IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.EntityAlreadyExistsException
IAM.Client.exceptions.MalformedPolicyDocumentException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'Policy': {
            'PolicyName': 'string',
            'PolicyId': 'string',
            'Arn': 'string',
            'Path': 'string',
            'DefaultVersionId': 'string',
            'AttachmentCount': 123,
            'PermissionsBoundaryUsageCount': 123,
            'IsAttachable': True|False,
            'Description': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'UpdateDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.EntityAlreadyExistsException
    IAM.Client.exceptions.MalformedPolicyDocumentException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_policy_version(PolicyArn=None, PolicyDocument=None, SetAsDefault=None):
    """
    Creates a new version of the specified managed policy. To update a managed policy, you create a new policy version. A managed policy can have up to five versions. If the policy has five versions, you must delete an existing version using  DeletePolicyVersion before you create a new version.
    Optionally, you can set the new version as the policy\'s default version. The default version is the version that is in effect for the IAM users, groups, and roles to which the policy is attached.
    For more information about managed policy versions, see Versioning for Managed Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_policy_version(
        PolicyArn='string',
        PolicyDocument='string',
        SetAsDefault=True|False
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM policy to which you want to add a new version.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :type PolicyDocument: string
    :param PolicyDocument: [REQUIRED]\nThe JSON policy document that you want to use as the content for this new version of the policy.\nYou must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n

    :type SetAsDefault: boolean
    :param SetAsDefault: Specifies whether to set this version as the policy\'s default version.\nWhen this parameter is true , the new policy version becomes the operative version. That is, it becomes the version that is in effect for the IAM users, groups, and roles that the policy is attached to.\nFor more information about managed policy versions, see Versioning for Managed Policies in the IAM User Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PolicyVersion': {
        'Document': 'string',
        'VersionId': 'string',
        'IsDefaultVersion': True|False,
        'CreateDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Contains the response to a successful  CreatePolicyVersion request.

PolicyVersion (dict) --
A structure containing details about the new policy version.

Document (string) --
The policy document.
The policy document is returned in the response to the  GetPolicyVersion and  GetAccountAuthorizationDetails operations. It is not returned in the response to the  CreatePolicyVersion or  ListPolicyVersions operations.
The policy document returned in this structure is URL-encoded compliant with RFC 3986 . You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the decode method of the java.net.URLDecoder utility class in the Java SDK. Other languages and SDKs provide similar functionality.

VersionId (string) --
The identifier for the policy version.
Policy version identifiers always begin with v (always lowercase). When a policy is created, the first policy version is v1 .

IsDefaultVersion (boolean) --
Specifies whether the policy version is set as the policy\'s default version.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the policy version was created.









Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.MalformedPolicyDocumentException
IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'PolicyVersion': {
            'Document': 'string',
            'VersionId': 'string',
            'IsDefaultVersion': True|False,
            'CreateDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.MalformedPolicyDocumentException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_role(Path=None, RoleName=None, AssumeRolePolicyDocument=None, Description=None, MaxSessionDuration=None, PermissionsBoundary=None, Tags=None):
    """
    Creates a new role for your AWS account. For more information about roles, go to IAM Roles . For information about limitations on role names and the number of roles you can create, go to Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command creates a role named Test-Role and attaches a trust policy to it that is provided as a URL-encoded JSON string.
    Expected Output:
    
    :example: response = client.create_role(
        Path='string',
        RoleName='string',
        AssumeRolePolicyDocument='string',
        Description='string',
        MaxSessionDuration=123,
        PermissionsBoundary='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Path: string
    :param Path: The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide .\nThis parameter is optional. If it is not included, it defaults to a slash (/).\nThis parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the role to create.\nIAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both 'MyResource' and 'myresource'.\n

    :type AssumeRolePolicyDocument: string
    :param AssumeRolePolicyDocument: [REQUIRED]\nThe trust relationship policy document that grants an entity permission to assume the role.\nIn IAM, you must provide a JSON policy that has been converted to a string. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\nUpon success, the response includes the same trust policy in JSON format.\n

    :type Description: string
    :param Description: A description of the role.

    :type MaxSessionDuration: integer
    :param MaxSessionDuration: The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.\nAnyone who assumes the role from the AWS CLI or API can use the DurationSeconds API parameter or the duration-seconds CLI parameter to request a longer session. The MaxSessionDuration setting determines the maximum duration that can be requested using the DurationSeconds parameter. If users don\'t specify a value for the DurationSeconds parameter, their security credentials are valid for one hour by default. This applies when you use the AssumeRole* API operations or the assume-role* CLI operations but does not apply when you use those operations to create a console URL. For more information, see Using IAM Roles in the IAM User Guide .\n

    :type PermissionsBoundary: string
    :param PermissionsBoundary: The ARN of the policy that is used to set the permissions boundary for the role.

    :type Tags: list
    :param Tags: A list of tags that you want to attach to the newly created role. Each tag consists of a key name and an associated value. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .\n\nNote\nIf any one of the tags is invalid or if you exceed the allowed number of tags per role, then the entire request fails and the role is not created.\n\n\n(dict) --A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .\n\nKey (string) -- [REQUIRED]The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.\n\nValue (string) -- [REQUIRED]The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.\n\nNote\nAWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Role': {
        'Path': 'string',
        'RoleName': 'string',
        'RoleId': 'string',
        'Arn': 'string',
        'CreateDate': datetime(2015, 1, 1),
        'AssumeRolePolicyDocument': 'string',
        'Description': 'string',
        'MaxSessionDuration': 123,
        'PermissionsBoundary': {
            'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
            'PermissionsBoundaryArn': 'string'
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'RoleLastUsed': {
            'LastUsedDate': datetime(2015, 1, 1),
            'Region': 'string'
        }
    }
}


Response Structure

(dict) --
Contains the response to a successful  CreateRole request.

Role (dict) --
A structure containing details about the new role.

Path (string) --
The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide .

RoleName (string) --
The friendly name that identifies the role.

RoleId (string) --
The stable and unique string identifying the role. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide guide.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the role was created.

AssumeRolePolicyDocument (string) --
The policy that grants an entity permission to assume the role.

Description (string) --
A description of the role that you provide.

MaxSessionDuration (integer) --
The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI, or API to assume the role can specify the duration using the optional DurationSeconds API parameter or duration-seconds CLI parameter.

PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the role.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are attached to the specified role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.






RoleLastUsed (dict) --
Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see Regions Where Data Is Tracked in the IAM User Guide .

LastUsedDate (datetime) --
The date and time, in ISO 8601 date-time format that the role was last used.
This field is null if the role has not been used within the IAM tracking period. For more information about the tracking period, see Regions Where Data Is Tracked in the IAM User Guide .

Region (string) --
The name of the AWS Region in which the role was last used.











Exceptions

IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.EntityAlreadyExistsException
IAM.Client.exceptions.MalformedPolicyDocumentException
IAM.Client.exceptions.ConcurrentModificationException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command creates a role named Test-Role and attaches a trust policy to it that is provided as a URL-encoded JSON string.
response = client.create_role(
    AssumeRolePolicyDocument='<URL-encoded-JSON>',
    Path='/',
    RoleName='Test-Role',
)

print(response)


Expected Output:
{
    'Role': {
        'Arn': 'arn:aws:iam::123456789012:role/Test-Role',
        'AssumeRolePolicyDocument': '<URL-encoded-JSON>',
        'CreateDate': datetime(2013, 6, 7, 20, 43, 32, 4, 158, 0),
        'Path': '/',
        'RoleId': 'AKIAIOSFODNN7EXAMPLE',
        'RoleName': 'Test-Role',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Role': {
            'Path': 'string',
            'RoleName': 'string',
            'RoleId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'AssumeRolePolicyDocument': 'string',
            'Description': 'string',
            'MaxSessionDuration': 123,
            'PermissionsBoundary': {
                'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                'PermissionsBoundaryArn': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'RoleLastUsed': {
                'LastUsedDate': datetime(2015, 1, 1),
                'Region': 'string'
            }
        }
    }
    
    
    :returns: 
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.EntityAlreadyExistsException
    IAM.Client.exceptions.MalformedPolicyDocumentException
    IAM.Client.exceptions.ConcurrentModificationException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_saml_provider(SAMLMetadataDocument=None, Name=None):
    """
    Creates an IAM resource that describes an identity provider (IdP) that supports SAML 2.0.
    The SAML provider resource that you create with this operation can be used as a principal in an IAM role\'s trust policy. Such a policy can enable federated users who sign in using the SAML IdP to assume the role. You can create an IAM role that supports Web-based single sign-on (SSO) to the AWS Management Console or one that supports API access to AWS.
    When you create the SAML provider resource, you upload a SAML metadata document that you get from your IdP. That document includes the issuer\'s name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that the IdP sends. You must generate the metadata document using the identity management software that is used as your organization\'s IdP.
    For more information, see Enabling SAML 2.0 Federated Users to Access the AWS Management Console and About SAML 2.0-based Federation in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_saml_provider(
        SAMLMetadataDocument='string',
        Name='string'
    )
    
    
    :type SAMLMetadataDocument: string
    :param SAMLMetadataDocument: [REQUIRED]\nAn XML document generated by an identity provider (IdP) that supports SAML 2.0. The document includes the issuer\'s name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that are received from the IdP. You must generate the metadata document using the identity management software that is used as your organization\'s IdP.\nFor more information, see About SAML 2.0-based Federation in the IAM User Guide\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the provider to create.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SAMLProviderArn': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  CreateSAMLProvider request.

SAMLProviderArn (string) --
The Amazon Resource Name (ARN) of the new SAML provider resource in IAM.







Exceptions

IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.EntityAlreadyExistsException
IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'SAMLProviderArn': 'string'
    }
    
    
    :returns: 
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.EntityAlreadyExistsException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_service_linked_role(AWSServiceName=None, Description=None, CustomSuffix=None):
    """
    Creates an IAM role that is linked to a specific AWS service. The service controls the attached policies and when the role can be deleted. This helps ensure that the service is not broken by an unexpectedly changed or deleted role, which could put your AWS resources into an unknown state. Allowing the service to control the role helps improve service stability and proper cleanup when a service and its role are no longer needed. For more information, see Using Service-Linked Roles in the IAM User Guide .
    To attach a policy to this service-linked role, you must make the request using the AWS service that depends on this role.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_service_linked_role(
        AWSServiceName='string',
        Description='string',
        CustomSuffix='string'
    )
    
    
    :type AWSServiceName: string
    :param AWSServiceName: [REQUIRED]\nThe service principal for the AWS service to which this role is attached. You use a string similar to a URL but without the http:// in front. For example: elasticbeanstalk.amazonaws.com .\nService principals are unique and case-sensitive. To find the exact service principal for your service-linked role, see AWS Services That Work with IAM in the IAM User Guide . Look for the services that have Yes in the Service-Linked Role column. Choose the Yes link to view the service-linked role documentation for that service.\n

    :type Description: string
    :param Description: The description of the role.

    :type CustomSuffix: string
    :param CustomSuffix: A string that you provide, which is combined with the service-provided prefix to form the complete role name. If you make multiple requests for the same service, then you must supply a different CustomSuffix for each request. Otherwise the request fails with a duplicate role name error. For example, you could add -1 or -debug to the suffix.\nSome services do not support the CustomSuffix parameter. If you provide an optional suffix and the operation fails, try the operation again without the suffix.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Role': {
        'Path': 'string',
        'RoleName': 'string',
        'RoleId': 'string',
        'Arn': 'string',
        'CreateDate': datetime(2015, 1, 1),
        'AssumeRolePolicyDocument': 'string',
        'Description': 'string',
        'MaxSessionDuration': 123,
        'PermissionsBoundary': {
            'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
            'PermissionsBoundaryArn': 'string'
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'RoleLastUsed': {
            'LastUsedDate': datetime(2015, 1, 1),
            'Region': 'string'
        }
    }
}


Response Structure

(dict) --

Role (dict) --
A  Role object that contains details about the newly created role.

Path (string) --
The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide .

RoleName (string) --
The friendly name that identifies the role.

RoleId (string) --
The stable and unique string identifying the role. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide guide.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the role was created.

AssumeRolePolicyDocument (string) --
The policy that grants an entity permission to assume the role.

Description (string) --
A description of the role that you provide.

MaxSessionDuration (integer) --
The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI, or API to assume the role can specify the duration using the optional DurationSeconds API parameter or duration-seconds CLI parameter.

PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the role.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are attached to the specified role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.






RoleLastUsed (dict) --
Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see Regions Where Data Is Tracked in the IAM User Guide .

LastUsedDate (datetime) --
The date and time, in ISO 8601 date-time format that the role was last used.
This field is null if the role has not been used within the IAM tracking period. For more information about the tracking period, see Regions Where Data Is Tracked in the IAM User Guide .

Region (string) --
The name of the AWS Region in which the role was last used.











Exceptions

IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'Role': {
            'Path': 'string',
            'RoleName': 'string',
            'RoleId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'AssumeRolePolicyDocument': 'string',
            'Description': 'string',
            'MaxSessionDuration': 123,
            'PermissionsBoundary': {
                'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                'PermissionsBoundaryArn': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'RoleLastUsed': {
                'LastUsedDate': datetime(2015, 1, 1),
                'Region': 'string'
            }
        }
    }
    
    
    :returns: 
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
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
    
    Exceptions
    
    :example: response = client.create_service_specific_credential(
        UserName='string',
        ServiceName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the IAM user that is to be associated with the credentials. The new service-specific credentials have the same permissions as the associated user except that they can be used only to access the specified service.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type ServiceName: string
    :param ServiceName: [REQUIRED]\nThe name of the AWS service that is to be associated with the credentials. The service you specify here is the only service that can be accessed using these credentials.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ServiceSpecificCredential (dict) --
A structure that contains information about the newly created service-specific credential.

Warning
This is the only time that the password for this credential set is available. It cannot be recovered later. Instead, you must reset the password with  ResetServiceSpecificCredential .


CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the service-specific credential were created.

ServiceName (string) --
The name of the service associated with the service-specific credential.

ServiceUserName (string) --
The generated user name for the service-specific credential. This value is generated by combining the IAM user\'s name combined with the ID number of the AWS account, as in jane-at-123456789012 , for example. This value cannot be configured by the user.

ServicePassword (string) --
The generated password for the service-specific credential.

ServiceSpecificCredentialId (string) --
The unique identifier for the service-specific credential.

UserName (string) --
The name of the IAM user associated with the service-specific credential.

Status (string) --
The status of the service-specific credential. Active means that the key is valid for API calls, while Inactive means it is not.









Exceptions

IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceNotSupportedException


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
    
    
    :returns: 
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceNotSupportedException
    
    """
    pass

def create_user(Path=None, UserName=None, PermissionsBoundary=None, Tags=None):
    """
    Creates a new IAM user for your AWS account.
    For information about limitations on the number of IAM users you can create, see Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following create-user command creates an IAM user named Bob in the current account.
    Expected Output:
    
    :example: response = client.create_user(
        Path='string',
        UserName='string',
        PermissionsBoundary='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Path: string
    :param Path: The path for the user name. For more information about paths, see IAM Identifiers in the IAM User Guide .\nThis parameter is optional. If it is not included, it defaults to a slash (/).\nThis parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user to create.\nIAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both 'MyResource' and 'myresource'.\n

    :type PermissionsBoundary: string
    :param PermissionsBoundary: The ARN of the policy that is used to set the permissions boundary for the user.

    :type Tags: list
    :param Tags: A list of tags that you want to attach to the newly created user. Each tag consists of a key name and an associated value. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .\n\nNote\nIf any one of the tags is invalid or if you exceed the allowed number of tags per user, then the entire request fails and the user is not created.\n\n\n(dict) --A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .\n\nKey (string) -- [REQUIRED]The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.\n\nValue (string) -- [REQUIRED]The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.\n\nNote\nAWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'User': {
        'Path': 'string',
        'UserName': 'string',
        'UserId': 'string',
        'Arn': 'string',
        'CreateDate': datetime(2015, 1, 1),
        'PasswordLastUsed': datetime(2015, 1, 1),
        'PermissionsBoundary': {
            'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
            'PermissionsBoundaryArn': 'string'
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Contains the response to a successful  CreateUser request.

User (dict) --
A structure with details about the new IAM user.

Path (string) --
The path to the user. For more information about paths, see IAM Identifiers in the IAM User Guide .

UserName (string) --
The friendly name identifying the user.

UserId (string) --
The stable and unique string identifying the user. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the user was created.

PasswordLastUsed (datetime) --
The date and time, in ISO 8601 date-time format , when the user\'s password was last used to sign in to an AWS website. For a list of AWS websites that capture a user\'s last sign-in time, see the Credential Reports topic in the IAM User Guide . If a password is used more than once in a five-minute span, only the first use is returned in this field. If the field is null (no value), then it indicates that they never signed in with a password. This can be because:

The user never had a password.
A password exists but has not been used since IAM started tracking this information on October 20, 2014.

A null value does not mean that the user never had a password. Also, if the user does not currently have a password but had one in the past, then this field contains the date and time the most recent password was used.
This value is returned only in the  GetUser and  ListUsers operations.

PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the user.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are associated with the specified user. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.














Exceptions

IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.EntityAlreadyExistsException
IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.ConcurrentModificationException
IAM.Client.exceptions.ServiceFailureException

Examples
The following create-user command creates an IAM user named Bob in the current account.
response = client.create_user(
    UserName='Bob',
)

print(response)


Expected Output:
{
    'User': {
        'Arn': 'arn:aws:iam::123456789012:user/Bob',
        'CreateDate': datetime(2013, 6, 8, 3, 20, 41, 5, 159, 0),
        'Path': '/',
        'UserId': 'AKIAIOSFODNN7EXAMPLE',
        'UserName': 'Bob',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'User': {
            'Path': 'string',
            'UserName': 'string',
            'UserId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'PasswordLastUsed': datetime(2015, 1, 1),
            'PermissionsBoundary': {
                'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                'PermissionsBoundaryArn': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    The user never had a password.
    A password exists but has not been used since IAM started tracking this information on October 20, 2014.
    
    """
    pass

def create_virtual_mfa_device(Path=None, VirtualMFADeviceName=None):
    """
    Creates a new virtual MFA device for the AWS account. After creating the virtual MFA, use  EnableMFADevice to attach the MFA device to an IAM user. For more information about creating and working with virtual MFA devices, go to Using a Virtual MFA Device in the IAM User Guide .
    For information about limits on the number of MFA devices you can create, see Limitations on Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_virtual_mfa_device(
        Path='string',
        VirtualMFADeviceName='string'
    )
    
    
    :type Path: string
    :param Path: The path for the virtual MFA device. For more information about paths, see IAM Identifiers in the IAM User Guide .\nThis parameter is optional. If it is not included, it defaults to a slash (/).\nThis parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type VirtualMFADeviceName: string
    :param VirtualMFADeviceName: [REQUIRED]\nThe name of the virtual MFA device. Use with path to uniquely identify a virtual MFA device.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :rtype: dict

ReturnsResponse Syntax
{
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
            'PasswordLastUsed': datetime(2015, 1, 1),
            'PermissionsBoundary': {
                'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                'PermissionsBoundaryArn': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
        'EnableDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Contains the response to a successful  CreateVirtualMFADevice request.

VirtualMFADevice (dict) --
A structure containing details about the new virtual MFA device.

SerialNumber (string) --
The serial number associated with VirtualMFADevice .

Base32StringSeed (bytes) --
The base32 seed defined as specified in RFC3548 . The Base32StringSeed is base64-encoded.

QRCodePNG (bytes) --
A QR code PNG image that encodes otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String where $virtualMFADeviceName is one of the create call arguments. AccountName is the user name if set (otherwise, the account ID otherwise), and Base32String is the seed in base32 format. The Base32String value is base64-encoded.

User (dict) --
The IAM user associated with this virtual MFA device.

Path (string) --
The path to the user. For more information about paths, see IAM Identifiers in the IAM User Guide .

UserName (string) --
The friendly name identifying the user.

UserId (string) --
The stable and unique string identifying the user. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the user was created.

PasswordLastUsed (datetime) --
The date and time, in ISO 8601 date-time format , when the user\'s password was last used to sign in to an AWS website. For a list of AWS websites that capture a user\'s last sign-in time, see the Credential Reports topic in the IAM User Guide . If a password is used more than once in a five-minute span, only the first use is returned in this field. If the field is null (no value), then it indicates that they never signed in with a password. This can be because:

The user never had a password.
A password exists but has not been used since IAM started tracking this information on October 20, 2014.

A null value does not mean that the user never had a password. Also, if the user does not currently have a password but had one in the past, then this field contains the date and time the most recent password was used.
This value is returned only in the  GetUser and  ListUsers operations.

PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the user.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are associated with the specified user. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.








EnableDate (datetime) --
The date and time on which the virtual MFA device was enabled.









Exceptions

IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.EntityAlreadyExistsException
IAM.Client.exceptions.ServiceFailureException


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
                'PasswordLastUsed': datetime(2015, 1, 1),
                'PermissionsBoundary': {
                    'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                    'PermissionsBoundaryArn': 'string'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
            'EnableDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    The user never had a password.
    A password exists but has not been used since IAM started tracking this information on October 20, 2014.
    
    """
    pass

def deactivate_mfa_device(UserName=None, SerialNumber=None):
    """
    Deactivates the specified MFA device and removes it from association with the user name for which it was originally enabled.
    For more information about creating and working with virtual MFA devices, go to Enabling a Virtual Multi-factor Authentication (MFA) Device in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deactivate_mfa_device(
        UserName='string',
        SerialNumber='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user whose MFA device you want to deactivate.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type SerialNumber: string
    :param SerialNumber: [REQUIRED]\nThe serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@:/-\n

    :returns: 
    IAM.Client.exceptions.EntityTemporarilyUnmodifiableException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_access_key(UserName=None, AccessKeyId=None):
    """
    Deletes the access key pair associated with the specified IAM user.
    If you do not specify a user name, IAM determines the user name implicitly based on the AWS access key ID signing the request. This operation works for access keys under the AWS account. Consequently, you can use this operation to manage AWS account root user credentials even if the AWS account has no associated users.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command deletes one access key (access key ID and secret access key) assigned to the IAM user named Bob.
    Expected Output:
    
    :example: response = client.delete_access_key(
        UserName='string',
        AccessKeyId='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the user whose access key pair you want to delete.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type AccessKeyId: string
    :param AccessKeyId: [REQUIRED]\nThe access key ID for the access key ID and secret access key you want to delete.\nThis parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.\n

    :return: response = client.delete_access_key(
        AccessKeyId='AKIDPMS9RO4H3FEXAMPLE',
        UserName='Bob',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_account_alias(AccountAlias=None):
    """
    Deletes the specified AWS account alias. For information about using an AWS account alias, see Using an Alias for Your AWS Account ID in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command removes the alias mycompany from the current AWS account:
    Expected Output:
    
    :example: response = client.delete_account_alias(
        AccountAlias='string'
    )
    
    
    :type AccountAlias: string
    :param AccountAlias: [REQUIRED]\nThe name of the account alias to delete.\nThis parameter allows (through its regex pattern ) a string of characters consisting of lowercase letters, digits, and dashes. You cannot start or finish with a dash, nor can you have two dashes in a row.\n

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
    
    Exceptions
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
    
    Exceptions
    
    :example: response = client.delete_group(
        GroupName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the IAM group to delete.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    """
    pass

def delete_group_policy(GroupName=None, PolicyName=None):
    """
    Deletes the specified inline policy that is embedded in the specified IAM group.
    A group can also have managed policies attached to it. To detach a managed policy from a group, use  DetachGroupPolicy . For more information about policies, refer to Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command deletes the policy named ExamplePolicy from the group named Admins:
    Expected Output:
    
    :example: response = client.delete_group_policy(
        GroupName='string',
        PolicyName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name (friendly name, not ARN) identifying the group that the policy is embedded in.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name identifying the policy document to delete.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :return: response = client.delete_group_policy(
        GroupName='Admins',
        PolicyName='ExamplePolicy',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_instance_profile(InstanceProfileName=None):
    """
    Deletes the specified instance profile. The instance profile must not have an associated role.
    For more information about instance profiles, go to About Instance Profiles .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command deletes the instance profile named ExampleInstanceProfile
    Expected Output:
    
    :example: response = client.delete_instance_profile(
        InstanceProfileName='string'
    )
    
    
    :type InstanceProfileName: string
    :param InstanceProfileName: [REQUIRED]\nThe name of the instance profile to delete.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :return: response = client.delete_instance_profile(
        InstanceProfileName='ExampleInstanceProfile',
    )
    
    print(response)
    
    
    """
    pass

def delete_login_profile(UserName=None):
    """
    Deletes the password for the specified IAM user, which terminates the user\'s ability to access AWS services through the AWS Management Console.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command deletes the password for the IAM user named Bob.
    Expected Output:
    
    :example: response = client.delete_login_profile(
        UserName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user whose password you want to delete.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

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
    This operation is idempotent; it does not fail or return an error if you call the operation for a provider that does not exist.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_open_id_connect_provider(
        OpenIDConnectProviderArn='string'
    )
    
    
    :type OpenIDConnectProviderArn: string
    :param OpenIDConnectProviderArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM OpenID Connect provider resource object to delete. You can get a list of OpenID Connect provider resource ARNs by using the ListOpenIDConnectProviders operation.\n

    """
    pass

def delete_policy(PolicyArn=None):
    """
    Deletes the specified managed policy.
    Before you can delete a managed policy, you must first detach the policy from all users, groups, and roles that it is attached to. In addition, you must delete all the policy\'s versions. The following steps describe the process for deleting a managed policy:
    For information about managed policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_policy(
        PolicyArn='string'
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM policy you want to delete.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.DeleteConflictException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_policy_version(PolicyArn=None, VersionId=None):
    """
    Deletes the specified version from the specified managed policy.
    You cannot delete the default version from a policy using this API. To delete the default version from a policy, use  DeletePolicy . To find out which version of a policy is marked as the default version, use  ListPolicyVersions .
    For information about versions for managed policies, see Versioning for Managed Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_policy_version(
        PolicyArn='string',
        VersionId='string'
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM policy from which you want to delete a version.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :type VersionId: string
    :param VersionId: [REQUIRED]\nThe policy version to delete.\nThis parameter allows (through its regex pattern ) a string of characters that consists of the lowercase letter \'v\' followed by one or two digits, and optionally followed by a period \'.\' and a string of letters and digits.\nFor more information about managed policy versions, see Versioning for Managed Policies in the IAM User Guide .\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.DeleteConflictException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_role(RoleName=None):
    """
    Deletes the specified role. The role must not have any policies attached. For more information about roles, go to Working with Roles .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command removes the role named Test-Role.
    Expected Output:
    
    :example: response = client.delete_role(
        RoleName='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the role to delete.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :return: response = client.delete_role(
        RoleName='Test-Role',
    )
    
    print(response)
    
    
    """
    pass

def delete_role_permissions_boundary(RoleName=None):
    """
    Deletes the permissions boundary for the specified IAM role.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_role_permissions_boundary(
        RoleName='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name (friendly name, not ARN) of the IAM role from which you want to remove the permissions boundary.\n

    """
    pass

def delete_role_policy(RoleName=None, PolicyName=None):
    """
    Deletes the specified inline policy that is embedded in the specified IAM role.
    A role can also have managed policies attached to it. To detach a managed policy from a role, use  DetachRolePolicy . For more information about policies, refer to Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command removes the policy named ExamplePolicy from the role named Test-Role.
    Expected Output:
    
    :example: response = client.delete_role_policy(
        RoleName='string',
        PolicyName='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name (friendly name, not ARN) identifying the role that the policy is embedded in.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the inline policy to delete from the specified IAM role.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :return: response = client.delete_role_policy(
        PolicyName='ExamplePolicy',
        RoleName='Test-Role',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.UnmodifiableEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_saml_provider(SAMLProviderArn=None):
    """
    Deletes a SAML provider resource in IAM.
    Deleting the provider resource from IAM does not update any roles that reference the SAML provider resource\'s ARN as a principal in their trust policies. Any attempt to assume a role that references a non-existent provider resource ARN fails.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_saml_provider(
        SAMLProviderArn='string'
    )
    
    
    :type SAMLProviderArn: string
    :param SAMLProviderArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the SAML provider to delete.\n

    """
    pass

def delete_server_certificate(ServerCertificateName=None):
    """
    Deletes the specified server certificate.
    For more information about working with server certificates, see Working with Server Certificates in the IAM User Guide . This topic also includes a list of AWS services that can use the server certificates that you manage with IAM.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_server_certificate(
        ServerCertificateName='string'
    )
    
    
    :type ServerCertificateName: string
    :param ServerCertificateName: [REQUIRED]\nThe name of the server certificate you want to delete.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    """
    pass

def delete_service_linked_role(RoleName=None):
    """
    Submits a service-linked role deletion request and returns a DeletionTaskId , which you can use to check the status of the deletion. Before you call this operation, confirm that the role has no active sessions and that any resources used by the role in the linked service are deleted. If you call this operation more than once for the same service-linked role and an earlier deletion task is not complete, then the DeletionTaskId of the earlier request is returned.
    If you submit a deletion request for a service-linked role whose linked service is still accessing a resource, then the deletion task fails. If it fails, the  GetServiceLinkedRoleDeletionStatus API operation returns the reason for the failure, usually including the resources that must be deleted. To delete the service-linked role, you must first remove those resources from the linked service and then submit the deletion request again. Resources are specific to the service that is linked to the role. For more information about removing resources from a service, see the AWS documentation for your service.
    For more information about service-linked roles, see Roles Terms and Concepts: AWS Service-Linked Role in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_service_linked_role(
        RoleName='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the service-linked role to be deleted.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DeletionTaskId': 'string'
}


Response Structure

(dict) --
DeletionTaskId (string) --The deletion task identifier that you can use to check the status of the deletion. This identifier is returned in the format task/aws-service-role/<service-principal-name>/<role-name>/<task-uuid> .






Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'DeletionTaskId': 'string'
    }
    
    
    """
    pass

def delete_service_specific_credential(UserName=None, ServiceSpecificCredentialId=None):
    """
    Deletes the specified service-specific credential.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_service_specific_credential(
        UserName='string',
        ServiceSpecificCredentialId='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the IAM user associated with the service-specific credential. If this value is not specified, then the operation assumes the user whose credentials are used to call the operation.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type ServiceSpecificCredentialId: string
    :param ServiceSpecificCredentialId: [REQUIRED]\nThe unique identifier of the service-specific credential. You can get this value by calling ListServiceSpecificCredentials .\nThis parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    
    """
    pass

def delete_signing_certificate(UserName=None, CertificateId=None):
    """
    Deletes a signing certificate associated with the specified IAM user.
    If you do not specify a user name, IAM determines the user name implicitly based on the AWS access key ID signing the request. This operation works for access keys under the AWS account. Consequently, you can use this operation to manage AWS account root user credentials even if the AWS account has no associated IAM users.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command deletes the specified signing certificate for the IAM user named Anika.
    Expected Output:
    
    :example: response = client.delete_signing_certificate(
        UserName='string',
        CertificateId='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the user the signing certificate belongs to.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type CertificateId: string
    :param CertificateId: [REQUIRED]\nThe ID of the signing certificate to delete.\nThe format of this parameter, as described by its regex pattern, is a string of characters that can be upper- or lower-cased letters or digits.\n

    :return: response = client.delete_signing_certificate(
        CertificateId='TA7SMP42TDN5Z26OBPJE7EXAMPLE',
        UserName='Anika',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_ssh_public_key(UserName=None, SSHPublicKeyId=None):
    """
    Deletes the specified SSH public key.
    The SSH public key deleted by this operation is used only for authenticating the associated IAM user to an AWS CodeCommit repository. For more information about using SSH keys to authenticate to an AWS CodeCommit repository, see Set up AWS CodeCommit for SSH Connections in the AWS CodeCommit User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_ssh_public_key(
        UserName='string',
        SSHPublicKeyId='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the IAM user associated with the SSH public key.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type SSHPublicKeyId: string
    :param SSHPublicKeyId: [REQUIRED]\nThe unique identifier for the SSH public key.\nThis parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    
    """
    pass

def delete_user(UserName=None):
    """
    Deletes the specified IAM user. Unlike the AWS Management Console, when you delete a user programmatically, you must delete the items attached to the user manually, or the deletion fails. For more information, see Deleting an IAM User . Before attempting to delete a user, remove the following items:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command removes the IAM user named Bob from the current account.
    Expected Output:
    
    :example: response = client.delete_user(
        UserName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user to delete.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :return: response = client.delete_user(
        UserName='Bob',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.DeleteConflictException
    IAM.Client.exceptions.ConcurrentModificationException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_user_permissions_boundary(UserName=None):
    """
    Deletes the permissions boundary for the specified IAM user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user_permissions_boundary(
        UserName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name (friendly name, not ARN) of the IAM user from which you want to remove the permissions boundary.\n

    """
    pass

def delete_user_policy(UserName=None, PolicyName=None):
    """
    Deletes the specified inline policy that is embedded in the specified IAM user.
    A user can also have managed policies attached to it. To detach a managed policy from a user, use  DetachUserPolicy . For more information about policies, refer to Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following delete-user-policy command removes the specified policy from the IAM user named Juan:
    Expected Output:
    
    :example: response = client.delete_user_policy(
        UserName='string',
        PolicyName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name (friendly name, not ARN) identifying the user that the policy is embedded in.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name identifying the policy document to delete.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :return: response = client.delete_user_policy(
        PolicyName='ExamplePolicy',
        UserName='Juan',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_virtual_mfa_device(SerialNumber=None):
    """
    Deletes a virtual MFA device.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following delete-virtual-mfa-device command removes the specified MFA device from the current AWS account.
    Expected Output:
    
    :example: response = client.delete_virtual_mfa_device(
        SerialNumber='string'
    )
    
    
    :type SerialNumber: string
    :param SerialNumber: [REQUIRED]\nThe serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the same as the ARN.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@:/-\n

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
    
    Exceptions
    
    :example: response = client.detach_group_policy(
        GroupName='string',
        PolicyArn='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name (friendly name, not ARN) of the IAM group to detach the policy from.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM policy you want to detach.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def detach_role_policy(RoleName=None, PolicyArn=None):
    """
    Removes the specified managed policy from the specified role.
    A role can also have inline policies embedded with it. To delete an inline policy, use the  DeleteRolePolicy API. For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detach_role_policy(
        RoleName='string',
        PolicyArn='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name (friendly name, not ARN) of the IAM role to detach the policy from.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM policy you want to detach.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.UnmodifiableEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def detach_user_policy(UserName=None, PolicyArn=None):
    """
    Removes the specified managed policy from the specified user.
    A user can also have inline policies embedded with it. To delete an inline policy, use the  DeleteUserPolicy API. For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detach_user_policy(
        UserName='string',
        PolicyArn='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name (friendly name, not ARN) of the IAM user to detach the policy from.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM policy you want to detach.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def enable_mfa_device(UserName=None, SerialNumber=None, AuthenticationCode1=None, AuthenticationCode2=None):
    """
    Enables the specified MFA device and associates it with the specified IAM user. When enabled, the MFA device is required for every subsequent login by the IAM user associated with the device.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_mfa_device(
        UserName='string',
        SerialNumber='string',
        AuthenticationCode1='string',
        AuthenticationCode2='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the IAM user for whom you want to enable the MFA device.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type SerialNumber: string
    :param SerialNumber: [REQUIRED]\nThe serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@:/-\n

    :type AuthenticationCode1: string
    :param AuthenticationCode1: [REQUIRED]\nAn authentication code emitted by the device.\nThe format for this parameter is a string of six digits.\n\nWarning\nSubmit your request immediately after generating the authentication codes. If you generate the codes and then wait too long to submit the request, the MFA device successfully associates with the user but the MFA device becomes out of sync. This happens because time-based one-time passwords (TOTP) expire after a short period of time. If this happens, you can resync the device .\n\n

    :type AuthenticationCode2: string
    :param AuthenticationCode2: [REQUIRED]\nA subsequent authentication code emitted by the device.\nThe format for this parameter is a string of six digits.\n\nWarning\nSubmit your request immediately after generating the authentication codes. If you generate the codes and then wait too long to submit the request, the MFA device successfully associates with the user but the MFA device becomes out of sync. This happens because time-based one-time passwords (TOTP) expire after a short period of time. If this happens, you can resync the device .\n\n

    :returns: 
    IAM.Client.exceptions.EntityAlreadyExistsException
    IAM.Client.exceptions.EntityTemporarilyUnmodifiableException
    IAM.Client.exceptions.InvalidAuthenticationCodeException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def generate_credential_report():
    """
    Generates a credential report for the AWS account. For more information about the credential report, see Getting Credential Reports in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.generate_credential_report()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'State': 'STARTED'|'INPROGRESS'|'COMPLETE',
    'Description': 'string'
}


Response Structure

(dict) --Contains the response to a successful  GenerateCredentialReport request.

State (string) --Information about the state of the credential report.

Description (string) --Information about the credential report.






Exceptions

IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'State': 'STARTED'|'INPROGRESS'|'COMPLETE',
        'Description': 'string'
    }
    
    
    """
    pass

def generate_organizations_access_report(EntityPath=None, OrganizationsPolicyId=None):
    """
    Generates a report for service last accessed data for AWS Organizations. You can generate a report for any entities (organization root, organizational unit, or account) or policies in your organization.
    To call this operation, you must be signed in using your AWS Organizations master account credentials. You can use your long-term IAM user or root user credentials, or temporary credentials from assuming an IAM role. SCPs must be enabled for your organization root. You must have the required IAM and AWS Organizations permissions. For more information, see Refining Permissions Using Service Last Accessed Data in the IAM User Guide .
    You can generate a service last accessed data report for entities by specifying only the entity\'s path. This data includes a list of services that are allowed by any service control policies (SCPs) that apply to the entity.
    You can generate a service last accessed data report for a policy by specifying an entity\'s path and an optional AWS Organizations policy ID. This data includes a list of services that are allowed by the specified SCP.
    For each service in both report types, the data includes the most recent account activity that the policy allows to account principals in the entity or the entity\'s children. For important information about the data, reporting period, permissions required, troubleshooting, and supported Regions see Reducing Permissions Using Service Last Accessed Data in the IAM User Guide .
    This operation returns a JobId . Use this parameter in the ``  GetOrganizationsAccessReport `` operation to check the status of the report generation. To check the status of this request, use the JobId parameter in the ``  GetOrganizationsAccessReport `` operation and test the JobStatus response parameter. When the job is complete, you can retrieve the report.
    To generate a service last accessed data report for entities, specify an entity path without specifying the optional AWS Organizations policy ID. The type of entity that you specify determines the data returned in the report.
    To generate a service last accessed data report for policies, specify an entity path and the optional AWS Organizations policy ID. The type of entity that you specify determines the data returned for each service.
    For more information about service last accessed data, see Reducing Policy Scope by Viewing User Activity in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.generate_organizations_access_report(
        EntityPath='string',
        OrganizationsPolicyId='string'
    )
    
    
    :type EntityPath: string
    :param EntityPath: [REQUIRED]\nThe path of the AWS Organizations entity (root, OU, or account). You can build an entity path using the known structure of your organization. For example, assume that your account ID is 123456789012 and its parent OU ID is ou-rge0-awsabcde . The organization root ID is r-f6g7h8i9j0example and your organization ID is o-a1b2c3d4e5 . Your entity path is o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-rge0-awsabcde/123456789012 .\n

    :type OrganizationsPolicyId: string
    :param OrganizationsPolicyId: The identifier of the AWS Organizations service control policy (SCP). This parameter is optional.\nThis ID is used to generate information about when an account principal that is limited by the SCP attempted to access an AWS service.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The job identifier that you can use in the  GetOrganizationsAccessReport operation.







Exceptions

IAM.Client.exceptions.ReportGenerationLimitExceededException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    Root \xe2\x80\x93 When you specify the root entity and a policy ID, the resulting report lists all of the services that are allowed by the specified SCP. For each service, the report includes data for all accounts in your organization to which the SCP applies. This data excludes the master account, because the master account is not limited by SCPs. If the SCP is not attached to any entities in the organization, then the report will return a list of services with no data.
    OU \xe2\x80\x93 When you specify an OU entity and a policy ID, the resulting report lists all of the services that are allowed by the specified SCP. For each service, the report includes data for all accounts in the OU or its children to which the SCP applies. This means that other accounts outside the OU that are affected by the SCP might not be included in the data. This data excludes the master account, because the master account is not limited by SCPs. If the SCP is not attached to the OU or one of its children, the report will return a list of services with no data.
    Master account \xe2\x80\x93 When you specify the master account, the resulting report lists all AWS services, because the master account is not limited by SCPs. If you specify a policy ID in the CLI or API, the policy is ignored. For each service, the report includes data for only the master account.
    Account \xe2\x80\x93 When you specify another account entity and a policy ID, the resulting report lists all of the services that are allowed by the specified SCP. For each service, the report includes data for only the specified account. This means that other accounts in the organization that are affected by the SCP might not be included in the data. If the SCP is not attached to the account, the report will return a list of services with no data.
    
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

def generate_service_last_accessed_details(Arn=None):
    """
    Generates a report that includes details about when an IAM resource (user, group, role, or policy) was last used in an attempt to access AWS services. Recent activity usually appears within four hours. IAM reports activity for the last 365 days, or less if your Region began supporting this feature within the last year. For more information, see Regions Where Data Is Tracked .
    The GenerateServiceLastAccessedDetails operation returns a JobId . Use this parameter in the following operations to retrieve the following details from your report:
    To check the status of the GenerateServiceLastAccessedDetails request, use the JobId parameter in the same operations and test the JobStatus response parameter.
    For additional information about the permissions policies that allow an identity (user, group, or role) to access specific services, use the  ListPoliciesGrantingServiceAccess operation.
    For more information about service last accessed data, see Reducing Policy Scope by Viewing User Activity in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.generate_service_last_accessed_details(
        Arn='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe ARN of the IAM resource (user, group, role, or managed policy) used to generate information about when the resource was last used in an attempt to access an AWS service.\n

    :rtype: dict
ReturnsResponse Syntax{
    'JobId': 'string'
}


Response Structure

(dict) --
JobId (string) --The JobId that you can use in the  GetServiceLastAccessedDetails or  GetServiceLastAccessedDetailsWithEntities operations. The JobId returned by GenerateServiceLastAccessedDetail must be used by the same role within a session, or by the same user when used to call GetServiceLastAccessedDetail .






Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.InvalidInputException
    
    """
    pass

def get_access_key_last_used(AccessKeyId=None):
    """
    Retrieves information about when the specified access key was last used. The information includes the date and time of last use, along with the AWS service and Region that were specified in the last request made with that key.
    See also: AWS API Documentation
    
    
    :example: response = client.get_access_key_last_used(
        AccessKeyId='string'
    )
    
    
    :type AccessKeyId: string
    :param AccessKeyId: [REQUIRED]\nThe identifier of an access key.\nThis parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.\n

    :rtype: dict
ReturnsResponse Syntax{
    'UserName': 'string',
    'AccessKeyLastUsed': {
        'LastUsedDate': datetime(2015, 1, 1),
        'ServiceName': 'string',
        'Region': 'string'
    }
}


Response Structure

(dict) --Contains the response to a successful  GetAccessKeyLastUsed request. It is also returned as a member of the  AccessKeyMetaData structure returned by the  ListAccessKeys action.

UserName (string) --The name of the AWS IAM user that owns this access key.

AccessKeyLastUsed (dict) --Contains information about the last time the access key was used.

LastUsedDate (datetime) --The date and time, in ISO 8601 date-time format , when the access key was most recently used. This field is null in the following situations:

The user does not have an access key.
An access key exists but has not been used since IAM began tracking this information.
There is no sign-in data associated with the user.


ServiceName (string) --The name of the AWS service with which this access key was most recently used. The value of this field is "N/A" in the following situations:

The user does not have an access key.
An access key exists but has not been used since IAM started tracking this information.
There is no sign-in data associated with the user.


Region (string) --The AWS Region where this access key was most recently used. The value for this field is "N/A" in the following situations:

The user does not have an access key.
An access key exists but has not been used since IAM began tracking this information.
There is no sign-in data associated with the user.

For more information about AWS Regions, see Regions and Endpoints in the Amazon Web Services General Reference.









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
    An access key exists but has not been used since IAM started tracking this information.
    There is no sign-in data associated with the user.
    
    """
    pass

def get_account_authorization_details(Filter=None, MaxItems=None, Marker=None):
    """
    Retrieves information about all IAM users, groups, roles, and policies in your AWS account, including their relationships to one another. Use this API to obtain a snapshot of the configuration of IAM permissions (users, groups, roles, and policies) in your account.
    You can optionally filter the results using the Filter parameter. You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_account_authorization_details(
        Filter=[
            'User'|'Role'|'Group'|'LocalManagedPolicy'|'AWSManagedPolicy',
        ],
        MaxItems=123,
        Marker='string'
    )
    
    
    :type Filter: list
    :param Filter: A list of entity types used to filter the results. Only the entities that match the types you specify are included in the output. Use the value LocalManagedPolicy to include customer managed policies.\nThe format for this parameter is a comma-separated (if more than one) list of strings. Each string value in the list must be one of the valid values listed below.\n\n(string) --\n\n

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :rtype: dict

ReturnsResponse Syntax
{
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
            ],
            'PermissionsBoundary': {
                'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                'PermissionsBoundaryArn': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
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
                            'Description': 'string',
                            'MaxSessionDuration': 123,
                            'PermissionsBoundary': {
                                'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                                'PermissionsBoundaryArn': 'string'
                            },
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ],
                            'RoleLastUsed': {
                                'LastUsedDate': datetime(2015, 1, 1),
                                'Region': 'string'
                            }
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
            ],
            'PermissionsBoundary': {
                'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                'PermissionsBoundaryArn': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'RoleLastUsed': {
                'LastUsedDate': datetime(2015, 1, 1),
                'Region': 'string'
            }
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
            'PermissionsBoundaryUsageCount': 123,
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


Response Structure

(dict) --
Contains the response to a successful  GetAccountAuthorizationDetails request.

UserDetailList (list) --
A list containing information about IAM users.

(dict) --
Contains information about an IAM user, including all the user\'s policies and all the IAM groups the user is in.
This data type is used as a response element in the  GetAccountAuthorizationDetails operation.

Path (string) --
The path to the user. For more information about paths, see IAM Identifiers in the IAM User Guide .

UserName (string) --
The friendly name identifying the user.

UserId (string) --
The stable and unique string identifying the user. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the user was created.

UserPolicyList (list) --
A list of the inline policies embedded in the user.

(dict) --
Contains information about an IAM policy, including the policy document.
This data type is used as a response element in the  GetAccountAuthorizationDetails operation.

PolicyName (string) --
The name of the policy.

PolicyDocument (string) --
The policy document.





GroupList (list) --
A list of IAM groups that the user is in.

(string) --


AttachedManagedPolicies (list) --
A list of the managed policies attached to the user.

(dict) --
Contains information about an attached policy.
An attached policy is a managed policy that has been attached to a user, group, or role. This data type is used as a response element in the  ListAttachedGroupPolicies ,  ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails operations.
For more information about managed policies, refer to Managed Policies and Inline Policies in the IAM User Guide .

PolicyName (string) --
The friendly name of the attached policy.

PolicyArn (string) --
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .





PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the user.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are associated with the specified user. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.










GroupDetailList (list) --
A list containing information about IAM groups.

(dict) --
Contains information about an IAM group, including all of the group\'s policies.
This data type is used as a response element in the  GetAccountAuthorizationDetails operation.

Path (string) --
The path to the group. For more information about paths, see IAM Identifiers in the IAM User Guide .

GroupName (string) --
The friendly name that identifies the group.

GroupId (string) --
The stable and unique string identifying the group. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the group was created.

GroupPolicyList (list) --
A list of the inline policies embedded in the group.

(dict) --
Contains information about an IAM policy, including the policy document.
This data type is used as a response element in the  GetAccountAuthorizationDetails operation.

PolicyName (string) --
The name of the policy.

PolicyDocument (string) --
The policy document.





AttachedManagedPolicies (list) --
A list of the managed policies attached to the group.

(dict) --
Contains information about an attached policy.
An attached policy is a managed policy that has been attached to a user, group, or role. This data type is used as a response element in the  ListAttachedGroupPolicies ,  ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails operations.
For more information about managed policies, refer to Managed Policies and Inline Policies in the IAM User Guide .

PolicyName (string) --
The friendly name of the attached policy.

PolicyArn (string) --
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .









RoleDetailList (list) --
A list containing information about IAM roles.

(dict) --
Contains information about an IAM role, including all of the role\'s policies.
This data type is used as a response element in the  GetAccountAuthorizationDetails operation.

Path (string) --
The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide .

RoleName (string) --
The friendly name that identifies the role.

RoleId (string) --
The stable and unique string identifying the role. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the role was created.

AssumeRolePolicyDocument (string) --
The trust policy that grants permission to assume the role.

InstanceProfileList (list) --
A list of instance profiles that contain this role.

(dict) --
Contains information about an instance profile.
This data type is used as a response element in the following operations:

CreateInstanceProfile
GetInstanceProfile
ListInstanceProfiles
ListInstanceProfilesForRole


Path (string) --
The path to the instance profile. For more information about paths, see IAM Identifiers in the IAM User Guide .

InstanceProfileName (string) --
The name identifying the instance profile.

InstanceProfileId (string) --
The stable and unique string identifying the instance profile. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the instance profile. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --
The date when the instance profile was created.

Roles (list) --
The role associated with the instance profile.

(dict) --
Contains information about an IAM role. This structure is returned as a response element in several API operations that interact with roles.

Path (string) --
The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide .

RoleName (string) --
The friendly name that identifies the role.

RoleId (string) --
The stable and unique string identifying the role. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide guide.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the role was created.

AssumeRolePolicyDocument (string) --
The policy that grants an entity permission to assume the role.

Description (string) --
A description of the role that you provide.

MaxSessionDuration (integer) --
The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI, or API to assume the role can specify the duration using the optional DurationSeconds API parameter or duration-seconds CLI parameter.

PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the role.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are attached to the specified role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.






RoleLastUsed (dict) --
Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see Regions Where Data Is Tracked in the IAM User Guide .

LastUsedDate (datetime) --
The date and time, in ISO 8601 date-time format that the role was last used.
This field is null if the role has not been used within the IAM tracking period. For more information about the tracking period, see Regions Where Data Is Tracked in the IAM User Guide .

Region (string) --
The name of the AWS Region in which the role was last used.











RolePolicyList (list) --
A list of inline policies embedded in the role. These policies are the role\'s access (permissions) policies.

(dict) --
Contains information about an IAM policy, including the policy document.
This data type is used as a response element in the  GetAccountAuthorizationDetails operation.

PolicyName (string) --
The name of the policy.

PolicyDocument (string) --
The policy document.





AttachedManagedPolicies (list) --
A list of managed policies attached to the role. These policies are the role\'s access (permissions) policies.

(dict) --
Contains information about an attached policy.
An attached policy is a managed policy that has been attached to a user, group, or role. This data type is used as a response element in the  ListAttachedGroupPolicies ,  ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails operations.
For more information about managed policies, refer to Managed Policies and Inline Policies in the IAM User Guide .

PolicyName (string) --
The friendly name of the attached policy.

PolicyArn (string) --
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .





PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the role.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are attached to the specified role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.






RoleLastUsed (dict) --
Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see Regions Where Data Is Tracked in the IAM User Guide .

LastUsedDate (datetime) --
The date and time, in ISO 8601 date-time format that the role was last used.
This field is null if the role has not been used within the IAM tracking period. For more information about the tracking period, see Regions Where Data Is Tracked in the IAM User Guide .

Region (string) --
The name of the AWS Region in which the role was last used.







Policies (list) --
A list containing information about managed policies.

(dict) --
Contains information about a managed policy, including the policy\'s ARN, versions, and the number of principal entities (users, groups, and roles) that the policy is attached to.
This data type is used as a response element in the  GetAccountAuthorizationDetails operation.
For more information about managed policies, see Managed Policies and Inline Policies in the IAM User Guide .

PolicyName (string) --
The friendly name (not ARN) identifying the policy.

PolicyId (string) --
The stable and unique string identifying the policy.
For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .

Path (string) --
The path to the policy.
For more information about paths, see IAM Identifiers in the IAM User Guide .

DefaultVersionId (string) --
The identifier for the version of the policy that is set as the default (operative) version.
For more information about policy versions, see Versioning for Managed Policies in the IAM User Guide .

AttachmentCount (integer) --
The number of principal entities (users, groups, and roles) that the policy is attached to.

PermissionsBoundaryUsageCount (integer) --
The number of entities (users and roles) for which the policy is used as the permissions boundary.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

IsAttachable (boolean) --
Specifies whether the policy can be attached to an IAM user, group, or role.

Description (string) --
A friendly description of the policy.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the policy was created.

UpdateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the policy was last updated.
When a policy has only one version, this field contains the date and time when the policy was created. When a policy has more than one version, this field contains the date and time when the most recent policy version was created.

PolicyVersionList (list) --
A list containing information about the versions of the policy.

(dict) --
Contains information about a version of a managed policy.
This data type is used as a response element in the  CreatePolicyVersion ,  GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations.
For more information about managed policies, refer to Managed Policies and Inline Policies in the IAM User Guide .

Document (string) --
The policy document.
The policy document is returned in the response to the  GetPolicyVersion and  GetAccountAuthorizationDetails operations. It is not returned in the response to the  CreatePolicyVersion or  ListPolicyVersions operations.
The policy document returned in this structure is URL-encoded compliant with RFC 3986 . You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the decode method of the java.net.URLDecoder utility class in the Java SDK. Other languages and SDKs provide similar functionality.

VersionId (string) --
The identifier for the policy version.
Policy version identifiers always begin with v (always lowercase). When a policy is created, the first policy version is v1 .

IsDefaultVersion (boolean) --
Specifies whether the policy version is set as the policy\'s default version.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the policy version was created.









IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.ServiceFailureException


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
                ],
                'PermissionsBoundary': {
                    'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                    'PermissionsBoundaryArn': 'string'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
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
                                'Description': 'string',
                                'MaxSessionDuration': 123,
                                'PermissionsBoundary': {
                                    'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                                    'PermissionsBoundaryArn': 'string'
                                },
                                'Tags': [
                                    {
                                        'Key': 'string',
                                        'Value': 'string'
                                    },
                                ],
                                'RoleLastUsed': {
                                    'LastUsedDate': datetime(2015, 1, 1),
                                    'Region': 'string'
                                }
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
                ],
                'PermissionsBoundary': {
                    'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                    'PermissionsBoundaryArn': 'string'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'RoleLastUsed': {
                    'LastUsedDate': datetime(2015, 1, 1),
                    'Region': 'string'
                }
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
                'PermissionsBoundaryUsageCount': 123,
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
    
    Exceptions
    Examples
    The following command displays details about the password policy for the current AWS account.
    Expected Output:
    
    :example: response = client.get_account_password_policy()
    
    
    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --Contains the response to a successful  GetAccountPasswordPolicy request.

PasswordPolicy (dict) --A structure that contains details about the account\'s password policy.

MinimumPasswordLength (integer) --Minimum length to require for IAM user passwords.

RequireSymbols (boolean) --Specifies whether to require symbols for IAM user passwords.

RequireNumbers (boolean) --Specifies whether to require numbers for IAM user passwords.

RequireUppercaseCharacters (boolean) --Specifies whether to require uppercase characters for IAM user passwords.

RequireLowercaseCharacters (boolean) --Specifies whether to require lowercase characters for IAM user passwords.

AllowUsersToChangePassword (boolean) --Specifies whether IAM users are allowed to change their own password.

ExpirePasswords (boolean) --Indicates whether passwords in the account expire. Returns true if MaxPasswordAge contains a value greater than 0. Returns false if MaxPasswordAge is 0 or not present.

MaxPasswordAge (integer) --The number of days that an IAM user password is valid.

PasswordReusePrevention (integer) --Specifies the number of previous passwords that IAM users are prevented from reusing.

HardExpiry (boolean) --Specifies whether IAM users are prevented from setting a new password after their password has expired.








Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command displays details about the password policy for the current AWS account.
response = client.get_account_password_policy(
)

print(response)


Expected Output:
{
    'PasswordPolicy': {
        'AllowUsersToChangePassword': False,
        'ExpirePasswords': False,
        'HardExpiry': False,
        'MaxPasswordAge': 90,
        'MinimumPasswordLength': 8,
        'PasswordReusePrevention': 12,
        'RequireLowercaseCharacters': False,
        'RequireNumbers': True,
        'RequireSymbols': True,
        'RequireUppercaseCharacters': False,
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    Exceptions
    Examples
    The following command returns information about the IAM entity quotas and usage in the current AWS account.
    Expected Output:
    
    :example: response = client.get_account_summary()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'SummaryMap': {
        'string': 123
    }
}


Response Structure

(dict) --Contains the response to a successful  GetAccountSummary request.

SummaryMap (dict) --A set of key\xe2\x80\x93value pairs containing information about IAM entity usage and IAM quotas.

(string) --
(integer) --









Exceptions

IAM.Client.exceptions.ServiceFailureException

Examples
The following command returns information about the IAM entity quotas and usage in the current AWS account.
response = client.get_account_summary(
)

print(response)


Expected Output:
{
    'SummaryMap': {
        'AccessKeysPerUserQuota': 2,
        'AccountAccessKeysPresent': 1,
        'AccountMFAEnabled': 0,
        'AccountSigningCertificatesPresent': 0,
        'AttachedPoliciesPerGroupQuota': 10,
        'AttachedPoliciesPerRoleQuota': 10,
        'AttachedPoliciesPerUserQuota': 10,
        'GroupPolicySizeQuota': 5120,
        'Groups': 15,
        'GroupsPerUserQuota': 10,
        'GroupsQuota': 100,
        'MFADevices': 6,
        'MFADevicesInUse': 3,
        'Policies': 8,
        'PoliciesQuota': 1000,
        'PolicySizeQuota': 5120,
        'PolicyVersionsInUse': 22,
        'PolicyVersionsInUseQuota': 10000,
        'ServerCertificates': 1,
        'ServerCertificatesQuota': 20,
        'SigningCertificatesPerUserQuota': 2,
        'UserPolicySizeQuota': 2048,
        'Users': 27,
        'UsersQuota': 5000,
        'VersionsPerPolicyQuota': 5,
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'SummaryMap': {
            'string': 123
        }
    }
    
    
    :returns: 
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def get_context_keys_for_custom_policy(PolicyInputList=None):
    """
    Gets a list of all of the context keys referenced in the input policies. The policies are supplied as a list of one or more strings. To get the context keys from policies associated with an IAM user, group, or role, use  GetContextKeysForPrincipalPolicy .
    Context keys are variables maintained by AWS and its services that provide details about the context of an API query request. Context keys can be evaluated by testing against a value specified in an IAM policy. Use GetContextKeysForCustomPolicy to understand what key names and values you must supply when you call  SimulateCustomPolicy . Note that all parameters are shown in unencoded form here for clarity but must be URL encoded to be included as a part of a real HTML request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_context_keys_for_custom_policy(
        PolicyInputList=[
            'string',
        ]
    )
    
    
    :type PolicyInputList: list
    :param PolicyInputList: [REQUIRED]\nA list of policies for which you want the list of context keys referenced in those policies. Each document is specified as a string containing the complete, valid JSON text of an IAM policy.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'ContextKeyNames': [
        'string',
    ]
}


Response Structure

(dict) --Contains the response to a successful  GetContextKeysForPrincipalPolicy or  GetContextKeysForCustomPolicy request.

ContextKeyNames (list) --The list of context keys that are referenced in the input policies.

(string) --







Exceptions

IAM.Client.exceptions.InvalidInputException


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
    Gets a list of all of the context keys referenced in all the IAM policies that are attached to the specified IAM entity. The entity can be an IAM user, group, or role. If you specify a user, then the request also includes all of the policies attached to groups that the user is a member of.
    You can optionally include a list of one or more additional policies, specified as strings. If you want to include only a list of policies by string, use  GetContextKeysForCustomPolicy instead.
    Context keys are variables maintained by AWS and its services that provide details about the context of an API query request. Context keys can be evaluated by testing against a value in an IAM policy. Use  GetContextKeysForPrincipalPolicy to understand what key names and values you must supply when you call  SimulatePrincipalPolicy .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_context_keys_for_principal_policy(
        PolicySourceArn='string',
        PolicyInputList=[
            'string',
        ]
    )
    
    
    :type PolicySourceArn: string
    :param PolicySourceArn: [REQUIRED]\nThe ARN of a user, group, or role whose policies contain the context keys that you want listed. If you specify a user, the list includes context keys that are found in all policies that are attached to the user. The list also includes all groups that the user is a member of. If you pick a group or a role, then it includes only those context keys that are found in policies attached to that entity. Note that all parameters are shown in unencoded form here for clarity, but must be URL encoded to be included as a part of a real HTML request.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :type PolicyInputList: list
    :param PolicyInputList: An optional list of additional policies for which you want the list of context keys that are referenced.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ContextKeyNames': [
        'string',
    ]
}


Response Structure

(dict) --
Contains the response to a successful  GetContextKeysForPrincipalPolicy or  GetContextKeysForCustomPolicy request.

ContextKeyNames (list) --
The list of context keys that are referenced in the input policies.

(string) --








Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException


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
    
    Exceptions
    
    :example: response = client.get_credential_report()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'Content': b'bytes',
    'ReportFormat': 'text/csv',
    'GeneratedTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --Contains the response to a successful  GetCredentialReport request.

Content (bytes) --Contains the credential report. The report is Base64-encoded.

ReportFormat (string) --The format (MIME type) of the credential report.

GeneratedTime (datetime) --The date and time when the credential report was created, in ISO 8601 date-time format .






Exceptions

IAM.Client.exceptions.CredentialReportNotPresentException
IAM.Client.exceptions.CredentialReportExpiredException
IAM.Client.exceptions.CredentialReportNotReadyException
IAM.Client.exceptions.ServiceFailureException


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
    
    Exceptions
    
    :example: response = client.get_group(
        GroupName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
            'PasswordLastUsed': datetime(2015, 1, 1),
            'PermissionsBoundary': {
                'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                'PermissionsBoundaryArn': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  GetGroup request.

Group (dict) --
A structure that contains details about the group.

Path (string) --
The path to the group. For more information about paths, see IAM Identifiers in the IAM User Guide .

GroupName (string) --
The friendly name that identifies the group.

GroupId (string) --
The stable and unique string identifying the group. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the group was created.



Users (list) --
A list of users in the group.

(dict) --
Contains information about an IAM user entity.
This data type is used as a response element in the following operations:

CreateUser
GetUser
ListUsers


Path (string) --
The path to the user. For more information about paths, see IAM Identifiers in the IAM User Guide .

UserName (string) --
The friendly name identifying the user.

UserId (string) --
The stable and unique string identifying the user. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the user was created.

PasswordLastUsed (datetime) --
The date and time, in ISO 8601 date-time format , when the user\'s password was last used to sign in to an AWS website. For a list of AWS websites that capture a user\'s last sign-in time, see the Credential Reports topic in the IAM User Guide . If a password is used more than once in a five-minute span, only the first use is returned in this field. If the field is null (no value), then it indicates that they never signed in with a password. This can be because:

The user never had a password.
A password exists but has not been used since IAM started tracking this information on October 20, 2014.

A null value does not mean that the user never had a password. Also, if the user does not currently have a password but had one in the past, then this field contains the date and time the most recent password was used.
This value is returned only in the  GetUser and  ListUsers operations.

PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the user.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are associated with the specified user. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.










IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException


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
                'PasswordLastUsed': datetime(2015, 1, 1),
                'PermissionsBoundary': {
                    'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                    'PermissionsBoundaryArn': 'string'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
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
    An IAM group can also have managed policies attached to it. To retrieve a managed policy document that is attached to a group, use  GetPolicy to determine the policy\'s default version, then use  GetPolicyVersion to retrieve the policy document.
    For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_group_policy(
        GroupName='string',
        PolicyName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group the policy is associated with.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the policy document to get.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GroupName': 'string',
    'PolicyName': 'string',
    'PolicyDocument': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  GetGroupPolicy request.

GroupName (string) --
The group the policy is associated with.

PolicyName (string) --
The name of the policy.

PolicyDocument (string) --
The policy document.
IAM stores policies in JSON format. However, resources that were created using AWS CloudFormation templates can be formatted in YAML. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'GroupName': 'string',
        'PolicyName': 'string',
        'PolicyDocument': 'string'
    }
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def get_instance_profile(InstanceProfileName=None):
    """
    Retrieves information about the specified instance profile, including the instance profile\'s path, GUID, ARN, and role. For more information about instance profiles, see About Instance Profiles in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command gets information about the instance profile named ExampleInstanceProfile.
    Expected Output:
    
    :example: response = client.get_instance_profile(
        InstanceProfileName='string'
    )
    
    
    :type InstanceProfileName: string
    :param InstanceProfileName: [REQUIRED]\nThe name of the instance profile to get information about.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :rtype: dict
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
                'AssumeRolePolicyDocument': 'string',
                'Description': 'string',
                'MaxSessionDuration': 123,
                'PermissionsBoundary': {
                    'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                    'PermissionsBoundaryArn': 'string'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'RoleLastUsed': {
                    'LastUsedDate': datetime(2015, 1, 1),
                    'Region': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --Contains the response to a successful  GetInstanceProfile request.

InstanceProfile (dict) --A structure containing details about the instance profile.

Path (string) --The path to the instance profile. For more information about paths, see IAM Identifiers in the IAM User Guide .

InstanceProfileName (string) --The name identifying the instance profile.

InstanceProfileId (string) --The stable and unique string identifying the instance profile. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --The Amazon Resource Name (ARN) specifying the instance profile. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --The date when the instance profile was created.

Roles (list) --The role associated with the instance profile.

(dict) --Contains information about an IAM role. This structure is returned as a response element in several API operations that interact with roles.

Path (string) --The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide .

RoleName (string) --The friendly name that identifies the role.

RoleId (string) --The stable and unique string identifying the role. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide guide.

CreateDate (datetime) --The date and time, in ISO 8601 date-time format , when the role was created.

AssumeRolePolicyDocument (string) --The policy that grants an entity permission to assume the role.

Description (string) --A description of the role that you provide.

MaxSessionDuration (integer) --The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI, or API to assume the role can specify the duration using the optional DurationSeconds API parameter or duration-seconds CLI parameter.

PermissionsBoundary (dict) --The ARN of the policy used to set the permissions boundary for the role.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --A list of tags that are attached to the specified role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.






RoleLastUsed (dict) --Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see Regions Where Data Is Tracked in the IAM User Guide .

LastUsedDate (datetime) --The date and time, in ISO 8601 date-time format that the role was last used.
This field is null if the role has not been used within the IAM tracking period. For more information about the tracking period, see Regions Where Data Is Tracked in the IAM User Guide .

Region (string) --The name of the AWS Region in which the role was last used.














Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command gets information about the instance profile named ExampleInstanceProfile.
response = client.get_instance_profile(
    InstanceProfileName='ExampleInstanceProfile',
)

print(response)


Expected Output:
{
    'InstanceProfile': {
        'Arn': 'arn:aws:iam::336924118301:instance-profile/ExampleInstanceProfile',
        'CreateDate': datetime(2013, 6, 12, 23, 52, 2, 2, 163, 0),
        'InstanceProfileId': 'AID2MAB8DPLSRHEXAMPLE',
        'InstanceProfileName': 'ExampleInstanceProfile',
        'Path': '/',
        'Roles': [
            {
                'Arn': 'arn:aws:iam::336924118301:role/Test-Role',
                'AssumeRolePolicyDocument': '<URL-encoded-JSON>',
                'CreateDate': datetime(2013, 1, 9, 6, 33, 26, 2, 9, 0),
                'Path': '/',
                'RoleId': 'AIDGPMS9RO4H3FEXAMPLE',
                'RoleName': 'Test-Role',
            },
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                    'Description': 'string',
                    'MaxSessionDuration': 123,
                    'PermissionsBoundary': {
                        'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                        'PermissionsBoundaryArn': 'string'
                    },
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'RoleLastUsed': {
                        'LastUsedDate': datetime(2015, 1, 1),
                        'Region': 'string'
                    }
                },
            ]
        }
    }
    
    
    """
    pass

def get_login_profile(UserName=None):
    """
    Retrieves the user name and password-creation date for the specified IAM user. If the user has not been assigned a password, the operation returns a 404 (NoSuchEntity ) error.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command gets information about the password for the IAM user named Anika.
    Expected Output:
    
    :example: response = client.get_login_profile(
        UserName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user whose login profile you want to retrieve.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :rtype: dict
ReturnsResponse Syntax{
    'LoginProfile': {
        'UserName': 'string',
        'CreateDate': datetime(2015, 1, 1),
        'PasswordResetRequired': True|False
    }
}


Response Structure

(dict) --Contains the response to a successful  GetLoginProfile request.

LoginProfile (dict) --A structure containing the user name and password create date for the user.

UserName (string) --The name of the user, which can be used for signing in to the AWS Management Console.

CreateDate (datetime) --The date when the password for the user was created.

PasswordResetRequired (boolean) --Specifies whether the user is required to set a new password on next sign-in.








Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command gets information about the password for the IAM user named Anika.
response = client.get_login_profile(
    UserName='Anika',
)

print(response)


Expected Output:
{
    'LoginProfile': {
        'CreateDate': datetime(2012, 9, 21, 23, 3, 39, 4, 265, 0),
        'UserName': 'Anika',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    Exceptions
    
    :example: response = client.get_open_id_connect_provider(
        OpenIDConnectProviderArn='string'
    )
    
    
    :type OpenIDConnectProviderArn: string
    :param OpenIDConnectProviderArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the OIDC provider resource object in IAM to get information for. You can get a list of OIDC provider resource ARNs by using the ListOpenIDConnectProviders operation.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :rtype: dict
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

(dict) --Contains the response to a successful  GetOpenIDConnectProvider request.

Url (string) --The URL that the IAM OIDC provider resource object is associated with. For more information, see  CreateOpenIDConnectProvider .

ClientIDList (list) --A list of client IDs (also known as audiences) that are associated with the specified IAM OIDC provider resource object. For more information, see  CreateOpenIDConnectProvider .

(string) --


ThumbprintList (list) --A list of certificate thumbprints that are associated with the specified IAM OIDC provider resource object. For more information, see  CreateOpenIDConnectProvider .

(string) --Contains a thumbprint for an identity provider\'s server certificate.
The identity provider\'s server certificate thumbprint is the hex-encoded SHA-1 hash value of the self-signed X.509 certificate. This thumbprint is used by the domain where the OpenID Connect provider makes its keys available. The thumbprint is always a 40-character string.



CreateDate (datetime) --The date and time when the IAM OIDC provider resource object was created in the AWS account.






Exceptions

IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException


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
    
    
    :returns: 
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def get_organizations_access_report(JobId=None, MaxItems=None, Marker=None, SortKey=None):
    """
    Retrieves the service last accessed data report for AWS Organizations that was previously generated using the ``  GenerateOrganizationsAccessReport `` operation. This operation retrieves the status of your report job and the report contents.
    Depending on the parameters that you passed when you generated the report, the data returned could include different information. For details, see  GenerateOrganizationsAccessReport .
    To call this operation, you must be signed in to the master account in your organization. SCPs must be enabled for your organization root. You must have permissions to perform this operation. For more information, see Refining Permissions Using Service Last Accessed Data in the IAM User Guide .
    For each service that principals in an account (root users, IAM users, or IAM roles) could access using SCPs, the operation returns details about the most recent access attempt. If there was no attempt, the service is listed without details about the most recent attempt to access the service. If the operation fails, it returns the reason that it failed.
    By default, the list is sorted by service namespace.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_organizations_access_report(
        JobId='string',
        MaxItems=123,
        Marker='string',
        SortKey='SERVICE_NAMESPACE_ASCENDING'|'SERVICE_NAMESPACE_DESCENDING'|'LAST_AUTHENTICATED_TIME_ASCENDING'|'LAST_AUTHENTICATED_TIME_DESCENDING'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe identifier of the request generated by the GenerateOrganizationsAccessReport operation.\n

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type SortKey: string
    :param SortKey: The key that is used to sort the results. If you choose the namespace key, the results are returned in alphabetical order. If you choose the time key, the results are sorted numerically by the date and time.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED',
    'JobCreationDate': datetime(2015, 1, 1),
    'JobCompletionDate': datetime(2015, 1, 1),
    'NumberOfServicesAccessible': 123,
    'NumberOfServicesNotAccessed': 123,
    'AccessDetails': [
        {
            'ServiceName': 'string',
            'ServiceNamespace': 'string',
            'Region': 'string',
            'EntityPath': 'string',
            'LastAuthenticatedTime': datetime(2015, 1, 1),
            'TotalAuthenticatedEntities': 123
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string',
    'ErrorDetails': {
        'Message': 'string',
        'Code': 'string'
    }
}


Response Structure

(dict) --

JobStatus (string) --
The status of the job.

JobCreationDate (datetime) --
The date and time, in ISO 8601 date-time format , when the report job was created.

JobCompletionDate (datetime) --
The date and time, in ISO 8601 date-time format , when the generated report job was completed or failed.
This field is null if the job is still in progress, as indicated by a job status value of IN_PROGRESS .

NumberOfServicesAccessible (integer) --
The number of services that the applicable SCPs allow account principals to access.

NumberOfServicesNotAccessed (integer) --
The number of services that account principals are allowed but did not attempt to access.

AccessDetails (list) --
An object that contains details about the most recent attempt to access the service.

(dict) --
An object that contains details about when a principal in the reported AWS Organizations entity last attempted to access an AWS service. A principal can be an IAM user, an IAM role, or the AWS account root user within the reported Organizations entity.
This data type is a response element in the  GetOrganizationsAccessReport operation.

ServiceName (string) --
The name of the service in which access was attempted.

ServiceNamespace (string) --
The namespace of the service in which access was attempted.
To learn the service namespace of a service, go to Actions, Resources, and Condition Keys for AWS Services in the IAM User Guide . Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, (service prefix: a4b) . For more information about service namespaces, see AWS Service Namespaces in the AWS General Reference .

Region (string) --
The Region where the last service access attempt occurred.
This field is null if no principals in the reported Organizations entity attempted to access the service within the reporting period .

EntityPath (string) --
The path of the Organizations entity (root, organizational unit, or account) from which an authenticated principal last attempted to access the service. AWS does not report unauthenticated requests.
This field is null if no principals (IAM users, IAM roles, or root users) in the reported Organizations entity attempted to access the service within the reporting period .

LastAuthenticatedTime (datetime) --
The date and time, in ISO 8601 date-time format , when an authenticated principal most recently attempted to access the service. AWS does not report unauthenticated requests.
This field is null if no principals in the reported Organizations entity attempted to access the service within the reporting period .

TotalAuthenticatedEntities (integer) --
The number of accounts with authenticated principals (root users, IAM users, and IAM roles) that attempted to access the service in the reporting period.





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.

ErrorDetails (dict) --
Contains information about the reason that the operation failed.
This data type is used as a response element in the  GetOrganizationsAccessReport ,  GetServiceLastAccessedDetails , and  GetServiceLastAccessedDetailsWithEntities operations.

Message (string) --
Detailed information about the reason that the operation failed.

Code (string) --
The error code associated with the operation failure.









Exceptions

IAM.Client.exceptions.NoSuchEntityException


    :return: {
        'JobStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED',
        'JobCreationDate': datetime(2015, 1, 1),
        'JobCompletionDate': datetime(2015, 1, 1),
        'NumberOfServicesAccessible': 123,
        'NumberOfServicesNotAccessed': 123,
        'AccessDetails': [
            {
                'ServiceName': 'string',
                'ServiceNamespace': 'string',
                'Region': 'string',
                'EntityPath': 'string',
                'LastAuthenticatedTime': datetime(2015, 1, 1),
                'TotalAuthenticatedEntities': 123
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string',
        'ErrorDetails': {
            'Message': 'string',
            'Code': 'string'
        }
    }
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    
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

def get_policy(PolicyArn=None):
    """
    Retrieves information about the specified managed policy, including the policy\'s default version and the total number of IAM users, groups, and roles to which the policy is attached. To retrieve the list of the specific users, groups, and roles that the policy is attached to, use the  ListEntitiesForPolicy API. This API returns metadata about the policy. To retrieve the actual policy document for a specific version of the policy, use  GetPolicyVersion .
    This API retrieves information about managed policies. To retrieve information about an inline policy that is embedded with an IAM user, group, or role, use the  GetUserPolicy ,  GetGroupPolicy , or  GetRolePolicy API.
    For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_policy(
        PolicyArn='string'
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the managed policy that you want information about.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :rtype: dict
ReturnsResponse Syntax{
    'Policy': {
        'PolicyName': 'string',
        'PolicyId': 'string',
        'Arn': 'string',
        'Path': 'string',
        'DefaultVersionId': 'string',
        'AttachmentCount': 123,
        'PermissionsBoundaryUsageCount': 123,
        'IsAttachable': True|False,
        'Description': 'string',
        'CreateDate': datetime(2015, 1, 1),
        'UpdateDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --Contains the response to a successful  GetPolicy request.

Policy (dict) --A structure containing details about the policy.

PolicyName (string) --The friendly name (not ARN) identifying the policy.

PolicyId (string) --The stable and unique string identifying the policy.
For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .

Path (string) --The path to the policy.
For more information about paths, see IAM Identifiers in the IAM User Guide .

DefaultVersionId (string) --The identifier for the version of the policy that is set as the default version.

AttachmentCount (integer) --The number of entities (users, groups, and roles) that the policy is attached to.

PermissionsBoundaryUsageCount (integer) --The number of entities (users and roles) for which the policy is used to set the permissions boundary.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

IsAttachable (boolean) --Specifies whether the policy can be attached to an IAM user, group, or role.

Description (string) --A friendly description of the policy.
This element is included in the response to the  GetPolicy operation. It is not included in the response to the  ListPolicies operation.

CreateDate (datetime) --The date and time, in ISO 8601 date-time format , when the policy was created.

UpdateDate (datetime) --The date and time, in ISO 8601 date-time format , when the policy was last updated.
When a policy has only one version, this field contains the date and time when the policy was created. When a policy has more than one version, this field contains the date and time when the most recent policy version was created.








Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'Policy': {
            'PolicyName': 'string',
            'PolicyId': 'string',
            'Arn': 'string',
            'Path': 'string',
            'DefaultVersionId': 'string',
            'AttachmentCount': 123,
            'PermissionsBoundaryUsageCount': 123,
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
    
    Exceptions
    
    :example: response = client.get_policy_version(
        PolicyArn='string',
        VersionId='string'
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the managed policy that you want information about.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :type VersionId: string
    :param VersionId: [REQUIRED]\nIdentifies the policy version to retrieve.\nThis parameter allows (through its regex pattern ) a string of characters that consists of the lowercase letter \'v\' followed by one or two digits, and optionally followed by a period \'.\' and a string of letters and digits.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PolicyVersion': {
        'Document': 'string',
        'VersionId': 'string',
        'IsDefaultVersion': True|False,
        'CreateDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Contains the response to a successful  GetPolicyVersion request.

PolicyVersion (dict) --
A structure containing details about the policy version.

Document (string) --
The policy document.
The policy document is returned in the response to the  GetPolicyVersion and  GetAccountAuthorizationDetails operations. It is not returned in the response to the  CreatePolicyVersion or  ListPolicyVersions operations.
The policy document returned in this structure is URL-encoded compliant with RFC 3986 . You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the decode method of the java.net.URLDecoder utility class in the Java SDK. Other languages and SDKs provide similar functionality.

VersionId (string) --
The identifier for the policy version.
Policy version identifiers always begin with v (always lowercase). When a policy is created, the first policy version is v1 .

IsDefaultVersion (boolean) --
Specifies whether the policy version is set as the policy\'s default version.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the policy version was created.









Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'PolicyVersion': {
            'Document': 'string',
            'VersionId': 'string',
            'IsDefaultVersion': True|False,
            'CreateDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def get_role(RoleName=None):
    """
    Retrieves information about the specified role, including the role\'s path, GUID, ARN, and the role\'s trust policy that grants permission to assume the role. For more information about roles, see Working with Roles .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command gets information about the role named Test-Role.
    Expected Output:
    
    :example: response = client.get_role(
        RoleName='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the IAM role to get information about.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :rtype: dict
ReturnsResponse Syntax{
    'Role': {
        'Path': 'string',
        'RoleName': 'string',
        'RoleId': 'string',
        'Arn': 'string',
        'CreateDate': datetime(2015, 1, 1),
        'AssumeRolePolicyDocument': 'string',
        'Description': 'string',
        'MaxSessionDuration': 123,
        'PermissionsBoundary': {
            'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
            'PermissionsBoundaryArn': 'string'
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'RoleLastUsed': {
            'LastUsedDate': datetime(2015, 1, 1),
            'Region': 'string'
        }
    }
}


Response Structure

(dict) --Contains the response to a successful  GetRole request.

Role (dict) --A structure containing details about the IAM role.

Path (string) --The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide .

RoleName (string) --The friendly name that identifies the role.

RoleId (string) --The stable and unique string identifying the role. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide guide.

CreateDate (datetime) --The date and time, in ISO 8601 date-time format , when the role was created.

AssumeRolePolicyDocument (string) --The policy that grants an entity permission to assume the role.

Description (string) --A description of the role that you provide.

MaxSessionDuration (integer) --The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI, or API to assume the role can specify the duration using the optional DurationSeconds API parameter or duration-seconds CLI parameter.

PermissionsBoundary (dict) --The ARN of the policy used to set the permissions boundary for the role.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --A list of tags that are attached to the specified role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.






RoleLastUsed (dict) --Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see Regions Where Data Is Tracked in the IAM User Guide .

LastUsedDate (datetime) --The date and time, in ISO 8601 date-time format that the role was last used.
This field is null if the role has not been used within the IAM tracking period. For more information about the tracking period, see Regions Where Data Is Tracked in the IAM User Guide .

Region (string) --The name of the AWS Region in which the role was last used.










Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command gets information about the role named Test-Role.
response = client.get_role(
    RoleName='Test-Role',
)

print(response)


Expected Output:
{
    'Role': {
        'Arn': 'arn:aws:iam::123456789012:role/Test-Role',
        'AssumeRolePolicyDocument': '<URL-encoded-JSON>',
        'CreateDate': datetime(2013, 4, 18, 5, 1, 58, 3, 108, 0),
        'Path': '/',
        'RoleId': 'AIDIODR4TAW7CSEXAMPLE',
        'RoleName': 'Test-Role',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Role': {
            'Path': 'string',
            'RoleName': 'string',
            'RoleId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'AssumeRolePolicyDocument': 'string',
            'Description': 'string',
            'MaxSessionDuration': 123,
            'PermissionsBoundary': {
                'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                'PermissionsBoundaryArn': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'RoleLastUsed': {
                'LastUsedDate': datetime(2015, 1, 1),
                'Region': 'string'
            }
        }
    }
    
    
    """
    pass

def get_role_policy(RoleName=None, PolicyName=None):
    """
    Retrieves the specified inline policy document that is embedded with the specified IAM role.
    An IAM role can also have managed policies attached to it. To retrieve a managed policy document that is attached to a role, use  GetPolicy to determine the policy\'s default version, then use  GetPolicyVersion to retrieve the policy document.
    For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    For more information about roles, see Using Roles to Delegate Permissions and Federate Identities .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_role_policy(
        RoleName='string',
        PolicyName='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the role associated with the policy.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the policy document to get.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RoleName': 'string',
    'PolicyName': 'string',
    'PolicyDocument': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  GetRolePolicy request.

RoleName (string) --
The role the policy is associated with.

PolicyName (string) --
The name of the policy.

PolicyDocument (string) --
The policy document.
IAM stores policies in JSON format. However, resources that were created using AWS CloudFormation templates can be formatted in YAML. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'RoleName': 'string',
        'PolicyName': 'string',
        'PolicyDocument': 'string'
    }
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def get_saml_provider(SAMLProviderArn=None):
    """
    Returns the SAML provider metadocument that was uploaded when the IAM SAML provider resource object was created or updated.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_saml_provider(
        SAMLProviderArn='string'
    )
    
    
    :type SAMLProviderArn: string
    :param SAMLProviderArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the SAML provider resource object in IAM to get information about.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :rtype: dict
ReturnsResponse Syntax{
    'SAMLMetadataDocument': 'string',
    'CreateDate': datetime(2015, 1, 1),
    'ValidUntil': datetime(2015, 1, 1)
}


Response Structure

(dict) --Contains the response to a successful  GetSAMLProvider request.

SAMLMetadataDocument (string) --The XML metadata document that includes information about an identity provider.

CreateDate (datetime) --The date and time when the SAML provider was created.

ValidUntil (datetime) --The expiration date and time for the SAML provider.






Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.ServiceFailureException


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
    For more information about working with server certificates, see Working with Server Certificates in the IAM User Guide . This topic includes a list of AWS services that can use the server certificates that you manage with IAM.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_server_certificate(
        ServerCertificateName='string'
    )
    
    
    :type ServerCertificateName: string
    :param ServerCertificateName: [REQUIRED]\nThe name of the server certificate you want to retrieve information about.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :rtype: dict
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

(dict) --Contains the response to a successful  GetServerCertificate request.

ServerCertificate (dict) --A structure containing details about the server certificate.

ServerCertificateMetadata (dict) --The meta information of the server certificate, such as its name, path, ID, and ARN.

Path (string) --The path to the server certificate. For more information about paths, see IAM Identifiers in the IAM User Guide .

ServerCertificateName (string) --The name that identifies the server certificate.

ServerCertificateId (string) --The stable and unique string identifying the server certificate. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --The Amazon Resource Name (ARN) specifying the server certificate. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .

UploadDate (datetime) --The date when the server certificate was uploaded.

Expiration (datetime) --The date on which the certificate is set to expire.



CertificateBody (string) --The contents of the public key certificate.

CertificateChain (string) --The contents of the public key certificate chain.








Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException


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

def get_service_last_accessed_details(JobId=None, MaxItems=None, Marker=None):
    """
    Retrieves a service last accessed report that was created using the GenerateServiceLastAccessedDetails operation. You can use the JobId parameter in GetServiceLastAccessedDetails to retrieve the status of your report job. When the report is complete, you can retrieve the generated report. The report includes a list of AWS services that the resource (user, group, role, or managed policy) can access.
    For each service that the resource could access using permissions policies, the operation returns details about the most recent access attempt. If there was no attempt, the service is listed without details about the most recent attempt to access the service. If the operation fails, the GetServiceLastAccessedDetails operation returns the reason that it failed.
    The GetServiceLastAccessedDetails operation returns a list of services. This list includes the number of entities that have attempted to access the service and the date and time of the last attempt. It also returns the ARN of the following entity, depending on the resource ARN that you used to generate the report:
    By default, the list is sorted by service namespace.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_service_last_accessed_details(
        JobId='string',
        MaxItems=123,
        Marker='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe ID of the request generated by the GenerateServiceLastAccessedDetails operation. The JobId returned by GenerateServiceLastAccessedDetail must be used by the same role within a session, or by the same user when used to call GetServiceLastAccessedDetail .\n

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED',
    'JobCreationDate': datetime(2015, 1, 1),
    'ServicesLastAccessed': [
        {
            'ServiceName': 'string',
            'LastAuthenticated': datetime(2015, 1, 1),
            'ServiceNamespace': 'string',
            'LastAuthenticatedEntity': 'string',
            'TotalAuthenticatedEntities': 123
        },
    ],
    'JobCompletionDate': datetime(2015, 1, 1),
    'IsTruncated': True|False,
    'Marker': 'string',
    'Error': {
        'Message': 'string',
        'Code': 'string'
    }
}


Response Structure

(dict) --

JobStatus (string) --
The status of the job.

JobCreationDate (datetime) --
The date and time, in ISO 8601 date-time format , when the report job was created.

ServicesLastAccessed (list) --
A ServiceLastAccessed object that contains details about the most recent attempt to access the service.

(dict) --
Contains details about the most recent attempt to access the service.
This data type is used as a response element in the  GetServiceLastAccessedDetails operation.

ServiceName (string) --
The name of the service in which access was attempted.

LastAuthenticated (datetime) --
The date and time, in ISO 8601 date-time format , when an authenticated entity most recently attempted to access the service. AWS does not report unauthenticated requests.
This field is null if no IAM entities attempted to access the service within the reporting period .

ServiceNamespace (string) --
The namespace of the service in which access was attempted.
To learn the service namespace of a service, go to Actions, Resources, and Condition Keys for AWS Services in the IAM User Guide . Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, (service prefix: a4b) . For more information about service namespaces, see AWS Service Namespaces in the AWS General Reference .

LastAuthenticatedEntity (string) --
The ARN of the authenticated entity (user or role) that last attempted to access the service. AWS does not report unauthenticated requests.
This field is null if no IAM entities attempted to access the service within the reporting period .

TotalAuthenticatedEntities (integer) --
The total number of authenticated principals (root user, IAM users, or IAM roles) that have attempted to access the service.
This field is null if no principals attempted to access the service within the reporting period .





JobCompletionDate (datetime) --
The date and time, in ISO 8601 date-time format , when the generated report job was completed or failed.
This field is null if the job is still in progress, as indicated by a job status value of IN_PROGRESS .

IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.

Error (dict) --
An object that contains details about the reason the operation failed.

Message (string) --
Detailed information about the reason that the operation failed.

Code (string) --
The error code associated with the operation failure.









Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException


    :return: {
        'JobStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED',
        'JobCreationDate': datetime(2015, 1, 1),
        'ServicesLastAccessed': [
            {
                'ServiceName': 'string',
                'LastAuthenticated': datetime(2015, 1, 1),
                'ServiceNamespace': 'string',
                'LastAuthenticatedEntity': 'string',
                'TotalAuthenticatedEntities': 123
            },
        ],
        'JobCompletionDate': datetime(2015, 1, 1),
        'IsTruncated': True|False,
        'Marker': 'string',
        'Error': {
            'Message': 'string',
            'Code': 'string'
        }
    }
    
    
    :returns: 
    JobId (string) -- [REQUIRED]
    The ID of the request generated by the  GenerateServiceLastAccessedDetails operation. The JobId returned by GenerateServiceLastAccessedDetail must be used by the same role within a session, or by the same user when used to call GetServiceLastAccessedDetail .
    
    MaxItems (integer) -- Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
    If you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.
    
    Marker (string) -- Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    
    """
    pass

def get_service_last_accessed_details_with_entities(JobId=None, ServiceNamespace=None, MaxItems=None, Marker=None):
    """
    After you generate a group or policy report using the GenerateServiceLastAccessedDetails operation, you can use the JobId parameter in GetServiceLastAccessedDetailsWithEntities . This operation retrieves the status of your report job and a list of entities that could have used group or policy permissions to access the specified service.
    You can also use this operation for user or role reports to retrieve details about those entities.
    If the operation fails, the GetServiceLastAccessedDetailsWithEntities operation returns the reason that it failed.
    By default, the list of associated entities is sorted by date, with the most recent access listed first.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_service_last_accessed_details_with_entities(
        JobId='string',
        ServiceNamespace='string',
        MaxItems=123,
        Marker='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe ID of the request generated by the GenerateServiceLastAccessedDetails operation.\n

    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]\nThe service namespace for an AWS service. Provide the service namespace to learn when the IAM entity last attempted to access the specified service.\nTo learn the service namespace for a service, go to Actions, Resources, and Condition Keys for AWS Services in the IAM User Guide . Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, (service prefix: a4b) . For more information about service namespaces, see AWS Service Namespaces in the AWS General Reference .\n

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED',
    'JobCreationDate': datetime(2015, 1, 1),
    'JobCompletionDate': datetime(2015, 1, 1),
    'EntityDetailsList': [
        {
            'EntityInfo': {
                'Arn': 'string',
                'Name': 'string',
                'Type': 'USER'|'ROLE'|'GROUP',
                'Id': 'string',
                'Path': 'string'
            },
            'LastAuthenticated': datetime(2015, 1, 1)
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string',
    'Error': {
        'Message': 'string',
        'Code': 'string'
    }
}


Response Structure

(dict) --

JobStatus (string) --
The status of the job.

JobCreationDate (datetime) --
The date and time, in ISO 8601 date-time format , when the report job was created.

JobCompletionDate (datetime) --
The date and time, in ISO 8601 date-time format , when the generated report job was completed or failed.
This field is null if the job is still in progress, as indicated by a job status value of IN_PROGRESS .

EntityDetailsList (list) --
An EntityDetailsList object that contains details about when an IAM entity (user or role) used group or policy permissions in an attempt to access the specified AWS service.

(dict) --
An object that contains details about when the IAM entities (users or roles) were last used in an attempt to access the specified AWS service.
This data type is a response element in the  GetServiceLastAccessedDetailsWithEntities operation.

EntityInfo (dict) --
The EntityInfo object that contains details about the entity (user or role).

Arn (string) --
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .

Name (string) --
The name of the entity (user or role).

Type (string) --
The type of entity (user or role).

Id (string) --
The identifier of the entity (user or role).

Path (string) --
The path to the entity (user or role). For more information about paths, see IAM Identifiers in the IAM User Guide .



LastAuthenticated (datetime) --
The date and time, in ISO 8601 date-time format , when the authenticated entity last attempted to access AWS. AWS does not report unauthenticated requests.
This field is null if no IAM entities attempted to access the service within the reporting period .





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.

Error (dict) --
An object that contains details about the reason the operation failed.

Message (string) --
Detailed information about the reason that the operation failed.

Code (string) --
The error code associated with the operation failure.









Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException


    :return: {
        'JobStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED',
        'JobCreationDate': datetime(2015, 1, 1),
        'JobCompletionDate': datetime(2015, 1, 1),
        'EntityDetailsList': [
            {
                'EntityInfo': {
                    'Arn': 'string',
                    'Name': 'string',
                    'Type': 'USER'|'ROLE'|'GROUP',
                    'Id': 'string',
                    'Path': 'string'
                },
                'LastAuthenticated': datetime(2015, 1, 1)
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string',
        'Error': {
            'Message': 'string',
            'Code': 'string'
        }
    }
    
    
    :returns: 
    JobId (string) -- [REQUIRED]
    The ID of the request generated by the GenerateServiceLastAccessedDetails operation.
    
    ServiceNamespace (string) -- [REQUIRED]
    The service namespace for an AWS service. Provide the service namespace to learn when the IAM entity last attempted to access the specified service.
    To learn the service namespace for a service, go to Actions, Resources, and Condition Keys for AWS Services in the IAM User Guide . Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, (service prefix: a4b) . For more information about service namespaces, see AWS Service Namespaces in the AWS General Reference .
    
    MaxItems (integer) -- Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .
    If you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.
    
    Marker (string) -- Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    
    """
    pass

def get_service_linked_role_deletion_status(DeletionTaskId=None):
    """
    Retrieves the status of your service-linked role deletion. After you use the  DeleteServiceLinkedRole API operation to submit a service-linked role for deletion, you can use the DeletionTaskId parameter in GetServiceLinkedRoleDeletionStatus to check the status of the deletion. If the deletion fails, this operation returns the reason that it failed, if that information is returned by the service.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_service_linked_role_deletion_status(
        DeletionTaskId='string'
    )
    
    
    :type DeletionTaskId: string
    :param DeletionTaskId: [REQUIRED]\nThe deletion task identifier. This identifier is returned by the DeleteServiceLinkedRole operation in the format task/aws-service-role/<service-principal-name>/<role-name>/<task-uuid> .\n

    :rtype: dict
ReturnsResponse Syntax{
    'Status': 'SUCCEEDED'|'IN_PROGRESS'|'FAILED'|'NOT_STARTED',
    'Reason': {
        'Reason': 'string',
        'RoleUsageList': [
            {
                'Region': 'string',
                'Resources': [
                    'string',
                ]
            },
        ]
    }
}


Response Structure

(dict) --
Status (string) --The status of the deletion.

Reason (dict) --An object that contains details about the reason the deletion failed.

Reason (string) --A short description of the reason that the service-linked role deletion failed.

RoleUsageList (list) --A list of objects that contains details about the service-linked role deletion failure, if that information is returned by the service. If the service-linked role has active sessions or if any resources that were used by the role have not been deleted from the linked service, the role can\'t be deleted. This parameter includes a list of the resources that are associated with the role and the Region in which the resources are being used.

(dict) --An object that contains details about how a service-linked role is used, if that information is returned by the service.
This data type is used as a response element in the  GetServiceLinkedRoleDeletionStatus operation.

Region (string) --The name of the Region where the service-linked role is being used.

Resources (list) --The name of the resource that is using the service-linked role.

(string) --The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .














Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'Status': 'SUCCEEDED'|'IN_PROGRESS'|'FAILED'|'NOT_STARTED',
        'Reason': {
            'Reason': 'string',
            'RoleUsageList': [
                {
                    'Region': 'string',
                    'Resources': [
                        'string',
                    ]
                },
            ]
        }
    }
    
    
    """
    pass

def get_ssh_public_key(UserName=None, SSHPublicKeyId=None, Encoding=None):
    """
    Retrieves the specified SSH public key, including metadata about the key.
    The SSH public key retrieved by this operation is used only for authenticating the associated IAM user to an AWS CodeCommit repository. For more information about using SSH keys to authenticate to an AWS CodeCommit repository, see Set up AWS CodeCommit for SSH Connections in the AWS CodeCommit User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_ssh_public_key(
        UserName='string',
        SSHPublicKeyId='string',
        Encoding='SSH'|'PEM'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the IAM user associated with the SSH public key.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type SSHPublicKeyId: string
    :param SSHPublicKeyId: [REQUIRED]\nThe unique identifier for the SSH public key.\nThis parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.\n

    :type Encoding: string
    :param Encoding: [REQUIRED]\nSpecifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use SSH . To retrieve the public key in PEM format, use PEM .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SSHPublicKey': {
        'UserName': 'string',
        'SSHPublicKeyId': 'string',
        'Fingerprint': 'string',
        'SSHPublicKeyBody': 'string',
        'Status': 'Active'|'Inactive',
        'UploadDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Contains the response to a successful  GetSSHPublicKey request.

SSHPublicKey (dict) --
A structure containing details about the SSH public key.

UserName (string) --
The name of the IAM user associated with the SSH public key.

SSHPublicKeyId (string) --
The unique identifier for the SSH public key.

Fingerprint (string) --
The MD5 message digest of the SSH public key.

SSHPublicKeyBody (string) --
The SSH public key.

Status (string) --
The status of the SSH public key. Active means that the key can be used for authentication with an AWS CodeCommit repository. Inactive means that the key cannot be used.

UploadDate (datetime) --
The date and time, in ISO 8601 date-time format , when the SSH public key was uploaded.









Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.UnrecognizedPublicKeyEncodingException


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
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.UnrecognizedPublicKeyEncodingException
    
    """
    pass

def get_user(UserName=None):
    """
    Retrieves information about the specified IAM user, including the user\'s creation date, path, unique ID, and ARN.
    If you do not specify a user name, IAM determines the user name implicitly based on the AWS access key ID used to sign the request to this API.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command gets information about the IAM user named Bob.
    Expected Output:
    
    :example: response = client.get_user(
        UserName='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the user to get information about.\nThis parameter is optional. If it is not included, it defaults to the user making the request. This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :rtype: dict
ReturnsResponse Syntax{
    'User': {
        'Path': 'string',
        'UserName': 'string',
        'UserId': 'string',
        'Arn': 'string',
        'CreateDate': datetime(2015, 1, 1),
        'PasswordLastUsed': datetime(2015, 1, 1),
        'PermissionsBoundary': {
            'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
            'PermissionsBoundaryArn': 'string'
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --Contains the response to a successful  GetUser request.

User (dict) --A structure containing details about the IAM user.

Warning
Due to a service issue, password last used data does not include password use from May 3, 2018 22:50 PDT to May 23, 2018 14:08 PDT. This affects last sign-in dates shown in the IAM console and password last used dates in the IAM credential report , and returned by this GetUser API. If users signed in during the affected time, the password last used date that is returned is the date the user last signed in before May 3, 2018. For users that signed in after May 23, 2018 14:08 PDT, the returned password last used date is accurate.
You can use password last used information to identify unused credentials for deletion. For example, you might delete users who did not sign in to AWS in the last 90 days. In cases like this, we recommend that you adjust your evaluation window to include dates after May 23, 2018. Alternatively, if your users use access keys to access AWS programmatically you can refer to access key last used information because it is accurate for all dates.


Path (string) --The path to the user. For more information about paths, see IAM Identifiers in the IAM User Guide .

UserName (string) --The friendly name identifying the user.

UserId (string) --The stable and unique string identifying the user. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --The date and time, in ISO 8601 date-time format , when the user was created.

PasswordLastUsed (datetime) --The date and time, in ISO 8601 date-time format , when the user\'s password was last used to sign in to an AWS website. For a list of AWS websites that capture a user\'s last sign-in time, see the Credential Reports topic in the IAM User Guide . If a password is used more than once in a five-minute span, only the first use is returned in this field. If the field is null (no value), then it indicates that they never signed in with a password. This can be because:

The user never had a password.
A password exists but has not been used since IAM started tracking this information on October 20, 2014.

A null value does not mean that the user never had a password. Also, if the user does not currently have a password but had one in the past, then this field contains the date and time the most recent password was used.
This value is returned only in the  GetUser and  ListUsers operations.

PermissionsBoundary (dict) --The ARN of the policy used to set the permissions boundary for the user.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --A list of tags that are associated with the specified user. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.













Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command gets information about the IAM user named Bob.
response = client.get_user(
    UserName='Bob',
)

print(response)


Expected Output:
{
    'User': {
        'Arn': 'arn:aws:iam::123456789012:user/Bob',
        'CreateDate': datetime(2012, 9, 21, 23, 3, 13, 4, 265, 0),
        'Path': '/',
        'UserId': 'AKIAIOSFODNN7EXAMPLE',
        'UserName': 'Bob',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'User': {
            'Path': 'string',
            'UserName': 'string',
            'UserId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'PasswordLastUsed': datetime(2015, 1, 1),
            'PermissionsBoundary': {
                'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                'PermissionsBoundaryArn': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def get_user_policy(UserName=None, PolicyName=None):
    """
    Retrieves the specified inline policy document that is embedded in the specified IAM user.
    An IAM user can also have managed policies attached to it. To retrieve a managed policy document that is attached to a user, use  GetPolicy to determine the policy\'s default version. Then use  GetPolicyVersion to retrieve the policy document.
    For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_user_policy(
        UserName='string',
        PolicyName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user who the policy is associated with.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the policy document to get.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UserName': 'string',
    'PolicyName': 'string',
    'PolicyDocument': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  GetUserPolicy request.

UserName (string) --
The user the policy is associated with.

PolicyName (string) --
The name of the policy.

PolicyDocument (string) --
The policy document.
IAM stores policies in JSON format. However, resources that were created using AWS CloudFormation templates can be formatted in YAML. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'UserName': 'string',
        'PolicyName': 'string',
        'PolicyDocument': 'string'
    }
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
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

def list_access_keys(UserName=None, Marker=None, MaxItems=None):
    """
    Returns information about the access key IDs associated with the specified IAM user. If there is none, the operation returns an empty list.
    Although each user is limited to a small number of keys, you can still paginate the results using the MaxItems and Marker parameters.
    If the UserName field is not specified, the user name is determined implicitly based on the AWS access key ID used to sign the request. This operation works for access keys under the AWS account. Consequently, you can use this operation to manage AWS account root user credentials even if the AWS account has no associated users.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command lists the access keys IDs for the IAM user named Alice.
    Expected Output:
    
    :example: response = client.list_access_keys(
        UserName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: The name of the user.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the response to a successful  ListAccessKeys request.

AccessKeyMetadata (list) --
A list of objects containing metadata about the access keys.

(dict) --
Contains information about an AWS access key, without its secret key.
This data type is used as a response element in the  ListAccessKeys operation.

UserName (string) --
The name of the IAM user that the key is associated with.

AccessKeyId (string) --
The ID for this access key.

Status (string) --
The status of the access key. Active means that the key is valid for API calls; Inactive means it is not.

CreateDate (datetime) --
The date when the access key was created.





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command lists the access keys IDs for the IAM user named Alice.
response = client.list_access_keys(
    UserName='Alice',
)

print(response)


Expected Output:
{
    'AccessKeyMetadata': [
        {
            'AccessKeyId': 'AKIA111111111EXAMPLE',
            'CreateDate': datetime(2016, 12, 1, 22, 19, 58, 3, 336, 0),
            'Status': 'Active',
            'UserName': 'Alice',
        },
        {
            'AccessKeyId': 'AKIA222222222EXAMPLE',
            'CreateDate': datetime(2016, 12, 1, 22, 20, 1, 3, 336, 0),
            'Status': 'Active',
            'UserName': 'Alice',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_account_aliases(Marker=None, MaxItems=None):
    """
    Lists the account alias associated with the AWS account (Note: you can have only one). For information about using an AWS account alias, see Using an Alias for Your AWS Account ID in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
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
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AccountAliases': [
        'string',
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  ListAccountAliases request.

AccountAliases (list) --
A list of aliases associated with the account. AWS supports only one alias per account.

(string) --


IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.ServiceFailureException

Examples
The following command lists the aliases for the current account.
response = client.list_account_aliases(
)

print(response)


Expected Output:
{
    'AccountAliases': [
        'exmaple-corporation',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    You can paginate the results using the MaxItems and Marker parameters. You can use the PathPrefix parameter to limit the list of policies to only those matching the specified path prefix. If there are no policies attached to the specified group (or none that match the specified path prefix), the operation returns an empty list.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_attached_group_policies(
        GroupName='string',
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name (friendly name, not ARN) of the group to list attached policies for.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies.\nThis parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AttachedPolicies': [
        {
            'PolicyName': 'string',
            'PolicyArn': 'string'
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  ListAttachedGroupPolicies request.

AttachedPolicies (list) --
A list of the attached policies.

(dict) --
Contains information about an attached policy.
An attached policy is a managed policy that has been attached to a user, group, or role. This data type is used as a response element in the  ListAttachedGroupPolicies ,  ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails operations.
For more information about managed policies, refer to Managed Policies and Inline Policies in the IAM User Guide .

PolicyName (string) --
The friendly name of the attached policy.

PolicyArn (string) --
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.ServiceFailureException


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
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_attached_role_policies(RoleName=None, PathPrefix=None, Marker=None, MaxItems=None):
    """
    Lists all managed policies that are attached to the specified IAM role.
    An IAM role can also have inline policies embedded with it. To list the inline policies for a role, use the  ListRolePolicies API. For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    You can paginate the results using the MaxItems and Marker parameters. You can use the PathPrefix parameter to limit the list of policies to only those matching the specified path prefix. If there are no policies attached to the specified role (or none that match the specified path prefix), the operation returns an empty list.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_attached_role_policies(
        RoleName='string',
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name (friendly name, not ARN) of the role to list attached policies for.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies.\nThis parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AttachedPolicies': [
        {
            'PolicyName': 'string',
            'PolicyArn': 'string'
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  ListAttachedRolePolicies request.

AttachedPolicies (list) --
A list of the attached policies.

(dict) --
Contains information about an attached policy.
An attached policy is a managed policy that has been attached to a user, group, or role. This data type is used as a response element in the  ListAttachedGroupPolicies ,  ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails operations.
For more information about managed policies, refer to Managed Policies and Inline Policies in the IAM User Guide .

PolicyName (string) --
The friendly name of the attached policy.

PolicyArn (string) --
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.ServiceFailureException


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
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_attached_user_policies(UserName=None, PathPrefix=None, Marker=None, MaxItems=None):
    """
    Lists all managed policies that are attached to the specified IAM user.
    An IAM user can also have inline policies embedded with it. To list the inline policies for a user, use the  ListUserPolicies API. For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    You can paginate the results using the MaxItems and Marker parameters. You can use the PathPrefix parameter to limit the list of policies to only those matching the specified path prefix. If there are no policies attached to the specified group (or none that match the specified path prefix), the operation returns an empty list.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_attached_user_policies(
        UserName='string',
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name (friendly name, not ARN) of the user to list attached policies for.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies.\nThis parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AttachedPolicies': [
        {
            'PolicyName': 'string',
            'PolicyArn': 'string'
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  ListAttachedUserPolicies request.

AttachedPolicies (list) --
A list of the attached policies.

(dict) --
Contains information about an attached policy.
An attached policy is a managed policy that has been attached to a user, group, or role. This data type is used as a response element in the  ListAttachedGroupPolicies ,  ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails operations.
For more information about managed policies, refer to Managed Policies and Inline Policies in the IAM User Guide .

PolicyName (string) --
The friendly name of the attached policy.

PolicyArn (string) --
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.ServiceFailureException


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
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_entities_for_policy(PolicyArn=None, EntityFilter=None, PathPrefix=None, PolicyUsageFilter=None, Marker=None, MaxItems=None):
    """
    Lists all IAM users, groups, and roles that the specified managed policy is attached to.
    You can use the optional EntityFilter parameter to limit the results to a particular type of entity (users, groups, or roles). For example, to list only the roles that are attached to the specified policy, set EntityFilter to Role .
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_entities_for_policy(
        PolicyArn='string',
        EntityFilter='User'|'Role'|'Group'|'LocalManagedPolicy'|'AWSManagedPolicy',
        PathPrefix='string',
        PolicyUsageFilter='PermissionsPolicy'|'PermissionsBoundary',
        Marker='string',
        MaxItems=123
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM policy for which you want the versions.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :type EntityFilter: string
    :param EntityFilter: The entity type to use for filtering the results.\nFor example, when EntityFilter is Role , only the roles that are attached to the specified policy are returned. This parameter is optional. If it is not included, all attached entities (users, groups, and roles) are returned. The argument for this parameter must be one of the valid values listed below.\n

    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all entities.\nThis parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type PolicyUsageFilter: string
    :param PolicyUsageFilter: The policy usage method to use for filtering the results.\nTo list only permissions policies, set PolicyUsageFilter to PermissionsPolicy . To list only the policies used to set permissions boundaries, set the value to PermissionsBoundary .\nThis parameter is optional. If it is not included, all policies are returned.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the response to a successful  ListEntitiesForPolicy request.

PolicyGroups (list) --
A list of IAM groups that the policy is attached to.

(dict) --
Contains information about a group that a managed policy is attached to.
This data type is used as a response element in the  ListEntitiesForPolicy operation.
For more information about managed policies, refer to Managed Policies and Inline Policies in the IAM User Guide .

GroupName (string) --
The name (friendly name, not ARN) identifying the group.

GroupId (string) --
The stable and unique string identifying the group. For more information about IDs, see IAM Identifiers in the IAM User Guide .





PolicyUsers (list) --
A list of IAM users that the policy is attached to.

(dict) --
Contains information about a user that a managed policy is attached to.
This data type is used as a response element in the  ListEntitiesForPolicy operation.
For more information about managed policies, refer to Managed Policies and Inline Policies in the IAM User Guide .

UserName (string) --
The name (friendly name, not ARN) identifying the user.

UserId (string) --
The stable and unique string identifying the user. For more information about IDs, see IAM Identifiers in the IAM User Guide .





PolicyRoles (list) --
A list of IAM roles that the policy is attached to.

(dict) --
Contains information about a role that a managed policy is attached to.
This data type is used as a response element in the  ListEntitiesForPolicy operation.
For more information about managed policies, refer to Managed Policies and Inline Policies in the IAM User Guide .

RoleName (string) --
The name (friendly name, not ARN) identifying the role.

RoleId (string) --
The stable and unique string identifying the role. For more information about IDs, see IAM Identifiers in the IAM User Guide .





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.ServiceFailureException


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
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_group_policies(GroupName=None, Marker=None, MaxItems=None):
    """
    Lists the names of the inline policies that are embedded in the specified IAM group.
    An IAM group can also have managed policies attached to it. To list the managed policies that are attached to a group, use  ListAttachedGroupPolicies . For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    You can paginate the results using the MaxItems and Marker parameters. If there are no inline policies embedded with the specified group, the operation returns an empty list.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command lists the names of in-line policies that are embedded in the IAM group named Admins.
    Expected Output:
    
    :example: response = client.list_group_policies(
        GroupName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group to list policies for.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PolicyNames': [
        'string',
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  ListGroupPolicies request.

PolicyNames (list) --
A list of policy names.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

(string) --


IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command lists the names of in-line policies that are embedded in the IAM group named Admins.
response = client.list_group_policies(
    GroupName='Admins',
)

print(response)


Expected Output:
{
    'PolicyNames': [
        'AdminRoot',
        'KeyPolicy',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    Exceptions
    Examples
    The following command lists the IAM groups in the current account:
    Expected Output:
    
    :example: response = client.list_groups(
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. For example, the prefix /division_abc/subdivision_xyz/ gets all groups whose path starts with /division_abc/subdivision_xyz/ .\nThis parameter is optional. If it is not included, it defaults to a slash (/), listing all groups. This parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the response to a successful  ListGroups request.

Groups (list) --
A list of groups.

(dict) --
Contains information about an IAM group entity.
This data type is used as a response element in the following operations:

CreateGroup
GetGroup
ListGroups


Path (string) --
The path to the group. For more information about paths, see IAM Identifiers in the IAM User Guide .

GroupName (string) --
The friendly name that identifies the group.

GroupId (string) --
The stable and unique string identifying the group. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the group was created.





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.ServiceFailureException

Examples
The following command lists the IAM groups in the current account:
response = client.list_groups(
)

print(response)


Expected Output:
{
    'Groups': [
        {
            'Arn': 'arn:aws:iam::123456789012:group/Admins',
            'CreateDate': datetime(2016, 12, 15, 21, 40, 8, 3, 350, 0),
            'GroupId': 'AGPA1111111111EXAMPLE',
            'GroupName': 'Admins',
            'Path': '/division_abc/subdivision_xyz/',
        },
        {
            'Arn': 'arn:aws:iam::123456789012:group/division_abc/subdivision_xyz/product_1234/engineering/Test',
            'CreateDate': datetime(2016, 11, 30, 14, 10, 1, 2, 335, 0),
            'GroupId': 'AGP22222222222EXAMPLE',
            'GroupName': 'Test',
            'Path': '/division_abc/subdivision_xyz/product_1234/engineering/',
        },
        {
            'Arn': 'arn:aws:iam::123456789012:group/division_abc/subdivision_xyz/product_1234/Managers',
            'CreateDate': datetime(2016, 6, 12, 20, 14, 52, 6, 164, 0),
            'GroupId': 'AGPI3333333333EXAMPLE',
            'GroupName': 'Managers',
            'Path': '/division_abc/subdivision_xyz/product_1234/',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    Exceptions
    Examples
    The following command displays the groups that the IAM user named Bob belongs to.
    Expected Output:
    
    :example: response = client.list_groups_for_user(
        UserName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user to list groups for.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the response to a successful  ListGroupsForUser request.

Groups (list) --
A list of groups.

(dict) --
Contains information about an IAM group entity.
This data type is used as a response element in the following operations:

CreateGroup
GetGroup
ListGroups


Path (string) --
The path to the group. For more information about paths, see IAM Identifiers in the IAM User Guide .

GroupName (string) --
The friendly name that identifies the group.

GroupId (string) --
The stable and unique string identifying the group. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the group was created.





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command displays the groups that the IAM user named Bob belongs to.
response = client.list_groups_for_user(
    UserName='Bob',
)

print(response)


Expected Output:
{
    'Groups': [
        {
            'Arn': 'arn:aws:iam::123456789012:group/division_abc/subdivision_xyz/product_1234/engineering/Test',
            'CreateDate': datetime(2016, 11, 30, 14, 10, 1, 2, 335, 0),
            'GroupId': 'AGP2111111111EXAMPLE',
            'GroupName': 'Test',
            'Path': '/division_abc/subdivision_xyz/product_1234/engineering/',
        },
        {
            'Arn': 'arn:aws:iam::123456789012:group/division_abc/subdivision_xyz/product_1234/Managers',
            'CreateDate': datetime(2016, 6, 12, 20, 14, 52, 6, 164, 0),
            'GroupId': 'AGPI222222222SEXAMPLE',
            'GroupName': 'Managers',
            'Path': '/division_abc/subdivision_xyz/product_1234/',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    Lists the instance profiles that have the specified path prefix. If there are none, the operation returns an empty list. For more information about instance profiles, go to About Instance Profiles .
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_instance_profiles(
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. For example, the prefix /application_abc/component_xyz/ gets all instance profiles whose path starts with /application_abc/component_xyz/ .\nThis parameter is optional. If it is not included, it defaults to a slash (/), listing all instance profiles. This parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
                    'Description': 'string',
                    'MaxSessionDuration': 123,
                    'PermissionsBoundary': {
                        'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                        'PermissionsBoundaryArn': 'string'
                    },
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'RoleLastUsed': {
                        'LastUsedDate': datetime(2015, 1, 1),
                        'Region': 'string'
                    }
                },
            ]
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  ListInstanceProfiles request.

InstanceProfiles (list) --
A list of instance profiles.

(dict) --
Contains information about an instance profile.
This data type is used as a response element in the following operations:

CreateInstanceProfile
GetInstanceProfile
ListInstanceProfiles
ListInstanceProfilesForRole


Path (string) --
The path to the instance profile. For more information about paths, see IAM Identifiers in the IAM User Guide .

InstanceProfileName (string) --
The name identifying the instance profile.

InstanceProfileId (string) --
The stable and unique string identifying the instance profile. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the instance profile. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --
The date when the instance profile was created.

Roles (list) --
The role associated with the instance profile.

(dict) --
Contains information about an IAM role. This structure is returned as a response element in several API operations that interact with roles.

Path (string) --
The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide .

RoleName (string) --
The friendly name that identifies the role.

RoleId (string) --
The stable and unique string identifying the role. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide guide.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the role was created.

AssumeRolePolicyDocument (string) --
The policy that grants an entity permission to assume the role.

Description (string) --
A description of the role that you provide.

MaxSessionDuration (integer) --
The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI, or API to assume the role can specify the duration using the optional DurationSeconds API parameter or duration-seconds CLI parameter.

PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the role.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are attached to the specified role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.






RoleLastUsed (dict) --
Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see Regions Where Data Is Tracked in the IAM User Guide .

LastUsedDate (datetime) --
The date and time, in ISO 8601 date-time format that the role was last used.
This field is null if the role has not been used within the IAM tracking period. For more information about the tracking period, see Regions Where Data Is Tracked in the IAM User Guide .

Region (string) --
The name of the AWS Region in which the role was last used.











IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.ServiceFailureException


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
                        'Description': 'string',
                        'MaxSessionDuration': 123,
                        'PermissionsBoundary': {
                            'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                            'PermissionsBoundaryArn': 'string'
                        },
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'RoleLastUsed': {
                            'LastUsedDate': datetime(2015, 1, 1),
                            'Region': 'string'
                        }
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
    Lists the instance profiles that have the specified associated IAM role. If there are none, the operation returns an empty list. For more information about instance profiles, go to About Instance Profiles .
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_instance_profiles_for_role(
        RoleName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the role to list instance profiles for.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
                    'Description': 'string',
                    'MaxSessionDuration': 123,
                    'PermissionsBoundary': {
                        'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                        'PermissionsBoundaryArn': 'string'
                    },
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'RoleLastUsed': {
                        'LastUsedDate': datetime(2015, 1, 1),
                        'Region': 'string'
                    }
                },
            ]
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  ListInstanceProfilesForRole request.

InstanceProfiles (list) --
A list of instance profiles.

(dict) --
Contains information about an instance profile.
This data type is used as a response element in the following operations:

CreateInstanceProfile
GetInstanceProfile
ListInstanceProfiles
ListInstanceProfilesForRole


Path (string) --
The path to the instance profile. For more information about paths, see IAM Identifiers in the IAM User Guide .

InstanceProfileName (string) --
The name identifying the instance profile.

InstanceProfileId (string) --
The stable and unique string identifying the instance profile. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the instance profile. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --
The date when the instance profile was created.

Roles (list) --
The role associated with the instance profile.

(dict) --
Contains information about an IAM role. This structure is returned as a response element in several API operations that interact with roles.

Path (string) --
The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide .

RoleName (string) --
The friendly name that identifies the role.

RoleId (string) --
The stable and unique string identifying the role. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide guide.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the role was created.

AssumeRolePolicyDocument (string) --
The policy that grants an entity permission to assume the role.

Description (string) --
A description of the role that you provide.

MaxSessionDuration (integer) --
The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI, or API to assume the role can specify the duration using the optional DurationSeconds API parameter or duration-seconds CLI parameter.

PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the role.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are attached to the specified role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.






RoleLastUsed (dict) --
Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see Regions Where Data Is Tracked in the IAM User Guide .

LastUsedDate (datetime) --
The date and time, in ISO 8601 date-time format that the role was last used.
This field is null if the role has not been used within the IAM tracking period. For more information about the tracking period, see Regions Where Data Is Tracked in the IAM User Guide .

Region (string) --
The name of the AWS Region in which the role was last used.











IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException


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
                        'Description': 'string',
                        'MaxSessionDuration': 123,
                        'PermissionsBoundary': {
                            'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                            'PermissionsBoundaryArn': 'string'
                        },
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'RoleLastUsed': {
                            'LastUsedDate': datetime(2015, 1, 1),
                            'Region': 'string'
                        }
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
    Lists the MFA devices for an IAM user. If the request includes a IAM user name, then this operation lists all the MFA devices associated with the specified user. If you do not specify a user name, IAM determines the user name implicitly based on the AWS access key ID signing the request for this API.
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_mfa_devices(
        UserName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: The name of the user whose MFA devices you want to list.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the response to a successful  ListMFADevices request.

MFADevices (list) --
A list of MFA devices.

(dict) --
Contains information about an MFA device.
This data type is used as a response element in the  ListMFADevices operation.

UserName (string) --
The user with whom the MFA device is associated.

SerialNumber (string) --
The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN.

EnableDate (datetime) --
The date when the MFA device was enabled for the user.





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException


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
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_open_id_connect_providers():
    """
    Lists information about the IAM OpenID Connect (OIDC) provider resource objects defined in the AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_open_id_connect_providers()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'OpenIDConnectProviderList': [
        {
            'Arn': 'string'
        },
    ]
}


Response Structure

(dict) --Contains the response to a successful  ListOpenIDConnectProviders request.

OpenIDConnectProviderList (list) --The list of IAM OIDC provider resource objects defined in the AWS account.

(dict) --Contains the Amazon Resource Name (ARN) for an IAM OpenID Connect provider.

Arn (string) --The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .










Exceptions

IAM.Client.exceptions.ServiceFailureException


    :return: {
        'OpenIDConnectProviderList': [
            {
                'Arn': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_policies(Scope=None, OnlyAttached=None, PathPrefix=None, PolicyUsageFilter=None, Marker=None, MaxItems=None):
    """
    Lists all the managed policies that are available in your AWS account, including your own customer-defined managed policies and all AWS managed policies.
    You can filter the list of policies that is returned using the optional OnlyAttached , Scope , and PathPrefix parameters. For example, to list only the customer managed policies in your AWS account, set Scope to Local . To list only AWS managed policies, set Scope to AWS .
    You can paginate the results using the MaxItems and Marker parameters.
    For more information about managed policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_policies(
        Scope='All'|'AWS'|'Local',
        OnlyAttached=True|False,
        PathPrefix='string',
        PolicyUsageFilter='PermissionsPolicy'|'PermissionsBoundary',
        Marker='string',
        MaxItems=123
    )
    
    
    :type Scope: string
    :param Scope: The scope to use for filtering the results.\nTo list only AWS managed policies, set Scope to AWS . To list only the customer managed policies in your AWS account, set Scope to Local .\nThis parameter is optional. If it is not included, or if it is set to All , all policies are returned.\n

    :type OnlyAttached: boolean
    :param OnlyAttached: A flag to filter the results to only the attached policies.\nWhen OnlyAttached is true , the returned list contains only the policies that are attached to an IAM user, group, or role. When OnlyAttached is false , or when the parameter is not included, all policies are returned.\n

    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies. This parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.

    :type PolicyUsageFilter: string
    :param PolicyUsageFilter: The policy usage method to use for filtering the results.\nTo list only permissions policies, set PolicyUsageFilter to PermissionsPolicy . To list only the policies used to set permissions boundaries, set the value to PermissionsBoundary .\nThis parameter is optional. If it is not included, all policies are returned.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Policies': [
        {
            'PolicyName': 'string',
            'PolicyId': 'string',
            'Arn': 'string',
            'Path': 'string',
            'DefaultVersionId': 'string',
            'AttachmentCount': 123,
            'PermissionsBoundaryUsageCount': 123,
            'IsAttachable': True|False,
            'Description': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'UpdateDate': datetime(2015, 1, 1)
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  ListPolicies request.

Policies (list) --
A list of policies.

(dict) --
Contains information about a managed policy.
This data type is used as a response element in the  CreatePolicy ,  GetPolicy , and  ListPolicies operations.
For more information about managed policies, refer to Managed Policies and Inline Policies in the IAM User Guide .

PolicyName (string) --
The friendly name (not ARN) identifying the policy.

PolicyId (string) --
The stable and unique string identifying the policy.
For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .

Path (string) --
The path to the policy.
For more information about paths, see IAM Identifiers in the IAM User Guide .

DefaultVersionId (string) --
The identifier for the version of the policy that is set as the default version.

AttachmentCount (integer) --
The number of entities (users, groups, and roles) that the policy is attached to.

PermissionsBoundaryUsageCount (integer) --
The number of entities (users and roles) for which the policy is used to set the permissions boundary.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

IsAttachable (boolean) --
Specifies whether the policy can be attached to an IAM user, group, or role.

Description (string) --
A friendly description of the policy.
This element is included in the response to the  GetPolicy operation. It is not included in the response to the  ListPolicies operation.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the policy was created.

UpdateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the policy was last updated.
When a policy has only one version, this field contains the date and time when the policy was created. When a policy has more than one version, this field contains the date and time when the most recent policy version was created.





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.ServiceFailureException


    :return: {
        'Policies': [
            {
                'PolicyName': 'string',
                'PolicyId': 'string',
                'Arn': 'string',
                'Path': 'string',
                'DefaultVersionId': 'string',
                'AttachmentCount': 123,
                'PermissionsBoundaryUsageCount': 123,
                'IsAttachable': True|False,
                'Description': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'UpdateDate': datetime(2015, 1, 1)
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_policies_granting_service_access(Marker=None, Arn=None, ServiceNamespaces=None):
    """
    Retrieves a list of policies that the IAM identity (user, group, or role) can use to access each specified service.
    The list of policies returned by the operation depends on the ARN of the identity that you provide.
    For each managed policy, this operation returns the ARN and policy name. For each inline policy, it returns the policy name and the entity to which it is attached. Inline policies do not have an ARN. For more information about these policy types, see Managed Policies and Inline Policies in the IAM User Guide .
    Policies that are attached to users and roles as permissions boundaries are not returned. To view which managed policy is currently used to set the permissions boundary for a user or role, use the  GetUser or  GetRole operations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_policies_granting_service_access(
        Marker='string',
        Arn='string',
        ServiceNamespaces=[
            'string',
        ]
    )
    
    
    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type Arn: string
    :param Arn: [REQUIRED]\nThe ARN of the IAM identity (user, group, or role) whose policies you want to list.\n

    :type ServiceNamespaces: list
    :param ServiceNamespaces: [REQUIRED]\nThe service namespace for the AWS services whose policies you want to list.\nTo learn the service namespace for a service, go to Actions, Resources, and Condition Keys for AWS Services in the IAM User Guide . Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, (service prefix: a4b) . For more information about service namespaces, see AWS Service Namespaces in the AWS General Reference .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PoliciesGrantingServiceAccess': [
        {
            'ServiceNamespace': 'string',
            'Policies': [
                {
                    'PolicyName': 'string',
                    'PolicyType': 'INLINE'|'MANAGED',
                    'PolicyArn': 'string',
                    'EntityType': 'USER'|'ROLE'|'GROUP',
                    'EntityName': 'string'
                },
            ]
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --

PoliciesGrantingServiceAccess (list) --
A ListPoliciesGrantingServiceAccess object that contains details about the permissions policies attached to the specified identity (user, group, or role).

(dict) --
Contains details about the permissions policies that are attached to the specified identity (user, group, or role).
This data type is used as a response element in the  ListPoliciesGrantingServiceAccess operation.

ServiceNamespace (string) --
The namespace of the service that was accessed.
To learn the service namespace of a service, go to Actions, Resources, and Condition Keys for AWS Services in the IAM User Guide . Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, (service prefix: a4b) . For more information about service namespaces, see AWS Service Namespaces in the AWS General Reference .

Policies (list) --
The PoliciesGrantingServiceAccess object that contains details about the policy.

(dict) --
Contains details about the permissions policies that are attached to the specified identity (user, group, or role).
This data type is an element of the  ListPoliciesGrantingServiceAccessEntry object.

PolicyName (string) --
The policy name.

PolicyType (string) --
The policy type. For more information about these policy types, see Managed Policies and Inline Policies in the IAM User Guide .

PolicyArn (string) --
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .

EntityType (string) --
The type of entity (user or role) that used the policy to access the service to which the inline policy is attached.
This field is null for managed policies. For more information about these policy types, see Managed Policies and Inline Policies in the IAM User Guide .

EntityName (string) --
The name of the entity (user or role) to which the inline policy is attached.
This field is null for managed policies. For more information about these policy types, see Managed Policies and Inline Policies in the IAM User Guide .









IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException


    :return: {
        'PoliciesGrantingServiceAccess': [
            {
                'ServiceNamespace': 'string',
                'Policies': [
                    {
                        'PolicyName': 'string',
                        'PolicyType': 'INLINE'|'MANAGED',
                        'PolicyArn': 'string',
                        'EntityType': 'USER'|'ROLE'|'GROUP',
                        'EntityName': 'string'
                    },
                ]
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    Marker (string) -- Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.
    Arn (string) -- [REQUIRED]
    The ARN of the IAM identity (user, group, or role) whose policies you want to list.
    
    ServiceNamespaces (list) -- [REQUIRED]
    The service namespace for the AWS services whose policies you want to list.
    To learn the service namespace for a service, go to Actions, Resources, and Condition Keys for AWS Services in the IAM User Guide . Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, (service prefix: a4b) . For more information about service namespaces, see AWS Service Namespaces in the AWS General Reference .
    
    (string) --
    
    
    
    """
    pass

def list_policy_versions(PolicyArn=None, Marker=None, MaxItems=None):
    """
    Lists information about the versions of the specified managed policy, including the version that is currently set as the policy\'s default version.
    For more information about managed policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_policy_versions(
        PolicyArn='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM policy for which you want the versions.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the response to a successful  ListPolicyVersions request.

Versions (list) --
A list of policy versions.
For more information about managed policy versions, see Versioning for Managed Policies in the IAM User Guide .

(dict) --
Contains information about a version of a managed policy.
This data type is used as a response element in the  CreatePolicyVersion ,  GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations.
For more information about managed policies, refer to Managed Policies and Inline Policies in the IAM User Guide .

Document (string) --
The policy document.
The policy document is returned in the response to the  GetPolicyVersion and  GetAccountAuthorizationDetails operations. It is not returned in the response to the  CreatePolicyVersion or  ListPolicyVersions operations.
The policy document returned in this structure is URL-encoded compliant with RFC 3986 . You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the decode method of the java.net.URLDecoder utility class in the Java SDK. Other languages and SDKs provide similar functionality.

VersionId (string) --
The identifier for the policy version.
Policy version identifiers always begin with v (always lowercase). When a policy is created, the first policy version is v1 .

IsDefaultVersion (boolean) --
Specifies whether the policy version is set as the policy\'s default version.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the policy version was created.





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.ServiceFailureException


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
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_role_policies(RoleName=None, Marker=None, MaxItems=None):
    """
    Lists the names of the inline policies that are embedded in the specified IAM role.
    An IAM role can also have managed policies attached to it. To list the managed policies that are attached to a role, use  ListAttachedRolePolicies . For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    You can paginate the results using the MaxItems and Marker parameters. If there are no inline policies embedded with the specified role, the operation returns an empty list.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_role_policies(
        RoleName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the role to list policies for.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PolicyNames': [
        'string',
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  ListRolePolicies request.

PolicyNames (list) --
A list of policy names.

(string) --


IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException


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

def list_role_tags(RoleName=None, Marker=None, MaxItems=None):
    """
    Lists the tags that are attached to the specified role. The returned list of tags is sorted by tag key. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_role_tags(
        RoleName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the IAM role for which you want to see the list of tags.\nThis parameter accepts (through its regex pattern ) a string of characters that consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items that you want in the response. If additional items exist beyond the maximum that you specify, the IsTruncated response element is true .\nIf you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when more results are available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --

Tags (list) --
The list of tags currently that is attached to the role. Each tag consists of a key name and an associated value. If no tags are attached to the specified role, the response contains an empty list.

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.






IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can use the Marker request parameter to make a subsequent pagination request that retrieves more items. Note that IAM might return fewer than the MaxItems number of results even when more results are available. Check IsTruncated after every call to ensure that you receive all of your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_roles(PathPrefix=None, Marker=None, MaxItems=None):
    """
    Lists the IAM roles that have the specified path prefix. If there are none, the operation returns an empty list. For more information about roles, go to Working with Roles .
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_roles(
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. For example, the prefix /application_abc/component_xyz/ gets all roles whose path starts with /application_abc/component_xyz/ .\nThis parameter is optional. If it is not included, it defaults to a slash (/), listing all roles. This parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Roles': [
        {
            'Path': 'string',
            'RoleName': 'string',
            'RoleId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'AssumeRolePolicyDocument': 'string',
            'Description': 'string',
            'MaxSessionDuration': 123,
            'PermissionsBoundary': {
                'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                'PermissionsBoundaryArn': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'RoleLastUsed': {
                'LastUsedDate': datetime(2015, 1, 1),
                'Region': 'string'
            }
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  ListRoles request.

Roles (list) --
A list of roles.

(dict) --
Contains information about an IAM role. This structure is returned as a response element in several API operations that interact with roles.

Path (string) --
The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide .

RoleName (string) --
The friendly name that identifies the role.

RoleId (string) --
The stable and unique string identifying the role. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide guide.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the role was created.

AssumeRolePolicyDocument (string) --
The policy that grants an entity permission to assume the role.

Description (string) --
A description of the role that you provide.

MaxSessionDuration (integer) --
The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI, or API to assume the role can specify the duration using the optional DurationSeconds API parameter or duration-seconds CLI parameter.

PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the role.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are attached to the specified role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.






RoleLastUsed (dict) --
Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see Regions Where Data Is Tracked in the IAM User Guide .

LastUsedDate (datetime) --
The date and time, in ISO 8601 date-time format that the role was last used.
This field is null if the role has not been used within the IAM tracking period. For more information about the tracking period, see Regions Where Data Is Tracked in the IAM User Guide .

Region (string) --
The name of the AWS Region in which the role was last used.







IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.ServiceFailureException


    :return: {
        'Roles': [
            {
                'Path': 'string',
                'RoleName': 'string',
                'RoleId': 'string',
                'Arn': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'AssumeRolePolicyDocument': 'string',
                'Description': 'string',
                'MaxSessionDuration': 123,
                'PermissionsBoundary': {
                    'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                    'PermissionsBoundaryArn': 'string'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'RoleLastUsed': {
                    'LastUsedDate': datetime(2015, 1, 1),
                    'Region': 'string'
                }
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_saml_providers():
    """
    Lists the SAML provider resource objects defined in IAM in the account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_saml_providers()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'SAMLProviderList': [
        {
            'Arn': 'string',
            'ValidUntil': datetime(2015, 1, 1),
            'CreateDate': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --Contains the response to a successful  ListSAMLProviders request.

SAMLProviderList (list) --The list of SAML provider resource objects defined in IAM for this AWS account.

(dict) --Contains the list of SAML providers for this account.

Arn (string) --The Amazon Resource Name (ARN) of the SAML provider.

ValidUntil (datetime) --The expiration date and time for the SAML provider.

CreateDate (datetime) --The date and time when the SAML provider was created.










Exceptions

IAM.Client.exceptions.ServiceFailureException


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
    Lists the server certificates stored in IAM that have the specified path prefix. If none exist, the operation returns an empty list.
    You can paginate the results using the MaxItems and Marker parameters.
    For more information about working with server certificates, see Working with Server Certificates in the IAM User Guide . This topic also includes a list of AWS services that can use the server certificates that you manage with IAM.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_server_certificates(
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. For example: /company/servercerts would get all server certificates for which the path starts with /company/servercerts .\nThis parameter is optional. If it is not included, it defaults to a slash (/), listing all server certificates. This parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the response to a successful  ListServerCertificates request.

ServerCertificateMetadataList (list) --
A list of server certificates.

(dict) --
Contains information about a server certificate without its certificate body, certificate chain, and private key.
This data type is used as a response element in the  UploadServerCertificate and  ListServerCertificates operations.

Path (string) --
The path to the server certificate. For more information about paths, see IAM Identifiers in the IAM User Guide .

ServerCertificateName (string) --
The name that identifies the server certificate.

ServerCertificateId (string) --
The stable and unique string identifying the server certificate. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the server certificate. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .

UploadDate (datetime) --
The date when the server certificate was uploaded.

Expiration (datetime) --
The date on which the certificate is set to expire.





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.ServiceFailureException


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
    
    
    :returns: 
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_service_specific_credentials(UserName=None, ServiceName=None):
    """
    Returns information about the service-specific credentials associated with the specified IAM user. If none exists, the operation returns an empty list. The service-specific credentials returned by this operation are used only for authenticating the IAM user to a specific service. For more information about using service-specific credentials to authenticate to an AWS service, see Set Up service-specific credentials in the AWS CodeCommit User Guide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_service_specific_credentials(
        UserName='string',
        ServiceName='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the user whose service-specific credentials you want information about. If this value is not specified, then the operation assumes the user whose credentials are used to call the operation.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type ServiceName: string
    :param ServiceName: Filters the returned results to only those for the specified AWS service. If not specified, then AWS returns service-specific credentials for all services.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ServiceSpecificCredentials (list) --
A list of structures that each contain details about a service-specific credential.

(dict) --
Contains additional details about a service-specific credential.

UserName (string) --
The name of the IAM user associated with the service-specific credential.

Status (string) --
The status of the service-specific credential. Active means that the key is valid for API calls, while Inactive means it is not.

ServiceUserName (string) --
The generated user name for the service-specific credential.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the service-specific credential were created.

ServiceSpecificCredentialId (string) --
The unique identifier for the service-specific credential.

ServiceName (string) --
The name of the service associated with the service-specific credential.











Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceNotSupportedException


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
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceNotSupportedException
    
    """
    pass

def list_signing_certificates(UserName=None, Marker=None, MaxItems=None):
    """
    Returns information about the signing certificates associated with the specified IAM user. If none exists, the operation returns an empty list.
    Although each user is limited to a small number of signing certificates, you can still paginate the results using the MaxItems and Marker parameters.
    If the UserName field is not specified, the user name is determined implicitly based on the AWS access key ID used to sign the request for this API. This operation works for access keys under the AWS account. Consequently, you can use this operation to manage AWS account root user credentials even if the AWS account has no associated users.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command lists the signing certificates for the IAM user named Bob.
    Expected Output:
    
    :example: response = client.list_signing_certificates(
        UserName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: The name of the IAM user whose signing certificates you want to examine.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the response to a successful  ListSigningCertificates request.

Certificates (list) --
A list of the user\'s signing certificate information.

(dict) --
Contains information about an X.509 signing certificate.
This data type is used as a response element in the  UploadSigningCertificate and  ListSigningCertificates operations.

UserName (string) --
The name of the user the signing certificate is associated with.

CertificateId (string) --
The ID for the signing certificate.

CertificateBody (string) --
The contents of the signing certificate.

Status (string) --
The status of the signing certificate. Active means that the key is valid for API calls, while Inactive means it is not.

UploadDate (datetime) --
The date when the signing certificate was uploaded.





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command lists the signing certificates for the IAM user named Bob.
response = client.list_signing_certificates(
    UserName='Bob',
)

print(response)


Expected Output:
{
    'Certificates': [
        {
            'CertificateBody': '-----BEGIN CERTIFICATE-----<certificate-body>-----END CERTIFICATE-----',
            'CertificateId': 'TA7SMP42TDN5Z26OBPJE7EXAMPLE',
            'Status': 'Active',
            'UploadDate': datetime(2013, 6, 6, 21, 40, 8, 3, 157, 0),
            'UserName': 'Bob',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_ssh_public_keys(UserName=None, Marker=None, MaxItems=None):
    """
    Returns information about the SSH public keys associated with the specified IAM user. If none exists, the operation returns an empty list.
    The SSH public keys returned by this operation are used only for authenticating the IAM user to an AWS CodeCommit repository. For more information about using SSH keys to authenticate to an AWS CodeCommit repository, see Set up AWS CodeCommit for SSH Connections in the AWS CodeCommit User Guide .
    Although each user is limited to a small number of keys, you can still paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_ssh_public_keys(
        UserName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: The name of the IAM user to list SSH public keys for. If none is specified, the UserName field is determined implicitly based on the AWS access key used to sign the request.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the response to a successful  ListSSHPublicKeys request.

SSHPublicKeys (list) --
A list of the SSH public keys assigned to IAM user.

(dict) --
Contains information about an SSH public key, without the key\'s body or fingerprint.
This data type is used as a response element in the  ListSSHPublicKeys operation.

UserName (string) --
The name of the IAM user associated with the SSH public key.

SSHPublicKeyId (string) --
The unique identifier for the SSH public key.

Status (string) --
The status of the SSH public key. Active means that the key can be used for authentication with an AWS CodeCommit repository. Inactive means that the key cannot be used.

UploadDate (datetime) --
The date and time, in ISO 8601 date-time format , when the SSH public key was uploaded.





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException


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
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    
    """
    pass

def list_user_policies(UserName=None, Marker=None, MaxItems=None):
    """
    Lists the names of the inline policies embedded in the specified IAM user.
    An IAM user can also have managed policies attached to it. To list the managed policies that are attached to a user, use  ListAttachedUserPolicies . For more information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    You can paginate the results using the MaxItems and Marker parameters. If there are no inline policies embedded with the specified user, the operation returns an empty list.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_user_policies(
        UserName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user to list policies for.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PolicyNames': [
        'string',
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  ListUserPolicies request.

PolicyNames (list) --
A list of policy names.

(string) --


IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException


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

def list_user_tags(UserName=None, Marker=None, MaxItems=None):
    """
    Lists the tags that are attached to the specified user. The returned list of tags is sorted by tag key. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_user_tags(
        UserName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the IAM user whose tags you want to see.\nThis parameter accepts (through its regex pattern ) a string of characters that consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: (Optional) Use this only when paginating results to indicate the maximum number of items that you want in the response. If additional items exist beyond the maximum that you specify, the IsTruncated response element is true .\nIf you do not include this parameter, it defaults to 100. Note that IAM might return fewer results, even when more results are available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --

Tags (list) --
The list of tags that are currently attached to the user. Each tag consists of a key name and an associated value. If no tags are attached to the specified user, the response contains an empty list.

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.






IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can use the Marker request parameter to make a subsequent pagination request that retrieves more items. Note that IAM might return fewer than the MaxItems number of results even when more results are available. Check IsTruncated after every call to ensure that you receive all of your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_users(PathPrefix=None, Marker=None, MaxItems=None):
    """
    Lists the IAM users that have the specified path prefix. If no path prefix is specified, the operation returns all users in the AWS account. If there are none, the operation returns an empty list.
    You can paginate the results using the MaxItems and Marker parameters.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command lists the IAM users in the current account.
    Expected Output:
    
    :example: response = client.list_users(
        PathPrefix='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type PathPrefix: string
    :param PathPrefix: The path prefix for filtering the results. For example: /division_abc/subdivision_xyz/ , which would get all user names whose path starts with /division_abc/subdivision_xyz/ .\nThis parameter is optional. If it is not included, it defaults to a slash (/), listing all user names. This parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Users': [
        {
            'Path': 'string',
            'UserName': 'string',
            'UserId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'PasswordLastUsed': datetime(2015, 1, 1),
            'PermissionsBoundary': {
                'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                'PermissionsBoundaryArn': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  ListUsers request.

Users (list) --
A list of users.

(dict) --
Contains information about an IAM user entity.
This data type is used as a response element in the following operations:

CreateUser
GetUser
ListUsers


Path (string) --
The path to the user. For more information about paths, see IAM Identifiers in the IAM User Guide .

UserName (string) --
The friendly name identifying the user.

UserId (string) --
The stable and unique string identifying the user. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the user was created.

PasswordLastUsed (datetime) --
The date and time, in ISO 8601 date-time format , when the user\'s password was last used to sign in to an AWS website. For a list of AWS websites that capture a user\'s last sign-in time, see the Credential Reports topic in the IAM User Guide . If a password is used more than once in a five-minute span, only the first use is returned in this field. If the field is null (no value), then it indicates that they never signed in with a password. This can be because:

The user never had a password.
A password exists but has not been used since IAM started tracking this information on October 20, 2014.

A null value does not mean that the user never had a password. Also, if the user does not currently have a password but had one in the past, then this field contains the date and time the most recent password was used.
This value is returned only in the  GetUser and  ListUsers operations.

PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the user.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are associated with the specified user. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.










IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.ServiceFailureException

Examples
The following command lists the IAM users in the current account.
response = client.list_users(
)

print(response)


Expected Output:
{
    'Users': [
        {
            'Arn': 'arn:aws:iam::123456789012:user/division_abc/subdivision_xyz/engineering/Juan',
            'CreateDate': datetime(2012, 9, 5, 19, 38, 48, 2, 249, 0),
            'PasswordLastUsed': datetime(2016, 9, 8, 21, 47, 36, 3, 252, 0),
            'Path': '/division_abc/subdivision_xyz/engineering/',
            'UserId': 'AID2MAB8DPLSRHEXAMPLE',
            'UserName': 'Juan',
        },
        {
            'Arn': 'arn:aws:iam::123456789012:user/division_abc/subdivision_xyz/engineering/Anika',
            'CreateDate': datetime(2014, 4, 9, 15, 43, 45, 2, 99, 0),
            'PasswordLastUsed': datetime(2016, 9, 24, 16, 18, 7, 5, 268, 0),
            'Path': '/division_abc/subdivision_xyz/engineering/',
            'UserId': 'AIDIODR4TAW7CSEXAMPLE',
            'UserName': 'Anika',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Users': [
            {
                'Path': 'string',
                'UserName': 'string',
                'UserId': 'string',
                'Arn': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'PasswordLastUsed': datetime(2015, 1, 1),
                'PermissionsBoundary': {
                    'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                    'PermissionsBoundaryArn': 'string'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
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
    Lists the virtual MFA devices defined in the AWS account by assignment status. If you do not specify an assignment status, the operation returns a list of all virtual MFA devices. Assignment status can be Assigned , Unassigned , or Any .
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
    :param AssignmentStatus: The status (Unassigned or Assigned ) of the devices to list. If you do not specify an AssignmentStatus , the operation defaults to Any , which lists both assigned and unassigned virtual MFA devices.,

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
                'PasswordLastUsed': datetime(2015, 1, 1),
                'PermissionsBoundary': {
                    'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                    'PermissionsBoundaryArn': 'string'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
            'EnableDate': datetime(2015, 1, 1)
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  ListVirtualMFADevices request.

VirtualMFADevices (list) --
The list of virtual MFA devices in the current account that match the AssignmentStatus value that was passed in the request.

(dict) --
Contains information about a virtual MFA device.

SerialNumber (string) --
The serial number associated with VirtualMFADevice .

Base32StringSeed (bytes) --
The base32 seed defined as specified in RFC3548 . The Base32StringSeed is base64-encoded.

QRCodePNG (bytes) --
A QR code PNG image that encodes otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String where $virtualMFADeviceName is one of the create call arguments. AccountName is the user name if set (otherwise, the account ID otherwise), and Base32String is the seed in base32 format. The Base32String value is base64-encoded.

User (dict) --
The IAM user associated with this virtual MFA device.

Path (string) --
The path to the user. For more information about paths, see IAM Identifiers in the IAM User Guide .

UserName (string) --
The friendly name identifying the user.

UserId (string) --
The stable and unique string identifying the user. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see IAM Identifiers in the IAM User Guide .

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the user was created.

PasswordLastUsed (datetime) --
The date and time, in ISO 8601 date-time format , when the user\'s password was last used to sign in to an AWS website. For a list of AWS websites that capture a user\'s last sign-in time, see the Credential Reports topic in the IAM User Guide . If a password is used more than once in a five-minute span, only the first use is returned in this field. If the field is null (no value), then it indicates that they never signed in with a password. This can be because:

The user never had a password.
A password exists but has not been used since IAM started tracking this information on October 20, 2014.

A null value does not mean that the user never had a password. Also, if the user does not currently have a password but had one in the past, then this field contains the date and time the most recent password was used.
This value is returned only in the  GetUser and  ListUsers operations.

PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the user.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are associated with the specified user. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.








EnableDate (datetime) --
The date and time on which the virtual MFA device was enabled.





IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Examples
The following command lists the virtual MFA devices that have been configured for the current account.
response = client.list_virtual_mfa_devices(
)

print(response)


Expected Output:
{
    'VirtualMFADevices': [
        {
            'SerialNumber': 'arn:aws:iam::123456789012:mfa/ExampleMFADevice',
        },
        {
            'SerialNumber': 'arn:aws:iam::123456789012:mfa/Juan',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                    'PasswordLastUsed': datetime(2015, 1, 1),
                    'PermissionsBoundary': {
                        'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                        'PermissionsBoundaryArn': 'string'
                    },
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
                'EnableDate': datetime(2015, 1, 1)
            },
        ],
        'IsTruncated': True|False,
        'Marker': 'string'
    }
    
    
    :returns: 
    The user never had a password.
    A password exists but has not been used since IAM started tracking this information on October 20, 2014.
    
    """
    pass

def put_group_policy(GroupName=None, PolicyName=None, PolicyDocument=None):
    """
    Adds or updates an inline policy document that is embedded in the specified IAM group.
    A user can also have managed policies attached to it. To attach a managed policy to a group, use  AttachGroupPolicy . To create a new managed policy, use  CreatePolicy . For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    For information about limits on the number of inline policies that you can embed in a group, see Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command adds a policy named AllPerms to the IAM group named Admins.
    Expected Output:
    
    :example: response = client.put_group_policy(
        GroupName='string',
        PolicyName='string',
        PolicyDocument='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group to associate the policy with.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-.\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the policy document.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyDocument: string
    :param PolicyDocument: [REQUIRED]\nThe policy document.\nYou must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n

    :return: response = client.put_group_policy(
        GroupName='Admins',
        PolicyDocument='{"Version":"2012-10-17","Statement":{"Effect":"Allow","Action":"*","Resource":"*"}}',
        PolicyName='AllPerms',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.MalformedPolicyDocumentException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def put_role_permissions_boundary(RoleName=None, PermissionsBoundary=None):
    """
    Adds or updates the policy that is specified as the IAM role\'s permissions boundary. You can use an AWS managed policy or a customer managed policy to set the boundary for a role. Use the boundary to control the maximum permissions that the role can have. Setting a permissions boundary is an advanced feature that can affect the permissions for the role.
    You cannot set the boundary for a service-linked role.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_role_permissions_boundary(
        RoleName='string',
        PermissionsBoundary='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name (friendly name, not ARN) of the IAM role for which you want to set the permissions boundary.\n

    :type PermissionsBoundary: string
    :param PermissionsBoundary: [REQUIRED]\nThe ARN of the policy that is used to set the permissions boundary for the role.\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.UnmodifiableEntityException
    IAM.Client.exceptions.PolicyNotAttachableException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def put_role_policy(RoleName=None, PolicyName=None, PolicyDocument=None):
    """
    Adds or updates an inline policy document that is embedded in the specified IAM role.
    When you embed an inline policy in a role, the inline policy is used as part of the role\'s access (permissions) policy. The role\'s trust policy is created at the same time as the role, using  CreateRole . You can update a role\'s trust policy using  UpdateAssumeRolePolicy . For more information about IAM roles, go to Using Roles to Delegate Permissions and Federate Identities .
    A role can also have a managed policy attached to it. To attach a managed policy to a role, use  AttachRolePolicy . To create a new managed policy, use  CreatePolicy . For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    For information about limits on the number of inline policies that you can embed with a role, see Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command adds a permissions policy to the role named Test-Role.
    Expected Output:
    
    :example: response = client.put_role_policy(
        RoleName='string',
        PolicyName='string',
        PolicyDocument='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the role to associate the policy with.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the policy document.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyDocument: string
    :param PolicyDocument: [REQUIRED]\nThe policy document.\nYou must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n

    :return: response = client.put_role_policy(
        PolicyDocument='{"Version":"2012-10-17","Statement":{"Effect":"Allow","Action":"s3:*","Resource":"*"}}',
        PolicyName='S3AccessPolicy',
        RoleName='S3Access',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.MalformedPolicyDocumentException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.UnmodifiableEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def put_user_permissions_boundary(UserName=None, PermissionsBoundary=None):
    """
    Adds or updates the policy that is specified as the IAM user\'s permissions boundary. You can use an AWS managed policy or a customer managed policy to set the boundary for a user. Use the boundary to control the maximum permissions that the user can have. Setting a permissions boundary is an advanced feature that can affect the permissions for the user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_user_permissions_boundary(
        UserName='string',
        PermissionsBoundary='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name (friendly name, not ARN) of the IAM user for which you want to set the permissions boundary.\n

    :type PermissionsBoundary: string
    :param PermissionsBoundary: [REQUIRED]\nThe ARN of the policy that is used to set the permissions boundary for the user.\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.PolicyNotAttachableException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def put_user_policy(UserName=None, PolicyName=None, PolicyDocument=None):
    """
    Adds or updates an inline policy document that is embedded in the specified IAM user.
    An IAM user can also have a managed policy attached to it. To attach a managed policy to a user, use  AttachUserPolicy . To create a new managed policy, use  CreatePolicy . For information about policies, see Managed Policies and Inline Policies in the IAM User Guide .
    For information about limits on the number of inline policies that you can embed in a user, see Limitations on IAM Entities in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command attaches a policy to the IAM user named Bob.
    Expected Output:
    
    :example: response = client.put_user_policy(
        UserName='string',
        PolicyName='string',
        PolicyDocument='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user to associate the policy with.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the policy document.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyDocument: string
    :param PolicyDocument: [REQUIRED]\nThe policy document.\nYou must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n

    :return: response = client.put_user_policy(
        PolicyDocument='{"Version":"2012-10-17","Statement":{"Effect":"Allow","Action":"*","Resource":"*"}}',
        PolicyName='AllAccessPolicy',
        UserName='Bob',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.MalformedPolicyDocumentException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def remove_client_id_from_open_id_connect_provider(OpenIDConnectProviderArn=None, ClientID=None):
    """
    Removes the specified client ID (also known as audience) from the list of client IDs registered for the specified IAM OpenID Connect (OIDC) provider resource object.
    This operation is idempotent; it does not fail or return an error if you try to remove a client ID that does not exist.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_client_id_from_open_id_connect_provider(
        OpenIDConnectProviderArn='string',
        ClientID='string'
    )
    
    
    :type OpenIDConnectProviderArn: string
    :param OpenIDConnectProviderArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM OIDC provider resource to remove the client ID from. You can get a list of OIDC provider ARNs by using the ListOpenIDConnectProviders operation.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :type ClientID: string
    :param ClientID: [REQUIRED]\nThe client ID (also known as audience) to remove from the IAM OIDC provider resource. For more information about client IDs, see CreateOpenIDConnectProvider .\n

    :returns: 
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def remove_role_from_instance_profile(InstanceProfileName=None, RoleName=None):
    """
    Removes the specified IAM role from the specified EC2 instance profile.
    For more information about IAM roles, go to Working with Roles . For more information about instance profiles, go to About Instance Profiles .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command removes the role named Test-Role from the instance profile named ExampleInstanceProfile.
    Expected Output:
    
    :example: response = client.remove_role_from_instance_profile(
        InstanceProfileName='string',
        RoleName='string'
    )
    
    
    :type InstanceProfileName: string
    :param InstanceProfileName: [REQUIRED]\nThe name of the instance profile to update.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the role to remove.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :return: response = client.remove_role_from_instance_profile(
        InstanceProfileName='ExampleInstanceProfile',
        RoleName='Test-Role',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.UnmodifiableEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def remove_user_from_group(GroupName=None, UserName=None):
    """
    Removes the specified user from the specified group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command removes the user named Bob from the IAM group named Admins.
    Expected Output:
    
    :example: response = client.remove_user_from_group(
        GroupName='string',
        UserName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group to update.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user to remove.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :return: response = client.remove_user_from_group(
        GroupName='Admins',
        UserName='Bob',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def reset_service_specific_credential(UserName=None, ServiceSpecificCredentialId=None):
    """
    Resets the password for a service-specific credential. The new password is AWS generated and cryptographically strong. It cannot be configured by the user. Resetting the password immediately invalidates the previous password associated with this user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reset_service_specific_credential(
        UserName='string',
        ServiceSpecificCredentialId='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the IAM user associated with the service-specific credential. If this value is not specified, then the operation assumes the user whose credentials are used to call the operation.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type ServiceSpecificCredentialId: string
    :param ServiceSpecificCredentialId: [REQUIRED]\nThe unique identifier of the service-specific credential.\nThis parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ServiceSpecificCredential (dict) --
A structure with details about the updated service-specific credential, including the new password.

Warning
This is the only time that you can access the password. You cannot recover the password later, but you can reset it again.


CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the service-specific credential were created.

ServiceName (string) --
The name of the service associated with the service-specific credential.

ServiceUserName (string) --
The generated user name for the service-specific credential. This value is generated by combining the IAM user\'s name combined with the ID number of the AWS account, as in jane-at-123456789012 , for example. This value cannot be configured by the user.

ServicePassword (string) --
The generated password for the service-specific credential.

ServiceSpecificCredentialId (string) --
The unique identifier for the service-specific credential.

UserName (string) --
The name of the IAM user associated with the service-specific credential.

Status (string) --
The status of the service-specific credential. Active means that the key is valid for API calls, while Inactive means it is not.









Exceptions

IAM.Client.exceptions.NoSuchEntityException


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
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    
    """
    pass

def resync_mfa_device(UserName=None, SerialNumber=None, AuthenticationCode1=None, AuthenticationCode2=None):
    """
    Synchronizes the specified MFA device with its IAM resource object on the AWS servers.
    For more information about creating and working with virtual MFA devices, go to Using a Virtual MFA Device in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.resync_mfa_device(
        UserName='string',
        SerialNumber='string',
        AuthenticationCode1='string',
        AuthenticationCode2='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user whose MFA device you want to resynchronize.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type SerialNumber: string
    :param SerialNumber: [REQUIRED]\nSerial number that uniquely identifies the MFA device.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type AuthenticationCode1: string
    :param AuthenticationCode1: [REQUIRED]\nAn authentication code emitted by the device.\nThe format for this parameter is a sequence of six digits.\n

    :type AuthenticationCode2: string
    :param AuthenticationCode2: [REQUIRED]\nA subsequent authentication code emitted by the device.\nThe format for this parameter is a sequence of six digits.\n

    :returns: 
    IAM.Client.exceptions.InvalidAuthenticationCodeException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def set_default_policy_version(PolicyArn=None, VersionId=None):
    """
    Sets the specified version of the specified policy as the policy\'s default (operative) version.
    This operation affects all users, groups, and roles that the policy is attached to. To list the users, groups, and roles that the policy is attached to, use the  ListEntitiesForPolicy API.
    For information about managed policies, see Managed Policies and Inline Policies in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_default_policy_version(
        PolicyArn='string',
        VersionId='string'
    )
    
    
    :type PolicyArn: string
    :param PolicyArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM policy whose default version you want to set.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :type VersionId: string
    :param VersionId: [REQUIRED]\nThe version of the policy to set as the default (operative) version.\nFor more information about managed policy versions, see Versioning for Managed Policies in the IAM User Guide .\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def set_security_token_service_preferences(GlobalEndpointTokenVersion=None):
    """
    Sets the specified version of the global endpoint token as the token version used for the AWS account.
    By default, AWS Security Token Service (STS) is available as a global service, and all STS requests go to a single endpoint at https://sts.amazonaws.com . AWS recommends using Regional STS endpoints to reduce latency, build in redundancy, and increase session token availability. For information about Regional endpoints for STS, see AWS Regions and Endpoints in the AWS General Reference .
    If you make an STS call to the global endpoint, the resulting session tokens might be valid in some Regions but not others. It depends on the version that is set in this operation. Version 1 tokens are valid only in AWS Regions that are available by default. These tokens do not work in manually enabled Regions, such as Asia Pacific (Hong Kong). Version 2 tokens are valid in all Regions. However, version 2 tokens are longer and might affect systems where you temporarily store tokens. For information, see Activating and Deactivating STS in an AWS Region in the IAM User Guide .
    To view the current session token version, see the GlobalEndpointTokenVersion entry in the response of the  GetAccountSummary operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_security_token_service_preferences(
        GlobalEndpointTokenVersion='v1Token'|'v2Token'
    )
    
    
    :type GlobalEndpointTokenVersion: string
    :param GlobalEndpointTokenVersion: [REQUIRED]\nThe version of the global endpoint token. Version 1 tokens are valid only in AWS Regions that are available by default. These tokens do not work in manually enabled Regions, such as Asia Pacific (Hong Kong). Version 2 tokens are valid in all Regions. However, version 2 tokens are longer and might affect systems where you temporarily store tokens.\nFor information, see Activating and Deactivating STS in an AWS Region in the IAM User Guide .\n

    """
    pass

def simulate_custom_policy(PolicyInputList=None, PermissionsBoundaryPolicyInputList=None, ActionNames=None, ResourceArns=None, ResourcePolicy=None, ResourceOwner=None, CallerArn=None, ContextEntries=None, ResourceHandlingOption=None, MaxItems=None, Marker=None):
    """
    Simulate how a set of IAM policies and optionally a resource-based policy works with a list of API operations and AWS resources to determine the policies\' effective permissions. The policies are provided as strings.
    The simulation does not perform the API operations; it only checks the authorization to determine if the simulated policies allow or deny the operations.
    If you want to simulate existing policies that are attached to an IAM user, group, or role, use  SimulatePrincipalPolicy instead.
    Context keys are variables that are maintained by AWS and its services and which provide details about the context of an API query request. You can use the Condition element of an IAM policy to evaluate context keys. To get the list of context keys that the policies require for correct simulation, use  GetContextKeysForCustomPolicy .
    If the output is long, you can use MaxItems and Marker parameters to paginate the results.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.simulate_custom_policy(
        PolicyInputList=[
            'string',
        ],
        PermissionsBoundaryPolicyInputList=[
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
    :param PolicyInputList: [REQUIRED]\nA list of policy documents to include in the simulation. Each document is specified as a string containing the complete, valid JSON text of an IAM policy. Do not include any resource-based policies in this parameter. Any resource-based policy must be submitted with the ResourcePolicy parameter. The policies cannot be 'scope-down' policies, such as you could include in a call to GetFederationToken or one of the AssumeRole API operations. In other words, do not use policies designed to restrict what a user can do while using the temporary credentials.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n\n(string) --\n\n

    :type PermissionsBoundaryPolicyInputList: list
    :param PermissionsBoundaryPolicyInputList: The IAM permissions boundary policy to simulate. The permissions boundary sets the maximum permissions that an IAM entity can have. You can input only one permissions boundary when you pass a policy to this operation. For more information about permissions boundaries, see Permissions Boundaries for IAM Entities in the IAM User Guide . The policy input is specified as a string that contains the complete, valid JSON text of a permissions boundary policy.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n\n(string) --\n\n

    :type ActionNames: list
    :param ActionNames: [REQUIRED]\nA list of names of API operations to evaluate in the simulation. Each operation is evaluated against each resource. Each operation must include the service identifier, such as iam:CreateUser . This operation does not support using wildcards (*) in an action name.\n\n(string) --\n\n

    :type ResourceArns: list
    :param ResourceArns: A list of ARNs of AWS resources to include in the simulation. If this parameter is not provided, then the value defaults to * (all resources). Each API in the ActionNames parameter is evaluated for each resource in this list. The simulation determines the access result (allowed or denied) of each combination and reports it in the response.\nThe simulation does not automatically retrieve policies for the specified resources. If you want to include a resource policy in the simulation, then you must include the policy as a string in the ResourcePolicy parameter.\nIf you include a ResourcePolicy , then it must be applicable to all of the resources included in the simulation or you receive an invalid input error.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n\n(string) --\n\n

    :type ResourcePolicy: string
    :param ResourcePolicy: A resource-based policy to include in the simulation provided as a string. Each resource in the simulation is treated as if it had this policy attached. You can include only one resource-based policy in a simulation.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n

    :type ResourceOwner: string
    :param ResourceOwner: An ARN representing the AWS account ID that specifies the owner of any simulated resource that does not identify its owner in the resource ARN. Examples of resource ARNs include an S3 bucket or object. If ResourceOwner is specified, it is also used as the account owner of any ResourcePolicy included in the simulation. If the ResourceOwner parameter is not specified, then the owner of the resources and the resource policy defaults to the account of the identity provided in CallerArn . This parameter is required only if you specify a resource-based policy and account that owns the resource is different from the account that owns the simulated calling user CallerArn .\nThe ARN for an account uses the following syntax: arn:aws:iam::*AWS-account-ID* :root . For example, to represent the account with the 112233445566 ID, use the following ARN: arn:aws:iam::112233445566-ID:root .\n

    :type CallerArn: string
    :param CallerArn: The ARN of the IAM user that you want to use as the simulated caller of the API operations. CallerArn is required if you include a ResourcePolicy so that the policy\'s Principal element has a value to use in evaluating the policy.\nYou can specify only the ARN of an IAM user. You cannot specify the ARN of an assumed role, federated user, or a service principal.\n

    :type ContextEntries: list
    :param ContextEntries: A list of context keys and corresponding values for the simulation to use. Whenever a context key is evaluated in one of the simulated IAM permissions policies, the corresponding value is supplied.\n\n(dict) --Contains information about a condition context key. It includes the name of the key and specifies the value (or values, if the context key supports multiple values) to use in the simulation. This information is used when evaluating the Condition elements of the input policies.\nThis data type is used as an input parameter to SimulateCustomPolicy and SimulatePrincipalPolicy .\n\nContextKeyName (string) --The full name of a condition context key, including the service prefix. For example, aws:SourceIp or s3:VersionId .\n\nContextKeyValues (list) --The value (or values, if the condition context key supports multiple values) to provide to the simulation when the key is referenced by a Condition element in an input policy.\n\n(string) --\n\n\nContextKeyType (string) --The data type of the value (or values) specified in the ContextKeyValues parameter.\n\n\n\n\n

    :type ResourceHandlingOption: string
    :param ResourceHandlingOption: Specifies the type of simulation to run. Different API operations that support resource-based policies require different combinations of resources. By specifying the type of simulation to run, you enable the policy simulator to enforce the presence of the required resources to ensure reliable simulation results. If your simulation does not match one of the following scenarios, then you can omit this parameter. The following list shows each of the supported scenario values and the resources that you must define to run the simulation.\nEach of the EC2 scenarios requires that you specify instance, image, and security-group resources. If your scenario includes an EBS volume, then you must specify that volume as a resource. If the EC2 scenario includes VPC, then you must supply the network-interface resource. If it includes an IP subnet, then you must specify the subnet resource. For more information on the EC2 scenario options, see Supported Platforms in the Amazon EC2 User Guide .\n\nEC2-Classic-InstanceStore  instance, image, security-group\nEC2-Classic-EBS  instance, image, security-group, volume\nEC2-VPC-InstanceStore  instance, image, security-group, network-interface\nEC2-VPC-InstanceStore-Subnet  instance, image, security-group, network-interface, subnet\nEC2-VPC-EBS  instance, image, security-group, network-interface, volume\nEC2-VPC-EBS-Subnet  instance, image, security-group, network-interface, subnet, volume\n\n

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'PermissionsBoundaryDecisionDetail': {
                'AllowedByPermissionsBoundary': True|False
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
                    },
                    'PermissionsBoundaryDecisionDetail': {
                        'AllowedByPermissionsBoundary': True|False
                    }
                },
            ]
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  SimulatePrincipalPolicy or  SimulateCustomPolicy request.

EvaluationResults (list) --
The results of the simulation.

(dict) --
Contains the results of a simulation.
This data type is used by the return parameter of ``  SimulateCustomPolicy `` and ``  SimulatePrincipalPolicy `` .

EvalActionName (string) --
The name of the API operation tested on the indicated resource.

EvalResourceName (string) --
The ARN of the resource that the indicated API operation was tested on.

EvalDecision (string) --
The result of the simulation.

MatchedStatements (list) --
A list of the statements in the input policies that determine the result for this scenario. Remember that even if multiple statements allow the operation on the resource, if only one statement denies that operation, then the explicit deny overrides any allow. In addition, the deny statement is the only entry included in the result.

(dict) --
Contains a reference to a Statement element in a policy document that determines the result of the simulation.
This data type is used by the MatchedStatements member of the ``  EvaluationResult `` type.

SourcePolicyId (string) --
The identifier of the policy that was provided as an input.

SourcePolicyType (string) --
The type of the policy.

StartPosition (dict) --
The row and column of the beginning of the Statement in an IAM policy.

Line (integer) --
The line containing the specified position in the document.

Column (integer) --
The column in the line containing the specified position in the document.



EndPosition (dict) --
The row and column of the end of a Statement in an IAM policy.

Line (integer) --
The line containing the specified position in the document.

Column (integer) --
The column in the line containing the specified position in the document.







MissingContextValues (list) --
A list of context keys that are required by the included input policies but that were not provided by one of the input parameters. This list is used when the resource in a simulation is "*", either explicitly, or when the ResourceArns parameter blank. If you include a list of resources, then any missing context values are instead included under the ResourceSpecificResults section. To discover the context keys used by a set of policies, you can call  GetContextKeysForCustomPolicy or  GetContextKeysForPrincipalPolicy .

(string) --


OrganizationsDecisionDetail (dict) --
A structure that details how Organizations and its service control policies affect the results of the simulation. Only applies if the simulated user\'s account is part of an organization.

AllowedByOrganizations (boolean) --
Specifies whether the simulated operation is allowed by the Organizations service control policies that impact the simulated user\'s account.



PermissionsBoundaryDecisionDetail (dict) --
Contains information about the effect that a permissions boundary has on a policy simulation when the boundary is applied to an IAM entity.

AllowedByPermissionsBoundary (boolean) --
Specifies whether an action is allowed by a permissions boundary that is applied to an IAM entity (user or role). A value of true means that the permissions boundary does not deny the action. This means that the policy includes an Allow statement that matches the request. In this case, if an identity-based policy also allows the action, the request is allowed. A value of false means that either the requested action is not allowed (implicitly denied) or that the action is explicitly denied by the permissions boundary. In both of these cases, the action is not allowed, regardless of the identity-based policy.



EvalDecisionDetails (dict) --
Additional details about the results of the cross-account evaluation decision. This parameter is populated for only cross-account simulations. It contains a brief summary of how each policy type contributes to the final evaluation decision.
If the simulation evaluates policies within the same account and includes a resource ARN, then the parameter is present but the response is empty. If the simulation evaluates policies within the same account and specifies all resources (* ), then the parameter is not returned.
When you make a cross-account request, AWS evaluates the request in the trusting account and the trusted account. The request is allowed only if both evaluations return true . For more information about how policies are evaluated, see Evaluating Policies Within a Single Account .
If an AWS Organizations SCP included in the evaluation denies access, the simulation ends. In this case, policy evaluation does not proceed any further and this parameter is not returned.

(string) --
(string) --




ResourceSpecificResults (list) --
The individual results of the simulation of the API operation specified in EvalActionName on each resource.

(dict) --
Contains the result of the simulation of a single API operation call on a single resource.
This data type is used by a member of the  EvaluationResult data type.

EvalResourceName (string) --
The name of the simulated resource, in Amazon Resource Name (ARN) format.

EvalResourceDecision (string) --
The result of the simulation of the simulated API operation on the resource specified in EvalResourceName .

MatchedStatements (list) --
A list of the statements in the input policies that determine the result for this part of the simulation. Remember that even if multiple statements allow the operation on the resource, if any statement denies that operation, then the explicit deny overrides any allow. In addition, the deny statement is the only entry included in the result.

(dict) --
Contains a reference to a Statement element in a policy document that determines the result of the simulation.
This data type is used by the MatchedStatements member of the ``  EvaluationResult `` type.

SourcePolicyId (string) --
The identifier of the policy that was provided as an input.

SourcePolicyType (string) --
The type of the policy.

StartPosition (dict) --
The row and column of the beginning of the Statement in an IAM policy.

Line (integer) --
The line containing the specified position in the document.

Column (integer) --
The column in the line containing the specified position in the document.



EndPosition (dict) --
The row and column of the end of a Statement in an IAM policy.

Line (integer) --
The line containing the specified position in the document.

Column (integer) --
The column in the line containing the specified position in the document.







MissingContextValues (list) --
A list of context keys that are required by the included input policies but that were not provided by one of the input parameters. This list is used when a list of ARNs is included in the ResourceArns parameter instead of "*". If you do not specify individual resources, by setting ResourceArns to "*" or by not including the ResourceArns parameter, then any missing context values are instead included under the EvaluationResults section. To discover the context keys used by a set of policies, you can call  GetContextKeysForCustomPolicy or  GetContextKeysForPrincipalPolicy .

(string) --


EvalDecisionDetails (dict) --
Additional details about the results of the evaluation decision on a single resource. This parameter is returned only for cross-account simulations. This parameter explains how each policy type contributes to the resource-specific evaluation decision.

(string) --
(string) --




PermissionsBoundaryDecisionDetail (dict) --
Contains information about the effect that a permissions boundary has on a policy simulation when that boundary is applied to an IAM entity.

AllowedByPermissionsBoundary (boolean) --
Specifies whether an action is allowed by a permissions boundary that is applied to an IAM entity (user or role). A value of true means that the permissions boundary does not deny the action. This means that the policy includes an Allow statement that matches the request. In this case, if an identity-based policy also allows the action, the request is allowed. A value of false means that either the requested action is not allowed (implicitly denied) or that the action is explicitly denied by the permissions boundary. In both of these cases, the action is not allowed, regardless of the identity-based policy.











IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.PolicyEvaluationException


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
                'PermissionsBoundaryDecisionDetail': {
                    'AllowedByPermissionsBoundary': True|False
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
                        },
                        'PermissionsBoundaryDecisionDetail': {
                            'AllowedByPermissionsBoundary': True|False
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

def simulate_principal_policy(PolicySourceArn=None, PolicyInputList=None, PermissionsBoundaryPolicyInputList=None, ActionNames=None, ResourceArns=None, ResourcePolicy=None, ResourceOwner=None, CallerArn=None, ContextEntries=None, ResourceHandlingOption=None, MaxItems=None, Marker=None):
    """
    Simulate how a set of IAM policies attached to an IAM entity works with a list of API operations and AWS resources to determine the policies\' effective permissions. The entity can be an IAM user, group, or role. If you specify a user, then the simulation also includes all of the policies that are attached to groups that the user belongs to.
    You can optionally include a list of one or more additional policies specified as strings to include in the simulation. If you want to simulate only policies specified as strings, use  SimulateCustomPolicy instead.
    You can also optionally include one resource-based policy to be evaluated with each of the resources included in the simulation.
    The simulation does not perform the API operations; it only checks the authorization to determine if the simulated policies allow or deny the operations.
    Context keys are variables maintained by AWS and its services that provide details about the context of an API query request. You can use the Condition element of an IAM policy to evaluate context keys. To get the list of context keys that the policies require for correct simulation, use  GetContextKeysForPrincipalPolicy .
    If the output is long, you can use the MaxItems and Marker parameters to paginate the results.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.simulate_principal_policy(
        PolicySourceArn='string',
        PolicyInputList=[
            'string',
        ],
        PermissionsBoundaryPolicyInputList=[
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
    :param PolicySourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of a user, group, or role whose policies you want to include in the simulation. If you specify a user, group, or role, the simulation includes all policies that are associated with that entity. If you specify a user, the simulation also includes all policies that are attached to any groups the user belongs to.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :type PolicyInputList: list
    :param PolicyInputList: An optional list of additional policy documents to include in the simulation. Each document is specified as a string containing the complete, valid JSON text of an IAM policy.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n\n(string) --\n\n

    :type PermissionsBoundaryPolicyInputList: list
    :param PermissionsBoundaryPolicyInputList: The IAM permissions boundary policy to simulate. The permissions boundary sets the maximum permissions that the entity can have. You can input only one permissions boundary when you pass a policy to this operation. An IAM entity can only have one permissions boundary in effect at a time. For example, if a permissions boundary is attached to an entity and you pass in a different permissions boundary policy using this parameter, then the new permission boundary policy is used for the simulation. For more information about permissions boundaries, see Permissions Boundaries for IAM Entities in the IAM User Guide . The policy input is specified as a string containing the complete, valid JSON text of a permissions boundary policy.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n\n(string) --\n\n

    :type ActionNames: list
    :param ActionNames: [REQUIRED]\nA list of names of API operations to evaluate in the simulation. Each operation is evaluated for each resource. Each operation must include the service identifier, such as iam:CreateUser .\n\n(string) --\n\n

    :type ResourceArns: list
    :param ResourceArns: A list of ARNs of AWS resources to include in the simulation. If this parameter is not provided, then the value defaults to * (all resources). Each API in the ActionNames parameter is evaluated for each resource in this list. The simulation determines the access result (allowed or denied) of each combination and reports it in the response.\nThe simulation does not automatically retrieve policies for the specified resources. If you want to include a resource policy in the simulation, then you must include the policy as a string in the ResourcePolicy parameter.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n\n(string) --\n\n

    :type ResourcePolicy: string
    :param ResourcePolicy: A resource-based policy to include in the simulation provided as a string. Each resource in the simulation is treated as if it had this policy attached. You can include only one resource-based policy in a simulation.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n

    :type ResourceOwner: string
    :param ResourceOwner: An AWS account ID that specifies the owner of any simulated resource that does not identify its owner in the resource ARN. Examples of resource ARNs include an S3 bucket or object. If ResourceOwner is specified, it is also used as the account owner of any ResourcePolicy included in the simulation. If the ResourceOwner parameter is not specified, then the owner of the resources and the resource policy defaults to the account of the identity provided in CallerArn . This parameter is required only if you specify a resource-based policy and account that owns the resource is different from the account that owns the simulated calling user CallerArn .

    :type CallerArn: string
    :param CallerArn: The ARN of the IAM user that you want to specify as the simulated caller of the API operations. If you do not specify a CallerArn , it defaults to the ARN of the user that you specify in PolicySourceArn , if you specified a user. If you include both a PolicySourceArn (for example, arn:aws:iam::123456789012:user/David ) and a CallerArn (for example, arn:aws:iam::123456789012:user/Bob ), the result is that you simulate calling the API operations as Bob, as if Bob had David\'s policies.\nYou can specify only the ARN of an IAM user. You cannot specify the ARN of an assumed role, federated user, or a service principal.\n\nCallerArn is required if you include a ResourcePolicy and the PolicySourceArn is not the ARN for an IAM user. This is required so that the resource-based policy\'s Principal element has a value to use in evaluating the policy.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :type ContextEntries: list
    :param ContextEntries: A list of context keys and corresponding values for the simulation to use. Whenever a context key is evaluated in one of the simulated IAM permissions policies, the corresponding value is supplied.\n\n(dict) --Contains information about a condition context key. It includes the name of the key and specifies the value (or values, if the context key supports multiple values) to use in the simulation. This information is used when evaluating the Condition elements of the input policies.\nThis data type is used as an input parameter to SimulateCustomPolicy and SimulatePrincipalPolicy .\n\nContextKeyName (string) --The full name of a condition context key, including the service prefix. For example, aws:SourceIp or s3:VersionId .\n\nContextKeyValues (list) --The value (or values, if the condition context key supports multiple values) to provide to the simulation when the key is referenced by a Condition element in an input policy.\n\n(string) --\n\n\nContextKeyType (string) --The data type of the value (or values) specified in the ContextKeyValues parameter.\n\n\n\n\n

    :type ResourceHandlingOption: string
    :param ResourceHandlingOption: Specifies the type of simulation to run. Different API operations that support resource-based policies require different combinations of resources. By specifying the type of simulation to run, you enable the policy simulator to enforce the presence of the required resources to ensure reliable simulation results. If your simulation does not match one of the following scenarios, then you can omit this parameter. The following list shows each of the supported scenario values and the resources that you must define to run the simulation.\nEach of the EC2 scenarios requires that you specify instance, image, and security group resources. If your scenario includes an EBS volume, then you must specify that volume as a resource. If the EC2 scenario includes VPC, then you must supply the network interface resource. If it includes an IP subnet, then you must specify the subnet resource. For more information on the EC2 scenario options, see Supported Platforms in the Amazon EC2 User Guide .\n\nEC2-Classic-InstanceStore  instance, image, security group\nEC2-Classic-EBS  instance, image, security group, volume\nEC2-VPC-InstanceStore  instance, image, security group, network interface\nEC2-VPC-InstanceStore-Subnet  instance, image, security group, network interface, subnet\nEC2-VPC-EBS  instance, image, security group, network interface, volume\nEC2-VPC-EBS-Subnet  instance, image, security group, network interface, subnet, volume\n\n

    :type MaxItems: integer
    :param MaxItems: Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true .\nIf you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the IsTruncated response element returns true , and Marker contains a value to include in the subsequent call that tells the service where to continue from.\n

    :type Marker: string
    :param Marker: Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you received to indicate where the next call should start.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'PermissionsBoundaryDecisionDetail': {
                'AllowedByPermissionsBoundary': True|False
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
                    },
                    'PermissionsBoundaryDecisionDetail': {
                        'AllowedByPermissionsBoundary': True|False
                    }
                },
            ]
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  SimulatePrincipalPolicy or  SimulateCustomPolicy request.

EvaluationResults (list) --
The results of the simulation.

(dict) --
Contains the results of a simulation.
This data type is used by the return parameter of ``  SimulateCustomPolicy `` and ``  SimulatePrincipalPolicy `` .

EvalActionName (string) --
The name of the API operation tested on the indicated resource.

EvalResourceName (string) --
The ARN of the resource that the indicated API operation was tested on.

EvalDecision (string) --
The result of the simulation.

MatchedStatements (list) --
A list of the statements in the input policies that determine the result for this scenario. Remember that even if multiple statements allow the operation on the resource, if only one statement denies that operation, then the explicit deny overrides any allow. In addition, the deny statement is the only entry included in the result.

(dict) --
Contains a reference to a Statement element in a policy document that determines the result of the simulation.
This data type is used by the MatchedStatements member of the ``  EvaluationResult `` type.

SourcePolicyId (string) --
The identifier of the policy that was provided as an input.

SourcePolicyType (string) --
The type of the policy.

StartPosition (dict) --
The row and column of the beginning of the Statement in an IAM policy.

Line (integer) --
The line containing the specified position in the document.

Column (integer) --
The column in the line containing the specified position in the document.



EndPosition (dict) --
The row and column of the end of a Statement in an IAM policy.

Line (integer) --
The line containing the specified position in the document.

Column (integer) --
The column in the line containing the specified position in the document.







MissingContextValues (list) --
A list of context keys that are required by the included input policies but that were not provided by one of the input parameters. This list is used when the resource in a simulation is "*", either explicitly, or when the ResourceArns parameter blank. If you include a list of resources, then any missing context values are instead included under the ResourceSpecificResults section. To discover the context keys used by a set of policies, you can call  GetContextKeysForCustomPolicy or  GetContextKeysForPrincipalPolicy .

(string) --


OrganizationsDecisionDetail (dict) --
A structure that details how Organizations and its service control policies affect the results of the simulation. Only applies if the simulated user\'s account is part of an organization.

AllowedByOrganizations (boolean) --
Specifies whether the simulated operation is allowed by the Organizations service control policies that impact the simulated user\'s account.



PermissionsBoundaryDecisionDetail (dict) --
Contains information about the effect that a permissions boundary has on a policy simulation when the boundary is applied to an IAM entity.

AllowedByPermissionsBoundary (boolean) --
Specifies whether an action is allowed by a permissions boundary that is applied to an IAM entity (user or role). A value of true means that the permissions boundary does not deny the action. This means that the policy includes an Allow statement that matches the request. In this case, if an identity-based policy also allows the action, the request is allowed. A value of false means that either the requested action is not allowed (implicitly denied) or that the action is explicitly denied by the permissions boundary. In both of these cases, the action is not allowed, regardless of the identity-based policy.



EvalDecisionDetails (dict) --
Additional details about the results of the cross-account evaluation decision. This parameter is populated for only cross-account simulations. It contains a brief summary of how each policy type contributes to the final evaluation decision.
If the simulation evaluates policies within the same account and includes a resource ARN, then the parameter is present but the response is empty. If the simulation evaluates policies within the same account and specifies all resources (* ), then the parameter is not returned.
When you make a cross-account request, AWS evaluates the request in the trusting account and the trusted account. The request is allowed only if both evaluations return true . For more information about how policies are evaluated, see Evaluating Policies Within a Single Account .
If an AWS Organizations SCP included in the evaluation denies access, the simulation ends. In this case, policy evaluation does not proceed any further and this parameter is not returned.

(string) --
(string) --




ResourceSpecificResults (list) --
The individual results of the simulation of the API operation specified in EvalActionName on each resource.

(dict) --
Contains the result of the simulation of a single API operation call on a single resource.
This data type is used by a member of the  EvaluationResult data type.

EvalResourceName (string) --
The name of the simulated resource, in Amazon Resource Name (ARN) format.

EvalResourceDecision (string) --
The result of the simulation of the simulated API operation on the resource specified in EvalResourceName .

MatchedStatements (list) --
A list of the statements in the input policies that determine the result for this part of the simulation. Remember that even if multiple statements allow the operation on the resource, if any statement denies that operation, then the explicit deny overrides any allow. In addition, the deny statement is the only entry included in the result.

(dict) --
Contains a reference to a Statement element in a policy document that determines the result of the simulation.
This data type is used by the MatchedStatements member of the ``  EvaluationResult `` type.

SourcePolicyId (string) --
The identifier of the policy that was provided as an input.

SourcePolicyType (string) --
The type of the policy.

StartPosition (dict) --
The row and column of the beginning of the Statement in an IAM policy.

Line (integer) --
The line containing the specified position in the document.

Column (integer) --
The column in the line containing the specified position in the document.



EndPosition (dict) --
The row and column of the end of a Statement in an IAM policy.

Line (integer) --
The line containing the specified position in the document.

Column (integer) --
The column in the line containing the specified position in the document.







MissingContextValues (list) --
A list of context keys that are required by the included input policies but that were not provided by one of the input parameters. This list is used when a list of ARNs is included in the ResourceArns parameter instead of "*". If you do not specify individual resources, by setting ResourceArns to "*" or by not including the ResourceArns parameter, then any missing context values are instead included under the EvaluationResults section. To discover the context keys used by a set of policies, you can call  GetContextKeysForCustomPolicy or  GetContextKeysForPrincipalPolicy .

(string) --


EvalDecisionDetails (dict) --
Additional details about the results of the evaluation decision on a single resource. This parameter is returned only for cross-account simulations. This parameter explains how each policy type contributes to the resource-specific evaluation decision.

(string) --
(string) --




PermissionsBoundaryDecisionDetail (dict) --
Contains information about the effect that a permissions boundary has on a policy simulation when that boundary is applied to an IAM entity.

AllowedByPermissionsBoundary (boolean) --
Specifies whether an action is allowed by a permissions boundary that is applied to an IAM entity (user or role). A value of true means that the permissions boundary does not deny the action. This means that the policy includes an Allow statement that matches the request. In this case, if an identity-based policy also allows the action, the request is allowed. A value of false means that either the requested action is not allowed (implicitly denied) or that the action is explicitly denied by the permissions boundary. In both of these cases, the action is not allowed, regardless of the identity-based policy.











IsTruncated (boolean) --
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. Note that IAM might return fewer than the MaxItems number of results even when there are more results available. We recommend that you check IsTruncated after every call to ensure that you receive all your results.

Marker (string) --
When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.PolicyEvaluationException


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
                'PermissionsBoundaryDecisionDetail': {
                    'AllowedByPermissionsBoundary': True|False
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
                        },
                        'PermissionsBoundaryDecisionDetail': {
                            'AllowedByPermissionsBoundary': True|False
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

def tag_role(RoleName=None, Tags=None):
    """
    Adds one or more tags to an IAM role. The role can be a regular role or a service-linked role. If a tag with the same key name already exists, then that tag is overwritten with the new value.
    A tag consists of a key name and an associated value. By assigning tags to your resources, you can do the following:
    For more information about tagging, see Tagging IAM Identities in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_role(
        RoleName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the role that you want to add tags to.\nThis parameter accepts (through its regex pattern ) a string of characters that consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe list of tags that you want to attach to the role. Each tag consists of a key name and an associated value. You can specify this with a JSON string.\n\n(dict) --A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .\n\nKey (string) -- [REQUIRED]The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.\n\nValue (string) -- [REQUIRED]The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.\n\nNote\nAWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.\n\n\n\n\n\n

    :returns: 
    Make sure that you have no invalid tags and that you do not exceed the allowed number of tags per role. In either case, the entire request fails and no tags are added to the role.
    AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.
    
    """
    pass

def tag_user(UserName=None, Tags=None):
    """
    Adds one or more tags to an IAM user. If a tag with the same key name already exists, then that tag is overwritten with the new value.
    A tag consists of a key name and an associated value. By assigning tags to your resources, you can do the following:
    For more information about tagging, see Tagging IAM Identities in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_user(
        UserName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user that you want to add tags to.\nThis parameter accepts (through its regex pattern ) a string of characters that consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe list of tags that you want to attach to the user. Each tag consists of a key name and an associated value.\n\n(dict) --A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .\n\nKey (string) -- [REQUIRED]The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.\n\nValue (string) -- [REQUIRED]The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.\n\nNote\nAWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.\n\n\n\n\n\n

    :returns: 
    Make sure that you have no invalid tags and that you do not exceed the allowed number of tags per role. In either case, the entire request fails and no tags are added to the role.
    AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.
    
    """
    pass

def untag_role(RoleName=None, TagKeys=None):
    """
    Removes the specified tags from the role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_role(
        RoleName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the IAM role from which you want to remove tags.\nThis parameter accepts (through its regex pattern ) a string of characters that consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of key names as a simple array of strings. The tags with matching keys are removed from the specified role.\n\n(string) --\n\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ConcurrentModificationException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def untag_user(UserName=None, TagKeys=None):
    """
    Removes the specified tags from the user. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_user(
        UserName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the IAM user from which you want to remove tags.\nThis parameter accepts (through its regex pattern ) a string of characters that consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of key names as a simple array of strings. The tags with matching keys are removed from the specified user.\n\n(string) --\n\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ConcurrentModificationException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_access_key(UserName=None, AccessKeyId=None, Status=None):
    """
    Changes the status of the specified access key from Active to Inactive, or vice versa. This operation can be used to disable a user\'s key as part of a key rotation workflow.
    If the UserName is not specified, the user name is determined implicitly based on the AWS access key ID used to sign the request. This operation works for access keys under the AWS account. Consequently, you can use this operation to manage AWS account root user credentials even if the AWS account has no associated users.
    For information about rotating keys, see Managing Keys and Certificates in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command deactivates the specified access key (access key ID and secret access key) for the IAM user named Bob.
    Expected Output:
    
    :example: response = client.update_access_key(
        UserName='string',
        AccessKeyId='string',
        Status='Active'|'Inactive'
    )
    
    
    :type UserName: string
    :param UserName: The name of the user whose key you want to update.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type AccessKeyId: string
    :param AccessKeyId: [REQUIRED]\nThe access key ID of the secret access key you want to update.\nThis parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.\n

    :type Status: string
    :param Status: [REQUIRED]\nThe status you want to assign to the secret access key. Active means that the key can be used for API calls to AWS, while Inactive means that the key cannot be used.\n

    :return: response = client.update_access_key(
        AccessKeyId='AKIAIOSFODNN7EXAMPLE',
        Status='Inactive',
        UserName='Bob',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_account_password_policy(MinimumPasswordLength=None, RequireSymbols=None, RequireNumbers=None, RequireUppercaseCharacters=None, RequireLowercaseCharacters=None, AllowUsersToChangePassword=None, MaxPasswordAge=None, PasswordReusePrevention=None, HardExpiry=None):
    """
    Updates the password policy settings for the AWS account.
    For more information about using a password policy, see Managing an IAM Password Policy in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
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
    :param MinimumPasswordLength: The minimum number of characters allowed in an IAM user password.\nIf you do not specify a value for this parameter, then the operation uses the default value of 6 .\n

    :type RequireSymbols: boolean
    :param RequireSymbols: Specifies whether IAM user passwords must contain at least one of the following non-alphanumeric characters:\n! @ # $ % ^ & * ( ) _ + - = [ ] { } | \'\nIf you do not specify a value for this parameter, then the operation uses the default value of false . The result is that passwords do not require at least one symbol character.\n

    :type RequireNumbers: boolean
    :param RequireNumbers: Specifies whether IAM user passwords must contain at least one numeric character (0 to 9).\nIf you do not specify a value for this parameter, then the operation uses the default value of false . The result is that passwords do not require at least one numeric character.\n

    :type RequireUppercaseCharacters: boolean
    :param RequireUppercaseCharacters: Specifies whether IAM user passwords must contain at least one uppercase character from the ISO basic Latin alphabet (A to Z).\nIf you do not specify a value for this parameter, then the operation uses the default value of false . The result is that passwords do not require at least one uppercase character.\n

    :type RequireLowercaseCharacters: boolean
    :param RequireLowercaseCharacters: Specifies whether IAM user passwords must contain at least one lowercase character from the ISO basic Latin alphabet (a to z).\nIf you do not specify a value for this parameter, then the operation uses the default value of false . The result is that passwords do not require at least one lowercase character.\n

    :type AllowUsersToChangePassword: boolean
    :param AllowUsersToChangePassword: Allows all IAM users in your account to use the AWS Management Console to change their own passwords. For more information, see Letting IAM Users Change Their Own Passwords in the IAM User Guide .\nIf you do not specify a value for this parameter, then the operation uses the default value of false . The result is that IAM users in the account do not automatically have permissions to change their own password.\n

    :type MaxPasswordAge: integer
    :param MaxPasswordAge: The number of days that an IAM user password is valid.\nIf you do not specify a value for this parameter, then the operation uses the default value of 0 . The result is that IAM user passwords never expire.\n

    :type PasswordReusePrevention: integer
    :param PasswordReusePrevention: Specifies the number of previous passwords that IAM users are prevented from reusing.\nIf you do not specify a value for this parameter, then the operation uses the default value of 0 . The result is that IAM users are not prevented from reusing previous passwords.\n

    :type HardExpiry: boolean
    :param HardExpiry: Prevents IAM users from setting a new password after their password has expired. The IAM user cannot be accessed until an administrator resets the password.\nIf you do not specify a value for this parameter, then the operation uses the default value of false . The result is that IAM users can change their passwords after they expire and continue to sign in as the user.\n

    :return: response = client.update_account_password_policy(
        MinimumPasswordLength=8,
        RequireNumbers=True,
    )
    
    print(response)
    
    
    :returns: 
    MinimumPasswordLength (integer) -- The minimum number of characters allowed in an IAM user password.
    If you do not specify a value for this parameter, then the operation uses the default value of 6 .
    
    RequireSymbols (boolean) -- Specifies whether IAM user passwords must contain at least one of the following non-alphanumeric characters:
    ! @ # $ % ^ & * ( ) _ + - = [ ] { } | \'
    If you do not specify a value for this parameter, then the operation uses the default value of false . The result is that passwords do not require at least one symbol character.
    
    RequireNumbers (boolean) -- Specifies whether IAM user passwords must contain at least one numeric character (0 to 9).
    If you do not specify a value for this parameter, then the operation uses the default value of false . The result is that passwords do not require at least one numeric character.
    
    RequireUppercaseCharacters (boolean) -- Specifies whether IAM user passwords must contain at least one uppercase character from the ISO basic Latin alphabet (A to Z).
    If you do not specify a value for this parameter, then the operation uses the default value of false . The result is that passwords do not require at least one uppercase character.
    
    RequireLowercaseCharacters (boolean) -- Specifies whether IAM user passwords must contain at least one lowercase character from the ISO basic Latin alphabet (a to z).
    If you do not specify a value for this parameter, then the operation uses the default value of false . The result is that passwords do not require at least one lowercase character.
    
    AllowUsersToChangePassword (boolean) -- Allows all IAM users in your account to use the AWS Management Console to change their own passwords. For more information, see Letting IAM Users Change Their Own Passwords in the IAM User Guide .
    If you do not specify a value for this parameter, then the operation uses the default value of false . The result is that IAM users in the account do not automatically have permissions to change their own password.
    
    MaxPasswordAge (integer) -- The number of days that an IAM user password is valid.
    If you do not specify a value for this parameter, then the operation uses the default value of 0 . The result is that IAM user passwords never expire.
    
    PasswordReusePrevention (integer) -- Specifies the number of previous passwords that IAM users are prevented from reusing.
    If you do not specify a value for this parameter, then the operation uses the default value of 0 . The result is that IAM users are not prevented from reusing previous passwords.
    
    HardExpiry (boolean) -- Prevents IAM users from setting a new password after their password has expired. The IAM user cannot be accessed until an administrator resets the password.
    If you do not specify a value for this parameter, then the operation uses the default value of false . The result is that IAM users can change their passwords after they expire and continue to sign in as the user.
    
    
    """
    pass

def update_assume_role_policy(RoleName=None, PolicyDocument=None):
    """
    Updates the policy that grants an IAM entity permission to assume a role. This is typically referred to as the "role trust policy". For more information about roles, go to Using Roles to Delegate Permissions and Federate Identities .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command updates the role trust policy for the role named Test-Role:
    Expected Output:
    
    :example: response = client.update_assume_role_policy(
        RoleName='string',
        PolicyDocument='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the role to update with the new policy.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type PolicyDocument: string
    :param PolicyDocument: [REQUIRED]\nThe policy that grants an entity permission to assume the role.\nYou must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n

    :return: response = client.update_assume_role_policy(
        PolicyDocument='{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":["ec2.amazonaws.com"]},"Action":["sts:AssumeRole"]}]}',
        RoleName='S3AccessForEC2Instances',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.MalformedPolicyDocumentException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.UnmodifiableEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_group(GroupName=None, NewPath=None, NewGroupName=None):
    """
    Updates the name and/or the path of the specified IAM group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command changes the name of the IAM group Test to Test-1.
    Expected Output:
    
    :example: response = client.update_group(
        GroupName='string',
        NewPath='string',
        NewGroupName='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nName of the IAM group to update. If you\'re changing the name of the group, this is the original name.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type NewPath: string
    :param NewPath: New path for the IAM group. Only include this if changing the group\'s path.\nThis parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type NewGroupName: string
    :param NewGroupName: New name for the IAM group. Only include this if changing the group\'s name.\nIAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both 'MyResource' and 'myresource'.\n

    :return: response = client.update_group(
        GroupName='Test',
        NewGroupName='Test-1',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.EntityAlreadyExistsException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_login_profile(UserName=None, Password=None, PasswordResetRequired=None):
    """
    Changes the password for the specified IAM user.
    IAM users can change their own passwords by calling  ChangePassword . For more information about modifying passwords, see Managing Passwords in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command creates or changes the password for the IAM user named Bob.
    Expected Output:
    
    :example: response = client.update_login_profile(
        UserName='string',
        Password='string',
        PasswordResetRequired=True|False
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the user whose password you want to update.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type Password: string
    :param Password: The new password for the specified IAM user.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\nHowever, the format can be further restricted by the account administrator by setting a password policy on the AWS account. For more information, see UpdateAccountPasswordPolicy .\n

    :type PasswordResetRequired: boolean
    :param PasswordResetRequired: Allows this new password to be used only once by requiring the specified IAM user to set a new password on next sign-in.

    :return: response = client.update_login_profile(
        Password='SomeKindOfPassword123!@#',
        UserName='Bob',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.EntityTemporarilyUnmodifiableException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.PasswordPolicyViolationException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_open_id_connect_provider_thumbprint(OpenIDConnectProviderArn=None, ThumbprintList=None):
    """
    Replaces the existing list of server certificate thumbprints associated with an OpenID Connect (OIDC) provider resource object with a new list of thumbprints.
    The list that you pass with this operation completely replaces the existing list of thumbprints. (The lists are not merged.)
    Typically, you need to update a thumbprint only when the identity provider\'s certificate changes, which occurs rarely. However, if the provider\'s certificate does change, any attempt to assume an IAM role that specifies the OIDC provider as a principal fails until the certificate thumbprint is updated.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_open_id_connect_provider_thumbprint(
        OpenIDConnectProviderArn='string',
        ThumbprintList=[
            'string',
        ]
    )
    
    
    :type OpenIDConnectProviderArn: string
    :param OpenIDConnectProviderArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM OIDC provider resource object for which you want to update the thumbprint. You can get a list of OIDC provider ARNs by using the ListOpenIDConnectProviders operation.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :type ThumbprintList: list
    :param ThumbprintList: [REQUIRED]\nA list of certificate thumbprints that are associated with the specified IAM OpenID Connect provider. For more information, see CreateOpenIDConnectProvider .\n\n(string) --Contains a thumbprint for an identity provider\'s server certificate.\nThe identity provider\'s server certificate thumbprint is the hex-encoded SHA-1 hash value of the self-signed X.509 certificate. This thumbprint is used by the domain where the OpenID Connect provider makes its keys available. The thumbprint is always a 40-character string.\n\n\n

    :returns: 
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_role(RoleName=None, Description=None, MaxSessionDuration=None):
    """
    Updates the description or maximum session duration setting of a role.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_role(
        RoleName='string',
        Description='string',
        MaxSessionDuration=123
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the role that you want to modify.\n

    :type Description: string
    :param Description: The new description that you want to apply to the specified role.

    :type MaxSessionDuration: integer
    :param MaxSessionDuration: The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.\nAnyone who assumes the role from the AWS CLI or API can use the DurationSeconds API parameter or the duration-seconds CLI parameter to request a longer session. The MaxSessionDuration setting determines the maximum duration that can be requested using the DurationSeconds parameter. If users don\'t specify a value for the DurationSeconds parameter, their security credentials are valid for one hour by default. This applies when you use the AssumeRole* API operations or the assume-role* CLI operations but does not apply when you use those operations to create a console URL. For more information, see Using IAM Roles in the IAM User Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IAM.Client.exceptions.UnmodifiableEntityException
IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_role_description(RoleName=None, Description=None):
    """
    Use  UpdateRole instead.
    Modifies only the description of a role. This operation performs the same function as the Description parameter in the UpdateRole operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_role_description(
        RoleName='string',
        Description='string'
    )
    
    
    :type RoleName: string
    :param RoleName: [REQUIRED]\nThe name of the role that you want to modify.\n

    :type Description: string
    :param Description: [REQUIRED]\nThe new description that you want to apply to the specified role.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Role': {
        'Path': 'string',
        'RoleName': 'string',
        'RoleId': 'string',
        'Arn': 'string',
        'CreateDate': datetime(2015, 1, 1),
        'AssumeRolePolicyDocument': 'string',
        'Description': 'string',
        'MaxSessionDuration': 123,
        'PermissionsBoundary': {
            'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
            'PermissionsBoundaryArn': 'string'
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'RoleLastUsed': {
            'LastUsedDate': datetime(2015, 1, 1),
            'Region': 'string'
        }
    }
}


Response Structure

(dict) --

Role (dict) --
A structure that contains details about the modified role.

Path (string) --
The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide .

RoleName (string) --
The friendly name that identifies the role.

RoleId (string) --
The stable and unique string identifying the role. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide guide.

CreateDate (datetime) --
The date and time, in ISO 8601 date-time format , when the role was created.

AssumeRolePolicyDocument (string) --
The policy that grants an entity permission to assume the role.

Description (string) --
A description of the role that you provide.

MaxSessionDuration (integer) --
The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI, or API to assume the role can specify the duration using the optional DurationSeconds API parameter or duration-seconds CLI parameter.

PermissionsBoundary (dict) --
The ARN of the policy used to set the permissions boundary for the role.
For more information about permissions boundaries, see Permissions Boundaries for IAM Identities in the IAM User Guide .

PermissionsBoundaryType (string) --
The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of Policy .

PermissionsBoundaryArn (string) --
The ARN of the policy used to set the permissions boundary for the user or role.



Tags (list) --
A list of tags that are attached to the specified role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

(dict) --
A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .

Key (string) --
The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value (string) --
The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.






RoleLastUsed (dict) --
Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see Regions Where Data Is Tracked in the IAM User Guide .

LastUsedDate (datetime) --
The date and time, in ISO 8601 date-time format that the role was last used.
This field is null if the role has not been used within the IAM tracking period. For more information about the tracking period, see Regions Where Data Is Tracked in the IAM User Guide .

Region (string) --
The name of the AWS Region in which the role was last used.











Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.UnmodifiableEntityException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'Role': {
            'Path': 'string',
            'RoleName': 'string',
            'RoleId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'AssumeRolePolicyDocument': 'string',
            'Description': 'string',
            'MaxSessionDuration': 123,
            'PermissionsBoundary': {
                'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                'PermissionsBoundaryArn': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'RoleLastUsed': {
                'LastUsedDate': datetime(2015, 1, 1),
                'Region': 'string'
            }
        }
    }
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.UnmodifiableEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_saml_provider(SAMLMetadataDocument=None, SAMLProviderArn=None):
    """
    Updates the metadata document for an existing SAML provider resource object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_saml_provider(
        SAMLMetadataDocument='string',
        SAMLProviderArn='string'
    )
    
    
    :type SAMLMetadataDocument: string
    :param SAMLMetadataDocument: [REQUIRED]\nAn XML document generated by an identity provider (IdP) that supports SAML 2.0. The document includes the issuer\'s name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that are received from the IdP. You must generate the metadata document using the identity management software that is used as your organization\'s IdP.\n

    :type SAMLProviderArn: string
    :param SAMLProviderArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the SAML provider to update.\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SAMLProviderArn': 'string'
}


Response Structure

(dict) --
Contains the response to a successful  UpdateSAMLProvider request.

SAMLProviderArn (string) --
The Amazon Resource Name (ARN) of the SAML provider that was updated.







Exceptions

IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidInputException
IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.ServiceFailureException


    :return: {
        'SAMLProviderArn': 'string'
    }
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.InvalidInputException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_server_certificate(ServerCertificateName=None, NewPath=None, NewServerCertificateName=None):
    """
    Updates the name and/or the path of the specified server certificate stored in IAM.
    For more information about working with server certificates, see Working with Server Certificates in the IAM User Guide . This topic also includes a list of AWS services that can use the server certificates that you manage with IAM.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_server_certificate(
        ServerCertificateName='string',
        NewPath='string',
        NewServerCertificateName='string'
    )
    
    
    :type ServerCertificateName: string
    :param ServerCertificateName: [REQUIRED]\nThe name of the server certificate that you want to update.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type NewPath: string
    :param NewPath: The new path for the server certificate. Include this only if you are updating the server certificate\'s path.\nThis parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type NewServerCertificateName: string
    :param NewServerCertificateName: The new name for the server certificate. Include this only if you are updating the server certificate\'s name. The name of the certificate cannot contain any spaces.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.EntityAlreadyExistsException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_service_specific_credential(UserName=None, ServiceSpecificCredentialId=None, Status=None):
    """
    Sets the status of a service-specific credential to Active or Inactive . Service-specific credentials that are inactive cannot be used for authentication to the service. This operation can be used to disable a user\'s service-specific credential as part of a credential rotation work flow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_service_specific_credential(
        UserName='string',
        ServiceSpecificCredentialId='string',
        Status='Active'|'Inactive'
    )
    
    
    :type UserName: string
    :param UserName: The name of the IAM user associated with the service-specific credential. If you do not specify this value, then the operation assumes the user whose credentials are used to call the operation.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type ServiceSpecificCredentialId: string
    :param ServiceSpecificCredentialId: [REQUIRED]\nThe unique identifier of the service-specific credential.\nThis parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.\n

    :type Status: string
    :param Status: [REQUIRED]\nThe status to be assigned to the service-specific credential.\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    
    """
    pass

def update_signing_certificate(UserName=None, CertificateId=None, Status=None):
    """
    Changes the status of the specified user signing certificate from active to disabled, or vice versa. This operation can be used to disable an IAM user\'s signing certificate as part of a certificate rotation work flow.
    If the UserName field is not specified, the user name is determined implicitly based on the AWS access key ID used to sign the request. This operation works for access keys under the AWS account. Consequently, you can use this operation to manage AWS account root user credentials even if the AWS account has no associated users.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command changes the status of a signing certificate for a user named Bob to Inactive.
    Expected Output:
    
    :example: response = client.update_signing_certificate(
        UserName='string',
        CertificateId='string',
        Status='Active'|'Inactive'
    )
    
    
    :type UserName: string
    :param UserName: The name of the IAM user the signing certificate belongs to.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type CertificateId: string
    :param CertificateId: [REQUIRED]\nThe ID of the signing certificate you want to update.\nThis parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.\n

    :type Status: string
    :param Status: [REQUIRED]\nThe status you want to assign to the certificate. Active means that the certificate can be used for API calls to AWS Inactive means that the certificate cannot be used.\n

    :return: response = client.update_signing_certificate(
        CertificateId='TA7SMP42TDN5Z26OBPJE7EXAMPLE',
        Status='Inactive',
        UserName='Bob',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_ssh_public_key(UserName=None, SSHPublicKeyId=None, Status=None):
    """
    Sets the status of an IAM user\'s SSH public key to active or inactive. SSH public keys that are inactive cannot be used for authentication. This operation can be used to disable a user\'s SSH public key as part of a key rotation work flow.
    The SSH public key affected by this operation is used only for authenticating the associated IAM user to an AWS CodeCommit repository. For more information about using SSH keys to authenticate to an AWS CodeCommit repository, see Set up AWS CodeCommit for SSH Connections in the AWS CodeCommit User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_ssh_public_key(
        UserName='string',
        SSHPublicKeyId='string',
        Status='Active'|'Inactive'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the IAM user associated with the SSH public key.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type SSHPublicKeyId: string
    :param SSHPublicKeyId: [REQUIRED]\nThe unique identifier for the SSH public key.\nThis parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.\n

    :type Status: string
    :param Status: [REQUIRED]\nThe status to assign to the SSH public key. Active means that the key can be used for authentication with an AWS CodeCommit repository. Inactive means that the key cannot be used.\n

    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    
    """
    pass

def update_user(UserName=None, NewPath=None, NewUserName=None):
    """
    Updates the name and/or the path of the specified IAM user.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command changes the name of the IAM user Bob to Robert. It does not change the user\'s path.
    Expected Output:
    
    :example: response = client.update_user(
        UserName='string',
        NewPath='string',
        NewUserName='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nName of the user to update. If you\'re changing the name of the user, this is the original user name.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type NewPath: string
    :param NewPath: New path for the IAM user. Include this parameter only if you\'re changing the user\'s path.\nThis parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n

    :type NewUserName: string
    :param NewUserName: New name for the user. Include this parameter only if you\'re changing the user\'s name.\nIAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both 'MyResource' and 'myresource'.\n

    :return: response = client.update_user(
        NewUserName='Robert',
        UserName='Bob',
    )
    
    print(response)
    
    
    :returns: 
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.EntityAlreadyExistsException
    IAM.Client.exceptions.EntityTemporarilyUnmodifiableException
    IAM.Client.exceptions.ConcurrentModificationException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def upload_server_certificate(Path=None, ServerCertificateName=None, CertificateBody=None, PrivateKey=None, CertificateChain=None):
    """
    Uploads a server certificate entity for the AWS account. The server certificate entity includes a public key certificate, a private key, and an optional certificate chain, which should all be PEM-encoded.
    We recommend that you use AWS Certificate Manager to provision, manage, and deploy your server certificates. With ACM you can request a certificate, deploy it to AWS resources, and let ACM handle certificate renewals for you. Certificates provided by ACM are free. For more information about using ACM, see the AWS Certificate Manager User Guide .
    For more information about working with server certificates, see Working with Server Certificates in the IAM User Guide . This topic includes a list of AWS services that can use the server certificates that you manage with IAM.
    For information about the number of server certificates you can upload, see Limitations on IAM Entities and Objects in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
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
    :param Path: The path for the server certificate. For more information about paths, see IAM Identifiers in the IAM User Guide .\nThis parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its regex pattern ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021 ) through the DEL character (\\u007F ), including most punctuation characters, digits, and upper and lowercased letters.\n\nNote\nIf you are uploading a server certificate specifically for use with Amazon CloudFront distributions, you must specify a path using the path parameter. The path must begin with /cloudfront and must include a trailing slash (for example, /cloudfront/test/ ).\n\n

    :type ServerCertificateName: string
    :param ServerCertificateName: [REQUIRED]\nThe name for the server certificate. Do not include the path in this value. The name of the certificate cannot contain any spaces.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type CertificateBody: string
    :param CertificateBody: [REQUIRED]\nThe contents of the public key certificate in PEM-encoded format.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n

    :type PrivateKey: string
    :param PrivateKey: [REQUIRED]\nThe contents of the private key in PEM-encoded format.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n

    :type CertificateChain: string
    :param CertificateChain: The contents of the certificate chain. This is typically a concatenation of the PEM-encoded public key certificates of the chain.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ServerCertificateMetadata': {
        'Path': 'string',
        'ServerCertificateName': 'string',
        'ServerCertificateId': 'string',
        'Arn': 'string',
        'UploadDate': datetime(2015, 1, 1),
        'Expiration': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Contains the response to a successful  UploadServerCertificate request.

ServerCertificateMetadata (dict) --
The meta information of the uploaded server certificate without its certificate body, certificate chain, and private key.

Path (string) --
The path to the server certificate. For more information about paths, see IAM Identifiers in the IAM User Guide .

ServerCertificateName (string) --
The name that identifies the server certificate.

ServerCertificateId (string) --
The stable and unique string identifying the server certificate. For more information about IDs, see IAM Identifiers in the IAM User Guide .

Arn (string) --
The Amazon Resource Name (ARN) specifying the server certificate. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .

UploadDate (datetime) --
The date when the server certificate was uploaded.

Expiration (datetime) --
The date on which the certificate is set to expire.









Exceptions

IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.EntityAlreadyExistsException
IAM.Client.exceptions.MalformedCertificateException
IAM.Client.exceptions.KeyPairMismatchException
IAM.Client.exceptions.ServiceFailureException

Examples
The following upload-server-certificate command uploads a server certificate to your AWS account:
response = client.upload_server_certificate(
    CertificateBody='-----BEGIN CERTIFICATE-----<a very long certificate text string>-----END CERTIFICATE-----',
    Path='/company/servercerts/',
    PrivateKey='-----BEGIN DSA PRIVATE KEY-----<a very long private key string>-----END DSA PRIVATE KEY-----',
    ServerCertificateName='ProdServerCert',
)

print(response)


Expected Output:
{
    'ServerCertificateMetadata': {
        'Arn': 'arn:aws:iam::123456789012:server-certificate/company/servercerts/ProdServerCert',
        'Expiration': datetime(2012, 5, 8, 1, 2, 3, 1, 129, 0),
        'Path': '/company/servercerts/',
        'ServerCertificateId': 'ASCA1111111111EXAMPLE',
        'ServerCertificateName': 'ProdServerCert',
        'UploadDate': datetime(2010, 5, 8, 1, 2, 3, 5, 128, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    
    :returns: 
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.EntityAlreadyExistsException
    IAM.Client.exceptions.MalformedCertificateException
    IAM.Client.exceptions.KeyPairMismatchException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def upload_signing_certificate(UserName=None, CertificateBody=None):
    """
    Uploads an X.509 signing certificate and associates it with the specified IAM user. Some AWS services use X.509 signing certificates to validate requests that are signed with a corresponding private key. When you upload the certificate, its default status is Active .
    If the UserName is not specified, the IAM user name is determined implicitly based on the AWS access key ID used to sign the request. This operation works for access keys under the AWS account. Consequently, you can use this operation to manage AWS account root user credentials even if the AWS account has no associated users.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following command uploads a signing certificate for the IAM user named Bob.
    Expected Output:
    
    :example: response = client.upload_signing_certificate(
        UserName='string',
        CertificateBody='string'
    )
    
    
    :type UserName: string
    :param UserName: The name of the user the signing certificate is for.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type CertificateBody: string
    :param CertificateBody: [REQUIRED]\nThe contents of the signing certificate.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Certificate': {
        'UserName': 'string',
        'CertificateId': 'string',
        'CertificateBody': 'string',
        'Status': 'Active'|'Inactive',
        'UploadDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Contains the response to a successful  UploadSigningCertificate request.

Certificate (dict) --
Information about the certificate.

UserName (string) --
The name of the user the signing certificate is associated with.

CertificateId (string) --
The ID for the signing certificate.

CertificateBody (string) --
The contents of the signing certificate.

Status (string) --
The status of the signing certificate. Active means that the key is valid for API calls, while Inactive means it is not.

UploadDate (datetime) --
The date when the signing certificate was uploaded.









Exceptions

IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.EntityAlreadyExistsException
IAM.Client.exceptions.MalformedCertificateException
IAM.Client.exceptions.InvalidCertificateException
IAM.Client.exceptions.DuplicateCertificateException
IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.ServiceFailureException

Examples
The following command uploads a signing certificate for the IAM user named Bob.
response = client.upload_signing_certificate(
    CertificateBody='-----BEGIN CERTIFICATE-----<certificate-body>-----END CERTIFICATE-----',
    UserName='Bob',
)

print(response)


Expected Output:
{
    'Certificate': {
        'CertificateBody': '-----BEGIN CERTIFICATE-----<certificate-body>-----END CERTIFICATE-----',
        'CertificateId': 'ID123456789012345EXAMPLE',
        'Status': 'Active',
        'UploadDate': datetime(2015, 6, 6, 21, 40, 8, 5, 157, 0),
        'UserName': 'Bob',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Certificate': {
            'UserName': 'string',
            'CertificateId': 'string',
            'CertificateBody': 'string',
            'Status': 'Active'|'Inactive',
            'UploadDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.EntityAlreadyExistsException
    IAM.Client.exceptions.MalformedCertificateException
    IAM.Client.exceptions.InvalidCertificateException
    IAM.Client.exceptions.DuplicateCertificateException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.ServiceFailureException
    
    """
    pass

def upload_ssh_public_key(UserName=None, SSHPublicKeyBody=None):
    """
    Uploads an SSH public key and associates it with the specified IAM user.
    The SSH public key uploaded by this operation can be used only for authenticating the associated IAM user to an AWS CodeCommit repository. For more information about using SSH keys to authenticate to an AWS CodeCommit repository, see Set up AWS CodeCommit for SSH Connections in the AWS CodeCommit User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.upload_ssh_public_key(
        UserName='string',
        SSHPublicKeyBody='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe name of the IAM user to associate the SSH public key with.\nThis parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n

    :type SSHPublicKeyBody: string
    :param SSHPublicKeyBody: [REQUIRED]\nThe SSH public key. The public key must be encoded in ssh-rsa format or PEM format. The minimum bit-length of the public key is 2048 bits. For example, you can generate a 2048-bit key, and the resulting PEM file is 1679 bytes long.\nThe regex pattern used to validate this parameter is a string of characters consisting of the following:\n\nAny printable ASCII character ranging from the space character (\\u0020 ) through the end of the ASCII character range\nThe printable characters in the Basic Latin and Latin-1 Supplement character set (through \\u00FF )\nThe special characters tab (\\u0009 ), line feed (\\u000A ), and carriage return (\\u000D )\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SSHPublicKey': {
        'UserName': 'string',
        'SSHPublicKeyId': 'string',
        'Fingerprint': 'string',
        'SSHPublicKeyBody': 'string',
        'Status': 'Active'|'Inactive',
        'UploadDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Contains the response to a successful  UploadSSHPublicKey request.

SSHPublicKey (dict) --
Contains information about the SSH public key.

UserName (string) --
The name of the IAM user associated with the SSH public key.

SSHPublicKeyId (string) --
The unique identifier for the SSH public key.

Fingerprint (string) --
The MD5 message digest of the SSH public key.

SSHPublicKeyBody (string) --
The SSH public key.

Status (string) --
The status of the SSH public key. Active means that the key can be used for authentication with an AWS CodeCommit repository. Inactive means that the key cannot be used.

UploadDate (datetime) --
The date and time, in ISO 8601 date-time format , when the SSH public key was uploaded.









Exceptions

IAM.Client.exceptions.LimitExceededException
IAM.Client.exceptions.NoSuchEntityException
IAM.Client.exceptions.InvalidPublicKeyException
IAM.Client.exceptions.DuplicateSSHPublicKeyException
IAM.Client.exceptions.UnrecognizedPublicKeyEncodingException


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
    
    
    :returns: 
    IAM.Client.exceptions.LimitExceededException
    IAM.Client.exceptions.NoSuchEntityException
    IAM.Client.exceptions.InvalidPublicKeyException
    IAM.Client.exceptions.DuplicateSSHPublicKeyException
    IAM.Client.exceptions.UnrecognizedPublicKeyEncodingException
    
    """
    pass

