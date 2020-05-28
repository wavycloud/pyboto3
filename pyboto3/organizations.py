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
    After you accept a handshake, it continues to appear in the results of relevant APIs for only 30 days. After that, it\'s deleted.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Bill is the owner of an organization, and he invites Juan\'s account (222222222222) to join his organization. The following example shows Juan\'s account accepting the handshake and thus agreeing to the invitation.
    Expected Output:
    
    :example: response = client.accept_handshake(
        HandshakeId='string'
    )
    
    
    :type HandshakeId: string
    :param HandshakeId: [REQUIRED]\nThe unique identifier (ID) of the handshake that you want to accept.\nThe regex pattern for handshake ID string requires 'h-' followed by from 8 to 32 lowercase letters or digits.\n

    :rtype: dict
ReturnsResponse Syntax{
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
        'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
        'Resources': [
            {
                'Value': 'string',
                'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                'Resources': {'... recursive ...'}
            },
        ]
    }
}


Response Structure

(dict) --
Handshake (dict) --A structure that contains details about the accepted handshake.

Id (string) --The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Arn (string) --The Amazon Resource Name (ARN) of a handshake.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Parties (list) --Information about the two accounts that are participating in the handshake.

(dict) --Identifies a participant in a handshake.

Id (string) --The unique identifier (ID) for the party.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Type (string) --The type of party.





State (string) --The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

REQUESTED : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond.
OPEN : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action.
CANCELED : This handshake is no longer active because it was canceled by the originating account.
ACCEPTED : This handshake is complete because it has been accepted by the recipient.
DECLINED : This handshake is no longer active because it was declined by the recipient account.
EXPIRED : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days).


RequestedTimestamp (datetime) --The date and time that the handshake request was made.

ExpirationTimestamp (datetime) --The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

Action (string) --The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

INVITE : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts.
ENABLE_ALL_FEATURES : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only invited member accounts. Created accounts do not receive this because those accounts were created by the organization\'s master account and approval is inferred.
APPROVE_ALL_FEATURES : This type of handshake is sent from the Organizations service when all member accounts have approved the ENABLE_ALL_FEATURES invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features.


Resources (list) --Additional information that is needed to process the handshake.

(dict) --Contains additional data that is needed to process a handshake.

Value (string) --The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

Type (string) --The type of information being passed, specifying how the value is to be interpreted by the other party:

ACCOUNT - Specifies an AWS account ID number.
ORGANIZATION - Specifies an organization ID number.
EMAIL - Specifies the email address that is associated with the account that receives the handshake.
OWNER_EMAIL - Specifies the email address associated with the master account. Included as information about an organization.
OWNER_NAME - Specifies the name associated with the master account. Included as information about an organization.
NOTES - Additional text provided by the handshake initiator and intended for the recipient to read.


Resources (list) --When needed, contains an additional array of HandshakeResource objects.












Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.HandshakeConstraintViolationException
Organizations.Client.exceptions.HandshakeNotFoundException
Organizations.Client.exceptions.InvalidHandshakeTransitionException
Organizations.Client.exceptions.HandshakeAlreadyInStateException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.AccessDeniedForDependencyException

Examples
Bill is the owner of an organization, and he invites Juan\'s account (222222222222) to join his organization. The following example shows Juan\'s account accepting the handshake and thus agreeing to the invitation.
response = client.accept_handshake(
    HandshakeId='h-examplehandshakeid111',
)

print(response)


