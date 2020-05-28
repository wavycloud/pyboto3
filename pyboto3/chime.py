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

def associate_phone_number_with_user(AccountId=None, UserId=None, E164PhoneNumber=None):
    """
    Associates a phone number with the specified Amazon Chime user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_phone_number_with_user(
        AccountId='string',
        UserId='string',
        E164PhoneNumber='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type UserId: string
    :param UserId: [REQUIRED]\nThe user ID.\n

    :type E164PhoneNumber: string
    :param E164PhoneNumber: [REQUIRED]\nThe phone number, in E.164 format.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.AccessDeniedException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_phone_numbers_with_voice_connector(VoiceConnectorId=None, E164PhoneNumbers=None, ForceAssociate=None):
    """
    Associates phone numbers with the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_phone_numbers_with_voice_connector(
        VoiceConnectorId='string',
        E164PhoneNumbers=[
            'string',
        ],
        ForceAssociate=True|False
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :type E164PhoneNumbers: list
    :param E164PhoneNumbers: List of phone numbers, in E.164 format.\n\n(string) --\n\n

    :type ForceAssociate: boolean
    :param ForceAssociate: If true, associates the provided phone numbers with the provided Amazon Chime Voice Connector and removes any previously existing associations. If false, does not associate any phone numbers that have previously existing associations.

    :rtype: dict

ReturnsResponse Syntax
{
    'PhoneNumberErrors': [
        {
            'PhoneNumberId': 'string',
            'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

PhoneNumberErrors (list) --
If the action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.

(dict) --
If the phone number action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.

PhoneNumberId (string) --
The phone number ID for which the action failed.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.











Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.AccessDeniedException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'PhoneNumberErrors': [
            {
                'PhoneNumberId': 'string',
                'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.AccessDeniedException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def associate_phone_numbers_with_voice_connector_group(VoiceConnectorGroupId=None, E164PhoneNumbers=None, ForceAssociate=None):
    """
    Associates phone numbers with the specified Amazon Chime Voice Connector group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_phone_numbers_with_voice_connector_group(
        VoiceConnectorGroupId='string',
        E164PhoneNumbers=[
            'string',
        ],
        ForceAssociate=True|False
    )
    
    
    :type VoiceConnectorGroupId: string
    :param VoiceConnectorGroupId: [REQUIRED]\nThe Amazon Chime Voice Connector group ID.\n

    :type E164PhoneNumbers: list
    :param E164PhoneNumbers: List of phone numbers, in E.164 format.\n\n(string) --\n\n

    :type ForceAssociate: boolean
    :param ForceAssociate: If true, associates the provided phone numbers with the provided Amazon Chime Voice Connector Group and removes any previously existing associations. If false, does not associate any phone numbers that have previously existing associations.

    :rtype: dict

ReturnsResponse Syntax
{
    'PhoneNumberErrors': [
        {
            'PhoneNumberId': 'string',
            'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

PhoneNumberErrors (list) --
If the action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.

(dict) --
If the phone number action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.

PhoneNumberId (string) --
The phone number ID for which the action failed.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.











Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.AccessDeniedException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'PhoneNumberErrors': [
            {
                'PhoneNumberId': 'string',
                'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.AccessDeniedException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def associate_signin_delegate_groups_with_account(AccountId=None, SigninDelegateGroups=None):
    """
    Associates the specified sign-in delegate groups with the specified Amazon Chime account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_signin_delegate_groups_with_account(
        AccountId='string',
        SigninDelegateGroups=[
            {
                'GroupName': 'string'
            },
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type SigninDelegateGroups: list
    :param SigninDelegateGroups: [REQUIRED]\nThe sign-in delegate groups.\n\n(dict) --An Active Directory (AD) group whose members are granted permission to act as delegates.\n\nGroupName (string) --The group name.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def batch_create_attendee(MeetingId=None, Attendees=None):
    """
    Creates up to 100 new attendees for an active Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see Using the Amazon Chime SDK in the Amazon Chime Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_create_attendee(
        MeetingId='string',
        Attendees=[
            {
                'ExternalUserId': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    )
    
    
    :type MeetingId: string
    :param MeetingId: [REQUIRED]\nThe Amazon Chime SDK meeting ID.\n

    :type Attendees: list
    :param Attendees: [REQUIRED]\nThe request containing the attendees to create.\n\n(dict) --The Amazon Chime SDK attendee fields to create, used with the BatchCreateAttendee action.\n\nExternalUserId (string) -- [REQUIRED]The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a builder application.\n\nTags (list) --The tag key-value pairs.\n\n(dict) --Describes a tag applied to a resource.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Attendees': [
        {
            'ExternalUserId': 'string',
            'AttendeeId': 'string',
            'JoinToken': 'string'
        },
    ],
    'Errors': [
        {
            'ExternalUserId': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

Attendees (list) --
The attendee information, including attendees IDs and join tokens.

(dict) --
An Amazon Chime SDK meeting attendee. Includes a unique AttendeeId and JoinToken . The JoinToken allows a client to authenticate and join as the specified attendee. The JoinToken expires when the meeting ends or when  DeleteAttendee is called. After that, the attendee is unable to join the meeting.
We recommend securely transferring each JoinToken from your server application to the client so that no other client has access to the token except for the one authorized to represent the attendee.

ExternalUserId (string) --
The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a builder application.

AttendeeId (string) --
The Amazon Chime SDK attendee ID.

JoinToken (string) --
The join token used by the Amazon Chime SDK attendee.





Errors (list) --
If the action fails for one or more of the attendees in the request, a list of the attendees is returned, along with error codes and error messages.

(dict) --
The list of errors returned when errors are encountered during the BatchCreateAttendee and CreateAttendee actions. This includes external user IDs, error codes, and error messages.

ExternalUserId (string) --
The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a builder application.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.











Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ResourceLimitExceededException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Attendees': [
            {
                'ExternalUserId': 'string',
                'AttendeeId': 'string',
                'JoinToken': 'string'
            },
        ],
        'Errors': [
            {
                'ExternalUserId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ResourceLimitExceededException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def batch_create_room_membership(AccountId=None, RoomId=None, MembershipItemList=None):
    """
    Adds up to 50 members to a chat room in an Amazon Chime Enterprise account. Members can be either users or bots. The member role designates whether the member is a chat room administrator or a general chat room member.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_create_room_membership(
        AccountId='string',
        RoomId='string',
        MembershipItemList=[
            {
                'MemberId': 'string',
                'Role': 'Administrator'|'Member'
            },
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type RoomId: string
    :param RoomId: [REQUIRED]\nThe room ID.\n

    :type MembershipItemList: list
    :param MembershipItemList: [REQUIRED]\nThe list of membership items.\n\n(dict) --Membership details, such as member ID and member role.\n\nMemberId (string) --The member ID.\n\nRole (string) --The member role.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Errors': [
        {
            'MemberId': 'string',
            'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

Errors (list) --
If the action fails for one or more of the member IDs in the request, a list of the member IDs is returned, along with error codes and error messages.

(dict) --
The list of errors returned when a member action results in an error.

MemberId (string) --
The member ID.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.











Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Errors': [
            {
                'MemberId': 'string',
                'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def batch_delete_phone_number(PhoneNumberIds=None):
    """
    Moves phone numbers into the Deletion queue . Phone numbers must be disassociated from any users or Amazon Chime Voice Connectors before they can be deleted.
    Phone numbers remain in the Deletion queue for 7 days before they are deleted permanently.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_delete_phone_number(
        PhoneNumberIds=[
            'string',
        ]
    )
    
    
    :type PhoneNumberIds: list
    :param PhoneNumberIds: [REQUIRED]\nList of phone number IDs.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'PhoneNumberErrors': [
        {
            'PhoneNumberId': 'string',
            'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
PhoneNumberErrors (list) --If the action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.

(dict) --If the phone number action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.

PhoneNumberId (string) --The phone number ID for which the action failed.

ErrorCode (string) --The error code.

ErrorMessage (string) --The error message.










Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'PhoneNumberErrors': [
            {
                'PhoneNumberId': 'string',
                'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def batch_suspend_user(AccountId=None, UserIdList=None):
    """
    Suspends up to 50 users from a Team or EnterpriseLWA Amazon Chime account. For more information about different account types, see Managing Your Amazon Chime Accounts in the Amazon Chime Administration Guide .
    Users suspended from a Team account are disassociated from the account, but they can continue to use Amazon Chime as free users. To remove the suspension from suspended Team account users, invite them to the Team account again. You can use the  InviteUsers action to do so.
    Users suspended from an EnterpriseLWA account are immediately signed out of Amazon Chime and can no longer sign in. To remove the suspension from suspended EnterpriseLWA account users, use the  BatchUnsuspendUser action.
    To sign out users without suspending them, use the  LogoutUser action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_suspend_user(
        AccountId='string',
        UserIdList=[
            'string',
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type UserIdList: list
    :param UserIdList: [REQUIRED]\nThe request containing the user IDs to suspend.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UserErrors': [
        {
            'UserId': 'string',
            'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

UserErrors (list) --
If the  BatchSuspendUser action fails for one or more of the user IDs in the request, a list of the user IDs is returned, along with error codes and error messages.

(dict) --
The list of errors returned when errors are encountered during the  BatchSuspendUser ,  BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and error messages.

UserId (string) --
The user ID for which the action failed.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.











Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'UserErrors': [
            {
                'UserId': 'string',
                'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def batch_unsuspend_user(AccountId=None, UserIdList=None):
    """
    Removes the suspension from up to 50 previously suspended users for the specified Amazon Chime EnterpriseLWA account. Only users on EnterpriseLWA accounts can be unsuspended using this action. For more information about different account types, see Managing Your Amazon Chime Accounts in the Amazon Chime Administration Guide .
    Previously suspended users who are unsuspended using this action are returned to Registered status. Users who are not previously suspended are ignored.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_unsuspend_user(
        AccountId='string',
        UserIdList=[
            'string',
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type UserIdList: list
    :param UserIdList: [REQUIRED]\nThe request containing the user IDs to unsuspend.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UserErrors': [
        {
            'UserId': 'string',
            'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

UserErrors (list) --
If the  BatchUnsuspendUser action fails for one or more of the user IDs in the request, a list of the user IDs is returned, along with error codes and error messages.

(dict) --
The list of errors returned when errors are encountered during the  BatchSuspendUser ,  BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and error messages.

UserId (string) --
The user ID for which the action failed.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.











Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'UserErrors': [
            {
                'UserId': 'string',
                'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def batch_update_phone_number(UpdatePhoneNumberRequestItems=None):
    """
    Updates phone number product types or calling names. You can update one attribute at a time for each UpdatePhoneNumberRequestItem . For example, you can update either the product type or the calling name.
    For product types, choose from Amazon Chime Business Calling and Amazon Chime Voice Connector. For toll-free numbers, you must use the Amazon Chime Voice Connector product type.
    Updates to outbound calling names can take up to 72 hours to complete. Pending updates to outbound calling names must be complete before you can request another update.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_update_phone_number(
        UpdatePhoneNumberRequestItems=[
            {
                'PhoneNumberId': 'string',
                'ProductType': 'BusinessCalling'|'VoiceConnector',
                'CallingName': 'string'
            },
        ]
    )
    
    
    :type UpdatePhoneNumberRequestItems: list
    :param UpdatePhoneNumberRequestItems: [REQUIRED]\nThe request containing the phone number IDs and product types or calling names to update.\n\n(dict) --The phone number ID, product type, or calling name fields to update, used with the BatchUpdatePhoneNumber and UpdatePhoneNumber actions.\n\nPhoneNumberId (string) -- [REQUIRED]The phone number ID to update.\n\nProductType (string) --The product type to update.\n\nCallingName (string) --The outbound calling name to update.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'PhoneNumberErrors': [
        {
            'PhoneNumberId': 'string',
            'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
PhoneNumberErrors (list) --If the action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.

(dict) --If the phone number action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.

PhoneNumberId (string) --The phone number ID for which the action failed.

ErrorCode (string) --The error code.

ErrorMessage (string) --The error message.










Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'PhoneNumberErrors': [
            {
                'PhoneNumberId': 'string',
                'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_update_user(AccountId=None, UpdateUserRequestItems=None):
    """
    Updates user details within the  UpdateUserRequestItem object for up to 20 users for the specified Amazon Chime account. Currently, only LicenseType updates are supported for this action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_update_user(
        AccountId='string',
        UpdateUserRequestItems=[
            {
                'UserId': 'string',
                'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
                'UserType': 'PrivateUser'|'SharedDevice',
                'AlexaForBusinessMetadata': {
                    'IsAlexaForBusinessEnabled': True|False,
                    'AlexaForBusinessRoomArn': 'string'
                }
            },
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type UpdateUserRequestItems: list
    :param UpdateUserRequestItems: [REQUIRED]\nThe request containing the user IDs and details to update.\n\n(dict) --The user ID and user fields to update, used with the BatchUpdateUser action.\n\nUserId (string) -- [REQUIRED]The user ID.\n\nLicenseType (string) --The user license type.\n\nUserType (string) --The user type.\n\nAlexaForBusinessMetadata (dict) --The Alexa for Business metadata.\n\nIsAlexaForBusinessEnabled (boolean) --Starts or stops Alexa for Business.\n\nAlexaForBusinessRoomArn (string) --The ARN of the room resource.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UserErrors': [
        {
            'UserId': 'string',
            'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

UserErrors (list) --
If the  BatchUpdateUser action fails for one or more of the user IDs in the request, a list of the user IDs is returned, along with error codes and error messages.

(dict) --
The list of errors returned when errors are encountered during the  BatchSuspendUser ,  BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and error messages.

UserId (string) --
The user ID for which the action failed.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.











Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'UserErrors': [
            {
                'UserId': 'string',
                'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_account(Name=None):
    """
    Creates an Amazon Chime account under the administrator\'s AWS account. Only Team account types are currently supported for this action. For more information about different account types, see Managing Your Amazon Chime Accounts in the Amazon Chime Administration Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_account(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the Amazon Chime account.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Account': {
        'AwsAccountId': 'string',
        'AccountId': 'string',
        'Name': 'string',
        'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
        'SupportedLicenses': [
            'Basic'|'Plus'|'Pro'|'ProTrial',
        ],
        'SigninDelegateGroups': [
            {
                'GroupName': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Account (dict) --The Amazon Chime account details.

AwsAccountId (string) --The AWS account ID.

AccountId (string) --The Amazon Chime account ID.

Name (string) --The Amazon Chime account name.

AccountType (string) --The Amazon Chime account type. For more information about different account types, see Managing Your Amazon Chime Accounts in the Amazon Chime Administration Guide .

CreatedTimestamp (datetime) --The Amazon Chime account creation timestamp, in ISO 8601 format.

DefaultLicense (string) --The default license for the Amazon Chime account.

SupportedLicenses (list) --Supported licenses for the Amazon Chime account.

(string) --


SigninDelegateGroups (list) --The sign-in delegate groups associated with the account.

(dict) --An Active Directory (AD) group whose members are granted permission to act as delegates.

GroupName (string) --The group name.












Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Account': {
            'AwsAccountId': 'string',
            'AccountId': 'string',
            'Name': 'string',
            'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'SupportedLicenses': [
                'Basic'|'Plus'|'Pro'|'ProTrial',
            ],
            'SigninDelegateGroups': [
                {
                    'GroupName': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_attendee(MeetingId=None, ExternalUserId=None, Tags=None):
    """
    Creates a new attendee for an active Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see Using the Amazon Chime SDK in the Amazon Chime Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_attendee(
        MeetingId='string',
        ExternalUserId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type MeetingId: string
    :param MeetingId: [REQUIRED]\nThe Amazon Chime SDK meeting ID.\n

    :type ExternalUserId: string
    :param ExternalUserId: [REQUIRED]\nThe Amazon Chime SDK external user ID. Links the attendee to an identity managed by a builder application.\n

    :type Tags: list
    :param Tags: The tag key-value pairs.\n\n(dict) --Describes a tag applied to a resource.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Attendee': {
        'ExternalUserId': 'string',
        'AttendeeId': 'string',
        'JoinToken': 'string'
    }
}


Response Structure

(dict) --

Attendee (dict) --
The attendee information, including attendee ID and join token.

ExternalUserId (string) --
The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a builder application.

AttendeeId (string) --
The Amazon Chime SDK attendee ID.

JoinToken (string) --
The join token used by the Amazon Chime SDK attendee.









Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ResourceLimitExceededException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Attendee': {
            'ExternalUserId': 'string',
            'AttendeeId': 'string',
            'JoinToken': 'string'
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ResourceLimitExceededException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_bot(AccountId=None, DisplayName=None, Domain=None):
    """
    Creates a bot for an Amazon Chime Enterprise account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_bot(
        AccountId='string',
        DisplayName='string',
        Domain='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type DisplayName: string
    :param DisplayName: [REQUIRED]\nThe bot display name.\n

    :type Domain: string
    :param Domain: The domain of the Amazon Chime Enterprise account.

    :rtype: dict

ReturnsResponse Syntax
{
    'Bot': {
        'BotId': 'string',
        'UserId': 'string',
        'DisplayName': 'string',
        'BotType': 'ChatBot',
        'Disabled': True|False,
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1),
        'BotEmail': 'string',
        'SecurityToken': 'string'
    }
}


Response Structure

(dict) --

Bot (dict) --
The bot details.

BotId (string) --
The bot ID.

UserId (string) --
The unique ID for the bot user.

DisplayName (string) --
The bot display name.

BotType (string) --
The bot type.

Disabled (boolean) --
When true, the bot is stopped from running in your account.

CreatedTimestamp (datetime) --
The bot creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated bot timestamp, in ISO 8601 format.

BotEmail (string) --
The bot email address.

SecurityToken (string) --
The security token used to authenticate Amazon Chime with the outgoing event endpoint.









Exceptions

Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ResourceLimitExceededException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ThrottledClientException


    :return: {
        'Bot': {
            'BotId': 'string',
            'UserId': 'string',
            'DisplayName': 'string',
            'BotType': 'ChatBot',
            'Disabled': True|False,
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1),
            'BotEmail': 'string',
            'SecurityToken': 'string'
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ResourceLimitExceededException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ThrottledClientException
    
    """
    pass

def create_meeting(ClientRequestToken=None, ExternalMeetingId=None, MeetingHostId=None, MediaRegion=None, Tags=None, NotificationsConfiguration=None):
    """
    Creates a new Amazon Chime SDK meeting in the specified media Region with no initial attendees. For more information about the Amazon Chime SDK, see Using the Amazon Chime SDK in the Amazon Chime Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_meeting(
        ClientRequestToken='string',
        ExternalMeetingId='string',
        MeetingHostId='string',
        MediaRegion='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        NotificationsConfiguration={
            'SnsTopicArn': 'string',
            'SqsQueueArn': 'string'
        }
    )
    
    
    :type ClientRequestToken: string
    :param ClientRequestToken: [REQUIRED]\nThe unique identifier for the client request. Use a different token for different meetings.\nThis field is autopopulated if not provided.\n

    :type ExternalMeetingId: string
    :param ExternalMeetingId: The external meeting ID.

    :type MeetingHostId: string
    :param MeetingHostId: Reserved.

    :type MediaRegion: string
    :param MediaRegion: The Region in which to create the meeting. Available values: ap-northeast-1 , ap-southeast-1 , ap-southeast-2 , ca-central-1 , eu-central-1 , eu-north-1 , eu-west-1 , eu-west-2 , eu-west-3 , sa-east-1 , us-east-1 , us-east-2 , us-west-1 , us-west-2 .

    :type Tags: list
    :param Tags: The tag key-value pairs.\n\n(dict) --Describes a tag applied to a resource.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :type NotificationsConfiguration: dict
    :param NotificationsConfiguration: The configuration for resource targets to receive notifications when meeting and attendee events occur.\n\nSnsTopicArn (string) --The SNS topic ARN.\n\nSqsQueueArn (string) --The SQS queue ARN.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Meeting': {
        'MeetingId': 'string',
        'ExternalMeetingId': 'string',
        'MediaPlacement': {
            'AudioHostUrl': 'string',
            'AudioFallbackUrl': 'string',
            'ScreenDataUrl': 'string',
            'ScreenSharingUrl': 'string',
            'ScreenViewingUrl': 'string',
            'SignalingUrl': 'string',
            'TurnControlUrl': 'string'
        },
        'MediaRegion': 'string'
    }
}


Response Structure

(dict) --

Meeting (dict) --
The meeting information, including the meeting ID and MediaPlacement .

MeetingId (string) --
The Amazon Chime SDK meeting ID.

ExternalMeetingId (string) --
The external meeting ID.

MediaPlacement (dict) --
The media placement for the meeting.

AudioHostUrl (string) --
The audio host URL.

AudioFallbackUrl (string) --
The audio fallback URL.

ScreenDataUrl (string) --
The screen data URL.

ScreenSharingUrl (string) --
The screen sharing URL.

ScreenViewingUrl (string) --
The screen viewing URL.

SignalingUrl (string) --
The signaling URL.

TurnControlUrl (string) --
The turn control URL.



MediaRegion (string) --
The Region in which to create the meeting. Available values: ap-northeast-1 , ap-southeast-1 , ap-southeast-2 , ca-central-1 , eu-central-1 , eu-north-1 , eu-west-1 , eu-west-2 , eu-west-3 , sa-east-1 , us-east-1 , us-east-2 , us-west-1 , us-west-2 .









Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.ResourceLimitExceededException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Meeting': {
            'MeetingId': 'string',
            'ExternalMeetingId': 'string',
            'MediaPlacement': {
                'AudioHostUrl': 'string',
                'AudioFallbackUrl': 'string',
                'ScreenDataUrl': 'string',
                'ScreenSharingUrl': 'string',
                'ScreenViewingUrl': 'string',
                'SignalingUrl': 'string',
                'TurnControlUrl': 'string'
            },
            'MediaRegion': 'string'
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.ResourceLimitExceededException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_phone_number_order(ProductType=None, E164PhoneNumbers=None):
    """
    Creates an order for phone numbers to be provisioned. Choose from Amazon Chime Business Calling and Amazon Chime Voice Connector product types. For toll-free numbers, you must use the Amazon Chime Voice Connector product type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_phone_number_order(
        ProductType='BusinessCalling'|'VoiceConnector',
        E164PhoneNumbers=[
            'string',
        ]
    )
    
    
    :type ProductType: string
    :param ProductType: [REQUIRED]\nThe phone number product type.\n

    :type E164PhoneNumbers: list
    :param E164PhoneNumbers: [REQUIRED]\nList of phone numbers, in E.164 format.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PhoneNumberOrder': {
        'PhoneNumberOrderId': 'string',
        'ProductType': 'BusinessCalling'|'VoiceConnector',
        'Status': 'Processing'|'Successful'|'Failed'|'Partial',
        'OrderedPhoneNumbers': [
            {
                'E164PhoneNumber': 'string',
                'Status': 'Processing'|'Acquired'|'Failed'
            },
        ],
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

PhoneNumberOrder (dict) --
The phone number order details.

PhoneNumberOrderId (string) --
The phone number order ID.

ProductType (string) --
The phone number order product type.

Status (string) --
The status of the phone number order.

OrderedPhoneNumbers (list) --
The ordered phone number details, such as the phone number in E.164 format and the phone number status.

(dict) --
A phone number for which an order has been placed.

E164PhoneNumber (string) --
The phone number, in E.164 format.

Status (string) --
The phone number status.





CreatedTimestamp (datetime) --
The phone number order creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated phone number order timestamp, in ISO 8601 format.









Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.AccessDeniedException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ResourceLimitExceededException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'PhoneNumberOrder': {
            'PhoneNumberOrderId': 'string',
            'ProductType': 'BusinessCalling'|'VoiceConnector',
            'Status': 'Processing'|'Successful'|'Failed'|'Partial',
            'OrderedPhoneNumbers': [
                {
                    'E164PhoneNumber': 'string',
                    'Status': 'Processing'|'Acquired'|'Failed'
                },
            ],
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.AccessDeniedException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ResourceLimitExceededException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_proxy_session(VoiceConnectorId=None, ParticipantPhoneNumbers=None, Name=None, ExpiryMinutes=None, Capabilities=None, NumberSelectionBehavior=None, GeoMatchLevel=None, GeoMatchParams=None):
    """
    Creates a proxy session on the specified Amazon Chime Voice Connector for the specified participant phone numbers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_proxy_session(
        VoiceConnectorId='string',
        ParticipantPhoneNumbers=[
            'string',
        ],
        Name='string',
        ExpiryMinutes=123,
        Capabilities=[
            'Voice'|'SMS',
        ],
        NumberSelectionBehavior='PreferSticky'|'AvoidSticky',
        GeoMatchLevel='Country'|'AreaCode',
        GeoMatchParams={
            'Country': 'string',
            'AreaCode': 'string'
        }
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime voice connector ID.\n

    :type ParticipantPhoneNumbers: list
    :param ParticipantPhoneNumbers: [REQUIRED]\nThe participant phone numbers.\n\n(string) --\n\n

    :type Name: string
    :param Name: The name of the proxy session.

    :type ExpiryMinutes: integer
    :param ExpiryMinutes: The number of minutes allowed for the proxy session.

    :type Capabilities: list
    :param Capabilities: [REQUIRED]\nThe proxy session capabilities.\n\n(string) --\n\n

    :type NumberSelectionBehavior: string
    :param NumberSelectionBehavior: The preference for proxy phone number reuse, or stickiness, between the same participants across sessions.

    :type GeoMatchLevel: string
    :param GeoMatchLevel: The preference for matching the country or area code of the proxy phone number with that of the first participant.

    :type GeoMatchParams: dict
    :param GeoMatchParams: The country and area code for the proxy phone number.\n\nCountry (string) -- [REQUIRED]The country.\n\nAreaCode (string) -- [REQUIRED]The area code.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ProxySession': {
        'VoiceConnectorId': 'string',
        'ProxySessionId': 'string',
        'Name': 'string',
        'Status': 'Open'|'InProgress'|'Closed',
        'ExpiryMinutes': 123,
        'Capabilities': [
            'Voice'|'SMS',
        ],
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1),
        'EndedTimestamp': datetime(2015, 1, 1),
        'Participants': [
            {
                'PhoneNumber': 'string',
                'ProxyPhoneNumber': 'string'
            },
        ],
        'NumberSelectionBehavior': 'PreferSticky'|'AvoidSticky',
        'GeoMatchLevel': 'Country'|'AreaCode',
        'GeoMatchParams': {
            'Country': 'string',
            'AreaCode': 'string'
        }
    }
}


Response Structure

(dict) --

ProxySession (dict) --
The proxy session details.

VoiceConnectorId (string) --
The Amazon Chime voice connector ID.

ProxySessionId (string) --
The proxy session ID.

Name (string) --
The name of the proxy session.

Status (string) --
The status of the proxy session.

ExpiryMinutes (integer) --
The number of minutes allowed for the proxy session.

Capabilities (list) --
The proxy session capabilities.

(string) --


CreatedTimestamp (datetime) --
The created timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated timestamp, in ISO 8601 format.

EndedTimestamp (datetime) --
The ended timestamp, in ISO 8601 format.

Participants (list) --
The proxy session participants.

(dict) --
The phone number and proxy phone number for a participant in an Amazon Chime Voice Connector proxy session.

PhoneNumber (string) --
The participant\'s phone number.

ProxyPhoneNumber (string) --
The participant\'s proxy phone number.





NumberSelectionBehavior (string) --
The preference for proxy phone number reuse, or stickiness, between the same participants across sessions.

GeoMatchLevel (string) --
The preference for matching the country or area code of the proxy phone number with that of the first participant.

GeoMatchParams (dict) --
The country and area code for the proxy phone number.

Country (string) --
The country.

AreaCode (string) --
The area code.











Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'ProxySession': {
            'VoiceConnectorId': 'string',
            'ProxySessionId': 'string',
            'Name': 'string',
            'Status': 'Open'|'InProgress'|'Closed',
            'ExpiryMinutes': 123,
            'Capabilities': [
                'Voice'|'SMS',
            ],
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1),
            'EndedTimestamp': datetime(2015, 1, 1),
            'Participants': [
                {
                    'PhoneNumber': 'string',
                    'ProxyPhoneNumber': 'string'
                },
            ],
            'NumberSelectionBehavior': 'PreferSticky'|'AvoidSticky',
            'GeoMatchLevel': 'Country'|'AreaCode',
            'GeoMatchParams': {
                'Country': 'string',
                'AreaCode': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_room(AccountId=None, Name=None, ClientRequestToken=None):
    """
    Creates a chat room for the specified Amazon Chime Enterprise account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_room(
        AccountId='string',
        Name='string',
        ClientRequestToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe room name.\n

    :type ClientRequestToken: string
    :param ClientRequestToken: The idempotency token for the request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Room': {
        'RoomId': 'string',
        'Name': 'string',
        'AccountId': 'string',
        'CreatedBy': 'string',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Room (dict) --
The room details.

RoomId (string) --
The room ID.

Name (string) --
The room name.

AccountId (string) --
The Amazon Chime account ID.

CreatedBy (string) --
The identifier of the room creator.

CreatedTimestamp (datetime) --
The room creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The room update timestamp, in ISO 8601 format.









Exceptions

Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ResourceLimitExceededException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Room': {
            'RoomId': 'string',
            'Name': 'string',
            'AccountId': 'string',
            'CreatedBy': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ResourceLimitExceededException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_room_membership(AccountId=None, RoomId=None, MemberId=None, Role=None):
    """
    Adds a member to a chat room in an Amazon Chime Enterprise account. A member can be either a user or a bot. The member role designates whether the member is a chat room administrator or a general chat room member.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_room_membership(
        AccountId='string',
        RoomId='string',
        MemberId='string',
        Role='Administrator'|'Member'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type RoomId: string
    :param RoomId: [REQUIRED]\nThe room ID.\n

    :type MemberId: string
    :param MemberId: [REQUIRED]\nThe Amazon Chime member ID (user ID or bot ID).\n

    :type Role: string
    :param Role: The role of the member.

    :rtype: dict

ReturnsResponse Syntax
{
    'RoomMembership': {
        'RoomId': 'string',
        'Member': {
            'MemberId': 'string',
            'MemberType': 'User'|'Bot'|'Webhook',
            'Email': 'string',
            'FullName': 'string',
            'AccountId': 'string'
        },
        'Role': 'Administrator'|'Member',
        'InvitedBy': 'string',
        'UpdatedTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

RoomMembership (dict) --
The room membership details.

RoomId (string) --
The room ID.

Member (dict) --
The member details, such as email address, name, member ID, and member type.

MemberId (string) --
The member ID (user ID or bot ID).

MemberType (string) --
The member type.

Email (string) --
The member email address.

FullName (string) --
The member name.

AccountId (string) --
The Amazon Chime account ID.



Role (string) --
The membership role.

InvitedBy (string) --
The identifier of the user that invited the room member.

UpdatedTimestamp (datetime) --
The room membership update timestamp, in ISO 8601 format.









Exceptions

Chime.Client.exceptions.ConflictException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.ResourceLimitExceededException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'RoomMembership': {
            'RoomId': 'string',
            'Member': {
                'MemberId': 'string',
                'MemberType': 'User'|'Bot'|'Webhook',
                'Email': 'string',
                'FullName': 'string',
                'AccountId': 'string'
            },
            'Role': 'Administrator'|'Member',
            'InvitedBy': 'string',
            'UpdatedTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.ConflictException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.ResourceLimitExceededException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_user(AccountId=None, Username=None, Email=None, UserType=None):
    """
    Creates a user under the specified Amazon Chime account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_user(
        AccountId='string',
        Username='string',
        Email='string',
        UserType='PrivateUser'|'SharedDevice'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type Username: string
    :param Username: The user name.

    :type Email: string
    :param Email: The user\'s email address.

    :type UserType: string
    :param UserType: The user type.

    :rtype: dict

ReturnsResponse Syntax
{
    'User': {
        'UserId': 'string',
        'AccountId': 'string',
        'PrimaryEmail': 'string',
        'PrimaryProvisionedNumber': 'string',
        'DisplayName': 'string',
        'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
        'UserType': 'PrivateUser'|'SharedDevice',
        'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
        'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
        'RegisteredOn': datetime(2015, 1, 1),
        'InvitedOn': datetime(2015, 1, 1),
        'AlexaForBusinessMetadata': {
            'IsAlexaForBusinessEnabled': True|False,
            'AlexaForBusinessRoomArn': 'string'
        },
        'PersonalPIN': 'string'
    }
}


Response Structure

(dict) --

User (dict) --
The user on the Amazon Chime account.

UserId (string) --
The user ID.

AccountId (string) --
The Amazon Chime account ID.

PrimaryEmail (string) --
The primary email address of the user.

PrimaryProvisionedNumber (string) --
The primary phone number associated with the user.

DisplayName (string) --
The display name of the user.

LicenseType (string) --
The license type for the user.

UserType (string) --
The user type.

UserRegistrationStatus (string) --
The user registration status.

UserInvitationStatus (string) --
The user invite status.

RegisteredOn (datetime) --
Date and time when the user is registered, in ISO 8601 format.

InvitedOn (datetime) --
Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

AlexaForBusinessMetadata (dict) --
The Alexa for Business metadata.

IsAlexaForBusinessEnabled (boolean) --
Starts or stops Alexa for Business.

AlexaForBusinessRoomArn (string) --
The ARN of the room resource.



PersonalPIN (string) --
The user\'s personal meeting PIN.









Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ConflictException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'User': {
            'UserId': 'string',
            'AccountId': 'string',
            'PrimaryEmail': 'string',
            'PrimaryProvisionedNumber': 'string',
            'DisplayName': 'string',
            'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'UserType': 'PrivateUser'|'SharedDevice',
            'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
            'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
            'RegisteredOn': datetime(2015, 1, 1),
            'InvitedOn': datetime(2015, 1, 1),
            'AlexaForBusinessMetadata': {
                'IsAlexaForBusinessEnabled': True|False,
                'AlexaForBusinessRoomArn': 'string'
            },
            'PersonalPIN': 'string'
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ConflictException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_voice_connector(Name=None, AwsRegion=None, RequireEncryption=None):
    """
    Creates an Amazon Chime Voice Connector under the administrator\'s AWS account. You can choose to create an Amazon Chime Voice Connector in a specific AWS Region.
    Enabling  CreateVoiceConnectorRequest$RequireEncryption configures your Amazon Chime Voice Connector to use TLS transport for SIP signaling and Secure RTP (SRTP) for media. Inbound calls use TLS transport, and unencrypted outbound calls are blocked.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_voice_connector(
        Name='string',
        AwsRegion='us-east-1'|'us-west-2',
        RequireEncryption=True|False
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the Amazon Chime Voice Connector.\n

    :type AwsRegion: string
    :param AwsRegion: The AWS Region in which the Amazon Chime Voice Connector is created. Default value: us-east-1 .

    :type RequireEncryption: boolean
    :param RequireEncryption: [REQUIRED]\nWhen enabled, requires encryption for the Amazon Chime Voice Connector.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VoiceConnector': {
        'VoiceConnectorId': 'string',
        'AwsRegion': 'us-east-1'|'us-west-2',
        'Name': 'string',
        'OutboundHostName': 'string',
        'RequireEncryption': True|False,
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

VoiceConnector (dict) --
The Amazon Chime Voice Connector details.

VoiceConnectorId (string) --
The Amazon Chime Voice Connector ID.

AwsRegion (string) --
The AWS Region in which the Amazon Chime Voice Connector is created. Default: us-east-1 .

Name (string) --
The name of the Amazon Chime Voice Connector.

OutboundHostName (string) --
The outbound host name for the Amazon Chime Voice Connector.

RequireEncryption (boolean) --
Designates whether encryption is required for the Amazon Chime Voice Connector.

CreatedTimestamp (datetime) --
The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.









Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.AccessDeniedException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ResourceLimitExceededException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'VoiceConnector': {
            'VoiceConnectorId': 'string',
            'AwsRegion': 'us-east-1'|'us-west-2',
            'Name': 'string',
            'OutboundHostName': 'string',
            'RequireEncryption': True|False,
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.AccessDeniedException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ResourceLimitExceededException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def create_voice_connector_group(Name=None, VoiceConnectorItems=None):
    """
    Creates an Amazon Chime Voice Connector group under the administrator\'s AWS account. You can associate Amazon Chime Voice Connectors with the Amazon Chime Voice Connector group by including VoiceConnectorItems in the request.
    You can include Amazon Chime Voice Connectors from different AWS Regions in your group. This creates a fault tolerant mechanism for fallback in case of availability events.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_voice_connector_group(
        Name='string',
        VoiceConnectorItems=[
            {
                'VoiceConnectorId': 'string',
                'Priority': 123
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the Amazon Chime Voice Connector group.\n

    :type VoiceConnectorItems: list
    :param VoiceConnectorItems: The Amazon Chime Voice Connectors to route inbound calls to.\n\n(dict) --For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to route inbound calls. Includes priority configuration settings. Limit: 3 VoiceConnectorItems per Amazon Chime Voice Connector group.\n\nVoiceConnectorId (string) -- [REQUIRED]The Amazon Chime Voice Connector ID.\n\nPriority (integer) -- [REQUIRED]The priority associated with the Amazon Chime Voice Connector, with 1 being the highest priority. Higher priority Amazon Chime Voice Connectors are attempted first.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VoiceConnectorGroup': {
        'VoiceConnectorGroupId': 'string',
        'Name': 'string',
        'VoiceConnectorItems': [
            {
                'VoiceConnectorId': 'string',
                'Priority': 123
            },
        ],
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

VoiceConnectorGroup (dict) --
The Amazon Chime Voice Connector group details.

VoiceConnectorGroupId (string) --
The Amazon Chime Voice Connector group ID.

Name (string) --
The name of the Amazon Chime Voice Connector group.

VoiceConnectorItems (list) --
The Amazon Chime Voice Connectors to which to route inbound calls.

(dict) --
For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to route inbound calls. Includes priority configuration settings. Limit: 3 VoiceConnectorItems per Amazon Chime Voice Connector group.

VoiceConnectorId (string) --
The Amazon Chime Voice Connector ID.

Priority (integer) --
The priority associated with the Amazon Chime Voice Connector, with 1 being the highest priority. Higher priority Amazon Chime Voice Connectors are attempted first.





CreatedTimestamp (datetime) --
The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.









Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.AccessDeniedException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ResourceLimitExceededException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'VoiceConnectorGroup': {
            'VoiceConnectorGroupId': 'string',
            'Name': 'string',
            'VoiceConnectorItems': [
                {
                    'VoiceConnectorId': 'string',
                    'Priority': 123
                },
            ],
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.AccessDeniedException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ResourceLimitExceededException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_account(AccountId=None):
    """
    Deletes the specified Amazon Chime account. You must suspend all users before deleting a Team account. You can use the  BatchSuspendUser action to do so.
    For EnterpriseLWA and EnterpriseAD accounts, you must release the claimed domains for your Amazon Chime account before deletion. As soon as you release the domain, all users under that account are suspended.
    Deleted accounts appear in your Disabled accounts list for 90 days. To restore a deleted account from your Disabled accounts list, you must contact AWS Support.
    After 90 days, deleted accounts are permanently removed from your Disabled accounts list.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_account(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.UnprocessableEntityException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {}
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.UnprocessableEntityException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_attendee(MeetingId=None, AttendeeId=None):
    """
    Deletes an attendee from the specified Amazon Chime SDK meeting and deletes their JoinToken . Attendees are automatically deleted when a Amazon Chime SDK meeting is deleted. For more information about the Amazon Chime SDK, see Using the Amazon Chime SDK in the Amazon Chime Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_attendee(
        MeetingId='string',
        AttendeeId='string'
    )
    
    
    :type MeetingId: string
    :param MeetingId: [REQUIRED]\nThe Amazon Chime SDK meeting ID.\n

    :type AttendeeId: string
    :param AttendeeId: [REQUIRED]\nThe Amazon Chime SDK attendee ID.\n

    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_events_configuration(AccountId=None, BotId=None):
    """
    Deletes the events configuration that allows a bot to receive outgoing events.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_events_configuration(
        AccountId='string',
        BotId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type BotId: string
    :param BotId: [REQUIRED]\nThe bot ID.\n

    :returns: 
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ResourceLimitExceededException
    
    """
    pass

def delete_meeting(MeetingId=None):
    """
    Deletes the specified Amazon Chime SDK meeting. When a meeting is deleted, its attendees are also deleted and clients can no longer join it. For more information about the Amazon Chime SDK, see Using the Amazon Chime SDK in the Amazon Chime Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_meeting(
        MeetingId='string'
    )
    
    
    :type MeetingId: string
    :param MeetingId: [REQUIRED]\nThe Amazon Chime SDK meeting ID.\n

    """
    pass

def delete_phone_number(PhoneNumberId=None):
    """
    Moves the specified phone number into the Deletion queue . A phone number must be disassociated from any users or Amazon Chime Voice Connectors before it can be deleted.
    Deleted phone numbers remain in the Deletion queue for 7 days before they are deleted permanently.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_phone_number(
        PhoneNumberId='string'
    )
    
    
    :type PhoneNumberId: string
    :param PhoneNumberId: [REQUIRED]\nThe phone number ID.\n

    """
    pass

def delete_proxy_session(VoiceConnectorId=None, ProxySessionId=None):
    """
    Deletes the specified proxy session from the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_proxy_session(
        VoiceConnectorId='string',
        ProxySessionId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime voice connector ID.\n

    :type ProxySessionId: string
    :param ProxySessionId: [REQUIRED]\nThe proxy session ID.\n

    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_room(AccountId=None, RoomId=None):
    """
    Deletes a chat room in an Amazon Chime Enterprise account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_room(
        AccountId='string',
        RoomId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type RoomId: string
    :param RoomId: [REQUIRED]\nThe chat room ID.\n

    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_room_membership(AccountId=None, RoomId=None, MemberId=None):
    """
    Removes a member from a chat room in an Amazon Chime Enterprise account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_room_membership(
        AccountId='string',
        RoomId='string',
        MemberId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type RoomId: string
    :param RoomId: [REQUIRED]\nThe room ID.\n

    :type MemberId: string
    :param MemberId: [REQUIRED]\nThe member ID (user ID or bot ID).\n

    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def delete_voice_connector(VoiceConnectorId=None):
    """
    Deletes the specified Amazon Chime Voice Connector. Any phone numbers associated with the Amazon Chime Voice Connector must be disassociated from it before it can be deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_voice_connector(
        VoiceConnectorId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    """
    pass

def delete_voice_connector_group(VoiceConnectorGroupId=None):
    """
    Deletes the specified Amazon Chime Voice Connector group. Any VoiceConnectorItems and phone numbers associated with the group must be removed before it can be deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_voice_connector_group(
        VoiceConnectorGroupId='string'
    )
    
    
    :type VoiceConnectorGroupId: string
    :param VoiceConnectorGroupId: [REQUIRED]\nThe Amazon Chime Voice Connector group ID.\n

    """
    pass

def delete_voice_connector_origination(VoiceConnectorId=None):
    """
    Deletes the origination settings for the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_voice_connector_origination(
        VoiceConnectorId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    """
    pass

def delete_voice_connector_proxy(VoiceConnectorId=None):
    """
    Deletes the proxy configuration from the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_voice_connector_proxy(
        VoiceConnectorId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    """
    pass

def delete_voice_connector_streaming_configuration(VoiceConnectorId=None):
    """
    Deletes the streaming configuration for the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_voice_connector_streaming_configuration(
        VoiceConnectorId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    """
    pass

def delete_voice_connector_termination(VoiceConnectorId=None):
    """
    Deletes the termination settings for the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_voice_connector_termination(
        VoiceConnectorId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    """
    pass

def delete_voice_connector_termination_credentials(VoiceConnectorId=None, Usernames=None):
    """
    Deletes the specified SIP credentials used by your equipment to authenticate during call termination.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_voice_connector_termination_credentials(
        VoiceConnectorId='string',
        Usernames=[
            'string',
        ]
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :type Usernames: list
    :param Usernames: The RFC2617 compliant username associated with the SIP credentials, in US-ASCII format.\n\n(string) --\n\n

    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def disassociate_phone_number_from_user(AccountId=None, UserId=None):
    """
    Disassociates the primary provisioned phone number from the specified Amazon Chime user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_phone_number_from_user(
        AccountId='string',
        UserId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type UserId: string
    :param UserId: [REQUIRED]\nThe user ID.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_phone_numbers_from_voice_connector(VoiceConnectorId=None, E164PhoneNumbers=None):
    """
    Disassociates the specified phone numbers from the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_phone_numbers_from_voice_connector(
        VoiceConnectorId='string',
        E164PhoneNumbers=[
            'string',
        ]
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :type E164PhoneNumbers: list
    :param E164PhoneNumbers: List of phone numbers, in E.164 format.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PhoneNumberErrors': [
        {
            'PhoneNumberId': 'string',
            'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

PhoneNumberErrors (list) --
If the action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.

(dict) --
If the phone number action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.

PhoneNumberId (string) --
The phone number ID for which the action failed.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.











Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'PhoneNumberErrors': [
            {
                'PhoneNumberId': 'string',
                'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def disassociate_phone_numbers_from_voice_connector_group(VoiceConnectorGroupId=None, E164PhoneNumbers=None):
    """
    Disassociates the specified phone numbers from the specified Amazon Chime Voice Connector group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_phone_numbers_from_voice_connector_group(
        VoiceConnectorGroupId='string',
        E164PhoneNumbers=[
            'string',
        ]
    )
    
    
    :type VoiceConnectorGroupId: string
    :param VoiceConnectorGroupId: [REQUIRED]\nThe Amazon Chime Voice Connector group ID.\n

    :type E164PhoneNumbers: list
    :param E164PhoneNumbers: List of phone numbers, in E.164 format.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PhoneNumberErrors': [
        {
            'PhoneNumberId': 'string',
            'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

PhoneNumberErrors (list) --
If the action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.

(dict) --
If the phone number action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.

PhoneNumberId (string) --
The phone number ID for which the action failed.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.











Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'PhoneNumberErrors': [
            {
                'PhoneNumberId': 'string',
                'ErrorCode': 'BadRequest'|'Conflict'|'Forbidden'|'NotFound'|'PreconditionFailed'|'ResourceLimitExceeded'|'ServiceFailure'|'AccessDenied'|'ServiceUnavailable'|'Throttled'|'Unauthorized'|'Unprocessable'|'VoiceConnectorGroupAssociationsExist'|'PhoneNumberAssociationsExist',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def disassociate_signin_delegate_groups_from_account(AccountId=None, GroupNames=None):
    """
    Disassociates the specified sign-in delegate groups from the specified Amazon Chime account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_signin_delegate_groups_from_account(
        AccountId='string',
        GroupNames=[
            'string',
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type GroupNames: list
    :param GroupNames: [REQUIRED]\nThe sign-in delegate group names.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def get_account(AccountId=None):
    """
    Retrieves details for the specified Amazon Chime account, such as account type and supported licenses.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_account(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Account': {
        'AwsAccountId': 'string',
        'AccountId': 'string',
        'Name': 'string',
        'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
        'SupportedLicenses': [
            'Basic'|'Plus'|'Pro'|'ProTrial',
        ],
        'SigninDelegateGroups': [
            {
                'GroupName': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Account (dict) --The Amazon Chime account details.

AwsAccountId (string) --The AWS account ID.

AccountId (string) --The Amazon Chime account ID.

Name (string) --The Amazon Chime account name.

AccountType (string) --The Amazon Chime account type. For more information about different account types, see Managing Your Amazon Chime Accounts in the Amazon Chime Administration Guide .

CreatedTimestamp (datetime) --The Amazon Chime account creation timestamp, in ISO 8601 format.

DefaultLicense (string) --The default license for the Amazon Chime account.

SupportedLicenses (list) --Supported licenses for the Amazon Chime account.

(string) --


SigninDelegateGroups (list) --The sign-in delegate groups associated with the account.

(dict) --An Active Directory (AD) group whose members are granted permission to act as delegates.

GroupName (string) --The group name.












Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Account': {
            'AwsAccountId': 'string',
            'AccountId': 'string',
            'Name': 'string',
            'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'SupportedLicenses': [
                'Basic'|'Plus'|'Pro'|'ProTrial',
            ],
            'SigninDelegateGroups': [
                {
                    'GroupName': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def get_account_settings(AccountId=None):
    """
    Retrieves account settings for the specified Amazon Chime account ID, such as remote control and dial out settings. For more information about these settings, see Use the Policies Page in the Amazon Chime Administration Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_account_settings(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'AccountSettings': {
        'DisableRemoteControl': True|False,
        'EnableDialOut': True|False
    }
}


Response Structure

(dict) --
AccountSettings (dict) --The Amazon Chime account settings.

DisableRemoteControl (boolean) --Setting that stops or starts remote control of shared screens during meetings.

EnableDialOut (boolean) --Setting that allows meeting participants to choose the Call me at a phone number option. For more information, see Join a Meeting without the Amazon Chime App .








Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'AccountSettings': {
            'DisableRemoteControl': True|False,
            'EnableDialOut': True|False
        }
    }
    
    
    """
    pass

def get_attendee(MeetingId=None, AttendeeId=None):
    """
    Gets the Amazon Chime SDK attendee details for a specified meeting ID and attendee ID. For more information about the Amazon Chime SDK, see Using the Amazon Chime SDK in the Amazon Chime Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_attendee(
        MeetingId='string',
        AttendeeId='string'
    )
    
    
    :type MeetingId: string
    :param MeetingId: [REQUIRED]\nThe Amazon Chime SDK meeting ID.\n

    :type AttendeeId: string
    :param AttendeeId: [REQUIRED]\nThe Amazon Chime SDK attendee ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Attendee': {
        'ExternalUserId': 'string',
        'AttendeeId': 'string',
        'JoinToken': 'string'
    }
}


Response Structure

(dict) --

Attendee (dict) --
The Amazon Chime SDK attendee information.

ExternalUserId (string) --
The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a builder application.

AttendeeId (string) --
The Amazon Chime SDK attendee ID.

JoinToken (string) --
The join token used by the Amazon Chime SDK attendee.









Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Attendee': {
            'ExternalUserId': 'string',
            'AttendeeId': 'string',
            'JoinToken': 'string'
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def get_bot(AccountId=None, BotId=None):
    """
    Retrieves details for the specified bot, such as bot email address, bot type, status, and display name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_bot(
        AccountId='string',
        BotId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type BotId: string
    :param BotId: [REQUIRED]\nThe bot ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Bot': {
        'BotId': 'string',
        'UserId': 'string',
        'DisplayName': 'string',
        'BotType': 'ChatBot',
        'Disabled': True|False,
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1),
        'BotEmail': 'string',
        'SecurityToken': 'string'
    }
}


Response Structure

(dict) --

Bot (dict) --
The chat bot details.

BotId (string) --
The bot ID.

UserId (string) --
The unique ID for the bot user.

DisplayName (string) --
The bot display name.

BotType (string) --
The bot type.

Disabled (boolean) --
When true, the bot is stopped from running in your account.

CreatedTimestamp (datetime) --
The bot creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated bot timestamp, in ISO 8601 format.

BotEmail (string) --
The bot email address.

SecurityToken (string) --
The security token used to authenticate Amazon Chime with the outgoing event endpoint.









Exceptions

Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException


    :return: {
        'Bot': {
            'BotId': 'string',
            'UserId': 'string',
            'DisplayName': 'string',
            'BotType': 'ChatBot',
            'Disabled': True|False,
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1),
            'BotEmail': 'string',
            'SecurityToken': 'string'
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    
    """
    pass

def get_events_configuration(AccountId=None, BotId=None):
    """
    Gets details for an events configuration that allows a bot to receive outgoing events, such as an HTTPS endpoint or Lambda function ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_events_configuration(
        AccountId='string',
        BotId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type BotId: string
    :param BotId: [REQUIRED]\nThe bot ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EventsConfiguration': {
        'BotId': 'string',
        'OutboundEventsHTTPSEndpoint': 'string',
        'LambdaFunctionArn': 'string'
    }
}


Response Structure

(dict) --

EventsConfiguration (dict) --
The events configuration details.

BotId (string) --
The bot ID.

OutboundEventsHTTPSEndpoint (string) --
HTTPS endpoint that allows a bot to receive outgoing events.

LambdaFunctionArn (string) --
Lambda function ARN that allows a bot to receive outgoing events.









Exceptions

Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ResourceLimitExceededException
Chime.Client.exceptions.NotFoundException


    :return: {
        'EventsConfiguration': {
            'BotId': 'string',
            'OutboundEventsHTTPSEndpoint': 'string',
            'LambdaFunctionArn': 'string'
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ResourceLimitExceededException
    Chime.Client.exceptions.NotFoundException
    
    """
    pass

def get_global_settings():
    """
    Retrieves global settings for the administrator\'s AWS account, such as Amazon Chime Business Calling and Amazon Chime Voice Connector settings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_global_settings()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'BusinessCalling': {
        'CdrBucket': 'string'
    },
    'VoiceConnector': {
        'CdrBucket': 'string'
    }
}


Response Structure

(dict) --
BusinessCalling (dict) --The Amazon Chime Business Calling settings.

CdrBucket (string) --The Amazon S3 bucket designated for call detail record storage.



VoiceConnector (dict) --The Amazon Chime Voice Connector settings.

CdrBucket (string) --The Amazon S3 bucket designated for call detail record storage.








Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'BusinessCalling': {
            'CdrBucket': 'string'
        },
        'VoiceConnector': {
            'CdrBucket': 'string'
        }
    }
    
    
    """
    pass

def get_meeting(MeetingId=None):
    """
    Gets the Amazon Chime SDK meeting details for the specified meeting ID. For more information about the Amazon Chime SDK, see Using the Amazon Chime SDK in the Amazon Chime Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_meeting(
        MeetingId='string'
    )
    
    
    :type MeetingId: string
    :param MeetingId: [REQUIRED]\nThe Amazon Chime SDK meeting ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Meeting': {
        'MeetingId': 'string',
        'ExternalMeetingId': 'string',
        'MediaPlacement': {
            'AudioHostUrl': 'string',
            'AudioFallbackUrl': 'string',
            'ScreenDataUrl': 'string',
            'ScreenSharingUrl': 'string',
            'ScreenViewingUrl': 'string',
            'SignalingUrl': 'string',
            'TurnControlUrl': 'string'
        },
        'MediaRegion': 'string'
    }
}


Response Structure

(dict) --
Meeting (dict) --The Amazon Chime SDK meeting information.

MeetingId (string) --The Amazon Chime SDK meeting ID.

ExternalMeetingId (string) --The external meeting ID.

MediaPlacement (dict) --The media placement for the meeting.

AudioHostUrl (string) --The audio host URL.

AudioFallbackUrl (string) --The audio fallback URL.

ScreenDataUrl (string) --The screen data URL.

ScreenSharingUrl (string) --The screen sharing URL.

ScreenViewingUrl (string) --The screen viewing URL.

SignalingUrl (string) --The signaling URL.

TurnControlUrl (string) --The turn control URL.



MediaRegion (string) --The Region in which to create the meeting. Available values: ap-northeast-1 , ap-southeast-1 , ap-southeast-2 , ca-central-1 , eu-central-1 , eu-north-1 , eu-west-1 , eu-west-2 , eu-west-3 , sa-east-1 , us-east-1 , us-east-2 , us-west-1 , us-west-2 .








Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Meeting': {
            'MeetingId': 'string',
            'ExternalMeetingId': 'string',
            'MediaPlacement': {
                'AudioHostUrl': 'string',
                'AudioFallbackUrl': 'string',
                'ScreenDataUrl': 'string',
                'ScreenSharingUrl': 'string',
                'ScreenViewingUrl': 'string',
                'SignalingUrl': 'string',
                'TurnControlUrl': 'string'
            },
            'MediaRegion': 'string'
        }
    }
    
    
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

def get_phone_number(PhoneNumberId=None):
    """
    Retrieves details for the specified phone number ID, such as associations, capabilities, and product type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_phone_number(
        PhoneNumberId='string'
    )
    
    
    :type PhoneNumberId: string
    :param PhoneNumberId: [REQUIRED]\nThe phone number ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'PhoneNumber': {
        'PhoneNumberId': 'string',
        'E164PhoneNumber': 'string',
        'Type': 'Local'|'TollFree',
        'ProductType': 'BusinessCalling'|'VoiceConnector',
        'Status': 'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'|'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
        'Capabilities': {
            'InboundCall': True|False,
            'OutboundCall': True|False,
            'InboundSMS': True|False,
            'OutboundSMS': True|False,
            'InboundMMS': True|False,
            'OutboundMMS': True|False
        },
        'Associations': [
            {
                'Value': 'string',
                'Name': 'AccountId'|'UserId'|'VoiceConnectorId'|'VoiceConnectorGroupId',
                'AssociatedTimestamp': datetime(2015, 1, 1)
            },
        ],
        'CallingName': 'string',
        'CallingNameStatus': 'Unassigned'|'UpdateInProgress'|'UpdateSucceeded'|'UpdateFailed',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1),
        'DeletionTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
PhoneNumber (dict) --The phone number details.

PhoneNumberId (string) --The phone number ID.

E164PhoneNumber (string) --The phone number, in E.164 format.

Type (string) --The phone number type.

ProductType (string) --The phone number product type.

Status (string) --The phone number status.

Capabilities (dict) --The phone number capabilities.

InboundCall (boolean) --Allows or denies inbound calling for the specified phone number.

OutboundCall (boolean) --Allows or denies outbound calling for the specified phone number.

InboundSMS (boolean) --Allows or denies inbound SMS messaging for the specified phone number.

OutboundSMS (boolean) --Allows or denies outbound SMS messaging for the specified phone number.

InboundMMS (boolean) --Allows or denies inbound MMS messaging for the specified phone number.

OutboundMMS (boolean) --Allows or denies outbound MMS messaging for the specified phone number.



Associations (list) --The phone number associations.

(dict) --The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID, Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

Value (string) --Contains the ID for the entity specified in Name.

Name (string) --Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

AssociatedTimestamp (datetime) --The timestamp of the phone number association, in ISO 8601 format.





CallingName (string) --The outbound calling name associated with the phone number.

CallingNameStatus (string) --The outbound calling name status.

CreatedTimestamp (datetime) --The phone number creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --The updated phone number timestamp, in ISO 8601 format.

DeletionTimestamp (datetime) --The deleted phone number timestamp, in ISO 8601 format.








Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'PhoneNumber': {
            'PhoneNumberId': 'string',
            'E164PhoneNumber': 'string',
            'Type': 'Local'|'TollFree',
            'ProductType': 'BusinessCalling'|'VoiceConnector',
            'Status': 'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'|'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
            'Capabilities': {
                'InboundCall': True|False,
                'OutboundCall': True|False,
                'InboundSMS': True|False,
                'OutboundSMS': True|False,
                'InboundMMS': True|False,
                'OutboundMMS': True|False
            },
            'Associations': [
                {
                    'Value': 'string',
                    'Name': 'AccountId'|'UserId'|'VoiceConnectorId'|'VoiceConnectorGroupId',
                    'AssociatedTimestamp': datetime(2015, 1, 1)
                },
            ],
            'CallingName': 'string',
            'CallingNameStatus': 'Unassigned'|'UpdateInProgress'|'UpdateSucceeded'|'UpdateFailed',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1),
            'DeletionTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_phone_number_order(PhoneNumberOrderId=None):
    """
    Retrieves details for the specified phone number order, such as order creation timestamp, phone numbers in E.164 format, product type, and order status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_phone_number_order(
        PhoneNumberOrderId='string'
    )
    
    
    :type PhoneNumberOrderId: string
    :param PhoneNumberOrderId: [REQUIRED]\nThe ID for the phone number order.\n

    :rtype: dict
ReturnsResponse Syntax{
    'PhoneNumberOrder': {
        'PhoneNumberOrderId': 'string',
        'ProductType': 'BusinessCalling'|'VoiceConnector',
        'Status': 'Processing'|'Successful'|'Failed'|'Partial',
        'OrderedPhoneNumbers': [
            {
                'E164PhoneNumber': 'string',
                'Status': 'Processing'|'Acquired'|'Failed'
            },
        ],
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
PhoneNumberOrder (dict) --The phone number order details.

PhoneNumberOrderId (string) --The phone number order ID.

ProductType (string) --The phone number order product type.

Status (string) --The status of the phone number order.

OrderedPhoneNumbers (list) --The ordered phone number details, such as the phone number in E.164 format and the phone number status.

(dict) --A phone number for which an order has been placed.

E164PhoneNumber (string) --The phone number, in E.164 format.

Status (string) --The phone number status.





CreatedTimestamp (datetime) --The phone number order creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --The updated phone number order timestamp, in ISO 8601 format.








Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'PhoneNumberOrder': {
            'PhoneNumberOrderId': 'string',
            'ProductType': 'BusinessCalling'|'VoiceConnector',
            'Status': 'Processing'|'Successful'|'Failed'|'Partial',
            'OrderedPhoneNumbers': [
                {
                    'E164PhoneNumber': 'string',
                    'Status': 'Processing'|'Acquired'|'Failed'
                },
            ],
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_phone_number_settings():
    """
    Retrieves the phone number settings for the administrator\'s AWS account, such as the default outbound calling name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_phone_number_settings()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'CallingName': 'string',
    'CallingNameUpdatedTimestamp': datetime(2015, 1, 1)
}


Response Structure

(dict) --
CallingName (string) --The default outbound calling name for the account.

CallingNameUpdatedTimestamp (datetime) --The updated outbound calling name timestamp, in ISO 8601 format.






Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'CallingName': 'string',
        'CallingNameUpdatedTimestamp': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def get_proxy_session(VoiceConnectorId=None, ProxySessionId=None):
    """
    Gets the specified proxy session details for the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_proxy_session(
        VoiceConnectorId='string',
        ProxySessionId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime voice connector ID.\n

    :type ProxySessionId: string
    :param ProxySessionId: [REQUIRED]\nThe proxy session ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ProxySession': {
        'VoiceConnectorId': 'string',
        'ProxySessionId': 'string',
        'Name': 'string',
        'Status': 'Open'|'InProgress'|'Closed',
        'ExpiryMinutes': 123,
        'Capabilities': [
            'Voice'|'SMS',
        ],
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1),
        'EndedTimestamp': datetime(2015, 1, 1),
        'Participants': [
            {
                'PhoneNumber': 'string',
                'ProxyPhoneNumber': 'string'
            },
        ],
        'NumberSelectionBehavior': 'PreferSticky'|'AvoidSticky',
        'GeoMatchLevel': 'Country'|'AreaCode',
        'GeoMatchParams': {
            'Country': 'string',
            'AreaCode': 'string'
        }
    }
}


Response Structure

(dict) --

ProxySession (dict) --
The proxy session details.

VoiceConnectorId (string) --
The Amazon Chime voice connector ID.

ProxySessionId (string) --
The proxy session ID.

Name (string) --
The name of the proxy session.

Status (string) --
The status of the proxy session.

ExpiryMinutes (integer) --
The number of minutes allowed for the proxy session.

Capabilities (list) --
The proxy session capabilities.

(string) --


CreatedTimestamp (datetime) --
The created timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated timestamp, in ISO 8601 format.

EndedTimestamp (datetime) --
The ended timestamp, in ISO 8601 format.

Participants (list) --
The proxy session participants.

(dict) --
The phone number and proxy phone number for a participant in an Amazon Chime Voice Connector proxy session.

PhoneNumber (string) --
The participant\'s phone number.

ProxyPhoneNumber (string) --
The participant\'s proxy phone number.





NumberSelectionBehavior (string) --
The preference for proxy phone number reuse, or stickiness, between the same participants across sessions.

GeoMatchLevel (string) --
The preference for matching the country or area code of the proxy phone number with that of the first participant.

GeoMatchParams (dict) --
The country and area code for the proxy phone number.

Country (string) --
The country.

AreaCode (string) --
The area code.











Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'ProxySession': {
            'VoiceConnectorId': 'string',
            'ProxySessionId': 'string',
            'Name': 'string',
            'Status': 'Open'|'InProgress'|'Closed',
            'ExpiryMinutes': 123,
            'Capabilities': [
                'Voice'|'SMS',
            ],
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1),
            'EndedTimestamp': datetime(2015, 1, 1),
            'Participants': [
                {
                    'PhoneNumber': 'string',
                    'ProxyPhoneNumber': 'string'
                },
            ],
            'NumberSelectionBehavior': 'PreferSticky'|'AvoidSticky',
            'GeoMatchLevel': 'Country'|'AreaCode',
            'GeoMatchParams': {
                'Country': 'string',
                'AreaCode': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_retention_settings(AccountId=None):
    """
    Gets the retention settings for the specified Amazon Chime Enterprise account. For more information about retention settings, see Managing Chat Retention Policies in the Amazon Chime Administration Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_retention_settings(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'RetentionSettings': {
        'RoomRetentionSettings': {
            'RetentionDays': 123
        },
        'ConversationRetentionSettings': {
            'RetentionDays': 123
        }
    },
    'InitiateDeletionTimestamp': datetime(2015, 1, 1)
}


Response Structure

(dict) --
RetentionSettings (dict) --The retention settings.

RoomRetentionSettings (dict) --The chat room retention settings.

RetentionDays (integer) --The number of days for which to retain chat room messages.



ConversationRetentionSettings (dict) --The chat conversation retention settings.

RetentionDays (integer) --The number of days for which to retain chat conversation messages.





InitiateDeletionTimestamp (datetime) --The timestamp representing the time at which the specified items are permanently deleted, in ISO 8601 format.






Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'RetentionSettings': {
            'RoomRetentionSettings': {
                'RetentionDays': 123
            },
            'ConversationRetentionSettings': {
                'RetentionDays': 123
            }
        },
        'InitiateDeletionTimestamp': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def get_room(AccountId=None, RoomId=None):
    """
    Retrieves room details, such as the room name, for a room in an Amazon Chime Enterprise account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_room(
        AccountId='string',
        RoomId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type RoomId: string
    :param RoomId: [REQUIRED]\nThe room ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Room': {
        'RoomId': 'string',
        'Name': 'string',
        'AccountId': 'string',
        'CreatedBy': 'string',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Room (dict) --
The room details.

RoomId (string) --
The room ID.

Name (string) --
The room name.

AccountId (string) --
The Amazon Chime account ID.

CreatedBy (string) --
The identifier of the room creator.

CreatedTimestamp (datetime) --
The room creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The room update timestamp, in ISO 8601 format.









Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Room': {
            'RoomId': 'string',
            'Name': 'string',
            'AccountId': 'string',
            'CreatedBy': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def get_user(AccountId=None, UserId=None):
    """
    Retrieves details for the specified user ID, such as primary email address, license type, and personal meeting PIN.
    To retrieve user details with an email address instead of a user ID, use the  ListUsers action, and then filter by email address.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_user(
        AccountId='string',
        UserId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type UserId: string
    :param UserId: [REQUIRED]\nThe user ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'User': {
        'UserId': 'string',
        'AccountId': 'string',
        'PrimaryEmail': 'string',
        'PrimaryProvisionedNumber': 'string',
        'DisplayName': 'string',
        'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
        'UserType': 'PrivateUser'|'SharedDevice',
        'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
        'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
        'RegisteredOn': datetime(2015, 1, 1),
        'InvitedOn': datetime(2015, 1, 1),
        'AlexaForBusinessMetadata': {
            'IsAlexaForBusinessEnabled': True|False,
            'AlexaForBusinessRoomArn': 'string'
        },
        'PersonalPIN': 'string'
    }
}


Response Structure

(dict) --

User (dict) --
The user details.

UserId (string) --
The user ID.

AccountId (string) --
The Amazon Chime account ID.

PrimaryEmail (string) --
The primary email address of the user.

PrimaryProvisionedNumber (string) --
The primary phone number associated with the user.

DisplayName (string) --
The display name of the user.

LicenseType (string) --
The license type for the user.

UserType (string) --
The user type.

UserRegistrationStatus (string) --
The user registration status.

UserInvitationStatus (string) --
The user invite status.

RegisteredOn (datetime) --
Date and time when the user is registered, in ISO 8601 format.

InvitedOn (datetime) --
Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

AlexaForBusinessMetadata (dict) --
The Alexa for Business metadata.

IsAlexaForBusinessEnabled (boolean) --
Starts or stops Alexa for Business.

AlexaForBusinessRoomArn (string) --
The ARN of the room resource.



PersonalPIN (string) --
The user\'s personal meeting PIN.









Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'User': {
            'UserId': 'string',
            'AccountId': 'string',
            'PrimaryEmail': 'string',
            'PrimaryProvisionedNumber': 'string',
            'DisplayName': 'string',
            'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'UserType': 'PrivateUser'|'SharedDevice',
            'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
            'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
            'RegisteredOn': datetime(2015, 1, 1),
            'InvitedOn': datetime(2015, 1, 1),
            'AlexaForBusinessMetadata': {
                'IsAlexaForBusinessEnabled': True|False,
                'AlexaForBusinessRoomArn': 'string'
            },
            'PersonalPIN': 'string'
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def get_user_settings(AccountId=None, UserId=None):
    """
    Retrieves settings for the specified user ID, such as any associated phone number settings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_user_settings(
        AccountId='string',
        UserId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type UserId: string
    :param UserId: [REQUIRED]\nThe user ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UserSettings': {
        'Telephony': {
            'InboundCalling': True|False,
            'OutboundCalling': True|False,
            'SMS': True|False
        }
    }
}


Response Structure

(dict) --

UserSettings (dict) --
The user settings.

Telephony (dict) --
The telephony settings associated with the user.

InboundCalling (boolean) --
Allows or denies inbound calling.

OutboundCalling (boolean) --
Allows or denies outbound calling.

SMS (boolean) --
Allows or denies SMS messaging.











Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'UserSettings': {
            'Telephony': {
                'InboundCalling': True|False,
                'OutboundCalling': True|False,
                'SMS': True|False
            }
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def get_voice_connector(VoiceConnectorId=None):
    """
    Retrieves details for the specified Amazon Chime Voice Connector, such as timestamps, name, outbound host, and encryption requirements.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_voice_connector(
        VoiceConnectorId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'VoiceConnector': {
        'VoiceConnectorId': 'string',
        'AwsRegion': 'us-east-1'|'us-west-2',
        'Name': 'string',
        'OutboundHostName': 'string',
        'RequireEncryption': True|False,
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
VoiceConnector (dict) --The Amazon Chime Voice Connector details.

VoiceConnectorId (string) --The Amazon Chime Voice Connector ID.

AwsRegion (string) --The AWS Region in which the Amazon Chime Voice Connector is created. Default: us-east-1 .

Name (string) --The name of the Amazon Chime Voice Connector.

OutboundHostName (string) --The outbound host name for the Amazon Chime Voice Connector.

RequireEncryption (boolean) --Designates whether encryption is required for the Amazon Chime Voice Connector.

CreatedTimestamp (datetime) --The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.








Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'VoiceConnector': {
            'VoiceConnectorId': 'string',
            'AwsRegion': 'us-east-1'|'us-west-2',
            'Name': 'string',
            'OutboundHostName': 'string',
            'RequireEncryption': True|False,
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_voice_connector_group(VoiceConnectorGroupId=None):
    """
    Retrieves details for the specified Amazon Chime Voice Connector group, such as timestamps, name, and associated VoiceConnectorItems .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_voice_connector_group(
        VoiceConnectorGroupId='string'
    )
    
    
    :type VoiceConnectorGroupId: string
    :param VoiceConnectorGroupId: [REQUIRED]\nThe Amazon Chime Voice Connector group ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'VoiceConnectorGroup': {
        'VoiceConnectorGroupId': 'string',
        'Name': 'string',
        'VoiceConnectorItems': [
            {
                'VoiceConnectorId': 'string',
                'Priority': 123
            },
        ],
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
VoiceConnectorGroup (dict) --The Amazon Chime Voice Connector group details.

VoiceConnectorGroupId (string) --The Amazon Chime Voice Connector group ID.

Name (string) --The name of the Amazon Chime Voice Connector group.

VoiceConnectorItems (list) --The Amazon Chime Voice Connectors to which to route inbound calls.

(dict) --For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to route inbound calls. Includes priority configuration settings. Limit: 3 VoiceConnectorItems per Amazon Chime Voice Connector group.

VoiceConnectorId (string) --The Amazon Chime Voice Connector ID.

Priority (integer) --The priority associated with the Amazon Chime Voice Connector, with 1 being the highest priority. Higher priority Amazon Chime Voice Connectors are attempted first.





CreatedTimestamp (datetime) --The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.








Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'VoiceConnectorGroup': {
            'VoiceConnectorGroupId': 'string',
            'Name': 'string',
            'VoiceConnectorItems': [
                {
                    'VoiceConnectorId': 'string',
                    'Priority': 123
                },
            ],
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_voice_connector_logging_configuration(VoiceConnectorId=None):
    """
    Retrieves the logging configuration details for the specified Amazon Chime Voice Connector. Shows whether SIP message logs are enabled for sending to Amazon CloudWatch Logs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_voice_connector_logging_configuration(
        VoiceConnectorId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'LoggingConfiguration': {
        'EnableSIPLogs': True|False
    }
}


Response Structure

(dict) --
LoggingConfiguration (dict) --The logging configuration details.

EnableSIPLogs (boolean) --When true, enables SIP message logs for sending to Amazon CloudWatch Logs.








Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'LoggingConfiguration': {
            'EnableSIPLogs': True|False
        }
    }
    
    
    """
    pass

def get_voice_connector_origination(VoiceConnectorId=None):
    """
    Retrieves origination setting details for the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_voice_connector_origination(
        VoiceConnectorId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Origination': {
        'Routes': [
            {
                'Host': 'string',
                'Port': 123,
                'Protocol': 'TCP'|'UDP',
                'Priority': 123,
                'Weight': 123
            },
        ],
        'Disabled': True|False
    }
}


Response Structure

(dict) --
Origination (dict) --The origination setting details.

Routes (list) --The call distribution properties defined for your SIP hosts. Valid range: Minimum value of 1. Maximum value of 20.

(dict) --Origination routes define call distribution properties for your SIP hosts to receive inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for each Amazon Chime Voice Connector.

Host (string) --The FQDN or IP address to contact for origination traffic.

Port (integer) --The designated origination route port. Defaults to 5060.

Protocol (string) --The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice Connectors use TCP protocol by default.

Priority (integer) --The priority associated with the host, with 1 being the highest priority. Higher priority hosts are attempted first.

Weight (integer) --The weight associated with the host. If hosts are equal in priority, calls are distributed among them based on their relative weight.





Disabled (boolean) --When origination settings are disabled, inbound calls are not enabled for your Amazon Chime Voice Connector.








Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Origination': {
            'Routes': [
                {
                    'Host': 'string',
                    'Port': 123,
                    'Protocol': 'TCP'|'UDP',
                    'Priority': 123,
                    'Weight': 123
                },
            ],
            'Disabled': True|False
        }
    }
    
    
    """
    pass

def get_voice_connector_proxy(VoiceConnectorId=None):
    """
    Gets the proxy configuration details for the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_voice_connector_proxy(
        VoiceConnectorId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime voice connector ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Proxy': {
        'DefaultSessionExpiryMinutes': 123,
        'Disabled': True|False,
        'FallBackPhoneNumber': 'string',
        'PhoneNumberCountries': [
            'string',
        ]
    }
}


Response Structure

(dict) --
Proxy (dict) --The proxy configuration details.

DefaultSessionExpiryMinutes (integer) --The default number of minutes allowed for proxy sessions.

Disabled (boolean) --When true, stops proxy sessions from being created on the specified Amazon Chime Voice Connector.

FallBackPhoneNumber (string) --The phone number to route calls to after a proxy session expires.

PhoneNumberCountries (list) --The countries for proxy phone numbers to be selected from.

(string) --









Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Proxy': {
            'DefaultSessionExpiryMinutes': 123,
            'Disabled': True|False,
            'FallBackPhoneNumber': 'string',
            'PhoneNumberCountries': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def get_voice_connector_streaming_configuration(VoiceConnectorId=None):
    """
    Retrieves the streaming configuration details for the specified Amazon Chime Voice Connector. Shows whether media streaming is enabled for sending to Amazon Kinesis. It also shows the retention period, in hours, for the Amazon Kinesis data.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_voice_connector_streaming_configuration(
        VoiceConnectorId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'StreamingConfiguration': {
        'DataRetentionInHours': 123,
        'Disabled': True|False,
        'StreamingNotificationTargets': [
            {
                'NotificationTarget': 'EventBridge'|'SNS'|'SQS'
            },
        ]
    }
}


Response Structure

(dict) --
StreamingConfiguration (dict) --The streaming configuration details.

DataRetentionInHours (integer) --The retention period, in hours, for the Amazon Kinesis data.

Disabled (boolean) --When true, media streaming to Amazon Kinesis is turned off.

StreamingNotificationTargets (list) --The streaming notification targets.

(dict) --The targeted recipient for a streaming configuration notification.

NotificationTarget (string) --The streaming notification target.












Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'StreamingConfiguration': {
            'DataRetentionInHours': 123,
            'Disabled': True|False,
            'StreamingNotificationTargets': [
                {
                    'NotificationTarget': 'EventBridge'|'SNS'|'SQS'
                },
            ]
        }
    }
    
    
    """
    pass

def get_voice_connector_termination(VoiceConnectorId=None):
    """
    Retrieves termination setting details for the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_voice_connector_termination(
        VoiceConnectorId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Termination': {
        'CpsLimit': 123,
        'DefaultPhoneNumber': 'string',
        'CallingRegions': [
            'string',
        ],
        'CidrAllowedList': [
            'string',
        ],
        'Disabled': True|False
    }
}


Response Structure

(dict) --
Termination (dict) --The termination setting details.

CpsLimit (integer) --The limit on calls per second. Max value based on account service quota. Default value of 1.

DefaultPhoneNumber (string) --The default caller ID phone number.

CallingRegions (list) --The countries to which calls are allowed, in ISO 3166-1 alpha-2 format. Required.

(string) --


CidrAllowedList (list) --The IP addresses allowed to make calls, in CIDR format. Required.

(string) --


Disabled (boolean) --When termination settings are disabled, outbound calls can not be made.








Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Termination': {
            'CpsLimit': 123,
            'DefaultPhoneNumber': 'string',
            'CallingRegions': [
                'string',
            ],
            'CidrAllowedList': [
                'string',
            ],
            'Disabled': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_voice_connector_termination_health(VoiceConnectorId=None):
    """
    Retrieves information about the last time a SIP OPTIONS ping was received from your SIP infrastructure for the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_voice_connector_termination_health(
        VoiceConnectorId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TerminationHealth': {
        'Timestamp': datetime(2015, 1, 1),
        'Source': 'string'
    }
}


Response Structure

(dict) --
TerminationHealth (dict) --The termination health details.

Timestamp (datetime) --The timestamp, in ISO 8601 format.

Source (string) --The source IP address.








Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'TerminationHealth': {
            'Timestamp': datetime(2015, 1, 1),
            'Source': 'string'
        }
    }
    
    
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

def invite_users(AccountId=None, UserEmailList=None, UserType=None):
    """
    Sends email to a maximum of 50 users, inviting them to the specified Amazon Chime Team account. Only Team account types are currently supported for this action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.invite_users(
        AccountId='string',
        UserEmailList=[
            'string',
        ],
        UserType='PrivateUser'|'SharedDevice'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type UserEmailList: list
    :param UserEmailList: [REQUIRED]\nThe user email addresses to which to send the email invitation.\n\n(string) --\n\n

    :type UserType: string
    :param UserType: The user type.

    :rtype: dict

ReturnsResponse Syntax
{
    'Invites': [
        {
            'InviteId': 'string',
            'Status': 'Pending'|'Accepted'|'Failed',
            'EmailAddress': 'string',
            'EmailStatus': 'NotSent'|'Sent'|'Failed'
        },
    ]
}


Response Structure

(dict) --

Invites (list) --
The email invitation details.

(dict) --
Invitation object returned after emailing users to invite them to join the Amazon Chime Team account.

InviteId (string) --
The invite ID.

Status (string) --
The status of the invite.

EmailAddress (string) --
The email address to which the invite is sent.

EmailStatus (string) --
The status of the invite email.











Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Invites': [
            {
                'InviteId': 'string',
                'Status': 'Pending'|'Accepted'|'Failed',
                'EmailAddress': 'string',
                'EmailStatus': 'NotSent'|'Sent'|'Failed'
            },
        ]
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_accounts(Name=None, UserEmail=None, NextToken=None, MaxResults=None):
    """
    Lists the Amazon Chime accounts under the administrator\'s AWS account. You can filter accounts by account name prefix. To find out which Amazon Chime account a user belongs to, you can filter by the user\'s email address, which returns one account result.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_accounts(
        Name='string',
        UserEmail='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Name: string
    :param Name: Amazon Chime account name prefix with which to filter results.

    :type UserEmail: string
    :param UserEmail: User email address with which to filter results.

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. Defaults to 100.

    :rtype: dict

ReturnsResponse Syntax
{
    'Accounts': [
        {
            'AwsAccountId': 'string',
            'AccountId': 'string',
            'Name': 'string',
            'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'SupportedLicenses': [
                'Basic'|'Plus'|'Pro'|'ProTrial',
            ],
            'SigninDelegateGroups': [
                {
                    'GroupName': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Accounts (list) --
List of Amazon Chime accounts and account details.

(dict) --
The Amazon Chime account details. An AWS account can have multiple Amazon Chime accounts.

AwsAccountId (string) --
The AWS account ID.

AccountId (string) --
The Amazon Chime account ID.

Name (string) --
The Amazon Chime account name.

AccountType (string) --
The Amazon Chime account type. For more information about different account types, see Managing Your Amazon Chime Accounts in the Amazon Chime Administration Guide .

CreatedTimestamp (datetime) --
The Amazon Chime account creation timestamp, in ISO 8601 format.

DefaultLicense (string) --
The default license for the Amazon Chime account.

SupportedLicenses (list) --
Supported licenses for the Amazon Chime account.

(string) --


SigninDelegateGroups (list) --
The sign-in delegate groups associated with the account.

(dict) --
An Active Directory (AD) group whose members are granted permission to act as delegates.

GroupName (string) --
The group name.









NextToken (string) --
The token to use to retrieve the next page of results.







Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Accounts': [
            {
                'AwsAccountId': 'string',
                'AccountId': 'string',
                'Name': 'string',
                'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
                'SupportedLicenses': [
                    'Basic'|'Plus'|'Pro'|'ProTrial',
                ],
                'SigninDelegateGroups': [
                    {
                        'GroupName': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_attendee_tags(MeetingId=None, AttendeeId=None):
    """
    Lists the tags applied to an Amazon Chime SDK attendee resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_attendee_tags(
        MeetingId='string',
        AttendeeId='string'
    )
    
    
    :type MeetingId: string
    :param MeetingId: [REQUIRED]\nThe Amazon Chime SDK meeting ID.\n

    :type AttendeeId: string
    :param AttendeeId: [REQUIRED]\nThe Amazon Chime SDK attendee ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --

Tags (list) --
A list of tag key-value pairs.

(dict) --
Describes a tag applied to a resource.

Key (string) --
The key of the tag.

Value (string) --
The value of the tag.











Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_attendees(MeetingId=None, NextToken=None, MaxResults=None):
    """
    Lists the attendees for the specified Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see Using the Amazon Chime SDK in the Amazon Chime Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_attendees(
        MeetingId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type MeetingId: string
    :param MeetingId: [REQUIRED]\nThe Amazon Chime SDK meeting ID.\n

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict

ReturnsResponse Syntax
{
    'Attendees': [
        {
            'ExternalUserId': 'string',
            'AttendeeId': 'string',
            'JoinToken': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Attendees (list) --
The Amazon Chime SDK attendee information.

(dict) --
An Amazon Chime SDK meeting attendee. Includes a unique AttendeeId and JoinToken . The JoinToken allows a client to authenticate and join as the specified attendee. The JoinToken expires when the meeting ends or when  DeleteAttendee is called. After that, the attendee is unable to join the meeting.
We recommend securely transferring each JoinToken from your server application to the client so that no other client has access to the token except for the one authorized to represent the attendee.

ExternalUserId (string) --
The Amazon Chime SDK external user ID. Links the attendee to an identity managed by a builder application.

AttendeeId (string) --
The Amazon Chime SDK attendee ID.

JoinToken (string) --
The join token used by the Amazon Chime SDK attendee.





NextToken (string) --
The token to use to retrieve the next page of results.







Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Attendees': [
            {
                'ExternalUserId': 'string',
                'AttendeeId': 'string',
                'JoinToken': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_bots(AccountId=None, MaxResults=None, NextToken=None):
    """
    Lists the bots associated with the administrator\'s Amazon Chime Enterprise account ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_bots(
        AccountId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. The default is 10.

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Bots': [
        {
            'BotId': 'string',
            'UserId': 'string',
            'DisplayName': 'string',
            'BotType': 'ChatBot',
            'Disabled': True|False,
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1),
            'BotEmail': 'string',
            'SecurityToken': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Bots (list) --
List of bots and bot details.

(dict) --
A resource that allows Enterprise account administrators to configure an interface to receive events from Amazon Chime.

BotId (string) --
The bot ID.

UserId (string) --
The unique ID for the bot user.

DisplayName (string) --
The bot display name.

BotType (string) --
The bot type.

Disabled (boolean) --
When true, the bot is stopped from running in your account.

CreatedTimestamp (datetime) --
The bot creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated bot timestamp, in ISO 8601 format.

BotEmail (string) --
The bot email address.

SecurityToken (string) --
The security token used to authenticate Amazon Chime with the outgoing event endpoint.





NextToken (string) --
The token to use to retrieve the next page of results.







Exceptions

Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ThrottledClientException


    :return: {
        'Bots': [
            {
                'BotId': 'string',
                'UserId': 'string',
                'DisplayName': 'string',
                'BotType': 'ChatBot',
                'Disabled': True|False,
                'CreatedTimestamp': datetime(2015, 1, 1),
                'UpdatedTimestamp': datetime(2015, 1, 1),
                'BotEmail': 'string',
                'SecurityToken': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ThrottledClientException
    
    """
    pass

def list_meeting_tags(MeetingId=None):
    """
    Lists the tags applied to an Amazon Chime SDK meeting resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_meeting_tags(
        MeetingId='string'
    )
    
    
    :type MeetingId: string
    :param MeetingId: [REQUIRED]\nThe Amazon Chime SDK meeting ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Tags (list) --A list of tag key-value pairs.

(dict) --Describes a tag applied to a resource.

Key (string) --The key of the tag.

Value (string) --The value of the tag.










Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_meetings(NextToken=None, MaxResults=None):
    """
    Lists up to 100 active Amazon Chime SDK meetings. For more information about the Amazon Chime SDK, see Using the Amazon Chime SDK in the Amazon Chime Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_meetings(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict

ReturnsResponse Syntax
{
    'Meetings': [
        {
            'MeetingId': 'string',
            'ExternalMeetingId': 'string',
            'MediaPlacement': {
                'AudioHostUrl': 'string',
                'AudioFallbackUrl': 'string',
                'ScreenDataUrl': 'string',
                'ScreenSharingUrl': 'string',
                'ScreenViewingUrl': 'string',
                'SignalingUrl': 'string',
                'TurnControlUrl': 'string'
            },
            'MediaRegion': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Meetings (list) --
The Amazon Chime SDK meeting information.

(dict) --
A meeting created using the Amazon Chime SDK.

MeetingId (string) --
The Amazon Chime SDK meeting ID.

ExternalMeetingId (string) --
The external meeting ID.

MediaPlacement (dict) --
The media placement for the meeting.

AudioHostUrl (string) --
The audio host URL.

AudioFallbackUrl (string) --
The audio fallback URL.

ScreenDataUrl (string) --
The screen data URL.

ScreenSharingUrl (string) --
The screen sharing URL.

ScreenViewingUrl (string) --
The screen viewing URL.

SignalingUrl (string) --
The signaling URL.

TurnControlUrl (string) --
The turn control URL.



MediaRegion (string) --
The Region in which to create the meeting. Available values: ap-northeast-1 , ap-southeast-1 , ap-southeast-2 , ca-central-1 , eu-central-1 , eu-north-1 , eu-west-1 , eu-west-2 , eu-west-3 , sa-east-1 , us-east-1 , us-east-2 , us-west-1 , us-west-2 .





NextToken (string) --
The token to use to retrieve the next page of results.







Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Meetings': [
            {
                'MeetingId': 'string',
                'ExternalMeetingId': 'string',
                'MediaPlacement': {
                    'AudioHostUrl': 'string',
                    'AudioFallbackUrl': 'string',
                    'ScreenDataUrl': 'string',
                    'ScreenSharingUrl': 'string',
                    'ScreenViewingUrl': 'string',
                    'SignalingUrl': 'string',
                    'TurnControlUrl': 'string'
                },
                'MediaRegion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_phone_number_orders(NextToken=None, MaxResults=None):
    """
    Lists the phone number orders for the administrator\'s Amazon Chime account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_phone_number_orders(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict

ReturnsResponse Syntax
{
    'PhoneNumberOrders': [
        {
            'PhoneNumberOrderId': 'string',
            'ProductType': 'BusinessCalling'|'VoiceConnector',
            'Status': 'Processing'|'Successful'|'Failed'|'Partial',
            'OrderedPhoneNumbers': [
                {
                    'E164PhoneNumber': 'string',
                    'Status': 'Processing'|'Acquired'|'Failed'
                },
            ],
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

PhoneNumberOrders (list) --
The phone number order details.

(dict) --
The details of a phone number order created for Amazon Chime.

PhoneNumberOrderId (string) --
The phone number order ID.

ProductType (string) --
The phone number order product type.

Status (string) --
The status of the phone number order.

OrderedPhoneNumbers (list) --
The ordered phone number details, such as the phone number in E.164 format and the phone number status.

(dict) --
A phone number for which an order has been placed.

E164PhoneNumber (string) --
The phone number, in E.164 format.

Status (string) --
The phone number status.





CreatedTimestamp (datetime) --
The phone number order creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated phone number order timestamp, in ISO 8601 format.





NextToken (string) --
The token to use to retrieve the next page of results.







Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'PhoneNumberOrders': [
            {
                'PhoneNumberOrderId': 'string',
                'ProductType': 'BusinessCalling'|'VoiceConnector',
                'Status': 'Processing'|'Successful'|'Failed'|'Partial',
                'OrderedPhoneNumbers': [
                    {
                        'E164PhoneNumber': 'string',
                        'Status': 'Processing'|'Acquired'|'Failed'
                    },
                ],
                'CreatedTimestamp': datetime(2015, 1, 1),
                'UpdatedTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_phone_numbers(Status=None, ProductType=None, FilterName=None, FilterValue=None, MaxResults=None, NextToken=None):
    """
    Lists the phone numbers for the specified Amazon Chime account, Amazon Chime user, Amazon Chime Voice Connector, or Amazon Chime Voice Connector group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_phone_numbers(
        Status='AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'|'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
        ProductType='BusinessCalling'|'VoiceConnector',
        FilterName='AccountId'|'UserId'|'VoiceConnectorId'|'VoiceConnectorGroupId',
        FilterValue='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Status: string
    :param Status: The phone number status.

    :type ProductType: string
    :param ProductType: The phone number product type.

    :type FilterName: string
    :param FilterName: The filter to use to limit the number of results.

    :type FilterValue: string
    :param FilterValue: The value to use for the filter.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'PhoneNumbers': [
        {
            'PhoneNumberId': 'string',
            'E164PhoneNumber': 'string',
            'Type': 'Local'|'TollFree',
            'ProductType': 'BusinessCalling'|'VoiceConnector',
            'Status': 'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'|'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
            'Capabilities': {
                'InboundCall': True|False,
                'OutboundCall': True|False,
                'InboundSMS': True|False,
                'OutboundSMS': True|False,
                'InboundMMS': True|False,
                'OutboundMMS': True|False
            },
            'Associations': [
                {
                    'Value': 'string',
                    'Name': 'AccountId'|'UserId'|'VoiceConnectorId'|'VoiceConnectorGroupId',
                    'AssociatedTimestamp': datetime(2015, 1, 1)
                },
            ],
            'CallingName': 'string',
            'CallingNameStatus': 'Unassigned'|'UpdateInProgress'|'UpdateSucceeded'|'UpdateFailed',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1),
            'DeletionTimestamp': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

PhoneNumbers (list) --
The phone number details.

(dict) --
A phone number used for Amazon Chime Business Calling or an Amazon Chime Voice Connector.

PhoneNumberId (string) --
The phone number ID.

E164PhoneNumber (string) --
The phone number, in E.164 format.

Type (string) --
The phone number type.

ProductType (string) --
The phone number product type.

Status (string) --
The phone number status.

Capabilities (dict) --
The phone number capabilities.

InboundCall (boolean) --
Allows or denies inbound calling for the specified phone number.

OutboundCall (boolean) --
Allows or denies outbound calling for the specified phone number.

InboundSMS (boolean) --
Allows or denies inbound SMS messaging for the specified phone number.

OutboundSMS (boolean) --
Allows or denies outbound SMS messaging for the specified phone number.

InboundMMS (boolean) --
Allows or denies inbound MMS messaging for the specified phone number.

OutboundMMS (boolean) --
Allows or denies outbound MMS messaging for the specified phone number.



Associations (list) --
The phone number associations.

(dict) --
The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID, Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

Value (string) --
Contains the ID for the entity specified in Name.

Name (string) --
Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

AssociatedTimestamp (datetime) --
The timestamp of the phone number association, in ISO 8601 format.





CallingName (string) --
The outbound calling name associated with the phone number.

CallingNameStatus (string) --
The outbound calling name status.

CreatedTimestamp (datetime) --
The phone number creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated phone number timestamp, in ISO 8601 format.

DeletionTimestamp (datetime) --
The deleted phone number timestamp, in ISO 8601 format.





NextToken (string) --
The token to use to retrieve the next page of results.







Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'PhoneNumbers': [
            {
                'PhoneNumberId': 'string',
                'E164PhoneNumber': 'string',
                'Type': 'Local'|'TollFree',
                'ProductType': 'BusinessCalling'|'VoiceConnector',
                'Status': 'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'|'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
                'Capabilities': {
                    'InboundCall': True|False,
                    'OutboundCall': True|False,
                    'InboundSMS': True|False,
                    'OutboundSMS': True|False,
                    'InboundMMS': True|False,
                    'OutboundMMS': True|False
                },
                'Associations': [
                    {
                        'Value': 'string',
                        'Name': 'AccountId'|'UserId'|'VoiceConnectorId'|'VoiceConnectorGroupId',
                        'AssociatedTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'CallingName': 'string',
                'CallingNameStatus': 'Unassigned'|'UpdateInProgress'|'UpdateSucceeded'|'UpdateFailed',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'UpdatedTimestamp': datetime(2015, 1, 1),
                'DeletionTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_proxy_sessions(VoiceConnectorId=None, Status=None, NextToken=None, MaxResults=None):
    """
    Lists the proxy sessions for the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_proxy_sessions(
        VoiceConnectorId='string',
        Status='Open'|'InProgress'|'Closed',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime voice connector ID.\n

    :type Status: string
    :param Status: The proxy session status.

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict

ReturnsResponse Syntax
{
    'ProxySessions': [
        {
            'VoiceConnectorId': 'string',
            'ProxySessionId': 'string',
            'Name': 'string',
            'Status': 'Open'|'InProgress'|'Closed',
            'ExpiryMinutes': 123,
            'Capabilities': [
                'Voice'|'SMS',
            ],
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1),
            'EndedTimestamp': datetime(2015, 1, 1),
            'Participants': [
                {
                    'PhoneNumber': 'string',
                    'ProxyPhoneNumber': 'string'
                },
            ],
            'NumberSelectionBehavior': 'PreferSticky'|'AvoidSticky',
            'GeoMatchLevel': 'Country'|'AreaCode',
            'GeoMatchParams': {
                'Country': 'string',
                'AreaCode': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ProxySessions (list) --
The proxy session details.

(dict) --
The proxy session for an Amazon Chime Voice Connector.

VoiceConnectorId (string) --
The Amazon Chime voice connector ID.

ProxySessionId (string) --
The proxy session ID.

Name (string) --
The name of the proxy session.

Status (string) --
The status of the proxy session.

ExpiryMinutes (integer) --
The number of minutes allowed for the proxy session.

Capabilities (list) --
The proxy session capabilities.

(string) --


CreatedTimestamp (datetime) --
The created timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated timestamp, in ISO 8601 format.

EndedTimestamp (datetime) --
The ended timestamp, in ISO 8601 format.

Participants (list) --
The proxy session participants.

(dict) --
The phone number and proxy phone number for a participant in an Amazon Chime Voice Connector proxy session.

PhoneNumber (string) --
The participant\'s phone number.

ProxyPhoneNumber (string) --
The participant\'s proxy phone number.





NumberSelectionBehavior (string) --
The preference for proxy phone number reuse, or stickiness, between the same participants across sessions.

GeoMatchLevel (string) --
The preference for matching the country or area code of the proxy phone number with that of the first participant.

GeoMatchParams (dict) --
The country and area code for the proxy phone number.

Country (string) --
The country.

AreaCode (string) --
The area code.







NextToken (string) --
The token to use to retrieve the next page of results.







Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'ProxySessions': [
            {
                'VoiceConnectorId': 'string',
                'ProxySessionId': 'string',
                'Name': 'string',
                'Status': 'Open'|'InProgress'|'Closed',
                'ExpiryMinutes': 123,
                'Capabilities': [
                    'Voice'|'SMS',
                ],
                'CreatedTimestamp': datetime(2015, 1, 1),
                'UpdatedTimestamp': datetime(2015, 1, 1),
                'EndedTimestamp': datetime(2015, 1, 1),
                'Participants': [
                    {
                        'PhoneNumber': 'string',
                        'ProxyPhoneNumber': 'string'
                    },
                ],
                'NumberSelectionBehavior': 'PreferSticky'|'AvoidSticky',
                'GeoMatchLevel': 'Country'|'AreaCode',
                'GeoMatchParams': {
                    'Country': 'string',
                    'AreaCode': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_room_memberships(AccountId=None, RoomId=None, MaxResults=None, NextToken=None):
    """
    Lists the membership details for the specified room in an Amazon Chime Enterprise account, such as the members\' IDs, email addresses, and names.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_room_memberships(
        AccountId='string',
        RoomId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type RoomId: string
    :param RoomId: [REQUIRED]\nThe room ID.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'RoomMemberships': [
        {
            'RoomId': 'string',
            'Member': {
                'MemberId': 'string',
                'MemberType': 'User'|'Bot'|'Webhook',
                'Email': 'string',
                'FullName': 'string',
                'AccountId': 'string'
            },
            'Role': 'Administrator'|'Member',
            'InvitedBy': 'string',
            'UpdatedTimestamp': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

RoomMemberships (list) --
The room membership details.

(dict) --
The room membership details.

RoomId (string) --
The room ID.

Member (dict) --
The member details, such as email address, name, member ID, and member type.

MemberId (string) --
The member ID (user ID or bot ID).

MemberType (string) --
The member type.

Email (string) --
The member email address.

FullName (string) --
The member name.

AccountId (string) --
The Amazon Chime account ID.



Role (string) --
The membership role.

InvitedBy (string) --
The identifier of the user that invited the room member.

UpdatedTimestamp (datetime) --
The room membership update timestamp, in ISO 8601 format.





NextToken (string) --
The token to use to retrieve the next page of results.







Exceptions

Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'RoomMemberships': [
            {
                'RoomId': 'string',
                'Member': {
                    'MemberId': 'string',
                    'MemberType': 'User'|'Bot'|'Webhook',
                    'Email': 'string',
                    'FullName': 'string',
                    'AccountId': 'string'
                },
                'Role': 'Administrator'|'Member',
                'InvitedBy': 'string',
                'UpdatedTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_rooms(AccountId=None, MemberId=None, MaxResults=None, NextToken=None):
    """
    Lists the room details for the specified Amazon Chime Enterprise account. Optionally, filter the results by a member ID (user ID or bot ID) to see a list of rooms that the member belongs to.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_rooms(
        AccountId='string',
        MemberId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type MemberId: string
    :param MemberId: The member ID (user ID or bot ID).

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Rooms': [
        {
            'RoomId': 'string',
            'Name': 'string',
            'AccountId': 'string',
            'CreatedBy': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Rooms (list) --
The room details.

(dict) --
The Amazon Chime chat room details.

RoomId (string) --
The room ID.

Name (string) --
The room name.

AccountId (string) --
The Amazon Chime account ID.

CreatedBy (string) --
The identifier of the room creator.

CreatedTimestamp (datetime) --
The room creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The room update timestamp, in ISO 8601 format.





NextToken (string) --
The token to use to retrieve the next page of results.







Exceptions

Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Rooms': [
            {
                'RoomId': 'string',
                'Name': 'string',
                'AccountId': 'string',
                'CreatedBy': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'UpdatedTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_tags_for_resource(ResourceARN=None):
    """
    Lists the tags applied to an Amazon Chime SDK meeting resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceARN='string'
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe resource ARN.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Tags (list) --A list of tag-key value pairs.

(dict) --Describes a tag applied to a resource.

Key (string) --The key of the tag.

Value (string) --The value of the tag.










Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_users(AccountId=None, UserEmail=None, UserType=None, MaxResults=None, NextToken=None):
    """
    Lists the users that belong to the specified Amazon Chime account. You can specify an email address to list only the user that the email address belongs to.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_users(
        AccountId='string',
        UserEmail='string',
        UserType='PrivateUser'|'SharedDevice',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type UserEmail: string
    :param UserEmail: Optional. The user email address used to filter results. Maximum 1.

    :type UserType: string
    :param UserType: The user type.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. Defaults to 100.

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Users': [
        {
            'UserId': 'string',
            'AccountId': 'string',
            'PrimaryEmail': 'string',
            'PrimaryProvisionedNumber': 'string',
            'DisplayName': 'string',
            'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'UserType': 'PrivateUser'|'SharedDevice',
            'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
            'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
            'RegisteredOn': datetime(2015, 1, 1),
            'InvitedOn': datetime(2015, 1, 1),
            'AlexaForBusinessMetadata': {
                'IsAlexaForBusinessEnabled': True|False,
                'AlexaForBusinessRoomArn': 'string'
            },
            'PersonalPIN': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Users (list) --
List of users and user details.

(dict) --
The user on the Amazon Chime account.

UserId (string) --
The user ID.

AccountId (string) --
The Amazon Chime account ID.

PrimaryEmail (string) --
The primary email address of the user.

PrimaryProvisionedNumber (string) --
The primary phone number associated with the user.

DisplayName (string) --
The display name of the user.

LicenseType (string) --
The license type for the user.

UserType (string) --
The user type.

UserRegistrationStatus (string) --
The user registration status.

UserInvitationStatus (string) --
The user invite status.

RegisteredOn (datetime) --
Date and time when the user is registered, in ISO 8601 format.

InvitedOn (datetime) --
Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

AlexaForBusinessMetadata (dict) --
The Alexa for Business metadata.

IsAlexaForBusinessEnabled (boolean) --
Starts or stops Alexa for Business.

AlexaForBusinessRoomArn (string) --
The ARN of the room resource.



PersonalPIN (string) --
The user\'s personal meeting PIN.





NextToken (string) --
The token to use to retrieve the next page of results.







Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Users': [
            {
                'UserId': 'string',
                'AccountId': 'string',
                'PrimaryEmail': 'string',
                'PrimaryProvisionedNumber': 'string',
                'DisplayName': 'string',
                'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
                'UserType': 'PrivateUser'|'SharedDevice',
                'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
                'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
                'RegisteredOn': datetime(2015, 1, 1),
                'InvitedOn': datetime(2015, 1, 1),
                'AlexaForBusinessMetadata': {
                    'IsAlexaForBusinessEnabled': True|False,
                    'AlexaForBusinessRoomArn': 'string'
                },
                'PersonalPIN': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_voice_connector_groups(NextToken=None, MaxResults=None):
    """
    Lists the Amazon Chime Voice Connector groups for the administrator\'s AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_voice_connector_groups(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict

ReturnsResponse Syntax
{
    'VoiceConnectorGroups': [
        {
            'VoiceConnectorGroupId': 'string',
            'Name': 'string',
            'VoiceConnectorItems': [
                {
                    'VoiceConnectorId': 'string',
                    'Priority': 123
                },
            ],
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

VoiceConnectorGroups (list) --
The details of the Amazon Chime Voice Connector groups.

(dict) --
The Amazon Chime Voice Connector group configuration, including associated Amazon Chime Voice Connectors. You can include Amazon Chime Voice Connectors from different AWS Regions in your group. This creates a fault tolerant mechanism for fallback in case of availability events.

VoiceConnectorGroupId (string) --
The Amazon Chime Voice Connector group ID.

Name (string) --
The name of the Amazon Chime Voice Connector group.

VoiceConnectorItems (list) --
The Amazon Chime Voice Connectors to which to route inbound calls.

(dict) --
For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to route inbound calls. Includes priority configuration settings. Limit: 3 VoiceConnectorItems per Amazon Chime Voice Connector group.

VoiceConnectorId (string) --
The Amazon Chime Voice Connector ID.

Priority (integer) --
The priority associated with the Amazon Chime Voice Connector, with 1 being the highest priority. Higher priority Amazon Chime Voice Connectors are attempted first.





CreatedTimestamp (datetime) --
The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.





NextToken (string) --
The token to use to retrieve the next page of results.







Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'VoiceConnectorGroups': [
            {
                'VoiceConnectorGroupId': 'string',
                'Name': 'string',
                'VoiceConnectorItems': [
                    {
                        'VoiceConnectorId': 'string',
                        'Priority': 123
                    },
                ],
                'CreatedTimestamp': datetime(2015, 1, 1),
                'UpdatedTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_voice_connector_termination_credentials(VoiceConnectorId=None):
    """
    Lists the SIP credentials for the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_voice_connector_termination_credentials(
        VoiceConnectorId='string'
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Usernames': [
        'string',
    ]
}


Response Structure

(dict) --
Usernames (list) --A list of user names.

(string) --







Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Usernames': [
            'string',
        ]
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def list_voice_connectors(NextToken=None, MaxResults=None):
    """
    Lists the Amazon Chime Voice Connectors for the administrator\'s AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_voice_connectors(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict

ReturnsResponse Syntax
{
    'VoiceConnectors': [
        {
            'VoiceConnectorId': 'string',
            'AwsRegion': 'us-east-1'|'us-west-2',
            'Name': 'string',
            'OutboundHostName': 'string',
            'RequireEncryption': True|False,
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

VoiceConnectors (list) --
The details of the Amazon Chime Voice Connectors.

(dict) --
The Amazon Chime Voice Connector configuration, including outbound host name and encryption settings.

VoiceConnectorId (string) --
The Amazon Chime Voice Connector ID.

AwsRegion (string) --
The AWS Region in which the Amazon Chime Voice Connector is created. Default: us-east-1 .

Name (string) --
The name of the Amazon Chime Voice Connector.

OutboundHostName (string) --
The outbound host name for the Amazon Chime Voice Connector.

RequireEncryption (boolean) --
Designates whether encryption is required for the Amazon Chime Voice Connector.

CreatedTimestamp (datetime) --
The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.





NextToken (string) --
The token to use to retrieve the next page of results.







Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'VoiceConnectors': [
            {
                'VoiceConnectorId': 'string',
                'AwsRegion': 'us-east-1'|'us-west-2',
                'Name': 'string',
                'OutboundHostName': 'string',
                'RequireEncryption': True|False,
                'CreatedTimestamp': datetime(2015, 1, 1),
                'UpdatedTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def logout_user(AccountId=None, UserId=None):
    """
    Logs out the specified user from all of the devices they are currently logged into.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.logout_user(
        AccountId='string',
        UserId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type UserId: string
    :param UserId: [REQUIRED]\nThe user ID.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_events_configuration(AccountId=None, BotId=None, OutboundEventsHTTPSEndpoint=None, LambdaFunctionArn=None):
    """
    Creates an events configuration that allows a bot to receive outgoing events sent by Amazon Chime. Choose either an HTTPS endpoint or a Lambda function ARN. For more information, see  Bot .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_events_configuration(
        AccountId='string',
        BotId='string',
        OutboundEventsHTTPSEndpoint='string',
        LambdaFunctionArn='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type BotId: string
    :param BotId: [REQUIRED]\nThe bot ID.\n

    :type OutboundEventsHTTPSEndpoint: string
    :param OutboundEventsHTTPSEndpoint: HTTPS endpoint that allows the bot to receive outgoing events.

    :type LambdaFunctionArn: string
    :param LambdaFunctionArn: Lambda function ARN that allows the bot to receive outgoing events.

    :rtype: dict

ReturnsResponse Syntax
{
    'EventsConfiguration': {
        'BotId': 'string',
        'OutboundEventsHTTPSEndpoint': 'string',
        'LambdaFunctionArn': 'string'
    }
}


Response Structure

(dict) --

EventsConfiguration (dict) --
The configuration that allows a bot to receive outgoing events. Can be either an HTTPS endpoint or a Lambda function ARN.

BotId (string) --
The bot ID.

OutboundEventsHTTPSEndpoint (string) --
HTTPS endpoint that allows a bot to receive outgoing events.

LambdaFunctionArn (string) --
Lambda function ARN that allows a bot to receive outgoing events.









Exceptions

Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ResourceLimitExceededException
Chime.Client.exceptions.NotFoundException


    :return: {
        'EventsConfiguration': {
            'BotId': 'string',
            'OutboundEventsHTTPSEndpoint': 'string',
            'LambdaFunctionArn': 'string'
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ResourceLimitExceededException
    Chime.Client.exceptions.NotFoundException
    
    """
    pass

def put_retention_settings(AccountId=None, RetentionSettings=None):
    """
    Puts retention settings for the specified Amazon Chime Enterprise account. We recommend using AWS CloudTrail to monitor usage of this API for your account. For more information, see Logging Amazon Chime API Calls with AWS CloudTrail in the Amazon Chime Administration Guide .
    To turn off existing retention settings, remove the number of days from the corresponding RetentionDays field in the RetentionSettings object. For more information about retention settings, see Managing Chat Retention Policies in the Amazon Chime Administration Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_retention_settings(
        AccountId='string',
        RetentionSettings={
            'RoomRetentionSettings': {
                'RetentionDays': 123
            },
            'ConversationRetentionSettings': {
                'RetentionDays': 123
            }
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type RetentionSettings: dict
    :param RetentionSettings: [REQUIRED]\nThe retention settings.\n\nRoomRetentionSettings (dict) --The chat room retention settings.\n\nRetentionDays (integer) --The number of days for which to retain chat room messages.\n\n\n\nConversationRetentionSettings (dict) --The chat conversation retention settings.\n\nRetentionDays (integer) --The number of days for which to retain chat conversation messages.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RetentionSettings': {
        'RoomRetentionSettings': {
            'RetentionDays': 123
        },
        'ConversationRetentionSettings': {
            'RetentionDays': 123
        }
    },
    'InitiateDeletionTimestamp': datetime(2015, 1, 1)
}


Response Structure

(dict) --

RetentionSettings (dict) --
The retention settings.

RoomRetentionSettings (dict) --
The chat room retention settings.

RetentionDays (integer) --
The number of days for which to retain chat room messages.



ConversationRetentionSettings (dict) --
The chat conversation retention settings.

RetentionDays (integer) --
The number of days for which to retain chat conversation messages.





InitiateDeletionTimestamp (datetime) --
The timestamp representing the time at which the specified items are permanently deleted, in ISO 8601 format.







Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.ConflictException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'RetentionSettings': {
            'RoomRetentionSettings': {
                'RetentionDays': 123
            },
            'ConversationRetentionSettings': {
                'RetentionDays': 123
            }
        },
        'InitiateDeletionTimestamp': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.ConflictException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def put_voice_connector_logging_configuration(VoiceConnectorId=None, LoggingConfiguration=None):
    """
    Adds a logging configuration for the specified Amazon Chime Voice Connector. The logging configuration specifies whether SIP message logs are enabled for sending to Amazon CloudWatch Logs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_voice_connector_logging_configuration(
        VoiceConnectorId='string',
        LoggingConfiguration={
            'EnableSIPLogs': True|False
        }
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :type LoggingConfiguration: dict
    :param LoggingConfiguration: [REQUIRED]\nThe logging configuration details to add.\n\nEnableSIPLogs (boolean) --When true, enables SIP message logs for sending to Amazon CloudWatch Logs.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LoggingConfiguration': {
        'EnableSIPLogs': True|False
    }
}


Response Structure

(dict) --

LoggingConfiguration (dict) --
The updated logging configuration details.

EnableSIPLogs (boolean) --
When true, enables SIP message logs for sending to Amazon CloudWatch Logs.









Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'LoggingConfiguration': {
            'EnableSIPLogs': True|False
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def put_voice_connector_origination(VoiceConnectorId=None, Origination=None):
    """
    Adds origination settings for the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_voice_connector_origination(
        VoiceConnectorId='string',
        Origination={
            'Routes': [
                {
                    'Host': 'string',
                    'Port': 123,
                    'Protocol': 'TCP'|'UDP',
                    'Priority': 123,
                    'Weight': 123
                },
            ],
            'Disabled': True|False
        }
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :type Origination: dict
    :param Origination: [REQUIRED]\nThe origination setting details to add.\n\nRoutes (list) --The call distribution properties defined for your SIP hosts. Valid range: Minimum value of 1. Maximum value of 20.\n\n(dict) --Origination routes define call distribution properties for your SIP hosts to receive inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for each Amazon Chime Voice Connector.\n\nHost (string) --The FQDN or IP address to contact for origination traffic.\n\nPort (integer) --The designated origination route port. Defaults to 5060.\n\nProtocol (string) --The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice Connectors use TCP protocol by default.\n\nPriority (integer) --The priority associated with the host, with 1 being the highest priority. Higher priority hosts are attempted first.\n\nWeight (integer) --The weight associated with the host. If hosts are equal in priority, calls are distributed among them based on their relative weight.\n\n\n\n\n\nDisabled (boolean) --When origination settings are disabled, inbound calls are not enabled for your Amazon Chime Voice Connector.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Origination': {
        'Routes': [
            {
                'Host': 'string',
                'Port': 123,
                'Protocol': 'TCP'|'UDP',
                'Priority': 123,
                'Weight': 123
            },
        ],
        'Disabled': True|False
    }
}


Response Structure

(dict) --

Origination (dict) --
The updated origination setting details.

Routes (list) --
The call distribution properties defined for your SIP hosts. Valid range: Minimum value of 1. Maximum value of 20.

(dict) --
Origination routes define call distribution properties for your SIP hosts to receive inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for each Amazon Chime Voice Connector.

Host (string) --
The FQDN or IP address to contact for origination traffic.

Port (integer) --
The designated origination route port. Defaults to 5060.

Protocol (string) --
The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice Connectors use TCP protocol by default.

Priority (integer) --
The priority associated with the host, with 1 being the highest priority. Higher priority hosts are attempted first.

Weight (integer) --
The weight associated with the host. If hosts are equal in priority, calls are distributed among them based on their relative weight.





Disabled (boolean) --
When origination settings are disabled, inbound calls are not enabled for your Amazon Chime Voice Connector.









Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Origination': {
            'Routes': [
                {
                    'Host': 'string',
                    'Port': 123,
                    'Protocol': 'TCP'|'UDP',
                    'Priority': 123,
                    'Weight': 123
                },
            ],
            'Disabled': True|False
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def put_voice_connector_proxy(VoiceConnectorId=None, DefaultSessionExpiryMinutes=None, PhoneNumberPoolCountries=None, FallBackPhoneNumber=None, Disabled=None):
    """
    Puts the specified proxy configuration to the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_voice_connector_proxy(
        VoiceConnectorId='string',
        DefaultSessionExpiryMinutes=123,
        PhoneNumberPoolCountries=[
            'string',
        ],
        FallBackPhoneNumber='string',
        Disabled=True|False
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime voice connector ID.\n

    :type DefaultSessionExpiryMinutes: integer
    :param DefaultSessionExpiryMinutes: [REQUIRED]\nThe default number of minutes allowed for proxy sessions.\n

    :type PhoneNumberPoolCountries: list
    :param PhoneNumberPoolCountries: [REQUIRED]\nThe countries for proxy phone numbers to be selected from.\n\n(string) --\n\n

    :type FallBackPhoneNumber: string
    :param FallBackPhoneNumber: The phone number to route calls to after a proxy session expires.

    :type Disabled: boolean
    :param Disabled: When true, stops proxy sessions from being created on the specified Amazon Chime Voice Connector.

    :rtype: dict

ReturnsResponse Syntax
{
    'Proxy': {
        'DefaultSessionExpiryMinutes': 123,
        'Disabled': True|False,
        'FallBackPhoneNumber': 'string',
        'PhoneNumberCountries': [
            'string',
        ]
    }
}


Response Structure

(dict) --

Proxy (dict) --
The proxy configuration details.

DefaultSessionExpiryMinutes (integer) --
The default number of minutes allowed for proxy sessions.

Disabled (boolean) --
When true, stops proxy sessions from being created on the specified Amazon Chime Voice Connector.

FallBackPhoneNumber (string) --
The phone number to route calls to after a proxy session expires.

PhoneNumberCountries (list) --
The countries for proxy phone numbers to be selected from.

(string) --










Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.AccessDeniedException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Proxy': {
            'DefaultSessionExpiryMinutes': 123,
            'Disabled': True|False,
            'FallBackPhoneNumber': 'string',
            'PhoneNumberCountries': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_voice_connector_streaming_configuration(VoiceConnectorId=None, StreamingConfiguration=None):
    """
    Adds a streaming configuration for the specified Amazon Chime Voice Connector. The streaming configuration specifies whether media streaming is enabled for sending to Amazon Kinesis. It also sets the retention period, in hours, for the Amazon Kinesis data.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_voice_connector_streaming_configuration(
        VoiceConnectorId='string',
        StreamingConfiguration={
            'DataRetentionInHours': 123,
            'Disabled': True|False,
            'StreamingNotificationTargets': [
                {
                    'NotificationTarget': 'EventBridge'|'SNS'|'SQS'
                },
            ]
        }
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :type StreamingConfiguration: dict
    :param StreamingConfiguration: [REQUIRED]\nThe streaming configuration details to add.\n\nDataRetentionInHours (integer) -- [REQUIRED]The retention period, in hours, for the Amazon Kinesis data.\n\nDisabled (boolean) --When true, media streaming to Amazon Kinesis is turned off.\n\nStreamingNotificationTargets (list) --The streaming notification targets.\n\n(dict) --The targeted recipient for a streaming configuration notification.\n\nNotificationTarget (string) -- [REQUIRED]The streaming notification target.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamingConfiguration': {
        'DataRetentionInHours': 123,
        'Disabled': True|False,
        'StreamingNotificationTargets': [
            {
                'NotificationTarget': 'EventBridge'|'SNS'|'SQS'
            },
        ]
    }
}


Response Structure

(dict) --

StreamingConfiguration (dict) --
The updated streaming configuration details.

DataRetentionInHours (integer) --
The retention period, in hours, for the Amazon Kinesis data.

Disabled (boolean) --
When true, media streaming to Amazon Kinesis is turned off.

StreamingNotificationTargets (list) --
The streaming notification targets.

(dict) --
The targeted recipient for a streaming configuration notification.

NotificationTarget (string) --
The streaming notification target.













Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'StreamingConfiguration': {
            'DataRetentionInHours': 123,
            'Disabled': True|False,
            'StreamingNotificationTargets': [
                {
                    'NotificationTarget': 'EventBridge'|'SNS'|'SQS'
                },
            ]
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def put_voice_connector_termination(VoiceConnectorId=None, Termination=None):
    """
    Adds termination settings for the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_voice_connector_termination(
        VoiceConnectorId='string',
        Termination={
            'CpsLimit': 123,
            'DefaultPhoneNumber': 'string',
            'CallingRegions': [
                'string',
            ],
            'CidrAllowedList': [
                'string',
            ],
            'Disabled': True|False
        }
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :type Termination: dict
    :param Termination: [REQUIRED]\nThe termination setting details to add.\n\nCpsLimit (integer) --The limit on calls per second. Max value based on account service quota. Default value of 1.\n\nDefaultPhoneNumber (string) --The default caller ID phone number.\n\nCallingRegions (list) --The countries to which calls are allowed, in ISO 3166-1 alpha-2 format. Required.\n\n(string) --\n\n\nCidrAllowedList (list) --The IP addresses allowed to make calls, in CIDR format. Required.\n\n(string) --\n\n\nDisabled (boolean) --When termination settings are disabled, outbound calls can not be made.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Termination': {
        'CpsLimit': 123,
        'DefaultPhoneNumber': 'string',
        'CallingRegions': [
            'string',
        ],
        'CidrAllowedList': [
            'string',
        ],
        'Disabled': True|False
    }
}


Response Structure

(dict) --

Termination (dict) --
The updated termination setting details.

CpsLimit (integer) --
The limit on calls per second. Max value based on account service quota. Default value of 1.

DefaultPhoneNumber (string) --
The default caller ID phone number.

CallingRegions (list) --
The countries to which calls are allowed, in ISO 3166-1 alpha-2 format. Required.

(string) --


CidrAllowedList (list) --
The IP addresses allowed to make calls, in CIDR format. Required.

(string) --


Disabled (boolean) --
When termination settings are disabled, outbound calls can not be made.









Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.AccessDeniedException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Termination': {
            'CpsLimit': 123,
            'DefaultPhoneNumber': 'string',
            'CallingRegions': [
                'string',
            ],
            'CidrAllowedList': [
                'string',
            ],
            'Disabled': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_voice_connector_termination_credentials(VoiceConnectorId=None, Credentials=None):
    """
    Adds termination SIP credentials for the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_voice_connector_termination_credentials(
        VoiceConnectorId='string',
        Credentials=[
            {
                'Username': 'string',
                'Password': 'string'
            },
        ]
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :type Credentials: list
    :param Credentials: The termination SIP credentials.\n\n(dict) --The SIP credentials used to authenticate requests to your Amazon Chime Voice Connector.\n\nUsername (string) --The RFC2617 compliant user name associated with the SIP credentials, in US-ASCII format.\n\nPassword (string) --The RFC2617 compliant password associated with the SIP credentials, in US-ASCII format.\n\n\n\n\n

    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def redact_conversation_message(AccountId=None, ConversationId=None, MessageId=None):
    """
    Redacts the specified message from the specified Amazon Chime conversation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.redact_conversation_message(
        AccountId='string',
        ConversationId='string',
        MessageId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type ConversationId: string
    :param ConversationId: [REQUIRED]\nThe conversation ID.\n

    :type MessageId: string
    :param MessageId: [REQUIRED]\nThe message ID.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def redact_room_message(AccountId=None, RoomId=None, MessageId=None):
    """
    Redacts the specified message from the specified Amazon Chime chat room.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.redact_room_message(
        AccountId='string',
        RoomId='string',
        MessageId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type RoomId: string
    :param RoomId: [REQUIRED]\nThe room ID.\n

    :type MessageId: string
    :param MessageId: [REQUIRED]\nThe message ID.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def regenerate_security_token(AccountId=None, BotId=None):
    """
    Regenerates the security token for a bot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.regenerate_security_token(
        AccountId='string',
        BotId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type BotId: string
    :param BotId: [REQUIRED]\nThe bot ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Bot': {
        'BotId': 'string',
        'UserId': 'string',
        'DisplayName': 'string',
        'BotType': 'ChatBot',
        'Disabled': True|False,
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1),
        'BotEmail': 'string',
        'SecurityToken': 'string'
    }
}


Response Structure

(dict) --

Bot (dict) --
A resource that allows Enterprise account administrators to configure an interface to receive events from Amazon Chime.

BotId (string) --
The bot ID.

UserId (string) --
The unique ID for the bot user.

DisplayName (string) --
The bot display name.

BotType (string) --
The bot type.

Disabled (boolean) --
When true, the bot is stopped from running in your account.

CreatedTimestamp (datetime) --
The bot creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated bot timestamp, in ISO 8601 format.

BotEmail (string) --
The bot email address.

SecurityToken (string) --
The security token used to authenticate Amazon Chime with the outgoing event endpoint.









Exceptions

Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ThrottledClientException


    :return: {
        'Bot': {
            'BotId': 'string',
            'UserId': 'string',
            'DisplayName': 'string',
            'BotType': 'ChatBot',
            'Disabled': True|False,
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1),
            'BotEmail': 'string',
            'SecurityToken': 'string'
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ThrottledClientException
    
    """
    pass

def reset_personal_pin(AccountId=None, UserId=None):
    """
    Resets the personal meeting PIN for the specified user on an Amazon Chime account. Returns the  User object with the updated personal meeting PIN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reset_personal_pin(
        AccountId='string',
        UserId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type UserId: string
    :param UserId: [REQUIRED]\nThe user ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'User': {
        'UserId': 'string',
        'AccountId': 'string',
        'PrimaryEmail': 'string',
        'PrimaryProvisionedNumber': 'string',
        'DisplayName': 'string',
        'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
        'UserType': 'PrivateUser'|'SharedDevice',
        'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
        'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
        'RegisteredOn': datetime(2015, 1, 1),
        'InvitedOn': datetime(2015, 1, 1),
        'AlexaForBusinessMetadata': {
            'IsAlexaForBusinessEnabled': True|False,
            'AlexaForBusinessRoomArn': 'string'
        },
        'PersonalPIN': 'string'
    }
}


Response Structure

(dict) --

User (dict) --
The user details and new personal meeting PIN.

UserId (string) --
The user ID.

AccountId (string) --
The Amazon Chime account ID.

PrimaryEmail (string) --
The primary email address of the user.

PrimaryProvisionedNumber (string) --
The primary phone number associated with the user.

DisplayName (string) --
The display name of the user.

LicenseType (string) --
The license type for the user.

UserType (string) --
The user type.

UserRegistrationStatus (string) --
The user registration status.

UserInvitationStatus (string) --
The user invite status.

RegisteredOn (datetime) --
Date and time when the user is registered, in ISO 8601 format.

InvitedOn (datetime) --
Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

AlexaForBusinessMetadata (dict) --
The Alexa for Business metadata.

IsAlexaForBusinessEnabled (boolean) --
Starts or stops Alexa for Business.

AlexaForBusinessRoomArn (string) --
The ARN of the room resource.



PersonalPIN (string) --
The user\'s personal meeting PIN.









Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'User': {
            'UserId': 'string',
            'AccountId': 'string',
            'PrimaryEmail': 'string',
            'PrimaryProvisionedNumber': 'string',
            'DisplayName': 'string',
            'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'UserType': 'PrivateUser'|'SharedDevice',
            'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
            'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
            'RegisteredOn': datetime(2015, 1, 1),
            'InvitedOn': datetime(2015, 1, 1),
            'AlexaForBusinessMetadata': {
                'IsAlexaForBusinessEnabled': True|False,
                'AlexaForBusinessRoomArn': 'string'
            },
            'PersonalPIN': 'string'
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def restore_phone_number(PhoneNumberId=None):
    """
    Moves a phone number from the Deletion queue back into the phone number Inventory .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.restore_phone_number(
        PhoneNumberId='string'
    )
    
    
    :type PhoneNumberId: string
    :param PhoneNumberId: [REQUIRED]\nThe phone number.\n

    :rtype: dict
ReturnsResponse Syntax{
    'PhoneNumber': {
        'PhoneNumberId': 'string',
        'E164PhoneNumber': 'string',
        'Type': 'Local'|'TollFree',
        'ProductType': 'BusinessCalling'|'VoiceConnector',
        'Status': 'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'|'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
        'Capabilities': {
            'InboundCall': True|False,
            'OutboundCall': True|False,
            'InboundSMS': True|False,
            'OutboundSMS': True|False,
            'InboundMMS': True|False,
            'OutboundMMS': True|False
        },
        'Associations': [
            {
                'Value': 'string',
                'Name': 'AccountId'|'UserId'|'VoiceConnectorId'|'VoiceConnectorGroupId',
                'AssociatedTimestamp': datetime(2015, 1, 1)
            },
        ],
        'CallingName': 'string',
        'CallingNameStatus': 'Unassigned'|'UpdateInProgress'|'UpdateSucceeded'|'UpdateFailed',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1),
        'DeletionTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
PhoneNumber (dict) --The phone number details.

PhoneNumberId (string) --The phone number ID.

E164PhoneNumber (string) --The phone number, in E.164 format.

Type (string) --The phone number type.

ProductType (string) --The phone number product type.

Status (string) --The phone number status.

Capabilities (dict) --The phone number capabilities.

InboundCall (boolean) --Allows or denies inbound calling for the specified phone number.

OutboundCall (boolean) --Allows or denies outbound calling for the specified phone number.

InboundSMS (boolean) --Allows or denies inbound SMS messaging for the specified phone number.

OutboundSMS (boolean) --Allows or denies outbound SMS messaging for the specified phone number.

InboundMMS (boolean) --Allows or denies inbound MMS messaging for the specified phone number.

OutboundMMS (boolean) --Allows or denies outbound MMS messaging for the specified phone number.



Associations (list) --The phone number associations.

(dict) --The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID, Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

Value (string) --Contains the ID for the entity specified in Name.

Name (string) --Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

AssociatedTimestamp (datetime) --The timestamp of the phone number association, in ISO 8601 format.





CallingName (string) --The outbound calling name associated with the phone number.

CallingNameStatus (string) --The outbound calling name status.

CreatedTimestamp (datetime) --The phone number creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --The updated phone number timestamp, in ISO 8601 format.

DeletionTimestamp (datetime) --The deleted phone number timestamp, in ISO 8601 format.








Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ResourceLimitExceededException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'PhoneNumber': {
            'PhoneNumberId': 'string',
            'E164PhoneNumber': 'string',
            'Type': 'Local'|'TollFree',
            'ProductType': 'BusinessCalling'|'VoiceConnector',
            'Status': 'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'|'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
            'Capabilities': {
                'InboundCall': True|False,
                'OutboundCall': True|False,
                'InboundSMS': True|False,
                'OutboundSMS': True|False,
                'InboundMMS': True|False,
                'OutboundMMS': True|False
            },
            'Associations': [
                {
                    'Value': 'string',
                    'Name': 'AccountId'|'UserId'|'VoiceConnectorId'|'VoiceConnectorGroupId',
                    'AssociatedTimestamp': datetime(2015, 1, 1)
                },
            ],
            'CallingName': 'string',
            'CallingNameStatus': 'Unassigned'|'UpdateInProgress'|'UpdateSucceeded'|'UpdateFailed',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1),
            'DeletionTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def search_available_phone_numbers(AreaCode=None, City=None, Country=None, State=None, TollFreePrefix=None, MaxResults=None, NextToken=None):
    """
    Searches phone numbers that can be ordered.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.search_available_phone_numbers(
        AreaCode='string',
        City='string',
        Country='string',
        State='string',
        TollFreePrefix='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AreaCode: string
    :param AreaCode: The area code used to filter results.

    :type City: string
    :param City: The city used to filter results.

    :type Country: string
    :param Country: The country used to filter results.

    :type State: string
    :param State: The state used to filter results.

    :type TollFreePrefix: string
    :param TollFreePrefix: The toll-free prefix that you use to filter results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'E164PhoneNumbers': [
        'string',
    ]
}


Response Structure

(dict) --

E164PhoneNumbers (list) --
List of phone numbers, in E.164 format.

(string) --








Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.AccessDeniedException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'E164PhoneNumbers': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def tag_attendee(MeetingId=None, AttendeeId=None, Tags=None):
    """
    Applies the specified tags to the specified Amazon Chime SDK attendee.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_attendee(
        MeetingId='string',
        AttendeeId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type MeetingId: string
    :param MeetingId: [REQUIRED]\nThe Amazon Chime SDK meeting ID.\n

    :type AttendeeId: string
    :param AttendeeId: [REQUIRED]\nThe Amazon Chime SDK attendee ID.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tag key-value pairs.\n\n(dict) --Describes a tag applied to a resource.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ResourceLimitExceededException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def tag_meeting(MeetingId=None, Tags=None):
    """
    Applies the specified tags to the specified Amazon Chime SDK meeting.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_meeting(
        MeetingId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type MeetingId: string
    :param MeetingId: [REQUIRED]\nThe Amazon Chime SDK meeting ID.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tag key-value pairs.\n\n(dict) --Describes a tag applied to a resource.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ResourceLimitExceededException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def tag_resource(ResourceARN=None, Tags=None):
    """
    Applies the specified tags to the specified Amazon Chime SDK meeting resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceARN='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe resource ARN.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tag key-value pairs.\n\n(dict) --Describes a tag applied to a resource.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def untag_attendee(MeetingId=None, AttendeeId=None, TagKeys=None):
    """
    Untags the specified tags from the specified Amazon Chime SDK attendee.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_attendee(
        MeetingId='string',
        AttendeeId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type MeetingId: string
    :param MeetingId: [REQUIRED]\nThe Amazon Chime SDK meeting ID.\n

    :type AttendeeId: string
    :param AttendeeId: [REQUIRED]\nThe Amazon Chime SDK attendee ID.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag keys.\n\n(string) --\n\n

    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def untag_meeting(MeetingId=None, TagKeys=None):
    """
    Untags the specified tags from the specified Amazon Chime SDK meeting.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_meeting(
        MeetingId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type MeetingId: string
    :param MeetingId: [REQUIRED]\nThe Amazon Chime SDK meeting ID.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag keys.\n\n(string) --\n\n

    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def untag_resource(ResourceARN=None, TagKeys=None):
    """
    Untags the specified tags from the specified Amazon Chime SDK meeting resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe resource ARN.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag keys.\n\n(string) --\n\n

    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_account(AccountId=None, Name=None):
    """
    Updates account details for the specified Amazon Chime account. Currently, only account name updates are supported for this action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_account(
        AccountId='string',
        Name='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type Name: string
    :param Name: The new name for the specified Amazon Chime account.

    :rtype: dict

ReturnsResponse Syntax
{
    'Account': {
        'AwsAccountId': 'string',
        'AccountId': 'string',
        'Name': 'string',
        'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
        'SupportedLicenses': [
            'Basic'|'Plus'|'Pro'|'ProTrial',
        ],
        'SigninDelegateGroups': [
            {
                'GroupName': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

Account (dict) --
The updated Amazon Chime account details.

AwsAccountId (string) --
The AWS account ID.

AccountId (string) --
The Amazon Chime account ID.

Name (string) --
The Amazon Chime account name.

AccountType (string) --
The Amazon Chime account type. For more information about different account types, see Managing Your Amazon Chime Accounts in the Amazon Chime Administration Guide .

CreatedTimestamp (datetime) --
The Amazon Chime account creation timestamp, in ISO 8601 format.

DefaultLicense (string) --
The default license for the Amazon Chime account.

SupportedLicenses (list) --
Supported licenses for the Amazon Chime account.

(string) --


SigninDelegateGroups (list) --
The sign-in delegate groups associated with the account.

(dict) --
An Active Directory (AD) group whose members are granted permission to act as delegates.

GroupName (string) --
The group name.













Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Account': {
            'AwsAccountId': 'string',
            'AccountId': 'string',
            'Name': 'string',
            'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'SupportedLicenses': [
                'Basic'|'Plus'|'Pro'|'ProTrial',
            ],
            'SigninDelegateGroups': [
                {
                    'GroupName': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_account_settings(AccountId=None, AccountSettings=None):
    """
    Updates the settings for the specified Amazon Chime account. You can update settings for remote control of shared screens, or for the dial-out option. For more information about these settings, see Use the Policies Page in the Amazon Chime Administration Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_account_settings(
        AccountId='string',
        AccountSettings={
            'DisableRemoteControl': True|False,
            'EnableDialOut': True|False
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type AccountSettings: dict
    :param AccountSettings: [REQUIRED]\nThe Amazon Chime account settings to update.\n\nDisableRemoteControl (boolean) --Setting that stops or starts remote control of shared screens during meetings.\n\nEnableDialOut (boolean) --Setting that allows meeting participants to choose the Call me at a phone number option. For more information, see Join a Meeting without the Amazon Chime App .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.ConflictException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_bot(AccountId=None, BotId=None, Disabled=None):
    """
    Updates the status of the specified bot, such as starting or stopping the bot from running in your Amazon Chime Enterprise account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_bot(
        AccountId='string',
        BotId='string',
        Disabled=True|False
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type BotId: string
    :param BotId: [REQUIRED]\nThe bot ID.\n

    :type Disabled: boolean
    :param Disabled: When true, stops the specified bot from running in your account.

    :rtype: dict

ReturnsResponse Syntax
{
    'Bot': {
        'BotId': 'string',
        'UserId': 'string',
        'DisplayName': 'string',
        'BotType': 'ChatBot',
        'Disabled': True|False,
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1),
        'BotEmail': 'string',
        'SecurityToken': 'string'
    }
}


Response Structure

(dict) --

Bot (dict) --
The updated bot details.

BotId (string) --
The bot ID.

UserId (string) --
The unique ID for the bot user.

DisplayName (string) --
The bot display name.

BotType (string) --
The bot type.

Disabled (boolean) --
When true, the bot is stopped from running in your account.

CreatedTimestamp (datetime) --
The bot creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated bot timestamp, in ISO 8601 format.

BotEmail (string) --
The bot email address.

SecurityToken (string) --
The security token used to authenticate Amazon Chime with the outgoing event endpoint.









Exceptions

Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ThrottledClientException


    :return: {
        'Bot': {
            'BotId': 'string',
            'UserId': 'string',
            'DisplayName': 'string',
            'BotType': 'ChatBot',
            'Disabled': True|False,
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1),
            'BotEmail': 'string',
            'SecurityToken': 'string'
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ThrottledClientException
    
    """
    pass

def update_global_settings(BusinessCalling=None, VoiceConnector=None):
    """
    Updates global settings for the administrator\'s AWS account, such as Amazon Chime Business Calling and Amazon Chime Voice Connector settings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_global_settings(
        BusinessCalling={
            'CdrBucket': 'string'
        },
        VoiceConnector={
            'CdrBucket': 'string'
        }
    )
    
    
    :type BusinessCalling: dict
    :param BusinessCalling: [REQUIRED]\nThe Amazon Chime Business Calling settings.\n\nCdrBucket (string) --The Amazon S3 bucket designated for call detail record storage.\n\n\n

    :type VoiceConnector: dict
    :param VoiceConnector: [REQUIRED]\nThe Amazon Chime Voice Connector settings.\n\nCdrBucket (string) --The Amazon S3 bucket designated for call detail record storage.\n\n\n

    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_phone_number(PhoneNumberId=None, ProductType=None, CallingName=None):
    """
    Updates phone number details, such as product type or calling name, for the specified phone number ID. You can update one phone number detail at a time. For example, you can update either the product type or the calling name in one action.
    For toll-free numbers, you must use the Amazon Chime Voice Connector product type.
    Updates to outbound calling names can take up to 72 hours to complete. Pending updates to outbound calling names must be complete before you can request another update.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_phone_number(
        PhoneNumberId='string',
        ProductType='BusinessCalling'|'VoiceConnector',
        CallingName='string'
    )
    
    
    :type PhoneNumberId: string
    :param PhoneNumberId: [REQUIRED]\nThe phone number ID.\n

    :type ProductType: string
    :param ProductType: The product type.

    :type CallingName: string
    :param CallingName: The outbound calling name associated with the phone number.

    :rtype: dict

ReturnsResponse Syntax
{
    'PhoneNumber': {
        'PhoneNumberId': 'string',
        'E164PhoneNumber': 'string',
        'Type': 'Local'|'TollFree',
        'ProductType': 'BusinessCalling'|'VoiceConnector',
        'Status': 'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'|'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
        'Capabilities': {
            'InboundCall': True|False,
            'OutboundCall': True|False,
            'InboundSMS': True|False,
            'OutboundSMS': True|False,
            'InboundMMS': True|False,
            'OutboundMMS': True|False
        },
        'Associations': [
            {
                'Value': 'string',
                'Name': 'AccountId'|'UserId'|'VoiceConnectorId'|'VoiceConnectorGroupId',
                'AssociatedTimestamp': datetime(2015, 1, 1)
            },
        ],
        'CallingName': 'string',
        'CallingNameStatus': 'Unassigned'|'UpdateInProgress'|'UpdateSucceeded'|'UpdateFailed',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1),
        'DeletionTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

PhoneNumber (dict) --
The updated phone number details.

PhoneNumberId (string) --
The phone number ID.

E164PhoneNumber (string) --
The phone number, in E.164 format.

Type (string) --
The phone number type.

ProductType (string) --
The phone number product type.

Status (string) --
The phone number status.

Capabilities (dict) --
The phone number capabilities.

InboundCall (boolean) --
Allows or denies inbound calling for the specified phone number.

OutboundCall (boolean) --
Allows or denies outbound calling for the specified phone number.

InboundSMS (boolean) --
Allows or denies inbound SMS messaging for the specified phone number.

OutboundSMS (boolean) --
Allows or denies outbound SMS messaging for the specified phone number.

InboundMMS (boolean) --
Allows or denies inbound MMS messaging for the specified phone number.

OutboundMMS (boolean) --
Allows or denies outbound MMS messaging for the specified phone number.



Associations (list) --
The phone number associations.

(dict) --
The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID, Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

Value (string) --
Contains the ID for the entity specified in Name.

Name (string) --
Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

AssociatedTimestamp (datetime) --
The timestamp of the phone number association, in ISO 8601 format.





CallingName (string) --
The outbound calling name associated with the phone number.

CallingNameStatus (string) --
The outbound calling name status.

CreatedTimestamp (datetime) --
The phone number creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated phone number timestamp, in ISO 8601 format.

DeletionTimestamp (datetime) --
The deleted phone number timestamp, in ISO 8601 format.









Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'PhoneNumber': {
            'PhoneNumberId': 'string',
            'E164PhoneNumber': 'string',
            'Type': 'Local'|'TollFree',
            'ProductType': 'BusinessCalling'|'VoiceConnector',
            'Status': 'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'|'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
            'Capabilities': {
                'InboundCall': True|False,
                'OutboundCall': True|False,
                'InboundSMS': True|False,
                'OutboundSMS': True|False,
                'InboundMMS': True|False,
                'OutboundMMS': True|False
            },
            'Associations': [
                {
                    'Value': 'string',
                    'Name': 'AccountId'|'UserId'|'VoiceConnectorId'|'VoiceConnectorGroupId',
                    'AssociatedTimestamp': datetime(2015, 1, 1)
                },
            ],
            'CallingName': 'string',
            'CallingNameStatus': 'Unassigned'|'UpdateInProgress'|'UpdateSucceeded'|'UpdateFailed',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1),
            'DeletionTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_phone_number_settings(CallingName=None):
    """
    Updates the phone number settings for the administrator\'s AWS account, such as the default outbound calling name. You can update the default outbound calling name once every seven days. Outbound calling names can take up to 72 hours to update.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_phone_number_settings(
        CallingName='string'
    )
    
    
    :type CallingName: string
    :param CallingName: [REQUIRED]\nThe default outbound calling name for the account.\n

    """
    pass

def update_proxy_session(VoiceConnectorId=None, ProxySessionId=None, Capabilities=None, ExpiryMinutes=None):
    """
    Updates the specified proxy session details, such as voice or SMS capabilities.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_proxy_session(
        VoiceConnectorId='string',
        ProxySessionId='string',
        Capabilities=[
            'Voice'|'SMS',
        ],
        ExpiryMinutes=123
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime voice connector ID.\n

    :type ProxySessionId: string
    :param ProxySessionId: [REQUIRED]\nThe proxy session ID.\n

    :type Capabilities: list
    :param Capabilities: [REQUIRED]\nThe proxy session capabilities.\n\n(string) --\n\n

    :type ExpiryMinutes: integer
    :param ExpiryMinutes: The number of minutes allowed for the proxy session.

    :rtype: dict

ReturnsResponse Syntax
{
    'ProxySession': {
        'VoiceConnectorId': 'string',
        'ProxySessionId': 'string',
        'Name': 'string',
        'Status': 'Open'|'InProgress'|'Closed',
        'ExpiryMinutes': 123,
        'Capabilities': [
            'Voice'|'SMS',
        ],
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1),
        'EndedTimestamp': datetime(2015, 1, 1),
        'Participants': [
            {
                'PhoneNumber': 'string',
                'ProxyPhoneNumber': 'string'
            },
        ],
        'NumberSelectionBehavior': 'PreferSticky'|'AvoidSticky',
        'GeoMatchLevel': 'Country'|'AreaCode',
        'GeoMatchParams': {
            'Country': 'string',
            'AreaCode': 'string'
        }
    }
}


Response Structure

(dict) --

ProxySession (dict) --
The proxy session details.

VoiceConnectorId (string) --
The Amazon Chime voice connector ID.

ProxySessionId (string) --
The proxy session ID.

Name (string) --
The name of the proxy session.

Status (string) --
The status of the proxy session.

ExpiryMinutes (integer) --
The number of minutes allowed for the proxy session.

Capabilities (list) --
The proxy session capabilities.

(string) --


CreatedTimestamp (datetime) --
The created timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated timestamp, in ISO 8601 format.

EndedTimestamp (datetime) --
The ended timestamp, in ISO 8601 format.

Participants (list) --
The proxy session participants.

(dict) --
The phone number and proxy phone number for a participant in an Amazon Chime Voice Connector proxy session.

PhoneNumber (string) --
The participant\'s phone number.

ProxyPhoneNumber (string) --
The participant\'s proxy phone number.





NumberSelectionBehavior (string) --
The preference for proxy phone number reuse, or stickiness, between the same participants across sessions.

GeoMatchLevel (string) --
The preference for matching the country or area code of the proxy phone number with that of the first participant.

GeoMatchParams (dict) --
The country and area code for the proxy phone number.

Country (string) --
The country.

AreaCode (string) --
The area code.











Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'ProxySession': {
            'VoiceConnectorId': 'string',
            'ProxySessionId': 'string',
            'Name': 'string',
            'Status': 'Open'|'InProgress'|'Closed',
            'ExpiryMinutes': 123,
            'Capabilities': [
                'Voice'|'SMS',
            ],
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1),
            'EndedTimestamp': datetime(2015, 1, 1),
            'Participants': [
                {
                    'PhoneNumber': 'string',
                    'ProxyPhoneNumber': 'string'
                },
            ],
            'NumberSelectionBehavior': 'PreferSticky'|'AvoidSticky',
            'GeoMatchLevel': 'Country'|'AreaCode',
            'GeoMatchParams': {
                'Country': 'string',
                'AreaCode': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_room(AccountId=None, RoomId=None, Name=None):
    """
    Updates room details, such as the room name, for a room in an Amazon Chime Enterprise account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_room(
        AccountId='string',
        RoomId='string',
        Name='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type RoomId: string
    :param RoomId: [REQUIRED]\nThe room ID.\n

    :type Name: string
    :param Name: The room name.

    :rtype: dict

ReturnsResponse Syntax
{
    'Room': {
        'RoomId': 'string',
        'Name': 'string',
        'AccountId': 'string',
        'CreatedBy': 'string',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Room (dict) --
The room details.

RoomId (string) --
The room ID.

Name (string) --
The room name.

AccountId (string) --
The Amazon Chime account ID.

CreatedBy (string) --
The identifier of the room creator.

CreatedTimestamp (datetime) --
The room creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The room update timestamp, in ISO 8601 format.









Exceptions

Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'Room': {
            'RoomId': 'string',
            'Name': 'string',
            'AccountId': 'string',
            'CreatedBy': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_room_membership(AccountId=None, RoomId=None, MemberId=None, Role=None):
    """
    Updates room membership details, such as the member role, for a room in an Amazon Chime Enterprise account. The member role designates whether the member is a chat room administrator or a general chat room member. The member role can be updated only for user IDs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_room_membership(
        AccountId='string',
        RoomId='string',
        MemberId='string',
        Role='Administrator'|'Member'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type RoomId: string
    :param RoomId: [REQUIRED]\nThe room ID.\n

    :type MemberId: string
    :param MemberId: [REQUIRED]\nThe member ID.\n

    :type Role: string
    :param Role: The role of the member.

    :rtype: dict

ReturnsResponse Syntax
{
    'RoomMembership': {
        'RoomId': 'string',
        'Member': {
            'MemberId': 'string',
            'MemberType': 'User'|'Bot'|'Webhook',
            'Email': 'string',
            'FullName': 'string',
            'AccountId': 'string'
        },
        'Role': 'Administrator'|'Member',
        'InvitedBy': 'string',
        'UpdatedTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

RoomMembership (dict) --
The room membership details.

RoomId (string) --
The room ID.

Member (dict) --
The member details, such as email address, name, member ID, and member type.

MemberId (string) --
The member ID (user ID or bot ID).

MemberType (string) --
The member type.

Email (string) --
The member email address.

FullName (string) --
The member name.

AccountId (string) --
The Amazon Chime account ID.



Role (string) --
The membership role.

InvitedBy (string) --
The identifier of the user that invited the room member.

UpdatedTimestamp (datetime) --
The room membership update timestamp, in ISO 8601 format.









Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'RoomMembership': {
            'RoomId': 'string',
            'Member': {
                'MemberId': 'string',
                'MemberType': 'User'|'Bot'|'Webhook',
                'Email': 'string',
                'FullName': 'string',
                'AccountId': 'string'
            },
            'Role': 'Administrator'|'Member',
            'InvitedBy': 'string',
            'UpdatedTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_user(AccountId=None, UserId=None, LicenseType=None, UserType=None, AlexaForBusinessMetadata=None):
    """
    Updates user details for a specified user ID. Currently, only LicenseType updates are supported for this action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user(
        AccountId='string',
        UserId='string',
        LicenseType='Basic'|'Plus'|'Pro'|'ProTrial',
        UserType='PrivateUser'|'SharedDevice',
        AlexaForBusinessMetadata={
            'IsAlexaForBusinessEnabled': True|False,
            'AlexaForBusinessRoomArn': 'string'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type UserId: string
    :param UserId: [REQUIRED]\nThe user ID.\n

    :type LicenseType: string
    :param LicenseType: The user license type to update. This must be a supported license type for the Amazon Chime account that the user belongs to.

    :type UserType: string
    :param UserType: The user type.

    :type AlexaForBusinessMetadata: dict
    :param AlexaForBusinessMetadata: The Alexa for Business metadata.\n\nIsAlexaForBusinessEnabled (boolean) --Starts or stops Alexa for Business.\n\nAlexaForBusinessRoomArn (string) --The ARN of the room resource.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'User': {
        'UserId': 'string',
        'AccountId': 'string',
        'PrimaryEmail': 'string',
        'PrimaryProvisionedNumber': 'string',
        'DisplayName': 'string',
        'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
        'UserType': 'PrivateUser'|'SharedDevice',
        'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
        'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
        'RegisteredOn': datetime(2015, 1, 1),
        'InvitedOn': datetime(2015, 1, 1),
        'AlexaForBusinessMetadata': {
            'IsAlexaForBusinessEnabled': True|False,
            'AlexaForBusinessRoomArn': 'string'
        },
        'PersonalPIN': 'string'
    }
}


Response Structure

(dict) --

User (dict) --
The updated user details.

UserId (string) --
The user ID.

AccountId (string) --
The Amazon Chime account ID.

PrimaryEmail (string) --
The primary email address of the user.

PrimaryProvisionedNumber (string) --
The primary phone number associated with the user.

DisplayName (string) --
The display name of the user.

LicenseType (string) --
The license type for the user.

UserType (string) --
The user type.

UserRegistrationStatus (string) --
The user registration status.

UserInvitationStatus (string) --
The user invite status.

RegisteredOn (datetime) --
Date and time when the user is registered, in ISO 8601 format.

InvitedOn (datetime) --
Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

AlexaForBusinessMetadata (dict) --
The Alexa for Business metadata.

IsAlexaForBusinessEnabled (boolean) --
Starts or stops Alexa for Business.

AlexaForBusinessRoomArn (string) --
The ARN of the room resource.



PersonalPIN (string) --
The user\'s personal meeting PIN.









Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'User': {
            'UserId': 'string',
            'AccountId': 'string',
            'PrimaryEmail': 'string',
            'PrimaryProvisionedNumber': 'string',
            'DisplayName': 'string',
            'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'UserType': 'PrivateUser'|'SharedDevice',
            'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
            'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
            'RegisteredOn': datetime(2015, 1, 1),
            'InvitedOn': datetime(2015, 1, 1),
            'AlexaForBusinessMetadata': {
                'IsAlexaForBusinessEnabled': True|False,
                'AlexaForBusinessRoomArn': 'string'
            },
            'PersonalPIN': 'string'
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_user_settings(AccountId=None, UserId=None, UserSettings=None):
    """
    Updates the settings for the specified user, such as phone number settings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user_settings(
        AccountId='string',
        UserId='string',
        UserSettings={
            'Telephony': {
                'InboundCalling': True|False,
                'OutboundCalling': True|False,
                'SMS': True|False
            }
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe Amazon Chime account ID.\n

    :type UserId: string
    :param UserId: [REQUIRED]\nThe user ID.\n

    :type UserSettings: dict
    :param UserSettings: [REQUIRED]\nThe user settings to update.\n\nTelephony (dict) -- [REQUIRED]The telephony settings associated with the user.\n\nInboundCalling (boolean) -- [REQUIRED]Allows or denies inbound calling.\n\nOutboundCalling (boolean) -- [REQUIRED]Allows or denies outbound calling.\n\nSMS (boolean) -- [REQUIRED]Allows or denies SMS messaging.\n\n\n\n\n

    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_voice_connector(VoiceConnectorId=None, Name=None, RequireEncryption=None):
    """
    Updates details for the specified Amazon Chime Voice Connector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_voice_connector(
        VoiceConnectorId='string',
        Name='string',
        RequireEncryption=True|False
    )
    
    
    :type VoiceConnectorId: string
    :param VoiceConnectorId: [REQUIRED]\nThe Amazon Chime Voice Connector ID.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the Amazon Chime Voice Connector.\n

    :type RequireEncryption: boolean
    :param RequireEncryption: [REQUIRED]\nWhen enabled, requires encryption for the Amazon Chime Voice Connector.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VoiceConnector': {
        'VoiceConnectorId': 'string',
        'AwsRegion': 'us-east-1'|'us-west-2',
        'Name': 'string',
        'OutboundHostName': 'string',
        'RequireEncryption': True|False,
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

VoiceConnector (dict) --
The updated Amazon Chime Voice Connector details.

VoiceConnectorId (string) --
The Amazon Chime Voice Connector ID.

AwsRegion (string) --
The AWS Region in which the Amazon Chime Voice Connector is created. Default: us-east-1 .

Name (string) --
The name of the Amazon Chime Voice Connector.

OutboundHostName (string) --
The outbound host name for the Amazon Chime Voice Connector.

RequireEncryption (boolean) --
Designates whether encryption is required for the Amazon Chime Voice Connector.

CreatedTimestamp (datetime) --
The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.









Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'VoiceConnector': {
            'VoiceConnectorId': 'string',
            'AwsRegion': 'us-east-1'|'us-west-2',
            'Name': 'string',
            'OutboundHostName': 'string',
            'RequireEncryption': True|False,
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

def update_voice_connector_group(VoiceConnectorGroupId=None, Name=None, VoiceConnectorItems=None):
    """
    Updates details for the specified Amazon Chime Voice Connector group, such as the name and Amazon Chime Voice Connector priority ranking.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_voice_connector_group(
        VoiceConnectorGroupId='string',
        Name='string',
        VoiceConnectorItems=[
            {
                'VoiceConnectorId': 'string',
                'Priority': 123
            },
        ]
    )
    
    
    :type VoiceConnectorGroupId: string
    :param VoiceConnectorGroupId: [REQUIRED]\nThe Amazon Chime Voice Connector group ID.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the Amazon Chime Voice Connector group.\n

    :type VoiceConnectorItems: list
    :param VoiceConnectorItems: [REQUIRED]\nThe VoiceConnectorItems to associate with the group.\n\n(dict) --For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to route inbound calls. Includes priority configuration settings. Limit: 3 VoiceConnectorItems per Amazon Chime Voice Connector group.\n\nVoiceConnectorId (string) -- [REQUIRED]The Amazon Chime Voice Connector ID.\n\nPriority (integer) -- [REQUIRED]The priority associated with the Amazon Chime Voice Connector, with 1 being the highest priority. Higher priority Amazon Chime Voice Connectors are attempted first.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VoiceConnectorGroup': {
        'VoiceConnectorGroupId': 'string',
        'Name': 'string',
        'VoiceConnectorItems': [
            {
                'VoiceConnectorId': 'string',
                'Priority': 123
            },
        ],
        'CreatedTimestamp': datetime(2015, 1, 1),
        'UpdatedTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

VoiceConnectorGroup (dict) --
The updated Amazon Chime Voice Connector group details.

VoiceConnectorGroupId (string) --
The Amazon Chime Voice Connector group ID.

Name (string) --
The name of the Amazon Chime Voice Connector group.

VoiceConnectorItems (list) --
The Amazon Chime Voice Connectors to which to route inbound calls.

(dict) --
For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to route inbound calls. Includes priority configuration settings. Limit: 3 VoiceConnectorItems per Amazon Chime Voice Connector group.

VoiceConnectorId (string) --
The Amazon Chime Voice Connector ID.

Priority (integer) --
The priority associated with the Amazon Chime Voice Connector, with 1 being the highest priority. Higher priority Amazon Chime Voice Connectors are attempted first.





CreatedTimestamp (datetime) --
The Amazon Chime Voice Connector group creation timestamp, in ISO 8601 format.

UpdatedTimestamp (datetime) --
The updated Amazon Chime Voice Connector group timestamp, in ISO 8601 format.









Exceptions

Chime.Client.exceptions.UnauthorizedClientException
Chime.Client.exceptions.NotFoundException
Chime.Client.exceptions.ForbiddenException
Chime.Client.exceptions.BadRequestException
Chime.Client.exceptions.ConflictException
Chime.Client.exceptions.ThrottledClientException
Chime.Client.exceptions.ServiceUnavailableException
Chime.Client.exceptions.ServiceFailureException


    :return: {
        'VoiceConnectorGroup': {
            'VoiceConnectorGroupId': 'string',
            'Name': 'string',
            'VoiceConnectorItems': [
                {
                    'VoiceConnectorId': 'string',
                    'Priority': 123
                },
            ],
            'CreatedTimestamp': datetime(2015, 1, 1),
            'UpdatedTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Chime.Client.exceptions.UnauthorizedClientException
    Chime.Client.exceptions.NotFoundException
    Chime.Client.exceptions.ForbiddenException
    Chime.Client.exceptions.BadRequestException
    Chime.Client.exceptions.ConflictException
    Chime.Client.exceptions.ThrottledClientException
    Chime.Client.exceptions.ServiceUnavailableException
    Chime.Client.exceptions.ServiceFailureException
    
    """
    pass

