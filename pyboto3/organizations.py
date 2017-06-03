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

def accept_handshake(HandshakeId=None):
    """
    Sends a response to the originator of a handshake agreeing to the action proposed by the handshake request.
    This operation can be called only by the following principals when they also have the relevant IAM permissions:
    See also: AWS API Documentation
    
    
    :example: response = client.accept_handshake(
        HandshakeId='string'
    )
    
    
    :type HandshakeId: string
    :param HandshakeId: [REQUIRED]
            The unique identifier (ID) of the handshake that you want to accept.
            The regex pattern for handshake ID string requires 'h-' followed by from 8 to 32 lower-case letters or digits.
            

    :rtype: dict
    :return: {
        'Handshake': {
            'Id': 'string',
            'Arn': 'string',
            'Parties': [
                {
                    'Id': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                },
            ],
            'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
            'RequestedTimestamp': datetime(2015, 1, 1),
            'ExpirationTimestamp': datetime(2015, 1, 1),
            'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES',
            'Resources': [
                {
                    'Value': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                    'Resources': {'... recursive ...'}
                },
            ]
        }
    }
    
    
    :returns: 
    REQUESTED : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond.
    OPEN : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action.
    CANCELED : This handshake is no longer active because it was canceled by the originating account.
    ACCEPTED : This handshake is complete because it has been accepted by the recipient.
    DECLINED : This handshake is no longer active because it was declined by the recipient account.
    EXPIRED : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days).
    
    """
    pass

