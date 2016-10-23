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


def add_custom_attributes(UserPoolId=None, CustomAttributes=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to add custom attributes.
            
    :type UserPoolId: string
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
            
            
    :type CustomAttributes: list
    """
    pass


def admin_confirm_sign_up(UserPoolId=None, Username=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for which you want to confirm user registration.
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The user name for which you want to confirm user registration.
            
    :type Username: string
    """
    pass


def admin_create_user(UserPoolId=None, Username=None, UserAttributes=None, ValidationData=None, TemporaryPassword=None,
                      ForceAliasCreation=None, MessageAction=None, DesiredDeliveryMediums=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where the user will be created.
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The username for the user. Must be unique within the user pool. Must be a UTF-8 string between 1 and 128 characters. After the user is created, the username cannot be changed.
            
    :type Username: string
    :param UserAttributes: An array of name-value pairs that contain user attributes and attribute values to be set for the user to be created. You can create a user without specifying any attributes other than Username. However, any attributes that you specify as required (in CreateUserPool or in the Attributes tab of the console) must be supplied either by you (in your call to AdminCreateUser) or by the user (when he or she signs up in response to your welcome message).
            To send a message inviting the user to sign up, you must specify the user's email address or phone number. This can be done in your call to AdminCreateUser or in the Users tab of the Amazon Cognito console for managing your user pools.
            In your call to AdminCreateUser, you can set the email_verified attribute to True, and you can set the phone_number_verified attribute to True. (You cannot do this by calling other operations such as AdminUpdateUserAttributes.)
            email : The email address of the user to whom the message that contains the code and username will be sent. Required if the email_verified attribute is set to True, or if 'EMAIL' is specified in the DesiredDeliveryMediums parameter.
            phone_number : The phone number of the user to whom the message that contains the code and username will be sent. Required if the phone_number_verified attribute is set to True, or if 'SMS' is specified in the DesiredDeliveryMediums parameter.
            (dict) --Specifies whether the attribute is standard or custom.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (string) --The value of the attribute.
            
            
    :type UserAttributes: list
    :param ValidationData: The user's validation data. This is an array of name-value pairs that contain user attributes and attribute values that you can use for custom validation, such as restricting the types of user accounts that can be registered. For example, you might choose to allow or disallow user sign-up based on the user's domain.
            To configure custom validation, you must create a Pre Sign-up Lambda trigger for the user pool as described in the Amazon Cognito Developer Guide. The Lambda trigger receives the validation data and uses it in the validation process.
            The user's validation data is not persisted.
            (dict) --Specifies whether the attribute is standard or custom.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (string) --The value of the attribute.
            
            
    :type ValidationData: list
    :param TemporaryPassword: The user's temporary password. This password must conform to the password policy that you specified when you created the user pool.
            The temporary password is valid only once. To complete the Admin Create User flow, the user must enter the temporary password in the sign-in page along with a new password to be used in all future sign-ins.
            This parameter is not required. If you do not specify a value, Amazon Cognito generates one for you.
            The temporary password can only be used until the user account expiration limit that you specified when you created the user pool. To reset the account after that time limit, you must call AdminCreateUser again, specifying 'RESEND' for the MessageAction parameter.
            
    :type TemporaryPassword: string
    :param ForceAliasCreation: This parameter is only used if the phone_number_verified or email_verified attribute is set to True. Otherwise, it is ignored.
            If this parameter is set to True and the phone number or email address specified in the UserAttributes parameter already exists as an alias with a different user, the API call will migrate the alias from the previous user to the newly created user. The previous user will no longer be able to log in using that alias.
            If this parameter is set to False, the API throws an AliasExistsException error if the alias already exists. The default value is False.
            
    :type ForceAliasCreation: boolean
    :param MessageAction: Set to 'RESEND' to resend the invitation message to a user that already exists and reset the expiration limit on the user's account. Set to 'SUPPRESS' to suppress sending the message. Only one value can be specified.
    :type MessageAction: string
    :param DesiredDeliveryMediums: Specify 'EMAIL' if email will be used to send the welcome message. Specify 'SMS' if the phone number will be used. The default value is 'SMS'. More than one value can be specified.
            (string) --
            
    :type DesiredDeliveryMediums: list
    """
    pass


def admin_delete_user(UserPoolId=None, Username=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to delete the user.
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The user name of the user you wish to delete.
            
    :type Username: string
    """
    pass


def admin_delete_user_attributes(UserPoolId=None, Username=None, UserAttributeNames=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to delete user attributes.
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The user name of the user from which you would like to delete attributes.
            
    :type Username: string
    :param UserAttributeNames: [REQUIRED]
            An array of strings representing the user attribute names you wish to delete.
            (string) --
            
    :type UserAttributeNames: list
    """
    pass


def admin_disable_user(UserPoolId=None, Username=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to disable the user.
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The user name of the user you wish to disable.
            
    :type Username: string
    """
    pass


def admin_enable_user(UserPoolId=None, Username=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to enable the user.
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The user name of the user you wish to ebable.
            
    :type Username: string
    """
    pass


def admin_forget_device(UserPoolId=None, Username=None, DeviceKey=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The user name.
            
    :type Username: string
    :param DeviceKey: [REQUIRED]
            The device key.
            
    :type DeviceKey: string
    """
    pass


def admin_get_device(DeviceKey=None, UserPoolId=None, Username=None):
    """
    :param DeviceKey: [REQUIRED]
            The device key.
            
    :type DeviceKey: string
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The user name.
            
    :type Username: string
    """
    pass


def admin_get_user(UserPoolId=None, Username=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to get information about the user.
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The user name of the user you wish to retrieve.
            
    :type Username: string
    """
    pass


def admin_initiate_auth(UserPoolId=None, ClientId=None, AuthFlow=None, AuthParameters=None, ClientMetadata=None):
    """
    :param UserPoolId: [REQUIRED]
            The ID of the Amazon Cognito user pool.
            
    :type UserPoolId: string
    :param ClientId: [REQUIRED]
            The client app ID.
            
    :type ClientId: string
    :param AuthFlow: [REQUIRED]
            The authentication flow.
            
    :type AuthFlow: string
    :param AuthParameters: The authentication parameters.
            (string) --
            (string) --
            
    :type AuthParameters: dict
    :param ClientMetadata: The client app metadata.
            (string) --
            (string) --
            
    :type ClientMetadata: dict
    """
    pass


def admin_list_devices(UserPoolId=None, Username=None, Limit=None, PaginationToken=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The user name.
            
    :type Username: string
    :param Limit: The limit of the devices request.
    :type Limit: integer
    :param PaginationToken: The pagination token.
    :type PaginationToken: string
    """
    pass


def admin_reset_user_password(UserPoolId=None, Username=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to reset the user's password.
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The user name of the user whose password you wish to reset.
            
    :type Username: string
    """
    pass


def admin_respond_to_auth_challenge(UserPoolId=None, ClientId=None, ChallengeName=None, ChallengeResponses=None,
                                    Session=None):
    """
    :param UserPoolId: [REQUIRED]
            The ID of the Amazon Cognito user pool.
            
    :type UserPoolId: string
    :param ClientId: [REQUIRED]
            The client ID.
            
    :type ClientId: string
    :param ChallengeName: [REQUIRED]
            The name of the challenge.
            
    :type ChallengeName: string
    :param ChallengeResponses: The challenge response.
            (string) --
            (string) --
            
    :type ChallengeResponses: dict
    :param Session: The session.
    :type Session: string
    """
    pass


def admin_set_user_settings(UserPoolId=None, Username=None, MFAOptions=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to set the user's settings, such as MFA options.
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The user name of the user for whom you wish to set user settings.
            
    :type Username: string
    :param MFAOptions: [REQUIRED]
            Specifies the options for MFA (e.g., email or phone number).
            (dict) --Specifies the different settings for multi-factor authentication (MFA).
            DeliveryMedium (string) --The delivery medium (email message or SMS message) to send the MFA code.
            AttributeName (string) --The attribute name of the MFA option type.
            
            
    :type MFAOptions: list
    """
    pass


def admin_update_device_status(UserPoolId=None, Username=None, DeviceKey=None, DeviceRememberedStatus=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The user name.
            
    :type Username: string
    :param DeviceKey: [REQUIRED]
            The device key.
            
    :type DeviceKey: string
    :param DeviceRememberedStatus: The status indicating whether a device has been remembered or not.
    :type DeviceRememberedStatus: string
    """
    pass


def admin_update_user_attributes(UserPoolId=None, Username=None, UserAttributes=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to update user attributes.
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The user name of the user for whom you want to update user attributes.
            
    :type Username: string
    :param UserAttributes: [REQUIRED]
            An array of name-value pairs representing user attributes.
            (dict) --Specifies whether the attribute is standard or custom.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (string) --The value of the attribute.
            
            
    :type UserAttributes: list
    """
    pass


def admin_user_global_sign_out(UserPoolId=None, Username=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID.
            
    :type UserPoolId: string
    :param Username: [REQUIRED]
            The user name.
            
    :type Username: string
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


def change_password(PreviousPassword=None, ProposedPassword=None, AccessToken=None):
    """
    :param PreviousPassword: [REQUIRED]
            The old password in the change password request.
            
    :type PreviousPassword: string
    :param ProposedPassword: [REQUIRED]
            The new password in the change password request.
            
    :type ProposedPassword: string
    :param AccessToken: The access token in the change password request.
    :type AccessToken: string
    """
    pass


def confirm_device(AccessToken=None, DeviceKey=None, DeviceSecretVerifierConfig=None, DeviceName=None):
    """
    :param AccessToken: [REQUIRED]
            The access token.
            
    :type AccessToken: string
    :param DeviceKey: [REQUIRED]
            The device key.
            
    :type DeviceKey: string
    :param DeviceSecretVerifierConfig: The configuration of the device secret verifier.
            PasswordVerifier (string) --The password verifier.
            Salt (string) --The salt.
            
    :type DeviceSecretVerifierConfig: dict
    :param DeviceName: The device name.
    :type DeviceName: string
    """
    pass


def confirm_forgot_password(ClientId=None, SecretHash=None, Username=None, ConfirmationCode=None, Password=None):
    """
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            
    :type ClientId: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.
    :type SecretHash: string
    :param Username: [REQUIRED]
            The user name of the user for whom you want to enter a code to retrieve a forgotten password.
            
    :type Username: string
    :param ConfirmationCode: [REQUIRED]
            The confirmation code sent by a user's request to retrieve a forgotten password.
            
    :type ConfirmationCode: string
    :param Password: [REQUIRED]
            The password sent by sent by a user's request to retrieve a forgotten password.
            
    :type Password: string
    """
    pass


def confirm_sign_up(ClientId=None, SecretHash=None, Username=None, ConfirmationCode=None, ForceAliasCreation=None):
    """
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            
    :type ClientId: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.
    :type SecretHash: string
    :param Username: [REQUIRED]
            The user name of the user whose registration you wish to confirm.
            
    :type Username: string
    :param ConfirmationCode: [REQUIRED]
            The confirmation code sent by a user's request to confirm registration.
            
    :type ConfirmationCode: string
    :param ForceAliasCreation: Boolean to be specified to force user confirmation irrespective of existing alias. By default set to False. If this parameter is set to True and the phone number/email used for sign up confirmation already exists as an alias with a different user, the API call will migrate the alias from the previous user to the newly created user being confirmed. If set to False, the API will throw an AliasExistsException error.
    :type ForceAliasCreation: boolean
    """
    pass


def create_user_import_job(JobName=None, UserPoolId=None, CloudWatchLogsRoleArn=None):
    """
    :param JobName: [REQUIRED]
            The job name for the user import job.
            
    :type JobName: string
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool that the users are being imported into.
            
    :type UserPoolId: string
    :param CloudWatchLogsRoleArn: [REQUIRED]
            The role ARN for the Amazon CloudWatch Logging role for the user import job.
            
    :type CloudWatchLogsRoleArn: string
    """
    pass


def create_user_pool(PoolName=None, Policies=None, LambdaConfig=None, AutoVerifiedAttributes=None, AliasAttributes=None,
                     SmsVerificationMessage=None, EmailVerificationMessage=None, EmailVerificationSubject=None,
                     SmsAuthenticationMessage=None, MfaConfiguration=None, DeviceConfiguration=None,
                     EmailConfiguration=None, SmsConfiguration=None, AdminCreateUserConfig=None):
    """
    :param PoolName: [REQUIRED]
            A string used to name the user pool.
            
    :type PoolName: string
    :param Policies: The policies associated with the new user pool.
            PasswordPolicy (dict) --A container with information about the user pool password policy.
            MinimumLength (integer) --The minimum length of the password policy that you have set. Cannot be less than 6.
            RequireUppercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password.
            RequireLowercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password.
            RequireNumbers (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one number in their password.
            RequireSymbols (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password.
            
            
    :type Policies: dict
    :param LambdaConfig: The Lambda trigger configuration information for the new user pool.
            PreSignUp (string) --A pre-registration AWS Lambda trigger.
            CustomMessage (string) --A custom Message AWS Lambda trigger.
            PostConfirmation (string) --A post-confirmation AWS Lambda trigger.
            PreAuthentication (string) --A pre-authentication AWS Lambda trigger.
            PostAuthentication (string) --A post-authentication AWS Lambda trigger.
            DefineAuthChallenge (string) --Defines the authentication challenge.
            CreateAuthChallenge (string) --Creates an authentication challenge.
            VerifyAuthChallengeResponse (string) --Verifies the authentication challenge response.
            
    :type LambdaConfig: dict
    :param AutoVerifiedAttributes: The attributes to be auto-verified. Possible values: email , phone_number .
            (string) --
            
    :type AutoVerifiedAttributes: list
    :param AliasAttributes: Attributes supported as an alias for this user pool. Possible values: phone_number , email , or preferred_username .
            (string) --
            
    :type AliasAttributes: list
    :param SmsVerificationMessage: A string representing the SMS verification message.
    :type SmsVerificationMessage: string
    :param EmailVerificationMessage: A string representing the email verification message.
    :type EmailVerificationMessage: string
    :param EmailVerificationSubject: A string representing the email verification subject.
    :type EmailVerificationSubject: string
    :param SmsAuthenticationMessage: A string representing the SMS authentication message.
    :type SmsAuthenticationMessage: string
    :param MfaConfiguration: Specifies MFA configuration details.
    :type MfaConfiguration: string
    :param DeviceConfiguration: The device configuration.
            ChallengeRequiredOnNewDevice (boolean) --Indicates whether a challenge is required on a new device. Only applicable to a new device.
            DeviceOnlyRememberedOnUserPrompt (boolean) --If true, a device is only remembered on user prompt.
            
    :type DeviceConfiguration: dict
    :param EmailConfiguration: The email configuration.
            SourceArn (string) --The Amazon Resource Name (ARN) of the email source.
            ReplyToEmailAddress (string) --The REPLY-TO email address.
            
    :type EmailConfiguration: dict
    :param SmsConfiguration: The SMS configuration.
            SnsCallerArn (string) --The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
            ExternalId (string) --The external ID.
            
    :type SmsConfiguration: dict
    :param AdminCreateUserConfig: The configuration for AdminCreateUser requests.
            AllowAdminCreateUserOnly (boolean) --Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.
            UnusedAccountValidityDays (integer) --The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call AdminCreateUser again, specifying 'RESEND' for the MessageAction parameter.
            InviteMessageTemplate (dict) --The message template to be used for the welcome message to new users.
            SMSMessage (string) --The message template for SMS messages.
            EmailMessage (string) --The message template for email messages.
            EmailSubject (string) --The subject line for email messages.
            
            
    :type AdminCreateUserConfig: dict
    """
    pass


def create_user_pool_client(UserPoolId=None, ClientName=None, GenerateSecret=None, RefreshTokenValidity=None,
                            ReadAttributes=None, WriteAttributes=None, ExplicitAuthFlows=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to create a user pool client.
            
    :type UserPoolId: string
    :param ClientName: [REQUIRED]
            The client name for the user pool client you would like to create.
            
    :type ClientName: string
    :param GenerateSecret: Boolean to specify whether you want to generate a secret for the user pool client being created.
    :type GenerateSecret: boolean
    :param RefreshTokenValidity: Refreshes the token validity.
    :type RefreshTokenValidity: integer
    :param ReadAttributes: The read attributes.
            (string) --
            
    :type ReadAttributes: list
    :param WriteAttributes: The write attributes.
            (string) --
            
    :type WriteAttributes: list
    :param ExplicitAuthFlows: The explicit authentication flows.
            (string) --
            
    :type ExplicitAuthFlows: list
    """
    pass


def delete_user(AccessToken=None):
    """
    :param AccessToken: The access token from a request to delete a user.
            ReturnsNone
            
    :type AccessToken: string
    """
    pass


def delete_user_attributes(UserAttributeNames=None, AccessToken=None):
    """
    :param UserAttributeNames: [REQUIRED]
            An array of strings representing the user attribute names you wish to delete.
            (string) --
            
    :type UserAttributeNames: list
    :param AccessToken: The access token used in the request to delete user attributes.
    :type AccessToken: string
    """
    pass


def delete_user_pool(UserPoolId=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool you want to delete.
            ReturnsNone
            
    :type UserPoolId: string
    """
    pass


def delete_user_pool_client(UserPoolId=None, ClientId=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to delete the client.
            
    :type UserPoolId: string
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            
    :type ClientId: string
    """
    pass


def describe_user_import_job(UserPoolId=None, JobId=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool that the users are being imported into.
            
    :type UserPoolId: string
    :param JobId: [REQUIRED]
            The job ID for the user import job.
            
    :type JobId: string
    """
    pass


def describe_user_pool(UserPoolId=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool you want to describe.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the response to describe the user pool.
            UserPool (dict) --The container of metadata returned by the server to describe the pool.
            Id (string) --The ID of the user pool.
            Name (string) --The name of the user pool.
            Policies (dict) --A container describing the policies associated with a user pool.
            PasswordPolicy (dict) --A container with information about the user pool password policy.
            MinimumLength (integer) --The minimum length of the password policy that you have set. Cannot be less than 6.
            RequireUppercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password.
            RequireLowercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password.
            RequireNumbers (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one number in their password.
            RequireSymbols (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password.
            
            LambdaConfig (dict) --A container describing the AWS Lambda triggers associated with a user pool.
            PreSignUp (string) --A pre-registration AWS Lambda trigger.
            CustomMessage (string) --A custom Message AWS Lambda trigger.
            PostConfirmation (string) --A post-confirmation AWS Lambda trigger.
            PreAuthentication (string) --A pre-authentication AWS Lambda trigger.
            PostAuthentication (string) --A post-authentication AWS Lambda trigger.
            DefineAuthChallenge (string) --Defines the authentication challenge.
            CreateAuthChallenge (string) --Creates an authentication challenge.
            VerifyAuthChallengeResponse (string) --Verifies the authentication challenge response.
            Status (string) --The status of a user pool.
            LastModifiedDate (datetime) --The last modified date of a user pool.
            CreationDate (datetime) --The creation date of a user pool.
            SchemaAttributes (list) --A container with the schema attributes of a user pool.
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
            
            AutoVerifiedAttributes (list) --Specifies the attributes that are auto-verified in a user pool.
            (string) --
            AliasAttributes (list) --Specifies the attributes that are aliased in a user pool.
            (string) --
            SmsVerificationMessage (string) --The contents of the SMS verification message.
            EmailVerificationMessage (string) --The contents of the email verification message.
            EmailVerificationSubject (string) --The subject of the email verification message.
            SmsAuthenticationMessage (string) --The contents of the SMS authentication message.
            MfaConfiguration (string) --Can be one of the following values:
            OFF - MFA tokens are not required and cannot be specified during user registration.
            ON - MFA tokens are required for all user registrations. You can only specify required when you are initially creating a user pool.
            OPTIONAL - Users have the option when registering to create an MFA token.
            DeviceConfiguration (dict) --The device configuration.
            ChallengeRequiredOnNewDevice (boolean) --Indicates whether a challenge is required on a new device. Only applicable to a new device.
            DeviceOnlyRememberedOnUserPrompt (boolean) --If true, a device is only remembered on user prompt.
            EstimatedNumberOfUsers (integer) --A number estimating the size of the user pool.
            EmailConfiguration (dict) --The email configuration.
            SourceArn (string) --The Amazon Resource Name (ARN) of the email source.
            ReplyToEmailAddress (string) --The REPLY-TO email address.
            SmsConfiguration (dict) --The SMS configuration.
            SnsCallerArn (string) --The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
            ExternalId (string) --The external ID.
            SmsConfigurationFailure (string) --The reason why the SMS configuration cannot send the message(s) to your users.
            EmailConfigurationFailure (string) --The reason why the email configuration cannot send the messages to your users.
            AdminCreateUserConfig (dict) --The configuration for AdminCreateUser requests.
            AllowAdminCreateUserOnly (boolean) --Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.
            UnusedAccountValidityDays (integer) --The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call AdminCreateUser again, specifying 'RESEND' for the MessageAction parameter.
            InviteMessageTemplate (dict) --The message template to be used for the welcome message to new users.
            SMSMessage (string) --The message template for SMS messages.
            EmailMessage (string) --The message template for email messages.
            EmailSubject (string) --The subject line for email messages.
            
            
            
            
    :type UserPoolId: string
    """
    pass


def describe_user_pool_client(UserPoolId=None, ClientId=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool you want to describe.
            
    :type UserPoolId: string
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            
    :type ClientId: string
    """
    pass


def forget_device(AccessToken=None, DeviceKey=None):
    """
    :param AccessToken: The access token for the forgotten device request.
    :type AccessToken: string
    :param DeviceKey: [REQUIRED]
            The device key.
            
    :type DeviceKey: string
    """
    pass


def forgot_password(ClientId=None, SecretHash=None, Username=None):
    """
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            
    :type ClientId: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.
    :type SecretHash: string
    :param Username: [REQUIRED]
            The user name of the user for whom you want to enter a code to retrieve a forgotten password.
            
    :type Username: string
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


def get_csv_header(UserPoolId=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool that the users are to be imported into.
            Return typedict
            ReturnsResponse Syntax{
              'UserPoolId': 'string',
              'CSVHeader': [
                'string',
              ]
            }
            Response Structure
            (dict) --Represents the response from the server to the request to get the header information for the .csv file for the user import job.
            UserPoolId (string) --The user pool ID for the user pool that the users are to be imported into.
            CSVHeader (list) --The header information for the .csv file for the user import job.
            (string) --
            
            
    :type UserPoolId: string
    """
    pass


def get_device(DeviceKey=None, AccessToken=None):
    """
    :param DeviceKey: [REQUIRED]
            The device key.
            
    :type DeviceKey: string
    :param AccessToken: The access token.
    :type AccessToken: string
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


def get_user(AccessToken=None):
    """
    :param AccessToken: The access token returned by the server response to get information about the user.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the response from the server from the request to get information about the user.
            Username (string) --The user name of the user you wish to retrieve from the get user request.
            UserAttributes (list) --An array of name-value pairs representing user attributes.
            (dict) --Specifies whether the attribute is standard or custom.
            Name (string) --The name of the attribute.
            Value (string) --The value of the attribute.
            
            MFAOptions (list) --Specifies the options for MFA (e.g., email or phone number).
            (dict) --Specifies the different settings for multi-factor authentication (MFA).
            DeliveryMedium (string) --The delivery medium (email message or SMS message) to send the MFA code.
            AttributeName (string) --The attribute name of the MFA option type.
            
            
            
    :type AccessToken: string
    """
    pass


def get_user_attribute_verification_code(AccessToken=None, AttributeName=None):
    """
    :param AccessToken: The access token returned by the server response to get the user attribute verification code.
    :type AccessToken: string
    :param AttributeName: [REQUIRED]
            The attribute name returned by the server response to get the user attribute verification code.
            
    :type AttributeName: string
    """
    pass


def get_waiter():
    """
    """
    pass


def global_sign_out(AccessToken=None):
    """
    :param AccessToken: The access token.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --The response to the request to sign out all devices.
            
            
    :type AccessToken: string
    """
    pass


def initiate_auth(AuthFlow=None, AuthParameters=None, ClientMetadata=None, ClientId=None):
    """
    :param AuthFlow: [REQUIRED]
            The authentication flow.
            
    :type AuthFlow: string
    :param AuthParameters: The authentication parameters.
            (string) --
            (string) --
            
    :type AuthParameters: dict
    :param ClientMetadata: The client app's metadata.
            (string) --
            (string) --
            
    :type ClientMetadata: dict
    :param ClientId: [REQUIRED]
            The client ID.
            
    :type ClientId: string
    """
    pass


def list_devices(AccessToken=None, Limit=None, PaginationToken=None):
    """
    :param AccessToken: [REQUIRED]
            The access tokens for the request to list devices.
            
    :type AccessToken: string
    :param Limit: The limit of the device request.
    :type Limit: integer
    :param PaginationToken: The pagination token for the list request.
    :type PaginationToken: string
    """
    pass


def list_user_import_jobs(UserPoolId=None, MaxResults=None, PaginationToken=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool that the users are being imported into.
            
    :type UserPoolId: string
    :param MaxResults: [REQUIRED]
            The maximum number of import jobs you want the request to return.
            
    :type MaxResults: integer
    :param PaginationToken: An identifier that was returned from the previous call to ListUserImportJobs, which can be used to return the next set of import jobs in the list.
    :type PaginationToken: string
    """
    pass


def list_user_pool_clients(UserPoolId=None, MaxResults=None, NextToken=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to list user pool clients.
            
    :type UserPoolId: string
    :param MaxResults: The maximum number of results you want the request to return when listing the user pool clients.
    :type MaxResults: integer
    :param NextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
    :type NextToken: string
    """
    pass


def list_user_pools(NextToken=None, MaxResults=None):
    """
    :param NextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
    :type NextToken: string
    :param MaxResults: [REQUIRED]
            The maximum number of results you want the request to return when listing the user pools.
            
    :type MaxResults: integer
    """
    pass


def list_users(UserPoolId=None, AttributesToGet=None, Limit=None, PaginationToken=None, Filter=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for which you want to list users.
            
    :type UserPoolId: string
    :param AttributesToGet: The attributes to get from the request to list users.
            (string) --
            
    :type AttributesToGet: list
    :param Limit: The limit of the request to list users.
    :type Limit: integer
    :param PaginationToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
    :type PaginationToken: string
    :param Filter: The filter for the list users request.
    :type Filter: string
    """
    pass


def resend_confirmation_code(ClientId=None, SecretHash=None, Username=None):
    """
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            
    :type ClientId: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.
    :type SecretHash: string
    :param Username: [REQUIRED]
            The user name of the user to whom you wish to resend a confirmation code.
            
    :type Username: string
    """
    pass


def respond_to_auth_challenge(ClientId=None, ChallengeName=None, Session=None, ChallengeResponses=None):
    """
    :param ClientId: [REQUIRED]
            The client ID.
            
    :type ClientId: string
    :param ChallengeName: [REQUIRED]
            The name of the challenge.
            
    :type ChallengeName: string
    :param Session: The session.
    :type Session: string
    :param ChallengeResponses: The responses to the authentication challenge.
            (string) --
            (string) --
            
    :type ChallengeResponses: dict
    """
    pass


def set_user_settings(AccessToken=None, MFAOptions=None):
    """
    :param AccessToken: [REQUIRED]
            The access token for the set user settings request.
            
    :type AccessToken: string
    :param MFAOptions: [REQUIRED]
            Specifies the options for MFA (e.g., email or phone number).
            (dict) --Specifies the different settings for multi-factor authentication (MFA).
            DeliveryMedium (string) --The delivery medium (email message or SMS message) to send the MFA code.
            AttributeName (string) --The attribute name of the MFA option type.
            
            
    :type MFAOptions: list
    """
    pass


def sign_up(ClientId=None, SecretHash=None, Username=None, Password=None, UserAttributes=None, ValidationData=None):
    """
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            
    :type ClientId: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.
    :type SecretHash: string
    :param Username: [REQUIRED]
            The user name of the user you wish to register.
            
    :type Username: string
    :param Password: [REQUIRED]
            The password of the user you wish to register.
            
    :type Password: string
    :param UserAttributes: An array of name-value pairs representing user attributes.
            (dict) --Specifies whether the attribute is standard or custom.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (string) --The value of the attribute.
            
            
    :type UserAttributes: list
    :param ValidationData: The validation data in the request to register a user.
            (dict) --Specifies whether the attribute is standard or custom.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (string) --The value of the attribute.
            
            
    :type ValidationData: list
    """
    pass


def start_user_import_job(UserPoolId=None, JobId=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool that the users are being imported into.
            
    :type UserPoolId: string
    :param JobId: [REQUIRED]
            The job ID for the user import job.
            
    :type JobId: string
    """
    pass


def stop_user_import_job(UserPoolId=None, JobId=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool that the users are being imported into.
            
    :type UserPoolId: string
    :param JobId: [REQUIRED]
            The job ID for the user import job.
            
    :type JobId: string
    """
    pass


def update_device_status(AccessToken=None, DeviceKey=None, DeviceRememberedStatus=None):
    """
    :param AccessToken: [REQUIRED]
            The access token.
            
    :type AccessToken: string
    :param DeviceKey: [REQUIRED]
            The device key.
            
    :type DeviceKey: string
    :param DeviceRememberedStatus: The status of whether a device is remembered.
    :type DeviceRememberedStatus: string
    """
    pass


def update_user_attributes(UserAttributes=None, AccessToken=None):
    """
    :param UserAttributes: [REQUIRED]
            An array of name-value pairs representing user attributes.
            (dict) --Specifies whether the attribute is standard or custom.
            Name (string) -- [REQUIRED]The name of the attribute.
            Value (string) --The value of the attribute.
            
            
    :type UserAttributes: list
    :param AccessToken: The access token for the request to update user attributes.
    :type AccessToken: string
    """
    pass


def update_user_pool(UserPoolId=None, Policies=None, LambdaConfig=None, AutoVerifiedAttributes=None,
                     SmsVerificationMessage=None, EmailVerificationMessage=None, EmailVerificationSubject=None,
                     SmsAuthenticationMessage=None, MfaConfiguration=None, DeviceConfiguration=None,
                     EmailConfiguration=None, SmsConfiguration=None, AdminCreateUserConfig=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool you want to update.
            
    :type UserPoolId: string
    :param Policies: A container with the policies you wish to update in a user pool.
            PasswordPolicy (dict) --A container with information about the user pool password policy.
            MinimumLength (integer) --The minimum length of the password policy that you have set. Cannot be less than 6.
            RequireUppercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password.
            RequireLowercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password.
            RequireNumbers (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one number in their password.
            RequireSymbols (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password.
            
            
    :type Policies: dict
    :param LambdaConfig: The AWS Lambda configuration information from the request to update the user pool.
            PreSignUp (string) --A pre-registration AWS Lambda trigger.
            CustomMessage (string) --A custom Message AWS Lambda trigger.
            PostConfirmation (string) --A post-confirmation AWS Lambda trigger.
            PreAuthentication (string) --A pre-authentication AWS Lambda trigger.
            PostAuthentication (string) --A post-authentication AWS Lambda trigger.
            DefineAuthChallenge (string) --Defines the authentication challenge.
            CreateAuthChallenge (string) --Creates an authentication challenge.
            VerifyAuthChallengeResponse (string) --Verifies the authentication challenge response.
            
    :type LambdaConfig: dict
    :param AutoVerifiedAttributes: The attributes that are automatically verified when the Amazon Cognito service makes a request to update user pools.
            (string) --
            
    :type AutoVerifiedAttributes: list
    :param SmsVerificationMessage: A container with information about the SMS verification message.
    :type SmsVerificationMessage: string
    :param EmailVerificationMessage: The contents of the email verification message.
    :type EmailVerificationMessage: string
    :param EmailVerificationSubject: The subject of the email verfication message.
    :type EmailVerificationSubject: string
    :param SmsAuthenticationMessage: The contents of the SMS authentication message.
    :type SmsAuthenticationMessage: string
    :param MfaConfiguration: Can be one of the following values:
            OFF - MFA tokens are not required and cannot be specified during user registration.
            ON - MFA tokens are required for all user registrations. You can only specify required when you are initially creating a user pool.
            OPTIONAL - Users have the option when registering to create an MFA token.
            
    :type MfaConfiguration: string
    :param DeviceConfiguration: Device configuration.
            ChallengeRequiredOnNewDevice (boolean) --Indicates whether a challenge is required on a new device. Only applicable to a new device.
            DeviceOnlyRememberedOnUserPrompt (boolean) --If true, a device is only remembered on user prompt.
            
    :type DeviceConfiguration: dict
    :param EmailConfiguration: Email configuration.
            SourceArn (string) --The Amazon Resource Name (ARN) of the email source.
            ReplyToEmailAddress (string) --The REPLY-TO email address.
            
    :type EmailConfiguration: dict
    :param SmsConfiguration: SMS configuration.
            SnsCallerArn (string) --The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
            ExternalId (string) --The external ID.
            
    :type SmsConfiguration: dict
    :param AdminCreateUserConfig: The configuration for AdminCreateUser requests.
            AllowAdminCreateUserOnly (boolean) --Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.
            UnusedAccountValidityDays (integer) --The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call AdminCreateUser again, specifying 'RESEND' for the MessageAction parameter.
            InviteMessageTemplate (dict) --The message template to be used for the welcome message to new users.
            SMSMessage (string) --The message template for SMS messages.
            EmailMessage (string) --The message template for email messages.
            EmailSubject (string) --The subject line for email messages.
            
            
    :type AdminCreateUserConfig: dict
    """
    pass


def update_user_pool_client(UserPoolId=None, ClientId=None, ClientName=None, RefreshTokenValidity=None,
                            ReadAttributes=None, WriteAttributes=None, ExplicitAuthFlows=None):
    """
    :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to update the user pool client.
            
    :type UserPoolId: string
    :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            
    :type ClientId: string
    :param ClientName: The client name from the update user pool client request.
    :type ClientName: string
    :param RefreshTokenValidity: The validity of the refresh token.
    :type RefreshTokenValidity: integer
    :param ReadAttributes: The read-only attributes of the user pool.
            (string) --
            
    :type ReadAttributes: list
    :param WriteAttributes: The writeable attributes of the user pool.
            (string) --
            
    :type WriteAttributes: list
    :param ExplicitAuthFlows: Explicit authentication flows.
            (string) --
            
    :type ExplicitAuthFlows: list
    """
    pass


def verify_user_attribute(AccessToken=None, AttributeName=None, Code=None):
    """
    :param AccessToken: Represents the access token of the request to verify user attributes.
    :type AccessToken: string
    :param AttributeName: [REQUIRED]
            The attribute name in the request to verify user attributes.
            
    :type AttributeName: string
    :param Code: [REQUIRED]
            The verification code in the request to verify user attributes.
            
    :type Code: string
    """
    pass