Expected Output:
{
    'Handshake': {
        'Action': 'INVITE',
        'Arn': 'arn:aws:organizations::111111111111:handshake/o-exampleorgid/invite/h-examplehandshakeid111',
        'ExpirationTimestamp': datetime(2017, 2, 28, 12, 15, 0, 1, 59, 0),
        'Id': 'h-examplehandshakeid111',
        'Parties': [
            {
                'Id': 'o-exampleorgid',
                'Type': 'ORGANIZATION',
            },
            {
                'Id': 'juan@example.com',
                'Type': 'EMAIL',
            },
        ],
        'RequestedTimestamp': datetime(2017, 2, 14, 12, 15, 0, 1, 45, 0),
        'Resources': [
            {
                'Resources': [
                    {
                        'Type': 'MASTER_EMAIL',
                        'Value': 'bill@amazon.com',
                    },
                    {
                        'Type': 'MASTER_NAME',
                        'Value': 'Org Master Account',
                    },
                    {
                        'Type': 'ORGANIZATION_FEATURE_SET',
                        'Value': 'ALL',
                    },
                ],
                'Type': 'ORGANIZATION',
                'Value': 'o-exampleorgid',
            },
            {
                'Type': 'ACCOUNT',
                'Value': '222222222222',
            },
        ],
        'State': 'ACCEPTED',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
            'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
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
    Attaches a policy to a root, an organizational unit (OU), or an individual account. How the policy affects accounts depends on the type of policy:
    SCPs are JSON policies that specify the maximum permissions for an organization or organizational unit (OU). You can attach one SCP to a higher level root or OU, and a different SCP to a child OU or to an account. The child policy can further restrict only the permissions that pass through the parent filter and are available to the child. An SCP that is attached to a child can\'t grant a permission that the parent hasn\'t already granted. For example, imagine that the parent SCP allows permissions A, B, C, D, and E. The child SCP allows C, D, E, F, and G. The result is that the accounts affected by the child SCP are allowed to use only C, D, and E. They can\'t use A or B because the child OU filtered them out. They also can\'t use F and G because the parent OU filtered them out. They can\'t be granted back by the child SCP; child SCPs can only filter the permissions they receive from the parent SCP.
    AWS Organizations attaches a default SCP named "FullAWSAccess to every root, OU, and account. This default SCP allows all services and actions, enabling any new child OU or account to inherit the permissions of the parent root or OU. If you detach the default policy, you must replace it with a policy that specifies the permissions that you want to allow in that OU or account.
    For more information about how AWS Organizations policies permissions work, see Using Service Control Policies in the AWS Organizations User Guide.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to attach a service control policy (SCP) to an OU:
    Expected Output:
    The following example shows how to attach a service control policy (SCP) to an account:
    Expected Output:
    
    :example: response = client.attach_policy(
        PolicyId='string',
        TargetId='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]\nThe unique identifier (ID) of the policy that you want to attach to the target. You can get the ID for the policy by calling the ListPolicies operation.\nThe regex pattern for a policy ID string requires 'p-' followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).\n

    :type TargetId: string
    :param TargetId: [REQUIRED]\nThe unique identifier (ID) of the root, OU, or account that you want to attach the policy to. You can get the ID by calling the ListRoots , ListOrganizationalUnitsForParent , or ListAccounts operations.\nThe regex pattern for a target ID string requires one of the following:\n\nRoot - A string that begins with 'r-' followed by from 4 to 32 lowercase letters or digits.\nAccount - A string that consists of exactly 12 digits.\nOrganizational unit (OU) - A string that begins with 'ou-' followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second '-' dash and from 8 to 32 additional lowercase letters or digits.\n\n

    :return: response = client.attach_policy(
        PolicyId='p-examplepolicyid111',
        TargetId='ou-examplerootid111-exampleouid111',
    )
    
    print(response)
    
    
    :returns: 
    PolicyId (string) -- [REQUIRED]
    The unique identifier (ID) of the policy that you want to attach to the target. You can get the ID for the policy by calling the  ListPolicies operation.
    The regex pattern for a policy ID string requires "p-" followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).
    
    TargetId (string) -- [REQUIRED]
    The unique identifier (ID) of the root, OU, or account that you want to attach the policy to. You can get the ID by calling the  ListRoots ,  ListOrganizationalUnitsForParent , or  ListAccounts operations.
    The regex pattern for a target ID string requires one of the following:
    
    Root - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits.
    Account - A string that consists of exactly 12 digits.
    Organizational unit (OU) - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.
    
    
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def cancel_handshake(HandshakeId=None):
    """
    Cancels a handshake. Canceling a handshake sets the handshake state to CANCELED .
    This operation can be called only from the account that originated the handshake. The recipient of the handshake can\'t cancel it, but can use  DeclineHandshake instead. After a handshake is canceled, the recipient can no longer respond to that handshake.
    After you cancel a handshake, it continues to appear in the results of relevant APIs for only 30 days. After that, it\'s deleted.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Bill previously sent an invitation to Susan\'s account to join his organization. He changes his mind and decides to cancel the invitation before Susan accepts it. The following example shows Bill\'s cancellation:
    Expected Output:
    
    :example: response = client.cancel_handshake(
        HandshakeId='string'
    )
    
    
    :type HandshakeId: string
    :param HandshakeId: [REQUIRED]\nThe unique identifier (ID) of the handshake that you want to cancel. You can get the ID from the ListHandshakesForOrganization operation.\nThe regex pattern for handshake ID string requires 'h-' followed by from 8 to 32 lowercase letters or digits.\n

    :rtype: dict
ReturnsResponse Syntax{
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
        'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
        'Resources': [
            {
                'Value': 'string',
                'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                'Resources': {'... recursive ...'}
            },
        ]
    }
}


Response Structure

(dict) --
Handshake (dict) --A structure that contains details about the handshake that you canceled.

Id (string) --The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Arn (string) --The Amazon Resource Name (ARN) of a handshake.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Parties (list) --Information about the two accounts that are participating in the handshake.

(dict) --Identifies a participant in a handshake.

Id (string) --The unique identifier (ID) for the party.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Type (string) --The type of party.





State (string) --The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

REQUESTED : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond.
OPEN : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action.
CANCELED : This handshake is no longer active because it was canceled by the originating account.
ACCEPTED : This handshake is complete because it has been accepted by the recipient.
DECLINED : This handshake is no longer active because it was declined by the recipient account.
EXPIRED : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days).


RequestedTimestamp (datetime) --The date and time that the handshake request was made.

ExpirationTimestamp (datetime) --The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

Action (string) --The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

INVITE : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts.
ENABLE_ALL_FEATURES : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only invited member accounts. Created accounts do not receive this because those accounts were created by the organization\'s master account and approval is inferred.
APPROVE_ALL_FEATURES : This type of handshake is sent from the Organizations service when all member accounts have approved the ENABLE_ALL_FEATURES invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features.


Resources (list) --Additional information that is needed to process the handshake.

(dict) --Contains additional data that is needed to process a handshake.

Value (string) --The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

Type (string) --The type of information being passed, specifying how the value is to be interpreted by the other party:

ACCOUNT - Specifies an AWS account ID number.
ORGANIZATION - Specifies an organization ID number.
EMAIL - Specifies the email address that is associated with the account that receives the handshake.
OWNER_EMAIL - Specifies the email address associated with the master account. Included as information about an organization.
OWNER_NAME - Specifies the name associated with the master account. Included as information about an organization.
NOTES - Additional text provided by the handshake initiator and intended for the recipient to read.


Resources (list) --When needed, contains an additional array of HandshakeResource objects.












Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.HandshakeNotFoundException
Organizations.Client.exceptions.InvalidHandshakeTransitionException
Organizations.Client.exceptions.HandshakeAlreadyInStateException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
Bill previously sent an invitation to Susan\'s account to join his organization. He changes his mind and decides to cancel the invitation before Susan accepts it. The following example shows Bill\'s cancellation:
response = client.cancel_handshake(
    HandshakeId='h-examplehandshakeid111',
)

print(response)


Expected Output:
{
    'Handshake': {
        'Action': 'INVITE',
        'Arn': 'arn:aws:organizations::111111111111:handshake/o-exampleorgid/invite/h-examplehandshakeid111',
        'ExpirationTimestamp': datetime(2017, 2, 28, 12, 15, 0, 1, 59, 0),
        'Id': 'h-examplehandshakeid111',
        'Parties': [
            {
                'Id': 'o-exampleorgid',
                'Type': 'ORGANIZATION',
            },
            {
                'Id': 'susan@example.com',
                'Type': 'EMAIL',
            },
        ],
        'RequestedTimestamp': datetime(2017, 2, 14, 12, 15, 0, 1, 45, 0),
        'Resources': [
            {
                'Resources': [
                    {
                        'Type': 'MASTER_EMAIL',
                        'Value': 'bill@example.com',
                    },
                    {
                        'Type': 'MASTER_NAME',
                        'Value': 'Master Account',
                    },
                    {
                        'Type': 'ORGANIZATION_FEATURE_SET',
                        'Value': 'CONSOLIDATED_BILLING',
                    },
                ],
                'Type': 'ORGANIZATION',
                'Value': 'o-exampleorgid',
            },
            {
                'Type': 'ACCOUNT',
                'Value': '222222222222',
            },
            {
                'Type': 'NOTES',
                'Value': 'This is a request for Susan's account to join Bob's organization.',
            },
        ],
        'State': 'CANCELED',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
            'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
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
    INVITE : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts.
    ENABLE_ALL_FEATURES : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only invited member accounts. Created accounts do not receive this because those accounts were created by the organization\'s master account and approval is inferred.
    APPROVE_ALL_FEATURES : This type of handshake is sent from the Organizations service when all member accounts have approved the ENABLE_ALL_FEATURES invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features.
    
    """
    pass

def create_account(Email=None, AccountName=None, RoleName=None, IamUserAccessToBilling=None):
    """
    Creates an AWS account that is automatically a member of the organization whose credentials made the request. This is an asynchronous request that AWS performs in the background. Because CreateAccount operates asynchronously, it can return a successful completion message even though account initialization might still be in progress. You might need to wait a few minutes before you can successfully access the account. To check the status of the request, do one of the following:
    The user who calls the API to create an account must have the organizations:CreateAccount permission. If you enabled all features in the organization, AWS Organizations creates the required service-linked role named AWSServiceRoleForOrganizations . For more information, see AWS Organizations and Service-Linked Roles in the AWS Organizations User Guide .
    AWS Organizations preconfigures the new member account with a role (named OrganizationAccountAccessRole by default) that grants users in the master account administrator permissions in the new member account. Principals in the master account can assume the role. AWS Organizations clones the company name and address information for the new account from the organization\'s master account.
    This operation can be called only from the organization\'s master account.
    For more information about creating accounts, see Creating an AWS Account in Your Organization in the AWS Organizations User Guide.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The owner of an organization creates a member account in the organization. The following example shows that when the organization owner creates the member account, the account is preconfigured with the name "Production Account" and an owner email address of susan@example.com.  An IAM role is automatically created using the default name because the roleName parameter is not used. AWS Organizations sends Susan a "Welcome to AWS" email:
    Expected Output:
    
    :example: response = client.create_account(
        Email='string',
        AccountName='string',
        RoleName='string',
        IamUserAccessToBilling='ALLOW'|'DENY'
    )
    
    
    :type Email: string
    :param Email: [REQUIRED]\nThe email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account. You must use a valid email address to complete account creation. You can\'t access the root user of the account or remove an account that was created with an invalid email address.\n

    :type AccountName: string
    :param AccountName: [REQUIRED]\nThe friendly name of the member account.\n

    :type RoleName: string
    :param RoleName: (Optional)\nThe name of an IAM role that AWS Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account.\nIf you don\'t specify this parameter, the role name defaults to OrganizationAccountAccessRole .\nFor more information about how to use this role to access the member account, see the following links:\n\nAccessing and Administering the Member Accounts in Your Organization in the AWS Organizations User Guide\nSteps 2 and 3 in Tutorial: Delegate Access Across AWS Accounts Using IAM Roles in the IAM User Guide\n\nThe regex pattern that is used to validate this parameter. The pattern can include uppercase letters, lowercase letters, digits with no spaces, and any of the following characters: =,.@-\n

    :type IamUserAccessToBilling: string
    :param IamUserAccessToBilling: If set to ALLOW , the new account enables IAM users to access account billing information if they have the required permissions. If set to DENY , only the root user of the new account can access account billing information. For more information, see Activating Access to the Billing and Cost Management Console in the AWS Billing and Cost Management User Guide .\nIf you don\'t specify this parameter, the value defaults to ALLOW , and IAM users and roles with the required permissions can access billing information for the new account.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CreateAccountStatus': {
        'Id': 'string',
        'AccountName': 'string',
        'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
        'RequestedTimestamp': datetime(2015, 1, 1),
        'CompletedTimestamp': datetime(2015, 1, 1),
        'AccountId': 'string',
        'GovCloudAccountId': 'string',
        'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'CONCURRENT_ACCOUNT_MODIFICATION'|'INTERNAL_FAILURE'|'GOVCLOUD_ACCOUNT_ALREADY_EXISTS'
    }
}


Response Structure

(dict) --

CreateAccountStatus (dict) --
A structure that contains details about the request to create an account. This response structure might not be fully populated when you first receive it because account creation is an asynchronous process. You can pass the returned CreateAccountStatus ID as a parameter to  DescribeCreateAccountStatus to get status about the progress of the request at later times. You can also check the AWS CloudTrail log for the CreateAccountResult event. For more information, see Monitoring the Activity in Your Organization in the AWS Organizations User Guide .

Id (string) --
The unique identifier (ID) that references this request. You get this value from the response of the initial  CreateAccount request to create the account.
The regex pattern for a create account request ID string requires "car-" followed by from 8 to 32 lower-case letters or digits.

AccountName (string) --
The account name given to the account when it was created.

State (string) --
The status of the request.

RequestedTimestamp (datetime) --
The date and time that the request was made for the account creation.

CompletedTimestamp (datetime) --
The date and time that the account was created and the request completed.

AccountId (string) --
If the account was created successfully, the unique identifier (ID) of the new account.
The regex pattern for an account ID string requires exactly 12 digits.

GovCloudAccountId (string) --
If the account was created successfully, the unique identifier (ID) of the new account in the AWS GovCloud (US) Region.

FailureReason (string) --
If the request failed, a description of the reason for the failure.

ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the limit on the number of accounts in your organization.
EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with that email address already exists.
GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not be created because this Region already includes an account with that email address.
INVALID_ADDRESS: The account could not be created because the address you provided is not valid.
INVALID_EMAIL: The account could not be created because the email address you provided is not valid.
INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Customer Support.










Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.ConstraintViolationException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.FinalizingOrganizationException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.UnsupportedAPIEndpointException

Examples
The owner of an organization creates a member account in the organization. The following example shows that when the organization owner creates the member account, the account is preconfigured with the name "Production Account" and an owner email address of susan@example.com.  An IAM role is automatically created using the default name because the roleName parameter is not used. AWS Organizations sends Susan a "Welcome to AWS" email:
response = client.create_account(
    AccountName='Production Account',
    Email='susan@example.com',
)

print(response)


Expected Output:
{
    'CreateAccountStatus': {
        'Id': 'car-examplecreateaccountrequestid111',
        'State': 'IN_PROGRESS',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CreateAccountStatus': {
            'Id': 'string',
            'AccountName': 'string',
            'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
            'RequestedTimestamp': datetime(2015, 1, 1),
            'CompletedTimestamp': datetime(2015, 1, 1),
            'AccountId': 'string',
            'GovCloudAccountId': 'string',
            'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'CONCURRENT_ACCOUNT_MODIFICATION'|'INTERNAL_FAILURE'|'GOVCLOUD_ACCOUNT_ALREADY_EXISTS'
        }
    }
    
    
    :returns: 
    When you create an account in an organization using the AWS Organizations console, API, or CLI commands, the information required for the account to operate as a standalone account, such as a payment method and signing the end user license agreement (EULA) is not automatically collected. If you must remove an account from your organization later, you can do so only after you provide the missing information. Follow the steps at To leave an organization as a member account in the AWS Organizations User Guide .
    If you get an exception that indicates that you exceeded your account limits for the organization, contact AWS Support .
    If you get an exception that indicates that the operation failed because your organization is still initializing, wait one hour and then try again. If the error persists, contact AWS Support .
    Using CreateAccount to create multiple temporary accounts isn\'t recommended. You can only close an account from the Billing and Cost Management Console, and you must be signed in as the root user. For information on the requirements and process for closing an account, see Closing an AWS Account in the AWS Organizations User Guide .
    
    """
    pass

def create_gov_cloud_account(Email=None, AccountName=None, RoleName=None, IamUserAccessToBilling=None):
    """
    This action is available if all of the following are true:
    AWS automatically enables AWS CloudTrail for AWS GovCloud (US) accounts, but you should also do the following:
    You call this action from the master account of your organization in the commercial Region to create a standalone AWS account in the AWS GovCloud (US) Region. After the account is created, the master account of an organization in the AWS GovCloud (US) Region can invite it to that organization. For more information on inviting standalone accounts in the AWS GovCloud (US) to join an organization, see AWS Organizations in the AWS GovCloud User Guide.
    Calling CreateGovCloudAccount is an asynchronous request that AWS performs in the background. Because CreateGovCloudAccount operates asynchronously, it can return a successful completion message even though account initialization might still be in progress. You might need to wait a few minutes before you can successfully access the account. To check the status of the request, do one of the following:
    When you call the CreateGovCloudAccount action, you create two accounts: a standalone account in the AWS GovCloud (US) Region and an associated account in the commercial Region for billing and support purposes. The account in the commercial Region is automatically a member of the organization whose credentials made the request. Both accounts are associated with the same email address.
    A role is created in the new account in the commercial Region that allows the master account in the organization in the commercial Region to assume it. An AWS GovCloud (US) account is then created and associated with the commercial account that you just created. A role is created in the new AWS GovCloud (US) account that can be assumed by the AWS GovCloud (US) account that is associated with the master account of the commercial organization. For more information and to view a diagram that explains how account access works, see AWS Organizations in the AWS GovCloud User Guide.
    For more information about creating accounts, see Creating an AWS Account in Your Organization in the AWS Organizations User Guide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_gov_cloud_account(
        Email='string',
        AccountName='string',
        RoleName='string',
        IamUserAccessToBilling='ALLOW'|'DENY'
    )
    
    
    :type Email: string
    :param Email: [REQUIRED]\nThe email address of the owner to assign to the new member account in the commercial Region. This email address must not already be associated with another AWS account. You must use a valid email address to complete account creation. You can\'t access the root user of the account or remove an account that was created with an invalid email address. Like all request parameters for CreateGovCloudAccount , the request for the email address for the AWS GovCloud (US) account originates from the commercial Region, not from the AWS GovCloud (US) Region.\n

    :type AccountName: string
    :param AccountName: [REQUIRED]\nThe friendly name of the member account.\n

    :type RoleName: string
    :param RoleName: (Optional)\nThe name of an IAM role that AWS Organizations automatically preconfigures in the new member accounts in both the AWS GovCloud (US) Region and in the commercial Region. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account.\nIf you don\'t specify this parameter, the role name defaults to OrganizationAccountAccessRole .\nFor more information about how to use this role to access the member account, see Accessing and Administering the Member Accounts in Your Organization in the AWS Organizations User Guide and steps 2 and 3 in Tutorial: Delegate Access Across AWS Accounts Using IAM Roles in the IAM User Guide.\nThe regex pattern that is used to validate this parameter. The pattern can include uppercase letters, lowercase letters, digits with no spaces, and any of the following characters: =,.@-\n

    :type IamUserAccessToBilling: string
    :param IamUserAccessToBilling: If set to ALLOW , the new linked account in the commercial Region enables IAM users to access account billing information if they have the required permissions. If set to DENY , only the root user of the new account can access account billing information. For more information, see Activating Access to the Billing and Cost Management Console in the AWS Billing and Cost Management User Guide.\nIf you don\'t specify this parameter, the value defaults to ALLOW , and IAM users and roles with the required permissions can access billing information for the new account.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CreateAccountStatus': {
        'Id': 'string',
        'AccountName': 'string',
        'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
        'RequestedTimestamp': datetime(2015, 1, 1),
        'CompletedTimestamp': datetime(2015, 1, 1),
        'AccountId': 'string',
        'GovCloudAccountId': 'string',
        'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'CONCURRENT_ACCOUNT_MODIFICATION'|'INTERNAL_FAILURE'|'GOVCLOUD_ACCOUNT_ALREADY_EXISTS'
    }
}


Response Structure

(dict) --

CreateAccountStatus (dict) --
Contains the status about a  CreateAccount or  CreateGovCloudAccount request to create an AWS account or an AWS GovCloud (US) account in an organization.

Id (string) --
The unique identifier (ID) that references this request. You get this value from the response of the initial  CreateAccount request to create the account.
The regex pattern for a create account request ID string requires "car-" followed by from 8 to 32 lower-case letters or digits.

AccountName (string) --
The account name given to the account when it was created.

State (string) --
The status of the request.

RequestedTimestamp (datetime) --
The date and time that the request was made for the account creation.

CompletedTimestamp (datetime) --
The date and time that the account was created and the request completed.

AccountId (string) --
If the account was created successfully, the unique identifier (ID) of the new account.
The regex pattern for an account ID string requires exactly 12 digits.

GovCloudAccountId (string) --
If the account was created successfully, the unique identifier (ID) of the new account in the AWS GovCloud (US) Region.

FailureReason (string) --
If the request failed, a description of the reason for the failure.

ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the limit on the number of accounts in your organization.
EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with that email address already exists.
GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not be created because this Region already includes an account with that email address.
INVALID_ADDRESS: The account could not be created because the address you provided is not valid.
INVALID_EMAIL: The account could not be created because the email address you provided is not valid.
INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Customer Support.










Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.ConstraintViolationException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.FinalizingOrganizationException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.UnsupportedAPIEndpointException


    :return: {
        'CreateAccountStatus': {
            'Id': 'string',
            'AccountName': 'string',
            'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
            'RequestedTimestamp': datetime(2015, 1, 1),
            'CompletedTimestamp': datetime(2015, 1, 1),
            'AccountId': 'string',
            'GovCloudAccountId': 'string',
            'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'CONCURRENT_ACCOUNT_MODIFICATION'|'INTERNAL_FAILURE'|'GOVCLOUD_ACCOUNT_ALREADY_EXISTS'
        }
    }
    
    
    :returns: 
    Verify that AWS CloudTrail is enabled to store logs.
    Create an S3 bucket for AWS CloudTrail log storage. For more information, see Verifying AWS CloudTrail Is Enabled in the AWS GovCloud User Guide .
    
    """
    pass

def create_organization(FeatureSet=None):
    """
    Creates an AWS organization. The account whose user is calling the CreateOrganization operation automatically becomes the master account of the new organization.
    This operation must be called using credentials from the account that is to become the new organization\'s master account. The principal must also have the relevant IAM permissions.
    By default (or if you set the FeatureSet parameter to ALL ), the new organization is created with all features enabled and service control policies automatically enabled in the root. If you instead choose to create the organization supporting only the consolidated billing features by setting the FeatureSet parameter to CONSOLIDATED_BILLING" , no policy types are enabled by default, and you can\'t use organization policies
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Bill wants to create an organization using credentials from account 111111111111. The following example shows that the account becomes the master account in the new organization. Because he does not specify a feature set, the new organization defaults to all features enabled and service control policies enabled on the root:
    Expected Output:
    In the following example, Bill creates an organization using credentials from account 111111111111, and configures the organization to support only the consolidated billing feature set:
    Expected Output:
    
    :example: response = client.create_organization(
        FeatureSet='ALL'|'CONSOLIDATED_BILLING'
    )
    
    
    :type FeatureSet: string
    :param FeatureSet: Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.\n\nCONSOLIDATED_BILLING : All member accounts have their bills consolidated to and paid by the master account. For more information, see Consolidated billing in the AWS Organizations User Guide.  The consolidated billing feature subset isn\'t available for organizations in the AWS GovCloud (US) Region.\nALL : In addition to all the features supported by the consolidated billing feature set, the master account can also apply any policy type to any member account in the organization. For more information, see All features in the AWS Organizations User Guide.\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'Organization': {
        'Id': 'string',
        'Arn': 'string',
        'FeatureSet': 'ALL'|'CONSOLIDATED_BILLING',
        'MasterAccountArn': 'string',
        'MasterAccountId': 'string',
        'MasterAccountEmail': 'string',
        'AvailablePolicyTypes': [
            {
                'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
                'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
            },
        ]
    }
}


Response Structure

(dict) --
Organization (dict) --A structure that contains details about the newly created organization.

Id (string) --The unique identifier (ID) of an organization.
The regex pattern for an organization ID string requires "o-" followed by from 10 to 32 lower-case letters or digits.

Arn (string) --The Amazon Resource Name (ARN) of an organization.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

FeatureSet (string) --Specifies the functionality that currently is available to the organization. If set to "ALL", then all features are enabled and policies can be applied to accounts in the organization. If set to "CONSOLIDATED_BILLING", then only consolidated billing functionality is available. For more information, see Enabling All Features in Your Organization in the AWS Organizations User Guide .

MasterAccountArn (string) --The Amazon Resource Name (ARN) of the account that is designated as the master account for the organization.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

MasterAccountId (string) --The unique identifier (ID) of the master account of an organization.
The regex pattern for an account ID string requires exactly 12 digits.

MasterAccountEmail (string) --The email address that is associated with the AWS account that is designated as the master account for the organization.

AvailablePolicyTypes (list) --A list of policy types that are enabled for this organization. For example, if your organization has all features enabled, then service control policies (SCPs) are included in the list.

Note
Even if a policy type is shown as available in the organization, you can separately enable and disable them at the root level by using  EnablePolicyType and  DisablePolicyType . Use  ListRoots to see the status of a policy type in that root.


(dict) --Contains information about a policy type and its status in the associated root.

Type (string) --The name of the policy type.

Status (string) --The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.












Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AlreadyInOrganizationException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.ConstraintViolationException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.AccessDeniedForDependencyException

Examples
Bill wants to create an organization using credentials from account 111111111111. The following example shows that the account becomes the master account in the new organization. Because he does not specify a feature set, the new organization defaults to all features enabled and service control policies enabled on the root:
response = client.create_organization(
)

print(response)


Expected Output:
{
    'Organization': {
        'Arn': 'arn:aws:organizations::111111111111:organization/o-exampleorgid',
        'AvailablePolicyTypes': [
            {
                'Status': 'ENABLED',
                'Type': 'SERVICE_CONTROL_POLICY',
            },
        ],
        'FeatureSet': 'ALL',
        'Id': 'o-exampleorgid',
        'MasterAccountArn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/111111111111',
        'MasterAccountEmail': 'bill@example.com',
        'MasterAccountId': '111111111111',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}


In the following example, Bill creates an organization using credentials from account 111111111111, and configures the organization to support only the consolidated billing feature set:
response = client.create_organization(
    FeatureSet='CONSOLIDATED_BILLING',
)

print(response)


Expected Output:
{
    'Organization': {
        'Arn': 'arn:aws:organizations::111111111111:organization/o-exampleorgid',
        'AvailablePolicyTypes': [
        ],
        'FeatureSet': 'CONSOLIDATED_BILLING',
        'Id': 'o-exampleorgid',
        'MasterAccountArn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/111111111111',
        'MasterAccountEmail': 'bill@example.com',
        'MasterAccountId': '111111111111',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                    'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
                    'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                },
            ]
        }
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AlreadyInOrganizationException
    Organizations.Client.exceptions.ConcurrentModificationException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.AccessDeniedForDependencyException
    
    """
    pass

def create_organizational_unit(ParentId=None, Name=None):
    """
    Creates an organizational unit (OU) within a root or parent OU. An OU is a container for accounts that enables you to organize your accounts to apply policies according to your business requirements. The number of levels deep that you can nest OUs is dependent upon the policy types enabled for that root. For service control policies, the limit is five.
    For more information about OUs, see Managing Organizational Units in the AWS Organizations User Guide.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to create an OU that is named AccountingOU. The new OU is directly under the root.:
    Expected Output:
    
    :example: response = client.create_organizational_unit(
        ParentId='string',
        Name='string'
    )
    
    
    :type ParentId: string
    :param ParentId: [REQUIRED]\nThe unique identifier (ID) of the parent root or OU that you want to create the new OU in.\nThe regex pattern for a parent ID string requires one of the following:\n\nRoot - A string that begins with 'r-' followed by from 4 to 32 lowercase letters or digits.\nOrganizational unit (OU) - A string that begins with 'ou-' followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second '-' dash and from 8 to 32 additional lowercase letters or digits.\n\n

    :type Name: string
    :param Name: [REQUIRED]\nThe friendly name to assign to the new OU.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OrganizationalUnit': {
        'Id': 'string',
        'Arn': 'string',
        'Name': 'string'
    }
}


Response Structure

(dict) --

OrganizationalUnit (dict) --
A structure that contains details about the newly created OU.

Id (string) --
The unique identifier (ID) associated with this OU.
The regex pattern for an organizational unit ID string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU). This string is followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.

Arn (string) --
The Amazon Resource Name (ARN) of this OU.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Name (string) --
The friendly name of this OU.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.









Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.ConstraintViolationException
Organizations.Client.exceptions.DuplicateOrganizationalUnitException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ParentNotFoundException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows how to create an OU that is named AccountingOU. The new OU is directly under the root.:
response = client.create_organizational_unit(
    Name='AccountingOU',
    ParentId='r-examplerootid111',
)

print(response)


Expected Output:
{
    'OrganizationalUnit': {
        'Arn': 'arn:aws:organizations::111111111111:ou/o-exampleorgid/ou-examplerootid111-exampleouid111',
        'Id': 'ou-examplerootid111-exampleouid111',
        'Name': 'AccountingOU',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'OrganizationalUnit': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        }
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.ConcurrentModificationException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.DuplicateOrganizationalUnitException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.ParentNotFoundException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    
    """
    pass

def create_policy(Content=None, Description=None, Name=None, Type=None):
    """
    Creates a policy of a specified type that you can attach to a root, an organizational unit (OU), or an individual AWS account.
    For more information about policies and their use, see Managing Organization Policies .
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to create a service control policy (SCP) that is named AllowAllS3Actions. The JSON string in the content parameter specifies the content in the policy. The parameter string is escaped with backslashes to ensure that the embedded double quotes in the JSON policy are treated as literals in the parameter, which itself is surrounded by double quotes:
    Expected Output:
    
    :example: response = client.create_policy(
        Content='string',
        Description='string',
        Name='string',
        Type='SERVICE_CONTROL_POLICY'|'TAG_POLICY'
    )
    
    
    :type Content: string
    :param Content: [REQUIRED]\nThe policy content to add to the new policy. For example, if you create a service control policy (SCP), this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see Service Control Policy Syntax in the AWS Organizations User Guide.\n

    :type Description: string
    :param Description: [REQUIRED]\nAn optional description to assign to the policy.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe friendly name to assign to the policy.\nThe regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.\n

    :type Type: string
    :param Type: [REQUIRED]\nThe type of policy to create.\n\nNote\nIn the current release, the only type of policy that you can create is a service control policy (SCP).\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Policy': {
        'PolicySummary': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
            'AwsManaged': True|False
        },
        'Content': 'string'
    }
}


Response Structure

(dict) --

Policy (dict) --
A structure that contains details about the newly created policy.

PolicySummary (dict) --
A structure that contains additional details about the policy.

Id (string) --
The unique identifier (ID) of the policy.
The regex pattern for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

Arn (string) --
The Amazon Resource Name (ARN) of the policy.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Name (string) --
The friendly name of the policy.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.

Description (string) --
The description of the policy.

Type (string) --
The type of policy.

AwsManaged (boolean) --
A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.



Content (string) --
The text content of the policy.









Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.ConstraintViolationException
Organizations.Client.exceptions.DuplicatePolicyException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.MalformedPolicyDocumentException
Organizations.Client.exceptions.PolicyTypeNotAvailableForOrganizationException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.UnsupportedAPIEndpointException

Examples
The following example shows how to create a service control policy (SCP) that is named AllowAllS3Actions. The JSON string in the content parameter specifies the content in the policy. The parameter string is escaped with backslashes to ensure that the embedded double quotes in the JSON policy are treated as literals in the parameter, which itself is surrounded by double quotes:
response = client.create_policy(
    Content='{\\"Version\\":\\"2012-10-17\\",\\"Statement\\":{\\"Effect\\":\\"Allow\\",\\"Action\\":\\"s3:*\\"}}',
    Description='Enables admins of attached accounts to delegate all S3 permissions',
    Name='AllowAllS3Actions',
    Type='SERVICE_CONTROL_POLICY',
)

print(response)


Expected Output:
{
    'Policy': {
        'Content': '{"Version":"2012-10-17","Statement":{"Effect":"Allow","Action":"s3:*"}}',
        'PolicySummary': {
            'Arn': 'arn:aws:organizations::111111111111:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111',
            'Description': 'Allows delegation of all S3 actions',
            'Name': 'AllowAllS3Actions',
            'Type': 'SERVICE_CONTROL_POLICY',
        },
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Policy': {
            'PolicySummary': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
                'AwsManaged': True|False
            },
            'Content': 'string'
        }
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.ConcurrentModificationException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.DuplicatePolicyException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.MalformedPolicyDocumentException
    Organizations.Client.exceptions.PolicyTypeNotAvailableForOrganizationException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.UnsupportedAPIEndpointException
    
    """
    pass

def decline_handshake(HandshakeId=None):
    """
    Declines a handshake request. This sets the handshake state to DECLINED and effectively deactivates the request.
    This operation can be called only from the account that received the handshake. The originator of the handshake can use  CancelHandshake instead. The originator can\'t reactivate a declined request, but can reinitiate the process with a new handshake request.
    After you decline a handshake, it continues to appear in the results of relevant APIs for only 30 days. After that, it\'s deleted.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows Susan declining an invitation to join Bill\'s organization. The DeclineHandshake operation returns a handshake object, showing that the state is now DECLINED:
    Expected Output:
    
    :example: response = client.decline_handshake(
        HandshakeId='string'
    )
    
    
    :type HandshakeId: string
    :param HandshakeId: [REQUIRED]\nThe unique identifier (ID) of the handshake that you want to decline. You can get the ID from the ListHandshakesForAccount operation.\nThe regex pattern for handshake ID string requires 'h-' followed by from 8 to 32 lowercase letters or digits.\n

    :rtype: dict
ReturnsResponse Syntax{
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
        'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
        'Resources': [
            {
                'Value': 'string',
                'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                'Resources': {'... recursive ...'}
            },
        ]
    }
}


Response Structure

(dict) --
Handshake (dict) --A structure that contains details about the declined handshake. The state is updated to show the value DECLINED .

Id (string) --The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Arn (string) --The Amazon Resource Name (ARN) of a handshake.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Parties (list) --Information about the two accounts that are participating in the handshake.

(dict) --Identifies a participant in a handshake.

Id (string) --The unique identifier (ID) for the party.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Type (string) --The type of party.





State (string) --The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

REQUESTED : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond.
OPEN : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action.
CANCELED : This handshake is no longer active because it was canceled by the originating account.
ACCEPTED : This handshake is complete because it has been accepted by the recipient.
DECLINED : This handshake is no longer active because it was declined by the recipient account.
EXPIRED : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days).


RequestedTimestamp (datetime) --The date and time that the handshake request was made.

ExpirationTimestamp (datetime) --The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

Action (string) --The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

INVITE : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts.
ENABLE_ALL_FEATURES : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only invited member accounts. Created accounts do not receive this because those accounts were created by the organization\'s master account and approval is inferred.
APPROVE_ALL_FEATURES : This type of handshake is sent from the Organizations service when all member accounts have approved the ENABLE_ALL_FEATURES invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features.


Resources (list) --Additional information that is needed to process the handshake.

(dict) --Contains additional data that is needed to process a handshake.

Value (string) --The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

Type (string) --The type of information being passed, specifying how the value is to be interpreted by the other party:

ACCOUNT - Specifies an AWS account ID number.
ORGANIZATION - Specifies an organization ID number.
EMAIL - Specifies the email address that is associated with the account that receives the handshake.
OWNER_EMAIL - Specifies the email address associated with the master account. Included as information about an organization.
OWNER_NAME - Specifies the name associated with the master account. Included as information about an organization.
NOTES - Additional text provided by the handshake initiator and intended for the recipient to read.


Resources (list) --When needed, contains an additional array of HandshakeResource objects.












Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.HandshakeNotFoundException
Organizations.Client.exceptions.InvalidHandshakeTransitionException
Organizations.Client.exceptions.HandshakeAlreadyInStateException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows Susan declining an invitation to join Bill\'s organization. The DeclineHandshake operation returns a handshake object, showing that the state is now DECLINED:
response = client.decline_handshake(
    HandshakeId='h-examplehandshakeid111',
)

print(response)


Expected Output:
{
    'Handshake': {
        'Action': 'INVITE',
        'Arn': 'arn:aws:organizations::111111111111:handshake/o-exampleorgid/invite/h-examplehandshakeid111',
        'ExpirationTimestamp': datetime(2016, 12, 15, 19, 27, 58, 3, 350, 0),
        'Id': 'h-examplehandshakeid111',
        'Parties': [
            {
                'Id': '222222222222',
                'Type': 'ACCOUNT',
            },
            {
                'Id': 'o-exampleorgid',
                'Type': 'ORGANIZATION',
            },
        ],
        'RequestedTimestamp': datetime(2016, 11, 30, 19, 27, 58, 2, 335, 0),
        'Resources': [
            {
                'Resources': [
                    {
                        'Type': 'MASTER_EMAIL',
                        'Value': 'bill@example.com',
                    },
                    {
                        'Type': 'MASTER_NAME',
                        'Value': 'Master Account',
                    },
                ],
                'Type': 'ORGANIZATION',
                'Value': 'o-exampleorgid',
            },
            {
                'Type': 'ACCOUNT',
                'Value': '222222222222',
            },
            {
                'Type': 'NOTES',
                'Value': 'This is an invitation to Susan's account to join the Bill's organization.',
            },
        ],
        'State': 'DECLINED',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
            'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
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
    INVITE : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts.
    ENABLE_ALL_FEATURES : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only invited member accounts. Created accounts do not receive this because those accounts were created by the organization\'s master account and approval is inferred.
    APPROVE_ALL_FEATURES : This type of handshake is sent from the Organizations service when all member accounts have approved the ENABLE_ALL_FEATURES invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features.
    
    """
    pass

def delete_organization():
    """
    Deletes the organization. You can delete an organization only by using credentials from the master account. The organization must be empty of member accounts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_organization()
    
    
    """
    pass

def delete_organizational_unit(OrganizationalUnitId=None):
    """
    Deletes an organizational unit (OU) from a root or another OU. You must first remove all accounts and child OUs from the OU that you want to delete.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to delete an OU. The example assumes that you previously removed all accounts and other OUs from the OU:
    Expected Output:
    
    :example: response = client.delete_organizational_unit(
        OrganizationalUnitId='string'
    )
    
    
    :type OrganizationalUnitId: string
    :param OrganizationalUnitId: [REQUIRED]\nThe unique identifier (ID) of the organizational unit that you want to delete. You can get the ID from the ListOrganizationalUnitsForParent operation.\nThe regex pattern for an organizational unit ID string requires 'ou-' followed by from 4 to 32 lowercase letters or digits (the ID of the root that contains the OU). This string is followed by a second '-' dash and from 8 to 32 additional lowercase letters or digits.\n

    :return: response = client.delete_organizational_unit(
        OrganizationalUnitId='ou-examplerootid111-exampleouid111',
    )
    
    print(response)
    
    
    """
    pass

def delete_policy(PolicyId=None):
    """
    Deletes the specified policy from your organization. Before you perform this operation, you must first detach the policy from all organizational units (OUs), roots, and accounts.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to delete a policy from an organization. The example assumes that you previously detached the policy from all entities:
    Expected Output:
    
    :example: response = client.delete_policy(
        PolicyId='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]\nThe unique identifier (ID) of the policy that you want to delete. You can get the ID from the ListPolicies or ListPoliciesForTarget operations.\nThe regex pattern for a policy ID string requires 'p-' followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).\n

    :return: response = client.delete_policy(
        PolicyId='p-examplepolicyid111',
    )
    
    print(response)
    
    
    """
    pass

def deregister_delegated_administrator(AccountId=None, ServicePrincipal=None):
    """
    Removes the specified member AWS account as a delegated administrator for the specified AWS service.
    You can run this action only for AWS services that support this feature. For a current list of services that support it, see the column Supports Delegated Administrator in the table at AWS Services that you can use with AWS Organizations in the AWS Organizations User Guide.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_delegated_administrator(
        AccountId='string',
        ServicePrincipal='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe account ID number of the member account in the organization that you want to deregister as a delegated administrator.\n

    :type ServicePrincipal: string
    :param ServicePrincipal: [REQUIRED]\nThe service principal name of an AWS service for which the account is a delegated administrator.\nDelegated administrator privileges are revoked for only the specified AWS service from the member account. If the specified service is the only service for which the member account is a delegated administrator, the operation also revokes Organizations read action permissions.\n

    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AccountNotFoundException
    Organizations.Client.exceptions.AccountNotRegisteredException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.ConcurrentModificationException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.UnsupportedAPIEndpointException
    
    """
    pass

def describe_account(AccountId=None):
    """
    Retrieves AWS Organizations-related information about the specified account.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows a user in the master account (111111111111) asking for details about account 555555555555:
    Expected Output:
    
    :example: response = client.describe_account(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe unique identifier (ID) of the AWS account that you want information about. You can get the ID from the ListAccounts or ListAccountsForParent operations.\nThe regex pattern for an account ID string requires exactly 12 digits.\n

    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --
Account (dict) --A structure that contains information about the requested account.

Id (string) --The unique identifier (ID) of the account.
The regex pattern for an account ID string requires exactly 12 digits.

Arn (string) --The Amazon Resource Name (ARN) of the account.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Email (string) --The email address associated with the AWS account.
The regex pattern for this parameter is a string of characters that represents a standard internet email address.

Name (string) --The friendly name of the account.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.

Status (string) --The status of the account in the organization.

JoinedMethod (string) --The method by which the account joined the organization.

JoinedTimestamp (datetime) --The date the account became a part of the organization.








Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AccountNotFoundException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows a user in the master account (111111111111) asking for details about account 555555555555:
response = client.describe_account(
    AccountId='555555555555',
)

print(response)


Expected Output:
{
    'Account': {
        'Arn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/555555555555',
        'Email': 'anika@example.com',
        'Id': '555555555555',
        'Name': 'Beta Account',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to request the status about a previous request to create an account in an organization. This operation can be called only by a principal from the organization\'s master account. In the example, the specified "createAccountRequestId" comes from the response of the original call to "CreateAccount":
    Expected Output:
    
    :example: response = client.describe_create_account_status(
        CreateAccountRequestId='string'
    )
    
    
    :type CreateAccountRequestId: string
    :param CreateAccountRequestId: [REQUIRED]\nSpecifies the operationId that uniquely identifies the request. You can get the ID from the response to an earlier CreateAccount request, or from the ListCreateAccountStatus operation.\nThe regex pattern for a create account request ID string requires 'car-' followed by from 8 to 32 lowercase letters or digits.\n

    :rtype: dict
ReturnsResponse Syntax{
    'CreateAccountStatus': {
        'Id': 'string',
        'AccountName': 'string',
        'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
        'RequestedTimestamp': datetime(2015, 1, 1),
        'CompletedTimestamp': datetime(2015, 1, 1),
        'AccountId': 'string',
        'GovCloudAccountId': 'string',
        'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'CONCURRENT_ACCOUNT_MODIFICATION'|'INTERNAL_FAILURE'|'GOVCLOUD_ACCOUNT_ALREADY_EXISTS'
    }
}


Response Structure

(dict) --
CreateAccountStatus (dict) --A structure that contains the current status of an account creation request.

Id (string) --The unique identifier (ID) that references this request. You get this value from the response of the initial  CreateAccount request to create the account.
The regex pattern for a create account request ID string requires "car-" followed by from 8 to 32 lower-case letters or digits.

AccountName (string) --The account name given to the account when it was created.

State (string) --The status of the request.

RequestedTimestamp (datetime) --The date and time that the request was made for the account creation.

CompletedTimestamp (datetime) --The date and time that the account was created and the request completed.

AccountId (string) --If the account was created successfully, the unique identifier (ID) of the new account.
The regex pattern for an account ID string requires exactly 12 digits.

GovCloudAccountId (string) --If the account was created successfully, the unique identifier (ID) of the new account in the AWS GovCloud (US) Region.

FailureReason (string) --If the request failed, a description of the reason for the failure.

ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the limit on the number of accounts in your organization.
EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with that email address already exists.
GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not be created because this Region already includes an account with that email address.
INVALID_ADDRESS: The account could not be created because the address you provided is not valid.
INVALID_EMAIL: The account could not be created because the email address you provided is not valid.
INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Customer Support.









Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.CreateAccountStatusNotFoundException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.UnsupportedAPIEndpointException

Examples
The following example shows how to request the status about a previous request to create an account in an organization. This operation can be called only by a principal from the organization\'s master account. In the example, the specified "createAccountRequestId" comes from the response of the original call to "CreateAccount":
response = client.describe_create_account_status(
    CreateAccountRequestId='car-exampleaccountcreationrequestid',
)

print(response)


Expected Output:
{
    'CreateAccountStatus': {
        'AccountId': '333333333333',
        'Id': 'car-exampleaccountcreationrequestid',
        'State': 'SUCCEEDED',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CreateAccountStatus': {
            'Id': 'string',
            'AccountName': 'string',
            'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
            'RequestedTimestamp': datetime(2015, 1, 1),
            'CompletedTimestamp': datetime(2015, 1, 1),
            'AccountId': 'string',
            'GovCloudAccountId': 'string',
            'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'CONCURRENT_ACCOUNT_MODIFICATION'|'INTERNAL_FAILURE'|'GOVCLOUD_ACCOUNT_ALREADY_EXISTS'
        }
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.CreateAccountStatusNotFoundException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.UnsupportedAPIEndpointException
    
    """
    pass

def describe_effective_policy(PolicyType=None, TargetId=None):
    """
    Returns the contents of the effective tag policy for the account. The effective tag policy is the aggregation of any tag policies the account inherits, plus any policy directly that is attached to the account.
    This action returns information on tag policies only.
    For more information on policy inheritance, see How Policy Inheritance Works in the AWS Organizations User Guide .
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_effective_policy(
        PolicyType='TAG_POLICY',
        TargetId='string'
    )
    
    
    :type PolicyType: string
    :param PolicyType: [REQUIRED]\nThe type of policy that you want information about.\n

    :type TargetId: string
    :param TargetId: When you\'re signed in as the master account, specify the ID of the account that you want details about. Specifying an organization root or OU as the target is not supported.

    :rtype: dict

ReturnsResponse Syntax
{
    'EffectivePolicy': {
        'PolicyContent': 'string',
        'LastUpdatedTimestamp': datetime(2015, 1, 1),
        'TargetId': 'string',
        'PolicyType': 'TAG_POLICY'
    }
}


Response Structure

(dict) --

EffectivePolicy (dict) --
The contents of the effective policy.

PolicyContent (string) --
The text content of the policy.

LastUpdatedTimestamp (datetime) --
The time of the last update to this policy.

TargetId (string) --
The account ID of the policy target.

PolicyType (string) --
The policy type.









Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConstraintViolationException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.TargetNotFoundException
Organizations.Client.exceptions.EffectivePolicyNotFoundException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.UnsupportedAPIEndpointException


    :return: {
        'EffectivePolicy': {
            'PolicyContent': 'string',
            'LastUpdatedTimestamp': datetime(2015, 1, 1),
            'TargetId': 'string',
            'PolicyType': 'TAG_POLICY'
        }
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.TargetNotFoundException
    Organizations.Client.exceptions.EffectivePolicyNotFoundException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.UnsupportedAPIEndpointException
    
    """
    pass

def describe_handshake(HandshakeId=None):
    """
    Retrieves information about a previously requested handshake. The handshake ID comes from the response to the original  InviteAccountToOrganization operation that generated the handshake.
    You can access handshakes that are ACCEPTED , DECLINED , or CANCELED for only 30 days after they change to that state. They\'re then deleted and no longer accessible.
    This operation can be called from any account in the organization.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows you how to request details about a handshake. The handshake ID comes either from the original call to "InviteAccountToOrganization", or from a call to "ListHandshakesForAccount" or "ListHandshakesForOrganization":
    Expected Output:
    
    :example: response = client.describe_handshake(
        HandshakeId='string'
    )
    
    
    :type HandshakeId: string
    :param HandshakeId: [REQUIRED]\nThe unique identifier (ID) of the handshake that you want information about. You can get the ID from the original call to InviteAccountToOrganization , or from a call to ListHandshakesForAccount or ListHandshakesForOrganization .\nThe regex pattern for handshake ID string requires 'h-' followed by from 8 to 32 lowercase letters or digits.\n

    :rtype: dict
ReturnsResponse Syntax{
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
        'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
        'Resources': [
            {
                'Value': 'string',
                'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                'Resources': {'... recursive ...'}
            },
        ]
    }
}


Response Structure

(dict) --
Handshake (dict) --A structure that contains information about the specified handshake.

Id (string) --The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Arn (string) --The Amazon Resource Name (ARN) of a handshake.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Parties (list) --Information about the two accounts that are participating in the handshake.

(dict) --Identifies a participant in a handshake.

Id (string) --The unique identifier (ID) for the party.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Type (string) --The type of party.





State (string) --The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

REQUESTED : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond.
OPEN : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action.
CANCELED : This handshake is no longer active because it was canceled by the originating account.
ACCEPTED : This handshake is complete because it has been accepted by the recipient.
DECLINED : This handshake is no longer active because it was declined by the recipient account.
EXPIRED : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days).


RequestedTimestamp (datetime) --The date and time that the handshake request was made.

ExpirationTimestamp (datetime) --The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

Action (string) --The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

INVITE : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts.
ENABLE_ALL_FEATURES : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only invited member accounts. Created accounts do not receive this because those accounts were created by the organization\'s master account and approval is inferred.
APPROVE_ALL_FEATURES : This type of handshake is sent from the Organizations service when all member accounts have approved the ENABLE_ALL_FEATURES invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features.


Resources (list) --Additional information that is needed to process the handshake.

(dict) --Contains additional data that is needed to process a handshake.

Value (string) --The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

Type (string) --The type of information being passed, specifying how the value is to be interpreted by the other party:

ACCOUNT - Specifies an AWS account ID number.
ORGANIZATION - Specifies an organization ID number.
EMAIL - Specifies the email address that is associated with the account that receives the handshake.
OWNER_EMAIL - Specifies the email address associated with the master account. Included as information about an organization.
OWNER_NAME - Specifies the name associated with the master account. Included as information about an organization.
NOTES - Additional text provided by the handshake initiator and intended for the recipient to read.


Resources (list) --When needed, contains an additional array of HandshakeResource objects.












Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.HandshakeNotFoundException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows you how to request details about a handshake. The handshake ID comes either from the original call to "InviteAccountToOrganization", or from a call to "ListHandshakesForAccount" or "ListHandshakesForOrganization":
response = client.describe_handshake(
    HandshakeId='h-examplehandshakeid111',
)

print(response)


Expected Output:
{
    'Handshake': {
        'Action': 'INVITE',
        'Arn': 'arn:aws:organizations::111111111111:handshake/o-exampleorgid/invite/h-examplehandshakeid111',
        'ExpirationTimestamp': datetime(2016, 11, 30, 17, 24, 58, 2, 335, 0),
        'Id': 'h-examplehandshakeid111',
        'Parties': [
            {
                'Id': 'o-exampleorgid',
                'Type': 'ORGANIZATION',
            },
            {
                'Id': '333333333333',
                'Type': 'ACCOUNT',
            },
        ],
        'RequestedTimestamp': datetime(2016, 11, 30, 17, 24, 58, 2, 335, 0),
        'Resources': [
            {
                'Resources': [
                    {
                        'Type': 'MASTER_EMAIL',
                        'Value': 'bill@example.com',
                    },
                    {
                        'Type': 'MASTER_NAME',
                        'Value': 'Master Account',
                    },
                ],
                'Type': 'ORGANIZATION',
                'Value': 'o-exampleorgid',
            },
            {
                'Type': 'ACCOUNT',
                'Value': '333333333333',
            },
        ],
        'State': 'OPEN',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
            'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
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
    INVITE : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts.
    ENABLE_ALL_FEATURES : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only invited member accounts. Created accounts do not receive this because those accounts were created by the organization\'s master account and approval is inferred.
    APPROVE_ALL_FEATURES : This type of handshake is sent from the Organizations service when all member accounts have approved the ENABLE_ALL_FEATURES invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features.
    
    """
    pass

def describe_organization():
    """
    Retrieves information about the organization that the user\'s account belongs to.
    This operation can be called from any account in the organization.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to request information about the current user\'s organization:/n/n
    Expected Output:
    
    :example: response = client.describe_organization()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'Organization': {
        'Id': 'string',
        'Arn': 'string',
        'FeatureSet': 'ALL'|'CONSOLIDATED_BILLING',
        'MasterAccountArn': 'string',
        'MasterAccountId': 'string',
        'MasterAccountEmail': 'string',
        'AvailablePolicyTypes': [
            {
                'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
                'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
            },
        ]
    }
}


Response Structure

(dict) --
Organization (dict) --A structure that contains information about the organization.

Id (string) --The unique identifier (ID) of an organization.
The regex pattern for an organization ID string requires "o-" followed by from 10 to 32 lower-case letters or digits.

Arn (string) --The Amazon Resource Name (ARN) of an organization.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

FeatureSet (string) --Specifies the functionality that currently is available to the organization. If set to "ALL", then all features are enabled and policies can be applied to accounts in the organization. If set to "CONSOLIDATED_BILLING", then only consolidated billing functionality is available. For more information, see Enabling All Features in Your Organization in the AWS Organizations User Guide .

MasterAccountArn (string) --The Amazon Resource Name (ARN) of the account that is designated as the master account for the organization.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

MasterAccountId (string) --The unique identifier (ID) of the master account of an organization.
The regex pattern for an account ID string requires exactly 12 digits.

MasterAccountEmail (string) --The email address that is associated with the AWS account that is designated as the master account for the organization.

AvailablePolicyTypes (list) --A list of policy types that are enabled for this organization. For example, if your organization has all features enabled, then service control policies (SCPs) are included in the list.

Note
Even if a policy type is shown as available in the organization, you can separately enable and disable them at the root level by using  EnablePolicyType and  DisablePolicyType . Use  ListRoots to see the status of a policy type in that root.


(dict) --Contains information about a policy type and its status in the associated root.

Type (string) --The name of the policy type.

Status (string) --The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.












Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows how to request information about the current user\'s organization:/n/n
response = client.describe_organization(
)

print(response)


Expected Output:
{
    'Organization': {
        'Arn': 'arn:aws:organizations::111111111111:organization/o-exampleorgid',
        'AvailablePolicyTypes': [
            {
                'Status': 'ENABLED',
                'Type': 'SERVICE_CONTROL_POLICY',
            },
        ],
        'FeatureSet': 'ALL',
        'Id': 'o-exampleorgid',
        'MasterAccountArn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/111111111111',
        'MasterAccountEmail': 'bill@example.com',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                    'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
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
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to request details about an OU:/n/n
    Expected Output:
    
    :example: response = client.describe_organizational_unit(
        OrganizationalUnitId='string'
    )
    
    
    :type OrganizationalUnitId: string
    :param OrganizationalUnitId: [REQUIRED]\nThe unique identifier (ID) of the organizational unit that you want details about. You can get the ID from the ListOrganizationalUnitsForParent operation.\nThe regex pattern for an organizational unit ID string requires 'ou-' followed by from 4 to 32 lowercase letters or digits (the ID of the root that contains the OU). This string is followed by a second '-' dash and from 8 to 32 additional lowercase letters or digits.\n

    :rtype: dict
ReturnsResponse Syntax{
    'OrganizationalUnit': {
        'Id': 'string',
        'Arn': 'string',
        'Name': 'string'
    }
}


Response Structure

(dict) --
OrganizationalUnit (dict) --A structure that contains details about the specified OU.

Id (string) --The unique identifier (ID) associated with this OU.
The regex pattern for an organizational unit ID string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU). This string is followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.

Arn (string) --The Amazon Resource Name (ARN) of this OU.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Name (string) --The friendly name of this OU.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.








Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.OrganizationalUnitNotFoundException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows how to request details about an OU:/n/n
response = client.describe_organizational_unit(
    OrganizationalUnitId='ou-examplerootid111-exampleouid111',
)

print(response)


Expected Output:
{
    'OrganizationalUnit': {
        'Arn': 'arn:aws:organizations::111111111111:ou/o-exampleorgid/ou-examplerootid111-exampleouid111',
        'Id': 'ou-examplerootid111-exampleouid111',
        'Name': 'Accounting Group',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to request information about a policy:/n/n
    Expected Output:
    
    :example: response = client.describe_policy(
        PolicyId='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]\nThe unique identifier (ID) of the policy that you want details about. You can get the ID from the ListPolicies or ListPoliciesForTarget operations.\nThe regex pattern for a policy ID string requires 'p-' followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).\n

    :rtype: dict
ReturnsResponse Syntax{
    'Policy': {
        'PolicySummary': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
            'AwsManaged': True|False
        },
        'Content': 'string'
    }
}


Response Structure

(dict) --
Policy (dict) --A structure that contains details about the specified policy.

PolicySummary (dict) --A structure that contains additional details about the policy.

Id (string) --The unique identifier (ID) of the policy.
The regex pattern for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

Arn (string) --The Amazon Resource Name (ARN) of the policy.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Name (string) --The friendly name of the policy.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.

Description (string) --The description of the policy.

Type (string) --The type of policy.

AwsManaged (boolean) --A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.



Content (string) --The text content of the policy.








Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.PolicyNotFoundException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.UnsupportedAPIEndpointException

Examples
The following example shows how to request information about a policy:/n/n
response = client.describe_policy(
    PolicyId='p-examplepolicyid111',
)

print(response)


Expected Output:
{
    'Policy': {
        'Content': '{\
  \\"Version\\": \\"2012-10-17\\",\
  \\"Statement\\": [\
    {\
      \\"Effect\\": \\"Allow\\",\
      \\"Action\\": \\"*\\",\
      \\"Resource\\": \\"*\\"\
    }\
  ]\
}',
        'PolicySummary': {
            'Arn': 'arn:aws:organizations::111111111111:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111',
            'AwsManaged': False,
            'Description': 'Enables admins to delegate S3 permissions',
            'Id': 'p-examplepolicyid111',
            'Name': 'AllowAllS3Actions',
            'Type': 'SERVICE_CONTROL_POLICY',
        },
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Policy': {
            'PolicySummary': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
                'AwsManaged': True|False
            },
            'Content': 'string'
        }
    }
    
    
    """
    pass

def detach_policy(PolicyId=None, TargetId=None):
    """
    Detaches a policy from a target root, organizational unit (OU), or account. If the policy being detached is a service control policy (SCP), the changes to permissions for IAM users and roles in affected accounts are immediate.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to detach a policy from an OU:/n/n
    Expected Output:
    
    :example: response = client.detach_policy(
        PolicyId='string',
        TargetId='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]\nThe unique identifier (ID) of the policy you want to detach. You can get the ID from the ListPolicies or ListPoliciesForTarget operations.\nThe regex pattern for a policy ID string requires 'p-' followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).\n

    :type TargetId: string
    :param TargetId: [REQUIRED]\nThe unique identifier (ID) of the root, OU, or account that you want to detach the policy from. You can get the ID from the ListRoots , ListOrganizationalUnitsForParent , or ListAccounts operations.\nThe regex pattern for a target ID string requires one of the following:\n\nRoot - A string that begins with 'r-' followed by from 4 to 32 lowercase letters or digits.\nAccount - A string that consists of exactly 12 digits.\nOrganizational unit (OU) - A string that begins with 'ou-' followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second '-' dash and from 8 to 32 additional lowercase letters or digits.\n\n

    :return: response = client.detach_policy(
        PolicyId='p-examplepolicyid111',
        TargetId='ou-examplerootid111-exampleouid111',
    )
    
    print(response)
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.ConcurrentModificationException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.PolicyNotAttachedException
    Organizations.Client.exceptions.PolicyNotFoundException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TargetNotFoundException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.UnsupportedAPIEndpointException
    Organizations.Client.exceptions.PolicyChangesInProgressException
    
    """
    pass

def disable_aws_service_access(ServicePrincipal=None):
    """
    Disables the integration of an AWS service (the service that is specified by ServicePrincipal ) with AWS Organizations. When you disable integration, the specified service no longer can create a service-linked role in new accounts in your organization. This means the service can\'t perform operations on your behalf on any new accounts in your organization. The service can still perform operations in older accounts until the service completes its clean-up from AWS Organizations.
    After you perform the DisableAWSServiceAccess operation, the specified service can no longer perform operations in your organization\'s accounts unless the operations are explicitly permitted by the IAM policies that are attached to your roles.
    For more information about integrating other services with AWS Organizations, including the list of services that work with Organizations, see Integrating AWS Organizations with Other AWS Services in the AWS Organizations User Guide.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_aws_service_access(
        ServicePrincipal='string'
    )
    
    
    :type ServicePrincipal: string
    :param ServicePrincipal: [REQUIRED]\nThe service principal name of the AWS service for which you want to disable integration with your organization. This is typically in the form of a URL, such as `` service-abbreviation .amazonaws.com`` .\n

    """
    pass

def disable_policy_type(RootId=None, PolicyType=None):
    """
    Disables an organizational control policy type in a root. A policy of a certain type can be attached to entities in a root only if that type is enabled in the root. After you perform this operation, you no longer can attach policies of the specified type to that root or to any organizational unit (OU) or account in that root. You can undo this by using the  EnablePolicyType operation.
    This is an asynchronous request that AWS performs in the background. If you disable a policy for a root, it still appears enabled for the organization if all features are enabled for the organization. AWS recommends that you first use  ListRoots to see the status of policy types for a specified root, and then use this operation.
    This operation can be called only from the organization\'s master account.
    To view the status of available policy types in the organization, use  DescribeOrganization .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to disable the service control policy (SCP) policy type in a root. The response shows that the PolicyTypes response element no longer includes SERVICE_CONTROL_POLICY:/n/n
    Expected Output:
    
    :example: response = client.disable_policy_type(
        RootId='string',
        PolicyType='SERVICE_CONTROL_POLICY'|'TAG_POLICY'
    )
    
    
    :type RootId: string
    :param RootId: [REQUIRED]\nThe unique identifier (ID) of the root in which you want to disable a policy type. You can get the ID from the ListRoots operation.\nThe regex pattern for a root ID string requires 'r-' followed by from 4 to 32 lowercase letters or digits.\n

    :type PolicyType: string
    :param PolicyType: [REQUIRED]\nThe policy type that you want to disable in this root.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Root': {
        'Id': 'string',
        'Arn': 'string',
        'Name': 'string',
        'PolicyTypes': [
            {
                'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
                'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
            },
        ]
    }
}


Response Structure

(dict) --

Root (dict) --
A structure that shows the root with the updated list of enabled policy types.

Id (string) --
The unique identifier (ID) for the root.
The regex pattern for a root ID string requires "r-" followed by from 4 to 32 lower-case letters or digits.

Arn (string) --
The Amazon Resource Name (ARN) of the root.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Name (string) --
The friendly name of the root.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.

PolicyTypes (list) --
The types of policies that are currently enabled for the root and therefore can be attached to the root or to its OUs or accounts.

Note
Even if a policy type is shown as available in the organization, you can separately enable and disable them at the root level by using  EnablePolicyType and  DisablePolicyType . Use  DescribeOrganization to see the availability of the policy types in that organization.


(dict) --
Contains information about a policy type and its status in the associated root.

Type (string) --
The name of the policy type.

Status (string) --
The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.













Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.ConstraintViolationException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.PolicyTypeNotEnabledException
Organizations.Client.exceptions.RootNotFoundException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.UnsupportedAPIEndpointException
Organizations.Client.exceptions.PolicyChangesInProgressException

Examples
The following example shows how to disable the service control policy (SCP) policy type in a root. The response shows that the PolicyTypes response element no longer includes SERVICE_CONTROL_POLICY:/n/n
response = client.disable_policy_type(
    PolicyType='SERVICE_CONTROL_POLICY',
    RootId='r-examplerootid111',
)

print(response)


Expected Output:
{
    'Root': {
        'Arn': 'arn:aws:organizations::111111111111:root/o-exampleorgid/r-examplerootid111',
        'Id': 'r-examplerootid111',
        'Name': 'Root',
        'PolicyTypes': [
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Root': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'PolicyTypes': [
                {
                    'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
                    'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                },
            ]
        }
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.ConcurrentModificationException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.PolicyTypeNotEnabledException
    Organizations.Client.exceptions.RootNotFoundException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.UnsupportedAPIEndpointException
    Organizations.Client.exceptions.PolicyChangesInProgressException
    
    """
    pass

def enable_all_features():
    """
    Enables all features in an organization. This enables the use of organization policies that can restrict the services and actions that can be called in each account. Until you enable all features, you have access only to consolidated billing, and you can\'t use any of the advanced account administration features that AWS Organizations supports. For more information, see Enabling All Features in Your Organization in the AWS Organizations User Guide.
    After you enable all features, you can separately enable or disable individual policy types in a root using  EnablePolicyType and  DisablePolicyType . To see the status of policy types in a root, use  ListRoots .
    After all invited member accounts accept the handshake, you finalize the feature set change by accepting the handshake that contains "Action": "ENABLE_ALL_FEATURES" . This completes the change.
    After you enable all features in your organization, the master account in the organization can apply policies on all member accounts. These policies can restrict what users and even administrators in those accounts can do. The master account can apply policies that prevent accounts from leaving the organization. Ensure that your account administrators are aware of this.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example shows the administrator asking all the invited accounts in the organization to approve enabling all features in the organization. AWS Organizations sends an email to the address that is registered with every invited member account asking the owner to approve the change by accepting the handshake that is sent. After all invited member accounts accept the handshake, the organization administrator can finalize the change to enable all features, and those with appropriate permissions can create policies and apply them to roots, OUs, and accounts:/n/n
    Expected Output:
    
    :example: response = client.enable_all_features()
    
    
    :rtype: dict
ReturnsResponse Syntax{
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
        'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
        'Resources': [
            {
                'Value': 'string',
                'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                'Resources': {'... recursive ...'}
            },
        ]
    }
}


Response Structure

(dict) --
Handshake (dict) --A structure that contains details about the handshake created to support this request to enable all features in the organization.

Id (string) --The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Arn (string) --The Amazon Resource Name (ARN) of a handshake.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Parties (list) --Information about the two accounts that are participating in the handshake.

(dict) --Identifies a participant in a handshake.

Id (string) --The unique identifier (ID) for the party.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Type (string) --The type of party.





State (string) --The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

REQUESTED : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond.
OPEN : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action.
CANCELED : This handshake is no longer active because it was canceled by the originating account.
ACCEPTED : This handshake is complete because it has been accepted by the recipient.
DECLINED : This handshake is no longer active because it was declined by the recipient account.
EXPIRED : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days).


RequestedTimestamp (datetime) --The date and time that the handshake request was made.

ExpirationTimestamp (datetime) --The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

Action (string) --The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

INVITE : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts.
ENABLE_ALL_FEATURES : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only invited member accounts. Created accounts do not receive this because those accounts were created by the organization\'s master account and approval is inferred.
APPROVE_ALL_FEATURES : This type of handshake is sent from the Organizations service when all member accounts have approved the ENABLE_ALL_FEATURES invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features.


Resources (list) --Additional information that is needed to process the handshake.

(dict) --Contains additional data that is needed to process a handshake.

Value (string) --The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

Type (string) --The type of information being passed, specifying how the value is to be interpreted by the other party:

ACCOUNT - Specifies an AWS account ID number.
ORGANIZATION - Specifies an organization ID number.
EMAIL - Specifies the email address that is associated with the account that receives the handshake.
OWNER_EMAIL - Specifies the email address associated with the master account. Included as information about an organization.
OWNER_NAME - Specifies the name associated with the master account. Included as information about an organization.
NOTES - Additional text provided by the handshake initiator and intended for the recipient to read.


Resources (list) --When needed, contains an additional array of HandshakeResource objects.












Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.HandshakeConstraintViolationException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
This example shows the administrator asking all the invited accounts in the organization to approve enabling all features in the organization. AWS Organizations sends an email to the address that is registered with every invited member account asking the owner to approve the change by accepting the handshake that is sent. After all invited member accounts accept the handshake, the organization administrator can finalize the change to enable all features, and those with appropriate permissions can create policies and apply them to roots, OUs, and accounts:/n/n
response = client.enable_all_features(
)

print(response)


Expected Output:
{
    'Handshake': {
        'Action': 'ENABLE_ALL_FEATURES',
        'Arn': 'arn:aws:organizations::111111111111:handshake/o-exampleorgid/enable_all_features/h-examplehandshakeid111',
        'ExpirationTimestamp': datetime(2017, 2, 28, 9, 35, 40, 1, 59, 0),
        'Id': 'h-examplehandshakeid111',
        'Parties': [
            {
                'Id': 'o-exampleorgid',
                'Type': 'ORGANIZATION',
            },
        ],
        'RequestedTimestamp': datetime(2017, 2, 13, 9, 35, 40, 0, 44, 0),
        'Resources': [
            {
                'Type': 'ORGANIZATION',
                'Value': 'o-exampleorgid',
            },
        ],
        'State': 'REQUESTED',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
            'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
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
    INVITE : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts.
    ENABLE_ALL_FEATURES : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only invited member accounts. Created accounts do not receive this because those accounts were created by the organization\'s master account and approval is inferred.
    APPROVE_ALL_FEATURES : This type of handshake is sent from the Organizations service when all member accounts have approved the ENABLE_ALL_FEATURES invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features.
    
    """
    pass

def enable_aws_service_access(ServicePrincipal=None):
    """
    Enables the integration of an AWS service (the service that is specified by ServicePrincipal ) with AWS Organizations. When you enable integration, you allow the specified service to create a service-linked role in all the accounts in your organization. This allows the service to perform operations on your behalf in your organization and its accounts.
    For more information about enabling services to integrate with AWS Organizations, see Integrating AWS Organizations with Other AWS Services in the AWS Organizations User Guide.
    This operation can be called only from the organization\'s master account and only if the organization has enabled all features .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_aws_service_access(
        ServicePrincipal='string'
    )
    
    
    :type ServicePrincipal: string
    :param ServicePrincipal: [REQUIRED]\nThe service principal name of the AWS service for which you want to enable integration with your organization. This is typically in the form of a URL, such as `` service-abbreviation .amazonaws.com`` .\n

    """
    pass

def enable_policy_type(RootId=None, PolicyType=None):
    """
    Enables a policy type in a root. After you enable a policy type in a root, you can attach policies of that type to the root, any organizational unit (OU), or account in that root. You can undo this by using the  DisablePolicyType operation.
    This is an asynchronous request that AWS performs in the background. AWS recommends that you first use  ListRoots to see the status of policy types for a specified root, and then use this operation.
    This operation can be called only from the organization\'s master account.
    You can enable a policy type in a root only if that policy type is available in the organization. To view the status of available policy types in the organization, use  DescribeOrganization .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to enable the service control policy (SCP) policy type in a root. The output shows a root object with a PolicyTypes response element showing that SCPs are now enabled:/n/n
    Expected Output:
    
    :example: response = client.enable_policy_type(
        RootId='string',
        PolicyType='SERVICE_CONTROL_POLICY'|'TAG_POLICY'
    )
    
    
    :type RootId: string
    :param RootId: [REQUIRED]\nThe unique identifier (ID) of the root in which you want to enable a policy type. You can get the ID from the ListRoots operation.\nThe regex pattern for a root ID string requires 'r-' followed by from 4 to 32 lowercase letters or digits.\n

    :type PolicyType: string
    :param PolicyType: [REQUIRED]\nThe policy type that you want to enable.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Root': {
        'Id': 'string',
        'Arn': 'string',
        'Name': 'string',
        'PolicyTypes': [
            {
                'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
                'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
            },
        ]
    }
}


Response Structure

(dict) --

Root (dict) --
A structure that shows the root with the updated list of enabled policy types.

Id (string) --
The unique identifier (ID) for the root.
The regex pattern for a root ID string requires "r-" followed by from 4 to 32 lower-case letters or digits.

Arn (string) --
The Amazon Resource Name (ARN) of the root.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Name (string) --
The friendly name of the root.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.

PolicyTypes (list) --
The types of policies that are currently enabled for the root and therefore can be attached to the root or to its OUs or accounts.

Note
Even if a policy type is shown as available in the organization, you can separately enable and disable them at the root level by using  EnablePolicyType and  DisablePolicyType . Use  DescribeOrganization to see the availability of the policy types in that organization.


(dict) --
Contains information about a policy type and its status in the associated root.

Type (string) --
The name of the policy type.

Status (string) --
The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.













Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.ConstraintViolationException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.PolicyTypeAlreadyEnabledException
Organizations.Client.exceptions.RootNotFoundException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.PolicyTypeNotAvailableForOrganizationException
Organizations.Client.exceptions.UnsupportedAPIEndpointException
Organizations.Client.exceptions.PolicyChangesInProgressException

Examples
The following example shows how to enable the service control policy (SCP) policy type in a root. The output shows a root object with a PolicyTypes response element showing that SCPs are now enabled:/n/n
response = client.enable_policy_type(
    PolicyType='SERVICE_CONTROL_POLICY',
    RootId='r-examplerootid111',
)

print(response)


Expected Output:
{
    'Root': {
        'Arn': 'arn:aws:organizations::111111111111:root/o-exampleorgid/r-examplerootid111',
        'Id': 'r-examplerootid111',
        'Name': 'Root',
        'PolicyTypes': [
            {
                'Status': 'ENABLED',
                'Type': 'SERVICE_CONTROL_POLICY',
            },
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Root': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'PolicyTypes': [
                {
                    'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
                    'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                },
            ]
        }
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.ConcurrentModificationException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.PolicyTypeAlreadyEnabledException
    Organizations.Client.exceptions.RootNotFoundException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.PolicyTypeNotAvailableForOrganizationException
    Organizations.Client.exceptions.UnsupportedAPIEndpointException
    Organizations.Client.exceptions.PolicyChangesInProgressException
    
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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def invite_account_to_organization(Target=None, Notes=None):
    """
    Sends an invitation to another account to join your organization as a member account. AWS Organizations sends email on your behalf to the email address that is associated with the other account\'s owner. The invitation is implemented as a  Handshake whose details are in the response.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows the admin of the master account owned by bill@example.com inviting the account owned by juan@example.com to join an organization.
    Expected Output:
    
    :example: response = client.invite_account_to_organization(
        Target={
            'Id': 'string',
            'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
        },
        Notes='string'
    )
    
    
    :type Target: dict
    :param Target: [REQUIRED]\nThe identifier (ID) of the AWS account that you want to invite to join your organization. This is a JSON object that contains the following elements:\n\n{ 'Type': 'ACCOUNT', 'Id': '<* **account id number** * >' }\nIf you use the AWS CLI, you can submit this as a single string, similar to the following example:\n\n--target Id=123456789012,Type=ACCOUNT\nIf you specify 'Type': 'ACCOUNT' , you must provide the AWS account ID number as the Id . If you specify 'Type': 'EMAIL' , you must specify the email address that is associated with the account.\n\n--target Id=diego@example.com,Type=EMAIL\n\nId (string) -- [REQUIRED]The unique identifier (ID) for the party.\nThe regex pattern for handshake ID string requires 'h-' followed by from 8 to 32 lower-case letters or digits.\n\nType (string) -- [REQUIRED]The type of party.\n\n\n

    :type Notes: string
    :param Notes: Additional information that you want to include in the generated email to the recipient account owner.

    :rtype: dict

ReturnsResponse Syntax
{
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
        'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
        'Resources': [
            {
                'Value': 'string',
                'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                'Resources': {'... recursive ...'}
            },
        ]
    }
}


Response Structure

(dict) --

Handshake (dict) --
A structure that contains details about the handshake that is created to support this invitation request.

Id (string) --
The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Arn (string) --
The Amazon Resource Name (ARN) of a handshake.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Parties (list) --
Information about the two accounts that are participating in the handshake.

(dict) --
Identifies a participant in a handshake.

Id (string) --
The unique identifier (ID) for the party.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Type (string) --
The type of party.





State (string) --
The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

REQUESTED : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond.
OPEN : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action.
CANCELED : This handshake is no longer active because it was canceled by the originating account.
ACCEPTED : This handshake is complete because it has been accepted by the recipient.
DECLINED : This handshake is no longer active because it was declined by the recipient account.
EXPIRED : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days).