def attach_policy(PolicyId=None, TargetId=None):
    """
    Attaches a policy to a root, an organizational unit, or an individual account. How the policy affects accounts depends on the type of policy:
    SCPs essentially are permission "filters". When you attach one SCP to a higher level root or OU, and you also attach a different SCP to a child OU or to an account, the child policy can further restrict only the permissions that pass through the parent filter and are available to the child. An SCP that is attached to a child cannot grant a permission that is not already granted by the parent. For example, imagine that the parent SCP allows permissions A, B, C, D, and E. The child SCP allows C, D, E, F, and G. The result is that the accounts affected by the child SCP are allowed to use only C, D, and E. They cannot use A or B because they were filtered out by the child OU. They also cannot use F and G because they were filtered out by the parent OU. They cannot be granted back by the child SCP; child SCPs can only filter the permissions they receive from the parent SCP.
    AWS Organizations attaches a default SCP named "FullAWSAccess to every root, OU, and account. This default SCP allows all services and actions, enabling any new child OU or account to inherit the permissions of the parent root or OU. If you detach the default policy, you must replace it with a policy that specifies the permissions that you want to allow in that OU or account.
    For more information about how Organizations policies permissions work, see Using Service Control Policies in the AWS Organizations User Guide .
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.attach_policy(
        PolicyId='string',
        TargetId='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]
            The unique identifier (ID) of the policy that you want to attach to the target. You can get the ID for the policy by calling the ListPolicies operation.
            The regex pattern for a policy ID string requires 'p-' followed by from 8 to 128 lower-case letters or digits.
            

    :type TargetId: string
    :param TargetId: [REQUIRED]
            The unique identifier (ID) of the root, OU, or account that you want to attach the policy to. You can get the ID by calling the ListRoots , ListOrganizationalUnitsForParent , or ListAccounts operations.
            The regex pattern for a target ID string requires one of the following:
            Root: a string that begins with 'r-' followed by from 4 to 32 lower-case letters or digits.
            Account: a string that consists of exactly 12 digits.
            Organizational unit (OU): a string that begins with 'ou-' followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second '-' dash and from 8 to 32 additional lower-case letters or digits.
            

    :returns: 
    PolicyId (string) -- [REQUIRED]
    The unique identifier (ID) of the policy that you want to attach to the target. You can get the ID for the policy by calling the  ListPolicies operation.
    The regex pattern for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.
    
    TargetId (string) -- [REQUIRED]
    The unique identifier (ID) of the root, OU, or account that you want to attach the policy to. You can get the ID by calling the  ListRoots ,  ListOrganizationalUnitsForParent , or  ListAccounts operations.
    The regex pattern for a target ID string requires one of the following:
    
    Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.
    Account: a string that consists of exactly 12 digits.
    Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    
    
    
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

def cancel_handshake(HandshakeId=None):
    """
    Cancels a handshake. Canceling a handshake sets the handshake state to CANCELED .
    This operation can be called only from the account that originated the handshake. The recipient of the handshake can't cancel it, but can use  DeclineHandshake instead. After a handshake is canceled, the recipient can no longer respond to that handshake.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_handshake(
        HandshakeId='string'
    )
    
    
    :type HandshakeId: string
    :param HandshakeId: [REQUIRED]
            The unique identifier (ID) of the handshake that you want to cancel. You can get the ID from the ListHandshakesForOrganization operation.
            The regex pattern for handshake ID string requires 'h-' followed by from 8 to 32 lower-case letters or digits.
            

    :rtype: dict
    :return: {
        'Handshake': {
            'Id': 'string',
            'Arn': 'string',
            'Parties': [
                {
                    'Id': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                },
            ],
            'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
            'RequestedTimestamp': datetime(2015, 1, 1),
            'ExpirationTimestamp': datetime(2015, 1, 1),
            'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES',
            'Resources': [
                {
                    'Value': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                    'Resources': {'... recursive ...'}
                },
            ]
        }
    }
    
    
    :returns: 
    ACCOUNT - Specifies an AWS account ID number.
    ORGANIZATION - Specifies an organization ID number.
    EMAIL - Specifies the email address that is associated with the account that receives the handshake.
    OWNER_EMAIL - Specifies the email address associated with the master account. Included as information about an organization.
    OWNER_NAME - Specifies the name associated with the master account. Included as information about an organization.
    NOTES - Additional text provided by the handshake initiator and intended for the recipient to read.
    
    """
    pass

def create_account(Email=None, AccountName=None, RoleName=None, IamUserAccessToBilling=None):
    """
    Creates an AWS account that is automatically a member of the organization whose credentials made the request. This is an asynchronous request that AWS performs in the background. If you want to check the status of the request later, you need the OperationId response element from this operation to provide as a parameter to the  DescribeCreateAccountStatus operation.
    AWS Organizations preconfigures the new member account with a role (named OrganizationAccountAccessRole by default) that grants administrator permissions to the new account. Principals in the master account can assume the role. AWS Organizations clones the company name and address information for the new account from the organization's master account.
    For more information about creating accounts, see Creating an AWS Account in Your Organization in the AWS Organizations User Guide .
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.create_account(
        Email='string',
        AccountName='string',
        RoleName='string',
        IamUserAccessToBilling='ALLOW'|'DENY'
    )
    
    
    :type Email: string
    :param Email: [REQUIRED]
            The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.
            

    :type AccountName: string
    :param AccountName: [REQUIRED]
            The friendly name of the member account.
            

    :type RoleName: string
    :param RoleName: (Optional)
            The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account.
            If you do not specify this parameter, the role name defaults to OrganizationAccountAccessRole .
            For more information about how to use this role to access the member account, see Accessing and Administering the Member Accounts in Your Organization in the AWS Organizations User Guide , and steps 2 and 3 in Tutorial: Delegate Access Across AWS Accounts Using IAM Roles in the IAM User Guide .
            The regex pattern that is used to validate this parameter is a string of characters that can consist of uppercase letters, lowercase letters, digits with no spaces, and any of the following characters: =,.@-
            

    :type IamUserAccessToBilling: string
    :param IamUserAccessToBilling: If set to ALLOW , the new account enables IAM users to access account billing information if they have the required permissions. If set to DENY , then only the root user of the new account can access account billing information. For more information, see Activating Access to the Billing and Cost Management Console in the AWS Billing and Cost Management User Guide .
            If you do not specify this parameter, the value defaults to ALLOW, and IAM users and roles with the required permissions can access billing information for the new account.
            

    :rtype: dict
    :return: {
        'CreateAccountStatus': {
            'Id': 'string',
            'AccountName': 'string',
            'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
            'RequestedTimestamp': datetime(2015, 1, 1),
            'CompletedTimestamp': datetime(2015, 1, 1),
            'AccountId': 'string',
            'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'INTERNAL_FAILURE'
        }
    }
    
    
    :returns: 
    ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the limit on the number of accounts in your organization.
    EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with that email address already exists.
    INVALID_ADDRESS: The account could not be created because the address you provided is not valid.
    INVALID_EMAIL: The account could not be created because the email address you provided is not valid.
    INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Customer Support.
    
    """
    pass

def create_organization(FeatureSet=None):
    """
    Creates an AWS organization. The account whose user is calling the CreateOrganization operation automatically becomes the master account of the new organization.
    This operation must be called using credentials from the account that is to become the new organization's master account. The principal must also have the relevant IAM permissions.
    By default (or if you set the FeatureSet parameter to ALL ), the new organization is created with all features enabled and service control policies automatically enabled in the root. If you instead choose to create the organization supporting only the consolidated billing features by setting the FeatureSet parameter to CONSOLIDATED_BILLING" , then no policy types are enabled by default and you cannot use organization policies.
    See also: AWS API Documentation
    
    
    :example: response = client.create_organization(
        FeatureSet='ALL'|'CONSOLIDATED_BILLING'
    )
    
    
    :type FeatureSet: string
    :param FeatureSet: Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.
            CONSOLIDATED_BILLING : All member accounts have their bills consolidated to and paid by the master account. For more information, see Consolidated Billing in the AWS Organizations User Guide .
            ALL : In addition to all the features supported by the consolidated billing feature set, the master account can also apply any type of policy to any member account in the organization. For more information, see All features in the AWS Organizations User Guide .
            

    :rtype: dict
    :return: {
        'Organization': {
            'Id': 'string',
            'Arn': 'string',
            'FeatureSet': 'ALL'|'CONSOLIDATED_BILLING',
            'MasterAccountArn': 'string',
            'MasterAccountId': 'string',
            'MasterAccountEmail': 'string',
            'AvailablePolicyTypes': [
                {
                    'Type': 'SERVICE_CONTROL_POLICY',
                    'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                },
            ]
        }
    }
    
    
    """
    pass

def create_organizational_unit(ParentId=None, Name=None):
    """
    Creates an organizational unit (OU) within a root or parent OU. An OU is a container for accounts that enables you to organize your accounts to apply policies according to your business requirements. The number of levels deep that you can nest OUs is dependent upon the policy types enabled for that root. For service control policies, the limit is five.
    For more information about OUs, see Managing Organizational Units in the AWS Organizations User Guide .
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.create_organizational_unit(
        ParentId='string',
        Name='string'
    )
    
    
    :type ParentId: string
    :param ParentId: [REQUIRED]
            The unique identifier (ID) of the parent root or OU in which you want to create the new OU.
            The regex pattern for a parent ID string requires one of the following:
            Root: a string that begins with 'r-' followed by from 4 to 32 lower-case letters or digits.
            Organizational unit (OU): a string that begins with 'ou-' followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second '-' dash and from 8 to 32 additional lower-case letters or digits.
            

    :type Name: string
    :param Name: [REQUIRED]
            The friendly name to assign to the new OU.
            

    :rtype: dict
    :return: {
        'OrganizationalUnit': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        }
    }
    
    
    """
    pass

def create_policy(Content=None, Description=None, Name=None, Type=None):
    """
    Creates a policy of a specified type that you can attach to a root, an organizational unit (OU), or an individual AWS account.
    For more information about policies and their use, see Managing Organization Policies .
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.create_policy(
        Content='string',
        Description='string',
        Name='string',
        Type='SERVICE_CONTROL_POLICY'
    )
    
    
    :type Content: string
    :param Content: [REQUIRED]
            The policy content to add to the new policy. For example, if you create a service control policy (SCP), this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see Service Control Policy Syntax in the AWS Organizations User Guide .
            

    :type Description: string
    :param Description: [REQUIRED]
            An optional description to assign to the policy.
            

    :type Name: string
    :param Name: [REQUIRED]
            The friendly name to assign to the policy.
            The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.
            

    :type Type: string
    :param Type: [REQUIRED]
            The type of policy to create.
            Note
            In the current release, the only type of policy that you can create is a service control policy (SCP).
            

    :rtype: dict
    :return: {
        'Policy': {
            'PolicySummary': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'SERVICE_CONTROL_POLICY',
                'AwsManaged': True|False
            },
            'Content': 'string'
        }
    }
    
    
    """
    pass

def decline_handshake(HandshakeId=None):
    """
    Declines a handshake request. This sets the handshake state to DECLINED and effectively deactivates the request.
    This operation can be called only from the account that received the handshake. The originator of the handshake can use  CancelHandshake instead. The originator can't reactivate a declined request, but can re-initiate the process with a new handshake request.
    See also: AWS API Documentation
    
    
    :example: response = client.decline_handshake(
        HandshakeId='string'
    )
    
    
    :type HandshakeId: string
    :param HandshakeId: [REQUIRED]
            The unique identifier (ID) of the handshake that you want to decline. You can get the ID from the ListHandshakesForAccount operation.
            The regex pattern for handshake ID string requires 'h-' followed by from 8 to 32 lower-case letters or digits.
            

    :rtype: dict
    :return: {
        'Handshake': {
            'Id': 'string',
            'Arn': 'string',
            'Parties': [
                {
                    'Id': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                },
            ],
            'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
            'RequestedTimestamp': datetime(2015, 1, 1),
            'ExpirationTimestamp': datetime(2015, 1, 1),
            'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES',
            'Resources': [
                {
                    'Value': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                    'Resources': {'... recursive ...'}
                },
            ]
        }
    }
    
    
    :returns: 
    ACCOUNT - Specifies an AWS account ID number.
    ORGANIZATION - Specifies an organization ID number.
    EMAIL - Specifies the email address that is associated with the account that receives the handshake.
    OWNER_EMAIL - Specifies the email address associated with the master account. Included as information about an organization.
    OWNER_NAME - Specifies the name associated with the master account. Included as information about an organization.
    NOTES - Additional text provided by the handshake initiator and intended for the recipient to read.
    
    """
    pass

def delete_organization():
    """
    Deletes the organization. You can delete an organization only by using credentials from the master account. The organization must be empty of member accounts, OUs, and policies.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_organization()
    
    
    """
    pass

def delete_organizational_unit(OrganizationalUnitId=None):
    """
    Deletes an organizational unit from a root or another OU. You must first remove all accounts and child OUs from the OU that you want to delete.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_organizational_unit(
        OrganizationalUnitId='string'
    )
    
    
    :type OrganizationalUnitId: string
    :param OrganizationalUnitId: [REQUIRED]
            The unique identifier (ID) of the organizational unit that you want to delete. You can get the ID from the ListOrganizationalUnitsForParent operation.
            The regex pattern for an organizational unit ID string requires 'ou-' followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second '-' dash and from 8 to 32 additional lower-case letters or digits.
            

    """
    pass

def delete_policy(PolicyId=None):
    """
    Deletes the specified policy from your organization. Before you perform this operation, you must first detach the policy from all OUs, roots, and accounts.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_policy(
        PolicyId='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]
            The unique identifier (ID) of the policy that you want to delete. You can get the ID from the ListPolicies or ListPoliciesForTarget operations.
            The regex pattern for a policy ID string requires 'p-' followed by from 8 to 128 lower-case letters or digits.
            

    """
    pass

def describe_account(AccountId=None):
    """
    Retrieves Organizations-related information about the specified account.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_account(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The unique identifier (ID) of the AWS account that you want information about. You can get the ID from the ListAccounts or ListAccountsForParent operations.
            The regex pattern for an account ID string requires exactly 12 digits.
            

    :rtype: dict
    :return: {
        'Account': {
            'Id': 'string',
            'Arn': 'string',
            'Email': 'string',
            'Name': 'string',
            'Status': 'ACTIVE'|'SUSPENDED',
            'JoinedMethod': 'INVITED'|'CREATED',
            'JoinedTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def describe_create_account_status(CreateAccountRequestId=None):
    """
    Retrieves the current status of an asynchronous request to create an account.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_create_account_status(
        CreateAccountRequestId='string'
    )
    
    
    :type CreateAccountRequestId: string
    :param CreateAccountRequestId: [REQUIRED]
            Specifies the operationId that uniquely identifies the request. You can get the ID from the response to an earlier CreateAccount request, or from the ListCreateAccountStatus operation.
            The regex pattern for an create account request ID string requires 'car-' followed by from 8 to 32 lower-case letters or digits.
            

    :rtype: dict
    :return: {
        'CreateAccountStatus': {
            'Id': 'string',
            'AccountName': 'string',
            'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
            'RequestedTimestamp': datetime(2015, 1, 1),
            'CompletedTimestamp': datetime(2015, 1, 1),
            'AccountId': 'string',
            'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'INTERNAL_FAILURE'
        }
    }
    
    
    """
    pass

def describe_handshake(HandshakeId=None):
    """
    Retrieves information about a previously requested handshake. The handshake ID comes from the response to the original  InviteAccountToOrganization operation that generated the handshake.
    This operation can be called from any account in the organization.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_handshake(
        HandshakeId='string'
    )
    
    
    :type HandshakeId: string
    :param HandshakeId: [REQUIRED]
            The unique identifier (ID) of the handshake that you want information about. You can get the ID from the original call to InviteAccountToOrganization , or from a call to ListHandshakesForAccount or ListHandshakesForOrganization .
            The regex pattern for handshake ID string requires 'h-' followed by from 8 to 32 lower-case letters or digits.
            

    :rtype: dict
    :return: {
        'Handshake': {
            'Id': 'string',
            'Arn': 'string',
            'Parties': [
                {
                    'Id': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                },
            ],
            'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
            'RequestedTimestamp': datetime(2015, 1, 1),
            'ExpirationTimestamp': datetime(2015, 1, 1),
            'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES',
            'Resources': [
                {
                    'Value': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                    'Resources': {'... recursive ...'}
                },
            ]
        }
    }
    
    
    :returns: 
    ACCOUNT - Specifies an AWS account ID number.
    ORGANIZATION - Specifies an organization ID number.
    EMAIL - Specifies the email address that is associated with the account that receives the handshake.
    OWNER_EMAIL - Specifies the email address associated with the master account. Included as information about an organization.
    OWNER_NAME - Specifies the name associated with the master account. Included as information about an organization.
    NOTES - Additional text provided by the handshake initiator and intended for the recipient to read.
    
    """
    pass

def describe_organization():
    """
    Retrieves information about the organization that the user's account belongs to.
    This operation can be called from any account in the organization.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_organization()
    
    
    :rtype: dict
    :return: {
        'Organization': {
            'Id': 'string',
            'Arn': 'string',
            'FeatureSet': 'ALL'|'CONSOLIDATED_BILLING',
            'MasterAccountArn': 'string',
            'MasterAccountId': 'string',
            'MasterAccountEmail': 'string',
            'AvailablePolicyTypes': [
                {
                    'Type': 'SERVICE_CONTROL_POLICY',
                    'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                },
            ]
        }
    }
    
    
    """
    pass

def describe_organizational_unit(OrganizationalUnitId=None):
    """
    Retrieves information about an organizational unit (OU).
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_organizational_unit(
        OrganizationalUnitId='string'
    )
    
    
    :type OrganizationalUnitId: string
    :param OrganizationalUnitId: [REQUIRED]
            The unique identifier (ID) of the organizational unit that you want details about. You can get the ID from the ListOrganizationalUnitsForParent operation.
            The regex pattern for an organizational unit ID string requires 'ou-' followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second '-' dash and from 8 to 32 additional lower-case letters or digits.
            

    :rtype: dict
    :return: {
        'OrganizationalUnit': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        }
    }
    
    
    """
    pass

def describe_policy(PolicyId=None):
    """
    Retrieves information about a policy.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_policy(
        PolicyId='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]
            The unique identifier (ID) of the policy that you want details about. You can get the ID from the ListPolicies or ListPoliciesForTarget operations.
            The regex pattern for a policy ID string requires 'p-' followed by from 8 to 128 lower-case letters or digits.
            

    :rtype: dict
    :return: {
        'Policy': {
            'PolicySummary': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'SERVICE_CONTROL_POLICY',
                'AwsManaged': True|False
            },
            'Content': 'string'
        }
    }
    
    
    """
    pass

def detach_policy(PolicyId=None, TargetId=None):
    """
    Detaches a policy from a target root, organizational unit, or account. If the policy being detached is a service control policy (SCP), the changes to permissions for IAM users and roles in affected accounts are immediate.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.detach_policy(
        PolicyId='string',
        TargetId='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]
            The unique identifier (ID) of the policy you want to detach. You can get the ID from the ListPolicies or ListPoliciesForTarget operations.
            The regex pattern for a policy ID string requires 'p-' followed by from 8 to 128 lower-case letters or digits.
            

    :type TargetId: string
    :param TargetId: [REQUIRED]
            The unique identifier (ID) of the root, OU, or account from which you want to detach the policy. You can get the ID from the ListRoots , ListOrganizationalUnitsForParent , or ListAccounts operations.
            The regex pattern for a target ID string requires one of the following:
            Root: a string that begins with 'r-' followed by from 4 to 32 lower-case letters or digits.
            Account: a string that consists of exactly 12 digits.
            Organizational unit (OU): a string that begins with 'ou-' followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second '-' dash and from 8 to 32 additional lower-case letters or digits.
            

    """
    pass

def disable_policy_type(RootId=None, PolicyType=None):
    """
    Disables an organizational control policy type in a root. A poicy of a certain type can be attached to entities in a root only if that type is enabled in the root. After you perform this operation, you no longer can attach policies of the specified type to that root or to any OU or account in that root. You can undo this by using the  EnablePolicyType operation.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_policy_type(
        RootId='string',
        PolicyType='SERVICE_CONTROL_POLICY'
    )
    
    
    :type RootId: string
    :param RootId: [REQUIRED]
            The unique identifier (ID) of the root in which you want to disable a policy type. You can get the ID from the ListPolicies operation.
            The regex pattern for a root ID string requires 'r-' followed by from 4 to 32 lower-case letters or digits.
            

    :type PolicyType: string
    :param PolicyType: [REQUIRED]
            The policy type that you want to disable in this root.
            

    :rtype: dict
    :return: {
        'Root': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'PolicyTypes': [
                {
                    'Type': 'SERVICE_CONTROL_POLICY',
                    'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                },
            ]
        }
    }
    
    
    """
    pass

def enable_all_features():
    """
    Enables all features in an organization. This enables the use of organization policies that can restrict the services and actions that can be called in each account. Until you enable all features, you have access only to consolidated billing, and you can't use any of the advanced account administration features that AWS Organizations supports. For more information, see Enabling All Features in Your Organization in the AWS Organizations User Guide .
    After all invited member accounts accept the handshake, you finalize the feature set change by accepting the handshake that contains "Action": "ENABLE_ALL_FEATURES" . This completes the change.
    After you enable all features in your organization, the master account in the organization can apply policies on all member accounts. These policies can restrict what users and even administrators in those accounts can do. The master account can apply policies that prevent accounts from leaving the organization. Ensure that your account administrators are aware of this.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_all_features()
    
    
    :rtype: dict
    :return: {
        'Handshake': {
            'Id': 'string',
            'Arn': 'string',
            'Parties': [
                {
                    'Id': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                },
            ],
            'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
            'RequestedTimestamp': datetime(2015, 1, 1),
            'ExpirationTimestamp': datetime(2015, 1, 1),
            'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES',
            'Resources': [
                {
                    'Value': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                    'Resources': {'... recursive ...'}
                },
            ]
        }
    }
    
    
    :returns: 
    ACCOUNT - Specifies an AWS account ID number.
    ORGANIZATION - Specifies an organization ID number.
    EMAIL - Specifies the email address that is associated with the account that receives the handshake.
    OWNER_EMAIL - Specifies the email address associated with the master account. Included as information about an organization.
    OWNER_NAME - Specifies the name associated with the master account. Included as information about an organization.
    NOTES - Additional text provided by the handshake initiator and intended for the recipient to read.
    
    """
    pass

def enable_policy_type(RootId=None, PolicyType=None):
    """
    Enables a policy type in a root. After you enable a policy type in a root, you can attach policies of that type to the root, any OU, or account in that root. You can undo this by using the  DisablePolicyType operation.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_policy_type(
        RootId='string',
        PolicyType='SERVICE_CONTROL_POLICY'
    )
    
    
    :type RootId: string
    :param RootId: [REQUIRED]
            The unique identifier (ID) of the root in which you want to enable a policy type. You can get the ID from the ListRoots operation.
            The regex pattern for a root ID string requires 'r-' followed by from 4 to 32 lower-case letters or digits.
            

    :type PolicyType: string
    :param PolicyType: [REQUIRED]
            The policy type that you want to enable.
            

    :rtype: dict
    :return: {
        'Root': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'PolicyTypes': [
                {
                    'Type': 'SERVICE_CONTROL_POLICY',
                    'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                },
            ]
        }
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

def get_waiter():
    """
    
    """
    pass

def invite_account_to_organization(Target=None, Notes=None):
    """
    Sends an invitation to another account to join your organization as a member account. Organizations sends email on your behalf to the email address that is associated with the other account's owner. The invitation is implemented as a  Handshake whose details are in the response.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.invite_account_to_organization(
        Target={
            'Id': 'string',
            'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
        },
        Notes='string'
    )
    
    
    :type Target: dict
    :param Target: [REQUIRED]
            The identifier (ID) of the AWS account that you want to invite to join your organization. This is a JSON object that contains the following elements:
            { 'Type': 'ACCOUNT', 'Id': '* **account id number** * ' }
            If you use the AWS CLI, you can submit this as a single string, similar to the following example:
            --target id=123456789012,type=ACCOUNT
            If you specify 'Type': 'ACCOUNT' , then you must provide the AWS account ID number as the Id . If you specify 'Type': 'EMAIL' , then you must specify the email address that is associated with the account.
            --target id=bill@example.com,type=EMAIL
            Id (string) --The unique identifier (ID) for the party.
            The regex pattern for handshake ID string requires 'h-' followed by from 8 to 32 lower-case letters or digits.
            Type (string) --The type of party.
            

    :type Notes: string
    :param Notes: Additional information that you want to include in the generated email to the recipient account owner.

    :rtype: dict
    :return: {
        'Handshake': {
            'Id': 'string',
            'Arn': 'string',
            'Parties': [
                {
                    'Id': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                },
            ],
            'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
            'RequestedTimestamp': datetime(2015, 1, 1),
            'ExpirationTimestamp': datetime(2015, 1, 1),
            'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES',
            'Resources': [
                {
                    'Value': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                    'Resources': {'... recursive ...'}
                },
            ]
        }
    }
    
    
    :returns: 
    REQUESTED : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond.
    OPEN : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action.
    CANCELED : This handshake is no longer active because it was canceled by the originating account.
    ACCEPTED : This handshake is complete because it has been accepted by the recipient.
    DECLINED : This handshake is no longer active because it was declined by the recipient account.
    EXPIRED : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days).
    
    """
    pass

def leave_organization():
    """
    Removes a member account from its parent organization. This version of the operation is performed by the account that wants to leave. To remove a member account as a user in the master account, use  RemoveAccountFromOrganization instead.
    This operation can be called only from a member account in the organization.
    See also: AWS API Documentation
    
    
    :example: response = client.leave_organization()
    
    
    """
    pass

def list_accounts(NextToken=None, MaxResults=None):
    """
    Lists all the accounts in the organization. To request only the accounts in a root or OU, use the  ListAccountsForParent operation instead.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_accounts(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: Use this parameter if you receive a NextToken response in a previous request that indicates that there is more output available. Set it to the value of the previous call's NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict
    :return: {
        'Accounts': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Email': 'string',
                'Name': 'string',
                'Status': 'ACTIVE'|'SUSPENDED',
                'JoinedMethod': 'INVITED'|'CREATED',
                'JoinedTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_accounts_for_parent(ParentId=None, NextToken=None, MaxResults=None):
    """
    Lists the accounts in an organization that are contained by the specified target root or organizational unit (OU). If you specify the root, you get a list of all the accounts that are not in any OU. If you specify an OU, you get a list of all the accounts in only that OU, and not in any child OUs. To get a list of all accounts in the organization, use the  ListAccounts operation.
    See also: AWS API Documentation
    
    
    :example: response = client.list_accounts_for_parent(
        ParentId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ParentId: string
    :param ParentId: [REQUIRED]
            The unique identifier (ID) for the parent root or organization unit (OU) whose accounts you want to list.
            

    :type NextToken: string
    :param NextToken: Use this parameter if you receive a NextToken response in a previous request that indicates that there is more output available. Set it to the value of the previous call's NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict
    :return: {
        'Accounts': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Email': 'string',
                'Name': 'string',
                'Status': 'ACTIVE'|'SUSPENDED',
                'JoinedMethod': 'INVITED'|'CREATED',
                'JoinedTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_children(ParentId=None, ChildType=None, NextToken=None, MaxResults=None):
    """
    Lists all of the OUs or accounts that are contained in the specified parent OU or root. This operation, along with  ListParents enables you to traverse the tree structure that makes up this root.
    See also: AWS API Documentation
    
    
    :example: response = client.list_children(
        ParentId='string',
        ChildType='ACCOUNT'|'ORGANIZATIONAL_UNIT',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ParentId: string
    :param ParentId: [REQUIRED]
            The unique identifier (ID) for the parent root or OU whose children you want to list.
            The regex pattern for a parent ID string requires one of the following:
            Root: a string that begins with 'r-' followed by from 4 to 32 lower-case letters or digits.
            Organizational unit (OU): a string that begins with 'ou-' followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second '-' dash and from 8 to 32 additional lower-case letters or digits.
            

    :type ChildType: string
    :param ChildType: [REQUIRED]
            Filters the output to include only the specified child type.
            

    :type NextToken: string
    :param NextToken: Use this parameter if you receive a NextToken response in a previous request that indicates that there is more output available. Set it to the value of the previous call's NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict
    :return: {
        'Children': [
            {
                'Id': 'string',
                'Type': 'ACCOUNT'|'ORGANIZATIONAL_UNIT'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Account: a string that consists of exactly 12 digits.
    Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    
    """
    pass

def list_create_account_status(States=None, NextToken=None, MaxResults=None):
    """
    Lists the account creation requests that match the specified status that is currently being tracked for the organization.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_create_account_status(
        States=[
            'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type States: list
    :param States: A list of one or more states that you want included in the response. If this parameter is not present, then all requests are included in the response.
            (string) --
            

    :type NextToken: string
    :param NextToken: Use this parameter if you receive a NextToken response in a previous request that indicates that there is more output available. Set it to the value of the previous call's NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict
    :return: {
        'CreateAccountStatuses': [
            {
                'Id': 'string',
                'AccountName': 'string',
                'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                'RequestedTimestamp': datetime(2015, 1, 1),
                'CompletedTimestamp': datetime(2015, 1, 1),
                'AccountId': 'string',
                'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'INTERNAL_FAILURE'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the limit on the number of accounts in your organization.
    EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with that email address already exists.
    INVALID_ADDRESS: The account could not be created because the address you provided is not valid.
    INVALID_EMAIL: The account could not be created because the email address you provided is not valid.
    INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Customer Support.
    
    """
    pass

def list_handshakes_for_account(Filter=None, NextToken=None, MaxResults=None):
    """
    Lists the current handshakes that are associated with the account of the requesting user.
    This operation can be called from any account in the organization.
    See also: AWS API Documentation
    
    
    :example: response = client.list_handshakes_for_account(
        Filter={
            'ActionType': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES',
            'ParentHandshakeId': 'string'
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters the handshakes that you want included in the response. The default is all types. Use the ActionType element to limit the output to only a specified type, such as INVITE , ENABLE-FULL-CONTROL , or APPROVE-FULL-CONTROL . Alternatively, for the ENABLE-FULL-CONTROL handshake that generates a separate child handshake for each member account, you can specify ParentHandshakeId to see only the handshakes that were generated by that parent request.
            ActionType (string) --Specifies the type of handshake action.
            If you specify ActionType , you cannot also specify ParentHandshakeId .
            ParentHandshakeId (string) --Specifies the parent handshake. Only used for handshake types that are a child of another type.
            If you specify ParentHandshakeId , you cannot also specify ActionType .
            The regex pattern for handshake ID string requires 'h-' followed by from 8 to 32 lower-case letters or digits.
            

    :type NextToken: string
    :param NextToken: Use this parameter if you receive a NextToken response in a previous request that indicates that there is more output available. Set it to the value of the previous call's NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict
    :return: {
        'Handshakes': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Parties': [
                    {
                        'Id': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                    },
                ],
                'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
                'RequestedTimestamp': datetime(2015, 1, 1),
                'ExpirationTimestamp': datetime(2015, 1, 1),
                'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES',
                'Resources': [
                    {
                        'Value': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                        'Resources': {'... recursive ...'}
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    REQUESTED : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond.
    OPEN : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action.
    CANCELED : This handshake is no longer active because it was canceled by the originating account.
    ACCEPTED : This handshake is complete because it has been accepted by the recipient.
    DECLINED : This handshake is no longer active because it was declined by the recipient account.
    EXPIRED : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days).
    
    """
    pass

def list_handshakes_for_organization(Filter=None, NextToken=None, MaxResults=None):
    """
    Lists the handshakes that are associated with the organization that the requesting user is part of. The ListHandshakesForOrganization operation returns a list of handshake structures. Each structure contains details and status about a handshake.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_handshakes_for_organization(
        Filter={
            'ActionType': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES',
            'ParentHandshakeId': 'string'
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: A filter of the handshakes that you want included in the response. The default is all types. Use the ActionType element to limit the output to only a specified type, such as INVITE , ENABLE-ALL-FEATURES , or APPROVE-ALL-FEATURES . Alternatively, for the ENABLE-ALL-FEATURES handshake that generates a separate child handshake for each member account, you can specify the ParentHandshakeId to see only the handshakes that were generated by that parent request.
            ActionType (string) --Specifies the type of handshake action.
            If you specify ActionType , you cannot also specify ParentHandshakeId .
            ParentHandshakeId (string) --Specifies the parent handshake. Only used for handshake types that are a child of another type.
            If you specify ParentHandshakeId , you cannot also specify ActionType .
            The regex pattern for handshake ID string requires 'h-' followed by from 8 to 32 lower-case letters or digits.
            

    :type NextToken: string
    :param NextToken: Use this parameter if you receive a NextToken response in a previous request that indicates that there is more output available. Set it to the value of the previous call's NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict
    :return: {
        'Handshakes': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Parties': [
                    {
                        'Id': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                    },
                ],
                'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
                'RequestedTimestamp': datetime(2015, 1, 1),
                'ExpirationTimestamp': datetime(2015, 1, 1),
                'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES',
                'Resources': [
                    {
                        'Value': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                        'Resources': {'... recursive ...'}
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    REQUESTED : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond.
    OPEN : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action.
    CANCELED : This handshake is no longer active because it was canceled by the originating account.
    ACCEPTED : This handshake is complete because it has been accepted by the recipient.
    DECLINED : This handshake is no longer active because it was declined by the recipient account.
    EXPIRED : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days).
    
    """
    pass

def list_organizational_units_for_parent(ParentId=None, NextToken=None, MaxResults=None):
    """
    Lists the organizational units (OUs) in a parent organizational unit or root.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_organizational_units_for_parent(
        ParentId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ParentId: string
    :param ParentId: [REQUIRED]
            The unique identifier (ID) of the root or OU whose child OUs you want to list.
            The regex pattern for a parent ID string requires one of the following:
            Root: a string that begins with 'r-' followed by from 4 to 32 lower-case letters or digits.
            Organizational unit (OU): a string that begins with 'ou-' followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second '-' dash and from 8 to 32 additional lower-case letters or digits.
            

    :type NextToken: string
    :param NextToken: Use this parameter if you receive a NextToken response in a previous request that indicates that there is more output available. Set it to the value of the previous call's NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict
    :return: {
        'OrganizationalUnits': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_parents(ChildId=None, NextToken=None, MaxResults=None):
    """
    Lists the root or organizational units (OUs) that serve as the immediate parent of the specified child OU or account. This operation, along with  ListChildren enables you to traverse the tree structure that makes up this root.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_parents(
        ChildId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ChildId: string
    :param ChildId: [REQUIRED]
            The unique identifier (ID) of the OU or account whose parent containers you want to list. Do not specify a root.
            The regex pattern for a child ID string requires one of the following:
            Account: a string that consists of exactly 12 digits.
            Organizational unit (OU): a string that begins with 'ou-' followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second '-' dash and from 8 to 32 additional lower-case letters or digits.
            

    :type NextToken: string
    :param NextToken: Use this parameter if you receive a NextToken response in a previous request that indicates that there is more output available. Set it to the value of the previous call's NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict
    :return: {
        'Parents': [
            {
                'Id': 'string',
                'Type': 'ROOT'|'ORGANIZATIONAL_UNIT'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.
    Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    
    """
    pass

def list_policies(Filter=None, NextToken=None, MaxResults=None):
    """
    Retrieves the list of all policies in an organization of a specified type.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_policies(
        Filter='SERVICE_CONTROL_POLICY',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: string
    :param Filter: [REQUIRED]
            Specifies the type of policy that you want to include in the response.
            

    :type NextToken: string
    :param NextToken: Use this parameter if you receive a NextToken response in a previous request that indicates that there is more output available. Set it to the value of the previous call's NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict
    :return: {
        'Policies': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'SERVICE_CONTROL_POLICY',
                'AwsManaged': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_policies_for_target(TargetId=None, Filter=None, NextToken=None, MaxResults=None):
    """
    Lists the policies that are directly attached to the specified target root, organizational unit (OU), or account. You must specify the policy type that you want included in the returned list.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_policies_for_target(
        TargetId='string',
        Filter='SERVICE_CONTROL_POLICY',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type TargetId: string
    :param TargetId: [REQUIRED]
            The unique identifier (ID) of the root, organizational unit, or account whose policies you want to list.
            The regex pattern for a target ID string requires one of the following:
            Root: a string that begins with 'r-' followed by from 4 to 32 lower-case letters or digits.
            Account: a string that consists of exactly 12 digits.
            Organizational unit (OU): a string that begins with 'ou-' followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second '-' dash and from 8 to 32 additional lower-case letters or digits.
            

    :type Filter: string
    :param Filter: [REQUIRED]
            The type of policy that you want to include in the returned list.
            

    :type NextToken: string
    :param NextToken: Use this parameter if you receive a NextToken response in a previous request that indicates that there is more output available. Set it to the value of the previous call's NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict
    :return: {
        'Policies': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'SERVICE_CONTROL_POLICY',
                'AwsManaged': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_roots(NextToken=None, MaxResults=None):
    """
    Lists the roots that are defined in the current organization.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_roots(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: Use this parameter if you receive a NextToken response in a previous request that indicates that there is more output available. Set it to the value of the previous call's NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict
    :return: {
        'Roots': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'PolicyTypes': [
                    {
                        'Type': 'SERVICE_CONTROL_POLICY',
                        'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_targets_for_policy(PolicyId=None, NextToken=None, MaxResults=None):
    """
    Lists all the roots, OUs, and accounts to which the specified policy is attached.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_targets_for_policy(
        PolicyId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]
            The unique identifier (ID) of the policy for which you want to know its attachments.
            The regex pattern for a policy ID string requires 'p-' followed by from 8 to 128 lower-case letters or digits.
            

    :type NextToken: string
    :param NextToken: Use this parameter if you receive a NextToken response in a previous request that indicates that there is more output available. Set it to the value of the previous call's NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict
    :return: {
        'Targets': [
            {
                'TargetId': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Type': 'ACCOUNT'|'ORGANIZATIONAL_UNIT'|'ROOT'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.
    Account: a string that consists of exactly 12 digits.
    Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    
    """
    pass

def move_account(AccountId=None, SourceParentId=None, DestinationParentId=None):
    """
    Moves an account from its current source parent root or OU to the specified destination parent root or OU.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.move_account(
        AccountId='string',
        SourceParentId='string',
        DestinationParentId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The unique identifier (ID) of the account that you want to move.
            The regex pattern for an account ID string requires exactly 12 digits.
            

    :type SourceParentId: string
    :param SourceParentId: [REQUIRED]
            The unique identifier (ID) of the root or organizational unit that you want to move the account from.
            The regex pattern for a parent ID string requires one of the following:
            Root: a string that begins with 'r-' followed by from 4 to 32 lower-case letters or digits.
            Organizational unit (OU): a string that begins with 'ou-' followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second '-' dash and from 8 to 32 additional lower-case letters or digits.
            

    :type DestinationParentId: string
    :param DestinationParentId: [REQUIRED]
            The unique identifier (ID) of the root or organizational unit that you want to move the account to.
            The regex pattern for a parent ID string requires one of the following:
            Root: a string that begins with 'r-' followed by from 4 to 32 lower-case letters or digits.
            Organizational unit (OU): a string that begins with 'ou-' followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second '-' dash and from 8 to 32 additional lower-case letters or digits.
            

    """
    pass

def remove_account_from_organization(AccountId=None):
    """
    Removes the specified account from the organization.
    The removed account becomes a stand-alone account that is not a member of any organization. It is no longer subject to any policies and is responsible for its own bill payments. The organization's master account is no longer charged for any expenses accrued by the member account after it is removed from the organization.
    This operation can be called only from the organization's master account. Member accounts can remove themselves with  LeaveOrganization instead.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_account_from_organization(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The unique identifier (ID) of the member account that you want to remove from the organization.
            The regex pattern for an account ID string requires exactly 12 digits.
            

    """
    pass

def update_organizational_unit(OrganizationalUnitId=None, Name=None):
    """
    Renames the specified organizational unit (OU). The ID and ARN do not change. The child OUs and accounts remain in place, and any attached policies of the OU remain attached.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.update_organizational_unit(
        OrganizationalUnitId='string',
        Name='string'
    )
    
    
    :type OrganizationalUnitId: string
    :param OrganizationalUnitId: [REQUIRED]
            The unique identifier (ID) of the OU that you want to rename. You can get the ID from the ListOrganizationalUnitsForParent operation.
            The regex pattern for an organizational unit ID string requires 'ou-' followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second '-' dash and from 8 to 32 additional lower-case letters or digits.
            

    :type Name: string
    :param Name: The new name that you want to assign to the OU.
            The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.
            

    :rtype: dict
    :return: {
        'OrganizationalUnit': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        }
    }
    
    
    """
    pass

def update_policy(PolicyId=None, Name=None, Description=None, Content=None):
    """
    Updates an existing policy with a new name, description, or content. If any parameter is not supplied, that value remains unchanged. Note that you cannot change a policy's type.
    This operation can be called only from the organization's master account.
    See also: AWS API Documentation
    
    
    :example: response = client.update_policy(
        PolicyId='string',
        Name='string',
        Description='string',
        Content='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]
            The unique identifier (ID) of the policy that you want to update.
            The regex pattern for a policy ID string requires 'p-' followed by from 8 to 128 lower-case letters or digits.
            

    :type Name: string
    :param Name: If provided, the new name for the policy.
            The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.
            

    :type Description: string
    :param Description: If provided, the new description for the policy.

    :type Content: string
    :param Content: If provided, the new content for the policy. The text must be correctly formatted JSON that complies with the syntax for the policy's type. For more information, see Service Control Policy Syntax in the AWS Organizations User Guide .

    :rtype: dict
    :return: {
        'Policy': {
            'PolicySummary': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'SERVICE_CONTROL_POLICY',
                'AwsManaged': True|False
            },
            'Content': 'string'
        }
    }
    
    
    """
    pass

