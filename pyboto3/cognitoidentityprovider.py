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

def add_custom_attributes(UserPoolId=None, CustomAttributes=None):
    """
    Adds additional user attributes to the user pool schema.
    See also: AWS API Documentation
    
    
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

def admin_add_user_to_group(UserPoolId=None, Username=None, GroupName=None):
    """
    Adds the specified user to the specified group.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
    :example: response = client.admin_add_user_to_group(
        UserPoolId='string',
        Username='string',
        GroupName='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool.
            

    :type Username: string
    :param Username: [REQUIRED]
            The username for the user.
            

    :type GroupName: string
    :param GroupName: [REQUIRED]
            The group name.
            

    """
    pass

def admin_confirm_sign_up(UserPoolId=None, Username=None):
    """
    Confirms user registration as an admin without using a confirmation code. Works on any user.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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
    Creates a new user in the specified user pool and sends a welcome message via email or phone (SMS). This message is based on a template that you configured in your call to CreateUserPool or UpdateUserPool . This template includes your custom sign-up instructions and placeholders for user name and temporary password.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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
    :param UserAttributes: An array of name-value pairs that contain user attributes and attribute values to be set for the user to be created. You can create a user without specifying any attributes other than Username . However, any attributes that you specify as required (in CreateUserPool or in the Attributes tab of the console) must be supplied either by you (in your call to AdminCreateUser ) or by the user (when he or she signs up in response to your welcome message).
            For custom attributes, you must prepend the custom: prefix to the attribute name.
            To send a message inviting the user to sign up, you must specify the user's email address or phone number. This can be done in your call to AdminCreateUser or in the Users tab of the Amazon Cognito console for managing your user pools.
            In your call to AdminCreateUser , you can set the email_verified attribute to True , and you can set the phone_number_verified attribute to True . (You can also do this by calling AdminUpdateUserAttributes .)
            email : The email address of the user to whom the message that contains the code and username will be sent. Required if the email_verified attribute is set to True , or if 'EMAIL' is specified in the DesiredDeliveryMediums parameter.
            phone_number : The phone number of the user to whom the message that contains the code and username will be sent. Required if the phone_number_verified attribute is set to True , or if 'SMS' is specified in the DesiredDeliveryMediums parameter.
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
    :param ForceAliasCreation: This parameter is only used if the phone_number_verified or email_verified attribute is set to True . Otherwise, it is ignored.
            If this parameter is set to True and the phone number or email address specified in the UserAttributes parameter already exists as an alias with a different user, the API call will migrate the alias from the previous user to the newly created user. The previous user will no longer be able to log in using that alias.
            If this parameter is set to False , the API throws an AliasExistsException error if the alias already exists. The default value is False .
            

    :type MessageAction: string
    :param MessageAction: Set to 'RESEND' to resend the invitation message to a user that already exists and reset the expiration limit on the user's account. Set to 'SUPPRESS' to suppress sending the message. Only one value can be specified.

    :type DesiredDeliveryMediums: list
    :param DesiredDeliveryMediums: Specify 'EMAIL' if email will be used to send the welcome message. Specify 'SMS' if the phone number will be used. The default value is 'SMS' . More than one value can be specified.
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
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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
            For custom attributes, you must prepend the custom: prefix to the attribute name.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def admin_disable_user(UserPoolId=None, Username=None):
    """
    Disables the specified user as an administrator. Works on any user.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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
    Requires developer credentials.
    See also: AWS API Documentation
    
    
    :example: response = client.admin_enable_user(
        UserPoolId='string',
        Username='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to enable the user.
            

    :type Username: string
    :param Username: [REQUIRED]
            The user name of the user you wish to enable.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def admin_forget_device(UserPoolId=None, Username=None, DeviceKey=None):
    """
    Forgets the device, as an administrator.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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
            The app client ID.
            

    :type AuthFlow: string
    :param AuthFlow: [REQUIRED]
            The authentication flow for this call to execute. The API action will depend on this value. For example:
            REFRESH_TOKEN_AUTH will take in a valid refresh token and return new tokens.
            USER_SRP_AUTH will take in USERNAME and SRPA and return the SRP variables to be used for next challenge execution.
            Valid values include:
            USER_SRP_AUTH : Authentication flow for the Secure Remote Password (SRP) protocol.
            REFRESH_TOKEN_AUTH /REFRESH_TOKEN : Authentication flow for refreshing the access token and ID token by supplying a valid refresh token.
            CUSTOM_AUTH : Custom authentication flow.
            ADMIN_NO_SRP_AUTH : Non-SRP authentication flow; you can pass in the USERNAME and PASSWORD directly if the flow is enabled for calling the app client.
            

    :type AuthParameters: dict
    :param AuthParameters: The authentication parameters. These are inputs corresponding to the AuthFlow that you are invoking. The required values depend on the value of AuthFlow :
            For USER_SRP_AUTH : USERNAME (required), SRPA (required), SECRET_HASH (required if the app client is configured with a client secret), DEVICE_KEY
            For REFRESH_TOKEN_AUTH/REFRESH_TOKEN : USERNAME (required), SECRET_HASH (required if the app client is configured with a client secret), REFRESH_TOKEN (required), DEVICE_KEY
            For ADMIN_NO_SRP_AUTH : USERNAME (required), SECRET_HASH (if app client is configured with client secret), PASSWORD (required), DEVICE_KEY
            For CUSTOM_AUTH : USERNAME (required), SECRET_HASH (if app client is configured with client secret), DEVICE_KEY
            (string) --
            (string) --
            

    :type ClientMetadata: dict
    :param ClientMetadata: This is a random key-value pair map which can contain any key and will be passed to your PreAuthentication Lambda trigger as-is. It can be used to implement additional validations around authentication.
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
    SMS_MFA : Next challenge is to supply an SMS_MFA_CODE , delivered via SMS.
    PASSWORD_VERIFIER : Next challenge is to supply PASSWORD_CLAIM_SIGNATURE , PASSWORD_CLAIM_SECRET_BLOCK , and TIMESTAMP after the client-side SRP calculations.
    CUSTOM_CHALLENGE : This is returned if your custom authentication flow determines that the user should pass another challenge before tokens are issued.
    DEVICE_SRP_AUTH : If device tracking was enabled on your user pool and the previous challenges were passed, this challenge is returned so that Amazon Cognito can start tracking this device.
    DEVICE_PASSWORD_VERIFIER : Similar to PASSWORD_VERIFIER , but for devices only.
    ADMIN_NO_SRP_AUTH : This is returned if you need to authenticate with USERNAME and PASSWORD directly. An app client must be enabled to use this flow.
    NEW_PASSWORD_REQUIRED : For users which are required to change their passwords after successful first login. This challenge should be passed with NEW_PASSWORD and any other required attributes.
    
    """
    pass

def admin_list_devices(UserPoolId=None, Username=None, Limit=None, PaginationToken=None):
    """
    Lists devices, as an administrator.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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

def admin_list_groups_for_user(Username=None, UserPoolId=None, Limit=None, NextToken=None):
    """
    Lists the groups that the user belongs to.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
    :example: response = client.admin_list_groups_for_user(
        Username='string',
        UserPoolId='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type Username: string
    :param Username: [REQUIRED]
            The username for the user.
            

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool.
            

    :type Limit: integer
    :param Limit: The limit of the request to list groups.

    :type NextToken: string
    :param NextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'Groups': [
            {
                'GroupName': 'string',
                'UserPoolId': 'string',
                'Description': 'string',
                'RoleArn': 'string',
                'Precedence': 123,
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def admin_remove_user_from_group(UserPoolId=None, Username=None, GroupName=None):
    """
    Removes the specified user from the specified group.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
    :example: response = client.admin_remove_user_from_group(
        UserPoolId='string',
        Username='string',
        GroupName='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool.
            

    :type Username: string
    :param Username: [REQUIRED]
            The username for the user.
            

    :type GroupName: string
    :param GroupName: [REQUIRED]
            The group name.
            

    """
    pass

def admin_reset_user_password(UserPoolId=None, Username=None):
    """
    Resets the specified user's password in a user pool as an administrator. Works on any user.
    When a developer calls this API, the current password is invalidated, so it must be changed. If a user tries to sign in after the API is called, the app will get a PasswordResetRequiredException exception back and should direct the user down the flow to reset the password, which is the same as the forgot password flow. In addition, if the user pool has phone verification selected and a verified phone number exists for the user, or if email verification is selected and a verified email exists for the user, calling this API will also result in sending a message to the end user with the code to change their password.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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
            The app client ID.
            

    :type ChallengeName: string
    :param ChallengeName: [REQUIRED]
            The challenge name. For more information, see AdminInitiateAuth .
            

    :type ChallengeResponses: dict
    :param ChallengeResponses: The challenge responses. These are inputs corresponding to the value of ChallengeName , for example:
            SMS_MFA : SMS_MFA_CODE , USERNAME , SECRET_HASH (if app client is configured with client secret).
            PASSWORD_VERIFIER : PASSWORD_CLAIM_SIGNATURE , PASSWORD_CLAIM_SECRET_BLOCK , TIMESTAMP , USERNAME , SECRET_HASH (if app client is configured with client secret).
            ADMIN_NO_SRP_AUTH : PASSWORD , USERNAME , SECRET_HASH (if app client is configured with client secret).
            NEW_PASSWORD_REQUIRED : NEW_PASSWORD , any other required attributes, USERNAME , SECRET_HASH (if app client is configured with client secret).
            The value of the USERNAME attribute must be the user's actual username, not an alias (such as email address or phone number). To make this easier, the AdminInitiateAuth response includes the actual username value in the USERNAMEUSER_ID_FOR_SRP attribute, even if you specified an alias in your call to AdminInitiateAuth .
            (string) --
            (string) --
            

    :type Session: string
    :param Session: The session which should be passed both ways in challenge-response calls to the service. If InitiateAuth or RespondToAuthChallenge API call determines that the caller needs to go through another challenge, they return a session with other challenge parameters. This session should be passed as it is to the next RespondToAuthChallenge API call.

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
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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
    Requires developer credentials.
    See also: AWS API Documentation
    
    
    :example: response = client.admin_update_device_status(
        UserPoolId='string',
        Username='string',
        DeviceKey='string',
        DeviceRememberedStatus='remembered'|'not_remembered'
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
            

    :type DeviceRememberedStatus: string
    :param DeviceRememberedStatus: The status indicating whether a device has been remembered or not.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def admin_update_user_attributes(UserPoolId=None, Username=None, UserAttributes=None):
    """
    Updates the specified user's attributes, including developer attributes, as an administrator. Works on any user.
    For custom attributes, you must prepend the custom: prefix to the attribute name.
    In addition to updating user attributes, this API can also be used to mark phone and email as verified.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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
            For custom attributes, you must prepend the custom: prefix to the attribute name.
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
    Requires developer credentials.
    See also: AWS API Documentation
    
    
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
    See also: AWS API Documentation
    
    
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
    :param AccessToken: [REQUIRED]
            The access token in the change password request.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def confirm_device(AccessToken=None, DeviceKey=None, DeviceSecretVerifierConfig=None, DeviceName=None):
    """
    Confirms tracking of the device. This API call is the call that begins device tracking.
    See also: AWS API Documentation
    
    
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
    Allows a user to enter a confirmation code to reset a forgotten password.
    See also: AWS API Documentation
    
    
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
            The confirmation code sent by a user's request to retrieve a forgotten password. For more information, see ForgotPassword
            

    :type Password: string
    :param Password: [REQUIRED]
            The password sent by a user's request to retrieve a forgotten password.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def confirm_sign_up(ClientId=None, SecretHash=None, Username=None, ConfirmationCode=None, ForceAliasCreation=None):
    """
    Confirms registration of a user and handles the existing alias from a previous user.
    See also: AWS API Documentation
    
    
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
    :param ForceAliasCreation: Boolean to be specified to force user confirmation irrespective of existing alias. By default set to False . If this parameter is set to True and the phone number/email used for sign up confirmation already exists as an alias with a different user, the API call will migrate the alias from the previous user to the newly created user being confirmed. If set to False , the API will throw an AliasExistsException error.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_group(GroupName=None, UserPoolId=None, Description=None, RoleArn=None, Precedence=None):
    """
    Creates a new group in the specified user pool.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
    :example: response = client.create_group(
        GroupName='string',
        UserPoolId='string',
        Description='string',
        RoleArn='string',
        Precedence=123
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group. Must be unique.
            

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool.
            

    :type Description: string
    :param Description: A string containing the description of the group.

    :type RoleArn: string
    :param RoleArn: The role ARN for the group.

    :type Precedence: integer
    :param Precedence: A nonnegative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. Zero is the highest precedence value. Groups with lower Precedence values take precedence over groups with higher or null Precedence values. If a user belongs to two or more groups, it is the group with the lowest precedence value whose role ARN will be used in the cognito:roles and cognito:preferred_role claims in the user's tokens.
            Two groups can have the same Precedence value. If this happens, neither group takes precedence over the other. If two groups with the same Precedence have the same role ARN, that role is used in the cognito:preferred_role claim in tokens for users in each group. If the two groups have different role ARNs, the cognito:preferred_role claim is not set in users' tokens.
            The default Precedence value is null.
            

    :rtype: dict
    :return: {
        'Group': {
            'GroupName': 'string',
            'UserPoolId': 'string',
            'Description': 'string',
            'RoleArn': 'string',
            'Precedence': 123,
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def create_identity_provider(UserPoolId=None, ProviderName=None, ProviderType=None, ProviderDetails=None, AttributeMapping=None, IdpIdentifiers=None):
    """
    Creates an identity provider for a user pool.
    See also: AWS API Documentation
    
    
    :example: response = client.create_identity_provider(
        UserPoolId='string',
        ProviderName='string',
        ProviderType='SAML',
        ProviderDetails={
            'string': 'string'
        },
        AttributeMapping={
            'string': 'string'
        },
        IdpIdentifiers=[
            'string',
        ]
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            

    :type ProviderName: string
    :param ProviderName: [REQUIRED]
            The identity provider name.
            

    :type ProviderType: string
    :param ProviderType: [REQUIRED]
            The identity provider type.
            

    :type ProviderDetails: dict
    :param ProviderDetails: [REQUIRED]
            The identity provider details, such as MetadataURL and MetadataFile .
            (string) --
            (string) --
            

    :type AttributeMapping: dict
    :param AttributeMapping: A mapping of identity provider attributes to standard and custom user pool attributes.
            (string) --
            (string) --
            

    :type IdpIdentifiers: list
    :param IdpIdentifiers: A list of identity provider identifiers.
            (string) --
            

    :rtype: dict
    :return: {
        'IdentityProvider': {
            'UserPoolId': 'string',
            'ProviderName': 'string',
            'ProviderType': 'SAML',
            'ProviderDetails': {
                'string': 'string'
            },
            'AttributeMapping': {
                'string': 'string'
            },
            'IdpIdentifiers': [
                'string',
            ],
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_user_import_job(JobName=None, UserPoolId=None, CloudWatchLogsRoleArn=None):
    """
    Creates the user import job.
    See also: AWS API Documentation
    
    
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

def create_user_pool(PoolName=None, Policies=None, LambdaConfig=None, AutoVerifiedAttributes=None, AliasAttributes=None, SmsVerificationMessage=None, EmailVerificationMessage=None, EmailVerificationSubject=None, SmsAuthenticationMessage=None, MfaConfiguration=None, DeviceConfiguration=None, EmailConfiguration=None, SmsConfiguration=None, UserPoolTags=None, AdminCreateUserConfig=None, Schema=None):
    """
    Creates a new Amazon Cognito user pool and sets the password policy for the pool.
    See also: AWS API Documentation
    
    
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
        UserPoolTags={
            'string': 'string'
        },
        AdminCreateUserConfig={
            'AllowAdminCreateUserOnly': True|False,
            'UnusedAccountValidityDays': 123,
            'InviteMessageTemplate': {
                'SMSMessage': 'string',
                'EmailMessage': 'string',
                'EmailSubject': 'string'
            }
        },
        Schema=[
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
    
    
    :type PoolName: string
    :param PoolName: [REQUIRED]
            A string used to name the user pool.
            

    :type Policies: dict
    :param Policies: The policies associated with the new user pool.
            PasswordPolicy (dict) --A container for information about the user pool password policy.
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
            SnsCallerArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
            ExternalId (string) --The external ID.
            

    :type UserPoolTags: dict
    :param UserPoolTags: The cost allocation tags for the user pool. For more information, see Adding Cost Allocation Tags to Your User Pool
            (string) --
            (string) --
            

    :type AdminCreateUserConfig: dict
    :param AdminCreateUserConfig: The configuration for AdminCreateUser requests.
            AllowAdminCreateUserOnly (boolean) --Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.
            UnusedAccountValidityDays (integer) --The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call AdminCreateUser again, specifying 'RESEND' for the MessageAction parameter. The default value for this parameter is 7.
            InviteMessageTemplate (dict) --The message template to be used for the welcome message to new users.
            SMSMessage (string) --The message template for SMS messages.
            EmailMessage (string) --The message template for email messages.
            EmailSubject (string) --The subject line for email messages.
            
            

    :type Schema: list
    :param Schema: An array of schema attributes for the new user pool. These attributes can be standard or custom attributes.
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
            'UserPoolTags': {
                'string': 'string'
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

def create_user_pool_client(UserPoolId=None, ClientName=None, GenerateSecret=None, RefreshTokenValidity=None, ReadAttributes=None, WriteAttributes=None, ExplicitAuthFlows=None, SupportedIdentityProviders=None, CallbackURLs=None, LogoutURLs=None, DefaultRedirectURI=None, AllowedOAuthFlows=None, AllowedOAuthScopes=None, AllowedOAuthFlowsUserPoolClient=None):
    """
    Creates the user pool client.
    See also: AWS API Documentation
    
    
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
        ],
        SupportedIdentityProviders=[
            'string',
        ],
        CallbackURLs=[
            'string',
        ],
        LogoutURLs=[
            'string',
        ],
        DefaultRedirectURI='string',
        AllowedOAuthFlows=[
            'code'|'implicit'|'client_credentials',
        ],
        AllowedOAuthScopes=[
            'string',
        ],
        AllowedOAuthFlowsUserPoolClient=True|False
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
    :param RefreshTokenValidity: The time limit, in days, after which the refresh token is no longer valid and cannot be used.

    :type ReadAttributes: list
    :param ReadAttributes: The read attributes.
            (string) --
            

    :type WriteAttributes: list
    :param WriteAttributes: The write attributes.
            (string) --
            

    :type ExplicitAuthFlows: list
    :param ExplicitAuthFlows: The explicit authentication flows.
            (string) --
            

    :type SupportedIdentityProviders: list
    :param SupportedIdentityProviders: A list of provider names for the identity providers that are supported on this client.
            (string) --
            

    :type CallbackURLs: list
    :param CallbackURLs: A list of allowed callback URLs for the identity providers.
            (string) --
            

    :type LogoutURLs: list
    :param LogoutURLs: A list of allowed logout URLs for the identity providers.
            (string) --
            

    :type DefaultRedirectURI: string
    :param DefaultRedirectURI: The default redirect URI. Must be in the CallbackURLs list.

    :type AllowedOAuthFlows: list
    :param AllowedOAuthFlows: Set to code to initiate a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the token endpoint.
            Set to token to specify that the client should get the access token (and, optionally, ID token, based on scopes) directly.
            (string) --
            

    :type AllowedOAuthScopes: list
    :param AllowedOAuthScopes: A list of allowed OAuth scopes. Currently supported values are 'phone' , 'email' , 'openid' , and 'Cognito' .
            (string) --
            

    :type AllowedOAuthFlowsUserPoolClient: boolean
    :param AllowedOAuthFlowsUserPoolClient: Set to True if the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

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
            ],
            'SupportedIdentityProviders': [
                'string',
            ],
            'CallbackURLs': [
                'string',
            ],
            'LogoutURLs': [
                'string',
            ],
            'DefaultRedirectURI': 'string',
            'AllowedOAuthFlows': [
                'code'|'implicit'|'client_credentials',
            ],
            'AllowedOAuthScopes': [
                'string',
            ],
            'AllowedOAuthFlowsUserPoolClient': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_user_pool_domain(Domain=None, UserPoolId=None):
    """
    Creates a new domain for a user pool.
    See also: AWS API Documentation
    
    
    :example: response = client.create_user_pool_domain(
        Domain='string',
        UserPoolId='string'
    )
    
    
    :type Domain: string
    :param Domain: [REQUIRED]
            The domain string.
            

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_group(GroupName=None, UserPoolId=None):
    """
    Deletes a group. Currently only groups with no members can be deleted.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_group(
        GroupName='string',
        UserPoolId='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group.
            

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool.
            

    """
    pass

def delete_identity_provider(UserPoolId=None, ProviderName=None):
    """
    Deletes an identity provider for a user pool.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_identity_provider(
        UserPoolId='string',
        ProviderName='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            

    :type ProviderName: string
    :param ProviderName: [REQUIRED]
            The identity provider name.
            

    """
    pass

def delete_user(AccessToken=None):
    """
    Allows a user to delete one's self.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_user(
        AccessToken='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]
            The access token from a request to delete a user.
            

    """
    pass

def delete_user_attributes(UserAttributeNames=None, AccessToken=None):
    """
    Deletes the attributes for a user.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_user_attributes(
        UserAttributeNames=[
            'string',
        ],
        AccessToken='string'
    )
    
    
    :type UserAttributeNames: list
    :param UserAttributeNames: [REQUIRED]
            An array of strings representing the user attribute names you wish to delete.
            For custom attributes, you must prepend the custom: prefix to the attribute name.
            (string) --
            

    :type AccessToken: string
    :param AccessToken: [REQUIRED]
            The access token used in the request to delete user attributes.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_user_pool(UserPoolId=None):
    """
    Deletes the specified Amazon Cognito user pool.
    See also: AWS API Documentation
    
    
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
    See also: AWS API Documentation
    
    
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

def delete_user_pool_domain(Domain=None, UserPoolId=None):
    """
    Deletes a domain for a user pool.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_user_pool_domain(
        Domain='string',
        UserPoolId='string'
    )
    
    
    :type Domain: string
    :param Domain: [REQUIRED]
            The domain string.
            

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_identity_provider(UserPoolId=None, ProviderName=None):
    """
    Gets information about a specific identity provider.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_identity_provider(
        UserPoolId='string',
        ProviderName='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            

    :type ProviderName: string
    :param ProviderName: [REQUIRED]
            The identity provider name.
            

    :rtype: dict
    :return: {
        'IdentityProvider': {
            'UserPoolId': 'string',
            'ProviderName': 'string',
            'ProviderType': 'SAML',
            'ProviderDetails': {
                'string': 'string'
            },
            'AttributeMapping': {
                'string': 'string'
            },
            'IdpIdentifiers': [
                'string',
            ],
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_user_import_job(UserPoolId=None, JobId=None):
    """
    Describes the user import job.
    See also: AWS API Documentation
    
    
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
    See also: AWS API Documentation
    
    
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
            'UserPoolTags': {
                'string': 'string'
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
    See also: AWS API Documentation
    
    
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
            ],
            'SupportedIdentityProviders': [
                'string',
            ],
            'CallbackURLs': [
                'string',
            ],
            'LogoutURLs': [
                'string',
            ],
            'DefaultRedirectURI': 'string',
            'AllowedOAuthFlows': [
                'code'|'implicit'|'client_credentials',
            ],
            'AllowedOAuthScopes': [
                'string',
            ],
            'AllowedOAuthFlowsUserPoolClient': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_user_pool_domain(Domain=None):
    """
    Gets information about a domain.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_user_pool_domain(
        Domain='string'
    )
    
    
    :type Domain: string
    :param Domain: [REQUIRED]
            The domain string.
            

    :rtype: dict
    :return: {
        'DomainDescription': {
            'UserPoolId': 'string',
            'AWSAccountId': 'string',
            'Domain': 'string',
            'S3Bucket': 'string',
            'CloudFrontDistribution': 'string',
            'Version': 'string',
            'Status': 'CREATING'|'DELETING'|'UPDATING'|'ACTIVE'
        }
    }
    
    
    """
    pass

def forget_device(AccessToken=None, DeviceKey=None):
    """
    Forgets the specified device.
    See also: AWS API Documentation
    
    
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
    Calling this API causes a message to be sent to the end user with a confirmation code that is required to change the user's password. For the Username parameter, you can use the username or user alias. If a verified phone number exists for the user, the confirmation code is sent to the phone number. Otherwise, if a verified email exists, the confirmation code is sent to the email. If neither a verified phone number nor a verified email exists, InvalidParameterException is thrown. To use the confirmation code for resetting the password, call ConfirmForgotPassword .
    See also: AWS API Documentation
    
    
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
            The user name of the user for whom you want to enter a code to reset a forgotten password.
            

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
    See also: AWS API Documentation
    
    
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
    See also: AWS API Documentation
    
    
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

def get_group(GroupName=None, UserPoolId=None):
    """
    Gets a group.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
    :example: response = client.get_group(
        GroupName='string',
        UserPoolId='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group.
            

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool.
            

    :rtype: dict
    :return: {
        'Group': {
            'GroupName': 'string',
            'UserPoolId': 'string',
            'Description': 'string',
            'RoleArn': 'string',
            'Precedence': 123,
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_identity_provider_by_identifier(UserPoolId=None, IdpIdentifier=None):
    """
    Gets the specified identity provider.
    See also: AWS API Documentation
    
    
    :example: response = client.get_identity_provider_by_identifier(
        UserPoolId='string',
        IdpIdentifier='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            

    :type IdpIdentifier: string
    :param IdpIdentifier: [REQUIRED]
            The identity provider ID.
            

    :rtype: dict
    :return: {
        'IdentityProvider': {
            'UserPoolId': 'string',
            'ProviderName': 'string',
            'ProviderType': 'SAML',
            'ProviderDetails': {
                'string': 'string'
            },
            'AttributeMapping': {
                'string': 'string'
            },
            'IdpIdentifiers': [
                'string',
            ],
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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
    See also: AWS API Documentation
    
    
    :example: response = client.get_user(
        AccessToken='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]
            The access token returned by the server response to get information about the user.
            

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
    See also: AWS API Documentation
    
    
    :example: response = client.get_user_attribute_verification_code(
        AccessToken='string',
        AttributeName='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]
            The access token returned by the server response to get the user attribute verification code.
            

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
    See also: AWS API Documentation
    
    
    :example: response = client.global_sign_out(
        AccessToken='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]
            The access token.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def initiate_auth(AuthFlow=None, AuthParameters=None, ClientMetadata=None, ClientId=None):
    """
    Initiates the authentication flow.
    See also: AWS API Documentation
    
    
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
            The authentication flow for this call to execute. The API action will depend on this value. For example:
            REFRESH_TOKEN_AUTH will take in a valid refresh token and return new tokens.
            USER_SRP_AUTH will take in USERNAME and SRPA and return the SRP variables to be used for next challenge execution.
            Valid values include:
            USER_SRP_AUTH : Authentication flow for the Secure Remote Password (SRP) protocol.
            REFRESH_TOKEN_AUTH /REFRESH_TOKEN : Authentication flow for refreshing the access token and ID token by supplying a valid refresh token.
            CUSTOM_AUTH : Custom authentication flow.
            ADMIN_NO_SRP_AUTH is not a valid value.
            

    :type AuthParameters: dict
    :param AuthParameters: The authentication parameters. These are inputs corresponding to the AuthFlow that you are invoking. The required values depend on the value of AuthFlow :
            For USER_SRP_AUTH : USERNAME (required), SRPA (required), SECRET_HASH (required if the app client is configured with a client secret), DEVICE_KEY
            For REFRESH_TOKEN_AUTH/REFRESH_TOKEN : USERNAME (required), SECRET_HASH (required if the app client is configured with a client secret), REFRESH_TOKEN (required), DEVICE_KEY
            For CUSTOM_AUTH : USERNAME (required), SECRET_HASH (if app client is configured with client secret), DEVICE_KEY
            (string) --
            (string) --
            

    :type ClientMetadata: dict
    :param ClientMetadata: This is a random key-value pair map which can contain any key and will be passed to your PreAuthentication Lambda trigger as-is. It can be used to implement additional validations around authentication.
            (string) --
            (string) --
            

    :type ClientId: string
    :param ClientId: [REQUIRED]
            The app client ID.
            

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
    SMS_MFA : Next challenge is to supply an SMS_MFA_CODE , delivered via SMS.
    PASSWORD_VERIFIER : Next challenge is to supply PASSWORD_CLAIM_SIGNATURE , PASSWORD_CLAIM_SECRET_BLOCK , and TIMESTAMP after the client-side SRP calculations.
    CUSTOM_CHALLENGE : This is returned if your custom authentication flow determines that the user should pass another challenge before tokens are issued.
    DEVICE_SRP_AUTH : If device tracking was enabled on your user pool and the previous challenges were passed, this challenge is returned so that Amazon Cognito can start tracking this device.
    DEVICE_PASSWORD_VERIFIER : Similar to PASSWORD_VERIFIER , but for devices only.
    NEW_PASSWORD_REQUIRED : For users which are required to change their passwords after successful first login. This challenge should be passed with NEW_PASSWORD and any other required attributes.
    
    """
    pass

def list_devices(AccessToken=None, Limit=None, PaginationToken=None):
    """
    Lists the devices.
    See also: AWS API Documentation
    
    
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

def list_groups(UserPoolId=None, Limit=None, NextToken=None):
    """
    Lists the groups associated with a user pool.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
    :example: response = client.list_groups(
        UserPoolId='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool.
            

    :type Limit: integer
    :param Limit: The limit of the request to list groups.

    :type NextToken: string
    :param NextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'Groups': [
            {
                'GroupName': 'string',
                'UserPoolId': 'string',
                'Description': 'string',
                'RoleArn': 'string',
                'Precedence': 123,
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_identity_providers(UserPoolId=None, MaxResults=None, NextToken=None):
    """
    Lists information about all identity providers for a user pool.
    See also: AWS API Documentation
    
    
    :example: response = client.list_identity_providers(
        UserPoolId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of identity providers to return.

    :type NextToken: string
    :param NextToken: A pagination token.

    :rtype: dict
    :return: {
        'Providers': [
            {
                'ProviderName': 'string',
                'ProviderType': 'SAML',
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_user_import_jobs(UserPoolId=None, MaxResults=None, PaginationToken=None):
    """
    Lists the user import jobs.
    See also: AWS API Documentation
    
    
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
    :param PaginationToken: An identifier that was returned from the previous call to ListUserImportJobs , which can be used to return the next set of import jobs in the list.

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
    See also: AWS API Documentation
    
    
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
    See also: AWS API Documentation
    
    
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
    See also: AWS API Documentation
    
    
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
            The user pool ID for the user pool on which the search should be performed.
            

    :type AttributesToGet: list
    :param AttributesToGet: An array of strings, where each string is the name of a user attribute to be returned for each user in the search results. If the array is empty, all attributes are returned.
            (string) --
            

    :type Limit: integer
    :param Limit: Maximum number of users to be returned.

    :type PaginationToken: string
    :param PaginationToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type Filter: string
    :param Filter: A filter string of the form 'AttributeName Filter-Type 'AttributeValue ''. Quotation marks within the filter string must be escaped using the backslash () character. For example, 'family_name = 'Reddy''.
            AttributeName : The name of the attribute to search for. You can only search for one attribute at a time.
            Filter-Type : For an exact match, use =, for example, 'given_name = 'Jon''. For a prefix ('starts with') match, use ^=, for example, 'given_name ^= 'Jon''.
            AttributeValue : The attribute value that must be matched for each user.
            If the filter string is empty, ListUsers returns all users in the user pool.
            You can only search for the following standard attributes:
            username (case-sensitive)
            email
            phone_number
            name
            given_name
            family_name
            preferred_username
            cognito:user_status (called Enabled in the Console) (case-sensitive)
            status (case-insensitive)
            Custom attributes are not searchable.
            For more information, see Searching for Users Using the ListUsers API and Examples of Using the ListUsers API in the Amazon Cognito Developer Guide .
            

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

def list_users_in_group(UserPoolId=None, GroupName=None, Limit=None, NextToken=None):
    """
    Lists the users in the specified group.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
    :example: response = client.list_users_in_group(
        UserPoolId='string',
        GroupName='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool.
            

    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group.
            

    :type Limit: integer
    :param Limit: The limit of the request to list users.

    :type NextToken: string
    :param NextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

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
        'NextToken': 'string'
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
    See also: AWS API Documentation
    
    
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
    See also: AWS API Documentation
    
    
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
            The app client ID.
            

    :type ChallengeName: string
    :param ChallengeName: [REQUIRED]
            The challenge name. For more information, see InitiateAuth .
            ADMIN_NO_SRP_AUTH is not a valid value.
            

    :type Session: string
    :param Session: The session which should be passed both ways in challenge-response calls to the service. If InitiateAuth or RespondToAuthChallenge API call determines that the caller needs to go through another challenge, they return a session with other challenge parameters. This session should be passed as it is to the next RespondToAuthChallenge API call.

    :type ChallengeResponses: dict
    :param ChallengeResponses: The challenge responses. These are inputs corresponding to the value of ChallengeName , for example:
            SMS_MFA : SMS_MFA_CODE , USERNAME , SECRET_HASH (if app client is configured with client secret).
            PASSWORD_VERIFIER : PASSWORD_CLAIM_SIGNATURE , PASSWORD_CLAIM_SECRET_BLOCK , TIMESTAMP , USERNAME , SECRET_HASH (if app client is configured with client secret).
            NEW_PASSWORD_REQUIRED : NEW_PASSWORD , any other required attributes, USERNAME , SECRET_HASH (if app client is configured with client secret).
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
    See also: AWS API Documentation
    
    
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
    See also: AWS API Documentation
    
    
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
            For custom attributes, you must prepend the custom: prefix to the attribute name.
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
        },
        'UserSub': 'string'
    }
    
    
    """
    pass

def start_user_import_job(UserPoolId=None, JobId=None):
    """
    Starts the user import.
    See also: AWS API Documentation
    
    
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
    See also: AWS API Documentation
    
    
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
    See also: AWS API Documentation
    
    
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

def update_group(GroupName=None, UserPoolId=None, Description=None, RoleArn=None, Precedence=None):
    """
    Updates the specified group with the specified attributes.
    Requires developer credentials.
    See also: AWS API Documentation
    
    
    :example: response = client.update_group(
        GroupName='string',
        UserPoolId='string',
        Description='string',
        RoleArn='string',
        Precedence=123
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group.
            

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool.
            

    :type Description: string
    :param Description: A string containing the new description of the group.

    :type RoleArn: string
    :param RoleArn: The new role ARN for the group. This is used for setting the cognito:roles and cognito:preferred_role claims in the token.

    :type Precedence: integer
    :param Precedence: The new precedence value for the group. For more information about this parameter, see CreateGroup .

    :rtype: dict
    :return: {
        'Group': {
            'GroupName': 'string',
            'UserPoolId': 'string',
            'Description': 'string',
            'RoleArn': 'string',
            'Precedence': 123,
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def update_identity_provider(UserPoolId=None, ProviderName=None, ProviderDetails=None, AttributeMapping=None, IdpIdentifiers=None):
    """
    Updates identity provider information for a user pool.
    See also: AWS API Documentation
    
    
    :example: response = client.update_identity_provider(
        UserPoolId='string',
        ProviderName='string',
        ProviderDetails={
            'string': 'string'
        },
        AttributeMapping={
            'string': 'string'
        },
        IdpIdentifiers=[
            'string',
        ]
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            

    :type ProviderName: string
    :param ProviderName: [REQUIRED]
            The identity provider name.
            

    :type ProviderDetails: dict
    :param ProviderDetails: The identity provider details to be updated, such as MetadataURL and MetadataFile .
            (string) --
            (string) --
            

    :type AttributeMapping: dict
    :param AttributeMapping: The identity provider attribute mapping to be changed.
            (string) --
            (string) --
            

    :type IdpIdentifiers: list
    :param IdpIdentifiers: A list of identity provider identifiers.
            (string) --
            

    :rtype: dict
    :return: {
        'IdentityProvider': {
            'UserPoolId': 'string',
            'ProviderName': 'string',
            'ProviderType': 'SAML',
            'ProviderDetails': {
                'string': 'string'
            },
            'AttributeMapping': {
                'string': 'string'
            },
            'IdpIdentifiers': [
                'string',
            ],
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_user_attributes(UserAttributes=None, AccessToken=None):
    """
    Allows a user to update a specific attribute (one at a time).
    See also: AWS API Documentation
    
    
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
            For custom attributes, you must prepend the custom: prefix to the attribute name.
            (dict) --Specifies whether the attribute is standard or custom.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (string) --The value of the attribute.
            
            

    :type AccessToken: string
    :param AccessToken: [REQUIRED]
            The access token for the request to update user attributes.
            

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

def update_user_pool(UserPoolId=None, Policies=None, LambdaConfig=None, AutoVerifiedAttributes=None, SmsVerificationMessage=None, EmailVerificationMessage=None, EmailVerificationSubject=None, SmsAuthenticationMessage=None, MfaConfiguration=None, DeviceConfiguration=None, EmailConfiguration=None, SmsConfiguration=None, UserPoolTags=None, AdminCreateUserConfig=None):
    """
    Updates the specified user pool with the specified attributes.
    See also: AWS API Documentation
    
    
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
        UserPoolTags={
            'string': 'string'
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
            PasswordPolicy (dict) --A container for information about the user pool password policy.
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
    :param EmailVerificationSubject: The subject of the email verification message.

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
            SnsCallerArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
            ExternalId (string) --The external ID.
            

    :type UserPoolTags: dict
    :param UserPoolTags: The cost allocation tags for the user pool. For more information, see Adding Cost Allocation Tags to Your User Pool
            (string) --
            (string) --
            

    :type AdminCreateUserConfig: dict
    :param AdminCreateUserConfig: The configuration for AdminCreateUser requests.
            AllowAdminCreateUserOnly (boolean) --Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.
            UnusedAccountValidityDays (integer) --The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call AdminCreateUser again, specifying 'RESEND' for the MessageAction parameter. The default value for this parameter is 7.
            InviteMessageTemplate (dict) --The message template to be used for the welcome message to new users.
            SMSMessage (string) --The message template for SMS messages.
            EmailMessage (string) --The message template for email messages.
            EmailSubject (string) --The subject line for email messages.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_user_pool_client(UserPoolId=None, ClientId=None, ClientName=None, RefreshTokenValidity=None, ReadAttributes=None, WriteAttributes=None, ExplicitAuthFlows=None, SupportedIdentityProviders=None, CallbackURLs=None, LogoutURLs=None, DefaultRedirectURI=None, AllowedOAuthFlows=None, AllowedOAuthScopes=None, AllowedOAuthFlowsUserPoolClient=None):
    """
    Allows the developer to update the specified user pool client and password policy.
    See also: AWS API Documentation
    
    
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
        ],
        SupportedIdentityProviders=[
            'string',
        ],
        CallbackURLs=[
            'string',
        ],
        LogoutURLs=[
            'string',
        ],
        DefaultRedirectURI='string',
        AllowedOAuthFlows=[
            'code'|'implicit'|'client_credentials',
        ],
        AllowedOAuthScopes=[
            'string',
        ],
        AllowedOAuthFlowsUserPoolClient=True|False
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
    :param RefreshTokenValidity: The time limit, in days, after which the refresh token is no longer valid and cannot be used.

    :type ReadAttributes: list
    :param ReadAttributes: The read-only attributes of the user pool.
            (string) --
            

    :type WriteAttributes: list
    :param WriteAttributes: The writeable attributes of the user pool.
            (string) --
            

    :type ExplicitAuthFlows: list
    :param ExplicitAuthFlows: Explicit authentication flows.
            (string) --
            

    :type SupportedIdentityProviders: list
    :param SupportedIdentityProviders: A list of provider names for the identity providers that are supported on this client.
            (string) --
            

    :type CallbackURLs: list
    :param CallbackURLs: A list of allowed callback URLs for the identity providers.
            (string) --
            

    :type LogoutURLs: list
    :param LogoutURLs: A list ofallowed logout URLs for the identity providers.
            (string) --
            

    :type DefaultRedirectURI: string
    :param DefaultRedirectURI: The default redirect URI. Must be in the CallbackURLs list.

    :type AllowedOAuthFlows: list
    :param AllowedOAuthFlows: Set to code to initiate a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the token endpoint.
            Set to token to specify that the client should get the access token (and, optionally, ID token, based on scopes) directly.
            (string) --
            

    :type AllowedOAuthScopes: list
    :param AllowedOAuthScopes: A list of allowed OAuth scopes. Currently supported values are 'phone' , 'email' , 'openid' , and 'Cognito' .
            (string) --
            

    :type AllowedOAuthFlowsUserPoolClient: boolean
    :param AllowedOAuthFlowsUserPoolClient: Set to TRUE if the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

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
            ],
            'SupportedIdentityProviders': [
                'string',
            ],
            'CallbackURLs': [
                'string',
            ],
            'LogoutURLs': [
                'string',
            ],
            'DefaultRedirectURI': 'string',
            'AllowedOAuthFlows': [
                'code'|'implicit'|'client_credentials',
            ],
            'AllowedOAuthScopes': [
                'string',
            ],
            'AllowedOAuthFlowsUserPoolClient': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def verify_user_attribute(AccessToken=None, AttributeName=None, Code=None):
    """
    Verifies the specified user attributes in the user pool.
    See also: AWS API Documentation
    
    
    :example: response = client.verify_user_attribute(
        AccessToken='string',
        AttributeName='string',
        Code='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]
            Represents the access token of the request to verify user attributes.
            

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

