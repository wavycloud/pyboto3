'''

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

'''

def add_custom_attributes(UserPoolId=None, CustomAttributes=None):
    """
    Adds additional user attributes to the user pool schema.
    
    
    :example: response = client.add_custom_attributes(
        UserPoolId='string',
        CustomAttributes=[
            {
                'Name': 'string',
                'AttributeDataType': 'String'|'Number'|'DateTime'|'Boolean',
                'DeveloperOnlyAttribute': True|False,
                'Mutable': True|False,
                'Required': True|False,
                'NumberAttributeConstraints': {
                    'MinValue': 'string',
                    'MaxValue': 'string'
                },
                'StringAttributeConstraints': {
                    'MinLength': 'string',
                    'MaxLength': 'string'
                }
            },
        ]
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to add custom attributes.
            

    :type CustomAttributes: list
    :param CustomAttributes: [REQUIRED]
            An array of custom attributes, such as Mutable and Name.
            (dict) --Contains information about the schema attribute.
            Name (string) --A schema attribute of the name type.
            AttributeDataType (string) --The attribute data type.
            DeveloperOnlyAttribute (boolean) --Specifies whether the attribute type is developer only.
            Mutable (boolean) --Specifies whether the attribute can be changed once it has been created.
            Required (boolean) --Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.
            NumberAttributeConstraints (dict) --Specifies the constraints for an attribute of the number type.
            MinValue (string) --The minimum value of an attribute that is of the number data type.
            MaxValue (string) --The maximum value of an attribute that is of the number data type.
            StringAttributeConstraints (dict) --Specifies the constraints for an attribute of the string type.
            MinLength (string) --The minimum length of an attribute value of the string type.
            MaxLength (string) --The maximum length of an attribute value of the string type.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def admin_confirm_sign_up(UserPoolId=None, Username=None):
    """
    Confirms user registration as an admin without using a confirmation code. Works on any user.
    
    
    :example: response = client.admin_confirm_sign_up(
        UserPoolId='string',
        Username='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for which you want to confirm user registration.
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name for which you want to confirm user registration.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def admin_create_user(UserPoolId=None, Username=None, UserAttributes=None, ValidationData=None, TemporaryPassword=None, ForceAliasCreation=None, MessageAction=None, DesiredDeliveryMediums=None):
    """
    Creates a new user in the specified user pool and sends a welcome message via email or phone (SMS). This message is based on a template that you configured in your call to CreateUserPool or UpdateUserPool. This template includes your custom sign-up instructions and placeholders for user name and temporary password.
    Requires developer credentials.
    
    
    :example: response = client.admin_create_user(
        UserPoolId='string',
        Username='string',
        UserAttributes=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        ValidationData=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        TemporaryPassword='string',
        ForceAliasCreation=True|False,
        MessageAction='RESEND'|'SUPPRESS',
        DesiredDeliveryMediums=[
            'SMS'|'EMAIL',
        ]
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where the user will be created.
            

    :type Username: string
    :param Username: [REQUIRED]
            The username for the user. Must be unique within the user pool. Must be a UTF-8 string between 1 and 128 characters. After the user is created, the username cannot be changed.
            

    :type UserAttributes: list
    :param UserAttributes: An array of name-value pairs that contain user attributes and attribute values to be set for the user to be created. You can create a user without specifying any attributes other than Username. However, any attributes that you specify as required (in CreateUserPool or in the Attributes tab of the console) must be supplied either by you (in your call to AdminCreateUser) or by the user (when he or she signs up in response to your welcome message).
            To send a message inviting the user to sign up, you must specify the user's email address or phone number. This can be done in your call to AdminCreateUser or in the Users tab of the Amazon Cognito console for managing your user pools.
            In your call to AdminCreateUser, you can set the email_verified attribute to True, and you can set the phone_number_verified attribute to True. (You cannot do this by calling other operations such as AdminUpdateUserAttributes.)
            email : The email address of the user to whom the message that contains the code and username will be sent. Required if the email_verified attribute is set to True, or if 'EMAIL' is specified in the DesiredDeliveryMediums parameter.
            phone_number : The phone number of the user to whom the message that contains the code and username will be sent. Required if the phone_number_verified attribute is set to True, or if 'SMS' is specified in the DesiredDeliveryMediums parameter.
            (dict) --Specifies whether the attribute is standard or custom.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (string) --The value of the attribute.
            
            

    :type ValidationData: list
    :param ValidationData: The user's validation data. This is an array of name-value pairs that contain user attributes and attribute values that you can use for custom validation, such as restricting the types of user accounts that can be registered. For example, you might choose to allow or disallow user sign-up based on the user's domain.
            To configure custom validation, you must create a Pre Sign-up Lambda trigger for the user pool as described in the Amazon Cognito Developer Guide. The Lambda trigger receives the validation data and uses it in the validation process.
            The user's validation data is not persisted.
            (dict) --Specifies whether the attribute is standard or custom.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (string) --The value of the attribute.
            
            

    :type TemporaryPassword: string
    :param TemporaryPassword: The user's temporary password. This password must conform to the password policy that you specified when you created the user pool.
            The temporary password is valid only once. To complete the Admin Create User flow, the user must enter the temporary password in the sign-in page along with a new password to be used in all future sign-ins.
            This parameter is not required. If you do not specify a value, Amazon Cognito generates one for you.
            The temporary password can only be used until the user account expiration limit that you specified when you created the user pool. To reset the account after that time limit, you must call AdminCreateUser again, specifying 'RESEND' for the MessageAction parameter.
            

    :type ForceAliasCreation: boolean
    :param ForceAliasCreation: This parameter is only used if the phone_number_verified or email_verified attribute is set to True. Otherwise, it is ignored.
            If this parameter is set to True and the phone number or email address specified in the UserAttributes parameter already exists as an alias with a different user, the API call will migrate the alias from the previous user to the newly created user. The previous user will no longer be able to log in using that alias.
            If this parameter is set to False, the API throws an AliasExistsException error if the alias already exists. The default value is False.
            

    :type MessageAction: string
    :param MessageAction: Set to 'RESEND' to resend the invitation message to a user that already exists and reset the expiration limit on the user's account. Set to 'SUPPRESS' to suppress sending the message. Only one value can be specified.

    :type DesiredDeliveryMediums: list
    :param DesiredDeliveryMediums: Specify 'EMAIL' if email will be used to send the welcome message. Specify 'SMS' if the phone number will be used. The default value is 'SMS'. More than one value can be specified.
            (string) --
            

    :rtype: dict
    :return: {
        'User': {
            'Username': 'string',
            'Attributes': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            'UserCreateDate': datetime(2015, 1, 1),
            'UserLastModifiedDate': datetime(2015, 1, 1),
            'Enabled': True|False,
            'UserStatus': 'UNCONFIRMED'|'CONFIRMED'|'ARCHIVED'|'COMPROMISED'|'UNKNOWN'|'RESET_REQUIRED'|'FORCE_CHANGE_PASSWORD',
            'MFAOptions': [
                {
                    'DeliveryMedium': 'SMS'|'EMAIL',
                    'AttributeName': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    UNCONFIRMED - User has been created but not confirmed.
    CONFIRMED - User has been confirmed.
    ARCHIVED - User is no longer active.
    COMPROMISED - User is disabled due to a potential security threat.
    UNKNOWN - User status is not known.
    
    """
    pass

def admin_delete_user(UserPoolId=None, Username=None):
    """
    Deletes a user as an administrator. Works on any user.
    
    
    :example: response = client.admin_delete_user(
        UserPoolId='string',
        Username='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to delete the user.
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name of the user you wish to delete.
            

    """
    pass

def admin_delete_user_attributes(UserPoolId=None, Username=None, UserAttributeNames=None):
    """
    Deletes the user attributes in a user pool as an administrator. Works on any user.
    
    
    :example: response = client.admin_delete_user_attributes(
        UserPoolId='string',
        Username='string',
        UserAttributeNames=[
            'string',
        ]
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to delete user attributes.
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name of the user from which you would like to delete attributes.
            

    :type UserAttributeNames: list
    :param UserAttributeNames: [REQUIRED]
            An array of strings representing the user attribute names you wish to delete.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def admin_disable_user(UserPoolId=None, Username=None):
    """
    Disables the specified user as an administrator. Works on any user.
    
    
    :example: response = client.admin_disable_user(
        UserPoolId='string',
        Username='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to disable the user.
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name of the user you wish to disable.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def admin_enable_user(UserPoolId=None, Username=None):
    """
    Enables the specified user as an administrator. Works on any user.
    
    
    :example: response = client.admin_enable_user(
        UserPoolId='string',
        Username='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to enable the user.
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name of the user you wish to ebable.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def admin_forget_device(UserPoolId=None, Username=None, DeviceKey=None):
    """
    Forgets the device, as an administrator.
    
    
    :example: response = client.admin_forget_device(
        UserPoolId='string',
        Username='string',
        DeviceKey='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name.
            

    :type DeviceKey: string
    :param DeviceKey: [REQUIRED]
            The device key.
            

    """
    pass

def admin_get_device(DeviceKey=None, UserPoolId=None, Username=None):
    """
    Gets the device, as an administrator.
    
    
    :example: response = client.admin_get_device(
        DeviceKey='string',
        UserPoolId='string',
        Username='string'
    )
    
    
    :type DeviceKey: string
    :param DeviceKey: [REQUIRED]
            The device key.
            

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name.
            

    :rtype: dict
    :return: {
        'Device': {
            'DeviceKey': 'string',
            'DeviceAttributes': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            'DeviceCreateDate': datetime(2015, 1, 1),
            'DeviceLastModifiedDate': datetime(2015, 1, 1),
            'DeviceLastAuthenticatedDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def admin_get_user(UserPoolId=None, Username=None):
    """
    Gets the specified user by user name in a user pool as an administrator. Works on any user.
    
    
    :example: response = client.admin_get_user(
        UserPoolId='string',
        Username='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to get information about the user.
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name of the user you wish to retrieve.
            

    :rtype: dict
    :return: {
        'Username': 'string',
        'UserAttributes': [
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        'UserCreateDate': datetime(2015, 1, 1),
        'UserLastModifiedDate': datetime(2015, 1, 1),
        'Enabled': True|False,
        'UserStatus': 'UNCONFIRMED'|'CONFIRMED'|'ARCHIVED'|'COMPROMISED'|'UNKNOWN'|'RESET_REQUIRED'|'FORCE_CHANGE_PASSWORD',
        'MFAOptions': [
            {
                'DeliveryMedium': 'SMS'|'EMAIL',
                'AttributeName': 'string'
            },
        ]
    }
    
    
    :returns: 
    UNCONFIRMED - User has been created but not confirmed.
    CONFIRMED - User has been confirmed.
    ARCHIVED - User is no longer active.
    COMPROMISED - User is disabled due to a potential security threat.
    UNKNOWN - User status is not known.
    
    """
    pass

def admin_initiate_auth(UserPoolId=None, ClientId=None, AuthFlow=None, AuthParameters=None, ClientMetadata=None):
    """
    Initiates the authentication flow, as an administrator.
    
    
    :example: response = client.admin_initiate_auth(
        UserPoolId='string',
        ClientId='string',
        AuthFlow='USER_SRP_AUTH'|'REFRESH_TOKEN_AUTH'|'REFRESH_TOKEN'|'CUSTOM_AUTH'|'ADMIN_NO_SRP_AUTH',
        AuthParameters={
            'string': 'string'
        },
        ClientMetadata={
            'string': 'string'
        }
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The ID of the Amazon Cognito user pool.
            

    :type ClientId: string
    :param ClientId: [REQUIRED]
            The client app ID.
            

    :type AuthFlow: string
    :param AuthFlow: [REQUIRED]
            The authentication flow.
            

    :type AuthParameters: dict
    :param AuthParameters: The authentication parameters.
            (string) --
            (string) --
            

    :type ClientMetadata: dict
    :param ClientMetadata: The client app metadata.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'ChallengeName': 'SMS_MFA'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
        'Session': 'string',
        'ChallengeParameters': {
            'string': 'string'
        },
        'AuthenticationResult': {
            'AccessToken': 'string',
            'ExpiresIn': 123,
            'TokenType': 'string',
            'RefreshToken': 'string',
            'IdToken': 'string',
            'NewDeviceMetadata': {
                'DeviceKey': 'string',
                'DeviceGroupKey': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def admin_list_devices(UserPoolId=None, Username=None, Limit=None, PaginationToken=None):
    """
    Lists devices, as an administrator.
    
    
    :example: response = client.admin_list_devices(
        UserPoolId='string',
        Username='string',
        Limit=123,
        PaginationToken='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name.
            

    :type Limit: integer
    :param Limit: The limit of the devices request.

    :type PaginationToken: string
    :param PaginationToken: The pagination token.

    :rtype: dict
    :return: {
        'Devices': [
            {
                'DeviceKey': 'string',
                'DeviceAttributes': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'DeviceCreateDate': datetime(2015, 1, 1),
                'DeviceLastModifiedDate': datetime(2015, 1, 1),
                'DeviceLastAuthenticatedDate': datetime(2015, 1, 1)
            },
        ],
        'PaginationToken': 'string'
    }
    
    
    """
    pass

def admin_reset_user_password(UserPoolId=None, Username=None):
    """
    Resets the specified user's password in a user pool as an administrator. Works on any user.
    When a developer calls this API, the current password is invalidated, so it must be changed. If a user tries to sign in after the API is called, the app will get a PasswordResetRequiredException exception back and should direct the user down the flow to reset the password, which is the same as the forgot password flow. In addition, if the user pool has phone verification selected and a verified phone number exists for the user, or if email verification is selected and a verified email exists for the user, calling this API will also result in sending a message to the end user with the code to change their password.
    
    
    :example: response = client.admin_reset_user_password(
        UserPoolId='string',
        Username='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to reset the user's password.
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name of the user whose password you wish to reset.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def admin_respond_to_auth_challenge(UserPoolId=None, ClientId=None, ChallengeName=None, ChallengeResponses=None, Session=None):
    """
    Responds to an authentication challenge, as an administrator.
    
    
    :example: response = client.admin_respond_to_auth_challenge(
        UserPoolId='string',
        ClientId='string',
        ChallengeName='SMS_MFA'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
        ChallengeResponses={
            'string': 'string'
        },
        Session='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The ID of the Amazon Cognito user pool.
            

    :type ClientId: string
    :param ClientId: [REQUIRED]
            The client ID.
            

    :type ChallengeName: string
    :param ChallengeName: [REQUIRED]
            The name of the challenge.
            

    :type ChallengeResponses: dict
    :param ChallengeResponses: The challenge response.
            (string) --
            (string) --
            

    :type Session: string
    :param Session: The session.

    :rtype: dict
    :return: {
        'ChallengeName': 'SMS_MFA'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
        'Session': 'string',
        'ChallengeParameters': {
            'string': 'string'
        },
        'AuthenticationResult': {
            'AccessToken': 'string',
            'ExpiresIn': 123,
            'TokenType': 'string',
            'RefreshToken': 'string',
            'IdToken': 'string',
            'NewDeviceMetadata': {
                'DeviceKey': 'string',
                'DeviceGroupKey': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def admin_set_user_settings(UserPoolId=None, Username=None, MFAOptions=None):
    """
    Sets all the user settings for a specified user name. Works on any user.
    
    
    :example: response = client.admin_set_user_settings(
        UserPoolId='string',
        Username='string',
        MFAOptions=[
            {
                'DeliveryMedium': 'SMS'|'EMAIL',
                'AttributeName': 'string'
            },
        ]
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to set the user's settings, such as MFA options.
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name of the user for whom you wish to set user settings.
            

    :type MFAOptions: list
    :param MFAOptions: [REQUIRED]
            Specifies the options for MFA (e.g., email or phone number).
            (dict) --Specifies the different settings for multi-factor authentication (MFA).
            DeliveryMedium (string) --The delivery medium (email message or SMS message) to send the MFA code.
            AttributeName (string) --The attribute name of the MFA option type.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def admin_update_device_status(UserPoolId=None, Username=None, DeviceKey=None, DeviceRememberedStatus=None):
    """
    Updates the device status as an administrator.
    
    
    :example: response = client.admin_update_device_status(
        UserPoolId='string',
        Username='string',
        DeviceKey='string',
        DeviceRememberedStatus='remembered'|'not_remembered'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name.
            

    :type DeviceKey: string
    :param DeviceKey: [REQUIRED]
            The device key.
            

    :type DeviceRememberedStatus: string
    :param DeviceRememberedStatus: The status indicating whether a device has been remembered or not.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def admin_update_user_attributes(UserPoolId=None, Username=None, UserAttributes=None):
    """
    Updates the specified user's attributes, including developer attributes, as an administrator. Works on any user.
    
    
    :example: response = client.admin_update_user_attributes(
        UserPoolId='string',
        Username='string',
        UserAttributes=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to update user attributes.
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name of the user for whom you want to update user attributes.
            

    :type UserAttributes: list
    :param UserAttributes: [REQUIRED]
            An array of name-value pairs representing user attributes.
            (dict) --Specifies whether the attribute is standard or custom.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (string) --The value of the attribute.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def admin_user_global_sign_out(UserPoolId=None, Username=None):
    """
    Signs out users from all devices, as an administrator.
    
    
    :example: response = client.admin_user_global_sign_out(
        UserPoolId='string',
        Username='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name.
            

    :rtype: dict
    :return: {}
    
    
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

def change_password(PreviousPassword=None, ProposedPassword=None, AccessToken=None):
    """
    Changes the password for a specified user in a user pool.
    
    
    :example: response = client.change_password(
        PreviousPassword='string',
        ProposedPassword='string',
        AccessToken='string'
    )
    
    
    :type PreviousPassword: string
    :param PreviousPassword: [REQUIRED]
            The old password in the change password request.
            

    :type ProposedPassword: string
    :param ProposedPassword: [REQUIRED]
            The new password in the change password request.
            

    :type AccessToken: string
    :param AccessToken: The access token in the change password request.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def confirm_device(AccessToken=None, DeviceKey=None, DeviceSecretVerifierConfig=None, DeviceName=None):
    """
    Confirms tracking of the device. This API call is the call that beings device tracking.
    
    
    :example: response = client.confirm_device(
        AccessToken='string',
        DeviceKey='string',
        DeviceSecretVerifierConfig={
            'PasswordVerifier': 'string',
            'Salt': 'string'
        },
        DeviceName='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]
            The access token.
            

    :type DeviceKey: string
    :param DeviceKey: [REQUIRED]
            The device key.
            

    :type DeviceSecretVerifierConfig: dict
    :param DeviceSecretVerifierConfig: The configuration of the device secret verifier.
            PasswordVerifier (string) --The password verifier.
            Salt (string) --The salt.
            

    :type DeviceName: string
    :param DeviceName: The device name.

    :rtype: dict
    :return: {
        'UserConfirmationNecessary': True|False
    }
    
    
    """
    pass

def confirm_forgot_password(ClientId=None, SecretHash=None, Username=None, ConfirmationCode=None, Password=None):
    """
    Allows a user to enter a code provided when they reset their password to update their password.
    
    
    :example: response = client.confirm_forgot_password(
        ClientId='string',
        SecretHash='string',
        Username='string',
        ConfirmationCode='string',
        Password='string'
    )
    
    
    :type ClientId: string
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            

    :type SecretHash: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

    :type Username: string
    :param Username: [REQUIRED]
            The user name of the user for whom you want to enter a code to retrieve a forgotten password.
            

    :type ConfirmationCode: string
    :param ConfirmationCode: [REQUIRED]
            The confirmation code sent by a user's request to retrieve a forgotten password.
            

    :type Password: string
    :param Password: [REQUIRED]
            The password sent by sent by a user's request to retrieve a forgotten password.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def confirm_sign_up(ClientId=None, SecretHash=None, Username=None, ConfirmationCode=None, ForceAliasCreation=None):
    """
    Confirms registration of a user and handles the existing alias from a previous user.
    
    
    :example: response = client.confirm_sign_up(
        ClientId='string',
        SecretHash='string',
        Username='string',
        ConfirmationCode='string',
        ForceAliasCreation=True|False
    )
    
    
    :type ClientId: string
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            

    :type SecretHash: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

    :type Username: string
    :param Username: [REQUIRED]
            The user name of the user whose registration you wish to confirm.
            

    :type ConfirmationCode: string
    :param ConfirmationCode: [REQUIRED]
            The confirmation code sent by a user's request to confirm registration.
            

    :type ForceAliasCreation: boolean
    :param ForceAliasCreation: Boolean to be specified to force user confirmation irrespective of existing alias. By default set to False. If this parameter is set to True and the phone number/email used for sign up confirmation already exists as an alias with a different user, the API call will migrate the alias from the previous user to the newly created user being confirmed. If set to False, the API will throw an AliasExistsException error.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_user_import_job(JobName=None, UserPoolId=None, CloudWatchLogsRoleArn=None):
    """
    Creates the user import job.
    
    
    :example: response = client.create_user_import_job(
        JobName='string',
        UserPoolId='string',
        CloudWatchLogsRoleArn='string'
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]
            The job name for the user import job.
            

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool that the users are being imported into.
            

    :type CloudWatchLogsRoleArn: string
    :param CloudWatchLogsRoleArn: [REQUIRED]
            The role ARN for the Amazon CloudWatch Logging role for the user import job.
            

    :rtype: dict
    :return: {
        'UserImportJob': {
            'JobName': 'string',
            'JobId': 'string',
            'UserPoolId': 'string',
            'PreSignedUrl': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'StartDate': datetime(2015, 1, 1),
            'CompletionDate': datetime(2015, 1, 1),
            'Status': 'Created'|'Pending'|'InProgress'|'Stopping'|'Expired'|'Stopped'|'Failed'|'Succeeded',
            'CloudWatchLogsRoleArn': 'string',
            'ImportedUsers': 123,
            'SkippedUsers': 123,
            'FailedUsers': 123,
            'CompletionMessage': 'string'
        }
    }
    
    
    :returns: 
    Created - The job was created but not started.
    Pending - A transition state. You have started the job, but it has not begun importing users yet.
    InProgress - The job has started, and users are being imported.
    Stopping - You have stopped the job, but the job has not stopped importing users yet.
    Stopped - You have stopped the job, and the job has stopped importing users.
    Succeeded - The job has completed successfully.
    Failed - The job has stopped due to an error.
    Expired - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started.
    
    """
    pass

def create_user_pool(PoolName=None, Policies=None, LambdaConfig=None, AutoVerifiedAttributes=None, AliasAttributes=None, SmsVerificationMessage=None, EmailVerificationMessage=None, EmailVerificationSubject=None, SmsAuthenticationMessage=None, MfaConfiguration=None, DeviceConfiguration=None, EmailConfiguration=None, SmsConfiguration=None, AdminCreateUserConfig=None):
    """
    Creates a new Amazon Cognito user pool and sets the password policy for the pool.
    
    
    :example: response = client.create_user_pool(
        PoolName='string',
        Policies={
            'PasswordPolicy': {
                'MinimumLength': 123,
                'RequireUppercase': True|False,
                'RequireLowercase': True|False,
                'RequireNumbers': True|False,
                'RequireSymbols': True|False
            }
        },
        LambdaConfig={
            'PreSignUp': 'string',
            'CustomMessage': 'string',
            'PostConfirmation': 'string',
            'PreAuthentication': 'string',
            'PostAuthentication': 'string',
            'DefineAuthChallenge': 'string',
            'CreateAuthChallenge': 'string',
            'VerifyAuthChallengeResponse': 'string'
        },
        AutoVerifiedAttributes=[
            'phone_number'|'email',
        ],
        AliasAttributes=[
            'phone_number'|'email'|'preferred_username',
        ],
        SmsVerificationMessage='string',
        EmailVerificationMessage='string',
        EmailVerificationSubject='string',
        SmsAuthenticationMessage='string',
        MfaConfiguration='OFF'|'ON'|'OPTIONAL',
        DeviceConfiguration={
            'ChallengeRequiredOnNewDevice': True|False,
            'DeviceOnlyRememberedOnUserPrompt': True|False
        },
        EmailConfiguration={
            'SourceArn': 'string',
            'ReplyToEmailAddress': 'string'
        },
        SmsConfiguration={
            'SnsCallerArn': 'string',
            'ExternalId': 'string'
        },
        AdminCreateUserConfig={
            'AllowAdminCreateUserOnly': True|False,
            'UnusedAccountValidityDays': 123,
            'InviteMessageTemplate': {
                'SMSMessage': 'string',
                'EmailMessage': 'string',
                'EmailSubject': 'string'
            }
        }
    )
    
    
    :type PoolName: string
    :param PoolName: [REQUIRED]
            A string used to name the user pool.
            

    :type Policies: dict
    :param Policies: The policies associated with the new user pool.
            PasswordPolicy (dict) --A container with information about the user pool password policy.
            MinimumLength (integer) --The minimum length of the password policy that you have set. Cannot be less than 6.
            RequireUppercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password.
            RequireLowercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password.
            RequireNumbers (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one number in their password.
            RequireSymbols (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password.
            
            

    :type LambdaConfig: dict
    :param LambdaConfig: The Lambda trigger configuration information for the new user pool.
            PreSignUp (string) --A pre-registration AWS Lambda trigger.
            CustomMessage (string) --A custom Message AWS Lambda trigger.
            PostConfirmation (string) --A post-confirmation AWS Lambda trigger.
            PreAuthentication (string) --A pre-authentication AWS Lambda trigger.
            PostAuthentication (string) --A post-authentication AWS Lambda trigger.
            DefineAuthChallenge (string) --Defines the authentication challenge.
            CreateAuthChallenge (string) --Creates an authentication challenge.
            VerifyAuthChallengeResponse (string) --Verifies the authentication challenge response.
            

    :type AutoVerifiedAttributes: list
    :param AutoVerifiedAttributes: The attributes to be auto-verified. Possible values: email , phone_number .
            (string) --
            

    :type AliasAttributes: list
    :param AliasAttributes: Attributes supported as an alias for this user pool. Possible values: phone_number , email , or preferred_username .
            (string) --
            

    :type SmsVerificationMessage: string
    :param SmsVerificationMessage: A string representing the SMS verification message.

    :type EmailVerificationMessage: string
    :param EmailVerificationMessage: A string representing the email verification message.

    :type EmailVerificationSubject: string
    :param EmailVerificationSubject: A string representing the email verification subject.

    :type SmsAuthenticationMessage: string
    :param SmsAuthenticationMessage: A string representing the SMS authentication message.

    :type MfaConfiguration: string
    :param MfaConfiguration: Specifies MFA configuration details.

    :type DeviceConfiguration: dict
    :param DeviceConfiguration: The device configuration.
            ChallengeRequiredOnNewDevice (boolean) --Indicates whether a challenge is required on a new device. Only applicable to a new device.
            DeviceOnlyRememberedOnUserPrompt (boolean) --If true, a device is only remembered on user prompt.
            

    :type EmailConfiguration: dict
    :param EmailConfiguration: The email configuration.
            SourceArn (string) --The Amazon Resource Name (ARN) of the email source.
            ReplyToEmailAddress (string) --The REPLY-TO email address.
            

    :type SmsConfiguration: dict
    :param SmsConfiguration: The SMS configuration.
            SnsCallerArn (string) --The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
            ExternalId (string) --The external ID.
            

    :type AdminCreateUserConfig: dict
    :param AdminCreateUserConfig: The configuration for AdminCreateUser requests.
            AllowAdminCreateUserOnly (boolean) --Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.
            UnusedAccountValidityDays (integer) --The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call AdminCreateUser again, specifying 'RESEND' for the MessageAction parameter.
            InviteMessageTemplate (dict) --The message template to be used for the welcome message to new users.
            SMSMessage (string) --The message template for SMS messages.
            EmailMessage (string) --The message template for email messages.
            EmailSubject (string) --The subject line for email messages.
            
            

    :rtype: dict
    :return: {
        'UserPool': {
            'Id': 'string',
            'Name': 'string',
            'Policies': {
                'PasswordPolicy': {
                    'MinimumLength': 123,
                    'RequireUppercase': True|False,
                    'RequireLowercase': True|False,
                    'RequireNumbers': True|False,
                    'RequireSymbols': True|False
                }
            },
            'LambdaConfig': {
                'PreSignUp': 'string',
                'CustomMessage': 'string',
                'PostConfirmation': 'string',
                'PreAuthentication': 'string',
                'PostAuthentication': 'string',
                'DefineAuthChallenge': 'string',
                'CreateAuthChallenge': 'string',
                'VerifyAuthChallengeResponse': 'string'
            },
            'Status': 'Enabled'|'Disabled',
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1),
            'SchemaAttributes': [
                {
                    'Name': 'string',
                    'AttributeDataType': 'String'|'Number'|'DateTime'|'Boolean',
                    'DeveloperOnlyAttribute': True|False,
                    'Mutable': True|False,
                    'Required': True|False,
                    'NumberAttributeConstraints': {
                        'MinValue': 'string',
                        'MaxValue': 'string'
                    },
                    'StringAttributeConstraints': {
                        'MinLength': 'string',
                        'MaxLength': 'string'
                    }
                },
            ],
            'AutoVerifiedAttributes': [
                'phone_number'|'email',
            ],
            'AliasAttributes': [
                'phone_number'|'email'|'preferred_username',
            ],
            'SmsVerificationMessage': 'string',
            'EmailVerificationMessage': 'string',
            'EmailVerificationSubject': 'string',
            'SmsAuthenticationMessage': 'string',
            'MfaConfiguration': 'OFF'|'ON'|'OPTIONAL',
            'DeviceConfiguration': {
                'ChallengeRequiredOnNewDevice': True|False,
                'DeviceOnlyRememberedOnUserPrompt': True|False
            },
            'EstimatedNumberOfUsers': 123,
            'EmailConfiguration': {
                'SourceArn': 'string',
                'ReplyToEmailAddress': 'string'
            },
            'SmsConfiguration': {
                'SnsCallerArn': 'string',
                'ExternalId': 'string'
            },
            'SmsConfigurationFailure': 'string',
            'EmailConfigurationFailure': 'string',
            'AdminCreateUserConfig': {
                'AllowAdminCreateUserOnly': True|False,
                'UnusedAccountValidityDays': 123,
                'InviteMessageTemplate': {
                    'SMSMessage': 'string',
                    'EmailMessage': 'string',
                    'EmailSubject': 'string'
                }
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_user_pool_client(UserPoolId=None, ClientName=None, GenerateSecret=None, RefreshTokenValidity=None, ReadAttributes=None, WriteAttributes=None, ExplicitAuthFlows=None):
    """
    Creates the user pool client.
    
    
    :example: response = client.create_user_pool_client(
        UserPoolId='string',
        ClientName='string',
        GenerateSecret=True|False,
        RefreshTokenValidity=123,
        ReadAttributes=[
            'string',
        ],
        WriteAttributes=[
            'string',
        ],
        ExplicitAuthFlows=[
            'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY',
        ]
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to create a user pool client.
            

    :type ClientName: string
    :param ClientName: [REQUIRED]
            The client name for the user pool client you would like to create.
            

    :type GenerateSecret: boolean
    :param GenerateSecret: Boolean to specify whether you want to generate a secret for the user pool client being created.

    :type RefreshTokenValidity: integer
    :param RefreshTokenValidity: Refreshes the token validity.

    :type ReadAttributes: list
    :param ReadAttributes: The read attributes.
            (string) --
            

    :type WriteAttributes: list
    :param WriteAttributes: The write attributes.
            (string) --
            

    :type ExplicitAuthFlows: list
    :param ExplicitAuthFlows: The explicit authentication flows.
            (string) --
            

    :rtype: dict
    :return: {
        'UserPoolClient': {
            'UserPoolId': 'string',
            'ClientName': 'string',
            'ClientId': 'string',
            'ClientSecret': 'string',
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1),
            'RefreshTokenValidity': 123,
            'ReadAttributes': [
                'string',
            ],
            'WriteAttributes': [
                'string',
            ],
            'ExplicitAuthFlows': [
                'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_user(AccessToken=None):
    """
    Allows a user to delete one's self.
    
    
    :example: response = client.delete_user(
        AccessToken='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: The access token from a request to delete a user.

    """
    pass

def delete_user_attributes(UserAttributeNames=None, AccessToken=None):
    """
    Deletes the attributes for a user.
    
    
    :example: response = client.delete_user_attributes(
        UserAttributeNames=[
            'string',
        ],
        AccessToken='string'
    )
    
    
    :type UserAttributeNames: list
    :param UserAttributeNames: [REQUIRED]
            An array of strings representing the user attribute names you wish to delete.
            (string) --
            

    :type AccessToken: string
    :param AccessToken: The access token used in the request to delete user attributes.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_user_pool(UserPoolId=None):
    """
    Deletes the specified Amazon Cognito user pool.
    
    
    :example: response = client.delete_user_pool(
        UserPoolId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool you want to delete.
            

    """
    pass

def delete_user_pool_client(UserPoolId=None, ClientId=None):
    """
    Allows the developer to delete the user pool client.
    
    
    :example: response = client.delete_user_pool_client(
        UserPoolId='string',
        ClientId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to delete the client.
            

    :type ClientId: string
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            

    """
    pass

def describe_user_import_job(UserPoolId=None, JobId=None):
    """
    Describes the user import job.
    
    
    :example: response = client.describe_user_import_job(
        UserPoolId='string',
        JobId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool that the users are being imported into.
            

    :type JobId: string
    :param JobId: [REQUIRED]
            The job ID for the user import job.
            

    :rtype: dict
    :return: {
        'UserImportJob': {
            'JobName': 'string',
            'JobId': 'string',
            'UserPoolId': 'string',
            'PreSignedUrl': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'StartDate': datetime(2015, 1, 1),
            'CompletionDate': datetime(2015, 1, 1),
            'Status': 'Created'|'Pending'|'InProgress'|'Stopping'|'Expired'|'Stopped'|'Failed'|'Succeeded',
            'CloudWatchLogsRoleArn': 'string',
            'ImportedUsers': 123,
            'SkippedUsers': 123,
            'FailedUsers': 123,
            'CompletionMessage': 'string'
        }
    }
    
    
    :returns: 
    Created - The job was created but not started.
    Pending - A transition state. You have started the job, but it has not begun importing users yet.
    InProgress - The job has started, and users are being imported.
    Stopping - You have stopped the job, but the job has not stopped importing users yet.
    Stopped - You have stopped the job, and the job has stopped importing users.
    Succeeded - The job has completed successfully.
    Failed - The job has stopped due to an error.
    Expired - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started.
    
    """
    pass

def describe_user_pool(UserPoolId=None):
    """
    Returns the configuration information and metadata of the specified user pool.
    
    
    :example: response = client.describe_user_pool(
        UserPoolId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool you want to describe.
            

    :rtype: dict
    :return: {
        'UserPool': {
            'Id': 'string',
            'Name': 'string',
            'Policies': {
                'PasswordPolicy': {
                    'MinimumLength': 123,
                    'RequireUppercase': True|False,
                    'RequireLowercase': True|False,
                    'RequireNumbers': True|False,
                    'RequireSymbols': True|False
                }
            },
            'LambdaConfig': {
                'PreSignUp': 'string',
                'CustomMessage': 'string',
                'PostConfirmation': 'string',
                'PreAuthentication': 'string',
                'PostAuthentication': 'string',
                'DefineAuthChallenge': 'string',
                'CreateAuthChallenge': 'string',
                'VerifyAuthChallengeResponse': 'string'
            },
            'Status': 'Enabled'|'Disabled',
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1),
            'SchemaAttributes': [
                {
                    'Name': 'string',
                    'AttributeDataType': 'String'|'Number'|'DateTime'|'Boolean',
                    'DeveloperOnlyAttribute': True|False,
                    'Mutable': True|False,
                    'Required': True|False,
                    'NumberAttributeConstraints': {
                        'MinValue': 'string',
                        'MaxValue': 'string'
                    },
                    'StringAttributeConstraints': {
                        'MinLength': 'string',
                        'MaxLength': 'string'
                    }
                },
            ],
            'AutoVerifiedAttributes': [
                'phone_number'|'email',
            ],
            'AliasAttributes': [
                'phone_number'|'email'|'preferred_username',
            ],
            'SmsVerificationMessage': 'string',
            'EmailVerificationMessage': 'string',
            'EmailVerificationSubject': 'string',
            'SmsAuthenticationMessage': 'string',
            'MfaConfiguration': 'OFF'|'ON'|'OPTIONAL',
            'DeviceConfiguration': {
                'ChallengeRequiredOnNewDevice': True|False,
                'DeviceOnlyRememberedOnUserPrompt': True|False
            },
            'EstimatedNumberOfUsers': 123,
            'EmailConfiguration': {
                'SourceArn': 'string',
                'ReplyToEmailAddress': 'string'
            },
            'SmsConfiguration': {
                'SnsCallerArn': 'string',
                'ExternalId': 'string'
            },
            'SmsConfigurationFailure': 'string',
            'EmailConfigurationFailure': 'string',
            'AdminCreateUserConfig': {
                'AllowAdminCreateUserOnly': True|False,
                'UnusedAccountValidityDays': 123,
                'InviteMessageTemplate': {
                    'SMSMessage': 'string',
                    'EmailMessage': 'string',
                    'EmailSubject': 'string'
                }
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_user_pool_client(UserPoolId=None, ClientId=None):
    """
    Client method for returning the configuration information and metadata of the specified user pool client.
    
    
    :example: response = client.describe_user_pool_client(
        UserPoolId='string',
        ClientId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool you want to describe.
            

    :type ClientId: string
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            

    :rtype: dict
    :return: {
        'UserPoolClient': {
            'UserPoolId': 'string',
            'ClientName': 'string',
            'ClientId': 'string',
            'ClientSecret': 'string',
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1),
            'RefreshTokenValidity': 123,
            'ReadAttributes': [
                'string',
            ],
            'WriteAttributes': [
                'string',
            ],
            'ExplicitAuthFlows': [
                'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def forget_device(AccessToken=None, DeviceKey=None):
    """
    Forgets the specified device.
    
    
    :example: response = client.forget_device(
        AccessToken='string',
        DeviceKey='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: The access token for the forgotten device request.

    :type DeviceKey: string
    :param DeviceKey: [REQUIRED]
            The device key.
            

    """
    pass

def forgot_password(ClientId=None, SecretHash=None, Username=None):
    """
    Retrieves the password for the specified client ID or username.
    
    
    :example: response = client.forgot_password(
        ClientId='string',
        SecretHash='string',
        Username='string'
    )
    
    
    :type ClientId: string
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            

    :type SecretHash: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

    :type Username: string
    :param Username: [REQUIRED]
            The user name of the user for whom you want to enter a code to retrieve a forgotten password.
            

    :rtype: dict
    :return: {
        'CodeDeliveryDetails': {
            'Destination': 'string',
            'DeliveryMedium': 'SMS'|'EMAIL',
            'AttributeName': 'string'
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

def get_csv_header(UserPoolId=None):
    """
    Gets the header information for the .csv file to be used as input for the user import job.
    
    
    :example: response = client.get_csv_header(
        UserPoolId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool that the users are to be imported into.
            

    :rtype: dict
    :return: {
        'UserPoolId': 'string',
        'CSVHeader': [
            'string',
        ]
    }
    
    
    """
    pass

def get_device(DeviceKey=None, AccessToken=None):
    """
    Gets the device.
    
    
    :example: response = client.get_device(
        DeviceKey='string',
        AccessToken='string'
    )
    
    
    :type DeviceKey: string
    :param DeviceKey: [REQUIRED]
            The device key.
            

    :type AccessToken: string
    :param AccessToken: The access token.

    :rtype: dict
    :return: {
        'Device': {
            'DeviceKey': 'string',
            'DeviceAttributes': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            'DeviceCreateDate': datetime(2015, 1, 1),
            'DeviceLastModifiedDate': datetime(2015, 1, 1),
            'DeviceLastAuthenticatedDate': datetime(2015, 1, 1)
        }
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

def get_user(AccessToken=None):
    """
    Gets the user attributes and metadata for a user.
    
    
    :example: response = client.get_user(
        AccessToken='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: The access token returned by the server response to get information about the user.

    :rtype: dict
    :return: {
        'Username': 'string',
        'UserAttributes': [
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        'MFAOptions': [
            {
                'DeliveryMedium': 'SMS'|'EMAIL',
                'AttributeName': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_user_attribute_verification_code(AccessToken=None, AttributeName=None):
    """
    Gets the user attribute verification code for the specified attribute name.
    
    
    :example: response = client.get_user_attribute_verification_code(
        AccessToken='string',
        AttributeName='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: The access token returned by the server response to get the user attribute verification code.

    :type AttributeName: string
    :param AttributeName: [REQUIRED]
            The attribute name returned by the server response to get the user attribute verification code.
            

    :rtype: dict
    :return: {
        'CodeDeliveryDetails': {
            'Destination': 'string',
            'DeliveryMedium': 'SMS'|'EMAIL',
            'AttributeName': 'string'
        }
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def global_sign_out(AccessToken=None):
    """
    Signs out users from all devices.
    
    
    :example: response = client.global_sign_out(
        AccessToken='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: The access token.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def initiate_auth(AuthFlow=None, AuthParameters=None, ClientMetadata=None, ClientId=None):
    """
    Initiates the authentication flow.
    
    
    :example: response = client.initiate_auth(
        AuthFlow='USER_SRP_AUTH'|'REFRESH_TOKEN_AUTH'|'REFRESH_TOKEN'|'CUSTOM_AUTH'|'ADMIN_NO_SRP_AUTH',
        AuthParameters={
            'string': 'string'
        },
        ClientMetadata={
            'string': 'string'
        },
        ClientId='string'
    )
    
    
    :type AuthFlow: string
    :param AuthFlow: [REQUIRED]
            The authentication flow.
            

    :type AuthParameters: dict
    :param AuthParameters: The authentication parameters.
            (string) --
            (string) --
            

    :type ClientMetadata: dict
    :param ClientMetadata: The client app's metadata.
            (string) --
            (string) --
            

    :type ClientId: string
    :param ClientId: [REQUIRED]
            The client ID.
            

    :rtype: dict
    :return: {
        'ChallengeName': 'SMS_MFA'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
        'Session': 'string',
        'ChallengeParameters': {
            'string': 'string'
        },
        'AuthenticationResult': {
            'AccessToken': 'string',
            'ExpiresIn': 123,
            'TokenType': 'string',
            'RefreshToken': 'string',
            'IdToken': 'string',
            'NewDeviceMetadata': {
                'DeviceKey': 'string',
                'DeviceGroupKey': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_devices(AccessToken=None, Limit=None, PaginationToken=None):
    """
    Lists the devices.
    
    
    :example: response = client.list_devices(
        AccessToken='string',
        Limit=123,
        PaginationToken='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]
            The access tokens for the request to list devices.
            

    :type Limit: integer
    :param Limit: The limit of the device request.

    :type PaginationToken: string
    :param PaginationToken: The pagination token for the list request.

    :rtype: dict
    :return: {
        'Devices': [
            {
                'DeviceKey': 'string',
                'DeviceAttributes': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'DeviceCreateDate': datetime(2015, 1, 1),
                'DeviceLastModifiedDate': datetime(2015, 1, 1),
                'DeviceLastAuthenticatedDate': datetime(2015, 1, 1)
            },
        ],
        'PaginationToken': 'string'
    }
    
    
    """
    pass

def list_user_import_jobs(UserPoolId=None, MaxResults=None, PaginationToken=None):
    """
    Lists the user import jobs.
    
    
    :example: response = client.list_user_import_jobs(
        UserPoolId='string',
        MaxResults=123,
        PaginationToken='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool that the users are being imported into.
            

    :type MaxResults: integer
    :param MaxResults: [REQUIRED]
            The maximum number of import jobs you want the request to return.
            

    :type PaginationToken: string
    :param PaginationToken: An identifier that was returned from the previous call to ListUserImportJobs, which can be used to return the next set of import jobs in the list.

    :rtype: dict
    :return: {
        'UserImportJobs': [
            {
                'JobName': 'string',
                'JobId': 'string',
                'UserPoolId': 'string',
                'PreSignedUrl': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'StartDate': datetime(2015, 1, 1),
                'CompletionDate': datetime(2015, 1, 1),
                'Status': 'Created'|'Pending'|'InProgress'|'Stopping'|'Expired'|'Stopped'|'Failed'|'Succeeded',
                'CloudWatchLogsRoleArn': 'string',
                'ImportedUsers': 123,
                'SkippedUsers': 123,
                'FailedUsers': 123,
                'CompletionMessage': 'string'
            },
        ],
        'PaginationToken': 'string'
    }
    
    
    :returns: 
    Created - The job was created but not started.
    Pending - A transition state. You have started the job, but it has not begun importing users yet.
    InProgress - The job has started, and users are being imported.
    Stopping - You have stopped the job, but the job has not stopped importing users yet.
    Stopped - You have stopped the job, and the job has stopped importing users.
    Succeeded - The job has completed successfully.
    Failed - The job has stopped due to an error.
    Expired - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started.
    
    """
    pass

def list_user_pool_clients(UserPoolId=None, MaxResults=None, NextToken=None):
    """
    Lists the clients that have been created for the specified user pool.
    
    
    :example: response = client.list_user_pool_clients(
        UserPoolId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to list user pool clients.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of results you want the request to return when listing the user pool clients.

    :type NextToken: string
    :param NextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'UserPoolClients': [
            {
                'ClientId': 'string',
                'UserPoolId': 'string',
                'ClientName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_user_pools(NextToken=None, MaxResults=None):
    """
    Lists the user pools associated with an AWS account.
    
    
    :example: response = client.list_user_pools(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type MaxResults: integer
    :param MaxResults: [REQUIRED]
            The maximum number of results you want the request to return when listing the user pools.
            

    :rtype: dict
    :return: {
        'UserPools': [
            {
                'Id': 'string',
                'Name': 'string',
                'LambdaConfig': {
                    'PreSignUp': 'string',
                    'CustomMessage': 'string',
                    'PostConfirmation': 'string',
                    'PreAuthentication': 'string',
                    'PostAuthentication': 'string',
                    'DefineAuthChallenge': 'string',
                    'CreateAuthChallenge': 'string',
                    'VerifyAuthChallengeResponse': 'string'
                },
                'Status': 'Enabled'|'Disabled',
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_users(UserPoolId=None, AttributesToGet=None, Limit=None, PaginationToken=None, Filter=None):
    """
    Lists the users in the Amazon Cognito user pool.
    
    
    :example: response = client.list_users(
        UserPoolId='string',
        AttributesToGet=[
            'string',
        ],
        Limit=123,
        PaginationToken='string',
        Filter='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for which you want to list users.
            

    :type AttributesToGet: list
    :param AttributesToGet: The attributes to get from the request to list users.
            (string) --
            

    :type Limit: integer
    :param Limit: The limit of the request to list users.

    :type PaginationToken: string
    :param PaginationToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type Filter: string
    :param Filter: The filter for the list users request.

    :rtype: dict
    :return: {
        'Users': [
            {
                'Username': 'string',
                'Attributes': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'UserCreateDate': datetime(2015, 1, 1),
                'UserLastModifiedDate': datetime(2015, 1, 1),
                'Enabled': True|False,
                'UserStatus': 'UNCONFIRMED'|'CONFIRMED'|'ARCHIVED'|'COMPROMISED'|'UNKNOWN'|'RESET_REQUIRED'|'FORCE_CHANGE_PASSWORD',
                'MFAOptions': [
                    {
                        'DeliveryMedium': 'SMS'|'EMAIL',
                        'AttributeName': 'string'
                    },
                ]
            },
        ],
        'PaginationToken': 'string'
    }
    
    
    :returns: 
    UNCONFIRMED - User has been created but not confirmed.
    CONFIRMED - User has been confirmed.
    ARCHIVED - User is no longer active.
    COMPROMISED - User is disabled due to a potential security threat.
    UNKNOWN - User status is not known.
    
    """
    pass

def resend_confirmation_code(ClientId=None, SecretHash=None, Username=None):
    """
    Resends the confirmation (for confirmation of registration) to a specific user in the user pool.
    
    
    :example: response = client.resend_confirmation_code(
        ClientId='string',
        SecretHash='string',
        Username='string'
    )
    
    
    :type ClientId: string
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            

    :type SecretHash: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

    :type Username: string
    :param Username: [REQUIRED]
            The user name of the user to whom you wish to resend a confirmation code.
            

    :rtype: dict
    :return: {
        'CodeDeliveryDetails': {
            'Destination': 'string',
            'DeliveryMedium': 'SMS'|'EMAIL',
            'AttributeName': 'string'
        }
    }
    
    
    """
    pass

def respond_to_auth_challenge(ClientId=None, ChallengeName=None, Session=None, ChallengeResponses=None):
    """
    Responds to the authentication challenge.
    
    
    :example: response = client.respond_to_auth_challenge(
        ClientId='string',
        ChallengeName='SMS_MFA'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
        Session='string',
        ChallengeResponses={
            'string': 'string'
        }
    )
    
    
    :type ClientId: string
    :param ClientId: [REQUIRED]
            The client ID.
            

    :type ChallengeName: string
    :param ChallengeName: [REQUIRED]
            The name of the challenge.
            

    :type Session: string
    :param Session: The session.

    :type ChallengeResponses: dict
    :param ChallengeResponses: The responses to the authentication challenge.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'ChallengeName': 'SMS_MFA'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
        'Session': 'string',
        'ChallengeParameters': {
            'string': 'string'
        },
        'AuthenticationResult': {
            'AccessToken': 'string',
            'ExpiresIn': 123,
            'TokenType': 'string',
            'RefreshToken': 'string',
            'IdToken': 'string',
            'NewDeviceMetadata': {
                'DeviceKey': 'string',
                'DeviceGroupKey': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def set_user_settings(AccessToken=None, MFAOptions=None):
    """
    Sets the user settings like multi-factor authentication (MFA). If MFA is to be removed for a particular attribute pass the attribute with code delivery as null. If null list is passed, all MFA options are removed.
    
    
    :example: response = client.set_user_settings(
        AccessToken='string',
        MFAOptions=[
            {
                'DeliveryMedium': 'SMS'|'EMAIL',
                'AttributeName': 'string'
            },
        ]
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]
            The access token for the set user settings request.
            

    :type MFAOptions: list
    :param MFAOptions: [REQUIRED]
            Specifies the options for MFA (e.g., email or phone number).
            (dict) --Specifies the different settings for multi-factor authentication (MFA).
            DeliveryMedium (string) --The delivery medium (email message or SMS message) to send the MFA code.
            AttributeName (string) --The attribute name of the MFA option type.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def sign_up(ClientId=None, SecretHash=None, Username=None, Password=None, UserAttributes=None, ValidationData=None):
    """
    Registers the user in the specified user pool and creates a user name, password, and user attributes.
    
    
    :example: response = client.sign_up(
        ClientId='string',
        SecretHash='string',
        Username='string',
        Password='string',
        UserAttributes=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        ValidationData=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ClientId: string
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            

    :type SecretHash: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

    :type Username: string
    :param Username: [REQUIRED]
            The user name of the user you wish to register.
            

    :type Password: string
    :param Password: [REQUIRED]
            The password of the user you wish to register.
            

    :type UserAttributes: list
    :param UserAttributes: An array of name-value pairs representing user attributes.
            (dict) --Specifies whether the attribute is standard or custom.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (string) --The value of the attribute.
            
            

    :type ValidationData: list
    :param ValidationData: The validation data in the request to register a user.
            (dict) --Specifies whether the attribute is standard or custom.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (string) --The value of the attribute.
            
            

    :rtype: dict
    :return: {
        'UserConfirmed': True|False,
        'CodeDeliveryDetails': {
            'Destination': 'string',
            'DeliveryMedium': 'SMS'|'EMAIL',
            'AttributeName': 'string'
        }
    }
    
    
    """
    pass

def start_user_import_job(UserPoolId=None, JobId=None):
    """
    Starts the user import.
    
    
    :example: response = client.start_user_import_job(
        UserPoolId='string',
        JobId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool that the users are being imported into.
            

    :type JobId: string
    :param JobId: [REQUIRED]
            The job ID for the user import job.
            

    :rtype: dict
    :return: {
        'UserImportJob': {
            'JobName': 'string',
            'JobId': 'string',
            'UserPoolId': 'string',
            'PreSignedUrl': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'StartDate': datetime(2015, 1, 1),
            'CompletionDate': datetime(2015, 1, 1),
            'Status': 'Created'|'Pending'|'InProgress'|'Stopping'|'Expired'|'Stopped'|'Failed'|'Succeeded',
            'CloudWatchLogsRoleArn': 'string',
            'ImportedUsers': 123,
            'SkippedUsers': 123,
            'FailedUsers': 123,
            'CompletionMessage': 'string'
        }
    }
    
    
    :returns: 
    Created - The job was created but not started.
    Pending - A transition state. You have started the job, but it has not begun importing users yet.
    InProgress - The job has started, and users are being imported.
    Stopping - You have stopped the job, but the job has not stopped importing users yet.
    Stopped - You have stopped the job, and the job has stopped importing users.
    Succeeded - The job has completed successfully.
    Failed - The job has stopped due to an error.
    Expired - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started.
    
    """
    pass

def stop_user_import_job(UserPoolId=None, JobId=None):
    """
    Stops the user import job.
    
    
    :example: response = client.stop_user_import_job(
        UserPoolId='string',
        JobId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool that the users are being imported into.
            

    :type JobId: string
    :param JobId: [REQUIRED]
            The job ID for the user import job.
            

    :rtype: dict
    :return: {
        'UserImportJob': {
            'JobName': 'string',
            'JobId': 'string',
            'UserPoolId': 'string',
            'PreSignedUrl': 'string',
            'CreationDate': datetime(2015, 1, 1),
            'StartDate': datetime(2015, 1, 1),
            'CompletionDate': datetime(2015, 1, 1),
            'Status': 'Created'|'Pending'|'InProgress'|'Stopping'|'Expired'|'Stopped'|'Failed'|'Succeeded',
            'CloudWatchLogsRoleArn': 'string',
            'ImportedUsers': 123,
            'SkippedUsers': 123,
            'FailedUsers': 123,
            'CompletionMessage': 'string'
        }
    }
    
    
    :returns: 
    Created - The job was created but not started.
    Pending - A transition state. You have started the job, but it has not begun importing users yet.
    InProgress - The job has started, and users are being imported.
    Stopping - You have stopped the job, but the job has not stopped importing users yet.
    Stopped - You have stopped the job, and the job has stopped importing users.
    Succeeded - The job has completed successfully.
    Failed - The job has stopped due to an error.
    Expired - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started.
    
    """
    pass

def update_device_status(AccessToken=None, DeviceKey=None, DeviceRememberedStatus=None):
    """
    Updates the device status.
    
    
    :example: response = client.update_device_status(
        AccessToken='string',
        DeviceKey='string',
        DeviceRememberedStatus='remembered'|'not_remembered'
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]
            The access token.
            

    :type DeviceKey: string
    :param DeviceKey: [REQUIRED]
            The device key.
            

    :type DeviceRememberedStatus: string
    :param DeviceRememberedStatus: The status of whether a device is remembered.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_user_attributes(UserAttributes=None, AccessToken=None):
    """
    Allows a user to update a specific attribute (one at a time).
    
    
    :example: response = client.update_user_attributes(
        UserAttributes=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        AccessToken='string'
    )
    
    
    :type UserAttributes: list
    :param UserAttributes: [REQUIRED]
            An array of name-value pairs representing user attributes.
            (dict) --Specifies whether the attribute is standard or custom.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (string) --The value of the attribute.
            
            

    :type AccessToken: string
    :param AccessToken: The access token for the request to update user attributes.

    :rtype: dict
    :return: {
        'CodeDeliveryDetailsList': [
            {
                'Destination': 'string',
                'DeliveryMedium': 'SMS'|'EMAIL',
                'AttributeName': 'string'
            },
        ]
    }
    
    
    """
    pass

def update_user_pool(UserPoolId=None, Policies=None, LambdaConfig=None, AutoVerifiedAttributes=None, SmsVerificationMessage=None, EmailVerificationMessage=None, EmailVerificationSubject=None, SmsAuthenticationMessage=None, MfaConfiguration=None, DeviceConfiguration=None, EmailConfiguration=None, SmsConfiguration=None, AdminCreateUserConfig=None):
    """
    Updates the specified user pool with the specified attributes.
    
    
    :example: response = client.update_user_pool(
        UserPoolId='string',
        Policies={
            'PasswordPolicy': {
                'MinimumLength': 123,
                'RequireUppercase': True|False,
                'RequireLowercase': True|False,
                'RequireNumbers': True|False,
                'RequireSymbols': True|False
            }
        },
        LambdaConfig={
            'PreSignUp': 'string',
            'CustomMessage': 'string',
            'PostConfirmation': 'string',
            'PreAuthentication': 'string',
            'PostAuthentication': 'string',
            'DefineAuthChallenge': 'string',
            'CreateAuthChallenge': 'string',
            'VerifyAuthChallengeResponse': 'string'
        },
        AutoVerifiedAttributes=[
            'phone_number'|'email',
        ],
        SmsVerificationMessage='string',
        EmailVerificationMessage='string',
        EmailVerificationSubject='string',
        SmsAuthenticationMessage='string',
        MfaConfiguration='OFF'|'ON'|'OPTIONAL',
        DeviceConfiguration={
            'ChallengeRequiredOnNewDevice': True|False,
            'DeviceOnlyRememberedOnUserPrompt': True|False
        },
        EmailConfiguration={
            'SourceArn': 'string',
            'ReplyToEmailAddress': 'string'
        },
        SmsConfiguration={
            'SnsCallerArn': 'string',
            'ExternalId': 'string'
        },
        AdminCreateUserConfig={
            'AllowAdminCreateUserOnly': True|False,
            'UnusedAccountValidityDays': 123,
            'InviteMessageTemplate': {
                'SMSMessage': 'string',
                'EmailMessage': 'string',
                'EmailSubject': 'string'
            }
        }
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool you want to update.
            

    :type Policies: dict
    :param Policies: A container with the policies you wish to update in a user pool.
            PasswordPolicy (dict) --A container with information about the user pool password policy.
            MinimumLength (integer) --The minimum length of the password policy that you have set. Cannot be less than 6.
            RequireUppercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password.
            RequireLowercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password.
            RequireNumbers (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one number in their password.
            RequireSymbols (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password.
            
            

    :type LambdaConfig: dict
    :param LambdaConfig: The AWS Lambda configuration information from the request to update the user pool.
            PreSignUp (string) --A pre-registration AWS Lambda trigger.
            CustomMessage (string) --A custom Message AWS Lambda trigger.
            PostConfirmation (string) --A post-confirmation AWS Lambda trigger.
            PreAuthentication (string) --A pre-authentication AWS Lambda trigger.
            PostAuthentication (string) --A post-authentication AWS Lambda trigger.
            DefineAuthChallenge (string) --Defines the authentication challenge.
            CreateAuthChallenge (string) --Creates an authentication challenge.
            VerifyAuthChallengeResponse (string) --Verifies the authentication challenge response.
            

    :type AutoVerifiedAttributes: list
    :param AutoVerifiedAttributes: The attributes that are automatically verified when the Amazon Cognito service makes a request to update user pools.
            (string) --
            

    :type SmsVerificationMessage: string
    :param SmsVerificationMessage: A container with information about the SMS verification message.

    :type EmailVerificationMessage: string
    :param EmailVerificationMessage: The contents of the email verification message.

    :type EmailVerificationSubject: string
    :param EmailVerificationSubject: The subject of the email verfication message.

    :type SmsAuthenticationMessage: string
    :param SmsAuthenticationMessage: The contents of the SMS authentication message.

    :type MfaConfiguration: string
    :param MfaConfiguration: Can be one of the following values:
            OFF - MFA tokens are not required and cannot be specified during user registration.
            ON - MFA tokens are required for all user registrations. You can only specify required when you are initially creating a user pool.
            OPTIONAL - Users have the option when registering to create an MFA token.
            

    :type DeviceConfiguration: dict
    :param DeviceConfiguration: Device configuration.
            ChallengeRequiredOnNewDevice (boolean) --Indicates whether a challenge is required on a new device. Only applicable to a new device.
            DeviceOnlyRememberedOnUserPrompt (boolean) --If true, a device is only remembered on user prompt.
            

    :type EmailConfiguration: dict
    :param EmailConfiguration: Email configuration.
            SourceArn (string) --The Amazon Resource Name (ARN) of the email source.
            ReplyToEmailAddress (string) --The REPLY-TO email address.
            

    :type SmsConfiguration: dict
    :param SmsConfiguration: SMS configuration.
            SnsCallerArn (string) --The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
            ExternalId (string) --The external ID.
            

    :type AdminCreateUserConfig: dict
    :param AdminCreateUserConfig: The configuration for AdminCreateUser requests.
            AllowAdminCreateUserOnly (boolean) --Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.
            UnusedAccountValidityDays (integer) --The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call AdminCreateUser again, specifying 'RESEND' for the MessageAction parameter.
            InviteMessageTemplate (dict) --The message template to be used for the welcome message to new users.
            SMSMessage (string) --The message template for SMS messages.
            EmailMessage (string) --The message template for email messages.
            EmailSubject (string) --The subject line for email messages.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_user_pool_client(UserPoolId=None, ClientId=None, ClientName=None, RefreshTokenValidity=None, ReadAttributes=None, WriteAttributes=None, ExplicitAuthFlows=None):
    """
    Allows the developer to update the specified user pool client and password policy.
    
    
    :example: response = client.update_user_pool_client(
        UserPoolId='string',
        ClientId='string',
        ClientName='string',
        RefreshTokenValidity=123,
        ReadAttributes=[
            'string',
        ],
        WriteAttributes=[
            'string',
        ],
        ExplicitAuthFlows=[
            'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY',
        ]
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to update the user pool client.
            

    :type ClientId: string
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            

    :type ClientName: string
    :param ClientName: The client name from the update user pool client request.

    :type RefreshTokenValidity: integer
    :param RefreshTokenValidity: The validity of the refresh token.

    :type ReadAttributes: list
    :param ReadAttributes: The read-only attributes of the user pool.
            (string) --
            

    :type WriteAttributes: list
    :param WriteAttributes: The writeable attributes of the user pool.
            (string) --
            

    :type ExplicitAuthFlows: list
    :param ExplicitAuthFlows: Explicit authentication flows.
            (string) --
            

    :rtype: dict
    :return: {
        'UserPoolClient': {
            'UserPoolId': 'string',
            'ClientName': 'string',
            'ClientId': 'string',
            'ClientSecret': 'string',
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1),
            'RefreshTokenValidity': 123,
            'ReadAttributes': [
                'string',
            ],
            'WriteAttributes': [
                'string',
            ],
            'ExplicitAuthFlows': [
                'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def verify_user_attribute(AccessToken=None, AttributeName=None, Code=None):
    """
    Verifies the specified user attributes in the user pool.
    
    
    :example: response = client.verify_user_attribute(
        AccessToken='string',
        AttributeName='string',
        Code='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: Represents the access token of the request to verify user attributes.

    :type AttributeName: string
    :param AttributeName: [REQUIRED]
            The attribute name in the request to verify user attributes.
            

    :type Code: string
    :param Code: [REQUIRED]
            The verification code in the request to verify user attributes.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