RequestedTimestamp (datetime) --
The date and time that the handshake request was made.

ExpirationTimestamp (datetime) --
The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

Action (string) --
The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

INVITE : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts.
ENABLE_ALL_FEATURES : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only invited member accounts. Created accounts do not receive this because those accounts were created by the organization\'s master account and approval is inferred.
APPROVE_ALL_FEATURES : This type of handshake is sent from the Organizations service when all member accounts have approved the ENABLE_ALL_FEATURES invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features.


Resources (list) --
Additional information that is needed to process the handshake.

(dict) --
Contains additional data that is needed to process a handshake.

Value (string) --
The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

Type (string) --
The type of information being passed, specifying how the value is to be interpreted by the other party:

ACCOUNT - Specifies an AWS account ID number.
ORGANIZATION - Specifies an organization ID number.
EMAIL - Specifies the email address that is associated with the account that receives the handshake.
OWNER_EMAIL - Specifies the email address associated with the master account. Included as information about an organization.
OWNER_NAME - Specifies the name associated with the master account. Included as information about an organization.
NOTES - Additional text provided by the handshake initiator and intended for the recipient to read.


Resources (list) --
When needed, contains an additional array of HandshakeResource objects.













Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.AccountOwnerNotVerifiedException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.HandshakeConstraintViolationException
Organizations.Client.exceptions.DuplicateHandshakeException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.FinalizingOrganizationException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows the admin of the master account owned by bill@example.com inviting the account owned by juan@example.com to join an organization.
response = client.invite_account_to_organization(
    Notes='This is a request for Juan's account to join Bill's organization',
    Target={
        'Id': 'juan@example.com',
        'Type': 'EMAIL',
    },
)

print(response)


Expected Output:
{
    'Handshake': {
        'Action': 'INVITE',
        'Arn': 'arn:aws:organizations::111111111111:handshake/o-exampleorgid/invite/h-examplehandshakeid111',
        'ExpirationTimestamp': datetime(2017, 2, 16, 9, 36, 5, 3, 47, 0),
        'Id': 'h-examplehandshakeid111',
        'Parties': [
            {
                'Id': 'o-exampleorgid',
                'Type': 'ORGANIZATION',
            },
            {
                'Id': 'juan@example.com',
                'Type': 'EMAIL',
            },
        ],
        'RequestedTimestamp': datetime(2017, 2, 1, 9, 36, 5, 2, 32, 0),
        'Resources': [
            {
                'Resources': [
                    {
                        'Type': 'MASTER_EMAIL',
                        'Value': 'bill@amazon.com',
                    },
                    {
                        'Type': 'MASTER_NAME',
                        'Value': 'Org Master Account',
                    },
                    {
                        'Type': 'ORGANIZATION_FEATURE_SET',
                        'Value': 'FULL',
                    },
                ],
                'Type': 'ORGANIZATION',
                'Value': 'o-exampleorgid',
            },
            {
                'Type': 'EMAIL',
                'Value': 'juan@example.com',
            },
        ],
        'State': 'OPEN',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
            'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
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
    Target (dict) -- [REQUIRED]
    The identifier (ID) of the AWS account that you want to invite to join your organization. This is a JSON object that contains the following elements:
    
    { "Type": "ACCOUNT", "Id": "<* **account id number** * >" }
    If you use the AWS CLI, you can submit this as a single string, similar to the following example:
    
    --target Id=123456789012,Type=ACCOUNT
    If you specify "Type": "ACCOUNT" , you must provide the AWS account ID number as the Id . If you specify "Type": "EMAIL" , you must specify the email address that is associated with the account.
    
    --target Id=diego@example.com,Type=EMAIL
    
    Id (string) -- [REQUIRED]The unique identifier (ID) for the party.
    The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.
    
    Type (string) -- [REQUIRED]The type of party.
    
    
    
    Notes (string) -- Additional information that you want to include in the generated email to the recipient account owner.
    
    """
    pass

def leave_organization():
    """
    Removes a member account from its parent organization. This version of the operation is performed by the account that wants to leave. To remove a member account as a user in the master account, use  RemoveAccountFromOrganization instead.
    This operation can be called only from a member account in the organization.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    TThe following example shows how to remove your member account from an organization:
    Expected Output:
    
    :example: response = client.leave_organization()
    
    
    :return: response = client.leave_organization(
    )
    
    print(response)
    
    
    :returns: 
    You can leave an organization only after you enable IAM user access to billing in your account. For more information, see Activating Access to the Billing and Cost Management Console in the AWS Billing and Cost Management User Guide.
    
    """
    pass

def list_accounts(NextToken=None, MaxResults=None):
    """
    Lists all the accounts in the organization. To request only the accounts in a specified root or organizational unit (OU), use the  ListAccountsForParent operation instead.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows you how to request a list of the accounts in an organization:
    Expected Output:
    
    :example: response = client.list_accounts(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Accounts (list) --
A list of objects in the organization.

(dict) --
Contains information about an AWS account that is a member of an organization.

Id (string) --
The unique identifier (ID) of the account.
The regex pattern for an account ID string requires exactly 12 digits.

Arn (string) --
The Amazon Resource Name (ARN) of the account.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Email (string) --
The email address associated with the AWS account.
The regex pattern for this parameter is a string of characters that represents a standard internet email address.

Name (string) --
The friendly name of the account.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.

Status (string) --
The status of the account in the organization.

JoinedMethod (string) --
The method by which the account joined the organization.

JoinedTimestamp (datetime) --
The date the account became a part of the organization.





NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows you how to request a list of the accounts in an organization:
response = client.list_accounts(
)

print(response)


Expected Output:
{
    'Accounts': [
        {
            'Arn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/111111111111',
            'Email': 'bill@example.com',
            'Id': '111111111111',
            'JoinedMethod': 'INVITED',
            'JoinedTimestamp': datetime(2016, 12, 15, 19, 30, 15, 3, 350, 0),
            'Name': 'Master Account',
            'Status': 'ACTIVE',
        },
        {
            'Arn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/222222222222',
            'Email': 'alice@example.com',
            'Id': '222222222222',
            'JoinedMethod': 'INVITED',
            'JoinedTimestamp': datetime(2016, 12, 15, 21, 2, 21, 3, 350, 0),
            'Name': 'Developer Account',
            'Status': 'ACTIVE',
        },
        {
            'Arn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/333333333333',
            'Email': 'juan@example.com',
            'Id': '333333333333',
            'JoinedMethod': 'INVITED',
            'JoinedTimestamp': datetime(2016, 12, 15, 21, 3, 47, 3, 350, 0),
            'Name': 'Test Account',
            'Status': 'ACTIVE',
        },
        {
            'Arn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/444444444444',
            'Email': 'anika@example.com',
            'Id': '444444444444',
            'JoinedMethod': 'INVITED',
            'JoinedTimestamp': datetime(2016, 12, 15, 21, 3, 32, 3, 350, 0),
            'Name': 'Production Account',
            'Status': 'ACTIVE',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_accounts_for_parent(ParentId=None, NextToken=None, MaxResults=None):
    """
    Lists the accounts in an organization that are contained by the specified target root or organizational unit (OU). If you specify the root, you get a list of all the accounts that aren\'t in any OU. If you specify an OU, you get a list of all the accounts in only that OU and not in any child OUs. To get a list of all accounts in the organization, use the  ListAccounts operation.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to request a list of the accounts in an OU:/n/n
    Expected Output:
    
    :example: response = client.list_accounts_for_parent(
        ParentId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ParentId: string
    :param ParentId: [REQUIRED]\nThe unique identifier (ID) for the parent root or organization unit (OU) whose accounts you want to list.\n

    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Accounts (list) --
A list of the accounts in the specified root or OU.

(dict) --
Contains information about an AWS account that is a member of an organization.

Id (string) --
The unique identifier (ID) of the account.
The regex pattern for an account ID string requires exactly 12 digits.

Arn (string) --
The Amazon Resource Name (ARN) of the account.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Email (string) --
The email address associated with the AWS account.
The regex pattern for this parameter is a string of characters that represents a standard internet email address.

Name (string) --
The friendly name of the account.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.

Status (string) --
The status of the account in the organization.

JoinedMethod (string) --
The method by which the account joined the organization.

JoinedTimestamp (datetime) --
The date the account became a part of the organization.





NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ParentNotFoundException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows how to request a list of the accounts in an OU:/n/n
response = client.list_accounts_for_parent(
    ParentId='ou-examplerootid111-exampleouid111',
)

print(response)


Expected Output:
{
    'Accounts': [
        {
            'Arn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/333333333333',
            'Email': 'juan@example.com',
            'Id': '333333333333',
            'JoinedMethod': 'INVITED',
            'JoinedTimestamp': 1481835795.536,
            'Name': 'Development Account',
            'Status': 'ACTIVE',
        },
        {
            'Arn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/444444444444',
            'Email': 'anika@example.com',
            'Id': '444444444444',
            'JoinedMethod': 'INVITED',
            'JoinedTimestamp': 1481835812.143,
            'Name': 'Test Account',
            'Status': 'ACTIVE',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.ParentNotFoundException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_aws_service_access_for_organization(NextToken=None, MaxResults=None):
    """
    Returns a list of the AWS services that you enabled to integrate with your organization. After a service on this list creates the resources that it requires for the integration, it can perform operations on your organization and its accounts.
    For more information about integrating other services with AWS Organizations, including the list of services that currently work with Organizations, see Integrating AWS Organizations with Other AWS Services in the AWS Organizations User Guide.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_aws_service_access_for_organization(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'EnabledServicePrincipals': [
        {
            'ServicePrincipal': 'string',
            'DateEnabled': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

EnabledServicePrincipals (list) --
A list of the service principals for the services that are enabled to integrate with your organization. Each principal is a structure that includes the name and the date that it was enabled for integration with AWS Organizations.

(dict) --
A structure that contains details of a service principal that represents an AWS service that is enabled to integrate with AWS Organizations.

ServicePrincipal (string) --
The name of the service principal. This is typically in the form of a URL, such as: `` servicename .amazonaws.com`` .

DateEnabled (datetime) --
The date that the service principal was enabled for integration with AWS Organizations.





NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConstraintViolationException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException


    :return: {
        'EnabledServicePrincipals': [
            {
                'ServicePrincipal': 'string',
                'DateEnabled': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_children(ParentId=None, ChildType=None, NextToken=None, MaxResults=None):
    """
    Lists all of the organizational units (OUs) or accounts that are contained in the specified parent OU or root. This operation, along with  ListParents enables you to traverse the tree structure that makes up this root.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to request a list of the child OUs in a parent root or OU:/n/n
    Expected Output:
    
    :example: response = client.list_children(
        ParentId='string',
        ChildType='ACCOUNT'|'ORGANIZATIONAL_UNIT',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ParentId: string
    :param ParentId: [REQUIRED]\nThe unique identifier (ID) for the parent root or OU whose children you want to list.\nThe regex pattern for a parent ID string requires one of the following:\n\nRoot - A string that begins with 'r-' followed by from 4 to 32 lowercase letters or digits.\nOrganizational unit (OU) - A string that begins with 'ou-' followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second '-' dash and from 8 to 32 additional lowercase letters or digits.\n\n

    :type ChildType: string
    :param ChildType: [REQUIRED]\nFilters the output to include only the specified child type.\n

    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Children': [
        {
            'Id': 'string',
            'Type': 'ACCOUNT'|'ORGANIZATIONAL_UNIT'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Children (list) --
The list of children of the specified parent container.

(dict) --
Contains a list of child entities, either OUs or accounts.

Id (string) --
The unique identifier (ID) of this child entity.
The regex pattern for a child ID string requires one of the following:

Account: A string that consists of exactly 12 digits.
Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU). This string is followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.


Type (string) --
The type of this child entity.





NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ParentNotFoundException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows how to request a list of the child OUs in a parent root or OU:/n/n
response = client.list_children(
    ChildType='ORGANIZATIONAL_UNIT',
    ParentId='ou-examplerootid111-exampleouid111',
)

print(response)


Expected Output:
{
    'Children': [
        {
            'Id': 'ou-examplerootid111-exampleouid111',
            'Type': 'ORGANIZATIONAL_UNIT',
        },
        {
            'Id': 'ou-examplerootid111-exampleouid222',
            'Type': 'ORGANIZATIONAL_UNIT',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    Account: A string that consists of exactly 12 digits.
    Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU). This string is followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    
    """
    pass

def list_create_account_status(States=None, NextToken=None, MaxResults=None):
    """
    Lists the account creation requests that match the specified status that is currently being tracked for the organization.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows a user requesting a list of only the completed account creation requests made for the current organization:
    Expected Output:
    The following example shows a user requesting a list of only the in-progress account creation requests made for the current organization:
    Expected Output:
    
    :example: response = client.list_create_account_status(
        States=[
            'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type States: list
    :param States: A list of one or more states that you want included in the response. If this parameter isn\'t present, all requests are included in the response.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'CreateAccountStatuses': [
        {
            'Id': 'string',
            'AccountName': 'string',
            'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
            'RequestedTimestamp': datetime(2015, 1, 1),
            'CompletedTimestamp': datetime(2015, 1, 1),
            'AccountId': 'string',
            'GovCloudAccountId': 'string',
            'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'CONCURRENT_ACCOUNT_MODIFICATION'|'INTERNAL_FAILURE'|'GOVCLOUD_ACCOUNT_ALREADY_EXISTS'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

CreateAccountStatuses (list) --
A list of objects with details about the requests. Certain elements, such as the accountId number, are present in the output only after the account has been successfully created.

(dict) --
Contains the status about a  CreateAccount or  CreateGovCloudAccount request to create an AWS account or an AWS GovCloud (US) account in an organization.

Id (string) --
The unique identifier (ID) that references this request. You get this value from the response of the initial  CreateAccount request to create the account.
The regex pattern for a create account request ID string requires "car-" followed by from 8 to 32 lower-case letters or digits.

AccountName (string) --
The account name given to the account when it was created.

State (string) --
The status of the request.

RequestedTimestamp (datetime) --
The date and time that the request was made for the account creation.

CompletedTimestamp (datetime) --
The date and time that the account was created and the request completed.

AccountId (string) --
If the account was created successfully, the unique identifier (ID) of the new account.
The regex pattern for an account ID string requires exactly 12 digits.

GovCloudAccountId (string) --
If the account was created successfully, the unique identifier (ID) of the new account in the AWS GovCloud (US) Region.

FailureReason (string) --
If the request failed, a description of the reason for the failure.

ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the limit on the number of accounts in your organization.
EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with that email address already exists.
GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not be created because this Region already includes an account with that email address.
INVALID_ADDRESS: The account could not be created because the address you provided is not valid.
INVALID_EMAIL: The account could not be created because the email address you provided is not valid.
INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Customer Support.






NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.UnsupportedAPIEndpointException

Examples
The following example shows a user requesting a list of only the completed account creation requests made for the current organization:
response = client.list_create_account_status(
    States=[
        'SUCCEEDED',
    ],
)

print(response)


Expected Output:
{
    'CreateAccountStatuses': [
        {
            'AccountId': '444444444444',
            'AccountName': 'Developer Test Account',
            'CompletedTimestamp': datetime(2017, 1, 15, 13, 45, 23, 6, 15, 0),
            'Id': 'car-exampleaccountcreationrequestid1',
            'RequestedTimestamp': datetime(2017, 1, 15, 13, 45, 23, 6, 15, 0),
            'State': 'SUCCEEDED',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example shows a user requesting a list of only the in-progress account creation requests made for the current organization:
response = client.list_create_account_status(
    States=[
        'IN_PROGRESS',
    ],
)

print(response)


Expected Output:
{
    'CreateAccountStatuses': [
        {
            'AccountName': 'Production Account',
            'Id': 'car-exampleaccountcreationrequestid2',
            'RequestedTimestamp': datetime(2017, 1, 15, 13, 45, 23, 6, 15, 0),
            'State': 'IN_PROGRESS',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CreateAccountStatuses': [
            {
                'Id': 'string',
                'AccountName': 'string',
                'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                'RequestedTimestamp': datetime(2015, 1, 1),
                'CompletedTimestamp': datetime(2015, 1, 1),
                'AccountId': 'string',
                'GovCloudAccountId': 'string',
                'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'CONCURRENT_ACCOUNT_MODIFICATION'|'INTERNAL_FAILURE'|'GOVCLOUD_ACCOUNT_ALREADY_EXISTS'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the limit on the number of accounts in your organization.
    EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with that email address already exists.
    GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the AWS GovCloud (US) Region could not be created because this Region already includes an account with that email address.
    INVALID_ADDRESS: The account could not be created because the address you provided is not valid.
    INVALID_EMAIL: The account could not be created because the email address you provided is not valid.
    INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Customer Support.
    
    """
    pass

def list_delegated_administrators(ServicePrincipal=None, NextToken=None, MaxResults=None):
    """
    Lists the AWS accounts that are designated as delegated administrators in this organization.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_delegated_administrators(
        ServicePrincipal='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServicePrincipal: string
    :param ServicePrincipal: Specifies a service principal name. If specified, then the operation lists the delegated administrators only for the specified service.\nIf you don\'t specify a service principal, the operation lists all delegated administrators for all services in your organization.\n

    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'DelegatedAdministrators': [
        {
            'Id': 'string',
            'Arn': 'string',
            'Email': 'string',
            'Name': 'string',
            'Status': 'ACTIVE'|'SUSPENDED',
            'JoinedMethod': 'INVITED'|'CREATED',
            'JoinedTimestamp': datetime(2015, 1, 1),
            'DelegationEnabledDate': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

DelegatedAdministrators (list) --
The list of delegated administrators in your organization.

(dict) --
Contains information about the delegated administrator.

Id (string) --
The unique identifier (ID) of the delegated administrator\'s account.

Arn (string) --
The Amazon Resource Name (ARN) of the delegated administrator\'s account.

Email (string) --
The email address that is associated with the delegated administrator\'s AWS account.

Name (string) --
The friendly name of the delegated administrator\'s account.

Status (string) --
The status of the delegated administrator\'s account in the organization.

JoinedMethod (string) --
The method by which the delegated administrator\'s account joined the organization.

JoinedTimestamp (datetime) --
The date when the delegated administrator\'s account became a part of the organization.

DelegationEnabledDate (datetime) --
The date when the account was made a delegated administrator.





NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConstraintViolationException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.UnsupportedAPIEndpointException


    :return: {
        'DelegatedAdministrators': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Email': 'string',
                'Name': 'string',
                'Status': 'ACTIVE'|'SUSPENDED',
                'JoinedMethod': 'INVITED'|'CREATED',
                'JoinedTimestamp': datetime(2015, 1, 1),
                'DelegationEnabledDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.UnsupportedAPIEndpointException
    
    """
    pass

def list_delegated_services_for_account(AccountId=None, NextToken=None, MaxResults=None):
    """
    List the AWS services for which the specified account is a delegated administrator.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_delegated_services_for_account(
        AccountId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe account ID number of a delegated administrator account in the organization.\n

    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'DelegatedServices': [
        {
            'ServicePrincipal': 'string',
            'DelegationEnabledDate': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

DelegatedServices (list) --
The services for which the account is a delegated administrator.

(dict) --
Contains information about the AWS service for which the account is a delegated administrator.

ServicePrincipal (string) --
The name of a service that can request an operation for the specified service. This is typically in the form of a URL, such as: `` servicename .amazonaws.com`` .

DelegationEnabledDate (datetime) --
The date that the account became a delegated administrator for this service.





NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AccountNotFoundException
Organizations.Client.exceptions.AccountNotRegisteredException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConstraintViolationException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.UnsupportedAPIEndpointException


    :return: {
        'DelegatedServices': [
            {
                'ServicePrincipal': 'string',
                'DelegationEnabledDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AccountNotFoundException
    Organizations.Client.exceptions.AccountNotRegisteredException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.UnsupportedAPIEndpointException
    
    """
    pass

def list_handshakes_for_account(Filter=None, NextToken=None, MaxResults=None):
    """
    Lists the current handshakes that are associated with the account of the requesting user.
    Handshakes that are ACCEPTED , DECLINED , or CANCELED appear in the results of this API for only 30 days after changing to that state. After that, they\'re deleted and no longer accessible.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows you how to get a list of handshakes that are associated with the account of the credentials used to call the operation:
    Expected Output:
    
    :example: response = client.list_handshakes_for_account(
        Filter={
            'ActionType': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
            'ParentHandshakeId': 'string'
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters the handshakes that you want included in the response. The default is all types. Use the ActionType element to limit the output to only a specified type, such as INVITE , ENABLE_ALL_FEATURES , or APPROVE_ALL_FEATURES . Alternatively, for the ENABLE_ALL_FEATURES handshake that generates a separate child handshake for each member account, you can specify ParentHandshakeId to see only the handshakes that were generated by that parent request.\n\nActionType (string) --Specifies the type of handshake action.\nIf you specify ActionType , you cannot also specify ParentHandshakeId .\n\nParentHandshakeId (string) --Specifies the parent handshake. Only used for handshake types that are a child of another type.\nIf you specify ParentHandshakeId , you cannot also specify ActionType .\nThe regex pattern for handshake ID string requires 'h-' followed by from 8 to 32 lower-case letters or digits.\n\n\n

    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
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


Response Structure

(dict) --

Handshakes (list) --
A list of  Handshake objects with details about each of the handshakes that is associated with the specified account.

(dict) --
Contains information that must be exchanged to securely establish a relationship between two accounts (an originator and a recipient ). For example, when a master account (the originator) invites another account (the recipient) to join its organization, the two accounts exchange information as a series of handshake requests and responses.

Note: Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30 days after entering that state After that they are deleted.


Id (string) --
The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Arn (string) --
The Amazon Resource Name (ARN) of a handshake.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Parties (list) --
Information about the two accounts that are participating in the handshake.

(dict) --
Identifies a participant in a handshake.

Id (string) --
The unique identifier (ID) for the party.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Type (string) --
The type of party.





State (string) --
The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

REQUESTED : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond.
OPEN : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action.
CANCELED : This handshake is no longer active because it was canceled by the originating account.
ACCEPTED : This handshake is complete because it has been accepted by the recipient.
DECLINED : This handshake is no longer active because it was declined by the recipient account.
EXPIRED : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days).


RequestedTimestamp (datetime) --
The date and time that the handshake request was made.

ExpirationTimestamp (datetime) --
The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

Action (string) --
The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

INVITE : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts.
ENABLE_ALL_FEATURES : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only invited member accounts. Created accounts do not receive this because those accounts were created by the organization\'s master account and approval is inferred.
APPROVE_ALL_FEATURES : This type of handshake is sent from the Organizations service when all member accounts have approved the ENABLE_ALL_FEATURES invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features.


Resources (list) --
Additional information that is needed to process the handshake.

(dict) --
Contains additional data that is needed to process a handshake.

Value (string) --
The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

Type (string) --
The type of information being passed, specifying how the value is to be interpreted by the other party:

ACCOUNT - Specifies an AWS account ID number.
ORGANIZATION - Specifies an organization ID number.
EMAIL - Specifies the email address that is associated with the account that receives the handshake.
OWNER_EMAIL - Specifies the email address associated with the master account. Included as information about an organization.
OWNER_NAME - Specifies the name associated with the master account. Included as information about an organization.
NOTES - Additional text provided by the handshake initiator and intended for the recipient to read.


Resources (list) --
When needed, contains an additional array of HandshakeResource objects.









NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows you how to get a list of handshakes that are associated with the account of the credentials used to call the operation:
response = client.list_handshakes_for_account(
)

print(response)


Expected Output:
{
    'Handshakes': [
        {
            'Action': 'INVITE',
            'Arn': 'arn:aws:organizations::111111111111:handshake/o-exampleorgid/invite/h-examplehandshakeid111',
            'ExpirationTimestamp': datetime(2017, 1, 28, 14, 35, 23, 5, 28, 0),
            'Id': 'h-examplehandshakeid111',
            'Parties': [
                {
                    'Id': 'o-exampleorgid',
                    'Type': 'ORGANIZATION',
                },
                {
                    'Id': 'juan@example.com',
                    'Type': 'EMAIL',
                },
            ],
            'RequestedTimestamp': datetime(2017, 1, 13, 14, 35, 23, 4, 13, 0),
            'Resources': [
                {
                    'Resources': [
                        {
                            'Type': 'MASTER_EMAIL',
                            'Value': 'bill@amazon.com',
                        },
                        {
                            'Type': 'MASTER_NAME',
                            'Value': 'Org Master Account',
                        },
                        {
                            'Type': 'ORGANIZATION_FEATURE_SET',
                            'Value': 'FULL',
                        },
                    ],
                    'Type': 'ORGANIZATION',
                    'Value': 'o-exampleorgid',
                },
                {
                    'Type': 'EMAIL',
                    'Value': 'juan@example.com',
                },
            ],
            'State': 'OPEN',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
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
    Handshakes that are ACCEPTED , DECLINED , or CANCELED appear in the results of this API for only 30 days after changing to that state. After that, they\'re deleted and no longer accessible.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows you how to get a list of handshakes associated with the current organization:
    Expected Output:
    
    :example: response = client.list_handshakes_for_organization(
        Filter={
            'ActionType': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
            'ParentHandshakeId': 'string'
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: A filter of the handshakes that you want included in the response. The default is all types. Use the ActionType element to limit the output to only a specified type, such as INVITE , ENABLE-ALL-FEATURES , or APPROVE-ALL-FEATURES . Alternatively, for the ENABLE-ALL-FEATURES handshake that generates a separate child handshake for each member account, you can specify the ParentHandshakeId to see only the handshakes that were generated by that parent request.\n\nActionType (string) --Specifies the type of handshake action.\nIf you specify ActionType , you cannot also specify ParentHandshakeId .\n\nParentHandshakeId (string) --Specifies the parent handshake. Only used for handshake types that are a child of another type.\nIf you specify ParentHandshakeId , you cannot also specify ActionType .\nThe regex pattern for handshake ID string requires 'h-' followed by from 8 to 32 lower-case letters or digits.\n\n\n

    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
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


Response Structure

(dict) --

Handshakes (list) --
A list of  Handshake objects with details about each of the handshakes that are associated with an organization.

(dict) --
Contains information that must be exchanged to securely establish a relationship between two accounts (an originator and a recipient ). For example, when a master account (the originator) invites another account (the recipient) to join its organization, the two accounts exchange information as a series of handshake requests and responses.

Note: Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30 days after entering that state After that they are deleted.


Id (string) --
The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Arn (string) --
The Amazon Resource Name (ARN) of a handshake.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Parties (list) --
Information about the two accounts that are participating in the handshake.

(dict) --
Identifies a participant in a handshake.

Id (string) --
The unique identifier (ID) for the party.
The regex pattern for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

Type (string) --
The type of party.





State (string) --
The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

REQUESTED : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond.
OPEN : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action.
CANCELED : This handshake is no longer active because it was canceled by the originating account.
ACCEPTED : This handshake is complete because it has been accepted by the recipient.
DECLINED : This handshake is no longer active because it was declined by the recipient account.
EXPIRED : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days).


RequestedTimestamp (datetime) --
The date and time that the handshake request was made.

ExpirationTimestamp (datetime) --
The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

Action (string) --
The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

INVITE : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts.
ENABLE_ALL_FEATURES : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only invited member accounts. Created accounts do not receive this because those accounts were created by the organization\'s master account and approval is inferred.
APPROVE_ALL_FEATURES : This type of handshake is sent from the Organizations service when all member accounts have approved the ENABLE_ALL_FEATURES invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features.


Resources (list) --
Additional information that is needed to process the handshake.

(dict) --
Contains additional data that is needed to process a handshake.

Value (string) --
The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

Type (string) --
The type of information being passed, specifying how the value is to be interpreted by the other party:

ACCOUNT - Specifies an AWS account ID number.
ORGANIZATION - Specifies an organization ID number.
EMAIL - Specifies the email address that is associated with the account that receives the handshake.
OWNER_EMAIL - Specifies the email address associated with the master account. Included as information about an organization.
OWNER_NAME - Specifies the name associated with the master account. Included as information about an organization.
NOTES - Additional text provided by the handshake initiator and intended for the recipient to read.


Resources (list) --
When needed, contains an additional array of HandshakeResource objects.









NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows you how to get a list of handshakes associated with the current organization:
response = client.list_handshakes_for_organization(
)

print(response)


Expected Output:
{
    'Handshakes': [
        {
            'Action': 'INVITE',
            'Arn': 'arn:aws:organizations::111111111111:handshake/o-exampleorgid/invite/h-examplehandshakeid111',
            'ExpirationTimestamp': datetime(2017, 1, 28, 14, 35, 23, 5, 28, 0),
            'Id': 'h-examplehandshakeid111',
            'Parties': [
                {
                    'Id': 'o-exampleorgid',
                    'Type': 'ORGANIZATION',
                },
                {
                    'Id': 'juan@example.com',
                    'Type': 'EMAIL',
                },
            ],
            'RequestedTimestamp': datetime(2017, 1, 13, 14, 35, 23, 4, 13, 0),
            'Resources': [
                {
                    'Resources': [
                        {
                            'Type': 'MASTER_EMAIL',
                            'Value': 'bill@amazon.com',
                        },
                        {
                            'Type': 'MASTER_NAME',
                            'Value': 'Org Master Account',
                        },
                        {
                            'Type': 'ORGANIZATION_FEATURE_SET',
                            'Value': 'FULL',
                        },
                    ],
                    'Type': 'ORGANIZATION',
                    'Value': 'o-exampleorgid',
                },
                {
                    'Type': 'EMAIL',
                    'Value': 'juan@example.com',
                },
            ],
            'State': 'OPEN',
        },
        {
            'Action': 'INVITE',
            'Arn': 'arn:aws:organizations::111111111111:handshake/o-exampleorgid/invite/h-examplehandshakeid111',
            'ExpirationTimestamp': datetime(2017, 1, 28, 14, 35, 23, 5, 28, 0),
            'Id': 'h-examplehandshakeid222',
            'Parties': [
                {
                    'Id': 'o-exampleorgid',
                    'Type': 'ORGANIZATION',
                },
                {
                    'Id': 'anika@example.com',
                    'Type': 'EMAIL',
                },
            ],
            'RequestedTimestamp': datetime(2017, 1, 13, 14, 35, 23, 4, 13, 0),
            'Resources': [
                {
                    'Resources': [
                        {
                            'Type': 'MASTER_EMAIL',
                            'Value': 'bill@example.com',
                        },
                        {
                            'Type': 'MASTER_NAME',
                            'Value': 'Master Account',
                        },
                    ],
                    'Type': 'ORGANIZATION',
                    'Value': 'o-exampleorgid',
                },
                {
                    'Type': 'EMAIL',
                    'Value': 'anika@example.com',
                },
                {
                    'Type': 'NOTES',
                    'Value': 'This is an invitation to Anika's account to join Bill's organization.',
                },
            ],
            'State': 'ACCEPTED',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
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
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to get a list of OUs in a specified root:/n/n
    Expected Output:
    
    :example: response = client.list_organizational_units_for_parent(
        ParentId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ParentId: string
    :param ParentId: [REQUIRED]\nThe unique identifier (ID) of the root or OU whose child OUs you want to list.\nThe regex pattern for a parent ID string requires one of the following:\n\nRoot - A string that begins with 'r-' followed by from 4 to 32 lowercase letters or digits.\nOrganizational unit (OU) - A string that begins with 'ou-' followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second '-' dash and from 8 to 32 additional lowercase letters or digits.\n\n

    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'OrganizationalUnits': [
        {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

OrganizationalUnits (list) --
A list of the OUs in the specified root or parent OU.

(dict) --
Contains details about an organizational unit (OU). An OU is a container of AWS accounts within a root of an organization. Policies that are attached to an OU apply to all accounts contained in that OU and in any child OUs.

Id (string) --
The unique identifier (ID) associated with this OU.
The regex pattern for an organizational unit ID string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU). This string is followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.

Arn (string) --
The Amazon Resource Name (ARN) of this OU.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Name (string) --
The friendly name of this OU.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.





NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ParentNotFoundException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows how to get a list of OUs in a specified root:/n/n
response = client.list_organizational_units_for_parent(
    ParentId='r-examplerootid111',
)

print(response)


Expected Output:
{
    'OrganizationalUnits': [
        {
            'Arn': 'arn:aws:organizations::111111111111:ou/o-exampleorgid/ou-examlerootid111-exampleouid111',
            'Id': 'ou-examplerootid111-exampleouid111',
            'Name': 'Development',
        },
        {
            'Arn': 'arn:aws:organizations::111111111111:ou/o-exampleorgid/ou-examlerootid111-exampleouid222',
            'Id': 'ou-examplerootid111-exampleouid222',
            'Name': 'Production',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.ParentNotFoundException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_parents(ChildId=None, NextToken=None, MaxResults=None):
    """
    Lists the root or organizational units (OUs) that serve as the immediate parent of the specified child OU or account. This operation, along with  ListChildren enables you to traverse the tree structure that makes up this root.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to list the root or OUs that contain account 444444444444:/n/n
    Expected Output:
    
    :example: response = client.list_parents(
        ChildId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ChildId: string
    :param ChildId: [REQUIRED]\nThe unique identifier (ID) of the OU or account whose parent containers you want to list. Don\'t specify a root.\nThe regex pattern for a child ID string requires one of the following:\n\nAccount - A string that consists of exactly 12 digits.\nOrganizational unit (OU) - A string that begins with 'ou-' followed by from 4 to 32 lowercase letters or digits (the ID of the root that contains the OU). This string is followed by a second '-' dash and from 8 to 32 additional lowercase letters or digits.\n\n

    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Parents': [
        {
            'Id': 'string',
            'Type': 'ROOT'|'ORGANIZATIONAL_UNIT'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Parents (list) --
A list of parents for the specified child account or OU.

(dict) --
Contains information about either a root or an organizational unit (OU) that can contain OUs or accounts in an organization.

Id (string) --
The unique identifier (ID) of the parent entity.
The regex pattern for a parent ID string requires one of the following:

Root: A string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.
Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.


Type (string) --
The type of the parent entity.





NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ChildNotFoundException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows how to list the root or OUs that contain account 444444444444:/n/n
response = client.list_parents(
    ChildId='444444444444',
)

print(response)


Expected Output:
{
    'Parents': [
        {
            'Id': 'ou-examplerootid111-exampleouid111',
            'Type': 'ORGANIZATIONAL_UNIT',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    Root: A string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.
    Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    
    """
    pass

def list_policies(Filter=None, NextToken=None, MaxResults=None):
    """
    Retrieves the list of all policies in an organization of a specified type.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to get a list of service control policies (SCPs):/n/n
    Expected Output:
    
    :example: response = client.list_policies(
        Filter='SERVICE_CONTROL_POLICY'|'TAG_POLICY',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: string
    :param Filter: [REQUIRED]\nSpecifies the type of policy that you want to include in the response.\n

    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Policies': [
        {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
            'AwsManaged': True|False
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Policies (list) --
A list of policies that match the filter criteria in the request. The output list doesn\'t include the policy contents. To see the content for a policy, see  DescribePolicy .

(dict) --
Contains information about a policy, but does not include the content. To see the content of a policy, see  DescribePolicy .

Id (string) --
The unique identifier (ID) of the policy.
The regex pattern for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

Arn (string) --
The Amazon Resource Name (ARN) of the policy.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Name (string) --
The friendly name of the policy.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.

Description (string) --
The description of the policy.

Type (string) --
The type of policy.

AwsManaged (boolean) --
A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.





NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.UnsupportedAPIEndpointException

Examples
The following example shows how to get a list of service control policies (SCPs):/n/n
response = client.list_policies(
    Filter='SERVICE_CONTROL_POLICY',
)

print(response)


Expected Output:
{
    'Policies': [
        {
            'Arn': 'arn:aws:organizations::111111111111:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111',
            'AwsManaged': False,
            'Description': 'Enables account admins to delegate permissions for any S3 actions to users and roles in their accounts.',
            'Id': 'p-examplepolicyid111',
            'Name': 'AllowAllS3Actions',
            'Type': 'SERVICE_CONTROL_POLICY',
        },
        {
            'Arn': 'arn:aws:organizations::111111111111:policy/o-exampleorgid/service_control_policy/p-examplepolicyid222',
            'AwsManaged': False,
            'Description': 'Enables account admins to delegate permissions for any EC2 actions to users and roles in their accounts.',
            'Id': 'p-examplepolicyid222',
            'Name': 'AllowAllEC2Actions',
            'Type': 'SERVICE_CONTROL_POLICY',
        },
        {
            'Arn': 'arn:aws:organizations::aws:policy/service_control_policy/p-FullAWSAccess',
            'AwsManaged': True,
            'Description': 'Allows access to every operation',
            'Id': 'p-FullAWSAccess',
            'Name': 'FullAWSAccess',
            'Type': 'SERVICE_CONTROL_POLICY',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Policies': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
                'AwsManaged': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.UnsupportedAPIEndpointException
    
    """
    pass

def list_policies_for_target(TargetId=None, Filter=None, NextToken=None, MaxResults=None):
    """
    Lists the policies that are directly attached to the specified target root, organizational unit (OU), or account. You must specify the policy type that you want included in the returned list.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to get a list of all service control policies (SCPs) of the type specified by the Filter parameter, that are directly attached to an account. The returned list does not include policies that apply to the account because of inheritance from its location in an OU hierarchy:/n/n
    Expected Output:
    
    :example: response = client.list_policies_for_target(
        TargetId='string',
        Filter='SERVICE_CONTROL_POLICY'|'TAG_POLICY',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type TargetId: string
    :param TargetId: [REQUIRED]\nThe unique identifier (ID) of the root, organizational unit, or account whose policies you want to list.\nThe regex pattern for a target ID string requires one of the following:\n\nRoot - A string that begins with 'r-' followed by from 4 to 32 lowercase letters or digits.\nAccount - A string that consists of exactly 12 digits.\nOrganizational unit (OU) - A string that begins with 'ou-' followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second '-' dash and from 8 to 32 additional lowercase letters or digits.\n\n

    :type Filter: string
    :param Filter: [REQUIRED]\nThe type of policy that you want to include in the returned list.\n

    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Policies': [
        {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
            'AwsManaged': True|False
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Policies (list) --
The list of policies that match the criteria in the request.

(dict) --
Contains information about a policy, but does not include the content. To see the content of a policy, see  DescribePolicy .

Id (string) --
The unique identifier (ID) of the policy.
The regex pattern for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

Arn (string) --
The Amazon Resource Name (ARN) of the policy.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Name (string) --
The friendly name of the policy.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.

Description (string) --
The description of the policy.

Type (string) --
The type of policy.

AwsManaged (boolean) --
A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.





NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TargetNotFoundException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.UnsupportedAPIEndpointException

Examples
The following example shows how to get a list of all service control policies (SCPs) of the type specified by the Filter parameter, that are directly attached to an account. The returned list does not include policies that apply to the account because of inheritance from its location in an OU hierarchy:/n/n
response = client.list_policies_for_target(
    Filter='SERVICE_CONTROL_POLICY',
    TargetId='444444444444',
)

print(response)


Expected Output:
{
    'Policies': [
        {
            'Arn': 'arn:aws:organizations::111111111111:policy/o-exampleorgid/service_control_policy/p-examplepolicyid222',
            'AwsManaged': False,
            'Description': 'Enables account admins to delegate permissions for any EC2 actions to users and roles in their accounts.',
            'Id': 'p-examplepolicyid222',
            'Name': 'AllowAllEC2Actions',
            'Type': 'SERVICE_CONTROL_POLICY',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Policies': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
                'AwsManaged': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TargetNotFoundException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.UnsupportedAPIEndpointException
    
    """
    pass

def list_roots(NextToken=None, MaxResults=None):
    """
    Lists the roots that are defined in the current organization.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to get the list of the roots in the current organization:/n/n
    Expected Output:
    
    :example: response = client.list_roots(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Roots': [
        {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'PolicyTypes': [
                {
                    'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
                    'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Roots (list) --
A list of roots that are defined in an organization.

(dict) --
Contains details about a root. A root is a top-level parent node in the hierarchy of an organization that can contain organizational units (OUs) and accounts. Every root contains every AWS account in the organization. Each root enables the accounts to be organized in a different way and to have different policy types enabled for use in that root.

Id (string) --
The unique identifier (ID) for the root.
The regex pattern for a root ID string requires "r-" followed by from 4 to 32 lower-case letters or digits.

Arn (string) --
The Amazon Resource Name (ARN) of the root.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Name (string) --
The friendly name of the root.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.

PolicyTypes (list) --
The types of policies that are currently enabled for the root and therefore can be attached to the root or to its OUs or accounts.

Note
Even if a policy type is shown as available in the organization, you can separately enable and disable them at the root level by using  EnablePolicyType and  DisablePolicyType . Use  DescribeOrganization to see the availability of the policy types in that organization.


(dict) --
Contains information about a policy type and its status in the associated root.

Type (string) --
The name of the policy type.

Status (string) --
The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.









NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows how to get the list of the roots in the current organization:/n/n
response = client.list_roots(
)

print(response)


Expected Output:
{
    'Roots': [
        {
            'Arn': 'arn:aws:organizations::111111111111:root/o-exampleorgid/r-examplerootid111',
            'Id': 'r-examplerootid111',
            'Name': 'Root',
            'PolicyTypes': [
                {
                    'Status': 'ENABLED',
                    'Type': 'SERVICE_CONTROL_POLICY',
                },
            ],
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Roots': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'PolicyTypes': [
                    {
                        'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
                        'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_tags_for_resource(ResourceId=None, NextToken=None):
    """
    Lists tags for the specified resource.
    Currently, you can list tags on an account in AWS Organizations.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceId='string',
        NextToken='string'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the resource that you want to retrieve tags for.\n

    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Tags (list) --
The tags that are assigned to the resource.

(dict) --
A custom key-value pair associated with a resource such as an account within your organization.

Key (string) --
The key identifier, or name, of the tag.

Value (string) --
The string value that\'s associated with the key of the tag. You can set the value of a tag to an empty string, but you can\'t set the value of a tag to null.





NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.TargetNotFoundException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.TargetNotFoundException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_targets_for_policy(PolicyId=None, NextToken=None, MaxResults=None):
    """
    Lists all the roots, organizational units (OUs), and accounts that the specified policy is attached to.
    This operation can be called only from the organization\'s master account or by a member account that is a delegated administrator for an AWS service.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to get the list of roots, OUs, and accounts to which the specified policy is attached:/n/n
    Expected Output:
    
    :example: response = client.list_targets_for_policy(
        PolicyId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]\nThe unique identifier (ID) of the policy whose attachments you want to know.\nThe regex pattern for a policy ID string requires 'p-' followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).\n

    :type NextToken: string
    :param NextToken: The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the NextToken response element is present and has a value (is not null). Include that value as the NextToken request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Targets (list) --
A list of structures, each of which contains details about one of the entities to which the specified policy is attached.

(dict) --
Contains information about a root, OU, or account that a policy is attached to.

TargetId (string) --
The unique identifier (ID) of the policy target.
The regex pattern for a target ID string requires one of the following:

Root: A string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.
Account: A string that consists of exactly 12 digits.
Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.


Arn (string) --
The Amazon Resource Name (ARN) of the policy target.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Name (string) --
The friendly name of the policy target.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.

Type (string) --
The type of the policy target.





NextToken (string) --
If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the NextToken response element comes back as null .







Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.PolicyNotFoundException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.UnsupportedAPIEndpointException

Examples
The following example shows how to get the list of roots, OUs, and accounts to which the specified policy is attached:/n/n
response = client.list_targets_for_policy(
    PolicyId='p-FullAWSAccess',
)

print(response)


Expected Output:
{
    'Targets': [
        {
            'Arn': 'arn:aws:organizations::111111111111:root/o-exampleorgid/r-examplerootid111',
            'Name': 'Root',
            'TargetId': 'r-examplerootid111',
            'Type': 'ROOT',
        },
        {
            'Arn': 'arn:aws:organizations::111111111111:account/o-exampleorgid/333333333333;',
            'Name': 'Developer Test Account',
            'TargetId': '333333333333',
            'Type': 'ACCOUNT',
        },
        {
            'Arn': 'arn:aws:organizations::111111111111:ou/o-exampleorgid/ou-examplerootid111-exampleouid111',
            'Name': 'Accounting',
            'TargetId': 'ou-examplerootid111-exampleouid111',
            'Type': 'ORGANIZATIONAL_UNIT',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    Root: A string that begins with "r-" followed by from 4 to 32 lower-case letters or digits.
    Account: A string that consists of exactly 12 digits.
    Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    
    """
    pass

def move_account(AccountId=None, SourceParentId=None, DestinationParentId=None):
    """
    Moves an account from its current source parent root or organizational unit (OU) to the specified destination parent root or OU.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to move a member account from the root to an OU:/n/n
    Expected Output:
    
    :example: response = client.move_account(
        AccountId='string',
        SourceParentId='string',
        DestinationParentId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe unique identifier (ID) of the account that you want to move.\nThe regex pattern for an account ID string requires exactly 12 digits.\n

    :type SourceParentId: string
    :param SourceParentId: [REQUIRED]\nThe unique identifier (ID) of the root or organizational unit that you want to move the account from.\nThe regex pattern for a parent ID string requires one of the following:\n\nRoot - A string that begins with 'r-' followed by from 4 to 32 lowercase letters or digits.\nOrganizational unit (OU) - A string that begins with 'ou-' followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second '-' dash and from 8 to 32 additional lowercase letters or digits.\n\n

    :type DestinationParentId: string
    :param DestinationParentId: [REQUIRED]\nThe unique identifier (ID) of the root or organizational unit that you want to move the account to.\nThe regex pattern for a parent ID string requires one of the following:\n\nRoot - A string that begins with 'r-' followed by from 4 to 32 lowercase letters or digits.\nOrganizational unit (OU) - A string that begins with 'ou-' followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second '-' dash and from 8 to 32 additional lowercase letters or digits.\n\n

    :return: response = client.move_account(
        AccountId='333333333333',
        DestinationParentId='ou-examplerootid111-exampleouid111',
        SourceParentId='r-examplerootid111',
    )
    
    print(response)
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.SourceParentNotFoundException
    Organizations.Client.exceptions.DestinationParentNotFoundException
    Organizations.Client.exceptions.DuplicateAccountException
    Organizations.Client.exceptions.AccountNotFoundException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.ConcurrentModificationException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.ServiceException
    
    """
    pass

def register_delegated_administrator(AccountId=None, ServicePrincipal=None):
    """
    Enables the specified member account to administer the Organizations features of the specified AWS service. It grants read-only access to AWS Organizations service data. The account still requires IAM permissions to access and administer the AWS service.
    You can run this action only for AWS services that support this feature. For a current list of services that support it, see the column Supports Delegated Administrator in the table at AWS Services that you can use with AWS Organizations in the AWS Organizations User Guide.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_delegated_administrator(
        AccountId='string',
        ServicePrincipal='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe account ID number of the member account in the organization to register as a delegated administrator.\n

    :type ServicePrincipal: string
    :param ServicePrincipal: [REQUIRED]\nThe service principal of the AWS service for which you want to make the member account a delegated administrator.\n

    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AccountAlreadyRegisteredException
    Organizations.Client.exceptions.AccountNotFoundException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.ConcurrentModificationException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.UnsupportedAPIEndpointException
    
    """
    pass

def remove_account_from_organization(AccountId=None):
    """
    Removes the specified account from the organization.
    The removed account becomes a standalone account that isn\'t a member of any organization. It\'s no longer subject to any policies and is responsible for its own bill payments. The organization\'s master account is no longer charged for any expenses accrued by the member account after it\'s removed from the organization.
    This operation can be called only from the organization\'s master account. Member accounts can remove themselves with  LeaveOrganization instead.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows you how to remove an account from an organization:
    Expected Output:
    
    :example: response = client.remove_account_from_organization(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe unique identifier (ID) of the member account that you want to remove from the organization.\nThe regex pattern for an account ID string requires exactly 12 digits.\n

    :return: response = client.remove_account_from_organization(
        AccountId='333333333333',
    )
    
    print(response)
    
    
    """
    pass

def tag_resource(ResourceId=None, Tags=None):
    """
    Adds one or more tags to the specified resource.
    Currently, you can tag and untag accounts in AWS Organizations.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the resource to add a tag to.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tag to add to the specified resource. Specifying the tag key is required. You can set the value of a tag to an empty string, but you can\'t set the value of a tag to null.\n\n(dict) --A custom key-value pair associated with a resource such as an account within your organization.\n\nKey (string) -- [REQUIRED]The key identifier, or name, of the tag.\n\nValue (string) -- [REQUIRED]The string value that\'s associated with the key of the tag. You can set the value of a tag to an empty string, but you can\'t set the value of a tag to null.\n\n\n\n\n

    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.ConcurrentModificationException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.TargetNotFoundException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    
    """
    pass

def untag_resource(ResourceId=None, TagKeys=None):
    """
    Removes a tag from the specified resource.
    Currently, you can tag and untag accounts in AWS Organizations.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the resource to remove the tag from.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag to remove from the specified resource.\n\n(string) --\n\n

    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.ConcurrentModificationException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.TargetNotFoundException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    
    """
    pass

def update_organizational_unit(OrganizationalUnitId=None, Name=None):
    """
    Renames the specified organizational unit (OU). The ID and ARN don\'t change. The child OUs and accounts remain in place, and any attached policies of the OU remain attached.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to rename an OU. The output confirms the new name:/n/n
    Expected Output:
    
    :example: response = client.update_organizational_unit(
        OrganizationalUnitId='string',
        Name='string'
    )
    
    
    :type OrganizationalUnitId: string
    :param OrganizationalUnitId: [REQUIRED]\nThe unique identifier (ID) of the OU that you want to rename. You can get the ID from the ListOrganizationalUnitsForParent operation.\nThe regex pattern for an organizational unit ID string requires 'ou-' followed by from 4 to 32 lowercase letters or digits (the ID of the root that contains the OU). This string is followed by a second '-' dash and from 8 to 32 additional lowercase letters or digits.\n

    :type Name: string
    :param Name: The new name that you want to assign to the OU.\nThe regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OrganizationalUnit': {
        'Id': 'string',
        'Arn': 'string',
        'Name': 'string'
    }
}


Response Structure

(dict) --

OrganizationalUnit (dict) --
A structure that contains the details about the specified OU, including its new name.

Id (string) --
The unique identifier (ID) associated with this OU.
The regex pattern for an organizational unit ID string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU). This string is followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.

Arn (string) --
The Amazon Resource Name (ARN) of this OU.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Name (string) --
The friendly name of this OU.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.









Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.DuplicateOrganizationalUnitException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.OrganizationalUnitNotFoundException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException

Examples
The following example shows how to rename an OU. The output confirms the new name:/n/n
response = client.update_organizational_unit(
    Name='AccountingOU',
    OrganizationalUnitId='ou-examplerootid111-exampleouid111',
)

print(response)


Expected Output:
{
    'OrganizationalUnit': {
        'Arn': 'arn:aws:organizations::111111111111:ou/o-exampleorgid/ou-examplerootid111-exampleouid111',
        'Id': 'ou-examplerootid111-exampleouid111',
        'Name': 'AccountingOU',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'OrganizationalUnit': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        }
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.ConcurrentModificationException
    Organizations.Client.exceptions.DuplicateOrganizationalUnitException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.OrganizationalUnitNotFoundException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    
    """
    pass

def update_policy(PolicyId=None, Name=None, Description=None, Content=None):
    """
    Updates an existing policy with a new name, description, or content. If you don\'t supply any parameter, that value remains unchanged. You can\'t change a policy\'s type.
    This operation can be called only from the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows how to rename a policy and give it a new description and new content. The output confirms the new name and description text:/n/n
    Expected Output:
    The following example shows how to replace the JSON text of the SCP from the preceding example with a new JSON policy text string that allows S3 actions instead of EC2 actions:/n/n
    Expected Output:
    
    :example: response = client.update_policy(
        PolicyId='string',
        Name='string',
        Description='string',
        Content='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]\nThe unique identifier (ID) of the policy that you want to update.\nThe regex pattern for a policy ID string requires 'p-' followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).\n

    :type Name: string
    :param Name: If provided, the new name for the policy.\nThe regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.\n

    :type Description: string
    :param Description: If provided, the new description for the policy.

    :type Content: string
    :param Content: If provided, the new content for the policy. The text must be correctly formatted JSON that complies with the syntax for the policy\'s type. For more information, see Service Control Policy Syntax in the AWS Organizations User Guide.

    :rtype: dict

ReturnsResponse Syntax
{
    'Policy': {
        'PolicySummary': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
            'AwsManaged': True|False
        },
        'Content': 'string'
    }
}


Response Structure

(dict) --

Policy (dict) --
A structure that contains details about the updated policy, showing the requested changes.

PolicySummary (dict) --
A structure that contains additional details about the policy.

Id (string) --
The unique identifier (ID) of the policy.
The regex pattern for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

Arn (string) --
The Amazon Resource Name (ARN) of the policy.
For more information about ARNs in Organizations, see ARN Formats Supported by Organizations in the AWS Organizations User Guide .

Name (string) --
The friendly name of the policy.
The regex pattern that is used to validate this parameter is a string of any of the characters in the ASCII character range.

Description (string) --
The description of the policy.

Type (string) --
The type of policy.

AwsManaged (boolean) --
A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.



Content (string) --
The text content of the policy.









Exceptions

Organizations.Client.exceptions.AccessDeniedException
Organizations.Client.exceptions.AWSOrganizationsNotInUseException
Organizations.Client.exceptions.ConcurrentModificationException
Organizations.Client.exceptions.ConstraintViolationException
Organizations.Client.exceptions.DuplicatePolicyException
Organizations.Client.exceptions.InvalidInputException
Organizations.Client.exceptions.MalformedPolicyDocumentException
Organizations.Client.exceptions.PolicyNotFoundException
Organizations.Client.exceptions.ServiceException
Organizations.Client.exceptions.TooManyRequestsException
Organizations.Client.exceptions.UnsupportedAPIEndpointException
Organizations.Client.exceptions.PolicyChangesInProgressException

Examples
The following example shows how to rename a policy and give it a new description and new content. The output confirms the new name and description text:/n/n
response = client.update_policy(
    Description='This description replaces the original.',
    Name='Renamed-Policy',
    PolicyId='p-examplepolicyid111',
)

print(response)


Expected Output:
{
    'Policy': {
        'Content': '{ "Version": "2012-10-17", "Statement": { "Effect": "Allow", "Action": "ec2:*", "Resource": "*" } }',
        'PolicySummary': {
            'Arn': 'arn:aws:organizations::111111111111:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111',
            'AwsManaged': False,
            'Description': 'This description replaces the original.',
            'Id': 'p-examplepolicyid111',
            'Name': 'Renamed-Policy',
            'Type': 'SERVICE_CONTROL_POLICY',
        },
    },
    'ResponseMetadata': {
        '...': '...',
    },
}


The following example shows how to replace the JSON text of the SCP from the preceding example with a new JSON policy text string that allows S3 actions instead of EC2 actions:/n/n
response = client.update_policy(
    Content='{ \\"Version\\": \\"2012-10-17\\", \\"Statement\\": {\\"Effect\\": \\"Allow\\", \\"Action\\": \\"s3:*\\", \\"Resource\\": \\"*\\" } }',
    PolicyId='p-examplepolicyid111',
)

print(response)


Expected Output:
{
    'Policy': {
        'Content': '{ \\"Version\\": \\"2012-10-17\\", \\"Statement\\": { \\"Effect\\": \\"Allow\\", \\"Action\\": \\"s3:*\\", \\"Resource\\": \\"*\\" } }',
        'PolicySummary': {
            'Arn': 'arn:aws:organizations::111111111111:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111',
            'AwsManaged': False,
            'Description': 'This description replaces the original.',
            'Id': 'p-examplepolicyid111',
            'Name': 'Renamed-Policy',
            'Type': 'SERVICE_CONTROL_POLICY',
        },
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Policy': {
            'PolicySummary': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'SERVICE_CONTROL_POLICY'|'TAG_POLICY',
                'AwsManaged': True|False
            },
            'Content': 'string'
        }
    }
    
    
    :returns: 
    Organizations.Client.exceptions.AccessDeniedException
    Organizations.Client.exceptions.AWSOrganizationsNotInUseException
    Organizations.Client.exceptions.ConcurrentModificationException
    Organizations.Client.exceptions.ConstraintViolationException
    Organizations.Client.exceptions.DuplicatePolicyException
    Organizations.Client.exceptions.InvalidInputException
    Organizations.Client.exceptions.MalformedPolicyDocumentException
    Organizations.Client.exceptions.PolicyNotFoundException
    Organizations.Client.exceptions.ServiceException
    Organizations.Client.exceptions.TooManyRequestsException
    Organizations.Client.exceptions.UnsupportedAPIEndpointException
    Organizations.Client.exceptions.PolicyChangesInProgressException
    
    """
    pass

